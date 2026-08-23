#!/usr/bin/env python3
# INTERNAL TOOLING, UNREVIEWED -- JC2 campaign ops (2026-08-18).
# msolve -v2 telemetry parser / lane progress reader. stdlib only, read-only.
#
# msolve writes -v2 telemetry to STDERR: launch lanes as
#     msolve -g 2 -v 2 -t 8 -f sys.ms -o sys.out 2> sys.v2log
# Run this tool on the box against the live .v2log (safe: it only reads),
# or scp -p the log down (plain scp resets mtime; age readouts then lie).
#
# Format knowledge is derived from actual msolve 0.10.1 -v2 logs
# (ops/telemetry_samples/), not from documentation. Anything unrecognized
# is counted as unknown-class, never silently dropped: --gates reports the
# unknown fraction per file.
#
# Modes:
#   --status  LOG          current phase, rounds, matrix trajectory, honest
#                          progress read (NO-ETA-POSSIBLE when trajectory
#                          does not support extrapolation)
#   --compare LOG1 LOG2    align two lanes' F4 trajectories (cross-prime
#                          divergence on near-identical systems is signal)
#   --gates  [LOGS...]     parse-completeness + truncation-tolerance gates
#                          over sample logs (default ops/telemetry_samples/)

import argparse
import glob
import math
import os
import re
import sys
import time
from collections import Counter
from dataclasses import dataclass, field
from statistics import median

# ---------------------------------------------------------------- patterns

RE_DASHES = re.compile(r"^-{6,}\s*$")
RE_TITLED = re.compile(r"^-+\s*([A-Z][A-Z ]+[A-Z])\s*-+$")
RE_SEED = re.compile(r"^Initial seed for pseudo-random number generator is\s+(\d+)\s*$")
RE_LEGEND_TITLE = re.compile(r"^Legend for f4 information\s*$")
RE_F4_HEADER = re.compile(r"^deg\s+sel\s+pairs\s+mat\s+density\s+new data\s+time\(rd\)")

# F4 round rows are written progressively: "deg sel pairs" at selection,
# "R x C" after symbolic preprocessing, "d%" with it, "N new M zero" after
# linear algebra, times at round end. A live log's last row may stop after
# any of these stages; parse whatever prefix is present.
RE_ROW_FULL = re.compile(
    r"^\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*x\s*(\d+)\s+([\d.]+)%"
    r"\s+(\d+)\s+new\s+(\d+)\s+zero\s+([\d.]+)\s*\|\s*([\d.]+)\s*$"
)
RE_ROW_NEWDATA = re.compile(
    r"^\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*x\s*(\d+)\s+([\d.]+)%"
    r"\s+(\d+)\s+new(?:\s+(\d+)\s+zero)?\s*$"
)
RE_ROW_DENSITY = re.compile(
    r"^\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*x\s*(\d+)\s+([\d.]+)%?\s*$"
)
RE_ROW_MAT = re.compile(r"^\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*x(?:\s*(\d+))?\s*$")
RE_ROW_SEL = re.compile(r"^\s*(\d+)(?:\s+(\d+))?(?:\s+(\d+))?\s*$")

RE_REDUCE_FINAL = re.compile(
    r"^reduce final basis\s+(\d+)\s*x\s*(\d+)\s+([\d.]+)%"
    r"\s+(\d+)\s+new\s+(\d+)\s+zero\s+([\d.]+)\s*\|\s*([\d.]+)\s*$"
)
RE_TIMING_KV = re.compile(r"^([A-Za-z][A-Za-z ().]*?)\s{2,}([\d.]+)\s+sec(?:\s+([\d.]+)%)?\s*$")
RE_GENERIC_KV = re.compile(r"^(#?[A-Za-z][^\s].*?)\s{2,}(\S.*?)\s*$")
RE_OVERALL = re.compile(
    r"^msolve overall time\s+([\d.]+)\s+sec \(elapsed\) / ([\d.]+)\s+sec \(cpu\)\s*$"
)
# FGLM / change-of-order markers: NOT present in our -g 2 sample logs, so
# recognized only by conservative keywords; format remains unverified.
RE_FGLM = re.compile(r"(?i)\bfglm\b|change of order|change-of-order|multiplication matri")

