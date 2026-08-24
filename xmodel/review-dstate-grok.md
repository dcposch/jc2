# Hostile review: `D-STATE-GATE`

| Field | Value |
|---|---|
| Claim | `NO-TYPED-STATIONARITY` (pure-`y` six-band window through 40, then a full-source typing stop) |
| Verdict | **CONFIRMED** |
| Smallest failing witness | none |
| Evidence tier | unreduced source at two named modular D25 witnesses; exact `Q`-coefficient identity at `t^{42}`; not an Ore/Spencer/Fitting object, inverse limit, germ, or characteristic-zero theorem |
| Reviewer | Grok 4.6 (adversarial different-model verifier) |
| CLI | `grok 1.0.5 (5115b46bc909) [stable]` |
| Python | 3.14.6 (`/opt/homebrew/opt/python@3.14/bin/python3.14`) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |
| UTC | 2026-08-24T03:24:01Z |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `8bf25a52f5f6c20886b77c6d9aeeb879eb18f8e4` |
| Scratch | `/tmp/dstate-grok-hUwGz5` (fresh `mktemp -d`) |

**Promotion.** The split record may be promoted off producer-checked provisional:

1. **Positive pure-`y` statement.** At the two previously reviewed modular D25 witnesses, the unreduced 30-input / 30-output pure-`y` source through band 40 has the registered six-band ladders, keeps `H_{29}` with start 36, has exact shifted `10 x 10` first-occurrence layers at 26/32/38, has coefficientwise commuting truncation squares, and satisfies `M_{38}-2M_{32}+M_{26}=0`.
2. **Negative typing stop.** The first omitted full-source interface is the displayed row-42 identity in `α_1,β_1`. Both partials are nonzero over `Q` and at both registered primes, and the current constructor does not type those coordinates as held, derived, or independent. The honest verdict is `NO-TYPED-STATIONARITY`.

Nothing else may be promoted.

**Quarantine if this review is treated as a failure.** Do not feed this record into an Ore/Spencer/Fitting object, a first syzygy obstruction, an all-depth stationarity theorem, a band-28 solve, a D43 point, a compatible inverse system, a formal germ, a characteristic-zero lift, algebraization, a polynomial Keller map, or a JC2 inference. Do not upgrade the stop to `STATIONARY-SOURCE-SIGNAL`, `SOURCE-MISMATCH`, or `UNBOUNDED-STATE`. Do not treat `U_g^2=U_f^3` as a licence to set `3α_1-2β_1=0`.

**Dirty-state perimeter.** HEAD matches the preregistered basis `8bf25a52f5f6c20886b77c6d9aeeb879eb18f8e4`. Tracked dirt is `APPROACHES.md`, `AUDIT.md`, `COORDINATION.md`, `PROGRESS.md`, and `pilot-local.log`; none is an input of this gate. The case directory and producer report are untracked post-basis artifacts, as are the hashed round-1 / ideation sources. Those frozen inputs were rehashed here and match `provenance.json` byte-for-byte.

Reviewer discipline: producer and replay implementations read in full before execution; scratch output only under `/tmp/dstate-grok-hUwGz5`; no network; no solver or remote/AWS job; no shared-ledger edit; no repository write except this file. Stored booleans, matrix hashes, and the producer `verdict` string are not authority. Verdicts rest on formula-derived registries, rebuilt dual jets, an independent `Q[η]` / bivariate `(t,η)` coefficient calculation, and an independent first-occurrence / finite-difference / Ore extraction.

---

## Claim under review (not enlarged)

1. Preregistration precedes execution, the frozen verdict taxonomy is the one applied, provenance hashes and the case manifest match disk, and the exact replay commands regenerate the banked JSON byte-for-byte.
2. The corrected 30-input / 30-output pure-`y` state, six-band starts, `H_{29}`, first-occurrence layers 26/32/38, coefficientwise projection squares, and `M_{38}-2M_{32}+M_{26}=0` hold at both registered primes on the banked D25 witnesses.
3. Dual-jet versus four-term written product-rule derivatives agree through band 40; a representative matrix relation is recomputed rather than accepted as a stored hash.
4. Independently,
   \[
   [t^{42}]\mathcal E_{\mathrm{full}}
   =[t^{42}]\mathcal E_y
   +42 S_M G_M(3\alpha_1-2\beta_1)p(\eta)^4 p'(\eta),
   \]
   and both partials are nonzero over `Q` and at `p=105337,105673`.
