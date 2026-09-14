# Two integral contact exponents force integral coefficients: a stronger 7-adic exclusion

2026-09-09. Independent MANUAL theorem, UNREVIEWED. First action21:46:24.678762771UTC; controlling stop22:01:24.678762771UTC. Exactly four accepted science inputs are charged in PINS.json. ZERO mathematical subprocesses, coefficient samples or executed arithmetic.

## 1. New result, distinguished from accepted17y

Fix r>=2, m=3r+1, n=5r+2 and1<=j<=r-1. Put x=n/m,y=(n+j)/m. The accepted normalization writes the possible cubic as

    c(t)=1+t+Vt^2+Wt^3, W!=0,
    H_i(z)=[t^i]c(t)^z.

The target equations are H6(x)=H7(x)=H6(y)=H7(y)=0. The NEW obstruction is:

    If x,y are distinct and7-adically integral, their TWO H6
    equations alone force v7(V)>=0 and v7(W)>=0.             (I)

Consequently the four-contact system has no point whenever either such exponent has residue0,1 or2 modulo7: its H7 equation has a unique negative-valued constant term. The residue2 conclusion is new relative to accepted17y, whose single-contact lemma fails its cubic-coefficient unit hypothesis there. This proof uses both exponents, not a reuse of the old degree>=7 bound.

Combining this result with accepted17y's negative-exponent case gives:

    NO simultaneous contacts for r=0,1,2,3 mod7, for EVERY
    allowed j. For r=4,5,6 mod7 the additional excluded j
    classes are given in section6.                           (II)

In particular ALL r=0 mod7 are now excluded, even when j is divisible by arbitrarily large powers of7. There is no assumed unit condition on y-x and no digit-by-digit lifting procedure. The remaining r/j classes are not settled, and no source, Keller, JC2 or full F10 assertion follows from this necessary-system theorem.

## 2. Accepted input and literal equations

Only the accepted17y producer/gate,17w producer, and16l producer were used. All four current hashes were checked before use. Both17y objects were read WHOLE; the unchanged earlier WHOLE17w/16l reads were explicitly reused. Historical UNREVIEWED headers are retained in the frozen inputs; their accepted scope is the root-specified one. No provenance or linked primary text was followed.

We use exactly the valuation setting admitted by17y: the normalized7-adic valuation extends to Q7bar, number-field points embed there, and a sum with one strictly least-valued nonzero term cannot vanish. Put v7(7)=1 and v7(0)=infinity. The needed normalized equations from17w are

    A_z=W^2/2+(z-2)VW+(z-2)(z-3)W/6
       +(z-2)V^3/6+(z-2)(z-3)V^2/4
       +(z-2)(z-3)(z-4)V/24
       +(z-2)(z-3)(z-4)(z-5)/720,

    B_z=W^2/2+V^2W/2+(z-3)VW/2+(z-3)(z-4)W/24
       +(z-3)V^3/6+(z-3)(z-4)V^2/12
       +(z-3)(z-4)(z-5)V/120
       +(z-3)(z-4)(z-5)(z-6)/5040.              (1)

Here H6(z)=z(z-1)A_z and H7(z)=z(z-1)(z-2)B_z. For the prescribed rational exponents5/3<x<y<2, these prefactors are nonzero; they need not be7-adic units to give equivalence of their zero equations in the field. A_z's denominators2,6,4,24,720 are ALL7-units.

For an integral exponent z!=2 set h=v7(z-2)>=0, finite. In A_z the W^2 coefficient is a unit, the V^3 coefficient has valuation EXACTLY h, and every coefficient other than W^2 has valuation at least h (zero coefficients are permitted). This common factor z-2 is the key feature that remains valid when z=2 modulo7.

## 3. A single A equation with negative V: exact shifted balance

Let a=v7(V), b=v7(W). Suppose A_z(V,W)=0 for an integral z!=2 and a<0. Then W cannot be zero: with b=infinity the V^3 term has valuation h+3a, strictly smaller than those of V^2,V,1, whose valuations are at least h+2a,h+a,h. Thus W is nonzero and b is finite. We prove

    2b=h+3a.                                             (2)

If h+3a<2b, then b>(h+3a)/2. The VW term has valuation at least h+a+b, and

    (h+a+b)-(h+3a)=b-2a>(h-a)/2>0.

The W term has valuation at least h+b, with difference b-3a>(h-3a)/2>0. The V^2,V,constant terms are likewise strictly higher because a<0. The W^2 term is higher by the assumed inequality. The V^3 coefficient has exact valuation h, so it is the unique least term, impossible.

If 2b<h+3a, then b<(h+3a)/2<h. The W term exceeds2b because h-b>0; the VW term exceeds2b because

    h+a-b>(h-a)/2>0.

The V^3 term is higher by the assumption, and V^2,V,constant have valuations at least h+2a,h+a,h, all strictly greater than h+3a and hence than2b. Therefore the unit W^2 term is uniquely least, also impossible. This proves(2) without assuming a sign for b, and in particular without assuming h=0.

