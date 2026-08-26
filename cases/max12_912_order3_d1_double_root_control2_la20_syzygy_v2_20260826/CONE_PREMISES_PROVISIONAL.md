# Finite witness-obstruction inequalities

Status: **exact consequence of the LPDP witness; independent global-`dp`
enumeration and hostile review pending**.

Write a general weight as

```text
w=(L,T,H,Q1,Q0,R2,R1,R0)
```

in variable order `(la,tau,rho,q1,q0,r2,r1,r0)`. The explicit witness in
`WITNESS_RESULT.md` has `la^20` as its unique least-weight term throughout
the open rational polyhedral region

```text
T                         > 0,
Q1 + 3*Q0                 > 20*L,
Q1 + R2 + R1              > 20*L,
Q1 + 2*R1                 > 20*L,
Q1 + R2 + R0              > 20*L,
Q0 + R1 + R0              > 20*L,
Q1 + 2*R0                 > 20*L.
```

`H=w_rho` is absent from this particular witness and is unrestricted by these
seven inequalities. At the charged point `(4,1,1,22,22,30,30,30)`, the
strict margins in the listed order are

```text
1, 8, 2, 2, 2, 2, 2.
```

Inside this region the initial ideal contains `la^20`, hence its
eight-coordinate torus localization is empty. These halfspaces describe a
**witness obstruction region**, not necessarily one Gröbner cone. On an
equality face the displayed initial witness is nonmonomial and the full face
initial ideal must be torus-saturated separately; no face is excluded here.

The independent global-`dp` V2 job is charged to enumerate the exact same
finite support and reproduce the weight-80 uniqueness check. Until that and
hostile review close, this file is not a promoted neighborhood theorem.
