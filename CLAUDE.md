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

- `pembilas/data/affixes.json` (in the gitignored reference clone of
  https://github.com/hobsojam/pembilas) is the canonical list of affixes
  already identified, with their core function and usage notes. Check it
  before writing a new chapter so terminology and affix IDs stay
  consistent with that tool.
- `pembilas/data/words.json` and `pembilas/data/annotations.json` hold
  vetted root/derived-form/gloss triples — prefer pulling example words
  from there over inventing new ones, since they've already been checked.
- If `pembilas/` is missing (fresh checkout), re-clone it from
  https://github.com/hobsojam/pembilas for reference. Never commit it into
  this repo (it's gitignored on purpose — it's that project's own history).

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
- Don't invent example words freely — prefer roots already in
  `pembilas/data/words.json`, or other well-attested, high-frequency
  roots.
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
