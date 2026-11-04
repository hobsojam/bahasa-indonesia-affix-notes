"""
Build the study guide into dist/book.html, dist/*.pdf, and dist/*.epub.

Usage:
    python scripts/build_book.py            # build everything
    python scripts/build_book.py --format epub
    python scripts/build_book.py --format pdf

See scripts/README.md for prerequisites and what each output needs.
"""
import argparse
import datetime
import re
import subprocess
import sys
import zipfile
from pathlib import Path

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
BOOK_DIR = ROOT / "book"
OUT_DIR = ROOT / "dist"

TITLE = "Indonesian Affixation: A Study Guide"
SUBTITLE = "An AI-assisted draft \u2014 see Appendix C before relying on specific claims"

md = MarkdownIt("gfm-like", {"html": True})


def slug(s):
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[\s_]+", "-", s)


def discover_files():
    """Every book/NN-slug.md file, in filename order. Add a new chapter by
    dropping a new NN-slug.md into book/ — no list to edit here."""
    return sorted(BOOK_DIR.glob("*.md"), key=lambda p: p.name)


def load_chapters():
    chapters = []
    for path in discover_files():
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        title = lines[0].lstrip("#").strip()
        body_html = md.render("\n".join(lines[1:]))
        # Force <details> open: Kindle/print renderers don't support the
        # interactive click-to-expand that <details> relies on elsewhere.
        body_html = body_html.replace("<details>", '<details open="open">')
        chapters.append(
            {"id": slug(path.stem), "title": title, "html": body_html, "file": path.name}
        )
    return chapters


HTML_CSS = """
body { font-family: Georgia, 'Times New Roman', serif; line-height: 1.5; color: #222; }
h1 { font-size: 1.6em; border-bottom: 2px solid #444; padding-bottom: 0.2em; }
h2 { font-size: 1.25em; margin-top: 1.6em; color: #333; }
h3 { font-size: 1.05em; margin-top: 1.3em; color: #333; }
code { background: #f1f1ef; padding: 0 3px; font-family: Consolas, monospace; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 0.92em; }
th, td { border: 1px solid #bbb; padding: 4px 8px; text-align: left; vertical-align: top; }
th { background: #eee; }
blockquote { margin: 0.8em 0 0.8em 1.2em; padding-left: 0.8em; border-left: 3px solid #ccc;
             color: #333; font-style: italic; }
blockquote em, blockquote strong { font-style: normal; }
details { margin: 0.8em 0; padding: 0.6em 1em; background: #f7f6f2; border: 1px solid #ddd; }
summary { font-weight: bold; cursor: default; }
hr { border: none; border-top: 1px solid #ccc; margin: 1.5em 0; }
.chapter { page-break-before: always; }
.titlepage { text-align: center; margin-top: 35%; page-break-after: always; }
.titlepage h1 { border: none; font-size: 2.2em; }
.toc ul { list-style: none; padding-left: 1em; }
.toc li { margin: 0.3em 0; }
.toc a { text-decoration: none; color: #223; }
"""


def build_html():
    chapters = load_chapters()
    toc_items = "\n".join(f'<li><a href="#{c["id"]}">{c["title"]}</a></li>' for c in chapters)
    parts = [
        f"<!DOCTYPE html><html><head><meta charset='utf-8'>"
        f"<title>{TITLE}</title><style>{HTML_CSS}</style></head><body>",
        f'<div class="titlepage"><h1>{TITLE}</h1><p>{SUBTITLE}</p></div>',
        f'<section class="chapter toc"><h1>Contents</h1><ul>{toc_items}</ul></section>',
    ]
    for c in chapters:
        parts.append(f'<section class="chapter" id="{c["id"]}">{c["html"]}</section>')
    parts.append("</body></html>")
    out = OUT_DIR / "book.html"
    out.write_text("\n".join(parts), encoding="utf-8")
    return out


CHROME_CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]


def find_browser():
    for c in CHROME_CANDIDATES:
        if Path(c).exists():
            return c
    return None


def build_pdf(html_path):
    browser = find_browser()
    if not browser:
        print(
            "No Edge/Chrome install found in the usual locations. "
            "Install one, or edit CHROME_CANDIDATES in this script, then re-run "
            "with --format pdf.",
            file=sys.stderr,
        )
        return None
    pdf_path = OUT_DIR / "Indonesian-Affixation-Study-Guide.pdf"
    subprocess.run(
        [
            browser,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            str(html_path),
        ],
        check=True,
        capture_output=True,
    )
    return pdf_path


