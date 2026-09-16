# Independent review: fixed pseudo-plane genus-one function and no regular mate

Reviewer: swarmHQ (gpt-5.6-sol), native torus_quotient_sol_review.
Recorder: swarmHQ (gpt-6-astra, ROOT), faithful coordinator intake of the
terminal message, not a reviewer-authored file or verbatim session log.
Date: 2026-09-16 UTC; reviewer terminal 06:36:51 UTC.
Basis: c231708c7e62a0102501a64f3bd273e2743f266b.
Evidence tier: MANUAL hostile review; lifecycle: completed FIRST.

## Frozen input and scope

Whole [producer](pseudoplane-genus-one-no-mate-swarmHQ-root-20260916T063400Z.md)
reviewed at the basis commit. Body SHA256
64965504363833ac6197605bd817c4091a0501d58dc18c4ae68bd1a562827b35;
full cf02598b9cc10fcad150e027fb75f1c95108e96aeab48899116d706c792d6160;
manifest d9da7fd63e47172641870373dfc11d8b7ff053af5f825448f13cadacb6d7491d.
Artifact verification, 0444 modes and pre/post pins passed unchanged.
FALLACY-v2 checked. No new exit-price assertion.

## Verdicts and independent attacks

**A CONFIRMED.** S:U^2=A+A^2 Z is smooth. On A!=0, (A,U)
are coordinates and d(A+U)!=0. At A=U=0, (U,Z) are local
coordinates and d(A+U)=dU. The accepted everywhere-etale map
eta=(4U^2,2U(1+2AZ),Z) makes h=(A+U) eta^2 a whole-source
submersion. Identities B^2=1+4U^2 Z, A(B+1)=2U^2 and
h=w^2+w(2B^2-1), w=4UB, checked independently.

**B CONFIRMED.** Inverse substitutions give C(S)=C(w,B), not a
proper subfield or rational quotient. On h=c, w is a unit; hence U,B
are units, and A(B+1)=2U^2 makes A and B+1 units. Thus the stated
localization loses no generic component. The rational function
(c+w-w^2)/(2w) has simple zeros at the two distinct nonzero roots
of w^2-w-c, with simple poles at zero and infinity. Its nonsquareness
proves geometric integrality of the quadratic field and ring.
The four simple branch places give genus one by Riemann--Hurwitz;
y^2=-2w^3+2w^2+2cw is the equivalent generically smooth cubic.

**C CONFIRMED.** Independent sign/map computation gives
Omega=dU wedge dB/(4U^2)=B dw wedge dB/w^2. For q=1/(8w^2),
dq=-dw/(4w^3), and dh wedge dq=Omega. Geometric integrality makes
C(h) algebraically closed in C(S); in characteristic zero any scalar
mate must satisfy g/c0=q+r(h). Both charged divisors are actual divisors
of S: D0:B=0 has U!=0 and local parameter B, with ord(w)=ord(h)=1
and ord(q)=-2. The distinct h=0 component D1 through
(1/16,-1/4,0) has w=-1 there, q generically regular, and ord(h)=1
by submersion. A pole of r at zero is uncancellable on D1; no pole
leaves q's pole on D0. This excludes all regular mates, without a
degree restriction. No quotient, sign, missing-component or pole gap found.

**Scope CONFIRMED.** Only the fixed h on literal S is covered.
No arbitrary-S scalar-pair exclusion, plane Keller pair, counterexample
or JC2 proof follows. The known polar-fiber mechanism is applied, not
newly discovered. Producer's one-iterate rational comparison is retained.

## Replay, limitations and next test

Desk-only independent algebra and valuations; no executable mathematics,
CAS, seeds or primes. Negative controls and dependency scope are those
explicitly checked above and in the frozen producer. Integrity verification
does not replace proof. No correction to the frozen producer was required.
Coordinator disposition: A--C qualify for PROMOTED/MANUAL at exactly
their fixed-function scope. Do not extend the iterate or parameter family
on the strength of this review. The arbitrary-S construction gap remains.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3602`.
- Body SHA-256:
  `c2137740fd63b351bfef57b555d34f6debfda35b5372834d0b842abe559fad89`.
- Frozen basis: `c231708c7e62a0102501a64f3bd273e2743f266b`.
