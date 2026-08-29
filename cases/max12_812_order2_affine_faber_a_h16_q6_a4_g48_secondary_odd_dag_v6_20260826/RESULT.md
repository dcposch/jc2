# Result: secondary odd functional and the H16 raw direct unit

Date: 2026-08-26

Status: **DUAL-AWS PASS; EXACT FIVE-TERM SECONDARY FUNCTIONAL.  TOGETHER
WITH V4 IT GIVES A RAW DIRECT UNIT ON `D(p*m)`.  REVIEW PENDING.**

For

```text
G=E(s)^2 P3+16 E(s) P5+96 P7,
```

the exact coefficient-only result is

```text
[s^48]G
 = 3 a p^2 m^2 r0 -3 a p^2 y^2
   -2 a p^4 d2 +(3/4) a p^6 d6
   -(5/2) p^2 m^3.                                  (1)
```

The earlier independently frozen functional is

```text
[s^48]F
 = (3/32) a p^2 m^2 r0 -(3/32) a p^2 y^2
   -(1/16) a p^4 d2 +(3/128) a p^6 d6
   -(1/64) p^2 m^3,                                 (2)

F=P7-E(s)^2 P3/32+E(s)^3 P1/64.
```

Subtracting the two exact sparse outputs gives the coefficient identity

```text
[s^48](G-32F) = -2 p^2 m^3.                         (3)
```

Both sides of (3) are coefficients of explicit combinations of raw source
rows.  Hence, when all row coefficients through grade 48 vanish, the left
side vanishes.  On `D(p*m)` the right side is a unit in characteristic zero.
This rules out the fixed integral `H=16,q=6,ord(a)=4` source family through
grade 48 without a projective `D(x)/D(y)` split or predecessor elimination.

Both AWS lanes completed in under three seconds with rc `0`, validator PASS,
zero swap, 665 abstract terms, nine valuation survivors, and five emitted
terms.  The `F65521` output has identical monomial support and the exact
coefficient reductions.  Three direct abstract raw-tail controls pass.  The
two old Singular slices evaluate (1) to `-3`; the two V5 first-functional-null
slices evaluate it to `-2`, exactly as independently recorded.

Exact-Q sparse output SHA:

```text
da16e1ce0a309f6fde5d280493f162f88b1ba4317f80219e2e1e407ca771a264
```

This result and (3) are scoped to the displayed fixed integral source family
and `D(p*m)`.  They do not establish rational regrading, neighboring `H,q,a`
walls, literal total-Rees coverage, factor-degenerate opens, order two,
maximum twelve, or JC2.

