# Hostile different-model review — TD6 smallest q-boundary deformation

| Field | Value |
|---|---|
| Claim under review | Frozen TD6-BOUNDARY-Q2-DEFORMATION: at the smallest bounded widening `p=t^{15}`, `q_B=t+B t^2+t^{25}` of the frozen x-boundary, the two exact values `B=1` and `B_*=ρ_0/(14012/145)` in the degree-18 field `E` are empty at the new centered band `[s^0 t^4]J`, and that degree-four residue is genuinely `B`-sensitive |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Hidden local-to-global step | none: emptiness of two exact points of one smallest q-jet deformation, inside one already-cut normalized SP-2 chart-pattern control, is not a kill of the one-parameter `B` family, of other q-jets, of centering/dead-stretch/F1 moduli, of SP-2, of a td=6 terminal class, or of JC2 |
| Evidence tier | independent exact algebra over `Q` and `E=K[A]/(A^3-α)` (registered `B=1` and adaptive replays; a second engine that does not import either probe: own two-form compilers for `[s^{-2}]J`, `[s^{-1}]J`, `[s^0]J-1`, and `[r^1](J-1)`, insertion-order and reverse-row least-index GE, unreduced left-null multiply, and a direct `B=1` versus `B=0` first-Jacobian matrix difference); primary-source read of the completed first-band, next-row, moduli-uniformity, paired-third-band, and uniform-third-band hostile reviews |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T12:58:15Z – 2026-08-24T13:16:11Z |
| Python | 3.14.6; stdlib `fractions.Fraction` / `hashlib` only |
| Host | Darwin arm64 |

Producer inputs reread in full before any verdict:

- `xmodel/td6-boundary-q2-deformation-gate-20260824.md` (SHA-256 `f098dea46ca99ed26bb0ad541efe2135c78c3c1f47da8d92096a91dfece4fcc0`)
- `cases/td6_boundary_q2_deformation_20260824/replay.py` (SHA-256 `0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357`)
- `cases/td6_boundary_q2_deformation_20260824/sextic_probe.py` (SHA-256 `8834cd9b365a9a20d058c3ef6b0ef927c6aee05c895b650b6bc2b927ed6250ca`)
- `cases/td6_boundary_q2_deformation_20260824/adaptive_probe.py` (SHA-256 `ca09d8dc6d154eec7a0fe39747c6ea348fc5e7cccd26bae7bdadae148cd51be5`)
- `cases/td6_boundary_q2_deformation_20260824/B1.stdout` (SHA-256 `68863a4c0deb4eb0d2745714612bfb8ea7b445dd7355833181cf5178241ef2bd`)
- `cases/td6_boundary_q2_deformation_20260824/ADAPTIVE.stdout` (SHA-256 `b5cf24e87e84900f796affb8c78a63af805bb0c68c0fdab03d0ef99fa318aceb`)
- `cases/td6_boundary_q2_deformation_20260824/FREEZE.sha256` (SHA-256 `1cc169979ee610649f87be1c7069a3517564752e8d3417f764dc09a7d22916a9`)

All seven frozen hashes match the launch prompt. The freeze file body is exactly the six producer payloads above; `MANIFEST.sha256` is the same byte string. `shasum -a 256 -c cases/td6_boundary_q2_deformation_20260824/FREEZE.sha256` from the repository root reports all six files `OK`. The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. No producer, case, canonical, or ladder file was edited. No AWS work was launched.

Frozen parent producers/reviews, reread against that basis:

