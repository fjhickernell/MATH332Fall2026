# Decisions

This file records important course, repository, and design decisions together
with the rationale behind them. Add entries when future maintainers or agents
would benefit from understanding why a choice was made.

## Decision log

### 2026-09-04 — Route the mutable tutoring schedule through Canvas

- **Decision:** The public course website tells enrolled students that Fall
  2026 Math Tutoring Center support is available in RE 129 and online, then
  routes them to Canvas. The Canvas Welcome page links directly to the faculty
  coordinator's original Google Drive PDF; do not upload or copy the PDF into
  Canvas or the course repository.
- **Rationale:** The coordinator may revise the schedule in place, and the PDF
  contains an online-tutoring Zoom link with its passcode. Referencing the
  original file preserves updates, while keeping its URL off the public course
  website reduces public discovery.
- **Consequences:** Do not add the Google Drive or Zoom URL to public course
  sources or metadata. Canvas authentication limits casual public exposure but
  cannot prevent students from forwarding an anyone-with-the-link file. The
  coordinator should restrict the Drive file to the intended Illinois Tech
  audience, and the Zoom meeting should use appropriate authentication or a
  waiting room, when feasible.

### 2026-09-02 — Keep WileyPLUS deadlines out of Canvas

- **Decision:** For WileyPLUS External Tool assignments, set and revise the
  deadline only in WileyPLUS. Leave the Canvas **Due** and **Until** fields
  blank rather than duplicating the deadline there.
- **Rationale:** WileyPLUS continued to show Assignment 1's original Friday
  deadline after its Canvas deadline was changed and complained that Canvas
  also had a deadline. The instructor corrected the WileyPLUS deadline
  manually.
- **Consequences:** Assignment 1 is due Monday, September 7, 2026, at 11:59 PM
  Chicago Time in WileyPLUS. For future WileyPLUS assignments and deadline
  changes, WileyPLUS is authoritative; the course pages, schedule, and deck
  notice echo its deadline, while Canvas retains the launch, points, and grade
  passback without its own deadline.

### 2026-09-02 — Keep SciPy PLU implementation in the companion notebook

- **Decision:** Keep Deck 03's live PLU sequence mathematical: derive
  $\mat{A}=\mat{P}\mat{L}\mat{U}$, explain compact rectangular factors, and
  finish with permutation, forward substitution, and back substitution for
  repeated solves. Put SciPy APIs, packed storage, pivot-index bookkeeping,
  and executable solves in the Lecture 03 companion notebook.
- **Rationale:** The mathematical derivation is useful in class, but six
  implementation slides after the triangular-solve conclusion interrupt the
  lecture arc. The notebook is a better place to inspect code, run actual
  solves, and check residuals.
- **Consequences:** Deck 03 links to the notebook from its final PLU slide and
  contains no SciPy code slides. The notebook must retain factor verification,
  explicit forward and back solves, factor-once/solve-many examples, packed
  $\mat{L}$/$\mat{U}$ storage with pivot history, residual checks, and compact
  rectangular factors. Continue to omit pivot-selection algorithms, stability
  analysis, and operation counts from this introductory treatment.

### 2026-08-25 — Make every assignment individual

- **Decision:** Require individual work and submission for every MATH 332
  assignment. Do not configure a Canvas group assignment or create a student
  group set, and do not offer a pair-submission option. This supersedes the
  earlier plan to retain pairs for file-upload assignments.
- **Rationale:** The instructor pivoted to one simple, consistent submission
  policy for the course. All planned homework is delivered through WileyPLUS,
  which grades and records work separately for each student.
- **Consequences:** The Assignments page states the course-wide individual-work
  rule and contains no alternate group or file-upload policy. Future Canvas
  assignments and announcements must use individual-submission language.

### 2026-08-24 — Prefer WileyPLUS autograding over exact textbook exercise numbers

- **Decision:** Use an individual WileyPLUS External Tool assignment when
  automatic grading is required, even when that requires replacing assigned
  Anton exercise numbers with comparable Wiley questions. The accompanying
  file-upload pair option was superseded by the August 25 decision to make
  every assignment individual.
- **Rationale:** Wiley's paired question bank did not contain Anton Exercises
  1.3.15 or 1.2.38, and Canvas prohibits group assignments from using External
  Tools. WileyPLUS provides per-student automatic grading and Canvas grade
  passback.
- **Consequences:** Assignment 1 uses four randomized Wiley questions covering
  Gaussian elimination, matrix dimensions, matrix multiplication by columns,
  and a matrix-product equation. It is individual, worth 20 points, and retains
  its original Canvas URL. Its original September 4 deadline was extended on
  September 2 to Monday, September 7, 2026, at 11:59 PM Chicago Time. For each
  future assignment, preview the live WileyPLUS questions, keep print exercise
  references distinct from WileyPLUS identifiers, and give the instructor a
  concise crosswalk for approval before substituting a question.

