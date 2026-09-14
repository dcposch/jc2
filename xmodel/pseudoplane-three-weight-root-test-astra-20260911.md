# Three-weight pseudo-plane critical-point root test

MANUAL BOUNDED DISCRIMINATOR / new claims UNREVIEWED. No code or source outcome.

Actual first action2026-09-11 08:58:33 UTC; own targets absent. ORIGINAL reserve09:11/HARD09:14 UTC, never reset. Exactly the nominated separated-weight producer, its manifest and designated FIRST are hash-pinned before fresh WHOLE reads. Their accepted chart and B/D/C/E results are imported, not re-reviewed. No linked, historical, mutable or pending input is consumed.

## Exact family and initial reduction

On the accepted surface R=C[A,U,Z]/(U²−A−A²Z), put t=AZ. The target is arbitrary d≥1, nonzero f,g in C[t], q in C[t], and H=Uf(t)+Z^d g(t)+q(t), with no degree cap. On U≠0 use the accepted coordinates u=U, t≠−1 and A=u²/(1+t), Z=t(1+t)/u². Set h=t^d(1+t)^d g, N=2d+1 and K=2d h f'+f h'. Where f h≠0, the critical equations are

u^N=2d h/f,   K+f u^(2d)q'=0.

They follow by multiplying H_u=f−2d u^(−N)h and H_t=u f'+u^(−2d)h'+q' by the displayed units. This preliminary chart reduction is not a claim that all roots of an eliminant are admissible.

## 1. Verdict, eliminant and exact lifts

THEOREM: every H in this entire family has a critical point, with no degree or squarefreeness assumption. Consequently it cannot be a coordinate of a nonzero scalar-bracket pair with ANY regular mate. The proof below establishes a root away from all discarded factors; no general arbitrary-H theorem is asserted.

Write k=2d, N=k+1 and

