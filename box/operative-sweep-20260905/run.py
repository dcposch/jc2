#!/usr/bin/env python3
"""OPERATIVE residual sweep: 1,420 C_FULL_TREE_POLYNOMIAL_ODE rows.

Uses the frozen census_sweep pipeline (exact-Q, source-complete charts,
builder_fix, FALLACY-v2). Does not edit box/lib/census_sweep.py.

Tiers (child-data p.174-effective partition):
  live_us1      174  u_s=1 and (C-TOP) holds
  us_ge2        310  u_s>=2 (C-TOP unlicensed; 6 U-NEG structurally dead)
  ctop_killed   936  u_s=1 and (C-TOP) fails (still under gate; separate tier)
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from collections import defaultdict
from math import gcd
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
BOX = ROOT / "box"
LIB = BOX / "lib"
DEST = BOX / "operative-sweep-20260905"
SCOPE_JSON = BOX / "scopeleaks-20260905" / "scope_enum.json"
CENSUS_DEST = BOX / "census-sweep-20260905"
FLEET_KEY = Path.home() / ".ssh" / "jc2-fleet"
SSH_OPTS = (
    "-i", str(FLEET_KEY),
    "-o", "StrictHostKeyChecking=no",
    "-o", "BatchMode=yes",
    "-o", "ConnectTimeout=12",
)
REMOTE_ROOT = "/home/ubuntu/jc2"
REMOTE_DEST = "/home/ubuntu/jc2/box/operative-sweep-20260905"
J0_A = "C_n32m24_Mm20_m6_ell0_s3_V1_6"
J0_B = "C_n36m24_Mm18_m8_ell0_s3_V2_9"

sys.path.insert(0, str(LIB))
sys.path.insert(0, str(BOX))
sys.path.insert(0, str(BOX / "moh14-charts-20260905"))
sys.path.insert(0, str(BOX / "orderbasis-20260903"))
sys.path.insert(0, str(BOX / "mohprog-drivers-20260903"))

import census_sweep as CS  # noqa: E402
import moh_skeleton_full as MS  # noqa: E402
import sprime3_compiler as S3  # noqa: E402
import split_window as SW  # noqa: E402


TIERS = ("live_us1", "us_ge2", "ctop_killed")


def v_int(raw) -> dict[int, int]:
    return {int(k): int(v) for k, v in raw.items()}


def skel_of(row: dict) -> MS.Skel:
    return MS.Skel(int(row["n"]), int(row["m"]), list(row["Ms"]), v_int(row["V"]))


def ctop_p174(descended: dict) -> dict:
    """(C-TOP) after Moh p.174 drop on the child's M' list: V'_s' <= d'_s'."""
    if not descended.get("ok_int"):
        return dict(holds=None, dropped=None, reason="descended_M_not_integer")
    M = CS.int_dict(descended["M"])
    d = CS.int_dict(descended["d"])
    V = CS.int_dict(descended["V"])
    datum = dict(
        n=int(descended["n"]), m=int(descended["m"]), s=int(descended["s"]),
        M=M, d=d, V=V, ell=int(descended["ell"]), us=int(descended["us"]),
    )
    dropped = S3.drop_p174(datum)
    s = dropped["s"]
    if s < 1 or s not in dropped["V"] or s not in dropped["d"]:
        return dict(holds=None, dropped=dropped["dropped"], reason="no_top_after_drop")
    holds = int(dropped["V"][s]) <= int(dropped["d"][s])
    return dict(
        holds=holds,
        dropped=dropped["dropped"],
        s_eff=s,
        V_top=int(dropped["V"][s]),
        d_top=int(dropped["d"][s]),
        M_top=int(dropped["M"][s]) if s in dropped["M"] else None,
    )


def uneg_of(descended: dict) -> bool | None:
    d = CS.int_dict(descended.get("d") or {})
    V = CS.int_dict(descended.get("V") or {})
    if not d or not V or 2 not in d or 2 not in V:
        return None
    return int(V[2]) > int(d[2])


def split_leaves(skel: MS.Skel) -> dict:
    """(ρ,λ) leaf count via the charged split_window screen."""
    try:
        view = SW.screen_skeleton(skel)
    except Exception as exc:
        return dict(ok=False, error=str(exc), survivor_count=None)
    survivors = view.get("survivors") or []
    return dict(
        ok=True,
        survivor_count=int(view.get("survivor_count") or 0),
        killed_count=int(view.get("killed_count") or 0),
        raw_pair_count=(view.get("finite_window") or {}).get("raw_pair_count"),
        orders=(view.get("finite_window") or {}).get("orders"),
        survivors=[{"rho": s.get("rho"), "partition": s.get("partition")}
                   for s in survivors],
    )


def size_entry(members: list[dict]) -> dict:
    representative = members[0]
    closed = None
    counts = None
    reason = None
    if not representative["ok_int"]:
        reason = "descended_M_not_integer"
    else:
        closed = CS.child_closed_form(dict(
            n=representative["n_prime"], m=representative["m_prime"],
            s=representative["s_prime"], M=representative["M"],
            d=representative["d"], V=representative["V"],
            ell=representative["ell"], us=representative["u_s"],
        ))
        if closed is None:
            reason = "closed_form_failed"
        elif closed["B"] >= 0:
            reason = "B_safe_nonneg"
            counts = CS.inventory_counts(closed)
        else:
            counts = CS.inventory_counts(closed)
    kinds = sorted(set(m["kind"] for m in members))
    kind = kinds[0] if len(kinds) == 1 else "mixed"
    if counts is None:
        nunk, engine = 10 ** 9, "unsizeable"
    else:
        nunk, engine = CS.solvable_unknowns(counts, kind)
    key = representative["class_key"]
    # split-window leaves: union of surviving (rho, partition) over sources
    leaf_union = []
    leaf_count = 0
    for m in members:
        sl = m.get("split_leaves") or {}
        if sl.get("ok"):
            leaf_count = max(leaf_count, int(sl.get("survivor_count") or 0))
            for item in sl.get("survivors") or []:
                leaf_union.append(item)
    # unique (rho, partition)
    seen = set()
    unique_leaves = []
    for item in leaf_union:
        tok = (item.get("rho"), tuple(item.get("partition") or ()))
        if tok not in seen:
            seen.add(tok)
            unique_leaves.append(item)
    return dict(
        class_id=CS.class_id_of(key),
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
            kind=m["kind"], uneg=m["uneg"], ctop=m["ctop"],
            split_survivor_count=(m.get("split_leaves") or {}).get("survivor_count"),
        ) for m in members],
        four_int_key=representative["four_int_key"],
        coarse_key=list(representative["coarse_key"]),
        tier=representative["tier"],
        n_uneg=sum(1 for m in members if m["uneg"]),
        split_survivor_count=len(unique_leaves) if kind in ("split", "mixed") else 0,
        split_leaves=unique_leaves if kind in ("split", "mixed") else [],
        window=representative.get("window") or [],
        u_s=representative["u_s"],
        v_s=representative["v_s"],
    )


def build_inventory() -> dict:
    payload = json.loads(SCOPE_JSON.read_text(encoding="utf-8"))
    rows_in = payload["operative_rows"]
    assert len(rows_in) == 1420, len(rows_in)
    started = time.time()
    recs = []
    skipped = 0
    for raw in rows_in:
        skel = skel_of(raw)
        descended = CS.descend(skel)
        if descended is None:
            skipped += 1
            continue
        cls = CS.classify_row(skel, descended)
        ctop = ctop_p174(descended)
        uneg = uneg_of(descended)
        us = int(cls["u_s"])
        if us >= 2:
            tier = "us_ge2"
        elif ctop.get("holds") is True:
            tier = "live_us1"
        else:
            tier = "ctop_killed"
        sl = split_leaves(skel) if cls["kind"] in ("split", "mixed") or us >= 2 else dict(
            ok=True, survivor_count=0, survivors=[],
        )
        rec = dict(
            src_n=int(raw["n"]), src_m=int(raw["m"]), src_M=list(raw["Ms"]),
            src_V=v_int(raw["V"]),
            src_s=skel.s, src_d=skel.d, src_K=skel.K,
            **cls, **{k: descended[k] for k in (
                "M", "d", "V", "ok_int", "ds", "us", "vs")},
            ctop=ctop.get("holds"),
            ctop_dropped=ctop.get("dropped"),
            ctop_detail=ctop,
            uneg=uneg,
            tier=tier,
            class_key=CS.class_key(descended),
            four_int_key=CS.four_int_key(descended),
            coarse_key=CS.coarse_key(descended),
            split_leaves=sl,
        )
        rec["class_id"] = CS.class_id_of(rec["class_key"])
        recs.append(rec)

    by_tier_rows = {t: [r for r in recs if r["tier"] == t] for t in TIERS}
    classes_by_tier: dict[str, list[dict]] = {}
    for tier in TIERS:
        groups: dict[tuple, list[dict]] = defaultdict(list)
        for rec in by_tier_rows[tier]:
            groups[rec["class_key"]].append(rec)
        sized = [size_entry(members) for members in groups.values()]
        sized.sort(key=lambda c: (c["nunk"], c["n_prime"], c["m_prime"], c["ell"],
                                  c["class_id"]))
        classes_by_tier[tier] = sized

    def hist(classes):
        buckets = defaultdict(int)
        for cls in classes:
            nunk = cls["nunk"]
            if nunk >= 10 ** 8:
                buckets["unsizeable"] += 1
            elif nunk <= 40:
                buckets["<=40"] += 1
            elif nunk <= 80:
                buckets["41-80"] += 1
            elif nunk <= 100:
                buckets["81-100"] += 1
            elif nunk <= 120:
                buckets["101-120"] += 1
            elif nunk <= 200:
                buckets["121-200"] += 1
            else:
                buckets[">200"] += 1
        return dict(buckets)

    summary = dict(
        n_operative=len(rows_in),
        n_descended=len(recs),
        n_skipped_no_descent=skipped,
        elapsed_seconds=round(time.time() - started, 3),
        rows_by_tier={t: len(by_tier_rows[t]) for t in TIERS},
        classes_by_tier={t: len(classes_by_tier[t]) for t in TIERS},
        nunk_hist_by_tier={t: hist(classes_by_tier[t]) for t in TIERS},
        nunk_le_100={t: sum(1 for c in classes_by_tier[t]
                            if c["nunk"] <= 100 and c["nunk"] < 10 ** 8)
                     for t in TIERS},
        uneg_by_tier={t: sum(1 for r in by_tier_rows[t] if r["uneg"])
                      for t in TIERS},
        mixed_by_tier={t: sum(1 for c in classes_by_tier[t]
                              if c["kind"] in ("split", "mixed"))
                       for t in TIERS},
        unsplit_by_tier={t: sum(1 for c in classes_by_tier[t]
                                if c["kind"] == "unsplit")
                         for t in TIERS},
    )
    slim_rows = []
    for rec in recs:
        slim_rows.append(dict(
            n=rec["src_n"], m=rec["src_m"], M=rec["src_M"], V=rec["src_V"],
            u_s=rec["u_s"], v_s=rec["v_s"], ell=rec["ell"],
            kind=rec["kind"], window=rec["window"],
            class_id=rec["class_id"], tier=rec["tier"],
            uneg=rec["uneg"], ctop=rec["ctop"],
            n_prime=rec["n_prime"], m_prime=rec["m_prime"],
            split_survivor_count=(rec.get("split_leaves") or {}).get("survivor_count"),
        ))
    inventory = dict(
        schema="operative-sweep-inventory-v1",
        summary=summary,
        classes_by_tier=classes_by_tier,
        n_rows=len(slim_rows),
        rows=slim_rows,
    )
    CS.atomic_json(DEST / "inventory.json", inventory)
    CS.atomic_json(DEST / "inventory-summary.json", summary)
    print("INVENTORY", json.dumps(summary, indent=2), flush=True)
    for tier in TIERS:
        print("---", tier, "smallest 12 ---", flush=True)
        for cls in classes_by_tier[tier][:12]:
            print("  nunk=%s engine=%s kind=%s %s fibre=%d K=%s B=%s leaves=%s skip=%s"
                  % (cls["nunk"] if cls["nunk"] < 10 ** 8 else "NA",
                     cls["engine"], cls["kind"], cls["class_id"],
                     cls["fibre_size"], cls.get("K"), cls.get("B_safe"),
                     cls.get("split_survivor_count"), cls.get("skip_reason")),
                  flush=True)
    return inventory


def load_inventory() -> dict:
    path = DEST / "inventory.json"
    if not path.is_file():
        return build_inventory()
    return json.loads(path.read_text(encoding="utf-8"))


def selected_for_sweep(inventory: dict, max_unknowns: int = 100) -> list[dict]:
    out = []
    for tier in TIERS:
        for cls in inventory["classes_by_tier"][tier]:
            if cls.get("skip_reason") and cls["nunk"] >= 10 ** 8:
                continue
            if cls["nunk"] > max_unknowns:
                continue
            out.append(cls)
    out.sort(key=lambda c: (c["nunk"], c["tier"], c["class_id"]))
    return out


def annotate_certificate(cert: dict, entry: dict) -> dict:
    """Record split leaves; never promote mixed/order-unit to class DEAD."""
    kind = entry.get("kind") or cert.get("kind")
    leaves = entry.get("split_leaves") or []
    leaf_n = entry.get("split_survivor_count") or 0
    cert["tier"] = entry.get("tier")
    cert["kind"] = kind
    cert["nunk_sort"] = entry.get("nunk")
    cert["engine"] = entry.get("engine")
    cert["split_survivor_count"] = leaf_n
    cert["split_leaves"] = leaves
    cert["window"] = entry.get("window") or []
    if kind in ("split", "mixed"):
        if cert.get("class_verdict") == "DEAD":
            cert["class_verdict"] = "OPEN"
            cert["note"] = (
                "unsplit/order chart UNIT would not kill a mixed class; "
                "split fibres remain OPEN with (rho,lambda) leaf count %d"
                % leaf_n
            )
        cert["open_split"] = True
        cert["split_reason"] = (
            "nonempty split window; (rho,lambda) survivors=%d via "
            "box/lib/split_window.py; order chart cannot kill split fibres"
            % leaf_n
        )
    uneg = entry.get("n_uneg") or 0
    if uneg:
        cert["uneg_sources"] = uneg
    return cert


def _msolve_screen(class_dir: Path, stem: str, timeout: int) -> dict:
    """Modular msolve -g 2 screen. Never promoted to a class kill."""
    import re
    meta_path = class_dir / "meta" / ("%s.json" % stem)
    if not meta_path.is_file():
        return dict(ok=False, reason="no_meta")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    rows_path = class_dir / "rows" / ("%s_rows.tsv" % stem)
    if not rows_path.is_file():
        return dict(ok=False, reason="no_rows")
    try:
        import order_basis_full as OB
        rows = OB.read_rows(rows_path)
    except Exception as exc:
        return dict(ok=False, reason="read_rows:%s" % exc)
    mapping = {}
    serial = 1
    for original in meta["variables"]:
        if original == "c":
            mapping[original] = "c"
        else:
            mapping[original] = "v%d" % serial
            serial += 1
    mapping["T"] = "z"
    ident = re.compile(r"[A-Za-z][A-Za-z0-9_]*")
    polys = []
    for row in rows:
        polys.append(ident.sub(lambda m: mapping.get(m.group(0), m.group(0)),
                               row["expr"]))
    polys.append("z*c-1")
    order = [mapping[v] for v in meta["variables"] if v in mapping] + ["z"]
    ms = class_dir / "jobs" / ("%s_p32003.ms" % stem)
    try:
        CS.emit_msolve_file(order, polys, 32003, ms)
    except Exception as exc:
        return dict(ok=False, reason="emit_msolve:%s" % exc)
    return CS.solve_msolve(ms, timeout)


def run_one_class(entry: dict, dest: Path, extract_timeout: int,
                  solve_timeout: int, with_msolve: bool) -> dict:
    """Emit + extract + msolve screen + exact-Q. Mixed never DEAD by order."""
    dest = dest.resolve()
    cid = entry["class_id"]
    if entry.get("n_uneg"):
        cert = CS.write_certificate(
            dest / "classes" / cid / "certificate.json",
            annotate_certificate(dict(
                class_id=cid, class_verdict="OPEN",
                reason="U-NEGATIVE_no_honest_chart",
                n_unknowns=entry.get("nunk"), kind=entry.get("kind"),
                stems=[], note=(
                    "V'_2 > K': no honest source-complete chart is emitted "
                    "(scope-leaks / Def 5.1(1)). Not a Groebner DEAD."
                ),
            ), entry),
        )
        return cert
    emitted = CS.emit_order_class(entry, dest, support="source-complete")
    if not emitted.get("ok"):
        cert = CS.write_certificate(
            dest / "classes" / cid / "certificate.json",
            annotate_certificate(dict(
                class_id=cid, class_verdict="OPEN",
                reason=emitted.get("reason"), n_unknowns=entry.get("nunk"),
                kind=entry.get("kind"), stems=[]), entry),
        )
        return cert
    class_dir = Path(emitted["dest"])
    union_stem = emitted["union_stem"]
    t0 = time.time()
    extract_u = CS.extract_stem(class_dir, union_stem, extract_timeout)
    msolve_u = None
    union_result = None
    if extract_u.get("ok") and with_msolve:
        print("msolve-screen", cid, flush=True)
        msolve_u = _msolve_screen(class_dir, union_stem, min(solve_timeout, 300))
        print("  msolve", msolve_u.get("status") or msolve_u.get("reason"),
              "unit_signal", msolve_u.get("unit_signal"), flush=True)
    if extract_u.get("ok"):
        print("exact-Q", cid, flush=True)
        union_result = CS.solve_rows_guided(
            class_dir, union_stem, solve_timeout, characteristic=0)
        if msolve_u is not None:
            union_result["msolve_p32003"] = msolve_u
        print("  exact-Q", union_result.get("verdict"),
              "unit", union_result.get("unit"),
              "dim", union_result.get("dimension"),
              "elapsed", union_result.get("elapsed_seconds"), flush=True)
    kind = entry.get("kind") or "unsplit"
    jac_zero = bool(
        extract_u.get("ok")
        and extract_u.get("declared_equations") == 1
        and union_result and union_result.get("equations") == 1
        and CS.stem_verdict(union_result) == "UNIT"
    )
    if extract_u.get("ok") and union_result and CS.stem_verdict(union_result) == "UNIT":
        if kind in ("split", "mixed"):
            class_v = "OPEN"
            note = (
                "unsplit/order chart is UNIT (exact Q), but this class has a "
                "nonempty split window: split fibres recorded OPEN with "
                "(rho,lambda) leaf count %s. Not promoted to class DEAD."
                % (entry.get("split_survivor_count"),)
            )
        else:
            class_v = "DEAD"
            note = (
                "union UNIT implies every unsplit fibre UNIT. "
                + ("Jacobian identically 0 on the D1 support; J=c impossible."
                   if jac_zero else
                   "full necessary order chart, exact-Q unit.")
            )
        cert = CS.write_certificate(class_dir / "certificate.json",
            annotate_certificate(dict(
                class_id=cid, kind=kind,
                chart_kind="order_source_complete_union",
                n_unknowns=union_result.get("unknowns"),
                class_verdict=class_v,
                stems=[union_result],
                union=union_result,
                extract=extract_u,
                msolve_screen=msolve_u,
                jacobian_identically_zero=jac_zero,
                note=note,
                exact_q=True,
                unsplit_order_unit=True,
                wall_seconds=round(time.time() - t0, 3),
            ), entry))
        return cert
    stem_results = []
    if union_result is not None:
        stem_results.append(union_result)
    # fibre_size 1: union IS the fibre. Extra fibre solve would double the wall.
    if int(emitted.get("fibre_size") or 0) > 1:
        for stem in emitted["stems"]:
            ex = CS.extract_stem(class_dir, stem, extract_timeout)
            if not ex.get("ok"):
                stem_results.append(dict(
                    stem=stem,
                    verdict="TIMEOUT" if ex.get("timed_out") else "OPEN",
                    extract=ex))
                continue
            solved = CS.solve_rows_guided(
                class_dir, stem, solve_timeout, characteristic=0)
            solved["extract"] = ex
            stem_results.append(solved)
    verdict = CS.class_verdict(stem_results) if stem_results else (
        "TIMEOUT" if extract_u.get("timed_out") else "OPEN")
    if kind in ("split", "mixed") and verdict == "DEAD":
        verdict = "OPEN"
    cert = CS.write_certificate(class_dir / "certificate.json",
        annotate_certificate(dict(
            class_id=cid, kind=kind,
            chart_kind="order_source_complete",
            n_unknowns=entry.get("nunk"),
            class_verdict=verdict,
            stems=stem_results,
            union=union_result,
            extract_union=extract_u,
            msolve_screen=msolve_u,
            fibre_size=emitted.get("fibre_size"),
            exact_q=any(r.get("characteristic") == 0 and r.get("unit")
                        for r in stem_results),
            wall_seconds=round(time.time() - t0, 3),
            note=(
                "NON_EMPTY is not a counterexample unless a point with J=const "
                "lifts. TIMEOUT at this size is the compute-bound threshold. "
                "msolve modular [1] is a screen only."
            ),
        ), entry))
    return cert


def run_controls(timeout: int = 180) -> dict:
    dest = DEST.resolve()
    dest.mkdir(parents=True, exist_ok=True)
    results = {}
    print("control tame automorphism", flush=True)
    results["tame"] = CS.tame_automorphism_control(dest)
    print("  -> survives", results["tame"].get("survives"), flush=True)

    # two J≡0 controls: replay through census_sweep.run_class on the same
    # source-complete order chart that the census-sweep lane certified.
    inventory = json.loads((CENSUS_DEST / "inventory.json").read_text())
    by_id = {c["class_id"]: c for c in inventory["classes"]}
    for cid, label in ((J0_A, "J0_A"), (J0_B, "J0_B")):
        print("control", label, cid, flush=True)
        entry = by_id[cid]
        # run into controls/ so they are not mixed with operative classes
        ctrl_dest = dest / "controls" / cid
        ctrl_dest.mkdir(parents=True, exist_ok=True)
        # run_class writes dest/classes/<id>; use a nested dest whose
        # classes/ lives under controls/<id>_run
        run_dest = dest / "controls" / (cid + "_run")
        run_dest.mkdir(parents=True, exist_ok=True)
        cert = CS.run_class(
            run_dest, entry,
            extract_timeout=timeout,
            solve_timeout=timeout,
            support="source-complete",
            with_msolve=False,
            primes=(),
        )
        jac = cert.get("jacobian_identically_zero")
        unit = cert.get("class_verdict") == "DEAD"
        results[label] = dict(
            class_id=cid,
            class_verdict=cert.get("class_verdict"),
            jacobian_identically_zero=jac,
            n_unknowns=cert.get("n_unknowns"),
            exact_q=cert.get("exact_q"),
            ok=bool(unit and jac),
            certificate=cert,
        )
        print("  ->", cert.get("class_verdict"), "jac0=", jac, flush=True)

    failed = []
    if not results["tame"].get("survives"):
        failed.append("tame")
    if not results["J0_A"].get("ok"):
        failed.append("J0_A")
    if not results["J0_B"].get("ok"):
        failed.append("J0_B")
    summary = dict(
        passed=not failed,
        failed=failed,
        tame_survives=bool(results["tame"].get("survives")),
        J0_A= {k: results["J0_A"][k] for k in (
            "class_id", "class_verdict", "jacobian_identically_zero",
            "n_unknowns", "ok") if k in results["J0_A"]},
        J0_B= {k: results["J0_B"][k] for k in (
            "class_id", "class_verdict", "jacobian_identically_zero",
            "n_unknowns", "ok") if k in results["J0_B"]},
    )
    CS.atomic_json(dest / "controls" / "summary.json", summary)
    print("CONTROLS", json.dumps(summary, indent=2), flush=True)
    return summary


def ssh(ip: str, remote: str, timeout: int = 30) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["ssh", *SSH_OPTS, "ubuntu@%s" % ip, remote],
        text=True, capture_output=True, timeout=timeout,
    )


def launch_remote(ip: str, dest: Path, class_id: str,
                  extract_timeout: int, solve_timeout: int) -> dict:
    class_dir = dest / "classes" / class_id
    ssh(ip, "mkdir -p %s/classes/%s" % (REMOTE_DEST, class_id), timeout=20)
    subprocess.run(
        ["rsync", "-az", "-e", "ssh %s" % " ".join(SSH_OPTS),
         "%s/" % class_dir,
         "ubuntu@%s:%s/classes/%s/" % (ip, REMOTE_DEST, class_id)],
        check=True,
    )
    log = "~/operative-sweep-%s.log" % class_id
    wall = extract_timeout + solve_timeout + 90
    cmd = (
        "cd %s && mkdir -p %s && setsid bash -c "
        "'timeout %d python3 -u box/operative-sweep-20260905/run.py run-class "
        "--class-id %s --extract-timeout %d --solve-timeout %d --msolve "
        "> %s 2>&1' </dev/null >/dev/null 2>&1 & echo LAUNCHED pid=$!"
        % (REMOTE_ROOT, REMOTE_DEST, wall, class_id,
           extract_timeout, solve_timeout, log)
    )
    proc = ssh(ip, cmd, timeout=25)
    return dict(ip=ip, class_id=class_id, stdout=proc.stdout,
                stderr=proc.stderr, returncode=proc.returncode, log=log)


def poll_remote(ip: str, class_id: str) -> dict:
    remote = (
        "python3 - <<'PY'\n"
        "import json, os\n"
        "p=os.path.expanduser('~/jc2/box/operative-sweep-20260905/classes/%s/certificate.json')\n"
        "print('CERT', int(os.path.isfile(p)))\n"
        "if os.path.isfile(p):\n"
        "    print(open(p).read())\n"
        "PY\n"
        "echo RUNNING $(pgrep -c -f 'run.py run-class' || true)\n"
        "echo LOGTAIL; tail -5 ~/operative-sweep-%s.log 2>/dev/null || true\n"
        % (class_id, class_id)
    )
    proc = ssh(ip, remote, timeout=25)
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
    import re
    m = re.search(r"RUNNING\s+(\d+)", text)
    if m:
        running = int(m.group(1)) > 0
    return dict(ip=ip, class_id=class_id, certificate=cert,
                running=running, raw=text[-2000:])


def pull_remote(ip: str, dest: Path, class_id: str) -> None:
    target = dest / "classes" / class_id
    target.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["rsync", "-az", "-e", "ssh %s" % " ".join(SSH_OPTS),
         "ubuntu@%s:%s/classes/%s/" % (ip, REMOTE_DEST, class_id),
         "%s/" % target],
        check=False,
    )


def push_libs(ip: str) -> None:
    """Sync the frozen pipeline and this driver onto a worker."""
    pairs = [
        (LIB / "census_sweep.py", "box/lib/census_sweep.py"),
        (LIB / "guided_gb.py", "box/lib/guided_gb.py"),
        (LIB / "split_window.py", "box/lib/split_window.py"),
        (LIB / "builder_fix.py", "box/lib/builder_fix.py"),
        (DEST / "run.py", "box/operative-sweep-20260905/run.py"),
        (DEST / "inventory.json", "box/operative-sweep-20260905/inventory.json"),
    ]
    ssh(ip, "mkdir -p %s/box/lib %s/box/operative-sweep-20260905" % (
        REMOTE_ROOT, REMOTE_ROOT), timeout=20)
    for local, remote in pairs:
        if not local.is_file():
            continue
        subprocess.run(
            ["rsync", "-az", "-e", "ssh %s" % " ".join(SSH_OPTS),
             str(local), "ubuntu@%s:%s/%s" % (ip, REMOTE_ROOT, remote)],
            check=True,
        )


def cmd_run_class(args: argparse.Namespace) -> int:
    dest = DEST.resolve()
    inventory = load_inventory()
    entry = None
    for tier in TIERS:
        for cls in inventory["classes_by_tier"][tier]:
            if cls["class_id"] == args.class_id:
                entry = cls
                break
        if entry:
            break
    if entry is None:
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
                split_survivor_count=data.get("split_survivor_count") or 0,
                split_leaves=data.get("split_leaves") or [],
                window=data.get("window") or [],
                tier=data.get("tier"),
            )
        else:
            raise SystemExit("unknown class %s" % args.class_id)
    cert = run_one_class(
        entry, dest,
        extract_timeout=args.extract_timeout,
        solve_timeout=args.solve_timeout,
        with_msolve=args.msolve,
    )
    print(json.dumps(cert, indent=2, default=CS.jdefault))
    return 0


def cmd_inventory(_args: argparse.Namespace) -> int:
    DEST.mkdir(parents=True, exist_ok=True)
    build_inventory()
    return 0


def cmd_controls(args: argparse.Namespace) -> int:
    DEST.mkdir(parents=True, exist_ok=True)
    summary = run_controls(timeout=args.timeout)
    return 0 if summary.get("passed") else 1


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="operative_sweep")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("inventory")
    p.set_defaults(func=cmd_inventory)
    p = sub.add_parser("controls")
    p.add_argument("--timeout", type=int, default=180)
    p.set_defaults(func=cmd_controls)
    p = sub.add_parser("run-class")
    p.add_argument("--class-id", required=True)
    p.add_argument("--extract-timeout", type=int, default=300)
    p.add_argument("--solve-timeout", type=int, default=300)
    p.add_argument("--msolve", action="store_true")
    p.set_defaults(func=cmd_run_class)
    p = sub.add_parser("list-sweep")
    p.add_argument("--max-unknowns", type=int, default=100)
    p.set_defaults(func=cmd_list_sweep)
    return ap


def cmd_list_sweep(args: argparse.Namespace) -> int:
    inventory = load_inventory()
    selected = selected_for_sweep(inventory, args.max_unknowns)
    print("selected", len(selected), "nunk<=", args.max_unknowns, flush=True)
    for cls in selected:
        print("%s nunk=%s kind=%s tier=%s fibre=%d engine=%s leaves=%s"
              % (cls["class_id"], cls["nunk"], cls["kind"], cls["tier"],
                 cls["fibre_size"], cls["engine"], cls.get("split_survivor_count")),
              flush=True)
    return 0


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
