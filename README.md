# Bahasa Indonesia Affixation — Study Guide

A focused study guide on the Indonesian affix system: prefixes, suffixes,
circumfixes, and infixes. This is **not** a full language course — word
order, vocabulary, pronunciation, etc. are out of scope by design.

## Structure

- `book/00-outline.md` — the full chapter list and current status of each
  chapter (drafted / not started).
- `book/NN-short-slug.md` — individual chapters, in reading order.

## Status

All 13 chapters and all four appendices are drafted — see
`book/00-outline.md` for the full chapter list and `book/16-appendix-c-ai-disclosure.md`
for a disclosure of how the content was produced (AI-assisted) and its
known reliability caveats. Every chapter and appendix has since been
through one accuracy-review pass (checking grammar claims and example
words against standard references, Wiktionary, and KBBI), which found
and corrected five errors — see Appendix C for specifics. That's still
not a native-speaker check; treat the content as a reviewed draft, not
a finished, independently verified one.

## Building a PDF or EPUB

`scripts/build_book.py` assembles the chapters into `dist/book.html`,
a PDF, and an EPUB (for Kindle/e-readers). See `scripts/README.md` for
prerequisites, usage, and known rendering quirks.

## Level & scope

Pitched at an intermediate learner: basic Indonesian vocabulary and
grammar are assumed, so explanations don't re-derive things like basic
word order or pronoun use from scratch.

## Related tools

[pembilas](https://github.com/hobsojam/pembilas) is a separate,
interactive affix lookup/derivation tool for Indonesian. A reference
clone lives in `pembilas/` here (gitignored — it's that project's own
repo, not part of this one) so chapters can stay consistent with its
vetted affix list and example data.
