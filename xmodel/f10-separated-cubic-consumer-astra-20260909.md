# F10: the strictly separated minimizing-triple regime

2026-09-09. Independent pure-prose producer; PROVISIONAL pending a different-model review. Basis `0d39df3c9fd69c939a8420c54d03228b9077777d`. No mathematical subprocess, source expansion, external search, or computation was performed.

## 1. Result, inputs, and exact scope

Under the literal hypotheses and canonical reference of accepted 16l, a minimizing triple factor cannot be strictly separated before its first F balance. This holds for every integer q>=0, includes the three-simple and one-simple-plus-double initial cubics, and retains every term of B. It does not exclude the remaining coalesced resonance, prove a receiver empty, or assert an actual-degree/source-map consequence.

The only scientific inputs were read WHOLE after checking their hashes:

* `xmodel/f10-coalesced-resonance-reduction-coordinator-20260909.md`, SHA256 `d225258c605617037d4d74b2cdce9430ce1fc8ac49e81d01dc1b125d76ad0ee1`.
* `xmodel/f10-coalesced-resonance-gate-fable5-20260909.md`, SHA256 `221a5d584c5a412c9b1ac8b51f6bb936e616108b40391a0cb0a50759465f38ff`.

Their accepted status is the invitation's frozen 16l post-state; historical status words inside the producer are not a new uncertainty. No provenance path in either document was followed. The new separated proof below is not imported from another local consumer.

Write m=3q+4, n=5q+7, T=m+n-1=8q+10, and N=7(m+n)-5=7T+2. Thus gcd(m,n)=1 and 3n=5m+1. Work over an algebraic closure of the characteristic-zero coefficient field; any original polynomial identity persists there. The literal top is K=b(b^2-a^2)^3, and the homogenized Jacobian is 2c s^N a^3, c!=0.

The accepted finite reference has combined degree seven and

    A_s=f_s(R)+F,
    f_s(z)=z^m+sum_{i=0}^{m-2} a_i s^{7(m-i)} z^i.

F is nonzero, j=ord_s F, and F_j has degree 7m-j. Take a globally minimizing triple factor, let d be its multiplicity in F_j, and put L=m-d/3>1. The accepted budget is j<=7L-Delta, with Delta>0 as in 16l; in particular d<=3m-4. We also use the weaker direct factor-count consequence

    j <= 7m-2d-ceil(d/3).                         (1)

Indeed the other triple factor has multiplicity at least d and the simple factor b has multiplicity at least ceil(d/3). This does not assume that F_j is divisible by K, and it includes ties. The accepted simple-minimizer exclusion licenses starting with a triple minimum.

At either triple line a=epsilon b, X=b, the exact accepted cubic chart is

    R=zeta^3+alpha(s,X) zeta+beta(s,X),
    F=sum_l c_l(s,X) zeta^l.

All original s orders are integral, all c_l have order at least j, c_d has order j and c_l has order greater than j for l<d. Here wt(s)=wt(X)=1, wt(zeta)=7/3. The transverse chart and its inverse have no negative s or transverse orders. The entire W=B_s-R^n, not an alleged remainder G, has strictly positive coefficientwise s order. Set

    r=min_{l<=d} ord(c_l)/(3m-l),
    lambda=min(ord(alpha)/2,ord(beta)/3).

We prove a contradiction under lambda<r. Since r<=j/(3L)<7/3, the only possibilities for lambda are

    1/3, 1/2, 2/3, 1, 4/3, 3/2, 5/3, 2.        (2)

Infinite alpha or beta orders are allowed; separation requires at least one finite order. These are original-order restrictions, not genericity assumptions.

## 2. Initial-form tools, including the full lower B

All formal constructions below take place over a finite algebraic extension of kbar(X), with the explicitly stated finite ramification in s. Algebraic coefficient functions retain their homogeneous weights. Constants of differentiation with respect to X in these fields are kbar. Positive transverse balances ensure that an infinite Taylor series has only finitely many terms at any fixed initial weight.

