# Contractible whole nonproper-value curves are excluded

Producer: swarmHQ ROOT (configured coordinator gpt-6-astra); independent reviewer: configured gpt-5.6-sol/ultra. Hosted model identities are not independently verified.
Date: 2026-10-31 UTC. Basis: a8564152a8ea83c377848837381ca4e036db3aef.
Evidence tier: MANUAL, conditional on the named inherited foundations. Lifecycle: PROVISIONAL; independent PASS_CONDITIONAL. Novelty unassessed.

## Statement and review

At the retained actual finite-normalization, sheet-budget and zero-slack scope, a noninvertible plane polynomial Keller map has no nonempty contractible WHOLE nonproper-value curve, including reducible unions. Noncontractible curves remain open; this does not resolve JC2.
The [independent review](contractible-nonproper-curve-review-sol56-20261031T1240Z.md) checks all six steps of the [unchanged original candidate](../box/contractible-nonproper-curve-swarmHQ-20261031T1245Z/CANDIDATE.md). The mathematical excerpt below is byte-identical to that candidate; its original proposal wording is preserved. The irreducible/unibranch endpoint was already retained through Integration9 CUSP-A-VOID/SMOOTH-KILL. Selected prior records do not establish novelty.
Dependencies: [all-Keller sheet budget](all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md), [zero-slack/immersion equivalence](zero-slack-immersion-swarmHQ-root-sol56-20261031T103000Z.md), and the explicitly named classical curve/line theorems below. Their source proofs are not newly audited here.

## Statement and inherited inputs
Let F:U=A2_C -> Y=A2_C be a noninvertible polynomial Keller map of geometric degree N>1, with nonempty reduced nonproper curve D. Proposed statement: D is not topologically contractible, allowing reducible D.
Use the retained finite-normalization package h:X->Y: omitted smooth A1 curves E_i, image curves D_j with normalization A1, generic omitted masses r_i*delta_i, generic affine counts d_j=N-sum_{E_i->D_j}r_i*delta_i, and budget N-1=sum_i r_i*delta_i+S, S>=0. The reviewed zero-slack criterion gives positive slack at a selected nonimmersed image branch.
Named foundations: affine-curve normalization/Euler formulas; finite etale covers and Euler multiplicativity; Lin-Zaidenberg for an irreducible contractible plane curve; Abhyankar-Moh for an embedded smooth A1; and the Keller theorem that injectivity on a line implies invertibility. These are inherited foundations, not freshly source-audited here.

## 1. A contractible inverse component
Assume D contractible. Put Z=F^{-1}(D), reduced; etaleness makes the scheme-theoretic inverse reduced too. Outside D, F is finite etale of degree N. Therefore 1=chi(U)=N*(1-chi(D))+chi(Z), so chi(Z)=1. Compactly supported Euler characteristic is understood; for these curves it equals ordinary Euler characteristic.
For an irreducible affine curve H, chi(H)=2-2g-s-b, where g is the genus of its smooth projective normalization, s>=1 counts points at infinity, and b is the sum of finite branch-identification deficits. Thus chi(H)<=1; positivity means normalization A1 and everywhere unibranchness, hence H is homeomorphic to C.
Euler characteristic of a reduced union is the sum over irreducible components minus nonnegative intersection terms. Thus Z contains an irreducible component Gamma with chi(Gamma)>0. Gamma is a contractible affine plane curve.
Contractibility of D implies every D_j is unibranch: gluing the A1 normalizations at finitely many points has a graph as homotopy model, and a self-identification contributes a cycle which further gluing cannot kill. Thus each normalization A1->D_j is bijective.

## 2. Smooth Gamma is impossible
If Gamma is smooth, Abhyankar-Moh rectifies it to a line. The induced map from this line to the normalization of its image D_j is a nonconstant polynomial a(t). If a'(t)=0, the derivative of F along the line vanishes, contradicting etaleness. Hence a has degree one. Since D_j is unibranch, F is injective on the actual line, so the injective-on-line theorem makes F invertible.
Unibranchness is essential here: a degree-one normalization map alone can still have a nodal image and does not imply injectivity on that image. This is not a proof of chi(D)<=0 for arbitrary multibranch D.
Thus Gamma is singular. Lin-Zaidenberg provides polynomial source coordinates with Gamma={x^p-y^q=0}, p,q>1 coprime.

