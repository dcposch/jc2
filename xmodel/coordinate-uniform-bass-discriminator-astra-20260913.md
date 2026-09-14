# Coordinate-uniform Bass: one global source discriminator

MANUAL co-research, not FIRST or promotion. Actual first action 2026-09-13 04:37:20.440750390 UTC. Original publication reserve04:56/HARD04:59 unchanged. Own targets absent; all named input and instrument hashes matched before reads.

## Selected missing implication

For the actual whole-plane Keller inclusion A=C[p,q] in R=C[x,y], N=R/A, determine whether coordinate-uniform Euler torsion-freeness forces an actual source section with an Euler annihilator or a tested first-order selection. Finite-monodromy constituents and polynomial source sections must remain distinct.

Verdict: NO_PROGRESS toward source selection from the ONE finite-monodromy horizontal-transfer test. Its first proposed calculation fails exactly: the Reynolds transfer of every horizontal vector in the split trace-zero source connection is ZERO. Polynomial coordinate changes do not alter that calculation. This is not an abstract control family or proof that coordinate-uniform Bass is insufficient by every conceivable mechanism.

## 1. Exact normalization and actual source space

Let F=C(p,q), L=C(x,y), d=[L:F]. The target derivations D_p,D_q extend to the source by the inverse Jacobian. The charged actual-source report proves R intersect F=A, using flatness, polynomial units and prime valuations. Hence

    N=R/A embeds into L/F,
    F tensor_A N = L/F.

The second equality uses the generic fibre of the dominant quasi-finite map: R tensor_A F is the finite field L. No finiteness over A or properness of the original Keller map is assumed. If d=1 the intersection already gives R=A, so a nonzero N requires d>1.

For a polynomial target coordinate system u,v and a chosen source point s, center at a=u(p(s),q(s)), b=v(p(s),q(s)). Translate the source origin to s. Bass Theorem1.4 then applies to

    C[e_u,e_v],  e_u=(u-a)D_u,  e_v=(v-b)D_v,

and makes N torsion-free over that Euler polynomial ring. This is an import of the theorem, not its proof. The permitted centers lie in the actual image; neither surjectivity nor normalization at every target point is used. The PDF's notation has the smaller target polynomial ring A and larger source ring B; its quotient B/A is our N. Theorem1.4 is on printed42, with normalization on printed40 and the homogeneous-prefix discussion on printed41.

## 2. The proposed finite-monodromy construction

The exact proposed shortcut is: split the finite algebraic source connection, take a nonzero horizontal vector, transfer it to the actual source, and use any centered Euler frame to obtain torsion. A nonzero horizontal vector would indeed be killed by both e_u and e_v, so it would contradict Bass if it became a nonzero element of N. The problem is the transfer, not a shortage of coordinate frames.

Let K/F be a finite Galois closure of L/F and G=Gal(K/F). Derivations extend uniquely in characteristic zero and commute with G. Trace commutes with these derivations, so the degree-normalized trace gives a differential splitting

    L=F direct-sum L_0,   L_0=ker Tr_(L/F),
    L/F isomorphic to L_0.

Over K, separability gives the actual connection isomorphism

    K tensor_F L -> product_(sigma:L->K) K,
    k tensor h -> (k*sigma(h))_sigma.

Differentiation on the right is componentwise; it agrees by the Leibniz rule and uniqueness of the extension. The trace-zero part consists of tuples with sum zero. The common constants of K under D_p,D_q are C: their vanishing means the absolute differential over C is zero, hence an element is algebraic over C, which is algebraically closed. Thus the horizontal vectors in K tensor_F L_0 are exactly

    H={ (c_sigma) in C^d : sum c_sigma=0 }.

This has dimension d-1. These are genuine horizontal vectors of the split generic connection, not yet polynomial source sections. No global regular-holonomic semisimplicity or embedding of an arbitrary constituent has been assumed.

## 3. The first calculation: the transfer is zero

G acts transitively on the d embeddings of L into K. On H its semilinear coefficient action is trivial because every entry is in C, leaving the permutation action. A fixed tuple therefore has all entries equal; the sum-zero condition makes it zero. Equivalently, the Reynolds projector satisfies the literal formula

    (1/|G|) sum_(g in G) g(c_sigma)
       = ((sum c_sigma)/d,...,(sum c_sigma)/d)=0.      (1)

In particular each proposed basic horizontal difference e_i-e_j transfers to zero, not to an Euler-torsion source class. This calculation holds for every finite transitive source field extension, including the actual one; no invented relaxed-source example is needed.

