# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version (RC-002 Go) | pending |

---

## Purpose

Identify who is affected by the Day 73 project, who decides and who reviews. Method: power/interest grid with four quadrants, concerns mapped to FURPS+.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A correct, well-explained solution that shows what was learned |
| S02 | Udemy coursists | Course participants who share code | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and README instructions |
| S03 | GitHub viewers | Visitors browsing for ideas | GitHub community | LOW | MEDIUM | Keep Informed | A clear description, topics and README, and no runtime dependencies beyond the lecture's |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, builds, reviews and accepts every artifact.
- **Keep Informed (S02, S03):** no decision power over the project, but they use the result; their needs shape the README, naming and wiki.
- **Keep Satisfied, Monitor:** none.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Every lecture step is reproduced and verified by tests | Functionality |
| CN-002 | S01 | Work is planned, reviewed and traceable | Supportability |
| CN-003 | S02 | Code is readable and uses the assignment's function names | Usability |
| CN-004 | S02 | Setup and run instructions work from a clean checkout | Usability |
| CN-005 | S03 | Repository has a description, topics and README | Usability |
| CN-006 | S03 | No runtime dependencies beyond pandas and Matplotlib | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CM-001 | Chat with S01 | Per request | Plan acceptance, run summary | All |
| CM-002 | README | Per milestone | Run instructions and screenshots | MIL-001, MIL-004 |
| CM-003 | Wiki (en, da, ms) | Once, in MIL-004 | What each lecture step teaches | MIL-004 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants the assignment's function names; clean code may prefer other names | S01, S02 | Keep the assignment's names for the public functions; document them in the README |
| S03 wants no extra dependencies; plotting needs Matplotlib and pandas | S01, S03 | Only pandas and Matplotlib as runtime dependencies; tooling stays in the `dev` extra |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-002 | Objective 1, 2 ([BC-001]) |
| S02 | CN-003, CN-004 | Objective 1, 3, 4 ([BC-001]) |
| S03 | CN-005, CN-006 | Objective 2, 5, 6 ([BC-001]) |

## Sign-Off

S01, as Product Owner and reviewer. In autonomous mode the AI signs as stand-in for S01, not independent.

---

[BC-001]: ./business-case.md