The conclusion includes the ordinary unit-cubic case h=0 used in17y, but also the failed old case h>=1. It does not by itself force any fractional denominator or contradiction.

## 4. The divided difference eliminates the entire negative branch

Now assume BOTH A_x=A_y=0, x,y distinct and integral. Their divided difference is a literal polynomial in x,y,V,W. With s=x+y and p=xy, the exact expression is

    Dxy=(A_y-A_x)/(y-x)
       =V^3/6+VW+(s-5)V^2/4+(s-5)W/6
        +(s^2-p-9s+26)V/24
        +(s^3-2ps-14(s^2-p)+71s-154)/720.        (3)

This is the same finite divided-difference identity underlying accepted17w, here applied to valuations BEFORE any W elimination. Its V^3 coefficient is exactly1/6, a7-unit. Its W^2 term is absent, and every remaining coefficient is integral for integral x,y.

Crucially, the integrality assertion follows from the DISPLAYED polynomial(3), not from an invalid inference that dividing an integral difference by y-x preserves integrality. The latter can have any positive valuation. The nonzero rational y-x may be divided out in Q7bar, and the coefficient formula proves the result is nevertheless integral.

Suppose a<0. Apply section3 to A_x, with h=v7(x-2)>=0. Equation(2) gives

    b=(h+3a)/2,
    b-2a=(h-a)/2>0,
    b-3a=(h-3a)/2>0.                             (4)

In Dxy the V^3 term therefore has exact valuation3a. The VW term has valuation a+b>3a; the W term has valuation at least b>3a. The V^2,V,constant terms have valuations at least2a,a,0, all strictly greater than3a. A zero coefficient only raises these bounds. Thus V^3/6 is the unique least term in Dxy, contradicting Dxy=0. We have proved a>=0, with V=0 allowed.

Finally, if b<0 and a>=0, the unit W^2 term in A_x has valuation2b. The VW and W terms have valuation at least b, and the remaining terms have nonnegative valuation. Hence W^2 is uniquely least. So b>=0 as well. This includes V=0, W=0 and all infinity-valued cases. The paired-A integrality assertion(I) is proved.

This is stronger than comparing the balances of the two A equations and merely obtaining v7(x-2)=v7(y-2). EVEN that apparent equal-valuation branch is rejected by(3)-(4). No equality of leading residues or additional digit test is assumed. All negative branches are ruled out in one finite support argument.

## 5. Residue2 now joins residues0 and1

Let z be either integral exponent and suppose z modulo7 lies in{0,1,2}. In B_z every nonconstant coefficient is integral: its denominators2,6,12,24,120 are7-units. In its constant numerator the four factors z-3,z-4,z-5,z-6 are all units at ANY of these three residues. Since5040=7*720,

    v7(B_z constant)=-1.                          (5)

By(I), V,W are integral. Consequently every nonconstant term of B_z has nonnegative valuation while its constant has valuation-1. This is a unique least term, a contradiction.

The new residue2 conclusion required no V^3-unit assumption in A_z: section3 retains its precise positive valuation h, and section4 uses the other exponent to finish. It also required no degree>=7 contradiction. The old single-contact theorem remains correct and its excluded hypothesis at residue2 has not been silently changed.

For exponent pairs with a negative7-adic exponent, accepted17y already proves nonexistence using17w's degree<=3 result. That argument is retained at its accepted scope and not reproduced as new work. If both exponents are integral, the present proof applies directly.

To pass from a hypothetical point over any algebraically closed characteristic-zero K to the valuation argument, use the accepted17w exact normalized algebra: V is a root of its rational monic cubic and W is a rational polynomial in V. The point is algebraic and embeds into Q7bar, preserving(1). The NUMBER3 is not used by the new integral-exponent contradiction; algebraicity and the admitted embedding suffice. The negative-exponent case still uses the accepted degree bound through17y.

If the guarded17w algebra in one of the newly excluded cases were nonzero, its finite-dimensionality over Q would give a number-field residue quotient. Its exact read-back restores all four contact equations and W!=0 there, contradicting the proof above. Hence that guarded algebra is zero, including potential nilpotents. No explicit unit cofactors or certificate are computed or emitted.

## 6. Actual parameter consequences and exact remaining classes

The numerator and denominator of x have coprime integers because3n-5m=1. If r=2 mod7, its denominator is divisible by7 and numerator is a unit, so accepted17y covers it. Otherwise BOTH x,y are integral. The criterion in section5 is applied to either exponent with no extrapolation to other same-degree objects.

For r=0 mod7, x=2 mod7. Section5 therefore excludes EVERY1<=j<=r-1, not only the previously excluded j=5,6 residues. When j is a positive multiple of7, the difference y-x is highly divisible by7; formula(3) still has integral coefficients and the proof is unchanged. Together with accepted17y the complete excluded r classes are now0,1,2,3 modulo7.

For the other three r classes the exact table is:

| r mod7 | x mod7 | y mod7 | excluded j mod7 by residues0,1,2 | NEW class beyond17y |
|---|---|---|---|---|
|4|6|6-j|4,5,6|4|
|5|3|3+4j|1,3,5|5|
|6|5|5+3j|1,3,6|6|