- `xmodel/td6-two-chart-first-band-20260824.md` SHA-256 `cb373892233bddaf1b8fbf7722335ca43ee366b337151c3b244d2604d8168bf2`
- `cases/td6_two_chart_first_band_20260824/replay.py` SHA-256 `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735`
- `xmodel/td6-two-chart-first-band-review-grok-20260824.md` SHA-256 `265c1103391e2bae889c018bb0637fe486e7292644c0295e4f9965e5085e7a25` (overall **CONFIRMED**; all six subclaims **CONFIRMED**)
- `xmodel/td6-two-chart-next-row-20260824.md` SHA-256 `32124d20ec84ef59d5b116639176b12053f5da6de1a9458dd4a2095d6b1618f0`
- `cases/td6_two_chart_next_row_20260824/replay.py` SHA-256 `0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8`
- `xmodel/td6-two-chart-next-row-review-grok-20260824.md` SHA-256 `12834c356c2c26243522b2609753370118ecd2c8ed87907033ca27e926d2ac2f` (overall **CONFIRMED**; all six subclaims **CONFIRMED**)
- `xmodel/td6-moduli-uniformity-gate-20260824.md` SHA-256 `499e95763759fe195ab1eba5fbf97bfb9d255bbf6fb2b090add938d92f1f3a06`
- `cases/td6_moduli_uniformity_20260824/replay.py` SHA-256 `55340fa662a20e1777eaa18fae2d26589c11ec7f3f2960f4a0a6efe015e7b6ab`
- `xmodel/td6-moduli-uniformity-review-grok-20260824.md` SHA-256 `d95e0d684464c2f56b76ceb5cf32158d47ed907565216ff2974ca1d5f883730b` (overall **CONFIRMED**; all seven subclaims **CONFIRMED**)
- `xmodel/td6-paired-third-band-20260824.md` SHA-256 `a98de6d23ff2942360c328e4eeb6c08e24a122b0f9c964a5ad586cf0b009e9f2`
- `cases/td6_paired_third_band_20260824/replay.py` SHA-256 `5d05a6de17e3959ad221527ab74c7da77ba1e1980e8a7d86d0fd8cdca10d468a`
- `xmodel/td6-paired-third-band-review-grok-20260824.md` SHA-256 `3f2462b2c61d01a39769cc82cf3e9a04732e2bc824edea92bcb0eb9c449d3ad7` (overall **CONFIRMED**; all six subclaims **CONFIRMED**)
- `xmodel/td6-moduli-uniform-third-band-20260824.md` SHA-256 `0d3e2dc8e57b03060582d6906212ae707cb1d42b10416cff85117daa93b4ed7b`
- `cases/td6_moduli_uniform_third_band_20260824/replay.py` SHA-256 `7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8`
- `xmodel/td6-moduli-uniform-third-band-review-grok-20260824.md` SHA-256 `582933fca15c8e1005460591f795102d43c60a9733b8bc19f0b7bdbd716784ef` (overall **CONFIRMED**; all eight subclaims **CONFIRMED**)

The `B=1` probe and the adaptive probe both pin the uniform-third replay at `7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8` before import; the base helper pins the next-row compiler at `0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8`, which itself pins the first-band compiler at `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735`. No imported-hash mismatch.

Cited canonical SP-2 / F1 / r9-M2 material, working-tree hashes on disk at review time:

- `ladder/SHEET6.md` SHA-256 `cac82e6494654ecbfa31d0b769138e0ef2be02e1c06fbe987668a6e894c3a040`
- `ladder/SHEET6-LROOT.md` SHA-256 `07b65b670d2a75a932ae0ce0596b4ffb214185e14c265393587c70269c632575` (SP-2 ledger 187–200)
- `ladder/SHEET6-AF2.md` SHA-256 `c7f7601d5b72e2512561d12d160ac8e7458ee3954a8c18182b41ef6174053b3c`
- `ladder/SHEET6-AF3.md` SHA-256 `555363fde61291a0c689bbf9d789c01f73734e0c403d350d85ae2fd0ddab8099`

`SHEET6.md` / `SHEET6-LROOT.md` differ from the first-band and third-band freeze hashes because of uncommitted campaign-status notes. The combinatorial SP-2/IIa/r9-M2 typing used below is the same ledger text at 187–200.

**Promotion.** Accept as `TWO-EXACT-EMPTY-SPECIALIZATIONS / STOP` of this one smallest q-boundary deformation at the two exact points `B=1` and `B_*`. Bank the deformed first row (5), ranks `3508/3602`, `36/94`, `25/58` at `B=1`, ranks `3470/3602 → 132`, `+38 → 94`, `+38 → 56`, `25/56` at `B_*`, the exact residues `ρ_1` and `ρ_1-ρ_0=-14012/145`, and the adaptive residue’s nonzero `1,A,A^2` support. Promote nothing else.

**Quarantine.** The one-parameter family in `B` is not killed. Other q-jets, common centering, nonzero dead stretch, other F1 patterns, SP-2, every td=6 terminal class, and JC2 remain open. Exact `J=1` is not proved or disproved.

---

## Headline and subclaim table

