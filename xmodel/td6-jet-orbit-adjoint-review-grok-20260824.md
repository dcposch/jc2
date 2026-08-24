# Hostile different-model review — TD6 jet-orbit adjoint gate

| Field | Value |
|---|---|
| Claim under review | Frozen TD6-JET-ORBIT-ADJOINT: after the registered linear chart and the `p=t^{15}` section, `q_2` is the sole transverse class of the smallest boundary-jet quotient, and exact differentiation of the staged elimination including `lambda'` gives `c'(0)=-4720/29\neq0` at the already-inconsistent degree-18 base point |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Hidden local-to-global step | none: a nonzero first derivative of an already nonzero residue proves that the obstruction moves and licenses an exact one-parameter compatibility polynomial; it is not a root, not a family kill, not a generic-rank theorem, and not SP-2 / terminal-class / JC2 |
| Evidence tier | independent exact algebra over `Q` and `E=K[A]/(A^3-α)` (registered orbit audit and dual replay; a second engine that does not import either registered program: own source-orbit/target-gauge/F1-tangent ranks, own two-form compilers for `[s^{-2}]J`, `[s^{-1}]J`, `[s^0]J-1`, and `[r^1](J-1)`, own dual-number class and Dual GE, unreduced `lambda(ε)^T A(ε)=0`, the two-summand identity for `c'(0)`, reverse-row affine GE over `E`, and the frozen-lambda counterexample `lambda_0^T b'(0)≠c'(0)`); primary-source read of the completed q2 point-probe producer/review |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T14:56:08Z – 2026-08-24T15:29:41Z |
| Python | 3.14.6; stdlib `fractions.Fraction` / `hashlib` only |
| Host | Darwin arm64 |

Producer inputs reread in full before any verdict:

- `xmodel/td6-jet-orbit-adjoint-gate-20260824.md` (SHA-256 `28a8869cf91f5e7d1e3601c52ee21742eca9187e57d7ac1065f22bcbd0ee402b`)
- `cases/td6_jet_orbit_adjoint_20260824/replay.py` (SHA-256 `fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198`)
- `cases/td6_jet_orbit_adjoint_20260824/replay.stdout` (SHA-256 `cd87743d3859a5fa5d4275f7e599a43a9565d0a16a01de4c133bd925b7df0ebf`)
- `cases/td6_jet_orbit_adjoint_20260824/orbit_audit.py` (SHA-256 `90bd44ebd6ed810e6d686d44bd84f2f852d623b22a371f137e215436394b967b`)
- `cases/td6_jet_orbit_adjoint_20260824/orbit_audit.stdout` (SHA-256 `e158eba810deac8334ec408d1acad313a677fe37552a36006d152f6b45718eb5`)
- `cases/td6_jet_orbit_adjoint_20260824/FREEZE.sha256` (SHA-256 `9d94e4f011584f5a6718e7bdb94609788faf76d87ec6455a2c9dd6ee34715378`)

All six freeze-file hashes match the launch prompt. The freeze file body is exactly the five producer payloads above; `MANIFEST.sha256` is the same byte string. `shasum -a 256 -c cases/td6_jet_orbit_adjoint_20260824/FREEZE.sha256` from the repository root reports all five files `OK`. The dual-syzygy digest `9527d18e4fbd48d0e6771cb9a45e1c4ffd6e33dfdc9c5cdc052fa6e37c883272` is printed by the dual replay, not a sixth freeze path, and is independently reproduced below. The committed basis is exactly `1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a`. No producer, case, canonical, ladder, or erratum file was edited. No AWS work was launched.

Imported and parent payloads, working-tree hashes on disk at review time:

- imported q2 compiler `cases/td6_boundary_q2_deformation_20260824/replay.py` SHA-256 `0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357`
- imported uniform-third replay `cases/td6_moduli_uniform_third_band_20260824/replay.py` SHA-256 `7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8`
- parent q2 point-probe report SHA-256 `f098dea46ca99ed26bb0ad541efe2135c78c3c1f47da8d92096a91dfece4fcc0`
- completed q2 hostile review SHA-256 `6df0d9c9dde4c4e8991b73da1c807ce40b4f44c2b587949c2312aaebf469665c` (overall **CONFIRMED**)

Frozen parent producers/reviews, reread against this tree:

