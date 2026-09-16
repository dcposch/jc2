# The retained fixed-direction formal pair is not algebraic

Producer: swarmHQ ROOT (gpt-6-astra), with native Astra co-research.
Date: 2026-09-16 UTC. Basis: dd0f956fc282d398c1779567543e8bda956b0c01.
Evidence: MANUAL. Lifecycle: PRODUCER-CHECKED / UNPROMOTED at author seal.
Different-model review is separate. JC2 remains unresolved.

## Statement and precise scope

Consider the exact formal construction in the September11
[source blind](ideation-20260911T1100Z-astra-source.md), section
"A scoped new-in-packet countercontrol", and its
[source cross](ideation-20260911T1100Z-cross-astra-source.md), section C-D.
The surface, completion and initial pair are

    S: U^2=A+A^2 Z,
    Rhat=C[z][[u]],   u=U, z=Z,
    A+z*A^2=u^2,     A(0,z)=0,
    H_0=z^2-u,       G_0=z^3-z-(3z/2)*u.

Use the bracket {u,z}=2(1+2Az). Whenever {H,G}=2+e_n(z)u^n
modulo u^(n+1), the specified correction, for n>=1, is

    (delta H,delta G)
       = -e_n(z)/(2(n+1)) * (-1,-3z/2) * u^(n+1).       (1)

THEOREM: the limiting H and G produced by this precise algorithm are
transcendental over C(u,z). Hence neither is algebraic over the function
field C(S), and neither becomes a rational function after any finite
algebraic extension of C(S). In particular this retained formal pair
cannot itself algebraize to regular functions on S or on a Zariski-open
neighborhood of its completed line.

This is an exclusion of the FIXED recursion (1), not of every formal pair,
every pair with the same boundary values, or every regular scalar-bracket
pair on S. The previously established formal/all-finite-jet construction
remains valid. No finite-jet contradiction is claimed.

## 1. The invariant direction gives one formal unknown

Every correction (1) is in the same direction as the initial u-term.
Consequently the pair, at each stage and in the limit, has the form

    H=z^2-F,
    G=z^3-z-(3z/2)*F,        F in u*C[z][[u]], F=u+O(u^2).       (2)

Direct differentiation, retaining the z-dependence of the direction,
gives the exact cancellation

    H_u*G_z-H_z*G_u=(1+3F/2)*F_u.                         (3)

Indeed H_u=-F_u, H_z=2z-F_z,
G_u=-(3z/2)F_u and G_z=3z^2-1-(3/2)F-(3z/2)F_z.
The F_z terms and the 3z^2 terms cancel in (3).

Set D=1+2zA. The surface relation gives

    D^2=1+4zu^2,       D(0,z)=1.                         (4)

The equation {H,G}=2 therefore becomes

    (1+3F/2)*F_u=1/D,
    partial_u(F+3F^2/4)=(1+4zu^2)^(-1/2).               (5)

Define I in u*C[z][[u]] by

    I_u=(1+4zu^2)^(-1/2),       I(0,z)=0.

Termwise integration uses only nonzero integers and gives

    I=sum_(j>=0) (-1)^j*binom(2j,j)*z^j*u^(2j+1)/(2j+1).

Equations (5) and the zero constant term give

    I=F+3F^2/4,
    F=(2/3)*(sqrt(1+3I)-1),                              (6)

with the square root of constant term one. This also proves formal
uniqueness. Conversely (6) has coefficients in C[z], satisfies (5),
and begins with u. The algorithm (1) produces this unique solution:
an error e_n*u^n is changed by delta F=-e_n*u^(n+1)/(2(n+1));
in (3) its degree-n effect on the full bracket is exactly -e_n*u^n.
All other effects have higher u-order. Thus the closed-form reduction
identifies the retained recursion, not a different formal solution.

## 2. Its antiderivative cannot be algebraic

Work over k=C(z), treating z as a transcendental constant for partial_u.
On the smooth projective conic with function field

    k(u,D),       D^2=1+4zu^2,

consider the relative rational differential omega=du/D. Extend constants
by s with s^2=z. The conic has rational parameter t with

    u=t/(s*(1-t^2)),       D=(1+t^2)/(1-t^2).

These formulas satisfy (4) and yield

    omega=dt/(s*(1-t^2)).                               (7)

Its residues at t=1 and t=-1 are respectively -1/(2s) and 1/(2s),
both nonzero. They are the two points over u=infinity. The formal branch
used in (4) is t=0, so this is the same differential as I_u=1/D.

