# HC4 KILL-PROBE: first quintic GL4 layer and 5→4 Schur descent

**Date:** 2026-08-23  
**Charge:** execute the cheap discriminator in
[hc4-adjudication.md](hc4-adjudication.md), §7, and
[APPROACHES.md](../APPROACHES.md), row 10. All representation calculations
below were run in stock Python 3 with exact integers and
fractions.Fraction; no floating point or CAS plethysm table was used.

## Verdict

**NO LEVERAGE on the \(y\)-linear/JC2 sector at the first quintic layer.**

The first layer below the top Hessian equation is the multiplicity-one
\(\mathrm{GL}_4\)-module

\[
E_{11}=S_{(13,2,2,2)}V,\qquad \dim E_{11}=364.
\]

It is useful on the bulk HC4 cone locus: for a genuinely ternary cone top it
forces the quartic part to be affine-linear in the cone direction. But on the
cotangent locus

\[
h(x,y)=y_1P(x)+y_2Q(x)
\]

its restriction is exactly

\[
C_{11}\big|_{y\text{-linear}}=2a_6a_5,
\]

where \(a_6\) and \(a_5\) are the degree-six and degree-five pieces of
\(\det DF\). The top Hessian equation is \(C_{12}=a_6^2\), hence its reduced
locus has \(a_6=0\), and \(C_{11}\) vanishes there identically. It does **not**
force \(a_5=0\). Exact branching shows that the relevant plane isotype occurs
twice in the sector coefficient space; the unique ambient GL4 copy selects
the old product \(a_6a_5\), not the other possible covariant.

The independent Meng–Yang kill-probe also stops cleanly: their five-variable
degree-14 counterexample has **no nonzero constant direction** in which the
potential is affine-linear, or even quadratic with constant nonzero second
derivative. Thus their one-variable Schur-descent lemma cannot be iterated
from five variables to four after any constant linear rechart.

The cheap probe therefore confirms the adjudication’s **“no new JC2 theorem”
discount**. It does not refute quintic HC4 and does not show that no later HC4
argument could help JC2.

---

## 1. The canonical first layer

Let \(V=\mathbb C^4\), and write a quintic potential, after discarding constant
and linear terms, as

\[
h=h_2+h_3+h_4+h_5,\qquad h_d\in\operatorname{Sym}^d V^*.
\]

Put \(H_d=\operatorname{Hess}(h_d)\), whose entries have coordinate degree
\(d-2\), and write

\[
\det(H_5+H_4+H_3+H_2)=\sum_{k=0}^{12}C_k,\qquad
C_k\in\operatorname{Sym}^kV^*.
\]

The first two layers are

\[
C_{12}=\det H_5,\qquad
C_{11}=\operatorname{tr}\!\bigl(\operatorname{adj}(H_5)H_4\bigr).
\]

This sits inside the adjudicated size ledger
\[
\dim(\operatorname{Sym}^3V^*\oplus\operatorname{Sym}^4V^*
\oplus\operatorname{Sym}^5V^*)=20+35+56=111,
\]
with \(\sum_{k=0}^{12}\dim\operatorname{Sym}^kV^*=\binom{16}{4}=1820\)
scalar quartic equations. The cheap probe uses only the top 455 and next 364
coefficient equations.

Thus \(C_{11}\) is cubic in the coefficients of \(h_5\), linear in those of
\(h_4\), and contains no \(h_3\) or \(h_2\). It is the first variation of the
top Hessian equation.

There is a convention issue hidden by the phrase “GL4-isotypic after
normalizing \(h_2\).” Fixing \(h_2\) to a standard quadric leaves only an
orthogonal residual group. The honest GL4 calculation must be made before
that gauge choice. This is unambiguous here because \(C_{12}\) and \(C_{11}\)
do not involve \(h_2\).

Use the action \((g\cdot f)(x)=f(g^{-1}x)\). The determinant covariance is

\[
\det\operatorname{Hess}(g\cdot f)
=\det(g)^{-2}\bigl(\det\operatorname{Hess}f\bigr)\circ g^{-1}.
\]

Consequently the degree-11 output is

