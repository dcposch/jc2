# D5G35: complete raw determinant range and conditional R7R1 cutoffs

Date: 2026-08-27  
Lane: `a1_total_lift_design` / Sol2

## Verdict

**`PASS-D5G35-COMPLETE-RAW-DETERMINANT; TARGET GATE UNSOLVED`.**

The frozen D3 raw alphabet is complete for the two source polygons, not
merely for determinant weights through 22: its positive rows stop at
weights 14 for `F` and 21 for `G`.  I compiled the literal raw determinant
through their full pair-sum range, serialized all contributions, and froze
the exact target gate

```text
D0=...=D21=0, D22=1, D23=...=D35=0.
```

No solution of that gate is asserted.  The extension is additive and
review-independent: rows `D0,...,D22` are byte-identical to frozen,
independently hostile-audited D5G, while the new rows use only the same
literal raw-source file and recurrence.

There is one useful sharpening.  The nominal top row `D35` cancels
identically; `D34` is the highest potentially nonzero row.  The requested
`D35=0` gate is retained as a checked redundant structural row.

## 1. Frozen ring, source, and map

Work over

```text
C = Q[400 named positive-weight D3 raw slots],
S = C[X,t],
H = X^8-1,
F = H^2 + sum_(i=1)^14 t^i F_i,
G = H^3 + sum_(j=1)^21 t^j G_j.
```

Each raw slot has exactly the name, source exponent, chart image, and weight
recorded in D3's frozen `RAW_INPUT.json`.  An independent enumeration of
the source polygons gives

| source | all polygon rows | weight-zero rows | positive slots used | largest positive weight |
|---|---:|---:|---:|---:|
| `F` | 141 | 17 | 124 | 14 |
| `G` | 301 | 25 | 276 | 21 |
| total | 442 | 42 | 400 | — |

The 42 weight-zero raw rows are not variables in `C`: as in D5G, the
normalized leading rows are fixed to `F0=H^2` and `G0=H^3`.  No local Morse
coordinate, factor evaluation, source equation, specialization, or alias
map is introduced.

The literal polynomial map is

```text
(F,G) |-> E=12 F_X G-8 F G_X-t(F_X G_t-F_t G_X)
          = sum_n D_n t^n,

D_n=sum_(i+j=n)((12-j)F_i'G_j+(i-8)F_iG_j').
```

Every final coefficient monomial and every pre-cancellation derivative
contribution is serialized in
`DIRECT_DETERMINANT_D0_D35.json`.

## 2. Exact complete-range result

The full artifact contains

```text
36 rows D0,...,D35,
63,012 serialized derivative contributions,
34,528 final nonzero sparse terms.
```

The first 23 row records, including all contribution lists and digests, are
byte-equal to D5G's frozen `DIRECT_DETERMINANT.json`.  D5G's exact D22
certificate is unchanged.  The first two new rows have

| row | final terms | serialized contributions | final-term digest |
|---|---:|---:|---|
| `D23` | 626 | 1,106 | `7b5ad4a59cdfb700135ceee56c2b7a0d1009f2fc5c1c1132371923781e916b61` |
| `D24` | 494 | 896 | `e0c13f3d358c6ebb12dc8c4be69b073aa0291d7c8c9c67d7ceda07704816c1c8` |

At the top,

```text
D34 = (2 f_2_0 g_3_1 - 3 f_2_1 g_3_0) X^4
    + (8 f_2_0 g_4_4 - 12 f_3_4 g_3_0) X^5,

D35 = (-18+18) f_2_0 g_3_0 X^4 = 0.
```

The `D35` record deliberately retains both opposite contributions.  All
rows above 35 vanish by source support; hence all rows above 34 vanish after
the displayed top cancellation.

## 3. Independent dense replay and mutations

The verifier has a second implementation that does not call the sparse
coefficient recurrence.  It assigns deterministic nonzero rational values
to all 400 raw slots, constructs dense series in `Q[X,t]/(t^36)`, performs
the four differentiated products, and compares every row `D0,...,D35`.
The exact comparison passes, with full-series digest

```text
6f164fca16821a3441e46713a7b90489145eeb9d39537e1a66c63e2dfa23df82.
```

The target gate contains 734 nonzero coefficient generators over `C`.
It is frozen with status `UNSOLVED-EXACT-GATE`.  Two load-bearing mutations
are replayed both in the sparse gate and under the dense control:

```text
D23 -> D23+1  rejects the D23 target row;
D24 -> D24+1  rejects the D24 target row.
```

These mutations revoke the corresponding R7R1 hypotheses; they do not
assert that the resulting `q`-form is non-exact.

## 4. Typed, conditional R7R1 interface

The additive corrected R7R1 report works after adjoining `p` with `p^4=H`
and changing to its characteristic coordinate.  Its sharp cutoff is

```text
E=t^22+O(t^N) licenses q_n dX exact exactly when n+22<N.
```

Consequently the raw target rows license the first forms only as follows:

| exact target rows available | congruence | licensed by corrected R7R1 |
|---|---|---|
| through `D22` | `E=t^22+O(t^23)` | `q0` only |
| plus `D23=0` | `E=t^22+O(t^24)` | `q0,q1` |
| plus `D24=0` | `E=t^22+O(t^25)` | `q0,q1,q2` |

Here

```text
q0=p^2,
q1=F1/(4p^5),
q2=F2/(4H)-F1^2/(16H^3).
```

Thus the `D23+1` mutation removes the license for `q1`, and `D24+1`
removes the license for `q2`.  Corrected R7R1 is still provisional pending
its frozen different-model review, so this table is a typed conditional
interface rather than a promoted downstream theorem.

If the entire frozen gate were later solved, the bounded determinant itself
would satisfy the exact identity `E=t^22`: `D35` is already structurally
zero and all higher rows vanish by support.  This does **not** make the
R7R1/de Rham tower finite.  Its transformed series `Q` can remain infinite,
and no finite decision or descent claim follows here.

## 5. Exact replay and custody

Case directory:

```text
cases/ggv_8_28_raw_global_determinant_d5g35_20260827/
```

Replay from that directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B compile_d5g35.py --check \
  ../ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json \
  DIRECT_DETERMINANT_D0_D35.json TARGET_GATE.json RESULT.json
```

The replay pins the preregistration, additive `D35` census note, D3 raw
source, D5G freeze/direct/D22 certificate/independent hostile audit, the
first R7 audit, and corrected R7R1 producer/verifier/frozen review prompt.

## Scope boundary

This result proves only a complete literal raw determinant compiler, a
frozen but unsolved coefficient gate, and a conditional cutoff interface.
It proves no source equations, target specialization, Keller landing,
finite tower, descent, `8_28` face or family exclusion, `G2-PSC`, `G2-BD`,
counterexample, or JC2 result.
