# Iterated images: known Keller reduction and two scoped controls

ROOT, September12,2026. MANUAL / INTERNAL-UNREVIEWED strategy discriminator.
No new theorem promotion, Keller pair, properness result or JC2 resolution.
Original publication reserve01:14/HARD01:17UTC; no external lane or worker.
Basis0d39df3c9fd69c939a8420c54d03228b9077777d.

## 1. Primary/history disposition

BGV, arXiv2609.05746v1, Theorem16.8 states eventual image stabilization
for quasi-finite endomorphisms of varieties. The paragraph before it
explicitly cites the earlier affine/open/finite-complement result of
Peretz--Nguyen Van Chau--Campbell--Gutierrez (PNCG). Their 2006 paper,
arXiv math/0411245v2, Corollary3 already applies to every complex plane
Keller map. Its Theorem2 equates JC2 with injectivity of surjective etale
endomorphisms of cofinite plane opens. Thus the Keller specialization is
KNOWN, not a new BGV shortcut. Neither statement alone supplies properness.

Sources: https://arxiv.org/pdf/2609.05746v1 and
https://arxiv.org/pdf/math/0411245v2 . BGV printed21--23 and70--73 read;
the first larger extraction clipped intervening pages, so no70--77 WHOLE
claim. PNCG mathematical text sections1--6 read through web extraction;
not a fresh audit of all imported foundations. The explicit controls below
are direct calculations, not conclusions inferred from an abstract.

## 2. Why a forward orbit does not count missing points

For a self-map e of a set B put M_n=B minus e^n(B), with M_0 empty. Exactly

    M_(n+1)=M_1 union {z in e(B): e^(-1)(z) is contained in M_n}.

It is ALL preimages that must be lost. Mere membership in e(M_n) is not
sufficient. This is also the definition of E_n in BGV Section3.

Over C take the polynomial endomorphism of A2

    e(x,y)=(xy-1, x(xy-1)+y).

For target(u,v), y=v-ux and

    -u*x^2+v*x-(u+1)=0.

This equation is never the zero polynomial: u=v=0 leaves constant -1.
Every fibre is finite. If u!=0 it has a root over C; if u=0,v!=0
the solution is x=1/v,y=v; the origin has no preimage. Hence M_1={o},
o=(0,0). The unique preimage of a=e(o)=(-1,0) is o, so M_2={o,a}.
But e(a)=(-1,1) has TWO preimages a and (0,1). The latter survives.
The exact recurrence therefore gives M_3=M_2 and all subsequent M_n=M_2.

The forward orbit begins o,(-1,0),(-1,1),(-2,3),...; it cannot be used
as a list of omitted points. ROOT's initial exploratory suspicion of
nonstabilization was false and is withdrawn before any theorem claim.
The Jacobian is x+y-x^2*y, so this is NOT a Keller map. Restriction to
A2 minus {o,a} is a surjective, degree2, quasi-finite self-map, not etale.
PNCG section6 already gives a different non-etale stable punctured-plane
example; this control adds no new general counterexample mechanism.

## 3. Etale control from the accepted S/T maps

Use the campaign's exact smooth surfaces and already-reviewed maps:

    T={t^2=1+x^2 Z}, S={U^2=A+A^2 Z},
    q:T->S, (x,t,Z)->(x^2,xt,Z),
    j:S->T, (A,U,Z)->(2U,1+2AZ,Z).

The completed DS-INV-1 proof/FIRST establish that q is finite etale of
degree2 and j identifies S with T minus L_minus, where
L_minus={Z=0,t=-1}. In particular L_minus is NOT the different divisor
D_minus={x=0,t=-1} whose complement is the A2 chart.

Now compose in the other order:

    eta=q composed j:S->S,
    eta(A,U,Z)=(4U^2,2U(1+2AZ),Z).

This is the classical pseudo-plane self-map followed by target rescaling,
not a new construction. It is etale as a composite. Over Z!=0, all two
q-preimages remain in j(S). Over Z=0 a target point has form(u^2,u,0);
its q-preimages are (u,1,0) and (-u,-1,0), exactly one of which is in
j(S). Thus eta is SURJECTIVE, has two-point fibres off Z=0 and one-point
fibres on Z=0. It has geometric degree2 and is nonfinite (a connected
finite etale cover would have constant fibre cardinal). Every iterated
image of eta is S, but eta is not injective.

