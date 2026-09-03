# Residual-chart findings from the frozen inputs

## Custody

The current lane receipt was parsed mechanically with `awk`; its 17 paired
`charged_input_i_sha256` / `charged_input_i_basename` fields were piped to
`sha256sum -c` against `/tmp/jc2-lane.ZvRDkK/inputs`.  Result: 17/17 `OK`.
No in-progress lane was read.  The only new executable is
`u2_pair_recurrence.py` in this directory.

## The proved b3-axis statement, including t=2

Use `q=2t+1`, `d=2qy-(t+1)`, and `3d^2=t+1`.  On
`b4=u2=...=u_(t-1)=0`, the charged symbolic identity is

```text
C=X^(t-1), U=X^(2t+1)+a*b3*X^t, b2=0,
a=-(6dt-3d+9t^2+2t-1)/(6t(3t-1)),
[X^(2t-1)]R=lambda_b*b3^2,
lambda_b=t(3t+1)(A_b*d+B_b)/
         (12(2t+1)^2(3t-1)^2(3t+2)),
A_b=27t^3-30t^2+t-2,
B_b=6t^3+13t^2-3t+2.
```

Here `R=-E`.  The primitive norm is

```text
3B_b^2-(t+1)A_b^2
 =-(t-2)(3t-1)^2(3t+2)(27t^3+17t^2+t+2).
```

Every factor other than the leading minus sign is positive for integer
`t>=3`.  Thus `lambda_b` is a unit in both factors at every split index.
The displayed formulas divide only by `2,3,t,2t+1,3t-1,3t+2`; all are
nonzero for `t>=3`.  The upstream high solves additionally use only the
already audited `y`, `p_C`, and `p_Q` units.

At `t=2`, `d=+/-1` and the formula specializes exactly to

```text
lambda_b=14(d+1)/625=28(5y-1)/625.
```

It is zero at `d=-1,y=1/5` and nonzero at `d=+1,y=2/5`, reproducing the
charged band-three row.  Hence RESIDUAL-ZERO is false in the product algebra
at `t=2`; the separately charged band-zero row is a unit on both factors.

This remains an axis-image assertion: it says
`b3^2 in image(I_(t,+) -> A_t[b3])`, equivalently only
`b3^2 in I_(t,+)+(u2,...,u_(t-1))`.  It does not say
`b3^N in I_(t,+)`.

## Exact coefficient-pair execution of (6.4)

The new driver stores an element as `(b,a)=b+a*d` and performs all products
with `d^2=(t+1)/3`.  Its only quadratic inverse is

```text
(b+a*d)^(-1)=3(b-a*d)/(3b^2-(t+1)a^2).
```

For each fixed `t>=3`, it forms `chi,upsilon,beta,f,delta,xi,rho` exactly as
in charged (6.4), truncated through `s^(t+1)`.  It solves

```text
chi_r,       1 <= r <= floor((t-1)/2),  with p_C(t,2r,d),
upsilon_r,   ceil(t/2) <= r <= t,       with p_Q(t,2r,d).
```

For every solve at `t=3,4,5,6,11`, recomputing the response by setting the
new coefficient successively to zero and one gives exactly the charged
closed pivot, not merely a nonzero associate.  After substitution,
`rho_1=...=rho_t=0` and `lambda_2=rho_(t+1)`.

As an independent internal reconstruction, the driver expands

```text
C=X^(t-1) chi(u2/X^2), U=X^(2t+1) upsilon(u2/X^2)
```

and reevaluates charged (2.3)--(2.7) directly in the X coefficient arrays at
`b3=b4=b2=0`.  At `t=3,4,5,6,11` every band from `2t` through `4t+1`
vanishes and

```text
[X^(2t-1)]R=lambda_2*u2^(t+1).
```

The independent root implementation agrees with all four exact pairs below.

Write the reduced pair as `lambda_2=(A*d+B)/D`, with
`gcd(A,B,D)=1`, `D>0`, and put `P=3B^2-(t+1)A^2`.  Exact results are:

