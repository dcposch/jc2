# Preregistration: isolated a8d3 `k6*R*C` bridge adjudication

Date: 2026-08-26

Status: **PREREGISTERED DIAGNOSTIC; NO CELL VERDICT.**

The complete a8d3 grade-38 producer failed its literal-to-analytic bridge
only in rows 4--7.  A high-memory `F_65519` replay localized every first
residual to grade 38 and to monomials proportional to `eta*k60*R*C`.

This diagnostic must independently specialize the frozen canonical literal
tails to `A=0`, `k10=k2=0`, fixed connection `p`,

```text
C=sigma^11*(c1+c0*t),
R=sigma^8*eta*(b1+b0*t),
k6=k60,
```

and extract every trilinear `k60*C*R` coefficient in rows 4--7 through
grade 38.  It must separately derive the Laurent coefficient

```text
binom(3/4,2) * 2! * 2 = -3/8
```

and assemble its pole-three Faber rows from

```text
H=(-3/8)*eta*k60*(b1+b0*t)*(c1+c0*t)*t^5
  *(1+(p/2)t^2)^(-3).
```

Print the complete literal coefficient, analytic coefficient, and their
difference for each of `row4:c1*b1`, `row5:c1*b0`, `row5:c0*b1`,
`row6:c0*b0`, `row6:c1*b1`, `row7:c1*b0`, and `row7:c0*b1`.

Run exact `Q` and two good-prime controls on three AWS hosts, ordinary rings
only, under fresh tags.  The result may identify which frozen representation
is inconsistent.  It cannot prove emptiness or nonemptiness of a8d3, alter
another promotion, or extrapolate to a neighboring cell.
