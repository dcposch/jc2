# KJN after the pure-boundary identity: resolved coefficients, the thick-line cokernel, and a one-root capacity lemma

**Date:** 2026-08-23  
**Input status:** `xmodel/sol-rooftop.md` was read in full.  I use its
identities (4.1)--(4.2) and the rooftop/Green identities as **EXACT**; the
independent confirmation in `xmodel/grok-rooftop-review.md` is accepted.
`TDBOUND.md` is used only at its stated tier.  Characteristic is zero.

## 0. Verdict

**KJN(C) is not proved here, for any finite \(B\)-independent \(C\).**  The
pure-boundary identity does, however, give two more exact structures than the
support statement recorded in the rooftop note:

1. On a resolution of the balanced base ideal, every exceptional ordinary
   ramification coefficient has an exact valuation--discrepancy formula,
   including a useful slack normal form; see (2.4) and (2.8).
2. The \(2\times2\) gradient cokernel of \(F,G\) is a matrix factorization
   supported scheme-theoretically on the single thick line
   \((d+e-2)L_\infty\); see (5.3)--(5.5).  Thus there is no residual Jacobian
   curve at a boundary breakpoint.  This is precisely what fails for the
   class-kill family.

The first structure does **not** yield a boundary budget.  Its effectivity
inequality bounds a base multiplicity in the wrong direction, and the
coefficient of the pulled-back \(Z\)-divisor is not consumed as blowups are
performed.  The second structure is the genuinely Keller-specific object
left to exploit.

I reduce KJN to the following strictly local sufficient statement.

> **CONJECTURE RPMC(C) (root-weighted pure-minor capacity).**  If
> \(F_d=\xi H^\alpha\), \(G_e=\eta H^\beta\), and a root \(P\) of \(H\) on
> \(L_\infty\) has multiplicity \(\mu_P\), then the complete point cluster
> over \(P\) satisfies
> 
> \[
> \mathcal E_P
> :=\frac12\sum_{p\succ P}
> \left(\frac{R_p}{\alpha}-\frac{S_p}{\beta}\right)^2
> \le C\frac{\mu_P}{B}.                              \tag{RPMC(C)}
> \]
> 
> The hypothesis includes the integrable pure-minor relation
> \(F_XG_Y-F_YG_X=jZ^{d+e-2}\), not just common leading powers.

This is not KJN rewritten: RPMC is a one-proper-root theorem in a completed
local surface, and it prescribes how the global unit budget is divided among
the roots.  It is stronger than KJN and no converse is asserted.  Since

\[
\sum_{P:H(P)=0}\mu_P=B,                              \tag{0.1}
\]

RPMC(C) sums exactly to \(\mathcal E_{\rm MR}\le C\), hence to
\(\deg\Psi\le C(\alpha\beta)^2\).  Thus RPMC(1) gives the sharp result, and
any finite RPMC(C) gives the cofinal result required by `TDBOUND.md`.

The single missing mathematical step is now local and explicit:

\[
\boxed{
\text{convert the absence of an off-}Z\text{ residual Jacobian curve into
the root-weighted square estimate RPMC(C).}}
\tag{0.2}
\]

Sections 2--5 explain why the ordinary discrepancy and log-effectivity
inequalities do not already make this conversion.

---

## 1. Set-up and conventions

Put

\[
d=B\alpha,\qquad e=B\beta,\qquad
N=B\alpha\beta=\beta d=\alpha e,                    \tag{1.1}
\]

where \(2\le\alpha<\beta\) and \((\alpha,\beta)=1\).  Let

\[
A=F^\beta,\qquad B_0=G^\alpha,\qquad C_0=Z^N,
\qquad \Psi=[A:B_0:C_0].                             \tag{1.2}
\]

The accepted identities are

\[
Q:=F_XG_Y-F_YG_X=jZ^M,qquad M=d+e-2,                \tag{1.3}
\]

and

\[
J_\Psi=cF^{\beta-1}G^{\alpha-1}Z^s,qquad
s=N+d+e-3=N+M-1.                                    \tag{1.4}
\]

Let

