# Generic univariate guarded decision by a bounded rational linear certificate

2026-09-09. NEW MANUAL THEOREM/CERTIFICATE CONTRACT, UNREVIEWED. First action18:53:46.700685UTC; controlling stop19:03:46.700685UTC. This is independent of any current univariate source reduction: no such report or gate is an input. ZERO mathematical subprocesses, actual coefficients, matrices, certificates or points computed.

## 1. Exact input scope and statement

The two current-pinned WHOLE inputs are the accepted17b leading-compression producer and its accepted gate, named with full hashes in PINS.json. The producer defines the literal degree-seven polynomial p(v), without an irreducible-factor choice. Its gate section D, using the accepted seven-orbit premise explicitly stated there, proves p squarefree. Thus

    B=Q[v]/(p(v))

is a nonzero finite-etale Q-algebra of rank7, with basis1,v,...,v^6. The gate, not the producer's historical unproved-separability paragraph alone, licenses this hypothesis. We do not reproduce or strengthen that imported premise. No claim that B is a field, has seven rational points, or is the full source ring is used.

Let f1,...,f9,q be ANY ten polynomials in B[T], each of degree at most5; zero polynomials are permitted. Put I=(f1,...,f9) and

    R=B[T,q^-1]/I.                                      (1)

Localization at the zero element is understood to give the zero ring. All nine literal generators, including zeros, duplicates and componentwise degree drops, are retained.

THEOREM. The following conditions are equivalent:

    (a) R is the zero ring;
    (b) q^5 belongs to I in B[T];
    (c) q^5=sum_(i=1)^9 hi(T)fi(T), with every deg hi<=25;
    (d) the rational matrix equation M cvec=bvec defined in section4
        has a solution in Q^1638.

If they fail, there is a rational vector lambda in Q^217 with

    lambda^t M=0, lambda^t bvec=1.                       (2)

This is an exact nonzero-quotient certificate at the generic tier of (1), not a polynomial point, a ring homomorphism or a source certificate. Conversely, (2) is impossible when (a) holds. Every nonzero R has a field-valued point in an extension of Q of degree at most35. No assertion that any actual complete source supplies the ten polynomials or their degree bounds is made here.

## 2. Saturation exponent5, including all exceptional components

Since B is finite etale, abstractly B is a finite product of number fields K_alpha. This decomposition is used only for a proof; no factorization or idempotent was computed or is required by the rational certificate. Polynomial rings, finitely generated ideals and localization commute with this finite product. R is zero if and only if every component R_alpha is zero.

Fix a field component K. If all fi vanish there, its ideal is zero. If q is the zero polynomial, its localization is zero and q^5=0 belongs to the ideal. If q is not zero, K[T,q^-1] is a nonzero domain and q^5 is nonzero, so both alternatives in (a),(b) fail. In particular, an all-zero row component is not silently discarded.

Otherwise I_K=(g), with g the monic greatest common divisor, and deg g<=5. No g needs to be computed to prove this. The localized quotient is zero exactly when g divides some power of q: indeed1 belongs to the localized ideal exactly when q^N belongs to I_K for some N. If q=0 this holds trivially. If q is nonzero, factor g abstractly into irreducibles. Each factor has multiplicity at most deg g<=5. Divisibility by a power of q is therefore equivalent to every irreducible factor of g dividing q; its multiplicity in q^5 is then at least5 and at least its multiplicity in g. This is equivalent to g dividing q^5. The converse follows by taking N=5. A constant g is a unit and causes no exception.

This proves (a)<=> (b) on every component, hence over B. The argument retains repeated roots of g: squarefreeness is required of the COEFFICIENT ALGEBRA B, not of any fi, g or q. For constant q, the same proof says that a nonzero q on a field component is already a unit, so its quotient is zero exactly when the ideal is the whole polynomial ring. Components where that constant is zero instead localize to zero automatically.

## 3. Uniform multiplier bound, without generic leading-coefficient inversion

It remains to bound an expression for q^5 whenever it belongs to the ideal. Work over one field component. If all fi=0 then q=0 by membership, and hi=0 works. Otherwise select a generator f0 of maximum degree d<=5 among the nonzero generators. This is only a componentwise proof choice; it is not a global algorithm dividing a possibly nonunit coefficient of B.

If d=0, f0 is a nonzero constant. Set h0=q^5/f0 and all other hi=0; its degree is at most25.