- `xmodel/td6-two-chart-first-band-20260824.md` SHA-256 `cb373892233bddaf1b8fbf7722335ca43ee366b337151c3b244d2604d8168bf2`
- `cases/td6_two_chart_first_band_20260824/replay.py` SHA-256 `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735`
- `xmodel/td6-two-chart-first-band-review-grok-20260824.md` SHA-256 `265c1103391e2bae889c018bb0637fe486e7292644c0295e4f9965e5085e7a25` (overall **CONFIRMED**)
- `xmodel/td6-two-chart-next-row-20260824.md` SHA-256 `32124d20ec84ef59d5b116639176b12053f5da6de1a9458dd4a2095d6b1618f0`
- `cases/td6_two_chart_next_row_20260824/replay.py` SHA-256 `0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8`
- `xmodel/td6-two-chart-next-row-review-grok-20260824.md` SHA-256 `12834c356c2c26243522b2609753370118ecd2c8ed87907033ca27e926d2ac2f` (overall **CONFIRMED**)
- `xmodel/td6-moduli-uniformity-gate-20260824.md` SHA-256 `499e95763759fe195ab1eba5fbf97bfb9d255bbf6fb2b090add938d92f1f3a06`
- `cases/td6_moduli_uniformity_20260824/replay.py` SHA-256 `55340fa662a20e1777eaa18fae2d26589c11ec7f3f2960f4a0a6efe015e7b6ab`
- `xmodel/td6-moduli-uniformity-review-grok-20260824.md` SHA-256 `d95e0d684464c2f56b76ceb5cf32158d47ed907565216ff2974ca1d5f883730b` (overall **CONFIRMED**)
- `xmodel/td6-paired-third-band-20260824.md` SHA-256 `a98de6d23ff2942360c328e4eeb6c08e24a122b0f9c964a5ad586cf0b009e9f2`
- `cases/td6_paired_third_band_20260824/replay.py` SHA-256 `5d05a6de17e3959ad221527ab74c7da77ba1e1980e8a7d86d0fd8cdca10d468a`
- `xmodel/td6-paired-third-band-review-grok-20260824.md` SHA-256 `3f2462b2c61d01a39769cc82cf3e9a04732e2bc824edea92bcb0eb9c449d3ad7` (overall **CONFIRMED**)
- `xmodel/td6-moduli-uniform-third-band-20260824.md` SHA-256 `0d3e2dc8e57b03060582d6906212ae707cb1d42b10416cff85117daa93b4ed7b`
- `xmodel/td6-moduli-uniform-third-band-review-grok-20260824.md` SHA-256 `582933fca15c8e1005460591f795102d43c60a9733b8bc19f0b7bdbd716784ef` (overall **CONFIRMED**; all eight subclaims **CONFIRMED**)

The dual replay pins the q2 compiler at `0ba18447…` and the uniform-third replay at `7a21f949…` before import; the q2 compiler itself pins the next-row compiler at `0fc299a1…`, which pins the first-band compiler at `c55e2136…`. No imported-hash mismatch.

Cited canonical SP-2 / F1 / r9-M2 material, working-tree hashes on disk at review time:

- `ladder/SHEET6.md` SHA-256 `5ea8003685a8be0c2554f6966987cbd492583bf9c07603ccb984da48b3ac04f2`
- `ladder/SHEET6-LROOT.md` SHA-256 `9ff5d00567d7b6752ecc79892bb41959a450ddff3837bdb26179899ad2dfad5a` (SP-2 ledger 187–200)
- `ladder/SHEET6-AF2.md` SHA-256 `c7f7601d5b72e2512561d12d160ac8e7458ee3954a8c18182b41ef6174053b3c`
- `ladder/SHEET6-AF3.md` SHA-256 `555363fde61291a0c689bbf9d789c01f73734e0c403d350d85ae2fd0ddab8099`

`SHEET6.md` / `SHEET6-LROOT.md` differ from the first-band and q2-deformation freeze hashes because of uncommitted campaign-status notes. The combinatorial SP-2/IIa/r9-M2 typing used below is the same ledger text at 187–200.

**Promotion.** Accept as `Q2-TRANSVERSE / NONZERO-FIRST-DERIVATIVE / EXACT-COMPATIBILITY-POLYNOMIAL-LICENSED / STOP` of this one smallest registered boundary-jet quotient. Bank the full t2 orbit (2), the orbit-complement representative (3), ranks `7→8` after the fixed-linear-chart section, target-gauge rank `4` with Jacobian first-order sensitivity `0`, source tangent rank `4/4` in `(S,D,L,A)` with `F(7/4)=-53875/512`, staged ranks `3470/3602 → 132`, `38/132 → 94`, `38/94 → 56`, current homogeneous `25/56`, affine stop at input row `t^4` after three pivots, base residue (5), `c'(0)=-4720/29`, syzygy supports `4` and `3`, dual-syzygy digest `9527d18e…`, vanishing rank-change flags, and the identity `c(1)-c(0)=-14012/145 ≠ c'(0)`. Promote nothing else.

