-- Run from psql after schema.sql; adjust the absolute path for your checkout.
-- Example: \set seed_path 'C:/.../data/seed/day1'
\copy customers FROM :'seed_path'/customers.csv CSV HEADER
\copy contacts FROM :'seed_path'/contacts.csv CSV HEADER
\copy contracts FROM :'seed_path'/contracts.csv CSV HEADER
\copy implementations FROM :'seed_path'/implementations.csv CSV HEADER
\copy usage_daily FROM :'seed_path'/usage_daily.csv CSV HEADER
\copy support_tickets FROM :'seed_path'/support_tickets.csv CSV HEADER
\copy communications FROM :'seed_path'/communications.csv CSV HEADER
\copy documents FROM :'seed_path'/documents.csv CSV HEADER
