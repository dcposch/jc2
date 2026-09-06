# Actual second-characteristic leaders in the order charts

This note uses only the eight frozen charged inputs verified by the root agent, the explicitly authorized class metadata/builders, and the roster. No ledger, jc2-lean, or other ideation input was read or edited. Its formulas are exact over Q.

## Attainment and the nonconstant Jacobian

The charged characteristic report, lines 18–43, prints Moh p.150's definitions and Proposition 2.2 at p.152. Write the h-chart exponents as E=n/K and Qexp=m/K, to distinguish E from Moh's source series index e_source. Since M1=−m, d1=n and d2=K,

    D2=−((-m)n+(M2+m)K)/K=(E−1)m−M2,
    L=E m=Qexp n, W=L−D2=m+M2.

Every listed M2 is less than n−1. The extension needed for a descendant with J(P,Q)=c x^ell is direct: set η=P^(−1/n), expand Q=Σ f_j(x)η^j, and differentiate while holding η fixed. The chain rule gives

    ∂Q/∂x|η=J(Q,P)/P_y=−(c/n)x^ell η^(n−1)(1+O(η)).

Thus f_j'(x)=0 for j<n−1 and f_(n−1)'(x)=−(c/n)x^ell. With c nonzero and characteristic zero, the first nonconstant source series coefficient is still e_source=n−1. Its degree is ell+1 instead of 1. Proposition 2.2's scalar-leader case at M2<e_source therefore applies with the same earlier constant coefficients. The proof changes no index into an attained one by a floor argument. The source pair's c nonzero is needed for this extension; the algebraic necessary receiver used in the computations can include c=0.

## The complete target family and a fixed polynomial lift

Proposition 3.1 gives

    T2=Q^E−P^Qexp+Σ γ_ab P^a Q^b,
    0≤b<E, a≥0, an+bm<L.

The unique equality monomial is P^Qexp and its coefficient is −1 after cancelling the monic leading terms. Since gcd(E,Qexp)=1, the displayed lower monomials have distinct degrees. For E,Qexp=3,2 the lower family is 1,Q,Q²,P,PQ. For 4,3 it is 1,Q,Q²,Q³,P,PQ,PQ²,P²,P²Q. These are full existential families; a member satisfying the necessary equations is not by itself the canonical resultant characteristic polynomial.

Use the literal G chart and its exact monic division by h. Set x=0 only in the coefficient extraction used to construct the scalar leader, and write

    h0=y^K+Σ h_0,a y^a,
    A_i=Σ A_i,0,a y^a, B_i=Σ B_i,0,a y^a,
    P*=H^E+Σ A_i H^(E−i), Q*=H^Qexp+Σ B_i H^(Qexp−i).

Here H is a temporary formal symbol. Replace every polynomial in H,y by its unique h0-adic normal expression: repeatedly divide its y-coefficients by the monic h0, retaining the remainder and carrying the quotient to the next H power. Denote the resulting coefficient vector by `ha`. This is division in Q[all x-charge-zero chart coordinates][y], not specialization of h's coefficients to constants. Monic division commutes with x→0, so it exactly computes the x⁰ image of the original chart's h-adic coefficients.

The following recursion is an explicit finite polynomial definition of the required λ in the ORIGINAL chart coordinates. It also specifies all necessary target-coefficient pivots without a denominator or branch:

1. Set C=ha((Q*)^E−(P*)^Qexp).
2. Process each allowed pair (a,b) with r=aE+bQexp and rK>D2 in decreasing r.
3. Set γ_ab=−[y⁰]C_r and replace C by C+γ_ab ha((P*)^a(Q*)^b).
4. With D2=JK+A, 0<A<K in all ten cases, set λ=[y^A]C_J.

Each processed family term has monic h-degree r, so this kills its own scalar upper coefficient and changes no greater h-degree. The unused family terms of degree≤D2 have h-degree≤J and contribute at most a scalar to C_J; hence they do not change the positive-y coefficient defining λ. The coefficient pivots are eliminations of necessary upper equations. All other upper equations remain necessary: every h-adic coefficient x^b y^a h^j with a+jK>D2 is zero; at a+jK=D2 the coefficients with b>0 are zero. Under these equations the displayed λ equals the ACTUAL ordinary coefficient [x⁰y^D2]T2, by the monic triangular relation between ordinary and h-adic coordinates. The localizer is Zλ−1. No claim that a raw coefficient without these upper equations is already an attained leader is made.

The executable polynomial recursion is `derive_leaders.py`; its generated exact-Q Singular scripts and expressions are kept in this directory. The process computes ha using polynomial division, not an approximate root inferred from a name. The unneeded h-adic coefficients below J are discarded only after carrying their monic quotients. Coefficients of y-degree below A in C_J are then discarded; neither operation changes an upper coefficient, a pivot, or λ. This keeps the symbolic derivation compact.

## Bigrading and the first two small examples

The charged grading is deg(A_i,b,a)=deg(B_i,b,a)=(b,iK−a), deg(h_b,a)=(b,K−a). Every target coefficient γ_ab has degree (0,L−an−bm). Thus T2 is homogeneous of degree (0,L) when y has degree (0,1) and x has degree (−1,0). Its h-adic λ has degree (0,W), W=L−D2. This remains true after every scalar pivot. Consequently λ^N lies in bidegree (0,NW), N=1,2,3. The canonical lift can contain h coordinates; the statement that it depends only on the top α/β coordinates is false literally. After imposing further upper equations it may have a simpler congruent representative.

