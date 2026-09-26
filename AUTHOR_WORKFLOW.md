# MATH 332 Quarto Website — Author Workflow

The `main` branch contains source files only. GitHub Actions renders the
website and the independent slide project, stages the slide output under
`_site/slides`, and publishes the combined output to `gh-pages`.

## Repository structure

- `index.qmd` — landing page
- `pages/*.qmd` — course logistics and student-facing pages
- `pages/_metadata.yml` — shared classlib article layout for every course page
- `slides/*.qmd` — authoritative RevealJS course decks
- `notebooks/` — Python demonstrations and exercises
- `assets/` — course-specific images and data
- `classlib/` — shared styling, metadata, pages, and teaching infrastructure

Put mathematical exposition in the corresponding RevealJS deck so that course
content is maintained only once.

## Adding or updating an assignment

### Dates before assignment details

When due dates are set before assignment content, add numbered, unlinked
`Details TBD` entries to the course Schedule. The schedule entry reserves the
date; it does not create or publish an assignment. Plan to publish the complete
course website and Canvas/WileyPLUS assignment one week before each due date,
adapting the dates each semester. Track that publication date on the Check-In
Dashboard under this course, and move its reminder to Urgent one calendar day
before publication while keeping the source task. Announce each assignment to
all sections when its details and live links are published. Do not post
separate announcements merely to announce tentative due dates. Replace each
placeholder with the assignment-detail link during the full workflow below.

Use this workflow whenever the instructor asks to create, set up, or materially
revise an assignment, including a minimal “here is an assignment” request. A
minimal request normally needs only the assignment number, desired coverage or
textbook exercises, and due date. A textbook exercise reference is an intake
source, not a final WileyPLUS selection until the corresponding live question
has been found and previewed.

Unless the instructor says otherwise, ordinary MATH 332 homework uses these
standing defaults:

- `Assignment N` as the Canvas title and
  `Assignment N: WileyPLUS — Topic` as the descriptive course-page title;
- individual, automatically graded work in a WileyPLUS External Tool launched
  from Canvas, with no student group set and not configured as a Canvas group
  assignment;
- a deadline of 11:59 PM America/Chicago on the stated date, set only in
  WileyPLUS while the Canvas **Due** and **Until** fields remain blank;
- a course-hosted detail page as the authoritative assignment description, with
  a short Canvas launch instruction linking to that page and the course
  Assignments page; and
- a course-wide Canvas announcement after publication that links to the live
  course pages and does not repeat details that could later diverge.

The WileyPLUS question selection, total and per-question points, randomization,
attempt policy, score reduction, and best-score behavior are not standing
defaults. Establish them from the live WileyPLUS assignment and the
instructor's intent each time; do not silently reuse Assignment 1's 20 points
or three-attempt policy.

At intake, give the instructor one compact checklist covering the textbook-to-
WileyPLUS crosswalk, WileyPLUS question set and policies, Canvas External Tool
launch, assignment page, Assignments table, Schedule, deck reminder, rendering
and deployment, announcement, and final verification. Identify supplied facts,
standing defaults, and only the unresolved decisions that materially change
the result. Complete discovery and every safe local or draft step first. Ask at
most one bundled question after discovery when a content mismatch or another
decision cannot be resolved safely.

### Reconciling textbook and WileyPLUS questions

Use the Illinois Tech paired `Wiley LTI 1.3` integration through Canvas and its
`Wiley Assignments` tool. Do not install the legacy App Center
`WileyPLUS (new)` entry or use a Consumer Key/Shared Secret form.

1. Record the instructor's textbook edition, exercise number or requested
   coverage, and the mathematical purpose of each requested problem.
2. Search the paired WileyPLUS question bank and preview the complete candidate
   question, including every subpart. Treat a printed exercise number and a
   WileyPLUS question identifier as different identifiers until the preview
   confirms that their statements and purpose match.
