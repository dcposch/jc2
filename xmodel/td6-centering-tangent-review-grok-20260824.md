# Hostile different-model review — TD6 full-cokernel centering tangent

| Field | Value |
|---|---|
| Claim under review | Frozen TD6-CENTERING-TANGENT: in the registered normalized section, the three common center jets are transverse to the reviewed regular source-reparametrization and rectangle-preserving target gauges at `(c1,c2,c3)=(1,1,1)`; exact matrix-changing differentiation of transport, both later parameterizations, and every current-band left-null compatibility gives an injective map `D C: E^3 → E^{10}` of rank three, with no common linearized root of `D C(v)=-C(1,1,1)` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Hidden local-to-global step | none: injective first-order sensitivity of an already nonzero current compatibility vector at a nonsolution is not a tangent space, not a nonlinear family kill, and not SP-2 / terminal-class / JC2 |
| Evidence tier | independent exact algebra over `Q` and `E=K[A]/(A^3-α)` (registered orbit audit and centering replay as provenance only; a second engine that does not import either centering program: own field/Rabin/norm proofs, own Laurent chart tangent and source/target/F1 ranks, own multinomial `dA` of the 3,602-column transport matrix, own solve of `A0 dx=-dA x0` with every dependent transport row checked, own two-form compilers for `[s^{-2}]J`, `[s^{-1}]J`, `[s^0]J-1`, and `[r^1](J-1)` that retain quadratic monomials and assert they cancel, own `Jet3` class and Dual GE including derivative-only columns, unreduced `λ(ε)^T A(ε)=0` with the two-summand identity, an independently chosen nonzero `3×3` minor on rows other than the producer’s lex-first triple, reverse-column and reverse-row ranks, and an independent affine solve of `D C v=-C0`); primary-source read of the completed adjoint and whole-`B` producer/reviews |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | charged basis `1e60fcedc8626650c7c7544ad296c3624173415f`; HEAD at close `a04affb7247fb5e87cad4e87f5926ab440254b24` (later AS/Faber commits; freeze-payload SHA-256 values unchanged) |
| Review window (UTC) | 2026-08-24T16:54:47Z – 2026-08-24T19:25:50Z |
| Python | 3.14.6; stdlib `fractions.Fraction` / `hashlib` only |
| Host | Darwin arm64 |

Producer inputs reread in full before any verdict:

- `xmodel/td6-centering-tangent-gate-20260824.md` (SHA-256 `15b08835512839d044c049b11ba889be1fbf06c52dc9ad6487e714910ac774d3`)
- `cases/td6_centering_tangent_20260824/replay.py` (SHA-256 `6b56865611cd44c506ea9cc665e0efb6616f512b8ddf611b3149d95c18ffa87e`)
- `cases/td6_centering_tangent_20260824/replay.stdout` (SHA-256 `c78b7fbbb4d3bb1ba7f5a63498efe35bc3cee51463a130f42113743d943144e8`)
- `cases/td6_centering_tangent_20260824/orbit_audit.py` (SHA-256 `4377e3079d109807dc7a0325ae1896205e58d31ff8ab84a3549af534619978db`)
- `cases/td6_centering_tangent_20260824/orbit_audit.stdout` (SHA-256 `5967696f796c6b0520186ca944ee64a9a2539ba52ba2de8c109424742698e68a`)
- `cases/td6_centering_tangent_20260824/README.md` (SHA-256 `f9a0b614ec3cdb90acfa4cab07d44f36602bb64885317b13634b69668075c83b`)
- `cases/td6_centering_tangent_20260824/MANIFEST.sha256` and `FREEZE.sha256` (both SHA-256 `983da3aca0f5018d00b72cf750285422b569e2f5afffe147d913f0552fa479c0`)

All seven freeze-file hashes match the launch prompt. The freeze file body is exactly the five producer payloads above; `MANIFEST.sha256` is the same byte string. `shasum -a 256 -c cases/td6_centering_tangent_20260824/MANIFEST.sha256` from the repository root reports all five files `OK`, and `cmp` of `MANIFEST.sha256` against `FREEZE.sha256` is silent. No producer, case, canonical, ladder, notes, prompt, log, run, or erratum file was edited. No AWS work was launched. All scratch work lived in `/tmp/td6_centering_tangent_review_20260824/`.

Frozen adjoint and whole-`B` payloads, working-tree hashes on disk at review time:

