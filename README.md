# Constraint Discovery for Robot Planning

This repository contains the source, literature artifacts, simulator, and ICLR-style paper for paper 08 in the robotics/embodied-intelligence batch.

## Thesis

Robot planners should discover an instance's active physical constraint signature before task or motion search, rather than repairing invalid plans one edge at a time or calling a verifier on every candidate edge.

## Main Artifacts

- `docs/related_work_matrix.csv`: 1000-paper landscape sweep.
- `docs/literature_map.md`: 300-paper skim and 225-paper deep-read map.
- `docs/hostile_prior_work.md`: 100-paper hostile prior-work set.
- `docs/novelty_decision.md`: selected thesis and novelty boundary.
- `src/acs_planning.py`: active-constraint-signature simulator and baselines.
- `scripts/run_experiments.py`: regenerates `results/` and `figures/main_results.*`.
- `scripts/run_full_scale_experiments.py`: regenerates the full-scale operating-envelope study.
- `results/full_scale/`: full-scale CSVs, summaries, and generated LaTeX tables.
- `paper/figures/`: full-scale paper figures.
- `paper/main.tex`: anonymous ICLR 2026-style manuscript.

## Reproduce

Install Python dependencies:

```powershell
python -m pip install -r requirements.txt
```

Regenerate the literature matrix and maps:

```powershell
python scripts/literature_pipeline.py
```

Regenerate the simulator results and figure:

```powershell
python scripts/run_experiments.py
```

Regenerate the full-scale evidence used by the final manuscript:

```powershell
python scripts/run_full_scale_experiments.py
```

Build the paper from `paper/`:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The required final PDF for the batch run is copied outside the repo to:

```text
C:/Users/wangz/Downloads/08.pdf
```

Current final export: 26 pages, 397,753 bytes, SHA256 `962CE3D8110DEE1A30DB3ABD31211CA3497048BDEB33415972E2EEB6CC717DB2`.

VLA-style boxed-link verification:

- Link annotations: 63 total on pages `[(1, 13), (2, 35), (3, 6), (7, 2), (9, 4), (10, 2), (11, 1)]`.
- Annotation colors: green = 54, red = 9, cyan = 0.
- Border widths: `(0, 0, 1)` for all link annotations.
- Visual audit: rendered pages 1, 2, 3, 7, 9, 10, and 11; green citation/URL boxes and red internal-reference boxes are crisp and aligned.

## Notes

The simulator is a proof-of-mechanism abstraction, not a physical-robot validation. It assumes a known constraint-family vocabulary and exact diagnostic probes in the main result so the planning-side effect of pre-search active-set discovery can be isolated.

## Full-Scale Final Pass

The final pass expands the manuscript to 26 pages and adds topology scaling,
diagnostic-noise, planner-label, false-positive, and cost-sensitivity studies.
In the baseline topology at active-family probability 0.35, ACS has median
total cost 21.97 versus 229.86 for blind repair, 61.55 for family repair, 68.14
for selected-path verification, and 120.16 for a perfect edge verifier.