```text
t=3
A=899681153346875
B=-1086570502350000
D=519514327089388904
D=2^3*7^4*13*1201^4
P=2^2*5^10*11*13^2*59*1201^4*34127

t=4
A=-1006104339844786520
B=1407746074342988250
D=4333331334410427568239
D=3^9*17*1669^5
P=2^2*5^3*7^5*11*13^2*17^3*1669^5*889391

t=5
A=38786889207640490918732705042952
B=-59574542867129014865563828615560
D=40082290641637556671586770153093175
D=5^2*7^2*11^6*23*31^6*311^6
P=2^6*3^25*17^3*23*31^5*311^6*10211367113652506331367

t=6
A=-409225265156779375091329194481574600540732376295812
B=707823952399586771505495529750181559547720300904344
D=1706220079877182223299750779453007063853355587595428877
D=3^2*13^7*43*79*8693^3*20161^7
P=2^4*3*5^2*7^5*11^14*19^2*43*79*277*8693^3*20161^7
  *1125763*193855531*655055668041221
```

All displayed factors called prime were checked by exact primality testing.
In particular, `P>0`, so the u2-axis coefficient is a unit at each of the
charged nonsplit specializations `t=3,4,5,6`.  These checks agree with, but
do not replace, the charged full-radical certificates at those four values.

At the split test `t=11`, the reduced denominator factors as

```text
D=2^9*17*19*23^13*29^2*73^4*103^12*107^12*131^6*193^4*331^6.
```

The two factor values are

```text
d=+2, y=7/23:
-6177238031896341800583932478426714962914784534097465979003012517235 /
 85640045846134140549846427464640089892780731720469546129870909190045312

d=-2, y=5/23:
-78989420135234935451475848925292706365825292589619934748046875 /
 120682949885215691747048150993541893519416225027977328410273853472
```

Both are nonzero.  This is an exact two-factor check, stronger than the
suggested good-prime falsification test, but still a fixed-index test.

## Denominator provenance and the remaining norm statement

The pair recurrence is defined for every integer `t>=3`.  Before reduction,
all denominator factors come from:

```text
2, 3, q=2t+1, t+1, 3t+2;
t-2r,                    0<=r<=floor((t-1)/2);
4t-4r+1,                 0<=r<=t;
t(3t+1)F_C(t,2r),        1<=r<=floor((t-1)/2);
t(3t+1)(q-2r)F_Q(t,2r),  ceil(t/2)<=r<=t.
```

The first two indexed scalar families are at least one.  In the Q range,
`q-2r>=1`.  Charged (3.4) proves `F_C>0`; charged (3.5) proves `F_Q>=12`.
The inverse of `y` has denominator `(t+1)(3t+2)`.  Thus every actual reduced
`D_t` divides a product of factors nonzero on the full index range, including
each component of a split algebra.  There is no denominator exception for
integer `t>=3`.

What has *not* emerged is a closed, bounded-description factorization of the
sequence

```text
N_t=3B_t^2-(t+1)A_t^2.
```

The number of triangular solves grows with `t`; fixed executions do not
produce a single polynomial in `t` whose integer roots can be checked.
The exact computations give `N_t>0` for `3<=t<=20` and the exact split values
above at `t=11`, but this is finite evidence only.  On the same range they
also give `sign(B_t)=(-1)^t`, `sign(A_t)=(-1)^(t+1)`, and
`|B_t|>sqrt((t+1)/3)|A_t|`.  Thus a particularly cheap sufficient symbolic
target is the branchwise invariant
`(-1)^t lambda_2(t,+sqrt((t+1)/3))>0` and
`(-1)^t lambda_2(t,-sqrt((t+1)/3))>0`.  The precise remaining u2-axis
statement is `N_t != 0` for every integer `t>=3`, preferably proved by that
sign invariant or by a closed recurrence/product.  Calling the finite factor
tables a uniform factorization would be a specialization fallacy.

Even that statement would prove only the final u2 coordinate quotient.  It
would not prove RESIDUAL-ZERO.  A sufficient uniform triangular certificate
still has to establish actual containments

```text
b3^N0 in I_(t,+),
u_j^Nj in I_(t,+)+(b3,u_(t-1),...,u_(j+1)),
                      j=t-1,t-2,...,2,
```

with unit coefficient norms and all specialization denominators checked.
The first containment and every intermediate `u_j` step (`j>=3`) remain
open.  The cheapest falsification is to compute these quotient normal forms,
not coordinate-axis restrictions, at the split index `t=11` on both
`d=+2,-2` factors modulo a good prime.  Therefore the rigorous verdict for
part (b) remains PARTIAL / `OPEN[RESIDUAL-ZERO-UNIFORM]`.
