#!/usr/bin/env python3
"""Mechanical audit of the ten K=7 LEVEL-4 I_light chart declarations.

This does not compute a Groebner basis.  It checks that the production chart
uses the charged pinned chart's coefficient boxes and identities, adds exactly
the two-scalar LEVEL-4 top described in the charged beta-strata report, and
declares no coefficient-floor deletion.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
from pathlib import Path


ROOT = Path("/home/ubuntu/jc2")
FROZEN = Path("/tmp/jc2-lane.qb6I1q/inputs")
PINNED_PATH = FROZEN / "pinned_chart.py"
BETA_DRIVER = ROOT / "box/k4ray-beta-strata-20260905/strata_chart.py"
SOLVE_DRIVER = ROOT / "box/k4ray-strata-solve-20260905/strata_chart.py"
EMITTED = ROOT / "box/k7-strata-gate-20260905/chart-audit/emitted"
PRODUCER_JOBS = ROOT / "box/k4ray-strata-solve-20260905/all-msjob.jsonl"

FROZEN_MS = {
    (9, 0): (241, 12675213, "15b4b715767a72e152f340dda11354af380897f6670d6370f0542841cdb4c275"),
    (9, 1): (235, 11511528, "09002c7229da517ca0d809f925873aeb94d44650467bd6addf71268aacbb7934"),
    (10, 0): (261, 19173893, "273a1a0f65308af6019c3b8986fa921c76d4e27da30d0b675afc532bc3f3d434"),
    (10, 1): (255, 17715692, "a49433e9834c4fa7a76a89aef50e7f3852ee0e26ff1d665bc1c8516dc390f97d"),
    (11, 0): (281, 27133266, "e8e57139c2292f0535226e7fb8fc2fac90b459685e939b825abec31531b2367e"),
    (11, 1): (275, 25367692, "42f96a5f916e94457887e933cb8cb3f8656537e1547e719e30851075990fd4f1"),
    (12, 0): (301, 36605124, "3a3821db1511fa96096f627d5d5ed23b1b60a2c95022f33dfb90791a4c60561d"),
    (12, 1): (295, 34517061, "875573726b784dc4700de3835f0130617279eb5bab451f712f77088c26cae4e2"),
    (13, 0): (325, 47622625, "970026efbf5ffd1150def477d64de057b8212455527a15f6abbf18807d5cce2c"),
    (13, 1): (317, 45201213, "570e241e4e2515d1c97c77f9b7696e5d519fb97697543da93410ca5eb2797a8b"),
}


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_q(d: int, pin: int) -> str:
    if pin == 0:
        x0 = "x" if d == 1 else f"x^{d}"
        x1 = "x" if d - 1 == 1 else f"x^{d-1}"
        return f"q0*{x0} + q1*{x1}*y"
    x1 = "x" if d - 1 == 1 else f"x^{d-1}"
    return f"q1*{x1}*y"


def independent_prelude(pinned, b: int, pin: int, theorem_cut: bool):
    """Reconstruct the chart from charged primitives plus the report formulas."""
    K = 7
    smin = 4
    d = b - smin - 1
    nQ = 2
    hm = pinned.h_mons(K)
    bm = pinned.lower_beta_mons(b, K)
    qn = ["q0", "q1"] if pin == 0 else ["q1"]
    localizer = f"q{pin}_inv"
    pv = []
    pv.extend((pinned.var_h(i, j), K - i - j) for i, j in hm)
    pv.extend((pinned.var_b(i, j), 2 * K - i - j) for i, j in bm)
    pv.extend((q, 2 * K - b) for q in qn)
    if theorem_cut:
        pv.append(("lam", 4 * K))
    pv.append((localizer, 1))
    names = [name for name, _ in pv]
    weights = [weight for _, weight in pv]
    geom = len(hm) + len(bm) + len(qn)
    qexpr = expected_q(d, pin)

    lines = []
    add = lines.append
    add("option(redSB); short=0;")
    add(f"// k4ray beta-stratum K=7 b={b} pin=q{pin} char=0 target=x^4 geom={geom}")
    add(f"ring RR = 0,(x,y,{','.join(names)}),dp;")
    add(pinned.QUOY)
    h_lower = pinned.join_terms(
        f"{pinned.var_h(i,j)}*x^{i}*y^{j}" for i, j in hm
    )
    add("poly h = y^6*(y-x)" + (f" + {h_lower}" if h_lower != "0" else "") + ";")
    add(f"poly Q = {qexpr};")
    add("poly Btop = 2*y^4*(y-x)*Q;")
    b_lower = pinned.join_terms(
        f"{pinned.var_b(i,j)}*x^{i}*y^{j}" for i, j in bm
    )
    add("poly B = Btop" + (f" + {b_lower}" if b_lower != "0" else "") + ";")
    add("poly f = h^2 + B;")
    add("poly Al = quoy(B^2, h, 7);")
    add("poly Rh = B^2 - Al*h;")
    add('print("PRE__SIZE_AL "+string(size(Al))+" SIZE_RH "+string(size(Rh)));')
    add('print("PRE__PIN_BTOP_DEG "+string(deg(Btop))+" SIZE_BTOP "+string(size(Btop)));')
    add(f'print("PRE__PIN_INDEX {pin} NQ 2 D {d} SMIN 4");')
    add("ideal I0; ideal JROWS; ideal EROWS; ideal RHOROWS; int ii; int dde;")
    rdeg = 3 * b - 14
    add("poly Rh_forced_top = (4/3)*y^0*(y-x)*Q^3;")
    add("matrix CR = coef(Rh - Rh_forced_top, x*y);")
    add("for (ii=1; ii<=ncols(CR); ii++)")
    add("{")
    add("  dde = deg(CR[1,ii]);")
    add(f"  if (dde>{rdeg}) {{ if (CR[2,ii] != 0) {{ RHOROWS=RHOROWS+ideal(CR[2,ii]); }} }}")
    add(f"  if (dde=={rdeg}) {{ if (CR[2,ii] != 0) {{ RHOROWS=RHOROWS+ideal(CR[2,ii]); }} }}")
    add("}")
    add("RHOROWS = simplify(RHOROWS,2);")
    add(f'print("PRE__RHO_RDEG {rdeg}");')
    add('print("PRE__RHOLEVEL4_ROWS "+string(size(RHOROWS)));')
    add("I0 = I0 + RHOROWS;")
    add(
        "poly JJ = (3/8)*(diff(B,x)*diff(Al,y)-diff(B,y)*diff(Al,x))"
        " - (3/4)*(diff(h,x)*diff(Rh,y)-diff(h,y)*diff(Rh,x));"
    )
    add('print("PRE__DEG_J "+string(deg(JJ)));')
    add('print("PRE__SIZE_J "+string(size(JJ)));')
    add("matrix CJ = coef(JJ, x*y);")
    add("poly CST = 0; int TARGET_FOUND = 0;")
    add("for (ii=1; ii<=ncols(CJ); ii++)")
    add("{")
    add("  if (CJ[1,ii]==x^4) { CST=CJ[2,ii]; TARGET_FOUND=1; }")
    add("  else { if (CJ[2,ii] != 0) { JROWS=JROWS+ideal(CJ[2,ii]); } }")
    add("}")
    add("JROWS = simplify(JROWS,2);")
    add('print("PRE__J_ROWS "+string(size(JROWS))+" TARGET_FOUND "+string(TARGET_FOUND));')
    add("I0 = I0 + JROWS;")
    if theorem_cut:
        add("poly E64 = 8*B^3 - 48*Rh*h^2 - 72*B*Rh + 9*Al^2;")
        add("poly ELAM = E64 - lam*f;")
        add('print("PRE__DEG_ELAM "+string(deg(ELAM))+" SIZE_ELAM "+string(size(ELAM)));')
        add("matrix CE = coef(ELAM, x*y);")
        add("for (ii=1; ii<=ncols(CE); ii++)")
        add("{")
        add("  dde = deg(CE[1,ii]);")
        add("  if (dde>13) { if (CE[2,ii] != 0) { EROWS=EROWS+ideal(CE[2,ii]); } }")
        add("}")
        add("EROWS = simplify(EROWS,2);")
        add('print("PRE__THEOREM_CUTOFF 13");')
        add('print("PRE__THEOREM_ROWS "+string(size(EROWS)));')
        add("I0 = I0 + EROWS;")
    else:
        add('print("PRE__THEOREM_SKIPPED disabled");')
    add("I0 = simplify(I0,2);")
    add('print("PRE__NROWS "+string(size(I0)));')
    add(f'print("PRE__NPARAMS_GEOM {geom}");')
    add(f'print("PRE__NPARAMS_GB {len(names)}");')
    add(f"ring SS = 0,({','.join(names)}),wp({','.join(str(w) for w in weights)});")
    add("ideal ROWS = imap(RR,I0); poly CSTP = imap(RR,CST);")
    add('print("PRE__CST_ZERO "+string(CSTP==0));')
    add('print("PRE__CST_WT "+string(deg(CSTP)));')
    add('print("PRE__HOMOG_I "+string(homog(ROWS)));')
    add('print("PRE__HOMOG_CST "+string(homog(CSTP)));')
    add(f'print("PRE__LOCALIZER q{pin}*{localizer}-1");')
    add('print("PRE__PRELUDE_DONE 1");')
    return "\n".join(lines), names, weights


def independent_dump(prelude: str, pin: int) -> str:
    return prelude + "\n" + "\n".join([
        "int i;",
        "ROWS = ROWS + ideal(CSTP-1);",
        f"ROWS = ROWS + ideal(q{pin}*q{pin}_inv-1);",
        "ROWS = simplify(ROWS,2);",
        'print("DUMP__N "+string(size(ROWS)));',
        'print("DUMP__VARS "+string(nvars(basering)));',
        'for (i=1; i<=size(ROWS); i++) { print("DUMP__ROW "+string(cleardenom(ROWS[i]))); }',
        'print("DUMP__DONE 1");',
        "quit;",
        "",
    ])


def row_source_core(prelude: str) -> list[str]:
    """The geometric definitions and rho/J row-producing source block."""
    lines = prelude.splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("proc quoy"))
    stop = next(i for i, line in enumerate(lines) if line == "I0 = I0 + JROWS;")
    return lines[start : stop + 1]


def independent_msolve(dump_out: Path, names: list[str]) -> str:
    rows = [
        line[len("DUMP__ROW "):].strip()
        for line in dump_out.read_text().splitlines()
        if line.startswith("DUMP__ROW ")
    ]
    alias = {name: f"v{i}" for i, name in enumerate(names)}
    pat = re.compile("|".join(re.escape(n) for n in sorted(names, key=len, reverse=True)))
    gens = [
        pat.sub(lambda m: alias[m.group(0)], row).replace(" ", "")
        for row in rows if row and row != "0"
    ]
    return ",".join(alias[n] for n in names) + "\n0\n" + ",\n".join(gens) + "\n"


def main() -> None:
    pinned = load("charged_pinned_chart", PINNED_PATH)
    strata = load("production_strata_chart", SOLVE_DRIVER)

    assert sha256(PINNED_PATH) == "eed2cdf5cc5b85e3358013416bca7f6f6bd272138533ff0c065a86afb4c47e43"
    beta_text = BETA_DRIVER.read_text()
    solve_text = SOLVE_DRIVER.read_text()
    beta_root = 'HERE = ROOT / "box" / "k4ray-beta-strata-20260905"'
    solve_root = 'HERE = ROOT / "box" / "k4ray-strata-solve-20260905"'
    assert beta_text.replace(beta_root, solve_root) == solve_text

    producer_exact_q = {}
    for line in PRODUCER_JOBS.read_text().splitlines():
        if not line.startswith("MSJOB__RESULT "):
            continue
        payload = json.loads(line[len("MSJOB__RESULT "):])
        if (
            payload.get("K") == 7
            and 9 <= payload.get("b", 0) <= 13
            and payload.get("char") == 0
            and payload.get("verdict") == "EXACTQ_UNIT"
        ):
            key = (payload["b"], payload["pin_index"])
            triple = (payload["ngens"], payload["ms_bytes"], payload["ms_sha256"])
            if key in producer_exact_q:
                assert producer_exact_q[key] == triple
            producer_exact_q[key] = triple
    assert producer_exact_q == FROZEN_MS

    # Charged primitives retained by the generalized construction.
    assert strata.QUOY == pinned.QUOY
    assert strata.h_mons(7) == pinned.h_mons(7)
    assert strata.lower_beta_mons(13, 7) == pinned.lower_beta_mons(13, 7)
    assert strata.var_h(2, 3) == pinned.var_h(2, 3)
    assert strata.var_b(2, 3) == pinned.var_b(2, 3)

    rows = []
    hm = pinned.h_mons(7)
    assert len(hm) == 27
    assert set(hm) == {
        (i, j) for j in range(7) for i in range(7 - j)
    } - {(0, 6)}

    for b in range(9, 14):
        bm = pinned.lower_beta_mons(b, 7)
        full_box = {(i, j) for j in range(7) for i in range(b - j)}
        assert set(bm) == full_box
        assert len(bm) == 7 * b - 21
        d = b - 5
        for pin in (0, 1):
            pre, names, weights, meta = strata.strata_prelude(
                7, b, pin_index=pin, ch=0, theorem_cut=False
            )
            rebuilt_pre, rebuilt_names, rebuilt_weights = independent_prelude(
                pinned, b, pin, False
            )
            assert rebuilt_pre == pre
            assert rebuilt_names == names and rebuilt_weights == weights
            expected_names = [pinned.var_h(i, j) for i, j in hm]
            expected_names += [pinned.var_b(i, j) for i, j in bm]
            expected_names += (["q0", "q1"] if pin == 0 else ["q1"])
            expected_names += [f"q{pin}_inv"]
            assert names == expected_names
            assert "lam" not in names
            assert meta["smin"] == 4 and meta["ymax_Q"] == 1
            assert meta["d"] == d and meta["nQ"] == 2
            assert meta["Q_expr"] == expected_q(d, pin)
            assert meta["lower_beta_parameter_count"] == len(full_box)
            assert meta["h_parameter_count"] == 27
            assert meta["top_parameter_count"] == 2 - pin
            assert meta["rho_top_degree"] == 3 * b - 14
            assert "PRE__THEOREM_SKIPPED disabled" in pre
            assert "poly E64" not in pre and "poly ELAM" not in pre
            assert "poly Al = quoy(B^2, h, 7);" in pre
            assert "poly Rh = B^2 - Al*h;" in pre
            assert "poly JJ = (3/8)*" in pre
            assert f"poly Q = {expected_q(d, pin)};" in pre
            assert "poly Btop = 2*y^4*(y-x)*Q;" in pre
            assert "poly Rh_forced_top = (4/3)*y^0*(y-x)*Q^3;" in pre
            assert f"if (dde>{3*b-14})" in pre
            assert f"if (dde=={3*b-14})" in pre
            assert f"PRE__LOCALIZER q{pin}*q{pin}_inv-1" in pre

            # The theorem-cut construction adds an auxiliary lambda and E rows;
            # after extending the light ideal to Q[light variables,lambda], all
            # geometric variables and the light row-producing code are retained.
            full_pre, full_names, _full_weights, full_meta = strata.strata_prelude(
                7, b, pin_index=pin, ch=0, theorem_cut=True
            )
            rebuilt_full, rebuilt_full_names, rebuilt_full_weights = independent_prelude(
                pinned, b, pin, True
            )
            assert rebuilt_full == full_pre
            assert rebuilt_full_names == full_names
            assert rebuilt_full_weights == _full_weights
            assert full_names[:-2] == names[:-1]
            assert full_names[-2:] == ["lam", f"q{pin}_inv"]
            assert full_meta["lambda_variable_included"] is True
            assert row_source_core(full_pre) == row_source_core(pre)
            assert "poly E64 = 8*B^3 - 48*Rh*h^2 - 72*B*Rh + 9*Al^2;" in full_pre
            assert "poly ELAM = E64 - lam*f;" in full_pre
            assert "if (dde>13)" in full_pre
            assert "PRE__THEOREM_CUTOFF 13" in full_pre

            item = {
                "b": b,
                "pin": pin,
                "d": d,
                "Q": meta["Q_expr"],
                "h_unknowns": 27,
                "lower_beta_unknowns": len(bm),
                "top_unknowns": 2 - pin,
                "geometric_unknowns": meta["geometric_parameter_count"],
                "gb_variables": meta["gb_parameter_count"],
                "rho_cutoff": meta["rho_top_degree"],
                "light_has_lambda": False,
                "full_auxiliary_lambda": True,
                "frozen_generators": FROZEN_MS[(b, pin)][0],
                "frozen_bytes": FROZEN_MS[(b, pin)][1],
                "frozen_sha256": FROZEN_MS[(b, pin)][2],
            }
            js = EMITTED / f"K7_B{b}_Q{pin}_p0.json"
            ms = EMITTED / f"K7_B{b}_Q{pin}_p0.ms"
            if js.exists() and ms.exists():
                payload = json.loads(js.read_text())
                assert payload["ms_sha256"] == sha256(ms)
                expected_ngens, expected_bytes, expected_hash = FROZEN_MS[(b, pin)]
                assert (payload["ngens"], payload["ms_bytes"], payload["ms_sha256"]) == (
                    expected_ngens, expected_bytes, expected_hash
                )
                dump_script = EMITTED / f"K7_B{b}_Q{pin}_p0_all.dump.sing"
                dump_out = dump_script.with_suffix(".out")
                assert dump_script.read_text() == independent_dump(rebuilt_pre, pin)
                rebuilt_ms = independent_msolve(dump_out, rebuilt_names)
                assert rebuilt_ms.encode() == ms.read_bytes()
                assert b"/" not in ms.read_bytes()
                assert ms.read_text().splitlines()[1] == "0"
                item.update(
                    emitted_sha256=payload["ms_sha256"],
                    emitted_bytes=payload["ms_bytes"],
                    emitted_generators=payload["ngens"],
                    fresh_matches_frozen=True,
                    markers=payload["markers"],
                )
            rows.append(item)

    print(json.dumps({
        "charged_pinned_sha256": sha256(PINNED_PATH),
        "producer_jobs_sha256": sha256(PRODUCER_JOBS),
        "beta_to_solver_driver_difference": "output-root line only",
        "charged_primitives_match": [
            "QUOY", "h_mons", "lower_beta_mons", "var_h", "var_b"
        ],
        "independent_preludes_match_byte_for_byte": True,
        "independent_alias_emission_matches_byte_for_byte": True,
        "light_geometric_row_source_equals_full_under_lambda_extension": True,
        "no_floor_deletion": True,
        "charts": rows,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
