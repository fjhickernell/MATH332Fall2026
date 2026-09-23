# Next task

## Current task

Prepare the September 24 lecture: begin Deck 05 at “Why distinguish points
from vectors?” and develop homogeneous directions and affine solution sets.
September 22 completed the Deck 04 determinants continuation and companion,
with a brief Deck 05 preview. The September 24 Illinois Tech calendar
occurrence has the continuation note for PH 109. The August 18–September 15
recordings were audited, and September 22 was reconciled in the lecture ledger.

Review the shortened 20-slide Deck 05 Euclidean Vector Spaces bridge and the
new 52-slide Deck 06 General Vector Spaces draft with the instructor. Deck 05
now visibly names its homogeneous directions as the null space, while Deck 06
develops the abstract structure using binary vectors, polynomials, and
functions before returning to null, column, and row spaces. Decide what to
refine before scheduling either deck, then turn the four remaining
chapter-sized decks into an explicit plan for the 20 class meetings after
Test 1.

The Deck 04 determinants slides, including the matrices-of-functions
enrichment, have been instructor-reviewed and accepted. The companion still
awaits instructor review. Its Colab badge has been added; rely on the
established setup and address reported Colab problems.

## Other active and deferred work

- Quiz 2 is scheduled for October 1, covering Deck 04 Determinants and
  Deck 05 Euclidean Vector Spaces, during the last 15 minutes of class.
  Course notices are prepared. Canvas On Paper assignment `104699` is saved
  and verified unpublished for Everyone, in Quizzes, with an October 1 at
  12:40 PM deadline matching Quiz 1's class-end time. Confirm the remaining
  Canvas settings before publication; the course notices were deployed in
  the earlier checkpoint.
- All-sections Canvas announcement `106298` posts the remaining quiz dates:
  Quiz 3 on October 15, Quiz 4 on November 12, and Quiz 5 on December 1. The
  same dates are recorded in the Schedule and Quizzes and Tests page; coverage
  for each remains TBD.
- Assignment 2 is published in Canvas (`104698`) and available in WileyPLUS,
  with four instructor-selected questions, five points each, three attempts,
  no deduction, best score, and per-student fixed values. Deadline:
  September 25, 2026, 11:59 PM CDT. Canvas Due and Until remain blank.
  The course website links are live; announcement `105900` is posted to all
  sections. Canvas Student View displays the 20-point assignment and WileyPLUS
  launch. No test answers or scores were submitted. Grade passback is configured
  through the paired LTI assignment; an actual graded submission has not been
  tested. Selection covers inverses, systems and determinants.
- Test 1 grading is complete. Canvas grades were posted September 21 under
  manual posting, and the worked answers with an anonymous score distribution
  were released on the course Quizzes and Tests page and in the test archive.
  All-sections Canvas announcement `106115` is posted.
- Test 2 is scheduled for Thursday, October 29, 2026, in PH 109. Published
  Canvas On Paper assignment `105162` is due at the 12:45 PM class end for
  Everyone in the Tests group; coverage remains TBD. All-sections announcement
  `106297` is posted. The announcement and Quizzes and Tests page state that
  the final-examination date will be posted when scheduled by the Registrar
  and that the cumulative examination will emphasize material not covered by
  Test 1 or Test 2.
- Later projection/rank-factorization material and next-offering Deck 00
  revisions remain deferred in `notes/TODO-LATER.md`.
- The broader tensor scope and placement discussion is deferred until much
  later in `notes/TODO-LATER.md`.

## Current state

- `slides/05-euclidean-vector-spaces.qmd` is now a focused 20-slide bridge
  rather than a broad review of Anton §§3.1–3.5. It distinguishes points from
  vectors and origin-dependent point coordinates, develops homogeneous
  directions and nonhomogeneous affine solution sets, and reuses the earlier
  dot-product geometry only for point differences, projection, and plane
  normals. Cross products remain as a compact three-dimensional connection to
  determinants. It now names the homogeneous direction space
  $\operatorname{Null}(\mat{A})$ and explicitly defers its subspace structure
  and connections with row and column spaces to Deck 06. The Course Map, Big
  Ideas, and closing transition make that handoff explicit. Source rendering
  and the revised closing layout have been visibly checked.
- `slides/06-general-vector-spaces.qmd` is now a substantive 52-slide draft
  covering Anton §§4.1–4.9. Its abstract examples include $\mathbb{F}_2^n$,
  polynomials, and continuous functions; later sections develop subspaces,
  span, independence, bases, coordinates, dimension, change of basis, the
  four matrix spaces, rank–nullity, and rank factorization. One matrix example
  ties the row, column, null, and left-null spaces together. The Course Map
  theme uses the basis-coordinate equation, exercise containers follow the
  established style, and representative dense slides have been visibly
  checked at the standard presentation viewport. Deck 00's cumulative terms
  index now points to the new definitions.
- `notebooks/demonstrations/04-determinants.ipynb` runs end to end with the
  `qmcpy` kernel on Mini (about eight seconds), with saved outputs and inspected
  geometric plots. It covers signed area, exact row operations, PLU and packed
  LU swap parity, determinant identities, eigenvalue products, conditioning,
  and `slogdet`. Deck 04 and the notebook page link to the draft. Its Colab
  badge is added; separate clean-Colab validation is not required by the
  instructor’s current policy.
- Deck 04 now separates the worked PLU example, general determinant formula,
  and permutation-cycle sign into three slides. The deck and companion define
  the row-swap count, explain the product rule, and give the direct cycle
  formula for the sign of a permutation. The revised slides fit in the local
  browser preview; instructor review remains pending.
- Deck 04's Big Ideas now explicitly distinguishes the nonnegative magnitude
  from the sign of the determinant; zero determinant has its own collapse bullet.
