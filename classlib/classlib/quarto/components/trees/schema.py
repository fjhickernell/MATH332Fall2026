"""Schema loading and validation for reusable tree diagrams."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any, Mapping

import yaml


SCHEMA_VERSION = 1
HERE = Path(__file__).resolve().parent
SAFE_IDENTIFIER = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")
CSS_LENGTH = re.compile(
    r"^(?:0|-?(?:\d+(?:\.\d+)?|\.\d+)(?:%|px|em|rem|vw|vh|cqw|cqh))$"
)
ASPECT_RATIO = re.compile(r"^\d+(?:\.\d+)?\s*/\s*\d+(?:\.\d+)?$")
ALIGNMENTS = frozenset({"left", "center", "right"})
STATUSES = frozenset({"ready", "placeholder"})


class TreeSchemaError(ValueError):
    """Raised when a tree configuration does not satisfy the schema."""


class TreeNotReadyError(TreeSchemaError):
    """Raised when code attempts to render a placeholder tree."""


@dataclass(frozen=True)
class ContentSpec:
    value: str
    trusted_html: bool = False


@dataclass(frozen=True)
class PositionSpec:
    left: str
    top: str


@dataclass(frozen=True)
class ImageSpec:
    file: str
    alt: str
    aspect_ratio: str


@dataclass(frozen=True)
class DefaultsSpec:
    width: str
    font_scale: float
    label_align: str
    group_align: str


@dataclass(frozen=True)
class LabelSpec:
    identifier: str
    content: ContentSpec
    position: PositionSpec
    align: str


@dataclass(frozen=True)
class GroupSpec:
    identifier: str
    content: ContentSpec
    labels: tuple[str, ...]
    position: PositionSpec
    align: str


@dataclass(frozen=True)
class MaskSpec:
    identifier: str
    description: str


@dataclass(frozen=True)
class TreeSpec:
    schema_version: int
    identifier: str
    status: str
    source_path: Path | None
    image: ImageSpec | None
    defaults: DefaultsSpec | None
    groups: Mapping[str, GroupSpec]
    labels: Mapping[str, LabelSpec]
    masks: Mapping[str, MaskSpec]


def _error(path: str, message: str) -> TreeSchemaError:
    return TreeSchemaError(f"{path}: {message}")


def _require_mapping(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise _error(path, "must be a mapping")
    return value


def _check_fields(
    value: Mapping[str, Any],
    *,
    path: str,
    required: set[str],
    optional: set[str] | None = None,
) -> None:
    optional = optional or set()
    missing = required - set(value)
    unknown = set(value) - required - optional
    if missing:
        raise _error(path, f"missing required fields: {sorted(missing)}")
    if unknown:
        raise _error(path, f"unknown fields: {sorted(unknown)}")


def _require_string(value: Any, path: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise _error(path, "must be a nonempty string")
    return value


def _safe_identifier(value: Any, path: str) -> str:
    identifier = _require_string(value, path)
    if not SAFE_IDENTIFIER.fullmatch(identifier):
        raise _error(
            path,
            "must match ^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$",
        )
    return identifier


def _css_length(value: Any, path: str) -> str:
    text = _require_string(value, path)
    if not CSS_LENGTH.fullmatch(text):
        raise _error(path, f"unsupported CSS length {text!r}")
    return text


def _alignment(value: Any, path: str) -> str:
    text = _require_string(value, path)
    if text not in ALIGNMENTS:
        raise _error(path, f"must be one of {sorted(ALIGNMENTS)}")
    return text


def _positive_number(value: Any, path: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise _error(path, "must be a number")
    number = float(value)
    if number <= 0:
        raise _error(path, "must be positive")
    return number


def _content(value: Mapping[str, Any], path: str) -> ContentSpec:
    present = {"text", "html"} & set(value)
    if len(present) != 1:
        raise _error(path, "must define exactly one of 'text' or 'html'")
    field = next(iter(present))
    return ContentSpec(
        value=_require_string(value[field], f"{path}.{field}"),
        trusted_html=field == "html",
    )


def _position(value: Any, path: str) -> PositionSpec:
    position = _require_mapping(value, path)
    _check_fields(
        position,
        path=path,
        required={"left", "top"},
    )
    return PositionSpec(
        left=_css_length(position["left"], f"{path}.left"),
        top=_css_length(position["top"], f"{path}.top"),
    )


def _image(value: Any, path: str) -> ImageSpec:
    image = _require_mapping(value, path)
    _check_fields(
        image,
        path=path,
        required={"file", "alt", "aspect_ratio"},
    )
    filename = _require_string(image["file"], f"{path}.file")
    if Path(filename).is_absolute():
        raise _error(f"{path}.file", "must be relative to the tree configuration")
    ratio = _require_string(image["aspect_ratio"], f"{path}.aspect_ratio")
    if not ASPECT_RATIO.fullmatch(ratio):
        raise _error(f"{path}.aspect_ratio", "must look like '4 / 3'")
    return ImageSpec(
        file=filename,
        alt=_require_string(image["alt"], f"{path}.alt"),
        aspect_ratio=ratio,
    )


def _defaults(value: Any, path: str) -> DefaultsSpec:
    defaults = _require_mapping(value, path)
    _check_fields(
        defaults,
        path=path,
        required={"width", "font_scale", "label_align", "group_align"},
    )
    return DefaultsSpec(
        width=_css_length(defaults["width"], f"{path}.width"),
        font_scale=_positive_number(
            defaults["font_scale"],
            f"{path}.font_scale",
        ),
        label_align=_alignment(
            defaults["label_align"],
            f"{path}.label_align",
        ),
        group_align=_alignment(
            defaults["group_align"],
            f"{path}.group_align",
        ),
    )


def _labels(
    value: Any,
    *,
    default_align: str,
    path: str,
) -> dict[str, LabelSpec]:
    raw_labels = _require_mapping(value, path)
    result: dict[str, LabelSpec] = {}
    for raw_identifier, raw_label in raw_labels.items():
        identifier = _safe_identifier(raw_identifier, f"{path} key")
        label_path = f"{path}.{identifier}"
        label = _require_mapping(raw_label, label_path)
        _check_fields(
            label,
            path=label_path,
            required={"position"},
            optional={"text", "html", "align"},
        )
        result[identifier] = LabelSpec(
            identifier=identifier,
            content=_content(label, label_path),
            position=_position(label["position"], f"{label_path}.position"),
            align=_alignment(
                label.get("align", default_align),
                f"{label_path}.align",
            ),
        )
    return result


def _groups(
    value: Any,
    *,
    labels: Mapping[str, LabelSpec],
    default_align: str,
    path: str,
) -> dict[str, GroupSpec]:
    raw_groups = _require_mapping(value, path)
    result: dict[str, GroupSpec] = {}
    for raw_identifier, raw_group in raw_groups.items():
        identifier = _safe_identifier(raw_identifier, f"{path} key")
        group_path = f"{path}.{identifier}"
        group = _require_mapping(raw_group, group_path)
        _check_fields(
            group,
            path=group_path,
            required={"labels", "position"},
            optional={"text", "html", "align"},
        )
        raw_label_ids = group["labels"]
        if not isinstance(raw_label_ids, list):
            raise _error(f"{group_path}.labels", "must be a list")
        label_ids: list[str] = []
        for index, raw_label_id in enumerate(raw_label_ids):
            label_id = _safe_identifier(
                raw_label_id,
                f"{group_path}.labels[{index}]",
            )
            if label_id not in labels:
                raise _error(
                    f"{group_path}.labels[{index}]",
                    f"references undefined label {label_id!r}",
                )
            label_ids.append(label_id)
        result[identifier] = GroupSpec(
            identifier=identifier,
            content=_content(group, group_path),
            labels=tuple(label_ids),
            position=_position(group["position"], f"{group_path}.position"),
            align=_alignment(
                group.get("align", default_align),
                f"{group_path}.align",
            ),
        )
    return result


def _masks(value: Any, path: str) -> dict[str, MaskSpec]:
    raw_masks = _require_mapping(value, path)
    result: dict[str, MaskSpec] = {}
    for raw_identifier, raw_mask in raw_masks.items():
        identifier = _safe_identifier(raw_identifier, f"{path} key")
        mask_path = f"{path}.{identifier}"
        mask = _require_mapping(raw_mask, mask_path)
        _check_fields(
            mask,
            path=mask_path,
            required={"description"},
        )
        result[identifier] = MaskSpec(
            identifier=identifier,
            description=_require_string(
                mask["description"],
                f"{mask_path}.description",
            ),
        )
    return result


def validate_tree(
    data: Any,
    *,
    source_path: str | Path | None = None,
    require_artwork: bool = False,
) -> TreeSpec:
    """Validate parsed YAML data and return a tree specification."""

    root = _require_mapping(data, "tree")
    _check_fields(
        root,
        path="tree",
        required={"schema_version", "id", "status"},
        optional={"image", "defaults", "groups", "labels", "masks"},
    )

    version = root["schema_version"]
    if isinstance(version, bool) or not isinstance(version, int):
        raise _error("tree.schema_version", "must be an integer")
    if version != SCHEMA_VERSION:
        raise _error(
            "tree.schema_version",
            f"unsupported version {version}; expected {SCHEMA_VERSION}",
        )

    identifier = _safe_identifier(root["id"], "tree.id")
    status = _require_string(root["status"], "tree.status")
    if status not in STATUSES:
        raise _error("tree.status", f"must be one of {sorted(STATUSES)}")

    resolved_source = Path(source_path).resolve() if source_path else None

    if status == "placeholder":
        unexpected = {"image", "defaults", "groups", "labels", "masks"} & set(root)
        if unexpected:
            raise _error(
                "tree",
                f"placeholder tree cannot define {sorted(unexpected)}",
            )
        return TreeSpec(
            schema_version=version,
            identifier=identifier,
            status=status,
            source_path=resolved_source,
            image=None,
            defaults=None,
            groups={},
            labels={},
            masks={},
        )

    ready_fields = {"image", "defaults", "groups", "labels", "masks"}
    missing = ready_fields - set(root)
    if missing:
        raise _error("tree", f"ready tree is missing {sorted(missing)}")

    image = _image(root["image"], "tree.image")
    defaults = _defaults(root["defaults"], "tree.defaults")
    labels = _labels(
        root["labels"],
        default_align=defaults.label_align,
        path="tree.labels",
    )
    groups = _groups(
        root["groups"],
        labels=labels,
        default_align=defaults.group_align,
        path="tree.groups",
    )
    masks = _masks(root["masks"], "tree.masks")

    if require_artwork:
        if resolved_source is None:
            raise _error("tree.image.file", "cannot resolve artwork without source_path")
        artwork = (resolved_source.parent / image.file).resolve()
        component_root = HERE.resolve()
        if component_root not in artwork.parents:
            raise _error("tree.image.file", "must resolve inside the trees component")
        if not artwork.is_file():
            raise _error("tree.image.file", f"artwork does not exist: {artwork}")

    return TreeSpec(
        schema_version=version,
        identifier=identifier,
        status=status,
        source_path=resolved_source,
        image=image,
        defaults=defaults,
        groups=groups,
        labels=labels,
        masks=masks,
    )


def load_tree_file(path: str | Path) -> TreeSpec:
    """Load and validate a tree configuration from an explicit YAML path."""

    source = Path(path).resolve()
    if not source.is_file():
        raise TreeSchemaError(f"tree configuration does not exist: {source}")
    data = yaml.safe_load(source.read_text(encoding="utf-8"))
    return validate_tree(data, source_path=source, require_artwork=True)


def load_tree(identifier: str) -> TreeSpec:
    """Load a registered tree configuration by safe identifier."""

    safe_identifier = _safe_identifier(identifier, "tree identifier")
    return load_tree_file(HERE / safe_identifier / "tree.yml")
