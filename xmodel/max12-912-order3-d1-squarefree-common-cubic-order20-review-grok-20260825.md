# Hostile different-model review — D1 squarefree common-cubic order-20 obstruction

| Field | Value |
|---|---|
| Target | `xmodel/max12-912-order3-d1-squarefree-common-cubic-order20-obstruction-20260825.md` |
| Target SHA-256 | `1b6e629affdc5a73995e0ab2d7f051ad772d92f75bb61e67362782fcb8f5b4ac` |
| SOURCE_CLOSURE SHA-256 | `a9dca05513f308d3d8685b88b957304b95b7f8fdcc7911417bf347531ac7597a` |
| FREEZE SHA-256 | `05435f25452b7e6148dff1a65f5abb2e203a12a96cbe8ef2877254503bccb4f1` |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation; CAS/Python emission is not a proof of the valuation theorem |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Missing hypothesis | none that affects the squarefree order-20 exclusion |
| Method | source reading and hand derivation; independent monomial/binomial enumeration; independent polynomial check of the double-root identity. AWS firewall stdout was read as a control, not as a substitute for the lemma |

## Verdict

**CONFIRMED**

In the exact ordinary isotrivial chart of the strict D1 coefficient-infinity gate, no formal or Puiseux arc centred on a squarefree depressed cubic can satisfy the eight loaded tail equations. After the moving monic division `E=KQ+R`, the rank-one valuation with `v(Lambda)=1` forces `v(Q)>=6` and `v(R)>=9` on the squarefree residue algebra; through weight 20 the only negative layers are then two proper fractions over `K` and `K^2`; reducing over the moving cubic packages them as `S/K^2` with `deg S<=5`; the first six tails triangulate `S` with unit diagonal; subtracting the exact moving targets `mu Lambda^{15} K + nu Lambda^{18}` kills those six tails through weight 20 and therefore kills `S`; row 8 of this layer is then zero through weight 20, contradicting the unit leading coefficient of `Lambda^{20}(1+tau)`. The argument is uniform in the constants `k,mu,nu` (including every zero-load stratum) and uniform in the strict slope. It uses reducedness of `L[z]/(K_0)`, not irreducibility of `K_0`. It does not cover the double-root point of weighted `P(2,3)`, does not lift that point, and does not bound local thickness.

No identity failed. Exposition looseness in the load-weight sentence and in the quadratic generating function `T_2` is recorded below and does not repair the theorem.

## Strongest exact claim that survives

Work in characteristic zero, in the ordinary isotrivial chart of the charged saturation source:

```text
Lambda = tau^3 rho,     kbar = Lambda^6 k,
r_ell(C, kbar) = Lambda^{12+ell} gamma_ell,
gamma_3=mu,  gamma_6=nu,  gamma_8=1+tau,
gamma_ell=0 otherwise.
```

Let a formal or Puiseux arc have projective common-cubic centre `K_0=z^3+p_0 z+c_0` with `Delta_0=-4 p_0^3-27 c_0^2 != 0`. Then the arc cannot satisfy the eight equations. Equivalently, the squarefree open of the reviewed common-cubic boundary carries no strict D1 coefficient-infinity arc.

If the global strict D1 Rees endpoint is nonunit, algebraic curve selection plus the independently reviewed reduced-support theorem place its projective support inside the single weighted-projective double-root point represented by `(p_0,c_0)=(-3,2)`. This is a set-theoretic containment. It does not assert that the point lies on the endpoint, that it lifts, or that the local ring is reduced.

## Sharpest non-claim

The double-root chart `Delta_0=0`, `(p_0,c_0)!=(0,0)` is open. Identity `(22)` is a negative control, not an arc. No finite jet is asserted on that chart. Local scheme thickness, accessibility of a rational section, finite coefficient load off this strict gate, every other passport, and JC2 remain open. Section 4 of the target (composition Jacobian, leading conic, special branch `(20)`) is reconnaissance and is not used.

---

## Sources actually used

Read in full, hashes verified against `SOURCE_CLOSURE.sha256` and `FREEZE.sha256` before any charged file was trusted:

- `xmodel/max12-912-order3-d1-squarefree-common-cubic-order20-obstruction-20260825.md` (target)
- `xmodel/max12-912-order3-d1-isotrivial-strict-rees-saturation-20260825.md` (ordinary source equations)
- `xmodel/max12-912-order3-d1-weighted-infinity-exceptional-support-review-grok-20260825.md` (common-cubic reduced-support theorem)
- `cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py` (inverse-root and tail convention)
- `cases/max12_912_order3_d1_normal_tangent_20260825/verify_firewall_controls.py` and `aws_box03_v1/firewall_controls.stdout` (triangularity / `z/K^3` / double-root / binomial-weight controls)
- `cases/max12_912_order3_d1_normal_tangent_20260825/README.md`, `PREREGISTRATION.md`

Every `SOURCE_CLOSURE` byte hash matched. `FREEZE.sha256` is the hash of that manifest. AWS `firewall_controls.stderr` is empty. The preserved orientation-failed stderr is a harness negative control (lower-triangular matrix mislabelled as upper-triangular) and is not an identity failure. No producer review was opened. Emitted CAS polynomials from `derive_*.py` were not used as a proof of the valuation table.

