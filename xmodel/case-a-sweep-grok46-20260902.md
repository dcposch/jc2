# CASE-A-SWEEP — chart the case-(A) survivors at 8 <= N <= 16

Lane: `CASE-A-SWEEP`. Date: 2026-09-02. Agent: Grok 4.6.
Exact integer orbifold-cage enumeration, plus a cycle-type representation
gate on the small-N residual. No Groebner, no CAS decision procedure.
Driver in `/tmp`, not installed in `box/`. Instrument `box/cover_h1.py`
consumed unmodified.

## 0. Custody

Frozen charged copies were hashed with `shasum -a 256` **before any was
read**; 3/3 match the charge:

```text
fa52e816869fc689db23d5dfb6354be0cf88cb361f365dd9ff16f51c01d97883  homcover-transfer-opus5-20260902.md
fadc17c809e72d64a493fc1fb16a739d441474b401f191081303de3b003d7d62  homcover-transfer-review-gpt55-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  mprime-alln-h2-opus5-20260902.md
```

Below: **HT** = the transfer report, **HV** = its hostile review, **MI** =
MPRIME-ALLN-H2. Instrument, as run (identical to the file HT hashed):

```text
dfb90ce32f589aae00ce7f2d3188114bbf27396120a8da3d8e67c0145b5177b2  box/cover_h1.py
```

`python3 box/cover_h1.py` — 4/4 built-in controls PASS, including
`Z (+) Z/3` and the fail-closed convention discriminator. Enumerator
`/tmp/case_a_sweep.py` (SHA-256 `5a2a3b6572789cf5c91191eeec127330eb94d7049bf9f90c1884550d63e73aff`)
and representation driver `/tmp/case_a_rho.py` are session-local. No
charged file was edited.

No `charge_basis` line: this report asserts no new exit price. N=8
survivors remain `REPRESENTATIVE` group-theoretic data, not
`FULL_ACTUAL_EXIT`.

## 1. Verdict

```text
CUSP-A-EMPTY (4<=N<=7)     REPLAYED. Pair counts 0,0,4,22 match HT/HV
                           exactly; representation cheap-gate 0 on every
                           N=6 cell and every N=7 type-cell.
N=8 numerical cage         40 (p,q) at HT's bound 200 (match); 6 finite
                           pairs + 2 arithmetic families bound-free.
N=8 representation         HT's four base cells reproduced: (2,3) 16,
                           (3,4) 6, (4,3) 4, all homology + COR 7.2.
                           Extra finite pairs (2,7),(2,15) and mirrors
                           die at the meridian gate (0 cheap survivors).
                           Family q=4D collapses: (3,20),(3,28),(3,44)
                           each still 6, mer type (4).
N=8 + 7.B / Lemma A / (K)  DOES NOT EMPTY the residual. (K)+Lemma 4.3
                           kill the two-birational reading of mer (3,3);
                           the single dicritical (2,3) and the (1,4)
                           family remain. OPEN[HOMCOVER-CUSP-A-N8] stays.
8..16 numerical            nonempty at every N. Finite-pair counts grow
                           irregularly (dip at primes); unbounded
                           s=1 families dominate truncated pair counts.
```

## 2. Enumerator, gates, and what a tuple is

Gates, in order, are exactly HT §5.3–§5.4 as confirmed by HV §9:

* `M | N`, `M >= 2`, `kappa = N/M`;
* `2 <= j <= a <= N-2`, so `W = N-a >= 2`;
* ORBIFOLD-CAGE `(C-1)`: `s + s' = M + 2 - j` with `1 <= s,s' <= M`
  (CENTRAL-RANK `r = j-1` is already substituted);
* integer partitions of `M` into `s` (resp. `s'`) parts: local degrees
  `m_i | p`, `l_j | q`, `sum m_i = sum l_j = M`;
* HT §7.3 reconstruction of `p` (symmetrically `q`): if `s = 1` then
  `p = M D` with `D >= 1` and `gcd(D, kappa) = 1` (unbounded); if
  `s >= 2` then `p = lcm(m_i) >= 2`, cone orders `D_i = p/m_i`
  pairwise coprime, `gcd(D_i, kappa) = 1` (`(C-2)`, `(C-3)`);
