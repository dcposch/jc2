# Golden H-divisible correction: two-sheet separated source exclusion

September8, coordinator/root Astra. PRODUCER-CHECKED, UNREVIEWED field-source
proof. This report treats the separated complement for two explicit strata.
Neither the pending simple-L nor coalesced-M exclusion is a premise. It does
not itself exclude the entire golden source, other clients or JC2.

## 1. Statement, accepted source and exact field

Let K have characteristic zero and contain either root rho of
rho²-3rho+1=0. Set t=1-rho, L=p+g, M=p+tg, H=p²LM². The literal source is

    deg A=15, deg B=25, A_15=H³, B_25=H⁵,
    w(g)=5, w(p)=-7, w(A)<=3, w(B)<=5,
    [A,B]_(g,p)=c*g², c in K*.

Use the accepted canonical homogeneous dilation and A-only references:

    [A_s,B_s]=c*s^36*g²,
    R_s=H+sum_(a=1)^5 s^a R_(5-a),
    A_s=R_s³+alpha*s^10 R_s+a0*s^15+F,
    j=ord_s F, F_j=H C !=0.

The accepted H-divisible alternative gives 1<=j<=9, C homogeneous of
degree10-j, w(C)<=2, deg_g C<=2. The source B reference, retaining every
scalar kernel, is

    B_s=R_s⁵+sum_(i=0)^4 b_i*s^(25-5i)R_s^i+q_s(R_s)F+G,
    q_s(R)=(5/3)R²+(4/3)b4*s^5 R+(b3-5alpha/9)*s^10,
    ord_s G>=2j.

No scalar, normal G block or constant is deleted. All statements here are
over a field, not a quotient by M² or any coefficient scheme.

The exact accepted Morse chart at g0=-p/t is

    R_s(g(s,zeta,p),p)=xi_s+zeta²,
    g=g_c(s,p)+w_s(zeta),
    g in E[[s,zeta]], E=Kbar(p^(1/2)),
    g(0,0,p)=g0, g_zeta(0,0,p)=1/(a*p^(3/2)), a²=t(t-1).

It follows from H(g0+w,p)=t(t-1)p³w²+rho*p²w³ and the formal implicit
and inverse-function constructions. Every inverse coefficient has
nonnegative s-order; p poles are allowed. The units t,t-1,a work for
both rho embeddings. The p derivation extends to E. Combined degrees are
deg s=deg p=1, deg zeta=5/2, deg xi=5.

Write the *actual entire transformed F*, not merely P0, as

    F(g(s,zeta,p),p)=sum_(n>=0) c_n(s,p) zeta^n.

Every c_n has order at least j. The assertion is the following, with
ord(0)=infinity:

| Explicit stratum | d | r |
|---|---:|---|
| C(g0,p)!=0 | 2 | min_(0<=n<=2) ord(c_n)/(6-n) |
| LM divides C, C!=0 | 3 | min_(0<=n<=3) ord(c_n)/(6-n) |

In either stratum the additional condition **kappa=ord xi < 2r** is
impossible. It implies finite positive kappa. This is a separated-source
exclusion conditional on the displayed inequality, not an assertion that
the inequality always holds. If L|C is separately established, these two
strata exhaust C, but that establishment is NOT used here.

Inputs: whole accepted framework
`xmodel/golden-two-regime-initial-discriminator-astra-20260908.md`,
SHA14c4cdeddf9b1166046759022378775fc7ebc147c7d939579cf93f6b78aa51c6;
whole frozen accepted poststate
`box/ideation-20260908T2220Z-poststate/snapshots/audit-15m-only.md`,
SHAb02ae267bb8cfef6956d6e0cec0b6188196b222d3d9d78e3d1582f4a5cc1a440.
The source's original unreviewed header is historical;15m owns its
accepted scope. Root derived this argument before reading the newly sealed
coalesced report; subsequently reading it supplied no additional premise.

## 2. Actual leading coefficient and the separated inequalities

