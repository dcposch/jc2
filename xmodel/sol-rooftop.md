# The balanced rooftop: exact energy, wrong-way Hodge, and the Keller-only wall

**Date:** 2026-08-23  
**Scope:** sharpened G5 rooftop-unit audit, based on
`xmodel/sol-g5rees.md`, `xmodel/sol-pcc-orbits.md`, and `TDBOUND.md`.  
**Status convention:** **EXACT** means proved below from the stated pencil or
Jacobian identities. Every proposed new inequality is labelled
**CONJECTURE**.

## 0. Verdict

**VERDICT: OBSTRUCTED.** The unit bound is not proved, and no
`B`-independent weak finite bound is proved.

The sharpened conclusions are:

1. The balanced rooftop is canonical and its energy has the exact four-way
   description

   \[
   \boxed{
   \mathcal E_{\rm MR}
   =B^2-\|\mathbf H_\cap\|^2
   =\frac12\left\|\frac{\mathbf Z_f}{\alpha}
                    -\frac{\mathbf Z_g}{\beta}\right\|^2
   =\frac{\operatorname{td}}{\alpha\beta}
   =\sum_P\frac{a_Pb_P}{\nu_P}.}
   \tag{0.1}
   \]

   This is **EXACT**, but it computes the desired quantity; it does not
   bound it.

2. Hodge index, Teissier--Rees--Sharp log-concavity, and mixed-volume
   convexity all have the wrong sign for G5. They give
   `E_MR >= 0`, equivalently an *upper* bound on the mixed multiplicity.
   G5 needs an almost-maximal *lower* bound on that mixed multiplicity.

3. The constant-Jacobian condition does yield a sharper exact projective
   identity than was displayed in `sol-g5rees.md`:

   \[
   F_XG_Y-F_YG_X=J(f,g)Z^{d+e-2},                    \tag{0.2}
   \]

   and hence, for
   `Psi=[F^beta:G^alpha:Z^N]`,

   \[
   \det D\Psi
   =c\,F^{\beta-1}G^{\alpha-1}Z^{N+d+e-3}.          \tag{0.3}
   \]

   Thus every residual critical contribution is created at the boundary
   while resolving the balanced base ideal. This identifies exactly where
   a proof must live. It does not give a numerical capacity bound.

4. The normalized multi-Rees algebra is finite over the ordinary
   multi-Rees algebra, so it does force **pointwise finiteness** of the
   energy for each fixed pair. That is not the finite bound needed for
   cofinality. Cofinality requires a constant independent of `B` (or a
   type-dependent constant on an already finite type menu).

5. Finite generation, rooftop convexity, and even the common leading-power
   property cannot supply such a uniform constant. For every fixed coprime
   `2 <= alpha < beta`, the explicit dominant non-Keller family

   \[
   f_B=x^{B\alpha}+y,\qquad
   g_B=x^{B\beta}+y^{B\beta-1}                       \tag{0.4}
   \]

   has the same balanced leading form
   `F_d=(X^B)^alpha`, `G_e=(X^B)^beta`, has a finite normalized
   multi-Rees algebra, and satisfies

   \[
   \boxed{\mathcal E_{\rm MR}=B^2-\frac{B}{\beta}.} \tag{0.5}
   \]

   Hence these formal structures allow energy asymptotic to the full
   Bezout value `B^2`. The missing ingredient is the *full* Keller identity
   (0.2), not merely its leading-form consequence.

The smallest honest remaining statement is **CONJECTURE KJN(C)** in
Section 7, the Jacobian-net degree bound. It is a clean homogeneous
intersection-theoretic form of the weak rooftop bound, but it is equivalent
to that bound rather than a proof of it. No standard inequality audited
here implies KJN(C).

---

## 1. Set-up and the canonical rooftop

Put

\[
d=B\alpha,\qquad e=B\beta,\qquad
N=\beta d=\alpha e=B\alpha\beta,                    \tag{1.1}
\]

and let

\[
\mathfrak a=(F,Z^d),\qquad
\mathfrak b=(G,Z^e).                                \tag{1.2}
\]

