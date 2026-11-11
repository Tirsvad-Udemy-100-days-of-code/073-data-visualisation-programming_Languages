# Docs: notebook, README and wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version (RC-007 Go) | [36a5948] |

---

## Purpose

Decide whether the project can be shared: notebook, README with screenshots and a wiki in three languages explain what each lecture step teaches.

## Deliverable

The Jupyter notebook `notebooks/programming_languages.ipynb`, a README with a screenshot per lecture step, and a wiki with the same pages in English, Danish and Bahasa Malaysia, each with the screenshots and an explanation of what was gained in each step.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Notebook runs top to bottom without errors (`jupyter nbconvert --execute`) | Exit code 0 | Error |
| 2 | README shows 10 screenshots, one per lecture step, and the run and test instructions | 10 images and instructions | Fewer |
| 3 | Wiki has the same page list in `en`, `da` and `ms`, each page with its screenshot | 3 languages, identical page lists | A page or language missing |
| 4 | `framework/scripts/check-languages.sh` and `check-readme.sh` pass | Exit code 0 | Non-zero |
| 5 | Wiki reviewed against `qc-wiki` with an `RC-*` verdict Go | Go | No-Go |
| 6 | opengrep scan clean and all pull requests merged | 0 error findings | Findings open |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | The screenshots and all functions must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4, 5 ([BC-001]) | Success criteria 3, 4 |
| Concern CN-002, CN-004, CN-005 ([SA-001]) | S01, S02, S03 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, not independent) |

## Target Date

2026-11-14 — the Business Case target of finishing by 2026-11-14.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create the Jupyter notebook | Create `notebooks/programming_languages.ipynb` that follows the ten lecture steps with markdown explanations and uses the package functions. Execute it with nbconvert to prove it runs. | No | [BC-001] Objective 1 |
| 2 | Add screenshots to the README | Add the ten step screenshots to `README.md` with a one-line caption each and a table of the assignment's function names. | No | [BC-001] Objective 4 |
| 3 | Write the English wiki | Write the wiki pages in English following `framework/process/wiki.md`: one page per lecture step, with the screenshot and what was gained in that step. | No | [BC-001] Objective 5 |
| 4 | Write the Danish wiki | Translate the same page list to Danish, using the same page names with a language suffix, with the same screenshots. | No | [BC-001] Objective 5 |
| 5 | Write the Bahasa Malaysia wiki | Translate the same page list to Bahasa Malaysia (`ms`), with the same screenshots. | No | [BC-001] Objective 5 |
| 6 | Review documents and open the pull request | Run `check-languages.sh` and `check-readme.sh`, review the wiki against `qc-wiki`, write the `RC-*`, run opengrep, open one pull request closing the milestone's issues. | No | [BC-001] Constraints |

---

[BC-001]: ../business-case.md
[36a5948]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/commit/36a594856f17f368264c6bceef2b3ae132e56d1c
