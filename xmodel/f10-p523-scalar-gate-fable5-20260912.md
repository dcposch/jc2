# f10-p523-scalar-gate-fable5-20260912

Reviewer: Fable 5.1 (independent, hostile). Tag f10-p523-scalar-gate-fable5-20260912.
Opened 2026-09-12T04:27:43Z. Reserve 04:48Z, HARD 04:51Z. Manual finite-field
review only; no subprocess arithmetic, no execution, both .py files read as inert text.

Scope: exact p=523 scalar attachment (fixed D0/D1/D2 denominators, 15 named scalar
inverses) at V=0 on the literal leading integral model. No whole-circuit claim.

## Prepins (sha256sum at 04:27:51Z, before any read; all six match the expected list)

    2caec1f5...1308 f10-p523-early-inverses-astra-20260912.md
    3f70c36d...1bbcb f10-r3-vzero-place-astra-20260911.md
    7b0298b1...4b1  f10-p523-place-candidate-root-20260911.md
    46f254c1...bb2c f10-p523-late-inverse-root-20260912.md
    50781428...80a  produce.py
    acd07f80...e73  arithmetic.py

All six were then read WHOLE.

## A. Prime, place, denominator registry, W/t5/H7, C,D, contacts, ODE — CONFIRMED

Derived from the literal code, not from the charged prose.

**Prime.** 22^2<523<23^2; 523 mod 2,3,5 nonzero by parity/digit sum 10/last digit;
523 = 7*74+5 = 11*47+6 = 13*40+3 = 17*30+13 = 19*27+10. Prime. `initialize` trial-divides
to sqrt(P), so the code agrees.

**Place.** phi=["0","1"] gives PHI=[0,1], DEGREE=1, PHI[-1]=1. `field(list)` reduces mod
V, so every list collapses to its constant term; in particular `field([0,1])` is 0, so the
T^2 coefficient of c vanishes (F=0). Frobenius loop is vacuous at degree 1 (v=x=0).
`rem(prescribed,PHI)` demands P7(0)=0 mod 523: S7(0)=dL^2*A*(8A-35tau(1+tau)) with
8A=48+40tau+8tau^2 gives 48+5tau-27tau^2 = 4707/100 = 9*523/100 at tau=3/10. Root confirmed.

**Monic denominator.** lead = -245*120*144*(3/10) = -1270080; 523*2428 = 1269844, so
lead = -236 = 287 mod 523, a unit. Its prime support is {2,3,5,7}.

**Registry.** D0: 10, 210, 287, 1..8, 22, 4, 21, 7, 2, 21, 11 — all units; 'D0:ell21' and
'D0:ratio-den:6' are distinct labels with equal value, and the registry keys on labels, so
no collision. D1: 10j-3(17-h); zero needs 10 | 17-h, i.e. h=7, j=3, and h=7 only ranges
j<=2. |values| <= 48. D2: j-3i on 0<=j<=4, 0<=i<=17-3j; zero exactly at (0,0),(3,1), both
excluded by the literal `if (j,i) not in (...)`; |values| <= 51. All nonzero mod 523.
The `upper` pivot 10j-3(17-h) is the same D1 value (derived below), so no hidden pivot.

**dL, W.** 100^-1=68 (6800=13*523+1). dL=143*68=9724=18*523+310. A=(2+tau)(3+tau)=759/100:
759*68=51612=98*523+358. K(0)=2*310*358=221960=424*523+208. W=-(1/210)*208*310^-1:
210*310=65100=124*523+248 and 151*248=37448=71*523+315=-208. W=151; 151*381=57531=110*523+1.
dL^-1=275: 310*275=85250=163*523+1. a=H=W^-1=381, F=0.