\[
\pi:X\longrightarrow\mathbf P^2                    \tag{1.5}
\]

be a sequence of point blowups resolving the three-generated ideal
\((F^\beta,G^\alpha,Z^N)\), so that the moving system defines a morphism
\(\varphi:X\to\mathbf P^2\).  For an exceptional prime \(E\), write

\[
p_E=v_E(F),\quad q_E=v_E(G),\quad z_E=v_E(Z),        \tag{1.6}
\]

\[
m_E=\min\{\beta p_E,\alpha q_E,Nz_E\},              \tag{1.7}
\]

and use the discrepancy convention

\[
K_X=\pi^*K_{\mathbf P^2}+\sum_E k_EE.               \tag{1.8}
\]

The fixed exceptional divisor of the pulled-back net is
\(\mathcal M=\sum_E m_EE\), and the moving line class is

\[
L=\pi^*(NH)-\mathcal M.                              \tag{1.9}
\]

All valuation formulas below remain true after further blowups.  Statements
about a minimal cluster use the minimal simultaneous principalization.

---

## 2. Pushing (1.4) through the base resolution

### 2.1 The cubic loss under removal of the fixed divisor (**EXACT**)

For three local sections \(s_0,s_1,s_2\) of one line bundle on a surface,
their Jacobian/Wronskian section can be written locally as

\[
W(s_0,s_1,s_2)
=s_0\,ds_1\wedge ds_2-s_1\,ds_0\wedge ds_2
 +s_2\,ds_0\wedge ds_1.                             \tag{2.1}
\]

If \(s_i=h\,t_i\) for all \(i\), direct expansion gives

\[
W(ht_0,ht_1,ht_2)=h^3W(t_0,t_1,t_2);                \tag{2.2}
\]

all terms containing \(dh\) cancel.  Pullback of the canonical factor adds
\(K_{X/\mathbf P^2}\).  Therefore the ramification divisor of the resolved
map is exactly

\[
\boxed{
R_\varphi
=\pi^*\operatorname{div}(J_\Psi)
 +K_{X/\mathbf P^2}-3\mathcal M.}                   \tag{2.3}
\]

This is the precise resolution form of (1.4).

### 2.2 Exceptional coefficients (**EXACT**)

Substituting (1.4) into (2.3), the coefficient of \(E\) is

\[
\boxed{
r_E=(\beta-1)p_E+(\alpha-1)q_E+s z_E+k_E-3m_E.}     \tag{2.4}
\]

Because \(\varphi\) is a morphism between smooth surfaces,
\(R_\varphi\) is effective.  Hence

\[
(\beta-1)p_E+(\alpha-1)q_E+s z_E+k_E\ge3m_E.        \tag{2.5}
\]

Inequality (2.5) is **PROVED**, not conjectural: it is just \(r_E\ge0\)
applied to (2.4).

### 2.3 Slack normal form (**EXACT**)

Define the three nonnegative coordinate slacks

\[
a_E=\beta p_E-m_E,\qquad
b_E=\alpha q_E-m_E,\qquad
c_E=Nz_E-m_E.                                      \tag{2.6}
\]

At least one of \(a_E,b_E,c_E\) is zero.  Since

\[
\frac{s}{N}=1+\frac1\alpha+\frac1\beta-\frac3N,    \tag{2.7}
\]

substitution of
\(p_E=(m_E+a_E)/\beta\),
\(q_E=(m_E+b_E)/\alpha\), and
\(z_E=(m_E+c_E)/N\) into (2.4) gives

\[
\boxed{
\begin{aligned}
r_E={}&k_E-\frac{3m_E}{N}
 +\left(1-\frac1\beta\right)a_E
 +\left(1-\frac1\alpha\right)b_E\\
&+\left(1+\frac1\alpha+\frac1\beta-\frac3N\right)c_E.
\end{aligned}}                                      \tag{2.8}
\]

The cancellation leaving \(-3m_E/N\) is the numerical shadow of the
log-Calabi--Yau cancellation in the rooftop note.  Effectivity gives the
proved inequality

