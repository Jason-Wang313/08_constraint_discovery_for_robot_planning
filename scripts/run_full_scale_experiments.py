from __future__ import annotations

import csv
import json
import math
import random
import statistics
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, FrozenSet, Iterable, List, Optional, Sequence, Set, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from acs_planning import (  # noqa: E402
    FAMILIES,
    Edge,
    MethodResult,
    PlanResult,
    Problem,
    active_constraint_signature,
    blind_repair,
    cost_model,
    edge_verifier,
    family_repair,
    first_violation,
    generate_problem,
    oracle_signature,
    shortest_path,
)


RESULTS = ROOT / "results" / "full_scale"
FIGURES = ROOT / "paper" / "figures"
DOCS = ROOT / "docs"

DEFAULT_COSTS = {
    "expansion_cost": 0.03,
    "verifier_cost": 0.18,
    "probe_cost": 0.55,
    "invalid_execution_cost": 18.0,
    "failure_cost": 250.0,
}

TRIAL_FIELDS = [
    "suite",
    "profile",
    "condition",
    "variant",
    "active_probability",
    "trial",
    "seed",
    "method",
    "success",
    "total_cost",
    "path_cost",
    "expansions",
    "edge_checks",
    "probes",
    "invalid_executions",
    "attempts",
    "active_family_count",
    "active_families",
    "discovered_count",
    "missed_active_families",
    "false_positive_families",
    "extra",
]


@dataclass(frozen=True)
class TopologyProfile:
    name: str
    depth: int
    width: int
    branching: int
    tag_density: float
    trials: int


TOPOLOGY_PROFILES = [
    TopologyProfile("low_label_density", depth=9, width=18, branching=5, tag_density=0.45, trials=56),
    TopologyProfile("baseline", depth=9, width=18, branching=5, tag_density=0.78, trials=72),
    TopologyProfile("wide_dense", depth=10, width=26, branching=7, tag_density=0.82, trials=48),
    TopologyProfile("deep_sparse", depth=14, width=14, branching=4, tag_density=0.70, trials=48),
]


def ensure_dirs() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)


def fmt_float(value: float) -> str:
    if math.isinf(value):
        return "inf"
    if math.isnan(value):
        return "nan"
    return f"{value:.6f}"


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else float("nan")


def percentile(values: Sequence[float], q: float) -> float:
    if not values:
        return float("nan")
    ordered = sorted(values)
    pos = (len(ordered) - 1) * q
    lo = int(pos)
    hi = min(lo + 1, len(ordered) - 1)
    frac = pos - lo
    return ordered[lo] * (1.0 - frac) + ordered[hi] * frac


