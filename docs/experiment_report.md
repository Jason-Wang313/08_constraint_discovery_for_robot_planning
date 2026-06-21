# Experiment Report

This report now points to the full-scale evidence used by the final manuscript.
The older small sweep is still reproducible with `python scripts/run_experiments.py`,
but the final paper is based on `python scripts/run_full_scale_experiments.py`.

## Full-Scale Evidence

- Main scaling: `results/full_scale/main_scaling_trials.csv` and `results/full_scale/main_scaling_summary.csv`
- Diagnostic noise: `results/full_scale/signature_noise_trials.csv` and `results/full_scale/signature_noise_summary.csv`
- Planner labels: `results/full_scale/label_quality_trials.csv` and `results/full_scale/label_quality_summary.csv`
- False positives: `results/full_scale/false_positive_stress_trials.csv` and `results/full_scale/false_positive_stress_summary.csv`
- Cost sensitivity: `results/full_scale/cost_sensitivity_summary.csv` and `results/full_scale/cost_winner_summary.csv`
- Figures: `paper/figures/full_scale_*.pdf`

## Key Result

In the baseline topology at active-family probability 0.35, ACS has median total
cost 21.97, compared with 229.86 for blind repair, 61.55 for family repair,
68.14 for selected-path verification, and 120.16 for a perfect edge verifier.

See `docs/full_scale_results_summary.md` for the detailed final summary.

## Final Artifact

- Canonical PDF: `C:/Users/wangz/Downloads/08.pdf`
- Pages: 26
- Size: 397,753 bytes
- SHA256: `962CE3D8110DEE1A30DB3ABD31211CA3497048BDEB33415972E2EEB6CC717DB2`
- VLA-style boxed-link inventory: 63 annotations on pages `[(1, 13), (2, 35), (3, 6), (7, 2), (9, 4), (10, 2), (11, 1)]`; green = 54, red = 9, cyan = 0; all borders `(0, 0, 1)`.
- Visual audit: rendered pages 1, 2, 3, 7, 9, 10, and 11 after export and confirmed crisp, aligned link boxes.
