# Setup: project skeleton and tooling

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version (RC-004 Go) | [36a5948] |

---

## Purpose

Decide whether the repository is ready for development: tooling, configuration and documentation of how to run it exist, and the repository is described on the git host.

## Deliverable

A Python 3.13+ project skeleton with `pyproject.toml`, Python `.gitignore`, `src/` and `tests/` folders, a `README.md` from the framework template with `.venv` instructions, passing opengrep scan, and a repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` declares `requires-python >= 3.13`, runtime dependencies `pandas` and `matplotlib` only, and a `dev` extra | Present and `pip install -e .[dev]` works | Missing or install fails |
| 2 | `.gitignore` ignores `.venv/`, `__pycache__/`, `.env`, notebook checkpoints | All four ignored | Any missing |
| 3 | README documents creating `.venv`, `python -m pip install --upgrade pip`, installing, running and testing | All five steps present | Any missing |
| 4 | `python -m pytest` runs on the skeleton | Exit code 0 | Non-zero |
| 5 | opengrep scan of the repository reports no finding of severity error | 0 findings | 1 or more |
| 6 | Repository has a description and at least 5 topics on the git host | Set and visible via the API | Not set |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3, 6 ([BC-001]) | Success criteria 5 and 7 |
| Concern CN-004, CN-005 ([SA-001]) | S02, S03 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, not independent) |

## Target Date

2026-11-11 — inside the Business Case target of finishing by 2026-11-14.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml | Create `pyproject.toml` for a `src` layout package with `requires-python >= 3.13`, runtime dependencies pandas and matplotlib, and a `dev` extra with pytest, jupyter and nbformat. Keeps runtime dependencies minimal for S03 (CN-006). | No | [BC-001] Objective 2 |
| 2 | Add Python .gitignore | Add the standard Python `.gitignore` plus `.env`, `.venv/` and notebook checkpoints so that the personal token file is never committed. | No | [BC-001] Risks |
| 3 | Create src and tests skeleton | Create the package `src/programming_languages/` and `tests/` with a smoke test, so `python -m pytest` runs from a fresh checkout. | No | [BC-001] Constraints |
| 4 | Write README with venv instructions | Create `README.md` from the framework template with sections for creating and using a local `.venv`, `python -m pip install --upgrade pip`, running the project and its tests. Run `framework/scripts/check-readme.sh`. | No | [BC-001] Objective 3 |
| 5 | Set repository description and topics | Using the token in `.env` (read only by the shell for this call, never printed or committed), set the Gitea repository description and topics through the API. Needs S01's chat approval of the wording because it is public-facing. | No | [BC-001] Objective 6 |
| 6 | Run opengrep before push | Run `~/.opengrep/cli/latest/opengrep.exe` on the repository before every push and record the command in the README contributing section. Fix or justify each finding. | No | [BC-001] Success criterion 6 |

---

[BC-001]: ../business-case.md
[36a5948]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/commit/36a594856f17f368264c6bceef2b3ae132e56d1c
