# Preregistration: upper-face cascade through weight six

Date: 2026-08-27 17:33Z  
Repository base: `418e413593120d19e15e6546eb50c985f4b1f038`

## Charged question

On the frozen D3 raw windows, derive `D1=...=D6=0` exactly for the two
squarefree degree-eight endpoint shapes

```text
P: H=A^2, deg A=4;
Q: H=A^2 B, deg A=3, deg B=2, gcd(A,B)=1.
```

Carry every polynomial kernel of the new-row operator.  Emit necessary and
sufficient gates, raw degree checks, honest dimensions where the strata have
constant rank, and controls separating the cascade from the provisional q1
image gate.

## Method and stop rule

Use the promoted determinant recurrence and the exact characteristic modes
`t^m F^((12-m)/8)`.  Work by coefficient identities and polynomial
divisibility, not Groebner elimination.  Stop after row six.  A report passes
only if an independent exact-Q replay reconstructs three full-window
fixtures, rejects one mutation at every new gate, and confirms q1
nonmembership for the separating controls.

## Firewalls

This case does not impose `D22=1` or `D23=0`.  In particular, an all-zero-row
control has endpoint `D22=0` and cannot decide whether endpoint-normalized
prefixes satisfy q1.  No GGV landing, family exclusion, counterexample, or
JC2 claim is licensed.

