# Appendix C: AI Assistance & Reliability Notes

This book is a personal study guide, not a published or commercially
distributed work. It isn't subject to the EU AI Act's transparency
obligations for AI-generated content (which target things like
published synthetic media and deployed AI systems interacting with the
public). This appendix exists anyway, in that regulation's spirit:
disclosing how the content was produced, and being specific about where
it's reliable and where it isn't, rather than presenting AI-drafted
grammar claims as if they carried the authority of a vetted textbook.

## How this book was produced

Chapters 1, 2, 4, 6–13, and this appendix were drafted by Claude
(Anthropic's AI assistant, model Sonnet 5, via Claude Code) at the
project owner's direction, in a single drafting pass per chapter, from
the owner's outline (`00-outline.md`) and the project's own sourcing
rules (`CLAUDE.md`). Chapters 3 and 5 were drafted earlier in the
project under the same process. No chapter was independently reviewed
line-by-line by a second source (human or otherwise) before being
committed. The project owner directed scope and structure and reviewed
the result at the chapter level, but the specific grammatical claims,
example sentences, and glosses below should be treated as a
knowledgeable-but-unverified first draft, not a proofread one.

A follow-up pass, after the project owner asked what was still missing
from the completed first draft, added two new sections that hadn't
existed anywhere in the original outline — Ch. 5 §5.4 (originally
labeled Passive Type 1; corrected below) and Ch. 4 §4.6 (*memper-*)
— and ran the live verification pass
described below. A third pass, prompted by the owner asking about
affixation differences by ethnicity or religion, added the sidebar in
Ch. 1 (§1.1) on the same basis — live web searches run in
conversation, not training-derived recall alone — covering Javanese-
Indonesian language contact, Jakarta colloquial Indonesian's
documented link to Betawi Malay rather than any single ethnic group,
and the absence of any literature tying affixation itself to religion
(only vocabulary/loanword choice). That sidebar is a brief summary of
a conversational answer, not independently re-verified beyond the
searches that produced it. A fourth pass, after the owner asked
whether Jakarta colloquial Indonesian's *nge-*/*-in* system (named but
not explained in that sidebar) had actually been covered anywhere,
added Ch. 7 §7.5 on the same live-search basis — citing Sneddon's
*Colloquial Jakartan Indonesian* and Hidajat's and Arka & Yannuar's
work on *-in* specifically (found via search, not read directly: the
primary texts themselves weren't fetched and checked line-by-line,
only secondary descriptions of them). Treat §7.5's claims as resting
on secondary characterizations of those sources, one level removed
from the primary literature. A fifth pass, after the owner asked
whether this book should cover Indonesian-vs-Malaysian-Malay affix
differences, added Appendix D. That appendix has the weakest sourcing
in the book by its own admission — no single systematic comparison of
the two standards' affixation was found, so its claims (Malaysian
*ter-*'s broader distribution relative to *di-*; *kena*'s extra
"have to" sense in Malaysian) are assembled from separate single-
variety corpus studies rather than a direct comparison, and are
flagged as such in the appendix's own reliability note rather than
only here. A sixth pass, after the owner asked whether the book
covered informal speech dropping affixes, added Ch. 6 §6.5
(*bekerja*/*kerja*, *berjalan*/*jalan*) — this one needed no new
verification, since it's a direct extension of the already-covered
*meN-*-dropping pattern (§3.3.2) to the one remaining prefix that
hadn't gotten the same note. A seventh pass, after the owner asked
whether Indonesian has an honorific/speech-level system, extended the
Ch. 1 sidebar with a paragraph on social hierarchy — again via live
search rather than recall alone, confirming (via academic sources
citing the structural point directly, not just the popular Wikipedia
article on *kramanisasi*) that Indonesian lacks Javanese's three-level
*ngoko*/*madya*/*krama* system where affixes themselves differ by
level, and that Indonesian politeness runs through pronoun/address-
term choice instead. An eighth pass, prompted by the owner's request
to check whether Passive Type 2 (§5.4) combines with *-kan*/*-i* and
whether colloquial *-in* (§7.5) works bare without *nge-*, caught a
real error while verifying the first question: **this book had the
Passive Type 1/Type 2 labels backwards.** Sneddon's *Indonesian
Reference Grammar* glossary — the authoritative source, confirmed
across multiple citations of it — defines Type 1 as the *di-*
construction and Type 2 as the bare-pronoun-fronting construction;
this book's §5.4 (and the matching entries in Appendix A and Appendix
B) had initially labeled them the other way around. All three have
been corrected. This is the most significant correction made during
any of this book's verification passes — unlike the *sekolah*/*-tah*
corrections in the earlier follow-up pass, a labeling swap like this
is exactly the kind of error that's easy to internalize wrong and
repeat, so flag it specifically if you'd already started using the
old labels from an earlier read of this book. The second question
(bare *-in*) resolved less cleanly: §7.5's new subsection presents it
as plausible by analogy, not confirmed — the sources checked didn't
specifically verify an imperative use of bare *-in*. These eight follow-up passes are the only
points in this book's production where claims were checked against
external sources *after* drafting, rather than drawn from
training-derived knowledge *during* drafting.

