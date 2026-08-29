# Fable5 hostile review: r3 fixed-even `Q=X` endpoint-zero theorem

Date: 2026-08-28
Reviewer: Fable 5, independent desk audit, standard library only.

Verdict: **PASS WITH ONE PRECISION REPAIR (theorem CONFIRMED)**

- Every displayed equation, constant, sign, and normalization in the charged
  report is exact and was reproduced by an independent checker that shares no
  code path with the producer chain (gates re-derived from the fractional
  powers `(F/F0)^((n+2)/8)` by an Euler-ODE recurrence; Laurent elements as
  normalized `N/A^k` pairs; windows re-extracted from the frozen
  `RAW_INPUT.json`).
- The surviving scope is exactly the stated one: the fixed even prefix
  `A=X^4-1, Q=X, r=e=F8=F10=F12=F14=0, F1=F3=F5=F6=0, F2=-A^3Q/8,
  F4=A^2Q^2/256`, `F7=A f`, literal odd raw windows, `q7..q15` exactness,
  `G13` literal lower floor, `G15` polynomiality, arbitrary scalar modes,
  characteristic zero. No promotion to arbitrary `Q/e/F8`, full `lambda=0`,
  endpoint/Keller, or JC2.
- First questionable line (the only one): report lines 94–95, "modes born
  after weight 10 have not entered by `G15`." Read literally this is false:
  `c12` enters the characteristic at weight 12 (constant load `c12*1` on
  `G12`, since `F^((6-6)/4)=F^0=1`) and `c14` enters at weight 14 with the
  Laurent carrier `c14*A^-1` (a pole unless cancelled by the even tail).
  What is true, and what the theorem needs, is that `c10,c12,c14` have zero
  load on all four audited coordinates `G11[X^0], G13[X^0], G15[X^1], R15`,
  for three distinct verified reasons: `c10` needs `[t^5](1+u)^(1/4)` and no
  odd `t`-partition of 5 exists (`F5=0`); `c12` multiplies `F^0=1`, which has
  no positive-degree `t`-coefficient; `c14` needs `[t^1]` and `F1=0`.
  `c16,c18,c20` are genuinely unborn (shifts 16,18,20 > 15). The matching
  producer-checker lines 252–254 (`assert 10+5==15 ...` and
  `assert min((12,14,16,18,20)) > 10`) are numerology, not a proof of
  mode-completeness; my checker replaces them with the computed census.
  This is a documentation/precision repair only; no verdict impact.

## Frozen inputs (verified at start and end of the run)

| file | sha256 |
| --- | --- |
| r3 report | `a6e49a08a6fc92c71f9f9ee34079b5626f6a00a20499b06e50c8b8451f3338be` |
| r3 checker | `49e61d547e8b30e6ffc3c792f1dffdb6ae8e960aec490047e5c544fee222adf1` |
| q15 report | `188317138e60224f5a7e9dc1de18ab339384c5246c1cabf12acc20657dac7d5f` |
| q15 checker | `6c63fe47ebf35dd56e286ab358b0932f1dad9143875fde30c216a425119e442a` |
| r2 report | `b5433f4e4a76f48d8899d59b28290dc7075ac591b89913323e5102a998e73a08` |
| r2 checker | `fb29dec1a7eb08a41818c8ea802c984f893d8a222d38aade6fdf4af9bc272638` |
| RAW_INPUT.json | `28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876` |

Neither producer checker was imported or executed. All producer bytes are
unmodified.

## 1. The 50-by-55 system (independent)

The five gates were re-derived from scratch as
`h_n = (2/(n+2)) A^((n-1)/2) [t^n](F/F0)^((n+2)/8)`, `n=7,9,11,13,15`,
using the ODE recurrence `n g_n = sum_j (e j - (n-j)) u_j g_{n-j}` for
`(1+u)^e` (the producers used a binomial summation — genuinely different
code). Unit columns at weight 15 match the frozen q15 closed form
(`-9/256 A^2 Q F13`, `45/2^15 A Q^2 F11`, `-15/2^21 Q^3 F9`,
`-45/2^29 Q^4 f`), and `h7 = f/4`.

