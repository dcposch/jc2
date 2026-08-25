# TD6 q2-beta raw `C=U=0` and origin rebuild — V70 AWS

## Verdict

**PRODUCER-EXACT PASS; hostile review pending.**  In the fixed source-typed
normalized A3 section with

```text
q_beta=t+beta*t^2+t^25,
q_beta'=1+2 beta t+25 t^24,
```

the raw stratum `C=U=0,V!=0` is inconsistent in the first band for every
beta, and the raw origin `C=V=U=0` is inconsistent already in transport.
Together with the hostile-reviewed V33 theorem on `U=0,C!=0`, these are a
producer-exact three-piece constructible cover of the whole raw `U=0`
divisor.  No whole-divisor composition is promoted before review of this V70
package.

## Exact results

On `C=U=0` over `E(V)[beta]`, transport has rank `3470/3602`.  Its two
nonconstant pivot events both have numerator `-V`, so the transport chart is
`V^2`.  The first-source denominator is `V`.  The first system has rank
`36/132` and the unique dependent original row `('X-2',14)`.  Its exact
14-row original-source combination has beta-degree-zero residual and monic
compatibility gcd one.  The V70 wrapper replays that combination, fires a
wrong-row control, and computes the complete parent-style denominator

```text
V^2 * V * 1 = V^3.
```

Thus this certificate excludes exactly `C=U=0,D(V)`; it does not itself
specialize to the origin.

At `C=V=U=0`, transport rank drops to `3468/3602` and one dependent original
transport row is incompatible: row 6460, key `('g','X',-19,20)`, with a
21-row original-source combination and beta-degree-zero unit residual.
There are no nonconstant transport pivots, and the complete certificate
denominator is one.  Its wrong-row control passes.  This closes the origin
as a raw transport theorem and correctly skips later bands.

Direct-q-prime omission controls reproduce both obstructions.  This shows
that these early contradictions do not depend on the direct `2 beta t` term;
it does not broaden the fixed source family.

The exact set-theoretic composition is

```text
V(U) = [V(U) intersect D(C)]
       union [V(C,U) intersect D(V)]
       union V(C,V,U).
```

The first piece is the corrected, hostile-reviewed V33 scope; the last two
are V70.  Restoration of a whole-`U=0` theorem is review-gated.

## AWS custody

The byte-identical source ran under 12-GiB caps on Box02
`34.203.207.55` and Box03 `98.80.65.144`:

- `td6_v70d_u_h_zero_box02_20260825T1636Z`, PID 191766;
- `td6_v70d_u_h_zero_box03_20260825T1636Z`, PID 82534;
- `td6_v70d_origin_box02_20260825T1636Z`, PID 191774;
- `td6_v70d_origin_box03_20260825T1636Z`, PID 82542.

All four main runs returned rc zero.  The two `u-h-zero` mathematical
outputs are byte-identical with SHA-256
`2431ed0217d8d71dce2929a8581036d0e11921396dff661466288901243f4ebd`;
the two origin outputs are byte-identical with SHA-256
`90df496c59c8283c85cec26521a2b422d6ca8d658aa0e8802c968052cd505d67`.
The omission-control output SHAs are `4a31f527...` and `6005d4ad...`.

The complete-localization wrapper SHA is
`07cf6df3b4f7c5c43f02dcbc30bff118618630090cbc85bd0cb587975c303179`;
it pins V69 replay SHA `9a518a4b...`.  The portable V69 dependency archive
SHA is `9e89808c...`, and the V70 source-manifest SHA is `6aed38de...`.
Recursive base/V31/V33/V69/V70 source checks passed on both hosts.

An initial origin wrapper reached and printed the same exact mathematical
unit obstruction, then exited rc one because its reporter expected a
first-stage source-denominator key for a transport-stage incompatibility.
Both failed-run byte streams are preserved as operator-failure evidence.
The repaired wrapper handles transport ancestry separately and is the sole
theorem source.

## Scope

This covers only raw `U=0` in the fixed normalized A3 q2-beta section, after
composition with the corrected V33 open.  It does not by itself repair the
separate staged-N13 denominator debt or automatically restore whole-H,
whole-B3, or fixed-A3 claims.  No other center coefficient, p/q-boundary
coefficient, dead stretch, F1 orbit, pole scale/data, whole TD6, SP-2,
landing, or JC2 conclusion follows.
