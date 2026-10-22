# MATH 332 Fall 2026 Construction Status

The RevealJS decks are the authoritative course presentation materials.
Mathematical content should be maintained only in the slides.

## Ordered checklist

1. [x] Create the repository skeleton and achieve a successful website and
   seven-deck render.
2. [ ] Finalize course information, syllabus, and policies.
   - [x] Record the 20-point homework and quiz policies, drop one lowest score
     in each category, protect the 10-point Diagnostic Survey from dropping,
     and save unpublished Canvas placeholders for Assignments 4–6
     (October 9, 2026).
   - [x] Add a detailed instructor statement describing how ChatGPT and Codex
     support course preparation, verification, and maintenance, and link to it
     from an abbreviated early slide in Deck 00.
3. [x] Draft the semester schedule without inventing unresolved dates.
   - [x] Audit all nine August 18–September 15 instructional recordings,
     reconcile actual schedule coverage, and save the September 22 continuation
     after the assessment-only September 17 meeting.
4. [x] Develop Deck 00: Why Linear Algebra? as the teaser and roadmap.
5. [x] Develop and revise Deck 01: Systems and Matrices in
   `slides/01-systems-and-matrices.qmd`.
6. [x] Decide and document the sequential Deck 00–08 architecture, including
   the three-deck Chapter 1 teaching sequence and application integration.
7. [x] Develop and validate the first Python demonstration.
8. [x] Construct and execute the Lecture 01 companion notebook draft.
9. [x] Review and finalize the Lecture 01 companion notebook.
10. [x] Implement the sequential Deck 00–08 architecture: create Decks 02 and
    03, renumber the current Chapter 2–6 placeholders as Decks 04–08, and
    update all metadata, navigation, schedule, course-map, and internal links.
11. [x] Draft Deck 02: Inverses and Invertibility.
12. [x] Review and refine Deck 02 for classroom use.
13. [x] Draft Deck 03: Matrix Structure and Transformations.
14. [x] Review and refine Deck 03 with the instructor for classroom use.
15. [x] Decide and document the paper quiz and test strategy, including the
    Canvas gradebook workflow for manually entered scores.
16. [x] Clarify that quiz and test application problems provide the linear
    system unless deriving it is explicitly assigned.
17. [x] Add a tridiagonal finite-difference ODE boundary-value application to
    Deck 03.
18. [x] Develop and audit Deck 04: Determinants.

## Later course construction

- [x] Give every deck, including placeholders, a Course Map with consistent
  38% course-deck, 4% gutter, and 58% deck-content proportions, and emphasize
  the current deck with the established larger-link treatment.
- [x] Add the Teaser Trailer theme to Deck 00 and the explicit equations,
  augmented-matrix, triangular-matrix, and solution sequence to Deck 01.
- [x] Add the inverse-solution equation as the Course Map theme for Deck 02.
- [x] Add geometric actions, PLU triangular solves, and basis images to the
  Deck 03 Course Map theme, and a volume-scaling theme to Deck 04.
- [x] Add a starred Householder involution exercise and derive the plane
  projection matrix in Deck 03, including its connection to Householder reflection.
