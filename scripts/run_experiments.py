import csv
import json
import random
import statistics
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from acs_planning import (
    FAMILIES,
    FAMILY_DESCRIPTIONS,
    cost_model,
    first_violation,
    generate_problem,
    run_all_methods,
    shortest_path,
)


RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
DOCS = ROOT / "docs"


def ensure_dirs():
    RESULTS.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)


def mean(xs):
    return sum(xs) / len(xs) if xs else float("nan")


def percentile(xs, q):
    if not xs:
        return float("nan")
    ys = sorted(xs)
    pos = (len(ys) - 1) * q
    lo = int(pos)
    hi = min(lo + 1, len(ys) - 1)
    frac = pos - lo
    return ys[lo] * (1.0 - frac) + ys[hi] * frac


def summarize(rows):
    grouped = defaultdict(list)
    for row in rows:
        grouped[(row["active_probability"], row["method"])].append(row)
    summary = []
    for (p, method), vals in sorted(grouped.items()):
        total_costs = [float(v["total_cost"]) for v in vals]
        invalids = [float(v["invalid_executions"]) for v in vals]
        checks = [float(v["edge_checks"]) for v in vals]
        expansions = [float(v["expansions"]) for v in vals]
        successes = [1.0 if v["success"] == "true" else 0.0 for v in vals]
        summary.append(
            {
                "active_probability": p,
                "method": method,
                "trials": len(vals),
                "mean_total_cost": mean(total_costs),
                "median_total_cost": statistics.median(total_costs),
                "p25_total_cost": percentile(total_costs, 0.25),
                "p75_total_cost": percentile(total_costs, 0.75),
                "mean_invalid_executions": mean(invalids),
                "mean_edge_checks": mean(checks),
                "mean_expansions": mean(expansions),
                "success_rate": mean(successes),
            }
        )
    return summary


def write_csv(path, rows, fieldnames):
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def noisy_signature_trial(problem, rng, false_negative_rate, false_positive_rate):
    discovered = set()
    for family in FAMILIES:
        if family in problem.active:
            if rng.random() >= false_negative_rate:
                discovered.add(family)
        elif rng.random() < false_positive_rate:
            discovered.add(family)

    plan = shortest_path(problem, forbidden_families=discovered)
    violation = None if plan.path is None else first_violation(problem, plan.path)
    success = plan.path is not None and violation is None
    invalid_executions = 1 if violation is not None else 0
    total = cost_model(
        plan.path_cost,
        plan.expansions,
        0,
        len(FAMILIES),
        invalid_executions,
        success,
    )
    missed = len(set(problem.active) - discovered)
    false_positives = len(discovered - set(problem.active))
    return {
        "success": success,
        "total_cost": total,
        "path_cost": plan.path_cost,
        "expansions": plan.expansions,
        "invalid_executions": invalid_executions,
        "missed_active_families": missed,
        "false_positive_families": false_positives,
    }


def run_signature_noise_stress(active_probability=0.35, trials=180, repeats=5):
    scenarios = [
        ("exact", 0.00, 0.00),
        ("miss_0.02", 0.02, 0.00),
        ("miss_0.05", 0.05, 0.00),
        ("miss_0.10", 0.10, 0.00),
        ("miss_0.20", 0.20, 0.00),
        ("false_positive_0.05", 0.00, 0.05),
        ("false_positive_0.10", 0.00, 0.10),
    ]
    rows = []
    for scenario, fn_rate, fp_rate in scenarios:
        for repeat in range(repeats):
            random_seed = 900000 + repeat * 10000 + int(fn_rate * 1000) * 100 + int(fp_rate * 1000)
            local_rng = random.Random(random_seed)
            for trial in range(trials):
                seed = 910000 + int(active_probability * 1000) * 1000 + repeat * 10000 + trial
                problem = generate_problem(seed=seed, active_probability=active_probability)
                result = noisy_signature_trial(problem, local_rng, fn_rate, fp_rate)
                rows.append(
                    {
                        "scenario": scenario,
                        "active_probability": f"{active_probability:.2f}",
                        "repeat": repeat,
                        "trial": trial,
                        "false_negative_rate": f"{fn_rate:.2f}",
                        "false_positive_rate": f"{fp_rate:.2f}",
                        "active_family_count": len(problem.active),
                        "success": str(result["success"]).lower(),
                        "total_cost": f"{result['total_cost']:.6f}",
                        "path_cost": f"{result['path_cost']:.6f}",
                        "expansions": result["expansions"],
                        "invalid_executions": result["invalid_executions"],
                        "missed_active_families": result["missed_active_families"],
                        "false_positive_families": result["false_positive_families"],
                    }
                )
    return rows


