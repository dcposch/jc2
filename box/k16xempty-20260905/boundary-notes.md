# Uniform complementary-chart audit

Author: boundary_structure subagent. All charged frozen inputs were already mechanically verified by root. This note uses the frozen F3/Theorem H definitions and the lane-owned exact t=3 reconstruction. It supplies exact reformulations and controls, not all-t emptiness.

## 1. A homogeneous interpretation of the boundary

Write R=k[c_1,...,c_(t-1),b], q=2t+1, and reconstruct

    B=M+bN, eta=rho+b sigma,
    Delta=N-sigma, A=rho-M, H=N rho-M sigma.

The weights are

    wt(M)=2t+1, wt(N)=t, wt(rho)=2t, wt(sigma)=t-1,
    wt(H)=3t.

H is homogeneous even though Delta and A are not. There is an exact identity in R, before imposing any E row:

    H=N eta-B sigma.

Therefore in the slice algebra R[s]/(J,B-eta,1-sB),

    H=B Delta,       A=b Delta.

Since B is a unit there, the closed ideals (H), (Delta), and (Delta,A) have the same quotient. In particular the complementary chart is precisely V(H) in X, scheme-theoretically, and the main chart is D(H) in X. This includes nilpotents; it is not merely a statement about geometric points.

Under the exact normalization U ≅ G_m × X, let v=B/eta. Since H has weight 3t, its pullback is v^(3t) H_X. Thus V(H) and D(H) are carried to G_m × V(H_X) and G_m × D(H_X). More explicitly,

    Delta_X=v^(-t) (N-v sigma)=v^(-t) H/eta.

Thus the entire main/boundary decomposition has the following homogeneous cone version. Put T=B eta. Then, in characteristic zero and factorwise,

    X_main is empty <=> T H lies in radical(J),
    X_boundary is empty <=> T lies in radical(J+(H)).

Proof: the first inverse chart localizes R/J at TH; the second localizes R/(J,H) at T. For a finitely generated k-algebra A, A_f is zero exactly when some power of f is zero in A. No projective argument is needed here.

This reformulation is useful for certificate gluing. If exact certificates give

    (T H)^r in J,
    T^s = H L modulo J,

then in R/J,

    T^(r(s+1)) = T^r (T^s)^r = T^r H^r L^r = 0.

Consequently T^(r(s+1)) lies in J. This is an explicit exponent rule. It does not produce r,s uniformly.

The homogeneous form does not authorize promotion of one-prime modular radical membership. For example, (x+p y) contains x modulo p but does not contain any positive power of x over Q. The homogeneous properness route would require a genuine empty weighted Proj statement for a closed cone, or other verified hypotheses; localization at T remains an open condition.

## 2. The boundary is not a degenerate normalization locus

The literal b derivative of the slice equation is Delta. On eta ≠ 0 one has

    partial_b(B/eta)=H/eta^2.

This is an ambient parameter derivative; there is no claim that partial_b is tangent to V(J). H=0 says the ratio B/eta has zero b derivative at fixed C. It does not say C has a repeated root, nor that the actual terminal scheme is singular.

Let D_c=sum_j j c_j partial_(c_j), omitting the b direction. The weight identities give

    D_c Delta = t N-(t-1)sigma = N+(t-1)Delta,
    D_c A = 2t rho-(2t+1)M = -M+2t A.

Hence on (Delta,A),

    D_c(B-eta)=D_c(b Delta-A)=bN+M=B.

B is invertible on the complementary chart. Thus coefficient scaling is transverse to the normalization equation there. Vanishing of its b derivative cannot be used as a contradiction: the nonzero scaling derivative is exactly what makes the global normalization work on this locus.

One could also cover the decoupled boundary by N≠0 and N=0. On N≠0 its b fibre is A^1 minus b=-M/N; on N=0 one has sigma=0 and B=M=rho, and the whole b line survives when M≠0. Neither fibre description imposes a terminal E row.

## 3. Exact t=3 decoupled boundary control

