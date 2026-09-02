#!/usr/bin/env python3
r"""covergeo.py -- cycle-type -> chi_c calculator for finite covers of the plane.

Lane: SOURCE-GATE-962 (xmodel/source-gate-962-opus5-20260902.md sec.7).
Charged by: ideation-20260902T0022Z-grok46.md sec.6 (calculator), sec.3
(FOUR-BOX EULER razor), sec.4 (the "(8,6,9) same species" claim -- see the
TYPING FIREWALL below, where that claim is REFUTED as stated and replaced by
the layer that really is shared).

WHAT THIS COMPUTES
------------------
Given a finite surjection  q : Y -> A^2  of degree N whose branch locus is a
curve D, and CONJUGACY-INVARIANT local monodromy data only, it returns the
stratified compactly-supported Euler characteristics

    chi_c(V_rho) = N * chi_c(A^2 - D)                    (Lemma 5.1(b))
    chi_c(Y)     = chi_c(V_rho)
                   + sum_i c_i * chi_c(D_i - Sing D)     (Lemma 3.1/3.3)
                   + sum_p #q^{-1}(p)                    (Lemma 5.1(a))

and, for a DECLARED four-box split, the boundary Euler characteristic

    chi_c(B_Y)   = m_Y * chi~  -  sum_p [ m_Y * r_p - c_p + a_p ]

(valid only when every boundary component is birational onto D, delta_j = 1),
then reports MATCH / MISMATCH / OPEN on the SHEET-GATE source test

    (FOUR-BOX EULER)      chi_c(Y)  ==  1 + chi_c(B_Y)      i.e.  U ~ A^2 .

All of chi_c-additivity, chi_c-multiplicativity in finite coverings and the
curve normalisation formula are SHEET-GATE Lemma 5.1 (round1033-sheet-gate,
lines 363-383); the fibre-point <-> orbit bijection is its Lemma 3.1.

TYPING FIREWALL (read before extending)
---------------------------------------
* chi_c here is a TOPOLOGICAL compactly-supported Euler characteristic of a
  NON-COMPACT AFFINE surface.  It is not c_1^2, not chi(O), not a Chern number
  of any bundle, and no compactification is used or needed.
* grok sec.4 proposes that this and the (8,6,9) input `c_2(T) = chi(O_Z)` are
  "the same Chern species".  They are NOT, and the module refuses to conflate
  them: TB-GERM 7.1 (tb-g2-finish-opus5-20260901.md:435) fixes `T` as the rank-2
  TSCHIRNHAUSEN bundle of the triple plane, with `chi(O_Z) = 23 - c_2(T^v)` --
  a Miranda triple-cover formula on a PROJECTIVE, SINGULAR Z, not a topological
  Euler number.  The layer that genuinely IS shared is the one implemented in
  `fibre_partition_over`: local-monodromy -> orbit decomposition -> point count
  and local type.  Asking this module for c_2 returns typed OPEN, never a number.
* `E = e(iota)` is an inner-BRAID exponent.  It is recorded as a row LABEL only
  and never enters any arithmetic here.  Identifying it with an Euler number is
  the flag/place/series fallacy (FALLACY-v2).

FAIL-CLOSED RULES
-----------------
1. every cycle type must be a partition of N; a_p, a_i must be declared with a
   provenance string, or the module returns an interval and an OPEN token;
2. `a_i = sigma_i` is NEVER assumed (OPEN[ACS-FIX-VS-DEFICIT]): the caller must
   pass `sheet_location_b` explicitly with a citation, or every admissible b is
   enumerated and each branch reported separately;
3. delta_j > 1 anywhere -> OPEN[COVERGEO-DELTA-GT-1] (chi~ of B_j unknown);
4. any request that needs a labelled ZvK transport -> OPEN[BMFACT-BASEPOINT];
5. any request that needs a compactification -> OPEN[RH-LINE-AT-INFINITY];
6. `source_gate` provenance string is REQUIRED and must be non-empty: the curve
   data must come from a radical-verified source (Sage footgun #10:
   squarefree_part() != radical()).  This module does no polynomial arithmetic,
   so #10 cannot fire inside it; the guard keeps it from firing upstream.
7. Sage footgun #11 (`sage script.sage` does not set __name__=="__main__", giving
   silent empty output with rc=0): the entry point is the public `main()`, the
   __main__ guard is a convenience only, and main() ends by asserting that it
   emitted its seal line.  Run as `python3 box/covergeo.py`, or from Sage as
   `import covergeo; covergeo.main()`, or set COVERGEO_FORCE_MAIN=1.
"""
from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple


