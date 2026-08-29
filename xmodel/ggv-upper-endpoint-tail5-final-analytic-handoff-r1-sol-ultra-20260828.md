# Final analytic handoff: cutoff-five two-branch certificates

Date: 2026-08-28  
Auditor: Sol Ultra, independent characteristic-mode lane  
Status: `INDEPENDENT EXACT REPLAY PASS; HOSTILE REVIEW STILL REQUIRED`

## Verdict of this audit

The producer packet

```text
cases/ggv_8_28_upper_endpoint_tail5_desk_20260828/
```

replays exactly and gives a complete exclusion of characteristic-zero field
points in the fixed cutoff-five endpoint specialization.  The two branches
are genuinely exhaustive:

```text
V0=0     : division-free endpoint unit over Q;
V0!=0    : D18 compatibility unit over
           K=Q[tau]/(12*tau^2+6*tau+1).
```

The final producer and certificate hashes checked here are

```text
a4f627c1bc62abc02410c3c64e03433c612cb97fa3c1ed6065238f2af65b2210
  RESULT.md
60bd4ef90fac13412e090af9f8ba6ead0d293e53b53e0b5b7520efe08d3b85e4
  CERTIFICATES/tail5_v0_unit.json
87efe8a899471d79347e7273dcd4f9b060e64877f63e974ac98bea85bf5496a2
  CERTIFICATES/tail5_v_nonzero_D18_K_unit.json
6e6ce211c1152812f639c140b384f65c51ddfedca9add1d9768df6203b224076
  TAIL5_DESK_ANALYSIS.json
f62fc30a1d26192e24e035d0645af141f90affa04247995d66e927f02cb5497e
  analyze_tail5.py
```

Running `python3 -B analyze_tail5.py --check --output .` returns `PASS` and
reconstructs both literal constants `1` without a CAS.

## Closed branch `V0=0`

Write

```text
a=p32, b=p139, c=p86, d=p91, e=p120,
v=V0, r=R0,
E0=1+a*b-c*d,
Ec=c-(3/16)*v*(v+4*r).
```

Let `E13,E14,E15` be the three frozen scalar-core equations and put

```text
G = 1-a*b+(a*b)^2.
```

The emitted generator order is

```text
E0, Ec, E13, E14, E15, v,
```

and the exact cofactors are

```text
G,
G*d,
-(2/3)*a^3*b,
-(4/3)*a^3*b,
(1/3)*a^3*(4*r+2*v),
G*d*((3/16)*v+(3/4)*r)
  +(1/3)*a^3*v^2*(v/4+r/2).
```

Independent decoding of `tail5_v0_unit.json`, multiplication of each
generator by the corresponding cofactor, and exact rational collection gives

```text
1
```

with no other term.  The core subidentity used in the cancellation is

```text
3*b^3 = 2*b*E13+4*b*E14-(4*r+2*v)*E15
        -v^3*(v/4+r/2).
```

No division by `v`, carrier localization, or root choice occurs on this
branch.

## Open branch `V0!=0`

The exact D17 residual is

```text
v*(b*v+r^2)=0.
```

After localizing only at the branch hypothesis `v!=0` and setting
`tau=r/v`, the core gives

```text
12*tau^2+6*tau+1=0,
v=tau/24,
r=-tau/48-1/288,
b=-tau/144-1/576,
e=-tau/192-7/4608,
c=tau/18432+1/36864.
```

The quadratic has discriminant `-12`, so it is irreducible over `Q`.  The
calculation works in the two-dimensional coefficient field `K`; it does not
choose either conjugate root.

I independently decoded the eight grouped compatibility entries in
`tail5_v_nonzero_D18_K_unit.json`.  Expanding every cofactor
`c0+c1*tau` into the rational rows `f` and `tau*f` gives exactly the 13
nonzero entries serialized in `expanded_nonzero_Q_witness`.  Reducing every
product with

```text
tau^2=-tau/2-1/12
```

and summing gives the literal polynomial `1`.  Thus the grouped eight-row
certificate and its 13-row rational expansion are exactly equivalent, not
merely equal up to a nonzero scalar.

The preliminary 13-term table in
`ggv-upper-endpoint-tail5-d18-quadratic-branch-unit-r0-sol-ultra-20260828.md`
was produced before the final `T=CQ` compatibility basis was frozen.  Its
row labels and several coefficients are therefore not termwise the final
RREF basis.  The final producer certificate supersedes that table; the
invariant mathematical statement—an exact `K`-linear D18 unit—is the same.

## Characteristic and radical firewalls

1. The steps from `D10` through `D15` use squarefreeness of `C=X^4-1` to
   pass from square congruences to divisibility on field points.  They are
   radical implications, not equalities of the upstream nonreduced scheme.
2. The split `v=0` or `v!=0` is a field-point cover.  Defining `tau=r/v`
   uses only the second branch hypothesis; it is not a global localization
   and does not discard a point of that branch.
3. A `K`-linear combination permits coefficients `c0+c1*tau`.  Representing
   it by the rational doubled rows `f,tau*f` is coefficient-field linear
   algebra; it does not assert that the coefficients of `1` and `tau` are
   separate determinant equations.
4. If a characteristic-zero base field does not contain a root of the
   quadratic, the open branch has no point before D18.  If it does, the
   exact unit survives scalar extension.  Hence the two conjugates are both
   covered without selecting one.
5. The slice `p129=F8[X^0]=0` is licensed by the exact additive determinant
   symmetry `F -> F+mu*t^8`.  It is not a normalization of any endpoint
   carrier.  The replay also checks that restoring `p129` changes no charged
   row.
6. The carrier relation for `c` is monic after the licensed radical
   parameterizations.  Eliminating it is not a unit normalization.  No one
   of `a,b,c,d` is set to `1` or inverted.
7. The closed branch uses the endpoint equation.  The open D18 unit does not
   use the endpoint, D19, or any later row.  `D23` is absent and there is no
   `G22` slot.
8. Rational denominators and the squarefree arguments are used only in
   characteristic zero.  No positive-characteristic strengthening is
   asserted.

The serialized regressions—carrier-term deletion, invisible-gauge restore,
charged-cofactor omission, quadratic-sign mutation, and omission of all
`tau` multiples—produce the stated nonzero failures.

## Scope

This audit supports promotion only of the statement that the fixed branch-P
square-baseline cutoff-five endpoint specialization has no
characteristic-zero field-valued point.  It is not an upstream scheme unit,
does not cover the full branch-P family or any other GGV branch, and makes no
Keller-pair, counterexample, or JC2 claim.