The driver `boundary_structure_t3.sing` imports the lane-owned `controls_t3_raw.sing`, whose declared coefficient field is Q(d), 3d^2=4. The map on c1,c2,b is the identity. It constructs M,N,rho,sigma by setting b=0 and differentiating with respect to b, then maps these polynomials to Q(d)[c1,c2,b,s] with degree-reverse-lexicographic order. It computes standard bases over that exact field, without finite-field promotion.

The foreground command was

    timeout 120 stdbuf -oL Singular -q box/k16xempty-20260905/boundary_structure_t3.sing > box/k16xempty-20260905/boundary_structure_t3.log 2>&1

It completed normally, in under one second. The complete log records

    DECOUPLED_BOUNDARY_DIM=1
    DECOUPLED_BOUNDARY_UNIT=0
    DECOUPLED_B0_DIM=0
    DECOUPLED_B0_VDIM=4
    DECOUPLED_B0_UNIT=0
    H_UNIVARIATE_DEG=4
    H_PRIMITIVE_GCD=1
    H_SQUAREFREE_GCD=1

Here the decoupled boundary ideal is (Delta,A,1-sB), and the second ideal also imposes b=0. No E_k is included in these controls. Thus even the b=0 decoupled boundary is a nonempty scheme of length four. The actual terminal equations are essential.

There is a compact algebraic description of its four geometric points. Set c1=a and c2=a^2 z. Weighted homogeneity gives

    M=a^7 m(z),  N=a^3 n(z),
    rho=a^6 r(z),  sigma=a^2 sigma_0(z),
    H=a^9 h(z),  h=n r-m sigma_0.

The exact factorization shows h has degree four, h is squarefree, and gcd(h,m n r sigma_0)=1. For any root z of h over an algebraic closure, put

    a=sigma_0(z)/n(z),   c1=a,  c2=a^2 z,  b=0,
    s=1/(a^7 m(z)).

All denominators are nonzero by the gcd calculation. Then Delta=0, A=0, B=eta≠0, and 1-sB=0. This is a concrete algebraic family construction of the decoupled control, not a terminal counterexample. The exact coefficients and the gcd computations are contained in the driver/log and imported raw model.

## 4. Why second descent has no licensed map yet

The frozen 8point1 report gives the exact Jacobian of the reconstructed pair in the (h,x) chart:

    J_(h,x)(Q,P)=tau+c b1 x+c b2 x^2+c b3 x^3-c(h-b4)x^4,
    c=-yg,  tau=-(gy/3)B eta.

On X, tau is invertible, but the displayed Jacobian is a nonconstant polynomial in h,x. The coefficient of h x^4 is -c, a scalar unit, for every t and both factors. Therefore any proposed second move requiring a constant-Jacobian source fails that hypothesis literally in this chart. The fact that the Jacobian restricts to the unit tau at x=0 does not make it constant on the whole plane.

The same frozen report gives

    J_(gamma,pi)(Q,P)=-c(pi-gamma)+tau pi,

in the other marked chart. An invertible linear change can normalize its nonzero linear form, but this still produces a monomial-Jacobian object, not a Keller object. The charged ideation section 4 correctly requires a new coefficient-ring map from a target receiver to a source witness chart, source-chart coverage, retention of markings and every support condition, and a well-founded degree decrease. None of those requirements is supplied by the scalar equation Delta=A=0.

Accordingly this lane has not constructed a second descent. The exact failed hypothesis of the naive reuse is constant Jacobian. A broader marked monomial-Jacobian descent theorem could remove that obstacle, but it must be proved together with its support and degree laws; it cannot be inferred from the existing first descent.

## 5. Typed status

PROVED: the homogeneous H interpretation, the exact gluing exponent, the nondegeneracy calculation on the complementary normalization locus, and the exact t=3 nonunit decoupled boundary controls.

OPEN: for every t>=3 and every field factor, T belongs to radical(J+(H)). The independent main requirement is T H in radical(J). The boundary observation does not close either statement for arbitrary t.

No charged input, ledger, jc2-lean file, or unrelated ideation file was edited. No CAS job remains running from this subtask.
