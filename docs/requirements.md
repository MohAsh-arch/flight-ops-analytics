# Requirements Specification: Flight Analytics Platform (SkyMetrics)

**Document Version:** 1.0
**Date:** 2026-09-02
**Author:** Mohamed

## 1. System Overview

SkyMetrics is a data platform for a regional airline operator, built to replace manual, spreadsheet-based reporting with a consolidated system that answers recurring operational, revenue, and airport-performance questions for three internal stakeholders. Each requirement below is traced to a specific stakeholder need surfaced through direct interviews, not assumed upfront.

---

## 2. Role-Based Requirements

### 2.1 Role: Operations Manager

**Description:** Owns day-to-day flight operations performance for the airline. Accountable for on-time performance, delay causes, and surfacing operational issues (including maintenance signals) to leadership.

#### Functional Requirements (FR)

*Specific behaviors, actions, or features the system must provide for this role.*

| Req ID | Feature / Action | Description |
| :--- | :--- | :--- |
| `OM-FR-01` | **Data consolidation** | The system must pull together data currently scattered across three places the Operations Manager currently manages by hand: delay/status logs from the ops team's tracker, flight records from the operations tracking database, and maintenance data from Engineering's logs. |
| `OM-FR-02` | **Weekly report** | The system must produce a report ready before the Monday ops review — not "weekly" as a loose cadence, but tied specifically to that deadline. |
| `OM-FR-03` | **Anomaly detection** | <ul><li><strong>Route condition:</strong> a route's on-time performance drops meaningfully below its normal range (working placeholder: below ~75%) sustained for 2+ consecutive days — one bad day is noise, a run of bad days isn't.</li><li><strong>Tail-number condition:</strong> a specific aircraft shows up in delay logs 3–4 times within a week — a possible maintenance signal.</li></ul> |
| `OM-FR-04` | **Weekly performance report content** | <ul><li><strong>Week-over-week delta:</strong> overall on-time performance vs. the prior week, presented as a single top-line delta.</li><li><strong>Worst-performing routes:</strong> a ranked short list (not all routes), each with a delay-cause breakdown attributed to carrier, weather, or NAS.</li><li><strong>Tail-number maintenance flags:</strong> aircraft appearing repeatedly in delay logs, surfaced clearly and prominently — not buried inside a dense table.</li><li><strong>Multi-week trend:</strong> indicate whether a struggling route is newly underperforming this week or has been running poorly for multiple consecutive weeks; requires looking back further than just the prior week's number.</li></ul> |

#### Non-Functional Requirements (NFR)

*Quality attributes, performance, security, and usability constraints for this role.*

| Req ID | Category | Description |
| :--- | :--- | :--- |
| `OM-NFR-01` | **Tunable thresholds** | Those two threshold numbers above must live in config, not hardcoded in pipeline logic — because the Operations Manager is guessing at the numbers and expects them to get refined once real data comes in. Baking them into code would mean a redeploy every time the Operations Manager wants to adjust the thresholds. |

---

### 2.2 Role: Revenue Analyst

**Status:** Interview in progress — not yet finalized. No FRs or NFRs committed to this section until the interview is complete and reviewed.

---

### 2.3 Role: Airport Operations Director

**Status:** Interview not yet started.

---