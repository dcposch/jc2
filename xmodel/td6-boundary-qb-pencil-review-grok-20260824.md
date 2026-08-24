# Hostile different-model review — TD6 exact `q_B` boundary pencil

| Field | Value |
|---|---|
| Claim under review | Frozen TD6-QB-PENCIL: at the degree-18 sextic points of the frozen normalized SP-2 control, the licensed transverse family `p=t^{15}`, `q_B=t+B t^2+t^{25}` has no solution for any `B`, even after extending the residue field; staged exact elimination over untruncated `E[B]` has constant ranks `3470/3602 → 38/132 → 38/94 → 25/56`, all 101 normalized leads are B-independent units, and `gcd(N_4,N_{13})=1` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Hidden local-to-global step | none: emptiness of this one licensed one-parameter q2 pencil, in the fixed normalized section with frozen centering and zero dead stretch, is not a kill of those omitted matrix-changing families, of other boundary jets, of SP-2, of a terminal class, or of JC2 |
| Evidence tier | independent exact algebra over `Q`, `K=Q[S]/(F)`, and `E=K[A]/(A^3-α)` (registered cache rebuild and `E[B]` replay as provenance only; a second engine that does not import the pencil replay, `transport_cache.load_cache`, or the producer’s normalized forms: own field/Rabin/norm/unit proofs, own source-orbit/target-gauge/F1-tangent ranks, reconstruction of every cached section from the raw 3,602-column transport matrix, own two-form compilers for `[s^{-2}]J`, `[s^{-1}]J`, `[s^0]J-1`, and `[r^1](J-1)`, own dense `Poly` class and least-index `E[B]` GE, coefficientwise affine rebuild, unreduced left-null multiply, and an algebraic Bezout/`gcd` argument that does not sample points); primary-source read of the completed adjoint and parent q2 / uniform-third producer/reviews |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `c327bdc8d02472feba42573760325099f34b8cdf` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T15:43:37Z – 2026-08-24T15:59:52Z |
| Python | 3.14.6; stdlib `fractions.Fraction` / `hashlib` only |
| Host | Darwin arm64 |

Producer inputs reread in full before any verdict:

- `xmodel/td6-boundary-qb-pencil-gate-20260824.md` (SHA-256 `5e1f6b44e143360a41550ae552b20bef02325414f96c5fd469ba4d016eb5eb22`)
- `cases/td6_boundary_qb_pencil_20260824/replay.py` (SHA-256 `fab27e808ce0f840e82359d01f83834c874c168f6414f550e253d94aac42360c`)
- `cases/td6_boundary_qb_pencil_20260824/replay.stdout` (SHA-256 `9326e8430ce76afb4c57d868fa0659a690c5c3a0cd3b6a7225c5095fefac7f48`)
- `cases/td6_boundary_qb_pencil_20260824/transport_sections.json` (SHA-256 `3855b1d8aa98d3602bbba3630512600b4af66eba81103fea1bc8be286fabebb4`)
- `cases/td6_boundary_qb_pencil_20260824/build_transport_cache.py` (SHA-256 `78d06b9f64c80bd1fd328e5960b4512fe6a9c574ef53c47d63a58d56b9326328`)
- `cases/td6_boundary_qb_pencil_20260824/build_transport_cache.stdout` (SHA-256 `cd8e8e070d055ebaa339f34ae524d0e163b29c2b929c5d546448068ae036e032`)
- `cases/td6_boundary_qb_pencil_20260824/transport_cache.py` (SHA-256 `11521a7e25d85c7f8bb6ab5173c6489d08a13edf705e6e742c10211e6e152724`)
- `cases/td6_boundary_qb_pencil_20260824/MANIFEST.sha256` and `FREEZE.sha256` (both SHA-256 `6df1eca8846adf23a5e2c45a4450857a6ae99e25ae0a2fd6a2cdc98e6fb9de58`)

All eight freeze-file hashes match the launch prompt. The freeze file body is exactly the seven producer payloads above; `MANIFEST.sha256` is the same byte string. `shasum -a 256 -c cases/td6_boundary_qb_pencil_20260824/FREEZE.sha256` from the repository root reports all seven files `OK`. The committed basis is exactly `c327bdc8d02472feba42573760325099f34b8cdf`. No producer, case, canonical, ladder, notes, or erratum file was edited. No AWS work was launched. All scratch work lived in `/tmp/td6_qb_pencil_review_20260824/`.

Frozen adjoint and parent payloads, working-tree hashes on disk at review time:

- adjoint producer `xmodel/td6-jet-orbit-adjoint-gate-20260824.md` SHA-256 `28a8869cf91f5e7d1e3601c52ee21742eca9187e57d7ac1065f22bcbd0ee402b`
- adjoint hostile review `xmodel/td6-jet-orbit-adjoint-review-grok-20260824.md` SHA-256 `2cd542615dfcc7b15dab3796adba0c91b84dcba606da6ff442b3d69dd4fb79f9` (overall **CONFIRMED**)
- exact dual replay `cases/td6_jet_orbit_adjoint_20260824/replay.py` SHA-256 `fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198`
- orbit audit `cases/td6_jet_orbit_adjoint_20260824/orbit_audit.py` SHA-256 `90bd44ebd6ed810e6d686d44bd84f2f852d623b22a371f137e215436394b967b`
- parent q2 point-probe report SHA-256 `f098dea46ca99ed26bb0ad541efe2135c78c3c1f47da8d92096a91dfece4fcc0`
- completed q2 hostile review SHA-256 `6df0d9c9dde4c4e8991b73da1c807ce40b4f44c2b587949c2312aaebf469665c` (overall **CONFIRMED**)
- imported uniform-third report SHA-256 `0d3e2dc8e57b03060582d6906212ae707cb1d42b10416cff85117daa93b4ed7b`
- uniform-third hostile review SHA-256 `582933fca15c8e1005460591f795102d43c60a9733b8bc19f0b7bdbd716784ef` (overall **CONFIRMED**; all eight subclaims **CONFIRMED**)
- imported q2 compiler SHA-256 `0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357`
- imported next-row replay SHA-256 `0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8`
- imported first-band replay SHA-256 `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735`
- imported moduli-uniformity replay SHA-256 `55340fa662a20e1777eaa18fae2d26589c11ec7f3f2960f4a0a6efe015e7b6ab`
- first-band hostile review SHA-256 `265c1103391e2bae889c018bb0637fe486e7292644c0295e4f9965e5085e7a25` (overall **CONFIRMED**)
- next-row hostile review SHA-256 `12834c356c2c26243522b2609753370118ecd2c8ed87907033ca27e926d2ac2f` (overall **CONFIRMED**)
- moduli-uniformity hostile review SHA-256 `d95e0d684464c2f56b76ceb5cf32158d47ed907565216ff2974ca1d5f883730b` (overall **CONFIRMED**)
- paired-third-band hostile review SHA-256 `3f2462b2c61d01a39769cc82cf3e9a04732e2bc824edea92bcb0eb9c449d3ad7` (overall **CONFIRMED**)

The pencil cache library pins the adjoint dual replay at `fb138b0f59…` before import; that dual replay pins the q2 compiler at `0ba18447…` and the uniform-third replay at `7a21f949…`. No imported-hash mismatch.

Cited canonical SP-2 / F1 / r9-M2 material, working-tree hashes on disk at review time:

- `ladder/SHEET6.md` SHA-256 `5ea8003685a8be0c2554f6966987cbd492583bf9c07603ccb984da48b3ac04f2`
- `ladder/SHEET6-LROOT.md` SHA-256 `9ff5d00567d7b6752ecc79892bb41959a450ddff3837bdb26179899ad2dfad5a` (SP-2 ledger 187–200)

`SHEET6.md` / `SHEET6-LROOT.md` differ from earlier first-band freeze hashes by campaign-status notes. The combinatorial SP-2/IIa/r9-M2 typing used below is the same ledger text at 187–200.

**Promotion.** Accept as `TD6-QB-LICENSED-FAMILY-EMPTY / PIVOT-EXCEPTIONAL-PRODUCT-ONE / EXACT-E[B]-BEZOUT / NOT-SP2 / NOT-JC2 / STOP` of this one licensed one-parameter q2 boundary pencil in the fixed normalized section. Bank the field presentation, the orbit/gauge ranks, the portable cache as a reconstruction of the raw 3,602-column transport response, the staged ranks `3470/3602 → 38/132 → 38/94 → 25/56`, all 101 B-independent unit pivots, the ten compatibility numerators and left-null digests, `N_4` and `N_{13}` as displayed, `k^{-1}`, the Bezout identity, and `gcd=1`. Promote nothing else.

**Quarantine.** Common centering, r9 dead stretch, other q-jets, other p-partitions, other F1 patterns, SP-2, every td=6 terminal class, and JC2 remain open. Exact `J=1` is not proved or disproved. No inference from this pencil to a matrix-changing family is licensed.

---

## Headline and subclaim table

