# Hostile review — exact one-parameter Rees reduction of the `(8,12)` order-two `U=2,[6,2]` strict-Rees boundary

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md` |
| Target SHA-256 | `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. Charged reviews were opened only because they are named; no producer status line and no charged `CONFIRMED`/`REPAIR` string is evidence |
| Method | source reading and hand derivation only; SHA-256 of the target and every charged local source; no Singular, Sage, msolve, Lean, or substantive exact Python |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b`, matching the required pin. Producer verdict language, the target's own status line, live AWS jobs, and the timeout packet named in target §1 were not used as evidence. No file other than this review was written.

---

## Verdict

After localizing at the unit `R=1+tau`, the change `C_i=R^{i mod 2} B_i`, `J=R j` is an automorphism of the formal `T=1` chart, and every exact V2 row becomes the displayed one-parameter family `(0.1)` by the single substitution `Lambda=tau^3 varrho`. The base map `Q[Lambda] to Q[tau,varrho,R^{-1}]` is torsion-free over a PID, hence flat; polynomial extension by all seven retained loads and the unit automorphism preserves flatness. Principal saturation by `Lambda J` commutes with that flat extension and equals sequential saturation by `tau`, `varrho`, `j` on the unit chart, because `D(Lambda J)=D(tau varrho j)`. The scheme-theoretic fibre of the saturated family over the `Q`-point `Lambda=0` equals the fibre of the pulled-back family over the `Q`-point `(tau,varrho)=(0,0)`; ramification of `tau^3` thickens the divisor `V(Lambda)` in the two-parameter base, not the closed-point fibre in coefficient-load space. Irrelevant saturation by `(C_0,...,C_6)` agrees with saturation by `(B_0,...,B_6)` on that fibre. All seven finite loads remain. The toy ideal `(x-Lambda m)` correctly shows that a generic-chart projection of a solved load enlarges the boundary, and the reduction does not make that projection. Equality of the two algebraic boundary schemes is not emptiness, Taylor realization, exclusion of `[6,2]`, order-two closure, `(8,12)`, maximum twelve, or JC2.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md` | `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b` | target (matches required pin) |
| `xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md` | `e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7` | source-typed client; ordinary chart `(3.2)`–`(3.6)`, loads, twists |
| `xmodel/max12-812-order2-u2-62-strict-rees-client-erratum-v2-20260825.md` | `5aa954cbe6396ef5de353519eaf10aed567aec55964bb197c9eb1576b131c10b` | replaces client `(3.7)` by sequential saturation `tau`, `varrho`, `j` |
| `xmodel/max12-812-order2-u2-62-strict-rees-compiler-v2-source-review-20260825.md` | `b7666bb12ef454f5047074898e0384968393916d97bd06673d3a1f20ab70f50d` | V2 emitter is the erratum patch of frozen V1; no `(9,12)`, no DS optimization, no endpoint |
| `cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | exact seven ordinary tails; ten-tuples `(a0..a6,k10,k6,k2)` |
| `cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/strict_rees_v2.sing` | `021654e753f1186874f10110d4338e7d9f9457afbfed75419407e87e3b00982c` | frozen V2 input; seven `Psi` rows, `sat` by `tau` then `rho` then `j` |

All six hashes match the values printed in the target and in the review prompt. The printed canonical all-tail digest `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8` is consistent across the target, the V2 `result.json`, and the one-parameter freeze; it was not independently recomputed from a JSON canonicalization. The timeout packet SHA named in target §1 is not a charged source for the algebra and was not opened.

The V2 compiler source review is used only as a hash-locked description of the emitter (erratum patch, retained `Psi` lines, no DS optimization). Its token `SOURCE-CONFIRMED FOR AWS EMISSION; NO SATURATION VERDICT` is not an input.

---

## Strongest exact theorem that survives

Let `R=1+tau`. In the source-typed ordinary strict-Rees chart of the order-two client `U=2`, `h=x^6(x-1)^2` at `T=1`, localize at `R` and apply the automorphism `C_i=R^{i mod 2} B_i`, `J=R j`, keeping every finite load `k_{10},k_6,k_2,mu_2,mu_4,mu_6` and the Jacobian constant. After `Lambda=tau^3 varrho`, the seven exact V2 generators are the pullbacks of

```text
Phi_ell =
 r_ell(C, Lambda^2 k10, Lambda^6 k6, Lambda^10 k2)
 - Lambda^(12+ell) delta_ell,

