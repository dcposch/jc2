# Hostile review — `(8,12)` order one: terminal `r7` pure-power component criterion

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order1-terminal-r7-pure-power-component-criterion-20260826.md` |
| Target SHA-256 | `bbd744fa0c3875f11d5f0038dbbdea461e2656c6a9eb98d2b9050c1eae31712a` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. The charged terminal-power review is same-model and is not used as a PASS/CONFIRMED certificate; the order-one formulae `(0.9)`–`(0.10)` are taken as statements of the charged theorem, then the source divisor, the extension through normalization, singleton-support descent, Riemann–Hurwitz saturation, the degree firewall, and the falsifier are re-derived below from those statements and from `8 r_7'=j/q` alone |
| Method | source reading and hand derivation only; SHA-256 of the target and the three named parents; no CAS, solver, substantive Python, Lean, or other heavy local computation |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is `bbd744fa0c3875f11d5f0038dbbdea461e2656c6a9eb98d2b9050c1eae31712a`, matching the launch pin. All three charged sources match the hashes printed in the target's Section 0. Producer verdict language, the target's own status line, and any prior PASS/CONFIRMED token were not used as evidence. No file other than this review was written.

---

## Verdict

The charged note is correct as a terminal necessary condition on any 1-dimensional fixed-load coefficient component met by a genuine order-one source with `U>=2`. Independently: `8 r_7'=j/q` with `q=c(x-a)^U` integrates to `r_7=lambda+gamma (x-a)^{1-U}` with the displayed `gamma=j/(8c(1-U))!=0`; the complete source divisor is `(U-1)([infinity]-[a])`; `U=1` is empty and `U=0` is affine-linear, hence separate; a nonconstant rational map from the complete source line to a projective curve extends uniquely through the normalization; nonconstancy of the pulled-back tail makes both `phi` and `R` nonconstant and forces `g(X)=0`; singleton support of the pullback zero and pole divisors, with `phi` finite and surjective, forces singleton support downstairs, equal orders, unique preimages, total ramification, and `d*n=U-1`; after coordinates one has `R=lambda+delta t^d`, with branch-value set `{lambda,infinity}` if `d>1` and an isomorphism if `d=1`; the two total-ramification points of `phi` saturate Riemann–Hurwitz, so `phi` is conjugate to a power map; the downstairs order `U-1` is not licensed without birationality; the proposed falsifier is a valid necessary screen, and consuming a modular projection still requires an actual component, the exact normalization, the complete graph of the actual `r_7`, chart complements, and a characteristic-zero lift. Passing these identities does not empty order one, close Taylor/Rees, empty `(8,12)`, prove maximum twelve, or touch JC2.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order1-terminal-r7-pure-power-component-criterion-20260826.md` | `bbd744fa0c3875f11d5f0038dbbdea461e2656c6a9eb98d2b9050c1eae31712a` | target (matches required pin) |
| `xmodel/max12-812-terminal-power-belyi-order1-theorem-20260825.md` | `a4d7d6a1173b5a0b785aa61a4c80ad5f46e4ea83f1d73103917c425608666633` | charged order-one classification `(0.9)`–`(0.10)`, terminal row `8 r_7'=j/q`, emptiness of `U=1`, converse primitives |
| `xmodel/max12-812-terminal-power-belyi-order1-review-grok-20260825.md` | `e322d508c2af66aebb408b2794bd017b05e96cf9ca67f0fc74be8407406f67e1` | same-model audit of the charged theorem (read; unused as a verdict) |
| `xmodel/max12-812-order1-fixedload-coefficient-curve-probe-design-20260826.md` | `14f872accdeaaa9120924bfbe187cec6092ef27a64af59c8c24a301efefc65e6` | fixed-load fibre, `r_7` as a graph function, plane-projection and chart-complement warnings; no genus or component verdict is consumed |