On a simultaneous point resolution, write the exceptional point-basis
divisors as `Z_f,Z_g` and put

\[
\mathbf X=\frac{\mathbf Z_f}{\alpha},\qquad
\mathbf Y=\frac{\mathbf Z_g}{\beta}.                \tag{1.3}
\]

The balanced ideal is

\[
\mathfrak c
=\overline{\mathfrak a^\beta+\mathfrak b^\alpha}
=\overline{(F^\beta,G^\alpha,Z^N)},                 \tag{1.4}
\]

and its normalized b-divisor is

\[
\mathbf H_\cap=\frac{\mathbf Z(\mathfrak c)}
                       {\alpha\beta}.               \tag{1.5}
\]

For every divisorial valuation `v`,

\[
\frac{v(\mathfrak c)}{\alpha\beta}
=\min\!\left(\frac{v(\mathfrak a)}\alpha,
              \frac{v(\mathfrak b)}\beta\right).  \tag{1.6}
\]

This is **EXACT**: `v(I+J)=min(v(I),v(J))`, powers multiply values,
and integral closure preserves all divisorial ideal values. Thus the
rooftop is canonical on the Riemann--Zariski surface. No packet
concentration, KPC, PCC floor, or choice of a common ordinary center enters
its definition.

The caveat from `sol-g5rees.md` remains essential: (1.6) is a minimum in
valuation coordinates. Its point-basis trace is obtained through the
proximity/antinef transform and is not the coordinatewise PCC floor.

---

## 2. Exact computation of the energy

### 2.1 Resolved pencils

Let

\[
C_f=dH-\mathbf Z_f,\qquad C_g=eH-\mathbf Z_g          \tag{2.1}
\]

be the mobile fiber classes. For generic finite target values,

\[
C_f^2=C_g^2=0,\qquad C_fC_g=\operatorname{td}.       \tag{2.2}
\]

Using `||U||^2=-U^2` on exceptional divisors gives

\[
\begin{aligned}
\|\mathbf X\|^2&=B^2,\\
\|\mathbf Y\|^2&=B^2,\\
\langle\mathbf X,\mathbf Y\rangle
 &=B^2-\frac{\operatorname{td}}{\alpha\beta}.
\end{aligned}                                       \tag{2.3}
\]

Therefore

\[
\boxed{
\frac12\|\mathbf X-\mathbf Y\|^2
=\frac{\operatorname{td}}{\alpha\beta}.}           \tag{2.4}
\]

This is the resolved-pencil form of `Delta^2=-2td/(alpha beta)`.

### 2.2 The balanced net

The three balanced generators define

\[
\Psi=[F^\beta:G^\alpha:Z^N]:\mathbf P^2
\dashrightarrow\mathbf P^2.                         \tag{2.5}
\]

On `Z=1`, this is `(f^beta,g^alpha)`. Since `f,g` are algebraically
independent,

\[
\deg\Psi
=[k(x,y):k(f^\beta,g^\alpha)]
=\alpha\beta\operatorname{td}.                     \tag{2.6}
\]

On a resolution of the balanced base ideal, a target line has class

\[
L=NH-\mathbf Z(\mathfrak c).                        \tag{2.7}
\]

Thus

\[
\alpha\beta\operatorname{td}
=L^2=N^2-\|\mathbf Z(\mathfrak c)\|^2.              \tag{2.8}
\]

After division by `(alpha beta)^2`,

\[
\boxed{
\|\mathbf H_\cap\|^2
=B^2-\frac{\operatorname{td}}{\alpha\beta}.}       \tag{2.9}
\]

Combining (2.3), (2.4), and (2.9) proves

\[
\boxed{
\|\mathbf H_\cap\|^2
=\langle\mathbf X,\mathbf Y\rangle,\qquad
\mathcal E_{\rm MR}
=B^2-\|\mathbf H_\cap\|^2
=\frac12\|\mathbf X-\mathbf Y\|^2.}               \tag{2.10}
\]

The Sigray identity in `TDBOUND.md` then supplies the final equality in
(0.1).

