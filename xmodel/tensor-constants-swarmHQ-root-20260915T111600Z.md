# Tensor constants of an actual plane Keller map

Producer: swarmHQ ROOT (gpt-6-astra), with native gpt-6-astra co-research.
Date: September 15, 2026 UTC.
Basis: `c72d78e5e9de751ee54b583da9814a0510e31947`.
Evidence: MANUAL/BOOK-relative. Lifecycle: PRODUCER-CHECKED, UNPROMOTED.
Novelty UNKNOWN. No JC2 proof, counterexample, or computational certificate.

## Statement and scope

Let F=(F1,F2):A2_C -> A2_C have nonzero constant Jacobian. Put
R=C[x1,x2], L=Frac(R), and let delta_i be the polynomial derivations
uniquely specified by delta_i(Fj)=Kronecker_ij. On

    B=L tensor_C R = C(p1,p2)[q1,q2]

use the diagonal SUM action: delta_i acts on both tensor factors, so
delta_i(a tensor b)=delta_i(a) tensor b+a tensor delta_i(b). Set

    t_i = F_i(q)-F_i(p),
    E = {b in B : delta_1(b)=delta_2(b)=0}.

Then

    E=C[t1,t2].

Consequently the natural map

    mu: L tensor_C E -> B,  a tensor e |-> (a tensor 1)e

is injective and has image L[F1(q),F2(q)]. Its surjectivity is equivalent
to C[F1,F2]=R, hence exactly to a polynomial inverse for F.

This computes the constants in the stated partial localization. It neither
establishes that surjectivity nor replaces it with a weaker source premise.
No finite exceptional-translation theorem, Chau import, properness,
surjectivity of F, complete flow, or fiberwise cohomology base change is used.

## Dependencies and comparison

The reviewed [branch-disjointness core](disjoint-branch-translates-swarmHQ-root-20260915T093700Z.md)
and its [independent Sol review](disjoint-branch-review-swarmHQ-sol-20260915T094600Z.md)
are the geometric input: the actual translated fiber product is smooth,
nonempty and irreducible when the two Galois branch divisors share no
component. Only that BOOK-relative core is consumed, not its conditional
finite exceptional-set bound. AUDIT records it as DISJOINT-BRANCH-TRANSLATES-1.
Producer full SHA256: ec07f8e07830fe297cb79033abe0a37476aa9fa833526a653ad709e775d2b87e.
Review full SHA256: ba178149d07ca8ac74f01068cc144e67150c71dcb27496d571bd7d3d849b94fd.
Both were wholly reread with unchanged hashes before this report.

