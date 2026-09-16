---
name: signee-weekly
description: Generate the Signee (Alpha Lewis Signs) weekly task report for Kim, covering Monday-Friday. Pulls completed items from master-tracker.md and Gmail activity, writes the report, and drafts it as an email to Kim.
---

# Signee: Weekly Task Report for Kim

Covers **Monday through Friday of the current week**. This is a task/progress summary, not a performance report - there's no live campaign spend yet. Once campaigns are live and tracking is built, this should evolve to include actual performance metrics (see `kf-google-weekly.md` in the Kenny Fuels project for what that eventually looks like) - don't force metrics into it before there's real data to report.

## Step 1: Confirm the reporting period

State the exact Monday-Friday date range for this week and confirm the output file name (e.g. `weekly-reports/week-sep-15-19.md`).

## Step 2: Pull completed items from the tracker

Read `master-tracker.md`. Pull every entry in "Completed" dated within this week's Monday-Friday range.

## Step 3: Check Gmail for anything not yet logged

Search for sent/received mail with Kim (kim@alphalewissigns.com.au) and Nic (nic@alphalewissigns.com.au) during the period. Cross-check against what's in the tracker - if something happened this week that isn't logged yet (a reply, a call, a decision), add it to master-tracker.md's "Completed" section before writing the report, don't let the report and the tracker drift apart.

## Step 4: Write the report

Create `weekly-reports/week-[dates].md`:

```
# Signee - Week of [Date Range], 2026

## What I did this week

- [task, in plain language Kim can follow without PPC jargon]
- [task]

## Open items / waiting on you

- [anything blocked on Kim or Nic specifically - be direct about what's needed and from whom]

## Next up

- [1-3 items, the next things happening once current blockers clear]
```

Keep it short and readable, not a data dump. Kim is not a PPC person, per her own "such an unknown area to us" comment in the original email thread - write for that audience. No em dashes (see CLAUDE.md).

## Step 5: Draft the email to Kim

Never send directly - create a Gmail draft only (per CLAUDE.md reporting rules). Use the gmail-jdd draft tool:
- To: kim@alphalewissigns.com.au
- Subject: `Signee - Week of [Date Range] Update`
- Body: the report content from Step 4, formatted for email (not raw markdown - convert to plain readable text)

## Step 6: Commit and push

```bash
cd "/Users/josette/Desktop/Personal/Alpha Lewis Signs"
git add "weekly-reports/week-[dates].md"
git commit -m "Weekly report: [date range]"
git push origin main
```

If push fails with a permission error, check `gh auth status` - this repo needs the `jdbartolome0023` GitHub account active.

## Step 7: Confirm

Report the file created, the draft created (with a note that it's sitting in Gmail for review, not sent), and push status.