Git HEAD at review: `24184c989634b40b00da1bbc3328bcc6ab92fa9b`. Target, closure packet, saturation source, and reduced-support review are uncommitted.

---

## Charge 1 — ordinary fixed-load equations

**CONFIRMED**

The charged saturation theorem writes the unshifted raw descended tails `D_ell` and the compiled rows `R_ell=D_ell-delta_ell` with `delta_3=mu`, `delta_6=nu`, `delta_8=1`. Character descent plus the étale coordinate `t` with `s=t^3`, `tau=t-1`, `q=t^3-1=tau u(tau)` and `u(0)=3` a unit converts the strict Rees chart `Lambda=q^3 rho` into the ordinary chart

```text
Lambda = tau^3 rho_t,     kbar = Lambda^6 k = tau^{18} rho_t^6 k,
r_ell(C, kbar) - Lambda^{12+ell} gamma_ell(tau) = 0,
gamma_3=mu,  gamma_6=nu,  gamma_8=1+tau.
```

The identity `gamma_8=t=1+tau` and the absence of an extra `t` factor on rows 3 and 6 are in the source, not an approximation. Sign convention: the independent reconstruction defines `r_ell = -[w^{-ell}] g(z(w))` with `g=F_{12}(f)+k F_6(f)` and `f(z(w))=w^9`. The fibre equations are `r_ell=gamma_ell` before Rees scaling and `r_ell=Lambda^{12+ell} gamma_ell` after it. A global sign flip of every tail would replace the row-8 leading coefficient by `-1`, still a unit; the obstruction is nonvanishing, not the displayed sign of `1`. The reconstruction's sign is the one used in `(1)`.

Weights. Row `ell` is homogeneous of weight `12+ell` when `wt(A_i)=9-i` and `wt(k)=6`. Consequently:

- `kbar=Lambda^6 k` has coordinate weight 6,
- the row-3 load is `mu Lambda^{15}`,
- the row-6 load is `nu Lambda^{18}`,
- the row-8 load is `Lambda^{20}(1+tau)`.

Meaning of the constants. The symbols `k,mu,nu` lie in the coefficient field (or are kept in the coefficient ring for a uniform statement). They are not series in `tau`. Zero-load strata are included:

- `k=0` makes `kbar` identically zero, not merely of valuation `>=6`;
- `mu=0` makes the row-3 target the zero series;
- `nu=0` makes the row-6 target the zero series;
- row 8 is independent of `k,mu,nu`. Because `v(tau)>0`, one has `v(1+tau)=0` with leading coefficient `1`, so the weight-20 initial form of row 8 is exactly `1`.

No step divides by `k`, `mu`, or `nu`. Vanishing of a load only deletes a target or a `kbar` summand and cannot create a row-8 leading term.

Slope uniformity. A strict rational or Puiseux slope is a rank-one valuation with `v(Lambda)>3 v(tau)` (equivalently both `tau` and `rho` vanish on the boundary and are nonzero at the generic point of the arc). Normalising `v(Lambda)=1` rescales the value group; inequalities among valuations are unchanged. The proof never uses a numerical slope `m/n`, only `v(Lambda)=1` and `v(tau)>0`. Formal series in `tau` with integer values are included by taking `v(Lambda)=3+v(rho)` and clearing the denominator; Puiseux series are included by allowing `Q`-valued valuations. Finite constant-field extensions do not change a divisibility in `L[z]`.

---

## Charge 2 — moving depressed cubic, exact division, binomial layers

**CONFIRMED**

The source polynomials are already depressed (no `z^8`). Along the arc write `f=z^9+a_7 z^7+a_6 z^6+cdots`. The moving cubic `K=z^3+p z+c` is the unique depressed monic cubic with `3p=a_7` and `3c=a_6`. Characteristic zero makes this an isomorphism on those two coefficients. Then `E:=f-K^3` has degree at most 5, identically in the moving `p,c`.

`K` is monic of degree 3 over the valuation ring. Polynomial division of `E` by `K` is therefore an exact coordinate change over that ring: `E=KQ+R` with `deg Q<=2`, `deg R<=2`, and no denominator. Six coefficients of `E` match six coefficients of `(Q,R)`. Motion of `p,c` moves `K` and therefore moves the division; it does not introduce poles.

Binomial expansion at infinity. Put `x=E/K^3`. At `z=infinity` one has `E=O(z^5)` and `K~z^3`, so `x=O(z^{-4})` vanishes, and the binomial series of `(1+x)^{4/3}` and `(1+x)^{2/3}` are valid as Laurent series in `z^{-1}`. Along the arc `E` has positive valuation, so the same series is valid Lambda-adically. Expanding:

```text
(1+x)^{4/3}
  = 1 + (4/3)x + (2/9)x^2 - (4/81)x^3 + (5/243)x^4 + ...,
(1+x)^{2/3}
  = 1 + (2/3)x - (1/9)x^2 + (4/81)x^3 + ....
```

Hence