E=K^N+(kh)^k f(q')^N,  M=h f^k.

Raising K=−f u^k q' to the odd power N and using u^N=kh/f gives E=0. There is a useful exact normalization, not just a set-theoretic elimination:

M'=f^(k−1)K,
f^((k−1)N) E=(M')^N+k^k M^k(q')^N=:D.

The second equality uses1+(k−1)N=k². Where M≠0, put v=u f(t); this is an invertible coordinate change. The original H becomes

H=v+M(t)/v^k+q(t),

and its critical equations are exactly v^N=kM, M'+v^k q'=0. Every zero t0 of D with M(t0)≠0 lifts as follows. If q'(t0)=0, then D=0 implies M'(t0)=0; choose any nonzero Nth root v of kM. If q'(t0)≠0, D=0 implies M'(t0)≠0; set v=−kM q'/M'. Because k is even and N=k+1 is odd, D=0 yields v^k=−M'/q' and then v^N=kM. These are the required equations, including their signs. Finally u=v/f(t0) and the accepted chart recover A,U,Z. M≠0 entails f,h≠0 and t0≠0,−1. Thus no boundary point, zero leading factor or undefined quotient is smuggled into the construction.

If D is identically zero, choose t away from the finitely many zeros of M; the same lifting cases apply, so critical points already exist. If q'=0 identically, the accepted derivative-root count for M, which has distinct roots0 and−1, supplies M'(t0)=0 with M(t0)≠0, and the first lift applies. It remains to prove that a nonzero D with q'≠0 cannot have ALL its zeros among those of M.

## 2. Elementary polynomial abc bound, proved here

Let nonzero pairwise-coprime polynomials a,b,c satisfy a+b=c, with at least one nonconstant. Let nu count the distinct roots of abc. Then max(deg a,deg b,deg c)≤nu−1. Indeed W=a'b−ab' is nonzero: otherwise a/b is constant in characteristic zero, contradicting coprimality and nonconstancy. At a root of any of a,b,c of multiplicity e, W has multiplicity at least e−1; for c use W=c'b−cb'. Therefore deg W≥deg a+deg b+deg c−nu. Comparing with deg W≤deg a+deg b−1 gives deg c≤nu−1, and permutation gives the other two bounds. This is the whole argument used; no outside theorem/source is imported.

We will also use its immediate equal-degree refinement. If deg a=deg b=deg c=L and nu≤L+1, the top terms in a'b−ab' cancel, so deg W≤2L−2, whereas the preceding lower bound gives deg W≥3L−nu≥2L−1. Thus these equal degrees are impossible under that root bound.

## 3. Root accounting: all k≥4, and the only remaining k=2 equality case

Suppose, for contradiction, that D≠0 has no root off M=0. Write the distinct roots of M as alpha_i, i=1,...,r, with multiplicities m_i; r≥2. Let c_i=ord_(alpha_i)(q') and let ell0=deg(q')−sum c_i≥0, the total multiplicity of q' zeros off M. Off M, M' and q' have no common zero, since such a zero would make D vanish. The total multiplicity of M' zeros off M is r−1, by the characteristic-zero derivative multiplicity formula.

Divide a0=(M')^N and b0=k^k M^k(q')^N by their monic gcd J, and put a=a0/J, b=b0/J, c=D/J. These are nonzero pairwise-coprime polynomials. J is supported on M=0. At alpha_i set

alpha_i^*=max(m_i−N(c_i+1),0),
beta_i^*=max(N(c_i+1)−m_i,0).

These are exactly the multiplicities remaining in a and b: the two original orders are N(m_i−1) and k m_i+N c_i. Hence, writing R0=r−1≥1,

deg a=N R0+sum alpha_i^*,
deg b=N ell0+sum beta_i^*.

All roots of c lie on M. The union of roots of abc therefore has size at most (r−1)+ell0+r=2R0+ell0+1: off M, count M' roots by r−1 and q' roots by ell0; on M there are only r locations. Applying the proved bound twice gives

ell0≥(N−2)R0+sum alpha_i^*,
(N−1)ell0+sum beta_i^*≤2R0.

For odd N≥5 these are incompatible, since R0≥1. For N=3 they force EXACTLY ell0=R0 and every alpha_i^*=beta_i^*=0. Thus m_i=3(c_i+1) at every root. Moreover deg a=deg b=3R0=:L0, and the distinct-root bound is L0+1. The polynomial abc bound forces equality in that root count. Consequently every root of M occurs in abc; since a,b are nonzero there, each is a root of c. Finally deg c<L0 by the equal-degree refinement above (and the ordinary bound deg c≤L0). These equality consequences are essential and are retained below.

## 4. The cubic equality case cannot occur

Now N=3, k=2. Write M=lambda B³, lambda≠0, with B monic and roots alpha_i of multiplicities e_i=c_i+1. Set n=deg B=sum e_i. The equality ell0=r−1 gives deg(q')=sum(e_i−1)+(r−1)=n−1, so deg q=n. The derivative B' also has degree n−1. Direct expansion gives

D=lambda² B^6 [27 lambda (B')³+4(q')³].

At alpha_i, B' and q' have order exactly e_i−1. Define the nonzero limit rho_i=(q'/B')(alpha_i). Since alpha_i is a root of c=D/J, its leading normalized terms cancel, so

rho_i³=−27 lambda/4.

At infinity let rho_inf=lc(q')/lc(B'). The inequality deg c<deg a=deg b means the leading terms of a0+b0 cancel before division by J. Equivalently the leading terms in the square brackets cancel, so rho_inf³=−27 lambda/4 as well. All rho_i and rho_inf are among the same three equimodular complex cube roots of a nonzero number.

The rational function (q'−rho_inf B')/B has degree at most−2 at infinity and at most simple poles at the alpha_i. Its finite residues are exactly e_i(rho_i−rho_inf), because B'/B has residue e_i. Partial fractions, or just the coefficient of1/t at infinity, therefore give

sum e_i rho_i = rho_inf sum e_i.

Divide by rho_inf and take real parts. Each ratio is1 or a nontrivial cube root of unity, whose real part is−1/2. Every e_i is a positive integer. The displayed weighted average equals1 only when ALL rho_i=rho_inf.

Choose another cube root rho≠rho_inf of−27 lambda/4. The polynomial q'−rho B' has degree n−1, since its leading coefficient is nonzero. At every alpha_i it has order exactly e_i−1, as rho_i−rho≠0. Its remaining r−1≥1 zeros, counted with multiplicity, lie OFF B=0. But it is a factor of27 lambda(B')³+4(q')³, so any such zero makes D vanish off M=0, contradicting the supposition. This closes the last equality case.

Thus for all d≥1 the normalized eliminant D is identically zero or has a root off M; in either case Section1 produces an actual critical point of the original H on U≠0. This proves the theorem for arbitrary f,g,q degrees. No multiplicity resonance, leading-degree cancellation or off-chart exception remains in the argument.

## 5. Controls, consequences and limits

The two-distinct-root hypothesis in the root argument is load-bearing. In the auxiliary cylinder C*×C with coordinates v,t, take M=t, q=0 and Phi=v+t/v^k. Its t derivative is v^−k, never zero, and the normalized eliminant is1. This is a manual countercontrol to any root lemma that forgets the two forced roots of M. It is NOT asserted to be an example in the original family, whose M=h f^k always has roots0 and−1. No execution or fixture is used.

Inside the actual surface, dropping the hypothesis g≠0 gives the accepted globally submersive family U+q(AZ), with constant boundary. Hence the theorem cannot be enlarged by silently allowing the Z^d term to disappear. Neither control supplies a scalar mate.

Because a biderivation vanishes at a point where the differential of its first entry vanishes, the constructed critical point excludes {H,G}=c≠0 for every regular G in R. This is an immediate obstruction consequence, with G unrestricted; it is not a converse equivalence between submersivity and existence of a mate. Arbitrary additional homogeneous components, all arbitrary normal forms in R, a general boundary-degree classification, rational/localized mates, other characteristics, source coverage and JC2 remain outside scope. In particular no conclusion about all H follows merely because f,g,q here have unbounded degree.

QUANTITY: does this new all-degree three-weight root theorem survive independent static review, especially the N=3 equality/leading-cancellation/residue argument? CHEAPEST TEST: one focused12-minute UNMEASURED manual review of the exact normalized identity, off-M lifts, internally proved polynomial bound, root-count equalities and the positive multiplicity cube-root average. This is a planning figure, not a runtime forecast, review launch or follow-on authorization. ROOT's bounded history note is not exhaustive novelty certification; this task performed no history or literature search and makes no novelty claim.

Own-only COLLISIONS: NONE; final report/manifest/box were absent at08:58:33. Only this report transaction and same-tag PINS/custody are authored. Exactly three frozen inputs are fresh-WHOLE; no linked reports, ledgers, pending bytes, coefficient payload, code, scientific subprocess/import/AST/syntax/test/CAS/dummy, network/AWS/SSH/Git/process control, protected/shared access or agents were used. The normalization hint arrived from ROOT after the same identity had been derived here; it was not adopted as a proof premise. The polynomial bound is proved inside the report, not imported from an external source.

Closeout09:07:35 UTC: own report and PINS freshly WHOLE without clipping; all3 input postpins and owned PINS match. Final report/manifest remain absent; no standalone marker yet; QUANTITY/CHEAPEST TEST/numeric UNMEASURED wall and collision check complete. Primes throughout denote ordinary differentiation in t. The bounded theorem is complete as a manual UNREVIEWED result, including all exceptional lifts and the cubic equality case. This marker ends mathematical/report authorship. Only documentary close/finalize/expected verification, sealed readback and custody remain before ORIGINAL09:11 reserve/09:14 hard stop.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11048`.
- Body SHA-256:
  `63b9cfae708dc93681bd4443ad9996659f440c914e5d5fc4b0ea6f9eff8e90b9`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
