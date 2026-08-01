# Core Backend v85 — Railway deployment

1. Upload this ZIP to the Git repository connected to the existing **core backend** Railway service.
2. Keep the current persistent volume and mount it at `/data`.
3. Set `RUNS_DIR=/data/runs`.
4. Keep the existing `ADMIN_PASSWORD`.
5. Set `FRONTEND_ORIGIN` to the final frontend Railway domain.
6. Deploy. Railway can use the root `railway.json`; no root-directory change is required. If the service already uses Root Directory `/backend`, the inner `backend/railway.json` also works.
7. Confirm `GET /health` returns HTTP 200.
8. Open the frontend and refresh the **DFP NGO ID Registry**. Startup backfill runs automatically. Enter `ADMIN_PASSWORD` and click **Backfill historical IDs** once if the inventory is incomplete, then export the registry.

Do not detach or replace the old core-backend volume during this deployment. Historical IDs can only be assigned to historical data that is still on that volume.
