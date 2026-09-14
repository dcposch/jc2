# Fixed constant graph: the specified collision residue

Manual producer-level co-research, not promotion. First actual action2026-09-12 10:59:42 UTC. Original reserve11:20/HARD11:23 unchanged. TASK and three input pins matched before charged reads; own destinations absent. No scientific execution or external input.

## Quantity

Verify ROOT's raw collision correspondence and compute only the normalized residue above a=b, 8b²+8b+1=0. The original constant-graph primitive question is addressed only if the correspondence and full residue calculation attach exactly.

## Result

**NONZERO.** At either specified quadratic point B=b0, the full base residue is

    Res eta = −(8B+5)/6,       8B²+8B+1=0.

The actual collision cover is ramified there with index2, so its residue is −(8B+5)/3, also nonzero. This excludes ALL target-polynomial area primitives for the literal H=1 subalgebra and consequently every pair in that subalgebra with nonzero constant Jacobian. This is a new manual producer result requiring independent FIRST, not a global JC2 conclusion. ROOT supplied the unreviewed candidate; the collision algebra, full cancellation and obstruction are derived below.

## 1. Attach the actual two source maps

Use only the supplied literal chart x=1/t,y=s−t and

    U=s²+st−Ws³, V=4s+2t−3Ws²,
    z=5t²−3st−Wt³.