**Series recurrence.** From c(c^nu)'=nu c'c^nu with c=1+T+WT^3:
j t_j=(nu-j+1)t_{j-1}+W(3nu-j+3)t_{j-3}. 10^-1=157, nu=17*157=2669=5*523+54, so
(55-j) and (165-j) as the charged reports state. t1=54; 2t2=53*54=2862=5*523+247, t2=385;
3t3=52*385+162*151=20020+24462=44482=85*523+27, t3=9; 4t4=459+(161*151 mod 523=253)*54:
253*54=13662=26*523+64, 459+64=523, t4=0; 5t5=(160*151 mod 523=102)*385=39270=75*523+45,
t5=9; 6t6=9(49+159*151)=9*24058=9*46*523, t6=0; t7 from t6,t4 = 0.
Contact6 and contact7 hold; t5=9, 9*465=4185=8*523+1.

**C, D.** C=381(1+T+151T^3), 381*151=1: C=T^3+381T+381. D=465*(1+54T+385T^2+9T^3+9T^5):
465*54=25110=48*523+6, 465*385=179025=342*523+159. D=T^5+T^3+159T^2+6T+465, b=465.

**Leading ODE** 10CD'-17C'D with D'=5T^4+3T^2+318T+6, C'=3T^2+381 (my own expansion):
T^7: 50-51=-1. T^6: 0. T^5: 33a-21=12552=24*523. T^4: 50a-4929=14121=27*523.
T^3: 13a-246=4707=9*523. T^2: 507a-23715=169452=324*523. T^1: 3138a=6*523a.
T^0: -7845a=-15*523a. Identity holds.

## B. Eighteen upper-basis columns and six 3x3 matrices — PARTIAL (see census)

**Recurrence from code.** `upper` sets b_j = -[T^{j+2}](op(h,A,V_{>j})-target)/(10j-3k),
k=17-h, descending j. Expanding [T^n] of 10CB'-kC'B with C=T^3+aT+a gives
(10(n-2)-3k)b_{n-2}+a(10n-k)b_n+10a(n+1)b_{n+1}, so the charged b_{n-2} formula is the
literal solve. Low rows: r1=E1+a(10-k)b1+20ab2, r0=E0-kab0+10ab1; rho_j=10ab0-17bA0.
`matrix[i][j]=columns[j][i]`: rows (r1,r0,rho), columns (1,T,T^2). Confirmed.
E-tables for A=1,T,T^2 re-derived from sAD'-17A'D-target; they match the charged ones,
including E6=5s-34+2[h=4] (target -2T^6 enters only at (h,A)=(4,T^2)).

**Orientation.** `det3` uses the six standard signed permutations. `invert_matrix` puts
(-1)^{i+j}*minor(rows!=j, cols!=i)/det at out[i][j], i.e. the adjugate transpose: correct,
and the routine then asserts both products equal I. Orientation cannot silently be wrong.

**M1 fully reconstructed by hand (h=1, k=16, s=9, q=(-48,-38,-28,-18,-8)).**
A=1: b2=45/28, 28^-1=467, b2=95; b0=(27+(45/7)a)/48 with 7^-1=299: (45/7)a=432=-91,
b0=-64/48=-4/3=173 (agrees with the charged -177/2=173). r1=247+298*95 (=68) = 315;
r0=54-343*173 (=240) = 337; rho=149*173 (=150) -60 = 90.
A=T: b3=14/9=234; b1=(10+(196/9)a)/38, 196/9=138, 138a=278, 38^-1=234, b1=448;
b0=(159+447*234)/48 = 157*316 = 450. r1=-48-194*448(=94) = 381; r0=-60-65+331=206;
rho=149*450=106.
A=T^2: b4=11/8=459 (8^-1=327); b2=(-7+33a)/28=14/28=262; b1=(71+73*459(=35))/38=106*234=223;
b0=(-150+2a)/48=89*316=405. r1=-120-376+149=176; r0=-320+278=481; rho=149*405=200.
So M1=[[315,381,176],[337,206,481],[90,106,200]] exactly as charged.
Minors m11=206*200-481*106=-9786=151, m12=24110=52, m13=17182=446.
det1=315*151-381*52+176*446=106249=203*523+80. 80*85=6800=13*523+1.

