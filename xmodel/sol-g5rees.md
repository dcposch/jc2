# G5 by normalized multi-Rees energy: the balanced rooftop is canonical, but its unit bound is new

**Date:** 2026-08-23  
**Scope:** execution of connection rank 2 in `sol-connections.md`, using
`sol-wtc1-round2.md`, `sol-pcc-orbits.md`, and `TDBOUND.md`.  
**Status convention:** statements marked **EXACT** are deductions from the
resolved-pencil identities or are proved below. Every missing inequality is
marked **CONJECTURE**.

## 0. Verdict

The multi-Rees route gives a clean replacement for packet concentration, but
not yet a bound.

1. There is a canonical common b-divisor. It is not the coordinatewise PCC
   floor and it does not require KPC. If

   \[
   \mathfrak a=(F,Z^{B\alpha}),\qquad
   \mathfrak b=(G,Z^{B\beta}),\qquad N=B\alpha\beta,
   \]

   define the **balanced diagonal ideal**

   \[
   \mathfrak c
   :=\overline{\mathfrak a^\beta+\mathfrak b^\alpha}
   =\overline{(F^\beta,G^\alpha,Z^N)}.                 \tag{0.1}
   \]

   Its normalized ideal b-divisor

   \[
   \mathbf H_\cap:=\frac{1}{\alpha\beta}\mathbf Z(\mathfrak c) \tag{0.2}
   \]

   is the valuationwise meet of the two normalized pencil b-divisors.

2. The correct normalized multi-Rees energy is **EXACTLY**

   \[
   \boxed{
   \mathcal E_{\rm MR}
   :=B^2-\|\mathbf H_\cap\|^2
   =\frac12\left\|
      \frac{\mathbf Z_f}{\alpha}-
      \frac{\mathbf Z_g}{\beta}\right\|^2
   =\frac{\operatorname{td}}{\alpha\beta}
   =\sum_{P\ {\mathrm{pole}}}\frac{a_Pb_P}{\nu_P}.}    \tag{0.3}
   \]

   Here the exceptional intersection norm is
   `||U||^2 := -U^2`. Thus the desired G5 ceiling is precisely the unit-energy
   inequality `E_MR <= 1`.

3. The normalized bi-Rees algebra does **not** supply KPC. It records the
   ordinary multiplicity drop after it occurs; normalization does not prevent
   it. In the Laurent separation control of `sol-wtc1-round2.md`, the balanced
   ideal has packet value 6 along the limiting flag but ordinary value 3 at
   its first center. Its Rees support function simply acquires a legitimate
   breakpoint. The vectors `(1,1)` and `(2,1)` also satisfy the usual
   proximity inequalities. Therefore KPC cannot be obtained from Rees
   normality, antinefness, the paired boundary powers, both denominator
   capacities, and the local Jacobian identity.

4. Log ramification adds the correct Keller-specific datum—ramification is
   confined to the boundary after the known power-map ramification is
   removed—but its standard divisor formula is linear in the two fiber
   classes. The energy is the square of their normalized difference. No
   available effectivity, Hodge-index, proximity, or Zariski-Main statement
   bounds that signed square.

5. Consequently this route presently gives no finite `td` bound. Its
   unconditional estimate is only

   \[
   0\le\mathcal E_{\rm MR}\le B^2,
   \qquad \operatorname{td}\le B^2\alpha\beta=\deg f\deg g, \tag{0.4}
   \]

   which is Bézout and is not cofinal as `B` varies. The minimal missing
   statement is **CONJECTURE G5-RBE** in §7. A bound by any absolute constant,
   not necessarily one, would already make the finite type ladder cofinal;
   no such constant follows here.

The gain is therefore structural and exact: KPC and PFE disappear from the
logical dependency, the common part becomes canonical, and the whole G5 wall
becomes one normalized mixed-multiplicity/Green-energy inequality. The loss is
equally clear: that inequality is equivalent to the desired `td` ceiling, not
a proof of it.

