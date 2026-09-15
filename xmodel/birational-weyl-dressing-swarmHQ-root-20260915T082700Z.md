# A birational Weyl endomorphism is polynomially invertible

Producer: swarmHQ ROOT (gpt-6-astra).
Independent co-check: swarmHQ native Astra (gpt-6-astra), same-model;
terminal CONFIRMED, not different-model hostile review.
Date: 2026-09-15 UTC.
Basis: 3343285b4130cb0ad953e803aec3ccf548532aaa.
Evidence: MANUAL, relative to the named standard imports below.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED. Novelty UNKNOWN; no priority claim.

## Statement and construction scope

Put
\[
 W=\mathbf C\langle x,\partial\mid\partial x-x\partial=1\rangle,
 \qquad D=\operatorname{Frac}(W).
\]
Let \(\phi:W\to W\) be a unital \(\mathbf C\)-algebra endomorphism, and
let \(N=\max(\deg_B\phi(x),\deg_B\phi(\partial))\), where \(\deg_B\)
is Bernstein total degree. Assume its induced map \(D\to D\) is an
automorphism. Then \(\phi\) is an automorphism of \(W\), with
\[
                       \deg_B\phi^{-1}\leq N.
\]

Consequently, a genuine automorphism of the rational Weyl division ring
whose images of both standard generators are polynomial cannot produce a
proper Weyl endomorphism. This excludes finite rational division-ring
automorphism dressings of the standard Heisenberg pair, not arbitrary
endomorphisms, formal or pseudodifferential transformations, or nonbirational
division-ring embeddings. No candidate pair or general JC2/DC1 proof follows.

## Dependencies and prior work

