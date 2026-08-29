# Affine-Faber `A`: correction-complete half-weight face through tau 90

Date: 2026-08-26

This is the ramified `q=15/2` successor to the relative-order-six
loaded-kernel gate.  Put

```text
sigma=tau^2,       Lambda=sigma^3=tau^6,
t=sigma^5=tau^10,  H=15 in sigma units=tau^30.
```

On the repeated moving-double-root chart, with `A=z-a`, write

```text
Q=A^2*(A^2+4*a*A+e) + X*A + R1*A+R0,
N=tau^30*(m*A*(A^2+4*a*A+e) + Y*A + m*X/2 + S1*A+S0).
```

The half-weight coordinates have `ord_tau(X)=ord_tau(Y)=15`.  The two
complementary linear polynomials have doubled relative order 30: `R` has
physical order 30 and `S`, which is inside the displayed `tau^30` factor,
has physical order 60.  The compiler retains both kernel coordinates,
all four complement coefficients, arbitrary moving `e,m` tangent jets
capable of meeting the window, moving center `a=tau^10*(...)`, every
coefficient of each of `k10,k6,k2,mu2` in absolute grades 84--90, and all
seven complete frozen ordinary-Faber rows.  Higher kernel jets raise the
first K2 term above grade 90; higher tangent jets likewise cannot lower a
term into this window.

The delayed-load exponent census is

```text
three leading loads and mu2 target     84,...,90,
half-weight K2 quadratic/cubic tie     90,
moving-center/load interaction         >=94,
mu4, mu6, J targets                     96,108,114.
```

Thus no `mu4`, `mu6`, or `J` coefficient is capable of entering this
client.  They are excluded by weight, not set to zero in a window where
they could contribute.

The compiler verifies the ordinary-Faber connection independently.  If
`P1,...,P5` are the source rows, `b=4*a`, and `e` is the moving quadratic
coefficient, the inverse unitriangular rows used here are

```text
H3 = P3-(b/2)P2+(5*b^2/32-e/4)P1,

H5 = P5-b*P4+(21*b^2/32-3*e/4)P3
       +(-5*b^3/16+3*b*e/4)P2
       +(195*b^4/2048-45*b^2*e/128+5*e^2/32)P1.
```

The preregistered exact identities are

```text
[tau^90]H3 = -(3/8)*m*x*y-(1/16)*m^3,
[tau^90]H5 =  (3/8)*p*m*x*y.
```

Consequently these two rows generate the unit ideal on `D(p*m*k10_0)`:
the second kills `x*y`, and the first then kills the unit `m`.  This unit
endpoint is preregistered, but only a fail-closed exact-Q AWS replay is
mathematical evidence.  Characteristic 65521 is a software control.

The actual half-weight exceptional divisor additionally has
`(x,y)!=(0,0)`.  No projective split is needed because the displayed ideal
is already the unit ideal before imposing that nonvanishing condition.

Scope: the fixed delayed-load repeated-root `A` face at `q=15/2`, through
absolute tau grade 90.  The separate `q=6` gate, the homogeneous open
intervals, `q>15/2` (which remains governed by the sigma-45 scope
erratum), `m=0`, terminal/Taylor receivers, other load slopes, total fan,
order two, and JC2 are outside this registration.