With q*Omega=omega and j*omega=2Omega as in DS-INV-1, eta*Omega=2Omega.
Thus volume scaling does not repair the general stable-etale argument.
Equivalently E=j q:T->T has E(T)=j(S) and E(j(S))=j(S), so its images
stabilize after the first iterate despite its omitted affine line.

Primary antecedent: Dubouloz--Palka,
https://arxiv.org/html/1701.01425v2 , Examples4.3,5.3; the latter gives
eta in its own coordinates. The current check uses the campaign's exact
rescaling and image formulas rather than identifying numerical degrees:
our eta equals psi composed eta_DP, psi(A,U,Z)=(4A,2U,Z/4).

S is NOT a cofinite open in A2: it has the connected finite etale cover q
of degree2, whereas such plane opens are simply connected. This control
does not refute PNCG Theorem2 or produce a plane counterexample. The two
controls must not be combined as if one example satisfied both sets of
hypotheses: the plane control is not etale, and the etale control is not
a punctured plane. The remaining joint condition is exactly the hard one.

## 4. A legitimate topological consequence, not a closing step

Conditionally let F be an actual Keller map with stable image V=F^N(A2),
choosing N>=1.
Then F(V)=V, so G=F^N restricts to a surjective etale self-map of V.
It factors as V inclusion A2 followed by G:A2->V. Consequently this
restriction is nullhomotopic: compose an ordinary contraction of A2 with
G. If A2 minus V has r>0 points, H^3(V,C)=C^r and the induced map there
is zero. This observation does not prove G is impossible. In particular,
one may not use the injectivity of pullback for a FINITE etale cover or a
proper transfer here: finiteness is the missing premise. If r=0, the
observation is vacuous and says nothing about a surjective noninvertible
Keller map. Thus even a future obstruction for r>0 would need a separate
argument for the surjective case. This conditional attachment is manual,
not promoted and not an assertion that any such F exists.

## 5. Custody, composition, and stop decision

Completed campaign inputs read WHOLE across bounded reads; post-read pins:

- xmodel/danielewski-invariantization-root-20260911.md:
  28fb540a4bb834ad40d1aa0349b8a2458cf7665951484e4896638f18275e3189.
- xmodel/danielewski-invariantization-gate-fable5-20260911.md:
  688ce2cafce3ef85593468f517de850098ee801ee9a82dbcf762dc6b5a6fdae5.
- Retained BGV PDF, box/websweep-20260911T2148Z-astra/bgv-v1.pdf:
  814c3f2572f660a47778663384077d6357e9947f1585c1e16372f6cdbe138425.

The primary web antecedents are selected reads, not new pinned downloaded
packets. No claim that a screenshot was inspected. Scoped canonical and
xmodel searches found the PNCG attribution externally and the exact
pseudo-plane mechanism internally; there is no corpus-wide novelty claim.
The preceding rational-involution revisit also hit the completed
quadratic-deck-exactness-discriminator-root-20260911.md and was stopped.

QUANTITY checked: whether stabilization supplies new injectivity/properness,
and exact missing sets/fibre cardinalities for the two controls. CHEAPEST
TEST used: manual substitutions plus primary/history comparison; no CAS,
scientific execution, model lane, fleet worker or new canonical OPEN.
Own publication transaction is documentary only.

Disposition: KNOWN Keller specialization; FALSE forward-orbit counting;
KNOWN nonproper etale mechanism; NO CLOSING SOURCE IMPLICATION. Do not
launch an echo review, an iterated-image enumeration, or a degree-growing
Chebyshev family search. A new argument must exploit the actual plane or
cofinite-plane source AND etaleness together, without assuming transfer,
properness or a degree bound. This micro-round changes no global ranking
or FULL/BROAD clock. JC2 remains unresolved.

COLLISIONS: no new canonical OPEN; the surface mechanism is an explicit
DS-INV-1/Dubouloz--Palka duplicate, and PNCG owns the Keller reduction.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7754`.
- Body SHA-256:
  `b11cf1ba1100cf96d38a503aac71fba97c83a224adf2b14568db70376181d580`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
