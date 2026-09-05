#!/usr/bin/env python3
"""Reusable u_s >= 2 census kill sweep.

Pipeline (one class at a time):

    enumerate admissible Moh (1)-(13) skeletons
      -> Prop 6.3/6.4 descent
      -> classify split / unsplit
      -> size the FULL necessary chart (h-support included)
      -> emit via order_basis_full + builder_fix (or a registered joint/k4-ray
         engine when that is the validated necessary chart)
      -> extract generators
      -> solve with guided_gb (exact Q) and optional msolve screen
      -> typed per-class certificate JSON

A class is DEAD only if every fibre/stem is UNIT, the chart is a full
necessary over-approximation, and the unit is characteristic-zero (exact Q,
or three good primes plus a separate exact-Q confirm). A modular [1] is
never promoted. A NON-EMPTY chart with a point is not a Keller counterexample
unless J is a nonzero constant at that point and the point lifts.

FALLACY-v2: a tot-degree / support sub-slice UNIT is not a kill; matching
variable names are not a ring map; REPRESENTATIVE is not FULL_ACTUAL.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import time
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from fractions import Fraction as F
from math import floor, gcd
from pathlib import Path
from typing import Any, Iterable, Sequence


ROOT = Path(__file__).resolve().parents[2]
BOX = ROOT / "box"
LIB = BOX / "lib"
CHARTS = BOX / "moh14-charts-20260905"
ORDER = BOX / "orderbasis-20260903"
DEFAULT_DEST = BOX / "census-sweep-20260905"
FLEET_KEY = Path.home() / ".ssh" / "jc2-fleet"
WORKERS = ("172.30.0.7", "172.30.0.18", "172.30.0.28")
GOOD_PRIMES = (32003, 32009, 32027)
SSH_OPTS = (
    "-i", str(FLEET_KEY),
    "-o", "StrictHostKeyChecking=no",
    "-o", "BatchMode=yes",
    "-o", "ConnectTimeout=12",
)

for path in (str(BOX), str(LIB), str(CHARTS), str(ORDER),
             str(BOX / "mohprog-drivers-20260903")):
    if path not in sys.path:
        sys.path.insert(0, path)

import moh_skeleton_full as MS  # noqa: E402
import order_basis_full as OB  # noqa: E402
import sprime3_compiler as S3  # noqa: E402
from builder_fix import fix_text  # noqa: E402

import guided_gb as GG  # noqa: E402


# ---------------------------------------------------------------------------
# small utilities
# ---------------------------------------------------------------------------

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def atomic_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True, default=jdefault) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def jdefault(obj: Any) -> Any:
    if isinstance(obj, F):
        return str(obj.numerator) if obj.denominator == 1 else "%s/%s" % (
            obj.numerator, obj.denominator)
    if isinstance(obj, Path):
        return str(obj)
    if isinstance(obj, set):
        return sorted(obj)
    raise TypeError(type(obj))


def qstr(value: F | int | None) -> str | None:
    if value is None:
        return None
    if isinstance(value, F):
        return str(value.numerator) if value.denominator == 1 else "%s/%s" % (
            value.numerator, value.denominator)
    return str(value)


def as_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, F):
        if value.denominator != 1:
            return None
        return value.numerator
    try:
        iv = int(value)
    except (TypeError, ValueError):
        return None
    if value != iv:
        return None
    return iv


def int_dict(mapping: dict) -> dict[int, int] | None:
    out: dict[int, int] = {}
    for key, value in mapping.items():
        iv = as_int(value)
        if iv is None:
            return None
        out[int(key)] = iv
    return out


def safe_name(text: str) -> str:
    out = re.sub(r"[^A-Za-z0-9_]+", "_", text).strip("_")
    return out or "x"


def env_single_thread() -> dict[str, str]:
    env = os.environ.copy()
    for key in (
        "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
        "NUMEXPR_NUM_THREADS", "FLINT_NUM_THREADS",
    ):
        env[key] = "1"
    return env


# ---------------------------------------------------------------------------
# descent, split window, classification
# ---------------------------------------------------------------------------

def u_s_of(skel: MS.Skel) -> int:
    return skel.d[skel.s] - skel.V[skel.s]


def v_s_of(skel: MS.Skel) -> int:
    return skel.V[skel.s]


def descend(skel: MS.Skel) -> dict | None:
    """Moh Prop 6.3/6.4.  ell = v_s - u_s - 1 (ERRATUM 17(dddddd))."""
    ds, vs, s = skel.d[skel.s], skel.V[skel.s], skel.s
    us = ds - vs
    if us < 1 or vs < 1:
        return None
    ell = vs - us - 1
    if ell < 0:
        return None
    if (skel.n * us) % ds or (skel.m * us) % ds:
        return None
    n2, m2 = skel.n * us // ds, skel.m * us // ds
    s2 = s - 1
    if s2 < 1:
        return None
    M2: dict[int, Any] = {}
    ok_int = True
    for i in range(1, s2 + 1):
        num = skel.M[i] * us
        if num % ds:
            ok_int = False
            M2[i] = F(num, ds)
        else:
            M2[i] = num // ds
    d2: dict[int, Any] = {}
    for i in range(1, s2 + 2):
        num = skel.d[i] * us
        if num % ds:
            ok_int = False
            d2[i] = F(num, ds)
        else:
            d2[i] = num // ds
    V2 = {i: skel.V[i] for i in range(2, s2 + 1)}
    V2[s2 + 1] = d2[s2 + 1]
    return dict(
        n=n2, m=m2, s=s2, M=M2, d=d2, V=V2, ell=ell,
        us=us, vs=vs, ds=ds, ok_int=ok_int,
        src_n=skel.n, src_m=skel.m, src_s=s,
        src_M=[skel.M[i] for i in range(2, s + 1)],
        src_V={i: skel.V[i] for i in range(2, s + 1)},
        src_d={i: skel.d[i] for i in range(1, s + 2)},
    )


def split_window(us: int, vs: int) -> list[F]:
    """Candidate principal-minor orders: 1 < a/b < v_s/u_s, 1 <= b <= u_s.

    The bound den(delta) <= u_s is Xu's working bound, not a theorem
    (h1-nonres).  The window is a finite candidate screen.
    """
    if us < 1 or vs < 1:
        return []
    cap = F(vs, us)
    out: set[F] = set()
    for den in range(1, us + 1):
        for num in range(den + 1, den * vs + 1):
            val = F(num, den)
            if 1 < val < cap:
                out.add(val)
    return sorted(out)


def genuine_partitions(us: int) -> list[tuple[int, ...]]:
    """Partitions of u_s with at least two parts (a one-part [u_s] is not a split)."""
    out: list[tuple[int, ...]] = []

    def rec(remaining: int, max_part: int, acc: list[int]) -> None:
        if remaining == 0:
            if len(acc) >= 2:
                out.append(tuple(acc))
            return
        for part in range(min(max_part, remaining), 0, -1):
            acc.append(part)
            rec(remaining - part, part, acc)
            acc.pop()

    rec(us, us, [])
    return out


def classify_row(skel: MS.Skel, descended: dict) -> dict:
    us, vs = descended["us"], descended["vs"]
    window = split_window(us, vs)
    parts = genuine_partitions(us)
    if window and parts:
        kind = "split"
    elif window:
        kind = "unsplit"  # arithmetic orders, no genuine multi-packet partition
    else:
        kind = "unsplit"
    # A nonempty window does not discharge the no-split alternative: the
    # unsplit fibre is the Prop 6.3 descent, and a class kill is conjunctive
    # over every stem (split fibres AND the unsplit descent).
    if window and parts:
        kind = "mixed"
    return dict(
        kind=kind,
        u_s=us, v_s=vs, d_s=descended["ds"], ell=descended["ell"],
        window=[qstr(v) for v in window],
        genuine_partitions=parts,
        n_prime=descended["n"], m_prime=descended["m"],
        s_prime=descended["s"],
    )


# ---------------------------------------------------------------------------
# chart-size estimate (full necessary D1 + optional outer-disc completion)
# ---------------------------------------------------------------------------

def child_closed_form(descended: dict) -> dict | None:
    M = int_dict(descended["M"])
    d = int_dict(descended["d"])
    V = int_dict(descended["V"])
    if M is None or d is None or V is None:
        return None
    datum = dict(
        n=int(descended["n"]), m=int(descended["m"]), s=int(descended["s"]),
        M=M, d=d, V=V, ell=int(descended["ell"]), us=int(descended["us"]),
        dropped=0,
    )
    dropped = S3.drop_p174(datum)
    phi = S3.phi_eff(dropped)
    if phi is None:
        return None
    try:
        closed = S3.closed_form_sprime(dropped, phi)
    except Exception:
        return None
    closed["dropped"] = dropped
    closed["phi"] = phi
    return closed


def inventory_counts(closed: dict) -> dict:
    """Return raw-D1 and source-complete unknown counts after gauges."""
    raw_h = S3.coeff_inventory_necessary(closed, 1)
    raw_a = {i: S3.coeff_inventory_necessary(closed, i)
             for i in range(1, closed["e"] + 1)}
    raw_b = {i: S3.coeff_inventory_necessary(closed, i)
             for i in range(2, closed["q"] + 1)}
    am, bm, _, _, _ = S3.apply_gauges(closed["e"], closed["q"], raw_a, raw_b)
    nunk_raw = len(raw_h) + sum(len(v) for v in am.values()) + sum(
        len(v) for v in bm.values()) + 1
    nunk_sc = None
    sc_ok = closed["delta_s"] < 0
    if sc_ok:
        try:
            sc_h = S3.coeff_inventory_source_complete(closed, 1)
            sc_a = {i: S3.coeff_inventory_source_complete(closed, i)
                    for i in range(1, closed["e"] + 1)}
            sc_b = {i: S3.coeff_inventory_source_complete(closed, i)
                    for i in range(2, closed["q"] + 1)}
            am2, bm2, _, _, _ = S3.apply_gauges(
                closed["e"], closed["q"], sc_a, sc_b)
            nunk_sc = (len(sc_h) + sum(len(v) for v in am2.values())
                       + sum(len(v) for v in bm2.values()) + 1)
        except (ValueError, OverflowError):
            sc_ok = False
            nunk_sc = None
    k4ray = (
        closed["ell"] == 4
        and closed["u"] == 1
        and closed["K"] >= 7
        and closed["e"] == 3
        and closed["q"] == 2
    )
    return dict(
        nunk_raw=nunk_raw,
        nunk_source_complete=nunk_sc,
        source_complete_ok=sc_ok,
        k4ray_shape=k4ray,
        K=closed["K"], e=closed["e"], q=closed["q"],
        u=closed["u"], V2=closed["V2"], ell=closed["ell"],
        B_safe=qstr(closed["B_safe"]),
        delta1=qstr(closed["delta1"]),
        delta_s=qstr(closed["delta_s"]),
        B_nonneg=closed["B"] >= 0,
        s_prime=closed["s"],
        two_point=bool(closed["two_point"]),
    )


def solvable_unknowns(counts: dict, kind: str) -> tuple[int, str]:
    """Size used to SORT the sweep: the chart we will actually try to solve.

    Joint incidence of the D=108 delta=3 type is 4 unknowns; the validated
    k=4-ray pin+lower-band charts are 36 unknowns; a source-complete order
    chart is used only when it is the full necessary over-approximation and
    small enough to finish.
    """
    if kind in {"split", "mixed"}:
        # joint is the right chart; order-only is a necessary subsystem.
        # Without a per-row incidence compiler the joint size is unknown and
        # is treated as at least the order size (never smaller).
        nunk = counts.get("nunk_source_complete") or counts["nunk_raw"]
        return int(nunk), "joint_at_least_order"
    if counts.get("k4ray_shape"):
        return 36, "k4ray_pin_lower_band"
    if counts.get("nunk_source_complete"):
        return int(counts["nunk_source_complete"]), "order_source_complete"
    return int(counts["nunk_raw"]), "order_raw_D1"


# ---------------------------------------------------------------------------
# enumeration
# ---------------------------------------------------------------------------

def class_key(descended: dict) -> tuple:
    M = int_dict(descended["M"]) or {}
    V = int_dict(descended["V"]) or {}
    middles = tuple(M[i] for i in range(2, descended["s"] + 1) if i in M)
    fibre = tuple(V[i] for i in range(2, descended["s"] + 1) if i in V)
    return (
        int(descended["n"]), int(descended["m"]), middles,
        int(descended["ell"]), int(descended["s"]), fibre,
    )


def class_id_of(key: tuple) -> str:
    n, m, middles, ell, s, fibre = key
    mtag = "_".join(("m%d" % abs(x) if x < 0 else str(x) for x in middles)) or "none"
    vtag = "_".join(str(x) for x in fibre) or "none"
    return "C_n%dm%d_M%s_ell%d_s%d_V%s" % (n, m, mtag, ell, s, vtag)


def four_int_key(descended: dict) -> tuple | None:
    V = int_dict(descended["V"])
    if V is None or 2 not in V:
        return None
    return (int(descended["n"]), int(descended["m"]),
            int(descended["ell"]), int(V[2]))


def coarse_key(descended: dict) -> tuple:
    return (int(descended["n"]), int(descended["m"]), int(descended["ell"]))


def enumerate_us_ge2(
    nmin: int = 16,
    nmax: int = 200,
    kmin: int = 16,
    full: bool = True,
) -> dict:
    """Enumerate (1)-(13) rows with u_s >= 2 and group descended classes."""
    started = time.time()
    rows: list[dict] = []
    n_raw = 0
    n_us = 0
    skipped = 0
    for n in range(max(nmin, 3 * kmin), nmax + 1):
        t0 = time.time()
        degree_rows = 0
        for m, Ms, V in MS.census(n, Kmin=kmin, full=full):
            n_raw += 1
            skel = MS.Skel(n, m, list(Ms), V)
            if u_s_of(skel) < 2:
                continue
            n_us += 1
            descended = descend(skel)
            if descended is None:
                skipped += 1
                continue
            cls = classify_row(skel, descended)
            rec = dict(
                src_n=n, src_m=m, src_M=list(Ms),
                src_V={i: V[i] for i in sorted(V)},
                src_s=skel.s, src_d=skel.d, src_K=skel.K,
                **cls, **{k: descended[k] for k in (
                    "M", "d", "V", "ok_int", "ds", "us", "vs")},
            )
            rec["class_key"] = class_key(descended)
            rec["four_int_key"] = four_int_key(descended)
            rec["coarse_key"] = coarse_key(descended)
            rec["class_id"] = class_id_of(rec["class_key"])
            rows.append(rec)
            degree_rows += 1
        if n % 10 == 0 or degree_rows:
            print("  n=%d  raw_cum=%d  us>=2_cum=%d  degree_us=%d  [%.1fs]"
                  % (n, n_raw, n_us, degree_rows, time.time() - t0),
                  flush=True)
    classes: dict[tuple, list[dict]] = defaultdict(list)
    for rec in rows:
        classes[rec["class_key"]].append(rec)

    sized = []
    for key, members in classes.items():
        representative = members[0]
        closed = None
        counts = None
        reason = None
        if not representative["ok_int"]:
            reason = "descended_M_not_integer"
        else:
            closed = child_closed_form(dict(
                n=representative["n_prime"], m=representative["m_prime"],
                s=representative["s_prime"], M=representative["M"],
                d=representative["d"], V=representative["V"],
                ell=representative["ell"], us=representative["u_s"],
            ))
            if closed is None:
                reason = "closed_form_failed"
            elif closed["B"] >= 0:
                reason = "B_safe_nonneg"
                counts = inventory_counts(closed)
            else:
                counts = inventory_counts(closed)
        kinds = sorted(set(m["kind"] for m in members))
        kind = kinds[0] if len(kinds) == 1 else "mixed"
        if counts is None:
            nunk, engine = 10 ** 9, "unsizeable"
        else:
            nunk, engine = solvable_unknowns(counts, kind)
        sized.append(dict(
            class_id=class_id_of(key),
            class_key=[list(x) if isinstance(x, tuple) else x for x in key],
            n_prime=key[0], m_prime=key[1], M_prime=list(key[2]),
            ell=key[3], s_prime=key[4], V_prime=list(key[5]),
            fibre_size=len(members),
            kind=kind,
            kinds=kinds,
            nunk=nunk,
            engine=engine,
            counts=counts,
            skip_reason=reason,
            B_safe=None if counts is None else counts.get("B_safe"),
            K=None if counts is None else counts.get("K"),
            sources=[dict(
                n=m["src_n"], m=m["src_m"], M=m["src_M"], V=m["src_V"],
                u_s=m["u_s"], v_s=m["v_s"], window=m["window"],
                kind=m["kind"],
            ) for m in members],
            four_int_key=representative["four_int_key"],
            coarse_key=list(representative["coarse_key"]),
        ))
    sized.sort(key=lambda c: (c["nunk"], c["n_prime"], c["m_prime"], c["ell"]))

    four_keys = {r["four_int_key"] for r in rows if r["four_int_key"]}
    coarse = {r["coarse_key"] for r in rows}
    elapsed = round(time.time() - started, 3)
    summary = dict(
        nmin=nmin, nmax=nmax, kmin=kmin, full=full,
        n_raw_1_13=n_raw, n_us_ge2=n_us, n_descended_rows=len(rows),
        n_skipped_no_descent=skipped,
        n_descended_classes=len(classes),
        n_coarse_n_m_ell=len(coarse),
        n_four_int_keys=len(four_keys),
        n_sizeable=sum(1 for c in sized if c["skip_reason"] is None),
        n_k4ray_shape=sum(1 for c in sized
                          if (c.get("counts") or {}).get("k4ray_shape")),
        n_split_or_mixed=sum(1 for c in sized if c["kind"] in ("split", "mixed")),
        n_unsplit=sum(1 for c in sized if c["kind"] == "unsplit"),
        elapsed_seconds=elapsed,
    )
    print("enumerate: raw %d  u_s>=2 %d  classes %d  4-int keys %d  "
          "coarse (n',m',ell) %d  [%.1fs]"
          % (n_raw, n_us, len(classes), len(four_keys), len(coarse), elapsed),
          flush=True)
    return dict(summary=summary, classes=sized, rows=rows)


def sharpen_four_int_from_xufloor(xufloor: Path) -> dict:
    """Astra-corrected 296 xu_ok_candidate records -> 132 (n',m',ell,V2') keys."""
    payload = json.loads(xufloor.read_text(encoding="utf-8"))
    records = payload["rows"]
    cand = [r for r in records
            if r.get("phase") == "us_gt_1" and r.get("xu_ok_candidate")]
    keys = set()
    unmatched = 0
    for rec in cand:
        V = {int(k): int(v) for k, v in rec["V"].items()}
        skel = MS.Skel(int(rec["n"]), int(rec["m"]), list(rec["M"]), V)
        descended = descend(skel)
        if descended is None:
            unmatched += 1
            continue
        key = four_int_key(descended)
        if key is None:
            unmatched += 1
            continue
        keys.add(key)
    return dict(
        n_us_gt_1=sum(1 for r in records if r.get("phase") == "us_gt_1"),
        n_xu_ok_candidate=len(cand),
        n_four_int_keys=len(keys),
        unmatched=unmatched,
        keys=sorted(keys),
    )


# ---------------------------------------------------------------------------
# emit (order chart via builder_fix) and extract
# ---------------------------------------------------------------------------

def emit_order_class(entry: dict, dest: Path, support: str = "source-complete") -> dict:
    """Emit the full necessary order chart for one descended class.

    Uses sprime3_compiler.build_spec (free leading y^K, B_safe, Theorem-1.2
    inventory) and builder_fix on every builder.  Union of V'-fibres is the
    class chart; each fibre is also emitted so a class kill stays conjunctive.
    """
    cid = entry["class_id"]
    dest = dest.resolve()
    class_dir = dest / "classes" / cid
    class_dir.mkdir(parents=True, exist_ok=True)
    n, m = entry["n_prime"], entry["m_prime"]
    ell, s = entry["ell"], entry["s_prime"]
    stems = []
    closed_forms = []
    for source in entry["sources"]:
        V = {int(k): int(v) for k, v in source["V"].items()}
        skel = MS.Skel(source["n"], source["m"], list(source["M"]), V)
        descended = descend(skel)
        if descended is None or not descended["ok_int"]:
            continue
        closed = child_closed_form(descended)
        if closed is None or closed["B"] >= 0:
            continue
        closed_forms.append((source, descended, closed))
    if not closed_forms:
        return dict(ok=False, reason="no_emittable_fibre", class_id=cid)

    def inventories(closed: dict, how: str):
        closed = dict(closed)
        if how == "source-complete" and closed["delta_s"] < 0:
            closed["support_basis"] = (
                "raw_D1_union_trace_centered_outer_disc_v1")
            inv = S3.coeff_inventory_source_complete
        else:
            closed["support_basis"] = "raw_D1_centered_hypothesis_required"
            inv = S3.coeff_inventory_necessary
        h = inv(closed, 1)
        alpha = {i: inv(closed, i) for i in range(1, closed["e"] + 1)}
        beta = {i: inv(closed, i) for i in range(2, closed["q"] + 1)}
        return closed, h, alpha, beta

    fibre_payloads = []
    for source, descended, closed in closed_forms:
        used, h, alpha, beta = inventories(closed, support)
        vtag = "_".join(str(descended["V"][i]) for i in range(2, descended["s"] + 1))
        stem = "%s_V%s" % (cid, vtag)
        row = OB.Row(
            key=stem, label="%s V'=%s" % (cid, vtag),
            n=n, m=m, M2=int(descended["M"][descended["s"]]),
            V2=int(used["V2"]), k=ell,
        )
        spec = S3.build_spec(used, h, alpha, beta, row, "freelead")
        payload = S3.write_builder(spec, stem, class_dir)
        S3.write_fleet_job(class_dir, stem, payload, cid)
        fibre_payloads.append((stem, payload, used, h, alpha, beta, source))
        stems.append(stem)

    # class union of fibre inventories
    Hu, Au, Bu = set(), defaultdict(set), defaultdict(set)
    for _stem, _pay, used, h, alpha, beta, _src in fibre_payloads:
        Hu.update(h)
        for i, mons in alpha.items():
            Au[i].update(mons)
        for i, mons in beta.items():
            Bu[i].update(mons)

    def sord(ms):
        return sorted(ms, key=lambda t: (-t[1], t[0]))

    hU, aU, bU = sord(Hu), {i: sord(Au[i]) for i in sorted(Au)}, {
        i: sord(Bu[i]) for i in sorted(Bu)}
    C_dom = min((p[2] for p in fibre_payloads), key=lambda C: C["B_safe"])
    C_union = dict(C_dom)
    C_union["u"] = max(p[2]["u"] for p in fibre_payloads)
    union_stem = cid + "_union"
    row_u = OB.Row(
        key=union_stem, label="%s union" % cid,
        n=n, m=m, M2=int(entry["M_prime"][-1]) if entry["M_prime"] else n - 2,
        V2=min(p[2]["V2"] for p in fibre_payloads), k=ell,
    )
    spec_u = S3.build_spec(C_union, hU, aU, bU, row_u, "freelead_union")
    pay_u = S3.write_builder(spec_u, union_stem, class_dir)
    S3.write_fleet_job(class_dir, union_stem, pay_u, cid)

    class_json = dict(
        class_id=cid,
        n_prime=n, m_prime=m, M_prime=entry["M_prime"],
        ell=ell, s_prime=s, kind=entry["kind"],
        fibre_size=len(fibre_payloads),
        stems=stems,
        union_stem=union_stem,
        union_parameter_count=pay_u["parameter_count"],
        support=support,
        chart="census_sweep_order_builder_fix_v1",
        builder_fix=True,
        fallacy_v2=(
            "necessary over-approx: free leading form + B_safe + full "
            "Theorem-1.2 D1 inventory; source-complete adjoins the "
            "trace-centered outer-disc support. A class dies only if every "
            "fibre is UNIT. Union empty => every fibre empty; the converse "
            "does not hold."
        ),
        rows=[dict(
            stem=stem, parameter_count=pay["parameter_count"],
            builder=pay["builder"], source=source,
        ) for stem, pay, _c, _h, _a, _b, source in fibre_payloads],
        engine=entry.get("engine"),
        nunk_sort=entry.get("nunk"),
    )
    (class_dir / "class.json").write_text(
        json.dumps(class_json, indent=2, sort_keys=True, default=jdefault) + "\n",
        encoding="utf-8")
    return dict(ok=True, class_id=cid, dest=str(class_dir),
                union_unknowns=pay_u["parameter_count"],
                fibre_size=len(fibre_payloads), stems=stems,
                union_stem=union_stem)


def extract_stem(class_dir: Path, stem: str, timeout: int) -> dict:
    """Run the fixed native builder in the class directory."""
    builder = class_dir / "builders" / ("%s_builder.sing" % stem)
    rows = class_dir / "rows" / ("%s_rows.tsv" % stem)
    jobs = class_dir / "jobs"
    jobs.mkdir(exist_ok=True)
    log = jobs / ("%s_extract.log" % stem)
    started = time.monotonic()
    with log.open("w", encoding="utf-8") as out:
        proc = subprocess.Popen(
            ["Singular", "--cpus=1", "--threads=1", "--flint-threads=1",
             "-q", "--no-rc", str(builder.relative_to(class_dir))],
            cwd=class_dir, stdout=out, stderr=subprocess.STDOUT,
            env=env_single_thread(), start_new_session=True,
        )
        timed_out = False
        try:
            rc = proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(proc.pid, signal.SIGTERM)
            try:
                rc = proc.wait(timeout=15)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                rc = proc.wait()
    text = log.read_text(encoding="utf-8", errors="replace")
    declared = None
    match = re.search(r"NATIVE_DONE equations=(\d+)", text)
    if match:
        declared = int(match.group(1))
    n_rows = 0
    if rows.is_file() and rows.stat().st_size > 42:
        with rows.open("rb") as handle:
            header = handle.readline()
            if header != b"source_index|h_power|x_power|y_power|expr\n":
                return dict(ok=False, reason="bad_header", stem=stem)
            n_rows = sum(1 for line in handle if line.strip())
    ok = (rc == 0 and not timed_out and declared is not None
          and declared == n_rows and n_rows > 0)
    return dict(
        ok=ok, stem=stem, timed_out=timed_out, returncode=rc,
        declared_equations=declared, rows=n_rows,
        wall_seconds=round(time.monotonic() - started, 3),
        log=str(log),
        lead_h_gate=("NATIVE_GATE lead_h_is_yK=1" in text),
        log_tail=text[-800:],
    )


# ---------------------------------------------------------------------------
# solve: guided_gb exact Q, optional modular screen, optional msolve
# ---------------------------------------------------------------------------

GG_UNIT_RE = re.compile(r"^GG__UNIT main (\d+)\s*$")
GG_DIM_RE = re.compile(r"^GG__DIM main (-?\d+|NONTERMINATING)\s*$")
GG_NF1_RE = re.compile(r"^GG__NF1_SIZE main (\d+)\s*$")
GG_BASIS_RE = re.compile(r"^GG__BASIS_SIZE main (\d+)\s*$")
GG_ACCEPT_RE = re.compile(r"^GG__ACCEPT main (\d+)\s*$")


def parse_gg_stdout(stdout: str) -> dict:
    out = dict(unit=None, dimension=None, nf1_size=None,
               basis_size=None, accepted=None)
    for line in stdout.splitlines():
        line = line.strip()
        m = GG_UNIT_RE.match(line)
        if m:
            out["unit"] = m.group(1) == "1"
        m = GG_DIM_RE.match(line)
        if m:
            tok = m.group(1)
            out["dimension"] = None if tok == "NONTERMINATING" else int(tok)
        m = GG_NF1_RE.match(line)
        if m:
            out["nf1_size"] = int(m.group(1))
        m = GG_BASIS_RE.match(line)
        if m:
            out["basis_size"] = int(m.group(1))
        m = GG_ACCEPT_RE.match(line)
        if m:
            out["accepted"] = m.group(1) == "1"
    return out


def parse_legacy_stdout(stdout: str) -> dict:
    """Parsers for the two control scripts (D=108 incidence, (99,66) stage-4)."""
    unit = None
    dimension = None
    basis_size = None
    if "MAIN_NF1" in stdout:
        lines = stdout.splitlines()
        for i, line in enumerate(lines):
            if line.strip() == "MAIN_NF1" and i + 1 < len(lines):
                unit = lines[i + 1].strip() == "0"
            if line.strip() == "MAIN_DIM" and i + 1 < len(lines):
                try:
                    dimension = int(lines[i + 1].strip())
                except ValueError:
                    pass
            if line.strip() == "MAIN_SIZE" and i + 1 < len(lines):
                try:
                    basis_size = int(lines[i + 1].strip())
                except ValueError:
                    pass
    if "BEGIN_DIM" in stdout:
        m = re.search(r"BEGIN_DIM\s*(-?\d+)\s*END_DIM", stdout, re.S)
        if m:
            dimension = int(m.group(1))
        m = re.search(r"BEGIN_GB\s*(.*?)\s*END_GB", stdout, re.S)
        if m:
            body = m.group(1).strip()
            unit = body in {"1", "_[1]=1", "[1]"} or body.endswith("=1") and "1" in body
            if "[1]:" in body or body == "1" or re.search(r"^1$", body, re.M):
                unit = True
                basis_size = 1
    if "reduce(1" in stdout and dimension == -1:
        unit = True
    return dict(unit=unit, dimension=dimension, basis_size=basis_size,
                accepted=bool(unit), nf1_size=0 if unit else None)


def run_singular(
    script: Path,
    output_prefix: Path,
    timeout: int,
    cwd: Path | None = None,
) -> dict:
    output_prefix.parent.mkdir(parents=True, exist_ok=True)
    stdout_path = output_prefix.with_suffix(".out")
    stderr_path = output_prefix.with_suffix(".err")
    cmd = [
        "stdbuf", "-oL", "-eL", "Singular",
        "--cpus=1", "--threads=1", "--flint-threads=1",
        "--no-rc", "-q", str(script),
    ]
    started = time.monotonic()
    timed_out = False
    with stdout_path.open("w", encoding="utf-8") as out, \
            stderr_path.open("w", encoding="utf-8") as err:
        proc = subprocess.Popen(
            cmd, stdout=out, stderr=err, cwd=str(cwd or ROOT),
            env=env_single_thread(), start_new_session=True,
        )
        try:
            rc = proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(proc.pid, signal.SIGTERM)
            try:
                rc = proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                rc = proc.wait()
    stdout = stdout_path.read_text(encoding="utf-8", errors="replace")
    parsed = parse_gg_stdout(stdout)
    if parsed["unit"] is None:
        parsed = {**parsed, **{k: v for k, v in parse_legacy_stdout(stdout).items()
                               if v is not None}}
    return dict(
        returncode=rc, timed_out=timed_out,
        elapsed_seconds=round(time.monotonic() - started, 3),
        stdout=str(stdout_path), stderr=str(stderr_path),
        script=str(script),
        script_sha256=sha256_file(script),
        stdout_sha256=sha256_file(stdout_path),
        stderr_sha256=sha256_file(stderr_path),
        **parsed,
    )


def solve_rows_guided(
    class_dir: Path,
    stem: str,
    timeout: int,
    characteristic: int = 0,
) -> dict:
    meta_path = class_dir / "meta" / ("%s.json" % stem)
    payload = json.loads(meta_path.read_text(encoding="utf-8"))
    rows_path = ROOT / payload["rows_path"]
    if not rows_path.is_file():
        rows_path = class_dir / "rows" / ("%s_rows.tsv" % stem)
    rows = OB.read_rows(rows_path)
    if not rows:
        return dict(ok=False, reason="no_rows", stem=stem)
    variables = list(payload["variables"]) + ["T"]
    char_token = "0" if characteristic == 0 else str(characteristic)
    prelude = "\n".join([
        "// generated by box/lib/census_sweep.py",
        "ring R=%s,(%s),dp;" % (char_token, ",".join(variables)),
        "option(redSB);",
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); } '
        'else { print("CONTROL_RING_FAIL"); }',
        "ideal CE=c,T*c-1;",
        "ideal GE=std(CE);",
        'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } '
        'else { print("CONTROL_EMPTY_FAIL"); }',
        "ideal CN=c-1,T*c-1;",
        "ideal GN=std(CN);",
        'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } '
        'else { print("CONTROL_NONEMPTY_FAIL"); }',
    ]) + "\n"
    generators = [row["expr"] for row in rows] + ["T*c-1"]
    system = GG.SingularSystem(
        name="%s_p%s" % (stem, char_token),
        prelude=prelude,
        generators=tuple(generators),
        characteristic=characteristic,
        variables=tuple(variables),
        homogeneous=False,
        metadata=dict(stem=stem, equations=len(rows),
                      unknowns=payload["parameter_count"]),
    )
    jobs = class_dir / "jobs"
    result = GG.guided_groebner(
        system,
        policy=GG.PromotionPolicy.exact_q(
            "census_sweep: modular units are not promoted"),
        config=GG.RunConfig(
            jobs, timeout_seconds=timeout, total_cores=1,
            max_parallel_jobs=1, run_perturbed_control=False,
        ),
    )
    run = result.certificate["runs"][0]
    main = run["main"]
    unit = bool(main.get("unit")) and characteristic == 0
    verdict = "TIMEOUT" if run.get("timed_out") else (
        "UNIT" if unit else (
            "NON_EMPTY" if main.get("dimension") is not None
            and main.get("dimension") >= 0 and not main.get("unit")
            else "OPEN"
        )
    )
    if run.get("timed_out"):
        verdict = "TIMEOUT"
    elif characteristic == 0 and main.get("unit") and main.get("dimension") == -1:
        verdict = "UNIT"
    elif characteristic != 0 and main.get("unit"):
        verdict = "MODULAR_UNIT_NOT_PROMOTED"
    elif main.get("dimension") is not None and main.get("dimension") >= 0:
        verdict = "NON_EMPTY"
    return dict(
        ok=True, stem=stem, engine="guided_gb",
        characteristic=characteristic,
        verdict=verdict,
        guided_verdict=result.verdict.value,
        unit=bool(main.get("unit")),
        dimension=main.get("dimension"),
        basis_size=main.get("basis_size"),
        nf_all_zero=main.get("nf_all_zero"),
        accepted=main.get("accepted"),
        timed_out=run.get("timed_out"),
        elapsed_seconds=run.get("elapsed_seconds"),
        equations=len(rows),
        unknowns=payload.get("parameter_count"),
        script=run.get("script"),
        stdout=run.get("stdout"),
        script_sha256=run.get("script_sha256"),
        stdout_sha256=run.get("stdout_sha256"),
        promotion="EXACT_Q" if characteristic == 0 else "NONE",
    )


