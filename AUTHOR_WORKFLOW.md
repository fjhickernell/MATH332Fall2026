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

Use the following workflow whenever an assignment is finalized or materially
revised:

1. Confirm the assignment content, coverage, due date and time, point value,
   submission requirements, and Canvas settings. Do not invent unresolved
   details.
2. If course sources need a stable Canvas assignment URL, create only an
   unpublished Canvas draft at this stage and record its URL as
   `canvas.assignment_N` in `course-metadata.yml`. Do not publish the Canvas
   assignment or announce it while its course-website links are unavailable.
3. Create or update `assignments/assignment_N.qmd` when the assignment needs a
   course-hosted detail page. State the due date, assignment, and submission
   requirements, and link back to the ground rules in
   `pages/assignments.qmd`.
4. Add or update the assignment in the table in `pages/assignments.qmd`, with
   its descriptive title, coverage, and due date. Link to the course-hosted
   detail page when one exists; otherwise link directly to Canvas.
5. Add or update the due-date entry in `pages/schedule.qmd`, linking to the
   same authoritative assignment details.
6. Determine from the schedule which RevealJS deck is current when the
   assignment is assigned. Add or update the due-date notice on that deck's
   title slide and, when useful, a brief linked logistics slide describing the
   assignment and group-submission expectations. Remove or replace stale
   notices as the course advances.
7. Render the root website and the independent slide project, assemble the
   complete site, and verify the assignment page, assignments table, schedule,
   Canvas links, deck notice, and internal links. Inspect the visible assignment
   page and affected deck at the standard RevealJS viewport. Checkpoint and
   push the website changes, then verify that the public assignment and
   Assignments-page URLs are live. This publication check is a hard gate before
   publishing the Canvas assignment.
8. Finish and publish the Canvas assignment only after the website is live.
   Unless the assignment explicitly requires individual work, create a
   separate self-sign-up group set named `Assignment N Groups` for that
   assignment so students may choose a new partner each time. Limit groups to
   pairs, and configure Canvas so that one submission is shared by both group
   members. Keep the assignment-specific details authoritative on the
   course-hosted detail page; the Canvas description should link to that page
   and to the course Assignments page rather than repeat instructions that
   could later diverge. Verify the published assignment, then announce it in
   Canvas by linking to the live course pages and providing only the operational
   group and submission information students need. Do not repeat the assignment
   content or due date in the announcement.

## Slide-source conventions

- Whenever a homework, assignment, quiz, or similar assessed item
  is finalized or updated on its course website page, also add or update its
  due-date notice on the title slide of the deck current when the item is
  assigned. Determine the relevant deck from the course schedule and the
  assignment date; remove or replace stale notices as the course advances.
- Write `#` section headings in title case: capitalize principal words while
  leaving articles, coordinating conjunctions, and short prepositions
  lowercase unless they begin or end the heading. Write `##` slide headings
  and `###` subheadings in sentence case: capitalize only the first word and
  proper nouns, acronyms, and mathematical notation.
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
- When a `.key-point` callout contains two or more distinct takeaways, place a
  standalone `&nbsp;` paragraph between them to create a small visual
  separation. Do not insert a spacer between clauses that form one definition,
  contrast, or tightly coupled statement.
- In slide-editing requests, interpret **highlight** as the established
  `{.alert}` style and **emphasize** as italic emphasis such as `\emph{}` unless
  the user specifies another treatment.
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
- RevealJS hierarchy exception: inside a `#` section slide, use an HTML `<h3>`
  for a visible tertiary heading because Quarto `###` does not render there as
  intended. Inside a `##` slide, ordinary Quarto `###` headings work normally.
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

## Preview and render

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

## Shared infrastructure

Reuse `classlib` for shared website and RevealJS infrastructure. A reusable
change belongs in HickernellAcademicLib only after it is validated, committed,
and pushed upstream; then update the recorded submodule pointer intentionally.
Keep all MATH 332 content in this repository.
