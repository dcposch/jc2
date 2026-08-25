# `p=2`, depth-three equal-cap pilot

Use the reviewed completed-gauge orientation

```text
C_(2,3)(X,Y) = (X-X^2, Y(1+2X+4X^2)),
F = C_(2,3) o phi,
phi=(A,B) = (x,y) mod 2.
```

The finite system `B_(2,3)(D,D)` uses total-degree simplices for both the
gauge and composed map, over `Z/8`, and explicitly charges

1. `det J(A,B)=1 mod 8`;
2. `det J(F)=1 mod 8` as a redundant orientation/control equation;
3. every over-cap coefficient of `F`;
4. the identity residue branch coefficientwise.

The seed forces `D>=2`.  The identity gauge is an exact positive control at
`D=3`, because `F=(x-x^2,y(1+2x+4x^2))`.  The preregistered discriminator is
whether `B_(2,3)(2,2)` is empty or has a nonidentity cancellation.  SAT must
be replayed by direct integer polynomial arithmetic; UNSAT is provisional
unless proof-checked and source-reviewed.

No comparison with `p=3`, all-depth, no-lift, or Jacobian-conjecture claim is
licensed.  All substantive execution is AWS-only.

