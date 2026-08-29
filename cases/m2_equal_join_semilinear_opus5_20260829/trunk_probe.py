#!/usr/bin/env python3
"""Cap-free P0 chain-step probe for the trunk emitted by an equal-join merge.

Re-derives (does not import) the BOOK-OFFAXIS.md §10 P0 one-step menu:

    p = (-) eta^eps (eta^nu - c^nu)^l prod_j (eta^nu - d_j^nu)^{m_j},
    q = (-) eta * (simple orbits),   l | M_parent (St 8.4),
    dp = eps + nu*(l + Sm),  dq = 1 + nu*(1 + k + lex),
    E  = l*dq - dp = (l - eps) + nu*C,  C = l*(k+lex) - Sm >= 0,
    kbar_F = l*w*dq/E in Z (nu >= 2),  w_F = l*w*(dq-1)/(nu*E) = l*w*s/E,
    M_F = gcd(dp,dq),
    lambda_F >= sum_j max(1, ceil(X/m_j - kbar)) + [eps>=1]*max(1, ceil((X/eps - kbar)/nu)).

Finiteness is the PRINTED P0 relation `E | l*num(w)*T`, T = Sm + l - eps*s >= 1,
in the extras-present branch (C >= 1), plus the pure-(b) branch (C = 0), which
is an exact residue family.  No numerical cap is used or accepted.

MP2 (interior trunk M >= 2) and NE/searrow strictness are enforced.
"""
import argparse
import json
import sys
from fractions import Fraction as Fr
from math import gcd

from eqjoin_semilinear import ceil_fr


def _partitions_le(k, hi):
    """All multisets of k integers in [1, hi] (sorted, exact, complete)."""
    if k == 0:
        yield ()
        return
    def rec(rem, lo, acc):
        if rem == 0:
            yield tuple(acc)
            return
        for v in range(lo, hi + 1):
            acc.append(v)
            yield from rec(rem - 1, v, acc)
            acc.pop()
    yield from rec(k, 1, [])


def p0_steps(w, M, budget_left, require_M2=True):
    """Complete one-step successor menu from a chain state (w, M)."""
    a = w.numerator
    out = []
    for l in [d for d in range(1, M + 1) if M % d == 0]:
        for eps in range(0, l):                      # NE on the free 0-root
            for k in range(0, budget_left + 1):      # lambda >= k (Thm 3.1)
                for ms in _partitions_le(k, max(l - 1, 0)):
                    Sm = sum(ms)
                    # ---- pure-(b): C = 0 needs k = lex = 0 -----------------
                    if k == 0:
                        # lex bound from E | l*a*T in the C >= 1 branch;
                        # lex = 0 with eps >= 1 is the free-nu pure-(b) family.
                        pass
                    # lex bound: C = l*(k+lex) - Sm and E = (l-eps) + nu*C
                    # with nu >= 2 and E <= l*a*T, T = Sm + l - eps*(1+k+lex).
                    lex = 0
                    while True:
                        s = 1 + k + lex
                        P = l + Sm
                        T = P - eps * s
                        C = l * (k + lex) - Sm
                        if C == 0:
                            # pure-(b) / neutral family: nu free
                            if k == 0 and lex == 0:
                                E = l - eps
                                if E > 0:
                                    w_F = Fr(l) * w * s / E
                                    lam = 0 if eps == 0 else max(1, ceil_fr(Fr(l) * w / eps))
                                    out.append({"l": l, "eps": eps, "ms": list(ms),
                                                "lex": lex, "C": 0, "nu": "FREE-AP",
                                                "w": w_F, "M": "gcd(%d, nu+1)" % E,
                                                "M_max": E, "lam": lam,
                                                "kind": "neutral" if eps == 0 else "pure-b"})
                            lex += 1
                            if lex > 2 + 2 * l * a:
                                break
                            continue
                        if T <= 0:
                            lex += 1
                            if lex > 2 + 2 * l * a * max(P, 1):
                                break
                            continue
                        Emax = l * a * T
                        if (l - eps) + 2 * C > Emax:
                            break                     # derived stop, not a cap
                        for E in range(1, Emax + 1):
                            if Emax % E:
                                continue
                            num = E - (l - eps)
                            if num <= 0 or num % C:
                                continue
                            nu = num // C
                            if nu < 2:
                                continue
                            dp = eps + nu * P
                            dq = 1 + nu * s
                            if l * dq - dp != E:
                                continue
                            if any(m * dq >= dp for m in ms):
                                continue
                            if eps >= 1 and eps * dq >= dp:
                                continue
                            kbar = Fr(l) * w * dq / E
                            if kbar.denominator != 1:
                                continue
                            if gcd(int(kbar), nu) != 1:        # N1
                                continue
                            MF = gcd(dp, dq)
                            if require_M2 and MF < 2:
                                continue
                            if any(dp == mstar * dq for mstar in
                                   set(ms) | {l} | ({eps} if eps else set())):
                                continue
                            X = kbar * Fr(dp, dq)
                            lam = 0
                            for m in ms:
                                lam += max(1, ceil_fr(X / m - kbar))
                            if eps >= 1:
                                lam += max(1, ceil_fr((X / eps - kbar) / nu))
                            if lam > budget_left:
                                continue
                            out.append({"l": l, "eps": eps, "ms": list(ms), "lex": lex,
                                        "C": C, "nu": nu, "dp": dp, "dq": dq,
                                        "w": Fr(l) * w * s / E, "M": MF,
                                        "kbar": int(kbar), "lam": lam, "kind": "dirty"})
                        lex += 1
                        if (l - eps) + 2 * (l * (k + lex) - Sm) > l * a * max(
                                P - eps * (1 + k + lex), 1) and lex > P + 2:
                            break
    return out