3. If a requested exercise is missing or materially different, prepare one
   compact crosswalk showing the source reference and intended concept, the
   available WileyPLUS identifier and concept, the relevant difference, and a
   proposed substitute and point allocation. The standing course decision
   favors a comparable WileyPLUS question that preserves the learning objective
   and automatic grading, but never substitute it without instructor approval.
   If the printed statement is not otherwise available, preview the WileyPLUS
   candidates first and include any request for a photo or short description of
   the printed problem in the same bundled content question.
4. Finalize the student-facing assignment only from the approved, previewed
   WileyPLUS questions. List the actual WileyPLUS identifiers and coverage on
   the course detail page; do not label a substituted question with the print
   exercise number it replaced or copy full proprietary question text.

If every requested exercise is an exact usable match, continue without a
content-decision pause. If there is a mismatch, present the completed crosswalk
and request one instructor decision before finalizing the question set.

### Publication sequence

The workflow has two publication gates after any required content decision:

1. After local validation, request the exact `Checkpoint` command if the
   instructor has not already issued it. The public website must be deployed
   and verified before Canvas publication.
2. After the public links are live and the WileyPLUS and Canvas changes are
   completely prepared, present one combined summary of the WileyPLUS question
   set and policies, Canvas launch shell, and announcement, then request one
   final publication confirmation. Once confirmed, finish the sequence without
   another pause unless WileyPLUS or Canvas exposes a material conflict.

After WileyPLUS and Canvas publication and verification, update the tracked
handoff and status files and request one closeout `Checkpoint` if those
completion updates are uncommitted. This preserves the finished external state
and is not another Canvas confirmation.

Then carry out the following steps:

1. Audit the repository, Canvas, and WileyPLUS for an existing assignment page,
   WileyPLUS question set, Canvas item, or announcement. Resume and verify valid
   existing work rather than creating duplicates.
2. Complete the textbook-to-WileyPLUS reconciliation above. In WileyPLUS,
   create or verify the approved question set, its total and per-question
   points, randomization, attempt and scoring policies, and 11:59 PM
   America/Chicago deadline.
3. Create or reuse an unpublished Canvas assignment shell. Configure it as an
   individual **External Tool** assignment in the **Assignments** group, display
   the grade as points, use the approved WileyPLUS deep link, set its points to
   the WileyPLUS total, and leave Canvas **Due** and **Until** blank. Record
   every Canvas assignment URL as
   `canvas.assignment_N` in `course-metadata.yml`. When converting an already
   published assignment, first inspect the complete submission roster. If any
   submission exists, stop and obtain explicit instructor direction before
   changing the assignment. If none exists, preserve its Canvas URL and point
   total unless the instructor explicitly changes the points, and make the
   WileyPLUS question weights sum to that total.
4. Create or update `assignments/assignment_N.qmd`. State the WileyPLUS
   deadline, actual selected question identifiers and coverage, point and
   attempt policies, and the individual Canvas-launch workflow. Link back to
   the ground rules in `pages/assignments.qmd`.
5. Add or update the assignment in the table in `pages/assignments.qmd`, with
   its descriptive title, coverage, and due date. Link to the course-hosted
   detail page.
6. Add or update the due-date entry in `pages/schedule.qmd`, linking to the same
   authoritative assignment details.
7. Determine from the assignment coverage which RevealJS deck contains the
   relevant notes. Put the assignment name and due date on exactly one deck's
   title slide. If the appropriate deck is ambiguous, choose one suitable deck
   rather than duplicating the reminder. When useful, add a brief linked
   logistics slide describing the individual WileyPLUS workflow. Retain past
   assignment reminders on their original decks as a chronological record; do
   not remove or replace them merely because their due dates have passed.
8. Render the root website and the independent slide project, assemble the
   complete site, and verify the assignment page, Assignments table, Schedule,
   Canvas links, deck notice, and internal links. Inspect the visible assignment
   page and affected deck at the standard RevealJS viewport. After the
   instructor issues the exact `Checkpoint` command, checkpoint and push the
   changes, then verify that the public assignment and Assignments-page URLs are
   live.
