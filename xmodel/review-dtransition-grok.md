# Hostile review: `FREE-TAIL-SIGNAL`

| Field | Value |
|---|---|
| Claim | `FREE-TAIL-SIGNAL` (one-band modular `X27 -> X25` signal only) |
| Verdict | **CONFIRMED** |
| Smallest failing witness | none |
| Evidence tier | mod `p` at four named `a00pp` points, one chart, one band; independent source replay + modular linear algebra; not a component / inverse-limit / char-0 object |
| Reviewer | Grok 4.6 (adversarial different-model verifier) |
| CLI | `grok 1.0.5 (5115b46bc909) [stable]` |
| Python | 3.14.6 (`/opt/homebrew/opt/python@3.14/bin/python3.14`) |
| Host | Darwin arm64 |
| UTC | 2026-08-24T01:48:46Z |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `8bf25a52f5f6c20886b77c6d9aeeb879eb18f8e4` |
| Scratch | `/tmp/dtransition-grok-XuuBQC` (fresh `mktemp -d`) |

**Promotion.** The four-point one-band modular signal may be promoted off producer-checked provisional. Nothing else may. In particular the six kernel directions are exact affine lifts of the unreduced recurrence *through band 26 only*.

**Quarantine if this review is treated as a failure.** Do not feed `FREE-TAIL-SIGNAL` into a component dimension, a locus-wide rank statement, dominance of `pi_27_25`, a band-28 persistence claim, a compatible inverse system, a formal germ, or a characteristic-zero point. Do not launch the proposed full-cell compatibility child from this review.

---

## Claim under review (not enlarged)

1. The unreduced source recurrence defines a typed projection `X27 -> X25` in the residue-A, B-frozen, no-log, `PIN42`, `W1*W2 != 0`, fiber `a00pp` chart, adding exactly ten band-26 rows and ten first-occurrence coordinates and changing no lower row.
2. The implementation has no dependency on D43 or `D43-NF-FID`, and the four sampled points satisfy the cited D25/source gates.
3. At each registered prime, the witness block has `rank(A)=rank([A|b])=4`, right- and left-kernel dimensions six, and all six displayed affine kernel lifts replay in the unreduced recurrence.
4. At each registered prime, the deterministic interior sample has `rank(A)=4`, `rank([A|b])=5`, hence is outside the one-band projection image.
5. These pointwise results justify only the scoped verdict: compatible six-dimensional one-band fibers exist over the two witnesses while other D25 points are cut by compatibility. They do not prove a component, dominance, persistence, inverse-limit survival, a formal germ, or a characteristic-zero object.

---

## Verdict table

| Clause | Verdict | What would have flipped it |
|---|---|---|
| Typed `X27 -> X25`: 10 band-26 rows, 10 first-occurrence coords, no lower-row change | **CONFIRMED** | census ≠ declared ten; new column support below band 26; undeclared eta at band 26; unit finite-difference mismatch |
| No D43 / `D43-NF-FID`; four points on promoted D25 + source gates | **CONFIRMED** | `d43*` import; D43 artifact in the relative block; failed 34-row / pristine / band-24 residual gate |
| Witness `rank A = rank [A\|b] = 4`, ker = coker = 6, six unreduced lifts | **CONFIRMED** | rank drop/split; `A v ≠ 0`; source residual through band 26 after a displayed lift |
| Interior `rank A = 4`, `rank [A\|b] = 5` (outside image) | **CONFIRMED** | `λ · b = 0` for all left-kernel `λ`; rank-augmented stays 4; particular solution exists |
| Scoped verdict only; no component / dominance / persistence / germ / char-0 | **HONEST** | hidden promotion past one band and four points |

---

## What was rerun, independently, and not

```bash
/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round1_dtransition/transition_symbol.py --selftest
# PASS selftest: modular RREF/kernel/cokernel/solve and exact 10x10 X27 registry

SCRATCH=$(mktemp -d /tmp/dtransition-grok-XXXXXX)
# SCRATCH=/tmp/dtransition-grok-XuuBQC
/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round1_dtransition/transition_symbol.py --run \
  --out "$SCRATCH/samples.json"
# VERDICT: FREE-TAIL-SIGNAL
```