5. `α_1,β_1` are not typed as held, derived with a chain rule, or independent source coordinates in the current constructor/state labels. The claimed absence is not a search or naming failure.
6. No band-28 solve, D43, all-depth stationarity, Ore/Spencer/Fitting construction, germ, characteristic-zero, or JC2 inference is consumed or emitted.

---

## Verdict table

| Clause | Verdict | What would have flipped it |
|---|---|---|
| Preregistration chronology, frozen taxonomy, provenance/manifest hashes, byte-replay | **CONFIRMED** | results before prereg; `UNBOUNDED-STATE` silently dropped as the live verdict; hash mismatch; scratch JSON differs |
| 30/30 six-band state, starts 288/276, `H_{29}` at 36, layers 26/32/38, projection squares, Ore second difference 0 at both primes | **CONFIRMED** | ladder not six-step; `H_{29}` omitted; first-occurrence ≠ declared 10; lower-row change; `M_{38}-2M_{32}+M_{26}≠0` |
| Two derivative groupings independent enough; representative relation recomputed | **CONFIRMED** | dual ≠ grouped through 40; second difference only a hash of the zero matrix with no rebuilt entries; replay imports producer routines |
| Row-42 identity and nonzero partials over `Q` and at both primes | **CONFIRMED** | leading row-0 identity fails; factored ≠ four-term ≠ bivariate perturbation; a partial vanishes at a registered prime |
| `α_1,β_1` untyped in the current source; absence is not a naming miss | **CONFIRMED** | `build_jets` grows an x-side argument; a 30-stream or `fixed` key *is* `α/β` with a banked shift map; a sourced chain rule is already in the registered constructor |
| Scope: no band 28 / D43 / all-depth / Ore-Spencer-Fitting object / germ / char-0 / JC2 | **HONEST** | `d43*` import; band-28 sample; promotion past the typing stop |

---

## What was rerun, independently, and not

```bash
SCRATCH=$(mktemp -d /tmp/dstate-grok-XXXXXX)
# SCRATCH=/tmp/dstate-grok-hUwGz5

/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round2_dstate_gate/dstate_gate.py \
  --output "$SCRATCH/results.json"
# VERDICT: NO-TYPED-STATIONARITY

/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round2_dstate_gate/replay.py \
  --input cases/round2_dstate_gate/results.json \
  --output "$SCRATCH/replay.json"
# review_verdict: PASS
```

Scratch producer JSON is **byte-identical** to `cases/round2_dstate_gate/results.json` (`cmp` silent; SHA-256 `4ca07ad9c922acec962b508e857d69c5db7ae336c3f0723837e2a0799d6f225f`). Scratch replay JSON is **byte-identical** to `cases/round2_dstate_gate/replay.json` (`cmp` silent; SHA-256 `7a0e534563085950a90fd0a54da9f63f541713d212bf412485ee7c4ab365f72c`). Not stale.

Independent work, **not** `dstate_gate.audit_banked_prime` / `xside_interface` and **not** stored `ore_second_difference_zero` / `two_derivations_agree` / `verdict` strings as authority:

- Rehashed all 8 `MANIFEST.sha256` paths and all 9 `provenance.json` sources against disk: **0 mismatches**. Recomputed producer `core_sha256` and replay `core_sha256` from the JSON objects; both match.
- Re-derived the 30 input starts from `r_ρ=6+ρ` (`r_4=16`) and the 30 output starts from `s_a=6+2*((a+1) mod 3)` (`s_{28}=16`, `s_{29}=36`). Sums 288 and 276. Residue-0 output count is 9 at band 30 and 10 at band 36, with `a=29` entering at 36.
- Rebuilt both witnesses from `transition_symbol.d25_sample` + `valuation_e2.build_jets` / `euler_rows`. Extracted the three `10 x 10` layers from the dual jet. Recomputed first-occurrence censuses, combined-unit projection squares at **all three** bands, dual-versus-grouped derivatives through band 40, and the Ore second difference as an actual matrix, not a hash.
- Independently derived the row-42 identity from the product rule (below). Recomputed `p^4 p'` over `Q`, the four unreduced Euler terms, and a separate bivariate `(t,η)` perturbation of `F_0` and `G_0`. All three paths agree with the banked rationals and with the stored modular reductions.
- Inspected `build_jets` signature, `GIDX` / `STREAMS` / `fixed` keys, `DBUILD=42`, and the out-of-scope D43 engine `cases/eplus43.py`.

