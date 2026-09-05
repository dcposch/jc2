**The (99,66) split branches on a chart rebuilt from the printed source**

Lane `g9966-corrected-engine-astra-20260905`; frozen basis `ec612a7dda0fa3eedea1324560dafaf127b6af96`.

**COMPUTE-BOUND on both branches:** delta2 at deep Jacobian power71; delta52 at power97. Both finite schedules and all minor pole rows completed. No corrected full-chart unit or full-chart survivor point was established; neither historical kill receives PROVED-HERE.

**Custody and scope.** Before mathematical use, I joined the receipt's indexed `_sha256` and `_basename` fields with `awk -F=`, prefixed `/tmp/jc2-lane.qdzvDy/inputs/`, and ran `sha256sum -c`. All seven frozen copies returned `OK`. The mechanically generated manifest and transcript are `box/g9966-corrected-20260905/inputs.sha256` and `hash-check.txt`. No mismatch occurred.

All drivers, audits, controls, snapshots and output are under `box/g9966-corrected-20260905/` (N below). No ledger was edited; no `jc2-lean` or `ideation-*` work was used. The repository was not assumed clean; only this lane's files are claimed. No exit price is asserted.

`N/moh-layout.txt` is a fresh layout extraction of the frozen Moh PDF. M below means physical lines of that extraction; printed pages were checked against retained page images. The full derivation audit is `N/print-audit-derivations.md`; executable arithmetic is `N/source_data.py` and `print-audit-source-data.json`. The input data are degree pair (99,66), characteristic entries M=(-66,77,97), V2=V3=8, and the stated minor radii/partitions. Faces, support exponents, cover exponents and remainder bounds are outputs of these formulas, not independent input tables.

**Objects, coordinates and radii.** Engine F of degree99 is Moh's g. Engine G of degree66 is Moh's partner f. The specialized first characteristic polynomial T1^psi agrees with that partner up to an additive scalar, which does not affect the negative-order systems used here. The degree33 and degree11 canonical auxiliary roots are h2 and h3; neither is silently identified with a characteristic T2 or T3. The characteristic gcd definition gives d=(99,33,11,1), hence the two root indices are3. Keller Lemma2.1, printed p151, gives e=98, so M2=77<e licenses Prop2.2. The characteristic recurrence gives q2=143, lambda2=-1815 and mu2=-55; the actual characteristic degrees99,66,55 have reduced ratio9:6:5. These are Moh printed p150, M:567–582, and Prop2.2(1), p152, M:680 onward.

Place the two directions at y=0 and y=x. The monic leading root polynomial is generated from cluster multiplicities as P0=y^3(y-x)^8, with F_top=P0^9, G_top=P0^6, h2_top=P0^3 and h3_top=P0. The source is Prop4.5, printed p169, M:1596–1599, and Prop4.6(1), p170, M:1632–1635, under the stated Ms=n-2 branch hypotheses. Set t=x^-1, w=ty, z=w-1, K3=t^11 h3 and K2=t^33 h2. Thus K3_top=z^8(1+z)^3 follows by substitution.

Def5.1(3), printed p179, M:2131–2138, gives the y-radii. The denominator in its product contains M_(j-1), not Mj-1. Direct substitution yields

```text
delta3 = 1-2 = -1,
delta2 = 1-22*5/165 = 1/3,
delta1 = 1-165*143*5/(1287*165) = 4/9.
```

Multiplication by t adds1 to root-difference valuations. The z-radii are therefore exactly4/3 and13/9. Clearing denominators gives `t=s^3,z=pi*s^4` and `t=e^9,z=alpha*e^12+Pi*e^13`. Every D2 weight is consequently W=3r+4q, and every D1 monomial exponent is9r+12q+k.

The major centre is not inferred from a denominator alone. Def5.1(1), M:2120–2124, puts72 of99 F-roots in D2. Every deck transformation preserves F and sends D2 to an equal-radius disc with72 roots. Such discs are equal or disjoint, and disjointness would require144 roots. Thus D2 and its unique strictly truncated centre are invariant. Prop1.2, printed p147, M:373–390, supplies the generic-disc/root interpretation and uniqueness. No nonintegral centre coefficient survives all deck transformations. Total degree equal to y-degree bounds root orders below by-1, leaving only the already placed leading term and an ordinary constant. One source translation removes that constant. The same argument inside a24-root alpha-packet makes the D1 centre lie in k((t^(1/3))); no exponent in that lattice lies strictly between1/3 and4/9.

