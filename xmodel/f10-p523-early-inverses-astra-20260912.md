# p523: all six early completed-matrix scalar nodes

First action 2026-09-12 04:07:14 UTC. Original reserve04:28 / HARD04:31.
Manual finite-field co-research, UNREVIEWED. No scientific execution.

## Endpoint and dependency scope

At the proposed523/V=0 leading specialization, all SIX actual early
completed determinants survive:

    (det1,...,det6)=(80,345,211,155,93,68).

Their inverses are respectively (85,285,233,27,45,100).
The source's row order is (T,1,rho), its columns are (1,T,T²), and
the exceptional h4 third-column target remains −2T6. No pivot,
gauge, cap, code or place has been changed.

The exact matrices, source recurrence, determinant cofactors and integer
inverse products are supplied below. Additional hand checks independently
reproduce the initial-five and late-four scalar attachments. All fifteen
named scalar expressions are therefore nonzero at this proposed leading
place. The reports and this extension remain manual/UNREVIEWED. This
does not certify every canonical anomaly, the full printed place vector,
an admissible whole-circuit execution, a rank, source outcome or JC2.

## 1. Leading specialization and actual operator

All residues are in F523. The old factored constant term gives a V=0
root: with tau=3/10, d=143/100 and A=759/100,

    S7(0)=d²*A*(48+5*tau−27*tau²),
    48+5*tau−27*tau²=9*523/100.

The monic denominator has only prime factors2,3,5,7. Trial division by
2,3,5,7,11,13,17,19 establishes primality of523; the last five remainders
are5,6,3,13,10. This checks the linear place, not every supplied P7 coefficient.

From the literal source constants,100^(-1)=68, dL(0)=310,
A=358 and K(0)=2*310*358=208. Hence W=−208/(210*310)=151:
the denominator is248 and151*248=−208 modulo523. Also151^(-1)=381.
With c=1+T+151T³ and nu=17/10=54, the derivative recurrence is

    j*t_j=(55−j)*t_(j−1)+(165−j)*151*t_(j−3),  t0=1.

Its reduced numerators for j1..7 are54,247,27,0,45,0,0, giving
(t0,...,t7)=(1,54,385,9,0,9,0,0). Thus, independently of the
advisory early scratch,

    C=T³+a*T+a, D=T5+T³+d*T²+6T+b,
    a=381, d=159, b=465.

The complete leading ODE is also consistent: the T5,T4,T3,T2
coefficients of10CD'−17C'D are respectively24,27,9,324 times523;
T1 is6*523*a, T0 is−15*523*a, T6 is0 and T7 is−1.

For k=17−h and s=10−h=k−7, source lines61–106 define

    O_h(A,B)=10CB'−k*C'B+s*AD'−17A'D.

For each A=1,T,T² put E=s*AD'−17A'D−target and
B=sum_(j=0)^4 b_j*T^j. The only nonzero target is −2T6 for
(h,A)=(4,T²). The actual descending upper solve is

    q_j=10j−3k,
    b_(n−2)=−[E_n+a*(10n−k)*b_n+10a*(n+1)*b_(n+1)]/q_(n−2),
    n=6,5,4,3,2,

with absent b_j zero. This follows by extracting T^n in O_h−target;
it does not insert an assumed completed-matrix formula. The low rows are

    r1=E1+a*(10−k)*b1+20a*b2,
    r0=E0−k*a*b0+10a*b1,
    rho=10a*b0−17b*A0.

Here10a=149,20a=298,30a=447,40a=73,−17b=463,
−34b=403. All divisions in this solve have nonzero integer pivots
of absolute value≤48, hence survive523.

For reproducibility, E has these exact coefficient descriptions:

* A=1: E4=5s,E2=3s,E1=318s,E0=6s.
* A=T: E5=5s−17,E3=3s−17,E2=(2s−17)*159,
  E1=6(s−17),E0=−17b.
* A=T²: E6=5s−34+2*[h=4],E4=3s−34,
  E3=(2s−34)*159,E2=6(s−34),E1=−34b,E0=0.

## 2. All eighteen upper-basis polynomials

