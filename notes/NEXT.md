# Next task

## Current task

Review and refine the first substantive Lecture 01 draft in
`slides/01-systems-and-matrices.qmd`, then create its companion demonstration
notebook.

## Current state

- Lecture 01 now has a 27-slide first substantive draft organized around
  reversible transformations of equations.
- The deck begins with scalar equations and concrete zero/one/infinitely-many
  solution sets, develops elimination on equations, and only then introduces
  dot products, `\mat{A}\vct{x}=\vct{b}`, augmented matrices, pivots, echelon
  form, RREF, consistency, and free variables.
- One recurring three-variable system connects equation-level elimination to
  augmented-matrix elimination. Elementary matrices and nonsingularity appear
  only as a closing preview.
- The deck, root website, and all seven decks render successfully. Its example
  RREF and free-variable parametrization have been checked with SymPy, and
  assembled-site deck navigation has been verified.
- Live browser inspection was unavailable during drafting, so Lecture 01 still
  needs a visual pass for overflow, spacing, pacing, and classroom density.
- No Lecture 01 notebook exists yet. The deck sketches a small SymPy companion
  using `Matrix` and the standard `qmcpy` kernel.
- The Lecture 00 demonstration notebook still awaits instructor review; that
  work remains valid but is no longer the immediate slide-development task.

## Questions to resolve

- Which Lecture 01 slides should be tightened, split, or cut after visual and
  instructor review?
- Should RREF remain in Lecture 01 or move later in the Chapter 1 deck?
- How much of the zero/one/infinitely-many comparison should the companion
  notebook automate versus leave for student prediction?

## Constraints

- Use Anton Chapter 1 as the course spine and the established MATH 332
  notation.
- Preserve the equations-first, reversibility-first narrative.
- Keep mathematical exposition authoritative in the RevealJS deck.
- Treat the notebook as a computational companion rather than a second source
  of mathematical content.
- Use SymPy `Matrix` for readable matrix displays and the `qmcpy` kernel.
- Keep Lecture 00 unchanged except for separately requested future polish.
- Do not reorganize or centralize additional CSS.

## Done when

- Every Lecture 01 slide has been visually inspected at the standard RevealJS
  viewport and obvious overflow, spacing, and pacing issues are fixed.
- The instructor has reviewed the deck's scope, organization, recurring
  example, and placement of RREF.
- The companion notebook executes from a clean `qmcpy` kernel, demonstrates
  the three solution outcomes without duplicating the lecture, and is linked
  from the notebooks page when ready.
