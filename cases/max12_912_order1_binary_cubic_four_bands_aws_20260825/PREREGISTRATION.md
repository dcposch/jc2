# Preregistration — complete degree-15 binary-cubic incidence lift

Status: frozen before execution.  All substantive computation is AWS-only.

For each characteristic-zero root type `L^3`, `L^2M`, and `LMN`, consume the
exact denominator-free degree-18/17/16 construction and retain its complete
nonreduced incidence.  Parameterize the full fresh degree-16 solution
`(P6,Q9)`—including all eight kernel parameters—and compile the next complete
original row

```text
[P9,Q8]+[P8,Q9]+[P7,Q10]+[P6,Q11]+[P5,Q12]=0.       (degree 15)
```

Registered steps:

1. reconstruct the full degree-18 kernel and degree-17 incidence;
2. RREF the complete degree-16 fresh map with an explicit invertible row
   transform, retain every transformed zero-row equation, and verify its span
   equals the complete left-cokernel projection;
3. express all coefficients of `(P6,Q9)` in the eight fresh kernel variables
   plus the exact polynomial particular solution;
4. build all 16 degree-15 source coefficients with two independent bracket
   implementations;
5. project to the complete cokernel of the fresh `(P5,Q8)` map;
6. emit the union of degree-17, degree-16, and degree-15 obstruction equations
   in `Q[s,t,u]` without radical, saturation, primary decomposition, component
   choice, or nilpotent removal;
7. run exact `std` and exact `slimgb` on separate AWS hosts, sharded by root
   type, with the all-zero lower-face positive control.

Dimension is navigation only.  A nonunit ideal is not a full Keller survivor;
a unit would exclude only compatibility through degree 15.  No endpoint proves
an all-depth lift, B9 residue preservation under PGL2, a Q8 landing, maximum
twelve, a counterexample, or JC2.

Every runner must refuse Darwin/non-Linux, a wrong hostname, a wrong registered
AWS tag, or non-Amazon platform identity before invoking Python or Singular.

