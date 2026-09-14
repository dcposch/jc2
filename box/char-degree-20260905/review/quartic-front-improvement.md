# A fourth-power front consequence from the first low digit

This supplements `../front-band-lemma.md` and `../cubic-front-improvement.md`.
It proves the further necessary radical consequence

    (99,66): D_r=0 for r<=29, C_r=0 for r<=60.

The D108 consequence remains D_r=0 for r<=32, C_r=0 for r<=66. No
target coefficient, source coordinate, or nonzero leader is specialized.

Use the audited four monic divisions in normalized t,z coordinates:

    v^2=UH+R,  vU=PH+R1,  vR=Qpart H+R2,  U^2=WH+R3.

Each displayed division is the transported physical monic division.
Its remainder has z-degree less than k. Let r>0 be the first t-order of
D, with r<2k-1, and put d=[t^r]v=[t^r]D, H0=[t^0]H. Monic division
implies ord U,ord R>=2r; all leading division bands are division by H0.

The full upper digit is

    3R/4 - tP/8 + p*t^(4k-2)=0.

Consequently R=tP/6-4p*t^(4k-2)/3. As ord P>=3r, if 3r+1<4k-2,
then ord R>=3r+1 and R_(3r+1)=P_(3r)/6. The identity at t^(2r)
first gives U_(2r)=d^2/H0, so H0 divides d^2.

The digit of normalization 5k-3 is

    E=Qpart - R1/8 - 9tW/64.

Here Qpart starts at least at4r+1, W at4r, whereas R1 starts at3r.
If 3r lies strictly before this digit's target band, its coefficient
forces rem_z(d*U_(2r),H0)=0. Therefore

    P_(3r)=d^3/H0^2,

which recovers the cubic divisibility proved independently in the
earlier note. This use of an actual first band prevents higher H and
D coefficients from contributing to the calculation.

The final low digit, of normalization 6k-3, is

    L=R2 - 9tR3/64 + p*t^(4k-2)*v + q*t^(6k-3).

Its first two terms start at least at4r+1: R2 is the remainder of
vR, whose first possible product band is d*P_(3r)/6 at4r+1; R3 is
the remainder of U^2, whose first possible product band is U_(2r)^2
at4r. Thus, provided the scalar terms arrive later,

    [t^(4r+1)]L
      = rem_z(d^4/(6H0^2),H0) - (9/64)rem_z(d^4/H0^2,H0)
      = (5/192) rem_z(d^4/H0^2,H0).                 (1)

Both dividends in (1) are polynomials: H0 divides d^2. Monic division
is linear over the coefficient field, and 5/192 is nonzero over Q.
If this low band is required to vanish, equation (1) proves

    H0^3 divides d^4.                              (2)

No raw characteristic coefficient beyond the first band of either low
product was isolated. Corrections to H or D start strictly later in
these products and cannot cancel (1). The depth inequalities are part
of the theorem; a low band at or beyond the permitted cutoff cannot
be set to zero by this argument.

For99, the cubic theorem already gives r>=29. At r29, H0 is
z^24(1+z)^9 and the source floor3r+4j>=189 requires ord_z d>=26,
while deg_z d<=32. Condition (2) forces ord_(z+1) d>=ceil(27/4)=7.
The coprime factors require degree at least26+7=33, a contradiction.
All orders used are legitimate: 3r+1=88<130, the E band3r=87 is
before140, the low band4r+1=117 is before141, and its p*v term starts
at130+29=159 while q starts at195. Therefore D starts at least at30.

The normalized quotient identity for C then starts at t^(2*30+1)=61;
the bD correction starts at30+33=63 and the scalar correction at98.
Hence C_r=0 for every r<=60.

This argument stops at the stated cutoff. At r30 the possible shape
d=tau*z^25*(1+z)^7 satisfies both cubic and quartic divisibility with
deg d=32; this is a negative control against claiming r30 is killed.
For108, r33 allows d=tau*z^29*(1+z)^6. Its degree is35 and it also
satisfies (2), so the fourth-power condition gives no additional cutoff.

`quartic_front_control.py/.json` checks the exact monic remainders,
the coefficient5/192, all boundary inequalities, the excluded99r29
candidate, and both surviving leading-shape controls over Q. These
are leading-band controls, not full necessary-chart survivor points.
The proof was independently checked by the source-theorem agent.

As before, these zero-coordinate additions are consequences on the
algebraic set, generally radical rather than individual ideal members.
An engine must apply them to actual source-position images, retain
every original source and characteristic row, and record its rational
graph maps. The theorem itself is not a unit of either whole chart.
