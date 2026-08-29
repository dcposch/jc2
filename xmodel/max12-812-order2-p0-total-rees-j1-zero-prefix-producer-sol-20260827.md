# Producer: exact `J1=0` specialization of the frozen total prefix

Date: 2026-08-27

Verdict: **PASS — NAVIGATION ONLY.**

Preregistration SHA-256:
`3dae2b1786635de41f5e3501de7bb90bca08e491f21fb2975cfb53a911f2fabc`.

Replay SHA-256:
`53ed677f8d60220480b37a87affd7958ce3c6cf59164ca373814e4993e7d1c60`.

The restricted-AST `Fraction` replay consumed the frozen 21 V9 exact-Q rows
`Tg10_1..Tg12_7` and V17 exact-Q `Tg14_5`, set
`J1=(rs,cs,c0,c1)=0`, and returned:

```text
all seven grade-10 rows                         zero
surviving grade-11 rows                         1,2,3,5,7
surviving grade-12 rows                         1,2,3,4,5,7
surviving grade-14 rows                         Tg14_5
surviving rows total                            12 of 22
first surviving grade                           11
Tg12_2 with only e1 retained                    (3/32)e1^2
A00 zero rows                                   22
A10 zero rows                                   22
```

Every surviving row except `Tg12_4` has both `a0`-support and `a1`-support.
The stage-one certificate rows `Tg10_1..Tg10_4,Tg12_6` all vanish on
`V(J1)`, as predicted; in fact all of grade 10 vanishes.  Each input and each
canonical specialized polynomial is independently SHA-256 recorded by the
replay.

## Consequences

1. Stage two first appears at grade 11 in this exported prefix.  It is a
   fresh row-support problem; none of the rows that closed the first-stage
   charts supplies a relation on `V(J1)`.
2. The exact `A00` point (`a0=1`, all other names zero, `rho` free) is a zero
   of every specialized row, so `a0` is not in the radical of this prefix
   ideal.  Likewise `A10` proves `a1` is not in the radical.  Therefore this
   22-row prefix cannot empty either standard `J2` chart or the terminal
   receiver.
3. A second-stage certificate search using only these rows is now ruled out.
   The next source task is not a Rees/Groebner launch: export the first
   unexported row that is nonzero at `A00` or `A10`, then rerun this census.

## Firewall

No ideal membership or radical was computed; the nonmembership statements
come only from explicit rational points.  No claim covers unexported
grade-13, other grade-14, higher, stage-two, or receiver equations.  These
points are source-prefix sections, not full source arcs or Keller maps.  No
Gate-T, order-two, maximum-twelve, or JC2 conclusion follows.  No AWS, CAS,
network, or `jc2-lean` was used.
