# DEP-D3 D4R1: repaired factor-local raw-to-Morse cleanup DAG

Date: 2026-08-27  
Lane: `a1_total_lift_design` / Sol2  
Status: provisional producer PASS; fresh hostile review required

## Verdict

**`PASS-DEP-D3-D4R1-FACTOR-LOCAL-CLEANUP-DAG-W22`.**

D4R1 additively repairs the quarantined D4 type error.  The sparse
polynomial

```text
R_pre=t^14 X-(1/4)t^16
```

is now correctly labelled an `X`-dependent precursor remainder, not the
Morse critical-value series.  The repaired producer evaluates the entire
49,964-node generic cleanup DAG under the five supporting raw coefficients
and obtains exactly

```text
U14=c in A=Q[c]/(c^8-1),
```

encoded as `(0,1,0,0,0,0,0,0)` in the basis
`1,c,...,c^7`.  Therefore the substantive discriminator survives: legal
lower raw rows really can synthesize factor-local `U14=X`, despite raw
`F14` containing only `X^2`.  The old precursor notation is not used as
evidence.

No descendant may consume this provisional result before fresh hostile
review.

## 1. Additive custody repair

The original D4 freeze and report remain byte-identical at

```text
8a79c5495f446d36dfd4bc08d6ac8a1326d7b4e885dc51d063fa1f4b52ff92d1
  cases/ggv_8_28_raw_to_morse_cleanup_dag_d4_20260827/FREEZE.sha256
bf81b9059e200bad690b3cd3f14b0fad102e4a07b0ae98f41e322216c2084803
  xmodel/ggv-8_28-raw-to-morse-cleanup-dag-d4-sol-20260827.md
```

and are explicitly quarantined.  D4R1 lives in a new case and report.  It
pins those old bytes only as negative custody/history, plus the exact D3 raw
source and reviewed R2 local interface.

The correction is load-bearing.  In a root-local chart `X=c+z`, a Morse
critical value belongs to `kappa_p[[t]]`; the precursor term `t^14 X`
contains `z` and cannot itself be called `U(t)`.  D4R1 instead uses it only
to define a legal raw polynomial and then applies the independently built
critical-section recurrence.

## 2. Exact five-row discriminator

Set

```text
H=X^8-1,
u_pre=H+t^6 X-(1/2)t^8,
R_pre=t^14 X-(1/4)t^16.
```

The precursor sparse identity is

```text
F=u_pre^2+R_pre
 =H^2+2t^6 H X-t^8 H+t^12 X^2.
```

Its five nonleading rows are all literal D3 slots:

| raw slot | chart monomial | coefficient |
|---|---|---:|
| `f_1_5` | `t^6 X` | `-2` |
| `f_9_29` | `t^6 X^9` | `2` |
| `f_0_0` | `t^8` | `1` |
| `f_8_24` | `t^8 X^8` | `-1` |
| `f_2_2` | `t^12 X^2` | `1` |

Raw weights 14 and 16 vanish by the displayed cancellations, but that is
only a support check.  The load-bearing second replay assigns these five
rationals to their generic raw leaves, assigns zero to every other
positive-weight leaf, and evaluates every DAG node exactly in `A`.

The nonzero resulting Morse critical values through weight 22 are

```text
U14 = c,
U16 = -1/4,
U20 = -(1/8)c^2,
U22 = (1/16)c.
```

In particular `U14=c` is not inferred by replacing local `X` with `c`; it is
the output of the exact critical-section evaluation.  The same evaluation
serializes the nonzero critical-shift coefficients, providing an independent
trace of the recentering.

The mutations retain their narrow meaning: sign changes break the precursor
identity or leave a forbidden weight-16 row, deleting a supporting row
breaks it, and a direct raw `F14:X` is rejected because no such D3 slot
exists.  None of these mutations substitutes for the exact `U14=c` check.

## 3. Generic cleanup DAG

The generic calculation is unchanged in scope from D4 but is re-frozen in
the corrected case.  It works over the finite etale algebra

```text
A=Q[c]/(c^8-1)
```

and fixes `F0=H^2`, `G0=H^3`.  All 400 positive-weight D3 raw slots are
independent leaves.  It solves

```text
F_X(c+s(t),t)=0
```

through weight 22, sets `U=F(c+s,t)`, constructs the oriented coordinate
`u=H mod t`, and emits every coefficient `0..22` of
`U,W,V,Q,Gamma`.

The only displayed unit inversions are

```text
(F0''(c))^-1 = (128c^6)^-1 = c^2/128,
(2H'(c))^-1  = (16c^7)^-1  = c/16,
(H'(c))^-1   = (8c^7)^-1   = c/8.
```

There is no inversion involving a raw variable.  Closed-fibre outputs are
`s0=U0=W0=V0=Q0=0`, `Gamma0=1`.

The DAG census is 400 raw leaves, 1,204 constants, 18,332 additions, and
30,028 multiplications, total 49,964 nodes.  Its canonical compact encoding
has 8,400,824 bytes and SHA-256

```text
bc3bd04c453eef74d19682b020541f64ca1f42557f2c177692f02485ed1a17d7.
```

Every coefficient is identified by its root node.  The deterministic
producer reconstructs the full DAG before byte-comparing the manifest.
Factor IDs, chart, deck `ORIENTED_PLUS_H`, orientation `u=H mod t`, and
determinant `H'(c)` remain explicit.  The `u^4+` terms are retained as a
typed residual; R2, not D4R1, supplies their constant-channel irrelevance.

## 4. Remaining global gap

D4R1 repairs the local provenance interface only.  It does not impose the
Keller recurrence on a raw specialization and does not glue the factor-local
outputs to a literal global polynomial `E22`.  D3 already shows that the
uncontrolled global `H`-multiple can move all seven `M`-cokernel
coordinates.  Consequently no support-only or branch-bit face exclusion
follows.

## Replay and scope

```bash
python3 cases/ggv_8_28_raw_to_morse_cleanup_dag_d4r1_20260827/compile_cleanup_dag_d4r1.py \
  --check \
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json \
  cases/ggv_8_28_raw_to_morse_cleanup_dag_d4r1_20260827/RESULT.json
```

Maximum scope is a factor-local formal cleanup DAG through weight 22 plus
the exact five-row `U14=c` discriminator.  This is not a global polynomial
automorphism, global `E22`, global `H`-multiple control, Keller
specialization, `8_28` face/family exclusion, `G2-PSC`, `G2-BD`, Keller
pair, counterexample, or JC2 result.
