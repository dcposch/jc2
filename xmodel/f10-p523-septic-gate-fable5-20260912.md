# f10-p523-septic-gate-fable5-20260912 — hostile review of the full P7 vector mod 523

Reviewer: Fable 5.1 (independent, different model from ROOT). Started 2026-09-12T05:01:06Z.
Publication reserve 05:16Z, HARD 05:19Z. Manual reasoning only; no local arithmetic tools,
no source execution, no fixture. Python inputs treated as inert text.

Charged claim (only): from produce.py's literal rational tau=3/10, dl, kl, ga, septic, lead,
monic (produce.py lines 11-24), reduction modulo 523 gives the ascending vector
["0","17","249","53","102","191","291","1"], and p="523", degree="1", phi=["0","1"]
satisfies arithmetic.py initialize's acceptance predicates for THIS monic. Nothing about
build(), diagnostics, scalar nodes, source rows, rank or any workflow is reviewed or implied.

## 0. Custody (pre-read hashes, all three matched the expected pins before any read)

- f10-p523-place-candidate-root-20260911.md 7b0298b10e190bfde6b6e32ad448ec2bf99dbcc099519c786b602159e1b9a4b1
- produce.py 5078142850c5f4d2e4f08da18fad01ea0271bf36c18740df372884747535280a
- arithmetic.py acd07f800707c379aba60bd06f239d38cd83c86867729561367abd2bcc04ce73

Interpretation used (arithmetic.py lines 20-34): lists are ascending powers of V; qa pads
and adds then trims trailing zeros; qs scales; qm is the Cauchy convolution out[i+j]+=v*w.
All arithmetic in produce.py is exact Fraction arithmetic (tau=Q(3,10) propagates, so
lead is a Fraction and 1/lead is Fraction(-1,1270080), not a float).

Justification for modular work: every rational below has denominator dividing
2^a 3^b 5^c 7^d, hence lies in Z_(523); reduction Z_(523) -> F_523 is a ring homomorphism,
so step-wise reduction equals ground() applied to the exact monic (ground, lines 47-51).
Signed representatives (x-523) are used freely in products.

## A. dl, kl, ga, monic divisor, L=287, L^-1=441 — CONFIRMED

Inverses: 10^-1=157 (10*157=1570=3*523+1); 100^-1=157^2=24649-47*523=68 (100*68=6800=13*523+1);
1000^-1=157*68=10676-20*523=216; 10000^-1=68^2=4624-8*523=440 (63*440=27720=53*523+1);
5^-1=314 (5*314=1570). tau=3*157=471.

Exact rationals, then residues:
- dl = [(13/10)(11/10), -12*7/10, 12] = [143/100, -42/5, 12].
  143*68=9724-18*523=310; 42*314=13188-25*523=113 -> -113=410; 12. dl=[310,410,12].
- kl = [2*11*13*23*33/10^4, 42*13*23*(-18)/10^3, 840*91/100, -840]
     = [217074/10000, -226044/1000, 3822/5, -840].
  217074-415*523=29, 29*440=12760-24*523=208; 226044-432*523=108, 108*216=23328-44*523=316,
  -316=207; 3822-7*523=161, 161*314=50554-96*523=346; -840+1046=206. kl=[208,207,346,206].
- ga = [3*13*23*33/10^4, -30*3*13*23/10^3, 180*39/100, -36] = [29601/10000, -2691/100, 351/5, -36].
  29601-56*523=313, 313*440=137720-263*523=171; 2691-5*523=76, 76*68=5168-9*523=461, -461=62;
  351*314=110214-210*523=384; -36=487. ga=[171,62,384,487].
