# Controls for `moh9966-B-lift-sol56-20260903`

## Scope and custody

The lane receipt was parsed mechanically and all 12 frozen inputs under
`/tmp/jc2-lane.kNGcqH/inputs` recomputed to the recorded SHA-256 values before
these controls were built.  The driver is `controls_replay.py`; the complete
machine record is `controls_results.json`.  All generated files are indexed by
`artifacts.sha256` (the shell-owned stdout/stderr capture files are deliberately
excluded because they remain open while the driver writes its manifest).

Reproduction from `/home/ubuntu/jc2`:

```text
python3 -u box/moh9966lift-20260903/controls/controls_replay.py >/dev/null
sha256sum -c box/moh9966lift-20260903/controls/artifacts.sha256
```

Measured software: Python 3.12.3, SymPy 1.12, Singular 4.3.2.  No failure
marker occurred.

## Branch A predecessor control

This is exactly the frozen 14-unknown predecessor, not Moh's unprinted
ten-variable eta system.  It is built in

```text
Q[h_0_8,...,h_0_0,bp,bq,br,bs,c,T]
```

from

```text
h = y^8(y-x) + sum_(j=0)^8 h_0_j y^j,
A = (h-h|_(y=0))/y,
beta = bp*A+bq*y+br*x+bs,
alpha = quotient_y(beta^2,h),
f = h^2+2*beta,
g = h^3+3*beta*h+(3/2)*alpha.
```

H-adic extraction of `J(f,g)-c*x^4` gives 29 generators.  Generator 0 is
`-c`, so after adjoining `T*c-1` there is the explicit certificate

```text
1 = -(T*c-1) - T*(-c).
```

The unsaturated ideal is nonunit.  Singular returned `[1]` over
`F_32003`, `F_32009`, `F_32027`, and `Q`.  In every ring the declared-ring,
empty wrapper, nonempty wrapper, unsaturated-nonunit, and result-ideal/ring
checks passed.  The exact rational transcript is
`branch_A_predecessor_Q.log`.

Typed result: `SATURATED-EMPTY[CONTROL-ANSATZ]`.  It calibrates the solver but
does not prove the missing bridge from every branch-A candidate to this
predecessor.

## Branch C exclusion

This is conditional on the fixed-radius-two `deg R=40`, `ord R=-25` leading
datum used in the task.  For squarefree

```text
H=z(z-a)(z-b),  a*b*(a-b) != 0,
```

the face ODE `2*H*R'-25*H'*R=k*H^14`, `k!=0`, forces `H^13|R`.
Writing the remaining monic linear factor as `L=z+ell` gives

```text
H'*L+2*H*L'-k*H=0.
```

Its four coefficients are

```text
f1 = 5-k,
f2 = (k-4)(a+b)+3*ell,
f3 = (3-k)*a*b-2(a+b)*ell,
f4 = a*b*ell.
```

In `Q[a,b,ell,k,T]` add `f5=T*a*b*(a-b)*k-1`.  With `s=a+b`, `p=a*b`,
and `d=a-b`, the independently expanded certificate is

```text
m1=T*d*k*(p/2-ell*s),  m2=-T*d*k*ell,  m3=-T*d*k/2,
m4=3*T^2*d^2*k^2*ell, m5=-3*T*d*k*ell^2-1,
1=m1*f1+m2*f2+m3*f3+m4*f4+m5*f5.
```

The unsaturated system is nonunit (for example
`a=b=ell=0,k=5`).  Singular returned `[1]` over the same three primes and
over `Q`; all ring and positive/negative wrapper controls passed.  See
`branch_C_exclusion_Q.log`.

Typed result: `SATURATED-EMPTY[FIXED-RADIUS-TWO]`.  This does not exclude a
split at a different radius.

## Moh `(16,12)` control

### Source-shaped p.208 predecessor

Moh's p.207 row is

```text
(n,m,M2,V2,delta2,delta1,J)=(16,12,13,3,-1,1/4,X).
```

Page 208 prints

```text
h=y^3(y-x)+b1*y^3+b2*y^2+b3*y+b4=y*A+b4=y^2*B+b3*y+b4,
alpha2=c1*A+c2,             beta2=c3*A+c4,
alpha3=c5*A+c6*B+c7,        beta3=c8*A+c9*B+c10,
alpha4=c11*A+c12*B+c13(y-x).
```

After absorbing the constant `alpha1`, set

```text
f=h^3+beta2*h+beta3,
g=h^4+alpha2*h^2+alpha3*h+alpha4.
```

