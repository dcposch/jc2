#!/usr/bin/env python3
"""Pinned k=4 ray residual chart driver.

Main chart:
  h = y^(K-1)(y-x) + lower terms, monic in y
  beta_b = mu*y^s*(y-x), s=b-1
  B = 2*beta
  f = h^2 + B
  g = h^3 + (3/2)*B*h + (3/8)*Al, Al = quo_y(B^2,h)

The ideal consists of:
  * all non-x^tk coefficients of J(f,g), formed through ID6,
  * the K+6 theorem rows coeff_{deg>K+6}(64*(g^2-f^3)-lam*f),
  * rho degree/top rows forced by LEVEL-4 when requested,
  * CSTP-1 and mu*mu_inv-1 as dehomogenization/localization generators.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from typing import Any, Iterable

ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "k4raypinned-20260903"
RUNS = HERE / "runs"

sys.path.insert(0, str(ROOT))

from box.lib.guided_gb import (  # noqa: E402
    HilbertHint,
    PromotionPolicy,
    RunConfig,
    SingularSystem,
    guided_groebner,
    prelude_from_script,
)


QUOY = """proc quoy(poly p, poly hh, int K)
{ poly q=0; poly ld; matrix cp; int d;
  while(1){ if(p==0){break;} cp=coeffs(p,y); d=nrows(cp)-1; if(d<K){break;}
    ld=cp[d+1,1]; q=q+ld*y^(d-K); p=p-ld*y^(d-K)*hh; } return(q); }"""


HINT_K4_B3_NUM = (
    1,
    0,
    -21,
    29,
    159,
    -566,
    546,
    558,
    -2037,
    2408,
    -1485,
    429,
    13,
    -42,
    8,
    0,
)


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(payload, encoding="utf-8")
    tmp.replace(path)


def mons(dmax: int, ymax: int) -> list[tuple[int, int]]:
    return [(i, j) for j in range(ymax + 1) for i in range(dmax - j + 1)]


def h_mons(K: int, drop_top: bool = True) -> list[tuple[int, int]]:
    out = mons(K - 1, K - 1)
    if drop_top:
        out = [ij for ij in out if ij != (0, K - 1)]
    return out


def lower_beta_mons(b: int, K: int) -> list[tuple[int, int]]:
    return mons(b - 1, K - 1)


def var_h(i: int, j: int) -> str:
    return f"h_{i}_{j}"


def var_b(i: int, j: int) -> str:
    return f"B_{i}_{j}"


def join_terms(terms: Iterable[str]) -> str:
    items = [term for term in terms if term]
    return " + ".join(items) if items else "0"


def pinned_metadata(K: int, b: int | None = None, s: int | None = None) -> dict[str, Any]:
    if b is None:
        b = K - 2
    if s is None:
        s = b - 1
    if b < 1:
        raise ValueError("b must be positive")
    if s < 0 or s + 1 != b:
        raise ValueError("this pinned driver expects beta_b=mu*y^(b-1)*(y-x)")
    hm = h_mons(K)
    bm = lower_beta_mons(b, K)
    return {
        "K": K,
        "b": b,
        "s": s,
        "rho_top_degree": 3 * b - 2 * K,
        "h_parameter_count": len(hm),
        "lower_beta_parameter_count": len(bm),
        "geometric_parameter_count": len(hm) + len(bm) + 1,
        "gb_parameter_count_without_localizer": len(hm) + len(bm) + 2,
        "gb_parameter_count_with_localizer": len(hm) + len(bm) + 3,
    }


def pinned_prelude(
    K: int,
    *,
    b: int | None = None,
    s: int | None = None,
    ch: int = 0,
    tk: int = 4,
    theorem_cut: bool = True,
    rho_level4: bool = True,
    drop_top: bool = True,
) -> tuple[str, list[str], list[int], dict[str, Any]]:
    meta = pinned_metadata(K, b, s)
    b = int(meta["b"])
    s = int(meta["s"])
    hm = h_mons(K, drop_top)
    bm = lower_beta_mons(b, K)

    pv: list[tuple[str, int]] = []
    pv.extend((var_h(i, j), K - i - j) for i, j in hm)
    pv.extend((var_b(i, j), 2 * K - i - j) for i, j in bm)
    pv.append(("mu", 2 * K - b))
    if theorem_cut:
        pv.append(("lam", 4 * K))
    pv.append(("mu_inv", 1))
    names = [name for name, _weight in pv]
    weights = [weight for _name, weight in pv]

    lines: list[str] = []
    add = lines.append
    add("option(redSB); short=0;")
    add(
        f"// pinned k4 ray chart K={K} b={b} s={s} char={ch} "
        f"target=x^{tk} geometric_params={meta['geometric_parameter_count']}"
    )
    add(f"ring RR = {ch},(x,y,{','.join(names)}),dp;")
    add(QUOY)
    h_lower = join_terms(f"{var_h(i,j)}*x^{i}*y^{j}" for i, j in hm)
    add(f"poly h = y^{K-1}*(y-x)" + (f" + {h_lower}" if h_lower != "0" else "") + ";")
    b_lower = join_terms(f"{var_b(i,j)}*x^{i}*y^{j}" for i, j in bm)
    add(f"poly Btop = 2*mu*y^{s}*(y-x);")
    add("poly B = Btop" + (f" + {b_lower}" if b_lower != "0" else "") + ";")
    add("poly f = h^2 + B;")
    add(f"poly Al = quoy(B^2, h, {K});")
    add("poly Rh = B^2 - Al*h;")
    add('print("PRE__SIZE_AL "+string(size(Al))+" SIZE_RH "+string(size(Rh)));')
    add('print("PRE__PIN_BTOP_DEG "+string(deg(Btop))+" SIZE_BTOP "+string(size(Btop)));')

    add("ideal I0; ideal JROWS; ideal EROWS; ideal RHOROWS; int ii; int dde;")

    if rho_level4:
        rdeg = int(meta["rho_top_degree"])
        if rdeg < 0:
            add(f'print("PRE__RHOLEVEL4_SKIPPED negative_rdeg_{rdeg}");')
        else:
            add(f"poly Rh_forced_top = (4/3)*mu^3*y^{s*3 - 2*K + 2}*(y-x);")
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
    else:
        add('print("PRE__RHOLEVEL4_SKIPPED disabled");')

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
    add(f"  if (CJ[1,ii]==x^{tk}) {{ CST=CJ[2,ii]; TARGET_FOUND=1; }}")
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
        add(f"  if (dde>{K+6}) {{ if (CE[2,ii] != 0) {{ EROWS=EROWS+ideal(CE[2,ii]); }} }}")
        add("}")
        add("EROWS = simplify(EROWS,2);")
        add(f'print("PRE__THEOREM_CUTOFF {K+6}");')
        add('print("PRE__THEOREM_ROWS "+string(size(EROWS)));')
        add("I0 = I0 + EROWS;")
    else:
        add('print("PRE__THEOREM_SKIPPED disabled");')

    add("I0 = simplify(I0,2);")
    add('print("PRE__NROWS "+string(size(I0)));')
    add(f'print("PRE__NPARAMS_GEOM {meta["geometric_parameter_count"]}");')
    add(f'print("PRE__NPARAMS_GB {len(names)}");')
    add(f"ring SS = {ch},({','.join(names)}),wp({','.join(str(weight) for weight in weights)});")
    add("ideal ROWS = imap(RR,I0); poly CSTP = imap(RR,CST);")
    add('print("PRE__CST_ZERO "+string(CSTP==0));')
    add('print("PRE__CST_WT "+string(deg(CSTP)));')
    add('print("PRE__HOMOG_I "+string(homog(ROWS)));')
    add('print("PRE__HOMOG_CST "+string(homog(CSTP)));')
    add('print("PRE__LOCALIZER mu*mu_inv-1");')
    add('print("PRE__PRELUDE_DONE 1");')
    meta = {
        **meta,
        "names": names,
        "weights": weights,
        "gb_parameter_count_without_localizer": len(names) - 1,
        "gb_parameter_count_with_localizer": len(names),
        "lambda_variable_included": theorem_cut,
        "theorem_cut": theorem_cut,
        "rho_level4": rho_level4,
        "target_power": tk,
        "characteristic": ch,
    }
    return "\n".join(lines), names, weights, meta


def run_singular_count(prelude: str, tag: str, timeout: int) -> dict[str, Any]:
    RUNS.mkdir(parents=True, exist_ok=True)
    cache = RUNS / f"{tag}.rowcount.json"
    script = RUNS / f"{tag}.count.sing"
    atomic_write(script, prelude + '\nprint("PRE__ROWS_FINAL "+string(size(ROWS)));\nquit;\n')
    t0 = time.time()
    cmd = ["stdbuf", "-oL", "-eL", "Singular", "--no-rc", "-q", str(script)]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)
        stdout = proc.stdout
        stderr = proc.stderr
        timed_out = False
        returncode = proc.returncode
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", errors="replace")
        timed_out = True
        returncode = None
    atomic_write(RUNS / f"{tag}.count.out", stdout)
    atomic_write(RUNS / f"{tag}.count.err", stderr)
    markers: dict[str, str] = {}
    for line in stdout.splitlines():
        if line.startswith("PRE__"):
            parts = line.split(maxsplit=1)
            markers[parts[0]] = parts[1] if len(parts) > 1 else ""
    info = {
        "tag": tag,
        "wall": round(time.time() - t0, 3),
        "timed_out": timed_out,
        "returncode": returncode,
        "n": int(markers["PRE__ROWS_FINAL"]) if "PRE__ROWS_FINAL" in markers else None,
        "markers": markers,
    }
    atomic_write(cache, json.dumps(info, indent=2, sort_keys=True) + "\n")
    return info


def build_system(
    tag: str,
    K: int,
    *,
    b: int | None,
    s: int | None,
    ch: int,
    tk: int,
    theorem_cut: bool,
    rho_level4: bool,
    count_timeout: int,
) -> tuple[SingularSystem | None, dict[str, Any], dict[str, Any]]:
    prelude, names, weights, meta = pinned_prelude(
        K,
        b=b,
        s=s,
        ch=ch,
        tk=tk,
        theorem_cut=theorem_cut,
        rho_level4=rho_level4,
    )
    info = run_singular_count(prelude, f"{tag}_p{ch}", count_timeout)
    if info["n"] is None:
        return None, info, meta
    generators = [f"ROWS[{idx}]" for idx in range(1, info["n"] + 1)]
    generators.extend(["CSTP-1", "mu*mu_inv-1"])
    system = SingularSystem(
        name=f"{tag}_p{ch}",
        prelude=prelude,
        generators=tuple(generators),
        characteristic=ch,
        variables=tuple(names),
        homogeneous=False,
        positive_weights=(),
        metadata=meta,
    )
    return system, info, meta


def run_chart(
    tag: str,
    K: int,
    *,
    b: int | None = None,
    s: int | None = None,
    chars: tuple[int, ...] = (0,),
    tk: int = 4,
    timeout: int = 900,
    count_timeout: int = 240,
    cores: int = 4,
    theorem_cut: bool = True,
    rho_level4: bool = True,
) -> dict[str, Any]:
    if cores < 1 or cores > 4:
        raise ValueError("cores must be between 1 and 4")
    systems: list[SingularSystem] = []
    counts: list[dict[str, Any]] = []
    metas: list[dict[str, Any]] = []
    for ch in chars:
        system, info, meta = build_system(
            tag,
            K,
            b=b,
            s=s,
            ch=ch,
            tk=tk,
            theorem_cut=theorem_cut,
            rho_level4=rho_level4,
            count_timeout=count_timeout,
        )
        counts.append(info)
        metas.append(meta)
        if system is not None:
            systems.append(system)
    if not systems:
        summary = {"tag": tag, "K": K, "verdict": "PRELUDE_FAILED", "counts": counts, "metadata": metas}
        out_dir = RUNS / tag
        atomic_write(out_dir / "summary.json", json.dumps(summary, indent=2, sort_keys=True) + "\n")
        print(json.dumps(summary, sort_keys=True))
        return summary

    cfg = RunConfig(
        output_dir=RUNS / tag,
        timeout_seconds=timeout,
        total_cores=cores,
        max_parallel_jobs=min(len(systems), cores),
        run_perturbed_control=False,
    )
    t0 = time.time()
    result = guided_groebner(
        systems,
        hint=None,
        policy=PromotionPolicy.exact_q("pinned k4 ray dehomogenised/localised residual chart"),
        config=cfg,
    )
    wall = round(time.time() - t0, 3)
    summary = {
        "tag": tag,
        "K": K,
        "b": metas[0]["b"],
        "s": metas[0]["s"],
        "chars": list(chars),
        "target": f"x^{tk}",
        "theorem_cut": theorem_cut,
        "rho_level4": rho_level4,
        "counts": counts,
        "metadata": metas[0],
        "extra_generators": ["CSTP-1", "mu*mu_inv-1"],
        "wall": wall,
        "verdict": result.verdict.value,
        "promotion_note": result.certificate["promotion_note"],
        "accepted_run_count": result.certificate["accepted_run_count"],
        "runs": [
            {
                "label": run["label"],
                "char": run["characteristic"],
                "unit": run["main"]["unit"],
                "dimension": run["main"]["dimension"],
                "vdim": run["main"]["vdim"],
                "basis_size": run["main"]["basis_size"],
                "nf_all_zero": run["main"]["nf_all_zero"],
                "timed_out": run["timed_out"],
                "returncode": run["returncode"],
                "elapsed_seconds": run["elapsed_seconds"],
                "stdout_sha256": run["stdout_sha256"],
                "script_sha256": run["script_sha256"],
            }
            for run in result.certificate["runs"]
        ],
        "crt_rational_reconstruction": result.certificate["crt_rational_reconstruction"],
    }
    atomic_write(RUNS / tag / "summary.json", json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, sort_keys=True))
    return summary


def positive_control(timeout: int, cores: int) -> dict[str, Any]:
    tag = "CTRL_TAME_K1"
    prelude = "\n".join(
        [
            "option(redSB); short=0;",
            "ring RR = 0,(x,y,mu,mu_inv),dp;",
            "poly h = y-x;",
            "poly beta = mu*x;",
            "poly f = h^2 + 2*beta;",
            "poly g = h^3 + 3*beta*h;",
            "poly JJ = diff(f,x)*diff(g,y)-diff(f,y)*diff(g,x);",
            'print("PRE__CTRL_J "+string(JJ));',
            "matrix CJ = coef(JJ,x*y);",
            "ideal I0; poly CST=0; int ii;",
            "for (ii=1; ii<=ncols(CJ); ii++)",
            "{",
            "  if (CJ[1,ii]==x) { CST=CJ[2,ii]; }",
            "  else { if (CJ[2,ii] != 0) { I0=I0+ideal(CJ[2,ii]); } }",
            "}",
            "I0=simplify(I0,2);",
            'print("PRE__NROWS "+string(size(I0)));',
            "ring SS = 0,(mu,mu_inv),dp;",
            "ideal ROWS=imap(RR,I0); poly CSTP=imap(RR,CST);",
            'print("PRE__CST_ZERO "+string(CSTP==0));',
            'print("PRE__PRELUDE_DONE 1");',
        ]
    )
    info = run_singular_count(prelude, f"{tag}_p0", 60)
    generators = [f"ROWS[{idx}]" for idx in range(1, (info["n"] or 0) + 1)]
    generators.extend(["CSTP-1", "mu*mu_inv-1"])
    system = SingularSystem(
        name=f"{tag}_p0",
        prelude=prelude,
        generators=tuple(generators),
        characteristic=0,
        variables=("mu", "mu_inv"),
        homogeneous=False,
        metadata={"control": "tame two-point survivor", "J": "6*mu^2*x"},
    )
    result = guided_groebner(
        system,
        policy=PromotionPolicy.exact_q("tame two-point survivor must not be killed"),
        config=RunConfig(RUNS / tag, timeout_seconds=timeout, total_cores=cores, run_perturbed_control=False),
    )
    summary = {
        "tag": tag,
        "verdict": result.verdict.value,
        "promotion_note": result.certificate["promotion_note"],
        "counts": info,
        "runs": [
            {
                "dimension": run["main"]["dimension"],
                "vdim": run["main"]["vdim"],
                "unit": run["main"]["unit"],
                "timed_out": run["timed_out"],
                "elapsed_seconds": run["elapsed_seconds"],
            }
            for run in result.certificate["runs"]
        ],
    }
    atomic_write(RUNS / tag / "summary.json", json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, sort_keys=True))
    return summary


def perturbed_hint_control(timeout: int, cores: int) -> dict[str, Any]:
    tag = "CTRL_HINT_K4_B3"
    script = ROOT / "box/k16stdhilb-20260903/t5_p1009_b0_tail_guided.sing"
    meta = json.loads(script.with_suffix(".json").read_text(encoding="utf-8"))
    prelude = prelude_from_script(script)
    generators = tuple(f"T{row}" for row in meta["selected_rows"])
    weights = tuple(meta["weights"])
    expected_length = int(meta["predicted_tail_length"])
    hint = HilbertHint.from_sequences(meta["target_hnum"], weights, expected_length)
    system = SingularSystem(
        name=f"{tag}_p1009",
        prelude=prelude,
        generators=generators,
        characteristic=1009,
        variables=tuple(meta["variables"]),
        homogeneous=True,
        positive_weights=weights,
        metadata={
            "control": "guided_gb Hilbert hint perturbation",
            "source_script": str(script.relative_to(ROOT)),
            "predicted_length": expected_length,
        },
    )
    result = guided_groebner(
        system,
        hint=hint,
        policy=PromotionPolicy.homogeneous_properness("charged homogeneous positive-weight hint fixture"),
        config=RunConfig(RUNS / tag, timeout_seconds=timeout, total_cores=cores, run_perturbed_control=True),
    )
    run = result.certificate["runs"][0]
    summary = {
        "tag": tag,
        "verdict": result.verdict.value,
        "accepted_run_count": result.certificate["accepted_run_count"],
        "predicted_length": expected_length,
        "main_lead_vdim": run["main"]["lead_vdim"],
        "perturbed_lead_vdim": None if run["perturbed"] is None else run["perturbed"]["lead_vdim"],
        "main_accepted": run["main"]["accepted"],
        "perturbed_accepted": None if run["perturbed"] is None else run["perturbed"]["accepted"],
        "elapsed_seconds": run["elapsed_seconds"],
    }
    atomic_write(RUNS / tag / "summary.json", json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, sort_keys=True))
    return summary


def run_controls(timeout: int, cores: int) -> list[dict[str, Any]]:
    outputs = []
    outputs.append(run_chart("CTRL_PIN_K4_B3", 4, b=3, s=2, timeout=timeout, count_timeout=120, cores=cores))
    outputs.append(run_chart("CTRL_PIN_K5_B4", 5, b=4, s=3, timeout=timeout, count_timeout=120, cores=cores))
    outputs.append(positive_control(timeout=120, cores=1))
    outputs.append(perturbed_hint_control(timeout=300, cores=1))
    atomic_write(RUNS / "controls.summary.json", json.dumps(outputs, indent=2, sort_keys=True) + "\n")
    return outputs


def summarize() -> dict[str, Any]:
    summaries: dict[str, Any] = {}
    for path in sorted(RUNS.glob("*/summary.json")):
        summaries[path.parent.name] = json.loads(path.read_text(encoding="utf-8"))
    atomic_write(HERE / "summary-all.json", json.dumps(summaries, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"summary_count": len(summaries), "tags": sorted(summaries)}, sort_keys=True))
    return summaries


def parse_chars(text: str) -> tuple[int, ...]:
    return tuple(int(piece) for piece in text.split(",") if piece != "")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_meta = sub.add_parser("meta")
    p_meta.add_argument("K", type=int)
    p_meta.add_argument("--b", type=int)
    p_meta.add_argument("--s", type=int)

    p_count = sub.add_parser("count")
    p_count.add_argument("tag")
    p_count.add_argument("K", type=int)
    p_count.add_argument("--b", type=int)
    p_count.add_argument("--s", type=int)
    p_count.add_argument("--char", type=int, default=0)
    p_count.add_argument("--tk", type=int, default=4)
    p_count.add_argument("--timeout", type=int, default=240)
    p_count.add_argument("--no-theorem", action="store_true")
    p_count.add_argument("--no-rho-level4", action="store_true")

    p_run = sub.add_parser("run")
    p_run.add_argument("tag")
    p_run.add_argument("K", type=int)
    p_run.add_argument("--b", type=int)
    p_run.add_argument("--s", type=int)
    p_run.add_argument("--chars", default="0")
    p_run.add_argument("--tk", type=int, default=4)
    p_run.add_argument("--timeout", type=int, default=900)
    p_run.add_argument("--count-timeout", type=int, default=240)
    p_run.add_argument("--cores", type=int, default=4)
    p_run.add_argument("--no-theorem", action="store_true")
    p_run.add_argument("--no-rho-level4", action="store_true")

    p_batch = sub.add_parser("batch-main")
    p_batch.add_argument("--timeout", type=int, default=900)
    p_batch.add_argument("--count-timeout", type=int, default=240)
    p_batch.add_argument("--cores", type=int, default=4)

    p_ctrl = sub.add_parser("controls")
    p_ctrl.add_argument("--timeout", type=int, default=300)
    p_ctrl.add_argument("--cores", type=int, default=4)

    sub.add_parser("summarize")

    args = parser.parse_args()
    if args.cmd == "meta":
        print(json.dumps(pinned_metadata(args.K, args.b, args.s), indent=2, sort_keys=True))
    elif args.cmd == "count":
        prelude, _names, _weights, meta = pinned_prelude(
            args.K,
            b=args.b,
            s=args.s,
            ch=args.char,
            tk=args.tk,
            theorem_cut=not args.no_theorem,
            rho_level4=not args.no_rho_level4,
        )
        info = run_singular_count(prelude, f"{args.tag}_p{args.char}", args.timeout)
        print(json.dumps({"metadata": meta, "count": info}, indent=2, sort_keys=True))
    elif args.cmd == "run":
        run_chart(
            args.tag,
            args.K,
            b=args.b,
            s=args.s,
            chars=parse_chars(args.chars),
            tk=args.tk,
            timeout=args.timeout,
            count_timeout=args.count_timeout,
            cores=args.cores,
            theorem_cut=not args.no_theorem,
            rho_level4=not args.no_rho_level4,
        )
    elif args.cmd == "batch-main":
        outputs = [
            run_chart("MAIN_K7_PIN", 7, timeout=args.timeout, count_timeout=args.count_timeout, cores=args.cores),
            run_chart("MAIN_K8_PIN", 8, timeout=args.timeout, count_timeout=args.count_timeout, cores=args.cores),
            run_chart("MAIN_K9_PIN", 9, timeout=args.timeout, count_timeout=args.count_timeout, cores=args.cores),
        ]
        atomic_write(RUNS / "main.summary.json", json.dumps(outputs, indent=2, sort_keys=True) + "\n")
    elif args.cmd == "controls":
        run_controls(timeout=args.timeout, cores=args.cores)
    elif args.cmd == "summarize":
        summarize()


if __name__ == "__main__":
    main()
