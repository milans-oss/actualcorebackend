# DFP 2.0 Core Backend v85 — Railway release

This is the complete core backend. Deploy this ZIP to the existing core-backend Railway service so its historical persistent volume remains attached.

## Main changes

- Permanent `DFP-NGO-XXXXXXXXXXXXXXXX` identifier across historical and future shortlisting records.
- Automatic, idempotent historical ID backfill on startup.
- NGO ID propagation through PM workstreams, Lead Pool, final ranking, Contact Tracker and retained recovery/repository CSVs.
- Karnataka Recovery core endpoints and ID-registry controls.

## Railway

The ZIP root already contains `railway.json` and `Procfile`.

Required variables:

```text
RUNS_DIR=/data/runs
ADMIN_PASSWORD=<existing password>
DFP2_ADMIN_TOKEN=<shared long random token>
DFP2_REQUIRE_MUTATION_AUTH=true
DFP2_PRODUCTION=true
FRONTEND_ORIGIN=https://<frontend>.up.railway.app
```

Mount the existing core-backend volume at `/data`. The historical ID migration can only backfill records still present on that volume.

After deployment:

```text
GET /health
GET /admin/ngo-ids/status
POST /admin/ngo-ids/backfill
GET /admin/ngo-ids/export.csv?password=<ADMIN_PASSWORD>
```

See `RAILWAY_DEPLOYMENT.md` and `backend/README_V85_NGO_ID_SINGLE_SERPER.md`.
