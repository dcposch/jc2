# V4 preregistration — corrected coefficient-infinity source controls

V3 failed before CAS because it mis-typed the pinned compiler's returned
`Ring` object as a tuple of variable names.  V4 pins/imports the immutable V3
helpers, removes only that invalid assertion, and retains all intended exact
controls.

Acceptance requires, before the projective closure result is read:

1. every homogenized row has its declared constant `(C0,C1)` degree;
2. `C1=1,C0=c` reproduces the original pinned source row exactly; and
3. simultaneous scaling `(C0,C1)->(lambda*C0,lambda*C1)` multiplies the row
   by `lambda^degree`.

The controls are checked both as Python polynomial dictionaries and as zero
polynomial differences in emitted Singular rings.  Expected imposed-row
degrees `(1,3,5,7,2,4)` are `(1,2,3,3,2,2)`.

After the controls, V4 repeats V2: homogenize before specialization, saturate
by `C1*w*x5*(x3-2*x5)`, contract, then impose `C0=1,C1=0` and pointed landing
`v=w=u=x1=x3=x5=0` in `d4=1+v,d2=2+v+u`.

Scope remains coefficient infinity with all other displayed coordinates
affine.  No other projective boundary, terminal/Taylor reconstruction,
trajectory, full `(9,12)`, maximum-twelve, or JC2 inference is licensed.
