# PC at one boundary root: adjunction, the Smith telescope, and the missing retention inequality

**Date:** 2026-08-23
**Characteristic:** \(0\).
**Accepted input:** xmodel/sol-rpmc.md in full and
xmodel/sol-kjn.md, Sections 5--7.  In particular, every statement quoted
from those files below is **EXACT/PROVED**.

## 0. Verdict

**PC(C) is not proved here for any finite \(B\)-independent \(C\).**  Thus
there is no G5 headline.

There are, however, three exact conclusions.

1. On the normalization \(\overline C_\lambda\) of a general \(F\)-fiber,
   the differential

   \[
   \omega=\frac{dy}{f_x}=-\frac{dx}{f_y}=\frac{dg}{j}
   \tag{0.1}
   \]

   is canonical and has no zero or pole on the affine fiber.  If

   \[
   a_\gamma=\operatorname{ord}_\gamma F_X-(d-2)m_\gamma,
   \tag{0.2}
   \]

   then

   \[
   \boxed{a_\gamma=-\operatorname{ord}_\gamma\omega-1.}
   \tag{0.3}
   \]

   Pole ends of \(g\) contribute \(a_\gamma=\delta_\gamma>0\), while
   finite ends contribute \(a_\gamma=-\kappa_\gamma<0\).  If \(g_C\) is
   the geometric genus, \(s\) is the number of ends, and
   \(K_\infty=\sum_{\gamma:\,g(\gamma)\ne\infty}\kappa_\gamma\), adjunction
   gives the exact **signed** identity

   \[
   \boxed{\Delta_\infty-K_\infty=2-2g_C-s.}
   \tag{0.4}
   \]

   It does not cap a local positive part.  The uncontrolled compensator is
   \(K_\infty\), the total local degree at finite boundary ends.

2. The higher Smith exponents from sol-rpmc.md do telescope internally.
   Put \(K_i=\ker T^i\).  There are nonnegative integers
   \(a_2,\ldots,a_M\) such that

   \[
   \sum_{i=2}^M a_i=c=\alpha\mu-1
   \tag{0.5}
   \]

   and, for \(1\le q\le M-1\),

   \[
   \boxed{
   \tau_q:=\sum_{a=1}^{\kappa_q}\ell_{q,a}
    =\sum_{i=q+1}^{M}\ \sum_{j=i-q+1}^{i}a_j
    \le \min(q,M-q)(\alpha\mu-1).}
   \tag{0.6}
   \]

   Thus every higher \(z\)-filtration torsion length is bounded by the
   first Smith defect.  No proved identity carries these \(\tau_q\) to the
   polar integer \(\Delta_P\).

3. Semicontinuity has the wrong orientation.  It gives

   \[
   n_P(\lambda,\nu)\le i_P(\Phi,\Gamma)
   \tag{0.7}
   \]

   when the special intersection is isolated.  PC requires a lower bound
   for \(n_P(\lambda,\nu)\).  Moreover \(H^\alpha,H^\beta\) are the
   restrictions to \(z=0\), not in general the two-variable tangent cones
   in \(k[[u,z]]\).  Coprimality does not control the missing \(z\)-jets.

The single missing statement is most sharply named as follows.

> **CONJECTURE DIR(C) -- displaced-intersection retention.**  With
> \(c=\alpha\mu-1\), for general \(\lambda,\nu\),
>
> \[
> \boxed{
> n_P=i_P(\Phi-\lambda z^d,\Gamma-\nu z^e)
> \ge e(c+1)\left(1-\frac{C}{B^2}\right).}
> \tag{DIR(C)}
> \]

Since \(e(c+1)=\alpha\beta B\mu\), DIR(C) is exactly PC(C), not an
additional assumption hidden in a proof.  Equivalently,

\[
B\Delta_P\le C\beta(c+1).
\tag{0.8}
\]

The factor \(B^{-1}\) in PC is therefore a \(B^{-2}\) **relative**
intersection-retention assertion.  None of adjunction, the two-block
shape, the Smith telescope, or upper semicontinuity proves it.

---

## 1. Accepted local identities

Move the root to \(P=[0:1:0]\), and use

\[
u=X/Y,\qquad z=Z/Y,\qquad R=k[[u,z]],\qquad O=k[[u]].
\tag{1.1}
\]

Write