- adjoint producer `xmodel/td6-jet-orbit-adjoint-gate-20260824.md` SHA-256 `28a8869cf91f5e7d1e3601c52ee21742eca9187e57d7ac1065f22bcbd0ee402b`
- adjoint hostile review `xmodel/td6-jet-orbit-adjoint-review-grok-20260824.md` SHA-256 `2cd542615dfcc7b15dab3796adba0c91b84dcba606da6ff442b3d69dd4fb79f9` (overall **CONFIRMED**)
- exact dual replay `cases/td6_jet_orbit_adjoint_20260824/replay.py` SHA-256 `fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198`
- whole-`B` producer `xmodel/td6-boundary-qb-pencil-gate-20260824.md` SHA-256 `5e1f6b44e143360a41550ae552b20bef02325414f96c5fd469ba4d016eb5eb22`
- whole-`B` different-model review `xmodel/td6-boundary-qb-pencil-review-grok-20260824.md` SHA-256 `5c238f2bd3cf11422093184e1563f7671d0abd4b8f06a6fb5dfd7d380ac51319` (overall **CONFIRMED**)

The centering replay pins the adjoint dual replay at `fb138b0f59…` before import; that dual replay pins the q2 compiler at `0ba18447…` and the uniform-third replay at `7a21f949…`. No imported-hash mismatch.

Cited canonical SP-2 / F1 / r9-M2 material, working-tree hashes on disk at review time:

- `ladder/SHEET6.md` SHA-256 `5ea8003685a8be0c2554f6966987cbd492583bf9c07603ccb984da48b3ac04f2`
- `ladder/SHEET6-LROOT.md` SHA-256 `9ff5d00567d7b6752ecc79892bb41959a450ddff3837bdb26179899ad2dfad5a` (SP-2 ledger 187–200)

**Promotion.** Accept as `CENTERING-TRANSVERSE / FULL-COKERNEL-INJECTIVE / NO-COMMON-LINEARIZED-ROOT / C1-PENCIL-LICENSED` of the three common-center jets **in this registered normalized section**. Bank the degree-18 field, the Laurent chart tangent (1), quotient rank three against regular source reparametrizations and the four rectangle-preserving det-1 target gauges, source tangent rank `4/4` in `(S,D,L,A)`, staged ranks `3470/3602 → 38/132 → 38/94 → 25/56` with vanishing derivative rank-change flags, the `t^4` residue and its three nonzero coordinate sensitivities, `λ'` support three, the exact `10×3` map of rank three and kernel zero, the augmented rank four, and the inconsistent affine equation `D C(v)=-C(1,1,1)`. Promote nothing else.

**Quarantine.** `centering_family_killed=false`, `SP2_killed=false`, and `JC2_resolved=false` remain hard. Injectivity of `D C` at an already inconsistent normalized control is sensitivity information, not a tangent space at a solution and not a kill of remote or nonlinear center roots. Dead stretch, other boundary jets, other F1/pole normalizations, SP-2, every td=6 terminal class, and JC2 remain open. Exact `J=1` is not proved or disproved.

---

## Headline and subclaim table

