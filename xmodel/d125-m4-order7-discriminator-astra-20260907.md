# D125: an order-seven obstruction, with the moving reference retained

2026-09-07. **DESK PASS, PROVISIONAL pending independent review.** The exact six-jet `d32b3965…` does not extend modulo s⁸. Changing A₅,A₆ and their compatible B coefficients cannot remove its obstruction while keeping its lower C,D data. A separately proved moving-reference argument yields the stronger scoped conclusion: no genuine finite k=s⁴ arc through a generic t₀≠−3 boundary center exists. This does not invalidate the six-jet modulo s⁷, exclude other ramification orders, or imply guarded-source emptiness.

## 1. Literal fixed prefix and the coefficient-seven pole

Use the exact formulas, field-algebra condition b⁴=3 and t₀=−4 from the terminal parent report. Its A coefficients are

    A₀=R³, A₂=RC, A₃=D, A₄=U, A₁=A₅=A₆=0,

and B through6 is the binomial five-thirds expansion with the retained γs⁶X term, where X=A^(1/3), γ=−5b²/9 and X₀=R. The root is used only in the formal localization K[g,p,R⁻¹][[s]], not asserted polynomial.

For a literal extension, add s⁷A₇ and s⁷B₇ without changing those earlier coefficients. The coefficient of s⁷ in X⁵ is

    Q₇=(5/3)R²A₇+(10/9)DU/R−(5/27)C²D/R².

The factor−5/27 comes from the three placements of A₃ in the cubic binomial term. Since A₁=0, γs⁶X has NO order7 term for this fixed reference. All Jacobian coefficients through7 must vanish: the prescribed nonzero target starts only at s¹².

After subtracting X⁵+γs⁶X, the first possible difference is s⁷Z₇. Its Jacobian equation gives [R,Z₇]=0. Clearing R² makes this a polynomial-centralizer identity. The accepted centralizer K[R] therefore gives

    R²(B₇−Q₇)=h(R).

Every polynomial on the left is odd under (g,p)→(−g,−p); thus h is odd, so R divides h(R). Equivalently, an odd localized-centralizer element with pole order≤2 can have a scalar/R pole, but NOT a scalar/R² pole. Reducing modulo R forces the necessary condition

    R divides C²D.                                      (7)

Neither the polynomial A₇ correction nor the simple-pole DU/R term can alter this double-pole condition.

## 2. A small exact contradiction for the fixed prefix

The actual parent data satisfy R=pT and

    C=b²(r²−TZ), D=(b³/3)(r³−Tq), r=g²p+gp²+p.

On T=0, C²D=b⁷r⁷/3. A hand-checkable certificate uses the finite nonzero algebra

    Q[b,a]/(b⁴−3, a⁴−4a²+1)

and evaluates the source coordinates at g=0,p=a. Here T=0, r=a, and both b and a are units:

    b⁻¹=b³/3,       a⁻¹=4a−a³.

The double-pole numerator after clearing R² is 5b⁷a⁷/81, a unit, contradicting (7). The checker multiplies it by (81/5)(b³/3)⁷(4a−a³)⁷ and reduces exactly to1. This is an evaluation certificate for a polynomial divisibility obstruction, not a source/Keller point.

Alternatively one may pass to any algebraic-closure values of b,a satisfying those equations; they are necessarily nonzero. The centralizer theorem is invoked over a characteristic-zero field there. Failure after scalar extension also excludes an extension over the parent's finite rational coefficient algebra, without an irreducibility assertion about that algebra.

## 3. Changing A₅ or A₆ is a different prefix, but does not repair this pole

The parent fixed A₅=A₆=0; replacing them is not a literal extension of its mod-s⁷ point. If one nevertheless allows arbitrary polynomial A₅,A₆ and adjusts B₅,B₆ compatibly while retaining A through4 and the earlier data, the order7 binomial coefficient becomes

    (5/3)R²A₇+(10/9)C A₅+(10/9)DU/R−(5/27)C²D/R².