def summarize_signature_noise(rows):
    grouped = defaultdict(list)
    for row in rows:
        grouped[row["scenario"]].append(row)
    summary = []
    for scenario, vals in grouped.items():
        costs = [float(v["total_cost"]) for v in vals]
        successes = [1.0 if v["success"] == "true" else 0.0 for v in vals]
        invalids = [float(v["invalid_executions"]) for v in vals]
        missed = [float(v["missed_active_families"]) for v in vals]
        fps = [float(v["false_positive_families"]) for v in vals]
        first = vals[0]
        summary.append(
            {
                "scenario": scenario,
                "false_negative_rate": first["false_negative_rate"],
                "false_positive_rate": first["false_positive_rate"],
                "trials": len(vals),
                "success_rate": mean(successes),
                "median_total_cost": statistics.median(costs),
                "mean_invalid_executions": mean(invalids),
                "mean_missed_active_families": mean(missed),
                "mean_false_positive_families": mean(fps),
            }
        )
    return sorted(summary, key=lambda r: (float(r["false_positive_rate"]) > 0, float(r["false_negative_rate"]), float(r["false_positive_rate"])))


def write_signature_noise_table(summary):
    wanted = ["exact", "miss_0.02", "miss_0.05", "miss_0.10", "miss_0.20"]
    by = {row["scenario"]: row for row in summary}
    labels = ["0\\%", "2\\%", "5\\%", "10\\%", "20\\%"]
    lines = [
        "\\begin{tabular}{lrrrrr}",
        "\\toprule",
        "Metric & " + " & ".join(labels) + " \\\\",
        "\\midrule",
    ]
    metrics = [
        ("success_rate", "Valid-plan rate", "{:.3f}"),
        ("median_total_cost", "Median total cost", "{:.2f}"),
        ("mean_invalid_executions", "Invalid executions", "{:.2f}"),
    ]
    for key, label, fmt in metrics:
        values = [fmt.format(float(by[scenario][key])) for scenario in wanted]
        lines.append(f"{label} & " + " & ".join(values) + " \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (RESULTS / "signature_noise_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def plot_summary(summary):
    method_order = ["blind_repair", "family_repair", "edge_verifier", "acs", "oracle_signature"]
    labels = {
        "blind_repair": "Blind repair",
        "family_repair": "Family repair",
        "edge_verifier": "Edge verifier",
        "acs": "ACS",
        "oracle_signature": "Oracle signature",
    }
    colors = {
        "blind_repair": "#7f1d1d",
        "family_repair": "#b45309",
        "edge_verifier": "#1d4ed8",
        "acs": "#047857",
        "oracle_signature": "#374151",
    }
    by_method = defaultdict(list)
    for row in summary:
        by_method[row["method"]].append(row)

    fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.6))
    for method in method_order:
        vals = sorted(by_method[method], key=lambda r: float(r["active_probability"]))
        xs = [float(v["active_probability"]) for v in vals]
        axes[0].plot(xs, [float(v["median_total_cost"]) for v in vals], marker="o", label=labels[method], color=colors[method])
        axes[1].plot(xs, [float(v["mean_invalid_executions"]) for v in vals], marker="o", label=labels[method], color=colors[method])
        axes[2].plot(xs, [float(v["mean_edge_checks"]) for v in vals], marker="o", label=labels[method], color=colors[method])

    axes[0].set_title("Total cost")
    axes[0].set_ylabel("median cost units")
    axes[1].set_title("Invalid executions")
    axes[1].set_ylabel("mean count")
    axes[2].set_title("Verifier calls")
    axes[2].set_ylabel("mean edge checks")
    for ax in axes:
        ax.set_xlabel("active constraint probability")
        ax.grid(True, alpha=0.25)
    axes[0].legend(loc="upper left", fontsize=8)
    fig.tight_layout()
    fig.savefig(FIGURES / "main_results.pdf")
    fig.savefig(FIGURES / "main_results.png", dpi=180)
    plt.close(fig)


