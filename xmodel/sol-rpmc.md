# RPMC at one root: the two-block thick-line degeneration and the polar-excess defect

**Date:** 2026-08-23
**Input status:** all statements in `xmodel/sol-kjn.md` are accepted as
**EXACT/PROVED**. Characteristic is zero. After a harmless residue-field
extension, the completed residue field is denoted by \(k\).

## 0. Verdict

**RPMC(C) is not proved here for any finite \(B\)-independent \(C\).** Two
parts of the proposed local program can nevertheless be made exact.

1. The degeneration of the thick-line gradient cokernel at a root is much
   more rigid than an arbitrary matrix factorization. If the root has
   multiplicity \(\mu\), put

   \[
   c=\alpha\mu-1.
   \]

   The cokernel is a free \(k[[u]]\)-module of rank \(M=d+e-2\). Multiplication
   by \(z\) has one Jordan block of length \(M\) over \(k((u))\), exactly two
   blocks of lengths \(r,M-r\) at \(u=0\), and Smith form

   \[
   \operatorname{diag}(1,\ldots,1,u^c,0)                 \tag{0.1}
   \]

   over \(k[[u]]\). Here

   \[
   1\le r\le d-1,\qquad M-r\ge e-1.                      \tag{0.2}
   \]

   Thus there is exactly one transverse elementary-divisor defect, of exact
   size \(\alpha\mu-1\). The higher \(z\)-filtration has a completely
   determined **number** of jumps at every level, but their positive
   \(u\)-exponents are not determined.

2. The point-basis square is exactly a local intersection defect. For
   general \(\lambda,\nu\), set

   \[
   n_P=i_P(F-\lambda Z^d,G-\nu Z^e),\qquad
   \Delta_P=\alpha\beta B\mu-n_P.                     \tag{0.3}
   \]

   Then

   \[
   \boxed{
   \mathcal E_P=\frac{\Delta_P}{\alpha\beta},\qquad
   \sum_{p\succ P}(\beta R_p-\alpha S_p)^2
       =2\alpha\beta\,\Delta_P.}                      \tag{0.4}
   \]

   In particular \(\Delta_P\) is a nonnegative integer. Hence a nonzero
   root energy has the stronger quantum

   \[
   \mathcal E_P\ge\frac1{\alpha\beta}.                \tag{0.5}
   \]

   On the normalization branches \(\gamma\) of a general \(F\)-fiber above
   \(P\), write \(m_\gamma=\operatorname{ord}_\gamma z\). The pure-minor
   identity gives the exact polar formula

   \[
   \boxed{
   \Delta_P=\sum_{\gamma\mid P}
     \max\{0,\operatorname{ord}_\gamma F_X
                  -(d-2)m_\gamma\}.}                 \tag{0.6}
   \]

   There is a symmetric formula on a general \(G\)-fiber. Formula (0.6) is
   the requested exact collective bridge from the gradient matrix to the
   point-basis discrepancies.

The unresolved inequality is now the following polar-capacity statement:

> **CONJECTURE PC(C).**
>
> \[
> \sum_{\gamma\mid P}
>   \max\{0,\operatorname{ord}_\gamma F_X-(d-2)m_\gamma\}
> \le C\alpha\beta\frac{\mu}{B}.                     \tag{0.7}
> \]

By (0.4)--(0.6), **PC(C) is equivalent to RPMC(C)**. The matrix-factorization
calculation proves the one-step defect \(c=\alpha\mu-1\) and the two-block
shape, but it does not prove (0.7): the split position \(r\), the higher
elementary-divisor exponents, and the polar orders along the fiber branches
remain uncontrolled. This is the single remaining step.

The Keller separation is exact. For the class-kill family the residual
Jacobian curve contributes an additional branch order \(de-d-1\) to the
right side of the general polar formula. The intrinsic polar excess is only
\(1\), while the actual defect is \(de-d\). Thus the step producing (0.6),
and also the freeness and nilpotence used in (0.1), fail exactly because
\(\operatorname{Fitt}_0\ne(Z^M)\).

