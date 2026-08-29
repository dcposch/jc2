# K00 closure: exact quadratic normal compatibility

Date: 2026-08-27  
Author: Sol coordinator lane  
Status: **EXACT DESK-SCALE NORMAL-FORM IDENTITY; HIGHER NORMAL ORDER OPEN**

## Result

Use the frozen seven ordinary tails and put `c=C6`.  Around the K00
coefficient core introduce transverse coordinates

```text
d0=256*C0-c^4,   d1=C1,   d2=16*C2-c^3,
d3=C3,           d4=8*C4-3*c^2,   d5=C5.
```

Set the three scaled lower loads to zero, as they are on the `Lambda=0`
pure coefficient slice, and expand each tail `r_l` in the ideal
`(d0,...,d5)`.  Every constant and linear term vanishes.  If `Q_l` is the
quadratic normal form, its term counts for `l=1,...,7` are

```text
8, 11, 9, 12, 8, 0, 6.
```

Exact coefficient arithmetic over `Q[c,d0,...,d5]` gives

```text
Q5 = -(3*c^2/128)*Q1 - (c/8)*Q3,
Q6 = 0,
Q7 = -(c^3/512)*Q1 - (c^2/128)*Q3.             (1)
```

Thus the terminal row has no new pure quadratic normal class after the odd
rows `1` and `3` are imposed.  In particular, no closure-first K00 decision
can be justified from a quadratic `Phi7` separator: the first possible
separation lies at higher coefficient-normal order or in a mixed
`Lambda`/load term.  This explains why restriction-first `Phi7` kills the
literal section while the closure-first saturation remains substantially
harder, and it gives the next normal-jet compiler three exact syzygies to
remove before elimination.

## Replay and custody

```sh
python3 cases/max12_812_order2_u2_62_k00_quadratic_normal_v6_20260827/replay_k00_quadratic_normal_v6.py
```

The replay pins `tails.json` at SHA-256
`d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`,
performs the K00 coordinate substitution with `Fraction` arithmetic, checks
the zero constant/linear census, and verifies all three identities in (1)
coefficientwise.  It uses no CAS, AWS, network, or `jc2-lean` access.

## Firewall

This is the pure coefficient-normal quadratic slice only.  It does not
include the mixed `Lambda^2*k10`, `Lambda^6*k6`, or `Lambda^10*k2` terms,
does not compute `I:Lambda^infinity:Jdet^infinity`, and proves neither
existence nor nonexistence of a K00 arc.  It does not close the receiver,
Gate T, order two, maximum twelve, or JC2.
