# Hostile different-model review — AS109 bounded polar conductor / completed-orbit algebraization gate

| Field | Value |
|---|---|
| Claim under review | Frozen AS109 bounded polar-conductor gate: the rational cotangent control `C_p=(x-x^p, y/(1-p x^{p-1}))` is an integral restricted-analytic determinant-one lift of `(x-x^p,y)` with a reduced exterior affine polar divisor of `p-1` vertical components at valuation `-1/(p-1)`; polynomial Keller right maps cannot cancel that divisor; a hypothetical polynomial lift has a unique identity-branch restricted-analytic symplectic gauge `C_p ∘ Φ_F = F` whose canonical truncation degrees `κ_n(F)` tend to infinity; every fixed simultaneous map/gauge total-degree cap fails at some finite Witt depth; the cap `D_F=D_φ=p` is empty at depth three for every odd prime |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (precisions below; nonexistence of a polynomial lift, identification of `E_p` with `A_infinity`, a growth law for `κ_n`, rational deck descent, and `p=109` are correctly *not* claimed) |
| Evidence tier | independent commutative algebra of `Z_p⟨x,y⟩` and of étale polynomial maps `A^2→A^2` over `Qpbar` (geometric series, Jacobian criterion, quasi-finiteness of point fibres, Gauss lemma); independent binomial/`p`-adic expansion of a general bounded gauge modulo `p^3`, with explicit `p=3` cubing; a second sparse engine that does not import the producer replay (forward and reversed-column Gauss, integer polynomial composition); unmodified rerun of `cases/as109_bounded_polar_conductor_20260824/replay.py` as regression control only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `6f2e49e63d74493910fa357a8adc82f0e40d219a` (matches the charged clean-bank basis) |
| Review window (UTC) | 2026-08-24T13:34:33Z – 2026-08-24T13:48:00Z |
| Python | 3.14.6; stdlib only (`math.comb`, integer dicts, `fractions.Fraction`) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, freeze, and cited parents reread in full before any verdict:

- `xmodel/as109-bounded-polar-conductor-gate-20260824.md` (SHA-256 `2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b`, matches the launch prompt)
- `cases/as109_bounded_polar_conductor_20260824/PREREGISTRATION.md` (SHA-256 `9e291d17a1d8f2fe83c8ebad9f7a4d799304398629a794d790c4fe81bfc0ee6a`)
- `cases/as109_bounded_polar_conductor_20260824/replay.py` (SHA-256 `26ead3001ce1e9bf939e47a4e9e529785561357dc9e95479823b3347841aca85`)
- `cases/as109_bounded_polar_conductor_20260824/replay.stdout.json` (SHA-256 `0b0ad8c2d0c05d0628a1efb3853f72be5f4234dbfbf81ab596cbf632066b1d99`)
- `cases/as109_bounded_polar_conductor_20260824/MANIFEST.sha256` (SHA-256 `aa07a878b41adfbe9e07beaa48aa793562fb49228ffae8982aa8773f600df4e2`, matches the launch prompt)
- `cases/as109_bounded_polar_conductor_20260824/FREEZE.sha256` (SHA-256 `aa07a878b41adfbe9e07beaa48aa793562fb49228ffae8982aa8773f600df4e2`, identical listing)

Reviewed wild-symplectic and `A_infinity` parents named by the producer, same charged basis:

- `xmodel/as109-wild-symplectic-conductor-gate-20260824.md` (SHA-256 `c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c`) and different-model review `xmodel/as109-wild-symplectic-conductor-review-grok-20260824.md` (SHA-256 `a59c7ccbf39971ad7ab47f8e865926c93e4ac9d46305be076f4bd0193b2b1a9a`), overall **CONFIRMED**
- `xmodel/as109-ainfinity-deck-descent-gate-20260824.md` (SHA-256 `f1cf4991e92e502459ca6c61a3cb4d0e346a65e6221890c8c64a808ec2e3b64b`) and different-model review `xmodel/as109-ainfinity-review-grok-20260824.md` (SHA-256 `a86b694364ebaf28a3890b7bd73aafb5057ddae100172db78a9490e7a2b55d76`), overall **CONFIRMED**

Named cotangent control, consumed only as the rational/restricted-analytic representative, already dual-reviewed:

- `xmodel/witt-tate-control-20260824.md` (SHA-256 `c38d0209b8bc4b4d2ad4fd3d371966fac5441e8e10c029d837647b6797fb8eb2`) and `xmodel/review-witt-tate-control-claude.md` (SHA-256 `b3eae1f5a1420cec99bb8d75c8b0cddfd7a2db1e2027032e3f0be3b4fc6735a2`)

The committed basis is exactly `6f2e49e63d74493910fa357a8adc82f0e40d219a`. Named producer, parent-review, and case artifacts remain uncommitted on top of that basis. No producer, case, canonical, ladder, or notes file was edited. No AWS call was made. The independent engine lived in `/tmp` and was not imported from the registered replay.

Write `p` an odd prime (the compiler samples `p=3,5`; the structural identities were re-derived for general odd `p` and machine-checked at `p=3,5,7,11`). Conditionally let `F` be a determinant-one polynomial lift of `(x-x^p,y)` over `Z_p`. Existence is not inferred. Do not insert a polynomial lift, a rational deck action, or an identification of the exterior polar divisor with `A_infinity` from completion.

Tried hard, and failed, to cancel `D(X)` against `Y` for a noninvertible Keller map, to reverse the completed-orbit orientation, to extract a growth rate or a nonexistence theorem from `κ_n→∞`, to break König compactness by dead-end fibres, to let `r2,s2` or a `p=3` binomial remainder kill the forbidden monomial, and to promote the `p=3,5` ranks into the all-odd-prime argument.

---

## Promotion

**Accept `POLAR-CONDUCTOR / UNBOUNDED-GAUGE` at the stated bounded-category scope.**

