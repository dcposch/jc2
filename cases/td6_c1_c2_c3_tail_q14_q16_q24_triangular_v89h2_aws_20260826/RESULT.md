# TD6 V89H2 `q14` plus high-tail triangular diagnostic

Date: 2026-08-26

Producer verdict: **diagnostic PASS on Box02 and r6d.** The reviewed q-zero
pivot block does not give a polynomial triangular FIRST inverse after `q14`
is added. This is a fail-closed pivot obstruction, not a source point or a
nonintegrability theorem.

## Exact result

The client set `q2,...,q13=0`, kept `q15` absent under the separately reviewed
target shear, and retained the ten independent variables

```text
q14,q16,...,q24.
```

It rebuilt the literal V87 transport, all 38 packed raw FIRST maps, and
genuine raw P12. At q zero, every source digest reproduces frozen V85. For
the reviewed q-zero FIRST pivot columns it formed

```text
B(q)=A0^(-1) A(q)=I+N(q).
```

The exact support graph of `N` has 368 directed edges and is cyclic. Its
first cycle is the self-loop

```text
row 0 -> column 0,
row key ('X-2',0), pivot section variable 0,
q support {14}, exactly one q term.
```

The self-loop entry has digest
`739fc738a4150dc5650a58cb4f7d9f4d45ec8fc4f3b0c152d8492aee512d6ed8`.
Thus the H1 finite nilpotent inverse does not extend to q14 using this square
pivot block: a q14-dependent diagonal factor appears before P12 reduction.
The client stopped there as preregistered and did not invert that factor.

## Denominators and fail-closed meaning

The complete rebuilt P12/FIRST family has common denominator

```text
C*U - 3*U^3 = U*H.
```

No F or q expression was inverted. The graph cycle proves only that this
particular polynomial triangular normalization fails. An alternate constant
pivot block, a unimodular row/column transformation, or a determinantal
stratification may still handle q14. The result supplies no radical
nonmembership and no formal or geometric source witness.

## Custody

- source archive:
  `d577e82e1a71fabbc45466664c4668b9c936d4ad001e333ae0e95e06335d2244`;
- source manifest:
  `e56340e97b9c47b095bd4de7318de7665797c212572698581c6bdd9f60282050`;
- client:
  `6991a4e59df51d0c4d67683d317518f22b0be3e2728156cf0ec79640137d63e3`;
- exact graph:
  `c918346cfedf44ed2dab86b4cf46bf54508e270f2188b8e053b478a2e65e1737`;
- exact result record:
  `3bc435e8906eb1df5c7185382c8a0d3ff9bd5278965bfc2f08a5a41328f62827`;
- byte-identical mathematical stdout:
  `dfd3fd497de8a0ef2cf3ddc84ee7008aeb4bfcab35f7de4bb441269f656d83d0`.

Both independent AWS runs returned rc=0 with the exact banner
`TD6-V89H2-TAIL-Q14-TRIANGULAR-OBSTRUCTION DIAGNOSTIC-PASS`.

## Scope firewall

This diagnostic concerns only `q14,q16,...,q24` on the retained normalized
three-center, fixed F1/pole/dead-stretch source family on `D(U H B3)`. The
H1 high-only collapse is withdrawn because its final denominator contains
the unregistered factor `K=2 R38`; H2 does not repair that gate. It does not
cover q2 through q13, totalize q15 beyond its target shear, cover omitted
geometric variables or total Rees, or prove any whole fixed-A3, TD6, SP-2,
or JC2 statement.
