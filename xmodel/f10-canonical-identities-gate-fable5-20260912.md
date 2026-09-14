# f10-canonical-identities-gate-fable5-20260912

Reviewer: Fable 5.1 (independent, hostile, different-model) of Astra.
Tag: f10-canonical-identities-gate-fable5-20260912
Start UTC: 2026-09-12T05:14:59Z. Reserve 05:31Z / HARD 05:34Z (never extended).
Mode: manual/model-side reasoning only; no code execution, no CAS, no subprocess arithmetic;
both Python inputs read as inert text. Only documentary date/hash/text commands were run.

## Custody (prepins at 05:15Z, before any read; all five match the expected list)

    4c38ed3b0764989f8c6a0104dd0ced4b3d2b9dc411f1abf571c215eab3beb7a5 f10-canonical-identities-astra-20260912.md
    5078142850c5f4d2e4f08da18fad01ea0271bf36c18740df372884747535280a produce.py
    acd07f800707c379aba60bd06f239d38cd83c86867729561367abd2bcc04ce73 arithmetic.py
    f4b7fdab548eb4b7f9cc3ec03972939fab3f22c914133937c251614ea3136585 f10-p523-scalar-gate-fable5-20260912.md
    35be725b4a820ac41ff8f2b10fa6713e463c794424792d220950748d08d529e1 f10-p523-missing-matrices-gate-sol-20260912.md

All five were then read WHOLE (produce.py 1-369, arithmetic.py 1-350, Astra 1-EOF incl. seal,
scalar gate 1-EOF, Sol gate 1-EOF incl. seal). Accepted, not re-reviewed: literal C,D, leading
ODE/contacts, F=0, 125 denominators, the 15 scalar inversions (ten by my scalar gate, five
determinant attachments and both h5/h6 inverse[2][2] identities by Sol), h7 column (355,40),
critical_c=36, pivots 464/429/298. Notation: k=17-h, s=10-h, a=381=[T^0]C=[T^1]C,
b=465=[T^0]D, u_h=[T^2]A_h, O_h(A,B)=10CB'-kC'B+sAD'-17A'D (produce.py 63-67).

## A. Census 111+39 from code — CONFIRMED

Counted from the `record(label,poly,zero)` calls, not from the producer's numbers:

| lines | labels | total | required |
|---|---|---:|---:|
| 93 | upper:h:part, h=1..6 | 6 | 6 |
| 99 | upper:h:basis:j, h=1..6, j=0..2 | 18 | 18 |
| 116-118 | early:h:residual, early:h:rho | 12 | 12 |
| 120-121 | middle:h:U2, middle:h:V4, h=5,6 | 4 | 4 |
| 144,146 | upper:h:part/variation, h=7..10, zero iff h==7 | 8 | 2 |
| 194 | install:h:j, exponent 10-h-3j<0 | 2 | 2 |
| 204-205 | auxiliary.Dnegative/Vnegative | 2 | 2 |
| 226 | Euler-resonance:0:0, 3:1 (no zero flag) | 2 | 0 |
| 233 | Euler-band:h, h=0..10, zero iff h<=7 | 11 | 8 |
| 251 | upper-J:j:i, j=2..7, i<24-3j, zero iff 23-i-3j<=7 | 63 | 41 |
| 258 | low-band:h:j, h=0..10, j=1,0, zero iff h<=7 | 22 | 16 |
| | | 150 | 111 |

Install labels: allowed T-degree is 3,2,2,2,2,2,2,1,0,0,-1 for h=0..10 (line 186); 10-h-3j<0
occurs only at (5,2),(6,2), so exactly two, both required. upper-J per j: 18,15,12,9,6,3 labels
and 8,8,8,8,6,3 required (i>=16-3j). Nonmandatory 6+2+3+22+6=39. Line 317 asserts 150/111/39;
disjointness is enforced by the reuse error at line 39, and every required label is one row of
Astra's table. Six SCALE groups (lines 287-300): 1+1+1+21+24+1=49.

## B. Early triangular solve, completed 3x3, middle cancellation, grading — CONFIRMED

