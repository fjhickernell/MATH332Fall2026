# MATH 332 Fall 2026 Project Plan

## Purpose and design principles

Build a coherent, reproducible Quarto course for **MATH 332 — Linear Algebra:
Theory and Applications**. MATH332Fall2026 is authoritative;
MATH565Fall2026 is the read-only architectural reference; and `classlib` is a
pinned shared dependency.

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

Develop Deck 00 as the course teaser and roadmap, then develop one deck for
each Anton chapter from 1 through 6. Each deck must work as an in-class
presentation and as a resource students revisit afterward. Use
metadata-driven titles, clear major sections, previous/next deck navigation,
and shared classlib styling.

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
