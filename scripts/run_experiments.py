import csv
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from acs_planning import FAMILIES, FAMILY_DESCRIPTIONS, generate_problem, run_all_methods


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