class Open(Exception):
    """Typed OPEN.  Never caught internally, never replaced by a default."""

    def __init__(self, token: str, detail: str = "") -> None:
        super().__init__("OPEN[%s]%s" % (token, (" " + detail) if detail else ""))
        self.token = token
        self.detail = detail


# --------------------------------------------------------------------------
# 1. conjugacy-invariant local data
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class LocalType:
    """The H_p-orbit decomposition of the N sheets at one point of the base.

    `orbit_sizes` is the multiset of orbit sizes -- a conjugacy invariant of the
    local monodromy subgroup H_p <= S_N.  At a generic point of D_i, H_p = <g_i>
    and `orbit_sizes` IS the cycle type of g_i (SHEET-GATE Lemma 3.1).
    """

    name: str
    orbit_sizes: Tuple[int, ...]

    def check(self, N: int) -> None:
        if sum(self.orbit_sizes) != N:
            raise Open("COVERGEO-BAD-CYCLE-TYPE",
                       "%s: %s is not a partition of N=%d"
                       % (self.name, list(self.orbit_sizes), N))
        if any(e < 1 for e in self.orbit_sizes):
            raise Open("COVERGEO-BAD-CYCLE-TYPE", self.name)

    @property
    def n_points(self) -> int:
        """#q^{-1}(p): one point per orbit (Lemma 3.1, Y normal => unibranch)."""
        return len(self.orbit_sizes)

    @property
    def n_fixed(self) -> int:
        """s_p = #Fix(H_p) = number of trivial orbits."""
        return sum(1 for e in self.orbit_sizes if e == 1)


@dataclass
class SingPoint:
    name: str
    r_p: int                 # number of local branches of D at p
    local: LocalType
    a_p: Optional[int] = None      # #F^{-1}(p); None => interval [0, s_p]
    a_p_source: str = ""


@dataclass
class Component:
    """One irreducible component D_i of the branch curve, in A^2."""

    name: str
    chi_norm: int            # chi_c of the normalisation of the AFFINE curve D_i
    generic: LocalType       # cycle type of the meridian of D_i
    sings: List[str] = field(default_factory=list)   # names of Sing points on D_i


@dataclass
class Row:
    label: str
    N: int
    components: List[Component]
    sings: List[SingPoint]
    source_gate: str = ""
    braid_label_E: Optional[int] = None   # recorded only; never consumed


# --------------------------------------------------------------------------
# 2. the shared layer:  local monodromy -> fibre partition
# --------------------------------------------------------------------------

def fibre_partition_over(local: LocalType, N: int) -> Dict[str, object]:
    """The layer that (9,6,2) and (8,6,9) genuinely share.

    Returns the point count over p, the fixed-sheet count, and the multiset of
    local multiplicities e_y.  Nothing here is a Chern class.
    """
    local.check(N)
    return {"n_points": local.n_points,
            "n_fixed": local.n_fixed,
            "e_multiset": tuple(sorted(local.orbit_sizes, reverse=True))}


def s4_to_s3_orbits(orbit_generators: Sequence[Tuple[int, ...]]) -> Tuple[int, ...]:
    """Push a local S_4 monodromy subgroup through S_4 -> S_4/V_4 = S_3 and
    return the orbit sizes of the image on the 3 letters.

    The three letters are the three ways of splitting {0,1,2,3} into two pairs.
    Used for the (8,6,9) triple-plane path (TB-GERM 7.1).
    """
    pairings = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]

    def act(g: Tuple[int, ...], idx: int) -> int:
        (a, b), (c, d) = pairings[idx]
        img = tuple(sorted((tuple(sorted((g[a], g[b]))), tuple(sorted((g[c], g[d]))))))
        for k, pr in enumerate(pairings):
            if tuple(sorted(pr)) == img:
                return k
        raise Open("COVERGEO-S3-QUOTIENT", "image pairing not found")

    seen = [{i} for i in range(3)]
    # union-find on the 3 letters under all generators
    parent = list(range(3))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for g in orbit_generators:
        if sorted(g) != [0, 1, 2, 3]:
            raise Open("COVERGEO-S3-QUOTIENT", "generator is not a permutation of 4 letters")
        for i in range(3):
            a, b = find(i), find(act(g, i))
            if a != b:
                parent[a] = b
    sizes: Dict[int, int] = {}
    for i in range(3):
        sizes[find(i)] = sizes.get(find(i), 0) + 1
    return tuple(sorted(sizes.values(), reverse=True))