def emit_msolve_file(
    variables: Sequence[str],
    polynomials: Sequence[str],
    characteristic: int,
    path: Path,
) -> Path:
    """Minimal msolve text format (same envelope as the D=108 control .ms)."""
    if any("_" in v for v in variables):
        raise ValueError("msolve identifiers cannot contain underscores")
    path.parent.mkdir(parents=True, exist_ok=True)
    body = ",".join(variables) + "\n" + str(characteristic) + "\n"
    body += ",\n".join(polynomials) + "\n"
    path.write_text(body, encoding="utf-8")
    return path


def parse_msolve_g2(out_text: str, characteristic: int) -> dict:
    compact = re.sub(r"\s+", "", out_text)
    unit_signal = "[1]" in compact or compact.endswith(",1]") 
    # a lone [1] reduced basis
    lone = bool(re.search(r"\[1\]\s*$", out_text.strip())) or compact in {
        "[1]", "[[1]]", "#Grobnerbasis(groebner-basis):[1]",
    }
    if re.search(r"\[\[1\]\]", compact) or re.search(r":\[1\]\s*$", compact):
        lone = True
    if characteristic == 0:
        status = "UNIT_SIGNAL_MODULAR_ONLY" if (unit_signal or lone) else "NONUNIT_OR_INCONCLUSIVE"
    else:
        status = "UNIT" if (unit_signal or lone) else "NONUNIT_OR_INCONCLUSIVE"
    return dict(status=status, unit_signal=bool(unit_signal or lone),
                characteristic=characteristic,
                promotion="NONE")


