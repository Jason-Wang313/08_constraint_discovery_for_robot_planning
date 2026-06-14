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

Response: The main theorem assumes sound discovery, and the full-scale stress suite makes the noisy case explicit. At active probability 0.35, direct ACS has valid-plan rate 0.828 at 10% independent false negatives and 0.708 at 10% correlated false negatives. Selected-path fallback restores 1.000 in the tested abstraction.

Weakness: The stress is synthetic and does not solve calibrated real diagnostics.

## Attack 7: Edge verification is made too expensive.

Response: The cost model is transparent in `results/config.json`; verifier cost can be changed and the experiment rerun. The core condition is analytical: ACS is preferable when `K * probe_cost` is smaller than `edge_checks * verifier_cost` plus avoided invalid-execution cost.

Weakness: The paper should state this condition instead of claiming universal dominance.

## Attack 8: ACS may prune valid plans if it has false positives.

Response: The formal claim is conditional on exact active-family detection for modeled families. The full-scale bridge false-positive construction shows the risk directly: direct ACS has success rate 0.000 when a false-positive family masks a mandatory cut. Abstaining to edge verification restores 1.000.

Weakness: The paper uses a simple abstention fallback, not a calibrated real-world uncertainty system.

## Attack 9: The literature sweep is metadata-driven, not a full manual survey.

Response: The sweep is broad and reproducible, with a 1000-paper matrix, 300-paper skim, 225-paper deep subset, and 100-paper hostile set. The extraction fields are heuristic and should be used as a map, not as authoritative close readings.

Weakness: Some prior-work nuances may be missed; the final paper should cite the closest clusters conservatively.

## Attack 10: ICLR may expect learning novelty.

Response: The paper is an embodied planning paper with a learning-adjacent diagnostic front end, but its contribution is algorithmic and conceptual. It may be a better fit for robotics/planning venues or an ICLR workshop unless extended with learned diagnostics on real perceptual data.

Weakness: The final paper is full-scale and submission-shaped as a simulation study, but a stronger empirical robotics claim still needs learned or calibrated diagnostics on a real benchmark or robot.
