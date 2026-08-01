# Backend v76 — Selective Firecrawl Recovery

## Purpose

This release keeps the 29,000-NGO first pass within a maximum of two Serper
queries per NGO, then uses Firecrawl only through a separate, explicitly
started recovery job.

## Search and verification flow

1. Reuse supplied website or organisational email domain at zero search cost.
2. Search the exact Darpan ID.
3. If unresolved, search one adaptive public-brand or registered-name query.
4. Verify candidates using direct HTTP and local PDF extraction.
5. Export unresolved rows to `dfp2_firecrawl_recovery_input.csv`.
6. Run the dedicated Firecrawl recovery strategy on that queue only.

The normal Serper strategy cannot spend Firecrawl credits.

## Firecrawl safeguards

Default envelope:

- Total allowance: 10,000 credits
- Candidate verification: 7,000 credits
- Search recovery: 2,000 credits
- Safety reserve: 1,000 credits
- Basic proxy only
- Maximum three Firecrawl scrapes per domain
- Maximum one Firecrawl search per unresolved NGO
- Maximum one nominated domain verified after a Firecrawl search

Firecrawl Search is called without `scrapeOptions`; results are filtered first,
and only the best unresolved candidate may be scraped.

## Other changes

- Local PDF parsing through `pypdf`, so ordinary accessible PDFs do not consume
  Firecrawl credits.
- Public-brand/programme-name recovery in the second Serper query.
- Candidate-site fetch failures stay separate from completed no-candidate
  searches.
- Firecrawl expenditure and action are included in row-level and run-level
  audit outputs.
- Confirmed/probable websites remain exportable for the existing Avika filter.
