# QUINTIC-Y FRONTIER PREFLIGHT — independent lane (2026-08-24)

## Verdict

**PROVISIONAL THEOREM (exact, pending hostile review).** Let `k` be a field of
characteristic zero and let `P,Q in k[x,y]` satisfy

```text
P_x Q_y - P_y Q_x in k* ,     deg_y P <= 5,     deg_y Q <= 5.
```

Then `k[P,Q]=k[x,y]`.  Equivalently, the pair is a polynomial
automorphism.

This preflight takes the independently audited `deg_y <= 4` theorem as an
input and closes every new degree-five pair.  It makes no priority claim.

Exact replay:

```bash
uv run --no-project --with sympy==1.14.0 python3 \
  cases/quintic_y_frontier_20260824/check.py
```

Current result: **24/24 exact checks pass**.

## 1. Reductions and conventions

Work first over `kbar`; write a prime for `d/dx`, and put
`K=kbar(x)`.  Actual `y`-degrees are used, so a zero leading coefficient
simply routes to a lower case.

If both actual degrees equal `r>0`, their leading coefficients `a,d`
satisfy

```text
r(a'd-ad')=0.
```

Thus `d/a` is constant and a constant target shear lowers one degree.  If
one degree is zero or one, the standard triangular argument applies.  For
example, if `P=ay+b` and `t=P`, then

```text
J(P,Q)=-a (partial Q/partial x)|_t.
```

All positive powers of `t` in `Q` have constant coefficients; the remaining
coefficient lies in `kbar[x,y] intersect K=kbar[x]`, and its derivative times
`a` is a unit.  Hence `a` is a unit and the pair is triangular.

After the `deg_y <= 4` theorem, the only new actual pairs are

```text
(2,5), (3,5), (4,5).
```

For `(m,5)`, the leading Jacobian row is

```text
5a'd-mad'=0.
```

Since `gcd(m,5)=1`, unique factorization and constant rescaling give

```text
a=h^m,       d=h^5,       h in kbar[x].
```

In each case use the common depression variable `t=hy+rho`.  The only
delicate issue is that `rho` and the depressed coefficients initially live
in `K`, not necessarily in `kbar[x]`.

## 2. Pair `(2,5)`

Depress the quadratic:

```text
P=t^2+p.
```

Solving the coefficient ODEs and removing constant multiples of `P^2`,
`P`, and `1` from `Q` gives

```text
Q=t^5+(5p/2+lambda)t^3
    +(15p^2/8+3lambda p/2+mu)t,                         (2.1)

J/h=p'(15p^2/8+3lambda p/2+mu).                         (2.2)
```

Let `C=P(x,0)=rho^2+p`, which is polynomial.  The constant `y`-coefficient
of (2.1) is exactly

```text
Q(x,0)=3rho^5/8-(5C/4+lambda/2)rho^3
        +(15C^2/8+3C lambda/2+mu)rho.                   (2.3)
```

At a finite pole of `rho`, the `3rho^5/8` term cannot cancel.  Hence `rho`
and then `p` are polynomials.  Equation (2.2), multiplied by `h`, is a
product of polynomials equal to a nonzero constant.  It forces `p'` and the
quadratic polynomial in `p` to be units.  The former makes `p` nonconstant
linear; the latter cannot then be constant.  Contradiction.

Exact pole control (`h=x^7`, `rho=x^-1`, `p=-x^-2`) gives

```text
P=x^14 y^2+2x^6 y,
J=15/4,
Q in kbar[x,y] + 3/(8x^5).
```

Thus the obstruction in (2.3) is attained exactly.

## 3. Pair `(3,5)`

Write

```text
P=t^3+At+B.
```

After solving the high coefficient rows and applying constant target shears,
the quintic is

```text
Q=t^5+gamma t^4+(5A/3)t^3
 +(4gamma A/3+5B/3+m)t^2
 +(5A^2/9+4gamma B/3+n)t
 +2gamma A^2/9+10AB/9+2mA/3.                           (3.1)
```

