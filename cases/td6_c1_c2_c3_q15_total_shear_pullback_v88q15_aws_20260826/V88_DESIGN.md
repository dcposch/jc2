# TD6 V88 design: exact q15 target-shear coordinate and V87 pullback

Date: 2026-08-26

Status: preregistered design; no V88 result is claimed here.

## Objective

V87 works with

```text
p(t)=t^15,
q_bar(t)=t+sum_{e=2..14,16..24} q_e*t^e+t^25
```

and explicitly fixes q15 to zero. The prior q15 CURRENT marker is only a
square-zero check. The missing nonlinear custody is an exact two-sided map
between the unnormalized q15 family and this normalized slice, including the
section coefficients which target shear moves.

## Exact triangular map

Let `b` be the raw coefficient of `t^15` in q. For every coefficient of the
two source polynomials/sections `f,g`, define

```text
p_raw = p_bar = t^15,
q_raw = q_bar + b*p_bar,
f_raw = f_bar,
g_raw = g_bar + b*f_bar.                         (2.1)
```

Here `f_bar` is embedded in the larger g rectangle by the literal monomial
map `(i,j) -> (i,j)` for `0<=i<=15,0<=j<=60`; all other g coefficients are
unchanged. The inverse is

```text
b     = [t^15]q_raw,
q_bar = q_raw - b*p_raw,
f_bar = f_raw,
g_bar = g_raw - b*f_raw.                         (2.2)
```

Both maps are integral polynomial maps, mutually inverse term by term, and
triangular with Jacobian determinant one. No localization, q15 division, or
tangent approximation occurs. This is the total coordinate form of the
lower target shear `q -> q-b*p`, `g -> g-b*f`.

## Literal transport check

The V88 client must evaluate every original unsolved transport row after
(2.1), not merely compare compiled CURRENT rows.

- In the X chart, transport is linear in the global coefficients. The added
  `b*f_bar` contributes `b` times the f X-boundary. Since that boundary is
  exactly `p=t^15`, the g boundary becomes `q_bar+b*t^15=q_raw`.
- In the F1 chart, g imposes rows at exponents `<=-25`; every embedded f row
  there is zero because f already vanishes below its `-15` leading face.
  Thus the fixed g F1 pattern is unchanged.
- At the r9 pole, g imposes rows at exponents `<=-5`; every embedded f row
  there is zero because f has cutoff `-3`. Thus the fixed g pole pattern is
  unchanged.

Promotion requires exact evaluation of all original rows over the
untruncated 23-variable ring and equality to the raw RHS, including exactly
one q15 source at `('g','X',0,15)`. Omitting this RHS source while retaining
the section shear must fail.

## Raw receiver invariance

The direct boundary derivative transforms as

```text
q_raw' = q_bar' + b*p',   p'=15*t^14.
```

FIRST is exactly invariant:

```text
f*(q_bar'+b*p') - p'*(g_bar+b*f)
  = f*q_bar' - p'*g_bar.
```

The CURRENT expression used for genuine P12 is also exactly invariant. Its
extra b coefficient is

```text
f1*f2' + 2*f2*f1' + 3*f3*p'
- 3*p'*f3 - 2*f1'*f2 - f2'*f1 = 0.              (2.3)
```

Therefore the V88 client must build raw bands by (2.1), include the direct
`15*b*t^14` term, and prove that all 38 packed raw FIRST maps and literal raw
P12 are byte-for-byte equal as exact polynomials to their V87 normalized
counterparts. Two negative controls are required: omit `b*f` while retaining
`b*p'`, and omit `b*p'` while retaining `b*f`; each must change raw FIRST.

## V87 consequence after pullback

If those checks pass, pullback of the frozen V87 identity along (2.1) gives
the same exact identity with no b remainder:

```text
U^12*H^3*B3
  = a_P*P12_raw + sum_i a_i*FIRST_i,raw
    + F*h_F + sum_{e != 15} q_e*h_e.
```

Thus q15 is an arbitrary orbit coordinate, not a transverse positive-
valuation generator. The narrow DVR exclusion then allows q15 to have any
valuation, including zero, while still requiring positive valuation of `F`
and all 22 quotient q coordinates. This does not cover a unit value of any
of those 22 transverse coordinates.

## Fail-closed acceptance gates

1. Use an untruncated exact polynomial ring in the 22 V87 q variables and b;
   any q-dependent inverse fails closed.
2. Verify the two-sided coefficient map on all `(16*61)+(26*101)=3602`
   global section coordinates and record the 976 shared monomial slots.
3. Evaluate every original transport equation after the map and require one
   and only one q15 boundary source.
4. Check both exact receiver cancellations, all 39 source equalities, the
   two receiver omissions, and the transport-q15 omission.
5. At b=0 reproduce the frozen V87 full source hashes; consume V87 only via
   its validated FREEZE/EVIDENCE/SOURCE custody.
6. Audit that (2.1)-(2.3) introduce no denominator and do not change the V87
   registered `U,H,B3` localization.
7. Run byte-identical bounded exact clients on two AWS hosts.

## Scope firewall and next routing step

A pass closes only q15/orbit custody on this normalized fixed-p component.
It does not cover unit fibres of the 22 transverse q variables, dead stretch,
correction, pole/orbit, moving centers, deck/torsion, other boundary data, a
total-Rees chart, whole fixed A3, TD6, SP-2, or JC2.

After V88, the next q step is a projective/ordered unit-q atlas: on each chart
`D(q_e)` for a transverse q coordinate, seek a literal total-F certificate
allowing only `q_e` as the new registered unit. V87 itself supplies no such
unit-q certificate.