def write_csv(path: Path, rows: Iterable[dict], fieldnames: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def append_progress(stage: str, payload: dict) -> None:
    (RESULTS / "progress.json").write_text(
        json.dumps({"stage": stage, **payload}, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def method_row(
    *,
    suite: str,
    profile: str,
    condition: str,
    variant: str,
    active_probability: float,
    trial: int,
    seed: int,
    problem: Problem,
    result: MethodResult,
    extra: Optional[dict] = None,
) -> dict:
    discovered = set(result.discovered)
    active = set(problem.active)
    return {
        "suite": suite,
        "profile": profile,
        "condition": condition,
        "variant": variant,
        "active_probability": f"{active_probability:.2f}",
        "trial": trial,
        "seed": seed,
        "method": result.method,
        "success": str(result.success).lower(),
        "total_cost": fmt_float(result.total_cost),
        "path_cost": fmt_float(result.path_cost),
        "expansions": result.expansions,
        "edge_checks": result.edge_checks,
        "probes": result.probes,
        "invalid_executions": result.invalid_executions,
        "attempts": result.attempts,
        "active_family_count": len(problem.active),
        "active_families": "|".join(sorted(problem.active)),
        "discovered_count": len(discovered),
        "missed_active_families": len(active - discovered) if discovered else "",
        "false_positive_families": len(discovered - active) if discovered else "",
        "extra": json.dumps(extra or {}, sort_keys=True),
    }


def make_result(
    method: str,
    success: bool,
    path_cost: float,
    expansions: int,
    edge_checks: int,
    probes: int,
    invalid_executions: int,
    attempts: int,
    discovered: Iterable[str],
    costs: Optional[dict] = None,
) -> MethodResult:
    cost_kwargs = {**DEFAULT_COSTS, **(costs or {})}
    total = cost_model(
        path_cost,
        expansions,
        edge_checks,
        probes,
        invalid_executions,
        success,
        **cost_kwargs,
    )
    return MethodResult(
        method=method,
        success=success,
        total_cost=total,
        path_cost=path_cost,
        expansions=expansions,
        edge_checks=edge_checks,
        probes=probes,
        invalid_executions=invalid_executions,
        attempts=attempts,
        discovered=tuple(sorted(discovered)),
    )


def lazy_path_verifier(problem: Problem, max_attempts: int = 160) -> MethodResult:
    forbidden_edges: Set[int] = set()
    expansions = 0
    edge_checks = 0
    attempts = 0
    final_path_cost = math.inf
    success = False

    for _ in range(max_attempts):
        attempts += 1
        plan = shortest_path(problem, forbidden_edges=forbidden_edges)
        expansions += plan.expansions
        if plan.path is None:
            break

        rejected = None
        for edge_id in plan.path:
            edge_checks += 1
            edge = problem.edge_by_id[edge_id]
            if edge.tags.intersection(problem.active):
                rejected = edge.edge_id
                break
        if rejected is None:
            final_path_cost = plan.path_cost
            success = True
            break
        forbidden_edges.add(rejected)

    return make_result(
        "lazy_path_verifier",
        success,
        final_path_cost,
        expansions,
        edge_checks,
        probes=0,
        invalid_executions=0,
        attempts=attempts,
        discovered=[],
    )


def exact_acs_with_path_check(problem: Problem) -> MethodResult:
    discovered = set(problem.active)
    plan = shortest_path(problem, forbidden_families=discovered)
    edge_checks = len(plan.path or [])
    success = plan.path is not None
    return make_result(
        "acs_path_checked",
        success,
        plan.path_cost,
        plan.expansions,
        edge_checks,
        probes=len(FAMILIES),
        invalid_executions=0,
        attempts=1,
        discovered=discovered,
    )


def run_main_methods(problem: Problem) -> List[MethodResult]:
    return [
        blind_repair(problem),
        family_repair(problem),
        lazy_path_verifier(problem),
        edge_verifier(problem),
        active_constraint_signature(problem),
        exact_acs_with_path_check(problem),
        oracle_signature(problem),
    ]


def shortest_path_labeled(
    problem: Problem,
    forbidden_edges: Optional[Set[int]] = None,
    forbidden_families: Optional[Set[str]] = None,
    verify_with_active_set: bool = False,
    planner_tags: Optional[Dict[int, FrozenSet[str]]] = None,
    true_tags: Optional[Dict[int, FrozenSet[str]]] = None,
) -> PlanResult:
    import heapq

    forbidden_edges = forbidden_edges or set()
    forbidden_families = forbidden_families or set()
    planner_tags = planner_tags or {edge_id: edge.tags for edge_id, edge in problem.edge_by_id.items()}
    true_tags = true_tags or {edge_id: edge.tags for edge_id, edge in problem.edge_by_id.items()}
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
            labels = planner_tags.get(edge.edge_id, edge.tags)
            if forbidden_families and labels.intersection(forbidden_families):
                continue
            if verify_with_active_set:
                edge_checks += 1
                if true_tags.get(edge.edge_id, edge.tags).intersection(problem.active):
                    continue
            new_cost = cost + edge.cost
            if new_cost + 1e-12 < best.get(edge.dst, math.inf):
                best[edge.dst] = new_cost
                counter += 1
                heapq.heappush(heap, (new_cost, counter, edge.dst, path + [edge.edge_id]))

    return PlanResult(path=None, path_cost=math.inf, expansions=expansions, edge_checks=edge_checks)


def first_labeled_violation(
    problem: Problem,
    path: Optional[Sequence[int]],
    true_tags: Optional[Dict[int, FrozenSet[str]]] = None,
) -> Optional[Edge]:
    if path is None:
        return None
    true_tags = true_tags or {edge_id: edge.tags for edge_id, edge in problem.edge_by_id.items()}
    for edge_id in path:
        if true_tags.get(edge_id, problem.edge_by_id[edge_id].tags).intersection(problem.active):
            return problem.edge_by_id[edge_id]
    return None


def execute_noisy_acs(
    problem: Problem,
    discovered: Set[str],
    method: str,
    planner_tags: Optional[Dict[int, FrozenSet[str]]] = None,
    true_tags: Optional[Dict[int, FrozenSet[str]]] = None,
    probes: int = len(FAMILIES),
) -> MethodResult:
    plan = shortest_path_labeled(problem, forbidden_families=discovered, planner_tags=planner_tags, true_tags=true_tags)
    violation = first_labeled_violation(problem, plan.path, true_tags)
    success = plan.path is not None and violation is None
    invalids = 1 if violation is not None else 0
    return make_result(
        method,
        success,
        plan.path_cost,
        plan.expansions,
        edge_checks=0,
        probes=probes,
        invalid_executions=invalids,
        attempts=1,
        discovered=discovered,
    )


def acs_with_path_fallback(
    problem: Problem,
    discovered: Set[str],
    method: str,
    planner_tags: Optional[Dict[int, FrozenSet[str]]] = None,
    true_tags: Optional[Dict[int, FrozenSet[str]]] = None,
    max_attempts: int = 32,
) -> MethodResult:
    working = set(discovered)
    forbidden_edges: Set[int] = set()
    expansions = 0
    edge_checks = 0
    attempts = 0
    final_path_cost = math.inf
    success = False

    for _ in range(max_attempts):
        attempts += 1
        plan = shortest_path_labeled(
            problem,
            forbidden_edges=forbidden_edges,
            forbidden_families=working,
            planner_tags=planner_tags,
            true_tags=true_tags,
        )
        expansions += plan.expansions
        if plan.path is None:
            break

        violation = None
        for edge_id in plan.path:
            edge_checks += 1
            tags = (true_tags or {}).get(edge_id, problem.edge_by_id[edge_id].tags)
            active_tags = set(tags).intersection(problem.active)
            if active_tags:
                violation = edge_id
                forbidden_edges.add(edge_id)
                working.update(active_tags)
                break
        if violation is None:
            final_path_cost = plan.path_cost
            success = True
            break

    return make_result(
        method,
        success,
        final_path_cost,
        expansions,
        edge_checks=edge_checks,
        probes=len(FAMILIES),
        invalid_executions=0,
        attempts=attempts,
        discovered=working,
    )


def acs_abstain_to_edge_verifier(
    problem: Problem,
    discovered: Set[str],
    method: str,
    planner_tags: Dict[int, FrozenSet[str]],
    true_tags: Optional[Dict[int, FrozenSet[str]]] = None,
) -> MethodResult:
    masked = shortest_path_labeled(problem, forbidden_families=discovered, planner_tags=planner_tags, true_tags=true_tags)
    if masked.path is not None:
        violation = first_labeled_violation(problem, masked.path, true_tags)
        success = violation is None
        invalids = 1 if violation is not None else 0
        return make_result(
            method,
            success,
            masked.path_cost,
            masked.expansions,
            edge_checks=0,
            probes=len(FAMILIES),
            invalid_executions=invalids,
            attempts=1,
            discovered=discovered,
        )

    verified = shortest_path_labeled(
        problem,
        forbidden_families=set(),
        verify_with_active_set=True,
        planner_tags=planner_tags,
        true_tags=true_tags,
    )
    return make_result(
        method,
        verified.path is not None,
        verified.path_cost,
        masked.expansions + verified.expansions,
        edge_checks=verified.edge_checks,
        probes=len(FAMILIES),
        invalid_executions=0,
        attempts=2,
        discovered=discovered,
    )


def diagnose_signature(problem: Problem, rng: random.Random, scenario: str) -> Tuple[Set[str], dict]:
    discovered: Set[str] = set()
    fn_rate = 0.0
    fp_rate = 0.0
    correlated = False
    family_bias = False

    if scenario == "exact":
        fn_rate = 0.0
    elif scenario.startswith("fn_"):
        fn_rate = float(scenario.split("_")[1]) / 100.0
    elif scenario.startswith("fp_"):
        fp_rate = float(scenario.split("_")[1]) / 100.0
    elif scenario.startswith("mixed_"):
        _, fn_txt, fp_txt = scenario.split("_")
        fn_rate = float(fn_txt) / 100.0
        fp_rate = float(fp_txt) / 100.0
    elif scenario.startswith("correlated_fn_"):
        fn_rate = float(scenario.split("_")[-1]) / 100.0
        correlated = True
    elif scenario == "biased_payload_miss":
        family_bias = True
    else:
        raise ValueError(f"unknown noise scenario {scenario}")

    miss_all = correlated and rng.random() < fn_rate
    for family in FAMILIES:
        if family in problem.active:
            if family_bias:
                local_fn = 0.18 if family in {"fragile_payload", "payload_limit"} else 0.03
                keep = rng.random() >= local_fn
            elif miss_all:
                keep = False
            else:
                keep = rng.random() >= fn_rate
            if keep:
                discovered.add(family)
        elif rng.random() < fp_rate:
            discovered.add(family)

    active = set(problem.active)
    return discovered, {
        "fn_rate": fn_rate,
        "fp_rate": fp_rate,
        "correlated": correlated,
        "family_bias": family_bias,
        "missed": len(active - discovered),
        "false_positives": len(discovered - active),
    }


def make_planner_tags(problem: Problem, variant: str, rng: random.Random) -> Dict[int, FrozenSet[str]]:
    pair_map = {
        "fragile_payload": "payload_limit",
        "payload_limit": "fragile_payload",
        "wet_floor": "narrow_passage",
        "narrow_passage": "wet_floor",
        "human_exclusion": "low_light_perception",
        "low_light_perception": "human_exclusion",
        "thermal_contact": "sealed_container",
        "sealed_container": "thermal_contact",
    }
    labels: Dict[int, FrozenSet[str]] = {}
    for edge_id, edge in problem.edge_by_id.items():
        tags = set(edge.tags)
        if variant == "exact_labels":
            pass
        elif variant == "missing_10":
            tags = {tag for tag in tags if rng.random() >= 0.10}
        elif variant == "missing_20":
            tags = {tag for tag in tags if rng.random() >= 0.20}
        elif variant == "extra_10":
            if rng.random() < 0.10:
                choices = [family for family in FAMILIES if family not in tags]
                if choices:
                    tags.add(rng.choice(choices))
        elif variant == "extra_20":
            if rng.random() < 0.20:
                choices = [family for family in FAMILIES if family not in tags]
                if choices:
                    tags.add(rng.choice(choices))
        elif variant == "swap_10":
            swapped = set()
            for tag in tags:
                if rng.random() < 0.10:
                    choices = [family for family in FAMILIES if family != tag]
                    swapped.add(rng.choice(choices))
                else:
                    swapped.add(tag)
            tags = swapped
        elif variant == "coarse_pairs":
            tags = set(tags)
            for tag in list(tags):
                tags.add(pair_map[tag])
        elif variant == "sparse_coverage_30":
            if tags and rng.random() < 0.30:
                tags = set()
        else:
            raise ValueError(f"unknown label variant {variant}")
        labels[edge_id] = frozenset(tags)
    return labels


def make_bridge_false_positive_tags(
    problem: Problem,
    rng: random.Random,
) -> Tuple[Dict[int, FrozenSet[str]], str, int]:
    inactive = [family for family in FAMILIES if family not in problem.active]
    bridge_family = rng.choice(inactive or list(FAMILIES))
    bridge_layer = max(0, problem.depth // 2)
    labels = {edge_id: set(edge.tags) for edge_id, edge in problem.edge_by_id.items()}
    for edge_id, edge in problem.edge_by_id.items():
        if edge.src[0] == bridge_layer:
            labels[edge_id].add(bridge_family)
    return {edge_id: frozenset(tags) for edge_id, tags in labels.items()}, bridge_family, bridge_layer


def summarize_rows(rows: Iterable[dict], group_keys: Sequence[str]) -> List[dict]:
    grouped: Dict[Tuple[str, ...], List[dict]] = defaultdict(list)
    for row in rows:
        grouped[tuple(str(row[key]) for key in group_keys)].append(row)

    summaries: List[dict] = []
    for key, values in sorted(grouped.items()):
        costs = [float(row["total_cost"]) for row in values]
        invalids = [float(row["invalid_executions"]) for row in values]
        checks = [float(row["edge_checks"]) for row in values]
        expansions = [float(row["expansions"]) for row in values]
        probes = [float(row["probes"]) for row in values]
        attempts = [float(row["attempts"]) for row in values]
        successes = [1.0 if row["success"] == "true" else 0.0 for row in values]
        active_counts = [float(row["active_family_count"]) for row in values]
        summary = {group_keys[i]: key[i] for i in range(len(group_keys))}
        summary.update(
            {
                "trials": len(values),
                "success_rate": mean(successes),
                "mean_total_cost": mean(costs),
                "median_total_cost": statistics.median(costs),
                "p25_total_cost": percentile(costs, 0.25),
                "p75_total_cost": percentile(costs, 0.75),
                "mean_invalid_executions": mean(invalids),
                "mean_edge_checks": mean(checks),
                "mean_expansions": mean(expansions),
                "mean_probes": mean(probes),
                "mean_attempts": mean(attempts),
                "mean_active_family_count": mean(active_counts),
            }
        )
        summaries.append(summary)
    return summaries


def summary_fieldnames(group_keys: Sequence[str]) -> List[str]:
    return list(group_keys) + [
        "trials",
        "success_rate",
        "mean_total_cost",
        "median_total_cost",
        "p25_total_cost",
        "p75_total_cost",
        "mean_invalid_executions",
        "mean_edge_checks",
        "mean_expansions",
        "mean_probes",
        "mean_attempts",
        "mean_active_family_count",
    ]


def read_csv_rows(path: Path) -> List[dict]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def run_main_scaling() -> List[dict]:
    active_probabilities = [0.0, 0.05, 0.10, 0.20, 0.35, 0.50, 0.65, 0.80]
    out_path = RESULTS / "main_scaling_trials.csv"
    rows: List[dict] = []
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=TRIAL_FIELDS)
        writer.writeheader()
        for profile_index, profile in enumerate(TOPOLOGY_PROFILES):
            for p in active_probabilities:
                for trial in range(profile.trials):
                    seed = 2000000 + profile_index * 200000 + int(p * 1000) * 200 + trial
                    problem = generate_problem(
                        seed=seed,
                        active_probability=p,
                        depth=profile.depth,
                        width=profile.width,
                        branching=profile.branching,
                        tag_density=profile.tag_density,
                    )
                    for result in run_main_methods(problem):
                        row = method_row(
                            suite="main_scaling",
                            profile=profile.name,
                            condition="active_probability",
                            variant="default_cost",
                            active_probability=p,
                            trial=trial,
                            seed=seed,
                            problem=problem,
                            result=result,
                            extra={
                                "depth": profile.depth,
                                "width": profile.width,
                                "branching": profile.branching,
                                "tag_density": profile.tag_density,
                            },
                        )
                        writer.writerow(row)
                        rows.append(row)
                append_progress("main_scaling", {"profile": profile.name, "active_probability": p, "rows": len(rows)})
    summary = summarize_rows(rows, ["suite", "profile", "active_probability", "method"])
    write_csv(RESULTS / "main_scaling_summary.csv", summary, summary_fieldnames(["suite", "profile", "active_probability", "method"]))
    return summary


def run_noise_stress() -> List[dict]:
    scenarios = [
        "exact",
        "fn_02",
        "fn_05",
        "fn_10",
        "fn_20",
        "fp_05",
        "fp_10",
        "fp_20",
        "mixed_05_05",
        "mixed_10_05",
        "correlated_fn_05",
        "correlated_fn_10",
        "biased_payload_miss",
    ]
    active_probability = 0.35
    trials = 192
    out_path = RESULTS / "signature_noise_trials.csv"
    rows: List[dict] = []
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=TRIAL_FIELDS)
        writer.writeheader()
        for scenario_index, scenario in enumerate(scenarios):
            for trial in range(trials):
                seed = 3000000 + scenario_index * 20000 + trial
                problem = generate_problem(seed=seed, active_probability=active_probability)
                rng = random.Random(seed + 991)
                discovered, meta = diagnose_signature(problem, rng, scenario)
                for result in [
                    execute_noisy_acs(problem, set(discovered), "noisy_acs"),
                    acs_with_path_fallback(problem, set(discovered), "noisy_acs_path_fallback"),
                ]:
                    row = method_row(
                        suite="signature_noise",
                        profile="baseline",
                        condition=scenario,
                        variant="diagnostic_noise",
                        active_probability=active_probability,
                        trial=trial,
                        seed=seed,
                        problem=problem,
                        result=result,
                        extra=meta,
                    )
                    writer.writerow(row)
                    rows.append(row)
            append_progress("signature_noise", {"scenario": scenario, "rows": len(rows)})
    summary = summarize_rows(rows, ["suite", "condition", "method"])
    write_csv(RESULTS / "signature_noise_summary.csv", summary, summary_fieldnames(["suite", "condition", "method"]))
    return summary


def run_label_quality() -> List[dict]:
    variants = [
        "exact_labels",
        "missing_10",
        "missing_20",
        "extra_10",
        "extra_20",
        "swap_10",
        "coarse_pairs",
        "sparse_coverage_30",
    ]
    active_probability = 0.35
    trials = 160
    out_path = RESULTS / "label_quality_trials.csv"
    rows: List[dict] = []
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=TRIAL_FIELDS)
        writer.writeheader()
        for variant_index, variant in enumerate(variants):
            for trial in range(trials):
                seed = 4000000 + variant_index * 20000 + trial
                problem = generate_problem(seed=seed, active_probability=active_probability)
                rng = random.Random(seed + 1337)
                planner_tags = make_planner_tags(problem, variant, rng)
                exact_discovered = set(problem.active)
                results = [
                    execute_noisy_acs(problem, set(exact_discovered), "acs_with_planner_labels", planner_tags=planner_tags),
                    acs_with_path_fallback(problem, set(exact_discovered), "acs_labels_path_fallback", planner_tags=planner_tags),
                    edge_verifier(problem),
                    oracle_signature(problem),
                ]
                for result in results:
                    row = method_row(
                        suite="label_quality",
                        profile="baseline",
                        condition=variant,
                        variant="planner_label_quality",
                        active_probability=active_probability,
                        trial=trial,
                        seed=seed,
                        problem=problem,
                        result=result,
                        extra={"label_variant": variant},
                    )
                    writer.writerow(row)
                    rows.append(row)
            append_progress("label_quality", {"variant": variant, "rows": len(rows)})
    summary = summarize_rows(rows, ["suite", "condition", "method"])
    write_csv(RESULTS / "label_quality_summary.csv", summary, summary_fieldnames(["suite", "condition", "method"]))
    return summary


def run_false_positive_stress() -> List[dict]:
    active_probability = 0.10
    trials = 144
    conditions = ["ordinary_false_positive", "bridge_false_positive"]
    out_path = RESULTS / "false_positive_stress_trials.csv"
    rows: List[dict] = []
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=TRIAL_FIELDS)
        writer.writeheader()
        for condition in conditions:
            for trial in range(trials):
                seed = 5000000 + (0 if condition == "ordinary_false_positive" else 20000) + trial
                problem = generate_problem(seed=seed, active_probability=active_probability)
                rng = random.Random(seed + 771)
                inactive = [family for family in FAMILIES if family not in problem.active]
                fp_family = rng.choice(inactive or list(FAMILIES))
                planner_tags = {edge_id: edge.tags for edge_id, edge in problem.edge_by_id.items()}
                bridge_layer = None
                if condition == "bridge_false_positive":
                    planner_tags, fp_family, bridge_layer = make_bridge_false_positive_tags(problem, rng)
                discovered = set(problem.active)
                discovered.add(fp_family)
                results = [
                    execute_noisy_acs(problem, set(discovered), "acs_false_positive", planner_tags=planner_tags),
                    acs_abstain_to_edge_verifier(problem, set(discovered), "acs_abstain_to_verifier", planner_tags=planner_tags),
                    edge_verifier(problem),
                    oracle_signature(problem),
                ]
                for result in results:
                    row = method_row(
                        suite="false_positive_stress",
                        profile="baseline",
                        condition=condition,
                        variant="false_positive_completeness",
                        active_probability=active_probability,
                        trial=trial,
                        seed=seed,
                        problem=problem,
                        result=result,
                        extra={"false_positive_family": fp_family, "bridge_layer": bridge_layer},
                    )
                    writer.writerow(row)
                    rows.append(row)
            append_progress("false_positive_stress", {"condition": condition, "rows": len(rows)})
    summary = summarize_rows(rows, ["suite", "condition", "method"])
    write_csv(RESULTS / "false_positive_stress_summary.csv", summary, summary_fieldnames(["suite", "condition", "method"]))
    return summary


