# MATH 332 Fall 2026 Construction Status

The RevealJS decks are the authoritative course presentation materials.
Mathematical content should be maintained only in the slides.

## Ordered checklist

1. [x] Create the repository skeleton and achieve a successful website and
   seven-deck render.
2. [ ] Finalize course information, syllabus, and policies.
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
- [ ] Develop the authoritative Decks 05–08 for Anton Chapters 3–6.
  - [x] Draft Deck 05: Euclidean Vector Spaces, covering Anton §§3.1–3.5
    as a focused bridge from points and displacement vectors to homogeneous
    directions, affine solution sets, and general vector spaces, with compact
    projection and cross-product connections.
  - [ ] Complete instructor-led content and visible-layout review of Deck 05.
  - [x] Draft Deck 06: General Vector Spaces, covering Anton §§4.1–4.9 from
    vector-space axioms and abstract examples through subspaces, span,
    independence, bases, coordinates, dimension, change of basis, the four
    matrix spaces, rank–nullity, and rank factorization.
  - [ ] Complete instructor-led content and visible-layout review of Deck 06.
  - [ ] Develop Decks 07–08.
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
  area scaling, and a brief differential-geometry outlook.
- [x] Clarify the surface parameterization and area factor without assuming
  cross products have been introduced; render the revised deck.
- [x] Add cumulative "How Far We Have Come" slides to developed Decks 02–06
  between Big Ideas and What Comes Next, with one Course Map link for each
  closing sequence; defer Decks 07–08 until their content is developed.
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
  - [x] Release Test 1 grades, post the all-sections Canvas announcement, and
    publish the worked-answer PDF with its anonymous score distribution on the
    course site and in the test archive.
  - [x] Schedule Quiz 2 for October 1 on Determinants and Euclidean Vector Spaces.
  - [x] Save and verify Quiz 2's unpublished On Paper Canvas assignment.
  - [ ] Confirm Quiz 2's remaining Canvas settings before publication.
  - [x] Schedule Test 2 for October 29 in PH 109; create and publish its
    On Paper Canvas assignment for 12:45 PM; add the date to the
    course website sources; and post the all-sections announcement. Coverage
    remains TBD.
  - [x] State that the final-examination date will be posted when scheduled by
    the Registrar and that the cumulative examination will emphasize material
    not covered by Test 1 or Test 2.
  - [x] Announce and add to the course website the remaining quiz dates—Quiz 3
    on October 15, Quiz 4 on November 12, and Quiz 5 on December 1—with
    coverage TBD.
- [ ] Validate navigation, links, notation, accessibility, and visible layout
  as content is added.
- [ ] Promote only validated, genuinely reusable infrastructure to classlib.