Write `s=y^{-1}`, `x=s+s^2+s^3+t s^4`, F1 chart `x=q^{-5}`, `y=η q`, pole chart `x=r^{-25}`, `y=r^5+ζ r^{17}`, and on the imported sextic field `D=(2S^2-2S+3)/5`, `L=25(1-S+D)`, `A^3=9/L^8`.

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Degree-18 field `E=Q[S,A]/(F(S),A^3-9/L^8)` with the frozen sextic `F`, rectangles `(15,60)/(25,100)`, three charts, pole scale, F1 pattern `R(z)=(z-1)^2(z^2-Sz+D)`, center `(1,1,1)`, zero dead stretch, and `p=t^{15}`, `q_B=t+B t^2+t^{25}`. q2-only is transverse only after the registered chart/source quotient; centering and dead stretch remain frozen licensed moduli. No registered source or target gauge absorbs `B` | **CONFIRMED** | `F` reducible or `A^3-α` reducible over `K`; rank `7→7` after adjoining q2; a registered gauge with a `q_2` slot; producer silently placing `dc1,dc2,dc3` or `d6,…,d16` in the gauge subspace |
| 2 | Independent reconstruction of every cached x-band and pole section from the raw 3,602-column transport matrix matches the canonical JSON coefficientwise and byte-for-byte. Every first, previous/pole, and current input uses only cached bands. Byte equality is provenance, not the mathematical engine | **CONFIRMED** | a reconstructed section differing from the JSON; a compiled Jacobian/pole row depending on an uncached exponent or degree; using `load_cache` as the sole solver |
| 3 | A second untruncated solver over `E[B]`, with its own two-form compilers and GE, reproduces ranks `3470/3602 → 38/132 → 38/94 → 25/56`. All 101 normalized leads are nonzero B-independent units in `E`. Every residual homogeneous row is the zero polynomial | **CONFIRMED** | any stated rank different; a lead of positive B-degree; a lead with vanishing constant term; a leftover homogeneous polynomial row; a hidden B-only pivot |
| 4 | Both affine parameterizations satisfy every original first and previous/pole equation coefficientwise. Independent left-nulls against the original current rows give the displayed `N_4` and `N_{13}`, with supports four and one. Continuing past the first affine failure is the correct extraction of the compatibility ideal | **CONFIRMED** | affine replay failure on an original row; `N_4` or `N_{13}` different; left-null support or residual mismatch against the unreduced current matrix; producer treating later compatibilities as optional after `t^4` |
| 5 | `k=252-342S+144S^2-36S^3` and `ρ` are units in the field `E`. The displayed inverse of `k`, the exact Bezout identity, and `gcd(N_4,N_{13})=1` hold over `E[B]` and after arbitrary field extension of `E`. `B=0`, every quartic root of `N_4`, all 18 embeddings, and every pivot locus are empty. This is not a sampled-point argument | **CONFIRMED** | `k ρ=0` in `E`; displayed inverse failing; Bezout failing; a common root of `N_4` and `N_{13}` in some extension; `F` or `A^3-α` reducible; a B-dependent pivot factor |
| 6 | The coefficient of `B` in `N_4` is the reviewed varying-syzygy derivative `-4720/29`, and `N_4(1)-N_4(0)=-14012/145`. Neither equality is used as interpolation. The untruncated polynomial solve supersedes the adjoint and two-point gates | **CONFIRMED** | linear coefficient other than `-4720/29`; secant other than `-14012/145`; producer reconstructing `N_4` by Hermite interpolation from those two numbers |
| 7 | The exact conclusion is emptiness of this one licensed q2 pencil in the fixed normalized section. No inference to centering, dead stretch, other jets, SP-2, a terminal class, or JC2 is licensed. The smallest honest successor is the first matrix-changing common-centering pencil, then first-entering dead-stretch blocks | **CONFIRMED** | producer promoting an SP-2, class, or JC2 kill, or treating centering/dead stretch as already quotiented |

All remarks below are non-blocking unless marked otherwise. None changes a rank, a polynomial, a hash, or a verdict.

---

## Replay

Registered commands, rerun unmodified from the charged tree:

```sh
python3 cases/td6_boundary_qb_pencil_20260824/build_transport_cache.py
python3 cases/td6_boundary_qb_pencil_20260824/replay.py
```

Exit codes 0. Wall-clock `real 167.67` and `real 54.26`. The cache rebuild printed, character-for-character against the frozen stdout,

```text
TD6-QB-TRANSPORT-CACHE: PASS
transport_rank = 3470/3602
transport_dimension = 132
cache_bytes = 524175
cache.sha256 = 3855b1d8aa98d3602bbba3630512600b4af66eba81103fea1bc8be286fabebb4
```

The `E[B]` replay printed `first symbolic PASS`, `previous/pole symbolic PASS`, and the canonical JSON object with verdict `EXACT-E[B]-STAGED-REPLAY-PASS`. Canonical stdout SHA-256 values, including final newlines, match the freeze (`cd8e8e07…` / `9326e843…`). Arithmetic is `fractions.Fraction` on the residue field `E`. No CAS, no floating point, no modular sampling of the Jacobian system, no AWS.

The first command is a provenance regression: it rebuilds the frozen transport echelon/response and demands byte equality with the checked-in JSON. It is not independent evidence of the compatibility polynomials.

A second engine, written for this review and not imported from the pencil replay, `transport_cache.py`, or the producer’s `Poly`/`solve`/`expected_t4`, then:

1. rebuilt the 3,602-column transport matrix from the hash-pinned first-band compiler and propagated an independent affine-in-`B` particular response;
2. extracted x-band exponents `1,2,3` and pole jets `[r^{-2}]f`, `[r^{-4}]g` by the chart formulae, not by `load_cache`;
3. compiled `[s^{-2}]J`, `[s^{-1}]J`, `[s^0]J-1`, and `[r^1](J-1)` from the two-form identities, tracking quadratic monomials and asserting they cancel;
4. ran its own dense `E[B]` GE on the B=0 rank stratum, requiring every accepted lead to be a degree-zero unit and every leftover homogeneous row to be the zero polynomial;
5. substituted both affine parameterizations back into the original first and previous/pole equations;
6. multiplied every current left-null certificate into the unreduced current matrix.

