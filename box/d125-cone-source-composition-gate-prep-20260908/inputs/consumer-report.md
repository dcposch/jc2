# Cone product-ring consumer: a conditional contradiction

2026-09-08. **PROVED CONDITIONAL ALGEBRAIC LEMMA, producer-checked.** The explicit interface below is inconsistent. This is NOT a claim that any D125 source, scaling, moving lift or degeneration supplies it. In particular no live source-derivation report was read. The argument takes global initial tuples before branch selection; the earlier common-branch countercontrol is not ignored or misidentified as a source point.

## 1. Exact hypotheses

Work over a characteristic-zero field K and K[[s]]. Let

    H=p²V0, V0=g³+p³, w(g)=5, w(p)=−7,
    R_s=H+T_s,

where T_s lies in sK[[s]][g,p], is odd, has degree<5 and weight<=1. Thus R_s is odd, degree5 and monic lexicographically at g³p². Assume odd F,G with coefficientwise degree/weight bounds13/3 and23/5 respectively, and

    j in {2,4,6,8}, ord(F)=j, F_j=H C,
    C even, homogeneous of degree10−j>0, normal modulo g³p²,
    C not zero modulo V0, ord(G)>=2j,
    alpha,beta,delta in K[[s]], ord(alpha)>=10, ord(delta)>=20.

Infinity is allowed for these scalar orders. The required definitions are

    A=R_s³+alpha R_s+F,
    B*=B−beta A
      =R_s⁵+(delta−5alpha²/9)R_s
                 +(5R_s²/3−5alpha/9)F+G.                 (1)

The task's initial A formula omitted +F; root explicitly confirmed this correction before the proof. Finally assume the original-coordinate bracket has first s-order36 and coefficient c g² with c!=0. In fact vanishing through every order<36 suffices for the contradiction.

All of these are HYPOTHESES. No14v first-contact statement, ordinary-lift condition, total-degree dilation or saturation consequence is silently imported for the cone. The preceding cone report is history, not a source-provenance premise.

## 2. Finite normal blocks and regular GLOBAL initials

Divide lexicographically by R_s. Replacement of g³p² decreases g-degree and does not increase total degree or weight. It follows coefficientwise and finitely that

    F=P0+R_s P1+R_s²P2,
    G=Q0+R_s Q1+...+R_s⁴Q4,

where Pi,Qi are monomial-normal, with degree bounds13−5i,23−5i, weight bounds3−i,5−i, and orders at least j,2j. No actual high power is expanded. Since C is normal, uniqueness of the order-j division gives P1_j=C, P0_j=P2_j=0. Put q=ord(P0)>j, possibly infinity.

Extend constants to Kbar. A normal polynomial of weight<=5 injects into the product of the three branch rings Kbar[p]. Indeed, if it vanishes on all lines g=zeta p, zeta³=−1, then V0 divides it. The quotient has weight<=−10, hence is divisible by p². The original polynomial is then divisible by H, incompatible with a nonzero normal remainder. This rederives the product injection, not an individual-branch injection.

At each generic line there is an implicit root g_zeta(s,z), R_s(g_zeta,p)=z, since its initial derivative is3zeta²p⁴, a unit in Kbar(p). Set

    eta=min(j/2,q/3),  j/3<eta<=j/2<=4,            (2)

with the usual q=infinity convention, and z=s^eta Z. A finite parameter extension clears fractional exponents. For each nonzero normal block, its first coefficient after taking ALL three branches is its regular restriction tuple, nonzero somewhere by product injection. Implicit corrections have strictly positive extra s-order. Thus the global minimum of block order+i eta has a regular initial in

    (Kbar[p])³[Z].

Different block indices give distinct Z powers, preventing cancellation at this global minimum. Individual zero components are allowed. No later first nonzero coefficient on such a component is asserted regular.

Since ord(alpha)>=10>2eta, A has weight3eta and monic initial

    P(Z)=Z³+uZ+v.                                (3)

The tuple u is even and v odd. Some component is nonconstant: if eta=j/2, u is C restricted to the branches, and at least one entry is a nonzero scalar times p^(10−j); if eta=q/3<j/2, v is a nonzero odd regular tuple. Equality is covered by the first case. The R_s²P2 term has weight at least j+2eta>3eta. This also handles q=infinity and alpha identically zero.

## 3. The stronger scalar orders remove every lower linear B initial

