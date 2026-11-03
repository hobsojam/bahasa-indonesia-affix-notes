# CLAUDE.md — Indonesian Affixation Study Guide

This is a content-writing project, not a software project. There's no
build/test step; the deliverable is markdown chapters.

## What this project is

A study guide on Bahasa Indonesia's affix system (prefixes, suffixes,
circumfixes, infixes), for an intermediate-level learner. Scope is
deliberately narrow: affixation only, not a full grammar/vocab course.
See `book/00-outline.md` for the chapter list and status.

## Setup

No install or build step. Chapters are plain markdown; there's nothing to
compile or run. The only external dependency is the `pembilas/` reference
clone described below, needed only for sourcing example data.

## Source of truth

Prefer the sources pembilas itself draws from over pembilas's own data,
wherever possible — see `pembilas/data/SOURCES.md` for exactly what each
file is derived from and its known gaps.

- **Grammar facts and rules**: use standard Indonesian reference grammars
  directly (the kind of material `pembilas/data/affixes.json` says it's
  "based on" — e.g. Sneddon's *Indonesian Reference Grammar*, Alwi et
  al.'s *Tata Bahasa Baku Bahasa Indonesia*), not pembilas's distilled
  one-line summaries.
- **Word meanings and example sentences**: prefer Wiktionary's Indonesian
  entries or KBBI over `pembilas/data/words.json`, which is a
  machine-inverted FreeDict/WikDict derivative with a documented,
  incomplete error-review process (their own gloss-review notes: roughly
  1 in 4 flagged glosses turn out to be correct-but-differently-phrased —
  implying most *flagged* ones are genuine errors, and that's only the
  flagged subset).

`pembilas/data/affixes.json` and `annotations.json` (in the gitignored
reference clone of https://github.com/hobsojam/pembilas) are still worth
checking, but as a **consistency anchor and secondary corroboration**,
not primary authority:

- `affixes.json` — use its affix IDs/labels so this book doesn't invent
  conflicting terminology for an affix it already models. Its 18-affix
  list isn't exhaustive: no infixes, no particles (*-kah*, *-pun*,
  *-tah*). Chapters outside that scope need to be sourced from standard
  grammar references directly, not from pembilas.
- `annotations.json` — hand-curated, but coverage is partial and "grows
  incrementally" per its own docs. An unannotated root/affix combination
  means "not yet checked," not "invalid." Treat a present annotation as
  one corroborating data point, not the final word — a form absent from
  a grammar reference and present only here is worth double-checking
  elsewhere before use.

If `pembilas/` is missing (fresh checkout), re-clone it from
https://github.com/hobsojam/pembilas for reference. Never commit it into
this repo (it's gitignored on purpose — it's that project's own
history).

## Chapter template

Established in `book/05-passive-di-ter.md`. Each chapter should follow
this shape:

1. **Overview** — one or two paragraphs, plus a quick comparison table if
   2+ affixes are in play.
2. **Forms** — how the affix attaches, including any phonological rule
   (nasal assimilation, r-initial dissimilation, etc.), with a
   before/after table.
3. **Usage notes** — numbered subsections, one per distinct
   meaning/function of the affix.
4. **"Trap" callouts** — explicitly flag anywhere a form looks like it
   means one thing but means another (e.g. *ter-* as superlative vs.
   passive), or anywhere English intuition would mislead.
5. **Decision table** — when 2+ affixes compete for the same semantic
   space, give a side-by-side table for choosing between them.
6. **Practice** — 2-4 items, with the answer key in a collapsible
   `<details>` block so it doesn't spoil the exercise.

## Accuracy guardrails

- This is reference-grammar material: facts need to be *right*, not just
  plausible.
- Flag lexically idiosyncratic rules explicitly (e.g. "which roots take
  *pe-...-an* vs *per-...-an* is lexically determined, not predictable").
  Don't present a word-specific exception as if it were the general rule.
- Don't invent example words freely — prefer well-attested, high-
  frequency roots (check Wiktionary/KBBI if unsure a form is real). A
  root also appearing in `pembilas/data/annotations.json` is a bonus
  corroboration, not a requirement.
- When unsure whether a specific gloss or derived form is natural/
  attested, say so rather than asserting confidently.

## Style

- Indonesian words/morphemes in italics; English glosses in quotes.
- No em-dashes (user-wide writing preference — use commas, periods, or
  separate sentences instead).
- Write and review one chapter at a time. Don't batch-write several
  chapters before the user has signed off on the current one.

## File naming

`book/NN-short-slug.md`, where `NN` is the two-digit chapter number
matching `book/00-outline.md`.
