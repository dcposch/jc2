# Hostile review: Sol's unbounded (1)–(13) family, pinned N = 6

Lane N6-FAMILY-REVIEW (Grok 4.6), 2026-09-03. Charged Sol submission
`ideation-20260903T1015Z-sol56.md` §2.3 (PROVED-HERE/UNREVIEWED), against
census-rebase §1 and branch-orbits v2. Frozen inputs in
`/tmp/jc2-lane.uLhiYA/inputs` matched 5/5 SHA-256; mismatch would have
stopped the lane:

```text
20f290f7e33a3b8a4f97d303751633b9d9b2df50ca8cbd0a46498856be5d5b2f  ideation-20260903T1015Z-sol56.md
55db4a9ef9021ef28d3a86dbd3e44d5e3a5aa1b72d61ba23043497f78ba94411  branch-orbits-v2-grok46-20260903.md
aaea3c345b1d53f561798f6a3e4352722f56c50a762f141dfe5e59cf35b1f276  knapsack.py
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  census-rebase-opus5-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full.py
```

Workspace `box/moh_skeleton_full.py` has the same hash. No other
`ideation-20260903T1015Z-*` file was opened, no running-lane report, no
`jc2-lean`, no ledger edit. Enumerator not modified. Desk CAS: sympy 1.12
and `fractions.Fraction`, one core. No exit-price assertion, so no
`charge_basis` line.

Charged claim (Sol §2.3): for every `a ≥ 0` and `L = 8a+5`, the skeleton
`n=21L`, `m=14L`, `M_1=−14L`, `M_2=7(3L+1)/4`, `M_3=21L−2`, `s=3`,
`V_2=1`, `V_3=5` satisfies Moh's printed (1)–(13) as implemented in
`box/moh_skeleton_full.py`; formal (UNI) `k=12` gives `N=6` exactly;
degrees `105, 273, 441, …`; first 21 members pass the census.
Consequence: `(1)–(13) + integral pinned N` is cofinally nonempty, so a
uniform theorem must use a datum outside the scalar skeleton. Branch-orbits
v2 overlay: `|O| = ∏_{j=2}^{s−1} ω_j` with `ω_j = A_j` on (10) and `1` on
(11); at `s=3` packing is exact; (10)-only packets have `k ∈ A_2 ℤ`, and
at `L=5` that is `k=18`, `N=9`, not `k=12`.

---

## 1. Algebra in `L` — (1)–(13) for every `a ≥ 0`

All identities below are sympy-exact on `a ≥ 0` (`L = 8a+5`), then checked
on `Skel` for `a = 0..20` plus `a ∈ {21, 50, 100, 200}`. They are not a
finite measurement.

**Integrality of `M_2`.** `3L+1 = 24a+16 = 8(3a+2)`, so
`(3L+1)/4 = 2(3a+2) ∈ ℤ` and `M_2 = 14(3a+2) = 42a+28 ∈ ℤ`.

**`d_j` from (5).** `d_1 = n = 21L`. `d_2 = gcd(21L, −14L) = 7L`.
`d_3 = gcd(7L, 7(3L+1)/4) = 7 · gcd(L, (3L+1)/4)`. Bezout:
`4 · (3L+1)/4 − 3L = 1`, hence that gcd is `1` and **`d_3 = 7` exactly,
not larger**. `d_4 = gcd(7, 21L−2)`. `21L−2 = 168a+103 ≡ 5 (mod 7)`, so
`d_4 = 1`. **`gcd(d_2, M_2) = d_3`** is the same identity.

**(2)** `m ∤ n`: `n/m = 3/2 ∉ ℤ`, independent of `a`.

**(6)** `s = 3 ∈ [3,5]`, `d_s = 7 ≥ 4`. The clause `s ≤ 5` is a
**consequence** for `n ≤ 100` (census-rebase §1.1: `K ≥ 4 · 2^{s−2}` and
`K ≤ n/3`), and **fails in general at `D = 192`** (first `s = 6` skeleton
`n=192`, `m=128`, `M = (−96,−80,−72,−68,190)`). This family has `s = 3`
for every `a`, so `s ≤ 5` is **not consumed**. Irrelevant here, as charged.

**(1) as implemented.** `m = 14L < n = 21L`. Moh's printed `n ≤ 100` is
his search bound, not a predicate of `moh_skeleton_full.py`; the
unbounded family is a statement about the enumerator, not about p. 200
l. 44.

**(3)/(4)** (Jacobian `= 1`, characteristic data) are geometric. The
scalar skeleton does not speak to them. Not a gap in Sol's *numerical*
claim; they are outside (1)–(13) as implemented.