Each entry below is (b0,b1,b2,b3,b4), not a source payload.
The completed matrix column is the residual AFTER these upper cancellations.

| h | A=1 | A=T | A=T² |
|---|---|---|---|
|1|(173,0,95,0,0)|(450,448,0,234,0)|(405,223,262,0,459)|
|2|(138,0,420,0,0)|(107,400,0,141,0)|(88,112,143,0,315)|
|3|(515,0,168,0,0)|(98,482,0,263,0)|(216,8,177,0,262)|
|4|(335,0,442,0,0)|(470,509,0,292,0)|(446,191,36,0,2)|
|5|(416,0,165,0,0)|(436,70,0,350,0)|(83,287,453,0,133)|
|6|(248,0,82,0,0)|(303,360,0,1,0)|(263,54,451,0,2)|

Hand sanity checks reverse the solve, rather than merely repeating the
determinant computation. For h2,A=T² the four nontrivial divisions reduce to
5*b4=6,25*b2=437,35*b1=259,45*b0=299, giving
315,143,112,88. At h3,A=T²,32*b1=256 gives b1=8.
At h5,A=T,36*b0=6 gives436; at h6,A=T,33*b0=62 gives303.
At h4,A=T², q4=1 and E6=−2 force b4=2; omitting the target would
give4, a different matrix. For h1,A=1,b0=−177/2=173 and
b2=45/28=95. The advisory scratch's M1/M4 are reproduced, but
their supplied numbers were not treated as independent verification.

## 3. The six literal matrices and determinant witnesses

Rows are (r1,r0,rho), columns (1,T,T²); every entry is reduced modulo523.

    M1 = [[315,381,176],[337,206,481],[90,106,200]]
    M2 = [[92,480,155],[62,323,158],[105,253,37]]
    M3 = [[513,187,163],[351,375,171],[317,481,281]]
    M4 = [[259,246,449],[260,432,331],[170,471,33]]
    M5 = [[29,457,383],[229,194,99],[210,112,338]]
    M6 = [[81,311,213],[380,205,452],[282,169,485]]

The following are UNSIGNED first-row minors (m11,m12,m13).
Thus det=M11*m11−M12*m12+M13*m13, with the middle minus retained.
The integer in column3 evaluates that expression using the reduced minors.

|h| minors | integer expansion | determinant | inverse | integer inverse product |
|---|---|---:|---:|---:|---|
|1|(151,52,446)|106249=203*523+80|80|85|6800=13*523+1|
|2|(219,348,76)|−135112=−259*523+345|345|285|98325=188*523+1|
|3|(112,492,271)|9625=18*523+211|211|233|49163=94*523+1|
|4|(88,426,381)|89065=170*523+155|155|27|4185=8*523+1|
|5|(92,128,75)|−27103=−52*523+93|93|45|4185=8*523+1|
|6|(25,352,134)|−78905=−151*523+68|68|100|6800=13*523+1|

These are scalar inverse products; no whole matrix-inverse array is
claimed to have been emitted. The exact matrix inverse is
det^(-1)*adj(M), and the universal adjugate identity proves both-sided
products. As a separate source-specific sanity check, the (3,3) cofactors
of M5,M6 are343,410. Multiplying by45,100 gives268,206, respectively.
These agree with (2/11)*H7_5 and (1/3)*H7_6 in the source's
middle-map coefficient identity, using the independently checked values below.

## 4. Additional initial-five and late-four attachment checks

This subsection is secondary to the six-matrix endpoint; it does not
replace any retained source test. For alpha=(27−h)/10 and
c=1+T+W*T³, partitions of7 give the exact formula

    H7(alpha)=binom(alpha,3)*
      [(alpha−3)(alpha−4)(alpha−5)(alpha−6)/840
       +W*(alpha−3)(alpha−4)/4+3W²].

Here W²=312,840^(-1)=33,4^(-1)=131. At h5, alpha=316,
binom(alpha,3)=180 and the bracket terms are237,410,413; their sum
is14 and H7=428. At h6, alpha=159, binom(alpha,3)=471 and the
bracket terms are441,160,413; their sum is491 and H7=95.
Independent reduced products for the first bracket numerator are
378*178=340 at h5 and122*27=156 at h6, before multiplying by33.
These checks do not infer an all-parameter contact theorem.

