# General Vector Spaces deck audit

Completed October 3, 2026 on M5. This records editorial decisions and
verification; the mathematical exposition remains authoritative in the slides.
The initial audit and reminder/proof revisions passed the October 3 build and
Pages deployment, through commit `1c78f80`, including the notation and
pivot-column boxes. The October 4 renumbering and notebook Checkpoint has
not yet had its remote deployment verified.

## October 27, 2026 — clarity and prerequisite review of Decks 06–07

The complete source review retains the progression from vector-space
operations and closure to span, independence, bases, dimension, coordinates,
and matrix representations. It preserves every previous example, the 14
Deck 06 and 20 Deck 07 exercise sets, and all previous explicit anchors.
No assessment content or coverage changes are part of this review.

The opening concept table now explicitly names V as a vector space and includes
Subspace: W is a subset containing zero and closed under linear combinations.
The row sits between Linear combination and Span. The revised deck renders
without warnings; the expanded table and takeaway fit in the browser preview.
The coordinate section now pairs expanded sums with row-times-coordinate
products throughout the standard and alternative vector bases, coordinate
arithmetic, affine solution directions, polynomial bases, and symmetric-matrix
example. Polynomial rows contain whole polynomials; the symmetric-matrix row
contains whole basis matrices. Redundant-generator coefficients remain weights,
distinct from unique coordinates in a basis. This convention is recorded in
AUTHOR_WORKFLOW.md.

Deck 07 renders without warnings. All revised coordinate layouts were checked
at 1280×720; the line comparison and symmetric-matrix slide keep both sum and
product forms without footer overlap. Exact reconstruction checks pass. The 89
slides, 20 exercise sets, and previous explicit anchors are preserved. These
table and coordinate edits are included in this Checkpoint; remote deployment
and live verification remain pending.

Instructor notation follow-up: use explicit column vectors wherever space
permits, reserving transposed rows for crowded layouts. Expanded the columns in
the coordinate arithmetic, basis definitions and exercises, oscillator, PCA
observation, and frame examples. The arithmetic example combines its input
polynomials into one line and labels their full coordinate columns in the
calculation. Genuine transpose operations are unchanged. AUTHOR_WORKFLOW.md
records this preference; the revised layouts and warning-free render pass.

Transition-column clarification: the original anchor now opens a P1 example
with B={1,1+t} and C={1,t}, showing each old basis polynomial's old and new
coordinate columns and the resulting numerical conversion matrix. A new
continuation derives the column rule from the explicit equality [b_j]_B=e_j
and explains that each bracketed term is a whole numerical column. The
preceding R^n slide names Q=P_C^{-1}P_B and explains its direction; presenter
notes distinguish rebuilding a vector from reading its coordinates. The
sequence now has 90 slides, retains all prior anchors and 20 exercise sets,
and leaves the teaching pickup unchanged. The three revised layouts, exact
conversion calculations, and warning-free render pass. These edits are
included in this Checkpoint; remote deployment and live verification remain
pending.

Standard-basis emphasis: the existing standard-basis slide highlights that
[x]_E=x in R^n. The numerical basis-matrix slide uses E consistently in that
identity and the change-of-basis route labels its middle vector x=[x]_E,
making the standard-coordinate identification explicit. No slides or exercises
are added by this follow-up. All three revised layouts fit at 1280×720; the
90-slide render has no warnings and the source checks pass.

Final coordinate clarity pass: move the same-vector/two-bases example and its
practice immediately after the standard basis, before the general coordinate
map. Update the section outline accordingly. Use alpha/beta consistently for
scalar weights and explain the one-to-one/onto property in plain language.
Show the polynomial arithmetic inputs expanded in their chosen basis before
reading their coordinate columns. Remove the repeated linearity calculation
from the length slide, retaining its length calculation, criterion and
orthonormal-basis definition, with full columns in the freed space. Call the
nonstandard basis {1,t,1+t^2} D rather than E. Clarify that another basis can
change a polynomial's coordinates and describe the identity transformation as
T(v)=v, avoiding confusion with an identity matrix. The abstract-vector,
sum/product, standard-basis, affine-displacement and transition-column
explanations remain. No examples, exercise sets or anchors are removed, and
the deck remains 90 slides. Exact reconstruction and length checks pass; the
deck renders without warnings. Changed layouts fit at 1280×720, the outline
matches the new order, and the source style and whitespace checks pass.

