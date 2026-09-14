# D125 k=s⁴: exact residue reduction and a complete unguarded six-jet survivor

2026-09-07. **DESK PASS: finite-jet survivor, not an arc.** Over K=Q[b]/(b⁴−3), the explicit formulas below satisfy the COMPLETE UNGUARDED moving-face source modulo s⁷ with k=s⁴, together with the three explicitly imposed saturated low equations. Thus the order-six residue conditions do not exclude m=4. The guard zk−1 is NOT imposed and cannot hold with nilpotent k. No extension through order7 or beyond, guarded point, proper guarded ideal, or JC2 consequence is claimed.

## 1. General residue condition, including intermediate orders and kernels

Use accepted14c/14g, the promoted first-tangent lemma14i, and the literal lift

    φ(g)=v⁻¹, φ(p)=v⁴u−v−v⁻¹,
    R_t=p²(p³+g³)+(t+3)gp²+t p³−(t+3)p.

For a genuine k=s⁴ finite arc near t₀≠−3, put h=t₀+3. Its low equations are a01=0, 9e=5kx and x²=3ky, so ord(x)=2 and x₂²=−3h³. Choose the unique formal reference t(s) with y=−(t(s)+3)³. This is only a reference choice. Whole scalar B→B−β(s)A shears are permitted operations preserving every face, origin, parity and lift row. The accepted first-tangent lemma, a01=0, the chosen y and e=O(s⁶) remove the first-order departure. The first nonzero A departure therefore has order2.

Write R=R_{t(s)}, F=A−R³. The orders2 and4 centralizer identities imply F₂=R₀C. Here C is even, ordinary, degree≤8 and weight5i−7j≤0. Put

    F=s²RC+s³D(s),     D=D(0).

All intermediate terms are retained in the formal polynomial D(s). In particular D need NOT be divisible by R₀. It is odd, ordinary, degree≤13, weight≤1 and satisfies the A lower side i≤2j. With u=gp,v=p², the actual low constraints are

    C(0,0)=0, C_v(0,0)=0, ξ:=C_u(0,0), ξ²=−3h,
    [p]D=[p³]D=0.

If t₁=[s]t(s), the additional low identity is [gp²]D=−ξ t₁/2; the survivor below has t₁=0 and this coefficient zero.

For clarity about every kernel, work temporarily in K[g,p,R₀⁻¹][[s]] and define the binomial root X=A^(1/3) with X₀=R₀. This does NOT assert X polynomial. Expanding X⁵ through order6 gives polynomial terms through5 and the only possible pole at6:

    (1/R₀)((5/9)D²−(5/81)C³).

Recursive centralizer subtraction is justified by clearing powers of R₀: the polynomial centralizer K[R₀] implies the localized centralizer K[R₀,R₀⁻¹]. At orders2–5, parity and total-degree bounds leave only scalar multiples of X and A. Scalar A multiples are whole target shears. The low e₂=e₃=0 kill the order2/3 X kernels. Since C(0)=0 and D(s) has no linear receiver term, the polynomial binomial terms at4/5 likewise have no p term; e₄=e₅=0 kill those X kernels too.

In particular, an order4 kernel γ₄s⁴X would contribute γ₄C/(3R₀) at order6. It must NOT be silently dropped: its order4 p coefficient is −hγ₄, so γ₄=0. The checker mutates both this factor and its low-e removal. At order6 the only additional negative-power kernel is a scalar/R₀; evaluation of its numerator at the origin, where C=D=0, kills that scalar. Consequently the genuine necessary residue condition is

    R₀ divides 9D²−C³.

The surviving order6 scalar-X kernel controls e₆ and is retained below. No polynomiality or full Jacobian completion is inferred from the residue condition alone.

## 2. The small ordinary spaces are exact

For C, the literal even degree≤8, weight≤0 support has15 monomials, all of the form uᵃvᵇ with a+b≤4. Set

    E=u+v−1, L=vE.

The complete linear negative-row matrix has rank6. Its kernel has the rational basis

    1,E,E²,E³,E⁴,L,EL,E²L,L².

Both E and L lift ordinarily; the owned witness emits all15 columns, every nonzero negative row, the exact kernel, and the displayed basis coordinates. Thus this is not just an inclusion or modular rank test. The analogous literal D support has33 columns; its complete ordinary kernel has dimension20, and adding [p]D=[p³]D=0 gives dimension18. Exact rational matrices/kernels are retained; no nonlinear solve was performed.

Every such D is divisible by p. The only negative exponents appearing when D/p is written in u,v are uⁱ/v for i=3,…,7. On T=R₀/p=0 they reduce polynomially using

    u³/v=h−hu−t₀v−v².

The even quotient retains F=u³+v³+huv+t₀v²−hv=0 and v invertible: p is a unit on T because T mod p=−h. The often useful E,L relation is

    3L²+[-3E²+(t₀−3)E−3]L+E(E+1)³=0.

Its literal substitution is E·F, not F; it is not a global replacement of the original curve without localization/exception control. In particular no square/non-square or smooth-projective-quartic hypothesis is inferred from it. The finite construction below makes such an exclusion route unnecessary at this order.

## 3. An exact residue survivor at t₀=−4

Now fix h=−1 and the nonzero finite rational algebra K=Q[b]/(b⁴−3). No field irreducibility assumption is needed. Define

    R=R_−4=p⁵+g³p²−gp²−4p³+p,       T=R/p,
    S=p³+gp²−p,  r=g²p+gp²+p,  Z=gp+p²,
    q=g³p²+3g²p³+2gp⁴+p³,
    C=b²(r²−TZ),      D=(b³/3)(r³−Tq).

