# Todo Later

This file tracks deferred work and lower-priority tasks that should remain
visible without crowding the active project plan or status. Entries should
state why the work was deferred when that context will matter later.

## Deferred work

- Revisit the placement and motivation of projections, vector spaces, and
  coordinates during the Decks 05--06 review; the instructor raised these
  questions again on September 16, 2026. Keep the placement open rather than
  treating the existing deferred plan as a final decision. Consider naming
  $\operatorname{Null}(\mat{A})=\{\vct{x}:\mat{A}\vct{x}=\vct{0}\}$
  early, using closure under linear combinations to motivate a vector space,
  then extracting independent directions by elimination. Introduce a basis
  as enough directions to describe every solution uniquely, and coordinates
  as the coefficients in that description. Define the vector space through
  its operations and closure before describing it by a chosen basis;
  coordinates represent its vectors rather than define the space itself.
- Revisit what certifies a projection matrix in Deck 03's concrete examples
  versus the later vector-space treatment. For a real square matrix,
  $\mat{P}^2=\mat{P}$ characterizes a linear projection onto its image along
  its kernel; adding $\mat{P}^{\mathsf T}=\mat{P}$ characterizes an
  orthogonal projection. Explain geometrically that projected vectors stay
  fixed and discarded components go to zero; idempotence alone allows
  oblique projections. Consider a short early recognition criterion, with
  the general column-space formula and proof later, once subspaces and
  orthogonal complements are established. Use
  $\mat{P}\mat{A}=\mat{A}$ and
  $\mat{A}^{\mathsf T}(\mat{I}-\mat{P})=\mat{0}$ to show respectively
  what is preserved and why the residual is orthogonal. The existing
  full-column-rank and least-squares plan below remains the starting point
  for this placement discussion.

- When reviewing Decks 05--06, use infinite solution sets of linear systems to
  motivate why bases and coordinates matter. Deck 05 already establishes the
  geometric picture
  $\{\vct{x}:\mat{A}\vct{x}=\vct{b}\}=\vct{x}_p+\operatorname{Null}(\mat{A})$:
  depending on the number of free variables, a consistent solution set may be
  an affine line, plane, or higher-dimensional affine subspace (reserve
  *hyperplane* for the codimension-one case). After its free-variable or
  elimination example, ask how to name the independent directions and locate
  a particular solution within this set. Deck 06 can answer by choosing a
  basis $(\vct{b}_1,\ldots,\vct{b}_k)$ for
  $\operatorname{Null}(\mat{A})$ and writing
  $\vct{x}=\vct{x}_p+c_1\vct{b}_1+\cdots+c_k\vct{b}_k$. The direction vectors
  need not be the standard $\vct{e}_i$; they are adapted to the solution
  geometry, and $(c_1,\ldots,c_k)$ gives affine coordinates relative to the
  chosen base point and direction basis. Consider a brief reprise of the Deck
  05 example near Deck 06's introduction of bases and coordinates, before the
  polynomial-coordinate example, so the formal definitions answer a question
  students have already encountered geometrically.
- Much later, decide whether MATH 332 should introduce tensors beyond Deck
  04's brief surface-area outlook and, if so, determine their scope, purpose,
  and placement in a companion notebook, later deck, or future-course note.
- When revisiting Deck 06, decide whether to add Wronskians now that function
  spaces and linear independence have been established. Define the general $n\times n$
  Wronskian using derivatives through order $n-1$; distinguish the always-valid
  implication “nonzero at one point implies linear independence” from the
  converse, which fails for arbitrary differentiable functions but holds for
  solutions of the same homogeneous $n$th-order linear ODE under the usual
  continuity hypotheses. Deck 04 contains the introductory $2\times2$ example
  and the distinction between Wronskians and Jacobians. Once the Deck 06
  Wronskian slide exists, update Deck 04's metadata-based deck link to its
  specific slide anchor.
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
