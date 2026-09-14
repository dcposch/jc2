# Same-task addendum: every full F10 point forces maximal degree of h

2026-09-09. NEW/PROVISIONAL manual theorem. Root explicitly authorized this separately leased addendum after the constant-h report had already been finalized at12:15:20 UTC; those earlier bytes and custody remain immutable. Same task and original conservative12:22 UTC stop, no reset or descendant. Addendum lease opened12:16:59 UTC. Basis0d39df3c9fd69c939a8420c54d03228b9077777d is provenance only.

## 1. Stronger exact statement and independent parents

For every r>=1, EVERY field point of the accepted complete normalized F10 system has

    deg h=2r+1.                                             (A)

Since h=1-u*d+S*v with deg d<=r and deg v<=2r, this equivalently forces the coefficient [S^(2r)]v to be NONZERO. No new normalization follows: that coefficient is not set to one. This is not a full-system exclusion or a proof of nonemptiness of the maximal-degree stratum.

The only mathematical parents are the same three current-pinned WHOLE accepted objects in this packet's PINS.json: Euler producer a5ab487c4619742b6252e2503488eea4d6e927b58fd2821207cc85bcba7cf8d5, accepted16r gate77d59f7b54e545d6a05f61ab270739c1498f93eed5d155e40222cecdc96c0a8c, accepted16q module26687318390a287fe08a803191e27d131d8a8fd4992d5b4d6d81a35f39d23954. Neither the newly sealed constant-h theorem nor the earlier unreviewed low-degree lemma is used. Root's new scratch suggested the comparisons; every comparison is independently derived below.

## 2. Full retained hypotheses

Let K be a characteristic-zero field, r>=1, m=3r+1, n=5r+2. The normalized complete pair is

    A=S t^3+f t^2+h t+k,       B=sum_(j=0)^5 Bj t^j,
    B5=S^2,                  [A,B]_(S,t)=Delta,
    p=t-u t^2+S t^3,         Delta=1+u t-ell*t*p-t*p^2.

All coefficient polynomials are in K[S]. Retain f=S*d-u, h=1-u*d+S*v, deg d<=r, deg v<=2r, deg k=m, deg B0=n, a=[S^m]k!=0, b=[S^n]B0!=0 and deg Bj<=n-rj. Both boundary conditions, all source-equivalent normalization/guard conditions and every upper/low equation remain required.

Primes are S derivatives. The two full low rows are

    k'B1-hB0'=1,
    2k'B2+h'B1-hB1'-2fB0'=u.                              (B)

The whole upper formula, independently obtained from `(l Ai'Bl-i AiBl')t^(i+l-1)`, is

    (j-3S*d/dS)Bj=delta_(j+2)
       -(j+1)f'B_(j+1)+2fB'_(j+1)
       -(j+2)h'B_(j+2)+hB'_(j+2)
       -(j+3)k'B_(j+3),                j=4,3,2,1,0.       (C)

Here higher Bj are zero and

    (delta0,...,delta7)
      =(1,u,-ell,ell*u-1,2u-ell*S,-u^2-2S,2uS,-S^2).

All lower coefficients remain in these identities. Extracting a necessary coefficient is not replacing their full equations by a top model.

## 3. Assume a smaller degree, and derive the forced leading zeros

If h=0 as a polynomial, the first row of (B) gives k'B1=1, impossible since deg k'=3r>0. Hence h!=0. Suppose for contradiction that tau=deg h<=2r. Since b!=0 and deg B0'=5r+1, the first row of (B) gives

    deg B1=tau+2r+1<=4r+1.                               (D)

In particular its S^(4r+2) coefficient is zero. This is forced by the exact constant-target equation, not imposed by an unlicensed coefficient deletion.

Define the following scalar coefficients regardless of whether they initially vanish:

    F=[S^(r+1)]f,
    E=[S^(r+2)]B4,
    C=[S^(2r+2)]B3,
    D=[S^(3r+2)]B2.

The symbol D from now on is this scalar, not an operator. The argument proves the needed nonzero scalars before dividing by them.

## 4. Five upper coefficients, including every possibly tied contribution

First, the j=4 row at S^(r+2) has left coefficient -(3r+2)E. The f terms contribute `[-5(r+1)+4]F=-(5r+1)F`. The target has degree1 and all other B terms vanish. Thus

    E=(5r+1)/(3r+2)*F.                                    (E1)

Second, j=3 at S^(2r+2) has left coefficient -(6r+3)C. Its f terms contribute `[-4(r+1)+2(r+2)]FE=-2rFE`. Both h terms have degree at most tau+1<=2r+1, strictly smaller. The target has degree1; there is no k term. Therefore

    C=2r/(6r+3)*F*E.                                      (E2)

