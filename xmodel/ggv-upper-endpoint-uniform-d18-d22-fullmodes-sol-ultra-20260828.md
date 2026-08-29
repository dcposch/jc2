# Uniform full-mode continuation through the `D22` endpoint

Date: 2026-08-28  
Packet: `cases/ggv_8_28_upper_endpoint_uniform_d18_d22_fullmodes_20260828/`

## Producer verdict

**PASS: the complete fixed upper branch-P endpoint fixture has no
characteristic-zero field point, conditional on the independently reviewed
complete-mode prefix through D17.**

This is the first producer calculation to reach the literal endpoint from
the uniform full fixture.  It retains all nine characteristic modes.  In
particular, `c16` is not set to zero; it remains governed by the reviewed
centered D16 relation.

## Starting relations

Use the reviewed D16/D17 notation

```text
B = F8-Y/2-TZ/8-QV/16-R^2/4,
C = F9-QR/2-TV/16-YZ/8,

3B^2+4c8B+8c16 = 8A^2M,
(3B+2c8)C-2M   = 4A^2N,
A=X^4-1.
```

No square-root sheet, gauge, carrier, or lower scalar equation is selected.

## D18 and D19

Define

```text
E = F10-CZ/4-Q^2/4-RT/2-VY/16.
```

After the complete D16/D17 substitutions, the exact negative part is

```text
polar(g18)
 = c18/A^3
   + ((3B+2c8)E/4 + 3C^2/8 - N/2)/A^2.
```

At a hypothetical raw point `G18` is a polynomial in the literal degree
window `X^2..X^6`.  Clearing the displayed expression gives

```text
c18 + A*((3B+2c8)E/4 + 3C^2/8 - N/2) in (A^3).
```

Reducing modulo `A` first forces the scalar `c18=0`; the remaining numerator
must then lie in `(A^2)`.  Write

```text
(3B+2c8)E/4 + 3C^2/8 - N/2 = A^2 O.              (D18)
```

The causal firewall is exact.  If `c18` is provisionally retained, its D19
predecessor contribution is `+9c18 A'/A^2` and its same-row contribution is
`-9c18 A'/A^2`; they cancel.  D19 does not independently kill `c18`.

Now define

```text
H = F11-EZ/2-QT/2-RY/2-CV/8.
```

Then

```text
polar(g19)=((3B+2c8)H/4 + 3CE/4 - O/2)/A^2,
(3B+2c8)H/4 + 3CE/4 - O/2 = A^2 P.                (D19)
```

## D20 and D21

Put

```text
J = F12-CR-EV/4-EZ^2/16-3HZ/4-QY/2-T^2/4.
```

The next exact polar coefficient is

```text
polar(g20)
 = c20/A^4
   + ((3B+2c8)J/4 + 3CH/4 + 3E^2/8 - P/2)/A^2.
```

The literal polynomial `G20` window similarly forces `c20=0` first and then

```text
(3B+2c8)J/4 + 3CH/4 + 3E^2/8 - P/2 = A^2 S.       (D20)
```

Again the successor does not supply the mode kill: at D21 the complete
`c20` predecessor and same-row pieces are respectively
`+12c20 A'/A^3` and `-12c20 A'/A^3`.

Finally set

```text
K = F13-CQ-2ER-EVZ/16-3HV/8-3HZ^2/16-JZ-TY/2.
```

Then

```text
polar(g21)=((3B+2c8)K/4 + 3CJ/4 + 3EH/4 - S/2)/A^2,
(3B+2c8)K/4 + 3CJ/4 + 3EH/4 - S/2 = A^2 U.        (D21)
```

The literal `G18,G19,G20,G21` windows have dimensions `5,3,2,1` and
independently reconstructed same-row ranks `5,3,2,1`, each with nullity
zero.  Their row hashes and all column images are serialized in `RESULT.json`.

## Endpoint contradiction

Define the last defect

```text
ELL = F14-CT-2EQ-ERZ/2-EV^2/64-3HR-3HVZ/16-HZ^3/64
      -JV/2-3JZ^2/8-5KZ/4-Y^2/4.
```

After D18--D21, the complete weight-22 continuation has

```text
polar(g22)
 = ((3B+2c8)ELL/4 + 3CK/4 + 3EJ/4 + 3H^2/8 - U/2)/A^2.
```

The full coefficient also has regular terms, but no term below `A^-2`;
the checker records exact A-exponent support `{-2,0,2,4,6,8}`.  There is no
raw `G22`.  With the literal determinant convention,

```text
D22_raw = -L22(g22),
L22(R)  = -40 A^3 A' R - 8 A^4 R'.
```

Writing `g22=q+W/A^2`, with `q,W` polynomial, gives

```text
D22_raw = 8A*(5A^2 A' q + A^3 q' + 3A'W + A W') in (A).
```

An optional endpoint homogeneous term `c22/A^5` is annihilated by `L22`
and changes nothing.  The authoritative raw row has target polynomial
`D22=1`.  Since the nonconstant polynomial `A=X^4-1` cannot divide `1`, the
hypothetical point cannot exist.

## Custody and scope

The checker pins the authoritative raw fixture SHA
`ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0`
and recursively pins the D16/D17 checker/result.
It reconstructs the complete Laurent recurrence and literal raw window maps
using standard-library `Fraction` arithmetic.  No CAS, AWS result, Lean
state, endpoint carrier normalization, or lower-window deletion is used.

The promoted scope, if hostile review passes, is only:

```text
no characteristic-zero field point of the complete fixed upper branch-P
endpoint fixture satisfies D4=...=D21=0 and D22=1.
```

It is not scheme-theoretic emptiness, an unrestricted branch-P theorem, a
claim about another GGV branch, a Keller-pair theorem, or JC2.
