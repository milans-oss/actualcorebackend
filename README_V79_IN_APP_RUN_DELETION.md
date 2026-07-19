# DFP 2.0 Backend v79 — In-App Run Deletion + Disk Usage

Mirrors worker v67. Adds:
- POST /repository/runs/delete        {password, confirm:true, run_id}
- POST /repository/runs/delete-many   {password, confirm:true, run_ids:[...]}
- GET  /repository/runs/disk-usage

Same safety guards: never deletes active runs, system folders, loose top-level
files, or anything outside RUNS_DIR. Requires password + confirm.
