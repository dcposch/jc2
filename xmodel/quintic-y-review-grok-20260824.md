# Hostile different-model review — QUINTIC-Y FRONTIER

| Field | Value |
|---|---|
| Claim under review | Characteristic-zero field theorem: every Keller pair with both `y`-degrees `<=5` is a polynomial automorphism; hence no exact `det J=1` lift of the AS109 seed has both correction `y`-degrees at most five |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking precisions in the last section; characteristic zero is load-bearing, not decorative; algebraic closure is a convenience) |
| Evidence tier | independent exact expansion over a generic characteristic-zero coefficient ring (hand Jacobian by `t`-degree from a general quintic, UFD valuations in `K[x]` and `Kbar[x]`, weighted valuations at finite places and at infinity, PID unique factorization on the Weierstrass cubic, chain-rule pullback of the constant row); a second sympy==1.14.0 engine that does not import the producer replay and re-derives every displayed identity from undifferentiated general coefficients; unmodified rerun of `cases/quintic_y_frontier_20260824/check.py` as regression control; quartic theorem consumed only through its completed different-model `CONFIRMED` review; banked Hensel lemma as previously dual-confirmed, rechecked on residue balls rather than marked sections |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T10:38:00Z – 2026-08-24T10:50:00Z |
| Python | 3.14.6; `uv run --no-project --with sympy==1.14.0` |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/quintic-y-frontier-preflight-independent-20260824.md` (SHA-256 `598cdf3799d4abf40ec761f1fd2b0a5a6457ee2b578371bd864c296259d2a978`)
- `cases/quintic_y_frontier_20260824/check.py` (SHA-256 `943676ec94a0e1829d80ca23f56e1ce8d919089c9eff8fecdbc5118200782bf5`)
- `cases/quintic_y_frontier_20260824/FREEZE.sha256` (SHA-256 `d45df0ffa46b198f5b8d6b058b3ac77a4d6783ee7f54555d3fc7a1e354953e06`)
- quartic producer `xmodel/as109-quartic-discriminator-gate-20260824.md` (SHA-256 `8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276`) and its completed different-model review `xmodel/as109-quartic-review-grok-20260824.md` (SHA-256 `3f9e763c07aa019a766b267774f92df857aadd94750cb8c3c9431671318d930e`); landed `CONFIRMED` during this review window, and is the sole logical dependency for pairs with both `y`-degrees `<=4`
- cubic parent `xmodel/as109-cubic-coupling-gate-20260824.md` (SHA-256 `198f0b2ff39f91a7815b9be15f7fc3c3afdd00c00b1c4c0ada6b9f6438d62820`) and `xmodel/as109-cubic-review-grok-20260824.md` (SHA-256 `2fdb8ae2beffb766b38d8e7de4bdff353bc354c4dba84d026225f88376f95cef`); context and a re-used affine/`(1,n)` argument, not a promotion dependency of the new quintic pairs
- Hensel noninjectivity in `xmodel/as109-support-gate-20260824.md` (SHA-256 `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5`) and `xmodel/as109-support-review-grok-20260824.md` (SHA-256 `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8`)
- carry erratum `xmodel/as109-support-gate-20260824-erratum.md` (SHA-256 `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb`) and `xmodel/as109-carry-erratum-review-grok-20260824.md` (SHA-256 `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212`), only to confirm Hensel independence from digit bookkeeping
- local primary/secondary priority notes: `papers/paper2/PRIORITY.md`, `papers/paper2/SCOPE.md`, `refs/zoladek2008_official.pdf` present; Y. Stein, Israel J. Math. 89 (1995) remains locally paywalled / surface-only as recorded in PRIORITY.md

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No enumerator was written or run. No sextic or higher `y`-degree family was searched. No AWS call was made.

Write `K` for an arbitrary characteristic-zero field, `Kbar` for an algebraic closure, `J(P,Q)=P_x Q_y-P_y Q_x`, and `p=109`. Actual `y`-degrees are used throughout: a vanishing leading coefficient simply routes to a lower case.

---

## Promotion

**Accept `QUINTIC-Y NO-GO` at the stated scope.**

- Over any characteristic-zero field, every Keller pair with both coordinates of `y`-degree at most five is a polynomial automorphism of `A^2_K`.
- There is therefore no exact `Z_{109}` polynomial lift of the seed `(x-x^{109},y)` with `det J=1` whose two correction polynomials both have `y`-degree at most five.

The three genuinely new actual patterns `(2,5)`, `(3,5)`, `(4,5)` are empty. Every remaining pattern with both `y`-degrees `<=5` is an automorphism by the confirmed `deg_y<=4` theorem, by equal-degree target shears, or by the affine/triangular argument.

**Do not promote this to:** a sextic or higher `y`-degree statement; nonexistence of an arbitrary finite-support AS109 lift; a found lift; a characteristic-zero point; a JC2 counterexample or disproof; `HEIGHT-CERT`; cap widening; an exponent rectangle; a finite Witt-level inference; or a novelty / priority claim for the field theorem.

**Keep `CLOSED-SUPPORT + UNIT-L` as a conditional resurrection target**, now with the necessary constraint that the section allow `y`-degree at least six in one correction. Whether any such coupled block closes remains open. This file licenses no sextic grammar and no support search.

---

## Quarantine

No result here proves or disproves JC2. Producer PASS strings and Laurent near-controls were not used as existence or nonexistence certificates; the identities below were re-derived. The quartic parent is recorded as landed `CONFIRMED` and is consumed only for pairs with both `y`-degrees at most four. The cubic parent is not consumed for the new quintic pairs. Generic uncarried two-layer digit equations remain as in the carry erratum: they are not the packed exact identity that Hensel consumes. Priority is quarantined from the mathematical verdict. Laurent controls are negative tests: they show that a predicted constant-term pole is attained when polynomiality of `Q` is dropped, and they do not substitute for the unit-product or resultant arguments.

---

## Scope (not enlarged)

One prime `p=109`, one seed `(x-x^{109},y)`, exact coefficient ring `Z_{109}` for the lift, and a field theorem over an arbitrary characteristic-zero `K` (applied at `K=Q_{109}`). Arbitrary finite `x`-degree, support, and coefficient coupling are in scope *inside* both `y`-degrees `<=5`. Sextic and higher `y`-degree, series lifts, and an arbitrary-AS109 no-go are out of scope. GL2 target normalization and polynomial target shears are used only as automorphy tests over `K` (or `Kbar`); they are not integral support gauges.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | After equal-degree target reduction, zero/affine cases, and target shears, the only new actual pairs above the confirmed quartic theorem are `(2,5),(3,5),(4,5)`. Affine-in-`y` pairs are triangular over `K`. Leading UFD gives `a=h^m`, `d=h^5` when `gcd(m,5)=1`. Depression is an identity in `K(x)[y]`, not a source automorphism. Automorphy descends from `Kbar` to `K`. The quartic dependency is discharged by its completed hostile review | **CONFIRMED** | a leftover `(0,5)` or `(1,5)` Keller pair that is not triangular; `5=0`; kernel of `d/dx` on `K(x)` larger than `K`; `m v(d)=5 v(a)` failing to produce integer `e` in `K[x]`; a missed actual pattern; quartic review landing `GAP`/`REFUTED` |
| 2 | For `(2,5)`, the normalized form is `P=t^2+p`, `Q=t^5+(5p/2+lambda)t^3+(15p^2/8+3 lambda p/2+mu)t`, with `J/h=p' q_1`. Every allowed constant target shear is used. The `y=0` expression has uncancellable leading term `3 rho^5/8`. After polynomiality, `h p' q_1` is a unit product, and a linear `p` makes `q_1` quadratic. Zero factors and constant branches give `J=0` | **CONFIRMED** | a surviving even `t`-power after shears; `3/8=0`; a finite pole of `rho` cancelled by `C,lambda,mu`; `q_1` constant on a degree-1 `p`; `h` cancelling a pole of `p' q_1` after polynomiality |
| 3 | For `(3,5)`, the shape (3.1), the first integral (3.2), and the constant row are exact. Weighted finite-pole analysis, including fractional valuations, forces `q=s` with no dropped ties. The three leading equations have Groebner basis `(1)` and subresultant/resultant `441`. Then `rho,A,B` are polynomials | **CONFIRMED** | a missed Jacobian row leaving an extra free function; weight-6 of `H` not dominating; a valuation tie with `q≠s` keeping `P(x,0)` polynomial; common root of `5a^2+10a+6` and `a^3-9a^2-18a-9`; a finite pole of `A` or `B` after `rho` is regular |
| 4 | Completing the square gives `225 Z^2=Phi(A)`. Distinct-root UFD in `Kbar[x]` forces `A` constant and `J=0`. Repeated and triple roots are parametrized by (3.5). Direct substitution of that parametrization into the independently derived constant row gives `J/h=R' Psi_epsilon(R)` with `deg=6` and `LC=-epsilon 35/27` identically in the parameters. No singular branch or cancellation makes this a unit | **CONFIRMED** | linear-in-`Z` remainder after completion; Pell-like nonconstant squares in `Kbar[x]` with constant difference; `LC(Psi)` vanishing on a locus of `(gamma,r)`; a polynomial `R` of degree `d>=1` with `7d-1=0`; `Psi` identically zero |
| 5 | For `(4,5)`, the depressed form (4.1), the integrals `I_2,I_1` in (4.2), and the constant bracket (4.3) match direct symbolic differentiation, including every sign and the factor `1/32` | **CONFIRMED** | a leftover `t^{>=3}` row; `t^2` or `t` not equal to `-I_2'/32` or `-I_1'/32`; a sign/factor mismatch in (4.3) against `t^0` |
| 6 | Every nonzero initial point of (4.4) has `c≠0`. Polynomiality of `P(x,0)` forces `q=s`. The four leading equations (4.5) have Groebner basis `(1)`. The `b=0` branch forces incompatible values of `a`; the `b≠0` branch has resultant `-12180258816`. No lower-weight constant or valuation tie was dropped in a way that creates a solution | **CONFIRMED** | a nonzero `(a,b,0)` solution of (4.4); a tie `q≠s` with cancelling poles in `P(x,0)`; a common root of `f_45` and `g_45`; a weight-4 remainder of `I_2` producing a new leading point that solves (4.5) |
| 7 | The only initial branches of (4.4) at polynomial infinity are types I--III. The degree `8q-1` coefficients of the weight-8 top of (4.3) are `5q c^2`, `5q a^4/32`, `55q a^4/32`, all nonzero in characteristic zero, and strictly heavier than every `L,M,N` term. Then `h j` cannot be a unit. Laurent controls attain the predicted poles and are negative tests | **CONFIRMED** | a fourth weighted-infinity branch; cancellation of the `8q-1` term against a lower-weight summand; `8q-1<=0` for some `q>0`; Laurent controls being used as a proof of polynomiality |
| 8 | The field theorem holds over every characteristic-zero `K`. Combined with the confirmed quartic theorem and residue-ball Hensel, no exact AS109 lift has both correction `y`-degrees at most five. No JC2 or novelty inference is licensed. Accessible local primary material does not identify this exact statement | **CONFIRMED** | `109 A` raising `y`-degree over `Q_{109}`; Hensel uniqueness failing for unit Jacobian; the contradiction applying only to a sheared non-integral pair; a claimed sextic or arbitrary-support no-go; confirmation being made to rest on an attribution |

