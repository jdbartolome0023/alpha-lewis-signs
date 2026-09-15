---
name: search-term-auditor
description: Audits the search terms report to find wasted spend and new keyword opportunities. Use when the user says 'search terms', 'search query report', 'what searches triggered my ads', 'find wasted spend', or wants to mine the search terms report. Surfaces irrelevant terms to add as negatives and high-performing terms to add as keywords, both ranked by spend and impact.
---

# search-term-auditor

*Cluster: Keywords & Targeting . Part of the 35 Google Ads Skills set by Vicky Lalwani, Digital Marketing Director.*

## Purpose

Mine the search terms report for the two highest-value moves: irrelevant terms to block as negatives, and converting terms to promote to keywords - both ranked by spend impact.

## When to use

- Weekly or biweekly account maintenance
- Hunting for wasted spend
- Finding new keyword opportunities from real queries
- Diagnosing why a campaign's CPA is high

## Inputs required

- The search terms report (required) - query, impressions, clicks, cost, conversions
- Optional: the goal (CPA/ROAS target), the existing keyword and negative lists

## Step-by-step instructions

1. Pull the search terms report with cost and conversion data.
2. Find the waste: terms with spend but no conversions, and terms clearly irrelevant to the offer. Rank by cost.
3. Find the opportunities: terms with conversions or strong CTR not yet keywords - candidates to add as exact/phrase for control.
4. Find the intent mismatches: terms broad match is pulling in that don't fit, signalling a match-type or negative fix.
5. Recommend the action per term: add as negative, add as keyword, or leave.
6. Output two ranked lists - negatives to add (by wasted spend) and keywords to add (by conversion value).

## Output format

Two ranked lists: Wasted terms to add as negatives (by spend) and Converting terms to add as keywords (by value). Each with the recommended match type.

## Quality checklist

- [ ] Waste is ranked by cost (biggest leaks first)
- [ ] Converting non-keyword terms are surfaced as opportunities
- [ ] Match types are recommended for both negatives and new keywords
- [ ] Intent mismatches from broad match are flagged
- [ ] Both lists are prioritized, not exhaustive dumps

## Optimization notes

This is the single highest-ROI recurring PPC task. The search terms report is where broad match's waste hides and where your best new keywords are revealed by real user behavior. Run it weekly. Promoting a converting term to an exact-match keyword gives you bid control over a proven winner.
