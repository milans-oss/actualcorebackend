# DFP 2.0 Core Backend V59 — Final Ranking and Human Leads archive

## Persistent additions

- `workspaces/<region>/final_ranking_state.json`
  - explicit Combined Review → Final Ranking selections
  - selected final tier
  - per-NGO display-text overrides
  - original PM workstream data is never overwritten
- Human Leads archive is reconstructed from both Lead Pool memory and historical PM workstream tasks.

## Routes

- `GET /workspace/{region}/human-leads/archive`
- `POST /ranking/final-selection`
- `POST /ranking/final-overrides/update`
- `GET /ranking/compiled-review?region=...`
- `GET /ranking/final-board?region=...`
- `GET /ranking/final-summary?region=...`

Final Ranking edits and transfers are included in the existing undo/redo journal.
