# DFP 2.0 Core Backend v89 — Final Railway Release

Complete core backend for Search Worker v76 and Frontend v158. Deploy it to the existing core-backend Railway service and preserve the existing `/data` volume.

## Included

- Permanent `DFP-NGO-XXXXXXXXXXXXXXXX` IDs across historical and future Lead Pool, PM workstream, shortlist, final-ranking and Contact Tracker records.
- Idempotent historical NGO-ID backfill and registry export.
- Karnataka Recovery result compatibility, including ownership-evidence fields and source-record IDs. The core service refuses `/karnataka-recovery` requests so recovery can only execute on the hardened Search Worker v76.
- Existing admin operations use only `ADMIN_PASSWORD`; there is no second mutation token.

## Required variables

```text
RUNS_DIR=/data/runs
ADMIN_PASSWORD=<your existing password; same on all three services>
DFP2_PRODUCTION=true
DFP2_SERVICE_ROLE=core
FRONTEND_ORIGIN=https://<frontend>.up.railway.app
```

Mount the existing core-backend volume at `/data`.

## Checks

```text
GET /health
GET /admin/ngo-ids/status
POST /admin/ngo-ids/backfill
GET /admin/ngo-ids/export.csv?password=<ADMIN_PASSWORD>
```