EPUB_CSS = """
body { font-family: serif; line-height: 1.4; }
h1 { font-size: 1.4em; }
h2 { font-size: 1.15em; }
h3 { font-size: 1.0em; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #999; padding: 3px 6px; font-size: 0.9em; }
blockquote { margin: 0.6em 0 0.6em 1em; font-style: italic; }
details { background: #f3f2ee; padding: 0.4em 0.8em; margin: 0.6em 0; }
"""


def build_epub():
    chapters = load_chapters()
    epub_path = OUT_DIR / "indonesian-affixation-study-guide.epub"
    epub_path.unlink(missing_ok=True)

    manifest_items, spine_items, ncx_items = [], [], []
    for i, c in enumerate(chapters):
        fname = f"chap{i:02d}.xhtml"
        c["fname"] = fname
        c["xhtml"] = (
            "<?xml version='1.0' encoding='utf-8'?>\n<!DOCTYPE html>\n"
            "<html xmlns='http://www.w3.org/1999/xhtml'>\n"
            f"<head><title>{c['title']}</title>"
            "<link rel='stylesheet' type='text/css' href='style.css'/></head>\n"
            f"<body>{c['html']}</body></html>"
        )
        manifest_items.append(f'<item id="{c["id"]}" href="{fname}" media-type="application/xhtml+xml"/>')
        spine_items.append(f'<itemref idref="{c["id"]}"/>')
        ncx_items.append(
            f'<navPoint id="navpt-{i}" playOrder="{i+1}">'
            f'<navLabel><text>{c["title"]}</text></navLabel><content src="{fname}"/></navPoint>'
        )

    nav_xhtml = (
        "<?xml version='1.0' encoding='utf-8'?>\n<!DOCTYPE html>\n"
        "<html xmlns='http://www.w3.org/1999/xhtml' xmlns:epub='http://www.idpf.org/2007/ops'>\n"
        "<head><title>Contents</title></head><body>\n<nav epub:type='toc'><h1>Contents</h1><ol>\n"
        + "\n".join(f'<li><a href="{c["fname"]}">{c["title"]}</a></li>' for c in chapters)
        + "\n</ol></nav></body></html>"
    )

    content_opf = f"""<?xml version='1.0' encoding='utf-8'?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="bookid" version="3.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">urn:uuid:indonesian-affixation-study-guide</dc:identifier>
    <dc:title>{TITLE}</dc:title>
    <dc:language>en</dc:language>
    <dc:creator>Drafted with AI assistance (see Appendix C)</dc:creator>
    <meta property="dcterms:modified">{datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}</meta>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="css" href="style.css" media-type="text/css"/>
    {''.join(manifest_items)}
  </manifest>
  <spine toc="ncx">{''.join(spine_items)}</spine>
</package>"""

    toc_ncx = f"""<?xml version='1.0' encoding='utf-8'?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head><meta name="dtb:uid" content="urn:uuid:indonesian-affixation-study-guide"/></head>
  <docTitle><text>{TITLE}</text></docTitle>
  <navMap>{''.join(ncx_items)}</navMap>
</ncx>"""

    with zipfile.ZipFile(epub_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr(
            "META-INF/container.xml",
            "<?xml version='1.0' encoding='utf-8'?>\n"
            "<container xmlns='urn:oasis:names:tc:opendocument:xmlns:container' version='1.0'>"
            "<rootfiles><rootfile full-path='OEBPS/content.opf' "
            "media-type='application/oebps-package+xml'/></rootfiles></container>",
        )
        z.writestr("OEBPS/content.opf", content_opf)
        z.writestr("OEBPS/toc.ncx", toc_ncx)
        z.writestr("OEBPS/nav.xhtml", nav_xhtml)
        z.writestr("OEBPS/style.css", EPUB_CSS)
        for c in chapters:
            z.writestr(f"OEBPS/{c['fname']}", c["xhtml"])
    return epub_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--format", choices=["all", "html", "pdf", "epub"], default="all",
        help="Which output(s) to build (default: all)",
    )
    args = parser.parse_args()

    OUT_DIR.mkdir(exist_ok=True)

    if args.format in ("html", "pdf", "all"):
        html_path = build_html()
        print("HTML:", html_path)
        if args.format in ("pdf", "all"):
            pdf_path = build_pdf(html_path)
            if pdf_path:
                print("PDF: ", pdf_path)

    if args.format in ("epub", "all"):
        epub_path = build_epub()
        print("EPUB:", epub_path)


if __name__ == "__main__":
    main()