\[
\operatorname{Sym}^{11}V^*\otimes(\det V^*)^2,
\]

and its dual coefficient-equation module is

\[
E_{11}=\operatorname{Sym}^{11}V\otimes(\det V)^2
=S_{(13,2,2,2)}V.
\]

It is irreducible and

\[
\dim S_{(13,2,2,2)}V
=\dim\operatorname{Sym}^{11}V
=\binom{14}{3}=364.
\]

The relevant coefficient ambient space is

\[
\operatorname{Sym}^3(\operatorname{Sym}^5V)
\otimes\operatorname{Sym}^4V.
\]

### 1.1 Exact plethysm and Pieri result

The exact Python calculation gave

\[
\begin{aligned}
\operatorname{Sym}^3(\operatorname{Sym}^5V)=\;&
S_{(15)}+S_{(13,2)}+S_{(12,3)}+S_{(11,4)}+S_{(11,2,2)}\\
&+S_{(10,5)}+S_{(10,4,1)}+S_{(9,6)}+S_{(9,4,2)}\\
&+S_{(8,6,1)}+S_{(8,5,2)}+S_{(7,4,4)}+S_{(6,6,3)}.
\end{aligned}
\]

Every displayed multiplicity is one. Tensoring with \(S_{(4)}V\) and using
Pieri, \(S_{(13,2,2,2)}V\) has exactly one contributing constituent:

\[
S_{(11,2,2)}V\otimes S_{(4)}V
\supset S_{(13,2,2,2)}V,
\]

again with multiplicity one. Hence

\[
\boxed{
\operatorname{mult}_{(13,2,2,2)}
\left(
\operatorname{Sym}^3(\operatorname{Sym}^5V)
\otimes\operatorname{Sym}^4V
\right)=1.}
\]

The analogous top equation is also multiplicity one:

\[
E_{12}=S_{(14,2,2,2)}V,\qquad
\dim E_{12}=455,\qquad
\operatorname{mult}_{E_{12}}
\operatorname{Sym}^4(\operatorname{Sym}^5V)=1.
\]

The exact run printed

~~~text
Sym^3(Sym^5 V), ell<=4: constituents=13 multiplicity_sum=13
degree-11 equation type (13, 2, 2, 2) multiplicity in ambient=1
parents contributing: [((11, 2, 2), 1)]
top equation type (14, 2, 2, 2) multiplicity=1
dimension checksum Sym^3(Sym^5 C^4): 30856 = binomial(58,3)
after Pieri: 79 types, weighted dimension 1079960 = 30856*35
~~~

Because \(C_{11}\) is visibly nonzero (take diagonal monomial Hessians), its
coefficient span is the entire unique copy \(E_{11}\); this is not merely an
upper-bound calculation.

### 1.2 What it does on the bulk cone locus

After Gordan–Noether cone reduction, suppose the top is genuinely ternary:

\[
h_5=\varphi(z_1,z_2,z_3),\qquad
H_5=\begin{pmatrix}A&0\\0&0\end{pmatrix},\qquad
\det A\ne0.
\]

Then \(\operatorname{adj}(H_5)\) has only its \((4,4)\)-entry nonzero, so

\[
C_{11}=(\det A)\,\partial_{44}h_4.
\]

The polynomial ring is a domain; hence \(C_{11}=0\) forces
\(\partial_{44}h_4=0\). This is real four-dimensional structure and the
quintic analogue of the first-variation step in Ni’s quartic proof. The issue
is whether it remains informative on the JC2 sector. It does not.

---

## 2. Exact restriction to the \(y\)-linear sector

Split \(V=X\oplus Y\), with \(\dim X=\dim Y=2\), and put

\[
h(x,y)=\langle y,F(x)\rangle,\qquad F=(P,Q).
\]

The block determinant identity is

\[
\det\operatorname{Hess}h=(\det DF)^2.
\]

Write \(F=F_1+F_2+F_3+F_4\) by homogeneous degree, put

\[
J_3=DF_4,\qquad J_2=DF_3,
\]

and define

\[
a_6=\det J_3,\qquad
a_5=[\det DF]_5
=\operatorname{tr}\!\bigl(\operatorname{adj}(J_3)J_2\bigr).
\]

