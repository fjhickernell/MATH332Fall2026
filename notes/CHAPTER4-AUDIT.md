# General Vector Spaces deck audit

Completed October 3, 2026 on M5. This records editorial decisions and
verification; the mathematical exposition remains authoritative in the slides.
The audit revisions are included in the October 3 Checkpoint; its new remote
deployment remains unverified.

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

- Keep elimination, its concrete redundancy-removal example, an alternative-
  basis exercise, and the frame preview together in the bases section.
- Show the row operation in the example; retain pivot columns of the original
  matrix. Explain existence from spanning and uniqueness from independence.
- Use a polynomial example for abstract change of basis, rather than repeating
  the earlier Euclidean-vector example. Show transition direction explicitly.
- Define finite dimension, the zero-space dimension, rank, nullity, and
  orthogonal complement before they are needed; state scalar and finite-
  dimensional assumptions for coordinate matrices.
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
- The three decks have 47, 47, and 32 slides, 15 instructional sections, 57 main
  topics, and 28 starred exercise containers, all with answer notes.
- All 85 original explicit content anchors survive; 96 are now present.
  Section outlines and Course Maps exactly match the headings.
- The assembled-site traversal checked 1,415 local links/resources and 514
  anchor references across 23 reachable pages/decks; no failures. All eleven
  deck navigation records resolve. Unused copied library fragments are not
  student-facing pages and were excluded from the traversal.
- Shared footer text now scales with viewport width and reserves menu-button
  space. All eleven complete footers clear the counter at 1280 by 720;
  additional 1600 by 1000 and 1024 by 768 checks passed. The reusable SCSS and
  guidance were published first in canonical HickernellAcademicLib at
  `98e0701`, then intentionally adopted by this course. Other consumer pins
  remain unchanged.
- The welcome page's expanded outline was reviewed at desktop and phone widths;
  it has no horizontal overflow. New cumulative-index entries were checked.

Instructor review, companion notebooks, and later-semester pacing remain open.
Local validation does not establish a new live deployment.
