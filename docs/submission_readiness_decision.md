# Submission Readiness Decision

## Decision

Full-scale simulation-ready final.

## Rationale

The final pass expands the paper beyond the initial ACS sweep into a 26-page manuscript with topology scaling, selected-path verification, diagnostic-noise stress, planner-label stress, false-positive completeness stress, and cost-sensitivity analysis. The core mechanism is now supported and bounded by multiple positive and negative findings.

The paper still should not claim physical-robot validation. The evidence remains a controlled simulator and formal abstraction with known constraint families and supplied edge labels.

The 2026-06-21 export also matches the visible VLA-v4 boxed-link convention: green citation/URL boxes, red internal-reference boxes, one-point borders, and no cyan link boxes in the audited final PDF.

## Required Before A Stronger Hardware/Benchmark Claim

- Real TAMP benchmark or robot-task integration.
- Learned/calibrated diagnostic probes with uncertainty estimates.
- Abstention or fallback verification for ambiguous signatures.
- Recovery analysis for false positives and false negatives.
