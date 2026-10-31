# One-step monomial polynomialization review

Status: FINAL BODY; seal appended only by the pinned verifier.
Verdict: PASS_CONDITIONAL.
Review completed UTC: 2026-10-31T00:28:16.619488+00:00
Configured model: gpt-5.6-sol. Hosted identity: UNVERIFIED.
Candidate: CANDIDATE.md, SHA-256 78ceadc10bc09672b823cfe3a09610985e0b393e763ef557d9c8042bd4dbbba7.
Frozen public basis: aadc008ce5982630c79fa844a7f18d6bcad61f7d.

## Meaning and scope of the verdict

The derivation in CANDIDATE.md survives hostile review provided exactly the finite-normalization/omitted-A1 package stated at lines 24-30 is assumed. I did not re-prove, source-audit, or promote that package. The verdict does not make the obstruction unconditional.

The conclusion is only for one target step M_k, for an arbitrary integer k, bracketed by arbitrary polynomial target automorphisms, followed on the source side by an arbitrary dominant rational substitution. It does not cover a sequence of nonpolynomial target steps, classify the birational symplectic group, produce an actual Keller donor, prove JC2, or assess novelty.

## Independent implication checks

1. Fixed donor and finiteness (lines 34-47): PASS.

The displayed degree-eight monic equation makes u integral over C[P,Q]. The displayed monic quadratic then makes v integral after adjoining u, so the finite-type algebra C[u,v] is integral, hence finite, over C[P,Q]. Direct expansion gives J(P,Q)=6v^2 and

    Q^2-64P^3 = v^3(9v+8u^3).

On E={v=0}, P=u^4 and Q=8u^6, so the cusp normalization P=t^2, Q=8t^3 pulls back by t=u^2. At the generic point of E, 9v+8u^3 is a unit; the cusp divisor therefore has pullback order 3. Equivalently, the characteristic-zero different formula agrees with the Jacobian order 2, giving normal ramification index e=3. The residue degree two implicit in t=u^2 is not confused with this transverse index.

2. The integer k=0 (lines 52-63): PASS.

M_0 is the identity. If G is polynomial, applying the polynomial inverse of Psi composed with Phi makes P after theta and Q after theta polynomial. The two monic equations put U=u after theta and V=v after theta in the integral closure of C[x,y] inside C(x,y), hence in C[x,y]. Dominance makes V nonconstant. The chain rule gives a nonzero scalar times 6V^2 J(U,V); a product of polynomials containing the nonunit V^2 cannot be a nonzero constant. No regularity or birationality of theta was inserted.

3. Arbitrary target automorphisms and every nonzero k (lines 65-83): PASS.

For an arbitrary polynomial automorphism Phi, both restrictions A(t),B(t) are nonconstant. If one were constant, the closed irreducible curve Phi(S) would equal a coordinate line, contradicting preservation of the cusp singularity. Thus the generic point lies in the torus, where M_k has inverse M_(-k), and the image curve still has function field C(t).

For k>=1, A^(k+1)B^k has a pole at infinity. At a finite zero of A, the other coordinate has order

    -k ord(A)+(1-k) ord(B) < 0.

For k<=-1, A^(-k)B^(1-k) has a pole at infinity. At a finite zero of B, the other coordinate has order

    (k+1) ord(A)+k ord(B) < 0.

These are distinct finite/infinite points. Since the coordinate functions generate C(t), the affine normalization is P1 with their pole set removed, hence has at least two punctures. Psi is an affine-plane automorphism and preserves that normalization. Common zeros of A and B do not spoil either strict inequality.

4. Ramification through an arbitrary dominant rational source substitution (lines 85-97): PASS.

Let K=C(P,Q), L=C(u,v), and F=C(x,y). The target birational changes identify the cusp valuation of K with the generic valuation of the final image curve because they are isomorphisms at its generic point. Dominance of theta gives a finite field extension L into F. For every prolongation W of the E-valuation,

    e(W/K) = e(W/L)e(L/K),

so 3 divides e(W/K). This uses ordinary multiplicativity in a tower of discrete valuations; it does not require theta to be regular, birational, or unramified.

Assuming the lines 24-30 package, the finite normalization for a polynomial Keller G contains the corresponding ramified height-one prime. It cannot have its generic point in the etale whole-source A2, so its reduced curve is an omitted A1. Restricting the finite normalization map gives a dominant finite morphism from that A1 to the image curve. This is exactly where, and only where, the conditional package is used.

5. Final affine-unit contradiction (lines 96-103): PASS.

Normality of A1 factors the finite dominant morphism through the affine normalization C-tilde. If C-tilde is P1 minus at least two points p,q, a rational function with divisor p-q is a nonconstant unit of its coordinate ring. Dominant pullback would give a nonconstant unit of C[z], contradicting C[z]^*=C*. The contradiction is valid without assuming the image curve itself is smooth.

## Error classification and limitations

Arithmetic errors: none found. The finiteness identities, Jacobian, cusp pullback, and pole-order inequalities all check.

Terminology errors: none material. “Affine normalization” at lines 74-75 is justified because the two coordinates have fraction field C(t); its missing points are exactly their poles.

Logical or scope errors: none found after conditioning on lines 24-30. The argument neither silently enlarges that premise nor uses it to infer a multi-step or JC2 result.

Unaudited foundations: the omitted-A1 finite-normalization package is assumed, not reviewed. No external source audit was made for the standard different formula, extension/multiplicativity of DVR valuations, centers in finite normalizations, or the universal property of curve normalization; their applications here were checked internally. The three fixed-map checks mentioned at lines 116-117 were not imported as computational evidence; the relevant identities were checked algebraically above.

Novelty is unassessed. No outside-packet collision search, source query, repository/history query, web access, example search, CAS/scientific computation, model probe, or secondary model was used.

## Reading and output audit

Preflight verified all 14 copied members, their custody metadata, and the one canonical candidate seal. Required packet bodies were displayed in 76 verified non-STATE windows totaling exactly 1711 LF and 9 verified STATE windows totaling exactly 175 LF. There were no failed, clipped, overlapping, or repeated packet windows.

The launch prompt itself embedded the same 36-LF FALLACY-v2 body later read from the required packet, so exact non-STATE body exposure including that unavoidable duplicate was 1747 LF, within the 2400-LF cap. No other repeated input LF occurred. Mutable report-body preview: 0 LF. ACK-body preview: 0 LF. The startup status JSON was metadata, not an ACK-body read. The pinned packet reader and seal helper were executed only and were not credited as human reading. The preliminary checkpoint's narrower 1711-LF statement counted packet windows only; this final accounting expressly adds the 36-LF prompt duplicate.

No theorem promotion or public-ledger change is authorized by this review.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7181`.
- Body SHA-256:
  `9543340fbd2e0a68c400fe169cf7512becc0cb3b9c5a545e1185f1074033681e`.
- Frozen basis: `aadc008ce5982630c79fa844a7f18d6bcad61f7d`.
