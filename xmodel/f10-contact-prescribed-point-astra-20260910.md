# Exact exclusion of the surviving prescribed client (r,j)=(4,1)

2026-09-10. Astra producer; UNREVIEWED. First action 02:53:42 UTC;
fixed stop 03:10:00 UTC; publication reserve begins 03:08:00 UTC.
ZERO mathematical subprocesses, code or generated coefficient artifacts.

## 1. Outcome and scope

There is NO guarded paired contact for

    r=4, j=1, m=13, n=22, x=22/13, y=23/13.

This removes one actual client from the inherited nine-pair residue GAP.
It is a single exact finite-algebra certificate, not a new residue campaign:
the reduction modulo 11 below is justified by the accepted monic cubic,
then proved empty over EVERY residue-field extension. V and W may be
complex; no reality or rationality of these coefficients is assumed.

Other prescribed clients remain GAP, including (4,2) and (4,3). No all-r
contact exclusion, earlier forcing/companion conclusion or source/JC2
closure follows. No new prime/residue enumeration is proposed or authorized.

Exactly nine charged inputs were current-pinned before use: the assigned
ROOT-CARD and producer/gate pairs accepted17zn,17zi,17zj,17w. Full hashes
are in the owned PINS and terminal custody. The card and new 17zn gate were
read WHOLE after matching pins; earlier exact WHOLE reads were reused only
after current matching pins as expressly allowed. The accepted interfaces
and Root's specified sign/unit-chart/ordered-cover qualifications control.
No extra source, ledger, provenance or live report/code was read.

## 2. Why reduction modulo 11 is valid for complex coefficient points

The exponents above satisfy 5/3<x<y<2. Suppose a normalized contact point
existed. Accepted17w gives a monic cubic J(V) with V algebraic of degree at
most three over Q, and W a specified polynomial in V with rational
coefficients. Set k=Z_(11). We need, and check, that the SAME formulas have
coefficients in k for this exact rational pair.

Modulo 11 the denominator 13 is a unit and

    x=0, y=6, s=6, p=0, d=y-x=6,
    s-3=3,
    Gamma=36p+9s^2-114s+181=8,
    Omega=15s^2-36p-30s+35=10.                  (1)

Thus d,s-3,Gamma,Omega are 11-adic units. The accepted17w construction
uses only those divisions and rational numerical denominators whose
prime factors are among 2,3,5,7. Specifically P_X,Q_X, L and N give
W=12N/Gamma; R1=F1-E/(d*Gamma) and J=-(6Gamma/Omega)R1 is monic.
All coefficients of W(V) and J therefore belong to k at this pair.
No unknown U, V, W or generic leading coefficient is inverted in this step.

Consequently V is integral over k and W belongs to k[V]. The nonzero
subring A=k[V,W] of the coefficient number field is a FINITE k-module.
We do NOT invert W in A. If A/11A were zero, Nakayama over the local ring
k would give A=0, impossible because A contains 1 inside a field.
Thus A/11A is nonzero and has a field quotient K of characteristic 11.
The images of V,W in K satisfy the reduced four contact rows.

This argument applies to a complex algebraic point via its number field;
it is not a claim that V,W are rational or real. The field-degree bound is
not itself used as a residue-field restriction. Nor is the original guard
asserted to stay a unit modulo 11: x in (1) is zero there. We reduce the
literal normalized polynomial equations AFTER their exact characteristic-
zero read-back. Their unguarded special fibre is what will be excluded.

## 3. All four exact reduced rows and a unit W elimination

Use a_X=720A_X and b_X=5040B_X. Both numerical multipliers are units at
11. Substitution x=0,y=6 into the accepted integer quartics gives, in
F11[V,W],

    a_x=2V^3+2V^2+6V+10+(V+5)W+8W^2,
    b_x=10V^3+2V^2+10V+8+(V^2+8V+1)W+W^2,
    a_y=7V^3+4V^2+5V+2+(9V+10)W+8W^2,
    b_y=V^3+V^2+10V+(V^2+3V+6)W+W^2.          (2)

These are hand reductions of the literal coefficients, not sampled
evaluations. For example a_0's coefficients come from
120,-720,1080,-240,720,-1440,360; b_6's V,V^2,V^3,W,VW,V^2W,W^2
coefficients come from 252,2520,2520,1260,7560,2520,2520 respectively.