PCA comparison follow-up: spell out Principal Component Analysis (PCA) in the
overview table. The score-calculation slide now displays the full numerical
product XQ=S, with matching observation rows aligned in X and S. Keep the
square-root-of-two score factor visible. The second columns have squared
lengths 482 and 68 respectively; this compares overall variation rather than
claiming that every score entry has smaller magnitude. All eight observations,
the basis matrix, score values and dimensions, and coordinate interpretations
remain unchanged. Exact multiplication, the warning-free render and the final
1280×720 layout pass; the first observation's coordinates use a full column.

Checkpoint validation: the complete website and all twelve decks render
without warnings. The assembled output passes 1,938 local link/asset checks
across 26 pages/decks and all twelve deck navigation records. Previous build
and Pages runs succeeded. All 20 exercise sets and prior anchors remain;
exact arithmetic, slide-source style, whitespace, and assessment-confidentiality
checks pass. AUTHOR_WORKFLOW.md, STATUS.md and the immediate handoff are
reconciled. Remote publication of this Checkpoint remains separate from these
local checks.

Instructor follow-up: keep the paired real/F2 vector-removal exercises
open-ended. Ask whether removing a vector could leave a subspace; do not
disclose either conclusion, prescribe the zero/nonzero case split, or add
“Explain your reasoning” instructions—the justification is understood.
The binary case ends with the instructor-requested follow-up “What is v+v?”;
its derivation and worked answers remain in presenter notes. The revised deck
renders without warnings; the open-question layout was inspected. The wording
and follow-up are included in this checkpoint; remote deployment remains pending.

- Rename the closure section to Subspaces and Closure, keeping its old anchor;
  Spans and Membership remains the subsequent construction section. Supply
  the span-closure/minimality justification in presenter notes, and explicitly
  defer the polynomial minimal-spanning challenge until the dimension argument.
- Rename Independence and Bases to Independence and Redundancy, retaining
  its anchor, to distinguish it from Bases and Unique Representations.
- Keep the coordinate-map proof and arithmetic practice together. Move the
  polynomial numerical-conversion example after the numerical basis-matrix
  rule, where its inverse and reference-basis roles have been introduced.
- Add “Basis directions locate every solution” before polynomial coordinates:
  x+2y=1 has xp=[1,0]^top, null-space basis {[-2,1]^top}, and the unique
  parameterization x=xp+t b1. Coordinates apply to x-xp in the direction space;
  the shifted solution line itself is not called a vector space or given a basis.
- In basis extension, name an independent list in V and a row of abstract
  vectors, avoiding a switch to numerical-column language inside the proof.

The October 22 ledger's pickup remains “Build a basis by adding or removing
vectors” (34/90), then the remaining dimension material and coordinates.
The relocated monomial practice can be revisited. The new slide increases
Deck 07 from 88 to 89 slides; the subsequent transition-column clarification
brings it to 90. Deck 06 remains 51, including title slides.

Validation: the complete website and all twelve decks render without warnings.
Both revised decks were refreshed after wording fixes. All 120 local links
from the two decks resolve, including preserved and moved anchors. Mathematical
review verifies the affine parameterization, basis/uniqueness claims and scalar
field conditions. The visible source has no prose bold or unnecessary terminal
periods (HTML comments and presenter notes excluded). Changed layouts and
navigation are checked in Safari and the separate browser preview at 1050×700.
These changes are included in the October 27 checkpoint; remote deployment
and live verification remain pending.

## October 21, 2026 — Bases and Coordinates reasoning and structure

The instructor found that examples separated prerequisites from the claims
they should explain. The revision keeps every example and the 19 original
exercise sets, adds a basis question and a linked roadmap, and frames each
section by its purpose. It grows from 69 to 81 slides without changing the recorded
October 22 lecture continuation or assessment coverage.

