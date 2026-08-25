# Hostile different-model review — TD6 licensed c1 line exclusion

| Field | Value |
|---|---|
| Claim under review | Frozen TD6-C1-LINE-EMPTY: in the licensed normalized control `(c1,c2,c3)=(C,1,1)`, `p=t^{15}`, `q=t+t^{25}`, there is no solution for any `C` over any field extension of `E`. The proof is the exact union of three frozen strata: raw `C=0`, raw `C=3`, the generic-transport identity on `C(C-3)J≠0`, and the raw rebuild over `E[C]/(J)` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Hidden local-to-global step | none: emptiness of this one licensed fixed normalized one-parameter section is not a kill of simultaneous center motion, of other moduli, of TD6, of SP-2, of a terminal class, or of JC2 |
| Evidence tier | independent exact algebra over `Q`, `K=Q[S]/(F)`, `E=K[A]/(A^3-α)`, `Q(C)`, and `E[C]/(J)` (registered replays as provenance only; a second engine that does not import the first-stage replay: own sparse polynomial division, lift, denominator-clearing, `D` factorization, reverse-row first rank, and coefficientwise identity replay; J-stratum and fibre rebuilds with every `EJ` inverse logged by an independent `xgcd` against `J`; own `k k^{-1}=1`, own `√6∉K` reduction at `p=11`, own cover of `A^1`); primary-source read of the three freezes and of the reviewed whole-`q_B`, adjoint, and centering-tangent packages |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` |
| Review window (UTC) | 2026-08-24T20:25:00Z – 2026-08-24T21:10:00Z |
| Python | 3.14.6; stdlib `fractions.Fraction` / `hashlib` only in the independent algebra; FLINT `fmpq` / `fmpq_poly` only as the exact `Q(C)` transport backend already used by the frozen source |
| Host | Darwin arm64 |

Producer inputs reread in full before any verdict:

- `xmodel/td6-c1-line-kill-gate-20260824.md` (SHA-256 `dbf60b008f968033b7e91a5c5975bbedffc0529009aa53db6fb4b139bd844cb9`)
- `xmodel/td6-c1-first-stage-localized-gate-20260824.md` (SHA-256 `152cc1092f60c5c32ee3eee3ff2e41f7ed3116dd18d7c82a76610b40591d98f9`)
- `xmodel/td6-c1-raw-transport-fibres-gate-20260824.md` (SHA-256 `24ecd47e3c9e2045d72f0b2c70cfa3257c5bf21e4142dcb0ae2c704f58b865e1`)
- quadratic `MANIFEST.sha256` / `FREEZE.sha256` (both SHA-256 `767af7e5de63b3a08dc495107b22a8ef568bca467eda9884a275dba1533905f0`)
- quadratic `replay.py` (SHA-256 `86a7931e31e6d1387e3797a58094c6bfd69444910e2fdf7d27a374d9942a1e7f`)
- quadratic `replay.stdout` (SHA-256 `4a9f3022fb7fd1dcc0933dd17d636c423729c70cc58ce0fb4399323b486f5dd2`)
- fibre `MANIFEST.sha256` / `FREEZE.sha256` (both SHA-256 `7cfe741bc6344a5eba2da60bac679b685f98f3b6c4d63d73fbdd6533dc6eda8c`)
- first-stage `MANIFEST.sha256` / `FREEZE.sha256` (both SHA-256 `3f844546eaedde3c96c1a834f882161d47890c7c0e4adbf1fceef2869a085d57`)

The four charged hashes in the launch prompt match disk. `shasum -a 256 -c` on all three `MANIFEST.sha256` files reports every named payload `OK`, and `cmp` of each `MANIFEST.sha256` against the sibling `FREEZE.sha256` is silent. Shared `c1_pencil.py`, `c1_rational_transport.py`, `fast_evec.py`, and `fast_efield.py` are byte-identical across the three cases. No producer, case, canonical, prompt/log/run, coordination, ladder, or predecessor file was edited. No AWS work was launched. All scratch lived in `/tmp/td6_c1_line_kill_review_20260824/`.

The first-stage freeze was completed during the review window: an initial inventory saw no `MANIFEST.sha256` / `FREEZE.sha256` and a 2 120-byte truncated stdout that stopped after the previous-stage checkpoint. By the time the independent first-stage engine finished, the freeze on disk was the 911 164-byte stdout hashed above, with matching manifest. The identity was reconstructed independently of that freeze and matches it.

Frozen predecessor licenses, working-tree hashes on disk at review time:

- whole-`q_B` producer `xmodel/td6-boundary-qb-pencil-gate-20260824.md` SHA-256 `5e1f6b44e143360a41550ae552b20bef02325414f96c5fd469ba4d016eb5eb22`
- whole-`q_B` hostile review `xmodel/td6-boundary-qb-pencil-review-grok-20260824.md` SHA-256 `5c238f2bd3cf11422093184e1563f7671d0abd4b8f06a6fb5dfd7d380ac51319` (overall **CONFIRMED**)
- adjoint producer `xmodel/td6-jet-orbit-adjoint-gate-20260824.md` SHA-256 `28a8869cf91f5e7d1e3601c52ee21742eca9187e57d7ac1065f22bcbd0ee402b`
- adjoint hostile review `xmodel/td6-jet-orbit-adjoint-review-grok-20260824.md` SHA-256 `2cd542615dfcc7b15dab3796adba0c91b84dcba606da6ff442b3d69dd4fb79f9` (overall **CONFIRMED**)
- adjoint dual replay `cases/td6_jet_orbit_adjoint_20260824/replay.py` SHA-256 `fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198`
- centering-tangent producer `xmodel/td6-centering-tangent-gate-20260824.md` SHA-256 `15b08835512839d044c049b11ba889be1fbf06c52dc9ad6487e714910ac774d3`
- centering-tangent hostile review `xmodel/td6-centering-tangent-review-grok-20260824.md` SHA-256 `3d33ed766a4ea02b79bee1dd13b144c2f3adbfd7a0dbb571314c36679b92d13a` (overall **CONFIRMED**)
- first-band replay `cases/td6_two_chart_first_band_20260824/replay.py` SHA-256 `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735`

`c1_pencil.py` pins the adjoint dual replay at `fb138b0f59…` before import; `c1_rational_transport.py` pins the first-band compiler at `c55e2136…`. No imported-hash mismatch.

**Promotion.** Accept as `TD6-C1-LINE-EMPTY / EXACT STRATUM COVER / FIXED NORMALIZED SECTION ONLY / NOT-SP2 / NOT-JC2` of this one licensed one-parameter section `(C,1,1)` in the frozen normalized TD6 source typing. Bank the generic transport exceptional divisor `C(C-3)`, the original-row identity `D P_{12}=D(-k/50)+∑ M_i L_i` with `D=(C-3)^2 J/4`, the two raw fibres `C=0,3`, the quotient rebuild over `E[C]/(J)`, the 38 Bezout first-band inverses, and `k k^{-1}=1`. Promote nothing else.

**Quarantine.** The machine flag `family_killed` is `false` in every stratum because no single freeze is the whole line; the scoped theorem is their exact logical union. `SP2_killed=false` and `JC2_resolved=false` throughout. This does not kill TD6, SP-2, a terminal class, or JC2. It does not cover simultaneous two- or three-center motion, q-boundary, p-boundary, dead-stretch, F1-orbit, or pole-scale moduli. The centering-tangent transversality and target-shear caveats remain active. Exact `J=1` is not proved or disproved.

---

## Headline and subclaim table

Write `s=y^{-1}`, `x=C s + s^2 + s^3 + t s^4`, F1 chart `x=q^{-5}`, `y=η q`, pole chart `x=r^{-25}`, `y=r^5+ζ r^{17}`, and on the imported sextic field `D_src=(2S^2-2S+3)/5`, `L=25(1-S+D_src)`, `A^3=9/L^8`. The current obstruction is the parameter-free unit `-k/50` with `k=252-342S+144S^2-36S^3`.

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | The licensed line is exactly `(c1,c2,c3)=(C,1,1)` with frozen `p=t^{15}`, `q=t+t^{25}`, frozen F1/pole patterns, and zero dead stretch. The generic two-chart transport echelon over `Q(C)` has exceptional irreducible factors exactly `C` (multiplicity 2) and `C-3` (multiplicity 1). No other center, boundary, dead-stretch, F1, or pole modulus is specialized after that normalization | **CONFIRMED** | a nonconstant pivot factor other than `C` and `C-3`; `c2` or `c3` not identically `1`; a silent `B`, dead-stretch, F1-orbit, or pole-scale assignment; selected-minor gcd with `J` of positive degree |
| 2 | Independent rebuild of the generic transport and first-band systems retains a genuine degree-two current polynomial `P_{12}` of 2 893 terms. Exact original-row division gives `D P_{12}=D(-k/50)+∑_{i=1}^{28} M_i L_i` with 1 489 multiplier terms, `D=(C-3)^2(4C^2+20C+1)/4`, and identity digest `31b56241…`. The cleared multipliers lie in `E[C][u]`, so the identity specializes at first-rank jumps. On the transport chart only `J=0` remains | **CONFIRMED** | identity digest mismatch; `D` not equal to the displayed factorization; remainder ≠ `D(-k/50)`; a non-polynomial multiplier after clearing; a first-pivot gcd with `D` other than `1`, `C-3`, or `(C-3)J` that the identity failed to cover |
| 3 | Raw rebuilds at `C=0` and `C=3` of the original 3 602-column transport, after specialization and not by evaluating a singular generic chart, have rank `3470`, first rank `38`, zero compatibility, genuine quadratic currents, and full original-row reduction to `-k/50` | **CONFIRMED** | generic `Q(C)` pivot list evaluated at a vanishing lead; rank ≠ `3470/3602` or first ≠ `38/132`; reduced current with a free parameter; remainder ≠ `-k/50` |
| 4 | Original transport rows rebuilt over `E[C]/(J)` without sampling a root reproduce rank `3470/3602`, first rank `38/132`, zero compatibilities, a 2 893-term degree-two current, and the 28-row / 1 530-term source identity with every documented digest | **CONFIRMED** | a sampled algebraic root of `J`; any stated digest different; a leftover free parameter in the reduced current |
| 5 | `J` is separable (`disc=384≠0`) and coprime to `C(C-3)`. It is in fact irreducible over `E`. Every one of the 38 first-band inverses, and every transport lead inverted in `E[C]/(J)`, has Bezout gcd of degree 0 with `J`. If the quotient split, those units would still be units on every geometric component. No nilpotents, no inseparability, no overlap with `C=0,3` | **CONFIRMED** | `disc(J)=0`; a first-band inverse with `gcd(·,J)` of positive degree; `J(0)=0` or `J(3)=0`; a hidden assumption that `J` stays irreducible used as the only cover argument |
| 6 | `k^{-1}` is the displayed degree-five element of `Q[S]/(F)`, and `k k^{-1}=1` exactly. Hence `-k/50` remains a unit after every scalar extension of `E` in scope | **CONFIRMED** | `k k^{-1}≠1` in `K`; `gcd(k,F)≠1`; a zero-divisor image of `-k/50` after a scalar extension of `E` |
| 7 | The four strata `C=0`, `C=3`, `C(C-3)J≠0`, and `J=0` exhaust the affine line over every extension of `E`. Every handoff between the three freezes is source-valid. No point of the licensed section is uncovered | **CONFIRMED** | a `C` at which the generic identity is invalid and no raw rebuild exists; a first-rank jump on the transport chart with `D≠0` at which the multipliers fail to be regular; an extra exceptional divisor of transport |
| 8 | Even confirmed, the theorem empties only this licensed fixed normalized one-parameter section. It is not TD6, SP-2, a terminal class, or JC2, and it does not cover simultaneous center motion or other moduli | **CONFIRMED** | producer promoting an SP-2, class, or JC2 kill; printed `SP2_killed` or `JC2_resolved` true; a claim uniform in `(c2,c3)` or in dead-stretch / F1 / pole / extra boundary jets |

All remarks below are non-blocking unless marked otherwise. None changes a rank, a polynomial, a hash, or a verdict.

---

## Replay

Registered commands, rerun unmodified from the charged tree (first-stage via an independent engine that loads only the hash-pinned `c1_pencil` source; quadratic and fibre via the registered `main` with extra inverse / remainder checks):

```sh
/opt/homebrew/bin/python3 cases/td6_c1_quadratic_stratum_20260824/replay.py
/opt/homebrew/bin/python3 cases/td6_c1_raw_transport_fibres_20260824/replay.py 0 3
```

Both exit 0. Independently recomputed JSON digests match the frozen stdout files byte-for-byte on every load-bearing hash. Printed machine flags, character-for-character against the frozen objects:

```text
family_killed = false
SP2_killed = false
JC2_resolved = false
```

The independent first-stage engine (no import of `cases/td6_c1_first_stage_ideal_20260824/replay.py`) rebuilt transport over `Q(C)`, the original first-band rows, and the genuine 132-variable current polynomial, then divided, lifted, and cleared. Wall-clock `real 1442.96`. Printed assertions:

```text
independent exceptional factors {'x': 2, 'x + (-3)': 1}
independent transport PASS
independent first PASS
independent raw P12 terms=2893 degree=2
independent first-stage identity PASS
D == (C-3)^2 J / 4 True
cleared remainder == D*(-k/50) True
reverse-row first rank 38
identity_sha256 = 31b56241f6edb79932af8ddb8b376ffc7727eea037abf741c5998867eea1ae69
source_relation_count = 28
source_relation_term_count = 1489
INDEPENDENT FIRST-STAGE ALL ASSERTIONS PASS
```

Producer PASS banners were not used as evidence. The identity digest, `D` digest `d533ae90…`, and `D(-k/50)` digest `cebbda8b…` were recomputed from the reconstructed polynomials and match the charged reports.

---

## 1. Normalized line and transport-exceptional fibres

The three cases set `fb.CENTER=(C,1,1)` and clear `_X_POWER_CACHE` before compiling the original 3 602-column two-chart transport. Boundary data are `{15: 1}` on the `(15,60)` chart and `{1: 1, 25: 1}` on the `(25,100)` chart. `qd.B` is the zero dual. No dead-stretch slot is written. F1 and pole patterns are those of the hash-pinned first-band compiler (`F1_CHAIN=1`, `F1_ORBIT_A=2`, `F1_ORBIT_B=28/25`, `POLE_A=1/9`). `configure_qd` installs the frozen source field `(S,D,L,A)` and `Q_PRIME={0:1, 24:25}` for later Jacobian compilation; it does not retarget F1 orbits, pole scale, or rectangles.

Independent `Q(C)` transport GE, rebuilt from those original rows, has rank `3470/3602`, four nonconstant pivot events, and exceptional irreducible factors exactly

```text
(x)                 aggregate_multiplicity=2
(x + (-3))          aggregate_multiplicity=1
```

The selected minor is linear, `aC+b`, with digest `7506dbb411cc205bccb03ce410934be0ce4ebe249e61316cab750554b723a542`. Independently, `gcd(aC+b, C)=1`, `gcd(aC+b, C-3)=C-3` so the minor itself vanishes at `C=3`, and `gcd(aC+b, J)=1`. Two of the four pivot events have denominator `C`, so the generic chart is also invalid at `C=0` even though the product of leads does not vanish there. No other irreducible appears. Specializing the generic parameterization at `C=0` or `C=3` is therefore not licensed; the fibre freeze rebuilds the original rows after specialization.

---

## 2. Generic first-stage identity

The independent engine never formed the rejected all-at-once affine `110×132` model. After the 132-dimensional transport chart, it compiled the genuine current `t^{12}` polynomial in all 132 parameters (2 893 terms, parameter degree 2) from the hash-pinned two-form compiler `compile_x_current`, whose degree-12 slice is termwise identical to the fibre/J `compile_current_degree`. Exact division by the normalized first-band echelon, lift of every quotient to the original first-band rows, and clearing of `C`-denominators produce

\[
 D(C)\,P_{12}
 = D(C)\Bigl(-{k\over50}\Bigr)
 + \sum_{i=1}^{28} M_i(C,\mathbf u)\,L_i(C,\mathbf u)
\]

in `E(C)[\mathbf u]`, with the displayed `D` and with every `M_i` in `E[C][\mathbf u]` (parameter degree ≤ 1, `C`-degree ≤ 10). The identity digest, `D` digest, and `D(-k/50)` digest match the charged reports. Reverse-row first-band GE independently reproduces rank `38/132` with no nonzero residual.

The eight distinct nonconstant first-pivot numerators have gcd with the cleared right-hand side equal to `1`, `C-3`, or `(C-3)J`, matching the first-stage report. On the transport chart `C(C-3)≠0` the only remaining zero of `D` is `J=0`. First-rank-jump values with gcd `1` against `D` (including `C=1,2,-2,-11/9,-1/18` and the extra root `C=-1/8` of the displayed quadratic) have `D≠0`, so the polynomial identity still forces `-k/50=0`. The first-stage JSON field `remaining_first_exceptional_stratum = 4C^3+8C^2-59C-3` is exactly `(C-3)J`; on the transport chart this is `J=0`. The flag `first_pivot_roots_covered=false` is the conservative `all(gcd.degree==0)` test and is not a hole in the polynomial identity.

Because the identity is polynomial in `C` and the transport sections are regular on `C(C-3)≠0`, it cannot be used at `C=0,3`. Those fibres are the raw-rebuild package.

---

## 3. Raw fibres `C=0` and `C=3`

Each fibre specializes `CENTER` first, then rebuilds both global transport charts from original rows. After specialization the elimination has degree span `0` and no exceptional factors: this is not evaluation of the singular generic chart. Independent rerun:

| fibre | transport | first | raw `P_{12}` | source rows / terms | reduced digest |
|---|---|---|---|---|---|
| `C=0` | `3470/3602`, free `132`, compat `0` | `38/132`, incompat `0` | 2 824 terms, deg 2, `be8e80ff…` | 28 / 1 423, `3c44f2dc…` | `233c0ce8…` |
| `C=3` | `3470/3602`, free `132`, compat `0` | `38/132`, incompat `0` | 2 885 terms, deg 2, `1bd39dc9…` | 28 / 1 515, `617017b2…` | `233c0ce8…` |

Selected-minor digests `3349b4fb…` and `be8c3932…` match the fibre report. Both reduced constants equal the independently computed `-k/50`, digest `8631ba66…`. Full original-row certificates were coefficientwise replayed before printing. No previous/pole or current-band parameterization is used.

---

## 4. Quadratic stratum over `E[C]/(J)`

`J=4C^2+20C+1` is specialized as a modulus, not as a sampled root. Independent rebuild of the original 3 602-column rows over `Q[C]/(J)`, propagation of the `E`-valued right-hand side in `E[C]/(J)`, and adaptive first-band elimination give

| object | independent value | charged |
|---|---|---|
| transport rank | `3470/3602` | same |
| compatibility | `0` | same |
| free variables | `132` | same |
| elimination digest | `affda5d3…` | same |
| first rank | `38/132` | same |
| first incompatibility | `0` | same |
| unit inverses | `38` | same |
| raw `P_{12}` | 2 893 terms, deg 2, `107615b4…` | same |
| source rows / terms | 28 / 1 530, `009b97df…` | same |
| reduced `P_{12}` | `a72003a4…` | same |

The reduced polynomial is the single term `-k/50`. The displayed `k` and `k^{-1}` records match. `previous_pole_or_current_parameterizations_used` is false.

---

## 5. Bezout inverses, splitting, nilpotents, overlap

`disc(J)=400-16=384=64·6` is not a square in `Q`, so `J` is irreducible over `Q` and separable in characteristic 0. Independently `J(0)=1`, `J(3)=97`, and `gcd(J,C)=gcd(J,C-3)=1`. There is no overlap with the transport-exceptional fibres and no double root, hence no nilpotents in `E[C]/(J)` after any scalar extension.

`[E:K]=3` is odd, so `√6∈E` if and only if `√6∈K`. Reduction of the frozen sextic `F` modulo `11` is square-free, has two simple linear factors `S=1` and `S=8`, and `(6/11)=-1`. A global square root of `6` in `K` would reduce to a square in those `F_{11}` components, which is impossible. Thus `J` remains irreducible over `E`, and `E[C]/(J)` is a field. The producer does not assume this: every inverse used in `E[C]/(J)` is an `xgcd` against `J` with gcd of degree 0.

An independent wrapper replaced `EJ.inverse` by an `xgcd` that records the gcd length, then reran the whole quotient rebuild. All 3 509 logged inverses (the 3 470 transport leads in `E[C]/(J)` together with the 38 first-band leads, plus the internal unit checks) have gcd length 1. In particular the 38 first-band inverses claimed by the report are units. If `J` had split, gcd degree 0 would still mean coprime to both linear factors, hence a unit on every geometric component of `V(J)`. Inseparability is excluded by `disc≠0` in characteristic 0. Zero-divisors do not occur on this `E`, and would not have been inverted without raising `NonUnit` if they had.

---

## 6. The obstruction is a unit

Working only in `Q[S]/(F)` with `F=24S^6-252S^5+1170S^4-3045S^3+4680S^2-4032S+1411` and the displayed inverse,

\[
 k·k^{-1}=1,\qquad \gcd(k,F)=1.
\]

Independently `-k/50=-126/25+171/25\,S-72/25\,S^2+18/25\,S^3`, whose `frac_record` digest is `8631ba66…` and whose `EJ`-record digest is `a72003a4…`, matching every reduced current in the three freezes. A point of any first-band fibre over any extension of `E` would force this unit to vanish.

---

## 7. Exhaustion and handoffs

The polynomial `C(C-3)J` is square-free over `Q`. Over any extension `L` of `E`, every value of `C` in `L` lies in exactly one of

```text
C = 0,     C = 3,     J(C) = 0,     C(C-3)J(C) ≠ 0.
```

Handoffs:

- generic identity: regular on the transport chart `C(C-3)≠0`; after imposing `-k/50≠0`, only `D=0` remains; on that chart `D=0` iff `J=0`;
- raw fibres: cover the two transport-exceptional points by original-row rebuild, not by specializing the generic chart;
- quotient rebuild: covers the whole scheme `V(J)` without choosing a root.

No first-rank jump on the transport chart is left as an extra stratum: those with `gcd(D,·)=1` are killed by the polynomial identity, and those sharing `C-3` or `J` are the fibres / quotient already rebuilt. The licensed section is affine in `C`; no claim is made at infinity. The union is therefore exhaustive for the advertised line.

---

## 8. Scope

Every freeze prints `family_killed=false`, `SP2_killed=false`, `JC2_resolved=false`. The combined report is the logical union of those three certificates and is still confined to the frozen normalized TD6 source typing and the one-parameter section `(C,1,1)`. Centering-tangent transversality remains a statement in the registered normalized section; a new global-domain normalization that moves the other charts or the fixed rectangles is not being declared a gauge that absorbs `C`. The invalid all-at-once affine `110×132` model is not used. Nonlinear current rows remain genuine polynomials until reduced through a licensed linear ideal.

---

## Non-blocking remarks

- The first-stage JSON still advertises `remaining_first_exceptional_stratum = 4C^3+8C^2-59C-3` and `first_pivot_roots_covered=false`. The cubic is `(C-3)J`, so on the transport chart the remaining zero is `J=0`, which is the reading of the combined report. Not a hole.
- `rt.factor` always prints the banner `TD6-C1-GENERIC-TRANSPORT: PASS`, including after numerical specialization. After `C=0` or `C=3` the printed exceptional-factor count is 0 and the degree span is 0; the banner is leftover naming, not a generic-chart evaluation.
- An independent `P_{12}` serialization that hashed a Python `list` rather than a `tuple` produced a different raw-polynomial digest; the identity digest, which includes `D`, the remainder, and the 28 relations, matched `31b56241…`, so the polynomial is the same.
- The first-stage freeze landed during the review window. The independent reconstruction does not depend on that timing.

---

## Verdict

**CONFIRMED.** The licensed normalized line `(c1,c2,c3)=(C,1,1)` is empty over every extension of `E`. This is not TD6, SP-2, a terminal class, or JC2.
