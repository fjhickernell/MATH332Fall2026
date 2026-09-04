# AGENTS.md

At the beginning of every new Codex session, reconstruct the project state
from the repository. Read `README.md`, `PLAN.md`, `STATUS.md`,
`AUTHOR_WORKFLOW.md`, and then `AGENTS.md`; inspect Git status, submodule
status, and recent commits before substantial work.

## Repository shorthand

Within the current teaching workspace:

- `332` refers to the most recent MATH 332 course repository.
- `565` refers to the most recent MATH 565 course repository.

If older course repositories are also open in the workspace, refer to them
explicitly by year (e.g., `565-2025` or `MATH565Fall2025`) to avoid ambiguity.

## Repository boundaries

- The most recent MATH 332 repository is the active, authoritative repository
  for this course.
- The most recent MATH 565 repository is a separate active course repository.
  During MATH 332 work, use it as an architectural reference without modifying
  it unless the task explicitly includes MATH 565.
- Older course repositories are read-only historical references. In
  particular, `MATH565Fall2025` is not the active MATH 565 repository.
- MATH 332 course content stays in this repository.
- Reusable tooling belongs in HickernellAcademicLib only after validation and
  an upstream commit.
- Do not modify reference repositories unless explicitly instructed.
- Initialize the recorded `classlib` commit recursively; do not update it to a
  moving branch tip during routine setup or validation.

## Shared guidance

This repository uses `classlib` as a shared submodule. The authority chain is:

1. Global operational workflow in `SharedConfigs/codex/AGENTS.md`
2. Shared teaching, presentation, and infrastructure guidance in
   `classlib/AGENTS.md`
3. MATH 332 additions and exceptions in this repository

Before creating or substantially revising slides, webpages, reusable
components, shared styling, or notebook presentation, read
`classlib/AGENTS.md`. Local documentation should record only course-specific
policies, terminology, notation, navigation, validation requirements, and
intentional exceptions. Do not duplicate universal style guidance locally.

Before substantial slide work, also read
`classlib/docs/slide-style.md`; before substantial webpage work, read
`classlib/docs/webpage-style.md`. MATH 332 currently has no separate local
style guides, so record a new local guide only when the course develops a
genuine addition or explicit exception.

If local guidance conflicts with shared guidance, follow an explicitly
documented local exception and flag any apparent accidental inconsistency.

## Institutional memory

The `notes/` directory is this repository's institutional memory. Agents
should consult its files when planning work, proposing changes, drafting or
revising course materials, or making architectural decisions.

These files document design intent, rationale, deferred ideas, and
implementation knowledge. Detailed institutional memory belongs there rather
than in this concise `AGENTS.md` file.

The files under `notes/` are not student-facing course content and must not be
treated as source material for lectures, slides, notebooks, assignments,
exams, or the course website.

Content from `notes/` should appear in student-facing materials only after it
has been intentionally incorporated into those materials or when the user
explicitly requests it.

## Resuming work

At the beginning of a work session, read `notes/NEXT.md` before proposing or
making changes. Treat it as the current handoff and starting point, not as
authorization to perform the task without the user's request.

At every checkpoint, update `notes/NEXT.md` with the single most likely next
task, its current state, unresolved decisions, constraints, and completion
criteria. Keep longer-term and non-immediate work in `notes/TODO-LATER.md`.

### Next-task shorthand

Interpret `Next?` as a request to read and summarize `notes/NEXT.md` from both
active repositories, `MATH332Fall2026` and `MATH565Fall2026`. Interpret
`Next 332?` and `Next 565?` as requests for only the named course. Read the
files each time rather than relying on conversation memory. Reporting a next
task does not authorize beginning it.

### Assignment request shorthand