\[
\Phi=F(u,1,z),\qquad \Gamma=G(u,1,z),\qquad
A_\lambda=\Phi-\lambda z^d,\qquad
B_\nu=\Gamma-\nu z^e.
\tag{1.2}
\]

At \(z=0\),

\[
\Phi=\xi h^\alpha,\qquad \Gamma=\eta h^\beta,
\qquad \operatorname{ord}_u h=\mu.
\tag{1.3}
\]

Set

\[
M=d+e-2,\qquad c=\alpha\mu-1,
\qquad W_P=\alpha\beta B\mu=e\alpha\mu=e(c+1).
\tag{1.4}
\]

For general \(\lambda,\nu\), the accepted intersection-defect identity is

\[
n_P=i_P(A_\lambda,B_\nu),\qquad
\Delta_P=W_P-n_P\in\mathbf Z_{\ge0},
\qquad \mathcal E_P=\frac{\Delta_P}{\alpha\beta}.
\tag{1.5}
\]

On a normalization branch \(\gamma\) of \(A_\lambda=0\), put

\[
m_\gamma=\operatorname{ord}_\gamma z,\qquad
q_\gamma=\operatorname{ord}_\gamma\Gamma.
\tag{1.6}
\]

The accepted pole and pure-polar formulas are

\[
\Delta_P=\sum_{\gamma\mid P}(em_\gamma-q_\gamma)_+
=\sum_{\gamma\mid P}
 \bigl(\operatorname{ord}_\gamma\Phi_u-(d-2)m_\gamma\bigr)_+.
\tag{1.7}
\]

Finally, for the thick-line gradient cokernel \(Q\) and multiplication
\(T=z\), the accepted facts are

\[
Q\simeq O^M,\qquad T^M=0,
\tag{1.8}
\]

generic Jordan type \((M)\), special type \((r,M-r)\), and

\[
1\le r\le d-1,\qquad M-r\ge e-1,
\tag{1.9}
\]

\[
Q/T^qQ\simeq O^q\oplus
 \bigoplus_{a=1}^{\kappa_q}O/(u^{\ell_{q,a}}),
\qquad
\kappa_q=\min(q,r,M-q),
\tag{1.10}
\]

with \(\ell_{1,1}=c\).

---

## 2. Adjunction and the exact signed polar ledger

