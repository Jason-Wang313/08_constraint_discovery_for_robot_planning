# Hostile Prior Work Set

This is the 100-paper hostile set: papers most likely to make a constraint-discovery-before-planning paper look incremental. Fields are extracted from title, abstract, venue metadata, and keyword patterns, then used as an adversarial map rather than as definitive historical claims.

## 1. R-LGP: A Reachability-guided Logic-geometric Programming Framework for Optimal Task and Motion Planning on Mobile Manipulators (2024)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states; invalid plans can be repaired with tolerable execution/search cost
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; reactive repair once invalidity is observed; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 2. Guiding Long-Horizon Task and Motion Planning with Vision Language Models (2025)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states; invalid plans can be repaired with tolerable execution/search cost
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; reactive repair once invalidity is observed; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 3. Long-Horizon Multi-Robot Rearrangement Planning for Construction Assembly (2022)

- Venue/source: IEEE Transactions on Robotics
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 4. Accelerating Integrated Task and Motion Planning with Neural Feasibility Checking (2022)

- Venue/source: arXiv (Cornell University)
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 5. Reactive task and motion planning for robust whole-body dynamic locomotion in constrained environments (2022)

- Venue/source: The International Journal of Robotics Research
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states; task constraints are specified before execution
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema; logical proposition set
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; reactive repair once invalidity is observed; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 6. Counterexample-Guided Repair for Symbolic-Geometric Action Abstractions (2021)

- Venue/source: arXiv (Cornell University)
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; the relevant precondition vocabulary is supplied or learnable from traces; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances; mode switches caused by contact and support changes
- What it makes less novel: interleaving planning with geometric feasibility reasoning; learning symbolic action models; reactive repair once invalidity is observed
- What it leaves open: making the binding constraint set a pre-planning object; reducing expensive feasibility calls by discovering instance-level constraints

## 7. Continuous Optimization-Based Task and Motion Planning with Signal Temporal Logic Specifications for Sequential Manipulation (2021)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states; task constraints are specified before execution
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 8. Planning Robotic Manipulation with Tight Environment Constraints (2021)

- Venue/source: 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 9. Combined Task and Motion Planning as Classical AI Planning (2017)

- Venue/source: arXiv (Cornell University)
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 10. Learning Geometric Constraints in Task and Motion Planning (2022)

- Venue/source: arXiv (Cornell University)
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; training distribution covers deployment constraint activations; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema; feature space and training labels
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: learning constraints/feasibility models for planning; interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; separating constraint-family discovery from edge-by-edge verification

## 11. COAST: COnstraints And STreams for Task and Motion Planning (2024)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 12. AutoTAMP: Autoregressive Task and Motion Planning with LLMs as Translators and Checkers (2024)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 13. Extended Task and Motion Planning of Long-horizon Robot Manipulation. (2021)

- Venue/source: arXiv (Cornell University)
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 14. Fast MILP-based Task and Motion Planning for Pick-and-Place with Hard/Soft Constraints of Collision-Free Route (2021)

- Venue/source: 2021 IEEE International Conference on Systems, Man, and Cybernetics (SMC)
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 15. Discovering State and Action Abstractions for Generalized Task and Motion Planning (2022)

- Venue/source: Proceedings of the AAAI Conference on Artificial Intelligence
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; training distribution covers deployment constraint activations; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema; feature space and training labels
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: learning constraints/feasibility models for planning; interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; separating constraint-family discovery from edge-by-edge verification

## 16. Simultaneous Action and Grasp Feasibility Prediction for Task and Motion Planning Through Multi-Task Learning (2023)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; training distribution covers deployment constraint activations; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 17. An incremental constraint-based framework for task and motion planning (2018)

- Venue/source: The International Journal of Robotics Research
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances; mode switches caused by contact and support changes
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 18. CaStL: Constraints as Specifications Through Llm Translation for Long-Horizon Task and Motion Planning (2025)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 19. Incremental Task and Motion Planning: A Constraint-Based Approach (2016)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 20. Optimal Task and Motion Planning and Execution for Multiagent Systems in Dynamic Environments (2023)

- Venue/source: IEEE Transactions on Cybernetics
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 21. Dual-arm Assembly Planning Considering Gravitational Constraints (2019)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 22. The new analog: A protocol for linking design and construction intent with algorithmic planning for robotic assembly of complex structures (2021)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 23. Efficiently combining task and motion planning using geometric constraints (2014)

