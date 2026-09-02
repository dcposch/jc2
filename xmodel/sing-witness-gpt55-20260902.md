# SING-WITNESS -- fixed-N singular asymptotic curve witness

Lane: `SING-WITNESS`. Date: 2026-09-02. Agent: GPT-5.5.

## 0. Verdict

`OPEN[SING-WITNESS]`, read literally as "fixed `N`, dominant maps, `g_L -> infinity`,
and singular `A_F`", has a desk-scale witness at `N = 6`:

```text
z := x y^3 - y,        e := 2k+1,
F_k = (P_k,Q_k) := ( x + z^e, z^2 ),        k >= 1.
```

Then `A_{F_k}` is the unibranch cusp

```text
U^2 = V^e
```

with `n = e`, `delta_aff = (e-1)/2 = k`, and one place at infinity.  The generic
meridian cycle type is `1^4 . 2`, with

```text
N = 6,  a = 4,  W = 2,  S = 1,  mu = 2,  K_cusp = 3 = a - 1.
```

The generic pencil genus is

```text
g_L = e - (gcd(e-1,3)-1)/2
    = 2k+1  if 3 does not divide k,
      2k    if 3 divides k,
```

so `g_L -> infinity` at fixed `N = 6`.

This answers only the unqualified singularity version.  It does not answer the
bounded-pair version: here `(n,delta_aff) = (2k+1,k)` is unbounded.  The remaining
honest question is therefore:

```text
OPEN[SING-WITNESS-BOUNDED].
At fixed N, can g_L -> infinity with A_F singular and with (n,delta_aff)
uniformly bounded?  BOUNDED QUANTITY: the pair (n,delta_aff), preferably in
Aut-minimal gauge.
```

No `charge_basis` line is present because this report asserts no new exit-price
claim.

## 1. Frozen Inputs And Scope

The four frozen charged inputs were hashed before reading; all matched:

```text
5d2723e36476903392fd79b3791d1bd9830a0dea6f4693070ae8f89ccc06d6e1
  keller-pencil-genus-opus5-20260902.md
d57d17f8eb6e776013d283e6796bef0db256088011dae2b73d1383c1e40cc56a
  keller-pencil-genus-review-grok46-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80
  mprime-alln-h2-opus5-20260902.md
d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853
  deg-af-vs-n-opus5-20260902.md
```

Consumed at the review-confirmed typing: `NEG-GENUS`, `PROFILE-WITNESS`,
`FORK-GENUS`, `ESCAPE-KAPPA`, `MPRIME`'s `[P3]`, `(L)`, `(K)`, `(C1)`-`(C3)`,
and `DEG-AF`'s invariant reading of `(n,delta_aff)`.  Case `(A)` is treated as
Keller-empty/caged exactly as charged; the witness below is non-Keller and
violates that Keller gate.  No `Z(G)=1`, no A2, and no `jc2-lean` inspection.
No canonical ledger was edited.

## 2. Why Source-Only `(x,g)` Cannot Work

For a map `H=(x,g(x,y))`, any escaping sequence with finite target limit has
first coordinate `x -> a`.  Hence every one-dimensional component of `A_H` lies
in a vertical line `{U=a}`.  If the component is reduced, it is that vertical
line; if several leading coefficients drop at the same `a`, the set-theoretic
component is still the same line.  Distinct such components are parallel.

This is the elementary form of Chau's dicritical picture in this special
coordinate: dicritical parameters may vary the second coordinate, but the first
coordinate is already fixed by the target coordinate `U=x`.  A target
automorphism sends a coordinate line to a smooth embedded `A^1`, so it cannot
turn this source-only family into a cusp or a node.  Thus the requested
`(x,x^c y^m+h)` search has a built-in obstruction if only automorphisms are
allowed after it.

The successful construction below uses the next smallest operation: a finite
target fold, not a target automorphism.  That is exactly where singularity of
`A_F` enters.

## 3. The `N = 6` Witness

Let

```text
H(x,y) = (x,z),        z = x y^3 - y,
psi_e(u,v) = (u+v^e,v),
T(u,v) = (u,v^2),
F_k = T o psi_e o H,  e = 2k+1.
```

So `F_k=(x+z^e,z^2)`.  Since `T` is finite, it is proper, and

```text
A_{F_k} = T(A_{psi_e o H}).
```

For `H`, the target equations are `u=x` and `u y^3-y=v`.  The generic degree is
`3`; over the nonproper line `{u=0}`, one finite point remains (`y=-v`) and two
sheets escape.  Hence `A_H={u=0}`, `a_H=1`, `W_H=2`, and the escaping cycle is
a 2-cycle.  After `psi_e`, the nonproper curve is `{u=v^e}`.  Applying `T`
gives

```text
t |-> (t^e,t^2),       hence       A_{F_k}: U^2 = V^e.
```

Because `e` is odd, this parametrization is generically one-to-one.  The curve
is rational, irreducible, has one place at infinity, and has a unique affine
singularity at `(0,0)`, analytically the `(2,e)` cusp.  Thus

```text
n = deg closure(A_F) = e,       delta_aff = (2-1)(e-1)/2 = k.
```