STAGES = ("selected", "matrix", "density", "linalg", "done")


@dataclass
class Round:
    idx: int              # 1-based F4 round number in log order
    lineno: int
    deg: int
    sel: int = None
    pairs: int = None
    rows: int = None
    cols: int = None
    density: float = None
    new: int = None
    zero: int = None
    t_real: float = None
    t_cpu: float = None
    stage: str = "selected"

    @property
    def complete(self):
        return self.stage == "done"

    def skey(self):
        return (self.deg, self.sel, self.pairs, self.rows, self.cols)


@dataclass
class LaneLog:
    path: str
    seed: int = None
    input_data: dict = field(default_factory=dict)
    rounds: list = field(default_factory=list)
    reduce_final: dict = None
    timings: dict = field(default_factory=dict)
    comp_data: dict = field(default_factory=dict)
    overall_real: float = None
    overall_cpu: float = None
    finished: bool = False
    fglm_lines: list = field(default_factory=list)
    line_classes: Counter = field(default_factory=Counter)
    unknown_lines: list = field(default_factory=list)
    total_lines: int = 0

    @property
    def completed_rounds(self):
        return [r for r in self.rounds if r.complete]

    @property
    def live_round(self):
        """Trailing partial round of a not-finished log, else None."""
        if self.rounds and not self.rounds[-1].complete and not self.finished:
            return self.rounds[-1]
        return None


# ---------------------------------------------------------------- parser