- Venue/source: The International Journal of Robotics Research
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 24. Sampling-based methods for factored task and motion planning (2018)

- Venue/source: The International Journal of Robotics Research
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances; mode switches caused by contact and support changes
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 25. A Survey of Optimization-based Task and Motion Planning: From Classical To Learning Approaches (2024)

- Venue/source: arXiv (Cornell University)
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; training distribution covers deployment constraint activations; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 26. PROTAMP-RRT: A Probabilistic Integrated Task and Motion Planner Based on RRT (2023)

- Venue/source: IEEE Robotics and Automation Letters
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances; mode switches caused by contact and support changes
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 27. Model Predictive Interaction Control for Robotic Manipulation Tasks (2022)

- Venue/source: IEEE Transactions on Robotics
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Induction of symbolic preconditions/effects or lifted operators from traces.
- Hidden assumptions: the relevant precondition vocabulary is supplied or learnable from traces; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: learning symbolic action models; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 28. Sequential Manipulation Planning on Scene Graph (2022)

- Venue/source: 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search
- Variables treated as fixed: object affordances/contact modes; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 29. Learning Feasibility for Task and Motion Planning in Tabletop Environments (2019)

- Venue/source: IEEE Robotics and Automation Letters
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; training distribution covers deployment constraint activations; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema; feature space and training labels
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: learning constraints/feasibility models for planning; interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; separating constraint-family discovery from edge-by-edge verification

## 30. Constraint propagation on interval bounds for dealing with geometric backtracking (2012)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; training distribution covers deployment constraint activations; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema; feature space and training labels
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: learning constraints/feasibility models for planning; interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; separating constraint-family discovery from edge-by-edge verification

## 31. Constraints on intervals for reducing the search space of geometric configurations (2012)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; training distribution covers deployment constraint activations; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema; feature space and training labels
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: learning constraints/feasibility models for planning; interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; separating constraint-family discovery from edge-by-edge verification

## 32. Sample-Based Methods for Factored Task and Motion Planning (2017)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 33. Search-based task and motion planning for hybrid systems: Agile autonomous vehicles (2023)

- Venue/source: Engineering Applications of Artificial Intelligence
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 34. Learning Symbolic Operators for Task and Motion Planning (2021)

- Venue/source: 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; training distribution covers deployment constraint activations; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema; feature space and training labels
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 35. Conflict-Directed Diverse Planning for Logic-Geometric Programming (2022)

- Venue/source: Proceedings of the International Conference on Automated Planning and Scheduling
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 36. Learning to Predict Action Feasibility for Task and Motion Planning in 3D Environments (2023)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; training distribution covers deployment constraint activations; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema; feature space and training labels
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 37. Case study in non-prehensile manipulation: planning and orbital stabilization of one-directional rollings for the “Butterfly” robot (2015)

- Venue/source: venue unknown
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 38. Fast Motion Planning in Dynamic Environments With Extended Predicate-Based Temporal Logic (2024)

- Venue/source: IEEE Transactions on Automation Science and Engineering
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Compilation of temporal specifications to automata or constrained search.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states; task constraints are specified before execution
- Variables treated as fixed: workspace geometry and robot model; logical proposition set
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: reactive repair once invalidity is observed; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 39. Mediating Between Contact Feasibility and Robustness of Trajectory Optimization Through Chance Complementarity Constraints (2022)

- Venue/source: Frontiers in Robotics and AI
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Continuous constrained optimization over trajectories or controls.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 40. Differentially constrained motion replanning using state lattices with graduated fidelity (2008)

- Venue/source: venue unknown
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Continuous constrained optimization over trajectories or controls.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states; invalid plans can be repaired with tolerable execution/search cost
- Variables treated as fixed: workspace geometry and robot model
- Failure modes ignored: ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: reactive repair once invalidity is observed; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object

## 41. Learning compositional models of robot skills for task and motion planning (2021)

- Venue/source: The International Journal of Robotics Research
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; training distribution covers deployment constraint activations; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: learning constraints/feasibility models for planning; interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; separating constraint-family discovery from edge-by-edge verification