All three parent hashes match the target's Section 0. The charged theorem is consumed only for the order-one leaf: `u=q` polynomial of degree `U`, the identity `8 r_7'=j/q`, the classification `U=0` or `q=c(x-a)^U` with `U>=2`, emptiness of `U=1`, and the explicit primitives `(0.10)`. Its nontrivial Kummer leaves, three-value passport, and reconstruction `(0.8)` are not inputs. The probe design is consumed only as the ambient language of a fixed-load coefficient fibre and as a warning that a plane eliminant is not a normalization; its sampled tuples, primes, and compiler contract are not inputs. No scope-firewall sentence of any parent is an input.

---

## Strongest exact theorem that survives

Let `k` be an algebraically closed field of characteristic zero and let `j in k^*`. On a genuine order-one client the terminal row is `8 r_7'=j/q` with `q in k[x]` of degree `U`. Then `U=1` is impossible. If `U=0`, then `q=c in k^*` and `r_7=(j/(8c))x+C` is affine-linear, with a pole at infinity rather than a finite value `r_7(infinity)`. If `U>=2`, then `q=c(x-a)^U` for `c in k^*`, `a in k`, and

```text
r_7 = lambda + gamma (x-a)^{1-U},     gamma = j/(8 c (1-U)) != 0,
div(r_7-lambda) = (U-1)([infinity]-[a]).
```

For `U>2` the source value map has degree `U-1` and branch-value set exactly `{lambda, infinity}`; for `U=2` it has degree one and is unramified.

Let `Z` be an irreducible projective curve, the projective closure of a 1-dimensional component of a fixed-load coefficient fibre met by such a genuine `U>=2` source. Let `X` be its normalization and let

```text
phi: P^1_x -> X
```

be the unique morphism extending the coefficient map through the normalization. Let `R in k(X)` be the function whose pullback is the Faber tail `r_7`. Then `R o phi` is nonconstant, so both `phi` and `R` are nonconstant, `g(X)=0`, and there exist unique points `Q_0,Q_infty in X` and an integer `d>=1` such that, with the same scalar `lambda` as above and with `n=deg(phi)`,

```text
div_X(R-lambda) = d (Q_0 - Q_infty),
d n = U-1,
```

`phi` is totally ramified above `Q_0` and `Q_infty` at `infinity` and `a` respectively, and after coordinates on `X` sending `Q_0,Q_infty` to `0,infinity` one has `R=lambda+delta t^d` with `delta!=0`. If `d>1` the branch-value set of `R` is exactly `{lambda,infinity}`; if `d=1`, `R` is an isomorphism. Likewise `phi` is conjugate to a power map.

If the source coefficient map is known independently to be birational onto `Z`, then `n=1` and the downstairs order is `U-1`. Without birationality only `d n = U-1` is licensed, with `d` a divisor of `U-1`.

A component on which the complete pole divisor of the actual `R` has more than one support point, or on which no scalar `lambda` has fibre a single point of multiplicity `deg(R)`, cannot be met by a genuine `U>=2` source.

This is a terminal necessary condition only. It does not empty order one, impose the first six tails beyond the fixed-load equations, close Taylor/Rees, empty `(8,12)`, prove maximum twelve, or prove JC2.

---

## Attack 1 — source formula, divisor, constants, `U=2`, empty `U=1`, and `U=0`

**CONFIRMED.** Formula `(1.1)` matches the charged primitive `(0.10)` with `C` renamed `lambda`; the complete divisor is `(1.2)`; the `U=2` and `U>2` branch statements are exact; `U=1` is empty; `U=0` is separate.

On the order-one leaf the charged theorem writes `h=q^4`, `u=q in L[x]`, `U=deg q`, and `8 r_7'=j/q` with `j in L^*`. Characteristic zero gives `8!=0`, so rationality of `r_7` is equivalent to existence of a rational primitive of `1/q`. Put `R=(8/j) r_7`, so `R'=1/q`.

**Constants, `U=0`.** If `U=0` then `q=c in k^*`, `R'=1/c`, and `r_7=(j/(8c))x+C`. This is affine-linear, with a simple pole at infinity and `r_7(infinity)=infinity`. There is no finite value `lambda=r_7(infinity)`, so the shape `(1.1)` is not available. The target correctly separates this case from `(1.1)`.

**Simple poles and `U=1`.** A rational derivative never has a simple pole: a pole of `R` of order `m>=1` produces a pole of `R'` of order `m+1>=2`, and a regular `R` has regular derivative. Equivalently, `Res(dR)=0` at every place, while a simple root of `q` gives `Res_a(dx/q)=1/q'(a)!=0`. Thus every root of `q` has multiplicity at least two. Degree one is therefore empty: a linear polynomial has a unique simple root. The target's appeal to the charged emptiness of `U=1` is correct, and the same emptiness re-derives from the residue obstruction without the parent review.

