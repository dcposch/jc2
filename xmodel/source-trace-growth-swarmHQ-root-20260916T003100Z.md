# Source-degree trace growth: bounded cancellation, unchanged integrality gap

Producer: swarmHQ ROOT (gpt-6-astra), with native Astra co-research.
Date: 2026-09-16 UTC.
Basis: `08624320be973852325011010f56f3b3cd8baaff`.
Evidence: MANUAL. Lifecycle: PRODUCER-CHECKED / UNPROMOTED.
Same-model co-research is not different-model FIRST. JC2 remains unresolved.

## 1. Exact statement

Let R=C[x,y], L=C(x,y), A=C[u,v] contained in L, K=C(u,v),
and d=[L:K]<infinity. For this general calculation u,v may be rational
functions of x,y. Fix an irreducible p in A and its normalized valuation
v_p on K. Write T=Tr_{L/K} and

    b(n)=max({0} union {-v_p(T(h)): h in R, deg(h)<=n, T(h)!=0}).

Degree means ordinary total degree in the specified source coordinates.
The maximum exists: the traces of the finitely many degree<=n monomials
span the relevant space over C, and constants have valuation zero.

Choose a normal closure M/K and one extension w of v_p to M, normalized
by w(p)=1. For all d K-embeddings sigma:L->M put

    rho=max(0, -w(sigma(x)), -w(sigma(y))).

The maximum is over all embeddings and both coordinates. If rho=0 then
b(n)=0 for every n. If rho>0 then, for every n>=d,

    rho*(n-d+1) <= b(n) <= rho*n.                    (1)

In particular lim b(n)/n=rho. Cancellation of conjugate leading terms
cannot postpone a maximally polar power beyond a window of d consecutive
exponents. This is elementary valuation/trace algebra, not a new Keller
source restriction or a literature-novelty claim.

## 2. Proof including cancellation

For every degree<=n polynomial h and every sigma, its monomials have
w-value at least -n*rho. The ultrametric inequality, first for h and
then for the trace sum, proves the upper bound in (1).

Assume rho>0. Choose a constant linear form ell=a*x+b*y so that its
maximal conjugate pole order is rho. Such a choice exists: at each of
the finitely many maximally polar conjugate pairs, cancellation excludes
at most one constant projective direction (and possibly none).

The value group of w is (1/E)Z for some positive E. Let pi be a
uniformizer with w(pi)=1/E and put r=E*rho, a positive integer. For each
embedding set beta_sigma=pi^r*sigma(ell). All have nonnegative value;
at least one has value zero. The distinct nonzero residues of these
elements are a_1,...,a_k, with positive integer multiplicities m_1,...,m_k,
where k<=d. Residue characteristic is zero.

For every positive integer N, not all of the k sums

    sum_j m_j*a_j^(N+s),       0<=s<k,

can vanish. Their coefficient matrix is a Vandermonde matrix times the
invertible diagonal matrix with entries a_j^N. It is invertible; the
nonzero multiplicity vector cannot lie in its kernel.

Take N=n-k+1, which is positive for n>=d. For some m in [N,n] the sum
is nonzero. The residues of positive-valuation beta_sigma contribute zero
to that positive power, so

    w(sum_sigma beta_sigma^m)=0,
    v_p(T(ell^m))=-m*rho.

Although rho can be fractional, this last value is automatically an
integer because the trace lies in K. Periodic cancellations are therefore
retained, not ignored. Since ell^m has source degree m<=n, the lower bound
b(n)>=rho*(n-k+1)>=rho*(n-d+1) follows. No completion or analytic
convergence is required.

## 3. The proposed sublinear estimate is integrality

The following conditions are equivalent:

1. b(n)=o(n).
2. rho=0.
3. x and y are integral over O=A_(p).
4. T(R) is contained in O.
5. b(d)=0.

The growth calculation gives 1 iff 2. Nonnegative values of all
conjugates are equivalent to integrality over the valuation ring: the
elementary symmetric functions give a monic polynomial over O, and an
integral root has nonnegative value in every extension. This gives 2 iff 3.
Integral elements have integral products and traces, giving 3 implies 4;
4 implies 5 is immediate. Finally, 5 includes T(x^j),T(y^j) in O for
1<=j<=d. Newton identities, whose integer denominators are units in O,
place the coefficients of both degree-d regular-representation
characteristic polynomials in O. Thus 5 implies 3.

The Newton implication is KNOWN and explicitly recorded in section 2 of
[the earlier power-trace report](keller-trace-powers-astra-20260911.md).
Its contrary no-rank-cutoff result concerns membership in
C[[u,v]][1/u]+C[[u,v]][1/v], which is NOT an algebra. The present
DVR criterion neither contradicts nor strengthens that mixed-pole result.

