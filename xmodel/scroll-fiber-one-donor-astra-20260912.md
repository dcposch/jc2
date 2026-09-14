# Fiber-degree-one Hirzebruch donors: all-line exclusion

MANUAL / PRODUCER-CHECKED / UNPROMOTED. First action2026-09-12 05:51:31UTC; targets absent. Original reserve06:10/HARD06:13UTC unchanged. Exact inputs are the accepted first-leg log integration, the frozen cubic-scroll report for scope/history only, and COORDINATION.md. All three were pinned before fresh WHOLE reads; no linked provenance was followed. No scientific execution, code, coefficients, worker or network is authorized or used.

Quantity: for every e>=0, finite complex morphism Phi:F_e->P2 with Phi^*O(1).f=1, and every target line ell, decide whether A2 can dominate the full complement of ramification and Phi^*ell. The first leg need not be finite or etale. This report tests only that exact client.

## 1. Exact verdict and divisors

The proposed exclusion is proved at producer level, with the accepted all-contact two-section log theorem retained as a premise. Write Y=F_e, pi:Y->P1 for the ruling, E for a section with E^2=-e, and f for a fiber. Put L=Phi^*O(1), D=Phi^*ell as a scheme divisor, and R=Ram(Phi) as the effective Jacobian divisor, including all components and their multiplicities. A finite morphism here is surjective: its closed image has dimension2. Characteristic0 makes it generically separable, so R is defined by a nonzero Jacobian determinant and

    K_Y=-2E-(e+2)f,  L=E+b f,
    R~K_Y+3L=E+(3b-e-2)f.

Finiteness makes L ample. Hence b>e, and the geometric degree

    d=deg(Phi)=L^2=2b-e >= e+2 >=2.

Both effective divisors D and R have fiber degree1. Every horizontal irreducible component has positive integral fiber degree and every multiplicity is positive integral. Therefore each divisor has exactly one horizontal component, with fiber degree1 and multiplicity1; all other components, if any, are ruling fibers, with arbitrary positive multiplicities retained.

Each horizontal component C is a smooth section, not just a rational curve: pi|C is proper and quasi-finite, hence finite, and has degree1. It is birational to the normal curve P1, so it is an isomorphism. This argument does not assume C normal in advance.

The two horizontal sections are distinct. Otherwise their common section C lies over ell and belongs to R. Its coefficient in D is1, so the ramification index at its generic point over ell is1. In characteristic0 the residue-field map of curves is separable; the generic Jacobian order along C is then0, contrary to C being a component of R. Equivalently, at its generic point the reduced line equation gives a nonzero normal derivative and the finite map C->ell gives a nonzero tangential derivative. Neither argument assumes a generic target line.

## 2. Three or more boundary components: a unit

Let B_1,...,B_N be the DISTINCT irreducible components of supp(D) union supp(R). They include the two different horizontal sections, so N>=2. If N>=3, Pic(Y)=Z E direct-sum Z f supplies integers n_i, not all zero, with sum n_i[B_i]=0. This is equality in Pic, not merely numerical equivalence; there is no Pic0 or torsion obstruction. Thus a nonconstant rational function h has divisor sum n_i B_i. On the smooth complement U it and its inverse are regular, giving a nonconstant unit.

A dominant everywhere-defined morphism A2->U would pull h back to a unit of C[x,y], hence a nonzero constant. Dominance injects function fields, contradicting h nonconstant. This proves the claim whenever ANY vertical boundary component occurs, including a vertical component shared by D and R or carrying multiplicity greater than1. No reducedness of the entire D or R is assumed in this branch.

## 3. Exactly two components: the literal ramification restriction

If N=2, the distinct horizontal sections already exhaust the boundary. Fiber degree1 forces D and R themselves to be reduced, irreducible, distinct smooth sections; there are no vertical components. In particular D~L and h=Phi|D:D->ell is a finite morphism P1->P1 of degree d: h^*O_ell(1)=L|D has degree L.D=L^2=d.

The scheme ramification divisor of h equals R|D, even for a special line or a tangency. To see the equality at every p in D, take local complex coordinates (u,v) on the target with ell={v=0}. Because the FULL pullback divisor is the smooth reduced D, x=Phi^*v is a local coordinate on Y transverse to D. Complete it to coordinates (x,t). The map is

    (x,t) |-> (g(x,t),x).

Its Jacobian is -partial g/partial t. Restricting its zero divisor to x=0 gives exactly the derivative of h:t|->g(0,t). The derivative is not identically zero in characteristic0. Thus the effective Cartier intersection R|D, including all intersection/contact multiplicities, is precisely Ram(h), not just linearly equivalent to it. No contribution at a removed vertical component was forgotten: this is the branch where none exists.