**Pure power, `U>=2`.** Over an algebraic closure let the distinct roots have multiplicities `m_i>=2` with sum `m_i=U` and `N` distinct roots. A rational primitive has a finite pole of exact order `m_i-1` at the `i`-th root and no other finite poles, so as a map `P^1->P^1` regular at infinity it has `deg R=sum(m_i-1)=U-N`. At infinity, `dR/dx=x^{-U}(lc(q)^{-1}+O(x^{-1}))` and `d/dx=-s^2 d/ds` with `s=1/x` force `R` finite at infinity with `ord_infinity(R-R(infinity))=U-1`. A local degree cannot exceed the global degree, so `U-1<=U-N`, hence `N<=1`. A nonconstant polynomial has a root, so `N=1` and `q=c(x-a)^U`. Direct integration gives

```text
r_7 = (j/(8 c (1-U))) (x-a)^{1-U} + C,
```

which is `(1.1)` after renaming `C` to `lambda` and `gamma=j/(8c(1-U))`. The constant is exact: differentiating `lambda+gamma (x-a)^{1-U}` produces `gamma(1-U)(x-a)^{-U}`, and `8 gamma(1-U)=j/c` is the identity `8 r_7'=j/q`. Characteristic zero, `j!=0`, `c!=0`, and `U>=2` give `1-U!=0` and therefore `gamma!=0`. The opposite sign `+j/(8c(U-1))` would reverse the primitive and is incompatible with `1-U` in the exponent.

**Complete divisor `(1.2)`.** With `t=x-a` one has `r_7-lambda=gamma t^{1-U}=gamma t^{-(U-1)}`. On `P^1_x`:

- at `t=0` (the point `a`): order `-(U-1)`, a pole of order `U-1`;
- at infinity, `t=1/s`: order `+(U-1)`, a zero of order `U-1`.

No other zeros or poles. Thus `div(r_7-lambda)=(U-1)([infinity]-[a])`, which is `(1.2)`. Degree zero, as required of a principal divisor. Omitting infinity would leave an affine function with a pole and no zero, which is not the complete principal divisor and would break every later pullback count.

**Branch values of the source value map.** The rational map `r_7:P^1->P^1` has degree `U-1`. In the coordinate `t`, the `t`-derivative is `gamma(1-U)t^{-U}`, which does not vanish at any finite `t!=0`. The only domain points that can ramify are therefore the pole `t=0` (local degree `U-1`) and infinity (local degree `U-1`). These two points are ramified if and only if `U-1>=2`, i.e. `U>=3`, with values `infinity` and `lambda` respectively. For `U>2` the branch-value set is exactly `{lambda,infinity}`. For `U=2` the map has degree one, hence is a Möbius transformation and is unramified; the branch-value set is empty. The target's split is exact, not merely a degree count.

What would have broken `(1.1)`–`(1.2)`: the opposite tail sign in `8 r_7'=j/q`; `gamma` written with `U-1` rather than `1-U` in the denominator; treating `U=0` as a finite `lambda`; a terminal germ at `U=1`; computing `(1.2)` on `A^1` and omitting the zero at infinity.

---

## Attack 2 — extension through the normalization, and nonconstancy of both maps

**CONFIRMED.** A rational coefficient map from the complete source line to a projective curve extends uniquely to a morphism, factors uniquely through the normalization, and nonconstancy of `R o phi` forces both factors nonconstant.

A genuine source supplies a rational map `P^1_x ⇢ Z` into the irreducible projective closure of the coefficient component it meets. The source is a smooth curve and `Z` is proper, so the rational map extends uniquely to a morphism `P^1_x -> Z`. The target's language is a coefficient-*curve* component, and the proof of Section 2 treats `X` as a smooth projective curve, so `dim Z=1` is load-bearing (see Remark 1). A nonconstant morphism from `P^1` to an irreducible projective curve is finite, hence dominant. The source `P^1` is normal, so the universal property of normalization supplies a unique lift `phi:P^1_x -> X` through `nu:X->Z`.

The Faber tail `r_7`, at fixed load, is a rational function of the coefficient coordinates, hence an element `R in k(Z)=k(X)`. Pullback along `phi` recovers the source tail. The identity `8 r_7'=j/q` with `j!=0` and `q` not identically zero forces `r_7'!=0` as a rational function, so `R o phi` is nonconstant. A constant morphism `phi` would make every pullback constant, and a constant function `R` would make every pullback constant. Thus both `phi` and `R` are nonconstant.

