# Novelty Boundary Map

## Areas That Are Not Novel Enough

- Learning a generic feasibility classifier and plugging it into a planner.
- Adding a verifier that rejects invalid plans during or after search.
- Repairing failed plans without changing the unit of generalization from edge to constraint family.
- Using an LLM or larger model to propose a task plan.
- Creating only a benchmark of invalid plans without a mechanism that changes planning behavior.
- Adding uncertainty estimates while leaving constraint activation as an edge-level property.
- Combining TAMP with learned affordances without a new planning-phase role for discovered constraints.

## Plausible Novel Boundary

A paper can claim a sharper contribution if it treats the active constraint set as an instance-level latent structure that is discovered before search, then proves or demonstrates that pruning by discovered constraint families changes the cost profile relative to repair-after-planning and edge-by-edge verification.

## Closest Hostile Clusters

### TAMP feasibility and geometric sampling

- R-LGP: A Reachability-guided Logic-geometric Programming Framework for Optimal Task and Motion Planning on Mobile Manipulators
- Guiding Long-Horizon Task and Motion Planning with Vision Language Models
- Long-Horizon Multi-Robot Rearrangement Planning for Construction Assembly
- Accelerating Integrated Task and Motion Planning with Neural Feasibility Checking
- Reactive task and motion planning for robust whole-body dynamic locomotion in constrained environments
- Counterexample-Guided Repair for Symbolic-Geometric Action Abstractions
- Continuous Optimization-Based Task and Motion Planning with Signal Temporal Logic Specifications for Sequential Manipulation
- Combined Task and Motion Planning as Classical AI Planning
- Learning Geometric Constraints in Task and Motion Planning
- COAST: COnstraints And STreams for Task and Motion Planning

### constrained motion planning

- Planning Robotic Manipulation with Tight Environment Constraints
- Case study in non-prehensile manipulation: planning and orbital stabilization of one-directional rollings for the “Butterfly” robot
- Fast Motion Planning in Dynamic Environments With Extended Predicate-Based Temporal Logic
- Mediating Between Contact Feasibility and Robustness of Trajectory Optimization Through Chance Complementarity Constraints
- Differentially constrained motion replanning using state lattices with graduated fidelity
- Dual-Arm Mobile Manipulation Planning of a Long Deformable Object in Industrial Installation
- Kinematics and Local Motion Planning for Quasi-static Whole-body Mobile Manipulation
- Sampling-based motion planning with reachable volumes for high-degree-of-freedom manipulators
- Sampling Based Motion Planning with Reachable Volumes
- Motion planning with dynamics awareness for long reach manipulation in aerial robotic systems with two arms

### action-model/precondition learning

- Model Predictive Interaction Control for Robotic Manipulation Tasks
- Grasp Planning Pipeline for Robust Manipulation of 3D Deformable Objects with Industrial Robotic Hand + Arm Systems
- A Hybrid Approach to Intricate Motion, Manipulation and Task Planning

### embodied planning constraints

- Semantic grasping: Planning robotic grasps functionally suitable for an object manipulation task
- Planning in-hand object manipulation with multifingered hands considering task constraints
- Autonomous Robot Planning System for In-Space Assembly of Reconfigurable Structures

### constraint or feasibility learning

- VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models
- Dextrous manipulation with rolling contacts

## Boundary Test

If the final method still calls a learned model or verifier per candidate edge, it falls inside hostile prior work. If it produces a reusable active-set certificate that masks entire action families before search and quantifies when that is cheaper than repair or verification, it crosses the proposed boundary.