We repeatedly use the following elementary argument. Suppose a local reference z has weight D, A has total weight mD, and, at z=s^eta Z with 0<eta<D, the A initial is monic of degree m, with no Z^{m-1} term. Suppose also that every coefficient of B-z^n has positive s order. A possible earlier B initial at order nu<n eta has highest degree v satisfying v eta<nu. If its top coefficient is h(X), Euler gives

    X h' = (nD-nu-v(D-eta))h,
    nD-nu-v(D-eta) > nD-D nu/eta > 0.            (3)

The highest Z^{m+v-1} coefficient of its Jacobian with the monic A initial is m h'. This power is positive. If the predicted bracket order is below the target, that coefficient is zero; if it meets a nonzero target constant in Z, that coefficient is still zero. If it is above the target, the full bracket starts too late. Hence an earlier B initial is impossible. This is an argument about the earliest term of the WHOLE B; it neither discards scalar kernels nor assumes ord G>=2j.

At order n eta, B is monic of degree n, and its other terms have smaller degree. When the bracket at these leading orders is zero, weighted Euler and commutation give Q^m=P^n: equivalently the logarithmic Z derivatives agree and monicity fixes the Z-independent ratio. Unique factorization and gcd(m,n)=1 then give P=V^m, Q=V^n with V monic linear. The absent Z^{m-1} coefficient forces V=Z. Thus a nonzero lower correction in P is impossible. The sole potential exception is equality of the leading bracket order with the target order.

The same proof applies to a reference of local multiplicity e: use monic degrees em,en and transverse weight D/e. In the commuting case the common monic factor has degree e. For e=2, a nonzero change to a monic quadratic produces a difference of its mth powers of degree at least 2(m-1); for e=3 the analogous degree is at least 3(m-1). This comparison is factored, not an expansion of the pair.

On a two-sheet product, take the GLOBAL earliest B order and then a component where its highest coefficient is nonzero. Equation (3) applies on that component because A is monic on both. Later, monic B initials are present on both components. This avoids the invalid inference that one component must separately realize every first nonzero remainder.

## 3. First splitting and legitimate division of both outputs

Put zeta=s^lambda Y and e0=denominator(lambda). The scaled reference is R=s^{3lambda} Rbar and

    Rbar(0)=S(Y)=Y^3+A(X)Y+B(X),
    h=7/3-lambda>0,  D=7-3lambda=3h.

S is not Y^3. Let mu be the first order of F after this substitution. The strict inequality lambda<r, including all higher Taylor terms, gives

    3m lambda < mu <= j+d lambda.                (4)

The upper bound is the actual c_d Y^d term; distinct Y degrees cannot cancel it. The initial polynomial phi has degree at most d.

Initially A has order 3m lambda and initial S^m. Apply the full-B top-coefficient argument before dividing B. It excludes all orders below 3n lambda. At that order Q is monic of degree 3n. The possible equality with the original target would require

    lambda=N/(3(m+n)-1)=(7m-1)/(3m).

Neither twice nor three times this number is integral for m>=4, whereas lambda must satisfy one of those integrality conditions. If the leading bracket order is greater than N there is a direct contradiction; otherwise it is strictly smaller. Euler and commutation then force Q=S^n. Consequently division is licensed and gives

    Abar=s^{-3m lambda} A_s,
    Bbar=s^{-3n lambda} B_s,
    Fbar=s^{-3m lambda} F,
    J=ord Fbar=mu-3m lambda>0,
    Bbar-Rbar^n has strictly positive coefficient orders.      (5)

All scalar A terms remain, now a_i s^{D(m-i)} Rbar^i. B has not been simplified by any target shear or kernel erasure. Its positive difference in (5) follows from its actual initial, not from the original positive order alone.

The new bracket in (Y,X) has target order

    N'=N-(3(m+n)-1)lambda = D T+2-2lambda>0,      (6)