---

## 1. Resolved pencils and the exceptional Hilbert space

Let

\[
d=B\alpha,\qquad e=B\beta,\qquad
2\le\alpha<\beta,\qquad (\alpha,\beta)=1.             \tag{1.1}
\]

Write

\[
\mathfrak a=(F,Z^d),\qquad \mathfrak b=(G,Z^e)        \tag{1.2}
\]

for the two projective pencil base ideals. Replace them by their integral
closures; this changes neither their divisorial values nor their point bases.
On a sufficiently high simultaneous point resolution, write their exceptional
divisors in the orthogonal total-transform basis as

\[
\mathbf Z_f=\sum_pR_pE_p^*,\qquad
\mathbf Z_g=\sum_pS_pE_p^*.                           \tag{1.3}
\]

The mobile fiber classes are

\[
C_f=dH-\mathbf Z_f,\qquad C_g=eH-\mathbf Z_g.         \tag{1.4}
\]

Put

\[
\langle U,V\rangle:=-U\mathbin\cdot V,
\qquad \|U\|^2=\langle U,U\rangle                    \tag{1.5}
\]

on exceptional Cartier b-divisors. Since
`E_p^* . E_q^* = -delta_pq`, this is the ordinary Euclidean pairing on
point-basis vectors. The resolved-pencil identities from
`sol-pcc-orbits.md` give

\[
\begin{aligned}
\|\mathbf Z_f\|^2&=B^2\alpha^2,\\
\|\mathbf Z_g\|^2&=B^2\beta^2,\\
\langle\mathbf Z_f,\mathbf Z_g\rangle
 &=B^2\alpha\beta-\operatorname{td}.                 \tag{1.6}
\end{aligned}
\]

Thus for

\[
\mathbf X:=\frac{\mathbf Z_f}{\alpha},\qquad
\mathbf Y:=\frac{\mathbf Z_g}{\beta},                \tag{1.7}
\]

both normalized divisors lie on the sphere of radius `B`:

\[
\|\mathbf X\|^2=\|\mathbf Y\|^2=B^2,\qquad
\langle\mathbf X,\mathbf Y\rangle
=B^2-\frac{\operatorname{td}}{\alpha\beta}.          \tag{1.8}
\]

Already this gives the exact distance identity

\[
\boxed{
\frac12\|\mathbf X-\mathbf Y\|^2
=\frac{\operatorname{td}}{\alpha\beta}.}             \tag{1.9}
\]

This is resolution-independent: blowing up after both ideals are principal
pulls back their Cartier divisors and leaves their intersection products
unchanged.

Equation (1.9) is the b-divisor version of `Delta^2 =
-2td/(alpha beta)` in `TDBOUND.md`. By itself it is only KME-2 in intrinsic
notation. The multi-Rees construction below adds a canonical common object,
not just the difference.

---

## 2. The normalized bi-Rees algebra and its balanced rooftop

### 2.1 The algebra

Consider the normalized bi-Rees algebra

\[
\mathscr R^\nu(\mathfrak a,\mathfrak b)
:=\overline{\mathcal O_{\mathbf P^2}
 [\mathfrak a u,\mathfrak b v]}.                      \tag{2.1}
\]

Equivalently, its `(m,n)` pieces record the integral closures of
`a^m b^n`. Its normalized multi-blowup carries the joint Rees valuations and
dominates the normalized blowups of each ideal. On the Riemann--Zariski
surface it records the two functions

\[
v\longmapsto v(\mathfrak a),\qquad
v\longmapsto v(\mathfrak b)                           \tag{2.2}
\]

on all divisorial valuations, together with the proximity transformations
between their traces on point models.

The correct diagonal is not `(1,1)`. The degrees are balanced by `(beta,0)`
and `(0,alpha)`. Put

\[
N=\beta d=\alpha e=B\alpha\beta                       \tag{2.3}
\]

