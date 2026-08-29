# Deep q1 lambda-zero branch: licensed q15 and the surviving odd fiber

Date: 2026-08-28  
Lane: independent full-system successor  
Status: **EXACT q15; UNIVERSAL q5--q15 SURVIVOR DIMENSION AT LEAST FIVE ON r=0; GENERIC DIMENSION FIVE**

## 1. Result

Continue on the reviewed characteristic-zero, squarefree branch-P component
with `c2!=0`, exact `D=0`, and

```text
lambda=0,  S=U=0.
```

The finite raw support really licenses q15 in the full determinant system:
`D35` is the last potentially nonzero determinant coefficient, while `D36`
and `D37` vanish identically.  No extra raw row is being assumed.

Writing `q15=p^3 h15`, with `p^2=A`, the exact coefficient is

```text
h15 = -9 A^2 Q F13/2^8 +45 A Q^2 F11/2^15
       +F9(9e/2^16-15Q^3/2^21)
       +f(9F8/2^5-9Qe/2^22-45Q^4/2^29)
       +r(9A F10/2^13-9QF8/2^19
           -27Q^2e/2^37-63Q^5/2^43)
       +3A r^3/2^33.                                 (1)
```

Here

```text
F5=A^2r/256,  F6=Ae/2048,  F7=Af.
```

The final term in `(1)` is the new three-odd-partition load from
`5+5+5`; omitting it is false.

The q15 gate does **not** exclude the branch.  On the exact sub-slice
`r=0`, q5 is automatic and the combined q7, q9, q11, q13, q15 system is
homogeneous linear.  With every literal lower and upper raw floor retained,
its raw solution space has dimension at least five for every fixed legal
even prefix.  On a nonempty Zariski-open set it has dimension exactly five.

The reviewed four-root leading endpoint system is even-only.  Composing it
with q15 therefore leaves this at-least-five-dimensional odd fiber over
every surviving even endpoint point.  The smallest remaining leading-face
resultant is a 15-equation system in `K[X]/(A)` described in Section 7;
half-step odd equations or later odd gates must be added to go further.

## 2. Frozen predecessor and scope

This pass pins but independently reconstructs the preceding odd-tail packet:

```text
xmodel/ggv-upper-endpoint-deep-q1-lambda0-odd-gate-tail-independent-sol-ultra-20260828.md
SHA256 b649e0821a07fa8d3ed861169b608a5b4dcd8356452f875b8b218693d3cb69a0

cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_odd_gate_tail_20260828/
  verify_lambda0_odd_gate_tail.py
SHA256 c063ccc20c12785d092f56c65e2def86215ae1cc49fb6c3cf8ab4754e1c782ca
```

The authoritative raw odd windows are

```text
r:   degrees 0..3,
f:   degrees 0..5,
F9:  degrees 1..7,
F11: degrees 1..5,
F13: degrees 2..3,
F15: absent.                                             (2)
```

The result is a full-system de Rham consequence.  It is not licensed in the
D22-only endpoint truncation.

## 3. Exact finite-support license

The raw source has

```text
F_i=0 for i>=15,
G_j=0 for j>=22.
```

Every determinant term at weight `n` pairs one `F_i` and one `G_j` with
`i+j=n`; differentiation in `X` and multiplication by `t partial_t` do not
change that weight.  Therefore

```text
max raw determinant weight = 14+21=35.                 (3)
```

The pair `(14,21)` is present, so D35 is not identically zero and must be
imposed.  There is no pair at weights 36 or 37, hence

```text
D36=D37=0 identically.                                 (4)
```

Once the full-system rows D23 through D35 vanish, `(3)`--`(4)` allow the
exact identity to be written as

```text
E=t^22+O(t^38).
```

The reviewed tower licenses q_n whenever `n+22<N`; for q15,

```text
15+22=37<38.                                           (5)
```

Thus q15 is licensed after D35, with D36 and D37 supplied by finite-support
identities.  It is not licensed before D35.

## 4. Independent q15 derivation

Use the Lagrange coefficient

```text
q15=2/17 [t^15]F^(17/8).                               (6)
```

Normalize by `F0=A^4`.  The nonzero reduced coefficients relevant through
weight 15 are

```text
F2=-A^3Q/8,        F4=A^2Q^2/256,
F5=A^2r/256,       F6=Ae/2048,       F7=Af,
F8,F9,F10,F11,F13,
```

with F15 absent.  An odd weight-15 partition has either one odd part or
three odd parts.  The only three-odd partition is `5+5+5`.  Consequently

```text
[t^15]F^(17/8)
 = (17/8) [one-odd contribution]
   + binom(17/8,3) F5^3 F0^(-7/8),                    (7)
```

where

```text
(2/17) binom(17/8,3)=3/512.
```

Expanding the one-odd term against the even normalized series through
weight ten and reducing powers with `p^2=A` gives `(1)`.  The frozen checker
performs this directly in a sparse Laurent polynomial ring from
`(F/F0)^(17/8)` and verifies cancellation of every negative `A` exponent.
It also rejects deletion of the cubic `3Ar^3/2^33` term.

