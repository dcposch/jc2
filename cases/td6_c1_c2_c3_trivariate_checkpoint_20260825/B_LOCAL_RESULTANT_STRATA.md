# Exact split of the corrected B3-local resultant debt

Work on the chart `U != 0` and put

```text
x=C/U^2,  y=V^2/U^3.
```

This is only an exact description of the weighted-homogeneous component
equations; it is not a gauge or a quotient of the source family.  Dividing
`B3` by `U^6` gives

```text
b(x,y)=4x^2-4xy+24x+y^2-20y+20.
```

The five nonmonomial factors of the actual V14 relation denominator restrict
respectively to

```text
l1=x-y+1,
l2=2x-3y+2,
l3=3x-3y+11,
l4=4x-3y+4,
t =4x^2-4xy+28x+y^2-24y+24 = b+4l1.
```

Direct substitution into `b` gives the exact elimination ledger

```text
b|l1=0 = y^2,
b|l2=0 = 4y(y+2),
b|l3=0 = (9y^2-96y-128)/9,
b|l4=0 = y(y-16)/4,
{b=t=0} = {b=l1=0}.
```

Hence `y=0` is the already closed divisor `V=0`.  Off `U V=0`, the complete
new B3-local debt consists of exactly three source-typed curves:

```text
C=11U^2,             V^2=16U^3;
C=-4U^2,             V^2=-2U^3;
C=(y-11/3)U^2,       V^2=yU^3,
9y^2-96y-128=0.
```

The first two equations follow from `l4=0,y=16` and `l2=0,y=-2`; the third
is `l3=0`.  Their common `U=0` specialization is the raw origin already
proved empty.  None is killed by this algebraic split: each requires a raw
transport/first/P12 rebuild over its exact function field.

