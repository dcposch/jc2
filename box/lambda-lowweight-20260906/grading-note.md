# Independent grading and truncation audit — 2026-09-06

Custody: before reading charged mathematical contents, an awk join of the receipt's numbered basename/SHA-256 fields produced `/tmp/lambda-grading-sha256.manifest`; `sha256sum -c` returned eight OK results against `/tmp/jc2-lane.IZAvbL/inputs/`. This note reads the frozen graded-Moh, source-support closeout, characteristic-degree report, guided_gb, and allowed class/roster metadata. It does not read any additional ideation input. No heavy Gröbner computation was performed for this audit.

## The exact weights and a structural obstruction

Let the source-support order chart have `n=eK`, `m=qK`, `D=n+m−1`, and coefficient ring R over Q. The frozen grading has

    deg(h_ba)=(b,K−a),
    deg(A_i,ba)=deg(B_i,ba)=(b,iK−a),
    deg(c)=(ell+1,D).

Every ordinary Jacobian coefficient row indexed by x^b y^a has degree `(b+1,D−a)`. Every h-adic row indexed by x^b y^a h^j has degree `(b+1,D−a−jK)`. In particular ALL Jacobian rows have strictly positive first charge, although many parameter coordinates have first charge zero. Write I_J for the homogeneous Jacobian coefficient ideal, BEFORE adjoining Tc−1.

Put `L=em=qn=eqK`. The permitted T2 family begins `Q^e−P^q` and has lower constant target coefficients multiplying P^a Q^b of degree `an+bm<L`. Give each such existential target coefficient degree `(0,L−an−bm)`. The family is then homogeneous of degree `(0,L)`, so its scalar coefficient at y^D2 has degree

    deg(lambda)=(0,W),    W=L−D2.

This remains the degree after rational monic pivots eliminate the lower target coefficients. The pivots are homogeneous, divide only by nonzero rational constants, and preserve the first charge zero. If the final formula is specified only modulo upper-degree equations, that quotient must be declared: it must not be substituted into I_J without retaining those equations or proving the equivalent ideal map.

From the printed definitions `d1=n`, `d2=K`, `q1=−m`, `q2=M2+m`, the numerical invariant is

    D2=−((-m)n+(M2+m)K)/K=L−(M2+m),
    W=M2+m.

For the six class files, M2 is the first entry of the shortened `M_prime` list. In roster complete child chains, the first entry is already M1=−m; M2 is the second entry. Confusing those conventions changes both D2 and W.

| Chart | K | L | D2 | wt(lambda) | Bidegrees of lambda, lambda², lambda³ |
|---|---:|---:|---:|---:|---|
| 70: n24m16, M−12,−2,5 | 8 | 48 | 44 | 4 | (0,4), (0,8), (0,12) |
| 109: n18m12, M2,9 | 6 | 36 | 22 | 14 | (0,14), (0,28), (0,42) |
| 127: n24m18, M−15,14 | 6 | 72 | 69 | 3 | (0,3), (0,6), (0,9) |
| 171: n24m16, M12,17 | 8 | 48 | 20 | 28 | (0,28), (0,56), (0,84) |
| 341: n24m18, M9,20 | 6 | 72 | 45 | 27 | (0,27), (0,54), (0,81) |
| 455: n16m12, M6,13 | 4 | 48 | 30 | 18 | (0,18), (0,36), (0,54) |
| R001: n21m14, M−14,16 | 7 | 42 | 12 | 30 | (0,30), (0,60), (0,90) |
| R002: n15m10, M−10,11 | 5 | 30 | 9 | 21 | (0,21), (0,42), (0,63) |
| R003: n15m10, M−10,11 | 5 | 30 | 9 | 21 | (0,21), (0,42), (0,63) |
| R004: n16m12, M−12,13 | 4 | 48 | 23 | 25 | (0,25), (0,50), (0,75) |

**Structural proposition.** `I_J ∩ R_(first charge 0)=0`. Indeed, every product of a coefficient-ring monomial with a Jacobian row has first charge at least 1. The first-charge-zero projection of any element of I_J is therefore zero. Consequently every nonzero polynomial lambda of first charge zero satisfies `lambda^N∉I_J` for ALL N≥1. This is stronger than bounded nonmembership and does not require a Gröbner basis.

Equivalently, set every positive-first-charge coefficient coordinate and c equal to zero while retaining all first-charge-zero coordinates. The resulting P,Q depend only on y, so all Jacobian equations vanish identically. Thus R/I_J maps onto the polynomial ring R0 in the charge-zero coordinates. If lambda is a nonzero polynomial in those coordinates, the map extends

    R[Z]/(I_J,Z lambda−1) -> R0[lambda^−1]