```text
f^{4/3} = K^4 + (4/3) K E + (2/9) K^{-2} E^2 - (4/81) K^{-5} E^3 + ...,
f^{2/3} = K^2 + (2/3) K^{-1} E - (1/9) K^{-4} E^2 + ...,
```

which is `(4)` of the target. The Faber polynomials are the nonnegative parts in `z`. The linear pieces `(4/3)KE` and `kbar K^2` are polynomials (`deg E<=5`), as is `(2/3)kbar Q` coming from `(2/3)kbar K^{-1}(KQ)`. Thus the ordinary tail map has zero differential at `E=kbar=0`. That fact explains why a quadratic (or higher) calculation is required; it is not itself the obstruction.

Negative quadratic terms. Substitute `E=KQ+R`. Then `E^2=K^2 Q^2+2K QR+R^2`, and the only non-polynomial summands of valuation two in `(E,kbar)` are

```text
(4/9) (QR)/K + (2/9) R^2/K^2 + (2/3) kbar R/K.
```

The strictly negative Laurent part of `(QR)/K` is `rem_K(QR)/K`, which is `(5)`. The cubic layer `Q^3/K^2` is not in `T_2`; it is the `j=3`, `r=0` term of `f^{4/3}` and is charged separately in the valuation table. Treating `T_2` as a complete generating function for the lemma would be a misreading; the lemma's displayed candidates are `(9)`, not `(5)`.

Two inverses. Let `z_0` be the unique Laurent series `z_0=w+O(w^{-1})` with `K(z_0(w))=w^3`. Let `z` be the unique series `z=w+O(w^{-1})` with `f(z(w))=w^9`. These agree if and only if `E=0`. Linearising `K(z)^3+E(z)=K(z_0)^3` gives

```text
3 K(z_0)^2 K'(z_0) (z-z_0) = -E(z) + higher.
```

Here `K'(z_0)=3z_0^2+p=3w^2+O(1)` and `K(z_0)=w^3`, so `3K^2 K'=9w^8+O(w^6)` has leading coefficient `9`, a unit. After the valuation lemma one has `v(E)>=6`, hence the coefficient valuation of `z-z_0` is at least 6. The valuation lemma itself is a statement about leading forms of Laurent polynomials in `z` modulo `K_0`; it does not require `z`. Substituting `z` for `z_0` into a layer of valuation at least 15 therefore changes coefficients only at valuation at least 21, which is Charge 5.

---

## Charge 3 — valuation lemma, line by line

**CONFIRMED; `beta>=6` and then `alpha>=9`**

Normalise `v(Lambda)=1`. Set `beta=v(Q)` and `alpha=v(R)` as minima of coefficient valuations. Both are strictly positive: the arc is centred at `f=K_0^3`, so `E` vanishes at the special point, and `(Q,R)` are exact coordinates of `E`. If `Q` (resp. `R`) is identically zero the corresponding valuation is `+infty` and the inequalities are easier.

Write `x=Q/K^2+R/K^3`. The negative terms of `f^{4/3}` are the summands with `2j+r>4` in

```text
binom(4/3,j) binom(j,r) Q^{j-r} R^r K^{4-2j-r},
```

and those of `kbar f^{2/3}` are the summands with `2j+r>2` in

```text
kbar binom(2/3,j) binom(j,r) Q^{j-r} R^r K^{2-2j-r}.
```

If `k=0` the second family is absent. If `k!=0` then `v(kbar)=6` exactly, so every `kbar` term occurs at least six units after the corresponding pure `(Q,R)` monomial.

### Exhaustiveness of the three candidates

The three displayed leading valuations are `beta+alpha` from `QR/K`, `2alpha` from `R^2/K^2`, and `3beta` from `Q^3/K^2`. No other negative monomial can be first when `beta<6`:

- `Q^2 R/K^3` has weight `2beta+alpha`. This is strictly larger than `beta+alpha`. It is `<= 2alpha` iff `alpha>=2beta`, and `<= 3beta` iff `alpha<=beta`. Those cannot hold together for `beta>0`. So this term is never first.
- `Q^4/K^4` has weight `4beta>3beta`.
- `R^3/K^5` has weight `3alpha>2alpha`.
- `kbar R/K` has weight `>=6+alpha`. Compared with `QR/K` this is strictly later when `beta<6`. (If `Q=0` identically then `beta=+infty`, which is not the case `beta<6`.)
- `kbar Q^2/K^2` has weight `>=6+2beta`. Compared with `Q^3/K^2` this is strictly later when `beta<6`.

Higher `j` only increases the `Q,R` weight and the denominator power. The three-candidate list is exhaustive for the first negative valuation.

A zero target means the displayed numerator is divisible by the displayed denominator as a polynomial (no negative Laurent part). If that first valuation equals 15, the row-3 target is a scalar multiple of `K` after placing the layer over `K^2`; it vanishes in `L[z]/(K_0)`. Valuation 18 is a scalar over `K^2` and likewise vanishes modulo `K_0`. Valuation 20 cannot be first in the range `beta<6`: the first valuation is at most `min(beta+alpha,2alpha,3beta)<18` once `beta<6` and `alpha>0` (if `3beta>=18` then `beta>=6`). So a weight-20 coincidence never rescues the case `beta<6`.