**Pivot and degree.** C=T^3+aT+a is monic with [T^2]C=0. Adding vT^j to B changes
10CB'-kC'B only in degrees <=j+2, and the degree-(j+2) coefficient by 10jv-3kv. So the
descending loop (lines 71-76) zeroes degrees degree+2,...,2 of op-target exactly, by division by
the D1 units, PROVIDED the initial residual sAD'-17A'D-target has degree <=degree+2. Nothing about
a matrix inverse is used for degrees >=2.

**Induction (h<=6).** A_h=sum_{j<=2} xyz_j T^j has degree <=2 and B_h=part+sum xyz_j V_j has
degree <=4 (V built from T^0..T^4). Hence each forcing summand (lines 88-90) has degree
<=max(2+3,1+4)=5<=6, so `part` has zero defect and, since [T^6]forcing=0, its T^4 coefficient
is 0. Basis inputs: sD' (deg 4), sTD'-17D (deg 5), sT^2D'-34TD-target (deg 6, target -2T^6 only
at (4,T^2)). All <=6, so the 18 basis defects vanish; moreover b4=0 for A=1,T (deg 4,5 gives
[T^6]=0), so deg V_0<=2, deg V_1<=3. This settles the 24 early upper defects and the "B4=0" and
basis-degree facts.

**Full residual.** By linearity of op, op(A,V)=op({},part)+sum_j xyz_j op(T^j,V_j)
= -forcing+r_part + sum_j xyz_j (target_j + r_j), where r=r[0]T+r[1] are the low rows and
target_j=-2T^6 exactly at (h,j)=(4,2), so sum_j xyz_j target_j equals the recorded target
(line 115). Thus early:h:residual = (base0+sum xyz_j r_j0)T + (base1+sum xyz_j r_j1)
= ((M xyz)_0+base0)T+((M xyz)_1+base1) with M rows (r_j0),(r_j1),(rho_j) (line 104 transposes
columns). xyz=M^{-1}(-base0,-base1,rho) with a two-sided inverse (arithmetic.py 315-320), so
M xyz is literally the right-hand side: both low coefficients vanish. early:h:rho
= sum_j xyz_j(10a[T^0]V_j-17b[T^0]A_j)-rho = (M xyz)_2-rho = 0. Twelve records.

**Middle (h=5,6).** First solve rho=0: q:=xyz_2 = inv20(-base0)+inv21(-base1). Second solve
rho' = q*(-1/ratio)*H7_h^{-1}; third component q+inv22*rho' = q - (ratio*H7_h)(q/(ratio*H7_h)) = 0
using the accepted inverse[2][2]=ratio*H7_h (line 110; Sol 268=268, 206=206). So U2=0
identically; V4=[T^4]part+xyz_0[T^4]V_0+xyz_1[T^4]V_1+0=0. Hence deg A_5,A_6<=1, deg B_5,B_6<=3,
and install:5:2, install:6:2 are the empty polynomial xyz_2.

**Grading.** x_h enters only as rho=var(h-1) at gap h (weights 1..4); z only in the h==7
branch (weight 7). Scalars have weight 0, forcing at gap h is bilinear in weights i and h-i, and
the solves are linear with scalar pivots; h=10 has targetvar=-T^4 of weight 0 multiplied by
value of weight 10. So A_h,B_h are homogeneous of weight h for every h (lines 261-263 hold).

## C. h7 top cancellation and Lambda — CONFIRMED (independent extraction)

**Top coefficients.** b4 for A=T^2 is -E6/(40-3k): h=3 gives E6=35-34=1, pivot -2, so
[T^4]B_3=u_3/2 (Sol: 262=1/2). h=4 gives E6=30-34+2=-2, pivot 1, so [T^4]B_4=2u_4 (Sol: 2).
Without the -2T^6 target it would be 4u_4.