No extension is lost at poles of individual affine coordinates: a pole of `a_i` on `P^1` is still a well-defined point of the projective closure `Z`. No base-point of the rational map to affine coefficient space survives after projectivization of the target. Characteristic zero is not required for the extension, only for the nonconstancy of the derivative in the terminal identity (already used).

What would have broken the claim: a non-proper target (affine closure only); a non-dominant map into a higher-dimensional component, which would lift only through the normalization of the image curve, not of `Z`; treating a constant-`r_7` locus as a genuine source.

---

## Attack 3 — singleton support downstairs, equal orders, unique preimages, total ramification, `d n = U-1`

**CONFIRMED.** None of the named failure modes (inseparability, constants, cancellation, singular affine charts, omitted points at infinity) occurs on the complete normal source and target in characteristic zero.

Write `D=div_X(R-lambda)=Z-P` with `Z,P` effective and disjoint (zeros and poles of a single nonconstant rational function). Functoriality of principal divisors along a morphism of smooth complete curves gives

```text
phi^* D = div(R o phi - lambda) = div(r_7-lambda) = (U-1)([infinity]-[a]).
```

The positive and negative parts of the right-hand side are disjoint, so `phi^* Z=(U-1)[infinity]` and `phi^* P=(U-1)[a]`. Explicitly, if `Z=sum_i d_i Q_i` with `d_i>0`, then

```text
phi^* Z = sum_i d_i sum_{phi(P)=Q_i} e_P [P] = (U-1)[infinity].
```

The support of the left-hand side is the union of the fibres `phi^{-1}(Q_i)`. A nonconstant morphism of irreducible projective curves is surjective, so each `Q_i` has nonempty fibre. Therefore there is a single zero `Q_0`, the fibre `phi^{-1}(Q_0)` is `{infinity}`, and the order identity is `d_0 e_{infinity}=U-1`. The same argument at the pole gives a single pole `Q_infty` with unique preimage `a` and `d_infty e_a=U-1`.

A principal divisor has degree zero, so `d_0=d_infty`. Write `d` for the common order. Over an algebraically closed field every residue degree is `1`, and the fundamental equality on a fibre of degree `n` reads `sum e_P=n`. A unique preimage therefore has ramification index `n`. Hence `e_{infinity}=e_a=n` and `d n=U-1`, which is `(2.1)`–`(2.2)` together with total ramification of `phi` above `Q_0` and `Q_infty` at infinity and `a` respectively. In particular `d` is a positive divisor of `U-1`.

**Inseparability.** Characteristic zero makes the function-field extension separable, so Riemann–Hurwitz applies in the tame form used later. The fibre-degree formula `sum e_P f_P=n` itself does not require separability; the algebraic closure already gives `f_P=1`. No purely inseparable phenomenon is available to split a fibre without appearing in the support of `(1.2)`.

**Constants.** If `R` were constant then `R-lambda` would be either identically zero or a unit. Identically zero contradicts `r_7-lambda=gamma t^{-(U-1)}!=0`. A unit has empty divisor, contradicting `(1.2)`. Nonconstancy of `R` was already forced in Attack 2.

**Cancellation.** Suppose extra zeros and extra poles of `R-lambda` pulled back to the same divisor and cancelled. That would be a nonzero divisor `E` on `X` with `phi^* E=0`. For a finite morphism of curves, `phi^*` is injective on divisors: `phi^*[Q]=sum e_P[P]` is a nonempty effective combination. Zeros and poles of a single function are disjoint, so a point of `P^1` cannot map to both a zero and a pole of `R-lambda`. There is nothing to cancel.

**Singular affine charts.** The argument lives on `X`, the normalization of a projective curve over an algebraically closed field, hence a smooth complete curve. Principal divisors are Cartier. Computing poles on a singular model `Z` could merge distinct poles of `X` over a single singular point and under-count support; the target correctly normalizes first. Affine charts of `Z` are not used as the complete model.

**Omitted points at infinity.** The source divisor `(1.2)` already includes the zero at `x=infinity`. The target of `phi` is complete. No point of `X` is missing from the divisor calculus. (The falsifier of Section 4 separately warns about omitted infinities when the test is applied computationally; that is a consumption premise, not a gap in the proof.)

