# The final ell column is unimodular for every r>=2

ROOT/Astra manual theorem, NOT PROMOTED. Recorded source/derivation check
08:25:30 UTC, publication begin08:26:41; conservative hard stop08:35 UTC,
final2min reserve. No scientific execution. This is a new composition of
accepted16r,17zz,17zzd, not a new source-exclusion theorem.

## 1. Exact statement and accepted interfaces

Fix integer r>=2, m=3r+1, n=5r+2, q=n-m=2r+1. In accepted16r retain

    A=S*t^3+f*t^2+h*t+k,
    f=S*d-u, h=1-u*d+S*v,
    deg d<=r, deg v<=2r, deg k<=m, k(0)=0.

The full mate is reconstructed by the five Euler inversions, with B5=S^2,
[S]B3=B0(0)=0, and full residuals

    R1=2k'*B2+h'*B1-h*B1'-2f*B0'-u,
    R0=k'*B1-h*B0'-1.                                  (1)

Primes in (1) are S derivatives. Impose the whole leading equations and
guard, so the accepted leading coefficient algebra L acts on the actual
coefficient base. Its C(theta)=theta^3+F*theta^2+H*theta+a and degree5
mate Dlead obey m*C*Dlead'-n*C'*Dlead=-theta^7, with a,b units.
Here F=d_r,H=v_(2r),a=k_m. Do not set any lower source parameter to zero.

Accepted17zz gives L=B_nu[s,s^-1], nu=n/m, with s=H/a a unit,
c(z)=1+z+V*z^2+W*z^3, C/a=c(s*theta). Accepted17zzd proves that

    Dden(V)=12V^2-12(1-tau)V+(1+tau)(2-3tau),
    tau=r/m=2-nu,                                      (2)

is a unit of the ENTIRE B_nu, hence of L and every base change. This is
the polynomial called D in17zzd, NOT Dlead. Formula(2) follows also by
expanding its displayed identity D=e+(V-v*)J, where
v*=3(1+tau)/14, e=(1+tau)(6tau-1)/49,
J=12(V+v*)+12(tau-1). No new middle-unit or residue theorem is used.

THEOREM. The coefficients of ell in the two actual residual rows
[S^(3r+1)]R1 and [S^(4r+1)]R0 generate the unit ideal in L. Therefore
ell admits an exact whole-ring elimination using those TWO rows and a
retained compatibility, with every other source equation substituted.
This is not a claim that either entry alone is a unit, that forcing is
outside the column image, or that the complete source ideal is zero.

## 2. The whole ell variation and its leading two rows

Differentiate the16r Euler recurrence coefficientwise with respect to ell,
holding all A coefficients and u fixed. The target derivative is -t*Pi,
Pi=t-u*t^2+S*t^3. The j=4,3 equations and fixed gauges give

    dotB5=dotB4=dotB3=0, dotB2=S,
    dotB1=-u+S*Jd,
    Jd=sum_(i=0)^r [2i/(3i+2)] d_i S^i.                (3)

Indeed E2(S)=-S; the j=1 forcing is
u-2S*f'+2f=-u-2S^2*d'. With G=dotB0 and G(0)=0, j=0 gives exactly

    -3S*G'=-1-f'*(-u+S*Jd)+2f*(S*Jd)'
               -2S*h'+h.                             (4)

Its constant coefficient is -1+u*d0+h(0)=0. Thus G is a polynomial,
deg G<=2r+1, by rational Euler division. No division by u or a source
boundary coordinate occurs. These derivatives are independent of ell.
The full recurrence is linear in the mate with an affine target, so
B=B^0+ell*dotB is an exact identity, not a first-order approximation.
Since deg G<=2r+1<n, the top guard is also ell-independent.

Put j0=2r/(3r+2), and

    g=((4r+1)H-(r+1)j0*F^2)/(3q),
    Q(theta)=theta^2+j0*F*theta+g.                     (5)

Equation(3) has top dotB1 coefficient j0 F. The coefficient S^(2r+1)
of (4)'s right side is (r+1)j0 F^2-(4r+1)H, proving the formula for g.
Thus Q is exactly the weight-(2r+1) leading ell-mate variation.
From the FULL residual derivatives

    dotR1=2S*k'+h'*(-u+S*Jd)-h*(S*Jd)'-2f*G',
    dotR0=k'*(-u+S*Jd)-h*G',                           (6)

we obtain deg dotR1<=3r+1, deg dotR0<=4r+1 and top coefficients

    L1=2m*a+r*j0*F*H-2q*F*g,
    L0=m*a*j0*F-q*H*g.                                (7)