- Linear factor (-140 tau)*[1+tau, -6] = [-273/5, 252]; 273*314=85722-163*523=473, -473=50.
  B=[50,252]. (Scalar placement: qs(...,-140*tau) commutes with qm, so this equals
  produce.py's qs(qm(qm([1+tau,-6],kl),dl),-140*tau).)
- lead = -245*120*144*(3/10) = -1270080 = -(2^6 3^4 5 7^2), an integer, 523-unit.
  1270080-2428*523=236, so L=-236=287. Cross-check: degree-7 term comes only from
  245*ga[3]*dl[2]^2 = 245*(-36)*144 = -1270080 = lead, so equal(septic[-1],lead) holds exactly.
- L^-1 derived, not assumed: 287=7*41; 7^-1=299 (7*299=2093=4*523+1); 41^-1: 523=12*41+31,
  41=31+10, 31=3*10+1 gives 1=4*523-51*41, so 41^-1=-51=472; 299*472=141128-269*523=441.
  Inverse product: 287*441=126567=242*523+1. CONFIRMED.

All denominators (10,100,1000,10000,5,1270080) are 523-units, so ground() never raises
STOP_BAD_DENOMINATOR on any of the eight monic coefficients.

## B. Full eight-coefficient convolution ledger — CONFIRMED coefficientwise

Signed inputs: kl=[208,207,-177,206], dl=[-213,-113,12], ga=[171,62,-139,-36], B=[50,252].

kl^2 (each: integer product, then residue):
c0=208^2=43264-82*523=378; c1=2*43056=86112-164*523=340; c2=-73632+42849=-30783, 30783-58*523=449,
-449=74; c3=85696-73278=12418-23*523=389; c4=85284+31329=116613-222*523=507;
c5=-72924, 72924-139*523=227, -227=296; c6=42436-81*523=73.
T1=2*kl^2=[756,680,148,778,1014,592,146,0]=[233,157,148,255,491,69,146,0].

kl*dl: d0=-44304, 44304-84*523=372, -372=151; d1=-23504-44091=-67595, -67595+129*523=-128, 395;
d2=2496-23391+37701=16806-32*523=70; d3=2484+20001-43878=-21393, -21393+40*523=-473, 50;
d4=-2124-23278=-25402, -25402+48*523=-298, 225; d5=2472-4*523=380. K*dL=[151,395,70,50,225,380]
(signed [151,-128,70,50,-298,-143]).

B*(kl*dl): e0=7550-14*523=228; e1=-6400+38052=31652-60*523=272; e2=3500-32256=-28756,
-28756+54*523=-514, 9; e3=2500+17640=20140-38*523=266; e4=-14900+12600=-2300, -2300+4*523=-208,
315; e5=-7150-75096=-82246, -82246+157*523=-135, 388; e6=-36036+68*523=-472, 51.
T2=[228,272,9,266,315,388,51,0].

dl^2: f0=45369-86*523=391; f1=48138-92*523=22; f2=-5112+12769=7657-14*523=335;
f3=-2712+5*523=-97, 426; f4=144. dl^2=[391,22,335,426,144] (signed [-132,22,-188,-97,144]).

ga*dl^2: g0=-22572+43*523=-83, 440; g1=3762-8184=-4422+8*523=-238, 285;
g2=-32148+1364+18348=-12436+23*523=-407, 116; g3=-16587-11656-3058+4752=-26549+50*523=-399, 124;
g4=24624-6014+26132-792=43950-84*523=18; g5=8928+13483+6768=29179-55*523=414;
g6=-20016+3492=-16524+31*523=-311, 212; g7=-5184+9*523=-477, 46.
ga*dl^2=[440,285,116,124,18,414,212,46] (signed [-83,-238,116,124,18,-109,212,46]).

T3=245*ga*dl^2: 245*83=20335-38*523=461, -461=62; 245*238=58310-111*523=257, -257=266;
245*116=28420-54*523=178; 245*124=30380-58*523=46; 245*18=4410-8*523=226;
245*109=26705-51*523=32, -32=491; 245*212=51940-99*523=163; 245*46=11270-21*523=287.
T3=[62,266,178,46,226,491,163,287].

Sum S7=T1+T2+T3: [233+228+62, 157+272+266, 148+9+178, 255+266+46, 491+315+226, 69+388+491,
146+51+163, 287] = [523,695,335,567,1032,948,360,287] = [0,172,335,44,509,425,360,287].

Normalization by L^-1=441=-82: 172*82=14104-26*523=506, -506=17; 335*82=27470-52*523=274,
-274=249; 44*82=3608-6*523=470, -470=53; (-14)(-82)=1148-2*523=102; (-98)(-82)=8036-15*523=191;
360*82=29520-56*523=232, -232=291; 287*441=1.
Monic = [0,17,249,53,102,191,291,1]. Every coefficient equals the charged vector.

Independent cross-checks (evaluation homomorphism, computed from the input polynomials, not
from the ledger): at V=1, kl(1)=967=444, dl(1)=732=209, ga(1)=1104=58, B(1)=302;
S7(1)=2*444^2+302*444*209+245*58*209^2 = 453+483+150 = 1086 = 40, and the ledger's
coefficient sum 2132-4*523 = 40; monic sum 904-523=381 with 287*381=109347-209*523=40. Agrees.
At V=-1, kl(-1)=141, dl(-1)=-88, ga(-1)=6, B(-1)=-202; S7(-1)=14+200+62=276, and the ledger's
alternating sum is 276; monic alternating sum 380 with 287*380=109060-208*523=276. Agrees.
Constant term also agrees with the factorization S7(0)=dl0^2(2+tau)(3+tau)(48+5tau-27tau^2)
(re-derived: 8(2+tau)(3+tau)-35tau(1+tau)=48+5tau-27tau^2), whose last factor at 3/10 is
4707/100 = 9*523/100, so the exact rational S7(0) is nonzero in Q but 523-divisible.

## C. Metadata acceptance predicates in initialize (arithmetic.py 99-129) — CONFIRMED

Traced in source order for place={p:"523",degree:"1",phi:["0","1"],P7_mod_p:<vector>} and
monic = the exact rational list of A/B:

1. integer("523",2147483647) (line 101): str, nonempty, 3<=10 chars, ascii, isdecimal, no
   leading zero, 523<=2^31-1. P=523. integer("1",7): DEGREE=1. Bounds line 103: P>=2, DEGREE>=1.
2. Primality (105-109): trials 2..22 (22^2=484<=523<529=23^2). 523 is odd; digit sum 10 so
   not 3-divisible; not 5; 523=7*74+5; =11*47+6; =13*40+3; =17*30+13; =19*27+10. Composite
   trials are excluded by their prime factors. 523 is prime; no raise.
3. Lengths (110): len(phi)=2=DEGREE+1; len(P7_mod_p)=8.
4. PHI=[integer("0",522),integer("1",522)]=[0,1] ("0" is a single char, so the
   leading-zero rule does not fire). prescribed=[0,17,249,53,102,191,291,1]; every string is
   canonical decimal, every value <=522.
5. Line 114: PHI[-1]=1; prescribed[-1]=1; [ground(v) for v in monic]: each monic coefficient is
   septic[i]/(-1270080) with denominator a 523-unit (section A), so ground returns the residue
   and by the homomorphism argument the list is exactly [0,17,249,53,102,191,291,1] (section B).
   Equality holds; no raise. This is the only predicate that compares against the formulas.
6. Factor (116): rem(prescribed,[0,1]) divides by V; each step zeroes the top entry and trims,
   ending with trim([0])=[], which is falsy. phi=V divides P7 exactly because P7(0)=0.
7. Frobenius/irreducibility (118-128): field([0,1]) reduces [0,1] mod PHI=[0,1] to [], padded to
   (0,), so x=(0,). fpow((0,),523): out=field(1)=(1,), first odd bit gives fm((1,),(0,))=(0,),
   all later products stay (0,). DEGREE//2=0, so the gcd/irreducibility loop body never runs
   for i=1 (a linear phi is irreducible with nothing to test). Final v=(0,)=x; no raise.
8. Line 129 clears UNITS/DENOMINATORS; no further predicates.

Optional consequence, not a replacement for anything above: coefficient 1 is 17 != 0, so
V=0 is a simple root of P7 mod 523 (P7'(0)=17). It is not consulted by initialize.

Scope statement: ground() is defined only on Z_(523) and raises STOP_BAD_DENOMINATOR
otherwise (lines 49-50). There is no reduction map from the whole characteristic-zero
field to F_523; the acceptance above concerns exactly these eight rationals. Whether other
quantities in build() (W, t5, H7_*, det*, pivot*, critical_c, the D0/D1/D2 registry) reduce or
invert is untested here and is not implied.

## D. Manual negative control: coefficient 1 changed 17 -> 18 — CONFIRMED (rejects at line 114)

Altered place vector ["0","18","249","53","102","191","291","1"]; formulas untouched.
Trace: predicates 1-4 pass unchanged ("18" is a valid string <=522; lengths unchanged).
Line 114 evaluates the `or` chain left to right: PHI[-1]!=1 is False, prescribed[-1]!=1 is
False, then prescribed!=[ground(v) for v in monic] compares [0,18,...] with [0,17,...] and is
True at index 1. initialize raises ValueError('STOP_BAD_PLACE: actual monic coefficients')
(line 115). Execution never reaches the factor and Frobenius checks. Had it reached them
they would still pass: the altered constant term is 0 so V still divides the altered vector
(the root V=0 survives), and the Frobenius loop depends only on P, DEGREE and PHI, never on
P7_mod_p. So the exact reconstructed-coefficient equality is the sole predicate that
distinguishes the genuine vector from this near-miss; linear-factor and Frobenius checks
cannot. The negative control is decided by reading, not by running.

## Verdicts

- A. CONFIRMED. dl=[310,410,12], kl=[208,207,346,206], ga=[171,62,384,487], linear factor
  [50,252], lead=-1270080=287 mod 523, L^-1=441 derived from 7^-1*41^-1, 287*441=242*523+1.
  All denominators are 523-units.
- B. CONFIRMED coefficientwise. T1=[233,157,148,255,491,69,146,0], T2=[228,272,9,266,315,388,51,0],
  T3=[62,266,178,46,226,491,163,287], S7=[0,172,335,44,509,425,360,287],
  monic=[0,17,249,53,102,191,291,1]. Two independent evaluation checks (V=1, V=-1) and the
  factored constant term agree with the ledger.
- C. CONFIRMED. All initialize predicates pass for this exact monic; degree-1 irreducibility
  loop is vacuous and Frobenius is trivially satisfied; the coefficient equality is the only
  formula-sensitive predicate.
- D. CONFIRMED. The 17->18 control is rejected by 'STOP_BAD_PLACE: actual monic coefficients'
  at arithmetic.py line 114-115 and by nothing else.
- GAPs sealed: none inside the charged scope. Outside scope and untouched: whether build()
  runs, the fifteen named inverse nodes, denominator registry, source rows, rank, canonical
  anomaly, characteristic-zero statements. A confirmed vector still must be recomputed by both
  scientific evaluators in an authorized execution; nothing here authorizes hardcoding.

Read scope: exactly the three pinned inputs, each read WHOLE once after hashing. No other file,
network, process, source execution or model was consulted. Custody and finalize remain with
the unchanged external launcher; no artifact_finalize or charge_basis declaration is made.

<!-- BODY-END -->
