# A D4 obstruction to a representation-only rational-base reduction

Producer: swarmHQ (ROOT/Astra; native Astra same-model manual co-check).
Date: September 17, 2026.
Basis: c06af4b34a39912fd4b22c4eb1e1b0814bd86be7.
Evidence tier: MANUAL, with classical Riemann existence/algebraization imported.
Lifecycle: PROVISIONAL; different-model hostile review pending.

## 1. Exact statement and excluded stronger readings

There exist a smooth connected affine complex curve C, a faithful action of
a finite group G on C with C/G isomorphic to A1, and a nonzero rational
G-module M, such that

    M^G = 0,    Hom_G(M,H^1(C,Q)) = 0,

but for EVERY subgroup H <= G with M^H != 0, the quotient C/H is NOT
isomorphic to A1. Thus the two displayed representation conditions alone
do not reduce arbitrary finite base covers to polynomial A1 base covers
retaining a nonzero invariant vector.

The witness is G=W(D4), the even signed permutations of four coordinates,
and its natural module M=Q^4. The notation C/Q in cohomology does not change
the ground field of the curve: C is a complex curve, Q the coefficient field.

This is NOT a Keller pair or a realization of M by geometric units on an
actual source. It refutes neither geometric-unit vanishing nor the reviewed
globalization bridge. Additional source/unit hypotheses could invalidate
this abstract witness as a model of the desired application. No JC2 proof,
counterexample, arbitrary finite-cover classification or group search follows.

## 2. Dependencies and comparison

The [geometric-unit globalization theorem](geometric-unit-globalization-swarmHQ-root-20260916T232700Z.md)
allows a unit on a geometric generic fiber to be represented, after power
and base rescaling, by a global unit on a finite base-changed source, under
its nonsingularity and EVERY-fiber-irreducible hypotheses. It does not
exclude that unit. A proposed subsequent reduction would retain a unit
representation on an intermediate A1 base, where a separate polynomial-base
argument might apply. The present theorem disproves only the bare group/
curve criterion stated in Section 1. It does not consume an unproved trace
pairing or polynomial-base vanishing assertion.

Named standard imports: Riemann existence for a generating product-one
branch tuple, algebraization of a compact Riemann surface and its finite
map; compact-support cohomology and Poincare duality of a smooth affine
curve; Maschke's theorem, Frobenius reciprocity; inertia orbits describing
points in an intermediate cover. Their exact uses are spelled out below.
Riemann existence is an explicit import, not freshly primary-proof-audited.
No priority claim is made for this finite-group example. Scoped history
searches found the earlier unit-globalization and trace-pairing gaps, not
this precise criterion; absence of a search hit is not novelty evidence.

## 3. Group and branch tuple

Write e1,e2,e3,e4 for the standard basis. G consists of the 4! coordinate
permutations and 2^3 even sign choices, hence has order192. Let s1=(12),
s2=(23), s3=(34) act as coordinate permutations, and define s4 by

    s4(e3)=-e4, s4(e4)=-e3, s4(e1)=e1, s4(e2)=e2.

Each si has order2 and a three-dimensional fixed subspace. The first three
generate S4. The product s3*s4 flips signs on coordinates3,4; its S4
conjugates generate all even sign changes. Thus the four si generate G.

With rightmost factors acting first, c=s1*s2*s3*s4 sends

    e1 -> e2 -> e3 -> -e1,    e4 -> -e4.

Consequently c^3=-I, and c has order6. In particular it is not of order2:
c(e1)=e2. The tuple (s1,s2,s3,s4,c^(-1)) has product1 and generates G.

Choose four distinct finite points of P1 and infinity. Riemann existence
applied to this tuple gives a connected regular G-cover X -> P1 with
these five inertia generators. Algebraization gives X a smooth connected
projective complex algebraic curve and the cover a finite algebraic map.
Remove precisely the points above infinity, and call the result C. It is
smooth, connected and affine, G acts faithfully, and C/G=A1. No explicit
polynomial equation for X is required by the imported existence theorem.

## 4. Rational equivariant cohomology

All identities in this section are in the Grothendieck group of rational
G-representations. Stratify the target A1 into the four branch points and
their complement U. Then chi_c(U)=1-4=-3. Above U the cover is free, so
its equivariant compact-support Euler characteristic is
-3[Q[G]]. This follows, for example, by lifting a finite compact-support
cell decomposition; it is an Euler-characteristic assertion, not triviality
of the covering local system.