Primary source: Belov-Kanel--Kontsevich, *The Jacobian Conjecture is stably
equivalent to the Dixmier Conjecture*, arXiv math/0512171v2, December16,2005,
[versioned text](https://arxiv.org/html/math/0512171v2).
We import the positive-characteristic center/Azumaya results of Sections3--4,
Propositions1--4, the Poisson compatibility of Lemmas4--6, and the Bernstein
degree comparison. Section2 recalls Gabber's polynomial-automorphism inverse
degree bound over any field. ROOT and the co-checker read these sections;
Gabber's original proof was not re-audited. We use these ingredients with
the extra rational-inverse hypothesis, not the paper's assumed JC endpoint.

Other standard inputs are the PBW basis, the Ore property and characteristic-zero
simplicity of the Weyl algebra, generic smoothness/spreading out, Zariski's Main
Theorem for quasi-finite birational maps to a normal target, and extension of
regular functions across codimension at least two in a normal variety.

Scoped history searches in notes, strategy archives and xmodel found no exact
statement of this rational-dressing filter; that is not a novelty certificate.
The prior source-reset discussion of DC1 does not identify arbitrary plane
Keller maps with first-Weyl endomorphisms. Retain the
[September15 correction](../notes.md#2026-09-15-0018-utc--source-strategy-intake-and-moment-criterion):
filtered strictness/operator-identification cannot be assumed.
No accepted transfer theorem or degree foundation is being reproved here.

## Argument

### 1. Spread only finite rational-inverse data

Characteristic-zero simplicity makes \(\phi\) injective. Surjectivity on
division rings gives elements \(a,b,c,e\in W\), with \(a,c\ne0\), such that
\[
 x=\phi(a)^{-1}\phi(b),\qquad
 \partial=\phi(c)^{-1}\phi(e).
\]
Thus the two polynomial identities
\[
                 \phi(a)x=\phi(b),\qquad
                 \phi(c)\partial=\phi(e)                 \tag{1}
\]
hold. Take a finitely generated \(\mathbf Z\)-domain \(R\subset\mathbf C\)
containing the coefficients of all these elements and of \(\phi\). Invert
one nonzero PBW coefficient of each of \(\phi(a),\phi(c)\). Those denominators
then remain nonzero in every residue field of the localized ring.

After further localization we can take \(R\) smooth over a localization of
\(\mathbf Z\), and exclude \(p=2\). Such a nonempty smooth locus exists
because the generic characteristic-zero field extension is separable.
Its characteristic-p fibers are reduced. We need reduced fibers, not integral
ones: no claim is made that every \(R/pR\) becomes integral by excluding
finitely many primes. For example \(\mathbf Z[i]/p\) splits for infinitely
many primes. This distinction avoids the stronger introductory sentence in
BKK Section4; the pointwise center argument only needs reduced fibers.

### 2. The specialized fraction maps remain automorphisms

Fix a remaining closed point and an algebraic closure \(k\) of its residue
field, of characteristic \(p>2\). Use the abstract PBW Weyl algebra \(W_k\),
not its nonfaithful action on \(k[x]\). Its center is
\(Z_k=k[X,Y]\), with \(X=x^p\), \(Y=\partial^p\).

The imported center and Poisson statements give an induced polynomial map
\(\psi_k:Z_k\to Z_k\) of Jacobian one. It is dominant, hence injective.
The induced endomorphism \(\phi_k:W_k\to W_k\) is also injective:
\(W_k\) is a domain finite over its center, and central localization is a
finite-dimensional division algebra. Therefore every nonzero two-sided ideal
of \(W_k\) meets \(Z_k\) nontrivially. A nonzero kernel would contradict
injectivity of \(\psi_k\).

We can consequently extend \(\phi_k\) to \(D_k=\operatorname{Frac}(W_k)\).
The specialized equations(1), with nonzero denominators, put both \(x\)
and \(\partial\) in its image. That image is a division subring containing
the scalar field and the generators, so equals \(D_k\). An automorphism of
\(D_k\) maps its center onto itself, and this center is
\(\operatorname{Frac}(Z_k)\). Thus \(\psi_k\) is birational as well as étale.

### 3. The plane center is invertible without JC

A birational étale morphism \(f:\mathbf A_k^2\to\mathbf A_k^2\) is an open
immersion by Zariski's Main Theorem and normality of the target. Write its
image as \(U\). If the complement contained a curve with irreducible equation
\(h\), then \(h\circ f\) would be nowhere zero on affine space over the
algebraically closed field. It would be a nonzero constant. Dominance then
contradicts the nonconstancy of \(h\).

Hence the complement has codimension at least two. Restriction gives
\(k[X,Y]\simeq\Gamma(U,\mathcal O_U)\) by normality. The scheme \(U\) is
affine since it is isomorphic to the source. Taking spectra shows the inclusion
\(U\hookrightarrow\mathbf A_k^2\) is an isomorphism. Apply this to the
geometric map of \(\psi_k\). No characteristic-zero Jacobian conjecture or
positive-characteristic analogue has been assumed.

### 4. A uniform bound makes characteristic-zero descent valid

The center/Bernstein degree comparison gives \(\deg\psi_k\leq N\).
Gabber's inverse bound in dimension two gives \(\deg\psi_k^{-1}\leq N\).
Since \(\psi_k\) is invertible, the Azumaya fiber argument lifts it to
invertibility of \(\phi_k\): the induced map between equal-rank Azumaya
algebras is an isomorphism on every matrix-algebra fiber and hence globally.
The degree comparison applied to its inverse yields
\(\deg_B\phi_k^{-1}\leq N\).

To descend, write unknown elements \(U,V\) in the finite PBW span
\(\{x^i\partial^j:i+j\leq N\}\). The equations
\[
                         \phi(U)=x,\qquad\phi(V)=\partial
\]
are finite linear coefficient systems over \(R\), with output degrees at
most \(N^2\). They have solutions over every good algebraically closed residue
field by the previous paragraph.

If one system were inconsistent over \(K=\operatorname{Frac}(R)\), its
augmented matrix would have larger generic rank than its coefficient matrix.
Inverting suitable nonzero minors would preserve this discrepancy on a
nonempty open subset of \(\operatorname{Spec}R\). Such an open subset has
positive-characteristic closed points, contradicting the specialized solutions.
Both systems therefore have solutions over \(K\subset\mathbf C\). Their
solutions give polynomial preimages of the generators in degree at most \(N\).
Surjectivity and the original injectivity prove the statement.

## Replay, controls, and limitations

Desk-only. No CAS, chosen-prime experiment, numerical evidence or computed
inverse is used. The two Ore identities, nonzero denominator coefficients,
center map, and bounded linear systems are the explicit specialization maps.
The co-check independently attacked those steps and the birational-étale
endpoint. Same-model agreement does not satisfy the promotion gate.

Two meaningful premise checks prevent stronger readings:

- In characteristic \(p\), \((X,Y)\mapsto(X-X^p,Y)\) has Jacobian one but
  field degree \(p\), so is not birational and is not covered by Step3.
  Jacobian one alone must not replace the rational-inverse premise.
- Conjugation by \(x\in D^*\) sends \(\partial\) to
  \(\partial-x^{-1}\). It is rationally invertible but fails the polynomial
  image premise. A division-ring automorphism alone is insufficient input.

This closes only the stated rational-automorphism construction attempt at the
producer-checked tier. A proper first-Weyl endomorphism would need a genuinely
non-surjective division-ring extension; none is constructed here. Arbitrary
plane Keller maps have not been placed in this class. JC2 remains unresolved.
Before promotion or any load-bearing descendant, obtain a different-model
hostile review of the sealed statement and its named imports. No broader
classification, low-degree search or family successor is selected here.

## OPENS RAISED

None. The unresolved general conjectures are not reissued as bounded tasks.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9387`.
- Body SHA-256:
  `a881066ea2b79cef0d4c3a19e199042a1a25695af8a85e97a1e8af3909ccb3ab`.
- Frozen basis: `3343285b4130cb0ad953e803aec3ccf548532aaa`.
