# V33 preregistration: prolong the rational ordered-a1 boundary point to grade 18

Date: 2026-08-27

The V32 six-coordinate grade-17 variety contains the algebraic normalized
branch

```text
aa0=0, ell2=l, cs1=12/l, rs2=-(20/9)l^2,
ee1=32l, ec3=576/l, a1=48,  with l^5=243/2.
```

Applying the sigma action with scale `u=l^2` eliminates `l` and yields the
rational point

```text
a1=708588, ell2=243/2, cs1=1458, rs2=-32805,
ee1=57395628, ec3=1033121304,
```

all other registered coordinates zero and `rho=0`.  Direct exact substitution
kills all 56 rows through grade 17.

V33 reconstructs the seven actual-total rows at grade 18, bridges the 56 old
rows to V23R1/V28/V30, and solves the grade-18 affine equations in every new
weight-18 coordinate.  Emit an exact extension or a rational dual obstruction.
Run independently over `Q` and `F_65521` on AWS.  This is a finite-prefix
test, not a formal branch or a JC2 conclusion.