9. After the final publication confirmation, publish the Canvas assignment and
   then its course-wide announcement. The Canvas description should give a
   concise launch instruction and link to the two live course pages without
   repeating the selected questions, deadline, points, or attempt policy.
10. Re-open the published Canvas item and verify its title, points, assignment
    group, individual External Tool submission type, intended WileyPLUS deep
    link, blank Canvas **Due** and **Until** fields, publication state, and
    course audience. In WileyPLUS, verify the approved question set and points,
    deadline and time zone, randomization, attempts and scoring, grade passback,
    and a student-visible Canvas launch. Verify the announcement links and
    audience, then update the appropriate handoff and status files. If the
    workflow is interrupted, preserve drafts and resume from the latest verified
    repository, Canvas, and WileyPLUS state rather than conversational memory.
    Request the exact `Checkpoint` command to publish any post-publication
    completion updates still uncommitted in the repository.

## Adding or updating a quiz or test

Use the following workflow whenever a quiz, test, or final-exam detail is
finalized or materially revised:

When dates are established before coverage or other details are final, first
follow the shared
[`Save-the-date announcements`](classlib/docs/assessment-save-the-date.md)
workflow. Then apply the MATH 332 rules below as the remaining details are
finalized.

Keep every assessment PDF out of the public repository and test archive until
the assessment has been administered and grading is complete. Never publish the
student/no-answers copy. After grading, publish only the answer-key PDF with an
anonymous score distribution, following **Released quiz and test answer keys**
below. The only exception is a take-home component of a final examination: its
student/no-answers copy may be published when the instructor intentionally
releases it to students, but its answers and score distribution remain private
until grading is complete.

1. Confirm the assessment name, date, duration, coverage, point value, and
   Canvas status. Leave unresolved dates and details explicitly marked TBD.
2. Maintain `pages/quizzes-and-tests.qmd` as the authoritative location for
   the combined assessment schedule and course-wide rules. State common rules
   once rather than repeating an administration column for every assessment.
   MATH 332 quizzes and tests are closed book and allow no devices; students
   may use up to four letter-sized sheets of paper as memory aids, while the
   final examination allows up to eight. Include the individual-work and
   academic-integrity expectations and state that students with recognized
   accommodations receive the testing arrangements specified in their
   accommodation letters. Unless the instructor explicitly announces
   otherwise, application problems must provide the linear system rather than
   require students to derive it from the application.
3. Record quiz coverage only on the combined Quizzes and Tests page. Quizzes
   use the last 15 minutes of class, tests use the full 75-minute class period,
   and these common timing rules belong in the page guidance rather than in
   every schedule row.
4. Add the assessment to `pages/schedule.qmd`. Put only its name in the class
   event column. In the materials column, link to every covered deck by its
   full title, placing each link on its own line with `<br>`. The Quizzes and
   Tests page is available through the site navigation and should not be
   linked redundantly from an assessment's schedule row.
5. Add the assessment name and date to the title slide of the latest deck
   included in its coverage. Do not put the coverage or duration on the deck
   title slide, and remove or replace stale notices as the course advances.
6. For a paper assessment, create a Canvas assignment configured for **On
   Paper** submission so that it appears in Grades without accepting an online
   submission. Grade the papers and enter scores manually. Do not publish a
   saved Canvas draft until publication is explicitly intended.
7. Render and assemble the complete course site. Verify the combined page,
   schedule links, assessment notice, internal navigation, and affected deck
   at the standard RevealJS viewport before checkpointing.

## Releasing a graded quiz, test, or examination

Use this workflow after grading is complete. The recommended trigger is
`Assessment release 332 Quiz 1`; substitute `565` and the exact assessment
name as needed. The command authorizes the grade release, answer-key
publication, required repository commits and pushes, live verification, and
preparation of an unpublished Canvas announcement. Publishing the announcement
remains a separate final action after the instructor reviews the draft.

