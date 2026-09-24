# Collision-component duals and a singular-fiber scope correction

Producer: swarmHQ ROOT/Codex, integrating Fable5.1's proposed auxiliary
identity and independent Astra hostile cross; hosted identities are not
independently attested.
Date: 2026-09-24 UTC.
Basis: faecac79115d13e82518574bb92d0d30a7057574.
Evidence: MANUAL, with the classical imports explicitly retained below.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED. No accepted-claim upgrade.
Novelty: UNKNOWN. JC2 remains unresolved.

## Statement and scope

Let F=(F1,F2):C^2->C^2 be a polynomial Keller map, let R=C[x,y], and
let A=C[F1,F2] subset R. The auxiliary statement reviewed here is

    End_A(R) = R,

where End denotes A-MODULE endomorphisms and the right side acts by
multiplication. The argument survives at the stated classical-import scope.
It does not imply A=R, produce a nonzero R->A functional, or show that the
off-diagonal collision scheme is empty.

A separate proposed construction filter asserted that singular points of
the image of G=(F1,F2,y) could occur only above nonreduced G-fibers. Its
displayed argument does not establish this. Actual Keller G-fibers are
reduced; a manual non-Keller control below shows exactly why image singularity
and differential immersion do not imply fiber nonreducedness. This is not
a counterexample to JC2 or to a statement restricted to all actual Keller maps.

## Dependencies and comparison

The [generic-dual finiteness lemma](generic-dual-integration-swarmHQ-root-20260923T163500Z.md)
is the accepted input: for domains D subset B, D Noetherian and finite
fraction-field degree, Hom_D(B,D)!=0 iff B is module-finite over D.
The [target-linear functional criterion](nonzero-dual-first-integration-swarmHQ-root-20260923T155000Z.md)
and [locality corrections](dual-locality-scope-review-swarmHQ-root-20260923T233500Z.md)
retain their scopes. In particular a local inverse-sheet evaluation is not
a global polynomial-valued functional.

The additional named classical imports are: standard etale/component facts;
triviality of connected finite etale covers of the complex affine plane;
and the fixed-point consequence of linearizability of finite-order
polynomial automorphisms of C^2. The present desk review does not supply a
fresh primary-source audit of those theorems. The auxiliary proof does NOT
require the Hamiltonian-isotropy criterion or the birational-Keller theorem.

Bounded searches in frozen public evidence and the team's dated history did
not establish priority or a previous proof of this exact identity. Earlier
rational-deck extension obstructions are adjacent, but a matching selection
heading is not evidence that this composition was proved there. No claim of
originality, exhaustive novelty search or new global closing mechanism follows.

## 1. Componentwise adjunction proves the auxiliary identity

Put S=Spec R and T=Spec A. The fiber product W=S times_T S is etale over S,
hence regular. Its diagonal is open by etaleness and closed by separatedness.
Regularity makes its finitely many irreducible components disjoint and
open-and-closed. Thus

    R tensor_A R = R x product_i B_i,

where B_i are the coordinate DOMAIN rings of nonempty off-diagonal components.
Each Spec B_i->S is etale, dominant and generically finite: its nonempty open
image lies in the irreducible source S. This domain assertion concerns each
component, not the whole disconnected tensor product.

Adjunction gives

    End_A(R) = Hom_R(R tensor_A R,R)
             = R directsum (directsum_i Hom_R(B_i,R)).

The first identification takes phi to the map r tensor s -> r*phi(s), using
the first factor for the R-action. The generic-dual lemma gives

    Hom_R(B_i,R)!=0 iff B_i is finite over R.

Suppose a component is finite. It is a connected finite etale cover of S,
so its first projection is an isomorphism. Its second projection defines a
polynomial map sigma with F sigma=F whose graph is disjoint from the diagonal.
Write K=Frac A and L=Frac R. Dominance makes sigma a K-embedding L->L.
As L/K is finite, it is a field automorphism. The finite group Aut_K(L)
then gives sigma^m=id for some m; equality on the polynomial ring shows that
sigma is a finite-order polynomial automorphism, with polynomial inverse.
The named fixed-point theorem contradicts disjointness of its graph from
the diagonal. Consequently no off-component is finite and every off-component
dual vanishes.

The remaining diagonal summand consists precisely of multiplication operators.
Their composition is multiplication, so the identity is canonical as a ring
identity, not merely an abstract module isomorphism.

This leaves open the existence of nonempty NONFINITE collision components.
Proving their projection proper remains a legitimate closing target: the
affine proper projection would be finite and the argument would force
emptiness. Its equivalence to a desired endpoint is not a reason to ban a
genuinely new proof of it. No such properness proof is supplied here.

Scope control: for the non-Keller map F=(x^2,y), R is free of rank2 over A,
so End_A(R)=M_2(A). The literal off-diagonal is the graph of (-x,y) restricted
to x!=0; its closure meets the diagonal. The Keller clopen product splitting
does not hold at the ramification locus. This example is only a scope contrast.

## 2. Image singularities are not nonreduced fibers

Normalize JF=1 and make F1 monic in x by the stated generic linear source
change. Let p(U,V,T) be the primitive irreducible relation
p(F1,F2,y)=0. The ring R is finite over A[y], since x satisfies the monic
F1 equation. Differentiating gives, on the parametrized image,

    (p_U,p_V,p_T) = p_T*(F2_x,-F1_x,1).

Thus V(p) is singular at G(z) precisely when p_T(G(z))=0. If JF=c instead,
the first two entries on the right are divided by c. These identities are
valid; they do not imply the proposed nonreduced-fiber conclusion.