Variables: exactly 20 raw (`f` degrees 0–5 with `F7=Af`; `F9` 1–7; `F11`
1–5; `F13` 2–3, all re-extracted from `RAW_INPUT.json`, which gives F-window
0–9 at weight 7, 1–7 at 9, 1–5 at 11, 2–3 at 13) plus 35 primitives
(`d7<=2, d9<=4, d11<=6, d13<=8, d15<=10`, forced by the block degrees
6,8,10,12,14 and the nonzero `T5` leading multiplier `k+10`). Equations:
`h_n = T5(d_n)` coefficientwise over 6+8+10+12+14 = 50 slots.

Exact RREF: rank 50, nullity 5, free coordinates precisely
`d15[X^4], d15[X^5], d15[X^6], d15[X^8], d15[X^9]` (verified by name
comparison AND by replaying every basis vector through all 50 original
equations via a full nonlinear series recomputation — this also certifies
joint linearity of the odd gates in the raw data). Canonical full-basis
digest (55 named exact fractions per vector, newline-joined):

```text
basis_sha256 = feb2e87498b4928ac5ec117523af2b0c2b0074d96945f920ff7a888c5972e7b5
```

Derived raw coordinates: `f0 = -(2^29/75)a1 + (2^28/225)a4` confirmed;
`F7[X^0] = A(0)f0 = -f0` confirmed.

## 2. Characteristic rows and mode census

`G = F^(3/2) + sum_{k=1..10} c_(2k) t^(2k) F^((6-k)/4)`, branch
`(A^4)^(m/4) := A^m`. For every basis vector and every label in
`base, c2, c4, c6, c8, c10, c12, c14` (with `c16, c18, c20` structurally
unborn, shift > 15) the full rows were computed:

- `G11[X^0]`: only `c4` loads, row `-f0`. All other labels zero.
- `G13[X^0]`: only `c6` loads, row `(3/4) f0`. All other labels zero.
- `G15[X^1]`: `c4` load is exactly `F11[X^1]` (since `A^4 u11 = F11`
  identically); `c6` row `(0, -2^21/5, 0, 0, -2^19/3)`; `c8` row
  `(0, 0, 2^29/75, 0, 0)`; `base, c2, c10, c12, c14` zero.
- `G15` pole: every label on every basis vector has pole order <= 1. The
  complete `A^-1` numerator reduced mod `A` has `X^1` coordinate rows
  `c6: (0,0,0,0,-7*2^19/3)`, `c8: (0,0,2^29/15,0,0)`, all others zero.
  Hence `R15 = -(7*2^19/3)c6 a4 + (2^29/15)c8 a2` and `G15` polynomiality
  over the char-0 coefficient field forces the whole remainder — in
  particular `R15` — to vanish. Only this one residue coordinate is needed.

Odd-row linearity in the fiber coordinates (which licenses per-basis
computation) holds for parity reasons — an odd weight <= 15 admits no
double-odd `t`-partition (7+7=14 even, 7+9=16>15) — and was verified
computationally at the non-basis point `a=(1,2,3,4,5)` for all labels and
all four rows.

Mode census (the precision repair): `c10` is born at `G10` (load `A`) with
all odd loads zero (`t^5` residual, `F5=0` and no partitions); `c12` is born
at `G12` (constant load 1, `F^0` has no positive `t`-coefficients above it);
`c14` is born at `G14` (Laurent load `A^-1`, killed at `t^1` by `F1=0`);
`c16..c20` are genuinely unborn.

## 3–5. Endpoint identity and exclusion

From the window census (re-derived from `RAW_INPUT.json` degrees plus the
row weights `12-j`, `i-8`), `D22[X^0]` sees exactly the nonzero-coefficient
pairs `(11,11,+1)` and `(7,15,-1)`, i.e.
`T = F11[X^1] G11[X^0] - F7[X^0] G15[X^1]`, with pinned target `+1`.

The `c4` contribution cancels identically between the two terms
(`quad(F11x1, -f0) + quad(f0, F11x1) = 0`), and

```text
E = f0*(c6*(-2^21 a1/5 - 2^19 a4/3) + c8*(2^29 a2/75))
E = (f0/5) R15 + (4/3)(-2^21 a1/5 + 2^20 a4/15) G13[X^0]
```