A₆ does not enter the nonlinear order7 term. A₅ contributes only a polynomial. Scalar A target kernels are polynomial as well. An order5 scalar-X kernel, even before its low-e removal, would add only a simple pole at7; an order6 such kernel contributes nothing at7 when A₁=0. Hence none changes (7). This is an obstruction for the fixed lower C,D, not an assertion that the parent prefix may be silently changed. Altering earlier data is addressed only by the separate general proof below.

## 4. Generic k=s⁴: reconstruct the hypotheses instead of freezing motion

Let K be any characteristic-zero field and suppose all receiver coefficients form a finite K[[s]] arc, with k=s⁴ and generic center t₀≠−3. Work with the full source and accepted14g low equations

    a01=0, 9e=5kx, x²=3ky.

They are consequences in the genuine domain arc; they are NOT inferred by canceling nilpotent k in a raw truncated ring. The accepted field classification and these low rows give a pure-power center up to the permitted whole βA shear. Put h=t₀+3. Since y₀=−h³ is a unit,

    ord(x)=2,       x₂²=−3h³≠0.

Choose the unique formal reference t(s), with t(0)=t₀, satisfying y(s)=−(t(s)+3)³. Existence follows recursively using the unit3h², with no field extension. This is a reference choice, NOT a source automorphism. Let R_s=R_{t(s)}. The accepted first-tangent lemma14i applies because the target Jacobian starts at12: its first A motion is cR₀+dR₀²∂_tR₀. The a01 row kills c, and the chosen y reference removes the remaining tangent from A−R_s³. The first B kernel has its scalar-R part killed by e₁=0 and its scalar-R³ part removed by a whole B shear. Thus both departures start at2, and A's departure is nonzero there because x₂≠0.

For completeness, the order2/3 linear centralizers have only R and R³ kernels by parity and degree. The low e₂=e₃=0 kill the first; whole target shears remove the second. The order4 identity is the square-divisibility identity of the accepted tangent calculation with first departure order2: after division by R₀ and evaluation at the origin it gives R₀|F₂², where F=A−R_s³. R₀ is squarefree for h≠0, so F₂=R₀C. This step retains the intermediate order3 polynomial; it does not say that polynomial is divisible by R₀.

The literal source bounds now give C even, ordinary, degree≤8, weight≤0. Its low coefficients satisfy

    C(0)=0, C_p²=0, ξ:=[gp]C=−x₂/h, ξ²=−3h≠0.

Fix this coefficient polynomial C and write EXACTLY

    F=s²R_s C+s³D(s).

All later/nonmultiple orders, including arbitrary A₄,A₅,A₆,A₇, remain inside the unrestricted formal polynomial D(s). It is ordinary and has no constant or linear receiver term. No reparametrization s→s² and no deletion of transverse motion has been made.

## 5. The moving-reference derivative is only a simple pole

Let D₀=D(0) and set

    M(s)=(5/9)D(s)²−(5/81)C³.

The formal binomial identity through order7 is

    X⁵ = polynomial terms
          +s⁶ M(s)/R_s −(5/27)s⁷ C²D(s)/R_s²  (mod s⁸).

Here the polynomial terms are R_s⁵+(5/3)s²R_s³C+(5/3)s³R_s²D(s)
 +(5/9)s⁴R_sC²+(10/9)s⁵CD(s). All intermediate orders of every factor are retained.

There are no hidden earlier pole kernels. Localized centralizers are obtained by multiplying by powers of R₀ and applying the accepted polynomial centralizer. Through order5 the displayed coefficients are polynomial; oddness/degree allow only scalar-X and scalar-A kernels. Whole A shears remove the latter. All e₁,…,e₅ vanish, and the displayed polynomial terms have no linear receiver part, so every scalar-X coefficient through5 is zero. In particular the possible order4 kernel, which would create a linear-C pole at6 and another double-pole term at7, is killed by its actual p coefficient−hγ₄.

