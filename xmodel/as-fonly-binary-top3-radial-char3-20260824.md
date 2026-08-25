# AS F-only `D=7`: pure-`N` top-three radial identities

**Status: PRODUCER EXACT; PROVISIONAL PENDING DIFFERENT-MODEL REVIEW.**

## Exact identities

Write the current cap-seven digit by homogeneous degree as

```text
C=C7+C6+C5+...,   D=D7+D6+D5+... .
```

On `y != 0`, put `t=x/y`, and let `c_i(t),d_i(t)` dehomogenize
`C_(7-i),D_(7-i)`.  The degree `12-r` coefficient of the pure quadratic
carry `N={C,D}` is

```text
sum_(i+j=r) ((1-j)c_i' d_j + (i-1)c_i d_j').       (1)
```

For the first three rows in characteristic three, (1) becomes

```text
N12 = c0'd0-c0d0',
N11 = c1'd0-c0d1',
N10 = (c2 d0-c0 d2)'.                              (2)
```

In particular, `{C6,D6}=0` for every pair of homogeneous degree-six binary
forms, not only for the six Frobenius spectator directions.  Therefore all
three rows in (2) are independent of those spectators.  The degree-ten row
is equivalent to

```text
c2 d0-c0 d2 in F3[t^3].                            (3)
```

## Derivation

Set `u=1/y` and factor

```text
C=u^-7 c(t,u),  D=u^-7 d(t,u),
c=sum_i u^i c_i(t),  d=sum_j u^j d_j(t).
```

The coordinate change gives

```text
{C,D}=u^-12 [c_t d-c d_t+u(c_u d_t-c_t d_u)]       (4)
```

in characteristic three, since `7=1`.  Extracting the coefficient of
`u^r` in (4) gives (1).  Formula (2) follows by setting `r=0,1,2`; the
middle pair at `r=2` cancels because both forms have degree six, divisible
by three.

Combining (2) with the frozen Wronskian normal form

```text
c0=h a^3,  d0=h b^3
```

turns `N11=0` into

```text
b^3 c1'=a^3 d1'.                                  (5)
```

For the three gcd strata this has the following exact consequences:

- `deg h=1`: coprimality of the quadratic `a,b` forces `c1'=d1'=0`;
- `deg h=4`: for coprime linear `a,b`, one has
  `c1'=a^3 q,d1'=b^3 q` with `deg q<=1`;
- `deg h=7`: for constant `(a,b) != (0,0)`, one has
  `c1'=a q,d1'=b q`, where `q` lies in the derivative image (its `t^2`
  and `t^5` coefficients vanish).

For the middle stratum, divisibility first gives `deg q<=2`; the forbidden
`t^2,t^5` derivative coefficients of `a^3q` force the quadratic coefficient
of `q` to vanish.  For the first stratum, at least one coprime homogeneous
quadratic has full dehomogenized degree two, while `c1',d1'` have degree at
most five, forcing the common quotient to vanish.

## Scope

The portable replay checks (2) coefficientwise with generic symbolic forms,
the universal degree-six cancellation, and a nonzero nearby control.  These
are pure-`N` identities.  They do not assert that any normal-form stratum
meets the predecessor accepted-digit gate or passes lower quotient/cross
rows.  No recurrence, all-depth, characteristic-zero, no-lift,
counterexample, or JC2 inference is made.