**Quarantine.** The one-parameter family in `B` is not killed. A nonzero derivative at an already inconsistent point does not prove absence of a finite root. Common centering, r9 dead stretch, broader p-boundary strata, other q-jets, other F1 patterns, SP-2, every td=6 terminal class, and JC2 remain open. Exact `J=1` is not proved or disproved. No interpolation of `c(B)` is licensed without a printed numerator/denominator degree bound and a separate treatment of every pivot/resultant root.

---

## Headline and subclaim table

Write `s=y^{-1}`, `x=s+s^2+s^3+t s^4`, F1 chart `x=q^{-5}`, `y=η q`, pole chart `x=r^{-25}`, `y=r^5+ζ r^{17}`, and on the imported sextic field `D=(2S^2-2S+3)/5`, `L=25(1-S+D)`, `A^3=9/L^8`.

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Infinitesimal `t↦t+ε t^2` acts as `(δT,δp,δq)=(t^2,15 t^{16},t^2+25 t^{26})`, not as `q_2` alone. The seven truncated orbit vectors `h=1,…,t^6` have rank seven; adjoining the q2-only vector raises rank to eight after the fixed linear chart. After `p=t^{15}`, `q(0)=0`, `q'(0)=1`, `q_2` is the sole remaining order-two q-slot and is transverse in that section | **CONFIRMED** | chart component omitted from the orbit; rank `7→7` after adjoining q2; a registered p-jet below `t^{14}` in the 15-fold-root stratum; producer treating q2-only as the full t2 orbit |
| 2 | Four rectangle-preserving det-1 target tangents have boundary-vector rank four and first-order Jacobian sensitivity zero. Source equations in `(S,D,L,A)` have rank `4/4` over `E`, using `F(7/4)=-53875/512≠0`. Common centering and r9 dead stretch are licensed frozen data, not gauges of this smallest quotient | **CONFIRMED** | target rank `<4`; a first-order `δJ` for a listed gauge; `F(7/4)=0` in `Q`; a source-compatible `(dS,dD,dL,dA)≠0`; producer silently placing `dc1,dc2,dc3` or `d6,…,d16` in the gauge subspace |
| 3 | Dual-number staged elimination, independently rebuilt, differentiates the normalized left syzygy. `lambda(ε)^T A(ε)=0` holds against the unreduced current matrix. `c'(0)=lambda_0^T b'(0)+lambda'(0)^T b_0`, and the frozen-lambda formula `lambda_0^T b'(0)` is not `c'(0)` | **CONFIRMED** | Dual GE that skips derivative-only columns and still prints `-4720/29` from `lambda_0` alone; unreduced `lambda^T A` nonzero; `lambda'` support `0`; two summands failing to add to `c'(0)` |
| 4 | Exact stages `3470→132`, `38→94`, `38→56`, current homogeneous `25/56`, no first-order rank-change flags, base residue (5) in `E`, `c'(0)=-4720/29≠0`, syzygy supports `4` and `3`. The old secant `c(1)-c(0)=-14012/145` is not substituted for the derivative | **CONFIRMED** | any stated rank different; a rank-change flag; residue ≠ (5); `c'(0)` with a nonzero `S` or `A` slot, or equal to `-14012/145`; affine system consistent at `t^4` |
| 5 | Full t2 reparametrization has vanishing `[t^4]` sensitivity by the power-series identity. Every listed target gauge has vanishing first-order Jacobian sensitivity. No registered chart, p-boundary, target, or F1-orbit direction absorbs the q2-only class | **CONFIRMED** | `[t^4](ρ(t+ε t^2)^4)≠0`; a listed gauge with `δJ` at order `ε`; orbit+targets+q2 rank `<12`; a source-compatible F1 tangent; producer calling centering a gauge that kills q2 |
| 6 | Nonzero `c'(0)` at an already inconsistent base point proves only that the obstruction moves and licenses an exact `B`-polynomial. No inference to absence of a root, generic rank, emptiness of the full `B`-family, centering/dead-stretch families, SP-2, a terminal class, or JC2 is licensed | **CONFIRMED** | producer promoting a family kill, a generic-rank theorem, an SP-2 or class kill, or JC2; printed flags `q2_family_killed`, `SP2_killed`, or `JC2_resolved` true |
| 7 | The proposed staged fraction-free `E[B]` calculation is the smallest source-honest successor, provided it prints certified numerator/denominator degree bounds, replays a symbolic or deterministically sufficient identity, and treats every pivot/resultant root as its own rank stratum. Point sampling and interpolation without a proved bound are not licensed. A frozen `lambda_0` kernel is not a cheaper certificate: `lambda'` support `3` kills it | **CONFIRMED** | producer licensing three-point interpolation as a family polynomial; a `B`-independent left kernel already in hand; successor omitting exceptional pivot strata |

