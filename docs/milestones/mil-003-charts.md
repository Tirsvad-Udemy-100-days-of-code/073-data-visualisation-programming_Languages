# Charts: visualise the data

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Deprecated | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version (RC-006 Go) | [36a5948] |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Source is laid out in the clean architecture layers instead of flat modules (RC-010 Go) | pending |

---

## Purpose

Decide whether the visualisation steps are correct: single, styled, two-language, all-language and rolling-mean line charts are produced from the prepared data.

## Deliverable

The layers of `src/programming_languages/` with `plot_language` and `plot_languages` (infrastructure) and `rolling_mean` (domain) that save charts to files with the Agg backend, tested, and one screenshot per lecture steps 6 to 10 in `docs/images/`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `plot_language` draws one language with figsize (16, 10), axis labels and y-limit 0 | Test inspects the figure and passes | Test fails |
| 2 | `plot_languages` draws every requested column with a legend and linewidth 3 | Test passes | Test fails |
| 3 | `rolling_mean(window=6)` equals `DataFrame.rolling(window=6).mean()` | Test passes | Test fails |
| 4 | Charts are saved without opening a window (Agg backend) | No GUI on the host desktop | A window opens |
| 5 | Screenshots for steps 6 to 10 exist in `docs/images/` | 5 images | Fewer than 5 |
| 6 | Code reviewed against `qc-programming-python` with an `RC-*` verdict Go | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The reshaped, filled DataFrame is the input of every chart |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1, 4 ([BC-001]) | Success criteria 1, 3 |
| Concern CN-001, CN-003 ([SA-001]) | S01, S02 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, not independent) |

## Target Date

2026-11-13 — inside the Business Case target of finishing by 2026-11-14.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement plot_language | Plot the Java series from the reshaped data (lecture step 6) and style it: figsize (16, 10), font sizes 14, labels Date and Number of Posts, `ylim(0, 35000)` (lecture step 7). Saves to a file; test with the Agg backend. | No | [BC-001] Objective 1 |
| 2 | Implement plot_languages | Plot Java and Python together (lecture step 8), then all languages in a loop with `linewidth=3`, `label=column` and a legend of font size 16 (lecture step 9). Tests count the lines and the legend entries. | No | [BC-001] Objective 1 |
| 3 | Implement rolling_mean | Smooth the series with `rolling(window=6).mean()` and plot it (lecture step 10), with a parameter for the window so 3 and 12 can be tried. Test against pandas directly. | No | [BC-001] Objective 1 |
| 4 | Generate chart screenshots | Write a script `src/programming_languages/presentation/screenshots.py` that renders each lecture step (tables as images, charts as saved figures) into `docs/images/step-NN-name.png` headlessly. | No | [BC-001] Objective 4 |
| 5 | Review chart code and open the pull request | Review against `qc-programming-python`, write the `RC-*`, run opengrep, open one pull request that closes this milestone's issues. | No | [BC-001] Constraints |

---

[BC-001]: ../business-case.md
[36a5948]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/commit/36a594856f17f368264c6bceef2b3ae132e56d1c
