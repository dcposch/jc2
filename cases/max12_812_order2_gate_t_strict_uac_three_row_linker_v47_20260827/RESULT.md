# V47 fail-closed direct three-row linker

Date: 2026-08-27

Status: **PASS — PRODUCER-CHECKED AND PROVISIONAL.  ENDPOINT REPLACEMENT IS
WITHHELD PENDING DIFFERENT-MODEL HOSTILE REVIEW.**

## Exact result

The desk verifier emitted

```text
PASS-GATE-T-STRICT-UAC-THREE-ROW-LINKER-V47
```

for exactly twelve registered low-band baseline closed tails and four raised
closed subtails.  It does not accept an arbitrary strict unique-`AC` contact.
Every accepted manifest pins the tuple as `(a,d,c=a+d,r_min)`, the grades
`G=10+a+c` and `T_C2=10+2c`, a complete aggregated polar inventory hash,
the frozen D1 endpoint authority/review hashes, and its explicit total-to-D1
leading alias/scaling map.

Endpoint localization and theorem type are resolved from the pinned endpoint
authority and retained per manifest: `D(p*k10)` for the two `d=1` families
and `D(p*k0)` for the low-`a` `d=2,3` family, always at arcwise/set-theoretic
strength.  The direct lemma's smaller algebraic dependence on `rho` does not
remove either upstream unit-load chart factor.

The twelve baselines are

```text
d=1: a=2,3,4,5,6;
d=2: a=2,3,4,5,6;
d=3: a=5,6.
```

The additional raised tails are

```text
(a,d,r_min)=(1,2,3),(2,3,5),(3,3,5),(4,3,5).
```

The verifier derives both lists from the wall policy rather than accepting a
second hard-coded expected list.  It also proves the closed-tail extension:
raising `r` only delays `R`-bearing primitives, while all `R`-free grades are
unchanged.

## Literal rows and theorem type

On the chart

```text
L=z^2-rho^2,
A0=A1*z+A0c,
C0=(C1*z+C0c)/2,
```

the pinned primitive coefficients `3/4` for `AC/L` and `3/8` for
`C^2/L^2` give

```text
g1=(3/8)(A0c*C1+A1*C0c),
g2=(3/8)(A0c*C0c+rho^2*A1*C1),
g4=(3/32)(C0c^2+rho^2*C1^2).
```

Four independently expanded polynomial syzygies prove, in the radical sense,
that `g1=g2=g4=0` forces `C0c=C1=0` on
`D(rho) intersect (D(A0c) union D(A1))`.  This is set-theoretic and
normalized-DVR-arc emptiness, not a scheme-theoretic unit ideal.  The row
bridge is literal:

```text
Phi1=h1, Phi2=h2, Phi4=h4+(P/2)h2.
```

The full moving-`P` simple-pole recurrence cancels every other pole-one
contributor from `Phi4`.  Acceptance requires that `AC/L` be the unique
primitive through `G`, that the only pole at least two through `T_C2` be the
pinned `C^2/L^2`, and that `G<28`, `T_C2<32`.

## Custody and controls

The verifier independently re-enumerated and aggregated all four binomial
summands, compared all 71 accepted inventory entries to the pinned support
miner, and ran a pad-`+1` sentinel per manifest.  It pins the 569 tails, the
tail emitter, V46 source-naturality schema/review, and every consumed D1
promotion/review.  Only V46 `V0,V1,V3,V4` is consumed; no old mixed
shifted-root display is used.

Eight negative contacts reject, including `RA^2`, persistent `A^3`, the
`a=7` `k6` tie, and a `k2`/target-wall cell.  Twelve required mutations fire:
both row normalizations, the `C0` factor two, `RA^2` misclassification,
uniqueness deletion, both target walls, stage-zero-name substitution,
`rho=0` row relabelling, `h4` for `Phi4`, the AC coefficient, and an
ambiguous tuple.

Frozen producer hashes:

```text
b1770cc0254098343c27600136f0ec1d95084623a4f48eed5216409106703ab2  SCHEMA.json
070d5a96627ac300f87791b9386e809de21b52317581b01731cde5dc55c7ecaa  GENERATED_MANIFESTS.json
903c6932a53ec5c0a1d2f7e7a7266135131fdc23512e8562f2b5b36ff20c0111  verify_three_row_linker.py
a8be0c67b113f0c92e077fc2ff3ef591edee6b859f2e83ed1abca38ec44c367b  run_v0_v9/result.json
```

## Firewall

Until different-model review, this artifact replaces no endpoint step.  Even
after review it can replace only the root-allocation step on the sixteen
listed closed tails; it neither upgrades the frozen endpoint theorem type nor
replaces a scheme-theoretic claim.  It does not cover the rejected `r=3,4`
part of `(a,c,r)=(2,5,r)`, exceptional `E`, `a=7` or later load cells, target
walls, `rho=0`, equality faces, positive-order leading loads, `k=0`, staged
Rees charts, the terminal receiver, a strict-fan union, `G2-PSC`, `G2-BD`,
Gate T, order two, maximum twelve, JC2, or a counterexample.