Suppose I were algebraic over k(u). Adjoin I,D,s and, if necessary,
extend the constant field to an algebraic closure. A connected component
of the resulting smooth projective normalization is a finite cover of
this conic. Its rational function I would satisfy dI=omega pulled back.
The equality follows by differentiating the specified formal branch;
characteristic-zero algebraic derivations extend uniquely.

At any point over t=1 with ramification index e>=1, the pulled-back
differential has residue -e/(2s), which is nonzero. This follows directly
from pulling back dt/(t-1) in a local uniformizer. An exact differential
of a rational function has residue zero: differentiating a Laurent
series never produces a nonzero coefficient of dw/w. Contradiction.

Thus I is transcendental over k(u). By (6), algebraicity of F would imply
algebraicity of I, so F is transcendental too. Equation (2) then gives
transcendence of H and G (z is nonzero in k).

Finally C(S) is algebraic over C(u,z), since A satisfies the displayed
quadratic relation. Any finite algebraic extension of C(S) is algebraic
over C(u,z); it cannot contain the specified F,H or G. This rules out
algebraization of these exact formal series, not just polynomial
termination. A polynomial in A,U,Z can have an infinite u-expansion;
nontermination alone would not have proved the theorem.

## 3. Checks, dependencies and excluded conclusions

Desk-only; no CAS, coefficient run, numerical experiment or code from an
external source was used. The proof rederives the recurrence, bracket,
conic parametrization and residue obstruction. The standard curve facts
used are existence of a smooth projective normalization of a finite
function-field extension and the local residue pullback calculation.
The latter and vanishing of exact residues are explicitly proved above.
No formal-GAGA or G3 theorem is used.

Two important scope checks:

- At z=0, I=u and F is algebraic by (6). This SPECIALIZATION does not
  contradict transcendence over C(z)(u); no assertion is made that every
  fixed-z specialization is transcendental.
- Each finite u-truncation is still represented by polynomials in U,Z.
  The all-order obstruction is a nonzero residue in the generic function
  field, not a failed finite boundary equation.

The boundary values remain (z^2,z^3-z), with the collision at z=1,-1.
No general obstruction to those boundary values, no global submersion
classification and no exclusion of all scalar pairs on S follows.
In particular the valid construction endpoint "a regular scalar pair on
S gives a plane Keller counterexample" is unchanged.

The native Astra co-researcher completed the whole recurrence/residue check
at00:42 UTC; its whole final response and authoritative COMPLETED status
were collected before the author seal. Its independent parameter
w=D+2*sqrt(z)*u gives omega=dw/(2*sqrt(z)*w), agreeing with (7).
ROOT checked both parametrizations and every scope distinction above.
No source theorem beyond the stated standard curve facts was imported.
Different-model review remains separate. All charged pre/post pins matched.

Charged history/guardrail pre/post SHA256 pins:

- FALLACY-v2.md:
  e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.
- xmodel/ideation-20260911T1100Z-astra-source.md:
  72e901ea33e07a5f6ad2f918da4c7674dc6f84e6f366f6b03d3a974d8bd4df8e.
- xmodel/ideation-20260911T1100Z-cross-astra-source.md:
  fa57c775349f3977fed7383e20a100876c9ff5e4b720e8b0ef1723dd70100a7a.

## Limitations and next test

The unchanged fixed-direction recursion cannot be a construction route,
even if more coefficients are computed. No jet or support farm follows.
Other correction directions or global constructions require their own
actual polynomial/algebraic realization; none is supplied or commissioned.
The current candidate needs only the independent review of this exact
recursion identification and the finite-cover residue argument.

## OPENS RAISED

None. No new canonical OPEN identifier or computation.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

The checker completed exit0. This concerns identifiers, not novelty.
Manual comparison: the original formal construction and all its finite
jets remain valid; its global algebraization was explicitly unproved.
The present log-residue obstruction decides that question for the exact
fixed recursion, not the unrestricted scalar-pair construction endpoint.
Existing sparse no-mate theorems and generic residue identities are not
being extended to arbitrary pairs. No exhaustive novelty claim.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8546`.
- Body SHA-256:
  `be9ded4fffaa8e7c9cfc65e5d3ea94af5c03aee807dcec9bc8d03d61b075e1ae`.
- Frozen basis: `dd0f956fc282d398c1779567543e8bda956b0c01`.
