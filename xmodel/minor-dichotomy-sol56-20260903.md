# `OPEN[MINOR-DICHOTOMY]`: source reading and the live `u_s>1` clients

## 0. Verdict

The gate does **not** close.  For `(99,66)`, p.209 displays a radius-2
`pi`-root of `g` while discussing roots inside `D_2^*`; it does **not** say
that this is the general point of the combined-product minor disc.  Thus the
literal Proposition 6.3 comparison with `8/3` is **UNDETERMINED**.  Moh's
two-root cubic branch does witness `delta_2^*<=2`, so the bound fails in that
branch; the linear-power branch leaves the bound undetermined, although Moh
asserts a transformed row.  Neither branch receives a displayed
contradiction.  P.211 only asserts that omitted cases compute similarly.

For `(108,72)`, only `delta_2^*>=1` is known, so comparison with `7/2` is
**UNDETERMINED**.  Its `u_3=2` split needs the actual minor general point;
Moh's cubic/ninth-power casework cannot be copied to it.

The charged `C_FULL_TREE_POLYNOMIAL_ODE` rerun is
`1,420 rows / 686 groups`, with `310 rows / 177 groups` having `u_s>1`.
The universal source floor decides **0/177 = 0%** of those groups at skeleton
level.

## 1. Frozen basis, page images, and scope

`MECHANICAL-CHECK`: the receipt generated an `awk` manifest passed to
`sha256sum -c`; all nine frozen inputs returned `OK`.

Printed page `p` is PDF page `p-139` (one-based).  `pdftoppm -png -r 200`
produced:

| printed pages | PDF pages | images under `box/minordich-20260903/pages/` |
|---|---:|---|
| 196--199 | 57--60 | `moh-pp196-199-57.png` through `-60.png` |
| 207--209 | 68--70 | `moh-pp207-209-68.png` through `-70.png` |
| 210--211, continuation | 71--72 | `moh-p210-71.png`, `moh-p211-72.png` |
| 202, source table | 63 | `moh-p202-63.png` |
| supporting 146--147, 150--152, 161, 168--171, 179--180, 190--195 | 7--8, 11--13, 22, 29--32, 40--41, 51--56 | correspondingly named `moh-p*.png` files |

P.209 has no formal citation: its “above mentioned method” points backward.
Pp.210--211 are the branch's continuation and blanket conclusion.

## 2. What the source actually licenses

### 2.1 Major radius is not minor radius

`SOURCE-READ`, Def.5.1(3), p.179: the discs in a **major tower** `D_s superset
... superset D_r` have logarithmic radii `delta_i` given by the displayed
rational formula.  These are the values computed by `moh_skeleton_full.py`.
They are not `delta^*_{s-1}`.

`SOURCE-READ`, Prop.6.1, pp.190--193: `D^*_{r-1}` uses the selected roots of
`g product_{i=1}^r T_i^psi`, but its distribution-detector conclusion stops
at `(g,T_1^psi,...,T_{r-1}^psi)`.  Its radius is the minimum actual contact.
Moh then warns (p.193):

> “The above proposition does not specify the logarithmic radius
> `delta^*_{r-1}` of `D^*_{r-1}`. We only get an estimate
> `delta^*_{r-1} >= 1`.”

Prop.4.4, pp.168--169, is conditional: after seven hypotheses its leading
polynomials are powers of a common linear polynomial.  It proves the floor
inside Prop.6.1, not `delta^*` from `(M,V,d)`.

### 2.2 Proposition 6.3 and the `u_s=1` upgrade

`SOURCE-READ`, p.197, Proposition 6.3 assumes, among its other hypotheses,

> “`delta_s=-1` and the logarithmic radius `delta^*_{s-1}` of the minor
> disc `D^*_{s-1} >= v_s/u_s`.”

With `gamma=theta^(1/u_s)`, it gives monic-in-`pi` polynomials of degrees

```text
u_s n/d_s,  u_s(-mu_1)/d_s, ..., u_s(-mu_{s-1})/d_s,
```

and Jacobian `-(u_s/b) gamma^(v_s-u_s-1)`.  P.198's last proof display puts
the exponent in a denominator; the proposition and Appendix-II monomials use
the positive exponent (`ERRATUM[PROP63-JAC-SIGN]`).

`SOURCE-READ`, p.198, Proposition 6.4 adds `u_s=1` and concludes