**h7 forcing degree 5.** [T^5] of (10-i)A_iB'_{7-i}-(10+i)A'_iB_{7-i} is
u_i B_{7-i,4}[(40-4i)-(20+2i)]=(20-6i)u_iB_{7-i,4}. Since u_5=u_6=0 and B_{5,4}=B_{6,4}=0, only
i=3,4 survive: 2u_3(2u_4)-4u_4(u_3/2)=2u_3u_4. A_part=(z-Ud_0)T with U=-u_4, d_0=u_3 contributes
(3*5-17)(z-Ud_0)=-2z+2Ud_0=-2z-2u_3u_4 at T^5; minus target -2zT^5 gives +2z. Total 0. The
initial residual has degree <=4 (no T^6: forcing <=5, A_part deg 1), so the degree-2 solve leaves
zero defect. Variation: 3D' has degree 4, zero defect. Both h7 upper records proved. With the
wrong h4 target the sum is 6u_3u_4-2u_3u_4=4u_3u_4, as Astra states (formula-level).

**Lambda.** invC2=W^2 c^{-2} through degree 6 equals C^{-2}; P=C^2 int(R C^{-2})
= c^2 int(R c^{-2}) since (aW)^2=1; lam=[T^6]P*F-[T^5]P/2=-[T^5]P/2 as F=0. With v=T+wT^3,
(1+v)^{-2}=1-2T+3T^2-(4+2w)T^3+(5+6w)T^4+..., c^2=1+2T+T^2+2wT^3+2wT^4+w^2T^6.
R=T: integral T^2/2-2T^3/3+3T^4/4-(4+2w)T^5/5; [T^5]=-(4+2w)/5+3/2-2/3+w=1/30+3w/5.
R=1: integral T-T^2+T^3-(1+w/2)T^4+(1+6w/5)T^5; [T^5]=1+6w/5-2-w+1-2w+2w=w/5.
Mod 523 with w=151: 60^{-1}=462 (60*462=27720=53*523+1), 10^{-1}=157, 3w/10=453*157=71121
=135*523+516=-7, so l1=-1/60-3w/10=61+7=68. l0=-151*157=-23707=-(45*523+172)=-172=351.
Cross-check: 30^{-1}=401, 3w/5=453*314=509, [T^5]=910-523=387, -387/2=-387*262=-455=68.
Determinant-one: 68*355+351*40=24140+14040=38180=73*523+1. Truncation to degree 6 loses nothing
(only degrees <=4 of c^{-2} enter [T^5]P).

**Low pair.** residual = base0 T+base1 + value(c1T+c0), value=-(l1 base0+l0 base1). With
l1c1+l0c0=1 and psi=base1*c1-base0*c0 (line 163): [T^1]=base0(1-l1c1)-c1l0 base1=-l0 psi,
[T^0]=base1(1-l0c0)-c0l1 base0 = l1c1 base1-c0l1 base0 = l1 psi. Matches lines 166-167 for any (l1,l0), so h8..10
hold with the one-sided witnesses too. Psi is not set to zero anywhere.

## D. Installation, S-divisibilities, Laurent identity, Euler — CONFIRMED

**Polynomiality.** a3=[theta^3]Ahat = A_{0,3}S^{1}=S. a2=sum_{h<=4}u_hS^{4-h} (F=0, u_5=u_6=0),
so a2|_{S=0}=u_4=-U and Dformal=(a2+U)/S is polynomial with [S^0]=u_3=d_0. a1|_{S=0}=A_{7,1}
=z-Ud_0, so a1-z+U*Dformal is divisible by S and Vformal is polynomial. Both auxiliary records
are the S^{-1} coefficients, identically zero. Then Ahat = S theta^3+(S Dformal-U)theta^2
+(z-U Dformal+S Vformal)theta+Kpar by definition.