and define `c` by (0.1).

### Theorem 2.1 — the balanced common b-divisor (**EXACT**)

For every divisorial valuation `v`, normalized so that it takes integral
values on local ideals,

\[
\frac{v(\mathfrak c)}{\alpha\beta}
=\min\left(\frac{v(\mathfrak a)}{\alpha},
           \frac{v(\mathfrak b)}{\beta}\right).       \tag{2.4}
\]

Moreover

\[
\overline{\mathfrak a^\beta+\mathfrak b^\alpha}
=\overline{(F^\beta,G^\alpha,Z^N)}.                   \tag{2.5}
\]

Hence `H_cap` in (0.2) is a canonical valuationwise common part of the two
normalized pencil ideals. It is constructed by one balanced slice of the
normalized bi-Rees algebra and requires no packet-to-center assignment.

#### Proof

For ideals, `v(I+J)=min(v(I),v(J))`, and values multiply under powers.
Therefore

\[
\begin{aligned}
v(\mathfrak a^\beta+\mathfrak b^\alpha)
 &=\min\bigl(\beta v(\mathfrak a),\alpha v(\mathfrak b)\bigr)\\
 &=\min\bigl(\beta v(F),\alpha v(G),Nv(Z)\bigr)\\
 &=v(F^\beta,G^\alpha,Z^N).                           \tag{2.6}
\end{aligned}
\]

The valuative criterion for integral closure gives (2.5), and division by
`alpha beta` gives (2.4). \(\square\)

### 2.2 Why this is not the PCC meet

PCC uses

\[
h_p=\min\left(\left\lfloor R_p/\alpha\right\rfloor,
               \left\lfloor S_p/\beta\right\rfloor\right)      \tag{2.7}
\]

in the **point basis**. Theorem 2.1 takes the minimum in **divisorial
valuation coordinates** and then passes through the proximity/antinef
transform to a point basis. Minimum, floor, and inverse proximity do not
commute. Consequently the point-basis coefficients of `H_cap` must not be
identified with `(h_p)`.

This distinction is the reason the new route genuinely bypasses classical
PCC. The rooftop is canonical even when contact splits and even when the two
ordinary point-basis vectors are not pointwise proportional. It gives up the
termwise PCC estimate in exchange for one global intersection number.

---

## 3. The exact normalized multi-Rees energy

### Theorem 3.1 — balanced degree/energy identity (**EXACT**)

Let `Z_c=Z(c)` be the exceptional base b-divisor of the balanced ideal. Then

\[
\boxed{
\|\mathbf H_\cap\|^2
=B^2-\frac{\operatorname{td}}{\alpha\beta}.}          \tag{3.1}
\]

Consequently

\[
\boxed{
\mathcal E_{\rm MR}
:=B^2-\|\mathbf H_\cap\|^2
=\frac{\operatorname{td}}{\alpha\beta}.}             \tag{3.2}
\]

#### Proof

The three generators in (2.5) define the rational map

\[
\Psi=[F^\beta:G^\alpha:Z^N]:\mathbf P^2\dashrightarrow\mathbf P^2. \tag{3.3}
\]

On the affine chart `Z=1`, this is

\[
(x,y)\longmapsto(f(x,y)^\beta,g(x,y)^\alpha).         \tag{3.4}
\]

Since `f,g` are algebraically independent,

\[
\begin{aligned}
[k(x,y):k(f^\beta,g^\alpha)]
 &=[k(x,y):k(f,g)]
   [k(f,g):k(f^\beta,g^\alpha)]\\
 &=\operatorname{td}\,\alpha\beta.                  \tag{3.5}
\end{aligned}
\]

Resolve the base ideal `c`. The pullback of a target line has mobile class

\[
L_\Psi=NH-\mathbf Z_c.                                \tag{3.6}
\]

The map is dominant onto `P^2`, so