Consequently every higher residual row is ell-independent. Direct
coefficient multiplication, now with theta derivatives, gives

    m*C*Q'-q*C'*Q=-theta^4+L1*theta+L0.               (8)

The theta4 coefficient is 2m-3q=-1. The theta3 coefficient is
2rF-(3r+2)j0F=0; theta2 is
(4r+1)H-(r+1)j0F^2-3qg=0. The remaining two coefficients are exactly(7).
This checks the target sign and the association with the actual rows,
not merely an abstract cubic/quadratic differential equation.

## 3. The unit argument, including a possibly nonreduced quotient

Work in R=L/(L1,L0); no field or nonemptiness is assumed. The polynomial
combination of(7) is

    m*a*L1-r*H*L0
      =2m^2*a^2+q*(r*H^2-2m*a*F)*g.                  (9)

Since a is a unit, in R this makes g a unit, with inverse
q*(2m*a*F-r*H^2)/(2m^2*a^2). In particular no g=0 branch was dropped.
Set beta=q/m=nu-1=1-tau, so beta and beta-1 are nonzero rationals.
Equation(8), divided in R[[theta]] by the unit series m*C*(C/a)^beta,
gives

    (Q/(C/a)^beta)'=-theta^4/[m*C*(C/a)^beta].

Formal integration over a Q-algebra is coefficientwise valid, including
nilpotents. Q(0)=g therefore gives Q=g*(C/a)^beta+O(theta^5).
Since deg Q=2, its theta3,theta4 coefficients vanish. Using C/a=c(s*theta)
and units g,s, we get t3(beta)=t4(beta)=0 in R, where ti(X)=[z^i]c(z)^X.

The two finite binomial coefficients are

    t3(beta)/beta=W+(beta-1)V+(beta-1)(beta-2)/6,
    t4(beta)/(beta*(beta-1))
       =W+V^2/2+(beta-2)V/2+(beta-2)(beta-3)/24.

Subtracting yields the EXACT polynomial identity

    24*(t4(beta)/(beta*(beta-1))-t3(beta)/beta)
       =12V^2-12beta V+(beta-2)(1-3beta)=Dden(V).       (10)

Hence the image of Dden is zero in R. But Dden is a unit of L by accepted
17zzd, so its image is a unit and R is the zero ring. This proves
(L1,L0)=L, not merely an assertion on reduced or generic components.
The proof uses neither septic irreducibility, a real-root assumption,
any h-congruence theorem, nor full-source properness.

## 4. Exact source elimination and what it does not prove

Choose p1,p0 in L with p1*L1+p0*L0=1, whose existence is proved above.
No coefficients of these Bezout multipliers have been computed or emitted.
They are elements of L before imposing source forcing, and thus survive
every actual coefficient-base quotient. Let that ell-independent base be A0,
retaining all higher equations and any other chosen earlier compatibilities.
The two selected full residual rows are

    L1*ell+c1, L0*ell+c0,

where c1,c0 are their actual ell=0 values after EXACT previous substitutions.
The matrix with rows (p1,p0),(-L0,L1) has determinant1. Hence their ideal is
exactly

    (ell+p1*c1+p0*c0, Psi), Psi=L1*c0-L0*c1.            (11)

For the full list of other residuals Ri(ell), the complete quotient is
isomorphic to A0/(Psi, Ri(ell_star) for EVERY other row), where
ell_star=-p1*c1-p0*c0. Forward map substitutes ell_star, backward map
retains all remaining coefficients; (11) proves both compositions.
This is valid over arbitrary Q-algebras, including nilpotents and zero rings.
If earlier triangular maps are used, they consume rows strictly above the
bounds in(6), so those maps may be taken ell-independent. No late or low row
is silently removed. One compatibility remains in place of the pair.

The source scale s is still invertible and free as a coefficient coordinate;
nothing here sets s=1 in the full source. The original guard remains encoded
by L and carried through every base change. The auxiliary g becomes a unit
only inside the contradiction quotient; it is NOT a new source guard.

Unlike the old unreviewed two-CONSTANT-row candidate whose obstruction lies
in(u), this uses the two HIGHEST ell-dependent rows. That old packet is
not a premise. No claim that u is a unit or that its boundary is empty is
needed. Crucially (11) does not make Psi a unit. Even an everywhere nonzero
column has a nonempty affine solution when forcing lies in its image.
Full source exclusion requires the remaining compatibilities/forcing.