Write `s=y^{-1}`, `x=s+s^2+s^3+t s^4`, F1 chart `x=q^{-5}`, `y=η q`, pole chart `x=r^{-25}`, `y=r^5+ζ r^{17}`, and on the imported sextic field `D=(2S^2-2S+3)/5`, `L=25(1-S+D)`, `A^3=9/L^8`.

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | `p=t^{15}`, `q_B=t+B t^2+t^{25}` retains degree `(15,25)`, `q_B(0)=0`, `q_B'(0)=1`, and the normalized single x-cluster; this is a bounded compiler control, not a complete SP-2 boundary normal form. Retained center `(1,1,1)`, zero dead stretch, reduced F1 `R(z)=(z-1)^2(z^2-Sz+D)`, r9 relation (2), sextic `F`, and degree-18 field `E` match the frozen parents | **CONFIRMED** | `q_B` of degree other than 25, `q_B(0)≠0`, or `q_B'(0)≠1`; producer treating (1) as a terminal-forced SP-2 normal form; a new rectangle, centering triple, dead-stretch slot, F1 orbit pattern, or pole shape; a different sextic or a numerical embedding of `E` |
| 2 | Independently, `dx∧dy=s^2 ds∧dt` forces the first centered row `f1(1+2Bt+25 t^{24})-15 t^{14} g1=0`. Every later x-boundary formula consumes this same `q_B'`. No `B=0` right-hand side, first-Jacobian echelon, or pole datum is silently reused where it depends on `B` | **CONFIRMED** | two-form `s^1` or `s^3`; `q_B'` missing the `2B t` term in a later x-compiler; `B=1` first-Jacobian matrix agreeing with the parent `B=0` matrix at degree `t^1`; adaptive transport omitting the `[t^2]g_0=B` row; pole jets copied from the numerical first-band `A=1/9` point |
| 3 | Exact `B=1`: ranks `3508/3602`, `36/94`, tangent `25/58`, empty at input row `t^4`, residue `ρ_1` as in (6). Parent `ρ_0` minus `ρ_1` is `-14012/145` in `E`. Nonzero status is the nonzero `A`-component in the `K`-basis `1,A,A^2`, not floating point or one embedding | **CONFIRMED** | reverse-row rank ≠ 3508 or previous rank ≠ 36; affine system consistent at `t^4`; residual ≠ (6); `ρ_1-ρ_0` other than `-14012/145`; `A`-coefficient of `ρ_1` vanishing |
| 4 | `B_*=ρ_0/(14012/145)` is well-defined in `E`, nonzero, and does not drop `deg q`, `q(0)=0`, or `q'(0)=1`. The adaptive program rebuilds transport and every `B`-dependent first/previous/current band, includes the inherited opposite-side pole row, and does not assume affine dependence on `B` | **CONFIRMED** | `14012/145=0` in `E`; `B_*=0`; adaptive reusing a `B=0` parameterization; pole row omitted at `B_*`; a secant formula used in place of the rebuilt linear systems |
| 5 | Adaptive staged ranks `3470/3602 → 132`, `+38 → 94`, `+38 → 56`, tangent `25/56`, affine inconsistency at `t^4`. The residue has genuinely nonzero `1,A,A^2` components in `E`. Reverse-row GE reproduces the ranks and the inconsistency | **CONFIRMED** | transport rank ≠ 3470; first-J rank ≠ 38; previous+pole rank ≠ 38; tangent ≠ 25; a vanishing `E/K` basis slot; reverse-row GE consistent; affine system nonempty |
| 6 | The only licensed conclusion is that `B=1` and the adaptive secant-cancellation point are empty and that the degree-four obstruction is `B`-sensitive. No inference to arbitrary `B`, generic rank, other q-jets, other centering/dead-stretch/F1 data, SP-2, a terminal class, or JC2 is licensed | **CONFIRMED** | producer promoting a family kill, a uniform-in-`B` rank, an SP-2 or class kill, or JC2; printed flags `full_b2_family_killed`, `SP2_killed`, or `JC2_resolved` true |
| 7 | Smallest source-honest next test is symbolic one-parameter elimination in `B`, including every pivot/rank-jump stratum. An adjoint/jet-orbit shortcut that ignores those strata cannot certify the same question. Sample interpolation is not a proof | **CONFIRMED** | a `B`-independent left kernel already in hand that remains nonzero as a polynomial in `B`; producer licensing three-point interpolation as a family kill |

All remarks below are non-blocking unless marked otherwise. None changes a rank, a residue, a hash, or a verdict.

---

## Replay

Registered commands, rerun unmodified from the charged tree:

