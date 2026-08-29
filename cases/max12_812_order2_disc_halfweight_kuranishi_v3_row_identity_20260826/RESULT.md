# Result: exact K2 source/analytic direct row identity

Date: 2026-08-26

Status: **DUAL AWS PASS.  EXACT-Q SOURCE/ANALYTIC K2 ROW EQUALITY
CERTIFIED.**

The first launch attempt on each host failed before freeze validation because
the relative output path was interpreted after `run_aws.sh` changed into the
frozen repository.  Those two failures are preserved.  The nonmutating retry
passed the identical absolute output path and changed no frozen source.

Successful lanes:

```text
Q:      max12_812_order2_disc_halfweight_v3rowsr1_q_20260826T073500Z_box03
p32003: max12_812_order2_disc_halfweight_v3rowsr1_p32003_20260826T073500Z_r6d
```

Both compilers returned zero; both engines returned zero; both validators
reported `PASS_DISC_HALFWEIGHT_V3_DIRECT_ROWS`.  In exact characteristic
zero, each of the seven identities

```text
16*source_l=sum_(j<=l) T_(l,j)(b,e)*analytic_j
```

is zero coefficientwise.  The matrix `T` is lower unitriangular and comes
from

```text
q^4+b*v*q^3+e*v^2*q^2=1,  q=A/w,  v=1/w.
```

Therefore the seven complete frozen-source K2 rows and the seven analytic
K2 rows generate the same ideal over Q.  This is stronger and cheaper than
the V2 two-sided Groebner comparison, whose exact-Q lane timed out.

Scope: this proves only exact K2 source/analytic row equality.  Composition
with the separately reviewed analytic K2 support theorem and the reviewed
normalized-ray theorem excludes the nonsquare discriminant branch on
`D(b*m)` at its necessary tail gate.  The square route, Taylor conditions,
overall order two, `(8,12)`, maximum twelve, and JC2 remain open.