def recomputed_total(row: dict, costs: dict) -> float:
    return cost_model(
        float(row["path_cost"]),
        int(float(row["expansions"])),
        int(float(row["edge_checks"])),
        int(float(row["probes"])),
        int(float(row["invalid_executions"])),
        row["success"] == "true",
        **costs,
    )


def run_cost_sensitivity() -> List[dict]:
    active_probability = 0.35
    trials = 168
    behavior_rows: List[dict] = []
    for trial in range(trials):
        seed = 6000000 + trial
        problem = generate_problem(seed=seed, active_probability=active_probability)
        for result in run_main_methods(problem):
            behavior_rows.append(
                method_row(
                    suite="cost_sensitivity_behavior",
                    profile="baseline",
                    condition="behavior_components",
                    variant="default_behavior",
                    active_probability=active_probability,
                    trial=trial,
                    seed=seed,
                    problem=problem,
                    result=result,
                )
            )
    write_csv(RESULTS / "cost_sensitivity_behavior.csv", behavior_rows, TRIAL_FIELDS)

    probe_costs = [0.15, 0.35, 0.55, 1.00, 2.00, 4.00]
    invalid_costs = [1.0, 4.0, 8.0, 18.0, 40.0, 80.0]
    verifier_costs = [0.03, 0.08, 0.18, 0.40, 0.80]
    summary_rows: List[dict] = []
    grouped_by_method: Dict[str, List[dict]] = defaultdict(list)
    for row in behavior_rows:
        grouped_by_method[row["method"]].append(row)

    for probe_cost in probe_costs:
        for invalid_cost in invalid_costs:
            for verifier_cost in verifier_costs:
                costs = dict(DEFAULT_COSTS)
                costs.update(
                    {
                        "probe_cost": probe_cost,
                        "invalid_execution_cost": invalid_cost,
                        "verifier_cost": verifier_cost,
                    }
                )
                for method, rows in sorted(grouped_by_method.items()):
                    values = [recomputed_total(row, costs) for row in rows]
                    summary_rows.append(
                        {
                            "probe_cost": f"{probe_cost:.2f}",
                            "invalid_execution_cost": f"{invalid_cost:.2f}",
                            "verifier_cost": f"{verifier_cost:.2f}",
                            "method": method,
                            "trials": len(rows),
                            "median_total_cost": statistics.median(values),
                            "mean_total_cost": mean(values),
                            "p25_total_cost": percentile(values, 0.25),
                            "p75_total_cost": percentile(values, 0.75),
                        }
                    )

    fields = [
        "probe_cost",
        "invalid_execution_cost",
        "verifier_cost",
        "method",
        "trials",
        "median_total_cost",
        "mean_total_cost",
        "p25_total_cost",
        "p75_total_cost",
    ]
    write_csv(RESULTS / "cost_sensitivity_summary.csv", summary_rows, fields)

    winner_rows: List[dict] = []
    grouped: Dict[Tuple[str, str, str], List[dict]] = defaultdict(list)
    for row in summary_rows:
        grouped[(row["probe_cost"], row["invalid_execution_cost"], row["verifier_cost"])].append(row)
    for key, values in sorted(grouped.items()):
        non_oracle = [row for row in values if row["method"] != "oracle_signature"]
        best = min(non_oracle, key=lambda row: float(row["median_total_cost"]))
        acs = next(row for row in values if row["method"] == "acs")
        edge = next(row for row in values if row["method"] == "edge_verifier")
        family = next(row for row in values if row["method"] == "family_repair")
        winner_rows.append(
            {
                "probe_cost": key[0],
                "invalid_execution_cost": key[1],
                "verifier_cost": key[2],
                "best_non_oracle": best["method"],
                "best_non_oracle_median": best["median_total_cost"],
                "acs_median": acs["median_total_cost"],
                "acs_minus_best_non_oracle": float(acs["median_total_cost"]) - float(best["median_total_cost"]),
                "acs_minus_edge_verifier": float(acs["median_total_cost"]) - float(edge["median_total_cost"]),
                "acs_minus_family_repair": float(acs["median_total_cost"]) - float(family["median_total_cost"]),
            }
        )
    write_csv(
        RESULTS / "cost_winner_summary.csv",
        winner_rows,
        [
            "probe_cost",
            "invalid_execution_cost",
            "verifier_cost",
            "best_non_oracle",
            "best_non_oracle_median",
            "acs_median",
            "acs_minus_best_non_oracle",
            "acs_minus_edge_verifier",
            "acs_minus_family_repair",
        ],
    )
    append_progress("cost_sensitivity", {"rows": len(summary_rows)})
    return summary_rows


