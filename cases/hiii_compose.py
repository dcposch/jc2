#!/usr/bin/env python3
"""COMPOSITION engine (SHEET6-HIII-REVIEW.md front 5): run the campaign BFS
with BOTH kill sets active:
  - Result 2 (SHEET6-III, e5d42e7): case-III steps use the E5-corrected
    (g')/(h') arithmetic (H5a/H5b): child rho_F = C := mu(kap_G-rho_G)/
    (k(mu-1)nu_G), kap_F = C(1+k nu_F), D_F/i = C(mu+k nu_F), lambda >=
    k*max(1, ceil(C(mu-1))) >= ceil(mu(kap_G-rho_G)/nu_G); N1 gcd(kap,nu)=1
    at every nu>=2 vertex (drop children/entries violating it identically).
  - Result 1 (SHEET6-H3, 048f2d9): IV-terminals classified by the (l)/(m)
    consistency tests + the psi-budget kill (St 9.4 (25), psi = ceil(R)-1),
    via h3_check.iv_dispositions.
Case I/II branches are inherited UNCHANGED from sheet6_campaign.step (the
(a)-(d) arithmetic is uncontested); only III-outcomes are replaced.
Internal gate: E5 child closed forms reproduce cong_survivors' witnesses on
the (1/2,4s+3,4,2s+2)/mu=4 tail; a PIT asserts (f)+(h') on every emitted
family. Exact arithmetic throughout.
Conservative directions (sound for kill claims, over-report survivors):
  - E5-III children keep residue families even where N1 kills a sub-residue
    (N1 dropped only when it kills ALL residues identically).
  - Unlocked parametric III nodes: killed only when budget_kill_all_s
    certifies mu(kap(s)-rho) > B nu(s) for all s; else recorded OPEN.
"""
import os, sys, re
from fractions import Fraction as Fr
from math import gcd
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sheet6_campaign as sc
import h3_check as hc

LF, Node = sc.LF, sc.Node
KMAX = 4          # lambda >= k, budget <= 4
NUF_SPAN = 2      # residue classes scanned over nu_F in [2, NUF_SPAN*T+1]
BUDGET_CAP = 4    # III-child lambda cap (= chain budget; tduniform overrides)


