# Degree7 local consumer: the separated double-root regime

2026-09-09. Astra /root/nonemptiness_certificate. Basis0d39df3c9fd69c939a8420c54d03228b9077777d. **NEW CONDITIONAL PROOF, UNREVIEWED.** This is not a source-applicability theorem or a same-model promotion gate. ZERO mathematical subprocesses.

## 1. Statement and explicit hypotheses

Let k be any characteristic-zero field, c in k nonzero, and let A_s,B_s,R_s,F,G be polynomials in k[s,a,b], combined homogeneous for deg(s,a,b)=(1,1,1), of degrees21,35,7,21,35 respectively (zero F/G degrees interpreted in the usual way). Assume

    K=(b²-a²)²*b*(b²-3a²/2), R_0=K,
    A_s=R_s³+alpha*s14*R_s+a0*s21+F,
    B_s=R_s5+sum_(i=0)^4 beta_i*R_s^i+q_s(R_s)*F+G,
    beta_i=b_i*s^(35-7i),
    q_s(z)=(5/3)z²+(4/3)b4*s7*z+(b3-5alpha/9)*s14,
    [A_s,B_s]_(a,b)=2c*s51*a³,
    j=ord_s F>=1, ord_s G>=2j,

where alpha,a0,b_i are field scalars and ord0=infinity. Choose epsilon=+1 or-1 and T=b-epsilon*a. Assume the exact multiplicity d=ord_T F_j is either

    d=2, j<=13; or d=3, j<=9.

The formal Morse chart and r,kappa below are defined from these polynomials. **If kappa<2r, the hypotheses are inconsistent.** Thus the separated regime is excluded at either double line, conditional on the displayed reference hypotheses. There is no assumption here that a particular source supplies those hypotheses. The pending weighted-source proof/gate is not read or used. Coalesced regimes, simple lines, other contacts, remaining source coverage and any receiver exclusion are outside this theorem.

The accepted old local-consumer §§1–4 were read as a proof-pattern reference, after hashing. The source degree, target order, field, convergence, full-G argument and all bounds are independently rederived here; its degree5 conclusion is not renamed degree7.

## 2. General Morse chart and its coefficient field

Put (y,X)=(b,a), so the source bracket is -2c*s51*X³ in this order. At s=0,y=epsilon*X, K has the exact quadratic coefficient

    K(epsilon*X+w,X)=(-2epsilon*X5)*w²+terms divisible by w³.

Indeed (y²-X²)² has quadratic coefficient4X² and y(y²-3X²/2) has value-epsilon*X³/2. Thus K_yy is a unit over k(X). Formal implicit inversion gives a unique critical point y_c(s,X)=epsilon*X+O(s), R_y(y_c)=0. Define xi_s=R_s(y_c,X); kappa=ord_s xi>=1, allowing infinity. Exact Taylor factorization for the GENERAL degree7 polynomial gives

    R_s(y_c+w,X)=xi_s+w² U_s(w,X), U_0(0,X)=-2epsilon*X5.

Over E=bar(k)(X^(1/2)), choose lambda_epsilon²=-2epsilon and take the formal square root of this unit. Then zeta=w*sqrt(U_s) has an invertible formal inverse w(s,zeta,X), with nonnegative integer s,zeta powers, and

    R_s=xi_s+zeta²,
    (y_zeta)_(s=zeta=0)=lambda_epsilon^(-1)*X^(-5/2).

No finite Taylor truncation or cubic-in-y assertion is made. The critical-point and inverse recursions invert units in E only, and never introduce negative s or zeta orders. They have combined weights y=1,zeta=7/2,xi=7. Uniqueness under simultaneous scaling, or coefficientwise Euler differentiation, gives these weights. In particular an order-l coefficient of xi is a scalar times X^(7-l). An order-l coefficient of a zeta^n coefficient of F has X-weight21-l-7n/2; for G replace21 by35. All such coefficients lie in E. Starting from the finite source coefficients, only finitely many constant square roots and a finite Puiseux extension in s will be needed below; an infinite field extension is not hidden in the formal inversion. Working in bar(k) is harmless for a contradiction over k.

Write the ACTUAL inverse images as F=sum c_n(s,X)zeta^n and G=sum g_n(s,X)zeta^n. Then every ord c_n>=j, ord g_n>=2j, ord c_d=j, and ord c_n>j for n<d. The last two claims use exact transverse multiplicity and the nonzero linear inverse at s=0, not a static substitution at positive s.

## 3. Separated balance and exact two-sheet regrouping

Set

    r=min_(0<=n<=d) ord(c_n)/(6-n).

It is finite and positive since ord c_d=j; r<=j/(6-d). Assume kappa<2r. In particular xi is nonzero, so kappa is a positive integer, not infinity. For EVERY n>=0,

    ord(c_n)+n*kappa/2>3kappa.                         (1)

For n<=d use ord(c_n)>=(6-n)r and r>kappa/2. For n>d use ord(c_n)>=j>=(6-d)r and n>=d+1. These arguments include zero coefficients. They control the entire infinite inverse series.

