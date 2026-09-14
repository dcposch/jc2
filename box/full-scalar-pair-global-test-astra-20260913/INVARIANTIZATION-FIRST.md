# FIRST hostile gate: exact scalar-pair invariantization (Fable 5.1)

tag: danielewski-invariantization-gate-fable5-20260911
reviewer: Fable 5.1, different-model hostile gate of ROOT/Astra manual mathematics.
launch (actual first action, `date -u`): 2026-09-11T19:36:31Z. Publication reserve
19:45:00Z, HARD 19:48:00Z (both the 19:45/19:48 fixed limits, earlier than launch+9/+12).
First action: a short skeleton without body marker, then hash verification. Manual
mathematics only: no CAS, code, network, Git, jc2-lean, or parallel Astra report.

## Inputs (hash-verified, sha256sum matched all three expected digests)

- danielewski-invariantization-root-20260911.md, 28fb540a4bb834ad40d1aa0349b8a2458cf7665951484e4896638f18275e3189, read WHOLE.
- danielewski-two-chart-interface-root-20260911.md, 9107e171cb1db948eabae96cad8961fbc3c1ceb6b8d8ddbe442c2381caed0033, read WHOLE.
- dubouloz-palka-1701.01425v2.pdf, 41150cfda4fdf477efefc7d2ce55bc5fb49941705620b567b3333df5fe84281e, SELECTED scope only:
  pdftotext of Example 4.3, §5A/(5.1)/(5.2), Corollary 5.2, Example 5.3. Not a
  whole-paper review.

## A. Maps and exceptional loci: CONFIRMED

Own derivation. O(T)=C[x,Z]⊕tC[x,Z] (free, t²=1+x²Z). σ-invariants are a(x,Z)+t b(x,Z)
with a even and b odd in x, so O(T)^σ=C[x²,xt,Z]; the map C[A,U,Z]→O(T)^σ is injective
modulo U²−A−A²Z because both sides are free of rank 2 over C[A,Z]. σ has no fixed point
(x=t=0 contradicts t²−1=x²Z), so q is the quotient by a free Z/2: finite étale of degree
2. O(T) is generated over O(S) by 1,x,t (xt=U, x²=A, t²=1+AZ), and on A≠0, B=1+AZ≠0
(B−AZ=1) the adjoined roots are units, as ROOT states.

j lands in T: (1+2AZ)²−1=4Z(A+A²Z)=(2U)²Z. Inverse A=(t−1)/(2Z)=x²/(2(t+1)), U=x/2; I
checked A+A²Z=(t−1)(t+1)/(4Z)=x²/4 and both compositions are identities. The two
inverse opens miss exactly L₋={Z=0,t=−1}, and Z=0 forces j-image t=1. So j: S≅T∖L₋,
E=j∘q=(2xt,2t²−1,Z) is étale, 2:1 onto the open dense T∖L₋, fibres {±p}, not finite
(image not closed). E∘σ=E. L₋ is an x-line. D₋={x=0,t=−1} is different: T∖D₋≅A² via
i(x,y)=(x,1+x²y,2y+x²y²), inverse y=(t−1)/x²=Z/(t+1). T∖L₋≅S is the pseudo-plane
S(2,2,1) of Dubouloz–Palka, not A². Provenance: DP (5.2) π=(x²,y,xz) is q with
(x,y,z)=(x,Z,t); DP Example 5.3 j=(w,4v,1+2uv) composed with the target automorphism
(x,y,z)↦(2x,y/4,z) of x²y=z²−1 gives ROOT's j with (u,v,w)=(A,Z,U). Checked.

Divisor bookkeeping (own): div(Z)=L₊+L₋, div(x)=D₊+D₋, div(t∓1)=L±+2D±.

## B. Volume forms: CONFIRMED

2t dt=2xZ dx+x² dZ gives ω=dx∧dZ/(2t) on t≠0; (x,t) resp. (x,Z) are local coordinates
on x≠0 resp. t≠0, which cover T, so ω is global and nowhere zero. σ*ω=ω, so it descends.
q*(dA∧dU/(2A²)) = 2x·x dx∧dt/(2x⁴) = ω. Own extra check: on 1+2AZ≠0, Ω=dU∧dZ/(2(1+2AZ)),
and {A≠0}∪{1+2AZ≠0}=S, so Ω is global nowhere zero. E*ω=(2t dx)∧(4t dt)/(4x²t²)=2ω on
the dense open, hence everywhere. j*ω computed directly: d(2U)∧d(1+2AZ)/(4U²) =
(1+AZ)dA∧dU/(A·A(1+AZ)) = dA∧dU/A² = 2Ω, using A dZ=(2U dU−(1+2AZ)dA)/A. Consistent with
the faithfully-flat argument. Equivalence: (1)⇒(3) by j*, scalar 2c; (3)⇒(2) by q*,
scalar c'; (2)⇒(1) trivial. The invariant pair is (H∘E, G∘E/2) with scalar c; this is
precomposition, no averaging.

