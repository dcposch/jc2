# Terminal Laurent recurrence and residual terminal lemma

This note uses only the frozen charged inputs.  It is a proof of the closed
Laurent/Euler recurrence below and an exact finite audit of its terminal
systems.  It is **not** an all-`t` proof that the terminal ideal is the unit
ideal.  The final status is therefore `PARTIAL`.

## 1. Exact change of coordinates

Put `p=pi`, `r=p^(-1)`, and `s=h-b4`.  From

```text
h=p^4+(b1-gamma)p^3+b2*p^2+b3*p+b4
```

one gets, identically in the localization at `p`,

```text
gamma*r = Phi(h,r)
        = 1+b1*r+b2*r^2+b3*r^3+(b4-h)r^4,
J(h,r)=r^(-1).
```

The localization is injective, so an identity obtained here is an identity in
the original polynomial ring after clearing the displayed powers of `p`.
After the already-proved first spine, endpoint gauge, and normalized `x=1`
relations, write

```text
Q=U+V*r+W*r^2,
P=X+Y*r+Z*r^2+T*r^3,
```

where, with `g=g3`,

```text
U(h)=h^q + sum_(j=2)^(2t) u_j h^(q-j),
a(h)=s*C(h),                       deg C=t-1, C monic,
V=s*a-y*b3,                        W=y*s,
B(h) has degree t and leading coefficient g2,
D(h) has degree 2t and leading coefficient g1,
Y=s*D-b3*B-g*b2,                   Z=s*B-g*b3,
T=g*s.
```

Here `e=3t+1`, `q=2t+1`, and

```text
g1=e/q,
g2=(e/q)y+e*t/(2q^2),
g=t(3t+1)y/q^2-t(3t+1)(t+1)/(6q^3),
c=-y*g.
```

These formulae are a direct regrouping of the charged coefficient spaces; in
particular no interpolation in `t` is used.

Since

```text
J(Q,P)=r^(-1)(Q_h P_r-Q_r P_h),
```

the equation `J(Q,P)=c*gamma` is equivalent to the following five polynomial
identities in `h` (prime means `d/dh`):

```text
U'Y - V X'                              = c,
2U'Z+V'Y-VY'-2WX'                       = c*b1,
3U'T+2V'Z-VZ'+W'Y-2WY'                  = c*b2,
3V'T-VT'+2W'Z-2WZ'                      = c*b3,
3W'T-2WT'                               = c*(b4-h).
```

This coefficient comparison also explains the post-spine zero/duplicate
rows: once the last four displayed identities have been imposed, every
non-`r^0` coefficient vanishes identically.  Only the coefficients of the
first identity can remain.  The exact canonical comparison in Section 3
checks the identification with the charged terminal tags at `t=2,3`.

## 2. Closed Euler recurrence

The `r^4` identity gives `c=-y*g`.  The `r^3` identity simplifies without any
division to

```text
2*y*s*B' = g*(3*s*a'+2*a).
```

Evaluation at `s=0` gives `a(0)=0`, because `y` and `g` are units in `A_t`.
Thus `a=s*C`.  If `C=sum_n c_n s^n` and `B=sum_n B_n s^n`, then

```text
B_(n+1) = g*(3n+5)c_n / (2*y*(n+1)).                 (B-rec)
```

The integration constant is denoted `B_0`.  The `r^2` identity is

```text
y*(D+2sD') = E,
E = 3gU' + aB-saB'+2sa'B
             + g*b3*(a/s+(5/2)a').
```

Consequently, if `E=sum_n E_n s^n`,

```text
D_n = E_n/(y(2n+1)).                                (D-rec)
```

For the `r^1` identity put

```text
N=y*g*b1-VY'+V'Y+2U'Z.
```

The coefficient of `b1` in `N(0)` is `y*g=-c`, a unit.  Choose `b1` uniquely
so that `N(0)=0`, and then set

```text
X'=N/(2ys).                                          (X-rec)
```

This division is exact because its numerator has just been made divisible by
`s`.  The remaining integration constant `B_0` is fixed by the charged gauge
`alpha_t=0`, equivalently

```text
[h^(q-1)]X'=0.
```