Write `s=y^{-1}`, `x=c_1 s+c_2 s^2+c_3 s^3+t s^4` at the base point `(c_1,c_2,c_3)=(1,1,1)`, F1 chart `x=q^{-5}`, `y=η q`, pole chart `x=r^{-25}`, `y=r^5+ζ r^{17}`, and on the imported sextic field `D=(2S^2-2S+3)/5`, `L=25(1-S+D)`, `A^3=9/L^8`.

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | In the registered normalized section, the three center jets have chart tangents `δt=-δc_1 s^{-3}-δc_2 s^{-2}-δc_3 s^{-1}` at fixed global `(x,y)`. Regular source reparametrizations have nonnegative `s`-support and cannot meet those Laurent monomials. `q'=1+25t^{24}` is a unit, so a boundary-preserving regular `t`-reparametrization has `h=0`. The four rectangle-preserving det-1 target gauges have rank four, Jacobian first-order sensitivity zero, and center projection zero. The qualifier “in this registered normalized section” is load-bearing | **CONFIRMED** | a regular `h∈E[[s,t]]` with a negative `s`-slot; `q'` a zero-divisor; a listed target gauge carrying a `chart_t` slot; a source automorphism of the registered charts/rectangles that absorbs a center direction |
| 2 | Independently differentiating the 3,602-column transport matrix and solving `A_0 δx=-δA x_0` in all three directions, without reusing a stale particular solution, reproduces ranks `3470/3602 → 38/132 → 38/94 → 25/56`. Every dependent transport row remains zero to first order. All derivative-only rank-change flags vanish | **CONFIRMED** | a leftover differentiated transport compatibility; any stated rank different; a nonzero rank-change flag; Dual GE that skipped derivative-only columns and still printed the advertised ranks |
| 3 | All ten current compatibilities are differentiated, including their left-null vectors. The `t^4` calculation contains the `λ'` contribution and is not merely `λ_0(δb-δA x_0)`. The three coordinate sensitivities of the first `t^4` residue are all nonzero in `E` | **CONFIRMED** | `λ'` support `0`; `λ_0^T b'` equal to the full derivative in any direction; a vanishing `dc_i` residue |
| 4 | The exact `10×3` map over `E` has rank three and kernel zero, certified by an independently chosen nonzero `3×3` minor on rows other than the producer’s lex-first triple. `[D C | -C_0]` has rank four, certified by an independently chosen nonzero `4×4` minor. The affine equation has no solution. Rank is stable to reverse-column and reverse-row order | **CONFIRMED** | every `3×3` minor zero; a nonzero kernel vector; augmented rank `3`; an exact affine root; reverse-column rank drop |
| 5 | The frozen `(S,D,L,A)` source block has rank `4/4` over `E`, using `F(7/4)=-53875/512≠0`. `q'` is a unit on the boundary section. The four target gauges have zero center projection. No registered chart, pole, or F1 tangent creates a hidden quotient direction. No larger legitimate global equivalence of this section was found | **CONFIRMED** | `F(7/4)=0`; source rank `<4`; a target or F1/pole vector with a center slot; a polynomial source automorphism keeping all three charts and both rectangles while absorbing a center |
| 6 | The base normalized control is already affine inconsistent, so injective `D C` is sensitivity at a nonsolution, not a tangent-space or nonlinear family kill. No inference to absence of remote/nonlinear center roots, uniformity in other moduli, SP-2, a terminal class, or JC2 is licensed. An exact matrix-changing `c1=C,c2=c3=1` pencil is the smallest licensed successor | **CONFIRMED** | producer promoting a family kill, an SP-2 or class kill, or JC2; printed flags `centering_family_killed`, `SP2_killed`, or `JC2_resolved` true; a cheaper successor that froze the transport matrix |

All remarks below are non-blocking unless marked otherwise. None changes a rank, a residue, a hash, or a verdict.

---

## Replay

Registered commands, rerun unmodified from the charged tree:

```sh
python3 cases/td6_centering_tangent_20260824/orbit_audit.py
python3 cases/td6_centering_tangent_20260824/replay.py
```

Exit codes 0. Wall-clock of the centering replay `real 1364.46`. Printed verdicts, character-for-character against the frozen stdout files:

```text
TD6-CENTERING-ORBIT-AUDIT: PASS
center_chart_tangents = -s^-3,-s^-2,-s^-1
regular_source_intersection = 0
qprime_unit_boundary_section = true
target_gauge_rank = 4
target_gauge_center_projection_rank = 0
centering_quotient_rank = 3
normalized_section_transversality_caveat = true
```

```text
TD6-CENTERING-MATRIX-TANGENT: PASS
transport_rank = 3470/3602; dimension=132
first_J_rank = 38/132; dimension=94
previous_pole_rank = 38/94; dimension=56
current_homogeneous_rank = 25/56
current_pivots_before_t4 = 3/56
...
centering_joint_image_rank_over_E = 3
centering_joint_kernel_dimension_over_E = 0
centering_joint_augmented_rank_over_E = 4
centering_joint_linearized_root_exists = False
rank_change_flags = {'first': [0, 0, 0], 'previous': [0, 0, 0], 'current_through_stop': [0, 0, 0], 'current_full': [0, 0, 0]}
centering_family_killed = false
SP2_killed = false
JC2_resolved = false
```

Canonical stdout SHA-256 values, including final newlines, match the freeze (`5967696f…` / `c78b7fbb…`). Arithmetic is `fractions.Fraction` on the residue field `E`. No CAS, no floating point, no modular sampling of the Jacobian system, no AWS.

These two programs are regressions. A second engine, written for this review and not imported from either centering program, then:

1. rebuilt the 3,602-column transport matrix from the hash-pinned first-band compiler and independently formed `δA` from the multinomial expansion of `(c_1 s+c_2 s^2+c_3 s^3+t s^4)^i` at `(1,1,1)`;
2. solved `A_0 δx=-δA x_0` on the frozen rational echelon, holding free-coordinate derivatives at zero, and asserted every differentiated dependent transport row is the zero form;
3. compiled `[s^{-2}]J`, `[s^{-1}]J`, `[s^0]J-1`, and `[r^1](J-1)` from the two-form identities, retaining quadratic monomials and asserting they cancel;
4. ran its own `Jet3` Dual GE that reduces derivative-only entries in already-pivoted columns;
5. split `c'(0)=λ_0^T b'(0)+λ'(0)^T b_0` in each of the three directions and checked that the frozen-`λ_0` formula is not the derivative;
6. formed the exact `10×3` map, ranked it by least-column and reverse-column GE, certified rank three by a `3×3` minor on rows `(t^4,t^7,t^{10})` rather than the producer’s lex-first triple, ranked `[D C|-C_0]` by an independent last-four `4×4`, and solved the affine equation.

Wall-clock `real 1605.41`. Every stated rank, the `t^4` inconsistency, all three residue-derivative hashes, the ten-row compatibility digest, the lex-first `3×3` hash as a consistency check, the vanishing rank-change flags, and the linearized-root failure matched. A separate exact field/orbit/gauge engine, also not imported from `orbit_audit.py`, independently reconstructed claim 1 and claim 5.

---

## 1. Scope and quotient

SP-2 from `SHEET6-LROOT.md:187–200`: chain

```text
F0 = (3,6,5,2,8) → F1 = (15,60,5,4,4)  (μ=2 IIa k=2, n=12) → (0,y),
```

type `(3,5)`, rectangles `(15,60)/(25,100)`, reduced F1 pattern `(η^5-c^5)^2 Π_2`, one x-cluster. With the chain orbit normalized to `C=1` this is `R(z)=(z-1)^2(z^2-Sz+D)`. The r9/M2 pole shape is the AF3 §4 family transported by `L=25(1-S+D)` and normalized by `L^8 A^3=9`. Zero dead stretch and common centering `(1,1,1)` are the same licensed specializations already confirmed by the first-band through whole-`B` reviews.

Independent field presentation. `F=24S^6-252S^5+1170S^4-3045S^3+4680S^2-4032S+1411` satisfies `F=0` in `K` by construction. `gcd(F,F')=1` over `Q`, so `F` is squarefree. Rabin’s criterion modulo 31 (prime divisors of six are 2 and 3) gives `gcd(F, x^{31^2}-x)=1`, `gcd(F, x^{31^3}-x)=1`, and `x^{31^6}≡x`, so `F` is irreducible over `F_{31}` and therefore over `Q`. Thus `K=Q[S]/(F)` is a degree-6 field.

The source relations `Q=-2S^2+2S+5D-3=0`, `D=(2S^2-2S+3)/5`, `H=1-S+D`, `3H^3=1`, `L=25H`, and `α=9/L^8` hold identically in `K`. The multiplication-by-`α` determinant on the `Q`-basis `1,S,…,S^5` is

```text
N_{K/Q}(α) = 3^{28}/5^{96}.
```

The 3-adic valuation 28 is not divisible by 3, so `α` is not a cube in `K`, so `T^3-α` is irreducible over `K`. Hence `E=K[A]/(A^3-α)` is a degree-18 field. There are no zero-divisors to hide a vanishing residue at one conjugate.

Chart tangent at fixed global `(x,y)`, independently of the producer audit. `y=s^{-1}` pins `s`. Differentiating `x=c_1 s+c_2 s^2+c_3 s^3+t s^4` at fixed `x` gives

```text
0 = δc_1 s + δc_2 s^2 + δc_3 s^3 + δt s^4,
```

hence (1):

```text
δt = -δc_1 s^{-3} - δc_2 s^{-2} - δc_3 s^{-1}.
```

The three vectors have rank three, and every displayed `s`-exponent is strictly negative.

A regular truncated source reparametrization has `δt∈E[[s,t]]`, so every `s`-exponent is nonnegative. Least-index reduction of an 8-by-10 spanning sample of nonnegative monomials has rank 80; adjoining the three center vectors raises the rank to 83. The supports are disjoint as monomials, so the conclusion is not an artifact of the truncated sample: no regular order meets (1). Independently, the eight jet vectors `h=1,t,…,t^7` of a pure `t`-reparametrization have rank eight and remain rank eleven after adjoining the centers.

