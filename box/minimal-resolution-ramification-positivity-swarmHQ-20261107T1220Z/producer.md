# GENUS1140: nef and big actual ramification and adjoint divisors

Status: ROOT proposal, MANUAL / UNREVIEWED / UNPROMOTED. No independent review, novelty certification or JC2 conclusion. Basis: HQ be30b622b8ce42cb47503c53414df84b883b0837; public27c4ab29317fa30501ddcecb9ba25b0ae6bca09c. No model, CAS or new source acquisition.

## Scope and proposed statements

Let f:Y -> P^2 be a generically finite morphism of degree N>1 from a smooth irreducible projective surface. Let U be an open subset isomorphic to the whole A^2, with f etale on U and f(U) missing a target line L. Assume f contracts no smooth rational (-1)-curve. Write H=f^*L, K=K_Y, R=R_f for the full effective determinant divisor, including multiplicities on contracted components, and Q=2K+3H=K+R in divisor class. The proposed conclusions are:

1. Q and R are nef and big.
2. For an irreducible curve C, Q.C=0 if and only if C is an f-contracted smooth rational (-2)-curve. The same equivalence holds with R.C=0.
3. p_a(R)>=2 and h^0(Y,Q)>=2.

These statements are intended for the SAME minimal resolution of the finite projective normalization of a hypothetical Keller map. They do not assume that normalization smooth, Q-Gorenstein or rational-singular, or that f itself is finite. Arbitrary extra boundary blowups are excluded. R is not assumed reduced, connected or SNC.

The retained MINIMAL-RESOLUTION-RAMIFICATION-GENUS-1 interface gives p_a(R)>=1 under exactly these hypotheses, at its MANUAL/PROVISIONAL, independently confirmed named-foundation scope. Its original report is xmodel/minimal-resolution-ramification-genus-swarmHQ-root-sol56-20261107T0755Z.md, full SHA2564d38a1b2b1c72e3dc9c32f38a3ad036aba9786af594438afd8e258a9546213df. No fresh proof audit or promotion of that interface is claimed.

Named foundations additionally used below: smooth-surface cone/contraction theorem; rational-surface classification and K^2+rho=10; adjunction/Riemann--Roch and Serre duality; Hodge index; Bertini and Stein factorization; divisor-class localization; proper quasi-finite implies finite; and absence of a nontrivial connected finite etale cover of complex A^2. These are named standard inputs, not newly source-proof audited. No semiampleness or vanishing theorem is required.

## 1. Nefness of Q

Y is rational, H is nef and H^2=N>0, while R is effective and R~K+3H. Suppose Q is not nef. On the K-nonnegative part of the curve cone, Q=2K+3H is nonnegative. A K-negative extremal ray therefore has Q negative, exactly as in the retained genus proof.

A birational extremal contraction has a smooth rational (-1)-curve C. If H.C=0, f contracts C, contrary to the hypothesis. Otherwise H.C is a positive integer and Q.C=-2+3H.C>=1, again a contradiction. A contraction to a point gives Y=P^2 and H=m[line]; Q negativity forces m=1, hence N=1.

For a contraction to a curve, a general fibre F has K.F=-2 and H.F>0 by Hodge index. The inequality Q.F=-4+3H.F<0 forces H.F=1. The one-ray and connected-fibre argument in the retained proof then makes every fibre irreducible and reduced and gives a P^1-bundle Y=F_n. Explicitly, a connected reducible fibre would have a component of negative square although every component is proportional to the square-zero fibre class; a multiple fibre mC is excluded by H.F=1. Arithmetic genus zero gives smooth P^1 fibres. Write H=S+bF. Then

R ~ S+(3b-n-2)F,

whose arithmetic genus is zero by adjunction on F_n, independently of effectivity, reducibility or multiplicities of a representative. This contradicts the supplied p_a(R)>=1. Thus Q is nef. The reasoning does not merely deduce nefness from the sign of Q.R: it excludes every possible Q-negative extremal contraction.

Since R=(Q+3H)/2 numerically, R is nef. Its square is (Q^2+6Q.H+9N)/4>0, so R is big.

## 2. Q is not numerically zero

If Q is numerically zero, K is numerically -(3/2)H. Thus K^2=9N/4 is an integer. Rationality gives K^2=10-rho(Y)<=9, so 4 divides N and N>1 forces N=4, K^2=9 and rho(Y)=1. A smooth rational projective surface of Picard rank one is P^2. Hence H has class2[line].

The boundary-prime group is isomorphic to Pic(Y): divisor-class localization and O(U)^*=O(Y)^*=C^*, Cl(U)=0 give this directly. There is exactly one boundary curve C, and its effective class must generate Pic(P^2), so C is a line. Both R and f^*L are supported on that line: f is etale on U and f(U) misses L. Consequently R=3C and f^*L=2C as effective divisors.