Riemann-Hurwitz gives deg Ram(h)=2d-2. Each point has ramification multiplicity e_p(h)-1<=d-1, since e_p(h)<=d. As d>=2, a divisor of degree2d-2 cannot be supported at just one point. Therefore D and R meet in at least two distinct points. Since pi|D is an isomorphism, those points lie over at least two DISTINCT RULING-BASE points. Their images in ell are irrelevant and are not being identified with ruling-base coordinates.

## 4. Apply the accepted all-contact theorem, with arbitrary first leg

In the two-component branch set D_infinity=D and D_0=R in the pinned August30 integration, and S=pi(D intersect R). The curve R minus D is closed in Y minus D and maps isomorphically onto P1 minus S. These are exactly the imported theorem's hypotheses. It already includes arbitrary finite contact orders. For every n>=1 its formula gives

    bar-P_n(U)=n*(|S|-2)+1 >=1.

Thus bar-kappa(U)>=0. The same accepted integration supplies injective pullback of logarithmic pluricanonical forms along any dominant generically finite morphism of smooth complex quasi-projective varieties, including nonproper morphisms. A dominant morphism from A2 to this surface is generically finite, whatever its degree. Since bar-kappa(A2)=-infinity, no such first leg exists. No properness, finiteness or etaleness of that first leg was inserted.

Together with the unit branch, this proves the exact all-e/all-degree/fiber-degree-one/all-target-line assertion. The source restriction L.f=1 is essential to this proof; no claim for higher-fiber-degree divisors is made.

## 5. Controls and scope boundaries

One-collision abstract sections are NOT excluded by the log theorem, and there is an explicit stronger control. On F_0=P1_t times P1_w take D_infinity={w=infinity} and D_0={w=t}. They meet only at (infinity,infinity). Their complement is actually A2: coordinates (w,z) give

    (w,z) |-> (t=[w*z+1:z], w),
    z=t_1/(t_0-w*t_1).

The denominator of the inverse is nonzero precisely away from the removed diagonal, and z=0 includes the full allowed part of the fiber t=infinity. These formulas are mutually inverse and everywhere defined on their stated domains. Thus a positive contact count or even two smooth horizontal sections does not by itself prove non-domination. The finite-map constraints rule out precisely this dangerous situation: if these were the entire line/ramification boundary, the scheme derivative calculation and degree-d Riemann-Hurwitz would require at least two ruling-base collisions. As a class check for this example, neither labeling of its two section classes satisfies both L ample and R~K+3L.

Multiplicity/shared-component control: one must count DISTINCT support components for the Picard-unit argument, not count a double fiber twice. A shared vertical component still adds a third component beyond the two horizontal sections. Horizontal sharing is not simply deleted; it is excluded by the generic reduced-pullback/separable-tangent argument. Only after proving there are exactly two support components may D and R be replaced by reduced sections. Tangency control: intersection multiplicities are e_p(h)-1, not a count of target branch values; one highly tangent collision cannot absorb 2d-2 because each e_p(h)<=d.

History/scope collision: the cubic F1 donor exclusion in the charged ROOT report is a known narrower client, not a new mechanism or premise needed for this proof. The accepted log theorem and units obstruction are also retained known mechanisms. The present attachment ranges over every Hirzebruch surface and all finite degrees subject to the exact ruling-degree-one hypothesis. It is NOT all quartic covers, all rational compactifications, all normalizations, all cubic block quotients, an actual Keller construction, or a JC2 theorem. No claim of global literature novelty; ROOT separately owns that checksum.

QUANTITY settled at producer level: nonexistence of dominant regular A2 first legs into the specified full open donor, uniformly over its stated parameters. CHEAPEST TEST performed: the manual support split and exact local derivative restriction, with the explicit one-collision A2 control. No numerical experiment or scientific subprocess. No mathematical OPEN is raised within the exact statement; promotion still requires ONE different-model FIRST review, an estimated <=20-minute manual check (planning only, not measured or authorized here). A failure of that review would quarantine this report; nothing downstream is authorized now.

## 6. Custody and read scope

Fresh WHOLE reads: first-leg integration all159lines; cubic-scroll report all252lines including its seal; COORDINATION all806lines in consecutive unclipped ranges1-220,221-440,441-660,661-806. Each exact supplied SHA was checked before any body read, and all three are rechecked before sealing. Links inside them are uncharged provenance, not followed. Own report and PINS receive complete readback; own final/manifest/custody target collisions are checked before the last marker. The report uses the ordinary private-partial begin/close/finalize/expected-verify transaction; custody excludes its own digest and includes all input/owned hashes. No shared, old corrected-flow, protected or live peer artifact is changed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10082`.
- Body SHA-256:
  `12702a6f68508808ccb1d614e6142adcfe250eecf3a0a53f7a7c4f5dd8434471`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
