# Exact rational area preservation does not force an invariant pencil

Producer: swarmHQ coordinator (Codex; hosted model identity not independently attested).
Date: September 20, 2026 UTC.
Basis: `339707ae305f39b08920849e5c7ce100736093bf`.
Evidence tier: MANUAL, with the named dynamical-degree import below.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED; independent hostile review pending.

## Statement and scope

Over C, consider the dominant rational self-map

    F(x,y) = (y/(2x), y^4/(16x^4) - x^2).

It has generic degree 2 and preserves dx wedge dy EXACTLY. Its first
dynamical degree satisfies lambda1(F)>=3, whereas lambda2(F)=2.
Consequently no positive iterate F^m preserves a rational pencil: there
are no nonconstant r in C(x,y) and rational phi in C(z) such that

    r composed with F^m = phi composed with r,  m>=1.

This is a countertest to the proposed RATIONAL implication
"exact standard area plus generic degree>1 forces a rational pencil."
It is NOT a polynomial Keller map or a counterexample to JC2. It has poles
along x=0. It does not exclude invariant foliations without rational first
integrals, or prove that F preserves no finite web. Only a LOWER BOUND on
lambda1 is asserted, not its exact value.

## Dependencies and comparison

The old punctured control D(x,y)=(x^2,y/(2x)) occurs, for example, in
[the canonical polar-trace report](canonical-polar-trace-discriminator-root-20260912.md).
It preserves the pencil x. Here the different map is F=H composed with D,
where H(u,v)=(v,v^4-u) is a polynomial determinant-one automorphism.
Postcomposition is not conjugacy, and need not preserve D's pencil.

The earlier [Euclidean source-scope check](arithmetic-euclidean-global-scope-root-20260913.md)
already distinguishes classification of invariant forms from classification
of maps. Nothing below attributes a maps/pencil theorem to Diller--Lin.
The existing polynomial rational-pencil criterion is unchanged: this example
removes polynomiality, not a hypothesis satisfied by an actual JC2 map.
This is a fixed discriminating example, not a novelty claim, donor search,
or invitation to a degree/parameter family.

