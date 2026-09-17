# Hostile review: integral back coordinates and elliptic multiplication

Reviewer: native Sol seat, swarmHQ; recorder: ROOT.
Date: September 17, 2026 UTC.
Basis: 3b8bc380acda08cf1217a493e080acc465e50186.
Evidence: MANUAL hostile review with named classical imports.
Verdict: CONFIRMED at the exact scope below.

This is ROOT's transcription and synthesis of the terminal native review,
not a verbatim execution log or a reviewer-authored filesystem artifact.
The requested reviewer seat differs from the producer's Astra seat;
exact hosted model identifiers were not independently exposed. Identity
is not mathematical evidence. Authoritative task status was COMPLETED
before collection, including the wording correction recorded in section 4.

## 1. Frozen input and read scope

[Producer: integral back coordinates obstruct rational Keller donors](integral-back-coordinate-donor-swarmHQ-root-20260917T161200Z.md).

- Full SHA256: a4167d78bfd3ab02fcea6d4bbb3bf426fd19a7a84dc77c413b06a3764725da5d.
- Body SHA256: a4cb7c23123c2dc4eb6e6d1401d7d0c5d1a08dfd8922e4c4c212b6ad95b54061.
- Manifest SHA256: 3342c40418f86ecb7b5c1501d50cd69aaa2cab2a0556c9bbbe60e6279c5018c3.
- Producer contribution: 3b8bc380acda08cf1217a493e080acc465e50186.

Reviewer read the whole producer, manifest and FALLACY-v2, and reported
unchanged pre/post pins, read-only modes and passing custody verification.
Selected comparison reads covered the fixed-source quotient review
section D, the isotrivial multiplication entry in notes.md, and the
Legendre producer/review; no complete historical-corpus audit is claimed.
Reviewer independently spot-checked the named primary division-polynomial
and elliptic references. Standard normality, etale openness, and finite
etale triviality of complex A2 remain explicitly named classical imports.
No CAS, numerical evidence, scientific Python or proof assistant was used.

## 2. Criterion: checks and verdict

Let G=(p,q) be rational on A2 with J(G)=c in C*, and assume BOTH original
coordinates x,y integral over A=C[p,q]. For any dominant rational sigma,
if H=G composed sigma is polynomial Keller on the whole source A2, then
sigma is polynomial Keller and G is a polynomial automorphism.

The hostile checks support all five steps:

1. Pulling back each monic equation gives integrality of the corresponding
   coordinate of sigma over the actual polynomial source ring. Normality
   of that ring, not merely a function-field argument, makes sigma
   polynomial. Dominance supplies the injective substitution used here.
2. The rational chain rule gives J(H)=c*J(sigma). The nonzero CONSTANT
   hypothesis on c therefore makes sigma etale on the entire plane.
3. Etaleness makes its image open. An omitted irreducible curve b=0
   would make b composed sigma a nowhere-zero polynomial, hence a
   nonzero constant, contradicting dominance. The complement is finite.
4. For a reduced donor coordinate a/b, choose a point on a denominator
   component outside both the numerator zero set and that finite
   complement. Evaluating a(sigma)=b(sigma)*H_i at a preimage contradicts
   the choice. Genuine donor poles cannot disappear; both p,q are
   polynomial. This is the previously reviewed cofinite-pole lemma with
   a new integrality-to-polynomial-etale bridge, not dominance alone.
5. The two integral generators make C[x,y] finite over A. Polynomial G
   is finite etale, hence an automorphism by triviality of connected
   finite etale covers of the complex affine plane.

The conclusion does NOT assert sigma invertible. Even an automorphism
donor leaves any unresolved Keller problem of sigma unchanged.

The negative control is valid: G=(x,y/x), sigma=(s,s*z), H=(s,z).
Both back coordinates lie in A, but J(G)=1/x and J(sigma)=s. This tests
why constant J(G) cannot be dropped. Automorphism donors provide the
positive control.

## 3. Elliptic application: checks and verdict

