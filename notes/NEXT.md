# Next task

## Current task

Develop the Lecture 01 companion notebook.

## Current state

- Lecture 01 instructor review is complete through the end of the deck. The
  heading hierarchy and section-overview links have been audited, and all
  seven decks render successfully.
- The deck begins with scalar equations and concrete zero/one/infinitely-many
  solution sets, develops elimination on equations, and only then introduces
  dot products, matrix multiplication, `\mat{A}\vct{x}=\vct{b}`, augmented
  matrices, pivots, echelon form, consistency, and free variables. Reduced row
  echelon form is intentionally omitted because the course computation uses
  Gaussian elimination and back substitution.
- One recurring three-variable system connects equation-level elimination to
  augmented-matrix elimination and now has solution $(-1,2,1)$. The deck also
  includes a required row exchange, reverse-engineered inconsistent and
  dependent three-plane systems, readable geometric diagrams, and a
  three-node resistance-network exercise with a 9 V source and kilohm
  resistors.
- `notebooks/demonstrations/01-systems-and-matrices.ipynb` is a valid placeholder
  linked from the deck and the Notebooks page. Its planned scope is SymPy
  Gaussian elimination, comparison of zero/one/infinitely-many solution sets,
  and the resistance-network exercise.
- Shared presentation guidance now names the 47%–6%–47% two-column layout the
  **Pomona gutter**.

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
- Reuse the established course-wide diagram primitives before adding
  deck-specific styling.

## Done when

- The placeholder is replaced by a polished computational companion that uses
  SymPy `Matrix`, executes cleanly with the `qmcpy` kernel, supports rather
  than duplicates the deck, and preserves working deck and website links.
