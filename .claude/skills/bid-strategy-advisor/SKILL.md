---
name: bid-strategy-advisor
description: Recommends the right Google Ads bidding strategy for a campaign's goal and data. Use when the user says 'bidding strategy', 'which bid strategy', 'manual vs smart bidding', 'tCPA or tROAS', 'maximize conversions', or is choosing how to bid. Matches the bidding strategy to the goal, the conversion volume, and the account's maturity, with the settings and prerequisites.
---

# bid-strategy-advisor

*Cluster: Performance & Optimization . Part of the 35 Google Ads Skills set by Vicky Lalwani, Digital Marketing Director.*

## Purpose

Match the bidding strategy to the campaign's goal, conversion volume, and maturity - so the account uses the strategy that actually fits its data, not a default that starves or misfires.

## When to use

- Choosing or changing a bidding strategy
- Deciding if there's enough data for Smart Bidding
- Switching from manual to automated (or troubleshooting after a switch)
- A bidding strategy isn't performing

## Inputs required

- The campaign goal (leads, ROAS, volume, awareness) (required)
- Recent conversion volume (required - Smart Bidding needs data)
- Optional: current strategy, account maturity, seasonality

## Step-by-step instructions

1. Clarify the goal: maximize conversions (volume), tCPA (cost control), tROAS (revenue efficiency), maximize clicks (traffic), or manual (full control).
2. Check conversion volume - Smart Bidding needs enough conversions to learn (roughly 30+/month for tCPA, more for tROAS). Thin data means manual or maximize-conversions first.
3. Match strategy to goal and data: new/low-volume campaigns start broad (maximize conversions) to gather data, then graduate to tCPA/tROAS once volume supports it.
4. Set realistic targets - a tCPA far below the current CPA chokes delivery; a tROAS too high limits volume.
5. Note the prerequisites: accurate conversion tracking is mandatory, and a learning period (1-2 weeks) where performance is unstable.
6. Output the recommended strategy, the settings, the prerequisites, and what to expect during learning.

## Output format

A bidding recommendation: strategy, target settings, prerequisites (tracking, volume), the learning-period expectation, and a graduation path as data grows.

## Quality checklist

- [ ] Strategy matches the goal AND the available conversion volume
- [ ] Targets are realistic relative to current performance
- [ ] Conversion-tracking accuracy is flagged as a prerequisite
- [ ] The learning period and its instability are explained
- [ ] A graduation path (manual -> maximize -> tCPA/tROAS) is given where relevant

## Optimization notes

Smart Bidding is only as good as the conversion data feeding it - garbage tracking produces garbage bids. Confirm tracking first. Don't set an aggressive tCPA/tROAS out of the gate; it strangles delivery before the algorithm learns. And respect the learning period: judging Smart Bidding after three days is how people panic and revert too early.