`--run` into the scratch directory produced a JSON that is **byte-identical** to `cases/round1_dtransition/samples.json` (`cmp` silent; SHA-256 `7ef37f359f518e4e6af3a8a00c3fb4f6d4fbf354d33481fef17fec6d44f51030`). Not stale.

Independent work, **not** `transition_symbol.audit_sample` and **not** stored `rank_A` / `compatible` / `verdict` strings as authority:

- Re-derived `NEW_ROWS` from the `S_A` start table `s_a = 6+2*((a+1) mod 3)`, `s_28=16`, `s_29=36`, keeping `s_a ≤ 26` and `s_a ≡ 2 (mod 6)`. Got `[0,3,6,9,12,15,18,21,24,27]`.
- Re-derived the ten names from ordinary families at `r=21` plus all six families at `r=26`. All ten sit in `GIDX`; `tg01_21` / `tg02_21` are absent (odd, `tg0` step 2). Absolute levels `32+r` are `tf1_53,tf2_53,tg1_53,tg2_53,tf1_58,tf2_58,tg1_58,tg2_58,tg01_58,tg02_58`.
- Rehashed all 19 `SOURCE_FILES` against the banked manifest: **0 mismatches**. Recomputed `source_manifest_sha256` and `projection_sha256`; both match.
- Rebuilt both `p=105337` samples and both `p=105673` samples from `d25_eplus` + `valuation_e2.build_jets` / `euler_rows`. Extracted `A,b` from the dual jet. Re-ran modular RREF. Recomputed the canonical 4×4 minor by Leibniz expansion (not producer RREF).
- Substituted the first canonical right-kernel vector into the unreduced recurrence at each witness. Residuals through band 26 are the zero array. Later even bands `30,36,40` are **not** zero.
- Evaluated the first left-kernel vector on interior `b` at each prime: `λ·b ≠ 0`, and `rank([A|b])=5`.
- Unit finite-difference of `tf1_53` at the `p=105337` witness equals the source column through band 26 and leaves bands `<26` unchanged.
- After reconstruction, `sys.modules` contains no `d43*` / `nffid` module.

Not done, and not required by the scoped claim:

- No full `A^14` cell compatibility rank. That child was not launched.
- The cyclic-orbit product `aside_orbit_jet` was not re-transcribed from a second paper source. Euler's written formula was checked against `euler_rows` (clause 1). Shared-source mistranscription of the orbit algebra remains a possible gap of a different kind; it is not live in the four-point arithmetic.
- Band 28 was not touched.

---

## Hashes

| object | SHA-256 |
|---|---|
| `cases/round1_dtransition/transition_symbol.py` | `869ff70bf04a991fe2e98e420951b26b94041ef01c91bec087d92b83f3fbe91d` |
| `cases/round1_dtransition/samples.json` (banked and scratch rerun) | `7ef37f359f518e4e6af3a8a00c3fb4f6d4fbf354d33481fef17fec6d44f51030` |
| `source_manifest_sha256` | `b60019973eb8af2676a8668f3cce8f4361ce08131763dd09d2654c527106dcfb` |
| `projection_sha256` | `686032872533b57e1084d8200d674be3b1ec569f8c9b70ff160c316a5a7bb3d5` |
| parked `d25fam_p105337_a00pp.ms` | `ef6db7e9ad36666537475fabf8238887de0c7e6d8f02c9381eaa7c810cbe4fe2` |
| parked `d25fam_p105673_a00pp.ms` | `43b81c4ea5f77a5d0d32f433a23e867e9ef4c7228f5d6e7624f43561aa976175` |
| `cases/valuation_e2.py` | `c1a858fbe53c291038b0386c124dbfd4bc79400eedc6b9d5d49a4088736d08f8` |
| `cases/d25_eplus.py` | `e964d2b467f76696f16ccef505f6f66cce7d68e722004bb1a70b6e1cf4f21e7c` |
| `directionb_tails_D21.pkl` | `b4ba8dfcd9755fb3201780cd97c1d2ef38bd26d2d1b023521a0e62a3d6db169e` |

Tool and JSON hashes match the producer report. Parked D25 cells match the previously reviewed D25 family artifacts.

---

## 1. Typed projection `X27 -> X25`

`euler_rows` implements the stated unreduced equation

```text
E = (theta(Phi)-12 Phi) Gamma_eta - Phi_eta (theta(Gamma)-18 Gamma) + 42 t^20
```