def parse_lane_log(text, path="<mem>"):
    """Parse msolve -v2 telemetry. Tolerant of truncated / live files:
    never raises on partial content; unrecognized lines are counted."""
    log = LaneLog(path=path)
    block = None          # None | input | legend_wait | legend | timings | compdata
    in_f4 = False
    ridx = 0

    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip("\n")
        log.total_lines += 1
        cls = None
        s = line.strip()

        if not s:
            cls = "blank"
            log.line_classes[cls] += 1
            continue

        m = RE_TITLED.match(s)
        if m and not RE_DASHES.match(s):
            title = m.group(1).strip()
            cls = "section-title"
            if title == "INPUT DATA":
                block = "input"
            elif title == "TIMINGS":
                block, in_f4 = "timings", False
            elif title == "COMPUTATIONAL DATA":
                block, in_f4 = "compdata", False
            log.line_classes[cls] += 1
            continue

        if RE_DASHES.match(s):
            cls = "delim"
            if block == "legend_wait":
                block = "legend"
            elif block in ("legend", "input", "timings", "compdata"):
                block = None
            log.line_classes[cls] += 1
            continue

        if block == "legend":
            log.line_classes["legend-body"] += 1
            continue

        m = RE_SEED.match(s)
        if m:
            log.seed = int(m.group(1))
            log.line_classes["seed"] += 1
            continue

        if RE_LEGEND_TITLE.match(s):
            block = "legend_wait"
            log.line_classes["legend-title"] += 1
            continue

        if RE_F4_HEADER.match(s):
            in_f4 = True
            log.line_classes["f4-header"] += 1
            continue

        m = RE_REDUCE_FINAL.match(s)
        if m:
            g = m.groups()
            log.reduce_final = dict(
                rows=int(g[0]), cols=int(g[1]), density=float(g[2]),
                new=int(g[3]), zero=int(g[4]),
                t_real=float(g[5]), t_cpu=float(g[6]))
            in_f4 = False
            log.line_classes["reduce-final"] += 1
            continue

        m = RE_OVERALL.match(s)
        if m:
            log.overall_real, log.overall_cpu = float(m.group(1)), float(m.group(2))
            log.finished = True
            log.line_classes["overall"] += 1
            continue

        if block == "input":
            m = RE_GENERIC_KV.match(s)
            if m:
                log.input_data[m.group(1).strip()] = m.group(2).strip()
                log.line_classes["input-kv"] += 1
                continue

        if block == "timings":
            m = RE_TIMING_KV.match(s)
            if m:
                log.timings[m.group(1).strip()] = (
                    float(m.group(2)),
                    float(m.group(3)) if m.group(3) else None)
                log.line_classes["timing-kv"] += 1
                continue

        if block == "compdata":
            m = RE_GENERIC_KV.match(s)
            if m:
                log.comp_data[m.group(1).strip()] = m.group(2).strip()
                log.line_classes["compdata-kv"] += 1
                continue

        if in_f4:
            m = RE_ROW_FULL.match(line)
            if m:
                g = m.groups()
                ridx += 1
                log.rounds.append(Round(
                    idx=ridx, lineno=lineno, deg=int(g[0]), sel=int(g[1]),
                    pairs=int(g[2]), rows=int(g[3]), cols=int(g[4]),
                    density=float(g[5]), new=int(g[6]), zero=int(g[7]),
                    t_real=float(g[8]), t_cpu=float(g[9]), stage="done"))
                log.line_classes["f4-round"] += 1
                continue
            for rex, stage in ((RE_ROW_NEWDATA, "linalg"),
                               (RE_ROW_DENSITY, "density"),
                               (RE_ROW_MAT, "matrix"),
                               (RE_ROW_SEL, "selected")):
                m = rex.match(line)
                if m:
                    g = [int(x) if x and "." not in x else x for x in m.groups()]
                    ridx += 1
                    r = Round(idx=ridx, lineno=lineno, deg=g[0], stage=stage)
                    if len(g) > 1 and g[1] is not None:
                        r.sel = g[1]
                    if len(g) > 2 and g[2] is not None:
                        r.pairs = g[2]
                    if stage in ("matrix", "density", "linalg"):
                        r.rows = g[3]
                        r.cols = g[4] if g[4] is not None else None
                    if stage in ("density", "linalg") and len(g) > 5 and g[5] is not None:
                        r.density = float(g[5])
                    if stage == "linalg":
                        r.new = g[6]
                        r.zero = g[7] if len(g) > 7 and g[7] is not None else None
                    log.rounds.append(r)
                    log.line_classes["f4-partial"] += 1
                    break
            if m:
                continue

        if RE_FGLM.search(s):
            log.fglm_lines.append((lineno, s))
            log.line_classes["fglm-marker"] += 1
            continue

        log.line_classes["unknown"] += 1
        log.unknown_lines.append((lineno, line))

    return log


def load(path):
    with open(path, "r", errors="replace") as fh:
        return parse_lane_log(fh.read(), path=path)


# ---------------------------------------------------------------- analysis

def fmt_t(sec):
    if sec is None:
        return "?"
    if sec < 120:
        return f"{sec:.2f} s"
    if sec < 7200:
        return f"{sec:.0f} s ({sec / 60:.1f} min)"
    return f"{sec:.0f} s ({sec / 3600:.2f} h)"


def fmt_mat(r):
    if r.rows is None:
        return "(not yet printed)"
    c = f"{r.cols}" if r.cols is not None else "?"
    d = f" {r.density:.2f}%" if r.density is not None else ""
    return f"{r.rows} x {c}{d}"


def degree_ladder(rounds):
    """[(deg, round_idx first reaching that running-max degree)]"""
    out, cur = [], -1
    for r in rounds:
        if r.deg is not None and r.deg > cur:
            cur = r.deg
            out.append((cur, r.idx))
    return out


def trailing_drops(vals):
    """Length of the strictly-decreasing run ending at vals[-1]."""
    k = 0
    for i in range(len(vals) - 1, 0, -1):
        if vals[i] < vals[i - 1]:
            k += 1
        else:
            break
    return k