In (1), delta R_s and alpha²R_s have weight>=20+eta>5eta, and alpha F has weight>=10+3eta>5eta. For the remaining blocks,

    R_s²P0: q+2eta>=5eta,
    R_s³P1: j+3eta>=5eta,
    R_s⁴P2: j+4eta>5eta,
    R_s^i Qi, i>=1: 2j+i eta>=5eta.

These inequalities use only q>=3eta, j>=2eta and eta<=4. Thus if the global B* weight nu is below5eta, its initial is JUST a nonzero odd regular tuple e from Q0, independent of Z. In particular the potentially dangerous lower dZ term is absent, not merely assumed diagonal.

The original bracket transforms by division by R_g. On all branches its order remains36, with initial c/(3p²). For global initial weights3eta and nu, the possible leading bracket has weight2eta+nu and coefficient

    P_Z DQ−DP Q_Z,  D=d/dp componentwise.

This coefficient identity is valid even with zero divisors: differentiation does not lower the extra s-order of implicit corrections. If nu<5eta, then 2eta+nu<7eta<=28<36, so the initial bracket must vanish. But with Q=e its Z² coefficient is3De. Therefore e is componentwise constant, and oddness forces e=0 on EVERY component, a contradiction.

Consequently nu=5eta: the exact R_s⁵ term ensures nu cannot be larger, and its coefficient1 cannot cancel with lower normal blocks at the same global weight. The R_s⁴ coefficient occurs strictly later. Hence

    Q(Z)=Z⁵+c3 Z³+c2 Z²+c1 Z+c0                (4)

is monic on ALL three branches, with regular tuple coefficients. Both A and B now have their actual initial at the global weight on each branch, by monicity. This is where branch selection becomes legitimate; it was not used before establishing (4).

## 4. The3/5 coefficient lemma finishes the conditional contradiction

Since7eta<=28<36, (3) and(4) commute in the product differential ring. Select a branch where u or v is nonconstant. Both polynomials remain monic of degrees3 and5 over Kbar(p). The accepted15f coefficient argument applies, and can be stated without discarding ANY integration constants.

For a cubic Z³+aZ+b and quintic Z⁵+cZ³+dZ²+eZ+f, vanishing bracket successively yields

    c=5a/3+c_0, d=5b/3+d_0,
    e=5a²/9+c_0 a+e_0,
    f=10ab/9+c_0 b+(2/3)d_0 a+f_0.

All four subscripted quantities are constants on the selected branch; they need not be identified with diagonal constants of the product. Put btilde=b+3d_0/5 and K0=9e_0/5. The two remaining equations are

    (a²−K0)a'−6btilde btilde'=0,
    2a btilde a'+(a²−K0)btilde'=0.

The first integral is L0=a³/3−K0 a−3btilde². If a'!=0, the determinant vanishes and gives

    (7/3)a⁴−6K0 a²−4L0 a+K0²=0.

This nonzero scalar polynomial forces a constant in Kbar(p), a contradiction. Hence a'=0, and the first equation also gives btilde'=0. Both cubic coefficients are constant, contradicting the chosen branch. d_0/f_0 were retained; parity is not needed for this final field lemma. Product zero divisors are irrelevant AFTER restriction to the selected monic component.

Thus no formal pair satisfies the stated interface. No source-to-interface, properness, boundary-existence or JC2 conclusion is part of this theorem.

## Evidence and terminal scope

The complete accepted15f producer proof and the terminal cone packet were read. All local cone statements needed above are rederived; no pending source theorem or live peer is charged. Ten capped normal/−O controls pass with zero Assert nodes and byte-identical witnesses. They check universal formal3/5 elimination with d_0/f_0, its first integral/quartic, finite valuation illustrations, and exact product examples. Actual mutations change the quintic constant coefficient, omit the d_0 shift, change the quartic coefficient, or replace an odd lower tuple by a constant tuple. A separate commuting example with non-diagonal d illustrates why a weaker dZ argument would need care; the present order bounds eliminate d entirely. Finite valuation tables are controls, not substitutes for the inequalities in Section3.

No actual H³/H⁵, A15/B25, full source, CAS, AWS, extra agent, live peer or shared/protected edit. The owned transaction/custody pins all writers and final evidence. **PRODUCER-CHECKED CONDITIONAL CONSUMER ONLY; source applicability remains an independent question. STOP/IDLE, all writers finished.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8451`.
- Body SHA-256:
  `c251264b8cb16dff755bb7f40d55fb432baab818183bf1d5cbee4b548dcad95a`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