This computation is resolution-independent. Further blowups pull back the
Cartier b-divisors and leave all displayed intersections unchanged.

### 2.3 Mixed-multiplicity form

Set

\[
I=\overline{\mathfrak a^\beta},\qquad
J=\overline{\mathfrak b^\alpha}.                    \tag{2.11}
\]

Their total boundary self-multiplicities and mixed multiplicity are

\[
e_\infty(I)=e_\infty(J)=N^2,\qquad
e_\infty(I,J)=N^2-\alpha\beta\operatorname{td}.     \tag{2.12}
\]

For this balanced pencil situation,

\[
e_\infty(\mathfrak c)=e_\infty(I,J).                \tag{2.13}
\]

Consequently the sharp and weak targets are respectively

\[
\begin{aligned}
\mathcal E_{\rm MR}\le1
&\Longleftrightarrow
e_\infty(I,J)\ge N^2-(\alpha\beta)^2,               \tag{2.14}\\
\mathcal E_{\rm MR}\le C
&\Longleftrightarrow
e_\infty(I,J)\ge N^2-C(\alpha\beta)^2.              \tag{2.15}
\end{aligned}
\]

Thus the desired result says that two boundary ideals of self-multiplicity
`N^2` have mixed multiplicity within `O((alpha beta)^2)` of its maximum,
uniformly as `N=B alpha beta` grows.

---

## 3. Why convexity and Hodge index do not give the ceiling

### 3.1 The exact sign

The exceptional intersection norm is positive definite. Cauchy--Schwarz,
equivalently the surface form of the Teissier--Rees--Sharp reverse
Alexandrov--Fenchel inequality, gives

\[
e_\infty(I,J)^2
\le e_\infty(I)e_\infty(J)=N^4.                     \tag{3.1}
\]

Hence

\[
e_\infty(I,J)\le N^2.                               \tag{3.2}
\]

Using (2.12), this is precisely

\[
\operatorname{td}\ge0
\quad\Longleftrightarrow\quad
\mathcal E_{\rm MR}\ge0.                           \tag{3.3}
\]

It is the wrong side of (2.14). Hodge index says
`Delta^2 <= 0`; G5 requires the non-Hodge lower bound
`Delta^2 >= -2`.

The rooftop operation does not reverse this sign. It gives the canonical
identity `||H_cap||^2=<X,Y>`, but convexity permits two radius-`B`
vectors to have inner product anywhere from near `B^2` down to zero.
The unit bound asserts the very strong stability estimate

\[
\frac{\langle\mathbf X,\mathbf Y\rangle}
     {\|\mathbf X\|\|\mathbf Y\|}
\ge1-\frac1{B^2}.                                    \tag{3.4}
\]

No equality or stability theorem for mixed multiplicities gives (3.4)
from finite generation or antinefness.

### 3.2 Mixed volume has the same obstruction

For monomial or divisorial models, Newton regions turn multiplicity into a
covolume and mixed multiplicity into its polarization. Reverse
Alexandrov--Fenchel again yields (3.1), not (2.14). The desired inequality
is not log-concavity; it is a Keller-specific *near-equality theorem* for
two generally distinct complete ideals.

### 3.3 ADE does not supply a free `-2` bound

A possible residual-ADE route must establish more than that the supporting
intersection graph is Du Val. A negative-definite ADE lattice contains
classes of arbitrarily negative square: if `E^2=-2`, then

\[
(kE)^2=-2k^2.                                        \tag{3.5}
\]

Only roots, not all supported classes, have square `-2`. Therefore an ADE
support would prove `Delta^2 >= -2` only after a separate theorem shows that
the normalized residual difference is a root (or zero), including its
integrality and primitivity. Rooftop convexity does not give that theorem.

---

## 4. What the constant Jacobian gives exactly

The preceding obstruction uses only intersection theory. The full Keller
condition gives a much more rigid identity, which is worth isolating.

### Theorem 4.1 -- pure boundary Jacobian (**EXACT**)

Let `F,G` be the degree-`d,e` homogenizations of `f,g`, and assume
`J(f,g)=j in k*`. Then