def solve_msolve(
    ms_path: Path,
    timeout: int,
    threads: int = 1,
) -> dict:
    out_path = ms_path.with_suffix(".g2.out")
    err_path = ms_path.with_suffix(".g2.stderr")
    msolve = shutil.which("msolve")
    if msolve is None:
        return dict(ok=False, reason="msolve_not_installed")
    started = time.monotonic()
    with out_path.open("w", encoding="utf-8") as out, \
            err_path.open("w", encoding="utf-8") as err:
        proc = subprocess.Popen(
            ["timeout", str(timeout), msolve, "-g", "2", "-t", str(threads),
             "-f", str(ms_path), "-o", str(out_path)],
            stdout=err, stderr=subprocess.STDOUT,
            env=env_single_thread(), start_new_session=True,
        )
        try:
            rc = proc.wait(timeout=timeout + 5)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            rc = proc.wait()
    text = out_path.read_text(encoding="utf-8", errors="replace") if out_path.exists() else ""
    # characteristic from the .ms second line
    try:
        char = int(ms_path.read_text(encoding="utf-8").splitlines()[1])
    except (IndexError, ValueError):
        char = 0
    parsed = parse_msolve_g2(text, char)
    return dict(
        ok=True, engine="msolve", returncode=rc,
        elapsed_seconds=round(time.monotonic() - started, 3),
        output=str(out_path), stderr=str(err_path),
        **parsed,
    )


