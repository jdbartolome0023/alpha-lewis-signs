---
name: account-auditor
description: Runs a full Google Ads account audit across structure, settings, performance, and waste. Use when the user says 'audit my account', 'PPC audit', 'full account review', 'health check my ads', or inherits/reviews an account. Produces a comprehensive prioritized audit covering structure, tracking, bidding, keywords, ads, budget, and waste - the master diagnostic that routes to the specialist skills.
---

# account-auditor

*Cluster: Analysis & Reporting . Part of the 35 Google Ads Skills set by Vicky Lalwani, Digital Marketing Director.*

## Purpose

Deliver a comprehensive, prioritized account audit - structure, tracking, bidding, keywords, ads, extensions, budget, and waste - that surfaces every issue and routes each to the right fix.

## When to use

- Taking over or inheriting an account
- A quarterly or onboarding full review
- Performance is off and the cause is unclear
- The user wants the complete picture before deciding what to fix

## Inputs required

- Account access or a full performance export (required)
- The goals and target CPA/ROAS (required)
- Optional: account history, the budget, business context

## Step-by-step instructions

1. Audit foundations first: conversion tracking accuracy (route to conversion-tracker-qa) - everything else is unreliable if this is broken.
2. Audit structure: campaign and ad group organization, naming, themed grouping (route to campaign-architect / skag-builder).
3. Audit bidding: strategy fit and target realism (route to bid-strategy-advisor).
4. Audit keywords and search terms: coverage, match types, negatives, waste (route to search-term-auditor / negative-keyword-builder).
5. Audit ads and extensions: ad strength, CTR, extension coverage (route to rsa-strength-grader / ctr-optimizer / ad-extension-builder).
6. Audit budget and waste: allocation and leaks (route to budget-allocator / wasted-spend-auditor). Compile every finding into one prioritized list by impact, with the owning skill.

## Output format

A prioritized audit report grouped by area, each finding with severity, impact, and the specialist skill that fixes it. Topped by an executive summary of the 5 biggest opportunities.

## Quality checklist

- [ ] Conversion tracking is audited first (it gates everything)
- [ ] All major areas are covered (structure, bidding, keywords, ads, budget)
- [ ] Each finding has a severity and impact
- [ ] Each fix is routed to the right specialist skill
- [ ] The report opens with the 5 highest-impact opportunities

## Optimization notes

This is the master diagnostic - its job is to find and prioritize, then hand off. Always start with conversion tracking; if that's broken, every performance number in the audit is fiction. End with a tight executive summary: a 40-point audit nobody acts on is worthless, but the top 5 opportunities ranked by impact get done.
