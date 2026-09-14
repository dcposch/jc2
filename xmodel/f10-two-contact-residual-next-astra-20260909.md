# Two contacts cannot occupy the same 7-adic exponent residue

2026-09-09. Independent MANUAL theorem, UNREVIEWED. First action23:05:02.418061737UTC; controlling stop23:27:02.418061737UTC. Exactly the six accepted17w/17y/17za producer/gate inputs are charged. No mathematical subprocess or numerical sample.

## 1. New uniform advance

For the prescribed parameters

    r>=2, m=3r+1, n=5r+2,
    x=n/m, y=(n+j)/m, 1<=j<=r-1,

over any algebraically closed characteristic-zero field there are NO cubics c(t)=1+ut+vt²+wt³, w!=0, with

    H6(x)=H7(x)=H6(y)=H7(y)=0

whenever the positive integer j is divisible by7. Here H_i(z)=[t^i]c(t)^z is defined by the formal binomial series at c(0)=1. Combining with the accepted exclusions, the only classes not settled by these arguments are

| r modulo7 | j modulo7 still undecided |
|---|---|
|4|1,2,3|
|5|2,4,6|
|6|2,4,5|

The NEW content removes the entire j=0 MODULO7 column from the three previously residual r classes. It does not exclude the exact diagonal j=0 by continuity, nor establish any point in the residual table. The statement is a necessary paired-contact obstruction, not a full F10/source/Keller/JC2 result.

The mechanism is the OTHER divided difference: accepted17za supplies integral V,W from the two A equations; the two B equations then exclude distinct exponent roots with the same residue. No new fractional-valuation claim or degree>=7 argument is needed for this integral case.

## 2. Accepted premises and their precise use

Accepted17w permits the common normalization u=1 and writes V=v/u², W=w/u³. Its guarded normalized algebra has a monic cubic relation for V and W is a rational polynomial in V. Thus any hypothetical normalized point is algebraic, and a nonzero guarded algebra has a number-field residue quotient. The accepted valuation setting embeds that field into Q7bar, with v7(7)=1.

When x,y are7-adically integral, accepted17za proves

    v7(V)>=0, v7(W)>=0.                             (I)

Its proof uses BOTH A equations and their exact polynomial divided difference, regardless of how divisible y-x is by7. This proof is used at its accepted prescribed-family scope, not reproduced as new work. Accepted17za already excludes either exponent residue0,1,2. Accepted17y handles the negative-valuation case, including r=2 modulo7, using17w's degree bound. All original contacts and the W guard remain present.

It therefore suffices to handle distinct integral x,y whose common residue k is in{3,4,5,6}. Write s=x+y, p=xy; the symbol p here is the symmetric product, not the prime7 or a source coordinate.

## 3. Literal B divided difference, with every denominator retained

The exact accepted equation is

    B_z = W²/2+V²W/2+(z-3)VW/2+(z-3)(z-4)W/24
          +(z-3)V³/6+(z-3)(z-4)V²/12
          +(z-3)(z-4)(z-5)V/120+F(z)/5040,
    F(z)=(z-3)(z-4)(z-5)(z-6).

Since x≠y in characteristic zero, B_x=B_y=0 implies D_B=0, where the following identity is obtained BEFORE valuation or reduction:

    D_B=(B_y-B_x)/(y-x)
       =VW/2+(s-7)W/24+V³/6+(s-7)V²/12
         +(s²-p-12s+47)V/120+Q(x,y)/5040,          (1)

    Q(x,y)=s³-2ps-18(s²-p)+119s-342.               (2)

Here F(z)=z⁴-18z³+119z²-342z+360, so Q is exactly its polynomial divided difference. The coefficients12,47 in(1) come from the three roots3,4,5;18,119,342 in(2) come from the four roots3,4,5,6. The W² and V²W terms cancel because neither depends on z. These cancellations and shifts are part of the proof; (1) is not the earlier A divided difference with renamed coefficients.

All nonconstant coefficients in(1) have denominators2,6,12,24,120, which are7-units. Thus (I) makes every nonconstant VALUE in(1) integral. It remains to compute the constant's valuation, rather than assuming that division by y-x preserves integrality.

As x≡y≡k modulo7, the INTEGER polynomial divided difference satisfies

    Q(x,y) ≡ F'(k) (mod7).                         (3)

Indeed (y^a-x^a)/(y-x)=sum_(i=0)^(a-1)y^(a-1-i)x^i reduces to a*k^(a-1); no inverse of y-x in the residue field is used. The roots3,4,5,6 of F modulo7 are distinct, and explicitly

    F'(3)=-6≡1, F'(4)=2,
    F'(5)=-2≡5, F'(6)=6 (mod7).                   (4)

Every value in(4) is nonzero. Therefore Q(x,y) is a7-adic unit for every common residual k under consideration, including arbitrarily large v7(y-x). Since5040=7*720 and720 is a7-unit,

    v7(Q(x,y)/5040)=-1.                            (5)

Equation(1) now has a unique term of strictly least valuation: its constant. It cannot be zero. This contradicts the two B equations and proves the new local obstruction. V=0 or W=0 in the valued field only removes nonconstant terms and cannot invalidate the contradiction; neither coefficient has been inverted.

## 4. Equivalent quartic interpretation and the exact carry issue

For fixed integral V,W, the monic exponent polynomial

    G(z)=5040 B_z

