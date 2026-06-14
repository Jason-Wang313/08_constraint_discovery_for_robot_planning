# Full-Scale Results Summary

## Scope

This pass expands Paper 08 from the initial active-probability sweep into a broader operating-envelope study. The simulator is still a finite robot-task abstraction with known constraint families; the new evidence adds topology scaling, diagnostic-noise structure, planner-label quality, cost sensitivity, and false-positive completeness stress.

## Main Scaling Result

In the baseline topology at active-family probability 0.35, ACS has median total cost 21.97, compared with blind repair 229.86, family repair 61.55, and edge verification 120.16.
The expanded sweep includes low-label-density, baseline, wide-dense, and deep-sparse topologies. ACS remains strongest when active families invalidate many tempting low-cost edges; it is least useful when there is little family sharing or no active constraint to discover.

## Diagnostic Noise

At a 10% independent false-negative rate, direct noisy ACS has valid-plan rate 0.828; adding path-level fallback verification raises the rate to 1.000 with median cost 24.80.
Correlated misses are worse than independent misses because one bad diagnostic event can leave an entire active set unmasked.

## Planner Labels

With 20% missing planner labels, direct ACS has valid-plan rate 0.412, while ACS with path fallback reaches 1.000.
Extra and coarse labels are generally safer but can increase cost by over-pruning valid shortcuts.

## False-Positive Completeness Boundary

In the bridge false-positive construction, direct ACS succeeds at rate 0.000; abstaining to an edge verifier when the mask disconnects the graph succeeds at rate 1.000.
This is the cleanest counterexample to a naive ACS claim: false positives can be safety-preserving but completeness-breaking.

## Generated Artifacts

- `results/full_scale/main_scaling_trials.csv` and `main_scaling_summary.csv`
- `results/full_scale/signature_noise_trials.csv` and `signature_noise_summary.csv`
- `results/full_scale/label_quality_trials.csv` and `label_quality_summary.csv`
- `results/full_scale/false_positive_stress_trials.csv` and `false_positive_stress_summary.csv`
- `results/full_scale/cost_sensitivity_summary.csv` and `cost_winner_summary.csv`
- `paper/figures/full_scale_*.pdf`
- `results/full_scale/full_scale_*_table.tex`
