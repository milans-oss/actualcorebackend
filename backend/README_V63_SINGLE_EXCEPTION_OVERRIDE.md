# V63 — Single exception override persistence

`POST /workstream/submit-metrics` now stores one response-level object:

```json
{
  "exception_override": {
    "enabled": true,
    "rank": 5,
    "reason": "Minimum 100 characters when enabled"
  }
}
```

Per-metric `override` and `override_reason` fields are no longer stored or exported.

Metric ceilings remain mandatory. A metric score above the configured ceiling is rejected. The exception override is a separate overall NGO judgement and does not modify any metric score or the earlier locked `rank` and `reason`.

CSV export fields:

- `exception_override_enabled`
- `exception_override_rank`
- `exception_override_reason`
- `exception_override_json`
