# FIRST gate: same-residue paired-contact exclusion (producer f10-two-contact-residual-next-astra-20260909)

2026-09-09. Gate lane fable5. Launch 23:13 UTC (inputs directory timestamp); ROOT TERM 23:27:00 UTC, own stop 23:25:00 UTC with the two-minute reserve, never reset. Charged inputs: exactly the four ordered SHA256 pins in the brief, all four verified byte-identical in the charged order at 23:14:03 UTC before any read. Producer under review: the 10891-byte WHOLE (a4c7e79e...). Read WHOLE: its READ-SCOPE (1209226c...), the accepted parent 17za producer (fe9fb4f2...) and its accepted gate (8c574c30...). Parents 17w/17y/17za are accepted at the exact scopes stated in the two charged parent reports; their interiors are not re-proved and no provenance was followed. Root 17za qualifications retained: prescribed 5/3 < x < y < 2 only, no z = 2 extension, and a residual absence of a forced pole is not existence, cancellation or lifting. ZERO mathematical subprocesses; every polynomial, valuation and residue below was recomputed by hand. No Seal, no charge_basis.

## 0. Verdict table

| Item | Verdict | Smallest actual defect |
|---|---|---|
| A exact B divided difference (1),(2) from the charged parent B_z; W² and V²W cancel; shifts s-7 and s²-p-12s+47; F = z⁴-18z³+119z²-342z+360; Q = s³-2ps-18(s²-p)+119s-342; no modular division by y-x | CONFIRMED | none mathematical; the section 1 headline "no cubic whenever 7 divides j" is stated for every r >= 2 while the NEW mechanism is used only at common residue k in {3,4,5,6} (section 2); at r = 3 mod 7 the common residue is 1 and F'(1) = -154 = -7·22 is NOT a unit, so that class rests entirely on the accepted parent's direct B_z pole, which the producer's "combining with the accepted exclusions" wording already signals |
| B accepted (I); Q = F'(k) mod 7 without inverting y-x; F'(3..6) = -6,2,-2,6 units; v7(Q/5040) = -1 unique least term; V = 0, W = 0, nonunit y-x and number-field embedding; G = 5040·B_z monic integral, reduces to F, at most one root per residue 3..6, no lift claimed | CONFIRMED | none |
| C r = 2 mod 7 to accepted 17y; otherwise m unit; x = y mod 7 iff 7 divides j; x residues 6,3,5 at r = 4,5,6; residual r4 j1,2,3 / r5 j2,4,6 / r6 j2,4,5 are nine infinite congruence classes, none asserted nonempty, none an external open case | CONFIRMED | none |
| D exact diagonal supplies no equation; distinct residues give Q = 0 mod 7 so the pole proof stops; zero guarded algebra via number-field quotient with no valuations on nilpotents; no source/affine-closure/Bezout/point/F10/JC2 claim | CONFIRMED | none |

Accepted scope: exactly the producer's common-residue obstruction. For r >= 2, 1 <= j <= r-1, r = 4,5,6 mod 7 and j a positive multiple of 7, the guarded normalized cubic algebra of 17w is the zero ring. Combined with the accepted parents the undecided perimeter is the nine-class table of the producer's section 1. Nothing about residual points, lifts, uniform closure, source elimination, F10, Keller or JC2 is accepted or claimed.

## A. Exact B divided difference

B_z from the charged parent, term for term the 17za gate's H7 partition list: W²/2 + V²W/2 + (z-3)VW/2 + (z-3)(z-4)W/24 + (z-3)V³/6 + (z-3)(z-4)V²/12 + (z-3)(z-4)(z-5)V/120 + F(z)/5040. Divided differences of the z-polynomials at x,y with s = x+y, p = xy: the z-independent W²/2 and V²W/2 cancel exactly; z-3 -> 1; (z-3)(z-4) = z²-7z+12 -> s-7; (z-3)(z-4)(z-5) = z³-12z²+47z-60 (12 = 3+4+5, 47 = 12+15+20, 60 = 3·4·5) -> (s²-p)-12s+47 via (y³-x³)/(y-x) = s²-p; F(z) = (z-3)(z-4)(z-5)(z-6) = z⁴-18z³+119z²-342z+360 (18 = 3+4+5+6; 119 = 12+15+18+20+24+30; 342 = 60+72+90+120; 360 = 3·4·5·6) -> (s³-2ps)-18(s²-p)+119s-342 via (y⁴-x⁴)/(y-x) = x³+x²y+xy²+y³ = (s³-3ps)+ps. Hence B_y - B_x = (y-x)·D_B with

    D_B = VW/2 + (s-7)W/24 + V³/6 + (s-7)V²/12 + (s²-p-12s+47)V/120 + Q/5040,
    Q = s³-2ps-18(s²-p)+119s-342,

an identity in Q[x,y,V,W]; both lines match the producer's (1),(2). Spot checks: at (x,y) = (3,4), s = 7, p = 12: s-7 = 0, s²-p-12s+47 = 37-84+47 = 0, Q = 343-168-666+833-342 = 0, each equal to the direct difference of the vanishing factors; at (0,1): Q = 1-18+119-342 = -240 = F(1)-F(0) = 120-360. Nonconstant denominators 2,24,6,12,120 are 7-units; 5040 = 7·720 with 720 = 2⁴·3²·5 carries exactly one 7, in the constant. Since y-x is a nonzero rational, B_x = B_y = 0 forces D_B = 0 in the field, with no division modulo 7 and no assumption on v7(y-x). CONFIRMED.

## B. Same-residue pole and the quartic reading

