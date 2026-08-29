# Hostile different-model review — Lemma AS-TRI (one-sided target `y`-degree)

| Field | Value |
|---|---|
| Claim under review | Derived Lemma AS-TRI in `xmodel/ideation-20260826T2350Z-crosspollination-opus5.md` §2.4: if `P=x-x^{109}+109A`, `Q=y+109B` lie in `Z_{109}[x,y]` and `det J(P,Q)=1`, then `deg_y(Q)>=2`, equivalently `deg_y(B)>=2` |
| Overall verdict | **CONFIRMED** |
| Separate §2.5 criterion | **CONFIRMED** as an integrality biconditional; the sentence "fails at `v_{109}(c)=0`" is a non-blocking wording defect and is **not** consumed |
| Smallest missing hypothesis | none that breaks the lemma (non-blocking precisions below; none is a hidden extension, a completion, or a two-sided no-go in disguise) |
| Evidence tier | independent hand algebra over the DVR `Z_{109}` and the rational function field `Q_{109}(x)`: Gauss valuation, exact `y^m` Jacobian coefficient, kernel of `d/dx`, integrality and residue of the target shear, induction, polynomial-degree contradiction. No CAS, no enumerator, no AWS, no `jc2-lean` |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (Opus 5 / Anthropic) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Review window (UTC) | 2026-08-27T00:45:17Z |
| Host | hand algebra only |

Producer and controlling inputs reread in full before any verdict:

- `xmodel/ideation-20260826T2350Z-crosspollination-opus5.md` §§2.2, 2.4, 2.5, 2.8--2.10 (SHA-256 `e645d822aa49199b69464f98b7b94846e6773e635bd389cb94a3a24806a3e341`)
- `xmodel/as109-support-gate-20260824.md` (SHA-256 `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5`) and different-model review `xmodel/as109-support-review-grok-20260824.md` (SHA-256 `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8`), Claim 6 only as typing of the seed, not as a logical input to AS-TRI
- carry erratum `xmodel/as109-support-gate-20260824-erratum.md` (SHA-256 `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb`) and `xmodel/as109-carry-erratum-review-grok-20260824.md` (SHA-256 `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212`), only to confirm that Hensel and the packed exact identity are independent of truncated digit bookkeeping; AS-TRI uses `det J=1` exactly
- `xmodel/as109-max11-floor12-composition-opus5-20260826.md` (SHA-256 `c76f26a6407a0e321da7d7001455819bd9ca92be6cc467afe5045aacc310c9be`) and `xmodel/as109-max11-floor12-composition-review-sol-20260826.md` (SHA-256 `430ffa3cc25a3141a03062072db4fecab0a3b6250daab3323c7b74194bfb9e84`), T3 as the two-sided floor, not consumed
- `xmodel/as109-partial-y-history-stop-20260824.md` (SHA-256 `6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe`) and `xmodel/as109-partial-y-history-review-grok-20260824.md` (SHA-256 `f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd`), only for the duplication check

No producer, canonical, ledger, freeze, or case file was edited. No web access, no AWS mutation, no heavy local computation, no `jc2-lean` access. Only this file was written.

Write `p=109`, `R=Z_{109}` the complete DVR of 109-adic integers, `K=Q_{109}` its fraction field (characteristic zero), `J(P,Q)=P_x Q_y-P_y Q_x`, and `v` the Gauss valuation on `R[x]` (minimum of the coefficient valuations). Gauss's lemma makes `v` a valuation on `K[x]`, hence on `K(x)` by `v(f/g)=v(f)-v(g)`. Units of `R[x]` are `R^\times`. The residue field is `F_{109}`; polynomial reduction `R[x]\to F_{109}[x]` is not the same as the function `a\mapsto a-a^{109}` on `F_{109}`-points.

---

## Promotion

**Accept Lemma AS-TRI at the stated scope.**

Let `P=x-x^{109}+109A` and `Q=y+109B` lie in `R[x,y]` with `det J(P,Q)=1`. Then `deg_y Q>=2`, equivalently `deg_y B>=2`.