At6 the only possible negative kernel is scalar/R₀. Clearing R₀ and evaluating at the origin C(0)=D₀(0)=0 kills its scalar. Thus

    M₀=R₀W₀ for a polynomial W₀,
    R₀ divides 9D₀²−C³.                                (6)

Write R_s=R₀+sR₁+… and M(s)=M₀+sM₁+…. The order7 contribution of the PREVIOUS pole term is exactly

    M₁/R₀−M₀R₁/R₀² = (M₁−W₀R₁)/R₀.

This derivative must be included, but it has only a SIMPLE pole. The surviving γ₆s⁶X contributes γ₆R₁ at7, a polynomial; it is not zero for a moving reference. All remaining scalar-A kernels are polynomial. Therefore the SOLE possible double pole at7 is

    −5C²D₀/(27R₀²).

The same odd localized-centralizer argument as §1 forces R₀|C²D₀. This proves the new necessary condition with the moving t(s), its derivative, intermediate coefficients, A₄ freedom and all earlier kernels explicitly present.

## 6. The generic contradiction and its exact scope

Write R₀=pT. For h≠0, T is irreducible over Kbar: after division by p its monic cubic in g has constant p-adic valuation−1; an integer-valuation Laurent root is impossible by unique lowest terms. Primitivity gives polynomial irreducibility, and T mod p=−h makes p coprime to T. This is the same already charged elementary argument, not a new classification import.

In the domain Kbar[g,p]/(T), conditions (6) and (7) force C=D₀=0. Hence T|C. But w(T)=8 and w(C)≤0, so Q=C/T has weight≤−8. Its constant and gp coefficients are both zero, since those monomials have weights0 and−2. T has no linear terms and constant−h; consequently [gp](TQ)=0. This contradicts ξ²=−3h≠0. No additional ordinary-kernel classification or smooth-projective-curve claim is needed here.

**Provisional generic conclusion:** no such k=s⁴ finite arc exists. Equivalently, field-coefficient seven-jets with these explicitly imposed saturated low equations and generic-center conditions cannot satisfy all the source rows. This does not assert raw unsaturated-jet emptiness or a theorem over arbitrary extra nilpotent coefficient bases. The genuine six-jet remains valid modulo s⁷; the obstruction appears at the next coefficient. Nothing is proved about t₀=−3, other ramification orders, coefficients escaping to infinity, or existence of any finite degeneration from a guarded point.

## 7. Evidence and stop

Ten capped normal/−O controls pass with exact byte-identical rational-string witnesses and zero Assert nodes. The actual moving-reference identity rejects omission of its nonzero denominator derivative and a changed double-pole factor. Further controls reject an even centralizer pole and an incorrect point relation; the fixed-prefix numerator has an explicit inverse in the finite point algebra. No actual degree15/25 pair or large C/D product is expanded. All commands use −B and disable bytecode before helper import.

Witness SHA256 `d1cb0a54485d376a554885f8ed34ddcc735c37e2147d59b74a01ee227ef4b486`. Inputs and all owned evidence are pinned in custody. The whole terminal producer was read; its separate six-jet gate remained live and was NOT read. The parent construction remains provisional at this packet's cutoff, and the NEW fixed-prefix/generic conclusions require their own review, especially §§4–6. The bounded history check found the already charged kernel/mixed-order warnings; no exhaustive novelty claim is made. Root supplied the initial pole seed and the final weight simplification; this lane checked the moving-reference identity and exact unit certificate. No AWS/SSH/CAS, solver, shared edit, full builder or further descendant was used. All writers idle at publication. **STOP/IDLE.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11312`.
- Body SHA-256:
  `7ce708d7912599c9bf5e6ac545afdd59c91963b136c8c1e43b26958d8e70b0b5`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
