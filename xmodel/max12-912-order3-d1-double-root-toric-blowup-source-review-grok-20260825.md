# Hostile source review — strict D1 double-root toric blow-up

| Field | Value |
|---|---|
| Claim under review | Frozen pre-solver source for the strict D1 double-root toric chart: exact ordinary tails of `f=K^3+K*x*Qhat+x^2*Rhat`, `K=z^3+pz+c`, `kbar=x*y*k`, targets `Lambda^(12+l) gamma_l` with loads at 15/18 and row 8 equal to `Lambda^20*(1+tau)`, interior saturation by `x*y*tau*rho`, boundary `x=y=Lambda=tau=rho=0`, `a=1`, `h=0`, leading family `Qhat(1)=Qhat(-2)=0`, `Qhat'(1)!=0`, `27*Rhat(1)=Qhat'(1)^2`, two independent encodings A/B. No solver verdict |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | the leading-ray Newton-fan statement (every `beta<6` case except `alpha=2 beta` with `Q0=q(z-1)(z+2)` and `R0(1)=q^2/3` is excluded) is **not in this frozen package**. It is consumed as a separately charged lemma, as the preregistration states. It was re-proved here and does not break a numbered source claim. Endpoints `beta=0,6`, the equal-slope chart `v(Lambda)=3 v(tau)`, the `tau`-unit chart, fixed-load specialization, finite-determinacy, and D1/JC2 are correctly *not* claimed |
| Evidence tier | independent integer/rational reconstruction of `a0..a7` and `kbar`; independent `build()` of the charged ordinary tails; independent sparse substitution matching both hosts' row digests termwise; independent expansion of all four emitted Singular scripts, proving factored A and expanded B are identical polynomials; exact univariate remainder calculus of the double-root Newton numerators over `Q`; Jacobian/cusp/boundary identities over `Q`; scheme-theoretic comparison of `sat` and Rabinowitsch elimination. No Singular run, no AWS compiler run, no solver inference |
| Reviewer / model | Grok 4.6 (xAI). Independent of the live solver result |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD at launch | `4fe628a133ae62e16b1bec5e4ed6fcee420dd880` |
| Git HEAD at close | `4fe628a133ae62e16b1bec5e4ed6fcee420dd880` (unchanged) |
| Python | host CPython 3.14.6 (hashes, tail reconstruction, sparse substitution, Singular-string parser, Newton remainders) |
| Singular | not executed |
| Host | Darwin arm64, local Mac. Charged compiler/solver are AWS-only; they were not run |

Frozen hashes charged in the prompt, recomputed and matched:

```text
015ed8156197ba4cfac55cbc6d33379d7545739bfe657856febd8e17c8d3913c  cases/max12_912_order3_d1_double_root_toric_blowup_20260825/FREEZE.sha256
7e6cce9beaed80cc4f75d33fddabc9b3a12d619f7831e110d58e4c3241d0a061  cases/max12_912_order3_d1_double_root_toric_blowup_20260825/SOURCE_CLOSURE.sha256
3b200a84f0d7ff3e3b30612e0e10d6792cbf1ebeda0da721ce4eef0103951228  cases/max12_912_order3_d1_double_root_toric_blowup_20260825/CUSTODY_PRELAUNCH.sha256
```

