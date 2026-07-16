import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("backend_main_metric_scoring", ROOT / "main.py")
main = importlib.util.module_from_spec(spec)
spec.loader.exec_module(main)


def _payload(response):
    return json.loads(response.body.decode("utf-8"))


def _configure(tmp_path, monkeypatch):
    monkeypatch.setattr(main, "WORKSTREAM_DATA_FILE", tmp_path / "workstream_data.json")
    monkeypatch.setattr(main, "_undo_snapshot_before", lambda paths: {})
    monkeypatch.setattr(main, "_undo_snapshot_after", lambda *args, **kwargs: None)
    monkeypatch.setenv("ADMIN_PASSWORD", "secret")
    main._write_workstream_payload(main._default_workstream_payload())


def test_admin_evidence_and_metric_scores_persist_and_export(tmp_path, monkeypatch):
    _configure(tmp_path, monkeypatch)

    evidence = {
        "child_progression": {
            "text": "Repeated Class 10 completion and college transitions are reported.",
            "links": [{"label": "Annual report", "url": "https://example.org/report"}],
        },
        "learning_model": {
            "text": "Level-based remedial groups and monthly assessments are described.",
            "links": [{"label": "Programme page", "url": "https://example.org/programme"}],
        },
        "development_ecosystem": {
            "text": "Residential care includes nutrition, counselling and career guidance.",
            "links": [{"label": "Support page", "url": "https://example.org/support"}],
        },
    }
    updated = _payload(main.workstream_admin_update({
        "password": "secret",
        "pm": "Milan",
        "scoring_reference_url": "https://example.org/scoring-guide",
        "evidence_task_index": 0,
        "metric_evidence": evidence,
    }))
    assert updated["ok"] is True
    assert updated["data"]["scoring_reference_url"] == "https://example.org/scoring-guide"
    assert updated["data"]["pms"]["Milan"]["tasks"][0]["metric_evidence"]["child_progression"]["links"][0]["label"] == "Annual report"

    reasons = {
        "child_progression": "The organisation reports repeated school completion and transitions into college across multiple cohorts, with named progression examples and scholarship support.",
        "learning_model": "The teaching model uses level-based groups, remedial support, regular assessment and individual mentoring rather than relying on one-off workshops or vague claims.",
        "development_ecosystem": "Children receive sustained residential care, nutrition, counselling, sports exposure, career guidance and scholarship support that continues beyond classroom hours.",
    }
    saved = _payload(main.workstream_submit({
        "pm": "Milan",
        "task_index": 0,
        "decision": "4",
        "rank": 4,
        "rank_label": "Strong fit",
        "reason": "Strong overall fit.",
        "metric_scores": {
            key: {"rank": rank, "reason": reasons[key]}
            for key, rank in {
                "child_progression": 4,
                "learning_model": 5,
                "development_ecosystem": 4,
            }.items()
        },
    }))
    assert saved["ok"] is True
    response = saved["data"]["pms"]["Milan"]["responses"]["0"]
    assert response["metric_scores"]["learning_model"]["rank"] == 5
    assert response["metric_scores"]["development_ecosystem"]["reason"].startswith("Children receive")

    exported = main.workstream_export_csv()
    csv_text = exported.body.decode("utf-8")
    assert "child_progression_rank" in csv_text
    assert "learning_model_reason" in csv_text
    assert "development_ecosystem_rank" in csv_text
    assert "The teaching model uses level-based groups" in csv_text