### 2026-08-24 — Index elimination matrices by pivot-column stage

- **Decision:** Use $\mat{M}_j$ for the grouped elimination matrix that clears
  column $j$ below row $j$, rather than for one elementary row operation. Keep
  individual one-row-operation matrices conceptually distinct as elementary
  matrices. In the no-row-exchange case, index the nontrivial elimination
  stages through $q=\min(m-1,n)$ for an $m\times n$ matrix.
- **Rationale:** The index $j$ then identifies the pivot column and the number
  of grouped stages is determined by the matrix dimensions. The bound requires
  special care for tall matrices: when $m>n$, the last coefficient column may
  still need an $\mat{M}_n$ stage.
- **Consequences:** Use $\mat{U}=\mat{M}_q\cdots\mat{M}_1\mat{A}$ and
  $\mat{L}=\mat{M}_1^{-1}\cdots\mat{M}_q^{-1}$ when no row exchanges are
  needed. Use a single $\mat{G}$ for the complete product of row-operation
  matrices in Gauss–Jordan reduction; do not introduce indexed Gauss–Jordan
  stage matrices unless a later algorithm genuinely needs them. Use
  $\mat{P}_{jk}$ only when naming the elementary permutation matrix that
  exchanges rows $j$ and $k$, and reserve $\mat{P}$ for the accumulated
  permutation in PLU.

### 2026-08-20 — Use SciPy's permutation convention for PLU

- **Decision:** Introduce triangular factorization briefly in Deck 02 and
  develop it in Deck 03 using
  $\mat{A}=\mat{P}\mat{L}\mat{U}$, equivalently
  $\mat{P}^{\mathsf T}\mat{A}=\mat{L}\mat{U}$. Thus
  $\mat{P}^{\mathsf T}$ places the rows in elimination order and $\mat{P}$
  restores the original order. State without proof that, when elimination
  proceeds without row exchanges, the inverse elimination matrices multiply
  to a unit lower-triangular matrix.
- **Rationale:** This is the convention returned by `scipy.linalg.lu`, so
  students will recognize the decomposition in later computational work.
  PLU also connects Deck 01's row operations and Deck 02's inverse algebra to
  Deck 03's triangular structure and composition of transformations without
  turning the course into numerical linear algebra.
- **Consequences:** Keep pivot-selection strategies, stability analysis, and
  operation counts out of the introductory treatment. The September 2
  decision above refines the former blanket exclusion of storage details.
  Do not assume a general permutation matrix equals its transpose; only a
  single row-exchange matrix is necessarily symmetric. Begin with the square,
  no-exchange LU example. For rectangular
  $\mat{A}\in\reals^{m\times n}$, state SciPy's compact factor shapes using
  $k=\min(m,n)$ and distinguish them once from the full elimination-product
  factors.

### 2026-08-19 — Number decks by teaching sequence and split Anton Chapter 1

- **Decision:** Number the authoritative course decks sequentially by teaching
  order rather than matching deck numbers to Anton chapter numbers. Retain
  Deck 00 as the course overview; use Decks 01–03 for the three Chapter 1
  teaching arcs; and renumber the current Chapter 2–6 placeholders as Decks
  04–08. Display Anton chapter and section coverage separately in deck
  metadata and title-slide subtitles.
- **Rationale:** A deck is a coherent teaching unit, whereas an Anton chapter
  may contain several substantial conceptual arcs. Chapter 1 already divides
  naturally into systems and matrices, inverses and invertibility, and matrix
  structure and transformations. Sequential deck numbers communicate the
  student's presentation order without implying a false one-deck-per-chapter
  correspondence.
- **Consequences:** The planned sequence is Deck 01: Systems and Matrices;
  Deck 02: Inverses and Invertibility; Deck 03: Matrix Structure and
  Transformations; and Decks 04–08 for Anton Chapters 2–6. Applications are
  to be woven into the theory or methods they motivate rather than placed in a
  separate end-of-chapter addendum. Implementing the decision requires adding
  Decks 02 and 03, renumbering the existing placeholder decks, and updating
  deck metadata, navigation, schedule entries, course maps, and internal
  links. No deck renumbering or creation was part of this documentation
  decision itself.

### 2026-08-07 — Keep Lecture 00 diagram styles local

- **Decision:** Keep `slides/00-why-linear-algebra.css` local to Lecture 00.
- **Rationale:** The completed CSS audit found possible reusable MATH 332
  components—`diagram-label`, `diagram-flow`, `diagram-node`,
  `diagram-arrow`, and `diagram-image`—but no demonstrated second use yet.
- **Consequences:** Wait until a second MATH 332 deck actually needs a
  component before creating a course-wide stylesheet. Consider promotion to
  `classlib` only after demonstrated cross-course reuse. Constructions
  specific to Lecture 00 remain local.
