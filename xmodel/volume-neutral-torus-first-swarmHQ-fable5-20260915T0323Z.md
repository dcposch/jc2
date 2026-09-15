# FIRST: volume-neutral torus quotient obstruction

Reviewer: swarmHQ Fable5.1 (claude-fable-5-1), different-model hostile FIRST of
ROOT/Astra. Lane tag volume-neutral-torus-first-swarmHQ-fable5-20260915T0323Z.
Launch clock 03:23 UTC; target 03:37; hard 03:41.

Claim reviewed: exactly VOLUME-NEUTRAL-TORUS-QUOTIENT-1 as printed in the
producer; no enlarged class, no JC2 consequence, no successor.

## Charged inputs (immutable, hashed before and after reading)

| basename | sha256 |
|---|---|
| volume-neutral-torus-quotient-swarmHQ-root-20260915.md | 181d7ae11675d27a61da977f143abaf5797415d6c64923e11be336281ce6df80 |
| COORDINATION.md | 4ce5b29af5a70e096a04b942cb978b1df425f9f0648decb720ec1f089ff37ac4 |
| README.md (team/swarmHQ) | 50cf45483cddf637e717ddfa2d136be4df074d13d360b851c1fb62a9e73edb0a |
| FALLACY-v2.md | e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5 |

All four read whole from /tmp/jc2-lane.N01dx8/inputs (producer 10439 B,
COORDINATION 694 lines in two reads, README, FALLACY). Post-read hashes are
in the custody section. No other file, ledger, log, network, package, agent
or computation was used. Native Astra co-checking was ignored as evidence.

## Verdict summary

Overall: CONFIRMED at exactly the printed scope. Every step was re-derived
independently below; no missing hypothesis was found. Two remarks (R1, R2)
are observations on the proof, not gaps, and raise no OPEN.

| # | item | verdict |
|---|---|---|
| 1 | normalization G=M^-1(F-b), fixed translation, det DG=1 | CONFIRMED |
| 2 | vertex smoothness, indecomposables = basis of m/m^2 | CONFIRMED |
| 3 | S-S=K (needs 1 in S, i.e. trivial determinant) | CONFIRMED |
| 4 | 1=a*alpha+b*beta with a=b=1 | CONFIRMED |
| 5 | zero/repeated weights | CONFIRMED (zero only at a singleton; none repeated for n>=3) |
| 6 | semi-invariant pieces x_i*P_i(u,v) / invariant at singleton | CONFIRMED |
| 7 | contraction identity, sign only, no boundary factor | CONFIRMED |
| 8 | descent det DH=1 in C[u,v] via G-related fields | CONFIRMED |
| 9 | line u=0, injective restriction, premise applied correctly | CONFIRMED |
| 10 | coordinate irreducibility kills A, then every P_i | CONFIRMED |
| 11 | singleton block: G_z=a*z+C(u), polynomial inverse | CONFIRMED |
| 12 | both explicit determinant controls | CONFIRMED (replayed by hand) |

Surviving scope: exactly the printed statement. The proof in fact yields the
sharper structural form recorded in R1, inside the same hypotheses.

## Independent reconstruction and attacks

Notation: source weights chi_1..chi_n in X^*(T), W:Z^n->X^*(T), K=ker W,
S=K cap N^n, rho source and sigma target representations.

Item 1, normalization. F(rho(t)x)=sigma(t)F(x). At x=0: b=F(0) is
sigma-fixed. Differentiating at 0: M rho(t)=sigma(t) M with M=DF(0)
invertible (Keller). Then G=M^-1(F-b) satisfies
G(rho(t)x)=M^-1 sigma(t)(F(x)-b)=rho(t)G(x), G(0)=0, DG(0)=I,
det DG=det(M)^-1 det DF constant and equal to 1 at 0. F is an
automorphism iff G is. Diagonalizing rho by a linear L and conjugating
G to L^-1 G L preserves all of this. Attack tried: a target
representation not isomorphic to rho. Then no invertible intertwiner
exists, so the hypothesis set is empty; vacuous, not a gap. CONFIRMED.

Item 2, vertex and indecomposables. C[x]^T is spanned by monomials x^h,
h in S, so equals C[S]. The augmentation ideal m is maximal with residue
field C; m^2 is spanned by the monomials of decomposable elements, so
the indecomposable monomials form a basis of m/m^2. Any C-algebra
isomorphism C[S]=C[u,v] sends m to a maximal ideal of a regular
2-dimensional ring, so dim m/m^2=2: exactly two indecomposables alpha,
beta. Induction on total exponent (a decomposable element splits into
two elements of smaller positive total exponent) gives
S=N alpha+N beta. CONFIRMED.

