# V35 preregistration: grade-19 test of the V34 rational orbit

Date: 2026-08-27

The exact-Q V34 basis is a degree-five Kummer scheme.  With `t=ec3` it has

```text
t^5 = 1215000000000,
cs1=11*t/600, ee1=21600/t, ell2=1575/(2*t),
aa0=-t^2/3750, rs2=-7*t^3/10800000, a1=48.
```

Under the sigma action, scaling by `lambda=t^3/13500000` gives the rational
representative

```text
a1=192, ell2=21/4, cs1=11, rs2=-35,
aa0=-96, ee1=576, ec3=2400,
```

with every other ordered-`a1`, `rho=0` source coordinate zero.  Exact local
replay kills all 63 frozen rows through grade 18.

V35 reconstructs the literal actual-total source through grade 19, bridges
all 63 frozen rows byte-exactly, checks the rational representative, and
evaluates all seven grade-19 rows over exact Q and independently over F65521.
No support enlargement or new jet is allowed: this is the fixed V34 support.

Because the source rows are sigma-homogeneous, a nonzero grade-19 value at
the rational representative kills the whole five-point normalized orbit;
all seven zero values preserve it through grade 19.  The orbit implication
requires independent review of the displayed Kummer presentation.  Neither
outcome decides the full ordered `T-a1` chart.