def write_report(summary, config):
    by = {(float(r["active_probability"]), r["method"]): r for r in summary}
    lines = []
    lines.append("# Experiment Report")
    lines.append("")
    lines.append("## Simulator")
    lines.append("")
    lines.append(
        "The simulator is a layered robot task-planning abstraction. Edges are macro-actions such as direct navigation, grasp, carry, inspect, or tool-use choices. Hidden physical properties activate constraint families that invalidate every edge carrying that family tag."
    )
    lines.append("")
    lines.append("Constraint families:")
    lines.append("")
    for family in FAMILIES:
        lines.append(f"- `{family}`: {FAMILY_DESCRIPTIONS[family]}")
    lines.append("")
    lines.append("## Methods")
    lines.append("")
    lines.append("- `blind_repair`: plans ignoring constraints, executes, blacklists only the failed edge, and replans.")
    lines.append("- `family_repair`: after a failed edge, generalizes to the violated constraint family and replans.")
    lines.append("- `edge_verifier`: calls a perfect feasibility verifier on every candidate edge considered by Dijkstra search.")
    lines.append("- `acs`: pays one diagnostic probe per constraint family, discovers the active signature, masks active families, and then plans.")
    lines.append("- `oracle_signature`: plans with the true active family set and no diagnostic cost.")
    lines.append("")
    lines.append("## Cost Model")
    lines.append("")
    for k, v in config["cost_model"].items():
        lines.append(f"- {k}: {v}")
    lines.append("")
    lines.append("## Main Result")
    lines.append("")
    lines.append("| active probability | method | median total cost | mean invalid executions | mean verifier calls | success rate |")
    lines.append("|---:|---|---:|---:|---:|---:|")
    for r in sorted(summary, key=lambda x: (float(x["active_probability"]), x["method"])):
        lines.append(
            f"| {float(r['active_probability']):.2f} | {r['method']} | {float(r['median_total_cost']):.2f} | {float(r['mean_invalid_executions']):.2f} | {float(r['mean_edge_checks']):.1f} | {float(r['success_rate']):.2f} |"
        )
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    p = 0.35
    if (p, "acs") in by:
        acs = float(by[(p, "acs")]["median_total_cost"])
        blind = float(by[(p, "blind_repair")]["median_total_cost"])
        verifier = float(by[(p, "edge_verifier")]["median_total_cost"])
        family = float(by[(p, "family_repair")]["median_total_cost"])
        lines.append(
            f"At active probability {p:.2f}, ACS has median cost {acs:.2f}, compared with blind repair {blind:.2f}, family repair {family:.2f}, and edge verification {verifier:.2f}."
        )
    lines.append(
        "The result is intended as runnable evidence for the mechanism, not as a physical-robot validation. It demonstrates the regime where discovering an active constraint family before planning is different from paying for failures or verifier calls inside search."
    )
    (DOCS / "experiment_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def append_signature_noise_report(noise_summary):
    path = DOCS / "experiment_report.md"
    text = path.read_text(encoding="utf-8")
    lines = [
        "",
        "## Signature Noise Stress",
        "",
        "At active probability 0.35, the diagnostic signature is corrupted before planning. False negatives miss active families; false positives mark inactive families as active. The table below summarizes all 900 trials per scenario.",
        "",
        "| Scenario | False negative | False positive | Valid-plan rate | Median total cost | Mean invalid executions |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in noise_summary:
        lines.append(
            f"| {row['scenario']} | {float(row['false_negative_rate']):.2f} | {float(row['false_positive_rate']):.2f} | {float(row['success_rate']):.3f} | {float(row['median_total_cost']):.2f} | {float(row['mean_invalid_executions']):.2f} |"
        )
    lines.extend(
        [
            "",
            "Interpretation: ACS is highly sensitive to false negatives because a missed active family can leave an invalid low-cost branch in the planner. False positives are safer in this simulator because the conservative untagged chain remains, but they can raise cost or remove valid options in less forgiving graphs.",
        ]
    )
    path.write_text(text.rstrip() + "\n" + "\n".join(lines) + "\n", encoding="utf-8")


def main():
    ensure_dirs()
    active_probabilities = [0.0, 0.10, 0.20, 0.35, 0.50, 0.65]
    trials_per_setting = 180
    rows = []
    progress_path = RESULTS / "experiment_progress.json"
    for p in active_probabilities:
        for trial in range(trials_per_setting):
            seed = 100000 + int(p * 1000) * 1000 + trial
            problem = generate_problem(seed=seed, active_probability=p)
            for result in run_all_methods(problem):
                rows.append(
                    {
                        "active_probability": f"{p:.2f}",
                        "trial": trial,
                        "seed": seed,
                        "active_family_count": len(problem.active),
                        "active_families": "|".join(sorted(problem.active)),
                        "method": result.method,
                        "success": str(result.success).lower(),
                        "total_cost": f"{result.total_cost:.6f}",
                        "path_cost": f"{result.path_cost:.6f}",
                        "expansions": result.expansions,
                        "edge_checks": result.edge_checks,
                        "probes": result.probes,
                        "invalid_executions": result.invalid_executions,
                        "attempts": result.attempts,
                        "discovered": "|".join(result.discovered),
                    }
                )
            if trial % 30 == 0:
                progress_path.write_text(
                    json.dumps({"active_probability": p, "trial": trial, "rows": len(rows)}, indent=2),
                    encoding="utf-8",
                )

    raw_fields = [
        "active_probability",
        "trial",
        "seed",
        "active_family_count",
        "active_families",
        "method",
        "success",
        "total_cost",
        "path_cost",
        "expansions",
        "edge_checks",
        "probes",
        "invalid_executions",
        "attempts",
        "discovered",
    ]
    write_csv(RESULTS / "raw_trials.csv", rows, raw_fields)
    summary = summarize(rows)
    summary_fields = [
        "active_probability",
        "method",
        "trials",
        "mean_total_cost",
        "median_total_cost",
        "p25_total_cost",
        "p75_total_cost",
        "mean_invalid_executions",
        "mean_edge_checks",
        "mean_expansions",
        "success_rate",
    ]
    write_csv(RESULTS / "summary.csv", summary, summary_fields)
    noise_rows = run_signature_noise_stress()
    noise_fields = [
        "scenario",
        "active_probability",
        "repeat",
        "trial",
        "false_negative_rate",
        "false_positive_rate",
        "active_family_count",
        "success",
        "total_cost",
        "path_cost",
        "expansions",
        "invalid_executions",
        "missed_active_families",
        "false_positive_families",
    ]
    write_csv(RESULTS / "signature_noise_stress.csv", noise_rows, noise_fields)
    noise_summary = summarize_signature_noise(noise_rows)
    noise_summary_fields = [
        "scenario",
        "false_negative_rate",
        "false_positive_rate",
        "trials",
        "success_rate",
        "median_total_cost",
        "mean_invalid_executions",
        "mean_missed_active_families",
        "mean_false_positive_families",
    ]
    write_csv(RESULTS / "signature_noise_summary.csv", noise_summary, noise_summary_fields)
    write_signature_noise_table(noise_summary)
    config = {
        "active_probabilities": active_probabilities,
        "trials_per_setting": trials_per_setting,
        "families": list(FAMILIES),
        "cost_model": {
            "expansion_cost": 0.03,
            "verifier_cost": 0.18,
            "probe_cost": 0.55,
            "invalid_execution_cost": 18.0,
            "failure_cost": 250.0,
        },
    }
    (RESULTS / "config.json").write_text(json.dumps(config, indent=2), encoding="utf-8")
    plot_summary(summary)
    write_report(summary, config)
    append_signature_noise_report(noise_summary)
    progress_path.write_text(json.dumps({"stage": "complete", "rows": len(rows)}, indent=2), encoding="utf-8")
    print(f"Wrote {RESULTS / 'raw_trials.csv'}")
    print(f"Wrote {RESULTS / 'summary.csv'}")
    print(f"Wrote {FIGURES / 'main_results.pdf'}")
    print(f"Wrote {DOCS / 'experiment_report.md'}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        ensure_dirs()
        (RESULTS / "experiment_progress.json").write_text(json.dumps({"stage": "failed", "error": repr(exc)}, indent=2), encoding="utf-8")
        print(f"run_experiments failed: {exc}", file=sys.stderr)
        sys.exit(1)
