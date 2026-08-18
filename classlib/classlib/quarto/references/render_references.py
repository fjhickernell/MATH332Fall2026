import math
import re
import textwrap
import yaml
from pathlib import Path


def load_papers(refs_path):
    refs_path = Path(refs_path)
    return yaml.safe_load(refs_path.read_text())["papers"]


def find_used_paper_keys(deck_text):
    return sorted(
        set(re.findall(r"papers\.([A-Za-z0-9_-]+)\.cite", deck_text))
        |
        set(re.findall(r"\\yamlref\{([A-Za-z0-9_-]+)\}", deck_text))
    )


def best_links(p):
    links = []
    if p.get("doi_url"):
        links.append(f'[DOI]({p["doi_url"]})')
    if p.get("arxiv_url"):
        links.append(f'[arXiv]({p["arxiv_url"]})')
    if p.get("publisher_url"):
        links.append(f'[publisher]({p["publisher_url"]})')
    if p.get("project_url"):
        links.append(f'[link]({p["project_url"]})')
    return " · ".join(links)


def sort_key_for(papers):
    def sort_key(key):
        return papers[key].get("short", papers[key].get("full", "")).lower()
    return sort_key


def estimated_ref_lines(p, wrap_width=92):
    label = f'[{p["cite"]}] '
    full = p.get("full", "")
    links = best_links(p)

    n = max(1, math.ceil(len(label + full) / wrap_width))
    if links:
        n += max(1, math.ceil(len(links) / wrap_width))
    return n + 1


def paginate_keys(keys, papers, max_lines=12, wrap_width=92):
    pages = []
    current = []
    current_lines = 0

    for key in keys:
        nlines = estimated_ref_lines(papers[key], wrap_width=wrap_width)

        if current and current_lines + nlines > max_lines:
            pages.append(current)
            current = []
            current_lines = 0

        current.append(key)
        current_lines += nlines

    if current:
        pages.append(current)

    return pages


def render_reference_slides(
    deck_path,
    refs_path,
    *,
    max_lines=12,
    wrap_width=92,
    title="References",
    refs_class="refs",
):
    deck_path = Path(deck_path)
    deck_text = deck_path.read_text()
    papers = load_papers(refs_path)

    used_keys = find_used_paper_keys(deck_text)
    used_keys = [key for key in used_keys if key in papers]
    ordered_keys = sorted(used_keys, key=sort_key_for(papers))
    pages = paginate_keys(
        ordered_keys,
        papers,
        max_lines=max_lines,
        wrap_width=wrap_width,
    )

    for page_num, page_keys in enumerate(pages, start=1):

        if page_num > 1:
            print("\n---\n")
        print(f"::: {{.{refs_class}}}")

        for key in page_keys:
            p = papers[key]
            links = best_links(p)

            print()
            print(f'[{p["cite"]}]{{.ref-label}} {p["full"]}')
            if links:
                print(links)

        print()
        print(":::")
        print()