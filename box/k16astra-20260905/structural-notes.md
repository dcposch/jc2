# Structural sublane: boundary factorization and the exact residual

Status: proved universal identities and a new equivalent open localization;
no all-t proof of (8.1) or (V0). Frozen charged reports only were read.
Root performed the mechanical SHA verification before delegation.

## 1. Notation that must not be conflated

The frozen terminal notation has `c=-yg`, and

\[
 E_t(h)=T_{t,0}+\sum_{k=1}^{2t-1}T_{t,k}h^k,
 \qquad \tau=T_{t,0}+c.
\]

Thus the homogeneous radical target uses this shifted `tau`, not literal
`T_{t,0}` with its nonzero constant term. Work factorwise over a characteristic
zero field factor of `A_t`; `y,g` are units in the charged normalization.

Write `x=L=h-b4`. Every prime below means differentiation with respect to
`x`, equivalently `h`. Put

\[
 K=x^2C-yb_3,\qquad F=xT-gb_3,\qquad
 Y=xS-b_3T-gb_2,
\]

where `C,T,S,U,V` are the translated univariate polynomials of the frozen
ansatz (the integration constant in `P0=V-gb1` has no derivative). Set

\[
 u=U'(0),\quad C_0=C(0),\quad T_0=T(0),\qquad
 \mathcal R=u+b_3 C_0.
\]

Here the argument `0` is **x=0**, hence **h=b4**. In unshifted notation,
`u=U'(b4)` and `C0=C(b4)`. The weights are

\[
 \operatorname{wt}(\mathcal R)=2t,\quad
 \operatorname{wt}(b_2)=2t+1,\quad
 \operatorname{wt}(b_1)=3t+1.
\]

The solved-spine equations are the following exact polynomial identities,
before imposing any positive terminal row:

\[
 \begin{aligned}
 D_3&: 2yT'=g(5C+3xC'),\\
 D_2&: -3gxU'+KF'-2K'F+2yxY'-yY=ygb_2,\\
 D_1&: 2yxV'+KY'-K'Y-2U'F=ygb_1.
 \end{aligned}
\]

The remaining residual is

\[
 D_0=KV'-U'Y=yg-E_t(h)
 =-\tau-\sum_{k=1}^{2t-1}T_{t,k}h^k.
\]

These equations are quoted directly from frozen DEP §2 and terminal proof
§2.1, with the sign checked against `D4=-ygL`.

## 2. New universal boundary factorization

**Lemma.** On the solved spine, for every `t>=2`, on both factors when split,

\[
 \boxed{b_1=-\frac{b_3}{y}\mathcal R},\qquad
 \boxed{D_0(h=b_4)=g b_2\mathcal R}.
 \tag{B1}
\]

Equivalently, there is an explicit ideal identity

\[
 \boxed{\tau+g b_2\mathcal R
 =-\sum_{k=1}^{2t-1}b_4^k T_{t,k}}.
 \tag{B2}
\]

Consequently, in `S_t/I_{t,+}`,

\[
 \boxed{\tau=-g b_2\mathcal R},\qquad
 \boxed{b_3\tau=yg b_1b_2}.
 \tag{B3}
\]

The second identity in (B3) is not a claim that `b3*tau` vanishes uniformly;
it identifies its residual product exactly.

**Proof.** At `x=0`,

\[
 K=-yb_3,\ K'=0,\ K''=2C_0,\quad
 F=-gb_3,\ F'=T_0,\ F''=5gC_0/y,\quad
 Y=-b_3T_0-gb_2.
\]

Differentiate `D2` once and evaluate there. The result is

\[
 yY'(0)=g(3u+b_3C_0).
 \tag{B4}
\]

Substitution into `D1(0)` gives

\[
 ygb_1=-yb_3Y'(0)+2gb_3u
       =-gb_3(u+b_3C_0),
\]

which proves the first formula of (B1). Differentiate `D2` twice. The terms
containing `b3*C'(0)` cancel by `D3`, leaving

