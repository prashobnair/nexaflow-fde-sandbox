#!/usr/bin/env python3
"""Lightweight integrity report; defects marked EXPECTED are teaching scenarios."""
import csv, json
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'data/seed/day1'
def rows(n):
    with (D/n).open(encoding='utf-8',newline='') as f: return list(csv.DictReader(f))
def main():
    cs=rows('customers.csv'); contracts=rows('contracts.csv'); tickets=rows('support_tickets.csv'); usage=rows('usage_daily.csv')
    ids={x['customer_id'] for x in cs}; refs=sum(x['customer_id'] not in ids for x in rows('contacts.csv')+contracts+rows('implementations.csv')+usage+tickets)
    invalid=[x['contract_id'] for x in contracts if x['end_date'] < x['start_date']]
    contradictory=[x['ticket_id'] for x in tickets if x['status']=='open' and x['resolved_at']]
    print(json.dumps({'foreign_key_errors':refs,'EXPECTED_invalid_contract_dates':invalid,'EXPECTED_open_resolved_tickets':contradictory,'usage_rows':len(usage)},indent=2))
    raise SystemExit(1 if refs else 0)
if __name__=='__main__': main()
