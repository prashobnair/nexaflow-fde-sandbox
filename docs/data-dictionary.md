# Data dictionary

All CSVs use UTF-8, ISO timestamps (`YYYY-MM-DD` or UTC `...Z`), and synthetic IDs.

| File | Grain | Key fields | Purpose |
|---|---|---|---|
| `customers.csv` | one customer account | `customer_id`, `segment`, `lifecycle_stage`, `health_score`, `health_label`, `renewal_date` | account master and benchmark health |
| `contacts.csv` | one person per account | `contact_id`, `customer_id`, `role`, `is_champion`, `last_engaged_at` | stakeholder coverage and engagement |
| `contracts.csv` | one commercial term | `contract_id`, `customer_id`, `start_date`, `end_date`, `arr_usd`, `status` | renewal and commercial context |
| `implementations.csv` | one rollout/workspace | `implementation_id`, `customer_id`, `status`, `target_go_live_date`, `actual_go_live_date`, `risk_reason` | delivery state |
| `usage_daily.csv` | customer/workspace/day | `usage_id`, `customer_id`, `workspace_id`, `usage_date`, `active_users`, `workflows_run`, `sla_breach_count` | adoption and operational value signals |
| `support_tickets.csv` | one support case | `ticket_id`, `customer_id`, `severity`, `status`, `opened_at`, `resolved_at`, `category` | support burden and service quality |
| `communications.csv` | one account interaction | `communication_id`, `customer_id`, `occurred_at`, `channel`, `direction`, `sentiment`, `summary` | CSM/support engagement evidence |
| `documents.csv` | one searchable document | `document_id`, `customer_id`, `document_type`, `updated_at`, `title`, `body`, `source_url` | future RAG corpus |
| `ground_truth.csv` | one planted scenario | `scenario_id`, `customer_id`, `expected_label`, `primary_driver`, `recommended_action`, `evidence` | evaluation oracle; never use as model input |

### Important conventions

- Missing dates/values are blank CSV cells, not zero.
- `active_users` can be zero; it means observed inactivity, not missing telemetry.
- `resolved_at` is blank for an open ticket.
- Health is calculated as of the generated dataset's `as_of_date`, recorded in `manifest.json`.
- IDs are stable only for a seed/profile pair.
