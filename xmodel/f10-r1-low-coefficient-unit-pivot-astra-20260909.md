# F10 r=1: an all-strata low-coefficient unit pivot

2026-09-09. NEW/PROVISIONAL manual algebra, for independent review. Basis0d39df3c9fd69c939a8420c54d03228b9077777d is provenance only. First exact local timestamp/current-pin check12:27:42 UTC; conservative controlling stop12:42 UTC. ZERO mathematical subprocesses.

## 1. Result and scope

There is a genuine global polynomial pivot, not a generic division by the coefficient of k1. One combination of the two LOW S-constant rows is affine-linear in (k1,k2), with a unimodular coefficient row. An explicit determinant-one change of these two parameters turns it into a coefficient-ONE equation, which removes one coordinate while preserving every stratum, including u=0 and the vanishing of its apparent k1 coefficient.

This yields a polynomial-quotient isomorphism from the accepted complete r=1 ideal L1 in12 variables/at most20 coefficient slots to an explicitly defined ideal in11 variables/at most19 slots. Every other row, the entire reconstructed mate and the exact top-product guard are substituted, not projected or dropped. The new coordinate is a polynomial linear combination of k1,k2, not a new source gauge. No coefficient is normalized, and no performance improvement, point, properness, unit or source exclusion is claimed.

Only accepted16r Euler producer/gate and accepted16q module were pinned before WHOLE reads. The current hashes and read perimeter are in the owned PINS.json/READ-SCOPE.md. No newer degree theorem or live gate is a premise. In particular maximal degree of h is not assumed.

## 2. The fixed complete system

Set r=1,m=4,n=7. Use the accepted normalized polynomials

    A=S t^3+f(S)t^2+h(S)t+k(S),
    B=sum_(j=0)^5 Bj(S)t^j,       B5=S^2,
    f=-u+d0*S+d1*S^2,
    h=H0+H1*S+H2*S^2+H3*S^3,
    H0=1-u*d0, H1=v0-u*d1, H2=v1, H3=v2,
    k=k1*S+k2*S^2+k3*S^3+k4*S^4.

The independent variables are u,ell,d0,d1,v0,v1,v2,k1,k2,k3,k4,omega. The entire mate is the accepted polynomial Euler reconstruction with [S]B3=0 and B0(0)=0. Its recursion is

    (j-3S*d/dS)Bj=delta_(j+2)
       -(j+1)f'B_(j+1)+2fB'_(j+1)
       -(j+2)h'B_(j+2)+hB'_(j+2)
       -(j+3)k'B_(j+3),                j=4,3,2,1,0,

where higher Bj vanish and

    (delta0,...,delta7)
       =(1,u,-ell,ell*u-1,2u-ell*S,-u^2-2S,2uS,-S^2).

All inversions divide only fixed nonzero rational eigenvalues. The complete remaining polynomials are

    E0=k'B1-hB0'-1,
    E1=2k'B2+h'B1-hB1'-2fB0'-u.

Retain EVERY coefficient of E0 (degree<=9), EVERY coefficient of E1 (degree<=8), and omega*a*b-1, where a=k4 and b=[S^7]B0. Both inverse-polynomiality conditions and upper rows remain supplied by the accepted reconstruction, including u=0. No free Bj replaces it.

Write e0=E0(0), e1=E1(0). These are residual constants, not the unrelated coefficients of B4 used in the parent.

## 3. Direct low-jet calculation

For clarity write a coefficient (Bj)_i=[S^i]Bj. The needed constant and low coefficients independent of k are obtained from the displayed recursion:

    (B2)_0=-u^2*d0/2,
    (B2)_1=ell-d0+u*d0^2-2u*H1-(2/5)u^2*d1,
    (B3)_0=u^2,       (B3)_1=0,
    (B3)_2=H1-(8/5)u*d1,
    (B1)_0= -H0^2-u*ell+u^2*H1+(4/5)u^3*d1.            (1)

For example (B3)_2 follows from eigenvalue -3 at j=3, using (B4)_2=d0/2,(B4)_3=6d1/5. The first two B2 coefficients use eigenvalues2,-1 at j=2. Substitution into the constant j=1 row

    (B1)_0=ell*u-1-2d0*(B2)_0-2u*(B2)_1-3u^2*H1

gives the last identity of (1). Thus the displayed k-independence is a consequence of the full recursion, not a guess from degrees.

It is efficient to compute the dependence on k1,k2 by exact differences. Change k by q1*S+q2*S^2, retaining all other parameters. B4,B3 do not change. The j=2 recursion gives

    delta B2=(5/4)q1*S^2+(10/7)q2*S^3.                 (2)

The j=1 recursion, at S and S^2, then gives

    delta(B1)_0=0,
    delta(B1)_1=-(3/2)u*q1,
    delta(B1)_2=-(d0/10)q1-(52/35)u*q2.               (3)