## 42. Combining high-level causal reasoning with low-level geometric reasoning and motion planning for robotic manipulation (2011)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 43. FFRob: Leveraging symbolic planning for efficient task and motion planning (2017)

- Venue/source: The International Journal of Robotics Research
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances; mode switches caused by contact and support changes
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 44. Robotic disassembly for end-of-life products focusing on task and motion planning: A comprehensive survey (2024)

- Venue/source: Journal of Manufacturing Systems
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 45. Contingent Task and Motion Planning under Uncertainty for Human–Robot Interactions (2020)

- Venue/source: Applied Sciences
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances; mode switches caused by contact and support changes
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 46. Dual-Arm Mobile Manipulation Planning of a Long Deformable Object in Industrial Installation (2023)

- Venue/source: IEEE Robotics and Automation Letters
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 47. Multiple Mobile Robot Task and Motion Planning: A Survey (2022)

- Venue/source: ACM Computing Surveys
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 48. Combining task and motion planning for mobile manipulators (2020)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances; mode switches caused by contact and support changes
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 49. Constraint Graphs: Unifying task and motion planning for Navigation and Manipulation Among Movable Obstacles (2016)

- Venue/source: HAL (Le Centre pour la Communication Scientifique Directe)
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 50. Kinematics and Local Motion Planning for Quasi-static Whole-body Mobile Manipulation (2016)

- Venue/source: venue unknown
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Continuous constrained optimization over trajectories or controls.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 51. Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning (2022)

- Venue/source: IEEE Robotics and Automation Letters
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 52. Extended Tree Search for Robot Task and Motion Planning (2021)

- Venue/source: arXiv (Cornell University)
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 53. Sampling-based motion planning with reachable volumes for high-degree-of-freedom manipulators (2018)

- Venue/source: The International Journal of Robotics Research
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Sampling-based motion planning with constraint projection or rejection.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 54. Semantic grasping: Planning robotic grasps functionally suitable for an object manipulation task (2012)

- Venue/source: venue unknown
- Problem claimed: Predict which object-action relations are physically possible for embodied interaction.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: the planner's constraint set is either known or discoverable during ordinary search
- Variables treated as fixed: object affordances/contact modes
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: the broad claim that robot planning benefits from explicit constraints
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 55. Logic-geometric programming: an optimization-based approach to combined task and motion planning (2015)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 56. Sampling Based Motion Planning with Reachable Volumes (2016)

- Venue/source: OakTrust (Texas A&M University Libraries)
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Continuous constrained optimization over trajectories or controls.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 57. Grasp Planning Pipeline for Robust Manipulation of 3D Deformable Objects with Industrial Robotic Hand + Arm Systems (2020)

- Venue/source: Applied Sciences
- Problem claimed: Learn action preconditions/effects so a planner can compose robot skills.
- Actual mechanism introduced: Induction of symbolic preconditions/effects or lifted operators from traces.
- Hidden assumptions: the relevant precondition vocabulary is supplied or learnable from traces
- Variables treated as fixed: object affordances/contact modes
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: learning symbolic action models
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 58. Large language models for chemistry robotics (2023)

- Venue/source: Autonomous Robots
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 59. Motion planning with dynamics awareness for long reach manipulation in aerial robotic systems with two arms (2018)

- Venue/source: International Journal of Advanced Robotic Systems
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Inverse learning from observed behavior to recover costs, constraints, or action parameters.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states; invalid plans can be repaired with tolerable execution/search cost
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances; mode switches caused by contact and support changes
- What it makes less novel: reactive repair once invalidity is observed; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object

## 60. Full-body motion planning and control for the car egress task of the DARPA robotics challenge (2015)

- Venue/source: venue unknown
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Continuous constrained optimization over trajectories or controls.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 61. Optimal Grasps and Placements for Task and Motion Planning in Clutter (2023)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 62. Motion Planning for Aerial Pick-and-Place With Geometric Feasibility Constraints (2024)

- Venue/source: IEEE Transactions on Automation Science and Engineering
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 63. Formal design of robot Integrated Task and Motion Planning (2016)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states; task constraints are specified before execution
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema; logical proposition set
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 64. VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (2023)

