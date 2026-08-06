# FASTCOEF — FLINT backend for the hot pipeline arithmetic

`lib/fastcoef.py` ports the hot coefficient arithmetic (SystemA bracket
generation, Cascade3 b-elimination) to FLINT via python-flint, keeping the
pure-Python path (lib/jc.py, lib/reduce3.py) as the default, the fallback,
and the differential oracle.

## Install

    python3 -m pip install --user --break-system-packages python-flint

Verified: python-flint 0.9.0 (`flint.fmpq_mpoly` available), Python 3.14.6,
macOS arm64. If python-flint is missing, `JC_BACKEND=flint` falls back to
the pure path with a one-time stderr warning — nothing breaks.

## Switch

    JC_BACKEND=python   # default: pure-Python Fractions (unchanged oracle)
    JC_BACKEND=flint    # fmpq_mpoly kernels

Read per call/at Cascade3 construction, so tests flip it in-process. Wired
into `jc.bracket` (SystemA generation) and `reduce3.Cascade3.run`
(elimination). `chartelim.two_chart` stays pure in both backends (it only
consumes the — parity-checked — cascade output).

`JC_MAXTERMS` (optional) overrides the Cascade3 swell abort threshold
(default 20000). Changing it changes which cores are reachable; parity runs
must leave it alone.

## What is flint, what is not

* `fastcoef.cadd/cmul/cscale/cneg` — drop-in coefficient ops over
  `fmpq_mpoly` (same dict contract as jc.py); oracle-tested.
* `fastcoef.subst_linear_many` — the Cascade3 hot kernel. Splits each
  equation c = A·v + B and computes B + A·g with one FLINT multiply per
  equation (g converted once per elimination), then inverse-pair reduction.
  Contexts are cached per variable-universe size; global var indices are
  mapped to a dense local range at the boundary (monomial-tuple <->
  exponent-vector adapters), so exponent vectors stay short at farm scale
  (1314 vars).
* `fastcoef.bracket_fast` — generation is accumulation-bound (coefficients
  are single variables), so the fast path is in-place accumulation, not
  FLINT; conversion-based variants measured slower for that shape.
* python-flint pitfall (measured): `fmpq_mpoly_ctx.from_dict` is quadratic
  in term count; large polynomials are built by chunked `from_dict` +
  balanced tree sums (`fastcoef._build`).

## Parity status: PROVEN (tests/test_parity.py)

`python3 tests/test_parity.py` — PASS (2026-08-05):
* 2000 randomized drop-in checks (int + Fraction) vs the jc.py oracle;
  60 randomized bracket checks vs the pure bracket;
* full pipeline (SystemA -> Cascade3 -> two_chart) on reg_9_24_c3 and
  open_8_28_c2 under both backends: identical cascade status, elimination
  sequence, zeroed vars, log, core equations, two_chart leaves, and
  byte-identical .ms emissions (SystemA raw, core at p=65521 and char 0,
  both chart leaves — 5 files per case).
* Full pre-existing suite (test_jc, test_planeprobe, test_conjE,
  ltest_polynomials) passes under both backends.

One semantic canonicalization was required for cross-backend determinism:
`Cascade3._pick_pivot` now iterates its per-equation candidate census in
sorted var order, so pivot TIE-breaks no longer depend on dict insertion
order (which differs between backends). Any unit pivot is sound (same
invariants as before); in tie cases cores could differ from pre-change
archives while remaining valid. Checked old-vs-new on reg_9_24_c3 and
open_8_28_c2: identical cores (no tie was actually decided differently).
python-vs-flint output is byte-identical by the parity gate.

## Two speedups, kept separate

1. Shared-path fix (both backends): Cascade3's substitute/g-builder/
   _inv_reduce used `out = cadd(out, {..})` chains, which copy the whole
   accumulator per term (quadratic). Rewritten to in-place accumulation —
   verified content- AND insertion-order-identical to the old code on
   reg_9_24_c3 and open_8_28_c2 (equations, elim sequence, key order all
   equal), so the pure path remains the same oracle, just linear.
2. FLINT kernel (JC_BACKEND=flint): per elimination, each affected equation
   c = A·v + B becomes B + A·g with one fmpq_mpoly multiply; Fraction
   arithmetic leaves Python entirely for the products.

## Benchmarks (12-core M-series Mac, 32 GB, 2026-08-05, final code)

Cascade3 wall time, each run SOLO on an idle machine (concurrent CPU-bound
processes were observed to inflate the Fraction-heavy python runs several-
fold; flint runs are much less sensitive). Generation negligible except
moh, listed separately.

| case                          | python         | flint              | speedup | status/notes |
|-------------------------------|----------------|--------------------|---------|--------------|
| reg_9_24_c3                   | 0.3s           | 0.2s               | 1.5x    | reduced; identical 23-var core |
| open_8_28_c2                  | 1.7s           | 1.3s               | 1.3x    | reduced; identical 30-var core |
| open_8_28_c1                  | 143.7s         | 107.1s             | 1.3x    | reduced; identical 73-var core (114 elims, median eq 1166 terms) |
| moh_48_64 (unreduced, 1314 v) | gen 2.0s + 13.7 min | gen 0.4s + 3.9 min | 3.5x | both: aborted-swell at 43/830 elims (biggest eq 21131 > 20000 cap), identical terminal state |

Context: the old documented moh baseline (notes.md 2026-07-30, pre-dating
this work) was 73 min to the same 43-elimination abort. On pivot-scan-
dominated cases (c1) most of the gain comes from the shared-path fix; the
FLINT kernel's multiply advantage shows at farm scale, where substitution
products dominate.

moh_48_64 completion: the cascade reaches its terminal verdict
(aborted-swell, 43 eliminations) in 3.9 minutes — well within 30. It still
does not run to a reduced core, because the MAXTERMS_EQ=20000 swell cap is
semantic (parity-pinned), not a speed limit. Raised-cap probe
(JC_MAXTERMS=200000, flint): pushes past the wall to 49+ eliminations, but
equations swell to ~48000 terms by elim 48 and keep growing — 830
eliminations do not complete within a 30-minute budget. The densification
is structural (consistent with notes.md: GGV §4 reductions are
load-bearing), not an arithmetic-speed problem.