**The scalar `lambda`.** For `U>2` the source function `r_7-lambda'` with `lambda'!=lambda` has `U-1` distinct finite zeros and a single pole, so singleton zero support characterises this particular `lambda`. For `U=2` one has `d n=1`, hence `d=n=1`, and every finite value of a degree-one function has singleton support; the target still correctly takes the same scalar as in `(1.1)`, namely `r_7(infinity)`.

What would have broken the descent: working on `A^1` and losing the zero at infinity; a non-surjective map into a higher-dimensional `X`; residue degree `>1` over a non-closed field; identifying zeros of `R-lambda'` for the wrong scalar when `U>2`.

---

## Attack 4 — genus zero, `R=lambda+delta t^d`, two branch values, degree-one exception

**CONFIRMED.** Genus zero is forced; the displayed coordinate form is exact; the branch-value set of `R` has two elements if and only if `d>1`.

A nonconstant morphism `P^1->X` with `X` a smooth projective curve forces `g(X)=0` by Riemann–Hurwitz: `-2=n(2g-2)+deg Diff`, and `deg Diff>=0` in characteristic zero, so `g>=1` would make the right-hand side nonnegative. Equivalently, `k(X)` embeds in `k(t)` and Lüroth gives rationality. Combined with smoothness one has `X\cong P^1`.

Choose a coordinate `t` on `X` with `t(Q_0)=0` and `t(Q_infty)=infinity` (unique up to scalar). Then `div(R-lambda)=d(Q_0-Q_infty)=d div(t)`, and units on `P^1` are constants, so `R-lambda=delta t^d` with `delta!=0`. This is `(2.3)`. Sending the pole to zero would produce a negative power; the target's choice of coordinates produces the positive power as written.

Now treat `R:P^1->P^1` of degree `d`. In this coordinate `R'=d delta t^{d-1}`. Characteristic zero gives `d!=0`.

- If `d=1`, then `R'` is a nonzero constant, `R` is a Möbius transformation, hence an isomorphism, and the branch-value set is empty.
- If `d>1`, the only finite critical point is `t=0`, with value `lambda` and local degree `d`. At infinity, `t=1/s` gives `R=lambda+delta s^{-d}`, a pole of order `d` and value `infinity`. These two local degrees already equal the global degree, so there is no other ramification. The values `lambda` (finite) and `infinity` are distinct. The branch-value set is exactly `{lambda,infinity}`.

No Chebyshev-type exception is available. A polynomial Chebyshev map of degree `>=3` has two finite critical values *and* a pole at infinity, hence three branch values. Riemann–Hurwitz for a degree-`d>=2` map `P^1->P^1` gives total ramification `2d-2`. Two fibres contribute `2d-(r_1+r_2)` if those are the only ramified fibres, so `r_1+r_2=2`, hence each of the two branch values has a unique preimage. That is the power-map type, not a dihedral type. The degree-one exception is therefore the only exception, and it is stated.

The same Riemann–Hurwitz count applied to `R` itself shows that `(2.1)` already forces `g(X)=0` even without the map from `P^1`: ramification at least `2(d-1)` from the two totally ramified points gives `2g-2>=-2d+2d-2=-2`, hence `g=0` with no leftover ramification. Item 1 of Section 2 is consequently redundant with `(2.1)`, but it is not false: it is the cheaper conclusion from `phi` alone.

What would have broken `(2.3)`: placing `Q_infty` at `0`; claiming two branch values when `d=1`; claiming that Chebyshev maps give a second isomorphism type with at most two branch values on `P^1`.

---

## Attack 5 — `phi` is conjugate to a power map: full Riemann–Hurwitz count

**CONFIRMED.** The two visible total-ramification points consume the entire ramification budget; no third ramified point is possible; the classification is a power map.

From Attack 3, `phi:P^1->X\cong P^1` has degree `n` and is totally ramified at `infinity` over `Q_0` and at `a` over `Q_infty`. Riemann–Hurwitz on the source, using `g(X)=0`, reads

```text
-2 = n(-2) + sum_P (e_P-1),
```

so the different has degree `2n-2`. The contribution of a tame ramification point of index `e` is `e-1`. The two known points contribute `(n-1)+(n-1)=2n-2` and saturate the budget. Any further point with `e_P>=2` would add at least `1` and overshoot. Characteristic zero excludes wild ramification. Therefore `phi` is unramified away from `{a,infinity}`.