**Complete systems and the source licence.** Def1.4, printed p148, M:445–461, requires disjoint discs covering all roots at equal generic valuation. Thm1.1, p149, M:478–483, requires divisibility of every multiplicity before transferring a system to an approximate root. Neither a total root count nor an exact valuation alone identifies a face.

At D2, `ord F=72/3-27=-3`. Complete this point by following the remaining minor rays to generic F order-3 and merging repeated discs. Along a ray the valuation is a continuous rational piecewise affine sum of distances with positive slope, so the required radius exists. The principal minor multiplicity3 is below d3/(n-M3)=11/2. Prop6.1(2), printed p191, M:2739–2762, therefore makes the added negative-order points distribution detectors for F,T1,T2. Its proof at M:2855–2874 also covers radii at least1. Def3.1(4), p161, M:1155–1172, and the9:6:5 degree ratio force every added F multiplicity divisible by9. The major72 is divisible by9 too. Apply Thm1.1 twice, with accuracies-1 for h2 and-1/3 for h3. This justifies the inner D2 remainder bounds.

For D1 use its three conjugate24-root children, completed by minor points at F accuracy-1/3. One cube-root transfer gives h2 multiplicity8 in each child. A second transfer is not licensed:8 is not divisible by3. The engine imposes the h2 D1 coefficient equations and does **not** impose invented C2/C3 D1 bounds.

At the minor endpoints F accuracies are-18 and-9/2. The target27-root minor disc and a72-root major disc of radius `(accuracy+27)/72` form a complete system. Those major radii are1/8 and5/16, both below1/3. To transfer the face rather than just its total multiplicity, refine the minor discs to a slightly larger common negative accuracy still below-3. Distribution forces each refined minor multiplicity divisible by9; the entire major packet remains intact. Two applications of Thm1.1 transfer the distinct residues to h2 and h3. Prop1.2 then reads the faces at the original splitting level. The same distributions make h2 a square quasi-approximate root of G: the major counts F72/G48 and the child counts F24/G16 transfer to h2 counts24 and8; each is half the corresponding G count. The completed minor points have the same3:2 ratio. Thus h2 has half G's multiplicity and generic accuracy at every point, as required by Def1.5, printed p149, M:488–493. These counts supply the source hypotheses for the G remainder equations.

**Faces are generated, and equality coefficients are kept.** Def5.1(4) and Prop4.6(1) give a monic degree24 cube-root face at D2 with an8-fold selected child. The cover acts by pi->omega*pi. Deck equivariance and degree24 force invariance, so the face is a polynomial in pi^3. A zero residue cannot have multiplicity8. Three nonzero conjugates with multiplicity8 exhaust its degree. The executable orbit product is

```text
Res_alpha(alpha^3-beta,pi-alpha) = pi^3-beta,
face_D2(K2) = (pi^3-beta)^8, beta != 0.
```

One uniform dilation permits beta=1 over the algebraic closure. Root distances give ord h2=-1 and ord h3=-1/3, hence normalized D2 floors96 and32. Enumeration of the entire degree11 lower coefficient triangle produces43 strict-below slots, two equality slots (4,5),(8,2), and21 strict-above slots. The equality face starts as

```text
H = pi^8+kappa*pi^5+ell*pi^2.
```

Thm1.2, printed p149, M:495–507, applied to `h2=h3^3+C2*h3+C3`, gives ord C2>=-2/3 and ord C3>=-1. Both remainders have y-degree below11. Their total-degree bounds are21 and32, by monic division and cancellation of the common degree33 top. Normalize by t22 and t33. The absent r=0 coefficients follow from these derived total-degree bounds21/32, not from a valuation cutoff. Their D2 floors64 and96 produce equality spaces

```text
U in span{pi^10,pi^7,pi^4,pi},
V in span{pi^9,pi^6,pi^3,1},
(pi^3-beta)^8 = H^3+U*H+V.
```

