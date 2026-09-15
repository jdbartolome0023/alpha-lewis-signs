---
name: budget-allocator
description: Allocates and reallocates budget across campaigns based on performance and goals. Use when the user says 'budget allocation', 'how should I split my budget', 'where to spend', 'reallocate budget', or 'am I spending in the right places'. Analyzes performance by campaign and recommends where to add, hold, or cut budget to maximize return against the goal.
---

# budget-allocator

*Cluster: Campaign Build & Structure . Part of the 35 Google Ads Skills set by Vicky Lalwani, Digital Marketing Director.*

## Purpose

Recommend where budget should move - which campaigns to scale, hold, or cut - based on each one's performance against the goal, so spend concentrates where it returns the most.

## When to use

- Deciding how to split a budget across campaigns
- Monthly budget reallocation
- A campaign is capped by budget while others underperform
- The user asks where they should be spending more or less

## Inputs required

- Total budget and the primary goal (ROAS, CPA, lead volume) (required)
- Per-campaign performance: spend, conversions, CPA/ROAS, impression share lost to budget (required)
- Optional: business priorities that override pure efficiency

## Step-by-step instructions

1. Pull each campaign's spend, conversions, CPA or ROAS, and impression share lost to budget.
2. Identify scale opportunities: campaigns hitting the goal that are limited by budget (high impression share lost to budget = leaving volume on the table).
3. Identify cut candidates: campaigns well off the goal with no improving trend.
4. Identify hold campaigns: on-goal but not budget-limited, or still in learning.
5. Balance pure efficiency against stated business priorities (a strategic line may justify a higher CPA).
6. Output the reallocation: per campaign, current spend -> recommended spend, with the reason and the expected impact.

## Output format

A reallocation table: Campaign | Current spend | Recommended spend | Action (scale/hold/cut) | Reason | Expected impact. Plus a one-line summary of the net change.

## Quality checklist

- [ ] Impression share lost to budget is checked to find capped winners
- [ ] Cut candidates show a sustained off-goal trend, not one bad week
- [ ] Business priorities can override pure efficiency where stated
- [ ] Each recommendation has an expected impact
- [ ] The reallocation nets to the available total budget

## Optimization notes

The fastest PPC win is usually reallocation, not optimization: a winning campaign capped by budget is leaving money on the table while a loser bleeds it. Always check impression share lost to budget. Don't cut on a single bad week - look for trend. And respect strategic priorities; the lowest-CPA campaign isn't always the most valuable.