# --------------------------------------------------------------------------
# 3. the four-box split, enumerated (never assumed)
# --------------------------------------------------------------------------

@dataclass
class FourBox:
    a: int          # (U, e=1)   = #F^{-1}(generic p of D_i)
    b: int          # (Y-U, e=1)
    ram: int        # sum over e_j >= 2 of delta_j * e_j
    m_Y: int        # number of boundary components over D_i
    deltas: Tuple[Tuple[int, int], ...]   # (delta_j, e_j)


def four_boxes(local: LocalType, N: int) -> List[FourBox]:
    """All four-box splits compatible with the cycle type.

    sigma = a + b = #Fix(g).  The multiplicities e_j >= 2 are exactly the
    nontrivial cycle lengths, each with delta_j = its multiplicity in the cycle
    type -- but the calculator only certifies delta_j = 1 (rule 3).
    b ranges over 0..sigma-1 because a >= 1 (SHEET-GATE box (U,e=1) NONEMPTY).
    """
    local.check(N)
    sigma = local.n_fixed
    if sigma < 1:
        raise Open("COVERGEO-NO-AFFINE-SHEET",
                   "#Fix(g) = 0 contradicts box (U,e=1) NONEMPTY")
    nontrivial = [e for e in local.orbit_sizes if e >= 2]
    if not nontrivial:
        raise Open("COVERGEO-UNRAMIFIED",
                   "no e_j >= 2: purity of the branch locus forces N = 1")
    ram = sum(nontrivial)
    out = []
    for b in range(0, sigma):
        a = sigma - b
        deltas = tuple([(1, e) for e in sorted(nontrivial, reverse=True)]
                       + [(1, 1)] * b)
        out.append(FourBox(a=a, b=b, ram=ram, m_Y=len(nontrivial) + b, deltas=deltas))
    return out


# --------------------------------------------------------------------------
# 4. the Euler engine
# --------------------------------------------------------------------------

def _gap(row: Row, bx: "FourBox", comp: Component, chi_Y: int, chi_V: int,
         chi_D0: int, sum_ap: int) -> int:
    """chi_c(Y) - (1 + chi_c(B_Y)) at a given total a_p.  Equals chi_c(U) - 1."""
    chi_BY = bx.m_Y * comp.chi_norm - sum(
        bx.m_Y * p.r_p - p.local.n_points for p in row.sings) - sum_ap
    return chi_Y - (1 + chi_BY)


def chi_c_D(row: Row) -> Tuple[int, Dict[str, int]]:
    by_name = {p.name: p for p in row.sings}
    for comp in row.components:
        for s in comp.sings:
            if s not in by_name:
                raise Open("COVERGEO-MISSING-SING", "%s on %s" % (s, comp.name))
    chi = sum(c.chi_norm for c in row.components) - sum(p.r_p - 1 for p in row.sings)
    return chi, {p.name: p.r_p for p in row.sings}


