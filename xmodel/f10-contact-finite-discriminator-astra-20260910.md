# A global quadratic-remainder unit on the generic contact chart

2026-09-10. Astra producer, UNREVIEWED. First action 02:11:19 UTC;
fixed stop 02:29:19 UTC; publication reserve begins 02:27:19 UTC.
ZERO mathematical subprocesses, code or generated coefficient artifacts.

## 1. New result, scope, and unchanged limit

On the ENTIRE accepted17zi guarded chart R[(3V-1)^-1], the quadratic
remainder coefficient U below is a UNIT. The whole U=0 divisor is empty,
including its exceptional V values. This is proved by explicit polynomial
factors and the remaining constant-row obstruction; U is not assumed
generically nonzero. The result licenses a single global quadratic pivot
on that chart, with nilpotents retained.

The prescribed rational-exponent exclusion remains GAP. This report does
not identify all finite points or close contact/source/JC2. The c=0 slice
is exactly the already accepted17zi three symmetric/six ordered points;
it is retained as a separate chart, not treated as a domain of U.

Exactly seven charged inputs, current-pinned before use, are listed with
full hashes in the owned PINS. They are the assigned ROOT-CARD and the six
specified accepted17w/17zi/17zj producers and first gates. The new card and
17zj gate were read WHOLE; prior same-byte WHOLE reads were reused only
after matching current pins as expressly allowed. Root's stated Cramer-sign,
u-unit-chart, ordered-cover lying-over and three/six-point qualifications
control. No extra source or linked provenance was read.

## 2. Explicit polynomials and a new factored identity

Let a=720A_X=X^4+a3 X^3+a2 X^2+a1 X+a0 and b=5040B_X be the literal
accepted17zi quartics. Put c=4-12V and, on the c-unit chart,

    h=(a-b)/c=X^3+uX^2+vX+w,
    U=a2-v-a3*u+u^2,
    T=a1-w-a3*v+uv,
    Z=a0+(u-a3)w.

Thus a=(X+a3-u)h+UX^2+TX+Z. No normalization of an unknown nonunit is
performed; c is inverted only on the explicitly assigned chart.
For a reproducible hand expansion write

    d=-48+234V-240V^2-90W,
    e=188-1194V+2040V^2-720V^3+(870-1800V)W,
    f=-240+1800V-3960V^2+2280V^3
      +(-1800+6120V-2520V^2)W-2160W^2,
    g=d-c*a3=8-54V+120V^2-90W.

Here u=d/c,v=e/c,w=f/c. Hence the numerator identities are

    c^2 U=c^2*a2-c*e+d*g,
    c^2 T=c^2*a1-c*f+e*g,
    c^2 Z=c^2*a0+f*g.                              (1)

Expanding the first two of (1) manually and dividing by the rational unit
60 gives the following ACTUAL polynomials, denoted U0,T0:

    U0=c^2 U/60
      =135W^2+2(54V^2-84V+17)W
         +3V(1-4V)(16V^2-13V+2),

    T0=c^2 T/60
      =27(84V-43)W^2
         +(-206+1152V-900V^2-1296V^3)W
         +3V(1-4V)(96V^3-212V^2+107V-14).           (2)

Their exact first W-elimination is the useful small factorization

    5T0-(84V-43)U0
      =48(1-4V)(1-3V)^2*[9W+V(1-6V)].             (3)

For coefficient checks of (3), the W coefficient on the left is
432(1-10V+33V^2-36V^3)=432(1-4V)(1-3V)^2; the constant is
48V(1-4V)(1-3V)^2(1-6V), and the W^2 coefficient cancels exactly.
Also direct substitution into the displayed U0 gives

    U0(V,V(6V-1)/9)=(20/9)V(1-3V)^3.              (4)

No resultant, software expansion or generic coefficient inversion is
behind (2)-(4); they are finite hand identities.

## 3. Every case on U=0, and the scheme-theoretic unit conclusion

Work in R_c=R[c^-1], with the ENTIRE original guard G still inverted.
The common q=X^2-sX+p divides both a and h. Therefore it divides
UX^2+TX+Z. Modulo U=0, monicity and degree of q force T=Z=0 as exact
coefficient equations, over arbitrary rings. It remains to show that
R_c/(U) is zero.

Suppose this finite Q-algebra had a field point. Its c and W are nonzero.
Equations U=T=0 imply U0=T0=0. Since 1-3V is nonzero, (3) gives precisely
two possibilities, with their overlap retained:

