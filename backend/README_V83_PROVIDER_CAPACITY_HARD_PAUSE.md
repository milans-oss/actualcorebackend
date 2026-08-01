# V83 — Provider-capacity hard pause

Backend recovery endpoints now expose and preserve provider-capacity pauses from Serper, Firecrawl, Brave Search and Claude Haiku / Anthropic.

Paused runs return:

- `run_status: paused`
- `stage: provider_credit_exhausted`
- `paused_provider`
- `paused_provider_label`
- `paused_key` (masked)
- `provider_status_code`
- `provider_error_detail`
- `processed`, `remaining`, downloads and `can_resume`

Resume clears the prior in-memory provider pause, re-reads Railway environment keys, and continues from the saved checkpoint. Provider-exhausted rows are not counted as completed failures.