Item 3, S-S=K. Trivial determinant means sum chi_i=0, so 1 in K, and
1 in N^n, so 1 in S. For h in K, h+k1 in S for k>=max(-h_i), and
h=(h+k1)-k1. So K=S-S=Z alpha+Z beta; K has rank 2 (weight rank n-2
from effectiveness), so alpha, beta are Z-independent and S-coordinates
are unique. CONFIRMED. Attack: without 1 in S the step fails, e.g.
weights (1,-1,-2) have S free on (1,1,0),(2,0,1) yet 1 not in K; there
the contraction of Omega equals du^dv/x^2, exactly the boundary factor
the producer says is absent here. Consistent with its section 5.

Item 4, a=b=1. 1=a alpha+b beta, a,b in N. If a=0 pick k>=max alpha_i:
k1-alpha lies in S with alpha-coordinate -1, contradicting uniqueness
with nonnegative coordinates. Same for b. alpha nonzero has some
alpha_i>=1, so 1=a alpha_i+b beta_i>=a, a=1; likewise b=1. Hence
alpha+beta=1, both in {0,1}^n with disjoint nonempty supports I, J,
I cup J=[n]; u=prod_I x_i, v=prod_J x_j. CONFIRMED.

Item 5, zero/repeated weights. chi_i=0 iff e_i in K=Z e_I+Z e_J iff {i}
is a block. chi_i=chi_j for distinct i,j would need e_i-e_j in K: the
same block gives a=1 and a=-1, different blocks force |I|=|J|=1, so
n=2. For n>=3 the weights are pairwise distinct and vanish exactly at a
singleton block. The producer's block argument never uses distinctness,
so nothing is lost either way. CONFIRMED.

Item 6, semi-invariant pieces. G_i(rho(t)x)=chi_i(t)G_i(x) and the
action is diagonal, so G_i is a sum of monomials x^h with h-e_i in K,
h=e_i+a e_I+b e_J in N^n. For i in I with |I|>=2, a second index of I
forces a>=0 and any index of J forces b>=0: x^h=x_i u^a v^b, so
G_i=x_i P_i(u,v). For a singleton block {i}: h=(1+a)e_i+b e_J with
1+a>=0, b>=0, so G_i is an arbitrary element of C[u,v]. Since n>=3, at
most one block is a singleton. CONFIRMED.

## Scope, remarks, OPENs