- Venue/source: arXiv (Cornell University)
- Problem claimed: Predict which object-action relations are physically possible for embodied interaction.
- Actual mechanism introduced: A learned constraint or feasibility model used to bias, prune, or score plans.
- Hidden assumptions: training distribution covers deployment constraint activations
- Variables treated as fixed: object affordances/contact modes; feature space and training labels
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: learning constraints/feasibility models for planning
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; separating constraint-family discovery from edge-by-edge verification

## 65. Randomized path planning for linkages with closed kinematic chains (2001)

- Venue/source: IEEE Transactions on Robotics and Automation
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances; mode switches caused by contact and support changes
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 66. Motion Planning of Multi-Limbed Robots Subject to Equilibrium Constraints: The Free-Climbing Robot Problem (2006)

- Venue/source: The International Journal of Robotics Research
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 67. Robot motion planning with nonholonomic constraints (2003)

- Venue/source: venue unknown
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 68. Embodied Lifelong Learning for Task and Motion Planning (2023)

- Venue/source: arXiv (Cornell University)
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; training distribution covers deployment constraint activations; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema; feature space and training labels
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 69. A Collision-Free MPC for Whole-Body Dynamic Locomotion and Manipulation (2022)

- Venue/source: 2022 International Conference on Robotics and Automation (ICRA)
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 70. A constraint-based method for solving sequential manipulation planning problems (2014)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 71. Planning in-hand object manipulation with multifingered hands considering task constraints (2013)

- Venue/source: venue unknown
- Problem claimed: Plan manipulation under contact, grasp, object, and support constraints.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: feasibility queries are cheap enough to call inside search
- Variables treated as fixed: object affordances/contact modes
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: the broad claim that robot planning benefits from explicit constraints
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 72. Hierarchical Motion Planning With Dynamical Feasibility Guarantees for Mobile Robotic Vehicles (2011)

- Venue/source: IEEE Transactions on Robotics
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Continuous constrained optimization over trajectories or controls.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 73. Path planning for mobile manipulator robots under non-holonomic and task constraints (2020)

- Venue/source: venue unknown
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Sampling-based motion planning with constraint projection or rejection.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 74. Model-Predictive Motion Planning: Several Key Developments for Autonomous Mobile Robots (2014)

- Venue/source: IEEE Robotics & Automation Magazine
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Continuous constrained optimization over trajectories or controls.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 75. Learning to guide task and motion planning using score-space representation (2019)

- Venue/source: The International Journal of Robotics Research
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; training distribution covers deployment constraint activations; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema; feature space and training labels
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: learning constraints/feasibility models for planning; interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; separating constraint-family discovery from edge-by-edge verification

## 76. Autonomous Robot Planning System for In-Space Assembly of Reconfigurable Structures (2021)

- Venue/source: venue unknown
- Problem claimed: Recover when an initially planned robot behavior becomes invalid.
- Actual mechanism introduced: Detect failure after plan generation and modify the plan or search state.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; invalid plans can be repaired with tolerable execution/search cost
- Variables treated as fixed: object affordances/contact modes
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: reactive repair once invalidity is observed
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 77. Task and Motion Planning Is PSPACE-Complete (2020)

- Venue/source: Proceedings of the AAAI Conference on Artificial Intelligence
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 78. Planning approaches to constraint‐aware navigation in dynamic environments (2014)

- Venue/source: Computer Animation and Virtual Worlds
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Detect failure after plan generation and modify the plan or search state.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states; invalid plans can be repaired with tolerable execution/search cost
- Variables treated as fixed: workspace geometry and robot model
- Failure modes ignored: ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: reactive repair once invalidity is observed; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object

## 79. AND/OR net representation for robotic task sequence planning (1998)

- Venue/source: IEEE Transactions on Systems Man and Cybernetics Part C (Applications and Reviews)
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search
- Variables treated as fixed: symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 80. Smooth-RRT*: Asymptotically Optimal Motion Planning for Mobile Robots under Kinodynamic Constraints (2021)

- Venue/source: venue unknown
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Continuous constrained optimization over trajectories or controls.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 81. Robotic control and nonholonomic motion planning (1991)

- Venue/source: venue unknown
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 82. Combining task and motion planning for intersection assistance systems (2016)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 83. Task-Motion Planning System for Socially Viable Service Robots Based on Object Manipulation (2024)

