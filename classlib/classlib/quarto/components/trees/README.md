# Reusable tree components

This component renders image-backed, labelled trees from versioned YAML
configurations. The renderer and base layout are generic. Each tree
configuration owns its labels, groups, positions, alignments, masks, and
tree-specific styles. Artwork is stored separately so multiple configurations
can explicitly share it.

## Files

- `schema.py` validates schema version 1 and resolves registered trees
- `renderer.py` returns an HTML fragment
- `tree-base.scss` supplies only generic layout
- `artwork/` contains reusable physical artwork
- `<tree-id>/tree.yml` contains a complete tree design
- `<tree-id>/tree.scss` contains artwork- and tree-specific presentation

The `qmc/` and `mc/` configurations share the physical artwork but independently
define their groups, labels, positions, alignments, masks, and styling.

## Schema version 1

A ready tree has this shape:

```yaml
schema_version: 1
id: example-tree
status: ready

image:
  file: "../artwork/tree.png"
  alt: "Meaningful alternative text"
  aspect_ratio: "4 / 3"

defaults:
  width: "100%"
  font_scale: 1
  label_align: left
  group_align: left

groups:
  example-group:
    text: "Group heading"
    labels: [first-label]
    position: {left: "40%", top: "50%"}
    align: center

labels:
  first-label:
    html: "Trusted<br>markup"
    position: {left: "20%", top: "70%"}
    align: center

masks:
  example-mask:
    description: "What the mask reveals or hides"
```

All mappings are strict: unknown fields are rejected. Identifiers are safe
kebab-case strings. `text` is HTML-escaped and `html` is deliberately trusted
inline markup. A content object must define exactly one of them. A placeholder
contains only `schema_version`, `id`, and `status: placeholder`.

## Loading from a Quarto repository

The submodule need not be installed as a Python package. A slide notebook can
put the component's parent directory on `sys.path`, then import `trees`. The
cell must use `output: asis` so Quarto passes the returned HTML through to
Pandoc:

````markdown
```{python}
#| echo: false
#| output: asis
from pathlib import Path
import sys

for repository_root in (Path.cwd(), *Path.cwd().parents):
    TREE_COMPONENTS = (
        repository_root
        / "classlib"
        / "classlib"
        / "quarto"
        / "components"
    )
    if (TREE_COMPONENTS / "trees" / "__init__.py").is_file():
        TREE_COMPONENTS = TREE_COMPONENTS.resolve()
        break
else:
    raise FileNotFoundError("Cannot find the classlib tree components")

sys.path.insert(0, str(TREE_COMPONENTS))

from trees import render_tree

html = render_tree(
    "qmc",
    groups=["foundation", "theory"],
    show_group_headings=True,
    asset_base_url="classlib/classlib/quarto/components/trees",
)
print(html)
```
````

Adjust `TREE_COMPONENTS` and `asset_base_url` for the notebook's location and
rendered output directory. The Quarto project must copy the submodule assets,
for example by including `classlib/**/*` in `project.resources`.

Styles are opt-in. Import both layers only in a deck that uses the tree:

```scss
@import "../classlib/classlib/quarto/components/trees/tree-base";
@import "../classlib/classlib/quarto/components/trees/qmc/tree";
```

The exact relative import paths depend on the location of the importing SCSS.
The component is intentionally not imported by the global Hickernell slide
theme.

## Rendering API

`render_tree()` accepts a registered tree identifier, an explicit YAML path, or
an already validated `TreeSpec`. Group selection expands labels in YAML order.
Direct labels are appended in request order. Duplicate labels are emitted once.
Group headings may be selected explicitly or all shown. Masks, width, font
scale, and additional safe classes are optional.

The returned value is an HTML string and has no notebook display side effect.