Item 7, contraction identity. Block I={1..p}, anchor 1, D_i=x_i d_i-x_1 d_1.
The 1-form i_{D_p}..i_{D_2}(dx_1^..^dx_p) has dx_k-coefficient
Omega_I(D_2,..,D_p,e_k). Expanding multilinearly: for k=1 only the term
with every x_i e_i survives, giving (-1)^(p-1) x_2..x_p; for k=i>=2 slot
i must contribute -x_1 e_1, giving -(-1)^p prod_{i' distinct from i} x_i'
=(-1)^(p-1) prod_{i' distinct from i} x_i'. All coefficients share one
sign, so the form is (-1)^(p-1) du exactly, on all of C^p; checked p=2
(-du) and p=3 (+du) by hand. I-fields annihilate Omega_J and J-fields
annihilate du, so the full contraction is +/- du^dv with no monomial or
integer factor. A singleton block contributes no field, and its dz is
dv. CONFIRMED.

Item 8, descent. The image of T lies in D_I x D_J (block products are
invariant), which is connected of dimension (|I|-1)+(|J|-1)=n-2, so
equals it; hence each D_i is a fundamental field of the action and
equivariance gives DG(x)D(x)=D(G(x)). Then G^* i_D=i_D G^* (evaluate on
vectors). G^*Omega=det(DG)Omega=Omega gives G^*(du^dv)=du^dv, i.e.
d(u o G)^d(v o G)=du^dv. u o G and v o G are invariant, so lie in C[u,v];
call them H_1,H_2. Chain rule: (det DH)(u,v) du^dv=du^dv in the free
module of 2-forms over the domain C[x]; du^dv is nonzero since u,v are
algebraically independent, so (det DH)(u,v)=1 in C[x], hence det DH=1 in
C[u,v] by injectivity of C[u,v]->C[x]. No division by a boundary
equation, no bundle claim needed. CONFIRMED.

Item 9, quotient line. With I nonsingleton, H_1=uA, A=prod_I P_i;
d_u H_1=A+uA_u, d_v H_1=uA_v. At u=0: A(0,v) d_v H_2(0,v)=1 in C[v], so
both are nonzero constants and H(0,v)=(0,a v+b), a nonzero: injective
on the affine line {u=0} of the (u,v)-plane. The accepted premise is
applied to a map with det DH=1 and an injective restriction to a genuine
affine line, so its hypotheses match literally. CONFIRMED (premise
consumed, not re-audited).

Item 10, irreducibility. H automorphism gives C[u,v]/(H_1)=C[H_2]=C[t],
a domain, so H_1 is prime, hence irreducible. H_1=uA with u a nonunit
forces A a nonzero constant; in the UFD C[u,v] a product is constant
only if each factor is, so every P_i=c_i is a nonzero constant and
DG(0)=I gives c_i=1. If J is also nonsingleton, the same for H_2 and G
is the identity. CONFIRMED.

Item 11, singleton block. J={z}, v=z, G=(x_I,B(u,z)). DG is block
triangular with unit diagonal on I, so det DG=d_z B(u,z)=1 in C[x],
hence in C[u,z]: B=z+C(u), C(0)=0. The inverse (y_I,w)->(y_I,w-C(prod y_I))
is polynomial. Before normalization the same argument gives
d_z B=1/prod c_i, matching the producer's a. CONFIRMED.

Item 12, controls. Positive: weights (1,-1,0), G=(x,y,z+P(xy)); rows
(1,0,0),(0,1,0),(yP',xP',1), det 1; H=(u,v+P(u)), det 1; equivariance
checked directly. Negative: G=(x,y(1+xy),z); d_x G_2=y^2, d_y G_2=1+2xy,
det 1+2xy; H=(u+u^2,v), det 1+2u, and 1+2u at u=xy reproduces det DG,
so the descent identity is also confirmed on a non-Keller map. Both
CONFIRMED.

### Remarks (not gaps)

R1. Sharper surviving form, same hypotheses: after normalization G is
the identity when both blocks are nonsingleton (so F=Mx+b is affine),
and G=(x_I, z+C(prod_I x_i)) with C(0)=0 when one block is a singleton.
The producer states only "automorphism"; the stronger form is what its
own steps 10-11 deliver and is recorded here as scope, not as a new claim.

R2. Hypothesis redundancy: "effective" and "dimension n-2" are implied by
trivial determinant plus C[x]^T=C[u,v]. A positive-dimensional kernel or
other torus dimension makes rank K differ from 2, and S-S=K then gives an
invariant ring of transcendence degree other than 2. Harmless; nothing
in the proof breaks. Conversely, dropping trivial determinant (weights
(1,-1,-2)) or polynomiality of invariants (weights (1,1,-2), the A_1
cone with three indecomposables) each defeats a specific step, so no
listed hypothesis beyond these two is idle.

Not reviewed: section 6 priority/source remarks (Shaska 2607.20210v2,
AUDIT pointers) are context, outside the charged claim, and no source
discovery was permitted. The n=2 exclusion, nonlinear actions, singular
quotients and nontrivial determinant are outside scope and untouched.

OPENs raised: none. No exit-price assertion, so no charge_basis line.

## COLLISIONS

Actual output of `python3 ops/open_collision.py xmodel/volume-neutral-torus-first-swarmHQ-fable5-20260915T0323Z.md --root .` (exit 0), 03:32 UTC:

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

## Custody

Post-read sha256 of the four inputs at 03:32 UTC, identical to the pre-read
values at 03:23 UTC:

| basename | sha256 |
|---|---|
| COORDINATION.md | 4ce5b29af5a70e096a04b942cb978b1df425f9f0648decb720ec1f089ff37ac4 |
| FALLACY-v2.md | e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5 |
| README.md | 50cf45483cddf637e717ddfa2d136be4df074d13d360b851c1fb62a9e73edb0a |
| volume-neutral-torus-quotient-swarmHQ-root-20260915.md | 181d7ae11675d27a61da977f143abaf5797415d6c64923e11be336281ce6df80 |

Authored only with apply_patch from the supplied PATH, in five bounded
writes; no artifact_finalize.py, no other file touched. Completed 03:33 UTC,
before the 03:37 target.

<!-- BODY-END -->