All remarks below are non-blocking unless marked otherwise. None changes a coefficient or a verdict.

---

## Replay and hashes

Frozen producer hashes, recomputed on the charged tree:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/quintic-y-frontier-preflight-independent-20260824.md` | `598cdf3799d4abf40ec761f1fd2b0a5a6457ee2b578371bd864c296259d2a978` | prompt and `FREEZE.sha256` |
| `cases/quintic_y_frontier_20260824/check.py` | `943676ec94a0e1829d80ca23f56e1ce8d919089c9eff8fecdbc5118200782bf5` | prompt and `FREEZE.sha256` |
| `cases/quintic_y_frontier_20260824/FREEZE.sha256` | `d45df0ffa46b198f5b8d6b058b3ac77a4d6783ee7f54555d3fc7a1e354953e06` | freeze of the two files above |
| `xmodel/as109-quartic-discriminator-gate-20260824.md` | `8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276` | quartic producer |
| `xmodel/as109-quartic-review-grok-20260824.md` | `3f9e763c07aa019a766b267774f92df857aadd94750cb8c3c9431671318d930e` | completed hostile review; overall `CONFIRMED` |
| `xmodel/as109-cubic-coupling-gate-20260824.md` | `198f0b2ff39f91a7815b9be15f7fc3c3afdd00c00b1c4c0ada6b9f6438d62820` | cubic producer; not consumed for the new pairs |
| `xmodel/as109-cubic-review-grok-20260824.md` | `2fdb8ae2beffb766b38d8e7de4bdff353bc354c4dba84d026225f88376f95cef` | cubic review `CONFIRMED`; not consumed for the new pairs |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | banked Hensel |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` | carry scope |
| `xmodel/as109-support-review-grok-20260824.md` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` | Hensel review |
| `xmodel/as109-carry-erratum-review-grok-20260824.md` | `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212` | carry review |

The case directory contains only `FREEZE.sha256` and `check.py`. Registered command, rerun unmodified:

```sh
uv run --no-project --with sympy==1.14.0 python3 \
  cases/quintic_y_frontier_20260824/check.py