Every entry of `FREEZE.sha256`, `SOURCE_CLOSURE.sha256`, `CUSTODY_PRELAUNCH.sha256`, `compile_source.sha256`, `solve_source_box02_A.sha256`, and `solve_source_r6d_B.sha256` was recomputed. Nested `repo/` prefixes map to the same repository files; nested `compiled/*.sing` prefixes map to the host-specific emitted scripts. All match. Empty compiler stderr files hash to the SHA-256 of the empty byte string `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. Both compiler return codes are `0`.

The two hosts differ in emitted scripts **only** by the printed `AWS_TAG`. After stripping that line the four scripts collapse to two byte-identical encodings. Row digests in the two compiler stdout files are identical; payload hashes differ only because they include the tag.

Read in full before the verdict: `PREREGISTRATION.md`, `README.md`, `compile_toric_blowup.py`, `remote_worker.sh`, `AWS_REGISTRATION.md`, charged `independent_reconstruct.py` at SHA-256 `67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623`, both hosts' `compiler.stdout` / `compiler.rc` / empty `compiler.stderr`, and all four emitted `.sing` files. Predecessor Newton V3 and the VDIM-125 exact chart were used only as the separately charged lemma the preregistration consumes, and as the finite exceptional algebra this chart is required to distinguish. No solver stdout was read for a unit/nonunit inference.

Tried hard, and failed, to break `a0..a7` against `K^3+K x Qhat+x^2 Rhat`; to make `kbar` other than `x y k`; to produce an ordinary-weight mismatch; to make a substituted row survive `x=0`; to make a `k` monomial appear without matching `x` and `y`; to make the factored and expanded rows differ as polynomials; to find a `beta<6` leading ray other than `alpha=2 beta` with `Q0=q(z-1)(z+2)` and `R0(1)=q^2/3`; to make the factor 27 other than `(Qhat'(1))^2 / (q^2/3)`; to make sequential principal saturations differ from saturation by the product in a Noetherian ring; to make `(lp(2),dp(18))` the wrong block order; to make `eliminate` drop a load; to read `H!=1` as a fixed-load lift; and to identify this scheme with the VDIM-125 exceptional algebra.

---

## Promotion

**Accept `THE FROZEN TORIC-BLOW-UP SOURCE IS AN EXACT, UNTRUNCATED SUBSTITUTION OF THE CHARGED ORDINARY EIGHT-TAIL SYSTEM INTO THE CHART f=K^3+K*x*Qhat+x^2*Rhat, K=z^3+p z+c, kbar=x*y*k, x y=Lambda^6, Lambda=tau^3 rho, WITH TARGETS Lambda^(12+l) gamma_l, LOADS PRECISELY AT 15/18 AND ROW 8 EQUAL TO Lambda^20 (1+tau). THE TWO ENCODINGS ARE IDENTICAL POLYNOMIALS. INTERIOR SATURATION BY x y tau rho FOLLOWED BY THE DISPLAYED BOUNDARY AND PRINCIPAL SATURATION BY Qhat'(1) IS THE CORRECT CLOSURE OF THE OPEN NILPOTENT LEADING FAMILY. A UNIT RESULT WOULD EXCLUDE THIS CHART FOR EVERY FIXED LOAD. A NONUNIT RESULT IS ONLY A TOTAL-LOAD-SPACE SURVIVOR. THE NEWTON-FAN CLASSIFICATION IS A SEPARATE LEMMA, RE-PROVED HERE FOR LEADING RAYS WITH 0<beta<6. THIS PACKAGE ALONE DOES NOT PROVE D1 OR JC2.`**

Do not promote this to: a solver unit or nonunit; a fixed-load formal lift; a classification of the equal-slope or `tau`-unit charts; a finite-determinacy bound from VDIM 125; emptiness of every D1 coefficient-infinity arc; or JC2.

---

## Charge 1 — coefficient images, `kbar`, tails, targets

**CONFIRMED**

Let `K=z^3+p z+c`, `Qhat=q2 z^2+q1 z+q0`, `Rhat=r2 z^2+r1 z+r0`. Direct expansion of `f=K^3+K x Qhat+x^2 Rhat` over `Z[p,c,x,q_i,r_i][z]` gives a monic degree-9 polynomial with vanishing `z^8` coefficient and

```text
a0 = c^3 + x c q0 + x^2 r0
a1 = 3 p c^2 + x (p q0 + c q1) + x^2 r1
a2 = 3 p^2 c + x (p q1 + c q2) + x^2 r2
a3 = p^3 + 3 c^2 + x (q0 + p q2)
a4 = 6 p c + x q1
a5 = 3 p^2 + x q2
a6 = 3 c
a7 = 3 p
```

These are identical to the compiler's `COEFFICIENT_STRINGS`. The reconstruction ring is `(a0,...,a7,k)` with `u_{9-i}=a_i` for `i=0..7` and no `a8`, so the missing `z^8` term is the depressed form forced by `K`. The ninth source coordinate is `kbar=x y k`, not an unscaled `k`.

Independent `build()` of `independent_reconstruct.py` (arithmetic only; `main` was not called) produced ordinary supports

```text
25, 36, 42, 55, 63, 84, 94, 121
```

for rows `ell=1..8`. Every source monomial of row `ell` has weight

```text
sum_{i=0}^{7} (9-i) a_i + 6 k = 12+ell
```

matching the compiler's ordinary-weight report. The reconstruction defines `tails[ell] = - [w^{-ell}] g(z(w))` with `g=F12+k F6`, so the charged equation is `r_ell = Lambda^{12+ell} gamma_ell`. Targets used by both the compiler and both encodings are

```text
gamma_3 = mu,     row 3: Lambda^{15} mu
gamma_6 = nu,     row 6: Lambda^{18} nu
gamma_8 = 1+tau,  row 8: Lambda^{20} (1+tau)
gamma_ell = 0 otherwise.
```

Signs: each charged row is `raw - target`. After substitution, rows 3, 6, 8 gain exactly the displayed target monomials and no others (`16→17`, `34→35`, `76→78`). This is the same isotrivial normalization already used by the reviewed order-20 squarefree obstruction, including leading coefficient `1` on row 8.

---

## Charge 2 — compiler anchoring, substitution, row identity

**CONFIRMED**

The compiler pins `independent_reconstruct.py` at SHA-256 `67343b56...` before import, refuses non-AWS execution, and runs these checks in order: ordinary weights, sparse substitution of every source monomial via a power table of the nine images, vanishing of every substituted raw row at `x=0`, `kbar` scaling (`every k` in a substituted monomial is accompanied by at least as many `x` and `y`), and `raw - charged = target`. Independent reconstruction of the same pipeline reproduced both hosts' eight raw and eight charged row SHA-256 digests exactly:

| ell | raw support / sha256 prefix | charged support / sha256 prefix |
|---|---|---|
| 1 | 6 / `4797a034` | 6 / `4797a034` |
| 2 | 11 / `ce8105be` | 11 / `ce8105be` |
| 3 | 16 / `5c9dd3f5` | 17 / `25e9d48b` |
| 4 | 25 / `0c573bb8` | 25 / `0c573bb8` |
| 5 | 31 / `1c70e6e8` | 31 / `1c70e6e8` |
| 6 | 34 / `24c962cd` | 35 / `43241d67` |
| 7 | 57 / `69f7c5a0` | 57 / `69f7c5a0` |
| 8 | 76 / `c753d12f` | 78 / `e936bbd3` |

Common-cubic vanishing at `x=0` holds because `f` becomes `K^3` and `kbar` becomes `0`, so `g=F12(K^3)` is a polynomial in the inverse of `K` and contributes no negative tails. The `kbar` check is the image of `k |-> x y k`; source maxima show `k` occurs at most to the first power.

A dedicated parser for Singular poly strings, including parenthesized rationals `(n/d)` and `^` powers, expanded every `E1..E8` in all four scripts. Factored encoding A, expanded encoding B, and the independent substituted polynomials are **identical** as elements of `Q[p,c,x,y,la,tau,q2,q1,q0,r2,r1,r0,k,mu,nu]`: eight equalities, not merely matching support counts. No Python indexing, multiplication, specialization, parenthesization, or rational-coefficient error survived this identity. The emitted strings are valid input for a characteristic-zero Singular polynomial ring (rationals appear only as `(n/d)` or integers; the predecessor V2 `q^2/3` parse failure is not present here).

All six normal coefficients `q2,q1,q0,r2,r1,r0` occur in the charged rows. Coordinates `a,h` do not occur in the tail rows; they enter only through `AX=p+3 a^2` and `CU=c-2 a^3-h`. Loads `k,mu,nu` occur and are never inverted.

---

## Charge 3 — chart coverage and the Newton-fan lemma

**CONFIRMED** as a coverage statement for this chart, with the Newton-fan classification identified as a lemma **not present in this frozen package** and re-proved here for leading rays.

Work at the normalized double-root `K0=(z-1)^2(z+2)=z^3-3z+2`, residue algebra `A=Q[z]/(K0)`, `L=z-1`, `U=z+2`, `N=L U`. Write `beta=v(Q)`, `alpha=v(R)` for coefficient-wise valuation, `Q0,R0` the leading degree-at-most-two polynomials. For `beta<6` the `kbar` layers (`v>=6`) are strictly later than the pure `Q^3` layer of valuation `3 beta`, so they do not affect the leading-ray table. Binomial leading numerators over `K^2` are

```text
(4/9) Q R K + (2/9) R^2 - (4/81) Q^3
```

with first-arriving pieces `QR/K` (`beta+alpha`), `R^2/K^2` (`2 alpha`), `Q^3/K^2` (`3 beta`). Exact remainder calculus over `Q`:

- `K0 | Q0^3` with `deg Q0 <= 2` if and only if `Q0` is a scalar multiple of `N`. Same for `R0^2`.
- `R0^2` is never `0` modulo `K0^2` for nonzero `deg<=2` `R0`. So `alpha<beta` produces negative tails of `R^2/K^2` (even on the nilpotent `R0 || N`, where the function is `r^2/(z-1)^2`).
- Combined `alpha=beta` numerator `(4/9)QRK+(2/9)R^2` reduces in `A` to a multiple of `R0^2`, so `R0 || N` is necessary. Writing `R0=r N` makes the `K0^2`-remainder equivalent to `(4/9) r Q0 N + (2/9) r^2 U`; evaluating at the double root `z=1` (where `N(1)=0` and `U(1)=3`) yields `(2/3) r^2`, nonzero in characteristic zero unless `r=0`. Excluded.
- `K0 | Q0 R0` holds on a classified mixed-vanishing locus, but the subsequent `R^2` or `Q^3` layer, written over `K0^2`, never vanishes for `deg<=2`. In particular `Q0^3 ≡ 0 (mod K0^2)` has **no** nonzero degree-at-most-two solution. This kills `beta<alpha<3 beta/2` after the `QR` layer, kills `3 beta/2 < alpha < 2 beta` after `QR`, and kills `alpha>2 beta` at the first layer.
- At `alpha=3 beta/2` the second layer is `(2/9)R^2-(4/81)Q^3` after `K0 | QR`. The simple-root factor `A/(U)` is a field, so the pair `Q0 R0=0` and `18 R0^2=4 Q0^3` there forces `Q0(-2)=R0(-2)=0`. Every remaining structural type (`N,N`, `L^2,U`, `N,L`, …) has nonzero remainder modulo `K0^2`; in particular `(N,N)` has constant term `40/27`. Excluded.
- At `alpha=2 beta` the combined `3 beta` numerator is `(4/81) Q (9 R K - Q^2)`. Reducing modulo `K0` forces `Q0^3=0` in `A`, hence `Q0=q N=q(z-1)(z+2)`. Substituting this form, the remainder modulo `K0^2` is affine in `(r0,r1,r2)` of rank one: it vanishes if and only if `R0(1)=r0+r1+r2=q^2/3`. The homogeneous kernel is two-dimensional. Direct check: `Q0=q(z^2+z-2)`, `R0=q^2/3` (constant) gives remainder zero; every extra direction with the same `R0(1)` also gives remainder zero; `Q0` not parallel to `N` never cancels.

Target coincidences at 15 and 18 cannot rescue the excluded rows: a layer that is already a nonzero remainder modulo `K0^2` of degree at most 5 produces some tail among rows 1–6, and a scalar row-3/row-6 target is a multiple of `K0` in the `K0^2`-numerator, hence vanishes in `A` and does not cancel a non-residue-zero remainder. For the surviving ray, the cancelled `3 beta` layer is a polynomial (`-4 q^3/81` when `R0` is the constant `q^2/3`), so it contributes no negative tail and cannot itself satisfy a nonzero row-3 target; the charged eight-tail system keeps every later layer, including weight 20.

Therefore the only leading low-valuation possibility with `0<beta<6` is `alpha=2 beta`, `Q0=q(z-1)(z+2)`, `R0(1)=q^2/3`. This lemma is **not in the frozen package**. Predecessor Newton V3 proved only the displayed cancellation and a quartic successor identity, and explicitly refused a complete tropical classification. The preregistration is honest that it consumes the classification as a separately charged lemma. The lemma is now available as an independent remainder theorem; it is not smuggled as if it lived in this freeze.

Covering map. On this ray set `x` of valuation `beta`, `Q=x Qhat`, `R=x^2 Rhat`, `y` of valuation `6-beta` with `x y = Lambda^6`. Then `0<v(x),v(y)` and both tend to zero. Saturation by `x y` followed by `x=y=0` is the strict transform of `{x y != 0}` closed onto the exceptional divisor, i.e. precisely the limits of interior points with `0<beta<6` in Lambda-normalization. Charges:

- *Ramification / nonintegral beta.* A Puiseux arc with rational valuations becomes integral after a finite ramification of the parameter. The equations are polynomial, so the scheme contains the image. If the saturated boundary ideal is `(1)` there is no point over any extension, hence no ramified arc. If it is not `(1)`, that still does not produce a formal lift.
- *Amplitude.* `Qhat` is free of scale; `QD=Qhat'(1)` is inverted only on the boundary open `q!=0`. Residual scaling between `Q` and `R` is the relation `alpha=2 beta`, already imposed by `R=x^2 Rhat`.
- *Unequal coefficient valuations.* The leading polynomials `Q0,R0` are the min-valuation forms; every special shape is a special case of the table above. Higher-valuation corrections sit in the free `Qhat,Rhat` and are included in the closure.
- *Endpoints `beta=0` and `beta=6`.* These make `x` or `y` a unit and are excluded by the boundary `x=y=0` after saturating `x y != 0`. `beta=0` is not centred on the common cubic. `beta=6` is the squarefree bound, a different theorem.
- *Overcoverage.* If `v(Qhat)>0` then actual `beta>v(x)`, a higher-valuation point of the same chart. Harmless for exclusion: a unit result still kills the intended open.

This chart therefore covers exactly the Puiseux arcs with `0<beta<6` on the unique surviving leading ray, together with some higher-valuation interior, and does not cover the endpoints or any excluded leading ray.

---

## Charge 4 — simultaneous strict-slope chart `Lambda=tau^3 rho`

**CONFIRMED**

`LT = la - tau^3 rho` is in the ideal. Interior saturation includes `tau` and `rho`, then the boundary sets `tau=rho=0`. Thus every interior point used in the closure has `tau,rho` invertible, and every boundary point is a limit with `v(tau)>0` and `v(rho)>0`. Then

```text
v(Lambda) = 3 v(tau) + v(rho) > 3 v(tau) > 0.
```

Compatible with the toric relation: `x y = Lambda^6` and `Lambda = tau^3 rho` give `x y = tau^9 rho^6`, so both `x` and `y` vanish whenever `tau` and `rho` do. Compatible with row 8: the target is `la^{20}(1+tau)`, the same `tau`. On this chart `1+tau → 1`, leading coefficient `1`.

Covered: every strict slope with `v(Lambda)/v(tau) > 3` and `v(tau)>0`.

Not covered:

- the equal slope `v(Lambda)=3 v(tau)`, i.e. `rho` a unit (`v(rho)=0`);
- the opposite inequality `v(Lambda) < 3 v(tau)`, a different chart `tau^3 = Lambda * sigma`;
- `v(tau)=0`, including every finite nonzero value of `tau` (row 8 leading coefficient a unit other than the limit `1`).

The monomial positive control `rho=tau`, `la=tau^4`, `x=tau^8`, `y=tau^{16}` is one integral point of the covered open: `v(Lambda)=4>3=3 v(tau)`, and `v(x)/v(Lambda)=2 ∈ (0,6)`.

---

## Charge 5 — moving axis/cusp, étaleness, six normal coefficients

**CONFIRMED**

```text
p = -3 a^2,     c = 2 a^3 + h,
K = (z-a)^2 (z+2a) + h,
Delta = -4 p^3 - 27 c^2 = -27 h (4 a^3 + h).
```

The first two identities are `AX` and `CU`. The Jacobian matrix of `(p,c)` in `(a,h)` is

```text
[-6 a    0]
[ 6 a^2  1],     det = -6 a,
```

equal to `-6` at `(a,h)=(1,0)`. Étale, hence a local analytic (and formal) isomorphism of the `(p,c)`-plane onto the `(a,h)`-plane at the normalized double-root `(-3,2)`. Retaining `a,h` as variables through interior saturation, and imposing `a-1=h=0` only on the boundary, includes every local motion of the cubic that returns to this point: an arc of `(p,c)` near `(-3,2)` lifts uniquely to `(a,h)` near `(1,0)` and is not killed by specializing the centre too early.

All three coefficients of `Qhat` and of `Rhat` are ring variables and occur in the charged rows. This is the raw coefficient chart, not the Hermite chart of the predecessor (which divides by `9 a^2` and would have been illegal at `a=0` in the interior). Degeneracy of the cusp coordinates at `a=0` is irrelevant to the boundary slice `a=1`.

---

## Charge 6 — boundary equations and the factor 27

**CONFIRMED**

On the surviving ray `Q0=q N=q(z-1)(z+2)=q(z^2+z-2)`, so

```text
Qhat(1) = q2+q1+q0 = 0,           QA
Qhat(-2) = 4 q2 - 2 q1 + q0 = 0,  QB
Qhat'(1) = 2 q2 + q1 = 3 q,       QD
```

and the cancellation condition is `R0(1)=q^2/3`. Then

```text
Qhat'(1)^2 = 9 q^2,     27 Rhat(1) = 27 (q^2/3) = 9 q^2,
```

so `LC = 27 RA - QD^2` is exactly that condition. The factor 27 is `(3 q)^2 / (q^2/3)` and is not a mis-normalized 9 or 81. The rank-one affine system of Charge 3 shows that this is the only condition on `Rhat`: the other two directions (for example a complement to `RA` in `(r0,r1,r2)`) remain free. Imposing a constant-`Rhat` slice would have been too strict.

Saturating by `QD` **after** taking the boundary is the correct closure of the open `q != 0` on the exceptional divisor. Saturating by `QD` in the interior would invert `Qhat'(1)` along the whole arc and exclude legitimate paths on which `q` has positive valuation in a non-leading coordinate. A boundary point with `QD != 0` is automatically a limit of interior points with `QD != 0`. Combined with `QA,QB,LC`, this is the closure of the nilpotent open leading family.

---

## Charge 7 — encoding A scheme operations

**CONFIRMED**

Ring `R=0,(p,c,a,h,x,y,la,tau,rho,q2,q1,q0,r2,r1,r0,k,mu,nu),dp` is characteristic zero, global degree order, eighteen variables, no auxiliary inverse. `LIB "elim.lib"` and `list SX=sat(I,CX); ideal S1=SX[1];` is the documented Singular API: `sat(I,J)` returns a list whose first entry is `I:J^infty`.

In any Noetherian ring, sequential principal saturations equal saturation by the product. The colon chain `I ⊆ I:f ⊆ I:f^2 ⊆ ...` stabilizes at `I:f^N = I:f^infty`. Then

```text
(I : x^infty) : y^infty : tau^infty : rho^infty
  = I : (x y tau rho)^infty.
```

Four calls `sat(-,x)`, `sat(-,y)`, `sat(-,tau)`, `sat(-,rho)` therefore compute interior saturation by `INTERIOR=x*y*tau*rho`. Boundary addition `S4, x, y, la, tau, rho, a-1, h, QA, QB, LC` is the intersection of that strict transform with the exceptional divisor and the leading family. Final `sat(BOUNDARY, QD)` is Charge 6.

Controls:

- Pure boundary `TOY_PURE=(x,y,tau,rho)` saturated only by `x`. This is weaker than the main path (it does not exercise `y,tau,rho`), but it is the same operation: `x ∈ (x,y,tau,rho)` so the saturation is already `(1)`, and the script correctly demands `reduce(1,GTP)==0`. It does not accidentally run a different scheme operation.
- Strict monomial arc `rho-tau, la-tau^4, x-tau^8, y-tau^{16}` is saturated by the same four sequential calls as the main path, then intersected with `x=y=la=tau=rho=0`. The closure contains the origin, so the script correctly demands that `1` does **not** reduce to 0. This is the same saturation-then-boundary operation as the charged computation.

Neither control substitutes a different colon, a radical, or an elimination of a load.

---

## Charge 8 — encoding B independently

**CONFIRMED**

Ring `R=0,(u,v,p,c,a,h,x,y,la,tau,rho,q2,q1,q0,r2,r1,r0,k,mu,nu),(lp(2),dp(18))` is valid Singular product-order syntax: lex on the first two variables `(u,v)`, degree reverse lex on the remaining eighteen named coordinates. `lp(2)` is an elimination block for `{u,v}` with `u>v`.

Rabinowitsch: for a polynomial ring,

```text
I : f^infty = ( I + (u f - 1) ) ∩ k[original].
```

Encoding B adjoins `u*INTERIOR-1` to `I` and eliminates `u`, then adjoins `v*QD-1` to `BOUNDARY` and eliminates `v`. These are the same two saturations as A. Loads `k,mu,nu` are among the last eighteen variables, never passed to `eliminate`, and never inverted. After eliminating `u` the generators do not involve `u`; after eliminating `v` they do not involve `v`. A leftover dummy ring variable `u` after the first elimination does not change membership of `1`.

`eliminate` on an already-computed standard basis is valid Singular semantics: `eliminate(I, var)` recomputes a Gröbner basis of the ideal `I` with respect to an elimination order and returns the elimination ideal. The current ring order is in fact already an elimination order for `u` (`u` is the largest variable), and after `u` is absent from generators it is an elimination order for `v`. Either way the call is legal.

Controls use the same inverse-and-eliminate operation as the main path: the pure-boundary ideal with `u*INTERIOR-1` is unit because `INTERIOR` vanishes on `(x,y,tau,rho)`; the strict monomial arc plus `u*INTERIOR-1`, after eliminating `u` and intersecting the exceptional divisor, is nonunit. `eliminate(GTA0,u)` without an extra `std` before adjoining the boundary is still an ideal; the subsequent `std(TOY_ARC_BOUNDARY)` is the membership test. No control eliminates a load or saturates by a different element.

---

## Charge 9 — fixed-load semantics

**CONFIRMED**

The ring retains polynomial coordinates `k,mu,nu` and never inverts them. A point of the total space may therefore have nonconstant load projection. The theorem sought for D1 is about constant-field loads.

- If `H=(1)`, then `1` lies in the saturated boundary ideal **before** any specialization of the loads. Specializing `k,mu,nu` to any constants (or to any values in any `Q`-algebra) preserves the unit ideal. Every fixed-load arc in this chart is therefore excluded by a unit result, uniformly in the loads, including the zero-load stratum.
- If `H != (1)`, the support may be a curve (or a component) along which `k,mu,nu` vary. That is not a fixed-load survivor and is not a formal lift of a D1 coefficient-infinity arc. It is only a nonempty subscheme of the total polynomial load space.

Repair required after any nonunit result, exactly as the preregistration states: specialize `k,mu,nu` to constants **before** saturation, or prove that every associated component of `H` is vertical over a load point (the elimination ideal in `k[k,mu,nu]` is a maximal ideal, equivalently the load projection is zero-dimensional). A printed basis of `H` is not itself that proof.

---

## Charge 10 — VDIM 125, finite-determinacy, local-to-global

**CONFIRMED**

The finite algebra with `BASIS_SIZE=101` and `VDIM=125` is the ordinary (unblown) exact local chart at the **fixed** cubic `K0=(z-1)^2(z+2)` with six free normal coefficients and no toric coordinates, no interior saturation, and no leading-family boundary. It is a finite-colength exceptional-fibre vector space, navigation only. This package is a different scheme: moving cusp coordinates, toric blow-up `(x,y,Lambda,tau,rho)`, saturation, and a leading-family slice. The preregistration states the distinction and does not infer a finite-determinacy bound, a properness theorem, or a local-to-global D1 result from VDIM 125.

No unproved finite-determinacy, properness, or curve-selection step is used as a theorem. Scheme-theoretic emptiness (`H=(1)`) excludes maps from any ring, hence excludes formal and Puiseux arcs in these coordinates, by the unit ideal, not by curve selection. Curve selection would be needed only in the converse direction (producing an algebraic curve from an analytic arc), which is not claimed. Local-to-global composition with the squarefree order-20 theorem, the endpoints, the equal-slope chart, and the `tau`-unit chart is explicitly out of scope.

---

## Firewalls enforced

- No solver unit or nonunit is inferred. A and B were still running at freeze.
- A future unit result excludes only the proven chart of Charges 3–6: the strict-slope, `0<beta<6`, nilpotent leading family, moving-axis closure. It does not exclude `beta in {0,6}`, `v(Lambda)=3 v(tau)`, `v(tau)=0`, or any other passport.
- A future nonunit result is not a lift and is not a fixed-load survivor without the Charge 9 repair.
- The Newton-fan classification remains a separate theorem obligation for any global D1 sentence, even though the leading-ray half was re-proved here.
- Nothing in this freeze proves D1 or JC2.

---

## Non-blocking remarks

1. Encoding A's pure-boundary control saturates only by `x`, not by `x y tau rho`. It is a correct instance of `sat` on a pure exceptional ideal, and the strict-arc control does exercise the four sequential calls. Repairable exposition, not a wrong operation.
2. Encoding B retains a dummy ring variable `u` after the first elimination. Membership of `1` is unaffected.
3. Predecessor Newton V3's quartic identity `(q^4/243)(5 L^2+18 L+15)` is a successor obstruction on the displayed ray, not a substitute for the eight-tail system, and is not used by this compiler.

None of these changes a numbered verdict.

---

## Scope (not enlarged)

One frozen pre-solver source package; two encodings of one chart; independent algebra of substitution, Newton leading rays at the double-root, and scheme operations. No solver output, no AWS execution, no D1 exclusion, no JC2 inference.

CONFIRMED