def pick_summary(
    rows: Sequence[dict],
    **criteria: str,
) -> Optional[dict]:
    for row in rows:
        if all(str(row.get(key)) == str(value) for key, value in criteria.items()):
            return row
    return None


def method_label(method: str) -> str:
    return {
        "blind_repair": "Blind repair",
        "family_repair": "Family repair",
        "lazy_path_verifier": "Path verifier",
        "edge_verifier": "Edge verifier",
        "acs": "ACS",
        "acs_path_checked": "ACS+path check",
        "oracle_signature": "Oracle",
        "noisy_acs": "Noisy ACS",
        "noisy_acs_path_fallback": "ACS+fallback",
        "acs_with_planner_labels": "ACS",
        "acs_labels_path_fallback": "ACS+fallback",
        "acs_false_positive": "ACS",
        "acs_abstain_to_verifier": "ACS+abstain",
    }.get(method, method.replace("_", " "))


def plot_main_scaling(summary: Sequence[dict]) -> None:
    baseline = [row for row in summary if row["profile"] == "baseline"]
    methods = ["blind_repair", "family_repair", "lazy_path_verifier", "edge_verifier", "acs", "acs_path_checked", "oracle_signature"]
    colors = {
        "blind_repair": "#8b1e3f",
        "family_repair": "#d97706",
        "lazy_path_verifier": "#7c3aed",
        "edge_verifier": "#2563eb",
        "acs": "#059669",
        "acs_path_checked": "#0f766e",
        "oracle_signature": "#374151",
    }
    fig, axes = plt.subplots(2, 2, figsize=(11.4, 7.2))
    by_method: Dict[str, List[dict]] = defaultdict(list)
    for row in baseline:
        by_method[row["method"]].append(row)
    for method in methods:
        vals = sorted(by_method.get(method, []), key=lambda row: float(row["active_probability"]))
        xs = [float(row["active_probability"]) for row in vals]
        axes[0, 0].plot(xs, [float(row["median_total_cost"]) for row in vals], marker="o", linewidth=1.7, label=method_label(method), color=colors[method])
        axes[0, 1].plot(xs, [float(row["mean_invalid_executions"]) for row in vals], marker="o", linewidth=1.5, label=method_label(method), color=colors[method])
        axes[1, 0].plot(xs, [float(row["mean_edge_checks"]) for row in vals], marker="o", linewidth=1.5, label=method_label(method), color=colors[method])

    p35 = [row for row in summary if row["active_probability"] == "0.35" and row["method"] == "acs"]
    p35_by_profile = sorted(p35, key=lambda row: row["profile"])
    axes[1, 1].bar(
        [row["profile"].replace("_", "\n") for row in p35_by_profile],
        [float(row["median_total_cost"]) for row in p35_by_profile],
        color="#059669",
    )
    axes[0, 0].set_title("Median total cost")
    axes[0, 1].set_title("Invalid executions")
    axes[1, 0].set_title("Verifier calls")
    axes[1, 1].set_title("ACS cost across topologies at p=0.35")
    axes[0, 0].set_ylabel("cost units")
    axes[0, 1].set_ylabel("mean count")
    axes[1, 0].set_ylabel("mean edge checks")
    axes[1, 1].set_ylabel("median cost units")
    for ax in [axes[0, 0], axes[0, 1], axes[1, 0]]:
        ax.set_xlabel("active-family probability")
        ax.grid(True, alpha=0.25)
    axes[1, 1].grid(True, axis="y", alpha=0.25)
    axes[0, 0].legend(fontsize=7, ncol=2, loc="upper left")
    fig.tight_layout()
    fig.savefig(FIGURES / "full_scale_main_scaling.pdf")
    fig.savefig(FIGURES / "full_scale_main_scaling.png", dpi=190)
    plt.close(fig)


