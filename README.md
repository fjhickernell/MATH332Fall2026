# MATH 332 — Fall 2026

This repository contains the Quarto website and course materials for **MATH
332: Linear Algebra: Theory and Applications** at Illinois Institute of
Technology.

The RevealJS decks in `slides/` are the authoritative course presentation
materials. Mathematical content should be maintained only in the slides.

The required textbook is Howard Anton, *Elementary Linear Algebra:
Applications Version*, 12th edition. Course content will be developed
incrementally across Chapters 1–6.

## Local setup

Prerequisites are Git, Quarto, and Python 3.11 or later. From a fresh clone:

```bash
git clone --recurse-submodules https://github.com/fjhickernell/MATH332Fall2026.git
cd MATH332Fall2026
python -m pip install -r requirements.txt
python -m pip install -e classlib
```

See `AUTHOR_WORKFLOW.md` for preview, validation, and publishing instructions.