H is ample, so f has no positive-dimensional fibre and is finite. Its restriction over P^2 minus L has source P^2 minus C=A^2, and is etale because the full determinant divisor is supported on C. This would be a connected finite etale degree4 cover of complex A^2, impossible. This argument does not require excluding isolated boundary points separately. Therefore Q is not numerically zero.

## 3. Excluding Q^2=0 without a semiampleness import

Suppose Q^2=0. Since Q is nonzero nef and H is nef of positive square, Q.H>0 by Hodge index. From K=(Q-3H)/2 we obtain K.Q=-(3/2)H.Q<0. For large n, H^2(Y,O(nQ))=H^0(Y,O(K-nQ))=0 because (K-nQ).H<0. Riemann--Roch gives

h^0(Y,nQ) >= chi(O(nQ)) = 1-(n/2)K.Q,

which tends to infinity. Choose n with h^0(nQ)>=2 and remove the fixed part of |nQ|, leaving a nonzero movable divisor class M. Nefness and nQ.M+nQ.Z=n^2Q^2=0, where Z is the fixed part, give Q.M=0. Two general members of |M| have no common component, so M^2>=0. Hodge index for the isotropic class Q implies M^2=0 and M is a positive numerical multiple of Q.

Because M^2=0, two general members cannot meet, hence |M| has no base points. Its image has dimension one. After Stein factorization its general connected fibre F is smooth, has F^2=0 and is numerically a positive multiple of Q. Thus K.F<0, so adjunction forces F=P^1 and K.F=-2. But Q.F=0 then says

0 = 2K.F+3H.F = -4+3H.F,

contrary to the integral intersection number H.F. This excludes Q^2=0. Therefore Q is nef and big.

## 4. Null curves, arithmetic genus and section count

Let C be irreducible and Q.C=0. Hodge index gives C^2<0. The identity 2K.C+3H.C=0 gives K.C<=0. Adjunction gives K.C=2p_a(C)-2-C^2>=-1. If H.C>0, integrality in that identity instead gives K.C<=-2, a contradiction. Hence H.C=K.C=0. Adjunction then gives p_a(C)=0 and C^2=-2, so C is a smooth rational f-contracted curve. The converse follows immediately from H.C=K.C=0. As R=(Q+3H)/2 and both summands are nef, the same null curves characterize R.

R is nef and big and Q is nef and nonzero, so Q.R>0 by Hodge index. Cartier adjunction yields Q.R=2p_a(R)-2. Consequently p_a(R)>=2. Finally H^0(K)=H^1(K)=0 on rational Y, so 0 -> O(K) -> O(K+R) -> omega_R -> 0 identifies H^0(Q) with H^0(omega_R). Duality on the Cartier divisor gives h^0(omega_R)=p_a(R)+h^0(O_R)-1>=2, without assuming R reduced or connected.

## 5. Numerical identity, minimality and remaining gap

Let gamma be the genus of a smooth general member of |H|. Adjunction and K^2+rho(Y)=10 give the exact identity

p_a(R)=1+K^2+(9/2)(H^2+K.H)=2+9gamma-rho(Y).

The proposed stronger bound would imply rho(Y)<=9gamma. More substantively, Q^2=16+24gamma-4rho(Y)-3N>0, and the nef inequalities hold for EVERY curve on the actual minimal model. No low-degree census or degree-bound re-audit is proposed.

For an extra boundary blowup beta, H'=beta^*H, R'=beta^*R+E and Q'=beta^*Q+2E. Thus R'.E=-1 and Q'.E=-2: nefness fails exactly as expected, and p_a(R')=p_a(R)-1. A count on an arbitrary common resolution therefore cannot be used as the opposite inequality on this minimal model.

No contrary intersection, empty adjoint space, properness, surjectivity, finite affine Keller realization or JC2 proof is obtained. At least two sections, even if confirmed, do not repair the existing trace, finite-pole or saturation gaps. The useful new review target is the global nef/big and null-curve constraint on the SAME actual normalization, not an elementary degree increment. A successor still needs a concrete whole-source argument incompatible with those constraints; no automatic control family or broad model-ideation lane follows.

Hostile review targets: the passage from the accepted genus theorem to nefness on every extremal ray; the Q numerically-zero endpoint; the elementary movable-pencil proof for Q^2=0; the null-curve adjunction argument; all uses of minimality; and preservation of the possibly singular normalization scope. Verdicts: CONFIRMED_AT_NAMED_FOUNDATIONS / GAP_FOUND / FALSE_WITH_CONTROL / INCOMPLETE.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8489`.
- Body SHA-256:
  `b5c554fccb99bf5a8d4af2ed1de60a46959f1ef0518d88595294eae2e17d3dd3`.
- Frozen basis: `be30b622b8ce42cb47503c53414df84b883b0837`.