def terminals(w, M):
    """P1 terminal test: w < 1, M >= 2, j = M*(1-w) in N*, psi = ceil(M/j)-1."""
    if w >= 1 or M < 2:
        return None
    j = M * (1 - w)
    if j.denominator != 1 or j <= 0:
        return None
    j = int(j)
    return {"j": j, "psi": -((-M) // j) - 1}


def bfs(w0, M0, budget, max_depth=6):
    seen = {}
    frontier = [((w0, M0), 0, [])]
    hits = []
    depth = 0
    while frontier and depth < max_depth:
        nxt = []
        for (state, spent, path) in frontier:
            w, M = state
            t = terminals(w, M)
            if t is not None and spent <= budget - t["psi"]:
                hits.append({"w": str(w), "M": M, "spent": spent,
                             "psi": t["psi"], "path": path})
            key = (str(w), M)
            if key in seen and seen[key] <= spent:
                continue
            seen[key] = spent
            for st in p0_steps(w, M, budget - spent):
                if st["nu"] == "FREE-AP":
                    for Mc in [d for d in range(2, st["M_max"] + 1)
                               if st["M_max"] % d == 0]:
                        nxt.append(((st["w"], Mc), spent + st["lam"],
                                    path + ["%s(l=%d,eps=%d)->w=%s,M=%d" %
                                            (st["kind"], st["l"], st["eps"], st["w"], Mc)]))
                else:
                    nxt.append(((st["w"], st["M"]), spent + st["lam"],
                                path + ["dirty(l=%d,eps=%d,k=%d,lex=%d,nu=%d)->w=%s,M=%d"
                                        % (st["l"], st["eps"], len(st["ms"]), st["lex"],
                                           st["nu"], st["w"], st["M"])]))
        frontier = nxt
        depth += 1
    return {"terminals_reached": hits, "states_seen": len(seen), "depth": depth}


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    for a in argv:
        if "CAP" in a.upper():
            raise SystemExit("REFUSED: cap token in %r" % a)
    ap = argparse.ArgumentParser()
    ap.add_argument("--w", default="9/2")
    ap.add_argument("--M", type=int, default=2)
    ap.add_argument("--budget", type=int, default=10)
    ap.add_argument("--depth", type=int, default=4)
    ap.add_argument("--output", default=None)
    args = ap.parse_args(argv)
    w = Fr(args.w)
    menu = p0_steps(w, args.M, args.budget)
    res = bfs(w, args.M, args.budget, args.depth)
    doc = {
        "start": {"w": str(w), "M": args.M, "budget": args.budget},
        "one_step_menu": [{k: (str(v) if isinstance(v, Fr) else v)
                           for k, v in st.items()} for st in menu],
        "bfs": res,
    }
    blob = json.dumps(doc, sort_keys=True, separators=(",", ":"))
    if args.output:
        open(args.output, "w").write(blob)
    print("one_step_menu %d" % len(menu))
    print("terminals_reached %d" % len(res["terminals_reached"]))
    print("states_seen %d depth %d" % (res["states_seen"], res["depth"]))
    for h in res["terminals_reached"][:8]:
        print("  TERMINAL w=%s M=%d spent=%d psi=%d %s" %
              (h["w"], h["M"], h["spent"], h["psi"], h["path"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