## 5. Changed-object controls and independent cross-check

1. Without the full leading Dden-unit relation the conclusion fails even
with a,H nonzero. At r=2 take F=14,H=49,a=49, so j0=1/2,q=5,g=49/5.
Then L1=F^3-5FH+14a=2744-3430+686=0 and
L0=(7/2)aF-3H^2+(1/2)HF^2=2401-7203+4802=0.
Normalized s=1,V=2/7,W=1/49 gives Dden=0. This is an explicit changed
cubic, not an allowed complete leading pair or source solution; by the
accepted Dden theorem it cannot satisfy the entire guarded leading system.
It shows that merely retaining a,H units would not justify elimination.
2. Dropping Psi in(11) is invalid even for column(1,0) and forcing(0,1):
the first row fixes ell=0, but the retained second row is1. The proposed
source maps retain Psi and every other row, avoiding this false solution.
3. Treating B^0 as the whole mate would drop (3)-(6). In particular it
would incorrectly erase dotB2=S and the nonzero leading target -theta^4.
4. No standalone field-point argument is hidden: (9) gives a polynomial
inverse to g modulo the entire column ideal, then(10) kills that entire
quotient by an already proved unit. Nilpotents therefore cannot survive.

ROOT sent the exploratory formulas to the independent r2 source-transfer
Astra lane after it had already derived its five-coordinate/twenty-slot
contract. That lane reported an independent r2 check from its already
charged accepted inputs: Q=theta^2+(F/2)theta+(6H-F^2)/10 and the same
unit argument. Its live body was not read; its acknowledgment is NOT a
different-model review or premise here. This ROOT theorem covers all r>=2.
FIRST Fable review is still required before any promotion or compute.

## 6. Read scope, exact pins and remaining work

Scientific premises are ONLY the following six accepted report/gate objects:

- xmodel/f10-whole-mate-euler-elimination-astra-20260909.md SHAa5ab487c4619742b6252e2503488eea4d6e927b58fd2821207cc85bcba7cf8d5
- xmodel/f10-euler-complete-presentation-gate-fable5-20260909.md SHA77d59f7b54e545d6a05f61ab270739c1498f93eed5d155e40222cecdc96c0a8c
- xmodel/f10-middle-resonance-unit-astra-20260910.md SHA8cf54b2f78840ced62fd35722da6d0d969eedd3344aa07d4ab08ff62c50df012
- xmodel/f10-middle-resonance-unit-gate-fable5-20260910.md SHAdc43ef1cfba68da21d0e26f6422e6af626d15a75d551858e72e78c7236ac27ad
- xmodel/f10-middle-univariate-unit-astra-20260910.md SHA890e5c9c63a333bf873e963821c368d2dc080476eaf12c9fc6a10dce53db75e5
- xmodel/f10-middle-septic-gate-fable5-20260910.md SHAcff18a06c050d64074ba9af70cea61b28b15614a61691125ebf26d3012577c62

All six hashes matched before new derivation (r2 invitation vector).
Current WHOLE rereads of16r producer/gate and17zzd producer; explicit
same-byte prior WHOLE reads reused for17zz producer/gate and17zzd gate.
Inherited accepted-premise/source-import qualifications remain; none is
newly re-hardened here. The17zzb producer was also reread for orientation,
but(2) was reconstructed above from the charged17zzd identity and needs
no additional uncharged formula premise. All new coefficient algebra in
sections2-5 was performed by hand. No live peer report/log/receipt was read.

No scientific subprocess, coefficient artifact, source code, CAS, import,
syntax/test/AST, network or AWS execution for this proof. Only text, hashes,
metadata, apply_patch and the existing publication transaction were used.
No new OPEN ID. The existing remaining quantity is the full source quotient
after all retained substitutions; the cheapest next interface is the bounded
r2 whole-row contract already independently assigned. A future implementation
must supply explicit Bezout multipliers and check full inverse identities;
this report gives no executable cofactor, cost estimate or run authority.

COLLISIONS: EMPTY (own report; distinct target, no shared proof file edited).
No assertion of source nonemptiness, source exclusion, an all-r degree bound,
or a proof/counterexample to JC2. Own WHOLE/OPEN/collision check precedes the
completion marker and the unchanged08:35 cap.

Own WHOLE read and hand sign/degree/unit/control recheck completed08:30 UTC;
all six current scientific input hashes matched again before completion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11851`.
- Body SHA-256:
  `af221afef39829a79c6ef02e92f8af741c5b1357af18ea50bc394bbbd4f258c1`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
