# Symbolic cone of the corrected full-q2 witness

Date: 2026-08-26 UTC

Status: **DUAL-AWS EXACT WITNESS-CONE CERTIFICATE; hostile review of the
underlying lift is pending.**

Both AWS traversals independently reconstruct the 37-term corrected witness
with canonical SHA

```text
ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b
```

and emit literally identical certificate JSON, SHA

```text
ee0639963d1d4788e6a4ba04fbf1c6f98246921d19dc29f2822c0cb136eae9c2.
```

Normalize by `wt(la)=L`, and write

```text
alpha = wt(r_i)/L, beta = wt(q1)=wt(q0) over L,
delta = wt(q2)/L, t=T/L>0, h=H/L>0.
```

Apart from `la^20` and the automatically higher `la^20*tau`, the 35
remaining terms give these 15 distinct strict inequalities:

```text
beta + 2 alpha > 20       4 beta > 20
delta + 2 alpha > 20      delta + beta + 2 alpha > 20
delta + 2 beta + alpha > 20
delta + 3 beta > 20
2 delta + beta + alpha > 20
2 delta + 2 beta > 20     2 delta + 3 beta > 20
3 delta + alpha > 20      3 delta + beta > 20
3 delta + 2 beta > 20
4 delta > 20              4 delta + beta > 20
5 delta > 20.
```

The full JSON retains every coefficient and monomial, including repeated
forms; there are 17 forms total after adding target and positive-split target.

## Uniform control-2 consequence

At `alpha=15/2`, substitute

```text
beta=5+u, delta=5+v.
```

For every non-target term the exact difference from target weight becomes
`c+q*u+d*v`, with `c,q,d>=0` and either `c>0` or `q+d>0`.  Hence for

```text
alpha=15/2, beta>5, delta>5, T>0,
```

the unique least term is `la^20`.  In fact the 15 halfspaces reduce exactly
to the two necessary and sufficient strict inequalities `beta>5` and
`delta>5` on this alpha-slice: the first is forced by `beta+2alpha>20`, and
the second by `delta+2alpha>20`; all other listed inequalities follow.

A later `q2` activation in the already charged control-2 semantics has
`delta>beta`.  Therefore the corrected witness excludes **every later q2
valuation** over the full control-2 window

```text
alpha=15/2, 5<beta<6, delta>beta,
```

for the frozen axis/cusp and loads.  Together with the reviewed `q2=0`
witness, there is no gap from an identically zero versus later-activating
`q2` coordinate within this fixed source/load chart.

## Exact boundary faces of this witness

- `beta=5, delta>5`: six terms tie with `la^20`: `q1*q0^3` and the five
  old `q*r*r` terms.  This is the already identified beta face; the witness
  alone does not kill it.
- `delta=5, beta>5`: six terms tie: the five nonzero `q2*r*r` terms and
  `q2^4`.
- `beta=delta=5`: twenty non-target terms tie, the union above plus eight
  mixed quartics of total `(q,q2)` degree four.  The exact monomial list and
  coefficients are in the certificate JSON.

The beta ray, delta ray, and corner need full exact initial-ideal/torus
saturations if they are geometrically allowed.  No equality-face conclusion
is taken here.

## Dual AWS custody

- Box03 forward: tag
  `max12_912_order3_d1_double_root_control2_q2_cone_v3_20260826T034000Z_box03_forward`,
  PID `152186`, rc 0, empty stderr, 20,856 KiB maximum RSS, zero swap.
- r6d reverse: tag
  `max12_912_order3_d1_double_root_control2_q2_cone_v3_20260826T034000Z_r6d_reverse`,
  PID `219931`, rc 0, empty stderr, 20,392 KiB maximum RSS, zero swap.

Both ran under 2-GiB / 600-s caps after hash-checked source registration and
returned the identical certificate bytes despite opposite traversal order.

## Firewall

This is the complete strict halfspace region of one explicit membership
witness, not a complete Groebner cone or Newton fan.  It freezes the source,
axis/cusp and loads `k=nu=0,mu=2/3`.  It does not cover moving axis/cusp,
moving loads, another normal coefficient, equality faces, a formal arc,
the whole double-root locus, D1, or JC2.
