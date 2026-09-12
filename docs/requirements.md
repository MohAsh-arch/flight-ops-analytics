# Requirements Specification: Flight Analytics Platform (SkyMetrics)

**Document Version:** 1.0
**Date:** 2026-09-02
**Author:** Mohamed A. Abdelazim

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

**Description:** Owns revenue performance and pricing strategy across routes. Accountable for explaining route profitability, competitive market position, and pricing decisions to leadership.

#### Functional Requirements (FR)

*Specific behaviors, actions, or features the system must provide for this role.*

| Req ID | Feature / Action | Description |
| :--- | :--- | :--- |
| `RA-FR-01` | **Data consolidation** | The system must consolidate ticket revenue data with route performance data into a single place, so route-level profitability questions don't require manual, one-off spreadsheet work. |
| `RA-FR-02` | **Market share by route** | The system must compute SkyMetrics's market share of passenger volume on its top 20 busiest routes, using the federal on-time performance dataset (which covers all carriers), trended monthly and quarterly, at the route level. **Open risk (to verify during data exploration):** dataset completeness for accurate per-route market volume — codeshares, edge cases, or data gaps may limit how cleanly this can be computed. This requirement may need revision once the dataset is profiled. |
| `RA-FR-03` | **Load factor vs. on-time performance** | The system must present load factor and on-time performance side by side, at the route level, so the Revenue Analyst can evaluate whether chronic lateness correlates with reduced bookings on specific routes. |
| `RA-FR-04` | **Yield vs. distance** | The system must calculate yield (revenue per passenger-mile) per route and present it against route distance, so the Revenue Analyst can evaluate whether short-haul and long-haul routes are being priced proportionately. |

#### Non-Functional Requirements (NFR)

*Quality attributes, performance, security, and usability constraints for this role.*

| Req ID | Category | Description |
| :--- | :--- | :--- |
| `RA-NFR-01` | **Market Share & Yield Freshness** | Market share and yield figures may be refreshed monthly, with staleness of up to about a week acceptable — because these are trend numbers used to support monthly exec-review conversations, not day-to-day operational decisions, so near-term staleness doesn't affect their usefulness. |
| `RA-NFR-02` | **Load Factor / OTP Correlation Freshness** | Load factor and on-time performance data must be refreshed weekly, not monthly — because this comparison is meant to catch a route's performance beginning to slide early enough to flag it, and month-old data would mean the warning arrives after the window to act on it has passed. |

---

### 2.3 Role: Airport Operations Director

**Description:** Owns ground and network-level airport performance across the operator's network. Accountable for identifying the root cause of delay cascades and ground-operations degradation, and for building the data-backed case for infrastructure or staffing investment at specific airports.

#### Functional Requirements (FR)

*Specific behaviors, actions, or features the system must provide for this role.*

| Req ID | Feature / Action | Description |
| :--- | :--- | :--- |
| `AOD-FR-01` | **Delay cascade source identification** | The system must distinguish which airports are causing delay cascades from which airports are merely experiencing delays that originated elsewhere. |
| `AOD-FR-02` | **Taxi time trend** | The system must show taxi-out and taxi-in times per airport, trended across multiple quarters, so the Airport Operations Director can visually judge whether ground operations are sustainably worsening. No automatic threshold or alert is required — she wants to see the trend and judge it herself. |
| `AOD-FR-03` | **Cancellation rate and cause by airport pair** | The system must show cancellation rates by airport pair, along with the primary cancellation reason (e.g. weather, mechanical, crew), so the Airport Operations Director can make a data-backed case to leadership for specific investments (e.g. de-icing equipment, ground staff) at the airports actually driving cancellations. |

#### Non-Functional Requirements (NFR)

*Quality attributes, performance, security, and usability constraints for this role.*

| Req ID | Category | Description |
| :--- | :--- | :--- |
| `AOD-NFR-01` | **No freshness constraint** | Confirmed directly with the Airport Operations Director: none of her requirements are time-sensitive. All three are used for multi-quarter, budget-case-style analysis rather than day-to-day decisions, so data being days or weeks old is acceptable. She explicitly prioritized correctness of the delay-cascade classification (`AOD-FR-01`) over speed. |

---