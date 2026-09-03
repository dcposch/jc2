# `(99,66)` fresh-eyes source review: what Moh 1983 and Xu 2022 actually print

Lane `g9966-source-review-opus5-20260903`.  Basis `afb7e21b`.

## Verdict first

`MECHANICAL-CHECK`: PASS.  The manifest was generated with `awk` from the
`charged_input_<i>_sha256` / `charged_input_<i>_basename` lines of
`xmodel/g9966-source-review-opus5-20260903.run.v2` and checked with
`sha256sum -c`; all ten frozen inputs returned `OK`.  No digest was retyped.
Manifest: `box/g9966rev-20260903/inputs.sha256`.

**No source route excludes either surviving branch.**  The review found no
printed statement in Moh pp.190--199 / 207--211 or Xu pp.4--13 that the lanes
missed and that constrains the `(99,66)` principal minor roots further.  It did
find three things the lanes did not have, all `DERIVED-SOURCE` and mechanically
checked:

* `DERIVED-SOURCE[PROP-6.1-ORDER-IDENTITY]`.  Moh's Prop. 6.1 proof (p.191) is
  an **exact order identity**, not only the `delta* >= 1` estimate.  Read with
  the *minor* multiplicity `V_r = u_s = 3` (p.190's dichotomy, not the p.202
  major `V_3 = 8`) it gives `ord g(sigma) = (n/d_s)(u_s*delta - v_s) =
  9(3*delta - 8)`, reproducing Moh's printed `t^-18` at `delta = 2` and *all
  five* of Xu §8's orders at both `delta = 2` and `5/2` from the skeleton
  alone.  Its corollary `ord g(sigma) < 0 <=> delta < v_s/u_s = 8/3` is the
  ceiling the lanes were missing; `Im_min = 8/3` is the same number.
* `DERIVED-SOURCE[SPLIT-ORDER-CLASSIFICATION]`.  That ceiling, Xu Prop. 7.3
  (`delta > 1`), Xu's denominator bound (`den(delta) <= u_s = 3`) and the
  resonance/degree budget of the face ODE give an **exhaustive** list: the only
  admissible split orders are `delta = 2` (partition `[2,1]` only, multiplicity
  vector `(25,14)` forced) and `delta = 5/2`.  Xu states §8(i) without this
  enumeration; this is an independent re-derivation.
* `DERIVED-SOURCE[DELTA-52-GALOIS-RIGIDITY]`.  At `delta = 5/2` the `mu_2`
  action `pi -> -pi` forces `[1,1,1]` with `p(pi) = pi(pi^2 - c)` and excludes
  the ODE-admissible `[2,1]` vectors.  After the `pi`-scaling gauge the
  `delta = 5/2` face is a **1-parameter** family; branch B's is a **point**.

The two questions the task asked to settle came out negative.
`SATURATED-EMPTY[SEPARATING-POWER]` for Theorem 3.4 + Theorem 4.7: their joint
bookkeeping is a *tree-blind identity* at `(99,66)` -- for every admissible
tree, `sum_{P_m}|D_sigma^{f_xi}|(delta_sigma-1)` minus the Theorem-3.4
principal term equals `30` exactly (§5 proves it in closed form), so equality
in 4.7(i) cannot separate the branches.  Corollary 5.3 (`IM >= Im`) passes
both: `IM = 16`, `Im = 6` (branch B), `Im = 7` (`delta = 5/2`) -- the charged
non-kill, now with exact `Im` rather than the floor `8/3`.

Status after this review, typed:

```text
OPEN[9966-DELTA-2-BRANCH-B]      face rigid; global lift unproved
OPEN[9966-DELTA-52-BRANCH]       face 1-parameter; global lift unproved
CLOSED[9966-DELTA-2-THREE-ROOT]  Moh p.209 printed + Xu Cor 7.5 + degree budget
CLOSED[9966-OTHER-SPLIT-ORDERS]  enumeration below (all delta != 2, 5/2)
```

