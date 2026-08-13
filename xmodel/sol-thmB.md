# Theorem B obstruction: functional 41-jet flexibility with tails

## Executive summary

1. The promoted zero-tail contradiction extends to tails of strictly positive valuation, but reduction no longer yields the killed tail-free system once a tail has valuation zero.
2. For the normalized residue-A lead \(p=\eta^6-6\eta^3+6\), explicit polynomial tails realize any prescribed nonzero Row \(20\) while every other J-row below slot \(42\) vanishes.
3. The escape is a common-cusp tangent in slot \(10\) whose square feeds Row \(20\), exactly the level-42 quadratic mechanism left open by the campaign ([SHEET6-DIRECTIONB.md:447-463](../SHEET6-DIRECTIONB.md)).
4. In the recorded full-window relaxation, tail-value vectors linearly span the inhomogeneous residual, so no unconditional additive residue/Gaussian/Mathieu separator can detect the \(-42\) ([SHEET6-DIRECTIONB.md:486-501](../SHEET6-DIRECTIONB.md)).
5. Thus any kill must additionally use template/monomial compatibility or later rows; the construction below is neither a template point nor an all-orders Jacobian pair, and campaign nonemptiness remains open ([SHEET6-DIRECTIONB.md:549-570](../SHEET6-DIRECTIONB.md)).

**Status.** This is a proved obstruction theorem, not a candidate kill. It gives a precise ceiling on a functional-level Theorem B based only on the square/cube skeleton and the pure \(y\)-side J-rows.

## 1. Functional setup and statement

In the campaign gauge \(\sigma=6\), the two merge directions are
\(a_1=3+\sqrt3\), \(a_2=3-\sqrt3\). Hence the normalized common factor is

\[
p(\eta)=(\eta^3-a_1)(\eta^3-a_2)
       =\eta^6-6\eta^3+6.
\]

This is the rigid residue-A merge pattern; the square/cube leads are scalar
multiples of \(p^2,p^3\) ([SHEET6-TEMPLATE.md:84-111](../SHEET6-TEMPLATE.md),
[SHEET6-CAMPAIGN.md:3-10](../SHEET6-CAMPAIGN.md)). Dividing the two jets by
their nonzero lead scalars only rescales the right-hand side, so it is enough
to use the normalized leads \(p^2,p^3\).

For \(\Phi,\Gamma\in K[\eta,t]\), put

\[
 \mathcal B(\Phi,\Gamma)
 :=(t\Phi_t-12\Phi)\Gamma_\eta
   -\Phi_\eta(t\Gamma_t-18\Gamma).
\]

The exact chart identity is
\(\mathcal B(\Phi,\Gamma)=-(42/(c_fc_g))t^{20}\), and its coefficient
rows are

\[
 R_k=\sum_{i+j=k}
 \bigl((i-12)F_iG_j'-(j-18)G_jF_i'\bigr),
 \qquad
 \Phi=\sum F_it^i,\quad \Gamma=\sum G_it^i.
 \tag{1}
\]

These are campaign facts from
[SHEET6-DIRECTIONB.md:44-66](../SHEET6-DIRECTIONB.md). The x-side factors
first enter at slot \(42\), so all rows \(0\leq k\leq41\) are pure
\(y\)-side data ([SHEET6-DIRECTIONB.md:68-73](../SHEET6-DIRECTIONB.md)).

### Theorem B-O (41-jet flexibility obstruction)

Let \(K\) be an algebraically closed field of characteristic zero and let
\(c\in K^\times\). There exist \(\Phi,\Gamma\in K[\eta,t]\) such that

\[
 \Phi\equiv p^2\pmod {t^{10}},\qquad
 \Gamma\equiv p^3\pmod {t^{10}},\qquad
 \mathcal B(\Phi,\Gamma)\equiv c t^{20}\pmod {t^{42}}.
 \tag{2}
\]