with a nonzero leading coefficient constant in Y. To check signs, initially zeta_0=X^{1/3}(X^2-a^2), and 2c a^3 a_{zeta_0}=-c X^{5/3}+c X^{-2/3}zeta_0. The first coefficient is the same on both actual triple lines epsilon=+1,-1. The second term, and all returning-coordinate corrections, are later at every positive transverse balance. In (6) the leading coefficient is -c X^{5/3}; it is not asserted that the full target is constant in Y.

Finally (4) and the accepted strict budget give

    J <= j-3L lambda <= D L-Delta.               (7)

Choose a minimizing root of phi relative to the multiplicities of S. Its relative multiplicity delta' is at most deg(phi)/3<=d/3. Thus J/(m-delta')<D. S has either three simple roots or exactly one simple and one double root. A depressed cubic with a triple root is a pure cube Y^3, already excluded here.

## 4. Every simple minimum after splitting is impossible

Suppose a simple root of S is minimizing, with t=ord_root(phi). Since deg(phi)<=3m-4, t<=m-2. The simple inverse z=Rbar near the returning root exists over the coefficient field with no further s ramification. Its coefficient orders remain in (1/e0)Z. All Fbar coefficients have order at least J; the coefficient of z^t has order J and lower indices have greater order.

At the first F balance

    eta=min_{l<=t} ord(Fbar_l)/(m-l)
         <= J/(m-t)<D,

the A initial is P=Z^m+U, 0!=U, deg U<=t<=m-2. Higher indices and all scalar reference terms are later. The whole B difference remains coefficientwise positive under the returning inverse. Section 2 leaves only

    eta=eta_*:=N'/T=D+(2-2lambda)/T.             (8)

For lambda<=1 this contradicts eta<D. For lambda>1, the four values in (2) are 4/3,3/2,5/3,2. In each case e0 D is integral and the fractional part of e0 eta_* has reduced denominator 4q+5: e0(2lambda-2) is respectively 2,2,4,2 and T=2(4q+5). This denominator is greater than m=3q+4. A nonzero correction of degree l<m at (8) would require e0(m-l)eta_* integral, which is impossible because 0<m-l<=m. Thus (8) also cannot occur.

This proves the entire three-simple case and excludes any tie involving the simple root in the one-plus-double case. It uses the original coefficient-order lattice, not just a rational-weight inequality.

## 5. One plus double: integer first split and the second coalesced case

Write S=(Y-a)^2(Y+2a), a!=0. Both cubic coefficients are nonzero, so 2lambda and 3lambda are integral. Thus lambda is 1 or 2. The double root must be a STRICT minimizing root, by section 4. Set e=ord_{Y-a}(phi), t=floor(e/2). The simple-root multiplicity is at least t+1, and hence

    deg(phi)>=3t+1 if e=2t,
    deg(phi)>=3t+2 if e=2t+1.                   (9)

In particular e<=2m-3. Notice that strictness in (9) is earned; it must not be replaced by an unproved generic double-minimum assumption.

The returning critical point is obtained by the formal implicit function theorem since S'' at the double root is nonzero. Subtract its value and take a square root of the remaining transverse unit. This gives an exact Morse chart

    Rbar=xi(s,X)+omega^2,
    wt(omega)=D/2, wt(xi)=D,

over a finite algebraic coefficient extension. There are no negative original s or omega orders; all s orders are now integral because lambda is integral. The Fbar coefficients have orders >=J, with first multiplicity e at order J. The whole Bbar-Rbar^n still has positive coefficient orders. Put

    rho=min_{l<=e} ord(Fbar_l)/(2m-l)<D/2.

Consider first ord(xi)>=2rho, including xi=0. The A initial is (Y^2+b)^m+U, where U is nonzero and has degree at most e<=2m-3. The scalar reference terms are later. Section 2 excludes earlier B initials even if their bracket would meet the constant target. At its monic order, commuting initials are impossible by the quadratic power-difference degree. Therefore the only possibility is

    rho=N'/(2T+1).                              (10)

