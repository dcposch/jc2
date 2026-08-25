# Hostile different-model review — TD6 c1 raw transport-exceptional fibres

| Field | Value |
|---|---|
| Claim under review | Frozen TD6-C1-RAW-TRANSPORT-FIBRES: in the registered normalized section `(c_1,c_2,c_3)=(C,1,1)`, `p=t^{15}`, `q=t+t^{25}`, the two fibres `C=0` and `C=3` of the generic two-chart transport exceptional divisor `C(C-3)` are empty after an adaptive rebuild of the original 3,602-column transport system, an adaptive first-band of rank `38/132`, and exact reduction of the genuine quadratic current `t^{12}` polynomial to the unit `-k/50` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Hidden local-to-global step | none: emptiness of these two raw fibres in one fixed normalized section is not emptiness of the `c1` line, not a first-stage cubic kill, not SP-2 / terminal-class / JC2 |
| Evidence tier | independent exact algebra over `Q` and `E=K[A]/(A^3-α)` after specializing `C` to `{0,3}` *before any elimination*; registered replay used only as regression. Second engine does not import the raw-fibre `replay.py`, its `Rat`-over-`Q(C)` factor, `FAST_FIELD`, or its division certificate: own flint `fmpq` sparse GE of the 3,602-column matrix, own reverse-row rank, own E-valued transport propagate, own first-band compiler from the adjoint identity, own current-`t^{12}` compiler from the q2 two-form identity, own min-index and max-index first-band echelons, own original-row polynomial identity replay, own EEA for `k^{-1}` and the unit `-k/50`. Generic c1 transport package used only to name why `C=0,3` are its transport-exceptional fibres |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | charged basis and HEAD at close `2e6104a417cfe15a93a901aa0a9129094a2ae11b` |
| Review window (UTC) | 2026-08-24T20:12:07Z – 2026-08-24T20:57:19Z |
| Python | 3.14.6; `fractions.Fraction`, flint `fmpq` 0.9.0, hash-pinned predecessor `E` |
| Host | Darwin arm64 |

Producer inputs reread in full before any verdict:

- `xmodel/td6-c1-raw-transport-fibres-gate-20260824.md` (SHA-256 `24ecd47e3c9e2045d72f0b2c70cfa3257c5bf21e4142dcb0ae2c704f58b865e1`)
- `cases/td6_c1_raw_transport_fibres_20260824/replay.py` (SHA-256 `e99e0dbdccca4c7c80f1809397ca5147283b51147c335664b1e620ad8dbfd755`)
- `cases/td6_c1_raw_transport_fibres_20260824/c1_pencil.py` (SHA-256 `ade679490b32397361fc04045580572240ee4ca04cfd25fb106a17361f88da49`)
- `cases/td6_c1_raw_transport_fibres_20260824/c1_rational_transport.py` (SHA-256 `ed6a70efddedcb4d1739826c6307d00194900bd745f646270e482ceaec5d3aab`)
- `cases/td6_c1_raw_transport_fibres_20260824/fast_evec.py` (SHA-256 `740ec0058aecf2656d3adc4eb1f8b7dbe5bcb1321fe3a3816f400643fc61cb91`)
- `cases/td6_c1_raw_transport_fibres_20260824/fast_efield.py` (SHA-256 `e2a614beac9c2ecb5655251029dd8f510dfb507402e80cf49d93d1d1bc525608`)
- `cases/td6_c1_raw_transport_fibres_20260824/replay.stdout` (SHA-256 `b48210ae9c97d358904fb32b7bfec391c1c422d0a776131762002be5799b510b`)
- `cases/td6_c1_raw_transport_fibres_20260824/MANIFEST.sha256` and `FREEZE.sha256` (both SHA-256 `7cfe741bc6344a5eba2da60bac679b685f98f3b6c4d63d73fbdd6533dc6eda8c`)

`shasum -a 256 -c cases/td6_c1_raw_transport_fibres_20260824/MANIFEST.sha256` reports every named file `OK`. `cmp` of `MANIFEST.sha256` against `FREEZE.sha256` is silent. The freeze body is exactly those seven payloads.

