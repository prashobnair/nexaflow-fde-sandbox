#!/usr/bin/env python3
"""Generate deterministic, fictional NexaFlow data with intentional defects."""
import argparse, csv, json, random, shutil
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILES = {"day1": (30, 90, 250), "portfolio": (150, 365, 3000), "scale": (1000, 548, 20000)}
AS_OF = date(2026, 9, 1)
FIRST = ["Asha", "Rohan", "Meera", "Vikram", "Nisha", "Arjun", "Priya", "Karan", "Leah", "Noah"]
COMPANIES = ["Atlas", "Harbor", "Cedar", "Northstar", "Meridian", "Summit", "Vantage", "Orbit", "Pioneer", "Bluebird"]
INDUSTRIES = ["Logistics", "Fintech", "Healthcare", "Retail", "Manufacturing"]
ARCHETYPES = ["healthy", "adoption_collapse", "ticket_cluster", "implementation_delay", "renewal_watch", "telemetry_gap", "stale_risk"]

def write(path, fields, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields); writer.writeheader(); writer.writerows(rows)

def iso(d): return d.isoformat()

def main():
    p = argparse.ArgumentParser(); p.add_argument("--profile", choices=PROFILES, default="day1"); p.add_argument("--seed", type=int, default=42)
    args = p.parse_args(); rng = random.Random(args.seed)
    n, days, ticket_target = PROFILES[args.profile]
    out = ROOT / "data" / "seed" / args.profile
    if out.exists(): shutil.rmtree(out)
    out.mkdir(parents=True)
    customers=[]; contacts=[]; contracts=[]; implementations=[]; usage=[]; tickets=[]; comms=[]; docs=[]; truth=[]
    for i in range(1, n + 1):
        cid=f"CUST-{i:04d}"; archetype=ARCHETYPES[(i-1) % len(ARCHETYPES)]
        name=f"{COMPANIES[(i-1)%len(COMPANIES)]} {['Operations','Systems','Group'][i%3]}"
        segment=["mid_market", "enterprise", "strategic"][i % 3]
        renewal=AS_OF + timedelta(days=(i * 23) % 360 - 40)
        score={"healthy":82,"adoption_collapse":31,"ticket_cluster":28,"implementation_delay":42,"renewal_watch":55,"telemetry_gap":50,"stale_risk":25}[archetype] + rng.randint(-5,5)
        customers.append(dict(customer_id=cid,customer_name=name,industry=INDUSTRIES[i%5],segment=segment,lifecycle_stage="implementation" if archetype=="implementation_delay" else "live",health_score=score,health_label="healthy" if score>=70 else ("watch" if score>=45 else "at_risk"),renewal_date=iso(renewal),account_owner=f"CSM-{(i%5)+1:02d}",created_at=iso(AS_OF-timedelta(days=500+i))))
        for j, role in enumerate(["Executive Sponsor", "Workspace Admin"]):
            first=FIRST[(i+j)%len(FIRST)]; email=f"{first.lower()}.{i}@example.nexaflow.test"
            if i % 11 == 0 and j == 1: email=email.upper() # deliberate near-duplicate style issue
            last="" if (i+j)%23==0 else iso(AS_OF-timedelta(days=(i*7+j*13)%100))
            contacts.append(dict(contact_id=f"CONT-{i:04d}-{j+1}",customer_id=cid,full_name=f"{first} {name.split()[0]}",email=email,role=role,is_champion="true" if j==1 else "false",last_engaged_at=last))
        start=AS_OF-timedelta(days=365-(i%90)); end=start+timedelta(days=365)
        if i==27: end=start-timedelta(days=4) # intentional invalid contract
        contracts.append(dict(contract_id=f"CON-{i:04d}",customer_id=cid,start_date=iso(start),end_date=iso(end),arr_usd=25000+(i%6)*25000,status="active"))
        target=AS_OF-timedelta(days=20+i%70); delayed=archetype=="implementation_delay"
        implementations.append(dict(implementation_id=f"IMP-{i:04d}",customer_id=cid,workspace_id=f"WS-{i:04d}",status="delayed" if delayed else "completed",target_go_live_date=iso(target),actual_go_live_date="" if delayed else iso(target-timedelta(days=i%10)),risk_reason="integration dependency" if delayed else ""))
        for d in range(days):
            day=AS_OF-timedelta(days=days-1-d); base=20+(i%18)
            active=base+rng.randint(-4,5); workflows=active*(3+rng.randint(0,3)); breached=rng.randint(0,2)
            if archetype=="adoption_collapse" and d>days-31: active=max(0,active-25); workflows=max(0,workflows-70)
            if archetype=="stale_risk": active=base+15+rng.randint(0,8); workflows=active*7
            if archetype=="telemetry_gap" and d in range(days-20,days-14): continue
            usage.append(dict(usage_id=f"USE-{i:04d}-{d+1:04d}",customer_id=cid,workspace_id=f"WS-{i:04d}",usage_date=iso(day),active_users=active,workflows_run=workflows,sla_breach_count=breached,ingested_at=(datetime.combine(day,datetime.min.time(),timezone.utc)+timedelta(hours=2 if not (i==19 and d%17==0) else 72)).isoformat().replace("+00:00","Z")))
        scenario={"adoption_collapse":("at_risk","adoption decline","Ask CSM to validate workflow adoption and schedule recovery plan"),"ticket_cluster":("at_risk","support burden","Route P1/P2 incident review to Support with CSM visibility"),"implementation_delay":("watch","implementation delay","Professional Services to unblock integration dependency"),"renewal_watch":("watch","renewal and weak engagement","CSM to confirm sponsor and renewal plan"),"telemetry_gap":("watch","missing telemetry","Data/CSM verification before risk outreach"),"stale_risk":("healthy","stale risk flag","Verify stale flag and recalibrate health score")}.get(archetype)
        if scenario: truth.append(dict(scenario_id=f"SCN-{i:04d}",customer_id=cid,expected_label=scenario[0],primary_driver=scenario[1],recommended_action=scenario[2],evidence=f"Planted archetype: {archetype}"))
        docs.append(dict(document_id=f"DOC-{i:04d}",customer_id=cid,document_type="implementation_plan",updated_at=iso(AS_OF-timedelta(days=i%50)),title=f"{name} rollout plan",body=f"Fictional {name} implementation plan. Owner is Professional Services. Current archetype is {archetype}.",source_url=f"nexaflow://documents/DOC-{i:04d}"))
        comms.append(dict(communication_id=f"COM-{i:04d}",customer_id=cid,occurred_at=iso(AS_OF-timedelta(days=(i*9)%90)),channel="email",direction="outbound",sentiment="neutral" if archetype!="renewal_watch" else "concerned",summary="Fictional customer-success check-in."))
    for k in range(1,ticket_target+1):
        i=((k-1)%n)+1; cid=f"CUST-{i:04d}"; archetype=ARCHETYPES[(i-1)%len(ARCHETYPES)]; sev="P1" if archetype=="ticket_cluster" and k%4==0 else ("P2" if archetype=="ticket_cluster" else "P3")
        opened=AS_OF-timedelta(days=(k*3)%days); open_ticket=archetype=="ticket_cluster" and k%3==0
        resolved="" if open_ticket else iso(opened+timedelta(days=1+k%5))
        if k==17: resolved=iso(opened+timedelta(days=1)) # open status inconsistency below
        tickets.append(dict(ticket_id=f"TKT-{k:05d}",customer_id=cid,severity=sev,status="open" if open_ticket or k==17 else "resolved",opened_at=iso(opened),resolved_at=resolved,category="Integration" if k%5 else "workflow-config",title="Fictional workflow support request"))
    tables={"customers":customers,"contacts":contacts,"contracts":contracts,"implementations":implementations,"usage_daily":usage,"support_tickets":tickets,"communications":comms,"documents":docs,"ground_truth":truth}
    for table, rows in tables.items(): write(out/f"{table}.csv", list(rows[0]) if rows else [], rows)
    (out/"manifest.json").write_text(json.dumps({"profile":args.profile,"seed":args.seed,"as_of_date":iso(AS_OF),"counts":{k:len(v) for k,v in tables.items()},"intentional_defects":["CUST-0027 invalid contract dates","TKT-00017 open status with resolved_at","telemetry gap archetypes","delayed ingestion rows"]},indent=2),encoding="utf-8")
    print(f"Generated {args.profile} data in {out}")
if __name__ == "__main__": main()
