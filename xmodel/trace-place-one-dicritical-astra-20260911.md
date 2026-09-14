# Trace places on the stipulated one-dicritical stratum

Author: Astra geometry. Manual bounded consumer, not automatic promotion.
First action2026-09-11 23:17:45 UTC; original reserve23:32/HARD23:35 unchanged.
Exactly TASK plus six pinned inputs. All hashes matched before bodies.

## Hostile formula check

Verdict: the finite-stratum formula is CORRECT with complete jump sets and
the axis qualification. Its proposed one-dicritical application is exact,
but its inequality is KNOWN/WEAKER on the currently surviving source scope.
The arbitrary-axis redundancy has the explicit polynomial proof below.

Keep geometric degree N distinct from all coordinate degrees. Let V={pq!=0},
D the actual reduced nonproperness curve, eta_i:Dtilde_i->D_i its finite
normalizations, epsilon(y)=N-#F^-1(y), and e_i its generic value on D_i.
Choose a finite set J in D intersect V containing ALL singular/intersection
points and ALL jumps of epsilon. Define w(y)=sum_(eta_i(t)=y) e_i,
counting normalization branches separately, including branches on one
irreducible component. Away from J, epsilon=w. Euler integration therefore gives

    integral epsilon dchi = sum_i e_i chi(Dtilde_i over V)
                           + sum_(y in J)(epsilon(y)-w(y)).

This proves Fable's correction term, rather than assigning one generic
weight to each singular target point. At the named TRACE/Bass/Mellin and
IC-comparison tiers, rho(R/A)=-integral epsilon dchi and
rho(L_i)=-chi(Dtilde_i over V). If each normalization is A1 and has a
finite set of nu_i axis preimages, subtraction yields

    rho(kerTr)=sum_i(e_i-1)(nu_i-1)+sum_(y in J)(w(y)-epsilon(y)).

A component in an axis has empty torus restriction; its finite nu_i notation
is invalid. Formula proof needs constructibility and normalization, not
Fable's optional semicontinuity signs. For a smooth jump the correction is
e_i-epsilon(y); at a general multibranch point no sign follows merely from
epsilon(y)>=each e_i. Formula errors would not refute Loeser--Sabbah.

Strict positivity requires the actual source and Bass tier: a nonzero
traceless element of the finite extension FracR/FracA, N>1, clears into R
because (FracA)R=FracR. Its injection into Bass-torsion-free R/A survives
Euler localization. Thus rho(kerTr)>=1; no full trace section is assumed.
Changing axes changes Euler operators: apply the named Bass/Mellin premises
in those SAME coordinates, not by transporting a previously computed rank.
Fable's e_i=1 example does not meet this client's already-proved W=2 datum.

## Actual source application and comparison

The stipulated single dicritical has normal index2 and tangential degree1.
Use the accepted source relations W=2, S_dicritical=1,

    epsilon(P)=N-a_P=2r_P+K_P,   K_P>=0,   sum_all_P K_P=N-3.

Let nu=number of DISTINCT normalization points over the UNION of the axes;
this nu is NOT MI's sum(r_P-1). Let K_axis=sum_(P on axes)K_P, counting a
target point once even if it lies on both axes, and K_V=sum_(P in V)K_P.
The sole normalization is A1; at every special point w(P)=2r_P, so each
correction is exactly -K_P. Hence, independently confirming ROOT's proposal,

    rho(kerTr)=nu-1-K_V=nu+2-N+K_axis,
    N<=nu+1+K_axis  <=>  K_V<=nu-2.                 (1)

All contracted-tail charges are already included in K_P. Neither local
support labels nor a claimed globally fixed escaping pair enters this sum.

For two generic affine axes, chosen transverse to D, avoiding its singular
and charge points and with intersection off D, put n_D=deg D. Then
nu=2n_D, K_axis=0. Equation(1) gives N<=2n_D+1. The repaired meridional
floor is n_D(W-S_dicritical)>=N-1, hence n_D>=N-1 here, strictly stronger.
Indeed it already gives rho(kerTr)=2n_D+2-N>=N. MF-EXACT retains its genus
and infinity terms; equality of the S-known floor is not assumed. Special
axes cannot inherit nu=2n_D, K_axis=0, or a generic-line connectivity claim.

Here is the decisive arbitrary-axis comparison. Write the birational
polynomial normalization eta(t)=(a(t),b(t)) in the CHOSEN target coordinates.
Constant-coordinate cases are disposed of first. If one coordinate is
identically zero, D is that axis and its torus restriction is empty; no
finite nu formula applies. If one is a nonzero constant, birationality
forces the other polynomial to have degree1, and D is an affine line.
Both constants cannot parametrize a curve. All these curve cases are smooth
and already excluded in this source scope. Thus on the singular survivor
both are nonconstant. Put m=deg a>0, n=deg b>0 and

    S(t)=product_(a(c)b(c)=0)(t-c),   deg S=nu,
    A(t)=S a'/a,  B(t)=S b'/b,  C(t)=n A(t)-m B(t).

