### R-4-001 Configurable values are not "confirmed" until the runtime value is known
- **Rule:** When a code KU's value comes from a configurable property with a default, do not classify the match ✅ on the default alone. Open a DISC asking for the production value.
- **Origin:** G4 · Tech Lead (ejemplo) · 2026-10-15 · DISC-EX-002
- **Applies to:** cross-reference, all processes
- **Example:** Doc 25 s vs code default 25 s (configurable) → ❓ until the prod config is confirmed, not ✅.
