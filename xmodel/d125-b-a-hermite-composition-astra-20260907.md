# D125: B reconstruction after the 27 A-Hermite pivots

2026-09-07; optional DESK composition, PRODUCER-CHECKED, not production authority. Both gates and producers in `box/d125-b-a-hermite-composition-20260907/inputs.json` were read wholly and hash-matched; B uses repaired exact witness `07b4ce88…`, not its refuted original serialization.

**Claim.** For each reviewed full-face receiver contract over K=Q or Q[rho]/(rho²−3rho+1), including both lambdas, the complete quotient is a polynomial extension in one gauge scalar of a quotient presented with **49/57/78 coordinates** (unequal/common3/common4). These are generator counts, not dimensions. No localization or field extension is added; both golden embeddings remain. The remaining ideal is not constructed or claimed proper.

**Base change.** Let S=K[lambda2,lambda3,free A,c,z], omitting c,z in the unequal case, where c is the prescribed nonzero field constant. Let I_A be all 30 A-negative lift rows. The reviewed 27 unimodular graphs, with the other three rows identically zero, give S/I_A=R, a polynomial ring on 44/50/71 retained A coordinates and the indicated parameters. They leave A15=H³, the full inner face and A0=0 unchanged. The reviewed B descent solves 192/210/265 B coordinates by selected Jacobian rows at degrees14–37, leaving beta_r=[pi^(5r)]B, r=1,2,3,4. Every pivot divisor is a fixed unit of K. Consequently the graph quotient S[free B]/I_piv is S[beta_1,...,beta_4]. Base-changing this explicit isomorphism along S→R gives R[free B]/(I_piv|_R)=R[beta_1,...,beta_4], even for nonreduced further quotients. This uses split constant-matrix graphs, not a domain-only kernel argument or flatness assumption. Every unselected equation is carried through both substitutions.

**Gauge overlap.** Put s=beta_3 and a_d=[pi^d]A in R. The whole shear B'=B−sA acts on the four coordinates by

    beta'_1=beta_1−s*a_5, beta'_2=beta_2−s*a_10,
    beta'_3=0, beta'_4=beta_4.

Although a_5,a_10 are themselves Hermite graph values, they belong to the base R; the inverse adds s*a_5,s*a_10 and restores beta_3=s. No A coordinate changes. The entire A polygon lies inside B's, strictly below its fixed inner face (weights3<5 or9<15); degree15<25 and A0=0 preserve all B faces, prescribed zero slots, monicity, origin and c. Since [A,B−sA]=[A,B] identically, selected pivot equations are invariant. Uniqueness of their polynomial reconstruction implies the same shear identity for the reconstructed B over R, without imposing high compatibility rows. Thus this is not deletion of sH³ alone, nor an assumption that the lower kernel coordinates stay fixed.

For the lift homomorphism phi, phi(B')=phi(B)−s phi(A). Every A-negative slot lies in the 75-slot B envelope, so modulo I_A each B-negative row is individually invariant. All Jacobian residuals and the guard are invariant too. Hence, if T is the gauge-slice quotient retaining the equations below, the original complete quotient is **T[s]**, not T itself. The slice and original therefore have same-field nonemptiness equivalence; properness of their defining ideals is equivalent, not asserted. A useful exact negative control is P=t v^−1,Q=0,s=1: the B-negative ideal changes from (0) to (t) unless the A-negative equation t=0 is retained. Our composition imposes that equation first.

**Nothing dropped.** Retain all Jacobian degrees0–13 (105 slots, including degree13 and [gamma²] target c), all unselected degrees14–37 (444/426/371 slots), and all 75 B-negative lift rows after substitution; degree38 and the five top B-negative rows may remain explicit zeros. Retain zc−1 in common cases. Counts are (44,50,71)+3 B coordinates+2 lambdas+(0,2,2)=(49,57,78). The 70 B-Hermite pivots and optional two-lambda pivots are **not** subtracted. Expanded residuals, fill, arithmetic degree and solver cost are unmeasured; no performance, dimension, point, properness, source-necessity or JC2 claim follows. No baseline dependency, builder change or follow-on computation is authorized. All writers idle at custody handoff.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4088`.
- Body SHA-256:
  `e59664cbce59ea0ebb9177fb3a23ee108464b8ee818070b605e541fcac3ef44c`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