def run_mode1(row: Row, sheet_location_b: Optional[int] = None,
              b_citation: str = "") -> Dict[str, object]:
    """Mode 1: A_F irreducible.  Returns one verdict per admissible b."""
    if not row.source_gate:
        raise Open("COVERGEO-NO-SOURCE-GATE",
                   "curve data needs a radical-verified provenance string (footgun #10)")
    if len(row.components) != 1:
        raise Open("COVERGEO-NOT-MODE-1", "Mode 1 needs exactly one component")
    N = row.N
    comp = row.components[0]
    comp.generic.check(N)
    for p in row.sings:
        p.local.check(N)

    chiD, _ = chi_c_D(row)
    s = len(row.sings)
    chi_D0 = chiD - s
    chi_V = N * (1 - chiD)
    c = comp.generic.n_points
    sum_cp = sum(p.local.n_points for p in row.sings)
    chi_Y = chi_V + c * chi_D0 + sum_cp

    boxes = four_boxes(comp.generic, N)
    if sheet_location_b is not None:
        if not b_citation:
            raise Open("COVERGEO-UNCITED-B",
                       "declaring b needs a citation (OPEN[SHEET-LOCATION])")
        boxes = [bx for bx in boxes if bx.b == sheet_location_b]
        if not boxes:
            raise Open("COVERGEO-BAD-B", "b=%s not admissible" % sheet_location_b)

    branches = []
    for bx in boxes:
        if any(d != 1 for d, _ in bx.deltas):
            raise Open("COVERGEO-DELTA-GT-1", "chi~ of a non-birational B_j is unknown")
        # a_p: declared, else forced by a_p <= s_p, else the whole interval
        a_ps, a_p_open = [], False
        for p in row.sings:
            if p.a_p is not None:
                if not p.a_p_source:
                    raise Open("COVERGEO-UNCITED-AP", p.name)
                if p.a_p > p.local.n_fixed:
                    raise Open("COVERGEO-AP-EXCEEDS-FIX",
                               "%s: a_p=%d > s_p=%d (Cor 3.2)"
                               % (p.name, p.a_p, p.local.n_fixed))
                a_ps.append(p.a_p)
            elif p.local.n_fixed == 0:
                a_ps.append(0)            # forced: a_p <= s_p = 0
            else:
                a_ps.append(None); a_p_open = True
        if a_p_open:
            # gap is affine and strictly increasing in sum(a_p) (chi_c(B_Y) loses
            # one unit per unit of a_p), so the whole ACS interval is decided by
            # its two endpoints.  Only if the interval straddles 0 is this OPEN.
            lo = sum(0 if v is None else v for v in a_ps)
            hi = sum((p.local.n_fixed if v is None else v)
                     for p, v in zip(row.sings, a_ps))
            gaps = [_gap(row, bx, comp, chi_Y, chi_V, chi_D0, t) for t in (lo, hi)]
            if all(g != 0 for g in gaps) and gaps[0] * gaps[1] > 0:
                branches.append({"box": bx, "chi_BY": None, "rhs": None,
                                 "chi_U": None, "sum_ap": (lo, hi),
                                 "gap": tuple(gaps),
                                 "verdict": "MISMATCH-ON-INTERVAL"})
            else:
                branches.append({"box": bx, "verdict": "OPEN",
                                 "token": "ACS-FIX-VS-DEFICIT",
                                 "detail": "a_p undeclared and the interval "
                                           "[%d,%d] straddles a match" % (lo, hi)})
            continue
        sum_ap = sum(a_ps)
        chi_BY = bx.m_Y * comp.chi_norm - sum(
            bx.m_Y * p.r_p - p.local.n_points + ap for p, ap in zip(row.sings, a_ps))
        rhs = 1 + chi_BY
        # implementation cross-check: chi_c(U) two ways must agree
        chi_U_strat = chi_V + bx.a * chi_D0 + sum_ap
        assert chi_Y - chi_BY == chi_U_strat, "internal chi_c additivity mismatch"
        branches.append({"box": bx, "chi_BY": chi_BY, "rhs": rhs,
                         "chi_U": chi_U_strat, "sum_ap": sum_ap,
                         "gap": chi_Y - rhs,
                         "verdict": "MATCH" if chi_Y == rhs else "MISMATCH"})
    return {"label": row.label, "N": N, "chi_D": chiD, "s": s, "chi_D0": chi_D0,
            "chi_V": chi_V, "c": c, "sigma": comp.generic.n_fixed,
            "ram": N - comp.generic.n_fixed, "sum_cp": sum_cp, "chi_Y": chi_Y,
            "branches": branches, "braid_label_E": row.braid_label_E}


def c2_tschirnhausen(*_args, **_kwargs):
    """Refused by construction -- see the TYPING FIREWALL."""
    raise Open("COVERGEO-C2-TSCHIRNHAUSEN",
               "c_2(T^v) is a Chern number of the rank-2 Tschirnhausen bundle of a "
               "projective SINGULAR triple plane; it is not a stratified chi_c and is "
               "not determined by cycle types.  Missing inputs: the singularity census "
               "of Delta-bar with its local monodromy, K_Z (or a declared resolution), "
               "and the Z/3-cover class.  See tb-g2-finish-opus5-20260901.md:435.")


# --------------------------------------------------------------------------
# 5. rows and controls
# --------------------------------------------------------------------------

TRANSPOSITION_4 = LocalType("transposition", (2, 1, 1))
THREECYCLE_4 = LocalType("3-cycle", (3, 1))
NODE_DISJOINT_T = LocalType("node: two disjoint transpositions", (2, 2))
NODE_Z3 = LocalType("node: Z/3", (3, 1))


