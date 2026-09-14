# F10 r=1 constant-h obstruction using the full upper rows

2026-09-09. NEW/PROVISIONAL manual proof, for independent review. Basis `0d39df3c9fd69c939a8420c54d03228b9077777d` is provenance only. ZERO mathematical subprocesses. First exact local timestamp/current-pin check12:11:02 UTC; conservative stop12:22 UTC within root's earlier-of-actual+12min/12:24 bound.

## 1. Exact result, not a whole-system exclusion

Over every characteristic-zero field, the accepted complete normalized F10 system at r=1 has NO point with h(S) constant. This includes h=0, all u and ell, and every allowed scalar mate shear/translation. The proof uses both FULL low identities and particular coefficients of the FULL upper equations. It independently derives the low-row identity; the earlier provisional low-degree theorem is not a premise.

For r>=2 a short independent degree comparison of the two low rows already excludes constant h. Thus, combining the two arguments, every hypothetical point of the accepted complete system for ANY r>=1 must have NONCONSTANT h. This does not prove that any nonconstant-h point exists, exclude all r=1 points, or exclude F10. No emitted ideal, unit certificate, coefficient builder, point or counterexample is supplied. No change to a complete builder or gauge is authorized before independent review.

Only the three WHOLE current-pinned inputs in the owned PINS.json/READ-SCOPE.md were read: accepted16r Euler producer and gate, and accepted16q module. Their exact accepted source/field equivalences are retained. No live low-residual gate, other peer, blind, mutable ledger or source follow-through was read.

## 2. Retained normalized system and whole-row formula

Let K have characteristic zero. At r=1 the exact normalized objects are

    A=S t^3+f(S)t^2+h(S)t+k(S),
    B=sum_(j=0)^5 Bj(S)t^j,         B5=S^2,
    [A,B]_(S,t)=Delta,

where

    p=t-u t^2+S t^3,
    Delta=1+u t-ell*t*p-t*p^2,
    f=S d-u,         h=1-u d+S v,
    deg d<=1,        deg v<=2,
    deg k=4,         a=[S^4]k !=0,
    deg B0=7,        b=[S^7]B0 !=0,
    deg Bj<=7-j.

The nonzero top-product guard is retained. The two S-leading coefficients a,b are not both normalized to one after the accepted output scalings. Both inverse-polynomiality conditions are part of the complete system; the module interpretation is unchanged.

Write primes for S derivatives. The exact two low rows are

    k' B1-h B0'=1,
    2k' B2+h' B1-h B1'-2f B0'=u.                (1)

The full upper coefficient formula is

    (j-3S*d/dS)Bj = Qj,                         j=4,3,2,1,0,
    Qj=delta_(j+2)
       -(j+1)f' B_(j+1)+2f B'_(j+1)
       -(j+2)h' B_(j+2)+h B'_(j+2)
       -(j+3)k' B_(j+3),                       (2)

with higher B indices zero and

    (delta0,...,delta7)
      =(1,u,-ell,ell*u-1,2u-ell*S,-u^2-2S,2uS,-S^2).

One can rederive (2) directly: the contribution of Ai(S)t^i and Bl(S)t^l to their bracket is `(l Ai' Bl-i Ai Bl')t^(i+l-1)`. The A3=S term gives the displayed diagonal operator; moving the other three A terms to the right gives every term and sign of (2). Thus no theorem rename or source leading-form replacement is used here. All upper equations and lower coefficients remain required; the contradiction below needs only a subset of their exact consequences.

## 3. What constant h forces from the ENTIRE low rows

Assume h=H is a scalar. If H=0, the first row of (1) gives k'B1=1, impossible because deg k'=3. Hence H!=0, without dividing u or imposing a boundary open set.

Put N=B1. Since deg B0'=6 and b!=0, the first row of (1) implies

    deg N=3,             4a*nu=7H*b,
    nu=[S^3]N !=0.                                      (3)

Multiplying the second row by H and using H B0'=k'N-1 gives the exact identity

    2k'(H B2-fN)=H^2 N'-2f+uH.                          (4)