For the 70-coordinate chart, K=8, D2=44, J=5, A=4, W=4. Its h⁵ coefficient is −2A1−quo_y(A1²,h0), up to a scalar target coefficient. Hence the exact global lift is

    λ=−2 A1_0_4−2 A1_0_7 A1_0_5−A1_0_6²
      +2 h_0_7 A1_0_7 A1_0_6−(h_0_7²−h_0_6)A1_0_7².

After the higher-y upper equations this is congruent to −2A1_0_4, but the unqualified replacement is not the exact globally polynomial lift. For the 127-coordinate chart, K=6,D2=69,J=11,A=3,W=3,

    λ=3 h_0_5 A1_0_5²−A1_0_5³−6 A1_0_5 A1_0_4−3 A1_0_3.

It becomes −3A1_0_3 after the higher upper equations. Both exact expressions vanish on the full constant-block cone control without imposing upper equations.

## Cone control and meaning of the receiver

On Δ all A_i and B_i are scalars (the two terminal scalar gauges remain zero), while h remains any permitted monic polynomial. The entire target expression is then a polynomial in h with scalar coefficients. Its canonical h-adic coefficients are scalar in y, before and after each target-coefficient pivot. Since A=D2 mod K is positive in every case, λ=0 IDENTICALLY on Δ. Thus 1=−(Zλ−1) on its quotient. In the original ring, if λ=Σ v C_v with v ranging over positive-y A/B coordinates, the explicit cofactor identity is

    1=Z Σ v C_v−(Zλ−1).

This is a unit certificate for the restricted cone-control ideal. It is not a certificate for the original chart. Direct substitution of h=y^K alone would have tested a smaller control and is insufficient; the retained check keeps every h coordinate.

The homogeneous Jacobian ideal I before Tc−1 has generators of x-charge b+1≥1, while λ has x-charge zero. Hence I∩Q[x-charge-zero parameters]={0}. Whenever the displayed λ is nonzero, λ^N is not in I for ANY N≥1. This is an exact structural obstruction to the proposed homogeneous membership strategy. It does not by itself say that the production c≠0 chart is proper. The latter contains Tc−1 and no longer has this nonnegative grading or the c=0 controls. Likewise a truncated localizer computation alone, especially with an inhomogeneous inverse relation and artificial positive weight for Z, does not certify completion of all original homogeneous membership components.

## Exact per-case inventory

| Case | Unknowns | K; E,Qexp | M2 | D2 | (J,A) | W | λ, λ², λ³ bidegrees | Monomials |
|---|---:|---|---:|---:|---|---:|---|---:|
| `C_n24m16_Mm12_m2_5_ell1_s4` | 70 | 8; 3,2 | -12 | 44 | (5,4) | 4 | (0,4), (0,8), (0,12) | 6 |
| `C_n18m12_M2_9_ell2_s3` | 109 | 6; 3,2 | 2 | 22 | (3,4) | 14 | (0,14), (0,28), (0,42) | 108 |
| `C_n24m18_Mm15_14_ell1_s3` | 127 | 6; 4,3 | -15 | 69 | (11,3) | 3 | (0,3), (0,6), (0,9) | 4 |
| `C_n24m16_M12_17_ell1_s3` | 171 | 8; 3,2 | 12 | 20 | (2,4) | 28 | (0,28), (0,56), (0,84) | 7,075 |
| `C_n24m18_M9_20_ell1_s3` | 341 | 6; 4,3 | 9 | 45 | (7,3) | 27 | (0,27), (0,54), (0,81) | 42,866 |
| `C_n16m12_M6_13_ell3_s3` | 455 | 4; 4,3 | 6 | 30 | (7,2) | 18 | (0,18), (0,36), (0,54) | 2,672 |
| `R001` | 193 | 7; 3,2 | 16 | 12 | (1,5) | 30 | (0,30), (0,60), (0,90) | 3,263 |
| `R002` | 199 | 5; 3,2 | 11 | 9 | (1,4) | 21 | (0,21), (0,42), (0,63) | 417 |
| `R003` | 199 | 5; 3,2 | 11 | 9 | (1,4) | 21 | (0,21), (0,42), (0,63) | 417 |
| `R004` | 241 | 4; 4,3 | 13 | 23 | (5,3) | 25 | (0,25), (0,50), (0,75) | 19,306 |

`leaders.json` binds the complete explicit expanded polynomials to deterministic gzip files, including both expanded and compressed SHA-256 hashes and byte counts. `derive_leaders.py` regenerates the exact polynomials from the class metadata/frozen roster. Largest expression: 42,866 monomials, so the recursive formula is substantially more legible than a raw expanded printout. The 10 expressions contain 76,134 monomials in total. The independent grading audit verifies the declared bidegree on each monomial and evaluates every expression at an exact full-attainment, zero-Jacobian witness.

The case-specific `delta_controls.py` partitions every λ monomial by its first positive-y α/β factor, giving exact polynomial cofactors in the displayed cone identity. It also performs ten exact-Q Singular computations retaining arbitrary h_0,a and scalar α/β variables, and checks both the cone UNIT and an independent negative localizer control. All h_b,a with b>0 are absent from λ by its x-charge-zero grading and remain arbitrary by polynomial-ring extension. Thus this is the full constant-block Δ control, not h=y^K.

An additional actual-polynomial negative control now computes untruncated `std(Z*λ−1)` separately for every exact expanded λ in the complete x-charge-zero coefficient ring. All ten principal bases have size 1 and leave the normal form of 1 equal to 1. `delta-controls.json` retains the original projected-Δ and independent-variable controls and adds full variable order, exact formula hash, backend output, wall time, and memory use for each actual-polynomial check.
