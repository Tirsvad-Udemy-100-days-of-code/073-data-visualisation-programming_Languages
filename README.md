# 🚀 Programming Languages: Day 73 of 100 Days of Code

Which programming language is the most popular? This project answers it by counting Stack Overflow posts per language tag with pandas and Matplotlib, as an assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp". It is for course participants who want runnable, readable code and for visitors looking for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The analysis follows the lecture step by step: explore the data, group by language, convert dates, pivot, fill missing values, plot one language, style the chart, plot several languages, plot all languages with a legend and smooth the lines with a rolling mean.

| Folder | Purpose |
| --- | --- |
| `src/programming_languages/` | The package with the functions of the assignment |
| `tests/` | Automated tests |
| `docs/` | Project documents (business case, plan, milestones, reviews) |

The project is delivered milestone by milestone; see the milestones in the appendix for what is done.

## 📋 Requirements

- Python 3.13 or newer, because the project targets it (`requires-python` in `pyproject.toml`).
- `pandas` and `matplotlib`, the only runtime dependencies.
- Development extras (`pytest`, `jupyter`, `ruff`, `mypy`) are installed only with `.[dev]`.

## 🛠️ Setup

Create and use a local virtual environment in `.venv`:

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/Scripts/activate   # Git Bash on Windows
source .venv/bin/activate       # Linux and macOS
```

```powershell
.venv\Scripts\Activate.ps1      # PowerShell on Windows
```

Upgrade pip, then install the project with the development extras:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`. Delete `.venv/` to start over.

## ▶️ Run

Open the notebook in Jupyter (added in a later milestone):

```bash
jupyter lab
```

## 🧪 Tests

```bash
python -m pytest
```

Before a push, scan the tracked files with opengrep (it must not report an `ERROR`; the `.env` file is personal and never scanned or committed):

```bash
~/.opengrep/cli/latest/opengrep.exe scan --config auto --error --exclude .env .
```

## 📄 License

[AGPL-3.0](./LICENSE)

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/issues
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
