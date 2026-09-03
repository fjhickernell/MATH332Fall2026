# Next task

## Current task

Explore tensors and decide whether a concise tensor treatment belongs in the
current MATH 332 sequence, where it would fit, and what mathematical and
computational purpose it would serve.

## Current state

- Decks 00--04 are substantive; Decks 01--03 are instructor-reviewed, and
  Deck 04 has been developed and audited. Decks 05--08 remain placeholders for
  Anton Chapters 3--6.
- The instructor reports successful end-to-end clean-Colab validation of all
  four published Deck 00--03 companion notebooks using the recorded
  `classlib` commit, without downgrading QMCPy. All four also execute locally
  with the `qmcpy` kernel.
- Deck 03 retains the mathematical PLU derivation and repeated-solve
  conclusion. Its companion notebook retains the detailed SciPy factor,
  solve, packed-storage, pivot, residual, and rectangular-factor sequence.
  The wide and tall examples now print the actual $\mat{A}$, $\mat{P}$,
  $\mat{L}$, and $\mat{U}$ matrices as well as their shapes.
- Deck 03 now states that a first dense solve costs $O(n^3)$ operations and
  each new right-hand side costs $O(n^2)$ when saved PLU factors are reused.
  The companion notebook measures both paths for
  $n=64,128,256,512,1024,2048,4096,8192,16384$ and displays a timing table
  and log--log plot. On the M3 clean-kernel validation run, the $n=16384$
  fresh solve took 5.996 seconds versus 0.203 seconds with saved PLU, a
  29.5-fold speedup. The full notebook executes without errors, and Deck 03
  renders cleanly outside the filesystem sandbox.
- Assignment 1 is the individual 20-point WileyPLUS assignment, due September
  7 at 11:59 PM Chicago Time. Quiz 1 is scheduled for September 10 and covers
  Decks 01--02. Test 1 is scheduled for September 17 and covers Decks 01--03.

## Questions to resolve

- What tensor concepts should MATH 332 introduce, and should they appear in a
  current deck, a companion notebook, a later deck, or a future-course note?
- Should Deck 03 briefly signpost Strang's later
  $\mat{A}=\mat{C}\mat{R}$ rank factorization, or should that remain deferred
  until vector spaces, bases, row and column spaces, RREF pivot columns, and
  rank have been established?

## Constraints

- Keep mathematical exposition authoritative in the RevealJS decks and use
  companion notebooks for executable detail and experimentation.
- Preserve SciPy's convention
  $\mat{A}=\mat{P}\mat{L}\mat{U}$, equivalently
  $\mat{P}^{\mathsf T}\mat{A}=\mat{L}\mat{U}$.
- Keep SciPy APIs, packed factors, pivot indices, executable solves, residual
  checks, and timing experiments in the companion notebook rather than
  restoring them to the live deck.
- Do not pin or downgrade to QMCPy 1.6.1; support the current QMCPy interface.
- Use Anton as the course spine and preserve the established MATH 332
  notation, deck sequence, application integration, and shared `classlib`
  conventions.

## Done when

- The instructor has decided the intended scope, purpose, and placement of
  tensors in MATH 332.
- The decision is recorded in the appropriate durable project file; any
  approved student-facing addition is implemented, rendered, and inspected,
  or the idea is explicitly deferred.
