# Building the PDF and EPUB

`build_book.py` turns every `book/NN-slug.md` file into:

- `dist/book.html` — the whole book as one HTML file (also the input the
  PDF step prints from)
- `dist/Indonesian-Affixation-Study-Guide.pdf`
- `dist/indonesian-affixation-study-guide.epub` — for Kindle (via
  [Send to Kindle](https://www.amazon.com/sendtokindle), which converts
  EPUB automatically) or any other e-reader

`dist/` is gitignored — these are build outputs, regenerated from the
`book/*.md` files, not checked in.

## Prerequisites

- Python 3, with `pip install -r scripts/requirements.txt`
  (`markdown-it-py` and `mdit-py-plugins`, for Markdown→HTML with
  GFM-style tables and raw-HTML passthrough — the book's `<details>`
  answer keys rely on the latter; `linkify-it-py`, since the `"gfm-like"`
  preset turns on autolinking and raises `ModuleNotFoundError` without it).
- Microsoft Edge or Google Chrome installed, for the PDF step only (it
  shells out to headless Chromium's `--print-to-pdf`). The script checks
  the usual Windows install paths automatically; if yours isn't found,
  edit `CHROME_CANDIDATES` at the top of `build_book.py`.
- No LaTeX, Pandoc, or Calibre needed — everything else is stdlib
  (`zipfile` for the EPUB) or the one dependency above.

## Usage

From the repo root:

```
python scripts/build_book.py              # builds HTML + PDF + EPUB
python scripts/build_book.py --format pdf
python scripts/build_book.py --format epub
python scripts/build_book.py --format html
```

## As the book evolves

Chapter files are picked up automatically (`BOOK_DIR.glob("*.md")`,
sorted by filename) — add a new `book/NN-slug.md` and it's included on
the next build with no edit to this script required. The book's first
line (`# Chapter N: Title`) becomes that chapter's title in the TOC/EPUB
nav; everything else is rendered as-is.

## Known rendering quirks

- **`<details>` is forced open.** The book's practice-answer-key
  `<details><summary>` blocks are interactive click-to-expand in a
  browser, but neither a printed PDF nor most e-readers support that, so
  the build forces them open (visible by default) in both outputs.
- **The `§` section-sign character can extract as a replacement glyph
  (`�`) if you copy-paste from the PDF or run `pdftotext` on it.** This
  was checked during development: the source Markdown and the
  intermediate `book.html` are both correctly UTF-8 (`\xc2\xa7`) — the
  mis-mapping happens inside Chromium's PDF text layer (a ToUnicode/CMap
  quirk specific to that character in its print-to-PDF path), not in the
  book's content. It's cosmetic: the glyph itself renders fine visually;
  only programmatic text-extraction from the PDF is affected. Rendering
  via the EPUB path doesn't have this problem. Not something the content
  side of this project can fix; worth re-checking if you ever change the
  PDF-generation approach.
- The PDF has no page numbers or running headers — headless Chromium's
  `--print-to-pdf` CLI doesn't expose CSS Paged Media margin boxes for
  that. Possible to add later via the DevTools `Page.printToPDF`
  protocol directly (with a header/footer template) instead of the
  plain CLI flag, if it's worth the extra complexity.
- Internal `§5.4`-style cross-references are plain text, not hyperlinks,
  in both outputs. Making them clickable would need resolving each
  reference to its target chapter's anchor — not implemented.