For lambda=1, D=4 and N'=4T. This fraction has reduced denominator 2T+1=16q+21>2m. Its double is not integral, so xi is later, b=0. No nonzero A correction of degree below 2m can satisfy the integral original s-order condition. This contradicts the definition of the balance.

For lambda=2, D=1 and N'=T-2. The common divisor of T-2 and 2T+1 is either 1 or 5. In the first case the same denominator argument applies. In the second, q=5h+4 for an integer h>=0 and

    m=15h+16, n=25h+27,
    rho=8(h+1)/(16h+17).

This fraction is reduced. Again 2rho is not integral, so b=0. Integral original orders force every index l in the A initial to satisfy (2m-l)rho integral. Consequently A's initial is divisible by Y^{14h+15}. The same condition for B forces its initial to be divisible by Y^{2h+3}. Their Jacobian is therefore divisible by Y^{16h+17}. It cannot equal the nonzero constant-in-Y target at (10). Vanishing of an allowed coefficient can only increase these divisibilities. This disposes of the exceptional congruence without using, or purporting to classify, the coalesced ODE solutions from 16l.

Thus the second coalesced Morse regime is impossible.

## 6. Second separated Morse regime: full two-sheet proof

Let kappa=ord(xi)<2rho. For lambda=2, integrality gives kappa>=1 while 2rho<D=1, a contradiction. Hence only lambda=1 remains, with D=4, N'=4T and kappa in {1,2,3}.

Write Fbar=sum c_l omega^l. Exact regrouping gives

    U(z)=sum_{h>=0} c_{2h}(z-xi)^h,
    V(z)=sum_{h>=0} c_{2h+1}(z-xi)^h,
    Fbar=U(z) +/- a sqrt(1-z/xi) V(z), a^2=-xi. (11)

All U,V coefficient orders are at least J. These series converge coefficientwise since kappa>0; on the balance z=s^eta Z used below eta>kappa, so the square-root expansion also converges in increasing s order. For e=2t, U_t has order J; for e=2t+1, V_t has order J. Contributions from higher transverse indices gain a positive multiple of kappa and cannot cancel these statements.

Define global two-sheet coefficient orders

    q_l=min(ord U_l,kappa/2+ord V_l).

This minimum is realized on at least one of the two signs: characteristic zero prevents cancellation on both. The strict separation inequality implies

    q_l+kappa*l > m*kappa  for l<m.

Indeed every original term c_i omega^i evaluated at omega of order kappa/2 lies strictly above m*kappa; regrouping cannot lower its order. Hence

    eta=min_{l<m} q_l/(m-l)>kappa,
    eta<=J/(m-t)                  if e=2t,
    eta<=(J+kappa/2)/(m-t)        if e=2t+1.     (12)

Higher analytic indices l>t are later: in the odd case they gain at least eta-kappa/2>0, and the even case is stronger. Nonconstant terms of sqrt(1-z/xi) gain eta-kappa>0. Thus the global A initials are

    P_+=Z^m+U_+(Z), P_-=Z^m+U_-(Z),
    deg U_+,deg U_- <= t<=m-2,

and not both corrections vanish.

The necessary sharp margin comes from the ORIGINAL degree budget, not a new local normal-form assumption. Since lambda=1, (1) and (4) give

    J<=4m-d-ceil(d/3).

Combine d>=deg(phi) with (9):

    J<=4(m-t)-2 if e=2t,
    J<=4(m-t)-3 if e=2t+1.                     (13)

Equations (12)-(13) imply eta<4 and, more precisely,

    eta<=4-2/(m-t)                         (even),
    eta<=4-(3-kappa/2)/(m-t)                (odd).

The exact inverse sheet has omega_z=1/(2omega). Thus its Jacobian target first has order 4T-kappa/2, with a nonzero coefficient constant in Z on each sheet. The signs on these two sheets are opposite, but we do not argue by comparing them. Returning shifts and all higher square-root terms gain positive order eta-kappa. Since T>m-t and kappa<=3, the two bounds above yield the STRICT margin

    T*eta < 4T-kappa/2.                         (14)

