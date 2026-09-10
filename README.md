# NexaFlow FDE Sandbox

NexaFlow is a fictional B2B workflow-operations SaaS company. This sandbox is a repeatable enterprise-shaped environment for learning the work of a Forward Deployed Engineer: discovery, data inspection, implementation delivery, AI-assisted operations, evaluation, and production-minded deployment.

## Day 1 quick start (Windows)

Prerequisites: Python 3.11+ and Git. PostgreSQL and Docker are optional for Day 1.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python scripts/generate_data.py --profile day1 --seed 42
python scripts/validate_data.py
```

The generated CSV files live in `data/seed/day1/`. The generator uses only Python's standard library, so it works well on an 8 GB machine. Load the same files into PostgreSQL later with `sql/schema.sql` and `sql/load_seed.sql`.

To start PostgreSQL when Docker is available:

```powershell
docker compose up -d
psql -U nexaflow -d nexaflow -f sql/schema.sql
```

Set the `seed_path` variable to the absolute `data/seed/day1` path before running `sql/load_seed.sql`. The supplied Compose password is development-only; replace it through environment variables before any cloud deployment.

## What is here

- `docs/` — business model, data dictionary, ER design, generator and evaluation plans.
- `data/seed/day1/` — reproducible small but realistic synthetic data.
- `scripts/` — data generation and validation.
- `sql/` — PostgreSQL schema and import helper.
- `assignments/day1-customer-health-analyzer.md` — first build assignment.

## Scale profiles

| Profile | Customers | Tickets | Usage history | Intended use |
|---|---:|---:|---|---|
| `day1` | 30 | ~250 | 90 days | local exploration and first assignment |
| `portfolio` | 150 | ~3,000 | 12 months | portfolio/API/RAG work |
| `scale` | 1,000 | ~20,000 | 18 months | performance and deployment exercises |

All profiles are deterministic for a supplied seed. The `scale` profile should be generated/imported in batches on an 8 GB laptop.

## 90-day use

1. **Weeks 1–2:** pandas/SQL health analysis on the Day-1 data.
2. **Weeks 3–4:** package the analyzer as an API and containerize it.
3. **Weeks 5–6:** add document retrieval and cited support/implementation assistance.
4. **Weeks 7–8:** build a tool-calling customer-success agent with human approvals.
5. **Weeks 9–10:** create scenario-based evaluations using the embedded ground truth.
6. **Weeks 11–13:** deploy, monitor, present a delivery plan, and turn the project into an FDE portfolio case study.

Read [the domain specification](docs/domain-specification.md) first, then start the Day-1 assignment.

## Guardrails

This is synthetic data only. Known imperfections are intentional; do not silently "fix" them before recording their effect on an analysis or evaluation.
