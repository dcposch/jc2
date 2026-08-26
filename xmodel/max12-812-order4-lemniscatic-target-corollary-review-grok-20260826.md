# Hostile review — order-four residual Kummer target is lemniscatic

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order4-lemniscatic-target-corollary-20260826.md` |
| Target SHA-256 | `97ace425a5fc0dc03aa12edb2e09f29e3143566b0939d3ce833a3872ee32a07f` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | a nonconstant morphism `P^1_x\to Y` from a relevant loaded order-four source component, which the target correctly refuses to treat as proved |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. No prior `CONFIRMED`/`REPAIR`/`REJECTED` string for this corollary, and no sentence of the target, is an input to a divisor, field, Weierstrass, or differential identity |
| Method | SHA-256 of the target and of the three charged predecessor/review/erratum files; reading of those bytes; independent divisor arithmetic, Kummer field comparison, exact polynomial reduction of (7), exact differentiation of (8), and the short-Weierstrass `j`-formula; no AWS parametrization, no Singular, no source ideal |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` (named target uncommitted) |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is `97ace425a5fc0dc03aa12edb2e09f29e3143566b0939d3ce833a3872ee32a07f`, matching the launch pin. Independently recomputed SHA-256 of every charged predecessor, review, and erratum matches the string printed in the target. Producer status lines and the predecessor review’s overall token were used only as custody of the promoted plane theorem `(g(X),div_X(v),g(Y))`; they are not evidence that (3), (4), (7), or (8) hold. No file other than this review was written.

---

## Verdict

Unconditionally, over `C`, on the complete normalization of the residual Kummer curve `Y: y^4=v`: the charged divisor (1) and a coordinate `t` with `(t(P_ul),t(P_A),t(P_B))=(0,1,\infty)` produce `v=c g^4/(t(t-1))`; `xi=c^{1/4} g/y` identifies the function field of the complete normalization of `Y` with `C(t,xi)/(xi^4-t(t-1))`; `W=2t-1` rewrites that model as `W^2=1+4 xi^4`; the maps (6) and the rational inverse `xi=2 X_E/Z_E`, `W=2 X_E^3/Z_E^2-1` are inverse on a dense chart and extend to an isomorphism of smooth projective genus-one curves with the short Weierstrass model `Z_E^2=X_E^3-16 X_E`, which has `Delta=2^{18}\neq 0` and `j=1728`; and `d X_E/Z_E=-d xi/W` is an identity of rational differentials, the left side being a basis of regular differentials on that complete model.