```

Exit code 0. Output: **24/24 exact checks passed**, covering the `(2,5)` bracket and `3/8` pole identity plus Laurent control; the `(3,5)` vanishing high rows, `H'/27`, subresultant `441`, Weierstrass completion, and both signs of the singular pullback; the `(4,5)` vanishing high rows, `-I_2'/32`, `-I_1'/32`, Groebner emptiness of (4.5), resultant `-12180258816`, three infinity coefficients, and Laurent control.

A second engine, written for this review and not importing the producer, started from a *general* quintic in the depression variable `t` and independently: integrated every Jacobian row; recovered (2.1)--(2.3), (3.1)--(3.2), (4.1)--(4.3); matched the `(3,5)` constant row to the pullback formula used in the replay; recomputed subresultant `441` and resultant `441`; Groebner-emptied both leading systems; recomputed `Psi_epsilon` from the constant row rather than from the replay expression; confirmed triple-root specialization still has degree 6 and the same leading coefficient; exhausted `c=0` in (4.4); re-derived `f_45,g_45` and the resultant `-12180258816`; recomputed the three `8q-1` coefficients. Result: **51/51 independent checks passed, 0 failed**.

The producer replay does not, by itself, prove polynomiality, unit products, or the absence of valuation ties. Those are the algebraic arguments below. Arbitrary `x`-degree is carried by `y`-degree (or `t`-degree) counting, not by the finite Laurent samples.

---

## Claim 1 — reduction, UFD, depression, descent, quartic dependency

**CONFIRMED.**

Let `P,Q in K[x,y]` satisfy `J(P,Q)=j in K^*` and `deg_y P, deg_y Q <=5`. Write actual `y`-degrees as `m<=n` after a possible swap `(P,Q)|->(Q,P)`, which sends `J` to `-J` still in `K^*`.

*Equal actual degrees `m=n=r>0`.* The only `y^{2r-1}` contributions come from the two leading coefficients `a,d in K[x]`, giving `r(a' d - a d')=0`. Characteristic zero supplies `r≠0` (`r<=5`). The kernel of `d/dx` on `K(x)` is `K`: if `u=p/q` in lowest terms and `u'=0`, then `q` divides `q'` or else `q` is a unit, and `deg q'<deg q` in characteristic zero forbids a nonconstant `q`. Thus `d/a` is constant, and a constant target row operation in `GL_2(K)` lowers one actual degree.

*Zero top, `m=0`.* Then `P=a_0(x)` and `J=a_0' Q_y`. A product of an element of `K[x]` and a polynomial of `y`-degree `n-1>=1` cannot be a nonzero constant: `Q_y` would have to be independent of `y`, hence `n=1`, contradicting `n>=1` in the remaining `(0,n)` list except `(0,1)`. The case `(0,1)` is triangular: `a_0' b_1=j` forces both factors to be units of `K[x]`, so `a_0` is degree one and `b_1` is a nonzero constant. In particular `(0,5)` is not Keller.

*Affine top, `m=1`.* Write `P=a y+b` with `a≠0` and put `t=P`. The Jacobian of `(x,t)` with respect to `(x,y)` has determinant `a`, and

```text
J_{x,y}(P,Q)= -a (partial Q/partial x)|_t.
```

Expand `Q=sum_{k=0}^N c_k(x) t^k` over `K(x)`. Then `sum c_k' t^k` is, up to the unit `-a`, a nonzero constant, so `c_k` is constant for every `k>=1`. The remaining coefficient `c_0` lies in `K[x,y] ∩ K(x)=K[x]`, and `-a c_0'=j`. Both factors are units of `K[x]`: `a in K^*` and `c_0` is degree one. The pair is triangular over `K`, with inverse polynomial over `K`. This argument never uses the quartic theorem and applies equally to `(1,2)`, `(1,3)`, `(1,4)`, and `(1,5)`.

Independent check: if `c_k` for `k>=1` are constants, `J=-a c_0'` identically.

*Pairs with `n<=4`.* After the reductions above one has either a triangular automorphism or a pair whose actual degrees are at most four. The completed different-model review of the quartic producer landed overall `CONFIRMED` (all eight of its numbered claims). That review re-proves the cubic base it uses and does not rest on promotion of its parent. This quintic review therefore consumes the quartic theorem at its stated scope: every Keller pair with both `y`-degrees at most four is a polynomial automorphism of `A^2_K`. The launch instruction to treat the quintic theorem as conditional on quartic is discharged by that landing.

*The only remaining actual patterns are `(2,5)`, `(3,5)`, `(4,5)`.* The list of actual pairs with `m<=n<=5` is

```text
(0,0),(0,1),...,(0,5);  (1,1),...,(1,5);  (2,2),...,(2,5);
(3,3),(3,4),(3,5);      (4,4),(4,5);      (5,5).
```

Equal-degree cases shear; `(0,n)` for `n>=2` is not Keller; `(1,n)` is triangular; everything with `n<=4` is the quartic theorem. What remains is exactly `(2,5)`, `(3,5)`, `(4,5)`.

*Leading UFD for `(m,5)` with `gcd(m,5)=1`.* The top Jacobian coefficient is `5 a' d - m a d'=0`, equivalently `(d^m / a^5)'=0`, so `d^m = c a^5` with `c in K^*`. At every irreducible of the UFD `K[x]` one has `m v(d)=5 v(a)`. Since `gcd(m,5)=1`, this forces `v(a)=m e` and `v(d)=5 e` for a nonnegative integer `e`. The product of those irreducibles to the powers `e` is a polynomial `h in K[x]`, and after constant target scaling one has `a=h^m`, `d=h^5`. Algebraic closure is not required: `K[x]` is already a UFD. (Over `Kbar` the irreducibles are linear, which is only a convenience.)

*Depression alignment.* Put `t=h y + rho` with `rho in K(x)` chosen to kill the `t^{m-1}` term of `P`. This is an identity in `K(x)[y]`, not a polynomial source automorphism of `A^2`. Unlike the quartic `(3,4)` case, only `P` needs a depression shift: the next Jacobian rows then determine the coefficients of `Q` as functions of those of `P`, in the same variable `t`. For `(2,5)` the quadratic shift is unique. For `(3,5)` the cubic shift is unique; the `t^4` coefficient of `Q` remains a constant `gamma` because no polynomial in `P` of degree `<=1` produces `t^4` (`P^2` has `t^6`). For `(4,5)` the quartic shift kills `t^3` in `P`, and a constant target shear `Q |-> Q-lambda P` kills the constant `t^4` coefficient of `Q` (that coefficient is constant by the `t^7` Jacobian row). No second rational depression of `Q` needs to be aligned with that of `P`.

