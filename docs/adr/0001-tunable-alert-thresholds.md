# ADR 0001: Tunable Alert Thresholds (Not Hardcoded)

**Status:** Accepted
**Date:** 2026-09-02
**Related requirement:** OM-NFR-01

## Context

During the Operations Manager interview, two anomaly-detection thresholds were defined for the mid-week alert (OM-FR-03):

- A route's on-time performance dropping below ~75%, sustained for 2+ consecutive days.
- A single tail number appearing in delay logs 3–4 times within a week.

The Operations Manager was explicit that these numbers are a starting guess, not a fixed standard — she has never had to put a number on "abnormal" before, and expects the thresholds to be refined once real weekly data shows what's actually meaningful.

## Decision

Alert thresholds will be stored as configuration (e.g. a config file, environment variables, or a dedicated settings table) rather than hardcoded into pipeline logic (Airflow DAGs, dbt models, or application code).

## Consequences

**Enables:**
- Thresholds can be adjusted as real data reveals better values, without a code change or redeploy.
- The same mechanism can support per-route or per-context threshold tuning later, if needed.

**Costs:**
- Requires a defined place to store and load this config (and a decision on where — file vs. table vs. env var — to be made when this phase is implemented).
- Threshold changes are no longer version-controlled the same way code is, unless the config itself is checked into the repo or otherwise tracked. 