The literal C has degree≤6, weight≤0, is even and has coefficients C₀=0, C_gp=−b², C_p²=0. Therefore C_gp²=b⁴=3=−3h. D has degree≤9, weight≤1, the A lower support, odd parity, and [p]D=[gp²]D=[p³]D=0.

R,T,r,Z all lift ordinarily. The lift of T has lowest v-power1, and the COMPLETE negative part of φ(q) is v⁻¹. Hence Tq and D lift ordinarily; the same is immediate for C. These are checked on the literal degree≤9 expressions, not inferred from names or a selected support row.

For an explicit global quotient, put

    M=−2r³q+Tq²+3r⁴Z−3r²TZ²+T²Z³.

The universal multiplication identity gives 9D²−C³=b⁶TM. Every term of M is divisible by p, since r,Z are divisible by p and q by p². Thus

    W=(5/81)(9D²−C³)/R = (5b⁶/81)(M/p)

is an ordinary receiver POLYNOMIAL; division by R is not a localization. It has degree≤13 and weight≤1 by exact product/division bounds. It is odd. Each term in M/p has total degree at least5, so W has neither constant nor linear g/p terms. Finally φ(W) is ordinary: φ(R) has v-order0, whereas φ(9D²−C³) is ordinary, so Laurent valuation gives ord_v φ(W)≥0. No cancellation of a nilpotent coefficient is used.

## 4. Complete finite jet, including the moving s⁴ faces

Put C*=E+1+L and

    U=r−R−2RC*+4R²S,       γ=−5b²/9.

This factored U is ordinary, odd, degree≤13, has the A lower support and unique weight3 leader g²p. Its total-degree-three part is EXACTLY g²p; its p, gp² and p³ coefficients are zero.

Over K[s]/(s⁷), set k=s⁴ and

    A=R³+s²RC+s³D+s⁴U,

    B=R⁵+(5/3)s²R³C+(5/3)s³R²D
        +s⁴[(5/3)R²U+(5/9)RC²]
        +(10/9)s⁵CD
        +s⁶[(10/9)CU+W+γR].

The full formal binomial/Jacobian identity, with the intermediate s³/s⁵ terms and the CU term retained, proves [A,B]=0 modulo s⁷. An independent tiny R=g control verifies every order through6 and rejects a changed CU factor. No actual degree15/25 pair is expanded.

ALL source contracts modulo s⁷ hold. Every displayed factor lifts ordinarily, including W, so every negative row vanishes. A's corrections have degree≤13 and permitted lower/weight bounds; B's corrections have degree≤23 and weight≤5. Thus the complete total faces remain H³/H⁵. The s⁴ A inner leader is g²p, and the s⁴ B inner leader is (5/3)g⁸p⁵, exactly as required. Other corrections have strictly smaller inner weight, including W and γR. Origins and odd parity hold coefficientwise. These support statements preserve prescribed zero face slots as well as nonzero endpoints.

The actual low coefficients are

    a01=0, x=−b²s², y=1, e=−5b²s⁶/9.

They satisfy a01=0, 9e=5kx and x²=3ky exactly in the stated finite algebra, using b⁴=3. In particular this is not the earlier x=0 mixed-order toy. The γR term intentionally supplies e₆; W supplies no linear term.

The fixed B_g=5s⁸/9 and the target Jacobian −5s¹²g²/9 vanish modulo s⁷. Their first NONZERO orders8 and12 are outside this verification and remain untested. The inverse guard is omitted, not weakened or claimed recoverable. This construction is a point of the unguarded source plus the three specified saturated low equations over a nonreduced finite algebra; it is NOT a point of the guarded source or of an asserted full k-saturation.

## 5. Evidence and exact stop

The first ten capped normal/−O runs certify the ordinary spaces, low C map and the linear-C kernel. A second ten final runs certify the literal residue construction, q's full negative part, U's low jet, the universal quotient identity, the complete order-six formal bracket, and actual polynomial multiplication/reduction of the low equations modulo b⁴−3. Real changed-q, changed-U, changed-CU and changed-b⁴ mutations fail the same checker. Zero Assert nodes; all runs use −B with bytecode disabled before helper import.

The initial jet runner already passed, but its b⁴ control only compared scalar constants. It was strengthened to actual polynomial multiplication in the finite coefficient algebra; only `jet-final-*` is charged for that control. Earlier owned evidence is retained. Final jet witness SHA256 `a7e4e151552ea554e4fee4144627d5f0acf4ea6ed9101346ccbf7265506c0426`; ordinary-space witness `3cb4d2ec0d02c862ea9988379f0216f65895900d88c6717b542aebf3a16fde2d`.

Root supplied the small C-space/curve seeds and the explicit t=−4 residue candidate. This lane independently derived the low-e kernel removal, exact linear-space certificates, and the U/γ completion to the full finite jet. The prior mixed-order gate was live and was not read. No extra primary theorem, smoothness assertion, nonlinear solve, full source expansion, AWS/SSH/CAS, shared edit or baseline change was used. The exact next gap is extension beyond order6 while retaining every future face/Jacobian/lift row. No such extension is claimed or attempted. All writers idle at custody publication. **STOP/IDLE.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10167`.
- Body SHA-256:
  `ed32d0364931bb9980deab5800b9fc083845d0e9eb7cb296fcee2eff3de935cb`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