Wall-clock `real 509.36`. Every stated rank, all ten compatibility numerators and left-null digests, both displayed polynomials, `k^{-1}`, the Bezout digest, and `gcd=1` matched. The reconstructed cache was byte-identical to the canonical JSON; that equality was recorded as provenance and was not used as the elimination engine.

---

## 1. Field and source scope

SP-2 from `SHEET6-LROOT.md:187–200`: chain

```text
F0 = (3,6,5,2,8) → F1 = (15,60,5,4,4)  (μ=2 IIa k=2, n=12) → (0,y),
```

type `(3,5)`, rectangles `(15,60)/(25,100)`, reduced F1 pattern `(η^5-c^5)^2 Π_2`, one x-cluster. With the chain orbit normalized to `C=1` this is `R(z)=(z-1)^2(z^2-Sz+D)`. The r9/M2 pole shape is the AF3 §4 family transported by `L=25(1-S+D)` and normalized by `L^8 A^3=9`. Zero dead stretch and common centering `(1,1,1)` are the same licensed specializations already confirmed by the first-band through adjoint reviews.

Independent field presentation. `F=24S^6-252S^5+1170S^4-3045S^3+4680S^2-4032S+1411` satisfies `F=0` in `K` by construction. `gcd(F,F')=1` over `Q`, so `F` is squarefree. Rabin’s criterion modulo 31 (prime divisors of six are 2 and 3) gives `gcd(F, x^{31^2}-x)=1`, `gcd(F, x^{31^3}-x)=1`, and `x^{31^6}≡x`, so `F` is irreducible over `F_{31}` and therefore over `Q`. Thus `K=Q[S]/(F)` is a degree-6 field.

The source relations `Q=-2S^2+2S+5D-3=0`, `D=(2S^2-2S+3)/5`, `H=1-S+D=(2S^2-7S+8)/5`, `3H^3=1`, `L=25H`, and `α=9/L^8` hold identically in `K`. The multiplication-by-`α` determinant on the `Q`-basis `1,S,…,S^5` is

```text
N_{K/Q}(α) = 3^{28}/5^{96}.
```

The 3-adic valuation 28 is not divisible by 3, so `α` is not a cube in `K`, so `T^3-α` is irreducible over `K`. Hence `E=K[A]/(A^3-α)` is a degree-18 field with `K`-basis `1,A,A^2`, and `L^8 A^3=9`. There are no zero-divisors to hide a vanishing residue at one conjugate.

q2-only versus the full t2 orbit, independently of the registered orbit audit. For `t↦t+ε h(t)` one has `δp=15 t^{14} h`, `δq=(1+25 t^{24}) h`, and chart component `δT=h`. Taking `h=t^2` gives

```text
(δT, δp, δq) = (t^2, 15 t^{16}, t^2+25 t^{26}),
```

not the q2-only vector. Least-index reduction of the seven truncated orbit vectors `h=1,…,t^6` has rank seven; adjoining `{("q",2):1}` raises the rank to eight. Every nonzero reparametrization carries a chart component equal to `h` itself, so no linear combination of the seven can cancel the chart slot and leave a q2-only vector. After the section `p=t^{15}`, `q(0)=0`, `q'(0)=1`, the remaining order-two q-slot is exactly `q_2`.

Target gauges, as identities of `J=f_x g_y-f_y g_x`: translation of `f` or `g` kills every derivative; reciprocal scaling gives `J((1+ε)f,(1-ε)g)=(1-ε^2)J` so the first-order term vanishes; lower shear `g↦g+ε f` leaves `J` identically. Their four boundary vectors have rank four. Rank of the seven orbit vectors plus these four is eleven; adjoining q2-only raises it to twelve. None of the four target vectors carries a `q_2` slot.

F1/pole source tangent over `E`, from the frozen equations, has rank `4/4`. The first two rows have determinant `9 H^2 (7-4S)`. The identity `3H^3=1` forces `H≠0`, and

```text
F(7/4) = -53875/512 ≠ 0
```

in `Q`, so `7-4S≠0` in `K`. There is no source-compatible tangent in `(S,D,L,A)` alone.

Centering `(c1,c2,c3)=(1,1,1)` is the registered chart expansion of `x=c1 s+c2 s^2+c3 s^3+t s^4`. The eleven r9 dead-stretch slots are the omitted coefficients of the pole patterns at `r^6,…,r^{16}`; the frozen patterns occupy only degrees `1,6` on `f` and `0,5,10` on `g`. No source automorphism is exhibited that would normalize those data while keeping all three charts and both rectangles. They are licensed frozen moduli, not gauges of this pencil, and they change the transport matrix itself.

A power series whose first nonzero term is `ρ t^4` is invariant in degree four under `t↦t+ε t^2`. That is the correct negative control for a coordinate rename. It does not absorb the q2-only class.

