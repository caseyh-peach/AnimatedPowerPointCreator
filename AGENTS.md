# AGENTS.md - AnimatedPowerPointCreator

## Review guidelines
<!-- estate-review-block v2 · canonical: caseyh-peach/TheApiary infrastructure/estate-agents-review-block.md -->

- Flag **P1** (bugs, data loss, security holes, broken contracts) and **P2** (real correctness or
  design gaps) only. Do NOT flag style, formatting, naming, or comment nits, and do not propose
  speculative hardening for internal tooling unless the diff touches an auth, input, or SQL boundary.
- **Severity-tag every finding** (`P1:` / `P2:`), tied to file + line, one
  finding per bullet in the gauntlet's round comment. The builder's tooling
  scores rounds by these tags.
- This repo carries **recorded decisions and contracts** (decision trails, BRDs, D-rows). When a
  change looks deliberate, allow that a recorded decision may exist — phrase the finding as
  "verify against the decision trail" rather than asserting the change is wrong.
- The builder agent triages every finding against the contract and may **dispose with citation**;
  do not re-raise a disposed finding unless new code changes the situation.

