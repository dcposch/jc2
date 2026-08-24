# AS gauge growth at p=3, depth five: an exact cap-eight survivor

**Producer verdict: `B_(3,5)(8,8)` IS NONEMPTY.  THE PREDICTED CAP-NINE
LAW FAILS AT DEPTH FIVE.**

- Date: 2026-08-24
- Arithmetic: exact integers reduced coefficientwise modulo `3^5=243`
- Support grammar: total-degree simplices only
- Status: producer result; independent Singular replay included; required
  different-model hostile review not yet run

## 1. Strict verdict

There is an exact point of the frozen bounded system
`B_(3,5)(8,8)`.  Consequently

```text
D_min(3,5) <= 8 < 9 = (5-1)(3-1)+1.
```

This falsifies the proposed formula
`D_min(p,n)=(n-1)(p-1)+1` at `(p,n)=(3,5)`.  It does **not** determine the
minimum: cap seven remains open.

The pre-result decision rule supplied by coordination was: test the
predicted cap nine against every cap at most eight, and treat a depth-five
survivor below nine as a falsification of the cap-growth law, not as a
polynomial lift.  The present point triggers exactly that rule.

## 2. Exact point

Work in `(Z/243Z)[x,y]`.  Put

```text
c = x^5(1-y),
d = x^4(1+y+y^2),
f = 7x^4 y + 5x^4 y^2,

A = x + 9c,
B = y + 9d + 27f
  = y + 9x^4 + 198x^4y + 144x^4y^2.
```

Thus `deg A=deg B=6`.  With

```text
S_5(A)=1+3A^2+9A^4+27A^6+81A^8,
P=A-A^3,
Q=B S_5(A),
```

the reduced coordinates are

```text
P = x + 242x^3 + 9x^5 + 234x^5y + 216x^7 + 27x^7y,

Q = y + 3x^2y + 9x^4 + 207x^4y + 144x^4y^2
      + 27x^6 + 189x^6y + 135x^6y^2 + 81x^8.
```

Hence `deg P=deg Q=8` and
`F=(P,Q)=(x-x^3,y) mod 3`.

## 3. Orientation and determinant

Let `D(A)=1-3A^2`.  The finite geometric identity gives

```text
D(A) S_5(A) = 1 mod 243.
```

Therefore `B=QD(A)` and the point has the frozen orientation

```text
C_3 o (A,B) = (P,Q).
```

Both replay engines independently verify

```text
det J(A,B)=1 mod 243,
det J(P,Q)=1 mod 243.
```

The first identity is also transparent from the construction.  Exact
integer differentiation gives

```text
c_x+d_y = 3x^4(2-y),
f_y     = x^4(10y+7),
{c,d}   = -3x^8(2y^2-3y-3).
```

Since `A=x+9c` and `B=y+9d+27f`, modulo 243,

```text
det J(A,B)
 = 1 + 9(c_x+d_y) + 27f_y + 81{c,d}
 = 1.
```

Indeed the first two corrections sum to `243x^4(1+y)`, while the bracket
is already a multiple of three.  This is the carry mechanism missed by
the naive two-row induction.

## 4. Structural counter-motif

The depth-four certificates suggested that the final cotangent class
should persist to degree nine.  At depth five it can instead move through
three linked rows:

1. `c=x^5(1-y)` and `d=x^4(1+y+y^2)` cancel the high part of
   `x^4d+x^3cy+x^8y` in the final `Q` digit.
2. Their divergence is not zero over the integers, but is exactly a
   multiple of three of degree at most five.
3. The next digit `f` absorbs that divided divergence, while the remaining
   quadratic bracket `{c,d}` is itself a multiple of three and therefore
   disappears at modulus 243.

Thus the obstruction is neither confined to the y-linear quotient nor to
the top associated symbol.  Nonlinear carries can make the apparent final
quadratic class a determinant coboundary one digit later.

## 5. Controls and exact replay

The integer-only Python producer reconstructs all products and
derivatives, asserts the exact supports and degrees, checks the truncated
inverse and orientation, and checks both determinants.  The independent
Singular script repeats the calculation directly over `Z/243Z`.

Run:

```sh
python3 replay_n5_d8_survivor.py
Singular -q audit_n5_d8_survivor.sing
```

The identity gauge remains the pinned positive control at cap nine:

```text
A=x, B=y,
Q=y(1+3x^2+9x^4+27x^6+81x^8),
deg Q=9.
```

The new point is a strictly better bounded control; it does not make the
identity control incorrect.

## 6. Refusal scope

This artifact makes none of the following claims:

- that cap eight is minimal (cap seven is unresolved);
- that this point extends to depth six or to any compatible tower;
- that a polynomial or Tate-algebra lift exists;
- that an `A_infinity` object has been identified;
- that any no-lift theorem fails;
- that the plane Jacobian conjecture follows or fails.

It is one exact finite-depth survivor and one exact falsification of the
proposed numerical cap-growth law.
