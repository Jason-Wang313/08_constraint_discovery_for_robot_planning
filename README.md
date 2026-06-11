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

## Notes

The simulator is a proof-of-mechanism abstraction, not a physical-robot validation. It assumes a known constraint-family vocabulary and exact diagnostic probes so the planning-side effect of pre-search active-set discovery can be isolated.