delta_1=delta_3=delta_5=0,
delta_2=mu2, delta_4=mu4, delta_6=mu6, delta_7=J/4.
```

The map `Q[Lambda] -> Q[tau,varrho,R^{-1}]`, `Lambda |-> tau^3 varrho`, is flat. Polynomial extension by the retained coefficient and load variables, followed by the unit automorphism, is a flat base change. Consequently, writing `I0=(Phi_1,...,Phi_7)` and writing `I=(Psi_1,...,Psi_7)` for the exact V2 ideal,

```text
((I0 : (Lambda J)^infinity) + (Lambda)) : (C0,...,C6)^infinity
```

and

```text
((I : (tau varrho j)^infinity) + (tau,varrho)) : (B0,...,B6)^infinity
```

define the same closed subscheme of affine coefficient-load space after the identifications `C_i=B_i` and `J=j` on the central fibre. The equality is scheme-theoretic: it includes nilpotents, embedded components, and every finite load. It is not an emptiness statement, a Taylor statement, or an exclusion of the source `[6,2]`.

---

## Attack 1 — row identity, exponents, twists, signs, `J/4`, no `(9,12)`

**CONFIRMED.** Every V2 row is the pullback of `(0.1)`. No `(9,12)` generator and no omitted load enters.

The charged client `(3.3)`–`(3.6)` already writes the ordinary coefficients as `C_i=(1+tau)^{i mod 2} B_i` and the seven equations as

```text
Psi_ell =
 r_ell(C, tau^6 varrho^2 k10, tau^18 varrho^6 k6, tau^30 varrho^10 k2)
 - tau^{3(12+ell)} varrho^{12+ell} gamma_ell(tau),
```

with `gamma_1=gamma_3=gamma_5=0`, `gamma_2=mu_2`, `gamma_4=mu_4`, `gamma_6=mu_6`, and `gamma_7=(j/4)(1+tau)`. The substitution `Lambda=tau^3 varrho` is an identity of monomials, not an approximation:

| object | two-parameter monomial | one-parameter monomial |
|---|---|---|
| `k10` | `tau^6 varrho^2` | `Lambda^2` |
| `k6` | `tau^18 varrho^6` | `Lambda^6` |
| `k2` | `tau^30 varrho^10` | `Lambda^{10}` |
| target weight `12+ell` | `tau^{3(12+ell)} varrho^{12+ell}` | `Lambda^{12+ell}` |

The four even/terminal target exponents in the frozen V2 input are `tau^{42} rho^{14} mu2`, `tau^{48} rho^{16} mu4`, `tau^{54} rho^{18} mu6`, and `tau^{57} rho^{19} (j/4)(1+tau)`. These are exactly `Lambda^{14} mu2`, `Lambda^{16} mu4`, `Lambda^{18} mu6`, and `Lambda^{19}(J/4)` after `J=R j`. Odd rows 1, 3, 5 have no target subtraction in V2, matching `delta_1=delta_3=delta_5=0`. Signs are uniformly minus on the displayed target.

The twist is the odd-coefficient power of `R`. In the V1 emitter that V2 wraps, each ordinary monomial is multiplied by `(1+tau)` to the total degree in `a1,a3,a5`. That is `C_odd=R B_odd` and `C_even=B_even`. Hand checks against `tails.json` and `Psi1`, `Psi2`, `Psi7`:

- tail 1, monomial `a0 a3`, coefficient `3/4` becomes `(3/4) C0 C3=(3/4)(1+tau) B0 B3`, which is the leading term of `Psi1`;
- tail 1, monomial `a5 k2`, coefficient `1/4` becomes `(1/4)(1+tau) B5 k2 tau^{30} rho^{10}`, the last `Psi1` summand;
- tail 1, monomial `a1 a5^2`, coefficient `-3/16` becomes `(-3/16)(1+tau)^3 B1 B5^2`, present in `Psi1`;
- tail 2, monomial `a1^2`, coefficient `3/8` becomes `(3/8)(1+tau)^2 B1^2`, present in `Psi2`;
- `Psi7` ends with `-tau^{57} rho^{19} ((j/4)(1+tau))`.

No division by a coefficient or a load occurs. The identity is polynomial on the unlocalized ring and becomes an automorphism only after inverting `R`.

The frozen tails are ordinary `(8,12)` tails: each monomial is a ten-tuple in `(a0,...,a6,k10,k6,k2)`, weights `12+ell`, no `a7`, no `k8`, no `F9`. Supports are 36, 54, 58, 81, 89, 120, 131. The V2 ring retains `k10,k6,k2,mu2,mu4,mu6,j`. The V2 source review forbids a lower-load DS optimization and requires reconstruction independent of every `(9,12)` source. The one-parameter ring retains `k10,k6,k2,mu2,mu4,mu6,J`.

---

## Attack 2 — `R` is a unit; automorphism; irrelevant ideal on the central fibre

**CONFIRMED.** Localization at `R` is load-bearing for invertibility and does not change the irrelevant ideal at `tau=varrho=0`.

In `Q[[tau]]` one has `R=1+tau` a unit. Algebraically the same chart is `Q[tau,varrho,R^{-1}]`. The locus `R=0` is `tau=-1`, i.e. `T=0`, the other finite branch point, disjoint from the formal chart `T=1`. The inverse change is `B_even=C_even`, `B_odd=R^{-1} C_odd`, `j=R^{-1} J`. On the unit chart each `C_i` is a unit times `B_i`, so `(C_0,...,C_6)=(B_0,...,B_6)` as ideals before specialization. On the central fibre `tau=0` one has `R=1`, hence `C_i=B_i` and `J=j` as elements, and the two irrelevant ideals coincide for a second independent reason.

Without inverting `R`, the polynomial substitution `(B,j) |-> (C,J)` collapses odd coefficients and `j` along `R=0` and is not an automorphism. That collapse is disjoint from `V(tau)` in the `tau`-line, so it cannot support an embedded component that meets `tau=varrho=0`. The special-fibre rings are canonically isomorphic:

```text
S_R / (tau,varrho)
  = S[u] / ((1+tau)u-1, tau, varrho)
  = (S/(tau,varrho))[u] / (u-1)
  ≅ S / (tau,varrho).