**M4 third column reconstructed (h=4, k=13, s=6, q=(-39,-29,-19,-9,1)).**
E6=-2 so b4=-E6/q4=2. b2=(-16+54a)/19, 54a=177, 19^-1=468, b2=36. b1=(-3498+146)/29
=309*505=191. b0=(-168+252a)/39, 252a=303, 39^-1=228, b0=446. r1=-120-222+268=449,
r0=-409+217=331, rho=149*446=33. Matches charged column (449,331,33).
**Negative control:** omitting the target gives E6=-4, b4=4, and every lower b of this
column changes through the a(10n-k)b_n feedback; columns 1 and 2 (A=1,T) have no target
term and are untouched. The changed column is the third (T^2) column of M4 only.
det4 from charged M4: m11=432*33-331*471=-141645=88, m12=-47690=426, m13=49020=381;
259*88-246*426+449*381=89065=170*523+155. 155*27=4185=8*523+1.

**Not reconstructed:** the remaining 14 basis polynomials (h=2,3,5,6 all columns; h=4
columns 1,2) and the entries of M2,M3,M5,M6. Integer inverse products checked:
345*285=98325=188*523+1; 211*233=49163=94*523+1; 93*45=4185; 68*100=6800. Those
products confirm the inverse of each charged residue, not the residue itself.

## C. Middle inverse[2][2], H7 scalars, rho normalization — CONFIRMED (H7, relation on supplied M5/M6)

**H7 formula.** [T^7](1+T+WT^3)^alpha: parts {1,3} partitions 1^7, 1^4 3, 1 3^2 give
binom(alpha,7)+5 binom(alpha,5)W+3 binom(alpha,3)W^2 = binom(alpha,3)[(alpha-3)(alpha-4)
(alpha-5)(alpha-6)/840 + W(alpha-3)(alpha-4)/4 + 3W^2]. 840*33=27720=53*523+1.
h=5: alpha=11/5, 5^-1=314, alpha=316; binom=316*315(=170)*314(=34)/6=17/3=180.
313*312=378, 311*310=178, 378*178=340, 340*33=237; 151*(378/4=356)=410; 3*312=413.
Sum 1060=14; H7_5=180*14=2520=428. 428*11=4708=9*523+1.
h=6: alpha=21*157=159; binom=159*158(=18)*157(=211)/6, 6^-1=436, 471. 156*155=122,
154*153=27, 122*27=156, 156*33=441; 151*61=320, 320*262=160; 413. Sum 1014=491;
H7_6=471*491=231261=442*523+95. 95*512=48640=93*523+1.

**inverse[2][2] relation.** Code asserts inverse[2][2] = ratio*H7_h, ratio=4/22, 7/21.
inverse[2][2]=cof_{22}/det=(M00 M11-M01 M10)/det. On the supplied matrices:
M5: 29*194-457*229=-99027=-180=343; 343*45=15435=29*523+268. 11^-1=428 so (2/11)*428
=2*428^2=2*134=268. M6: 81*205-311*380=-101575=-113=410; 410*100=41000=78*523+206;
(1/3)*95=349*95=33155=63*523+206. Relation holds on the supplied M5,M6 and det5,det6;
it is conditional on those unreconstructed entries.

**rho normalization.** For h<=4 rho=var(h-1) (fresh parameter); for h=5,6 the code
re-solves with rho = xyz[2]*(-1/ratio)*H7_h^-1 and records middle U2/V4 diagnostics.
The third row of every matrix is rho_j=10ab0-17bA0 with 10a=149, -17b=463 (17*465=7905
=15*523+60). The charged reports use the same normalization. Confirmed as read.

## D. critical_c=36 and the late pivots — CONFIRMED