# ---------------------------------------------------------------------------
# certificates
# ---------------------------------------------------------------------------

def stem_verdict(result: dict) -> str:
    if result.get("timed_out"):
        return "TIMEOUT"
    if result.get("verdict"):
        return result["verdict"]
    if result.get("unit") and result.get("characteristic") == 0:
        return "UNIT"
    if result.get("dimension") is not None and result["dimension"] >= 0:
        return "NON_EMPTY"
    return "OPEN"


def class_verdict(stem_results: list[dict]) -> str:
    """Conjunctive: every stem UNIT => DEAD; any NON_EMPTY => NON_EMPTY;
    any TIMEOUT without a NON_EMPTY => TIMEOUT; else OPEN."""
    if not stem_results:
        return "OPEN"
    labels = [stem_verdict(r) for r in stem_results]
    if any(v == "NON_EMPTY" for v in labels):
        return "NON_EMPTY"
    if all(v == "UNIT" for v in labels):
        return "DEAD"
    if any(v == "TIMEOUT" for v in labels):
        return "TIMEOUT"
    return "OPEN"


def write_certificate(path: Path, payload: dict) -> dict:
    payload.setdefault("schema", "census-sweep-class-certificate-v1")
    payload.setdefault("fallacy_v2", (
        "A class kill needs the FULL necessary chart (h-support included; "
        "for u_s>=2 split rows the joint chart: order + minor-incidence + "
        "pole + Jacobian) AND every stem UNIT AND exact-Q confirm. Modular "
        "[1] is not a kill. A surviving point is not a counterexample unless "
        "J is a nonzero constant and the point lifts."
    ))
    atomic_json(path, payload)
    payload["certificate_path"] = str(path)
    payload["certificate_sha256"] = sha256_file(path)
    return payload


