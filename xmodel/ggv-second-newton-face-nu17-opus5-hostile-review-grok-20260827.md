# Hostile review: Opus5 second-Newton-face / `NU17` ideation theorem

**Reviewer:** Grok 4.6 (independent adversarial referee, different model).
**Date:** 2026-08-27.
**Target:** the leading mathematical contribution of

```text
xmodel/ideation-20260827T1606Z-opus5.md
SHA-256 9f9d3d053933560c6e555ce357025254d9237d989b4ba78f205dbb870939b4fa
```

re-derived from the frozen D3 polygons and the Jacobian definition. Producer
confidence labels, `PASS` strings, and self-audits were ignored. The Fable5
peer submission was not opened, listed, hashed, or searched. Canonical
ledgers were not edited. No AWS. No `jc2-lean` access. No heavy local
algebra: all checks are exact `Fraction` arithmetic in `/tmp`.

**Claim under review (narrow):** with the lower chart `x=tau^{-4} xi`,
`y=tau`, `F=tau^8 f`, `G=tau^{12} g`, the operator `E` of D5G/R5 becomes
`Etil=-tau^{17} J(f,g)_{x,y}`; the `(4,-1)` grading re-partitions the same
442 D3 slots; the unshifted face is square/cube; the weight-`N` endpoint is
exactness of `K^{-w(1,1)/m} dxi`; at `N=17` this is `4Kg'-3K'g=4K` with
polynomial `g`, degree law `{1, 3 deg K / 4}`, and a multiplicity
classification whose two-root slice is `gamma ≡ 3 (mod 4)`; the control
residual for `K=xi(xi-1)^7` is the displayed degree-six polynomial; the
second face was previously unnamed as a determinant tower; the upper face of
the genuine object is a vacuous monomial proxy while the lower face is pinned
by the GGV chain; a reachable row 17 would be a complete face fixture; and
the second tower is a regrade of the same 442 D5G slots.

**Not under review as a theorem, and not granted if implied:** a GGV family
exclusion, GGV landing, `G2-PSC`, `G2-BD`, cofinality, a raw `nu`-jet, JC2,
or any statement about the Fable5 peer file.

**Method.** Rehashed the charged ideation (digest above). Independently
enumerated the lattice points of the frozen D3 polygons

```text
2S = conv{(0,0),(2,0),(16,56),(0,8)},
3S = conv{(0,0),(3,0),(24,84),(0,12)},
```

