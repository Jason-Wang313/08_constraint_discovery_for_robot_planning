# Submission Readiness Decision

## Decision

Workshop-only.

## Rationale

The v2 paper is stronger because it adds the noisy-signature stress missing from the initial audit. The result supports ACS under exact or low-miss diagnostics, but it shows false negatives quickly undermine valid planning.

The paper is not ready for a main conference because the evidence is synthetic, the constraint vocabulary and edge labels are supplied, and no real robot or real TAMP benchmark is evaluated.

## Required Before Main-Conference Submission

- Real TAMP benchmark or robot-task integration.
- Learned/calibrated diagnostic probes with uncertainty estimates.
- Abstention or fallback verification for ambiguous signatures.
- Recovery analysis for false positives and false negatives.
