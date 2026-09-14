# r2 infinity: explicit remaining-chart reduction at 89

## 1. Status, clock, and exact scope

Verdict: PROVISIONAL MANUAL ADVANCE / COMPLETE SPECIAL-FIBRE GAP. The actual
remaining-chart H5 is computed below; its exceptional denominator fibre is
empty. All three initial forms admit the indicated integral model. The two
remaining univariate polynomials and their gcd are NOT computed, so neither
the complete special fibre nor generic weighted-projective emptiness is proved.

First action was 2026-09-10 10:41:53 UTC; the two exact destinations were absent.
The earlier deadline is 11:01:00 UTC (not first+21 minutes); publication reserve
begins 10:58:00 UTC. This clock was never reset. Ownership is only this report,
its documentary transaction, and box/f10-r2-infinity-remainder-astra-20260910/.
Basis: 0d39df3c9fd69c939a8420c54d03228b9077777d.

Exactly the ROOT card and its nine named parents were hash-pinned before body
use. The card was read WHOLE; all nine unchanged parent bodies use expressly
permitted, previously completed same-byte WHOLE reads. Exact pins and reuse are
in READSCOPE.md. The compatibility-infinity parent is PROVISIONAL: ROOT reports
that its FIRST gate did not complete the arithmetic replay. This cheap child
therefore receives no accepted-truth status from that parent, and must be
quarantined if the parent arithmetic fails. No reviewer body is an input.

Only manual source-text mathematics was performed. There was no scientific
subprocess of any size, code execution, syntax/import/test/CAS, generated
coefficient artifact, implementation, network, corpus, process inspection,
other-lane read, or follow-on authorization. Documentary publication alone used
the existing transaction utility.

## 2. Integral model and conventions

Use the exact B=Q[Z]/(P7) and initial forms H5,H6,H7 from the charged parents;
z=0 means a weighted initial-form diagnostic, NEVER a source specialization.
Take the local order A=(Z_(89)[Z]/(P7))_(89,Z). P7 is monic and integral at 89,
and P7(0)=0 modulo 89. The parent's displayed numerator check is 17+42+30=0.
Equivalently its constant numerator contains
(2+tau)(3+tau)(48+5tau-27tau^2), with the last factor 2*13*89/49.
This is a residue map of an integral order, not a Q-algebra map B -> F89.
Its generic field is the whole field B, with no selected embedding.

All subsequent displayed coefficients are in F89 and ascending powers of T.
At (89,Z), tau=13, dL=16, KL=26, gamma=70, W=74, t5=77, and

    C=T^3-6T-6,
    D=T^5-27T^3+39T^2+38T+37.

Thus a=H=-6, F=0. The extra middle divisor [T^7]c^(15/7)=84 is a unit.
The low residual determinants at gaps 1,2,3 are respectively 52,73,76;
after their two low rows are solved, the rho coefficients in the quadratic
coefficient q_h are respectively -7,73,6. The gap-4 low matrix is

    ((36,19),(17,54)), determinant 19.

These are unit determinants. Integer divisions in the triangular Phi/band
formulas (including 2,3,5,7,10,14,18,21 and the gap parameters 18,17,16,15)
are prime to 89. The leading normalization divisors dL,W,t5 are also units.

For completeness the ACTUAL selected compatibility completions also extend
integrally, so this audit includes H7 rather than only H5/H6. Critical
chi=(36,77). Since c^-2 begins (1,-2,3,26,4), the critical integral formula
P_j(R)=[T^j]c^2 integral(R/c^2) gives P5(T)=83, P5(1)=86. With F=0,
Lambda=(-83/2,-86/2)=(3,46), and 3*36+46*77=1 modulo 89.
The late column is (62,23); its first entry is a B-unit with unit residue,
so the ordered Euclidean completion is (g1^-1,0), reducing to (56,0).
Check: 62*56=3472=1 modulo 89. (An earlier informal message's 33 was
immediately corrected: 62*33=-1, and it is NOT the chosen inverse.)
For ell, g_e=(6H-F^2)/10=32, the column is (5,70), and the same ordered
convention reduces to (18,0), with 5*18=1. This proves regularity of each
fixed completion used to define the actual three forms.

