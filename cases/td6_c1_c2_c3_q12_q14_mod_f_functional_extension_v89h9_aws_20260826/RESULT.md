# TD6 V89H9 q12 functional extension — producer result

Date: 2026-08-26

Verdict: **PASS at producer tier, pending hostile review.**

## Exact theorem scope

On the exact `F=0` specialization over `D(U*H*B3)`, with independent
untruncated variables

```text
q12,q13,q14,q16,...,q24,
```

with `q2,...,q11=0` and `q15` absent only by the reviewed target shear, the
registered 38-column original-FIRST pivot block is polynomially invertible.
Its sole cyclic SCC is

```text
(0,1,2,3,4,5,6,11,12,13)
```

and has determinant exactly one.  The emitted two-sided inverse recovers all
38 original FIRST rows before literal P12 division.

The canonical P12 remainder has 17 parameter terms and q support exactly

```text
(12,), (13,), (14,).
```

Its maximum total q degree is one; in particular there is no q12-q14 mixed
term.  The pure-q14, empty-parameter, E3-coordinate-0 functional is exactly
the reviewed V89H7 functional and remains nonzero.  Its denominator radical
is contained in the registered `U*H*B3` firewall on `F=0`.

This does not restore q2,...,q11, totalize q15, prove a unit ideal or source
exclusion, supply a total-Rees chart, close whole TD6, or resolve JC2.

## Dual-AWS custody

- Source archive SHA: `1babd74c3b823045b524699fcde5ff37b85614bcd39c4b3e52b938a898e71300`.
- Source manifest SHA: `fc4ca45fdbdea2855b1a4c32460331d63e0de9c1258fb0f3a49ef97502b9c3fc`.
- Client SHA: `d5014ed29582a90384712403a103fcc05f60f42d995b7eb2194781e83d3ab6ab`.
- Both Box02 and r6d returned rc 0 with byte-identical stdout SHA
  `8d799a20b15f7206c7495ea837df943002f9849ba18aeaac9400f425fd00d039`.
- SCC artifact SHA: `52188fe1c05d25ea82947334dca3e25bb54fa5f4909c409cedbd20a52d31fd79`.
- Canonical remainder SHA: `db55d372399375c4dd94fa3df91bf694ab23e9428b1b1ce7f1ec81d7b91a9911`.
- q-support SHA: `7ab50a6796be631896692a5e5465ac5e150a6855fc43eb19fbc48a16c66e3c15`.
- Machine result SHA: `57f405a24c81597b00d89d73323382149ec57657cf5d8d5d1ab8f44d6db07db2`.

All substantive computation ran on AWS.  `jc2-lean` was not touched.