All remarks below are non-blocking unless marked otherwise. None changes a rank, a residue, a hash, or a verdict.

---

## Replay

Registered commands, rerun unmodified from the charged tree:

```sh
python3 cases/td6_jet_orbit_adjoint_20260824/orbit_audit.py
python3 cases/td6_jet_orbit_adjoint_20260824/replay.py
```

Exit codes 0. Wall-clock of the dual replay `real 357.53`. Printed verdicts, character-for-character against the frozen stdout files:

```text
TD6-JET-ORBIT-AUDIT: PASS
full_t2_orbit = chart:t^2; p:15*t^16; q:t^2+25*t^26
q2_only_mod_orbit = -chart:t^2-15*p:t^16-25*q:t^26
fixed_linear_chart_q2_transverse = true
target_gauge_rank = 4 (two translations, reciprocal scaling, g+=eps*f)
source_tangent_rank_SDLA = 4/4
F(7/4) = -53875/512
full_t2_orbit_t4_adjoint_derivative = 0
```

```text
TD6-Q2-DUAL-ADJOINT: PASS
transport_rank = 3470/3602
first_J_rank = 38/132
previous_paired_rank = 38/94
current_affine_pivots_before_t4_stop = 3/56
current_homogeneous_rank = 25/56
residual_value = (2495634/3625)*S^0+...|(136875/29)*S^0|0
residual_q2_derivative = (-4720/29)*S^0|0|0
derivative_nonzero = True
lambda_support = 4
lambda_prime_support = 3
dual_left_syzygy.sha256 = 9527d18e4fbd48d0e6771cb9a45e1c4ffd6e33dfdc9c5cdc052fa6e37c883272
rank_change_flags = {'first': 0, 'previous': 0, 'current_through_stop': 0}
verdict = Q2-TRANSVERSE-NONZERO-FIRST-DERIVATIVE
q2_family_killed = false
SP2_killed = false
JC2_resolved = false
```

Canonical stdout SHA-256 values, including final newlines, match the freeze (`e158eba8…` / `cd87743d…`). Arithmetic is `fractions.Fraction` on the residue field `E`. No CAS, no floating point, no modular sampling of the Jacobian system, no AWS.

A second engine, written for this review and not imported from either registered program, rebuilt the 3602-variable transport from the hash-pinned first-band compiler and then diverged: (i) first-Jacobian, previous-centered, current-centered, and inherited-pole compilers derived from the two-form `[s^{k+2}](F_s G_t-F_t G_s)` and the pole wedge divided by `-25`, taking `q_B'=1+2ε t+25 t^{24}` as an explicit dual argument; (ii) an independent dual-number class and Dual GE that reduces derivative-only entries in already-pivoted columns; (iii) coefficientwise affine replay over `E[ε]/(ε^2)`; (iv) unreduced left-null multiply of the current matrix; (v) reverse-row affine GE over `E`; (vi) the frozen-lambda counterexample `lambda_0^T b'(0)`. Every stated rank, the `t^4` inconsistency, both residue serializations, the derivative `-4720/29`, both syzygy supports, the dual-syzygy digest, and the vanishing rank-change flags matched. The frozen-lambda formula is not the derivative. Wall-clock `real 389.18`. A separate exact orbit/gauge/F1 engine, also not imported from `orbit_audit.py`, independently reconstructed (2)–(4) and the rank table `7→8`, `4`, `4/4`.

---

## 1. Source-orbit quotient

SP-2 from `SHEET6-LROOT.md:187–200`: chain

```text
F0 = (3,6,5,2,8) → F1 = (15,60,5,4,4)  (μ=2 IIa k=2, n=12) → (0,y),
```

type `(3,5)`, rectangles `(15,60)/(25,100)`, reduced F1 pattern `(η^5-c^5)^2 Π_2`, one x-cluster. With the chain orbit normalized to `C=1` this is `R(z)=(z-1)^2(z^2-Sz+D)`. The r9/M2 pole shape is the AF3 §4 family transported by `L=25(1-S+D)` and normalized by `L^8 A^3=9`. Zero dead stretch and common centering `(1,1,1)` are the same licensed specializations already confirmed by the first-band through q2-deformation reviews.

The registered x-boundary is the polynomial pair `p=t^{15}`, `q=t+t^{25}`. For a local reparametrization `t↦t+ε h(t)`,

```text
δp = p' h = 15 t^{14} h,     δq = q' h = (1+25 t^{24}) h,
```

and the chart slot is `δT=h` because `t` is the displayed coefficient of `s^4`. Taking `h=t^2` gives, independently of the producer audit,

