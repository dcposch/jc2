# GENERIC1835: local exclusion of a divisorial fixed valuation
Author: retained Astra, co-research (not independent review). Launch89c9da0f2ec8c2941a78c518ecbb195d21ceb6de. INTERNAL pending review.

## Statement and scope
Let G:(C²,0)->(C²,0) be holomorphic, G(u,v)=(u^d a(u,v),u^p b(u,v)), where d>=2,1<=p<d and a,b are units. Assume G*(u^(-3)du∧dv)=u^(-3)du∧dv as meromorphic forms. Then no divisorial valuation ν centered at0 satisfies ν(f∘G)=dν(f) for all meromorphic germs f.
Here divisorial means a positive multiple of the order of an exceptional prime on a finite succession of point blowups of the smooth germ. This is the usual smooth-surface divisorial realization; the proof uses it explicitly. The conclusion is local only: no global eigenvaluation selection, classification of infinitely singular valuations, JC2 conclusion or external-source theorem is asserted.

## 1. Analytic triangular normalization, constructed directly
DG(0) is nilpotent: its only possible nonzero entry is the lower-left entry when p=1. Choose a complex vector-space norm in which its operator norm is less than1, then a small ball on which G is a strict contraction and maps the ball into itself. Shrink again so a has a holomorphic logarithm A.
The series L=Σ_(k>=0) d^(-k-1) A∘G^k converges normally: A is bounded on a slightly larger invariant ball and d>=2. It satisfies dL=A+L∘G. Set z=u exp(L); then z∘G=z^d, and (z,v) are holomorphic coordinates since exp(L(0)) is nonzero.
In these coordinates u^(-3)du∧dv=z^(-3)h(z,v)dz∧dv with h a holomorphic unit. Indeed u=z times a unit and ∂u/∂z is a unit. Define w(z,v)=∫_0^v h(z,t)dt. This is a holomorphic coordinate, w(z,0)=0, and the form is exactly z^(-3)dz∧dw.
Write G in these coordinates as (z^d,W(z,w)). Preserving the form gives d z^(-2d-1)∂W/∂w=z^(-3), hence ∂W/∂w=d^(-1)z^(2d-2). Therefore
    G(z,w)=(z^d, P(z)+d^(-1)z^(2d-2)w).
P is convergent and ord_z P=p. To check the latter, on w=0 one has v=0 and u=z times a unit; the output original v-coordinate is u^p b(u,0), while w at the output equals that v-coordinate times a unit. Thus the lowest order is unchanged. This construction invokes no normal-form classification.

## 2. The finite-prefix fact needed for a divisorial valuation
Suppose such a ν exists. Scale it to its primitive integral order on K=Frac C{z,w}; write v for that order and m=v(z)>0. Also v(w)>0. Its residue field is C(E)=C(q): the prime E is a rational exceptional curve created by a point blowup, and subsequent blowups do not change its function field.
Analytic coordinates are not identified with a global rational field. The analytic coordinate isomorphism preserves this local K. If the eigenrelation was initially stated on rational functions in u,v, it extends to convergent germs by Taylor truncation: positive v(u),v(v) and positive v(u∘G),v(v∘G) make both truncation remainders arbitrarily large. The same truncation observation preserves residue classes of fractions whose numerator and denominator have finite value.
For clarity the elementary completion facts used below are: a complete DVR has a unique extension of its valuation to any finite field extension; an embedding of fields extends to an algebraic closure. Uniqueness follows from Henselianity (the integral closure is local), and Henselianity here follows by convergent Newton lifting in a complete DVR. These basic valued-field facts, not a valuation classification or an external cited result, are the only lifting inputs.
The completion Khat can be written C(q)((t)): lift a residue generator q to a unit of K, choose a uniformizer t, and recursively subtract lifted residues to expand any element. The lifted rational functions C(q) form a coefficient field. We retain C as its given constant field.
Write z=t^m a with a a unit. Adjoin an m-th root of its residue, then lift the root of a by the characteristic-zero binomial/Hensel expansion. Thus L=Khat(z^(1/m)) is unramified over Khat, with finite residue extension k'/C(q), and τ=z^(1/m) is a uniformizer. Choose the lifted coefficient field k'; expanding in τ gives w=Σ_(j>=1) a_j τ^j with a_j∈k'.
There is a first coefficient a_k not in C. Otherwise z=τ^m and w∈C[[τ]], and every nonzero convergent germ f(z,w), hence every fraction of two such germs, has constant leading coefficient. Substitution converges in the valuation topology since v(z),v(w)>0. The residue field of K would then be C, contrary to C(E)=C(q).
Put r=k/m and s(z)=Σ_(j<k) a_j z^(j/m). Then
    w=s(z)+z^r η,     v(η)=0,     residue(η)=a_k∉C.