Not done, and not required by the scoped claim:

- No second transcription of the cyclic-orbit algebra from a paper source. Shared-source mistranscription of `aside_orbit_jet` remains a possible gap of a different kind; it is not live in the two-prime arithmetic or the coefficient identity.
- Band 28 was not emitted, solved, or sampled.
- No D43 point, no `eplus43` run, no syzygy/Spencer/Fitting construction.

---

## Hashes

| object | SHA-256 |
|---|---|
| `cases/round2_dstate_gate/PREREGISTRATION.md` | `e34d1b090dcf4447bc735f9b289e445a87b1168eeb5a70678f0f8d03348b98ab` |
| `cases/round2_dstate_gate/provenance.json` | `7cb56a470ffa437f7afda684f07ebeb71a4d2a85ad80068670ffb673e535dbdc` |
| `cases/round2_dstate_gate/dstate_gate.py` | `d312c84bfe601e667c74b2453ef09287d5b2dd9796e4201d57b6b364debae309` |
| `cases/round2_dstate_gate/results.json` (banked and scratch rerun) | `4ca07ad9c922acec962b508e857d69c5db7ae336c3f0723837e2a0799d6f225f` |
| `cases/round2_dstate_gate/replay.py` | `770fc71405d2d5c819508451c454af7f59a25c46867934af9e302603e15f232a` |
| `cases/round2_dstate_gate/replay.json` (banked and scratch rerun) | `7a0e534563085950a90fd0a54da9f63f541713d212bf412485ee7c4ab365f72c` |
| `cases/round2_dstate_gate/verify.py` | `829ef2d35d74babb7bbedca02c9bcf368ca21bc0d5f22d28159a4b0d9a7fbbc2` |
| `xmodel/round2-dstate-gate-20260824.md` | `57536d0557d4aaaf267ce493c3236b33eed1c1d2829484e496211934ea78d512` |
| producer `core_sha256` | `fa2e2ec2323306b8aa461b0ce7e850b4fe05f0c91d0ea08666d509c317aa8ef0` |
| independent `core_sha256` | `a43d99621955796dc35dd570904fbfe5bf70d39406d4fd9cc479a18fd11841dc` |
| `p=105337` completed point | `c74f220e2cc5badfb3418421825571165aa84af3a18abd585fdd1dbd59fbea02` |
| `p=105673` completed point | `efe0d125541a652c546444dcbac80accf8982962e8198e93812b8754f2b6b26c` |
| independent `α`-partial encoding | `e6774fb02a5e6e1d41f9094fc65734e8cdaba260651f113dc30e5a845039b574` |
| independent `β`-partial encoding | `c9823d59c2129c810fabf3e09ec49311f2aac8f42e5baf4cf91845a11778fef0` |
| `10 x 10` zero matrix (Ore remainder) | `fe7689ecc8886006b1c043a8bf0792e47340dc54cb95e883ad8d32b709ede915` |

Provenance sources, all matching disk:

| source | SHA-256 |
|---|---|
| `cases/eplus_certify.py` | `e453abb417f8b5d6b0afd8d438e2f98e3d48ca6d7b94a90178cc8ceb1093bfe4` |
| `cases/r1_experiment.py` | `1214f58eac807128eb7d6edb32726e8cf0923241e7340cbe78bdd5c0aca5d7c1` |
| `cases/round1_dtransition/transition_symbol.py` | `869ff70bf04a991fe2e98e420951b26b94041ef01c91bec087d92b83f3fbe91d` |
| `cases/valuation_e2.py` | `c1a858fbe53c291038b0386c124dbfd4bc79400eedc6b9d5d49a4088736d08f8` |
| `xmodel/ideation-20260824T0156Z-synthesis.md` | `9c0455ddae2388d7f5256ec46094c0d97dd5bc6748f2b61177f736cc23581f50` |
| `xmodel/review-dtransition-grok.md` | `617c29cffa9e321ab5e5027543d2f6ee800e2ac94eab3ecb37f0ab494aefed74` |
| `xmodel/round1-dtransition-fullcell-20260824.md` | `2b25b3ac5591360f2bac2f1c74f1c97bb936f1826f6aaed3d2969ad37be1f5df` |
| `xmodel/sol-newton-lemma.md` | `30ca1b8e6e2d7443278430a4f80dfdbc520303100b2a91783dcdeb55bbf55be8` |
| `xmodel/sol-xside-spec.md` | `f946a4ae65965200d5138b6a213945f1a3be6076fa8da1bfac9d4ba24381d9ff` |

Completed-point hashes are the same two witnesses already confirmed in `cases/round1_dtransition/samples.json` and the full-cell review. Tool hashes match the producer report.

---

## 1. Preregistration, taxonomy, provenance, replay

Claimed freeze: `2026-08-24T02:59:31Z`, before executing the gate. File mtimes (UTC) are consistent with that claim and with the written commands:

| mtime (UTC) | path |
|---|---|
| 03:00:12 | `PREREGISTRATION.md`, `provenance.json` |
| 03:03:20 | `dstate_gate.py` |
| 03:03:36 | `results.json` |
| 03:05:22 | `replay.py` |
| 03:05:38 | `replay.json` |
| 03:06:56 | `xmodel/round2-dstate-gate-20260824.md` |
| 03:07:11 | `verify.py` |
| 03:07:25 | `MANIFEST.sha256` |

The 41-second gap between the frozen timestamp and the preregistration mtime is the write of the frozen text, not a post-hoc backdate of a result. Results, replay, report, and manifest all come after the freeze file.

Frozen verdicts, in the required order: `SOURCE-MISMATCH`, `UNBOUNDED-STATE`, `STATIONARY-SOURCE-SIGNAL`, `NO-TYPED-STATIONARITY`. The producer code raises only `SOURCE-MISMATCH` as an exception; if the finite checks pass it then branches on whether a typed shift/projection map and an `α,β` classification are present. Those two fields are fail-closed (`None` / `False`) after a constructor-signature and label inventory. `UNBOUNDED-STATE` is never emitted. That is a completeness hole in the driver, not a live misclassification: the omitted x-side is a finite list of factor coordinates (`α_1..α_{42}`, `β_1..β_{63}`), so the unreduced derivation does not prove unbounded new types.

`replay.py` does not import `dstate_gate.py`. Both implementations import the registered source `valuation_e2` and the reviewed D25 sampler `transition_symbol`. That is the correct object: the claim is about this constructor, not about a second cyclic-product transcription. The independent reviewer's matrix extraction, Ore arithmetic, first-occurrence census, finite differences, and coefficient engines do not call producer audit routines.

---

## 2. Corrected 30-state, layers, squares, Ore identity

Registries from the written formulas, not from stored matrices:

- inputs: residues `0..5` on `tf1,tf2,tg1,tg2` and `0,2,4` on `tg01,tg02`;
- `r_ρ=6+ρ` except `r_4=16` (`PIN42` excludes `r=10`);
- 30 disjoint six-step ladders, partitioning the 170 `GIDX` coordinates;
- outputs `s_a=6+2*((a+1) mod 3)` for `a≤28`, `s_{28}=16`, `s_{29}=36`.

`sum r = 288`, `sum s = 276`. `valuation_e2.STREAMS` / `S_A` / `S_29` match. The stale `valuation_e2` docstring still talks about a 29-row lemma with `E_{29}=0`; the live constants used by the gate are the corrected 30-row object. That docstring is not an input.

Layer type from the same start table, residue class `n ≡ 2 (mod 6)`:

```text
rows at 26, 32, 38:  a = 0,3,6,9,12,15,18,21,24,27
coords at n:         ordinary r = n-5; all six families at r = n
band 26 names:       tf1_53 tf2_53 tg1_53 tg2_53
                     tf1_58 tf2_58 tg1_58 tg2_58 tg01_58 tg02_58
```