```text
δT = t^2,     δp = 15 t^{16},     δq = t^2 + 25 t^{26}.
```

That is (2). The vector `δq=t^2` by itself is not (2). Subtracting the orbit from the q2-only vector produces the fixed-chart representative (3):

```text
(-δT, -δp, -δq) = (-t^2, -15 t^{16}, 25 t^{26}).
```

The over-cap terms `t^{16}` and `t^{26}` lie outside the compiled degree caps `deg p=15` and `deg q=25`. Truncating (2) to those caps leaves `chart:t^2 + q:t^2`. In the fixed-linear-chart section the chart slot is set to zero, so this truncated orbit is still linearly independent of q2-only. That is the geometric content of the rank jump.

Independent least-index row reduction of the seven vectors `h=1,t,…,t^6`, each carrying its chart component, the p-block `15 t^{14}h`, and the q-block `(1+25 t^{24})h`, has rank seven. Adjoining `{("q",2):1}` raises the rank to eight. Every nonzero reparametrization has a chart component equal to `h` itself, so no linear combination of the seven can cancel the chart slot and leave a q2-only vector.

p-stratum, independently: the polynomial family `a(t-b)^{15}` at `(a,b)=(1,0)` has tangents `t^{15}` (scale) and `-15 t^{14}` (root translation). These are exactly the p-blocks of `h=t` and `h=1`. Coefficients of `p` below `t^{14}` change the root partition and leave the 15-fold-root stratum. After the section

```text
p=t^{15},  q(0)=0,  q'(0)=1,
```

the order-two q-jet is `(q_0,q_1,q_2)` with `q_0` a g-translation (target gauge) and `q_1` already fixed, so the only remaining slot is `q_2`. That is the sense in which `q_2` is the sole transverse class at the smallest registered boundary-jet order: sole remaining order-two q-coefficient, and transverse to the registered reparametrization ledger after the linear chart is fixed. It is not a uniqueness claim in a larger automorphism group that would unfreeze centering or dead stretch.

Claim 1 stands.

---

## 2. Other gauges and omitted moduli

Four rectangle-preserving determinant-one target tangents, as raw boundary vectors:

| gauge | boundary vector | Jacobian to first order |
|---|---|---|
| translation of `f` | `δp=1` | `δJ=0` identically: constants vanish in every derivative |
| translation of `g` | `δq=1` | `δJ=0` identically |
| reciprocal scaling | `(δp,δq)=(p,-q)` | `J((1+ε)f,(1-ε)g)=(1-ε^2)J`, so `[ε^1]=0` |
| lower shear | `δq=p` i.e. `g↦g+ε f` | `f_x(g_y+ε f_y)-f_y(g_x+ε f_x)=J` identically |

These are identities of `J=f_x g_y-f_y g_x`, not samples. Upper shear `f↦f+ε g` would raise `deg f` from 15 to 25 and leave the rectangle; it is correctly omitted. Independent rank of the four boundary vectors is four. Rank of the seven orbit vectors plus these four is eleven. Rank of that eleven plus q2-only is twelve: none of the four target vectors carries a `q_2` slot, so they cannot absorb the class.

F1/pole source tangent, independently reconstructed from the frozen equations `Q=-2S^2+2S+5D-3=0`, `H=1-S+D`, `3H^3=1`, `L=25H`, `L^8 A^3=9`:

```text
(-4S+2) dS + 5 dD           = 0,
-9 H^2 dS + 9 H^2 dD         = 0,
25 dS - 25 dD + dL           = 0,
(8/L) dL + (3/A) dA          = 0.
```

Least-index field GE over `E` has rank `4/4`. The first two rows have determinant `9 H^2 (7-4S)`. The identity `3H^3=1` in `E` forces `H≠0`. Direct evaluation of the imported primitive `F=24S^6-252S^5+1170S^4-3045S^3+4680S^2-4032S+1411` at `S=7/4` is the rational

```text
F(7/4) = -53875/512 ≠ 0,
```

so `7-4S≠0` in `K=Q[S]/(F)`. There is no source-compatible tangent in `(S,D,L,A)` alone. Those coordinates can still appear later as forced compensators; they are not free moduli of this gate.

Common centering `(c1,c2,c3)` and the eleven r9 dead-stretch slots `d6,…,d16` are named in the producer table as licensed, not audited as gauge, and not computed in this scoped gate. No source automorphism is exhibited that would normalize them while keeping all three charts and both rectangles. They are therefore not silently placed in the gauge subspace, and they are not part of the smallest order-two q-quotient. Their adjoint columns change the transport matrix itself and require separate pencils.

Claim 2 stands.

