# Final Audit

Checked: 2026-06-14

1. **Chosen thesis:** Robot planners should discover an instance's active physical constraint signature before task or motion search, rather than repairing invalid plans one edge at a time or calling a verifier on every candidate edge.

2. **Field assumption broken:** Constraint-discovery timing is not an implementation detail. ACS challenges the assumption that late discovery through edge verification or repair has negligible planning cost.

3. **Central mechanism:** Active Constraint Signatures (ACS): a pre-planning diagnostic certificate that identifies active constraint families and masks entire action families before downstream planning.

4. **Novelty boundary:** The contribution is the planner-facing active-family certificate and its timing/granularity, not generic constraint learning, a verifier, plan repair, an LLM planner, uncertainty, or a new benchmark.

5. **Closest hostile prior work:** Task-and-motion planning with geometric constraints and streams (`PDDLStream`, FFRob, incremental constraint-based TAMP, COAST, R-LGP), learned geometric constraints and neural feasibility checking, action abstraction learning, counterexample/repair work, and LLM/VLM-guided TAMP.

6. **Literature coverage:** `docs/related_work_matrix.csv` contains 1000 entries. `docs/literature_map.md` records the 300-paper serious skim and 225-paper deep-read subset. `docs/hostile_prior_work.md` records 100 hostile prior papers.

7. **Proof/formal status:** `paper/main.tex` proves a conditional finite-graph guarantee: exact ACS signatures preserve validity and completeness relative to the modeled feasible masked graph. The paper explicitly excludes unmodeled constraints, false positives, false negatives, and hardware safety from the theorem.

8. **Strongest evidence:** `scripts/run_full_scale_experiments.py` generates topology scaling, diagnostic-noise, planner-label, false-positive, and cost-sensitivity suites. At active probability 0.35 in the baseline topology, ACS median total cost is 21.97 versus 229.86 for blind repair, 61.55 for family repair, 68.14 for selected-path verification, and 120.16 for a perfect edge verifier.

9. **Boundary evidence:** At a 10% independent false-negative rate, direct noisy ACS has valid-plan rate 0.828; selected-path fallback reaches 1.000 with median cost 24.80. With 20% missing planner labels, direct ACS valid-plan rate is 0.412; fallback reaches 1.000. In the bridge false-positive construction, direct ACS succeeds at 0.000 while abstaining to an edge verifier succeeds at 1.000.

10. **Biggest weaknesses:** No physical robot validation; known constraint-family vocabulary; simulator-supplied edge labels; illustrative cost model; synthetic diagnostic-noise stress; ACS loses when constraints are absent, probes are expensive, invalid execution is cheap, or labels/signatures are unreliable without fallback.

11. **Final paper status:** Full-scale final manuscript, 26 pages, simulation-scoped and submission-shaped. It is still honest that hardware or real TAMP benchmark validation would be required for a stronger empirical robotics claim.

12. **Exact Downloads PDF path:** `C:/Users/wangz/Downloads/08.pdf` (26 pages, 397,753 bytes, SHA256 `962CE3D8110DEE1A30DB3ABD31211CA3497048BDEB33415972E2EEB6CC717DB2`)

13. **Final PDF verification:** `C:/Users/wangz/Downloads/08.pdf`, 26 pages, 397,753 bytes, copied after LaTeX log, link, visual, and text scans passed. Local `paper/main.pdf` removed after copy.

14. **VLA-style boxed-link audit:** 63 link annotations on pages `[(1, 13), (2, 35), (3, 6), (7, 2), (9, 4), (10, 2), (11, 1)]`; colors green = 54, red = 9, cyan = 0; all borders `(0, 0, 1)`.

15. **Visual link audit:** pages 1, 2, 3, 7, 9, 10, and 11 rendered after export; green citation/URL boxes and red internal-reference boxes are crisp and aligned.

16. **GitHub URL:** `https://github.com/Jason-Wang313/08_constraint_discovery_for_robot_planning`

## VLA-Style Link Hardening

Checked: 2026-06-21
Action: Added `hyperref` plus explicit VLA-style `\hypersetup` policy, rebuilt with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`, copied the final PDF to Downloads, and removed local `paper/main.pdf`.
Decision: Final link styling matches the visible VLA-v4 role model; this pass added boxed links to a previously unlinked final PDF.
Downloads PDF: C:/Users/wangz/Downloads/08.pdf (26 pages, 397,753 bytes, SHA256 `962CE3D8110DEE1A30DB3ABD31211CA3497048BDEB33415972E2EEB6CC717DB2`)
Link audit: 63 annotations on pages `[(1, 13), (2, 35), (3, 6), (7, 2), (9, 4), (10, 2), (11, 1)]`; green = 54, red = 9, cyan = 0; all borders `(0, 0, 1)`.
Visual audit: rendered pages 1, 2, 3, 7, 9, 10, and 11; boxes are crisp and aligned.
Filename policy: no duplicate `C:/Users/wangz/Downloads/8.pdf` created.