The named external import is Dinh--Nguyen,
[Comparison of dynamical degrees for semi-conjugate meromorphic maps,
arXiv:0903.2621v1](https://arxiv.org/pdf/0903.2621v1), Theorem 1.1.
For a dominant rational surface map preserving a pencil over P1, its formula
gives lambda1=max(a,b) and lambda2=ab, where a is the base degree and b the
relative first dynamical degree. Here a>=1, b>=1, and relative degree zero
is 1 (Proposition 3.6 and its proof). Section 3 also records invariance
under birational conjugacy, powers under iteration, and the generic-fiber
interpretation of the top degree. These are named imports, not re-proved here.

Source scope: the v1 landing records March 15, 2009; the PDF's typeset date
says November 4, 2018. This is not a new-publication claim. The opening
hypotheses/Theorem 1.1, selected Section 3 definitions and the stated
properties were checked. Retrieval also exposed neighboring current-theory
paragraphs. This is NOT a whole-paper or dependency-proof audit, and no raw
PDF-byte hash is claimed. No Diller--Lin body was reacquired for this test.

## 1. Exact area and generic degree

The matrices for D and H are

    dD = [[2x, 0], [-y/(2x^2), 1/(2x)]],
    dH = [[0, 1], [-1, 4v^3]].

Both determinants are 1. Hence det dF=1 in C(x,y), equivalently
F*(dx wedge dy)=dx wedge dy. H^{-1}(s,t)=(s^4-t,s).

Writing p=x^2 and q=y/(2x), we have y=2qx and x^2=p. The element p is
not a square in C(p,q), since its valuation at p=0 is odd. Therefore

    [C(x,y):C(p,q)]=2.

The polynomial automorphism H does not change the output field, giving
lambda2(F)=2. Alternatively, the generic pair of source points (x,y) and
(-x,-y) has the same image. The field computation also establishes that
there are exactly two generic points, rather than just at least two.

F is regular and etale on {x!=0}, but that open is NOT asserted forward
invariant. All iterates below are rational maps, defined on their dense
domains, or equivalently substitutions in the function field.

## 2. A useful birational conjugacy

Set

    T(x,y)=(u,v)=(x,y/(2x)),   T^{-1}(u,v)=(u,2uv).

Direct substitution gives

    G = T composed with F composed with T^{-1},
    G(u,v) = (v, (v^4-u^2)/(2v))
           = (v, v^3/2-u^2/(2v)).

T is birational, not a claimed polynomial or symplectic coordinate change.
The area statement above was established in the original x,y coordinates;
only the birationally invariant dynamical degrees are transferred using T.
For reference, T^{-1}*(dx wedge dy)=2u du wedge dv, consistently with
det dG=u/v and G*(2u du wedge dv)=2u du wedge dv.

## 3. All-iterate degree-growth lower bound

On C[u,v], give u weight 1 and v weight 3. Let delta of a nonzero
polynomial be its largest monomial weight; on C(u,v)^* put
delta(P/Q)=delta(P)-delta(Q). This is well-defined because weighted
degree is additive under multiplication. It satisfies

    delta(A+B)=max(delta(A),delta(B)) if delta(A)!=delta(B).

Write G^n=(u_n,v_n), including u_0=u and v_0=v. We claim

    delta(u_n)=3^n,   delta(v_n)=3^(n+1).

The assertion holds for n=0. If it holds for n, then u_(n+1)=v_n, while

    v_(n+1)=v_n^3/2-u_n^2/(2v_n).

The two summands have delta-values 3^(n+2) and
2*3^n-3^(n+1)=-3^n. They differ strictly, so their leading terms cannot
cancel. This proves the induction for EVERY n, without symbolic iteration
or a numerical growth fit.

Let d_n be the projective algebraic degree of G^n on P2. A homogeneous
triple of degree d_n representing G^n gives, after setting the source
homogenizing coordinate to 1, a representation v_n=P_n/Q_n with both
ordinary polynomial degrees at most d_n. The denominator is nonzero.
Since the weights are positive,

    delta(v_n)=delta(P_n)-delta(Q_n)
               <= delta(P_n) <= 3*d_n.

Here delta(Q_n)>=0; cancellation of common factors does not affect the
difference. Thus d_n>=3^n. Taking nth roots in the definition of the first
dynamical degree yields lambda1(G)>=3, hence lambda1(F)>=3.

This argument does not claim d_n=3^n or lambda1(F)=3. It avoids the
frequent error of reading exact rational-map degree from uncancelled
coordinate expressions.

## 4. Exclusion of rational pencils, including iterates

Suppose F^m preserved a nonconstant rational pencil r. It would give
dominant meromorphic maps P2 to P1 and phi:P1 to P1 satisfying the exact
semiconjugacy required by the named product formula. Its hypotheses do
not require polynomiality or a connected generic fiber of the pencil.

For any such surface semiconjugacy, the formula and a,b>=1 give

    lambda1(F^m)=max(a,b) <= a*b=lambda2(F^m).

But the checked iterate rule and Sections 1--3 give

    lambda1(F^m)>=3^m > 2^m=lambda2(F^m),

a contradiction. Thus no positive iterate admits the stated pencil.

## Replay, checks and excluded stronger readings

Desk-only. The displayed Jacobians, field extension, rational conjugacy,
strict weighted-degree induction and product-formula attachment constitute
the replay; no CAS, randomized search, primes or experimental degree fits.
The meaningful comparison is the OLD D itself, whose pencil x is explicit;
passing to H composed with D is precisely the changed test, not a claim
that a source or target automorphism preserves dynamical degrees separately.

FALLACY checks: field maps and coordinate change are explicit; determinant
one does not remove poles; degree lower bound is not an equality; the
topological and first dynamical degrees are distinguished. There is no
exit-price assertion. The example does not become polynomial because H is
polynomial, nor does its regularity on an open make it a whole-plane map.

Pre-input SHA256 pins:

    AGENTS.md 31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f
    COORDINATION.md 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e
    APPROACHES.md 127a838cbd9b77ef3b82905250f0355ca9e1acc0a8149537959b4ad71b1f7f1e
    FALLACY-v2.md e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5

## Limitations and next test

Independent hostile review should attack the rational conjugacy, the
strict all-iterate weighted bound and each hypothesis of the named
product formula. No claim is promoted here. The already-open polynomial
source problem remains: a proof needs a genuinely polynomial-source
argument, or another global premise not provided by exact area alone.
No foliation/web exclusion, new construction family or automatic source
classification sequel is proposed.

## OPENS RAISED

None. This report records a fixed countertest, not a new open-ended queue.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

This trusted checker output is not a novelty or mathematical verification.
Whole proof readback and post-input hash check completed September20
21:19:10 UTC; all four displayed input pins matched. No computational
verification, independent review, or broader classification is claimed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9088`.
- Body SHA-256:
  `7f8131d6300255fea6d894ee79e32a35a5980fb47091f925b6a1449850c59b61`.
- Frozen basis: `339707ae305f39b08920849e5c7ce100736093bf`.