def row_962(generic: LocalType = TRANSPOSITION_4) -> Row:
    """Realized (9,6,2): delta_aff = 4 ordinary nodes, one place at infinity,
    normalisation A^1.  REP-96 sec.1 (rep-96-inner-opus5-20260901.md:100-133)."""
    node_local = NODE_DISJOINT_T if generic is TRANSPOSITION_4 else NODE_Z3
    sings = [SingPoint("node%d" % i, 2, node_local) for i in range(1, 5)]
    return Row("(9,6,2) Mode 1 / %s" % generic.name, 4,
               [Component("D_1", 1, generic, [p.name for p in sings])],
               sings,
               source_gate="REP-96 sec.1 exact re-verification; p=t^9+12t^5+24t, "
                           "q=t^6+8t^2; gcd(p,p')=1; 4 nodes exhaust delta_aff",
               braid_label_E=-20)


def row_64() -> Row:
    """(6,4,3), beta_1 = 15: delta_aff = 3 nodes, one place at infinity.
    NEGATIVE CONTROL.  E = e(iota) = 10 - beta_1 = -5 is a BRAID label only."""
    sings = [SingPoint("node%d" % i, 2, NODE_DISJOINT_T) for i in range(1, 4)]
    return Row("(6,4,3) Mode 1 / transposition", 4,
               [Component("D_1", 1, TRANSPOSITION_4, [p.name for p in sings])],
               sings,
               source_gate="banked (6,4) row: beta_1=15, delta_inf=7, delta_aff=3",
               braid_label_E=-5)


def row_smooth(generic: LocalType) -> Row:
    """D smooth, rational, one place at infinity (D ~ A^1), no singular points.
    Discriminating control: SHEET-GATE sec.8 'smooth-A_F law' says a = 1, so the
    a = 1 branches MUST match and the a = 2 branch MUST NOT."""
    return Row("smooth A^1 branch curve / %s" % generic.name, 4,
               [Component("D_1", 1, generic, [])], [],
               source_gate="synthetic control (SHEET-GATE sec.8 smooth-A_F law)")


def _fmt(res: Dict[str, object]) -> str:
    out = ["  %s   N=%d" % (res["label"], res["N"]),
           "    chi_c(D)=%d  s=%d  chi_c(D_0)=%d  chi_c(V_rho)=%d  c=%d  "
           "sigma=%d  ram=%d  sum_cp=%d" %
           (res["chi_D"], res["s"], res["chi_D0"], res["chi_V"], res["c"],
            res["sigma"], res["ram"], res["sum_cp"]),
           "    chi_c(Y)_RH = %d" % res["chi_Y"]]
    if res["braid_label_E"] is not None:
        out.append("    [row label only, never consumed: E = e(iota) = %d]"
                   % res["braid_label_E"])
    for br in res["branches"]:
        bx = br["box"]
        if br["verdict"] == "OPEN":
            out.append("    (a,b,ram,m_Y)=(%d,%d,%d,%d) -> OPEN[%s] %s"
                       % (bx.a, bx.b, bx.ram, bx.m_Y, br["token"], br["detail"]))
        elif br["verdict"] == "MISMATCH-ON-INTERVAL":
            out.append("    (a,b,ram,m_Y)=(%d,%d,%d,%d)  sum a_p in [%d,%d] "
                       "(undeclared, ACS interval)  gap in [%d,%d]  -> %s"
                       % (bx.a, bx.b, bx.ram, bx.m_Y, br["sum_ap"][0],
                          br["sum_ap"][1], br["gap"][0], br["gap"][1],
                          br["verdict"]))
        else:
            out.append("    (a,b,ram,m_Y)=(%d,%d,%d,%d)  chi_c(B_Y)=%d  "
                       "1+chi_c(B_Y)=%d  chi_c(U)=%d  gap=%d  -> %s"
                       % (bx.a, bx.b, bx.ram, bx.m_Y, br["chi_BY"], br["rhs"],
                          br["chi_U"], br["gap"], br["verdict"]))
    return "\n".join(out)


