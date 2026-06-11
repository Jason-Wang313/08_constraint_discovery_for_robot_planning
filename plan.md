# Paper 08 Plan

## Objective
Produce a complete, anonymous ICLR-style robotics paper for `Constraint Discovery for Robot Planning`, with a defensible novelty boundary, runnable evidence, compiled PDF at `C:/Users/wangz/Downloads/08.pdf`, and a public GitHub repository named `08_constraint_discovery_for_robot_planning`.

## Execution Stages
1. Initialize status tracking and inspect the current repository without assuming prior artifacts are valid.
2. Build a broad literature corpus:
   - collect at least 1000 robot planning / constraint discovery / task-and-motion planning / learning-for-planning papers into `docs/related_work_matrix.csv`;
   - derive a 300-paper serious skim, a 200-250-paper deep-read subset, and a 100-paper hostile prior-work set;
   - write `docs/literature_map.md`, `docs/hostile_prior_work.md`, and `docs/novelty_boundary_map.md`.
3. Identify hidden assumptions in the field, propose directions that break them, choose the strongest thesis, and document the decision in `docs/novelty_decision.md`.
4. Develop a scoped method and evidence package:
   - implement a runnable toy robot-planning simulator where constraint discovery before planning is testable;
   - compare against repair-after-planning and verifier-style baselines;
   - save figures/tables/data and document commands.
5. Write claims and adversarial review artifacts:
   - `docs/claims.md`;
   - `docs/reviewer_attacks.md`;
   - `docs/final_audit.md`.
6. Create an anonymous ICLR-style LaTeX paper using the latest official ICLR template available at runtime or document fallback if unavailable.
7. Compile with direct `pdflatex`/`bibtex` passes and copy the final PDF only to `C:/Users/wangz/Downloads/08.pdf`.
8. Commit all reproducible source artifacts, create/push the public GitHub repository `08_constraint_discovery_for_robot_planning`, and record the URL or failure.

## Safety Rules
- Keep commands non-interactive and tolerant of expected failures.
- Use explicit long timeouts for retrieval, experiments, and LaTeX builds.
- Update `child_status.md` compactly after every major stage, rewriting it from current facts if needed.
- Do not delete or overwrite useful existing artifacts unless they are demonstrably invalid.
- Mark unsupported claims honestly rather than inflating novelty.
