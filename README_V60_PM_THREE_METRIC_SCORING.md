# Backend v60 — PM Three-Metric Scoring

## Changes
- Persists three metric ranks and reasons inside each existing PM response.
- Persists metric-specific evidence and source links on the selected PM task/NGO.
- Persists an optional scoring-reference document URL.
- Preserves all legacy overall ranking and reason fields.
- Adds metric columns to the workstream CSV export.
- Sanitises evidence links and clamps metric ranks to the 1–5 scale.

## New response object
`metric_scores.child_progression`, `metric_scores.learning_model`, and `metric_scores.development_ecosystem` each contain `rank` and `reason`.

## New task object
`metric_evidence` contains `text` and labelled `links` for each of the three metrics.