`(99,66)` remains `OPEN`.  Nothing here is a Keller witness.

## 1. Pages opened

`SOURCE-READ`.  Printed Moh page `p` is PDF page `p-139`; Xu printed page `p`
is PDF page `p`.  Images at 200 dpi in `box/g9966rev-20260903/pages/`:

| content | printed | image |
|---|---|---|
| Moh minor-disc dichotomy, Prop. 6.1 statement | 190 | `moh_p190_pdf51.png` |
| Moh Prop. 6.1 proof, order identity | 191--193 | `moh_p191_pdf52.png` -- `moh_p193_pdf54.png` |
| Moh Lemma 6.1 and `delta_{s-1}` formula; **Prop. 6.2**; Props. 6.3--6.4 | 194--199 | `moh_p194_pdf55.png` -- `moh_p199_pdf60.png` |
| Moh Appendix II table (`(16,12)`), `Omega`, 11-variable claim, `(15,10)` | 207--211 | `moh_p207_pdf68.png` -- `moh_p211_pdf72.png` |
| Xu Lemma 4.1--Thm 4.7, Thm 5.1, Cor 5.3, §6 | 4--9 | `xu_p4_pdf4.png` -- `xu_p9_pdf9.png` |
| Xu Prop. 7.3, Cor 7.5, §8 `(99,66)` | 10--13 | `xu_p10_pdf10.png` -- `xu_p13_pdf13.png` |

### 1.1 What Proposition 6.2 says (the task's premise, corrected)

The task supposed the lanes never cite Prop. 6.2.  They do:
`moh9966-branchB-sol56-20260903.md` uses its output as the `27/72, 18/48,
15/40` minor/major table.  The printed statement (p.195) is stronger than a
count.  With `z = y - bx - e` (p.194 eq. (10)) and `g, T_i^psi` rewritten as
`gbar, Tbar_i^psi` in `(y,z)`:

```text
(1) deg_y gbar        = v_s * n/d_s          (2) deg_z gbar        = u_s * n/d_s
(3) deg_y Tbar_i^psi  = v_s * (-mu_i)/d_s    (4) deg_z Tbar_i^psi  = u_s * (-mu_i)/d_s
                                                 for i = 1,...,s-1.
```

At `(99,66)`: `(deg_y, deg_z) = (72,27)` for `g`, `(48,18)` for `f = T_1^psi`,
`(40,15)` for `T_2^psi`.  Since `72 + 27 = 99` and `48 + 18 = 66` are the
*total* degrees and `(x,y) -> (y,z)` is linear, the top forms are forced to be
the single monomials `y^72 z^27` and `y^48 z^18`.  Proposition 6.2 is therefore
a **bidegree box plus a corner**, and it says nothing about `T_s^psi = T_3^psi`
(its range is `i <= s-1`).  It is the right cut for the global object (§6), not
a new constraint on the minor roots.

### 1.2 The three source facts that bracket the problem

`SOURCE-READ`, Moh p.190: the disc `D*_{r-1}` is **minor** exactly when
`V_r <= d_r/(n - M_r)`.  At `(99,66)` that threshold is `11/2`, so the `v_3 = 8`
factor is major and the `u_3 = 3` factor is minor: every Prop. 6.1 formula
applied to the principal packet must be read with `V_r = 3`, not the p.202
major `V_3 = 8`.

`SOURCE-READ`, Moh p.193, immediately after the Q.E.D.: "*The above proposition
does not specify the logarithmic radius `delta*_{r-1}` of `D*_{r-1}`.  We only
get an estimate `delta*_{r-1} >= 1`.*"  That sentence is the whole
`OPEN[PRINCIPAL-MINOR-RADIUS]`.  Prop. 6.3 **assumes** `delta* >= v_s/u_s`;
Prop. 6.4 proves that premise **only under `u_s = 1`**.  Moh p.207 confirms
`u_3 = d_3 - v_3 = 1` for `(64,48)`, `(84,56)`, `(75,50)` and that 6.3/6.4 are
applied to exactly those three.