For h7,8,9 the literal variation has Avar=1, targetvar=0, Bvar degree≤2.
Writing k=17−h,s=10−h, upper cancellation gives

    b2=−5s/(20−3k), b1=0,
    b0=((20−k)*a*b2+3s)/(3k),
    c1=20a*b2+318s, c0=−k*a*b0+6s.

It yields:

| h | (b0,b1,b2) | (c1,c0) |
|---|---|---|
|7|(400,0,263)|(355,40)|
|8|(388,0,375)|(464,72)|
|9|(369,0,132)|(429,267)|

At h10 the actual DIFFERENT variation is Avar=0,targetvar=−T4:
(b0,b1,b2)=(460,0,1), (c1,c0)=(298,138).
The code tests c1 first, so the selected pivots are exactly464,429,298;
no residue-dependent replacement of the generic operator is being made.

The first occurrence of z is h7. Earlier forcing is z-free, while
[z]Apart=T and [z]target=−2T5. Their upper solve gives
Bz=517+418T: the relevant forcing contribution is
−8T³−1749T²−84T−7905, so Bz1=−2/5 and Bz0=−583/10.
Its low pair is(439,356). Hence the source's exact sign convention
Psi7=c1*base0−c0*base1 gives

    critical_c=355*356−40*439=108820=208*523+36.

It does not depend on unknown earlier forcing coefficients or on the
choice of the h7 completion functional. No full h7-functional or
full-band anomaly test is claimed from this scalar calculation.

For completeness, the remaining nine named scalar inverse products are:

| node | residue | inverse | integer product |
|---|---:|---:|---|
|dL|310|275|85250=163*523+1|
|W|151|381|57531=110*523+1|
|t5|9|465|4185=8*523+1|
|H7_5|428|11|4708=9*523+1|
|H7_6|95|512|48640=93*523+1|
|critical_c|36|247|8892=17*523+1|
|pivot8|464|195|90480=173*523+1|
|pivot9|429|306|131274=251*523+1|
|pivot10|298|86|25628=49*523+1|

Thus the six new tests and the nine rechecked attachments cover all
fifteen NAMED SCALAR inverse nodes, not the whole circuit's assertions.

## 5. Controls, exact stopping point and read scope

The det4 result depends on retaining the modified third-column target.
Swapping the low-row order or the sign of rho changes the actual matrices;
nonzero determinants alone would not validate such a port. Every entry
above is from the source's stated upper solve, before source forcing is
used to solve the completed affine maps. A vanished determinant would
have been a BAD PLACE for this circuit, not a characteristic-zero scalar
vanishing or source conclusion; none vanishes here.

Five frozen inputs were freshly pinned before WHOLE inert-text reads:
the old V=0 precheck, ROOT's place candidate, actual necessary-row
produce.py, ROOT's late-node report, and the explicitly nonblind early
scratch. The scratch is advisory, not an independent reviewer; M1/M4
agreement is disclosed as such. All formulas and arithmetic in this report
were checked manually; exact ranges and hashes are in PINS.json.
No arithmetic implementation, live peer report, coefficient/source payload,
external source or runtime was accessed. No code, cap or frozen input
was edited. Scientific subprocess/import/AST/syntax/test/CAS/fixtures: NONE.

Remaining scalar-test quantity at this fixed leading place: zero.
Remaining whole-source anomalies, exact serialized place-vector comparison,
source row formation/readback, resource completion and rank: NOT CHECKED.
Cheapest next validation is an independent hand review of the six
recurrence tables and scalar products; planning10–15min is UNMEASURED,
not a deadline, cap, launch or automatic follow-on authority. No theorem
promotion, actual source point, source exclusion, all-r claim or JC2
verdict follows. This report stops at its named scalar endpoint.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10344`.
- Body SHA-256:
  `874ceace5e5487039bf83638a478520a3cfe73b6ed785855c66524cb41d4bce6`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