Equal target triples at s,s' imply roots of Ws³−2s²+Vs−2U. With sigma=s+s', delta=s−s', subtraction gives

    V=2sigma−W(sigma²−ss').

Therefore, defining a=3W sigma/4−1,b=W delta/4,

    t=delta(a+b), t'=−delta(a−b),
    C=(a+1)/(3b), s=delta(C+1)/2, s'=delta(C−1)/2.

For example 2t=3Ws²−4s+V and factoring s−s' gives the displayed t; the primed formula follows with the opposite difference. Conversely these definitions and that V make the two cubic values equal, so U=(Ws³−2s²+Vs)/2 is common and equals the chart U on both branches. Thus equality of the triple is literal, not inferred from a numerical profile.

Set u=a−b,v=a+b,W=4b/delta. Direct substitution of t=delta v,t'=−delta u gives

    (z−z')/delta² = E/b,
    (z+z')/delta² = K,

where the independently expanded polynomials are

    E=−a²−a+20ab²−3b²−8a³b²−24ab⁴,
    K=(10−24b²)a²−4a−1+10b²−8b⁴.

Indeed the difference before substituting C is 20ab−3aC−3b−8a³b−24ab³; the sum is 10(a²+b²)−3(bC+a)−24a²b²−8b⁴. Hence E=0 and delta²=2/K give z=z'=1. Where b,K,u,v are nonzero, both x,y maps are defined and distinct, since s−s'=delta≠0. These conditions hold generically on the branch used below.

## 2. The one-form, with the correct cover

The source primitive alpha0=x dy=(ds−dt)/t has derivative dx wedge dy. Subtract its pullbacks on the two maps. The coefficients of dC and dlog delta are respectively a/(uv) and (aC−b)/(uv), and the remaining term is −dlog(v/u). Since delta²=2/K, the difference is precisely

    eta = a/(uv) dC −(aC−b)/(2uv) dlog K −dlog(v/u).

This identity is on E=0 and uses its differential, not independent da,db. It descends to the base curve, although the source maps require adjoining delta. No optional symmetric-primitive formula is needed.

Let B satisfy Q(B)=8B²+8B+1=0. Substituting a=b yields

    E(b,b)=−b(2b−1)²Q(b),
    E_a(B,B)=−14B²,
    (E_a+E_b)(B,B)=52B+9.

The last quantity is nonzero: its quadratic norm is −49. Thus E is smooth there and u=a−b is a local parameter, with

    b=B+d u+O(u²),   d=14B²/(52B+9)=(20B+9)/28.

The simplification follows by multiplying out and using B²=−B−1/8. In particular this is an actual normalized branch, not a singular point with an assumed parameter.

The decisive useful exact identity, valid after a=b+u, is

    E=bK+(2b−1)u−(10b+1)u²−8b²u³.

Consequently on E=0,

    K=(1/b−2)u+(10+1/b)u²+8b u³,
    K=k1 u+k2 u²+O(u³),
    k1=1/B−2,  k2=10+1/B−d/B².

Here B≠0,1/2, so K has a SIMPLE zero. Choose the unique irreducible component through this smooth point and its normalized projective completion. The odd valuation of2/K makes adjoining delta a genuine quadratic function-field extension, with ramification index2 at this place. This also establishes a genuine nonempty open with the required maps: none of b,u,v,K vanish identically on this smooth branch. No other pole or component was scanned.

## 3. Full Laurent cancellation

Write C=C0+C1u+O(u²), with

    C0=(B+1)/(3B), C1=(B−d)/(3B²), v0=2B.

Since aC−b=[v(C−1)+u(C+1)]/2, put

    M=(aC−b)/(2v)=(C−1)/4+u(C+1)/(4v).

Then eta=(a/v)C' du/u−M(K'/K)du/u−dv/v+du/u. Here
K'/K=1/u+k2/k1+O(u), a/v has constant1/2, and
M0=(C0−1)/4, M1=C1/4+(C0+1)/(8B). Thus EVERY possible simple-pole contribution is

    Res eta=1+C1/4−(C0+1)/(8B)−(C0−1)k2/(4k1)
           =1−(2B+2d+1)/(24B²)
                −(10B²+B−d)/(12B²)
           =(4B²−4B−1)/(24B²)
           =−(8B+5)/6.

In the second line (1−2B)/B=k1 cancels exactly; the d contributions then cancel. The last equality has the literal check

    6 Res eta+(8B+5)=(4B−1)Q(B)/(4B²)=0.

The apparent double pole contributes through k2/k1 and M1; omitting it would be wrong. In particular the explicit −dlog(v/u) alone gives +1, NOT the answer. The norm of 8B+5 is −7, so neither conjugate residue vanishes. Pullback to the normalized delta cover multiplies residues by2, giving the stated nonzero values there. Sign of the square root does not alter eta.

## 4. Global exactness obstruction and limits

Suppose alpha=A(U,V,W)dU+B0(U,V,W)dV+C0(U,V,W)dW is polynomial and its graph pullback has derivative dx wedge dy. Then phi*alpha−alpha0 is a closed polynomial one-form on A2, hence dH for a POLYNOMIAL H(x,y). This polynomial Poincare assertion follows directly by ordinary homogeneous radial contraction, with division only by positive integer degrees.

On the collision cover the two target maps are identical, so the alpha pullbacks cancel. Therefore eta=d(H_second−H_first), a differential of a rational function on that cover. A rational differential of this form has zero residue at every normalized projective place: differentiating a Laurent series cannot produce a nonzero coefficient of dw/w. This remains true when the source chart has a pole there. The nonzero residue found above is a contradiction.

This is all-degree, not a bounded coefficient ansatz. If f,g belong to C[p,q,r] with J(f,g)=c≠0, the target-polynomial one-form representing f dg/c would give the forbidden primitive. Thus no such pair exists in this FIXED subalgebra. No assertion follows for other graph H, all target algebras, arbitrary plane maps or global JC2. No collision novelty, ambient nonclosure argument, local Darboux implication or source point is claimed. The norm and cover checks are meaningful controls against false cancellation and an incorrectly normalized place.

Quantity settled for this test: exact nonzero residue with source attachment. Cheapest test was this single manual Laurent calculation; the20-minute allocation is UNMEASURED planning, not a runtime claim. No further pole test, computation or successor is selected.

## Scope and closeout

TASK and ROOT-CANDIDATE freshly WHOLE after pins. Constant-graph Astra report reused from same-agent exact-pin WHOLE at10:38; COORDINATION from05:51–05:53. No other scientific source or linked input. Own complete readback, four postpins, quantity/control/scope/collision check before marker LAST. No new canonical OPEN, shared edit, runtime or successor authority.

## COLLISIONS

status: EMPTY

- Own-only scope/identifier check; this is the specified new residue, not a rebranded two-point collision. ROOT candidate is disclosed as the source of the proposal, not independent confirmation. Independent FIRST remains required before promotion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7838`.
- Body SHA-256:
  `0982587c63e90d18f67c161e8575c1a819d9466ad0280df80fb8a4a2af7aa103`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
