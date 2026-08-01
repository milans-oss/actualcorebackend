# V56 Force CORS Core Patch

This build adds an outer CORS guard that stamps CORS headers on every response, including early auth/service-role failures and OPTIONS preflight responses.

Use for Railway corebackend service:
- DFP2_SERVICE_ROLE=core
- RUNS_DIR=/data/runs
- FRONTEND_ORIGINS=https://thedailyfeedingprogram-production.up.railway.app,https://the-daily-feeding-program.vercel.app,http://localhost:3000

Your restored workspace data remains on the Railway volume at /data/runs and is not included in this zip.