\[
\boxed{
\frac{3m_E}{N}\le k_E
 +\left(1-\frac1\beta\right)a_E
 +\left(1-\frac1\alpha\right)b_E
 +\left(1+\frac1\alpha+\frac1\beta-\frac3N\right)c_E.}
\tag{2.9}
\]

For \(2\le\alpha<\beta\), every displayed slack coefficient is positive.

### 2.4 Why (2.9) does not give the Noether-square lower bound

KJN requires

\[
\sum_E m_E^2\ge N^2-C(\alpha\beta)^2,               \tag{2.10}
\]

which is **CONJECTURE KJN(C)** in base-multiplicity form, not a proved new
inequality.  Formula (2.9) is an upper bound on each \(m_E\) in terms of
discrepancy and coordinate slacks.  It supplies no lower bound on the sum of
their squares.  Moreover \(k_E\) grows along a long blowup chain, so (2.9)
becomes weaker, rather than stronger, with depth.

Thus (2.4) is the requested exact push-through of (4.2), but effectivity of
its coefficients does not perform the conversion to rooftop (2.14).

---

## 3. The \(Z\)-exponent is not a consumable blowup budget

The tempting counting argument in attack (A) treats the exponent
\(s=N+d+e-3\) as if one unit were spent at every boundary blowup.  Total
transform arithmetic shows that this is false.

Blow up a point of \(Z=0\), and then repeatedly blow up a free point on the
newest exceptional component, away from the strict transform of \(Z=0\).
If \(E_n\) is the \(n\)-th exceptional prime, then

\[
v_{E_n}(Z)=1,qquad k_{E_n}=n.                       \tag{3.1}
\]

Consequently the coefficient of \(E_n\) in the total transform of \(sZ\)
is

\[
s\,v_{E_n}(Z)=s                                      \tag{3.2}
\]

for every \(n\).  It does not decrease from \(s\) to \(s-1,s-2,\ldots\).
At a satellite blowup, \(v_E(Z)\) can instead increase.  Equations
(3.1)--(3.2) are exact pullback arithmetic.

This observation by itself uses nonminimal extra blowups, so it is not a
counterexample to a theorem specifically about the *minimal* balanced base
resolution.  It does prove that no depth bound follows from the coefficient
of the total transform alone.  Minimal ideals also exhibit depth growing
with their exponent: resolving the local pencil ideal

\[
(u,z^m)                                               \tag{3.3}
\]

replaces it successively by
\((u_1,z^{m-1}),(u_2,z^{m-2}),\ldots\), and requires a chain whose length
grows with \(m\).  Here the relevant exponents \(N\) and \(s\) themselves
grow linearly with \(B\).

Therefore a \(B\)-independent depth theorem would have to use the
integrability and pure-minor structure of \(F,G\), not the numerical degree
of the \(Z\)-factor.  Such a theorem would be new Keller leverage and would
feed directly into RPMC.

---

## 4. The resolved logarithmic determinant

### 4.1 Exact coefficient of the log cokernel

On the affine chart \(Z=1\), put

\[
\omega=d\log f\wedge d\log g
=j\frac{dx\wedge dy}{fg}.                            \tag{4.1}
\]

Further resolve, if necessary, until the union of the boundary and the zero
divisors of \(f\) and \(g\) is simple normal crossing.  Along an exceptional
prime \(E\),

\[
v_E(dx\wedge dy)=k_E-3z_E,                           \tag{4.2}
\]

while

\[
v_E(f)=p_E-dz_E,\qquad v_E(g)=q_E-ez_E.              \tag{4.3}
\]

As a logarithmic two-form, one adds one copy of \(E\).  Thus the coefficient
of the determinant of the logarithmic differential map is

\[
\boxed{
\lambda_E=k_E+1-p_E-q_E+(d+e-3)z_E.}                \tag{4.4}
\]

The pullback of a logarithmic form is logarithmic, so its divisor as a
section of the log-canonical bundle is effective.  Therefore

\[
\boxed{p_E+q_E\le k_E+1+(d+e-3)z_E}                 \tag{4.5}
\]

is **PROVED** from (4.1)--(4.4).