> “the logarithmic radius `delta^*_{s-1}` of the minor disc
> `D^*_{s-1} >= v_s/u_s = v_s`.”

Its proof assumes the contrary, uses Prop.6.1 and gcd 1 to force a common
linear polynomial, then says this “contradicts the very definition of
`delta^*_{s-1}`” (p.199).  This step is expressly restricted to `u_s=1`.

This is also how Appendix II announces its scope on p.207:

> “We shall apply Proposition 6.4 to the first three cases. Note that in
> these cases we always have `u_3=d_3-v_3=1`.”

Thus the fourth case is deliberately outside that automatic descent.

## 3. Moh's `(99,66)` case, exactly

### 3.1 Tower and radius test

`MEASURED / EXACT-ARITHMETIC` from the p.202 row and Def.5.1:

```text
n=99, m=66, s=3
M_1..M_3 = (-66,77,97)
d_1..d_4 = (99,33,11,1)
V_2,V_3 = (8,8)
v_3=8, u_3=d_3-v_3=3, v_3/u_3=8/3
major (delta_1,delta_2,delta_3) = (4/9,1/3,-1).
```

The positive `delta_2=1/3` is the major-disc radius.  It is not the tested
minor radius.

`SOURCE-READ, RADIUS-2 G-PROBE`: p.209 introduces the distribution of roots
of `g` in `D_2^*` and immediately (“Namely”) displays “an unique `pi`-root
`sigma` of `g(y)`”:

```text
sigma = a_{-1} t^{-1} + a_0 + a_1 t + pi t^2,
g(sigma) = g_sigma(pi) t^{-18} + ... .
```

P.147 makes this the general point of **a** radius-2 disc.  It does not identify
that disc with the minimal combined-product disc defining `D_2^*` in
Prop.6.1.  The distinction matters because `D_2^*` also contains the selected
roots of the `T_i^psi`.  The probe order checks:

```text
ord g(sigma) = (n/d_3)(u_3*2-v_3) = 9(6-8) = -18.
```

Consequently the displayed exponent alone proves neither
`delta_2^*>=8/3` nor its negation: **Prop.6.3 is UNDETERMINED overall**.  In
the two-root branch, however, Prop.1.2 turns the two roots of `g_sigma` into
two `g`-roots in `D_2^*` with contact exactly 2.  Since `delta_2^*` is the
minimum combined contact, `delta_2^*<=2<8/3`, and Prop.6.3 fails there.  In
the linear branch `g` does not split at the probe, but the text gives no
common-probe profile for any `T_i^psi`; one can set an earlier combined
boundary, so the comparison stays undetermined.
Conditionally, if one separately identified the probe disc with `D_2^*`,
then `delta_2^*=2` and Prop.6.3 would fail in both branches; Moh does not make
that identification.

### 3.2 The two alternatives and their actual dispositions

P.209 says:

> “The polynomial `g_sigma(pi)` is either a power of a linear polynomial or
> the 9-th power of a cubic polynomial with precisely two roots.”

`EXACT-ARITHMETIC`: p.150 defines `q_1=M_1`, `q_2=M_2-M_1`,
`lambda_2=q_1d_1+q_2d_2`, and `mu_2=lambda_2/d_2`.  Here

```text
mu_2=[(-66)99+(77+66)33]/33=-55.
```

P.152 gives `deg_y T_2^psi=55`.  If the radius bound were independently
certified, Prop.6.3 would give the tower `(27,18,15)` and Jacobian
`-(3/b)gamma^4`.

`CONDITIONAL-CHECK`: `(99,66,55)=11(9,6,5)`, so a certified common detector
would have profiles `(c_gH^9,c_1H^6,c_2H^5)` by Def.3.1; the cubic branch's
`deg g_sigma=27` would give `deg H=3`.  P.209 calls `sigma` only a `pi`-root
of `g`, however, and gives no common `T_1,T_2` certificate.  Prop.6.1 therefore
does not derive the `SOURCE-ASSERTED` cubic.

The remaining formal cubic partition `1+1+1` is not excluded on the page.
Propositions 4.5--4.6 offer possible at-most-two-root mechanisms, but Moh
neither cites them nor checks their local hypotheses.  Thus “precisely two
roots” is `SOURCE-ASSERTED`, not an audited arithmetic/coefficient/count
exclusion.  Once accepted, the multiplicities are `2+1`.

