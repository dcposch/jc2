# D125 physical-axis Bezout: an explicit existing-source unit

2026-09-08. **KNOWN/REDUNDANT PRINCIPLE; EXACT SOURCE CONSEQUENCE, NO NEW EXCLUSION.** The proposed leading axis coefficients are correct. Two scalar functions E and delta_axis satisfy E·delta_axis=5k³/9 in the full14c quotient, so both are units on its guarded chart, even over nonreduced coefficient rings. This recovers the accepted critical-unit principle in this literal source; it adds no equation and establishes no elimination or runtime gain. The global unit's mathematical parent is14c alone. Older unit results are history; boundary reports supply the separately requested comparison. No pending high-alpha result is used.

## 1. Individual coefficient projections, not source expansion

Write receiver coefficients as Z_ij. Under phi(g)=v⁻¹, phi(p)=v⁴u−v−v⁻¹, the contribution of g^i p^j to [u^t v^e] is

    (-1)^(j-t) binom(j,t) binom(j-t,nu),
    nu=(e+i+j-5t)/2,

interpreted as zero unless nu is an integer with 0<=nu<=j-t and 0<=t<=j. This follows by selecting t copies of v⁴u, nu copies of −v, and the remaining copies of −v⁻¹. It defines explicit rational-linear source functions; all coefficients below mean these literal projections, not new independent coordinates.

Odd receiver degree and the bounds15/25 imply: at e=0, t is odd and 5t<=15/25; at e=1, t is even and 5t<=16/26. Only the prescribed total face contributes to the highest e=0 terms. For H=p²(g³+p³), the m+1 known monomials of H^m have (i,j)=(3(m-r),2m+3r) and coefficient binom(m,r). Individual projections, without expanding a source pair or high R power, give

    m=3: -20+252-660+455=27,
    m=5: -252+6435-43680+116280-131670+53130=243.

Thus in the COMPLETE ordinary-lift quotient, with physical-axis coefficient names a,b,c,E0,E2,D0,D2,D4,

    P(u,0)=27u³+a u,          P_v(u,0)=E2u²+E0,
    Q(u,0)=243u⁵+b u³+c u,  Q_v(u,0)=D4u⁴+D2u²+D0.

Negative lift rows are required for P,Q to be polynomials; no omitted negative term is treated as an ordinary coefficient. The chart determinant is v², so the physical target is J(P,Q)=−5k³/9, including its sign.

## 2. Exact four-row certificate over arbitrary Q-algebras

Reduction by u²+a/81 is monic division; it does not invert a or pass to field points. It gives

    Q_u mod(P_u)=delta_axis=c−ab/27+5a²/27,
    P_v mod(P_u)=E=E0−aE2/81.

Let r_i=[u^i](P_u Q_v−P_v Q_u+5k³/9)|_(v=0). Its only possible rows are

    r6=81D4−1215E2,
    r4=81D2+aD4−3bE2−1215E0,
    r2=81D0+aD2−cE2−3bE0,
    r0=aD0−cE0+5k³/9.

The literal universal polynomial identity is

    E delta_axis−5k³/9
      = −r0+(a/81)r2−(a²/81²)r4+(a³/81³)r6.      (B)

Writing Pi_(t,e) for the projection in Section1, the exact original-row map is r_i=Pi_(i,−2)([A,B]+5k³g²/9), since J(P,Q)=v²phi([A,B]). Each physical row is therefore a linear combination of the original receiver-Jacobian coefficient rows. Hence (B) is valid after ANY coefficient base change, including nilpotents. It holds already on the unguarded full quotient; the guarded relation zk−1 then gives

    delta_axis⁻¹=(9/5)z³E,     E⁻¹=(9/5)z³delta_axis.

This is actual ideal membership and an explicit inverse, not radical membership, a sampled rank, or a unit ideal. No existence of a guarded point is asserted.

## 3. What changes, and what does not

The accepted transverse-critical-unit report/gate already license this kind of full-Jacobian unit argument. Here parity makes BOTH remainders scalar in the rank-two critical algebra; no critical root or separability assumption is needed. The named D125 history did not display these exact source functions, but this is only a recovered source-specific certificate, not a priority claim or new global obstruction.

Localization at E or delta_axis loses nothing on the complete guarded quotient. For example adjoining w with Ew−1 is an isomorphism, with inverse substitution w=(9/5)z³delta_axis. Formally it gives

    c=ab/27−5a²/27+(5/9)k³w.

However c is a source linear functional, not proved to be an independent remaining coefficient. Adjoining w costs a variable/row, and all original equations must still be transported. No actual coefficient elimination, reduced dimension, cheaper presentation, gauge E=1, or new solver constraint follows. Smaller row subsets cannot use (B) unless they retain its supporting rows and guard.

## 4. Exact comparison with the boundary delta

At an accepted14f field center, A0=R_t³+alpha R_t and B0=R_t⁵+beta R_t³+gamma R_t, where

    R_t=p²(g³+p³)+(t+3)gp²+t p³−(t+3)p.

Individual degree-five projections give phi(R_t)(u,0)=3u and partial_v phi(R_t)(u,0)=−(t+4)=:r. Differentiating the FACTORED references, without their expansion, yields

    a=3alpha, b=27beta, c=3gamma,
    E2=27r, E0=alpha r,
    delta_axis=3(gamma−beta alpha+5alpha²/9)=3Delta0,
    E=0.

This normalization map holds on that parameterized center, including t=−3; it is not an equality between axis coefficients and arbitrary moving reference series away from the center. Residual F/G terms can contribute to the physical axis. The global identity specializes to 0=0 at k=0 and alone does NOT force Delta0=0: the accepted boundary family with gamma=1, alpha=beta=0 has delta_axis=3 and E=0. The stronger exceptional-center finite-arc result is therefore a separate theorem, not recovered by canceling E at the boundary. No finite degeneration is assumed.

## 5. Controls, history exposure and custody

Self-contained check.py verifies the individual top projections, an independent degree-three Laurent expansion, universal certificate(B), actual R_t projections, boundary scaling and an axis-only model over Q[epsilon]/(epsilon²). The latter has a=epsilon, b=0, c=5/9, E0=1, E2=0, D2=15, D0=−5epsilon/27, D4=0, k=1; all four rows vanish. It is NOT a full-source point. Fourteen capped normal/−O runs pass: changed A/B fixed-face coefficients, delta factor, deleted E2 correction, omitted r6 and reversed target sign are rejected. Positive outputs coincide; zero Assert nodes; no actual high source power or CAS.

The initial overly broad history command accidentally exposed three high-alpha producer snippets before its exclusion-glob error was noticed. Root was informed; those bytes are uncharged and not premises. No body/code or live gate was read, and no broad search was repeated. The exact perimeter/correction is in history-and-scope.md. Immutable source and output pins plus complete tiny replay are retained in the owned box. All writers/children terminal; transactional publication verified. **STOP: explicit redundant full-source unit, no re-review request or further computation.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6744`.
- Body SHA-256:
  `1ee3c56088b6b2a74f1b206a11425a8ddbd1b52ac36600b53e739e4ccecde303`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
