# Technical Notes

This file records repository architecture, implementation notes, maintenance
knowledge, and technical context useful to future maintainers and agents. Keep
details here when they are durable but too specific for `AGENTS.md`.

## Repository notes

### Deck 05 projection figure: implementation and validation

The worked nearest-point example in
`slides/05-euclidean-vector-spaces.qmd#nearest-point-worked-example` is the
course reference for an equation-and-geometry slide. Follow the shared
`classlib/docs/revealjs-diagram-construction.md` guide; these notes describe
this figure's implementation.

- Keep the inline SVG inside a fenced `{=html}` block. This preserves SVG
  text and `tspan` subscripts without Markdown interpreting the asterisks as
  emphasis and breaking the figure's element nesting.
- The course stylesheet defaults SVG text to Arial. The scoped
  `.affine-projection-geometry .math-label` rule in
  `slides/math332-slides.scss` selects Times New Roman/Times/serif for
  mathematical labels, including mathematical spans within prose captions.
  A `font-family` SVG attribute alone does not override the stylesheet.
- Use bold italic lowercase symbols for vectors, regular-weight italic
  uppercase symbols for points, and regular-weight italic scalars. Keep
  coordinates upright. Use `tspan` with `baseline-shift="sub"` for the
  nearest-point and minimizing-parameter subscripts. Plain SVG text does not
  automatically inherit the LaTeX vector macros or MathJax typography.
  Keep square roots and similar constructions in the adjacent MathJax
  calculation unless the SVG explicitly draws the full mathematical glyph;
  a plain Unicode radical does not extend its bar over the radicand.
- At this figure's 580-by-450 viewBox, the displacement and projection stems
  use widths 8 and 9; arrowheads use 26-by-26 markers with a 24-by-24 path,
  `markerUnits="userSpaceOnUse"`, and the reference point at the arrow tip.
  The dashed perpendicular uses width 6. Keep the underlying affine line
  thinner, and retain the right-angle marker and labeled points.
- The drawing is a view in the plane containing the line and the external
  point, not a plot of the first two coordinates. Preserve perpendicularity
  and relative segment lengths when changing the example. Update the
  equations, diagram labels, geometry, accessibility description, and speaker
  notes together.
- Keep the 47% / 6% / 47% equation-and-figure layout. Compact transposed-row
  coordinate displays leave room for the concluding key point above the footer.
- Render Deck 05, refresh the assembled `_site/slides/` output, and inspect
  the complete slide in the browser at ordinary presentation size. Check
  serif/bold styling, arrowheads, labels, and footer clearance. Inspect the
  rendered HTML to confirm that every label remains inside the SVG; a valid
  source SVG or successful render alone cannot establish this. A standalone
  SVG preview is useful but does not include the course stylesheet.

### Lecture 00 handoff — 2026-08-07

- `slides/00-why-linear-algebra.qmd` is largely complete. Its opening now
  establishes scalar, vector, matrix, and tensor representations, then makes
  matrix action explicit. The main examples cover images, regression,
  transformations, composition, systems and least squares, networks and
  repeated action, and machine learning.
- `# Compute responsibly` now distinguishes ill-posedness, ill-conditioning,
  numerical instability, and computational cost. Its cancellation example is
  an executable NumPy/Jupyter cell whose values are rendered as a table.
- The MATH 565-style logistics material in `# The course ahead` has been
  adapted to MATH 332 and is substantially complete: the website links,
  Schedule route to slides, and the currently documented website/Canvas
  division are present. Unresolved submission and quiz procedures remain
  identified as unconfirmed rather than invented.
- The deck currently has **30 slides**. The latest Lecture 00 render completed
  successfully on 2026-08-07; revised slides were visually checked for
  overflow, section navigation was verified, and the new relative course-page
  links were checked against generated site pages.
- The remaining Lecture 00 issue is only the conceptual wrap-up surrounding
  the logistics slides. The final abstract roadmap and closing have not yet
  been approved; do not describe the whole final section as unfinished.

### Lecture 01 first substantive draft — 2026-08-11

- `slides/01-systems-and-matrices.qmd` contains 27 slides. It begins with
  equations and concrete solution sets, motivates elementary row operations by
  reversibility, and performs elimination on equations before introducing
  matrices.
- A single three-variable system recurs through equation elimination, row-dot-
  product interpretation, augmented-matrix notation, echelon form, and RREF.
  Variants of its last row motivate inconsistency and free variables before the
  general zero/one/infinitely-many classification is stated.
- The closing computation slide plans a small SymPy companion notebook using
  `Matrix` and the `qmcpy` kernel. Elementary matrices and nonsingularity are
  only previewed near the end.
- The deck, root website, and all seven decks rendered successfully on
  2026-08-11. The recurring example and free-variable parametrization were
  checked with SymPy, and assembled-site navigation was verified.
- Live browser inspection was unavailable during drafting. Before treating the
  deck as classroom-ready, inspect every slide at the standard RevealJS
  viewport and fix overflow, spacing, pacing, or density issues.

### Chapter 1 deck transition — 2026-08-19

- The dated Lecture 01 notes above describe the first draft, not the current
  deck. `slides/01-systems-and-matrices.qmd` now has 48 slides and carries the
  arc from equation operations through augmented-matrix elimination, pivots,
  solution sets, a resistance circuit, and finally grouped elimination
  matrices, built from elementary matrices, as an algebraic representation of
  reversible row operations.
- `slides/02-inverses-and-invertibility.qmd` has 29 slides. It restricts the
  inverse discussion to square matrices, develops inverse algebra and
  Gauss–Jordan computation, and treats Leontief production and Gaussian
  covariance/precision as conceptual applications rather than derivations to
  memorize.
- The cumulative glossary in Deck 00 links each term to its first substantial
  treatment. Application-specific terms introduced in Deck 02, including
  covariance and precision matrices, belong in that index as they are added.
- The root site and all nine decks rendered successfully on 2026-08-19. The
  revised Decks 00–02 course maps, Deck 01 elimination and Big Ideas slides,
  and Deck 02 framing, applications, and Big Ideas slides were visually
  checked at the standard RevealJS viewport.

### WileyPLUS integration — 2026-09-04

- On September 16, enabled `Wiley Course Resources` in Canvas navigation and
  verified that it opens the paired Anton course with the eTextbook launch and
  Practice tab. Its durable Canvas External Tool URL is recorded as
  `canvas.wiley_resources` in `course-metadata.yml`; use this Canvas route rather
  than a transient Wiley session URL. The published Welcome page links directly
  to it, including the first bold required-access statement. The course-wide
  access announcement is Canvas discussion `105776`.
- Use Illinois Tech's admin-installed, course-paired `Wiley LTI 1.3`
  integration and the `Wiley Assignments` External Tool in Canvas. Do not
  install the legacy App Center `WileyPLUS (new)` entry or use its Consumer
  Key/Shared Secret form.
- Do not store integration codes, keys, secrets, or transient LTI launch and
  deep-link URLs in the repository. The durable Canvas assignment URL may be
  recorded in `course-metadata.yml` for linking and duplicate prevention.
- WileyPLUS stores and enforces the instructor-approved question selection,
  deadline, and attempt/scoring settings. Canvas provides the persistent course
  launch, publication state, and grade destination. The Canvas point total must
  match the WileyPLUS question-set total, and its **Due** and **Until** fields
  remain blank for WileyPLUS assignments.
