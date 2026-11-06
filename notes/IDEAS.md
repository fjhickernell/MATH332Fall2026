# Ideas

This file collects brainstorming, future enhancements, and teaching ideas
worth preserving for later consideration. Entries are exploratory rather than
commitments and should include enough context to remain useful over time.

## Ideas to explore

### Matrix Spaces: movie ratings and the PageRank distinction

- Add a Netflix-style movie-ratings example to the row- and column-space
  applications in Matrix Spaces and Rank (Deck 08), as Fred suggested
  November 6. Begin with a small synthetic user-by-movie matrix: rows are
  users' rating profiles across movies, and columns are movies' rating
  patterns across users. Explain their spans, then explore how shared
  low-dimensional structure could help predict a user's rating for a movie
  they have not watched or rated. Make the assumptions for estimating missing
  entries explicit; missing ratings are not zero ratings, and the space
  definitions alone do not determine them. Keep this tied to the current
  matrix-space examples; placement and development remain for instructor
  review. No new slide has been added for this idea.
- Fred also asked whether this relates to Google PageRank and whether
  PageRank is outdated. Keep the applications distinct when teaching:
  movie ratings suggest user/movie profile spaces and prediction of missing
  entries, while PageRank uses a web-link transition matrix and a stationary
  eigenvector. The shared connection is large matrices; the mathematical
  questions differ. PageRank is a natural later connection to eigenvalues,
  iteration, and networks rather than the main missing-ratings example.
- Google’s [ranking-systems guide](https://developers.google.com/search/docs/appearance/ranking-systems-guide#link-analysis-systems-and-pagerank),
  checked November 6, 2026, says PageRank has evolved and remains part of its
  core ranking systems. Present it as a continuing mathematical application,
  without implying that it alone describes modern Google Search.

### Other teaching ideas

- Replace the synthetic low-rank landscape in Deck 00 with a recognizable,
  properly licensed photograph if classroom testing shows that a familiar
  image would make the SVD teaser more compelling. Preserve a reproducible
  low-rank sequence and visible source attribution.
- Develop an optional companion demonstration for Deck 00 only after the
  slides have been classroom-tested. The strongest candidates are an
  adjustable least-squares projection, an image-rank slider, and a tiny
  PageRank iteration; interaction should earn its setup time rather than
  duplicate the complete story already told by the slides.
- Consider adding presenter notes with suggested prompts, likely student
  responses, and optional cuts for a 45-minute class after the first live use.
