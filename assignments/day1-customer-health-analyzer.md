# Day 1 assignment — Customer Health Analyzer

Build a small Python analysis that reads the Day-1 CSVs and produces `outputs/customer_health_report.csv` plus a concise Markdown summary. Do not use `ground_truth.csv` as an input.

## User story

As a Customer Success Operations lead, I need a ranked list of accounts needing attention so that CSM and Professional Services teams can act from evidence rather than intuition.

## Required output fields

`customer_id`, `customer_name`, `calculated_risk`, `primary_driver`, `evidence`, `recommended_action`, `owner`, `confidence`, `data_quality_note`.

## Acceptance criteria

- Reads raw CSVs and runs on Windows with Python 3.11; no cloud service required.
- Calculates recent (last 30 days) adoption against the prior 30 days and flags material decline or inactivity.
- Counts unresolved severity P1/P2 tickets and identifies implementation status and renewal proximity.
- Ranks and explains at least the five most urgent accounts, citing concrete dates/counts.
- Keeps missing telemetry distinct from zero activity and writes a verification note for ambiguous accounts.
- Routes implementation issues to Professional Services and support issues to Support/CSM; no autonomous customer communication.
- Produces deterministic output for seed 42 and does not read ground truth during analysis.
- Includes a short README section explaining assumptions and known data limitations.

## Stretch goals

Load the CSVs into PostgreSQL, expose the report through FastAPI, add tests, and compare results to ground truth only after the report is frozen.