Under the conditional exact-lift hypothesis, and equally for the restricted-analytic cotangent control itself:

- `C_p=(g, y/D)` with `g=x-x^p` and `D=1-p x^{p-1}` lies in `Z_p⟨x,y⟩^2`, reduces to `(x-x^p,y)`, and has `det J(C_p)=1` as an identity of restricted series, not merely a congruence. Over `Qpbar` the denominator is reduced, with exactly `p-1` distinct vertical components, each at source valuation `-1/(p-1)`, hence outside the closed unit bidisc. This is an affine polar divisor of a rational representative. It is not the projective line at infinity and it is not the Hensel residual factor `A_infinity`.
- For every polynomial `φ=(X,Y)` over `Qpbar` with `det J(φ)=1` — invertibility not assumed, JC not used — one has `gcd(D(X),Y)=1`. Étaleness supplies quasi-finite point fibres; the Jacobian-wedge argument also kills multiplicities and every irreducible factor of a reducible pullback, and shows `D(X)` itself is square-free. Under polynomial symplectic automorphisms the polar divisor pulls back isomorphically, so nonvanishing and the `p-1` geometric components are genuine invariants. Under merely Keller right maps one gets only non-cancellation: `C_p ∘ φ` remains nonpolynomial.
- The confirmed wild theorem supplies a unique identity-branch restricted-analytic symplectic automorphism `Φ_F ≡ id (mod p)` in the orientation `C_p ∘ Φ_F = F`. Reverse composition, rationality, polynomiality, a global degree drop, and deck descent are not inserted.
- Canonical conductors `κ_n(F)` are the max total degrees of the unique identity-branch reductions modulo `p^n`. They are finite, nondecreasing, and computable. A uniform degree bound, or a uniform bound on the nested canonical support cardinalities, would make `Φ_F` polynomial and contradict the no-cancellation lemma. The exact conclusion is `κ_n(F)→∞`. It is not a growth rate and not nonexistence of a polynomial lift.
- For every fixed total-degree caps `(D_F, D_φ)`, the systems `B_{(p,n)}(D_F,D_φ)` on total-degree simplices are finite, finitely branching under reduction, and empty for some finite `n`: otherwise König's lemma produces a bounded polynomial gauge over `Z_p` with bounded polynomial composition, contradicting no-cancellation.
- At the first natural cap `D_F=D_φ=p`, depth two survives by `φ=id`. Depth three is empty for every odd prime: the first-coordinate cap forces every degree-`≥2` coefficient of `r` to vanish; first-order determinant one forces `[x^{p-1} y]s=0`; the coefficient of `p^2 x^{2p-2} y` in the second composition is then exactly `1`. Binomial terms with two or more copies of `p r` have valuation `≥3`, including at `p=3`. This necessary subsystem already kills the full bounded gauge (6.2).
- Independent exact row reduction recovers the registered `p=3,5` table. Sample agreement is a control on the structural argument, not a substitute for it.

**Do not promote this to:** nonexistence of a polynomial lift; identification of `E_p` with `A_infinity` or with projective infinity; rational or polynomial deck descent; a global generic-degree drop beyond the reviewed `d≥p`; a `p=109` enumeration; a lift construction; or any JC2 decision.

**Keep the successor as a new quantitative or comparison theorem, not a deeper unrestricted cohomology run.** The smallest honest successor toward excluding a bounded-degree polynomial point of the completed orbit is a lower growth law for `κ_n(F)` in terms of a bound on `F`, or emptiness of `B_{(p,n)}(D_F,D_φ)` for a sequence of intrinsic caps. A second, independent successor is a proved comparison of the exterior valuation `-1/(p-1)` with the valued initial systems that govern `A_infinity`. That comparison is not automatic and is not licensed by sharing the word *boundary*.

---

## Quarantine

No result here proves or disproves JC2. Producer string `POLAR-CONDUCTOR / UNBOUNDED-GAUGE` and the registered Booleans were not used as evidence for the geometric series, for étale quasi-finiteness, for the binomial expansion, or for König compactness; those were re-derived. The registered replay is a `p=3,5` digit-matrix and cotangent-identity suite, not a checker of Henselian pairs or of the all-odd-prime emptiness proof. The completed `C_p` action and the unique gauge `Φ_F` live on the integral unit bidisc and remain compatible with the confirmed residual factor `A_infinity` of the global formal generic algebra; they are not the missing descent key of the `A_infinity` parent. Moskowicz, TDU at `td=109`, and the independent `deg_y ≤ 5` frontier are not consumed.

---

## Scope (not enlarged)

