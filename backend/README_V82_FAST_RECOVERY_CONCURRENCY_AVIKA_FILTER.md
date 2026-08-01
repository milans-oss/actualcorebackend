# V82 — Fast Recovery concurrency + Avika-filtered Lead Pool handoff

This backend mirrors the Railway worker changes:

- accepts `fast` and `deep` recovery strategies;
- exposes Avika-filtered repository/audit/rejected downloads;
- prefers the filtered repository CSV when importing a recovery run;
- rotates multiple Serper keys concurrently;
- disables exhausted/invalid keys and cools down temporary 429 keys;
- reports per-key masked usage/in-flight/cooldown status.

Use the Railway variables documented in `README_V69_FAST_RECOVERY_CONCURRENCY_AVIKA_FILTER.md` in the worker package.
