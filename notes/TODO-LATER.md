# Todo Later

This file tracks deferred work and lower-priority tasks that should remain
visible without crowding the active project plan or status. Entries should
state why the work was deferred when that context will matter later.

## Deferred work

- When developing Deck 06, revisit Wronskians after function spaces and linear
  independence have been established. Deck 04 now contains the introductory
  determinant example and the distinction between Wronskians and Jacobians.
- Save the general orthogonal-projection formula for the treatment of column
  spaces, orthogonal complements, and least-squares regression rather than
  expanding Deck 03's concrete transformation examples. For a real matrix
  $\mat{A}$ with linearly independent columns,
  $\mat{P}=\mat{A}(\mat{A}^{\mathsf T}\mat{A})^{-1}\mat{A}^{\mathsf T}$
  projects onto $\operatorname{col}(\mat{A})$, and $\mat{I}-\mat{P}$ projects
  onto $\operatorname{col}(\mat{A})^\perp=\ker(\mat{A}^{\mathsf T})$, the
  vectors perpendicular to every column of $\mat{A}$. Derive this from the
  normal equations and identify $\mat{P}\vct{b}$ as the fitted vector and
  $(\mat{I}-\mat{P})\vct{b}$ as the residual. Reconnect to Deck 03's plane
  projection as the one-column case $\mat{A}=\vct{u}$ of $\mat{I}-\mat{P}$.
  The inverse formula requires full column rank. For arbitrary rank, the
  projector is $\mat{A}\mat{A}^{\dagger}$ using the Moore--Penrose
  pseudoinverse, once that concept is introduced.
- When developing Deck 06, introduce Strang's
  $\mat{A}=\mat{C}\mat{R}$ rank factorization after students have learned
  vector spaces, subspaces, span, linear independence, basis and coordinates,
  column and row spaces, RREF pivot columns, and rank. Construct $\mat{C}$
  from the pivot columns of the original matrix and $\mat{R}$ from the
  corresponding coordinate coefficients, conveniently obtained as the
  nonzero rows of $\operatorname{rref}(\mat{A})$. Use the topic to reconnect
  Deck 01's row operations with Deck 03's factorization viewpoint. During the
  Deck 03 review, consider only a brief forward signpost; do not move the full
  treatment there before its space, basis, and rank prerequisites.
- Before the next offering, rethink the role and sequencing of Deck 00. In the
  first Fall 2026 lecture, its abstract overview was too much to absorb before
  students had encountered concrete linear systems. Only part of the deck was
  presented before moving to Deck 01, with the intention of returning to Deck
  00 later. Consider beginning with concrete material from Deck 01 and
  revisiting the motivating ideas in Deck 00 after students have examples to
  anchor them.
- Review the abstract roadmap and closing of `# The course ahead`.
- Decide whether slides such as `Return to the opening` communicate anything
  useful or merely repeat earlier material.
- Consider replacing the rhetorical recap with a concrete transition to the
  first substantive topic, likely solving linear systems.
- Preserve the existing logistics slides unless a concrete error is found;
  they are substantially complete.
- Reconsider the reusable CSS candidates only when a second MATH 332 deck
  actually needs them.

Lecture 00 is largely complete, but its final conceptual closing has not yet
been approved.