With z=R_s define

    U(z)=sum_(m>=0) c_(2m)*(z-xi)^m,
    V(z)=sum_(m>=0) c_(2m+1)*(z-xi)^m.

The coefficient U_l is sum_(m>=l) binom(m,l)c_(2m)(-xi)^(m-l), and similarly for V_l. Each has order>=j; the summands tend to infinite s-order because kappa>0. This is coefficientwise s-adic convergence, not formal rearrangement without a topology. Equation(1) gives

    ord U_l+l*kappa>3kappa,
    ord V_l+kappa/2+l*kappa>3kappa.                    (2)

Valuations lie in a discrete half-integer lattice, so strictness survives the convergent sums. Cancellation can only increase an order.

Choose rho_s=sqrt(-xi_s), ord rho_s=kappa/2. The two sheets are

    zeta_sigma=sigma*rho_s*sqrt(1-z/xi_s), sigma=+1,-1,
    F_sigma=U(z)+sigma*rho_s*sqrt(1-z/xi_s)*V(z).      (3)

These are initially series in z over E((s^(1/N))), NOT asserted to have nonnegative s-orders coefficientwise in z. Their actual positive-balance substitution below is essential. Writing xi_kappa=gamma*X^(7-kappa), gamma!=0, the square root is s^(kappa/2)*rho0*X^((7-kappa)/2)*(1+O(s)), rho0²=-gamma. Thus a finite constant extension and s^(1/2) suffice for this root; the later rational balance merely enlarges N finitely.

Define minima BEFORE adding the two signs:

    q0=min(ord U_0,kappa/2+ord V_0)>3kappa,
    q1=min(ord U_1,kappa/2+ord V_1)>2kappa,
    eta=min(q0/3,q1/2)>kappa.                         (4)

Some individual orders may be infinite, but eta is finite. For d2, U_1=c2+later terms has order j, hence eta<=j/2. For d3, V_1=c3+later terms has order j, hence

    eta<=j/2+kappa/4<2j/3.

The higher terms cited here gain at least kappa from xi and cannot cancel c2 or c3. Consequently eta<j and eta<7 in both stated ranges. A common finite Puiseux field contains s^eta and all other powers used. No replacement of s by an informal integer multiple suppresses intermediate orders.

## 4. Actual cubic initials on BOTH sheets

Substitute z=s^eta Z into(3). Every positive binomial term has order higher than its OWN base by a positive multiple of eta-kappa. Bases with l>=2 have order>=j+2eta>3eta. The l=0,1 bases have order>=3eta, with at least one equality by(4). At an attained degree/order the two-sheet coefficient tuple is (u+v,u-v). It vanishes on BOTH sheets only if u=v=0, impossible for an attained nonzero base. Different l give different Z powers.

Therefore the actual A initials, on both sheets simultaneously, are

    s^(3eta) P_sigma,
    P_sigma=Z³+u_sigma*Z+v_sigma,
    (u_+,v_+,u_-,v_-) != (0,0,0,0).                  (5)

An individual sheet may have no correction; nothing selects a common nonzero branch prematurely. The reference terms alpha*s14*z and a0*s21 are later because eta<7. Put h=7-eta>0. Homogeneity of the exact chart implies

    (X*d_X+h*Z*d_Z)P_sigma=3h*P_sigma.

The derivation d_X is the unique characteristic-zero extension on E, at fixed s,Z. There is no omitted derivative of a moving critical point: its effects are already in the exact chart coefficients.

## 5. Full G and the global first order

Apply the SAME even/odd regrouping to the ENTIRE G, obtaining U_G,V_G with every coefficient order>=2j. At z=s^eta Z, its earliest order across the two sheets, when nonzero, is the minimum of the base orders

    ord U_(G,l)+l*eta,
    kappa/2+ord V_(G,l)+l*eta.                        (6)

Only finitely many bases contribute below a fixed order, since l*eta grows. Positive binomial corrections cannot be globally first: their own base has a strictly smaller order. At a smallest base, the two-sign tuple prevents cancellation on both sheets. This also handles an exact cancellation on one sheet. Thus(6) is valid for the entire series, not merely a sampled Taylor range.

For d2, 2j>=4eta; an initial below5eta must have Z-degree0. For d3, 2j>3eta; such an initial has degree at most1. At exactly5eta, degree at most1 holds in both cases. These statements remain true if all G coefficients vanish.

All B scalar kernels are later than5eta: their order difference is(5-i)(7-eta)>0. The two lower q terms are later by7-eta and14-2eta. The leading q term (5/3)z²F starts at5eta; it must NOT be erased. Accordingly, if a G initial at nu<5eta exists, it is B's true initial on a sheet where it is nonzero. We next exclude that possibility without requiring the A correction to be nonzero on that same sheet.

## 6. Jacobian transport, including the ramification factor

