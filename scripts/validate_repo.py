#!/usr/bin/env python3
"""Validate local Markdown links, required files, metadata, and placeholders."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "CONTENT_LICENSE.md",
    "product.yml",
    "docs/PACKAGE_MAP.md",
    "docs/STUDY_PATHS.md",
    "docs/ERRATA.md",
    "samples/dsa/TwoSumThreeApproaches.java",
]

PLACEHOLDERS = [
    "YOUR_GUMROAD_URL",
    "YOUR_GITHUB_USERNAME",
    "YOUR_SUPPORT_EMAIL",
    "YOUR_SECURITY_EMAIL",
]

LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def validate_required_files() -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")
    return errors


def validate_local_links() -> list[str]:
    errors: list[str] = []
    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(text):
            target = raw_target.strip().split()[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            resolved = (markdown.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"Link escapes repository: {markdown.relative_to(ROOT)} -> {target}")
                continue
            if not resolved.exists():
                errors.append(f"Broken local link: {markdown.relative_to(ROOT)} -> {target}")
    return errors


def find_placeholders() -> list[str]:
    warnings: list[str] = []
    excluded = {Path("scripts/validate_repo.py"), Path("docs/CUSTOMIZE_BEFORE_PUBLISHING.md")}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        relative = path.relative_to(ROOT)
        if relative in excluded:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for placeholder in PLACEHOLDERS:
            if placeholder in text:
                warnings.append(f"Placeholder remains in {relative}: {placeholder}")
    return warnings


def validate_product_metadata() -> list[str]:
    errors: list[str] = []
    text = (ROOT / "product.yml").read_text(encoding="utf-8")
    expected = {
        "pdf_count: 17",
        "pdf_pages: 1049",
        "package_file_count: 36",
        "sql_lab_file_count: 8",
        "standalone_diagram_count: 10",
    }
    for entry in sorted(expected):
        if entry not in text:
            errors.append(f"product.yml is missing expected metadata: {entry}")
    return errors


def main() -> int:
    errors = []
    errors.extend(validate_required_files())
    errors.extend(validate_local_links())
    errors.extend(validate_product_metadata())
    warnings = find_placeholders()

    for warning in warnings:
        print(f"WARNING: {warning}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"Validation passed with {len(warnings)} placeholder warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