\[
L_\Psi^2=\deg\Psi=\alpha\beta\operatorname{td}.      \tag{3.7}
\]

Since `H` is orthogonal to the exceptional lattice,

\[
\alpha\beta\operatorname{td}
=N^2+\mathbf Z_c^2
=N^2-\|\mathbf Z_c\|^2.                              \tag{3.8}
\]

Divide by `(alpha beta)^2` and use `N/(alpha beta)=B`. \(\square\)

### Corollary 3.2 — the rooftop/distance identity (**EXACT**)

The following three quantities coincide:

\[
\boxed{
B^2-\|\mathbf H_\cap\|^2
=\frac12\|\mathbf X-\mathbf Y\|^2
=B^2-\langle\mathbf X,\mathbf Y\rangle.}             \tag{3.9}
\]

Equivalently, this special balanced rooftop satisfies

\[
\|\mathbf H_\cap\|^2=\langle\mathbf X,\mathbf Y\rangle. \tag{3.10}
\]

Thus the proposed “common positive part” exists canonically, and its square
is computable. What remains conjectural is only the lower bound on that
square.

### 3.3 Mixed-multiplicity form

Let `e_infinity(I,J)` denote the total mixed base multiplicity, summed over
the boundary local rings. In the point basis,

\[
e_\infty(\mathfrak a,\mathfrak b)
=\sum_pR_pS_p.                                        \tag{3.11}
\]

For one ideal, the corresponding self-multiplicity is
\(e_\infty(I)=\|\mathbf Z(I)\|^2\).

For the balanced powers

\[
I=\overline{\mathfrak a^\beta},\qquad
J=\overline{\mathfrak b^\alpha},                     \tag{3.12}
\]

Theorem 3.1 and (1.6) give the special equality

\[
\boxed{
e_\infty(\mathfrak c)
=e_\infty(I,J)
=N^2-\alpha\beta\operatorname{td}.}                  \tag{3.13}
\]

Hence

\[
\mathcal E_{\rm MR}
=\frac{N^2-e_\infty(\mathfrak c)}{(\alpha\beta)^2}
=B^2-\frac{e_\infty(\mathfrak a,\mathfrak b)}
              {\alpha\beta}.                         \tag{3.14}
\]

This is the coefficient of the failure of maximal polarization in the
Bhattacharya/intersection quadratic form. Indeed

\[
\begin{aligned}
\|m\beta\mathbf Z_f+n\alpha\mathbf Z_g\|^2
 &=N^2(m+n)^2
   -2\alpha\beta\operatorname{td}\,mn.              \tag{3.15}
\end{aligned}
\]

The normalized multi-Rees algebra therefore carries the target energy
intrinsically; no root enumeration is needed to define it.

### 3.4 Pole-mass form

`TDBOUND.md` gives the exact Sigray-frame identity

\[
\frac{\operatorname{td}}{\alpha\beta}
=\sum_{P\ {\mathrm{pole}}}\frac{a_Pb_P}{\nu_P}.       \tag{3.16}
\]

Combining it with Theorem 3.1 produces the promised bridge:

\[
\boxed{
\sum_{P\ {\mathrm{pole}}}\frac{a_Pb_P}{\nu_P}
=B^2-\|\mathbf H_\cap\|^2
=\frac12\|\mathbf X-\mathbf Y\|^2.}                 \tag{3.17}
\]

The pole mass is the loss of common balanced Rees multiplicity, or
equivalently the Dirichlet energy of the normalized difference divisor.

---

## 4. Proximity and Rees-charge form

The energy can be written using only Rees excesses and the proximity Green
kernel.

Fix a common finite cluster carrying both complete ideals. For a point-basis
vector `r=(r_p)`, define its excess at `p` by

\[
(\mathsf P r)_p
:=r_p-\sum_{q\to p}r_q,                               \tag{4.1}
\]

where the sum is over points proximate to `p`. The upper-triangular matrix
`P` is the proximity matrix. Completeness/antinefness says