**Laurent bracket.** For f=S^pA(theta/S^3), g=S^qB(theta/S^3): f_S=S^{p-1}(pA-3TA'),
f_theta=S^{p-3}A', so [f,g]=S^{p+q-4}(pAB'-qA'B); the 3TA'B' terms cancel. With p=10-i,
q=17-j, summing i+j=h gives S^{23-h}(O_h(A_h,B_h)+forcing_h)(theta/S^3), the leading ODE at
h=0. Delta expands to -S^2theta^7 + 2USteta^6 - 2zStheta^5 - U^2theta^5 + (2zU-ES)theta^4
+(EU-z^2)theta^3 - Eztheta^2, weights 0,4,7,8,10/11,14,17; the weight<=7 terms are exactly
the images of the targets -T^7, 2UT^6=-2xyz_2T^6, -2zT^5. Installed B exponents 17-h-3j are
>=0 through h=10 (degrees 5,4,4,4,4,3,3,2,3,2,2), so the identity is between polynomials.
Hence for the formal bands, (J-Delta) at weight h<=7 equals S^{23-h}(low_h)(theta/S^3): zero for
h<=6 and -l0psi7 S^{13}theta + l1psi7 S^{16} at h=7 (P1[13]=172psi7, P0[16]=68psi7).

**Euler recurrence.** [theta^{j+2}]J = j b_j+(j+1)a2'b_{j+1}+(j+2)a1'b_{j+2}+(j+3)a0'b_{j+3}
-3Sb_j'-2a2b'_{j+1}-a1b'_{j+2}, so [theta^{j+2}](J-Delta)=0 is (j-3S d/dS)b_j=q_j with q_j
literally lines 212-217; S^i has multiplier j-3i, zero only at (0,0),(3,1) in the ranges, and
the Euler pivot j-3(17-h-3j)=10j-51+3h is the D1 pivot. Weights: b_j is homogeneous of weight
17-3j, so q_j has S-degree <=17-3j and the loop range 18-3j is complete. Descending j=4..0,
weight-h components of q_j involve only weight<=h parts of b_{j+1..j+3} and of a_k (all
parameter weights positive), so later gaps cannot reach h<=7. Induction: formal B satisfies the
same equations at weight<=7 (its J-Delta has theta-degree<=1 there) with b_5=S^2 and b_6..8=0
agreeing; nonresonant coefficients agree by unit division; at (3,1) (weight 7, gap 7, theta^3)
the formal B_7 has degree<=2, so both sides are 0, and q_{3,1}=0 is forced. (0,0) has weight 17,
outside every band, and is never required. Eight Euler-band records proved.

**Upper-J and low-band.** At nonresonant (j>=2, j-2<=4) positions the Euler construction itself
zeroes the coefficient; the resonant required position is upper-J:5:1 (weight 7), which equals
-q_{3,1}=0 by the formal argument; theta^7 gives 5S^2-6S^2+S^2=0 directly. All 41. Low bands:
weight-h parts of J use only A,B of weight<=h, which agree with the formal bands for h<=7, so
low-band:h:j are 0 for h<=6 and the h=7 records subtract exactly (-l0psi7, l1psi7). All 16.
Astra's "same upper equations" wording is slightly loose (most upper-J zeros need no band
agreement) but the conclusion is correct.

## E. 49 SCALE comparisons — CONFIRMED

scaled(poly,k) maps z^{e4}S^{e5}theta^{e6} to s^{2e4+e6+k}S^{e5}t^{e6}=s^k sigma(monomial),
sigma(z)=s^2, sigma(theta)=st, a ring map, injective on monomials (e4 recovered from
(2e4+e6+k,e6)); s=1 is never substituted. A_inverse: s^{-3}sigma of the Ahat identity gives
St^3+(S origd-origu)t^2+(s^2*st*s^{-3}=1 - origu origd + S origv)t+origk, line 284-286.
target_inverse: s^{-3}sigma(Pi)=t-origu t^2+St^3=origPi, and s^{-7}sigma(Delta)
=-(origell t origPi + t origPi^2)=origUpper. bracket_scale: d_S commutes with sigma and
d_t sigma(f)=s sigma(d_theta f), so origJ=s^{-3-5}*s*sigma(J)=s^{-7}sigma(J). low1/low0:
[S^i t^j](s^{-7}sigma(residual))=s^{j-7}sigma(P_{j,i}), offsets -6 and -7; the literal
origResidual subtracts 1+origu t, which lives only at (i,j)=(0,0),(0,1) since U is S-free,
matching both i=0 subtractions; 21+24 zeros without any P vanishing. guard_product: orig_a
=s^{-3}Wi (Euler-band:0 and [T^0]C=Wi), orig_b=s^{-5}t5i ([S^17 theta^0]Bhat has weight 0, is
nonresonant, equals [T^0]D), and s^8 W t5 times them is 1. Six groups, 49 polynomials; the
13-key scale_record (line 319) is a container count, not 13 equations.