```sh
python3 cases/td6_boundary_q2_deformation_20260824/sextic_probe.py
python3 cases/td6_boundary_q2_deformation_20260824/adaptive_probe.py
```

Exit codes 0. Wall-clock `real 236.27` and `real 317.36`. Printed verdicts, character-for-character against the frozen stdout files:

```text
TD6-BOUNDARY-Q2-B1: PASS
verdict = B2-EQUALS-ONE-EMPTY
base = rank 3508 / 3602; dimension 94
previous_x = rank 36 / 94; dimension 58
current_centered_band = tangent_rank 25 / 58; EMPTY at t^4
residual.sha256 = d091b65e4bc7c66a83946499ab037ceb3812bcedc4c5311bbda8276bfa213732
full_b2_family_killed = false
```

```text
TD6-BOUNDARY-Q2-ADAPTIVE: PASS
verdict = ADAPTIVE-B2-CANDIDATE-EMPTY
boundary = p=t^15; q=t+B*t^2+t^25
candidate = B=RHO_0/(14012/145) in exact degree-18 source field
transport = rank 3470 / 3602; dimension 132
first_J_band = rank 38 / 132; dimension 94
previous_paired_bands = rank 38 / 94; dimension 56
current_centered_band = tangent_rank 25 / 56; EMPTY at t^4
residual_basis_support = 1,A,A^2 (all nonzero)
candidate_B.sha256 = 64010183890daa1938b4eac6add7933767238738e9783f41b5821dcc4b56d750
residual.sha256 = be22c8d155c26a5091494d68c32e043cce66b4275330a022e493528659a4a53b
full_b2_family_killed = false
SP2_killed = false
JC2_resolved = false
```

Canonical stdout SHA-256 values, including final newlines, match the freeze (`68863a4c…` / `b5cf24e8…`). Arithmetic is `fractions.Fraction` on the residue field `E`. No CAS, no floating point, no modular sampling of the Jacobian system, no AWS.

A second engine, written for this review and not imported from either registered probe, rebuilt the 3602-variable transport from the hash-pinned first-band compiler and then diverged on purpose: (i) first-Jacobian, previous-centered, current-centered, and inherited-pole compilers derived from the two-form `[s^{k+2}](F_s G_t-F_t G_s)` and the pole wedge divided by `-25`, taking `q_B'` as an explicit argument; (ii) insertion-order and reverse-row-order least-index GE of every homogeneous and affine stage; (iii) a direct matrix difference between the `B=1` and parent `B=0` first-Jacobian rows; (iv) an unreduced left-null certificate for each advertised residual; (v) reconstruction of `B_*` and of `ρ_1-ρ_0` in `E` from the frozen parent residual. Every stated rank, the `t^4` inconsistency, both residue serializations, and both `B_*` / `ρ_1` hashes matched. No assertion failed. Wall-clock `real 578.80`.

---

## 1. Source typing

SP-2 from `SHEET6-LROOT.md:187–200`: chain

```text
F0 = (3,6,5,2,8) → F1 = (15,60,5,4,4)  (μ=2 IIa k=2, n=12) → (0,y),
```

type `(3,5)`, rectangles `(15,60)/(25,100)`, reduced F1 pattern `(η^5-c^5)^2 Π_2`, one x-cluster. With the chain orbit normalized to `C=1` this is `R(z)=(z-1)^2(z^2-Sz+D)`. The r9/M2 pole shape is the AF3 §4 family transported by `L=25(1-S+D)` and normalized by `L^8 A^3=9`. Zero dead stretch and common centering `(1,1,1)` are the same licensed specializations already confirmed by the first-band through uniform-third-band reviews.

The deformed x-boundary is the polynomial pair

```text
p(t) = t^{15},     q_B(t) = t + B t^2 + t^{25}.
```

Degree, origin, and derivative are exact, not numerical:

- `deg p = 15` with leading coefficient `1`, so the displayed single x-cluster is retained;
- `deg q_B = 25` with leading coefficient `1`, independently of `B`;
- `q_B(0) = 0`;
- `q_B'(t) = 1 + 2 B t + 25 t^{24}`, hence `q_B'(0) = 1`.

