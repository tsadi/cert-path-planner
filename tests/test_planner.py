import pytest

from cert_path import build_plan, critical_items, render_markdown, to_csv
from cert_path import catalog
from cert_path.cli import main


def ids(plan):
    return {i.id for p in plan.phases for i in p.items}


def test_every_product_references_known_standards():
    for name, spec in catalog.PRODUCTS.items():
        for sid in spec["base"] + [s for v in spec["options"].values() for s in v]:
            assert sid in catalog.STANDARDS, (name, sid)


def test_every_standard_has_valid_phase_and_leadtime():
    phases = {p["id"] for p in catalog.PHASES}
    for sid, (title, phase, (lo, hi), mk) in catalog.STANDARDS.items():
        assert phase in phases, sid
        assert 0 < lo <= hi, sid
        assert mk <= {"us", "eu"} and mk, sid


def test_mv_sst_us_core():
    plan = build_plan("mv-sst", ["us"])
    s = ids(plan)
    assert {"UL2877", "UL1998", "IEC62443", "LISTING", "NEC"} <= s
    assert "IEC62477-1" not in s  # EU-only entry dropped for a US plan
    assert "UL1741SB" not in s    # only with grid export


def test_mv_sst_grid_export_adds_1741():
    s = ids(build_plan("mv-sst", ["us"], ["grid_export"]))
    assert {"UL1741SB", "IEEE1547", "UL2941"} <= s


def test_bess_us_eu():
    s = ids(build_plan("bess", ["us", "eu"]))
    assert {"UL9540", "UL9540A", "UL1973", "IEC62619", "EUBATT", "NFPA855", "CEFILE"} <= s


def test_robot_eu_includes_machinery_regulation():
    s = ids(build_plan("industrial-robot", ["eu"]))
    assert "MACHREG" in s and "ISO10218" in s and "UL1740" not in s


def test_timeline_is_sequential_by_stage():
    plan = build_plan("bess", ["us"])
    by_id = {p.id: p for p in plan.phases}
    assert plan.start_low["plan"] == 0
    assert plan.start_low["precomp"] == by_id["plan"].low
    # parallel phases in stage 4 share a start
    assert plan.start_low["safety"] == plan.start_low["emc"]
    assert plan.total_low <= plan.total_high


def test_long_poles_for_bess_include_9540a_or_9540():
    poles = {i.id for i in critical_items(build_plan("bess", ["us"]))}
    assert poles & {"UL9540A", "UL9540"}


def test_render_and_csv():
    plan = build_plan("mobile-robot", ["us", "eu"])
    md = render_markdown(plan)
    assert "Standards map" in md and "Timeline" in md
    csv = to_csv(plan)
    assert csv.splitlines()[0].startswith("phase,standard_id")


def test_bad_inputs():
    with pytest.raises(KeyError):
        build_plan("toaster")
    with pytest.raises(ValueError):
        build_plan("bess", ["jp"])
    with pytest.raises(ValueError):
        build_plan("bess", ["us"], ["teleport"])


def test_cli(capsys, tmp_path):
    assert main(["mv-sst", "--markets", "us", "--option", "grid_export", "--csv", str(tmp_path / "p.csv")]) == 0
    assert "UL 2877" in capsys.readouterr().out
    assert (tmp_path / "p.csv").exists()
