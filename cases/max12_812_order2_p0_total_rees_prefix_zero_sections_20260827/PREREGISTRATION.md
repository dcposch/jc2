# Preregistration — exact prefix zero sections

Date: 2026-08-27

Status: **DESK-SCALE SOURCE-PREFIX CHECK ONLY.**

## Question

Before spending AWS time on the genuine-localizer complement `k=0` or on
the second-stage `J2=(a0,a1)` charts, test whether the currently frozen
literal actual-total source prefix can possibly make their special fibres
empty.

Consume exactly:

- all 21 exact-Q V9 source rows `Tg10_1..Tg12_7`; and
- the exact-Q V17 source row `Tg14_5`.

Evaluate them over `Q[rho]` at three assignments:

```text
CS0: cs=1, k=0, every other source variable except rho=0;
A00: a0=1, J1=(rs,cs,c0,c1)=0, every other source variable except rho=0;
A10: a1=1, J1=(rs,cs,c0,c1)=0, every other source variable except rho=0.
```

The replay must parse the frozen polynomial bytes without `eval`, preserve
`rho` symbolically, use exact rational arithmetic, hash every input, and
require all 66 residual polynomials to be zero.  It must also check:

- the reviewed `T-cs` witness gives `Tg12_2=0` and
  `Tg14_5=-21/320`; and
- deliberately setting `cs=k=1,e1=0,rho=0` makes `Tg12_2` nonzero.

## Interpretation registered in advance

- PASS proves only that these 22 exported source rows contain horizontal
  source-prefix sections and therefore cannot, by themselves, yield a
  special-fibre-emptiness certificate on the named loci.
- It does not prove a point of an uncompiled Rees chart, survival of any
  unexported source row, a formal or algebraic arc, Gate T, order two,
  maximum twelve, or JC2.
- FAIL is a source-byte/evaluator discrepancy and freezes the conclusion.

This replay is intentionally tiny and local: no Gröbner basis, Singular,
network, AWS mutation, or `jc2-lean` access.