*Descent.* Two independent descents, either of which suffices, once the three new patterns are shown empty over `Kbar` and the remaining pairs are automorphisms over `Kbar`.

Uniqueness / Galois invariance: a polynomial endomorphism of `A^2` has at most one polynomial inverse. If `(P,Q)` is defined over `K` and becomes an automorphism over `Kbar`, that inverse is unique as a morphism, hence Galois-fixed, hence defined over `K` (`K` is perfect in characteristic zero).

Faithful flatness: `Kbar/K` is faithfully flat, and isomorphy of affine coordinate rings descends along faithfully flat base change.

Injectivity, which is all AS109 needs, descends even more cheaply.

In fact `Kbar` is unnecessary for the new pairs: valuations and unique factorization work in `K[x]`, the kernel of `d/dx` on `K(x)` is `K`, and the finite-place arguments below use the discrete valuations of `K(x)` attached to irreducibles of `K[x]`, not just linear places. The producer's `Kbar` detour is correct and is not load-bearing. The auxiliary `t=h y+rho` is never treated as a source automorphism.

---

## Claim 2 — pair `(2,5)`

**CONFIRMED.**

Work in `K(x)[t]` with `P=t^2+p` and a general quintic

```text
Q=t^5 + alpha t^4 + beta t^3 + gamma t^2 + delta t + epsilon.
```

Direct expansion of `J_{x,t}(P,Q)` (so that `J_{x,y}=h J_{x,t}`) yields

```text
t^5: -2 alpha'
t^4: 5 p' - 2 beta'
t^3: 4 alpha p' - 2 gamma'
t^2: 3 beta p' - 2 delta'
t^1: 2 gamma p' - 2 epsilon'
t^0: delta p'.
```

Thus `alpha` is constant. The target shear `Q |-> Q - alpha P^2` is a polynomial automorphism of the target plane (`P^2=t^4+2p t^2+p^2`) and kills `alpha`. With `alpha=0`, `beta'=(5/2)p'`, so `beta=5p/2+lambda` with `lambda` constant. Then `gamma` is constant, and `Q |-> Q - gamma P` kills it. Then `delta'=(3/2) beta p'`, so

```text
delta = 15 p^2/8 + 3 lambda p/2 + mu,          mu constant.
```

Then `epsilon` is constant and a target translation kills it. No further polynomial in `P` of degree `<=2` remains: `P` and `P^2` are even in `t` after depression, and `P^3` has `t^6`. The normalized pair is exactly (2.1), and the remaining Jacobian is (2.2):

```text
J/h = p' (15 p^2/8 + 3 lambda p/2 + mu) = p' q_1.
```

The second engine reproduced both identities from the general quintic, not by substituting the producer shape.

*The `y=0` expression.* Let `C=P(x,0)=rho^2+p in K[x]` and substitute `p=C-rho^2` into `Q(x,0)`. Expanding in `rho` gives exactly (2.3):

```text
Q(x,0) = 3 rho^5/8 - (5C/4 + lambda/2) rho^3
         + (15 C^2/8 + 3 C lambda/2 + mu) rho.
```

At a finite place where `rho` has pole order `s>0`, the term `3 rho^5/8` has pole order `5s`. The coefficient `C` is polynomial, hence regular, as are the constants `lambda,mu`. The remaining terms have pole orders `<=3s` and `<=s`. In characteristic zero, `3/8≠0`, so there is no cancellation. A rational function with no finite poles is a polynomial: `rho in K[x]`, then `p=C-rho^2 in K[x]`.

*Unit product, including `h`, zero factors, and constant branches.* After polynomiality, `h`, `p'`, and `q_1` all lie in `K[x]`, and their product is the nonzero constant `j`. Units of `K[x]` are `K^*`, so each factor is a nonzero constant.

- `h=0` identically is excluded from the genuine `(2,5)` branch (`a=h^2≠0`).
- `p'=0` makes `J=0`.
- `q_1=0` as a polynomial in `p` requires `15/8=0`, contrary to characteristic zero. If `q_1` vanishes identically along a particular `p`, it is still a polynomial factor of a unit, hence a unit, so cannot be the zero function.
- `p'` a nonzero constant means `p` has degree 1. Then `q_1` has degree 2 with leading coefficient `(15/8) (lead p)^2 ≠ 0`, so `q_1` is not constant.

Every branch contradicts `j≠0`. Nonconstant `h` is included and is forced to be a unit by the same product; it cannot cancel poles of `p' q_1` because, after polynomiality, there are no poles.

The Laurent sample `h=x^7`, `rho=x^{-1}`, `p=-x^{-2}` produces polynomial `P=x^{14} y^2+2 x^6 y`, constant `J=15/4`, and `Q(x,0)=3/(8x^5)`. It shows that the `3/8` obstruction is attained exactly when polynomiality of `Q` is dropped. It is a negative test, not a proof of the unit product.

---

## Claim 3 — pair `(3,5)`: normal form, finite poles, subresultant `441`

**CONFIRMED.**

*Independent integration of the general quintic against `P=t^3+A t+B`.* The Jacobian `t`-rows of a general quintic `Q=t^5+al t^4+be t^3+ga t^2+de t+ep` are

```text
t^6: -3 al'
t^5: 5 A' - 3 be'
t^4: -A al' + 4 al A' + 5 B' - 3 ga'
t^3: -A be' + 3 be A' + 4 al B' - 3 de'
t^2: -A ga' + 2 ga A' + 3 be B' - 3 ep'
t^1: -A de' + de A' + 2 ga B'
t^0: -A ep' + de B'.
```

Thus `al` is constant; call it `gamma`. Then `be=5A/3+k`, and the target shear `Q |-> Q-k P` kills `k`. Then

```text
ga = 4 gamma A/3 + 5 B/3 + m,     m constant
```

(`P^2` has `t^6`, so `m` cannot be sheared away). Then

```text
de = 5 A^2/9 + 4 gamma B/3 + n,     n constant,
ep = 2 gamma A^2/9 + 10 A B/9 + 2 m A/3
```

up to a constant, which a target translation kills. This is exactly (3.1). On this shape, `t^{>=2}` vanish identically. The `t^1` row is `H'/27` with