1. Reconstruct the current state before changing anything. Inspect the private
   LaTeX source and trailing private notes, the grading workbook or other
   authoritative score record, the Canvas assignment and posting policy, the
   Quizzes and Tests page, the current-assessment directory, the canonical test
   archive, repository status, submodule status, and relevant recent commits.
   Confirm that grading is complete and that the assessment name, point total,
   and Canvas column agree. Stop rather than guessing if scores or identities
   conflict.
2. Reconcile every correction between the authoritative score record and
   Canvas. Before entering any unreviewed scores, set and verify manual grade
   posting, load the scores while they remain hidden, exclude Test Student, and
   present the completed Gradebook for instructor review. Treat a zero as a
   nonparticipant only when Canvas or the grading record establishes that the
   student did not take the assessment; otherwise retain it as an earned score.
3. Add an anonymous score distribution to the answer version. Include all and
   only participating students, omit names and identifiers, and use the
   course's established exam-style stem-and-leaf and summary statistics. Keep
   questions and worked solutions in the authoritative private LaTeX source
   using `Answer` environments. Build with `fh-exam-build.py`, which creates
   the explicit `_NO_Answers.pdf` and `_Answers.pdf` outputs, and visually
   inspect the complete answer PDF. Never publish the no-answers copy.
4. Verify manual posting in Canvas immediately before release. Post the
   assessment grades and any approved held feedback to the intended graded
   students, then verify the student-facing posting state. If the course uses
   a synthetic item such as **Best Test**, confirm its point value, assignment
   group, no-submission setting, and published state. Leave it ungraded until
   the underlying scores needed for its calculation exist; when they do,
   enter and verify the value defined by the syllabus policy.
5. Copy the verified `_Answers.pdf` into the matching course folder of the
   canonical `HickernellTestArchive`. Commit and push the archive first. Then
   copy that identical PDF into `assets/tests/current/`, update the course's
   pinned archive commit, and link the current copy from
   `pages/quizzes-and-tests.qmd`. Do not advance another course's archive pin
   merely because the archive now contains this release.
6. Update the course handoff files and reconcile the authoritative
   `GitTracked/Check-In-Dashboard.md`. Remove every completed grading task for
   the released assessment under the Dashboard completion policy, preserve
   related work that remains incomplete, ensure the course's current next task
   is still represented, and update the Dashboard timestamp. Follow the
   Dashboard repository's own synchronization and commit-scope rules rather
   than silently bundling it into the course commit. Render the affected page
   and perform the public-repository confidentiality audit:
   the diff may contain only the released answer PDF, anonymous distribution,
   public links, and nonsensitive release status. It must not contain student
   data, the private source, grading files, the no-answers PDF, or unreleased
   assessment details.
7. Commit and push the affected course repository after the archive push.
   Push or verify every writable submodule involved in the release, while
   leaving read-only pinned dependencies unchanged. Do not update or push an
   unrelated course merely as part of a single-course release.
8. Wait for the course-site deployment because the next step depends on live
   links. Verify the deployment result, the Quizzes and Tests page, the current
   answer-PDF URL, and the archive URL. Confirm that both public PDFs return
   successfully and are byte-identical to the visually inspected release copy.
9. Draft a concise all-sections Canvas announcement stating that grades are
   posted and linking to the live Quizzes and Tests page. When applicable,
   explain how a **Best Test** item will implement the syllabus weighting
   without exposing any student's result. Keep the announcement unpublished
   for instructor review; Canvas may provide only a **Publish** button, in
   which case leave the completed editor open and report that the draft is not
   durably saved.
10. Report the Canvas posting result, live links, archive and course commit
    hashes, deployment result, validation performed, clean repository states,
    intentionally uncommitted work, and remaining actions. The usual remaining
    action is `Publish the assessment announcement` after reviewing the draft.

## Post-lecture pacing reconciliation

After each lecture, reconcile the public schedule and the next lecture plan
against the Panopto recording:

The exact command `Lecture update` runs this workflow for the current course;
`Lecture update 332` and `Lecture update 565` select the named active course
from either course repository. The command itself authorizes the email,
Panopto, schedule, and single-occurrence calendar actions below.

