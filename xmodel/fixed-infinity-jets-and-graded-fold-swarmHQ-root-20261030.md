# Fixed infinity-Jacobian precision and a degree-two residue fold

Producer: swarmHQ ROOT. Date: 2026-10-30 UTC.
Basis: 397632cbdf8eaaac8c6f22db1c69921adc85f9e4.
Evidence: MANUAL, elementary algebra and divisorial-valuation calculations.
Lifecycle: UNPROMOTED. The original candidate received an independent **GAP** review concerning Poisson closure before grading. This corrected text incorporates the reviewer's requested distinction; independent final-text delta review has not been performed. The original GAP verdict is preserved.

## Statement and exact scope

For every fixed positive integer M there are global polynomial pairs whose Jacobian is1 modulo the M-th power of a chosen infinity uniformizer, with primitive source and target raw discrepancies -1, normal index1 and residue degree2.
Their full graded source is smooth, normal, finitely generated and symplectic, and the ambient graded bracket restricts to the full graded target with leading Jacobian1.
Thus these data alone do not exclude the fold when degree is allowed to grow. The pairs are NOT Keller maps. This makes no assertion about a degree-dependent certificate using all coefficients, exact global Jacobian, component nonsingularity, or full filtered Poisson compatibility.

## Explicit pairs and valuations

Put z=xy^3-1 and, for n>=1, set

    P=xy,
    Q_n=(1/2) sum_{k=1}^n (-1)^(k+1) z^k/k.

For {f,g}=f_x g_y-f_y g_x, direct differentiation and the finite geometric series give

    {P,z}=2(1+z),
    {P,Q_n}=(1+z) sum_{j=0}^{n-1}(-z)^j=1-(-z)^n.

This is nonconstant for every n. In rational source coordinates u=y and t=z/y,

    x=(1+ut)/u^3,  y=u,
    dx wedge dy=-u^(-2) du wedge dt,
    P=u^(-2)(1+ut),  Q_n=ut/2+O(u^2).

The u-adic valuation is primitive and lies at infinity because v(y)=1 and v(x)=-3. Its raw discrepancy, defined as the order of the volume form plus one, is -1.
On the target use full rational field generators a=Q and b=P Q^2, with inverse P=b/a^2 and Q=a. Then

    dP wedge dQ=-a^(-2) da wedge db,
    a=u(t/2+O(u)),  b=t^2/4+O(u).

The restricted target valuation is primitive, has raw discrepancy -1 and normal index e=1. Its residue field C(t^2/4) has degree2 in C(t). The leading normal coefficient t/2 equals the derivative of the residue map t^2/4.
These assertions concern generic points of the divisors; they do not assert an everywhere regular map of the displayed charts.
Since {P,Q_n}-1=(-1)^(n+1)u^n t^n, any n>=M provides the claimed fixed-precision obstruction. Degree grows with n.
The formal limit Q_infinity=(1/2)log(1+z) has formal Jacobian1 but is not a polynomial component or a global map.

## Full graded rings and the necessary correction

Write r=in_v(u) and s=in_v(z), with degrees1 and1. Since x=(1+z)/u^3, every source polynomial has an initial form in C[r,r^(-1),s]. Conversely r, r^(-1) and s are the initials of y, xy^2 and xy^3-1. Hence

    gr_v C[x,y]=C[r,r^(-1),s].

This full ring is smooth, normal and finitely generated. The ambient graded bracket is {r,s}=-r^3, is nondegenerate because r is a unit, and has valuation-degree shift +1. Its inverse form is -r^(-3)dr wedge ds.
For A_n=C[P,Q_n], distinct monomials P^a Q_n^b have distinct initial Laurent monomials 2^(-b)r^(-2a)s^b. Consequently cancellation among equal-valuation terms produces no additional generators, and

    gr_v A_n=C[p,q],  p=r^(-2),  q=s/2.

The ambient graded bracket restricts to this embedded ring, where {p,q}=1. For n>=2, this is NOT the associated graded of a source-induced Poisson bracket on A_n: A_n is not Poisson-closed before grading.
Indeed P,z are algebraically independent, so A_n intersect C[z]=C[Q_n(z)]. If J_n=1-(-z)^n belonged to A_n, equal z-degrees would force J_n=c Q_n+d with c nonzero. For n>=2 the linear coefficient of J_n is zero and that of Q_n is1/2, a contradiction. For n=1 only, J_1=1+2Q_1 belongs to A_1.
This distinction is essential: an actual Keller target algebra is Poisson-closed before grading because {P,Q}=1.
The controls also fail component nonsingularity: dP vanishes at the origin and dQ_n vanishes along y=0. Neither filtered Poisson closure nor these global nonsingularity conditions is included among the data refuted above.

## Evidence and limitations

The [original qualified note](../box/fixed-infinity-jets-swarmHQ-20261030/initial-qualified-handoff.md) is retained byte-for-byte. The [first independent hostile review](infinity-jet-graded-obstruction-review-sol56-20261030T1300Z.md) verified the formulas, valuations and full graded rings but returned GAP on the ambiguous phrase induced bracket. Its exact correction is incorporated here without changing its verdict. [Custody and review scope](../box/fixed-infinity-jets-swarmHQ-20261030/README.md).
This is the same one construction, not a degree census or new control-family program. It supplies no actual Keller counterexample, polynomial no-fold theorem, source-scope promotion, or JC2 conclusion. The whole-polynomial compatibility gap remains open.

## OPENS RAISED

None. No new computation, source audit or successor is launched by this report.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `397632cbdf8eaaac8c6f22db1c69921adc85f9e4` (Git blobs only).

No novelty claim is made.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5313`.
- Body SHA-256:
  `22fc58dbd0b058aab2ba8bbcde877a1edf7f666550201505c3be16f946fad0bf`.
- Frozen basis: `397632cbdf8eaaac8c6f22db1c69921adc85f9e4`.
