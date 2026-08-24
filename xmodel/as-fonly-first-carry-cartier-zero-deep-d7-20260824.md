# AS map-only first carry: universal Cartier zero and the complete deep `D=7` branch

**Producer verdict: THE FIRST MAP-DIGIT CARRY HAS ZERO BASIC CARTIER
COEFFICIENT IN EVERY CHARACTERISTIC `p`.  ON THE `p=3,D=7` BRANCH WITH
ZERO DEGREE-SEVEN LAYER AND FROBENIUS DEGREE-SIX LAYER, FIRST-DIGIT
ACCEPTANCE IS EXACTLY A 29-ROW NONRADICAL SCHEME WITH TWO SATURATION
BRANCHES.  THIS DOES NOT DECIDE THE NEXT DEPTH OR THE FULL `D=7` LOCUS.**

- Date: 2026-08-24
- Universal lemma: exact termwise proof over every `F_p`
- Consumed corollary: `p=3`, map-only AS special fibre, total-degree cap 7
- Engines: dependency-free Python and exact Singular
- Hostile different-model review: not yet run

## 1. General-prime first-carry lemma

Let `U,V in F_p[x,y]`.  The coefficient of `x^(p-1)y^(p-1)` in the
Jacobian bracket

```text
{U,V}=U_x V_y-U_y V_x
```

is zero.

Indeed a pair of monomials

```text
u_(a,b)x^a y^b,     v_(c,d)x^c y^d
```

can contribute only when

```text
a+c=p,     b+d=p.
```

Its coefficient multiplier is

```text
ad-bc = a(p-b)-b(p-a) = p(a-b) = 0 in F_p.       (1)
```

This is a coefficient-level form of the Cartier/de Rham fact for a
polynomial Jacobian bracket.  It is termwise; no cancellation, degree cap,
or genericity assumption is used.

For the AS first carry at prime `p`, the extra seed term is

```text
-x^(p-1)V_y.
```

To contribute to `x^(p-1)y^(p-1)`, it would have to differentiate a term
`v_(0,p)y^p`, whose multiplier is `p=0`.  Therefore

```text
[x^(p-1)y^(p-1)]
  ((U_x-x^(p-1))V_y-U_yV_x)=0.                 (2)
```

Equation (2) is the universal first-carry Cartier-zero lemma.

It is not a statement that the carry itself vanishes.  At `p=3`, the
source-honest control

```text
U=x^3,       V=x^2y
```

satisfies `U_x+V_y=x^2` and gives

```text
K=(U_x-x^2)V_y-U_yV_x=-x^4 != 0,
```

while `[x^2y^2]K=0` as required.

## 2. Why the lemma is sufficient at the first `p=3,D=7` lift

If the first map digit is accepted, a second digit `(C,D)` must solve

```text
C_x+D_y=-K                                      (mod 3).       (3)
```

At cap seven, the divergence in (3) has degree at most six.  Its cokernel in
that simplex is spanned by monomials whose two exponents are both `2 mod 3`.
The only such monomial of total degree at most six is `x^2y^2`.  By (2), its
coefficient in `K` is automatically zero.

Consequently first-digit acceptance is equivalent solely to vanishing of
the terms of `K` above degree six.  Once they vanish, a canonical monomial
homotopy solves (3): integrate in `x` when `i+1` is a unit mod 3, and
otherwise in `y`; the failed case would be exactly `i=j=2 mod 3`.

This simplification is special to the **first carry**.  Later integer carry
residuals are not a single bracket of the form (2) and can, and in reviewed
controls do, have nonzero Cartier classes.

## 3. The complete deep branch

Start from the exact associated-top decomposition frozen separately.  Take
the rank-zero descendant

```text
U_7=V_7=0
```

and require `U_6,V_6` to be Frobenius polynomials in `x^3,y^3`.  Their six
coefficients have zero derivative, so they form a free `A^6` factor and do
not occur in divergence or `K`.

Retain every coefficient of `U,V` in homogeneous degrees one through five:
40 variables after target translations are normalized.  The generated ideal
contains:

- every nonzero coefficient of `U_x+V_y-x^2`: 14 rows;
- every coefficient of `K` in total degree eight: 9 rows;
- every nonzero coefficient of `K` in total degree seven: 6 rows;
- no Cartier row, because canonical term combination proves it is the zero
  polynomial.

Thus the complete first-digit acceptance ideal on this branch has

```text
variables                         40
actual rows                       29
reduced Groebner basis size       78
dimension                         19
radical Groebner basis size       45
minimal associated primes          2
minimal dimensions              18,19
minimal-prime basis sizes        22,44
```

The six free degree-six Frobenius coefficients raise the actual branch
dimensions to 24 and 25 respectively.

## 4. Exact nonradical coverage by saturation branches

The original 29-row ideal `I` is nonradical.  It is not replaced by its two
minimal primes.  Instead the replay constructs two exact saturation ideals.

Let `q4` be the explicit quartic printed by the replay on the rank-changing
degree-four intersection, and let `u5_0` be the coefficient of `y^5` in
`U_5`.  Define

```text
Q0 = I : q4^infinity,
Q1 = I : u5_0^infinity.
```

Exact saturation and ideal-containment checks give

```text
dim(Q0), size(GB(Q0)) = 18,116,
dim(Q1), size(GB(Q1)) = 19, 61,
I = Q0 intersection Q1.                              (4)
```

Moreover

```text
rad(Q0)=P0,     rad(Q1)=P1,
```

where `P0,P1` are exactly the two minimal primes above (radical basis sizes
22 and 44).  Equation (4) is equality of the original nonreduced ideal in
both directions.  Any nilpotent or embedded structure internal to a branch
is retained; no assertion that `Q0,Q1` are prime or primary is needed.

Geometrically `P0` is the rank-zero degree-five branch: `U_5=V_5=0` and the
degree-four layer remains divergence-free.  `P1` is the active degree-five
branch with its exact degree-four follower relations.  The separately
confirmed triangular point has zero degree-five and degree-four layers and
therefore supplies a positive control on the rank-zero branch.

## 5. What is and is not complete

For the stated deep branch, the producer completely characterizes which
first digits admit at least one second digit: equations (2)--(4) include all
divergence rows, all cap-boundary rows, and the only possible bounded Cartier
class.

It does not yet:

- choose or classify the affine space of accepted second digits;
- impose the next integer carry;
- cover the active degree-seven branches or the general degree-six branch;
- empty or prove nonempty any full depth-seven `D=7` system;
- produce an all-depth, characteristic-zero, counterexample, no-lift, or JC2
  conclusion.

The next exact gate should attach the accepted-second-digit affine kernel to
`Q0` and `Q1` separately, with their intersection retained, and project the
next cap-boundary/Cartier residual through a Fitting matrix.

## 6. Replay

From the case directory:

```sh
python3 replay_universal_cartier.py
python3 generate_deep_branch_gate.py | Singular -q
DECOMP=1 python3 generate_deep_branch_gate.py | Singular -q
Singular -q audit_cartier_control.sing
shasum -a 256 -c MANIFEST.sha256
```

The Python replay checks the all-prime termwise multiplier identity through
an independent bounded enumeration and reconstructs the `p=3` controls.  The
generated Singular gate canonically combines symbolic terms before emission,
so the absent Cartier row is an exact zero, not a dropped equation.