hold as exact quadratic-form identities in `Q[a0..a4]`, per c-mode,
verified coefficientwise for **every** label (base and `c2, c10, c12, c14`
give `0 = 0`, not merely the nonzero rows). Because the multipliers
`f0/5` and `(4/3)(-2^21 a1/5 + 2^20 a4/15)` are polynomials, this is
**ring-level ideal membership** `E ∈ (R15, G13[X^0])` — a syzygy valid over
any Q-algebra — not a field or radical consequence. The `G13` literal lower
floor gives `G13[X^0]=0`, `G15` polynomiality gives `R15=0`, hence `T=E=0`
with no case split and for arbitrary scalar modes; the target is `1 != 0`
(and a target sign flip to `-1` would not rescue anything), so the entire
fixed even prefix is excluded. Confirmed.

## 6. r2 one-point control

The r2 mutation point is exactly basis vector `a=(0,1,0,0,0)`: its raw data
`f=(2^29/75)(-1+11X^4)`, `F9=(2^23/75)(7X-27X^5)`, `F11=F13=0` and
primitives `d7..d15` coincide with the RREF basis vector, so it passes the
q gates by the basis replay. With `c2=c6=1`: `G8..G12` are polynomial and in
their literal windows; the first failure is
`G13[X^0] = -2^27/25` (`= (3/4)*1*(-2^29/75)`, matching formula (2)); the
determinant rows `D0..D13` all vanish. Setting `c6=0` repairs the `G13`
window, after which `G14` has a genuine `A^-1` pole with remainder
`-5X^2/2^34` (the producer's `-5X^6/2^34` numerator reduced mod `A`).
Endpoint directly computed: before, `T = 2^50/375` (the frozen upstream
coupling, reachable as target only after a `theta^2=375/2^50` rescale);
after `c6=0`, `T = 0`. The r3 theorem explains the control: with `c6=1` the
point violates the theorem's `G13`-floor hypothesis, with `c6=0` it
satisfies the hypotheses and lands on `T=0 != 1`, exactly as the theorem
predicts. No contradiction.

## 7. Scope firewall — assumptions that enter

char-0 field; `A=X^4-1`; `Q=X`; `r=e=F8=F10=F12=F14=0`; `F1=F3=F5=F6=0`;
fixed `F2=-A^3Q/8`, `F4=A^2Q^2/256`; the branch divisibility `F7=A f`
(pinned upstream, not derived here); literal odd raw windows from
`RAW_INPUT.json`; `q7..q15` exactness with primitive degree caps; the
branch normalization `(A^4)^(m/4)=A^m`; `G13` literal lower floor; `G15`
polynomiality; pinned endpoint target `+1` (only `!=0` is used). Arbitrary
scalar modes are genuinely free, including `c2`. Nothing here promotes to
arbitrary `Q/e/F8`, full `lambda=0`, four-root endpoint, Keller, or JC2.

## 8. Mutation battery (all detected)

M1 dropped equation row → dimension 6 ≠ 5. M2 dropped variable `d13_0` →
free census wrong. M3 wrong free set `{...,d15_7,...}` → name mismatch.
M4 omitted `c6` trajectory → r2 coupling `2^50/375` lost. M5 treating
`c12/c14` as genuinely unborn → refuted by their nonzero `G12/G14` loads.
M6 residue sign flip → identity (4) fails. M7 endpoint relative-sign flip →
`c4` cancellation destroyed (nonzero `c4` quadratic form). M8 target-sign:
exclusion robust, `0 != ±1`, and target ≠ 0 pinned. M9 nonzero mod-`A`
remainder (the repaired-`G14` element) must not be accepted as polynomial —
the strict remainder test rejects it; a pole-order-only test would not.
Frozen hashes re-verified after the mutation battery.

## Replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  xmodel/ggv-upper-endpoint-deep-q1-lambda0-qx-fixed-even-endpoint-zero-r3-hostile-review-fable5-20260828-check.py
```

Deterministic, standard-library only, repo-root-relative manifest, ends with
`PASS_FABLE5_HOSTILE_R3_QX_FIXED_EVEN_ENDPOINT_ZERO`.
