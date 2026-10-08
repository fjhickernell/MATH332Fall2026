# Next task

## Current task

Review the new opening motivation in Bases and Coordinates: linear
combinations build vectors, span describes reach, independence gives unique
coefficients, and an ordered basis turns them into coordinates. Seven content
slides use a square-to-parallelogram map, redundancy practice, polynomial
differentiation through a coordinate matrix, regression with a three-response
example, and centered PCA with a one-direction approximation. Vector Spaces
and Span links directly to this bridge. The examples link forward to Matrix
Spaces and Rank, Inner Products, and Special Topics. Local mathematical,
rendered-layout, and link checks pass; instructor review remains. The October 8
checkpoint `f03285f` publishes this bridge and its notation/exercise touch-ups.
The isolated full website and twelve-deck renders pass without warnings; the
assembled site passes 1,703 local references and 695 anchors. The schedule
and assessment tables pass text-boundary and visible checks at desktop and
phone widths. Both publishing and Pages deployment succeeded; the live
coverage pages and Decks 05–07 were verified. All-sections Canvas coverage announcement
[107573](https://iit.instructure.com/courses/23913/discussion_topics/107573)
is published and verified (October 8, 8:35 AM CDT).
Notation touch-ups use square brackets for numerical vector columns and
explicit columns in the zero-test set definitions. The extra-generator
practice now states its representation equation and allows zero coefficients;
its answer notes explain why redundancy makes coefficients nonunique.

Inner Product Spaces (`slides/10-inner-product-spaces.qmd`, 46 slides) now
has an instructor-review draft covering inner products, projections,
Gram–Schmidt/QR, regression, and function/Fourier approximation. Review this
foundation before Special Topics (`slides/11-special-topics.qmd`, 55 slides).
The capstone prioritizes SVD and regression, with quadratic forms, FFT,
tensor products, power iteration/PageRank, and graph Laplacians as modular
choices. Its class-preferences slide asks students to rank optional coverage;
select topics and pacing after review. Companion demonstrations remain to be
built. The imminent October 8 preparation and Chapter 4 review below remain.

Both new decks and the twelve-deck navigation pass local rendering,
MathJax/layout inspection, and link/anchor checks. Worked QR, regression,
DFT, pseudoinverse, and Kronecker examples were checked numerically. The
unchanged shared biography snippet retains its standalone image-path issue;
the course homepage image resolves.

The cumulative How Far recaps in Decks 02–08 and 10–11 have been audited
and revised for fuller explanations and balanced one-page layouts at ordinary
type size. Inverses now recalls both the system augmentation [A|b] and the
Gauss–Jordan computation [A|I] to [I|A^-1]; its Big Ideas label is "Inverse
of a product." Inverses and Matrix Transformations use "inconsistencies
(contradictions)." Later recaps carry the solution, geometry, basis, rank,
projection, and least-squares connections forward with formula conditions.
All twelve decks render; the nine recaps pass MathJax/layout review and the
assembled site passes local-link/anchor checks. Instructor review remains.
Deck 09 is still the only placeholder; the review order above is unchanged.

Pivot reminders now point to the original Systems and Matrices definition,
`#pivots-organize-elimination`, at the first mention in every deck that uses
the term and in relevant closing summaries. The definition explicitly covers
any m-by-n matrix, including augmented matrices; pivots need not be unit
entries or diagonal entries. Zero entries considered during elimination are
called pivot candidates, and the triangular example's invertibility test
requires a pivot in every column. This course convention is recorded in
AUTHOR_WORKFLOW.md. The seven new first-use links were clicked and verified;
the definition and corrected examples pass visual/MathJax review, and the
website and all twelve decks render with valid local links and anchors.
Instructor review and topic selection remain.

The General Vector Spaces material is now three instructor-review decks:
Vector Spaces, Subspaces, and Span (`06-general-vector-spaces.qmd`, Anton
§§4.1–4.3); Bases, Dimension, and Coordinates
(`07-bases-dimension-and-coordinates.qmd`, §§4.4–4.7, with basis extraction
from §4.8); and Matrix Spaces and Rank (`08-matrix-spaces-and-rank.qmd`,
§§4.8–4.9, with a closing preview of §§8.1 and 8.4). Their instructional
sections number four, seven, and five; their slide counts are 47, 55, and 35,
including titles and closing slides.

The deck sequence is consecutive from 00 through 11: the Chapter 4 decks
are 06–08, Eigenvalues is 09, Inner Products is 10, and Special Topics is 11.
Continue at 12 for future decks. Three draft companions now exist under
`notebooks/demonstrations/`, using the same basenames as Decks 06–08.
Each runs in a fresh `qmcpy` kernel with exact checks and saved output;
instructor review remains. They are linked from their decks and the Notebooks
page. The website and all eleven decks render; the assembled site passes
562 local-link checks and 183 cross-page anchor checks. New notebook callouts,
course maps/navigation, and the Notebooks page at desktop and phone widths
passed browser inspection. The October 4 Checkpoint includes these changes;
its build/publication and Pages deployment succeeded; live companion
content has not been rechecked. Matrix-space operators are lowercase `col`, `row`, and
`null`; the rank deck and notebook explicitly explain the transpose identities.

The October 3 audit checked the exact 12th Applications edition, repaired
missing definitions and assumptions, moved elimination and redundancy removal
into the bases section, made the example's row operation explicit, and added
big-picture connections and exercises. All 85 original explicit anchors
survive; there are now 99 anchors and 28 starred exercise blocks with answer
notes. Every instructional section has at least two main topics. The tilted
plane, polynomial-coordinate diagram, and four-space diagram are in place.
All 126 slides passed rendered visual review; final layout refinements,
all eleven deck renders, the assembled-site links/navigation, cumulative
terms entries, and the welcome page at desktop and phone widths were checked.
See `notes/CHAPTER4-AUDIT.md` for the crosswalk and verification record.
The October 3 Checkpoint publishes these audit revisions. The responsive
footer fix was published first in canonical HickernellAcademicLib at
`98e0701`; this course intentionally adopts that exact commit. Other
consumers retain their existing pins.

The instructor's follow-up review added local reminders of definitions,
chosen vectors, matrices, and coordinate conventions across all three decks.
Matrix Spaces and Rank now contrasts echelon form for bases with RREF for
the direct rank-factorization coefficients. Systems and Matrices supplies an
explicit rectangular RREF definition and distinguishes it from the
Gauss–Jordan process. A returning-reader pass replaced fourteen vague
lead-ins with compact cues about coefficients, membership, coordinate roles,
and factor/basis dimensions; no slides or recap blocks were added. All eleven
decks and the website rerender successfully; the changed layouts and local
links pass. These follow-ups were published in `3233d9b`; its build and Pages
deployment succeeded.

The latest follow-up enriches the cumulative summaries in Euclidean
Spaces and the three split decks. It carries systems and all solutions,
geometry, reusable factors, abstract spans, and basis/coordinate connections
forward. Two new continuation slides prove the A=C R extraction recipe;
C's columns and R's rows are explicitly identified as the corresponding
bases. The numerical check explains that R x gives the coordinates of A x
in C's ordered column-space basis. The rank closing states both compatibility
tests and x=x_p+N t with n-r free parameters. All four affected decks render;
the nine changed/new slides pass visible layout review and the assembled-site
links/anchors pass. Details and current counts are in CHAPTER4-AUDIT.md.

Rank-factorization notation now reserves R for the nonzero-row factor in
A=C R, writes the full reduced matrix as rref(A), and keeps U for PLU.
Teal boxes mark the running example's pivot columns in the RREF definition
and rank deck; matching boxes in R expose I_2 after removing the zero row.
The notation and boxes were published in `1c78f80`; its build and Pages
deployment succeeded.

Continue instructor-led content review of the three decks and their companion
notebooks. Keep exercise answers in presenter notes. Fourier modes
use $e^{2\pi\sqrt{-1}\,kt}$ on $[0,1]$. The infinite-basis example uses
$C(\reals)$ with an uncountable algebraic (Hamel) basis; distinguish finite
algebraic representations from convergent Hilbert-space expansions.
Named deck references follow `classlib/docs/slide-style.md`, intentionally
adopted in this course at HickernellAcademicLib commit `5becc32`.

The lecture ledger and schedule are reconciled through October 6. Prepare
October 8 to resume Deck 06 at “Spanning polynomials means matching every
coefficient.” October 6 completed subspace tests, span as linear combinations,
plane-span membership, and redundant generators. The October 8 Illinois Tech
Fred → Calendar occurrence was saved using “Only This Event” and reopened to
verify its continuation note, PH 109, and 11:15 AM–12:45 PM hours. Fantastical
independently confirms the saved note and Chicago times. These schedule and
handoff changes are included in the October 7 checkpoint; remote deployment
is pending.

Quiz 2 website coverage is updated to Determinants and Euclidean Vector
Spaces through projections (excluding cross products), as confirmed by the
instructor on September 24. All-sections Canvas announcement `106481`,
“Quiz 2 on October 1: coverage through projections,” is posted and verified.
The updated coverage passed the full local website and slide renders.

The private Quiz 2 draft is complete and was sent to CDR on September 30.
The Canvas On Paper assignment is published and verified; grades will be
entered after grading.

Deck 05 instructor-led content and layout review is complete, as confirmed
October 4. Its locally executed companion notebook still awaits instructor
review. Decks 06–08 and their locally validated draft companions also await
instructor review. Then plan the Eigenvalues and Inner Products units and
allocate the 20 post-Test-1 meetings among instruction, exercises, companions,
Test 2, and review. The Chapter 4 slide audit and companion construction are
complete; instructor approval remains.

The Deck 04 determinants slides were previously instructor-reviewed. The
surface outlook was revised after the instructor flagged the premature cross
product and unclear meaning of $\vct{G}(u,v)$; the new explanation and local
area formula await visible review. The companion still awaits instructor
review. Its Colab badge has been added; rely on the established setup and
address reported Colab problems.

## Other active and deferred work

- Assignment 3 is published in Canvas (`105825`) and available in WileyPLUS:
  five questions, 20 points, due October 9 at 11:59 PM CDT. Course links are
  live; all-sections announcement `106960` is posted and verified. Canvas
  Student View shows the assignment and WileyPLUS launch button. No test
  scores were submitted. Full verification and closeout are recorded in
  `notes/ASSIGNMENT-3-PUBLICATION.md`.
- Quiz 2 is scheduled for October 1, covering Deck 04 Determinants and
  Deck 05 Euclidean Vector Spaces through projections (excluding cross products),
  during the last 15 minutes of class.
  Canvas On Paper assignment `104699` is published and verified for Everyone,
  in Quizzes, with an October 1 at 12:40 PM deadline. Quizzes 3–5 are also
  published for their announced October 15, November 12, and December 1 dates;
  Quiz 3 covers Euclidean Vector Spaces and Vector Spaces, Subspaces, and Span.
  Quiz 4 and Quiz 5 coverage remains TBD. Both tests are published. Grades
  remain for later entry.
- All-sections Canvas announcement `106298` posts the remaining quiz dates:
  Quiz 3 on October 15, Quiz 4 on November 12, and Quiz 5 on December 1. The
  same dates are recorded in the Schedule and Quizzes and Tests page. Quiz 3
  coverage is finalized as the full Euclidean Vector Spaces and Vector
  Spaces, Subspaces, and Span decks. The October 8 coverage announcement
  [107573](https://iit.instructure.com/courses/23913/discussion_topics/107573),
  “Quiz 3: Coverage for Thursday, October 15,” is published and verified for
  All Sections. Quiz 4 and Quiz 5 coverage remains TBD. Quiz 3 grading is due
  October 21, six calendar days after October 15. Mixed lecture/quiz schedule rows now separate the
  quiz and its coverage with a light divider and blank-line spacing. All
  monthly tables, including the final examination, use consistent columns.
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
- Tensor products are drafted in Deck 11; review their scope alongside the
  other optional topics and develop a companion demonstration.

## Current state

- `slides/05-euclidean-vector-spaces.qmd` is now a 33-slide bridge (including its title slide)
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
- Deck 05 now explicitly connects linear combinations, affine solution sets,
  and their dimension. Projection and cross products have worked examples and
  starred exercises with speaker-note answers. The projection figure uses
  $t_*=2$, serif vector/point notation, and thick arrows; the cross-product
  sequence includes the determinant mnemonic and a component-to-area proof.
  Euclidean Tools retains five main topics, with six supporting continuation
  slides. Decks 01–06 now link callbacks, previews, and cumulative reviews to
  their targets. Diagram implementation is documented in
  `notes/TECHNICAL-NOTES.md`, with author-workflow links and continuation rules.
- The former General Vector Spaces draft is split into three audited decks:
  Vector Spaces and Span (47 slides), Bases and Coordinates (55), and Matrix
  Spaces and Rank (35). Precise Anton ranges appear in their metadata,
  subtitles, website outline, and PLAN. Section outlines, previous/next links,
  course maps, schedule references, and the cumulative terms index agree.
  Redundancy removal precedes coordinates; dimension is defined before use;
  rank, nullity, and orthogonal complement have explicit definitions. The
  abstract linear-transformation closing section is labeled as a Chapter 8
  preview. Instructor review of Decks 06–08 and their completed draft
  companions remains open.
- `notebooks/demonstrations/04-determinants.ipynb` runs end to end with the
  `qmcpy` kernel on Mini (about eight seconds), with saved outputs and inspected
  geometric plots. It covers signed area, exact row operations, PLU and packed
  LU swap parity, determinant identities, eigenvalue products, conditioning,
  and `slogdet`. Deck 04 and the notebook page link to the draft. Its Colab
  badge is added; separate clean-Colab validation is not required by the
  instructor’s current policy.
- `notebooks/demonstrations/05-euclidean-vector-spaces.ipynb` now runs end to
  end with the `qmcpy` kernel and has saved outputs. It explores point
  coordinates, homogeneous directions, affine solution sets, nearest-point
  projection, and cross products and determinants of displacements. Deck 05
  and the Notebooks page link to this instructor-review draft.
- Deck 04 now separates the worked PLU example, general determinant formula,
  and permutation-cycle sign into three slides. The deck and companion define
  the row-swap count, explain the product rule, and give the direct cycle
  formula for the sign of a permutation. The revised slides fit in the local
  browser preview; instructor review remains pending.
- Deck 04's Big Ideas now explicitly distinguishes the nonnegative magnitude
  from the sign of the determinant; zero determinant has its own collapse bullet.
- Developed Decks 02–08 now close with Big Ideas, a cumulative "How Far We
  Have Come" slide, and What Comes Next. Each Course Map links once to Big
  Ideas for the closing sequence. Deck 09 remains a placeholder and should
  gain this sequence when developed; the new Decks 10–11 drafts include it.
- Deck 04 now proves the parallelogram-area formula immediately after its
  signed-area statement, using base times perpendicular height; the proof
  includes the zero-edge case and explains the sign. Rendering, visible layout,
  and the section-outline link are validated.
- Deck 04 now includes an eight-slide matrices-of-functions enrichment covering
  a parameter-dependent determinant, the Wronskian of cosine and sine,
  Jacobians as local linear maps, the polar-coordinate area factor, the
  spherical-coordinate volume factor and its determinant by row operations,
  and a brief surface-area and tensor outlook. The Wronskian slide describes the
  constant-coefficient relation concretely and calls forward to the formal
  definition of linear independence in Deck 06. The Jacobian slides emphasize
  that the underlying function may be nonlinear, present its first-order
  linear approximation, and give the general $n$-dimensional coordinate-change
  formula for volume elements alongside the polar special case.
- The surface outlook now explicitly defines $\vct{G}:D\subseteq\reals^2\to
  \reals^3$, explains that $(u,v)$ are optional input labels distinct from
  output $(x,y,z)$, and uses a graph example. It gives local area through
  $\det(\mat{J}_{\vct{G}}^{\mathsf T}\mat{J}_{\vct{G}})$ without assuming
  prior knowledge of cross products. All slides rendered in the instructor's
  `quarto-slides-live all` run. A shared MathJax loader fix allows slides to
  display before the remote script loads; Deck 05 projection screenshots now
  confirm visible equation typesetting and corrected layout. The instructor
  confirmed Deck 04 and the Deck 05 title slide visually on September 28;
  Deck 05 content and layout review was completed October 4.
- Decks 00--04 are substantive and instructor-reviewed; Deck 04 has also been
  developed and audited. Deck 05 is an expanded 33-slide draft (including its
  title), the three Chapter 4 decks are audited drafts, and Deck 09 remains
  a placeholder for Anton Chapter 5. Decks 10–11 have instructor-review drafts.
  The post-Test-1 schedule has 20 class meetings, but their allocation among
  Decks 05–11, Test 2, exercises, companions, and review has
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

- When next reviewing the MATH 332 lectures, revisit Decks 05–08
  motivation for bases and coordinates through infinite solution sets. Use
  the precise affine-subspace formulation recorded in `notes/TODO-LATER.md`:
  Deck 05 poses the geometric need, and Decks 07–08 explain that a basis of the
  null space supplies adapted directions while its coefficients locate a
  solution relative to a particular solution.
- How should the 20 class meetings after Test 1 be allocated among Decks
  05--11, Test 2, exercises, companion notebooks, synthesis, and review? In
  particular, should the large Chapter 5 and 6 units remain Decks 09 and 10 or
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
- The instructor has reviewed Decks 06–08 and 10–11 and the pending companion
  notebooks, selected Special Topics modules, and identified any revisions
  needed before they are scheduled. Deck 05 slide review is already complete.
- The remaining-semester arc makes the instructional scope hidden inside
  Decks 05--11 visible and assigns the available meetings without rushing the
  denser later material.