| branch | source operation | radius gate | auditable outcome |
|---|---|---|---|
| A: `LINEAR-POWER` | p.209 asserts transformed `(n,m,M_2,V_2,delta_2,delta_1,Jac)=(27,18,21,8,-1,0,X^4)` and reduces to 10 coefficients | combined `delta_2^*` undetermined | `OPEN[99-LINEAR-10]`; no displayed contradiction |
| B: `TWO-ROOT-CUBIC` | `g_sigma=H^9`, `deg H=3`, two roots; Moh gives `Omega` and reduces to 11 variables | `delta_2^*<=2`, so Prop.6.3 fails | `OPEN[99-CUBIC-11]`; no displayed contradiction |

In branch B, raising the `2+1` multiplicities to the ninth power gives
`18+9` roots of `g` (`ARITHMETIC-INFERENCE`).  Moh's transform is

```text
x -> x^{-1},  y -> a_0+a_1 x+a_2 x^2+y x^3,
Omega(f)=x^6 y^18+...,        Omega(g)=x^9 y^27+...,
Omega(T_2^psi)=x^5 y^15+..., Omega(T_3^psi)=x^15 y^40+...,
J(Omega(f),Omega(g))=x.
```

Neither alternative is excluded there by arithmetic, by a coefficient
equation, or by a minor-disc count.  The explicit `a_9=0` / `a_9 != 0`
coefficient contradiction on pp.210--211 treats
`(n,m,M_2,V_2)=(15,10,11,3)`, the transformed `(75,50)` case.  It is not a
calculation for either `(99,66)` branch.  P.211 finally says:

> “All other cases can be computed directly as above. There is no
> counter-example of polynomials of degrees less than or equal to 100.”

That assertion of omitted computation is not an exhibited kill and cannot
promote A or B to `KILLED` under `FALLACY-v2`.

The exact shapes, transformed `M_2=21`, and `Omega` are case-specific; Moh
states no theorem making them a template for arbitrary `u_s>1`.

## 4. The live `D=108` row

### 4.1 What is and is not determined

`MEASURED / EXACT-ARITHMETIC`:

```text
n=108, m=72, s=3
M_1..M_3 = (-72,81,106)
d_1..d_4 = (108,36,9,1)
V_2,V_3 = (7,7)
v_3=7, u_3=d_3-v_3=2, v_3/u_3=7/2
major (delta_1,delta_2,delta_3) = (3/8,1/4,-1).
```

Def.5.1 gives the unstarred radii; Prop.6.1 gives only `delta_2^*>=1`.
No source gives this row actual contacts, so the `7/2` bound is
**UNDETERMINED**; substituting major `1/4` would be invalid.

P.150 gives `mu_1=-72` and
`mu_2=[(-72)108+(81+72)36]/36=-63`.  If a certificate gives
`delta_2^*>=7/2`, Prop.6.3 yields the complete `pi`-degree tower
`(g,T_1^psi,T_2^psi)=(24,16,14)` and Jacobian `-(2/b)gamma^4`: respectively
`2(108,72,63)/9` and `v_3-u_3-1=4`, with `b!=0`.  This
`DESCEND-WITH-MODIFIED-HYPOTHESIS` is not a kill; no new `M_2'` or radius is
inferred.

### 4.2 Faithful conditional branch enumeration

Let `rho=delta_2^*` be the **actual** minor radius.  If `rho<7/2`, the general
point `sigma_rho` has

```text
ord g(sigma_rho) = (108/9)(2 rho-7) = 12(2 rho-7) < 0.
```

Prop.6.1 therefore makes it a distribution detector for
`(g,T_1^psi,T_2^psi)`.  The global degrees are
`(108,72,63)=9(12,8,7)`, so Def.3.1 gives profiles with common-polynomial
exponents `(12,8,7)`.  The full minor `g` multiplicity is
`u_3n/d_3=24` by Prop.6.2, pp.194--195; hence `12 deg H=24`, `deg H=2`, and the local degrees are
`(24,16,14)`.  A quadratic has two exhaustive factor partitions:

| conditional subcritical branch | detector profile | outcome and missing datum |
|---|---|---|
| A108: one distinct root | `H=c(pi-a)^2`; exponents `(24,16,14)` | `OPEN[108-A]`: `T_3^psi` must carry the combined split; need its profile, the actual jet, and a derived coefficient system |
| B108: two distinct roots | `H=c(pi-a)(pi-b)`; packets `g:12+12`, `T_1:8+8`, `T_2:7+7` | `OPEN[108-B]`: need both subdisc jets, the `T_3^psi` profile, and a case-specific coefficient system; no source step kills it |

This is abstract `ONE-G-ROOT / MULTIPLE-G-ROOTS` branching, not Moh's cubic.
For general `u_s>1`, B must retain the full degree-`u_s` factor partition.

They require a measured `rho<7/2`; the skeleton licenses no fixed-radius
probe or transform.

## 5. Typed `u_s>1` procedure

Input is a screened skeleton `S=(n,m,M_i,d_i,V_i)`, optional actual-disc data
`R` (minor radius/general-point jet and all leading polynomials), and an
optional non-boundary probe `P` such as Moh's p.209 `g`-probe.

```text
MINOR(S,R,P):
  1. Check every source hypothesis: monic/total-degree condition, delta_s=-1,
     M_s=n-2, the actual minor cluster, and u_s=d_s-v_s>0.
  2. Compute v_s=V_s, u_s=d_s-v_s, q=v_s/u_s.  Compute Def.5.1 delta_i,
     but label them MAJOR; never substitute delta_{s-1} for delta*_{s-1}.
  3. If u_s=1, Prop.6.4 certifies delta*>=q.  Output
     DESCEND-WITH-MODIFIED-HYPOTHESIS via Prop.6.3.
  4. If u_s>1 and R has no actual delta*, use only Prop.6.1's delta*>=1.
     If 1>=q, descend; otherwise output OPEN[MINOR-RADIUS].
  5. If R proves delta*>=q, output DESCEND-WITH-MODIFIED-HYPOTHESIS with
     Prop.6.3's pi-degree tower and monomial Jacobian.
  6. If R proves delta*<q, form the general point at the actual delta* and
     verify ord g<0 before using Prop.6.1.  Factor every leading polynomial.
       A. One distinct g-root: output BRANCH A with the full T-root profile.
       B. More than one distinct g-root: output BRANCH B with the full
          multiplicity partition.
     Apply only a case-proved coordinate transform and coefficient system.
     If either is absent, return OPEN; a lower coefficient count is not a kill.
  7. If only P is known, never relabel its radius as delta*.  Multiple roots
     at radius r give delta*<=r only after checking that both belong to the
     selected minor cluster; a one-root g profile gives no combined bound.
     Output the supported branch plus OPEN.
```

For `(99,66)`, p.209 supplies `P`, not `R`, and asserts its row-specific A/B
profiles.  Step 7 proves failure only in B.  For `(108,72)`, step 4 returns
`OPEN[MINOR-RADIUS-108]`; §4.2 is the continuation once `R` exists.

## 6. Census application

`MEASURED`: `census_usgt1.py` imports the two frozen charged programs,
rechecks all receipt hashes, and applies
`full_tree_polynomial_ode_ok`.  Group key is exactly
`(n,m,(M_2,...,M_s),V_s)`; intermediate `V_i` values are row paths.  It
reproduces:

```text
48<=D<=200 POLY+ODE       1420 rows / 686 groups
u_s>1                       310 rows / 177 groups
ODE u_s>1                   310 rows / 177 groups
ODE and POLY+ODE u_s>1 row and group key sets: identical
```

At the top, condition (7) and `M_s=n-2` imply
`v_s>d_s/(n-M_s)=d_s/2`.  Therefore
`u_s=d_s-v_s<d_s/2` and `v_s/u_s>1`.  Prop.6.1's floor 1 consequently proves
the Prop.6.3 bound for none of these skeletons.  The full measured threshold
range is `4/3` through `9/2`; the exact outcome of the skeleton procedure is
**0/177 (0%)**, not an attainment claim about actual Jacobian pairs.

The requested `48<=D<=120` list is:

| `(D,m)` | `M_1,...,M_s` | `d_1,...,d_{s+1}` | `V_2,...,V_s` | `u_s`; bound | Def.5.1 major `delta_1,...,delta_s` | result |
|---|---|---|---|---|---|---|
| `(99,66)` | `(-66,77,97)` | `(99,33,11,1)` | `(8,8)` | `3`; `8/3` | `(4/9,1/3,-1)` | skeleton `OPEN`; p.209 probe: A undetermined, B fails bound |
| `(108,72)` | `(-72,81,106)` | `(108,36,9,1)` | `(7,7)` | `2`; `7/2` | `(3/8,1/4,-1)` | `OPEN[MINOR-RADIUS-108]` |
| `(120,80)` | `(-80,-60,-10,25,118)` | `(120,40,20,10,5,1)` | `(1,1,6,3)` | `2`; `3/2` | `(11/16,19/28,51/77,37/56,-1)` | `OPEN[MINOR-RADIUS]` |
| `(120,100)` | `(-100,30,115,118)` | `(120,20,10,5,1)` | `(6,3,3)` | `2`; `3/2` | `(54/65,43/52,1/2,-1)` | `OPEN[MINOR-RADIUS]` |

There are four rows and four groups in this stratum through 120, each with one
selected `V` path; the skeleton decision fraction is **0/4**.

## 7. Bounded OPENs and cheapest tests

| typed OPEN | bounded quantity | cheapest fail-closed test |
|---|---|---|
| `OPEN[MINOR-RADIUS-99]` | one combined `delta_2^*` and its first-separation witness (needed in the linear branch) | compute first contacts among selected roots of `g` and `T_1^psi,T_2^psi,T_3^psi`; compare with `8/3`; do not relabel the p.209 probe |
| `OPEN[99-DICHOTOMY-EXHAUSTIVE]` | one missing exclusion of a three-distinct-root cubic | either check every Prop.4.5/4.6 hypothesis after an explicit local re-gauging, or retain a third `1+1+1` branch |
| `OPEN[99-LINEAR-10]` | Moh's stated 10-variable linear-power coefficient system, presently not displayed | reconstruct the p.208--209 approximate-root ansatz for `(27,18,21,8)` and solve it with explicit ring map, vanished-leader branches, and positive/negative controls |
| `OPEN[99-CUBIC-11]` | Moh's stated 11-variable `Omega(g)=0` system and the `18+9` minor packets | derive the omitted equations after the printed `Omega`, then solve both root packets; the p.211 `(15,10)` calculation is only a control |
| `OPEN[MINOR-RADIUS-108]` | one actual rational `delta_2^*`, its common Puiseux jet, and the leading `g,T_i` polynomials | compute first pairwise contacts in the actual minor cluster; compare once with `7/2`; do not compute a major radius again |
| `OPEN[108-A]` | the one-root detector profile and boundary `T_3^psi` profile | derive the case-specific transform and coefficient equations; no generic Prop.6.4 step |
| `OPEN[108-B]` | the two-root quadratic profile (`12+12`) plus its two subdisc jets | normalize both roots, construct the transform at the measured radius, and solve the resulting coefficient system |
| `OPEN[177-MINOR-DATA]` | 177 group questions represented by 310 row/path radius cases; 4/4 in the `D<=120` pilot | batch first-contact tests, sharing results only when proved; a skeleton-only rerun cannot improve 0/177 |

No DP survivor is asserted to be a `FULL_ACTUAL_EXIT`.

## 8. Reproduction, typing, and `FALLACY-v2`

`box/minordich-20260903/` contains the two checked drivers, their reproduction
commands in `README.md`, and 28 named 200-dpi page images.  Both drivers exited
zero; the census took 18.12 seconds and 150396 KiB RSS.  No ledger,
`jc2-lean`, or `ideation-*` file was edited.

```text
SOURCE-READ       Moh pp.147,150-152,161,168-171,179,190-199,202,207-211.
SOURCE-ASSERTED   p.209's two alternatives, including omission of cubic 1+1+1.
CONDITIONAL-CHECK p.209 common-profile arithmetic; D=108 subcritical branches.
EXACT-ARITHMETIC  gcd towers, major radii, thresholds, orders, and degrees.
MEASURED          charged POLY+ODE counts, group lists, threshold distribution.
OPEN              all eight bounded residues in §7; no branch is promoted to a kill.
```

`FALLACY-v2`: combined disc, `g` profile, and major radii remain distinct;
there is no floor-as-attainment or exit-price assertion, hence no
`charge_basis` line.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17579`.
- Body SHA-256:
  `17aac9cbc93a3c888d2e93792e63284e4bf28b52b450191e952968346711e8c2`.
- Frozen basis: `bf8fcd78da081f8147c20ee797360cc8133555ac`.