For a polynomial Keller source u=f, v=g, proving sublinear growth at every
target prime would make x,y integral over A. Indeed the characteristic
coefficients would lie in the intersection of A_(p) over height-one
primes, which is A. Then R is finite over A; the finite etale plane map
would be an automorphism. This is the desired closing conclusion, not
an estimate supplied by the growth calculation.

## 4. What the actual source derivations provide

Now assume J(f,g)=1. The lifted target derivations are

    D_u=g_y*partial_x-g_x*partial_y,
    D_v=-f_y*partial_x+f_x*partial_y.

They preserve R and commute with field trace. If p_u is nonzero, it is
not divisible by the irreducible p. For any z in K with v_p(z)=-m<0,
the derivative partial_u(z) has valuation exactly -m-1: write z=a/p^m
with a a unit of O, use partial_u(O) contained in O, and note that the
leading coefficient -m*a*p_u is a unit. Characteristic zero is essential.

Put C=deg(g)-2. If b(n)>0 and C>0, choosing h attaining b(n) gives

    deg(D_u h)<=n+C,
    b(n+C)>=b(n)+1.

Iteration and (1) imply rho>=1/C, a LOWER bound. For C<=0 a pole is
impossible: repeated differentiation produces unbounded pole order inside
a fixed finite source-degree space. If p_v is nonzero the corresponding
statement uses D_v and C=deg(f)-2. At least one target partial is nonzero.
The degree-lowering cases are familiar and are not a new degree exclusion.

Ordinary source derivatives also yield the exact adjoint identities

    T(h_x)=partial_u T(f_x*h)+partial_v T(g_x*h),
    T(h_y)=partial_u T(f_y*h)+partial_v T(g_y*h).

For example D_u(f_x)+D_v(g_x)=partial_x J=0 and
f_x D_u+g_x D_v=partial_x. The identities cancel leading poles among
weighted moments of larger source degree. They give no upper sublinear
bound in this calculation. This is a failure of the tested inference,
not a theorem that no further Keller-specific argument can supply one.

## 5. Replay, checks and scope

Desk-only. No mathematical subprocess, CAS, numerical experiment, code
execution from another project, or new control family was used.

The already recorded Kummer cancellation is a useful exact check. In the
general setting take u=x^(-e), v=y, p=u, e>=1. Then d=e,
T(x^m)=0 unless e divides m, and T(x^m)=e*u^(-m/e) when it does.
Consequently rho=1/e and b(n)=floor(n/e). The bounded cancellation
window in (1) is necessary. This is the same Kummer calculation as
section 4 of the earlier report; u is not a polynomial source coordinate,
so it is NOT a Keller counterexample. The identity presentation u=x,v=y
has rho=b(n)=0 and checks the nonpolar case.

ROOT independently derived (1), then exchanged it with the native Astra
co-researcher `/root/source_trace_growth`. Its complete final derivation
was collected and authoritative COMPLETED status observed by00:34 UTC,
before the original00:40 collection and00:45/00:48 terminal targets.
ROOT checked the valuation window, Newton equivalence and both derivative
calculations in full. Same-model agreement supplies no different-model
promotion. The main mathematical task began00:27:50 UTC; no second
research tranche or new control was commissioned.

Pre/post pins matched before sealing:

- FALLACY-v2.md:
  e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.
- xmodel/keller-trace-powers-astra-20260911.md:
  bf94cc3ebf702f85a6971b80560ac3076d84e8873b74778c645333cf173503f0.

## 6. Limitations and next test

No actual trace-regularity, zero-slope estimate, integrality, properness,
degree-one conclusion or polynomial inverse has been proved. The new
bounded test returns to the known local-integrality gap. Its derivative
inequality points in the opposite direction from the proposed upper bound.
STOP this quantitative shortcut; no moment, degree, prime or control farm
follows. A future source-specific argument must actually prove an upper
bound stronger than (1), or furnish another global closing implication.
This report is not a reason to reprove the standard Newton criterion.

## OPENS RAISED

None. No new machine OPEN identifier, computation or dependent task.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

The checker completed exit0; EMPTY concerns identifiers, not novelty.
Manual dispositions: Newton/DVR integrality is KNOWN; the mixed-pole
nonalgebra cutoff is a different question; the actual source adjoint
identities already existed. The quantitative cancellation-window proof
changes the proposed growth test to an explicit integrality equivalence,
not a new closing source implication. No exhaustive novelty claim.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9026`.
- Body SHA-256:
  `4af3a160dbbf279f6e706a46f6d43f7d500c62009a769f6d09c2ea82f415d79e`.
- Frozen basis: `08624320be973852325011010f56f3b3cd8baaff`.