For every fixed a in C and t=y^2-x^3-a*x, consider multiplication by m
on the generic smooth E_t: Y^2=X^3+a*X+t. For EVERY integer |m|>=2,
write G_m=(U_m,V_m)=[m](x,y). The reviewer confirms:

- Generic smoothness follows from the nonzero discriminant polynomial;
  no assertion requires every closed fiber to be smooth.
- t=V_m^2-U_m^3-a*U_m is in the actual output ring A_m=C[U_m,V_m].
- The relative invariant differential identity, wedged with dt, gives
  dU_m wedge dV_m=m*dx wedge dy, so the rational Jacobian is constant m.
- For n=|m|, the division-polynomial numerator phi_n is monic of degree
  n^2 in its independent X variable, while Psi_n=psi_n^2, after eliminating
  Y^2, is polynomial of degree n^2-1. Thus phi_n(T;a,t)-U_m*Psi_n(T;a,t)
  is MONIC over A_m and vanishes at x. The leading coefficient n^2 of
  Psi_n is standard but is not needed: only the degree drop is used.
- Even n is included: retain the 2Y factor before squaring. In particular
  Psi_2=4*(X^3+a*X+t) has degree three, not one.
- y is integral over A_m[x] from y^2=x^3+a*x+t, hence integral over A_m
  by transitivity. No localization is substituted for whole-ring integrality.
- A nonzero n-torsion point on the geometric generic curve lies in its
  affine part and maps to O. Pullback of the target X coordinate has a
  genuine pole there. Thus U_m cannot be polynomial in original x,y.

The criterion excludes EVERY dominant rational source substitution
making this fixed donor pair a whole-plane polynomial Keller pair.
Negative m only changes the V sign; rescaling V by 1/m changes neither
output ring nor exclusion. Orders m=1,-1 are correctly left out.

Primary import spot-checks: Naskrecki--Verzobio,
[Common valuations of division polynomials, section 2(A)--(C)](https://doi.org/10.1017/prm.2024.7),
and selected multiplication/torsion/invariant-differential statements in
[Milne, Elliptic Curves, second edition](https://www.jmilne.org/math/Books/EC2.pdf).
No whole-book or valuation-theorem audit is claimed.

## 4. Correction before freezing this review

The reviewer's initial terminal message misstated an intermediate wedge
identity. ROOT pointed out that the correct identity is

    (dU/(2V)) wedge dt = m*(dx/(2y)) wedge dt.

Using dt=2V*dV-(3U^2+a)*dU=2y*dy-(3x^2+a)*dx gives directly
dU wedge dV=m*dx wedge dy. The reviewer explicitly confirmed the
correction, stated that it affects its review wording only, and retained
the CONFIRMED verdict with unchanged scope and assumptions. The producer
already contains the correct divided-form argument and was not modified.
The correction was collected from a separately completed follow-up before
this review was frozen. It is not a repaired producer proof.

## 5. Scope and stopping

This is INTEGRAL-BACK-COORDINATE-DONOR-1, PROMOTION-ELIGIBLE/MANUAL with
the named classical imports. It supplies neither integrality for arbitrary
Keller sources nor a conclusion that sigma is invertible. No JC2 proof or
counterexample follows.

Polynomial target automorphisms preserve the hypotheses. Arbitrary
birational target changes need not; they are NOT covered. No arbitrary
elliptic family, general isogeny, or all-donor theorem is asserted.
The a=0 exclusion overlaps the earlier isotrivial result. This argument
also covers nonisotrivial fixed a!=0 and all multiplication orders, but
does not claim literature priority. Fixed Legendre tripling remains a
separate branch-line argument.

Stop the multiplication construction. No automatic next multiplier,
parameter, target repair, normalization calculation or coefficient farm.

## OPEN(S) RAISED

None. The general actual-source integrality/properness gap is unchanged.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7692`.
- Body SHA-256:
  `2b5e59281697f5ffc668ac94d74a84f0877443ed23963d2fe2370c6488a33d06`.
- Frozen basis: `3b8bc380acda08cf1217a493e080acc465e50186`.