by Z↦lambda^−1. The receiver on the right is nonzero, so the localized ideal is proper. This proof is an algebraic properness statement about the NECESSARY ENLARGEMENT. It supplies neither a Keller pair nor a source realization.

There are two distinct possible enlargements, and their effects must be explicit. (i) Adjoining Tc−1 destroys the nonnegative grading and invalidates this projection, because c=0 cannot satisfy it. (ii) Adjoining the characteristic upper-degree rows introduces first-charge-zero relations; then the correct membership ideal is I_J+U, and the statement becomes `(I_J+U)_charge0=(U)_charge0`. A nonzero raw polynomial lambda need not stay nonzero modulo U. Both distinctions are material; neither can be hidden in the notation I.

## The localizer cannot be homogeneous for positive wp

For W>0, `Z lambda−1` is homogeneous in the original y-deficit grading only if `wt(Z)=−W`. Such a weight is inadmissible in a strictly positive global wp order. Giving Z weight 1 produces terms of degrees W+1 and 0. Therefore a direct `std(I_J+(Z lambda−1))` with positive wp and degBound is NOT the homogeneous truncated computation licensed in the frozen grading report.

The current primary Singular manual source makes the restriction explicit: its degBound section permits global inhomogeneous input only for dp/Dp; it further states that std uses ordinary total degree for block orders, while slimgb always does. Reference: [Singular reference.doc, degBound](https://github.com/Singular/Singular/blob/spielwiese/doc/reference.doc), fetched 2026-09-06. The installed version is Singular 4.3.2 (4330, 64 bit), Apr 1 2024. A single `wp(w1,...,wr)` block is necessary for the intended positive weighted cutoff.

Any explicit rational UNIT cofactor identity found by a partial computation is still a genuine identity. Discarding entire original rows is safe for that positive conclusion because it uses a subideal. In contrast, replacing a row by its low-degree term truncation changes the row and is not safe without an ideal-lift proof. A partial non-unit, including one at a declared inhomogeneous wp degBound, proves no finite-weight completeness statement by itself. “No relation of weight ≤B” should be reserved for a certified homogeneous membership/certificate block, and must specify the target relation.

## Safe homogenized localizer recipe

Introduce s and give both Z and s weight 1. Keep all original positive parameter weights and form

    H=(I_J, Z lambda−s^(W+1)) ⊂ Q[original variables,Z,s].

If upper characteristic rows U are required, include their homogeneous images as well. Then H is positively homogeneous. Run `std` with a SINGLE wp block through a declared B. A unit after dehomogenizing s=1 has a certificate with maximal weighted summand degree at most B iff `s^B∈H`; homogeneous projection proves this equivalence. Thus `NF_H(s^B)≠0`, backed by all required S-pairs through B, means no certificate of that bounded homogenized degree. It does NOT mean the affine localized ideal is proper.

To cover a potential homogeneous identity `lambda^N=Σ a_i f_i`, whose summands have weight NW, it suffices to take `B=N(W+1)`. Explicitly, writing u=Z lambda and v=s^(W+1),

    s^(N(W+1)) = Z^N lambda^N
       −(Z lambda−s^(W+1)) Σ_(k=0)^(N−1) u^k v^(N−1−k).

Replace lambda^N by its cofactor expression to obtain a homogeneous certificate. Conversely dehomogenizing s=1 gives the Rabinowitsch unit identity. In the requested notation `B=NW+margin`, a fixed margin≥3 covers N=1,2,3 for this translation. Using margin=3 gives first-class cutoffs 7,11,15; these have an exact interpretation absent from direct inhomogeneous wp truncation.

If the full chart additionally includes Tc−1, give T weight 1 and homogenize it as `Tc−s^(D+1)`. It first enters at weight D+1. For the 70-coordinate class D=39, every cutoff 7,11,15 lies below that row. The requested first three low-weight probes cannot then see the Keller localizer. This is a mathematical consequence of that grading and cutoff, not a claim of class survival.

For a bounded homogeneous standard basis G, independently verify each required S-pair whose weighted lcm degree is ≤B reduces to zero, and verify input images through B. Higher-degree homogeneous rows cannot contribute at or below B. A zero target remainder must be accompanied by a cofactor identity in the original declared ring if promoted as a kill. A nonzero remainder requires bounded Buchberger closure, not merely all original generators reducing to zero. Do not apply `dim`, `vdim`, Hilbert-series or radical conclusions to an incompletely computed standard basis.

The frozen `guided_gb.py` is a full-standard-basis wrapper. Its generic full-basis/dimension acceptance markers cannot be used unchanged as a finite-cutoff verifier. In particular, reduction of all generators to zero is not a proof that all required critical pairs have been processed. No modular properness promotion is needed or licensed here; all requested identities are over Q.

## Cone vertex and exact-Q controls

At Delta the coefficient blocks alpha_i,beta_i are constants, while h stays an arbitrary monic polynomial. Every constant-coefficient target polynomial in P,Q belongs to k[h]. Every nonconstant nonzero member of k[h] has y-degree a positive multiple of K. The values D2 in the table are all positive and not divisible by K. Consequently Delta cannot satisfy the WHOLE upper-degree-plus-attained-leader block with lambda≠0.

There is a crucial distinction between the chosen canonical h-adic lift and an ordinary y-coefficient. Write D2=JK+a, with 0<a<K in all ten cases, and take the canonical lift lambda=`[x^0 y^a]H_J` after the declared h-adic target pivots. On Delta every H_j is a scalar polynomial in the constant block coordinates: division of these constants by the monic degree-K h creates no carry, and the family corrections remain polynomials in h. Hence this CANONICAL H-ADIC lambda vanishes on Delta globally, even before upper-degree rows are imposed. This is the right lift for the present lane's direct vertex test.

The ORDINARY raw coefficient `[y^D2]T2` need not vanish for arbitrary h before the upper-degree equations; intermediate y powers occur in h^j. The frozen characteristic report's warning applies to that different coefficient. Ordinary and canonical h-adic leaders agree only on the declared upper-degree locus. For an ordinary-coefficient vertex control, retain that upper block or normal-form by it first. Once the chosen lambda=0 consequence has been checked, the localizer gives the exact identity

    1 = Z lambda − (Z lambda−1).

If lambda=Σ a_i u_i modulo Delta and the necessary upper rows, the actual certificate is `1=Σ Z a_i u_i−(Z lambda−1)`. This proves UNIT ON DELTA, not on the unrestricted class. A control must retain all allowed constant block coefficients; assigning them arbitrarily can turn it into a point control.

The retained tiny exact-Q script `grading-controls.sing` and output `grading-controls.out` establish these backend controls:

* In Q[b,a], wp(2,1), `(b²−a⁴,ab)`: a⁵ survives cutoff 4, vanishes at cutoff 5, and a⁴ stays nonzero. Exact identity: `a⁵=−a(b²−a⁴)+b(ab)`.
* In Q[l,Z,s], wp(1,1,1), H=(l²,Zl−s²): s³ survives cutoff 3 and s⁴ vanishes at cutoff 4. Exact identity: `s⁴=Z²l²−(Zl+s²)(Zl−s²)`.
* Full exact vertex ideal `(l,Zl−1)` is unit with `1=Zl−(Zl−1)`; removing the vertex row leaves `(Zl−1)` proper, witnessed at l=Z=1.

All 12 assertion markers and the completion marker are 1. Singular's “is no standard basis” warnings in the truncated controls are expected reminders that finite completion must not be called a full basis. They are not suppressed or reclassified as proof of global completion.

The additional independent script `verify_j0_witnesses.py` and 6,160-byte `j0-witness-controls.json` check explicit exact-degree, zero-Jacobian points for all ten strengthened necessary charts, including ALL upper T2 rows and the lambda localizer. Each witness has h=y^K and univariate P,Q supported in allowed b=0 blocks, with beta1 absent and both terminal constant gauges respected. Nine are rational; R004 lies over the exact quadratic field Q[a]/(54a²−36a+5). There, expanded Q⁴−P³ has degrees 23,18,13,8,3 and lambda=2/243−4a/81; its resultant with the quadratic is 8/6561, so it is nonzero at both quadratic roots. All ten controls pass. These points prove properness of the strengthened necessary enlargement with c=0; they do not satisfy Tc−1 and are not Keller pairs or source realizations.

Independent emitted-formula audit: a separate sparse signed-monomial parser read every one of the ten expanded lambda files, computed each factor weight from its actual block name/index, and evaluated each term with exact rational arithmetic at the independently checked witnesses (exact quadratic remainder for R004). ALL 76,134 monomials have bidegree (0,W), and every evaluated formula equals the actual expanded T2 leader. Term counts in the table order are 6,108,4,7075,42866,2672,3263,417,417,19306. The independent audit took 2.38 seconds and all assertions passed. The derivation driver was also inspected: ascending monic carry computes the unique h-adic expansion, target pivots use the constant digit at distinct leading h-degrees, and target monomials below D2 cannot affect the chosen leader digit.

No class-emptiness or new exit-price assertion is made by this audit. The notation and cutoff repairs above are needed before interpreting any larger computation.