Charged launch-prompt hashes versus freeze:

| object | charged | on disk | match |
|---|---|---|---|
| producer report | `24ecd47e3c9e2045…58b865e1` | `24ecd47e3c9e2045…58b865e1` | yes |
| MANIFEST | `7cfe741bc6344a5e…dc6eda8c` | `7cfe741bc6344a5e…dc6eda8c` | yes |
| FREEZE | `7cfe741bc6344a5e…dc6eda8c` | `7cfe741bc6344a5e…dc6eda8c` | yes |
| canonical stdout | `b48210ae90100151…1894e1b7` | `b48210ae9c97d358…579b510b` | **no** |

The launch prompt’s “canonical stdout” field shares the prefix `b48210ae` with the freeze file and then diverges. The MANIFEST line for `replay.stdout` is the on-disk hash. Registered replay of `replay.py 0 3` reproduced the freeze file byte-for-byte (`cmp` silent, SHA-256 `b48210ae9c97d358…579b510b`). This is a launch-prompt transcription error, not a freeze-integrity failure, and it does not touch any identity below.

No producer, case, canonical, ladder, notes, prompt, log, run, coordination, or predecessor file was edited. No AWS work was launched. All scratch lived in `/tmp/td6_c1_raw_fibres_review_20260824/`.

Frozen predecessor payloads, working-tree hashes on disk at review time:

- whole-`B` producer `xmodel/td6-boundary-qb-pencil-gate-20260824.md` SHA-256 `5e1f6b44e143360a41550ae552b20bef02325414f96c5fd469ba4d016eb5eb22`
- whole-`B` different-model review `xmodel/td6-boundary-qb-pencil-review-grok-20260824.md` SHA-256 `5c238f2bd3cf11422093184e1563f7671d0abd4b8f06a6fb5dfd7d380ac51319` (overall **CONFIRMED**)
- adjoint producer `xmodel/td6-jet-orbit-adjoint-gate-20260824.md` SHA-256 `28a8869cf91f5e7d1e3601c52ee21742eca9187e57d7ac1065f22bcbd0ee402b`
- adjoint hostile review `xmodel/td6-jet-orbit-adjoint-review-grok-20260824.md` SHA-256 `2cd542615dfcc7b15dab3796adba0c91b84dcba606da6ff442b3d69dd4fb79f9` (overall **CONFIRMED**)
- exact dual replay `cases/td6_jet_orbit_adjoint_20260824/replay.py` SHA-256 `fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198`
- centering-tangent producer `xmodel/td6-centering-tangent-gate-20260824.md` SHA-256 `15b08835512839d044c049b11ba889be1fbf06c52dc9ad6487e714910ac774d3`
- centering-tangent hostile review `xmodel/td6-centering-tangent-review-grok-20260824.md` SHA-256 `3d33ed766a4ea02b79bee1dd13b144c2f3adbfd7a0dbb571314c36679b92d13a` (overall **CONFIRMED**)
- two-chart first-band compiler `cases/td6_two_chart_first_band_20260824/replay.py` SHA-256 `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735`

The raw-fibre `c1_pencil.py` pins the dual replay at `fb138b0f59…` before import; `c1_rational_transport.py` pins the first-band compiler at `c55e2136…`. No imported-hash mismatch.

The generic c1 transport source `c1_rational_transport.py` is byte-identical in `cases/td6_c1_first_stage_ideal_20260824/` (SHA-256 `ed6a70ef…`). That package is used below only to name the generic *transport* exceptional divisor. Its later first-stage cubic is distinguished, not used as a raw-rank certificate.

Cited SP-2 ledger, working-tree hash on disk at review time:

- `ladder/SHEET6-LROOT.md` SHA-256 `9ff5d00567d7b6752ecc79892bb41959a450ddff3837bdb26179899ad2dfad5a` (SP-2 ledger 187–200)