`SOURCE-READ`, Xu p.12--13 §8: Xu lists the three claims Moh's p.209 sentence
needs, proves (ii) and (iii), and leaves one case of (i) open, naming
`delta = 5/2`.  His tools are named on p.13: "*the denominator of order
`delta <= u_s = 3`*" and equation (7.1).  Cor. 7.5 (p.11): if `u_s > 1` and
`delta_sigma < (v_s+1)/(u_s+1)` then `sigma` cannot split to `u_s` different
roots.  At `(99,66)` that bound is `9/4`, so it kills the three-root split at
`2` and does not reach `5/2`, whose denominator `2 <= 3` also passes.  The
task's read of both is correct, and **no printed strengthening of either exists
in the source.**

## 2. The order identity and the ceiling `delta < 8/3`

Moh p.191 derives, for the unique `pi`-root `sigma*` of `g prod T_i^psi` in the
minor disc,

```text
ord g(sigma*) = n*delta_s + V_r (n/d_r)(delta*_{r-1} - delta_r).
```

With `r = s = 3`, `delta_3 = -1`, `V_3 = u_3 = 3`, `n/d_3 = 9`:

```text
ord g(sigma) = -99 + 27(delta + 1) = 9(3*delta - 8) = (n/d_s)(u_s*delta - v_s).
```

The driver checks this against the direct root-contact count
(`72` major roots at contact `-1`, `27` principal at contact `delta`) for all
`delta in {1, 7/6, ..., 4}`: exact agreement.  Specialisations:

```text
delta = 2  : ord (f,g,T2,(T3)_f,T3) = (-12, -18, -10, -44, -25)   [Moh p.209: t^-18]
delta = 5/2: ord (f,g,T2,(T3)_f,T3) = (-3, -9/2, -5/2, -11, -5)
```

Both rows reproduce Xu §8's printed orders exactly, including the shifted
`T_3` order `13(-8+3delta) - 1 + delta`.  The ceiling is immediate:

```text
ord g(sigma) < 0   <=>   delta < v_s/u_s = 8/3.
```

`ord g(sigma) < 0` is what makes `sigma` a distribution detector (Prop. 6.1(2)),
i.e. what forces the leading coefficients to be powers of one `p(pi)`.  It is
the same `8/3` as the campaign's `Im_min` and as Moh Prop. 6.3's unproved
premise -- now structural rather than a numerical coincidence.

## 3. Complete classification of admissible split orders

`DERIVED-SOURCE`.  Write the p.209 place's Jacobian face equation.  With
`a = ord T_3(sigma) = 40*delta - 105`, `b = ord g(sigma) = 27*delta - 72`,
`deg p = u_s = 3`, `deg q = 13*u_s + 1 = 40`, Xu (7.1) has matching orders on
both sides for every `delta` and reduces to

```text
9*a*q*p' - b*q'*p = c * p^14,    c = 27a - 40b = 45  (delta-independent).
```

At a root of `p` of multiplicity `mm` with `ord_q = r`, either `r = 13mm + 1`
(non-resonant) or `9*a*mm = b*r`, i.e. `r = rho*mm` with
`rho = 5(8delta-21)/(3delta-8)`.  `deg q = 40` is the budget.  Screening
`1 < delta < 8/3` with `den(delta) <= 3`:

| `delta` | `[1,1,1]` | `[2,1]` |
|---|---|---|
| `4/3, 3/2, 5/3, 7/3` | `rho` non-integral, non-resonant `42 > 40` -> dead | `rho` non-integral, non-resonant `41 > 40` -> dead |
| `2` | `rho = 25/2` -> dead | `rho(2) = 25`; vector `(25,14)`, total `39 <= 40` -> **alive** |
| `5/2` | `rho = 10`; vectors `(10,10,10)`, `(14,10,10)`, `(10,14,14)` -> **alive** | vectors `(20,10),(20,14),(27,10)` -> alive at ODE level |

