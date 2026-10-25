# EULERREVIEW2335 — independent hostile review of the global sheet budget

Status: PASS_CONDITIONAL / INTERNAL / MANUAL / independently reviewed.
Launch/report basis: 0f332e6ea7c653c65cb35b17468511d50e565c52.
Selection basis: fc76778e4af1f71d098de5ca4cebc1414c85413c.

## Scope and conclusion

Under the adopted ACTUAL divisorial package, let X=W\C and let the finite map
h:X->A2 have degree e. Its restriction to U=A2 is etale. Write the omitted curves as
E_i^o=E_i\C≅A1, let r_i be transverse ramification, and let delta_i be the degree onto
the normalization of the polynomial image. Then

    sum_i r_i delta_i <= e-1.                                      (SB)

The proof below handles all omitted curves simultaneously, including distinct images.
It does not sum incompatible per-image degree budgets or assume an unramified affine
sheet. It uses the actual finite whole-source map. The tensor/sheet inequality in the
published logarithmic-defect report remains unproved and outside this review.

## Disjoint omitted curves and Euler characteristic

Curves over different k-centres are disjoint. Over one centre, every compact E_i≅P1
meets C at the unique point of C above that centre, so any two already meet each other
at that point. If they also met away from C, their reduced union would have intersection
scheme of length at least two and hence H1(O)>0. The reduced exceptional fibre has H1(O)=0 by the admitted
rational-singularity resolution premise. Hence the E_i^o are pairwise disjoint.

Therefore X is the constructible disjoint union of U and s copies of A1, so

    chi_c(X)=1+s.                                                   (1)

No assertion that W\C equals U is made; X contains the omitted curves.

## Flatness and the local multiplicity inequality

X is normal of dimension two, hence Cohen--Macaulay. A finite dominant map from X to
smooth A2 has equal-dimensional local rings; miracle flatness makes h finite flat of
rank e. For x over y define

    m_x=length_C(O_{X,x}/m_y O_{X,x}).

Thus sum_{x over y}m_x=e. The function m_x is constructible (finite coherent fibre
length on a finite morphism), equals one on U, and generically equals r_i on E_i^o.

Fix x in E_i^o. Let t_x be the local degree at x of E_i^o->normalization(D_i^o).
Take a sufficiently small analytic disc T in that normalized image branch through y,
and base-change the finite flat map along T->A2. Its direct image is locally free of
rank e over T. Shrink source neighborhoods so the finitely many points over y are
separated. The summand supported near x has constant fibre length m_x by conservation
of length. For a general point of T, exactly t_x points of E_i^o in this neighborhood
specialize to x; at each, the scheme-theoretic inverse image of the image branch has
generic multiplicity r_i. Other components or branches contribute nonnegative length.
Consequently

    m_x >= r_i t_x.                                                 (2)

This argument takes place after finite base change and separation of the actual finite
source germs. It neither requires X smooth at x nor identifies different image branches.
At a multibranch image point, selecting one normalized branch gives the same lower bound;
all other branch contributions remain on the nonnegative side.

## Euler integration

For a finite flat map, constructible Euler integration and the fibre-length identity give

    integral_X m_x dchi_c = integral_A2 sum_{x over y}m_x dchi_c = e.

Together with (1), and stratifying each E_i^o by its generic value r_i,

    e-(1+s) = integral_X(m_x-1)dchi_c
            = sum_i[(r_i-1)+sum_{x in E_i^o}(m_x-r_i)].

Only finitely many correction terms are nonzero. Cancelling s yields the exact identity

    e-1 = sum_i r_i + sum_i sum_x(m_x-r_i).                         (3)

This is the whole-source identity; no target-image labels are combined.

The compactification of E_i^o->normalization(D_i^o) is a map P1->P1 whose unique point
over target infinity is source infinity. Hence the affine normalization is A1 and the
map is polynomial of degree delta_i. Riemann--Hurwitz, or the derivative divisor of a
polynomial, gives

    sum_{x in E_i^o}(t_x-1)=delta_i-1.                              (4)

From (2), m_x-r_i >= r_i(t_x-1). Summing (4) in (3) proves (SB).

## Verdict and limitations

PASS_CONDITIONAL for (SB) at the exact adopted actual-divisorial, finite-normalization
scope. The decisive local inequality is a conservation-of-length statement for the
finite flat base change, so singular source points and coincident image branches do not
invalidate it. This review makes no novelty claim.

The reviewed public identity

    sum_i r_i + sum_alpha m_alpha + Theta + Delta.c1(V)=2(e-1)

is only a consumer. Even with (SB), contradiction still requires the separately displayed
UNPROVED tensor/sheet inequality. Neither that inequality, an infinitely-singular transfer,
JC2, a low-degree campaign, nor an automatic successor is certified here.

## Coverage and custody

ACK was measured 2026-10-25T23:33:18.873189Z. All 39 fixed inputs passed regular-file,
path, mode, byte, LF, and SHA-256 gates. Frozen STATE327 was read whole by
2026-10-25T23:33:28.729816Z and equals launch STATE byte-for-byte. Whole reads: task9,
proposal14, and frozen STATE327 (separate). Selected reads: EULER1755 terminal64--87
(24 LF) and published logarithmic-defect61--73 (13 LF). Accepted public foundations were
used only at their pinned scopes; own earlier whole coverage was reused after fresh hashes.

The canonical capability was persisted mode0600 and file/directory-fsynced before body
creation; the allocated body was inspected empty. A substantive partial was saved before
extended synthesis. No new source, history query, CAS, paid/cloud lane, child, Git/public/
shared/protected edit, low-degree search, or successor occurred. Final postpins, selection-basis
archive comparisons, four public-blob comparisons, exact read charge, and collision custody
are in the companion receipts.

OPEN(S) RAISED
None.

## COLLISIONS
Terminal frozen-public collision custody is recorded separately after sealing.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6138`.
- Body SHA-256:
  `1c32e63409bc97329da9c45553cda77dc06ea82516b97750a5ee245dc987d131`.
- Frozen basis: `0f332e6ea7c653c65cb35b17468511d50e565c52`.
