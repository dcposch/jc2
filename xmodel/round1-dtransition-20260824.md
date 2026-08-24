# D1 report: source-faithful `X27 -> X25` transition discriminator

**Producer:** Nash / `/root/outerloop_critic`

**Portfolio root:** D1, launched independently of the D43 review

**Date:** 2026-08-24 UTC

**Status:** INTERNAL / PRODUCER-CHECKED / MOD-p SIGNAL ONLY

**Verdict:** `FREE-TAIL-SIGNAL`

## Result

There is a clean typed next-depth projection derived only from the promoted
D25 source system.  In the residue-A, B-frozen, no-log, `PIN42`,
`W1*W2 != 0` chart, `X27` adds to `X25`:

- the ten pristine coefficients
  `Row_26[eta^a]`, `a = 0,3,6,9,12,15,18,21,24,27`; and
- exactly ten first-occurrence source coordinates

```text
tf1_53 tf2_53 tg1_53 tg2_53
tf1_58 tf2_58 tg1_58 tg2_58 tg01_58 tg02_58.
```

The projection `pi_27_25 : X27 -> X25` retains every D25
cell/reconstruction/frontier coordinate and forgets only those ten new
coordinates.  Direct source rebuilds prove that all ten new columns are zero
on every band below 26.  Thus no D43 object, `D43-NF-FID`, x-side model,
compatibility compression, or reconstructed D43 witness is used.

At four exact non-origin D25 points (one promoted witness and one
deterministic interior point at each of the two registered primes), the
relative band-26 system is a `10 x 10` affine system `A u = b`:

| prime | D25 point | rank `A` | rank `[A|b]` | ker | coker | exact band-26 lifts |
|---:|---|---:|---:|---:|---:|---:|
| 105337 | witness | 4 | 4 | 6 | 6 | 6, one per kernel basis direction |
| 105337 | interior sequence point | 4 | 5 | 6 | 6 | none; cokernel obstruction |
| 105673 | witness | 4 | 4 | 6 | 6 | 6, one per kernel basis direction |
| 105673 | interior sequence point | 4 | 5 | 6 | 6 | none; cokernel obstruction |

At both witnesses `b=0`.  Each of the six canonical right-kernel basis
vectors was substituted into the unreduced product/Euler recurrence, and
all residual coefficients through band 26 replayed as zero: 12/12 exact
lifts.  Consequently the declared one-band fiber over each named witness is
an exact six-dimensional affine linear solution space over its finite
field, not merely a tangent-kernel count.

At both deterministic interior points the six-dimensional left cokernel has
nonzero pairing with `b`; equivalently rank rises from 4 to 5 after
augmentation.  Those two named D25 points are outside the projection image.
The simultaneous occurrence of compatible six-free-direction fibers and
obstructed base points is the reason for `FREE-TAIL-SIGNAL`: the next band
does not close the relative tail, but its compatibility conditions also cut
the D25 base.

## Exact projection and source audit

The source recurrence used is the unreduced cyclic-orbit construction
`valuation_e2.build_jets`, followed by the pristine Euler equation

```text
E = (theta(Phi)-12 Phi) Gamma_eta
    - Phi_eta (theta(Gamma)-18 Gamma) + 42 t^20.
```

No row reduction or Schur/compatibility elimination occurs before extracting
the new band.  The code computes the full source expression only to check
typing; the emitted mathematical object contains only the ten new rows and
ten new unknowns.

All of the following exact gates pass at every sample and both primes:

1. the sample satisfies all 34 D25 cell equations;
2. the D21/D23 pristine reconstruction gates and D25 band-24 frontier gate
   pass, and every residual through band 24 vanishes;
3. scanning all banked source columns finds exactly the declared ten with
   first support at band 26;
4. none of those ten columns changes a row below band 26;
5. no undeclared eta component occurs in the new band;
6. the dual-number derivative equals the independently grouped product-rule
   derivative;
7. ten unit perturbations per sample reproduce the corresponding source
   column exactly and leave all lower rows unchanged;
8. a mixed ten-coordinate perturbation equals the linear combination of
   the ten columns, proving exact affineness at this band;
9. the canonical nonzero rank-4 minors replay at both primes; right kernels,
   left kernels, and obstruction pairings replay directly;
10. every claimed compatible lift is substituted back through the source
    constructor, not merely through `A`.

The canonical pivot pattern is identical at all four points: eta rows
`0,3,6,9` and columns `tf1_53,tf2_53,tf1_58,tf2_58`.  The corresponding
minor determinants are `85798 mod 105337` and `58578 mod 105673`, both
nonzero.  This repeated pattern is evidence of structure, not a proof that
rank 4 is locus-wide.

The machine record contains hashes for the D21 source pickle, recurrence
and reconstruction code, promoted D25 replay, both D25 cell emissions, both
atlases, and the pristine D23 reconstruction emissions.  Its canonical
source-manifest hash is:

```text
b60019973eb8af2676a8668f3cce8f4361ce08131763dd09d2654c527106dcfb
```

The exact projection-description hash is:

```text
686032872533b57e1084d8200d674be3b1ec569f8c9b70ff160c316a5a7bb3d5
```

## Perimeter

This result is modular only, at `p=105337,105673`, in one chart and one
fiber, at four named points.  It proves neither:

- a component dimension or a locus-wide rank statement;
- dominance, closed image, or global nonemptiness/emptiness of the
  projection;
- persistence of the six directions at band 28 or later;
- existence of a compatible inverse system, a formal germ, a characteristic
  zero point, or a polynomial map.

In particular, first-order rank is not a component or inverse-limit
statement.  The exact affine lifts strengthen the two witness fibers only
through this one next band.

## Stop and next discriminator

The pre-registered D1 question is answered, so this lane stops here.  It
must not roll forward automatically to D43, D75, or B=168.

After independent review, the cheapest useful continuation is not another
point sample.  It is to express the six band-26 cokernel compatibility
functions on one full `A^14` D25 cell and determine their generic rank and
nonempty zero locus by the existing triangular certificate.  That would
decide whether the mixed witness/interior behavior is a genuine positive-
dimensional image stratum.  Only a reviewed, nonempty compatible base
stratum should be prolonged to band 28.

## Reproduction and artifacts

```sh
/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round1_dtransition/transition_symbol.py --selftest

/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round1_dtransition/transition_symbol.py --run \
  --out cases/round1_dtransition/samples.json
```

Artifacts:

- `cases/round1_dtransition/transition_symbol.py`
  - SHA-256 `869ff70bf04a991fe2e98e420951b26b94041ef01c91bec087d92b83f3fbe91d`
- `cases/round1_dtransition/samples.json`
  - SHA-256 `7ef37f359f518e4e6af3a8a00c3fb4f6d4fbf354d33481fef17fec6d44f51030`

No shared ledger was edited.
