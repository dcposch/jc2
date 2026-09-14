# Reducible cone: global initial tuples survive; branch selection does not

2026-09-08. **Exact local discriminator, not a source theorem.** Weight-filtered normal remainders still inject into the product of the three cone branches. Taking the global Newton initial before branch projection preserves regularity. But this does NOT ensure a branch on which both actual first nonzero moving remainders are regular, nor supply the nonconstant coefficient required by15f. Tiny exact countercontrols separate these statements. No global scaling, degeneration, first-contact or Keller-source arrow is assumed.

## 1. The valid product-ring replacement

Over an algebraically closed characteristic-zero field K let

    V0=g³+p³=product_(zeta³=-1)(g−zeta p),  R0=p²V0,
    w(g)=5, w(p)=−7.

Assume R_s=R0+T_s, where T_s lies in sK[[s]][g,p], has total degree<5 and weight<=1. This vanishing-at-s=0 condition is necessary to call V0 the initial cone. Assume R_s odd when parity is used. These are local hypotheses, not consequences established for a proposed moving source.

Lexicographic division by the monic leading monomial g³p² terminates and does not increase total degree or weight: every replacement term has smaller g-degree, degree<=5 and weight<=1. Repeated division therefore gives finite normal blocks. For odd F of degree<=13, weight<=3 the blocks Pi in F=sum R_s^i Pi, i=0,1,2 satisfy

    deg Pi<=13−5i,  w(Pi)<=3−i.

For odd G of degree<=23, weight<=5 the analogous Qi, i=0,...,4 satisfy bounds23−5i and5−i. No actual high R power is expanded here.

Every normal remainder of weight<=5 injects into

    K[g,p]/(V0) -> product_(zeta³=-1) K[p].

Indeed vanishing on ALL three lines means V0 divides P. Writing P=V0 U gives w(U)<=−10, so U has no p-degree0 or1 terms. Thus p² divides U and R0 divides P, impossible for a nonzero remainder normal modulo g³p². Irreducibility of V0 is unnecessary for this PRODUCT statement. The product is the normalization ring, not a field; its differential constants are K³ rather than automatically the diagonal K.

At each generic branch, R_g=3zeta²p⁴ is invertible in K(p). Thus there are formal roots g_zeta(s,z) with R_s(g_zeta,p)=z and g_zeta(0,0)=zeta p. Fix eta>0, after a finite parameter extension if needed, and put z=s^eta Z. For a normal block with first coefficient s^n P_n, the coefficient at order n of its THREE composed branches is exactly

    (P_n(zeta p,p))_zeta.

It is a nonzero tuple of regular polynomials, although some entries can vanish. Every implicit correction has positive extra s-order. Multiplication by s^(i eta)Z^i and taking the GLOBAL minimum of n_i+i eta therefore produces a regular product-ring Newton initial; different i cannot cancel because their Z powers differ. This proves a useful tuple version of the15f regular-initial step.

An adequate additional branch-selection hypothesis is explicit overlap: on one branch the chosen GLOBAL initials of both objects remain nonzero, and the needed A coefficient restricts nonconstantly. Then those branch initials really are the actual first initials and are regular. Product injectivity alone does not imply this overlap.

## 2. An exact no-common-branch countercontrol

Take the allowed odd monic deformation and two allowed normal inputs

    R_s=R0+s p,
    F=p²(g+p),              G=p(g²−gp+p²).

Both inputs have degree3 and odd parity; their weights are respectively−9 and3, within the F/G bounds. They are already normal. On R_s=0 near the branch g=zeta p,

    g=zeta p−s/(3zeta²p³)+O(s²).

This follows directly by inserting the expression into the degree5 equation; no Puiseux or implicit regularity theorem is being used at the affine origin.

On zeta=−1 the first nonzero moving F residue is

    −s/(3p),

which has a pole at p=0, whereas G has the nonzero regular initial3p³. On either of the other branches, where zeta²−zeta+1=0, F has nonzero regular initial(zeta+1)p³, but G has first nonzero residue

    −(2zeta−1)s/(3zeta²p).

Its numerator is nonzero. Consequently **no normalization branch makes BOTH actual first nonzero moving remainders regular**. Their product-global order0 initials are nevertheless regular with complementary zero supports. Replacing s by a positive power or multiplying F/G by scalar s-powers does not cure this support issue. With z=s^eta Z and eta>1, the displayed order1 pole remains the first branch contribution when the order0 residue vanishes.

This countercontrol satisfies the stated cone/division/weight/parity hypotheses. It does NOT satisfy14v first-contact F_j=R0 C, the saturated low equations, or any full Jacobian/lift system. Those hypotheses have not been supplied for the cone. Hence it refutes the bare local branch-selection inference, not an actual source degeneration or any possible product-ring reformulation.

## 3. Nonconstancy and the target are separate conditions

The bounds also permit the formal choice F=s²R_s. At eta=1, the formal object A=R_s³+F has initial Z³+Z, whose coefficients are all scalar. Thus the bounds and product injectivity do not by themselves produce a nonconstant A coefficient.

A useful sufficient replacement is to supply the actual first-contact coefficient C with C(0)=0 and V0 not dividing C. Then some branch restriction is nonzero and cannot be constant, because every branch passes through the origin. Its provenance and the relevant order bounds would still need proof from the source. They are not inferred here. Similarly, scalar coefficients from a reference series remain diagonal in K³ only by their provenance, not because the total fraction ring has one constant field.

On each line, D=d/dp preserves K[p]. The potential transformed target g²/R_g has initial1/(3p²), which is not regular. Thus a genuinely regular coefficientwise initial bracket could still support a pole contradiction. But extracting the CORRECT nonzero initial bracket, retaining its orders and all scalar-reference terms, is not licensed by product injectivity alone. No assertion about a new full3/5 proof or target-order comparison is made.

## Evidence and stop

Both complete15e/f producer proofs were read; their accepted status was supplied by root, while their frozen original headers are unchanged. Named history checks found no charged version of this cone countercontrol; no exhaustive novelty claim. No live moving-lift work or global source map was read. No new external theorem is imported.

Eight capped normal/−O controls pass, using exact Q[zeta]/(zeta²−zeta+1) arithmetic and only the degree5 divisor to first formal order and degree3 inputs. Actual changes freeze the moving root, change the central curve, or replace F by p³; each fails the corresponding identity or no-common-branch verifier. Positive witnesses are byte-identical, with zero Assert nodes. The scalar-initial example is a transparent formal identity, not a full-source fixture or a computation of R_s³. Inputs, evidence and transaction are pinned in custody. No CAS, AWS, full source expansion, new lane, live peer or shared/protected edit. **STOP: valid product-tuple lemma plus explicit branch-selection GAP; all writers idle at terminal handoff.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7244`.
- Body SHA-256:
  `939179c6bafe41757e7c679a7b5940b7f0cd7a4b25cc83f1d705c17415033190`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