**Promotion.** Accept as `TD6-C1-C0-C3-EMPTY / RAW-TRANSPORT-REBUILT / FULL-FIRST-ROW-POLYNOMIAL-CERTIFICATES / NOT-A-FAMILY-KILL` of the two fibres `C=0` and `C=3` **in this one fixed normalized section**. Bank the adaptive transport ranks `3470/3602`, vanishing transport compatibility, 132 parameters, the two adaptive-minor digests, adaptive first-band rank `38/132` with empty incompatibility, the genuine quadratic current `t^{12}` polynomials of `2824` and `2885` terms, the original-row identities `P_{12}=-k/50+∑ M_i L_i` with `28` nonzero source rows and multiplier term counts `1423` and `1515`, and that `-k/50` is a nonzero unit of `E`. Promote nothing else.

**Quarantine.** `family_killed=false`, `SP2_killed=false`, and `JC2_resolved=false` remain hard. This does not close the full `c1` line, the later generic first-stage exceptional roots of `4C^2+20C+1`, other center / boundary / dead-stretch / F1 / pole moduli, SP-2, any td=6 terminal class, or JC2. The running source-valid successor is a denominator-cleared `t^{12}` identity over `E[C]` through the generic first-band ideal, covering every first-stage pivot root on the transport chart `C(C-3)≠0`.

---

## Headline and subclaim table

Write `s=y^{-1}`, `x=C s+s^2+s^3+t s^4`, F1 chart `x=q^{-5}`, `y=η q`, pole chart `x=r^{-25}`, `y=r^5+ζ r^{17}`, and on the imported sextic field `D=(2S^2-2S+3)/5`, `L=25(1-S+D)`, `A^3=9/L^8`, `k=252-342S+144S^2-36S^3`.

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | After specializing `C=0` and `C=3` before any elimination, each original 3,602-column two-chart transport system has rank `3470/3602`, zero dependent-row incompatibility, and 132 free parameters. Adaptive selected-minor digests are `3349b4fb…e2477a` at `C=0` and `be8c3932…940036` at `C=3`. No singular generic pivot list is evaluated | **CONFIRMED** | rank other than `3470`; a leftover transport compatibility; a generic `Q(C)` pivot formula with vanishing denominator used at either fibre; adaptive minor digest mismatch |
| 2 | On each independently rebuilt chart the first centered band, compiled from source, is consistent of rank `38/132`. Rank is stable to reverse-row and max-column GE. The min-index echelon is triangular (`pivot = min(row)`), which is why the producer’s increasing sweep is an elimination order | **CONFIRMED** | first-band rank other than `38`; a nonzero residual on a dependent first row; max-column rank drop |
| 3 | Before first-band reduction the current `t^{12}` equation is genuinely quadratic, with `2824` terms at `C=0` (digest `be8e80ff…de55a1`) and `2885` terms at `C=3` (digest `1bd39dc9…8a18275`) | **CONFIRMED** | parameter degree other than two; term-count or digest mismatch; a linear or constant raw polynomial |
| 4 | Exact division by the normalized adaptive first-band echelon leaves the one-term remainder `-k/50` at both fibres (digest `233c0ce8…6644c7`). The same constant is the remainder against the *max-column* first-band echelon. Lifted multipliers replay against the original 38 first rows: `28` nonzero source rows, `1423` terms at `C=0` (digest `3c44f2dc…1115e7`) and `1515` terms at `C=3` (digest `617017b2…ca5581`). A reduced-row-only certificate is not the object checked | **CONFIRMED** | remainder other than `-k/50`; identity failing on an original row; 28/1423/1515 or digest mismatch |
| 5 | `F=24S^6-252S^5+1170S^4-3045S^3+4680S^2-4032S+1411` is irreducible over `Q` by Rabin modulo 31, `A^3-α` is irreducible over `K` because `N_{K/Q}(α)=3^{28}/5^{96}` is not a cube, the displayed `k^{-1}` multiplies `k` to `1` in `K`, and `-k/50` is a nonzero unit of `E` and of every field extension of `E` | **CONFIRMED** | `gcd(F,k)≠1`; displayed inverse failing; `-k/50=0` in `E`; a zero-divisor in the residue ring |
| 6 | `C=0` and `C=3` are precisely the two exceptional fibres of the named generic *transport* echelon (`C` multiplicity 2, `C-3` multiplicity 1, four nonconstant pivot events). Later first-stage exceptional roots of `4C^2+20C+1` are a different object. The theorem closes only these two raw fibres in one fixed normalized section | **CONFIRMED** | a third generic transport irreducible; promoting a line kill, an SP-2 kill, or JC2; printed `family_killed` / `SP2_killed` / `JC2_resolved` true |

