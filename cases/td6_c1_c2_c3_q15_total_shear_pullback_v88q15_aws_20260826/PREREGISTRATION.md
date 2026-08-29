# TD6 V88Q15 exact total q15 target-shear pullback

Date: 2026-08-26

Status at freeze: producer preregistration; no result claimed.

## Exact question

Starting from the frozen V87 normalized family with `p=t^15` and

```text
q_bar=t+sum_{e=2..14,16..24} q_e*t^e+t^25,
```

introduce an unrestricted coefficient `b=q15` and the literal target-shear
coordinate map

```text
q_raw=q_bar+b*p,  f_raw=f_bar,  g_raw=g_bar+b*f_bar.
```

Prove this is an exact two-sided integral coordinate map on the complete
global coefficient rectangles and that the raw transport, FIRST, and genuine
P12 source pull back exactly to V87, with no b remainder.

## Acceptance gates

1. Work over the untruncated sparse ring in all 23 variables `q2..q24`; any
   q-dependent inverse fails closed.
2. Verify the triangular map and inverse on all 3,602 global coefficients,
   including exactly 976 shared f-to-g monomial slots.
3. Compare the shared part of every original g transport row with the
   corresponding f row. Require that the only nonzero induced raw boundary
   is `('g','X',0,15)` with coefficient b; F1 and pole patterns must remain
   fixed. Omitting that boundary source must fail.
4. Build normalized V87 bands with all 22 transverse q coordinates, form
   raw bands by the exact section shear, and include `15*b*t^14` in `q'`.
   Require equality of all 38 raw FIRST maps and literal P12 with their
   normalized counterparts.
5. Omitting the section shear while retaining direct q15, and omitting
   direct q15 while retaining the section shear, must each change raw FIRST.
6. At b=0 reproduce the frozen V87 full source hashes. Audit source
   denominators against `U,H,B3`; neither F nor a q variable may be inverted.
7. Run two registered AWS clients and require byte-identical mathematical
   stdout and output hashes.

## Consequence and scope

A pass makes q15 a proved arbitrary orbit coordinate on this fixed-p
component, including q15 units. Pullback of the frozen V87 identity then has
no q15 term. It does not cover a unit among the other 22 transverse q
coordinates or any dead/correction/pole/center/deck/torsion/boundary chart,
whole fixed A3, TD6, SP-2, or JC2.