At order s^j the exact F substitution is

    zeta² C(g0+w_0(zeta),p).

In the first stratum c2 has order exactly j, c0,c1 have orders greater
than j. In the second, normality and homogeneity force
C=lambda*p^(8-j)*LM, lambda!=0. Its weight is 7j-46<=2, hence j<=6.
Its M zero is simple: C_g(g0,p)=lambda*(t-1)*p^(9-j)!=0.
Consequently c3 has order j, with coefficient
lambda*(t-1)*p^(15/2-j)/a, and c0,c1,c2 have orders greater than j.
Thus r is finite, positive and bounded respectively by j/4 or j/3.

For EVERY n we have

    ord(c_n)+n*kappa/2 > 3*kappa.                 (1)

For n<=d, ord(c_n)>=(6-n)r>(6-n)kappa/2.
For n>d, ord(c_n)>=j and j>=(6-d)r>(6-d)kappa/2,
so j+n*kappa/2>3*kappa. Infinite orders satisfy the same assertion.
In particular kappa<j/2 in the first stratum, and kappa<2j/3 in the
second. These strict bounds are actual consequences of the separated
hypothesis; they are not guessed from a static jet.

## 3. Exact even/odd regrouping before selecting the balance

Put z=R_s, so zeta²=z-xi_s. Define

    U(z)=sum_(m>=0) c_(2m)*(z-xi_s)^m,
    V(z)=sum_(m>=0) c_(2m+1)*(z-xi_s)^m.

Write U(z)=sum U_l z^l and V(z)=sum V_l z^l. These are legitimate
series in E[[s,z]]: because kappa>0, each coefficient sum converges
s-adically, and all U_l,V_l have order at least j. Precisely,

    U_l=sum_(m>=l) binom(m,l)c_(2m)*(-xi_s)^(m-l),
    V_l=sum_(m>=l) binom(m,l)c_(2m+1)*(-xi_s)^(m-l).

The uniform bound on c_n makes only finitely many m relevant below any
finite s-order. From (1), term by term and then after summation,

    ord U_l+l*kappa>3*kappa,
    ord V_l+kappa/2+l*kappa>3*kappa.             (2)

Strictness is preserved: the orders lie in a discrete group and tend to
infinity with m. Cancellation only raises them.

Moreover ord U1=j in the first stratum: its m=1 term is c2, whereas
every m>=2 term has order at least j+kappa. Likewise ord V1=j in the
second stratum, from c3 and the same estimate. This is the nonvanishing
source attachment that a two-point static value alone does not supply.

Choose a_s²=-xi_s. After a finite s-Puiseux extension it has order
kappa/2 and coefficients in E: the leading xi coefficient is homogeneous
in p of degree5-kappa, so its square root is in E. The two *distinct*
field branches are

    zeta_±(z)=±a_s*sqrt(1-z/xi_s),
    F_±(z)=U(z)±a_s*sqrt(1-z/xi_s)*V(z).         (3)

Define actual scalar orders

    q0=min(ord U0, kappa/2+ord V0),
    q1=min(ord U1, kappa/2+ord V1),
    eta=min(q0/3,q1/2).

Equation (2) gives q0>3kappa and q1>2kappa, hence eta>kappa.
q1 is finite by the preceding source coefficient. In the first stratum
eta<=j/2<=9/2; in the second
eta<=j/2+kappa/4<2j/3<=4. In particular eta<j and eta<5.
Infinite q0 is harmless. Clear denominators with a finite Puiseux extension.

## 4. All implicit terms and the depressed cubic on both branches

Substitute z=s^eta Z in (3). Because eta>kappa, the binomial series
sqrt(1-z/xi_s) is well-defined s-adically; its b-th positive term adds
order b*(eta-kappa)>0 relative to the corresponding a_s V_l z^l term.
For every l>=2 the analytic U_l z^l and a_s V_l z^l have orders at least
j+l*eta and j+kappa/2+l*eta, respectively, both strictly greater than
3eta since eta<j. These uniform bounds control all infinite Taylor terms,
not merely a finite sample of derivatives.

