# F10 r2: a conditional faithful fifth-root/cubic scale cover

2026-09-10. NEW MANUAL RESULT, UNREVIEWED; application CONDITIONAL on the provisional transfer report pinned in PINS.json. First action 08:53:02.730671475 UTC; controlling stop 09:09:02.730671475 UTC, publication reserve from 09:07:02.730671475 UTC. No scientific execution or source outcome.

## 1. Exact conditional statement

Assume precisely the parent’s normalized presentation and polynomial weights. Write its ring as

    A = B[s,s^-1,X1,X2,X3]/I19,  z=s²,

with the WHOLE coefficient algebra B; no embedding or field component is chosen. Let F_k denote the seventeen homogeneous rows

    Psihat5, Psihat6, Psihat7;
    K1_1,...,K1_6; K0_1,...,K0_8,

whose respective weights are 5,6,7; 13,12,11,10,9,8; and 15,14,13,12,11,10,9,8. Weights of X1,X2,X3,z are 1,2,3,5. The other two rows are

    K0_0(X,z)-s^7,  K1_0(X,z)-U(X,z)s^5,          (1)

where K0_0,K1_0,U have weights 16,14,3. Every polynomial here includes the parent’s complete particular forcing and all previous compatibility substitutions.

Use NEW coordinates Y1,Y2,Y3, distinct from the parent’s pre-normalization free coordinates. Put

    L0=K0_0(Y,1), L1=K1_0(Y,1), U0=U(Y,1),
    C = B[Y1,Y2,Y3,L0^-1]/
        (all seventeen F_k(Y,1), L1-U0 L0).       (2)

Then there is an explicit common algebra

    A[w]/(w^5-s) ≅ C[w]/(w^3-L0).                (3)

The left side is finite free faithfully flat of rank five over A; the right side is finite free faithfully flat of rank three over C. Consequently A is the zero ring if and only if C is the zero ring. This is NOT an isomorphism A≅C or a source operation s=1. No nonzero, finite-dimensional, reduced or proper full-source quotient is asserted.

The proof works over every commutative B-algebra, including ones with nilpotents. Only the application to the complete source uses the provisional parent; the following algebraic cover calculation is self-contained.

## 2. Every row and both inverse maps

Set D=A[w]/(w^5-s). Its A-module basis is 1,w,w²,w³,w⁴ by division by the monic polynomial. Moreover w is a unit, with inverse w⁴/s. Make the invertible Laurent polynomial coordinate change

    Xi=w^(2i) Yi,   Yi=w^(-2i) Xi,   s=w^5.

Thus z=w^10. A weight-k polynomial becomes w^(2k) times its value at (Y,1). Each of the seventeen rows therefore differs from its sliced row only by a unit. The first and second rows in (1) become respectively

    w^32(L0-w³),
    w^28(L1-w³ U0).                              (4)

Replace the second parenthesized row by L1-U0 L0: their difference is U0 times the first parenthesized row. This is an invertible triangular ideal-row operation, not deletion of a low equation. Because w is a unit, the first row makes L0=w³ a unit. Localizing L0 hence changes nothing. Conversely, in C[w]/(w³-L0), w^-1=w²/L0; the same operations read all nineteen parent rows back to zero.

Explicitly the forward map in (3) sends

    s ↦ w^5, s^-1 ↦ w^-5, Xi ↦ w^(2i)Yi, w ↦ w.

Its inverse sends

    Yi ↦ w^(-2i)Xi, L0^-1 ↦ w^-3, w ↦ w.

These maps fix B. Substitution verifies both composites on every generator. The low-row read-back is particularly literal:

    L1-w³U0 = (L1-U0L0)+U0(L0-w³).

No coefficient division or selected irreducible factor enters these identities. They remain true if a retained row is zero or dependent, or if L0 becomes nilpotent: in that last case its localization correctly collapses the corresponding quotient.

## 3. Faithfulness, guards and full-source reconstruction

On the right of (3), the basis is 1,w,w², and the inverse of w displayed above is already in that rank-three algebra. For either monic extension, tensoring any base module gives the direct sum of respectively five or three copies. It is therefore flat and faithful, not just surjective on certain field-valued points. In particular a nonzero base cannot become zero. The maps are also etale: their derivatives 5w⁴ and 3w² are units over the Q-algebra base. Etaleness is unnecessary for the zero-ring equivalence.

The sole new localization in (2) is L0. All original leading units of B remain the same units. Under reconstruction s=w⁵ is a unit, so every Laurent factor used by the parent is legitimate. In particular the parent’s actual source guard reads

    omega = W*t5*s^8 = W*t5*w^40,

with W and t5 the parent’s fixed B-units. The parent’s inverse band maps, full Euler mate, inverse-polynomiality conditions and fixed gauges are then applied unchanged. All eliminated original rows retain their stated read-back; (4) additionally checks BOTH low rows. Nothing is inferred from a receiver-only or leading-only point.