def analyze(log, window=8):
    """Monotonicity-based progress read. Returns dict; never fabricates:
    eta is None unless a drain regime (monotone pair-list contraction)
    justifies extrapolation, and even then it is labeled ROUGH."""
    a = {"phase": None, "reasons": [], "eta": None, "drain": False}
    comp = log.completed_rounds
    live = log.live_round

    if log.finished:
        a["phase"] = "FINISHED"
    elif log.comp_data or log.timings:
        a["phase"] = "terminal accounting blocks (F4 done, run wrapping up)"
    elif log.reduce_final:
        a["phase"] = "final basis reduction done; timing blocks pending"
    elif live:
        stage_txt = {
            "selected": "pairs selected; matrix dims not yet printed -> "
                        "symbolic preprocessing / matrix construction",
            "matrix": "matrix built; density pending",
            "density": "matrix built -> linear algebra in progress",
            "linalg": "linear algebra done; round timing pending",
        }[live.stage]
        a["phase"] = (f"F4 round {live.idx} IN PROGRESS at deg {live.deg} "
                      f"({stage_txt})")
    elif log.rounds:
        a["phase"] = (f"F4 after round {log.rounds[-1].idx} "
                      "(next selection not yet in log)")
    elif log.input_data:
        a["phase"] = "startup: input read, F4 not started"
    else:
        a["phase"] = "startup: no telemetry yet"
    if log.fglm_lines:
        a["phase"] += " [FGLM/change-of-order markers present]"

    a["ladder"] = degree_ladder(log.rounds)
    if a["ladder"]:
        maxdeg, first_idx = a["ladder"][-1]
        a["maxdeg"] = maxdeg
        a["plateau_rounds"] = (log.rounds[-1].idx - first_idx)
        a["plateau_time"] = sum(r.t_real for r in comp if r.idx >= first_idx)
    if not comp:
        a["reasons"].append("no completed F4 rounds yet")
        return a

    tail = comp[-min(window, len(comp)):]
    pairs_seq = [r.pairs for r in tail]
    a["pairs_seq"] = pairs_seq
    drops = trailing_drops(pairs_seq)
    rows_tail = [r.rows for r in tail]
    half = len(rows_tail) // 2
    rows_up = (half > 0 and median(rows_tail[half:]) > median(rows_tail[:half]))

    if log.finished:
        return a

    drain = drops >= 5 or (drops >= 3 and pairs_seq[-1] <= 50)
    if live and live.pairs is not None and pairs_seq and live.pairs > pairs_seq[-1]:
        drain = False  # live selection shows the pair list grew again
    a["drain"] = drain
    if drain:
        run = pairs_seq[-(drops + 1):]
        per_round = (run[0] - run[-1]) / drops
        rounds_left = max(1, math.ceil(pairs_seq[-1] / per_round))
        recent_t = [r.t_real for r in tail[-(drops + 1):] if r.t_real is not None]
        a["eta"] = (rounds_left,
                    rounds_left * median(recent_t),
                    rounds_left * max(recent_t))
    else:
        if drops < 5:
            a["reasons"].append(
                f"pair list not draining: last {len(pairs_seq)} completed rounds "
                f"go {pairs_seq[0]} -> {pairs_seq[-1]} "
                f"(only {drops} consecutive drop(s) at tail)")
        if live and live.pairs is not None:
            a["reasons"].append(
                f"live round selected at pair-list size {live.pairs} "
                "(list still growing)")
        if "maxdeg" in a and a.get("plateau_rounds", 0) >= 3:
            a["reasons"].append(
                f"degree plateau: max deg {a['maxdeg']} unchanged for "
                f"{a['plateau_rounds']} rounds "
                f"({fmt_t(a['plateau_time'])} of round time) -- new-degree "
                "jumps remain possible; no monotone degree signal")
        if rows_up:
            a["reasons"].append("matrix sizes still trending up over the window")
    return a