Corrections from a vanished `QR/K` layer: if `Q_0 R_0` is already `0` in `L[z]/(K_0)`, then `rem_{K_0}(Q_0 R_0)=0` and the leading negative part of `QR/K` is zero. A later jet of `Q` or `R` can meet `R^2` or `Q^3` at equal valuation. Placing a term over denominator `K` onto the common denominator `K^2` multiplies its numerator by `K`, so the correction vanishes in `L[z]/(K_0)`. Every "then `R_0^2=0`" or "then `Q_0^3=0`" step below is therefore stable under such corrections. This is the only place a vanished layer could have re-entered, and it cannot.

### The seven ranges, with `beta<6`

Write `Q=Lambda^{beta} Q_0+...` and `R=Lambda^{alpha} R_0+...` with residue polynomials of degree at most two, not both leading polynomials zero.

**`alpha<beta`.** First valuation `2alpha` from `R^2/K^2`. Next candidates `beta+alpha` and `3beta` are strictly larger. Required congruence: `R_0^2=0` in `L[z]/(K_0)`. Squarefreeness gives `R_0=0` at every root of `K_0`, hence `K_0` divides `R_0`, impossible by degree.

**`alpha=beta`.** First valuations `beta+alpha=2alpha` coincide; `3beta=3alpha>2alpha`. Combined numerator over `K^2`:

```text
(4/9) K Q R + (2/9) R^2 = (2/9) R (2 K Q + R).
```

The congruence is `R_0(2 Q_0 K_0+R_0)=0`. Reducing modulo `K_0` yields `R_0^2=0`, the same obstruction.

**`beta<alpha<3beta/2`.** Order: `beta+alpha < 2alpha < 3beta`. First: `Q_0 R_0=0` in the residue algebra. This may be mixed vanishing (different factors at different roots). After that layer is killed, next is `R_0^2=0`, which forces `R_0=0` at every root and contradicts degree. Mixed vanishing does not survive the second equation.

**`alpha=3beta/2`.** First: `QR/K` at `5beta/2`. Then `R^2/K^2` and `Q^3/K^2` together at `3beta`. Coefficients of the second layer, after the `QR` leading term is gone:

```text
(2/9) R^2 - (4/81) Q^3 = (1/81)(18 R^2 - 4 Q^3)
```

over `K^2`. At each root of `K_0` one has `Q_0 R_0=0` and `18 R_0^2=4 Q_0^3`. In each field factor: if `R_0!=0` then `Q_0=0` and `18 R_0^2=0`, hence `R_0=0`; if `Q_0!=0` then `R_0=0` and `-4 Q_0^3=0`, hence `Q_0=0`. Both residue polynomials vanish at all three roots. The target coincidence `5beta/2=15` forces `beta=6`, outside this case. The coincidence `3beta=15` makes the second layer a row-3 target, which still vanishes modulo `K_0` and yields the same pair of residue equations.

**`3beta/2<alpha<2beta`.** Order: `beta+alpha < 3beta < 2alpha`. First `Q_0 R_0=0`, then `Q_0^3=0`, hence `K_0` divides `Q_0`. Apparent target coincidence: `beta+alpha=15` forces `5<beta<6`, after which `Q^3/K^2` has valuation strictly between 15 and 18 and is not a target, so `Q_0^3=0` still. The coincidences `3beta=15` reduce modulo `K_0` to `Q_0^3=0` and are equally impossible. Weight 18 is at least `3beta>15` and, in this open range with `beta<6`, is strictly larger than the `Q^3` layer already contradicted.

**`alpha=2beta`.** First valuations `beta+alpha=3beta` coincide. Combined numerator:

```text
(4/9) QR/K - (4/81) Q^3/K^2 = (4/81) Q (9 K R - Q^2) / K^2.
```

Reducing modulo `K_0` gives `Q_0^3=0`. This is precisely the identity that can hold without `Q_0=0` when `K_0` is non-reduced; on the squarefree chart it cannot. Charge 8 records the explicit cancellation.

**`alpha>2beta`.** First valuation `3beta` from `Q^3/K^2`, so `Q_0^3=0`.

All seven rows contradict degree on a squarefree cubic. This proves `beta>=6`.

### The second inequality `alpha<9`

Now `beta>=6` and suppose `alpha<9`, so `2alpha<18`. The only term over denominator `K_0^2` whose residue modulo `K_0` can be nonzero at valuation `2alpha` is `R_0^2`: `Q^3/K^2` has valuation `3beta>=18`, and `kbar Q^2/K^2` has valuation `>=18`. Any simultaneous term over denominator `K_0` (`QR/K` or `kbar R/K`) acquires a factor of `K_0` after being written over `K_0^2`. A possible valuation-15 target is a scalar multiple of `K_0` and vanishes modulo `K_0`. Therefore `R_0^2=0` in `L[z]/(K_0)`, hence `K_0` divides `R_0`, impossible by degree.

