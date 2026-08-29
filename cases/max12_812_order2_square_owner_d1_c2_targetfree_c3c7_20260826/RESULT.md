# Producer result: D1 target-free primary-C2 cell, `3<=c<=7`

Date: 2026-08-26

Status: **EXACT-Q PRODUCER PASS WITH TWO FRESH GOOD-PRIME CONTROLS; HOSTILE
REVIEW REQUIRED BEFORE PROMOTION.**

## Exact result

After the frozen generic-square and D1 source gates, the complete seven
literal Faber equations are empty on the closed primary-C2 cell

```text
D(p*k0), ord(C)=c, 3<=c<=7,
ord(A)>=c, ord(R)>=c-1.
```

For every integer `c=3,...,7`, an independent cost-bounded census of all
four frozen binomial summands through absolute grade `T=10+2c`, repeated
with padded bounds, gives the following complete boundary source at
`ord(A)=c, ord(R)=c-1`:

```text
c=3:     AC, C2, R3, RC, all at grade 16;
c=4..6:  AC, C2, RC, all at grades 18,20,22;
c=7:     AC, C2, RC, k6*C, all at grade 24.
```

In every threshold `C2=(3/8)C^2/L^2` is the unique pole-two family.  The
other displayed families have pole one.  Every target begins at grade 28,
and `k2` is absent through all five registered ceilings.  Raising `ord(A)`
or `ord(R)` can only delay a family with positive `A` or `R` exponent; it
cannot add a lower-grade family, change the pole ceiling, or change target
timing.  This is the exact monotone source bridge to the displayed closed
tails, with no inversion of an `A` or `R` coefficient.

For `L=z^2+p/2`, each threshold independently rebuilds all seven literal
rows and an analytic Laurent source, checks their coefficientwise bridge,
and reconstructs the canonical pole-two numerator modulo `L^2`.  On the
finite etale root cover `p=-2*lambda^2`, the two root Faber functionals are
exactly

```text
N2(+lambda)=(3/8)C(+lambda)^2,
N2(-lambda)=(3/8)C(-lambda)^2.
```

The coefficient charts `D(c1)` and `D(c0)` exhaust nonzero linear `C`.
Both localized ideals contain `1` before radicals.  Omitting `C2` makes
both root terminals zero, so the decisive source column is required.

## AWS executions

| endpoint | tag | rc / wall / max RSS KiB / swap | stdout SHA256 |
|---|---|---|---|
| exact `Q`, Box02 | `max12_812_order2_square_d1_c2_targetfree_c3c7_q_box02_20260826T203500Z` | 0 / 0.21 s / 21760 / 0 | `0567178e69d23bdf79f55defefd4ba6729f237c95349ba2708cc416e9a32cf91` |
| `F_65519`, Box03 | `max12_812_order2_square_d1_c2_targetfree_c3c7_p65519_box03_20260826T203500Z` | 0 / 0.19 s / 21908 / 0 | same |
| `F_65521`, r6d | `max12_812_order2_square_d1_c2_targetfree_c3c7_p65521_r6d_20260826T203500Z` | 0 / 0.20 s / 21984 / 0 | same |

All validators returned `PASS_D1_C2_TARGETFREE_C3C7_CLOSED_TAILS`; all
engines returned rc 0 with zero swap.  Exact `Q` is the characteristic-zero
endpoint and the primes are independent software/host controls.  Every
generated program uses an ordinary polynomial ring and explicit standard
bases/reductions; no Singular `qring` occurs.

## Required c=8 split and firewall

This producer deliberately excludes `c=8`.  There `k6*C/L` first occurs at
grade 25, and its grade-26 moving-connection prolongation contributes a
pole-two term proportional to `-ell1*k6*C/L^2`.  The grade-26 functional is
therefore not the pure `C^2` square used above.  This is a source-timing wall,
not a missing threshold in this producer.

If hostile review confirms it, this producer closes only the displayed
target-free primary-C2 cell.  It says nothing about `c>=8`, another primary
or tied face, positive-order leading load, `p=0`, `k0=0`, the exact-square
zero section, an excluded terminal/global chart, fan exhaustiveness, order
two, maximum twelve, or JC2.
