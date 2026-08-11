# Technical Notes

This file records repository architecture, implementation notes, maintenance
knowledge, and technical context useful to future maintainers and agents. Keep
details here when they are durable but too specific for `AGENTS.md`.

## Repository notes

### Lecture 00 handoff — 2026-08-07

- `slides/00-why-linear-algebra.qmd` is largely complete. Its opening now
  establishes scalar, vector, matrix, and tensor representations, then makes
  matrix action explicit. The main examples cover images, regression,
  transformations, composition, systems and least squares, networks and
  repeated action, and machine learning.
- `# Compute responsibly` now distinguishes ill-posedness, ill-conditioning,
  numerical instability, and computational cost. Its cancellation example is
  an executable NumPy/Jupyter cell whose values are rendered as a table.
- The MATH 565-style logistics material in `# The course ahead` has been
  adapted to MATH 332 and is substantially complete: the website links,
  Schedule route to slides, and the currently documented website/Canvas
  division are present. Unresolved submission and quiz procedures remain
  identified as unconfirmed rather than invented.
- The deck currently has **30 slides**. The latest Lecture 00 render completed
  successfully on 2026-08-07; revised slides were visually checked for
  overflow, section navigation was verified, and the new relative course-page
  links were checked against generated site pages.
- The remaining Lecture 00 issue is only the conceptual wrap-up surrounding
  the logistics slides. The final abstract roadmap and closing have not yet
  been approved; do not describe the whole final section as unfinished.

### Lecture 01 first substantive draft — 2026-08-11

- `slides/01-systems-and-matrices.qmd` contains 27 slides. It begins with
  equations and concrete solution sets, motivates elementary row operations by
  reversibility, and performs elimination on equations before introducing
  matrices.
- A single three-variable system recurs through equation elimination, row-dot-
  product interpretation, augmented-matrix notation, echelon form, and RREF.
  Variants of its last row motivate inconsistency and free variables before the
  general zero/one/infinitely-many classification is stated.
- The closing computation slide plans a small SymPy companion notebook using
  `Matrix` and the `qmcpy` kernel. Elementary matrices and nonsingularity are
  only previewed near the end.
- The deck, root website, and all seven decks rendered successfully on
  2026-08-11. The recurring example and free-variable parametrization were
  checked with SymPy, and assembled-site navigation was verified.
- Live browser inspection was unavailable during drafting. Before treating the
  deck as classroom-ready, inspect every slide at the standard RevealJS
  viewport and fix overflow, spacing, pacing, or density issues.
