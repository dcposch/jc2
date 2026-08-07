"""DRY-RUN GATE for the Phase 3 farm driver (lib/farm.py, cases/farm_driver.py).

GF1  catalog: the 34 GGV5 deg<=150 rows, k-histogram, S4 alias resolution.
GF2  pre-filter, family level: reg_9_24_c3's family (9,24) classifies
     MECHANISM-ABSENT (k=1 no-gap) exactly as SURPLUS-EXT 3.2; the only
     THEOREM-COVERED rows are the two (8,28) corner rows, PARTIAL, never
     skipped; 0 families settled without compute at deg<=150.
GF3  pre-filter, subcase level (SURPLUS-EXT 3.2 ground truth on the seven
     emit.py polygon sets): pentagons/quad OUT-OF-SCOPE; reg_9_24_c3 strip
     k=1 MECHANISM-ABSENT; open_8_28_c2 strip (2,2) THEOREM-COVERED -> the
     one EMPTY-BY-THEOREM client.
GF4  torus-determinant rule reproduces cases/emit.py FIX on all 7 cases.
GF5  plan: subcase ordering/naming matches the GGV22 numbering; with the
     pre-filter on, 8_28's c2 is settled EMPTY-BY-THEOREM((2, 2)) with no
     emission while c1 still computes.
GF6  DRY RUN, the four S4 families (pre-filter off) into a temp dir:
     byte-compare against every archived emission that the campaign
     produced (v6 cores, c3/c2 charts, cCa2/cCa6 splits, at p=65521 AND
     char 0); structural compare for the two pre-rewrite _partial archives
     (same a-var set, b-frontier overlap, close eq counts).  Also: the
     recomputed pivot product equals AUDIT.md's committed artifact.
GF7  dispatch: every emitted system lands on exactly one box queue,
     round-robin by size, per-box loads balanced.

Heavy (~6-10 min: two swell cascades + two 100s cascades + big writes).
FARM_GATE=fast skips GF6/GF7.
"""
import sys, os, json, tempfile, filecmp
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "cases"))
os.environ.setdefault("JC_BACKEND", "flint")

import farm
from emit import CASES, FIX

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SYS = os.path.join(ROOT, "systems")
FAST = os.environ.get("FARM_GATE", "") == "fast"

S4_NAMES = {"9_27": "9_27mn23d108", "9_24": "9_24mn23d99",
            "8_28": "8_28mn32d108", "7_21": "7_21mn23d84"}


def test_gf1_catalog():
    cat = farm.catalog(150)
    assert len(cat) == 34, len(cat)
    hist = {}
    for r in cat:
        hist[r.cd.rhs_exp] = hist.get(r.cd.rhs_exp, 0) + 1
    assert hist == {1: 19, 2: 11, 3: 2, 4: 2}, hist   # SURPLUS-EXT 3.1
    assert len({r.name for r in cat}) == 34            # names unique
    for alias, name in S4_NAMES.items():
        assert farm.find_family(alias).name == name, alias
    print("GF1 OK: 34-row catalog, k-histogram, S4 aliases")


def test_gf2_prefilter_family():
    f924 = farm.find_family("9_24")
    pf = farm.prefilter_family(f924.cd)
    assert pf["cell"] == "MECHANISM-ABSENT" and pf["k"] == 1 \
        and pf["d2star"] == 3 and not pf["skip"], pf     # SURPLUS-EXT 3.2 F17
    pf828 = farm.prefilter_family(farm.find_family("8_28").cd)
    assert pf828["cell"] == "THEOREM-COVERED" and pf828["cellkd"] == (2, 2) \
        and pf828["partial"] and not pf828["skip"], pf828
    cells = {}
    skips = 0
    for r in farm.catalog(150):
        p = farm.prefilter_family(r.cd)
        cells.setdefault(p["cell"], []).append(r.name)
        skips += p["skip"]
    assert skips == 0                                  # 3.2: no full coverage
    assert sorted(cells["THEOREM-COVERED"]) == \
        ["8_28mn32d108", "8_28mn34d144"], cells["THEOREM-COVERED"]
    assert len(cells["MECHANISM-ABSENT"]) == 23        # 19 k=1 + 4 k>=3
    print("GF2 OK: family cells per SURPLUS-EXT 3.2; (9,24)=MECHANISM-ABSENT; "
          "0 families settled without compute")