# ---------------------------------------------------------------------------
# known engines (validated necessary charts, replayed through this sweep)
# ---------------------------------------------------------------------------

KNOWN = {
    "D108_delta3": dict(
        label="D=108 delta=3 common-h3 minor incidence",
        kind="split",
        nunk=4,
        script=CHARTS.parent / "g108band-20260903/runs/delta3/stage0/death_replay.sing",
        expected="UNIT",
        chart="joint_order_incidence_pole_jacobian",
        note="killing family = common-h3 minor incidence; 17(ddddd)/17(aaaaa)",
        sources=[dict(n=108, m=72, M=[-72, 81, 106], V={2: 7, 3: 7},
                      u_s=2, v_s=7, delta="3", partition=[1, 1])],
    ),
    "G9966_delta2_stage4": dict(
        label="(99,66) delta=2 stage-4 unit (6264)",
        kind="split",
        nunk=2,
        script=CHARTS.parent / "g9966band-20260903/runs/delta2/stage4.sing",
        expected="UNIT",
        chart="joint_order_incidence_pole_jacobian",
        note="stage4_J_d159_k35 = 6264; 17(pppp)",
        sources=[dict(n=99, m=66, M=[-66, 77, 97], V={2: 8, 3: 8},
                      u_s=3, v_s=8, delta="2", partition=[2, 1])],
    ),
    "K8_d108_nosplit": dict(
        label="D=108 no-split k=4 ray K=8 pin+lower-band",
        kind="unsplit",
        nunk=36,
        script=(CHARTS.parent / "k4rayk89-20260903/explicit-runs/"
                "k8-rho-3prime-exact/exact/rho/K8_single_rho_p0_Q.sing"),
        expected="UNIT",
        chart="k4ray_pin_lower_band",
        note="36-var reduced chart; UNIT_IDEAL_CHAR0; 17(bbbbbb)",
        sources=[dict(n=108, m=72, n_prime=24, m_prime=16, M2=18, V2=7, ell=4)],
    ),
    "K9A_9966_unsplit": dict(
        label="(99,66) case A internal split A, K=9 pin+lower-band",
        kind="unsplit",
        nunk=36,
        script=(CHARTS.parent / "k4rayk89-20260903/driver-audit-artifacts/"
                "sparse-rho-guided/ROOT_K9A_FULL96_EXACTQ_V1/"
                "K9_A_full96_exact_Q_p0_Q.sing"),
        expected="UNIT",
        chart="k4ray_pin_lower_band",
        note="36-var chart A; UNIT_IDEAL_CHAR0; 17(bbbbbb)",
        sources=[dict(n=99, m=66, n_prime=27, m_prime=18, M2=21, V2=8, ell=4)],
    ),
}


def replay_known(name: str, dest: Path, timeout: int = 120) -> dict:
    spec = KNOWN[name]
    script = Path(spec["script"])
    if not script.is_file():
        return dict(ok=False, reason="missing_script", name=name, script=str(script))
    out_dir = dest / "controls" / name
    out_dir.mkdir(parents=True, exist_ok=True)
    replay = out_dir / (script.name)
    if replay.resolve() != script.resolve():
        shutil.copy2(script, replay)
    run = run_singular(replay, out_dir / name, timeout=timeout, cwd=replay.parent)
    unit = bool(run.get("unit"))
    dimension = run.get("dimension")
    if name == "G9966_delta2_stage4":
        # The stage-4 script prints BEGIN_GB; dim=-1 and basis 1 is the unit.
        stdout = Path(run["stdout"]).read_text(encoding="utf-8", errors="replace")
        if "BEGIN_DIM" in stdout:
            m = re.search(r"BEGIN_DIM\s*(-?\d+)", stdout)
            if m:
                dimension = int(m.group(1))
                run["dimension"] = dimension
            gb = re.search(r"BEGIN_GB\s*(.*?)\s*END_GB", stdout, re.S)
            if gb:
                body = gb.group(1).strip()
                unit = (dimension == -1) or body.strip() in {"1", "_[1]=1"} or (
                    "_[1]=1" in body.replace(" ", ""))
                run["unit"] = unit
                run["basis_size"] = 1 if unit else run.get("basis_size")
    if name == "D108_delta3":
        stdout = Path(run["stdout"]).read_text(encoding="utf-8", errors="replace")
        # MAIN_NF1 / 0 means reduce(1)=0
        mdim = re.search(r"MAIN_DIM\s*(-?\d+)", stdout)
        mnf = re.search(r"MAIN_NF1\s*(-?\d+)", stdout)
        msz = re.search(r"MAIN_SIZE\s*(-?\d+)", stdout)
        if mdim:
            dimension = int(mdim.group(1))
            run["dimension"] = dimension
        if mnf:
            unit = int(mnf.group(1)) == 0
            run["unit"] = unit
        if msz:
            run["basis_size"] = int(msz.group(1))
    verdict = "TIMEOUT" if run["timed_out"] else (
        "UNIT" if unit and (dimension in (-1, None) or dimension == -1) else
        ("NON_EMPTY" if dimension is not None and dimension >= 0 and not unit else "OPEN")
    )
    if unit and dimension == -1:
        verdict = "UNIT"
    cert = write_certificate(out_dir / "certificate.json", dict(
        class_id=name,
        label=spec["label"],
        kind=spec["kind"],
        chart_kind=spec["chart"],
        n_unknowns=spec["nunk"],
        engine="singular_replay",
        expected=spec["expected"],
        class_verdict="DEAD" if verdict == "UNIT" else verdict,
        stems=[dict(
            stem=name, verdict=verdict,
            **{k: run[k] for k in run if k != "stdout"},
            stdout=run.get("stdout"),
        )],
        note=spec["note"],
        sources=spec["sources"],
        control=True,
        exact_q=True,
        matched_expected=(verdict == spec["expected"]),
    ))
    return dict(ok=True, name=name, verdict=verdict, certificate=cert, run=run)


