# Two-exponent obstruction attempt: an exact quadratic comparison, but no uniform exclusion

2026-09-09. Independent MANUAL result, UNREVIEWED. First action21:22:42.218945832UTC; controlling stop21:37:42.218945832UTC. Exactly three accepted science inputs, pinned before use; no mathematical subprocess of any size.

## 1. Outcome

For the assigned parameters

    m=3r+1, n=5r+2, r>=2, 1<=j<=r-1,
    x=n/m, y=(n+j)/m, delta=y-x,
    5/3<x<y<2,

I do NOT establish uniform nonexistence or construct a simultaneous-contact cubic. The attempted exponent-divisibility shortcut excludes V=1/3, but that exclusion is already implied by the SINGLE x contact; it is not a new two-contact contradiction.

There is a concrete new lower-degree necessary relation: the two degree-five truncated powers, if simultaneous contacts exist, have an exact linear combination divisible by c, with quotient Q of degree EXACTLY TWO. This yields the factored differential identity(12) below and five explicit proportional-contact equations(10), with all divisions licensed. Its highest-degree coefficient is automatically satisfied, so a degree comparison alone does not finish the obstruction. The remaining lower identities are not proved inconsistent.

Thus the uniform decision remains GAP. The report records the exact successful identities and the failed stronger inference, not another replacement for the already accepted cubic exceptional algebra. No new canonical OPEN ID, source/Keller/JC2 claim, coefficient computation, runtime estimate or follow-on authority is supplied.

## 2. Accepted setting and scope

The accepted16l theorem licenses normalizing the common linear coefficient to1 using the x contact, without discarding field points. Write

    c(t)=1+t+Vt^2+Wt^3, W!=0,
    H_i(z)=[t^i]c(t)^z,
    H6(x)=H7(x)=H6(y)=H7(y)=0.                    (1)

The unknowns V,W are in an algebraically closed characteristic-zero field; they are NOT presumed real. Formal powers have constant1. All exponent denominators below are fixed nonzero rationals. The diagonal j=0 is excluded from divisions, and must remain consistent by accepted16l single-contact existence.

Only the unchanged accepted producer17w, its terminal first gate, and16l were used. Both producer WHOLE reads were reused after current-pin checks; the current terminal gate was read WHOLE. The supplemental Cramer expression in gate B has the root-identified sign correction

    e_y=+12(1+L)E/Gamma,

not the printed minus. The producer's determinant argument is unchanged and no Cramer expression is used in this new proof. No other provenance, corpus, ledger, source, peer or review was read.

## 3. Exponent divisibility and the V=1/3 stratum

Use exactly the accepted polynomial normalizations

    A_X=H6(X)/(X(X-1)),
    B_X=H7(X)/(X(X-1)(X-2)),
    F(X)=720A_X, G(X)=5040B_X.                     (2)

They are monic quartics in X. Two distinct roots x,y imply divisibility of BOTH by X^2-(x+y)X+xy, over the coefficient field; this conclusion requires no inference from numerical degrees alone. Their cubic coefficients are

    [X^3]F=-14+30V,
    [X^3]G=-18+42V,
    [X^3](G-F)=12V-4.                             (3)

The apparent simpler case is V=1/3. Put e=W-1/27. Direct substitution in the literal finite formulas gives the exact polynomial identity

    G(X)-F(X)
      =90e{(X-4/3)(X-5/3)+24e}.                  (4)

For example its X^2 and X coefficients are90e,-270e, and its constant is200e+2160e^2. These are manual coefficient checks of the small exponent polynomials, not executed expansions.

If e=0, then c=(1+t/3)^3. Its x contact fails because H6(x)=binom(3x,6)/3^6 is nonzero for5<3x<6. If e!=0, the quadratic in braces in(4) would have both roots x,y, forcing x+y=3. But x+y>10/3. Hence V=1/3 is impossible on the assigned two-contact locus.

This is NOT yet a genuine two-contact gain. The next calculation shows the same stratum is absent already for a single exponent x in(5/3,2).

## 4. Why that special-locus contradiction is single-contact content

Set

    J=(3x-4)(3x-5), K=(3x-1)(3x-2),
    e_star=-J/216.

At V=1/3 one can write c=(1+t/3)^3+e t^3. Taking only its degree6 coefficient gives

    A_x=e^2/2+eJ/54+KJ/58320.                     (5)

The difference(4) at X=x is2160e(e-e_star). For a common zero of A_x and B_x, either e=0 or e=e_star. At those two values,

    A_x(0)=KJ/58320,
    A_x(e_star)=J(8K-35J)/466560.                 (6)