There is also an exact comparison with the ordinary ramification formula.
The coefficients of the three pullbacks of the coordinate lines along \(E\)
are \(a_E,b_E,c_E\), so

\[
\boxed{\lambda_E=r_E+1-a_E-b_E-c_E.}                \tag{4.6}
\]

Substitution of (2.4) and (2.6) into (4.6) recovers (4.4) exactly.

### 4.2 What the log inequality sees, and what it misses

Let the signed pole orders be

\[
u_E=dz_E-p_E,\qquad v_E'=ez_E-q_E.                  \tag{4.7}
\]

Then (4.5) is the proved sum inequality

\[
u_E+v_E'\ge3z_E-k_E-1.                              \tag{4.8}
\]

The rooftop energy, by contrast, measures the square of a normalized
**difference** after the proximity transform.  When both functions have a
pole along \(E\), the corresponding valuation-coordinate difference is

\[
\frac{v_E'}{\beta}-\frac{u_E}{\alpha}.              \tag{4.9}
\]

A lower bound on the unnormalized sum (4.8) gives no upper bound on the
square of (4.9).  This is the exact sum-versus-difference failure of the
immediate log argument.

In particular, a refined BMY argument must use more than effectivity of the
divisor \(\sum\lambda_EE\).  It must control the zero-dimensional or filtered
part of the log differential cokernel that records how long the leading
logarithmic determinant continues to cancel.  Section 5 gives a concrete
gradient-cokernel precursor that retains the pure determinant before
resolution; it is not asserted to be the resolved log cokernel itself.

---

## 5. The thick-line gradient cokernel

### 5.1 A Keller-specific matrix factorization (**EXACT**)

Consider the homogeneous gradient matrix

\[
\mathcal A=
\begin{pmatrix}
F_X&G_X\\
F_Y&G_Y
\end{pmatrix}:
\mathcal O_{\mathbf P^2}(1-d)\oplus
\mathcal O_{\mathbf P^2}(1-e)\longrightarrow
\mathcal O_{\mathbf P^2}^{\oplus2}.                 \tag{5.1}
\]

Its determinant is \(jZ^M\).  Hence it is injective as a sheaf map, and

\[
0\longrightarrow
\mathcal O(1-d)\oplus\mathcal O(1-e)
\xrightarrow{\mathcal A}\mathcal O^{\oplus2}
\longrightarrow\mathcal Q\longrightarrow0           \tag{5.2}
\]

is exact.  Its zeroth Fitting ideal is

\[
\boxed{\operatorname{Fitt}_0(\mathcal Q)=(Z^M).}     \tag{5.3}
\]

Equivalently, \(\mathcal A\) and \(j^{-1}\operatorname{adj}(\mathcal A)\)
form a matrix factorization of \(Z^M\).  Thus \(\mathcal Q\) is supported
scheme-theoretically on the \(M\)-fold thickening of \(L_\infty\), with no
additional Jacobian curve.

After blowing up a boundary point, (5.3) has a particularly concrete local
meaning.  Once the monomial exceptional factors are removed, the transform
of \(\det\mathcal A\)

- is a power of the local equation of the strict transform of \(Z=0\) at a
  point lying on that transform; and
- is a unit at every point away from that strict transform.

This off-\(Z\) unit statement is the strongest exact Keller input found in
this audit.  Valuation effectivity in (2.9) and (4.5) forgets it.

### 5.2 Numerical size of the cokernel (**EXACT**)

Put \(a=d-1\), \(b=e-1\), so \(M=a+b\).  From (5.2), for \(t\gg0\),

\[
\begin{aligned}
\chi(\mathcal Q(t))
&=2\binom{t+2}{2}
 -\binom{t-a+2}{2}-\binom{t-b+2}{2}\\
&=Mt+\frac{3M-a^2-b^2}{2}.                           \tag{5.4}
\end{aligned}
\]

In the original degrees this is

\[
\boxed{
\chi(\mathcal Q(t))
=(d+e-2)t+
\frac{3(d+e-2)-(d-1)^2-(e-1)^2}{2}.}                \tag{5.5}
\]

The constant term has quadratic \(B\)-scale.  Therefore the support
statement (5.3), the determinant, and the ordinary Chern data of
\(\mathcal Q\) do not by themselves contain a \(B\)-independent numerical
ceiling.  A successful log-cokernel proof must exploit the **filtered local
distribution** of this thick-line module together with the fact that its two
columns are gradients.  Arbitrary sheaves on \(ML_\infty\) are too flexible.

This local filtered problem is narrower than applying log-BMY to the whole
open surface and is the natural algebraic route to RPMC.

---

## 6. Exact decomposition by proper boundary roots

### 6.1 Common leading power (**EXACT**)

Restrict (1.3) to \(Z=0\).  The binary forms \(F_d=F(X,Y,0)\) and
\(G_e=G(X,Y,0)\) have zero Jacobian.  On \(Y\ne0\), write

\[
F_d=Y^d\phi(X/Y),\qquad G_e=Y^e\psi(X/Y).            \tag{6.1}
\]

The binary Jacobian equation becomes

\[
e\phi'\psi-d\phi\psi'=0,                            \tag{6.2}
\]

so \(\phi^e/\psi^d\) is constant.  Since
\(d=B\alpha,e=B\beta\) and \((\alpha,\beta)=1\), unique
factorization gives, after absorbing nonzero constants,

\[
\boxed{F_d=\xi H^\alpha,\qquad G_e=\eta H^\beta}     \tag{6.3}
\]

for a homogeneous binary form \(H\) of degree \(B\).  Over the algebraic
closure write

\[
\operatorname{div}_{L_\infty}(H)=\sum_i\mu_iP_i,
\qquad \sum_i\mu_i=B.                               \tag{6.4}
\]

The proper base points of the balanced net lie among the \(P_i\).

### 6.2 Orthogonal local energy split (**EXACT**)

Let \(R_p,S_p\) be the point-basis multiplicities of
\((F,Z^d)\) and \((G,Z^e)\) on a common cluster.  The rooftop identity gives

\[
\mathcal E_{\rm MR}
=\frac12\sum_p
\left(\frac{R_p}{\alpha}-\frac{S_p}{\beta}\right)^2
=\frac12\delta^T\mathsf G\delta.                   \tag{6.5}
\]

Every infinitely near point belongs to the cluster over one proper point
\(P_i\).  Define

\[
\mathcal E_i
=\frac12\sum_{p\succ P_i}
\left(\frac{R_p}{\alpha}-\frac{S_p}{\beta}\right)^2.\tag{6.6}
\]

Because the total-transform point basis is orthogonal, there are no
cross-terms between proper roots:

\[
\boxed{\mathcal E_{\rm MR}=\sum_i\mathcal E_i.}      \tag{6.7}
\]

This is the exact localization needed for a one-root lemma.  Notice also
the coprime arithmetic

\[
\frac{R_p}{\alpha}-\frac{S_p}{\beta}
=\frac{\beta R_p-\alpha S_p}{\alpha\beta}.          \tag{6.8}
\]

If the difference is nonzero, its numerator is a nonzero integer.  This
gives a **proved lower quantum**, not an upper bound:

\[
\frac12
\left(\frac{R_p}{\alpha}-\frac{S_p}{\beta}\right)^2
\ge\frac{1}{2(\alpha\beta)^2}.                       \tag{6.9}
\]

Thus coprimality alone makes persistent divergence costly; it does not bound
the number of divergence points or their amplitude.  The pure-minor unit
condition must supply that missing control.

---

## 7. The strictly local missing lemma and its consequence

### CONJECTURE RPMC(C) -- root-weighted pure-minor capacity

Fix one root \(P_i\) in (6.4), complete the surface at \(P_i\), and take the
minimal simultaneous principalization of the two pencil ideals and the
balanced ideal above that point.  Assume the germs come from homogeneous,
integrable \(F,G\) satisfying the pure-minor identity (1.3).  Then

\[
\boxed{
\mathcal E_i
\le C\frac{\mu_i}{B}.}                              \tag{7.1}
\]

Inequality (7.1) is **CONJECTURE RPMC(C)**.  The sharp proposal is \(C=1\).
No claim in this file proves it.

RPMC is strictly more local than KJN:

- its input is one completed boundary germ and its infinitely-near cluster;
- it mentions neither dominance, topological degree, nor the other roots;
- its Keller datum is the off-(Z) unit transform of the integrable matrix
  factorization (5.1)--(5.3); and
- it specifies a root budget \(\mu_i/B\), so it is a sufficient strengthening,
  not an equivalent reformulation of the global answer.

### Theorem 7.1 -- RPMC(C) implies KJN(C) (**PROVED conditional reduction**)

Assume RPMC(C) at every proper root.  Summing (7.1) and using (6.4) and
(6.7) gives

\[
\mathcal E_{\rm MR}
=\sum_i\mathcal E_i
\le\frac{C}{B}\sum_i\mu_i=C.                        \tag{7.2}
\]

The rooftop degree identity then gives

\[
\boxed{
\deg\Psi=(\alpha\beta)^2\mathcal E_{\rm MR}
\le C(\alpha\beta)^2.}                              \tag{7.3}
\]

Thus RPMC(1) proves sharp KJN(1), while any finite \(C\) independent of \(B\)
proves the cofinal form.

### What a proof of RPMC must actually show

The calculation above reduces the work to one missing statement, but does
not hide its difficulty.  A proof must control both:

1. the size of each integer discrepancy
   \(\beta R_p-\alpha S_p\); and
2. how long a nonzero discrepancy can persist along a free or satellite
   proximity chain.

Equations (2.9) and (4.5) control neither.  The additional available datum is
that, after exceptional monomials are removed, the transformed determinant
of the gradient matrix is a unit at every center off the strict transform of
\(Z=0\).  One concrete proof program is therefore:

- classify or estimate the two-generated graded matrix factorizations of
  \(Z^M\) that satisfy the gradient integrability equations
  \((F_X)_Y=(F_Y)_X\), \((G_X)_Y=(G_Y)_X\);
- relate their \(Z\)-adic elementary-divisor jumps at \(P_i\) to the point
  multiplicity discrepancies in (6.6); and
- prove that the resulting square sum is at most the normalized root length
  \(\mu_i/B\), or at most \(C\mu_i/B\) for some absolute finite \(C\).

The third bullet is precisely RPMC(C).  The first two identify information
discarded by ordinary ramification effectivity and by Chern classes.

---

## 8. Exact separation from the non-Keller class-kill family

Take the confirmed control

\[
f_B=x^d+y,\qquad g_B=x^e+y^{e-1},qquad
d=B\alpha, e=B\beta.                               \tag{8.1}
\]

Its homogenizations are

\[
F=X^d+YZ^{d-1},\qquad G=X^e+Y^{e-1}Z.               \tag{8.2}
\]

The leading common power is exactly the target one:

\[
F_d=(X^B)^\alpha,\qquad G_e=(X^B)^\beta.            \tag{8.3}
\]

Thus \(H=X^B\) has a single root \(P=[0:1:0]\) of multiplicity
\(\mu_P=B\).  Coprimality and the entire leading-power input of attack (C)
are present.

But direct differentiation gives

\[
\boxed{
Q_B
=d(e-1)X^{d-1}Y^{e-2}Z
 -eX^{e-1}Z^{d-1}.}                                 \tag{8.4}
\]

This is not \(jZ^{d+e-2}\).  Accordingly,
\(\operatorname{Fitt}_0(\mathcal Q_B)=(Q_B)\) has an extra Jacobian curve,
and the off-\(Z\) unit-transform statement in Section 5 fails.

The failure can be seen numerically at the first boundary valuation.  In the
chart \(Y=1\), write \(u=X/Y,z=Z/Y\).  At the ordinary blowup valuation
\(v(u)=v(z)=1\),

\[
p=d-1,\qquad q=1,\qquad z_E=1,\qquad k_E=1.          \tag{8.5}
\]

If one retained only the bare Keller log expression (4.4), its value would
be

\[
k_E+1-p-q+(d+e-3)z_E=e-1.                           \tag{8.6}
\]

On the other hand, (8.4) has

\[
v_E(Q_B)=d,qquad
v_E(Q_B)-(d+e-2)v_E(Z)=2-e.                          \tag{8.7}
\]

The actual logarithmic determinant coefficient is therefore

\[
(e-1)+(2-e)=1.                                      \tag{8.8}
\]

All arithmetic in (8.5)--(8.8) is exact.  Two conclusions follow.

1. Mere nonnegativity of the bare expression (4.4) would not exclude this
family: (8.6) is positive.  Hence log-effectivity alone cannot be the
   Keller step.
2. The exact pure support of the determinant is the separating datum.  The
   class-kill family carries the correction (8.7), produced by its extra
   Jacobian curve; a Keller pair has correction identically zero because
   \(Q=jZ^{d+e-2}\).

Finally, the confirmed degree computation gives

\[
\mathcal E_P=\mathcal E_{\rm MR}
=B^2-\frac B\beta.                                  \tag{8.9}
\]

For this one-root family, RPMC(C) would demand
\(\mathcal E_P\le C\mu_P/B=C\).  Equation (8.9) violates every fixed \(C\)
as \(B\) grows, exactly as required of a discriminating lemma.  There is no
contradiction because the pure-minor/matrix-factorization hypothesis fails
at (8.4).

This pinpoints the Keller-only step more sharply than “the family is not
Keller”: the proof must use the vanishing of the **residual Jacobian curve
in the transformed gradient cokernel**.  Common powers, coprimality, and
log-effectivity all survive too much of the control family.

---

## 9. Status ledger

| Statement | Status |
|---|---|
| pure-boundary identities (1.3)--(1.4) | **EXACT; accepted dual-confirmed input** |
| resolved ramification formula (2.3)--(2.4) | **EXACT** |
| slack normal form (2.8) | **EXACT** |
| exceptional effectivity inequality (2.9) | **PROVED; wrong direction for the Noether square** |
| the (Z)-exponent is consumed one unit per blowup | **FALSE as total-transform arithmetic; (3.1)--(3.2)** |
| log coefficient (4.4) and sum inequality (4.5) | **EXACT / PROVED; controls a sum, not the Green difference** |
| gradient cokernel is supported on \(ML_\infty\) | **EXACT, (5.3)** |
| its ordinary Chern/Hilbert data give a constant capacity bound | **NO; (5.5) has quadratic \(B\)-scale** |
| common leading form and root weights | **EXACT, (6.3)--(6.4)** |
| energy splits by proper roots | **EXACT, (6.7)** |
| coprimality bounds Green energy | **NO; it only gives the lower quantum (6.9)** |
| root-weighted pure-minor capacity RPMC(C) | **CONJECTURE; single localized missing statement** |
| RPMC(C) implies KJN(C) | **PROVED, Theorem 7.1** |
| finite \(B\)-independent \(C\) | **NOT OBTAINED** |

## 10. Final conclusion

Attack (A) yields an exact formula but not a budget: the resolved
ramification coefficient is (2.8), its effectivity has the wrong orientation,
and the (Z)-multiplicity persists under blowup rather than being spent.
Attack (B) identifies the sharper object: the integrable gradient cokernel is
a matrix factorization of \(Z^{d+e-2}\), supported on a single thick boundary
line.  Its determinant and Chern data still scale with \(B\), so a refined
argument must use its local filtration, not just BMY or effectivity.  Attack
(C) supplies only a discrepancy quantum; the class-kill computation shows
that coprimality and common powers do not control its number or depth.

The honest endpoint is therefore

\[
\boxed{
\textbf{OBSTRUCTED, but reduced to CONJECTURE RPMC(C): a one-root,
pure-minor, filtered-cokernel capacity lemma.}}
\]

Any proof of RPMC(C) with finite \(C\) independent of \(B\) proves KJN(C),
makes `TDBOUND.md` a theorem at the stated campaign tier, and renders the
sheet-number ladder cofinal.  No such (C) is proved in this file.
