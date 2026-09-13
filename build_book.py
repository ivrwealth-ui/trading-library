#!/usr/bin/env python3
"""
Generic book builder. Builds markdown + styled HTML + PDF for any book folder
containing a `frontmatter.md` and a `chapters/*.md` set.

Usage: python3 build_book.py /path/to/book/folder
"""
import re
import sys
from pathlib import Path

import markdown


def sanitize(name: str) -> str:
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"\s+", "-", name.strip())
    return name


def parse_frontmatter(front: Path):
    text = front.read_text(encoding="utf-8")
    title = subtitle = ""
    for line in text.splitlines():
        s = line.strip()
        if not title and s.startswith("# "):
            title = s[2:].strip()
        elif not subtitle and s.startswith("## "):
            subtitle = s[3:].strip()
        if title and subtitle:
            break
    return title, subtitle


CSS = """
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 11pt; line-height: 1.62; color: #1a1d21; margin: 0;
}
.cover {
  height: 100vh; page-break-after: always;
  display: flex; flex-direction: column; justify-content: center;
  padding: 3cm 2.5cm; background: #0d1715; color: #e8f0ee;
}
.cover .rule { width: 64px; height: 4px; background: #2dd4bf; margin-bottom: 2.2rem; }
.cover h1 { font-size: 38pt; line-height: 1.08; font-weight: 600; color: #fff; margin: 0 0 1.4rem; letter-spacing: -0.5px; }
.cover .subtitle { font-size: 15pt; color: #9fb5ae; line-height: 1.5; max-width: 34em; }
.cover .pub { margin-top: 3rem; font-size: 11pt; letter-spacing: 0.14em; text-transform: uppercase; color: #2dd4bf; }
.cover .ednote { margin-top: 0.6rem; font-size: 9pt; color: #6c817b; }
h1 { font-size: 23pt; font-weight: 600; color: #0f172a; page-break-before: always; margin: 0 0 1.1rem; padding-bottom: 0.4rem; border-bottom: 2px solid #2dd4bf; }
h2 { font-size: 15.5pt; font-weight: 600; color: #0f766e; margin: 1.6rem 0 0.6rem; }
h3 { font-size: 12.5pt; font-weight: 600; color: #1a1d21; margin: 1.2rem 0 0.4rem; }
p { margin: 0.5rem 0; }
strong { color: #0f172a; }
em { color: #334155; }
a { color: #0f766e; text-decoration: none; }
hr { border: none; border-top: 1px solid #e2e8f0; margin: 2rem 0; }
ul, ol { margin: 0.5rem 0 0.8rem; padding-left: 1.5rem; }
li { margin: 0.25rem 0; }
code { font-family: 'SF Mono', Menlo, Consolas, monospace; font-size: 9pt; background: #f1f5f9; padding: 1px 5px; border-radius: 3px; color: #0f766e; }
pre { background: #0f172a; color: #e2e8f0; padding: 0.9rem 1.1rem; border-radius: 6px; font-size: 9pt; line-height: 1.5; white-space: pre-wrap; word-wrap: break-word; }
pre code { background: none; color: inherit; padding: 0; }
blockquote { border-left: 3px solid #2dd4bf; background: #f0fdfa; margin: 0.8rem 0; padding: 0.7rem 1rem; color: #0f3d37; font-style: italic; border-radius: 0 4px 4px 0; }
blockquote p { margin: 0.3rem 0; }
table { border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 9.5pt; page-break-inside: avoid; }
th, td { border: 1px solid #dbe3e8; padding: 5px 8px; text-align: left; vertical-align: top; }
th { background: #0f766e; color: #fff; font-weight: 600; }
tr:nth-child(even) td { background: #f8fafc; }
h1:first-of-type { page-break-before: auto; }
h2#important-disclaimer, h2#how-to-read-this-book, h2#table-of-contents { page-break-before: always; }
"""


def build(book_dir: Path):
    front = book_dir / "frontmatter.md"
    chapters_dir = book_dir / "chapters"
    title, subtitle = parse_frontmatter(front)

    parts = [front.read_text(encoding="utf-8")]
    for f in sorted(chapters_dir.glob("*.md")):
        parts.append(f.read_text(encoding="utf-8"))
    md_text = "\n\n".join(parts)

    body = markdown.markdown(md_text, extensions=["extra", "sane_lists", "toc"])
    cover = (
        f'<section class="cover"><div class="rule"></div>'
        f'<h1>{title}</h1><div class="subtitle">{subtitle}</div>'
        f'<div class="pub">Published by StratLab</div>'
        f'<div class="ednote">Educational content only — not investment advice. StratLab is not SEBI-registered.</div>'
        f'</section>'
    )
    html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{cover}{body}</body></html>"

    stem = sanitize(title)
    md_out = book_dir / f"{stem}.md"
    html_out = book_dir / f"{stem}.html"
    pdf_out = book_dir / f"{stem}.pdf"
    md_out.write_text(md_text, encoding="utf-8")

    tmp = book_dir / "_book.html"
    tmp.write_text(html, encoding="utf-8")

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(tmp.as_uri())
        page.pdf(
            path=str(pdf_out), format="A4",
            margin={"top": "2cm", "bottom": "1.8cm", "left": "1.9cm", "right": "1.9cm"},
            display_header_footer=True,
            header_template="<div></div>",
            footer_template=(
                '<div style="font-size:8px; color:#94a3b8; width:100%; padding:0 1.9cm; text-align:center;">'
                '<span class="pageNumber"></span> / <span class="totalPages"></span></div>'
            ),
            print_background=True,
        )
        browser.close()
    html_out.write_text(html, encoding="utf-8")
    tmp.unlink(missing_ok=True)

    pages = pdf_out.stat().st_size
    print(f"[{book_dir.name}] '{title}' -> {md_out.name} ({len(md_text.split())} words), {pdf_out.name} ({pages//1024} KB)")


if __name__ == "__main__":
    for arg in sys.argv[1:] or ["."]:
        build(Path(arg).resolve())
