# Next task

## Current task

Review and refine the Lecture 01 companion notebook draft.

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
  dependent three-plane systems, and readable geometric diagrams. Its
  resistance-network exercise uses three clockwise mesh currents and a
  coupled $3\times3$ system; replacing the first top and left vertical
  resistances by ideal wires creates a short circuit and the contradiction
  row $[\,0\ 0\ 0\mid9\,]$.
- `notebooks/demonstrations/01-systems-and-matrices.ipynb` is now an executable
  32-cell working draft linked from the deck and the Notebooks page. It uses
  SymPy for exact row operations, echelon forms, augmented-rank classification,
  parameterized solutions, and exact residuals; it uses NumPy for unique
  floating-point solves, numerical residuals, and rank checks. Prediction
  prompts precede the zero/one/infinitely-many comparison and the
  resistance-network computations.
- The recurring system is isolated in one clearly marked editable `A`, `b`
  cell. Exact reusable routines display every forward-elimination operation
  and each bottom-to-top back-substitution calculation. Student directions
  explain how to change the equations and restart and run all cells; singular
  edits report that unique back substitution or a NumPy square solve does not
  apply instead of stopping execution.
- All 15 code cells execute without errors using the `qmcpy` kernel. The draft
  explicitly warns that numerical rank deficiency does not distinguish no
  solutions from infinitely many and keeps the exact SymPy analysis
  authoritative for that distinction.
- Shared presentation guidance now names the 47%–6%–47% two-column layout the
  **Pomona gutter**.

## Questions to resolve

- Whether the draft has the right depth and pacing for its first classroom use.

## Constraints

- Use Anton Chapter 1 as the course spine and the established MATH 332
  notation.
- Preserve the equations-first, reversibility-first narrative.
- Keep mathematical exposition authoritative in the RevealJS deck.
- Treat the notebook as a computational companion rather than a second source
  of mathematical content.
- Use SymPy `Matrix` for readable matrix displays and the `qmcpy` kernel.
- Use NumPy for floating-point solves and residual checks without letting
  numerical rank heuristics replace exact structural interpretation.
- Reuse the established course-wide diagram primitives before adding
  deck-specific styling.

## Done when

- The working draft has been instructor-reviewed and refined into a polished
  computational companion that executes cleanly with the `qmcpy` kernel,
  supports rather than duplicates the deck, and preserves working deck and
  website links.
