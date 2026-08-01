# Core backend v64 — PM edit locking removed

- Removed lock enforcement from metric submission, legacy response submission, metric clearing and response deletion.
- Stale `edit_locks` state in `workstream_data.json` is discarded on read.
- `/workstream/admin/lock-edits` remains as a temporary compatibility no-op and always leaves all PM workspaces editable.
- Existing PM assignments, legacy rankings, metric scores, evidence packs and override data are preserved.