**Windows (7) = Def 5.1(2).**
`i = 3`: `d_3/(n−M_3) = 7/2`, `V_4 d_3/d_4 = 7`, so `7/2 < 5 ≤ 7`.
`i = 2`: `n−M_2 = 7(9L−1)/4`, so `d_2/(n−M_2) = 4L/(9L−1)`, and
`V_3 d_2/d_3 = 5L`. Thus `4L/(9L−1) < 1 ≤ 5L`. The left half is
`4L < 9L−1 ⇔ 1 < 5L`, true for `L ≥ 5`. **Both windows for all `a ≥ 0`.**

**Def 5.1(3) radii** (the product in `moh_skeleton_full.Skel._delta`,
census-rebase §1):

```text
delta_3 = -1
delta_2 = 2(3L-1) / (3(5L-1))  =  (12a+7) / (6(5a+3))
delta_1 = 7/12                 (independent of L)
```

Reduced `gcd(12a+7, 6(5a+3)) = 1` for all `a ≥ 0` (Euclid: remainder 1).

**`A_2`.** `L_2 = lcm{den δ_3} = 1`, so `A_2 = den(δ_2) = 6(5a+3) =
3(5L−1)/4`. **All `a`.**

**(9)/(10)/(11) at `j = 2`.** `Q = V_3 d_2/d_3 = 5L`. Division:
`5L = 1 · A_2 + (5L+3)/4`, so `△_2 = 1`, `□_2 = 10a+7`.
**(10) is equality:** `V_2 = 1 ≤ △_2 = 1`, admits `V_2 = 1` for all `a`.
**(11) fails for all `a`:** `(5L−1)/A_2 = 4/3 ∉ ℤ`. Split is
**(10)-only**. Saturated: one NZ orbit of size `A_2` consumes `A_2` of
`Q = 5L` slots; leftover `□_2 = 10a+7 < A_2`; a second copy overfills
(`2 A_2 ≤ 5L ⇔ 20a ≤ −11`, never).

**`A_1` as a function of `a`.** `L_1 = A_2`, `A_1 = den(A_2 · 7/12) =
den(7(5a+3)/2)`. `5a+3` is odd iff `a` is even, and `gcd(7,2)=1`. Hence

```text
A_1 = 2  if a even
A_1 = 1  if a odd
```

Sol's `{1,2}` is exact, not a bag.

**(12)/(13).** `n* = e = 3`, `m* = d = 2`, `V_2 = 1`.
(12) `A_1 | 3` and `A_1 | 1`; (13) `A_1 | 2` and `A_1 | 2`.
Even `a`: `A_1=2` kills (12), (13) holds. Odd `a`: `A_1=1`, both hold.
p. 188 identity `A_1 | (e+d)V_2 − 1 = 4` holds in both cases.
**(12)∨(13) for all `a ≥ 0`.**

**`q`, `u`.** `q = (1−7/12)·2·3/(2+3) = 1/2`. `u = V_3 K/d_3 = 5L`.
Formal (UNI): `k=12 ≤ u=5L` for `L ≥ 5`, `N = k q = 6`.

**Verdict (1).** CONFIRMED for **all** `a ≥ 0`, not only measured
members. Every displayed quantity matches Sol. `M_2 ∈ ℤ`, `d_3 = 7`
exactly, `gcd(d_2,M_2)=d_3`, (2), (6), both windows, (10)-only, (12)∨(13),
`q=1/2`, `u=5L`. `s ≤ 5` not consumed.

---

## 2. Census membership

`census(n, Kmin=7L, full=True)` is the appropriate slice: `n/3 = 7L`, so
the family's `K` is the unique admissible `K` with `e=3`. Family row
means `(m, M_2, M_3, V) = (14L, 7(3L+1)/4, 21L−2, {2:1, 3:5})` with
`full_ok`.

| `L` | `n` | `Kmin` | V-assign | groups | family | `A_2` | `A_1` | 12/13 | wall |
|---:|---:|---:|---:|---:|---|---:|---:|---|---:|
| 5 | 105 | 35 | 9 | 8 | yes, `V_2={1}` | 18 | 2 | (13) | 0.004s |
| 13 | 273 | 91 | 44 | 38 | yes, `{1}` | 48 | 1 | (12)∧(13) | 0.015s |
| 21 | 441 | 147 | 1620 | 841 | yes, `{1}` | 78 | 2 | (13) | 0.416s |
| 29 | 609 | 203 | 97 | 80 | yes, `{1}` | 108 | 1 | (12)∧(13) | 0.043s |
| 37 | 777 | 259 | 153 | 115 | yes, `{1}` | 138 | 2 | (13) | 0.058s |
| 45 | 945 | 315 | 286582 | 90842 | yes, `{1}` | 168 | 1 | (12)∧(13) | 63.404s |

