# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version (RC-001 Go) | [36a5948] |

---

## Executive Summary

Day 73 of Udemy's "100 Days of Code" asks which programming language is the most popular, measured by the number of Stack Overflow posts per language tag since July 2008. This project delivers that analysis as readable, runnable Python (pandas and Matplotlib) with a Jupyter notebook, tests, a README with screenshots of every lecture step, and a three-language wiki (English, Danish, Bahasa Malaysia). The recommendation is to proceed: the scope is small, the dependencies are known, and the result is shared with other course participants and GitHub viewers.

## Methodological and Standards Foundation

Quality is reviewed against the framework checklists, tagged with ISO/IEC 25010:2023 characteristics. Code follows the framework's Python conventions and Clean Architecture; the plan-first gate governs when code may be written.

## Problem Statement

The course assignment is normally delivered as a notebook only. Course participants (S02) share and compare solutions, but a notebook alone is hard to run, test and review, and gives GitHub viewers (S03) no explanation. The belief that would kill the idea: the assignment data (`QueryResults.csv`) cannot be obtained, so the analysis cannot be run and verified.

## Business Opportunity

A small, well-documented repository turns one lesson into a reusable reference: the assignment's function names, tests, screenshots and a wiki that explains what each lecture step teaches, in three languages.

## Objectives

1. Reproduce every lecture step of Day 73 (explore, group, convert dates, pivot, fill NaN, plot one language, style, two languages, all languages with legend, rolling mean) in runnable code.
2. Keep the code readable, tested and free of runtime dependencies beyond pandas and Matplotlib.
3. Document how to create and use a local `.venv` and run the project and its tests.
4. Show every lecture step with a screenshot in the README and the wiki.
5. Explain what each lecture step teaches in a wiki in English, Danish and Bahasa Malaysia.
6. Publish the repository with a description and topics.

## Scope

### In Scope

- Python 3.13 or newer package under `src/`, tests under `tests/`, documents under `docs/`.
- `pyproject.toml`, Python `.gitignore`, `.venv` instructions, `README.md` from the framework template.
- A Jupyter notebook following the lecture.
- Screenshots (charts) per lecture step; wiki in `en`, `da`, `ms`.
- Static analysis with opengrep before every push.

### Out of Scope

- Fetching live data from Stack Overflow or the Stack Exchange API.
- A GUI, a web service or packaging for PyPI.
- Using or committing the `.env` file or any token.
- Other days of the course.

## Expected Benefits

### Tangible Benefits

- A runnable, tested solution reproducible from the README in under five minutes.
- Screenshots and a wiki in three languages for every lecture step.

### Intangible Benefits

- A clear learning record of pandas and Matplotlib techniques.
- A tidy repository that other course participants can compare against.

## Strategic Alignment

The project is one step of the 100 Days of Code course and is delivered through the SQA/QC framework as practice for planning-first, reviewed delivery.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Lecture steps reproduced | 10 of 10 steps have code | Step list in the README against the code |
| 2 | Automated tests pass | 100 % of tests, 0 failures | `python -m pytest` |
| 3 | Screenshots present | 1 per lecture step in README and each wiki language | Count of images per document |
| 4 | Wiki languages | 3 (en, da, ms) with the same pages | Page list per language |
| 5 | Runtime dependencies | 2 (pandas, matplotlib) | `pyproject.toml` `dependencies` |
| 6 | Static analysis | 0 opengrep findings of severity error before each push | opengrep report |
| 7 | Repository metadata | Description and at least 5 topics set | Repository page |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| `QueryResults.csv` link is a signed, expiring Udemy URL and may no longer work | High: no data to analyse | Download once with the user's approval; otherwise the user supplies the file; stop and report, never invent the data |
| Matplotlib needs a display for screenshots | Medium | Use the `Agg` backend and save charts to files; no GUI test on the host desktop |
| Tokens in `.env` leak into the repository | High | `.env` stays in `.gitignore`, is never read by project code, never printed |
| Wiki translations drift from each other | Medium | Same page list in each language, checked with `check-languages.sh` |

## Assumptions

- S01 is Product Owner, developer and reviewer; the AI acts as stand-in reviewer in autonomous mode and the review records say so.
- The course data is for personal learning and the dataset may be committed under `data/`.
- Python 3.13 or newer and git are installed on the author's machine.
- The belief that the CSV is obtainable is untested until milestone 2.

## Constraints

- Python 3.13 or newer, `venv`, `pyproject.toml`.
- Folder structure `src/`, `tests/`, `docs/`.
- Runtime dependencies kept to what the lecture needs.
- Work happens on branches with one pull request per milestone.
- Target completion 2026-11-14, with no hard deadline and no budget; the effort is a few days of part-time work.

## Cost–Benefit Assessment

Qualitative: the cost is the author's own time (roughly 2 to 3 working days, no money spent); the benefit is a learning record and a shareable reference, which has no market value to quantify.

| Costs | Benefits |
| --- | --- |
| About 2 to 3 days of the author's time | Runnable, tested lecture solution |
| Maintenance of three wiki languages | Reusable reference for S02 and S03 |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owns the result, builds it and reviews it |
| S02 | Reads and runs the code, compares solutions |
| S03 | Browses the repository for ideas |

## Recommendation

Proceed — a small, low-risk project with clear scope whose only open question (the data file) is handled in milestone 2.

---

[SA-001]: ./stakeholder-analysis.md
[36a5948]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/commit/36a594856f17f368264c6bceef2b3ae132e56d1c