If `alpha<6` the first term is already `R^2` at `2alpha<12`, not a target. If `alpha=6` the `QR` and `kbar R` layers can meet `R^2` at weight 12, still not a target, and the residue is still `R_0^2`. If `6<alpha<9` the `QR` layer may precede `R^2`; it is either a zero target or a weight-15 target, both `0` modulo `K_0`, and the subsequent `R^2` layer at `2alpha in (12,18)` is then a zero target except at the measure-zero meeting `2alpha=15` (`alpha=7.5`), where the combined residue is again `R_0^2`. No weight-20 term is involved.

This proves `(8)`. The argument never uses a generic numerical value of a load, and it never uses irreducibility of `K_0`.

---

## Charge 4 — every use of squarefreeness

**CONFIRMED; squarefree is necessary and is not replaced by irreducible**

The residue algebra `A=L[z]/(K_0)` is reduced if and only if `K_0` is squarefree. After a finite splitting extension, `A` is a product of three fields, one for each simple root. Every displayed product equation is checked componentwise in those fields. Passing to the extension does not change whether a monic cubic divides a degree-at-most-two polynomial defined over `L`.

Uses, and nothing else:

1. Nilpotent-free division. In a product of fields, `X^n=0` implies `X=0`. This is the step `R_0^2=0 => R_0=0` and `Q_0^3=0 => Q_0=0`. It fails the moment `A` has a nilpotent, which is exactly `Delta_0=0`.
2. Degree at most two. A nonzero polynomial of degree `<=2` cannot vanish at three distinct points, equivalently cannot be divisible by a monic cubic. This uses three distinct roots, i.e. squarefreeness, not irreducibility. A split cubic `z(z-1)(z+1)` is allowed and is covered. An irreducible squarefree cubic is also covered: `A` is then already a field, and the same nilpotent-free implication holds in one factor instead of three. Using only irreducibility would *exclude* the split open, which is a weaker theorem and is not what the target claims.
3. Mixed vanishing of products. `Q_0 R_0=0` in `A` means that at each root, at least one factor vanishes. The factors may vanish at different roots. A second equation (`R_0^2=0`, or `18 R_0^2=4 Q_0^3`, or `Q_0^3=0`) then forces both factors to vanish at every root. Componentwise checking is essential: one cannot conclude `Q_0=0` or `R_0=0` as polynomials from `Q_0 R_0=0` alone.

No step replaces `K_0` by an irreducible. No step divides by `Delta_0` in a coefficient ring; `Delta_0!=0` is used only to guarantee reducedness of `A`. The axes `p_0=0`, `c_0!=0` and `c_0=0`, `p_0!=0` are squarefree (`Delta=-27 c_0^2` and `Delta=-4 p_0^3` respectively, nonzero in characteristic zero) and are included.

---

## Charge 5 — negative monomials through weight 20

**CONFIRMED**

Under equality in `(8)` assign weights `(Q,R,kbar)=(6,9,6)`. If any of `beta`, `alpha`, or `v(kbar)` is strictly larger, every weight below only increases, so the equality case is the earliest arrival. The complete negative families are:

F12, weight `6(j-r)+9 r`, denominator power `max(0, 2j+r-4)`:

| j | r | denom | weight |
|---|---|---|---|
| 2 | 1 | 1 | 15 |
| 2 | 2 | 2 | 18 |
| 3 | 0 | 2 | 18 |
| 3 | 1 | 3 | 21 |
| 3 | 2 | 4 | 24 |
| 3 | 3 | 5 | 27 |
| 4 | 0 | 4 | 24 |

and later. kF6, weight `6+6(j-r)+9 r`, denominator power `max(0, 2j+r-2)`:

| j | r | denom | weight |
|---|---|---|---|
| 1 | 1 | 1 | 15 |
| 2 | 0 | 2 | 18 |
| 2 | 1 | 3 | 21 |
| 2 | 2 | 4 | 24 |
| 3 | 0 | 4 | 24 |

Through weight 20 one has exactly five terms, in two layers:

```text
M = (2/9)(2Q + 3 kbar) R / K,                 denom 1, weight 15,
N = (1/81)(18 R^2 - 9 kbar Q^2 - 4 Q^3) / K^2, denom 2, weight 18.
```

Coefficient check. From `f^{4/3}`, `binom(4/3,2)=2/9` produces `(4/9)QR/K+(2/9)R^2/K^2`, and `binom(4/3,3)=-4/81` produces `-(4/81)Q^3/K^2`. From `kbar f^{2/3}`, `binom(2/3,1)=2/3` produces `(2/3)kbar R/K` and `binom(2/3,2)=-1/9` produces `-(1/9)kbar Q^2/K^2`. Summing the `R/K` coefficients: `(4/9)Q+(2/3)kbar=(2/9)(2Q+3kbar)`. Summing the `K^{-2}` numerators over 81 gives `(11)`. These are `(10)` and `(11)`.

