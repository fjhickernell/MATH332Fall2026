# Next task

## Reconcile the October 27 lecture

The October 27 Panopto readiness notice in Illinois Tech Fred identifies an
11:24 AM recording start and approximately 78 minutes. Recording inspection
is pending: Safari reached the Illinois Tech sign-in page after starting at
the portal. Resume `Lecture update 332` after sign-in, verify the actual
stopping point, and reconcile the schedule, ledger, and next instructional
calendar occurrence on November 3. October 29 is Test 2 and must not receive
the continuation note. The ledger remains reconciled through October 22;
no October 27 coverage or calendar change has been inferred.

The preparation notes below describe the earlier plan, not verified
October 27 coverage.

## October 27 coordinate review — ready for teaching

Resume at “Build a basis by adding or removing vectors” (slide 34 of the
current 90-slide Deck 07), then its independence proof, scalar-field example,
and “Coordinates and Their Arithmetic.” Revisit the relocated monomial/dimension
practice if needed. The October 22 recording and October 27 calendar note
still determine this pickup; editorial changes do not
establish new lecture coverage.

The coordinate sequence now moves from the standard basis and same-vector
example to arithmetic. It pairs expanded sums with basis-row products, uses
full coordinate columns where they fit, highlights [x]_E=x in R^n, and builds
transition columns through a concrete polynomial example before the general
rule. The PCA calculation displays the full numerical product XQ=S with
aligned input and score rows. All prior examples, 20 Deck 07 exercise sets,
and named anchors remain; Decks 06 and 07 have 51 and 90 slides.

These revisions and the notation conventions in AUTHOR_WORKFLOW.md are
included in this Checkpoint. Local validation is recorded in
`notes/CHAPTER4-AUDIT.md`; remote deployment and live verification remain
pending. Test 2 coverage still ends at dimension, excluding coordinates and
transformations. Its remaining private preparation and course actions are
listed below.

## October 27 lecture continuation

October 22 is reconciled from the now-available captions and closing slides.
The damped spring was completed in both output bases, followed by review of
independence, bases and dimension through the equivalence of independence
and spanning tests for exactly dim(V) vectors. Resume Deck 07 at “Build a
basis by adding or removing vectors,” remaining dimension examples, then
“Coordinates and Their Arithmetic.” The October 27 occurrence is saved and
reopened in Fantastical on Illinois Tech Fred → Calendar, PH 109,
11:15 AM–12:45 PM Chicago. Schedule and ledger edits are included in this
checkpoint; remote deployment and live-page verification remain pending.

For October 27, the instructor aims to finish Bases and Coordinates. The
October 26 local revisions clarify arbitrary vectors and numerical
representations across Decks 06 and 07. That revision left Deck 06 with 51 slides and Deck 07
with 88, with conceptual section outlines, preserved examples/exercises,
highlighted uniqueness, and a separate length-preservation topic. The
monomial dimension example and practice now follow the dimension definition,
before the equivalent basis tests; revisit that relocated practice as needed.
Review these revisions before teaching. The abstract-vector and coordinate-map
changes are published in `6cebaa2`; the regression/PCA clarification below is
included in this Checkpoint, with deployment/live verification pending. The
notation convention is recorded in AUTHOR_WORKFLOW.md.

Deck 06 also has paired gold-star proof exercises after the zero-vector test:
removing one vector from a real vector space cannot leave a subspace, while an
example over F2 can. Worked proofs are in presenter notes. Full website and
twelve-deck renders, the new slide and outline layouts, and local links pass.
These additions are included in this Checkpoint; remote deployment remains
pending. Lecture preparation is complete per the Dashboard; the next action
is to teach the recorded October 27 continuation.

Regression/PCA clarification: a visible comparison distinguishes using
explanatory data X and response y to fit y from representing X without using
a response. Regression now consistently uses X, y, and beta. PCA shows the
actual eight centered observations as an 8-by-2 matrix, the 2-by-2 orthonormal
basis, and all eight rows of scores XQ before the preserved geometric picture.
Three supporting slides make these objects and the variance comparison visible
without deriving the PCA algorithm. X now contains whole-number observations
without a common scale factor; scores, variances, and figure labels are scaled
consistently. Original coordinate variances are 482/7 each; PCA variances are
128 and 68/7, concentrating 92.9% of total variance in the first score versus
50% in either original coordinate. A table and generated bar comparison show
this change while total variance stays fixed. Original feature-space axes are
e_1,e_2; data columns X_1,X_2 collect the eight coordinate values. Exact
arithmetic and matching against the plotted points pass. The complete website
and all twelve decks render; 1,755 local links/assets and changed layouts pass
checks, including browser review. These latest edits are included in this
Checkpoint; deployment/live verification remains pending.

