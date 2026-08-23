# Exact Belyi test for the residue-A genome

**Date:** 2026-08-23  
**Scope:** rank-3 experiment from `xmodel/sol-connections.md`, using the
residue-A data of `SHEET6-TEMPLATE.md` and the rung-36 record of
`SHEET6-DIRECTIONB.md`. All polynomial and tangent calculations below were
run exactly in Python 3 / SymPy 1.14 over `QQ(sqrt(3))`; no floating-point
recognition is used.

## Verdict

1. **VERIFIED.** The residue-A collapse is exactly the degree-four Belyi map

   \[
   \beta(u)=\frac{u(u-2/3)^3}{(u^2-u+1/6)^2}
   \]

   with passport
   \(((3,1),(2,2),(3,1))\). Its monodromy group is \(A_4\) in the
   four-point action, the ordered Nielsen class has one simultaneous-
   conjugacy orbit, and its two double poles have ratio \(2+\sqrt3\) (or its
   inverse \(2-\sqrt3\)). Thus the `a1/a2` datum really is the pole field of
   the rigid tetrahedral cover.

2. **REFUTED AS STATED.** The rung-36 row is not identified by the exact
   source formulas with the tangent equation of that Hurwitz passport. Its
   coefficient vector is instead the universal top-coefficient equation in
   the first variation of the upstream common-power cancellation
   \(g^2-f^3\), after the \(g\)-carrier splits into multiplicities \(2+1\).
   It exists for an arbitrary pair of distinct pole positions and therefore
   does not detect the tetrahedral modulus. There is a formal resemblance to
   one of the two Hurwitz coefficient equations, but the variables do not
   have the required branch-point meanings and the second independent
   Hurwitz equation is absent.

3. Consequently the conditional payoff in rank 3 does **not** fire. The
   Belyi map gives a characteristic-zero certificate for the *leading local
   collapse and pole field*. It does not certify the full D43 elimination,
   identify the residue-A tower with a classical Hurwitz object, bound tower
   depth, prove the `ell+` dichotomy, or give G5.

## 1. The actual tetrahedral Belyi map

Put

\[
 N=u(u-2/3)^3,\qquad D=(u^2-u+1/6)^2,\qquad \beta=N/D.
\]

Exact expansion gives

\[
\begin{aligned}
N&=u^4-2u^3+\frac43u^2-\frac8{27}u,\\
D&=u^4-2u^3+\frac43u^2-\frac13u+\frac1{36},\\
N-D&=\frac{4u-3}{108},\\
\beta'(u)&=-\frac19
 \frac{(u-2/3)^2}{(u^2-u+1/6)^3}.
\end{aligned}
\]

Hence the three fibers are as follows.

| target value | source fiber | ramification partition |
|---|---|---|
| \(0\) | \(u=2/3\) triple, \(u=0\) simple | \((3,1)\) |
| \(\infty\) | the two roots of \(u^2-u+1/6\), both double | \((2,2)\) |
| \(1\) | \(u=\infty\) triple, \(u=3/4\) simple | \((3,1)\) |

At infinity, \(\beta-1\sim 1/(27u^3)\), so the stated triple
ramification is literal. The Riemann--Hurwitz defect is

\[
 (3-1)+(2-1)+(2-1)+(3-1)=6=2\cdot4-2,
\]

so there are no omitted critical points.

The two poles are

\[
 a_1=\frac12+\frac{\sqrt3}{6}
     =\frac12\left(1+\frac1{\sqrt3}\right),\qquad
 a_2=\frac12-\frac{\sqrt3}{6}
     =\frac12\left(1-\frac1{\sqrt3}\right),
\]

and therefore

\[
 \frac{a_1}{a_2}=2+\sqrt3,\qquad
 \frac{a_2}{a_1}=2-\sqrt3.
\]

This verifies exactly the field and ratio banked in the residue-A genome.
The scale change \(t=\sigma u\) recovers
\(a_1+a_2=\sigma\), \(a_1a_2=\sigma^2/6\),
\(b=2\sigma/3\), and \(b_2=3\sigma/4\).

### Monodromy and rigidity

One branch-cycle triple, with product \(1\), is

\[
 \sigma_0=(1\,2\,3),\qquad
 \sigma_1=(2\,3\,4),\qquad
 \sigma_\infty=(1\,2)(3\,4).
\]

