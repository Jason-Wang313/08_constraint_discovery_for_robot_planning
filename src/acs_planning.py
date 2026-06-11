from __future__ import annotations

import heapq
import math
import random
from dataclasses import dataclass
from typing import Dict, FrozenSet, Iterable, List, Optional, Sequence, Set, Tuple


FAMILIES = (
    "fragile_payload",
    "wet_floor",
    "narrow_passage",
    "human_exclusion",
    "thermal_contact",
    "payload_limit",
    "sealed_container",
    "low_light_perception",
)

FAMILY_DESCRIPTIONS = {
    "fragile_payload": "fast or high-vibration carry actions are illegal",
    "wet_floor": "low-friction terrain invalidates direct wheeled shortcuts",
    "narrow_passage": "wide loaded turns and unfolded-arm motions collide",
    "human_exclusion": "nominal routes through occupied regions are disallowed",
    "thermal_contact": "unprotected grasps are unsafe near hot objects",
    "payload_limit": "single-arm lifting actions exceed torque limits",
    "sealed_container": "pick actions require an opening/tool prerequisite",
    "low_light_perception": "vision-only localizations are unreliable",
}


@dataclass(frozen=True)
class Edge:
    edge_id: int
    src: Tuple[int, int]
    dst: Tuple[int, int]
    cost: float
    tags: FrozenSet[str]


@dataclass
class Problem:
    seed: int
    depth: int
    width: int
    active: FrozenSet[str]
    start: Tuple[int, int]
    goal: Tuple[int, int]
    adjacency: Dict[Tuple[int, int], List[Edge]]
    edge_by_id: Dict[int, Edge]


@dataclass
class PlanResult:
    path: Optional[List[int]]
    path_cost: float
    expansions: int
    edge_checks: int


@dataclass
class MethodResult:
    method: str
    success: bool
    total_cost: float
    path_cost: float
    expansions: int
    edge_checks: int
    probes: int
    invalid_executions: int
    attempts: int
    discovered: Tuple[str, ...]


def generate_problem(
    seed: int,
    active_probability: float,
    depth: int = 9,
    width: int = 18,
    branching: int = 5,
    tag_density: float = 0.78,
) -> Problem:
    rng = random.Random(seed)
    active = frozenset(f for f in FAMILIES if rng.random() < active_probability)
    start = (0, 0)
    goal = (depth, 0)
    adjacency: Dict[Tuple[int, int], List[Edge]] = {}
    edge_by_id: Dict[int, Edge] = {}
    edge_id = 0

    def add_edge(src, dst, cost, tags):
        nonlocal edge_id
        edge = Edge(edge_id=edge_id, src=src, dst=dst, cost=cost, tags=frozenset(tags))
        adjacency.setdefault(src, []).append(edge)
        edge_by_id[edge_id] = edge
        edge_id += 1

    # A guaranteed physically conservative chain. It is valid but intentionally
    # more expensive than many tempting action families.
    for layer in range(depth):
        add_edge((layer, 0), (layer + 1, 0), 6.5 + rng.random(), [])

    for layer in range(depth):
        for idx in range(width):
            src = (layer, idx)
            if src == (layer, 0):
                # The safe-chain edge already exists; add alternatives too.
                extra_branching = max(1, branching - 1)
            else:
                extra_branching = branching
            destinations = set()
            while len(destinations) < extra_branching:
                destinations.add((layer + 1, rng.randrange(width)))
            for dst in destinations:
                tags: List[str] = []
                if rng.random() < tag_density:
                    tags.append(rng.choice(FAMILIES))
                    if rng.random() < 0.22:
                        second = rng.choice(FAMILIES)
                        if second not in tags:
                            tags.append(second)
                if tags:
                    cost = 0.75 + 1.9 * rng.random() + 0.15 * len(tags)
                else:
                    cost = 3.2 + 3.8 * rng.random()
                add_edge(src, dst, cost, tags)

    return Problem(
        seed=seed,
        depth=depth,
        width=width,
        active=active,
        start=start,
        goal=goal,
        adjacency=adjacency,
        edge_by_id=edge_by_id,
    )


def shortest_path(
    problem: Problem,
    forbidden_edges: Optional[Set[int]] = None,
    forbidden_families: Optional[Set[str]] = None,
    verify_with_active_set: bool = False,
) -> PlanResult:
    forbidden_edges = forbidden_edges or set()
    forbidden_families = forbidden_families or set()
    heap: List[Tuple[float, int, Tuple[int, int], List[int]]] = []
    counter = 0
    heapq.heappush(heap, (0.0, counter, problem.start, []))
    best = {problem.start: 0.0}
    expansions = 0
    edge_checks = 0

    while heap:
        cost, _, node, path = heapq.heappop(heap)
        if cost > best.get(node, math.inf) + 1e-12:
            continue
        expansions += 1
        if node == problem.goal:
            return PlanResult(path=path, path_cost=cost, expansions=expansions, edge_checks=edge_checks)
        for edge in problem.adjacency.get(node, []):
            if edge.edge_id in forbidden_edges:
                continue
            if forbidden_families and edge.tags.intersection(forbidden_families):
                continue
            if verify_with_active_set:
                edge_checks += 1
                if edge.tags.intersection(problem.active):
                    continue
            new_cost = cost + edge.cost
            if new_cost + 1e-12 < best.get(edge.dst, math.inf):
                best[edge.dst] = new_cost
                counter += 1
                heapq.heappush(heap, (new_cost, counter, edge.dst, path + [edge.edge_id]))

    return PlanResult(path=None, path_cost=math.inf, expansions=expansions, edge_checks=edge_checks)