The right side has degree at most2. Since k' has degree3, (4) forces BOTH

    H B2=fN,             H^2 N'=2f-uH.                 (5)

The leading coefficient of N' is3nu!=0. Therefore f has degree exactly2. Set

    d1=[S^2]f=[S]d !=0.                                (6)

This settles the d1=0 case before any cancellation by d1. For the source parametrization, writing d=d0+d1S, constant h means

    H=1-u*d0,      v=u*d1

(the higher coefficients of v vanish). There is no assumption u!=0: at u=0 one has H=1 and v=0, still covered literally. The lower coefficients of k, d, B and the parameter ell remain free subject to the complete equations.

## 4. Exact highest coefficients from the full upper equations

Define scalar coefficients, not guessed leading terms,

    e1=[S^3]B4,
    C=[S^4]B3,
    D=[S^5]B2.

The upper bounds are deg B4<=3, deg B3<=4 and deg B2<=5. Each comparison below explicitly checks all tied terms.

### 4.1 The j=4, S^3 row

Its left side is `(4-9)e1=-5e1`. On the right only `-5f'S^2+2f(2S)` reaches degree3: its coefficient is `-10d1+4d1=-6d1`. The target delta6=2uS is lower; all further B terms vanish. Hence

    e1=6d1/5.                                           (7)

### 4.2 The j=3, S^4 row

The left coefficient is `(3-12)C=-9C`. The two f terms give

    -4(2d1)e1+2d1(3e1)=-2d1e1.

Here h'=0; hB5'=2HS has degree1 and delta5=-u^2-2S also has degree1. There is no k term since B6=0. Therefore

    C=2d1e1/9=4d1^2/15 !=0.                            (8)

### 4.3 The j=0, S^7 row

The left coefficient is -21b. By (3), the f terms involving N have degree at most4, h'=0 and hB2' has degree at most4. The target delta2=-ell is constant. Only `-3k'B3` reaches degree7, with coefficient -12aC. Thus

    b=4aC/7,
    nu=H*C,                                             (9)

where the second equality uses (3). These divisions are by nonzero rational scalars and a; the nonzero a is already part of the actual guard.

Now the first identity of (5), at S^5, gives

    H D=d1*nu,      hence D=d1*C !=0.                  (10)

### 4.4 The j=2, S^5 row

The left coefficient is `(2-15)D=-13D`. The two f terms contribute

    -3(2d1)C+2d1(4C)=2d1C.

The h' term is zero, hB4' has degree at most2, and delta4=2u-ell*S has degree at most1. The remaining term `-5k'S^2` contributes -20a. Consequently

    13D=20a-2d1C.

Substituting (10) gives 15d1C=20a. By (8),

    d1^3=5a.                                            (11)

### 4.5 The j=1, S^6 row

The left coefficient is ZERO: the full low row already forced deg B1=3 in (3), despite its original envelope6. This is the essential use of the low equation, not a silent support cut.

On the right the two f terms contribute

    -2(2d1)D+2d1(5D)=6d1D.

The term h'B3 vanishes and hB3' has degree at most3; delta3=ell*u-1 is constant. The remaining term `-4k'B4` contributes -16a e1. Therefore

    6d1D=16a e1,       D=16a/5,                         (12)

using (7) and the already established d1!=0. With (8),(10), this instead gives

    d1^3=12a.                                           (13)

Equations (11),(13) imply 7a=0, contrary to characteristic zero and a!=0. This is the required full-upper/low contradiction.

## 5. Gauges, all scalars, and exact exclusion scope

No coefficient of the target involving u or ell was discarded without an explicit degree check in section4. No zero/nonzero case of u was omitted. H=0 and d1=0 were separately settled in section3, and every remaining cancellation is by a scalar proved nonzero. There is no squarefree, generic-root, real-field, algebraic-closure or nilpotent-base degree assumption.

The mate change B->B+beta*A+gamma does not affect b,e1,C,D or nu: its respective degrees in B0,B4,B3,B2,B1 are at most4, absent,1,2,0 under constant h. It also leaves H B2-fB1 invariant. The A constant translation changes no derivative or highest coefficient. Thus the proof covers the entire accepted scalar gauge orbit, not only the chosen beta=gamma=0 representative. No polynomial-in-S shear is introduced.