If d>=1, start with ANY finite ideal expression q^5=sum ai fi. For each i other than0, divide ai by f0 in K[T], writing ai=bi f0+hi with deg hi<d. Then

    q^5-sum_(i!=0)hi fi

is divisible by f0: the discarded multiples can be absorbed into its multiplier. Its degree is at most max(25,2d-1), hence at most25. The quotient h0 therefore has degree at most25-d; the other multipliers have degree at most d-1<=4. This remains true if cancellations lower the numerator degree or make it zero.

The chosen index0 and degree d may differ between components. Pad every component multiplier with zero coefficients through degree25. The finite-product isomorphism now glues each scalar coefficient into B, producing nine polynomials hi of degree at most25 over the FULL B. Thus (b)=>(c), with no branch lost and no global leading coefficient inverted. The reverse implication is immediate. The proof does not promise a single selected generator has an invertible leading coefficient over B.

## 4. Exact rational matrix and the two certificate forms

Use the fixed ordered basis1,v,...,v^6 of B. Every product is reduced by the literal accepted p(v), equivalently by its monic rational normalization; no modulus, prime or irreducible factor is substituted. Define rows by the pairs

    (k,a), 0<=k<=30, 0<=a<=6,

representing the coefficient of v^a T^k. Define columns by

    (i,j,l), 1<=i<=9, 0<=j<=25, 0<=l<=6.

The column (i,j,l) of M is the coefficient vector of v^l T^j fi(T), after exact reduction in B. The target bvec is the vector of q(T)^5 with the same reduction and ordering. Thus M has exactly

    31*7=217 rows, 9*26*7=1638 columns.                  (3)

Every column has T-degree at most30, while the target has degree at most25 and is zero in rows26 through30. Those high rows MUST remain: they check cancellation in the bounded multiplier expression. The complete rational system is exactly the coefficient comparison in (c), proving (c)<=> (d).

A UNIT certificate is a rational vector cvec of length1638. Reconstruct hi=sum_(j,l)c_(i,j,l)v^l T^j, and check M cvec=bvec at all217 rows. The theorem then proves R=0; no numerical rank claim is part of the certificate.

It also gives a literal guarded polynomial cofactor identity in B[T,Z], not only a localization assertion:

    1=Z^5 sum_i hi fi -(Zq-1) sum_(j=0)^4 (Zq)^j.       (5)

Indeed the two right-hand terms are (Zq)^5 and minus((Zq)^5-1). Thus the original nine polynomials plus the inverse guard admit explicit cofactors once the rational vector is supplied. This implication alone is valid even over a nonreduced coefficient ring; reducedness is needed for completeness of the bounded test and the separator's nonzero-quotient interpretation.

A NONZERO-QUOTIENT certificate is a rational column lambda of length217 satisfying (2). Such a vector exists whenever bvec is not in the column space: extend a Q-basis of im M by bvec, assign value0 on im M and value1 on bvec, and extend to a rational linear functional on Q^217. Conversely, applying lambda to M cvec=bvec would give0=1. This elementary vector-space argument supplies the complete alternative over Q, not merely over its algebraic closure. Lambda is a separating functional, NOT a multiplicative character, a point or a positivity witness.

A future verifier must bind the literal p, all nine indexed fi, q, their actual coefficients and degree bounds; reconstruct M and bvec exactly; and check the full identities. A precomputed matrix of unknown provenance is insufficient. A modular solution, rank computation or separator alone does not establish either exact rational certificate. These are a generic certificate contract, not implemented checks or a new launch policy.

Arithmetic shape only: a dense M has217*1638 rational slots, and bvec217; no claim is made that these slots are nonzero. Given a correctly reconstructed matrix, direct unit-witness checking uses at most217*1638 rational scalar multiplications and217*(1638-1) additions before equality comparisons. A separator check uses at most217*(1638+1) scalar multiplications, covering all columns and bvec. Matrix construction, coefficient bit lengths, elimination work, memory and wall time are not bounded by these counts and were not measured. No matrix or witness was constructed here.

## 5. Properness and the degree-at-most35 field-point interface

Suppose R is nonzero. Some field component K of B survives, and [K:Q]<=7. If at least one fi is nonzero on that component, let g be their gcd. Since localization is nonzero, g has an irreducible factor h which does not divide q. Then L=K[T]/(h) is a field, [L:K]=deg h<=5, all fi vanish there and q remains nonzero. Hence R has an L-valued point with

    [L:Q]=[L:K][K:Q]<=35.                              (4)

