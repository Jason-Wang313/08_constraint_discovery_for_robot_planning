# Reviewer Attacks

## Attack 1: This is just a learned feasibility checker before planning.

Response: A feasibility checker usually evaluates candidate edges, streams, or trajectories. ACS outputs a compact active-family signature once per problem instance and uses it to mask entire action families before search. The experiments compare against a perfect edge verifier; ACS wins when verifier calls are not free.

Weakness: If an implementation of ACS were merely a per-edge classifier, the novelty would collapse.

## Attack 2: Task-and-motion planning already reasons about constraints.

Response: The hostile set confirms that TAMP, PDDLStream-style streams, logic-geometric programming, and optimization-based planners all reason about constraints. The proposed difference is not the presence of constraints but when the binding subset is identified and how broadly each discovered constraint generalizes.

Weakness: The paper needs to avoid implying that TAMP lacks constraints. It should say TAMP often queries or samples feasibility during search, whereas ACS supplies an instance-level active set before expansion.

## Attack 3: Plan repair can generalize from a failure to a family.

Response: The experiments include `family_repair`, which generalizes after the first failed edge. ACS still avoids the first failed execution for each active family. This matters when invalid execution is expensive or unsafe.

Weakness: If failures are purely simulated and cheap, family repair may be enough.

## Attack 4: The simulator bakes in the answer.

Response: The simulator is intentionally an abstraction that isolates the mechanism: many low-cost branches share latent physical constraints. The paper should frame it as a stress test and proof-of-mechanism, not as complete empirical validation.

Weakness: A stronger paper would add a physical robot or established TAMP benchmark with real stream costs.

## Attack 5: The active constraint vocabulary is assumed known.

Response: Correct. ACS in this paper discovers which modeled families are active, not the family ontology itself. This assumption is narrower than claiming open-world constraint discovery, and it matches many robot deployments with known sensors/tools but unknown scene-specific activations.

Weakness: The title and abstract must not overstate "constraint discovery" as discovering arbitrary new physics.

## Attack 6: Diagnostics could be noisy or expensive.

Response: The main theorem assumes sound discovery and the simulator uses deterministic probes. The paper explicitly marks noise robustness as future work and shows ACS loses when no constraints are active because it pays diagnostic cost.

Weakness: Reviewers may demand a noisy-probe ablation. It is not present in the current evidence package.

## Attack 7: Edge verification is made too expensive.

Response: The cost model is transparent in `results/config.json`; verifier cost can be changed and the experiment rerun. The core condition is analytical: ACS is preferable when `K * probe_cost` is smaller than `edge_checks * verifier_cost` plus avoided invalid-execution cost.

Weakness: The paper should state this condition instead of claiming universal dominance.

## Attack 8: ACS may prune valid plans if it has false positives.

Response: The formal claim is conditional on sound and complete active-family detection for modeled families. False positives are outside the proved guarantee and would trade safety for completeness.

Weakness: The current paper does not solve calibrated abstention or recovery from mistaken signatures.

## Attack 9: The literature sweep is metadata-driven, not a full manual survey.

Response: The sweep is broad and reproducible, with a 1000-paper matrix, 300-paper skim, 225-paper deep subset, and 100-paper hostile set. The extraction fields are heuristic and should be used as a map, not as authoritative close readings.

Weakness: Some prior-work nuances may be missed; the final paper should cite the closest clusters conservatively.

## Attack 10: ICLR may expect learning novelty.

Response: The paper is an embodied planning paper with a learning-adjacent diagnostic front end, but its contribution is algorithmic and conceptual. It may be a better fit for robotics/planning venues or an ICLR workshop unless extended with learned diagnostics on real perceptual data.

Weakness: The final audit should probably judge it as workshop/revise rather than full-submit.
