# Lambda-nonzero unit-S face: the order-five pole is exactly the reviewed D12 product

Date: 2026-08-28  
Lane: Sol Ultra coordinator, exact desk theorem  
Status: **PROVISIONAL; DIFFERENT-MODEL HOSTILE REVIEW REQUIRED**

## Verdict

The strengthened unit-`S` expansion from the order-four theorem has one
possible pole at relative order five.  Its residue is, up to a nonzero local
unit, exactly

```text
J*(20*c2*J+3*N),
```

the product already forced divisible by `A` by the reviewed residual D12 row
`(R12r)`.  Hence the complete characteristic is regular through relative
order five as well.  This face calculation supplies no new cut beyond the
existing determinant cascade.

The result strongly lowers the priority of continuing unit-`S` face-pole
expansion in isolation.  Raw receiver windows, endpoint coupling, or a proof
that a later local residue is not merely the next determinant row are cleaner
discriminators.

## 1. Abstract order-five pole

At one simple `A`-root use the notation from the frozen order-four packet and
write

```text
epsilon^-4 F
 = L^4+epsilon*L^3*J1+epsilon^2*L*H2
      +epsilon^3*C3+epsilon^4*D4+O(epsilon^5).
```

Expanding every characteristic mode born by relative order five shows that
the only negative `L`-power is

```text
L^-1*H2*(3*C3/4+5*c2*tau^2*H2/32-3*J1*H2/16).       (1)
```

The `c4` mode is integral because it multiplies `F`; the `c6`, `c8`, and
newborn `c10` modes are also regular.  No omitted mode can enter this order.

## 2. Exact identification with the D12 row

Expand the literal `F0,...,F7` prefix under the reviewed root lifts

```text
QS+4U=A*ell,
2048F6-2SP1-4QSU-8U^2=A*e1.
```

Put, at `X=alpha`,

```text
a=A', s=S, q=Q, p=P1, f7=F7,
Jc=p-s*q^2/2,
Nc=8192*f7-e1*s+q*Jc.
```

At the face root `tau0=-4a/s`, exact cancellation of all jet terms gives

```text
H2(tau0)=-4*a^5*Jc/s^5,                              (2)

(3*C3/4+5*c2*tau^2*H2/32-3*J1*H2/16)|tau0
  =-a^7*(20*c2*Jc+3*Nc)/(2*s^7).                    (3)
```

Therefore the numerator of the possible pole (1), evaluated at its unique
face root, is

```text
2*a^12*Jc*(20*c2*Jc+3*Nc)/s^12.                     (4)
```

All displayed factors outside the campaign product are units: `a` and `s`
are nonzero on the squarefree lambda-nonzero branch.  The independently
reviewed residual D12 formula is

```text
g12^- = Jc*(20*c2*Jc+3*Nc)/(8388608*A).
```

Polynomiality therefore gives `A | Jc*(20*c2*Jc+3*Nc)`.  At every root the
value in (4) is zero, so the numerator in (1) is divisible by the linear face
factor `L`.  The relative-order-five coefficient is regular.

## 3. Reproduction, dependencies, and scope

Run

```text
python3 cases/ggv_8_28_upper_endpoint_lambda_nonzero_unit_s_order5_row_identity_20260828/verify_unit_s_order5_row_identity.py
```

Expected marker:

```text
PASS_EXACT_UNIT_S_ORDER5_ROW_IDENTITY
```

The checker pins the frozen order-four engine at SHA-256
`a4e6f18b718fb99495aaf048a4b104109ef20b320b89e2016c50dfb63a608e40`.
It independently reconstructs the literal root jets through `F7`, verifies
(1)--(4), includes all born modes, and detects an `8192 -> 8191` F7-load
mutation.  It uses only Python's standard library and no heavy local algebra.

This theorem consumes the reviewed exact-`D=0`, active-`c2` D12 cascade.  It
does not prove raw-window compatibility, any later coefficient, the endpoint,
a Keller theorem, or JC2.  It also does not claim that every future face pole
must be a previous determinant row; establishing or refuting such a general
identity is the natural theorem-interface successor.
