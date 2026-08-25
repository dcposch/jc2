# Preregistration: rank-drop `b=1` slope-three continuation

Date: 2026-08-25  
Status: **FROZEN BEFORE CAS**

Use exactly the pinned six-row corrected-Q8 source.  First verify the
weighted leading chart

```text
d4=b,
d2=b+1+Q1*t,
x5=z*t+Z2*t^2,
x3=z*t+X2*t^2,
x1=U2*t^2,
w=W*t^3.
```

On `D(z)`, coefficients through order three must force

```text
b=1,
U2=0,
Q1=(c-1/3)*z,
X2-Z2=-z^2/3,
W=2*z^3/9.
```

Then normalize the unramified transverse coordinate by `x5=t` and use

```text
c_src=c+C1*t,
d4=1+B1*t+B2*t^2,
d2=2+(B1+c-1/3)*t+(B2+Q2)*t^2,
x3=t-t^2/3+X3*t^3,
x1=U3*t^3,
w=2*t^3/9+W4*t^4.
```

For `A=C1-Q2`, check that the `t^3` coefficients of the upper rows
`e1,e5,e7`, up to individual nonzero rational scalars, generate the same
ideal as

```text
9*(A+U3)+c+1,
-26*c-27*B1+9*(A+U3)-15,
83*c+81*B1+18*(A+U3)-58.
```

This ideal must be the unit ideal; equivalently the first two imply
`B1=-c-16/27` and the third reduces to `-108`.

Acceptance requires two exact-Q AWS engines/orders, mutual ideal
containments for both the leading chart and continuation obstruction, fixed
source hashes, and no diagnostics.  The theorem scope is only unramified
arcs with `ord(x5)=1` in this chart.  Ramified arcs with earlier drift of
`c,d4,q` remain charged.