The argument is elementary, stays inside `R[x,y]`, and does not use Hensel noninjectivity, T1, T3, or any two-sided degree no-go.

**Do not promote this to:** a bound on `deg_y A`; a two-sided floor; T3; a max-12 routing; an `n>=2` integral Abhyankar step; a residue-shape statement after a unit-coefficient shear; a series lift; existence or nonexistence of an AS109 lift; a support bound; a marked collision; a characteristic-`109` theorem; a JC2 decision.

**Do not treat §2.5's monicization/Frobenius paragraph as reviewed.** Only the displayed integrality biconditional of §2.5 is confirmed below, separately, and it is not a logical input to AS-TRI.

---

## Quarantine

No result here proves or disproves JC2. AS-TRI is conditional on an exact integral polynomial lift in the displayed coordinates; it asserts none. Digit carries, marked sections, and the frozen support grammar are irrelevant. The Hensel nonautomorphy lemma is not consumed: the contradiction is a polynomial `x`-degree, not noninjectivity. Producer language "derived-here, unreviewed" is discharged by this review and is not evidence.

---

## Scope (not enlarged)

One prime `p=109`, coefficient ring `R=Z_{109}` (not `F_{109}`, not `Z/109^k`, not a series ring), polynomial maps, exact `det J=1`. Arbitrary finite `x`-degree is in scope. The `y`-degree is the polynomial degree in `R[x][y]`, which agrees with the degree over `K` because `p` is not a zero-divisor. Source changes are not used. Target shears that appear are constant-coefficient and integral, with integral inverses.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Seed shape forces Gauss `(F1)/(F2)`: `v(p_j)>=1` for `j>=1`; `v(q_j)>=1` for `j>=2`; `v(q_1)=0` and `q_1\equiv 1\pmod{109}`. `deg_y Q=0` is impossible. Equivalence `deg_y Q>=2\Leftrightarrow deg_y B>=2` holds in `R[x,y]` | **CONFIRMED** | `p` annihilating a leading coefficient; `q_1\equiv 0\pmod{109}`; `1+109\beta_1=0` in `R[x]`; reading `Z_{109}` as `F_{109}` |
| 2 | Under `deg_y Q=1`, the coefficient of `y^m` in `J` is exactly `p_m' q_1-m p_m q_1'`, with no `q_0` or lower-`P` contribution | **CONFIRMED** | a leftover `y^{m+1}` or a `y^m` summand from `p_{m-1}` or `q_0'` |
| 3 | That identity is `(p_m/q_1^m)'=0` in `K(x)`. Kernel of `d/dx` on `K(x)` is `K`. So `p_m=c q_1^m` with `c\in K`. No nonconstant unit of `R[x]` is used; `q_1` is not inverted in `R[x]` | **CONFIRMED** | `ker(d/dx)` larger than `K` (would need char `p`, or a series/analytic category); `q_1=0`; the ratio a nonconstant rational function with vanishing derivative |
| 4 | Gauss gives `v(c)=v(p_m)-m v(q_1)=v(p_m)>=1`, hence `c\in 109 R`. The identity `p_m=c q_1^m` therefore holds in `R[x]`. Multiplicativity is Gauss, not the valuation of leading `x`-coefficients. The case `p\mid m` does not break this: `m\neq 0` in `K`, and `R[x]` is a domain | **CONFIRMED** | Gauss failing to be multiplicative on `R[x]`; content of `q_1` positive; `c` of negative valuation; `m=0` in `K` |
| 5 | Target shear `(u,v)\mapsto(u-c v^m,v)` is an `R`-automorphism of Jacobian `1`, inverse `(u,v)\mapsto(u+c v^m,v)`. `P'=P-c Q^m` lies in `R[x,y]`, has strictly smaller `y`-degree, and `P'\equiv P\equiv x-x^{109}\pmod{109}`. `Q` is unchanged. The reduced shear is the identity on `A^2_{F_{109}}`. Induction terminates | **CONFIRMED** | `c` not integral; `Q^m` contributing a second `y^m` term; residue of `c Q^m` nonzero; a new higher `y`-power; infinite descent |
| 6 | At `m=0`, `p_0' q_1=1` in `R[x]` forces both factors to be constant units, so `p_0=ax+b` with `a\in R^\times`. Polynomial congruence `p_0\equiv x-x^{109}\pmod{109}` has `x^{109}`-coefficient a unit, degree `109`. Contradiction. This is polynomial degree in `F_{109}[x]`, not the zero function `a-a^{109}` on `F_{109}`-points | **CONFIRMED** | a nonconstant unit of `R[x]`; `p_0'` of degree `0` in char `109` while `deg p_0=109` (the residue-field ghost); treating Fermat as a polynomial identity |
| 7 | AS-TRI is not a duplicate of T3, nor of any charged two-sided correction no-go. Combined with T3 it kills the floor branches `(12,<=1)`. A classical automorphy route via history-stop `gcd<=2` plus Hensel exists and is not consumed | **CONFIRMED** | T3 already excluding `deg_y B<=1`; the lemma using Hensel or a two-sided bound as a load-bearing step |
| 8 | §2.5 criterion `v(p_m)>=(m/n) v(q_n)` iff the Abhyankar step at `n\mid m` is `109`-integral, is correct over `R` and is independent of AS-TRI. The phrase "fails at `v(c)=0`" is false relative to that iff | **CONFIRMED** (iff) / wording defect (non-blocking) | `p_m/q_n^{m/n}` leaving `K`; `Q^{m/n}` not a polynomial; Gauss cancellation making `v(q_n^r)>r v(q_n)`; the iff using `v(c)=0` as failure of integrality |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Independent proof of AS-TRI

