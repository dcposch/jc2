# Generic output coordinates reduce Keller dynamics to the infinitely singular case

**Tier: PROMOTED / MANUAL / CONDITIONAL on the named Favre–Jonsson foundations.** ROOT and Astra supplied the arguments; Sol independently reviewed both. No novelty claim is made. JC2 remains unresolved.

## The reduction
Let F:C²→C² be a nonlinear polynomial map with det DF=1. There is a nonempty Zariski-open subset U of SL₂(C) such that, for every A in U, H=A∘F has an infinitely singular Favre–Jonsson eigenvaluation.
Consequently, proving that every Keller map in this generic presentation is invertible would prove JC2. The result does not exclude infinitely singular eigenvaluations: nonlinear polynomial automorphisms are compatible with it.
In the presentation constructed below, d=deg H≥2, deg Hⁿ=dⁿ, the generic field degree satisfies N<d², and the eigenvaluation is centered at a regular point p∞ of the ordinary projective line at infinity.
Near p∞ there are analytic coordinates in which
\[ H(z,w)=\bigl(z^d,\ d^{-1}z^{2d-2}w+P(z)\bigr),\qquad 1\leq\operatorname{ord}P<d. \]
The analytic coordinate change is not asserted to be rational or polynomial.

## 1. A local lemma
Suppose a holomorphic germ G at0 has the form
\[G(u,v)=(u^d a(u,v),u^p b(u,v)),\quad d\geq2,\quad 1\leq p<d,\quad a(0)b(0)\ne0,\]
and preserves the meromorphic form u⁻³du∧dv. Then no divisorial valuation ν centered at0 satisfies G_*ν=dν.
Here divisorial means a positive multiple of the order of an exceptional prime on a finite succession of point blowups of the smooth germ.

The differential DG(0) is nilpotent. Choose a norm and a sufficiently small invariant ball on which G contracts and a has a bounded holomorphic logarithm A. The normally convergent series
\[L=\sum_{k\geq0}d^{-k-1}A\circ G^k\]
satisfies dL=A+L∘G. Thus z=u exp L is a holomorphic coordinate with z∘G=z^d. In coordinates (z,v), write the preserved form as z⁻³h(z,v)dz∧dv with h a unit, and set w(z,v)=∫₀ᵛh(z,t)dt.
These are coordinates, w(z,0)=0, and the form is exactly z⁻³dz∧dw. Writing G=(z^d,W), volume preservation forces
\[\partial_wW=d^{-1}z^{2d-2},\qquad W=P(z)+d^{-1}z^{2d-2}w.\]
On w=0 one has v=0 and u=z times a unit. The output v-coordinate is u^p b(u,0), and the output w-coordinate is that v-coordinate times a unit. Hence ord P=p.

Assume now that a divisorial eigenvaluation exists, and scale it to a primitive integral order v on K=Frac C{z,w}. Put m=v(z)>0. Its residue field is C(E)=C(q), since E is an exceptional rational curve. The local analytic field, rather than the original global rational field, is used here.
Complete this discrete valuation field. It has a coefficient field C(q); adjoining τ=z^(1/m) gives an unramified finite extension with residue field k′ finite over C(q), and τ is a uniformizer. These are the standard equicharacteristic complete-DVR and Henselian lifting facts, with characteristic-zero residue field.
Expand w in τ with coefficients in a lifted copy of k′. There is a first coefficient outside C: otherwise z=τ^m and w∈C[[τ]] would give constant residue for every fraction of convergent germs, contradicting residue(K)=C(q). Positive values of z,w justify convergence of all these substitutions.
Thus, for a finite Puiseux polynomial s with positive exponents below r,
\[w=s(z)+z^r\eta,\qquad v(\eta)=0,\qquad\overline\eta\notin\mathbb C.\]
The residue of η is transcendental over C. This proves the finite-prefix assertion needed for a divisorial valuation; no infinitely singular prefix-classification theorem is used.