\[
\boxed{F_XG_Y-F_YG_X=jZ^{d+e-2}.}                   \tag{4.1}
\]

#### Proof

The left side is homogeneous of degree `d+e-2`. On `Z=1` it equals
`f_xg_y-f_yg_x=j`. The only homogeneous form of degree `d+e-2` whose
dehomogenization is the constant `j` is `jZ^(d+e-2)`. \(\square\)

### Corollary 4.2 -- Jacobian of the balanced net (**EXACT**)

For the three homogeneous coordinate forms

\[
A=F^\beta,\qquad B_0=G^\alpha,\qquad C=Z^N,
\]

one has

\[
\boxed{
\det\frac{\partial(A,B_0,C)}{\partial(X,Y,Z)}
=j\alpha\beta N
 F^{\beta-1}G^{\alpha-1}Z^{N+d+e-3}.}               \tag{4.2}
\]

Indeed, expansion along the third row gives

\[
NZ^{N-1}\alpha\beta F^{\beta-1}G^{\alpha-1}
(F_XG_Y-F_YG_X),
\]

and (4.1) finishes the calculation.

Formula (4.2) says more than “ramification is at infinity.” Before base
resolution, the entire critical divisor of the balanced projective net is
the two known power-map fibers plus the line at infinity. Every further
ramification coefficient is produced by pulling these divisors through the
base-point resolution and adding discrepancies.

This is the exact Keller-specific datum missing from the countermodels in
Section 5. A successful intersection proof must convert the resolved
multiplicities in (4.2) into (2.14) or (2.15).

### 4.3 Why the immediate log argument cancels

Let `T={UVW=0}` be the coordinate triangle in the target. Then

\[
K_{\mathbf P^2}+T\sim0.                              \tag{4.3}
\]

On

\[
U_X=\mathbf A^2\setminus\{fg=0\},
\]

the balanced map lands in `P^2\T=(G_m)^2`, and

\[
\Psi^*\!\left(\frac{dU}{U}\wedge\frac{dV}{V}\right)
=\alpha\beta j\frac{dx\wedge dy}{fg}.               \tag{4.4}
\]

It is nowhere zero on `U_X`. Thus the natural logarithmic target is log
Calabi--Yau, and the log ramification formula has no positive multiple of
the line class on its right:

\[
K_X+D_X
=\Psi^*(K_{\mathbf P^2}+T)+R_{\log}
=R_{\log}.                                           \tag{4.5}
\]

Effectivity of `R_log` therefore does not directly control
`L^2=alpha beta td`. Pairing the ordinary ramification formula

\[
R_\Psi=K_X+3L                                        \tag{4.6}
\]

with `L` merely introduces the uncontrolled term `K_X.L`; the number and
depth of boundary blowups can grow with `B`.

This is not a theorem that every refined log-BMY construction must fail.
It is a precise obstruction to obtaining the unit bound “for free” from
the standard log pair, effectivity, or Hodge index. A successful BMY route
would need an additional Keller-specific bound on the resolved boundary
discrepancies or on the logarithmic differential cokernel.

---

## 5. What finite generation really proves

### 5.1 Pointwise finiteness (**EXACT**)

The ordinary multi-Rees algebra

\[
\mathscr R(\mathfrak a,\mathfrak b)
=\mathcal O[\mathfrak a u,\mathfrak b v]             \tag{5.1}
\]

is a finite-type algebra on every affine chart. These rings are excellent,
so their normalizations are finite. Consequently the normalized
multi-blowup is a finite-type model with finitely many exceptional prime
divisors. The balanced diagonal is determined on a finite model, and its
self-intersection is a finite rational number.

Thus finite generation proves

\[
\mathcal E_{\rm MR}(f,g)<\infty                      \tag{5.2}
\]

for each fixed pair.

But (5.2) is already visible from

\[
0\le\mathcal E_{\rm MR}\le B^2.                    \tag{5.3}
\]

It is not cofinal. What G5 needs is

\[
\exists C<\infty\quad\forall B:\quad
\mathcal E_{\rm MR}\le C,                          \tag{5.4}
\]

