#!/usr/bin/env python3
"""H3 checker (SHEET6-H3.md §5): for every IV-terminal hit of the campaign
engine, test the root-vertex kill:
  (l)-test : R := deg(p_G)/d_F = nu/(rho+nu-kap) > 1  (iff rho < kap); else
             case IV impossible at that s (Prop 9.3 (l), with (k): d_F > 0
             needs rho+nu-kap > 0).
  (m)-test : d_F*M_G/deg(p_G) = M*(rho+nu-kap)/nu in N* (j-free); else case
             IV impossible (Prop 9.3 (m)).
  psi-kill : psi := ceil(R)-1; killed iff lam_recorded > td - 1 - psi
             (St 9.4 (25) via SHEET6-H3.md §4a, using lam_recorded as a
             lower bound for sum lambda).
Exact arithmetic (Fraction). Parametric shapes evaluated at s = 0..SMAX with
the s->infty limit of R reported. Exit disposition per hit:
  DEAD_l / DEAD_m (case IV impossible), KILLED_psi, SURVIVOR (else).
Engine gate on IV is (j)-only (kap < nu), a superset of (i)-(m): every hit
below already satisfies (j) at the listed s.
"""
import os, sys
from fractions import Fraction as Fr
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sheet6_campaign as sc

SMAX = 40


