# Small F2 receiver: exact finite polynomial-lift acceptance contract

Status: **PROVISIONAL EXACT CONTRACT, NO EXISTENCE CLAIM**, 2026-09-06. Frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d`. One bounded reverse-map task. No full symbolic source expansion, ideal builder, CAS, solver, AWS or live gate read.

## Outcome

The missing reverse arrow can be imposed by **105 finite polynomiality rows and two unrestricted lift parameters**. This closes the *acceptance contract*, not the existence problem:

> Any characteristic-zero field point satisfying the complete degree-(15,25) receiver Jacobian equations, monicity, nonzero Jacobian scalar, and all 105 negative-Laurent-coefficient equations below reconstructs actual polynomial Keller maps of exact degrees `(75,125)`.

Neither degree divides the other, so the reviewed plane polynomial-automorphism degree criterion makes such a point a JC2 counterexample. Equivalently, properness over Q or the stated quadratic coefficient field of a **fully emitted ideal satisfying this contract** would certify a counterexample over an algebraic extension. No proper ideal or point is exhibited, no complete ideal is emitted here, and no runtime gain is measured.

This sufficiency statement does **not** depend on the incoming GGV/Strinz/F2 necessity theorem, Roy pins, a Moh source attachment, or the live composition gate. Necessity for a given normalized standard-F2 family remains conditional on the previously gated incoming chain and the exact coordinate composition. Those directions must remain separate.

## 1. Inputs and finite ring

Let k be a characteristic-zero field. For the squarefree outer face k may be Q. For the golden face use `k=Q[rho]/(rho²-3rho+1)`; both embeddings into Qbar are retained. In a Q implementation this can equivalently be represented by one rho variable and its quadratic equation, without choosing a numerical root. It is a field because the discriminant 5 is nonsquare in Q, and `rho^-1=3-rho`.

Let

`A(gamma,pi)=sum a_(i,j) gamma^i pi^j`, `B(gamma,pi)=sum b_(i,j) gamma^i pi^j`

be ordinary polynomials with total degrees at most 15 and25. Require

`a_(0,15)=1`, `b_(0,25)=1`, `[A,B]=c gamma²`, `c!=0`.

The three existing receiver polygon envelopes, their prescribed outer/inner faces and the chosen economical normalizations may be imposed as additional equations. They are useful for the necessary family and a smaller parameter presentation, but are **not needed for this sufficiency proof** beyond the degree bounds and monicity. The baseline parameter ring adds only `lambda2,lambda3`, both free and allowed to be zero, plus a scalar c and its guard `z_c*c-1` if c is not already a fixed nonzero coefficient-field element. No inverse of either lambda is allowed or required.

For clarity, the complete Jacobian rows can be defined without a builder by

`J_(r,s)=sum_(i+k=r+1, j+l=s+1) (i*l-j*k) a_(i,j)b_(k,l)-c*delta_(r,2)*delta_(s,0)`.

Every `(r,s)>=0` with `r+s<=38` is retained; absent source coefficients are zero. This universal envelope has 780 slots, many identically zero for the actual polygons/fixed faces. It is only a safe row definition/count, not a claim that 780 nonzero polynomials were generated. No partial bracket, projection or local recurrence suffices in place of all these rows.

## 2. Source map, cut order and exact inverse

The original post-affine polynomial-source variables are related to the receiver by

`u=gamma^4*pi+lambda2*gamma²+lambda3*gamma³+gamma^5`, `v=gamma^-1`.

This has exactly the cut order of the earlier derivation. After swapping `(x,y)=(v,u)`, the lower cuts are `y -> y+lambda2*x^-2+lambda3*x^-3`, followed by the selected initial double-root cut `y -> y+x^-5`. All are translations of y by functions of x, hence commute. Substituting `x=gamma^-1,y=gamma^4*pi` gives the formula displayed above. An absent lower cut is represented by its lambda being zero. There is **no x^-4 parameter**: the accepted three-case reduction deliberately stopped before those optional later upper cuts. No hidden ordering or chart variable is missing.

The exact inverse is

`gamma=v^-1`, `pi=v^4*u-lambda2*v²-lambda3*v-v^-1`.

Direct substitution in both orders gives the identity in the Laurent coordinate rings. The forward coordinate Jacobian with respect to `(gamma,pi)` is **+gamma²**, and the inverse coordinate Jacobian with respect to `(u,v)` is **+v²**. Indeed the inverse determinant is `0*pi_v-(-v^-2)*v^4=v²`. Therefore, defining

`P(u,v)=A(v^-1,v^4*u-lambda2*v²-lambda3*v-v^-1)`,

`Q(u,v)=B(v^-1,v^4*u-lambda2*v²-lambda3*v-v^-1)`,

one obtains `[P,Q]=v²*(c v^-2)=c` in `k[u,v,v^-1]`. Polynomiality is the only missing issue in this step; it is not inferred merely from this constant bracket.

## 3. All negative coefficient equations: exact formula and 105 slots

For a source coefficient a_(i,j), choose t factors `v^4*u`, b factors `-lambda2*v²`, d factors `-lambda3*v`, and `j-t-b-d` factors `-v^-1`. The contribution is

`a_(i,j) * j!/(t! b! d! (j-t-b-d)!) * (-1)^(j-t) * lambda2^b lambda3^d * u^t v^(5t+3b+2d-i-j)`.

The sign includes all three negative summands; no extra saturation or denominators beyond rational constants occur. Thus for every t>=0 and e<0 define

`L^A_(t,e)=sum a_(i,j) * multinomial(j;t,b,d,j-t-b-d) * (-1)^(j-t) * lambda2^b lambda3^d`,

where the sum is over supported `(i,j)`, `t+b+d<=j`, and `5t+3b+2d-i-j=e`. Define `L^B` identically with b_(i,j) and degree bound25. These are literal coefficient extractions `[u^t v^e]P,Q`, not formal growing-degree limits.

If `i+j<=D`, a negative exponent must satisfy

`0<=t<=floor((D-1)/5)`, `5t-D<=e<=-1`.

Consequently the complete uniform list is:

| source | t values | number of negative-v rows by t | total |
|---|---|---|---|
| P, D=15 | `0,1,2` | `15,10,5` | **30** |
| Q, D=25 | `0,1,2,3,4` | `25,20,15,10,5` | **75** |

All 105 slots are retained, including any that become identically zero after face substitutions. Before specialization, the exact union of possible negative indices equals this list for **each** of the three polygon envelopes: every envelope contains the entire pi-axis segment, and the monomial pi^(5t-e) with the appropriate all-`-v^-1` remainder attains each listed `(t,e)`. The owned support-only enumeration verifies equality; it does not expand any full source pair.

Each row is linear in the receiver coefficients. Negativity gives `3b+2d<=D-5t-1`, hence lambda-degree at most7 for P and12 for Q. Before coefficient-face substitutions, the total semantic degrees are therefore at most8 and13. These are algebraic bounds, not term counts or solving measurements.

The 105 equations are sufficient and necessary for P,Q to be polynomials in u,v: the expansions are finite Laurent polynomials, and distinct monomials `u^t v^e` are linearly independent. This is a coefficientwise equality, not a condition imposed only on a sampled v value or on a finite jet of an unbounded series.

## 4. Degree and counterexample acceptance proof

Each expanded monomial has u-degree t<=j and v-exponent `e=4t+2b+d-(j-t-b-d)-i`. Its ordinary total degree satisfies

`t+e<=5j-i<=5D`.

Also `e<=4j-i<=4D`, and `5t-e=i+j-3b-2d<=D`. Once all negative powers vanish, P and Q therefore lie in the respective rectangles `(deg_u,deg_v)<=(15,60),(25,100)` and satisfy the original weight bounds `(5,-1)<=15,25`.

The coefficient of `u^D v^(4D)` is exactly the coefficient of pi^D. To contribute u^D one needs j>=D; since i+j<=D this forces `(i,j)=(0,D)`, and all D factors must be `v^4*u`. Hence the coefficient is 1. No other monomial has total degree 5D, so the unique total leaders are `u^15 v^60` and `u^25 v^100`. Exact degrees75 and125 are automatic from monicity; no further degree-guard parameter is needed.

Combined with section2 this proves: every field point of the complete guarded receiver-plus-lift ideal yields `[P,Q]=c!=0` in `k[u,v]`, with exact degrees75/125. The already reviewed plane automorphism degree-divisibility criterion excludes a polynomial automorphism because neither degree divides the other. That criterion remains a named external input; it is not re-proved here.

For an ideal over Q or the quadratic coefficient field, properness supplies a maximal-ideal point over a finite algebraic extension by the weak Nullstellensatz. Its scalar guard keeps c nonzero, and the finite coefficient formulas reconstruct a pair over Qbar, hence over C. Thus a **genuinely complete proper ideal** meeting this contract would be a JC2 counterexample certificate. A proper projection, omitted-row subsystem, modular point or informal receiver family is not such a certificate.

## 5. Economical normalizations preserve the inverse parameters

Target constant translations are harmless: subtracting the receiver constants subtracts the same constants from P,Q, changes neither the bracket nor negative rows, and leaves their leaders unchanged. If constants are fixed to zero, use the **closed polygon envelopes**, not simultaneous nonzero guards on the former `(0,0)` vertices. The other mandatory vertex/face coefficients remain guarded.

For the monic outer faces define

`A_tau=tau^-15 A(tau*gamma,tau*pi)`, `B_tau=tau^-25 B(tau*gamma,tau*pi)`, `tau!=0`.

The exact corresponding source change is

`P_tau(u,v)=tau^-15 P(tau^5*u,tau^-1*v)`,

`Q_tau(u,v)=tau^-25 Q(tau^5*u,tau^-1*v)`,

with inverse parameters

`lambda2_tau=lambda2*tau^-3`, `lambda3_tau=lambda3*tau^-2`.

The selected fifth-cut coefficient stays 1. This follows by substituting the source map: the coefficient of gamma² scales by tau² before factoring tau^5, and that of gamma³ by tau³. The polynomial-source property is preserved by the diagonal source automorphism, and no new inverse parameter or localization is introduced. The scalar becomes `c_tau=c*tau^-36`, consistent with both Jacobian calculations.

Let kappa be the gamma³ coefficient of the normalized outer cubic: kappa=1 in the squarefree case and kappa=rho in the golden case. The incoming monic unequal face has low endpoint a and forces `c=-(5/9)a³/kappa`. Since c!=0, a!=0. Choosing `tau^12=a` over the algebraic closure sets **a=1**, giving `c=-5/(9*kappa)`. Do not also impose c=1. Kappa is a fixed nonzero coefficient-field element, so this unequal scalar requires no variable guard once substituted exactly.

For common_3 the inner-root parameter transforms as `mu_tau=mu/tau²`; choose `tau²=mu` to make mu=1. For common_4 it transforms as `mu_tau=mu/tau`; choose tau=mu. In these cases retain c as a free nonzero scalar with its guard. Both changes carry lambda2 and lambda3 by the formulas above, including zero values, and preserve all outer slope ratios. No same-field existence of the twelfth or square root is asserted; these are geometric nonemptiness equivalences over the algebraic closure. Tau is a proof-time choice, not an additional ideal parameter.

Thus the economical models need no additional algebraic variables beyond the two lift lambdas, the receiver's c guard where needed, and the existing rho coefficient field. The fixed rho equation retains both conjugate golden branches.

## 6. Optional exact reconstruction of both lift parameters

This root-suggested lemma is banked separately from the baseline 105-row construction. It requires the **fixed monic outer face**, not merely monicity of pi^15. Write

`A(gamma,gamma*z)=sum_(k=0)^15 gamma^(15-k) a_k(z)`,

with `a_0(z)=h(z)^3`, where

`h(z)=z²(z³+1)` or `h(z)=z²(z+1)(z+1-rho)²`.

In both cases z=-1 is a simple root of h. Put `D0=a_0'''(-1)`. Since `a_0=h³`,

`D0=6 h'(-1)^3=162` in the squarefree case, and `D0=6 rho^6` in the golden case.

These are nonzero **constant coefficient-field units**, with inverse `(3-rho)^6/6` in the golden case. There is no generic parameter localization.

The inverse map gives `z=-1+v^5*u-lambda3*v²-lambda2*v³`. Taylor expansion at -1, or the same multinomial formula, yields exactly

`[u²v^-5]P=a_0''(-1)/2=0`,

`[u²v^-4]P=a_1''(-1)/2`,

`[u²v^-3]P=(a_2''(-1)-lambda3*D0)/2`,

`[u²v^-2]P=(a_3''(-1)-lambda3*a_1'''(-1)-lambda2*D0)/2`.

Hence two of the actual negative rows are triangular graph equations:

`lambda3=a_2''(-1)/D0`,

`lambda2=(a_3''(-1)-lambda3*a_1'''(-1))/D0`.

The first right-hand side is linear and the second is at most quadratic in the free receiver coefficients. Replacing the two rows by these equations uses only invertible constant scalings and triangular row operations. Eliminating the two graph variables gives an isomorphic coordinate ring **provided every other row, scalar guard and source constraint is retained with the exact substitution**. This is stronger than a generic-rank or radical-only statement. The baseline is still all105 rows with two lambdas; no substitution into the remaining system is performed here, and coefficient/term growth is not claimed manageable. The automatic row and any further zero identities may simply remain in the baseline.

## 7. Exact controls, real omission control and custody

Owned `box/d125-small-receiver-polynomial-lift-contract-20260906/check.py` uses only standard-library exact rational dictionaries. It checks both map compositions and Jacobian signs, positive polynomiality fixtures, all negative support slots for the three closed polygons, degree/weight bounds, uniqueness of the monic source leader, scaling covariance with both lambda parameters, the four selected Taylor rows and both constant D0 values. Only tiny fixtures and selected coefficient rows are expanded; no full receiver/source ideal is built. Ordinary and `-O` runs pass; genuine wrong inverse-Jacobian and wrong pivot-sign mutations fail in both modes.

The omission control uses the **actual inverse map** at lambda2=lambda3=0:

`A=gamma`, `B=gamma²*pi+gamma³`, `[A,B]=gamma²`.

It reconstructs `P=v^-1`, `Q=v²*u`, with `[P,Q]=1`. Exactly one negative coefficient remains: `[u^0 v^-1]P=1`. The full polynomiality verifier rejects this pair. Omitting that actual row makes the same verifier accept, even though P is nonpolynomial. This is a genuine row-omission mutation, not a verbal warning or a test that fails some unrelated row. The fixture has toy degrees, not the degree15/25 monic faces, and is not claimed to refute a stronger reverse theorem with all those conditions. Positive cancellation controls reconstruct u and u² from their forward images and are explicitly not Keller counterexample fixtures.

Inputs: the author's terminal T4 packet SHA `7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413` and exact checker SHA `3ff299bc761f0e80ef47c254ce59b187e5e87315e8855f77b2a522a7a99e9ac3`. The earlier incoming necessary theorem is used only for the separately conditional necessity discussion. The live Fable T4 composition gate, live engineering/positive-face gates, and protected project were not read. No shared or immutable artifact was changed.

Registration, input pins, replay and terminal custody are in the owned box. Commands are capped at 30 wall seconds,25 CPU seconds,512 MiB. All owned writers finish before handoff; no worker or background process is retained. **STOP:** the output is a finite sufficient CE contract and an optional exact graph elimination, not a point, a properness result, a built solver input or a speedup claim.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15284`.
- Body SHA-256:
  `f4a2aab6fa5f2092312b19bd243b79afe6d35abe3090d0fc50958ddc8230b1fe`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