```text
H = 36 gamma A B + 54 m B + 27 n A - 5 A^3 + 45 B^2,
```

so `H=kappa` is a constant (the last nonconstant Jacobian row). The constant row, derived independently and *not* copied from the replay, is

```text
J/h = (-4 gamma A^2/9 - 2 m A/3 - 10 A B/9) A'
      + (4 gamma B/3 + n - 5 A^2/9) B'.
```

This matches the replay's pullback formula with `d/dx` in place of `d/dR`, which is the only justification for using that formula later.

*Weighted finite poles, including fractional valuations.* At a finite place of `K(x)`, give `(A,B)` weights `(2,3)` and set

```text
q = max{ 0, -v(A)/2, -v(B)/3 }.
```

The function `H` is a constant, hence has no pole. Its terms have weights `6` (`A^3`, `B^2`), `5` (`gamma A B`), `3` (`m B`), and `2` (`n A`). If `q>0`, weight `6` strictly dominates (even for fractional `q`: `6q>5q`). For the weight-6 top `-5 A^3+45 B^2` not to pole, both `A` and `B` must attain the scale, and their leading coefficients must satisfy `a^3=9 b^2`. In particular `v(A)=-2q` and `v(B)=-3q` are integers, so `q` itself is an integer: a half-integral `q` with `-v(A)/2` not matching `-v(B)/3` leaves an uncancelled pole in `H`, and matching forces `q in Z`. There is no fractional escape.

*The step `q=s`, and ties.* Let `rho` have pole order `s`, and write `P(x,0)=rho^3+A rho+B in K[x]`. The three summands have pole orders `3s`, `2q+s`, `3q`.

- If `q>s`, then `B` is the unique largest pole (order `3q>2q+s` and `3q>3s`).
- If `q<s`, then `rho^3` is the unique largest pole (order `3s>2q+s` and `3s>3q`).

Either contradicts polynomiality of `P(x,0)`. The only remaining case is `q=s`. At `q=s` all three terms have pole order `3s` and may cancel; that cancellation is the leading equation `1+a+b=0`, not a dropped tie. Other candidate equalities (`2q+s=3q`, `3s=2q+s`) are the same condition `q=s`. If `q=s=0`, there is no pole at this place.

*Leading equations and subresultant `441`.* Put `A ~ a rho^2`, `B ~ b rho^3`. Polynomiality of `P(x,0)`, of `H`, and of `Q(x,0)` give

```text
1+a+b=0,
a^3=9 b^2,
1 + 5a/3 + 5b/3 + 5 a^2/9 + 10 a b/9 = 0.
```

(The `gamma,m,n` terms in `Q(x,0)` are strictly lower order, pole `<=4s`.) Substituting `b=-1-a` into the third equation produces `(5a^2+10a+6)/(-9)=0`. Substituting into the second produces `a^3-9a^2-18a-9=0`. The second engine checked both reductions, computed the subresultant chain

```text
[a^3-9a^2-18a-9,  5a^2+10a+6,  70a+105,  441],
```

and obtained resultant `441` and `gcd=1`. Groebner basis of the three equations in `(a,b)` over `Q` is `(1)`. The roots of `5a^2+10a+6` are `-1 ± i sqrt(5)/5`; at those points the cubic equals `7/5 ± (14 i sqrt(5))/25 ≠ 0`. Characteristic zero is used: `441=3^2 7^2`.

A fourth leading contribution from the constant Jacobian row is of strictly lower or equal weight and cannot *create* a solution of an already empty system. After the weight-6 top of `H` cancels, the weight-5 remainder `36 gamma A B` would itself have to be regular; that is an extra constraint, not a new leading point.

*Polynomiality of `rho,A,B`, not assumed.* Emptiness of the leading system forbids `q=s>0`. Combined with `q=s`, one has `s=0`: `rho` has no finite pole, hence `rho in K[x]`. If `A` or `B` still had a finite pole, the same weighted top of `H` would force `B` to have pole order `3q>0`, unique in `P(x,0)` because `rho` is now regular. Thus `A,B in K[x]`. No circular use of the conclusion: polynomiality of `P(x,0)` and `Q(x,0)` is used as input (they are specializations of polynomials), and polynomiality of `rho,A,B` is the output.

---

## Claim 4 — Weierstrass cubic, parametrization, `Psi`

**CONFIRMED.**

*Completion of the square.* Put `Z=B+2 gamma A/5 + 3m/5`. Direct expansion, independently of the replay, gives

```text
5(H-kappa) = 225 Z^2 - Phi(A),
Phi(A)=25 A^3 + 36 gamma^2 A^2 + (108 gamma m - 135 n) A + 5 kappa + 81 m^2.
```

The linear-in-`Z` terms cancel. Leading coefficient `25≠0` in characteristic zero, so `Phi` is a genuine cubic.

*Distinct-root UFD.* If `Phi` has three distinct roots `r_i` in `Kbar`, then `225 Z^2=25 (A-r_1)(A-r_2)(A-r_3)` makes `Phi(A)` a square in `Kbar[x]` up to a constant square. The factors `A-r_i` are pairwise coprime (their differences are nonzero constants). Unique factorization therefore puts each `A-r_i` equal to a constant times a square: `A-r_i=c_i U_i^2`. The difference of two such squares is a nonzero constant. Over `Kbar[x]`, which is a PID, write `c_1 U_1^2 - c_2 U_2^2=(sqrt(c_1) U_1 - sqrt(c_2) U_2)(sqrt(c_1) U_1 + sqrt(c_2) U_2)`. A product of two polynomials equal to a nonzero constant forces each factor to be a unit, hence constant, so `U_1,U_2` are constant and `A` is constant. (The integer Pell equation is irrelevant: units of `Kbar[x]` are `Kbar^*`, not `±1` in `Z`.) Then `Z` is constant, hence `B` is constant. The constant Jacobian row vanishes when `A'=B'=0`, so `J=0`, contrary to `j≠0`.

*Repeated and triple roots.* A nonconstant polynomial point therefore requires a repeated root. Write `Phi(A)=25(A-r)^2(A-s)`. Unique factorization in `Kbar[x]` gives `A-s=R^2` (absorbing a constant square) and `3Z=epsilon (A-r) R` with `epsilon in {+1,-1}`. This is (3.5). The triple-root case `s=r` is included: it forces `r=-12 gamma^2/25` from the `A^2` coefficient of `Phi`, and then `3Z=epsilon R^3`. The identity `225 Z^2=Phi(A)` holds identically on (3.5) for both signs, including the triple root. The case `A=r` identically makes `Z=0` and `A` constant, already excluded. The case `Phi` identically zero requires `25=0`.