```

Localizing at `R` before saturation therefore does not change the boundary scheme of the original client.

---

## Attack 3 — flatness of the toric base change

**CONFIRMED.** Torsion-freeness over the PID applies, and the claimed extensions remain flat.

The ring `Q[Lambda]` is a Euclidean domain. The target `Q[tau,varrho,(1+tau)^{-1}]` is a domain (a localization of a polynomial ring) and embeds in the field `Q(tau,varrho)`. If `P(Lambda) f=0` in the target, then `P(tau^3 varrho)=0` or `f=0`. The elements `(tau^3 varrho)^n` are linearly independent over `Q` (evaluate at `tau=1` to get `P(varrho)`), so `P=0`. Thus the target is torsion-free as a `Q[Lambda]`-module. Over a PID, torsion-free modules are flat. Finite generation is not required: the criterion is not “finitely generated torsion-free implies free”.

The same argument already gives flatness of `Q[Lambda] -> Q[tau,varrho]` by `Lambda |-> tau^3 varrho`; inverting `R` is a further localization, hence flat, and a composite of flat maps is flat. Geometrically the map is surjective on spectra (`Lambda=c` is hit by `tau=1`, `varrho=c` for `c` arbitrary, including zero), so it is faithfully flat. Faithful flatness is not named in the target; ordinary flatness is what the colon-commutation uses. Faithful flatness is recorded here because it also gives `I B cap A=I`, so no extra contracted elements appear after extension.

Let `A=Q[Lambda,C0,...,C6,k10,k6,k2,mu2,mu4,mu6,J]`. Polynomial extension is base change of the toric map along the free algebra `Q[Lambda] -> A`, hence flat. The unit automorphism of the localized two-parameter ring is an isomorphism, hence flat. The composite

```text
A -> Q[tau,varrho,R^{-1},C0,...,C6,k10,k6,k2,mu2,mu4,mu6,J]
  -> Q[tau,varrho,R^{-1},B0,...,B6,k10,k6,k2,mu2,mu4,mu6,j]