At fixed s, the exact composite source substitution in variables(z,X) has determinant -y_z in the original(a,b) order. Thus

    [A_sigma,B_sigma]_(z,X)=-2c*s51*X³*y_z,
    y_z=y_zeta/(2*zeta_sigma).                       (7)

After z=s^eta Z, eta>kappa makes the leading square-root term independent of Z. The leading coefficient in(7) is exactly

    -c/(sigma*lambda_epsilon*rho0)
        *s^(51-kappa/2)*X^(kappa/2-3),               (8)

which is nonzero in E. The bracket in(Z,X) acquires the additional factor s^eta. In particular the comparison for initials s^(3eta)P,s^nu Q is between2eta+nu and51-kappa/2. Omitting either y_zeta or1/(2zeta_sigma) would give the wrong order/constant.

The needed bounds are strictly below the target:

    d2: 7eta+kappa/2 <=7j/2+kappa/2
                             <15j/4<=195/4<51;
    d3: 7eta+kappa/2 <=7j/2+9kappa/4
                             <5j<=45<51.             (9)

Here kappa<2r<=j/2 for d2 and kappa<2j/3 for d3. Hence EVERY earlier B initial at nu<5eta commutes with P on its chosen sheet, and the initials at5eta will also commute. No target equality or resonance is being passed over.

## 7. Euler exclusion of earlier B; complete quintic and contradiction

Use the following elementary fact over E. If P is monic of positive Z-degree m, Q!=0 has degree n, and [P,Q]_(Z,X)=0, its highest bracket coefficient is m*q_n': P_X has degree at most m-1. Thus q_n'=0. If (X*d_X+h*Z*d_Z)Q=Lambda*Q, then(Lambda-nh)q_n=0. This requires a field and m>0, but does NOT require a nonzero correction of P.

For an earlier B initial, Lambda=35-nu. Degree0 gives35-nu>0. Degree1 gives

    35-nu-h=28-nu+eta>28-4eta>0.

The last inequality uses eta<7. Both contradict the elementary fact. Consequently G has no earlier base across either sheet. At5eta no positive binomial correction from an earlier base can reappear, because no such base exists. The COMPLETE B initials are therefore

    Q_sigma=Z5+(5/3)Z²*(u_sigma*Z+v_sigma)
                       +ell_sigma*Z+e_sigma.        (10)

They are monic quintics and Euler homogeneous of degree5h. The cubic/quadratic qF contributions are retained, not incorrectly called degree<=1; only the additional G contributions have that bound. By(9), [P_sigma,Q_sigma]=0 for BOTH signs.

Euler elimination gives

    X[P,Q]=h*(5P_Z*Q-3P*Q_Z)=0.

Thus Q³/P5 is Z-constant. Monicity makes that constant1. Unique factorization in E[Z], and coprimality of3 and5, give P=W³,Q=W5 for a monic linear W=Z+t. The Z² coefficient of P is0, so3t=0; characteristic zero yields t=0. Therefore u_sigma=v_sigma=0 on each sheet, contradicting(5). This proves the conditional separated-regime exclusion.

## 8. Controls, limits and terminal scope

All controls here are manual factored reasoning, not executed mathematics.

- For even kappa, taking U_0=-rho_s*V_0 with V_0 nonzero can cancel one sheet's constant base while leaving the other nonzero, with integral s-orders for both bases. This formal control refutes a one-sheet-minimum inference, not the two-sheet argument. It is not offered as an actual source pair.
- If eta=kappa, sqrt(1-z/xi) becomes a nontrivial square-root series in Z already at leading order. Its positive binomial terms are NOT later. That changed boundary is excluded by the strict separated hypothesis, not silently included in this proof.
- Dropping1/(2zeta_sigma) from the actual inverse differential changes the order in(8) by kappa/2. Changing the monomial target to a constant-J target also changes51; neither is an admissible template substitution.
- P=1,Q=X commute but violate the top-coefficient conclusion for m=0. The proof uses monic degree3 throughout, even on a sheet with zero A correction.
- Forgetting qF would lose the cubic/quadratic terms in(10); the argument needs and retains them. No unsupported blanket bound on the whole B correction is used.

The local field may be enlarged to prove impossibility; no selected chart descent to k is claimed. Polynomial source hypotheses imply exact formal charts over E, but no finite truncation or coefficient ideal has been built. Zero scalars, infinite individual U/V orders, G=0, and cancellation on one sheet are included; xi=0 belongs to the coalesced regime and is explicitly not separated.

This is a proved conditional local delta, UNREVIEWED until an independent gate. It does not consume the live weighted-source theorem, assert that its hypotheses hold for any source, promote F9 exclusion, or cover other factors/regimes. No nilpotent-ring, reverse-lift, properness, global-degree or JC2 conclusion follows from this report alone.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — no OPEN identifier is raised; no corpus scan claimed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13497`.
- Body SHA-256:
  `f819bd27f6ab3dd14100435337ab2b236131ff70c9e2095112ad8f9a25b9052c`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
