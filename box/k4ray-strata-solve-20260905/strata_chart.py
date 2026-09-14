#!/usr/bin/env python3
"""Per-stratum k=4-ray charts with the LEVEL-4 top band, unpinned below.

For residual b = deg beta in [b_min, 2K-1]:

    H = y^(K-1)*(y-x)
    smin = ceil(2(K-1)/3)
    P = y^smin * (y-x) * Q
    Q = sum_{j=0..min(d, ymax_Q)} q_j x^(d-j) y^j
    d = b - smin - 1
    ymax_Q = K-2-smin   (=1 at K=7,8,9)

This is the full LEVEL-4 locus H^2 | P^3 on homogeneous P of degree b with
deg_y P <= K-1, not a one-scalar pin (that pin is the d=0 case b=b_min only).

The lower beta block is the exact box mons(b-1, K-1) of 17(bbbbbb)/pinned_chart
(no weight-floor drop of unknowns).  The light decision ideal is

    I_light = < non-x^4 coeffs of ID6 J,  LEVEL-4 rho rows,  CSTP-1,  localizer >

A unit of I_light kills the theorem-cut ideal.  Cover charts for P != 0:

    q0-chart: q0 * q0_inv - 1          (q0 != 0, remaining q_j free)
    qj-chart: q_0=...=q_{j-1}=0 and q_j * q_j_inv - 1

FALLACY-v2: dropping ROWS is safe; the rho rows add equations.  The
localization is the explicit Rabinowitsch generator, not a dropped unknown.
Exact Q is the only characteristic-zero promotion path.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import sys
import time
from typing import Any, Iterable

ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "k4ray-strata-solve-20260905"
RUNS = HERE / "runs"

sys.path.insert(0, str(ROOT))

from box.lib.guided_gb import (  # noqa: E402
    PromotionPolicy,
    RunConfig,
    SingularSystem,
    guided_groebner,
)


QUOY = """proc quoy(poly p, poly hh, int K)
{ poly q=0; poly ld; matrix cp; int d;
  while(1){ if(p==0){break;} cp=coeffs(p,y); d=nrows(cp)-1; if(d<K){break;}
    ld=cp[d+1,1]; q=q+ld*y^(d-K); p=p-ld*y^(d-K)*hh; } return(q); }"""


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(payload, encoding="utf-8")
    tmp.replace(path)


def mons(dmax: int, ymax: int) -> list[tuple[int, int]]:
    if dmax < 0:
        return []
    return [(i, j) for j in range(ymax + 1) for i in range(dmax - j + 1)]


def h_mons(K: int, drop_top: bool = True) -> list[tuple[int, int]]:
    out = mons(K - 1, K - 1)
    if drop_top:
        out = [ij for ij in out if ij != (0, K - 1)]
    return out


def lower_beta_mons(b: int, K: int) -> list[tuple[int, int]]:
    return mons(b - 1, K - 1)


def smin_of(K: int) -> int:
    return math.ceil(2 * (K - 1) / 3)


def bmin_of(K: int) -> int:
    return max(smin_of(K) + 1, math.ceil((2 * K + 1) / 3))


def ymax_Q_of(K: int) -> int:
    return K - 2 - smin_of(K)


def var_h(i: int, j: int) -> str:
    return f"h_{i}_{j}"


def var_b(i: int, j: int) -> str:
    return f"B_{i}_{j}"


def join_terms(terms: Iterable[str]) -> str:
    items = [term for term in terms if term]
    return " + ".join(items) if items else "0"


def stratum_metadata(K: int, b: int, pin_index: int = 0) -> dict[str, Any]:
    if b < 1:
        raise ValueError("b must be positive")
    smin = smin_of(K)
    d = b - smin - 1
    if d < 0:
        raise ValueError(f"b={b} is below the LEVEL-4 floor smin+1={smin+1}")
    yq = ymax_Q_of(K)
    nQ = min(d, yq) + 1
    if pin_index < 0 or pin_index >= nQ:
        raise ValueError(f"pin_index {pin_index} out of range 0..{nQ-1}")
    hm = h_mons(K)
    bm = lower_beta_mons(b, K)
    # Cover chart pin_index: q_0=...=q_{pin_index-1} are omitted (set to 0);
    # q_pin_index is localized; later q_j remain free.
    nQ_chart = nQ - pin_index
    return {
        "K": K,
        "b": b,
        "smin": smin,
        "d": d,
        "ymax_Q": yq,
        "nQ": nQ,
        "pin_index": pin_index,
        "nQ_chart": nQ_chart,
        "rho_top_degree": 3 * b - 2 * K,
        "h_parameter_count": len(hm),
        "lower_beta_parameter_count": len(bm),
        "top_parameter_count": nQ_chart,
        "geometric_parameter_count": len(hm) + len(bm) + nQ_chart,
        "bmin": bmin_of(K),
        "bmax": 2 * K - 1,
        "one_scalar_pin": nQ == 1,
        "cover": f"q{pin_index}!=0"
        + ("".join(f", q{j}=0" for j in range(pin_index))),
    }


def q_names(nQ: int, pin_index: int) -> list[str]:
    return [f"q{j}" for j in range(pin_index, nQ)]


def strata_prelude(
    K: int,
    b: int,
    *,
    pin_index: int = 0,
    ch: int = 0,
    tk: int = 4,
    theorem_cut: bool = False,
    rho_level4: bool = True,
) -> tuple[str, list[str], list[int], dict[str, Any]]:
    meta = stratum_metadata(K, b, pin_index)
    smin = int(meta["smin"])
    d = int(meta["d"])
    nQ = int(meta["nQ"])
    hm = h_mons(K)
    bm = lower_beta_mons(b, K)
    qn = q_names(nQ, pin_index)
    localizer = f"q{pin_index}_inv"

    pv: list[tuple[str, int]] = []
    pv.extend((var_h(i, j), K - i - j) for i, j in hm)
    pv.extend((var_b(i, j), 2 * K - i - j) for i, j in bm)
    pv.extend((name, 2 * K - b) for name in qn)
    if theorem_cut:
        pv.append(("lam", 4 * K))
    pv.append((localizer, 1))
    names = [name for name, _weight in pv]
    weights = [weight for _name, weight in pv]

    Q_terms: list[str] = []
    for j in range(nQ):
        if j < pin_index:
            continue
        mon = []
        xp = d - j
        yp = j
        if xp:
            mon.append(f"x^{xp}" if xp != 1 else "x")
        if yp:
            mon.append(f"y^{yp}" if yp != 1 else "y")
        body = "*".join(mon) if mon else "1"
        Q_terms.append(f"q{j}*{body}" if body != "1" else f"q{j}")
    Q_expr = join_terms(Q_terms)

    lines: list[str] = []
    add = lines.append
    add("option(redSB); short=0;")
    add(
        f"// k4ray beta-stratum K={K} b={b} pin=q{pin_index} char={ch} "
        f"target=x^{tk} geom={meta['geometric_parameter_count']}"
    )
    add(f"ring RR = {ch},(x,y,{','.join(names)}),dp;")
    add(QUOY)
    h_lower = join_terms(f"{var_h(i,j)}*x^{i}*y^{j}" for i, j in hm)
    add(f"poly h = y^{K-1}*(y-x)" + (f" + {h_lower}" if h_lower != "0" else "") + ";")
    add(f"poly Q = {Q_expr};")
    add(f"poly Btop = 2*y^{smin}*(y-x)*Q;")
    b_lower = join_terms(f"{var_b(i,j)}*x^{i}*y^{j}" for i, j in bm)
    add("poly B = Btop" + (f" + {b_lower}" if b_lower != "0" else "") + ";")
    add("poly f = h^2 + B;")
    add(f"poly Al = quoy(B^2, h, {K});")
    add("poly Rh = B^2 - Al*h;")
    add('print("PRE__SIZE_AL "+string(size(Al))+" SIZE_RH "+string(size(Rh)));')
    add('print("PRE__PIN_BTOP_DEG "+string(deg(Btop))+" SIZE_BTOP "+string(size(Btop)));')
    add(f'print("PRE__PIN_INDEX {pin_index} NQ {nQ} D {d} SMIN {smin}");')

    add("ideal I0; ideal JROWS; ideal EROWS; ideal RHOROWS; int ii; int dde;")

    rdeg = int(meta["rho_top_degree"])
    if rho_level4:
        if rdeg < 0:
            add(f'print("PRE__RHOLEVEL4_SKIPPED negative_rdeg_{rdeg}");')
        else:
            # Rh = 4 rho, rho_top = P^3 / (3 H^2), P = y^smin (y-x) Q,
            # P^3/H^2 = y^{3 smin - 2K + 2} (y-x) Q^3.
            exp_y = 3 * smin - 2 * K + 2
            add(f"poly Rh_forced_top = (4/3)*y^{exp_y}*(y-x)*Q^3;")
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
    add(f'print("PRE__LOCALIZER q{pin_index}*{localizer}-1");')
    add('print("PRE__PRELUDE_DONE 1");')
    meta = {
        **meta,
        "names": names,
        "weights": weights,
        "localizer": localizer,
        "gb_parameter_count": len(names),
        "lambda_variable_included": theorem_cut,
        "theorem_cut": theorem_cut,
        "rho_level4": rho_level4,
        "target_power": tk,
        "characteristic": ch,
        "Q_expr": Q_expr,
    }
    return "\n".join(lines), names, weights, meta


def extra_generators(pin_index: int) -> list[str]:
    return ["CSTP-1", f"q{pin_index}*q{pin_index}_inv-1"]


def run_singular_count(prelude: str, tag: str, timeout: int) -> dict[str, Any]:
    RUNS.mkdir(parents=True, exist_ok=True)
    cache = RUNS / f"{tag}.rowcount.json"
    script = RUNS / f"{tag}.count.sing"
    atomic_write(script, prelude + '\nprint("PRE__ROWS_FINAL "+string(size(ROWS)));\nquit;\n')
    t0 = time.time()
    cmd = ["stdbuf", "-oL", "-eL", "Singular", "--no-rc", "-q", str(script)]
    try:
        proc = __import__("subprocess").run(
            cmd, capture_output=True, text=True, timeout=timeout, check=False
        )
        stdout = proc.stdout
        stderr = proc.stderr
        timed_out = False
        returncode = proc.returncode
    except __import__("subprocess").TimeoutExpired as exc:
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
            markers[parts[0]] = parts[1] if len(parts) else ""
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
    b: int,
    *,
    pin_index: int,
    ch: int,
    tk: int,
    theorem_cut: bool,
    rho_level4: bool,
    count_timeout: int,
) -> tuple[SingularSystem | None, dict[str, Any], dict[str, Any]]:
    prelude, names, _weights, meta = strata_prelude(
        K,
        b,
        pin_index=pin_index,
        ch=ch,
        tk=tk,
        theorem_cut=theorem_cut,
        rho_level4=rho_level4,
    )
    info = run_singular_count(prelude, f"{tag}_p{ch}", count_timeout)
    if info["n"] is None:
        return None, info, meta
    generators = [f"ROWS[{idx}]" for idx in range(1, info["n"] + 1)]
    generators.extend(extra_generators(pin_index))
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
    b: int,
    *,
    pin_index: int = 0,
    chars: tuple[int, ...] = (0,),
    tk: int = 4,
    timeout: int = 900,
    count_timeout: int = 240,
    cores: int = 4,
    theorem_cut: bool = False,
    rho_level4: bool = True,
) -> dict[str, Any]:
    if cores < 1 or cores > 16:
        raise ValueError("cores must be between 1 and 16")
    systems: list[SingularSystem] = []
    counts: list[dict[str, Any]] = []
    metas: list[dict[str, Any]] = []
    for ch in chars:
        system, info, meta = build_system(
            tag,
            K,
            b,
            pin_index=pin_index,
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
        summary = {
            "tag": tag,
            "K": K,
            "b": b,
            "pin_index": pin_index,
            "verdict": "PRELUDE_FAILED",
            "counts": counts,
            "metadata": metas[0] if metas else {},
        }
        atomic_write(RUNS / tag / "summary.json", json.dumps(summary, indent=2, sort_keys=True) + "\n")
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
        policy=PromotionPolicy.exact_q(
            "k4ray beta-stratum dehomogenised/localised LEVEL-4 chart; exact Q only"
        ),
        config=cfg,
    )
    wall = round(time.time() - t0, 3)
    summary = {
        "tag": tag,
        "K": K,
        "b": b,
        "pin_index": pin_index,
        "chars": list(chars),
        "target": f"x^{tk}",
        "theorem_cut": theorem_cut,
        "rho_level4": rho_level4,
        "counts": counts,
        "metadata": metas[0],
        "extra_generators": extra_generators(pin_index),
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


def parse_chars(text: str) -> tuple[int, ...]:
    return tuple(int(piece) for piece in text.split(",") if piece != "")


def cover_indices(K: int, b: int) -> list[int]:
    nQ = stratum_metadata(K, b, 0)["nQ"]
    return list(range(nQ))


def tag_for(K: int, b: int, pin_index: int, *, theorem: bool, chs: str) -> str:
    kind = "FULL" if theorem else "LIGHT"
    return f"K{K}_B{b}_Q{pin_index}_{kind}_{chs}"


def summarize() -> dict[str, Any]:
    summaries: dict[str, Any] = {}
    for path in sorted(RUNS.glob("*/summary.json")):
        summaries[path.parent.name] = json.loads(path.read_text(encoding="utf-8"))
    atomic_write(HERE / "summary-all.json", json.dumps(summaries, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"summary_count": len(summaries), "tags": sorted(summaries)}, sort_keys=True))
    return summaries


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_meta = sub.add_parser("meta")
    p_meta.add_argument("K", type=int)
    p_meta.add_argument("b", type=int)
    p_meta.add_argument("--pin-index", type=int, default=0)

    p_census = sub.add_parser("census")

    p_count = sub.add_parser("count")
    p_count.add_argument("tag")
    p_count.add_argument("K", type=int)
    p_count.add_argument("b", type=int)
    p_count.add_argument("--pin-index", type=int, default=0)
    p_count.add_argument("--char", type=int, default=0)
    p_count.add_argument("--tk", type=int, default=4)
    p_count.add_argument("--timeout", type=int, default=240)
    p_count.add_argument("--theorem", action="store_true")
    p_count.add_argument("--no-rho-level4", action="store_true")

    p_run = sub.add_parser("run")
    p_run.add_argument("tag")
    p_run.add_argument("K", type=int)
    p_run.add_argument("b", type=int)
    p_run.add_argument("--pin-index", type=int, default=0)
    p_run.add_argument("--chars", default="0")
    p_run.add_argument("--tk", type=int, default=4)
    p_run.add_argument("--timeout", type=int, default=900)
    p_run.add_argument("--count-timeout", type=int, default=240)
    p_run.add_argument("--cores", type=int, default=4)
    p_run.add_argument("--theorem", action="store_true")
    p_run.add_argument("--no-rho-level4", action="store_true")

    p_cover = sub.add_parser("cover-run")
    p_cover.add_argument("K", type=int)
    p_cover.add_argument("b", type=int)
    p_cover.add_argument("--chars", default="0")
    p_cover.add_argument("--timeout", type=int, default=900)
    p_cover.add_argument("--count-timeout", type=int, default=240)
    p_cover.add_argument("--cores", type=int, default=4)
    p_cover.add_argument("--theorem", action="store_true")

    sub.add_parser("summarize")

    args = parser.parse_args()
    if args.cmd == "meta":
        print(json.dumps(stratum_metadata(args.K, args.b, args.pin_index), indent=2, sort_keys=True))
    elif args.cmd == "census":
        rows = []
        for K in (7, 8, 9):
            for b in range(bmin_of(K), 2 * K):
                meta0 = stratum_metadata(K, b, 0)
                rows.append(
                    {
                        "K": K,
                        "b": b,
                        "nQ": meta0["nQ"],
                        "h": meta0["h_parameter_count"],
                        "lower_beta": meta0["lower_beta_parameter_count"],
                        "geom_q0": meta0["geometric_parameter_count"],
                        "gb_q0": meta0["geometric_parameter_count"] + 1,
                        "covers": cover_indices(K, b),
                    }
                )
        print(json.dumps(rows, indent=2))
    elif args.cmd == "count":
        prelude, _names, _weights, meta = strata_prelude(
            args.K,
            args.b,
            pin_index=args.pin_index,
            ch=args.char,
            tk=args.tk,
            theorem_cut=args.theorem,
            rho_level4=not args.no_rho_level4,
        )
        info = run_singular_count(prelude, f"{args.tag}_p{args.char}", args.timeout)
        print(json.dumps({"metadata": meta, "count": info}, indent=2, sort_keys=True))
    elif args.cmd == "run":
        run_chart(
            args.tag,
            args.K,
            args.b,
            pin_index=args.pin_index,
            chars=parse_chars(args.chars),
            tk=args.tk,
            timeout=args.timeout,
            count_timeout=args.count_timeout,
            cores=args.cores,
            theorem_cut=args.theorem,
            rho_level4=not args.no_rho_level4,
        )
    elif args.cmd == "cover-run":
        chs = args.chars.replace(",", "p")
        outputs = []
        for pin in cover_indices(args.K, args.b):
            tag = tag_for(args.K, args.b, pin, theorem=args.theorem, chs=f"c{chs}")
            outputs.append(
                run_chart(
                    tag,
                    args.K,
                    args.b,
                    pin_index=pin,
                    chars=parse_chars(args.chars),
                    timeout=args.timeout,
                    count_timeout=args.count_timeout,
                    cores=args.cores,
                    theorem_cut=args.theorem,
                )
            )
        atomic_write(
            RUNS / f"COVER_K{args.K}_B{args.b}.json",
            json.dumps(outputs, indent=2, sort_keys=True) + "\n",
        )
    elif args.cmd == "summarize":
        summarize()


if __name__ == "__main__":
    main()
