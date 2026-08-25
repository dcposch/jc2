# TD6-C1-C3-FIRST-IDEAL-DUAL — the earliest c1-line obstruction is first-order rigid in c3

Date: 2026-08-24  
Status: **EXACT PRODUCER / GENERIC FIRST-IDEAL DUAL CERTIFICATE / FIRST ORDER ONLY**

## Verdict

On the frozen normalized TD6 source typing, retain the full nonlinear common-
center line and thicken the third center by

\[
 (c_1,c_2,c_3)=(C,1,1+\epsilon),\qquad \epsilon^2=0.
\]

Over `E(C)[eps]/eps^2`, exact refactorization of the varying 3,602-column
transport and the varying original first-band ideal gives

\[
 P_{12}(C,1+\epsilon)=-{k\over 50}
       +\sum_i M_i(C,\epsilon,\mathbf u)L_i(C,\epsilon,\mathbf u),
       \pmod {\epsilon^2},
\]

where

\[
 k=252-342S+144S^2-36S^3.
\]

Thus the exact first-ideal remainder has base coefficient `-k/50` and
identically zero `dc3` coefficient.  This is first-order rigidity of this one
early obstruction class on the generic `C` chart.  It is not a two-center
plane theorem, a neighbourhood theorem, or a family kill.

```text
TD6-C1-C3-FIRST-IDEAL-DUAL / DC3 REMAINDER ZERO /
FIRST-ORDER ONLY / NOT-A-NEIGHBOURHOOD / NOT-SP2 / NOT-JC2
```

## 1. Exact staged identity

The dependency order is

```text
varying raw transport, 3,602 columns -> 132 variables
varying original first-band rows     -> 94 variables
genuine quadratic current P12       -> exact first-ideal remainder
```

| object | exact value |
|---|---:|
| transport rank | `3470/3602` |
| first-band rank | `38/132` |
| raw `P12` parameter degree | `2` |
| raw `P12` pair terms | `2,893` |
| raw `P12` pair digest | `5c832bbf9303278febc583572150d7167dcd3df18d33a69081f38af5ccd648a9` |
| nonzero original first rows in the source lift | `28` |
| multiplier monomial slots | `1,489` |
| source-lift pair digest | `27b13dff3d6947cbfe39934a2594df2096fbdc0070a0ae664095d055a7233780` |
| remainder pair digest | `b7c7eda00c0cd52f0e7b05674b4fb0125d1eff9cdb97231bb70339882c72375b` |

The printed base representative is

\[
 -{126\over25}+{171\over25}S-{72\over25}S^2+{18\over25}S^3
 =-{k\over50}.
\]

The `dc3` remainder has zero terms and no free-parameter monomial.  Division
is replayed first against the normalized varying echelon and then lifted all
the way back to the original first-band rows; no substituted all-stage affine
model is used.

## 2. Varying echelon and omission controls

Every coefficient is computed as an exact pair `(value,dc3)`.  Transport
factorization, affine propagation, first-band Gaussian normalization, quotient
division, and the source certificates all use dual inverses and dual row
operations.  Consequently the differentiated row multipliers—the
`lambda'` contribution—are retained; this is not a frozen-echolon evaluation
of `lambda_0 delta b`.

The replay has two independent fail-closed controls before accepting the zero
remainder derivative:

- the genuine raw `P12` must have a nonzero `dc3` component (`2,781` terms,
  digest `16825ddf8c8dd5189cdc46e241ac57bf8f38df673eda2ae21abab35ed321f558`);
- `11` of the 38 unnormalized first-band pivot leads must have nonzero
  `dc3` coefficient.

Either a frozen raw polynomial or a frozen first echelon trips an assertion.
The zero quotient derivative is therefore an exact cancellation after
coefficient and certificate variation, not omitted differentiation.

## 3. Meaning and fixed scope

Established here:

- the displayed exact dual-number identity over `E(C)`;
- first-order stationarity in the `dc3` direction of the specific earliest
  `P12` class after the original first-band ideal;
- deterministic exact source replay through 28 original rows.

Not established here:

- specialization at every pivot root in `C` (this package is over `E(C)`);
- a full `(c1,c3)` polynomial pencil, even locally;
- absence of an escape beginning at order `eps^2` or at projective infinity;
- vanishing of the later full-current `dc3` sensitivity;
- a statement uniform in boundary, dead-stretch, F1-orbit, pole-scale, or
  other center moduli;
- an SP-2, terminal-class, or JC2 conclusion.

There is no conflict with the reviewed full-cokernel centering tangent: that
package differentiates all later current compatibilities at `(1,1,1)`, while
this package isolates one earlier first-ideal class along a nonlinear generic
`c1` line.  The normalized-section transversality, full three-part Laurent
source tangent, and target-shear caveats of that review remain active.

The honest successor is exact order `eps^2` over `E(C)[eps]/eps^3`, followed
by a certified `c3`-degree or homogeneous/projective gate if needed.  A zero
first derivative alone licenses no neighbourhood inference.

## 4. Source custody and deterministic replay

Case directory: `cases/td6_c1_c3_first_ideal_dual_20260824/`.

The portable helpers resolve the repository relative to their own case path.
They also pin the two canonical compiler sources before import:

| canonical dependency | pinned SHA-256 |
|---|---|
| `cases/td6_jet_orbit_adjoint_20260824/replay.py` | `fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198` |
| `cases/td6_two_chart_first_band_20260824/replay.py` | `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735` |

The local exact-source digests are:

| case source | SHA-256 |
|---|---|
| `replay.py` | `0894a5243588bb9ad68804824f378ddbff97ccb7d0cd28692b01b6c41bb103ed` |
| `c1_c3_thickening.py` | `63379dff67d4f69769bf2434d3d78d5e7b405a0e2ba5f41faf759f3f5bc1a5f9` |
| `c1_pencil.py` | `9077514d6278980c2b23115850d484ef5471ffe925989567a8bc47fb624cddae` |
| `c1_rational_transport.py` | `53ee452432540b2864c7a06e151e16044a566492b797d2673c743daebfb8fad9` |
| `fast_evec.py` | `740ec0058aecf2656d3adc4eb1f8b7dbe5bcb1321fe3a3816f400643fc61cb91` |
| `fast_efield.py` | `e2a614beac9c2ecb5655251029dd8f510dfb507402e80cf49d93d1d1bc525608` |

```sh
/opt/homebrew/bin/python3 cases/td6_c1_c3_first_ideal_dual_20260824/replay.py \
  > /tmp/td6-c1-c3-first-ideal-dual.stdout
cmp /tmp/td6-c1-c3-first-ideal-dual.stdout \
  cases/td6_c1_c3_first_ideal_dual_20260824/replay.stdout
shasum -a 256 -c \
  cases/td6_c1_c3_first_ideal_dual_20260824/MANIFEST.sha256
cmp cases/td6_c1_c3_first_ideal_dual_20260824/MANIFEST.sha256 \
  cases/td6_c1_c3_first_ideal_dual_20260824/FREEZE.sha256
```

The replay uses exact FLINT-backed rational functions and the frozen exact
tower field only.  It performs no floating-point calculation, interpolation,
sampled-root inference, AWS work, or exceptional-fibre inference.

**Quarantine:** `family_killed=false`, `SP2_killed=false`, and
`JC2_resolved=false` are emitted or fixed by scope.