* `p, q >= 2`, `gcd(p, q) = 1` (cross-side coprimality of cone orders
  is then free);
* CUSP-PARITY: some `eps in {±1}` with `(-1)^{N-s} = eps^q` and
  `(-1)^{N-s'} = eps^p`, realised by a partition of `W` into parts
  `>= 2` (7.B: `mu_l >= 2`) via `eps = (-1)^{W - n_cyc}`.
  Realisability: `W = 2` forces `eps = -1`; `W = 3` forces `eps = +1`;
  `W >= 4` both. In particular `j = N-2` admits only `eps = -1`.

Both-unbounded (`s = s' = 1`) is empty: `p` and `q` are both multiples
of `M >= 2`. `(C-4)` is the identification of `s, s'` with cycle counts
of `rho(alpha), rho(beta)`, so the implied cycle types are
`alpha ~ (m_i kappa)_i`, `beta ~ (l_j kappa)_j`.

A **pair** is a unique `(p, q)`. A **tuple** is
`(p, q, j, M, kappa, s, s', alpha-type, beta-type, a, mer, eps)`.
Unbounded `D`-families are truncated only for listing; the exact
objects are the finite cells plus the arithmetic progressions of §5.

This is the numerical cage. The representation gate (transitivity,
meridian type, `cover_h1` torsion-free of rank `j`, COR 7.2
nonregular) is run on N <= 8 and on selected N = 9 cells; it is **not**
claimed for N >= 10.

## 3. Control: N <= 7 emptiness, exact match

```text
N   bound     pairs   expected (HT/HV)   tuples
4   any       0       0                  0
5   any       0       0                  0
6   any       4       4                  4
7   130       22      22                 26
7   218       36      36  (HT "36 cells")  —
8   200       40      40                 120
```

N = 6 pairs, verbatim: `(2,3), (2,5), (3,2), (5,2)`. Each is the unique
tuple `j=3, M=6, kappa=1`, meridian `(2,)` at `a=4`, `eps=-1`. Cycle
types `(2,2,2)/(3,3)` and `(2,2,2)/(5,1)` and mirrors.

