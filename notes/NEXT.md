# Next task

## Current task

Develop Deck 03: Matrix Structure and Transformations.

## Current state

- The sequential Deck 00–08 architecture is implemented. Deck 01 remains
  Systems and Matrices, Deck 02 is Inverses and Invertibility, Deck 03 is the
  placeholder for Matrix Structure and Transformations, and Anton Chapters
  2–6 are represented by Decks 04–08. Metadata, previous/next navigation,
  course maps, schedule links, and internal links use the new numbering.
- `slides/02-inverses-and-invertibility.qmd` is a concise, 28-slide,
  instructor-reviewed deck covering Anton §§1.4–1.6 and an integrated §1.11
  Leontief input–output
  application. It develops inverse matrices, inverse algebra, Gauss–Jordan
  reduction of `[A | I]` to `[I | A^{-1}]`, equivalent signs of invertibility,
  and the distinction between conceptual inverses and direct computational
  solves. The standalone $2\times2$ inverse formula is intentionally omitted;
  determinants remain in Deck 04. The deck now opens by contrasting Deck 01's
  rectangular setting with its square-matrix focus. It derives a nonzero null
  vector for singular $\mat{A}$ from a missing pivot and free variable, then
  shows explicitly why the right-hand side determines no solutions versus
  infinitely many. A high-level Gaussian-process application now interprets
  covariance as joint variation and precision as conditional structure and
  covariance-aware weighting, while reinforcing solves rather than explicit
  inversion.
- Deck 01 now develops elementary matrices through a continuing three-equation
  example and a student exercise that connect an equation operation, the
  corresponding augmented-matrix row operation, and left multiplication by a
  row-operation matrix. The notation distinguishes $E_i$ for equations, $R_i$
  for matrix rows, and $\mat{M}_j$ for row-operation matrices. `Eliminate on
  Matrices` now completes direct augmented-matrix elimination, pivots, back
  substitution, solution-set interpretation, and a resistance-circuit
  application before reinterpreting row operations as matrix actions. It
  identifies direct row operations as the computational method closest to
  software and elementary matrices as an algebraic representation that need
  not be formed for a solve. The section then writes elimination as an ordered
  product and distinguishes associativity (regrouping is allowed) from
  noncommutativity (reordering is not). Deck 01 previews inverses by pairing the
  $3\times3$ matrix $\mat{M}_1$ with an undoing matrix $\mat{N}_1$ satisfying
  $\mat{N}_1\mat{M}_1=\mat{I}$; Deck 02 reuses the same pair, defines an inverse,
  and identifies $\mat{N}_1=\mat{M}_1^{-1}$ before explaining why elementary
  matrices are invertible. Deck 02 explicitly notes the special commuting pair
  $\mat{A}\mat{A}^{-1}=\mat{I}=\mat{A}^{-1}\mat{A}$ and uses associativity to
  derive the reverse-order product rule. It closes by handing off to Deck 03's
  matrix structure and transformation geometry. Course maps in Decks 00–02
  show the full Deck 00–08 sequence.
- The course-wide computational principle is now explicit in Deck 00 and
  `notes/COURSE-PHILOSOPHY.md`: compute only what the problem requires because
  unnecessary work wastes time and creates more opportunities for round-off
  error to accumulate or propagate. For one or a few right-hand sides, use
  Gaussian elimination and back substitution; for many right-hand sides,
  reuse elimination structure or a factorization; compute an explicit inverse
  when the inverse itself is the object of interest.
- Decks 01 and 02 now close their substantive content with gold-bordered `Big
  Ideas` summaries before the next-deck handoff, and their Course Maps link to
  those summaries. `AUTHOR_WORKFLOW.md` records this as the convention for each
  completed instructional deck beginning with Deck 01.
- The Lecture 01 companion notebook has been instructor-reviewed and was
  judged fine for now; no further notebook revisions were requested during
  this task.

## Questions to resolve

- Which Anton §§1.7–1.9 ideas should carry the most classroom weight in Deck
  03 while preserving the established representation-and-action narrative.

## Constraints

- Use Anton Chapter 1 as the course spine and the established MATH 332
  notation.
- Number decks by teaching sequence, show Anton coverage separately, and
  integrate applications with the theory or methodology they motivate.
- Preserve the equations-first, reversibility-first narrative and the smooth
  transition from Deck 01.
- Reserve $E_i$ for equations, $R_i$ for matrix rows, and $\mat{M}_j$ for
  row-operation matrices.
- Do not teach the special $2\times2$ inverse formula before determinants;
  use Gauss–Jordan reduction to compute an inverse.
- Do not present explicit inversion as the routine way to solve linear
  systems. Use Gauss–Jordan reduction because it is useful for finding the
  inverse itself, while retaining Gaussian elimination and back substitution
  for one or a few right-hand sides.
- Keep mathematical exposition authoritative in the RevealJS deck.
- Reuse the established course-wide diagram primitives before adding
  deck-specific styling.

## Done when

- Deck 03 has an instructor-reviewable draft with a smooth Deck 02→03→04
  handoff, accurate Anton coverage, integrated applications where appropriate,
  and visibly sound slides at the standard RevealJS viewport.
