# Final Audit

1. **Chosen thesis:** Robot planners should discover an instance's active physical constraint signature before task or motion search, rather than repairing invalid plans one edge at a time or calling a verifier on every candidate edge.

2. **Field assumption broken:** The timing of constraint discovery is not an implementation detail. Many robot-planning methods assume constraints are known, checked inside search, or repaired after failure; ACS breaks the assumption that late discovery has negligible planning cost.

3. **New central mechanism:** Active Constraint Signatures (ACS): a pre-planning diagnostic certificate that identifies active constraint families and masks entire action families before downstream planning.

4. **Genuine novelty:** The novelty is the planner-facing active-family certificate and its timing/granularity, not generic constraint learning, a verifier, plan repair, an LLM planner, uncertainty, or a new benchmark.

5. **Closest hostile prior work:** Task-and-motion planning with geometric constraints and streams (`PDDLStream`, FFRob, incremental constraint-based TAMP, COAST, R-LGP), learned geometric constraints and neural feasibility checking, action abstraction learning, counterexample/repair work, and LLM/VLM-guided TAMP.

6. **Literature coverage:** `docs/related_work_matrix.csv` contains 1000 entries. `docs/literature_map.md` records the 300-paper serious skim and 225-paper deep-read subset. `docs/hostile_prior_work.md` records 100 hostile prior papers with problem, mechanism, assumptions, fixed variables, ignored failures, novelty threats, and open space.

7. **Proof/formal-claim status:** A conditional finite-graph theorem is proved in `paper/main.tex`: if ACS returns the exact modeled active set and the downstream planner is complete on the masked graph, returned plans are valid and complete relative to modeled-valid paths. No guarantee is claimed for unmodeled constraints, false positives, or false negatives.

8. **Strongest evidence:** Runnable simulator in `src/acs_planning.py` and `scripts/run_experiments.py`. At active probability 0.35, ACS median total cost is 22.01 versus 261.01 for blind repair, 65.16 for family repair, and 116.79 for a perfect edge verifier. The v2 signature-noise stress shows valid-plan rate falls from 1.000 exact to 0.887 at 5% active-family misses, 0.766 at 10%, and 0.584 at 20%. Results are saved in `results/summary.csv`, `results/signature_noise_summary.csv`, and plotted in `figures/main_results.pdf`.

9. **Biggest weaknesses:** No physical robot validation; known constraint-family vocabulary; simulator-supplied edge labels; illustrative cost model; synthetic rather than calibrated diagnostic-noise stress; ACS loses when constraints are absent, probes are expensive, or false-negative diagnostics are common.

10. **Paper-readiness judgment:** Workshop-only for immediate submission; strong-revise for a main-conference target. The mechanism is crisp and runnable, and v2 adds the missing noisy-signature stress, but a full ICLR submission would need stronger empirical validation and ideally integration with a real TAMP benchmark or robot task.

11. **Exact Downloads PDF path:** `C:/Users/wangz/Downloads/08.pdf`

12. **GitHub URL:** `https://github.com/Jason-Wang313/08_constraint_discovery_for_robot_planning`

13. **Visible Desktop PDF status:** Present at `C:\Users\wangz\OneDrive\Desktop\08.pdf`; orchestrator copy appears complete.

## Orchestrator Desktop Copy

Checked: 2026-06-11 09:58:01 +01:00
Downloads PDF: C:/Users/wangz/Downloads/08.pdf
Result: copy script exit 0 log C:\Users\wangz\robotics_60_paper_batch\logs\desktop_copy_08_20260611_095759.log

## Submission-Hardening v2

Checked: 2026-06-12 21:42:25 +01:00
Terminal decision: workshop-only
Key change: added signature-noise stress and narrowed the claim to low-false-negative family diagnostics.
Canonical PDF target: C:/Users/wangz/Downloads/08.pdf, 161983 bytes