def tame_automorphism_control(dest: Path) -> dict:
    """Genuine tame automorphism must remain non-unit (positive control)."""
    out = dest / "controls" / "tame_automorphism"
    out.mkdir(parents=True, exist_ok=True)
    prelude = r"""
option(redSB); short=0;
ring RR = 0,(x,y,mu,mu_inv),dp;
poly h=x;
poly beta=mu*y;
poly alpha=(2/3)*(x-x^3-3*mu*x*y);
poly f=h^2+2*beta;
poly g=h^3+3*beta*h+(3/2)*alpha;
poly JJ=diff(f,x)*diff(g,y)-diff(f,y)*diff(g,x);
print("PRE__TAME_F "+string(f));
print("PRE__TAME_G "+string(g));
print("PRE__TAME_J "+string(JJ));
poly F0=x^2-y;
poly G0=x;
poly CHECK_IF_X=G0-x;
poly CHECK_IF_Y=G0^2-F0-y;
poly IX=y;
poly IY=y^2-x;
poly CHECK_FI_X=IX^2-IY-x;
poly CHECK_FI_Y=IX-y;
print("PRE__TAME_INVERSE_AFTER_FORWARD_X "+string(CHECK_IF_X));
print("PRE__TAME_INVERSE_AFTER_FORWARD_Y "+string(CHECK_IF_Y));
print("PRE__TAME_FORWARD_AFTER_INVERSE_X "+string(CHECK_FI_X));
print("PRE__TAME_FORWARD_AFTER_INVERSE_Y "+string(CHECK_FI_Y));
ring SS = 0,(mu,mu_inv),dp;
poly JCONST=-2*mu-1;
poly LOCALIZER=mu*mu_inv-1;
""".strip()
    system = GG.SingularSystem(
        name="CTRL_GENUINE_TAME_AUTOMORPHISM",
        prelude=prelude,
        generators=("JCONST", "LOCALIZER"),
        characteristic=0,
        variables=("mu", "mu_inv"),
        homogeneous=False,
        metadata={"specialized_map": "(f,g)=(x^2-y,x)", "jacobian": "1"},
    )
    result = GG.guided_groebner(
        system,
        policy=GG.PromotionPolicy.exact_q(
            "genuine tame J=1 automorphism must remain nonunit"),
        config=GG.RunConfig(
            out, timeout_seconds=30, total_cores=1,
            max_parallel_jobs=1, run_perturbed_control=False,
        ),
    )
    run = result.certificate["runs"][0]
    main = run["main"]
    stdout = Path(run["stdout"]).read_text(encoding="utf-8")
    markers_ok = all(m in stdout for m in (
        "PRE__TAME_INVERSE_AFTER_FORWARD_X 0",
        "PRE__TAME_FORWARD_AFTER_INVERSE_X 0",
    ))
    survives = (
        result.verdict.value in {"DIM0_CHAR0", "POSDIM"}
        and main.get("unit") is False
        and main.get("dimension") == 0
        and markers_ok
    )
    cert = write_certificate(out / "certificate.json", dict(
        class_id="CTRL_GENUINE_TAME_AUTOMORPHISM",
        label="genuine tame automorphism survives",
        kind="control",
        chart_kind="tame_J_const",
        n_unknowns=2,
        class_verdict="SURVIVES" if survives else "FAIL",
        expected="NON_EMPTY_DIM0",
        stems=[dict(
            stem="tame", verdict="NON_EMPTY" if survives else "FAIL",
            unit=main.get("unit"), dimension=main.get("dimension"),
            vdim=main.get("vdim"), guided_verdict=result.verdict.value,
            script=run.get("script"), stdout=run.get("stdout"),
            script_sha256=run.get("script_sha256"),
            stdout_sha256=run.get("stdout_sha256"),
        )],
        control=True,
        note="Negative control: a genuine automorphism is not a unit ideal.",
    ))
    return dict(ok=survives, certificate=cert, survives=survives)


# ---------------------------------------------------------------------------
# per-class run (local or worker)
# ---------------------------------------------------------------------------

def run_class(
    dest: Path,
    entry: dict,
    extract_timeout: int,
    solve_timeout: int,
    support: str = "source-complete",
    with_msolve: bool = False,
    primes: Sequence[int] = (),
) -> dict:
    cid = entry["class_id"]
    emitted = emit_order_class(entry, dest, support=support)
    if not emitted.get("ok"):
        cert = write_certificate(
            dest / "classes" / cid / "certificate.json",
            dict(class_id=cid, class_verdict="OPEN",
                 reason=emitted.get("reason"), n_unknowns=entry.get("nunk"),
                 kind=entry.get("kind"), stems=[]),
        )
        return cert
    class_dir = Path(emitted["dest"])
    # Conjunctive fibres: solve each V-stem. The union is a cheap sufficient
    # kill (union UNIT => every fibre UNIT) but not necessary.
    stem_results = []
    union_result = None
    extract_u = extract_stem(class_dir, emitted["union_stem"], extract_timeout)
    if extract_u.get("ok"):
        union_result = solve_rows_guided(
            class_dir, emitted["union_stem"], solve_timeout, characteristic=0)
        if primes:
            screens = []
            for p in primes:
                screens.append(solve_rows_guided(
                    class_dir, emitted["union_stem"], solve_timeout,
                    characteristic=p))
            union_result["prime_screens"] = screens
        if with_msolve and union_result.get("unknowns", 10 ** 9) <= 80:
            try:
                meta = json.loads(
                    (class_dir / "meta" / ("%s.json" % emitted["union_stem"])
                     ).read_text(encoding="utf-8"))
                rows = OB.read_rows(class_dir / "rows" / (
                    "%s_rows.tsv" % emitted["union_stem"]))
                mapping = {}
                serial = 1
                for original in meta["variables"]:
                    if original == "c":
                        mapping[original] = "c"
                    else:
                        mapping[original] = "v%d" % serial
                        serial += 1
                mapping["T"] = "z"
                polys = []
                ident = re.compile(r"[A-Za-z][A-Za-z0-9_]*")
                for row in rows:
                    polys.append(ident.sub(
                        lambda m: mapping.get(m.group(0), m.group(0)),
                        row["expr"]))
                polys.append("z*c-1")
                order = [mapping[v] for v in meta["variables"] if v in mapping] + ["z"]
                ms = class_dir / "jobs" / ("%s_p32003.ms" % emitted["union_stem"])
                emit_msolve_file(order, polys, 32003, ms)
                union_result["msolve_p32003"] = solve_msolve(ms, min(solve_timeout, 300))
            except Exception as exc:
                union_result["msolve_error"] = str(exc)
        if stem_verdict(union_result) == "UNIT":
            stem_results.append(union_result)
            kind = entry.get("kind") or "unsplit"
            jac_zero = (
                extract_u.get("declared_equations") == 1
                and union_result.get("equations") == 1
            )
            if kind in ("split", "mixed"):
                class_v = "OPEN"
                note = (
                    "unsplit/order chart is UNIT (exact Q), but this class "
                    "has a nonempty split window: the joint chart (order + "
                    "minor-incidence + pole + Jacobian) is still required "
                    "for every split fibre. Not promoted to class DEAD."
                )
            else:
                class_v = "DEAD"
                note = (
                    "union UNIT implies every unsplit fibre UNIT. "
                    + ("Jacobian identically 0 on the D1 support "
                       "(x-free inventory); J=c is impossible."
                       if jac_zero else
                       "full necessary order chart, exact-Q unit.")
                )
            cert = write_certificate(class_dir / "certificate.json", dict(
                class_id=cid, kind=kind,
                chart_kind="order_source_complete_union",
                n_unknowns=union_result.get("unknowns"),
                class_verdict=class_v,
                stems=stem_results,
                union=union_result,
                extract=extract_u,
                jacobian_identically_zero=jac_zero,
                note=note,
                exact_q=True,
                unsplit_order_unit=True,
            ))
            return cert
    # union did not kill: run fibres
    for stem in emitted["stems"]:
        ex = extract_stem(class_dir, stem, extract_timeout)
        if not ex.get("ok"):
            stem_results.append(dict(
                stem=stem, verdict="TIMEOUT" if ex.get("timed_out") else "OPEN",
                extract=ex))
            continue
        solved = solve_rows_guided(class_dir, stem, solve_timeout, characteristic=0)
        solved["extract"] = ex
        stem_results.append(solved)
    verdict = class_verdict(stem_results)
    if union_result is not None and not any(
            r.get("stem") == emitted["union_stem"] for r in stem_results):
        # record the non-unit union as diagnostic, not as a stem of the kill
        pass
    cert = write_certificate(class_dir / "certificate.json", dict(
        class_id=cid, kind=entry.get("kind"),
        chart_kind="order_source_complete",
        n_unknowns=entry.get("nunk"),
        class_verdict=verdict,
        stems=stem_results,
        union=union_result,
        extract_union=extract_u,
        fibre_size=emitted["fibre_size"],
        exact_q=any(r.get("characteristic") == 0 and r.get("unit")
                    for r in stem_results),
        note=(
            "NON_EMPTY is not a counterexample unless a point with J=const "
            "lifts. TIMEOUT at this size is the compute-bound threshold."
        ),
    ))
    return cert