The main progression is construction, independence, bases, dimension,
coordinates and arithmetic, then transformations. The dimension comparison
uses an explicit vector-list factorization, a homogeneous coefficient system,
and a free-variable argument, before
dimension is defined; it does not assume the dimension or rank-nullity
theorems. The exact-size equivalence uses the same column-list factorization,
with an explicitly square coefficient matrix, to connect uniqueness and
spanning to column and row pivots. The instructor prefers these matrix
factorizations to indexed sums for the dimension and basis-extension arguments.
The extension and reduction constructions follow with a visible independence
argument using an augmented column matrix to append a vector outside the span.

The remaining-notation audit converts five further proofs to matrix form:
the zero-vector test, removal of a redundant generator, coordinate uniqueness,
coordinate arithmetic, and determination of a linear map by its basis images.
The redundancy proof uses the same augmented-column notation as the extension
proof. Coordinate arithmetic distributes the reconstruction matrix over two
coefficient columns; the map proof carries one coefficient column through the
input vectors, their images, and the output-coordinate columns. The closing
reconstruction formula uses the same notation. Expanded finite combinations
remain in definitions, the coefficient-system bridge, regression, and concrete
polynomial/function examples where they explain individual weights. Bracketed
lists of abstract vectors denote linear-combination maps rather than requiring
an ambient numerical coordinate system. All 20 current exercise sets are
unchanged by this audit; every example remains. The polynomial continuation
described below brings the deck to 81 slides.

The basis-matrix sequence explicitly includes the identity matrix for the
standard basis and the two-step coordinate-to-vector-to-coordinate arrows.
The transition-column rule is explained by feeding in a standard coefficient
column: this selects a matrix column and represents one old basis vector.
The following polynomial example now has two slides: a table derives all
three transition columns, then a continuation derives the input coordinates
by matching coefficients, shows the matrix-product arithmetic, and
reconstructs the original polynomial using the output basis.

A final whole-deck source review found no arithmetic or matrix-direction
errors. Exact symbolic checks cover 14 groups: the opening map and redundant
weights, independence and pivot examples, coordinate and polynomial-basis
exercises, transition matrices, differentiation, both spring models,
regression, and the displayed PCA geometry. Minor clarifications distinguish
one fixed linear combination from the span, define column-list products for
abstract vectors visibly, retain list multiplicity in the counting theorem,
and label the ODE uniqueness result as supplied background. A stale reference
to frames as an earlier topic is corrected. All examples, 20 exercise sets,
81 slides, and existing anchors remain; full browser layout review is still
pending under the local-file access restriction.

Other visible reasons explain the zero-vector test, original pivot columns,
coordinate arithmetic, and why images of a basis determine a map's matrix.
The basis-extraction procedure explicitly stops at row echelon form. Its
proof uses a triangular pivot submatrix and back substitution, so the
justification uses the same form. The procedure and proof omit discussion
of further reduction to keep attention on locating pivots and selecting
original columns.
Mixed prose/math spacing was audited throughout Deck 07. The mixed labels
use explicit TeX word spaces at text/symbol boundaries, including the
basis equivalence, transition label, and input/output basis labels.
Distinct visible statements have explicit line breaks; ordinary source
newlines had joined those statements in the rendered paragraphs. Periods
were not added.
The differentiation example follows that derivation. Regression, PCA, frames,
and infinite bases move to Applications and Extensions after the foundations;
later projection/PCA claims are identified as previews of later geometry.
All previous explicit anchors and content headings are retained, and section
outlines and the Course Map follow the new order. The terminology index's
existing destinations remain valid; no new index term is needed.

The roadmap uses Question / How we will answer it / Concept, with explicit
explanatory steps. The parallelogram slide leads with the same map acting on
the shape and basis vectors. Its SVG canvas is shorter while drawing scale
and geometry are retained; the two diagram headings move into unused space.
The standalone SVG crop and label clearance were inspected in a rendered PNG.
The unique-address slide first asks whether the two pictured directions reach
every vector in R^2 uniquely, identifying that property as a basis. Presenter
notes solve the general target explicitly. A separate continuation keeps the
same target vector from the diagram and asks for two coefficient lists after adding a redundant
generator. This exposes lost uniqueness directly; the span-growth question
and its definition detour are removed. Answers remain in presenter notes,
which distinguish basis coordinates from coefficients in a redundant family.
The continuation concludes that the extra generator is redundant for a coordinate
system: it adds no direction and makes coefficient lists nonunique.