def test_gf3_prefilter_subcase():
    def cell(name):
        s = CASES[name]
        return farm.prefilter_subcase(s["cornersP"], s["cornersQ"], s["rhs"][0])
    for name in ["reg_9_27", "reg_9_24_c1", "reg_9_24_c2", "open_8_28_c1",
                 "reg_7_21"]:
        c = cell(name)
        assert c["cell"] == "OUT-OF-SCOPE" and not c["skip"], (name, c)
    c = cell("reg_9_24_c3")
    assert (c["cell"], c["d2"], c["wP"], c["wQ"], c["skip"]) == \
        ("MECHANISM-ABSENT", (3, 3), 2, 3, False), c   # 3.2 ground truth
    c = cell("open_8_28_c2")
    assert c["cell"] == "THEOREM-COVERED" and c["cellkd"] == (2, 2) \
        and c["skip"] and (c["wP"], c["wQ"]) == (2, 3), c
    print("GF3 OK: subcase cells match SURPLUS-EXT 3.2 reduced-case truth")


def test_gf4_torus_fix():
    for name, spec in CASES.items():
        fix, det = farm.torus_fix(spec["cornersP"], spec["cornersQ"],
                                  spec["rhs"][0])
        assert det != 0 and sorted(fix) == sorted(
            (k, tuple(p)) for k, p in FIX[name]), (name, fix, FIX[name])
    _, det = farm.torus_fix(CASES["open_8_28_c2"]["cornersP"],
                            CASES["open_8_28_c2"]["cornersQ"], 2)
    assert det == -100                                 # AUDIT.md claim 2
    print("GF4 OK: automatic fix_ones == emit.py FIX, det(8_28) = -100")


def test_gf5_plan():
    plan = farm.plan_family(farm.find_family("8_28"), prefilter=True)
    c1, c2 = plan["cases"]
    assert c1["name"].endswith("_c1") and c1["decision"] == "emit"
    assert [tuple(p) for p in c1["NP"]] == CASES["open_8_28_c1"]["cornersP"]
    assert c2["decision"] == "empty-by-theorem" \
        and c2["verdict"] == "EMPTY-BY-THEOREM((2, 2))" \
        and [tuple(p) for p in c2["NP"]] == CASES["open_8_28_c2"]["cornersP"]
    plan = farm.plan_family(farm.find_family("9_24"), prefilter=True)
    assert [e["decision"] for e in plan["cases"]] == ["emit"] * 3
    for e, ref in zip(plan["cases"], ["reg_9_24_c1", "reg_9_24_c2",
                                      "reg_9_24_c3"]):
        assert [tuple(p) for p in e["NP"]] == CASES[ref]["cornersP"], ref
        assert [tuple(p) for p in e["NQ"]] == CASES[ref]["cornersQ"], ref
    print("GF5 OK: plans; c-numbering = GGV22; 8_28 c2 EMPTY-BY-THEOREM, "
          "no emission; c1 computes")


# ---------------------------------------------------------------- GF6 dry run

BYTE_MAP = {   # (family alias, farm system name suffix) -> archive base name
    "9_24": [("c1_core", "reg_9_24_c1_v6"), ("c2_core", "reg_9_24_c2_v6"),
             ("c3_core", "reg_9_24_c3_v6"), ("c3_chartG", "reg_9_24_c3_chartG"),
             ("c3_chartC", "reg_9_24_c3_chartC")],
    "8_28": [("c1_core", "open_8_28_c1_v6"), ("c2_core", "open_8_28_c2_v6"),
             ("c2_chartG", "open_8_28_c2_chartG"),
             ("c2_chartC", "open_8_28_c2_chartC"),
             ("c2_cCa2", "open_8_28_c2_cCa2"), ("c2_cCa6", "open_8_28_c2_cCa6")],
}
STRUCT_MAP = {"9_27": ("c1_partial", "reg_9_27_partial"),
              "7_21": ("c1_partial", "reg_7_21_partial")}


def _vars_of(path):
    with open(path) as f:
        return f.readline().strip().split(",")


def _run_four(tmp):
    from families import get_pllc
    mans = {}
    pllc = get_pllc(60)
    for alias in ["9_24", "8_28", "9_27", "7_21"]:
        row = farm.find_family(alias)
        mans[alias] = farm.run_family(row, tmp, relroot=ROOT, prefilter=False,
                                      pllc=pllc, verbose=False)
    return mans


