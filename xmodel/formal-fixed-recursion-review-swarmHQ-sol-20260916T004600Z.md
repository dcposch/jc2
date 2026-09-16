# Different-model review: fixed formal recursion is non-algebraic

Reviewer: swarmHQ gpt-5.6-sol, native task formal_pair_sol_review.
Recorder: ROOT, from the complete terminal review message; mathematical
derivations and qualifications are transcribed below, not a verbatim log.
Evidence: MANUAL hostile proof review. Verdict: CONFIRMED on items A-E.
Completed: 2026-09-16T00:45:53Z.
Frozen reviewed commit: 4dec780b0656c6d62ee7298b1bed55626c356b64.

## Custody and read scope

Sol verified the frozen commit before and after review, with no change;
the finalizer returned VERIFIED and report/manifest modes were0444.
Both the charged proof and manifest, and both comparison reports, were
read whole. The designated HQ/public policies and guardrail were read.
No files were edited; no mathematical subprocess, CAS, Python mathematics,
network, AWS, descendants or protected-repository probes were used.

Pre/post hashes, all unchanged:

- [Charged report](formal-fixed-recursion-nonalgebraicity-swarmHQ-root-20260916T004300Z.md):
  73c182f4531e635b5da3e9238df042afbb745b98d8e03fb37f30b997101d7488.
- Its artifact manifest:
  29869b9fcc7ebeb131054215722655173c717e0a7ea72256d5f4046756f0a409.
- Embedded producer basis: dd0f956fc282d398c1779567543e8bda956b0c01.
- FALLACY-v2.md:
  e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.
- [Source blind](ideation-20260911T1100Z-astra-source.md):
  72e901ea33e07a5f6ad2f918da4c7674dc6f84e6f366f6b03d3a974d8bd4df8e.
- [Source cross](ideation-20260911T1100Z-cross-astra-source.md):
  fa57c775349f3977fed7383e20a100876c9ff5e4b720e8b0ef1723dd70100a7a.

The source and cross contain exactly the retained recursion under review:
surface U^2=A+A^2Z, boundary pair(z^2,z^3-z), initial direction(-1,-3z/2),
and correction -e_n(z)/(2(n+1))*(-1,-3z/2)*u^(n+1).

## A. Fixed direction and determinant — CONFIRMED

The initial u-term and every later correction lie in the same z-dependent
direction, so the pair is exactly

    H=z^2-F,       G=z^3-z-(3z/2)*F,       F=u+O(u^2).

Keeping all z-derivatives,

    H_u=-F_u,                    H_z=2z-F_z,
    G_u=-(3z/2)*F_u,             G_z=3z^2-1-(3/2)F-(3z/2)F_z.

It follows that

    H_u G_z-H_z G_u=F_u*(1+3F/2).

Both the 3z^2 terms and the zF_z terms cancel. The report does not
mistakenly treat the direction as constant in z. With D=1+2zA, the
surface equation gives D^2=1+4zu^2 and D(0,z)=1. The surface bracket
is2D times that determinant, so constant bracket2 is equivalent to

    (1+3F/2)*F_u=D^(-1).

## B. ODE, recursion identification and uniqueness — CONFIRMED

Integration gives

    partial_u(F+3F^2/4)=(1+4zu^2)^(-1/2).

The unique zero-constant-term primitive is

    I=integral_0^u (1+4zv^2)^(-1/2) dv
     =sum_(j>=0) (-1)^j*binom(2j,j)*z^j*u^(2j+1)/(2j+1).

Consequently I=F+3F^2/4 and F=(2/3)*(sqrt(1+3I)-1), with square-root
constant term1. This proves formal existence and uniqueness.

It identifies the source recursion, not merely another solution. An error
e_n*u^n in the full bracket produces the prescribed change

    F -> F-e_n*u^(n+1)/(2(n+1)).