Third, j=2 at S^(3r+2) has left coefficient -(9r+4)D. Its f terms contribute `[-3(r+1)+2(2r+2)]FC=(r+1)FC`. Each h term has degree at most tau+r+1<=3r+1. The k term is -5k'S^2 with coefficient -5ma. The target has degree at most1. Hence

    (9r+4)D=5ma-(r+1)FC.                                 (E3)

Fourth, j=1 at S^(4r+2) has left coefficient zero by (D). Its f terms contribute `[-2(r+1)+2(3r+2)]FD=(4r+2)FD`. The h terms have degree at most tau+2r+1<=4r+1, while -4k'B4 contributes -4maE. The target is constant. Thus

    (4r+2)FD=4maE.                                       (E4)

Fifth, j=0 at S^n=S^(5r+2) has left coefficient -3nb. By (D), the f terms have degree at most5r+1. The h terms have degree at most tau+3r+1<=5r+1. The target is constant. Only -3k'B3 reaches degree n, with coefficient -3maC. Consequently

    b=maC/n.                                             (E5)

Because a,b are nonzero and m,n are positive integers in characteristic zero, (E5) forces C!=0. Equations (E1),(E2) then force F!=0 and E!=0. No generic-leading assumption or division by u has occurred.

## 5. The remaining full low row supplies the contradiction

Take the S^(6r+2) coefficient of the SECOND row of (B). Its first term contributes 2maD and its f term contributes -2Fnb. The combined h terms have degree at most

    deg(h'B1), deg(hB1') <= 2tau+2r <= 6r,

so neither can contribute at S^(6r+2). The target u is constant. Hence maD=Fnb. Using (E5) and ma!=0 gives

    D=FC.                                                (F1)

Substitution in (E3) gives

    (10r+5)FC=5ma,       (2r+1)FC=ma.                    (F2)

Substituting (F1) into (E4) and then using (F2) gives

    2maF=4maE,          F=2E.                            (F3)

By (E1) and F!=0, (F3) forces

    3r+2=2(5r+1),       7r=0.

This contradicts r>=1 in characteristic zero. Therefore tau<=2r is impossible. The original support bound deg h<=2r+1 proves (A).

The proof used no field extension, root choice, repeated-root hypothesis, leading ODE solution, or prior constant-h/low-degree theorem. It includes r=1, h a nonzero constant, h=0, u=0 and every value of ell. Those parameters occur only in target coefficients whose strictly lower degrees were checked explicitly.

## 6. Controls and precise stopping boundary

The proof cannot be repeated when deg h=2r+1: in the j=3 comparison, the previously lower h terms now contribute the nonzero-allowed quantity

    -5(2r+1)*[S^(2r+1)]h+2*[S^(2r+1)]h
       =-(10r+3)*[S^(2r+1)]h

at the SAME degree2r+2. The later h terms likewise cease to be uniformly lower. Thus omitting them would falsify the literal full coefficient equations; maximal degree is not itself contradictory. This is the exact missing margin for any stronger conclusion from these comparisons.

The hand control in the separately sealed constant-h report can be rechecked without consuming its theorem: at r=1,u=ell=0, take f=S^2,h=1,k=S^4,B1=(2/3)S^3-1,B2=fB1,B0=(8/21)S^7-S^4-S,B3=(2/3)S^4,B4=0,B5=S^2. The full two low rows hold, but t^6 has residual6S^3. In the present notation F=1,E=0, violating (E1). Therefore keeping the full upper equations is genuinely load-bearing, even when the low equations, boundaries and top-product guard hold. This is not a full-system point.

Under the accepted scalar mate shear B->B+beta*A+gamma, the coefficients E,C,D,b and the forced absent S^(4r+2) slot of B1 are unchanged: the added t-coefficient degrees are respectively absent,1,r+1,m and at most2r in B1 under the contradiction hypothesis. No scalar gauge can evade the argument. The A constant translation has no effect on any derivative or highest coefficient.

Novelty is unassessed. A root history advisory during writing suggests that (A) may recover a known nonvanishing coefficient of the leading ODE, now by a direct complete-Lr argument. No additional history object was opened or charged, and no claimed leading-ODE identification is a premise. This packet claims the literal source-attached consequence above, not a new independent geometric obstruction; root retains the separate exact history/interface comparison.

Only the same three accepted science inputs were read, with their current pins unchanged. All calculations here are manual scalar/coefficient comparisons; ZERO mathematical subprocesses, source expansions, CAS, web, AWS/SSH, agents, shared edits, live reviews or protected-project access. No builder narrowing, extra guard, h normalization, solver or descendant is authorized. This new result remains PROVISIONAL until independent review. It says every possible full point has maximal degree h; it does not exhibit a point, decide the remaining ideal, or exclude F10 or JC2.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only extraction, no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8900`.
- Body SHA-256:
  `8a0eb64f84d0647a34d1c1e667e0de44aa2e54375aa1812d2c7893d0a3c8a4bb`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
