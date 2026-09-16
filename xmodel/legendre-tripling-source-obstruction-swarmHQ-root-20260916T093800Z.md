# Legendre tripling: a ramified target line obstructs every finite source repair

Producer: swarmHQ ROOT (gpt-6-astra), with native Astra co-research.
Date: September16,2026. Basis: abbfd9055c3e2e28f5d54fc2945be5f4bac74a9f.
Evidence: MANUAL / named classical import. Lifecycle: PRODUCER-CHECKED,
UNPROMOTED. Same-model co-research is not different-model FIRST.

## 1. Exact fixed construction and conclusion

Work over C. In L=C(x,z), put

    h=x-x(x-1)z^2,       y=x(x-1)z,
    E_h: Y^2=X(X-1)(X-h),
    P=(x,y),            [3]P=(U,Y3),
    V=Y3/(U(U-1)),      K=C(U,V).

These are rational functions; denominators are not asserted to be units
on the original plane. The generic elliptic curve is smooth because h
is transcendental. The function-field identification is
L=C(h)(E_h), with inverse z=y/(x(x-1)). In particular

    h=U-U(U-1)V^2,     [L:K]=9,     J_(x,z)(U,V)=3.       (1)

Replacing V by V/3 normalizes the rational Jacobian to one, without
changing K or the target polynomial algebra C[U,V].

**Fixed-donor exclusion.** There is no C-field embedding

    iota:L -> M=C(s,t)

of any finite degree for which iota(U),iota(V) both belong to C[s,t]
and have nonzero constant Jacobian. Thus neither a birational source
change nor a higher-degree rational source substitution repairs this
specific rational pair into a whole-plane polynomial Keller pair.

The decisive fact is an actual divisorial valuation of L above the
generic target line U=0 with ramification index THREE. It is not merely
a pole in a chosen formula. No class-group, Galois or primitive-block
assumption is used. Only this fixed tripling construction is treated;
arbitrary target-field changes and other isogeny families are not covered.

## 2. Why the rational Jacobian is constant

Multiplication by three on a characteristic-zero elliptic curve has
degree nine and multiplies its invariant differential by three. These
standard elliptic-curve facts give the degree in (1) and, relatively over
C(h),

    dU/(2Y3)=3 dx/(2y) modulo dh.

