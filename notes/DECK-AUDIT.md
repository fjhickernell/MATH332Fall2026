# MATH 332 deck accuracy and clarity audit

## November 19, 2026 — tennis-racket wobble explanation

Added a short continuation immediately after the racket example. It separates
the inertia tensor's three positive principal moments from the eigenvalues
of the two-component small-wobble linearization: an imaginary pair at the
extreme-moment axes and a positive/negative real pair at the middle axis.
Presenter notes retain the rigid, torque-free assumptions, the omitted neutral
spin-speed direction, the initial-growth qualification and the distinction
between oscillation and decay. The continuation previews the exponential
mode without deriving Euler's equations. Terminology links now point to the
racket example's first substantial treatment.

Independent mechanics review and the primary university mechanics references
support the explanation. Both affected decks render; the two racket slides
fit at 1280×720, and the new continuation and revised index also pass
inspection at the standard 1600×1000 size, with no MathJax errors or browser
console warnings/errors. Source prose and whitespace
checks pass. The new explanation is slide 14, after the original example on
slide 13. The deck has 73 slides. The instructor gave the demonstration in
the [November 19 lecture](LECTURE-UPDATES.md#november-19-recording-evidence-and-continuation).

## November 19, 2026 — Leontief review and transition

Expanded the original input-matrix example into the opening topic of Powers
and Dynamics, before its general powers and matrix-function formulas. The new
demand forecast activates both eigenmodes with whole-number coordinates.
The worked sequence covers echelon form and back substitution, eigenpairs,
shared net-output eigendirections and their economic interpretation, basis
coordinates, powers, successive input requirements, iteration and the response
as a matrix function. Preserved the earlier iteration explanation and existing
Leontief anchors. The signed adjustment direction is distinguished from a
feasible production profile, and invertibility from series convergence.
The interpretation explicitly identifies parallel total output, internal
demand and net output available for external demand along an eigendirection.
The coordinate solve is followed by a worked baseline-plus-adjustment
decomposition of production and the corresponding internal/external demand
changes, with negative entries explicitly interpreted as decreases.
The final classroom-use audit found no mathematical or economic errors.
It clarified the scalar component notation in the eigenspace calculations
and distinguished convergence of input-round vectors from componentwise
monotonic decrease. Independent exact-arithmetic review confirmed every
displayed numerical value and both feasible production plans.

Exact symbolic checks and independent source review passed. The website and
all twelve decks render without warnings; 477 local references in the changed
outputs and all twelve decks' navigation targets pass. Visible slide checks at
1600×1000 and 1280×720 verify the review and general-function transition, with
no MathJax errors or browser console warnings/errors. The revised Terms index
and overview links navigate to the intended slides. The planned Schedule row
fits desktop and phone widths; all six monthly tables fit at 390 pixels.
Source prose and whitespace checks pass. Instructor review, teaching and
publication remain separate; no coverage ledger or calendar occurrence changed.

## November 17, 2026 — map direction and multiplication order

Audited Decks 00–11 for action diagrams whose reading direction conflicts
with adjacent column-vector products. Such diagrams now place the input on
the right and output on the left, matching the factors in the product.
Corrections cover introductory action/composition and affine-layer boxes,
inverse round trips, PLU actions, determinant products, coordinate conversion,
four-space maps, and the eigenbasis/ODE routes and paired figures. Labels,
panel placement, captions, accessible descriptions and presenter notes agree
with the reversed arrows. The author workflow records the convention.
Conventional function signatures, basis-image definitions, row operations,
solver procedures, chronological workflows and convergence arrows retain
their usual directions.

Validation: all twelve decks render successfully. The assembled site's 24
primary outputs have 1,844 local references and 851 fragments, with no broken
targets. Browser review verifies the revised composition, inverse, PLU,
determinant, coordinate, four-space and solution-function diagrams at
1600×1000; the ODE route and numerical commuting square also fit at
1280×800. No console, MathJax or image-loading errors were found. SVG XML,
geometry preservation and whitespace checks pass. These revisions are included
in the November 17 checkpoint; remote deployment remains unverified.

## November 17, 2026 — eigenbasis coordinates and solution spaces

Audited all of Deck 09, including worked examples, exercise answers,
multiplicities, complex pairs, matrix functions, population dynamics and the
real symmetric spectral theorem. No arithmetic or theorem correction was
needed. The exponential slide did need a visible distinction between the
general matrix-exponential solution and the eigenbasis formula that requires
diagonalizability; this condition is now explicit. Taylor-series examples
have their own continuation slide to keep the exponential slide readable.

Added labeled coordinate-to-vector and initial-data-to-function boxes, with
the map on each connecting arrow, and an explicit derivation of the
decoupled differential system. The full solution product includes its initial
vector and is paired with the change/evolve/reconstruct coordinate route;
notes distinguish the evolution matrix from a solution vector.
The paired initial-vector and solution-function
boxes display the same coordinate column. Paired phase
portraits depict one trajectory in the eigenbasis and original coordinates,
with matched time markers and a reproducible figure generator. The
initial-data map now distinguishes a whole solution function from its value
at one time. Corresponding initial-vector and solution-function bases share
the same fixed coefficients, while current-state coordinates evolve.
Differentiation on the finite-dimensional solution space provides an
optional conceptual extension. The earlier undamped spring returns as a
first-order system, reproducing the previous complex coefficient change and
the real circular flow. Presenter notes distinguish the critically damped
case, where the solution map still exists without an eigenbasis.

The coordinate-box diagram is followed by a worked oblique-eigenbasis
example, with a four-box comparison of the two routes through the action,
and a matching starred exercise. The exercise distinguishes the input
vector from its eigenbasis coordinate column and checks the reconstructed
output against direct multiplication; complete answers are in presenter notes.

The optional generalized-eigenvector definition now uses the algebraic
multiplicity as a sufficient common kernel power, includes ordinary
eigenvectors, and distinguishes a vector's potentially smaller minimal
power. Its new third slide states the full generalized-basis theorem, with
the real-matrix/real-roots condition for a real basis and the complex
alternative. Generalized eigenspace is included in the terminology index.

Use $\mathbb{K}$ for a generic scalar field, explicitly defined as $\reals$
or $\mathbb{C}$ for the solution map. The same generic-field notation is
used in Bases and Coordinates and recorded in the author workflow;
the specific finite field $\mathbb{F}_2$ retains its notation.
The eigenvalue-characterization
equation explicitly includes nonzero membership in the shifted null space,
with the nonzero-vector assumption stated before its equivalences.

Reduced Eigenvector Bases and Diagonalization from ten main outline entries
to five. The worked example, coordinate diagram and distinct-eigenvalue
result are continuations of the eigenbasis heading; multiplicities continue
the repeated-root heading; practice continues the recipe. All slide breaks,
content and named anchors are preserved.
Powers and Dynamics is also reduced to five main entries: powers, functions,
the exponential/differential system, the initial-data solution map, and
discrete/continuous comparison. Examples and supporting results are
continuations under those umbrellas; the population-example anchor is retained.

Updated the section outlines, Big Ideas, and Deck 00's alphabetical index.
The current lecture pickup and coverage ledger are unchanged: these are
prepared additions, not evidence of classroom coverage.

Validation: the original 20 exact symbolic checks pass in `qmcpy`, including
diagonalization, the exponential differential equation and initial data,
derivative intertwining, oscillator eigenpairs, complex coefficients, and
the real rotation formula. An additional 36 exact checks validate the new
coordinate example/exercise and generalized-kernel dimensions, inclusion,
exponent sufficiency and full bases for defective and semisimple examples.
The root website and all twelve decks rendered earlier in this audit;
modified Decks 00, 07 and 09 were rendered again after their final additions.
Deck 09 now has 61 slides.
Across 24 primary assembled outputs, all 1,904 local references and 851
fragments resolve. Previous/next metadata passes for all twelve decks.
Browser inspection at 1600×1000 and 1280×800 verifies the new figure's footer
clearance; the other new/revised slides, outlines and index continuations
pass visible review. The eigenfunction index link, solution-map section
link and neighboring-deck navigation reach their intended destinations.
The final assembled preview has no console warnings/errors or MathJax
errors. The boxed diagrams, added null-space equivalence and reduced section
outline also pass focused rendering and visible review. Visible-source
bold/punctuation checks and `git diff --check` pass.
The new worked square, exercise, generalized definition and full-basis
statement, dynamics outline, comparison slide and terminology entry pass
visible review. The dense new example and definition also fit at 1280×800.
Blackboard-bold field notation in Decks 07/09 and the full ODE solution
product also pass visible review; the solution product fits at both review sizes.
These additions are included in the November 17 checkpoint; instructor content
review remains open.

## November 12, 2026 — queued slide navigation and Taylor-series connection

The shared navigation helper now reads the current hash rather than replaying
obsolete queued URLs. It also recognizes a direct child target when Reveal's
earlier hash listener reaches the slide before the helper. Horizontal arrows
still start a new section at its overview.

The new regression distinguishes the original infinite replay and an
incomplete fix that lost the requested child. All five Node tests pass.
In an actual browser fixture, the original code reaches the 43-event safety
cutoff; the refined fix settles on the intended child after two events and
remains there while idle. Links, horizontal arrows and browser back/forward
are verified. All twelve decks render with the shared fix. Canonical library
commit `87811e3` is published and intentionally adopted by course `5fd74d0`.
Its [publishing run](https://github.com/fjhickernell/MATH332Fall2026/actions/runs/43248359747)
and [Pages deployment](https://github.com/fjhickernell/MATH332Fall2026/actions/runs/43248605853)
succeeded. Live verification confirms the current-hash helper and child-target
guard are present, the deep link reaches its child, and horizontal navigation
starts at the next section overview. Issue 3 is closed after this verification.

The matrix-exponential slide now shows the full equality from a convergent
Taylor series to the eigenbasis formula for f(A). Diagonalizability and
convergence of the scalar series at every eigenvalue are explicit. Sine and
cosine are examples; notes explain centered series and their convergence
domain. The revised slide renders and fits at 1600×1000 and 1280×800; the final
Taylor-series identity and convergence condition are also verified live.

## November 12, 2026 — matrix functions and practical eigenvalue computation

Deck 09 adds practical eigensolver guidance and three slides after matrix
powers: general matrix functions, the matrix exponential and linear
differential systems, and a worked two-mode example. The diagonalizable
hypothesis and scalar-function domain are explicit; the exponential's series
definition applies to every square matrix. The existing exercise now contrasts
discrete multiplication with continuous exponential evolution.

The spectral theorem now directly says every real symmetric matrix is
orthogonally diagonalizable. The opening direction heading is dimension
independent, the definition highlights the nonzero requirement, and the
invariant-span statement uses inclusion with equality for nonzero eigenvalues.
Deck 00's alphabetical index and the course/notebook descriptions include the
new matrix-function topics.

All 16 companion code cells pass in qmcpy in 12.9 seconds, with saved outputs.
Symbolic checks verify a polynomial of the running matrix, its exponential,
the differential equation and initial conditions. The root website and all
twelve decks render without warnings or errors. Across 23 primary assembled
pages/decks, 1,858 local references and 841 fragments resolve. Representative
layouts pass 1600×1000 and 1280×800 browser review, and the new index and section
links reach their intended slides. The reviewed browser reports no warnings
or errors. Visible-source style and diff checks pass; bold “nonzero” is the
instructor's explicit emphasis request.

These are prepared teaching additions; their construction does not establish
classroom coverage. Instructor review remains open.

## November 11, 2026 — characteristic-polynomial convention

Deck 09 and its companion follow Anton's monic
`p_A(lambda)=det(lambda I-A)`. The definition slide visibly notes that some
sources use `det(A-lambda I)`, with the same roots and multiplicities.
Presenter notes explain the `(-1)^n` factor, the monic leading coefficient
and the constant term `(-1)^n det(A)`. The worked determinant, triangular
product and similarity identity retain the monic convention. SymPy's
`charpoly` matches it directly; the companion's code is unchanged from the
previously validated monic version, with the convention note added in Markdown.

The seven exercise sets and their answers are retained. This Checkpoint
includes the clarification; remote deployment remains unverified.

The final monic companion passes all 14 code cells in a fresh qmcpy run,
with saved outputs and no errors. Deck 09 renders, and the definition plus
alternative-convention note fits at 1280×720 with no browser warnings/errors.
The visible-prose and diff checks pass. The latest completed main-branch
publishing workflow, run 43078470941 for 638e543, succeeded.
Its separate Pages deployment run 43078769945 failed while creating the
deployment with GitHub HTTP 502; no local rendering failure was reported.
The next publication must not be described as live until deployment is verified.

## November 11, 2026 — SVD in Inner Product Spaces

Moved the existing SVD and regression-through-QR/SVD sections to Deck 10,
after least squares and before function/Fourier approximation. Deck 10 has
68 slides; Deck 11 retains 28 slides of optional quadratic forms, FFT,
networks and the single tensor glimpse. Every original instructional slide
is preserved across the two decks; only the reference-term lists were
regrouped. Both companion notebooks retain their existing filenames.
The SVD notebook changes only Markdown links and introductory routing;
its code cells and saved outputs are unchanged.

Course maps, closing summaries, terminology-index links, the Deck 07 PCA
forward link, notebook links and the welcome-page outline now follow the new
location. Deck 09's recap example has a presenter reminder that the 2-norm
condition number uses singular values; the symmetric-positive-definite
eigenvalue-ratio exception is explicit there and in Deck 10's sensitivity notes.

The root website and all twelve decks render successfully; 1,311 local
links/assets, including destination fragments, pass across the assembled
welcome page, Notebooks page and twelve decks. Source-style and diff checks
pass, with no new duplicate anchors. At 1280×720, the revised course maps,
SVD outline, Deck 10 cumulative recap and next-deck handoff, sensitivity slide
and retained tensor slide fit and typeset correctly. The tensor-to-SVD link
opens the intended child slide in Deck 10. Both presenter corrections are
present in the rendered notes; no browser warnings/errors were reported in
the reviewed deck. The expanded course outline fits at 1280 and 390 pixels;
the revised notebook listing fits at 390 pixels without horizontal overflow.
Instructor content review remains open; this Checkpoint includes the changes.
Remote deployment remains unverified.

## November 10, 2026 — eigenvector notation and optional chains

Deck 09 and its companion use V for ordinary eigenvector matrices and Q for
orthonormal eigenvectors; P remains a general similarity change of basis.
Two explicitly optional slides define generalized eigenvectors and work a
length-two chain for the existing defective 2-by-2 example. G denotes the
generalized basis. The terms index links to both new concepts; a matching
notebook cell verifies the chain, basis, and coupled Jordan-block identities.
No general Jordan algorithm or defective-matrix power formula is included.

The Eigenvalues companion passes all 14 code cells in a fresh qmcpy run
(13.2 seconds), with saved outputs and no errors. The root website and all
twelve decks render successfully. All 1,834 local references and 820 anchors
across 23 assembled outputs resolve. The optional slides, V diagonalization
slide, and both modified terms-index slides pass visible browser review;
both new index links navigate to their intended slides. Source-style and
diff checks pass. Instructor review and optional-topic selection remain open.

## November 2, 2026 — all existing decks

Reviewed the complete current Quarto sources for Decks 00–11, including
worked examples, all 75 exercise sets and their presenter answers, theorem
conditions, proof dependencies, scalar fields, notation, and cross-deck
connections. The slides remain the authoritative mathematical exposition;
this file records findings and verification only.

The review includes the instructor's preceding Deck 08 revisions: introduce
rank–nullity immediately after the definitions, explicitly connect it to
column-space dimension, use row echelon form until the direct A=CR recipe,
and highlight original columns and nonzero RREF rows.

### Findings and corrections

| Deck | Result |
|---|---|
| 00 — Why Linear Algebra? | Restrict the camera-composition example to linear maps with a shared origin and orthographic projection; note the additional operations needed for translation/perspective. Add the rotation activity's presenter answer and the linear-isometry index entry. |
| 01 — Systems and Matrices | Repair the labeled-but-undrawn final top resistor in both circuit diagrams. Specify real scalars for the zero/one/infinite classification; clarify squaring both sides and optional pivot normalization. Add missing exercise explanations in presenter notes. |
| 02 — Inverses and Invertibility | Use sufficient row echelon form in the recap; scope square-matrix claims to two-sided inverses; clarify that determinant magnitude alone does not diagnose near singularity. |
| 03 — Matrix Structure and Transformations | Distinguish codomain dimension from image dimension; state linearity before the basis-images rule; add the Householder exercise proof in presenter notes. |
| 04 — Determinants | No material mathematical correction identified. Reviewed determinant rules and examples, exercise answers, permutation signs, Wronskian qualifications, and Jacobian/spherical-coordinate calculations. |
| 05 — Euclidean Vector Spaces | Qualify the cross-product direction/normal statement when the product is nonzero; apply the inline-fraction convention. |
| 06 — Vector Spaces, Subspaces, and Span | No material correction identified. Reviewed axioms, closure/span arguments, examples and scalar-field distinctions, including the real-versus-binary-field removal exercises. |
| 07 — Bases, Dimension, and Coordinates | Describe one fitted response vector rather than three fitted responses. Correct the PCA notes to say dot product, rather than cross product, for the score columns; apply the inline-fraction convention. |
| 08 — Matrix Spaces and Rank | Preserve the instructor's revised rank–nullity/echelon/CR sequence; add presenter justification of the orthogonal pairs and standardize transpose/numerical-column notation. All worked examples and exercises checked. |
| 09 — Eigenvalues and Eigenvectors | No material mathematical correction identified; standardize transpose notation. Review includes diagonalizability conditions, complex pairs, discrete dynamics and symmetric spectral theory. |
| 10 — Inner Product Spaces | Correct the recap's coefficient argument order under the declared complex-inner-product convention; define the weight matrix in weighted least squares; clarify orthonormal coordinates and the integral of a square. Standardize basis, matrix and vector notation. |
| 11 — Special Topics | Express the tensor coordinate matrix using coordinate columns of abstract factors; correct the SVD recap link and spectral-theorem reference; require orthonormal input eigenvectors in the SVD construction; replace the loose ellipse-curvature claim with quadratic scale. Standardize numerical notation. |

The course workflow now records the instructor's reduction principle: request
only the form needed for the operation, and match the subsequent examples to
that form. No topic dates, assessment coverage, assignments, grades, or
notebook contents were changed by this audit.

### Validation

- Exact/rounded computational checks in the existing qmcpy environment:
  19 checks for Decks 00–04 (systems, inverses, LU/PLU, circuits, Leontief,
  covariance/precision, ODE grid, determinants, rotations and minimum norm);
  52 checks for Decks 05–07 (geometry, bases, coordinate arithmetic and
  conversions, differential equations, regression, PCA and frames);
  46 checks for Decks 09–11 (eigenvalues/dynamics, QR/projection/regression,
  integrals/Fourier coefficients, SVD/pseudoinverse, DFT, Laplacians and
  separability). Separate exact checks of Deck 08 cover its echelon/RREF
  matrices, four-space bases, factorization exercises, compatibility and
  polynomial-map calculations.
- The root website and all twelve decks render successfully with no warnings
  or errors found in the build logs. Generated slide output is assembled
  locally beneath `_site/slides`.
- All 1,240 local links and asset references emitted by the twelve decks
  resolve, including destination fragments. Rendered deck IDs are unique.
- Existing explicit anchors and all 75 exercise sets are preserved; visible
  prose emphasis/terminal-period checks and `git diff --check` pass.
- Both pinned dependencies remain clean and unchanged.

### Remaining review and publication

Mathematical/source review is complete; no further mathematical error was
identified in this pass. This does not establish that every presentation
choice has instructor approval. Enrichment selection and pacing remain the
instructor's choices, especially in the later draft decks.

Browser security blocked the local-file preview. No alternate browser or
local-server route was attempted. Visual fit, MathJax display, and interactive
navigation were not verified in this pass; rendered HTML/link checks do not
replace that review. Recheck the changed slides and diagrams visually before
classroom use, including the circuit, introductory camera composition,
rank–nullity/CR sequence and tensor-coordinate explanation.

The corrections and this record are included in the November 2 Checkpoint.
Remote CI/deployment and live verification remain pending. The recorded
November 3 Deck 07 lecture continuation is unchanged.

## November 4, 2026 — Deck 08 classroom-preparation review

Rechecked the complete 35-slide Matrix Spaces and Rank deck, including all
six exercise sets and presenter answers. Sixteen exact-arithmetic checks
confirm the running echelon/RREF example, four-space bases and dimensions,
rank factors, compatibility conditions, factorization and orthogonality
exercises, and polynomial differentiation/evaluation maps. No new
mathematical correction was needed; preserve the instructor's existing
rank–nullity, echelon-form, and direct CR sequence.

Inspected every slide at 1280×720, including the four-space Course Map,
factorization proofs, exercises, and cumulative summary. Content clears the
footer, and no MathJax or browser-console errors were found. The coefficient
interpretation also fits at 1600×1000. Course Map and section links were
followed in the browser. This completes this agent review, not instructor
approval of the deck or companion notebook.

During Fred's parallel Deck 07 review, retained full transition subscripts
throughout the Taylor inverse slide and replaced the polynomial-only
regression setup with fixed nonlinear functions of two predictors. Updated
the observation table, matrix, outline label, and presenter explanations
together. Exact checks confirm the feature evaluations, independent sampled
columns, and nonzero fitting residual; the three revised slides fit at
1280×720 and 1600×1000. Existing anchors remain for previously published links.

The isolated root website and all twelve decks render without warnings or
errors. All 175 local links/resources from Decks 07–08 resolve, including
destination fragments; explicit anchors and all 20/6 exercise sets are
preserved. Visible prose style and `git diff --check` pass. At this review,
changes remained local pending Checkpoint; no deployment or instructor approval
was claimed.

November 12 closeout of [teaching cleanup issue 2](https://github.com/fjhickernell/MATH332Fall2026/issues/2):
Fred confirmed the November 3 cleanup complete. The four Taylor-coordinate
slides and two regression setup slides are accepted; the cleanup and lecture
reconciliation were published in `731e2b8`, with the coordinate/regression
refinements in `10f1505`. The November 3 lecture and November 5 calendar
continuation are reconciled in `notes/LECTURE-UPDATES.md`; later reconciled
meetings supersede that pickup. Broader review of the Chapter 4 decks and
companion notebooks remains separate and open.

### Instructor follow-up: visible orthogonality and practice

The deck now has 38 slides and seven exercise sets. Added a visible proof of
both orthogonal-complement identities: the homogeneous equations are exactly
the zero dot products with all rows, hence with their span; apply the same
equivalence to the transpose for the column/left-null pair. The proof does
not depend on a separate dimension argument.

Moved Orthogonal Pairs to follow the first row/column/null-space calculation
and its new starred basis-extraction exercise, before Rank and Solution Sets.
This brings the geometry directly after concrete spaces while retaining the
instructor's rank–nullity placement immediately after the definitions. The
new exercise fills the early computational-practice gap; retain the six
existing multi-part sets and their presenter answers.

Added an original SVG of the orthogonally placed four spaces, with a visible
attribution/link to Figure 1 in Strang's MIT-hosted essay. The two ambient
spaces have separate zeros, right-angle markers, and labeled dimensions;
the row-to-column arrow represents the restriction of the matrix. Shapes
are explicitly schematic. This is a course drawing, not an embedded book scan.

The new exercise and right-angle geometry pass exact checks. The diagram,
proof, and exercise fit at 1280×720 and 1600×1000; the revised Course Map
order was inspected. The website and affected deck render cleanly; all
176 local links/resources from Decks 07–08 resolve, IDs are unique, existing
anchors survive, and visible-source style checks pass. Refreshed the
validated generated Decks 07–08 in the existing local preview locations.
No publication or instructor approval is inferred.

### Instructor follow-up: the row-space restriction

A continuation immediately after the four-space picture now proves the
one-to-one and onto claim visibly. The first argument shows that a row-space
vector in the kernel is perpendicular to itself and hence zero, then applies
this to the difference of two inputs. The second projects a preimage onto
the row space; its perpendicular component is killed by the matrix, so the
projected vector gives the same output. The domain restriction, real scalar
field, and column representation of row-space vectors are explicit.

The deck now has 39 slides and retains seven exercise sets. Local rendering
and source checks pass; browser layout review of the new continuation remains
pending. These changes are included in the course Checkpoint; remote
deployment and live verification remain pending.


## November 6, 2026 — matrix-space intuition and applications

Deck 08 now has 56 slides and eight exercise sets. A practical four-space
table follows rank–nullity and links to the new Applications section after
Orthogonal Pairs. Its examples cover regression, camera/sensor measurements,
PCA, network flows, and chemical balancing. Existing examples, exercises,
and explicit anchors are preserved. The cumulative terminology index already
contains the important terms introduced here.

The six regression slides retain one instructor-selected four-row,
three-column design throughout: features 1, t, and 1+t for t=0,1,2,3.
One imperfect least-squares fit connects column space, coefficient ambiguity,
the determined intercept/slope combinations in row space, new predictions,
and the nonzero left-null residual. The design remains fixed; hats distinguish
fitted responses from observed responses. PCA distinguishes positive sample
variation, zero-variation directions, observation scores, and truncation.

Exact symbolic checks verify the final regression fit, all four-space bases,
row combinations and predictions; separate checks verify the PCA variance
split and reconstruction, sensor recovery, network balances, and chemistry.
The complete website and twelve-deck project render without warnings or
errors; the final revised deck also renders. New application layouts and
the final regression explanations pass 1280×720 visible review. The prior
row-space-restriction continuation also passes visible review. All 1,849
local references and 826 destination anchors pass, as do source-style checks.
The Course Map spacing is tightened to accommodate the added section link.

These changes are included in this Checkpoint. Instructor review remains
open; remote deployment and live-page verification are separate from the
completed local validation.
