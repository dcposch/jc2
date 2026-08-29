# Registration: generic affine-Faber odd-parity/J exclusion

Date: 2026-08-26

Status: **PREREGISTERED EXACT-Q PRODUCER PLUS GOOD-PRIME CONTROL.**

Work in the normalized ordinary-Faber `k10=1` face with the exact affine
coefficient coordinates

```text
f=Q^2+N,
Q=z^4+p*z^2+c*z+r,
N=n3*z^3+n2*z^2+n1*z+n0,
u=n1-(p/2)*n3.
```

These are all seven depressed monic degree-eight coefficient directions,
not a selected tangent slice.  On the corrected affine graph put

```text
D=(p^2-4*r)/4,
s=5*D-4*beta,
beta=(5*D-s)/4,
gamma=D*(5*D-4*s)/16,
mu2=D^2*s/32.
```

The client reconstructs all seven frozen ordinary Faber tails and checks:

1. the exact coefficient-coordinate inverse;
2. odd/even equivariance under `(c,u,n3) -> -(c,u,n3)`;
3. the affine graph rows;
4. the complete Jacobian of `(R1,R3,R5)` in `(c,u,n3)` and determinant
   `-a*K^2/16`, where
   `a=D*(5*D+2*s)/32` and `K=5*D*(5*D-2*s)/16`;
5. on `5*D+2*s=0`, rank two and vanishing of `dR7` on the sole kernel;
6. on `5*D-2*s=0`, rank one and vanishing of `dR7` on its two-dimensional
   kernel; and
7. the two raw transverse identities used to control the exceptional fans.

A PASS supports the complete-local parity/implicit-function argument on
the generic open

```text
D* (5*D+2*s) * (5*D-2*s) != 0.
```

It is not by itself a total-Rees accessibility theorem.  Consumption by the
global boundary still requires the reviewed divided-row chart to identify
this normalized face and its coefficient coordinates, with torsion and all
target/load directions retained.  The two exceptional divisors, terminal
`[6,2]`, Taylor landing, order two, `(8,12)`, maximum twelve, and JC2 remain
open.

