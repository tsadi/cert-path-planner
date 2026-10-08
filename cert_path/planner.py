"""Turn a product type into a standards map, test sequence and timeline."""

from __future__ import annotations

from dataclasses import dataclass, field

from . import catalog as C


@dataclass
class Item:
    id: str
    title: str
    phase: str
    low: int
    high: int


@dataclass
class PhasePlan:
    id: str
    name: str
    stage: int
    items: list = field(default_factory=list)

    @property
    def low(self) -> int:
        return max((i.low for i in self.items), default=0)

    @property
    def high(self) -> int:
        return max((i.high for i in self.items), default=0)


@dataclass
class Plan:
    product: str
    label: str
    markets: set
    options: set
    phases: list
    start_low: dict
    start_high: dict
    total_low: int
    total_high: int


def build_plan(product: str, markets=("us",), options=()) -> Plan:
    if product not in C.PRODUCTS:
        raise KeyError(f"unknown product {product!r}; choose from {sorted(C.PRODUCTS)}")
    markets = {m.lower() for m in markets}
    bad = markets - {"us", "eu"}
    if bad:
        raise ValueError(f"unsupported markets {sorted(bad)}; use us and/or eu")
    options = set(options)
    bad = options - set(C.OPTION_FLAGS)
    if bad:
        raise ValueError(f"unknown options {sorted(bad)}; choose from {C.OPTION_FLAGS}")

    spec = C.PRODUCTS[product]
    ids = list(spec["base"])
    for opt in options:
        ids += spec["options"].get(opt, [])
    seen, chosen = set(), []
    for sid in ids:
        if sid in seen:
            continue
        seen.add(sid)
        title, phase, (lo, hi), mk = C.STANDARDS[sid]
        if mk & markets:
            chosen.append(Item(sid, title, phase, lo, hi))

    phases = []
    for ph in C.PHASES:
        items = [i for i in chosen if i.phase == ph["id"]]
        if items:
            phases.append(PhasePlan(ph["id"], ph["name"], ph["stage"], items))

    # stages run in sequence; phases inside a stage run in parallel
    start_low, start_high = {}, {}
    t_low = t_high = 0
    for stage in sorted({p.stage for p in phases}):
        group = [p for p in phases if p.stage == stage]
        for p in group:
            start_low[p.id], start_high[p.id] = t_low, t_high
        t_low += max(p.low for p in group)
        t_high += max(p.high for p in group)

    return Plan(product, spec["label"], markets, options, phases, start_low, start_high, t_low, t_high)


def critical_items(plan: Plan) -> list:
    """Items that set the duration of their stage (the long poles)."""
    out = []
    for stage in sorted({p.stage for p in plan.phases}):
        group = [p for p in plan.phases if p.stage == stage]
        longest = max(p.high for p in group)
        for p in group:
            out += [i for i in p.items if i.high == longest]
    return out


def gantt(plan: Plan, width: int = 60) -> str:
    scale = width / max(plan.total_high, 1)
    lines = []
    for p in plan.phases:
        s = int(plan.start_low[p.id] * scale)
        lo = max(1, int(p.low * scale))
        extra = max(0, int((plan.start_high[p.id] + p.high) * scale) - s - lo)
        bar = " " * s + "#" * lo + "-" * extra
        lines.append(f"{p.name[:34]:<34} |{bar:<{width}}|")
    lines.append(f"{'':<34}  0 wk{'':>{width - 10}}{plan.total_high} wk")
    lines.append("# = optimistic duration, - = added time in the pessimistic case")
    return "\n".join(lines)


def render_markdown(plan: Plan) -> str:
    m = "/".join(sorted(x.upper() for x in plan.markets))
    opts = ", ".join(sorted(plan.options)) or "none"
    out = [f"# Certification path: {plan.label}", "",
           f"Markets: {m} · Options: {opts}", "",
           f"Planned duration: **{plan.total_low}-{plan.total_high} weeks** "
           f"({plan.total_low / 4.33:.0f}-{plan.total_high / 4.33:.0f} months) from design freeze.", ""]
    out += ["## Standards map", "", "| Phase | Standard | Weeks |", "|---|---|---|"]
    for p in plan.phases:
        for i in p.items:
            out.append(f"| {p.name} | {i.title} | {i.low}-{i.high} |")
    out += ["", "## Test sequence", ""]
    stage_no = 0
    for stage in sorted({p.stage for p in plan.phases}):
        stage_no += 1
        group = [p for p in plan.phases if p.stage == stage]
        names = " + ".join(p.name for p in group)
        par = " (in parallel)" if len(group) > 1 else ""
        lo = plan.start_low[group[0].id]
        hi = plan.start_high[group[0].id]
        out.append(f"{stage_no}. **{names}**{par}: starts week {lo}-{hi}")
    out += ["", "## Long poles", ""]
    for i in critical_items(plan):
        out.append(f"- {i.title} ({i.low}-{i.high} wk)")
    out += ["", "## Timeline", "", "```", gantt(plan), "```", "",
            "_Lead times are planning assumptions for a first-of-kind product with lab slots booked. "
            "Edit `cert_path/catalog.py` for your NRTL, lab capacity and design maturity. "
            "Applicability of each standard depends on the final design and intended use._"]
    return "\n".join(out) + "\n"


def to_csv(plan: Plan) -> str:
    rows = ["phase,standard_id,title,weeks_low,weeks_high,start_week_low,start_week_high"]
    for p in plan.phases:
        for i in p.items:
            title = i.title.replace('"', "'")
            rows.append(f'{p.name},{i.id},"{title}",{i.low},{i.high},{plan.start_low[p.id]},{plan.start_high[p.id]}')
    return "\n".join(rows) + "\n"