---

## 3. Differentiated elimination

The chart two-form is `dx∧dy=s^2 ds∧dt`, already confirmed by the first-band review and re-derived here:

```text
y=s^{-1},  x=s+s^2+s^3+t s^4,
dx∧dy = s^4 dt ∧ (-s^{-2} ds) = s^2 ds∧dt.
```

Writing `F=p+s f1+s^2 f2+s^3 f3+…` and `G=q_B+s g1+s^2 g2+s^3 g3+…`, the identity `(F_x G_y-F_y G_x) s^2 = F_s G_t-F_t G_s` with `J=1` forces

```text
[s^0]:  f1 q' - 15 t^{14} g1 = 0,
[s^1]:  f1 g1' - f1' g1 + 2 f2 q' - 30 t^{14} g2 = 0,
[s^2]:  f1 g2' + 2 f2 g1' + 3 f3 q' - 45 t^{14} g3 - 2 f1' g2 - f2' g1 = 1.
```

The independent engine compiled these three bands, and the inherited pole row

```text
[r^1](J-1) = (-3 p q1' - 2 p1 q' + 4 p' q1 + 5 p1' q)/(-25),
```

over `E[ε]/(ε^2)` with `q'=1+2ε t+25 t^{24}`. It did not call the producer `Dual` class, `solve`, `affine_parameterization`, or `inconsistency_certificate`.

Dual GE was written to reduce every already-pivoted column, including a coefficient that is derivative-only. That is the `lambda' A` term. Affine parameterizations were split into a frozen triangular base solve over `E` and a differentiated triangular solve for the `ε`-parts, with free coordinates held at zero derivative (the stable-pivot section, licensed by the vanishing rank-change flags below). Coefficientwise identity replay over the dual field held at the first-J and previous-paired stages.

At the current band the independent engine produced a dual left syzygy of support four, with derivative support three. Direct multiplication against the unreduced current matrix proved

```text
lambda(ε)^T A(ε) = 0,     lambda(ε)^T b(ε) = ρ - (4720/29) ε.
```

The two-summand decomposition is an identity of that syzygy, not a fit:

```text
c'(0) = lambda_0^T b'(0) + lambda'(0)^T b_0.
```

Independently, the two summands are the producer’s printed elements of `E`, every nonconstant `S` slot and the `A` slot cancel, and the remaining rationals satisfy

```text
-209308447819087441/4020125 + 209308447164777441/4020125
  = -654310000/4020125 = -4720/29.
```

The frozen-lambda formula `lambda_0^T b'(0)` equals the first summand and is not `c'(0)`. That is the common invalid shortcut, independently refuted: `lambda'` is nonzero on three of the four current rows, so the base left syzygy does not stay a kernel.

The dual-syzygy digest of the independent combination is `9527d18e4fbd48d0e6771cb9a45e1c4ffd6e33dfdc9c5cdc052fa6e37c883272`, matching the freeze. Reverse-row affine GE over `E` of the same current matrix remains rank `25` homogeneously and remains inconsistent.

Claim 3 stands.

---

## 4. Ranks, residue, and derivative

Independent Dual GE (insertion order) and reverse-row affine GE over `E`:

| stage | independent result |
|---|---|
| transport only | rank `3470/3602`, dimension `132` |
| first centered Jacobian band | rank `38/132`, dimension `94`; Dual rank-change flags `0` |
| previous centered + inherited pole | rank `38/94`, dimension `56`; Dual rank-change flags `0` |
| current homogeneous | rank `25/56` (insertion and reverse-row) |
| current affine | empty at input row `("X0",4)` after three Dual pivots; Dual rank-change flags `0` through the stop |

The insertion-order residual equals the advertised element of `E`

```text
ρ = (2495634 - 4154976 S + 4405068 S^2
     - 2488119 S^3 + 761922 S^4 - 105084 S^5)/3625
    + (136875/29) A.
```

Nonzero status is the nonzero `A`-component in the `K`-basis `1,A,A^2`, already confirmed by the uniform-third and q2-deformation hostile reviews. The Dual derivative is the rational `-4720/29` with vanishing `S` and `A` slots. In particular `c'(0)≠0` in `E`. Serialization of the derivative matches the producer printout; the dual-syzygy digest matches the freeze.

The parent q2 point-probe identity `ρ_1-ρ_0=-14012/145` is the secant of the two exact samples `B=0` and `B=1`. Clearing denominators,

```text
-4720/29 = -23600/145 ≠ -14012/145,
```

and the difference `-9588/145` is a nonzero rational. The Dual calculation is not a substitution of that secant. The adaptive emptiness at the secant-cancellation point `B_*=ρ_0/(14012/145)`, already confirmed by the parent hostile review, is the geometric content of the same distinction: the reduced residue is not affine in `B`.

