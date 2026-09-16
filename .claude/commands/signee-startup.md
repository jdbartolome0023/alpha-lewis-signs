---
name: signee-startup
description: Start a Signee (Alpha Lewis Signs) work session. Pulls latest from GitHub, reads Google Ads Tasks/master-tracker.md and CLAUDE.md, and surfaces outstanding and completed items.
---

# Signee (Alpha Lewis Signs): Session Startup

## Step 1: Pull latest from GitHub

```bash
cd "/Users/josette/Desktop/Personal/Alpha Lewis Signs"
git pull origin main
```

Report any new files pulled or conflicts.

## Step 2: Read the state files

Read:
- `CLAUDE.md` (account details, writing/reporting rules)
- `Google Ads Tasks/master-tracker.md` (outstanding items, lessons learned, completed log)

## Step 3: Check Gmail before reporting status

Search for replies from Kim (kim@alphalewissigns.com.au) or Nic (nic@alphalewissigns.com.au) since the last session, especially:
- Google Ads invite acceptance confirmations
- Billing setup completion
- Any questions on the step-by-step email sent Sep 16 2026

Do not report a gap or an "all clear" without checking mail first.

## Step 4: Verify Google Ads account state directly (once Kim/Nic report billing is done)

If the tracker's "Full Setup Checklist" (all phases) section shows billing as still pending, but Gmail suggests Kim/Nic have acted, check the account directly:
- Admin > Account settings on CID 715-970-4117 - confirm Time zone shows an Australian zone (not Philippine Standard Time) and currency is AUD
- Do not trust wizard-screen previews - only Admin > Account settings is authoritative (see "Lessons learned" in Google Ads Tasks/master-tracker.md for why)

## Step 5: Surface what needs attention

From `Google Ads Tasks/master-tracker.md`, identify:
- Unchecked items in "Full Setup Checklist" (all phases)
- Anything now resolved based on Gmail/account checks in Steps 3-4 (flag for the user to confirm before checking off)

## Step 6: Print the session brief

```
## Signee: Session Brief [DATE]

**Outstanding:**
- [item]

**Resolved since last session (needs confirmation):**
- [item]

**Next up:**
- [the single next actionable item, e.g. "build GTM/GA4" or "wait on Kim's billing confirmation"]
```

Lead with the most urgent item. If everything in "Full Setup Checklist" (all phases) is still genuinely blocked on Kim/Nic, say so plainly rather than inventing busywork.