All coefficients of `J(f,g)-c*x` give 77 equations in 18 unknowns
`b1..b4,c1..c13,c` (plus Rabinowitsch `T`).  The raw ideal has the exact
origin with `c=0`.  Over `Q`, the extended ideal has reduced basis `[1]`; all
ring, actual-pair, empty/nonempty-wrapper, and origin controls pass.  See
`moh1612_literal_p208_Q.log`.

This is a source-shaped 17-coefficient predecessor plus the Jacobian scalar.
Moh says that an eta change reduces 17 coefficients to 10, but does not print
that ten-variable system.  The replay must not be attributed to an unprinted
elimination.

### Order-band / second-spine calibration

The frozen `t_order_system.py` at `t=1`, with its three safe target gauges,
builds a necessary order-chart superset for the same tuple.  It has 23 rows in
18 chart unknowns including `c`.  The rows by descending `h` band are

```text
h^5: 1, h^4: 2, h^3: 2, h^2: 5, h^1: 6, h^0: 7.
```

The frozen constant-pivot rule (descending band, then remainder tag and
original variable order) makes these seven `Q*` pivots:

| step | source | band | tag | variable | coefficient |
|---:|---:|---:|---|---|---:|
| 1 | 22 | 5 | `(0,1)` | `a2_1` | `3` |
| 2 | 21 | 4 | `(0,0)` | `a3_2` | `6` |
| 3 | 20 | 4 | `(0,1)` | `a3_1` | `3` |
| 4 | 19 | 3 | `(0,0)` | `a4_2` | `6` |
| 5 | 18 | 3 | `(0,1)` | `a4_1` | `3` |
| 6 | 14 | 2 | `(0,3)` | `a4_0` | `-12` |
| 7 | 13 | 2 | `(1,2)` | `a4_3` | `-9/4` |

The resulting exact ring map was checked on every one of the original 23
generators.  It leaves 15 rows in 11 unknowns including `c`; the complete
right sides are in `moh1612_t1_Qstar_pivots.tsv`.  Both the full chart and this
residual return `[1]` over `Q` with every wrapper/ring/actual-pair control
passing.

The residual has a unique primitive positive grading

```text
b1:1,b2:2,b3:3,b4:4, a2_0:8,a3_0:12,
q2_0:8,q2_1:5,q3_0:9,q3_1:10,c:25.
```

Put `x=q2_1`, `y=q3_1`.  Two exact rows give

```text
c=4*x*y*(x^2-9*y)/81,
Hhom=5*x^4-36*x^2*y+54*y^2.
```

Since `c!=0`, `x!=0`; the verified positive grading permits the torus slice
`x=1` over the algebraic closure.  Then

```text
H=54*y^2-36*y+5, disc(H)=216,
cbar=-4*y*(9*y-1)/81.
```

`H` is irreducible over `Q`.  The exact `c`-unit certificate is

```text
cbar*(2187*y/5-2187/10)-1 = -(18*y+1)*H/5.
```

After rational-associate deduplication there are 11 nonzero rows over
`K=Q[y]/(H)` in eight auxiliary unknowns.  Four checked affine pivots are:

| step | band/tag | variable | coefficient | inverse modulo `H` |
|---:|---|---|---|---|
| 1 | `1/(1,2)` | `q3_0` | `3-9y` | `2-6y` |
| 2 | `0/(1,1)` | `b4` | `60y-10` | `9/10-9y/5` |
| 3 | `2/(0,1)` | `b2` | `36y-4` | `1/2-9y/10` |
| 4 | `1/(0,0)` | `a3_0` | `27y-9` | `2y-2/3` |

Each inverse and pivot-row substitution was checked modulo `H`.  A remaining
band-zero row is the coefficient-field unit

```text
u=20*y-10/3,  v=27/10-27*y/5,
u*v-1=-2*H, hence 1=u*v+2*H.
```

This is the explicit terminal certificate.  The normalized Singular replay
checks both `cbar` and `u` as units, repeats wrapper controls in the coefficient
ring and final polynomial ring, and returns `[1]`; see
`moh1612_t1_normalized_unit_Q.log`.

Typed result: `SATURATED-EMPTY[ORDER-CHART-CONTROL]`.  It is the requested
positive calibration that the lifting machinery detects the known
Appendix-II obstruction.  Because the order chart is only a necessary
superset and Moh's eta system is unprinted, it is not a claim that these are
Moh's literal ten variables or pivots.