It is transitive and generates \(A_4\) (order \(12\)); all three
generators are even, so the monodromy is not \(S_4\). Exact enumeration of
the \(24\) transitive ordered triples of types
\((3,1),(3,1),(2,2)\) gives one orbit under simultaneous conjugacy by
\(S_4\). This is the rigid tetrahedral Nielsen class.

The same rigidity can be seen without permutation enumeration, at the
coefficient level needed for the tangent comparison.

## 2. Exact Hurwitz deformation complex

Use target `PGL_2` to put the branch values at \(0,1,\infty\), and use
source `PGL_2` to put the triple point over \(1\) at source infinity. A
nearby factored cover with the same labelled passport then has

\[
 A(u)=(u-r)(u-b)^3,\qquad
 C(u)=(u-a)^2(u-c)^2,\qquad \beta=A/C,
\]

after equating the two leading coefficients. Triple contact with \(1\) at
infinity says that \(A-C\) has degree at most one. Its two equations are

\[
\begin{aligned}
 E_3&=2a-3b+2c-r=0,\\
 E_2&=-a^2-4ac+3b^2+3br-c^2=0.             \tag{2.1}
\end{aligned}
\]

At

\[
 (r,b,a,c)=
 \left(0,\frac23,
 \frac12+\frac{\sqrt3}{6},
 \frac12-\frac{\sqrt3}{6}\right),
\]

their exact Jacobian in the order \((r,b,a,c)\) is

\[
 J_H=
 \begin{pmatrix}
 -1&-3&2&2\\
 2&4&-3+\sqrt3/3&-3-\sqrt3/3
 \end{pmatrix}.                                      \tag{2.2}
\]

It has rank \(2\). Its kernel is exactly the two-dimensional residual
affine source gauge: simultaneous translation has vector
\((1,1,1,1)\), and scaling has vector

\[
 \left(0,\frac23,
 \frac12+\frac{\sqrt3}{6},
 \frac12-\frac{\sqrt3}{6}\right).
\]

Both are killed by (2.2). Conversely, imposing the source gauges
\(r=0\) and \(a+c=1\) gives the square tangent matrix

\[
 d(E_3,E_2,r,a+c-1),\qquad \det=-2\sqrt3\ne0.           \tag{2.3}
\]

Thus the gauge-quotiented Hurwitz tangent space is zero. In the symmetric
coordinates \(s=a+c\), \(p=ac\), with \(r=0\), its two non-gauge
coefficient equations may also be written

\[
 3\,db-2\,ds=0,\qquad 3\,dp-s\,ds=0.                   \tag{2.4}
\]

Passport rigidity therefore has **two** independent coefficient equations
before the residual affine source gauge is removed; it is not represented
by a lone six-variable trace row.

## 3. What the rung-36 row actually linearizes

The banked modular row is

\[
 c_1(tf1_{48}+tf2_{48})+
 c_2\{2(tg1_{48}+tg2_{48})+tg01_{48}+tg02_{48}\}=0.
\]

At the two primes,

\[
\begin{array}{c|c|c|c}
p&c_1&c_2&c_1+3c_2\pmod p\\ \hline
105337&48635&54013&0\\
105673&50809&18288&0
\end{array}
\]

so its rational candidate is, up to sign,

\[
 L=3(F_1+F_2)-2(G_1+G_2)-(H_1+H_2)=0,                 \tag{3.1}
\]

where \(F_i=tf_i\), \(G_i=tg_i\), and \(H_i=tg0_i\). This is also the
linear part of the exact characteristic-zero window equation `C16.10`,
after multiplication by \(184\).

The source formulas determine the meaning of these six variables. At each
pole cluster \(i\), the `f` stream has reduced multiplicity \(2\), while
the `g` carrier is split between a multiplicity-\(2\) `Gp` stream and a
multiplicity-\(1\) `G0p` stream. In the unreduced \(C_7\)-orbit product
these are the sizes \(6,6,3\) recorded by
`C7SUB = {42: 6, 21: 3}`; this merely multiplies the following equation by
three.

Let \(q_i=u-a_i\), and perturb those three carrier factors by dual numbers:

\[
\begin{aligned}
 f_\epsilon&=\prod_{i=1}^2(q_i+\epsilon F_i)^2,\\
 g_\epsilon&=\prod_{i=1}^2
 (q_i+\epsilon G_i)^2(q_i+\epsilon H_i).
\end{aligned}
\]

SymPy factors the exact first variation as