1. Check the Illinois Tech email account for the Panopto “Ready to view”
   notice. This standing workflow authorizes that read-only email check. If
   Panopto authentication is required, begin at `https://portal.iit.edu` and
   continue in the same browser session.
2. Inspect the recording near the end of the substantive lecture portion,
   before any quiz, test, or administrative wrap-up. Use the captions and the
   visible slide or board to identify the last topic actually completed and
   the first topic that still needs attention; do not infer the stopping point
   from the planned schedule alone.
3. Update the completed meeting's row in `pages/schedule.qmd` to describe what
   was actually covered. Update the next instructional meeting's row with the
   continuation topic and its existing deck or material link. Keep assessment
   rows and coverage statements intact. Never use an assessment-only meeting
   as the continuation destination; when a quiz, test, or examination
   intervenes, carry the continuation to the next instructional meeting.
4. Add a concise continuation note to the next instructional MATH 332 event on
   the Illinois Tech `Calendar` calendar. Name the deck and first slide or
   section to resume, followed by a short record of what the preceding lecture
   completed. Edit only that occurrence of the recurring course event unless
   the instructor explicitly requests a series-wide change.
5. Verify the calendar account, occurrence date, event time, location, and
   saved note, then render or otherwise validate the changed schedule page.
6. Record the successful reconciliation in `notes/LECTURE-UPDATES.md`,
   including the lecture date, Panopto recording identifier or link, next
   instructional event annotated, and check date. Do not advance the ledger
   when the recording or stopping point could not be verified.
7. Leave repository changes uncommitted and unpublished until the instructor
   gives the exact `Checkpoint` command.

If the recording notice has not arrived, do not guess. Leave the schedule and
calendar unchanged and check again later.

## Slide-source conventions

- Whenever an assessed item is finalized or updated on its course website
  page, also put its name and date on exactly one relevant deck title slide,
  following the assessment-specific workflow above. Choose one suitable
  covered deck for an assignment when the placement is ambiguous, and retain
  past assignment reminders there as a chronological record. Use the latest
  covered deck for a quiz or test; do not add its coverage or duration to the
  deck title, and remove or replace stale quiz and test notices as the course
  advances.
- Write `#` section headings in title case: capitalize principal words while
  leaving articles, coordinating conjunctions, and short prepositions
  lowercase unless they begin or end the heading. Write `##` slide headings
  and `###` subheadings in sentence case: capitalize only the first word and
  proper nouns, acronyms, and mathematical notation.
- In the Course Map's **In this deck** list, repeat each linked `#` section
  heading exactly, including its title capitalization and punctuation.
