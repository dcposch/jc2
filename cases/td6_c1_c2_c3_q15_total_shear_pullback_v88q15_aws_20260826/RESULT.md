# TD6 V88Q15 exact total target-shear pullback result

Date: 2026-08-26

Producer verdict: **PASS on Box02 and r6d.** Independent hostile review of
V88 is not yet incorporated. The V87 hostile review found no defect in the
represented all-q identity but requested a separate V87-to-V86 q2
specialization custody check; that repair does not enter the algebra below.

## Exact two-sided coordinate map

Let

```text
p=t^15,
q_bar=t+sum_{e=2..14,16..24} q_e*t^e+t^25,
b=q15.
```

On all global section coefficients define

```text
q_raw=q_bar+b*p,  f_raw=f_bar,  g_raw=g_bar+b*f_bar.       (1)
```

The f rectangle embeds monomial-for-monomial into the g rectangle. The
inverse is

```text
q_bar=q_raw-b*p,  f_bar=f_raw,  g_bar=g_raw-b*f_raw.       (2)
```

These are mutually inverse integral polynomial maps, triangular with
Jacobian determinant one. The emitted inventory checks all 3,602 global
coefficient coordinates: 976 f coordinates, 2,626 g coordinates, and
exactly 976 shared monomial slots. No q15 or other factor is inverted.

## Literal transport custody

The client compared the shared part of every original unsolved g transport
row with the corresponding f row: all 4,743 g rows match, against the 1,764
f-row inventory. Under (1), the only nonzero added boundary RHS is exactly

```text
('g','X',0,15) = b.
```

All g F1 and r9-pole boundary rows receive zero from the embedded f section,
so their fixed patterns are unchanged. Omitting the q15 transport RHS leaves
that unique nonzero residual and fails the registered negative control.

## Exact raw-source invariance

With direct derivative

```text
q_raw'=q_bar'+15*b*t^14=q_bar'+b*p',
```

all 38 packed raw FIRST maps and the literal degree-12 raw CURRENT/P12 map
are exactly equal, as polynomials over the untruncated 23-variable ring, to
their normalized V87 counterparts. The cancellations are identities, not
square-zero tests. In particular FIRST uses

```text
f*(q_bar'+b*p')-p'*(g_bar+b*f)=f*q_bar'-p'*g_bar,
```

and the b part of CURRENT is

```text
f1*f2' + 2*f2*f1' + 3*f3*p'
- 3*p'*f3 - 2*f1'*f2 - f2'*f1 = 0.
```

The resulting raw source has exact q15 degree zero. Omitting the section
shear while retaining direct q15 changes 15 FIRST rows; omitting direct q15
while retaining the section shear also changes 15 FIRST rows. Both first
failures occur at `('X-2',14)`.

All 39 normalized/raw source hashes reproduce frozen V87. The 9,827 raw
source `E3` coefficients have common denominator exactly

```text
C*U-3*U^3=U*H,
```

and the target-shear map introduces no denominator.

## Pullback and DVR consequence

Exact source invariance pulls the frozen V87 identity back along (1) with
q15 remainder zero:

```text
U^12*H^3*B3
  = a_P*P12_raw + sum_i a_i*FIRST_i,raw
    + F*h_F + sum_{e=2..14,16..24} q_e*h_e.
```

Consequently, on the same `D(U*H*B3)` fixed-p source component, q15 is an
arbitrary target-shear orbit coordinate and may in particular be a DVR unit.
The V87 contradiction still requires positive valuation of `F` and each of
the other 22 transverse q coordinates. No unit chart for those 22 variables
is supplied.

## Evidence hashes

- source archive:
  `46dee1d1333c721ef7776849603c81053466d7310e57c453fef6587b1f8871a6`;
- V88 client:
  `402dc792ac565dd1da40a26df4d8257fa02e571caf2bc00740280467e6c99169`;
- coefficient-map inventory:
  `602b3a03c601bad6c489851b0e948bcae39129ef0b1a98678a33df7104582600`;
- original-row transport audit:
  `807a9a65373263b37962f5efd7dacca04d19387ce845ab6bc8a1d17f022ee2a7`;
- 39-source invariance inventory:
  `5cb919b9d4a8760d24111e786eaa277cc7c900be96d0e1923863ef3557a0fdbb`;
- exact-result record:
  `e6adc9867f37cc7280cdbe97ea77d4eada1ab2582021db267b05500fa14c9fc8`;
- byte-identical mathematical stdout:
  `eb4eede4a1a9c6dd9d361be793ddfe60317c6899c02dc2f52e7e88d943de578f`.

## AWS custody

Both clients returned `rc=0` with the distinct
`TD6-V88Q15-EXACT-TOTAL-TARGET-SHEAR-PULLBACK PASS` banner. Stdout and all
four mathematical output files are byte-identical.

- Box02: 2:15.51 elapsed, 298,324 KiB maximum RSS, zero swap;
- r6d: 2:17.37 elapsed, 298,044 KiB maximum RSS, zero swap.

## Scope firewall

This proves only exact q15 orbit custody on the fixed `p=t^15`, normalized
three-center component and transfers the frozen V87 identity to that raw
q15 family. It does not cover a unit among the other 22 transverse q jets,
dead stretch, correction, orbit/pole, moving centers, deck/torsion, other
boundary data, a total-Rees chart, whole fixed A3, TD6, SP-2, or JC2.
