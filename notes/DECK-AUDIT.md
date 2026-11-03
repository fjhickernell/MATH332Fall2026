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