**First appearance of z.** `z=var(4)` is used only inside the `h==7` branch
(Apart=(z-Uglobal*d0)*T, target=-2zT^5). For h<=6 the circuit uses C,D,T and the fresh
parameters var(0..3) only, so Ab[1..6], Bb[1..6], Uglobal, d0 and the h7 forcing are
z-free. `upper` is linear in (A, target-forcing, V), so [z]Vpart solves O_7(T,Bz)=-2T^5
with no dependence on the unknown early inverses. Independence confirmed from code.

**Bz and low pair (h=7, k=10, s=3, q=(-30,-20,-10)).** E=3TD'-17D+2T^5
=(15-17+2)T^5+(9-17)T^3+(954-2703)T^2+(18-102)T-7905 = -8T^3-1749T^2-84T-7905.
b2=0 (E4=0); b1=-(-8)/(-20)=-2/5=-2*314=418; b0=-(-1749)/(-30)=-583/10=-583*157
=-91531=-(175*523+6)=517. Bz=517+418T. base[0]=[T^1]=E1=-84=439;
base[1]=[T^0]=-7905+10a(b1-b0)=-60+149*(-99): 149*99=14751=28*523+107, so -60-107=356.

**Variation column (Avar=1, target 0).** E=3D'=15T^4+9T^2+954T+18. b2=3/2, b1=0,
b0=(9+15a)/30. c1=954+30a=431+447=355. c0=18-10a*b0=18-3a-5a^2: 3a=97,
a^2=145161=277*523+290, 5*290=404; 18-97-404=-483=40. Charged (355,40) reproduced.

**Psi sign.** Code: `psi = base[1]*c1 - base[0]*c0`. [z]Psi7=356*355-439*40
=126380-17560=108820=208*523+36. critical_c=36; 36*247=8892=17*523+1.
This is the literal source sign, independent of the h7 Lambda functional (lams only
enter the 'determinant-one column' assertion, which I did NOT review) and of the
`scalar()` requirement that the z^1 coefficient be parameter-free (true, since the
z-coefficients of Apart and target are the parameter-free T and -2T^5).

**Late pivots.** h8 (k=9,s=2): b2=-10/(20-27)=10/7; c1=200a/7+636. a/7=381*299
=113919=217*523+428; 200*428=85600=163*523+351; 636=113; c1=464. 464*195=90480
=173*523+1. h9 (k=8,s=1): b2=5/4, c1=25a+318=111+318=429; 429*306=131274=251*523+1.
h10 (Avar=0, targetvar=-T^4, so E=+T^4): q2=-1 gives b2=1; b1=0; b0=13a/21, 21^-1=274,
13a=246, 246*274=67404=128*523+460; c1=20a*b2=298, c0=-7a*460=-52*460=-385=138.
298*86=25628=49*523+1. The code tests `any(c1)` first, so pivot8/9/10 are the c1 values
464/429/298. The h10 'r3 ell literal column' assertion also holds here: with F=0, H=a,
ge=13a/21=460=b0. Using the h8/9 Avar=1 formula at h10 would be wrong; the code's h10
branch is distinct and was followed literally.

**Not reviewed here:** the h7 Lambda/invC2 identity, the full Psi7 (Hq part), the
'critical affine graph'/'critical elimination'/'guard identification' assertions, all
`record(...,True)` canonical anomalies, Euler band, 108 Jacobian positions, scale
comparisons, and the 150/111/39 inventory.

## E. Fifteen-node census and strongest surviving attachment

`m.UNITS` must equal exactly {dL,W,t5,H7_5,H7_6,critical_c,det1..det6,pivot8,pivot9,
pivot10}. Census of what THIS review establishes at 523/V=0:

| node | residue | inverse | status here |
|---|---:|---:|---|
| dL | 310 | 275 | reconstructed |
| W | 151 | 381 | reconstructed |
| t5 | 9 | 465 | reconstructed |
| H7_5 | 428 | 11 | reconstructed |
| H7_6 | 95 | 512 | reconstructed |
| det1 | 80 | 85 | matrix and det reconstructed |
| det4 | 155 | 27 | column 3 reconstructed; det on charged rows |
| det2,3,5,6 | 345,211,93,68 | 285,233,45,100 | inverse products only; entries NOT reconstructed |
| critical_c | 36 | 247 | reconstructed |
| pivot8/9/10 | 464/429/298 | 195/306/86 | reconstructed |

Fixed D0/D1/D2 denominators: all nonzero (A). Registry/pivot identity confirmed.

**Strongest surviving attachment (exact).** At p=523, phi=V, on the literal leading model:
all fixed denominators and 11 of the 15 named inverse nodes are independently nonzero
with the charged residues; det4 is nonzero conditional on the charged columns 1,2 of M4;
det2,det3,det5,det6 are nonzero only on the charged matrices, whose 12 columns I did not
re-derive. Nonzero scalars license evaluating those expressions in F_523. They do NOT
establish: the `equal` construction identities beyond the leading ODE, contacts, the
inverse[2][2] relation on supplied rows and the h10 ell column; row formation; serialized
place-vector acceptance (F); rank; characteristic-zero source nonemptiness or zero; an
execution gate; or JC2. The already accepted source-exclusion theorem and support bound
were not re-reviewed and their hypotheses remain undischarged.

## F. P7_mod_p vector — GAP (secondary)

Checked: constant term 0 (root, A) and leading term 1 (lead=287, 287*441=126567
=242*523+1 so the charged L_inverse=441 is right). The other six coefficients
17,249,53,102,191,291 and the simple-root claim P7'(0)=17 were NOT reconstructed from
2K^2+BK dL+245 gamma dL^2 in this window. `initialize` compares all eight against the
literal monic, so a wrong entry is a refused place, not a wrong scalar. GAP retained.

## Verdicts

- A: CONFIRMED.
- B: CONFIRMED for recurrence, row/column order, h4 target, inverse orientation, M1
  (all three columns, det1, inverse), M4 column 3 and the negative control; GAP for the
  14 unreconstructed basis columns and the entries of M2,M3,M5,M6 (only det-from-charged
  and inverse products checked for det4; only inverse products for det2,3,5,6).
- C: CONFIRMED for H7_5, H7_6 and the rho normalization; inverse[2][2] relation CONFIRMED
  on the supplied M5/M6 only.
- D: CONFIRMED (critical_c=36, Bz, low pair, Psi sign, 464/429/298, four inverse products).
- E: census as tabulated; no whole-circuit admissibility claimed or implied.
- F: GAP.

No REFUTED item. No code, prime, or scope change. No charge_basis line (no exit claim).

## Postpins (sha256sum at 04:34:07Z after all reads; identical to the prepins)

    2caec1f58e008cb175b5334627b7899d888e4f2a26a971adf006761da0151308 f10-p523-early-inverses-astra-20260912.md
    3f70c36d66bb9cc8fdbbb53a8546fcf1dc4547897374cc50a3b55658d7b1bbcb f10-r3-vzero-place-astra-20260911.md
    7b0298b10e190bfde6b6e32ad448ec2bf99dbcc099519c786b602159e1b9a4b1 f10-p523-place-candidate-root-20260911.md
    46f254c123e9b1ea9b30e2758e8229a739b603fb431dba076054bde90c90bb2c f10-p523-late-inverse-root-20260912.md
    5078142850c5f4d2e4f08da18fad01ea0271bf36c18740df372884747535280a produce.py
    acd07f800707c379aba60bd06f239d38cd83c86867729561367abd2bcc04ce73 arithmetic.py

Own WHOLE readback of this body completed before the marker. No artifact_finalize;
the unchanged launcher owns custody. No later edits.

<!-- BODY-END -->