Let `P,Q\in R[x,y]` with `P=x-x^{109}+109A`, `Q=y+109B`, and `J(P,Q)=1`. Write

```text
P = sum_{j>=0} p_j(x) y^j,     Q = sum_{j>=0} q_j(x) y^j,
```

with `p_j,q_j\in R[x]`. Comparing with the seed,

```text
p_0 = x-x^{109}+109 \alpha_0,   p_j = 109 \alpha_j  (j>=1),
q_0 = 109 \beta_0,             q_1 = 1+109 \beta_1,   q_j = 109 \beta_j  (j>=2).
```

Thus `v(p_j)>=1` for every `j>=1` that actually occurs, `v(q_j)>=1` for every `j>=2`, and `v(q_1)=0` with `q_1\equiv 1\pmod{109}` as polynomials. In particular the coefficient of `y` in `Q` cannot vanish: `v(1+109\beta_1)=0`. So `deg_y Q>=1`.

If `deg_y B>=2` then `deg_y(109B)>=2` because `109\neq 0` in the domain `R`, hence `deg_y Q>=2`. Conversely a `y`-power `>=2` in `Q` can come only from `109B`. It remains to rule out `deg_y Q=1`.

Assume `Q=q_1 y+q_0`. Proceed by induction on `m=deg_y P`.

**If `m>=1`.** Expand

```text
P_x = p_m' y^m + lower,     P_y = m p_m y^{m-1} + lower,
Q_x = q_1' y + q_0',        Q_y = q_1.
```

Then `P_x Q_y` and `P_y Q_x` both have `y`-degree exactly `m`. The coefficient of `y^m` in `J` is

```text
p_m' q_1 - m p_m q_1'.
```

The `q_0'` term and every coefficient of `P` below `p_m` land in `y^{m-1}` or lower. Since `J=1`, that coefficient is `0` in `R[x]`. In `K(x)` one has `q_1\neq 0` and

```text
(p_m / q_1^m)' = (p_m' q_1 - m p_m q_1') / q_1^{m+1} = 0.
```

The kernel of `d/dx` on `K(x)` is `K` (characteristic zero). Thus `p_m=c q_1^m` for some `c\in K`. Gauss multiplicativity gives

