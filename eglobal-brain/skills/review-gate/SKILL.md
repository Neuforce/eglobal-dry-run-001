---
name: review-gate
description: Run a human-in-the-loop gate for a phase folder. Build a review packet (sample + all flagged items), capture approve/correct/reject decisions, apply them, log them, and turn generalizable corrections into RULES.md rules.
argument-hint: "<phase-folder e.g. 01-legacy | 02-asis | 03-code | 04-audit | 05-spec/CAP-… | 06-poc/POC-…>"
---
# Skill: review-gate
**Agent:** `verifier` assists with the packet.

## Inputs
- `<phase>/output/**` (or the capability/PoC folder)
- `<phase>/RULES.md`, `guide/02-human-in-the-loop.md` (sampling, thresholds, RACI)
- `templates/review-log-entry.md`

## Steps
1. Identify the gate, the approver (RACI), and the items in scope.
2. **Build the packet:**
   - Random sample of `proposed` KUs (rate per the HITL guide), plus **all** items that are L-confidence, ⚠️, ❓, `needs-source`, or flagged by `verifier`.
   - Show each item compactly: ID · statement · citation · excerpt · agent note.
   - For `04-audit`: present the DISC records grouped by impact, with the evidence table and recommendation.
3. **Collect decisions** from the human: `approve` | `correct: …` | `reject: …`. Go in batches of ~10. Never assume a decision.
4. **Apply:** update each item's `status` (`approved` / `corrected` / `rejected`), its text, and the reviewer and date. For 04-audit, fill the DISC "Decision" section and add an entry to `review/decision-log.md`.
5. **Learn:** for each correction, ask "Does this generalize?" If yes, draft an `R-<phase>-###` rule (format in RULES.md), show it, and add it after confirmation.
6. **Log:** append the session to `<phase>/review/*-log.md` (newest first), with the accuracy.
7. **Gate decision:** if accuracy ≥ threshold and nothing is pending, ask the approver to confirm the gate passed. Remind them to set the banner to `✅ APPROVED` and to add a line to `decisions/approvals.md`. Otherwise, recommend a re-run with the new rules.

## Rules
- Only humans approve. Never change a banner to ✅ yourself.
- Keep the corrected and rejected items, with the reason. They are evidence.
