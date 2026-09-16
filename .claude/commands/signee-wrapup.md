---
name: signee-wrapup
description: Wrap up a Signee (Alpha Lewis Signs) work session. Logs the day's findings/fixes into Google Ads Tasks/master-tracker.md, shows what changed, commits, and pushes to GitHub.
---

# Signee (Alpha Lewis Signs): Session Wrap Up

Log everything from this session and push to GitHub. This covers the whole session's work, not just already-staged files - findings, fixes, replies, and open items discussed but not yet written down.

## Step 1: Log the session into Google Ads Tasks/master-tracker.md

Before checking git status, review the conversation and make sure `Google Ads Tasks/master-tracker.md` reflects everything from this session:
- New items completed - move/add to "Completed" with today's date
- New items discovered or still open - add to "Immediate - Outstanding"
- Any new lessons learned about the account/site/client - add to "Lessons learned" if applicable

Do not skip this step even if it feels redundant - the tracker is the record, not the chat log.

## Step 2: Check what changed

```bash
cd "/Users/josette/Desktop/Personal/Alpha Lewis Signs"
git status
```

List all changed/new files, not just the tracker - check for anything else touched this session (skills, CLAUDE.md, reports, scripts).

## Step 3: Stage changed files

Add the specific files that changed this session. Do not use `git add -A` blindly - review the list first in case anything sensitive or unrelated shows up.

```bash
git add "Google Ads Tasks/master-tracker.md"
# Add any other specific files that changed this session
```

## Step 4: Write a clear commit message

Summarize what the session actually did, e.g.:
- `"Confirm no GTM/GA4/GSC live on site, log Google Ads account setup"`
- `"Google Ads: campaign draft build, Kim/Nic invites sent"`

```bash
git commit -m "[message]"
```

## Step 5: Push to GitHub

```bash
git push origin main
```

If this fails with a permission error, check `gh auth status` - this repo needs the `jdbartolome0023` GitHub account active, not `josetteb-ai`.

## Step 6: Confirm

Report:
- Files committed
- Commit message used
- Push status (success or any errors)
- Note if there was nothing to commit