On the registered boundary `q=t+t^{25}`, one has `q'=1+25 t^{24}`. For each `h=t^k` with `k=0,…,11` the product `q'h` has leading slot `t^k` with coefficient `1`. Thus `q'` is a unit of `E[[t]]`, with formal inverse `1-25 t^{24}+O(t^{48})`. A regular reparametrization preserving `δq=0` therefore has `h=0`. That is the boundary counterpart of the Laurent-support argument; it does not use a finite spanning sample as the general reason.

Four rectangle-preserving determinant-one target tangents, as raw boundary vectors:

| gauge | boundary vector | Jacobian to first order |
|---|---|---|
| translation of `f` | `δp=1` | `δJ=0` identically |
| translation of `g` | `δq=1` | `δJ=0` identically |
| reciprocal scaling | `(δp,δq)=(p,-q)` | `J((1+ε)f,(1-ε)g)=(1-ε^2)J`, so `[ε^1]=0` |
| lower shear | `δq=p` i.e. `g↦g+ε f` | `f_x(g_y+ε f_y)-f_y(g_x+ε f_x)=J` identically |

These are identities of `J=f_x g_y-f_y g_x`. Upper shear `f↦f+ε g` would raise `deg f` from 15 to 25 and leave the rectangle; it is correctly omitted. Rank of the four is four. None carries a `chart_t` slot, so the center projection is zero: rank of targets plus centers is seven. Rank of regular source plus targets plus centers is regular-plus-target rank plus three.

F1 chart `x=q^{-5}`, `y=η q` and pole chart `x=r^{-25}`, `y=r^5+ζ r^{17}` do not mention `(c_1,c_2,c_3)`. Their transport rows are therefore center-independent; only the X-chart expansion of global monomials sees the centers. That is independently visible in `δA`: every differentiated transport row has owner-chart key `X`.

The qualifier “in this registered normalized section” is load-bearing. A later global-domain normalization that changed the other charts, the fixed rectangles, or the identification of `t` would be a different equivalence relation and would have to redo the quotient. No such automorphism is exhibited, and none is being declared a residual gauge here.

A power series `R=ρ t^4+O(t^5)` is invariant in degree four under `t↦t+ε t^k` for every `k≥2`, because the first-order term is `4ρ ε t^{3+k}`. Scaling `k=1` does move `[t^4]`; that direction is already in the target reciprocal-scaling / chart-normalization quotient, not a center slot. This is the correct negative control for a regular coordinate rename, and it does not absorb (1).

Claim 1 stands.

---

## 2. Matrix-changing differentiation

Changing a center changes the 3,602-column transport matrix, because `[s^a t^b]` of `x^i y^j` is the multinomial expansion of `(c_1 s+c_2 s^2+c_3 s^3+t s^4)^i s^{-j}`. The independent engine did not reuse a stale particular solution. It rebuilt `A_0` from the hash-pinned first-band compiler at `(1,1,1)`, matched every X-row coefficientwise against that compiler’s `x_power_expansion`, formed `δA` by differentiating the same multinomials (`∂/∂c_1` multiplies the `a_1`-slot by `a_1`, and cyclically), and solved

```text
A_0 δx = -δA x_0
```

on the frozen rank-3,470 echelon, with free-coordinate derivatives held at zero. Every differentiated dependent transport row reduced to the zero affine form in all three directions. F1 and pole rows have `δA=0`; their first-order identities are inherited from `δx` alone.

Pulled-back x-bands used the product rule: variation of the global coefficients from the differentiated transport, plus direct variation of the chart row. Pole coefficients were rebuilt from `-25 i+5 j+12 ζ=exponent` with binomial weights `C(j,ζ)` and matched the next-row formula coefficientwise; they see centers only through `δx`.

Independent `Jet3` Dual GE, reducing every already-pivoted column including a coefficient that is derivative-only:

| stage | independent result |
|---|---|
| two-chart transport | rank `3470/3602`, dimension 132; all differentiated dependent rows zero |
| first centered Jacobian | rank `38/132`, dimension 94; Dual rank-change flags `[0,0,0]` |
| previous centered + inherited pole | rank `38/94`, dimension 56; Dual rank-change flags `[0,0,0]` |
| current homogeneous | rank `25/56` (insertion order and reverse-row); Dual rank-change flags `[0,0,0]` |
| current affine | empty at input row `("X0",4)` after three Dual pivots |