---

## 1. Completed local gradient matrix

Move the root to \(P=[0:1:0]\), and use

\[
u=X/Y,\qquad z=Z/Y,\qquad R=k[[u,z]],\qquad O=k[[u]]. \tag{1.1}
\]

Write

\[
\Phi(u,z)=F(u,1,z),\qquad \Gamma(u,z)=G(u,1,z).      \tag{1.2}
\]

Euler's identity gives the local form of the homogeneous gradient matrix:

\[
\mathcal A=
\begin{pmatrix}
\Phi_u&\Gamma_u\\
d\Phi-u\Phi_u-z\Phi_z&e\Gamma-u\Gamma_u-z\Gamma_z
\end{pmatrix},
\qquad \det\mathcal A=jz^M.                         \tag{1.3}
\]

Let \(h(u)=H(u,1)\). Since \(P\) has multiplicity \(\mu\),

\[
h=u^\mu\varepsilon(u),\qquad \varepsilon(0)\ne0,    \tag{1.4}
\]

and on \(z=0\)

\[
\Phi=\xi h^\alpha,\qquad \Gamma=\eta h^\beta.       \tag{1.5}
\]

The two columns of \(\mathcal A\bmod z\) are proportional. Moreover

\[
(h_u,Bh-uh_u)=(u^{\mu-1})\subset O.                 \tag{1.6}
\]

Indeed \(h_u\) has exact order \(\mu-1\) in characteristic zero; (1.6)
also covers \(\mu=B\), when the second displayed generator can vanish.
It follows from (1.5) that

\[
I_1(\mathcal A\bmod z)=(u^{\alpha\mu-1}),           \tag{1.7}
\]

because \(\alpha<\beta\). This is the first place where the gradient and
the common leading powers enter quantitatively.

---

## 2. The exact elementary-divisor degeneration

Let

\[
Q=\operatorname{coker}(\mathcal A:R^2\to R^2),
\qquad T:Q\to Q,\quad T(q)=zq.                      \tag{2.1}
\]

### Theorem 2.1 -- the one-defect/two-block normal form (**PROVED**)

Put \(c=\alpha\mu-1\). Then:

1. \(Q\) is free of rank \(M\) over \(O\), and \(T^M=0\).
2. Over \(K=\operatorname{Frac}(O)\), \(T\) is one regular nilpotent block
   of length \(M\).
3. As an \(O\)-linear map on \(Q\simeq O^M\), \(T\) has Smith form

   \[
   \operatorname{SNF}_O(T)
   =\operatorname{diag}(1^{M-2},u^c,0).             \tag{2.2}
   \]

4. There is an integer \(r\), \(1\le r\le d-1\), such that

   \[
   Q/uQ\simeq k[[z]]/(z^r)\oplus
                    k[[z]]/(z^{M-r}).               \tag{2.3}
   \]

   Since \(d<e\), \(r<M/2\) and \(M-r\ge e-1\).

#### Proof

The adjugate factorization gives

\[
\operatorname{adj}(\mathcal A)\mathcal A
=\mathcal A\operatorname{adj}(\mathcal A)=jz^M I_2. \tag{2.4}
\]

Thus \(z^M Q=0\), so \(Q\) is finite over \(O\). Since
\(\det\mathcal A\ne0\), the presentation has projective dimension one.
Auslander--Buchsbaum gives \(\operatorname{depth}_R Q=1\). Its support is
exactly \(V(z)\); hence its only associated prime is \((z)\). Therefore
\(u\) is a nonzerodivisor on \(Q\), and the finite \(O\)-module \(Q\) is
free.

After inverting \(u\), (1.7) says that \(\mathcal A\bmod z\) has a unit
entry and rank one. Hence