Coefficient comparison in the square gives the formal identities

\[
\boxed{C_{12}=a_6^2,\qquad C_{11}=2a_6a_5.}
\]

These were also checked over the universal integer coefficient ring for two
generic binary quartics and two generic binary cubics (18 independent
coefficients). The exact sparse-polynomial run printed

~~~text
a6 terms=20 a5 terms=36
[degree 12] (det J)^2 = a6^2: PASS, terms=180
[degree 11] (det J)^2 = 2*a6*a5: PASS, terms=520
mod radical(top equation)=(a6), degree-11 restriction = 0: PASS
~~~

Therefore the reduced top equation gives \(a_6=0\), after which the complete
degree-11 layer vanishes. It supplies no equation on \(a_5\). The next even
layer starts

\[
C_{10}=a_5^2+2a_6a_4,
\]

so, only after \(a_6=0\), it recovers \(a_5=0\) set-theoretically. This is the
ordinary plane determinant descent, delayed and squared—not an additional
constraint.

**Scheme caveat.** Relative to the nonreduced equations “coefficients of
\(a_6^2\),” the \(a_6a_5\) layer can change nilpotent structure. But every
coefficient of \(C_{11}\) lies in the reduced top ideal generated by the
coefficients of \(a_6\). It removes no reduced point and proves no new JC2
statement. Dividing by \(a_6\) on \(a_6=0\) is invalid.

### 2.1 Branching explains the loss

The unique GL4 equation type branches simply:

\[
\begin{aligned}
S_{(13,2,2,2)}(X\oplus Y)
&=(\det X)^2(\det Y)^2\operatorname{Sym}^{11}(X\oplus Y)\\
&=\bigoplus_{i=0}^{11}
S_{(i+2,2)}X\boxtimes S_{(13-i,2)}Y.
\end{aligned}
\]

The output independent of \(y\) is the endpoint

\[
S_{(13,2)}X\boxtimes S_{(2,2)}Y,
\]

and it occurs once in the restricted GL4 module.

Now compute directly in the sector coefficient space. Its degree-\((3,1)\)
piece is

\[
\operatorname{Sym}^3(Y\otimes\operatorname{Sym}^4X)
\otimes(Y\otimes\operatorname{Sym}^3X).
\]

Exact Cauchy/plethysm bookkeeping gives

\[
\begin{aligned}
S_{(2,1)}(\operatorname{Sym}^4X)=\;&
S_{(11,1)}+S_{(10,2)}+S_{(9,3)}\\
&+2S_{(8,4)}+S_{(7,5)}.
\end{aligned}
\]

Only the \(S_{(2,1)}Y\otimes Y\) Cauchy summand can produce
\(S_{(2,2)}Y\). On the \(X\)-side, both \(S_{(11,1)}\) and
\(S_{(10,2)}\), after tensoring with \(S_{(3)}X\), produce
\(S_{(13,2)}X\). Hence

\[
\operatorname{mult}_{S_{(13,2)}X\boxtimes S_{(2,2)}Y}
\left(
\operatorname{Sym}^3(Y\otimes\operatorname{Sym}^4X)
\otimes Y\otimes\operatorname{Sym}^3X
\right)=2.
\]

The restriction of the unique ambient GL4 copy occupies only one line in this
two-dimensional multiplicity space. The block determinant identifies that
line exactly as \(a_6a_5\). The other sector covariant is **not** selected by
the Hessian determinant layer. This is the requested isotypic discriminator:
the extra ambient symmetry chooses the already-vanishing product, not a new
plane equation.

For comparison, the top sector type
\(S_{(14,2)}X\boxtimes S_{(2,2)}Y\) occurs once and is \(a_6^2\). The exact
GL2 check was

\[
S_{(2,2)}(\operatorname{Sym}^4X)
=S_{(14,2)}+2S_{(12,4)}+S_{(11,5)}
+2S_{(10,6)}+2S_{(8,8)}.
\]

### 2.2 Geometric reading

On the reduced plane top locus, \(a_6=0\) says that the two homogeneous
quartic components have zero Jacobian; in the equal-degree binary setting
they are proportional. After a \(Y\)-change one may write