```

is therefore a flat base change, as claimed in target `(3.1)` and the paragraph that follows it.

A ramified finite map such as `Q[t] -> Q[x]`, `t |-> x^2`, is likewise torsion-free over a PID and flat. Ramification is not an obstruction to flatness of `(3.1)`.

---

## Attack 4 — scheme equality, not generic-chart or reduced-support equality

**CONFIRMED.** No extra torsion, embedded component, nilpotent, or nonflat specialization is introduced by the ramified toric pullback.

**Opens.** On the unit chart, `Lambda J=tau^3 varrho R j`. Invertibility of `R` and the identity `D(tau^3)=D(tau)` give

```text
D(Lambda J)=D(tau varrho j).
```

The target writes the first factor and leaves `D(tau^3)=D(tau)` implicit; the identity is correct.

**Product versus sequential saturation.** For any ideal, `(I:f^infty):g^infty=(I:(f g)^infty)`. Saturating `I0` by `Lambda` then `J` equals saturating by `Lambda J`. Saturating the V2 ideal by `tau` then `varrho` then `j` equals saturating by `tau varrho j`. The erratum replaced original client `(3.7)`, which omitted `j`, by `(E.1)`; the theorem and the frozen V2 input both use the erratum.

**Colons commute with flat extension.** If `A -> B` is flat and `I subset A` is finitely generated, multiplication-by-`f^n` on `A/I` remains exact after `otimes_A B`, so `(I:f^n) B=(I B:f^n)` for each `n`. Directed unions commute with extension of ideals; Noetherianity makes the colon chain stabilize, so

```text
(I0:(Lambda J)^infty) B = (I0 B:(Lambda J)^infty) = (I0 B:(tau varrho j)^infty).
```

That is target `(3.2)`. The second equality uses the identity of principal opens, not a radical or a generic-chart restriction. Equivalently, `I:f^infty` is the kernel of `A -> (A/I)_f`, and the two localizations of the quotient at `Lambda J` and at `tau varrho j` coincide.

**Closed-point fibres, not the ramified divisor.** Let `K_A=I0:(Lambda J)^infty` and let `K_B` be its extension. The one-parameter boundary before irrelevant saturation is the fibre of `V(K_A)` over the `Q`-point `Lambda=0`. The two-parameter boundary before irrelevant saturation is the fibre of `V(K_B)` over the `Q`-point `(tau,varrho)=(0,0)`. For an arbitrary morphism of bases `T -> S` and a scheme `Z` over `S`, the fibre of `Z times_S T` over a point `p` of `T` is the fibre of `Z` over the image of `p`. Here that image is `Lambda=0`, and the residue-field map is `Q -> Q`. Explicitly,

```text
A / (Lambda) ≅ Q[C0,...,C6,k10,k6,k2,mu2,mu4,mu6,J],
B' / (tau,varrho) ≅ Q[C0,...,C6,k10,k6,k2,mu2,mu4,mu6,J],
```

the second isomorphism sending `R^{-1}` to `1`, and the image of `K_A` in the first quotient equals the image of `K_B` in the second. This is an equality of ideals, not of radicals, so nilpotents and embedded components match.

The ramification `Lambda=tau^3 varrho` thickens the divisor `V(Lambda)` in the two-parameter base to `V(tau^3 varrho)`, a non-reduced union of axes. That divisor is not the boundary of the client. The client specialises to the closed point `(tau,varrho)=(0,0)`. Quotienting by `(tau,varrho)` kills `tau` to first order, so the multiplicity three never appears in the coefficient-load fibre. Comparing fibres over the non-reduced scheme `Spec Q[Lambda]/(Lambda)` with fibres over `Spec Q[tau,varrho]/(tau^3 varrho)` would be a different, false, claim. The theorem does not make it.

**Irrelevant saturation.** On the identified special-fibre ring, `(C_0,...,C_6)=(B_0,...,B_6)`. Saturating the two boundary ideals by those irrelevant ideals therefore yields the same scheme. Loads are not among the irrelevant generators, so they survive as affine coordinates on both sides.

The original unlocalized saturation has the same special fibre as the `R`-localized one by Attack 2. This closes the comparison with erratum `(E.1)`.

---

## Attack 5 — retained loads and the toy projection

**CONFIRMED.** Every finite load remains. The toy is a correct negative control. The reduction does not project.

The one-parameter family `(0.1)` is an ideal in

```text
Q[Lambda,C0,...,C6,k10,k6,k2,mu2,mu4,mu6,J].
```

All seven finite loads of client contract item 3 are present. Rows 2, 4, 6, 7 are affine in `mu2, mu4, mu6, J` with coefficients `Lambda^{14}`, `Lambda^{16}`, `Lambda^{18}`, `Lambda^{19}`. On `D(Lambda)` those four variables may be solved. The theorem forbids eliminating them before closure.

The toy `I=(x-Lambda m)` in `Q[Lambda,m,x]` is prime, isomorphic to `Q[Lambda,m]` via `x=Lambda m`, and does not contain `Lambda`, so it is already `Lambda`-saturated. Its special fibre is `(x,Lambda)` with `m` free, hence `x=0`. On `D(Lambda)` one may set `m=x/Lambda` and forget `m`; the projection is the whole `D(Lambda)` in the `(Lambda,x)`-plane, whose closure meets `Lambda=0` in every `x`. Generic-chart projection of a solved load strictly enlarges the Rees boundary. The displayed family does not perform that projection. Successor language in target §5 (coefficientwise finite-quotient jets, odd-row `3 x 3` in `k10,k6,k2`, retained divisibility orders `14,16,18,19`) is not the theorem and, as written, still retains the loads.

---

## Attack 6 — frozen one-parameter compiler versus the theorem

**CONFIRMED as a consistency check.** The package retains the seven loads, pins the exact tails, and does not promote an endpoint. Live AWS jobs were not used as algebra.

Inspection of `cases/max12_812_order2_u2_62_oneparam_rees_20260826/compile_oneparam_rees.py` (freeze hash `5905e57578c5f9af047f70f8fce48a6ab56ce9dccfc2a33d868d8e05b3f4ea82`):

- ring variables `Lambda,C0,...,C6,k10,k6,k2,mu2,mu4,mu6,J`;
- targets `0, mu2, 0, mu4, 0, mu6, J/4`;
- lower-load monomials scaled by `Lambda^2`, `Lambda^6`, `Lambda^{10}`;
- pinned hashes of the theorem, the client, the erratum, the V2 source review, `tails.json`, and the canonical all-tail digest;
- affine-linearity and weight-`12+ell` checks on the frozen tails;
- sequential `sat` by `Lambda` then `J`, then `Lambda=0`, then saturation by `(C0,...,C6)`;
- `result.json` scope `strict_rees_endpoint=EMITTED_NOT_RUN`, `order2_closed=false`, `JC2=NOT_CLAIMED`, Taylor families not compiled.

The print `ONEPARAM_REES_ENDPOINT=PASS` is an unconditional stage-completion sentinel after `H` is formed, parallel to V2's `STRICT_REES_J_NONZERO_SATURATED=1`. Unit-hood of `H` is a separate measured string `ONEPARAM_H_IS_UNIT`. That is not an endpoint claim. Registration and the launch note both refuse to interpret a timeout or a missing sentinel as a mathematical verdict. The two recorded AWS jobs are producer experiments and are not evidence for the reduction.

Non-blocking implementation observation, not a defect of the theorem: the emitter assigns `sat(...)` directly to an ideal, whereas the frozen V2 input unpacks `sat` through a list. The algebraic saturation prescribed by the theorem is the same in either encoding.

---

## Attack 7 — firewall

**CONFIRMED.** Target §0 last paragraph and §6 state that the theorem is equality of two algebraic boundary schemes, conditional on the frozen source-typed client, and that it proves neither scheme empty or realizable. It does not solve either finite Taylor family, exclude the fixed `[6,2]` source, close order two, close `(8,12)`, prove maximum twelve, or prove JC2. Section 5's Hall/Shioda remark is explicitly a prefilter of the all-lower-load-zero sub-stratum, not order-two closure, and is not used in the reduction.

---

## Attacks that failed to break the claim

Treating `Q[tau,varrho]` as having `Lambda`-torsion because `tau^3 varrho` is ramified (the ring is a domain; `P(tau^3 varrho)` vanishes only if `P=0`). Treating ramification as nonflatness (torsion-free over a PID is flat; the classical map `t |-> x^2` is finite flat). Comparing the one-parameter special fibre to the two-parameter fibre over the non-reduced divisor `V(tau^3 varrho)` rather than over the origin (the theorem specialises to `tau=varrho=0` and to `Lambda=0` as `Q`-points). Claiming that `D(tau^3)` is strictly smaller than `D(tau)` (a ring element is invertible if and only if its cube is). Reading original client `(3.7)` instead of the charged erratum (V2 and the theorem both saturate by `j`). Treating affine-linearity of the tails in `k10,k6,k2` as a hypothesis of the base-change theorem (it is a successor optimization; homogeneity of the scaling uses only the weights). Treating live AWS timeouts or stage sentinels as saturation evidence (they are not).

---

## Scope that remains open

The common boundary scheme may still be the unit ideal or a nonempty cone. Neither finite Taylor family is imposed. The reduction does not exclude `[6,2]`, close order two, close `(8,12)`, prove maximum twelve, or prove JC2.

CONFIRMED