\[
 \left.\frac{d}{d\epsilon}(g_\epsilon^2-f_\epsilon^3)
 \right|_{\epsilon=0}
 =2q_1^5q_2^5\{R_1q_2+R_2q_1\},                       \tag{3.2}
\]

where

\[
 R_i=2G_i+H_i-3F_i.
\]

The coefficient of (u) in the braces in (3.2) is

\[
 R_1+R_2=-L.                                           \tag{3.3}
\]

This is exactly the rung-36 trace row. The other coefficient is

\[
 -cR_1-aR_2,
\]

and full first-order common-power cancellation would require both
\(R_1=R_2=0\), not just their trace sum.

Equation (3.3) explains all three observed features without using the
Belyi map:

- \(3\) is the derivative exponent of \(f^3\);
- \(2\) is the derivative exponent of \(g^2\), applied to the doubled
  `Gp` carrier;
- \(1\) is the remaining simple `G0p` carrier;
- the pole-swap trace occurs because the row extracts the top coefficient
  of \(R_1q_2+R_2q_1\).

In particular (3.3) holds with \(a_1,a_2\) arbitrary and distinct. Neither
\(a_1a_2=1/6\) nor \(a_1/a_2=2+\sqrt3\) enters. It is an infinitesimal
equation for staying in the `(2,3)` common-power/h-tower stratum *before*
the residual quotient \(h_1^3/f^4\) becomes the Belyi map.

### Why the numerical resemblance is not an identification

The first Hurwitz equation in (2.1) has differential

\[
 3\,db-2\,d(a+c)+dr=0.                                  \tag{3.4}
\]

Thus (3.1) can be made to look like (3.4) by declaring

\[
 d b=\operatorname{Tr}(tf),\quad
 d(a+c)=\operatorname{Tr}(tg),\quad
 dr=-\operatorname{Tr}(tg0).
\]

But this declaration is not the map supplied by `directionb_window`:
`tf_i`, `tg_i`, and `tg0_i` are three Puiseux carrier perturbations over
the *same pole cluster* \(a_i\); they are not respectively the triple zero
\(b\), the double-pole sum \(a+c\), and the simple zero \(r\) of the
residual Belyi map. The exact induced equation is (3.2), not (3.4).

There is also a decisive layer-orientation check. The Belyi quotient is
the leading residual of \(h_1^3/f^4\): after removal of the common
\(P^6\), the `f` side supplies its double-pole denominator \(P^2\). A
literal pullback of (3.4) along the direct branch-factor map would therefore
attach the Hurwitz multiplicity \(2\) to the `tf` pole motion. The rung row
instead attaches \(3\) to `tf`. That \(3\) is exactly the exponent of
`f` in the *previous* cancellation \(h_1=g^2-f^3\), while its \(2\) is
the exponent of the raw `g` carrier. The coefficient orientation therefore
places (3.1) one collapse upstream from the Belyi passport.

There are two further exact separators.

1. The Hurwitz complex has the second independent row in (2.2), which
   contains the pole anti-trace over `QQ(sqrt(3))`. The rung row is a single
   rational trace projection and is blind to it.
2. Set \(F_1=1,F_2=-1\) and all \(G_i,H_i=0\). Then (3.1) vanishes. Under
   the natural pole-position projection
   \((dr,db,da,dc)=(0,0,-1,1)\), however,

   \[
   J_H(0,0,-1,1)^T=(0,-2\sqrt3/3)^T\ne0.                \tag{3.5}
   \]

   Thus the kernel of the rung functional is strictly larger than the
   Hurwitz tangent space even in the most favorable direct projection.

This refutes `CONJECTURE 3` of `sol-connections.md` in its stated form.

> **CONJECTURE (weaker surviving possibility).** After imposing *all*
> earlier h-tower cancellation equations, constructing the residual
> \(h_1^3/f^4\) to the relevant order, and retaining its four marked branch
> loci, some later D43 conormal class may pull back from one of the two
> Hurwitz rows (2.2). No such marked residual-jet map is presently
> constructed. The isolated rung-36 trace row is not that result.

## 4. What the rigid identification buys—and what it does not

### What is now certified in characteristic zero

The local collapse

\[
 t(t-2\sigma/3)^3-(t-a_1)^2(t-a_2)^2
   =\frac{\sigma^3}{27}(t-3\sigma/4)
\]

is the scaled defining identity of a unique rigid \(A_4\) Belyi cover.
This is a small characteristic-zero certificate for all of the following
leading data:

- the passport \(((3,1),(2,2),(3,1))\);
- the rational field of moduli of the cover;
- the double-pole splitting field `QQ(sqrt(3))`;
- \(a_1/a_2=2\pm\sqrt3\), \(b=2\sigma/3\), and
  \(b_2=3\sigma/4\);
- uniqueness of this marked degree-four leading quotient modulo `PGL_2`.

Separately, (3.2) gives a characteristic-zero explanation of the rational
coefficient vector \(3:-2:-1\). It does **not** by itself prove that the
entire modular D43 left-kernel construction, including its reductions and
graph equations, is the reduction of one characteristic-zero row. That
stronger certificate still requires an exact characteristic-zero replay of
the D43 constructor or a proof that the relevant left-kernel module is
integral and specializes with constant rank. Two primes alone do not prove
that statement.

### No tower-depth theorem follows

Classical Hurwitz rigidity says that the marked degree-four cover has no
non-gauge first-order deformation and that its fixed-passport Hurwitz space
is finite. The residue-A tower contains much more information: common
factors removed before forming \(h_1^3/f^4\), Puiseux tails, dead stretches,
the \(B\)-side and \(x\)-side, and later Jacobian graph equations. Those data
can vary while the leading Belyi quotient stays literally constant. The
rung calculation exhibits precisely such upstream directions.

Therefore rigidity supplies no bound on the formal tower depth and no route
by itself to the `ell+` dichotomy or G5. A route of that kind would need at
least the following new statement.

> **CONJECTURE (faithful marked-jet landing).** Beyond some explicit level,
> every non-gauge residue-A tower prolongation induces a nonzero deformation
> of a finite marked jet of the tetrahedral cover, and the landing map has
> uniformly bounded kernel.

The classical degree-four cover proves neither existence nor faithfulness
of this landing map. The naive version landing only in the ordinary
Hurwitz space is false: (3.2) shows common-power carrier directions that are
invisible to the residual cover. An enriched object carrying the removed
common divisor and marked jets would be needed before rigidity could
possibly control depth.

## 5. Exact-computation record

The decisive SymPy assertions were:

```python
from sympy import Matrix, Rational, diff, expand, factor, simplify, sqrt, symbols

u, r, b, a, c, eps = symbols('u r b a c eps')
F1, F2, G1, G2, H1, H2 = symbols('F1 F2 G1 G2 H1 H2')

N = expand(u*(u-Rational(2,3))**3)
D = expand((u**2-u+Rational(1,6))**2)
assert simplify(factor(N-D) - (4*u-3)/108) == 0
assert simplify(diff(N/D, u)
    + Rational(1,9)*(u-Rational(2,3))**2
      /(u**2-u+Rational(1,6))**3) == 0

A = expand((u-r)*(u-b)**3)
C = expand((u-a)**2*(u-c)**2)
E3 = (A-C).coeff(u, 3)
E2 = (A-C).coeff(u, 2)
pt = {r: 0, b: Rational(2,3),
      a: (1+1/sqrt(3))/2, c: (1-1/sqrt(3))/2}
J = Matrix([E3,E2]).jacobian([r,b,a,c]).subs(pt)
Jg = Matrix([E3,E2,r,a+c-1]).jacobian([r,b,a,c]).subs(pt)
assert J.rank() == 2
assert simplify(Jg.det() + 2*sqrt(3)) == 0

fe = (u-a+eps*F1)**2*(u-c+eps*F2)**2
ge = ((u-a+eps*G1)**2*(u-a+eps*H1)
      *(u-c+eps*G2)**2*(u-c+eps*H2))
dh = diff(ge**2-fe**3, eps).subs(eps, 0)
assert simplify(dh/(2*(u-a)**5*(u-c)**5)
    - ((2*G1+H1-3*F1)*(u-c)
       +(2*G2+H2-3*F2)*(u-a))) == 0
```

The monodromy enumeration found \(24\) transitive ordered branch-cycle
triples and one simultaneous-conjugacy orbit; the generated group has order
\(12\).

## Final disposition of rank 3

**The residue-A leading genome contains a genuine rigid tetrahedral Belyi
map, but the residue-A tower is not thereby identified with that map.** The
quadratic unit is a real Belyi invariant. The rung-36 `3:2:1` row is a real
characteristic-zero common-power tangent invariant. They are adjacent
consequences of the nested collapse, not two coordinates of one proved
Hurwitz-rigidity certificate. The proposed bridge to a depth bound is a
gap, not a theorem.