\[
h_5=y_1R_4(x_1,x_2),
\]

whose cone vertex is the \(y_2\)-direction. But \(h_4\) was already linear in
all \(y\)-variables, so \(\partial_{y_2y_2}h_4=0\) before HC4 says anything.
Thus the bulk conclusion of §1.2 becomes tautological on the cotangent locus.

Equivalently, the map from plane top data to the Hesse-zero equations is
quadratically ramified there: it pulls the top equation back to \(a_6^2\), so
its first variation vanishes along \(a_6=0\). The first GL4 layer sees **less**
infinitesimal information than the reduced plane equation, not more.

---

## 3. Meng–Yang 5→4 Schur-descent kill-probe

Meng–Yang obtain their five-variable counterexample from a six-variable
doubled potential by the following lemma. If

\[
\Phi(t,w)=tA(w)+B(w)
\]

is affine-linear in a pivot \(t\), has constant nonzero full Hessian
determinant, and the unbordered pencil

\[
M(s,w)=\operatorname{Hess}_w(B+sA)
\]

has \(\det M(s,w)\equiv0\), then

\[
\psi_{\lambda,\mu}=B+\frac{\lambda}{2}A^2+\mu A
\]

has constant nonzero Hessian determinant in one fewer variable. To iterate
the construction, the descended five-variable polynomial must possess a new
constant pivot direction.

For their explicit example, with variables
\((x_1,x_2,y_1,y_2,y_3)\) and \(u=1+x_1x_2\),

\[
\begin{aligned}
A={}&y_1u^3+3x_1y_2u^2-x_1^3y_3,\\
\Psi={}&A^2+13A+2B,
\end{aligned}
\]

where \(B\) is linear in \(y_1,y_2,y_3\). Its top form is

\[
\Psi_{14}=x_1^6x_2^6y_1^2.
\]

Let

\[
v=p\partial_{x_1}+q\partial_{x_2}+r\partial_{y_1}
+s\partial_{y_2}+t\partial_{y_3}
\]

be an arbitrary constant direction. If \(\Psi\) were affine in a linear
pivot with direction \(v\), then \(D_v^2\Psi=0\). The degree-12 part of
\(D_v^2\Psi\), coming from \(\Psi_{14}\), contains the distinct monomials

\[
30p^2x_1^4x_2^6y_1^2,\qquad
30q^2x_1^6x_2^4y_1^2,\qquad
2r^2x_1^6x_2^6.
\]

Therefore \(p=q=r=0\). In the remaining two-dimensional vertex space,
linearity of \(A\) and \(B\) in \(y\) gives the exact identity

\[
D_v^2\Psi
=2\left(3s x_1(1+x_1x_2)^2-tx_1^3\right)^2.
\]

It vanishes identically only when \(s=t=0\). The same calculation rules out
a unit quadratic pivot: if \(D_v^2\Psi\) were a nonzero constant, the top
degree again forces \(p=q=r=0\), after which the displayed square has an
\(x_1^2\) factor and cannot be a nonzero constant.

The exact sparse-polynomial run reconstructed all 42 monomials of \(\Psi\)
and printed

~~~text
Psi terms=42 degree=14
top(Psi)=x1^6*x2^6*y1^2
D_v^2 top degree has 6 terms
identity check:
  D2|_(p=q=r=0) = 2(3*s*x1*(1+x1*x2)^2-t*x1^3)^2 : PASS
nonzero constant affine/quadratic pivot direction: NONE
~~~

This is invariant under constant linear recharts: choosing a coordinate as
pivot after a GL5 change is the same as choosing a nonzero constant direction
\(v\) before it. The descent therefore fails before the secondary condition
\(\det M(s,w)\equiv0\) is reached. The top form is indeed a cone, with the two
obvious \(y_2,y_3\) vertex directions, so Gordan–Noether is not violated; the
lower rank-one term \(A^2\) prevents either top vertex direction from
extending to a pivot of the full potential. This makes precise the paper’s
statement that the first descent “spends” the dual-variable linearity.