The coefficient of `B_0` in this gauge is exactly `q/y`: indeed a variation
`delta B=1` gives `delta D=a/y`, cancellation in `delta N` gives
`delta N=2sU'`, and hence `delta X'=U'/y`.  Thus the gauge uses only the unit
`y` and the nonzero integer `q`.

Finally define

```text
R(h)=V X'-U'Y-y*g.
```

This note's `R` is the negative of the report's `E_t=C01`; it is exactly the
sign convention used by `terminal_laurent_model.py` and the
`terminal_laurent_t*.json` records.  Multiplying every terminal generator by
`-1` does not change its ideal.  Accordingly `R(0)=c_t`, whereas the report's
`E_t(0)=-c_t` at the residual origin.

The remaining second-spine equations are the coefficients of `R`.  In the
deterministic order used by `terminal_laurent_model.py`, they are

```text
band 4t,4t-1,...,3t+2:  C_1,...,C_(t-1),
band 3t+1,3t,...,2t+1:  u_t,...,u_(2t),
band 2t:                 b2.
```

After these affine solves, the closed terminal family is

```text
T_(t,k)=[h^k]R(h),  k=0,...,2t-1,
```

in the `t` variables

```text
b3,b4,u_2,...,u_(t-1).
```

This is an indexed closed recurrence, not a fixed-size presentation.  The
driver checks each quotient-ring inverse by multiplication modulo `H_t`, each
affine substitution on its pivot row, and every defining differential
identity after construction.

The recurrence itself only divides by nonzero rational integers and by `y`,
`g`, or `c=-yg`.  Their unit property is already charged.  Its explicit
parameter denominators divide products of

```text
2, 3, ..., 4t+1,  (2t+1),  6(2t+1)^3,
```

and hence have no positive integer root.  The later affine high-tail pivots
must still be justified by their separate resultant formula; a generic-`t`
certificate cannot silently invert them.

## 3. Exact audits

`terminal_laurent_model.py` produced exact records for `t=2,3,4`, with
respectively 4, 6, and 8 terminal rows.  Bandwise comparison modulo `H_t`
against independently reconstructed canonical terminals gives:

```text
t=2, bands 0..3:  Laurent/canonical ratios
                   -1/625,-1/125,-1/125,+1/125;
t=3, bands 0..5:  ratios +,+,-,+,-,- times 1/2401.
```

Every ratio has nonzero resultant with `H_t`.  The comparison is recorded in
`terminal_laurent_exact_comparison.json`.  The obsolete raw canonical `t=4`
replay was terminated before it emitted a record, so no independent bandwise
`t=4` comparison is claimed.

Weighted homogeneity gives, on `b4 != 0`,

```text
z=b3/b4^(t+1),  r_i=u_i/b4^i,
T_(t,k)=b4^(4t+1-k) F_(t,k)(z,r_2,...,r_(t-1)).
```

Thus the `b4=1` and `b4=0` charts exhaust geometric points (after an
algebraic extension for the weighted scaling).  The exact results are:

```text
t=2: both rational factors of split A_2, top 2 rows on b4=1 UNIT;
t=3: full b4=0 UNIT, full b4=1 UNIT, top 3 rows on b4=1 UNIT;
t=4: full b4=0 UNIT, full b4=1 UNIT, top 4 rows on b4=1 UNIT.
```

For `t=5`, modulo `1009`, `H_t` has roots `433` and `760`.  On both fibres,
the full `b4=0` chart, full `b4=1` chart, and top five rows on `b4=1` are
UNIT.  These modular calculations are discovery controls only.

## 4. The sharp remaining terminal lemma

On `b4=0`, let

```text
I_(t,+)=(T_(t,1),...,T_(t,2t-1))
        subset A_t[b3,u_2,...,u_(t-1)].
```

Exact Groebner bases show

```text
sqrt(I_(3,+))=(b3,u_2),
sqrt(I_(4,+))=(b3,u_2,u_3).
```

They contain the triangular pure powers `b3^t` and, successively modulo the
previous variables, `u_j^(t+1)`.  Modulo `1009`, both `t=5` fibres have the
same 63-monomial lead ideal, containing

```text
b3^5, u_4^6, u_3^6, u_2^6.
```

At the residual origin there is an explicit recurrence solution

