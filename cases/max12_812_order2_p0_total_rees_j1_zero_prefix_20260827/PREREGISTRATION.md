# Preregistration — `J1=0` prefix specialization

Date: 2026-08-27

Status: **DESK-SCALE EXACT NAVIGATION ONLY.**

## Question

Before constructing either second-stage `J2=(a0,a1)` Rees chart, restrict the
currently frozen literal actual-total prefix to

```text
J1=(rs,cs,c0,c1)=0
```

and identify exactly which rows and variables survive.  Consume only the 21
exact-Q V9 rows `Tg10_1..Tg12_7` and the exact-Q V17 row `Tg14_5`.

## Frozen checks

The replay must:

1. parse the literal polynomial bytes with a restricted AST and exact
   `Fraction` arithmetic, never `eval` or a CAS;
2. hash every input and emit a canonical SHA-256 for every specialized row;
3. print every surviving row's grade, term count, total degree, and variable
   support, and the first surviving grade;
4. assert that `Tg10_1..Tg10_4` and `Tg12_6` vanish identically on `V(J1)`;
5. assert that the `e1`-only restriction of `Tg12_2` is exactly
   `(3/32)e1^2`; and
6. recheck the `A00` and `A10` zero-section controls.  Those controls imply
   that neither `a0` nor `a1` lies even in the radical of this 22-row
   specialized ideal.

No ideal membership, radical, Rees chart, or higher-grade source computation
is licensed.

## Interpretation registered in advance

- PASS identifies the first grade and literal support through which stage two
  can receive information from this prefix.
- The two zero-section controls prove that this prefix does not empty either
  standard `J2` chart or the terminal receiver by itself.
- The result says nothing about unexported grade-13, other grade-14, higher,
  stage-two, or receiver equations, and nothing about a full source arc,
  Gate T, order two, maximum twelve, or JC2.

The replay is deliberately local and tiny.  No Singular, Groebner, network,
AWS mutation, or `jc2-lean` access.