## What was actually cross-checked, and against what

Per this project's own sourcing rules, three tiers of material went
into each chapter, with different reliability implications:

1. **Core grammar rules** (nasal assimilation, r-initial dissimilation,
   the function of each affix) — drawn from the AI's training-derived
   knowledge of standard Indonesian reference grammar (the kind of
   material `pembilas/data/affixes.json` itself cites as its basis:
   Sneddon's *Indonesian Reference Grammar*, Alwi et al.'s *Tata
   Bahasa Baku Bahasa Indonesia*), not fetched or quoted from those
   texts directly during drafting. Treat these as *plausible
   restatements* of standard grammar, not verified citations.
2. **Example words and derived forms** — where the root appears in
   `pembilas/data/annotations.json`, the chapters above were written
   to match that file's hand-curated glosses, and several specific
   corroborations are called out inline (e.g. §9.7's note on *temu*,
   §6.2/§8.4/§9.6/§12.2's repeated flagging of *kerja*'s
   irregularities). Where a root *isn't* annotated there — most
   infixes (Ch. 11), most particles (Ch. 10's *-kah*/*-pun*/*-tah*),
   and several individual example words even within annotated roots'
   entries — the example was sourced from the AI's general knowledge
   of Indonesian vocabulary instead, consistent with this project's
   own instruction to prefer dictionary sources over invented
   examples, but without a live Wiktionary/KBBI lookup for every word.
3. **Glosses/meanings** — follow the same tiering as (2). No chapter's
   example sentences were checked against a native speaker in this
   drafting pass.

## Follow-up verification pass

After the initial drafting pass above, a second pass ran live web
searches (Wiktionary, KBBI-derived sources, and published linguistics
abstracts) against the specific items flagged as lower-confidence
below, and against a couple of items that weren't flagged but turned
out to need it. This is still not the same as a native-speaker check
or a direct KBBI lookup (most results came from third-party sites
mirroring KBBI, or from Wiktionary, rather than `kbbi.kemdikbud.go.id`
itself) — treat it as a meaningfully stronger check than the first
pass, not a complete one. Three items changed as a result:

- **Ch. 10, §10.3 (now corrected)** — the *sekolah* etymology
  originally named *Dutch* "*school*" as the source. Search results
  favored a different lineage (Malay *sekolah*, from Portuguese
  *escola*), with a Dutch-origin claim appearing only on one
  lower-quality source. The chapter text has been corrected to
  Portuguese *escola*, via Malay.
- **Ch. 10, §10.8 (now corrected)** — the *-tah* particle was
  originally framed as "literary/classical." The one source actually
  found that discusses it (an ISMIL conference abstract on Malay
  particles) instead groups it with *-lah*/*-kah* as a discourse
  particle in **colloquial/regional Malay varieties**, not classical
  literary registers specifically. The chapter text now avoids the
  "literary/classical" claim and just says it's essentially inert in
  standard modern Indonesian — a narrower, better-supported claim.
- **Ch. 13's former reference to a "beyond this book's core scope"
  *per-...-kan* pattern** is resolved, not just corrected: that
  pattern is now actually covered, in the new §4.6 (added after this
  book's first complete draft — see below). The old cross-reference
  to it as *§13.4* was also simply wrong regardless (§13.4 is the
  *pemberitahuan* section; the *diperdagangkan* example lives in the
  unnumbered Practice answer key) — both the scope gap and the broken
  reference are fixed now.

Two items were checked and held up, raising confidence rather than
changing the text:

- **Ch. 9, §9.7** — the *penemuan* ("discovery") vs. *pertemuan*
  ("meeting") split on *temu* is independently confirmed by
  KBBI-derived sources, matching this book's text and *against* what
  `pembilas/data/annotations.json`'s single conflated gloss for *temu*
  would suggest.
- **Ch. 10, §10.2** — the *ketua* (← *ke-* + *tua*) and *kekasih*
  (← *ke-* + *kasih*) etymologies are confirmed by Wiktionary
  (*kasih* traced further to Proto-Malayo-Polynesian *\*ka-qasiq*).

## Remaining lower-confidence spots

- **Ch. 7, §7.5** — the *nge-*/*-in* examples (*ngerti*, *ngomong*,
  *ngerjain*, *ngasihin*, *ngetawain*) and the claim that *-in*
  collapses the *-kan*/*-i* distinction are sourced from search-engine
  summaries of Hidajat's and Arka & Yannuar's work and Sneddon's book,
  not from reading those sources directly. The specific glosses given
  for *ngetawain* and *ngasihin* in particular are this book's own
  attempt to map a colloquial form onto its nearest standard
  equivalent, which wasn't something any of the sources found did
  explicitly — treat those two glosses as the least certain claims in
  the section, and the *-in*-replaces-both-suffixes claim itself (which
  a source did state directly) as the most certain one.
- **Ch. 4, §4.6** — the *memper-* pattern (added in the same pass as
  this verification) is the newest material in the book and the
  least settled: published sources disagree on whether its *-kan*/*-i*
  combinations are best described as "causative" or "intensifying,"
  and this book's text reflects that disagreement rather than resolving
  it. The *memperbesarkan*-is-an-error claim and the *memperbesar*/
  *mempercepat*/*memperlambat* adjective-root examples are better
  supported than the *-kan*/*-i* combinations (*mempertahankan*,
  *memperdagangkan*, *memperbaiki*); if you need precision here,
  check a reference grammar rather than relying on this section alone.
- **Ch. 4, §4.5** — *mengerjai* ("to prank/trick someone") wasn't found
  in the KBBI mirror checked during the verification pass (which
  returned no entry at all for that specific inflected form). The
  colloquial sense is still consistent with general knowledge of
  spoken Indonesian, but it's the one specific gloss in this book that
  a dictionary search actively failed to confirm rather than simply
  not covering — worth a second opinion from a native speaker before
  you rely on it.
- **Every cross-reference between chapters** (the "§X.Y" citations
  throughout) was written by the same drafting pass that wrote the
  content, with one exception now fixed (the §13.4 reference above).
  The rest weren't individually re-checked against the final files
  after every subsequent edit. If you spot one that points to the
  wrong section, that's a drafting error worth fixing, not a sign the
  underlying grammar claim is wrong.

## What this means for using the book

Treat every example sentence and gloss as "probably right, consistent
with how a knowledgeable source would describe it" rather than
"verified." For anything you intend to actually rely on — teaching
someone else, using in writing that matters, or settling a specific
disagreement about whether a form is natural — check it against KBBI,
Wiktionary's Indonesian entries, a standard reference grammar, or a
native speaker, the same way this project's own `CLAUDE.md` already
asks you to treat `pembilas/data/words.json` and
`annotations.json` as corroboration rather than final authority. The
affixation *rules* in this book (Chapters 2–11's forms tables) are the
part most likely to hold up unmodified; the specific *example
sentences and glosses* are the part most worth independently spot-
checking before you lean on them.