Indeed, for an actual Keller map the F-fiber algebra

    R/(F1-u,F2-v)

is a finite product of copies of C, because F is etale and quasi-finite.
The G-fiber algebra is its quotient by y-t, and is again reduced. Multiple
distinct inverse points are not nilpotents. The proposed filter would
therefore require absence of singular image points, an additional global
assertion not proved by the gradient identity.

Exact manual countercheck to the local inference:

    f=x^2-1, h=x(x^2-1)+y, G=(f,h,y),
    p(U,V,T)=(V-T)^2-U^2(U+1).

This G is finite onto the irreducible hypersurface V(p), since x^2=U+1.
Its x-derivative (2x,3x^2-1,0) never vanishes and is independent of its
y-derivative (0,1,1), so G has differential rank2 everywhere. At (0,t,t)
all three partials of p vanish, but the fiber ideal is

    (x^2-1,y-t),

giving two REDUCED points x=1 and x=-1. The first two outputs have Jacobian
2x and are etale at those points, but this is NOT a Keller pair on the whole
plane. It disproves the inference from finiteness/immersion/local etaleness
to nonreduced fibers, not a universal statement restricted to actual Keller
maps. Do not discard a candidate using that unsupported filter.

The separate leading-coefficient condition survives with its own argument.
Under hypothetical noninvertibility, the T-leading coefficient a(U,V) of
primitive p cannot be constant: otherwise y, then x, is integral over A.
Moreover V(a) is contained in the nonproper locus at the standard finiteness-
locus scope. If F were finite near a generic prime dividing a, y would be
integral over that normal DVR. Its monic minimal polynomial would have
integral coefficients, contradicting primitivity of p and the positive
valuation of its leading coefficient. Closedness of the nonproper locus
then includes the whole divisor. This is not a polynomial-pair construction.

## 3. Dual-filtration clarification

Let M_d be the A-span of source monomials of total degree at most d. Its
generic rank can initially increase. Choose d_* so that K M_(d_*)=L.
Only from that point are all M_d^* naturally decreasing submodules of the
SAME Hom_K(L,K), with intersection Hom_A(R,A). Eventual stabilization would
give a nonzero global dual and hence finiteness. Conversely, finiteness puts
an A-generating set of R in some M_d, so M_d=R eventually. The stabilization
target is a reformulation, not an established positive premise. Noetherianity
does not itself stabilize descending chains. The freeness assertion in the
raw proposal needs additional reflexive/projective-freeness imports and is
unnecessary for this conclusion.

A fixed trace-dual basis supplies the omitted valuation justification.
Choose monomial K-basis elements b_i of degrees<=d_* and their trace-dual
basis beta_i in L. Let v be a valuation centered on the finite normalization
over A, so v(A)>=0, and suppose a source coordinate z has v(z)<0. If
Tr(c*M_d) subset A and k=d-d_*>=0, then

    c*z^k = sum_i Tr(c*z^k*b_i)*beta_i,
    v(c) >= min_i v(beta_i) - k*v(z).

This estimate handles trace cancellation using one FIXED basis. It explains
shrinking duals at an omitted finite-normalization divisor; it is not a
Jacobian-based upper bound or a proof that the boundary is absent. The
manual clarification remains UNPROMOTED and authorizes no descendant.

## Review record, replay and limitations

Fable proposed the auxiliary identity and filter. ROOT and a separate Astra
cross independently checked the terminal proposal before this integration;
both obtained the finite-field order simplification and the same nodal
countercheck. This is different-model hostile checking of Fable, not a
different-model FIRST for every additional ROOT/Astra clarification. No
accepted ledger claim is promoted by this report. Ordinary, local, generic,
integral and whole-source statements retain their distinct scopes.

Desk-only; no CAS, cloud computation, randomness or primes. The displayed
polynomials, derivatives and fiber ideal are complete replay data. Frozen
review evidence, retained by the team, has these full-file hashes:

    Fable initial 8dcda04a11db851fb096db02d7987a812c8d79c4b1ddc56db0476d0d7a369c14
    ROOT cross a1f1a24ffe4dfca724ccf80c1c8bbf77610fedccd2f56912aecb9a6002f7255a
    Astra cross 504cfc57b6f653d086991b84a1db1038cdb81258ec4cfd3873bd735e21e357cb

The raw external report's legacy receipt custody is distinct from a valid
canonical seal: its missing Body-bytes declaration was not repaired. This
new report follows the canonical publication workflow and contains the
complete integrated arguments; hashes are integrity evidence, not a proof.

No new global closing test survives. Polynomial construction, properness,
analytic and other genuinely changed arguments remain eligible. Neither
agreement on this conclusion nor a lexical search proves exhaustion.

## OPENS RAISED

None. No new experiment or automatic successor is requested.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `faecac79115d13e82518574bb92d0d30a7057574` (Git blobs only).

The scanner used completed immutable pre-collision author snapshot
afa8a8cca1a5e66aa77eedd1740e7dde7e132f0bb9a7d8122243f10e1fccc8be.
EMPTY here means no raised OPEN was available to match, not novelty or
mathematical correctness. No stopped mechanism/test pair is renewed.

Whole-author readback and unchanged evidence pins verified2026-09-24
11:24:12 UTC. Measured author completion:2026-09-24 11:24:12 UTC.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11389`.
- Body SHA-256:
  `09615d7275fbc8bc50acfdac3b78ca55dec733f7b786a1544fa8bcab4889a35c`.
- Frozen basis: `faecac79115d13e82518574bb92d0d30a7057574`.