Every displayed scalar is nonzero on the parameter range. Indeed J,K>0 as rational numbers, and

    8K-35J=-9(27x^2-97x+76)>0.

To check the latter without a complex-coefficient sign assumption, put z=2-x, so0<z<1/3. Then

    27x^2-97x+76=-10-11z+27z^2<-10-2z<0.

Consequently V-1/3 is a unit already in the normalized SINGLE-contact coefficient ring, not just nonvanishing at a chosen field point. A literal algebraic certificate prescription is available without evaluating its coefficients: take the affine polynomial I(e) interpolating

    I(0)=1/A_x(0), I(e_star)=1/A_x(e_star).

Since e_star and both values in(6) are nonzero rationals, I is defined over Q. The polynomial I(e)A_x(e)-1 is divisible by e(e-e_star), hence by the rational-unit multiple G(x)-F(x). This proves the two restricted contact polynomials generate the unit ideal at V=1/3. Lifting the identity through evaluation V->1/3 shows1 belongs to the original single-contact ideal plus(V-1/3); its image is therefore a unit in that quotient, including nilpotents. The original W guard can remain in place and is not weakened.

Accordingly, on the contact algebra G-F truly has degree3 in X, with unit cubic coefficient(3). This is a checked special-stratum fact, but it does not eliminate two distinct roots of that cubic. Treating it as a uniform exclusion would be a false inference. No novelty relative to other uncharged campaign work is claimed.

## 5. Compare the TWO entire truncated-power ODE solutions

Define

    D(t)=sum_(i=0)^5 H_i(x)t^i,
    E(t)=sum_(i=0)^5 H_i(y)t^i.

The four contacts and the degree bounds imply exact polynomial identities

    cD'-x c'D=k_x t^7,
    cE'-y c'E=k_y t^7.                            (7)

Their right sides are not merely leading terms. Formal approximation through degree7 makes the left sides O(t^7), and their polynomial degrees are at most7. The first accepted contact supplies k_x!=0. The second k_y is also nonzero: if it vanished, writing y=a/b in lowest terms gives E^b=c^a. Every factor multiplicity in c would be divisible by b. But5/3<y<2 implies b>=4 (no rational with denominator1,2,3 lies strictly in that interval), whereas c has degree3. This contradiction proves k_y!=0. Both D and E therefore have degree exactly5, and their leading coefficients D5,E5 satisfy

    k_x=(5-3x)W D5,
    k_y=(5-3y)W E5,                               (8)

with all factors nonzero. The same identities show c is squarefree: a repeated root of c is nonzero because c(0)=1, and would contradict either nonzero right side in(7). These are derived facts, not root assumptions.

Put sigma=x*k_y/(y*k_x), a nonzero field scalar. At every root beta of c, evaluation of(7) gives E(beta)=sigma D(beta). Since c is squarefree,

    E-sigma D=cQ,                                 (9)

for a polynomial Q with degree at most2. It has degree EXACTLY2, because

    Q2=(E5-sigma D5)/W
       =5*delta*E5/{y(5-3x)W}!=0.

This construction does not divide by D or E at their roots, does not assume sigma!=1, and does not invert Q0 or Q1. In particular Q0=1-sigma may vanish.

The local series version of(9) supplies five literal lower-degree comparison equations:

    H_i(y-1)=sigma H_i(x-1), i=3,4,5,6,7.          (10)

Indeed E/c=c^(y-1)+O(t^8) and D/c=c^(x-1)+O(t^8), whereas Q has degree2. Its first three coefficients are

    Q0=1-sigma,
    Q1=(y-1)-sigma(x-1),
    Q2=(y-1)V+(y-1)(y-2)/2
          -sigma{(x-1)V+(x-1)(x-2)/2}.

Equation(10) is a genuine degree-two comparison consequence of BOTH whole ODE solutions. It does not assert that either shifted exponent separately has zero contact coefficients, and no denominator from an individual H_i is inverted. A ratio test discarding their zero locus is not licensed.

## 6. A factored second-order identity, and why its top gives no contradiction

Substitution of(9) into(7), with k_y=sigma*y*k_x/x, gives exact identities

    D'=x/(sigma*delta){cQ'+(1-y)c'Q},
    E'=y/delta{cQ'+(1-x)c'Q}.                     (11)

For example, the first follows after subtracting the two ODEs: the remaining term is c times sigma*(x-y)D'/x+cQ'+(1-y)c'Q. Dividing by the nonzero polynomial c is legitimate in the field polynomial ring; the factor delta is the explicitly excluded diagonal. These identities use all polynomial terms, not a leading-only approximation.