This is the lowest-degree extra term after the jet already forced by `q(0)=0` and `q'(0)=1`. It is **not** a complete SP-2 boundary normal form. A general unsplit degree-15/25 pair with those origin/derivative conditions still has free coefficients `t^2,…,t^{14}` in `p` and `t^3,…,t^{24}` in `q`, plus the option of a different common centering or a nonzero dead stretch. The first-band hostile review already classified `t^{15}/(t+t^{25})` as a selected monomial boundary inside broader degree-15/25 data (`td6-two-chart-first-band-review-grok-20260824.md`, selected-versus-forced table). The producer states the same restriction. No inference from (1) to every licensed x-direction polynomial is licensed.

Retained parent hypotheses, checked against the hash-pinned uniform-third field arithmetic rather than against prose:

| datum | status |
|---|---|
| rectangles `(15,60)/(25,100)` | fixed (inherited combinatorics) |
| center `(c1,c2,c3)=(1,1,1)` | fixed |
| r9 dead stretch | fixed at zero |
| F1 `R(z)=(z-1)^2(z^2-Sz+D)`, `C=1` | fixed shape; `S` lives in `K=Q[S]/(F)` |
| source relation `D=(2S^2-2S+3)/5`, `H=1-S+D`, `L=25H` | fixed; `3H^3=1` in `K` |
| pole normalization `L^8 A^3=9` | fixed; cubic of `E` |
| sextic `F=24S^6-252S^5+1170S^4-3045S^3+4680S^2-4032S+1411` | imported, not re-eliminated |
| `E=K[A]/(A^3-α)` of degree 18, basis `1,A,A^2` | imported from the frozen uniform-third irreducibility proof |

`F` and `E` are retained hypotheses: the calculation asks whether the already-cut 18 pole-normalized conjugates survive this q-jet. It does not re-prove that `F` is the constant-row polynomial of the deformed family. That is source-honest, because `q_B'(0)=1` for every `B` and the `B=1` current band is consistent through `t^0`. Claim 1 stands.

---

## 2. First centered row and no stale matrix

The chart two-form is `dx∧dy=s^2 ds∧dt`, already confirmed by the first-band review. Write

```text
F = p + s f1 + s^2 f2 + s^3 f3 + ⋯,
G = q_B + s g1 + s^2 g2 + s^3 g3 + ⋯,
```

with `p=t^{15}` and `q_B=t+B t^2+t^{25}`. Then `[s^k]J` is the coefficient of `s^{k+2}` in `F_s G_t - F_t G_s`. The first centered row is therefore the constant term

```text
f1 q_B' - p' g1 = 0,
```

i.e.

```text
f1 (1 + 2 B t + 25 t^{24}) - 15 t^{14} g1 = 0.
```

This is the displayed formula (5). The parent `B=0` compiler used only the summands `1` and `25 t^{24}`. The extra `2 B t` coupling is the entire first-order deformation of that row.

Later x-boundary formulae, re-derived from the same two-form and checked against the producer compilers:

| band | two-form identity | `q_B'` consumption |
|---|---|---|
| `[s^{-2}]J` | `f1 q_B' - 15 t^{14} g1` | every `t`-degree via `{0:1, 1:2B, 24:25}` |
| `[s^{-1}]J` | `f1 g1' - f1' g1 + 2 f2 q_B' - 30 t^{14} g2` | the `2 f2 q_B'` summand |
| `[s^0]J-1` | `f1 g2' + 2 f2 g1' + 3 f3 q_B' - 45 t^{14} g3 - 2 f1' g2 - f2' g1 - 1` | the `3 f3 q_B'` summand |

The inherited pole row `[r^1](J-1)` is the opposite-chart wedge `(-3 p q1' - 2 p1 q' + 4 p' q1 + 5 p1' q)/(-25)` in the r9 coordinate `ζ`. Its leading `p,q` are the r9 patterns, independent of `q_B`. Its jets `p1,q1` **are** `B`-dependent through the global coefficients, and the adaptive compiler rebuilds them from the `B_*`-parameterization rather than copying the numerical first-band pole.

Stale-matrix audit, against the actual matrices rather than comments:

