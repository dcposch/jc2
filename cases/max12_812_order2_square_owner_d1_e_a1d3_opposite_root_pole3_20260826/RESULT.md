# Result: exceptional D1 `E=(a,d,r)=(1,3,>=2)`

Date: 2026-08-26

Status: **TRIPLE-AWS EXACT-Q PRODUCER PASS; AWAITING HOSTILE REVIEW.**

## Exact producer theorem

After the frozen square/D1 and unique-first-`AC` gates, over
characteristic zero on `D(p*k0)`, the seven literal Faber equations have no
point in the exceptional strict-contact block

```text
ord(A)=1, ord(C)=4, ord(R)>=2.
```

No coefficient of `R` is inverted, so this is the entire closed
`ord(R)>=2` tail.  This is the routed block `E` and no neighboring cell is
imported.

## Complete source and the pole-three functional

The independently replayed source through grade 18 has exactly eight
primitive families and global pole ceiling three.  Its unique pole-three
family is

```text
-(1/16)*A^3/L^3, first appearing at grade 18.
```

In particular, the replay retains the competing pole-two terms
`(3/8)C^2/L^2` and `-(3/8)R*A^2/L^2`, including the latter's exact second
correction.  It neither deletes them nor assumes a cancellation.

For the full grade-18 source `H=N3/L^3`, the producer reconstructs the
proper numerator from Laurent coefficients `h_i` as

```text
N3 = h1*z^5+h2*z^4+(h3+3P*h1/2)*z^3
   +(h4+3P*h2/2)*z^2
   +(h5+3P*h3/2+3P^2*h1/4)*z
   +(h6+3P*h4/2+3P^2*h2/4).
```

It also verifies the next Laurent recurrence

```text
h7+(3P/2)h5+(3P^2/4)h3+(P^3/8)h1=0
```

and, on the moving-root cover `p=-2*lambda^2`, both exact evaluations

```text
N3(+lambda)=Phi6+lambda*(Phi5+(P/4)Phi3+(3P^2/32)Phi1),
N3(-lambda)=Phi6-lambda*(Phi5+(P/4)Phi3+(3P^2/32)Phi1).
```

## Opposite-root obstruction

The first `AC/L` equations allocate the nonzero leading forms to opposite
roots.  In the orientation

```text
A0=au*(z-lambda), C0=cv*(z+lambda),
```

evaluate the pole-three numerator at the `C` root `z=-lambda`.  Every
pole-at-most-two column is multiplied by at least one factor of `L` in the
`L^3` numerator and therefore vanishes at the root.  This includes the
full `C^2/RA^2` collision with its retained correction.  The sole
pole-three column instead gives

```text
-(1/16)*A0(-lambda)^3=+(1/2)*au^3*lambda^3.
```

The deck-swapped orientation gives the opposite terminal
`-(1/2)*au^3*lambda^3`.  The producer checks every lower grade coefficient
is zero in both orientations.  Rows 1, 3, 5, and 6 are target-free through
grade 18, so neither functional contains a target term.  After inverting
only `lambda`, `au`, `cv`, and `k0`, each terminal generates the unit ideal.
The moving-root cover is finite etale over `D(p)`, so emptiness descends.

## Source and AWS custody

The replay rebuilds all eight primitives and all seven literal source rows
from frozen ancestry.  It mechanically derives the complete jet ceilings

```text
p:3, A:3, C:3, R:2, k10:2, k6:0, k2:0, mu2:0, mu4:0
```

and checks every recursive quotient, the literal/analytic seven-row
bridge, the sole-pole-three census, the exact `RA^2` correction, both root
identities, both terminal values, target freedom, and the localized unit
ideals.

Box02 exact Q, Box03 `F_65519`, and r6d `F_65521` each return rc zero and
`PASS_D1_E_A1D3_OPPOSITE_ROOT_POLE3_EMPTY`, with byte-identical
mathematical stdout, empty compiler stderr, no Singular diagnostic, and
zero swap.  Exact Q is the characteristic-zero endpoint; the two finite
fields are independent screens only.  Launch/resource custody is in
`AWS_LAUNCH_METADATA.md`, and every retrieved byte is pinned by
`EVIDENCE.sha256`.

## Firewall

This producer closes only `E`, conditional on its named frozen gates, on
`D(p*k0)`.  It does not decide an equality face, a positive-order leading
load, `p=0`, `k0=0`, another D1 face, a terminal/global chart, the square
component, order two, `(8,12)`, maximum twelve, or JC2.