Bands 32 and 38 are the same list with every displayed absolute level increased by 6 and 12. They were not solved.

`H_{29}`: residue-0 rows are 9 at band 30 and 10 at band 36. On both rebuilt witnesses the only `a=29` support is band 36. This is the registered transient, not evidence against the corrected state.

Both witnesses: frontier completion **not** applied; `PIN42` slot empty; new layer coordinates unassigned; `fixed` keys are chart/radical/B-side (`A1,A2,W1,W2,HW1,HW2,uf18,uf24,uf30,vf*_34,vf*_36,r3,h32`). After reconstruction `sys.modules` contains no `d43*` / `nffid` / `fullcell` module.

At each prime, independently extracted from the rebuilt dual jet:

| prime | V through 40 | G through 40 | dual = grouped | layers 26/32/38 first-occurrence | squares | `M38-2M32+M26` |
|---:|---|---|---|---|---|---|
| 105337 | `c5803c10…a294e7` | `1ca95b04…31b3a0` | yes through 40 | exact `10 x 10`, no lower-column support, no outside row | lower unchanged; FD = derivative at 26, 32, and 38 | zero matrix |
| 105673 | `196d1d7f…e37088` | `3b8d249c…bdc6ee0` | yes through 40 | same | same | zero matrix |

Those hashes match the banked JSON. Combined unit perturbation of a new layer is the finite-difference form of the commuting square: forgetting the layer cannot change a lower source row, and at the first band the difference equals the source derivative. Per-column first-occurrence already shows each new column is zero below its band.

Ore identity, recomputed as matrices, not as a stored boolean. The three matrices are **not** equal (`M26≠M32≠M38`). Of 100 entries at `p=105337`, 90 have a genuine common first difference and 10 are constant (affine with slope 0). All 100 satisfy the second difference 0. Representative changing slot, output row `a=3`, column `tf1` at `r=n-5`:

```text
M26[1,0] = 93239
M32[1,0] = 53061
M38[1,0] = 12883
common difference = 65159 (mod 105337)
12883 - 2*53061 + 93239 ≡ 0
```

This is the expected Euler/Ore scalar law `θ(t^r Z(u))=t^r(r+6Θ)Z(u)` sampled at three simultaneous six-shifts, at two modular points. It is not a polynomial identity of an Ore module, and it does not construct a Spencer or Fitting object.

`jmul` is `float64`. Rechecked: `34·42·p^2 < 2^{53}` at both primes (`1.584e13` and `1.595e13` versus `9.007e15`).

---

## 3. Two derivative implementations

**Pure-`y` window.** `euler_rows` multiplies full dual jets `(θ-12)Φ` and `Γ_η`, then subtracts `Φ_η(θ-18)Γ`. `path_A_rows` splits each factor into a value-only jet and a gradient-only jet and assembles the four Leibniz terms by hand. They share `jmul`, `theta_shift`, and `eta_deriv`, so they are two groupings of one constructor, not two cyclic-product codes. That is independent enough for the claim that was made: the dual source derivative equals a separately grouped differentiation of the written Euler rule. Independently confirmed: the two gradient arrays agree through band 40 at both rebuilt witnesses. Finite-difference rebuilds at 26/32/38 are a third path for the projection square; replay only checked band 38, the reviewer checked all three.

**Row-42 interface.** Producer "Derivation I" inserts the boxed formula and evaluates `42 S_M G_M p^4 p'` times `3` and `-2`. Producer "Derivation II" evaluates the four unreduced Euler terms at `t^{42}` before using the `p`-power identities. Those are the two algebraic rearrangements already written as (3.5) and (3.6) in `sol-xside-spec.md`, computed in one univariate `η`-polynomial engine. That is weak as "two implementations". The replay engine is actually different: sparse bivariate `(t,η)` maps, `θ` by multiplying the `t`-exponent, `∂_η` by the `η`-exponent, and a unit `t^{42}` copy of `F_0` or `G_0`. The reviewer used a third copy of that bivariate engine plus an independent four-term expansion. All three agree. The coefficient claim does not rest on a stored hash.

---

## 4. Independent derivation of the row-42 formula

Source:

\[
\mathcal B(Φ,Γ)=(θΦ-12Φ)Γ_η-Φ_η(θΓ-18Γ),\qquad
\mathcal E=\mathcal B+42 t^{20}.
\]

Full factors, `η`-independent:

\[
Φ_{\mathrm{full}}=U_f Φ_y,\qquad Γ_{\mathrm{full}}=U_g Γ_y,
\]

\[
U_f=1+α_1 t^{42}+O(t^{84}),\qquad
U_g=1+β_1 t^{42}+O(t^{84}).
\]

Product rule, using `∂_η U_f=∂_η U_g=0`:

\[
θ(U_f Φ_y)=(θ U_f)Φ_y+U_f θΦ_y,
\]

and likewise for `Γ`. Expanding and regrouping gives exactly

\[
\mathcal B(U_f Φ_y, U_g Γ_y)
=U_f U_g\mathcal B(Φ_y,Γ_y)
+U_g(θ U_f)Φ_y Γ_{y,η}
-U_f(θ U_g)Φ_{y,η}Γ_y.
\]

The inhomogeneous `42 t^{20}` is added after this identity; it is not multiplied by `U_f U_g`, and it does not meet `t^{42}`.

Leading jets, banked and re-used here as coefficient algebra, not as a D43 sample:

\[
F_0=S_M p^2,\qquad G_0=G_M p^3,\qquad
S_M=7^{12}/2^6,\qquad G_M=-7^{18}/2^9,
\]

\[
p(η)=η^6-6η^3+6.
\]

`F_0,G_0` are `t`-independent, so `θ F_0=θ G_0=0` and

\[
\mathcal B(F_0,G_0)=-12 F_0 G_0'+18 G_0 F_0'
=-36 S_M G_M p^4 p'+36 S_M G_M p^4 p'=0.
\]

Independently verified: this polynomial is the zero list. Also `G_M^2=S_M^3`. Extracting `[t^{42}]` from the product identity, using row 0, and `θ(t^{42})=42 t^{42}` yields

\[
[t^{42}]\mathcal B_{\mathrm{full}}
=[t^{42}]\mathcal B_y
+42α_1 F_0 G_0'
-42β_1 F_0' G_0
=[t^{42}]\mathcal B_y
+42 S_M G_M(3α_1-2β_1)p^4 p'.
\]

The same correction is `[t^{42}]\mathcal E`. Before using row 0 the two Euler corrections are `α(30 F_0 G_0'+18 G_0 F_0')` and `β(-12 F_0 G_0'-24 G_0 F_0')`. Substituting the `p`-powers recovers `126 S_M G_M p^4 p'` and `-84 S_M G_M p^4 p'`.

Independent `Q[η]` evaluation:

- `p^4 p'` nonzero support is exactly the spec table
  `η^{2,5,8,11,14,17,20,23,26,29}` with
  `(-23328, 101088, -186624, 191808, -120528, 47952, -12096, 1872, -162, 6)`;
- factored formula = four-term Euler = bivariate perturbation;
- `2·(α`-partial`)+3·(β`-partial`)=0` identically (window-proportionality, not a quotient licence);
- both partials nonzero over `Q`;
- `2,3,7,42` are units at both registered primes, so `S_M,G_M` and the leading `6η^{29}` survive; every stored modular coefficient matches the independent reduction of the rationals.

Bivariate perturbation is the honest second implementation: add one `t^{42}` copy of `F_0` (resp. `G_0`), run `B`, subtract the baseline. It does not assume the boxed formula.

---

## 5. Typing of `α_1,β_1`: not a search miss

Current constructor, inspected rather than grepped once:

- `build_jets(point, p, Z)` only. `point` top-fields: `tails`, `fixed`, `zc_hash`.
- `DBUILD=42` means slots `0..41`. The pure-`y` window is exact below `t^{42}` by truncation. The constructor cannot represent the first x-side term.
- `STREAMS` / `GIDX`: six families `tf1,tf2,tg1,tg2,tg01,tg02`, 170 y-tail coordinates, no `alpha`/`beta`/`U_*` family.
- `fixed` keys at both witnesses: chart/radical/B-prefix, not polynomial factor coefficients.
- `orbit_levels` / `through_block` / `other_block` / `b_block` multiply cyclic y-orbits and a frozen B-orbit. They do not multiply `U_f` or `U_g`.