In particular, all slots \(1,\ldots,9\) of both jets vanish, \(R_{20}=c\),
and \(R_k=0\) for every \(0\leq k<42\), \(k\ne20\).

Algebraic closure is used only to take square roots in Lemma 2. Thus a
finite algebraic extension of any characteristic-zero field over which
\(p\) and \(c\) are defined suffices; no assertion is made that the
construction is defined over \(\mathbb Q(\sqrt3)\) itself.

Consequently, the square/cube leading skeleton, polynomiality in \(\eta\),
and even the entire pure \(y\)-side J-window do **not** imply that Row \(20\)
is zero, divisible by \(p\), or excluded by a valuation-at-infinity argument.
Any theorem killing the campaign tails must use additional admissibility of
the branch-product tails, relations among their monomials, or information
outside this unrestricted 41-jet problem.

## 2. First lemma: cusp tangents and the quadratic escape

### Lemma 1 (lead-linear normal form)

Let \(p\in K[\eta]\) be nonconstant, \(F_0=p^2\), and \(G_0=p^3\). For
a prospective slot-\(n\) pair \((F_n,G_n)=(f,g)\), set

\[
 h:=g-\frac32pf.
\]

Its contribution linear in \((f,g)\) to Row \(n\) is

\[
 L_n(f,g)=-2p\bigl(6p h'+(n-18)p'h\bigr).
 \tag{3}
\]

If \(p\) is squarefree, then \(L_{10}(f,g)=0\) forces
\(g=(3/2)pf\). If the earlier nonzero data consist of
\(F_{10}=r\), \(G_{10}=(3/2)pr\), then their self-pair contributes to
Row \(20\)

\[
 Q_{20}(r)=-3p'r^2+9prr',
 \qquad Q_{20}(r)\equiv-3p'r^2\pmod p.
 \tag{4}
\]

#### Proof

The pairs \((n,0)\) and \((0,n)\) in (1) give

\[
\begin{aligned}
L_n(f,g)
 &=3(n-12)p^2p'f+18p^3f'
   -12p^2g'-2(n-18)pp'g.
\end{aligned}
\]

