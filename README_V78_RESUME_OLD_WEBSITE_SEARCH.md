# Backend v78 — Resume Old Website Searches

Adds a durable resumable-run listing endpoint for advanced website recovery.

## New endpoint

`GET /repository/recheck/resumable?limit=100`

Returns checkpoint-backed Serper and Firecrawl runs that are paused, stopped, cancelled, failed, or interrupted by restart. Each row includes strategy, processed/total/remaining counts, last update, original input filename, query/credit usage, and output availability.

## Resume hardening

- Old cancelled runs have stale cancellation flags cleared before restart.
- Completed NGOs remain checkpointed and are not processed again.
- Stale `running` status with no live thread is presented as `interrupted` and resumable.
- Runs without `uploaded_input.csv` are not offered and cannot be resumed.
- Original upload filename is now saved in the run status.

## Persistence requirement

Set `RUNS_DIR` to a Railway persistent volume path. Old runs are recoverable only while their run folder, status JSON, uploaded input CSV, and checkpoint outputs still exist.