# ---------------------------------------------------------------- --status

def render_status(log, window=8, now=None):
    out = []
    p = out.append
    p(f"LANE STATUS  {log.path}   [INTERNAL TOOLING, UNREVIEWED]")
    if os.path.exists(log.path):
        mt = os.path.getmtime(log.path)
        age = (now or time.time()) - mt
        p(f"  log mtime : {time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(mt))}"
          f"  ({fmt_t(age)} since last telemetry write; trustworthy only "
          "on-box or after scp -p)")
    idata = log.input_data
    if idata:
        p(f"  system    : {idata.get('#variables', '?')} vars / "
          f"{idata.get('#equations', '?')} eqs, char {idata.get('field characteristic', '?')}, "
          f"threads {idata.get('#threads', '?')}, order {idata.get('monomial order', '?')}"
          + (f", seed {log.seed}" if log.seed else ""))
    a = analyze(log, window=window)
    p(f"  phase     : {a['phase']}")
    comp = log.completed_rounds
    tsum = sum(r.t_real for r in comp)
    p(f"  rounds    : {len(comp)} completed"
      + (f" + 1 in progress" if log.live_round else "")
      + f"; sum of round wall time {fmt_t(tsum)}"
      " (time(rd) includes symbolic prep, so this approximates elapsed)")
    if a.get("ladder"):
        lad = " ".join(f"d{d}@r{i}" for d, i in a["ladder"])
        p(f"  deg ladder: {lad}   (first round reaching each new max degree)")
    if comp:
        p(f"  trajectory (last {min(window, len(comp))} completed rounds):")
        p("      rnd  deg      sel        pairs                 matrix    density"
          "      new     zero        t_real")
        for r in comp[-window:]:
            p(f"    {r.idx:5d} {r.deg:4d} {r.sel:8d} {r.pairs:12d} "
              f"{r.rows:10d} x {r.cols:<10d} {r.density:7.2f}% {r.new:8d} "
              f"{r.zero:8d} {r.t_real:13.2f}")
        big = max(comp, key=lambda r: r.rows * r.cols)
        p(f"  largest matrix so far: {fmt_mat(big)} at deg {big.deg} "
          f"(round {big.idx}, {fmt_t(big.t_real)})")
    live = log.live_round
    if live:
        p(f"  live round: r{live.idx} deg {live.deg}"
          + (f", sel {live.sel}" if live.sel is not None else "")
          + (f" of {live.pairs} pairs" if live.pairs is not None else "")
          + (f", matrix {fmt_mat(live)}" if live.rows is not None else "")
          + f"  [stage: {live.stage}]")
        prec = [r for r in comp if r.deg == live.deg]
        if prec:
            q = prec[-1]
            p(f"    nearest precedent (last completed deg-{live.deg} round r{q.idx}): "
              f"sel {q.sel} -> {fmt_mat(q)}, {fmt_t(q.t_real)}")
    if log.reduce_final:
        rf = log.reduce_final
        p(f"  reduce final basis: {rf['rows']} x {rf['cols']} {rf['density']:.2f}%, "
          f"{rf['new']} new, {fmt_t(rf['t_real'])}")
    if log.finished:
        p(f"  FINISHED: overall {fmt_t(log.overall_real)} elapsed / "
          f"{fmt_t(log.overall_cpu)} cpu"
          + (f"; basis size {log.comp_data.get('size of basis')}"
             if log.comp_data else ""))
        if log.timings:
            sp = log.timings.get("symbolic prep.")
            la = log.timings.get("linear algebra")
            if sp and la:
                p(f"  time split: symbolic prep {sp[1]:.1f}%, linear algebra {la[1]:.1f}%")
    elif a["eta"]:
        rl, lo, hi = a["eta"]
        p(f"  progress  : DRAIN REGIME -- pair list monotonically contracting "
          f"({' -> '.join(str(x) for x in a['pairs_seq'])})")
        p(f"  ROUGH ETA : ~{rl} more rounds; {fmt_t(lo)} .. {fmt_t(hi)} of round "
          "time IF drain continues at recent rate. A new degree jump voids "
          "this; treat as best-case, not a promise.")
    else:
        p("  progress  : NO-ETA-POSSIBLE -- trajectory does not support "
          "extrapolation. Refusing to fabricate one.")
        for rs in a["reasons"]:
            p(f"      - {rs}")
    if log.unknown_lines:
        p(f"  NOTE: {len(log.unknown_lines)} unrecognized line(s) "
          f"(of {log.total_lines}); first: "
          f"line {log.unknown_lines[0][0]}: {log.unknown_lines[0][1][:70]!r}")
    return "\n".join(out)


