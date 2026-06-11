# Novelty Decision

## Chosen Thesis

Robot planners should discover an instance's active physical constraint signature before task or motion search, rather than discovering the same constraint families one invalid edge, stream, or repaired plan at a time.

## Field Assumption Broken

The field often treats constraint knowledge as either known up front, queried edge-by-edge inside search, or recovered after a failed plan. The broken assumption is that this timing is mostly an implementation detail. The thesis here is that timing and granularity are central: when many candidate actions share the same latent physical constraint family, discovering the active family before search can remove whole invalid subtrees and avoid repeated invalid execution.

## New Central Mechanism

**Active Constraint Signatures (ACS):** a pre-planning diagnostic phase that maps scene cues and cheap robot probes to a compact set of active constraint families. The planner then masks action families and stream calls using this signature before graph expansion begins.

The mechanism is not a bigger model, a generic verifier, a plan repair module, or an LLM planner. It changes the object passed to the planner: from a planner with per-edge feasibility checks to a planner with an instance-level constraint-family certificate.

## Why This Survives the Hostile Set

The 100-paper hostile set contains strong work on task-and-motion planning, geometric streams, learned feasibility checks, symbolic-geometric repair, action-model learning, temporal constraints, and manipulation constraints. These make the following claims weak:

- "learn constraints for planning"
- "use a verifier during planning"
- "repair invalid plans"
- "add neural feasibility prediction to TAMP"
- "translate task constraints from language"

They leave a narrower opening:

- identify which constraint families are binding for this instance before planning;
- use that active set to remove entire equivalence classes of actions;
- quantify when this beats edge-level verification and repair-after-planning.

## Candidate Directions Considered

1. **Active constraint signatures before planning**: strongest because it changes timing, planner input, and search complexity.
2. **Constraint-family repair**: useful baseline, but still learns from a failed plan and is therefore less clean as a central contribution.
3. **Assumption stress tests for learned feasibility**: good evaluation angle, but benchmark-only without a mechanism would be weak.
4. **Planner-native precondition discovery**: close to action-model learning and risks being swallowed by existing precondition-learning work.
5. **Constraint activation certificates**: valuable framing, but best treated as the output of ACS rather than a separate paper.

## Chosen Paper Direction

Develop and evaluate ACS for robot task-planning abstractions where hidden physical properties activate constraint families such as fragile-object handling, payload limits, narrow-passage geometry, human exclusion zones, terrain restrictions, or tool requirements.

## Claim Boundary

Supported target claims:

- ACS reduces invalid executions relative to blind repair in environments where multiple low-cost plan branches share an active constraint family.
- ACS reduces expensive feasibility calls relative to edge-by-edge verification when diagnostic probes are cheaper than repeatedly checking candidate edges.
- ACS preserves ordinary planner completeness with respect to the pruned problem if the discovered active set is sound and complete for the modeled constraint families.

Unsupported or intentionally not claimed:

- ACS solves arbitrary unknown constraints outside the modeled family vocabulary.
- ACS eliminates the need for motion feasibility checking after the active signature is known.
- ACS is already validated on a physical robot.
- ACS dominates when constraints are rare, probes are expensive, or active-set discovery is noisy and uncalibrated.
