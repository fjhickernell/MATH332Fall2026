# MATH 332 Fall 2026 Project Plan

## Purpose and design principles

Build a coherent, reproducible Quarto course for **MATH 332 — Linear Algebra:
Theory and Applications**. The most recent MATH 332 repository is
authoritative. The most recent MATH 565 repository is a separate active course
repository whose proven architecture may be consulted read-only during MATH
332 work. Older course repositories are read-only historical references, and
`classlib` is a pinned shared dependency.

Anton provides the course spine.

Strang provides conceptual insight and geometric perspective.

Python provides visualization, computation, and experimentation.

The recurring course motif is:

> Algebra reveals geometry. Geometry explains algebra.

The RevealJS decks are the authoritative course presentation materials.
Mathematical content must be maintained only in the slides.

## 1. Repository and deployment

Maintain an independent Git repository with a root Quarto website and a
separate RevealJS subproject in `slides/`. Render both projects, stage slide
output under `_site/slides`, and publish the assembled site to `gh-pages`.
Reuse pinned shared infrastructure from `classlib`.

## 2. Syllabus and policies

Finalize course logistics, prerequisites, learning outcomes, assessment
policies, accessibility information, and institutional policies. Leave
unknown details explicitly marked TBD rather than inventing them.

## 3. Semester schedule

Build the Fall 2026 meeting calendar and then assign chapter pacing,
assignments, quizzes, reviews, and tests only after dates are confirmed.

## 4. Authoritative RevealJS decks

Develop Deck 00 as the course teaser and roadmap, then number the remaining
decks sequentially by teaching order rather than by Anton chapter. Display the
corresponding Anton chapter and section coverage separately in each deck's
metadata and title-slide subtitle. This keeps the deck number aligned with the
student's course sequence while retaining Anton as the course spine.

The planned sequence is:

| Deck | Teaching arc | Principal Anton coverage |
|---|---|---|
| 00 | Why Linear Algebra? | Course overview |
| 01 | Systems and Matrices | Sections 1.1–1.3 and selected Section 1.10 applications |
| 02 | Inverses and Invertibility | Sections 1.4–1.6 and selected Sections 1.10–1.11 applications |
| 03 | Matrix Structure and Transformations | Sections 1.7–1.9 |
| 04 | Determinants | Chapter 2 |
| 05 | Euclidean Vector Spaces | Chapter 3 |
| 06 | General Vector Spaces | Chapter 4 |
| 07 | Eigenvalues and Eigenvectors | Chapter 5 |
| 08 | Inner Product Spaces | Chapter 6 |

Applications should be woven into the theory and methodology they motivate or
illuminate rather than collected as a terminal addendum. In particular, use
the existing circuit model within systems and elimination; consider Leontief
input-output models as a motivating or culminating inverse application;
connect chemical balancing to homogeneous systems and free variables; connect
polynomial interpolation to unique solvability; and develop reflections,
rotations, projections, and compositions as the concrete substance of matrix
transformations.

Each deck must work as an in-class presentation and as a resource students
revisit afterward. Use metadata-driven titles, clear major sections,
previous/next deck navigation, and shared classlib styling.

## 5. Lecture slide development

Apply the MATH565Fall2026 slide conventions incrementally: title-slide
structure, course maps where useful, section overview slides, consistent
notation, accessible visuals, and complete render-and-inspection validation.
Preserve enough explanation for independent reading without duplicating the
mathematics elsewhere.

## 6. Python demonstrations

Develop small demonstrations using NumPy, SciPy, Matplotlib, and SymPy. Keep
notebook notation self-contained because Quarto and RevealJS LaTeX macros do
not automatically propagate into Jupyter.

## 7. Assignments and quizzes

Create homework that reinforces theory and computation. Determine the Canvas
quiz strategy before publishing quiz dates or links.

## 8. Tests

Develop test coverage, review materials, dates, and administration details
without inventing unresolved information.

## 9. Reusable classlib opportunities

Identify genuinely reusable website, slide, or teaching infrastructure only
after it has recurred and been validated locally. Make any such change in
HickernellAcademicLib, commit and push it upstream first, and only then update
the course repository's `classlib` pointer. Course-specific content remains
here.