def plot_noise(summary: Sequence[dict]) -> None:
    order = [
        "exact",
        "fn_02",
        "fn_05",
        "fn_10",
        "fn_20",
        "fp_10",
        "mixed_05_05",
        "correlated_fn_10",
        "biased_payload_miss",
    ]
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 3.8))
    width = 0.38
    for offset, method, color in [(-width / 2, "noisy_acs", "#059669"), (width / 2, "noisy_acs_path_fallback", "#2563eb")]:
        vals = [pick_summary(summary, condition=condition, method=method) for condition in order]
        xs = list(range(len(order)))
        axes[0].bar([x + offset for x in xs], [float(row["success_rate"]) if row else 0.0 for row in vals], width=width, label=method_label(method), color=color)
        axes[1].bar([x + offset for x in xs], [float(row["median_total_cost"]) if row else 0.0 for row in vals], width=width, label=method_label(method), color=color)
    for ax in axes:
        ax.set_xticks(list(range(len(order))))
        ax.set_xticklabels([label.replace("_", "\n") for label in order], fontsize=7)
        ax.grid(True, axis="y", alpha=0.25)
    axes[0].set_ylim(0, 1.05)
    axes[0].set_title("Valid-plan rate under signature noise")
    axes[1].set_title("Median cost under signature noise")
    axes[0].set_ylabel("success rate")
    axes[1].set_ylabel("cost units")
    axes[1].legend(fontsize=8, loc="upper left")
    fig.tight_layout()
    fig.savefig(FIGURES / "full_scale_signature_noise.pdf")
    fig.savefig(FIGURES / "full_scale_signature_noise.png", dpi=190)
    plt.close(fig)