- Homogeneous *transport* rank is `3470/3602` independently of `B`. That is the parent `946/976 + 2524/2626` split. The `[t^2]` slot of `[s^0]g` is present even at `B=0`, with right-hand side `0`; the deformation only changes that right-hand side to `B`. Reusing the transport *homogeneous* factorization is correct.
- The first-Jacobian *homogeneous* matrix is not `B`-independent. An independent `B=1` versus parent `B=0` row difference is identically zero except for the extra `2 t` coupling, and the degree-`t^1` difference is nonempty. The `B=1` probe factorizes the deformed matrix, not the parent echelon.
- `B=1` right-hand sides send `(g, t^2)` to `1` and send F1/pole leading lines through the field patterns `R^3,R^5` and `(L,A)`, not through the numerical first-band point `P=(η^5-1)^2(η^5-2)(η^5-28/25)`, `A=1/9`.
- Adaptive transport is rebuilt, then the first Jacobian, previous centered band, current centered band, and pole row are all recompiled with `Q_PRIME={0:1, 1:2 B_*, 24:25}` in `E`. No parent 94-space parameterization is reused.
- `replay.py` hard-codes rational `B=Q(1)` and is only the bounded helper / preflight. The load-bearing `B=1` theorem is `sextic_probe.py` over `E`.

Claim 2 stands.

---

## 3. Exact `B=1` branch

Independent insertion-order and reverse-row GE over `Q` then `E`:

| stage | insertion | reverse-row |
|---|---|---|
| transport + first Jacobian | rank `3508/3602`, dim `94` | rank `3508` |
| previous centered `[s^{-1}]J` | rank `36/94`, dim `58`, consistent | rank `36`, consistent |
| current homogeneous | tangent rank `25/58` | tangent rank `25` |
| current affine | empty at input row `("X0",4)` | empty (nonzero residual) |

The insertion-order residual equals the advertised element of `E`

```text
ρ_1 = (2145334 - 4154976 S + 4405068 S^2
       - 2488119 S^3 + 761922 S^4 - 105084 S^5)/3625
      + (136875/29) A.
```

An unreduced left-null combination reproduces this residual and a zero variable side. Serialization SHA-256 `d091b65e4bc7c66a83946499ab037ceb3812bcedc4c5311bbda8276bfa213732` matches the frozen probe.

The frozen parent `B=0` residue, copied from the hash-pinned uniform-third certificate (itself confirmed by the completed third-band hostile review) is the same `E`-element with constant numerator `2495634`. The difference is the rational

```text
ρ_1 - ρ_0 = (2145334 - 2495634)/3625 = -350300/3625 = -14012/145 ∈ Q ⊂ E.
```

Every higher `S`-coefficient and the `A`-coefficient are identical. In particular `ρ_1 ≠ ρ_0` in `E`, so the degree-four obstruction is `B`-sensitive: it is not an invariant copied from the monomial boundary. The identity is exact in the field, not a secant slope claimed to be `dρ/dB`.

Nonzero status: `ρ_1` has `A`-component `136875/29 ≠ 0` in `K`, and `1,A,A^2` is a `K`-basis of the irreducible cubic extension `E/K`. Hence `ρ_1 ≠ 0` in `E`. No floating-point evaluation and no single complex embedding is used. Every `Q`-homomorphism `E → C` is injective, so the contradiction holds at all 18 pole-normalized conjugates.

The `B=1` probe does not impose the inherited pole row. That is valid for emptiness: an affine system already inconsistent on the 58-space remains inconsistent on every affine subspace, including the 56-space cut by the pole. The adaptive branch, which does impose the pole, is the certificate that the death is not a one-sided omission.

Claim 3 stands.

---

## 4. Adaptive candidate

`Δ = 14012/145` is a nonzero rational, hence a unit in `E`. The parent residue `ρ_0` is nonzero in `E` (nonzero `A`-component). Therefore

```text
B_* = ρ_0 / Δ
```

is a well-defined nonzero element of `E`. Its `repr` SHA-256 is `64010183890daa1938b4eac6add7933767238738e9783f41b5821dcc4b56d750`, matching the freeze. Degeneracy of the registered q-boundary cannot occur:

- leading coefficient of `t^{25}` is `1`;
- coefficient of `t` is `1`;
- `q_{B_*}(0)=0` and `q_{B_*}'(0)=1`;
- the deformation coefficient itself is `B_* ≠ 0` in `E`, so this is not a silent return to the monomial boundary.

The adaptive program does not plug `B_*` into a secant formula. It rebuilds:

1. the 6547-row transport, with `[t^2]g_0` right-hand side equal to `B_*`;
2. the first Jacobian band with `q'=1+2 B_* t+25 t^{24}`;
3. the previous centered band with the same derivative;
4. the inherited pole row from field `(L,A)` and from the `B_*`-dependent jets `p1,q1`;
5. the current centered band, again with that derivative.

