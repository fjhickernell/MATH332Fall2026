# Todo Later

This file tracks deferred work and lower-priority tasks that should remain
visible without crowding the active project plan or status. Entries should
state why the work was deferred when that context will matter later.

## Deferred work

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
