# Global adjoint filtration: source-conditional derivation obstruction

INTERNAL / MANUAL / UNREVIEWED. First actual action 2026-09-12 07:59:59 UTC. TASK and five input pins matched before bodies; all new owned targets absent, root TASK retained. Original publication reserve 08:17 / HARD 08:20 UTC unchanged. No scientific execution, network, code, worker, or shared edit. The accepted source attachment is reused, not re-proved; the two selected old excerpts are history only.

## 1. Exact verdict

SOURCE-CONDITIONAL OBSTRUCTION. Let F=(f,g) be a hypothetical noninvertible complex plane Keller map. In its accepted full-field normalization, the proposed adjoint spaces are finite-dimensional spaces of actual source polynomials, but their union is not invariant under both inverse-Jacobian derivations. More precisely, for every affine ramification prime T of index e>1, at least one of D_f,D_g and, for every sufficiently large m, some h in J_m satisfy

    v_T(h)=1-e,       v_T(Dh)=1-2e,
    Dh is in C[x,y] but in no J_n, for any integer n.

Thus no stability, decreasing-filtration assertion, or finite index-shift bound for these particular spaces can be inferred from the given hypotheses. This is conditional on the hypothetical source, not construction of such a source and not a Jacobian-conjecture verdict. Local pole growth is old; the present attachment is the actual global adjoint section that realizes the pole bound.

## 2. Canonical identification and global attainment

Write A=C[f,g], K=C(x,y), B the integral closure of A in K, Y=Spec B, and Phi:Ybar->P2 its finite normal projective normalization. The accepted full-scope report and gate give the literal inclusion B into R=C[x,y], the open immersion j:A2->Y, and nonempty affine divisorial ramification if F is noninvertible. Every such ramification divisor is missed by j. They also fix the absolute canonical sheaf compatibly with finite duality and open restriction; no arbitrary invertible twist is permitted.

Let L=Phi^*O(1), let t be the pullback of the target infinity section, and set D_infty=div(t). Thus Y=Ybar minus supp(D_infty), t trivializes L on Y, and L is ample. Let omega denote the rank-one reflexive canonical sheaf of the normal projective surface. With s=df wedge dg, define precisely

    J_m = { ((sigma/t^m)|Y)/s : sigma in H0(Ybar,omega tensor L^m) }.

This quotient is taken as rational canonical forms in the common function field. On j(A2), open restriction identifies omega with regular two-forms and s=Jac(F) dx wedge dy is a nowhere-zero generator. Consequently the quotient is a regular function on the entire affine source, hence an actual polynomial in R. Restriction is injective because the source is dense and omega is torsion-free. Projectivity gives finite dimension. Multiplication by t gives J_m contained in J_(m+1), without changing its represented polynomial. These statements do not say the union exhausts R.

Fix a ramification prime T in Y, W=O_(Y,eta_T), and normalized valuation v_T. W is a DVR; omega is free there. The accepted canonical/different calculation gives v_T(s)=e-1 relative to a local generator. Since t is a unit at T, every h in every J_n obeys

    v_T(h) >= 1-e.                                      (1)

To attain the bound globally, use the standard ample-twist global-generation theorem for coherent sheaves: omega tensor L^m is globally generated for all sufficiently large m. This theorem does not require omega invertible or rational singularities. At eta_T, its stalk is a free rank-one W-module. If every global section had coefficient in the maximal ideal of W, their stalks could not generate. Therefore some actual global section sigma has unit coefficient. Its polynomial h above has exactly v_T(h)=1-e. This chooses a genuine global section first; it does not assume a formal local section descends. No effective value of m or numerical coefficient is asserted.

## 3. Tame local derivative and the noncancellation check

Let q in A define the irreducible affine branch divisor below T. At least one of q_f,q_g is nonzero modulo q: otherwise a nonconstant irreducible polynomial in characteristic zero would divide each nonzero partial derivative of strictly smaller degree. Choose the corresponding base derivation partial_f or partial_g, and denote its unique extension to K by D. Then Dq is a unit in W. On the source, explicitly,

    D_f=(g_y partial_x-g_x partial_y)/Jac(F),
    D_g=(-f_y partial_x+f_x partial_y)/Jac(F).

Both preserve R because the Jacobian is a nonzero constant. The chosen base derivation preserves the local ring A_(q), although it does not preserve its maximal ideal.

