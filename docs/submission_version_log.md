# Submission Version Log

## full-scale final - 2026-06-14

- Added `scripts/run_full_scale_experiments.py`.
- Added full-scale topology, diagnostic-noise, planner-label, false-positive, and cost-sensitivity suites under `results/full_scale/`.
- Added full-scale figures under `paper/figures/`.
- Expanded `paper/main.tex` to a 26-page final manuscript with fuller formal analysis, experiment protocol, results, limitations, and appendices.
- Updated reproducibility, audit, and readiness docs.
- Terminal decision: full-scale simulation-ready final; still no hardware-validation claim.

## Final-link-hardening - 2026-06-21

- Added `hyperref` plus explicit VLA-style `\hypersetup` policy for boxed PDF links; the prior final PDF had no link annotations.
- Rebuilt from `paper/` with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Canonical PDF: `C:/Users/wangz/Downloads/08.pdf` (26 pages, 397,753 bytes).
- SHA256: `962CE3D8110DEE1A30DB3ABD31211CA3497048BDEB33415972E2EEB6CC717DB2`.
- Link inventory: 63 annotations on pages `[(1, 13), (2, 35), (3, 6), (7, 2), (9, 4), (10, 2), (11, 1)]`; green = 54, red = 9, cyan = 0; all borders `(0, 0, 1)`.
- Rendered pages 1, 2, 3, 7, 9, 10, and 11 after export and confirmed crisp green citation/URL boxes and red internal-reference boxes.
- Local `paper/main.pdf` removed after the canonical copy.
- No additional `C:/Users/wangz/Downloads/8.pdf` duplicate was created.

## v2 - 2026-06-12

- Added `results/signature_noise_stress.csv`, `results/signature_noise_summary.csv`, and `results/signature_noise_table.tex`.
- Updated the experiment script to run false-negative and false-positive signature corruption stress.
- Updated manuscript, README, claims, reviewer attacks, final audit, and submission docs.
- Historical decision at that stage: workshop/revise.

## v1 - 2026-06-11

- Initial ACS paper package, literature audit, simulator evidence, compiled PDF, and GitHub push.