For a lower-degree obstruction attempt eliminate D itself. Set b=delta*k_y/y!=0. Combining the first identity(11) with its ODE in(7) gives

    sigma*delta*c'D
      =c^2Q'+(1-y)cc'Q-bt^7.

Differentiate this equation and eliminate D' using(11), without dividing by c'. The result is the exact polynomial identity

    c^2 c' Q''
      +{(3-x-y)c(c')^2-c^2c''}Q'
      +(1-x)(1-y)(c')^3Q
       =b t^6(7c'-t c'').                         (12)

Thus no critical point of c' is omitted. This is a cubic-c/quadratic-Q identity, not a new source equation or a constructed solution. It is only a necessary condition; no sufficiency or independent-row assertion is made for(10)-(12).

The most immediate proposed contradiction from(12) FAILS. Its top coefficient t^8 says

    3(5-3x)(5-3y)W^3 Q2=15bW.                   (13)

Substituting the exact Q2 from section5 and k_y=(5-3y)W E5 makes BOTH sides identical. No sign comparison is available for W,Q2 in an algebraically closed field. The remaining lower coefficients of(12), together with the complete contact equations, are not proved inconsistent in this task. Likewise (10) is not a contradiction merely because x!=y: the scalar sigma and all coefficient-zero cases remain.

## 7. Controls, scope and stopping decision

- DIAGONAL: at j=0 the single-contact solutions from16l survive. Sigma then equals1 for the identical D,E, Q vanishes, and the divisions by delta in(11) are invalid. This verifies that the quadratic comparison is a distinct-exponent statement, not an accidental single-contact exclusion.
- LOWER-DEGREE OR ZERO TARGET: k_y=0 was ruled out using its reduced denominator>=4 and deg c=3. Outside that range, c=(1+t/3)^3 and y=5/3 have E=(1+t/3)^5 and zero ODE target. One cannot import the exact-degree or squarefree-root argument into that changed hypothesis.
- ZERO COEFFICIENTS: neither Q0=1-sigma nor any H_i(x-1),H_i(y-1) was divided by. The field-root argument establishing(9) is explicitly not a nilpotent-ring theorem. By contrast the unit claim in section4 has its own literal ideal proof and does include nilpotents.
- ACTUAL TOP CONTROL: the cancellation in(13) uses the exact nonzero scalar b and Q2; changing either scalar alone makes the necessary identity fail. The highest coefficient is therefore checked, but is automatic for the genuine data and cannot be counted as a new obstruction.
- CUBIC IN X: V!=1/3 only proves G-F has degree3; a cubic may have two distinct prescribed roots. Excluding its vanished-leading-coefficient stratum is not a root-count contradiction.

The strongest new necessary object here is the exact quadratic quotient(9) with its whole derivative comparison(11)-(12). The elementary exponent-division special-locus idea was tested and found to be single-contact content. Neither route closes the uniform four-contact question. No sampling, coefficient execution, new reduction framework, source point, certificate, solver, performance or downstream claim is made. The report stops at this precise gap rather than promoting a generic or top-only calculation.

## 8. Read perimeter and publication

All three current hashes matched before reads. Unchanged producer WHOLE reads were explicitly reused; the terminal gate was read WHOLE with its announced supplemental Cramer sign correction. No uncharged scientific object or process state was accessed. Documentary time/hash/read checks, own apply_patch and existing begin-close-finalize-verify only. ZERO mathematical subprocess, CAS, arithmetic/import/compile/test, coefficient-code or data artifact, numerical sample, web/network/AWS/SSH/proc/agent/shared/frozen/protected write. Own WHOLE and raised-question/collision checks precede the unique marker. All writers become IDLE before21:37:42.218945832UTC.

## OPEN(S) RAISED

- UNRESOLVED ASSIGNED QUESTION, no new canonical ID: QUANTITY the dimension0..3 of the accepted guarded cubic exceptional algebra for each(r,j), still undetermined. CHEAPEST TEST remains its exact r=2,j=1 cubic/two-quadratic gcd with guard and read-back, cost unknown and not executed or authorized. A claimed obstruction from(12) would first have to use a genuinely nonautomatic lower coefficient; its top coefficient alone has been falsified as an obstruction by(13).

## COLLISIONS

status: EMPTY

- NONE — own-only extraction; no corpus or ledger search.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13132`.
- Body SHA-256:
  `4d5dbbe06ce834c8d3e20b06fa9f7c1c1b336f3346d92026a7e59d93dc9bfa53`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
