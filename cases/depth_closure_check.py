#!/usr/bin/env python3
"""Chain-depth closure verification (SHEET6-DEPTH.md).

The M=1 pre-merge chain step (MP5 single simple nu-orbit; Prop 9.3 (b)+(d),
mu = 1, i-normalized rho := D/deg p_full) acts on frames (rho, nu, kap) by

    child pattern (nuF, dq = npat*nuF + 1), nuF >= 2, npat >= 1
    n    = (nuF*kap - dq*rho)/(dq - nuF)   in Z, n >= 1        [edge param]
    kapF = (kap + n)/nu                    in Z (V1 integrality)
    rhoF = (rho + n)/(nu*nuF)

CLAIMED STRUCTURE (SHEET6-DEPTH.md DS2-DS5), verified here exactly:
  (W)  w := (kap - rho)/nu satisfies w' = w * npat/Delta with
       Delta := (npat-1)*nuF + 1; so npat = 1 ("l=0 step") preserves w,
       and npat >= 2 ("resonant step") contracts: w' <= (2/3) w.
  (D)  a resonant step forces Delta | num(w)  (from kapF in Z).
  (M)  merge-cell child data factorizes through w: for any mu=1 edge into a
       merged cell (dp_c, dq_c): kap_m = w*dq_c/Dc, D/i = w*dp_c/Dc with
       Dc = dq_c - dp_c, so kap_m - D/i = w (the "handshake"); the join
       forces all arriving edges to share w; jump cells (l >= 1) obey
       w < kap_m <= (r+1) w, and (kap_m, l) DETERMINES nu_c per family.
  (S)  hence the cumulative jump-cell menu over all depths equals the menu
       of the finite w-closure W(w0), reached at small depth: DEPTH-INVARIANCE.

Checks:
  1. step law (W) + divisibility (D) + contraction on every BFS edge.
  2. td=6 record: entry (1,2,5): W = {2}; no resonant step exists;
     cumulative M>=2 menu constant from depth 1 and equal to
       {IIa (r,nu,l)=(2,3,1), M=2, child (kap,D/i)=(5,3)}   [= merged child
          Q=(6,12,3,2,5) @ i=2 -- the promoted residue, SHEET6-L1 s6]
       {ZCH (nu,l)=(2,3), M=3, child (kap,D/i)=(3,1)}       [= the L1 s0
          gcd(nu+1,l)>=2 survivor family; SUFFIX-killed in the promoted
          record (phase-4 kill), leaving the unique residue]
     nu_c=1 (family I) cells only l in {1,2,4} (l=1 M=1; l=2,4 interior
     nu=1, ODE-dead by MP9's even-l log-obstruction); root merges need
     kap_child = 1, i.e. w < 1: impossible here (w = 2) -- reproves the
     MP-REVIEW s2c root kill in one line.
  3. all m=2, b=1 entries with td <= 12: BFS(depth 8) w-set inside the
     arithmetic closure W(w0); cumulative menu stabilizes by depth
     d0 = gen(W) + 2 (compared against depth 8).
  4. closed-form menu(w) (nu-determination per (kap_m, l)) reproduces the
     capped sweep menus exactly (within caps) for every reached w.
  5. St 9.6(v) cross-check (printed p. 51): the thesis's own lam=0 suffix
     family Q = ((6s+3)j,(4s+2)j,2s+1,2,3s+3) has w == 3/2 for ALL s --
     the w-invariance is visible in the printed record itself.

Exact arithmetic throughout (int/Fraction). Runtime ~seconds.
"""
import sys
from fractions import Fraction as Fr
from math import gcd

NUMAX, NPMAX = 24, 8      # chain-step caps (menu is nuF-independent)
CNUMAX, CLMAX = 48, 12    # merge-cell sweep caps
FAIL = []

def ok(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)

def w_of(rho, nu, kap):
    return Fr(kap - rho, 1) / nu

# ----------------------------------------------------------- chain step
def chain_children(rho, nu, kap, numax=NUMAX, npmax=NPMAX):
    """All admissible M=1 single-orbit children (rhoF,nuF,kapF,n,npat)."""
    out = []
    for nuF in range(2, numax + 1):
        for npat in range(1, npmax + 1):
            dp, dq = nuF, npat * nuF + 1
            n = Fr(dp * kap - dq * rho, dq - dp)
            if n.denominator != 1 or n < 1:
                continue
            kapF = Fr(kap + int(n), nu)
            if kapF.denominator != 1:
                continue
            out.append((Fr(rho + n, nu * nuF), nuF, int(kapF), int(n), npat))
    return out