One odd prime in the analytic/algebraic theorem; compiler primes `{3,5}` only, with extra independent checks at `{7,11}`; one seed `(x-x^p,y)`; exact coefficient ring `Z_p` for a hypothetical polynomial lift, or the restricted Tate algebra for completed lifts; the closed unit bidisc versus algebraic `A^2` over `Qpbar`. Characteristic-zero language is purely conditional on an exact integral polynomial lift that this run did not produce. No construction, no `p=109` enumeration, no AWS, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | `C_p` is integral restricted-analytic on the closed unit bidisc, reduces to `(x-x^p,y)`, and has determinant one as a restricted-series identity. Over `Qpbar`, `D` is reduced with exactly `p-1` vertical components at valuation `-1/(p-1)`, outside the closed unit bidisc. The object is an affine polar divisor, not projective infinity and not `A_infinity` | **CONFIRMED** | `p^j` failing to tend to `0` in `Z_p`; `D S_∞ ≠ 1` in `Z_p⟨x⟩`; a multiple root of `D`; a root with nonnegative valuation; a sentence identifying `E_p` with `A_infinity` or with `P^1_∞` |
| 2 | For arbitrary polynomial `φ=(X,Y)` with `det J(φ)=1`, without JC or invertibility: `gcd(D(X),Y)=1`. Étaleness gives quasi-finite point fibres; multiplicities and reducible pullbacks are handled; `D(X)` is square-free. Automorphisms make `Pol` an isomorphic pullback invariant; Keller right maps give only non-cancellation | **CONFIRMED** | a determinant-one polynomial with a curve in `φ^{-1}(α,0)`; `dX∧dY` vanishing along a common factor while remaining `1`; invertibility smuggled in; `p-1` components claimed invariant for noninvertible Keller maps |
| 3 | Unique identity-branch restricted-analytic symplectic gauge in the orientation `C_p ∘ Φ_F = F`, against the frozen wild theorem. No reverse composition, rationality, polynomiality, global generic degree, or deck descent | **CONFIRMED** | orientation `Φ_F ∘ C_p = F` or `F ∘ Φ_F = C_p`; a second identity-residue solution; `det J(Φ_F)` only a unit; a sentence asserting `Φ_F` polynomial or rational; `d=p` from bidisc rank |
| 4 | `κ_n(F)` is canonical, finite, and nondecreasing. A uniform degree bound, or a uniform nested-support-cardinality bound, makes `Φ_F` polynomial and contradicts Claim 2. Exact conclusion: `κ_n→∞`, not a rate and not nonexistence of a polynomial lift | **CONFIRMED** | two identity-branch gauges with different truncations; a coefficient of degree `>B_0` of valuation `∞` that is nonzero; `D(A)` a unit while nonconstant; `κ_n→∞` sold as “no polynomial `F`” |
| 5 | Systems `B_{(p,n)}(D_F,D_φ)` live on total-degree simplices, reduce, are finite and finitely branching, and if nonempty at every depth yield a bounded polynomial gauge and a bounded polynomial composition over `Z_p`, contradicting Claim 2 | **CONFIRMED** | an infinite inverse system of nonempty finite sets with no compatible path; `Y S_n(X)` inverse-limiting to a nonpolynomial of bounded degree; reduction `B_{n+1}→B_n` failing; a rectangular-support theorem sold as this one |
| 6 | Independent expansion of `Φ=id+p(r,s)+p^2(r2,s2)` modulo `p^3` at caps `p,p`: depth two survives; every `deg r ≥ 2` coefficient vanishes; `[x^{p-1} y]s=0`; the `p^2 x^{2p-2} y` coefficient is `1`. The `p=3` binomial remainder has valuation `3`. The necessary subsystem empties the full nonlinear cap for every odd prime | **CONFIRMED** | `v_p(C(p,k) p^k)<3` for some `k≥2`; a degree-`>p` term of `r2` or `s2` under the cap; `[x^p]r` surviving the first-coordinate cap; the forbidden coefficient cancellable by a remaining linear digit; emptiness claimed only for the linear subsystem and not for (6.2) |
| 7 | Frozen `p=3,5` replay plus independent reconstruction: variables `20,42`; coefficient/augmented ranks `12/13,32/33`; forbidden monomials `x^4 y`, `x^8 y`; manifest and stdout hashes match. Sample agreement is only a control | **CONFIRMED** | a different rank under reversed-column Gauss; a consistent augmented system; `MANIFEST.sha256` or stdout digest mismatch; the `p=3,5` ranks used as the all-prime proof |
| 8 | Maximum licensed promotion is `POLAR-CONDUCTOR / UNBOUNDED-GAUGE`. It does not exclude a polynomial lift, identify `A_infinity`, descend a deck action, run `p=109`, or decide JC2. Quantitative conductor growth, or a proved comparison with `A_infinity`, is the smallest honest successor | **CONFIRMED** | the gate concluding `CONTRADICTION` or `PULLBACK-CANCELLATION`; `E_p` used as `A_infinity`; a `p=109` licence; unrestricted deeper cohomology treated as an invariant |

All remarks below are non-blocking unless marked otherwise. None changes a valuation, a rank, a forbidden coefficient, or a numbered verdict.

---

## Replay and hashes

