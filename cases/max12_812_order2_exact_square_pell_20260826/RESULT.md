# Exact-square seven-tail Pell/Chebyshev result

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER PASS; EXACT CHARACTERISTIC-ZERO REDUCED-SUPPORT
COMPUTATION, PENDING HOSTILE REVIEW AND TOTAL-REES SOURCE PULLBACK.**

Let

```text
Q=z^4+p*z^2+c*z+r,
H=sqrt(Q)*(Q^2+beta*Q+gamma),
Delta=p^2-4*r,
```

using the formal square-root branch `sqrt(Q)=z^2+O(1)` at infinity.  Let
`E1,...,E7` be the coefficients of `z^-1,...,z^-7` in `H`.  The exact-Q
calculation gives

```text
rad(E1,...,E7)
 = (c,
    Delta*(5*Delta-16*beta),
    Delta*(beta^2-5*gamma)).
```

Equivalently, the reduced solution set is exactly the union of

```text
square:       c=0, Delta=0, with beta,gamma arbitrary;
Chebyshev:    c=0, beta=5*Delta/16, gamma=5*Delta^2/256.
```

There is no reduced component on `D(c)`.  The exact-Q radical and the
explicit intersection of the two proposed prime ideals reduce to zero
against one another.  Characteristic `65521` independently gives the same
three-generator basis modulo the prime.  Both AWS validators report
`PASS_EXACT_REDUCED_SUPPORT`, engine rc `0`, 0.03 seconds, about 15 MiB RSS,
and zero swap.

## Exact survivor

Put

```text
T=z^2+p/2,
P(Q)=Q^2+(5*Delta/16)*Q+5*Delta^2/256,
A=T^5-(5*Delta/16)*T^3+(5*Delta^2/256)*T.
```

The independently checked polynomial identity is

```text
A^2-Q*P(Q)^2=Delta^5/262144.                         (1)
```

Thus the nonsquare Chebyshev component is genuine.  It is the scaled
`T_5/U_4` identity for
`Q=T^2-Delta/4`.  Since

```text
A-sqrt(Q)P(Q)
 = (Delta^5/262144)/(A+sqrt(Q)P(Q)) = O(z^-10),
```

its first nine negative Laurent coefficients vanish.  In particular a
combined `k10/k6/k2` load can cancel the first seven rows even when `Q` is
not a square.  Any source fan or total-Rees chart that treats one lower load
in isolation would delete a real receiver.

## Custody and firewall

V1 is preserved as negative custody: its radical stage printed the same
support, but a malformed separate identity control left undefined symbols
and the validator failed.  V2 repaired only that control and duplicate
library diagnostics; it did not change the seven equations.

The exact-Q result is an exact Singular radical computation, not yet a
CAS-free proof or hostile-reviewed theorem.  Its source application uses the
reviewed unitriangular Laurent-to-Faber change, but the literal total Rees
rows, target ties, terminal `[6,2]` condition, and two Taylor receivers have
not yet been pulled back to this component.  This result therefore neither
constructs nor excludes a strict arc, closes order two or `(8,12)`, proves
maximum twelve, nor proves or disproves JC2.