- Venue/source: Biomimetics
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 84. Task planning using physics-based heuristics on manipulation actions (2016)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 85. A Hybrid Approach to Intricate Motion, Manipulation and Task Planning (2009)

- Venue/source: The International Journal of Robotics Research
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Induction of symbolic preconditions/effects or lifted operators from traces.
- Hidden assumptions: the relevant precondition vocabulary is supplied or learnable from traces; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: learning symbolic action models; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 86. Online Motion Planning for Deforming Maneuvering and Manipulation by Multilinked Aerial Robot Based on Differential Kinematics (2020)

- Venue/source: IEEE Robotics and Automation Letters
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 87. Fine-motion planning for robotic assembly under modelling and sensing uncertainties (1998)

- Venue/source: venue unknown
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 88. SyDeBO: Symbolic-Decision-Embedded Bilevel Optimization for Long-Horizon Manipulation in Dynamic Environments (2021)

- Venue/source: IEEE Access
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 89. Planning Motions Compliant to Complex Contact States (2001)

- Venue/source: The International Journal of Robotics Research
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Sampling-based motion planning with constraint projection or rejection.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 90. SMT-based synthesis of integrated task and motion plans from plan outlines (2014)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; mode switches caused by contact and support changes
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 91. Coordinated Motion Generation and Object Placement: A Reactive Planning and Landing Approach (2021)

- Venue/source: 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 92. Adversarial Actor-Critic Method for Task and Motion Planning Problems Using Planning Experience (2019)

- Venue/source: Proceedings of the AAAI Conference on Artificial Intelligence
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; training distribution covers deployment constraint activations; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema; feature space and training labels
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 93. Manipulation Task Planning and Motion Control Using Task Relaxations (2022)

- Venue/source: Journal of Control Automation and Electrical Systems
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 94. A direct method for trajectory optimization of rigid bodies through contact (2013)

- Venue/source: The International Journal of Robotics Research
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Continuous constrained optimization over trajectories or controls.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 95. Dextrous manipulation with rolling contacts (2002)

- Venue/source: venue unknown
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: A learned constraint or feasibility model used to bias, prune, or score plans.
- Hidden assumptions: training distribution covers deployment constraint activations; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model; feature space and training labels
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: learning constraints/feasibility models for planning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; separating constraint-family discovery from edge-by-edge verification

## 96. Perceptive Locomotion for Legged Robots in Rough Terrain (2018)

- Venue/source: Repository for Publications and Research Data (ETH Zurich)
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Continuous constrained optimization over trajectories or controls.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 97. An energy-based numerical continuation approach for quasi-static mechanical manipulation (2025)

- Venue/source: Data-Centric Engineering
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Planning architecture, learned model, or constraint formalism for robot decision making.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 98. DELTA: Decomposed Efficient Long-Term Robot Task Planning using Large Language Models (2024)

- Venue/source: arXiv (Cornell University)
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints

## 99. Humanoid Robot Locomotion and Manipulation Step Planning (2012)

- Venue/source: Advanced Robotics
- Problem claimed: Find feasible robot motions under collision, kinematic, dynamic, or environment constraints.
- Actual mechanism introduced: Inverse learning from observed behavior to recover costs, constraints, or action parameters.
- Hidden assumptions: continuous constraints can be evaluated locally at sampled states
- Variables treated as fixed: object affordances/contact modes; workspace geometry and robot model
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution

## 100. Active Model Learning and Diverse Action Sampling for Task and Motion Planning (2018)

- Venue/source: venue unknown
- Problem claimed: Bridge symbolic task choices and continuous geometric feasibility in robot planning.
- Actual mechanism introduced: Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks.
- Hidden assumptions: feasibility queries are cheap enough to call inside search; training distribution covers deployment constraint activations; the relevant precondition vocabulary is supplied or learnable from traces
- Variables treated as fixed: workspace geometry and robot model; symbolic operator schema; feature space and training labels
- Failure modes ignored: late discovery of a binding constraint after many invalid branches; ambiguous observations that hide which constraint family is active; constraint activations shifting across task instances
- What it makes less novel: interleaving planning with geometric feasibility reasoning; learning symbolic action models; constrained motion planning machinery
- What it leaves open: making the binding constraint set a pre-planning object; avoiding families of invalid plans before a first failed execution; reducing expensive feasibility calls by discovering instance-level constraints