This is not a claim that every intermediate Gauss--Jordan implementation
pivot has nonzero residue: it need not. Use the mathematical Phi formulas or
the adjugate divided by the determinant of the WHOLE invertible low matrix.
They represent the same unique solution over B and extend over A. Intermediate
poles cancel. Accordingly all actual H5,H6,H7 coefficients are regular in A.
These claims still inherit the explicitly provisional arithmetic inputs above.

## 3. Weighted triangular coordinates and solved bands

Let q_h=[T^2]A_h for h=1,2,3. The direct residual solves give

    X1=-7q1,
    X2=73q2+23q1^2,
    X3=6q3+2q1q2+44q1^3.

These are weighted triangular coordinates of weights 1,2,3, with unit
diagonal. They are statements in the special fibre, not a lift with these
same integer coefficients to B. On X1!=0 normalize q1=1 and put q2=u,q3=v.
The parent's excluded X1=0 divisor is complementary to this chart, conditional
on that provisional exclusion being validated.

The following explicit bands make the new H5 calculation reproducible. Each
tuple lists the coefficients in ascending powers of T:

    A1=(-4,-2,1)
    V1=(-19,-5,22,-3,19)
    A2=(37u+57,65u+4,u)
    V2=(50u+16,56u-6,14u+20,-5u+10,45u)
    A3=(62v+35u+8,19v+58u+53,v)
    V3=(31v+35u+13,21v+34u+27,48v+27u+36,
        55v+12u+41,2v)

The first low matrix, in columns (q,l,k), has rows

    (61,46,59), (77,78,47), (65,14,11).

Its first two equations give l=-2q,k=-4q; the last gives rho=-7q.
For a direct forcing check, the next two complete forcings are

    W2=(58,24,74,45,52,38),
    W3=(34u+53,28u+29,70u+13,31u+21,7u+41,53u).

Their zero-quadratic partial low pairs are (17,-3) and
(10u+56,18u+49). The gap-2 and gap-3 low matrices/rho rows are respectively

    (21,41,14), (72,70,17), (46,8,42);
    (38,30,39), (5,53,21), (61,59,4).

For gap 4 the full forcing is

    W4=(21u^2+69u+26v+54,
        42u^2+19u+3v+78,
        34u^2+5u+25v+26,
        29u^2+80u+14v+6,
        83u^2+51u+84v+51,
        76v).

Its partial low pair is
(44u^2+23u+75v+14, 26u^2+67u+15v+36). Solving gives

    A4=(51u^2+81u+34v+38, 4u^2+11u+22v+29),
    V4=(18u^2+43u+34v+39,
        60u^2+59u+56v-5,
        67u^2+2u+6v+71,
        4u^2+11u+77v+29).

For an independent internal control, their u^2 coefficients equal the
previous homogeneous X1=0 gap-4 coefficients multiplied by 73^2=78.
Also the q_h-to-X_h diagonal constants reproduce the parent's homogeneous
gap-2 and gap-3 bands. These are changed-object controls, not new external
premises or machine checks.

## 4. Actual H5 chart and complete exceptional-fibre exclusion

The critical fixed shift is y=-U*d0=uv, since U=-v and d0=u.
For N_i=-W5_i+(12-2i)yD_i the critical partial solution is

    q2=38N4, q1=19N3, q0=13N4-17N2,
    b1=12N4-N1,
    b0=3N3+12N4-2N2-N0.

Thus H5=36b0-77b1 is

    53N0+77N1+17N2+19N3+42N4
      =36W5_0+12W5_1+72W5_2+70W5_3+47W5_4+16uv.

