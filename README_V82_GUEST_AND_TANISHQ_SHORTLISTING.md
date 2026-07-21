# V82 — Guest and Tanishq shortlisting

- Adds a persistent Guest shortlist bucket that accepts blind copies of PM assignments.
- Copying an assignment to Guest does not remove the source PM task, response, progress or official ranking.
- A completed source PM assessment is stored as a hidden benchmark; if it is completed later, the backend resolves it when Guest submits.
- The benchmark is stripped from every public workstream response until the Guest assessment is complete.
- After Guest submits, the source DFP PM ranking is returned for the Thank You reveal.
- Guest scores are excluded from the official combined PM ranking and totals.
- Converts Tanishq from the legacy referral/POC details workflow to the standard three-metric shortlisting workflow.
- Archives meaningful legacy Tanishq details on disk, migrates them into task context, removes untouched placeholder rows, and clears old detail responses from the active scorer.
