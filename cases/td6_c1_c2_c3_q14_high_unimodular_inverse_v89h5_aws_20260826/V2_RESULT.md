# TD6 V89H5V2 q14 remainder localized-`(F)` membership result

Date: 2026-08-26

Producer verdict: **NONMEMBERSHIP PASS on Box02 and r6d (both rc 0).**

## Exact input and ring

The client consumes the byte-identical V89H5V1 normalized P12 remainder

```text
eb939448f5636a3084ca129aa3a5cdf44709ac3a8ca28be77a14c2e5fdea7c14
```

on the residue block `q2=...=q13=0`, q15 absent under the reviewed target
shear, with independent untruncated `q14,q16,...,q24`.  The frozen TSV has
18 data records: one q-zero record and seventeen positive records, every one
with q monomial `(14,)` and none with another q monomial.

The membership ring is

```text
R = Q[C,V,U,1/(U*H*B3)],
F = C*U - V^2 + U^3,
H = C - 3*U^2.
```

Neither F nor any q expression is inverted.

## Exact negative certificate

The common denominator of the original seventeen-record positive remainder
factors exactly as

```text
(1/4)*B3*H^2.
```

It is therefore registered and coprime to F.  Formal coefficientwise
division of all 306 rank-18 scalar coordinates by F replays exactly in the
fraction field, but its common denominator factors as

```text
(1/4)*F*B3*H^2.
```

Forty nonzero coordinates require this unlicensed F factor.  Already record
0, parameter monomial `()`, q monomial `(14,)`, extension coordinate 0 has
nonzero numerator residue modulo F:

```text
964054/375*V^11
 + 406466606/375*V^9*U^3
 + 7631257816/375*V^7*U^6
 - 2659677202/375*V^5*U^9
 - 1042046824/75*V^3*U^12
 + 177632/15*V*U^15.
```

Because `U`, `H`, and `B3` are each coprime to F, localization at their
product cannot remove that residue.  Thus this particular normalized
positive-q14 remainder is not coefficientwise in the principal ideal `(F)`
inside R.  The complete 306-coordinate inventory, exact first failure, and
an omission fixture are byte-identical on the two hosts.

## Consequence and firewall

This rejects the cheapest composition “use the V89H5 inverse, then absorb
its entire q14-positive remainder by one F multiplier.”  There is no licensed
F quotient for that specific normalized remainder.

It does **not** compare the remainder class across the alternate H3/H4 FIRST
splittings, and it does not exclude adding a different combination of the
original FIRST rows before reducing modulo F.  In particular, it is not a
nonunit theorem for `(P12,FIRST,F)`.  It supplies no low-q unit-chart cover,
total-Rees/source result, source point, whole fixed A3, TD6, SP-2, or JC2
statement.

The next exact gate is therefore a splitting-independent cokernel test:
reduce literal P12 and the full original FIRST module modulo F and ask whether
the q14-positive class vanishes, rather than testing this chosen normal form
coordinatewise.

## Custody

- final source archive:
  `f4c0cbfb1dfe174e0f87b9b2f7a0a02dccf3b126965fc760cd91c28bfe15714a`;
- source manifest:
  `dc3c088a66aee68657d256dc84cc0f7984635234c69608d2a51d64cdeba53294`;
- final client:
  `263f892df9cb6834a6fd722229d848cb53cefe6b7c7fd6405e10183dc54efedd`;
- byte-identical mathematical stdout:
  `8298bf7e5d5cf1d5affffffa25e2176c9cf782d49f94ccf76f1486766c0928b3`;
- exact result:
  `55108cfae75437abade24d87b75e3b889bebeac31df50a967b9e4f8dd994a725`;
- negative certificate:
  `45493d18c62c524db77641f51b1a23128e48f5c63e059cc07990936617611c71`;
- complete coordinate inventory:
  `216ae5ae3fc67af7cce7de129524d14243406ff66e6709813870ff3628d2bde5`.