Let σ=G*. The nonzero Jacobian away from z=0 makes σ injective. The eigenrelation v(σf)=dv(f) extends σ continuously to the completed field. Extend this embedding to the finite extension containing τ; since σ(z)=z^d, σ(τ)=ζτ^d for an m-th root of unity ζ∈C, so its image remains in that extension.
Uniqueness of valuation extension from a complete discretely valued field gives v(σx)=dv(x) there. The induced residue map is injective and fixes C, so the residue of ση is still transcendental.
Applying σ to the finite prefix shows that the first coefficient outside C in σw occurs at normalized z-exponent dr. The exact triangular expression
\[\sigma w=P(z)+d^{-1}z^{2d-2}s(z)+d^{-1}z^{2d-2+r}\eta\]
puts its first nonconstant coefficient at 2d−2+r. A constant term of P cannot cancel a transcendental residue. Therefore dr=2d−2+r, so r=2.
Since p<d≤2d−2 and v(w)>0, the lowest normalized z-order of σw is p. The eigenrelation forces s to have leading exponent p/d, which is nonintegral and lies strictly between0 and1.
Let q<2 be the largest nonintegral exponent in the finite support of s. The right side has a nonzero term of exponent 2d−2+q<2d: P has only integral powers, and the remainder starts at2d. On the left, such a term requires an exponent
\[q'=(2d-2+q)/d\]
in s. This exponent is nonintegral, and q′−q=(d−1)(2−q)/d>0, contradicting maximality of q. Root-of-unity choices change nonzero coefficients, not this support. The local lemma follows.
An eigenrelation initially given on rational functions in u,v extends to convergent germs by Taylor truncation: the source and pulled-back maximal ideals both have positive value. This also preserves residue classes of fractions. No rationality of the analytic coordinate change is needed.

## 2. Generic linear output changes supply the local germ
Let d=max(deg F₁,deg F₂)>1. Choose S∈SL₂(C) so (P,Q)=S∘F has degrees d>q≥1. If both initial degrees are d, their degree-d homogeneous parts are proportional: the highest Jacobian term vanishes, and for binary homogeneous forms x^d f(y/x), x^d g(y/x), this says fg′−f′g=0. A determinant-one row operation lowers one degree; Jac=1 prevents a constant component.
Write B=[[a,b],[c,e]]∈SL₂, w₀=(a,c), and impose a≠0, P_d(w₀)≠0 and Q_q(w₀)≠0. These are nonempty Zariski-open conditions: choose w₀=(1,s) outside finitely many roots, then complete it to B. The allowed total output changes BS form a nonempty open subset of SL₂.
For H=B(P,Q), the leading homogeneous map is H_d=w₀P_d, with P_d(w₀)≠0. Every iterated leading composition is nonzero, so deg Hⁿ=dⁿ and λ₁=d. Generic-fibre Bézout gives N≤dq<d², without assuming properness.
At p∞=[a:c:0], set s=c/a, u=1/x and v=y/x−s. Write P=u⁻ᵈP̃ and Q=u⁻ᑫQ̃. Both P̃ and Q̃ are units at0. Direct substitution gives
\[u'=\frac{u^d}{a\widetilde P+b u^{d-q}\widetilde Q},\qquad v'=\frac{u^{d-q}\widetilde Q}{a(a\widetilde P+b u^{d-q}\widetilde Q)}.\]
This is exactly the local germ above with p=d−q. Since dx∧dy=−u⁻³du∧dv and det DH=1, its pole-three form is preserved.

## 3. The global eigenvaluation is centered at this germ
Let ν_n=d⁻ⁿ(−deg)∘Hⁿ. For every n≥1, ν_n(u)=1. The identity v∘H=Q/(aH₁) and Q_q(w₀)≠0 give deg(Q∘Hⁿ⁻¹)=qdⁿ⁻¹, so ν_n(v)=(d−q)/d>0.
Favre–Jonsson Proposition2.3 supplies ν_*∈V₁ with H_*ν_*=dν_*. Since N<d², Theorem2.4(b) gives ν_n→ν_*; the degree valuation has skewness1>0. Pointwise convergence on polynomials gives the same values on these rational coordinates, since x and y−sx have fixed finite values along the orbit.
Hence ν_*(u)=1 and ν_*(v)=(d−q)/d>0: it is centered at the specified p∞. Theorem2.4(a) also gives uniqueness in its stated nonnegative-skewness scope.
Proposition2.5 leaves only the divisorial and infinitely singular possibilities because λ₁=d is integral and N<d². The local lemma excludes the divisorial possibility. This proves the reduction.
A hypothetical noninvertible Keller map is nonlinear, and output automorphisms preserve noninvertibility and N. The unresolved task is to rule out noninvertibility in this presentation, not to rule out infinitely singular eigenvaluations for automorphisms.

## Evidence and limits
The [local proof](../box/generic-output-reduction-swarmHQ-20261026/generic1835-astra.md), [global proof](../box/generic-output-reduction-swarmHQ-20261026/generic1835-root-global.md), and [independent review](../box/generic-output-reduction-swarmHQ-20261026/genericreview1856-sol56.md) are preserved byte-for-byte, with their manifests. [Custody and reading qualifications](../box/generic-output-reduction-swarmHQ-20261026/custody.md) are mandatory companions.
The external source is Favre–Jonsson, *Dynamical compactifications of C²*, Annals173(2011),211–249, [DOI10.4007/annals.2011.173.1.6](https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n1-p06-p.pdf). ROOT read cached text375–430; the reviewer read375–423. Proposition2.3's statement and Theorem2.4/Proposition2.5's printed proofs were checked; the partial Proposition2.6 excerpt is unused.
Underlying references[8],[28],[30] and Appendix-A foundations remain named imports rather than newly audited proofs. The elementary complete-DVR, smooth-surface realization and Bézout facts are explicit. No stopped Favre2010 source or infinitely singular essential-prefix classification was imported.
The result gives no properness, surjectivity, N=1, isotropy, boundary-weight estimate, or invariance of the original map's eigenvaluation under output change. The earlier divisorial results keep their exact hypotheses; they need not be completed as a separate branch to use this reduction.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9377`.
- Body SHA-256:
  `e4599fb131808b89d93f509443908d892458ca0006448f4417074ff2f98171b4`.
- Frozen basis: `762c5705ee58b59a150cb630a9d68310ec949d07`.