Affine dependence on `B` is not assumed at any of those stages. The appearance of a nonzero `A^2` component in the adaptive residue, while both `ρ_0` and `ρ_1` have vanishing `A^2` slot, is an exact witness that the reduced residue is not affine in `B`. A program that had interpolated the two sample residues would have kept `A^2=0` and would have reported zero at `B_*`.

Claim 4 stands.

---

## 5. Adaptive ranks and obstruction

Independent insertion-order and reverse-row GE over `E`:

| stage | insertion | reverse-row |
|---|---|---|
| transport only | rank `3470/3602`, dim `132` | rank `3470` |
| first Jacobian (5) | adds rank `38`, dim `94` | rank `38` |
| previous centered + pole | adds rank `38`, dim `56` | rank `38` |
| current homogeneous | tangent rank `25/56` | tangent rank `25` |
| current affine | empty at `("X0",4)` | empty (nonzero residual) |

Transport rank `3470` recovering the parent transport-only rank is the expected `B`-independence of the homogeneous transport matrix. First-Jacobian rank remaining `38` at this particular `B_*` is a sample, not a generic-rank theorem.

The insertion-order residual has all three `E/K` basis slots nonzero (`[True, True, True]` on `residual.coefficients`, each a nonzero element of `K`). That is the correct field-nonzero test: a slot is zero iff all six rational coordinates of the corresponding `K`-element vanish. Serialization SHA-256 `be22c8d155c26a5091494d68c32e043cce66b4275330a022e493528659a4a53b` matches the freeze. An unreduced left-null combination reproduces this residual and a zero variable side. Reverse-row GE is also inconsistent, so the emptiness is not an insertion-order pivot artefact.

Claim 5 stands.

---

## 6. Logical scope

What is proved, and only what is proved:

- the two exact points `B=1` and `B_*` of this one q-jet are empty through the displayed centered band;
- at those points the previous-band (and, at `B_*`, pole) constraints remain consistent, so the death is at `[s^0 t^4]J`;
- the degree-four residue moves with `B`, because `ρ_1-ρ_0=-14012/145≠0` in `E`;
- the simple secant zero of `{ρ_0,ρ_1}` is not a survivor after the full `B`-dependent rebuild.

Printed flags `full_b2_family_killed = false`, `SP2_killed = false`, and `JC2_resolved = false` match that scope.

What is not proved, and is not licensed by any rank or residue in this freeze:

- emptiness for arbitrary `B`, or even for generic `B`;
- constancy of the ranks `3508`, `36`, `38`, `25` off the two tested points (the producer correctly warns that echelon pivots vary with `B`);
- any other q-jet (`t^3`, …, `t^{24}` in `q`, or any extra term in `p`);
- a different common centering, a nonzero dead-stretch coefficient, a different reduced F1 shape, or a different pole normalization;
- SP-2, any of the eight td=6 terminal classes, landing, mapping degree, or JC2.

Two empty points do not cut a one-parameter family. Rank-jump loci of the `B`-dependent linear systems are unexamined. Claim 6 stands.

---

## 7. Successor

The current obstruction, at a fixed `B`, is an affine inconsistency of a linear system compiled *after* a `B`-dependent previous-band solve. Both the ambient affine space and the current matrix depend on `B` through pivot denominators. A family kill therefore has to:

1. work on the generic-rank stratum, producing a residual that is a rational function of `B` with values in `E`;
2. separately treat every locus at which a pivot lead vanishes (rank jumps), as a finite list of exact specializations.

That is symbolic one-parameter elimination, including the rank-jump strata. Sample interpolation cannot substitute: the adaptive calculation already shows that the two-point secant of `{ρ_0,ρ_1}` is not the true residual.

An adjoint or jet-orbit shortcut does **not** certify the same question more cheaply, for three independent reasons.

- A left kernel that is independent of `B` would have to remain a left kernel after composition through the `B`-dependent previous-band parameterization. Constructing such a kernel is the elimination.
- `B` cannot be absorbed by reparameterizing the centered coordinate `t`. Here `t=xy^4-y^3-y^2-y` is the specific polynomial of the frozen chart `(1,1,1)`. Absorbing the `t^2` coefficient of `q` would be a *different* licensed deformation (centering), not a normalization of this family.
- Finite-difference / adjoint-at-`B=0` along the `t^2` direction is exactly the secant that `B_*` already tested and that failed. The new `A^2` support at `B_*` is the obstruction to that shortcut.

