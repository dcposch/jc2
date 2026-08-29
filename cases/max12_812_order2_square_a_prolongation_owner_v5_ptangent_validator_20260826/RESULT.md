# Result: moving-`p` tangent addendum to the square A-prolongation

Date: 2026-08-26

Status: **DUAL-AWS EXACT-Q / GOOD-PRIME PASS.  MOVING-BASE ADDENDUM ONLY;
NO FAN, SQUARE-BRANCH, OR ORDER-TWO VERDICT.**

The exact-Q Box03 lane
`max12_812_order2_square_aprolong_owner_v5_ptangent_q_20260826T081800Z_box03`
and the independent `F_65521` r6d lane
`max12_812_order2_square_aprolong_owner_v5_ptangent_p65521_20260826T081800Z_r6d`
both returned engine rc `0` and validator
`PASS_SQUARE_APROL_PTANGENT_V5`.  Exact-Q stdout SHA is
`933e6a87342e0797641206ede622136a841ba76cd9f5c96da3f8e33a45be1fd0`;
good-prime stdout SHA is
`dfd0be88c169e258ed4d68509e77bc111a01770d94b04bd574ead6eff65b0383`.

Under

```text
p -> p+2*sigma*ell,
L(sigma)=z^2+p/2+sigma*ell,
```

all seven complete source rows remain exactly divisible by `sigma^14`.
Their grades fourteen and fifteen satisfy the exact moving row identities

```text
g14 = T(p) h14,
g15 = T(p) h15moving + 2*ell*(dT/dp)(p) h14,
```

where `T` is lower unitriangular.  Every later load/target is absent at
these grades.

For the grade-fourteen cleared numerator and the moving-base correction,
both fields certify the polynomial identities

```text
Num14   == -12*B*A^2                 (mod L),
Delta   ==  12*ell*B*A^2             (mod L),
Delta   == -ell*Num14                (mod L).
```

Consequently, after the grade-fourteen equation, the moving-`p` tangent
does not change the grade-fifteen separator:

```text
Num15moving == -A^3                  (mod L, Num14).
```

Thus the fixed-`p` high-contact conclusion `A=0` on `D(p)` is stable under
the omitted tangent along the generic square component.

V3 is preserved as a pre-engine wrapper-anchor failure.  V4 is preserved as
an engine-pass/validator-prefix failure.  V5 changes only the validator
spelling and is the promotable evidence package.

The result still covers only the high-contact cone after the reviewed
half-weight receiver.  In particular the lower rays with `ord(R)=1` or
`ord(C)<=3`, the `p=0` intersection, later terminal/Taylor receivers, the
whole square branch, and all order two remain open.
