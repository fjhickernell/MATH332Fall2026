"""HTML rendering for reusable image-backed tree diagrams."""

from __future__ import annotations

import html
from pathlib import Path
import posixpath
from typing import Iterable
from urllib.parse import urlsplit, urlunsplit

from .schema import (
    CSS_LENGTH,
    SAFE_IDENTIFIER,
    ContentSpec,
    TreeNotReadyError,
    TreeSchemaError,
    TreeSpec,
    load_tree,
    load_tree_file,
)


class TreeRenderError(ValueError):
    """Raised when a render request is inconsistent with its tree schema."""


def _identifier_list(
    values: Iterable[str] | None,
    *,
    field: str,
) -> list[str]:
    if values is None:
        return []
    if isinstance(values, (str, bytes)):
        raise TreeRenderError(f"{field} must be a sequence, not a string")
    result: list[str] = []
    for index, value in enumerate(values):
        if not isinstance(value, str) or not SAFE_IDENTIFIER.fullmatch(value):
            raise TreeRenderError(
                f"{field}[{index}] must be a safe kebab-case identifier"
            )
        result.append(value)
    return result


def _positive_number(value: float, *, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TreeRenderError(f"{field} must be a number")
    number = float(value)
    if number <= 0:
        raise TreeRenderError(f"{field} must be positive")
    return number


def _css_length(value: str, *, field: str) -> str:
    if not isinstance(value, str) or not CSS_LENGTH.fullmatch(value):
        raise TreeRenderError(f"{field} must be a supported CSS length")
    return value


def _content_html(content: ContentSpec) -> str:
    if content.trusted_html:
        return content.value
    return html.escape(content.value)


def _asset_url(
    *,
    asset_base_url: str,
    tree_identifier: str,
    image_file: str,
) -> str:
    if not isinstance(asset_base_url, str) or not asset_base_url.strip():
        raise TreeRenderError("asset_base_url must be a nonempty string")

    base = f"{asset_base_url.rstrip('/')}/{tree_identifier}/"
    parsed = urlsplit(base)
    normalized_path = posixpath.normpath(
        posixpath.join(parsed.path, image_file)
    )
    if parsed.path.startswith("/") and not normalized_path.startswith("/"):
        normalized_path = f"/{normalized_path}"
    return urlunsplit(
        (
            parsed.scheme,
            parsed.netloc,
            normalized_path,
            parsed.query,
            parsed.fragment,
        )
    )


def _position_style(*, left: str, top: str, align: str) -> str:
    return (
        f"--tree-left: {left}; "
        f"--tree-top: {top}; "
        f"--tree-align: {align};"
    )


def _resolve_tree(tree: str | Path | TreeSpec) -> TreeSpec:
    if isinstance(tree, TreeSpec):
        return tree
    if isinstance(tree, Path):
        return load_tree_file(tree)
    if isinstance(tree, str):
        return load_tree(tree)
    raise TreeRenderError("tree must be a tree identifier, path, or TreeSpec")


def render_tree(
    tree: str | Path | TreeSpec,
    *,
    groups: Iterable[str] | None = None,
    labels: Iterable[str] | None = None,
    group_headings: Iterable[str] | None = None,
    show_group_headings: bool = False,
    mask: str | None = None,
    width: str | None = None,
    font_scale: float | None = None,
    classes: Iterable[str] | None = None,
    asset_base_url: str,
) -> str:
    """Render a configured tree as a namespaced HTML fragment."""

    spec = _resolve_tree(tree)
    if spec.status != "ready":
        raise TreeNotReadyError(f"tree {spec.identifier!r} is a placeholder")
    if spec.image is None or spec.defaults is None:
        raise TreeSchemaError(f"ready tree {spec.identifier!r} is incomplete")

    group_ids = _identifier_list(groups, field="groups")
    direct_label_ids = _identifier_list(labels, field="labels")
    heading_ids = _identifier_list(group_headings, field="group_headings")
    extra_classes = _identifier_list(classes, field="classes")

    for group_id in group_ids:
        if group_id not in spec.groups:
            raise TreeRenderError(f"undefined group {group_id!r}")
    for label_id in direct_label_ids:
        if label_id not in spec.labels:
            raise TreeRenderError(f"undefined label {label_id!r}")
    for heading_id in heading_ids:
        if heading_id not in spec.groups:
            raise TreeRenderError(f"undefined group heading {heading_id!r}")

    if show_group_headings and heading_ids:
        raise TreeRenderError(
            "show_group_headings and group_headings are mutually exclusive"
        )
    if show_group_headings:
        heading_ids = list(spec.groups)

    selected_labels: list[str] = []
    seen: set[str] = set()
    for group_id in group_ids:
        for label_id in spec.groups[group_id].labels:
            if label_id not in seen:
                selected_labels.append(label_id)
                seen.add(label_id)
    for label_id in direct_label_ids:
        if label_id not in seen:
            selected_labels.append(label_id)
            seen.add(label_id)

    if mask is not None:
        if not isinstance(mask, str) or not SAFE_IDENTIFIER.fullmatch(mask):
            raise TreeRenderError("mask must be a safe kebab-case identifier")
        if mask not in spec.masks:
            raise TreeRenderError(f"undefined mask {mask!r}")

    render_width = _css_length(
        width if width is not None else spec.defaults.width,
        field="width",
    )
    render_font_scale = _positive_number(
        font_scale if font_scale is not None else spec.defaults.font_scale,
        field="font_scale",
    )

    container_classes = [
        "tree-component",
        f"tree-component--{spec.identifier}",
        *extra_classes,
    ]
    container_style = (
        f"--tree-width: {render_width}; "
        f"--tree-font-scale: {render_font_scale:g}; "
        f"--tree-aspect-ratio: {spec.image.aspect_ratio};"
    )
    image_url = _asset_url(
        asset_base_url=asset_base_url,
        tree_identifier=spec.identifier,
        image_file=spec.image.file,
    )

    lines = [
        (
            f'<div class="{html.escape(" ".join(container_classes), quote=True)}" '
            f'data-tree-id="{html.escape(spec.identifier, quote=True)}" '
            f'style="{html.escape(container_style, quote=True)}">'
        ),
        (
            f'  <img class="tree-component__image" '
            f'src="{html.escape(image_url, quote=True)}" '
            f'alt="{html.escape(spec.image.alt, quote=True)}">'
        ),
    ]

    if mask is not None:
        lines.append(
            f'  <div class="tree-component__mask '
            f'tree-component__mask--{html.escape(mask, quote=True)}" '
            f'data-mask-id="{html.escape(mask, quote=True)}"></div>'
        )

    for group_id in heading_ids:
        group = spec.groups[group_id]
        style = _position_style(
            left=group.position.left,
            top=group.position.top,
            align=group.align,
        )
        lines.append(
            f'  <div class="tree-component__group-heading" '
            f'data-group-id="{html.escape(group_id, quote=True)}" '
            f'style="{html.escape(style, quote=True)}">'
            f"{_content_html(group.content)}</div>"
        )

    for label_id in selected_labels:
        label = spec.labels[label_id]
        style = _position_style(
            left=label.position.left,
            top=label.position.top,
            align=label.align,
        )
        lines.append(
            f'  <div class="tree-component__label" '
            f'data-label-id="{html.escape(label_id, quote=True)}" '
            f'style="{html.escape(style, quote=True)}">'
            f"{_content_html(label.content)}</div>"
        )

    lines.append("</div>")
    return "\n".join(lines)