# ---------------------------------------------------------------- --compare

def render_compare(la, lb, window=8):
    out = []
    p = out.append
    p(f"LANE COMPARE   A={la.path}   B={lb.path}   [INTERNAL TOOLING, UNREVIEWED]")
    for key in ("#variables", "#equations", "field characteristic", "#threads"):
        va, vb = la.input_data.get(key), lb.input_data.get(key)
        flag = "" if va == vb else "   <-- DIFFERS"
        p(f"  {key:22s} A={va}  B={vb}{flag}")
    same_sys = all(la.input_data.get(k) == lb.input_data.get(k)
                   for k in ("#variables", "#equations"))
    if not same_sys:
        p("  WARNING: different systems (vars/eqs differ); round alignment is "
          "not meaningful, structural comparison below is best-effort.")
    ra, rb = la.completed_rounds, lb.completed_rounds
    n = min(len(ra), len(rb))
    prefix = 0
    div = None
    for i in range(n):
        if ra[i].skey() == rb[i].skey():
            prefix += 1
        else:
            div = i
            break
    p(f"  completed rounds: A={len(ra)}  B={len(rb)}; structurally identical "
      f"prefix (deg,sel,pairs,mat): {prefix} rounds")
    if div is not None:
        x, y = ra[div], rb[div]
        p(f"  FIRST DIVERGENCE at round {div + 1}:")
        p(f"    A: deg {x.deg} sel {x.sel} pairs {x.pairs} mat {fmt_mat(x)} t {fmt_t(x.t_real)}")
        p(f"    B: deg {y.deg} sel {y.sel} pairs {y.pairs} mat {fmt_mat(y)} t {fmt_t(y.t_real)}")
        if same_sys:
            p("    (near-identical cross-prime lanes should not diverge "
              "structurally: divergence = prime-sensitive pivoting or an "
              "unlucky prime -- investigate before trusting either lane)")
    elif len(ra) != len(rb):
        ahead, nm = (la, "A") if len(ra) > len(rb) else (lb, "B")
        p(f"  no structural divergence; {nm} is {abs(len(ra) - len(rb))} "
          f"round(s) ahead")
        for r in ahead.completed_rounds[prefix:prefix + window]:
            p(f"    {nm} extra r{r.idx}: deg {r.deg} sel {r.sel} pairs {r.pairs} "
              f"mat {fmt_mat(r)} t {fmt_t(r.t_real)}")
    else:
        p("  no structural divergence and equal round counts")
    if prefix:
        ta = sum(r.t_real for r in ra[:prefix])
        tb = sum(r.t_real for r in rb[:prefix])
        ratio = f"{tb / ta:.2f}x" if ta > 0 else "n/a"
        p(f"  wall over common prefix: A {fmt_t(ta)}  B {fmt_t(tb)}  (B/A {ratio})")
        dens = [abs(ra[i].density - rb[i].density) for i in range(prefix)
                if ra[i].density is not None and rb[i].density is not None]
        if dens:
            p(f"  density drift over prefix: max abs diff {max(dens):.2f} pts")
    for nm, lg in (("A", la), ("B", lb)):
        av = analyze(lg, window=window)
        p(f"  {nm} phase: {av['phase']}")
    return "\n".join(out)