Substitute \(g=(3/2)pf+h\). The coefficients of both \(f\) and \(f'\)
cancel, leaving exactly (3).

At \(n=10\), the equation is \(6ph'-8p'h=0\). Suppose \(h\ne0\), and
let \(\alpha\) be any simple root of \(p\). In the local parameter
\(x=\eta-\alpha\), write \(p=xu\) and \(h=x^mv\), where
\(u(0)v(0)\ne0\) and \(m\in\mathbb Z_{\ge0}\). The lowest coefficient of
\(6ph'-8p'h\) is

\[
 (6m-8)u(0)v(0)x^m,
\]

which cannot vanish in characteristic zero because \(m\ne4/3\). Thus
\(h=0\), proving the slot-10 assertion.

Finally, the \((10,10)\) term of (1) is

\[
 -2r\left(\frac32pr\right)'
 +8\left(\frac32pr\right)r'
 =-3p'r^2+9prr'.
\]

Reduction modulo \(p\) gives (4). \(\square\)

The point of (4) is that the first tail is invisible linearly but not
quadratically. Thus the associated graded at tail degree one loses the
very term that can supply the inhomogeneity.

## 3. The campaign-specific Bezout identity

### Lemma 2 (square lift and fractional-weight primitive)

Set

\[
 s(\eta)=\frac{4\eta-\eta^4}{108}.
\]

Then

\[
 \frac92ps'-3p's=1. \tag{5}
\]

For every \(c\in K^\times\), there are \(r,Q\in K[\eta]\) satisfying

\[
 r^2=cs+p^3Q. \tag{6}
\]

#### Proof

Put \(z=\eta^3\). Then \(p=z^2-6z+6\),
\(s'=(1-z)/27\), and \(p'=6\eta^2(z-3)\). Therefore

\[
\begin{aligned}
 \frac92ps'-3p's
 &=\frac16\bigl(p(1-z)-z(z-3)(4-z)\bigr)\\
 &=\frac16\bigl(6\bigr)=1,
\end{aligned}
\]

which proves (5).

The polynomial \(p\) is squarefree: a common zero of \(p\) and
\(p'=6\eta^2(\eta^3-3)\) would have \(\eta=0\) or \(\eta^3=3\), but
\(p\) then equals \(6\) or \(-3\). Also \(p\) and \(s\) are coprime,
since a zero of \(s=\eta(4-\eta^3)/108\) has \(\eta=0\) or
\(\eta^3=4\), where \(p=6\) or \(-2\).

Thus \(cs\) is a unit in the reduced algebra \(K[\eta]/(p)\). Since
\(K\) is algebraically closed, this algebra is a product of copies of
\(K\), and \(cs\) has a square root in it. Choose a polynomial
\(r_1\) representing such a root.

It remains only to lift the congruence from \(p\) to \(p^3\). Suppose
\(r_m^2-cs=p^md_m\) for \(m=1\) or \(2\). The class of \(2r_m\) is a
unit modulo \(p\), so choose \(u_m\) with

\[
 d_m+2r_mu_m\equiv0\pmod p.
\]

For \(r_{m+1}=r_m+p^mu_m\), expansion gives

\[
 r_{m+1}^2-cs
 =p^m\bigl(d_m+2r_mu_m+p^mu_m^2\bigr),
\]

which is divisible by \(p^{m+1}\). Two steps give \(r=r_3\) with
\(p^3\mid r^2-cs\); defining \(Q=(r^2-cs)/p^3\) proves (6). \(\square\)

Identity (5) is the special rigidity failure. It is the inhomogeneous
equation

\[
 pC'-\frac23p'C=c,
 \qquad C=\frac92cs. \tag{7}
\]

Here \(\deg C=4=(2/3)\deg p\), so the leading term is resonant. The
promoted Theorem A applies to the integer weights \(w\ge1\) and uses the
factor \(\deg C-w\deg A\) at infinity
([MATHIEU.md:279-315](../MATHIEU.md)); it cannot be extended naively to
the fractional weight \(2/3\), for which (7) is an explicit counterexample.

## 4. Proof of Theorem B-O

Choose \(r,Q\) as in Lemma 2 and define

\[
 a=\frac{pQ}{12},
 \qquad
 b=\frac32\frac{a^2}{p}=\frac{pQ^2}{96}.
 \tag{8}
\]

Both are polynomials. Set

\[
\begin{aligned}
 \Phi&=p^2+r t^{10}+a t^{20},\\
 \Gamma&=p^3+\frac32pr t^{10}+6pa t^{20}+b t^{40}.
\end{aligned}
\tag{9}
\]

Only row indices \(0,10,20,30,40\) can occur below \(42\).
The lead row \(R_0\) vanishes because \(p^2,p^3\) are a square/cube pair,
and Lemma 1 gives \(R_{10}=0\).

For Row \(20\), put

\[
 h_{20}:=G_{20}-\frac32pF_{20}
 =\frac92pa
 =\frac38\frac{r^2-cs}{p}.
\]

Combining (3) with the quadratic term (4) gives

\[
 R_{20}=9prr'-3p'r^2-12p^2h_{20}'-4pp'h_{20}.
\]

Defining

\[
 C:=\frac92r^2-12ph_{20}=\frac92cs,
\]

gives

\[
 R_{20}=pC'-\frac23p'C
 =c\left(\frac92ps'-3p's\right)=c
\]

by (5).

At Row \(30\), the only pairs are \((10,20)\) and \((20,10)\), hence

\[
\begin{aligned}
 R_{30}
 &=-2\bigl(rG_{20}\bigr)'
   +8\bigl(aG_{10}\bigr)'\\
 &=-2(6par)'+8\left(\frac32par\right)'=0.
\end{aligned}
\]

At Row \(40\), the self-pair of the slot-20 coefficients contributes

\[
 8a(6pa)'-2(6pa)a'=48p'a^2+36paa'.
\]

The term linear in \(G_{40}=b\) is

\[
 -12p^2b'-44pp'b=-48p'a^2-36paa',
\]

where (8) was used. Thus \(R_{40}=0\). Every other row below \(42\)
vanishes by support, proving (2). In fact the exact remainder is

\[
 \mathcal B(\Phi,\Gamma)
 =ct^{20}+(-2rb'-22br')t^{50}
          +(8ab'-22ba')t^{60}.
 \tag{10}
\]

This completes the proof. \(\square\)

## 5. What the associated graded does prove

### Proposition 3 (no positive-valuation deformation of the skeleton)

Let \((R,\mathfrak m)\) be a local ring with characteristic-zero residue
field. Suppose a residue-A template jet through slot \(20\) has
\(c_f,c_g\in R^\times\), and every free P-side and B-side tail coefficient
lies in \(\mathfrak m\); the seven dead-stretch coefficients may be
arbitrary elements of \(R\). Then the jet cannot satisfy the J-identity
through slot \(20\).

#### Proof

Reduce every row modulo \(\mathfrak m\). Every tail-loaded monomial
disappears, while \(-42/(c_fc_g)\) remains nonzero because the residue
field has characteristic zero. The reduced equations are precisely the
pure-dead-stretch zero-tail system: the full-window gate verifies that
tail specialization reproduces that system coefficient-for-coefficient
([SHEET6-DIRECTIONB.md:389-396](../SHEET6-DIRECTIONB.md)). The promoted
zero-tail theorem rules it out uniformly in all seven dead-stretch
coefficients ([SHEET6-DIRECTIONB.md:221-238](../SHEET6-DIRECTIONB.md)).
Contradiction. \(\square\)

Thus every possible survivor has at least one order-zero tail under any
such valuation. The associated graded skeleton excludes infinitesimal or
positive-valuation deformations, but it says nothing about the order-one
quadratic escape constructed in (9). This agrees with the campaign's
inconsistent differentials at the tested zero-tail points
([SHEET6-DIRECTIONB.md:503-518](../SHEET6-DIRECTIONB.md)).

## 6. Why a fixed additive moment cannot repair the argument

The preceding theorem concerns unrestricted polynomial jets. There is
also a narrower obstruction inside the campaign's actual 83-variable
window.

Fix a value-tier specialization for which the promoted free-monomial
relaxation is reported consistent (in particular, the normalized verdict
specialization), and base-change its étale coefficient algebra to an
infinite field factor \(K\). Collect the 77 recorded eta-component
equations into

\[
 r+P(u)=0,
 \qquad
 P(u)=\sum_{\alpha\in A}v_\alpha u^\alpha\in W:=K^{77},
 \tag{11}
\]

where \(u\) is the tail/dead-stretch tuple, \(A\) is the finite set of
distinct nonconstant monomials, and \(r\) is the zero-tail residual,
including the pole-scale block and the Row-20 constant. The campaign's
value-tier algebra and unit-pivot semantics are documented at
[SHEET6-DIRECTIONB.md:404-425](../SHEET6-DIRECTIONB.md).

### Lemma 4 (evaluation-span lemma)

For any polynomial map of the form (11) over an infinite field,

\[
 \operatorname{span}_K\{P(u):u\in K^N\}
 =\operatorname{span}_K\{v_\alpha:\alpha\in A\}. \tag{12}
\]

#### Proof

The left side is contained in the right side by expansion. Let \(U\) be
the left side and let \(\pi:W\to W/U\) be the quotient map. For every
\(u\in K^N\),

\[
 \sum_{\alpha\in A}\pi(v_\alpha)u^\alpha=\pi(P(u))=0.
\]

Apply any linear functional \(\lambda\in(W/U)^*\). The resulting scalar
polynomial vanishes on all of \(K^N\). Since \(K\) is infinite and the
monomials are distinct, every coefficient
\(\lambda(\pi(v_\alpha))\) is zero. Linear functionals separate points in
the finite-dimensional space \(W/U\), so \(\pi(v_\alpha)=0\) for every
\(\alpha\). Hence every \(v_\alpha\in U\), proving the reverse inclusion.
\(\square\)

The exact free-monomial computation reports:

- Row \(20\): 10 rows, 2718 monomial columns, rank 10, consistent;
- full window: 77 rows, 5106 monomial columns, rank 57, consistent.

These are promoted campaign results
([SHEET6-DIRECTIONB.md:475-501](../SHEET6-DIRECTIONB.md)). For Row \(20\),
rank 10 says its coefficient vectors span the entire ten-dimensional
eta-slot space. Lemma 4 therefore implies that the span of evaluated
Row-20 tail contributions contains, in particular, the pure
\(\eta^0\)-constant vector.

Separately, consistency of the full affine system says
\(-r\in\operatorname{span}\{v_\alpha\}\), and Lemma 4 upgrades this to

\[
 -r\in\operatorname{span}_K\{P(u):u\in K^{83}\}. \tag{13}
\]

Therefore, if a fixed linear functional annihilates the Row-20 tail
contribution for every tail assignment, it annihilates the pure constant
vector; and if \(\Lambda:W\to K\) annihilates the full contribution
\(P(u)\) for every assignment, it also annihilates \(r\). Likewise, every
fixed linear subspace containing all evaluated tail contributions contains
their span, hence the corresponding constant vector and full residual.
In particular, a residue, constant-term, Gaussian-moment functional, or
proposed Mathieu subspace used **only in this unconditional
additive-separation form** cannot contain all tails while excluding the
nonzero constant. Here only the underlying linear subspace of a Mathieu
subspace is being used
([MATHIEU.md:37-47](../MATHIEU.md)); the conclusion does not exclude a
power/multiplicative Mathieu argument after imposing the lower-band ideal.

This does **not** produce one tail tuple solving the equations: (13) may
use a linear combination of values at different tuples. Equivalently, the
relaxation treats the monomial coordinates \(u^\alpha\) independently,
whereas a real tuple must lie on their monomial (toric/Veronese) image.
A functional formed only after restricting to the nonlinear lower-band
variety is not excluded by this theorem; it would be using precisely the
missing multiplicative information.

## 7. Scope and surviving frontier

There is no conflict with the campaign's killed slot-20-linear stratum:
that smaller map has rank \(4/10\) and its target lies outside the image,
while a survivor needs the level-42 quadratic block or lower cross-terms
([SHEET6-DIRECTIONB.md:447-463](../SHEET6-DIRECTIONB.md)). Formula (4)
exhibits exactly why restoring the quadratic block changes the answer.

Nor does Theorem B-O construct an actual residue-A point. Its coefficients
have not been shown to arise from the prescribed 315 branch factors
([SHEET6-DIRECTIONB.md:141-158](../SHEET6-DIRECTIONB.md)), and
(10) is generally nonzero beyond the pure \(y\)-window. The actual
campaign variety remains the 47 lower-band conditions plus the ten
inhomogeneous slot-20 conditions; its nonemptiness was not certified
([SHEET6-DIRECTIONB.md:549-570](../SHEET6-DIRECTIONB.md)).
The saturated residual system has now been emitted for Groebner testing,
but the recorded characteristic-zero lane has not been run
([SHEET6-DIRECTIONB.md:605-645](../SHEET6-DIRECTIONB.md)).

The conclusion is negative and precisely scoped:

> The tail-free skeleton controls the formal neighbourhood of the origin,
> but by itself does not control unrestricted order-one tails. At the
> functional level the
> \(2{:}3\) cusp converts Theorem A's integer-weight rigidity into the
> solvable fractional resonance (7), and at the campaign coefficient
> level the inhomogeneous residual already lies in the span of nonlinear
> tail values. Monomial compatibility, template support, or later J-rows
> is indispensable.
