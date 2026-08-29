# Result: D1 `a=9`, `D(k60)` grade-27 exact-contact obstruction

Date: 2026-08-26

Status: **DUAL-AWS EXACT-Q PRODUCER PASS; SCOPED THEOREM, HOSTILE REVIEW NOT YET RUN.**

## Result

There is no point of the registered fixed-contact D1 chart

```text
ord_sigma(A)=9,  ord_sigma(C)=10,  ord_sigma(R)>=9
```

on `D(p*k0*k60)` satisfying the seven literal-Faber source rows.

Indeed, the corrected complete-source V3 replay is exactly divisible by
`sigma^27`, has no earlier nonzero row, and its first two divided rows are

```text
g27_1=(3/4)c1*k60,
g27_2=(3/4)c0*k60.
```

Thus `k60 != 0` forces `c1=c0=0`.  This contradicts exact
`ord_sigma(C)=10`, whose leading coefficient is `c1*z+c0` and must be
nonzero.  Equivalently, after adjoining inverses for `p,k0,k60` and Bezout
coordinates imposing `(c1,c0)!=(0,0)`, the two grade-27 equations generate
the unit ideal.  Exact Q and `F_65521` independently returned

```text
D1A9_K60_GRADE27_IDENTITIES=1
D1A9_K60_FORCES_C_ZERO=1
D1A9_K60_EXACT_CONTACT_AUGMENTED_IDEAL_UNIT=1
D1A9_K60_UNIT_GRADE27_ENDPOINT=PASS_EMPTY_EXACT_CONTACT
```

## Complete-source custody

This is not a truncated-load obstruction.  The replay also certified:

- grade 28 rows 1--3 including `k60_1`, and the moving connection
  `-(3/8)*ell1*c1*k60` in row 3;
- the grade-28 `mu20` target;
- the grade-31 coefficients of delayed `k20`, `k0_1`, and `k60_4`;
- the literal full-source target insertions `mu4`, `mu6`, and `J/4`, even
  though they occur after the extracted grade-31 window;
- all 224 recursive row-status markers, no rows below grade 27, and the
  exact recursive quotient identities.

The Chebyshev/Pell identity for `Q=z^4-1` also passed, so this client does not
encode a blanket square-forcing assertion.  The normalized endpoint-marker
stream agrees between the two fields with SHA-256
`8b18dd5c0d6015862ef0a1b4223f67c9da06d073028dfad0b050e3ff3ca3952f`.

## AWS custody

Exact Q / Box03:

- tag `max12_812_order2_square_d1_a9_k60_unit_grade27_v2_q_20260826_box03`,
  PID `229360`;
- compiled input SHA-256
  `b4db6502507c368827b6a40ad866a7792f026fb98d0a4b79f645ebc08b2a1cba`;
- stdout SHA-256
  `00066ec7a17918e4fdedd2212f358ff55a13e19b0f29ec4d0ce416e94a462b12`;
- metadata SHA-256
  `d0aaeab7c8dc12ad296553684b872d45378f013c3b1c7580bb4ddffc5aafa004`;
- wall `5.78s`, peak RSS `1255352 KiB`, swaps `0`, engine `rc=0`;
- validator `PASS_D1_A9_K60_UNIT_GRADE27_V2_EMPTY_EXACT_CONTACT`.

`F_65521` / r6d:

- tag
  `max12_812_order2_square_d1_a9_k60_unit_grade27_v2_p65521_20260826_r6d`,
  PID `286619`;
- compiled input SHA-256
  `d85c5871137b579901989ca9586115b49ec1e1634818beb4855d3504fa53088c`;
- stdout SHA-256
  `ccc17f85fbbc5c437de4fc50a67f160c0911787306b068d0b50194632c960f21`;
- metadata SHA-256
  `57aecd6002a94113c2e2110985511027a09fb6d14ce6f4463e85c942df3abc47`;
- wall `3.89s`, peak RSS `889144 KiB`, swaps `0`, engine `rc=0`;
- validator `PASS_D1_A9_K60_UNIT_GRADE27_V2_EMPTY_EXACT_CONTACT`.

## Exact remaining `a=9` module

The result removes only `D(k60)`.  The next source-complete module is the
closed branch `V(k60)`, beginning at grades 28--29 with the
`k60_1`--`mu20`--moving-connection collision.  It must retain all higher
normal corrections, delayed `k20/k0_1`, and terminal targets.  Nothing here
licenses a claim on that branch.

## Firewall

This is a fixed-contact `a=9` theorem on `D(p*k0*k60)` only.  It does not
cover `V(k60)`, contact-raising arcs, any other valuation cell, all of D1,
the square component, order two, `(8,12)`, maximum-twelve, or JC2.

