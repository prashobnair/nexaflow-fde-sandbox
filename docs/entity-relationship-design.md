# Entity relationship design

```mermaid
erDiagram
  CUSTOMERS ||--o{ CONTACTS : has
  CUSTOMERS ||--o{ CONTRACTS : signs
  CUSTOMERS ||--o{ IMPLEMENTATIONS : delivers
  CUSTOMERS ||--o{ USAGE_DAILY : generates
  CUSTOMERS ||--o{ SUPPORT_TICKETS : opens
  CUSTOMERS ||--o{ COMMUNICATIONS : records
  CUSTOMERS ||--o{ DOCUMENTS : owns
  CUSTOMERS ||--o{ GROUND_TRUTH : evaluated_by
  IMPLEMENTATIONS ||--o{ USAGE_DAILY : enables
```

`workspace_id` models an independently configured operating unit. Day 1 uses one workspace per customer; later profiles can vary this. `ground_truth` is intentionally separated from operational tables to prevent target leakage in analytics or AI prompts.

### PostgreSQL access pattern

Start from `customers`, aggregate the last 30/60/90 days of `usage_daily`, open tickets, latest implementation, renewal horizon, and engagement. Preserve raw tables and build derived views/models rather than updating source records.