Six-`L` wall **63.941s** one core (dominated by `L=45`: `K=315=3^2·5·7`
has a long divisor-chain tree at a single `K`; the family row is still
emitted). `L=5` with default `Kmin=16`: **14 groups, 15 V-assignments,
family present `full_ok`**, 0.008s — matches census-rebase §6 at `D=105`
to the unit. First 21 members (`a=0..20`) via `census(Kmin=7L)` with
early-out: **21/21 found, `full_ok`, 0.931s, missing none.** Group of
the family row has unique `V_2=1` on every requested `L` (the (10)
saturation `△_2=1` plus (12)/(13) kill every other candidate).

**Verdict (2).** CONFIRMED. Family row appears with `full_ok` at every
charged `L` and at all 21 of Sol's claimed first members.

---

## 3. Orbit-admissible packets (branch-orbits v2)

Law as charged, exact at `s=3`: `|O|(D_1) = ω_2`, `ω_2 = A_2` on (10),
`1` on (11). This family is (10)-only, so `|O| = A_2 = 6(5a+3)`. Packet
`(w,c) = (A_2, A_2/2)` with `A_2/2 = 3(5a+3) ∈ ℤ`. Budget `w ≤ u=5L`
holds once; twice never. Unique orbit-admissible integer:

```text
k ∈ A_2 ℤ_{>0} ∩ [1, 5L]  =  {A_2}
N_orb = {3(5a+3)} = {15a+9}
```

| `a` | `L` | `n` | `A_2` | `u` | `k` adm. | `N_orb` | `k=12`? |
|---:|---:|---:|---:|---:|---|---|---|
| 0 | 5 | 105 | 18 | 25 | 18 | **9** | no |
| 1 | 13 | 273 | 48 | 65 | 48 | 24 | no |
| 2 | 21 | 441 | 78 | 105 | 78 | 39 | no |
| 3 | 29 | 609 | 108 | 145 | 108 | 54 | no |
| 4 | 37 | 777 | 138 | 185 | 138 | 69 | no |
| 5 | 45 | 945 | 168 | 225 | 168 | 84 | no |
| 20 | 165 | 3465 | 618 | 825 | 618 | 309 | no |

At `L=5` this is census-rebase / branch-orbits **`D=105` group A**:
`m=70`, `M=[28,103]`, `V_s=5`, `|O|=18`, UNI interval `{6..12}` shrinks
to `{9}`. Matches branch-orbits v2 §3.3 to the unit.

**`k=12` ever orbit-admissible?** `A_2 | 12` with `A_2 ≥ 18`: **never**,
all `a ≥ 0`.

**Smallest orbit-admissible `N` per `L`:** `15a+9 ≥ 9`, linear in `L`.

**Alive at `N ≥ 6` in the orbit-aware knapsack?** **Yes**, uniquely at
`N=15a+9`. `s=3` exact (Z 0–1 is vacuous: (11) fails). Cap never
relevant (one packet).

**Does Sol's consequence survive?** Split:

- **Formal (UNI) `k=12`, `N=6`.** CONFIRMED as Sol tagged it: a theorem
  about the printed numerical skeleton plus the size-1 knapsack, not
  about Galois-closed discs. Cofinal nonemptiness of
  `(1)–(13) + UNI-integral N=6` stands.
- **Orbit-aware pinned `N=6` on this family.** **REFUTED.** Orbit
  `N` grows without bound (`+15` per step in `a`). This ray is **not**
  a fixed-`N` laboratory under the charged orbit law. The Card 2
  “fixed-`N` cofinal family / valuated-MDS” target must be retyped:
  either keep this ray and replace `N=6` by `N=15a+9`, or move the
  `N=6` laboratory to the second family of §4.
- **“A uniform theorem must use a datum outside the scalar skeleton.”**
  SURVIVES, and is **stronger** under orbit correction: already this
  family keeps `(1)–(13) + orbit-integral N ≥ 6` cofinally nonempty
  (at unbounded `N`), and §4 supplies a second ray that keeps
  orbit-admissible **`N=6` itself** cofinally nonempty. Emptiness of
  the numerical (1)–(13) space, UNI or orbit, cannot prove JC2.