\[
 \frac y2Y''(0)=gU''(0)+C_0T_0.
 \tag{B5}
\]

Now `D1'(0)=0` reads

\[
 2yV'(0)-yb_3Y''(0)+2C_0(b_3T_0+gb_2)
          +2gb_3U''(0)-2uT_0=0.
\]

By (B5), this simplifies to

\[
 yV'(0)=uT_0-gb_2C_0.
 \tag{B6}
\]

Hence

\[
 \begin{aligned}
 D_0(0)
 &=-yb_3V'(0)+u(b_3T_0+gb_2)\\
 &=g b_2(u+b_3C_0)=g b_2\mathcal R.
 \end{aligned}
\]

Evaluation of the displayed polynomial residual at `h=b4` proves (B2), and
then (B3) follows. No division by `b3`, `b2`, `R`, or a residual polynomial
was used. In particular, the formulas hold when any of these vanish. The
arbitrary constant `T0` cancels, so the conclusion is invariant under the
`P -> P + lambda Q` integration gauge. ∎

## 3. Exact new all-t partial and equivalent open chart

**Proved on a union of two explicitly defined hypersurfaces, all `t>=2`:**

\[
 V(I_{t,+})\cap\bigl(V(b_2)\cup V(\mathcal R)\bigr)
 \subseteq V(\tau).
 \tag{B7}
\]

This requires neither finiteness of the cone nor a Cohen--Macaulay hypothesis
on a determinantal curve. Since `g` is a unit,

\[
 \tau\in\sqrt{I_{t,+}}
 \quad\Longleftrightarrow\quad
 b_2\mathcal R\in\sqrt{I_{t,+}}.
 \tag{B8}
\]

The exact residual can therefore be written as one Rabinowitsch chart

\[
 \boxed{1\in
 (I_{t,+},\,1-z b_2\mathcal R)\subset S_t[z]}.
 \tag{B9}
\]

Equivalently one may use `(1-z b2, 1-w R)` with two inverse variables. This
is an inhomogeneous localization and any computation intended as a
characteristic-zero certificate must be exact over the field factors; an
inhomogeneous unit ideal modulo a prime is not promotable by the cone
properness lemma alone.

Since `b2` and `R` each have at most degree one in `b3` by the charged weight
bound on solved high variables, (B2) replaces the cubic homogeneous constant
row by a product of two polynomials each at most linear in `b3`, modulo the
positive rows. This is a reduction of the actual coefficients, not an
inference from a Hilbert series or a nilpotence degree bound.

On `D(R)`, the exact identity `b1=-(b3/y)R` says `b1=0` iff `b3=0`.
Thus the remaining chart may, if useful, be partitioned into `b3 != 0` and
`b3=b1=0`, always retaining `b2 R != 0`. No chart is silently discarded.

The full all-t assertion (B9) remains **OPEN**. The boundary factorization
does not by itself force either `b2` or `R` to vanish on every cone component.

## 4. Next exact jets and the residual at b3=0

Use `u_i=(d/dx)^i U'(0)` and `C_i=C^(i)(0)`. Directly continuing the same
derivatives, with no interpolation in `t`, gives

\[
 \begin{aligned}
 D_0'(0)=g\biggl[&b_2\left(u_1+\frac32b_3C_1\right)
 +\frac{b_3^2}{20}(u_2+2b_3C_2)\\
 &-\frac{(u_0+b_3C_0)(3u_0+2b_3C_0)}y\biggr].
 \end{aligned}
 \tag{J1}
\]

On the cone `D0` is constant, so all its positive `x` derivatives vanish.
On `b3=0` the first three exact equations are

\[
 yb_2u_1=3u_0^2,
 \tag{J2}
\]

\[
 yb_2u_2=8u_0u_1+2b_2C_0^2,
 \tag{J3}
\]

\[
 5b_2u_3y^2=54u_0u_2y+30u_1^2y
             +75b_2C_0C_1y-90C_0^2u_0.
 \tag{J4}
\]

