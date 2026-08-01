# Backend v75 — Low-cost website recovery and retry safety

## Search policy

- Smart website recovery defaults to Serper only.
- Maximum paid search calls per NGO defaults to 2.
- Pass 1: exact Darpan ID when available.
- Pass 2: exact registered name + district/state.
- Brave, Firecrawl, and rename-recovery searches are opt-in and disabled by default.
- Default full-run query cap is 58,000, enough for 29,000 NGOs at two searches each.

## Avika-fit integration

The existing repository classifier remains `avika_fit_v2`.

Advanced website recovery performs identity recovery only. It now writes
`dfp2_recovered_websites_for_avika_filter.csv`. Upload that file into the normal
Bulk Scan. The repository engine preserves the supplied `website` column, skips
another Serper website search, fetches the site, and applies the existing
Avika-fit classifier.

## Fetch-error handling

- Direct fetches retry the original URL and conservative www/scheme variants.
- A nominated but unreachable website becomes `candidate_site_unreachable`, not
  `no_candidate_after_completed_search`.
- The retry CSV includes the candidate website. Re-uploading it retries the
  website directly with zero additional Serper calls.
- Repository resume now retries `fetch_failed`, `search_failed`, and
  `skipped_error` rows. Fetch retries reuse the previously found website.

## Recommended environment

```bash
SMART_RECHECK_USE_BRAVE=false
SMART_RECHECK_USE_FIRECRAWL=false
SMART_RECHECK_ENABLE_RENAME_RECOVERY=false
SMART_RECHECK_MAX_QUERIES_PER_ROW=2
SMART_RECHECK_MAX_TOTAL_QUERIES=58000
SMART_RECHECK_FETCH_RETRY_ATTEMPTS=2
SMART_RECHECK_FETCH_RETRY_BACKOFF_SEC=0.75
```
