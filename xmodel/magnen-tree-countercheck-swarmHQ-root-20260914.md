# Magnen's tree factorization: a degree-two plane countercheck

Producer: swarmHQ ROOT, 2026-09-14. Evidence: MANUAL exact algebra.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED; independent source check pending.
This rejects a displayed proof step, not the Jacobian Conjecture.

## Source and exact question

Jacques Magnen, *The Jacobian conjecture*, arXiv:2311.14723v1,
https://arxiv.org/pdf/2311.14723v1 (2023). Frozen PDF:
`box/magnen-tree-screen-swarmHQ-20260914/magnen-v1.pdf`, SHA256
`963c7ac5130670869724402b2c12dc5b86df421d39dfbf2ce82a3b785f01ed83`.
ROOT read the nine-page PDF's extracted text, including the definitions,
factorizations, final bound and appendix. A screenshot request for page4
failed; the conclusions below use the extracted equations and definitions.

The paper defines the inverse by F=y+V(F). Its Definition3 orders a vertex's
incoming edge before its outgoing edges; root and leaf edges belong to the
tree. Definition6 retains only trees without two aligned index-one edges;
write this restricted sum G=F(|1). Equation(3.19) claims that each F_i is
G_i times the exponential of the trace-log terms containing index one.
Equation(3.1) instead prints an unrestricted trace-log factor. Neither
version survives the following test. The test does not depend on the
appendix, on a degree-bound theorem, or on whether higher-dimensional JC
is true.

## Actual plane Keller control

Work over Q, and hence over C, with source coordinates x=(x1,x2), s=x1+x2:

    V(x)=(s^2,-s^2),       K(x)=x-V(x).
    M=V'(x)=2s [[1,1],[-1,-1]].

Both components are symmetric quadratic polynomials, V(0)=V'(0)=0,
M^2=0, tr(M)=det(M)=0 and det(I-M)=1. Thus K satisfies even the
homogeneous/quadratic and symmetry readings of the paper's hypotheses.
Because V1+V2=0, K preserves x1+x2, and direct substitution in both
orders gives the polynomial inverse

    F(y)=(y1+(y1+y2)^2, y2-(y1+y2)^2).

This is an actual ordinary polynomial plane automorphism, not a rational
map, formal-only candidate, or putative counterexample to JC2.

## Coefficients of the restricted tree sum

Let O(3) mean terms in (y1,y2)^3 in Q[[y1,y2]]. Since every vertex is
quadratic, terms of total degree2 have exactly one vertex. There are no
unseen multivertex contributions at this degree.

For component2 the root edge has index2. The two outgoing leaf edges
are siblings, hence are not aligned with one another. Thus all its
quadratic monomials survive the index-one restriction:

    G2=y2-(y1+y2)^2+O(3).

For component1 the root has index1. Any index1 leaf is aligned with it
and forbidden. Only the two-index2-leaf monomial survives:

    G1=y1+y2^2+O(3).

In both components the linear terms survive. These facts follow from
the paper's vertex/edge definitions, not a new graphical convention.

## Failure of the restricted trace factor, equation(3.19)

Put h=y1+y2. In -tr log(I-M(G)), the only degree-one trace term whose
index cycle contains1 is M11(G)=2h+O(2). Terms with at least two
matrix factors have degree at least2, so they cannot change this linear
coefficient. The factor printed in(3.19) therefore is

    E1(G)=1+2h+O(2).

Its alleged component2 equality gives

    G2 E1(G)=y2-h^2+2y2*h+O(3),
    F2       =y2-h^2.

Their difference has nonzero quadratic part 2y2*(y1+y2). For example,
at y1=0 the predicted coefficient of y2^2 is +1, whereas the actual
coefficient is -1. Thus(3.19) is false on this genuine Keller map.
This component2 check does not rely on the component1 root restriction.

As a consistency check, the restricted trace sum can also be identified
by subtracting the all-index2 cycles from the full trace-log. Since
M(z)^2=0 and tr M(z)=0 for every z, the full trace-log is zero; its
all-index2 part is -log(1+2(z1+z2)). Their difference exponentiates to
1+2(z1+z2), agreeing with the first-order calculation above.

## Failure of the unrestricted version and final restriction

If(3.1)'s unqualified trace-log is used instead, its exponential is
identically1, by det(I-M(z))=1 at every formal z. Then F1=G1 is false
already at degree2, with missing terms y1^2+2y1*y2.

The final restricted object F(|<=2) in Definition7 still forbids two
aligned index1 edges: there is no smaller index that could separate them.
Hence its component1 quadratic part also is y2^2. The determinant-one
conclusion F=F(|<=2) in(4.4) has the same contradiction. Reinstating
the restricted qualifier in(3.1) therefore does not repair the proof,
and the failure is present in dimension two itself.

## Positive control and disposition

For the triangular map V=(x2^2,0), the inverse is (y1+y2^2,y2).
All its nonzero trees survive the restrictions and every trace cycle
vanishes. Both displayed factorizations pass on this control. The
failed example is its linearly conjugated shear, where the discarded
coordinate-index terms can no longer be dropped. The test is not a
failure of inverse existence or of the Jacobian condition.

The decisive missing operation is a valid resummation preserving rooted
tree weights, rather than multiplication of every root component by one
scalar determinant factor. No repair, all-degree cancellation theorem,
or new counterexample construction has been obtained. Do not import
Theorem1.2 from this proof. This is a bounded negative source screen,
not a proposal to classify tree families or rerun accepted bounds.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

The existing lexical checker returned exit0 with this block. Its
no-raised-OPEN result is not a novelty certificate or mathematical check.

## Review boundary and resources

Targeted case-insensitive searches for Magnen/2311.14723/Abdesselam in
APPROACHES, AUDIT, PROGRESS, notes, ladder/REDUCTION and Markdown reports
under xmodel/history/refs (excluding zheglov) returned no relevant hit.
This is not an exhaustive priority search or a completed BROAD sweep.
No canonical OPEN is raised. ROOT's independent calculation was not
sent to the parallel Astra source checker before that author's seal.
Same-model agreement will not be called different-model FIRST.

Only manual algebra, primary retrieval, text/hash/status operations,
the existing lexical collision checker and administrative finalizer were
used. No scientific code,
CAS, AWS worker, paid external lane, repository-wide test or protected
nested-repository access. A source-check report may change the scope
before any promotion; AUDIT is unchanged.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6484`.
- Body SHA-256:
  `258b309bb39fe97b2436fcf0cd0d40ef606fd749f2596e380ae4726f9774dd16`.
- Frozen basis: `9131f71b35f524751a1182f4f4f7cc7cca6afda9`.