Affine parameterizations were substituted back into every original first and previous/pole equation over `Jet3`. Quadratic monomials in `f_1 g_1'` and the analogous current/pole products cancelled identically (`previous_quadratic_cancelled=0`, `pole_quadratic_cancelled=0`, `current_quadratic_cancelled=0`). That cancellation is a structural fact of these bands on the transported family, not the producer `len(monomial)==1` assertion.

Free Dual coordinates held at zero derivative are a section of the affine family, valid on the observed first-order rank-stable stratum. They are not a proof that the same index set of free variables is generic off `(1,1,1)`. Homogeneous transport rank `3470` is the rank of `A_0`, not evidence that first-Jacobian rank `38` is generic in the centers.

Claim 2 stands.

---

## 3. Varying left-null space

The current system has 35 rows. Homogeneous rank 25, hence ten exact dependent compatibilities, at input rows

```text
t^0, t^4, t^5, t^6, t^7, t^8, t^9, t^{10}, t^{11}, t^{12}.
```

The first affine contradiction is `t^4` after three current pivots, as advertised. Row `t^0` is a compatibility with vanishing base residue: it is the constant row already cut by the field `E`. Its derivatives still enter `D C`. Continuing past `t^4` is the correct extraction of the compatibility cokernel.

The normalized left-null of the `t^4` obstruction has support four and derivative support three. Direct multiplication against the unreduced current matrix proves `λ(ε)^T A(ε)=0` and

```text
λ(ε)^T b(ε) = ρ + (∂_{c_1}ρ) dc_1 + (∂_{c_2}ρ) dc_2 + (∂_{c_3}ρ) dc_3,
```

with the advertised base residue

```text
ρ = (2495634 - 4154976 S + 4405068 S^2
     - 2488119 S^3 + 761922 S^4 - 105084 S^5)/3625
    + (136875/29) A.
```

The two-summand identity holds in each direction as an identity of that syzygy, not a fit:

```text
∂_{c_i}ρ = λ_0^T (∂_{c_i} b) + (∂_{c_i} λ)^T b_0.
```

Independently, `λ_0^T (∂_{c_i} b)` is not `∂_{c_i}ρ` in any of the three directions. That is the common invalid shortcut, independently refuted: `λ'` is nonzero on three of the four current rows that support the syzygy. The three coordinate sensitivities are all nonzero in `E` (each has a nonzero `A`-component in the `K`-basis `1,A,A^2`):

```text
dc1 sha256 23afdddfcea7985ec8764c34bd5f0293f7f7f2d33a6cb7683bad5554fe09fcd1
dc2 sha256 0848e6c9a543de1600f67411fd0867ba1cca76cbbce22ace7aa2eadeb8218b92
dc3 sha256 6a65174bab17999e5ce229937e9a2d22b75a538fa32663e7d973c40e08596ec4
```

These three hashes match the freeze. The full ten-row multidual compatibility digest is

```text
8fc63678526c16182a2eb8b318b1a41de3983c6d467ae4942137ef2361117d26,
```

matching the freeze. A printed left-null digest that folds `repr` of the dual object is representation-dependent on the dual class name; it is not used as a rank certificate. The load-bearing identities are the two-summand split, the three residue hashes, and the ten-row digest.

The one-functional kernel of `t^4` alone is two-dimensional over `E`, as the producer warned. No direction should be selected from that single-row kernel. The intersection of all ten kernels is the object ranked in claim 4.

Claim 3 stands.

---

## 4. Full cokernel ranks

The exact `10×3` sensitivity matrix over `E` was ranked by least-column GE and by reverse-column GE. Both give rank three and kernel dimension zero. Because `E` is a field, this rank is independent of the `K`-basis presentation of `E` and of the ordering of `{dc_1,dc_2,dc_3}` up to that reversal.

An independently chosen nonzero `3×3` minor, not the producer’s lexicographic first triple, sits on rows `(t^4, t^7, t^{10})` and is nonzero in `E`. The last-three triple `(t^{10},t^{11},t^{12})` has vanishing determinant; that is a linear dependence among those three rows, not a rank drop of the `10×3` map. Rank three is therefore not an artifact of the producer’s pivot schedule, of lex-first row search, or of including the field-defining row `t^0`. The producer’s lex-first minor on `(t^0,t^4,t^5)` is independently nonzero and hashes to the freeze value

