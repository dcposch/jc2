# Independent audit: odd golden first contact j=12 attaches to the eight-parameter ansatz

September8 2026. **CONFIRMED at the conditional FIELD-valued source-interface scope below.** This is an independent audit of Fable's frozen blind/cross claim, not a proof that an arbitrary golden source has j=12. The separate seven-row ansatz exclusion remains ROOT-CHECKED PROVISIONAL and is NOT a premise of this attachment theorem. No nonodd or whole-golden exclusion is asserted.

## Literal theorem and normalization

Let K be any characteristic-zero field containing rho with rho²−3rho+1=0. Define t=1−rho, L=p+g, M=p+t g, H=p²LM² and D=pLM. Both conjugates are retained; rho,t,t−1 are nonzero. Suppose A,B in K[g,p] are ODD, of degrees15,25 with tops H³,H⁵, weights<=3,5 for w(g)=5,w(p)=−7, and [A,B]=c g²,c!=0. No inverse-lift equations or other source pins are used.

Put A_s=sum s^(15-d)A_d and B_s=sum s^(25-d)B_d. Then [A_s,B_s]=c s^36 g². The A-only normalizations below define R_s=H+s²R3+s⁴R1 and alpha_s=alpha s^10. Set F=A_s−R_s³−alpha_s R_s. **Additional stratum hypothesis: ord_s F=12.** Under this hypothesis there exist u,v,w,lambda,tau,alpha,beta,gamma in K, lambda!=0, such that at s=1

    R=H+u gp²+v p³+w p, F=lambda D+tau p, mu=5lambda²/9,
    A=R³+alpha R+F,
    B=R⁵+beta R³+gamma R+(5R²/3+beta−5alpha/9)F+mu L.       (1)

This is exactly the shared eight-parameter family, not just matching dimensions or support. All parameters remain in K; no additional root extraction or parameter localization is used. The argument is field-valued, not an arbitrary nilpotent-base classification. Conditional composition with a separately accepted exclusion of (1) would remove j=12 only.

## 1. Centralizer: check rather than transport by analogy

Let h=H and K0=K(h). On the generic fiber put u=g/p and z=1/p. Then

    z^5=(1+u)(1+t u)^2/h.                         (2)

Over an algebraic closure of K0, the right side has valuation ONE at u=−1: the other linear factor does not vanish there. The polynomial Z^5−(1+u)(1+t u)^2/h is Eisenstein in that discrete valuation ring. Thus the generic fiber is geometrically integral. Repeated M in the special fiber does not invalidate this simple-L argument. This also supplies an alternative to Fable's correctly directed cubic Newton-slope argument in g/p.

Consequently K0 is algebraically closed in K(g,p). To spell out the derivation step, [H,u]=−5H/p² is nonzero; normalize the Hamiltonian derivation to send u to1 and fix K0. The full function field is finite algebraic over K0(u). A Hamiltonian constant's minimal polynomial over K0(u), after differentiation, has a polynomial of smaller degree annihilating that constant; hence every coefficient is constant for d/du and belongs to K0. The constant is algebraic over K0, therefore in K0. Rational centralizer=K(H).

If a(H)/b(H) with coprime a,b is a polynomial in g,p, Bézout makes b(H) a polynomial unit; hence b is constant. The polynomial centralizer is K[H]. A homogeneous centralizer of degree d is a scalar H^(d/5) when5 divides d, and zero otherwise. These arguments apply over the original K and both embeddings. No special-fiber irreducibility or reducedness is assumed.

## 2. Exact A-only reference and exceptional alpha

Divide by3H² with lex order g>p; leading coefficient3rho² and leading monomial g⁶p⁴ are units/fixed. Replacement lowers g-degree, preserves total degree and does not increase w, because H's leading weight is1 and every other monomial has smaller weight. Define R3 and R1 through

    A13=3H²R3+N13,
    A11−3H R3²=3H²R1+N11,                       (3)

with normal remainders. The quotient bounds give degree3/1 and weight<=1: exactly R3=u gp²+v p³ and R1=w p. Choose alpha so A5−3R3 R1²−alpha H is normal for g³p²; its scalar quotient divides by rho only. In particular alpha may be ZERO: ord(alpha_s)>=10, not necessarily equal10.

These definitions make F2,F4 normal for H² and F10 normal for H. All F_l have degree15−l, weight<=3 and even l; there are no coefficients beyond l=14. No claim that F6 or F8 vanishes follows from (3); their vanishing here is part of ord F=12. Also F cannot vanish identically under c!=0, since then the degree10 polynomial3R_s²+alpha_s would divide the degree2 Jacobian target over K((s))[g,p].

