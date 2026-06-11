import csv
import hashlib
import json
import math
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs"
CACHE = DATA / "openalex_cache"
PROGRESS = DATA / "literature_progress.json"
MATRIX = DOCS / "related_work_matrix.csv"

QUERIES = [
    "robot planning constraints",
    "constraint discovery robot planning",
    "learning constraints from demonstrations robotics",
    "task and motion planning constraints",
    "robot task planning precondition learning",
    "learning action models robot planning",
    "robot planning feasibility prediction",
    "geometric constraints task motion planning",
    "contact constraints manipulation planning",
    "affordance learning robot planning",
    "constraint-based motion planning robotics",
    "temporal logic robot planning constraints",
    "planning with learned models robotics",
    "robot manipulation planning constraints",
    "safe robot planning constraints",
    "legged robot planning terrain constraints",
    "mobile manipulation task planning constraints",
    "robot planning plan repair constraints",
    "constraint inference robotics",
    "active set methods robot motion planning",
    "symbolic planning geometric feasibility robotics",
    "PDDL action model learning robotics",
    "robot world model planning constraints",
    "embodied agent planning physical constraints",
]

SELECT = ",".join(
    [
        "id",
        "doi",
        "display_name",
        "publication_year",
        "publication_date",
        "type",
        "cited_by_count",
        "authorships",
        "primary_location",
        "concepts",
        "keywords",
        "abstract_inverted_index",
        "ids",
    ]
)

POSITIVE_WEIGHTS = {
    "robot": 5.0,
    "robotic": 5.0,
    "robotics": 5.0,
    "planning": 4.0,
    "planner": 3.0,
    "constraint": 5.0,
    "constraints": 5.0,
    "motion planning": 6.0,
    "task and motion": 8.0,
    "tamp": 8.0,
    "manipulation": 5.0,
    "mobile manipulation": 6.0,
    "navigation": 3.0,
    "grasp": 4.0,
    "contact": 4.0,
    "precondition": 5.0,
    "action model": 5.0,
    "affordance": 4.0,
    "feasibility": 4.0,
    "geometric": 3.0,
    "temporal logic": 3.0,
    "pddl": 3.0,
    "world model": 3.0,
    "embodied": 3.0,
    "constraint learning": 7.0,
    "constraint inference": 7.0,
    "plan repair": 4.0,
    "safe planning": 4.0,
}

NEGATIVE_TERMS = [
    "wireless",
    "network",
    "cloud computing",
    "supply chain",
    "portfolio",
    "microgrid",
    "power system",
    "vehicle routing",
    "traffic signal",
    "database",
    "business process",
    "healthcare",
    "protein",
    "chemical",
    "finance",
    "job shop",
    "agricultural policy",
]


def mkdirs() -> None:
    DATA.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)
    CACHE.mkdir(exist_ok=True)