Since deg(UH)<=18 and deg V<=9, the pi21 coefficient gives `3*kappa=-8*beta`. This equation, with rational leader3, generates the corrected t4*z5 coefficient-8/3. It is not typed into the replacement as an unsupported face. Complete coefficient elimination leaves ell free; for example U10=20*beta^2/3-3*ell. `print-audit-face-control.py/.json` solves the remaining face identity and checks every coefficient exactly. Its old-face negative control has pi21 residual-8*beta. Neither ell nor the remaining U1 is divided out.

The minor face is also constructed as a product. The [2,1] datum, with the double residue carried by minor_a2, gives `P=zeta^2(zeta+3*rho)` after defining rho as a signed separation divided by3. The [1,1,1] denominator2 deck action gives `P=pi*(pi^2-c)` by eliminating the conjugate residue with a resultant. The refinements above generate K2_face=P^3, F_face=P^9 and G_face=P^6. Outside-packet leading constants are-1 to the even powers24,72,48; no unrecorded scalar is hidden in these faces.

**Full coefficients and explicit equations.** The new engine allocates the full coefficient boxes before solving any valuation equation. Distinct pi powers at a generic D2 point have independent coefficients. Thus a strict-below scalar coefficient is an actual zero equation with rational leader1; an equality coefficient remains a variable. All eliminated-coordinate lists, counts, row hashes and rechecks are serialized. There is no operation that turns a numerical floor into an exact monomial face.

For h3, strict-above coefficients use the old triangular basis z^v(1+z)^j, whose diagonal is1; equality coefficients use separate raw monomials. This preserves the meaning of Hc_11_0. The minor rows are freshly extracted from the full series and solved by rational pivots. Their18/20 pivots leave8/6 coordinates including all centres. A further unit triangular exchange keeps the equality coordinate E82=ell itself free in place of Hc_8_3. This reduces expression growth without selecting a locus. Both equality slots therefore remain represented; kappa is derived, ell is free until later equations solve it.

The C2 box has187 ambient coordinates and154 D2 zero equations, leaving33. The C3 box has308 coordinates and271 zero equations, leaving37. The K2 face gives seven further rational pivots. At D1, root distances give ord h2=-1/9, so `ord_e K2>=9*(33-1/9)=296`. Expansion at the child gives five equations at W97,k0..4 and two at W98,k0..1. These seven rows are solved, with no typed D1 face. Initial source inner dimensions are therefore `8+70-14=64` and `6+70-14=62`. An independent generic-before-minor calculation reproduces both counts and zero residual.

The inherited low-q K2 output coordinates did not imply these C2/C3 equations. A free t5*z21 perturbation divides by K3_top=z^8(1+z)^3 with quotient beginning at normalized C2 weight15, below64. Ordinary monic division is a valid coordinate operation; it does not confer the approximate-root bound. This is why adding the missing h3 face terms alone leaves a diagnostic enlargement. The replacement computes `K2=K3^3+(t22*C2)K3+t33*C3` directly from the explicit remainder coordinates.

Outer blocks are likewise explicit:

```text
F=h2^3+A2*h2+A3, G=h2^2+B1*h2+B2,
deg_y(A2,A3,B1,B2)<33.
```

The missing h2^2 term in F is the approximate-root definition, printed p148, M:463–468; it is not a source gauge. Monic division gives total-degree bounds65,98,32,65. If D is one of these bounds, the normalized block is t^D Q(t^-1,(z+1)/t), and its contribution to KF or KG has one additional t. Thm1.2 on the D2/D1 complete systems derives all twelve old constants:

| block | total-degree bound | D2 floor | D1 floor |
|---|---:|---:|---:|
| A2 |65|189|583|
| A3 |98|285|879|
| B1 |32|93|287|
| B2 |65|189|583|

