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
   - Evidence: At active probability 0.35, ACS median cost is 22.01 versus 261.01 for blind edge repair and 65.16 for family repair.
   - Boundary: ACS pays diagnostic cost even when no constraint is active; at active probability 0.00, blind repair is cheaper.

3. **ACS is different from an edge verifier.**
   - Claim: ACS amortizes one family-level diagnostic across many candidate edges, while a verifier pays per considered edge.
   - Evidence: At active probability 0.35, edge verification averages 527.0 verifier calls, while ACS uses 8 probes and has lower median total cost.
   - Boundary: If verifier calls are extremely cheap or probes are expensive, edge verification may be preferable.

4. **Sound signatures preserve completeness for the masked problem.**
   - Claim: If ACS returns exactly the active modeled constraint families and the downstream planner is complete on the pruned graph, then the planner is complete for feasible plans that avoid active-family violations.
   - Evidence: Direct proof in the paper; the simulator uses a conservative safe chain to ensure feasibility.
   - Boundary: This is not a completeness claim for unmodeled constraints or noisy discovery.

5. **False negatives are the main diagnostic failure mode.**
   - Claim: Missing active families can destroy the planner-facing value of ACS because invalid low-cost branches remain in the graph.
   - Evidence: In the v2 signature-noise stress at active probability 0.35, valid-plan rate drops from 1.000 exact to 0.887 at 5% active-family misses, 0.766 at 10%, and 0.584 at 20%.
   - Boundary: The stress is synthetic and does not replace calibrated real diagnostics.

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
- `src/acs_planning.py`: simulator and planning baselines.
- `results/raw_trials.csv`: 5400 method-trial records.
- `results/summary.csv`: aggregate metrics.
- `results/signature_noise_stress.csv`: v2 noisy-signature stress.
- `results/signature_noise_summary.csv`: aggregate noisy-signature metrics.
- `figures/main_results.pdf`: main result plot.
- `docs/experiment_report.md`: experiment description and numeric table.