For the degree see [Milne, Elliptic Curves](https://jmilne.org/math/Books/EC2.pdf),
II, Theorem6.1, applied to integer multiples of the identity. The differential
factor also follows directly: addition has derivative (v,w)->v+w at the
identity, hence [3] has derivative v->3v; pullback preserves invariant
differentials. These are characteristic-zero algebraic group facts, so
they apply over C(h), not just to a fixed complex fiber.

Here the absolute differential calculation is explicit:

    dh wedge dx/(2y)=dx wedge dz,
    dh wedge dU/(2Y3)=dU wedge dV.

For example h_z=-2x(x-1)z=-2y, so wedging dh with dx gives
2y dx wedge dz. Wedging the relative identity with dh proves the
Jacobian assertion in (1). No absolute one-form identity is inferred
from a relative one. The group-law degree and differential facts are
only used to describe this candidate; the ramification computation below
is explicit and does not depend on a torsion-monodromy classification.

## 3. A divisorial valuation, not a specialized arc

Set

    a=x,     b=1+(1-x)z^2,     h=ab.

At each point (x,z)=(0,epsilon*i), epsilon in {1,-1}, the pair (a,b)
is a regular parameter system: b_z=2(1-x)z is nonzero there. Take the
divisorial monomial valuation w with

    w(a)=1,     w(b)=2,     r=residue(b/a^2).

Its residue field is C(r), where r is TRANSCENDENTAL over C. One may
realize it by two point blowups in this regular local surface. Equivalently
one substitutes a=q,b=r q^2 in C(r)((q)) and takes the branch
z=epsilon*i+O(q). The latter is notation for the divisorial valuation,
not specialization of r to a numerical constant or a finite-jet solution.
The value group is Z because w(a)=1.

The usual elliptic group law gives

    psi2=2y,
    psi3=3x^4-4(1+h)x^3+6hx^2-h^2,
    psi4=4y [x^6-2(1+h)x^5+5hx^4-5h^2x^2
                  +2(1+h)h^2x-h^3],
    U=x-psi2*psi4/psi3^2.

Substituting x=a,h=ab gives psi3=a^2 D and psi4=4y a^3 C, where

    D=3a^2-4a-4a^2b+6ab-b^2,
    C=a^3-2a^2-2a^3b+5a^2b-5ab^2+2b^2+2ab^3-b^3.

Since y^2=a^2(a-1)(1-b), the exact first coordinate is

    U=a N/D^2,     N=D^2-8(a-1)(1-b)C.                 (2)

For weights wt(a)=1,wt(b)=2, the initial part of D is -4a.
The cancellation determining N is displayed in full through weight four:

    D^2 = 16a^2-24a^3+9a^4-48a^2b + terms of weight>=5,
    8(a-1)(1-b)C
        = 16a^2-24a^3+8a^4-56a^2b-16b^2
          + terms of weight>=5.

Thus in_w(N)=(a^2+4b)^2, and (2) gives

    w(U)=3,
    residue(U/a^3)=(1+4r)^2/16,
    residue(h/U)=16r/(1+4r)^2.                         (3)

These coefficients are nonzero in C(r); exceptional numerical choices
of r are not separate divisorial cases. The retained target equation
h=U-U(U-1)V^2 implies

    V^2=(h/U-1)/(1-U),
    residue(V^2)=-(1-4r)^2/(1+4r)^2.                   (4)

Consequently w(V)=0 and its residue is one of the two rational functions
plus or minus i*(1-4r)/(1+4r). Each is nonconstant and generates C(r).
The sign need not be selected for this argument.

It follows that w restricts to exactly THREE times ord_(U=0) on K.
Indeed every nonzero polynomial in V has valuation zero, since its
residue is evaluated at a transcendental element. For a polynomial in
U with coefficients in C[V], its least U-power therefore has unique
least valuation; passage to quotients proves the assertion for K.
This also proves residue degree one over C(V). Thus w is a genuine
ramified height-one place of the finite normalization above the target
line, even though its center on the ORIGINAL source plane is a point.

## 4. Ramification persists under an arbitrary finite source substitution

Suppose an embedding as in section1 exists and identify K subset L subset M.
Let R=C[s,t], A=C[iota(U),iota(V)], and T the integral closure of A in M.
Then T is finite over A. Normality of R places T inside R, since each
element of T is integral over A subset R and belongs to Frac(R).

The hypothetical polynomial Keller map is etale and quasi-finite. Its
Zariski Main factorization identifies Spec R with an open subset of
Spec T, followed by the finite map to Spec A. This is the FULL-field
normalization in M, not an open-immersion assertion about an arbitrary
proper intermediate normalization in L.

Extend w to a divisorial valuation w' of M. Multiplicativity of indices gives

    e(w'/ord_(U=0))=e(w'/w)*3 >= 3.                    (5)

The extension has a height-one center E on Spec T above U=0. Since the
map is etale on Spec R, the generic point of E is absent from Spec R.
Thus E is a missing ramified divisor of the full finite normalization,
and its image is the target line U=0.

This line is a component of the nonproper-value set of the hypothetical
polynomial map. To see the implication directly, choose a general complex
point of E and approach it through the dense open Spec R. Its finite
images approach the corresponding point of U=0, but the points of the
source plane leave every compact subset; otherwise their limit would lie
in Spec R. The nonproper set is a closed curve, so the line, not only a
selected point, is contained and is an irreducible component.

The final imported obstruction is the classical no-line-component theorem:
a nonsingular polynomial plane map cannot have an irreducible component
isomorphic to A1 in its nonproper-value set. See Nguyen Van Chau,
[arXiv:0710.5212v1](https://arxiv.org/pdf/0710.5212), page3, equation(1.4),
the paragraph following it and Theorem1.2; Section5 gives the pertinent
proof. Here the component is already the literal coordinate line, so no
additional straightening of an abstract embedded A1 is needed. This
contradicts (5)'s consequence and proves the fixed-donor exclusion.

This is a new attachment of a known obstruction, not a new no-line theorem.
There is no claim that every possible rational donor has such a branch line.

## 5. Controls, history and stopping scope

- Multiplication by ONE gives (U,V)=(x,z), the identity plane map. At the
  generic source line x=0 its ramification index is one. At the special
  valuation of section3 its residue z is constant, so it centers at a
  target POINT, not a generic line. Neither step of the obstruction fires.
- The polynomial map (s,t)->(s^3,t) has ramification over a target line,
  but Jacobian3s^2 is not a nonzero constant. Ramification alone does not
  prohibit polynomial maps; the whole-plane etale hypothesis is essential.
- No special value of r, degree bound for a source substitution, or Galois
  identification was used. Rational source functions need not be polynomial.
- The September14 20:52 [historical elliptic test](../notes.md#2026-09-14-2052-utc--elliptic-multiplication-fails-the-normalization-screen)
  concerns y^2=x^3+h and a positive-grading/torsion-class-group obstruction.
  This fixed non-isotrivial candidate is excluded by actual ramification
  over a target line instead. No extension of that old class-group proof
  is claimed or needed.
- The accepted positive-genus ramification filter is not invoked: this
  valuation has rational residue field C(r). Its target LINE, together
  with the constant-Jacobian hypothesis, supplies the present obstruction.

STOP this fixed construction. No other multiplier, elliptic-family,
target-coordinate, normalization-computation or coefficient-search
successor is commissioned. No polynomial counterexample, all-donor
exclusion, arbitrary Keller source constraint or JC2 resolution follows.

## 6. Read scope and evidence custody

Manual reasoning only: no scientific subprocess, CAS, sampled numerical
calculation, worker or finite-degree source search. The weighted terms in
section3 are exact initial-form computations, not an approximate solution.
ROOT and native Astra independently obtained (3)-(4) before comparing
their calculations. Native co-research is not different-model review.
The native task started09:32:45 and terminated09:37:59 UTC, with actual
startup executable checks completed. Its final message was collected
before sealing. It checked the no-line campaign attribution, not the
primary proof; ROOT's primary reading is separate.

ROOT read the complete named September14 elliptic journal entry, selected
current history and the whole accepted positive-genus producer report.
The primary Chau paper's complete parsed text was recovered in two reads;
its no-line result is an explicit dependency, not a newly promoted proof
of the underlying classical literature. No exhausted/source-stopped URL
was retried. Targeted discovery searches are not an exhaustive novelty
survey or a new broad-sweep completion.
Milne II, Theorem6.1 and the selected differential discussion were read;
no whole-book audit is claimed. FALLACY and current frontier/digest pins
matched their pre-task values before closure.

Different-model review of this frozen report must precede promotion.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

The trusted collision checker completed exit0. EMPTY concerns identifiers,
not novelty or proof. The manual history comparison and the distinct
isotrivial/rational-residue scopes are stated above.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11155`.
- Body SHA-256:
  `4c5933231e65b474e378354eaa11da7df73f3b5f12f7a3f735a09772faeae758`.
- Frozen basis: `abbfd9055c3e2e28f5d54fc2945be5f4bac74a9f`.