For example the A2 floors are `3*(65-2)=189` and `9*(65-2/9)=583`. At D1 the row rule is `sum_(3r+4q=W) binom(q,k)c_(r,q)=0` when3W+k is below the derived threshold. It produces the finite offsets0..7. Exact pivot counts41,38,33,25,19,11,6,3 are reproduced as controls, not used as source data. All6600 ambient outer coordinates exist before5598 independent D2 equations; all eight D1 bands remove176 more, leaving826. The first41 D1 pivots also kill all outer D2 equality coordinates, in ranks11,11,8,11. Their possible face degrees are smaller than the total multiplicity demanded at the three child discs. Consequently the F/G D2 faces become K2_face^3 and K2_face^2 through emitted equations; they are not additional coefficient pins.

**Gauge ledger.** The ledger records group actions separately from equations and internal coordinate definitions.

| parameter/action | use in this chart |
|---|---|
| Source linear shear and relative scale | Place the two distinct directions at y=0,y=x; each is used once. Source translations remain available. |
| Two target scales | Make F,G monic; canonical h2,h3 monicity then follows internally. |
| Uniform source dilation with compensating target scales | Sends beta->beta*lambda^-4 and is used once to normalize beta=1. It does not also normalize rho, c or the Jacobian scalar. |
| First source translation combination B-A | Removes the major ordinary constant. |
| Residual diagonal source translation A=B | The generic engine carries jet0 freely. The accelerated strong run spends this second translation once, on jet0=0, through the complete invertible transport below. It is never spent on Hc_11_0. |
| Delta2 at-level double residue | minor_a2 is free and appears in y=jet0+u*t+(minor_a2+zeta)t^2. No division by u removes it. |
| Delta52 lower centres | jet0,u,v are free in y=jet0+u*t+v*t^2+pi*t^(5/2). The deck action determines the at-level odd cubic. |
| Hc_11_0 | Allocated freely on both branches, never gauged away. All other h3 terms have positive z-power, so h3(x,x)=Hc_11_0 and diagonal translation preserves it. |
| Approximate roots, triangular basis changes and rational pivots | Internal definitions or invertible coordinate operations; no group parameter is spent. |
| rho or c | Kept nonzero by a Rabinowitsch equation; set to1 only in explicitly tested rational points. |

There are two independent source translations after placing the directions, not one. For any degree-D coefficient polynomial, diagonal translation acts by the explicitly generated formula

```text
T_q K = sum_(r,p) c_(r,p) t^r z^p (1+q*t)^(D-r-p).
```

All exponents are nonnegative because the full polynomial degree triangle was allocated. This is a unit triangular polynomial map, with inverse T_(-q). Its centre action is jet0->jet0-q, u->u, and minor_a2 or v -> minor_a2 or v-q*u. The separation rho/c and Hc_11_0 are unchanged. Taking q=jet0 gives the full chart as the jet0=0 chart times an affine line. No division by u occurs, and no vanishing-leader branch is lost. The two disc radii, source degree boxes, canonical root identities, all translated remainder conditions and the full Jacobian equation are preserved by this automorphism.

N/translation-proof.md, N/translation-controls.json and N/minor_gauge-transport-controls.json check the inverse, tower and Jacobian covariance. N/minor_gauge-final-audit.md certifies coverage. A unit on this slice therefore transports to the full chart; its dimension is one less.

**Finite and deep row schedules.** Historical synchronization of D1 offsets, pole powers and Jacobian degrees is a driver convention. The finite run performs0..8 on both branches, including all stages of each historical endpoint schedule. Pole powers are4+s and8+s; prior bands and the named first Jacobian rows are retained. The normalized Jacobian is derived by direct differentiation:

```text
t^163 J = 99 KF KG_z-t KF_t KG_z-66 KF_z KG+t KF_z KG_t.
```

Its t-power r has global degree163-r. The deep schedule completes omitted top/low slots, then continues positive-degree bands until a unit or the cutoff. The constant is retained as a free nonzero Jc, with ZJ*Jc-1; no second dilation sets it to1.

Prop4.6's r=1 clause, printed p170, M:1646–1648, also requires the D1 differential face to be a nonzero scalar. Def5.1(4), and Prop5.3's tower extension on p180, carry this condition to the child. It is a necessary part of the requested chart. Let P(Pi),Q(Pi) be the actual F/G D1 faces computed from the surviving coefficients. With x=e^-9 and y=e^-9+e^3+Pi*e^4, the coordinate determinant is-9e^-6. Physical F/G orders are-3 and-2, so direct differentiation gives