Validation: the complete website and all twelve decks render without warnings.
The assembled course site passes 1,721 local-reference and 750 anchor checks,
including previous/next navigation across all twelve decks.
Automated source and HTML checks verify retention of the 19 original exercise
sets, plus the new
basis question (20 total, with the early redundancy exercise refocused on
the instructor's fixed-vector question), every
original content heading, 62 explicit anchors, all section outlines, all
same-deck links, and 20 distinct incoming course anchors. Visible prose has
no bold emphasis or unnecessary terminal periods; HTML IDs are unique and
`git diff --check` passes. Quarto needed access to its normal user Sass cache.
Browser visual inspection remains pending: the local-file URL was blocked by
browser policy. Rendering and source checks do not establish visible layout.
The instructor subsequently authorized publication with Checkpoint. Remote
deployment and live-page verification of this revision remain pending.

## Anton crosswalk

Verified against Wiley's official contents for *Elementary Linear Algebra:
Applications Version*, 12th edition, ISBN 9781119282365:
[Wiley contents PDF](https://media.wiley.com/product_data/excerpt/65/11192823/1119282365-25.pdf).
The publisher PDF was retrieved and its contents extracted locally.

| Deck | Principal sections | Additional connection |
|---|---|---|
| Vector Spaces, Subspaces, and Span | 4.1 Real Vector Spaces; 4.2 Subspaces; 4.3 Spanning Sets | Finite fields, multivariable polynomials, differential equations, and finite Fourier sums extend the examples |
| Bases, Dimension, and Coordinates | 4.4 Linear Independence; 4.5 Coordinates and Basis; 4.6 Dimension; 4.7 Change of Basis | Elimination-based basis extraction connects to 4.8; complex dimension and isomorphisms preview 5.3 and 8.3 |
| Matrix Spaces and Rank | 4.8 Row Space, Column Space, and Null Space; 4.9 Rank, Nullity, and the Fundamental Matrix Spaces | The closing abstract-map examples preview 8.1 and 8.4 |

The separate Spanning Sets section in the 12th edition shifts later numbering
relative to older editions. Frames and infinite algebraic bases are enrichment;
convergent infinite Fourier expansions preview 6.6. Core ranges agree in deck
metadata/subtitles, the welcome outline, and PLAN.

## Editorial decisions

- Follow-up notation and exercise clarification: use square brackets for
  numerical vector rows/columns, with explicit vertical columns in the
  zero-test set definitions; retain parentheses for points and ordered lists.
  The extra-generator exercises state the representation equation and permit
  zero coefficients. Instructor notes distinguish nonunique coefficient lists
  for dependent generators from unique coordinates in a basis.
- October 8 motivation bridge: open Bases and Coordinates with a section on
  linear combinations as constructions, span as reach, independence as
  coefficient uniqueness, and ordered bases as coordinate systems. Seven
  content slides use a square-to-parallelogram map, redundancy practice,
  differentiation P_3 to P_2 through a coordinate matrix, regression in
  response space, and centered PCA. Keep the formal definitions
  and proofs afterward. The bounded parallelogram is not a subspace; the edge
  vectors form a basis of the full plane. Use the same geometric scale in both
  panels and transform every grid line and point consistently. Regression
  needs full column rank for unique coefficients, while the fitted vector is
  unique even with dependent columns. A retained PCA basis gives coordinates
  of the projection, not an exact representation of every original vector.
  Link back from Vector Spaces and Span and forward to the existing least
  squares and low-rank treatments; leave algorithms and proofs there.
- Keep elimination, its concrete redundancy-removal example, an alternative-
  basis exercise, and the frame preview together in the bases section.
- Show the row operation in the example; retain pivot columns of the original
  matrix. Explain existence from spanning and uniqueness from independence.
- Use a polynomial example for abstract change of basis, rather than repeating
  the earlier Euclidean-vector example. Show transition direction explicitly.
- Define finite dimension, the zero-space dimension, rank, nullity, and
  orthogonal complement before they are needed; state scalar and finite-
  dimensional assumptions for coordinate matrices.
- A follow-up added the missing explicit RREF definition beside echelon form
  in Systems and Matrices. The definition applies to any rectangular matrix;
  its 3-by-4 example has pivots in columns 1 and 3 and nonzero entries in
  nonpivot columns. Gauss–Jordan names the process and RREF the resulting
  form. Later RREF mentions and the cumulative index link to the definition.
- A second follow-up audited every slide for backward references that carry
  needed information. Local reminders repeat particular-solution notation,
  space definitions, closure tests, chosen polynomials and generators,
  basis/coordinate meaning, transition direction, and the exact matrices
  needed in later calculations. Repeated letters no longer leave students
  guessing which exercise matrix is intended.
- Echelon form suffices for pivot-column and row bases. A new continuation
  contrasts it with RREF: normalized identity pivot columns make the nonzero
  rows the coefficient matrix directly in the chosen factorization A=C R.
  The running A and its full reduced matrix appear together at the section
  introduction;
  subsequent steps restate the factors or column-space basis when needed.
- The cumulative-summary follow-up audited all seven developed How Far We
  Have Come slides. The first three already preserve the growing ideas;
  Euclidean Spaces and all three split decks now retain systems and all
  solutions, reusable elimination, composition/inverses/determinants,
  geometry, abstract vectors, spans, bases, and coordinates. The rank closing
  includes left-null compatibility, orthogonal pairs, and x=x_p+N t with
  exactly n-r free parameters. Local author guidance records these threads.
- Two continuation slides prove the rank-factorization recipe: reversible
  row operations preserve every column relation and its coefficients; RREF
  pivot columns are unit columns, so its nonzero-row block supplies the
  coefficients of the original columns in C. State explicitly that C's
  columns and R's rows give column-space and row-space bases. The numeric
  check also interprets R x as the coordinates of A x in C's ordered basis.
- A returning-reader pass replaced fourteen vague lead-ins with brief
  reminders across the three decks. Cues identify constant coefficients,
  the relevant zero vector, membership equations, coordinate entry meanings,
  transition direction, column notation, factor sizes, and input/output bases.
  Existing adequate reminders remain in place; no recap blocks or slides
  were added.
- Connect rank to existence versus uniqueness and left-null vectors to equation
  compatibility. Distinguish a necessary zero test from sufficient closure.
- Use continuous real-valued functions on the whole real line for the
  uncountable Hamel-basis example. Distinguish finite algebraic combinations
  from Hilbert-space series; do not imply an inclusion into square-integrable
  functions on the whole line.
- Preserve old anchors, use Example: headings and unprefixed gold-star prompts,
  and promote main ideas so every instructional section has multiple topics.
- Keep all objects in the tilted-plane diagram under one linear projection;
  retain polynomial-vector versus coordinate-column and four-space overview
  diagrams.

## Rank-factorization notation

R denotes the r-by-n nonzero-row factor in A=C R; the full reduced matrix is
written rref(A)=[R;0]. In the proof, B names a row-equivalent matrix and is
explicitly set to rref(A) when reduction is complete. U remains the upper
triangular factor in PLU.
Independent review checked the proof, dimensions, and exercise answers. The
deck rerendered; all ten changed slides fit at 1280 by 720, and the proof and
coefficient slides also fit at 1600 by 1000, with no typeset-math errors.
Headings and anchors are unchanged; the assembled-site link check passes.
Teal whole-column outlines now mark pivot columns 1 and 3 in the four full
RREF displays and two matching R displays, including the earlier definition
in Systems and Matrices. Full reduced columns are e_1,e_2 in three-space;
the corresponding columns in R form I_2. Independent review confirmed that
all entries are unchanged. Both decks render, all six changed slides fit at
1280 by 720 and 1600 by 1000 without typeset-math errors, and links pass.

## Validation

- Independent mathematical and structural reviews passed. Exact arithmetic
  checked the displayed reductions, bases, rank factorizations, coordinate
  changes, and new exercise answers.
- All eleven decks and the root website render without warnings/errors. The
  final full slide render used an isolated source copy to avoid competing with
  the instructor's live preview; its outputs were used for the final checks.
- All 126 slides across the three decks received rendered visual review with
  typeset equations; content clears the footer. The final tight course-map and
  polynomial-transition layouts were rechecked after revision.
- The three decks now have 47, 47, and 35 slides, 15 instructional sections, 57 main
  topics, and 28 starred exercise containers, all with answer notes.
- All 85 original explicit content anchors survive; 99 are now present.
  Section outlines and Course Maps exactly match the headings.
- The assembled-site traversal checked 1,415 local links/resources and 514
  anchor references across 23 reachable pages/decks; no failures. All eleven
  deck navigation records resolve. Unused copied library fragments are not
  student-facing pages and were excluded from the traversal.
- The backward-reference follow-up rendered all four affected decks and
  visually checked all 51 changed slides, including the new rectangular RREF
  definition and the new echelon/RREF comparison. All typeset mathematics
  fits above the footer at 1280 by 720; standard-size checks and the actual
  cross-deck RREF link also passed. Exact arithmetic reconfirmed the displayed
  reductions, rank factors, and left-null equations. The refreshed assembled
  site checks 1,424 local links/resources and 523 anchors with no failures.
- The cumulative-summary and proof follow-up rendered all four affected
  decks and visually checked all nine changed/new slides with typeset
  equations at 1280 by 720. Content clears the footer at normal font; the
  complete rank summary also passes at 1600 by 1000. Independent review
  confirmed the proof, basis roles, coordinate interpretation, and solution
  conditions. The assembled site now checks 1,442 local links/resources and
  552 anchors across 23 reachable pages/decks, with no failures; all eleven
  navigation records resolve. Anchor retention, source style, section/topic
  counts, and git diff --check pass.
- The returning-reader pass rerendered all eleven decks and the full website
  in the isolated source copy, without errors or warnings. All fourteen
  changed slides passed rendered visual review with typeset mathematics at
  1280 by 720. Headings, anchors, slide breaks, and answer notes are unchanged;
  source style and git diff --check pass. The assembled site again passes
  1,442 local links/resources and 552 anchors, with eleven navigation records.
- The Checkpoint review normalized two remaining Euclidean Spaces headings
  to “Example:”. That deck rerendered successfully; anchors are unchanged,
  and the assembled-site traversal still passes.
- Shared footer text now scales with viewport width and reserves menu-button
  space. All eleven complete footers clear the counter at 1280 by 720;
  additional 1600 by 1000 and 1024 by 768 checks passed. The reusable SCSS and
  guidance were published first in canonical HickernellAcademicLib at
  `98e0701`, then intentionally adopted by this course. Other consumer pins
  remain unchanged.
- The welcome page's expanded outline was reviewed at desktop and phone widths;
  it has no horizontal overflow. New cumulative-index entries were checked.
- October 8 motivation bridge on M3: the updated Vector Spaces and Span,
  Bases and Coordinates, and cumulative-index decks render. The seven new
  content slides, section outline, and updated Course Map pass 27 rendered
  overflow/MathJax checks at 1600 by 1000, 1280 by 800, and 1024 by 768.
  Visible review confirms diagram labels and footer/navigation clearance;
  the PCA and differentiation layouts were refined before the final pass.
  Exact checks cover the transformed point, derivative coordinate matrix,
  regression residual, and synthetic PCA principal directions. All prior
  explicit anchors survive; 210 local anchor references and local image
  assets pass. Cross-deck clicks reach the new bridge and the existing
  transformation, least-squares, and low-rank treatments. Source style and
  git diff --check pass. Instructor review remains; publication is included
  in the October 8 Checkpoint.
- The notation/exercise follow-up rerendered Decks 06 and 07. All 27 changed
  slide sections pass 81 overflow/MathJax checks across the same three viewport
  sizes, with no browser errors. Visible review confirms the explicit-column
  zero tests, revised extra-generator prompts, and PCA coordinate notation;
  210 local anchor references and local image assets still pass.
- October 8 Checkpoint `f03285f` publishes the motivation and notation
  revisions. The isolated full website and twelve-deck renders pass without
  warnings; the assembled site passes 1,703 local references and 695 anchors.
  Publishing and Pages deployment succeeded, and the live bridge was verified.
  Instructor content review remains open.

Companion drafts for Decks 06–08 are constructed and locally validated.
Instructor review of the decks and companions, and later-semester pacing,
remain open.
Local validation does not establish a new live deployment.

## October 15, 2026 — flow, practice, and correctness audit of Decks 05–07

Reviewed the complete source, worked examples, proofs, and presenter answers
in Euclidean Spaces, Vector Spaces and Span, and Bases and Coordinates.
The geometry-to-abstraction-to-coordinates sequence remains coherent; preserve
the existing anchors and recorded classroom stopping points.

| Deck | Rendered slides | Starred exercise sets | Explicit subparts |
|---|---:|---:|---:|
| 05 Euclidean Spaces | 34 | 6 | 19 |
| 06 Vector Spaces and Span | 48 | 12 | 34 |
| 07 Bases and Coordinates | 60 | 14 | 34 |

Counts distinguish a starred set from its subparts; the lead prompt can also
require work. All 32 sets now have presenter-only answer notes. Previous set
counts were 5, 11, and 12. Added targeted practice for points/displacements,
axiom consequences, a concrete homogeneous independence test, and the new
two-point polynomial coordinate example. Do not add exercises merely to meet
a numerical quota: every core section now includes an active check. The
finite/infinite-basis enrichment does not require a separate exercise.

- Deck 05: explain two independent plane directions without presupposing the
  formal definition; qualify the zero-vector direction language; normalize
  numerical vector columns to square brackets. Supply the missing affine-
  elimination answer notes. The first projection and first plane exercise
  are the core practice; the second plane exercise is useful reserve practice.
  Split the title subtitle before the textbook citation to prevent clipping.
- Deck 06: include nonemptiness in the subspace-test takeaway and explicitly
  check the zero matrix in matrix-family proofs. Extend the operations
  example's answer notes to show why ordinary scalar multiplication fails.
  New presenter pacing guidance keeps fields, multivariable polynomials,
  DEs, and Fourier sums as selectable extensions around the polynomial core.
- Deck 07: label the applications opening as a motivation preview. Make the
  regression basis/coordinate claim conditional on independent feature
  columns and leave rank terminology to the later development. The line
  example distinguishes constrained samples from nonunique synthesis weights;
  highlight “quadratic” using the standard alert style. Follow it with an
  exercise whose answers remain in presenter notes.

No erroneous numerical example or worked-answer formula was found. Exact
checks cover affine systems, both projection calculations, cross products,
plane equations/areas, determinant identities, polynomial arithmetic and
membership, DE solution families, differentiation coordinates, regression
residuals, PCA score covariance, independence, basis extraction, coordinate
arithmetic, and transition matrices: 83 symbolic/numerical assertions pass.
Definitions, scalar fields, zero/degenerate cases, finite versus infinite
representations, and exercise solutions were also reviewed directly.

The root website and all twelve decks render. At 1050 by 700, DOM geometry checks cover all 142
slides in the three audited decks with no MathJax errors or content-slide
overflow. Title-card container bounds require text-range/visible inspection;
Deck 05's long subtitle was the actual clipping issue and was split locally.
Source checks find no bold prose or unnecessary visible terminal periods;
HTML source comments and presenter notes are excluded. All three title text
bounds and the four new exercises pass final visible/layout review. All
section outlines and original explicit anchors survive; 759 local deck
links/anchors pass in the assembled site. When checking actual slide positions,
allow the shared 350 ms horizontal-to-section-top reset to settle before
descending; verify the active heading rather than counting navigation attempts.
These are local checks; instructor review and publication remain separate.
