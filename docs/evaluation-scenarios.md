# Evaluation-scenario design

`data/seed/day1/ground_truth.csv` is the hidden answer key for later work. During model development, exclude it from prompts, embeddings, training, feature computation, and dashboards. Reveal it only in an evaluation run.

| Scenario | Expected result | What it tests |
|---|---|---|
| Adoption collapse | at-risk; adoption decline | computes recent-versus-baseline usage and cites dated evidence |
| Critical-ticket cluster | at-risk; support burden | counts unresolved high severity tickets and routes ownership |
| Implementation delay | watch/at-risk; delivery | distinguishes pre-go-live accounts from adoption failure |
| Renewal near with weak champion | watch; renewal | combines commercial horizon and engagement without overclaiming |
| Telemetry gap | needs verification | does not equate missing telemetry with zero activity |
| Stale-risk conflict | healthy/watch after verification | handles contradictory score versus behavioral evidence |
| Contract date defect | data-quality escalation | validates inputs before recommending outreach |

## Evaluation rubric

Score each answer 0–2 for: correct label/priority, primary driver, evidence citation (IDs/dates), safe handling of data quality, correctly assigned owner, and feasible next action. A passing baseline is 9/12 with no unsafe recommendation. Track false reassurance separately: marking an at-risk account healthy is a critical error.

## Scenario format for future agents

Provide only approved operational tables plus an account question. Capture structured output: `risk_level`, `drivers`, `evidence`, `confidence`, `recommended_action`, `owner`, `needs_human_review`. Compare it with ground truth and retain failures as regression tests.