```text
J_e0 = (3*P*Qprime - 2*Pprime*Q)/9.
```

The strong driver equates this derived expression to Jc and includes ZJ*Jc-1. It does not prescribe P or Q. N/d1_jacobian_face.py extracts them from full K2 and the outer blocks; cutoff98 is justified because omitted K2 monomials have D1 exponent at least297, above296. An independent coordinate-determinant control checks the formula. Both primary continuations then add Jacobian bands in ascending t-power, with the actual constant minus Jc last at r=163. A separate delta52 control inserts that constant early, using physical degree-corner jets. Its result is not substituted for the primary trace. A zero-Jacobian point fails the printed nonzero clause and is not a full-chart survivor.

For a minor y-radius delta, ord h3=3*delta-8. Multiplying by degree ratios and clearing denominators derives every pole endpoint:

| branch | K3 local floor | K2 local floor | KF local floor | KG local floor |
|---|---:|---:|---:|---:|
| delta2 |9|27|81|54|
| delta52 |21|63|189|126|

Strictly lower coefficients are zero. At equality the rows subtract P,P^3,P^9,P^6; they never zero the nonzero face. The old inclusive support function would otherwise create a false terminal unit. The fresh tag formula uses cover L, generic w exponent g=L*(1+delta), and includes k at power n exactly when n>=L+g*k and n-g*k is divisible by L. Each tag is realized by an actual monomial in the full degree box. All four counts1134,513,1316,594 agree with the frozen controls, including the full centres.

The endpoint complete systems also license strict minor remainder rows. Effective normalized C2,C3 floors are18,27 or42,63. Effective A2,A3,B1,B2 floors are54,81,27,54 or126,189,63,126; unshifted outer floors subtract the cover1 or2. Equality coefficients remain unknown. These equations are generated from Thm1.2 and the same source systems, not inferred from a higher D1 floor. The first C2 minor coefficient is20/3-3E82 at local power8 or16. When this strict-below equation arrives, it legitimately derives E82=20/9. This is a later consequence, not the unjustified D2-face pin warned against by the gate.

**Historical and point controls.** The frozen historical engine was run on the fleet through both charged endpoints. At delta2 stage4 the actual reduced row `stage4_J_d159_k35` is6264; at delta52 stage8 `stage8_G_local16_coord0` is64. Both localized ideals are unit. The exact artifacts are N/historical-delta2-stage4.json/.sing and N/historical-delta52-stage8.json/.sing, with logs and GNU time output under N/logs/historical-fleet/. These are real compatibility controls on the historical coordinate chart. Adding the newly derived C2/C3 source bounds to the old face would already contradict the pi21 equation. Therefore this control does not claim that toggling one coefficient inside the stronger replacement reproduces the same *first* unit stage.

The named gate points are carried as substitution controls, not equations. The diagnostic delta2 point has jet0=rho=1; the delta52 point has jet0=c=1; all other diagnostic coordinates are0, including the newly carried minor_a2. Their exact inverse monic division gives C2 minimum D2 weight15<64, with coefficients t5*z0=-4224 and t5*z10=-64; C3 minimum weight47<96. Thus they fail the replacement's source preblock immediately. On the diagnostic enlargement itself, they survive the old endpoints and first fail at G_local10_coord0=4096 (delta2 stage6) and G_local20_coord0=4096 (delta52 stage12). N/deep_frozenbasis_diagnostic_point_delta2.json and its delta52 counterpart repeat this test using this lane's diagnostic module rebuilt from the frozen arithmetic, rather than relying on matching variable names in a different ring.

New source-coordinate points are obtained after every rational pivot block by choosing remaining coordinates, solving the displayed graph map, and checking every accumulated raw row. Assigning all free coordinates0 except jet0 and the separation parameter initially gives valid source D2/D1 points, but the first minor C2 strict row has value20/3. The solver changes the point when this row arrives. N/deep_source_point_delta2.json and its delta52 counterpart distinguish these source assignments from the old diagnostic points. A reported dimension is a dimension of the entire maintained locus; a tested point is never substituted into the equations used to compute that dimension.

