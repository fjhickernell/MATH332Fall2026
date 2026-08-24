# Next task

## Current task

Review the Deck 03 draft with the instructor and make any requested
refinements.

## Current state

- Assignment 1 is defined as Anton Exercises 1.3.15, 1.2.38, and 1.3.2,
  due Friday, September 4, 2026, at 11:59 PM Chicago Time. Its course-hosted
  detail page, assignments-table entry, schedule entry, and Deck 03 title-slide
  notice are published and render cleanly. Canvas Assignment 1 is published for
  20 points with unlimited file-upload attempts and its own 20-group
  self-sign-up set, `Assignment 1 Groups`, limited to pairs; one submission and
  grade are shared by each group. The course-hosted detail page is the
  authoritative source. The Canvas description links to the live assignment
  and course Assignments pages without repeating the exercise details, and the
  Canvas announcement has been posted.
- The sequential Deck 00–08 architecture is implemented. Decks 01–03 now have
  substantive drafts, and Anton Chapters 2–6 are represented by Decks 04–08.
  Metadata, previous/next navigation, course maps, schedule links, and internal
  links use the sequential numbering.
- `slides/02-inverses-and-invertibility.qmd` is a concise, 29-slide,
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
  inversion. It now previews triangular factorization without proof: inverse
  grouped column-elimination matrices yield a unit lower-triangular factor
  when elimination proceeds without row exchanges. Deck 03 first develops
  that plain LU example and only then accounts for row order with a
  permutation matrix.
- `slides/03-matrix-structure-and-transformations.qmd` is a 32-slide
  instructor-review draft covering Anton §§1.7–1.9. It develops diagonal,
  triangular, transposed, and symmetric structure; supplements Anton with PLU,
  including SciPy's compact factor shapes for rectangular matrices;
  defines linear transformations and standard matrices; treats scaling,
  reflections, projections, and rotations, including a coordinate-plane
  comparison of three actions; and closes with composition, inverse actions,
  and a determinant handoff. It uses SciPy's convention
  $\mat{A}=\mat{P}\mat{L}\mat{U}$, equivalently
  $\mat{P}^{\mathsf T}\mat{A}=\mat{L}\mat{U}$. The Markdown parses cleanly,
  the displayed examples have been checked computationally, and internal
  fragment targets have been checked. The root site and all nine decks render
  cleanly outside the filesystem sandbox; Deck 03 has been inspected slide by
  slide at the standard $1600\times1000$ RevealJS viewport, and the assembled
  site's student-facing local files and fragments resolve.
- Deck 01 now develops grouped elimination matrices through a continuing
  three-equation example that connects equation operations, the corresponding
  augmented-matrix row operations, and left multiplication. The notation
  distinguishes $E_i$ for equations, $R_i$ for matrix rows, and $\mat{M}_j$
  for the matrix that zeros column $j$ below row $j$. Each $\mat{M}_j$ is a
  product of elementary matrices. `Eliminate on
  Matrices` now completes direct augmented-matrix elimination, pivots, back
  substitution, solution-set interpretation, and a resistance-circuit
  application before reinterpreting row operations as matrix actions. It
  identifies direct row operations as the computational method closest to
  software and elimination matrices as an algebraic representation that need
  not be formed for a solve. The section uses
  $q=\min(m-1,n)$ stages for an $m\times n$ matrix, explicitly noting that a
  tall matrix may require $\mat{M}_n$, then distinguishes associativity
  (regrouping is allowed) from noncommutativity (reordering is not). Deck 01
  previews inverses by pairing the $3\times3$ matrix $\mat{M}_1$, which clears
  the entire first column below its pivot, with an undoing matrix $\mat{N}_1$
  satisfying $\mat{N}_1\mat{M}_1=\mat{I}$; Deck 02 reuses the same pair, defines
  an inverse, and identifies $\mat{N}_1=\mat{M}_1^{-1}$ before explaining why
  grouped elimination matrices are invertible. Deck 02 explicitly notes the
  special commuting pair
  $\mat{A}\mat{A}^{-1}=\mat{I}=\mat{A}^{-1}\mat{A}$ and uses associativity to
  derive the reverse-order product rule. It closes by handing off to Deck 03's
  matrix structure and transformation geometry. Deck 01's dot-product section
  now identifies the standard dot product on $\reals^n$ as the course's first
  inner product and derives its cosine formula from the planar Law of Cosines,
  supported by a labeled triangle in the plane containing
  $\vct{0},\vct{a},\vct{x}$. Course maps in Decks 00–02 show the full Deck
  00–08 sequence.
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

- **Temporary cross-machine reconciliation note:** On the next machine, check
  whether an earlier Assignment 1 source or Canvas assignment already exists
  there. Reconcile it with the Assignment 1 created on M3, then remove this
  note.
- Does the Deck 03 draft place the right classroom weight on special matrix
  structure, PLU, geometric transformations, and composition?
- Should Deck 03's PLU treatment include a brief forward signpost to Strang's
  later $\mat{A}=\mat{C}\mat{R}$ rank factorization? Keep any mention
  prospective rather than developing it here: the full treatment belongs
  after vector spaces, subspaces, basis, column and row spaces, RREF pivot
  columns, and rank have been established.
- Which slides need additional examples, exercises, visual explanation, or
  trimming after instructor review?

## Constraints

- Use Anton Chapter 1 as the course spine and the established MATH 332
  notation.
- Number decks by teaching sequence, show Anton coverage separately, and
  integrate applications with the theory or methodology they motivate.
- Preserve the equations-first, reversibility-first narrative and the smooth
  transition from Deck 01.
- Reserve $E_i$ for equations, $R_i$ for matrix rows, and $\mat{M}_j$ for the
  grouped elimination matrix that zeros column $j$ below row $j$.
- Use one aggregate $\mat{G}$ for the complete Gauss–Jordan row-operation
  product. Use $\mat{P}_{jk}$ only when a particular row exchange must be
  named, and $\mat{P}$ for the accumulated permutation in PLU.
- Do not teach the special $2\times2$ inverse formula before determinants;
  use Gauss–Jordan reduction to compute an inverse.
- Do not present explicit inversion as the routine way to solve linear
  systems. Use Gauss–Jordan reduction because it is useful for finding the
  inverse itself, while retaining Gaussian elimination and back substitution
  for one or a few right-hand sides.
- Use SciPy's PLU convention
  $\mat{A}=\mat{P}\mat{L}\mat{U}$ and explain that
  $\mat{P}^{\mathsf T}$ applies the row ordering used for elimination.
- Treat PLU as a concise structural bridge, not as a numerical-methods unit;
  omit pivot-selection algorithms, stability analysis, operation counts, and
  storage details.
- Keep mathematical exposition authoritative in the RevealJS deck.
- Reuse the established course-wide diagram primitives before adding
  deck-specific styling.

## Done when

- Assignment 1 is finalized, linked from the assignments page, configured in
  Canvas, and assigned by Monday, August 24.
- The instructor has reviewed Deck 03's scope, sequence, examples, and
  mathematical emphasis, and requested refinements are complete.
- Any requested refinements render cleanly and remain visibly sound at the
  standard RevealJS viewport, with working section, glossary, and
  previous/next links.