The `mu_e` Galois action on the `t^{1/e}`-ramified place acts by
`pi -> zeta_e pi` and must fix the root multiset of `p` **with
multiplicities**.  For `e = 2` a `[2,1]` multiset of distinct roots would need
both the double and the simple root at `pi = 0`: impossible.  Hence

```text
delta = 2   ->  partition [2,1] only, p = pi^2(pi + 3a)              (branch B)
delta = 5/2 ->  partition [1,1,1] only, p = pi(pi^2 - c), c != 0.
```

`FALLACY-v2 / floor-attainment`: the table is an exhaustive *screen*.  Alive
means the face system has a solution, never that a Keller pair exists.

Face solutions, verified symbolically (residual identically zero):

```text
delta = 2  : p = pi^2(pi+3a), q = pi^25(pi+3a)^14(pi-2a)        [charged family]
delta = 5/2: p = pi(pi^2-c),  q = p^10 * q1,  q1' = 10 p^3, deg q1 = 10.
```

Xu writes `q1 = -2 int p^3`; the scalar differs only by his normalisation of
`q`, not by content.  After the gauge `pi -> lam*pi` (which sends `c -> c/lam^2`
and `a -> lam*a`) branch B's face is a **single point** and the `delta = 5/2`
face is a **1-parameter** family (the integration constant `e_0` of `q1`).

## 4. The two split trees are completely determined