Claim 4 stands.

---

## 5. Gauge negative controls

Full t2 reparametrization, as a power series. If a compatibility series begins `R=ρ t^4+O(t^5)`, then

```text
R(t+ε t^2) = ρ (t+ε t^2)^4 + O(t^5) = ρ t^4 + 4 ρ ε t^5 + O(ε^2,t^5),
```

so the coefficient of `t^4` is invariant. Directly, `compose_tangent({4:1}, {2:1})` has vanishing degree-four slot. This is the correct negative control for a coordinate rename. A Dual run that deformed only `p` by `15 t^{16}` and `q` by `t^2+25 t^{26}` with the chart held fixed would be the wrong control: those over-cap terms are invisible to the compiled degree caps, and the leftover compiled vector is q2 itself, whose sensitivity is the nonzero number (1). The chart component is what makes (2) a pure reparametrization.

Target gauges: the four Jacobian identities of §2 are the first-order sensitivity. Because the residue is a coefficient of `J-1`, a target motion that preserves `J` to first order cannot move that coefficient. Translations leave the registered section (`p(0)=0`, `q(0)=0`); they are quotient directions, not new jets.

Missing-direction audit, against the actual tangent table rather than comments:

- every reparametrization `h=t^k` for `k=0,…,6` has a chart component and is quotiented by the fixed linear chart;
- p-stratum scale and translation are the `k=1` and `k=0` orbit p-blocks;
- the four target gauges are independent of the orbit and of q2 (rank 12);
- `(dS,dD,dL,dA)` has rank `4/4` on the frozen source equations;
- common centering and dead stretch are named as licensed extra families, not as gauges of this quotient.

No registered chart, p-boundary, target, or F1-orbit direction makes the q2 class gauge-trivial. A later theorem that unfroze centering and absorbed `B t^2` into a chart automorphism would be a different statement; it is not claimed, and the producer correctly defers those columns to a matrix-changing pencil.

Claim 5 stands.

---

## 6. Logical meaning

What is proved, and only what is proved:

- in the registered section, `q_2` is a genuine one-dimensional transverse class of the smallest boundary-jet quotient;
- at the already inconsistent sextic points, the first derivative of the `t^4` residue along that class is `-4720/29≠0` in `E`;
- every inherited rank is stable to first order, so the derivative is not a pivot jump in disguise;
- the obstruction therefore moves, and an exact one-parameter compatibility polynomial in `B` is now a licensed next calculation.

Printed flags `q2_family_killed = false`, `SP2_killed = false`, and `JC2_resolved = false` match that scope.

What is not proved, and is not licensed by `c'(0)≠0`:

- absence of a finite root of the (not yet computed) compatibility polynomial;
- generic rank of any `B`-dependent matrix off `B=0`;
- emptiness of the full `B`-family, or even emptiness for generic `B`;
- anything about the three common centering coefficients or the eleven dead-stretch coefficients;
- other q-jets, a different p-partition, a different F1 shape, or a different pole normalization;
- SP-2, any of the eight td=6 terminal classes, landing, mapping degree, or JC2.

A first derivative at an inconsistent point is a motion of an obstruction, not a kill of the zero locus. Claim 6 stands.

---

## 7. Successor audit

The current obstruction, as a function of `B`, is an affine inconsistency compiled after a `B`-dependent previous-band solve. Both the ambient affine space and the current matrix depend on `B` through pivot denominators. A family polynomial therefore has to:

1. work on the generic-rank stratum, producing a residual that is a rational function of `B` with values in `E`;
2. separately treat every locus at which a pivot lead vanishes, as a finite list of exact specializations.

The proposed staging is the correct implementation of that test, not a different test:

- reuse the constant rank-`3470` transport factorization (homogeneous transport is `B`-independent; the particular response is affine in the single `[t^2]g_0` slot);
- form the first-J pencil, which is genuinely affine in `B` via `q'=1+2Bt+25 t^{24}` and the affine g-particular;
- fraction-free / Bareiss elimination over `E[B]`, recording a generic pivot minor and every exceptional factor;
- propagate only the reduced family through previous centered/pole rows and then the current compatibilities;
- at roots of the compatibility numerator or of the pivot/resultant product, rebuild exact systems.

Adjoint data at `B=0` are Hermite conditions `c(0)=ρ`, `c'(0)=-4720/29`. They prove the numerator is locally nonconstant. They do not certify interpolation. A reconstructed rational function becomes theorem-grade only after a fraction-free numerator and denominator degree bound is printed, more exact value/derivative conditions than that bound are used, the cross-multiplied identity is replayed symbolically or on a provably sufficient deterministic evaluation set, and every root of the pivot product is handled as its own rank stratum.

