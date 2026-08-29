# Result: repaired H17/q7/a3 numeric formal prolongation V8

Date: 2026-08-26

Status: **DUAL-AWS PASS; FIXED-BRANCH NAVIGATION ONLY.**

The exact-Q Box03 lane and independent F65521 Box02 lane both passed the
preregistered repaired recursion.  V8 first verifies the exact leading
solution

```text
(S0,Y,d2,dm,d4,d6,kappa)
  = (0,0,1/2,-7/64,3/32,-10,8/5)
```

and then solves 24 positive-index coefficient blocks.  The same seven by
seven new-coefficient matrix occurs at every step.  Over Q it is

```text
[3/4,  0,    0,  0,  0,      0,         0]
[3/16,-3/8,  0,  0,  0,      0,         0]
[0,    0, 1/128, 0,  0, -1/512, -15/1024]
[0,    0,  -1/8,-1,  0,   3/128,    15/128]
[0,    0,     0, 0, -1,       0,         0]
[0,    0,   1/8,-1,  4,  -9/128,   -65/128]
[0,    0,     0, 0,  0,       0,       5/4]
```

with determinant `45/524288`; its F65521 image is `40951`, also nonzero.
The complete raw seven-row system vanishes through common raw grade 72 in
both fields.  The recursion crosses the first effective source determinant
target at grade 57, so this is positive evidence that the normalized
Kummer receiver is not a finite-jet artifact.

The full exact rational coefficient lists are preserved in the Box03
`prolongation.json`; the independent modular lists are preserved in the
Box02 copy.  In particular, the first several nonzero coefficients are
nontrivial rather than an identically constant solution.

## Evidence

- immutable source/input manifest SHA:
  `cb4d25db83d386329944ffb1872f5960729c8a57a89b974a74a089e6461c5760`;
- exact-Q prolongation SHA:
  `2d9f690f889ca860f29c892b6d5df8429d4616c8768790bd17c64290e26b18f0`;
- F65521 prolongation SHA:
  `a6fd131edfcfb5cbdc0a28b3c1080768d3971b73ea8f267d1981f32601d69bc6`;
- both external validators say
  `PASS_A_H17_Q7_A3_NUMERIC_PROLONG_V8`.

## Scope firewall

This proves only one fixed normalized numeric branch on the registered
`D(x)` chart through grade 72.  It is not the general complete-local IFT
theorem, a literal source/total-Rees or finite Taylor realization, an
algebraic/rational termination statement, or an order-two, maximum-twelve,
or JC2 verdict.  V7 remains an immutable deployment-negative artifact: it
incorrectly linearized the nonlinear leading face at the zero vector and
has no mathematical verdict.