\[
\rho^f:=\mathsf P R\ge0,\qquad
\rho^g:=\mathsf P S\ge0.                              \tag{4.2}
\]

Positive entries are the Rees excesses; their supports are the Rees
valuations, with the usual allowance for a common refinement. Define the
signed normalized charge

\[
\delta:=\frac{\rho^f}{\alpha}-
         \frac{\rho^g}{\beta}                         \tag{4.3}
\]

and the proximity Green matrix

\[
\mathsf G:=(\mathsf P^{-1})^{\!T}\mathsf P^{-1}.      \tag{4.4}
\]

Since

\[
\frac{R}{\alpha}-\frac{S}{\beta}
=\mathsf P^{-1}\delta,                                \tag{4.5}
\]

equation (1.9) becomes

\[
\boxed{
\mathcal E_{\rm MR}
=\frac12\delta^T\mathsf G\delta.}                    \tag{4.6}
\]

This is the normalized multi-Rees **energy functional** in valuation-algebra
coordinates. It has the desired features:

- Rees normalization supplies the two nonnegative charge measures
  `rho^f,rho^g`;
- the canonical point IDs and proximity paths proved in WTC round 2 supply
  the Green kernel;
- repeated chart presentations disappear because charges live on valuations;
- contact splitting is retained rather than forced into one center; and
- divergence of the two flows appears as a signed charge, exactly where the
  Laurent example says it must.

Normality gives positivity of the two separate charges. It gives no smallness
of their **difference** in the Green norm. That is the remaining wall.

---

## 5. Attempt to recover KPC from the valuation algebra

### 5.1 The tempting argument and its precise failure

At a packet point use regular parameters

\[
E=(x=0),\qquad \mathfrak m=(x,r),                     \tag{5.1}
\]

and the rank-two flag valuation

\[
\widehat\nu(x)=(1,0),\qquad
\widehat\nu(r)=(0,1)                                 \tag{5.2}
\]

with lexicographic order. The packet boundary restrictions say

\[
A_f(0,r)=u_fr^{\alpha T},\qquad
A_g(0,r)=u_gr^{\beta T}.                              \tag{5.3}
\]

It is tempting to argue that integral closure extends these values from the
flag to the ordinary blowup valuation and hence gives KPC. This is invalid.
The flag regards every `(0,n)` as smaller than `(1,0)`, while the ordinary
valuation gives both `x` and `r` value one. There is no order-preserving
coarsening of the lexicographic flag that recovers ordinary order.

More concretely, take the monomial divisorial valuations

\[
v_s(r)=1,\qquad v_s(x)=s\quad(s\ge1).                 \tag{5.4}
\]

The flag is the limiting `s -> infinity` direction, while ordinary order is
`v_1`. A Rees support function may be constant at the packet value for all
large `s` and bend at a finite Rees slope before `s=1`. Normalization records
this convex/antinef envelope; it does not prohibit the bend.

### 5.2 Exact Laurent control on the normalized bi-Rees algebra

For Proposition 5.1 of `sol-wtc1-round2.md`, let

\[
I_f=(r^2+x,x^2),\qquad
I_g=(r^3+\tfrac32xr,x^3).                              \tag{5.5}
\]

The divisorial support functions along (5.4) are

\[
\begin{aligned}
v_s(I_f)&=\min(2,s),\\
v_s(I_g)&=\min(3,s+1).                                \tag{5.6}
\end{aligned}
\]

Thus

\[
\begin{array}{c|cc}
 &s\ge2&s=1\\ \hline
v_s(I_f)&2&1\\
v_s(I_g)&3&2.
\end{array}                                           \tag{5.7}
\]

The limiting flag sees exactly the packet powers `(2,3)`, whereas the first
ordinary blowup sees `(1,2)`.

The balanced local diagonal is