# ---------------------------------------------------------------- --gates

def run_gates(paths, window=8):
    ok = True
    print("TELEMETRY PARSER GATES   [INTERNAL TOOLING, UNREVIEWED]")
    if not paths:
        print("  FAIL: no sample logs found")
        return False
    for path in paths:
        with open(path, "r", errors="replace") as fh:
            text = fh.read()
        log = parse_lane_log(text, path=path)
        counted = sum(log.line_classes.values())
        unk = log.line_classes["unknown"]
        frac = unk / log.total_lines if log.total_lines else 0.0
        g_account = counted == log.total_lines
        g_unknown = frac <= 0.02
        g_input = "#variables" in log.input_data and "field characteristic" in log.input_data
        g_rounds = len(log.rounds) >= 1
        g_trailer = log.finished == (log.overall_real is not None)
        g_trunc = True
        for cut in (0.5, 0.75, 0.9, 0.98):
            try:
                sub = parse_lane_log(text[: int(len(text) * cut)], path=path)
                if len(sub.rounds) > len(log.rounds):
                    g_trunc = False
                render_status(sub, window=window)   # must not raise either
                analyze(sub, window=window)
            except Exception as e:                  # noqa: BLE001 -- gate must report, not die
                g_trunc = False
                print(f"    truncation@{cut}: EXCEPTION {e!r}")
        gates = {
            "line-accounting (parsed+unknown==total)": g_account,
            "unknown-fraction<=2%": g_unknown,
            "input-block-parsed": g_input,
            "f4-rounds-parsed": g_rounds,
            "finished-trailer-consistent": g_trailer,
            "truncation-tolerant": g_trunc,
        }
        st = "PASS" if all(gates.values()) else "FAIL"
        ok = ok and all(gates.values())
        ncomp = len(log.completed_rounds)
        print(f"  [{st}] {os.path.basename(path)}: {log.total_lines} lines, "
              f"unknown {unk} ({frac:.1%}); rounds {ncomp} completed"
              f"{' +1 partial' if log.rounds and not log.rounds[-1].complete else ''}"
              f"{', finished' if log.finished else ', truncated/live'}")
        clist = ", ".join(f"{k}={v}" for k, v in sorted(log.line_classes.items()))
        print(f"         classes: {clist}")
        for name, val in gates.items():
            if not val:
                print(f"         GATE FAIL: {name}")
        for lineno, line in log.unknown_lines[:5]:
            print(f"         unknown line {lineno}: {line[:78]!r}")
    print(f"GATES {'PASS' if ok else 'FAIL'}")
    return ok


# ---------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(
        description="msolve -v2 telemetry parser (INTERNAL TOOLING, UNREVIEWED). "
                    "Reads lane logs only; never touches running jobs.")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--status", metavar="LOG", help="progress read of one lane log")
    mode.add_argument("--compare", nargs=2, metavar=("LOG1", "LOG2"),
                      help="align two lanes' F4 trajectories")
    mode.add_argument("--gates", nargs="*", metavar="LOG",
                      help="parse-completeness gates over sample logs "
                           "(default: ops/telemetry_samples/*.v2log)")
    ap.add_argument("--window", type=int, default=8,
                    help="trailing-round window for trend reads (default 8)")
    args = ap.parse_args(argv)

    if args.status:
        print(render_status(load(args.status), window=args.window))
        return 0
    if args.compare:
        print(render_compare(load(args.compare[0]), load(args.compare[1]),
                             window=args.window))
        return 0
    paths = args.gates
    if not paths:
        here = os.path.dirname(os.path.abspath(__file__))
        paths = sorted(glob.glob(os.path.join(here, "telemetry_samples", "*.v2log")))
    return 0 if run_gates(paths, window=args.window) else 1


if __name__ == "__main__":
    sys.exit(main())