`DERIVED-SOURCE`.  Continue past the split order along one packet of `gk` roots
of `g` (`fk = gk*2/3`, `T2k = gk*5/9`, plus the `T_3` multiplicity).  The order
identity gives `ord g(sigma') = -72 + delta*(27-gk) + gk*delta'`; the packet
stays unsplit while `ord g < 0` because the common face `p` then has degree
`gcd(fk, gk, T2k, T3k) = 1` (Xu §8(iii)'s argument, verified per packet).  The
packet becomes final exactly at `ord g = 0`.  Independently, Xu's Thm 4.7 proof
step `delta_sigma = -ord f_y(alpha)` gives the same numbers from
`48 - sum(contacts)`.  Both derivations agree in every row.

```text
branch B (delta = 2)                 delta = 5/2
 27 g-roots -> 18 + 9                 27 g-roots -> 9 + 9 + 9
 18 g / 12 f : final at delta = 3     each 9 g / 6 f : final at delta = 3
  9 g /  6 f : final at delta = 4
 Im = 1 + 2 + 3 = 6                   Im = 1 + 3*2 = 7
 sum |D|(delta-1) = 42                sum |D|(delta-1) = 36
 principal places: 27, all e = 1      principal places: 18, nine with e = 2
```

Every final order clears the sharpened principal floor `V_s/u_s = 8/3`
(`3, 4` and `3, 3, 3`), so `xu-principal-floor-sol56` is consistent with both.
`IM = -sum_{P_M}|D^f_sigma| lambda^g_sigma`; the major tower gives
`lambda^g(sigma_1) = -1/3` at `delta_1 = 4/9` over `48` major `f`-roots, so
`IM = 16` exactly.  Corollary 5.3 passes for both (`16 >= 6`, `16 >= 7`).

## 5. Theorem 3.4 with the exact `I(f_xi, f_y)`: a tree-blind identity

The task asked whether Theorem 4.7(i) at **equality**, evaluated with Theorem
3.4's exact `I(f_xi, f_y)`, separates the branches.  It does not, and the
reason is structural.

Theorem 3.4 sums `-(e(f_sigma)-1)lambda_sigma` over splitting `pi`-roots.  On
the principal side only the split order contributes (the final roots have
`lambda_sigma = 0`), giving `-(k-1) * (m/d_s)(u_s*delta - v_s)` for a `k`-way
split.  Xu's (4.3) is an equality and contributes
`sum_{P_m}|D_sigma^{f_xi}|(delta_sigma-1)`.  The driver evaluates both on every
admissible tree:

| tree | `sum |D|(delta-1)` | Thm 3.4 principal term | difference |
|---|---:|---:|---:|
| `delta=2`, `[2,1]` | 42 | 12 | **30** |
| `delta=5/2`, `[1,1,1]` | 36 | 6 | **30** |
| `delta=2`, `[1,1,1]` (dead control) | 54 | 24 | **30** |

The constancy is an exact identity, not a coincidence.  For a `k`-way split at
`delta` into principal `f`-packets of sizes `n_1,...,n_k` with `sum n_i = 18`,
§4 gives `n_i*delta_i = 48 - delta(18 - n_i)`, so

```text
sum n_i(delta_i - 1) = 48k - 18*delta*(k-1) - 18,
Thm 3.4 principal term = (k-1)*6*(8 - 3*delta) = (k-1)(48 - 18*delta),
difference = 30    for every k and every delta.
```

Both quantities count the same `f_y` zeros through the same partition, so
Theorem 3.4 and (4.3) are two readings of one identity.  The only slack in
4.7(i) is Xu's (4.4) step `ord g_y(beta) >= -delta_sigma`, a *lower* bound,
which therefore never tightens against a candidate.
`SATURATED-EMPTY[THM-34-EQUALITY-SEPARATION]`.

The genus/Milnor route is *not* tree-blind and is the one live external hook.
The principal places differ: branch B has `27` unramified non-proper places,
`delta = 5/2` has `18` (nine with `e = 2`).  Fable's §5.2 identity
`2g_c - 2 + N + r_prop = sum_np (e_P - 1)` with `N = I(f_xi,g) = IM = 16` is
therefore branch-sensitive through `r_np`.  `NOT-EVALUATED-HERE`: its `e_P` is
`ord_P(f - a_0)`, which needs one Puiseux coefficient beyond the tree, and
`r_prop`/`g_c` need the p.202 major tree's final structure, which this desk did
not derive.  Typed as `OPEN[9966-RH-FIBRE-EVAL]`, cheapest test in §7.

## 6. Why `(16,12)` closes and `(99,66)` does not

`SOURCE-READ`, Moh p.207 and p.210.  The `(16,12)` row has `u_3 = d_3 - v_3 = 1`
and Moh chooses coordinates so the minor `pi`-root is
`sigma* = t^-1 + a_0 + a_1 t + a_2 t^2 + pi t^3` -- one root, no `pi`-polynomial
to split.  With `u_s = 1` the principal face `p(pi)` has degree 1 forever, so
Prop. 6.4 pins `delta* = v_s/u_s = v_s` and the entire principal branch is a
**single** Puiseux series.  Then p.210's closing move is available: `g` has one
approximate-root expansion
`g = f^{3/2} + a f^{-1/2} + b f^{-6/10} + c(x^3+d) f^{-9/10} + ...`, and, in
Moh's own words, "*Since `g` is a polynomial in `y`, then the powerseries in
`y^-1` in the expression (1) shall naturally cancel out*", which is exactly
equations (3) and (4).  The killer is the `pi^-1` tail at the **same** place:
polynomiality in the original coordinates, evaluated on the *one* branch.

At `(99,66)`, `u_s = 3` and the principal packet **does** split, so `g` at the
principal point is `2` or `3` Puiseux branches with different final orders
(`3, 4` or `3,3,3`) and there is no single expansion whose tail can be
cancelled.  Cancelling one branch's tail constrains only that branch's
coefficients, and each new band introduces new Puiseux coefficients at the rate
it consumes equations -- which is exactly why `moh9966-B-lift-sol56` sees
growing dimension through band 5.  The local lift at one `pi`-root cannot close
in principle: the closing constraint lives elsewhere.

**The proposed joint object.**  Not another band, and not the `p.209`
`Omega`-image alone.  Take Prop. 6.2's `(y,z)` coordinates (`z = y - bx - e`,
`b != 0`), in which the two points at infinity are the two coordinate
directions and the top forms are forced monomials:

```text
Fbar in span{ y^i z^j : i <= 48, j <= 18, i + j <= 66 },  corner y^48 z^18
Gbar in span{ y^i z^j : i <= 72, j <= 27, i + j <= 99 },  corner y^72 z^27
J_{y,z}(Fbar, Gbar) = const != 0
+ the principal-point branch data of §4 imposed at z-direction infinity
+ the major tower (delta_2 = 1/3, delta_1 = 4/9) imposed at y-direction infinity.
```

Sizes, exact.  The full total-degree arrays have `2278 + 5050 = 7328`
coefficients (`7326` in the monic gauge; Moh prints `7348` on p.207 under a
convention this report does not silently identify with either).  Because
`48 + 18 = 66` and `72 + 27 = 99`, the Prop. 6.2 bidegree boxes are exactly the
full rectangles: `49*19 = 931` and `73*28 = 2044`, total `2975`, a factor
`2.46` cut before any branch data is imposed.  That is the honest size of the
smallest first-principles joint object; Moh's unprinted "11 variables" is a
further, unexhibited elimination.  `OPEN[MOH-11-VARIABLE-ELIMINATION]` stands.

## 7. Typed list: every necessary condition now known at `(99,66)`

| # | condition | source / type | leaves open |
|---|---|---|---|
| N1 | `d = (99,33,11,1)`, `u_3 = 3`, `v_3 = 8`, `delta_2 = 1/3`, `delta_1 = 4/9` | Moh p.194 formula, checked against p.202 | both |
| N2 | principal branch is minor: `u_3 = 3 <= d_3/(n-M_3) = 11/2` | Moh p.190, `PRINTED` | both |
| N3 | `ord g(sigma) = 9(3delta-8)`; detector iff `delta < 8/3` | Moh p.191, `DERIVED-SOURCE` | both |
| N4 | `delta* >= 1`, and no split at `delta = 1` | Moh Prop. 6.1; Xu Prop. 7.3, `PRINTED` | both |
| N5 | `den(delta) <= u_s = 3` | Xu p.13, `PRINTED` (Xu asserts; proof not exhibited) | both |
| N6 | `delta in {2, 5/2}` | §3 enumeration, `DERIVED-SOURCE` = Xu §8(i) | both |
| N7 | no `u_s`-way split below `(v_s+1)/(u_s+1) = 9/4` | Xu Cor. 7.5, `PRINTED` | kills `[1,1,1]` at 2 only |
| N8 | `delta=2 -> [2,1]`, `q`-vector `(25,14)`; face = one point mod gauge | §3, `DERIVED-SOURCE` | branch B |
| N9 | `delta=5/2 -> [1,1,1]`, `p = pi(pi^2-c)`; face 1-parameter mod gauge | §3 + Galois, `DERIVED-SOURCE` | `delta=5/2` |
| N10 | no second split before the final order; finals `(3,4)` resp. `(3,3,3)` | §4, `DERIVED-SOURCE` = Xu §8(iii) generalised | both |
| N11 | `delta_sigma >= V_s/u_s = 8/3` at every principal final root | `xu-principal-floor-sol56`, `PROMOTED` | both (`3,4` / `3,3,3` clear it) |
| N12 | `IM >= Im`: `16 >= 6` / `16 >= 7` | Xu Cor. 5.3, `PRINTED` | both |
| N13 | Thm 3.4 = (4.3) bookkeeping, difference `30` | §5, `DERIVED-SOURCE` | both (tree-blind) |
| N14 | `Fbar, Gbar` in the Prop. 6.2 bidegree boxes with monomial corners | Moh Prop. 6.2, `PRINTED` | both, `not yet used as a system` |
| N15 | `Omega`-polynomiality of the `pi^-1` tail at the principal place | Moh p.210 method, `PRINTED` for `u_s = 1` only | both, `OPEN` for `u_s = 3` |