\[
I_\cap:=\overline{I_f^3+I_g^2}.                       \tag{5.8}
\]

Its valuation function is

\[
v_s(I_\cap)
=\min\bigl(3\min(2,s),\,2\min(3,s+1)\bigr).          \tag{5.9}
\]

It has value `6` for `s >= 2` but value `3` at `s=1`. Integral closure cannot
repair this: it preserves every divisorial ideal value, including `v_1`.
The normalized bi-Rees algebra therefore displays the KPC failure rather than
excluding it.

The same example has contact prefixes

\[
(1,1),\qquad(2,1),                                    \tag{5.10}
\]

which are permitted by the proximity inequalities on a free chain. KPC would
replace them by the extremal vectors `(2,0,...)` and `(3,0,...)`. Neither
antinefness nor nonnegative Rees excess forces that extremum.

This is not a counterexample to polynomial KPC: the pair is Laurent and is
not certified as a full eligible polynomial-origin packet. It is, however, a
counterexample to the implication

\[
\begin{gathered}
\text{normalized multi-Rees structure}+
\text{paired powers}+\text{denominator capacities}\\
+\text{local constant Jacobian}
\quad\Longrightarrow\quad\text{KPC}.                 \tag{5.11}
\end{gathered}
\]

### 5.3 Polynomial origin without Keller is still insufficient

There is also a global control separating polynomial origin from the Keller
condition. Choose generic polynomials of degrees `d,e` whose leading forms
have disjoint zero sets on the line at infinity. Then the two projective
pencil clusters are disjoint, the balanced ideal

\[
(F^\beta,G^\alpha,Z^N)                                \tag{5.12}
\]

has no base point, and a generic target fiber has `de` points. Hence

\[
\mathbf H_\cap=0,\qquad
\mathcal E_{\rm MR}=B^2,
\qquad \operatorname{td}=de.                         \tag{5.13}
\]

So polynomial origin, a common balanced denominator, complete ideals, and a
normal multi-Rees algebra allow the maximum possible energy. The constant
Jacobian and its global boundary consequences are indispensable.

### 5.4 KPC verdict

The multi-Rees construction can **compute** the ordinary point-basis vector
once the full two ideals are supplied. It cannot infer its first coefficient
from a packet's limiting flag value. Therefore:

> **CONJECTURE KPC remains CONJECTURE.** The normalized multi-Rees algebra
> neither proves nor is needed by KPC. A proof of KPC would still have to rule
> out finite-slope Rees breakpoints using the full eligible prefix or a new
> global Keller/canonical-divisor constraint.

For G5 this is acceptable: Theorems 2.1 and 3.1 replace KPC rather than use
it. The target becomes a bound on the entire balanced b-divisor.

---

## 6. Log surfaces and Zariski Main: the attempted bound

### 6.1 What the Jacobian supplies exactly

Let a common resolution make

\[
\Phi:X\longrightarrow\mathbf P^1\times\mathbf P^1   \tag{6.1}
\]

the two resolved pencil maps. Its fiber classes are `C_f,C_g`. The
ramification formula is

\[
K_X=\Phi^*K_{\mathbf P^1\times\mathbf P^1}+R_\Phi,
\qquad
R_\Phi=K_X+2C_f+2C_g\ge0.                             \tag{6.2}
\]

Because `J(f,g)` is a nonzero constant, `Phi` is etale on the affine plane;
all components of `R_Phi` not introduced by compactification are therefore
supported on the boundary.

The balanced map also has an exact affine ramification factor:

\[
d(f^\beta)\wedge d(g^\alpha)
=\alpha\beta f^{\beta-1}g^{\alpha-1}\,df\wedge dg.   \tag{6.3}
\]

Thus after subtracting the known power-map ramification on `f=0` and `g=0`,
the residual ramification of `Psi` is again a boundary divisor. This is the
right place for a log-surface proof to use the Keller hypothesis.

### 6.2 Why the standard log inequalities stop

