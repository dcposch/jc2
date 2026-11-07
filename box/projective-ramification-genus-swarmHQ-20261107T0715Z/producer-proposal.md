# Positive arithmetic genus of projective ramification — ROOT proposal

INTERNAL / UNPROMOTED / INDEPENDENT REVIEW PENDING. Producer: swarmHQ ROOT, MORIRAM0635, 2026-11-07.

## Proposed statement and scope

Over C, let X be a smooth irreducible projective surface, h:X→P² finite of degree N>1, and L a target line. Suppose an open immersion j:A²→X has image U such that h(U)⊂P² minus L and h is étale on U. Put H=h*L and let R be the full ramification divisor, with multiplicities, so R is linearly equivalent to K_X+3H.
The proposal is p_a(R)≥1, where p_a(R)=1−χ(O_R) is arithmetic genus, including for a nonreduced or disconnected divisor. In particular R cannot be a nonempty reduced SNC forest of smooth rational curves.
This is conditional on the named foundations and accepted interface below. It does not prove JC2. A resolution of a singular finite normalization generally destroys finiteness and cannot replace the assumed smooth X.

## Named foundations and retained interface

Named imports: adjunction/Riemann–Roch for Cartier divisors on a smooth projective surface; the surface cone/contraction theorem and classification of K-negative extremal contractions; divisor-class localization; and the classification/Picard lattice of rational ruled surfaces. Also use that P² has no nontrivial connected finite étale cover over C. These foundations are not newly source-audited here. The independent reviewer must check their exact use.
Accepted CUBIC-SCROLL-DONOR-1 interface: for every finite degree-three φ:F_1→P² and every target line L, there is no dominant everywhere-defined morphism A²→F_1 minus (support Ram(φ) union support φ*L).
Its MANUAL/BOOK-relative, different-model-reviewed scope is in public AUDIT.md20885–20920 at bc9a5972e4215486b0bb3fc6ae419f07781dbb9f; full AUDIT SHA2566a4d3cf4a008a42e3aef200354abb0670f256bc820f7d978ec0e60547368d295. Integration xmodel/cubic-scroll-donor-exclusion-root-20260912.md has full SHA256f5abd9086559b1cfdd6900baafcf339c1a8ad394917ab3141d23bc999403545a.
The interface is not re-audited or enlarged. In particular this proof must supply its own landing on F_1; no general cubic-cover classification is imported.

## Proposed proof

1. H is ample and H²=N. X is rational because it contains the dense open A². The effective ramification divisor R is disjoint from U. It is nonzero: otherwise the determinant of dh never vanishes, h is finite étale, and simple connectedness of P² gives N=1.
Assume p_a(R)≤0. Set D=2K_X+3H, which is linearly equivalent to K_X+R. Adjunction gives

    D·R = (K_X+R)·R = 2p_a(R)−2 < 0.

This identity uses the full Cartier divisor R with its multiplicities. Thus D is not nef.

2. The cone theorem gives a K-negative extremal ray on which D is negative: on the K-nonnegative part D is positive on every nonzero class because H is ample. A birational extremal curve E is a (-1)-curve, hence D·E=−2+3H·E≥1, impossible. If the contraction is to a point, X≅P² and H≅O(m) with m≥1; negativity gives −6+3m<0, so m=1 and N=1, also impossible.
The remaining contraction is to a curve. For its general fibre F, K_X·F=−2. Negativity and integrality imply H·F=1. The smooth rational surface is therefore a ruled surface F_n, n≥0, with Pic(X)≅Z². The contraction classification, including possible singular/reducible fibres, is an explicit review target; it must justify this conclusion without an additional minimality assumption.
Now R·F=−2+3=1.

3. R has exactly one horizontal irreducible component C, with coefficient1 and C·F=1; any other components are vertical. The effective divisor T=h*L likewise has exactly one horizontal component B, with coefficient1 and B·F=1.
C is not a component of T. Otherwise h(C)=L, and coefficient1 in R means ramification index2 at the generic point of C. Hence mult_C(T)=2, contradicting T·F=1. Thus C and B are distinct.

4. Every curve in support R or support T is a boundary curve of U. The divisor-class localization sequence is

    O(X)* → O(U)* → ⊕_{Z⊂X minus U, codim Z=1} Z[Z] → Cl(X) → Cl(U) → 0.

Both unit groups are C*, and Cl(U)=0. Hence boundary curves form an integral basis of Pic(X)≅Z². There are exactly two boundary curves, already the distinct C and B. No additional vertical component of R or T is possible. Therefore R=C and T=B, both with coefficient1. This only uses U⊂X minus (C union B); no equality of opens or absence of isolated missing points is assumed.

5. Write Pic(F_n)=Z[S]⊕Z[F], with S²=−n, S·F=1, F²=0. Since H·F=1, H=S+bF; ampleness gives b>n and N=H²=2b−n. The canonical formula gives

    K_X=−2S−(n+2)F,     R=S+(3b−n−2)F.

The boundary classes R and T=H form an integral basis, so their determinant has absolute value1:

    | b−(3b−n−2) | = | 2−N | = 1.

N>1 forces N=3. From 2b−n=3, b>n and n≥0, obtain n=1, b=2. Thus h is a finite cubic map F_1→P². The open immersion U≅A² gives a dominant everywhere-defined morphism into F_1 minus (support R union support h*L), contradicting exactly CUBIC-SCROLL-DONOR-1. Therefore p_a(R)≥1.
For the forest consequence, a nonempty reduced SNC rational forest with c connected components has χ(O_R)=c and p_a(R)=1−c≤0.

## Limits and review targets

Arithmetic genus is not geometric genus. Positive p_a can arise from singularities, incidence or multiplicities of rational components; it does not contradict the existing positive-geometric-genus donor obstruction. Singular projective normalizations and p_a(R)≥1 remain outside the exclusion. No actual normalization smoothness, global genericity or JC2 conclusion follows.
The Chisini-type source motivated a scope question only. None of its statements or proofs is a premise here. The history screen found the cubic-scroll interface and the distinct geometric-genus obstruction; selected lexical views do not establish novelty.
Hostile review must check the extremal-ray/ruled step, the C⊂T index contradiction, the boundary localization sequence even with possible isolated missing points, the integral determinant, and exact composition with the retained cubic-scroll interface. Try to find a counterexample satisfying the whole-A² and finite-map hypotheses.
Verdicts: CONFIRMED_AT_NAMED_FOUNDATIONS / GAP_FOUND / FALSE_WITH_CONTROL / INCOMPLETE. No promotion before independent review.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6398`.
- Body SHA-256:
  `a18462514403dd5dfcfc6a3435b5baae2a2c031cd921732e8e51412e7b7e51a7`.
- Frozen basis: `8b11a9d642cb0ae05ea57ceb1edbddf03a6d0083`.