# ---------------------------------------------------------------------------
# fleet: setsid/nohup on workers, then poll (no unwaited local background)
# ---------------------------------------------------------------------------

def ssh(ip: str, remote: str, timeout: int = 30) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["ssh", *SSH_OPTS, "ubuntu@%s" % ip, remote],
        text=True, capture_output=True, timeout=timeout,
    )


def rsync_to(ip: str, local: Path, remote: str) -> None:
    subprocess.run(
        ["rsync", "-az", "-e", "ssh %s" % " ".join(SSH_OPTS),
         "%s/" % local, "ubuntu@%s:%s/" % (ip, remote)],
        check=True,
    )


def launch_remote_class(
    ip: str,
    dest: Path,
    class_id: str,
    extract_timeout: int,
    solve_timeout: int,
    support: str,
) -> dict:
    remote_root = "~/jc2"
    remote_dest = "/home/ubuntu/jc2/box/census-sweep-20260905"
    # push the library and this class directory
    subprocess.run(
        ["rsync", "-az", "-e", "ssh %s" % " ".join(SSH_OPTS),
         str(LIB / "census_sweep.py"),
         "ubuntu@%s:%s/box/lib/census_sweep.py" % (ip, remote_root)],
        check=True,
    )
    class_dir = dest / "classes" / class_id
    if class_dir.is_dir():
        ssh(ip, "mkdir -p %s/%s/classes/%s" % (remote_root, remote_dest, class_id))
        subprocess.run(
            ["rsync", "-az", "-e", "ssh %s" % " ".join(SSH_OPTS),
             "%s/" % class_dir,
             "ubuntu@%s:%s/%s/classes/%s/" % (
                 ip, remote_root, remote_dest, class_id)],
            check=True,
        )
    log = "~/census-sweep-%s.log" % class_id
    cmd = (
        "cd %s && mkdir -p %s && setsid bash -c "
        "'timeout %d python3 -u box/lib/census_sweep.py run-class "
        "--dest %s --class-id %s --extract-timeout %d --solve-timeout %d "
        "--support %s > %s 2>&1' </dev/null >/dev/null 2>&1 & echo LAUNCHED pid=$!"
        % (remote_root, remote_dest, extract_timeout + solve_timeout + 60,
           remote_dest, class_id, extract_timeout, solve_timeout, support, log)
    )
    proc = ssh(ip, cmd, timeout=20)
    return dict(
        ip=ip, class_id=class_id, stdout=proc.stdout, stderr=proc.stderr,
        returncode=proc.returncode, log=log,
    )


def poll_remote_class(ip: str, class_id: str) -> dict:
    remote = (
        "python3 - <<'PY'\n"
        "import json, os, glob\n"
        "p=os.path.expanduser('~/jc2/box/census-sweep-20260905/classes/%s/certificate.json')\n"
        "print('CERT', int(os.path.isfile(p)))\n"
        "if os.path.isfile(p):\n"
        "    print(open(p).read())\n"
        "PY\n"
        "echo RUNNING $(pgrep -c -f 'census_sweep.py run-class' || true)\n"
        "echo LOGTAIL; tail -3 ~/census-sweep-%s.log 2>/dev/null || true\n"
        % (class_id, class_id)
    )
    proc = ssh(ip, remote, timeout=20)
    text = proc.stdout or ""
    cert = None
    if "CERT 1" in text:
        try:
            blob = text.split("CERT 1", 1)[1]
            blob = blob.split("RUNNING", 1)[0].strip()
            cert = json.loads(blob)
        except json.JSONDecodeError:
            cert = None
    running = False
    m = re.search(r"RUNNING\s+(\d+)", text)
    if m:
        running = int(m.group(1)) > 0
    return dict(ip=ip, class_id=class_id, certificate=cert,
                running=running, raw=text[-1500:])


def pull_remote_class(ip: str, dest: Path, class_id: str) -> None:
    target = dest / "classes" / class_id
    target.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["rsync", "-az", "-e", "ssh %s" % " ".join(SSH_OPTS),
         "ubuntu@%s:~/jc2/box/census-sweep-20260905/classes/%s/" % (ip, class_id),
         "%s/" % target],
        check=False,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def cmd_enumerate(args: argparse.Namespace) -> int:
    dest = Path(args.dest).resolve()
    dest.mkdir(parents=True, exist_ok=True)
    inventory = enumerate_us_ge2(
        nmin=args.nmin, nmax=args.nmax, kmin=args.kmin, full=not args.no_full)
    # drop bulky per-row closed forms from the JSON
    slim_rows = []
    for rec in inventory["rows"]:
        slim_rows.append(dict(
            n=rec["src_n"], m=rec["src_m"], M=rec["src_M"], V=rec["src_V"],
            u_s=rec["u_s"], v_s=rec["v_s"], ell=rec["ell"],
            kind=rec["kind"], window=rec["window"],
            class_id=rec["class_id"],
            four_int_key=rec["four_int_key"],
            coarse_key=rec["coarse_key"],
            n_prime=rec["n_prime"], m_prime=rec["m_prime"],
        ))
    payload = dict(summary=inventory["summary"], classes=inventory["classes"],
                   n_rows=len(slim_rows), rows=slim_rows)
    if args.xufloor:
        payload["sharpened"] = sharpen_four_int_from_xufloor(Path(args.xufloor))
        print("sharpened xu_ok_candidate: %d records -> %d four-int keys"
              % (payload["sharpened"]["n_xu_ok_candidate"],
                 payload["sharpened"]["n_four_int_keys"]), flush=True)
    atomic_json(dest / "inventory.json", payload)
    # size histogram
    hist: dict[str, int] = defaultdict(int)
    for cls in inventory["classes"]:
        nunk = cls["nunk"]
        if nunk >= 10 ** 8:
            bucket = "unsizeable"
        elif nunk <= 40:
            bucket = "<=40"
        elif nunk <= 80:
            bucket = "41-80"
        elif nunk <= 120:
            bucket = "81-120"
        elif nunk <= 200:
            bucket = "121-200"
        else:
            bucket = ">200"
        hist[bucket] += 1
    print("size histogram:", dict(hist), flush=True)
    print("smallest 15:")
    for cls in inventory["classes"][:15]:
        print("  nunk=%s engine=%s kind=%s %s fibre=%d K=%s B=%s"
              % (cls["nunk"] if cls["nunk"] < 10 ** 8 else "NA",
                 cls["engine"], cls["kind"], cls["class_id"],
                 cls["fibre_size"], cls.get("K"), cls.get("B_safe")))
    return 0


def cmd_controls(args: argparse.Namespace) -> int:
    dest = Path(args.dest).resolve()
    dest.mkdir(parents=True, exist_ok=True)
    results = {}
    for name in ("D108_delta3", "G9966_delta2_stage4",
                 "K8_d108_nosplit", "K9A_9966_unsplit"):
        print("control", name, flush=True)
        results[name] = replay_known(name, dest, timeout=args.timeout)
        print("  ->", results[name].get("verdict"),
              results[name].get("reason"), flush=True)
    print("control tame automorphism", flush=True)
    results["tame"] = tame_automorphism_control(dest)
    print("  -> survives", results["tame"].get("survives"), flush=True)
    atomic_json(dest / "controls" / "summary.json", dict(
        results={k: {kk: vv for kk, vv in v.items() if kk != "run"}
                 for k, v in results.items()},
    ))
    failed = []
    if results["D108_delta3"].get("verdict") != "UNIT":
        failed.append("D108_delta3")
    if results["G9966_delta2_stage4"].get("verdict") != "UNIT":
        failed.append("G9966_delta2_stage4")
    if results["K8_d108_nosplit"].get("verdict") != "UNIT":
        failed.append("K8_d108_nosplit")
    if results["K9A_9966_unsplit"].get("verdict") != "UNIT":
        failed.append("K9A_9966_unsplit")
    if not results["tame"].get("survives"):
        failed.append("tame")
    print("controls failed:" if failed else "ALL CONTROLS PASSED", failed)
    return 1 if failed else 0


