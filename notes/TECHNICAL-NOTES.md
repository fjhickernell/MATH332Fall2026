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