This calculation rules out the **Meng–Yang constant-linear Schur pivot**. It
does not rule out a nonlinear coordinate change or a different
dimension-lowering construction.

---

## 4. Exact bookkeeping method

The GL calculations used the power-sum basis and the Frobenius character
formula. For \(\mu=(1^{m_1}2^{m_2}\cdots)\), put
\(z_\mu=\prod_i i^{m_i}m_i!\). The script formed

\[
h_r[h_m]
=\sum_{\nu\vdash r}\frac1{z_\nu}
\prod_{k\in\nu}
\left(\sum_{\rho\vdash m}\frac{p_{k\rho}}{z_\rho}\right)
\]

as an exact partition-to-Fraction dictionary. It recovered Schur
multiplicities by

\[
[S_\lambda]f=\sum_\mu[p_\mu]f\,\chi^\lambda(\mu).
\]

The integer characters were computed independently from the Frobenius
coefficient formula

\[
\chi^\lambda(\mu)
=[x^{\lambda+\delta}]\,\Delta(x)p_\mu(x),
\qquad \delta=(n-1,n-2,\ldots,0),
\]

by enumerating the at most \(4!\) Vandermonde monomials and assigning the
parts of \(\mu\) to four variables. Pieri was then an exact horizontal-strip
test. Internal checks included the \(S_3\) standard character row
\((2,0,-1)\), Weyl-dimension sums, and the independent GL2 checks

\[
\dim S_{(2,1)}(\mathbb C^5)=40,\qquad
\dim S_{(2,2)}(\mathbb C^5)=50.
\]

No numerical character evaluation or interpolation enters the result.

---

## 5. Gap ledger and decision

### Exact conclusions

1. The first post-top quintic equation module is the unique
   \(S_{(13,2,2,2)}V\), of dimension 364.
2. On a genuinely ternary HC4 top cone it forces
   \(\partial_{vv}h_4=0\) in the vertex direction.
3. On the \(y\)-linear sector its complete restriction is \(2a_6a_5\), hence
   zero modulo the radical of the top equation \(a_6^2=0\).
4. The relevant sector isotype has multiplicity two, but the ambient GL4
   layer selects only the factored, already-vanishing copy.
5. The explicit Meng–Yang HC5 counterexample has no constant affine or
   unit-quadratic pivot, so their Schur descent does not iterate 5→4 through
   any linear rechart.

### CONJECTURE gaps

- **CONJECTURE:** no later cone-stratified HC4 layer yields a degree-uniform
  proof mechanism on the cotangent sector. The present computation settles
  only the first layer; it supports this statement but does not prove it.
- **CONJECTURE:** no nonlinear rechart or different partial-Legendre device
  descends the Meng–Yang example to four variables. Only the exact
  constant-linear pivot class used by their theorem was killed.
- The full quintic HC4 case, including binary/unary cone strata and all lower
  coupled layers, remains open. No quintic HC4 theorem or counterexample is
  claimed here.

### Row-10 decision

The first GL4 module has **bulk HC4 leverage but no JC2-sector leverage**. It
reproduces a useful cone-direction constraint generically, yet that constraint
is automatic on cotangent potentials and its restricted equation is killed by
the preceding plane top equation. The 5→4 counterexample factory also
self-terminates exactly as advertised.

**KILL-PROBE verdict: NO LEVERAGE. Confirm the “no new theorem” discount.**
Keep HC4 quintic as an intrinsically interesting four-dimensional problem,
but do not promote its first isotypic layer as evidence for a new plane
theorem.

## Sources checked

- Repository adjudication and row-10 specification:
  [hc4-adjudication.md](hc4-adjudication.md) and
  [APPROACHES.md](../APPROACHES.md).
- G. Meng and L. Yang, *A five-variable counterexample to the Hessian
  conjecture, and the low-dimensional status of the Jacobian and Hessian
  conjectures*, [arXiv:2607.22198v2](https://arxiv.org/abs/2607.22198),
  especially Appendix A (Schur descent).
- Z. Ni, *The Quartic Hessian Conjecture in Dimension Four*,
  [arXiv:2608.14217](https://arxiv.org/abs/2608.14217), especially the
  first-variation and coupled-layer arguments.