A degree-`n` morphism `P^1->P^1` that is totally ramified above two points and unramified elsewhere is conjugate to `z |-> z^n`. Concretely: the coordinates of `(2.3)` send `Q_0,Q_infty` to `0,infinity`, and the source coordinate `t=x-a` sends `a,infinity` to `0,infinity`; then `t_X o phi` has a zero of order `n` at infinity and a pole of order `n` at `a`, hence equals `c (x-a)^{-n}`. After possibly inverting the target coordinate this is a positive power. For `n=1` the map is an isomorphism, which is a power map of degree one, and the ramification budget is `0=0`.

The target's last sentence of the Section 2 proof — that the two total-ramification points consume the entire ramification of `phi` — is exactly this count, not an inspection of only the two points without a budget. The full count is charged and closes.

What would have broken the classification: using only the two visible points without comparing to `2n-2`; characteristic `p` dividing `n`; identifying `Q_0` with `Q_infty`.

---

## Attack 6 — overstrong downstairs exponent `U-1`, and the degree firewall

**CONFIRMED.** The overstrong form `(3.1)` is not derivable without birationality; only `d n=U-1` is licensed in general.

The composition formula for degrees of rational functions is `deg(R o phi)=deg(R) deg(phi)`. The left-hand side is `deg(r_7)=U-1` by `(1.2)`, and `deg(R)=d` by `(2.1)`, which is the same identity `d n=U-1`. Nothing in the divisor calculus, the function-field inclusion `k(X) subset k(P^1)`, or the power-map shape of `R` eliminates `n`. A genuine source may well be invariant under `x |-> a+zeta(x-a)` for an `n`-th root of unity, in which case the coefficient map factors through a degree-`n` cover and `d=(U-1)/n`.

If the source coefficient map is independently known to be birational onto `Z`, then the map `P^1->Z` has degree one. Normalization is birational, so `n=1` and `(2.1)` strengthens to `(3.1)`. Without that extra input, `(3.1)` on the coefficient normalization is false in general. The target's Section 3 firewall is therefore necessary, and is the exact conclusion licensed by the argument. The full order `U-1` always holds on the source line, as `(1.2)` records, and is not in dispute.

Trying to promote `d=U-1` by uniqueness of `lambda`, by genus zero, or by the power shape of `R` does not work: all of those hold for every divisor `d` of `U-1`. The distinction is essential when consuming a modular plane projection or a non-birational invariant quotient, as the target states.

---

## Attack 7 — component falsifier, and premises needed to consume a modular projection

**CONFIRMED.** The five-step screen is a valid necessary condition on any 1-dimensional component met by a genuine `U>=2` source. Survival is not sufficiency. Every listed consumption premise is load-bearing.

**Steps 3–4 are necessary.** By `(2.1)`–`(2.3)`, the actual function `R` on the normalization has a unique pole, and there is a scalar `lambda` for which the fibre `R=lambda` is a single point of multiplicity `deg(R)=d`. A component whose complete pole divisor has two or more support points cannot be met by such a source. A constant `R` has empty pole divisor, so it is not rejected by step 3, but step 4 rejects it: the fibre `R=lambda` is either empty or the whole curve, not one point of multiplicity `deg(R)`. A Weierstrass-type function with a unique pole but two zeros of `R-lambda` for every finite `lambda` is rejected by step 4, not by step 3.

**Step 5 is equivalent on a rational parametrization.** After `g(X)=0`, “more than two branch values” is equivalent to failure of `(2.3)`, with the degree-one exception (empty branch-value set) stated in Section 2. Riemann–Hurwitz as in Attack 4 excludes a Chebyshev-type survivor with exactly two branch values of non-power type. Applying step 5 without a rational parametrization is not licensed; steps 3–4 do not require one.

**The optional degree check.** If `n=deg(phi)` is known, `deg(R) n=U-1` is `(2.2)` and is necessary. If `n` is unknown, the check is correctly withheld.

**“Later genus or Taylor/Rees.”** A survivor of steps 3–4 already satisfies `(2.1)`, hence already has genus zero by Attack 4. A later genus test on the same curve is redundant as a rejection tool, but it is not claimed to be independent, and Taylor/Rees is a different test. The sentence is a cost-ordering comment, not a promotion of survivors to sources.

