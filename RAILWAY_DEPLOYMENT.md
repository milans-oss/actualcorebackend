# Core Backend v88 — Railway deployment

1. Extract this ZIP into the root of the Git repository connected to the existing core-backend service.
2. Do not detach or replace the historical persistent volume. Mount it at `/data`.
3. Set:

```text
RUNS_DIR=/data/runs
ADMIN_PASSWORD=<your existing password>
DFP2_PRODUCTION=true
DFP2_SERVICE_ROLE=core
FRONTEND_ORIGIN=https://<frontend>.up.railway.app
```

4. Delete `DFP2_ADMIN_TOKEN` and `DFP2_REQUIRE_MUTATION_AUTH` if they remain from an older release.
5. Deploy and confirm `GET /health`.
6. Confirm that `/karnataka-recovery/modes` returns a wrong-service 404 on core; that route belongs only to the search worker.
7. Use the DFP NGO ID Registry card in the frontend to refresh status and run the idempotent historical backfill when required.

Only `ADMIN_PASSWORD` is used for protected operations.