1. 9W+V(1-6V)=0. Equation (4) then forces V=0 or V=1/3. The latter
   is outside this chart; the former forces W=0, forbidden by G.

2. V=1/4. The displayed U0 becomes

       U0=(5/4)W(108W-1).

   Since W!=0, W=1/108. At this pair c=1 and the literal coefficients give

       a3=-13/2,     u=-16/3,       w=-325/54,
       a0=2305/324,  u-a3=7/6,
       Z=a0+(u-a3)w
        =(2305-2275)/324=5/54 != 0.               (5)

   This contradicts the retained row Z=0. For direct checks: a0 is
   15/4+360/108+360/108^2=2305/324, while
   w=-15/8-(855/2)/108-2160/108^2=-325/54.

These cases exhaust every field point; no assumption that V or W is real
or rational was made. Accepted17zj makes R_c/(U) finite-dimensional over Q.
If it were nonzero it would have a maximal ideal and a field point, contrary
to the two-case proof. Thus R_c/(U)=0, or equivalently (U)=R_c:

    U is a UNIT in the entire R_c, with nilpotents retained.             (6)

This is a unit conclusion about the ring, not merely a count of reduced
roots or nonvanishing on one component. The original guard is still

    G=W*p*(p-s+1)*(9p-15s+25)*(p-2s+4)*(s^2-4p)
      *(s-3)*(4-s)*(36p+9s^2-114s+181)
      *(15s^2-36p-30s+35).

Only the already prescribed c-unit chart and the W factor of G were needed
in the exclusion; every other G factor is retained. No further divisor was
inverted. The separate c=0 slice remains exactly as accepted17zi states.

## 4. Licensed read-back and meaningful changed-object control

Since U is now proved a unit, q is globally the monic normalization of the
quadratic remainder on R_c:

    q=X^2+(T/U)X+Z/U,          s=-T/U, p=Z/U.

The two remaining coefficients of q|h are exactly

    UZ-T^2+uUT-vU^2=0,
    uUZ-TZ-wU^2=0.                                  (7)

Conversely, with c,U and the substituted G units, (7) gives
h=q(X+u-T/U), and a=(X+a3-u)h+Uq; hence q divides a,b and recovers all
four symmetric rows. These are the original chart's exact equations,
now with a justified GLOBAL pivot. Their further elimination or prescribed
point verdict is not established here; the schematic equations (7) alone
are not claimed as the new advance. The new content is (2)-(6).

The W guard is essential. Drop ONLY W from it and take V=W=0, x=3,y=4
(s=7,p=12). Then a=(X-2)(X-3)(X-4)(X-5),
b=(X-3)(X-4)(X-5)(X-6), and h=(X-3)(X-4)(X-5).
Thus U=T=Z=0 and q=(X-3)(X-4) divides both quartics. All other guard
factors survive: Delta=1, Gamma=256, Omega=128, and neither exponent is
0,1,5/3 or 2, with s!=3,4. This is an exact countercontrol to extending
the unit statement over W=0, not a point of the actual guarded problem.
Likewise dropping Z=0 at the pair (1/4,1/108) would defeat the contradiction
(5); U=T alone is insufficient.

## OPEN(S) RAISED

- ASSIGNED GAP ONLY; no new canonical ID: exclude/classify the remaining
  finite guarded generic points at the prescribed rational exponents.
  This report proves the global U pivot but no such final exclusion,
  enumeration, all-r source implication or JC2 closure. No follow-on work
  is authorized by publication.

## COLLISIONS

status: KNOWN DUPLICATE ABANDONED; NEW OWNED CLAIM AS ABOVE

- Root supplied collision context that the exploratory 7-adic nine-pair
  residue exclusion is already accepted17y/17za/17ze. That duplicate route
  was stopped and is not a new claim or proof premise here. No additional
  source was read. The report records only the new explicit U-divisor proof.
- Own report and box were ABSENT at first action. No corpus or history scan.

Own WHOLE report/PINS and own-only OPEN/collision checks were completed
at 02:25:31 UTC. All mathematics was manual; no mathematical subprocess
ANY size, code/coefficient artifact, network/AWS/SSH/process/agent,
corpus/live/shared/protected/Git or frozen-file work occurred. Only owned
apply_patch documentary writes and the existing publication transaction
were used. Root retains custody and any FIRST different-model gate;
this producer grants no promotion or follow-on authority.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7794`.
- Body SHA-256:
  `5373cb1b7ace584e7072451049ad580c596234e51699e3bbf37def87b0401037`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