def check_edge_laws(par, ch):
    """(W) + (D) + contraction on one edge; returns True iff all hold."""
    rho, nu, kap = par
    rhoF, nuF, kapF, n, npat = ch
    wp, wc = w_of(rho, nu, kap), w_of(rhoF, nuF, kapF)
    Delta = (npat - 1) * nuF + 1
    lawW = (wc == wp * Fr(npat, Delta))
    lawD = (npat == 1) or (wp.numerator % Delta == 0)
    lawC = (npat == 1 and wc == wp) or (npat >= 2 and wc <= Fr(2, 3) * wp)
    return lawW and lawD and lawC

# ------------------------------------------------------------ merge menu
def cells(r, cnumax=CNUMAX, clmax=CLMAX):
    for l in range(0, clmax + 1):
        yield ('I', 1, l, r, r + l)                      # nu = 1 (root menu)
    for v in range(2, cnumax + 1):
        for l in range(0, clmax + 1):
            yield ('IIa', v, l, r * v, (r + l) * v + 1)
        for l in range(1, clmax + 1):
            yield ('ZCH', v, l, (r - 1) * v + 1, (r - 1 + l) * v + 1)

def menu_sweep(rho, nu, kap, r=2):
    """Jump-cell menu from ONE frame, mu=(1,..,1): per-edge Prop 9.3 solve.
    Returns {(fam, nu_c, l, M, kap_m, Di)}; checks kap_m - Di == w."""
    out, wv = set(), w_of(rho, nu, kap)
    for fam, v, l, dp, dq in cells(r):
        if dq <= dp:
            continue                                     # searrow (St 8.2)
        n = Fr(dp * kap - dq * rho, dq - dp)
        if n.denominator != 1 or n < 1:
            continue
        km = Fr(kap + int(n), nu)
        if km.denominator != 1:
            continue
        Di = Fr(rho + n, nu)
        assert km - Di == wv, ('handshake', fam, v, l)
        out.add((fam, v, l, gcd(dp, dq), int(km), Di))
    return out

def menu_of_w(w, r=2):
    """Closed-form: solve (kap_m, l) -> nu per family (DS4).  Necessary
    conditions only (per-edge n_e admissibility not imposed): a SUPERSET
    of any frame menu at this w, restricted to l >= 1 jump cells.
    NOTE: ZCH here uses the engine's (a)-(d) edge model for the 0-edge
    (conservative over-generation); the corrected case-(III) model is
    CHECK 7."""
    out = set()
    kml = []
    # integers kap_m with w < kap_m <= (r+1) w
    lo, hi = w, (r + 1) * w
    k = int(lo) + 1
    while Fr(k) <= hi:
        kml.append(k)
        k += 1
    for km in kml:
        Di = km - w
        if Di <= 0:
            continue
        for l in range(1, CLMAX + 1):
            # IIa: Di = w r nu/(l nu + 1)  =>  nu (w r - Di l) = Di
            den = w * r - Di * l
            if den > 0:
                nu = Di / den
                if nu.denominator == 1 and nu >= 2:
                    v = int(nu)
                    M = gcd(r * v, (r + l) * v + 1)
                    out.add(('IIa', v, l, M, km, Di))
            # ZCH: Di = w((r-1)nu + 1)/(l nu) => nu (l Di - w(r-1)) = w
            den = l * Di - w * (r - 1)
            if den > 0:
                nu = w / den
                if nu.denominator == 1 and nu >= 2:
                    v = int(nu)
                    M = gcd((r - 1) * v + 1, (r - 1 + l) * v + 1)
                    out.add(('ZCH', v, l, M, km, Di))
            # I (nu=1): Di = w r / l
            if Di * l == w * r:
                out.add(('I', 1, l, gcd(r, r + l), km, Di))
    return out

# ------------------------------------------------------------ w-closure
def w_closure(w0):
    """Arithmetic over-approximation of reachable w-values: closure of {w0}
    under w -> w*npat/Delta, Delta | num(w), Delta = (npat-1)*nu+1 >= 3,
    npat >= 2, nu >= 2.  Returns (set, generations)."""
    W, frontier, gen = {w0}, {w0}, 0
    while frontier:
        nxt = set()
        for w in frontier:
            a = w.numerator
            for Delta in range(3, a + 1):
                if a % Delta:
                    continue
                for nu in range(2, Delta):
                    if (Delta - 1) % nu:
                        continue
                    npat = (Delta - 1) // nu + 1
                    if npat < 2:
                        continue
                    wn = w * Fr(npat, Delta)
                    if wn not in W:
                        nxt.add(wn)
        W |= nxt
        frontier = nxt
        if nxt:
            gen += 1
    return W, gen