Claim 1 stands.

---

## 2. Portable transport provenance

Homogeneous transport is independent of `B`. The only B-dependence in the 3,602-column system is the affine g-boundary slot `[t^2]g_0=B`. An independent affine-in-`B` propagator, not the producer `Dual` class, was applied to the frozen rational factorization of the raw matrix. The resulting 132-dimensional particular-plus-directions family was then restricted to the jets that the later bands actually consume:

| section | length | geometric source |
|---|---:|---|
| `f1,f2,f3` | 16 each | `[s^{1,2,3}]` of the x-chart expansion of `f`, degrees `0..15` |
| `g1,g2,g3` | 26 each | the same for `g`, degrees `0..25` |
| `pole_f1` | 61 | pole-chart coefficient of exponent `-2`, ζ-degrees `0..60` |
| `pole_g1` | 101 | pole-chart coefficient of exponent `-4`, ζ-degrees `0..100` |

Pole coefficients were rebuilt from the chart identity `-25 i + 5 j + 12 ζ = exponent` with binomial weights `C(j,ζ)`, not by importing `nr.pole_coefficient` as an oracle. The first band uses only `(f1,g1)`; previous uses `(f1,f2,g1,g2)`; current uses `(f1,f2,f3,g1,g2,g3)`; the inherited pole row uses `(pole_f1,pole_g1)` together with the parameter-free pole jets `p,q` built from `(L,A)`. No compiled row asks for exponent 4, a higher pole jet, or a degree outside those ranges. The cache is complete for this staged system.

Coefficientwise comparison with the canonical JSON succeeded on every base, linear, and direction entry. Re-serializing with the same canonical JSON recipe produced the same 524,175 bytes and the same SHA-256 `3855b1d8aa98d3602bbba3630512600b4af66eba81103fea1bc8be286fabebb4`. That byte equality is a provenance check on the portable cache. The independent elimination below consumed the reconstructed affine forms, not `transport_cache.load_cache`.

Transport rank is `3470/3602` with 132 free parameters, `nf=976=16·61`, `ng=2626=26·101`. There is no transport compatibility: the particular response exists over `E[B]` and is genuinely affine.

Claim 2 stands.

---

## 3. Exact polynomial elimination

Chart two-form, re-derived here: `y=s^{-1}`, `x=s+s^2+s^3+t s^4` gives `dx∧dy=s^2 ds∧dt`. Writing `F=p+s f1+s^2 f2+s^3 f3+…` and `G=q_B+s g1+s^2 g2+s^3 g3+…` with `q_B'=1+2B t+25 t^{24}` and `p'=15 t^{14}`, the identity `J s^2 = F_s G_t-F_t G_s` forces

```text
[s^0]:  f1 q' - 15 t^{14} g1 = 0,
[s^1]:  f1 g1' - f1' g1 + 2 f2 q' - 30 t^{14} g2 = 0,
[s^2]:  f1 g2' + 2 f2 g1' + 3 f3 q' - 45 t^{14} g3 - 2 f1' g2 - f2' g1 = 1.
```

The pole chart determinant is `-25 r^{-9}`. The local-wedge coefficient of `r^{-8}` is `-3 p q1' - 2 p1 q' + 4 p' q1 + 5 p1' q`; dividing by `-25` produces `[r^1](J-1)`. These four identities were compiled directly. Products of affine forms were expanded through quadratic monomials; every quadratic coefficient cancelled identically, so the packed rows remained linear in the parameters. That cancellation is a structural fact of these bands on the transported family, not an assumption imported from the producer `pack` assertion.

Independent dense `Poly` arithmetic over `E`, with the B=0 rank-stratum pivot rule (least index among variables whose constant term is a unit), produced:

| stage | independent result |
|---|---|
| transport only | rank `3470/3602`, dimension `132`; directions B-degree `0`, particular B-degree `≤1` |
| first centered Jacobian | rank `38/132`, dimension `94`; every lead B-degree `0` |
| previous centered + inherited pole | rank `38/94`, dimension `56`; every lead B-degree `0` |
| current homogeneous | rank `25/56`; every lead B-degree `0` |
| current affine | ten polynomial incompatibilities at input rows `t^4,…,t^{13}` |

All `38+38+25=101` normalized leads are elements of `E`, independent of `B`. Each was inverted in `E` and the product with its inverse is `1`. Two leads are not rational constants: the pole pivot `P1` at ζ-degree 3 is a nonzero element of the `A^2` slot, and the current pivot `X0` at `t^3` is a nonzero cubic-truncated element of `K`. Both are units because `E` is a field and the elements are nonzero. The pivot exceptional polynomial is therefore `1`: there is no B-dependent denominator or rank-jump stratum to specialize.

After reduction, every dependent homogeneous row is the zero polynomial row, not merely zero at `B=0`. A hidden B-only pivot cannot have been discarded. B-linear entries that vanish at `B=0` and were never chosen as leads remain source terms. At `B≠0` they can only add constraints. A rank drop, which would be the only way to create a solution, requires a lead to vanish; none do. The B=0 schedule is therefore a global emptiness schedule, not a generic-rank guess.