with `+42` written only into `V[0][20]` (inhomogeneous, no gradient). `build_jets` is the cyclic-orbit product; no Schur complement, no row reduction, and no D43 object is applied before the band-26 block is cut out. Dual-jet `E.G` was required to equal the independently grouped product-rule path `path_A_rows` through band 26 at every rebuilt sample.

Band-26 output rows from the start table are exactly the ten residue-`2` streams with `s_a ≤ 26`. That is the same congruence rule as the D25 band-24 frontier (nine residue-`0` streams with start 6), shifted by two. The ten first-occurrence coordinates are the band-24 frontier pattern with `n ↦ n+2`:

```text
ordinary r = n-5:  tf1_53 tf2_53 tg1_53 tg2_53
all six   r = n:   tf1_58 tf2_58 tg1_58 tg2_58 tg01_58 tg02_58
```

At all four rebuilt points, scanning every `GIDX` column for first support equal to 26 returns **exactly** those ten labels. The ten new columns are zero on bands `<26`. No eta outside `{0,3,...,27}` carries a band-26 residual or a new-column derivative. The `tf1_53` unit perturbation at the `p=105337` witness reproduces the source column and leaves lower rows unchanged.

This is a fail-closed measurement of the source operator at four modular points, together with the grading/causality constraints (`n ≥ r`, odd bands empty, `n ≡ s_a (mod 6)`). It is not a polynomial-identity certificate that those columns vanish on lower rows as elements of a polynomial ring. Inside the declared four-point modular scope that is the claim, not a defect.

`jmul` uses `float64` with a documented exactness bound. Rechecked: `34·42·p^2 < 2^53` at both primes (`1.58e13` and `1.59e13` versus `9.01e15`), and every product is reduced mod `p` before the next multiply.

---

## 2. No D43; D25/source gates

Grep of the runtime chain (`transition_symbol.py`, `d25_eplus.py`, `valuation_e.py`, `valuation_e2.py`, `eplus_certify.py`, `r1_experiment.py`, `r1_fullcore.py`, `directionb_compress.py`, `directionb_residual32_emit.py`) finds **no** `D43` / `d43` / `nffid` token. After reconstructing points, no such module is loaded.

`directionb_compress` **does** load, but only as the D21 no-log window loader `load_nolog_rows()` used by `verify_full_point` (`raw_D21_rows_vanish`). That is D21 provenance for D25 membership, not a D43 or `D43-NF-FID` object, and it is not used to assemble `A` or `b`. The relative block is cut from unreduced `euler_rows`.

`row22red_32` is a frozen D23 reduced emission checked as one of six `a00pp` pristine gates. It does not construct the band-26 system. Dual-path confirmation: the same points also kill the *pristine* Row_22 and the unreduced dual-jet residual through band 24.

All four rebuilt points:

- lie on the 34-row parked cell (`eval_row` all zero);
- stay in `W1*W2 ≠ 0`;
- pass `raw_D21_rows_vanish`, `pristine_row22_vanish`, `row22compat_48`, `compat_c_zero`, `core23_77`, `row22red_32`;
- have zero dual-jet residual through band 24;
- do not already assign any of the ten X27-only coordinates.

Witnesses need no band-24 frontier completion. Interior sequential points (`free_values = {FREE_BASE+FREE_LIFT mapped to 1..14}`, cell 0) do, at rank 4, and after that completion band 24 is dead. Fiber is `a00pp` (radical frame) at both primes. No field/fiber mismatch.

---

## 3. Witness blocks and unreduced lifts

Independent RREF on rebuilt `A,b` and on the banked matrices, plus Leibniz 4×4 determinants of the canonical minors:

| prime | `rank A` | `rank [A\|b]` | ker | coker | minor | `b` | first kernel vector (tf1_53, tf2_53, tg1_53, …) |
|---:|---:|---:|---:|---:|---:|---|---|
| 105337 | 4 | 4 | 6 | 6 | 85798 | `0` | `(103736, 0, 1, 0, 0, 0, 0, 0, 0, 0)` |
| 105673 | 4 | 4 | 6 | 6 | 58578 | `0` | `(58593, 0, 1, 0, 0, 0, 0, 0, 0, 0)` |

Pivots are identical at all four points: eta rows `0,3,6,9` and columns `tf1_53, tf2_53, tf1_58, tf2_58`. Both minors are nonzero, so rank 4 is not an RREF bookkeeping error.