def test_gf6_dry_run_gate(tmp=None):
    tmpdir = tmp or tempfile.mkdtemp(prefix="farmgate_")
    mans = _run_four(tmpdir)
    nbyte = 0
    for alias, pairs in BYTE_MAP.items():
        fam = S4_NAMES[alias]
        for suffix, ref in pairs:
            for ch in ("p65521.ms", "q.ms"):
                a = os.path.join(tmpdir, fam, f"{fam}_{suffix}.{ch}")
                b = os.path.join(SYS, f"{ref}.{ch}")
                if not os.path.exists(b):
                    continue                    # archive lacks this char
                assert os.path.exists(a), a
                assert filecmp.cmp(a, b, shallow=False), (a, b)
                nbyte += 1
    assert nbyte == 22, nbyte
    # structural compare for the two pre-rewrite partial archives
    for alias, (suffix, ref) in STRUCT_MAP.items():
        fam = S4_NAMES[alias]
        man = mans[alias]
        e = man["cases"][0]
        assert e["cascade"]["status"] == "aborted-swell", alias
        assert e["verdict"] == "PARTIAL-EMITTED"
        assert any("aborted-swell" in s for s in man["statuses"])
        a = os.path.join(tmpdir, fam, f"{fam}_{suffix}.p65521.ms")
        va, vb = set(_vars_of(a)), set(_vars_of(os.path.join(SYS, f"{ref}.p65521.ms")))
        asplit = lambda vs: {v for v in vs if v[0] == "a"}
        assert asplit(va) == asplit(vb), alias          # same a-frontier
        assert len(va & vb) / len(va | vb) > 0.9, alias # b-frontier overlap
    # the recomputed pivot product == AUDIT.md committed artifact
    ch = next(e for e in mans["8_28"]["cases"] if e["name"].endswith("c2"))["chart"]
    assert ch["prod_terms"] == 1 and ch["prod_nonunits"] == ["a2", "a6"]
    assert ch["prod"].replace(" ", "") == "-1/5*a2^2*a6*ia1^2*ib43", ch["prod"]
    assert ch["splits"] == ["a2", "a6"]
    # manifest hygiene: every recorded path exists with recorded size
    for man in mans.values():
        for e in man["cases"]:
            for rec in e.get("systems", []):
                if "path" in rec:
                    p = os.path.join(ROOT, rec["path"])
                    assert os.path.getsize(p) == rec["bytes"], rec
    print(f"GF6 OK: dry run reproduces the S4 archives -- {nbyte} files "
          "byte-identical (incl. char 0), partials structurally matched, "
          "pivot product == AUDIT.md artifact")
    return tmpdir


def test_gf7_dispatch(tmpdir):
    summary = farm.dispatch(tmpdir, 3)
    qdir = os.path.join(tmpdir, "queue")
    queued = []
    for box in sorted(os.listdir(qdir)):
        with open(os.path.join(qdir, box, "queue.txt")) as f:
            queued += [l.strip() for l in f if l.strip() and not l.startswith("#")]
    emitted = []
    for fam in os.listdir(tmpdir):
        mp = os.path.join(tmpdir, fam, "manifest.json")
        if os.path.isfile(mp):
            man = json.load(open(mp))
            for e in man["cases"]:
                emitted += [r["path"] for r in e.get("systems", []) if "path" in r]
    assert sorted(queued) == sorted(emitted), (len(queued), len(emitted))
    assert len(queued) == len(set(queued))
    loads = [b for _, b in summary]
    assert max(loads) <= 2 * (sum(loads) / len(loads)) + 1, loads
    print(f"GF7 OK: dispatch covers all {len(queued)} systems once, "
          f"loads {loads}")


if __name__ == "__main__":
    test_gf1_catalog()
    test_gf2_prefilter_family()
    test_gf3_prefilter_subcase()
    test_gf4_torus_fix()
    test_gf5_plan()
    if FAST:
        print("FARM_GATE=fast: skipping GF6/GF7 (heavy dry run)")
    else:
        tmpdir = test_gf6_dry_run_gate()
        test_gf7_dispatch(tmpdir)
    print("ALL FARM TESTS PASS")