- [ ] Develop the authoritative Decks 05–10 for Anton Chapters 3–6.
  - [x] Draft Deck 05: Euclidean Vector Spaces, covering Anton §§3.1–3.5
    as a focused bridge from points and displacement vectors to homogeneous
    directions, affine solution sets, and general vector spaces, with compact
    projection and cross-product connections.
  - [x] Clarify linear combinations, affine solution sets, and affine dimension;
    add projection and cross-product examples, starred exercises, an illustrated
    projection with nonunit parameter, and the cross-product area derivation.
  - [x] Link callbacks and previews across Decks 01–06 and organize Deck 05's
    supporting examples and derivations as continuation slides.
  - [x] Complete instructor-led content and visible-layout review of Deck 05
    (confirmed by the instructor October 4).
  - [x] Draft Deck 06: General Vector Spaces, covering Anton §§4.1–4.9 from
    vector-space axioms and abstract examples through subspaces, span,
    independence, bases, coordinates, dimension, change of basis, the four
    matrix spaces, rank–nullity, and rank factorization.
  - [x] Divide the General Vector Spaces draft into Vector Spaces, Subspaces,
    and Span; Bases, Dimension, and Coordinates; and Matrix Spaces and Rank,
    with section outlines, closing summaries, and updated course navigation.
  - [x] Audit the three decks against Anton's 12th Applications edition;
    repair definitions and assumptions, balance main headings, make basis
    extraction explicit, add conceptual examples and starred exercises,
    and verify every rendered slide and website/navigation consistency.
    Verification and scope are recorded in `notes/CHAPTER4-AUDIT.md`.
  - [ ] Complete instructor-led content and visible-layout review of these
    three Chapter 4 decks.
  - [x] Add an opening motivation bridge in Bases and Coordinates connecting
    linear combinations, span, independence, bases, and coordinates through
    transformed grids, polynomial differentiation by a coordinate matrix,
    regression, and PCA; link it from Vector Spaces and Span.
  - [x] Expand General Vector Spaces with worked-example and starred-practice
    pairs for multivariable polynomials, concrete spans, matrix bases,
    dimension, coordinate arithmetic, orthogonality, and matrix representations
    of linear maps; keep exercise solutions in presenter notes.
  - [x] Add the high school line example to Bases and Coordinates: slope and
    intercept versus two sampled values, the constraint on a third point,
    and nonunique coefficients with redundant linear generators.
  - [x] Audit Decks 05–07 for flow, starred practice, and correctness; fill
    practice/answer-note gaps and clarify assumptions and preview pacing.
    Current audit and exercise counts are in `notes/CHAPTER4-AUDIT.md`.
  - [x] Refine Deck 07's action table and pivot-column example, add three
    starred exercises with answer notes, connect transformations to input
    and output coordinates, and consolidate the Course Map to seven entries.
  - [x] Add Deck 07's undamped initial-data solution map with real and
    complex bases as a worked example; use the critically damped car-spring
    model and its coordinate matrices for starred practice.
  - [x] Expose and highlight both oscillator coordinate-change matrices,
    reinforce Deck 07's main distinctions, and audit the intro terminology
    index against all twelve decks (191 linked entries on ten pages).
  - [x] Reorganize Deck 07 around its motivating questions and proof
    dependencies; justify the dimension equivalence, basis-size comparison,
    pivot-column method, and coordinate/matrix rules while retaining all
    examples and 19 original exercise sets (October 21).
  - [ ] Review Deck 07's revised 82-slide flow and remaining visible layouts;
    the local render and source/link checks pass; opening table review is complete.
  - [x] Review the opening concept table with the instructor; show expanded
    sums and matrix products for combinations and independence, and verify
    column widths and the key point's clearance above the footer.
  - [x] Audit Deck 07's remaining finite-dimensional arguments for matrix
    notation; convert five general proofs and the closing reconstruction
    formula while preserving every example and all 20 current exercise sets.
  - [x] Pin the bundled MathJax runtime and verify Safari rendering through
    reloads and slide/section navigation without a CDN dependency.
  - [ ] Develop Deck 09.
  - [x] Draft Deck 10 with QR, regression, and Fourier approximation.
- [x] Renumber the split Chapter 4 decks as 06–08 and the later placeholders
  as 09–10; update metadata, course maps, navigation, links, and author guidance.
- [x] Create and locally validate the three Deck 06–08 companions on spans,
  bases and coordinates, and matrix spaces and rank; add their deck and
  Notebooks-page links.
- [ ] Review the Deck 06–08 companion notebooks with the instructor.
- [x] Create the initial Notebooks page for demonstrations and exercises.
- [x] Create and locally validate companion notebooks for Decks 02 and 03.
- [x] Create and locally validate the Deck 04 determinants companion, including
  signed-area plots, exact row operations, PLU, eigenvalue products, and
  determinant scaling and logarithmic computation; add deck and notebook-page links.
- [x] Clarify PLU determinant signs, swap counts, and permutation cycles in
  Deck 04 and its companion; split the worked example from the general formula
  to keep the slides readable.
- [x] Prove the two-dimensional determinant-area formula in Deck 04 using
  base times perpendicular height, including the zero-edge case and orientation.
- [x] Add the optional Deck 04 matrices-of-functions enrichment: a
  parameter-dependent determinant, Wronskians, Jacobians, polar-coordinate
  area scaling, spherical-coordinate volume scaling with a determinant
  derivation, and a brief differential-geometry outlook.
- [x] Clarify the surface parameterization and area factor without assuming
  cross products have been introduced; render the revised deck.
