# Desk lane: MF-DEFECT and MULT-VS-BETA

Lane: `MF-DEFECT-MULT-VS-BETA`. Date: 2026-09-02. Agent: grok-4.6.
Desk derivation plus exact integer enumeration (`python3`; no Groebner, no
AWS, no ledger edit, no `jc2-lean`). No `charge_basis` line: this report
asserts no new exit price.

## 0. Custody, typing, scope

The four frozen charged copies were hashed with `shasum -a 256` **before any
was read**; all four match the charge exactly:

```text
4fa4b5f60692ade07b3ce45405ab2623edb4ef3aef1174e34beaf2373ce2f2a4  meridian-floor-sharpen-opus5-20260902.md
32c043320d11b619ef717cbb2dc5f3ca1ec7756abaa5f470d2ee0fb49dfe7b82  meridian-floor-sharpen-review-gpt55-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  mprime-alln-h2-opus5-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  horn-flagship-opus5-20260902.md
```

Abbreviations: **MFS** = MERIDIAN-FLOOR-SHARPEN producer; **MR** = its gpt-5.5
hostile review; **MI** = MPRIME-ALLN-H2; **HF** = HORN-FLAGSHIP.

Typing, as charged. MF-EXACT, LOC-MULT, MF-SHARP, SHARP-CHAU are consumed at
MR's **CONFIRMED** typing **with its repairs**: the S-known floor
`n >= ceil((N-1)/(W-S))` is distinct from the W-only table floor
`MFb = ceil((N-1)/(W-1))`, and equality `(g_L, theta_inf)=(0,1)` attains the
S-known floor, not the W-only relaxation unless `S=1`; LOC-MULT is a lower
bound under the orbit hypothesis `T_P = #` orbits of `rho(Loc_P)` on the `N`
sheets; no cell is a nonemptiness theorem; no `Z(G)=1` anywhere. MI and HF
are banked (`Lemma A`, `(L)`, `(K)`, `(C1)`-`(C3)`, Lemma 4.1–4.3, 7.B',
THEOREM PROFILE, N4-PIN). Case (A) is EMPTY (integration #9);
PERIPHERAL-RANK / MERIDIAN-SPAN are not used. Coordinator desk note
(~11:05Z, UNREVIEWED, negative) is consumed as a **prohibition**: the Suzuki /
Hà–Lê defect budget `nW - N + 1` is fully spent by `(K)`, so MF-DEFECT cannot
be decided by counting fibre defects.

## 1. Verdict, up front

```text
(Q1) OPEN[MF-DEFECT]   CLOSED, YES.
     For every noninvertible plane Keller map under H2 and every generic
     line L, 2 g_L + theta_inf >= 2. The S-known floor n >= ceil((N-1)/(W-S))
     is never attained. MF-EXACT upgrades to n(W-S) >= N.
     Bounded quantity decided: (g_L, theta_inf) with g_L=0 and theta_inf=1
     excluded; remaining range 0 <= g_L <= p_a(D_F), 1 <= theta_inf <= N,
     nS + theta_inf <= D_F, and 2 g_L + theta_inf >= 2.
     Mechanism: structure of the fibre of a polynomial submersion, not the
     defect budget. Polar branches of u o F are equinumerous in the fibre
     (covering of a product neighbourhood of infinity in C^2 \ A_F); Jac
     constant forces every irreducible component of every fibre to carry at
     least one polar branch; so theta_inf=1 implies every affine fibre of
     u o F is irreducible. A rational polynomial with all affine fibres
     irreducible has exactly one horizontal curve of degree 1 (Miyanishi–
     Sugie / Saito / Kaliman Euler, Neumann–Norbury Prop. 3), hence
     theta_L=1. MF-EXACT reads theta_L = nS + theta_inf = nS + 1 >= 4
     (S>=1 by 7.B', n>=3 by H2 + SMOOTH-KILL). Contradiction.

(Q2) OPEN[MULT-VS-BETA] CLOSED, NO.
     In (B3) at W=2, beta=1 is not forced for N>=5. Every value
     beta in {1,...,N-3} is counting-admissible under (L), (K), (C1)-(C3)
     and Lemma 4.3. The unique forcing is D_gap=0, which is N=4 (N4-PIN).
     Bounded quantity decided: beta in {1,...,N-3}, and the lower end is
     not a theorem for N>=5.
     N=5,6,7 types are listed in Sec 4. No Keller realisation is claimed.

Floor consequence. At W=2 one has S=1, W-S=1, so Q1 gives n_min >= N
for the whole column, independently of beta. This is the n-floor prize
the producer attached to a YES on Q2; Q1 supplies it without Q2. The
integer S-known floor ceil(N/(W-S)) exceeds ceil((N-1)/(W-S)) if and
only if W-S divides N-1; it is not a +1 at every cell of the Phi table.
The W-only MFb upgrades to ceil(N/(W-1)) iff W-1 divides N-1, hence at
every W=2 cell.
```

## 2. Recalled identities, at confirmed typing

Generic target coordinates `(u,v)`, generic line `L={u=gamma}`,
`h := u o F`, `C_L := F^{-1}(L) = {h = gamma}`. Because `Jac F` is a nonzero
constant, `dh` never vanishes: `h` is a polynomial **submersion**, `C_L` is
smooth and reduced, and `deg C_L = D_F := max(deg P, deg Q)` for generic `u`
(MR:100-105). Transitive monodromy of the restricted cover
`C_L \ F^{-1}(A_F) -> L \ A_F` makes `C_L` irreducible (MR:107-116).
Riemann–Hurwitz on the compactified `v`-map `pi : X_L -> P^1` of degree `N`
is MF-EXACT (MR:141-149, wording repair MR:33-36):

```text
n (W - S)  =  N - 2 + 2 g_L + theta_inf,
theta_L    =  n S + theta_inf,
chi(C_L)   =  N - n W.
```

Here `theta_inf` is the number of points of `X_L` over `infty` of the target
line `L` (places of `C_L` at which `v -> infty`); the `n S` remaining
source-infinity places of `C_L` lie over the `n` points of `L cap A_F`.
The banked S-known floor is `g_L >= 0`, `theta_inf >= 1`, i.e.
`2 g_L + theta_inf >= 1`, attained if and only if `(g_L, theta_inf)=(0,1)`.
The exact defect relative to that floor is `2 g_L + theta_inf - 1`.
SHARP-CHAU (MR:378-397): `n S + theta_inf <= D_F`.

7.B' forces `S >= 1` and, at `W=2`, `(s, mu)=(1,2)`, so `S=1`, `R=0`,
`a=N-2`, `D_gap=N-4`. SMOOTH-KILL (MI:177-201) plus H2: `A_F` is irreducible
and singular, hence `n = deg closure(A_F) >= 3` (a line is smooth; an
irreducible conic over `C` is smooth; the first irreducible singular plane
curves have degree 3). Lemma A (MI:120-143): `D~ cong A^1`, one place at
infinity of `A_F`.

The coordinator's ~11:05Z computation is accepted as stated: Suzuki's formula
`sum_c (chi(F_c) - chi_gen) = 1 - chi_gen = n W - N + 1` with Hà–Lê
nonnegativity has every unit of the budget accounted for by the `(K)` ledger.
No step below uses that budget as an inequality.

## 3. Q1: THEOREM MF-DEFECT

> **THEOREM MF-DEFECT.** Let `F` be a noninvertible plane Keller map of
> geometric degree `N` under H2, and let `L` be a generic line in the target.
> Then `2 g_L + theta_inf >= 2`. Equivalently
> `n (W - S) >= N`, and the S-known floor `n >= ceil((N-1)/(W-S))` is not
> attained.

*Proof.* If `g_L >= 1` then `2 g_L + theta_inf >= 3`. Suppose toward a
contradiction that `g_L = 0` and `theta_inf = 1`. Write `h := u o F` for
generic `u`.

**Step 1 (polar number is constant).** Lemma A puts a single place of `A_F`
at infinity, so `closure(A_F)` meets the target line at infinity in one
point. Generic `u` makes that point distinct from the point at infinity
`infty_L` of `L = {u = c}`. Consequently, for every compact set of finite
values `c` there is `R` such that

```text
{ u = c, |v| > R }  subset  C^2 \ A_F.
```

`F : C^2 \ F^{-1}(A_F) -> C^2 \ A_F` is finite étale of degree `N`, so
`F^{-1}(Delta x {|v|>R}) -> Delta x {|v|>R}` is an unbranched covering of a
product, for a small disk `Delta` of `c`-values. Restricting to a fibre of
`u`, the polar part `{p in C_L : |v o F(p)| > R}` is a covering of
`{|v|>R} ~= ` a punctured neighbourhood of `infty_L`. The number of connected
components of that covering is the number of cycles of the monodromy of `F`
around `infty_L`, which is `theta_inf`, and the product structure makes it
independent of `c`. (This is the equianalyticity of polar germs for a Keller
component, in the form needed here; compare Chau, arXiv:0804.3172, Thm 4,
whose degree-ratio input is replaced by genericity of `u` plus Lemma A.)

**Step 2 (every component carries a polar branch).** Every fibre of `h` is
smooth and reduced (`h` is a submersion). An irreducible component `C` of
any fibre is therefore a smooth affine curve. If `C` has no polar branch,
then `v o F` is a polynomial function on `C` which remains bounded (the
image of `F|C` stays in a bounded subset of the line `{u=c}`). A bounded
polynomial function on an affine curve is constant, so `F` is constant on
`C`, so `dF` kills `TC`, contradicting `Jac F in C^*`. Thus every irreducible
component of every fibre has at least one polar branch, and a fibre with `k`
components has at least `k` polar branches. Combined with Step 1:
`theta_inf = 1` forces `k=1` on every fibre. Every affine fibre of `h` is
irreducible.

**Step 3 (one horizontal, of degree 1).** Now `h` is a primitive rational
polynomial (generic fibre irreducible of genus 0) with **all** affine fibres
irreducible. Let `Y = C^2 cup E` be a smooth compactification of `C^2` on
which `h` extends to a morphism `Y -> P^1`, with `E` a normal-crossings tree
of smooth rational curves. A component of `E` is **horizontal** if `h` is
nonconstant on it. Write `delta` for the number of horizontal components and
`r_c` for the number of irreducible components of the affine fibre
`h^{-1}(c)`. Miyanishi–Sugie (Osaka J. Math. 17 (1980), Lemma 1.6, attributed
there to Saito) and equivalently Kaliman (Pacific J. Math. 154 (1992),
Corollary 2), as recorded by Neumann–Norbury (Bull. Austral. Math. Soc. 58
(1998), p. 501), give

```text
delta - 1  =  sum_{c in C} (r_c - 1).
```

Step 2 makes every summand zero, so `delta = 1`: exactly one horizontal
curve. Neumann–Norbury, Proposition 3: if `d` is the gcd of the degrees of
`h` on the horizontal curves and `D` is the sum of those degrees, the
generic fibre of `h` has `d` components, each with `D/d` places at infinity.
The generic fibre is irreducible, so `d=1`. With a unique horizontal, that
horizontal has degree 1, and the generic fibre has exactly one place at
infinity: `theta_L = 1`.

**Step 4 (place count).** MF-EXACT supplies `theta_L = n S + theta_inf`. The
standing hypotheses give `S >= 1` and `n >= 3`, and we are in the case
`theta_inf = 1`, so `theta_L >= 4`. This contradicts Step 3.

Hence `(g_L, theta_inf) != (0,1)`, so `2 g_L + theta_inf >= 2`, and
MF-EXACT yields `n(W-S) >= N`. ∎

**Remarks.** (i) The Euler sum of fibre defects is not used as an inequality;
the contradiction is that one polar branch cannot coexist with `nS >= 3`
further places over `L cap A_F`. (ii) AMS kills a fibre `cong A^1`, i.e.
`(g_L, theta_L)=(0,1)`, and is used only inside banked SMOOTH-KILL. The
floor case is `(g_L, theta_inf)=(0,1)`, a rational curve with
`theta_L >= 4` punctures. Fibre `cong C^*` is `theta_L=2`, hence `n=1`,
likewise forbidden. (iii) Razar (Israel J. Math. 32 (1979), 97–106) is a
second death: after a linear change of target, Step 2 puts `h` in Razar's
hypotheses (rational, all fibres irreducible, Jacobian partner) and
noninvertibility dies without Step 4. The place-count is preferred because
it contradicts MF-EXACT internally. (iv) Positive control, `N=4`, `W=2`:
`n = 2 + 2 g_L + theta_inf`, so MF-DEFECT gives `n >= 4`, recovering the
Chau-lane / LOC-MULT value without N4-PIN. If `n=4` is attained then
`(g_L, theta_inf)=(0,2)` (MR:179-182). (v) Non-Keller control: `F_m=(x,y^m)`
attains `(0,1)` (MFS:164-168). It is not étale, so Steps 1–2 fail, and `x`
is a coordinate.

**Integer floor, honestly.** The identity upgrade is `n(W-S) >= N`. The
integer S-known floor `ceil(N/(W-S))` exceeds `ceil((N-1)/(W-S))` iff
`W-S` divides `N-1`. At `W=2`, 7.B' forces `S=1`, so `n_min >= N` for the
whole column and the crossing price becomes `C(N) <= N-1`, independently
of `beta` — the n-floor prize the producer attached to MULT-VS-BETA, obtained
from Q1 without Q2. The W-only `MFb` upgrades to `ceil(N/(W-1))` iff `W-1`
divides `N-1` (every `W=2` cell). Tabulated `Phi` (min over configs of a
max of floors) rises only where the meridian was binding and `W-S` divides
`N-1`; cells where LOC-MULT already gave `Phi = MFb+1` need not rise. "YES
adds +1 to Phi at every cell" is an identity-level sentence, not a statement
about the integer table. No cell is claimed empty.

## 4. Q2: THEOREM MULT-VS-BETA, NO

> **THEOREM MULT-VS-BETA.** In case (B3) at `W=2`, the constraints `(L)`,
> `(K)`, `(C1)`-`(C3)` and Lemma 4.3 do **not** force `beta=1` for `N >= 5`.
> Every integer `beta in {1,...,N-3}` is counting-admissible. The unique
> `N` at which those constraints force `beta=1` is `N=4` (N4-PIN).

*Setup, all banked.* `W=2` and 7.B' force a single dicritical `(s, mu)=(1,2)`,
so `S=1`, `R=0`, `a=N-2`, `D_gap=N-4`, and `(K)` is `sum K_p = N-3`.
Lemma 4.3 (MI:285-289), applicable because `s_1=1`: every point of `A_F`
carrying a singular branch has `K_p >= 1`. Lemma 4.2 (MI:279-283) with
`R=0`: every point with `K_p > 0` carries a singular branch. Therefore

```text
{ p : K_p > 0 }  =  { p : some branch of A_F at p is singular },
```

so `#{K_p > 0} = beta`, and `(C3)` is an equality. Combined with `(K)` and
`K_p >= 1` on those points: `beta <= N-3`, which is MI Proposition 6.2.
At a cusp, `(L)` is `a - a_p = K_p` with `K_p <= a`. At a multibranch
point, `(C2)` is `K_p <= D_gap` and `(C1)` is `r_p W <= N`. Case (B3)
requires at least one cusp and at least one multibranch point.

*Why N=4 is forced, and N>=5 is not.* At `N=4`, `D_gap=0` and `charge=1`.
A multibranch point cannot carry `K>0`. Lemma 4.3 therefore puts the unique
unit of charge on a singular-branch point, which `(L)` plus `a_p >= 0`
forces to be unibranch: N4-PIN (MI:580-605). For `N >= 5` one has
`charge = N-3 >= 2` and `D_gap = N-4 >= 1`. Charge can be split over two
or more singular-branch points, each with `K_p >= 1`, and a multibranch
point is allowed to carry `1 <= K_p <= D_gap`. Nothing in `(C3)` or
Lemma 4.3 forbids this. (MI:648-651 already flagged that the N=4 sharpness
is a small-degree phenomenon and must not be extended by analogy; the
present enumeration is that warning, made exact.)

*Enumeration, N=5,6,7.* Types are listed up to permutation of points of the
same kind. Each line is a solution of `(L)+(K)+(C1)+(C2)+(C3)+Lemma 4.3`
in (B3); extra `K=0` double points of two smooth branches (`r=2`,
`a_p = N-2r`) may be added freely whenever `a_p >= 0`, and are required
for (B3) precisely when there is no charged multibranch point. No type is
a Keller realisation.

```text
N=4  (control: unique, N4-PIN)
  beta=1  1 cusp (r,K,a_p)=(1,1,1); K=0 nodes (2,0,0)

N=5  charge=2, D_gap=1, a=3     beta in {1,2}
  beta=1  1 cusp (1,2,1); K=0 nodes (2,0,1)
  beta=2  1 cusp (1,1,2) + 1 charged mb (2,1,0)
  beta=2  2 cusps (1,1,2),(1,1,2); K=0 nodes (2,0,1)

N=6  charge=3, D_gap=2, a=4     beta in {1,2,3}
  beta=1  1 cusp (1,3,1); K=0 nodes (2,0,2)
  beta=2  1 cusp (1,1,3) + 1 charged mb (2,2,0)
  beta=2  1 cusp (1,2,2) + 1 charged mb (2,1,1)
  beta=2  2 cusps K=(1,2); K=0 nodes (2,0,2)
  beta=3  1 cusp (1,1,3) + 2 charged mb (2,1,1),(2,1,1)
  beta=3  2 cusps (1,1,3),(1,1,3) + 1 charged mb (2,1,1)
  beta=3  3 cusps K=(1,1,1); K=0 nodes (2,0,2)

N=7  charge=4, D_gap=3, a=5     beta in {1,2,3,4}
  beta=1  1 cusp (1,4,1); K=0 nodes (2,0,3)
  beta=2  1 cusp + 1 charged mb, K-splits (1,3)/(2,2)/(3,1);
          or 2 cusps, splits (1,3)/(2,2)
  beta=3  1c+2mb, 2c+1mb, or 3 cusps (all K-splits of 4 into 3 parts >=1
          with mb parts <=3)
  beta=4  1c+3mb, 2c+2mb, 3c+1mb, or 4 cusps; all K=1
```

*General argument.* For `N >= 5` and `beta in {1,...,N-3}`, write
`N-3 = sum_{i=1}^{beta} K_i` with each `K_i >= 1`. Put `K_1` on a cusp
(`a_p = a - K_1 >= 1`). If `beta=1`, add `K=0` nodes (`r=2`, `2r=4<=N`,
`a_p=N-4>=1`). If `beta>=2`, each remaining part is `<= N-4 = D_gap`, so
it may sit on a further cusp or a charged mb. (B3) always has a
multibranch point (charged, or a `K=0` node). Counting-admissible is not
realised. After Q1 the n-floor of the W=2 column no longer depends on
`beta`.

## 5. Opens raised, with bounded quantities

```text
OPEN[MF-RATIONAL]  (new).  Can g_L = 0 occur for a noninvertible Keller map
   under H2 and generic L?  Equivalently: can a generic linear combination
   u o F be a rational polynomial?  BOUNDED QUANTITY: g_L in
   {0, 1, ..., p_a(D_F)}; if g_L=0 then Theorem MF-DEFECT forces
   2 <= theta_inf <= N and nS + theta_inf <= D_F.  A NO would upgrade
   MF-EXACT to n(W-S) >= N+1.  Status: OPEN.  This is Chau's 2010
   concluding question (arXiv:0804.3172, Sec 5) specialised to a generic
   component of a Jacobian pair; Razar / Neumann–Norbury kill only the
   all-fibres-irreducible subcase, which is already excluded by
   theta_inf >= 2.  Not needed by any consumer of Sec 3-4.
```

Carried unchanged: `OPEN[DELTA-AFF-VS-N]`, `OPEN[N-VS-MAPDEG]` (upper half),
`OPEN[MIN-EMBED-DEGREE]`. Not re-raised: OPEN[MF-DEFECT], OPEN[MULT-VS-BETA].

## 6. FALLACY-v2 audit

`n`, `n_min`, `D_F`, `mrk(G)`, `g_L`, `theta_inf`, `theta_L`, `delta`,
`beta`, `K_p` are kept apart; polar branches of `h` are not the `nS`
dicritical places, and the S-known floor is not `MFb`. No exit price; no
`charge_basis`. MF-DEFECT excludes `(0,1)` and does not attain `(0,2)` or
`n=N`. Phi remains a floor, min over configs. MULT-VS-BETA types are
counting-admissible, not Keller curves. The integer ceil rises only when
`W-S` divides `N-1`. The chart at `infty_L` is used only after Lemma A
puts `infty_L != closure(A_F) cap L_infty`. Enumerator: partitions of
`N-3` into `beta` parts `>=1`, ceilings `K<=a` (cusp) and `K<=D_gap` (mb),
`r W <= N`, `a_p >= 0`; positive control N4-PIN, negative control
`D_gap=0` rejects `beta>=2` at `N=4`. No `sat()`, no remainder degree.
Case-(A) instruments unused; N4-PIN not extended by analogy; the defect
budget is not recycled as a lower bound. Had the Miyanishi–Sugie formula
been unavailable, the output would have been typed OPEN.

## 7. Typed verdict block

```text
LANE              MF-DEFECT-MULT-VS-BETA
SCOPE             Keller, noninvertible, H2, case (B) of THEOREM PROFILE.
                  Case (A) EMPTY and not used; A2 untouched; no Z(G)=1;
                  SCOPE[B3-QH] unused.  Classical citations: Miyanishi–
                  Sugie 1980 Lemma 1.6 / Saito; Kaliman 1992 Cor. 2;
                  Neumann–Norbury 1998 Prop. 3 and the Euler formula;
                  Razar 1979 (unused, recorded as a second death);
                  AMS only through banked SMOOTH-KILL.

PROVED HERE       (PROVED-HERE, UNREVIEWED)
                  MF-DEFECT     2 g_L + theta_inf >= 2; n(W-S) >= N;
                                S-known floor never attained.
                  W2-COLUMN     n_min >= N at every W=2 cell, independent
                                of beta.  Crossing price C(N) <= N-1.
                  MULT-VS-BETA  beta=1 is not forced in (B3) at W=2 for
                                N>=5; every beta in {1,...,N-3} is
                                counting-admissible.  Forced only at N=4.

CONSUMED          MF-EXACT, LOC-MULT, MF-SHARP, SHARP-CHAU at MR-CONFIRMED
                  typing with repairs (S-known vs W-only; orbit hypothesis;
                  no Z(G)=1).  MI Lemma A, (L), (K), (C1)-(C3), Lemmas
                  4.1-4.3, 7.B', THEOREM PROFILE, N4-PIN, SMOOTH-KILL.
                  HF at banked typing, unused except as scope boundary.
                  Coordinator ~11:05Z defect-budget note: respected.

CONTROLS          N=4 W=2: MF-DEFECT recovers n>=4 without N4-PIN.
                  N=4 W=2 enumeration: unique beta=1 type, matches N4-PIN.
                  N=5,6,7: every beta in {1,...,N-3} realised by an
                  integer solution of the ledger (Sec 4).
                  Non-Keller F_m attains (0,1); Steps 1-2 fail, correctly.

NOT CLAIMED       any kill at any N; any cell EMPTY; any Keller realisation
                  of a beta>=2 type or of (g_L, theta_inf)=(0,2);
                  attainment of n=N; +1 to tabulated Phi at every cell;
                  that g_L cannot be 0 (OPEN[MF-RATIONAL]); anything about
                  case (A), A2, Z(G), or the reducible branch.

OPENS RAISED      OPEN[MF-RATIONAL]  can g_L=0?  Bounded: g_L <= p_a(D_F);
                                     if 0 then 2 <= theta_inf <= N.

SUCCESSOR         (1) OPEN[MF-RATIONAL] is the remaining +1 on the identity
                      (n(W-S) >= N+1 if g_L>=1 always).  Classical, not
                      a counting question; Chau 2010 Sec 5 is the same
                      question for a single (not necessarily generic)
                      component.
                  (2) The gate is unchanged: OPEN[DELTA-AFF-VS-N] /
                      OPEN[N-VS-MAPDEG] upper half.  W=2 now dies only
                      under n_min <= C(N) with C(N) <= N-1.

DEVIATIONS        Classical statements used as charged (load-bearing:
                  Miyanishi-Sugie 1980 Lemma 1.6).  Desk CAS: python3
                  integer partitions, under 1 s.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20457`.
- Body SHA-256:
  `e39f761a29d91d1b774f4020fa88f8cb26b78ed5d847895fb246d82651f3a6ec`.
- Frozen basis: `9644e4e4025cb7aa87f9c5bb60c53842e56b563e`.