In the unresolved `b3=0, b2 R != 0` chart, `R=u0`, so `u0`, `b2` and, by
(J2), `u1` are nonzero. This is a genuine necessary jet condition. It does
not establish that a formal series cannot truncate to the required
polynomials; proving such a polynomial truncation obstruction would be a
new step, not a consequence of these first jets.

There is a precise reason a finite local-jet argument cannot suffice without
using the global polynomial degree conditions.

**Formal existence lemma.** Let `K` be any characteristic-zero field and
choose `y,g,b2,u0` in `K^*`, a series `C(x)` in `K[[x]]`, and an arbitrary
integration constant `T0`. Set `b3=b1=0`. There is a unique formal series
`u(x)=U'(x)` with constant term `u0`, together with uniquely determined
`T,Y,V'`, satisfying `D1,D2,D3` and

\[
 D_0(x)\equiv g b_2u_0\ne0.
 \tag{J5}
\]

Here uniqueness concerns the displayed derivatives and series; the irrelevant
additive constants of `U,V` can be fixed arbitrarily.

**Proof.** D3 determines T from C and T0. Since `K=x^2 C`, `F=xT` and
`Y(0)=-gb2`, the coefficient of `x^n` in D2, for `n>=1`, solves `Y_n` with
the unit diagonal `y(2n-1)` and uses only `u_0,...,u_(n-1)` and the chosen
C,T data. D1 is divisible by x and solves V' with unit diagonal `2y`.
Its coefficient `V'_(n-2)` uses only `u_0,...,u_(n-2)` and already solved Y
coefficients. Finally, for `n>=1`, the coefficient of `x^n` in

\[
 D_0=x^2C V'-uY
\]

has the unique highest-index U' term `g b2*u_n`. All other terms use earlier
`u_i`: the first product has the factor `x^2`; in the second product the
term with `Y_n` uses only `u_i` with `i<=n-1`. Thus its vanishing determines
`u_n` uniquely because `g b2` is a unit. Induction proves existence and
uniqueness; the constant term is exactly `g b2u0`. ∎

This lemma does not produce a counterexample to (8.1): the resulting formal
series have no reason to terminate at the mandated degrees or satisfy the
leading coefficients and gauge of the ray. It isolates a specific missing
global statement: show that these formal solutions with `u0*b2 != 0` cannot
truncate with `C` monic of degree `t-1` and `U'` of degree `2t` and leading
coefficient `q=2t+1`, together with the remaining normalized spine data.
That polynomial truncation problem is a concrete approximate-root direction
for the new residual. It is not settled by (J2)--(J4).

`structural_boundary_jets.py` reconstructs these identities universally
over rational functions in algebraically independent jet coefficients, with
no use of the finite `t` controls. It solves D2's first five Taylor bands and
D1's first four bands, then checks (B1), (B6), and (J1) identically. A
foreground `timeout 1800 stdbuf -oL python3 ...` run took approximately 3.4 s
and printed `UNIVERSAL_BOUNDARY_JETS_PASS`. It also prints (J2)--(J4).

## 4A. A scalar polynomial Abel equation on the unresolved b3=0 chart

This is a coefficient-sensitive reduction of the remaining polynomial
truncation problem. It eliminates both `U'` and `V'` and contains no
derivative of C after a suitable shift.

Assume `b3=b1=0`, write `B=b2`, and let `D0=delta` be constant. Put

\[
 Z=Y-\frac{x^2CT}{y},\qquad
 a=\frac{3x^3C^2}{4y^2},\qquad
 w=\frac Zg+a,\qquad \kappa=\frac\delta g.
 \tag{A1}
\]

Then the three differential equations and the constant residual are
equivalent, with the polynomial reconstruction formulas below, to

