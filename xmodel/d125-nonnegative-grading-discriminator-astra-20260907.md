# D125 straight nonnegative grading: one-row infeasibility certificate

2026-09-07. **NO-GO for the exact straight-grading proposal in Sol2200 Card1.**
A single mandatory original lift equation contains a nonzero rational constant
and a nonzero k monomial. Thus no assignment with wt(k)>0 makes EVERY literal
original generator homogeneous. Nonnegativity of the other weights is not
even needed for this obstruction. This is not an exclusion of the source,
proof that its ideal is inhomogeneous under every generating set, or a result
about recentered coordinates, abstract quotient gradings or filtrations.

## 1. Literal ring; no hybrid or inverse-coordinate substitution

Use accepted14c/14t: S is the polynomial ring over Q in the original normalized
odd source coefficients and k. I contains all unguarded rows, with no z and
no zk-1. The optional whole B-shear slice has no effect on the A row below.
After applying the fixed face coefficients, write

    A=H³+k g²p+sum_(i,j in E) a_ij g^i p^j,
    H=p²(p³+g³),
    phi(g)=v^-1, phi(p)=v^4 u-v-v^-1.

E consists of the33 odd free A slots in the literal polygon with vertices
(0,0),(0,15),(9,6),(2,1), excluding its fixed total and (5,-7) faces.
Equivalently i+j<=15, 5i-7j<=3 and i<=2j, with i+j odd, i+j!=15 and
5i-7j!=3. The whole total face, including zeros, is fixed by H³; the other
nonzero inner coefficient is k at(2,1). These statements are the literal
accepted source, not a claim about arbitrary Keller pairs.

The ring map used here is just this face specialization into S and the
displayed Laurent substitution S[g,p] -> S[u,v,v^-1]. No coefficients are
solved for, no k is inverted, and no map from hybrid81 to the k=0 closure is
assumed or needed.

## 2. The mandatory coefficient row

All negative-v coefficients of phi(A) are rows of I. In particular, let

    L=[u^0 v^-3]phi(A).

For a monomial g^i p^j its contribution is

    c_ij=(-1)^j binom(j,(j-i+3)/2),

where the value is zero unless the lower binomial index is an integer in
[0,j]. The four already fixed top coefficients, at(0,15),(3,12),(6,9),(9,6),
give respectively

    -5005, 2772, -252, 1; their sum is -2484.

This is an individual coefficient projection, not expansion of the full A
or H³. Independently, at u=0 the degree-five H has Laurent expression

    -v^5-5v^3-10v-9v^-1-3v^-3.

Only exponent triples(-3,-3,3),(-3,-1,1),(-1,-1,-1) contribute to its cubic
coefficient at-3; they give -135-1620-729=-2484. Also the actual small lift
phi(g²p)=v²u-v^-1-v^-3 contributes -k. Therefore the literal row is

    L=-2484-k+sum_(i,j in E) c_ij a_ij.            (1)

Exactly32 of the33 free coefficients contribute; (1) has34 nonzero literal
terms. `witness.json` retains the entire sparse row, all33 slots and the
two independent scalar derivations. This is one named row only; no full row
stream or high-degree polynomial was imported or generated.

## 3. Exact infeasibility and its boundary

Give the independent coefficient variables integer weights, with Q in degree0.
If (1) is homogeneous of degree d, its constant term forces d=0, while its
nonzero k term forces d=wt(k). Hence wt(k)=0, a contradiction. This certificate
uses only two monomials of one actual row; a grading feasibility solver is
unnecessary. It rules out even arbitrary integer weights with wt(k)>0 for
this literal-generator requirement, not merely nonnegative weights.

If 'all coefficients' instead means keeping pinned coefficients as variables,
the same obstruction takes three rows: a_(9,6)-1 forces wt(a_(9,6))=0;
the unspecialized lift row contains a_(9,6) and -a_(2,1), forcing their
weights equal; a_(2,1)-k then forces wt(k)=0. Thus eliminating the prescribed
face variables is not responsible for the contradiction.

Sol's proposed abstract bridge is otherwise valid: a homogeneous I and
homogeneous k give homogeneous J=I:k^infinity. If S/J is nonzero and
nonnegatively graded, positive-degree k cannot be a unit, because k times
any finite homogeneous sum has no degree-zero part. Then J+(k) is proper,
providing a finite geometric boundary point for14t. The identified failure
is precisely the proposed sufficient hypothesis that all these actual
original rows be homogeneous.

An inhomogeneous member of an ideal does not alone refute a grading of the
ideal using another generating set: for example (k,a-1), with wt(k)=1 and
wt(a)=0, is homogeneous although its redundant member k+a-1 is not. Likewise
affine changes of coefficient origins change the tested presentation. Neither
possibility is analyzed here. No claim that I or J is proper/unit, that k is
or is not a unit in S/J, or that a boundary point actually exists follows.

## 4. History, controls and stop

The canonical history search found genuine positive/bigradings on the older
Moh/K16 charts, and the named normalized-scaling reports explicitly retain
the lambda character before fixing lambda3=1. Those are different rings.
The whole Sol Card1,14c,14t and symmetry/source reports were read, together
with the pinned literal metadata. No prior claim asserting this normalized
source grading was found in those named checks; no exhaustive novelty claim
is made. In particular, the finite etale comparison at k!=0 in14c is not a
map preserving k=0 closures, as Sol correctly warns.

A one-row control makes the normalization issue visible. If a formal ell
is restored in phi(p)=v^4u-ell*v-v^-1, the constant in (1) becomes
-2484 ell^6 and a_ij is multiplied by ell^((i+j-3)/2). The weights
wt(ell)=1, wt(k)=6, wt(a_ij)=(15-i-j)/2 make THIS row homogeneous of degree6.
The pin ell-1 is not homogeneous. This is a changed-row control, not a new
complete source construction or an assertion of boundary equivalence.

Ten normal/-O controls pass with identical witness bytes and zero Assert
nodes. Changed actual objects include a top-face coefficient, the v^-1 lift
sign, deletion of the constant and deletion of the k term; the same exact
coefficient/certificate checks reject them. Separate unchanged homogeneity
checks show that deleting either mandatory term can falsely admit a positive-k
candidate. Only a literal polygon is parsed from metadata; make_contract and
its power routines are NEVER imported or called. Each local child is bounded
by30wall/25CPU/512MiB and uses Python -I -B before imports. Witness SHA256
`e6efd2c671f9c4ef8a1588d8a27b81b9fbaf993e5a7cc52a34af6357d50d2e2d`.

Replay `check.py` normally/-O in the owned box with those caps. Inputs,
history/read scope and owned artifacts are pinned in custody. No full source
expansion, AWS/SSH/CAS, linear solver, initial ideal, filtration program,
canonical edit, live peer read or agent fanout occurred. The task stops at
this exact small no-go; no alternative grading program is launched. The
new certificate is PRODUCER-CHECKED pending review. All writers idle at
handoff. **STOP/IDLE.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6879`.
- Body SHA-256:
  `9ca3476d7fa94e669e0273e0b17c307fa7e0d6ee52ed3342700f39094291836b`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
