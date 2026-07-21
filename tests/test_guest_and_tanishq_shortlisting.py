import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("backend_main_guest_shortlisting", ROOT / "main.py")
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


def _scores(child=4, learning=4, ecosystem=4):
    reason = (
        "This assessment is based on the available programme evidence and explains the judgement clearly enough "
        "for comparison while preserving the reviewer's independent reasoning across the required dimension."
    )
    return {
        "child_progression": {"rank": child, "reason": reason},
        "learning_model": {"rank": learning, "reason": reason},
        "development_ecosystem": {"rank": ecosystem, "reason": reason},
    }


def test_guest_is_blind_copy_then_reveals_pm_ranking_without_affecting_official_score(tmp_path, monkeypatch):
    _configure(tmp_path, monkeypatch)

    pm_saved = _payload(main.workstream_submit_metrics({
        "pm": "Milan",
        "task_index": 0,
        "metric_scores": _scores(5, 4, 3),
        "exception_override": {"enabled": False, "rank": 3, "reason": ""},
    }))
    assert pm_saved["ok"] is True

    copied = _payload(main.workstream_admin_transfer_tasks({
        "password": "secret",
        "from_pm": "Milan",
        "to_pm": "Guest",
        "task_index": 1,
        "move_responses": True,
    }))
    assert copied["ok"] is True
    assert copied["copied"] is True
    assert len(copied["data"]["pms"]["Milan"]["tasks"]) == 3
    assert copied["data"]["pms"]["Milan"]["responses"]["0"]["metric_submitted"] is True
    assert len(copied["data"]["pms"]["Guest"]["tasks"]) == 1
    assert copied["data"]["pms"]["Guest"]["responses"] == {}
    assert "guest_reference_review" not in copied["data"]["pms"]["Guest"]["tasks"][0]

    guest_saved = _payload(main.workstream_submit_metrics({
        "pm": "Guest",
        "task_index": 0,
        "metric_scores": _scores(2, 3, 4),
        "exception_override": {"enabled": False, "rank": 3, "reason": ""},
    }))
    assert guest_saved["ok"] is True
    reference = guest_saved["guest_reference_review"]
    assert reference["reviewer"] == "Milan"
    assert reference["metric_scores"]["child_progression"]["rank"] == 5
    assert reference["metric_scores"]["learning_model"]["rank"] == 4
    assert guest_saved["data"]["pms"]["Guest"]["tasks"][0]["guest_reference_review"]["reviewer"] == "Milan"

    official = main._workstream_metric_review_candidates(main._read_workstream_payload())
    assert [(row["pm"], row["ngo_name"]) for row in official] == [("Milan", "Aina Trust")]


def test_tanishq_legacy_referral_rows_migrate_to_standard_shortlisting(tmp_path, monkeypatch):
    _configure(tmp_path, monkeypatch)
    data = main._read_workstream_payload()
    data["pms"]["Tanishq"] = {
        "name": "Tanishq",
        "deadline": "2026-07-22T18:00",
        "responsibility": "Complete referral and POC details.",
        "task_type": "ngo_details",
        "tasks": [
            {"ngo_name": "Referral NGO 1", "background": "Capture NGO details and referral / POC details cleanly."},
            {"ngo_name": "Useful NGO", "website": "https://example.org", "background": "Useful programme context."},
        ],
        "responses": {
            "1": {
                "ngo_description": "Runs a sustained education programme for children.",
                "contact_number": "9999999999",
                "referral_source": "Partner NGO",
                "submitted": True,
            }
        },
    }
    main._write_workstream_payload(data)

    migrated = main._read_workstream_payload()
    tanishq = migrated["pms"]["Tanishq"]
    assert tanishq["task_type"] == "shortlisting"
    assert len(tanishq["tasks"]) == 1
    assert tanishq["tasks"][0]["ngo_name"] == "Useful NGO"
    assert "NGO details: Runs a sustained education programme" in tanishq["tasks"][0]["background"]
    assert "Referral source: Partner NGO" in tanishq["tasks"][0]["background"]
    assert tanishq["responses"] == {}

    public = main._workstream_public_payload(migrated)
    assert "legacy_details_archive" not in public["pms"]["Tanishq"]
