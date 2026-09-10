# NexaFlow business and domain specification

## Business context

NexaFlow sells a configurable workflow and operations-management platform to mid-market and enterprise customers. Customers use it to standardize intake, approvals, work routing, SLA tracking, and operational reporting. The customer-facing delivery motion resembles enterprise SaaS implementation: discovery, configuration, integrations, training, go-live, adoption, support, renewal, and expansion.

The primary personas are an executive sponsor, implementation lead, workspace administrators, operational managers, and end users. NexaFlow teams include Account Executives, Professional Services, Customer Success, Support, Product, and Solutions Engineering.

## Customer lifecycle

`prospect → contracted → implementation → live → adoption/renewal → expanded or churned`

An implementation can be on track, at risk, delayed, completed, or cancelled. A customer may have several workspaces, contracts, contacts, tickets, communications, and knowledge documents. Contract ARR is recorded in USD for simplicity.

## Key operational questions

- Which customers are at risk, and why?
- Is the risk driven by adoption, unresolved support, implementation delay, stakeholder engagement, or renewal proximity?
- What should a CSM do next, and what evidence supports it?
- Which account signals are trustworthy versus missing, stale, or contradictory?

## Health model (ground-truth-oriented)

`health_score` is a 0–100 generated benchmark—not a production truth. It combines adoption (35%), support burden (25%), implementation (20%), engagement (10%), and renewal context (10%). Labels: `healthy` ≥70, `watch` 45–69, `at_risk` <45. Some deliberately planted scenarios override expected behavior; see `docs/evaluation-scenarios.md`.

The best action is not always "contact the customer." Implementation risk should be routed to Professional Services; a suspected data defect should trigger verification before outreach.

## Privacy model

Names, emails, company names, message bodies, documents, and identifiers are fictional. Fields are designed to resemble the access-controlled inputs an FDE would encounter, not to represent actual NexaFlow customers.