**Premises required to consume a modular projection.** None of the following is supplied by the present note, and each can produce a false rejection or a false survival if omitted.

1. *Actual component.* The object tested must be an irreducible component of the actual coefficient fibre, not a union, not an embedded component, and not a plane image that mixes components. A non-birational plane projection can merge poles or split them; Section 3 already flags this.
2. *Exact normalization.* Pole support must be computed on the normalization of the component, not on a singular projective model (which can merge poles over a singularity and fail to reject) and not on the normalization of a plane eliminant (whose function field may be a proper subfield). The probe parent already forbids calling a plane arithmetic genus a normalization genus; the same warning applies to pole divisors.
3. *Complete graph of the actual `r_7`.* The function tested must be the Faber tail `r_7` on that component, not a linear plane coordinate, not a truncation, and not a different graph variable. A random rational function on a rational curve can easily have one pole; that is not `(2.3)`.
4. *Chart complements.* Poles may live on a chart complement (the probe parent splits `a_6!=0` from `a_6=0` and forbids treating either as coverage). Incomplete charts miss poles (false survival) or miss that two affine pieces are the same component. The target's step 2 explicitly includes “all points at infinity and chart complements.”
5. *Characteristic-zero lift.* A modular component need not lift. In characteristic `p` the derivative identities, the equality `ord(f')=ord(f)-1`, and tame Riemann–Hurwitz all fail when `p` divides a local order, `p` divides `U-1`, or `p=2` (the factor `8`). A mod-`p` power map can be purely inseparable. Rejecting a modular component does not reject a characteristic-zero component it does not lift from; surviving one does not produce a characteristic-zero source. Section 5 already records this.

With those premises, the falsifier is a correct necessary screen. Without them it is not a theorem about the characteristic-zero source tree.

---

## Attack 8 — terminal-only scope

**CONFIRMED.** No order-one emptiness, Taylor/Rees closure, `(8,12)` emptiness, maximum-twelve, or JC2 claim slips through.