This retains the prescribed compatibility normalization, not a rescaled
substitute. To display the entire coefficient check compactly, apply
L(B)=36B0+12B1+72B2+70B3+47B4 to each cross pair in
W5=sum(i+j=5)((7-i)Ai Vj'-(12-j)Ai' Vj):

| Pair (i,j) | Its L contribution |
| --- | --- |
| (1,4) | 40u^2+86u+66v+41 |
| (4,1) | 60u^2+85u+52v+28 |
| (2,3) | 38u^2+50uv+37u+11v+27 |
| (3,2) | 9u^2+61uv+39u+56v+31 |

For direct replay of this small multiplication, the vectors for
L(B'), L(TB'), L(T^2B'), L(TB) are respectively
(0,36,24,38,13), (0,12,55,32,10), (0,72,51,52,0), (12,72,70,47,0).
For A=k+lT+qT^2, m=7-i, n=7+i, the contribution is
m*k*L(B')+l*(m*L(TB')-n*L(B))+q*(m*L(T^2B')-2n*L(TB)).

Adding the four rows and the fixed 16uv gives the NEW exact chart equation

    H5 = P(u)+Q(u)v,
    P(u)=58u^2+69u+38,    Q(u)=38u+7.

The uv coefficient also agrees with the prior homogeneous control
20*73*6=38. Every assertion here concerns actual coefficient residues, not
formal generic coefficients.

The missing-denominator fibre is now completely checked: Q has its unique
root u=49 (38^-1=-7). At that root 49^2=-2 and

    P(49)=58*(-2)+69*49+38=10 != 0.

Consequently NO point of the H5 zero locus has Q=0, including over the
algebraic closure of F89. Eliminating v=-P/Q loses no point of this chart.
This is stronger than displaying a chart recipe with an unexamined divisor.

## 5. Smallest remaining concrete operation and honest GAP

Weights and the provisional homogeneous controls imply the actual chart
forms have the shapes

    H6 = B3(u)+B1(u)v+88v^2,
    H7 = C3(u)+C2(u)v+c*v^2,

where deg B3=3, lc B3=54, deg B1<=1, deg C3<=3, deg C2<=2.
Indeed 62*73^3=54 and 42*6^2=88. Five H6 coefficients and eight H7
coefficients remain to be obtained from the fixed critical/late/ell bands.
They are definite residues of the charged construction, not free parameters.

The complete remaining chart test is the ordinary gcd in F89[u] of

    F=Q^2*B3-P*Q*B1+88P^2,
    G=Q^2*C3-P*Q*C2+cP^2.

F has degree EXACTLY five with leading coefficient 38^2*54=12; G has
degree at most five. Moreover F(49)=88*10^2=78 != 0, independently of
the thirteen uncomputed residues. Thus Q is already coprime to F; there
is no residual saturation/exceptional-fibre task at this prime.

GAP: compute those thirteen specified residues by the fixed band operations,
then decide gcd(F,G). This report does not possess either full polynomial,
a Bezout certificate, or a common root. It makes NO complete-emptiness claim.
The leading coefficient and Q-fibre checks do not decide that gcd.

With the integral model in section 2, the weighted-projective family is
proper over A. If BOTH the provisional X1=0 exclusion is validated AND the
above gcd is 1, its special fibre is empty; properness then forces the generic
fibre over B empty. Until both obligations are discharged, this implication
is conditional only. Nonempty special fibre would not imply generic
nonemptiness. Neither possibility is by itself a source counterexample or
full-source/JC2 closure. No new finite-algebra dimension claim is promoted.

## 6. Publication boundary

The final custody artifact records all ten input pins, owned pins, expected
transaction manifest, and the terminal idle time. No code or executable
payload is supplied. All mathematics stopped before the original publication
reserve. This report is a terminal provisional packet for ROOT's independent
custody-FIRST / expected-transaction / WHOLE intake, not authority to launch
another consumer, review, execution, or research lane.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10387`.
- Body SHA-256:
  `bffe787bdc93bd2f55e7b82b4efea8edb892107fd0d98d1774e65ea8dddbc48b`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