def plot_label_quality(summary: Sequence[dict]) -> None:
    order = ["exact_labels", "missing_10", "missing_20", "extra_10", "extra_20", "swap_10", "coarse_pairs", "sparse_coverage_30"]
    methods = ["acs_with_planner_labels", "acs_labels_path_fallback"]
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 3.8))
    width = 0.36
    for offset, method, color in [(-width / 2, methods[0], "#059669"), (width / 2, methods[1], "#2563eb")]:
        vals = [pick_summary(summary, condition=condition, method=method) for condition in order]
        xs = list(range(len(order)))
        axes[0].bar([x + offset for x in xs], [float(row["success_rate"]) if row else 0.0 for row in vals], width=width, label=method_label(method), color=color)
        axes[1].bar([x + offset for x in xs], [float(row["median_total_cost"]) if row else 0.0 for row in vals], width=width, label=method_label(method), color=color)
    for ax in axes:
        ax.set_xticks(list(range(len(order))))
        ax.set_xticklabels([label.replace("_", "\n") for label in order], fontsize=7)
        ax.grid(True, axis="y", alpha=0.25)
    axes[0].set_ylim(0, 1.05)
    axes[0].set_title("Planner-label robustness")
    axes[1].set_title("Cost with imperfect labels")
    axes[0].set_ylabel("success rate")
    axes[1].set_ylabel("cost units")
    axes[1].legend(fontsize=8, loc="upper left")
    fig.tight_layout()
    fig.savefig(FIGURES / "full_scale_label_quality.pdf")
    fig.savefig(FIGURES / "full_scale_label_quality.png", dpi=190)
    plt.close(fig)