For a generic point `p_s=(s^e,s^2)` of `A_F`, `s != 0`, the fold preimage has
two points:

```text
(s^e,s)    lies on {u=v^e};
(s^e,-s)   lies off {u=v^e}.
```

The first contributes one finite source point and two escaping sheets.  The
second is a proper point of `psi_e o H` and contributes all three finite sheets.
Therefore

```text
N = 2*3 = 6,       a = 1+3 = 4,       W = N-a = 2,
S = 1,             mu = 2,            meridian cycle type = 1^4 . 2.
```

At the cusp `p_0=(0,0)`, the only fold preimage is `(0,0)`, and the source
equations force `x=0`, `y=0`.  Thus `a_{p_0}=1`, `r_{p_0}=1`, and MPRIME's
fibre law gives

```text
K_{p_0} = N - a_{p_0} - r_{p_0} W = 6 - 1 - 2 = 3 = a - 1.
```

There are no other affine singularities of `A_F`, so `(K)` is matched exactly.
Also:

```text
[P3]        a + W = 4 + 2 = 6 = N.
(C1)        r W = 2 <= 6 at the unibranch cusp.
(C2)        unibranch points only have K_p <= a; here 3 <= 4.
(C3)        #{K_p>0}=1 <= R+beta = 0+1.
7.B'        mu = 2.
```

The Jacobian is

```text
Jac(P_k,Q_k) = 2 z (3 x y^2 - 1)
             = 2 y (x y^2 - 1)(3 x y^2 - 1),
```

so the family is deliberately non-Keller.

## 4. Genus Computation

For a generic pencil `alpha P_k + beta Q_k = t` with `alpha != 0`, the affine
curve is isomorphic to the sparse curve in `(z,y)`:

```text
f_e(z,y) := y^3 (t - alpha z^e - beta z^2) - alpha y - alpha z = 0,
x = (t - alpha z^e - beta z^2)/alpha.
```

For `(alpha,beta,t)=(3,5,7)`, the Newton polygon has vertices

```text
(0,1), (1,0), (e,3), (0,3).
```

Its doubled area is `3e+2`, its boundary lattice count is
`e + gcd(e-1,3) + 3`, and Pick's formula gives

```text
# interior lattice points
  = e - (gcd(e-1,3)-1)/2.
```

The face checks are exact.  The only nontrivial top face is

```text
h_e(z) = 7 - 5 z^2 - 3 z^e.
```

If `h_e` and `h'_e` had a nonzero common root, then
`z^{e-2}=-10/(3e)` and `z^2=7e/(5e-10)`, forcing
`100/(9e^2) = (7e/(5e-10))^{e-2}`.  For odd `e >= 3`, the right side is
greater than `1` while the left side is at most `100/81`; contradiction.  The
other faces have a monomial derivative obstruction or the face
`7y^3-3y`, which has no multiple torus root.  Thus the curve is
Newton-nondegenerate, and the genus is the interior lattice count.

The resulting table for `k=1..4` is:

```text
k  e=2k+1  N  n  delta_aff  a  W  S  mu  cycle    K_cusp  g_L
1     3    6  3      1       4  2  1   2  1^4.2      3      3
2     5    6  5      2       4  2  1   2  1^4.2      3      5
3     7    6  7      3       4  2  1   2  1^4.2      3      6
4     9    6  9      4       4  2  1   2  1^4.2      3      9
```

By `FORK-GENUS`, this means the fork excess grows at fixed `N`; explicitly
`Psi - Lambda - kappa = 2g_L - 2 - N`.  The report does not compute the
resolution tree and does not promote a value of `Psi`, `Lambda`, or `kappa`.

## 5. CAS Record

Tools used: Python 3.14.7, Sympy 1.14.0, and Singular 4.4.1 `normal.lib`.
The report's algebraic claims are Sympy/Newton except for the `normal.lib`
genus control.

Sympy, over `QQ[x,y,U,V]`, returned for `k=1..4`:

```text
Jac(P,Q) = 2*y*(x*y^2 - 1)*(3*x*y^2 - 1)
Sing(U^2 - V^e): Groebner basis [U, V^(e-1)]  (radical point (0,0))
gcd(7 - 5 z^2 - 3 z^e, d/dz) = 1
sample target (U,V)=(7,1): discriminants -948 and -1696 on the two z-branches
```

The same Sympy run computed the Newton data:

```text
k  e  area2  boundary  genus
1  3    11      7        3
2  5    17      9        5
3  7    23     13        6
4  9    29     13        9
```

Singular `normal.lib` on the sparse isomorphic pencil model gave:

```text
alpha,beta,t = 3,5,7:
  k=1 e=3 deg=6  g=3
  k=2 e=5 deg=8  g=5
  k=3 e=7 deg=10 g=6
  k=4 e=9 deg=12 g=9

alpha,beta,t = 2,11,3:
  k=1 e=3 deg=6  g=3
  k=2 e=5 deg=8  g=5
  k=3 e=7 deg=10 g=6
  k=4 e=9 deg=12 g=9
```