Let \(\overline C_\lambda\) be the normalization of the projective curve
\(F-\lambda Z^d=0\).  The general affine fiber is smooth because
\(df\ne0\), a consequence of \(J(f,g)=j\ne0\).
It is irreducible by the characteristic-zero Bertini--Krull composite
criterion: generic reducibility would give \(f=p(h)\) with
\(\deg p>1\), and a root of \(p'\) would force \(df=0\) somewhere on
\(h=\text{constant}\).
For the global sum one may choose the boundary coordinate \(Y\) nonzero at
all finitely many roots of \(H\); otherwise the calculation is made in one
such chart at a time.  The notation \(g_C\) below refers to the genus of
the connected general fiber.

### Proposition 2.1 -- local canonical order (**PROVED**)

For every boundary branch \(\gamma\),

\[
\operatorname{ord}_\gamma\Phi_u-(d-2)m_\gamma
=-\operatorname{ord}_\gamma\omega-1,
\qquad
\omega=\frac{dy}{f_x}=\frac{dg}{j}.
\tag{2.1}
\]

#### Proof

On \(f=\lambda\),

\[
df=f_x\,dx+f_y\,dy=0,
\tag{2.2}
\]

so

\[
dg=g_x\,dx+g_y\,dy
=\frac{f_xg_y-f_yg_x}{f_x}\,dy
=j\frac{dy}{f_x}.
\tag{2.3}
\]

The residue differential \(dy/f_x=-dx/f_y\) is regular and nonvanishing
on the smooth affine fiber.  It pulls back to a meromorphic canonical
differential on \(\overline C_\lambda\).

In the chart (1.1), \(y=1/z\).  If \(t\) is a uniformizer on \(\gamma\),
then characteristic zero gives

\[
\operatorname{ord}_\gamma(dy)=-m_\gamma-1.
\tag{2.4}
\]

Homogeneity gives

\[
\Phi_u=F_X(u,1,z)=z^{d-1}f_x(u/z,1/z),
\tag{2.5}
\]

and hence

\[
\begin{aligned}
\operatorname{ord}_\gamma\omega
&=-m_\gamma-1
 -\bigl(\operatorname{ord}_\gamma\Phi_u-(d-1)m_\gamma\bigr)\\
&=(d-2)m_\gamma-\operatorname{ord}_\gamma\Phi_u-1.
\end{aligned}
\tag{2.6}
\]

This is (2.1). \(\square\)

### Proposition 2.2 -- pole/finite-end dichotomy (**PROVED**)

Put

\[
a_\gamma=\operatorname{ord}_\gamma\Phi_u-(d-2)m_\gamma.
\tag{2.7}
\]

Exactly one of the following holds.

1. If \(g\) has pole order \(\delta_\gamma>0\), then

   \[
   a_\gamma=\delta_\gamma.
   \tag{2.8}
   \]

2. If \(g\) has finite value \(b_\gamma\), put

   \[
   \kappa_\gamma=\operatorname{ord}_\gamma(g-b_\gamma)\ge1.
   \tag{2.9}
   \]

   Then

   \[
   a_\gamma=-\kappa_\gamma.
   \tag{2.10}
   \]

#### Proof

At a pole, \(\operatorname{ord}_\gamma dg=-\delta_\gamma-1\).  At a finite
end, \(\operatorname{ord}_\gamma dg=\kappa_\gamma-1\).  Apply (2.1) and
\(dg=j\omega\). \(\square\)

Thus the positive polar part is precisely the pole divisor of \(g\), while
the negative polar part is the local-degree divisor at finite ends.

### Proposition 2.3 -- adjunction/Riemann--Hurwitz ledger (**PROVED**)

Let

\[
\Pi=\{\gamma:g(\gamma)=\infty\},\qquad
\Lambda=\{\gamma:g(\gamma)\ne\infty\},
\tag{2.11}
\]

\[
\Delta_\infty=\sum_{\gamma\in\Pi}\delta_\gamma,
\qquad
K_\infty=\sum_{\gamma\in\Lambda}\kappa_\gamma,
\qquad
s=|\Pi|+|\Lambda|.
\tag{2.12}
\]

Then

\[
\boxed{
2g_C-2=K_\infty-\Delta_\infty-s,
\qquad
\Delta_\infty=K_\infty+2-2g_C-s.}
\tag{2.13}
\]

In particular,

\[
\Delta_\infty\le K_\infty+1.
\tag{2.14}
\]

#### Proof

The divisor of the nonzero rational differential \(\omega\) has degree
\(2g_C-2\).  It has no affine support.  Propositions 2.1--2.2 give

\[
\begin{aligned}
2g_C-2
&=\sum_{\gamma\in\Pi}(-\delta_\gamma-1)
 +\sum_{\gamma\in\Lambda}(\kappa_\gamma-1)\\
&=K_\infty-\Delta_\infty-s.
\end{aligned}
\tag{2.15}
\]

Since \(g_C\ge0\) and \(s\ge1\), (2.14) follows.  Equivalently, apply
Riemann--Hurwitz to \(g:\overline C_\lambda\to\mathbf P^1\): it is
unramified on the affine fiber, a pole of order \(\delta\) contributes
\(\delta-1\), and a finite end of local degree \(\kappa\) contributes
\(\kappa-1\). \(\square\)

For each proper root \(P\), define

\[
K_P=\sum_{\substack{\gamma\mid P\\g(\gamma)\ne\infty}}
\kappa_\gamma.
\tag{2.16}
\]

Then the exact local signed ledger is

\[
\sum_{\gamma\mid P}a_\gamma=\Delta_P-K_P,
\tag{2.17}
\]

and summing over roots yields (2.13).  Adjunction constrains only that
sum.  It supplies no pointwise upper bound for either \(\Delta_P\) or
\(K_P\).  Positive polar order at one root may be compensated by a high
finite local degree at the same or another root.

### 2.4 Classical polar class gives the same signed information

The projective polar \(F_X=0\) has degree \(d-1\), so

\[
\sum_{\gamma\text{ at }\infty}
 \operatorname{ord}_\gamma F_X
 +R_y^{\mathrm{aff}}=d(d-1),
\tag{2.18}
\]

where \(R_y^{\mathrm{aff}}\) is the affine ramification degree of the
projection \(y\) on the general fiber.  Also

\[
\sum_{\gamma\text{ at }\infty}m_\gamma=d.
\tag{2.19}
\]

Consequently

\[
\sum_{\gamma\text{ at }\infty}a_\gamma
=d-R_y^{\mathrm{aff}}=2-2g_C-s.
\tag{2.20}
\]

This is again (2.13), after (2.17) is summed.  A genus bound controls the
signed sum, not its positive variation.  Therefore neither adjunction nor
the ordinary polar-class formula produces the factor \(\mu/B\).
Indeed the plane bound
\(g_C\le(d-1)(d-2)/2\) improves no positive-part estimate.  Rootwise,
(4.5) below gives the exact boundary weight

\[
\sum_{\gamma\mid P}(d-2)m_\gamma=(d-2)\alpha\mu,
\tag{2.21}
\]

but (2.17) becomes

\[
\sum_{\gamma\mid P}\operatorname{ord}_\gamma F_X
 -(d-2)\alpha\mu=\Delta_P-K_P.
\tag{2.22}
\]

Thus the known \(\mu\)-supported intersection with \(L_\infty\) still
controls only a signed difference.  The missing \(B^{-1}\) cannot be
extracted without a rootwise control of both that signed contribution and
\(K_P\), or an equivalent direct control of the positive variation.

---

## 3. The higher Smith exponents really do telescope

This section strengthens the filtration ledger in sol-rpmc.md.  It is
pure \(O\)-linear algebra after the Keller-specific freeness and nilpotence
(1.8) have been established.

### Theorem 3.1 -- kernel-flag telescope (**PROVED**)

Let \(O\) be a DVR, let \(Q\) be free of rank \(M\), and let
\(T^M=0\) have one regular nilpotent block over \(\operatorname{Frac}(O)\).
Suppose the torsion part of \(\operatorname{coker}T\) has length \(c\).
For

\[
K_i=\ker T^i,\qquad 0\le i\le M,
\tag{3.1}
\]

there are integers \(a_i\ge0\), \(2\le i\le M\), with

\[
c=\sum_{i=2}^M a_i.
\tag{3.2}
\]

If \(\tau_q\) is the torsion length of \(Q/T^qQ\), then

\[
\boxed{
\tau_q=\sum_{i=q+1}^{M}\sum_{j=i-q+1}^{i}a_j
=\sum_{j=2}^{M}w_{q,j}a_j,}
\tag{3.3}
\]

where

\[
w_{q,j}
=\#\{i:\ q+1\le i\le M,\ i-q+1\le j\le i\}.
\tag{3.4}
\]

Hence

\[
\boxed{\tau_q\le\min(q,M-q)c.}
\tag{3.5}
\]

Moreover,

\[
\boxed{
\sum_{q=1}^{M-1}\tau_q
=\sum_{j=2}^{M}(j-1)(M-j+1)a_j
\le\left\lfloor\frac{M^2}{4}\right\rfloor c.}
\tag{3.6}
\]

#### Proof

Each \(K_i\) is saturated in \(Q\), because \(Q/K_i\) is isomorphic to
\(\operatorname{im}T^i\subset Q\) and is torsion-free.  Similarly,
\(K_i/K_{i-1}\) is free of rank one: \(T^{i-1}\) embeds it into \(K_1\).

The map \(T\) induces an injection of rank-one free modules

\[
\theta_i:K_i/K_{i-1}\longrightarrow K_{i-1}/K_{i-2}.
\tag{3.7}
\]

After choices of generators, \(\theta_i\) is multiplication by a unit times
\(u^{a_i}\), for a unique \(a_i\ge0\).

The injection

\[
\overline T:Q/K_1\longrightarrow K_{M-1}
\tag{3.8}
\]

has cokernel equal to the torsion part of \(\operatorname{coker}T\).  With
the saturated kernel flags on source and target, its associated graded maps
are \(\theta_2,\ldots,\theta_M\).  Taking determinants proves (3.2).

Likewise,

\[
\overline {T^q}:Q/K_q\longrightarrow K_{M-q}
\tag{3.9}
\]

has cokernel equal to the torsion part of \(Q/T^qQ\).  On the graded line
indexed by \(i\), \(q+1\le i\le M\), its map is

\[
\theta_{i-q+1}\circ\cdots\circ\theta_i,
\tag{3.10}
\]

whose determinant valuation is
\(\sum_{j=i-q+1}^{i}a_j\).  Summing over the graded lines proves (3.3).

There are \(M-q\) intervals in (3.3), each containing \(q\) consecutive
indices.  Therefore

\[
0\le w_{q,j}\le\min(q,M-q),
\tag{3.11}
\]

and (3.2) gives (3.5).  Finally, as \(q\) varies, the number of intervals
of consecutive edges in \(\{2,\ldots,M\}\) that contain \(j\) is
\((j-1)(M-j+1)\).  Its maximum is
\(\lfloor M^2/4\rfloor\), proving (3.6). \(\square\)

### Corollary 3.2 -- application to the two-block module (**PROVED**)

For the accepted thick-line cokernel at \(P\),

\[
\boxed{
\kappa_q=\min(q,r,M-q),\qquad
\kappa_q\le\tau_q
\le\min(q,M-q)(\alpha\mu-1).}
\tag{3.12}
\]

The left inequality holds because \(\tau_q\) is the sum of
\(\kappa_q\) positive exponents.  In particular every individual exponent
satisfies

\[
1\le\ell_{q,a}\le\min(q,M-q)(\alpha\mu-1).
\tag{3.13}
\]

This is an exact bound on all higher extension exponents.  It is not
\(B\)-independent when \(q\) grows with \(M=d+e-2\), and even (3.6) has
quadratic \(M\)-scale.

Most importantly, the accepted results contain no equality or inequality
of the form

\[
\Delta_P\ \mathrel{?}\ \mathscr F(\tau_1,\ldots,\tau_{M-1}).
\tag{3.14}
\]

The \(\tau_q\) measure saturation defects of images of powers of \(z\) in
the gradient cokernel \(Q\).  The number \(n_P\) is the length of the
different complete intersection \(R/(A_\lambda,B_\nu)\).  Nilpotence only
gives \(z^M=0\) in this latter algebra and hence the wrong-way upper bound
\(n_P\le M\alpha\mu\).  The Smith telescope does not reverse it.

Thus the proposed statement that the higher Smith exponents telescope
**to the polar excess** is **CONJECTURE**, not a consequence of the
two-block normal form.  The telescope (3.3) is proved; the transfer
(3.14) is absent.

---

## 4. Displaced intersections and semicontinuity

### 4.1 Exact scale of the required retention

By (1.4)--(1.5),

\[
n_P=e(c+1)-\Delta_P.
\tag{4.1}
\]

PC(C) is therefore equivalent to

\[
n_P\ge e(c+1)-\frac{C\beta(c+1)}{B}
=e(c+1)\left(1-\frac{C}{B^2}\right).
\tag{4.2}
\]

This is DIR(C).  The leading boundary powers determine the maximal
Cauchy--Schwarz value \(e(c+1)\), but the desired error is only a
\(C/B^2\) fraction of that value.

Because \(\Delta_P\) is an integer, any finite PC(C) would force

\[
\Delta_P=0\qquad\text{if}\qquad B>C\alpha\beta\mu.
\tag{4.3}
\]

In particular a fixed \(C\) forces exact proportionality over every
sufficiently light root.  A bound merely polynomial or linear in \(\mu\)
cannot supply (4.3).

### 4.2 One-sided displacement ledger (**PROVED**)

Fix a general \(\lambda\).  Assume \(i_P(A_\lambda,\Gamma)<\infty\), and put

\[
n_P^0=i_P(A_\lambda,\Gamma)=\sum_{\gamma\mid P}q_\gamma.
\tag{4.4}
\]

Since

\[
\sum_{\gamma\mid P}m_\gamma=i_P(A_\lambda,z)=\alpha\mu,
\tag{4.5}
\]

one has

\[
W_P=\sum_{\gamma\mid P}em_\gamma.
\tag{4.6}
\]

Define the opposite displacement excess

\[
D_P^+=\sum_{\gamma\mid P}(q_\gamma-em_\gamma)_+.
\tag{4.7}
\]

Then

\[
\boxed{
n_P=n_P^0-D_P^+,
\qquad
n_P^0-W_P=D_P^+-\Delta_P.}
\tag{4.8}
\]

#### Proof

Genericity of \(\nu\) gives, branch by branch,

\[
n_P=\sum_{\gamma\mid P}\min(q_\gamma,em_\gamma).
\tag{4.9}
\]

Subtract (4.9) from (4.4) to obtain the first equality.  Subtract (4.6)
from (4.4) and separate the positive and negative parts of
\(q_\gamma-em_\gamma\) to obtain the second. \(\square\)

Upper semicontinuity in \(\nu\) sees \(D_P^+=n_P^0-n_P\).  PC concerns the
disjoint opposite part

\[
\Delta_P=\sum_{\gamma\mid P}(em_\gamma-q_\gamma)_+.
\tag{4.10}
\]

Thus even the exact drop under one displacement controls the wrong side of
the signed branch ledger.

### 4.3 Full specialization also has the wrong direction

If \((\Phi,\Gamma)\) is \((u,z)\)-primary, upper semicontinuity of local
intersection multiplicity gives

\[
i_P(A_\lambda,B_\nu)\le i_P(\Phi,\Gamma)
\tag{4.11}
\]

for general \(\lambda,\nu\).  If \(\Phi,\Gamma\) have a common local
component, the right side is infinite and gives no information.  In neither
case does specialization provide the lower bound (4.2).

There is also a basic local-language obstruction.  Equation (1.3) fixes
the restrictions of \(\Phi,\Gamma\) to \(z=0\).  It does not say that
\(\xi h^\alpha,\eta h^\beta\) are their lowest total-degree forms in
\(k[[u,z]]\).  Terms involving \(z\) can occur at lower total order.  Hence
the phrase “common tangent cone” cannot be used without an additional
theorem derived from the pure-minor equations.

Finally, \((\alpha,\beta)=1\) proves the common-power factorization and the
integer discrepancy quantum.  It places no direct restriction on the
\(z\)-coefficients of \(\Phi,\Gamma\), on the branchwise comparison
\(q_\gamma\) versus \(em_\gamma\), or on the size of \(D_P^+\) and
\(\Delta_P\).

---

## 5. The single missing inequality

The three proposed routes now meet at one exact point:

\[
\boxed{
\textbf{DIR(C):}\quad
i_P(\Phi-\lambda z^d,\Gamma-\nu z^e)
\ge\alpha\beta B\mu-C\alpha\beta\frac{\mu}{B}.}
\tag{5.1}
\]

Equivalently,

\[
\boxed{
\sum_{\gamma\mid P}
 \bigl(\operatorname{ord}_\gamma\Phi_u-(d-2)m_\gamma\bigr)_+
\le C\alpha\beta\frac{\mu}{B}.}
\tag{5.2}
\]

The equivalence is **PROVED** by the accepted identities (1.5)--(1.7).
The inequality itself is **CONJECTURE DIR(C) = CONJECTURE PC(C)**.

What has been bounded, and what remains, is exact:

| Quantity/source | Result | Tier |
|---|---:|---|
| residual-Jacobian correction \(Mm_\gamma-\operatorname{ord}_\gamma Q_0\) | \(0\) on every Keller branch | **PROVED; pure Fitting ideal used** |
| signed canonical contribution \(\Delta_\infty-K_\infty\) | \(2-2g_C-s\le1\) | **PROVED** |
| finite-end compensator \(K_\infty\) | no root-weighted bound | **OPEN** |
| first Smith torsion | \(\tau_1=\alpha\mu-1\) | **PROVED** |
| every higher Smith torsion | \(\tau_q\le\min(q,M-q)(\alpha\mu-1)\) | **PROVED** |
| transfer from \(\{\tau_q\}\) to \(\Delta_P\) or \(n_P\) | none | **OPEN** |
| special-to-general intersection change | upper semicontinuous | **PROVED; wrong direction** |
| \(B^{-2}\) displaced-intersection retention (5.1) | no finite \(C\) obtained | **CONJECTURE DIR(C)** |

The only actual positive-polar source left after the Keller residual term is
removed is the intrinsic pole divisor of the exact differential \(dg/j\).
Adjunction balances it against finite boundary local degrees; it does not
bound it root by root.  The Smith telescope controls a different module
until a polar/complete-intersection transfer theorem is proved.

---

## 6. Critical sanity gate: the class-kill control

Take

\[
f=x^d+y,\qquad g=x^e+y^{e-1},\qquad
d=B\alpha,\quad e=B\beta.
\tag{6.1}
\]

There is one root with \(\mu=B\).  In the boundary chart,

\[
\Phi=u^d+z^{d-1},\qquad \Gamma=u^e+z.
\tag{6.2}
\]

A general \(F\)-fiber branch has

\[
m_\gamma=d,\qquad \operatorname{ord}_\gamma u=d-1,
\qquad q_\gamma=d.
\tag{6.3}
\]

Therefore the actual pole/intersection defect is

\[
\Delta_P=ed-d=d(e-1)
=\alpha\beta B^2-\alpha B
=\alpha\beta\left(B^2-\frac B\beta\right).
\tag{6.4}
\]

Thus the actual defect violates the proposed root-weighted bound for every
finite \(B\)-independent \(C\), whose right side at \(\mu=B\) is only
\(C\alpha\beta\).  The control is not Keller, so the issue is precisely
which Keller-only equality fails.

The intrinsic polar term, however, is

\[
\operatorname{ord}_\gamma\Phi_u-(d-2)m_\gamma
=(d-1)^2-d(d-2)=1.
\tag{6.5}
\]

For a general pair, the exact non-Keller branch identity is

\[
em_\gamma-q_\gamma
=\underbrace{\operatorname{ord}_\gamma\Phi_u-(d-2)m_\gamma}_{1}
 +\underbrace{Mm_\gamma-\operatorname{ord}_\gamma Q_0}
 _{de-d-1}.
\tag{6.6}
\]

Indeed

\[
Q_0=F_XG_Y-F_YG_X
=zu^{d-1}
 \bigl(d(e-1)-eu^{e-d}z^{d-2}\bigr),
\tag{6.7}
\]

so

\[
\operatorname{Fitt}_0(\mathcal Q_B)=(Q_0)\ne(z^M).
\tag{6.8}
\]

This pinpoints both failures.

1. **Polar failure.**  The passage from actual pole order to intrinsic
   polar order uses

   \[
   Q_0=jz^M
   \quad\Longrightarrow\quad
   \operatorname{ord}_\gamma Q_0=Mm_\gamma.
   \tag{6.9}
   \]

   It deletes the second bracket in (6.6).  For the control that bracket is
   exactly \(de-d-1\).  Its canonical differential has intrinsic excess
   \(1\), while \(dg=J(f,g)\omega\) has the additional residual pole order.

2. **Smith failure.**  The proof of Theorem 3.1 in the campaign applies to
   this gradient module only after

   \[
   \operatorname{Fitt}_0(Q)=(z^M)
   \Longrightarrow z^MQ=0,\quad Q\simeq O^M.
   \tag{6.10}
   \]

   For the control, \(Q\) has the residual support \(u=0\); after inverting
   \(u\), its determinant has \(z\)-order \(1\), not \(M\).  Thus
   \(K_M=Q\), the rank-\(M\) kernel flag, and the telescope (3.3) are not
   available.

The adjunction calculation itself does not falsely kill the control.  On
the rational general fiber, there is one end and the intrinsic identity is

\[
1=2-2(0)-1.
\tag{6.11}
\]

Only the invalid replacement of the actual defect (6.4) by the intrinsic
term (6.5) would lose the residual amount.  That replacement is exactly
where the pure Fitting ideal is indispensable.

---

## 7. Final tier

Theorem 3.1 closes the purely linear-algebraic question left open about the
sums of the higher Smith exponents: they are controlled by the single
first defect through the kernel-flag telescope.  Proposition 2.3 closes the
adjunction calculation: it yields a signed pole-versus-finite-end ledger,
not a local positive-part cap.  Proposition 4.2 isolates why
semicontinuity measures the opposite displacement excess.

No proved result connects these exact controls strongly enough to yield
the \(B^{-2}\) relative retention in DIR(C).  Therefore

\[
\boxed{
\textbf{TIER: DECISIVE PARTIAL.  PC(C)=RPMC(C) remains open for every
finite \(B\)-independent \(C\).  The single missing inequality is DIR(C),
equation (5.1).}}
\]

If DIR(C) is proved for any finite \(B\)-independent \(C\), the accepted
chain gives RPMC(C), Theorem 7.1 gives KJN(C), and the campaign's TDBOUND
theorem follows.