Here is the unit bound, including residue-field issues. Pass to the strict henselization of A_(q) and choose a branch of the normalized base change above T. Characteristic zero makes the residue extension separable and the ramification tame. The standard tame-DVR normal form, after this unramified base change, is W'=A_(q)^sh[pi] with pi^e=q. The base derivation extends through etale algebras and preserves A_(q)^sh; it need not fix a coefficient field or residue elements. Its extension to the branch satisfies

    Dpi=(Dq/e) pi^(1-e),       D(W') contained in pi^(1-e) W'.       (2)

The second inclusion follows by differentiating the finite basis 1,pi,...,pi^(e-1): coefficient derivatives remain in the base ring. This is the tame inverse-different estimate, not an assumption that derivatives of units are regular. The local unramified extension preserves normalized valuations of original elements; branchwise calculation therefore proves the same valuation conclusion in K.

Write the already chosen global h as pi^k u, k=1-e<0 and u a unit of W'. Then

    Dh=(k/e)u(Dq)pi^(k-e) + pi^k D(u).

The first term has valuation k-e and nonzero coefficient: k and e are nonzero in characteristic zero, and u,Dq are units. By (2), the second has valuation at least k+1-e, strictly larger. Thus tangential, coefficient-field, and absorbed-unit terms cannot cancel the leading term. Hence v_T(Dh)=1-2e, strictly below (1), proving the claimed failure for EVERY J_n. No analytic completion, chosen real root, or constant-residue-field assumption is used.

## 4. What fails, and the minimal additional hypothesis

The failure is stronger than failure of one proposed finite-dimensional stage: D does not preserve the union of the J_n. In fact that union is H0(Y,omega_Y)/s. To see the converse inclusion, a canonical section on Y is a rational canonical form on Ybar. A sufficiently high power of t clears its finitely many divisorial poles on D_infty; it is then regular at every height-one point and extends globally by reflexivity on the normal surface. The forward inclusion is immediate. The global h and polynomial Dh above show that this canonical-lattice subspace is strictly smaller than R under the hypothetical noninvertible-source assumptions. Finite dimensionality of its individual stages cannot establish local finiteness on R.

There is also no compensating Lie-derivative term: for either inverse-Jacobian derivation, Lie_D(s)=0 since Df,Dg are constants. Thus Lie_D(hs)=(Dh)s as rational forms. Using this natural canonical-form action gives the same obstruction.

For completeness, iteration of the same strict leading-term argument gives

    v_T(D^j h)=1-(j+1)e,       j>=0.

Every exponent encountered is negative, so the integer leading factor never vanishes. The iterates are polynomials but linearly independent over C: in a nontrivial finite relation the largest index has uniquely smallest valuation. This is the old pole-growth non-local-finiteness mechanism attached to an actual global adjoint section, not a new classification of derivations.

The minimal missing structural condition for the proposed simultaneous stability is absence of affine ramification. Indeed, invariance even of the union under both D_f,D_g would contradict the construction at any T with e>1. In the accepted source setting, absence of affine ramification already gives trivial finite normalization and automorphy by purity and the triviality of connected finite etale covers of complex A2. Therefore asserting this filtration's invariance would insert, rather than prove, a decisive missing condition. Allowing other pole lattices or other derivation methods is a different question; none is proposed or authorized here.

## 5. Controls, imports, and exact limit

- Unramified control: for the identity map, Ybar=P2 and L=O(1). J_m consists of polynomials of total degree at most m-3 for m>=3, and is zero for smaller m. Ordinary partial derivatives decrease degree. The negative exponent k=1-e and its nonzero leading factor are absent when e=1.
- Tangential control: for a branch q=f, D_g(q)=0 while D_f(q)=1. The argument selects D_f and does not falsely assert that each derivation is transverse to every branch. At least one always is.
- Small-twist control: an arbitrary small J_m may be zero or may fail to attain the local bound. Global generation, not a guessed local-to-global extension, is why the conclusion holds for sufficiently large m.
- Singular/vertical control: omega need only be reflexive. T is an AFFINE height-one prime, so twisting the infinity divisor cannot relax its bound. Codimension-two singularities and components at infinity supply no cancellation of this single DVR obstruction.
- Source control: the tame local model alone is not a polynomial Keller pair. Actual polynomiality of h and every Dh uses the accepted open source immersion and the constant-Jacobian formulas. The result does not assert that a hypothetical noninvertible map exists.

Named standard imports, not newly primary-read or represented as fully re-proved: finite pullback preserves ampleness; ample twists of a coherent sheaf on a projective scheme are eventually globally generated; canonical reflexivity and extension from height one on normal surfaces; unique extension of derivations across separable algebraic field extensions and lifting through etale algebras; and the strict-henselian tame-DVR normal form. The finite-basis differentiation establishing (2), valuation comparison, and actual-global-section attainment are explicit above. The accepted source normalization, canonical open restriction, ramification order e-1, and nonempty missed ramification are consumed at the charged gate's scope. Neither H1 vanishing nor a genus classification is needed.

Verdict: the prescribed global-attainment discriminator is settled at MANUAL/UNREVIEWED producer tier. There is no remaining mathematical GAP in this obstruction conditional on the named standard imports and accepted source attachment. The missing extra hypothesis in the proposed shortcut is the invariance/no-affine-ramification condition, not a numerical cutoff. Cheapest next discriminator, only if ROOT separately selects it: one focused different-model review of the global-generation-to-unit-stalk step and tame unit-derivative bound; 10 minutes is an UNMEASURED reading allocation, not an execution forecast. No D-module closure, trace-family successor, source exclusion, or downstream authority follows.

## 6. Publication scope

Exactly TASK plus five local inputs were hash-bound before charged body reads. TASK, the accepted full-scope producer, and its gate were read FRESH_WHOLE this turn. COORDINATION was REUSED_WHOLE after its matching current pin (all 806 lines previously read today at 05:51–05:53). The old conductor proposal was read ONLY lines 118–183 and the old valuation prereview ONLY lines 62–95. Their labels, proposed experiments, and cited inputs are history rather than adopted premises; no linked bodies were followed. PINS.json and READ-SCOPE.md preserve these limits.

Own whole readback, unchanged six input postpins, owned-output collision and quantity/limit checks precede the final marker. The ordinary transaction uses basis 0d39df3c9fd69c939a8420c54d03228b9077777d; close, finalize, and expected verification precede terminal custody and ALL WRITERS IDLE. No old file, root TASK, shared ledger, or protected source is edited.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12129`.
- Body SHA-256:
  `1786e220c6a7138eb2d1b8d58f356913ae20ed37f60bb5260133bb881b6fe780`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
