---
name: wasted-spend-auditor
description: Finds wasted ad spend across the account and quantifies the leak. Use when the user says 'wasted spend', 'where am I losing money', 'budget leaks', 'find waste', or wants to cut inefficient spend. Audits search terms, keywords, placements, audiences, and devices for spend with no return, then ranks the leaks by cost and gives the fix for each.
---

# wasted-spend-auditor

*Cluster: Performance & Optimization . Part of the 35 Google Ads Skills set by Vicky Lalwani, Digital Marketing Director.*

## Purpose

Find and quantify where the account is spending without returning - across search terms, keywords, placements, devices, and times - and rank the leaks so the biggest waste gets cut first.

## When to use

- CPA is too high or ROAS too low
- The user wants to cut waste before adding budget
- A periodic efficiency audit
- Diagnosing a spend that isn't converting

## Inputs required

- Account performance: spend and conversions by keyword, search term, placement, device, time (required)
- The goal (CPA/ROAS target) (required)
- Optional: the date range, conversion lag considerations

## Step-by-step instructions

1. Pull spend and conversion data across dimensions: search terms, keywords, placements (Display/PMax), audiences, devices, and dayparts.
2. Find spend with zero or far-below-target return in each dimension, accounting for conversion lag so recent spend isn't unfairly flagged.
3. Quantify each leak: how much is being spent with no/poor return.
4. Identify the cause per leak: irrelevant search terms (add negatives), losing keywords (pause/adjust), bad placements (exclude), underperforming devices/times (bid down).
5. Rank all leaks by wasted cost - fix the biggest first.
6. Output the ranked waste list with the cost, the cause, and the specific fix for each.

## Output format

A ranked waste report: Leak | Dimension | Wasted spend | Cause | Fix. Biggest cost leaks first, with the total recoverable spend summarized.

## Quality checklist

- [ ] Multiple dimensions are checked, not just keywords
- [ ] Conversion lag is accounted for before flagging recent spend
- [ ] Each leak is quantified in actual cost
- [ ] The cause and a specific fix accompany each leak
- [ ] Leaks are ranked by wasted spend

## Optimization notes

Cutting waste is faster and safer than chasing new wins - the money's already being spent. But mind conversion lag: pausing a keyword that converts on a 14-day cycle because it shows zero conversions in the last 7 days is a mistake. Always frame the date window against the conversion lag before declaring something wasteful.
