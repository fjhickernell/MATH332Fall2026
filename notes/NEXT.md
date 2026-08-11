# Next task

## Current task

Create and validate the companion demonstration notebook for Lecture 01.

## Current state

- Lecture 01 now has a 33-slide revised deck organized around reversible
  transformations of equations.
- The deck begins with scalar equations and concrete zero/one/infinitely-many
  solution sets, develops elimination on equations, and only then introduces
  dot products, `\mat{A}\vct{x}=\vct{b}`, augmented matrices, pivots, echelon
  form, RREF, consistency, and free variables.
- Dot-product notation now uses `\vct{a}^{\top}\vct{x}`. The deck defines its
  geometric interpretation, orthogonal and parallel vectors, normal vectors,
  and the role of parallel equations in the zero/infinitely-many outcomes.
- One recurring three-variable system connects equation-level elimination to
  augmented-matrix elimination. Elementary matrices and nonsingularity appear
  only as a closing preview.
- The instructor and visual revision pass is complete. The key revised slides
  have been inspected at the standard RevealJS viewport, and all seven decks
  render successfully with the `qmcpy` kernel.
- No Lecture 01 notebook exists yet. The deck sketches a small SymPy companion
  using `Matrix` and the standard `qmcpy` kernel.
- The Lecture 00 demonstration notebook still awaits instructor review; that
  work remains valid but is no longer the immediate slide-development task.

## Questions to resolve

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

- The companion notebook executes from a clean `qmcpy` kernel, demonstrates
  the three solution outcomes without duplicating the lecture, and is linked
  from the notebooks page when ready.
