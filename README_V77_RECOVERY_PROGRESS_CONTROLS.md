# Backend v77 — Recovery Progress Controls

Adds persistent checkpoint control to Advanced Website Recovery:

- Live processed, total, remaining, percentage, throughput and ETA fields.
- `POST /repository/recheck/pause/{run_id}`.
- `POST /repository/recheck/stop/{run_id}`.
- `POST /repository/recheck/resume/{run_id}`.
- Existing cancel route safely aliases stop.
- Partial results, audit, Avika and Firecrawl queues are appended after every completed NGO.
- Resume skips completed Darpan IDs/name-location identities and restores query/Firecrawl counters.
- Paused time is excluded from ETA calculation.
- Partial exports are initialized at run start and remain downloadable in every state.