**Finite results.** Both branches completed stages0 through8 over Q. There are no nonlinear residual equations after the recorded rational pivots at any of these finite checkpoints. The dimensions below include the redundant free jet0; the audited translation slice has dimension one less.

| stage | delta2 dimension | delta52 dimension |
|---|---:|---:|
|0|1025|1023|
|1|978|976|
|2|936|934|
|3|902|900|
|4|875|873|
|5|856|854|
|6|842|840|
|7|831|829|
|8|824|822|

At every entry a fresh rational point satisfies all accumulated source and schedule rows, including rho/c localization. The delta2 replacement stage4 dimension875 agrees with the diagnostic917 after adding one omitted centre and43 independent source equations. The delta52 stage8 dimension is822. Neither historical death survives as a source-chart death at its old endpoint.

**Deep computation and exact controls.** After the D108 incremental local-power order, the equivalent accelerated order completes C2/C3 minor rows and K2's target, then the outer minor rows and F/G targets. N/print-audit-pole-membership.* proves by polynomial convolution that these equations imply every later F/G pole coefficient and equality face; 14 negative controls per branch distinguish the required targets. No unknown coefficient is deleted. All inner remainder rows alone reduce the free inner dimensions64/62 to31/11, with explicit rational points and zero residual. The full inner/outer minor block reaches gauge dimensions349/103, still with exact rational points.

Each phase declares Q, ordered generators, localizer, before/after maps, emitted rows, full rational pivot equations and residuals. Only Q* leaders are solved. A radical step a*f^n=0 -> f=0 requires an exact single-factor identity with a in Q*; no component of a product is selected. Only the declared separation and Jacobian scalars are localized.

Singular uses Q, degree-reverse-lexicographic order and explicit Rabinowitsch equations Zrho*rho-1 or Zc*c-1, plus ZJ*Jc-1. The ideal is passed directly, with no sat() wrapper. N/minor_final_verify.py checks immutable hashes, source generator images, complete graph/radical chains and terminal rows regenerated on the *before* map, then reruns Singular. Negative controls alter fields, leaders, maps and radical identities. Independent D1 and origin emitters use direct e,Pi series and physical x,y Taylor derivatives.

The derived D1 face uses graph coordinates for its computed arrays. Deck congruence gives P(Pi)=p(X), Q(Pi)=Pi*q(X), X=Pi^3. The equation p*q+3X*p*qprime-2X*pprime*q=3Jc has13 scalar coefficients; degree13 cancels by the generated degrees8 and5. Rational graph leaders give an invertible coordinate change. The D1 dimensions are337/91; the separate delta52 early-constant control has dimension90. Merging the verified weak Jacobian prefixes through r=41/46 gives dimensions296/82. Equality of both full source-polynomial images and ordered ambient generators is checked before merging, rather than inferred from coordinate names. The final native prefixes are J0..70, dimension213 (delta2), and J0..96, dimension34 (delta52), on the audited translation slice. They cover9159/11252 of the13530 global Jacobian coefficients;4371/2278 remain in the primary schedule, ending at163. N/results-fullJ-batch/fullJ-batch-delta2.json and its delta52 counterpart bind every completed phase. GNU timeout stopped the jobs at20:30; unfinished work is not counted.

Reordering the actual constant row on the J66/J89 parents gives NONUNIT dimensions229/43. N/print-audit-corner-completion.md supplies the first-Taylor determinant and exact certificates. For delta52 it derives that e is already a unit, then uses d=R*e^2 in the irreducible quadratic field, retaining e and its inverse. The bidirectional algebra map preserves both complex embeddings; no e specialization occurs. These are separate row controls, not the newer primary prefixes.

No new rational point exists after imposing this nonzero D1 face. Independently normalizing its fixed rational leading coefficients, eight rational pivots eliminate the lower p coefficients. The remaining universal face ideal has dimension1. Its exact Groebner basis gives q4!=0 and R=q3/q4^2 satisfying153664*R^2-117584*R+22789=0, whose discriminant is-181398528. The independent audit checks both ideal inclusions against both the original coefficient equations and a graph model. See N/universal_D1_control.* and N/print-audit-universal-d1-verify.*. Thus subsequent point fields honestly report dimension only. This is not a complex-locus death; the universal curve is nonempty over the algebraic closure.