Here s is a FINITE Puiseux polynomial with positive exponents less than r. The residue a_k is transcendental over C because C is algebraically closed. This argument proves exactly the finite-prefix assertion used; no infinite-essential-prefix theorem is invoked.

## 3. Lifting the eigenrelation without identifying conjugate prefixes
Let σ=G*:K->K. It is injective because the preserved form gives a nonzero Jacobian off z=0. The hypothesis is v(σ f)=d v(f). Thus σ extends continuously to Khat as an embedding, with the same scaling.
Extend that field embedding to L inside an algebraic closure of Khat. Since σ(z)=z^d, the image of τ is ζτ^d for some m-th root of unity ζ∈C. Consequently σ(L)⊂L. The pulled-back valuation v_L∘σ is an extension of d v on Khat; uniqueness for the complete DVR gives v_L(σ x)=d v_L(x) for all x∈L.
In particular σ induces an injective map on residue fields fixing C. Hence residue(ση) remains transcendental over C. No assumption that σ preserves our chosen coefficient field is needed. Applying σ to the finite-prefix expression gives
    σw=Σ_(j<k) a_j ζ^j z^(dj/m) + ζ^k z^(dr) ση.
Its first coefficient outside C occurs at exponent dr. Earlier coefficients lie in C, and the coefficient at dr is transcendental; later terms cannot affect it. On the other hand the exact triangular identity gives
    σw=P(z)+d^(-1)z^(2d-2)s(z)+d^(-1)z^(2d-2+r)η.
Its first coefficient outside C occurs at exponent 2d-2+r. P has only integral powers with constant coefficients; adding any constant at that exponent cannot cancel a transcendental coefficient. Both expansions use the same uniformizer τ and coefficient field k'. Therefore dr=2d-2+r, so r=2.
This also addresses root-of-unity choices: they change the nonzero constants ζ^j, not the support or transcendence of the first nonconstant term.

## 4. Finite fractional support gives the contradiction
The normalized z-order v(σw)/m is p: P has z-order p<d, whereas z^(2d-2)w has normalized order greater than 2d-2>=d. Thus d v(w)/m=p. Since r=2, the finite prefix s has a nonzero leading term of exponent p/d, strictly between0 and1 and nonintegral.
Let q be the largest nonintegral exponent in s; this exists because s is finite, and q<2. Compare the two expressions for σw at exponent b=2d-2+q<2d. The right-hand side has a nonzero coefficient there from the unique q term of s. P cannot contribute because b is nonintegral; the remainder starts at2d. No cancellation is possible.
On the left, all terms below2d come from the finite prefix. A term of exponent b requires an exponent q'=b/d=(2d-2+q)/d in s. Since b is nonintegral, q' is nonintegral, and q'-q=(d-1)(2-q)/d>0. This contradicts maximality of q. The assumed divisorial eigenvaluation does not exist.

## Qualifications and custody
The proof uses convergent holomorphic coordinates and the completed DVR of a divisorial prime. It does not claim those coordinates are rational or polynomial. It applies to all analytic germs with the displayed hypotheses, not merely a polynomial model; the finite local germ degree is not identified with a global mapping degree.
No source body was accessed. The named smooth-surface divisorial realization and elementary complete-DVR algebra are explicit foundational scope; no FJ selection, properness, infinitely singular classification or general norm/trace theorem enters the local proof. ROOT's separate global selection argument has not been independently reviewed here.
Own inputs: new wholeSTATE200; old minimization report119 whole; selection/history27; permitted dynamics routing325-334; exact-pinned own governors1304 reused. Initial metadata script used bytes.splitlines on a PDF and failed against the mandatory LF count; ROOT clarified the convention, the exact LF recheck passed with unchanged bytes/hashes, and the error is retained in receipts. Source0 remains intact.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8504`.
- Body SHA-256:
  `19916b8910fb5f38dda005aec75696c5ae6bb525662844913622b76de0e97203`.
- Frozen basis: `89c9da0f2ec8c2941a78c518ecbb195d21ceb6de`.
