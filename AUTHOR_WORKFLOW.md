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

## Slide-source conventions

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
- Prefer readable Quarto Markdown for headings, text, columns, equations, and
  ordinary emphasis. Use raw HTML when a diagram or specialized layout is
  materially easier to construct that way.
- RevealJS hierarchy exception: inside a `#` section slide, use an HTML `<h3>`
  for a visible tertiary heading because Quarto `###` does not render there as
  intended. Inside a `##` slide, ordinary Quarto `###` headings work normally.
- Follow the shared slide-writing guidance in `classlib/AGENTS.md`.
- Typeset matrix symbols in sans serif. In RevealJS slides, use `\mat{A}` from
  the JavaScript-provided MathJax macros. JupyterLab does not load those
  macros, so use explicit `\mathsf{A}` in notebook Markdown.
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
seven decks, verify previous/next deck navigation, and confirm that internal
links and shared `classlib` assets resolve. Do not commit `_site/`, `.quarto/`,
or other generated output.

## Shared infrastructure

Reuse `classlib` for shared website and RevealJS infrastructure. A reusable
change belongs in HickernellAcademicLib only after it is validated, committed,
and pushed upstream; then update the recorded submodule pointer intentionally.
Keep all MATH 332 content in this repository.
