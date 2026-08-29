# V89H1 denominator obstruction

Date: 2026-08-26

The dual V2 AWS clients reached the final denominator gate after all of the
following exact checks passed:

- literal V87 transport, FIRST, and P12 rebuild;
- q-zero V85 source custody;
- acyclic 38 by 38 high-q FIRST graph and two-sided polynomial inverse;
- normalized FIRST replay from the original literal source rows;
- literal P12 reduction to one q-independent q-zero remainder term;
- reconstruction from the original FIRST sources;
- one active FIRST-row omission control and P12 omission control.

The common denominator of the audited P12, original and normalized FIRST
sources, transformation matrices, source multipliers, remainder, and proposed
unit certificate has exact factorization

```text
(1/8) * K * B3 * U^2 * H^2,
K = 2*C*V^2*U + 16*C*U^4 - V^4 - 14*V^2*U^3 + 16*U^6.
```

`B3`, `U`, and `H` are registered. `K` is not. Both clients therefore failed
closed at `factors_allowed(common)` with rc=1 before emitting an exact-result
record or a PASS banner.

This factor has prior exact custody. Frozen V83 names

```text
R38 = C*V^2*U + 8*C*U^4 - (1/2)*V^4
      - 7*V^2*U^3 + 8*U^6,
```

so `K=2*R38`. V83 proves FIRST rank 38 only on
`D(U H B3 R38)` for its selected minor and explicitly records `R38=0` as an
alternate-minor/raw-fibre debt. Its `MANIFEST.sha256` has SHA256
`355686c91424b05d21a7a03f8052028b7d32a67b1dbfe948c0d7c3c00121227e`;
the copied V83 `FREEZE.sha256` file has SHA256
`dfafe95a1c993e6181398eab8c84e0699ac4f8785e96e5adb36660e42f6d74f1`.
Thus K is a known FIRST selected-minor factor, not a newly licensed CURRENT
denominator.

The canonical one-line K formula is in `K_FORMULA.txt`, SHA256
`2db6935d74924896248fa192120888d8067004a314e4f8fc41c581a7675c2f87`.

No theorem on `D(U H B3)` may consume the provisional unit remainder. In
particular V89H1 does not currently prove that the high jets are polynomial
row coordinates on the registered open, does not prove
`1 in J+(q2,...,q14)`, and cannot seed the global low-q radical shortcut.
The rational calculation is usable only as support discovery until K is
licensed, proved a unit modulo the literal source ideal, its zero stratum is
covered, or an alternate certificate removes it.