equivalently `0 ≤ i ≤ 16`, `max(0,4i-8) ≤ j ≤ 3i+8` and `0 ≤ i ≤ 24`,
`max(0,4i-12) ≤ j ≤ 3i+12`. Independently expanded `J(f,g)=f_x g_y - f_y g_x`
under the two charts. Independently extracted the `tau^n` recurrence.
Independently solved `4Kg'-3K'g=4K` by exact linear algebra over `Q`.
Independently expanded the three live `8_28` control polynomials (fibre-tagged
native pair, D3 artificial completion, and the producer's `f=B^2`).
Independently searched the repository for a prior lower-chart identity,
`nu=8-4i+j` windows, target `-tau^{17}`, or `4Kg'-3K'g=4K`. Producer
random-Laurent `True` flags were not used as evidence.

**Firewall.** A correct chart identity is not a jet. A correct endpoint ODE
is not a raw row. A reachable row 17 is not a complete face system. A
reindexing of 442 slots is not a compiler. Pinning of one explicit control
is not pinning of the GGV family.

---

## Verdict table

| Item | Verdict |
|---|---|
| 1. Chart / Jacobian / sign / exponent 17 / recurrence | **CONFIRMED** |
| 2. `(4,-1)` `nu` windows, census, `F_17`/`G_17`, square/cube; chain vs control | **GAP/REPAIR** (windows/census/handles confirmed; pinning and “saturated `htil` of degree 7” overclaimed) |
| 3. General face-endpoint formula `K^{-w(1,1)/m} dxi` | **GAP/REPAIR** (ODE identity on the unshifted unmixed square/cube face; not a theorem in the advertised generality) |
| 4. Lower-face ODE, poles, degree law, multiplicity classification | **GAP/REPAIR** (ODE, pole lemma, degree law, and necessity of `gamma ≡ 3 (mod 4)` confirmed; closed form remains computational on the sufficiency side; genus sketch is not a proof) |
| 5. `K=xi(xi-1)^7` residual | **CONFIRMED** as an unmixed ODE solution; **does not** decide a raw `nu`-jet |
| 6. Repository history / novelty | **GAP/REPAIR** (tower/chart/ODE new; face itself already derived; general formula is a rewording of the author’s 1349Z `(alpha,beta,N)` slogan) |
| 7. Strategic claims | **REFUTED** on monomial-upper-face, complete-fixture, and drop-in regrade; **GAP/REPAIR** on chain pinning |

No item is a GGV landing, a family exclusion, or a license to freeze `NU17`
as specified. The chart identity and the 442-slot census are the only
statements that survive at theorem strength.

---

## Independent hashes and pins

Recomputed SHA-256 of the charged input, matching the review prompt:

```text
9f9d3d053933560c6e555ce357025254d9237d989b4ba78f205dbb870939b4fa
  xmodel/ideation-20260827T1606Z-opus5.md
```

Frozen D3 polygons and slot census were read from the live D3 freeze, not
from producer prose:

```text
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
012acfe5ca560757269fd6e332ed3c4bab2f1005bce43113109f31b705ffe022
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/FREEZE.sha256
```

The ideation’s parenthetical `012acfe5...` on `RAW_INPUT.json` is the freeze
list, not the JSON blob. Custody slop only; the polygons used below are the
JSON polygons.

Native `(4,-1)` faces of the fibre-tagged control, used only to separate
that polynomial from `B^2` and from the D3 artificial completion, were
already derived in the reviewed pinning control (not re-imported as a
theorem of this ideation):

```text
f = B^2 - x - y^8,     B = x(xy^4-1)^7,
g = B^3 - 2x^2 y^2 + y^{12} + tau x y^{15}.
```

Repository `HEAD` at review time:
`418e413593120d19e15e6546eb50c985f4b1f038`.

---

## 1. Chart, Jacobian, sign, exponent 17, recurrence — CONFIRMED

Let `J(f,g)_{x,y} = f_x g_y - f_y g_x`. The lower chart is
`x = tau^{-4} xi`, `y = tau`, so

```text
det ∂(x,y)/∂(xi,tau) = tau^{-4}.
```

Hence `J(f,g)_{xi,tau} = tau^{-4} J(f,g)_{x,y}`. Substituting
`f = tau^{-8} F`, `g = tau^{-12} G` and expanding gives

```text
J(f,g)_{xi,tau}
  = tau^{-21} [ -12 F_xi G + 8 F G_xi + tau (F_xi G_tau - F_tau G_xi) ].
```

Define the same operator the campaign writes as `E`, now in `(xi,tau)`:

```text
Etil := 12 F_xi G - 8 F G_xi - tau (F_xi G_tau - F_tau G_xi).
```

Then `J_{xi,tau} = - tau^{-21} Etil`, therefore

```text
Etil = - tau^{17} J(f,g)_{x,y}.
```

A Keller pair `J_{x,y}=1` yields `Etil = -tau^{17}`. The target exponent is
`w(f)+w(g)-w(1,1)` on a quasi-homogeneous face: lower `w=(4,-1)` gives
`w(1,1)=3` and `8+12-3=17`; upper `w'=(-3,1)` gives `w'(1,1)=-2` and
`8+12-(-2)=22`. The sign of the identity is opposite to the upper-face
identity `E = t^{22} J`, because the Jacobian chart factor `tau^{-4}`
together with the two Euler identities for `tau^{±8}`, `tau^{±12}` produce
an overall minus.

Writing `F = sum F_n(xi) tau^n`, `G = sum G_n(xi) tau^n` and collecting
`tau^n` in `Etil` is the D5G recurrence with the same `(12-j)` and `(i-8)`:

```text
Dtil_n = sum_{i+j=n} [ (12-j) F_i' G_j + (i-8) F_i G_j' ].
```

For a Keller pair, `Dtil_n = 0` for `n ≠ 17` and `Dtil_17 = -1`.

Independent exact checks, not the producer’s random-Laurent flag:

- the identity `Etil + tau^{17} J_{x,y} = 0` on the Keller pair `(x,y)`, on
  sparse polynomials, and on eight random Laurent pairs;
- the matching upper identity `E - t^{22} J_{x,y} = 0` on the same sample;
- the recurrence against the literal expansion of `Etil`, summing over all
  integer tau-weights (the lattice case is the sub-sum `n ≥ 0`).

The first displayed formula of the ideation §3.2 (the `tau^{-21}` block)
and the executive-summary form `Etil = -tau^{17} J` are the same identity.
No sign or exponent repair is required.

---

## 2. Windows, census, handles, square/cube, pinning — GAP/REPAIR

### 2.1 Windows and census — CONFIRMED

The chart sends `x^i y^j` in `f` to `tau^{8-4i+j} xi^i`, so
`nu_F = 8-4i+j`. Likewise `nu_G = 12-4i+j`. Intersecting with the D3
inequalities yields exactly the advertised windows

```text
F_nu :  max(0, ceil((8-nu)/4))  ≤ i ≤ 16-nu,
G_nu :  max(0, ceil((12-nu)/4)) ≤ i ≤ 24-nu,
```

empty when the lower bound exceeds the upper bound. Direct lattice
enumeration of `2S` and `3S` agrees with the windows as sets, for every
`nu`, and recounts D3’s census to the digit:

```text
# 2S = 141,   # 3S = 301,   total 442.
```

The `(4,-1)` face itself is `nu=0`: 15 points of `2S` (`i=2..16`) and
22 points of `3S` (`i=3..24`). Both faces are saturated in the polygon
(the windows are nonempty).

### 2.2 Handles — CONFIRMED, with a tail the ideation suppresses

```text
F_17 = empty,
G_17 = degrees 0..7   (8 slots).
```

The target row is linear in `G_17` plus bilinear mixed terms from
`i+j=17` with `1 ≤ i ≤ 16`. That is a genuine linear handle, unlike
`D_22` where both windows are empty.

What the ideation does not record: the lower grading does **not** stop at
17. Lattice support continues to

```text
max nu_F = 16,   max nu_G = 24,
G_18..G_24 : 7+6+5+4+3+2+1 = 28 slots,
first n with both windows empty : 25,
max possible Dtil degree : 16+24 = 40.
```

The identity `Etil = -tau^{17}` therefore imposes `Dtil_n=0` for every
`n ≠ 17` in `0..40`, not merely `n=0..16`. This is used in item 7.

### 2.3 Square/cube — CONFIRMED as a `Dtil_0` identity, not as a polygon identity

On `nu=0`,

```text
Dtil_0 = 12 F_0' G_0 - 8 F_0 G_0' = 0
```

is `3 (log F_0)' = 2 (log G_0)'`, hence `F_0^3 ∝ G_0^2`. In a UFD of
characteristic zero, `F_0 = alpha K^2`, `G_0 = beta K^3` after absorbing
units. The window `i ≥ 2` on `F_0` forces `xi | K`, so `K = xi · htil`
with `deg htil ≤ 7`. Direct substitution of `K=xi(xi-1)^7` confirms
`Dtil_0=0` identically.

The polygon does **not** force a square/cube leading form: a general
`F_0` in the 15-dimensional window of degrees `2..16` is not a square.
Square/cube is the Jacobian face equation, not the support. The wording
“exactly saturated by the frozen face: … precisely `xi^2 htil^2` with
`deg htil=7`” conflates the 15-dimensional window with the 8-dimensional
family of squares. Degree 7 is the maximum the window permits, attained
by the fibre-tagged control, not forced by D3.

### 2.4 What the GGV chain actually forces — GAP/REPAIR

Three different polynomials are in play. Independent expansion:

| polynomial | `(4,-1)` face of `f` | upper face `j-3i=8` of `f` | `F_0` in the upper chart |
|---|---|---|---|
| fibre-tagged native `f=B^2-x-y^8` | `B^2` (15 terms) | `(16,56)` and `(0,8)` | `X^{16}-1` |
| D3/R5 artificial `f=B^2-2x^8 y^{32}+y^8` | `B^2` | `(16,56)`, `(8,32)`, `(0,8)` | `(X^8-1)^2` |
| producer’s “control” `f=B^2` | `B^2` | only `(16,56)` | `X^{16}` |

The ideation §B2 and §0 quote `f=B^2=x^2(xy^4-1)^{14}` as “the frozen
`8_28` control” and conclude that the genuine upper face is the monomial
`H=X^8`, `delta=8`. That polynomial is not the frozen control. The
fibre-tagged native pair, which is the object whose `(4,-1)` faces are
`B^2`/`B^3` with `gamma=7`, has upper face `X^{16}-1`, which is **not a
square**. The D3/R5 object with `F_0=(X^8-1)^2` is the campaign’s own
artificial completion of the `y`-edge, already labelled as such.

What the frozen chain *does* force, for a one-place GGV realisation:

- Newton polygon `S=conv{(0,0),(1,0),(8,28),(0,4)}`, hence the two
  extremal edges of `2S`/`3S`;
- a `(4,-1)` step with residual multiplicity `gamma=7` at a **single**
  characteristic root, for members that actually arise from that chain.

What it does **not** force, on the D3 raw lattice:

- `K=xi(xi-rho)^7` rather than a general degree-8 polynomial with
  `xi | K` (multiple residual roots remain lattice-legal);
- the artificial upper-face `H=X^8-1`;
- emptiness of the genuine upper face.

Card B is the right question. The executive summary answers it in the
success tense. That is the repair: keep Card B as a read, and stop
calling `K=xi(xi-1)^7` a theorem of the chain.

---

## 3. General face-endpoint formula — GAP/REPAIR

On the unshifted square/cube edge `F_0=c K^2`, `G_0=c' K^3`, with a
perturbation `G_N=d`, `F_N=0` and with all mixed terms from weights
`1..N-1` set to zero, the `N`-row is

```text
(12-N) F_0' d - 8 F_0 d' = -8c K^{2+q} (K^{-q} d)',    q=(12-N)/4.
```

Setting this equal to the inhomogeneous target produces exactness of

```text
K^{(N-8-12)/m} dxi = K^{-w(1,1)/m} dxi,    m=4,
```

as an identity of first-order ODEs. For the two faces this specialises
to `K^{+1/2} dX` and `K^{-3/4} dxi`, matching the numerology of R5 and
of the lower ODE in item 4. That calculation is confirmed, and the
numerator `N-a-b=-w(1,1)` is invariant under the shift
`(a,b)=(8-nu_f, 12-nu_g)`.

It is **not** a theorem that the weight-`N` endpoint is rationally
solvable if and only if that class vanishes, in the generality
advertised. Hidden hypotheses, each independently load-bearing:

1. **Unshifted square/cube.** `F_0=c K^{a/m}`, `G_0=c' K^{b/m}` with
   `(a,b,m)=(8,12,4)`. If `F_0=0` or `G_0=0`, `m=gcd(8-nu_f,12-nu_g)`
   changes and the actual exponent `-w(1,1)/m` changes. The finite
   shifted list `nu_f+nu_g ≤ 17` is not enumerated (the ideation
   records this). Negative `a` or `b` is not a polynomial leading form.

2. **`F_N=0`.** Used to drop the `F_N` pairing. True at `N=17` on the
   raw lower windows; true at `N=22` on the raw upper windows. Not an
   identity of the operator.

3. **Mode subtraction / vanishing mixed terms.** The identity omits
   `sum_{i=1}^{N-1} pair(F_i,G_{N-i})`. R5’s theorem at `N=22` includes
   a mode-completeness proof that this remainder can be subtracted in
   `K(X)[[t]]`. Instantiating at `N=17` requires a new such proof. The
   ideation names this as Card A’s first dependency; it is still a gap.
   On the *raw* lattice the mixed terms are polynomial and need not lie
   in the rational mode span.

4. **Rationality, not cover-exactness.** Exactness of
   `K^{-w(1,1)/m} dxi` on `y^m=K` is necessary for a primitive in the
   function field of the cover. The residual `d` is required to lie in
   a specific `K(xi)`-line (here `d ∈ K^{-q} K(xi)`). An arbitrary
   meromorphic primitive on the cover does not produce a rational `d`.
   This is the same repair the 1349Z Grok review already demanded of
   the author’s `(alpha,beta,N)` slogan.

5. **Primitive cover.** `y^4=K` is not primitive when
   `gcd(4,e_i,deg K)>1`. The relevant component must be taken. The
   ideation’s “`4 | e_1` makes the cover reducible with
   `K^{-3/4}` rational and nonzero residues” is the right idea for
   fourth powers, but it does not cover the semi-primitive case
   `e_i ≡ 2 (mod 4)` (e.g. `[2,2]`, which *is* ODE-solvable; see
   item 4).

6. **Constants and normalisation.** `c`, `alpha`, `beta` in `K^*`; the
   inhomogeneous scale is fixed by `D_N=-1`, not merely by exactness
   of a class. Characteristic zero (or at least `2,3` invertible, and
   `4r-3 deg K ≠ 0` when that coefficient is used).

7. **Base field.** The ODE is over `K(xi)` for a characteristic-zero
   field `K`. The multiplicity classification is stated over an
   algebraic closure. Over `Q`, a two-root polynomial need not split;
   `rho=1` is a normalisation of the control, not of the farm.

8. **`m`.** Executive summary `m=gcd(w(f),w(g))` agrees with
   `m=gcd(a,b)` only on the unshifted face. After a shift they can
   differ.

The formula is the 1349Z identity `v' = -1/(beta F_0^{(alpha+beta-N)/beta})`
with `(alpha,beta,N)=(12,8,17)` and with the Newton packaging
`-w(1,1)/m`. Packaging is not a new existence theorem. Maximum
promotable content: the unmixed unshifted ODE, with the eight hypotheses
above listed as premises, not as corollaries.

---

## 4. Lower-face ODE, poles, degrees, classification — GAP/REPAIR

### 4.1 The ODE — CONFIRMED

At `N=17`, `q=-5/4`, with `c=1` and `g := 8 K^2 d`,

```text
(12-17) F_0' d - 8 F_0 d' = -1
```

is exactly

```text
4 K g' - 3 K' g = 4 K,
```

equivalently `(K^{-3/4} g)' = K^{-3/4}`. Direct substitution confirms
the two forms.

### 4.2 Rational poles are impossible — CONFIRMED (valuation bookkeeping repaired)

Let `v_p(K)=e ≥ 1` and `v_p(g)=mu`. In the divided form
`g'-(3/4)(K'/K)g=1` one has `v(K'/K)=-1` and leading coefficient
`mu-3e/4` on the left. This vanishes only at `mu=3e/4`. For a pole,
`mu ≤ -1`, so `3e/4 < 0` is impossible. Hence `v(LHS)=mu-1 < 0 = v(RHS)`.
The ideation’s display `v(LHS)=mu-1 < 0=v(RHS)` silently uses the
divided equation and writes `v(4K)=0`; the unrepaired form
`4Kg'-3K'g=4K` has `v(RHS)=e` and `v(LHS)=e+mu-1`, which still
contradicts `mu ≤ -1`. After that repair, `g` is a polynomial.

Independent confirmation: the linear systems for `g=u/K^k` with
`k=1,2,3` and `deg u ≤ 19` (resp. 23) on `K=X^8-1` and on
`K=X^4(X-1)^4` are inconsistent, matching the ideation’s check 8.

### 4.3 Degree alternatives — CONFIRMED

Let `D=deg K`, `r=deg g`. Leading coefficient of the left side is
`(4r-3D) lc(K) lc(g)` at degree `r+D-1`. The right side has degree `D`.

- If `4r ≠ 3D`, then `r+D-1=D`, so `r=1`.
- If `4r=3D`, then `r=3D/4` and `4 | D`; leading terms cancel.

No other degrees are possible. For `D=8` this is `{1,6}`, as advertised.
The ideation’s wording “`r ∈ {1,6}` exactly” is the `D=8` case, not a
law for general `D`. For general `D` the second slot exists only when
`4 | D`, and even then it is a candidate degree, not an automatic
solution.

### 4.4 Multiplicity classification — GAP/REPAIR

Independent exact sweep, all partitions of `deg K ≤ 8`, all two-root
patterns to `deg K ≤ 16`, all partitions of `deg K = 9,10,11,12` with
three or more parts, and the single-residual family
`K=xi(xi-1)^gamma` for `gamma=1..28`:

- agrees with the ideation on every pattern it claimed, including
  `deg K=4: [4],[3,1],[2,2]` and `deg K=8: [8],[7,1],[6,2],[5,3]`;
- `[4,4]` at degree 8 is unsolvable, as claimed;
- three or more distinct roots: no solution through degree 12,
  including the genus-zero pattern `[4,4,1]` at five root-position
  samples;
- `gamma=1..28` solvable if and only if `gamma ∈ {3,7,11,15,19,23,27}`.

No counterexample was found beyond the producer range.

**Necessity of `gamma ≡ 3 (mod 4)` for the two-root shape, as a
theorem.** For `K=c(xi-a)^e (xi-b)^f` with `e,f ≥ 1` and `a ≠ b`, the
linear branch `r=1` never works: translating to `{0,1}` and comparing
coefficients in `4a K - 3(ax+b)K' = 4K` forces `b=0` and then `e=D`,
contradicting two roots. Hence a two-root polynomial solution can exist
only on the cancellation branch `r=3D/4`, which requires `4 | D`. For
the GGV shape `K=xi(xi-rho)^gamma` one has `D=gamma+1` and `e_1=1`, so
`4 | (gamma+1)` i.e. `gamma ≡ 3 (mod 4)`, and automatically
`4 ∤ e_1`. This direction is a proof, not a sample.

**Sufficiency is not a proof.** The cover `y^4=K` has genus

```text
g = 2s - 1 - (sum_i gcd(4,e_i) + gcd(4,D))/2
```

on a primitive (or after reducing by `gcd` of all exponents) model.
Two finite roots with `4 | D` and `4 ∤ e_i` give ramification type
`(1,1,4)` and genus 0, which is consistent with solvability but does
not produce `g`. The ideation’s sketch “genus 0 only with at most two
branch points; with `≥ 3` the form is holomorphic and never exact” is
false as stated: `[4,4,1]` at degree 9 is a three-root genus-0 cover
and is still ODE-unsolvable. Genus 0 is not sufficient, and holomorphy
of `dxi/y^3` is not the obstruction for every three-root pattern.
After stripping fourth powers, two-root types reduce to the three
models `(1,3)`, `(2,2)`, `(3,1)` of degree 4; residue vanishing of the
pulled-back form on the `(1,3)` t-line is elementary, but pushing the
primitive back to a polynomial in `xi` was not completed here as a
uniform algebraic identity. Sufficiency of the closed form, and the
claim “three or more distinct roots: never”, remain computational.

The farm-wide filter `gamma ≡ 3 (mod 4)` is therefore:

- a **necessary** condition on the *unmixed endpoint ODE* for
  corners whose `(4,-1)` face is exactly two-rooted of shape
  `K=xi(xi-rho)^gamma`;
- **not** a jet obstruction (item 5);
- **not** a family obstruction until Card B pins that shape;
- **not** a theorem of sufficiency, though no counterexample
  appeared through `gamma=27`.

`8_28` has `gamma=7 ≡ 3 (mod 4)` and passes the ODE filter. That
sanity check survives, and does not promote the filter.

---

## 5. Control residual `K=xi(xi-1)^7` — CONFIRMED as ODE, not as jet

The displayed polynomial

```text
g = 4 xi - (84/5) xi^2 + (448/15) xi^3 - (1792/65) xi^4
    + (14336/1105) xi^5 - (8192/3315) xi^6
```

satisfies `4Kg'-3K'g=4K` identically over `Q`, and `g(0)=g(1)=0`. The
solution space at degree 6 has no free variables (the homogeneous
kernel `K^{3/4}` is not rational, matching `4 ∤ 5 delta` at weight 17).
Writing `d=g/(8K^2)` and cancelling `xi(xi-1)` once produces a
numerator of degree 4 over the denominator `8 xi (xi-1)^{13}`, as
advertised.

What this **does** imply:

- the unmixed lower-face endpoint ODE is solvable in `Q[xi]` for this
  `K`;
- that polynomial solution is unique;
- the corresponding residual `d` is *not* a polynomial, and in
  particular is not an element of the raw `G_17` window (polynomials
  of degree `≤ 7`).

What this **does not** imply:

- a raw `nu`-jet through row 17, or the impossibility of one;
- vanishing of mixed terms from `Dtil_1,...,Dtil_16`;
- vanishing of `Dtil_18,...,Dtil_40`;
- uniqueness of a raw polynomial solution of the *mixed* row
  `L_17(G_17)+mixed_17=-1`;
- an exclusion of `8_28`.

The polar residual *does* exclude the unmixed truncation
`L_17(G_17)=-1` inside the raw window: the unique rational solution is
not a polynomial of degree `≤ 7`. Mixed terms of degree up to 23 (from
`deg F_0 + deg G_17`) can in principle cancel the polar part. That is
exactly Card A step 3, and it is not done. The ideation’s own firewall
on this point is correct and is hereby retained as a referee condition,
not as optional caution.

---

## 6. History / novelty — GAP/REPAIR

Targeted search, excluding the charged file, its prompt, and the Fable5
peer file. Hits:

| content | status before this ideation |
|---|---|
| `(4,-1)` as a GGV step, `gamma=7`, faces `B^2`/`B^3` | already derived: fibre-tagged prototype; independently re-derived in the pinning hostile review |
| D3 polygons `2S`/`3S`, census 141/301/442, upper chart `n=8+3i-j` | frozen D3 |
| operator `E` and recurrence `(12-j),(i-8)` | frozen D5G / R5 |
| general `(alpha,beta,N)` endpoint ODE and the slogan “one superelliptic criterion per GGV face” | the same author’s 1349Z ideation §3.2; already marked `GAP/REPAIR` by the Grok superelliptic review of that round |
| chart `x=tau^{-4} xi`, `y=tau` | **absent** |
| identity `Etil=-tau^{17} J` | **absent** |
| windows `nu=8-4i+j`, complete lower census, `F_17` empty / `G_17` of size 8 | **absent** |
| ODE `4Kg'-3K'g=4K`, pole lemma, `gamma ≡ 3 (mod 4)` | **absent** |

The second *face of the polygon* is not a discovery: it is the native
`(4,-1)` face the campaign already uses to name `B^2`/`B^3`. The
second *determinant grading* — chart, sign, exponent 17, windows, and
the lower ODE — is genuinely absent from prior artifacts. The “general
face-endpoint theorem” is a Newton re-packaging of a formula this
author already published in the previous round, and that formula was
already refused promotion for primitive-cover, rationality, and
mode-completeness gaps. Those gaps are inherited, not repaired.

Do not award novelty for “the campaign spent its whole GGV effort on
one of two faces” as a geometric sentence. Award novelty only for the
lower-chart identity, the `nu`-census, and the `N=17` ODE analysis.

---

## 7. Strategic claims — REFUTED / GAP/REPAIR

### 7.1 “The upper face is proxy-only because the genuine face is `H=X^8`” — REFUTED

The genuine fibre-tagged control has upper face `X^{16}-1`, two
monomials, `delta` not 8, and is not a square. The monomial computation
`max(j-3i)=8` only at `(16,56)` is a correct computation about `B^2`,
and a false computation about `f`. The campaign’s upper-face programme
*is* scoped to an artificial squarefree replacement `H=X^8-1`; that is
the campaign’s own label, already in D3/R3/R5, and does not need this
argument. The pinning review already recorded that the same replacement
*keeps* the native `(4,-1)` faces and *completes* the `y`-edge to
`(X^8-1)^2`. Claiming that the genuine upper face is the maximally
floppy `b=0` branch is the opposite of the native `F_0=X^{16}-1`, which
R3 explicitly disclaims and which the 1349Z ODE already excludes as an
endpoint (squarefree, `A=1`, `deg B-1=15`).

Whether a *generic* `8_28` lattice member has a free degree-eight
squarefree `H` on the upper edge remains Card B. The control does not
settle it, and the producer’s control computation is on the wrong
polynomial.

### 7.2 “Lower-face pinning follows from the frozen chain” — GAP/REPAIR

For the fibre-tagged polynomial, `in_{(4,-1)}(f)=B^2` and
`in_{(4,-1)}(g)=B^3` with a single residual root of multiplicity 7 is
true, and was already a reviewed identity. For the D3 raw lattice, the
leading form is a 15+22 dimensional window constrained to a square/cube
by `Dtil_0=0`, not to `K=xi(xi-1)^7`. For the GGV one-place family, a
single residual root is part of the chain’s meaning and is the
plausible pinning; it is not a theorem of the frozen `RAW_INPUT.json`
slot list. Card B must distinguish those three objects. The executive
summary does not.

### 7.3 “A reachable target row is a complete face fixture” — REFUTED

Counterexample: the raw pair with `Dtil_0=…=Dtil_16=0` and
`Dtil_17=-1`, and with an arbitrary nonzero `G_24` (the slot `g_0_12`,
raw `y^{12}`, `nu=24`). The identity `Etil=-tau^{17}` fails at
`tau^{24}`. There are 28 live `G`-slots above the target and mixed
rows through degree 40. On the upper face the target `n=22` coincides
with the last possible mixed row of the lattice (`G_22` empty, no
`n>22` slots). That coincidence is special to `w=(-3,1)` and is false
for `w=(4,-1)`.

Card A’s FAIL meaning, as written, is therefore false. A jet through
row 17 is a *truncated* face system. The honest FAIL object is a raw
polynomial pair with `Dtil_n=0` for all `n ≠ 17` in `0..40` and
`Dtil_17=-1`. The honest PASS object is unsatisfiability of that
system, or of any prefix that already includes the tail, inside the
raw windows.

### 7.4 “The compiler is a regrade of the same 442 slots” — GAP/REPAIR

The 442 slots are the same lattice points, and the operator `E` is the
same polynomial. That much is confirmed. The live D5G compiler is not
a face-parameterised machine:

- slot weights in `RAW_INPUT.json` are the upper values `n=8+3i-j`,
  precomputed by D3;
- `compile_d5g.py` loops `for n in range(23)`, hard-codes
  `H=X^8-1`, `F0=H^2`, `G0=H^3`, and emits `D_0..D_22` in the
  `t,X` chart;
- `second_offset=-8` is already a parameter; the face normal is not;
- a cross-grading comparison of `(x,y)`-monomials of `E` is a
  different expansion than D5G’s `t,X` sparse arithmetic.

A correct second-face compiler must (i) recompute `nu=8-4i+j` from
`raw_exponents`, (ii) run through `n=0..40` (or at least through 24),
(iii) replace the artificial `F0,G0` by either the 15+22 dimensional
window or a pinned `K`, (iv) set the inhomogeneous target at 17 with
the minus sign, and (v) treat agreement of two gradings as a
consistency checksum, never as different-model review. That is a
bounded patch, not a `--face 4,-1` flag on the frozen artifact, and
not “zero marginal implementation cost”.

The proposed checksum idea is still a legitimate hostile test of D5G
*if* both expansions are taken in the original `(x,y)` coordinates.
It does not upgrade D5G, and a disagreement quarantines both.

---

## Maximum promotable scope

Promote, as exact identities over a characteristic-zero field, and only
as such:

1. `Etil = -tau^{17} J(f,g)_{x,y}` under `x=tau^{-4} xi`, `y=tau`,
   `F=tau^8 f`, `G=tau^{12} g`, together with the D5G recurrence and
   the Keller specialisation `Dtil_17=-1`.
2. The `(4,-1)` windows, the census `141+301=442`, `F_17=∅`,
   `G_17 = Q[xi]_{≤7}`, and the tail `G_18..G_24`.
3. `Dtil_0=0 ⇒ F_0=alpha K^2`, `G_0=beta K^3` in a UFD, with
   `xi | K` from the window.
4. The unmixed unshifted ODE `4Kg'-3K'g=4K`, polynomiality of `g`,
   the degree law `r=1` or `r=3D/4`, and **necessity** of
   `gamma ≡ 3 (mod 4)` for a two-root face of shape
   `K=xi(xi-rho)^gamma`.
5. The displayed residual of `K=xi(xi-1)^7` as the unique polynomial
   solution of that ODE, with polar `d=g/(8K^2)`.

Do **not** promote:

- the general face-endpoint “theorem” as an iff;
- sufficiency of the multiplicity closed form;
- any farm-wide exclusion, including `gamma ≡ 3 (mod 4)` as a GGV
  filter;
- lower-face pinning of the D3 lattice to `K=xi(xi-1)^7`;
- monomial degeneration of the genuine upper face;
- row-17 reachability as a complete fixture;
- a drop-in `--face` regrade of frozen D5G;
- any `8_28` exclusion, GGV landing, `G2-PSC`, `G2-BD`, or JC2.

Nothing in the charged file contradicts R5 at `N=22`. Nothing in it
licenses R5 at `N=17` without a mode-completeness repair.

---

## Cleanest bounded successor

Do not launch Card A as written. The cheapest honest next object is
the following desk-scale sequence, each step fail-closed.

**S0. Correct the control polynomial.** All lower-face claims about
“the frozen `8_28` control” must use `f=B^2-x-y^8`,
`g=B^3-2x^2 y^2+y^{12}+tau x y^{15}`, or else explicitly name the D3
artificial completion. The `f=B^2` monomial computation is retired.

**S1. Card B, as a read, on three objects separately.** For each of
(native control, D3 artificial, GGV chain/family as in
`lib/families.py:8_28`): is the upper leading form pinned, free, or
not a square? Is the lower leading form pinned to a single residual
root of multiplicity 7, or only to `xi | K`, `deg K ≤ 8`? Output is a
scope annotation, not a freeze.

**S2. A second-face compiler through the live tail, not through 17.**
Recompute `nu` from D3 `raw_exponents`; emit `Dtil_0..Dtil_40` (or
stop at the first `n` whose raw windows and all mixed partners are
empty); target `Dtil_17=-1` and `Dtil_n=0` otherwise. Hard cap: one
D5G-equivalent budget. Cross-grading checksum only in `(x,y)`
coordinates, as consistency, never as review.

**S3. Unmixed linear test, then mixed prefix.** With `F_0=K^2`,
`G_0=K^3` at the S1-pinned `K` (or, if S1 returns free, over the
8-dimensional square family with `xi | K`): decide
`L_17(G_17)=-1` in `Q[xi]_{≤7}` (already no, by item 5), then decide
`L_17(G_17)+mixed_17=-1` after imposing `Dtil_1=…=Dtil_16=0` *and*
the tail `Dtil_18=…=0` inside the raw windows. Stop at the first
unsatisfiable row. Either outcome is a truncated raw-face statement,
still not GGV landing.

**S4. R5 `N`-genericity only if S3 needs a rational-mode span.** If
the raw polynomial system is decided without it, do not re-prove R5
at 17. If S3 is used as a rational uniqueness argument, the
mode-completeness proof is a named lemma with the same scope as R5,
not a corollary of `q=(12-N)/4`.

Rollback: any S2/S3 artifact rolls back with a negative S1 pinning
read, with a cross-grading disagreement, or with a failed `N=17`
mode audit if that audit is invoked. The existing `t`-tower does not
depend on this successor.

---

## Review verdict

**DO NOT PROMOTE `NU17` as specified.** Promote only the chart
identity, the `(4,-1)` census, the unmixed ODE, and the necessity
half of `gamma ≡ 3 (mod 4)`. Repair Card A to include the live tail
`n=18..40`, the correct control polynomial, and Card B as a
prerequisite read. The second grading is a real reindexing of one
equation system; the ideation’s strategic inversion of the two faces
is not.