The energy divisor can be written using the mobile classes as

\[
\Delta:=\frac{C_f}{\alpha}-\frac{C_g}{\beta}
=-\mathbf X+\mathbf Y,
\qquad
\Delta^2=-2\mathcal E_{\rm MR}.                       \tag{6.4}
\]

The obstruction is one of polarization:

- the ramification identity (6.2) is linear in the **sum** `C_f+C_g`;
- the desired bound is quadratic in the normalized **difference** `Delta`;
- `Delta` is neither effective nor nef, so effectivity of `R_Phi` gives no
  sign after pairing with it; and
- the Hodge index theorem gives only `Delta^2 <= 0`, namely
  `E_MR >= 0`, which was already known.

Pairing `R_Phi` with either nef fiber class gives ordinary nonnegative
ramification degrees. It does not give a lower bound `Delta^2 >= -2`.
Likewise, on a resolution of `Psi`,

\[
R_\Psi=K_X+3L_\Psi                                   \tag{6.5}
\]

is effective after the known affine ramification is included. Intersecting
with `L_Psi` contains the uncontrolled term `K_X . L_Psi`; the number and
depth of boundary blowups are not uniformly bounded. No upper bound on
`L_Psi^2=alpha beta td` follows.

At the proximity level, contraction/contact with the line at infinity gives
linear sums of point-basis multiplicities. Splitting such a sum along a long
chain decreases the square norm—the same wrong sign isolated in WTC round 2.
The log divisor records the discrepancies of the chain but no banked theorem
bounds the Green energy of the signed charge (4.3).

Zariski Main has the same stopping point. It canonically locates added
boundary over the target when the etale map is not finite, and those boundary
valuations can be included among the Rees valuations. It does not bound their
number, proximity depth, or signed Green energy. A statement that did so would
be new finiteness leverage, not a formal consequence of normalization.

### 6.3 The exact missing log input

A successful log-surface proof must convert the support statement

\[
\text{residual ramification is confined to the polynomial boundary} \tag{6.6}
\]

into a **polarized capacity bound** on the normalized Rees charge:

\[
\frac12\delta^T\mathsf G\delta\le1.                  \tag{6.7}
\]

No inequality in the four audited files, and no standard effectivity/Hodge
step used above, makes this conversion. Equation (6.7) must therefore remain
labelled **CONJECTURE**.

---

## 7. Minimal missing inequality and cofinality

### CONJECTURE G5-RBE — Keller balanced-Rees energy

For the balanced ideal `c` of every Sigray-normalized polynomial Keller pair,

\[
\boxed{
\mathcal E_{\rm MR}
=B^2-\left\|\frac{\mathbf Z(\mathfrak c)}{\alpha\beta}\right\|^2
\le1.}                                                \tag{G5-RBE}
\]

By the exact results above, the following are equivalent formulations of this
single conjecture:

\[
\begin{aligned}
-\mathbf H_\cap^2&\ge B^2-1,                         &&\tag{7.1}\\
e_\infty(\mathfrak c)&\ge N^2-(\alpha\beta)^2,       &&\tag{7.2}\\
e_\infty(\mathfrak a,\mathfrak b)
 &\ge\alpha\beta(B^2-1),                             &&\tag{7.3}\\
\frac12\delta^T\mathsf G\delta&\le1,               &&\tag{7.4}\\
\sum_{P\ {\mathrm{pole}}}\frac{a_Pb_P}{\nu_P}&\le1,   &&\tag{7.5}\\
\operatorname{td}&\le\alpha\beta.                  &&\tag{7.6}
\end{aligned}
\]

Formula (7.2) is perhaps the most concrete Rees target: the base cluster of
the special degree-`N` rational map

\[
[F^\beta:G^\alpha:Z^N]                                \tag{7.7}
\]

must consume all but `(alpha beta)^2` of its Noether square `N^2`. Formula
(7.4) is the cleanest proximity target: the normalized signed Rees charge has
Green energy at most one.

