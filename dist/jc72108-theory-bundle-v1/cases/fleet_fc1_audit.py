#!/usr/bin/env python3
"""FLEET JOB (box01): the FC1 beyond-core window audit, all three
td-11 opponent seeds at gross budget 9.

Per ops/FLEET.md conventions: pure python (no msolve), single lane,
self-recording, orphan-safe.  Launch from the repo checkout:

  cd ~/jc72108/cases/scratch_offaxis_pricing && \\
  nohup sh -c "python3 ../fleet_fc1_audit.py > ../fc1_audit.log 2>&1; \\
    echo \\"FC1 lane: rc=$? $(date +%H:%M)\\" >> ../lanes.log" \\
    >/dev/null 2>&1 &

DESIGN (the two-tier audit, proved bounds only -- no grammar sups):
  tier 1 (cheap): a state first reached at degree D is window-safe if
    2 * R_bound(a, M) < D with the PROVED ratio bounds
      R_clean  <= 1 + a/2          (Delta | a, nu >= 2)
      R_dirty  <= 20 + 5*a*M       (from the FC2-proved k/lex sups:
                                    k <= 9 via lambda >= k;
                                    lex <= a(Sm+l)/2 + Sm/l - k)
      R_pure-b <= 2, R_ndrop <= 3/2
  tier 2 (exact): states failing tier 1 get the full cap-free menu
    (the FC2 enumerator, k <= 9, lex to the proved sups) and every
    step's gap ratio/D is checked against 1/2.
  Discovery: px2.chain_steps PLUS the cap-free complement sweep at
  every expanded state (so no successor is lost to the engine caps).
VERDICT per seed: CLOSED (zero in-window steps beyond the seed
5/8) or the named live/violating states listed.
"""
import sys
import time
from fractions import Fraction as Fr
from math import gcd
import heapq

sys.path.insert(0, '.')
import px2   # noqa: E402
import px5   # noqa: E402


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def capfree_dirty(w, M, kmax=9):
    """The FC2 cap-free dirty enumerator at proved sups."""
    a = w.numerator
    out = []
    for l in divisors(M):
        if l < 2:
            continue
        for eps in range(0, l):
            for k in range(0, kmax + 1):
                if eps == 0 and k == 0:
                    continue
                smin, smax = (k, k * (l - 1)) if k else (0, 0)
                for Sm in range(smin, smax + 1):
                    lexsup = ((Sm + l) // eps + 1 if eps >= 1
                              else (a * (Sm + l)) // 2 + Sm // l + 2)
                    for lex in range(0, lexsup + 1):
                        C = l * (k + lex) - Sm
                        if C <= 0:
                            continue
                        T = Sm + l - eps * (1 + k + lex)
                        if T <= 0:
                            continue
                        if 2 * C > l * a * T:
                            break
                        for E in divisors(l * a * T):
                            nuq, rem = divmod(E - (l - eps), C)
                            if rem or nuq < 2:
                                continue
                            dq = (1 + k + lex) * nuq + 1
                            dp = eps + nuq * (l + Sm)
                            kb = Fr(l * w * dq, E)
                            if kb.denominator != 1 or kb < 1:
                                continue
                            if eps and eps * dq >= dp:
                                continue
                            mm = min(l - 1, (dp - 1) // dq) if k else 0
                            if k and (mm < 1 or Sm > k * mm or Sm < k):
                                continue
                            w2 = Fr(l * w * (dq - 1), nuq * E)
                            out.append((Fr(dq * l, dp), Fr(dp, l),
                                        (w2, gcd(dp, dq)), 1))
    return out


def menu(w, M):
    """px2 steps + the cap-free complement (dedup by target/ratio)."""
    out = []
    for (w2, M2, dl, tag) in sorted(set(px2.chain_steps(w, M))):
        if tag.startswith('clean'):
            nu = int(tag.split('nu')[-1])
            D = int(tag.split('D')[1].split('n')[0])
            n = (D - 1) // nu + 1
            out.append((Fr(n * nu + 1, nu), Fr(nu), (w2, M2), dl))
        elif tag.startswith('st96'):
            body = tag[5:]
            l = int(body.split('e')[0][1:])
            dp, dq = (int(x) for x in
                      body.split('(')[1].rstrip(')').split(','))
            out.append((Fr(dq * l, dp), Fr(dp, l), (w2, M2), dl))
        elif tag.startswith('pure-b'):
            out.append((Fr(3, 2), Fr(2), (w2, M2), dl))
        else:
            out.append((Fr(3, 2), Fr(2), (w2, M2), dl))
    out += capfree_dirty(w, M)
    return out


def audit(seed, p, B=9):
    t0 = time.time()
    best, heap = {}, [(p, 0, seed)]
    mcache, viol, checked = {}, [], 0
    while heap:
        deg, lam, st = heapq.heappop(heap)
        if any(d <= deg for (s2, l2), d in best.items()
               if s2 == st and l2 <= lam):
            continue
        best[(st, lam)] = deg
        a, M = st[0].numerator, st[1]
        Rb = max(Fr(2 + a, 2), Fr(20 + 5 * a * M))
        tier2 = (2 * Rb >= deg)
        if st not in mcache and (tier2 or True):
            mcache[st] = menu(*st)
        checked += 1
        for step in mcache[st]:
            r, m, st2, dl = step[0], step[1], step[2], step[3]
            if tier2 and Fr(r, 1) / deg >= Fr(1, 2) \
                    and not (st == seed and deg == p):
                viol.append((str(st), deg, str(r)))
            if lam + dl > B:
                continue
            nd = deg * m
            if nd.denominator == 1:
                heapq.heappush(heap, (int(nd), lam + dl, st2))
        if checked % 100 == 0:
            print(f"  ...{checked} pops, {len(mcache)} states, "
                  f"{time.time()-t0:.0f}s", flush=True)
    return len(mcache), viol, time.time() - t0


for (seed, p) in (((Fr(3), 2), 4), ((Fr(3, 2), 2), 4),
                  ((Fr(4, 3), 3), 6)):
    print(f"== seed {seed} ==", flush=True)
    n, viol, dt = audit(seed, p)
    print(f"seed {seed}: {n} states, violations beyond seed-level: "
          f"{len(viol)} {viol[:10]} ({dt:.0f}s)", flush=True)
print("FC1 AUDIT COMPLETE")