The [September13 source comparison](primary-global-watch-astra-20260913.md),
item4, already left the tensor-constant generation criterion unattached.
Adamus--Crespo--Hajto, *Jacobian Conjecture via Differential Galois Theory*,
SIGMA15(2019),034, [publisher PDF](https://sigma-journal.com/2019/034/sigma19-034.pdf),
Theorem3.1, gives polynomial invertibility if this tensor map is an
isomorphism; Remark3.2 reduces surjectivity to generation of the source
coordinates. ROOT read the complete seven-page publisher extraction,
including references, on September15. This report adds an explicit
plane constants calculation to that campaign comparison. It does not
claim an error in their criterion or a new theorem's literature priority.
The paper's general strong-normality proof is not a dependency here.

The other geometric import is [Stacks Project, Lemma37.27.6,
tag055A](https://stacks.math.columbia.edu/tag/055A): for a finite-type
morphism over an integral base, the number of geometric irreducible
components of the fibers is constant on some nonempty base open. ROOT
read the entire statement and proof on September15; its dependency
lemmas were not independently re-audited. This is not the stronger and
generally unavailable assertion of constancy at every parameter.

## Argument

### 1. The geometric generic difference fiber is integral

Let D be the reduced branch divisor of the finite Galois normalization
associated to F, and write its finitely many irreducible components D_i.
For any pair i,j, the translations with D_i=D_j+s form a closed proper
subset of A2_s. To see closedness, normalize leading coefficients of
irreducible defining polynomials and compare the finitely many
coefficients after translation. Equality of the translated curves is
exactly the resulting polynomial coefficient equalities (or impossible
when the normalized top parts differ). The set cannot be all A2: then
D_i would be invariant under every translation, impossible for a proper
nonempty curve. This argument permits line components and positive-
dimensional stabilizers; it does not assert the bad set is finite.

The complement of these finitely many proper closed sets is a nonempty
open. The reviewed core implies irreducibility of each complex fiber of

    Phi:A4 -> A2,  Phi(p,q)=F(q)-F(p),

over a suitable nonempty parameter open (the reviewed report uses the
opposite sign, so its fiber is X_{-t}). If D is empty there is no excluded
translation. The morphism Phi is smooth: its q-Jacobian has rank2
everywhere. All its fibers are nonempty, since the dense open image U
of the etale F meets U-t for every complex t.

By tag055A, geometric component count is constant on a nonempty open
containing the generic point. Intersect this open with the one just
obtained and choose a complex closed point. Its fiber is irreducible,
so the generic geometric component count is one as well. Smoothness
gives geometric reducedness. Thus the geometric generic fiber is integral.
In particular k=C(t1,t2) is relatively algebraically closed in
Omega=C(p1,p2,q1,q2). Equivalently, the corresponding finitely generated
function-field extension is regular; characteristic zero excludes an
inseparable obstruction. This standard function-field consequence is
BOOK-relative, not a new cohomology-specialization theorem.

### 2. Rational constants are k

The t_i are algebraically independent. Indeed F is dominant, and the map
(F(p),F(q)) is dominant onto A4; passing to (F(p),F(q)-F(p)) is an invertible
linear target change. Set u_i=F_i(p). Then Omega is finite separable over

    C(t1,t2,u1,u2)=k(u1,u2).

The diagonal delta_i kill t1,t2 and satisfy delta_i(u_j)=Kronecker_ij.
They are therefore an Omega-basis of Der_k(Omega). In characteristic
zero an element of a finitely generated field extension annihilated by
every base-field derivation is algebraic over that base: if it were
transcendental, extend it to a separating transcendence basis and extend
the derivation taking it to1 through the finite separable extension.
Conversely algebraic elements are killed by all such derivations.
Relative algebraic closedness now yields Omega^delta=k.

### 3. Denominators cannot survive partial localization

Certainly C[t1,t2] lies in E. Conversely let h in E. By the preceding
step write h=P(t)/Q(t) with coprime P,Q in C[t1,t2] and Q nonzero.
As h is in C(p)[q], clearing its FIRST-source denominators gives

    a(p) P(F(q)-F(p)) = Q(F(q)-F(p)) b(p,q)

for nonzero a in C[p] and b in C[p,q]. If Q is nonconstant, choose a
complex t0 such that Q(t0)=0 and P(t0) is nonzero: a component of V(Q)
is not contained in V(P), by coprimality. The two sets

    F(A2 minus V(a))  and  F(A2)-t0

are nonempty dense opens, since F is etale and dominant. Pick a point
in their intersection. It has representatives p,q with a(p) nonzero
and F(q)-F(p)=t0. Evaluation of the displayed polynomial identity gives
a(p)P(t0)=0, a contradiction. Hence Q is constant and E=C[t1,t2].
Only intersection of dense opens was needed, not surjectivity of F.

### 4. The exact remaining surjectivity condition

The t_i are algebraically independent even over L=C(p), since F(q)
is dominant over that field. Thus mu is injective and

    image(mu)=L[t1,t2]=L[F1(q),F2(q)].

Let A=C[F1,F2] be the specified subalgebra of R. Equality of this image
with B is precisely surjectivity of L tensor_C A -> L tensor_C R.
Apply faithful scalar extension L/C to the C-vector space R/A: its
tensor product vanishes if and only if R/A=0. Therefore the equality
holds if and only if A=R. In that case each source coordinate is a
polynomial in F1,F2, giving a polynomial inverse; the converse is immediate.

## Replay and negative controls

Desk-only, no scientific program, primes or random seeds. ROOT manually
reconstructed the proof; native gpt-6-astra separately checked the field,
specialization and denominator steps, completed September15 at11:12:51 UTC.
That same-model co-research is not different-model review or promotion.
The artifact manifest records the publication basis and byte custody.

- For F the identity in characteristic zero, the usual change from (p,q)
  to (p,q-p) gives precisely E=C[q-p], and mu is surjective, as required.
- Characteristic zero is load-bearing even for the identity: in
  characteristic ell>0, p1^ell is killed by the diagonal derivations and
  lies in L, but is not in C[q1-p1,q2-p2]. Thus the stated constants
  calculation must not be exported to positive characteristic.
- The ring matters. If B is further localized at t1, then 1/t1 becomes
  a constant. Its denominator cannot be cleared using only first-source
  polynomials. The claimed E is for L tensor_C R, not arbitrary rational
  localization or a generic translated-fiber coordinate field.
- The proof of geometric generic integrality gives nothing about the
  zero fiber. The clopen diagonal of X0 remains compatible with this
  result if F has degree greater than1. No polynomial inverse is inferred.

## Limitations and next test

The exact constants calculation is unpromoted and uses the reviewed
branch criterion plus the named BOOK-relative imports. Independent
different-model hostile review should precede promotion or descendants.
No new generation algorithm, degree bound, complexity improvement or
actual noninvertible Keller pair is supplied. The calculation identifies
the unchanged polynomial-generation gap; it does not close JC2. Do not
renew tensor generation on the strength of these constants alone.

## OPENS RAISED

None. The already recorded global polynomial-inverse gap is not reissued
as a new bounded task or a source-algebra construction.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9864`.
- Body SHA-256:
  `ac41d0bd37c56b01ed1aafec2c82797e436d16c6b17d71d81e37719286385350`.
- Frozen basis: `c72d78e5e9de751ee54b583da9814a0510e31947`.