```text
v(c) = v(p_m) - m v(q_1) = v(p_m) >= 1,
```

so `c\in 109 R\subset R` and the equality `p_m=c q_1^m` holds in `R[x]`. (If `109` divides the integer `m`, still `m\neq 0` in `K`, and the Wronskian identity is exact in the domain `R[x]`, not merely residual.) The target automorphism

```text
\sigma(u,v) = (u - c v^m, v)
```

has Jacobian `1` and inverse `(u,v)\mapsto(u+c v^m,v)`, both defined over `R`. Set `P'=P-c Q^m`. Then `P'\in R[x,y]`, `J(P',Q)=1`, and the unique `y^m` term of `Q^m` is `q_1^m y^m`, so the `y^m` coefficient of `P'` is `p_m-c q_1^m=0`. Thus `deg_y P'<m`. Moreover `v(c)>=1`, so `c Q^m\equiv 0\pmod{109}` and `P'\equiv P\equiv x-x^{109}\pmod{109}`. The reduced map `\overline{\sigma}` is the identity, so `(P',Q)` is again an exact integral AS109 lift. Repeat. Each step strictly lowers a nonnegative integer degree, so the process terminates at `m=0`.

**If `m=0`. ** Now `P=p_0(x)` and `J=p_0' q_1=1` in `R[x]`. Both factors are units of `R[x]`, hence constant units: `p_0=ax+b` with `a\in R^\times`. But

```text
p_0 \equiv x-x^{109} \pmod{109}
```

in `R[x]`. The coefficient of `x^{109}` on the right is `-1` plus an element of `109 R`, hence a unit, so `deg_x p_0=109`. Contradiction.

Therefore `deg_y Q>=2` and `deg_y B>=2`.

---

## Checkpoint attacks

### Gauss valuation of leading coefficient polynomials

The quantity `v(p_m)` is the Gauss valuation of the polynomial `p_m\in R[x]`, not the 109-adic valuation of its leading `x`-coefficient. A mixed-valuation example such as `p_m=109+(109 x)` still has Gauss valuation `>=1`; the identity `p_m=c q_1^m` never produces a Gauss mismatch because `v` is a valuation. Primitivity of `q_1` is exactly `v(q_1)=0`, which is `(F2)`. No leading coefficient of `P` in `y` can be the zero polynomial: `m` is the actual `y`-degree. Reduction modulo `109` can and does kill every `y^{>=1}` coefficient of `P`; that is `(F1)`, and it is why `v(c)>=1` rather than merely `>=0`.

### Coefficient of `y^m`

Direct expansion, recorded in the proof. Under `deg_y Q=1` there is no `y^{m+1}` in `J`. The formula is the `n=1` case of the classical top Jacobian identity `n a_m' b_n-m a_m b_n'` from the history stop, specialised to `n=1`, `b_1=q_1`.

### Differential-constant inference

This step lives in `K(x)`, characteristic zero. It would fail over `F_{109}(x)`: the kernel of `d/dx` is then `F_{109}(x^{109})`, and separately `m` may vanish. The lemma is not claimed over the residue field. Over `K(x)` a rational function with vanishing derivative is a constant in `K`; there are no nonconstant units of `K[x]` to hide in. The polynomial `q_1` may be nonconstant (e.g. `1+109 x`); it is then not a unit of `R[x]`, and is not inverted in `R[x]`. The only inversion is in `K(x)`, after which `p_m=c q_1^m` restores a polynomial identity.

### Integrality and residue of the repeated target shear

`v(c)>=1` puts `c` in `109 R`, so `\sigma` and `\sigma^{-1}` are `R`-points of `Aut`. The shear is constant-coefficient in the target coordinates; it is not the illegal `x`-dependent operation `P\mapsto P-(p_m/q_1^m) Q^m` before constancy is proved. Residue: `\overline{\sigma}=\mathrm{id}`, so the seed shape is strictly preserved, not merely up to an `F_{109}`-automorphism. This is stronger than integrality, which would already follow from `v(c)>=0`.

### Termination