has integral coefficients and reduces modulo7 to F(z): all seven nonconstant-in-(V,W) terms acquire a factor7 on multiplication by5040. Consequently TWO distinct roots of G cannot have the same residue3,4,5 or6. Proof: their divided difference reduces to the nonzero derivative in(4), whereas two exact roots would make it zero. This is an elementary difference identity, not an imported Hensel-lifting or irreducibility theorem.

The apparent “carry” is now explicit. Individual F(x)/5040 and F(y)/5040 can both be integral because F(x),F(y) each vanish modulo7. Nevertheless their divided difference has valuation−1: a common simple root of F has unit first derivative. It would be invalid to reduce F(x)=F(y)=0 modulo7 and divide those zeros by y-x modulo7, or to discard the constant because each separate B constant is integral. The exact polynomial Q is what prevents that error.

This interpretation gives a sharp limitation of the argument too: if x and y have DISTINCT residues in{3,4,5,6}, then Q(x,y)≡0 modulo7, since the denominator y-x is a residue unit and both F-values vanish. The constant of(1) is then integral, so the current unique-pole proof stops. This does NOT prove cancellation, a residue solution, an unramified lift, or a low-degree global point on those remaining classes.

## 5. Actual parameter composition and zero algebra

If r=2 modulo7, accepted17y already excludes every j. Otherwise m is a7-unit, so x,y are integral and

    x≡y (mod7) iff j≡0 (mod7).

For r=0,1,3 the parent exclusions already settle every j. For r=4,5,6 the x residues are respectively6,3,5. If j is a positive multiple of7, y has the same residual value and sections3–4 apply. This is the NEW exclusion in each of the three residual r classes, without any bound on the power of7 dividing j. Removing exactly that column from17za's table gives the table in section1; no other class is silently claimed.

For the scheme-level consequence, suppose the accepted guarded finite Q-algebra of17w were nonzero at one of these parameters. Take a maximal ideal and its number-field residue field. The exact17w read-back supplies all four normalized contact equations and W!=0 there. Embed into Q7bar, apply(I), then(1)–(5), obtaining a contradiction. Hence that guarded algebra is the zero ring, including possible nilpotents. Valuations are used only in the field quotient, never assigned to nilpotents. No explicit rational Bezout coefficients or certificate were computed, and no irreducibility or particular coefficient-field factor is assumed.

## 6. Changed-hypothesis controls

1. EXACT DIAGONAL. If j=0, then x=y and the second B equation duplicates the first. Although the polynomial Q extends to Q(x,x)=F'(x), D_B=0 is NOT a consequence of the duplicated equations. Replacing them by the exponent derivative would add a new equation. The accepted single-contact existence controls therefore survive. Positive j≡0 modulo7 is not this diagonal.

2. DISTINCT RESIDUES. At distinct k,l in{3,4,5,6}, Q(k,l)=0 in F7. The alleged valuation−1 conclusion then fails exactly at its unit hypothesis. This demonstrates the honest residual stop, not a constructed solution.

3. OMIT PAIRED INTEGRALITY. Without(I), nonconstant terms of(1) can have negative valuation, and the unique-pole argument is unavailable. The parent TWO-A-equation theorem is load-bearing; a single B or a generic coefficient-degree assertion does not replace it.

4. WRONG TERM/INDEX. The z-independent V²W and W² coefficients cancel in D_B. Keeping either as a divided coefficient, or using s-5 instead of s-7 for the W/V² terms, would not represent B_y-B_x. Formula(1) records the actual shifts and(2) records all quartic terms, including119s and−342.

5. GUARD AND RINGS. No W=0 point is introduced into the original guarded problem; allowing its valuation to be positive or infinite inside the local contradiction only strengthens that local statement. Ring emptiness is deduced through an actual field quotient, not from a count of reduced points or a modular-only unit assertion. All source/affine-scheme conclusions beyond the paired-contact algebra remain outside this task.

## 7. Stop, read scope and custody

Outcome: one new uniform arithmetic obstruction proved manually, removing all remaining positive-j-multiple-of7 classes. The nine residual congruence pairs in section1 remain undecided by this argument. No other prime, digit tree, source construction, coefficient artifact, computation or dependent task is launched.

All six current inputs were hash-matched before WHOLE reads; clipped passages were recovered as documented in READ-SCOPE. Root's ancillary17w Cramer-sign correction and17za scope qualifications were retained. No uncharged science, provenance, ledger, peer, live gate, BGV work or new network source was used. ZERO mathematical subprocesses of any size; only manual equations and documentary metadata/publication. Own WHOLE/raised-OPEN/collision checks precede the unique completion marker. This result remains UNREVIEWED until a separate first different-model review.

## OPEN(S) RAISED

No new canonical OPEN ID. Remaining quantity is the dimension0..3 of the accepted guarded cubic algebra for each of the nine residual congruence pairs in section1. The cheapest already-specified exact test is a guarded cubic/two-quadratic gcd with literal read-back for one retained parameter; cost unknown, no execution or registration authorized. The new argument proves only the common-residue obstruction, not uniform closure.

## COLLISIONS

status: EMPTY — own-only targets and report, no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10558`.
- Body SHA-256:
  `6650d5e0ddbec689866e8478cbd4fb31f2a4b8519d4b57f5f9c4c233c8855650`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