def plot_false_positive(summary: Sequence[dict]) -> None:
    conditions = ["ordinary_false_positive", "bridge_false_positive"]
    methods = ["acs_false_positive", "acs_abstain_to_verifier", "edge_verifier", "oracle_signature"]
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 3.8))
    width = 0.18
    colors = ["#059669", "#2563eb", "#7c3aed", "#374151"]
    for i, (method, color) in enumerate(zip(methods, colors)):
        offset = (i - 1.5) * width
        vals = [pick_summary(summary, condition=condition, method=method) for condition in conditions]
        xs = list(range(len(conditions)))
        axes[0].bar([x + offset for x in xs], [float(row["success_rate"]) if row else 0.0 for row in vals], width=width, label=method_label(method), color=color)
        axes[1].bar([x + offset for x in xs], [float(row["median_total_cost"]) if row else 0.0 for row in vals], width=width, label=method_label(method), color=color)
    for ax in axes:
        ax.set_xticks(list(range(len(conditions))))
        ax.set_xticklabels(["ordinary\nfalse positive", "bridge\nfalse positive"])
        ax.grid(True, axis="y", alpha=0.25)
    axes[0].set_ylim(0, 1.05)
    axes[0].set_title("False-positive completeness stress")
    axes[1].set_title("Fallback cost")
    axes[0].set_ylabel("success rate")
    axes[1].set_ylabel("cost units")
    axes[1].legend(fontsize=8, loc="upper left")
    fig.tight_layout()
    fig.savefig(FIGURES / "full_scale_false_positive_stress.pdf")
    fig.savefig(FIGURES / "full_scale_false_positive_stress.png", dpi=190)
    plt.close(fig)


def plot_cost_sensitivity() -> None:
    winner_rows = read_csv_rows(RESULTS / "cost_winner_summary.csv")
    probe_costs = [0.15, 0.35, 0.55, 1.00, 2.00, 4.00]
    invalid_costs = [1.0, 4.0, 8.0, 18.0, 40.0, 80.0]
    matrix = []
    for invalid in invalid_costs:
        row_values = []
        for probe in probe_costs:
            row = pick_summary(
                winner_rows,
                probe_cost=f"{probe:.2f}",
                invalid_execution_cost=f"{invalid:.2f}",
                verifier_cost=f"{DEFAULT_COSTS['verifier_cost']:.2f}",
            )
            row_values.append(float(row["acs_minus_best_non_oracle"]) if row else float("nan"))
        matrix.append(row_values)
    fig, ax = plt.subplots(figsize=(7.2, 4.7))
    vmax = max(abs(value) for row in matrix for value in row if not math.isnan(value))
    image = ax.imshow(matrix, cmap="coolwarm", vmin=-vmax, vmax=vmax, aspect="auto")
    ax.set_xticks(list(range(len(probe_costs))))
    ax.set_xticklabels([f"{value:.2f}" for value in probe_costs])
    ax.set_yticks(list(range(len(invalid_costs))))
    ax.set_yticklabels([f"{value:.0f}" for value in invalid_costs])
    ax.set_xlabel("probe cost")
    ax.set_ylabel("invalid execution cost")
    ax.set_title("ACS median cost minus best non-oracle")
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            ax.text(x, y, f"{value:.1f}", ha="center", va="center", fontsize=7)
    fig.colorbar(image, ax=ax, label="cost difference; negative favors ACS")
    fig.tight_layout()
    fig.savefig(FIGURES / "full_scale_cost_sensitivity.pdf")
    fig.savefig(FIGURES / "full_scale_cost_sensitivity.png", dpi=190)
    plt.close(fig)


