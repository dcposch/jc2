# Common squarefree receivers to the unequal interface: a scoped map discriminator

Status: TERMINAL DESK / NO COMPLETE TRANSFER. September 8, 2026. Only the accepted minimal-receiver composition is a mathematical input. No pending odd/nonodd, cone, golden or other review is a premise. No source expansion, high polynomial powers, solver, CAS, remote work or new lane.

## Result and exact scope

For common_3, the natural divisor/top-preserving triangular polynomial source transformations cannot reach the unequal bounds. The tempting Laurent root-centering has a genuinely unavoidable pole. For common_4, polynomial root-centering is valid, but it does **not by itself** establish the full unequal weight bounds. The first missing arrow is that the remaining forbidden coefficients vanish as a consequence of ALL Jacobian equations. No such implication is established here; no receiver point or exclusion is claimed.

Write H=p²(p³+g³), w(g)=5,w(p)=-7, and normalize the guarded target top scalars so A_15=H³, B_25=H⁵. The source has [A,B]=c g², c nonzero. The unequal target interface requires w(A)<=3,w(B)<=5. Common faces, with mu nonzero, are powers of G3=g(gp-mu)² or G4=g³(p-mu)². All these data are taken literally from the accepted report, not identified by degree alone.

## 1. Tested transformation class

Consider source polynomial automorphisms preserving the Jacobian divisor {g=0}, and triangular target changes preserving the ordered degrees 15,25. A source automorphism has first coordinate a*g (a unit): pullback of g² must be a scalar multiple of g². Its second coordinate is b*p+f(g), b a unit; invertibility over K[g] forces p-degree one and constant leading coefficient. If deg f>1, the unique monomial p^15 produces a unique term of degree 15*deg f, exceeding15. Thus f=d*g+e. The unique multiplicity-two projective factor p of H forces d=0 if the outer form is preserved up to scalar. Comparing the two terms of H then gives a³=b³. These arguments hold in characteristic zero, over an algebraic closure if needed; the displayed transformations themselves remain same-field when their parameters lie there.

Thus this natural class reduces to g_old=a*g, p_old=b*p+e, a³=b³, with independent target scalings and translations. Before target rescaling its Jacobian scalar is c*a³*b. After monic rescaling it remains a nonzero scalar. The triangular output freedom at these ordered degrees is A'=u*A+constant, B'=v*B+t*A+constant: nonlinear powers of A have degree at least30. In particular these output operations cannot remove a forbidden nonconstant coefficient of A. We do not classify arbitrary composite source/target operations that change intermediate degrees, nor noninvertible or birational maps with separate cancellation hypotheses.

## 2. Common_3: concrete obstruction

The exact common_3 polygon has g-degree9 and its g^9 coefficient is precisely p^6. To obey w<=3 after the above substitution, this coefficient must still be a scalar times p^6. Its transform is a^9(bp+e)^6, so e=0. But then the original nonzero g^3 p^0 coefficient mu^6 survives, with weight15>3. Scaling or translating the target A cannot remove it.

The direct attempt to center gp-mu instead uses p_old=p+mu/g. It has determinant1 in the Laurent ring and fixes the monomial Jacobian, but is not polynomial on A. For a supported monomial g^i p^j, the most negative possible g exponent after substitution is i-j. Since i+j<=15, exponent -15 can only come from (i,j)=(0,15). Monicity makes its Laurent coefficient exactly mu^15, nonzero. Hence A acquires the unavoidable term mu^15*g^-15. The inverse-sign centering has the same obstruction with its corresponding nonzero sign. This rules out this literal Laurent substitution, not every birational transformation or a different incoming cut.

## 3. Common_4: a valid face normalization, not a full transfer

Here the exact g^9 and g^15 coefficients are (p-mu)^6 and (p-mu)^10. The necessary centering is e=mu, giving p_old=b*p+mu. With b=1,a=1 it is the polynomial automorphism p_old=p+mu, inverse p=p_old-mu. It preserves the total tops H³,H⁵ and [A,B]=c*g² exactly and turns both highest-g coefficients into p^6,p^10. Target constants may be reset afterward. It need not preserve odd parity or a separate lift normalization; neither is required or asserted in this task.

The missing assertion is stronger: after centering one needs every coefficient with 5i-7j>3 in A, and >5 in B, to vanish. Fixing the highest-g coefficients alone does not do this. An exact degree-five support/face control is

    R=H+g³((p-mu)²-p²)+g².

Its total top is H, its highest-g coefficient is (p-mu)², and its support lies in the primitive common_4 polygon. Formally A=R³,B=R⁵ therefore have all required common_4 outer and inner faces and polygon envelopes (no powers were expanded). After centering,

    R'=(p+mu)^5+g³p²+g²,

so w(R')=10, w(A')=30,w(B')=50. Weighted leading terms cannot cancel in these powers over a field. This is **only a commuting support/face control**: its Jacobian is zero, not c*g². It proves neither that a genuine receiver evades the centering transfer nor that the transfer is impossible. It identifies precisely why an additional full-Jacobian theorem, not another coordinate substitution, would be needed. No such theorem was supplied by the sole accepted input or derived in this bounded task.

## Evidence and stop boundary

Whole accepted source read: xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md, SHA256 7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413. Its common-face and scaling sections supply all exact data above. Named history searches in APPROACHES.md, AUDIT.md and ladder/REDUCTION.md found the already recorded three faces/scaling (AUDIT entry near18461), but no exact common-to-unequal polynomial transfer under the searched names. This limited checksum is not a novelty census. No live report, gate or protected project was consumed.

Owned standard-library controls evaluate only R of degree5, primitive coefficient shifts, single-monomial Laurent index bounds and a scalar Jacobian factor. Eight normal/-O modes include actual changed shift sign, omitted g² coefficient and dropped mu guard; all changes fail the same verifier. No Assert statements. Each subprocess has 30s wall,25s CPU,512MiB limits. Exact witness bytes are written directly, not through a numeric JavaScript roundtrip. Custody pins the whole source, report and owned artifacts after transactional publication; all writers finish before handoff. No performance, properness, full-source coverage or JC2 claim. STOP / IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6674`.
- Body SHA-256:
  `a2d9e631c2dcc13109c8c73c14fcea750e1a36f1c75042ce28638db1efb84408`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
