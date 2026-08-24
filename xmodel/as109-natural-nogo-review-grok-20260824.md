# Hostile different-model review — AS109 natural certificate no-go

| Field | Value |
|---|---|
| Claim under review | Two structural no-go theorems for AS109: no finite full independent literal-slot `CLOSED-SUPPORT + UNIT-L` certificate; no exact `det J=1` lift whose corrections are both affine in `y` |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking precisions in the last section) |
| Evidence tier | independent exact expansion over `Z` and `Z_109` (hand Jacobian, ambient monomial coefficients, Wronskian, polynomial units in `Q_109[x]`); a second sparse engine that does not import the producer replay; unmodified rerun of `verify_no_go.py` as regression control |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T09:34:00Z – 2026-08-24T09:52:00Z |
| Python | 3.14.6; stdlib only |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/as109-closed-support-gate-20260824.md` (SHA-256 `b3fa62651673db06b89fb6ad8217ebc2a61bacd5940b7a08501a1f3a47a7d717`)
- `cases/as109_closed_support_20260824/verify_no_go.py` (SHA-256 `01d890b7f048765565203778a038a2d31a7cc8132a7f59c15ebff2655599eb50`)
- `cases/as109_closed_support_20260824/FREEZE.sha256` (SHA-256 `4fd38dfaac13042be5eb333c1bbdb28c604486a0468f2e661f31b9d40babe8bb`)
- packed-equation and contraction sections of `xmodel/as109-support-gate-20260824.md` (SHA-256 `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5`)
- `xmodel/as109-support-gate-20260824-erratum.md` (SHA-256 `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb`)

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No enumerator was written or run.

Write `p=109`, `s=x^{108}`, `R=Z_{109}`, `L(A,B)=A_x+B_y`, and `N(A,B)=(A_x-s)B_y-A_y B_x`.

---

## Promotion

**Accept `NO-INDEPENDENT-SLOT-CERTIFICATE / AFFINE-Y NO-GO` at the stated scope.**

- There is no finite slot set `S`, finite free residual module `W`, and `R`-linear right inverse of `L` satisfying the report's full independent literal-slot hypotheses (2.1)--(2.2).
- There is no exact `Z_{109}` polynomial lift of the seed `(x-x^{109},y)` with `det J=1` whose two correction polynomials are both affine in `y`.

**Do not promote either theorem to:** nonexistence of an arbitrary finite-support lift; a found lift; a characteristic-zero point; a JC2 counterexample or disproof; `HEIGHT-CERT`; `NO-CYCLE-AT-8`; cap widening; an exponent rectangle; or a finite Witt-level inference.

**Keep `CLOSED-SUPPORT + UNIT-L` as a conditional resurrection target**, now with two necessary constraints: the coefficient module must be a genuinely coupled section rather than the full independent slot module on its raw support, and the section must allow `y`-degree at least two because the entire affine-`y` family is impossible. Whether any such coupled block closes remains open.

## Quarantine

No result here proves or disproves JC2. The rank-one generator `(x^{109},(1-109)x^{108}y)` is a scope countercontrol, not a candidate Keller map. Producer JSON strings `IMPOSSIBLE` / `PASS-AS109-NATURAL-NOGO` were not used as evidence; the identities below were re-derived. Generic uncarried two-layer digit equations remain as in the carry erratum: they are not this packed `Z_{109}` identity.

---

## Scope (not enlarged)

One prime `p=109`, one seed `(x-x^{109},y)`, exact coefficient ring `R=Z_{109}`, and polynomial corrections in `R[x,y]`. Theorem 1 is a no-go for full independently variable literal-slot certificates. Theorem 2 is a no-go for the affine-`y` correction motif. Neither statement is a classification of all finite-support lifts, all coupled submodules, or all gauge sections with nonlinear `y`-dependence.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Over `Z[x,y]` and hence over `Z_{109}[x,y]`, `det J(x-x^p+pA,y+pB)-1 = p(L(A,B)-s+p N(A,B))` with the displayed `L` and `N`; this is an exact packed identity, not a truncated digit expansion, and has no base-109 carry | **CONFIRMED** | a leftover term of order `p^3` or higher; `N` not equal to `[A,B]-s B_y`; a carry remainder after splitting `A=A_0+p A_1` |
| 2 | Under the full independent module (2.1) and (2.2), a unit right inverse at `s` forces the individual slot `q_1=(0,sy)` as an element of `U_S`; a coupled combination inside `U_S` does not avoid declaring `q_1` | **CONFIRMED** | another literal slot whose divergence has a nonzero `x^{108}` term; `109` a unit of `Z_{109}`; `1` lying in `109 R` |
| 3 | For every `k>=1`, only `r_k=(x^{108k+1},0)` and `q_k=(0,x^{108k}y)` can feed the ambient coefficient of `s^k`; the `Q`-branch or the unit-`P` plus polarization (2.4) puts `s^{k+1}` in any finite free `W`, with no monomial-basis hypothesis on `W` | **CONFIRMED** | a third slot contributing to `[x^{108k}]L`; polarization remainder not `a_k s^{k+1}`; `{x^{108k}:k>=1}` linearly dependent over `R` in `R[x,y]`; the argument using a basis of `W` rather than the ambient monomial basis |
| 4 | Theorem 1 excludes full independently variable literal supports, not coupled submodules or gauge sections; the rank-one countercontrol has `L(u)=s` and `N(u)=-108^2 s^2`, fails closure on `R\cdot s`, and does not exclude an arbitrary fixed-support lift | **CONFIRMED** | the proof isolating `q_1` without (2.1); `N(u)` already in `R\cdot s`; the report asserting nonexistence of every finite-support lift |
| 5 | For `A=a(x)+c(x)y`, `B=d(x)+b(x)y`, the displayed `[y]` and `[y^0]` formulae hold; `[y]=0` gives `c=k(1+pb)` with `k` a 109-adic integer; polynomial units in `Q_{109}[x]` force `b` and `c` constant | **CONFIRMED** | a `y^2` term in `det J`; Wronskian `h c'-c h'` not the `[y]` factor; kernel of `d/dx` on `Q_{109}(x)` larger than constants; `1+pb` having constant term divisible by `109` |
| 6 | `[x^{108}]` of the second factor is `-109+109^2 a_{109}-109^3 k d_{109}`, valuation `1`, hence not zero; this rules out every exact affine-`y` lift, with no collision or degree cap | **CONFIRMED** | a further source of `x^{108}` cancelling valuation `1`; `a_{109}` or `k` allowed negative 109-valuation; a hidden collision or degree bound in the argument |
| 7 | A surviving certificate of this design must have essential coefficient coupling and at least one correction of `y`-degree `>=2`; no lift, characteristic-zero point, or JC2 conclusion follows | **CONFIRMED** | the report exhibiting a closed coupled core; an inferred existence or nonexistence statement for general finite support; a Hensel/Lefschetz promotion from these two theorems |

All remarks below are non-blocking unless marked otherwise. None changes a coefficient, a slot, or a verdict.

---

## Replay and hashes

Frozen producer hashes, recomputed on the charged tree:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-closed-support-gate-20260824.md` | `b3fa62651673db06b89fb6ad8217ebc2a61bacd5940b7a08501a1f3a47a7d717` | prompt and `FREEZE.sha256` |
| `cases/as109_closed_support_20260824/verify_no_go.py` | `01d890b7f048765565203778a038a2d31a7cc8132a7f59c15ebff2655599eb50` | prompt and `FREEZE.sha256` |
| `cases/as109_closed_support_20260824/FREEZE.sha256` | `4fd38dfaac13042be5eb333c1bbdb28c604486a0468f2e661f31b9d40babe8bb` | prompt |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | producer provenance table |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` | producer provenance table |

Registered command, rerun unmodified:

```sh
python3 cases/as109_closed_support_20260824/verify_no_go.py
```

Exit code 0. Top-level fields:

```text
verdict = PASS-AS109-NATURAL-NOGO
affine_y.exact_lift_affine_in_y = IMPOSSIBLE
literal_slot.full_independent_literal_slot_certificate = IMPOSSIBLE
enumeration_run = false
lift_found = false
characteristic_zero_inference = false
prime = 109
p_divisible_P_slot_multipliers_at_k = [1, 110, 219]
```

The case directory contains only `FREEZE.sha256` and `verify_no_go.py`. The replay is a finite regression control (`k=1..220` for (2.4); a sparse formal exponent set including `x^{109}` for (3.5)). The identities below are the proofs for every `k` and arbitrary polynomial degree.

A second sparse engine, written for this review and not importing the producer, checked: the packed identity on 222 random, monomial, affine, and coupled pairs (0 failures); `N=[A,B]-s B_y` (0 failures); unique contributing slots for `k` in `{1,2,3,4,108,109,110,218,219,220}`; polarization (2.4) on `k=1..220` plus `{500,1000,1090,10^4}` (0 failures); the coupled countercontrol; the affine split on 25 random coefficient lists (0 failures); and the displayed `x^{108}` obstruction.

---

## Claim 1 — packed determinant identity

**CONFIRMED.**

Let `P=x-x^p+pA` and `Q=y+pB`. Then

```text
P_x = 1 - p s + p A_x,     P_y = p A_y,
Q_x = p B_x,               Q_y = 1 + p B_y.
```

Expanding over `Z[x,y]`:

```text
det J = P_x Q_y - P_y Q_x
      = (1 - p s + p A_x)(1 + p B_y) - p^2 A_y B_x
      = 1 + p(A_x + B_y - s) + p^2((A_x - s)B_y - A_y B_x).