**Verdict (3).** CONFIRMED the orbit-size law on this family and the
`L=5` identification with group A (`k=18`, `N=9`). REFUTED `k=12`
orbit-admissibility. REFUTED fixed-`N=6` cofinality **of this family**.
CONFIRMED orbit-alive at `N ≥ 6` with `N=15a+9` unbounded. Consequence
of cofinal numerical nonemptiness: CONFIRMED (retyped: not pinned `N=6`
on *this* ray).

---

## 4. A second, orbit-consistent family with `N` bounded

Search: `s=3` slice of `census(..., full=True)` (byte-identical to the
full enumerator on `{105,117,88,75,84}`), keep `q=1/2`, `D ∈ [48,500]`.
**251** such V-assignments, wall **13.19s**. Among `V_2=1`, (10)-only,
`A_2 | 12` (so `k=12` is an orbit multiple and `N=6` is admissible
whenever `12 ≤ u`): **19 rows, none of them Sol's family.**

One infinite ray is visible in the `A_2=6` histogram, all `(d,e)=(2,3)`:

```text
D = 54, 117, 180, 243, 306, 369, 432, 495,   (then 558, …)
    = 9(7t+6) for t = 0, 1, 2, …
```

Closed form, for every integer `t ≥ 0`, with `P = 7t+6`:

```text
n=9P,  m=6P,  M_1=-6P,  M_2=4P,  M_3=9P-2,
s=3,   V_2=1, V_3=6t+5,
d_2=3P, d_3=P, d_4=gcd(P,2) ∈ {1,2}.
```

Sympy (deltas independent of `d_4`) plus `Skel` for `t=0..20, 30, 40, 50`
and census emission at `t=0,1,2,3`:

```text
delta_3=-1,  delta_2=1/6,  delta_1=7/12,
A_2=6 (constant),  A_1=2,
Q=18t+15,  TRI=3t+2,  SQ=3,
(10) only (1 ≰ 3 mod 6),  (13) holds,
q=1/2,  u=18t+15 >= 15,
|O|=6,  copies t_* <= 3t+2,
N_orb = {3,6,9,...,3(3t+2)}.
```

Two copies (`k=12`) fit for every `t ≥ 0` (`12 ≤ 18t+15`). **`N=6` is
orbit-admissible on every member.** Smallest orbit `N ≥ 6` is **6**,
bounded in the parameter; the degree `9(7t+6)` is unbounded. First
member `D=54` is already a rebase/orbit survivor (`N_orb={3,6}`).
`D=117` is branch-orbits v2 §3.2's live row
`m=78 M=[52,115] V_s=11 |O|=6 N={6,9,12,15}`.

This is **not** Sol's ray (`A_2` grows; `d_3=7` fixed; `(d,e)=(2,3)` is
shared, that is all). No other `A_2`-constant `(d,e)`-pure ray was
isolated as a closed form in `D ≤ 500` (the `A_2=12` bucket mixes
`(2,3),(3,4),(5,6)`). (11)-only `|O|=1` rows with `q=1/2` exist and
make UNI `k` orbit-legal, but `V_2` is typically `3` or `5` and `N`
hits `3,6,…` by a Z packet; they are scattered, not a second closed
family in this pass.

**Verdict (4).** CONFIRMED: an orbit-consistent family with **pinned
`N=6`** exists, cofinal in `D`. It is the `A_2=6` ray above, **not**
Sol's `L=8a+5` family. Sol's consequence (numerical cofinal
nonemptiness, even at orbit-pinned `N=6`) therefore **survives and
does not need his ray**. Geometric realisation of either ray is not
claimed.

---

## 5. Hostile checks

- **Could `d_3` jump above 7 for some `a`?** No: Bezout remainder 1.
- **Could (11) turn on and make `|O|=1`, restoring `k=12`?** No:
  `(5L−1)/A_2 = 4/3` identically.
- **Could two copies of the NZ packet hit `N=6`?** No: two copies
  overfill `u` for every `a`, and one copy has `N=15a+9 ≠ 6`.
- **Could mixing other `V_2` of the same group make `N=6`?** The
  family's group has unique `V_2=1` on every measured `L` (and
  `△_2=1` forbids any other (10) value). No mix.
- **Is `s ≤ 5` silently used?** No. Family `s=3`. First general `s=6`
  is `D=192`, irrelevant.
- **Did Sol already refuse the orbit injection?** Yes, §2.3(b): the
  `A_2 ∈ {18,13,17}` observation is tagged unproved and “not used in
  any count below.” The family in (f) is explicitly **formal UNI**.
  The hostility is not that he claimed `k=12` geometric; it is that
  the charged orbit law, now a PROVED-HERE input, removes this family
  from the fixed-`N=6` slot he assigned it in Card 2.