For example the first row uses inverse6 of the denominator6 modulo7, not a change of exponent orientation. The three possible y residues0,1,2 are solved exactly in each displayed affine expression. These are symbolic congruence consequences for all integers in each class, not evaluated examples.

The remaining classes after combining both the accepted and new results are precisely the following UNDECIDED perimeter:

| r mod7 | j mod7 still undecided by these arguments |
|---|---|
|4|0,1,2,3|
|5|0,2,4,6|
|6|0,2,4,5|

The entry j=0 MODULO7 means an allowed positive multiple of7 within1<=j<=r-1; it is not the excluded exact diagonal j=0. No remaining row is asserted nonempty.

For these residual classes both exponent residues lie in{3,4,5,6}. In B_z the constant has valuation

    v7(z-k)-1>=0,

where k is its unique residue representative among3,4,5,6; the other three numerator factors are units. All nonconstant coefficients are integral too. The new proof gives V,W integral, but there is then no necessarily negative constant term. This is the exact barrier to extending THIS least-term argument: it no longer singles out a strictly least valuation or forces a fractional valuation denominator. Higher cancellation conditions or another mechanism would require a separate argument. This report does not claim an actual integral residual solution, an unramified lift, or a low-degree surviving number field.

## 7. Controls and failed stronger scopes

1. DIAGONAL. At exact j=0 the divided difference of two distinct equations cannot be formed as a consequence. Accepted16l's single-contact solutions survive;17y's nonintegral coefficients of degree>=7 are consistent with that fact. Replacing the missing second equation by the exponent derivative of the first would be unlicensed.

2. LARGE v7(y-x). Formula(3) is a polynomial divided difference with denominators7-units. It remains valid when y-x is NOT a unit, including all positive multiples of7 for j in r=0 mod7. Assuming y-x is a unit would lose exactly these cases; the proof does not make that assumption.

3. ZERO UNKNOWN OR COEFFICIENT. V=0 is handled by the final a>=0 case; W=0 is rejected only when a<0 by the actual least-term argument, not by assigning it a finite valuation. Extra factors in the other coefficients of A_z can vanish or have positive valuation. The proof only needs their lower bounds and the exact W^2/V^3 valuations.

4. OMITTED W^2 CANCELLATION. The first A equation can balance W^2 against V^3 at negative valuations, as the accepted single-contact theorem illustrates. The second DIFFERENT exponent removes the W^2 term in(3). Discarding that step would merely reproduce a compatible single-contact balance rather than a contradiction.

5. RESIDUAL CONSTANT. At residues3,4,5,6 the numerator factor in(5) is divisible by7, so the claimed valuation-1 is false. Its resulting nonnegative valuation is not a zero-ring certificate, and the integrality lemma alone is not a proof of uniform closure. No residue point or lift has been fabricated to claim the opposite either.

6. SCOPE OF FIELD AND RING CLAIMS. The elementary valuations are statements about fields with the admitted7-adic valuation. Nilpotent zero-algebra consequences are obtained separately through a field quotient of the exact finite guarded algebra, not by assigning valuations to nilpotents. The W guard and original four rows remain in that algebra throughout. No fixed rational-coefficient assumption, source attachment or global-degree conclusion was made.

## 8. Stop and custody scope

Outcome: a genuinely stronger necessary-system arithmetic obstruction is PROVED manually. It closes r=0 mod7 entirely and adds one y-residue class in each remaining r=4,5,6 class. The residual table is still open; no general fractional-valuation, another-prime or digit-lift program is claimed. No further task or computation is launched.

All4 science pins matched before use and are rechecked before terminal custody. Both new17y objects were read WHOLE, with unchanged prior WHOLE17w/16l reads explicitly reused. Only manual support comparisons and the literal divided difference were used. No other scientific input, provenance, coefficient sample, mathematical subprocess, CAS/arithmetic/import/compile/test, code/data artifact, network/AWS/SSH/proc/agent/shared/frozen/protected write occurred. Documentary metadata, own apply_patch and existing begin-close-finalize-verify only. Own WHOLE/raised-question/collision checks precede the unique marker; all writers IDLE before22:01:24.678762771UTC.

## OPEN(S) RAISED

- UNRESOLVED ASSIGNED QUESTION, no new canonical ID: QUANTITY the dimension0..3 of the accepted guarded cubic exceptional algebra for each parameter in the remaining table, still undetermined. CHEAPEST TEST would be an exact guarded cubic/two-quadratic gcd for one retained case (for instance the symbolic class's first allowed r=4,j=1), with literal read-back and unknown cost; no evaluation, registration or execution is authorized here. The current valuation mechanism stops because every B constant is integral on that table.

## COLLISIONS

status: EMPTY

- NONE — own-only extraction; no corpus or ledger scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15044`.
- Body SHA-256:
  `847f0d3b1989be37898159bf1eeaed20e4345c67e1b7251958e49a3692590e82`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