Conditionally, a nonconstant morphism `P^1_x\to Y` in characteristic zero would pull (8) back to a nonzero regular differential on `P^1`, which is impossible. That source map is not proved here. The loaded order-four leaf, maximum twelve, and JC2 are untouched.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order4-lemniscatic-target-corollary-20260826.md` | `97ace425a5fc0dc03aa12edb2e09f29e3143566b0939d3ce833a3872ee32a07f` | target (matches required pin) |
| `xmodel/max12-812-order4-residual-cusp-kummer-genus1-gate-20260826.md` | `cd6c37c145e325a48dbf382453bde4c727b98a576897d10a1f9b3752ebdd1756` | promoted plane theorem: `g(X)=0`, (1), `Y:y^4=v` geometrically irreducible of degree four, complete normalization of genus one |
| `xmodel/max12-812-order4-residual-cusp-kummer-genus1-review-grok-20260826.md` | `59fb338533ff47a25d00893684caa3076bb7bb7bc2a43ab788cabbc0eb932c6a` | independent `CONFIRMED` of that plane theorem; not a lemma of this corollary |
| `xmodel/max12-812-order4-residual-cusp-kummer-genus1-tangent-erratum-20260826.md` | `26a083fcfa805a52fdb295ceaaf94ae7497047d8545a2323a48a688ac39e2300` | nonmutating tangent-coefficient wording; explicitly changes none of (1) |

Only the explicitly promoted target-curve statements are consumed: `X` is geometrically integral of genus zero, the four places in (1) are distinct, and the complete normalization of `Y:y^4=v` is a geometrically irreducible cyclic degree-four cover of `X` of genus one. Source projection, dominance, primeness of the corrected ideal, `a_6`-saturation, and chart coverage of the coefficient fibre are not inputs and are not conclusions.

---

## Strongest exact theorem that survives

Work over `C`. Let `X` be the normalization of the residual plane of the charged gate, with

```text
g(X)=0,
div_X(v)=8 P_0-P_ul-P_A-6 P_B,
```

the four places distinct. Let `Y: y^4=v`, and let `Y~` be its complete normalization. Then there is a coordinate `t` on `X` with `t(P_ul)=0`, `t(P_A)=1`, `t(P_B)=\infty`, and there exist `g\in C(X)^*` and `c\in C^*` such that `v=c g^4/(t(t-1))`. For any fourth root of `c`, the function `xi=c^{1/4} g/y` satisfies `xi^4=t(t-1)` and induces a `C`-isomorphism of `Y~` with the unique complete smooth model of that `(4,4,2)` Kummer curve. The further change `W=2t-1` and

```text
X_E=2(W+1)/xi^2,     Z_E=4(W+1)/xi^3
```

is an isomorphism of `Y~` with the elliptic curve `Z_E^2=X_E^3-16 X_E`, which is smooth of `j`-invariant `1728`. In particular the geometric isomorphism class of `Y~` over `C` is the unique lemniscatic class and does not retain any coefficient of the residual 18-term plane. The identity `d X_E/Z_E=-d xi/W` exhibits a nonzero regular differential on `Y~`.

If a relevant loaded order-four source component induces a nonconstant morphism `P^1_x\to Y~`, characteristic zero yields a contradiction. No such morphism is proved here.

---

## Attack 1 — divisor subtraction, Picard, and `v=c g^4/(t(t-1))`

**CONFIRMED.** Signs, 4-divisibility, the constant `c`, and the use of `C` all survive.

The charged places `P_0,P_ul,P_A,P_B` are distinct: they are the unique zero of `v`, the primitive upper-left pole, the simple top pole at `q=484/9261`, and the `(2,7)` top cusp at `q=-4/27`. Cross-multiplication gives `484\cdot 27\neq -4\cdot 9261`, and neither `q`-value is `0` or `\infty`. Three distinct points of a genus-zero complete curve over an algebraically closed field may be sent to `0,1,\infty`. Thus a coordinate `t` with

```text
t(P_ul)=0,\qquad t(P_A)=1,\qquad t(P_B)=\infty
```

exists, and is unique. That coordinate is an isomorphism `X\cong P^1_C`, so it has a single simple pole. Consequently

```text
div(t)=P_ul-P_B,\qquad div(t-1)=P_A-P_B,
div(t(t-1))=P_ul+P_A-2 P_B,
div\bigl(1/(t(t-1))\bigr)=-P_ul-P_A+2 P_B.
```

The last line is the target’s displayed divisor of `1/(t(t-1))`. Subtracting it from the charged (1) is

```text
(8 P_0-P_ul-P_A-6 P_B)-(-P_ul-P_A+2 P_B)=8 P_0-8 P_B=4(2 P_0-2 P_B),
```

which is (2). No sign error is available: the `+2 P_B` on the subtracted divisor is what turns `-6 P_B` into `-8 P_B`, and the two simple poles of `v` cancel exactly against the two simple zeros of `t(t-1)`.

`Pic^0(P^1_C)=0`, so every degree-zero divisor is principal. The 4-power in (3) is not this statement alone: it uses that `8 P_0-8 P_B` is four times a degree-zero divisor *as a divisor*, not merely 4-divisible in `Pic`. The divisor `2 P_0-2 P_B` has degree zero, hence equals `div(g)` for some `g\in C(X)^*`. Then `div(g^4)=8 P_0-8 P_B`, and

```text
div\bigl(v\cdot t(t-1)/g^4\bigr)=0.
```

A rational function on a complete curve with empty divisor is a nonzero constant, so `v=c g^4/(t(t-1))` with `c\in C^*`. (Equivalently, if `u` is a local parameter with `div(u)=P_0-P_B`, then `g` may be taken as `u^2` and `c` absorbs the remaining unit.) The same identity with `g` replaced by `lambda g` multiplies `c` by `lambda^{-4}`; existence is unaffected.

Working over `C` is load-bearing for three separate reasons, all of which hold:

1. A smooth proper geometrically integral genus-zero curve over an algebraically closed field is isomorphic to `P^1`, so a global coordinate `t` exists. Over a non-closed field the same `X` could a priori be a conic.
2. Fourth roots of `c` exist in `C^*`. Equivalently `C^*/(C^*)^4=1`, so the Kummer class of `v` equals that of `1/(t(t-1))` rather than a twist `c/(t(t-1))`.
3. The later geometric isomorphism class of elliptic curves is the `j`-line over `C`.

Nothing in this step uses a `Q`-rational parameter, a rational point of `X` over `Q` beyond what the charged places already supply, or any source function.

---

## Attack 2 — `xi=c^{1/4} g/y` is an isomorphism of complete normalized curves

**CONFIRMED.** The identity `xi^4=t(t-1)` is tautological from (3), and the map has degree one on function fields.

On `Y: y^4=v`, choose any fourth root of `c` and set `xi=c^{1/4} g/y`. Then

```text
xi^4=c g^4/y^4=c g^4/v=c g^4\cdot t(t-1)/(c g^4)=t(t-1).
```

This is (4). The four choices of fourth root differ by `mu_4` and induce the deck transformations of the cyclic cover; they determine the same curve (4).

Function fields: `C(X)=C(t)` because `t` is a coordinate on a genus-zero curve. Then `C(Y)=C(t)(y)` with `y^4=c g^4/(t(t-1))` and `g\in C(t)^*`. The displayed formula puts `xi\in C(Y)` and `y=c^{1/4} g/xi\in C(t,xi)`. Thus

```text
C(Y)=C(t,y)=C(t,xi),\qquad xi^4=t(t-1).
```

The extensions `C(t,y)/C(t)` and `C(t,xi)/C(t)` both have degree four: `t(t-1)` has valuations `1,1,-2` at `P_ul,P_A,P_B`, so it is not a fourth power in `C(t)^*`, matching the charged odd valuations of `v` at `P_ul` and `P_A`. Equal function fields of transcendence degree one have a unique complete nonsingular model up to unique isomorphism. Therefore the complete normalization of `Y` is isomorphic over `C` to the complete normalization of the affine model (4), not merely mapped to it with positive degree.

The affine curve `xi^4=t(t-1)` is smooth: `f=xi^4-t(t-1)` has gradient `(4 xi^3,-2t+1)`, and the simultaneous vanishing `xi=0`, `t=1/2` gives `f=1/4\neq 0`. Its plane projective closure is a quartic, hence may be singular at infinity; the isomorphism claimed is of complete normalizations, which the target states.

Ramification of (4) over `P^1_t` is the charged `(4,4,2)` portrait and no other: a place of valuation `n` for the radicand contributes `4-\gcd(4,n)`.

| place | `ord(t(t-1))` | contribution |
|---|---:|---:|
| `t=0` (`P_ul`) | `1` | `3` |
| `t=1` (`P_A`) | `1` | `3` |
| `t=\infty` (`P_B`) | `-2` | `2` |
| `t=t(P_0)` | `0` | `0` |

So `R=8` and `2g-2=4(-2)+8=0`, genus one, independently of the residual coefficients. Distinctness of `P_0` from `{P_ul,P_A,P_B}` is exactly `t(P_0)\notin\{0,1,\infty\}`, so `P_0` contributes no extra ramification and cannot collide with the three branch points. This is the unique cyclic degree-four cover of `P^1` with that ramification portrait up to the already-fixed identification of the three points with `0,1,\infty`: the Kummer class of `t^3(t-1)^3` generates the same subgroup of `C(t)^*/C(t)^{*4}`, while `t^3(t-1)` and `t(t-1)^3` are unramified at infinity and have genus zero.

Zeros of `g` at `P_0` do not change the field: at points above `P_0`, `t(t-1)` is a unit and `y^4=c g^4/(t(t-1))` forces `y` and `g` to vanish to the same order, so `xi` is a unit there.

---

## Attack 3 — birational transformation to `Z_E^2=X_E^3-16 X_E`, inverse, smoothness, `j=1728`

**CONFIRMED.** The forward substitution is an identity on `W^2=1+4 xi^4`; a rational inverse exists on the dense chart `Z_E\neq 0`; the Weierstrass model is smooth of `j`-invariant `1728`.

`W=2t-1` is an affine coordinate change on the base: `t=(W+1)/2`, and

```text
W^2=(2t-1)^2=4t^2-4t+1=4t(t-1)+1=1+4 xi^4,
```

which is (5). The polynomial `W^2-4 xi^4-1` is irreducible in `C(xi)[W]` because `4 xi^4+1` is not a square in `C(xi)`. Affine smoothness: `f=W^2-4 xi^4-1` has gradient `(2W,-16 xi^3)`, and `W=xi=0` gives `f=-1\neq 0`.

On the common dense chart `xi\neq 0` put

```text
X_E=2(W+1)/xi^2,\qquad Z_E=4(W+1)/xi^3.
```

Then `Z_E^2=16(W+1)^2/xi^6` and

```text
X_E^2-16=\bigl(4(W+1)^2-16 xi^4\bigr)/xi^4.
```

The relation `W^2-1=4 xi^4` rewrites the numerator as

```text
4(W+1)^2-4(W-1)(W+1)=4(W+1)\bigl((W+1)-(W-1)\bigr)=8(W+1),
```

so

```text
X_E(X_E^2-16)=\bigl(2(W+1)/xi^2\bigr)\cdot\bigl(8(W+1)/xi^4\bigr)=16(W+1)^2/xi^6=Z_E^2.
```

Equivalently, as polynomials, `8(W+1)^3-32(W+1)xi^4-16(W+1)^2` reduces to the zero polynomial under `W^2\mapsto 1+4 xi^4`. This is (7). (The same reduction is the identity `8(W^2-4 xi^4-1)=0` after cancelling a factor `W+1`.)

Forward (6) is undefined as written at `xi=0`. On the curve, `xi=0` forces `W=\pm 1`. The branch `W\to-1` has `t\to 0` and `W+1\sim-2 xi^4`, hence `X_E\to 0`, `Z_E\to 0`, filling the 2-torsion point `(0,0)`. The branch `W\to+1` has `t\to 1` and `X_E\sim 4/xi^2\to\infty`, filling the point at infinity of the Weierstrass model. At `xi\to\infty`, `W\sim\pm 2 xi^2` fills the remaining 2-torsion points `(4,0)` and `(-4,0)`. Thus (6) extends to a morphism of complete models.

Rational inverse on the dense chart `Z_E\neq 0`:

```text
xi=2 X_E/Z_E,
W=X_E\cdot xi^2/2-1=2 X_E^3/Z_E^2-1=(X_E^2+16)/(X_E^2-16).
```

The first line is identical to `xi` wherever `W+1\neq 0` and `xi\neq 0`. The second is identical to `W` wherever `xi\neq 0`. On the Weierstrass curve `Z_E^2=X_E(X_E^2-16)` one has

```text
1+4 xi^4=1+64 X_E^2/(X_E^2-16)^2=(X_E^2+16)^2/(X_E^2-16)^2=W^2,
```

so the inverse lands on (5). At `(0,0)` the expression `2X_E/Z_E` has a removable singularity: `Z_E^2=-16 X_E+X_E^3` gives `X_E=-Z_E^2/16+\cdots` and `2X_E/Z_E=-Z_E/8+\cdots\to 0`. At `(4,0)` and `(-4,0)` it has a pole, corresponding to `xi=\infty`. So the two rational maps are inverse on dense opens, hence birational. Smooth proper models of a genus-one function field are unique up to isomorphism, so the maps complete to an isomorphism `Y~\cong E`, where `E` is the projective closure of (7).

Smoothness of (7): `2 Z_E=0` and `3 X_E^2-16=0` on the curve would require `X_E\in\{0,\pm 4\}` and `3 X_E^2-16\in\{-16,32,32\}`, none of which is zero. The discriminant of `Z^2=X^3+A X+B` with `A=-16`, `B=0` is

```text
Delta=-16\bigl(4 A^3+27 B^2\bigr)=-16\cdot 4\cdot(-4096)=262144=2^{18}\neq 0.
```

The point at infinity is therefore regular as well. The `c_4`-invariant is `-48 A=768`, and

```text
j=c_4^3/Delta=768^3/2^{18}=(2^8\cdot 3)^3/2^{18}=2^6\cdot 27=1728.
```

Any short Weierstrass curve with `B=0` and `A\neq 0` has `j=1728`; the specific `A=-16` is a convenient integral model, not a coefficient of the residual plane. Over `C` there is a unique elliptic curve with this `j`-invariant up to isomorphism, the lemniscatic curve with CM by `Z[i]`. The geometric isomorphism class of `Y~` therefore retains none of the 18 residual coefficients.

This is a `C`-isomorphism, not a claim of a model over `Q`. A `Q`-form could a priori be a quadratic twist of `Z^2=X^3-16X`; the target never asserts otherwise.

---

## Attack 4 — independent differentiation of `d X_E/Z_E=-d xi/W`

**CONFIRMED.** The identity is exact, and the left side is a nonzero regular differential on the complete Weierstrass model.

Differentiating (5): `2 W\,dW=16 xi^3\,d xi`, so `dW=8 xi^3\,d xi/W` wherever `W\neq 0`. Differentiating (6),

```text
d X_E=2\bigl(xi^2\,dW-2 xi(W+1)\,d xi\bigr)/xi^4=2\bigl(xi\,dW-2(W+1)\,d xi\bigr)/xi^3.
```

Dividing by `Z_E=4(W+1)/xi^3`,

```text
d X_E/Z_E=\bigl(xi\,dW-2(W+1)\,d xi\bigr)/\bigl(2(W+1)\bigr)
          =\bigl(xi/(2(W+1))\bigr) dW-d xi.