\[
 \boxed{2xww'=w^2+(B-2a)w+\frac{a^2}{3}-Ba-\frac{3x\kappa}{y}}.
 \tag{A2}
\]

For a point in the still-unresolved chart, the constraints include

\[
 \begin{gathered}
 B\ne0,\quad \kappa\ne0,\quad
 C\text{ monic of degree }t-1,\quad
 w\in K[x],\ \deg w=q=2t+1,\quad w(0)=-B.
 \end{gathered}
 \tag{A3}
\]

**Derivation and reconstruction.** D3 determines T with arbitrary T0.
Substitution of `Y=Z+x^2CT/y` into D2 gives

\[
 U'=\frac{y(2xZ'-Z-gB)}{3gx}+\frac{x^2CT'}g.
 \tag{A4}
\]

D1 then gives

\[
 V'=\frac{U'T}{y}
 +\frac{(2C+xC')Y-xCY'}{2y}.
 \tag{A5}
\]

These expressions are polynomial when C,w are polynomial and `w(0)=-B`:
the numerator involving division by x in (A4) vanishes at x=0. Set
`Y=g(w-a)+x^2CT/y`, and recover `S=(Y+gB)/x`, also polynomial. Their degree
bounds are exactly `deg T=t`, `deg S<=2t`, `deg U'<=2t`, `deg V'<=3t`.
Substituting (A4)--(A5) into `D0=x^2CV'-U'Y` gives the exact identity