The first nonlinear exporter test caught Singular's parsing of q^9/32768 as a fractional exponent. N/deep_safe_singular.py now multiplies each row by its exact nonzero rational denominator and serializes integer polynomials, recording every scale and rejecting parser diagnostics. Independent unit/nonunit regression controls include rational powers and both localizers. All prior zero-residual stages and integral historical controls are unaffected. Frozen run snapshots remain immutable; resume records identify the safe helper separately.

Native FLINT arithmetic retains the full free ring; smaller occurring-variable rings have explicit embeddings. Cached bands are transported through every later proved graph map. Actual overlap bands agree exactly with individual generation. For speed the actual D1 Groebner basis derives three rational graph solves and, writing d=Zface_H2_2,e=Zface_H2_5, the monic relation

```text
q=d^2-(283/3500658)*d*e^2+(37/20415837456)*e^4=0.
```

All old residuals are retained under the recorded graph maps, and q remains a generator. Coefficient arithmetic uses the rank-two module modulo q and emits each combined A+B*d row; it never splits those coefficients or chooses a root. The leader is1 and d/e are protected from subsequent pivots. Original rows and normal forms differ by multiples of q. N/print-audit-quotient-d1.* verifies both ideal inclusions, both branches, dimensions, powers0..40 and the negative control q=d^2-e,row=d-1: splitting creates a false unit. The quotient is a derived ideal consequence, not another face assumption.

**Support-subchart survivors.** N/print-audit-full-chart-survivor.py constructs rational points with all outer blocks0, corrected C2/C3 equations and every minor target satisfied. Assignments and row hashes are in N/print-audit-full-chart-survivor-delta2.json and its delta52 counterpart, with .rows.tsv files. Despite the older filenames, their scope is only the support and positive-Jacobian subchart.

The tests check41774/42639 rows, including source equations, finite/pole rows and all13529 positive-degree Jacobian coefficients. These are row counts, not ranks. Every row vanishes over Q. Negative controls B1c_0_32=1 and separation0 give values-864 and-1.

These points have F=h2^3,G=h2^2 and J=0. They are **necessary support-chart survivors only, not full requested-chart survivors or Keller pairs**. Extra zero-Jacobian bands cannot remove them. A separate characteristic instrument requires T2's actual degree55 and nonzero leader (Lemma2.1 p151, Prop2.2 p152, Prop3.1 p157). Its family G^3-F^2+a*G^2+b*F*G+c*F+d*G+e must retain all five lower target coefficients. At these pure-power points every possible degree is a multiple of33, hence not55. A degree upper bound cannot replace attainment. N/print-audit-nonchart-instrument.md and its exact control document this limited obstruction; it is not a full-chart kill.

Independent replay verifies every graph and the final ideal at J70/J96, including dimensions213/34. Complete independent F/G coefficient reconstruction reaches J67/dimension226 and J93/dimension39; the latest direct reconstructions hit the verification cutoff. These scopes are distinct. N/minor_authoritative_index.json binds the successful and bounded receipts; every referenced hash was checked.

N/stage-trace.csv curates403 records from the selected schedules and continuations, with hashed ancestry; it does not add a verdict. N/README.md identifies entry points and immutable code snapshots. N/deep_final_fleet_receipt.json binds final runs and stopped process groups; all24 hash references were mechanically checked. Worker `i-0e0d5719a280cf30f` was verified TERMINATED at20:40:14 UTC before sealing (N/fleet-termination.json). N/artifacts.sha256 verifies3652 files; its SHA-256 is `7cc2be6ab6556558cda34caba76a79dc46242d96f34b9d45d8cbdadc29f1064f`.

Both gate outcomes remain **OPEN / compute-bound**; no full-chart survivor is asserted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `29567`.
- Body SHA-256:
  `5487f32a463f62954ba5a8c58f63b1ceb22c1e8561cd652c2d3706ef4246b6e3`.
- Frozen basis: `ec612a7dda0fa3eedea1324560dafaf127b6af96`.
