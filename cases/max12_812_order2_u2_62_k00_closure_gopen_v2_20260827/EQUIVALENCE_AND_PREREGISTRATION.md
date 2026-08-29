# K00 closure V2: eventual-open saturation acceleration

Date: 2026-08-27

Status: **EXACT IDEAL IDENTITY AND PREREGISTERED ALGORITHM.  NO ENDPOINT.**

Let

```text
Q=(Lambda)+M_K00,             g=C6*k10*Jdet,
K=(I:Lambda^infinity:Jdet^infinity),
H=(K+Q):g^infinity.
```

The V1 ideal can equivalently be computed as

```text
Kopen=I:(Lambda*g)^infinity,
Hopen=(Kopen+Q):g^infinity.                         (1)
```

Indeed saturation by `g` is contraction from `A_g`.  In `A_g`, `Jdet` is a
unit, so the intermediate `Jdet` saturation has no effect after extension.
Saturation/localization commute, and `Lambda` and `g` generate principal
multiplicative sets, hence

```text
(I:Lambda^infinity:Jdet^infinity) A_g
 = (I:Lambda^infinity) A_g
 = (I:(Lambda*g)^infinity) A_g.
```

Adding `Q` after these source operations and contracting from `A_g` proves
`H=Hopen`.  No boundary/core equation is imposed before source saturation.
This is not the invalid restriction-first ideal `(I+Q):(Lambda*g)^infinity`.

The compiler is a hash-gated transformation of frozen V1: it changes only
the two source saturations to (1), retains the invariant-core row checks,
retains the explicit restriction-first unit as a negative control, and
retains the same final basis/lift evidence.

First race: characteristic 65519 on AWS r6d, 30-minute / 64-GiB cap.  It is
an algorithm screen and finite-field software control.  If it reaches an
endpoint quickly, freeze and launch an exact-Q V2 lane on a distinct AWS
host.  Timeout, failure, missing marker, or certificate failure is no
verdict.  Both outcomes have exactly the limited V1 scope.