- Deck 04 now proves the parallelogram-area formula immediately after its
  signed-area statement, using base times perpendicular height; the proof
  includes the zero-edge case and explains the sign. Rendering, visible layout,
  and the section-outline link are validated.
- Deck 04 now includes a five-slide matrices-of-functions enrichment covering
  a parameter-dependent determinant, the Wronskian of cosine and sine,
  Jacobians as local linear maps, the polar-coordinate area factor, and a
  brief surface-area and tensor outlook. The Wronskian slide describes the
  constant-coefficient relation concretely and calls forward to the formal
  definition of linear independence in Deck 06. The Jacobian slides emphasize
  that the underlying function may be nonlinear, present its first-order
  linear approximation, and give the general $n$-dimensional coordinate-change
  formula for volume elements alongside the polar special case.
- Decks 00--04 are substantive and instructor-reviewed; Deck 04 has also been
  developed and audited. Deck 05 is a complete 20-slide draft, Deck 06 is a
  substantive 52-slide draft, and Decks 07--08 remain placeholders for Anton
  Chapters 5--6. The post-Test-1 schedule has 20 class meetings, but their
  allocation among Decks 05--08, Test 2, exercises, companions, and review has
  not yet been decided.
- Deck 03 includes a starred Householder involution exercise and the
  construction of orthogonal projection onto a plane. It now explicitly
  distinguishes the necessary condition $\mat{A}^2=\mat{I}$ from the
  sufficient Householder certificate
  $\mat{A}=\mat{I}-2\vct{u}\vct{u}^{\mathsf T}$ for a unit normal
  $\vct{u}$, using $-\mat{I}_2$ as a counterexample to sufficiency and the
  reflection across $y=x$ as the positive example. Keep the general
  column-space projector for the later least-squares treatment recorded in
  `notes/TODO-LATER.md`.
- The instructor reports successful end-to-end clean-Colab validation of all
  four published Deck 00--03 companion notebooks using the recorded
  `classlib` commit, without downgrading QMCPy. All four also execute locally
  with the `qmcpy` kernel.
- Deck 03 retains the mathematical PLU derivation and repeated-solve
  conclusion. Its companion notebook retains the detailed SciPy factor,
  solve, packed-storage, pivot, residual, and rectangular-factor sequence.
  The wide and tall examples now print the actual $\mat{A}$, $\mat{P}$,
  $\mat{L}$, and $\mat{U}$ matrices as well as their shapes.
- Deck 03 now states that a first dense solve costs $O(n^3)$ operations and
  each new right-hand side costs $O(n^2)$ when saved PLU factors are reused.
  The companion notebook measures both paths for
  $n=64,128,256,512,1024,2048,4096,8192,16384$ and displays a timing table
  and log--log plot. On the M3 clean-kernel validation run, the $n=16384$
  fresh solve took 5.996 seconds versus 0.203 seconds with saved PLU, a
  29.5-fold speedup. The full notebook executes without errors, and Deck 03
  renders cleanly outside the filesystem sandbox.
- Assignment 1 is the individual 20-point WileyPLUS assignment, due September
  7 at 11:59 PM Chicago Time. Quiz 1 is scheduled for September 10 and covers
  Decks 01--02. Test 1 is scheduled for September 17 and covers Decks 01--03.
- Test 1 grading is complete. Canvas grades were posted September 21, 2026,
  and the public answer-version PDF includes the anonymous score distribution.
  All-sections Canvas announcement `106115` is posted. The student copy and
  private source remain outside this public repository.

## Questions to resolve

- Revisit how to recognize projection and orthogonal-projection matrices,
  and whether to introduce null spaces earlier to motivate vector spaces,
  bases, and coordinates. The placement questions and proposed criteria are
  recorded in `notes/TODO-LATER.md`; no deck changes are yet decided.

- When next reviewing the MATH 332 lectures, revisit the Deck 05--06
  motivation for bases and coordinates through infinite solution sets. Use
  the precise affine-subspace formulation recorded in `notes/TODO-LATER.md`:
  Deck 05 poses the geometric need, and Deck 06 explains that a basis of the
  null space supplies adapted directions while its coefficients locate a
  solution relative to a particular solution.
- How should the 20 class meetings after Test 1 be allocated among Decks
  05--08, Test 2, exercises, companion notebooks, synthesis, and review? In
  particular, should the large Chapter 5 and 6 units remain Decks 07 and 08 or
  be divided into smaller teaching decks?
- Should Deck 03 briefly signpost Strang's later
  $\mat{A}=\mat{C}\mat{R}$ rank factorization, or should that remain deferred
  until vector spaces, bases, row and column spaces, RREF pivot columns, and
  rank have been established?

## Constraints

- Keep mathematical exposition authoritative in the RevealJS decks and use
  companion notebooks for executable detail and experimentation.
- Preserve SciPy's convention
  $\mat{A}=\mat{P}\mat{L}\mat{U}$, equivalently
  $\mat{P}^{\mathsf T}\mat{A}=\mat{L}\mat{U}$.
- Keep SciPy APIs, packed factors, pivot indices, executable solves, residual
  checks, and timing experiments in the companion notebook rather than
  restoring them to the live deck.
- Do not pin or downgrade to QMCPy 1.6.1; support the current QMCPy interface.
- Use Anton as the course spine and preserve the established MATH 332
  notation, deck sequence, application integration, and shared `classlib`
  conventions.

## Done when

- The instructor has reviewed the determinants companion; local validation
  and the companion's Colab badge are complete. Address Colab problems if
  reported.
- The instructor has reviewed Decks 05 and 06 and identified any revisions
  needed before they are scheduled.
- The remaining-semester arc makes the instructional scope hidden inside
  Decks 05--08 visible and assigns the available meetings without rushing the
  denser later material.
