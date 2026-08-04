# AGENTS.md

At the beginning of every new Codex session, reconstruct the project state
from the repository. Read `README.md`, `PLAN.md`, `STATUS.md`,
`AUTHOR_WORKFLOW.md`, and then `AGENTS.md`; inspect Git status, submodule
status, and recent commits before substantial work.

## Repository boundaries

- `MATH332Fall2026` is authoritative for this course.
- `MATH565Fall2026` is a read-only architectural reference.
- MATH 332 course content stays in this repository.
- Reusable tooling belongs in HickernellAcademicLib only after validation and
  an upstream commit.
- Do not modify reference repositories unless explicitly instructed.
- Initialize the recorded `classlib` commit recursively; do not update it to a
  moving branch tip during routine setup or validation.

## Slides

The RevealJS decks in `slides/` are the authoritative course presentation
materials. Mathematical content must be maintained only in its corresponding
deck.

Follow the classlib-based RevealJS architecture proven in MATH565Fall2026:
shared options and styling, metadata-driven deck titles, title-slide
conventions, major-section organization, and previous/next deck navigation.

Jupyter notebook LaTeX macros cannot be assumed to propagate from Quarto or
RevealJS, so notebooks should use self-contained notation when necessary.

## Validation

Render the root website and the independent `slides/` project. Stage slide
output beneath `_site/slides` for an assembled-site check. Review every
warning or error, verify all seven decks and their navigation, and keep
generated files out of Git.

## Git and checkpoints

Do not commit or push unless the user's message begins with the exact word
`Checkpoint`. A message beginning with `Checkpoint` authorizes the validation,
staging, commit, and push workflow described by the applicable global
instructions. Ordinary work must remain uncommitted and unpushed.