If all fi vanish, q is a nonzero polynomial of degree at most5. Among the SIX distinct rational elements0,1,2,3,4,5 of K, at least one is not a root of q. Evaluation there supplies a K-valued point, of degree at most7. If q is a nonzero constant every one of these evaluations works. If q=0 on a component, it contributes no surviving point. These are existence proofs, not actual evaluations performed during this task.

Consequently nonzero R, properness of the corresponding guarded ideal in B[T,Z] with Zq-1, and existence of an algebraic characteristic-zero point are equivalent. The point can be chosen of degree at most35 over Q, but need not be Q-rational. An exact separator proves the nonzero ring and this existence result; it does not itself specify h, a factor of p or the point. We make no assertion about a further cubic cover, a complete source, a Keller pair, a counterexample, its map degree or JC2. Such attachments would require separately proved complete-input maps, not this generic lemma.

## 6. Manual changed-object controls and limits

1. EXPONENT SHARPNESS. Over Q take f1=T^5, f2=...=f9=0, q=T. Localization kills the quotient, q^5 belongs to I, but q^4 does not: its degree is smaller than the nonzero multiples of T^5. Thus a universal exponent4 is false. Repeated gcd roots cannot be ignored.

2. REDUCEDNESS IS LOAD-BEARING. Replace B by the rank-seven nonreduced algebra Q[e]/(e^7), take all fi=0 and q=e, a polynomial of T-degree0. Its localization is the zero ring because e is nilpotent; nevertheless q^5=e^5 is nonzero and not in the zero ideal. The candidate saturation exponent and the resulting interpretation of a linear separator both fail. This is an exact changed-hypothesis control, not a criticism of accepted17b, whose gate supplies finite etaleness.

3. ALL-ZERO ROWS. Over Q, all fi=0,q=1 gives M=0 and a nonzero target; extraction of the constant coefficient is an exact separator. Changing q to0 gives a zero localized ring and the zero unit-witness vector. No special all-zero matrix branch may be declared automatically proper or automatically unit without the guard.

4. COMPONENT DROPS. Over the test algebra Q times Q, set f1=(1,T), other fi=0, q=(0,1). The first component is zero after localization; the second is Q[T]/(T), hence nonzero. Neither replacing q by a globally invertible scalar nor using the first component's constant generator globally is licensed. The componentwise proof/gluing in section3 preserves this case.

5. COMPLETE GENERATOR FRAMING. Over Q take f1=T,f2=T-1, other fi=0,q=1. The full ideal is the unit ideal since f1-f2=1. Dropping f2 would permit a spurious nonzero-quotient conclusion from the smaller matrix. Zero/duplicate labels may remain as redundant columns; an unverified omitted row may not.

6. COMPLETE COEFFICIENT FRAMING. With f1=T, other fi=0,q=1, omitting the constant target row would make the remaining target zero and falsely accept the zero vector as a unit witness. Likewise coefficients through T^30, not merely the target degree, belong to the complete identity check. These are hand controls of literal changed objects; no subprocess was run.

The criterion proves neither independence of nine equations nor finite dimensionality of every surviving quotient. All fi can be zero on a surviving component, leaving a localized affine line. The degree bound(4) concerns a selectable algebraic point, not the dimension or length of R. No irreducible factor, gcd, matrix rank, coefficient height, runtime or source outcome has been computed. The term NEW labels a new campaign generic certificate contract; literature novelty was not investigated.

## 7. Completion and documentary custody

Both targets were absent at first action. Exactly two scientific objects were checked before WHOLE reads and are rechecked at completion. No current univariate report, live gate, other science, source data or code was read. All new mathematics is factored/manual. Only documentary metadata, apply_patch and existing artifact begin/close/finalize/verify tools ran. The source coefficients required to instantiate this generic test remain outside the task; there is no execution authority or automatic follow-on.

Own WHOLE read and own-only raised-OPEN/collision checks precede the completion marker. All writers IDLE at handoff before the original19:03:46.700685UTC cap.

## OPEN(S) RAISED

None. The complete generic criterion is proved under its literal hypotheses; no new source attachment is asserted. The cheapest future application test would be exact binding/read-back of all ten actual polynomials and their degree bounds before any certificate is accepted, only under separate authority.

## COLLISIONS

status: EMPTY

- NONE — own-only check, no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14283`.
- Body SHA-256:
  `c2b070aba8ed7807f51da6607b5d45077c242ff70fadc201a578a074185a9f6d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