A strictly decreasing sequence of nonnegative integers. `Q` is never changed, so `(F2)` is inherited. Each new `P'` still satisfies `(F1)` by residue preservation.

### Final polynomial-degree contradiction

`p_0' q_1=1` in `R[x]` is degree-additive over `K[x]` as well: both degrees vanish. The contradiction is not "a degree-`109` polynomial cannot have derivative a unit in characteristic `109`". In characteristic `109` one has `(x^{109})'=0`, so `x-x^{109}` itself would satisfy `(x-x^{109})'\cdot 1=1` and would be a counterexample. That ghost is exactly the residue map, and it is why the coefficient ring must be `R` (or `K`) and not `F_{109}`. As polynomials over `R` or over `F_{109}`, `x-x^{109}` has degree `109` and leading coefficient a unit. Fermat's identity `a^{109}=a` on `F_{109}`-points does not make `x^{109}-x` the zero polynomial.

The producer's "so `deg_x p_0<=1`" is slightly loose: `p_0'=0` is already excluded by `J=1`, so the degree is exactly `1`. Non-blocking.

---

## Section 2.5, separately

The displayed criterion is: at an Abhyankar step with `n\mid m`, writing `r=m/n` and `c=p_m/q_n^r`,

```text
P \mapsto P - c Q^r    is 109-integral    <=>    v(p_m) >= r v(q_n).
```

**The biconditional is correct**, and it does not depend on AS-TRI.

Derivation, independent of §2.4. The top Jacobian identity is `n p_m' q_n-m p_m q_n'=0` in `R[x]`. Since `R[x]` is a domain and `n\neq 0` in `K`, this is `p_m' q_n-r p_m q_n'=0`, i.e. `(p_m/q_n^r)'=0` in `K(x)`. Here `q_n^r` is an ordinary polynomial power (`r` is an integer); no radical extension of `K[x]` is required. The kernel of `d/dx` again gives `c\in K` with `p_m=c q_n^r`. Gauss multiplicativity converts `v(c)>=0` into the displayed inequality. For `c\in R` the polynomial `P-c Q^r` has coefficients in `R`; if `v(c)<0` it does not. The leading `y^m` term of `Q^r` is uniquely `q_n^r y^m`.

For `n=1`, `v(q_1)=0`, so integrality is `v(p_m)>=0`, which is automatic for `p_m\in R[x]`. Residue preservation is the stronger `v(p_m)>=1`, from `(F1)`, and is what §2.4 uses. The producer sentence "for `n=1` this is automatic (`v(q_1)=0`, `v(p_m)>=1`) — that is exactly AS-TRI" therefore bundles three distinct facts (integrality, residue preservation, the `m=0` contradiction). The first two are the `n=1` engine of AS-TRI; they are not the theorem.

For `n>=2`, `(F2)` gives `v(q_n)>=1`. The inequality can fail (`v(c)<0`), in which case the step is defined over `K` but not over `R`.

**Wording defect, non-blocking.** The producer writes: "when it fails at `v_{109}(c)=0` the reduction remains defined but the reduced map changes". Relative to the displayed iff, `v(c)=0` is **success** of integrality (equality), not failure. The correct split is:

- `v(c)<0`: not `R`-integral; defined over `K`; residue shape is not even a statement over `R`;
- `v(c)=0`: `R`-integral, `c` a unit, residue shape becomes `\overline{P}-c\bar Q^r`, an AS-twisted map;
- `v(c)>=1`: `R`-integral and residue-shape-preserving.

That split is already what §2.5 items 1--3 say in prose. The one sentence is wrong. It does not infect the iff, and it does not infect AS-TRI.

**This valid criterion was not used to rescue AS-TRI.** AS-TRI was checked on the six steps of §2.4. Even a correct `n=1` integrality criterion does not give the `m=0` degree contradiction by itself.

The later monicization / Frobenius-additivity paragraph of §2.5 cites AS-TRI and is outside this review.

---

## Duplication against charged two-sided no-gos