```text
7c7ed8953e421e68dd4845f17972b7d1427f7c13d37c65a97591ce5126a45ab2.
```

Cramer’s rule on the independent `(t^4,t^7,t^{10})` triple produces a candidate Newton step that fails on the other seven compatibility rows, including `t^0`. So even a `3×3` subsystem that ignores the field-defining row cannot cancel the full residue vector.

The augmented matrix `[D C | -C_0]` has rank four by least-column GE and by reverse-column GE. An independently chosen nonzero `4×4` minor on the last four rows `(t^9,t^{10},t^{11},t^{12})` is nonzero in `E`. Least-column affine GE of `D C(v)=-C_0` fails at compatibility index 3 (input row `t^6`), with the same leftover residue the producer printed. There is no common linearized root.

Reverse-row homogeneous rank of the 35-row current matrix over `E` is again 25. Insertion-order Dual rank and reverse-row `E` rank therefore agree. Field-reduction conventions (least-column vs reverse-column, Dual vs base-only, lex-first vs last-available nonzero minor) do not change the ranks `3` and `4`.

Claim 4 stands.

---

## 5. Orbit / source audit

F1/pole source tangent, independently reconstructed from the frozen equations `Q=-2S^2+2S+5D-3=0`, `H=1-S+D`, `3H^3=1`, `L=25H`, `L^8 A^3=9`:

```text
(-4S+2) dS + 5 dD           = 0,
-9 H^2 dS + 9 H^2 dD         = 0,
25 dS - 25 dD + dL           = 0,
(8/L) dL + (3/A) dA          = 0.
```

Least-index field GE over `E` has rank `4/4`. The first two rows have determinant `9 H^2 (7-4S)`. The identity `3H^3=1` forces `H≠0`. Direct evaluation of `F` at `S=7/4` is the rational `-53875/512≠0`, so `7-4S≠0` in `K`. There is no source-compatible tangent in `(S,D,L,A)` alone.

`q'=1+25 t^{24}` is a unit, as in §1. The four target gauges have zero center projection, as in §1. F1 and pole charts do not carry a center slot. The eleven r9 dead-stretch slots `d_6,…,d_{16}` remain licensed omitted data: no source automorphism is exhibited that would normalize them while keeping all three charts and both rectangles. They are not silently placed in the gauge subspace of this section.

No larger legitimate global equivalence of the registered section was found. A hypothetical later theorem that unfroze centering by changing the other charts or the rectangles would be a different statement; it is not claimed, and the producer correctly flags `normalized_section_transversality_caveat=true`. There is no smallest correction to the quotient rank, because no extra gauge was found.

Claim 5 stands.

---

## 6. Logical meaning and successor

The base normalized control is already affine inconsistent: the `t^4` residue `ρ` is a nonzero element of `E`. The derivative `D C` is therefore the sensitivity of an obstruction at a nonsolution, not the tangent space of a solution scheme. Injective `D C` means that no infinitesimal common-center step kills all ten current compatibilities to first order, and that no single Newton step `v` solves `C(1,1,1)+D C(v)=0`. It does not mean:

- emptiness of any positive-dimensional center family;
- absence of a nonlinear root at another center, including a remote point at which a pivot jumps;
- a statement uniform in boundary, dead-stretch, F1, or pole moduli;
- an SP-2, terminal-class, or JC2 decision.

Printed flags `centering_family_killed=false`, `SP2_killed=false`, and `JC2_resolved=false` match that scope and are replayed.

After kernel zero, every line through `(1,1,1)` is a licensed one-parameter test. The sparsest monomial choice is a coordinate axis. The line `(c_1,c_2,c_3)=(C,1,1)` is one such axis; `(1,C,1)` and `(1,1,C)` are equally sparse. The producer’s choice `c_1=C` is conventional (leading center) and is the smallest honest successor of this gate: it must factor the genuinely changing transport matrix over `Q(C)`, carry the affine solve into the small `E(C)` stages, record every pivot numerator and denominator, and rebuild every exceptional specialization before any family claim. Interpolation without a proved degree bound is not licensed. A frozen `λ_0` kernel is not a cheaper certificate: `λ'` support 3 kills it.

Claim 6 stands.

---

## Parameter, staging, and field caveats (non-blocking)