The `A^1` coefficient of `Phi` determines `n` as a constant in terms of `gamma,m,r,s`; the constant term determines `kappa`. Both are used only as algebraic constraints among constants.

*Direct substitution into the constant row.* Substituting (3.5) into the independently derived constant row and applying the chain rule `d/dx=R' d/dR` (legitimate because `gamma,m,n,r,s` are constants) produces a polynomial `Psi_epsilon(R) in Q(gamma,r)[R]` with

```text
J/h = R' Psi_epsilon(R),     deg Psi_epsilon = 6,
LC(Psi_epsilon) = -epsilon * 35/27.
```

The leading coefficient is independent of `gamma,m,r` (and `m` cancels entirely from `Psi`). Both signs were expanded term by term. The triple-root specialization `r=-12 gamma^2/25` still has degree 6 and the same leading coefficient. Factorization over `Q(gamma,r)` is

```text
Psi_+ = (-25 R^2 + 36 gamma^2 + 75 r) * (quartic in R) / 84375,
```

with the quartic's `R^4` coefficient equal to `4375≠0`. The quadratic factor is a constant times `A-r` and vanishes only when `R` is constant. Neither factor is identically zero in characteristic zero (`35=5*7`, `27=3^3`, `4375=7*5^4`).

*No unit branch.* If `R` has degree `d>=1`, then `R' Psi(R)` has degree `7d-1>=6`, with leading coefficient `(-epsilon 35/27) d (lead R)^7 ≠ 0`. This cannot be a unit of `K[x]`. Lower-degree terms of `Psi` cannot cancel that leading term because `Psi` has constant coefficients. If `R` is constant then `R'=0` and `J=0`. There is no integer `d` with `7d-1=0`. Nonconstant `h` makes the contradiction stricter: `J=h R' Psi(R)` would have even larger degree. Zero factors of `R'` or of `Psi(R)` make `J=0`.

---

## Claim 5 — pair `(4,5)`: depressed form, `I_2`, `I_1`, constant bracket

**CONFIRMED.**

*Independent integration.* Against `P=t^4+A t^2+B t+C`, a general quintic has Jacobian rows

```text
t^7: -4 al'
t^6: 5 A' - 4 be'
t^5: -2 A al' + 4 al A' + 5 B' - 4 ga'
t^4: -2 A be' + 3 be A' - B al' + 4 al B' + 5 C' - 4 de'
t^3: -2 A ga' + 2 ga A' - B be' + 3 be B' + 4 al C' - 4 ep'
```

plus lower rows. Thus `al` is constant, and `Q |-> Q-al P` kills it. Then `be=5A/4+L` and `ga=5B/4+M` with constants `L,M`. Substituting into the `t^4` row integrates to

```text
de = 5 A^2/32 + 3 L A/4 + 5 C/4 + N,
```

and the `t^3` row integrates to

```text
ep = 5 A B/16 + M A/2 + 3 L B/4
```

up to a constant, which is translated away. This is exactly (4.1). On this shape, `t^{>=3}` vanish.

*First integrals and the constant row, against direct differentiation.* Define `I_2` and `I_1` by (4.2). Direct differentiation of the producer-shaped Jacobian gives

```text
[t^2] J_{x,t} = -I_2'/32,     [t^1] J_{x,t} = -I_1'/32,
```

as identities in `A,B,C` and the constants `L,M,N`. The constant row is exactly (4.3):

```text
j = J/h = [
  24 L A C' - 24 L B B' - 16 M B A' + 32 N C'
  + 5 A^2 C' - 10 A B B' - 10 B^2 A' + 40 C C'
]/32.
```

Written without the common denominator this is

```text
(3/4) L A C' - (3/4) L B B' - (1/2) M B A' + N C'
+ (5/32) A^2 C' - (5/16) A B B' - (5/16) B^2 A' + (5/4) C C',
```

which matches the expanded `t^0` coefficient termwise (every sign and every factor of `2`). If `A,B,C` are constant, every derivative vanishes and `j=0`.

The second engine obtained these identities by substituting the integrated shape into `P_x Q_t - P_t Q_x` and comparing with `diff(I_2)`, `diff(I_1)`, and (4.3). No sign was taken from the producer on trust.

---

## Claim 6 — weighted `(2,3,4)` pole lemma

**CONFIRMED.**

Give `(A,B,C)` weights `(2,3,4)`. The weight-6 tops of the constants `I_2,I_1` are

```text
a^3 - 8 a c - 4 b^2 = 0,     b(3 a^2 - 8 c) = 0.          (4.4)
```

Lower-weight summands of `I_2,I_1` (`L A^2`, `L C`, `M B`, `N A`, `M C`, `N B`) have weights `<=4` and cannot cancel a weight-6 pole when `q>0`.

*Every nonzero solution of (4.4) has `c≠0`.* Setting `c=0` gives `a^3=4 b^2` and `3 a^2 b=0`. If `b=0` then `a=0`. If `b≠0` then `a=0`, hence `b=0`. The only solution is the zero initial point. Independently, `solve` over `Q` returns only `{a:0,b:0}`. Consequently, if `q>0`, the initial point of `(A,B,C)` satisfies (4.4) and is nonzero, so `C` has exact pole order `4q`.

*The step `q=s`.* Let `rho` have pole order `s` and set `q=max{0,-v(A)/2,-v(B)/3,-v(C)/4}`. Polynomiality of `P(x,0)=rho^4+A rho^2+B rho+C` compares pole orders `4s`, `2q+s`, `3q+s`, `4q`.

- If `q>s`, then `C` is the unique largest pole (order `4q`).
- If `q<s`, then `rho^4` is the unique largest pole. (If `q=0` and `s>0` this is the same comparison.)

Thus `q=s`. At `q=s` all four terms may cancel, which is the equation `1+a+b+c=0`, not a dropped tie. Other candidate equalities (`2q+s=4q`, `3q+s=4q`) reduce to `s=2q` or `s=q`; combined with `q=s` they give either `s=0` or the main case. Fractional `q` is harmless: attaining degrees of polynomials are integers, and a non-attaining coordinate simply does not appear in the initial point.

*The four leading equations (4.5).* Put `A ~ a rho^2`, `B ~ b rho^3`, `C ~ c rho^4`. From `P(x,0)`, from (4.4), and from `Q(x,0)` with `L=M=N` of lower weight,

```text
1+a+b+c=0,
a^3-8ac-4b^2=0,
b(3a^2-8c)=0,
-1/4 + 5 a^2/32 + 5 a b/16=0.
```

