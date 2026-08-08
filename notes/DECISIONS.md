# Decisions

This file records important course, repository, and design decisions together
with the rationale behind them. Add entries when future maintainers or agents
would benefit from understanding why a choice was made.

## Decision log

### 2026-08-07 — Keep Lecture 00 diagram styles local

- **Decision:** Keep `slides/00-why-linear-algebra.css` local to Lecture 00.
- **Rationale:** The completed CSS audit found possible reusable MATH 332
  components—`diagram-label`, `diagram-flow`, `diagram-node`,
  `diagram-arrow`, and `diagram-image`—but no demonstrated second use yet.
- **Consequences:** Wait until a second MATH 332 deck actually needs a
  component before creating a course-wide stylesheet. Consider promotion to
  `classlib` only after demonstrated cross-course reuse. Constructions
  specific to Lecture 00 remain local.