\[
\operatorname{SNF}_{K[[z]]}(\mathcal A)
=\operatorname{diag}(1,z^M),                        \tag{2.5}
\]

so \(Q\otimes_OK\simeq K[[z]]/(z^M)\). This proves the rank and the
generic Jordan assertion.

Right exactness after reduction modulo \(z\), followed by (1.7), gives

\[
Q/zQ\simeq\operatorname{coker}(\mathcal A\bmod z)
       \simeq O\oplus O/(u^c).                      \tag{2.6}
\]

But \(Q/zQ=\operatorname{coker}T\). The structure theorem over the DVR
\(O\), together with \(\operatorname{rank}_K T=M-1\), proves (2.2).

Finally, every entry of \(\mathcal A(0,z)\) is divisible by \(z\), while
its determinant is \(jz^M\). Smith reduction over \(k[[z]]\) therefore
gives

\[
\operatorname{SNF}_{k[[z]]}(\mathcal A(0,z))
=\operatorname{diag}(z^r,z^{M-r})                  \tag{2.7}
\]

for \(1\le r\le M-r\). The first column consists of restrictions of
degree-\((d-1)\) homogeneous forms and is not identically zero. Some entry
in that column consequently has \(z\)-order at most \(d-1\), so the smaller
Smith exponent satisfies \(r\le d-1\). As \(d<e\), this also gives
\(M-r\ge e-1\). Equation (2.3) follows. \(\square\)

### 2.2 All higher jump counts (**PROVED**)

For \(1\le q\le M-1\), write

\[
C_q=Q/T^qQ.
\]

The generic rank of \(C_q\) over \(O\) is \(q\). From the two blocks in
(2.3),

\[
\dim_k(C_q/uC_q)=\min(q,r)+\min(q,M-r).              \tag{2.8}
\]

Consequently the \(O\)-module structure has the exact form

\[
C_q\simeq O^q\oplus
 \bigoplus_{a=1}^{\kappa_q}O/(u^{\ell_{q,a}}),
\qquad \ell_{q,a}\ge1,                              \tag{2.9}
\]

where

\[
\boxed{\kappa_q=\min(q,r,M-q).}                     \tag{2.10}
\]

At the first level, \(\kappa_1=1\) and

\[
\ell_{1,1}=c=\alpha\mu-1.                           \tag{2.11}
\]

Thus the number of elementary-divisor jumps at every \(z\)-level is fixed
by one integer \(r\), and the first jump size is fixed by \(\mu\). The
higher positive integers \(\ell_{q,a}\) are extension data; neither (1.3)
nor the argument above bounds the sums

\[
\tau_q:=\sum_a\ell_{q,a}.                           \tag{2.12}
\]

No assertion about the \(\tau_q\) is made here.

### 2.3 Why determinant plus integrability does not determine \(r\)

For arbitrary \(c\ge1\) and \(1\le r<M\), the formal matrix

\[
\mathcal A_{c,r}=
\begin{pmatrix}
X^c&Z^r\\
-Z^{M-r}&0
\end{pmatrix}                                      \tag{2.13}
\]

has determinant \(Z^M\), and both columns are gradients:

\[
F=\frac{X^{c+1}}{c+1}-YZ^{M-r},\qquad
G=XZ^r.                                             \tag{2.14}
\]

If \(c=M-r\), these are homogeneous of degrees \(M-r+1\) and \(r+1\).
Thus pure support and gradient integrability alone allow arbitrary block
positions. Example (2.14) does **not** have the campaign's two nonzero
leading powers \(H^\alpha,H^\beta\); it is not a counterexample to RPMC.
It proves that the common leading profile, not merely “matrix factorization
plus gradients,” must constrain the higher filtration.

The simultaneous two-dimensional equivalence class of \(\mathcal A\) is
not classified by \((c,r)\). Equations (2.2), (2.3), and (2.9) are the
proved normal-form data; a claim of a full diagonal form over \(R\) would
be false in general.

---