Frozen producer hashes, recomputed on the charged tree:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-bounded-polar-conductor-gate-20260824.md` | `2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b` | prompt, `MANIFEST.sha256`, `FREEZE.sha256` |
| `cases/as109_bounded_polar_conductor_20260824/PREREGISTRATION.md` | `9e291d17a1d8f2fe83c8ebad9f7a4d799304398629a794d790c4fe81bfc0ee6a` | `MANIFEST.sha256` |
| `cases/as109_bounded_polar_conductor_20260824/replay.py` | `26ead3001ce1e9bf939e47a4e9e529785561357dc9e95479823b3347841aca85` | `MANIFEST.sha256` |
| `cases/as109_bounded_polar_conductor_20260824/replay.stdout.json` | `0b0ad8c2d0c05d0628a1efb3853f72be5f4234dbfbf81ab596cbf632066b1d99` | `MANIFEST.sha256` |
| `cases/as109_bounded_polar_conductor_20260824/MANIFEST.sha256` | `aa07a878b41adfbe9e07beaa48aa793562fb49228ffae8982aa8773f600df4e2` | prompt |
| `xmodel/as109-wild-symplectic-conductor-gate-20260824.md` | `c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c` | producer provenance |
| `xmodel/as109-wild-symplectic-conductor-review-grok-20260824.md` | `a59c7ccbf39971ad7ab47f8e865926c93e4ac9d46305be076f4bd0193b2b1a9a` | producer provenance |
| `xmodel/witt-tate-control-20260824.md` | `c38d0209b8bc4b4d2ad4fd3d371966fac5441e8e10c029d837647b6797fb8eb2` | producer provenance |
| `xmodel/review-witt-tate-control-claude.md` | `b3eae1f5a1420cec99bb8d75c8b0cddfd7a2db1e2027032e3f0be3b4fc6735a2` | producer provenance |
| `xmodel/as109-ainfinity-deck-descent-gate-20260824.md` | `f1cf4991e92e502459ca6c61a3cb4d0e346a65e6221890c8c64a808ec2e3b64b` | producer provenance |
| `xmodel/as109-ainfinity-review-grok-20260824.md` | `a86b694364ebaf28a3890b7bd73aafb5057ddae100172db78a9490e7a2b55d76` | producer provenance |

Every member hash inside `MANIFEST.sha256` was recomputed from the repository root and matched. `FREEZE.sha256` is byte-identical to `MANIFEST.sha256`.

Registered command, rerun unmodified from the charged tree:

```sh
python3 cases/as109_bounded_polar_conductor_20260824/replay.py
```

Exit code 0. Stdout SHA-256 `0b0ad8c2d0c05d0628a1efb3853f72be5f4234dbfbf81ab596cbf632066b1d99`, byte-identical to the frozen `replay.stdout.json`. The script writes no files.

The registered program is a finite `p∈{3,5}` control suite: Euclidean `gcd(D,D')` over `Q`, the truncated geometric-series identity through depths `2,3,4`, and RREF of a necessary first-digit linear system at the cap `D_F=D_φ=p`. Those Booleans were discarded as evidence for Claims 1–6 and 8; every numbered claim below is re-derived independently. Process remark, non-blocking: `replay.py` encodes the first-coordinate cap as the tautological rows `r_{ij}=0` for `i+j≥2`, rather than by composing `g(X)` and reading high-degree coefficients. The composition identity that justifies those rows is Claim 6, not the script.

A second engine, written for this review and not imported from the registered script, used only `math.comb`, integer dictionaries, and `fractions.Fraction`, with `s`-first / `y`-major monomial order and both forward and reversed-column Gauss elimination. It recorded zero failures on: `gcd(D,D')=1` at `p=3,5,7,11`; the integer identity `(1-p x^{p-1}) S_n = 1-p^n x^{n(p-1)}` through `n=5`; binomial valuations `v_p(C(p,k) p^k)≥3` for all `k≥2` at those primes, with the `p=3` cube `(x+3r+9 r2)^3 ≡ x^3 + 9 x^2 r (mod 27)` as an explicit polynomial identity; random integer composition of `g(X)` and `Y S_3(X)` matching (6.3)–(6.4) modulo `p^3` at `p=3,5,7`; the forbidden coefficient equal to `1` after the structural vanishings, including at `p=7`; and digit-system ranks

| `p` | variables | high-`r` rows | divergence rows | coeff / aug rank | forbidden | inconsistent |
|---:|---:|---:|---:|---|---|---|
| 3 | 20 | 7 | 6 | `12 / 13` | `x^4 y` | yes |
| 5 | 42 | 18 | 15 | `32 / 33` | `x^8 y` | yes |
| 7 | 72 | 33 | 28 | `60 / 61` | `x^{12} y` | yes (extra) |
| 11 | 156 | 75 | 66 | `140 / 141` | `x^{20} y` | yes (extra) |

Scratch engine SHA-256 `5c372358b1b912aa20d343b09f4c2f35dde45eb2e309c07dccb1f4681264ee1a` (outside the repository; not a freeze input). Forward and reversed-column ranks agreed in every case.

---

## Independent recomputation

### 1. Basepoint and exterior divisor — CONFIRMED

Put `g=x-x^p`, `D=g'=1-p x^{p-1}`, `z=p x^{p-1}`, and

```text
S_∞ = ∑_{j≥0} z^j = ∑_{j≥0} p^j x^{j(p-1)} ∈ Z_p⟨x⟩.
```

The coefficient of `x^{j(p-1)}` is `p^j`, of valuation `j→∞`. That is the definition of a restricted series. Equivalently, on the closed unit bidisc one has `|z|≤|p|<1` in the Gauss norm, so the geometric series converges. Thus `C_p=(g, y S_∞)=(g, y/D)` is an element of `Z_p⟨x,y⟩^2`. Reduction modulo `p` sends `S_∞` to `1`, hence `C_p` to `(x-x^p,y)`.

Determinant, as restricted series. For each finite `N`,

```text
D · S_N = (1-z) ∑_{j<N} z^j = 1 - z^N = 1 - p^N x^{N(p-1)}
```

is an identity in `Z[x]`. The remainder has Gauss norm `|p|^N→0`, so `D·S_∞=1` in `Z_p⟨x⟩`. The Jacobian matrix of `C_p` is triangular,

```text
J(C_p) = [[g', 0], [y ∂_x(S_∞), S_∞]],
```

and `det J(C_p)= g' S_∞ = D·S_∞=1`. This is an exact characteristic-zero identity in the Tate algebra, not a congruence at finite depth. The same identity modulo `p^n` is the reviewed cotangent tower.

Poles over `Qpbar`. `D(α)=0` if and only if `α^{p-1}=1/p`, hence `v_p(α)=-1/(p-1)<0`. In particular `|α|=p^{1/(p-1)}>1`, so every point of `V(D)` lies outside the closed unit bidisc. The polynomial `D(T)=1-p T^{p-1}` has derivative `D'=-p(p-1)T^{p-2}`. Euclid gives

```text
1 - p T^{p-1} = T · (-p T^{p-2}) + 1,
```

so `gcd(D, T^{p-2})=1` and therefore `gcd(D,D')=1` over `Q` and over `Z_p` (content of `D` is `1`). Thus `D` is separable. Over `Qpbar` it has exactly `p-1` distinct roots, and `E_p=V(D)` is the disjoint union of the `p-1` vertical lines `x=α`. (Over `Q_p` itself `D` is irreducible, by Eisenstein for `U^{p-1}-p` after inversion; the splitting is a feature of the algebraic closure, as the producer stated.)

Terminology. The phrase *exterior polar divisor* means the height-one polar divisor of the rational map `C_p` on algebraic `A^2`, consisting of points that are invisible on the integral unit bidisc. It is not the line at infinity of a projective compactification: the poles are affine, at finite `x=α`. It is not the campaign's `A_infinity`. The confirmed parent describes `A_infinity` as the residual factor of `L⊗_M E` recording geometric roots of a *hypothetical polynomial lift* `F` with `min(v(X),v(Y))<0` after localizing the formal tube at `(p)`. That is a property of the fibre algebra of `F`, not of the poles of this particular rational representative. The producer refuses the identification. No hidden identification was found.

Precision, non-blocking. The poles sit at Gauss radius `p^{1/(p-1)}`, strictly outside the Shilov boundary of the unit bidisc. Calling them “the boundary of the integral affinoid in this valuation sense” is informal; the load-bearing statements are the valuation, the count, reducedness, and the two refusals above.

### 2. No polynomial-gauge cancellation — CONFIRMED

Work over `K=Qpbar`. Let `φ=(X,Y)∈K[x,y]^2` satisfy `det J(φ)=1`. Then `X` is nonconstant: otherwise the Jacobian vanishes. Hence `D(X)=1-p X^{p-1}` is nonconstant.

Factor `D(T)=-p ∏_{α^{p-1}=1/p}(T-α)`. Suppose an irreducible `h∈K[x,y]` divides both `D(X)` and `Y`. Primality of `(h)` gives `h∣(X-α)` for some root `α`. Then `V(h)⊂φ^{-1}(α,0)`. The left side is a curve. The right side is a scheme-theoretic fibre of a morphism `A^2→A^2`.

Étaleness. The Jacobian criterion over a field of characteristic zero, with `det J(φ)=1` a unit, makes `φ` étale. Étale morphisms of finite type are quasi-finite: every fibre is zero-dimensional. A curve cannot be contained in a point fibre.

Differential form, used as the actual working argument and as the multiplicity handler. Write `X-α=h^m u` and `Y=h^k v` with `m,k≥1` and `h` dividing neither `u` nor `v`. Along `V(h)`:

- if `m≥2`, then `dX` vanishes identically, so `dX∧dY=0`;
- if `k≥2` and `m=1`, then `dY` vanishes and `dX` is a multiple of `dh`, so the wedge vanishes;
- if `m=k=1`, both `dX` and `dY` are multiples of `dh`, so the wedge vanishes.

In all cases `det J(φ)` vanishes along `V(h)`, contradicting `det J=1`. This is characteristic-zero (no `m=p` pathology) and does not use invertibility. It treats a reducible pullback factor by factor. The same vanishing of `dX` along `V(h)` when `h^2∣(X-α)` shows that `D(X)` itself is square-free, whether or not `h` divides `Y`. Thus each geometric component of `φ^* E_p` is reduced.

Consequently `gcd(D(X),Y)=1` in `K[x,y]`. The second coordinate of `C_p∘φ` is the reduced rational function `Y/D(X)`, whose polar divisor is the nonempty zero divisor of `D(X)`. That is (0.1).

What is invariant, versus what is merely noncancellable.

- If `φ` is a polynomial symplectic *automorphism*, then `Pol(C_p∘φ)=φ^* E_p`, and the inverse automorphism makes this a genuine equivalence invariant: nonvanishing, reducedness, and the `p-1` geometric components survive right composition. That is (3.5).
- If `φ` is merely a Keller map (`det J=1`, invertibility refused), the same gcd still forbids polynomiality of `C_p∘φ`, but the polar divisor need not be isomorphic to `E_p`: `X-α` may factor, and the number of components may grow. The producer records this distinction and does not claim the `p-1` count as a Keller invariant.

JC is not used. Quasi-finiteness of an étale endomorphism of `A^2` is not properness and is not invertibility.

### 3. Completed-orbit orientation — CONFIRMED

The confirmed wild theorem (producer §3, review Claim 4) states: if `A,B` are any two determinant-one restricted-analytic lifts of the fixed special map, there is a unique `φ≡id (mod p)` in `Aut Z_p⟨x,y⟩` with `A∘φ=B` and `det J(φ)=1`. Uniqueness is in the identity residue branch; reversing `A,B` produces the inverse; both `φ∘ψ` and `id` solve `A(H)=A` in that branch.

`C_p` is such a lift by Claim 1. A hypothetical polynomial `F` with `det J(F)=1` and `F≡(x-x^p,y) (mod p)` is such a lift. Taking `A=C_p` and `B=F` gives exactly

```text
C_p ∘ Φ_F = F,     Φ_F ≡ id (mod p),     det J(Φ_F)=1.
```

This is not `Φ_F∘C_p=F` and not `F∘Φ_F=C_p`. The wild chain-rule identity is `J(A)(φ) J(φ)=J(B)`, hence `det J(φ)=1` rather than a mere unit. Finite truncations of `Φ_F` are polynomial over `Z/p^n` because `Z_p⟨x,y⟩/p^n=(Z/p^n)[x,y]`; uniqueness of the identity branch makes those truncations canonical.

Firewall, checked against the body. No sentence of the producer asserts that `Φ_F` is rational or polynomial. No sentence drops `d` to `p`. No sentence supplies an element of `Aut_M(L)`. The construction sees only the completed unit bidisc, and is compatible with a possibly nonzero `A_infinity` of the global formal generic algebra. The `A_infinity` parent's descent key remains unearned.

### 4. Unbounded conductor — CONFIRMED

Write `Φ_F=(A,B)∈Z_p⟨x,y⟩^2`. For a restricted series `H=∑ c_{ij} x^i y^j` set

```text
deg_n(H) = max { i+j : v_p(c_{ij}) < n },
κ_n(F)   = max(deg_n(A), deg_n(B)).
```

Finiteness is the definition of a restricted series: only finitely many coefficients are nonzero modulo `p^n`. Canonicity is uniqueness in Claim 3. Nestedness: `v_p(c)<n` implies `v_p(c)<n+1`, so supports are nested and `κ_n` is nondecreasing.

Uniform degree bound. If `κ_n(F)≤B_0` for every `n`, every coefficient of total degree `>B_0` has valuation `≥n` for all `n`, hence is zero. Thus `Φ_F` is a polynomial map of degree `≤B_0`. From `C_p∘Φ_F=F` one has `F_2=B/D(A)` in `Q_p(x,y)`. Polynomiality of `F_2` and Gauss's lemma give `D(A)∣B` in `Q_p[x,y]`. Claim 2, applied to `Φ_F` (which satisfies `det J=1`), gives `gcd(D(A),B)=1`. Also `A≡x (mod p)`, so `A` is nonconstant and `D(A)` is nonconstant. A nonconstant polynomial cannot be a unit. Contradiction.

Uniform nested-support cardinality. The supports modulo `p^n` are nested finite sets. A uniform bound on their cardinalities forces the sequence to stabilize, hence the union to be finite. Coefficients off the union vanish, so `Φ_F` is polynomial, and the same contradiction applies. A common fixed finite support is stronger still.

Exact conclusion. A nondecreasing sequence of integers that is not bounded tends to infinity. That is (0.3). No rate is proved: the cotangent control itself grows linearly in `n`, but that is one representative, not a lower bound on the orbit. Coefficient integrality, or Gauss norm `≤1`, is automatic in `Z_p⟨x,y⟩` and does not algebraize: `S_∞` is the basic example.

This does not prove that a polynomial `F` is absent from the completed orbit. It proves that if such an `F` exists, its unique identity-branch analytic gauge cannot be polynomial, hence cannot have bounded truncation degree or bounded nested support. A polynomial point with unbounded relative analytic-gauge conductor remains compatible with everything proved here.

### 5. Finite-cap compactness — CONFIRMED

Over `R_n=Z/p^n` put `S_n=∑_{j<n} p^j x^{j(p-1)}` and `C_{(p,n)}=(g, y S_n)`. Then `det J(C_{(p,n)})=1` in `R_n[x,y]` by the finite geometric-series identity. For fixed total-degree caps `(D_F,D_φ)`, the set `B_{(p,n)}(D_F,D_φ)` consists of `φ=(X,Y)` over `R_n` with

```text
X≡x, Y≡y (mod p),     det J(X,Y)=1,
deg X, deg Y ≤ D_φ,     deg(g(X)), deg(Y S_n(X)) ≤ D_F.
```

These are finitely many polynomial congruences in the coefficients of the total-degree simplices of radius `D_φ`. There is no rectangular-support choice. If a point exists, `F=C_{(p,n)}∘φ` is automatically a determinant-one lift at that depth by the chain rule.

Reduction maps `B_{(p,n+1)}→B_{(p,n)}` exist: `S_{n+1}≡S_n (mod p^n)`, determinant one and the identity residue class survive reduction, and degree bounds are identical. Each level is a finite set (finite ring, finite monomials). Finite branching is `≤ p^{#coefficients}`.

König. Form the rooted tree whose depth-`n` nodes are the points of `B_{(p,n)}`, with parent the reduction map, and a formal root attached to `B_{(p,1)}`. If every level is nonempty the tree is infinite and locally finite. König's lemma supplies an infinite ray: a compatible system of coefficient tuples. (Dead-end nodes that do not lift are finite branches; they do not block the lemma. Equivalently, the stable images `I_n=∩_k im(B_{n+k}→B_n)` are nonempty finite sets with surjective transition maps, and the inverse limit of those is nonempty.)

The inverse limits `X,Y` are polynomials over `Z_p` of degree `≤ D_φ`, with `det J=1` and `φ≡id (mod p)`. The compositions `g(X)` and `Y S_n(X)` have degree `≤ D_F` at every finite level, so they inverse-limit to polynomials of degree `≤ D_F`. The second of these limits is `Y S_∞(X)=Y/D(X)` as restricted series, because `X∈Z_p[x,y]` has Gauss norm `≤1` and `p X^{p-1}` has Gauss norm `≤|p|<1`. A restricted series that equals a polynomial is a polynomial, so `D(X) Q = Y` as polynomials. Claim 2 then contradicts `gcd(D(X),Y)=1`.

Thus for every fixed pair of caps, `B_{(p,n)}` is empty for at least one finite `n`. This is an existence-of-a-finite-obstruction theorem. It does not produce a uniform formula for the first failing depth as a function of the caps.

Digit lifting, recorded correctly and not used as a substitute for the base search: once a depth-`n` point is fixed, the correction `p^n(r,s)` expands linearly over `F_p` modulo `p^{n+1}`. The search at the base level may be nonlinear. Both layers belong in a compiler; the present gate is the emptiness theorem, not a compiler.

### 6. All-odd-prime first cap — CONFIRMED

Depth two. `C_{(p,2)}=(x-x^p, y(1+p x^{p-1}))` has total degree `p`, Jacobian `1` in `R_2`, and `φ=id` satisfies (5.3) at `D_F=D_φ=p`. Nonempty.

Depth three. Write a general bounded gauge

```text
X = x + p r + p^2 r2,     Y = y + p s + p^2 s2,
deg(r,s,r2,s2) ≤ p.
```

Binomial expansion of `X^p` modulo `p^3`. For `0<k<p`, `v_p(C(p,k))=1`; the term `C(p,k) x^{p-k} (p r)^k` therefore has valuation `1+k`. For `k=1` this is the displayed `p^2 x^{p-1} r`. For `k≥2` one has valuation `≥3`. For `k=p`, `(p r)^p` has valuation `≥p≥3`. The mixed term `C(p,1) x^{p-1} (p^2 r2)` has valuation `3`. Thus, for every odd prime,

```text
X^p ≡ x^p + p^2 x^{p-1} r  (mod p^3),
g(X) ≡ g(x) + p r + p^2 (r2 - x^{p-1} r)  (mod p^3).
```

At `p=3` this is the explicit cube: `C(3,2)=3`, `3·(3r)^2=27 r^2 x^{1}`, and `(3r)^3=27 r^3`, both `0` modulo `27`. Direct multiplication gives `(x+3r+9 r2)^3 ≡ x^3 + 9 x^2 r (mod 27)`, independently of the binomial count. Oddness is necessary: at `p=2` the `k=2` term has valuation `2` and would contaminate the `p^2` digit.

First-coordinate cap. The `p^2` digit of `g(X)` is `r2 - x^{p-1} r`. The summand `r2` has degree `≤p`. Multiplication by `x^{p-1}` is injective on the monomial basis, and sends a monomial of total degree `d≥2` to a unique monomial of degree `d+p-1≥p+1`. No other term in (6.3) can cancel that monomial. Therefore every coefficient of `r` of total degree `≥2` vanishes. In particular `[x^p]r=0`. After this vanishing, `r` is affine. Linear and constant terms of `r` produce, after multiplication by `x^{p-1}`, degree `≤p`, which the cap allows and `r2` may cancel.

First determinant digit. Expanding `det J(X,Y)` modulo `p^2` gives `r_x+s_y=0` over `F_p`. The coefficient of `x^{p-1}`: in characteristic `p`, `∂_x(x^p)=0`, so `r_x` cannot contribute (and `[x^p]r` is already zero by the map cap). The unique source in `s_y` of `x^{p-1}` is `[x^{p-1} y]s`, because `deg s≤p` forbids a `y^{1+p m}` loophole. Hence `[x^{p-1} y]s=0`.

Second coordinate. `S_3(T)=1+p T^{p-1}+p^2 T^{2p-2}`. Working modulo `p^3` one needs `X^{p-1}` only modulo `p^2` and `X^{2p-2}` only modulo `p`:

```text
X^{p-1} ≡ x^{p-1} + p(p-1) x^{p-2} r  (mod p^2),
X^{2p-2} ≡ x^{2p-2}  (mod p).
```

Thus

```text
Y S_3(X) ≡ y + p(s + x^{p-1} y)
         + p^2 ( s2 + x^{p-1} s + (p-1) x^{p-2} r y + x^{2p-2} y )  (mod p^3).
```

The monomial `x^{2p-2} y` has total degree `2p-1>p`. Neither `s2` nor `r2` can reach it under the cap (`r2` is invisible in this digit: it would enter `X^{p-1}` at order `p^2`, then be multiplied by the outer `p`). The coefficient of `p^2 x^{2p-2} y` is therefore

```text
[x^{p-1} y]s + (p-1)[x^p]r + 1.
```

Both unknown coefficients have been forced to zero, and `p-1≢0 (mod p)`. The coefficient is `1` in `F_p`. It cannot vanish. Hence

```text
B_{(p,3)}(p,p) = ∅
```

for every odd prime.

The full gauge (6.2) was substituted, including `r2,s2` and every monomial of degree `≤p`. Extra binomial remainders have valuation `≥3`. The obstruction is a necessary consequence of (6.2) together with the two caps and first-order symplecticity; adding the unused `p^2` Jacobian digit cannot resurrect an already inconsistent system. At this particular Witt depth the digit equations happen to be affine — products of two copies of `p r` lie in `p^3` — but the statement remains a theorem about the full bounded gauge, not about an affine truncation of it.

Precision, non-blocking. Producer language “characteristic `p` kills the only possible `r_x` source `p[x^p]r`” mixes the characteristic-zero derivative with the first Witt digit. The actual first-digit computation is `∂_x(x^p)=0` over `F_p`. The conclusion `[x^{p-1} y]s=0` is unaffected. The map cap, not the gauge cap, is what kills `[x^p]r`; without it, `(p-1)[x^p]r` could have cancelled the `+1`. The producer’s degree argument is the one that does that killing.

Independent composition. Sparse integer polynomials with reduced digits, multiplied in `Z[x,y]` and reduced modulo `p^3`, matched (6.3)–(6.4) at `p=3,5,7`. After imposing the two vanishings, the forbidden coefficient was `1` in every trial, including `p=7`.

### 7. Exact controls — CONFIRMED

Number of monomials of total degree `≤p` in two variables is `(p+1)(p+2)/2`. Two coordinates give `(p+1)(p+2)` variables: `20` at `p=3`, `42` at `p=5`. Divergence outputs are all monomials of degree `≤p-1`, hence `p(p+1)/2` rows: `6` and `15`. High-`r` rows are that count minus the three affine monomials: `7` and `18`. Plus the inhomogeneous target: `14` and `34` necessary rows, matching the frozen JSON.

The independent `s`-first / `y`-major matrix, row-reduced both left-to-right and right-to-left over `F_p`, produced coefficient rank `12` and augmented rank `13` at `p=3`, and `32/33` at `p=5`, both inconsistent. Forbidden monomials `(2p-2,1)` are `x^4 y` and `x^8 y`. Forced coefficient after dividing by `p^2` is `1`. The Euclidean `gcd(D,D')` over `Q` is `1`. Cotangent total degrees through depths `2,3,4` are `3,5,7` at `p=3` and `5,9,13` at `p=5`, i.e. `(n-1)(p-1)+1`. All of this agrees with the frozen stdout, whose digest matches the registered replay byte-for-byte.

Extra, not registered: the same emptiness and a one-step rank jump occur at `p=7` (`60/61`) and `p=11` (`140/141`). Those numbers are a control, not a proof. The all-odd-prime emptiness is Claim 6.

Sample agreement is only a control on the structural proof. The registered script does not expand `X^p` or `Y S_3(X)`; it assumes (6.3)–(6.4) and row-reduces the necessary linear shadow. Using its ranks as the all-prime theorem would be a type failure. The producer does not do that.

### 8. Scope and successor — CONFIRMED

Preregistered stop outcomes were `POLAR-CONDUCTOR / UNBOUNDED-GAUGE`, `PULLBACK-CANCELLATION`, and `BOUNDED-D3-SURVIVOR`. Claims 1–2 close no-cancellation, so the second stop is not taken. Claim 6 closes emptiness of the registered cap at depth three, so the third stop is not taken. Claims 3–5 give unbounded canonical gauge degree/support for every hypothetical polynomial point of the unique completed orbit, and emptiness of every fixed simultaneous cap at some finite depth. The admissible result is exactly `POLAR-CONDUCTOR / UNBOUNDED-GAUGE`.

Quarantine, checked against the body:

- Nonexistence of a polynomial lift: refused in §0, §4, and §8. Unbounded `κ_n` is compatible with polynomial `F`.
- Identification of `E_p` with `A_infinity` or with projective infinity: refused in §1 and §8. The `A_infinity` parent remains a residual-sheet theorem about a hypothetical polynomial fibre algebra.
- Rational / polynomial deck descent: firewalled by the wild parent and not reopened.
- Global generic degree beyond the reviewed `d≥p`: not touched.
- `p=109` enumeration: not performed; the structural theorem is already uniform in odd `p`.
- JC2: none.

Smallest honest successor. Two directions, not interchangeable.

1. Quantitative conductor growth. From a bound on `deg F` or on the support of `F`, derive a lower envelope for `κ_n(F)`, or prove emptiness of `B_{(p,n)}(D_F, D_φ)` along a sequence of intrinsic caps, using digit-by-digit linear lifting plus exact nonlinear base components. This is the smallest successor that could exclude a *bounded-degree* polynomial point of the completed orbit. The present theorem does not do it: `κ_n→∞` has no rate, and the first failing depth is not given as a function of the caps.
2. Comparison with `A_infinity`. Prove a relation between the exterior valuation `-1/(p-1)` of `E_p` and the valued initial systems that count residual sheets of a polynomial lift. Until that theorem exists, the two uses of *boundary* must not be identified. This is an independent successor, not a corollary, and not smaller than (1) for the bounded-gauge programme this gate actually starts.

Neither successor is a `p=109` run, a deeper unrestricted cohomology computation, or a JC2 decision. Unrestricted completed gauge remains a single orbit by the wild parent; support becomes an obstruction only inside a uniformly bounded polynomial-gauge category, which is exactly what Claims 4–6 begin to test.

---

## Dependency and Tate-algebra caveats

- Logical dependency for Claims 1–8 is the exact-lift hypothesis (or the restricted-analytic analogue with `det J=1`), the confirmed wild right-equivalence, standard commutative algebra of Tate algebras and of étale maps of affine planes, and Gauss's lemma. Finite presentation of Tate algebras is not required beyond Claim 1's geometric series.
- Digit carries of the AS109 Hensel erratum are irrelevant. This gate consumes packed `det J=1`.
- The completed bidisc is the integral unit polydisc. Residual sheets of the confirmed `A_infinity` parent live at negative Gauss valuation after localizing the formal tube at `(p)`. The polar divisor of `C_p` lives at radius `p^{1/(p-1)}` on algebraic `A^2`. The two categories do not mix without a comparison theorem.
- Classical Galois Keller, TDU, Moskowicz, and bounded-`y` automorphy theorems are not inputs.
- The all-Witt / Tate control is the cotangent representative of Claims 1 and 6–7, already confirmed as a nonpolynomial inverse limit. This gate does not widen that control into a polynomial lift; it uses it as the basepoint of the unique completed orbit.

---

## Exact scope exclusions

Do not read this file, or the producer, as any of the following:

- a construction of an exact polynomial lift, series lift, or complex point;
- a proof that no exact lift exists;
- a rational or polynomial `C_p` deck transformation, or an element of `Aut_M(L)`;
- `A_infinity=0`, `d=p`, or an identification of `E_p` with `A_infinity` or with projective infinity;
- a growth law for `κ_n`, a uniform formula for the first failing depth at arbitrary caps, or a `p=109` computation;
- a licence to treat unrestricted finite-depth support as a completed-gauge invariant;
- a JC2 proof or counterexample.

---

## Smallest missing hypothesis or overclaim

None of the eight claims is an existence theorem, a nonexistence theorem, a global degree theorem, or a JC2 decision.

The smallest precision a reader could miss, and that this review therefore isolates, is that `C_p ∘ Φ_F = F` can hold with `F` polynomial and `Φ_F` a nonpolynomial restricted series: Claim 4 says that if a polynomial lift exists, this is exactly what must happen. Emptiness of a bounded-gauge cap is not emptiness of the completed orbit.

The smallest genuinely missing objects remain a lower growth law for `κ_n` in terms of a bound on `F`, emptiness of a sequence of intrinsic caps, or a proved comparison of `E_p` with `A_infinity`. Any of those would be a new paper. Unrestricted completed cohomology, residue-ball Hensel, and the first natural cap `p,p` do not supply them.

A cancellation that was available — a common factor of `D(X)` and `Y` for a noninvertible Keller map, or a `p=3` binomial remainder of valuation `2` — is not committed. The Jacobian-wedge argument and the explicit cube exist precisely to block those.

---

## Promotion advice

Accept internally as an exact, hostile-confirmed bounded-category gate

```text
exact AS109 lift (conditional)
  =>  unique identity-branch analytic gauge C_p ∘ Φ_F = F
      with κ_n(F) → ∞,
      every fixed simultaneous map/gauge cap empty at some finite depth,
      and the cap p,p empty at depth three for every odd prime;
      and none of this is a polynomial-lift exclusion,
      an A_infinity identification, a deck descent, or a JC2 decision.
```

Record it as `POLAR-CONDUCTOR / UNBOUNDED-GAUGE`. Do **not** promote it into `APPROACHES.md` as a kill of avenue 19, as `d=p`, as a fixed-support exclusion, as a `p=109` licence, or as any JC2 implication. Do **not** answer it by computing unrestricted deeper cohomology or by launching AWS. Successor work that wants a contradiction must bring a quantitative conductor law, a sequence of intrinsic caps, or a comparison theorem with `A_infinity`; this gate correctly refuses to invent them.