def ceil_fr(x):
    x = Fr(x)
    return -((-x.numerator) // x.denominator)


def lcm(a, b):
    return a * b // gcd(a, b)


def e5_iii_outcomes(node, mu):
    """E5-corrected case-III outcomes from `node` for root multiplicity mu.
    Concrete or LOCKED-parametric nodes: exact family enumeration (children
    are s-free; family parameter t is the nu_F progression). Unlocked
    parametric: OPEN_E5U marker (BFS applies budget_kill_all_s)."""
    rho = node.rho
    na, nb = LF(node.nu)
    ka, kb = LF(node.kap)
    parametric = bool(na or ka)
    if parametric and not sc.is_locked(node):
        return [('OPEN_E5U', f"mu={mu} III-E5 unlocked parametric at {node}", 1, mu)]
    out = []
    if parametric:
        Lam = Fr(mu) * rho                      # locked: kap-rho = rho*nu
    else:
        Lam = Fr(mu) * (Fr(kb) - rho) / nb
    if Lam <= 0:
        return out                              # kap_F >= 1 impossible
    for k in range(1, KMAX + 1):
        lam_k = k * max(1, ceil_fr(Lam / k))
        if lam_k > BUDGET_CAP:
            continue
        C = Lam / (k * (mu - 1))                # = rho_F
        b = C.denominator
        T = lcm(b, mu - 1)                      # period of kapF-in-Z and M_F
        fams = {}
        for nuF in range(2, NUF_SPAN * T + 2):
            kapF = C * (1 + k * nuF)
            if kapF.denominator != 1:
                continue
            MF = gcd(mu - 1, 1 + k * nuF)
            if MF < 2:
                continue                        # Prop 8.4 kill
            fams.setdefault((nuF % T, MF), []).append(nuF)
        for (r, MF), lst in sorted(fams.items()):
            base = min(lst)
            # n >= 1 window over nuF in the class {base + T*t}. Both tests
            # are linear in nuF: A(nuF) = na*kapF - nuF*ka (s-slope of n for
            # parametric nodes), B(nuF) = nb*kapF - nuF*kb (n at s=0 / the
            # concrete n). window = A>0 (parametric only) or B>=1.
            def kapF_of(nuF):
                return C * (1 + k * nuF)

            def window(nuF):
                kf = kapF_of(nuF)
                if parametric and na * kf - nuF * ka > 0:
                    return True
                return nb * kf - nuF * kb >= 1
            slope_A = na * C * k - ka           # d/d nuF of A
            slope_B = nb * C * k - kb           # d/d nuF of B
            emit = []                           # nuF linear forms
            if slope_B > 0 or (parametric and slope_A > 0):
                # a positive slope guarantees an eventually-passing tail:
                # find FIRST passing member; family covers all later t
                # (over-covers any interior failures: conservative).
                while not window(base):
                    base += T
                emit.append((T, base))
            elif (slope_B == 0 and nb * kapF_of(base) - base * kb >= 1) or \
                 (parametric and slope_A == 0 and
                  na * kapF_of(base) - base * ka > 0):
                emit.append((T, base))          # constant passing test
            else:
                # every passing test strictly decreasing: finite prefix.
                nuF, guard = base, 0
                while guard < 100000:
                    if window(nuF):
                        emit.append((0, nuF))
                    elif (not parametric or na * kapF_of(nuF) - nuF * ka <= 0) \
                            and nb * kapF_of(nuF) - nuF * kb < 1:
                        break                   # all tests failed, slopes<=0
                    nuF += T
                    guard += 1
            for nuF_form in emit:
                dT, base_ = nuF_form
                kap_form = (int(C * k * dT), int(C * (1 + k * base_)))
                # N1 at child: drop only if gcd>1 identically
                if dT == 0:
                    if gcd(base_, kap_form[1]) > 1:
                        continue
                else:
                    R_, killed = sc.n1_residues(nuF_form, kap_form)
                    if len(killed) == R_:
                        continue
                # PIT: (f) + (h') at three instances (and s for parametric)
                for t in (0, 1, 2):
                    nuF = dT * t + base_
                    kapF = kap_form[0] * t + kap_form[1]
                    for s in ((6, 7, 9) if parametric else (0,)):
                        nuG, kapG = na * s + nb, ka * s + kb
                        n = nuG * kapF - nuF * kapG
                        if n < 1:
                            continue
                        assert (mu + k * nuF) * (nuF * kapG + n) == \
                            (1 + k * nuF) * mu * (nuF * rho + n), "E5 (f) PIT"
                        assert (nuF * kapG + n) % nuG == 0 and \
                            (nuF * kapG + n) // nuG == kapF, "E5 (h') PIT"
                dp0, ddp = mu + k * base_, k * dT
                pcF = (node.pc // mu) * (gcd(ddp, dp0) if ddp else dp0)
                child = Node(C, nuF_form, MF, kap_form, pcF,
                             tag=f"<-IIIe5mu{mu}k{k}")
                why = (f"mu={mu} III-E5 k={k} nuF={sc.lf_str(nuF_form)} "
                       f"MF={MF} -> {child} lam>={lam_k}")
                out.append(('CONT', lam_k, child, why))
    return out


_III_PAT = re.compile(r"mu=\d+ III[ :]")


def step_e5(node):
    """sc.step with III-outcomes replaced by E5 arithmetic, and N1 filter on
    all CONT children."""
    out = []
    for o in sc.step(node):
        if o[0] == 'CONT' and _III_PAT.search(o[3]):
            continue
        if o[0] == 'OPEN' and _III_PAT.search(o[1]):
            continue
        out.append(o)
    for mu in sc.divisors_gt1(node.M):
        if mu >= 3:
            out.extend(e5_iii_outcomes(node, mu))
    filt = []
    for o in out:
        if o[0] == 'CONT':
            ch = o[2]
            cna, cnb = LF(ch.nu)
            cka, ckb = LF(ch.kap)
            if not (cna or cka):
                if cnb >= 2 and gcd(cnb, ckb) > 1:
                    continue                    # N1 kill (concrete)
            else:
                try:
                    R_, killed = sc.n1_residues(ch.nu, ch.kap)
                    if len(killed) == R_:
                        continue                # N1 kill (all residues)
                except AssertionError:
                    pass                        # proportional forms: skip N1
        filt.append(o)
    return filt


def run_compose(entries, td, budget, label, show=8):
    print(f"\n=== COMPOSE {label}: td={td}, budget={budget} ===")
    surv_shapes, opens_all, sf1 = {}, {}, []
    for name, Lam, sanct, node in entries:
        na, nb = LF(node.nu)
        if nb >= 2 and not na and gcd(nb, LF(node.kap)[1]) > 1:
            print(f"[{name}] ENTRY KILLED by N1 (gcd(kap,nu)>1)")
            continue
        seen = {node.shape(): 0}
        dq = deque([(node, 0, [f"ENTRY {node}"])])
        hits, opens, frontier = [], [], 0
        while dq:
            nd, lam, tr = dq.popleft()
            if len(tr) - 1 >= 7:
                frontier += 1                   # depth-cap hit: exclusion
                continue                        # claims unsound if > 0
            for o in step_e5(nd):
                if o[0] == 'TERMINAL_IV':
                    hits.append((nd, lam, tr))
                elif o[0] == 'OPEN_E5U':
                    _, msg, lmin, mu = o
                    if lam + lmin > budget:
                        continue
                    if sc.budget_kill_all_s(nd, mu, budget - lam):
                        continue                # certified E5 budget kill
                    opens.append((msg, lam))
                elif o[0] == 'OPEN':
                    lmin = o[2] if len(o) > 2 else 0
                    if lam + lmin > budget:
                        continue
                    opens.append((o[1], lam))
                elif o[0] == 'CONT':
                    _, dl, child, why = o
                    nl = lam + dl
                    if nl > budget or child.M == 1:
                        continue
                    if LF(child.nu) == (0, 1) and LF(child.kap) == (0, 1):
                        sf1.append((name, nl, str(child)[:60]))
                    sh = child.shape()
                    if sh in seen and seen[sh] <= nl:
                        continue
                    seen[sh] = nl
                    dq.append((child, nl, tr + [why]))
        seen_h = set()
        n_iv_surv = 0
        for nd, lam, tr in hits:
            key = (nd.shape(), lam)
            if key in seen_h:
                continue
            seen_h.add(key)
            rows, _ = hc.iv_dispositions(nd, lam, td)
            surv = [(s, R) for s, v, R in rows if v == 'SURVIVOR']
            if surv:
                n_iv_surv += 1
                sk = (str(nd.shape()), lam)
                if sk not in surv_shapes:
                    surv_shapes[sk] = (name, tr,
                                       sorted({str(R) for _, R in surv}))
        od = {}
        for msg, lam in opens:
            od.setdefault(re.sub(r" at Q\[.*", "", msg), []).append(lam)
        opens_all[name] = od
        print(f"[{name}] {'SANC' if sanct else 'ext '} iv_hits={len(seen_h)} "
              f"iv_SURV_classes={n_iv_surv} open_kinds={len(od)} "
              f"frontier={frontier}")
        for kmsg, lams in sorted(od.items()):
            print(f"    OPEN minlam={min(lams)} x{len(lams)} {kmsg[:95]}")
    print(f"--- {label}: composed IV-survivor (shape,lam) classes: "
          f"{len(surv_shapes)}")
    for i, (sk, (name, tr, Rset)) in enumerate(sorted(surv_shapes.items())):
        if i >= show:
            break
        print(f"  IVSURV[{name}] lam={sk[1]} shape={sk[0]} R={Rset}")
        for t in tr:
            print(f"      | {t[:118]}")
    if sf1:
        ded = sorted({(n, l, c) for n, l, c in sf1})
        print(f"--- {label}: SF1 (nu,kap)=(1,1) children: {len(ded)}")
        for n, l, c in ded:
            print(f"    SF1[{n}] lam={l} {c}")
    return surv_shapes, opens_all


def gate_compose():
    """E5 closed forms must reproduce cong_survivors on a known tail."""
    tail = Node(Fr(1, 2), (4, 3), 4, (2, 2), 4)
    wits, _ = sc.cong_survivors(tail, 4, 2)
    fams = [(o[1], o[2]) for o in e5_iii_outcomes(tail, 4) if o[0] == 'CONT']

    def on_line(w):
        k, nuF, MF, kapF, lam = w
        for lamf, ch in fams:
            dT, base = LF(ch.nu)
            dK, bK = LF(ch.kap)
            if dT == 0:
                if (nuF, kapF) != (base, bK):
                    continue
            else:
                if (nuF - base) % dT or nuF < base:
                    continue
                t = (nuF - base) // dT
                if dK * t + bK != kapF:
                    continue
            if ch.M == MF and lamf == lam:
                return True
        return False
    missing = [w for w in wits if not on_line(w)]
    assert not missing, f"GATE FAIL: cong_survivors witnesses missing {missing}"
    return f"COMPOSE GATE PASS: {len(wits)} tails3 witnesses reproduced by E5 closed forms"


# --- AF3' M-pin stage (SHEET6-AF3.md; additive) -------------------------
# At F in T_a,pole: m_F = 0 (Prop 5.1(i)/(iii) + Not 5.1/5.2, pp. 23-24), so
# Not 8.1's family (p. 39) collapses to {h_0} = {g} (Prop 4.2, p. 19) and
# M_F = gcd(deg p_F, deg p_g,F) EXACTLY -- a table-(23) (p. 46) lookup, not
# a menu. Prop 8.4 (single-pole) then kills every gcd = 1 row at entry.
PIN_EXPECT = {  # printed table (23) degree pairs -> pinned M (A2P front 7c)
    (2, 2, 2, 3): 1, (2, 2, 1, 6): 1, (4, 2, 2, 6): 1, (2, 4, 3, 4): 2,
    (3, 3, 3, 4): 1, (3, 3, 2, 6): 1, (2, 2, 2, 5): 1, (2, 6, 5, 6): 3,
    (3, 6, 5, 6): 2, (4, 4, 4, 5): 1, (5, 5, 5, 6): 1}


def pin_entry_nodes(lam_target):
    """Entries with M pinned to gcd(P, Pg); gcd = 1 rows are entry-dead."""
    rows = sorted(sc.prop91(Lmax=7),
                  key=lambda r: (r[4], r[0], r[1], r[2], r[3]))
    ent = []
    for (al, be), (D, Dg), (P, Pg), nu, Lam in rows:
        if Lam != lam_target:
            continue
        Mpin = gcd(P, Pg)
        assert PIN_EXPECT[(D, P, nu, Lam)] == Mpin, "pin vs table (23)"
        tag = f"({al},{be})D{D}P{P}nu{nu}Mpin{Mpin}"
        if Mpin == 1:
            print(f"[{tag}] ENTRY DEAD: M = gcd({P},{Pg}) = 1 (Prop 8.4)")
            continue
        ent.append((tag, Lam, True, Node(Fr(D, P), nu, Mpin, D + Dg, P)))
    return ent


if __name__ == "__main__":
    if 'pin' in sys.argv[1:]:                  # SHEET6-AF3: pinned entries
        sc.IIB_DERIVED = True
        print("[AF3'] entry M pinned to gcd(deg p, deg p_g) per Not 8.1 + "
              "Prop 5.1(iii); IIB_DERIVED=True (AF2 default)")
        print(gate_compose())
        tot = {}
        for lam_t in (3, 4, 5):
            s_, _ = run_compose(pin_entry_nodes(lam_t), lam_t, lam_t - 2,
                                f"PIN td<=5 Lambda={lam_t}")
            tot[lam_t] = s_
        s6, _ = run_compose(pin_entry_nodes(6), 6, 4, "PIN td=6")
        tot[6] = s6
        print("\n==== PINNED GRAND: "
              + ", ".join(f"td{k}: {len(v)}" for k, v in tot.items())
              + " ====")
        sys.exit(0)
    if 'iib' in sys.argv[1:]:                  # SHEET6-AF2: derived IIb pricing
        sc.IIB_DERIVED = True
        print("[AF2] IIB_DERIVED=True: IIb priced per St 9.3 (24) "
              "(k orbits at max(1,ceil(gap)) + 0-root at max(1,ceil(gap/nu_F)))")
    print(gate_compose())
    tot = {}
    for lam_t in (3, 4, 5):
        s_, _ = run_compose(sc.entry_nodes(lam_t), lam_t, lam_t - 2,
                            f"td<=5 Lambda={lam_t}")
        tot[lam_t] = s_
    s6, _ = run_compose(sc.entry_nodes(6), 6, 4, "td=6")
    tot[6] = s6
    print("\n==== COMPOSED GRAND: "
          + ", ".join(f"td{k}: {len(v)}" for k, v in tot.items()) + " ====")