N = 7 pairs at `p,q <= 130`, verbatim (HV's 22):

```text
(2,3), (2,7), (2,21), (2,35), (2,49), (2,63), (2,77), (2,91), (2,105), (2,119),
(3,2), (3,10),
(7,2), (10,3), (21,2), (35,2), (49,2), (63,2), (77,2), (91,2), (105,2), (119,2)
```

Finite: `(2,3), (3,2), (3,10), (10,3)`. Family: `p=2, q=7E` with `E` odd
(and the swap). Bound `2 M^2 + 120 = 218` extends `E` through 31 and
reproduces HT's 36.

**Representation cheap-gate (this lane, MEASURED).** Every N=6 cell:
relation-satisfying transitive pairs exist (600 for `(2,3)`, 2160 for
`(2,5)`), cheap survivors **0**. Every N=7 type-cell, including family
members `E = 1, 3, 5, 7` (meridian word changes with `E`): cheap
survivors **0**. Homology is not reached. This is HV's "H2+cage+parity
cheap survivors = 0", replayed on the cycle-type restricted search
rather than on all of `S_N^2`; terminal count identical.

N = 4, 5 have no numerical cells, so the desk proofs of HT §5.5 are
not re-opened.

## 4. Census 8 <= N <= 16

Truncated pair counts use HT's listing bounds where they exist
(N=8: 200) and `2 N^2 + 120` otherwise. Bound-free counts (finite
pairs + arithmetic families) do not depend on a cap.

```text
N    bound   pairs  tuples  finite_pairs  n_families
 8     200      40     120             6           2
 9     282     102     518            10           4
10     320      64      96            20           2
11     362      42     120            10           2
12     408      82     536            28           2
13     458     128     380             8           6
14     512      70     776            20           2
15     570     386   12924            48           8
16     632     382    7770            50          10
```

At the uniform bound `2 N^2 + 120`, N=8 has 48 pairs (the extra eight
are further `D` in the `(3, 4D)` family). Finite-pair lists and family
keys for N=10..16 are the appendix.

The pair count does **not** grow monotonically. It dips at several
primes (N=11: 42; N=13's 128 is family-heavy, only 8 finite). The
jumps at N=15, 16 are composite `M` supplying more `s=1` families.
Finite pairs grow slowly then jump: 6, 10, 20, 10, 28, 8, 20, 48, 50.

## 5. N = 8 tuples, verbatim

Forty pairs at `p, q <= 200`. Each pair has unique
`(j, M, kappa, s, s', alpha, beta)`; meridians listed.

**Finite (6 pairs).**

```text
(p,q)=(2,3)  j=2 M=4 kappa=2 s,s'=2,2  alpha=(4,4) beta=(6,2)  cones_q=(3)
  mers: a=2 mer=(4,2); a=2 mer=(3,3); a=3 mer=(5); a=4 mer=(2,2); a=5 mer=(3)
  eps=+1
(p,q)=(3,2)  mirror: alpha=(6,2) beta=(4,4); same meridians
(p,q)=(2,7)  j=4 M=8 kappa=1 s,s'=4,2  alpha=(2,2,2,2) beta=(7,1)  cones_q=(7)
  mers: a=4 mer=(2,2); a=5 mer=(3)   eps=+1
(p,q)=(7,2)  mirror
(p,q)=(2,15) j=4 M=8 kappa=1 s,s'=4,2  alpha=(2,2,2,2) beta=(5,3)  cones_q=(3,5)
  mers: a=4 mer=(2,2); a=5 mer=(3)   eps=+1
(p,q)=(15,2) mirror
```

**Family (34 truncated pairs, 2 arithmetic progressions).**
`M=4`, `kappa=2`, `j=3`. `D` odd, `gcd(D, 3)=1`, `4D <= 200`:

```text
D in {1,5,7,11,13,17,19,23,25,29,31,35,37,41,43,47,49}   (n=17)
q-family: (p,q)=(3, 4D), s,s'=2,1, alpha=(6,2), beta=(8), cones_p=(3) [and (D) if D>1]
p-family: (p,q)=(4D, 3), s,s'=1,2, alpha=(8),   beta=(6,2)
mers (both): a=3 mer=(3,2); a=4 mer=(4); a=6 mer=(2)   eps=-1
pairs: (3,4), (3,20), (3,28), ..., (3,196) and the 17 swaps
```

This is HT's `q ≡ 4 (mod 8)`, `gcd(q, 3)=1` family: `4 · odd = 4 (mod 8)`.
`D=1` is the base cell `(3,4)` / `(4,3)`.

## 6. N = 9 tuples

102 pairs at `p, q <= 282`. Bound-free: 10 finite + 4 families.

**Finite (10), verbatim.**

```text
(2,3)  j=3 M=9 kappa=1 s,s'=5,3  alpha=(2,2,2,2,1) beta=(3,3,3)
  mers a=3 (4,2)/(3,3); a=4 (5); a=5 (2,2); a=6 (3)   eps=+1
(3,2)  mirror
(3,4)  j=5 M=9 kappa=1 s,s'=3,3  alpha=(3,3,3) beta=(4,4,1)
  mers a=5 (2,2); a=6 (3)   eps=+1
(4,3)  mirror
(3,8)  j=6 M=9 kappa=1 s,s'=3,2  alpha=(3,3,3) beta=(8,1)   mer a=7 (2)  eps=-1
(8,3)  mirror
(3,14) j=6 M=9 kappa=1 s,s'=3,2  alpha=(3,3,3) beta=(7,2)   mer a=7 (2)  eps=-1
(14,3) mirror
(3,20) j=6 M=9 kappa=1 s,s'=3,2  alpha=(3,3,3) beta=(5,4)   mer a=7 (2)  eps=-1
(20,3) mirror
```

**Families (exact arithmetic).** `D` with `gcd(D, kappa)=1` and
`gcd(M D, p_or_q)=1`; truncated `M D <= 282` in the pair list.

```text
(F9.1) q=3D, p=2, j=2, M=3, kappa=3, s,s'=2,1, alpha=(6,3), beta=(9)
       D ≢ 0 (mod 3); D-sample 1,5,7,11,...   [D=1 is (2,3) at this (j,M)]
(F9.2) p=3D, q=2,  mirror of F9.1, alpha=(9), beta=(6,3)
(F9.3) q=9D, p=2, j=5, M=9, kappa=1, s,s'=5,1, alpha=(2,2,2,2,1), beta=(9)
       D odd (else gcd(2,9D)=2)
(F9.4) p=9D, q=2,  mirror of F9.3
```

The 102 truncated pairs are exactly the 10 finite pairs together with
the members of F9.1–F9.4 inside the bound. Equivalently, the `(2, q)`
column is all `q ≡ 3 (mod 6)` up to 279, plus the four finite extras
`(3,4),(3,8),(3,14),(3,20)` and all swaps.

## 7. N = 8 representation, then 7.B / Lemma A / (K)

Cycle-type search, left-action homomorphisms, `cover_h1` via
`to_transport_convention`. Relator `alpha^p beta^{-q}`.

**Fixed-alpha counts, matching HT §5.5 / HV §6.**

```text
(2,3)  alpha fixed = (1,2,4,6,0,7,5,3) type (4,4)
       32 of 3360 type-(6,2) betas have alpha^2=beta^3 (all transitive);
       16 cheap; 16 homology rank 2, torsion-free, |G|>8.
       All 16 have a=2, mer=(3,3).   MATCH 16.
(3,4)  alpha fixed type (6,2): 48 relation, 6 cheap, 6 homology
       nonregular; all a=4, mer=(4).   MATCH 6.
(4,3)  alpha fixed an 8-cycle: 4 homology nonregular, mer=(4).  MATCH 4.
```

Family collapse, MEASURED not proved: the same fixed `(6,2)` alpha
gives 6 survivors of mer type `(4)` at `q = 4, 20, 28, 44`. For an
8-cycle, `beta^{4D} = beta^4` whenever `D` is odd, so the relation
`alpha^3 = beta^{4D}` is independent of `D`; the meridian word
`alpha^e beta^f` does change, and still lands on type `(4)`.

**Extra finite cells die.** `(2,7)`: 604800 transitive relation pairs,
cheap 0. `(2,15)`: 282240 transitive relation pairs, cheap 0. Mirrors
identical. These are numerical-cage only; they are not HT's 192.

So the N=8 representation residual is exactly HT's four base cells
plus the `(3, 4D)` / `(4D, 3)` family.

**Promoted geometric arsenal, applied honestly.**

* **7.B budget.** Already in the cage as `mu_l >= 2`. For mer `(3,3)`,
  `W=6`, either one dicritical `(s, mu)=(2, 3)` (`R=1`) or two
  `(1,3)+(1,3)` (`R=0`); both satisfy `2 sum s_l <= W`. For mer `(4)`,
  unique reading `(1,4)`, `R=0`. 7.B does not kill either survivor.
  The nodal-section bound `R <= W/2 - 1` is a case-(B1) tool; applying
  it here would be a profile identification, and is not done.
* **Lemma A / H3.** Case (A) already uses `D~ ≅ A^1` and one place at
  infinity (Lin–Zaidenberg substrate). `{x^p = y^q}` satisfies it.
  No extra numerical constraint.
* **`(K)` excess ledger.** Unique unibranch cusp, `K_p = a - 1`,
  `a_p = 1` (MI Prop. 6.1). `(C3)`: `#{K_p > 0} <= R + beta` with
  `beta = 1` is `1 <= R + 1`, free.
  The one sharp kill: mer `(3,3)` read as two dicriticals each
  `s_l = 1`. Lemma 4.3 (each `s_l = 1` contributes `k_t >= 1` at the
  NI place) plus additivity of `K_p` gives `K_p >= 2`, against
  `a - 1 = 1`. So the two-birational reading is dead.
  The single-dicritical reading `(2, 3)` has `R=1`, `K_p=1`, compatible
  with RH on a degree-2 map `A^1 -> A^1`.
  For `(3, 4D)`: `a=4`, `K_p=3`, one dicritical `(1, 4)`, `R=0`.
  Lemma 4.3 gives `K >= 1`; `K=3` means the unique `t` over the cusp
  has `mu_t = 7`. Not a contradiction in MI.

**FULL promoted arsenal survivors at N=8:** the trefoil cell
`(2,3)/(3,2)` with dicritical `(s, mu)=(2, 3)`, `a=2`, `j=2`, `M=4`,
`kappa=2`, `|rho(G)|=24`; and the family `(3, 4D)/(4D, 3)` with
dicritical `(1, 4)`, `a=4`, `j=3`, `M=4`, `kappa=2`, `|rho(G)|=192`.
Both remain `REPRESENTATIVE`. `OPEN[HOMCOVER-CUSP-A-N8]` is not closed.

## 8. Structure, and a typed conjecture

Numerical pair counts neither stabilize nor empty. They are the sum of
a slowly growing finite set and a handful of `s=1` arithmetic
progressions whose truncated length is `Θ(N)` at the `2 N^2` bound
and would be infinite without a cap. Parity of `N` is not a kill:
both even and odd N >= 8 are nonempty. A usable congruence is local
to each family (N=8: `q ≡ 4 (mod 8)`, `gcd(q, 3)=1`; N=9: the `(2, q)`
column is `q ≡ 3 (mod 6)`).

The representation gate is the actual thinning. At N=6, 7 every
numerical cell is `kappa=1` and dies at the meridian. At N=8 the two
`kappa=1` finite extras die the same way; the two `kappa=2` cells
live. At N=9, MEASURED:

```text
finite (2,3) M=9 kappa=1 types (2^4 1)/(3^3): one alpha, all 2912
  type-(3,3,3) betas satisfy the relation (both sides identity);
  cheap 0. Cycle type is a single conjugacy class, so 0 for one
  alpha is 0 for all. EMPTY at this cell.
finite (3,4) M=9 kappa=1: 11340 relation, cheap 0. EMPTY.
family F9.1 D=1, (2,3) j=2 M=3 kappa=3 types (6,3)/(9):
  18 relation, 6 cheap, 6 homology rank 2, nonregular, mer=(6) a=3.
  NONEMPTY. This is the N=9 trefoil, at the small-M high-kappa slot.
```

> **CONJECTURE (CUSP-A-KAPPA).** Under H2, in case (A), every
> numerical cage cell with `kappa = 1` fails the meridian cycle-type
> gate at every `N`. Representation-level survivors, when they exist,
> sit in the cells with `kappa >= 2` (equivalently `M <= N/2`),
> typically the trefoil `(2,3)` and the `(3, 4D)` family and their
> swaps, at the unique `(j, M)` the cage assigns to that `kappa`.

Evidence: N=6,7 all cells `kappa=1`, all cheap-empty; N=8 `kappa=1`
extras cheap-empty, `kappa=2` cells live; N=9 `kappa=1` finite
`(2,3)/(3,4)` cheap-empty, `kappa=3` trefoil family live. Not proved:
the conjugacy reduction used at N=9 `(2,3)` does not run for a cell
whose `alpha`-type splits into more than one conjugacy class in the
normaliser, and N >= 10 was not representation-gated. Status:
conjecture, not a theorem.

## 9. Negative control (over-constraining)

Drop CUSP-PARITY, keep every other gate, bound 200:

```text
N=4  pairs=2   (2,3), (3,2)     <-- HT's "without the parity gate" leftover
N=5  pairs=40  (unbounded 5D family appears)
N=6  pairs=10  the 4 plus (3,4),(3,5),(4,3),(4,5),(5,3),(5,4)
N=7  pairs=46
```

N=4 is the designed negative control: the numerical cage with
CENTRAL-RANK + ORBIFOLD-CAGE + Kurosh-divisor repair but without
parity admits exactly the cell HT's second N=4 proof then kills by
the trefoil/transposition argument. Survivors appear; the enumerator
is not over-constrained into a spurious empty set. Restoring parity
kills them because `j = N-2` forces `eps=-1` while both-even `s, s'`
demand `eps=+1`.

## 10. FALLACY-v2

* **Flag/place/series.** Case (A) only. `G ≅ G_{p,q}` is HT's
  Lin–Zaidenberg identification, not re-identified with `Gamma_infty`
  or a germ. (B3) is not touched. NODAL-ALL-N's `R`-bound is not
  transported onto the cusp.
* **Carrier/attainment.** Every surviving cell is `REPRESENTATIVE`.
  No Keller map is asserted.
* **Floor/attainment.** `r = j-1` is HT's equality, consumed. Truncated
  pair counts are listing floors on unbounded families, not attainment
  of a geometric count.
* **Prime label.** `s'` is the q-side preimage count; dicritical `s_l`
  is a different symbol and is only used in §7.
* **No gap by cap.** N >= 10 representation is typed un-run.
  Family collapse is MEASURED on the listed `D`, not proved. Where
  `(K)` does not kill, the residual is reported.

## 11. Typed verdict block

```text
LANE              CASE-A-SWEEP
CHARGE            chart case-(A) survivors 8<=N<=16 with reviewed cage;
                  apply 7.B / Lemma A / (K) at N=8; structure; controls.

N<=7 CONTROL      MATCH HT/HV. pairs 0,0,4,22. N=6 and N=7 representation
                  cheap-gate 0 on every type-cell (this lane).
N=8 NUMERICAL     40 pairs at bound 200, MATCH. 6 finite + family (3,4D).
N=8 RHO           (2,3) 16, (3,4) 6, (4,3) 4, family collapse on D=1,5,7,11.
                  (2,7),(2,15) cheap 0.
N=8 GEOMETRY      7.B and Lemma A do not kill. (K)+Lemma 4.3 kill only
                  the two-(1,3) reading of mer (3,3). Residual nonempty.
8..16             numerical nonempty every N. Finite pairs 6,10,20,10,28,
                  8,20,48,50. Families 2,4,2,2,2,6,2,8,10.
N=9 RHO (spot)    kappa=1 finite (2,3) and (3,4) cheap 0; kappa=3 trefoil
                  family 6 homology survivors, mer=(6), a=3.

CONJECTURE        CUSP-A-KAPPA: kappa=1 cells die at the meridian gate;
                  survivors live at kappa>=2. Evidence in §8. TYPED
                  conjecture.

NEGATIVE CONTROL  parity OFF: N=4 admits (2,3),(3,2). Not over-constrained.

NOT CLAIMED       geometric realisation; anything about (B3); all-degree
                  JC2; N>=10 representation emptiness; a proof of family
                  collapse.

CONSUMED          HT CENTRAL-RANK, ORBIFOLD-CAGE, CUSP-PARITY, CUSP-A-EMPTY
                  (at HV's confirmed typing). MI Lemma A, 7.B', (K),
                  Lemma 4.3, Prop. 6.1, COR 7.2. All at banked typing.
```

## Appendix. N=10..16, machine-readable

Bounds `B(N)=2 N^2+120`. `finite` = pairs with `s,s' >= 2`. Families
are `p=M D` or `q=M D` with `gcd(D,kappa)=1` and `gcd(M D, other)=1`.

```text
# N=10 B=320 pairs=64 finite=20 families=2
finite: (2,3),(2,5),(2,9),(2,21),(3,2),(3,4),(3,5),(3,8),(4,3),(4,5),(4,9),(4,21),(5,2),(5,3),(5,4),(8,3),(9,2),(9,4),(21,2),(21,4)
fam q=10D p=3 j=7 M=10 kappa=1 s,s'=4,1 alpha=(3,3,3,1) beta=(10) a=8 mer=(2)
fam p=10D q=3  (swap)

# N=11 B=362 pairs=42 finite=10 families=2
finite: (2,5),(5,2),(5,6),(5,18),(5,24),(5,28),(6,5),(18,5),(24,5),(28,5)
fam q=11D p=2 j=6 M=11 kappa=1 s,s'=6,1 alpha=(2^5,1) beta=(11) a in {6,7,9}
fam p=11D q=2  (swap)

# N=12 B=408 pairs=82 finite=28 families=2
finite: (2,3),(2,5),(2,9),(2,11),(2,35),(3,2),(3,4),(3,5),(3,8),(3,10),(3,11),(3,35),(4,3),(4,9),(4,11),(4,35),(5,2),(5,3),(8,3),(9,2),(9,4),(10,3),(11,2),(11,3),(11,4),(35,2),(35,3),(35,4)
fam q=6D p=5 j=5 M=6 kappa=2 s,s'=2,1 alpha=(10,2) beta=(12)
fam p=6D q=5  (swap)

# N=13 B=458 pairs=128 finite=8 families=6
finite: (2,3),(3,2),(3,4),(3,22),(3,40),(4,3),(22,3),(40,3)
fam q=13D p=2 j=7 M=13 kappa=1 s,s'=7,1 alpha=(2^6,1) beta=(13)
fam q=13D p=3 j=9 M=13 kappa=1 s,s'=5,1 alpha=(3^4,1) beta=(13)
fam q=13D p=4 j=10 M=13 kappa=1 s,s'=4,1 alpha=(4^3,1) beta=(13)
and three swaps

# N=14 B=512 pairs=70 finite=20 families=2
finite: (2,7),(2,13),(2,33),(2,45),(4,7),(4,13),(4,33),(4,45),(6,7),(6,13),(7,2),(7,4),(7,6),(13,2),(13,4),(13,6),(33,2),(33,4),(45,2),(45,4)
fam q=7D p=3 j=5 M=7 kappa=2 s,s'=3,1 alpha=(6,6,2) beta=(14)
fam p=7D q=3  (swap)

# N=15 B=570 pairs=386 finite=48 families=8
finite: (2,3),(2,5),(2,7),(3,2),(3,5),(3,7),(3,10),(3,14),(3,26),(3,44),(3,56),(5,2),(5,3),(5,6),(5,7),(5,12),(5,14),(5,18),(5,26),(5,44),(5,56),(6,5),(6,7),(7,2),(7,3),(7,5),(7,6),(7,10),(7,12),(7,18),(7,26),(7,44),(10,3),(10,7),(12,5),(12,7),(14,3),(14,5),(18,5),(18,7),(26,3),(26,5),(26,7),(44,3),(44,5),(44,7),(56,3),(56,5)
fam M=3 kappa=5 p=2 q=3D j=2 alpha=(10,5) beta=(15)
fam M=5 kappa=3 p=2 q=5D j=3 alpha=(6,6,3) beta=(15)
fam M=5 kappa=3 p=4 q=5D j=4 alpha=(12,3) beta=(15)
fam M=15 kappa=1 p=2 q=15D j=8 alpha=(2^7,1) beta=(15)
and four swaps

# N=16 B=632 pairs=382 finite=50 families=10
finite: (2,3),(2,5),(2,7),(2,15),(2,39),(2,55),(2,63),(3,2),(3,4),(3,5),(3,8),(3,14),(3,55),(4,3),(4,5),(4,7),(4,15),(4,39),(4,55),(4,63),(5,2),(5,3),(5,4),(5,8),(5,12),(5,14),(5,39),(5,63),(6,7),(7,2),(7,4),(7,6),(7,15),(8,3),(8,5),(12,5),(14,3),(14,5),(15,2),(15,4),(15,7),(39,2),(39,4),(39,5),(55,2),(55,3),(55,4),(63,2),(63,4),(63,5)
fam M=4 kappa=4 p=3 q=4D j=3 alpha=(12,4) beta=(16)   [N=8 family, scaled]
fam M=8 kappa=2 p=7 q=8D j=7 alpha=(14,2) beta=(16)
fam M=8 kappa=2 p=15 q=8D j=7 alpha=(10,6) beta=(16)
fam M=16 kappa=1 p=3 q=16D j=11 alpha=(3^5,1) beta=(16)
fam M=16 kappa=1 p=5 q=16D j=13 alpha=(5^3,1) beta=(16)
and five swaps
```

Replay: `python3 /tmp/case_a_sweep.py control` (pair counts 0,0,4,22,40
and the parity-off N=4 pair `(2,3)`); `python3 /tmp/case_a_rho.py n6`
and `n8-23-fixed` / `n8-34-fixed`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `21236`.
- Body SHA-256:
  `225bd8676d5521f20493f9bf4b4c219e3f6feea19e05f60d4c48c992a49af0a4`.
- Frozen basis: `aedb8c8828f318c1030be47c336c24adb87427d2`.
