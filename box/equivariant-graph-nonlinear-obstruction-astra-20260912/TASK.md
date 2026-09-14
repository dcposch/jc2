# Exact graph/subalgebra obstruction: independent manual co-research

ROOT task September12,2026. Astra primary co-researcher. First action
acknowledge TASK SHA and actual UTC, then read THIS TASK fresh WHOLE.
Sole scientific input THIS TASK; no peers, corpus, primary web, science/CAS,
code execution/import/test, AWS/SSH/Git/process/new agent or protected tree.
Documentary date/hash/text reads, apply_patch and existing artifact
transaction only. All preceding assignments are terminal and distinct.

Write only own leased partial/final
xmodel/equivariant-graph-nonlinear-obstruction-astra-20260912.md,
its artifact transaction and own box PINS/custody. Begin/close/finalize/
expected-manifest verify via ops/artifact_finalize.py, basis
0d39df3c9fd69c939a8420c54d03228b9077777d. Skeleton WITHOUT marker;
bounded sections; marker last only at completion. Original reserve01:32,
HARD01:35UTC, no extension. <=1800words. Full readback, postpin and
terminal custody-FIRST handoff with ALL WRITERS IDLE UTC and hashes.
No promotion or follow-on task authorized by this card.

Over C take these THREE EXPLICIT polynomials (no external construction
or counterexample attribution is a proof premise):

 P=(1+xy)^3 z+y^2(1+xy)(4+3xy),
 Q=y+3x(1+xy)^2 z+3xy^2(4+3xy),
 R=2x-3x^2 y-x^3 z.

For every h in C[w], restrict to the entire polynomial graph z=y^2 h(xy).
Let p,q,r be the three restrictions and B=C[p,q,r] inside C[x,y].
QUESTION: does B contain ANY two elements f,g with J_xy(f,g) in C*?
ROOT proposes NO for every h, without an ordinary degree bound on h,f,g.
This is broader than constant linear projections but restricted to these
equivariant graphs; it is NOT all graphs, all embedded planes or JC2.

Independently prove or break the following candidate argument, checking
every grading, coefficient-ring and root-multiplicity implication.

Set w=xy and give x weight -1,y weight1. Then in C[x,y,y^-1],

 p=y^2 a(w), q=y b(w), r=y^-1 c(w),
 a=(1+w)^3 h+(1+w)(4+3w),
 b=1+3w(1+w)^2 h+3w(4+3w),
 c=w*k, k=2-3w-w^2 h.

The weights of p,q,r are2,1,-1. Candidate exact graded pieces:
B_0=C[qr,pr^2]=C[bc,ac^2], B_-1=r B_0, B_-3=r^3 B_0.
These are equalities of subspaces/rings inside C[x,y], not assertions
that p,q,r are algebraically independent. Weight projection of an
arbitrary polynomial expression should be legitimate because all three
generators are homogeneous.

Cauchy--Binet says any J(f,g) lies in
B*J(p,q)+B*J(p,r)+B*J(q,r). Therefore a constant nonzero member forces

 C0=d1(bc,ac^2)*c^3(a' b-2a b')
    -d2(bc,ac^2)*c(a' c+2a c')
    -d3(bc,ac^2)*(bc)',

for some polynomials d1,d2,d3, where primes mean w derivatives.
Indeed this is the weight-zero part, using the three graded-piece formulas.
It is a NECESSARY module condition; do not claim its sufficiency for a pair.

At w=0, c=0,b=1,c'=2, so d3(0,0)=-C0/2. At every root alpha of k,
c(alpha)=0, the SAME d3(0,0) is used, so b(alpha)c'(alpha)=2.
Since k(0)=2, alpha!=0; repeated roots would violate this equality.
The exact identity w*b=4w+6-3(1+w)^2*k then yields

    (4alpha+6) k'(alpha)=2

at every root. If D=deg k>=1, squarefreeness should imply

    (4w+6) k'(w)-2=4D k(w).

But evaluation at0 gives -20=8D, impossible for positive integer D.
Check h=0 and all nonzero/constant h, rather than assuming generic roots.

Controls: h=0 gives k=2-3w, roots c at0 and2/3, and -(bc)' has values
-2 and26. The alternative plane x=0 has restrictions(P,Q,R)=(z+4y^2,y,0)
and J_(y,z)(P,Q)=-1; it lies outside the graph statement and prevents an
all-plane overclaim. A polynomial automorphism of the parameter plane
preserves nonexistence by the chain rule; determine whether that harmless
extension is valid. Arbitrary NON-polynomial target coefficients are not
licensed by the graded B_0 argument.

Deliver a rigorous argument or a precise failing step/counterexample.
QUANTITY: whether the displayed B-Jacobian module intersects C*; strongest
available claim is that it does not. CHEAPEST TEST: manual graded-module
and univariate root argument, planned under15minutes, no numerical run.
No new canonical OPEN. Label all genuine gaps without an echo task.