def test_metric_rescore_preserves_legacy_ranking_and_uses_one_exception_override(tmp_path, monkeypatch):
    _configure(tmp_path, monkeypatch)

    legacy = _payload(main.workstream_submit({
        "pm": "Milan",
        "task_index": 0,
        "decision": "4",
        "rank": 4,
        "rank_label": "Strong fit",
        "reason": "Earlier overall judgement that must remain locked and unchanged.",
    }))
    assert legacy["ok"] is True

    evidence = {
        "child_progression": {
            "text": "65 students were in higher education.\nTen completed higher education that year.",
            "links": [{"label": "Annual report · page 15", "url": "https://example.org/report#page=15"}],
            "ceiling_rank": 4,
            "ceiling_reason": "No complete multi-cohort employment picture is published.",
        },
        "learning_model": {
            "text": "Daily arts training is reported.",
            "links": [],
            "ceiling_rank": 4,
            "ceiling_reason": "The research pack recommends a maximum of 4.",
        },
        "development_ecosystem": {"text": "Residential care is reported.", "links": [], "ceiling_rank": 5},
    }
    admin = _payload(main.workstream_admin_update({
        "password": "secret",
        "pm": "Milan",
        "evidence_task_index": 0,
        "metric_evidence": evidence,
    }))
    assert admin["data"]["pms"]["Milan"]["tasks"][0]["metric_evidence"]["child_progression"]["ceiling_rank"] == 4

    reasons = {
        "child_progression": "The report provides aggregate higher-education numbers, completion evidence and named alumni destinations, but not a complete multi-cohort employment picture across most former students.",
        "learning_model": "The programme embeds intensive daily performing-arts training alongside formal academics, with regular practice, performance and a clearly structured progression pathway for students.",
        "development_ecosystem": "Children receive residential care, meals, healthcare, adult supervision, arts opportunities and continued higher-education support as one connected and sustained environment.",
    }

    blocked = _payload(main.workstream_submit_metrics({
        "pm": "Milan",
        "task_index": 0,
        "metric_scoring_version": "v1.2",
        "metric_scores": {
            "child_progression": {"rank": 4, "reason": reasons["child_progression"]},
            "learning_model": {"rank": 5, "reason": reasons["learning_model"]},
            "development_ecosystem": {"rank": 5, "reason": reasons["development_ecosystem"]},
        },
        "exception_override": {
            "enabled": True,
            "rank": 5,
            "reason": "The three dimensions do not capture the institution's exceptional strategic fit, long-term cultural pathway and unusually strong relevance to the programme's overall purpose.",
        },
    }))
    assert blocked["ok"] is False
    assert "ceiling" in blocked["error"].lower()

    exception_reason = "The three metric scores do not fully capture Kalkeri's exceptional overall strategic fit, the central role of food in its residential model, and the unusually coherent long-term pathway it offers children."
    rescored = _payload(main.workstream_submit_metrics({
        "pm": "Milan",
        "task_index": 0,
        "metric_scoring_version": "v1.2",
        "metric_scores": {
            "child_progression": {"rank": 4, "reason": reasons["child_progression"]},
            "learning_model": {"rank": 4, "reason": reasons["learning_model"]},
            "development_ecosystem": {"rank": 5, "reason": reasons["development_ecosystem"]},
        },
        "exception_override": {"enabled": True, "rank": 5, "reason": exception_reason},
    }))
    assert rescored["ok"] is True
    response = rescored["data"]["pms"]["Milan"]["responses"]["0"]
    assert response["rank"] == 4
    assert response["reason"] == "Earlier overall judgement that must remain locked and unchanged."
    assert response["metric_submitted"] is True
    assert response["metric_scores"]["learning_model"] == {"rank": 4, "reason": reasons["learning_model"]}
    assert response["exception_override"]["enabled"] is True
    assert response["exception_override"]["rank"] == 5
    assert response["exception_override"]["reason"].startswith("The three metric scores")

    exported = main.workstream_export_csv().body.decode("utf-8")
    assert "exception_override_rank" in exported
    assert "exception_override_reason" in exported
    assert "The three metric scores" in exported
    assert "learning_model_override" not in exported

    cleared = _payload(main.workstream_delete_metrics({"pm": "Milan", "task_index": 0}))
    response_after_clear = cleared["data"]["pms"]["Milan"]["responses"]["0"]
    assert response_after_clear["rank"] == 4
    assert response_after_clear["reason"] == "Earlier overall judgement that must remain locked and unchanged."
    assert "metric_scores" not in response_after_clear
    assert "metric_submitted" not in response_after_clear
    assert "exception_override" not in response_after_clear



def test_stale_edit_locks_are_ignored_and_removed(tmp_path, monkeypatch):
    _configure(tmp_path, monkeypatch)
    data = main._read_workstream_payload()
    data["edit_locks"] = {"all": True, "pms": {"Milan": True}}
    main._atomic_write_text(main.WORKSTREAM_DATA_FILE, json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    reasons = {
        "child_progression": "The available evidence gives named and aggregate progression information that is sufficient for a defensible screening score under the current public-evidence protocol.",
        "learning_model": "The available evidence explains the teaching mechanisms, regularity and structure clearly enough to support an independent learning-model judgement by the reviewer.",
        "development_ecosystem": "The available evidence describes the support surrounding children, its continuity and how the different supports work together over time in the programme.",
    }
    saved = _payload(main.workstream_submit_metrics({
        "pm": "Milan",
        "task_index": 0,
        "metric_scores": {
            "child_progression": {"rank": 3, "reason": reasons["child_progression"]},
            "learning_model": {"rank": 3, "reason": reasons["learning_model"]},
            "development_ecosystem": {"rank": 3, "reason": reasons["development_ecosystem"]},
        },
        "exception_override": {"enabled": False, "rank": 3, "reason": ""},
    }))
    assert saved["ok"] is True
    assert "edit_locks" not in saved["data"]

    compatibility = _payload(main.workstream_admin_lock_edits({
        "password": "secret",
        "all_pms": True,
        "locked": True,
    }))
    assert compatibility["ok"] is True
    assert compatibility["locked"] is False
    assert compatibility["removed"] is True
    assert "edit_locks" not in compatibility["data"]