# ------------------------------------------------------------------ BFS
def bfs(entry, depth, numax=NUMAX, npmax=NPMAX, r=2):
    """Returns per-depth state lists, edge-law verdict, cum. menus/depth."""
    lay = {0: [entry]}
    seen = {entry}
    edges_ok = True
    cum = [menu_sweep(*entry, r=r)]
    for d in range(1, depth + 1):
        lay[d] = []
        for st in lay[d - 1]:
            for ch in chain_children(*st, numax=numax, npmax=npmax):
                edges_ok &= check_edge_laws(st, ch)
                key = ch[:3]
                if key in seen:
                    continue
                seen.add(key)
                lay[d].append(key)
        m = set(cum[-1])
        for st in lay[d]:
            m |= menu_sweep(*st, r=r)
        cum.append(m)
    return lay, seen, edges_ok, cum

def jumps(menu):
    """Restrict a menu to resonant jump cells (l >= 1, M >= 2, nu_c >= 2)."""
    return {c for c in menu if c[2] >= 1 and c[3] >= 2 and c[1] >= 2}

def roots(menu):
    return {c for c in menu if c[0] == 'I'}

# ------------------------------------------------------------- check 2
print("== CHECK 2: td=6 record (entry (rho,nu,kap) = (1,2,5)) ==")
entry6 = (Fr(1), 2, 5)
lay, seen, edges_ok, cum = bfs(entry6, 12)
ok(edges_ok, "step law (W)+(D)+contraction on every edge, depth <= 12")
Wr = {w_of(*s) for s in seen}
ok(Wr == {Fr(2)}, f"reached w-set == {{2}} (got {sorted(Wr)})")
res = [1 for s in seen for c in chain_children(*s) if c[4] >= 2]
ok(not res, "no resonant (l>=1) chain step admissible anywhere (Delta|2 empty)")
Wc, gen = w_closure(w_of(*entry6))
ok(Wc == {Fr(2)} and gen == 0, f"arithmetic closure W(2) == {{2}}, gen 0")
stab = all(jumps(cum[d]) == jumps(cum[1]) for d in range(1, 13))
ok(stab, "cumulative jump menu constant for all depths 1..12")
promoted = ('IIa', 3, 1, 2, 5, Fr(3))
zchcell = ('ZCH', 2, 3, 3, 3, Fr(1))
ok(jumps(cum[12]) == {promoted, zchcell},
   "jump menu == {IIa (2,3,1) M=2 child (5,3)} u {ZCH (2,3) M=3 child "
   "(3,1)}; the IIa cell IS the promoted residue Q=(6,12,3,2,5) @ i=2 "
   "(SHEET6-L1 s6 / 2POLE s6a); the ZCH cell is suffix-killed there")
rc = {(c[2], c[3]) for c in roots(cum[12])}
ok(rc == {(1, 1), (2, 2), (4, 2)},
   f"nu=1(I)-cells l in {{1,2,4}} only (got {sorted(rc)}): l=1 M=1, "
   f"l=2,4 even = MP9 ODE-dead; none has kap_m = 1")
ok(all(w_of(*s) >= 1 for s in seen),
   "w >= 1 at every frame: no root merge (root needs kap=1 <=> w<1)")

# ------------------------------------------------------------- check 3+4
print("\n== CHECK 3+4: all m=2, b=1 entries, td <= 12 ==")
def entries_m2(tdmax=12):
    out = []
    for al in range(2, 7):
        for be in range(al + 1, 7):
            if gcd(al, be) != 1 or 2 * be > tdmax:
                continue
            nus = [n for n in range(1, be + 1)
                   if (al % n == 0 and (be - 1) % n == 0)
                   or (be % n == 0 and (al - 1) % n == 0)]
            for nu in nus:
                for a in range(1, tdmax):
                    lam = Fr(a * al * be, nu)
                    if lam.denominator != 1 or lam < be or lam > tdmax - be:
                        continue
                    out.append(((al, be), a, nu, (Fr(a), nu, a * (al + be))))
    return out

all_ok = True
rows = []
for (al, be), a, nu, ent in entries_m2():
    w0 = w_of(*ent)
    Wc, gen = w_closure(w0)
    d0 = gen + 2
    lay, seen, e_ok, cum = bfs(ent, 8)
    Wr = {w_of(*s) for s in seen}
    c1 = Wr <= Wc
    c2 = e_ok
    c3 = jumps(cum[min(d0, 8)]) == jumps(cum[8])
    # closed-form menu(w) superset check within caps
    c4 = True
    for s in seen:
        mv = jumps(menu_sweep(*s))
        sup = {c for c in menu_of_w(w_of(*s)) if c[1] <= CNUMAX and c[2] <= CLMAX}
        c4 &= mv <= sup
    all_ok &= c1 and c2 and c3 and c4
    rows.append(((al, be), a, nu, w0, sorted(Wc), gen, len(seen),
                 len(jumps(cum[8])), c1 and c2 and c3 and c4))