The orbit over the ith finite branch point contributes
[Q[G/<si>]]. Additivity therefore gives

    chi_c,G(C) = -3[Q[G]] + sum_i [Q[G/<si>]].

Since C is connected and noncompact, H_c^0(C,Q)=0 and H_c^2(C,Q)=Q.
The latter representation is trivial since the action preserves complex
orientation. Poincare duality identifies H^1 with the dual of H_c^1
(a Tate twist is irrelevant to these rational G-representations). All
permutation representations displayed above are self-dual. Hence

    [H^1(C,Q)] = [Q] + 3[Q[G]] - sum_i [Q[G/<si>]].       (1)

The natural module has M^G=0: invariance under every pair sign flip forces
all four coordinates to vanish. It is self-dual under the standard dot
product. By Maschke, Hom_G(M,-) is exact; Frobenius reciprocity gives

    dim Hom_G(M,Q) = 0,
    dim Hom_G(M,Q[G]) = dim M = 4,
    dim Hom_G(M,Q[G/<si>]) = dim M^<si> = 3.

Applying it to (1) yields dim Hom_G(M,H^1(C,Q))=0+3*4-4*3=0.
This is a rational calculation; no passage from missing complex characters
to missing rational constituents is assumed. For an additional check, M
is absolutely irreducible: its restriction to the even-sign subgroup has
four distinct coordinate characters and S4 permutes their lines transitively.
Irreducibility is not needed for the dimension calculation itself.

## 5. No rational one-puncture quotient retaining a vector

Every nonzero vector v in M has G-orbit of size at least8. If its support
has size k=1,2,3, coordinate permutations and sign changes yield at least
binomial(4,k)*2^k distinct vectors: first choose the support, then all sign
choices there. A zero coordinate absorbs the even-parity constraint. The
three lower bounds are8,24,32. For support size4 the subgroup of even
sign changes already gives8 distinct vectors. Repeated nonzero coordinates
do not merge the distinct supports or the distinct sign patterns counted.

If M^H !=0, choose v !=0 fixed by H. Then H is contained in Stab_G(v),
so [G:H] >= [G:Stab_G(v)] >=8.

On the other hand, suppose C/H is isomorphic to A1. The smooth projective
curve X/H then completes it by exactly one point. Since C was obtained by
removing all points over infinity, this says there is exactly one point
of X/H above infinity. Such points are the orbits of the cyclic infinity
inertia I=<c> on G/H (equivalently the appropriate double cosets). Thus I
acts transitively on G/H, forcing [G:H] to divide |I|=6. In particular
[G:H] <=6, a contradiction. This applies to nonnormal as well as normal H.

## 6. Checks and controls

Desk-only; no CAS, numerical search, worker or scientific program used.
ROOT and one native Astra instance checked the displayed tuple, rational
cohomology dimensions and orbit obstruction separately; this is same-model
co-research, NOT the required different-model hostile review.

Riemann--Hurwitz supplies an independent scalar checksum:

    2g(X)-2 = 192*(-2 + 4*(1-1/2) + (1-1/6)) = 160,

so g(X)=81. Infinity has192/6=32 points. Consequently b1(C)=2*81+32-1
=193, agreeing with dimensions in (1):1+3*192-4*96=193.

Positive control for the proposed implication: let G=C2 act on C=A1 by
z -> -z and let M be the one-dimensional sign module. Here C/G=A1,
M^G=0 and H^1(C,Q)=0; H={1} has C/H=A1 and M^H=M. So the hypotheses
are nonvacuous and sometimes give the desired quotient. In that control,
the minimal nonzero-vector orbit is2, matching the inertia order2; the
strict orbit/inertia mismatch in the D4 witness is genuinely needed.

The negative-scope control is that no map from an actual finite-base-changed
Keller source to a unit torus has been constructed. Replacing the abstract
module in Section 1 by actual geometric units is an additional hypothesis,
not a feature of this example and not a conclusion of its existence proof.

## 7. Limitations and next test

The cheapest next test is a single independent manual hostile audit of
Sections3--6, including the RET interface, rational duality and quotient
conventions. A successful audit would close this representation-only
shortcut at exactly the stated scope. No higher-rank family, geometric-unit
realization search, or descendant theorem is proposed. The all-degree JC2
properness/construction gap is unchanged.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8965`.
- Body SHA-256:
  `99b369f08791bb2ff11580e8372c8c22ba0926bd2e9ed634b17f978ed29be86f`.
- Frozen basis: `c06af4b34a39912fd4b22c4eb1e1b0814bd86be7`.