For l=0 the two base orders are at least q0>=3eta. For l=1 they are
at least q1+eta>=3eta. Thus all positive binomial corrections are also
strictly later than3eta. At least one of the l=0 or l=1 base terms
attains3eta, by the definition of eta. On the two branches its coefficient
tuple is of the form (a+b,a-b). In characteristic zero this tuple cannot
vanish unless a=b=0. Different Z-degrees cannot cancel. Therefore the
actual F initials are u_± Z+v_± with

    (u_+,v_+,u_-,v_-) != (0,0,0,0).

One entire branch correction MAY be zero; the argument retains both.
The references alpha*s^10*z and a0*s^15 are later because eta<5.
The full A initials on the two fields are

    P_±=Z³+u_± Z+v_±, at order3eta.             (4)

They are monic and depressed on both branches. Since the original A has
combined degree15, z has degree5, and Z has degree h=5-eta>0, each obeys

    (p*d_p+h*Z*d_Z)P_±=3h P_±.

The formal square-root branches respect the same grading; the coefficient
field permits the necessary fractional p powers and p derivation. No
identification of the two signs or nilpotent Euler calculation occurs.

## 5. Earlier B terms: global earliest G and the degree bound

Every scalar B kernel is later than5eta, by
(5-i)*(5-eta)>0 for i<5. In q_s(z)F only (5/3)z²F can enter5eta;
the other terms are later by5-eta or10-2eta. Thus any B term earlier
than5eta must be a G term. It is not legitimate simply to assert
ord G>=5eta: the accepted bound2j need not imply it.

Transform the ENTIRE G to the Morse coordinate. Each zeta coefficient
has order at least2j, since every inverse coefficient has nonnegative
s-order. Perform exactly the even/odd regrouping of Section3:

    G_±(z)=U_G(z)±a_s*sqrt(1-z/xi_s)*V_G(z),
    ord [z^l]U_G>=2j, ord [z^l]V_G>=2j.         (5)

The regrouping again converges because kappa>0. Let nu be the GLOBAL
earliest order of G on the pair after z=s^eta Z, if G is nonzero. It
equals the minimum of the analytic base-term orders

    ord [z^l]U_G+l*eta,
    kappa/2+ord [z^l]V_G+l*eta.                 (6)

Proof: positive binomial corrections are strictly later than their own
base terms. At the minimum, different l have different Z-degrees, and
for each l the tuple (a+b,a-b) cannot vanish on both fields. Finite
contribution at any order follows from the uniform bounds2j+l*eta.
This proof of (6) also applies if one branch has later order or is zero.

Suppose nu<5eta. Every degree l contributing to this global initial has

    2j+l*eta<=nu<5eta.

In the first stratum eta<=j/2, so l<1, hence the G initials are constants.
In the second eta<2j/3, so l<2, hence degree at most1. At least one field
has a nonzero initial Q of degree n within those bounds. On that field
it is also the initial of B, since all other B terms are at least5eta.
Its Euler degree is 25-nu.

The exact transformed source bracket in z,p is

    c*s^36*g_±(z,p)²*g_zeta(s,zeta_±,p)/(2*zeta_±).

Its order is exactly36-kappa/2, with nonzero leading coefficient on
EACH field. Here g0!=0, g_zeta(0,0,p)!=0 and a_s has order kappa/2.
The relevant initial bracket [P_±,Q] occurs at order2eta+nu. We have

    7eta+kappa/2 <= 15j/4 <=135/4 <36       (first stratum),
    7eta+kappa/2 <= 7j/2+9kappa/4 <5j<=30<36 (second stratum).

The first bound uses eta<=j/2 and kappa<j/2; the displayed weak bound
suffices. Thus 2eta+nu<7eta<36-kappa/2 and [P_±,Q]=0.