## F. Controls and overstatement check — CONFIRMED with two notes

Psi7=Hq+36z is a nonzero polynomial (z enters linearly at h7 with parameter-free coefficient
36 from the accepted scalar gate), while the two required h7 low-band diagnostics subtract
172psi7 and 68psi7 exactly: the diagnostics vanish, the bracket coefficients do not. Wrong h4
target leaves 4u_3u_4 at T^5 (C above); changed gauge B_{3,1}=eta shifts Euler-band:7 by eta
theta^3. Both are formula-level; Astra labels them so and evaluates no modified source (Sol's
wrong-target mutation is a scalar-level control on M4, an accepted input). Notes: (1) Astra's
"b_lead" in rho is the constant term [T^0]D=465, a naming slip only; (2) the support remarks
(theta-degree<=7, S-degree<=23-3j, 108 positions, q_j range) are exact homogeneity statements
and are correctly separated from the 100000-term cap, wire caps, RSS, CPU and wall time. No
runtime or all-source conclusion is drawn here.

## Verdict

- A CONFIRMED (150/111/39 counted from code; disjoint by label uniqueness).
- B CONFIRMED (degree bound, full 3x3 residual, middle q-kappa cancellation, grading).
- C CONFIRMED (l1=68, l0=351 independently; 68*355+351*40=73*523+1; signs).
- D CONFIRMED (both S-divisibilities, Laurent identity, Euler uniqueness, gauge (3,1)=0,
  (0,0) not required, all 8+41+16 records).
- E CONFIRMED (49 = 1+1+1+21+24+1, offsets -3,-5,-1,-2,-3,-1,-3,-7,-6,-7, Jacobian power -7).
- F CONFIRMED; no REFUTED item; no GAP within the 111+49 question.

Strongest exact composed consequence: at the literal leading (523, V=0) point, given the
accepted units, inverse-entry identities and h7 column, every one of the 111 required diagnostic
polynomials and 49 SCALE comparison polynomials is the zero element of
F_523[x1,x2,x3,x4,z][S,theta] (or its s-Laurent extension), so lines 328-332 cannot raise
STOP_CANONICAL_ANOMALY or STOP_CONSTRUCTION_ANOMALY for algebraic reasons. This is not a
characteristic-zero or generic identity, not row generation, program completion, a cap/runtime
statement, a rank/minor, source-zero, point, all-r, modulus-vector, or JC2 result. No scope
expansion, code edit, guard/cap change, new prime, helper, worker or further model. No
charge_basis line (no exit claim). No artifact_finalize; the unchanged launcher owns custody.

## Postpins (sha256sum at 05:24:36Z after all reads and after own WHOLE readback; identical to the prepins)

    4c38ed3b0764989f8c6a0104dd0ced4b3d2b9dc411f1abf571c215eab3beb7a5 f10-canonical-identities-astra-20260912.md
    5078142850c5f4d2e4f08da18fad01ea0271bf36c18740df372884747535280a produce.py
    acd07f800707c379aba60bd06f239d38cd83c86867729561367abd2bcc04ce73 arithmetic.py
    f4b7fdab548eb4b7f9cc3ec03972939fab3f22c914133937c251614ea3136585 f10-p523-scalar-gate-fable5-20260912.md
    35be725b4a820ac41ff8f2b10fa6713e463c794424792d220950748d08d529e1 f10-p523-missing-matrices-gate-sol-20260912.md

Own WHOLE readback of this body was completed before this marker. No later edits, no Seal,
no artifact_finalize, no side files. Written within the original reserve.

<!-- BODY-END -->