When the user asks to create, set up, or materially revise an assignment,
including a minimal “here is an assignment” request, treat it as authorization
to carry out the complete
[`AUTHOR_WORKFLOW.md`](AUTHOR_WORKFLOW.md#adding-or-updating-an-assignment)
assignment workflow unless the user explicitly limits its scope. A minimal
request may identify textbook exercises, but do not assume those identifiers
refer to the same questions in WileyPLUS. Inspect and preview the live paired
WileyPLUS bank, keep the textbook references and WileyPLUS identifiers distinct,
and prepare a concise crosswalk when anything is unavailable or materially
different. Never make a substitution without the instructor's approval.

Apply the MATH 332 standing defaults: individual WileyPLUS External Tool work,
not configured as a Canvas group assignment, an 11:59 PM America/Chicago
deadline stored only in WileyPLUS, and blank Canvas **Due** and **Until**
fields. Do not infer points, question
weights, randomization, or attempt and scoring policies from an earlier
assignment; verify them for the current WileyPLUS set.

Complete all authorized discovery, local work, validation, duplicate checks,
and draft preparation before pausing. If a question mismatch remains, present
one completed comparison and ask one bundled content question. Remind the user
when the exact `Checkpoint` command is needed to deploy the website. After the
public links are verified, summarize the prepared WileyPLUS set, Canvas launch,
and announcement and request one combined publication confirmation. Once
confirmed, finish the sequence without asking again unless Canvas or WileyPLUS
reveals a material conflict. Resume interrupted work from the latest verified
repository, Canvas, and WileyPLUS state and do not create duplicates. After
final external verification and tracked handoff updates, request one closeout
`Checkpoint` when needed to preserve the completed state; do not treat it as
another publication confirmation.

### Dashboard reconciliation at Checkpoint

As part of every Checkpoint, read `notes/NEXT.md` from both active teaching
repositories and minimally reconcile their entries in the authoritative
`GitTracked/Check-In-Dashboard.md`. Follow `GitTracked/AGENTS.md` and all
Dashboard editing, status, completion, synchronization, and timestamp rules.

- Ensure the current next task for MATH 332 and MATH 565 appears under the
  matching Teaching project and the dot status required by the Dashboard.
- Remove completed course-task bullets from those two Teaching projects when
  completion is established by the work being checkpointed.
- Preserve the `T2. MATH 332` and `T1. MATH 565` project headings and IDs.
- Do not change, move, reorder, rewrite, or remove any other Dashboard item.

## Slides

The RevealJS decks in `slides/` are the authoritative course presentation
materials. Mathematical content must be maintained only in its corresponding
deck.

Follow `classlib/AGENTS.md` and the classlib-based RevealJS architecture proven
in MATH565Fall2026: shared options and styling, metadata-driven deck titles,
title-slide conventions, major-section organization, and previous/next deck
navigation.

Jupyter notebook LaTeX macros cannot be assumed to propagate from Quarto or
RevealJS, so notebooks should use self-contained notation when necessary.

## Validation

Render the root website and the independent `slides/` project. Stage slide
output beneath `_site/slides` for an assembled-site check. Review every
warning or error, verify all nine decks and their navigation, and keep
generated files out of Git.

## Git and checkpoints

Do not commit or push unless the user's message begins with the exact word
`Checkpoint`. A message beginning with `Checkpoint` authorizes the validation,
staging, commit, and push workflow described by the applicable global
instructions. Ordinary work must remain uncommitted and unpushed.

<!-- classlib-consumer-contract:start -->
## Shared classlib guidance

This repository consumes `classlib` as a pinned submodule. Initialize the
recorded submodule commit before substantive work; do not replace it with a
moving branch tip during routine setup or validation.

Before substantive work involving shared teaching, presentation, webpage,
content, component, or infrastructure conventions, read
`classlib/AGENTS.md`. Guidance applies in this order:

1. applicable global instructions;
2. shared guidance in the pinned `classlib/AGENTS.md`;
3. explicit consumer-local instructions and exceptions.

Keep universal guidance in `classlib` rather than copying it locally. Record a
genuine local exception explicitly, including its scope and reason. Flag an
apparent accidental conflict for review instead of silently resolving it.
<!-- classlib-consumer-contract:end -->
