# A 7-adic obstruction to two contact exponents: three infinite residue classes

2026-09-09. Root/Astra MANUAL theorem, UNREVIEWED. This is not a source
exclusion or a JC2 result. Manual derivation21:28–21:31 UTC, transaction
opened21:32; original publication stop21:43 UTC. Zero mathematical subprocesses.
Accepted17w supplies the exact formulas and degree-at-most-three implication.

## 1. Statement and scope

Put r>=2, m=3r+1, n=5r+2, x=n/m, y=(n+j)/m, 1<=j<=r-1.
For every r congruent to1,2 or3 modulo7, there is NO cubic

    c(t)=1+ut+vt²+wt³, w!=0,

over an algebraically closed characteristic-zero field with
H6(x)=H7(x)=H6(y)=H7(y)=0, where Hk(X)=[t^k]c(t)^X.
Thus the normalized guarded cubic algebra of17w is the zero ring for these
parameters. The four other residue classes remain undecided here.

More generally the argument applies whenever either prescribed exponent z
has v7(z)<0, or is7-adically integral and congruent to0 or1 modulo7. The
residue-class conclusion above uses only z=x, not a classification using y.

The proof contrasts two rigorous degree bounds: any simultaneous normalized
point has its V in an extension of Q of degree<=3 by17w; a SINGLE contact
at such a z forces V to have degree>=7. The latter is not an assertion that
the single-contact algebra is a field, irreducible or of dimension7.

## 2. Exact two-equation input and the one external elementary fact

The normalization u=1 is licensed by17w, including its u=0 check. Write
V=v/u² and W=w/u³. For a rational exponent z in the prescribed interval,
the two contact equations are A_z(V,W)=B_z(V,W)=0, with

    A_z=W²/2+(z-2)(V+(z-3)/6)W
         +(z-2)V³/6+(z-2)(z-3)V²/4
         +(z-2)(z-3)(z-4)V/24
         +(z-2)(z-3)(z-4)(z-5)/720,

    B_z=W²/2+V²W/2+(z-3)VW/2+(z-3)(z-4)W/24
         +(z-3)V³/6+(z-3)(z-4)V²/12
         +(z-3)(z-4)(z-5)V/120
         +(z-3)(z-4)(z-5)(z-6)/5040.

