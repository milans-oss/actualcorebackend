# V84 — Karnataka Source-Record Recovery

The backend now exposes the same separate `/karnataka-recovery` router as the Railway worker so either deployed search service can support the new frontend module.

## Included

- Source-record preservation; no name/district input deduplication.
- Zero-query URL and saved-candidate verification.
- Missing-query-only, enhanced, new/unlinked and collision queues.
- Technical recommendation regression mode.
- Candidate page-type classification and continuation after mismatch.
- Serper key preflight, per-key failover and concurrency clamping.
- Optional Firecrawl v2 fallback with a hard per-run credit ceiling.
- Checkpointed pause/resume/cancel and downloadable source-level audit.
- Optional Avika/DFP-fit callback only after website identity is established.

## API

`/karnataka-recovery/modes`, `/capacity`, `/start`, `/status`, `/pause`, `/resume`, `/cancel`, `/runs`, and `/export`.

## Validation

- Python compilation passed.
- Karnataka recovery tests: **8 passed**.
- Full backend suite: **80 passed, 1 failed**.
- The one failing integrated final-ranking test is unrelated and also fails unchanged against the pre-V84 `main.py` backup (`grouped_by_rating` is absent). No ranking code was altered for this release.