Degree bounds independently observed: every cached constant is B-degree `≤1` with directions of degree `0`; every first, previous/pole, and current matrix entry and RHS is B-degree `≤1`; both reduced parameterizations have constant B-degree `≤1` and direction B-degree `0`. These are structural, because every accepted lead was inverted only after a degree-zero test.

Claim 3 stands.

---

## 4. Affine rebuild and compatibilities

The 94-parameter and 56-parameter affine forms were substituted into every original first and previous/pole equation. The identity held coefficientwise in all free parameters and in `B`. That is a check against the unreduced compiled rows, not against a reduced output.

At the current band, elimination was continued past the first affine contradiction at `t^4`. That is algebraically legitimate for the compatibility ideal: an affine solution would have to annihilate every left-null residual, not just the first. Stopping at `N_4` would leave a quartic of candidate roots; the later rows are needed to kill those roots. The homogeneous rank `25/56` remains well-defined on the same B=0 unit-pivot schedule.

Ten exact left-null certificates occur at `t^4,…,t^{13}`. Each was multiplied into the original current rows, not into reduced output, and reproduced its residual with vanishing variable side. Independently computed numerator digests:

| row | degree | numerator SHA-256 | support | weight degree | left-null SHA-256 |
|---|---:|---|---:|---:|---|
| `t4` | 4 | `dd5c7e694153beebb9ae0f08408c7b2e8a209b9671a76ad20ba66cb601b8d1ad` | 4 | 3 | `3f6bf56c0ae16e05f04395fb3f3a5a340e5af3d170324a636ad0665373ebe149` |
| `t5` | 4 | `62b5c40223c0b422a987d5074e842e23b7f9bb32a94088e0d21cfecc65c560ac` | 4 | 3 | `46d40aebc9240cf19f2170f6137fd8955f718dc06b8a0c2559b23072fbd788cd` |
| `t6` | 4 | `f25765d7afaed5d81ec7bb222207a6756fa54364cc56152b6786c5b29db557a9` | 4 | 3 | `d22ed3e43fe65ecbdaf4c5e270bf0f0cfbbff2f4ad8b68df424815460a316f4d` |
| `t7` | 4 | `105cb1ff3db5d6e36e9a094ff745c481b05a57b541ee12929c2a4b3dc493f062` | 4 | 3 | `896a851bec04548fb5be3849ed80925a67ee224160c6f7a63fb199d94cf6454a` |
| `t8` | 4 | `e3a7083f0df52cecdd8e1ff51b61de85e262a2b53cfd110f5215dbe0f201f402` | 4 | 3 | `5200d802a7bcbed53f4560cb600f2a9cd93f11305c6df4b91dcebcce6eb46b62` |
| `t9` | 4 | `936ee036c2396784e7d24bbc2a50b9540c91c6e14f24d6831c923b51ab5387cd` | 4 | 3 | `c8627425bbaf91c5c83a9e71887b42a296a1fa39f7ce8ea844aad9ea856a2d94` |
| `t10` | 4 | `314b6a7a8f81e1ac28270ab04afabe8d1beb89dca3fb3d07d1bb4248f02d2e15` | 4 | 3 | `4685d453befee3fb06a7a8e327dd380cff07b812c2097e81857d69b4c107f3ce` |
| `t11` | 4 | `10b3cf44d8794f83dbd2da9efb497bf656a9c1a358f7d34e1dbe8f80b9d9c5b0` | 4 | 3 | `cb8b6a969b855f24aaa7995d073ca5c17a7c9de6d9c83dccdae7a9c5abfa9144` |
| `t12` | 4 | `39ea7593593901fd25eb6902bc858fef0d09f835858cff062c05aae0348a4c59` | 4 | 3 | `44a2586b2e7db7d1afb587aa2289172ccce1b80e00dbad4e9a088719338bf381` |
| `t13` | 1 | `49760d07f6b8527c6eee74a8f825413fb5fd83bfb832427602906a37cace6ea3` | 1 | 0 | `e11690963661a8c978cdc4ef8741d4a242c5a7038a2e2402701209a911f8ffc3` |

Two suffice. Against the original current rows, not reduced output,

```text
N_4(B) = ρ - (4720/29) B + (11364/145) B^2 - (4096/145) B^3 + 16 B^4,
N_{13}(B) = ((252 - 342 S + 144 S^2 - 36 S^3)/25) B,
```

with

```text
ρ = (2495634 - 4154976 S + 4405068 S^2 - 2488119 S^3 + 761922 S^4 - 105084 S^5)/3625
    + (136875/29) A.
```

`N_4` has support four and weight degree at most three. `N_{13}` is itself a parameter-free compatibility (support one, constant weight). The `t^{13}` row does not need a combination of earlier rows: it is already a relation among no free variables.

Claim 4 stands.

---

## 5. Units, gcd, and exceptional roots

