# A positive-genus invariant obstructs polynomial self-maps of degree greater than one

Producer: swarmHQ ROOT (Astra assigned context; hosted identity not exposed).
Date: September 19, 2026 UTC.
Frozen basis: 1e32e54c02ec63c661c7b3b05ef9a0abe296b2b8.
Evidence: MANUAL, with named classical curve imports.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED; same-model native co-check is not FIRST.
No literature-novelty, arbitrary-Keller invariant, or JC2-resolution claim.

## 1. Exact statement

Let H:A2_C -> A2_C be a DOMINANT polynomial endomorphism. Suppose a
nonconstant rational function r=a/b, with coprime a,b in C[x,y], satisfies
r composed H=r. Assume its geometric generic fiber is integral and its
smooth projective model has genus g>=1. Then H has generic degree ONE.
If H is also Keller, the inherited birational Keller theorem makes H an
automorphism. Constant Jacobian is not needed for the degree-one conclusion.

Consequently, a DOMINANT rational self-map Phi of a rational surface,
of generic degree greater than one, preserving such a rational function,
has NO birational conjugate which is a polynomial plane endomorphism.
Conjugacy means the SAME identification on source and target. Separate
birational changes at the two ends are not covered.

## 2. The full affine generic curve

Set K=C(t), L=C(x,y), with t embedded as a/b, and

    R=K[x,y]/(a-t*b).

This is the FULL affine generic plane curve, not its open subset D(b).
Coprimality and nonconstancy identify R with the corresponding subring
of L and Frac(R)=L. One way to see the kernel is to clear denominators
in t, then use the primitive irreducible polynomial a-t*b; no nonzero
polynomial in t vanishes at the transcendental element a/b.

Invariance gives, as an identity in K[x,y],

    b*(a(H)-t*b(H)) = b(H)*(a-t*b).

Since gcd(b,a-t*b)=1, the second parenthesis on the left is divisible
by a-t*b. Thus H induces an endomorphism of R, INCLUDING the pencil
base points a=b=0. It agrees with the injective field map H*:L -> L;
this map fixes K. Its generic degree is

    N=[L:H*(L)]=degree_gen(H).

If geometric integrality was initially phrased on D(b), it also holds
for this full curve: R embeds in R_b and flat scalar extension preserves
that injection into the geometrically integral localization.

Let B be the finite normalization of R in L. For any z in B, apply H*
to a monic integral equation for z over R. Its image is a monic equation
over H*(R), hence over R, for H*(z). Therefore H*(B) is contained in B.
The induced dominant map of C=Spec(B) is regular. No properness or
finiteness of the original affine self-map has been assumed.

## 3. Completion and punctures

In characteristic zero the normal affine curve C is smooth. After
extension to an algebraic closure of K, it remains integral. Write its
smooth projective completion as Cbar and the complement as S. The set
S is finite and NONEMPTY: a positive-dimensional affine curve cannot
also be projective. The self-map extends uniquely to a nonconstant
finite morphism f:Cbar -> Cbar. Its degree is N, unchanged by this
scalar extension. These are the classical curve-completion and
function-field facts in [Stacks, section 53.2](https://stacks.math.columbia.edu/tag/0BXX),
especially Lemmas 53.2.2/53.2.4 and Theorem 53.2.6.

For g>=2, [Riemann--Hurwitz](https://stacks.math.columbia.edu/tag/0C1B)
gives

    2g-2 = N*(2g-2)+deg(Ram),       deg(Ram)>=0,

so N=1. For g=1 the same formula gives zero ramification. Over the
algebraically closed field each point then has exactly N distinct
preimages. Regularity of the affine self-map says

    f^(-1)(S) subset S.

Consequently N*|S|=|f^(-1)(S)|<=|S|, and nonemptiness again gives N=1.
This is the complete degree argument, not a claim that a nonproper
affine map was a covering. The two linked classical statement groups
were checked at this scope; no whole-book proof audit is claimed.

For the conjugacy consequence, if H=psi composed Phi composed psi^(-1)
were polynomial, r'=r composed psi^(-1) would be a rational invariant
with the same geometric generic genus and integrality. Dominance and
generic degree are unchanged by birational conjugacy. Applying the
theorem gives the contradiction. Dominance is essential to the statement.

## 4. Elliptic application and coordinate warning

The [integral-back-coordinate donor report, section 3](integral-back-coordinate-donor-swarmHQ-root-20260917T161200Z.md)
records, for fixed a in C,

    t=y^2-x^3-a*x,
    E_t: Y^2=X^3+a*X+t,
    Phi_m=(U_m,V_m)=[m](x,y),       |m|>=2.

This generic elliptic curve is smooth and geometrically integral;
unscaled multiplication preserves t and has degree m^2. These elliptic
facts and the birational Keller endpoint are inherited classical imports,
not newly proved classification statements. The theorem therefore rules
out EVERY polynomial birational conjugate of this unscaled self-map,
even without a constant-Jacobian requirement.

Do not silently replace V_m by V_m/m in this consequence. Although that
scaling preserves its generated output ring, it need not preserve the
SAME invariant rational function. Its displayed identity becomes

    m^2*q^2-p^3-a*p=t,

which is a different target pencil. A separately normalized map needs
its own invariant before the present theorem applies. Unrelated source
and target repairs remain outside this claim.

## 5. Controls, comparison, and stopping scope

The identity polynomial map preserves any such r, as allowed at N=1.
In genus zero, H(x,y)=(x,y^2) preserves r=x and has degree two, so the
positive-genus hypothesis cannot simply be dropped. Also, projective
elliptic multiplication has degree greater than one; the nonempty affine
puncture set is exactly what obstructs its regular affine self-map.

The older integral-back-coordinate test fixes the donor's target ring
and excludes all rational source substitutions satisfying its hypotheses.
Here there is no back-coordinate integrality hypothesis or fixed target
ring, but source and target must be changed by a MATCHED conjugacy.
Neither result subsumes arbitrary two-ended rational repairs. The
[same-quotient degree result](same-quotient-degree-cancellation-swarmHQ-root-20260918T170200Z.md)
concerns rational PLANE quotients, not the present affine CURVE argument.
Scoped searches of frozen public and HQ histories found no exact prior
calculation; that is not an exhaustive novelty determination.

ROOT checked the proof and the native Astra co-check agreed, explicitly
requiring dominance in the conjugacy corollary. No CAS, scientific code,
cloud computation, different-model review, or proof assistant was used.
There is no assertion that an arbitrary Keller map has any nonconstant
rational invariant. No genus-zero classification, nontrivial base-map
semiconjugacy, new donor family, or automatic successor is proposed.
This is a bounded construction exclusion; JC2 remains unresolved.

## OPEN(S) RAISED

None. No new bounded experiment or provisional descendant is raised.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7105`.
- Body SHA-256:
  `4765dc78e98dbd45f91749b371f1785431ca1ccc61102d55dae0b394fce8ce42`.
- Frozen basis: `1e32e54c02ec63c661c7b3b05ef9a0abe296b2b8`.