- **FALLACY-v2.** Flag/place/series: `A_2` is an orbit-size of
  `p(π)`-factors, not a count of actual bottom discs and not a cover
  series. Per-ray: one V-assignment, one packet. Carrier: UNI `k=12`
  and orbit `k=A_2` are numerical packets, not `FULL_ACTUAL_EXIT`.
  Floor/attainment: knapsack existence ≠ geometric realisation
  (`OPEN[STAR-REALISABILITY]` untouched). No `sat()`, no pole
  identity, no merge-free inference, no exit price.

---

## 6. OPENs (bounded, with cheapest test)

```text
OPEN[STAR-REALISABILITY]  (integration #17; untouched).  Geometric
   realisation of any packet of either family.

OPEN[SECOND-RAY-GEOM]  (new; the A2=6 ray of §4 as a geometric object).
   Bounded: the four members D=54,117,180,243, each the unique
   (10)-only V2=1 assignment above, packet k=12 / two copies of |O|=6,
   N=6.  Cheapest test: feed D=54 and D=117 into the moment engine
   Sol already specified for Card 2 (34+1 rows at D=105-scale is
   smaller here: n-m = 3P = 18,39 at the first two).

OPEN[SOL-CARD2-RETYPE]  (new; Card 2's laboratory).  Bounded: one
   choice, two options already computed — (i) keep L=8a+5 and run
   moments at N=15a+9 for a=0,1,2,3 (degrees 105,273,441,609);
   (ii) move N=6 to the A2=6 ray, same four D.  Cheapest: (ii) at
   D=54, one graded page.

OPEN[MOH-PROGRAM], OPEN[PROP-5.6-SHADOW], OPEN[NESTED-PACK],
OPEN[BRANCH-ORBITS] geometric existence: untouched.  Nested packing
   is exact on both families (s=3).
```

No other OPEN is filled by cap or analogy.

---

## 7. Typed block

```text
LANE          N6-FAMILY-REVIEW (Grok 4.6), 2026-09-03
CHARGED       Sol ideation-20260903T1015Z §2.3 family; census-rebase §1;
              branch-orbits v2 law; enumerator d20bf0841a1ba2b2.
PROVED-HERE   all displayed quantities of the L=8a+5 family as
              identities in a>=0 (sympy + Skel); d3=7 exactly by
              Bezout; (10) saturated TRI=1, (11) never; A1=2 (a even)
              / 1 (a odd); (12)v(13) all a; |O|=A2=6(5a+3);
              unique orbit N=15a+9; k=12 never orbit-admissible;
              second family n=9(7t+6), A2=6 constant, N=6 orbit-adm
              for all t>=0 (delta_2=1/6, q=1/2, (10)-only).
CONFIRMED     (1) algebra of Sol's family for ALL a>=0, including
              M2 in Z, d3=7, both windows, q=1/2, u=5L, (6) with
              s<=5 not consumed (fails generally at D=192);
              (2) census row + full_ok at L=5,13,21,29,37,45
              (six-L wall 63.941s) and first 21 members (0.931s);
              L=5 Kmin=16 reproduces 14 groups / 15 V-assign;
              (3) D=105 group A is k=18, N=9, not k=12;
              family orbit-alive at N>=6 with N=15a+9;
              UNI k=12 N=6 on this family as a FORMAL packet;
              (4) a second orbit-consistent N=6 family exists.
REFUTED       k=12 orbit-admissible on Sol's family, any a;
              this family as a fixed-N=6 laboratory under
              branch-orbits v2; Card 2's "pinned N=6" target on
              L=8a+5 without retyping N to 15a+9.
SURVIVES      cofinal nonemptiness of (1)-(13)+integral N, UNI or
              orbit; the claim that a uniform theorem must use a
              datum outside the scalar skeleton (strengthened:
              orbit-pinned N=6 is itself cofinal, via §4).
NOT CLAIMED   geometric realisation of either family; nested packing
              at s>3; emptying any degree; PLACE-LEDGER identity;
              Moh's unpublished program as a filter on either ray.
MEASURED      six L census as table §2; s=3 q=1/2 search D<=500:
              251 rows, 13.19s, 19 V2=1 (10)-only A2|12 rows,
              A2=6 (2,3) ray of length 8 in range.  Wall ~80s one
              core, peak at L=45 census 63s.
OPEN          STAR-REALISABILITY; SECOND-RAY-GEOM (4 members);
              SOL-CARD2-RETYPE (one binary choice); MOH-PROGRAM;
              PROP-5.6-SHADOW; NESTED-PACK; BRANCH-ORBITS geom.
ARTIFACTS     enumerator not modified.  No ledger edit.
```

<!-- BODY-END -->