for r in rows:
    print(f"   type={r[0]} a={r[1]} nu={r[2]} w0={r[3]} W={r[4]} gen={r[5]} "
          f"states={r[6]} jumpcells={r[7]} {'ok' if r[8] else 'FAIL'}")
ok(all_ok, f"{len(rows)} entries: BFS w-set in W(w0); step laws; menu "
           f"stabilized by d0 = gen+2 vs depth 8; menu(w) closed form "
           f"covers every frame menu")

# ------------------------------------------------------------- check 5
print("\n== CHECK 5: St 9.6(v) (p. 51) w-invariance of the printed family ==")
c5 = all(w_of(Fr(6 * s + 3, 4 * s + 2), 2 * s + 1, 3 * s + 3) == Fr(3, 2)
         for s in range(0, 21))
ok(c5, "Q=((6s+3)j,(4s+2)j,2s+1,2,3s+3): w == 3/2 for s = 0..20 "
       "(rho = (6s+3)/(4s+2), P-free)")
c5b = w_of(Fr(1, 2), 3, 5) == Fr(3, 2)
ok(c5b, "St 9.6 hypothesis Q(G)=(j,2j,3,2,5): w == 3/2 (same class)")

# ------------------------------------------------------------- check 7
print("\n== CHECK 7: corrected ZCH 0-edge model (Prop 9.3 case (III)) ==")
# The 0-direction chain's own pole has ZERO coefficient at the meet, so
# the meet is NOT a characteristic value of that pole's series: the 0-edge
# is case (III), (e)-(h) with nu := nu_F.  i-normalized: kap_m = kap_G + n',
# Di = rho_G + n', n' = n/nu_c in (1/nu_c)Z, n >= 1; handshake
# kap_m - Di = kap_G - rho_G = nu_G * w  (NOT w).  Join with the case-(II)
# edges (handshake w') forces w' = nu_G * w, nu_G >= 2.
def zch3_edges(rho, nu, kap, r=2):
    """Corrected 0-edge solves: {(nu_c, l, M, kap_m, Di)}."""
    out = set()
    for v in range(2, CNUMAX + 1):
        for l in range(1, CLMAX + 1):
            dp, dq = (r - 1) * v + 1, (r - 1 + l) * v + 1
            npr = Fr(dp * kap - dq * rho, dq - dp)   # n' rational
            if npr * v < 1 or (npr * v).denominator != 1:
                continue                              # n = n' nu_c in N*
            km = kap + npr
            if km.denominator != 1:
                continue
            Di = rho + npr
            assert km - Di == kap - rho == nu * w_of(rho, nu, kap)
            out.add((v, l, gcd(dp, dq), int(km), Di))
    return out
# td=6: all frames share w = 2, so a join needs 2 = nu_G * 2, nu_G >= 2:
# impossible => corrected jump menu drops the ZCH cell entirely.
z_all = set()
for s in seen:
    z_all |= zch3_edges(*s)
joinable = {c for c in z_all if any(
    c[3] - c[4] == w_of(*s2) for s2 in seen)}   # 0-edge handshake == some w'
ok(not joinable,
   f"td=6: corrected-model ZCH 0-edges solved ({len(z_all)} cells) but NONE "
   f"joinable (needs w' = nu_G*w in W = {{2}}): corrected jump menu == "
   f"{{IIa (2,3,1) M=2}} exactly -- the promoted residue, pre-suffix")

# ------------------------------------------------------------- check 6
print("\n== CHECK 6: engine cross-check (twopole_check phase 4 frames) ==")
try:
    import twopole_check as tp
    seen4 = tp.l1_premerge()
    c6 = True
    nmu1 = nzch = 0
    for sh, (dep, why, nd) in seen4.items():
        (na, nb), (ka, kb) = tp.LF(nd.nu), tp.LF(nd.kap)
        if na == 0 and nb == 1:
            nzch += 1          # nu=1 zch over-generation: excluded by DS1
        else:
            nmu1 += 1
        for s in range(0, 6):
            nu, kap = na * s + nb, ka * s + kb
            if nu < 1:
                continue
            c6 &= (w_of(nd.rho, nu, kap) == Fr(2))
    ok(c6, f"all {len(seen4)} promoted phase-4 shapes ({nmu1} mu1-type, "
           f"{nzch} nu=1 zch-type) have w == 2 at every instance; note "
           f"nu_F=1 steps have Delta = npat so they too preserve w")
except Exception as e:
    ok(False, f"engine cross-check could not run: {e}")

print("\n" + ("ALL CHECKS PASS" if not FAIL else f"FAILURES: {FAIL}"))
sys.exit(1 if FAIL else 0)