def ceil_fr(x):
    return -((-x.numerator) // x.denominator)


def iv_dispositions(node, lam, td):
    """Per-s analysis of one IV hit. Returns list of (s, verdict, R) and the
    limit info for parametric shapes."""
    rho, M = node.rho, node.M
    na, nb = sc.LF(node.nu)
    ka, kb = sc.LF(node.kap)
    rows, limit = [], None
    svals = range(0, SMAX + 1) if (na or ka) else [0]
    for s in svals:
        nu, kap = na * s + nb, ka * s + kb
        if not kap < nu:                       # (j) fails at this s: no IV
            rows.append((s, 'NO_IV_j', None))
            continue
        den = rho + nu - kap                   # d_F/deg(p_G) * nu
        if den <= 0:
            rows.append((s, 'DEAD_k', None))   # d_F <= 0: (k) unsatisfiable
            continue
        R = Fr(nu) / den
        if R <= 1:                             # (l) fails
            rows.append((s, 'DEAD_l', R))
            continue
        m_val = Fr(M) * den / nu               # d_F M/deg p_G, j-free
        if m_val.denominator != 1 or m_val == 0:
            rows.append((s, 'DEAD_m', R))
            continue
        psi = ceil_fr(R) - 1
        if lam > td - 1 - psi:
            rows.append((s, 'KILLED_psi', R))
        else:
            rows.append((s, 'SURVIVOR', R))
    if na or ka:
        d = na - ka                            # R(s) -> na/d as s->infty
        limit = ('R->%s' % (Fr(na, d) if d > 0 else 'inf/neg'), 'dR_den=%d' % d)
    return rows, limit


def run(entries, td, budget, label, show_traces=0):
    print(f"\n=== {label}: td={td}, budget={budget} ===")
    n_surv, agg = 0, {}
    surv_shapes = {}
    for name, Lam, sanct, node in entries:
        # BFS identical to sc.bash but capturing the node at TERMINAL_IV
        seen = {node.shape(): 0}
        dq = deque([(node, 0, [f"ENTRY {node}"])])
        hits = []
        while dq:
            nd, lam, tr = dq.popleft()
            if len(tr) - 1 >= 7:               # sc.bash maxdepth
                continue
            for o in sc.step(nd):
                if o[0] == 'TERMINAL_IV':
                    hits.append((nd, lam, tr))
                elif o[0] == 'CONT':
                    _, dl, child, why = o
                    nl = lam + dl
                    if nl > budget or child.M == 1:
                        continue
                    sh = child.shape()
                    if sh in seen and seen[sh] <= nl:
                        continue
                    seen[sh] = nl
                    dq.append((child, nl, tr + [why]))
        if not hits:
            continue
        seen_h = set()
        for nd, lam, tr in hits:
            key = (nd.shape(), lam)
            if key in seen_h:
                continue
            seen_h.add(key)
            rows, limit = iv_dispositions(nd, lam, td)
            cls = ('SURVIVOR' if any(v == 'SURVIVOR' for _, v, _ in rows) else
                   'KILLED_psi' if any(v == 'KILLED_psi' for _, v, _ in rows) else
                   'DEAD(l/m/k/j)')
            agg.setdefault(name, {'SURVIVOR': 0, 'KILLED_psi': 0,
                                  'DEAD(l/m/k/j)': 0})[cls] += 1
            if cls == 'SURVIVOR':
                surv = [(s, R) for s, v, R in rows if v == 'SURVIVOR']
                n_surv += len(surv)
                Rset = sorted({str(R) for _, R in surv})
                psis = sorted({ceil_fr(R) - 1 for _, R in surv})
                sk = (nd.shape(), lam, tuple(Rset))
                if sk not in surv_shapes:
                    surv_shapes[sk] = (name, tr, psis)
    for name in sorted(agg):
        a = agg[name]
        print(f"[{name}] hits: dead={a['DEAD(l/m/k/j)']} "
              f"killed_psi={a['KILLED_psi']} SURV={a['SURVIVOR']}")
    print(f"--- {label}: survivor (shape,lam) classes: {len(surv_shapes)}; "
          f"(shape,s) pairs: {n_surv}")
    for i, (sk, (name, tr, psis)) in enumerate(sorted(surv_shapes.items(),
                                               key=lambda kv: str(kv[0]))):
        if i >= show_traces:
            break
        sh, lam, Rset = sk
        print(f"  SURV[{name}] lam={lam} shape={sh} R={Rset} psi={psis}")
        for t in tr:
            print(f"      | {t[:120]}")
    return n_surv


def scan_root_lookalikes():
    """SF1 (SHEET6-H3.md §7): CONT children with (nu,kap) = (1,1) — the St 9.2
    signature of (0,y) — i.e. possible root-terminations via case I that the
    campaign does not model as terminal."""
    print("\n=== SF1 scan: (nu,kap)=(1,1) CONT children ===")
    found = 0
    for lam_t, bud in ((3, 1), (4, 2), (5, 3), (6, 4)):
        for name, Lam, sanct, node in sc.entry_nodes(lam_t):
            seen = {node.shape(): 0}
            dq = deque([(node, 0, 0)])
            while dq:
                nd, lam, d = dq.popleft()
                if d >= 7:
                    continue
                for o in sc.step(nd):
                    if o[0] != 'CONT':
                        continue
                    _, dl, ch, why = o
                    if lam + dl > bud or ch.M == 1:
                        continue
                    if sc.LF(ch.nu) == (0, 1) and sc.LF(ch.kap) == (0, 1):
                        found += 1
                        print(f"  td={lam_t} [{name}] lam={lam+dl} {ch} "
                              f"via {why[:60]}")
                    sh = ch.shape()
                    if sh in seen and seen[sh] <= lam + dl:
                        continue
                    seen[sh] = lam + dl
                    dq.append((ch, lam + dl, d + 1))
    print(f"--- SF1 root-lookalike CONT children: {found}")


if __name__ == "__main__":
    tot = 0
    for lam_t in (3, 4, 5):
        ent = sc.entry_nodes(lam_t)
        tot += run(ent, lam_t, lam_t - 2, f"td<=5 validation Lambda={lam_t}",
                   show_traces=6)
    tot += run(sc.entry_nodes(6), 6, 4, "td=6 campaign", show_traces=10)
    print(f"\n==== GRAND TOTAL SURVIVOR (shape,s) PAIRS: {tot} ====")
    scan_root_lookalikes()