Cheaper exact methods that remain the same mathematical test: Bareiss on the last compatibility minor after the staged reductions (Cramer’s rule for the residual), or a determinant of a certified generic maximal minor of the current pencil over `E[B]`. Both still require the printed degree bound and the exceptional-strata list.

Methods that are not licensed:

- point sampling, two-point or three-point interpolation, or Hermite interpolation, without a proved bound (the parent adaptive emptiness at `B_*` is already the counterexample to the two-point secant);
- a `B`-independent left kernel. The identity `lambda'(0)≠0` on three current rows is an exact obstruction to that shortcut.

Claim 7 stands.

---

## Parameter, staging, and field caveats (non-blocking)

1. `F` and `E` are imported from the frozen uniform-third gate, not re-derived as the constant-row polynomial of the `B`-family. The current band being consistent through `t^0` on that field is compatible with `[s^0 t^0]J-1` still vanishing, because `q_B'(0)=1` for every `B`. A uniform-in-`B` derivation of the constant row is a different theorem and is not claimed.
2. Dual free coordinates are held at zero derivative. That is a section of the affine family, valid on the observed first-order rank-stable stratum, not a proof that the same index set of free variables is generic in `B`.
3. Homogeneous transport rank `3470` is `B`-independent and is not evidence that first-Jacobian rank `38` is generic in `B`.
4. The full t2-orbit negative control is the power-series identity for `[t^4]`, not a second Dual elimination of the over-cap pair `(15 t^{16}, 25 t^{26})` with the chart held fixed. That truncated pair is q2, whose sensitivity is (1).
5. Target-gauge Jacobian identities are identities of `J`, not four extra 3602-variable Dual pencils. Residue invariance along those target motions of the map follows from `J` invariance.
6. `SHEET6.md` / `SHEET6-LROOT.md` hashes differ from the first-band freeze by campaign-status notes. The IIa/r9 combinatorics at 187–200 are the same ledger text.

---

## Hashes

| artifact | SHA-256 |
|---|---|
| producer report | `28a8869cf91f5e7d1e3601c52ee21742eca9187e57d7ac1065f22bcbd0ee402b` |
| exact dual replay | `fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198` |
| canonical dual stdout | `cd87743d3859a5fa5d4275f7e599a43a9565d0a16a01de4c133bd925b7df0ebf` |
| orbit/source audit | `90bd44ebd6ed810e6d686d44bd84f2f852d623b22a371f137e215436394b967b` |
| canonical orbit stdout | `e158eba810deac8334ec408d1acad313a677fe37552a36006d152f6b45718eb5` |
| dual-syzygy certificate digest | `9527d18e4fbd48d0e6771cb9a45e1c4ffd6e33dfdc9c5cdc052fa6e37c883272` |
| freeze manifest | `9d94e4f011584f5a6718e7bdb94609788faf76d87ec6455a2c9dd6ee34715378` |
| imported q2 compiler | `0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357` |
| imported uniform-third replay | `7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8` |
| parent q2 point-probe report | `f098dea46ca99ed26bb0ad541efe2135c78c3c1f47da8d92096a91dfece4fcc0` |
| completed q2 hostile review | `6df0d9c9dde4c4e8991b73da1c807ce40b4f44c2b587949c2312aaebf469665c` |
| imported uniform-third report | `0d3e2dc8e57b03060582d6906212ae707cb1d42b10416cff85117daa93b4ed7b` |
| imported next-row replay | `0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8` |
| imported first-band replay | `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735` |
| uniform-third hostile review | `582933fca15c8e1005460591f795102d43c60a9733b8bc19f0b7bdbd716784ef` |
| moduli-uniformity hostile review | `d95e0d684464c2f56b76ceb5cf32158d47ed907565216ff2974ca1d5f883730b` |
| paired-third-band hostile review | `3f2462b2c61d01a39769cc82cf3e9a04732e2bc824edea92bcb0eb9c449d3ad7` |
| first-band hostile review | `265c1103391e2bae889c018bb0637fe486e7292644c0295e4f9965e5085e7a25` |
| next-row hostile review | `12834c356c2c26243522b2609753370118ecd2c8ed87907033ca27e926d2ac2f` |

**JC2 scope.** This is an exact transversality-and-first-derivative certificate for one smallest q-boundary class inside one normalized SP-2 chart-pattern control. The one-parameter `B` family is not killed. The calculation neither realizes nor kills a terminal class, supplies no Keller pair, does not quantify centering or dead-stretch moduli, and neither proves nor disproves the plane Jacobian conjecture.