To check the latter coefficients manually: before division by eigenvalue -2 the S coefficient is `-5u*q1+8u*q1=3u*q1`. Before division by eigenvalue -5 the S^2 coefficient is `(d0/2)q1+(52/7)u*q2`; the terms are exactly -2f' delta B2+2f(delta B2)'-4(delta k)'B4. No h term varies because B3 is fixed.

The S coefficient of the j=0 forcing varies by

    d0*delta(B1)_1-4u*delta(B1)_2
      +2H0*delta(B2)_2-6u^2*q2.

The final term is the complete contribution of -3(delta k)'B3, using (B3)_0=u^2,(B3)_1=0. Dividing by eigenvalue -3 gives

    delta B0'(0)=(-5/6+(6/5)u*d0)q1+(2/105)u^2*q2.  (4)

There is no hidden k3/k4 contribution to these constants. A variation of k starting with S^j for j>=3 changes B2 only from S^(j+1), B1 only from S^j and B0 only from S^(j-1). In particular the four scalar entries used in e0,e1 above do not see it. This is checked directly from the same recursion, including the factors B4 of S-order1 and B3 of S-order0.

Equations (1)–(4) prove exact affine dependence, not just a tangent computation: B2 is affine in k, B1 is affine in k because its only k-dependent inputs are B2 and k', and B0 is affine in k because B1,B2 enter linearly and B3 is fixed. In e0 the factor k1 multiplies the k-independent (B1)_0; in e1 it multiplies the k-independent (B2)_0. Hence these particular residual constants are genuinely affine in k1,k2.

## 4. The literal two constants and their combination

Let c0 and c1 be e0 and e1 evaluated at k1=k2=0 through the SAME full recurrence. They are specified polynomials in the other parameters, not extra variables or an omitted equation. The preceding calculation gives

    e0=Acoef*k1-(2/105)H0*u^2*k2+c0,
    e1=Q*k1+(4/105)u^3*k2+c1,                         (5)

where

    Acoef=-H0*(1/6+u*d0/5)-u*ell+u^2*v0-u^3*d1/5,
    Q=-u/6-u^2*d0/10.

For direct checking, the k1 coefficients before simplification are

    (B1)_0-H0*(-5/6+(6/5)u*d0),
    2(B2)_0+(3/2)u*H0+2u*(-5/6+(6/5)u*d0),

respectively. Inserting (1), H0=1-u*d0 and H1=v0-u*d1 gives exactly Acoef,Q in (5).

Take the single row operation

    R=e0-(d0/2)e1.

Because H0+u*d0=1, its k2 coefficient simplifies without any parameter division. Precisely,

    R=J*k1+L*k2+R0,
    L=-(2/105)u^2,
    R0=c0-(d0/2)c1,
    J=-1/6+u*j1+u^2*j2,
    j1=d0/20-ell,
    j2=d0^2/4+v0-u*d1/5.                              (6)

The original ideal contains e0,e1 iff it contains R,e1; this is an elementary invertible row operation with inverse e0=R+(d0/2)e1. All other coefficient rows remain untouched at this stage.

Neither J nor u is being assumed a unit. Formula (6), not a generic nonvanishing assertion, is the all-strata opportunity.

## 5. Explicit determinant-one coordinates and unit pivot

Work over the polynomial base ring

    T=Q[u,ell,d0,d1,v0,v1,v2,k3,k4,omega].

Define polynomials

    M=36*j1^2+6*j2+36*u*j1*j2,
    s=-6*(1+6*u*j1),
    z=-(105/2)*M.

These use only fixed rational denominators. Direct multiplication gives

    s*J=1-u^2*M,
    z*L=u^2*M,
    s*J+z*L=1.                                          (7)

Here s,z are auxiliary coefficient polynomials, not source coordinates. Thus (J,L) is a unimodular row over T, with an EXPLICIT inverse certificate. No abstract completion theorem is imported. Set

    X=J*k1+L*k2,
    Y=-z*k1+s*k2.

The matrix has determinant J*s+L*z=1. Its polynomial inverse is

    k1=s*X-L*Y,
    k2=z*X+J*Y.                                         (8)

Under this coordinate change, the exact row R becomes `X+R0`. The coefficient of X is ONE on every stratum. Eliminate it by X=-R0. The complete explicit back-map is therefore

    k1=-s*R0-L*Y,
    k2=-z*R0+J*Y.                                       (9)

This is not a new gauge and not a projection onto a guessed subset. Equations (7)–(9) are polynomial identities valid over arbitrary Q-algebras, including nonreduced ones. In particular no u=0, J=0 or H0=0 stratum is removed. The use of the accepted source theorem afterward remains at its original field-point scope.

## 6. Complete smaller ideal and exact back-map