The last nonconstant Jacobian row is the derivative of

```text
H=36gamma AB+54mB+27nA-5A^3+45B^2=kappa.              (3.2)
```

### 3.1 Depression integrality

At a hypothetical pole of `rho` of order `s`, give `(A,B)` weights `(2,3)`
and put

```text
q=max{0,-v(A)/2,-v(B)/3}.
```

If `q>0`, the top of (3.2), `-5A^3+45B^2`, forces both `A` and `B` to
attain that scale; in particular `B` has pole order `3q`.  If `q>s`, `B`
is the unique largest pole of `P(x,0)=rho^3+A rho+B`; if `q<s`, `rho^3`
is.  Thus `q=s`.  Put

```text
A ~ a rho^2,       B ~ b rho^3.
```

Polynomiality of `P(x,0)` and `Q(x,0)` gives

```text
1+a+b=0,
a^3=9b^2,
5a^2+10a+6=0.                                           (3.3)
```

The last two equations after eliminating `b` are

```text
a^3-9a^2-18a-9=0,
5a^2+10a+6=0.
```

Their exact subresultant chain ends in `441`, so (3.3) has no
characteristic-zero solution.  Therefore `rho` is polynomial.  If `A` or
`B` then had a finite pole, the weighted top of (3.2) would make `B` have
pole order `3q`; it would be the unique pole of
`P(x,0)=rho^3+A rho+B`.  Hence `A,B` are polynomials.

### 3.2 Polynomial points on the invariant cubic

Complete the square with

```text
Z=B+2gamma A/5+3m/5.
```

Equation (3.2) becomes

```text
225 Z^2 = Phi(A),

Phi(A)=25A^3+36gamma^2 A^2+(108gamma m-135n)A
       +5kappa+81m^2.                                  (3.4)
```

If `Phi` has three distinct roots, the three pairwise-coprime polynomials
`A-r_i` must each be constant times a square.  The difference of two such
squares is a nonzero constant, so both are constant; hence `A` is constant.
That gives zero Jacobian.

Thus a nonconstant polynomial point requires a repeated root.  Write

```text
Phi(A)=25(A-r)^2(A-s).
```

Unique factorization gives, for a polynomial `R` and `epsilon in {+1,-1}`,

```text
A=s+R^2,       3Z=epsilon(A-r)R.                        (3.5)
```

Substitution in the constant Jacobian row gives

```text
J/h=R' Psi_epsilon(R),

deg Psi_epsilon=6,
LC(Psi_epsilon)=-epsilon 35/27.                         (3.6)
```

The replay checks (3.6) for both signs.  If `R` is nonconstant of degree
`d`, the right side has degree `7d-1`; it cannot be a unit.  If `R` is
constant, the Jacobian is zero.  Thus `(3,5)` is impossible.

## 4. Pair `(4,5)`

Depress the quartic and remove the constant `t^4` row of `Q` by a target
linear shear:

```text
P=t^4+At^2+Bt+C,

Q=t^5+(5A/4+L)t^3+(5B/4+M)t^2
 +(5A^2/32+3LA/4+5C/4+N)t
 +5AB/16+MA/2+3LB/4.                                   (4.1)
```

The `t^2` and `t` Jacobian rows are respectively `-I_2'/32` and
`-I_1'/32`, where

```text
I_2=5A^3+12LA^2-32NA-40AC-20B^2-64MB-96LC,

I_1=24LAB+16MA^2-64MC-32NB+15A^2B-40BC.                (4.2)
```

Both are constants.  The constant row is

```text
j:=J/h=
 [24LA C'-24LB B'-16MB A'+32NC'
  +5A^2C'-10AB B'-10B^2A'+40CC']/32.                  (4.3)
```

### 4.1 Weighted pole lemma

Give `(A,B,C)` weights `(2,3,4)`.  The weighted tops of (4.2) are