All remarks below are non-blocking unless marked otherwise. None changes a rank, a remainder, a hash, or a verdict.

---

## Replay

Registered command, rerun unmodified from the charged tree:

```sh
/opt/homebrew/bin/python3 cases/td6_c1_raw_transport_fibres_20260824/replay.py 0 3
```

Exit code 0. Wall-clock `real 168.85`. `cmp` against `cases/td6_c1_raw_transport_fibres_20260824/replay.stdout` is silent. Printed scope, character-for-character against the freeze:

```text
"family_killed": false
"SP2_killed": false
"JC2_resolved": false
"previous_pole_or_current_parameterizations_used": false
"fixed_normalized_section_only": true
"all_requested_fibres_empty": true
```

This program is a regression. A second engine, written for this review and not imported from `replay.py`, then, for each of `C=0` and `C=3`:

1. set `CENTER=(C,1,1)` in the hash-pinned first-band compiler *before* building any matrix, with coefficients in `Q` (flint `fmpq`), not `Q(C)`;
2. rebuilt both global charts (`15×60` and `25×100`) from original rows and ran independent min-index sparse GE, recording every reduction factor;
3. propagated the adjoint source RHS over `E` and asserted every dependent transport row is `0`;
4. repeated min-index GE on the reversed row list (rank `3470` at both fibres);
5. restricted the six licensed `x`-bands to the 132-parameter affine chart, compiled `[s^{-2}]J` from the adjoint first-band identity, and ranked the packed 38 rows by min-index, max-index, and reverse-row GE;
6. compiled current `t^{12}` from the q2 two-form identity, independently of the producer’s single-degree specialization;
7. reduced that polynomial by the min-index first-band echelon (producer elimination order: increasing least-variable pivots) and, separately, by the max-index echelon (decreasing greatest-variable pivots);
8. lifted min-index quotients through the original 38 first-row combinations and replayed `P_{12}=-k/50+∑ M_i L_i` coefficient by coefficient.

Wall-clock `332.6` (`C=0`) and `372.0` (`C=3`). Every stated rank, both adaptive minors, both raw-polynomial digests, the reduced one-term digest, both original-row relation digests, and the unit remainder matched. A separate exact field engine, importing only the hash-pinned uniform-third presentation, independently reconstructed claim 5.

The specialized producer `rt.factor` still prints `TD6-C1-GENERIC-TRANSPORT: PASS`. That string is leftover naming. On both fibres it reports `max_rational_degree_span = 0` and `exceptional_irreducible_factor_count = 0`, i.e. constant rationals after specialization, not evaluation of the singular generic pivot list (whose denominators include `C`).

---

## 1. Adaptive transport rebuild

The first-band compiler expands `(C s + s^2 + s^3 + t s^4)^i` with the specialized rational `C` already substituted. The two charts contribute `976+2626=3602` columns and, after packing, `6507` rows. Independent flint GE with least-column pivots yields rank `3470` at both fibres, selected minors

```text
C=0:  +257966442530576208068773078615688721775504212455540300396334725797259347241775670913367306598807799716248037647462774182696432427807687902600418764541779814170203892671730914370249368230847958611216610490299068807485834098075214860578103412773386666008457935453315452652595400270807424192298640264198184013366699218750
C=3:  -85988814176858736022924359538562907258501404151846766798778241932419782413925223637789102199602599905416012549154258060898810809269229300866806254847259938056734630890576971456749789410282652870405536830099689602495278032691738286859367804257795555336152645151105150884198466756935808064099546754732728004455566406250
```

exactly the producer adaptive minors, with lifted digests `3349b4fb…e2477a` and `be8c3932…940036`. Reverse-row min-index GE again has rank `3470`. The 3037 dependent rows have vanishing E-valued residual. Free dimension is `3602-3470=132`.