## C. Exact weight support: CONFIRMED

Independent proof of (1) by the monomial basis x^aZ^bt^ε, weight m=a−2b: for m<0 the
weight-m piece is x^m·span{(t²−1)^b,(t²−1)^b t : b≥k} = x^m(t²−1)^k C[t], k=⌈−m/2⌉; for
m≥0 it is x^mC[t]. This agrees with ROOT's two-chart Taylor proof and with the endpoint's
x^ε Z^k C[t]. The grading is the G_m-action (λx,t,λ⁻²Z), DP's C*-action, and E is DP's
Example 4.3 endomorphism with d=2, λ=1 (U₁=2t, T₂=2t²−1), so E* is weight-preserving;
distinct m cannot cancel. Block formula: p'_m=2^m 4^k t^{m+2k}(t²−1)^k a(2t²−1) with
m+2k∈{0,1}; checked at m=−1,−2,−3,−4. Polynomial, still (t²−1)^k-divisible, parity
p'_m(−t)=(−1)^m p'_m(t), nonzero since a(2t²−1)≠0 for a≠0. deg p'_m = m+4k+2(d−2k)=2d+m,
and 2d+m ≥ 4k+m ≥ −m > 0 for m<0. Support set of each coordinate exactly preserved, so
∃ unrestricted pair at supports (S₁,S₂) ⟺ ∃ invariant pair at (S₁,S₂), same scalar.
Note E* does not act on O(T)[x⁻¹] (E*(1/x)=1/(2xt)); the identity is in C(x,t) and the
finite sum is the unique Laurent expansion. No hidden pole.

## D. Controls: CONFIRMED

E*Z=Z (m=−2,k=1,a=1: 2⁻²·4·(t²−1)); E*(xZ)=2t(t²−1)/x=2xtZ. Bracket {H,G}=x²(H_xG_t−H_tG_x):
{x,t}=x², {x,Z}=2t, {t,Z}=2xZ, {x,tZ}=3t²−1 (both arguments anti-invariant, bracket
invariant, Reynolds gives {0,0}=0). {2xt,Z}=4t²+4x²Z=8t²−4=2E*(2t). E*y=(2t²−2)/(4x²t²)=
Z/(2t²); t=0 is a smooth reduced fibre with x,Z units there, so a genuine order-2 pole.
Injectivity of E* on O(T) (dominant) keeps a nonconstant bracket error nonconstant.
Global minimum of summed interval widths over ALL pairs is E-stable; no orbit claim is
made and none follows.

## E. Campaign consequence: CONFIRMED, one GAP of scope

i*ω=dx∧(2xy dx+x²dy)/x²=dx∧dy, so (H∘i,G∘i) is Keller with Jacobian c. A polynomial
inverse would make b(H,G) regular on T equal to y=(t−1)/x², which has an order-2 pole at
the generic point of D₋ (x uniformizer, t−1 unit). So a regular pair on T is a JC2
counterexample. No converse reduction is claimed by either report; none is proved.
Merging EXISTENCE at prescribed weight supports is licensed by C; merging function spaces
or t-degree bounds is not, and both reports say so.

GAP (scope): ROOT §5 asserts that the Newton reduction's endpoint ratio n/m and scalar
errors are preserved. Weight endpoints and bracket errors are preserved (C, D), but that
reduction report is not a charged input, so I cannot confirm what n/m denotes there.

## Strongest attack and salvage

Attacks tried: a point of L₋ in j(S) (none, Z=0⇒t=1); cross-weight cancellation under E*
(impossible, graded); odd negative m (t-power m+2k=1 absorbed); H=x with support {1}
(no mate before or after E, consistent with the endpoint's weight −2 argument); reading
E as an automorphism or as the A² chart (refuted by D). No claim exceeds the proved
implication. Weaker salvage, explicitly one-directional: an unrestricted pair with
t-degrees ≤D and weights ≤m_max yields an invariant pair with t-degrees ≤2D+m_max, so a
degree-bounded invariant search of that size dominates the unrestricted one, never
conversely. E is the d=2 member of DP's Chebyshev family; higher even d also factor
through q but are not needed.

Verdicts: A CONFIRMED, B CONFIRMED, C CONFIRMED, D CONFIRMED, E CONFIRMED with the
scope GAP above. No promotion, no charge_basis, no Seal authored here.

<!-- BODY-END -->