## 3. Retain every B kernel and its later terms

Initially set beta=gamma=0, and always define

    beta_s=beta s^10, gamma_s=gamma s^20,
    q_s=5R_s²/3+beta_s−5alpha_s/9,
    delta_s=gamma_s−beta_s alpha_s+5alpha_s²/9,
    G=B_s−R_s⁵−beta_s R_s³−gamma_s R_s−q_s F.

Direct differentiation gives the exact identity

    [A_s,B_s]=[R_s,(3R_s²+alpha_s)G−delta_s F−(5/3)R_s F²]+[F,G]. (4)

Its dR∧dF coefficient is −delta_s−(10/3)R_s F; the other two coefficients are3R_s²+alpha_s and1. This retains the alpha cross term and all scalar references.

If l<24 is the first nonzero G coefficient, (4) implies [H,3H²G_l]=0. Indeed RF² starts at24, delta F at>=32, [F,G] at12+l, and the target at36; earlier G coefficients vanish. Oddness and total combined degree25 leave only l=10, G_l=eta H³, or l=20, G_l=theta H. Remove them with the exact whole updates

    Delta_beta G=−eta s^10(R_s³+F), Delta_beta delta_s=−eta alpha s^20,
    Delta_gamma G=−theta s^20 R_s, Delta_gamma delta_s=theta s^20.    (5)

Later coefficients in these formulas are NOT suppressed. Each update removes the designated leading kernel and changes no earlier coefficient. Continuing through l=22 proves ord G>=24. There are no hidden negative-H kernels: G is polynomial. beta,gamma,delta may vanish, and no division by them occurs. All coefficients of G have odd positive degree25−l, so G=s^24 G1, where G1 is a weight<=5 linear polynomial.

## 4. Order24 and evaluation at1

At order24, the target and [F,G] have not yet appeared. Equation(4) gives

    [H,3H²G1−(5/3)H F12²]=0.

The expression inside has degree11, so the centralizer lemma makes it ZERO. Hence H divides F12². The distinct linear factors of H have multiplicities(2,1,2), so unique factorization gives D divides F12. Since F12 is nonzero of degree3, it equals lambda D with lambda!=0. Since D²=HL,

    G1=(5/9)lambda²L.

The only degree1 weight<=3 term is tau p, giving F=s^12 lambda D+s^14 tau p. Evaluating the exact identities at s=1 proves (1). The unequal inner coefficient a=lambda*t and the resulting d=5lambda²/9 are nonzero; comparison with the monomial target forces c=−(5/9)lambda³t. This is not an independent c=1 normalization. No physical polynomiality row has been inferred from this receiver statement.

## Verdicts and corrections

CONFIRMED: the conditional odd-j12 attachment, the complete beta/gamma removal, and the formula for G1. Fable's phrase “verbatim” was insufficient as a proof; sections1–4 supply the actual golden derivation. The parity restriction is essential to this reference/kernel list and is not licensed merely because one golden factor control is odd. The source theorem does NOT select j=12 or exclude any j<=10. No j10 scalar exception is used here: at order24 degree11 is not a multiple of5. The only earlier scalar exceptions are l10/l20 and both are retained explicitly. alpha=0, beta=0, gamma=0, delta=0 and zero R3/R1 are all allowed; lambda=0 is excluded solely by the stratum hypothesis. Characteristic0 is essential. No nonodd or arbitrary coefficient-ring attachment is claimed.

Fable's eight-variable evaluation-versus-decision error and receiver-versus-physical-lift wording remain corrected by the terminal cross. The separately root-checked ansatz contradiction is not re-audited or promoted here. Once independently accepted, it may be composed with this FIELD-valued attachment, not with an unstated whole-golden coverage claim.

## Evidence and custody

Whole frozen Fable blind/cross bodies were read after their exact collected hashes were checked. Whole accepted minimal-receiver and golden-factor controls, and the exact source-normalization proof used as comparison, were read; no accepted code farm or live/unreleased review was read. Tiny owned controls check the free differential coefficients, actual extra parity-breaking kernel, and changed order24 scalar, normal/−O, without actual H/R high powers. The universal proof above is not inferred from scalar samples. Inputs, replay and transaction are pinned in owned custody. No AWS, CAS, model launch, shared/protected edit or source expansion. This audit is terminal independently of the separate PREP-only task. All writers idle at handoff.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8621`.
- Body SHA-256:
  `b459d73faf74c86579ad3b3ce9494867c7cb9e7ff028dd4ff56db07fae011c1d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