```text
U=h^q, a=h^t, B=g2*h^t, D=g1*h^(2t),
X'=e*h^(e-1), b1=b2=B0=0.
```

Thus the positive powers in `V X'-U'Y` cancel, and the only nonzero terminal
row is band zero, **exactly**

```text
T_(t,0)=-y*g=c_t.
```

This is already a charged unit.  It is also related uniformly to the fifth
binomial coefficient

```text
g5=[z^5](1+z+y*z^2)^((3t+1)/(2t+1)).
```

Modulo `H_t`, with `q=2t+1`, direct reduction gives

```text
g5 = -t(t+1)(3t+1)*(10q*y-(3t+2))/(60q^5).
5q*g5=c_t=T_(t,0) at the residual origin.
```

Moreover

```text
Res_y(H_t,10q*y-(3t+2))
  =4q^2(3t+2)(4t+1),
Res_y(H_t,numerator(g5))
  =4t^2(t+1)^2q^2(3t+1)^2(3t+2)(4t+1),
```

so `g5` is a unit for every positive integer `t`.  The only displayed
denominator is `60(2t+1)^5`, which has no positive integer root.

This remains valid on every split fibre.  If `t=3s^2-1` and
`d=2q*y-(t+1)`, then `3d^2=t+1`, so the two product factors have `d=+s` and
`d=-s`; there

```text
10q*y-(3t+2)=5d+2t+3=(3s+1)(2s+1)
```

or `(3s-1)(2s-1)`, respectively.  Neither factor vanishes for `s>=1`.
No zero divisor has been inverted.

Therefore the following single radical statement would finish the entire
`b4=0` chart:

```text
RESIDUAL-ZERO:
sqrt(I_(t,+))=(b3,u_2,...,u_(t-1)) for every t>=3.
```

Indeed, modulo `I_(t,+)` the difference `T_(t,0)-c_t` then lies in the
nilradical and is nilpotent.  Since `c_t` is a unit, `T_(t,0)` is a unit in
that quotient, so `(I_(t,+),T_(t,0))=[1]`.  This argument is componentwise
valid when `A_t` is a product algebra.

The lower bound `t>=3` is necessary.  At `t=2`, all three positive-band rows
vanish after `b4=0`, so `I_(2,+)=0` and `RESIDUAL-ZERO` is false.  The full
`t=2` chart is nevertheless closed immediately by its band-zero unit; this is
the exact two-factor base calculation recorded in
`terminal_laurent_t2_product_exact.json`.  The exceptional `t=1` fibre is the
separate banked four-pivot-plus-unit base case.

A particularly cheap triangular proof target is

```text
b3^t in I_(t,+),
u_(t-1)^(t+1) in I_(t,+)+(b3),
...
u_2^(t+1) in I_(t,+)+(b3,u_(t-1),...,u_3).
```

For `b4 != 0`, the smallest observed certificate is stronger: the top `t`
rows `T_(t,t),...,T_(t,2t-1)` already generate the unit ideal after `b4=1`
for exact `t=2,3,4` and for both modular fibres at `t=5`.  The corresponding
all-`t` top-tail unit statement is the second residual lemma:

```text
TOP-TAIL-UNIT:
(T_(t,t)|_(b4=1),...,T_(t,2t-1)|_(b4=1))
  = A_t[b3,u_2,...,u_(t-1)] for every t>=2.
```

The tempting shortcut that every nonconstant term of band zero is divisible
by `b4` is false.  It holds at `t=2,3` but fails at `t=4`; terms surviving at
`b4=0` include monomials of shapes `b3^2*u_2^2*u_3`, `b3*u_2^6`,
`u_2^7*u_3`, and `u_2*u_3^5`.  The radical lemma, rather than divisibility of
band zero, is the correct induction target.

## 5. Verdict

`PARTIAL`: the terminal family now has a proved exact recurrence for `t>=2`,
with `t=1` handled by the separate exact base calculation, and
the split-algebra and denominator issues in that recurrence are controlled.
Exact terminal inconsistency is established through `t=4`, with modular
evidence at `t=5`.  What remains is precisely `RESIDUAL-ZERO` for `t>=3` on `b4=0` and
the top-tail unit statement on `b4=1` (or any equivalent all-`t` terminal
certificate).  Finite Groebner outputs are not promoted to such a theorem.