The argument is over any characteristic-zero field and uses the accepted source normalization over that same field; no extra embedding or field extension is required. Its conclusion excludes precisely the constant-h sublocus of the complete normalized client. It does not normalize h=1, replace h by a nonconstant polynomial, assume any particular nonconstant degree, or alter the complete equation set.

## 6. Rechecked low-compatible negative control and its exact upper failure

To verify that the new contradiction genuinely uses upper rows, independently take r=1,u=ell=0 and the following scalar-polynomial data:

    d=S, v=0, f=S^2, h=1, k=S^4,
    B0=(8/21)S^7-S^4-S,
    B1=(2/3)S^3-1,
    B2=(2/3)S^5-S^2,
    B3=(2/3)S^4, B4=0, B5=S^2.                        (14)

All degree bounds and the nonzero a=1,b=8/21 hold; k(0)=B0(0)=[S]B3=0. The whole inverse boundaries hold because at u=0, p=t+St^3 and y=St^2,

    A=k+p+S*y,
    B=B0+B1*p+((2/3)S^4-S+p)*y

are in the accepted common ring. Directly B0'=k'B1-1, B2=fB1 and B1'=2f, so BOTH entire low rows (1) hold.

But the t^6 coefficient of [A,B]-Delta is

    5f'B5-2fB5'=6S^3 !=0,

because B4=0 and delta6=0. Equivalently it fails (7): d1=1 but e1=0. Thus (14) is explicitly NOT an Euler-reconstructed mate, full compact point or source/Keller point. Retaining only the low rows, even with all these degree/boundary/gauge/nonzero-top conditions, cannot prove the new exclusion.

A changed-object hand check is to replace B2 by B2+1: E0 stays zero and E1 becomes 2k'=8S^3, so even the low compatibility is lost. No polynomial pair was expanded by a program, and no old checker or previous provisional report was used as evidence.

## 7. Independent completion of the constant-h scope for r>=2

Within the same bounded task, this case does not require another upper-row analysis. Keep the accepted general bounds m=3r+1,n=5r+2 and a*b!=0, and assume h=H constant. Again H=0 would give k'B1=1 and is impossible. For H!=0 the full E0 gives deg B1=2r+1; in particular its derivative has exact degree2r with nonzero leading coefficient.

Independently multiplying full E1 by H and eliminating H B0' gives exactly

    2k'(H B2-fB1)=H^2 B1'-2f+uH.                     (15)

For r>=2 the right side has exact degree2r, since deg f<=r+1<2r. It is nonzero, but (15) makes it divisible by k', of degree3r. This is impossible. The proof is uniform, uses no earlier low-degree theorem, and includes u=0 unchanged.

Together with sections3–4, constant h is therefore impossible for every r>=1 in the complete accepted client. For u=0 this implies v!=0 because h=1+Sv; for arbitrary u it says exactly that 1-u*d+Sv is nonconstant. It is not an equation permitting a new normalization or a claim that the nonconstant-h sublocus has points.

## 8. Terminal status

The root scratch's scalar comparisons are confirmed by independent coefficient accounting: the incompatible requirements are d1^3=5a and d1^3=12a. The new theorem remains PROVISIONAL pending independent review. Its only accepted parents are the three pinned files; it does not depend on the pending low-degree lemma, any live reviewer or a fixed-A/source-realization assertion.

No full F10, r=1 or JC2 exclusion follows; no literal unit, properness or point is claimed. No builder changes, solver authority, review launch, descendants or continuation follow from this report. All mathematics was manual. Only permitted text reads, hashes and owned documentary publication ran; no mathematical subprocess of any size, CAS, web, AWS/SSH, shared edit or protected-project access occurred. Own whole-body and raised-OPEN checks precede sealing; terminal custody records current pins and all writers idle.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN extraction; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11697`.
- Body SHA-256:
  `e05a71c6a968a07cf929480f2ce25e1c9618a0a9d2edec2ccda175c63727f6a0`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