1. `F` and `E` are imported from the frozen uniform-third gate, independently re-certified here by Rabin, `gcd(F,F')`, and the norm of `α`. They are not re-derived as the constant-row polynomial of the center family.
2. Dual free coordinates are held at zero derivative. That is a section of the affine family, valid on the observed first-order rank-stable stratum.
3. Homogeneous transport rank `3470` is the rank of `A_0` and is not evidence that first-Jacobian rank `38` is generic in the centers.
4. Some `3×3` minors of `D C` vanish, including the last-three triple `(t^{10},t^{11},t^{12})`. Rank three is the existence of some nonzero minor, independently certified on `(t^4,t^7,t^{10})`.
5. Row `t^0` is a compatibility with vanishing base residue. Rank three remains after excluding it from the independent minor.
6. Quadratic monomials in the compiled two-forms cancel on this transported family. The independent compiler kept those terms and asserted they vanished.
7. Target-gauge Jacobian identities are identities of `J`, not four extra 3,602-variable Dual pencils.
8. A printed left-null digest that includes `repr` of a dual number is representation-dependent on the dual class. Residual-value hashes and the ten-row compatibility digest are the load-bearing certificates.
9. HEAD moved from the charged basis `1e60fce…` to `a04affb…` by later AS/Faber commits during the review window. Freeze-payload SHA-256 values were unchanged.

---

## Hashes

| artifact | SHA-256 |
|---|---|
| producer report | `15b08835512839d044c049b11ba889be1fbf06c52dc9ad6487e714910ac774d3` |
| exact centering replay | `6b56865611cd44c506ea9cc665e0efb6616f512b8ddf611b3149d95c18ffa87e` |
| canonical replay stdout | `c78b7fbbb4d3bb1ba7f5a63498efe35bc3cee51463a130f42113743d943144e8` |
| orbit/source audit | `4377e3079d109807dc7a0325ae1896205e58d31ff8ab84a3549af534619978db` |
| canonical orbit stdout | `5967696f796c6b0520186ca944ee64a9a2539ba52ba2de8c109424742698e68a` |
| README | `f9a0b614ec3cdb90acfa4cab07d44f36602bb64885317b13634b69668075c83b` |
| manifest / freeze | `983da3aca0f5018d00b72cf750285422b569e2f5afffe147d913f0552fa479c0` |
| `t^4` residue `dc1` | `23afdddfcea7985ec8764c34bd5f0293f7f7f2d33a6cb7683bad5554fe09fcd1` |
| `t^4` residue `dc2` | `0848e6c9a543de1600f67411fd0867ba1cca76cbbce22ace7aa2eadeb8218b92` |
| `t^4` residue `dc3` | `6a65174bab17999e5ce229937e9a2d22b75a538fa32663e7d973c40e08596ec4` |
| ten-row compatibility digest | `8fc63678526c16182a2eb8b318b1a41de3983c6d467ae4942137ef2361117d26` |
| lex-first `3×3` minor | `7c7ed8953e421e68dd4845f17972b7d1427f7c13d37c65a97591ce5126a45ab2` |
| independent `3×3` on `(t^4,t^7,t^{10})` | `e2323e2f60c5dc99ee701dc2f82f574f95539f1015f85a5d03bffa3a39b0db72` |
| independent `4×4` on `(t^9,…,t^{12})` | `464b33cb8a0545316ea4d07c42bb708dbc17eed667db98fec4148752e21960da` |
| adjoint producer | `28a8869cf91f5e7d1e3601c52ee21742eca9187e57d7ac1065f22bcbd0ee402b` |
| adjoint hostile review | `2cd542615dfcc7b15dab3796adba0c91b84dcba606da6ff442b3d69dd4fb79f9` |
| whole-`B` producer | `5e1f6b44e143360a41550ae552b20bef02325414f96c5fd469ba4d016eb5eb22` |
| whole-`B` hostile review | `5c238f2bd3cf11422093184e1563f7671d0abd4b8f06a6fb5dfd7d380ac51319` |
| imported dual replay | `fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198` |
| imported first-band replay | `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735` |
| imported next-row replay | `0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8` |
| imported uniform-third replay | `7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8` |

**JC2 scope.** This is an exact first-order full-cokernel sensitivity certificate for the three common-center jets inside one registered normalized SP-2 chart-pattern control. The center family is not killed. The calculation neither realizes nor kills a terminal class, supplies no Keller pair, does not quantify dead-stretch or other boundary moduli, and neither proves nor disproves the plane Jacobian conjecture.
