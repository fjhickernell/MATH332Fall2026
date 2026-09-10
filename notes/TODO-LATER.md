# Todo Later

This file tracks deferred work and lower-priority tasks that should remain
visible without crowding the active project plan or status. Entries should
state why the work was deferred when that context will matter later.

## Deferred work

- Develop optional enrichment on matrices involving functions, prompted by a
  student's question (September 10, 2026). The instructor requested that the
  ideas be preserved for later; slides have not yet been authorized or drafted.
  Ask the student for an example of what he encountered to distinguish
  Wronskians, Jacobians, and possible differential-geometry interests.
  Proposed scope: four or five optional slides at the end of Deck 04, then
  revisit Wronskians with function spaces in Deck 06. Keep the sequence tied
  to familiar determinants, homogeneous systems, and geometric scaling:
  - Begin with a matrix-valued function
    $A(t)=\begin{bmatrix}1&t\\t&1\end{bmatrix}$, whose determinant is
    $1-t^2$. At each fixed parameter this is an ordinary numerical matrix;
    invertibility fails precisely at $t=\pm1$.
  - Introduce the Wronskian using $\cos t$ and $\sin t$: the matrix of
    their values and first derivatives has determinant $1$. Explain the
    independence argument: a constant-coefficient relation holding for every
    $t$, together with its derivative, gives a homogeneous system; an
    invertible matrix at one point forces both constants to vanish.
    Emphasize constant coefficients and distinguish independence of functions
    on an interval from independence of numerical columns at a point.
    A nonzero Wronskian at one point proves function independence; a zero
    Wronskian does not generally prove dependence without extra hypotheses.
    Reference: https://onlinehw.math.ksu.edu/math340book/chap2/theoryrev.php
  - Introduce the Jacobian through
    $F(p+h)\approx F(p)+J_F(p)h$: its columns describe transformed small
    displacement vectors, and its determinant gives local signed volume
    scaling. Reconnect explicitly to Deck 04's scale, orientation, and
    collapse interpretation.
  - Use polar coordinates $F(r,\theta)=(r\cos\theta,r\sin\theta)$:
    $J_F=\begin{bmatrix}\cos\theta&-r\sin\theta\\
    \sin\theta&r\cos\theta\end{bmatrix}$ and $\det J_F=r$.
    Illustrate a small coordinate rectangle mapping approximately to a
    parallelogram of area $r\,\Delta r\,\Delta\theta$ for $r>0$;
    connect this to the polar integration factor. Include a geometric picture.
    Reference: https://math.mit.edu/~poonen/notes02.pdf
  - Explicitly distinguish the purposes: Wronskians test constant-coefficient
    relations among functions; Jacobians describe how a map transforms nearby
    displacements. Both involve derivatives, but their columns mean different
    things.
  - Offer a brief differential-geometry outlook: derivatives of a surface
    parametrization give tangent vectors; linear algebra measures their
    lengths, angles, and spanned area. Keep manifolds and tensors as an
    outlook unless the student's example and instructor's scope decision
    justify more depth.
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