Put

    L1=a_y-a_x=P1+(8V+5)W,
    P1=5V^3+2V^2+10V+3,
    L2=b_y-b_x=P2+(6V+5)W,
    P2=2V^3+10V^2+3.

The exact combination 6(8V+5)+3(6V+5)=1 gives

    6L1+3L2=W+3V^3+9V^2+5V+5.

Hence every common zero satisfies

    W=8V^3+2V^2+6V+6.                           (3)

Neither individual linear W coefficient is inverted. The independent
cross-equation is retained:

    (6V+5)L1-(8V+5)L2
      =(6V+5)P1-(8V+5)P2
      =V^2(3V^2+2V+9)=0.                       (4)

The two combinations are globally valid, including zeros of either
individual coefficient and all W=0 branches. We do not claim that (3)-(4)
alone suffice for the original rows; a_x=0 is still imposed below.

## 4. Exhaustive obstruction, including all field extensions and nilpotents

Work in any field K of characteristic 11 satisfying the four rows. By (4):

- If V=0, equation (3) gives W=6 and the retained row is
  a_x=10+5*6+8*6^2=9, a contradiction in F11.

- Otherwise R(V)=3V^2+2V+9=0. Reduction modulo this polynomial gives

      V^2=3V+8,  V^3=6V+2,
      W=5V+5,   W^2=4V+5,
      a_x=2V+3.

  Thus a_x=0 forces V=4, but R(4)=3*16+8+9=10, another contradiction.

Both remaining constants 9 and 10 are nonzero. This covers all algebraic
and transcendental field extensions of F11, without enumerating only V in
F11. A field point with V=0 was checked separately; no factor V was simply
cancelled. The quadratic branch uses monic division after dividing by the
unit 3, and no root or discriminant branch was dropped.

Equations (3)-(4) also show that the full four-row quotient of F11[V,W]
is finite-dimensional (V satisfies a unit-leading quartic and W is a
polynomial in V). If it were nonzero it would have a maximal ideal and a
field point, which the two cases exclude. Thus it is the ZERO RING, with
nilpotents retained. In particular the nonzero field quotient K of A/11A
from section 2 cannot exist. The assumed characteristic-zero contact point
at (r,j)=(4,1) is therefore impossible.

## 5. Controls and relation to the accepted global pivot

The inherited c=0 slice already lies outside the prescribed exponent range.
The new certificate does not require inversion of c or U after reduction;
it excludes the whole unguarded coefficient fibre, even if a previously
inverted guard vanishes modulo 11. Thus all exceptional charts are covered
without claiming their inverses have good reduction.

Integrality is load-bearing: k[1/11] is nonzero but has zero mod-11 fibre;
it is not finite over k. This changed object shows why the checked monic
J and polynomial W, followed by the finite-module argument, cannot be
replaced by an informal reduction of arbitrary complex coefficients.
Keeping the cross-equation (4) and the final a_x row is also essential;
eliminating W alone does not prove the four-row fibre empty.

Only this exact rational pair has been certified. The calculation is not
being extrapolated into another congruence table or a new residue farm.

## OPEN(S) RAISED

- ASSIGNED GAP ONLY; no new canonical ID: the other prescribed finite
  contact clients remain unclassified. The exact (4,1) client is excluded;
  no broader all-r or source conclusion, review launch, or follow-on
  execution is authorized by this report.

## COLLISIONS

status: EMPTY FOR THE NEW FIXED-CLIENT CERTIFICATE

- The inherited nine-pair residue boundary was retained as given; it was
  not rederived. The chosen (4,1) client lies among those surviving pairs.
- Own targets were ABSENT at first action. No corpus/history scan or extra
  source read occurred. No claim of all-corpus novelty is made.

Own WHOLE report/PINS and own-only OPEN/collision checks completed at
2026-09-10 03:04:22 UTC. All mathematics was manual; no mathematical
subprocess, new source read, or downstream action occurred. Terminal
custody and independent ROOT review remain required before any promotion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7856`.
- Body SHA-256:
  `f6e66f8b5a30575adedab916e7c2c80d622f673cef31e835e5d464e3adde2fd5`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