- [x] Add cumulative "How Far We Have Come" slides to developed Decks 02–08
  between Big Ideas and What Comes Next, with one Course Map link for each
  closing sequence; Decks 10–11 now include it, while Deck 09 remains deferred
  until its content is developed.
- [x] Audit all nine developed How Far recaps for sufficient explanation and
  readable one-page layout: include augmented matrices and solution-preserving
  elimination, state formula conditions, and connect geometry, bases, rank,
  projection, and least squares; distinguish the Special Topics core from
  optional extensions. Retain ordinary type size and verify renders and links.
- [x] Link each deck's first pivot mention and relevant closing reminders to
  the original Systems and Matrices definition; make its rectangular and
  augmented-matrix scope explicit and distinguish zero candidates from pivots.
- [ ] Verify the revised surface slide layout and MathJax typesetting in Safari.
- [x] Add the Deck 04 companion’s Colab badge using the established setup;
  separate clean-Colab validation is not required by instructor policy.
- [ ] Review the Deck 04 companion with the instructor.
- [x] Create and locally execute the Deck 05 companion on point coordinates,
  homogeneous and affine solutions, projection, and displacement geometry;
  link it from the deck and Notebooks page.
- [ ] Review the Deck 05 companion with the instructor.
- [x] Validate all four published Deck 00--03 companion notebooks end to end
  in clean Google Colab runtimes using the recorded `classlib` commit without
  downgrading QMCPy.
- [x] Complete the Deck 03 companion's PLU sequence with printed factors for
  the rectangular examples and measured $O(n^3)$ fresh-solve versus $O(n^2)$
  saved-factor timing through $n=16384$.
- [x] Add student repository-access instructions.
- [x] Create Assignment 1 for Anton §§1.2–1.3; publish it in Canvas for
  20 points; convert it to an individual, automatically graded WileyPLUS
  assignment when the original textbook exercises proved unavailable; and
  add its course-page, schedule, and Deck 01 title-slide notice.
- [x] Publish the Assignment 1 website updates.
- [x] Prepare Assignment 2's four-question, 20-point WileyPLUS draft and
  unpublished Canvas launch, with September 25 deadline and course notices.
- [x] Deploy Assignment 2's course pages, verify live links, enable WileyPLUS,
  publish Canvas, and post the all-sections announcement (`105900`); verify
  the assignment and WileyPLUS launch in Canvas Student View.
- [x] Prepare Assignment 4's instructor-approved five-question, 20-point
  website draft, Schedule/Assignments links, and Deck 07 reminder; render and
  inspect the affected content. Deadline: October 23 at 11:59 PM Chicago time.
- [x] Save/link Assignment 4 in WileyPLUS and the existing unpublished Canvas
  shell; verify 20 points, selected questions/policies, unavailable WileyPLUS
  state, new-tab launch, and blank saved Canvas Due/Until fields.
- [x] Verify Fred’s All Sections Assignment 4 announcement (`107874`), posted
  October 12; corrected link spacing is present.
- [x] Deploy and verify Assignment 4 website links; with instructor approval,
  enable WileyPLUS and publish Canvas 106680. Published settings and the
  20-point Student View launch are verified October 12. Announcement `107874`
  is already posted; actual graded-submission passback remains untested.
- [x] Prepare Assignment 3's five-question, 20-point WileyPLUS set, unpublished
  Canvas launch, October 9 deadline, course pages, and Deck 05 title notice.
- [x] Deploy Assignment 3's pages, enable WileyPLUS, publish Canvas item
  `105825`, and post all-sections announcement `106960`; verify the saved
  settings, live links, and Canvas Student View launch button.
- [x] Reconcile the Canvas description and announcement with the individual
  WileyPLUS workflow.
- [x] Document the minimal-input assignment workflow, the textbook-to-WileyPLUS
  crosswalk, the Canvas/LTI publication sequence, and end-to-end verification.
- [x] Make the required WileyPLUS access, course-wide individual-assignment
  policy, and included online textbook explicit on the course homepage,
  Resources page, and Assignments page.
- [x] Save and publish the matching required-resource statement on the live
  Canvas Welcome page.
- [x] Enable Wiley Course Resources in Canvas navigation, verify the Anton
  textbook and Practice resources, and add its direct Canvas launch link to
  the published Canvas Welcome page and the website Welcome and Resources sources.