```

Substitute `dW`:

```text
d X_E/Z_E=\bigl(4 xi^4/((W+1)W)\bigr) d xi-d xi.
```

The relation `4 xi^4=W^2-1=(W-1)(W+1)` cancels `W+1` and yields

```text
d X_E/Z_E=\bigl((W-1)/W\bigr) d xi-d xi=-d xi/W,
```

which is (8). The cancellation `W+1` is legitimate on a dense chart: `W+1=0` forces `xi=0` on (5), a finite set. At `W=0` one has `4 xi^4=-1`, so `xi\neq 0`, and `d xi/W=dW/(8 xi^3)` is regular there. The identity of rational differentials therefore holds on the whole function field.

On any short Weierstrass model with `Delta\neq 0`, `dX/Z` is a basis of `H^0(E,Omega^1)`. Locally at the origin of (7), `Z_E^2=-16 X_E+\cdots` gives `d X_E/Z_E=-d Z_E/8+\cdots`, regular and nonvanishing. At the point at infinity, the standard parameter `u=X_E/Z_E` has `X_E=u^{-2}+\cdots`, `Z_E=-u^{-3}+\cdots`, hence `d X_E/Z_E=2\,du`, regular and nonvanishing in characteristic zero. The form is therefore a nonzero regular differential on the complete curve (7). Transport along the isomorphism of Attack 3 makes `-d xi/W` a nonzero regular differential on `Y~`. It is not the zero section of `Omega^1`, and it has no poles.

---

## Attack 5 — characteristic-zero pullback contradiction and source firewall

**CONFIRMED as a conditional statement, with the firewall intact.**

A nonconstant morphism of complete nonsingular curves in characteristic zero is finite and separable: the corresponding function-field extension is a finite extension of fields of characteristic zero, hence separable. Pullback of a nonzero rational differential along a separable morphism is nonzero. In particular, if `f: P^1\to Y~` is nonconstant, then `f^*(d X_E/Z_E)` is a nonzero regular differential on `P^1`. But `H^0(P^1,Omega^1)=0`. This is the same obstruction as the nonexistence of a nonconstant map from `P^1` to a genus-one curve, written on an explicit nowhere-vanishing differential.

The implication requires the source hypothesis that a relevant loaded order-four component induces such an `f`. The target does not prove that hypothesis, and neither does this review. Explicitly refused, because unproved:

- nonconstancy of the rational map from a source component to `Y`;
- dominance of every relevant component onto `Y`;
- nonvanishing of `a_6` on every component (the charged formulae `q=a_5^2/a_6^3`, `y=a_6^2` are a chart);
- primeness of the corrected, `r_7`-saturated source ideal;
- elimination of the loaded order-four leaf;
- maximum twelve;
- JC2.

The weakest still-missing source hypothesis is exactly the first: a relevant component of the loaded order-four source, after whatever saturation is needed to define `(q,y)`, induces a nonconstant morphism from its complete genus-zero deck quotient to `Y~`. Primeness is strictly stronger than required (several components could each map nonconstantly). Nonconstancy of `rho=r_7^4` is not this hypothesis; the charged gate already says so. Exact membership of the cleared substitution in the saturated source ideal is a containment, not dominance.

No broader order-four, maximum-twelve, or JC2 inference is licensed.

---

## Attack 6 — collisions, hidden constants, chart loss, `Q` versus `C`

**CONFIRMED; none of the four named failure modes occurs.**

**Four places.** Distinctness is charged and rechecked by `q`-values in Attack 1. The coordinate conditions `t\in\{0,1,\infty\}` mark precisely `{P_ul,P_A,P_B}`. Distinctness of `P_0` from those three is `t(P_0)\notin\{0,1,\infty\}`, so the zero of `v` does not collide with a branch point of (4) and does not change the Kummer class.

**Hidden constant / fourth power.** The constant `c` is absorbed by choosing `c^{1/4}` over `C`. Over `Q` the same identity would read `v=c g^4/(t(t-1))` with `c` not necessarily a fourth power, and the Kummer extension of `Q(t)` could be a twist `xi^4=c\, t(t-1)` rather than (4). The target works over `C` and never claims a `Q`-isomorphism, so this is not a gap. Replacing `g` by a unit times `g` multiplies `c` by a fourth power and does not change (4). The class of `t(t-1)` in `C(t)^*/C(t)^{*4}` has exact order four because of the odd valuations at `0` and `1`; there is no accidental fourth-power factorization.

**Chart loss.** The `t`-chart places `P_B` at infinity, which is included in the complete curve. Forward (6) is meromorphic of the expected orders and extends to all of `Y~` as recorded in Attack 3. The inverse is regular on `Z_E\neq 0` and extends across the three 2-torsion points. The affine models (4) and (5) are smooth; only the naive plane quartic compactification of (4) or (5) is singular at infinity, and the target compares complete normalizations.

**Rationality over `Q` versus geometric rationality over `C`.** Every existence statement that needs a fourth root, a coordinate sending three geometric points to `0,1,\infty`, or uniqueness of the `j=1728` class is made over `C`. The residual plane is defined over `Q` and the charged places are geometric; the corollary never promotes a rational parameter `t\in Q(X)` or a Weierstrass isomorphism over `Q`. The phrase “no coefficient of the original 18-term plane remains in its geometric isomorphism class” is therefore a statement about `Y~` over `C`, where that class is the single point `j=1728` on the `j`-line.

---

## Scope that is not promoted

This is a target-curve corollary. It identifies the complete normalization of `Y` over `C` with the lemniscatic curve and writes an explicit regular differential. It does not close the source projection gate of the charged genus-one note, does not saturate `a_6`, does not factor the corrected source, and does not empty the loaded order-four leaf.

CONFIRMED
