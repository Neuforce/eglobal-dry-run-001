# FAQ

> **🟩 METHOD — NeuForce standard.** Review optional; propose changes via PR. **Owner:** NeuForce

**Do we need Claude?** No. Any agent that can read Markdown and use MCP works (Gemini, Codex, Devin). Claude Code just gets `/slash` shortcuts.

**Does NeuForce need access to our code?** No. The agent reads your code on your side through a read-only MCP. Only knowledge (rules with citations) goes into this repo.

**What if a document can't be connected through MCP?** Export it to `input/raw/` in the matching phase folder and list it in `00-context/sources.md`.

**What if the agent gets something wrong?** Correct it at the gate. `/review-gate` turns your correction into a rule so the mistake isn't repeated.

**Can we skip phases?** Phases 1–3 can run in parallel. Phase 4 needs all three. Phase 6 needs the architecture inputs.

**What is the first thing to do?** Steps 0 and 1 of `guide/00-prompt-guide.md`, then the files marked 🟥 in `README.md`.