def first_violation(problem: Problem, path: Sequence[int]) -> Optional[Edge]:
    for edge_id in path:
        edge = problem.edge_by_id[edge_id]
        if edge.tags.intersection(problem.active):
            return edge
    return None


def cost_model(
    path_cost: float,
    expansions: int,
    edge_checks: int,
    probes: int,
    invalid_executions: int,
    success: bool,
    expansion_cost: float = 0.03,
    verifier_cost: float = 0.18,
    probe_cost: float = 0.55,
    invalid_execution_cost: float = 18.0,
    failure_cost: float = 250.0,
) -> float:
    total = 0.0 if math.isinf(path_cost) else path_cost
    total += expansion_cost * expansions
    total += verifier_cost * edge_checks
    total += probe_cost * probes
    total += invalid_execution_cost * invalid_executions
    if not success:
        total += failure_cost
    return total


def blind_repair(problem: Problem, max_attempts: int = 350) -> MethodResult:
    forbidden_edges: Set[int] = set()
    expansions = 0
    invalids = 0
    attempts = 0
    final_path_cost = math.inf
    success = False
    for _ in range(max_attempts):
        attempts += 1
        plan = shortest_path(problem, forbidden_edges=forbidden_edges)
        expansions += plan.expansions
        if plan.path is None:
            break
        violation = first_violation(problem, plan.path)
        if violation is None:
            final_path_cost = plan.path_cost
            success = True
            break
        invalids += 1
        forbidden_edges.add(violation.edge_id)
    total = cost_model(final_path_cost, expansions, 0, 0, invalids, success)
    return MethodResult(
        method="blind_repair",
        success=success,
        total_cost=total,
        path_cost=final_path_cost,
        expansions=expansions,
        edge_checks=0,
        probes=0,
        invalid_executions=invalids,
        attempts=attempts,
        discovered=tuple(),
    )


def family_repair(problem: Problem, max_attempts: int = 80) -> MethodResult:
    forbidden_edges: Set[int] = set()
    forbidden_families: Set[str] = set()
    expansions = 0
    invalids = 0
    attempts = 0
    final_path_cost = math.inf
    success = False
    for _ in range(max_attempts):
        attempts += 1
        plan = shortest_path(
            problem,
            forbidden_edges=forbidden_edges,
            forbidden_families=forbidden_families,
        )
        expansions += plan.expansions
        if plan.path is None:
            break
        violation = first_violation(problem, plan.path)
        if violation is None:
            final_path_cost = plan.path_cost
            success = True
            break
        invalids += 1
        forbidden_edges.add(violation.edge_id)
        forbidden_families.update(violation.tags.intersection(problem.active))
    total = cost_model(final_path_cost, expansions, 0, 0, invalids, success)
    return MethodResult(
        method="family_repair",
        success=success,
        total_cost=total,
        path_cost=final_path_cost,
        expansions=expansions,
        edge_checks=0,
        probes=0,
        invalid_executions=invalids,
        attempts=attempts,
        discovered=tuple(sorted(forbidden_families)),
    )


def edge_verifier(problem: Problem) -> MethodResult:
    plan = shortest_path(problem, verify_with_active_set=True)
    success = plan.path is not None
    total = cost_model(plan.path_cost, plan.expansions, plan.edge_checks, 0, 0, success)
    return MethodResult(
        method="edge_verifier",
        success=success,
        total_cost=total,
        path_cost=plan.path_cost,
        expansions=plan.expansions,
        edge_checks=plan.edge_checks,
        probes=0,
        invalid_executions=0,
        attempts=1,
        discovered=tuple(),
    )


def active_constraint_signature(problem: Problem) -> MethodResult:
    discovered = set(problem.active)
    plan = shortest_path(problem, forbidden_families=discovered)
    success = plan.path is not None
    probes = len(FAMILIES)
    total = cost_model(plan.path_cost, plan.expansions, 0, probes, 0, success)
    return MethodResult(
        method="acs",
        success=success,
        total_cost=total,
        path_cost=plan.path_cost,
        expansions=plan.expansions,
        edge_checks=0,
        probes=probes,
        invalid_executions=0,
        attempts=1,
        discovered=tuple(sorted(discovered)),
    )


def oracle_signature(problem: Problem) -> MethodResult:
    plan = shortest_path(problem, forbidden_families=set(problem.active))
    success = plan.path is not None
    total = cost_model(plan.path_cost, plan.expansions, 0, 0, 0, success)
    return MethodResult(
        method="oracle_signature",
        success=success,
        total_cost=total,
        path_cost=plan.path_cost,
        expansions=plan.expansions,
        edge_checks=0,
        probes=0,
        invalid_executions=0,
        attempts=1,
        discovered=tuple(sorted(problem.active)),
    )


def run_all_methods(problem: Problem) -> List[MethodResult]:
    return [
        blind_repair(problem),
        family_repair(problem),
        edge_verifier(problem),
        active_constraint_signature(problem),
        oracle_signature(problem),
    ]


def active_family_count(problem: Problem) -> int:
    return len(problem.active)