The generic leftover selected-minor (product of generic leads after cancelling `C` in numerator and denominator) is the linear polynomial `A C + B` whose constant term is the `C=0` adaptive minor and whose leading coefficient is the `C=3` adaptive minor. Evaluating that leftover is *not* a rank certificate: two generic leads have denominator `C`, so the generic pivot *list* is singular at `C=0`. The adaptive rebuild does not use that list.

A greedy greatest-column GE of the same 3,602-column matrix fills in and was not used as a rank certificate. Over the field `Q`, the min-index echelon plus vanishing dependent rows already pins rank `3470`. The first-band pivot-choice attack is in claim 2, where the matrix is `38×132`.

Claim 1 stands.

---

## 2. Adaptive first band

The six `x`-bands of `f,g` in degrees `1,2,3` were restricted to the 132-parameter chart using the independent transport echelon, not a generic first-stage pivot list. The first-band identity is the adjoint formula

```text
[s^{-2} t^d] J  :  (q' * f_1)_d  -  15 (g_1)_{d-14}  =  0,
```

with `q'=1+25 t^{24}`. Packing keeps exactly 38 nonzero rows. Independent GE over `E`:

| strategy | rank | incompatibility |
|---|---|---|
| min-index (producer) | `38/132` | 0 |
| max-index | `38/132` | 0 |
| reverse-row min-index | `38/132` | 0 |

Every min-index pivot is the least variable of its normalized row; every max-index pivot is the greatest. That triangularity is the elimination order used in claim 4. Rank `38` on 38 packed rows means the first-band map is injective on its 38-dimensional image: there is no leftover first-band compatibility to hide a fibre.

Claim 2 stands.

---

## 3. Genuine current `t^{12}`

The current compiler is the q2 two-form identity for `[s^0 t^{12}](J-1)`, implemented independently from `compile_x_current` and run on the unreduced 132-parameter affine forms (no previous/pole substitution). Parameter degree is two at both fibres. Term counts and producer fingerprints of the independently computed polynomials:

| fibre | terms | degree | raw digest |
|---|---:|---:|---|
| `C=0` | 2824 | 2 | `be8e80ffa067a37b30418361812656405ef843a0fa5398766f12268dd1de55a1` |
| `C=3` | 2885 | 2 | `1bd39dc9756dd7e83c17ab04a0ccfd2655514a5a42f593eac80df88ce8a18275` |

Neither polynomial is parameter-free. The producer’s single-degree specialization of `compile_x_current` is therefore faithful at `t^{12}`.

Claim 3 stands.

---

## 4. Original-row identity

Multivariate division against a least-variable triangular basis is an elimination order only if pivots are taken in increasing index. A naive reverse sweep of the same basis reintroduces smaller pivots and is *not* a completed reduction; that is an implementation fact, not a second remainder. Against the producer increasing sweep the remainder is the one-term polynomial `-k/50` at both fibres. Against the *greatest-variable* first-band echelon, reduced largest-pivot-first, the remainder is the same constant. So the remainder is a property of the first-band ideal, not of one pivot convention.

Independently, `-k/50` serialized in the producer fingerprint is `233c0ce8f90585ed8da5085cd33f178f5c0e2300d87e4a44b4deeb9eb06644c7`, matching the freeze at both fibres. Numerator `(-126/25)+(171/25)S+(-72/25)S^2+(18/25)S^3` is exactly `-k/50`.

Quotients of the min-index division were lifted through the original-row combination vectors of the 38 packed first rows. The identity

```text
P_12 = -k/50 + sum_i M_i L_i
```

replays coefficient by coefficient on those original rows (not on the reduced echelon rows). Support:

| fibre | nonzero original rows | multiplier terms | relation digest |
|---|---:|---:|---|
| `C=0` | 28 | 1423 | `3c44f2dc21490bed6b402ea89a3653dade1fbd7f81c6cc4fa311a11bd31115e7` |
| `C=3` | 28 | 1515 | `617017b265be79efafbc155fa002f9e7597070e3e2623ade5fdd88deabca5581` |

The 28 nonzero rows are indices `0,…,27` of the packed 38; rows `28,…,37` have zero multipliers. That is allowed: those ten original rows are in the span used to triangularize, and the identity does not need them.