Checkpoint validation also corrects the shared navigation reset: explicit
cross-section links and hash addresses retain the requested child slide,
while horizontal arrows still open the section overview. This course
intentionally pins HickernellAcademicLib `5484f82`; other dependencies remain
unchanged. At that Checkpoint, the complete website and all twelve decks
rendered without warnings; 1,756 local links/assets, exercise preservation,
exact new calculations, and browser navigation checks passed. Instructor
review remains distinct from these local checks.

### Test 2 — private preparation complete

The private draft is complete and reviewed; final printing remains for the
October 29 test in PH 109. Grading is due November 4. Keep unreleased
assessment material private.

### Test 2 coverage correction — Canvas published, website pending

The instructor confirmed on October 22 that Test 2 ends at dimension.
Coordinates, coordinate arithmetic, change of basis and transformations are
excluded, as are the later applications and Matrix Spaces and Rank. Canvas
assignment `105162` and the prior coverage announcement `107870` are corrected.
The new [all-sections correction announcement](https://iit.instructure.com/courses/23913/discussion_topics/108764)
is published and verified. The website Schedule and Quizzes and Tests source
rows have the same cutoff and exclusions and are included in this checkpoint;
remote deployment and live-page verification remain pending. The complete website and all twelve decks render; the
corrected assessment and schedule rows pass desktop and 390-pixel Safari
layout checks, and `git diff --check` passes. Test date/location and grading
deadline are unchanged:
October 29, PH 109; grading due November 4.

## Decks 07–09 revision and development

Deck 07 now explains abstract basis-column reconstruction and labels the later
matrix/polynomial basis examples as review. Deck 08 replaces its repeated
transformation definition with kernel/image coordinates and rank–nullity,
including the differentiation example's constant kernel and full P1 image.

Deck 09 is now a substantive Chapter 5 draft: preserved directions,
characteristic polynomials/eigenspaces, diagonalization and multiplicities,
complex pairs, powers and population exchange, and real symmetric spectral
theory. It includes seven starred exercise sets with presenter-note answers,
a geometric eigenvector figure, section outlines and the cumulative closing
sequence. The intro terminology links now point to its developed treatments;
the welcome-page description lists the draft coverage without assigning hours.

Complete instructor review of the new deck and remaining Deck 07/08 layouts
before teaching. No lecture dates, assessment coverage, or notebook assignments
were changed. These revisions are included in the October 24 teaching
Checkpoint; remote deployment and instructor review remain pending.

Validation: exact symbolic checks pass for the numerical examples and exercise
answers; the root website and all twelve decks render. All 41 Deck 09 slides
and the five edited Deck 07/08 slides were inspected in the browser, with the
figure and matrix-basis takeaway clearance corrected. The welcome page and
twelve decks pass 985 local-link/asset checks; source style and
`git diff --check` pass. Instructor content review remains distinct from this
local validation.

## Deck 07 structure review

The opening concept table is instructor-approved: linear combinations and
independence show both expanded sums and matrix products. Its 18/48/34 column
proportions and compact row spacing pass rendered browser review, with the key
point clear of the footer. Continue reviewing the remaining layouts.

Review the revised 88-slide flow and visible layouts before teaching. The
October 21 revision organizes the deck by motivating questions, puts visible
matrix proofs before their applications, moves dimension before the coordinate
examples, and places enrichment after the foundations. All examples and the
19 original exercise sets remain; the opening basis question makes 20 sets.
The basis-matrix sequence includes the standard-basis identity, labeled
conversion arrows, a derivation of transition columns, and a two-slide worked
polynomial conversion with reconstruction.

Exact checks of 14 mathematical groups, the full website and twelve-deck
renders, source/style, exercise preservation, outlines, and local/incoming
anchor checks pass. Browser visual review remains pending because access to
local-file URLs was blocked. The instructor authorized publication with
Checkpoint; remote deployment of this revision remains pending. The recorded
October 22 lecture continuation above is unchanged. See
`notes/CHAPTER4-AUDIT.md` for the rationale and validation scope. Older
construction details below are historical context when their ordering differs
from this revision.

## Current task

The October 19 Safari math-loading fix is validated and published in
HickernellAcademicLib `8b84f9a`, intentionally pinned here. MathJax 3.2.2 is
bundled instead of downloaded from the CDN; the local metadata inherits the
shared setting. Twelve decks render, and Safari reload and slide/section
navigation pass, confirmed by the instructor. Other computers obtain the
runtime through normal recursive repository synchronization.

The oscillator continuation now displays both coordinate-change directions,
with the forward matrix boxed in blue and a numerical round trip. Selective
emphasis reinforces basis order, uniqueness, matrix columns, and arrow
direction throughout Deck 07. The intro index has been audited against all
twelve decks: 191 alphabetized terms across ten pages, linked to substantive
treatments. Matrix representation now links to Deck 07 and SVD to Deck 11.
Exact oscillator checks, full rendering, local links, and visible layout
checks pass; see `notes/TERMINOLOGY-AUDIT.md`. The October 20 revisions are
validated for publication; live deployment has not yet been verified.

The October 20 continuation in Deck 07 is prepared. Recap independence and
coordinate uniqueness, then resume “Coordinates in a Chosen Basis” →
“A basis gives every vector unique coordinates.” October 15 covered the
line-coordinate example, Fourier-mode independence, homogeneous coefficient
tests, and basis extraction by elimination. Frames and infinite bases were
brief previews before Quiz 3. Systematic coordinate calculations and the
previously deferred differentiation-by-coordinates, regression, and PCA
motivation remain. The October 20 single-occurrence note is saved and reopened
in Fantastical on Illinois Tech Fred → Calendar: PH 109, 11:15 AM–12:45 PM
America/Chicago. Schedule and ledger are reconciled through October 15;
these pacing changes are deployed, and the live October 20 continuation
was verified October 19.

The unqualified `Lecture update` command now reconciles both active courses;
`Lecture update 332` and `Lecture update 565` select only the named course.

Deck 07's coordinate section now includes the high school line example after
polynomial coefficients: slope/intercept versus values at x=0,1, followed by
the constrained third sample at x=2 and nonunique weights in a redundant
spanning family. Exact symbolic checks, full website/twelve-deck renders,
759 local slide-link/anchor checks, and visible review of all three new slides
at 1050-by-700 pass. The follow-up flow/correctness audit of Decks 05–07 adds
four targeted exercises (6/12/14 starred sets in 34/48/60 slides), fills the
missing affine-elimination answer notes, and clarifies subspace nonemptiness,
regression assumptions, and preview pacing. Details and validation are in
`notes/CHAPTER4-AUDIT.md`. Include these additions in the pending instructor
review; the recorded continuation and assessment coverage are unchanged.

Course notation now uses braces for bases; coordinates and basis-matrix
columns follow the listed order. QR uses A=Q R with plain R; its triangular
factor differs from R in A=C R. Deck 00's cumulative terms index now includes
compact notation cues, QR, and separate upper-/lower-triangular entries,
with no redundant generic triangular entry. These conventions are recorded
in AUTHOR_WORKFLOW.md. Bases and Coordinates now uses `^\top` for all
transposes; retain this notation in future revisions. The October 20
continuation is the next task. Three additional gold-star exercises now
cover algebra versus lengths, polynomial transition direction, and
differentiation in distinct input/output bases, with full answers in notes.
The closing transformation explanation returns to the opening motivation
and distinguishes output coordinates from the vector. The later sections
are consolidated as Dimension and Coordinate Arithmetic, and Transformations
and Change of Basis; the Course Map has seven entries and fits at normal
type size. Existing section anchors remain available.
Deck 07 now has 69 slides and 19 starred exercise sets; exact calculations,
rendering, and visible review of the new content slides pass.
The redundant-generator example now retains columns 1 and 3 after moving
the former fourth generator to second; the following alternate-basis and
frame examples use the same relabeling. Exact rank/dependence checks pass.
The opening “From building vectors to giving them addresses” summary slide
has the gold border selected by the instructor. Its October 19 revision uses
Concept / Notation / What it does, with concrete actions replacing the
question-and-payoff columns; the table and equations pass visible review.

Deck 07 also has a five-slide initial-value sequence at the end of
Transformations and Change of Basis. The worked undamped example uses
`y''+y=0`, its initial-data solution map, the inverse coordinate map, and
complex exponential coordinates. The critically damped car-spring model
`y''+2y'+y=0` supplies two starred exercise slides on the solution map and
its matrices in two output bases; answers remain in presenter notes.
The imaginary unit is `\sqrt{-1}`. Include this sequence and Deck 00's
linked index entry in the pending instructor review; the October 20
continuation is unchanged.
Symbolic checks of both initial-value problems and coordinate matrices pass;
the complete website and twelve-deck renders, local links, and five new
slide layouts are verified.

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
both membership parts ask “If so, find coefficients.” Its answer notes explain
why redundancy makes coefficients nonunique.

Inner Product Spaces (`slides/10-inner-product-spaces.qmd`, 46 slides) now
has an instructor-review draft covering inner products, projections,
Gram–Schmidt/QR, regression, and function/Fourier approximation. Review this
foundation before Special Topics (`slides/11-special-topics.qmd`, 55 slides).
The capstone prioritizes SVD and regression, with quadratic forms, FFT,
tensor products, power iteration/PageRank, and graph Laplacians as modular
choices. Its class-preferences slide asks students to rank optional coverage;
select topics and pacing after review. Companion demonstrations remain to be
built. The October 20 preparation and Chapter 4 review below remain.

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
Deck 09 now has its Chapter 5 draft and closing recap; review it before
continuing to Inner Product Spaces and Special Topics.

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

Rank-factorization notation uses R for the nonzero-row factor in
A=C R, writes the full reduced matrix as rref(A), and keeps U for PLU.
QR also uses plain R in A=Q R, as requested by the instructor; its role
is determined by context.
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

The lecture ledger and schedule are reconciled through October 15. Deck 06
is complete for classroom pacing, with remaining practice left to students;
its Course Outline estimate remains three 50-minute hours. Deck 07 has now
covered line coordinates, Fourier-mode independence, homogeneous coefficient
tests, and basis extraction by elimination. Resume systematic coordinates
on October 20, with the saved single-occurrence note described above.
Differentiation, regression, and PCA motivation still require follow-up.
The updated schedule renders successfully and passes desktop and phone
layout checks; the continuation anchor resolves. Remote deployment of this
checkpoint remains pending.

Quiz 2 website coverage is updated to Determinants and Euclidean Vector
Spaces through projections (excluding cross products), as confirmed by the
instructor on September 24. All-sections Canvas announcement `106481`,
“Quiz 2 on October 1: coverage through projections,” is posted and verified.
The updated coverage passed the full local website and slide renders.

Quiz 2 grading is complete. Canvas grades are posted and the All Sections
announcement [Quiz 2 scores are posted](https://iit.instructure.com/courses/23913/discussion_topics/107714)
was published and verified October 9. The released answer PDF includes the
anonymous distribution for 19 participants, excluding the confirmed
nonparticipant and Test Student. The identical answer PDF is in the current
assessment folder and canonical archive commit `89cc874`; the course archive
pin and Quizzes and Tests link are updated. The Dashboard grading task and
matching Academic reminder are complete. Private sources remain outside Git.

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
  All Sections. Quiz 4 and Quiz 5 coverage remains TBD. Quiz 3 grading is
  complete; all 20 Canvas scores are posted. The answer PDF includes the
  anonymous distribution, including both earned zeros, and is released in the
  current-assessment folder and canonical archive commit `bc6be6c`. The course
  release is commit `f60d12b`; Quarto publication and GitHub Pages deployment
  succeeded, and both live PDFs match the inspected release byte for byte.
  The All Sections [Quiz 3 grades and answers are posted announcement](https://iit.instructure.com/courses/23913/discussion_topics/108704)
  was published and verified October 22. The grading Dashboard task and
  matching Academic reminder are complete. Mixed lecture/quiz schedule rows now separate the
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
  Everyone in the Tests group. Coverage is Determinants through dimension in Deck 07; coordinates,
  change of basis, transformations and Matrix Spaces and Rank are excluded
  by the instructor's October 22 correction. Both website source tables
  are updated, and the Test 2 title-slide notice moves from Deck 08 to Deck 07.
  These pages and both decks render locally; the live coverage pages and
  Deck 07 title-slide notice were verified October 19.
  The self-contained coverage
  announcement [107870](https://iit.instructure.com/courses/23913/discussion_topics/107870)
  is published to All Sections; its October 15 correction and notification
  are verified. Grading remains due November 4, 2026.
  Existing save-the-date announcement
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
- Developed Decks 02–11 close with Big Ideas, a cumulative "How Far We
  Have Come" slide, and What Comes Next. Each Course Map links once to Big
  Ideas for the closing sequence; Deck 09 gained it with its Chapter 5 draft.
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
  title), the three Chapter 4 decks are audited drafts, and Deck 09 now has
  an instructor-review draft for Anton Chapter 5. Decks 10–11 have
  instructor-review drafts.
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

- The October 27 Deck 07 example now connects an infinite solution set to a
  basis of its null-space directions and unique affine parameters. Preserve
  this connection when reviewing Matrix Spaces and Rank; the remaining
  Decks 05–08 placement questions are in `notes/TODO-LATER.md`.
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

## Assignment 4 preparation — October 12, 2026

Instructor selected WileyPLUS 4.1 Q11, 4.3 Q09, 4.4 Q11, 4.5 Q16,
and 4.8 Q09a; all five full previews inspected. Instructor approved four
points each (20 total), three attempts, no deduction, best score, fixed
per-student values, and October 23 at 11:59 PM America/Chicago.

WileyPLUS question set Assignment 4 is saved and linked to Canvas 106680.
Its assessment identifier is `d81b5d4a-2f61-4970-8b3e-7dc905b2092b`.
The saved dashboard verifies five questions, four points each, October 23 at
11:59 PM, and “Available to students” after the approved release; its Policies tab verifies three
attempts, best score, immediate feedback, assistance timing, and per-student
randomization. Canvas 106680 is published for Everyone, in Assignments, worth
20 points, with individual External Tool submission and a new-tab launch.
The concise description links to the assignment and Assignments pages.
Reopened saved settings verify Due, Until, and Available from are blank.
WileyPLUS still displays its duplicate-LMS-deadline warning despite these
blank saved Canvas fields; recheck at release rather than restoring a Canvas
deadline. Instructor launch reaches the correct saved set.

Local assignment detail, Assignments table, Schedule link, metadata Canvas
URL, and Deck 07 title reminder are prepared. Website and twelve-deck renders
completed; assembled deck title and website preview inspected. Slide render
reported unchanged classlib resource warnings. All 176 local references from affected pages resolve; Assignment 4 and the
Assignments table pass desktop and phone review, and the Deck 07 title passes
1050-by-700 review.

Fred published the All Sections announcement
[107874](https://iit.instructure.com/courses/23913/discussion_topics/107874),
“Assignment 4 is available in WileyPLUS,” on October 12 at 3:54 PM CDT.
The posted text and corrected space after the Assignments-page link are verified.
Publication completed October 12 after Fred’s explicit approval to publish
Canvas and WileyPLUS. Course Checkpoint `1dffa0e` has successful publishing
and Pages deployment runs; live assignment details, Assignments and Schedule
links are verified. WileyPLUS confirms Available to students, five questions,
20 points and October 23 at 11:59 PM CDT. Reopened Canvas settings verify
Published for Everyone, 20 points, Assignments, the correct individual External
Tool deep link, new-tab launch and blank Due/Until fields. Canvas Student View
shows the assignment and WileyPLUS launch button; no answers or scores were
submitted. Actual graded-submission passback remains untested. Do not repost
the verified announcement. Preserve the October 29 WileyPLUS-grading/Canvas-
transfer review deadline. This closeout Checkpoint preserves the verified
external-completion updates.

## Canvas homework and quiz setup — October 9, 2026

All six numbered homework assignments are 20 points. The Assignments group
drops one lowest score and excludes the unchanged 10-point Diagnostic Survey
with Never Drop. All five quizzes already exist at 20 points with schedule-matching
dates; the Quizzes group now drops one lowest score.

Assignment 4 now uses the configured External Tool launch described above.
The remaining Canvas placeholders are saved and verified, **unpublished**,
with no submission requested yet. Due dates reserve the schedule date at
11:59 PM America/Chicago. Reuse these IDs during the full assignment setup:

- Assignment 5: [106681](https://iit.instructure.com/courses/23913/assignments/106681), due November 6, 2026.
- Assignment 6: [106682](https://iit.instructure.com/courses/23913/assignments/106682), due November 20, 2026.

When the WileyPLUS launches are configured, replace the placeholder submission
type with External Tool, set the authoritative deadlines in WileyPLUS, and
clear Canvas Due/Until fields under the existing course workflow. Existing
Assignments 1–3 retain their WileyPLUS setup and blank Canvas due dates.

The student-facing Assignments page now records the 20-point homework and
lowest-score-drop policy, including the Diagnostic Survey exception.
The Quizzes and Tests page also records the 20-point quiz and lowest-quiz-drop
policy.
Affected pages render successfully and pass desktop/390-pixel browser layout
checks. The policy updates have successful publishing and Pages deployment runs,
verified October 9.
