#!/usr/bin/env python3
"""H3 checker (SHEET6-H3.md §5): for every IV-terminal hit of the campaign
engine, test the root-vertex kill:
  (l)-test : R := deg(p_G)/d_F = nu/(rho+nu-kap) > 1  (iff rho < kap); else
             case IV impossible at that s (Prop 9.3 (l), with (k): d_F > 0
             needs rho+nu-kap > 0).
  (m)-test : d_F*M_G/deg(p_G) = M*(rho+nu-kap)/nu in N* (j-free); else case
             IV impossible (Prop 9.3 (m)).
  psi-kill : psi := ceil(R)-1; conditionally killed iff
             lam_recorded > td - 1 - psi, using the currently accepted
             Section 7 weighted budget / first-separation ledger and
             lam_recorded as a lower bound for sum lambda.
Exact arithmetic (Fraction). Parametric shapes evaluated at s = 0..SMAX with
the s->infty limit of R reported and an explicit OPEN_s_tail marker: the
finite scan is never treated as a proof about all s. Exit disposition per hit:
  DEAD_l / DEAD_m (case IV impossible), KILLED_psi, SURVIVOR, and
  OPEN_s_tail for every unproved parametric remainder.
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
        rows.append((SMAX + 1, 'OPEN_s_tail', None))
    return rows, limit


def run(entries, td, budget, label, show_traces=0):
    print(f"\n=== {label}: td={td}, budget={budget} "
          "[conditional Section 7 ledger] ===")
    n_surv, agg = 0, {}
    surv_shapes, root_shapes = {}, set()
    for name, Lam, sanct, node in entries:
        # BFS identical to sc.bash but capturing the node at TERMINAL_IV
        seen = {node.shape(): 0}
        dq = deque([(node, 0, [f"ENTRY {node}"])])
        hits, root_hits, opens, frontier = [], [], [], 0
        while dq:
            nd, lam, tr = dq.popleft()
            if len(tr) - 1 >= 7:               # sc.bash maxdepth
                frontier += 1
                continue
            for o in sc.step(nd):
                if o[0] == 'TERMINAL_IV':
                    hits.append((nd, lam, tr))
                elif o[0] == 'OPEN':
                    lmin = o[2] if len(o) > 2 else 0
                    if lam + lmin <= budget:
                        opens.append((o[1], lam))
                elif o[0] == 'CONT':
                    _, dl, child, why = o
                    nl = lam + dl
                    if nl > budget:
                        continue
                    disposition = sc.dispose_constructed_child(child)
                    if disposition in (sc.TERMINAL_ROOT_M1,
                                       sc.TERMINAL_ROOT_M_GT1):
                        root_hits.append((child.shape(), nl, disposition, tr + [why]))
                        continue
                    if disposition == sc.KILL_NR_M1:
                        continue
                    assert disposition == sc.KEEP
                    sh = child.shape()
                    if sh in seen and seen[sh] <= nl:
                        continue
                    seen[sh] = nl
                    dq.append((child, nl, tr + [why]))
        if root_hits:
            dedup_roots = {(shape, root_lam, disposition)
                           for shape, root_lam, disposition, _ in root_hits}
            root_shapes.update((name,) + root for root in dedup_roots)
            print(f"[{name}] root terminals (case I/single-orbit): "
                  f"{len(dedup_roots)}")
        if opens or frontier:
            print(f"[{name}] NO_VERDICT: open_kinds={len({msg for msg, _ in opens})} "
                  f"depth_frontier={frontier}")
        seen_h = set()
        for nd, lam, tr in hits:
            key = (nd.shape(), lam)
            if key in seen_h:
                continue
            seen_h.add(key)
            rows, limit = iv_dispositions(nd, lam, td)
            cls = ('SURVIVOR' if any(v == 'SURVIVOR' for _, v, _ in rows) else
                   'OPEN_s_tail' if any(v == 'OPEN_s_tail' for _, v, _ in rows) else
                   'KILLED_psi' if any(v == 'KILLED_psi' for _, v, _ in rows) else
                   'DEAD(l/m/k/j)')
            agg.setdefault(name, {'SURVIVOR': 0, 'KILLED_psi': 0,
                                  'OPEN_s_tail': 0,
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
              f"conditionally_killed_psi={a['KILLED_psi']} "
              f"OPEN_s_tail={a['OPEN_s_tail']} SURV={a['SURVIVOR']}")
    print(f"--- {label}: survivor (shape,lam) classes: {len(surv_shapes)}; "
          f"(shape,s) pairs: {n_surv}; separate root-terminal classes: "
          f"{len(root_shapes)}")
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
    signature of (0,y). These were historically omitted; the root-aware
    engine now records them as terminal candidates."""
    print("\n=== SF1 scan: (nu,kap)=(1,1) CONT children ===")
    found, opens, frontier = set(), 0, 0
    for lam_t, bud in ((3, 1), (4, 2), (5, 3), (6, 4)):
        for name, Lam, sanct, node in sc.entry_nodes(lam_t):
            seen = {node.shape(): 0}
            dq = deque([(node, 0, 0)])
            while dq:
                nd, lam, d = dq.popleft()
                if d >= 7:
                    frontier += 1
                    continue
                for o in sc.step(nd):
                    if o[0] == 'OPEN':
                        lmin = o[2] if len(o) > 2 else 0
                        if lam + lmin <= bud:
                            opens += 1
                        continue
                    if o[0] != 'CONT':
                        continue
                    _, dl, ch, why = o
                    nl = lam + dl
                    if nl > bud:
                        continue
                    disposition = sc.dispose_constructed_child(ch)
                    if disposition in (sc.TERMINAL_ROOT_M1,
                                       sc.TERMINAL_ROOT_M_GT1):
                        # M is part of the key: corrected Prop. 8.4 imposes no
                        # root restriction, so M=1 and M>1 are distinct cells.
                        key = (lam_t, name, nl, ch.shape(), ch.M, disposition)
                        if key not in found:
                            found.add(key)
                            print(f"  td={lam_t} [{name}] lam={nl} M={ch.M} "
                                  f"{ch} [{disposition}] via {why[:60]}")
                        continue
                    if disposition == sc.KILL_NR_M1:
                        continue
                    assert disposition == sc.KEEP
                    sh = ch.shape()
                    if sh in seen and seen[sh] <= nl:
                        continue
                    seen[sh] = nl
                    dq.append((ch, nl, d + 1))
    print(f"--- SF1 root-terminal children (M-sensitive dedup): {len(found)}; "
          f"NO_VERDICT open={opens} depth_frontier={frontier}")


if __name__ == "__main__":
    tot = 0
    for lam_t in (3, 4, 5):
        ent = sc.entry_nodes(lam_t)
        tot += run(ent, lam_t, lam_t - 2, f"td<=5 validation Lambda={lam_t}",
                   show_traces=6)
    tot += run(sc.entry_nodes(6), 6, 4, "td=6 campaign", show_traces=10)
    print(f"\n==== GRAND TOTAL IV-SURVIVOR (shape,s) PAIRS: {tot}; "
          "root terminals reported separately above ====")
    scan_root_lookalikes()
