# Submission Attack Log

## Paper 08 v2

- Attack: ACS assumes perfect diagnostics.
  - Response: Added signature-noise stress. At active probability 0.35, valid-plan rate drops from 1.000 exact to 0.887 at 5% active-family misses, 0.766 at 10%, and 0.584 at 20%.
  - Residual risk: The stress is synthetic and does not calibrate perception/probe uncertainty.
- Attack: False positives can prune valid plans.
  - Response: The v2 CSV includes false-positive rows. In this simulator, 5% and 10% false positives keep valid-plan rate at 1.000 because an untagged conservative chain remains, but the paper states less forgiving graphs may lose completeness.
- Attack: The simulator supplies the family vocabulary and edge labels.
  - Response: Preserved as a limitation; ACS discovers active modeled families, not arbitrary new physics.
- Attack: No hardware or real TAMP benchmark.
  - Response: Terminal decision is workshop-only.