def load_inventory(dest: Path) -> dict:
    path = dest / "inventory.json"
    return json.loads(path.read_text(encoding="utf-8"))


def cmd_sweep(args: argparse.Namespace) -> int:
    dest = Path(args.dest).resolve()
    dest.mkdir(parents=True, exist_ok=True)
    inventory = load_inventory(dest)
    classes = inventory["classes"]
    selected = []
    for cls in classes:
        if cls.get("skip_reason"):
            continue
        if cls["nunk"] > args.max_unknowns:
            continue
        selected.append(cls)
        if args.limit and len(selected) >= args.limit:
            break
    print("sweep selected %d classes with nunk <= %d"
          % (len(selected), args.max_unknowns), flush=True)
    workers = list(args.workers) if args.workers else []
    local_cutoff = args.local_cutoff
    certificates = []
    remote_jobs = []
    # emit locally first so workers have builders
    for i, cls in enumerate(selected):
        nunk = cls["nunk"]
        use_remote = bool(workers) and nunk > local_cutoff
        if use_remote:
            emit_order_class(cls, dest, support=args.support)
            ip = workers[i % len(workers)]
            launch = launch_remote_class(
                ip, dest, cls["class_id"],
                args.extract_timeout, args.solve_timeout, args.support)
            print("LAUNCH", cls["class_id"], "nunk", nunk, "->", ip,
                  launch.get("stdout"), flush=True)
            remote_jobs.append(dict(ip=ip, entry=cls, launch=launch))
        else:
            print("LOCAL", cls["class_id"], "nunk", nunk, flush=True)
            cert = run_class(
                dest, cls,
                extract_timeout=args.extract_timeout,
                solve_timeout=args.solve_timeout,
                support=args.support,
                with_msolve=args.msolve,
                primes=GOOD_PRIMES if args.primes else (),
            )
            print("  ->", cert.get("class_verdict"), flush=True)
            certificates.append(cert)
    # poll remotes in the FOREGROUND
    deadline = time.time() + args.poll_seconds
    pending = list(remote_jobs)
    while pending and time.time() < deadline:
        still = []
        for job in pending:
            status = poll_remote_class(job["ip"], job["entry"]["class_id"])
            if status.get("certificate"):
                pull_remote_class(job["ip"], dest, job["entry"]["class_id"])
                certificates.append(status["certificate"])
                print("REMOTE DONE", job["entry"]["class_id"],
                      status["certificate"].get("class_verdict"), flush=True)
            elif status.get("running"):
                still.append(job)
            else:
                # not running and no cert yet — give it one more pass
                job["misses"] = job.get("misses", 0) + 1
                if job["misses"] < 3:
                    still.append(job)
                else:
                    print("REMOTE LOST", job["entry"]["class_id"],
                          status.get("raw", "")[-200:], flush=True)
                    certificates.append(dict(
                        class_id=job["entry"]["class_id"],
                        class_verdict="TIMEOUT", n_unknowns=job["entry"]["nunk"],
                        stems=[], note="worker job vanished without certificate",
                    ))
        pending = still
        if pending:
            time.sleep(args.poll_interval)
    for job in pending:
        pull_remote_class(job["ip"], dest, job["entry"]["class_id"])
        certificates.append(dict(
            class_id=job["entry"]["class_id"],
            class_verdict="TIMEOUT", n_unknowns=job["entry"]["nunk"],
            stems=[], note="poll deadline",
        ))
        print("REMOTE TIMEOUT", job["entry"]["class_id"], flush=True)

    dead = [c for c in certificates if c.get("class_verdict") == "DEAD"]
    nonempty = [c for c in certificates if c.get("class_verdict") == "NON_EMPTY"]
    timeout = [c for c in certificates if c.get("class_verdict") == "TIMEOUT"]
    open_ = [c for c in certificates if c.get("class_verdict") not in
             {"DEAD", "NON_EMPTY", "TIMEOUT"}]
    # compute-bound threshold: smallest nunk among TIMEOUT, else first skipped
    bound = None
    timeout_sizes = sorted(c.get("n_unknowns") or 10 ** 9 for c in timeout)
    if timeout_sizes:
        bound = timeout_sizes[0]
    elif selected and classes:
        larger = [c["nunk"] for c in classes
                  if c["nunk"] > args.max_unknowns and c["nunk"] < 10 ** 8]
        if larger:
            bound = min(larger)
    tally = dict(
        swept=len(certificates),
        dead=len(dead),
        nonempty=len(nonempty),
        timeout=len(timeout),
        open=len(open_),
        max_unknowns=args.max_unknowns,
        compute_bound_threshold=bound,
        dead_ids=[c.get("class_id") for c in dead],
        nonempty_ids=[c.get("class_id") for c in nonempty],
        timeout_ids=[c.get("class_id") for c in timeout],
    )
    atomic_json(dest / "tally.json", dict(tally=tally, certificates=certificates))
    print("TALLY", json.dumps(tally, indent=2), flush=True)
    return 0


def cmd_run_class(args: argparse.Namespace) -> int:
    dest = Path(args.dest).resolve()
    inventory = load_inventory(dest)
    entry = None
    for cls in inventory["classes"]:
        if cls["class_id"] == args.class_id:
            entry = cls
            break
    if entry is None:
        # allow a class.json already on disk (worker path)
        cj = dest / "classes" / args.class_id / "class.json"
        if cj.is_file():
            data = json.loads(cj.read_text(encoding="utf-8"))
            entry = dict(
                class_id=args.class_id, kind=data.get("kind", "unsplit"),
                nunk=data.get("union_parameter_count") or data.get("nunk") or 0,
                n_prime=data["n_prime"], m_prime=data["m_prime"],
                M_prime=data["M_prime"], ell=data["ell"],
                s_prime=data["s_prime"],
                sources=[r["source"] for r in data.get("rows", [])],
                engine=data.get("engine"),
            )
        else:
            raise SystemExit("unknown class %s" % args.class_id)
    cert = run_class(
        dest, entry,
        extract_timeout=args.extract_timeout,
        solve_timeout=args.solve_timeout,
        support=args.support,
        with_msolve=args.msolve,
        primes=GOOD_PRIMES if args.primes else (),
    )
    print(json.dumps(cert, indent=2, default=jdefault))
    return 0 if cert.get("class_verdict") in {"DEAD", "NON_EMPTY", "TIMEOUT", "OPEN"} else 1


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="census_sweep")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("enumerate", help="u_s>=2 census + descended classes + sizes")
    p.add_argument("--dest", type=Path, default=DEFAULT_DEST)
    p.add_argument("--nmin", type=int, default=16)
    p.add_argument("--nmax", type=int, default=200)
    p.add_argument("--kmin", type=int, default=16)
    p.add_argument("--no-full", action="store_true")
    p.add_argument("--xufloor", type=str,
                   default=str(BOX / "xufloor-20260903/results.json"))
    p.set_defaults(func=cmd_enumerate)

    p = sub.add_parser("controls", help="replay D=108 d=3, (99,66) d=2, k4ray, tame auto")
    p.add_argument("--dest", type=Path, default=DEFAULT_DEST)
    p.add_argument("--timeout", type=int, default=180)
    p.set_defaults(func=cmd_controls)

    p = sub.add_parser("sweep", help="emit+solve the smallest N classes")
    p.add_argument("--dest", type=Path, default=DEFAULT_DEST)
    p.add_argument("--limit", type=int, default=24)
    p.add_argument("--max-unknowns", type=int, default=120)
    p.add_argument("--local-cutoff", type=int, default=40)
    p.add_argument("--extract-timeout", type=int, default=600)
    p.add_argument("--solve-timeout", type=int, default=600)
    p.add_argument("--support", default="source-complete",
                   choices=("source-complete", "raw-D1"))
    p.add_argument("--msolve", action="store_true")
    p.add_argument("--primes", action="store_true")
    p.add_argument("--workers", nargs="*", default=list(WORKERS))
    p.add_argument("--poll-seconds", type=int, default=2400)
    p.add_argument("--poll-interval", type=int, default=20)
    p.set_defaults(func=cmd_sweep)

    p = sub.add_parser("run-class", help="emit+extract+solve one class (worker entry)")
    p.add_argument("--dest", type=Path, default=DEFAULT_DEST)
    p.add_argument("--class-id", required=True)
    p.add_argument("--extract-timeout", type=int, default=600)
    p.add_argument("--solve-timeout", type=int, default=600)
    p.add_argument("--support", default="source-complete",
                   choices=("source-complete", "raw-D1"))
    p.add_argument("--msolve", action="store_true")
    p.add_argument("--primes", action="store_true")
    p.set_defaults(func=cmd_run_class)
    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
