# Experiment Report

## Simulator

The simulator is a layered robot task-planning abstraction. Edges are macro-actions such as direct navigation, grasp, carry, inspect, or tool-use choices. Hidden physical properties activate constraint families that invalidate every edge carrying that family tag.

Constraint families:

- `fragile_payload`: fast or high-vibration carry actions are illegal
- `wet_floor`: low-friction terrain invalidates direct wheeled shortcuts
- `narrow_passage`: wide loaded turns and unfolded-arm motions collide
- `human_exclusion`: nominal routes through occupied regions are disallowed
- `thermal_contact`: unprotected grasps are unsafe near hot objects
- `payload_limit`: single-arm lifting actions exceed torque limits
- `sealed_container`: pick actions require an opening/tool prerequisite
- `low_light_perception`: vision-only localizations are unreliable

## Methods

- `blind_repair`: plans ignoring constraints, executes, blacklists only the failed edge, and replans.
- `family_repair`: after a failed edge, generalizes to the violated constraint family and replans.
- `edge_verifier`: calls a perfect feasibility verifier on every candidate edge considered by Dijkstra search.
- `acs`: pays one diagnostic probe per constraint family, discovers the active signature, masks active families, and then plans.
- `oracle_signature`: plans with the true active family set and no diagnostic cost.

## Cost Model

- expansion_cost: 0.03
- verifier_cost: 0.18
- probe_cost: 0.55
- invalid_execution_cost: 18.0
- failure_cost: 250.0

## Main Result

| active probability | method | median total cost | mean invalid executions | mean verifier calls | success rate |
|---:|---|---:|---:|---:|---:|
| 0.00 | acs | 20.16 | 0.00 | 0.0 | 1.00 |
| 0.00 | blind_repair | 15.76 | 0.00 | 0.0 | 1.00 |
| 0.00 | edge_verifier | 128.74 | 0.00 | 625.0 | 1.00 |
| 0.00 | family_repair | 15.76 | 0.00 | 0.0 | 1.00 |
| 0.00 | oracle_signature | 15.76 | 0.00 | 0.0 | 1.00 |
| 0.10 | acs | 20.60 | 0.00 | 0.0 | 1.00 |
| 0.10 | blind_repair | 17.02 | 2.03 | 0.0 | 1.00 |
| 0.10 | edge_verifier | 127.20 | 0.00 | 606.9 | 1.00 |
| 0.10 | family_repair | 17.02 | 0.54 | 0.0 | 1.00 |
| 0.10 | oracle_signature | 16.20 | 0.00 | 0.0 | 1.00 |
| 0.20 | acs | 21.05 | 0.00 | 0.0 | 1.00 |
| 0.20 | blind_repair | 81.93 | 7.06 | 0.0 | 1.00 |
| 0.20 | edge_verifier | 123.76 | 0.00 | 586.3 | 1.00 |
| 0.20 | family_repair | 39.07 | 1.32 | 0.0 | 1.00 |
| 0.20 | oracle_signature | 16.65 | 0.00 | 0.0 | 1.00 |
| 0.35 | acs | 22.01 | 0.00 | 0.0 | 1.00 |
| 0.35 | blind_repair | 261.01 | 18.08 | 0.0 | 1.00 |
| 0.35 | edge_verifier | 116.79 | 0.00 | 527.0 | 1.00 |
| 0.35 | family_repair | 65.16 | 2.40 | 0.0 | 1.00 |
| 0.35 | oracle_signature | 17.61 | 0.00 | 0.0 | 1.00 |
| 0.50 | acs | 24.01 | 0.00 | 0.0 | 1.00 |
| 0.50 | blind_repair | 653.75 | 36.78 | 0.0 | 1.00 |
| 0.50 | edge_verifier | 112.39 | 0.00 | 482.4 | 1.00 |
| 0.50 | family_repair | 97.35 | 3.38 | 0.0 | 1.00 |
| 0.50 | oracle_signature | 19.61 | 0.00 | 0.0 | 1.00 |
| 0.65 | acs | 31.51 | 0.00 | 0.0 | 1.00 |
| 0.65 | blind_repair | 1447.38 | 62.76 | 0.0 | 1.00 |
| 0.65 | edge_verifier | 97.24 | 0.00 | 389.1 | 1.00 |
| 0.65 | family_repair | 134.94 | 4.71 | 0.0 | 1.00 |
| 0.65 | oracle_signature | 27.11 | 0.00 | 0.0 | 1.00 |

## Interpretation

At active probability 0.35, ACS has median cost 22.01, compared with blind repair 261.01, family repair 65.16, and edge verification 116.79.
The result is intended as runnable evidence for the mechanism, not as a physical-robot validation. It demonstrates the regime where discovering an active constraint family before planning is different from paying for failures or verifier calls inside search.