`A v = 0` holds for the displayed first kernel vector at both primes (direct matvec). Substituting that vector into `build_jets`/`euler_rows` kills every residual coefficient through band 26. The producer `--run` additionally required this for all six free directions at both witnesses (12/12); the scratch JSON is byte-identical, so those `require()` gates fired.

These directions are not Euler gauges of the whole operator: after the same substitution, bands `30, 36, 40` remain nonzero. They are genuine one-band affine fiber directions in the ten new coordinates.

Because `b=0` at both witnesses, the affine space is the linear right kernel. Rank versus solvability do not diverge here: `rank A = rank [A|b] = 4` and a particular solution exists (the origin).

---

## 4. Interior points are outside the image

| prime | `rank A` | `rank [A\|b]` | first left kernel `λ` | `λ · b` |
|---:|---:|---:|---|---:|
| 105337 | 4 | 5 | `(35188, 59711, 45655, 94807, 1, 0, 0, 0, 0, 0)` | 23070 |
| 105673 | 4 | 5 | rebuilt; pairing matches banked `31240` | 31240 |

All six left-kernel pairings are nonzero at both interior points. `rank([A|b])=5` is the affine obstruction: `b ∉ im(A)`. No particular solution. This is not a kernel-dimension count mistaken for incompatibility — `ker A` is still 6, and that is why a cokernel pairing is required.

Observed structure, **not** claimed by the producer and **not** used to enlarge the verdict: at each prime, witness `A` equals interior `A` exactly. Compatibility at these two points is therefore a condition on `b` alone. That is consistent with the new columns first appearing at band 26, but it is still only two points per prime.

---

## 5. Scope of `FREE-TAIL-SIGNAL`

The four-point record is exactly what the verdict name is allowed to mean: two named D25 witnesses carry an exact 6-dimensional affine one-band fiber in the ten new coordinates, and two named interior D25 points are cut by the band-26 compatibility conditions.

It does **not** prove:

- rank 4 on the whole `A^14` cell, or a component dimension;
- that the projection image is dominant, closed, nonempty in the Zariski sense, or empty off the witnesses;
- that the six directions survive at band 28 or in an inverse limit;
- a formal germ, a characteristic-zero point, or a polynomial map.

The producer perimeter states this. The residual support at bands `30,36,40` after a band-26 kernel lift is independent confirmation that persistence is false as an extrapolation from this data.

Software note, not a mathematical failure: `decide()` returns `FREE-TAIL-SIGNAL` from compatible positive-dimensional lifts alone and does not require an interior obstruction. The banked data nevertheless contain the two cuts, and the report's narrative uses them. The verdict string of the JSON is therefore slightly weaker than the report prose; the four-point record is not.

---

## Attack checklist

| Attack | Result |
|---|---|
| Stale samples | **Fail.** Scratch `--run` is byte-identical. |
| Accidental D43 / `D43-NF-FID` import | **Fail.** No token, no module, no D43 artifact in `A`/`b`. |
| Accidental reduction/NF as the band-26 source | **Fail.** Block comes from unreduced `euler_rows`. `row22red` is a D25 membership gate only. |
| Incorrect first-occurrence registry | **Fail.** Independent `S_A` derivation and `GIDX` census agree with the declared ten. |
| Rank vs affine solvability confusion | **Fail.** Witnesses: ranks equal and `b=0`. Interiors: rank jumps 4→5 and `λ·b ≠ 0`. |
| Gauge directions | **Fail as a refutation.** Lifts kill band 26 and *not* bands 30/36/40. |
| Field/fiber mismatch | **Fail.** Both primes, fiber `a00pp`, radical frame, `W1*W2 ≠ 0`. |
| Shared source mistranscription | **Inspected, not live in the arithmetic.** Euler formula matches `euler_rows`. Orbit products were not re-derived from a second text. |

---

## Final verdict

**CONFIRMED**

Evidence tier: modular, four named points, primes `105337` and `105673`, fiber `a00pp`, one chart, one band. Independent source reconstruction, independent modular linear algebra, and a byte-identical producer rerun all agree. The six-dimensional one-band fibers over the two witnesses are exact affine solution spaces of the unreduced recurrence through band 26; the two interior points are genuinely outside that image. Nothing past that scope is confirmed.
