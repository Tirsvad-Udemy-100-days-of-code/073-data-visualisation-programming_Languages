# Review of the code of MIL-002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the data code under `src/` and `tests/` of MIL-002 ([MIL-002])
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules, functions and constants follow PEP 8 casing. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose; the assignment's names are kept (`load_data`, `convert_dates`, `reshape_data`, `fill_missing`). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` clean, no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All signatures annotated; `mypy --strict` passes. One string annotation `Series[int]` is needed because pandas-stubs makes `Series` generic. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No exception handling; no bare except. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; `window: int = 6` and a Path constant only. |
| 7 | Files, locks and connections are managed with context managers | Pass | Files are read by `pd.read_csv` and written by matplotlib, which close them; the code opens none itself. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public modules and functions have docstrings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `screenshots.py` reports with `logging`, not `print`; no secret is logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | The project has no DCD: tasks are plain technical tasks. Layers and names follow the clean-architecture skill. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 15 tests (unit, integration, e2e), named for behaviour; no network; the real CSV is in the repository. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` reports no issue on 10 source files. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Runtime dependencies pandas and matplotlib, lower bounds only; none unused. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Column names are constants in the domain; the data path is defined once in infrastructure. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | Deviation recorded: the domain imports pandas because the DataFrame is the domain's data type; it imports no IO, UI or other layer. application imports domain only; infrastructure and presentation import inward. No import cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Small pure functions, one reason to change each; one frozen dataclass. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | `domain`, `application`, `infrastructure`, `presentation` under `src/`; `unit`, `integration`, `e2e` under `tests/`; snake_case. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names English, lowercase, no spaces. |

## Overall Verdict

Go. No Mandatory criterion fails; N-A rows say why they do not apply. Stand-in review, not independent, open to challenge in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---

[MIL-002]: ../../milestones/mil-002-data.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