`α_1 t^{42} F_0` is a multiple of the leading `η`-polynomial `p^2`. A residue-0 y-tail coefficient at global level 42 is a different `η`-shape already inside `[t^{42}]\mathcal E_y`. The extra term is not secretly one of the 30 streams.

`sol-xside-spec.md` states the three-way classification as mandatory and then **leaves it as conjecture**. `CONJECTURE X-SIDE-DERIVATION` is undischarged; `CONJECTURE X-SIDE-30` is the statement that the x-side adds no independent 30-state direction, not a proof that it doesn't. No numerical value of `α,β` is assigned. `CONJECTURE X-CUBE-RELATION` (`U_g^2=U_f^3 ⇒ 2β=3α`) would cancel the first correction; it is explicitly unproved and must not be consumed.

Adversarial extra hit: `cases/eplus43.py` **declares** `α,β` independent filtered tangents, uses completion values `α=β=0`, and builds a D43 window `184 x 182`. That is a fail-closed D43 engine, out of the frozen perimeter, and the declaration is exactly the undischarged case-3 choice the spec forbids treating as sourced. Importing it here would invent the state map and violate the D43 ban. The producer search (signature + family-name) was thin; the deeper search does not change the stop.

Hence `α_1,β_1` are not held, not derived with a banked chain rule, and not independent coordinates of the registered 30-state. They are an untyped full-source interface. `NO-TYPED-STATIONARITY` is the first applicable frozen verdict.

---

## 6. Scope discipline

Runtime grep of `dstate_gate.py`, `replay.py`, `transition_symbol.py`, `valuation_e2.py`: no `d43` / `nffid` import; D43 appears only in perimeter comments. After reconstruction, no such module is loaded. `BANKED_SHIFT_BANDS=(26,32,38)`; band 28 is never assembled. Row 42 is a universal coefficient identity, not a specialized D43 point. The Ore second difference is a three-sample modular observation, not an Ore/Spencer/Fitting construction. No germ, characteristic-zero, or JC2 sentence is emitted.

---

## What may enter `AUDIT.md`

**May enter**, as a split source-typing record, not as a stationarity theorem:

- At the two named modular D25 witnesses already confirmed for the one-band `X27→X25` signal (`p=105337` and `p=105673`, fiber `a00pp`), the unreduced pure-`y` Euler product through band 40 matches the corrected 30-by-30 six-band registry of `sol-newton-lemma.md`: 30 disjoint six-step input ladders with `PIN42`, output starts summing to 276, and `H_{29}` first at band 36.
- First-occurrence layers at 26, 32, and 38 are the exact shifted ten-row / ten-coordinate type. Combined unit perturbations of each new layer leave every lower source row unchanged and equal the source derivative at the first band.
- Dual-jet and four-term written product-rule derivatives agree through band 40.
- After simultaneous input/output relabeling by six, the three relative matrices satisfy `M_{38}-2M_{32}+M_{26}=0` at both primes. This is a modular Euler/Ore affine check on those three layers, not an Ore module.
- Independently derived and thrice-evaluated:
  `[t^{42}]\mathcal E_{\mathrm{full}}=[t^{42}]\mathcal E_y+42 S_M G_M(3α_1-2β_1)p(η)^4 p'(η)`.
  Both partials are nonzero over `Q` and at both registered primes.
- The current `build_jets` constructor has no x-side argument, the 30 registered streams do not contain `α_1,β_1`, and no sourced held/derived/independent classification or six-shift projection map is banked. Verdict: `NO-TYPED-STATIONARITY`.

**Must not enter:** `STATIONARY-SOURCE-SIGNAL`; a finite full-source state; an Ore/Spencer/Fitting or syzygy object; all-depth closure; band-28 persistence; D43 membership or rank; a germ or characteristic-zero point; `U_g^2=U_f^3`; JC2.

---

## Caveats