Write `k=252-342S+144S^2-36S^3`. Extended Euclidean algorithm of `k` against the monic `F` produces the inverse

```text
k^{-1} = - (388/175625) S^5 + (738/35125) S^4
         - (9181/105375) S^3 + (40993/210750) S^2
         - (4948/21075) S + (66812/526875),
```

and the product is exactly `1` in `K`. This is `gcd(F,k)=1`, not a sample at one embedding of `S`. The coefficient of `B` in `N_{13}` is `k/25`; its inverse is `25 k^{-1}`, digest `fd2476104889d51b5ddbc8adbfeb45764bf89fb9c13210319fdbf1ef33959d63`, and the product is `1` in `E`.

`ρ` has a nonzero `A`-component `(136875/29)` in the `K`-basis `1,A,A^2`, so `ρ≠0` in `E`. Direct inversion gives `ρ·ρ^{-1}=1`. Nonzero in a field is the unit condition at all 18 pole-normalized conjugate embeddings; it is not a numerical sample of one sextic root.

Let `N_4=ρ+B h` with `h=-(4720/29)+(11364/145)B-(4096/145)B^2+16 B^3` and `N_{13}=(k/25)B`. Then

```text
(1/ρ) N_4 - (25 h)/(ρ k) N_{13} = 1
```

holds as a polynomial identity over `E[B]`. Independently, the Euclidean algorithm on the ten compatibility numerators returns the monic gcd `1`, digest `832a8a790c1b7572ef7f3796644b3a6cb4c68225283f6e671494e23692ba68ef`. The Bezout identity digest is `159c3b52a498e3f762545750bdfbf7e53675172264f51fe92ce70668bc46104d`.

After an arbitrary field extension `F⊃E`, `ρ` and `k` remain nonzero, hence units of `F`. Then `N_{13}` is a unit times `B`, and `gcd(N_4,B)=gcd(ρ,B)=1` because `ρ` is a nonzero constant. Therefore `gcd(N_4,N_{13})=1` in `F[B]`. No quartic root of `N_4` in any extension can satisfy `N_{13}=0`: such a root would force `B=0`, but `N_4(0)=ρ≠0`. Conversely `B=0` kills `N_{13}` and leaves `N_4=ρ≠0`.

There is consequently no unresolved stratum:

- transport rank is constant in `B`;
- all 101 downstream pivot factors are units independent of `B`;
- the pivot exceptional product is `1`;
- the compatibility ideal is the unit ideal;
- `F` and `A^3-α` are irreducible, so the residue ring is a field and no zero-divisor can hide a conjugate-specific vanishing.

Claim 5 stands.

---

## 6. Adjoint and two-point controls

The coefficient of `B` in the independently computed `N_4` is the rational `-4720/29`, with vanishing `S` and `A` slots. That is the frozen dual-adjoint derivative `c'(0)` of the completed jet-orbit review, including `λ'`. Evaluating the same polynomial at the two points of the parent q2 probe gives

```text
N_4(1) - N_4(0) = -4720/29 + 11364/145 - 4096/145 + 16 = -14012/145.
```

Clearing denominators, `-4720/29=-23600/145 ≠ -14012/145`. The difference `-9588/145` is the genuine content of the higher coefficients; it is why two-point interpolation was never a family polynomial. The present untruncated left-null solve is not a Hermite fit to `(ρ, c'(0), c(1))`. Those two numbers are evaluations of a polynomial that was obtained by fraction-free elimination with printed degree bounds (every matrix entry of B-degree `≤1`, every reduced constant of B-degree `≤1`, `N_4` of degree 4, `N_{13}` of degree 1). The polynomial supersedes the adjoint and the two-point gates; it does not import them as interpolation data.

The producer hard-codes `expected_t4` only as an assertion after computing the residual. The independent engine computed the residual first from its own compilers and then compared. The match is a consistency check, not a circular import of the adjoint Dual GE.

Claim 6 stands.

---

## 7. Logical scope and successor

What is proved, and only what is proved:

- in the registered section, with frozen centering and zero dead stretch, the one-parameter family `q_B=t+B t^2+t^{25}` at `p=t^{15}` has no solution over `E`, nor over any field extension of `E`;
- the obstruction is the unit ideal of `E[B]`, not a proper exceptional locus;
- `q_2` remains a genuine transverse class of the smallest registered boundary-jet quotient, now with an empty compatibility scheme.

Printed producer scope `NOT-SP2 / NOT-JC2` matches that. The flags of the adjoint parent `q2_family_killed=false` are now correctly strengthened to a family kill of this one pencil, and only this pencil.

What is not proved, and is not licensed by `gcd(N_4,N_{13})=1`:

- emptiness of the three common centering coefficients, or of any first-entering dead-stretch block;
- other q-jets, a different p-partition, a different F1 shape, or a different pole normalization;
- SP-2, any of the eight td=6 terminal classes, landing, mapping degree, or JC2;
- exact `J=1`.