## 3. Exact conversion of point-basis energy to a local defect

Choose general \(\lambda,\nu\in k^\times\), and put

\[
A_\lambda=\Phi-\lambda z^d,\qquad
B_\nu=\Gamma-\nu z^e,\qquad
n_P=\ell_R R/(A_\lambda,B_\nu).                    \tag{3.1}
\]

The choices can be made so that the two germs have no common component and
their strict transforms do not meet on any exceptional component after the
simultaneous pencil resolution.

### Proposition 3.1 -- the local defect identity (**PROVED**)

One has

\[
\sum_{p\succ P}R_p^2=B\alpha^2\mu,\qquad
\sum_{p\succ P}S_p^2=B\beta^2\mu,\qquad
\sum_{p\succ P}R_pS_p=n_P.                          \tag{3.2}
\]

Hence, with

\[
\Delta_P=\alpha\beta B\mu-n_P,                     \tag{3.3}
\]

\[
\boxed{
\mathcal E_P=\frac{\Delta_P}{\alpha\beta},\qquad
\sum_{p\succ P}(\beta R_p-\alpha S_p)^2
 =2\alpha\beta\Delta_P.}                            \tag{3.4}
\]

#### Proof

Two different general members of the first pencil have local intersection

\[
i_P(\Phi-\lambda z^d,\Phi-\lambda' z^d)
=i_P(\Phi,z^d)
=d\,\operatorname{ord}_u\Phi(u,0)
=d\alpha\mu=B\alpha^2\mu.                          \tag{3.5}
\]

Noether's infinitely-near intersection formula gives the first square sum;
the second is identical. For a general pair \((\lambda,\nu)\), the image
of every exceptional curve under the two resolved pencils is at most
one-dimensional. A general point of the two-dimensional parameter space
avoids their finite union, so there is no residual intersection above \(P\).
Noether's formula then gives the mixed identity in (3.2).

Expanding the square in the definition of \(\mathcal E_P\) and using (3.2)
gives (3.4). Cauchy--Schwarz applied to the two point-basis vectors gives
\(n_P\le\alpha\beta B\mu\), so \(\Delta_P\in\mathbf Z_{\ge0}\). \(\square\)

### Corollary 3.2 -- the root quantum (**PROVED**)

If \(\mathcal E_P\ne0\), then

\[
\boxed{\mathcal E_P\ge\frac1{\alpha\beta}.}         \tag{3.6}
\]

Equivalently,

\[
2\alpha\beta\mid
\sum_{p\succ P}(\beta R_p-\alpha S_p)^2.            \tag{3.7}
\]

This is stronger than the single-center quantum in `sol-kjn.md` (6.9), but
it is still a lower, not an upper, bound. In particular, RPMC(C) would
force

\[
\Delta_P=0\quad\text{whenever}\quad
B>C\alpha\beta\mu.                                  \tag{3.8}
\]

Thus a finite root-weighted constant would make every sufficiently light
root have exactly proportional point-basis vectors in the square norm.
Summing (3.3) over the proper roots and using the accepted global
intersection identity also gives

\[
\boxed{\sum_P\Delta_P=\operatorname{td}.}           \tag{3.9}
\]

Thus the \(\Delta_P\) form an exact nonnegative integral allocation of the
topological degree among the boundary roots. The unconditional local bound
obtained here is only

\[
0\le\Delta_P\le\alpha\beta B\mu,\qquad
0\le\mathcal E_P\le B\mu.                           \tag{3.10}
\]

It has the wrong \(B\)-scale for RPMC.

---

## 4. Pure minor converts the defect to polar excess

Let \(\widetilde C_\lambda\) be the normalization of the germ
\(A_\lambda=0\). For a branch \(\gamma\) over \(P\), write

\[
m_\gamma=\operatorname{ord}_\gamma z,\qquad
q_\gamma=\operatorname{ord}_\gamma\Gamma.           \tag{4.1}
\]

Since \(i_P(A_\lambda,z)=\alpha\mu\), genericity of \(\nu\) gives

\[
n_P=\sum_{\gamma\mid P}\min(q_\gamma,e m_\gamma).   \tag{4.2}
\]

As \(e\alpha\mu=\alpha\beta B\mu\), (3.3) becomes

\[
\boxed{
\Delta_P=\sum_{\gamma\mid P}
\max(0,e m_\gamma-q_\gamma).}                       \tag{4.3}
\]

Thus \(\Delta_P\) is the total pole order of
\(g=\Gamma/z^e\) on the ends of a general \(f\)-fiber over \(P\).

### Proposition 4.1 -- the pure polar formula (**PROVED**)

Under \(F_XG_Y-F_YG_X=jZ^M\),

\[
\boxed{
\Delta_P=\sum_{\gamma\mid P}
\max\{0,\operatorname{ord}_\gamma\Phi_u
                 -(d-2)m_\gamma\}.}                \tag{4.4}
\]

Symmetrically, on the normalization branches \(\sigma\) of a general
\(G\)-fiber,

\[
\boxed{
\Delta_P=\sum_{\sigma\mid P}
\max\{0,\operatorname{ord}_\sigma\Gamma_u
                 -(e-2)\operatorname{ord}_\sigma z\}.} \tag{4.5}
\]

#### Proof

In the chart (1.1), direct expansion gives

\[
J_{u,z}(f,g)
=\det\frac{\partial(f,g)}{\partial(u,z)}
=-\frac{F_XG_Y-F_YG_X}{z^{d+e+1}}
=-jz^{-3}.                                         \tag{4.6}
\]

Let \(t\) be a parameter on \(\gamma\). Along \(f=\lambda\),

\[
\frac{dg}{dt}
=J_{u,z}(f,g)\frac{dz/dt}{f_u},\qquad
f_u=z^{-d}\Phi_u.                                  \tag{4.7}
\]

If \(g\) has pole order
\(\delta_\gamma=e m_\gamma-q_\gamma>0\), then
characteristic zero gives

\[
-\delta_\gamma-1
=-3m_\gamma+(m_\gamma-1)
 -\bigl(\operatorname{ord}_\gamma\Phi_u-dm_\gamma\bigr).
\tag{4.8}
\]

Therefore

\[
\delta_\gamma
=\operatorname{ord}_\gamma\Phi_u-(d-2)m_\gamma.    \tag{4.9}
\]

On a branch where \(g\) is finite, the positive part of the right side is
zero. Summing (4.9) and using (4.3) proves (4.4). Interchanging \(F,d\)
and \(G,e\) proves (4.5). \(\square\)

### 4.2 The exact residual-curve correction

For an arbitrary homogeneous pair put

\[
Q_0=F_XG_Y-F_YG_X.
\]

Then (4.6) reads

\[
J_{u,z}(f,g)=-Q_0z^{-(d+e+1)}.                     \tag{4.10}
\]

The same branch calculation shows that, on every pole branch,

\[
e m_\gamma-q_\gamma
=\operatorname{ord}_\gamma\Phi_u+e m_\gamma
 -\operatorname{ord}_\gamma Q_0                    \tag{4.11}
\]

or, since \(M=d+e-2\),

\[
e m_\gamma-q_\gamma
=\underbrace{\operatorname{ord}_\gamma\Phi_u
 -(d-2)m_\gamma}_{\text{intrinsic polar excess}}
 +\underbrace{M m_\gamma-\operatorname{ord}_\gamma Q_0}
              _{\text{residual-Jacobian correction}}. \tag{4.12}
\]

The pure-minor identity is used **exactly** to set the second bracket to
zero on every branch and after every blowup. This is the valuation form of
“the transformed determinant is a unit off the strict transform of \(z=0\).”
It removes the residual correction; it does not bound the first bracket.

### 4.3 Artin-algebra consequence (**PROVED, wrong direction**)

Let \(L_P=R/(A_\lambda,B_\nu)\), and let

\[
D=\det\frac{\partial(A_\lambda,B_\nu)}{\partial(u,z)}.
\]

An exact expansion gives

\[
Q_0+zD=e\Phi_uB_\nu-d\Gamma_uA_\lambda.             \tag{4.13}
\]

The class of \(D\) generates the socle of the zero-dimensional complete
intersection \(L_P\). Hence \(zD=0\) in \(L_P\). Under \(Q_0=jz^M\),

\[
z^M=0\quad\text{in }L_P.                            \tag{4.14}
\]

Also

\[
\dim_k L_P/zL_P=\alpha\mu.                          \tag{4.15}
\]

Thus (4.14) only yields

\[
n_P=\dim_kL_P\le M\alpha\mu.                        \tag{4.16}
\]

This is an upper bound on \(n_P\). RPMC needs the almost-maximal lower
bound

\[
\boxed{
n_P\ge\alpha\beta B\mu-C\alpha\beta\frac{\mu}{B}.}
\tag{4.17}
\]

Inequality (4.17) is **CONJECTURE PC(C)/RPMC(C)**. The Artin nilpotence
(4.14) has the wrong orientation and does not prove it.

---

## 5. What the elementary divisors do and do not control

The exact information can now be aligned:

\[
\begin{array}{c|c}
\text{thick-line module }Q&\text{generic pencil intersection }L_P\\ \hline
Q/zQ=O\oplus O/(u^{\alpha\mu-1})
 &L_P/zL_P\text{ has length }\alpha\mu\\
\text{generic }z\text{-block }(M)
 &z^M L_P=0\\
\text{special blocks }(r,M-r)
 &\Delta_P=\text{total pole/polar excess}.
\end{array}                                        \tag{5.1}
\]

The first row is the exact root-size datum. The second records the
pure-minor thickness. The third is where persistence lives. Equations
(2.9)--(2.12) show that the filtration contains jump data at as many as
\(M-1\) levels. Equations (4.3)--(4.4) show that the Green square measures
the polar excess carried by the actual fiber branches, not merely the
number of those module jumps.

In particular, the off-\(z\) unit condition performs one exact operation:
it deletes the residual correction in (4.12). A proof of RPMC must still
show that the remaining intrinsic polar excess satisfies

\[
\sum_{\gamma\mid P}
\max\{0,\operatorname{ord}_\gamma\Phi_u-(d-2)m_\gamma\}
\le C\alpha\beta\frac{\mu}{B}.                      \tag{5.2}
\]

Inequality (5.2) is **CONJECTURE PC(C)**. Neither the exact first defect
\(\alpha\mu-1\), the split bound \(r\le d-1\), nor the known determinant
and integrability equations imply (5.2) by an argument established here.

There is therefore no proved control of either the total discrepancy size
\(\Delta_P\) or its point-by-point persistence from (2.2) alone. The proved
progress is the complete first-step/two-block classification and the exact
conversion of the entire discrepancy square into the polar integer
\(\Delta_P\).

---

## 6. Critical sanity gate: the class-kill family

Take

\[
f=x^d+y,\qquad g=x^e+y^{e-1},\qquad d=B\alpha,\quad e=B\beta. \tag{6.1}
\]

At \(P=[0:1:0]\),

\[
\Phi=u^d+z^{d-1},\qquad \Gamma=u^e+z,               \tag{6.2}
\]

and

\[
Q_B=d(e-1)u^{d-1}z-eu^{e-1}z^{d-1}
=zu^{d-1}\bigl(d(e-1)-eu^{e-d}z^{d-2}\bigr).        \tag{6.3}
\]

The parenthesis is a unit in \(k[[u,z]]\). Hence the local Jacobian support
contains the residual curve \(u=0\) with multiplicity \(d-1\), and, for
the corresponding gradient cokernel \(\mathcal Q_B\),

\[
\operatorname{Fitt}_0(\mathcal Q_B)=(Q_B)\ne(z^M).  \tag{6.4}
\]

This breaks Theorem 2.1 at its first step: the cokernel is not annihilated
by \(z^M\), is not \(O\)-free of rank \(M\), and after inverting \(u\) its
determinant has \(z\)-order \(1\), not \(M\).

The failure of the polar step is equally explicit. A general first-pencil
germ has leading equation

\[
A_\lambda=u^d+z^{d-1}-\lambda z^d=0.                \tag{6.5}
\]

Its unique Newton branch has

\[
\operatorname{ord}_\gamma z=d,\qquad
\operatorname{ord}_\gamma u=d-1.                   \tag{6.6}
\]

Therefore

\[
\operatorname{ord}_\gamma\Phi_u=(d-1)^2,\qquad
\operatorname{ord}_\gamma Q_B=d^2-d+1.             \tag{6.7}
\]

The intrinsic polar excess appearing in the Keller formula would be only

\[
(d-1)^2-d(d-2)=1.                                  \tag{6.8}
\]

But the residual-Jacobian correction in (4.12) is

\[
Md-(d^2-d+1)=de-d-1.                               \tag{6.9}
\]

Thus the actual pole/intersection defect is

\[
\Delta_P=1+(de-d-1)=de-d=d(e-1).                   \tag{6.10}
\]

Equivalently \(n_P=d\), and (3.4) gives

\[
\mathcal E_P
=\frac{de-d}{\alpha\beta}
=B^2-\frac B\beta,                                  \tag{6.11}
\]

exactly the accepted control value.

This is the required sanity failure. If one incorrectly discards the
second bracket in (4.12) without using \(Q_0=jz^M\), the control would be
assigned defect \(1\) instead of \(de-d\). The missing amount is exactly
the valuation of its extra Jacobian curve.

---

## 7. Status and the remaining lemma

| Statement | Tier |
|---|---|
| \(Q\) is \(O\)-free of rank \(M\), with generic block \((M)\) | **PROVED; pure minor used** |
| unique first transverse defect \(u^{\alpha\mu-1}\) | **PROVED; leading gradient powers used** |
| special \(z\)-blocks are exactly \((r,M-r)\), \(1\le r\le d-1\) | **PROVED** |
| number of jumps of \(Q/T^qQ\) is \(\min(q,r,M-q)\) | **PROVED** |
| higher jump exponents \(\ell_{q,a}\) have a \(B\)-independent bound | **NOT PROVED** |
| \(\mathcal E_P=\Delta_P/(\alpha\beta)\), \(\Delta_P\in\mathbf Z_{\ge0}\) | **PROVED** |
| \(\Delta_P\) equals total pole order on a generic fiber | **PROVED** |
| \(\Delta_P\) equals the positive polar excess (4.4) | **PROVED; pure minor used exactly** |
| \(\Delta_P\le C\alpha\beta\mu/B\) | **CONJECTURE PC(C), equivalent to RPMC(C)** |
| any finite \(B\)-independent \(C\) | **NOT OBTAINED** |

The single remaining step is not “show that the determinant has no residual
curve”; that has already been used exactly in passing from (4.12) to (4.4).
It is:

\[
\boxed{
\text{bound the intrinsic polar excess of the generic fiber at }P
\text{ by }C\alpha\beta\mu/B.}                      \tag{7.1}
\]

Equivalently, one must turn the higher filtered extension data in
(2.9) into the almost-maximal local intersection lower bound (4.17). The
first Smith defect and the two-block special fiber do not yet perform that
conversion.

Thus the honest endpoint is

\[
\boxed{
\textbf{TIER: DECISIVE PARTIAL. RPMC remains open; its local square is now
an integer polar-excess defect, and the thick-line degeneration is
classified through all jump counts but not their exponents.}}
\]