- Follow the [shared Course Map theme convention](classlib/docs/slide-style.md#course-map-themes).
  MATH 332 uses 38% for Course decks, a 4% empty gutter, and 58% for In this
  deck throughout the course. Placeholder decks use the same map and link
  only their existing section headings. Center phrase-only themes at
  `1.5em`; Deck 00 uses a 🎬 clapperboard beside `[Teaser Trailer]{.alert}`.
- Every instructional `#` section slide must link to all of its child `##`
  slides in presentation order; `###` subheadings do not belong in this list.
  When the section slide also contains content, place brief framing or
  motivation above the links by default and supporting examples or secondary
  material below them. Decide case by case, keeping the links easy to scan.
- Treat each `##` heading as the conceptual umbrella for every following `###`
  until the next `##`. Keep a `###` and its content on the governing `##` slide
  by default. Add `---` only when the combined slide would be crowded or a
  separate slide materially improves presentation pacing; the slide break does
  not change the heading hierarchy. Do not multiply slide breaks merely to
  separate headings. Do not merely demote a heading to reduce the section
  outline: ensure that each `###` heading and its content substantively flow
  from the governing `##`. Rename or add an umbrella heading, or regroup the
  slides, when that relationship is unclear. The `##` slide may contain
  framing or other overall content before the first `###`.
- Maintain the cumulative **Terms to know** index in Deck 00. After completing
  or substantially revising a lecture deck, audit it for important terminology
  and add appropriate terms alphabetically. Link each term to the slide where
  it first receives substantial treatment, not merely its first mention. Do
  not invent links for topics that have not yet been developed. Split the
  index into alphabetical continuation slides as needed while retaining
  `#terms-to-know` as its stable entry point.
- Prefer readable Quarto Markdown for headings, text, columns, equations, and
  ordinary emphasis. Use raw HTML when a diagram or specialized layout is
  materially easier to construct that way.
- When a `.key-point` callout contains two or more distinct takeaways, use a
  standalone `&nbsp;` paragraph between them only when the takeaways are
  substantial enough to need visual separation—for example, when at least one
  occupies roughly two-thirds of a line or more, or wraps, at the standard
  slide viewport. When all of the takeaways are shorter than roughly
  two-thirds of a line, omit the spacer because it creates too much empty
  space. Treat this threshold as a visual heuristic rather than a source-text
  character count. Do not insert a spacer between clauses that form one
  definition, contrast, or tightly coupled statement.
- In slide-editing requests, interpret **highlight** as the established
  `{.alert}` style and **emphasize** as italic emphasis such as `\emph{}` unless
  the user specifies another treatment.
- For a matrix such as $\mat{A}$, denote its columns by uppercase vector
  symbols $\vct{A}_j$ and its rows by lowercase transposed vector symbols
  $\vct{a}_i^{\mathsf T}$. Apply the same uppercase-column/lowercase-row
  convention to other matrices.
- When prose refers to another course deck, use the metadata-defined short deck
  title and link it to that deck or the relevant slide. Avoid bare numeric
  labels such as `Deck 02` unless the deck number or sequence is itself the
  point.
- Beginning with Deck 01, each completed instructional deck should close its
  substantive content with a `# Big Ideas {data-state="goldborder"}` summary
  slide before any next-deck handoff. Include `Big Ideas` in the Course Map and
  summarize only ideas earned by that deck, using concise statements and
  selective `{.alert}` highlighting. Add the slide when a deck is developed;
  do not invent summaries for placeholders.
- Beginning with Deck 02, follow Big Ideas with `# How Far We Have Come` and
  then `# What Comes Next`. The middle slide should synthesize ideas actually
  developed from the start of the course through that deck, not repeat its Big
  Ideas slide. In the Course Map, one `Big Ideas` link points to the start of
  this three-slide closing sequence. Add the sequence to placeholder decks
  only when their instructional content has been developed.
- RevealJS hierarchy exception: inside a `#` section slide, use an HTML `<h3>`
  for a visible tertiary heading because Quarto `###` does not render there as
  intended. Inside a `##` slide, ordinary Quarto `###` headings work normally.
- For MATH 332 topic sequences, supporting derivations, worked examples, and
  exercises may use `---` followed by a `###` continuation heading under the
  preceding `##` topic. Retain explicit anchors for direct links, and list only
  the main `##` topics in the section outline. Deck 05's Euclidean Tools
  section demonstrates this course-specific continuation-slide convention.
- Follow the shared slide-writing guidance in `classlib/AGENTS.md`.
- Typeset matrix symbols in sans serif. In RevealJS slides, use `\mat{A}` from
  the JavaScript-provided MathJax macros. JupyterLab does not load those
  macros, so use explicit `\mathsf{A}` in notebook Markdown.
- Use the shared statistical notation macros in slides, including `\Norm` for
  the normal distribution and the lowercase Biometrika-style operators `\var`
  and `\cov`. Do not replace them with ad hoc `\mathcal{N}`, `\operatorname{Var}`,
  or `\operatorname{Cov}` forms.
- Mark questions and in-class exercises with `$\exstar$` (or the appropriate
  shared exercise notation). Do not place worked answers later in the
  student-visible deck when they would reveal an activity students should do
  in class.
- Prefer `\begin{align}` or `\begin{align*}` for multiline displayed equations
  when it works directly. Use `aligned` only when the equations must be nested
  inside another math environment or diagram element.
- Reuse classlib semantic and spacing classes, including `vspace-sm`, `vspace`,
  and `vspace-lg`. Avoid new one-off classes for prose or simple spacing.
- Keep deck-specific CSS focused on genuine diagram construction. Before adding
  a selector, check whether classlib or an existing deck class already provides
  the needed behavior.

## Fresh clone and Python environment

Use the standard `qmcpy` Python environment and Jupyter kernel. If the
environment does not already exist, create it once with Python 3.11 or later:

```bash
conda create --name qmcpy "python>=3.11"
```

Then install the course dependencies and register that environment as the
`qmcpy` kernel:

```bash
git clone --recurse-submodules https://github.com/fjhickernell/MATH332Fall2026.git
cd MATH332Fall2026
git submodule update --init --recursive
conda activate qmcpy
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e classlib
python -m ipykernel install --user --name qmcpy --display-name "qmcpy"
```

### Colab notebooks

A student-facing Colab badge must open the notebook in this repository. Rely
on the established Colab setup and address problems when reported; separate
clean-Colab execution is not required for every notebook. Keep local execution
validation and instructor content review. Keep the setup cell a no-op outside
Colab. In Colab, clone the current course repository, initialize the recorded
`classlib` submodule using its public HTTPS URL, and install that checkout.
This preserves the course's validated shared-library version instead of
silently substituting a moving branch or an unrelated package release.

Install TeX packages only for notebooks that enable Matplotlib's external TeX
rendering. Do not change the working directory during setup, and remind
students that Colab does not save changes back to the course repository.

### Notebook execution timing

Every course notebook must set
`NOTEBOOK_START_TIME = time.perf_counter()` in its initial setup cell, before
Colab detection and setup, and keep a final code cell with the ID
`notebook-runtime` that reports `Total execution time for this notebook is …
min … sec.` The runtime cell must remain the notebook's last cell. Validate the
complete run and its timing output with the `qmcpy` kernel before publication;
separate clean-Colab validation is not a publication requirement.

## Preview and render

For the Deck 05 equation-and-geometry figure pattern, including serif vector
labels, raw SVG blocks, and arrow sizing, see
[the projection-figure implementation notes](notes/TECHNICAL-NOTES.md#deck-05-projection-figure-implementation-and-validation).

Preview the website:

```bash
quarto preview
```

Render and assemble the complete site:

```bash
quarto render
(cd slides && quarto render)
rm -rf _site/slides
mkdir -p _site/slides
rsync -a --delete slides/_site/ _site/slides/
```

After rendering, inspect warnings, open representative website pages and all
nine decks, verify previous/next deck navigation, and confirm that internal
links and shared `classlib` assets resolve. Do not commit `_site/`, `.quarto/`,
or other generated output.

For Schedule changes, follow the shared
[webpage style guide](classlib/docs/webpage-style.md)
guidance. Inspect every monthly table, including sparse future rows; keep Week
and Date compact, leave Topic useful space, and check assessment line breaks
and indentation.

## Shared infrastructure

Reuse `classlib` for shared website and RevealJS infrastructure. A reusable
change belongs in HickernellAcademicLib only after it is validated, committed,
and pushed upstream; then update the recorded submodule pointer intentionally.
Keep all MATH 332 content in this repository.

## Released quiz and test answer keys

After grading is complete, keep released answer-key PDFs in
`assets/tests/current/` and link them from `pages/quizzes-and-tests.qmd`.
Include the anonymous score distribution in the PDF; keep student names and the
private LaTeX source out of the public repository. Never publish the
student/no-answers copy. Copy the same released PDF into the `332/` folder of the
canonical `HickernellTestArchive` checkout. Publish archive changes separately;
then intentionally advance this course's pinned archive to that published
commit. Do not update another course's pinned archive merely to add a MATH 332
file.