This is the minimal missing inequality for the rank-2 route. It is not KPC,
PFE, or PCC in disguise at the level of local data: none of those statements
is needed to define `c`, `H_cap`, or `delta`. It is, however, **equivalent to
the final td ceiling** by Theorem 3.1. Calling the balanced object canonical
does not make its unit bound formal.

### 7.1 Weak cofinal version

For an absolute constant `C`, define

> **CONJECTURE G5-RBE(C).** Every polynomial Keller pair satisfies
> \[
> \mathcal E_{\rm MR}\le C,
> \quad\text{equivalently}\quad
> e_\infty(\mathfrak c)\ge N^2-C(\alpha\beta)^2.      \tag{7.8}
> \]

Any finite `C` independent of `B` gives

\[
\operatorname{td}\le C\alpha\beta.                  \tag{7.9}
\]

Combined with the banked finite menu of Sigray/GGV types, this would give an
absolute finite `td` ceiling and make the book ladder cofinal. Thus the route
does not need the sharp constant one to win G5.

What follows unconditionally from the Rees/intersection structure is only

\[
0\le\langle\mathbf X,\mathbf Y\rangle\le B^2,
\qquad 0\le\mathcal E_{\rm MR}\le B^2.                \tag{7.10}
\]

The upper bound grows with `B`, and the polynomial non-Keller control in
§5.3 attains it. Neither normalized multi-Rees theory nor the audited log
formulas supply an absolute `C`.

---

## 8. Dependency and status ledger

| statement | status |
|---|---|
| packet flag, point ID, and proximity path | **PROVED** in WTC round 2 |
| packet boundary order transports to contact-chain sums | **PROVED** in WTC round 2 |
| normalized bi-Rees algebra and balanced ideal `c` | **EXACT**, §2 |
| `H_cap` is the valuationwise normalized meet | **EXACT**, Theorem 2.1 |
| balanced energy equals `td/(alpha beta)` | **EXACT**, Theorem 3.1 |
| energy equals half the normalized difference square | **EXACT**, Corollary 3.2 |
| energy equals the proximity Green norm | **EXACT**, §4 |
| energy equals `Sum ab/nu` | **EXACT**, using `TDBOUND.md` |
| multi-Rees normality forces packet ordinary multiplicities | **NO**, §5.2 |
| KPC for full polynomial-origin eligible packets | **CONJECTURE KPC** |
| log ramification is boundary-supported after known affine power ramification | **EXACT**, §6.1 |
| boundary ramification bounds the signed Rees Green energy | **CONJECTURE G5-RBE** |
| sharp `td <= alpha beta` | **CONJECTURE; equivalent to G5-RBE** |
| any absolute finite `td` ceiling from this route | **NOT REACHED** |

## 9. Strategic conclusion

The rank-2 connection succeeds as a change of proof object.

The two pencil ideals should not be asked to concentrate every packet at one
ordinary point. Their normalized bi-Rees algebra already contains the full
contact splitting, all Rees valuations, and the proximity form. The balanced
diagonal `(beta,alpha)` produces one canonical ideal `c`; its b-divisor is the
correct common part, and its missing self-intersection is exactly the Sigray
pole mass.

But the algebra is an accountant, not the inequality. It faithfully records
the finite-slope breakpoints that defeat KPC and admits energy as large as
`B^2` away from the Keller locus. The Keller condition contributes a boundary
ramification statement, while the needed conclusion is a uniform quadratic
capacity bound on a signed divisor. The unproved passage between those two
sentences is precisely **CONJECTURE G5-RBE**.

So the honest final verdict is:

\[
\boxed{
\text{canonical Rees energy: achieved;}\quad
\text{KPC from Rees algebra: no;}\quad
\text{finite td bound: not yet;}\quad
\text{minimal gap: G5-RBE(C), sharply }C=1.}
\]
