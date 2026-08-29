# Producer — full ordered `T-c1` cubic exceptional-power certificate

Date: 2026-08-27

Status: **EXACT HAND CANDIDATE, AWAITING THE ALREADY-RUNNING BLIND FABLE5
RESIDUAL SEARCH / DIFFERENT-MODEL REVIEW.**

## Charged rows and provenance

Use the exact actual-total grade-10 rows

```text
Tg10_2 = (15/64)rho^2 cs^2 rs k +(3/8)rho^2 a1 c1
        +(5/1024)rs^3 k +(3/32)c1^2 +(3/8)a0 c0,

Tg10_4 = (3/32)rho^2 c1^2 +(3/32)c0^2.
```

Their frozen exact-Q file hashes are

```text
50c88196628dc04407c47c49059849f7f43265ade03afa13c9f27eecc1f928a6
6c33503e153a1adda56810a62db220f74b1dfd8c71158d1f3794f128773c503d
```

Fable5 has already reimplemented the corrected literal actual-total V0R1
emitter and independently reproduced both rows, plus their complete total
and frozen grade-10/11/12 families, in review SHA
`139ecb673995eff3c19f72da54b7a79d0a2a4c9c01f3b8600935f855704066fb`.
Thus the source-provenance input needed by this candidate is already
independently discharged; the new issue is the cubic combination and its
chart typing.

## Exact identity

Direct expansion gives

```text
c1^3
 = (32/3)c1*Tg10_2 - (128/3)a1*Tg10_4
   - rs*((5/2)rho^2 cs^2 k c1 + (5/96)rs^2 k c1)
   - c0*(4a0 c1 - 4a1 c0).                              (C1)
```

Indeed `(32/3)c1*Tg10_2` contains
`c1^3+4rho^2 a1 c1^2`; the latter term cancels exactly against
`(128/3)a1*Tg10_4`, whose remaining term is `4a1 c0^2`.  The displayed
`rs` and `c0` cofactors remove every other term.

## Chart type and candidate theorem

On the ordered fourth `J1=(rs,cs,c0,c1)` chart stratum, the honest base-
function equations are

```text
rs=cs=c0=0,
```

together with the `T-c1` Rees bilinears.  Identity (C1) is a direct
certificate of the reviewed staged form with

```text
exceptional power: c1^3
genuine localizer: 1
rho-unit factor:   1       (W=0)
ordered equations: rs, c0  (the identity does not need cs)
source rows:       Tg10_2, Tg10_4.
```

Kernel-as-saturation absorbs `c1^3`; `c1` is never inverted or called a
unit.  If the chart/stratum typing is independently confirmed, the honest
ordered `T-c1` chart stratum is empty for the entire registered total
family, not merely on `rho=0`.  The residual claimed in the earlier
repairable review arose from consuming `Tg10_2` alone and disappears after
the `Tg10_4` cancellation.

## Firewall

No conclusion is promoted from this producer note before different-model
review.  Even after confirmation it would close only the ordered registered
`T-c1` stage-one stratum.  It says nothing about `T-cs`, second-stage
`a0/a1`, the terminal receiver, remaining localizer complements, the
generic deck/square bridge, order two, maximum twelve, or JC2.
