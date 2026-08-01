# Backend v66 — Evidence packs without rankings

## What changed

- Removed all preset metric rankings, recommended ceilings and ranking rationales from the named NGO evidence packs.
- The PM's three metric scores and overall response remain separate and are not prefilled or overwritten.
- The v66 migration clears any v65 preset `ceiling_rank` and `ceiling_reason` values for matching assignments while preserving existing PM responses.
- Added source-linked evidence packs for 25 NGOs across:
  - Child Progression & Alumni Outcomes
  - Learning Model
  - Development Ecosystem / Environment
- Existing admin-added evidence is retained on first-time preset application. The three old v65 generated packs are replaced to prevent duplicate v65 content.

## Files

- `workstream_evidence_presets.py` contains the neutral evidence and official source links.
- `main.py` imports and applies the versioned presets to persistent `workstream_data.json`.

## Validation

- `pytest -q`: 18 tests passed.
- Tests confirm that all 25 packs contain only evidence text and links at source level.
- Tests confirm migrated evidence rows have zero preset ceilings and empty ceiling reasons.
- Tests confirm existing PM rankings and written responses remain unchanged.
