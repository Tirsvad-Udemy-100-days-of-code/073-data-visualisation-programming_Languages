# Data: load and prepare the dataset

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version (RC-005 Go) | pending |

---

## Purpose

Decide whether the data can be loaded and prepared correctly: the dataset is available and the first five lecture steps (explore, group, convert dates, pivot, fill NaN) are implemented and tested.

## Deliverable

The dataset `data/QueryResults.csv` and the module `src/programming_languages/data.py` with the functions `load_data`, `posts_per_language`, `months_per_language`, `convert_dates`, `reshape_data` and `fill_missing`, each tested, and a screenshot per lecture step stored in `docs/images/`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `data/QueryResults.csv` exists with columns DATE, TAG, POSTS and 1991 data rows | Shape (1991, 3) after load | Different shape or file missing |
| 2 | `load_data` returns a DataFrame with columns DATE, TAG, POSTS | Test passes | Test fails |
| 3 | `posts_per_language` and `months_per_language` return one row per tag | Tests pass | Tests fail |
| 4 | `convert_dates` returns DATE as `datetime64` | Test passes | Test fails |
| 5 | `reshape_data` returns 145 rows and 14 columns, and no NaN remain after `fill_missing` | Tests pass | Tests fail |
| 6 | Screenshots for steps 1 to 5 exist in `docs/images/` | 5 images | Fewer than 5 |
| 7 | Code reviewed against `qc-programming-python` with an `RC-*` verdict Go | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The skeleton, `pyproject.toml` and test runner must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1, 4 ([BC-001]) | Success criteria 1, 2, 3 |
| Concern CN-001, CN-003 ([SA-001]) | S01, S02 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, not independent) |

## Target Date

2026-11-12 — inside the Business Case target of finishing by 2026-11-14.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Obtain QueryResults.csv | Download the dataset from the link given in the assignment, after S01 has approved the filename, source and size in chat, and save it as `data/QueryResults.csv`. If the signed link has expired, stop and ask S01 for the file; never invent data (BC-001 Risks). | No | [BC-001] Risks |
| 2 | Implement load_data and exploration | Read the CSV with `pd.read_csv(..., names=['DATE','TAG','POSTS'], header=0)`; show head, tail, shape and count (lecture step 1). Includes tests and a screenshot. | No | [BC-001] Objective 1 |
| 3 | Implement language grouping | Add `posts_per_language` (groupby TAG, sum POSTS) and `months_per_language` (groupby TAG, count) as in lecture step 2, with tests and a screenshot. | No | [BC-001] Objective 1 |
| 4 | Implement convert_dates | Convert the DATE strings to timestamps with `pd.to_datetime` (lecture step 3), with a test that checks the dtype and a screenshot of the type check. | No | [BC-001] Objective 1 |
| 5 | Implement reshape_data and fill_missing | Pivot to one column per language (`index='DATE'`, `columns='TAG'`, `values='POSTS'`), then replace NaN with 0 and check `isna().values.any()` is False (lecture steps 4 and 5). Tests assert 145 rows and 14 columns. | No | [BC-001] Objective 1 |
| 6 | Review data code and open the pull request | Review `src/` and `tests/` against `qc-programming-python`, write the `RC-*`, run opengrep, then open one pull request that closes this milestone's issues. | No | [BC-001] Constraints |

---

[BC-001]: ../business-case.md