Every denominator-power-three term starts at weight 21: the first are `Q^2 R/K^3` (F12, `j=3`, `r=1`) and `kbar Q R/K^3` (kF6, `j=2`, `r=1`). Jets of `Q,R` only raise valuations, so under `(8)` a `K^{-3}` layer cannot appear at weight `<=20`. There is no monomial `Q^a R^b kbar^c` of weight exactly 20 at these leading weights (`6(a+c)+9b=20` has no nonnegative integer solution); weight 20 in `S` can still arise from higher jets (`Q^{(i)} R^{(j)}` has weight `15+i+j`, etc.). That is why the common-numerator argument is required, and why a raw "no weight-20 monomial" slogan would be false.

Inverse substitution through weight 20. After `(8)`, `v(E)>=6` and `v(z-z_0)>=6`. A layer of coefficient valuation at least 15, differentiated in `z` (weight 0) and multiplied by `z-z_0`, has valuation at least 21. Therefore replacing the moving inverse of `K` by the exact inverse of `f` cannot change a coefficient through weight 20. The valuation lemma did not need this comparison; the order-20 tail reading does.

The AWS binomial control reproduces the same five-term list and the same next layer at weight 21. That is a machine check of an enumeration already performed by hand, not a proof of the lemma.

---

## Charge 6 — common numerator, triangularity, `z/K^3` firewall

**CONFIRMED**

Remainders are taken with respect to the *moving* monic `K`, not `K_0`. Then `K(z_0(w))=w^3` holds identically in the moving `p,c`, as a Laurent identity at infinity, with no finite jet bound and no extra denominator.

Through weight 20 the two layers are `M=N_M/K` with `deg N_M<=4` and `N=N_N/K^2` with `deg N_N<=6` (`Q^3` has degree at most 6). Placing `M` over `K^2` produces numerator `N_M K` of degree at most 7. Reducing a polynomial of degree at most 7 (resp. 6) modulo the monic degree-6 polynomial `K^2` leaves a remainder `S` of degree at most 5. Thus through weight 20 one has exactly

```text
S(z_0(w))/w^6,     deg_z S <= 5.
```

Triangularity. If `S=s_5 z^5+cdots+s_0` and `z_0=w+O(w^{-1})`, then `[w^n] z_0^n=1` for each `n`, and `[w^m] z_0^n=0` whenever `n<m`. Therefore the map sending `(s_5,...,s_0)` to the coefficients of `w^{-1},...,w^{-6}` in `S(z_0)/w^6` is lower triangular in the highest-degree-first ordering, with unit diagonal. Equivalently, a proper numerator of degree `d<3j` over `K^j` has first tail at `w^{d-3j}` with leading coefficient the leading coefficient of the numerator. For `j=2` the first six tails determine `S` by back-substitution over the valuation ring, coefficient by coefficient in the Lambda-adic filtration. Off-diagonal entries depend on `p,c`; the diagonal does not. Invertibility does not divide by `Delta_0`.

Killing the first six tails through weight 20 therefore kills all six coefficients of each homogeneous piece `S_w`, hence kills `S` through weight 20, hence kills every later tail of this layer, including row 7 and row 8. Inductively on weight: if `S_j=0` for `j<w`, motion of `z_0` cannot manufacture weight-`w` tails from nothing, so the triangular map at the special fibre applies to `S_w` alone.

Sharp negative control `z/K^3`. Evaluating `z/K^3` at `z_0` gives `z_0/w^9`. Since `z_0=w+O(w^{-1})` and the inverse of a depressed cubic has no `w^0` term,

```text
z_0/w^9 = w^{-8} + O(w^{-10}).
```

Rows 1 through 7 vanish and row 8 equals 1. A `K^{-3}` layer through weight 20 could therefore feed the row-8 target without being visible in the first six tails. The binomial enumeration of Charge 5 is the statement that no such layer exists through weight 20, and `z/K^3` is the statement that this vanishing is load-bearing for the cutoff. That is the firewall protecting the argument. The AWS control confirms the unit-diagonal matrix and the profile of `z/K^3`; the identities are elementary Laurent leading-term facts and do not depend on that run.

---

## Charge 7 — target subtraction and the row-8 coefficient

**CONFIRMED; no motion of `p,c`, `tau`, or a load supplies it**

The valuation-15 and valuation-18 targets, evaluated at `z_0`, are exactly

```text
(mu Lambda^{15} K + nu Lambda^{18}) / K^2
  = mu Lambda^{15} w^{-3} + nu Lambda^{18} w^{-6}.
```

This uses `K(z_0)=w^3` identically, for the moving cubic. The row-3 target occupies only `w^{-3}` and the row-6 target occupies only `w^{-6}`; there is no leakage into any other tail, in particular none into row 7 or row 8. Subtract this moving numerator from `S`. The remainder `S'` still has degree at most 5. Through weight 20 its first six tails vanish: rows 1, 2, 4, 5 have zero targets at every weight, row 3 has been cancelled at weight 15 and is zero at every other weight `<=20`, and row 6 has been cancelled at weight 18 and is zero elsewhere through 20. Charge 6 then gives `S'=0` through weight 20.

Consequently the unadjusted layer `S/K^2` agrees with the target numerator through weight 20, and its row-8 coefficient through weight 20 is zero.

