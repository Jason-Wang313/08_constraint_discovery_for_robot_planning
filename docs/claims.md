# Claims

## Main Thesis Claim

Active Constraint Signatures (ACS) make the active constraint family set an explicit pre-planning object. In robot planning instances where many candidate actions share the same latent physical constraint family, discovering that family before search can reduce invalid executions and expensive feasibility calls relative to repair-after-planning or edge-by-edge verification.

Status: supported by the formal abstraction and runnable simulator, not yet by physical-robot experiments.

## Mechanism Claims

1. **Constraint-family granularity matters.**
   - Claim: Pruning one active family can remove many invalid candidate actions.
   - Evidence: In the simulator, each hidden physical property invalidates all macro-actions carrying the same family tag.
   - Boundary: This requires a meaningful family vocabulary. It does not apply if every invalid edge is idiosyncratic.

2. **Timing matters.**
   - Claim: Discovering active families before search can be cheaper than discovering them through failed executions.
   - Evidence: In the full-scale baseline topology at active probability 0.35, ACS median cost is 21.97 versus 229.86 for blind repair, 61.55 for family repair, 68.14 for selected-path verification, and 120.16 for edge verification.
   - Boundary: ACS pays diagnostic cost even when no constraint is active; at active probability 0.00, blind repair is cheaper.

3. **ACS is different from an edge verifier.**
   - Claim: ACS amortizes one family-level diagnostic across many candidate edges, while a verifier pays per considered edge.
   - Evidence: At active probability 0.35 in the full-scale baseline topology, edge verification averages 537.08 verifier calls, while ACS uses 8 probes and has lower median total cost. In the wide-dense topology, edge verification averages 1361.50 calls.
   - Boundary: If verifier calls are extremely cheap or probes are expensive, edge verification may be preferable.

4. **Sound signatures preserve completeness for the masked problem.**
   - Claim: If ACS returns exactly the active modeled constraint families and the downstream planner is complete on the pruned graph, then the planner is complete for feasible plans that avoid active-family violations.
   - Evidence: Direct proof in the paper; the simulator uses a conservative safe chain to ensure feasibility.
   - Boundary: This is not a completeness claim for unmodeled constraints or noisy discovery.

5. **False negatives and missing labels are the main safety failures.**
   - Claim: Missing active families or missing planner labels can destroy the planner-facing value of direct ACS because invalid low-cost branches remain in the graph.
   - Evidence: In the full-scale diagnostic-noise stress, direct ACS valid-plan rate is 0.828 at 10% independent false negatives and 0.708 at 10% correlated false negatives; selected-path fallback restores 1.000 in the tested abstraction. With 20% missing planner labels, direct ACS valid-plan rate is 0.412; fallback restores 1.000.
   - Boundary: The stresses are synthetic and do not replace calibrated real diagnostics or safety-rated hardware verification.

6. **The hostile prior-work boundary is timing plus certificate granularity.**
   - Claim: The novelty is not "learn constraints" or "check feasibility"; it is pre-search active-set certification that masks action families.
   - Evidence: The hostile set contains TAMP streams, neural feasibility checking, geometric constraints, plan repair, and action-model learning; the proposed boundary is the reusable active-family certificate.
   - Boundary: A paper that only calls a classifier per edge would be incremental.

## Unsupported Claims Not Made

- ACS has been validated on a real robot.
- ACS discovers arbitrary new constraint vocabularies from scratch.
- ACS replaces continuous motion planning or contact feasibility checking.
- ACS is robust to high false-negative diagnostic rates.
- ACS dominates when constraints are rare, probes are costly, or invalid execution is cheap.

## Evidence Artifacts

- `scripts/run_experiments.py`: regenerates all simulator evidence.
- `scripts/run_full_scale_experiments.py`: regenerates the full-scale operating-envelope evidence.
- `src/acs_planning.py`: simulator and planning baselines.
- `results/raw_trials.csv`: 5400 method-trial records.
- `results/summary.csv`: aggregate metrics.
- `results/full_scale/*.csv`: full-scale trial, summary, label, noise, false-positive, and cost-sensitivity artifacts.
- `figures/main_results.pdf`: main result plot.
- `paper/figures/full_scale_*.pdf`: full-scale manuscript figures.
- `docs/experiment_report.md`: experiment description and numeric table.
- `docs/full_scale_results_summary.md`: final full-scale result summary.