Premise (I): v7(V) >= 0, v7(W) >= 0 from the accepted 17za two-A-equation theorem (x,y distinct, integral, both below 2 so z != 2). With x = y = k mod 7 the divided difference of z^a is the sum of y^(a-1-i)x^i, which is a·k^(a-1) mod 7 as an identity among 7-integral elements; so Q(x,y) = F'(k) mod 7 with no inverse of y-x, valid for arbitrarily large v7(y-x). At a root k of F, F'(k) is the product of k minus the other three roots: F'(3) = (-1)(-2)(-3) = -6 = 1, F'(4) = (1)(-1)(-2) = 2, F'(5) = (2)(1)(-1) = -2 = 5, F'(6) = 3·2·1 = 6; cross-checked with F'(z) = 4z³-54z²+238z-342: 108-486+714-342 = -6, 256-864+952-342 = 2, 500-1350+1190-342 = -2, 864-1944+1428-342 = 6. All units, so v7(Q) = 0 and v7(Q/5040) = -1. Every nonconstant term of D_B is a 7-integral value over a unit denominator, valuation >= 0, infinity if V or W vanishes, which only removes terms. The constant is the unique strictly least term, D_B != 0, contradicting the two B equations. The number-field embedding into Q7bar is the accepted parent setting. CONFIRMED.

Quartic reading: G(z) = 5040·B_z = 2520W² + 2520V²W + 2520(z-3)VW + 210(z-3)(z-4)W + 840(z-3)V³ + 420(z-3)(z-4)V² + 42(z-3)(z-4)(z-5)V + F(z); 2520 = 7·360, 210 = 7·30, 840 = 7·120, 420 = 7·60, 42 = 7·6. For integral V,W, G is a monic integral quartic in z with G = F mod 7, whose residue roots 3,4,5,6 are simple. Two distinct roots x,y of G with a common residue k would make the integral polynomial (G(y)-G(x))/(y-x) vanish while it is G'(k) = F'(k) != 0 mod 7. This is the same difference identity; no lift, Hensel step or irreducibility is claimed or needed. CONFIRMED.

## C. Parameter mapping and the residual table

3n-5m = 15r+6-15r-5 = 1. 7 | m = 3r+1 iff r = 2 mod 7, where n = 12 = 5 mod 7 is a unit: negative exponent valuation, accepted 17y only. Otherwise m is a unit, x,y are integral, y-x = j/m, so x = y mod 7 iff 7 | j. Residues: r = 4: n = 22 = 1, m = 13 = 6, 6^-1 = 6, x = 6; r = 5: n = 27 = 6, m = 16 = 2, 2^-1 = 4, x = 24 = 3; r = 6: n = 32 = 4, m = 19 = 5, 5^-1 = 3, x = 12 = 5. All lie in {3,4,5,6}, so for a positive multiple j of 7 (which needs r >= 8; the smallest members r = 4,5,6 have no such j, harmlessly) section B applies with k = 6,3,5 and no bound on v7(j). The parent's undecided table 0,1,2,3 / 0,2,4,6 / 0,2,4,5 minus its j = 0 column gives r4: 1,2,3; r5: 2,4,6; r6: 2,4,5, nine pairs. Each is an infinite congruence class of (r,j) (for instance r = 4+7t, j = 1 for every t >= 0), undecided by this argument; no class is claimed nonempty and none is an external open case. On those classes y = 6-j, 3+4j, 5+3j gives y residues 5,4,3 / 4,5,6 / 4,3,6, all in {3,4,5,6} and distinct from x, consistent with the parent's barrier. CONFIRMED.

## D. Diagonal, distinct residues, guard and scope

Exact diagonal j = 0: the two B equations coincide, so D_B = 0 is not a consequence; Q(x,x) = F'(x) is only a polynomial extension, and adding the exponent derivative would be a new equation, which the producer correctly declines; accepted single-contact existence survives. Distinct residues k != l in {3,4,5,6}: F(y)-F(x) = (y-x)Q with F(x) = F(y) = 0 mod 7 and y-x a unit, so Q = 0 mod 7, the constant of D_B is integral, and no strictly least term is guaranteed. This specific pole proof stops there; the producer claims no cancellation, residue point, lift or low-degree field, matching the root 17za qualification. Guard and nilpotents: a nonzero finite guarded 17w algebra has a maximal ideal whose number-field residue field carries the exact read-back of the four contact rows and W != 0; embedding into Q7bar, (I) and sections A-B contradict, so the algebra is the zero ring; valuations are used only in that field quotient, never on nilpotents. No source affine closure, Bezout certificate, point, F10 or JC2 statement appears (producer sections 1, 4, 5, 6.5, 7). CONFIRMED.

## E. Read scope and custody

All four hashes matched in the charged order before reading (23:14:03 UTC). Documentary text only: the producer's marker is standalone and unique in the read body; its Seal (body bytes 10558, 6650d5e0...) was not recomputed. Both my targets were absent at launch. Written: this report and box/f10-two-contact-same-residue-gate-fable5-20260909/READ-SCOPE.md only, via apply_patch. No provenance, corpus, ledger, peer, live gate, protected path, network, process or agent access; zero mathematical subprocesses, samples, code or data. Own WHOLE reread, raised-OPEN check and own-only collision check completed before the marker.

## OPENS RAISED

- NONE new. The producer's recorded gap stands: the nine residual congruence classes are not settled by the least-term mechanism, and this gate adds no mechanism, cost estimate or authorization.

## COLLISIONS

status: EMPTY

- NONE — own-only check: both owned targets were absent at launch (23:13 UTC) and are the only paths written. No corpus, ledger or provenance scan performed.

<!-- BODY-END -->