A cheaper *implementation* of the same mathematical test is still allowed: fraction-free GE over `E(B)` (or over `Q(B)` for the rational first band, then `E(B)`), recording vanishing principal minors as the rank-jump loci, then specializing those finitely many points. That remains one-parameter elimination, not interpolation, and not an adjoint certificate. The producer’s stated successor is therefore the smallest source-honest next test.

Claim 7 stands.

---

## Parameter, staging, and field caveats (non-blocking)

1. `F` and `E` are imported from the frozen uniform-third gate, not re-derived as the constant-row polynomial of the `B`-family. The `B=1` current band being consistent through `t^0` on that field is compatible with `[s^0 t^0]J-1` still vanishing, because `q_B'(0)=1` for every `B`. A uniform-in-`B` derivation of the constant row is a different theorem and is not claimed.
2. Dimension `94` at `B=1` matches the parent total rank, but the free-variable *index set* need not be the parent set: the first-Jacobian matrix depends on `B`. The claim is dimension, not a named identity block.
3. `replay.py` `main()` is a rational preflight at the numerical first-band F1/pole specialization, not the degree-18 theorem. The load-bearing `B=1` certificate is `sextic_probe.py`.
4. Homogeneous transport rank `3470` is `B`-independent and is not evidence that first-Jacobian rank `38` is generic in `B`.
5. The `B=1` probe omits the pole; the adaptive probe includes it. Emptiness on the 58-space implies emptiness on the 56-space, so the omission does not weaken the `B=1` kill. It does mean pole consistency at `B=1` is unstated.
6. `SHEET6.md` / `SHEET6-LROOT.md` hashes differ from the first-band freeze by campaign-status notes. The IIa/r9 combinatorics at 187–200 are the same ledger text.

---

## Hashes

| artifact | SHA-256 |
|---|---|
| deformation report | `f098dea46ca99ed26bb0ad541efe2135c78c3c1f47da8d92096a91dfece4fcc0` |
| bounded compiler helpers | `0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357` |
| exact `B=1` replay | `8834cd9b365a9a20d058c3ef6b0ef927c6aee05c895b650b6bc2b927ed6250ca` |
| exact adaptive replay | `ca09d8dc6d154eec7a0fe39747c6ea348fc5e7cccd26bae7bdadae148cd51be5` |
| `B=1` canonical stdout | `68863a4c0deb4eb0d2745714612bfb8ea7b445dd7355833181cf5178241ef2bd` |
| `B=1` exact residue | `d091b65e4bc7c66a83946499ab037ceb3812bcedc4c5311bbda8276bfa213732` |
| adaptive canonical stdout | `b5cf24e87e84900f796affb8c78a63af805bb0c68c0fdab03d0ef99fa318aceb` |
| adaptive candidate `B_*` | `64010183890daa1938b4eac6add7933767238738e9783f41b5821dcc4b56d750` |
| adaptive exact residue | `be22c8d155c26a5091494d68c32e043cce66b4275330a022e493528659a4a53b` |
| freeze manifest | `1cc169979ee610649f87be1c7069a3517564752e8d3417f764dc09a7d22916a9` |
| imported uniform-third replay | `7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8` |
| imported uniform-third report | `0d3e2dc8e57b03060582d6906212ae707cb1d42b10416cff85117daa93b4ed7b` |
| imported next-row replay | `0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8` |
| imported first-band replay | `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735` |
| uniform-third hostile review | `582933fca15c8e1005460591f795102d43c60a9733b8bc19f0b7bdbd716784ef` |
| moduli-uniformity hostile review | `d95e0d684464c2f56b76ceb5cf32158d47ed907565216ff2974ca1d5f883730b` |
| paired-third-band hostile review | `3f2462b2c61d01a39769cc82cf3e9a04732e2bc824edea92bcb0eb9c449d3ad7` |
| first-band hostile review | `265c1103391e2bae889c018bb0637fe486e7292644c0295e4f9965e5085e7a25` |
| next-row hostile review | `12834c356c2c26243522b2609753370118ecd2c8ed87907033ca27e926d2ac2f` |

**JC2 scope.** This is an exact emptiness certificate for two points of one smallest q-boundary deformation inside one normalized SP-2 chart-pattern control. The one-parameter `B` family is not killed. The calculation neither realizes nor kills a terminal class, supplies no Keller pair, does not quantify broader boundary, centering, or dead-stretch moduli, and neither proves nor disproves the plane Jacobian conjecture.
