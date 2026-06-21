# Paper 08 Full-Scale Execution Plan

Paper: `08_constraint_discovery_for_robot_planning`  
Working rule: finish this paper only, do not start Paper 09, and do not copy `08.pdf` to Downloads until the manuscript is verified as final, technically coherent, and at least 25 pages.

## Target Claim

The paper should make a narrow but strong claim: Active Constraint Signatures (ACS) are useful when many candidate plan edges share a small number of latent physical constraint families. In that regime, discovering the active family set before planning amortizes feasibility information across the search graph, reduces invalid executions, and avoids the verifier-call explosion of per-edge checking.

The paper must stay honest about the boundary:

- The evidence is simulation and formal abstraction, not hardware deployment.
- ACS assumes a predeclared diagnostic vocabulary of constraint families.
- False negatives in the signature are the central failure mode.
- ACS is not expected to dominate when active constraints are rare, probes are expensive, invalid execution is cheap, or edge labels are badly wrong.
- False positives can preserve safety while hurting completeness or cost, depending on graph slack.

## Current Gaps To Close

- The existing manuscript is too short for a submission-ready final version and still contains an old internal version marker.
- The existing experiment set supports the core idea but is not broad enough to expose the full operating envelope.
- The current result tables focus on active probability and basic signature noise; they do not yet stress graph topology, cost regimes, family granularity, edge-label quality, or recovery strategies.
- The manuscript needs deeper method explanation, more formal cost intuition, richer related-work positioning, fuller experimental detail, more figures, more tables, and stronger limitations.
- The final artifact must be built, visually/logically checked, copied to Downloads only after verification, and then removed from the local `paper/` directory.

## Full-Scale Experiment Suites

All experiment code must be RAM-light: stream or append CSV rows incrementally, avoid holding all trial objects in memory, use compact summaries, and split suites into commands that can resume safely.

1. Main scaling sweep
   - Vary active-family probability across the existing range plus denser points near the apparent break-even region.
   - Repeat across graph sizes, layer counts, branching factors, shortcut density, and family fanout.
   - Compare blind repair, family repair, edge verifier, lazy cached verification if feasible, ACS, noisy ACS, ACS with fallback verification, and oracle signature.

2. Active set and family-sharing structure
   - Stress sparse, moderate, and dense active family sets.
   - Compare independent edge-family assignment against clustered families where many edges share a latent hazard.
   - Quantify when family-level discovery has high or low amortization value.

3. Signature-noise taxonomy
   - Extend existing false-negative and false-positive sweeps.
   - Add correlated false negatives, family-specific miss rates, mixed false-positive/false-negative regimes, and abstention/reprobe variants.
   - Report valid-plan rate, invalid executions, cost, and failure modes separately.

4. Cost-model sensitivity
   - Sweep probe cost, verifier cost, invalid-execution penalty, expansion cost, and terminal failure penalty.
   - Produce break-even tables showing when ACS should lose, tie, or dominate.
   - Make the cost assumptions visible rather than hiding them behind a single parameterization.

5. Edge-label and vocabulary quality
   - Test missing labels, extra labels, mislabeled edges, overbroad family tags, and merged/split vocabularies.
   - Show whether ACS is robust to mild label noise and where semantic granularity breaks the benefit.

6. Completeness and conservatism stress
   - Construct cases where false positives remove cheap routes but leave expensive safe routes.
   - Construct cases where false positives remove all feasible routes.
   - Separate safety-preserving conservatism from practical planning failure.

7. Planner behavior diagnostics
   - Track verifier calls, probe calls, repaired families, replanning count, invalid executions, selected path length, expansion count, and terminal failures.
   - Include qualitative case studies of representative worlds that explain why each baseline wins or loses.

## Figures And Tables

Required final visual/table set:

- Main active-probability cost and validity curves.
- Method decomposition showing invalid executions, verifier calls, and probes.
- Graph-size/topology scaling plot.
- Signature-noise validity and cost plot.
- Cost-model break-even heatmap or table.
- Edge-label/vocabulary robustness plot.
- False-positive completeness stress table.
- One compact qualitative case-study diagram or table.

Figures should be generated from reproducible CSV outputs, not manually edited.

## Manuscript Expansion Plan

The final paper should be built as a real full manuscript, not padded text:

- Abstract: sharpen claim, evidence type, and boundary.
- Introduction: motivate constraint-family discovery before planning; explain why per-edge repair wastes structure.
- Contributions: formal ACS abstraction, planner integration, cost analysis, simulation benchmark, noise and boundary study.
- Related work: task and motion planning, lazy collision checking, constraint learning, safe planning, diagnostic probing, and sim-to-real/task feasibility distinctions.
- Problem setup: graph, edge families, active signatures, diagnostic observations, cost model, and assumptions.
- Method: ACS probe model, mask construction, planning algorithm, fallback variants, and implementation details.
- Formal analysis: soundness/completeness under exact signatures, amortization cost inequalities, and counterexamples for hostile regimes.
- Experiments: simulator, graph generation, baselines, metrics, suite design, statistical protocol, and RAM-light reproducibility.
- Results: one subsection per suite, with positive findings and explicit negative/boundary findings.
- Discussion: when ACS is the right abstraction, what it does not solve, and what hardware validation would need.
- Limitations: diagnostic vocabulary, label correctness, noisy signatures, no physical robot, no learned perception stack, no continuous dynamics proof.
- Reproducibility: commands, seeds, artifact layout, and exact outputs.
- Appendix: additional tables, algorithms, parameter grids, proofs, and case studies.

## Verification Checklist

Before copying anything to Downloads:

- `paper/main.tex` has no stale internal-process marker.
- Full-scale results, summaries, figures, and manuscript are updated.
- The PDF builds without fatal LaTeX errors, undefined references, missing citations, or serious overfull layout issues.
- `pdfinfo paper/main.pdf` reports at least 25 pages.
- The PDF text reflects the new full-scale results and does not contain placeholder language.
- The final copy is written to `C:\Users\wangz\Downloads\08.pdf` only after the above checks pass.
- After copying, remove local `paper/main.pdf`.
- Update final audit/reproducibility docs.
- Commit and push Paper 08 changes.
- Verify git status is clean and upstream matches before moving to Paper 09.

## Post-v3 VLA Link-Hardening Acceptance

Checked: 2026-06-21

- Active `paper/main.tex` now loads `hyperref` and the explicit VLA-style `\hypersetup` policy.
- Final PDF remains 26 pages and is exported to `C:/Users/wangz/Downloads/08.pdf`.
- Final export metadata: 397,753 bytes, SHA256 `962CE3D8110DEE1A30DB3ABD31211CA3497048BDEB33415972E2EEB6CC717DB2`.
- Link inventory: 63 annotations on pages `[(1, 13), (2, 35), (3, 6), (7, 2), (9, 4), (10, 2), (11, 1)]`; green = 54, red = 9, cyan = 0; all borders `(0, 0, 1)`.
- Visual audit rendered pages 1, 2, 3, 7, 9, 10, and 11 and confirmed crisp, aligned green citation/URL boxes and red internal-reference boxes.
- Local `paper/main.pdf` was removed after the canonical copy.
- No duplicate `C:/Users/wangz/Downloads/8.pdf` was created.