For the even case, the saved amount is 2T/(m-t)>kappa/2. For the odd case it is (3-kappa/2)T/(m-t)>kappa/2, also at kappa=3.

It remains essential to check the entire B rather than a selectively rebuilt G. Regroup Wbar=Bbar-Rbar^n into its even and odd omega parts exactly as in (11). All analytic coefficient orders remain strictly positive. At eta>kappa, nonconstant square-root terms cannot be the GLOBAL earliest term: the corresponding unmultiplied analytic term occurs earlier on at least one sign. A global earlier B initial at nu<n eta therefore has highest degree v with v eta<nu. Equation (3), with D=4, excludes it on a component where its top coefficient is nonzero. The other component may have zero such coefficient; no division by an element of the product ring is used.

At n eta both B initials are monic of degree n, with all corrections of smaller degree. All scalar kernels, including any terms linear or constant in the local reference, are still part of this argument. By (14) the two leading Jacobians must commute. Euler and unique factorization apply separately to each field component and force U_+=U_-=0, contradicting the global first balance. This excludes the second separated regime.

## 7. Coverage, controls, and limitations

The first split has only three-simple or one-plus-double possibilities. Section 4 handles the former and every simple tie in the latter. The remaining double minimum is strict; its second Morse regimes are exhaustively coalesced (including xi=0) or separated (xi nonzero). Sections 5 and 6 handle these respectively. All finite and infinite deformation orders are included. No discriminant boundary has been replaced by a generic three-simple argument.

The coefficient-field extensions are harmless for this necessary contradiction. The first split introduces only the denominator of lambda, at most three; simple-root inverses preserve that lattice. In the one-plus-double case lambda is integral, so the second coalesced argument genuinely uses integral original orders. The second separated square root introduces at most an additional factor two. All root/critical-point choices require finite algebraic extensions of the coefficient function field and formal Hensel inverses, not an asserted same-field normal form for the original polynomial source. Localization at generic X is only a test of an existing identity; it does not remove a putative polynomial identity from consideration.

Manual changed-hypothesis controls, not claimed full-source examples:

1. The actual depressed cubic (Y-a)^2(Y+2a)=Y^3-3a^2Y+2a^3 has a simple and a double root. Replacing a cubic unfolding by a pure cube erases this case; the proof retains both coefficients.
2. In (11), choosing U=aV nonzero cancels one constant square-root sign but doubles the other. This refutes a one-sheet first-nonzero shortcut and is why the minimum is taken globally.
3. An arbitrary positive-order B correction s h(X)z^v need not start at 2j. Such terms are retained in (3); an unsupported G>=2j statement would lose them.
4. The polynomial phi=S^t has equal relative multiplicities at the simple and double roots. It does not satisfy strictness (9), and the saving in (13) would fail if section 4 had not first excluded that tie.
5. If arbitrary rational original s orders were allowed, the denominator contradiction in (8) would no longer follow. The proof checks the actual original lattice at every returning chart rather than silently replacing s by a rescaled valuation variable.
6. In the lambda=2 exceptional congruence, both initial polynomials have positive Y multiplicity. Their Jacobian's positive multiplicity is a direct obstruction to a constant target; ignoring the permitted B indices would miss this control.

These are manual algebraic checks of the cited steps, not executed programs, numerical samples, or candidate Keller points. There is no new claim of properness, an ideal unit certificate, or a solver gain. Together with accepted 16l this narrows the literal hypothetical receiver to its already specified coalesced resonance conditions only. The existence of abstract coalesced ODE solutions is not addressed or overturned here.

Publication: private body was read WHOLE, own raised-OPEN extraction checked before closing, and only the two named scientific input hashes were rechecked. Final publication/custody metadata are in the owned box. No further derivation, gate launch, or downstream task is authorized by this report.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19793`.
- Body SHA-256:
  `4de52d4197c5c9da61a7db0e0487b5a19b1ff81bdd73df0bf21753b2fbc87678`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
