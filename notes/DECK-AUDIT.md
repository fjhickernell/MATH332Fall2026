# MATH 332 deck accuracy and clarity audit

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
preserved. Visible prose style and `git diff --check` pass. Changes remain
local pending Checkpoint; no new deployment or instructor approval is claimed.

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
