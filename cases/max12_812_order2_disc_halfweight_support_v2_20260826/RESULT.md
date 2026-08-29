# Direct-`m` discriminant half-weight support V2 result

Date: 2026-08-26

Status: **dual-AWS producer endpoint PASS; initial Kuranishi support only.**

## Frozen inputs

- package `FREEZE.sha256` SHA-256:
  `3576b8ca6692ed1d1d47319436ae6b85e981cabf8b90e4155c794b75797c9722`;
- exact-Q tag:
  `max12_812_order2_disc_halfweight_support_v2_q_20260826T063500Z_box03`;
- characteristic-32003 tag:
  `max12_812_order2_disc_halfweight_support_v2_p32003_20260826T063500Z_r6d`.

Both frozen compilers returned zero.  Both Singular engines returned zero and
the fail-closed validators printed
`validator=PASS_DISC_HALFWEIGHT_SUPPORT_V2`.

## Exact endpoint

After saturation by `m`, the `kappa != 0` chart is the unit ideal.  In the
`kappa=0` chart, localizing away from `e=0` is also the unit ideal.  On
`D(b*m)` the raw triple-root K2 scheme has exact-Q standard basis

```text
kappa,
e,
6*b*y^2 + m^3 + 12*h*y,
b*m^3 - 6*h^2,
m^6 + 12*h*y*m^3 + 36*h^2*y^2.
```

It is nonreduced.  Its radical agrees, in both directions, with

```text
kappa = 0,
e = 0,
h = -b*y,
m^3 + 6*h*y = 0,
```

equivalently `e=kappa=0`, `h=-b*y`, and `6*b*y^2=m^3` on `D(b*m)`.
The characteristic-32003 run gives the same dimensions, unit tests, raw
scheme shape, radical, and two containment sentinels.

## Firewall

This classifies the reduced support (and records the nonreduced scheme) of
the seven-row **K2 initial obstruction** on the stated open chart.  It does
not prove that the surviving triple-root direction lifts to K3, satisfies
the terminal/Taylor source rows, or yields an order-two solution.  It also
does not cover `b=0` or `m=0`; those were deliberately saturated away.

## Custody

- exact-Q stdout SHA-256:
  `7de0a587270481736b0b85b76cffce761567d7778d014cc0ddd4cd557ed0cb26`;
- characteristic-32003 stdout SHA-256:
  `9dca3aaaaa628083f60c553823f67d9decfc4664e588828ffdb27be11f72336d`;
- each validation file SHA-256:
  `1bc42aff3080b42343b09b29a8d1d384f7bcebda0bbe1d29da528caedbff3437`.

The complete retrieved-file manifest is `RESULTS.sha256`.