- Dual versus grouped derivatives share `jmul`. Independence is grouping-plus-finite-difference, not a second orbit algebra.
- Producer Derivation I/II are two rearrangements of `sol-xside-spec.md` (3.5)–(3.6) in one univariate engine. The independent bivariate perturbation is the second implementation that actually matters.
- Three sampled bands make the second difference a test of affinity on those bands, not a polynomial identity.
- `float64` dual jets, exactness bound checked, not `Q`-arithmetic for the modular matrices.
- `UNBOUNDED-STATE` is in the frozen taxonomy but not in the driver. It is not the live verdict.
- `valuation_e2` still documents a refuted 29-row lemma in its header; live constants are the corrected 30-row object.
- `eplus43.py` exists and must not be read as a sourced classification.

---

## Adversarial attack log

| # | Attack | Result |
|---:|---|---|
| 1 | Results predate preregistration | Fail. mtimes: freeze files 03:00:12, results 03:03:36 |
| 2 | Manifest / provenance hash mismatch | Fail. 8+9 paths, 0 mismatches |
| 3 | Scratch rerun differs from banked JSON | Fail. `cmp` silent both ways |
| 4 | Trust stored `ore_second_difference_zero` | Fail. Rebuilt matrices; 90/100 entries have nonzero common difference; second difference 0 |
| 5 | Degenerate Ore: all three matrices equal | Fail. `M26≠M32≠M38`; remainder hash is the zero matrix because the remainder *is* zero |
| 6 | Dual ≠ grouped through 40 | Fail. Arrays equal at both primes |
| 7 | Replay imports producer engine | Fail. No `import dstate_gate` |
| 8 | Boxed formula is only a stored string | Fail. Derived from the product rule; four-term and bivariate paths agree |
| 9 | A partial vanishes at a registered prime | Fail. Independent modular reductions are nonzero; `2,3,7,42` are units |
| 10 | `α,β` hide under another name in `GIDX` or `fixed` | Fail. Six families, 170 y-columns, chart/B keys only |
| 11 | `α_1` is the `u^6` coefficient of a start-6 residue-0 stream | Fail. That term is already in `[t^{42}]E_y`; the extra term is `p^4 p'` times the leading jet |
| 12 | `eplus43.py` already types them independent | Out of scope. D43 engine, undischarged case-3 declaration, `α=β=0` completion, not a source proof |
| 13 | Consume `U_g^2=U_f^3` and cancel `3α-2β` | Forbidden. `CONJECTURE X-CUBE-RELATION` is unproved |
| 14 | `H_{29}` silently dropped | Fail. Start 36, support `{36}` on both witnesses, ten residue-0 rows at 36 |
| 15 | D43 / `nffid` / full-cell import | Fail. No such module after reconstruction; full-cell report is hashed provenance, not imported |
| 16 | Band-28 sample hidden in the three layers | Fail. Layers are 26/32/38 only |
| 17 | `STATIONARY-SOURCE-SIGNAL` is unreachable only because of hardcoded `False` | The hardcoded stop is the required fail-closed inventory; deeper search finds no map to flip it legally |
| 18 | Promote the Ore check to a Spencer/Fitting object | Scope violation; not done |
| 19 | `float64` overflow at band 40 | Fail. `34·42·p^2 < 2^{53}` |
| 20 | Same Ore remainder hash at both primes hides a bug | Fail. Both remainders are the zero `10 x 10`; the hash is independently that of `[[0]*10]*10` |

No live hit. Smallest failing identity: none. Blast radius if this review is misread as a full-source stationarity theorem: any later Ore/Spencer, band-28, D43, germ, or JC2 claim that treats the 30-state as closed.

---

## Commands actually run

```text
/opt/homebrew/opt/python@3.14/bin/python3.14 -  # independent Q[η] / bivariate coefficient engine
/opt/homebrew/opt/python@3.14/bin/python3.14 -  # independent modular rebuild, both primes, three squares
/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round2_dstate_gate/dstate_gate.py \
  --output /tmp/dstate-grok-hUwGz5/results.json
/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round2_dstate_gate/replay.py \
  --input cases/round2_dstate_gate/results.json \
  --output /tmp/dstate-grok-hUwGz5/replay.json
/opt/homebrew/opt/python@3.14/bin/python3.14 -  # changing Ore entries at p=105337
```

Network: not used. Solver / AWS: not used. Repository writes other than this file: none.
