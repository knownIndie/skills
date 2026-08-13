#!/usr/bin/env python3
"""Validate the mechanical safety and portability rules for HTML Doc output."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

MAX_BYTES = 512 * 1024

BANNED_TAGS = {
    "applet",
    "base",
    "embed",
    "form",
    "frame",
    "frameset",
    "iframe",
    "input",
    "object",
    "select",
    "textarea",
}

BANNED_SCRIPT_PATTERNS = {
    "network request": re.compile(
        r"\b(fetch|XMLHttpRequest|WebSocket|EventSource)\s*\(|navigator\.sendBeacon\b"
    ),
    "browser storage or cookies": re.compile(
        r"\b(localStorage|sessionStorage|indexedDB|caches)\b|document\.cookie\b"
    ),
    "worker": re.compile(r"\b(?:new\s+)?(?:SharedWorker|Worker)\s*\(|serviceWorker\b"),
    "popup": re.compile(r"\bwindow\.open\s*\("),
    "automatic navigation": re.compile(
        r"\b(?:location\.(?:assign|replace)|window\.location\s*=|document\.location\s*=)"
    ),
}

LOCAL_PATH_PATTERN = re.compile(
    r"(?:file:/{1,3}|/(?:Users|home|private|var|tmp)/|(?<![A-Za-z])[A-Za-z]:[\\/])",
    re.IGNORECASE,
)

SECRET_PATTERN = re.compile(
    r"(?:sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9_]{20,}|AIza[0-9A-Za-z_-]{20,})"
)


class DocumentAudit(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.errors: list[str] = []
        self.lang: str | None = None
        self.title_depth = 0
        self.title_text: list[str] = []
        self.has_viewport = False
        self.has_script = False
        self.script_depth = 0
        self.script_text: list[str] = []
        self.external_links: list[dict[str, str]] = []

    def handle_decl(self, decl: str) -> None:
        if decl.strip().lower() != "doctype html":
            self.errors.append("Use the HTML5 doctype: <!doctype html>.")

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        values = {key.lower(): value or "" for key, value in attrs}

        if tag in BANNED_TAGS:
            self.errors.append(f"Banned element found: <{tag}>.")

        for name in values:
            if name.startswith("on"):
                self.errors.append(f"Inline event handler found: {name}.")
            if name == "srcdoc":
                self.errors.append("The srcdoc attribute is not allowed.")

        if tag == "html":
            self.lang = values.get("lang") or None

        if tag == "title":
            self.title_depth += 1

        if tag == "meta" and values.get("name", "").lower() == "viewport":
            content = values.get("content", "").replace(" ", "").lower()
            if "width=device-width" in content and "initial-scale=1" in content:
                self.has_viewport = True

        if tag == "meta" and values.get("http-equiv", "").lower() == "refresh":
            self.errors.append("Meta refresh is not allowed.")

        if tag == "link":
            self.errors.append("Linked resources are not allowed. Keep CSS and assets inline.")

        if tag == "script":
            self.has_script = True
            self.script_depth += 1
            if values.get("src"):
                self.errors.append("External scripts are not allowed.")
            if values.get("type", "").strip().lower() == "module":
                self.errors.append("Module scripts are not allowed. Use an inline classic script.")

        for attr_name in ("href", "src", "action", "poster", "data"):
            raw_url = values.get(attr_name)
            if not raw_url:
                continue
            self._audit_url(tag, attr_name, raw_url, values)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title" and self.title_depth:
            self.title_depth -= 1
        if tag == "script" and self.script_depth:
            self.script_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title_text.append(data)
        if self.script_depth:
            self.script_text.append(data)

    def _audit_url(
        self,
        tag: str,
        attr_name: str,
        raw_url: str,
        values: dict[str, str],
    ) -> None:
        url = raw_url.strip()
        lowered = url.lower()

        if lowered.startswith("javascript:"):
            self.errors.append(f"javascript: URL found in {tag}[{attr_name}].")
            return

        if LOCAL_PATH_PATTERN.search(url):
            self.errors.append(f"Local filesystem path found in {tag}[{attr_name}].")

        parsed = urlparse(url)
        if parsed.scheme == "http":
            self.errors.append(f"Insecure HTTP URL found in {tag}[{attr_name}]. Use HTTPS.")

        if tag in {"img", "source"} and attr_name == "src":
            if parsed.scheme and parsed.scheme not in {"https", "data"}:
                self.errors.append(f"Image source must use HTTPS or a data URL: {url[:80]}")

        if tag == "a" and attr_name == "href" and parsed.scheme in {"http", "https"}:
            self.external_links.append(
                {
                    "url": url,
                    "target": values.get("target", ""),
                    "rel": values.get("rel", ""),
                }
            )


def audit_file(path: Path) -> list[str]:
    errors: list[str] = []

    if not path.is_file():
        return [f"File does not exist: {path}"]
    if path.suffix.lower() != ".html":
        errors.append("Output must use the .html extension.")
    if path.stat().st_size > MAX_BYTES:
        errors.append(
            f"File is {path.stat().st_size:,} bytes. Maximum allowed size is {MAX_BYTES:,} bytes."
        )

    text = path.read_text(encoding="utf-8")
    if not re.match(r"\s*<!doctype\s+html\s*>", text, re.IGNORECASE):
        errors.append("Missing HTML5 doctype.")
    if "@import" in text:
        errors.append("CSS @import is not allowed.")
    if LOCAL_PATH_PATTERN.search(text):
        errors.append("The document contains a local filesystem path.")
    if SECRET_PATTERN.search(text):
        errors.append("The document appears to contain a secret or access token.")

    parser = DocumentAudit()
    try:
        parser.feed(text)
        parser.close()
    except Exception as exc:  # pragma: no cover
        errors.append(f"HTML parsing failed: {exc}")

    errors.extend(parser.errors)

    if not parser.lang:
        errors.append("The <html> element must include a lang attribute.")
    if not "".join(parser.title_text).strip():
        errors.append("The document must include a non-empty <title>.")
    if not parser.has_viewport:
        errors.append(
            'Missing responsive viewport: <meta name="viewport" content="width=device-width, initial-scale=1">.'
        )

    script = "\n".join(parser.script_text)
    for label, pattern in BANNED_SCRIPT_PATTERNS.items():
        if pattern.search(script):
            errors.append(f"Inline script uses banned capability: {label}.")

    for link in parser.external_links:
        rel_tokens = set(link["rel"].lower().split())
        if parser.has_script:
            if link["target"].lower() == "_blank":
                errors.append(
                    f"Scripted documents must omit target=\"_blank\": {link['url'][:80]}"
                )
        else:
            if link["target"].lower() != "_blank":
                errors.append(
                    f"Script-free external links must use target=\"_blank\": {link['url'][:80]}"
                )
            if not {"noopener", "noreferrer"}.issubset(rel_tokens):
                errors.append(
                    f"Script-free external links need rel=\"noopener noreferrer\": {link['url'][:80]}"
                )

    return list(dict.fromkeys(errors))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a self-contained HTML communication document."
    )
    parser.add_argument("file", type=Path, help="Path to the HTML file")
    args = parser.parse_args()

    errors = audit_file(args.file.expanduser().resolve())
    if errors:
        print(f"HTML validation failed with {len(errors)} issue(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    size = args.file.expanduser().resolve().stat().st_size
    print(f"HTML validation passed: {args.file} ({size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