## 3. Curves disjoint from the cusp
Claim: every irreducible closed affine curve H disjoint from Gamma has chi(H~)<0 for its smooth affine normalization H~.
Otherwise H~ is A1 or G_m. Its coordinate functions a,b satisfy that f=a^p-b^q is a unit. For A1 this unit is a nonzero constant c. The resulting map to a^p-b^q=c extends to P1 and its smooth projective target completion has genus (p-1)(q-1)/2>=1, forcing the map constant, a contradiction.
For G_m, f=c*t^k. If k=0 the same argument applies. If k!=0, make the finite torus substitution t=z^(pq), and set A=z^(-kq)*a(z^(pq)), B=z^(-kp)*b(z^(pq)). Then A^p-B^q=c, so the positive-genus argument makes A=alpha,B=beta constant. Hence a(z^(pq))=alpha*z^(kq) and b(z^(pq))=beta*z^(kp). Both coordinates tend to zero as z->0 for k>0, or z->infinity for k<0. Since H is closed, it contains the origin, contradiction. Zero alpha or beta causes no exception.
The genus computation is elementary Riemann-Hurwitz: projection to b has degree p, q simple finite branch values and one totally ramified point at infinity, so 2g-2=-2p+(q+1)*(p-1). A nonconstant P1 map to a curve of genus at least one is impossible.

## 4. The whole inverse curve is connected
Every connected reduced affine curve W has chi(W)<=1: each normalized component contributes at most one, and connecting v components costs at least v-1 branch identifications.
Let Z0 be the connected component containing Gamma. Every irreducible component of any other connected component W of Z is disjoint from Gamma and has negative normalized Euler characteristic by Section 3. Finite gluing only lowers Euler characteristic, so chi(W)<0.
But chi(Z0)<=1 and chi(Z)=1. Hence no other W exists. Z is connected with chi(Z)=1. Equality in the connected-curve bound forces every irreducible component of Z to have normalization A1, with a tree as its gluing graph. This uses the whole inverse curve, not a residual slice.

## 5. F restricted to Z is finite etale of degree one
Each irreducible component H of Z maps dominantly to some D_j, since F is quasi-finite. The induced map between their A1 normalizations is a nonconstant polynomial, hence finite. Thus C[H~] is finite over C[D_j]. Its intermediate C[D_j]-submodule C[H] is finite by Noetherianity.
The ring C[Z] embeds into the finite product of these C[H], a finite C[D]-module. Again by Noetherianity C[Z] is finite over C[D]. Hence F|Z is finite, and it is etale by base change.
Every D_j has generic affine inverse points: the budget gives sum_{E_i->D_j}r_i*delta_i<=N-1, hence d_j>=1. Thus the finite map Z->D is surjective. Since D is connected, its etale degree k is constant. Now 1=chi(Z)=k*chi(D)=k, so Z->D is an isomorphism and each d_j=1.

## 6. Contradiction from the sheet budget
Writing ell for the number of D_j, d_j=1 gives sum_{E_i->D_j}r_i*delta_i=N-1 for every j. Summation and the budget give N-1=ell*(N-1)+S. For ell>=2 this contradicts N>1 and S>=0.
If ell=1, S=0 and Z=Gamma is singular and isomorphic to D, so D has a nonimmersed branch. Since N-1>0 some omitted E_i maps onto D. Its polynomial map of A1 normalizations is finite and surjective, so it has a point over the cusp. The zero-slack criterion gives positive slack there, contradicting S=0. This recovers the retained irreducible/unibranch exclusion; it is not claimed as new.
Subject to checking the argument and inherited foundations, the entire contractible case is excluded. Noncontractible nonproper curves and JC2 remain open.

## Replay, controls and limitations

Desk-only proof; no CAS or finite-case experiment supports the all-degree conclusion. The explicit negative scope check is that degree one on normalizations does not imply injectivity onto a multibranch image; the line step uses unibranchness. No individual-component exclusion inside an arbitrary reducible locus, general Euler-sign inequality, or global properness theorem is claimed.
The [evidence README](../box/contractible-nonproper-curve-swarmHQ-20261031T1245Z/README.md) gives checksums and seal-verification commands. Exact producer/reviewer bytes are retained. The review undercounts reading windows by one (79 stated, 80 independently verified); full required coverage and zero repeats were checked, with no change to the mathematical verdict. No independent review of this presentation wrapper is claimed.

## OPENS RAISED

None. The existing noncontractible-case gap remains.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `a8564152a8ea83c377848837381ca4e036db3aef` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8990`.
- Body SHA-256:
  `ed957082a80392e949d5634e648b3d8e2ccd3e79b927a2c056625dea0f756953`.
- Frozen basis: `a8564152a8ea83c377848837381ca4e036db3aef`.
