---
name: status
description: Show where the project is — file review status (🟥/🟨/🟩/✅), phase progress, open gates, pending decisions and open questions — and refresh STATUS.md.
---
# Skill: status

## Steps
1. Run `scripts/review-status.sh` (or scan the banners manually if you can't run shell commands).
2. For each phase: does the output exist? Last review-log entry? Gate passed?
3. Count the pending ⚠️/❓ without decisions, `needs-source` KUs, and unanswered open questions.
4. Rewrite `STATUS.md` with: a phase table, blockers (🟥 files by owner), next recommended step (from `guide/00-prompt-guide.md`).
5. Print a short summary.