For monic cubic P and Q of degree n with leading coefficient q_n, the
coefficient of Z^(n+2) in [P,Q] is 3q_n'. Hence q_n'=0. Q's Euler
homogeneity also gives

    p*q_n'=(25-nu-nh)q_n.

This coefficient is nonzero: in the first stratum n=0 and
25-nu>25-5eta>0; in the second n<=1 and
25-nu-nh>=20-nu+eta>20-4eta>0. This includes constants. It contradicts
q_n!=0. P's Euler homogeneity is not needed for this leading-coefficient
step. Consequently NO earlier G/B initial exists on either branch.

## 6. Monic quintics, strict target gap and contradiction

The absence of earlier G terms forces all the analytic base orders (6)
to be at least5eta; otherwise their global earliest initial would have
survived. Hence at5eta positive binomial corrections still cannot enter.
The degree bound is now 2j+l*eta<=5eta. In the first stratum this gives
l<=1. In the second the strict eta<2j/3 also gives l<=1. Thus G MAY
contribute a linear term and a constant at5eta, and both are retained.

On each branch the complete B initial is consequently a monic quintic

    Q_±=Z⁵+(5/3)Z²(u_± Z+v_±)+ell_± Z+e_±,
    ord B_±=5eta,
    (p*d_p+h*Z*d_Z)Q_±=5h Q_±.                 (7)

There is no competing quintic leader from G, scalar kernels or implicit
corrections. Equations (4),(7) and the strict target-order gap give
[P_±,Q_±]=0 separately on the two field factors. Euler elimination gives

    p[P,Q]=h*(5P_Z Q-3P Q_Z)=0.

So Q³/P⁵ is Z-constant, and monicity makes it1. UFD in E[Z] implies
P=W³, Q=W⁵ for a monic linear W. The depressed cubic has zero Z²
coefficient, forcing W=Z and hence u_±=v_±=0 on BOTH fields. This
contradicts the nonzero correction tuple in Section4. The asserted
separated alternative is excluded in the two exact source strata.

## 7. Attacks, scope and evidence

The one-sheet shortcut fails already for coefficient tuples: taking
a=b!=0 gives (a+b,a-b)=(2a,0). Our proof permits this cancellation and
uses the global pair minimum. It never claims every individual constant
or linear coefficient is nonzero. The same argument is used anew for G;
one cannot transfer a chosen A sheet's minimum to G without it.

The strict eta>kappa is essential: at eta=kappa the binomial powers do
not acquire increasing s-order. The separated hypothesis and (1),(2)
establish the needed strictness rather than assuming denominators safe.
The degree bound for the first G initial uses its actual order2j and the
global minimum; applying the coalesced positive-order lemma directly
through the split square-root substitution would be unjustified.

The assertions are pure formal-field source implications. No computer
algebra, actual H/R high power, full A15/B25 pair, degree6/10 pair,
source row stream, numerical sample or computational theorem check was
executed. The displayed sign and boundary controls attack proof shortcuts,
not the existence of a full source. No computational mutation claim is
made. Evidence is the complete proof and frozen accepted input hashes.

Both rho roots, both square-root choices and infinite coefficient orders
are covered. The separated hypothesis itself excludes xi=0, which belongs
to the complementary coalesced regime; no finite kappa is inferred there.
The LM stratum is explicit; M|C with L∤C is outside this statement.
No pending simple-L/coalesced theorem, no source reverse lift, scheme
unit ideal, properness, all-degree coverage or JC2 resolution is asserted.
Independent different-model review is required before promotion.

No new OPEN identifier is raised. Local publication and input-pin checks
are the only executed procedures; root retains the separate live gate and
typing tasks without reading their mutable artifacts. The report is ready
for hostile review, not publication as a resolution claim.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

The existing extractor was called on this private body before sealing;
no corpus scan or peer artifact access was needed. Both named source pins
matched again before completion. All mathematical sections are complete.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13987`.
- Body SHA-256:
  `4c8576a75051400099e2be5ba1226e3df81a4a1c455b5253cb10f30f5e928b48`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