def write_latex_tables(
    main_summary: Sequence[dict],
    noise_summary: Sequence[dict],
    label_summary: Sequence[dict],
    fp_summary: Sequence[dict],
) -> None:
    methods = ["blind_repair", "family_repair", "lazy_path_verifier", "edge_verifier", "acs", "acs_path_checked", "oracle_signature"]
    active_probs = ["0.00", "0.10", "0.35", "0.65", "0.80"]
    lines = [
        "\\begin{tabular}{lrrrrrrr}",
        "\\toprule",
        "Active prob. & Blind & Family & Path ver. & Edge ver. & ACS & ACS+check & Oracle \\\\",
        "\\midrule",
    ]
    for p in active_probs:
        values = []
        for method in methods:
            row = pick_summary(main_summary, profile="baseline", active_probability=p, method=method)
            values.append(f"{float(row['median_total_cost']):.2f}" if row else "--")
        lines.append(f"{float(p):.2f} & " + " & ".join(values) + " \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (RESULTS / "full_scale_main_cost_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

    noise_conditions = ["exact", "fn_02", "fn_05", "fn_10", "fn_20", "mixed_05_05", "correlated_fn_10"]
    lines = [
        "\\begin{tabular}{lrrrr}",
        "\\toprule",
        "Scenario & ACS valid & ACS cost & Fallback valid & Fallback cost \\\\",
        "\\midrule",
    ]
    for condition in noise_conditions:
        acs = pick_summary(noise_summary, condition=condition, method="noisy_acs")
        fallback = pick_summary(noise_summary, condition=condition, method="noisy_acs_path_fallback")
        lines.append(
            f"{condition.replace('_', '-')}"
            f" & {float(acs['success_rate']):.3f}"
            f" & {float(acs['median_total_cost']):.2f}"
            f" & {float(fallback['success_rate']):.3f}"
            f" & {float(fallback['median_total_cost']):.2f} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (RESULTS / "full_scale_noise_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

    label_conditions = ["exact_labels", "missing_10", "missing_20", "extra_20", "coarse_pairs", "sparse_coverage_30"]
    lines = [
        "\\begin{tabular}{lrrrr}",
        "\\toprule",
        "Label condition & ACS valid & ACS cost & Fallback valid & Fallback cost \\\\",
        "\\midrule",
    ]
    for condition in label_conditions:
        acs = pick_summary(label_summary, condition=condition, method="acs_with_planner_labels")
        fallback = pick_summary(label_summary, condition=condition, method="acs_labels_path_fallback")
        lines.append(
            f"{condition.replace('_', '-')}"
            f" & {float(acs['success_rate']):.3f}"
            f" & {float(acs['median_total_cost']):.2f}"
            f" & {float(fallback['success_rate']):.3f}"
            f" & {float(fallback['median_total_cost']):.2f} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (RESULTS / "full_scale_label_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

    lines = [
        "\\begin{tabular}{lrrrr}",
        "\\toprule",
        "Condition & ACS valid & ACS cost & Abstain valid & Abstain cost \\\\",
        "\\midrule",
    ]
    for condition in ["ordinary_false_positive", "bridge_false_positive"]:
        acs = pick_summary(fp_summary, condition=condition, method="acs_false_positive")
        abstain = pick_summary(fp_summary, condition=condition, method="acs_abstain_to_verifier")
        lines.append(
            f"{condition.replace('_', '-')}"
            f" & {float(acs['success_rate']):.3f}"
            f" & {float(acs['median_total_cost']):.2f}"
            f" & {float(abstain['success_rate']):.3f}"
            f" & {float(abstain['median_total_cost']):.2f} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (RESULTS / "full_scale_false_positive_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_report(
    main_summary: Sequence[dict],
    noise_summary: Sequence[dict],
    label_summary: Sequence[dict],
    fp_summary: Sequence[dict],
) -> None:
    baseline_035_acs = pick_summary(main_summary, profile="baseline", active_probability="0.35", method="acs")
    baseline_035_blind = pick_summary(main_summary, profile="baseline", active_probability="0.35", method="blind_repair")
    baseline_035_family = pick_summary(main_summary, profile="baseline", active_probability="0.35", method="family_repair")
    baseline_035_edge = pick_summary(main_summary, profile="baseline", active_probability="0.35", method="edge_verifier")
    noise_fn10 = pick_summary(noise_summary, condition="fn_10", method="noisy_acs")
    noise_fn10_fb = pick_summary(noise_summary, condition="fn_10", method="noisy_acs_path_fallback")
    label_missing20 = pick_summary(label_summary, condition="missing_20", method="acs_with_planner_labels")
    label_missing20_fb = pick_summary(label_summary, condition="missing_20", method="acs_labels_path_fallback")
    bridge_acs = pick_summary(fp_summary, condition="bridge_false_positive", method="acs_false_positive")
    bridge_abstain = pick_summary(fp_summary, condition="bridge_false_positive", method="acs_abstain_to_verifier")

    lines = [
        "# Full-Scale Results Summary",
        "",
        "## Scope",
        "",
        "This pass expands Paper 08 from the initial active-probability sweep into a broader operating-envelope study. The simulator is still a finite robot-task abstraction with known constraint families; the new evidence adds topology scaling, diagnostic-noise structure, planner-label quality, cost sensitivity, and false-positive completeness stress.",
        "",
        "## Main Scaling Result",
        "",
        (
            "In the baseline topology at active-family probability 0.35, ACS has median total cost "
            f"{float(baseline_035_acs['median_total_cost']):.2f}, compared with blind repair "
            f"{float(baseline_035_blind['median_total_cost']):.2f}, family repair "
            f"{float(baseline_035_family['median_total_cost']):.2f}, and edge verification "
            f"{float(baseline_035_edge['median_total_cost']):.2f}."
        ),
        "The expanded sweep includes low-label-density, baseline, wide-dense, and deep-sparse topologies. ACS remains strongest when active families invalidate many tempting low-cost edges; it is least useful when there is little family sharing or no active constraint to discover.",
        "",
        "## Diagnostic Noise",
        "",
        (
            "At a 10% independent false-negative rate, direct noisy ACS has valid-plan rate "
            f"{float(noise_fn10['success_rate']):.3f}; adding path-level fallback verification raises the rate to "
            f"{float(noise_fn10_fb['success_rate']):.3f} with median cost "
            f"{float(noise_fn10_fb['median_total_cost']):.2f}."
        ),
        "Correlated misses are worse than independent misses because one bad diagnostic event can leave an entire active set unmasked.",
        "",
        "## Planner Labels",
        "",
        (
            "With 20% missing planner labels, direct ACS has valid-plan rate "
            f"{float(label_missing20['success_rate']):.3f}, while ACS with path fallback reaches "
            f"{float(label_missing20_fb['success_rate']):.3f}."
        ),
        "Extra and coarse labels are generally safer but can increase cost by over-pruning valid shortcuts.",
        "",
        "## False-Positive Completeness Boundary",
        "",
        (
            "In the bridge false-positive construction, direct ACS succeeds at rate "
            f"{float(bridge_acs['success_rate']):.3f}; abstaining to an edge verifier when the mask disconnects the graph succeeds at rate "
            f"{float(bridge_abstain['success_rate']):.3f}."
        ),
        "This is the cleanest counterexample to a naive ACS claim: false positives can be safety-preserving but completeness-breaking.",
        "",
        "## Generated Artifacts",
        "",
        "- `results/full_scale/main_scaling_trials.csv` and `main_scaling_summary.csv`",
        "- `results/full_scale/signature_noise_trials.csv` and `signature_noise_summary.csv`",
        "- `results/full_scale/label_quality_trials.csv` and `label_quality_summary.csv`",
        "- `results/full_scale/false_positive_stress_trials.csv` and `false_positive_stress_summary.csv`",
        "- `results/full_scale/cost_sensitivity_summary.csv` and `cost_winner_summary.csv`",
        "- `paper/figures/full_scale_*.pdf`",
        "- `results/full_scale/full_scale_*_table.tex`",
    ]
    (DOCS / "full_scale_results_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_dirs()
    main_summary = run_main_scaling()
    noise_summary = run_noise_stress()
    label_summary = run_label_quality()
    fp_summary = run_false_positive_stress()
    run_cost_sensitivity()
    plot_main_scaling(main_summary)
    plot_noise(noise_summary)
    plot_label_quality(label_summary)
    plot_false_positive(fp_summary)
    plot_cost_sensitivity()
    write_latex_tables(main_summary, noise_summary, label_summary, fp_summary)
    write_report(main_summary, noise_summary, label_summary, fp_summary)
    append_progress(
        "complete",
        {
            "main_summary_rows": len(main_summary),
            "noise_summary_rows": len(noise_summary),
            "label_summary_rows": len(label_summary),
            "false_positive_summary_rows": len(fp_summary),
        },
    )
    print(f"Wrote full-scale results under {RESULTS}")
    print(f"Wrote full-scale figures under {FIGURES}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        ensure_dirs()
        append_progress("failed", {"error": repr(exc)})
        print(f"run_full_scale_experiments failed: {exc}", file=sys.stderr)
        raise