**Cheapest computation that would decide `(99,66)`.**  Attack `delta = 5/2`
first: after §3 it is a `1`-parameter face with a `(3,3,3)` tree and a
*ramified* place, i.e. maximally rigid.  Take §6's joint two-point system
restricted to the `z`-direction jets that tree forces:

* unknowns: the `Gbar` coefficients on the `z`-adic bands `z^27, ..., z^24`
  compatible with `p = pi(pi^2-1)` (`c` gauged to `1`), together with `e_0`,
  the three final-root coefficient vectors at `delta = 3`, and the Jacobian
  constant.  Under the `mu_2` symmetry the unknown count is
  `<= 60` after the `y`-degree box of N14 truncates each band;
* equations: `J_{y,z}(Fbar, Gbar) = c` band by band through `z`-adic order 4,
  plus `Fbar = ` approximate-root relation, plus the `mu_2`-equivariance;
* tool: Singular, Rabinowitsch-saturated at `c != 0` and `gamma != 0` (never
  `sat()`), over `F_32003`, `F_32009`, `F_32027` and `Q`, with the
  empty/nonempty-wrapper and unsaturated-nonunit controls.

A `[1]` there kills `delta = 5/2` and reduces `(99,66)` to branch B, whose face
is a *single point* -- at which the same system has no free parameter and is a
finite check.  Second-cheapest and independent: evaluate Fable's §5.2
Riemann--Hurwitz identity with `N = 16` on both trees.  It needs `g_c`,
`r_prop` and the escape orders (the p.202 major tree's final structure, one
desk, plus one Puiseux coefficient per principal place) and is the only
identified condition that is **not** tree-blind.

## 8. FALLACY-v2 audit

Flag/place/series: Moh's major radii `(4/9, 1/3, -1)` are never identified with
the split order `delta` or with the combined minor radius `delta*`; §2's ceiling
is on `delta` and N11's floor is on the final `delta_sigma` -- different objects
that share the value `8/3` for the stated reason.  Carrier/attainment: "alive"
in §3 is a screen survivor, never `FULL_ACTUAL_EXIT`; the branch-B and
`delta = 5/2` faces are `REPRESENTATIVE[FACE-ODE]` points, not Keller pairs.
Floor/attainment: `IM = 16` is the all-major value, used only to make N12 pass,
so no kill rests on it.  `sat()`: no ideal was saturated in this desk; §7
declares the Rabinowitsch form and the controls.  Prime mark: `p'`, `q'` are
`d/dpi`, stated, never a label.  Variable/ring map: the `(y,z)` map is Moh
p.194 eq. (10) with `b != 0` declared; the `pi`-gauge of §3 is given with its
action on `a` and `c`.  Raw remainder degree: the `deg q = 40` budget enumerates
both the resonant and non-resonant branches rather than dropping leaders.  No
exit-price assertion is made, so no `charge_basis` line is licensed.

## 9. Reproduction

`python3 box/g9966rev-20260903/g9966rev_driver.py > .../results.json`.
Python 3, SymPy 1.12; under 10 s, no Singular call in this desk.  Artifacts:
`box/g9966rev-20260903/{g9966rev_driver.py, results.json, inputs.sha256,
artifacts.sha256, pages/*.png}`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `21198`.
- Body SHA-256:
  `4e4db63a70024910f9467accfe64ea9211700803019dd13725e080b7a404f8d2`.
- Frozen basis: `afb7e21be9164e6fed9748614361f51db26e1410`.