```text
a^3-8ac-4b^2=0,
b(3a^2-8c)=0.                                          (4.4)
```

Every nonzero solution of (4.4) has `c != 0`.  Indeed, setting `c=0`
forces first `a=0` or `b=0`, and then both vanish.

At a finite place define

```text
q=max{0,-v(A)/2,-v(B)/3,-v(C)/4}.
```

If `q>0`, the initial point satisfies (4.4), so `C` has exact pole order
`4q`.  (If `q=0` and `rho` has a pole, `rho^4` is already the unique
largest pole.)
If `rho` has pole order `s`, polynomiality of

```text
P(x,0)=rho^4+A rho^2+B rho+C
```

forces `q=s`: for `q>s`, `C` is the unique largest pole; for `q<s`,
`rho^4` is.

Put `A~a rho^2`, `B~b rho^3`, `C~c rho^4`.  The leading equations from
`P(x,0)`, (4.2), and `Q(x,0)` are

```text
1+a+b+c=0,
a^3-8ac-4b^2=0,
b(3a^2-8c)=0,
-1/4+5a^2/32+5ab/16=0.                                (4.5)
```

They have no solution:

* If `b=0`, then `c=-1-a`, `a(a^2+8a+8)=0`, and
  `5a^2=8`.  These force `a=-6/5` and simultaneously `a^2=8/5`.
* If `b!=0`, then `c=3a^2/8` and
  `b=-1-a-3a^2/8`.  The remaining two equations are

  ```text
  9a^4+80a^3+112a^2+128a+64=0,
  15a^3+20a^2+40a+32=0,
  ```

  whose resultant is exactly `-12180258816`.

Thus `rho` is polynomial.  If any of `A,B,C` still had a finite pole, (4.4)
would again give a pole of order `4q` in `C`, unique in `P(x,0)` because
`rho` is regular.  Hence `A,B,C` are polynomials.

### 4.2 Polynomial infinity

Suppose at least one of `A,B,C` is nonconstant, and define

```text
q=max{deg(A)/2,deg(B)/3,deg(C)/4}>0.
```

The leading point again satisfies (4.4), and exactly one of the following
three types occurs:

```text
I.    a=b=0, c!=0;
II.   b=0, a!=0, c=a^2/8;
III.  b!=0, c=3a^2/8, b^2=-a^3/2.
```

The weight-eight top of (4.3) is

```text
[5A^2C'-10AB B'-10B^2A'+40CC']/32.
```

Its coefficient in degree `8q-1` is respectively

```text
I.    5q c^2,
II.   5q a^4/32,
III.  55q a^4/32.
```

All are nonzero.  Therefore `j` has positive degree.  But `h j=J` is a
nonzero constant, so both polynomial factors must be units.  Contradiction.
If all three coefficients are constant, (4.3) is zero, also impossible.
This closes `(4,5)`.

An exact boundary control on type I is

```text
h=x^9, rho=x^-1, A=B=0, C=-x^-4,

P=x^36y^4+4x^26y^3+6x^16y^2+4x^6y,
J=-5,
Q in kbar[x,y] - 1/(4x^5).
```

Again the predicted constant-term pole is attained exactly.

## 5. Descent, scope, and review targets

The quintic cases are impossible over `kbar`; every remaining pair is an
automorphism by the `deg_y <= 4` theorem and target shears.  Therefore

```text
kbar[P,Q]=kbar[x,y].
```

Faithful flatness of `kbar/k` gives `k[P,Q]=k[x,y]`.

The two highest-value hostile-review targets are:

1. the weighted-pole assertion that every nonzero initial point of (4.2)
   has nonzero `C` coordinate; and
2. the singular-cubic pullback calculation (3.6).

Both are replayed exactly.  No canonical file is edited by this lane, and no
literature-priority claim is made.  The closest locally cited source still
requiring inspection is Y. Stein, *The Jacobian problem as a system of
ordinary differential equations*, Israel J. Math. 89 (1995), 301–319.