or, on a finite type menu, constants `C_(alpha,beta)` independent of `B`.
Noetherianity contains no uniform bound on the number, slopes, coefficients,
or proximity depth of the normalized generators as the input degrees grow.

### 5.2 Uniform finite generation is refuted by an exact control

Fix coprime integers `2 <= alpha < beta` and let

\[
d=B\alpha,\qquad e=B\beta.
\]

Define

\[
f_B=x^d+y,\qquad g_B=x^e+y^{e-1}.                    \tag{5.5}
\]

These polynomials are algebraically independent. Put `u=f_B`. Then
`y=u-x^d`, and

\[
g_B=x^e+(u-x^d)^{e-1}.                               \tag{5.6}
\]

As a polynomial in `x` over `k(u)`, the right side has degree
`d(e-1)`, since `d(e-1)>e`. Therefore

\[
\operatorname{td}(f_B,g_B)
=[k(u,x):k(u,g_B)]
=d(e-1).                                             \tag{5.7}
\]

The homogenizations are

\[
F=X^d+YZ^{d-1},\qquad
G=X^e+Y^{e-1}Z,                                      \tag{5.8}
\]

so on `Z=0`,

\[
F_d=X^d=(X^B)^\alpha,\qquad
G_e=X^e=(X^B)^\beta.                                 \tag{5.9}
\]

Thus the leading forms have exactly the balanced common-power alignment
forced in the intended pencil frame. Nevertheless, the exact energy formula
gives

\[
\begin{aligned}
\mathcal E_{\rm MR}
 &=\frac{d(e-1)}{\alpha\beta}\\
 &=\frac{B\alpha(B\beta-1)}{\alpha\beta}\\
 &=\boxed{B^2-\frac B\beta}.
\end{aligned}                                       \tag{5.10}
\]

Equivalently, the normalized rooftop retains only

\[
\|\mathbf H_\cap\|^2=\frac B\beta.                 \tag{5.11}
\]

Every multi-Rees algebra in this family is finitely generated and has
finite normalization, yet the energies are unbounded and asymptotic to
`B^2`.

The family is deliberately not Keller:

\[
J(f_B,g_B)
=d(e-1)x^{d-1}y^{e-2}-ex^{e-1}.                     \tag{5.12}
\]

It is therefore not a counterexample to G5-RBE. It is a counterexample to
each proposed implication

\[
\begin{gathered}
\text{finite normalized multi-Rees algebra},\\
\text{complete/antinef rooftop},\\
\text{balanced common denominator and common leading power}
\end{gathered}
\quad\Longrightarrow\quad
\mathcal E_{\rm MR}\le C                            \tag{5.13}
\]

for any `B`-independent `C`.

For comparison, generic pairs with disjoint leading zero sets have
`td=de`, `H_cap=0`, and `E_MR=B^2`; thus the full Bezout endpoint is also
attained when the common-leading-power condition is dropped.

### 5.3 Finite-generation verdict

The answer to attack (3) is therefore two-tiered:

- **YES, pointwise:** normalization gives a finite model and a finite
  intersection number for every fixed pair.
- **NO, uniformly:** it supplies no bound independent of `B`, even with
  fixed `(alpha,beta)`, a fixed number of original generators, and balanced
  leading forms.

Only the second meaning is useful for cofinality.

---

## 6. The exact remaining geometric wall

On a common cluster let `P` be the proximity matrix and let

\[
\rho^f=PR,\qquad \rho^g=PS,
\qquad
\delta=\frac{\rho^f}{\alpha}-\frac{\rho^g}{\beta},
\qquad
G=(P^{-1})^TP^{-1}.                                  \tag{6.1}
\]

Then

\[
\mathcal E_{\rm MR}=\frac12\delta^TG\delta.         \tag{6.2}
\]

Finite generation says that `delta` is represented on a finite model.
Antinefness says that `rho^f,rho^g` are separately nonnegative. Neither
controls the Green norm of their signed difference.

The pure-boundary Jacobian identity (4.1) imposes relations among the
successive coefficients of these two charges. What is absent is a theorem
that turns those relations into

