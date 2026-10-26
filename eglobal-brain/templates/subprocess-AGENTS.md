<!--
PURPOSE:     Executable context for agents (and developers) building or operating ONE capability/subprocess.
OWNER:       Agent drafts with the SDD · Tech Lead approves
FILE:        05-spec/CAP-###-<slug>/AGENTS.md (later copied into the implementation repo)
-->
# AGENTS.md: CAP-###-<slug>

## Purpose
<!-- What this capability does, in 3 lines -->

## Source of truth
- Spec: `./sdd.md` (requirements REQ-…), `./prd.md`
- Validated As-Is: `04-audit/output/validated-asis/<P-PROC>.md`
- Architecture: `00-context/architecture/` (standards, platform)

## Inputs / outputs
## Rules you must obey
1. Implement only the requirements in `sdd.md`. Unknowns become questions, not assumptions.
2. Follow `standards.md` (language, logging, errors, tests).
3. Every test references a REQ/AC ID.
4. <!-- capability-specific business rules that are easy to get wrong -->

## Files you may touch
## Commands
```bash
# build · test · run locally · deploy (dry-run)
```
## Definition of done
- [ ] All ACs have passing tests
- [ ] Manifests validate
- [ ] Deviations documented