The exact targets `(1)` have no weight-20 initial form in rows 1 through 7: `mu Lambda^{15}` and `nu Lambda^{18}` are pure of those weights (`mu,nu` are constants), and the remaining six rows have zero targets. Row 8 has initial form `Lambda^{20}(1+tau)` with `v(tau)>0`, hence leading coefficient `1` at weight 20. This contradicts the vanishing just obtained.

Search for a substitute leading term at weight 20:

- Motion of `p,c`. These are regular coordinates of the projective centre (`p=B_7/3`, `c=B_6/3`). They may vanish (axes, already squarefree) but they do not pole. Their motion is already absorbed into moving `K` and moving `z_0`. Derivatives of `K` do not re-enter as extra denominators. Off-diagonal triangular entries depending on `p,c` are handled by back-substitution and cannot create a kernel, because the diagonal is identically 1.
- Motion of `tau`. The only `tau` in the targets is the factor `1+tau` on row 8, which contributes at weight strictly larger than 20. It cannot cancel the leading `1`, nor can it appear on the left-hand side through weight 20 after `S'=0`.
- Zero loads. Setting `k=0` deletes `kbar` summands from `M` and `N`; setting `mu=0` or `nu=0` deletes a target. Both operations make more tails vanish, not fewer. They cannot produce a unit in row 8.
- Nonzero loads. The `kbar` terms are already inside `M,N` and therefore inside `S`. The loads `mu,nu` feed only rows 3 and 6, exactly, at `z_0`, and only at weights 15 and 18 through the cutoff.
- Higher jets of `Q,R`. These do produce weight-20 pieces of `S` (for instance `Q^{(i)} R^{(j)}` at `i+j=5`). All of them remain inside a degree-at-most-five numerator over `K^2` and are killed with the first six tails.
- Inverse substitution. Charge 5: contamination starts at weight 21.
- A `K^{-3}` layer. Charge 5: first appearance at weight 21.

No remaining source for a weight-20 row-8 coefficient exists on the squarefree chart.

---

## Charge 8 — remaining locus, identity `(22)`, conditional corollary

**CONFIRMED**

### Double-root normal form and weighted `P(2,3)`

A nonirrelevant depressed cubic with `Delta_0=0` has a double root. If the double root is at `a` and the simple root is at `b`, depression forces `2a+b=0`, hence `b=-2a` with `a!=0`. Expanding,

```text
(z-a)^2 (z+2a) = z^3 - 3 a^2 z + 2 a^3,
```

so `p_0=-3a^2` and `c_0=2a^3`. Directly, `-4 p_0^3-27 c_0^2=108 a^6-108 a^6=0`. The triple root is `a=0`, i.e. `(p_0,c_0)=(0,0)`, i.e. `K_0=z^3`, the affine origin of the common-cubic cone, which is not a point of `Proj`. Thus `(21)` is the unique projective survivor.

Weighted homogeneity is `(p,c) |-> (lambda^2 p, lambda^3 c)`. The curve `c^2 : p^3` is constant on the double-root locus. Scaling `a=1` gives `(-3,2)`; scaling `a=-1` gives `(-3,-2)`, which is the same point of `P(2,3)` via `lambda=-1` (weight 2 even, weight 3 odd). So the remaining locus is one point of weighted `P(2,3)`, represented by `(p_0,c_0)=(-3,2)`.

### Identity `(22)` and why the squarefree proof stops

At the normalised point `K=(z-1)^2(z+2)=z^3-3z+2`, take `Q=(z-1)(z+2)=z^2+z-2` and `R=1/3`. Direct expansion:

```text
K^2 = z^6 - 6 z^4 + 4 z^3 + 9 z^2 - 12 z + 4,
9 R K - Q^2 = 3K - Q^2,
Q (9 R K - Q^2) = -K^2.
```

The last identity was checked by multiplying the polynomials; both sides equal `-z^6+6z^4-4z^3-9z^2+12z-4`. In the `alpha=2beta` numerator of Charge 3 this says

```text
(4/81) Q(9 K R - Q^2)/K^2 = (4/81)(-K^2)/K^2 = -4/81,
```

a polynomial, hence no negative tails, even though `Q` is not divisible by `K`. Equivalently, in the non-reduced algebra `L[z]/(K)` one has `Q^3 equiv 0` while `Q notequiv 0`: `Q` vanishes at both geometric roots but is missing one factor of `(z-1)`. This is exactly the nilpotent that Charge 4 forbids. The identity is a negative control demonstrating that the implication `Q_0^3=0 => K_0 | Q_0` is false on `Delta=0`; it is not a formal arc, and it does not by itself produce a solution of the eight loaded equations.

### Conditional global-support corollary

Ingredients, and only these:

1. The independently reviewed common-cubic reduced-support theorem (charged grok review, verdict CONFIRMED): the reduced support of the exceptional fibre `k=0`, `r_1=cdots=r_8=0` is the graph of `C=z^3+p z+r`, `f=C^3`, `g=C^4`, projectively `P(2,3)`, including both axes and the discriminant-zero locus. The affine origin is a point of the cone and is not a projective coefficient-infinity centre.
2. This theorem: no strict arc is centred on the squarefree open `Delta_0!=0` of that graph. The axes are squarefree and are included.
3. Algebraic curve selection, as stated in the charged saturation source, section 4: a nonirrelevant zero of the saturated endpoint `H` is a centre of a formal/Puiseux arc (after a finite extension) lying in the interior at the generic point. Conversely, the centre of any strict branch is a nonirrelevant zero of `H`.