These are polynomials. A and B have leading terms m t^(nu-1),
n t^(nu-1), so deg C<=nu-2 if C!=0. At a normalization point c over V,
S,a,b are units. Therefore ord_c C>=min(ord_c a',ord_c b'). The latter
is the branch multiplicity minus1: expand a-a(c), b-b(c) in the uniformizer
t-c, using characteristic0 and the primitive normalization parameter.

At each singular target point P, the repaired LOC-MULT with W-S_dicritical=1
and its stipulated small-ball orbit/component hypothesis gives
K_P<=mult_P(D)-r_P. Multiplicity is additive over the branches, hence

    K_V <= sum_(c over V) min(ord_c a',ord_c b')
        <= deg C <= nu-2.                         (2)

Smooth branches contribute zero. All branches over a target point are
included, so no branch charge is silently omitted. This proves EXACTLY(1)
from the existing local inequality plus elementary polynomial normalization.
No new trace-specific restriction survives when C is nonzero.

The exceptional C=0 is fully identifiable, not a lost divisor. It says
n a'/a=m b'/b, so a^n/b^m is constant. Factorization yields
a=alpha h^u, b=beta h^v with gcd(u,v)=1 and u,v>0. Birationality gives
C(a,b)=C(h)=C(t); thus the polynomial h has degree1. Consequently nu=1,
and D is a smooth embedded A1 or a one-cusp monomial curve, with no multibranch point.
Conversely nu=1 forces this same form, since both coordinate polynomials
have only that root. Equation(1) forbids it, since K_axis<=N-3 gives rank<=0.

This is NOT a new surviving case: smooth D is already excluded by MI, and
MFS explicitly imports case-(A)'s closure and restricts its surviving scope
to case(B). MI alone only cages the cuspidal case; do not attribute that
closure to MI's Euler calculation. At MFS's stated imported tier, no actual
allowed configuration meets nu=1. If that imported closure were withheld,
the Mellin exclusion of the monomial case would remain conditional at its
own tier, not an all-one-dicritical exclusion. For the retained case(B),
C!=0 and(2) settle redundancy for EVERY permitted affine axis pair,
independently of any extra coordinate-applicability issue for Bass.

## Controls, limits, and completion

The finite-polynomial Kummer control checks the Bass boundary precisely.
Take R'=C[s,s^-1,q], p=s^2. It is etale over the open p!=0, not an A2
Keller source. Trace sends even powers s^(2j) to2p^j and odd powers to0;
thus kerTr contains s and is nonzero. The operators e_p=(s/2)partial_s,
e_q=q partial_q make every Laurent monomial s^i q^j a joint eigenvector.
Every element has FINITE support, so a product of finitely many nonzero
linear Euler factors annihilates it. Euler localization kills R', its
quotient by A, and its trace kernel. D={p=0} is an axis component: all torus
terms vanish, consistently giving rank0. This tests the necessity of Bass
torsion-freeness, not the actual-source theorem. It says NOTHING about an
arbitrary infinite formal series having an Euler annihilator.

At a K_P=0 ordinary node, (1)'s correction is0 although r_P=2. This agrees
with the earlier conditional transport control, not with fixed global
sheet labels. The old missing inequality N<=2+sum K_P would contradict
sum K_P=N-3; neither (1) nor (2) supplies it or controls those global paths.

QUANTITY: whether the exact place bound excludes any previously surviving
configuration in this stated stratum. CHEAPEST TEST performed: the logarithmic
polynomial and LOC-MULT comparison, planned <=900seconds UNMEASURED manual
work; no mathematical subprocess. Verdict KNOWN/WEAKER, no new exclusion,
source point, degree bound or JC2 conclusion. No follow-on or new OPEN selected.

Read scope: TASK and five reports fresh WHOLE, MFS review before producer;
all fresh report reading completed by23:18:39. audit-new exact-pin
REUSED_WHOLE from this agent's FULL2240 blind/cross, with its accepted tiers;
no linked foundations are newly verified. All seven pre/postpins, own WHOLE
partial/PINS, quantity/cheapest-test and collision checks precede the unique
BODY-END. Normal transaction, sealed WHOLE, expected verification and final
custody follow. No scientific execution, outside input, shared edit or worker.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8803`.
- Body SHA-256:
  `3683c4839c2c5114fa9a3efaa58bb8afdd392c6535d38a2e4882e67211cffd9c`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