The failure cannot be repaired merely by clearing denominators from F. If h in F*, then transfer(hv)=h*transfer(v)=0. Choosing instead coefficients h in K can produce a nonzero transfer, but loses horizontality:

    D_u transfer(hv)=transfer((D_u h)v),
    D_v transfer(hv)=transfer((D_v h)v).

The right sides are not known to vanish or span a finite-dimensional C-space. An algebraic equation for h is nonlinear; it does not by itself give a polynomial in the two commuting Euler operators annihilating the transferred vector. Further, a generic rational class in L/F need not be represented by R, so membership in N still requires a separate polynomial-section check.

The obstruction is therefore stronger than an unidentified constituent-lifting debt: for the horizontal vectors selected by this test, invariant descent is proved zero already at the generic point. Polynomial words in horizontal constant tuples remain constant tuples; their averages are diagonal constants and vanish in L/F. Products or norms therefore do not rescue the proposed horizontal transfer. This observation does not define multiplication on N.

## 4. Why all coordinates and acyclicity do not change (1)

Polynomial target coordinate changes leave the fields F,L,K and their transitive embedding set unchanged. The two new derivations form an invertible F-linear recombination of D_p,D_q. Their simultaneous constants, H and its G-action are consequently the SAME. Recentring changes e_u,e_v but still kills every horizontal vector before transfer. Thus (1) holds in every permitted frame simultaneously; a different normalization cannot make its zero output nonzero.

This does not prove that an Euler-torsion vector must be horizontal. It only settles the particular construction selected above. Coordinate-uniform Bass might rule out other actual source phenomena, but no such implication has been obtained here. Nor is a rational Euler-localized line the same object as a one-dimensional constant subspace of this algebraic field connection.

Actual de Rham acyclicity is consistent with this failure. The Keller Jacobian identifies the source de Rham complex with R tensor Lambda(dp,dq), and its target subcomplex with A tensor Lambda(dp,dq). Both polynomial planes have only the common constant H^0; the quotient complex for N is therefore acyclic. In particular H^0(N)=0, exactly as the generic trace calculation predicts. This global acyclicity does not turn a noninvariant horizontal vector after field extension into an invariant one. No acyclicity of a localized module N(*D), equality N=N(*D), or property of a missing target origin is assumed.

## 5. Scope and stopping decision

The old translated Kummer control is not re-proved or extended. Its fixed-frame success does not weaken the genuinely stronger source hypothesis. Instead the present calculation tests a different proposed bridge: finite algebraic monodromy supplies split horizontals, but transitive field descent annihilates their entire trace-zero space. This is the first exact failed operation and is independent of any branch-divisor classification.

The missing all-degree selection remains: construct an actual polynomial source class with a nonzero Euler annihilator or obtain the separately tested first-order form. No such class, delta-line or normalization was selected. Requiring a nonzero invariant in H is not a useful extra hypothesis: (1) proves it impossible for the connected source field extension. A new test would need genuinely nonhorizontal source information; none is proposed as an automatic successor.

Cheapest discriminator for THIS mechanism was the finite transitive-permutation average (1), now completed manually. A focused independent audit is estimated at5 minutes UNMEASURED, not a worker request. NO_PROGRESS is the mathematical outcome, with a complete bounded failed test rather than a new equivalent criterion, countermodel family, source exclusion or JC2 claim. No canonical OPEN or follow-on authority is created.

## Read scope and publication

Three reports freshly WHOLE after matching pins. The named Bass PDF was read through pdftotext to stdout: PDF1 cover and PDF2-5 (printed39-42) for the theorem statement and normalization; incidental neighboring statements were visible, but the full proof is imported and no later page or linked reference was read. Current COORDINATION lines502-525 were freshly read; the previous full personal read at hash33cfa610... is historical protocol reuse, not a claim of freshly reading the current full document. The new current hash517fca6f... is retained before and after. ROOT's separate geometric work is not a premise.

All mathematics was manual. Only inert text/hash/date, documentary PDF extraction, apply_patch and the unchanged administrative finalizer were used. No scientific interpreter/import/AST/syntax/test/CAS/helper, network, worker, agent, protected tree/mirror, linked source, live peer or shared edit. Own WHOLE, postpins, collision and quantity checks precede marker LAST, expected-manifest verification and final custody.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9765`.
- Body SHA-256:
  `12625c8c2eb292c4d7c7ed8bf1519d45c1a86ce08283cc7011f25853523c588e`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
