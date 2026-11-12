# Review of the published wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [MIL-004], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [64dadec] |

---

## Artifact Under Review

- Instance reviewed: the published wiki of the repository (delta of RC-013, criterion 14) ([MIL-004])
- Checklist used: [QC-WIKI-001] (`QC-WIKI-001`)
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Starts with the bold title, then one list of the English pages, Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | Link check over all 37 files: 0 dead links; every English page is in the sidebar. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | The wiki has no related wiki, so the sidebar has no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | `**Languages**` is the last section, one line per language in that language. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is hand-written; no generator exists. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Language line on every page. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English and Bahasa Malaysia and Dansk; the PO language is en. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | 12 English pages, each with a `-da` and a `-ms` page. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Every page starts with the language line, current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | `<Page>-da.md`, `<Page>-ms.md`, English without suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Code, commands and file names are English on every page. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | After the merge (run of `Publish wiki`, success) all 36 pages answer HTTP 200 on the host, the sidebar is published and the 10 screenshots load from the raw URL. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | No generator or template in this project. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All pages and `_Sidebar.md` are directly in `docs/wiki/`. |

## Overall Verdict

Go. No Mandatory criterion fails; N-A rows say why they do not apply. Stand-in review, not independent, open to challenge in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---

[MIL-004]: ../../milestones/mil-004-docs.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[64dadec]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/commit/64dadece74b60c54903f4c997b6aef07c5f4ed0c