Its derivative changes the determinant at degree n by -e_n*u^n/2.
Multiplication by2D, where D=1+O(u^2), changes the full bracket by exactly
-e_n*u^n at that degree. Contributions involving the pre-existing F,
the correction itself or D-1 occur later. Thus the algorithm converges
coefficientwise to the unique solution above.

## C. Algebraic-primitive obstruction — CONFIRMED

Work over k=C(z), introduce D^2=1+4zu^2, and extend constants by s^2=z.
The parametrization

    u=t/(s*(1-t^2)),       D=(1+t^2)/(1-t^2)

satisfies the conic equation and gives

    omega=du/D=dt/(s*(1-t^2)).

Its residues at t=1 and t=-1 are -1/(2s) and 1/(2s), both nonzero.
If I were algebraic over k(u), take the smooth projective normalization
of a finite extension containing I,D,s and, if desired, enlarge constants
algebraically. Characteristic-zero derivations extend uniquely, so the
formal identity dI=omega is an identity of differentials on the relevant
component.

At a point over t=1 with ramification index e, the pullback residue is
-e/(2s), nonzero. But the differential of a rational function has zero
residue, since differentiating a Laurent series cannot create a dw/w
term. Contradiction. This survives arbitrary finite covers and algebraic
constant extensions. Thus I is transcendental over C(z)(u). Since
algebraicity of F implies algebraicity of I=F+3F^2/4, F is transcendental.

## D. Transfer to S, H and G — CONFIRMED

C(S)=C(A,U,Z), with U^2=A+A^2Z, is algebraic over C(u,z)=C(U,Z).
In the generic field z is nonzero and

    F=z^2-H,
    F=-2/(3z)*(G-(z^3-z)).

Algebraicity of either H or G would imply algebraicity of F. Both are
transcendental over C(u,z), and therefore cannot belong to C(S) or any
finite algebraic extension of C(S). This rules out realization of these
exact completed series as regular functions on S, on a Zariski-open
neighborhood of the completed line, or as rational functions after a
finite algebraic cover.

Binding qualification: this concerns the specified embeddings/expansions
of these formal series. It does not say that unrelated functions on
finite covers cannot have similar finite jets.

## E. Specialization, finite jets and global scope — CONFIRMED

At z=0, I=u and F=(2/3)*(sqrt(1+3u)-1), so the specialization is
algebraic. This does not contradict generic transcendence over C(z)(u).
Algebraic behavior on a special fiber does not make the generic element
algebraic.

Every finite u-truncation has coefficients in C[z] and is represented
by an element of the original surface ring to that order. The obstruction
is all-order, arising from nonzero residues of the generic primitive,
not a failed finite-jet equation. The prior finite-jet construction stays
intact.

The result excludes only the exact fixed-direction correction algorithm.
It does NOT exclude other correction directions, other formal pairs with
the same boundary values, arbitrary regular scalar-bracket pairs on S,
algebraization under additional different global data, or any other
construction/proof resolving JC2. Overall verdict CONFIRMED at the
expressly narrow fixed-recursion scope.

## ROOT intake and next test

ROOT collected the whole final response and observed authoritative
COMPLETED status before publishing this record. Independent manual
reconstruction agrees with A-E, including both stated qualifications.
No scientific computation is represented as having been independently
executed. Review establishes only the named fixed-recursion theorem.
No coefficient extension, new correction direction or dependent research
is selected. The source-surface construction frontier remains open.

## OPENS RAISED

None. The charged review is complete; no new computational quantity.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Checker exit0. Identifier emptiness is not a novelty certification.
Manual scope comparison is the full A-E review above. No global JC2
conclusion, new source family or strengthened finite-jet claim follows.
ROOT rechecked all five listed file pins before sealing; unchanged.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7198`.
- Body SHA-256:
  `bdd7de552902ed6db6cc27c76997004fc0a4c54d3637c25d04ccd55cccc8e5ad`.
- Frozen basis: `4dec780b0656c6d62ee7298b1bed55626c356b64`.
