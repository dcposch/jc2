# T-rs chart: grade-12 rho-unit certificate on D(k)

Date: 2026-08-26

Status: **EXACT-Q SATURATION PASS AND INDEPENDENT F65521 ELIMINATION PASS;
PRODUCER-TIER CHART LEMMA; HOSTILE REVIEW PENDING.**

## Result

On the actual total-Rees T-rs chart

```text
cs=rs*qcs,  c0=rs*qc0,  c1=rs*qc1,
```

let `J` be the complete grade-12 prefix ideal after saturation by `rs` and
write

```text
P1   = Tg10_1/rs,
P2   = Tg10_2/rs,
P3   = Tg10_3/rs,
P126 = Tg12_6/rs^2,
V    = 8*rho^2*qcs^2+3,
U    = 1+32*rho^2*qcs^2*V.
```

The exact source coefficients satisfy

```text
35*rs^2*k*U
 = 32768*P126 + 4096*P2 + 8192*qcs*P3
   + 12288*rho^2*qcs*P1.                         (1)
```

Consequently `35*k*U` belongs to `J`.  After localizing at `k`, the ideal
contains `U`, and therefore

```text
rho * (-32*rho*qcs^2*V) = 1 mod J_D(k).          (2)
```

Thus `rho` is a unit on this chart over characteristic zero.  As a redundant
scheme-theoretic check, adjoining `rho` and the inverse variable equation
`1-v*k` gives the unit ideal.  The special fiber `J+(rho)` separately
contains `k`.

## Independent registered lanes

| field / encoding | host | engine | peak RSS | swap | verdict |
|---|---|---:|---:|---:|---|
| exact `Q`, direct `sat(J,rs)` | Box02 | 0.03 s | 11,484 KiB | 0 | PASS |
| `F_65521`, inverse-variable elimination | r6d | 0.02 s | 11,804 KiB | 0 | PASS |

Both lanes used source archive
`5f9fe385066d1db5827f512b1732ef3493e6882bd3d88f61fd67456a76ad244a`,
passed all multiplication-back identities and two negative controls, emitted
no Singular diagnostic, wrote all four registered artifacts, and ended with
validator `PASS_T_RS_RHO_UNIT_V16`.

Critical result hashes are:

- exact-Q `RESULT.json`:
  `f30365d06e64bd94fbea17c9b1d5a0ab4ee364d883c55bbeb71fb863d342a905`;
- F65521 `RESULT.json`:
  `8a9962dfe4e610e186c3d493faece07fc1db53260bfff256c5f32308988edbe3`;
- common certificate artifact:
  `890aede0abfef6fae6a574e44fa0883415cd8943b2b6d81905f65ff6374d9e28`;
- common unit-ideal artifact:
  `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b`.

## Fail-closed predecessor record

- V12 stopped at multiplication-back because it assigned the specialized
  rather than total chart valuation to `Tg10_3`.
- V13 stopped in its compiler because its repair census expected two rather
  than the observed three registered occurrences.
- V14 stopped before compilation because its remote freeze check used the
  wrong working directory.
- V15 passed the core mathematics but its final unit-ideal line used an
  invalid three-argument Singular `std` signature; its validator rejected
  the diagnostics.
- V16 changes only that line to `std(std(J,rho),1-v*k)` and is the first
  fully validating endpoint.

None of the failed predecessors is evidence for the result.

## Scope firewall

This closes only the T-rs standard chart on `D(k)` for the complete
grade-12 prefix.  It does not cover the other total-Rees charts, prove the
global Gate-T implication, close order two, prove maximum twelve, or prove
JC2.  Promotion awaits independent hostile review of the coefficient pins,
chart valuations, saturation logic, explicit inverse, and scope.