The fourth equation was re-derived by substituting the leading forms into `Q(x,0)` and reducing along `1+a+b+c=0`; the `5a/4` and `5b/4` contributions cancel against part of `5c/4`. Groebner basis over `Q` in lex order `(c,b,a)` is `(1)`.

*Branch `b=0`.* Then `c=-1-a`, the second equation becomes `a(a^2+8a+8)=0`, and the fourth becomes `5a^2=8`. The root `a=0` fails `5a^2=8`. Combining `a^2+8a+8=0` with `5a^2=8` produces the candidate `a=-6/5`, for which `a^2=36/25 ≠ 8/5`. Resultant of `a^2+8a+8` and `5a^2-8` is `-256≠0`.

*Branch `b≠0`.* Then `c=3a^2/8` and `b=-1-a-3a^2/8`. The identity `a^3-8ac-4b^2=0` becomes `b^2=-a^3/2`. The case `a=0` forces `c=0` and `b=-1`, which fails `b^2=-a^3/2`. Clearing denominators in the remaining two equations produces exactly

```text
f_45 = 9a^4 + 80 a^3 + 112 a^2 + 128 a + 64,
g_45 = 15 a^3 + 20 a^2 + 40 a + 32,
```

with `gcd=1` and resultant `-12180258816 = -2^{25}·3·11^2 ≠ 0` in characteristic zero. Both polynomials were re-derived: `g_45` is `-4` times the cleared `Q` equation, and `f_45=(3a^2+8a+8)^2+32 a^3`.

*No dropped lower-weight constant.* After (4.4) kills weight 6, the weight-4 remainder `12 L(A^2-8C)` of `I_2` must itself be regular if `q>0`. That is an additional constraint (e.g. type I with `L≠0` is already impossible from `I_2` alone). It does not produce a new solution of (4.5). Constants `L,M,N` have weight 0 and cannot compete with weight 6 when `q>0`.

Thus `rho` is polynomial. If any of `A,B,C` still had a finite pole, (4.4) would again give a pole of order `4q` in `C`, unique in `P(x,0)` because `rho` is regular. Hence `A,B,C in K[x]`.

---

## Claim 7 — polynomial infinity and Laurent controls

**CONFIRMED.**

Suppose at least one of `A,B,C` is nonconstant, and set

```text
q = max{ deg(A)/2, deg(B)/3, deg(C)/4 } > 0.
```

The leading point of `(A,B,C)` satisfies (4.4). The solutions with not all of `a,b,c` zero are exactly three types:

```text
I.    a=b=0, c≠0;
II.   b=0, a≠0, c=a^2/8;
III.  b≠0, c=3a^2/8, b^2=-a^3/2
```

(type III forces `a≠0` and hence `c≠0`, else the zero point). There is no fourth branch: (4.4) is `b=0` or `c=3a^2/8`, and `b=0` splits on `a=0` versus `c=a^2/8`.

*The weight-8 top of (4.3)* is `[5 A^2 C'-10 A B B'-10 B^2 A'+40 C C']/32`. Homogenizing `A=a X^{2q}` and likewise for `B,C`, the coefficient of `X^{8q-1}` in the numerator is

```text
q (20 a^2 c - 50 a b^2 + 160 c^2).
```

Dividing by 32 and specializing:

```text
I.    5 q c^2,
II.   5 q a^4 / 32,
III.  55 q a^4 / 32.
```

All are nonzero in characteristic zero for a nonzero initial point and `q>0`. The `L,M,N` terms of (4.3) have degrees `<=6q-1`. The gap is `2q>0`, so they cannot cancel the `8q-1` term. In particular `j` has degree `8q-1`. The minimal positive `q` for a nonconstant polynomial is `1/4` (when `deg C=1`), and `8q-1>=1`.

Then `J=h j` is a product of two polynomials of which `j` has positive degree, so cannot be a nonzero constant. If `A,B,C` are all constant, (4.3) vanishes identically, also contrary to `j≠0`. This closes `(4,5)`.

*Laurent controls are negative tests.* The type-I sample `h=x^9`, `rho=x^{-1}`, `A=B=0`, `C=-x^{-4}` produces polynomial `P=x^{36} y^4+4 x^{26} y^3+6 x^{16} y^2+4 x^6 y`, constant `J=-5`, and `Q(x,0)=-1/(4 x^5)`. Directly: `Q=t^5+(5C/4) t` gives `Q(x,0)=rho^5+(5C/4) rho=x^{-5}-(5/4) x^{-5}=-1/(4x^5)`. Combined with the `(2,5)` sample, these show that the predicted constant-term poles are attained exactly when polynomiality of `Q` is dropped. They do not prove the unit-product or resultant statements, and the preflight does not use them as such.

---

## Claim 8 — field theorem, AS109 consequence, priority hygiene

**CONFIRMED.**

*Field theorem over every characteristic-zero `K`.* Claims 2--7 show that the genuine patterns `(2,5)`, `(3,5)`, `(4,5)` are empty over `Kbar` (and in fact over `K`). Claim 1 reduces every other pair with both `y`-degrees at most five to a triangular automorphism or to the confirmed quartic theorem. Therefore `Kbar[P,Q]=Kbar[x,y]`. Descent in claim 1 gives `K[P,Q]=K[x,y]`.

Characteristic zero is load-bearing for the global factors `2,3,4,5`, for `deg pi'=deg pi-1`, for `3/8`, `15/8`, `25`, `35/27`, `441=3^2 7^2`, and `-12180258816=-2^{25}·3·11^2`, and for the type-III infinity coefficient `55=5·11`. It is stated in the theorem.

*AS109 consequence.* Suppose there were an exact polynomial lift

```text
F=(P,Q)=(x-x^{109}+109 A,  y+109 B),
A,B in Z_{109}[x,y],     deg_y(A), deg_y(B) <= 5,     det J(F)=1.
```

View `P,Q` in `Q_{109}[x,y]`. The summand `x-x^{109}` is independent of `y`, and `109≠0` in `Q_{109}`, so `deg_y(P)=deg_y(A)` if `deg_y(A)>=1` and `=0` otherwise. Likewise `deg_y(Q)<=5`: the only way the seed `y` could interact with `109 B` is to drop degree, and in any case `-1/109` is not in `Z_{109}`, so the coefficient of `y` in `Q` cannot vanish for integral `B`. Thus `deg_y(P), deg_y(Q)<=5`. The identity `det J(F)=1` survives `Z_{109}->Q_{109}`. The field theorem over `K=Q_{109}` makes `F` a polynomial automorphism, hence injective on `Q_{109}^2`.