```

Hence

```text
det J - 1 = p(L(A,B) - s + p N(A,B)).                 (1.1)
```

This is an identity of polynomials, not a congruence modulo `p^3`. There is no residue-digit split `A=A_0+pA_1`, so there is no base-109 carry to track. The displayed `N` equals the contraction-section formula `[A,B]-s B_y` of gate §5.1 and erratum §4. The erratum's carry appears only in the truncated two-layer expansion; it does not infect this packed `Z_{109}` equation.

---

## Claim 2 — unit right inverse at `s` forces `q_1`

**CONFIRMED.**

`L` sends each labeled slot to a single monomial or to zero:

```text
L(P(a,b)) = a x^{a-1} y^b,          L(Q(c,d)) = d x^c y^{d-1}.
```

The ambient coefficient of `x^{108}` in `L(U_S)` receives contributions only from

```text
r_1 = P(109,0):   multiplier 109,
q_1 = Q(108,1):   multiplier 1.
```

No other nonnegative exponents hit `(108,0)`. If `u=sum lambda_e e` in `U_S`, then

```text
[x^{108}] L(u) = 109 lambda_{r_1} + lambda_{q_1}  in R.
```

Hypothesis (2.2) puts `s` in `W` and demands `L(R_0(s))=s`, so this coefficient equals `1`. If `q_1` is not declared, the coefficient lies in `109 R`. But `1` is a unit of `Z_{109}` and `109` is the uniformizer, so `1` is not in `109 R`. Hence `q_1` must be a declared slot.

A coupled preimage inside the *full* module does not avoid this. The relation `109 alpha + beta = 1` is solvable in `R` (take any `alpha` and `beta=1-109 alpha`), but it still requires the independent generator `q_1` to be present in `S`. Once (2.1) is in force, `q_1` itself lies in `U_S`, and

```text
N(q_1) = (0-s)s - 0 = -s^2,
```

so `s^2` lies in `W`. Coupling is an escape only after dropping (2.1), which is claim 4.

---

## Claim 3 — induction, polarization, and no monomial basis on `W`

**CONFIRMED.**

Fix `k>=1`. The ambient coefficient of `s^k=x^{108k}` in `L(U_S)` is fed only by

```text
r_k = P(108k+1, 0):   multiplier a_k = 108k+1,
q_k = Q(108k, 1):     multiplier 1.
```

This is again an equality in `R[x,y]`, whose monomial basis is used; it does not require `W` to be a coordinate-monomial module. `L(R_0(s^k))=s^k` forces that ambient coefficient to be `1`.

- If `q_k` is declared, then `N(q_k)=-s^{k+1}`, so `s^{k+1}` lies in `W`.
- If `q_k` is absent, then `a_k lambda_{r_k}=1`, so `r_k` is declared and `a_k` is a unit of `R`. Now `108k+1 equiv 1-k mod 109`, hence `a_k` is a nonunit if and only if `k equiv 1 mod 109`. At those stages the `Q`-branch is compulsory (in particular at `k=1`, recovering claim 2). When `a_k` is a unit, (2.1) puts `r_k`, `q_1`, and `r_k+q_1` in `U_S`. Direct expansion gives

```text
N(r_k) = 0,
N(q_1) = -s^2,
N(r_k+q_1) = a_k s^{k+1} - s^2,
```

so

```text
N(r_k+q_1) - N(r_k) - N(q_1) = a_k s^{k+1}.           (2.4)
```

(`N` is not a homogeneous quadratic, because of the `-s B_y` summand; the bilinear remainder is still exactly (2.4).) The left side lies in `W`. Multiplying by the inverse of `a_k` puts `s^{k+1}` in `W`.

Thus every `s^k`, `k>=1`, lies in `W` as an actual polynomial. These monomials are `R`-linearly independent in the ambient module `R[x,y]`. A finite free `R`-module cannot contain an infinite independent set. No basis of `W` is used: independence is inherited from the ambient free module on monomials.

The replay's three nonunit stages `k=1,110,219` match `k equiv 1 mod 109`. At `k=110` one has `a_{110}=109^2`, still a nonunit; the report's phrase “divisible by 109 exactly when” is the biconditional, not a claim that the valuation is always `1`.

---

## Claim 4 — scope and coupled countercontrol

**CONFIRMED.**

The isolation step that turns “`q_1` appears in some preimage” into “`N(q_1)` lies in `W`” is (2.1). A coupled submodule with the same raw support need not contain `q_1` as an independent generator, so polarization and the `N(q_k)` branch are unavailable. Theorem 1 therefore does not apply to gauge sections.

The displayed rank-one module is a valid countercontrol. For `u=(x^{109},(1-109)sy)`:

```text
L(u) = 109 s + (1-109)s = s,
N(u) = (109s-s)(1-109)s = 108(1-109)s^2 = -108^2 s^2.
```

Numerically `N(u)=-11664\, s^2`. This is not an `R`-multiple of `s` in `R[x,y]`, so closure fails on `W=R\cdot s`. Raw support on `{P(109,0), Q(108,1)}` does not decide the coupled problem.

Theorem 1 does not exclude an arbitrary finite-support lift: a single pair `(A,B)` is not the full coefficient module on its support. Theorem 2 excludes only the affine-`y` *shape*, not every finite support. The report's statement that these theorems prove neither existence nor nonexistence of an arbitrary fixed-support lift is accurate.

---

## Claim 5 — affine-`y` expansion, `c=k(1+109b)`, integrality of `k`

**CONFIRMED.**

Let `A=a(x)+c(x)y` and `B=d(x)+b(x)y` with `a,b,c,d in R[x]`. Then `P_y=pc` is independent of `y`, `Q_y=1+pb` is independent of `y`, and `P_x`, `Q_x` are affine in `y`. Hence `det J` has `y`-degree at most one. Expanding:

```text
[y] det J = p((1+pb)c' - p c b'),                      (3.2)
[y^0] det J = (1+pb)(1-ps+p a') - p^2 c d'.            (3.3)
```

If `det J=1`, then (3.2) vanishes. `Z_{109}` is torsion-free, so

```text
h c' - c h' = 0,    h := 1+pb.
```

The polynomial `h` is nonzero (constant term `1`). In the characteristic-zero field `Q_{109}(x)`, the kernel of `d/dx` is `Q_{109}`, so `c/h=k` for some `k in Q_{109}`, i.e. `c=k(1+pb)`. Substitute into (3.3):

```text
(1+pb)(1-ps+p a' - p^2 k d') = 1.                      (3.4)
```

Both factors lie in `Q_{109}[x]` and multiply to `1`. Units of a univariate polynomial ring over a field are the nonzero constants, so both factors are constants. Thus `b` is constant, then `c=k(1+pb)` is constant.

Why `k` is 109-adically integral: after constancy, `b in R` and `1+pb equiv 1 mod p`, so `1+pb` is a unit of `R`. Also `c in R`. Therefore `k=c/(1+pb)` lies in `R`. Equivalently, even before constancy: `c=k h` with `h` of constant term `1`, so a negative 109-valuation of `k` would make the constant term of `c` non-integral, contradicting `c in R[x]`.

---

## Claim 6 — the `x^{108}` obstruction

**CONFIRMED.**

With `b,c,k in R` and `1+pb` a nonzero constant, (3.4) forces the second factor

```text
g = 1 - p s + p a' - p^2 k d'
```

to be constant. The coefficient of `x^{108}` in `g` has exactly three sources:

```text
-p s              contributes  -p,
p a'              contributes  p * 109 a_{109} = p^2 a_{109},
-p^2 k d'         contributes  -p^2 k * 109 d_{109} = -p^3 k d_{109}.
```

No other degree in `a` or `d` differentiates onto `x^{108}`. There is no monomial collision and no degree cap: if `a_{109}=d_{109}=0`, the coefficient is still `-p`. Thus

```text
[x^{108}] g = -p + p^2 a_{109} - p^3 k d_{109}.         (3.5)
```

Here `a_{109},d_{109},k in R`. Dividing by `p` in the torsion-free ring `R` yields `-1 + p a_{109} - p^2 k d_{109} equiv -1 mod p`. If (3.5) vanished, this would be `0 equiv -1 mod p`. Equivalently `v_p((3.5))=1`, so (3.5) is not zero in `R`. Hence `g` is not constant, contradicting (3.4).

This uses neither marked collision nor an exponent bound. It rules out every exact lift in this seed chart whose two corrections both have `y`-degree at most one, including the canonical ray `B=x^{108}y` with `A` affine in `y`.

The only way (3.5) could cancel is if `a_{109}` or `k` had negative 109-valuation (e.g. `a_{109}=1/p`). That is forbidden by `a in R[x]` and claim 5.

---

## Claim 7 — resurrection statement and non-promotion

**CONFIRMED.**

Theorem 1 makes essential linear coupling necessary for any `CLOSED-SUPPORT + UNIT-L` certificate on literal slots. Theorem 2 makes `y`-degree at most one on *both* corrections impossible for an exact lift, hence impossible for a contraction certificate whose module consists of, or whose fixed point would be, affine-`y` polynomials. A surviving proposal of this design must therefore:

1. use a coupled `R`-module or gauge section, not `U_S`;
2. close `N` on that coupled module, including polarizations;
3. retain an integral right inverse of `L` after coupling;
4. allow `y`-degree at least two in the fixed point, hence in the section.

The report finds no positive closed core, launches no enumeration, and draws no Hensel/Lefschetz conclusion. The affine-`y` theorem is a family-wise nonexistence result, not a lift and not a characteristic-zero point. No JC2 statement follows. A finite Hamiltonian/gauge-paired block with quadratic `y`-dependence is correctly flagged as the smallest remaining motif *type*, not as an existence theorem.

---

## Smallest missing hypothesis, and non-blocking precisions

No numbered claim fails for want of a hypothesis.

Non-blocking precisions, none of which is an overclaim of existence, nonexistence of arbitrary finite support, or JC2:

1. In claims 2--3, “the coefficient of `s^k`” is the ambient monomial coefficient in `R[x,y]`. That is the correct object; it is why the argument does not need a monomial basis of `W`.
2. The producer replay's affine-`y` engine uses a finite formal exponent set. That is a control. The obstruction identity only involves `a_{109}` and `d_{109}`, and the hand expansion covers all degrees.
3. “`y`-degree at least two” means that at least one of `A,B` has `y`-degree `>=2`. Degree-one monomials remain legal inside a higher-degree section.
4. Theorem 2 *does* exclude the affine-`y` subclass of finite-support lifts. The word “arbitrary” in the report's nonexistence disclaimer is doing the work of leaving general finite support open.

## What this does not prove

- existence of a coupled closed core;
- nonexistence of a finite-support exact lift outside the two excluded families;
- a characteristic-zero polynomial Keller map;
- any statement about JC2.

Do not answer these theorems by widening a slot cap, sampling an exponent rectangle, or treating `PASS-AS109-NATURAL-NOGO` as a height certificate.
