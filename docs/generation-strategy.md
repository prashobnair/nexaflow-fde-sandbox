# Synthetic-data generation strategy

## Design principles

The generator creates internally coherent records first, then adds controlled imperfections. Customer archetypes determine likely usage, support, delivery, and communications behavior. A fixed seed makes every result reproducible. Generation never calls an external API.

The Day-1 profile is purposefully small: 30 customers, 90 days of customer/workspace usage, roughly 250 tickets, and supporting lifecycle records. It is sufficient for pandas, SQL, joins, anomaly detection, and evaluation design without stressing an 8 GB laptop.

## Scaling

Profiles parameterize customer count, history days, ticket rate, and workspace count. `scale` targets approximately 1,000 customers, 20,000 tickets, and 18 months of usage. Generate one profile at a time; use PostgreSQL `COPY` for larger loads. Future enrichment may map public datasets (for example, public help-desk text or customer-support intent corpora) into a separate `data/external/` layer with provenance, license, and a mapping document. Do not mix external data into the canonical synthetic ground truth.

## Deliberate imperfections

- 4% missing `last_engaged_at`; 3% duplicate-like contact emails with casing variation.
- A small number of usage rows have delayed ingestion timestamps; selected customers have telemetry gaps.
- Some open tickets have an incorrectly populated `resolved_at`; selected ticket titles have inconsistent category wording.
- A small number of contracts have an end date preceding a start date (data-quality scenario).
- One account has contradictory high usage and a low score caused by a stale CSM-risk flag.

These defects are deterministic and are documented by the manifest. They teach reconciliation, data contracts, and safe AI behavior.

## Recreate data

```powershell
python scripts/generate_data.py --profile day1 --seed 42
python scripts/validate_data.py
```

Generated files are versioned as a teaching snapshot. Regeneration with the same arguments overwrites them with identical values.