\[
\frac12\delta^TG\delta\le C.                         \tag{6.3}
\]

This is a uniform boundary-capacity theorem. It must control both the size
of each breakpoint and its proximity depth; bounding only the number of
Rees valuations, or only linear contact sums, cannot bound the Green energy.

No audited identity supplies that control. The Laurent breakpoint example
in `sol-g5rees.md` shows why local packet power plus normality cannot do it,
and the family (5.5) shows why global leading alignment cannot do it.

---

## 7. Minimal sublemma and status

The cleanest irreducibly Keller-specific formulation is the following.

### CONJECTURE KJN(C) -- Jacobian-net degree bound

Let `F,G` be homogeneous forms of degrees `B alpha,B beta` such that

\[
F_XG_Y-F_YG_X=jZ^{B(\alpha+\beta)-2},\qquad j\ne0,   \tag{7.1}
\]

and suppose their dehomogenizations are dominant. Put

\[
\Psi=[F^\beta:G^\alpha:Z^{B\alpha\beta}].            \tag{7.2}
\]

There is a constant `C<infinity`, independent of `B`, such that

\[
\boxed{\deg\Psi\le C(\alpha\beta)^2.}               \tag{7.3}
\]

The sharp conjecture is `C=1`.

By (2.6),

\[
\deg\Psi=\alpha\beta\operatorname{td}
=(\alpha\beta)^2\mathcal E_{\rm MR}.                \tag{7.4}
\]

Therefore KJN(C) is equivalent to G5-RBE(C). Its advantage is not logical
weakening; it is that all hypotheses and the only Keller-specific identity
are visible in one projective net. It asks for a degree bound on rational
maps whose Jacobian divisor has the exact three-factor form (4.2).

Equivalently, on the normalized blowup of the three-generated base ideal,
KJN(C) is

\[
N^2-\|\mathbf Z(\mathfrak c)\|^2
\le C(\alpha\beta)^2.                                \tag{7.5}
\]

Any proof must use more than the support of the critical divisor: it must
use the exact Keller multiplicities and their transforms at every boundary
breakpoint.

### Status ledger

| Statement | Status |
|---|---|
| balanced rooftop is canonical | **EXACT** |
| rooftop energy equals `td/(alpha beta)` | **EXACT** |
| energy equals `Sum a_P b_P/nu_P` | **EXACT**, using `TDBOUND.md` |
| Hodge / mixed-volume inequality gives the unit bound | **NO; wrong direction** |
| ADE support alone gives `Delta^2 >= -2` | **NO; the residual class must separately be a root** |
| projective Jacobian identities (4.1)--(4.2) | **EXACT** |
| ordinary log-ramification effectivity gives a degree ceiling | **NO immediate implication; line class cancels in the natural log pair** |
| normalized multi-Rees finite generation gives per-pair finite energy | **EXACT** |
| finite generation gives a `B`-uniform finite bound | **NO; refuted without Keller by (5.5)** |
| any `B`-independent `C` for Keller pairs | **CONJECTURE KJN(C) / G5-RBE(C)** |
| sharp unit bound | **CONJECTURE KJN(1)** |

## 8. Final conclusion

The rooftop construction has done all the canonicalization one can ask of
it. It replaces packet concentration and computes the whole G5 defect on a
single normalized three-generated ideal. But its convexity is bookkeeping,
not coercivity.

The sharp obstruction can now be stated without ambiguity:

\[
\boxed{
\text{prove that the pure-boundary Jacobian identity (4.1), after base
resolution, forces a uniform Green-capacity bound (6.3).}}
\]

Hodge index proves the opposite-side inequality. Log-Calabi--Yau
ramification cancels the line class. Finite generation is only pointwise,
and explicit common-leading-power controls have energy
`B^2-B/beta`. Therefore neither the unit bound nor any cofinal weak finite
bound is presently proved.

The honest final label is:

\[
\boxed{
\textbf{OBSTRUCTED: exact reduction to CONJECTURE KJN(C); no uniform }C
\textbf{ obtained.}}
\]
