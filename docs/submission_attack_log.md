# Submission Attack Log

## Paper 08 full-scale final

- Attack: ACS assumes perfect diagnostics.
  - Response: Full-scale diagnostic-noise stress includes independent, correlated, mixed, and family-biased misses. At 10% independent false negatives, direct ACS valid-plan rate is 0.828; selected-path fallback restores 1.000 in the tested abstraction.
  - Residual risk: The stress is synthetic and does not calibrate real perception/probe uncertainty.
- Attack: False positives can prune valid plans.
  - Response: Bridge false-positive stress creates a mandatory cut with an inactive false-positive family. Direct ACS success is 0.000; abstaining to edge verification restores 1.000.
- Attack: The simulator supplies the family vocabulary and edge labels.
  - Response: Preserved as a limitation and tested with planner-label corruption. With 20% missing labels, direct ACS valid-plan rate is 0.412; fallback reaches 1.000 by checking and blacklisting rejected edges.
- Attack: No hardware or real TAMP benchmark.
  - Response: The final manuscript states simulation scope in the abstract, limitations, reproducibility, and conclusion. No hardware claim is made.