\[
 D_0=\frac{gy}{3x}
 \left(w^2+(B-2a)w+\frac{a^2}{3}-Ba-2xww'\right).
 \tag{A6}
\]

Thus (A2) is equivalent to `D0=delta`, with `delta=g*kappa`. The T0 gauge
cancels identically. No division by w or C is used; their zero sets and
possible multiple roots are retained. The full ray's normalization and
gauges still have to accompany (A3) when turning a polynomial solution of
this ODE back into a ray point. For exclusion it is enough to rule out the
necessary polynomial solutions with the displayed leading coefficient.

**Leading coefficient.** Write `d=2qy-(t+1)`, so `3d^2=t+1`, and let

\[
 \alpha=[x^q]a=\frac{3}{4y^2},\qquad
 \omega=[x^q]w.
\]

The required leading coefficient `U'=q x^(2t)+...` in (A4) is exactly

\[
 \boxed{\omega=\alpha\frac{2d-1}{4t+1}}.
 \tag{A7}
\]

The top band of (A2) says

\[
 (4t+1)\omega^2+2\alpha\omega-\alpha^2/3=0,
\]

which is precisely the banked relation `3d^2=t+1`. The leading balance
therefore supplies no contradiction. Both `2d-1` and `2d+1` are units for
every admissible integer t, since their norms are `-(4t+1)/3`.

At x=0 the first coefficients are

\[
 w_0=-B,\qquad w_1=\frac{3\kappa}{yB},\qquad
 w_2=\frac{w_1^2}{3B}
 \quad(w_i=[x^i]w).
 \tag{A8}
\]

In particular, the residual `kappa != 0` forces `w1 != 0`.

**Divisibility and roots.** The exact polynomial form of (A2) is

\[
 w\mid \frac{a^2}{3}-Ba-\frac{3x\kappa}{y},
\]

with quotient `2xw'-w-B+2a`. This quotient is divisible by x and has a
simple zero at x=0 when `kappa != 0`. More economically set

\[
 A=xC,\qquad
 H=\frac{2xw'-w-B+2a}{x}.
\]

Then

\[
 \boxed{wH=\frac{3}{16y^4}
       \left(xA^4-4By^2A^2-16y^3\kappa\right)}.
 \tag{A9}
\]

Here `deg A=t`, `deg w=2t+1`, `deg H=2t`,

\[
 H(0)=w_1\ne0,\qquad
 [x^{2t}]H=\alpha(2d+1).
\]

Evaluation at a root of A proves the genuine coprimality conditions

\[
 \gcd(w,A)=\gcd(H,A)=1\quad\text{if }\kappa\ne0.
 \tag{A10}
\]

These conditions do not imply `gcd(w,H)=1`; repeated roots of the product
in (A9) remain possible. Any argument dividing by w, H, or their derivatives
must cover those branches.

`structural_abel.py` verifies (A4)--(A6), the leading identity, and (A9) in
SymPy with symbolic functions C,T,Z and algebraically independent constants.
The foreground run prints `UNIVERSAL_ABEL_IDENTITY_PASS`,
`LEADING_NORMALIZATION_PASS`, and `ROOT_DIVISIBILITY_IDENTITY_PASS` in about
1.3 s.

**Residual status.** A coefficient-sensitive polynomial Abel/Darboux or
approximate-root theorem excluding (A2)--(A3), (A7) with `kappa != 0` would
close the `b3=0` part of the new open chart. It would not by itself close the
`b3 != 0` part. No such theorem is established here. Merely comparing degrees
in (A2) or (A9) reproduces the valid leading normalization and is therefore
insufficient.

## 4B. The full polynomial Abel atom, including every b3 chart

The same completion works without setting b3 to zero. The result is a
**single scalar polynomial differential equation equivalent to the entire
cone problem**, after the standard gauges. It is not an emptiness proof.

Fix t and a field factor as above. Write `b=b3`, `B=b2`, and take a monic
polynomial C of degree `t-1`. Seek a polynomial W of degree `q=2t+1` with

\[
 W(0)=-B,\qquad
 [x^q]W=\omega=\frac{3(2d-1)}{4y^2(4t+1)}.
 \tag{F1}
\]

Set

\[
 \eta=W'(0),\quad r=b^2/4,\quad K=x^2C-yb,\quad
 A=\frac{3x^3C^2}{4y^2},\quad D=\frac{3bxC}{2y}.
 \tag{F2}
\]

The full polynomial Abel equation is

\[
 \boxed{\begin{aligned}
 2(xW-r)W'={}&W^2+(B-2A+D)W+\frac{A(A-D)}3-B(A-D)\\
 &-\frac{b\eta K}{2y}-B\eta x
   +\frac{2rA-4r(B+W)}x.
 \end{aligned}}
 \tag{F3}
\]

The displayed quotient is polynomial: both A and `B+W` are divisible by x.
There is no division by `b`, `C`, `W`, `xW-r`, or any of their derivatives.
All roots, including repeated roots and the degeneracy `b=0`, are included.

**Exact atom.** For every fixed `t>=2`, factorwise, (8.1) is equivalent to
the absence of solutions of (F1)--(F3) with

\[
 \boxed{B\eta\ne0}.
 \tag{F4}
\]

The proof of this equivalence follows below. It does not assume that the
determinantal curve has the expected height or that the cone is finite. In
particular, the t=2 exceptional positive-dimensional cone is compatible with
the statement because its points have `B eta=0`.

### Derivation

Before removing a pole, put

\[
 a=\frac{3K^2}{4y^2x},\qquad d_0=\frac{3bK}{2yx},\qquad
 w=\frac Yg-\frac{KF}{gyx}+a.
\]

Writing `delta=D0=g*kappa`, direct elimination of U',V' from D2,D1 gives

\[
 2xww'=w^2+(B-2a-d_0)w+\frac{a(a+d_0)}3-Ba
       +\frac{3b_1K}{2y}-\frac{3x\kappa}{y}.
 \tag{F5}
\]

In these expressions the only pole of w is `-b^2/(4x)`. More explicitly,

\[
 W=w+\frac{b^2}{4x}
   =\frac{xS}{g}-B-\frac{x^2CT}{gy}
      -\frac{bxC}{2y}+\frac{3x^3C^2}{4y^2}
 \tag{F6}
\]

is polynomial, and the boundary identities imply

\[
 W(0)=-B,\quad
 \eta=\frac{3\mathcal R}{y},\quad
 b_1=-\frac{b\eta}{3},\quad
 \kappa=\frac{By\eta}{3}.
 \tag{F7}
\]

Substitution of `w=W-r/x` in (F5), followed by (F7), gives (F3). Its leading
coefficient is the same omega as in (A7), because the pole removal and the
terms involving b do not change the top coefficient. Thus every cone point
produces a solution (F1)--(F3), and

\[
 \tau=-g\kappa=-\frac{gy}{3}B\eta.
 \tag{F8}
\]

### Polynomial reconstruction and normalization

Conversely, suppose C,W,B,b satisfy (F1)--(F3). Define T by D3, with an
arbitrary integration constant. Define

\[
 \boxed{U'=
 \frac{y(2xW'-W-B)}{3x}
 +\frac{x^2C(5C+2xC')}{4y}
 -bC-\frac b2xC'},
 \tag{F9}
\]

\[
 \boxed{S=\frac{g(W+B)}x
       -\frac{3gx^2C^2}{4y^2}+\frac{gbC}{2y}+\frac{xCT}{y}}.
 \tag{F10}
\]

The quotients in (F9)--(F10) are polynomial because `W(0)=-B`. Put
`F=xT-gb`, `Y=xS-bT-gB`, `b1=-b eta/3`, and set

\[
 V'=\frac{ygb_1-KY'+K'Y+2U'F}{2yx}.
 \tag{F11}
\]

This too is polynomial. Indeed, (F9) gives
`U'(0)=y eta/3-b C0`, while (F10) and D3 give
`Y'(0)=g eta-2gb C0/y`. The constant numerator in (F11) is exactly
`yg(b1+b eta/3)=0`. The degree bounds are

\[
 \deg U'=2t,\quad \deg T=t,\quad
 \deg S\le2t,\quad \deg V'\le3t.
\]

D1 holds by construction, D2 follows on substituting (F9)--(F10), and D3
is the definition of T. The universal identity (F5) plus (F3) proves

\[
 D_0\equiv\frac{gy}{3}B\eta.
\]

The leading coefficients are the required ones. Formula (F1) gives
`lead U'=q`; D3 gives
`lead T=g(3t+2)/(2yt)=g2`. Then

\[
 \operatorname{lead}S=g\omega-\frac{3g}{4y^2}+\frac{g_2}{y}=g_1,
\]

\[
 \operatorname{lead}V'=\frac{-t g_1+2qg_2}{2y}=e.
\]

Each equality is a direct identity in `Q(t,d)/(3d^2-t-1)`; they were also
mechanically reduced to zero by the universal driver.

Integrate U' to a monic degree-q polynomial U. If its `x^(q-1)` coefficient
is `lambda`, choose `b4=lambda/q` and set `h=x+b4`; then U as a polynomial
in h has zero `h^(q-1)` coefficient. Choose its additive constant so that
`U(h=0)=0`. Thus it has exactly the original allowed U shape.

The integration gauge of T can enforce the V' gauge: replacing T by
`T+epsilon` changes S by `epsilon*xC/y`, and changes V' by
`epsilon*U'/y`, while C,W,U',B,b remain fixed. Consequently the coefficient
`[h^(2t)]V'` changes by `epsilon*q/y`, a unit pivot; choose epsilon so that
this coefficient is zero. Integrating V' gives a monic degree-e V, whose
irrelevant additive constant can be set as prescribed. The same gauge could
instead be fixed by `T(L=0)=0`, as in the compact frozen driver; terminal
rows are invariant under this `P -> P+(epsilon/y)Q` change.

The reconstructed polynomials now have all the normalized ansatz shapes,
and `D0` is constant. In particular all high D0 bands vanish. The banked
high-spine pivot theorem has units factorwise for every `t>=2`, so its
uniqueness forces these reconstructed coefficients to be precisely the
solved spine at the resulting residual point. The positive terminal rows
vanish there, and (F8) holds. Thus a solution satisfying (F4) is exactly an
(8.1) counterexample, and the converse already proved gives the equivalence.

### Verification and status

`structural_abel_general.py` checks the all-b3 elimination with symbolic
functions, the parent's pole-elimination formula, (F9)--(F10), and every
normalized leading coefficient. It prints

```text
ALL_B3_LAURENT_ABEL_PASS
REGULAR_LAURENT_FORM_PASS
PARENT_POLE_ELIMINATION_PASS
POLYNOMIAL_RECONSTRUCTION_PASS
ALL_NORMALIZED_LEADING_COEFFICIENTS_PASS
```

in a foreground run of about 2.4 s. The coefficient field is characteristic
zero; the checks are universal algebraic identities, not tests at finitely
many t.

The new full atom (F1)--(F4) remains **OPEN**. It is the most concrete
coefficient-sensitive new next step identified in this sublane: classify
the normalized polynomial solutions of the single Abel equation (F3), or
prove `B eta=0` for them. A degree-only leading comparison cannot suffice,
because it gives exactly the valid banked quadratic normalization. No
normalization of a determinantal curve, unproved divisor condition, or
single-chart fraction is needed in this reduction.

## 5. Hyperelliptic formulation and what it does not prove

Over a generic level `a` of the original polynomial Q, set `z=1/pi` and

\[
 v=K+2yxz,\qquad
 D_a(x)=K^2-4yx(U-a).
\]

Then the generic fibre is birational to

\[
 v^2=D_a(x),\qquad \deg D_a=2t+2,
\]

with leading coefficient `1-4y`, a unit at the admissible integer indices.
Thus the geometric genus is at most `t`, equal to `t` when the hyperelliptic
polynomial is squarefree. Reduction of the cubic Laurent P modulo the
quadratic equation of Q gives

\[
 H(x,a)=\frac gy a+Y+\frac Ky\left(\frac{gxC}y-T\right)-\frac gyU,
\]

\[
 P=A(x,a)+\frac{H(x,a)}{2yx}v,
\]

where

\[
 A=V+\frac{(a-U)(T-gxC/y)}y-\frac{HK}{2yx}.
\]

`H` is polynomial in `x` and affine in `a`. On a cone point,

\[
 dP=-\frac{\tau+c b_1z+c b_2z^2+c b_3z^3-cxz^4}{v}\,dx.
\]

This provides an exact-differential/period formulation over the generic
hyperelliptic fibre. No vanishing theorem for the resulting period class has
been obtained. In particular, a naive Riemann--Hurwitz contradiction is
false: in addition to the two poles of P of orders `e=3t+1` at large `x`,
there is an extra simple pole at the point over `pi=0` at infinity. The map
has degree `2e+1=6t+3`, and its ramification count is compatible with genus
`t` both when `tau=0` and when `tau != 0`. The sibling Moh sublane independently
identified the same count and the bare Belyi structure.

## 6. Guardrails on the proposed Gamma valuation route

1. The frozen rank report's EN-CURVE theorem explicitly assumes
   `V(J_tail)={0}` before proving expected height and Cohen--Macaulay
   dimension one. Its all-t expected-height premise is not available as an
   unconditional theorem in the charged inputs. The later reports repeat
   the formulas, but this does not discharge the original premise.
2. A one-dimensional Cohen--Macaulay local ring need not be a DVR or even
   reduced. For example `k[u,v]/(v^2)` is a one-dimensional CM ring; the
   cusp `k[s^2,s^3]` is a reduced one-dimensional CM domain whose local ring
   at the origin is not a DVR. Valuations belong to branches of a
   normalization after passing to the reduction, not automatically to
   every point of the original CM scheme.
3. Even assuming a reduced weighted cone component normalizes to a line,
   the pullback of a homogeneous form is either zero or a scalar times the
   dictated power of the line parameter. The valuation is then either
   infinity or the dictated degree. The distinction is precisely the
   missing coefficient nonvanishing; weights alone do not decide it.
4. The point count `d_Gamma` is a weighted degree including multiplicities
   and orbifold weights, and is not literally an integer number of distinct
   points (`d_Gamma(3)=15/2`).

These cautions do not refute a future normalization/valuation proof with
additional structure. They prevent the proposed CM=>DVR shortcut from
assuming the missing theorem.

No background job is running from this sublane. No ledger, main report,
`jc2-lean`, or other lane file was edited.
