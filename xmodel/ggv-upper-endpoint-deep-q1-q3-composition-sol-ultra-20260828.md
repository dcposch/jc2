# Deep upper endpoint: licensed q1/q3 composition on the exact-D=0 branch

Date: 2026-08-28  
Author: Sol Ultra / coordinator  
Status: **EXACT PROVISIONAL DERIVATION; DIFFERENT-MODEL REVIEW RUNNING**

## 1. Result

Work over a characteristic-zero field.  Let `A` be a monic squarefree
quartic and assume the reviewed branch-P reduced prefix, the deep condition
`A|V0`, the open `c2!=0`, and the exact successor `D=R-4SU=0`.  The q1 gate
is used only after its full-system license `D23=0`; the q3 gate is used only
after `D23=D24=D25=0`.

The licensed q1 parametrization first gives

```text
R0=lambda A,
V0=3lambda A A',
S=V0/A=3lambda A'.                                   (1)
```

The reviewed D11/D12 repair on the exact-`D=0` branch gives

```text
A | L,                 L=QS+4U.                       (2)
```

Composing (1)--(2) with the licensed q3 gate gives an exact global formula:

```text
U=-(3lambda/4)(A'Q+A Q')-(9lambda^3/2)A A''',         (3)
L=-3lambda A(Q'+6lambda^2 A''').                      (4)
```

In particular,

```text
lambda=0  ==>  S=0 and U=0.                           (5)
```

This is a strict reduction of the deep endpoint branch.  It uses neither
the false claim that the shear `X -> X-(3lambda/4)t` preserves all raw
windows nor any q-gate before its licensed determinant row.  It does not
exclude the branch: the later q5, q7, q9, q11, and q13 gates and the
remaining determinant conditions are still required.

## 2. Inputs and scope firewall

The reduced prefix is

```text
F0=A^4,
F1=A^3 S,
F2=A^2(S^2+Z)/4,
F3=A(SZ+AU)/8,
S^2-2Z=AQ.                                            (6)
```

The q1 theorem says

```text
V0=A'R0+2AR0',       deg R0<=4.                       (7)
```

The implication (1) is elementary but consumes squarefreeness:
`A|V0` gives `A|A'R0`; `gcd(A,A')=1` gives `A|R0`; and the degree bound
then gives `R0=lambda A`.

The D12 input (2) is presently reviewed only on the `c2!=0`, exact-`D=0`
successor.  Mere `A|D` is not enough: the independently found valuation
repair shows that `D*B11/A^2` can retain a pole.  Accordingly, nothing
below is asserted on the other `D`-valuation branches or on the separate
`c2=0` companion.

The exact Keller identity licenses the de Rham tower.  At the finite-row
level, q3 requires all three later zero rows `D23,D24,D25`; it is not a
consequence of the endpoint subsystem `D0,...,D22` alone.

## 3. Exact q3 coefficient

Let `H=A^2`, choose the quadratic branch `p^2=A` after a harmless field
extension, so `p^4=H`, and use the reviewed coefficient

```text
q3=p^5 [ F3/(4H^2)
          -(3/32)F1F2/H^4
          +(11/512)F1^3/H^6 ].                        (8)
```

Substitution of (6) gives

```text
q3 = p(16AU+4SZ-S^3)/(512A).
```

Using `2Z=S^2-AQ`, this becomes

```text
q3=N/(512p),
N=S^3+A(16U-2SQ).                                     (9)
```

The other quadratic sheet changes only an irrelevant nonzero scalar/sign.
Formula (8) may also be recovered directly from Lagrange inversion:

```text
q_n = 2/(n+2) [t^n] F^((n+2)/8).                      (10)
```

## 4. Exactness ODE and its polynomial reduction

The odd element `q3` has a primitive in `K(X)(p)` iff its odd-character
part has one.  Writing that primitive as `p*c/512` and rescaling
`C=256c`, (9) is exact iff

```text
2A C' + A'C = N,             C in K[X,1/A].            (11)
```

Equation (11) itself forces `C` to be a polynomial.  At a simple root
`alpha` of `A`, if `C` had a pole of positive integral order `m`, the
leading coefficient on the left would be

```text
(1-2m) A'(alpha) c_(-m) (X-alpha)^(-m),
```

which cannot cancel and cannot match the regular polynomial `N`.  Thus
there are no finite poles.  Since `deg N<=9`, comparison at infinity in
(11) gives `deg C<=6`: for `deg C=d`, the leading coefficient of the left
side is `(2d+4)lc(C) X^(d+3)`, nonzero in characteristic zero.

Now substitute `S=3lambda A'`.  Reducing (11) modulo `A` gives

```text
A'C = S^3 = 27lambda^3(A')^3  mod A.
```

Squarefreeness and the degree bound therefore give a polynomial `r` with
`deg r<=2` such that

```text
C=27lambda^3(A')^2+A r.                               (12)
```

Substitution of (12) into (11), followed by cancellation of `S^3`, yields

```text
16U=2SQ+108lambda^3 A'A''+3A'r+2A r'.                 (13)
```

This is the exact q3 parametrization before the D12 lift is used.

## 5. Composition with the D12 lift

Reduce (13) modulo `A`.  From (2), `4U=-QS mod A`, so

```text
-4SQ=2SQ+108lambda^3 A'A''+3A'r  mod A.
```

Since `S=3lambda A'` and `A'` is a unit modulo squarefree `A`, this gives

```text
r=-6lambda Q-36lambda^3 A''  mod A.                   (14)
```

Both sides have degree at most two, so (14) is equality as polynomials.
Putting it back into (13) gives (3), and direct substitution gives (4).
At `lambda=0`, (14) gives `r=0`, and (3) gives `U=0`, proving (5).

The argument is stable under base-field extension and is field/radical
algebra.  It is not a nonreduced scheme-membership statement.

## 6. Why this matters next

On `lambda=0`, the preceding common-root Newton theorem also gives

```text
A|P1,  A|F7.
```

Since `S=U=R=0`, this means `F3=0` and
`F5=A^2 r5/256`.  Formula (10) immediately makes the next odd gate

```text
q5=F5/(4p).
```

Thus q5 is a small connection-image problem on a four-dimensional `r5`
window; q7, q9, q11, and especially q13 are triangular affine successors.
The last raw window has only the two coefficients `F13[X^2],F13[X^3]`
against a three-dimensional odd de Rham obstruction.  This is the sharp
finite successor: compile the licensed odd gates through q13 on both
literal q1 slices before attempting another broad 300-variable Groebner
run.

No q5--q13 incompatibility, full deep-locus emptiness, unrestricted
branch-P theorem, landing theorem, Keller theorem, or JC2 result is claimed
here.