For a field-valued C-point one may pass to an extension of degree at most three by choosing a root of w³=L0, then set s=w⁵ and Xi=w^(2i)Yi. In the other direction an A-point admits the construction after a field extension of degree at most five. These descriptions do not assume the original field contains those roots. The ring proof (3), rather than pointwise selection, is the statement that preserves arbitrary base change and nilpotents. It constructs no point.

## 4. Exact finite envelopes and the decision interface

For k≥0 define the explicit finite exponent set

    M_k={ (a1,a2,a3) in N³ :
           a1+2a2+3a3≤k,
           k-a1-2a2-3a3 is a nonnegative multiple of 5 }.

Slicing a homogeneous weight-k polynomial at z=1 gives support within M_k and ordinary Y-degree at most k. For each exponent triple the former z exponent is uniquely (k-a1-2a2-3a3)/5. Thus this slice does not merge distinct monomial slots of one homogeneous row.

The seventeen degree bounds are exactly the listed weights in section 1. The eighteenth row has support within M_19, not merely M_14: it is the slice of

    z*K1_0-U*K0_0,

which is homogeneous of weight 19. Its ordinary degree bound is consequently 19. The guard L0 has support M_16 and degree bound 16. These are justified upper bounds, not assertions of attained degree, nonzero coefficients, independent rows or dimension. The finite inventory is the sum of the seventeen corresponding |M_k|, plus |M_19|, with |M_16| for the guard. Each slot has seven rational coordinates in the complete B-basis; no coefficients or counts have been evaluated.

A denominator-cleared presentation over B uses four variables Y1,Y2,Y3,J and the eighteen rows in (2) plus J*L0-1; the latter has total degree at most 17. If B=Q[Z]/P7 as in the parent, reduce every B coefficient to Z-degree at most six and add P7(Z). This gives five variables and twenty relation slots. A sliced weight-k row has total degree at most k+6 over Q; the mixed low row is at most 25, the guard row at most 23, and P7 has degree seven.

Compared with the parent’s six-variable, twenty-one-slot polynomial presentation, this removes one variable and one slot through faithful monic covers. It does not prove that the total coefficient count, coefficient height or computational cost decreases: the combined low row has the larger degree bound 19. The concrete decision quantity is whether (2), with ALL eighteen rows and L0 inverted, is zero. No solver or certificate is generated, and no computation is authorized.

## 5. No further scale or source-coordinate shortcut

Nothing charged licenses removing Y1. The z=1 notation is a coordinate calculation AFTER adjoining w, not a source specialization. Ordinary weighted rescaling of Y alone does not generally preserve the sliced equations: monomials within one row have Y-weights differing by multiples of five. Only a finite fifth-root-of-unity scaling is automatic from that grading. It supplies neither a free continuous normalization nor a proof that Y1 is a unit. Likewise translating S changes the fixed coefficient Ahat3=S; a compensating exact source symmetry would need an additional proof. No such symmetry is claimed here.

## 6. Changed-object controls and stop

These are abstract algebra controls, not full-source points or numerical samples.

1. Without the L0 localization, the closed stratum L0=0 is retained. Its proposed lift would require a unit w with w³=0, impossible in a nonzero ring. The guard is essential.
2. Setting w=1 replaces w³=L0 by L0=1. For the abstract unit parameter T, the algebra Q[T,T^-1,w]/(w³-T) has T unconstrained; imposing w=1 discards it. No parent relation licenses that specialization.
3. Dropping the second low row leaves the independent residual L1-U0L0. Formally take L0 an invertible parameter, U0=0 and L1 an independent variable: the first low equation does not kill L1. This tests row retention, not existence in the actual source system.
4. The quotient Q[epsilon]/(epsilon²)→Q has the same field-valued points but kills epsilon and is not faithfully flat. Pointwise root-taking alone cannot replace the two explicit monic bases used in (3).

Verdict: the proposed fifth-root/cubic common cover and three-variable localized eighteen-row decision interface are proved CONDITIONALLY on the exact provisional parent. No whole-source exclusion, point, unit certificate, runtime claim or additional symmetry follows. Parent refutation or narrowing requires quarantine or corresponding narrowing of this application.

## OPEN(S) RAISED

None new. Remaining quantity: C=0 for the exact eighteen rows with L0 inverted. The cheapest prerequisite is a complete-B documentary/algebraic read-back of the finite parent reconstruction and these explicit monic maps; actual coefficients, certificate, cost and outcome remain unknown. No follow-on or execution authority is issued.

## COLLISIONS

status: EMPTY

Owned targets were absent before the lease. Only owned documentary files and the existing publication metadata are written; no shared or frozen scientific file is modified.

Own WHOLE proof, input/read-scope and raised-OPEN review completed before the marker; the precise Q-algebra wording was checked on final reread. All three scientific/documentary input hashes remain unchanged. No mathematical subprocess or additional research task was started.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10105`.
- Body SHA-256:
  `d47d7efdf4335e8812c8b99cf5ef38dd67cb2bba65a27e4071fc7e722fc7828d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