T3 (`c76f26a6...` / `430ffa3c...`) says: conditionally on an exact integral lift, `max(deg_y A, deg_y B)>=12`. This permits the branches `(12,0)` and `(12,1)`. AS-TRI kills both. It is therefore strictly one-sided and not implied by T3.

The quadratic/cubic/quartic/... correction no-gos bound **both** `y`-degrees. A pair with `deg_y B<=1` and large `deg_y A` is outside all of them.

The history stop's recorded AS109 corollary is: a lift cannot have **maximum** actual `y`-degree at most eight. Again two-sided.

**Classical alternative route, not consumed.** The history stop's field theorem (confirmed) says that every characteristic-zero Keller pair with `gcd(deg_y P, deg_y Q)<=2` is an automorphism, and the case `n=1` is included (`m,n>0`; after the large source shear both total degrees are at least `2` and the total gcd may be chosen prime). Hensel then says an AS109 lift is not an automorphism. Composing those two charged facts yields the conclusion of AS-TRI. That composition is not a charged AS109 corollary, uses source shears that destroy the seed residue, and uses Hensel. The proof under review uses neither. Confirming AS-TRI therefore does not double-count a two-sided no-go; it records an elementary Hensel-free integral-target-shear proof and a one-sided constraint T3 does not supply. No novelty claim against Magnus / Moskowicz / the history stop is licensed.

---

## Non-blocking remarks

1. `deg_x p_0<=1` should be `deg_x p_0=1`. The constant subcase is `J=0`.
2. Identifying the `n=1` case of the §2.5 criterion with AS-TRI is sloppy prose; the theorem is that criterion plus termination plus the degree-`109` contradiction.
3. `P'=P-0=x-x^{109}\pmod{109}` in the producer writeup means `P-c Q^m` with `c\equiv 0\pmod{109}`. Informal, not false.
4. The lemma is false if `Z_{109}` is read as `F_{109}`: `(x-x^{109},y)` itself would be a counterexample. The campaign's typing, T2, and the use of `Q_{109}` all fix the 109-adic integers. State the ring when composing.

---

## Hashes

Recomputed SHA-256 on the charged tree:

| Artifact | SHA-256 |
|---|---|
| `xmodel/ideation-20260826T2350Z-crosspollination-opus5.md` | `e645d822aa49199b69464f98b7b94846e6773e635bd389cb94a3a24806a3e341` |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` |
| `xmodel/as109-support-review-grok-20260824.md` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` |
| `xmodel/as109-carry-erratum-review-grok-20260824.md` | `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212` |
| `xmodel/as109-max11-floor12-composition-opus5-20260826.md` | `c76f26a6407a0e321da7d7001455819bd9ca92be6cc467afe5045aacc310c9be` |
| `xmodel/as109-max11-floor12-composition-review-sol-20260826.md` | `430ffa3cc25a3141a03062072db4fecab0a3b6250daab3323c7b74194bfb9e84` |
| `xmodel/as109-partial-y-history-stop-20260824.md` | `6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe` |
| `xmodel/as109-partial-y-history-review-grok-20260824.md` | `f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd` |

---

## Firewall / nonclaims

```text
ALLOWED:  AS-TRI as a one-sided constraint deg_y B >= 2 on exact integral
          polynomial AS109 lifts; composition with T3 to kill (12, <=1)
          at the floor; the §2.5 integrality iff at n | m, used as a
          valuation test, not as a routing totality statement.

FORBIDDEN:
  (i)   any bound on deg_y A, or restating T3 as a consequence of AS-TRI;
  (ii)  any claim that n >= 2 Abhyankar steps are automatically integral;
  (iii) reading v(c) = 0 as failure of the §2.5 iff;
  (iv)  Hensel, T1, or a two-sided no-go as a load-bearing step of AS-TRI;
  (v)   residue-field or series versions;
  (vi)  a lift, support bound, marked collision, max-12 routing, or JC2
        inference;
  (vii) the §2.5 monicization / Frobenius paragraph, which was not reviewed.
```

**CONFIRMED**