A direct Singular run on the original `(x,y)` pencil matched `g=3` at `k=1`
but was stopped before `k=2` after exceeding the control budget.  It is not
consumed; the isomorphism to the sparse model is explicit above.

## 6. Failed Lower-N Attempts

The failures are useful because they explain why `N=6` is the first clean fold
witness in this format.

At `N=3`, source-only maps `(x,g)` have only vertical-line components in `A_F`,
and target automorphisms preserve smoothness.  A finite target fold would need a
degree-one nonproper source, which does not exist.

At `N=4`, take a degree-two source and a degree-two fold.

First, `H=(x,xy^2-y)` has `a_H=1` and `W_H=1`; after the fold it gives a cusp
and the special count can satisfy `(K)`, but `W=1`, so the 2-cycle profile and
`7.B'` are lost.

Second, `H=(x,xy^2+c)` with `c != 0` has `a_H=0` and `W_H=2`; after the fold it
has `N=4`, `a=2`, `W=2`, and cycle type `1^2 . 2`, but at the cusp
`a_p=0`, so

```text
K_cusp = 4 - 0 - 2 = 2 != a - 1 = 1.
```

With `c=0`, the cusp fibre contains the line `x=0`, so the profile count is not
finite.  Thus the two requirements `W=2` and `K=a-1` pull in opposite
directions at `N=4` for this triangular source plus fold template.

At `N=6`, `H=(x,xy^3-y)` has exactly the missing combination: one finite generic
point over the asymptotic line and two escaping sheets.  The fold then supplies
three extra fixed sheets, giving `a=4`, `W=2`, and `K=a-1`.

## 7. Controls

Automorphism control, `F=(x,y+x^k)`, pencil `3P+5Q-7`:

```text
k=1..6:  genus = 0 in every case.
```

This is the expected `A_F=empty`, `N=1`, `g_L=0` control.

Reviewed `PROFILE-WITNESS`, `G_k=psi_k o (x,xy^4-y^2)`, pencil `3P+5Q-7`:

```text
k=1: deg=5,  g=0
k=2: deg=10, g=3
k=3: deg=15, g=4
```

This reproduces the charged table.  The `k=4` direct Singular control was
stopped after the `k=1..3` reproduction because it did not return inside the
desk-scale check window.  The reviewed lower-bound proof of `g_L -> infinity`
for `PROFILE-WITNESS` is consumed at its confirmed typing.

## 8. Ledger Match And Violations

Matched by the `N=6` witness:

```text
H2 shape:      A_F irreducible, rational, one place at infinity.
Singular A_F: one unibranch cusp of type (2,2k+1).
[P3]:          a+W=N.
(C1):          r_p W <= N.
(C2):          at the unibranch point, K_p <= a.
(C3):          #{K_p>0}=1 <= R+beta=1.
7.B':          mu=2.
(K):           sum K_p = 3 = a-1.
Generic cycle: 1^4 . 2.
```

Violated:

```text
Jac F in C^*:  Jac = 2 y (x y^2 - 1)(3 x y^2 - 1).
Keller etale complement: impossible because of the affine ramification divisor.
Case-(A) empty/cusp cage: for p=2, q=e and fixed N=6, the Keller cage
  branch with j>=2 applies because P^2-Q^e = x(x+2z^e); its requirement
  N >= pq+1 = 2e+1 fails already at e=3.
Bounded-pair version: n=e and delta_aff=k are unbounded.
```

Therefore the profile ledger is blind to genus even after imposing that `A_F`
is singular, unless "singular structure" is upgraded to a quantitative bound on
`(n,delta_aff)` or to a Keller-only condition such as the finite-etale complement
and its monodromy gates.  The fixed-`N=6` family shows that singularity as a
boolean datum is not the missing ceiling.

## 9. The Remaining Door

Since a singular witness exists, task item (3) is not triggered in its strict
"if candidates all fail" form.  The useful residue is narrower and should be
kept typed:

```text
CONJECTURAL DOOR[DELTA-FORK-CEILING].
Fix N and the typed H2 profile data (a,W,S,mu_l,s_l) satisfying [P3],
(C1)-(C3), 7.B', and (K).  Among dominant polynomial maps with irreducible
rational one-place A_F and with (n,delta_aff) <= B, the polar fork mass Psi,
and hence g_L by FORK-GENUS, is bounded by a function of (N,B).
BOUNDED QUANTITY: (n,delta_aff).
```

This report gives evidence for why the bound, if true, must mention
`delta_aff` or an equivalent singularity-size invariant.  In the witness,
`N`, `a`, `W`, `S`, `mu`, the meridian cycle type, and `(K)` are all fixed,
while

```text
delta_aff = k,       n = 2k+1,       g_L = 2k+O(1).
```

So the growth is not hidden in a changing cycle profile; it is visible exactly
in the size of the cusp.  A Keller proof could still kill the family through
`Jac F in C^*`, the finite-etale complement, non-normality of the monodromy
subgroup, or the case-(A) cage.  What it cannot do is use only the listed
numerical profile ledger plus the boolean assertion "`A_F` is singular."

<!-- BODY-END -->