- [x] Publish the course-wide Canvas announcement explaining the new WileyPLUS
  textbook and study-resource link (September 16, 2026).
- [x] Add a public-safe Math Tutoring Center notice to the Resources page and
  link the coordinator-maintained live schedule from the Canvas Welcome page.
- [x] Schedule Quiz 1 for the last 15 minutes of class on September 10,
  covering Decks 01--02; create the combined Quizzes and Tests page, add the
  schedule and Deck 02 notices, and save the unpublished 20-point Canvas
  on-paper assignment for manual grade entry.
- [x] Add the read-only `HickernellTestArchive` submodule and expose archived
  MATH 476, MATH 563, and MATH 565 assessments as examples of the
  instructor's question style, with a warning that they are not MATH 332
  practice tests.
- [ ] Create assignments, quizzes, tests, and review materials.
  - [x] Reserve Assignment 3–6 due dates on October 9, October 23,
    November 6, and November 20 with details pending.
  - [x] Release Test 1 grades, post the all-sections Canvas announcement, and
    publish the worked-answer PDF with its anonymous score distribution on the
    course site and in the test archive.
  - [x] Schedule Quiz 2 for October 1 on Determinants and Euclidean Vector Spaces.
  - [x] Clarify Quiz 2 coverage through projections, excluding cross products,
    and post all-sections Canvas announcement `106481`.
  - [x] Publish and verify Quiz 2's On Paper Canvas assignment on September 30; grades remain for later entry.
  - [x] Prepare the private Quiz 2 source for administration.
  - [x] Release Quiz 2 grades, publish the answer PDF with anonymous scores,
    and announce the posted scores to all sections (October 9, 2026).
  - [x] Finalize Quiz 3 coverage as Euclidean Vector Spaces and Vector Spaces,
    Subspaces, and Span; update the assessment page, schedule, and Deck 06 notice.
  - [x] Publish and verify the Quiz 3 coverage announcement (`107573`) to all Canvas sections.
  - [x] Release Quiz 3 grades, publish identical answer PDFs with the anonymous
    distribution in the course and archive, verify live deployment, and post
    the all-sections Canvas announcement (October 22, 2026).
  - [x] Publish and verify Quizzes 3–5 for their announced October 15,
    November 12, and December 1 dates; Quiz 4 and Quiz 5 coverage remains TBD. Both tests are
    published. Grades remain for later entry.
  - [x] Schedule Test 2 for October 29 in PH 109; create and publish its
    On Paper Canvas assignment for 12:45 PM; add the date to the
    course website sources; and post the all-sections save-the-date announcement.
  - [x] Finalize Test 2 coverage as Determinants through Matrix Spaces and Rank
    (Decks 04–08, inclusive); update both website tables and the Deck 08 notice.
  - [x] Publish and verify the All Sections Test 2 coverage announcement
    (`107870`), October 12, 2026.
  - [x] Reduce Test 2 coverage to Determinants through Bases, Dimension, and
    Coordinates (Decks 04–07), excluding Matrix Spaces and Rank, October 15.
    Update both website tables, move the test notice to Deck 07, and correct
    announcement `107870` with a student notification. Local renders pass;
    live deployment verification remains pending.
  - [x] Include the validated Test 2 coverage website update in the October 12
    teaching Checkpoint; remote deployment remains unverified.
  - [x] State that the final-examination date will be posted when scheduled by
    the Registrar and that the cumulative examination will emphasize material
    not covered by Test 1 or Test 2.
  - [x] Announce and add to the course website the remaining quiz dates—Quiz 3
    on October 15, Quiz 4 on November 12, and Quiz 5 on December 1—with
    coverage TBD.
- [ ] Validate navigation, links, notation, accessibility, and visible layout
  as content is added.
- [ ] Promote only validated, genuinely reusable infrastructure to classlib.

## Special Topics capstone

- [x] Draft Deck 11 with SVD and regression as priorities, quadratic forms,
  FFT, tensor products, and optional network/eigenvector applications.
- [ ] Complete instructor content and visible-layout review of Deck 11.
- [x] Draft QR, least squares, and Fourier prerequisites in Deck 10.
- [ ] Complete instructor content and visible-layout review of Deck 10.
- [ ] Build and validate the selected Special Topics demonstrations.
