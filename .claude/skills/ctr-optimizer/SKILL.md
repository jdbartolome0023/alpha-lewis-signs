---
name: ctr-optimizer
description: Finds ads and keywords with low click-through rate and improves them. Use when the user says 'low CTR ads', 'improve ad CTR', 'my ads aren't getting clicked', 'CTR optimization', or wants more clicks from existing impressions. Identifies the under-clicking ads, diagnoses the cause, and routes to copy, extension, or relevance fixes ranked by impact.
---

# ctr-optimizer

*Cluster: Performance & Optimization . Part of the 35 Google Ads Skills set by Vicky Lalwani, Digital Marketing Director.*

## Purpose

Lift click-through rate on the ads and keywords that under-click for their position - through better copy, extensions, and relevance - so the account earns more clicks from impressions it already has.

## When to use

- Ads have impressions but low CTR
- The user wants more clicks without more spend
- CTR is dragging Quality Score and raising CPC
- Refreshing fatigued ads

## Inputs required

- Ad and keyword performance: impressions, clicks, CTR, position (required)
- The current ad copy and extensions (required)
- Optional: position benchmarks, the goal

## Step-by-step instructions

1. Pull CTR by ad and keyword alongside average position - low CTR matters most where position is high (the ad is seen but ignored).
2. Benchmark CTR against the position - what looks low at the top is fine lower down.
3. Diagnose the cause for under-clickers: weak headline, no keyword in the ad, missing extensions, weak offer, ad fatigue (CTR declining over time).
4. Route the fix: copy weakness -> rsa-writer; missing extensions -> ad-extension-builder; relevance -> skag-builder; fatigue -> new creative.
5. Rank opportunities by potential click gain (impressions x CTR gap).
6. Output the under-performers with cause, fix, and expected click gain.

## Output format

A CTR opportunity list: Ad/keyword | Position | CTR vs benchmark | Cause | Fix (and which skill) | Expected click gain. Ranked by impact.

## Quality checklist

- [ ] CTR is benchmarked against position, not a flat number
- [ ] High-position low-CTR ads are prioritized
- [ ] The cause is diagnosed before prescribing a fix
- [ ] Ad fatigue (declining CTR over time) is checked
- [ ] Opportunities are ranked by potential click gain

## Optimization notes

CTR is a compounding metric: it drives clicks today and lifts Quality Score (lowering CPC) tomorrow. Prioritize high-position, low-CTR ads - they're being seen and skipped, the clearest sign the copy or offer is weak. Watch for fatigue: a once-strong ad whose CTR is sliding needs fresh creative, not a tweak.
