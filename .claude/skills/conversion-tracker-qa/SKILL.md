---
name: conversion-tracker-qa
description: Audits Google Ads conversion tracking to make sure the data driving bids is accurate. Use when the user says 'conversion tracking', 'is my tracking working', 'check my conversions', 'tracking QA', 'are my conversions accurate', or suspects tracking problems. Audits conversion setup, attribution, double-counting, and tracking gaps - because Smart Bidding is only as good as the data it learns from.
---

# conversion-tracker-qa

*Cluster: Performance & Optimization . Part of the 35 Google Ads Skills set by Vicky Lalwani, Digital Marketing Director.*

## Purpose

Verify that conversion tracking is accurate and complete - no double-counting, no gaps, correct attribution - because every bid decision and optimization depends on the data being right.

## When to use

- Before trusting Smart Bidding or any data-driven decision
- Conversion numbers look too high, too low, or inconsistent
- After a site change, migration, or tracking setup
- A periodic tracking health check

## Inputs required

- The conversion actions being tracked (required)
- How they're set up (Google tag, GA4 import, offline import, call tracking) (required)
- Optional: the conversion data, the attribution model in use

## Step-by-step instructions

1. List every conversion action and how each is tracked.
2. Check for double-counting: the same conversion fired by two methods, or 'every' vs 'one' counting set wrong (leads should count one, sales may count every).
3. Check for gaps: conversions not tracked at all (phone calls, offline sales, micro-conversions that should inform bidding).
4. Check attribution: is the model appropriate (data-driven is usually best), and is the conversion window sensible for the sales cycle?
5. Check value: are conversion values assigned where relevant (essential for tROAS), and are primary vs secondary conversion actions set correctly?
6. Output a tracking QA report: each action's status (correct / double-counting / missing / misconfigured) with the fix.

## Output format

A tracking QA report: each conversion action with status (correct / double-counted / gap / misconfigured), the issue, and the fix. Plus an overall data-trust verdict.

## Quality checklist

- [ ] Every conversion action and its method are listed
- [ ] Double-counting (method overlap, count setting) is checked
- [ ] Tracking gaps (calls, offline, key micro-conversions) are flagged
- [ ] Attribution model and conversion window are assessed
- [ ] Conversion values and primary/secondary settings are checked

## Optimization notes

This is the foundation everything else stands on. Smart Bidding optimizes toward your conversion data - if that data double-counts, misses calls, or misattributes, the algorithm optimizes toward the wrong thing and quietly wastes budget. Audit tracking before trusting any automated bidding or any performance conclusion. Bad data is worse than no data.