The note consumes only the terminal row and the order-one classification of `q`. It does not solve `r_1'=cdots=r_6'=0` beyond the standing fixed-load equations that cut the fibre, does not produce the remaining Faber coefficients, does not impose either original Taylor-boundary family, polynomiality, or a strict Rees boundary, and does not assert that any coefficient fibre is empty. Section 4's “later genus or full Taylor/Rees test” is deferred work, not a conclusion. The title names the cell `(8,12)` as the ambient terminal identity `8 r_7'=j/q`; it does not empty the cell. Maximum twelve and JC2 are unmentioned as claims. Section 5 matches this boundary: no modular lift, no birationality of a plane projection, no completeness of retained components, and no source-map degree one are obtained.

The charged theorem's converses (every pure-power `q` of degree `U>=2` has a rational terminal primitive) are existence of a primitive of `1/q`, not existence of a genuine Keller source on that core, and are not promoted here.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | `(1.1)` with `gamma=j/(8c(1-U))!=0`; complete divisor `(1.2)`; `U>2` has branch values `{lambda,infinity}`; `U=2` degree one unramified; `U=1` empty; `U=0` affine-linear and separate | **CONFIRMED** | opposite tail sign; `U-1` rather than `1-U` in the denominator of `gamma`; divisor computed on `A^1`; a rational primitive of `1/(x-a)`; treating `U=0` as a finite `lambda` |
| 2 | Rational map `P^1->Z` extends and factors uniquely through the normalization; `R o phi` nonconstant forces both nonconstant | **CONFIRMED** | affine (non-proper) target; constant tail admitted as a genuine source; a non-dominant map into a higher-dimensional component treated as a map onto `Z` |
| 3 | Singleton pullback support forces singleton support downstairs, `d_0=d_infty=d`, unique preimages, `e=n`, and `d n=U-1` | **CONFIRMED** | cancellation in `phi^*`; omitted zero at infinity; residue degree `>1`; inseparable splitting in characteristic `p`; computing on a singular model |
| 4 | `g(X)=0`; `R=lambda+delta t^d`; branch-value set `{lambda,infinity}` iff `d>1`; `d=1` an isomorphism | **CONFIRMED** | pole placed at `0`; two branch values claimed for `d=1`; a Chebyshev-type second isomorphism class with `<=2` branch values on `P^1` |
| 5 | Two total-ramification points of `phi` saturate `2n-2`; `phi` conjugate to a power map | **CONFIRMED** | ramification budget not charged; a third ramified point compatible with Riemann–Hurwitz in characteristic zero |
| 6 | Without birationality, `(3.1)` is too strong; only `d n=U-1` is licensed | **CONFIRMED** | a hidden identification `n=1`; degree formula `deg(R o phi)=deg(R)deg(phi)` failing |
| 7 | Falsifier is a valid necessary screen; modular consumption needs actual component, exact normalization, actual `r_7`, chart complements, and a characteristic-zero lift | **CONFIRMED** | treating survival as sufficiency; testing a plane eliminant or a single affine chart; applying the screen in characteristic `p` dividing `U-1` as if it were characteristic zero |
| 8 | Terminal necessity only; no order-one emptiness, Taylor/Rees, `(8,12)`, maximum twelve, or JC2 | **CONFIRMED** | a hidden promotion in the status line, Section 4, or Section 5 |

---

## Remarks (non-blocking)

1. Dimension one is load-bearing and is carried by the words “coefficient-curve,” “genus,” and “smooth projective curve `X`.” If a component of dimension `>=2` is met by a genuine source, the necessary condition is that the image curve (the closure of `phi(P^1)`, then its normalization) satisfy `(2.1)`–`(2.3)`, not that `R` as a function on the whole component have two-point divisor support. Dimension zero cannot meet a nonconstant source. This is a scoping remark, not a numbered failure.
2. For `U=2` the downstairs data are forced: `d n=1` implies `d=n=1`, so both `R` and `phi` are isomorphisms. The degree-one exception on `R` is then automatic, not an extra case.
3. The genus-zero item in Section 2 is implied by `(2.1)` as well as by the existence of `phi`. Harmless redundancy.
4. “Conjugate to a power map” for `phi` includes the possibility `t |-> c t^{-n}` before inverting the target coordinate, matching `phi(infinity)=Q_0` and `phi(a)=Q_infty`. Not a second isomorphism type.
5. Characteristic zero is essential and present: `8!=0`, `U-1!=0` in the primitive, `ord(f')=ord(f)-1`, tame Riemann–Hurwitz, and `d!=0` in `R'`.
6. Geometric irreducibility is implicit in working over an algebraically closed field. An `L`-irreducible component that splits after scalar extension must be tested on its geometric irreducible components. No loss for the geometric necessary condition, as the target states.

None of these remarks changes a numbered verdict.

---

## Strict scope firewall

This review confirms a terminal necessary condition: on a 1-dimensional fixed-load coefficient component met by a genuine order-one source with `U>=2`, the normalization is rational and the actual `r_7` function is a power in the stated coordinates, with `d n=U-1`. It does **not**:

- empty the order-one leaf, or convert the charged emptiness of `U=1` into emptiness of a coefficient fibre;
- solve `r_1'=cdots=r_6'=0` beyond the fixed-load equations that define the fibre, or determine those six constants;
- impose either original Taylor-boundary family, a strict Rees boundary, polynomiality of a reconstructed pair, or existence of a Keller pair;
- prove that a modular component lifts to characteristic zero, that a plane projection is birational, that every source component was retained, or that a source map has degree one;
- close `(8,12)`, bound maximum twelve, or speak to JC2.

The target's own Section 5 matches this boundary. No creep was found.

---

## Terminal boundary (accepted, not enlarged)

```text
source_formula_1.1_and_divisor_1.2=PROVED
U=2_degree_one_unramified=PROVED
U=1_empty_U=0_separate=PROVED
extension_through_normalization=PROVED
both_phi_and_R_nonconstant=PROVED
singleton_descent_and_d*n=U-1=PROVED
g(X)=0_and_R=lambda+delta_t^d=PROVED
branch_values_two_iff_d>1=PROVED
phi_power_map_RH_saturated=PROVED
downstairs_order_U-1_only_if_n=1=PROVED
falsifier_necessary_not_sufficient=PROVED
modular_lift_birational_projection=NOT_CLAIMED
other_six_tails=NOT_SOLVED
Taylor_Rees_polynomiality=NOT_CLAIMED
order_one_empty=false
(8,12)_empty=false
maximum_twelve=NOT_CLAIMED
JC2=NOT_CLAIMED
```