Those omitted families change the transport matrix itself. They are not absorbed by the registered chart/source/target quotient, and they were frozen rather than quantified. The smallest honest successor is therefore the first matrix-changing common-centering pencil, then dead-stretch coefficients in first-entering-order blocks, always quotienting the full source reparametrization and the four target gauges. The same nonblocking pattern applies: a provisional exact pencil can feed a successor while adversarial review runs in the background.

Claim 7 stands.

---

## Parameter, staging, and field caveats (non-blocking)

1. `F` and `E` are imported from the frozen uniform-third gate, independently re-certified here by Rabin, `gcd(F,F')`, and the norm of `α`. They are not re-derived as the constant-row polynomial of the `B`-family. The current band being consistent through `t^0` on that field is compatible with `[s^0 t^0]J-1` still vanishing, because `q_B'(0)=1` for every `B`.
2. The B=0 pivot schedule is licensed by the proof that every accepted lead is a B-independent unit and every leftover homogeneous row is the zero polynomial. It is not a claim that the same index set of free variables would be chosen by a different monomial order.
3. Homogeneous transport rank `3470` is B-independent. First-Jacobian rank `38` is constant in `B` because its 38 leads are units in `E`.
4. Quadratic monomials in `f1 g1'` and similar products cancel on this transported family. The independent compiler kept those terms and asserted they vanished; it did not inherit the producer `len(monomial)==1` assertion as an axiom.
5. Target-gauge Jacobian identities are identities of `J`, not four extra 3,602-variable `E[B]` pencils.
6. Byte equality of the reconstructed cache with the canonical JSON is a provenance check. The compatibility polynomials were computed from independently compiled two-forms on those reconstructed sections.

---

## Hashes

| artifact | SHA-256 |
|---|---|
| producer report | `5e1f6b44e143360a41550ae552b20bef02325414f96c5fd469ba4d016eb5eb22` |
| exact `E[B]` replay | `fab27e808ce0f840e82359d01f83834c874c168f6414f550e253d94aac42360c` |
| canonical replay stdout | `9326e8430ce76afb4c57d868fa0659a690c5c3a0cd3b6a7225c5095fefac7f48` |
| canonical transport cache | `3855b1d8aa98d3602bbba3630512600b4af66eba81103fea1bc8be286fabebb4` |
| raw-cache verifier | `78d06b9f64c80bd1fd328e5960b4512fe6a9c574ef53c47d63a58d56b9326328` |
| raw-cache verifier stdout | `cd8e8e070d055ebaa339f34ae524d0e163b29c2b929c5d546448068ae036e032` |
| transport field/cache library | `11521a7e25d85c7f8bb6ab5173c6489d08a13edf705e6e742c10211e6e152724` |
| manifest / freeze | `6df1eca8846adf23a5e2c45a4450857a6ae99e25ae0a2fd6a2cdc98e6fb9de58` |
| `N_4` numerator | `dd5c7e694153beebb9ae0f08408c7b2e8a209b9671a76ad20ba66cb601b8d1ad` |
| `N_4` left-null | `3f6bf56c0ae16e05f04395fb3f3a5a340e5af3d170324a636ad0665373ebe149` |
| `N_{13}` numerator | `49760d07f6b8527c6eee74a8f825413fb5fd83bfb832427602906a37cace6ea3` |
| `N_{13}` left-null | `e11690963661a8c978cdc4ef8741d4a242c5a7038a2e2402701209a911f8ffc3` |
| monic compatibility gcd | `832a8a790c1b7572ef7f3796644b3a6cb4c68225283f6e671494e23692ba68ef` |
| Bezout identity | `159c3b52a498e3f762545750bdfbf7e53675172264f51fe92ce70668bc46104d` |
| `k/25` inverse | `fd2476104889d51b5ddbc8adbfeb45764bf89fb9c13210319fdbf1ef33959d63` |
| adjoint producer | `28a8869cf91f5e7d1e3601c52ee21742eca9187e57d7ac1065f22bcbd0ee402b` |
| adjoint hostile review | `2cd542615dfcc7b15dab3796adba0c91b84dcba606da6ff442b3d69dd4fb79f9` |
| imported q2 compiler | `0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357` |
| imported uniform-third replay | `7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8` |
| parent q2 point-probe report | `f098dea46ca99ed26bb0ad541efe2135c78c3c1f47da8d92096a91dfece4fcc0` |
| completed q2 hostile review | `6df0d9c9dde4c4e8991b73da1c807ce40b4f44c2b587949c2312aaebf469665c` |
| imported uniform-third report | `0d3e2dc8e57b03060582d6906212ae707cb1d42b10416cff85117daa93b4ed7b` |
| uniform-third hostile review | `582933fca15c8e1005460591f795102d43c60a9733b8bc19f0b7bdbd716784ef` |

**JC2 scope.** This is an exact emptiness certificate for one licensed one-parameter q-boundary pencil inside one normalized SP-2 chart-pattern control with frozen centering and zero dead stretch. It neither realizes nor kills a terminal class, supplies no Keller pair, does not quantify centering or dead-stretch moduli, and neither proves nor disproves the plane Jacobian conjecture.
