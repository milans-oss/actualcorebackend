# DFP 2.0 Core Backend v85

This release adds a permanent NGO identifier layer and the core-side controls for Karnataka Recovery.

## Permanent DFP NGO ID

Every shortlisting-facing record now carries an ID in this format:

```text
DFP-NGO-XXXXXXXXXXXXXXXX
```

The ID is deterministic and existing valid IDs are always preserved. Identity seed priority is:

1. NGO Darpan ID (when a true Darpan Unique ID is available)
2. Source record ID
3. Lead Pool ID
4. Registration reference + NGO name + district + state
5. Canonical website domain
6. NGO name + district + state

This means a website redirect or replacement does not change the ID when a stronger legal/source identifier exists. Same-name Darpan source rows remain separate whenever they have distinct source IDs. Registration descriptors are bound to name and location because the supplied Karnataka extract reuses short registration values across unrelated rows.

## Historical backfill

On startup, the backend performs one idempotent migration over the existing persistent volume. It adds IDs to:

- all historical PM shortlisting/workstream tasks;
- Lead Pool rows;
- final-ranking selection snapshots;
- Contact Tracker rows;
- historical repository, recovery, presence and Karnataka Recovery CSVs retained under `RUNS_DIR`.

The migration never deletes, merges, deduplicates or reorders rows. It can only backfill data that is still present on the core backend persistent volume.

Admin endpoints:

```text
GET  /admin/ngo-ids/status
POST /admin/ngo-ids/backfill
GET  /admin/ngo-ids/export.csv?password=...
```

The frontend exposes these under NGO Discovery → Advanced settings → Karnataka Recovery → DFP NGO ID Registry.

## Railway

This ZIP is deployable either from the repository root or with Railway Root Directory set to `/backend`.

Required persistent configuration:

```text
RUNS_DIR=/data/runs
ADMIN_PASSWORD=<existing admin password>
FRONTEND_ORIGIN=https://<frontend-service>.up.railway.app
DFP2_PRODUCTION=true
```

Mount the existing core-backend Railway volume at `/data`. Replacing the service or attaching a new blank volume will not contain the historical shortlist data that needs backfilling.
