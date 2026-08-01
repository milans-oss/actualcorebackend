# Backend v65 — Three NGO evidence packs

This release adds reviewed metric evidence packs for:

- Sree Siddaganga Math
- Sri Vishwesha Dhama Gurukulam
- Tadimety Radhakrishna Charitable Trust (TRCT)

## What is stored for each NGO

Each of the three PM scoring metrics now receives:

- factual evidence, one sentence per line;
- labelled source links;
- the annual-report search status;
- an NGO-specific recommended ceiling; and
- a ceiling rationale.

## Production migration

The PM assignment data remains in the persistent Railway file:

`/data/runs/workstream_data.json`

On the first `/workstream` read after deployment, v65 finds these NGOs by common name variants and adds the evidence packs to every matching assigned task. The migration:

- preserves all earlier overall rankings and PM responses;
- retains earlier admin-added evidence sentences and links;
- places the reviewed v65 evidence first;
- applies the new metric ceilings; and
- records the migration under `data_migrations.v65-three-ngo-evidence-2026-07-17`.

The migration is idempotent and does not run again after the task has the v65 marker.

## Metric ceilings

| NGO | Alumni outcomes | Learning model | Development environment |
|---|---:|---:|---:|
| Sree Siddaganga Math | 2 | 2 | 4 |
| Sri Vishwesha Dhama Gurukulam | 3 | 4 | 3 |
| Tadimety Radhakrishna Charitable Trust | 2 | 2 | 2 |

## Validation

Backend test suite: `17 passed`.