If `H!=(1)`, a projective point of `V(H)` therefore exists, lies on the common-cubic graph, and is the specialisation of a Puiseux arc to which this theorem applies. That point cannot have `Delta!=0`. The only remaining projective point is the double-root point `(-3:2)`. This is a containment of reduced projective support. It does not follow that the point lies in `V(H)`, that a branch through it exists, that the local ring has finite length, or that a rational section exists. Those are the double-root chart, thickness, and accessibility, all open.

---

## Attacks recorded and rejected

- A higher binomial term (`Q^2 R/K^3`, `Q^4/K^4`, `kbar R/K`, `kbar Q^2/K^2`) arriving before the three candidates when `beta<6`. Weight comparisons forbid it.
- Equal-valuation cancellation among `QR`, `R^2`, and `Q^3` producing a non-residue-zero numerator that is still divisible by `K_0^2` on the squarefree chart. The only meeting that can hide a term is `alpha=2beta`, and reducing modulo `K_0` still yields `Q_0^3=0`. Hiding requires a nilpotent.
- A vanished `QR/K` layer re-entering at the next valuation via a jet of `Q` and cancelling `R_0^2` modulo `K_0`. The correction is a term over denominator `K` and dies modulo `K_0` after clearing the common denominator.
- Target coincidences at 15, 18, or 20 in the range `beta<6`. Weight 20 is never first. Weight 15 replaces zero by a multiple of `K_0`. Weight 18 is too late to save a `Q^3` layer already contradicted between 15 and 18 when `5<beta<6`.
- Replacing squarefree by irreducible, or refusing to split. The residue algebra of a split squarefree cubic is a product of fields; componentwise checking is the correct (and weaker) hypothesis.
- Mixed vanishing `Q_0 R_0=0` with neither polynomial zero, surviving the second equation. The second equation forces both values to vanish at every component.
- Weight-20 monomials of leading `(Q,R,kbar)`. None exist, but higher jets do; they live in `S` and are killed by triangularity. A slogan "no weight-20 term" would be a gap; the target does not make it.
- Inverse of `f` versus inverse of `K` mixing a weight-20 tail. Contamination starts at weight 21.
- Motion of `p,c` introducing a pole or a kernel of the six-by-six tail map. Moving monic division; unit diagonal independent of `p,c`.
- A zero or nonzero load feeding row 8. Loads feed rows 3 and 6 only, or delete terms.
- `tau` cancelling the leading `1` of row 8. `v(tau)>0`.
- Extending the lemma across `Delta=0` by the same residue argument. Identity `(22)` is an explicit counterexample to `Q^3=0 => Q=0`.
- Inferring that `(-3:2)` lifts, or that `H` is nonunit. The corollary is a containment conditional on `H!=(1)`.
- Using AWS-reconstructed quadrics, the composition Jacobian, or the special branch `(20)` as a step. None is used. Branch `(20)` is squarefree (`77 p_0^3` as a discriminant factor) and is already excluded by the order-20 theorem if it were to lift; that remark is optional.

## Exposition defects, not mathematical gaps

1. Formula `(5)` is the complete *quadratic* generating function and omits `Q^3/K^2`. The valuation table lists that cubic term separately in `(9)`. A reader who treats `(5)` as the input to Charge 3 will be looking at the wrong generating function. The proof as written does not make that mistake.
2. The sentence assigning `v(kbar)=6` in the load-weight paragraph is the Rees weight of the coordinate `kbar=Lambda^6 k`. When `k=0` the specialised series is the zero series. The argument never divides by `k` and never needs the specialised valuation to be exactly 6. The wording is slightly loose.
3. The first AWS firewall run rejected a correct unit-diagonal matrix because the harness called it upper-triangular. The identity was unchanged; the corrected control is the charged `verify_firewall_controls.py`. Retaining the failed stderr is honest and is not a theorem defect.

None of these alters an identity or a hypothesis.

## Firewalls (enforced)

| Forbidden reading | Status |
|---|---|
| The double-root point is excluded | Open. Identity `(22)` shows the squarefree step fails there. |
| That point lifts, or `H` is nonunit | Not claimed. Corollary is conditional containment. |
| Local thickness / embedded structure of the endpoint | Open. Reduced support only. |
| Finite jet on the remaining chart | Explicitly declined. |
| Accessibility of a rational constant-field section | Open. Curve selection is Puiseux, not D1 monodromy. |
| Finite coefficient load off this strict gate | Open. |
| Other passports, `(8,12)`, maximum-twelve, JC2 | Open. |
| Section 4 leading system as part of the exclusion | Not used. |

## Strongest surviving statement, restated

No strict D1 coefficient-infinity arc in the ordinary isotrivial chart is centred on a squarefree common cubic. The only remaining projective centre on the reviewed exceptional support is the double-root point of `P(2,3)`. Whether that point is attained, and with what thickness, is a different theorem.

CONFIRMED