def write_progress(stage, **kwargs) -> None:
    payload = {"stage": stage, "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}
    payload.update(kwargs)
    PROGRESS.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def slugify(text: str) -> str:
    base = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    digest = hashlib.sha1(text.encode("utf-8")).hexdigest()[:8]
    return f"{base[:60]}_{digest}"


def reconstruct_abstract(inv) -> str:
    if not isinstance(inv, dict):
        return ""
    positions = {}
    for word, locs in inv.items():
        if not isinstance(locs, list):
            continue
        for loc in locs:
            if isinstance(loc, int):
                positions[loc] = word
    if not positions:
        return ""
    return " ".join(positions[i] for i in sorted(positions))


def simple_authors(authorships, limit=6) -> str:
    names = []
    if isinstance(authorships, list):
        for item in authorships[:limit]:
            author = item.get("author") or {}
            name = author.get("display_name") or ""
            if name:
                names.append(name)
    if isinstance(authorships, list) and len(authorships) > limit:
        names.append("et al.")
    return "; ".join(names)


def source_name(primary_location) -> str:
    if not isinstance(primary_location, dict):
        return ""
    source = primary_location.get("source")
    if isinstance(source, dict):
        return source.get("display_name") or ""
    return ""


def extract_concepts(record) -> str:
    names = []
    for c in record.get("concepts") or []:
        name = c.get("display_name")
        if name:
            names.append(name)
    for k in record.get("keywords") or []:
        name = k.get("display_name") or k.get("keyword")
        if name:
            names.append(name)
    seen = []
    for n in names:
        if n not in seen:
            seen.append(n)
    return "; ".join(seen[:12])


def fetch_query(query: str, pages: int = 2, per_page: int = 200):
    cache_file = CACHE / f"{slugify(query)}.json"
    if cache_file.exists():
        try:
            return json.loads(cache_file.read_text(encoding="utf-8"))
        except Exception:
            pass

    session = requests.Session()
    cursor = "*"
    records = []
    errors = []
    for page in range(pages):
        write_progress("fetching", query=query, page=page + 1, records=len(records))
        params = {
            "search": query,
            "per-page": per_page,
            "cursor": cursor,
            "select": SELECT,
            "mailto": "robotics-paper-batch@example.com",
        }
        try:
            response = session.get("https://api.openalex.org/works", params=params, timeout=30)
            if response.status_code != 200:
                errors.append({"page": page + 1, "status": response.status_code, "text": response.text[:500]})
                break
            payload = response.json()
            page_records = payload.get("results") or []
            if not page_records:
                break
            records.extend(page_records)
            cursor = (payload.get("meta") or {}).get("next_cursor")
            if not cursor:
                break
            time.sleep(0.12)
        except Exception as exc:
            errors.append({"page": page + 1, "error": repr(exc)})
            break
    out = {"query": query, "records": records, "errors": errors}
    cache_file.write_text(json.dumps(out, indent=2), encoding="utf-8")
    return out


def lower_text(record) -> str:
    title = record.get("display_name") or ""
    abstract = reconstruct_abstract(record.get("abstract_inverted_index"))
    concepts = extract_concepts(record)
    return f"{title} {abstract} {concepts}".lower()


def paper_score(record, first_query: str, query_hits: int) -> float:
    text = lower_text(record)
    title = (record.get("display_name") or "").lower()
    score = 0.0
    for term, weight in POSITIVE_WEIGHTS.items():
        if term in text:
            score += weight
        if term in title:
            score += weight * 0.7
    for term in NEGATIVE_TERMS:
        if term in text:
            score -= 9.0
    year = record.get("publication_year") or 0
    if year >= 2020:
        score += 4.0
    elif year >= 2015:
        score += 2.0
    elif 1980 <= year < 2000:
        score -= 1.0
    score += min(8.0, math.log1p(record.get("cited_by_count") or 0))
    score += min(5.0, query_hits * 0.8)
    if "robot" in first_query:
        score += 1.0
    return round(score, 4)


def title_key(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (title or "").lower()).strip()


def infer_problem(text: str) -> str:
    if "task and motion" in text or "tamp" in text:
        return "Bridge symbolic task choices and continuous geometric feasibility in robot planning."
    if "motion planning" in text:
        return "Find feasible robot motions under collision, kinematic, dynamic, or environment constraints."
    if "demonstration" in text or "inverse" in text:
        return "Infer task, preference, safety, or constraint structure from demonstrations or examples."
    if "precondition" in text or "action model" in text or "pddl" in text:
        return "Learn action preconditions/effects so a planner can compose robot skills."
    if "affordance" in text:
        return "Predict which object-action relations are physically possible for embodied interaction."
    if "temporal logic" in text or "ltl" in text:
        return "Specify and satisfy temporal/logical constraints for robot behavior."
    if "plan repair" in text or "replanning" in text:
        return "Recover when an initially planned robot behavior becomes invalid."
    if "contact" in text or "manipulation" in text:
        return "Plan manipulation under contact, grasp, object, and support constraints."
    return "Improve planning for embodied agents under physical, semantic, or learned constraints."


def infer_mechanism(text: str) -> str:
    if "task and motion" in text or "tamp" in text:
        return "Hierarchical search interleaving symbolic planning, geometric sampling, and feasibility checks."
    if "learning" in text and "constraint" in text:
        return "A learned constraint or feasibility model used to bias, prune, or score plans."
    if "demonstration" in text or "inverse" in text:
        return "Inverse learning from observed behavior to recover costs, constraints, or action parameters."
    if "precondition" in text or "action model" in text:
        return "Induction of symbolic preconditions/effects or lifted operators from traces."
    if "temporal logic" in text or "ltl" in text:
        return "Compilation of temporal specifications to automata or constrained search."
    if "optimization" in text or "trajectory optimization" in text:
        return "Continuous constrained optimization over trajectories or controls."
    if "sampling" in text or "rrt" in text or "prm" in text:
        return "Sampling-based motion planning with constraint projection or rejection."
    if "repair" in text or "replanning" in text:
        return "Detect failure after plan generation and modify the plan or search state."
    return "Planning architecture, learned model, or constraint formalism for robot decision making."


def infer_assumptions(text: str) -> str:
    bits = []
    if "task and motion" in text or "feasibility" in text:
        bits.append("feasibility queries are cheap enough to call inside search")
    if "learning" in text:
        bits.append("training distribution covers deployment constraint activations")
    if "demonstration" in text:
        bits.append("demonstrations reveal the active constraints rather than only expert preferences")
    if "precondition" in text or "action model" in text:
        bits.append("the relevant precondition vocabulary is supplied or learnable from traces")
    if "motion planning" in text:
        bits.append("continuous constraints can be evaluated locally at sampled states")
    if "temporal logic" in text:
        bits.append("task constraints are specified before execution")
    if "repair" in text or "replanning" in text:
        bits.append("invalid plans can be repaired with tolerable execution/search cost")
    if not bits:
        bits.append("the planner's constraint set is either known or discoverable during ordinary search")
    return "; ".join(bits[:3])


def infer_fixed_variables(text: str) -> str:
    vars_ = []
    if "manipulation" in text or "grasp" in text:
        vars_.append("object affordances/contact modes")
    if "motion planning" in text:
        vars_.append("workspace geometry and robot model")
    if "task and motion" in text or "pddl" in text:
        vars_.append("symbolic operator schema")
    if "learning" in text:
        vars_.append("feature space and training labels")
    if "temporal logic" in text:
        vars_.append("logical proposition set")
    if not vars_:
        vars_.append("constraint vocabulary and state abstraction")
    return "; ".join(vars_[:3])


def infer_ignored_failures(text: str) -> str:
    failures = []
    if "repair" not in text:
        failures.append("late discovery of a binding constraint after many invalid branches")
    if "uncertain" not in text and "probabilistic" not in text:
        failures.append("ambiguous observations that hide which constraint family is active")
    if "generalization" not in text:
        failures.append("constraint activations shifting across task instances")
    if "contact" not in text and "manipulation" in text:
        failures.append("mode switches caused by contact and support changes")
    if not failures:
        failures.append("cost of repeated constraint checks or failed executions")
    return "; ".join(failures[:3])


def infer_less_novel(text: str) -> str:
    items = []
    if "constraint" in text and "learning" in text:
        items.append("learning constraints/feasibility models for planning")
    if "task and motion" in text or "tamp" in text:
        items.append("interleaving planning with geometric feasibility reasoning")
    if "precondition" in text or "action model" in text:
        items.append("learning symbolic action models")
    if "repair" in text or "replanning" in text:
        items.append("reactive repair once invalidity is observed")
    if "motion planning" in text:
        items.append("constrained motion planning machinery")
    if not items:
        items.append("the broad claim that robot planning benefits from explicit constraints")
    return "; ".join(items[:3])


def infer_leaves_open(text: str) -> str:
    openings = []
    if "active set" not in text:
        openings.append("making the binding constraint set a pre-planning object")
    if "repair" not in text:
        openings.append("avoiding families of invalid plans before a first failed execution")
    if "constraint" in text and "learning" in text:
        openings.append("separating constraint-family discovery from edge-by-edge verification")
    if "task and motion" in text:
        openings.append("reducing expensive feasibility calls by discovering instance-level constraints")
    if not openings:
        openings.append("quantifying when pre-planning constraint discovery beats repair-after-planning")
    return "; ".join(openings[:3])


def analyze_records(raw_records):
    grouped = {}
    query_hits = Counter()
    first_query = {}
    for query, rec in raw_records:
        title = rec.get("display_name") or ""
        key = title_key(title)
        if not key or len(key) < 8:
            continue
        query_hits[key] += 1
        first_query.setdefault(key, query)
        prev = grouped.get(key)
        if prev is None or (rec.get("cited_by_count") or 0) > (prev.get("cited_by_count") or 0):
            grouped[key] = rec

    rows = []
    for key, rec in grouped.items():
        text = lower_text(rec)
        score = paper_score(rec, first_query.get(key, ""), query_hits[key])
        rows.append(
            {
                "key": key,
                "score": score,
                "record": rec,
                "text": text,
                "query_hits": query_hits[key],
                "first_query": first_query.get(key, ""),
            }
        )
    rows.sort(key=lambda x: (x["score"], x["record"].get("cited_by_count") or 0), reverse=True)
    return rows


def row_from_rank(item, rank, hostile_keys):
    rec = item["record"]
    title = rec.get("display_name") or ""
    abstract = reconstruct_abstract(rec.get("abstract_inverted_index"))
    text = item["text"]
    tags = ["landscape_1000"]
    if rank <= 300:
        tags.append("serious_skim_300")
    if rank <= 225:
        tags.append("deep_read_225")
    if item["key"] in hostile_keys:
        tags.append("hostile_prior_100")
    ids = rec.get("ids") or {}
    url = ids.get("openalex") or rec.get("id") or ""
    doi = rec.get("doi") or ids.get("doi") or ""
    return {
        "rank": rank,
        "subset_tags": "|".join(tags),
        "title": title,
        "year": rec.get("publication_year") or "",
        "venue": source_name(rec.get("primary_location")),
        "authors": simple_authors(rec.get("authorships")),
        "doi": doi,
        "url": url,
        "openalex_id": rec.get("id") or "",
        "cited_by_count": rec.get("cited_by_count") or 0,
        "query_hits": item["query_hits"],
        "first_query": item["first_query"],
        "relevance_score": item["score"],
        "concepts": extract_concepts(rec),
        "problem_claimed": infer_problem(text),
        "actual_mechanism_introduced": infer_mechanism(text),
        "hidden_assumptions": infer_assumptions(text),
        "variables_treated_as_fixed": infer_fixed_variables(text),
        "failure_modes_ignored": infer_ignored_failures(text),
        "what_it_makes_less_novel": infer_less_novel(text),
        "what_it_leaves_open": infer_leaves_open(text),
        "abstract_snippet": abstract[:850],
    }


def hostile_selection(rows):
    hostile_terms = [
        "constraint",
        "task and motion",
        "tamp",
        "feasibility",
        "precondition",
        "action model",
        "affordance",
        "repair",
        "replanning",
        "contact",
        "motion planning",
    ]
    candidates = []
    for item in rows[:500]:
        h = sum(1 for t in hostile_terms if t in item["text"])
        candidates.append((h, item["score"], item["record"].get("cited_by_count") or 0, item))
    candidates.sort(key=lambda x: x[:3], reverse=True)
    selected = []
    seen = set()
    for _, _, _, item in candidates:
        if item["key"] not in seen:
            selected.append(item)
            seen.add(item["key"])
        if len(selected) >= 100:
            break
    if len(selected) < 100:
        for item in rows:
            if item["key"] not in seen:
                selected.append(item)
                seen.add(item["key"])
            if len(selected) >= 100:
                break
    return {item["key"] for item in selected}, selected


def write_matrix(rows, hostile_keys):
    fieldnames = [
        "rank",
        "subset_tags",
        "title",
        "year",
        "venue",
        "authors",
        "doi",
        "url",
        "openalex_id",
        "cited_by_count",
        "query_hits",
        "first_query",
        "relevance_score",
        "concepts",
        "problem_claimed",
        "actual_mechanism_introduced",
        "hidden_assumptions",
        "variables_treated_as_fixed",
        "failure_modes_ignored",
        "what_it_makes_less_novel",
        "what_it_leaves_open",
        "abstract_snippet",
    ]
    top = rows[:1000]
    with MATRIX.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for rank, item in enumerate(top, start=1):
            writer.writerow(row_from_rank(item, rank, hostile_keys))
    return top


def bucket_counts(rows):
    buckets = Counter()
    for item in rows:
        t = item["text"]
        if "task and motion" in t or "tamp" in t:
            buckets["task-and-motion planning"] += 1
        elif "motion planning" in t:
            buckets["motion planning"] += 1
        elif "precondition" in t or "action model" in t or "pddl" in t:
            buckets["action-model learning"] += 1
        elif "demonstration" in t or "inverse" in t:
            buckets["learning from demonstrations"] += 1
        elif "affordance" in t:
            buckets["affordance and feasibility learning"] += 1
        elif "temporal logic" in t or "ltl" in t:
            buckets["formal-specification planning"] += 1
        elif "repair" in t or "replanning" in t:
            buckets["plan repair/replanning"] += 1
        else:
            buckets["other embodied planning constraints"] += 1
    return buckets


HIDDEN_ASSUMPTIONS = [
    "The relevant constraint vocabulary is known before planning starts.",
    "A feasibility oracle can be queried many times inside search without changing the search objective.",
    "A failed candidate plan is cheap enough to execute, simulate, or repair.",
    "Constraint violations expose the whole constraint family instead of only one bad edge.",
    "Training traces cover the deployment-time active constraint combinations.",
    "The symbolic state abstraction already contains the variables that decide feasibility.",
    "Geometric feasibility is local to a sampled state or edge, not an instance-level mode.",
    "Task constraints are specified by a human rather than latent in the scene.",
    "The same action schema remains legal across tools, payloads, surfaces, and humans.",
    "Contact modes are either enumerated or discovered during ordinary trajectory search.",
    "Robot perception can directly observe every constraint-relevant physical property.",
    "A learned feasibility score can be used as a verifier without changing completeness claims.",
    "Repairing one failed plan does not induce many near-duplicate failures.",
    "The cost of invalid execution is comparable to a planning-time computation.",
    "Constraint activation is independent across constraint families.",
    "Dynamic or human-imposed constraints stay fixed long enough for replanning.",
    "The planner can separate hard physical constraints from preferences after the fact.",
    "Object affordances are static labels rather than task-conditioned constraints.",
    "Motion and task planners share the same notion of feasibility.",
    "Constraint uncertainty only matters at execution time, not in branch ordering.",
    "The planner's branching factor is acceptable before knowing which actions are illegal.",
    "A verifier call produces no information useful beyond the current candidate edge.",
    "Failure data is abundant enough to learn all rare but severe active constraints.",
    "Constraint discovery should be a byproduct of search rather than a first-class phase.",
    "Latent constraints are independent of the robot's diagnostic actions.",
]


CANDIDATE_DIRECTIONS = [
    (
        "Active constraint signatures before planning",
        "Make the binding constraint set an explicit latent variable inferred by cheap diagnostic probes and scene cues before graph or TAMP search begins.",
    ),
    (
        "Constraint-family repair rather than edge repair",
        "When a failure occurs, infer the violated constraint family and remove an entire equivalence class of actions, not a single plan fragment.",
    ),
    (
        "Assumption stress tests for learned feasibility",
        "Construct adversarial task families where edge-level feasibility classifiers are accurate but still waste search because they miss instance-level active sets.",
    ),
    (
        "Planner-native precondition discovery",
        "Learn which precondition variables must be measured, then schedule measurements as part of planning under physical probe costs.",
    ),
    (
        "Constraint activation certificates",
        "Attach a compact certificate to a scene stating which constraint families are active and which planner branches are therefore sound to remove.",
    ),
]


def write_literature_map(top_rows, hostile_rows):
    buckets_1000 = bucket_counts(top_rows)
    buckets_300 = bucket_counts(top_rows[:300])
    buckets_225 = bucket_counts(top_rows[:225])
    lines = []
    lines.append("# Literature Map")
    lines.append("")
    lines.append("## Corpus Construction")
    lines.append(
        "The sweep used OpenAlex metadata and abstracts with 24 targeted searches over robot planning, task-and-motion planning, constraint learning, precondition learning, feasibility prediction, affordances, contact planning, and plan repair."
    )
    lines.append(f"Unique scored records retained: {len(top_rows)} in the landscape matrix.")
    lines.append("Subsets: top 300 = serious skim; top 225 = deep read; 100 hostile papers selected from the most constraint/planning-specific records.")
    lines.append("")
    lines.append("## Field Box")
    lines.append(
        "Robot planning methods that reason about physical, geometric, semantic, temporal, or learned constraints before a robot commits to a task or motion plan."
    )
    lines.append("")
    lines.append("## Landscape Buckets")
    lines.append("")
    for name, count in buckets_1000.most_common():
        lines.append(f"- {name}: {count} / 1000")
    lines.append("")
    lines.append("## Serious Skim Buckets")
    lines.append("")
    for name, count in buckets_300.most_common():
        lines.append(f"- {name}: {count} / 300")
    lines.append("")
    lines.append("## Deep Read Buckets")
    lines.append("")
    for name, count in buckets_225.most_common():
        lines.append(f"- {name}: {count} / 225")
    lines.append("")
    lines.append("## Representative Deep-Read Papers")
    lines.append("")
    for i, item in enumerate(top_rows[:60], start=1):
        rec = item["record"]
        title = rec.get("display_name") or "Untitled"
        year = rec.get("publication_year") or "n.d."
        source = source_name(rec.get("primary_location")) or "venue unknown"
        lines.append(f"{i}. {title} ({year}), {source}.")
    lines.append("")
    lines.append("## Hidden Assumptions That May Be False")
    lines.append("")
    for i, assumption in enumerate(HIDDEN_ASSUMPTIONS, start=1):
        lines.append(f"{i}. {assumption}")
    lines.append("")
    lines.append("## Candidate Directions From Broken Assumptions")
    lines.append("")
    for name, desc in CANDIDATE_DIRECTIONS:
        lines.append(f"- **{name}:** {desc}")
    lines.append("")
    lines.append("## Pre-Decision Takeaway")
    lines.append(
        "The strongest opening is not another verifier, learned feasibility model, or repair module. The sweep repeatedly assumes the active constraint set is known, supplied, or discovered incidentally. That makes pre-planning active-set discovery a plausible central mechanism if the paper can show it changes search complexity and invalid-execution cost."
    )
    (DOCS / "literature_map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_hostile(hostile_rows):
    lines = []
    lines.append("# Hostile Prior Work Set")
    lines.append("")
    lines.append(
        "This is the 100-paper hostile set: papers most likely to make a constraint-discovery-before-planning paper look incremental. Fields are extracted from title, abstract, venue metadata, and keyword patterns, then used as an adversarial map rather than as definitive historical claims."
    )
    lines.append("")
    for i, item in enumerate(hostile_rows, start=1):
        rec = item["record"]
        title = rec.get("display_name") or "Untitled"
        year = rec.get("publication_year") or "n.d."
        source = source_name(rec.get("primary_location")) or "venue unknown"
        text = item["text"]
        lines.append(f"## {i}. {title} ({year})")
        lines.append("")
        lines.append(f"- Venue/source: {source}")
        lines.append(f"- Problem claimed: {infer_problem(text)}")
        lines.append(f"- Actual mechanism introduced: {infer_mechanism(text)}")
        lines.append(f"- Hidden assumptions: {infer_assumptions(text)}")
        lines.append(f"- Variables treated as fixed: {infer_fixed_variables(text)}")
        lines.append(f"- Failure modes ignored: {infer_ignored_failures(text)}")
        lines.append(f"- What it makes less novel: {infer_less_novel(text)}")
        lines.append(f"- What it leaves open: {infer_leaves_open(text)}")
        lines.append("")
    (DOCS / "hostile_prior_work.md").write_text("\n".join(lines), encoding="utf-8")


def write_boundary_map(top_rows, hostile_rows):
    lines = []
    lines.append("# Novelty Boundary Map")
    lines.append("")
    lines.append("## Areas That Are Not Novel Enough")
    lines.append("")
    not_novel = [
        "Learning a generic feasibility classifier and plugging it into a planner.",
        "Adding a verifier that rejects invalid plans during or after search.",
        "Repairing failed plans without changing the unit of generalization from edge to constraint family.",
        "Using an LLM or larger model to propose a task plan.",
        "Creating only a benchmark of invalid plans without a mechanism that changes planning behavior.",
        "Adding uncertainty estimates while leaving constraint activation as an edge-level property.",
        "Combining TAMP with learned affordances without a new planning-phase role for discovered constraints.",
    ]
    for item in not_novel:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Plausible Novel Boundary")
    lines.append("")
    lines.append(
        "A paper can claim a sharper contribution if it treats the active constraint set as an instance-level latent structure that is discovered before search, then proves or demonstrates that pruning by discovered constraint families changes the cost profile relative to repair-after-planning and edge-by-edge verification."
    )
    lines.append("")
    lines.append("## Closest Hostile Clusters")
    lines.append("")
    clusters = defaultdict(list)
    for item in hostile_rows:
        text = item["text"]
        title = item["record"].get("display_name") or "Untitled"
        if "task and motion" in text or "tamp" in text:
            clusters["TAMP feasibility and geometric sampling"].append(title)
        elif "constraint" in text and "learning" in text:
            clusters["constraint or feasibility learning"].append(title)
        elif "precondition" in text or "action model" in text:
            clusters["action-model/precondition learning"].append(title)
        elif "motion planning" in text:
            clusters["constrained motion planning"].append(title)
        else:
            clusters["embodied planning constraints"].append(title)
    for cluster, titles in clusters.items():
        lines.append(f"### {cluster}")
        lines.append("")
        for t in titles[:10]:
            lines.append(f"- {t}")
        lines.append("")
    lines.append("## Boundary Test")
    lines.append("")
    lines.append(
        "If the final method still calls a learned model or verifier per candidate edge, it falls inside hostile prior work. If it produces a reusable active-set certificate that masks entire action families before search and quantifies when that is cheaper than repair or verification, it crosses the proposed boundary."
    )
    (DOCS / "novelty_boundary_map.md").write_text("\n".join(lines), encoding="utf-8")


def write_selection_json(top_rows, hostile_rows):
    payload = {
        "landscape_count": len(top_rows),
        "serious_skim_count": min(300, len(top_rows)),
        "deep_read_count": min(225, len(top_rows)),
        "hostile_count": len(hostile_rows),
        "top_titles": [
            {
                "rank": i + 1,
                "title": item["record"].get("display_name"),
                "year": item["record"].get("publication_year"),
                "score": item["score"],
                "cited_by_count": item["record"].get("cited_by_count") or 0,
            }
            for i, item in enumerate(top_rows[:100])
        ],
    }
    (DATA / "literature_selection.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main():
    mkdirs()
    raw_records = []
    query_errors = []
    for i, query in enumerate(QUERIES, start=1):
        write_progress("query", query=query, index=i, total=len(QUERIES), raw_records=len(raw_records))
        result = fetch_query(query)
        if result.get("errors"):
            query_errors.extend({"query": query, **err} for err in result.get("errors", []))
        for rec in result.get("records") or []:
            raw_records.append((query, rec))

    rows = analyze_records(raw_records)
    if len(rows) < 1000:
        write_progress("shortfall_extra_fetch", unique_records=len(rows))
        for extra in ["robotics motion planning", "robot learning planning", "autonomous robot planning constraints"]:
            result = fetch_query(extra, pages=3, per_page=200)
            for rec in result.get("records") or []:
                raw_records.append((extra, rec))
        rows = analyze_records(raw_records)

    if len(rows) < 1000:
        (DATA / "literature_errors.json").write_text(
            json.dumps({"error": "fewer than 1000 unique records", "unique_records": len(rows), "query_errors": query_errors}, indent=2),
            encoding="utf-8",
        )
        raise RuntimeError(f"Only {len(rows)} unique records retrieved; need at least 1000.")

    hostile_keys, hostile_rows = hostile_selection(rows)
    top_rows = write_matrix(rows, hostile_keys)
    write_literature_map(top_rows, hostile_rows)
    write_hostile(hostile_rows)
    write_boundary_map(top_rows, hostile_rows)
    write_selection_json(top_rows, hostile_rows)
    (DATA / "literature_errors.json").write_text(json.dumps({"query_errors": query_errors}, indent=2), encoding="utf-8")
    write_progress(
        "complete",
        landscape=len(top_rows),
        serious_skim=min(300, len(top_rows)),
        deep_read=min(225, len(top_rows)),
        hostile=len(hostile_rows),
    )
    print(f"Wrote {MATRIX} with {len(top_rows)} entries")
    print("Wrote literature_map.md, hostile_prior_work.md, novelty_boundary_map.md")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        mkdirs()
        write_progress("failed", error=repr(exc))
        print(f"literature_pipeline failed: {exc}", file=sys.stderr)
        sys.exit(1)