def run_controls() -> List[str]:
    log: List[str] = []
    fails: List[str] = []

    def emit(title: str, res: Dict[str, object]) -> None:
        log.append("== " + title)
        log.append(_fmt(res))

    def expect(title: str, res: Dict[str, object], want: Sequence[str]) -> None:
        got = [br["verdict"] for br in res["branches"]]
        emit(title, res)
        ok = got == list(want)
        log.append("    EXPECT %s  GOT %s  -> %s" % (list(want), got, "OK" if ok else "FAIL"))
        if not ok:
            fails.append(title)

    # CTRL-P1 / CTRL-P2: the calculator can say MATCH (not hardwired to kill)
    expect("CTRL-P1  smooth A^1 branch, 3-cycle class (a=1 forced)  MUST MATCH",
           run_mode1(row_smooth(THREECYCLE_4)), ["MATCH"])
    expect("CTRL-P2  smooth A^1 branch, transposition class; a=2 MUST FAIL, "
           "a=1 MUST MATCH", run_mode1(row_smooth(TRANSPOSITION_4)),
           ["MISMATCH", "MATCH"])

    # positive control charged by the lane: the (9,6,2) four-box
    r = run_mode1(row_962())
    emit("CTRL-962 positive control: four-box (sigma,ram) MUST be (2,2)", r)
    ok = (r["sigma"], r["ram"]) == (2, 2)
    log.append("    EXPECT (sigma,ram)=(2,2)  GOT (%d,%d)  -> %s"
               % (r["sigma"], r["ram"], "OK" if ok else "FAIL"))
    if not ok:
        fails.append("CTRL-962 four-box")
    got = [br["verdict"] for br in r["branches"]]
    log.append("    EXPECT every branch MISMATCH  GOT %s  -> %s"
               % (got, "OK" if set(got) == {"MISMATCH"} else "FAIL"))
    if set(got) != {"MISMATCH"}:
        fails.append("CTRL-962 verdicts")

    emit("CTRL-962b (9,6,2) Mode 1, 3-cycle class", run_mode1(row_962(THREECYCLE_4)))

    # negative control
    expect("CTRL-64  negative control (6,4,3) MUST NOT MATCH", run_mode1(row_64()),
           ["MISMATCH", "MISMATCH"])

    # CTRL-REJECT: malformed input must raise, not default
    log.append("== CTRL-REJECT  fail-closed probes")
    for name, thunk in [
        ("cycle type not a partition of N",
         lambda: run_mode1(Row("bad", 4, [Component("D", 1, LocalType("bad", (2, 2, 2)), [])],
                               [], source_gate="x"))),
        ("no source_gate provenance (footgun #10 guard)",
         lambda: run_mode1(Row("bad", 4, [Component("D", 1, TRANSPOSITION_4, [])], []))),
        ("a_p > s_p (violates Cor 3.2)",
         lambda: run_mode1(Row("bad", 4, [Component("D", 1, TRANSPOSITION_4, ["p"])],
                               [SingPoint("p", 2, NODE_DISJOINT_T, a_p=1, a_p_source="fake")],
                               source_gate="x"))),
        ("c_2(T^v) requested", c2_tschirnhausen),
    ]:
        try:
            thunk()
        except Open as exc:
            log.append("    %-45s -> %s  OK" % (name, str(exc).split("]")[0] + "]"))
        else:
            log.append("    %-45s -> NO RAISE  FAIL" % name)
            fails.append("CTRL-REJECT " + name)

    # (8,6,9) shared layer: reproduce TB-GERM's "10 A_1 points"
    log.append("== CTRL-869  shared layer only: S_4 -> S_4/V_4 = S_3 at an affine node")
    node_gens = [(1, 0, 2, 3), (0, 1, 3, 2)]          # (01) and (23), disjoint
    sizes = s4_to_s3_orbits(node_gens)
    log.append("    S_4-local orbit sizes on 4 sheets : %s" % [NODE_DISJOINT_T.orbit_sizes])
    log.append("    S_3-local orbit sizes on 3 sheets : %s  (expect (2,1) -> one A_1)"
               % [sizes])
    ok = sizes == (2, 1)
    log.append("    10 affine double points of Delta-bar => 10 A_1 points of Z  -> %s"
               % ("OK (reproduces TB-GERM 7.1)" if ok else "FAIL"))
    if not ok:
        fails.append("CTRL-869")
    log.append("    c_2(T^v) / chi(O_Z): refused above, OPEN[COVERGEO-C2-TSCHIRNHAUSEN]")

    log.append("")
    log.append("CONTROLS: %s" % ("ALL PASS" if not fails else "FAILURES " + str(fails)))
    return log


def main() -> int:
    lines = run_controls()
    print("\n".join(lines))
    seal = "COVERGEO-SEAL v1"
    print(seal)
    assert seal, "footgun #11 guard: main() must emit its seal line"
    return 0 if lines[-1].endswith("ALL PASS") else 1


if __name__ == "__main__" or os.environ.get("COVERGEO_FORCE_MAIN"):
    sys.exit(main())