## 5. Exactness equation

The preceding independently proved connection theorem applies unchanged:

```text
p^3h dX is exact in K(X,p)
 iff h=T5(d):=(5A'd+2Ad')/2 for some d in K[X].         (8)
```

Necessity includes the finite-pole argument and the two reductions modulo
squarefree `A`; sufficiency is the identity

```text
d(p^5d)=p^3 T5(d)dX.
```

Since `(1)` has degree at most 13, q15 exactness is the finite equation

```text
h15=T5(d15),                 deg d15<=10.               (9)
```

The leading coefficient of `2T5(X^k)` is `2k+20`, so `T5` has no
polynomial kernel in characteristic zero.

## 6. q5--q15 remain consistent: universal and generic dimensions

Set `r=0`.  This is an exact allowed sub-slice, not a localization or a
closure argument.  Then q5 vanishes and `(1)` loses both its F10 term and
its cubic term.  For fixed `(A,Q,e,F8)`, the five remaining equations

```text
h7=T5(d7), h9=T5(d9), h11=T5(d11),
h13=T5(d13), h15=T5(d15)                              (10)
```

are homogeneous linear in the literal raw variables

```text
f, F9, F11, F13
```

and primitive variables.  Their exact dimensions are

| object | dimensions |
|---|---:|
| raw `f,F9,F11,F13` windows | `6+7+5+2=20` |
| primitives `d7,d9,d11,d13,d15` | `3+5+7+9+11=35` |
| coefficient equations, degrees through `5,7,9,11,13` | `6+8+10+12+14=50` |

Thus the extended kernel has dimension at least

```text
20+35-50=5.                                            (11)
```

Projection to the raw variables is injective because `T5` has zero kernel.
Therefore `(11)` is a universal lower bound on the legal raw odd survivor,
for every fixed legal even prefix.  In particular, q15 cannot be a universal
contradiction.

The exact checker builds all 50 rows with the literal floors in `(2)`.  On
both

```text
A=X^4-1,
A=X^4+X+1,
```

and unrelated dense legal choices of `Q,e,F8`, it finds

```text
rank=50, columns=55, nullity=5.                         (12)
```

Because a maximal minor is nonzero at either fixture, rank 50 holds on a
nonempty Zariski-open set of even prefixes.  Hence the generic raw dimension
on the `r=0` slice is exactly five.  Special prefixes can only enlarge this
fiber.

## 7. Composition with the four-root endpoint system

The leading common-root face depends only on the even data.  In the quotient
algebra

```text
R=K[X]/(A),                  dim_K R=4,
```

put

```text
P(z)=(1-Qz/16)^2+e z^3/2048+F8 z^4,

C(z)=P(z)^(3/2)
     +sum_(k=1,...,10) c_(2k) z^k P(z)^((6-k)/4).      (13)
```

The four-root regularity equations are

```text
[z^7]C=[z^8]C=[z^9]C=[z^10]C=0 in R.                  (14)
```

At row `k`, the newborn scalar `c_(2k)` occurs with coefficient one.
Eliminating the four global scalars `c14,c16,c18,c20` from `(14)` therefore
leaves three nonconstant quotient coordinates per row, hence 12 exact
equations.

Let `I_A'=A`.  The endpoint primitive-difference condition is

```text
[z^11]C-I_A/8 is constant in R.                        (15)
```

Eliminating that constant (equivalently `gamma`, with optional `c22`
absorbed into it) contributes three more quotient coordinates.  The
smallest leading-face resultant is therefore

```text
12 regularity equations + 3 endpoint equations = 15.  (16)
```

Equations `(13)`--`(16)` involve `A,Q,e,F8` and the earlier global modes,
but no odd raw variable in `(10)`.  Therefore every even point satisfying
the 15-equation resultant still carries the at-least-five-dimensional odd
fiber from Section 6.  Direct composition with the leading endpoint face
does not produce an exclusion.

The next computation must either:

1. compile the half-step odd Newton equations and intersect them with this
   five-dimensional fiber; or
2. continue to q17, the next no-new-raw-odd-slot exactness gate, while
   retaining `(16)`.

## 8. Frozen verifier and scope firewall

Checker:

```text
cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_q15_20260828/
  verify_lambda0_q15.py
```

Replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_q15_20260828/verify_lambda0_q15.py
```

Expected marker:

```text
PASS_EXACT_LAMBDA0_Q15
```

The checker uses only standard-library exact rational arithmetic.  It pins
the predecessor packet, reconstructs the finite-support license, derives
q15 symbolically, requires the cubic mutation control, and freezes the two
rank-50 matrices.

No claim is made about the half-step odd equations, q17 or later gates,
solvability of the 15-equation even resultant, emptiness of the deep branch,
a Keller theorem, or JC2.
