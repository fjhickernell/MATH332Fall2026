# Next task

## Current task

Resume the instructor review of Lecture 01 and review the Lecture 00 companion
notebook.

## Current state

- Lecture 01 now has a 39-slide revised deck. Three shared slides about
  significant institutional and broader change follow the title slide and
  precede the Course Map; the instructional deck remains organized around
  reversible transformations of equations. Instructor review is complete
  through the entire `# Compress the Repeated Structure` block. Resume review
  at the beginning of `# Eliminate on Matrices`; that block and the later
  slides still need review.
- The deck begins with scalar equations and concrete zero/one/infinitely-many
  solution sets, develops elimination on equations, and only then introduces
  dot products, `\mat{A}\vct{x}=\vct{b}`, augmented matrices, pivots, echelon
  form, RREF, consistency, and free variables.
- Dot-product notation now uses `\vct{a}^{\top}\vct{x}`. The deck defines its
  geometric interpretation, orthogonal and parallel vectors, normal vectors,
  hyperplanes in $\mathbb{R}^n$, and the role of parallel equations in the
  zero/infinitely-many outcomes. New 2-D line and 3-D plane diagrams make the
  geometry explicit.
- One recurring three-variable system connects equation-level elimination to
  augmented-matrix elimination. Elementary matrices and nonsingularity appear
  only as a closing preview.
- The reviewed portion has received an instructor and visual revision pass.
  Key revised slides have been inspected at the standard RevealJS viewport,
  and all seven decks render successfully with the `qmcpy` kernel. Course-wide
  diagram primitives now live in `slides/math332-slides.scss`; Deck 00 retains
  only its one-off diagram construction.
- No Lecture 01 notebook exists yet. The deck sketches a small SymPy companion
  using `Matrix` and the standard `qmcpy` kernel.
- The Lecture 00 demonstration notebook still awaits instructor review and is
  a coequal next priority with finishing the Lecture 01 deck review.

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
- Keep Lecture 00 content unchanged except for separately requested future
  polish.
- Reuse the established course-wide diagram primitives before adding
  deck-specific styling.

## Done when

- The Lecture 01 deck has been reviewed from `# Eliminate on Matrices` through
  the end.
- The Lecture 00 companion notebook has received an instructor review, and any
  requested revisions have been validated from a clean `qmcpy` kernel.