Claim 4 stands.

---

## 5. The constant is a unit

`F=24S^6-252S^5+1170S^4-3045S^3+4680S^2-4032S+1411` is the charged whole-`B` / uniform-third polynomial. Rabin modulo 31 (prime divisors of six are 2 and 3) gives `gcd(F, x^{31^2}-x)=1`, `gcd(F, x^{31^3}-x)=1`, and `x^{31^6}≡x`, so `F` is irreducible over `F_{31}` and over `Q`. Thus `K=Q[S]/(F)` is a degree-6 field.

Extended Euclidean algorithm of `k=252-342S+144S^2-36S^3` against `F` produces

```text
k^{-1} = -(388/175625) S^5 + (738/35125) S^4
         - (9181/105375) S^3 + (40993/210750) S^2
         - (4948/21075) S + (66812/526875),
```

and `k·k^{-1}=1` in `K`. This is `gcd(F,k)=1`, not a sample at one embedding.

`N_{K/Q}(α)=3^{28}/5^{96}` has 3-adic valuation 28, not divisible by 3, so `α` is not a cube in `K` and `T^3-α` is irreducible over `K`. Hence `E=K[A]/(A^3-α)` is a degree-18 field. There are no zero-divisors to hide a conjugate-specific vanishing of `-k/50`.

`-k/50` is nonzero in `E`; its inverse is `-50 k^{-1}`. After an arbitrary field extension `F⊃E` both remain nonzero, hence units of `F`. A point of the first-band affine space would kill every `L_i`, hence force `P_{12}=-k/50=0`, which is impossible.

Claim 5 stands. It reconfirms the whole-`B` unit of `k`; it does not reopen that pencil.

---

## 6. Exceptional fibres and refusal boundary

The named generic transport factorization (identical `c1_rational_transport.py`, run over `Q(C)` in the first-stage package) reports

```text
exceptional_irreducible_factor_count = 2
pivot_factor = (x); aggregate_multiplicity=2
pivot_factor = (x + (-3)); aggregate_multiplicity=1
nonconstant_pivot_event_count = 4
```

The four events are `F0` leads `-2C`, `(5/2)(C-3)/C` on the `f` chart and `-2C`, `-5/C` on the `g` chart. Vanishing numerators: two at `C=0`, one at `C=3`. Vanishing denominators: two at `C=0`, none at `C=3`. No other irreducible appears. That is why these two fibres, and only these two, are the generic *transport* exceptions.

The successor names a later first-stage cubic `4C^3+8C^2-59C-3`. Independently, that cubic factors as `(C-3)(4C^2+20C+1)`. The leftover quadratic has discriminant `384` and neither root is `0` or `3`. `C=0` is not a root of the cubic. `C=3` is already excluded by the transport chart; the new first-stage roots are not closed here. This review does not independently recompute that cubic from a generic first-band GE; it only distinguishes it from the transport divisor `C(C-3)`.

Printed flags `family_killed=false`, `SP2_killed=false`, `JC2_resolved=false` match the gate’s refusal boundary. SP-2 remains the ledger at `SHEET6-LROOT.md:187–200`. Exact `J=1` is not proved or disproved.

Claim 6 stands.

---

## Non-blocking remarks

1. The launch prompt’s canonical-stdout SHA-256 is a transcription error (`b48210ae90100151…` vs freeze `b48210ae9c97d358…`). The freeze, the MANIFEST line, and the registered replay agree. Not a mathematical gap.
2. `rt.factor` prints `TD6-C1-GENERIC-TRANSPORT: PASS` on the specialized fibres. Harmless leftover naming; the specialized runs have constant leads.
3. A reduced-row certificate against the 38-pivot echelon would have been insufficient. The freeze emits original-row multipliers, and the independent engine replayed those.
4. Greatest-column GE of the 3,602-column transport matrix fills in and was not used. Transport rank is pinned by the min-index echelon over `Q` plus vanishing dependent rows; first-band rank and the `t^{12}` remainder were attacked with a second pivot convention.

---

— Grok 4.6, hostile different-model reviewer, 2026-08-24T20:57Z
