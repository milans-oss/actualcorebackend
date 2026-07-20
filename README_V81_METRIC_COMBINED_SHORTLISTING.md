# Backend v81 — Metric Combined Shortlisting

## Changes

### PM shortlist deletion

Added `POST /workstream/admin/delete-tasks`.

The endpoint:

- requires the existing admin password;
- accepts a PM plus one 1-based task number or a start/end range;
- deletes the selected assignments and their saved responses;
- reindexes all later responses so task/response alignment remains correct;
- writes an undo snapshot and global audit-log entry.

### Combined Shortlisting

`GET /ranking/compiled-review` now uses only completed three-metric assessments.

For each NGO it:

- averages duplicate PM assessments by NGO identity;
- returns average scores for the three metrics;
- calculates `combined_points = A + B + C`;
- calculates `combined_score = combined_points / 15`;
- sorts the default response from highest to lowest combined score.

Legacy overall rankings remain untouched for the existing final-ranking workflow.
