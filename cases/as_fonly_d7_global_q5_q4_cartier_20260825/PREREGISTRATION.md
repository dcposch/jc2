# Global Q5-locus Q4 Cartier discriminator

Consume the source-pinned global Q5/H6,J6 formula, retaining every one of
its 197 displayed rows and every exact-division gate.  Add exactly the
single source coefficient

```text
[x^2 y^2] G4 = 0 in F3,
```

where `G4` is the degree-four divided carry before the new homogeneous
degree-five digit `(H5,J5)`.  In characteristic three this coordinate is
unchanged by `(H5)_x+(J5)_y`, because its two possible coefficients are
multiples of three.

Discriminator:

- SAT plus direct integer replay gives a Q5 state not killed by this Cartier
  coordinate and is the next witness-first Q4 target;
- proof-checked UNSAT, after source/compiler review, closes the displayed
  global Q5 locus at Q4;
- solver UNSAT without a checked certificate remains diagnostic.

The omission control is the already direct-replayed base-513 Q5 SAT model,
whose Cartier coordinate is one and therefore must fail only the new row.

Strict scope: the parent is the aligned F-only `D=7` formula.  Even SAT does
not restore the other four Q4 rows or Q3 through Q0, and no residue-ball,
all-depth, no-lift, or Jacobian-conjecture inference is licensed.

All substantive execution is AWS-only.

