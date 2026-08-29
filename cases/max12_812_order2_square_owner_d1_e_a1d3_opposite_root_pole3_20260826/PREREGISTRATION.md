# Preregistration: exceptional D1 `E=(a,d,r)=(1,3,>=2)`

Date: 2026-08-26

Status: **PREREGISTERED EXACT-SOURCE OPPOSITE-ROOT POLE-THREE PRODUCER.**

## Exact scope

After the frozen square/D1 and unique-first-`AC` gates, compile only

```text
ord(A)=1, ord(C)=4, ord(R)>=2
```

in characteristic zero on `D(p*k0)`.  This is the routed exceptional block
`E`; no neighboring cell is imported.

## Controlling invariant

The frozen complete inventory through grade 18 has eight primitive families,
global pole ceiling three, and exactly one pole-three family:

```text
-(1/16)*A^3/L^3, first grade 18.
```

Retain the competing pole-two families `(3/8)C^2/L^2` and
`-(3/8)R*A^2/L^2`, including the latter's exact second correction.  They are
not deleted or assumed to cancel.

For a source `H=N3/L^3`, reconstruct the degree-at-most-five numerator from
the Laurent rows by

```text
N3 = h1*z^5+h2*z^4+(h3+3P*h1/2)*z^3
   +(h4+3P*h2/2)*z^2
   +(h5+3P*h3/2+3P^2*h1/4)*z
   +(h6+3P*h4/2+3P^2*h2/4).
```

At either moving root, independently verify the exact Faber identity

```text
N3(lambda)=Phi6+lambda*(Phi5+(P/4)*Phi3+(3P^2/32)*Phi1).
```

The first `AC/L` equations allocate the nonzero leading forms to opposite
roots.  In the orientation

```text
A0=au*(z-lambda), C0=cv*(z+lambda),
```

evaluate the pole-three functional at the opposite, `C`-allocated root
`-lambda`.  Every pole-at-most-two family becomes divisible by `L` in the
`L^3` numerator and vanishes there, including the `C^2/RA^2` collision.
The sole pole-three family gives

```text
-(1/16)*A0(-lambda)^3=+(1/2)*au^3*lambda^3.
```

The deck-swapped orientation must give `-(1/2)au^3 lambda^3`.  Rows
`1,3,5,6` are target-free through grade 18, and these values are units on
the exact-contact root charts before radicals.

## Acceptance

1. Rebuild the complete eight-family source and all seven literal rows
   through grade 18 from frozen ancestry; certify every recursive quotient.
2. Require the sole pole-three signature and the exact `L^3` recurrence.
3. Require both moving-root Faber identities and both opposite-root terminal
   coefficients, with every lower coefficient zero.
4. Retain and recheck the exact grade-18 `RA^2` second correction from the
   routed negative control.
5. Check target freedom row by row, and unit ideals after inverting only the
   named exact-contact/root/load coefficients.
6. Run exact Q and independently `F_65521` and `F_65519` on AWS with fresh
   tags, fail-closed validators, and zero swap.

## Firewall

A PASS concerns only `E` on `D(p*k0)`.  It does not use a pure-`C^2`
endpoint, decide an equality face, a positive-order leading load, `p=0`,
`k0=0`, another D1 face, a terminal/global chart, the square component,
order two, `(8,12)`, maximum twelve, or JC2.