Target `GL_2`, shears, and the auxiliary `t` are internal to the proof of the field theorem. They are not applied to the integral seed. The contradiction is for `F` itself.

Modulo `109`, `F` is `(x-x^{109},y)`, with derivative the identity (because `d(x^{109})=109 x^{108}=0` in characteristic `109`) and with `F_bar(a,b)=(0,b)` for every `a` by Fermat. Multivariate Hensel on the complete DVR `Z_{109}`, using that `det J_F=1` is a unit at every integral point, says that `F` maps each source ball `(a,b)+109 Z_{109}^2` bijectively onto the target ball `(0,b)+109 Z_{109}^2`. The `109` distinct source balls for fixed `b` therefore all cover the same target ball, so `F` is noninjective over `Q_{109}`, contradiction.

This uses neither a finite-Witt approximation nor a marked lattice-point collision. The packed identity `det J=1` is the hypothesis; the truncated two-layer expansion and its base-109 carry are not used. The erratum leaves the Hensel lemma intact, and the different-model carry review confirmed that independence.

Hence: **no exact AS109 determinant-one lift has both correction `y`-degrees at most five.** Any exact lift of this seed, if one exists, must have correction `y`-degree at least six in one coordinate. That is a necessary condition, not a construction.

*Scope exclusions, audited.*

- In scope: every exact determinant-one lift whose two corrections both have `y`-degree at most five, with no cap on `x`-degree, number of monomials, coefficient height, or linear coupling among those coefficients.
- Out of scope: any pair in which at least one correction has `y`-degree `>=6`; series lifts; an arbitrary-AS109 no-go; a JC2 decision. No finite grammar for the sextic range is supplied.
- Not used: marked collision equations, support cap, `x`-degree bound, coefficient height, finite Witt layer, exponent/support search, AWS.
- The run produced no lift and no JC2 inference.

*Priority hygiene, not a novelty grant.* Accessible local primary material was reread only for whether *this exact theorem* (Keller, both `y`-degrees at most five, arbitrary characteristic-zero field, conclusion polynomial automorphy) is already identifiable there.

- Magnus, Math. Scand. 3 (1955) 255--260, as recorded from the local copy in PRIORITY.md, is the coprime *total-degree* case: `m,n>=2` coprime implies the Jacobian constant is `0` and `u,v in K[h]`. That is a different statement.
- Żołądek 2008 Lemma A.7 / 3.9, locally present at `refs/zoladek2008_official.pdf`, is the Schwarz--Christoffel / Darboux obstruction used as Theorem A of the Mathieu programme, not a `y`-degree-at-most-five automorphy theorem.
- Hermoso--Alcázar, arXiv 2410.18867, Theorem 4 with `n=2`, is the unweighted Wronskian, the affine tail of the quadratic base.
- Y. Stein, Israel J. Math. 89 (1995), 301--319, remains locally paywalled (PRIORITY.md: Springer 303-redirect, surface only, reduction-to-ODE-system framing). No attribution to Stein is licensed from a title or a citers' summary. The producer already makes no priority claim and flags this source as still requiring inspection.
- Appelgate--Onishi 1985 and Nowicki--Nakai 1988 remain locally unresolved / paywalled, as in the cubic and quartic reviews.

The exact theorem is **not** identifiable from accessible local primary material. That does **not** license a novelty or prior-art claim. The producer already makes none. This review promotes none. Mathematical confirmation of claims 1--7 does not depend on priority: the derivation above is self-contained. A later primary-source identification of the same statement would be a citation update, not a refutation.

---

## Smallest missing hypothesis or overclaim

None of the eight claims is an existence theorem, a sextic statement, an arbitrary-support AS109 no-go, a JC2 decision, or a novelty claim.

Hostile attempts to break the field theorem produced no counterexample:

- the normalized `(2,5)` form with linear `p` makes `q_1` quadratic of leading coefficient `15/8`;
- Groebner bases of both leading pole systems are `(1)`;
- `Psi_epsilon` has leading coefficient `-epsilon 35/27` even on the triple-root locus and after factoring off `A-r`;
- `c=0` in (4.4) forces the zero point;
- type I--III infinity coefficients are nonzero in characteristic zero;
- constant `A,B` (resp. `A,B,C`) make the constant Jacobian row vanish;
- the affine identity `J=-a c_0'` holds exactly.

The smallest precisions a reader could miss, and that this review therefore isolates, are:

- Characteristic zero is used for the factors `2,3,4,5`, for `deg pi'=deg pi-1`, and for the nonvanishing of `3/8`, `15/8`, `25`, `35/27`, `441`, `55`, and `-12180258816`. In characteristic `3` or `7` the `(3,5)` subresultant vanishes; in characteristic `5` the Weierstrass leading term and the `(2,5)` quadratic in `p` collapse; in characteristic `11` the type-III infinity coefficient `55 q a^4/32` vanishes and would need a lower-weight analysis. None of these is in scope.
- Algebraic closure is a convenience for writing linear places and for taking square roots of constants in the Weierstrass parametrization. Unique factorization in `K[x]` already produces `h in K[x]`. Descent is correct as written and is not needed if one never leaves `K`.
- The compressed line "the difference of two such squares is a nonzero constant, so both are constant" is valid in `Kbar[x]` because a product of two polynomials equal to a constant forces each to be a unit. It would be false in `Z` (Pell). The load-bearing ring is `Kbar[x]`, a PID.
- The producer replay's 24 checks are regression controls for universal identities. Polynomiality, unit products, valuation ties, and emptiness of leading systems are the algebraic arguments above. The two Laurent samples are negative tests.
- Constants `lambda, gamma, L, ...` lie in `K` (or `Kbar` on the producer's detour), not necessarily in `Z_{109}`. Target operations decide automorphy over `Q_{109}` and are not integral gauges.
- Hensel's collision is 109-to-1 covering of residue balls. It does not use marked sections and does not use truncated digit carries.
- The quartic theorem is a genuine logical dependency of the overall `deg_y<=5` statement, and is used only after its different-model review landed `CONFIRMED`. The new work of this lane is the emptiness of `(2,5)`, `(3,5)`, `(4,5)`.
- No novelty claim is attached to confirmation.

Those are scope reminders, not missing hypotheses in the written lemmas.

---

## Stop conditions that remain in force

No cap, degree, or prime may be changed in response to this review. Sextic and higher `y`-degree are not licensed as a search by this file. The only resurrection trigger remains a separately reviewed finite coupled section that meets `CLOSED-SUPPORT + UNIT-L` and, by claim 8, allows `y`-degree at least six in one correction.

No result here proves or disproves JC2.
