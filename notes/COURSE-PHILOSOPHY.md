# Course Philosophy

This file preserves long-term teaching philosophy, course goals, and recurring
design principles. Use it for durable pedagogical guidance that informs course
development without serving as student-facing course content.

## Guiding principles

- Take a computational mindset throughout the course: compute only what the
  problem requires. Unnecessary work wastes time and creates additional
  opportunities for floating-point round-off error to accumulate or
  propagate. Prefer direct solves to explicit matrix inverses when the goal is
  only to solve for one or a few right-hand sides, and reuse elimination
  structure or a factorization when many right-hand sides share the same
  coefficient matrix.
- Use applications to develop high-level interpretation and computational
  judgment. Unless a derivation is explicitly assigned, students should not
  need to memorize application-specific derivations; they should understand
  what the quantities represent, what the linear-algebra operation does, and
  why the chosen computation is appropriate.
- Use forward-looking applications from statistics, computer science, AI, and
  data science as accessible previews when they help students recognize where
  linear algebra will reappear. Do not assume the later subject as a
  prerequisite; plant an interpretation students can reconnect with when they
  study the application more fully.

## Roles of linear algebra references

- Anton, Rorres, and Kaul's *Elementary Linear Algebra: Applications Version*
  provides the chapter sequence and primary student reading. Course pacing and
  assigned reading should follow its 12th edition unless an intentional course
  decision says otherwise.
- Strang's books and MIT OpenCourseWare materials supply geometric intuition,
  motivation, and selected examples. They enrich Anton's sequence rather than
  replacing it.
- Boyd and Vandenberghe connect vectors, matrices, least squares, data, and
  computation, making their text a particularly useful bridge to applications
  for computer science students.
- Trefethen--Bau and Golub--Van Loan are instructor references for numerical
  stability, conditioning, matrix factorizations, and computational issues;
  they do not set the level or sequence of the student-facing course.
- Axler is an instructor reference for conceptual structure and proof-level
  insight, not the primary course sequence.
- Hastie--Tibshirani--Friedman and Goodfellow--Bengio--Courville provide
  motivating machine-learning and computer-science examples. Those examples
  should illuminate linear algebra topics without allowing the application
  texts to define the syllabus.