These are the literal17w formulas, not newly generated data. Work in an
algebraic closure of Q7 with its valuation v7 normalized by v7(7)=1.
Existence of this extension is the standard fact in theorem10.4 and
remarks10.5/10.7 of [Sutherland's MIT notes](https://math.mit.edu/classes/18.785/2021fa/LectureNotes10.pdf).
Any number-field point may be embedded there. We use only the ultrametric
rule: a sum having a unique term of strictly least valuation cannot vanish.
The needed degree argument is proved below, rather than importing a
ramification or Newton-polygon irreducibility theorem.

## 3. A valuation lemma for the displayed support

Consider polynomials A(P,Q), B(P,Q) overQ7 with the respective supports

    A: Q², PQ, Q, P³, P², P, 1;
    B: Q², P²Q, PQ, Q, P³, P², P, 1.

Assume every A coefficient is integral, coefficients of Q² and P³ are
units; every NONCONSTANT B coefficient is integral, its P²Q coefficient
is a unit, and its constant has valuation exactly-1. Coefficients elsewhere
may vanish or have positive valuation. Then any simultaneous zero satisfies

    v7(P)=-2/7,      v7(Q)=-3/7.                 (L)

Proof. Put a=v7(P),b=v7(Q), permitting infinity for zero. If both are
nonnegative, B's constant is the unique least term. If a>=0,b<0, the Q²
term is the unique least term inA. If a<0,b>=0, the P³ term is uniquely
least inA. These arguments include P=0 or Q=0, so both must be nonzero
with a,b<0.

If3a<2b, then b>3a/2 and each of2a,a,b,a+b,0 is strictly larger than3a;
thus the unit P³ term is uniquely least inA. If2b<3a, then b<3a/2<a,
and each of3a,2a,a,b,a+b,0 is strictly larger than2b; thus Q² is uniquely
least. Consequently3a=2b. Write a=-2t,b=-3t,t>0.

In B the P²Q term now has valuation-7t; every other nonconstant term has
valuation at least one of -6t,-5t,-4t,-3t,-2t, all strictly larger. Its
constant has valuation-1. Vanishing forces -7t=-1. This proves(L).

## 4. Integral exponents congruent to0 or1

Suppose z is7-adically integral with z mod7 equal0 or1. Every coefficient
ofA_z is integral: 2,6,4,24,720 are7-adic units. The Q² coefficient is1/2
and the P³ coefficient (z-2)/6 is a unit. All nonconstant B_z coefficients
are integral and the P²Q coefficient is1/2. Its constant has valuation-1,
because z-3,z-4,z-5,z-6 are allunits, while v7(5040)=1.

The lemma applies directly withP=V,Q=W. It forces

    v7(V)=-2/7,      v7(W)=-3/7.                 (I)

No cancellation or integrality of the unknowns was assumed.

## 5. Exponents with negative7-adic valuation

Suppose v7(z)=-h<0, h a positive integer. Set V=zP,W=z²Q and divide both
equations byz^4. In A_z(zP,z²Q)/z^4 the seven coefficients, in the order
Q²,PQ,Q,P³,P²,P,1, are

    1/2,
    1-2/z,
    (1-2/z)(1-3/z)/6,
    (1-2/z)/6,
    (1-2/z)(1-3/z)/4,
    (1-2/z)(1-3/z)(1-4/z)/24,
    (1-2/z)(1-3/z)(1-4/z)(1-5/z)/720.

They are all integral and the two required ones are units. In the scaledB,
the eight coefficients in the orderQ²,P²Q,PQ,Q,P³,P²,P,1 are

    1/2, 1/2, (1-3/z)/2, (1-3/z)(1-4/z)/24,
    (1-3/z)/6, (1-3/z)(1-4/z)/12,
    (1-3/z)(1-4/z)(1-5/z)/120,
    (1-3/z)(1-4/z)(1-5/z)(1-6/z)/5040.

Since1/z has positive valuation, every factor1-k/z is a unit. The scaled
constant in B has valuation-1; the other coefficients are integral, with
P²Q coefficient1/2. The same lemma givesv7(P)=-2/7,v7(Q)=-3/7, hence

    v7(V)=-h-2/7,      v7(W)=-2h-3/7.           (N)

This rational rescaling is only for the valuation argument. It is not a
new source normalization, a specialization ofc, or a division by unknownV/W.

## 6. Degree contradiction and the residue classes

If an algebraic number V has valuation an integer minus2/7, it satisfies
NO nonzero rational polynomial of degree<=6. Indeed the nonzero terms
a_i V^i have valuations v7(a_i)+i*v7(V). For distinct i,j between0 and6,
these cannot be equal: their fractional parts differ by -2(i-j)/7, which
is not an integer. Thus any such polynomial has a unique least-valued
term, so cannot vanish. In particular [Q(V):Q]>=7.

On the other hand17w proves that every normalized simultaneous contact
point has V a root of the specific rational monic cubic J3, and W=W(V)
is rational-polynomial inV. This point is algebraic, embeds intoQ7bar,
and contradicts either(I) or(N). The argument is valid for either exponent,
provided it meets the stated7-adic condition.

Forx=(5r+2)/(3r+1) the required three classes are immediate:

| r modulo7 | numerator modulo7 | denominator modulo7 | x behavior |
|---|---|---|---|
|1|0|4|integral, residue0|
|2|5|0|negative valuation|
|3|3|3|integral, residue1|

The numerator is a unit in the middle row even if the denominator is
divisible by a higher power of7. Therefore the obstruction holds for every
r in these classes and every1<=j<=r-1, not just for three sample values.
It includes the suggested smallest test r=2,j=1 without running its gcd.

If the guarded17w algebra were nonzero, as a finite-dimensional Q-algebra
it would have a field quotient with algebraic normalized coefficients,
contradicting the proof. Thus the guarded algebra is zero, including any
possible nilpotents. No particular Bezout certificate is emitted.

## 7. Controls, non-conclusions and completion

- A single contact is not excluded: its coefficients can have degree>=7.
  Accepted16l provides single-contact solutions for the relevantx. It is the
  SECOND distinct exponent and17w's cubic bound that create the contradiction.
- Atj=0,17w's divisions byy-x and its cubic bound do not apply; no spurious
  single-contact nonexistence conclusion follows.
- For integralz congruent to2, the P³ coefficient inA need not be a unit.
  For integralz congruent to3,4,5,6, the numerator ofB's constant need not
  be a unit. Those cases are not covered by the valuation lemma application.
- V=0 and W=0 are explicitly handled in the proof, not discarded by assuming
  their valuations finite. All coefficients may be complex/algebraic; no
  real-root positivity is used.
- A number of degree>=7 may have the fractional valuation: the contradiction
  depends on the proved cubic, not on an assumption that all coefficients
  are rational. No assertion that the whole leading algebra is irreducible
  or degree7 was used or proved.

The result is a uniform necessary-system obstruction on three infinite
residue classes. It does NOT exclude any complete F10 source: a late-column
exception being empty may license further affine elimination, but that
attachment is not part of this report. The other residue classes, middle
band exceptions, fullsource outcome and JC2 remain unresolved. No scientific
subprocess, sample, package import/test, source expansion, AWS or code edit.
Only the recorded primary-text fact, manual algebra and documentary custody.

## OPEN(S) RAISED

None new. The assigned uniform contact question is narrowed, not resolved:
remainingr residues0,4,5,6 modulo7 are not settled by this report. Cheapest
next discriminator is to apply the stated criterion also toy, or examine
those residual valuation cases, manually; no computation is registered here.

## COLLISIONS

Own new report/box only; no corpus scan. Own WHOLE proof, input read scope,
and raised-OPEN check completed21:34 UTC before this marker and transaction
close. No exact first-thought timestamp is claimed. No later source write.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9254`.
- Body SHA-256:
  `8e7469498296d858e545d171710be3eb9c5625b2550a6890cfc7e640c0561c57`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