Define the new ideal in T[Y] as follows:

1. Retain e1 and every nonconstant S coefficient of E0, together with every other S coefficient of E1.
2. Retain omega*k4*b-1 with b=[S^7]B0 from the ENTIRE accepted reconstruction.
3. In every retained polynomial substitute (9), using R0 as defined by the full recurrence at k1=k2=0. Do not treat R0 or b as an independent variable.

There are11 variables: the10 variables of T and Y. The original20-row envelope loses exactly the row X+R0 after solving it, giving at most19 rows. These are definition/envelope counts, not emitted nonzero-row counts, dimensions or cost estimates.

The original12-variable quotient by L1 is isomorphic to this11-variable quotient. Indeed the invertible row operation replaces e0 by R without changing the ideal, the determinant-one change is a polynomial ring automorphism over T, and quotienting by X+R0 is ordinary coefficient-one elimination. The maps (8),(9), with X=-R0, give the explicit inverses. Every other residual, upper reconstruction, inverse-boundary identity, target sign and top-product guard is transported by literal substitution. Neither k4 nor omega is changed; b is fully transported, not assumed independent of the eliminated coordinates.

The quotient isomorphism proves preservation of unitness/properness for this exact finite ideal, and of all its field or Q-algebra points. Composing with the ACCEPTED16r field-point equivalence preserves the existing compact/source endpoints; it does not establish any new point or source exclusion. Parameter-polynomial degrees may increase substantially in (9), so no runtime or sparsity advantage is claimed. There is no emitted system, implementation or solver authorization here.

## 7. Boundary and changed-object controls by hand

At u=0, the needed low jets of the reconstruction simplify to

    (B2)_0=0,
    (B2)_1=ell-d0,
    (B2)_2=(5/4)k1-(9/10)d1,
    (B1)_0=-1,     (B1)_1=-v0,
    B0'(0)=-(5/6)k1-d1/15+ell*v0/3.

For the last formula, the j=0 S coefficient is `d1/5-ell*v0+(5/2)k1` and its eigenvalue is -3. Consequently

    e0=-k1/6+d1/15-ell*v0/3-1,
    e1=0.                                                (10)

Thus root's u=0 scratch is confirmed, but only on that exact boundary. Here J=-1/6,L=0 and (9) gives

    k1=(2/5)d1-2ell*v0-6,

while Y still parametrizes every k2 through the invertible map (8). The coefficient -1/6 is a genuine rational unit there. A changed value k1+6 changes e0 by -1, so this is not an automatic vanished row. The constant target1 is retained.

Away from the boundary J really can vanish without violating the already-required top guard at the reconstructed-upper stage. Set

    u=1, ell=d0=d1=0, v0=1/6, v1=0, v2=1,
    k=S^4.

Then j1=0,j2=1/6,J=0,L=-2/105. The full upper reconstruction and inverse boundaries still hold by the accepted construction. Its leading coefficients are a=1, [S^4]B3=13/9 and [S^5]B2=20/13; the j=0 leading row gives

    b=((20/13)+12*(13/9))/21 !=0.

These leading comparisons are unchanged by the displayed lower u,v0 terms, whose degrees are strictly smaller. Choosing omega=1/b retains the guard. This is only an upper/guard control, NOT a full residual point, and is not exclusion evidence. It demonstrates why treating J as an already-required unit would need an additional unproved implication.

The global pivot remains regular at that control: M=1,s=-6,z=-105/2 and

    [[J,L],[-z,s]]=[[0,-2/105],[105/2,-6]]

has determinant1. Omitting the lower-left entry (equivalently using z=0 while retaining the first row) gives determinant0 at this same changed object. Thus the Bezout completion is load-bearing, not a decorative invertibility assertion. No programmed arithmetic, finite-field test or actual full-source point was used.

## 8. Terminal decision

Outcome: a genuinely all-strata coefficient-one elimination after an explicit polynomial coordinate change. A direct division by the apparent k1 coefficient would have been generic and unlicensed; the fixed Bezout identity (7) removes that obstruction without branching. The proof does not depend on maximal-h or constant-h exclusions and does not add a new gauge.

This new quotient-presentation result remains PROVISIONAL for independent review. The complete builder is unchanged. No proof of ideal consistency/inconsistency, properness, point, F10/JC2 exclusion or measured speedup follows. Exactly three accepted inputs were read; no live/new theorem, shared ledger, web, protected tree or remote state was accessed. All calculations and controls are manual, with ZERO mathematical subprocesses of any size. Own whole/open checks precede sealing; terminal custody records unchanged current pins and all writers idle. No follow-on authority.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN extraction; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12882`.
- Body SHA-256:
  `d6305dbf956f6057b8890f4fa5e9f22c10265a2dde5ceb7d36f1938d1a23b00d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
