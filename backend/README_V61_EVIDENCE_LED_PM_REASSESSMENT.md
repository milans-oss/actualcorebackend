# Backend v61 — Evidence-led PM Re-assessment

## Persistence model

PM shortlisting state is stored in:

`RUNS_DIR/workstream_data.json`

For the Railway core service, `RUNS_DIR` must point to the mounted persistent volume:

`RUNS_DIR=/data/runs`

Therefore the production PM memory file should be:

`/data/runs/workstream_data.json`

## Exact stored variables

### Earlier overall ranking — preserved

`pms.<PM>.responses.<task_index>`

- `decision`
- `rank`
- `rank_label`
- `reason`
- `submitted`
- `submitted_at`

### New three-metric response

Stored in the same response object without changing the earlier fields:

- `metric_scores.child_progression.rank`
- `metric_scores.child_progression.reason`
- `metric_scores.learning_model.rank`
- `metric_scores.learning_model.reason`
- `metric_scores.development_ecosystem.rank`
- `metric_scores.development_ecosystem.reason`
- `metric_submitted`
- `metric_submitted_at`
- `metric_scoring_version`

### Admin evidence package

`pms.<PM>.tasks.<task_index>.metric_evidence.<metric>`

Each metric contains:

- `text` — one factual sentence per line
- `links` — labelled official source links
- `ceiling_rank` — optional NGO-specific recommended maximum
- `ceiling_reason` — why that ceiling applies

## New endpoints

- `POST /workstream/submit-metrics`
  - saves only the three new scores
  - preserves the earlier overall rank and reason exactly
  - validates 100 characters per rationale
- `POST /workstream/delete-metrics`
  - clears only the new three-metric response
  - preserves the earlier overall response
- `GET /workstream/storage-info`
  - reports the resolved storage paths and whether the core service appears to use `/data`

## Other persistent files on the core volume

- Lead Pool: `/data/runs/workspaces/<region>/lead_pool.csv`
- Workspace event log: `/data/runs/workspaces/<region>/workspace_log.jsonl`
- Undo/redo: `/data/runs/undo_redo/undo_stack.json` and `redo_stack.json`

## Railway core variables

- `DFP2_SERVICE_ROLE=core`
- `RUNS_DIR=/data/runs`
- `FRONTEND_ORIGINS=<frontend domains>`
- `ADMIN_PASSWORD=<gearbox admin password>`
- `DFP2_ADMIN_TOKEN=<optional mutation token>`

The search worker should not be treated as the PM memory service. It normally uses temporary run storage such as `/tmp/dfp2-runs`.
