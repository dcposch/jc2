# General first-delta-order operators: a Puiseux--Fabry exclusion

Owner /root/contact_collision_geometry. MANUAL / UNREVIEWED. Actual first action 2026-09-11 21:36:50 UTC. Original publication reserve 21:52 UTC / HARD 21:55 UTC, unchanged. Basis 0d39df3c9fd69c939a8420c54d03228b9077777d.

Inputs are ROOT TASK, the pinned Bass 1989 PDF, and ROOT's separately authorized ADDENDUM (fresh hash/WHOLE at 21:43:06 UTC). The addendum's Puiseux lead is verified below, not assumed as a theorem; original clocks remain fixed. TASK was read WHOLE after its hash; the PDF was freshly pinned and assigned printed pages 41--49 / PDF pages 4--12 read WHOLE. No clipping, reuse, other report, live affine review or linked reference was used.

## 1. General recurrence and the actual-source vertical case

Let A=C[p,q] inside the actual normalized Keller source R=C[x,y], and N=R/A. Put e_p=p partial_p, e_q=q partial_q, delta=p partial_q, with the lifted derivatives on R. Fix r>=0 and Phi=e_p-r+delta G(e_p,e_q), with delta on the LEFT. We prove injectivity on N for EVERY G in C[X,Y], using Bass and the explicitly named standard background in section 3. This is a manual candidate, not a theorem that arbitrary Keller annihilators have this form.

On degree r+n, coefficients below p-degree r vanish because the diagonal entries i-r are nonzero. The coefficient c_n of p^r q^n is free. Writing the coefficient of p^(r+j)q^(n-j) as c_n V(n,j), the literal order of operators gives

    j V(n,j)+(n-j+1)G(r+j-1,n-j+1)V(n,j-1)=0,
    V(n,0)=1.

Therefore

    V(n,j)=(-1)^j binom(n,j) product_(k=0)^(j-1)G(r+k,n-k).  (1)

Degrees below r have no kernel. Every formal kernel element has the unique expansion

    f=sum_(n>=0)c_n sum_(j=0)^n V(n,j)p^(r+j)q^(n-j).       (2)

In particular f=p^r(H(q)+p times a formal series), H(q)=sum c_n q^n. If f is algebraic over C(p,q), then H is algebraic over C(q). To see this from a NONZERO initial relation, choose polynomial F(p,q,f)=0. The polynomial F(p,q,p^r T) is nonzero. Divide by its greatest common power p^mu; its p=0 coefficient is a nonzero polynomial Q(q,T). Substitution of f/p^r followed by p=0 gives Q(q,H(q))=0. This is exactly the lowest-p-weight relation with wt(T)=r before factoring, not an assumed projection property of algebraic series.

Suppose G has a factor X-(r+J), integer J>=0. In (1) the k=J factor kills every V(n,j) with j>=J+1. Thus every formal kernel element has p-degrees only r,...,r+J and is killed by

    Psi=product_(j=0)^J(e_p-r-j),

a NONZERO diagonal operator. For an actual f in R, Bass Theorem 1.4's torsion-freeness of N over C[e_p,e_q] forces f in A. This includes G=0 by the same direct diagonal conclusion. It does not assert that every algebraic formal kernel element is polynomial in this vertical case: p^r/(1-q) for G=0 is a rational countercontrol, not an actual source element.

To pass from exact kernels to injectivity on N, if Phi f lies in A, subtract from f its finite homogeneous prefix through the degree of Phi f. The remainder stays in R and is killed by Phi, because Phi preserves total degree. This is Bass's printed page 41 reduction. No infinite subseries or arbitrary projection is asserted to belong to R.

## 2. Nonlinear sparse-truncation theorem

THEOREM (manual candidate). For every r>=0 and

    G(X,Y)=Y-(X-r)^2,

every algebraic formal f in C[[p,q]] killed by Phi is polynomial. Consequently this Phi is injective on the actual N, by the preceding finite-prefix reduction and algebraicity of the actual source over C(p,q).

Here G(r+k,n-k)=n-k(k+1), so

    V(n,n)=(-1)^n product_(k=0)^(n-1)(n-k(k+1)).            (3)

Let E={m(m+1):m>=0}. For n=m(m+1), m>=1, the first zero product occurs at j=m+1; all later coefficients vanish. Thus its last possibly nonzero j is m, genuinely sublinear in n. A uniform linear-length nonzero initial window is FALSE, exactly as the task warns. The n=0 term is handled separately and harmlessly.

For n outside E, all factors in (3) are nonzero INTEGERS and therefore have modulus at least one. For n>=8 and ceil(n/2)<=k<=n-1,

    |n-k(k+1)|=k(k+1)-n >= n^2/8.

There are floor(n/2) such factors. Therefore, uniformly outside E,

    |V(n,n)| >= (n^2/8)^floor(n/2),
    |V(n,n)|^(1/n) -> infinity.                            (4)

The one-variable restriction f(p,0)=sum c_n V(n,n)p^(r+n) is algebraic: divide a polynomial relation by its common q power before specializing. One-variable algebraic formal series converge near zero. Thus |c_n V(n,n)|<=M rho^(-r-n) for some M,rho>0. Equation (4) implies |c_n|^(1/n)->0 through n outside E.

It follows that H_good(q)=sum_(n notin E)c_n q^n is ENTIRE. The full H(q) is algebraic by section 1 and hence convergent. Set H_bad=H-H_good, supported on E. If its infinite nonzero exponents are nu_1<nu_2<..., then nu_l/l tends to infinity: a subsequence of m(m+1) is at least quadratically sparse after a finite initial shift.

If H_bad had finite positive radius, the Fabry gap theorem in the form used by Bass on printed page 49 would give a natural boundary on that circle. Adding the entire H_good cannot remove that boundary. But an algebraic H has only finitely many finite singularities and therefore cannot have a natural-boundary circle. This contradiction shows H_bad is entire (the polynomial case is immediate). Thus H is entire algebraic and hence polynomial, by the same algebraic-entire conclusion used by Bass. Only finitely many c_n survive, so (2) is a polynomial.

All infinite decompositions here take place in formal/convergent one-variable series, NOT in the actual source. No arithmetic condition on c_n, no lower coefficient bound, and no assumption that H_good or H_bad is individually algebraic was used. Their complementary roles are essential: entirety of one and sparsity of the other suffice.

## 3. General complex G: Puiseux separation and sparse bad degrees

Explicit STANDARD BACKGROUND, not newly primary-verified here: algebraic formal power series over C converge near the origin; roots of a polynomial in k with polynomial n-coefficients admit convergent Laurent--Puiseux expansions at n=infinity. Such expansions can be differentiated along positive real n. The following proof uses exactly these facts and Bass's printed Fabry argument, not an arithmetic lower bound on arbitrary complex numbers.

Suppose G is nonconstant and has NO factor X-(r+J), J>=0. Put g(k,n)=G(r+k,n-k). If its k-degree v is positive, factor for all sufficiently large real n

    g(k,n)=A(n) product_(i=1)^v(k-z_i(n)),

counting multiplicities. A is a nonzero polynomial; write gamma=deg A>=0, so |A(n)|>=C n^gamma eventually. Its finite zeros are discarded. Each nonconstant unbounded root has leading term c n^s, s>0 rational. Choose 0<epsilon<1/4 below one quarter of EVERY nonzero linear slope modulus, and choose sigma in (0,1) above every sublinear exponent s<1. Bounded roots are also o(n^sigma). Consequently, uniformly for n^sigma<=k<=epsilon n, every root has distance at least Ck from k: sublinear/bounded roots have modulus <=k/2, and linear/superlinear roots have modulus >=2epsilon n with a fixed n-order separation. Thus

    |g(k,n)|>=C n^gamma k^v.                              (5)

For the earlier integer k, classify all possible small distances. A non-real branch has imaginary part with a first nonzero Puiseux power, giving a fixed polynomial lower bound, unless it is identically real. A bounded real branch either stays away from integers, approaches an integer with a first nonzero Puiseux power, or is that constant integer. A constant integer J>=0 would imply g(J,n)=0 identically and the excluded vertical factor. Negative constants or negative unbounded real roots cannot approach k>=0. Linear and superlinear roots already lie outside the window. Only positive real unbounded sublinear roots remain.

For each such root z(n)~c n^s, c>0 and 0<s<1, exclude integer n with dist(z(n),Z)<n^(-L). Choose one L larger than every preceding polynomial-loss exponent and every 1-s. On a dyadic interval [N,2N], z is eventually increasing with derivative bounded below by C N^(s-1). Its range contains O(N^s) relevant integer targets. The preimage of each target's N^(-L)-neighborhood has length O(N^(1-s-L))<1, hence contains O(1) integer n. There are therefore O(N^s) excluded n. Summing dyadic blocks and finitely many branches gives a bad set E_* with count O(X^sigma), after increasing sigma still below one. Repeated roots change constants/multiplicities only.

Outside E_*, every early distance is at least C n^(-L). The O(n^sigma) factors with k<n^sigma consequently lose only O(n^sigma log n) in logarithm. The factors from n^sigma to epsilon n/2 are eventually >=1 by (5), and a positive fraction near epsilon n are >=C n^(gamma+v). Taking j=floor(epsilon n), the recurrence product thus satisfies

    log |V(n,j)| >= c_1 n log n - O(n^sigma log n)-O(n),

for some c_1>0; binom(n,j)>=1. Its nth root tends to infinity. If v=0, g=A(n) is nonconstant of degree gamma>=1, and the same conclusion follows directly from |A(n)|^j, without bad degrees. This also accounts for every leading-coefficient exception.

Convergence of algebraic f gives uniform coefficient bounds |c_n V(n,j)|<=M rho^(-r-n). Thus the c_n subseries outside E_* is entire. The exceptional exponents satisfy nu_l/l->infinity because their counting function is O(X^sigma). Section 2's entire-plus-Fabry argument now applies verbatim to algebraic H: H is polynomial, so f is polynomial. This proves the stronger formal assertion for every nonconstant G without an accessible vertical factor. Vertical factors were settled on N in section 1. Finally if G=gamma is constant, use the actual target coordinates p,u=q-gamma p: Phi is e_p in that frame minus r, so Bass's diagonal theorem applies. Hence every G is covered on N.

## 4. Controls and surviving limits

For G=(Y-1)(X-r+1), no accessible vertical factor exists but V(n,n)=0 for every n>=1. Thus the fixed q=0 exceptional set is cofinite, not sparse; section 3's shorter moving window is indispensable. This is not a counterexample to injectivity. The sublinear truncation of section 2 likewise refutes a uniform linear nonzero window without exceptional degrees. Tiny nonzero complex values are handled by counting bad degrees, never declared integers or uniformly bounded below.

QUANTITY / CHEAPEST TEST: injectivity of the exact first-delta-order family on N, via recurrence, bounded-p diagonal reduction, and the ROOT-suggested but independently checked Puiseux/Fabry estimate. Scientific runtime is UNMEASURED. The remaining source gap is the unproved reduction of arbitrary Keller annihilators to this family; no general U classification, JC2, novelty claim, new OPEN or follow-on is made.

OWN CHECKS: three inputs pinned before their assigned reads; TASK and ADDENDUM untouched. Own WHOLE partial/PINS, input postpins and scope/collision checks precede the unique final marker. Expected transaction verification and sealed WHOLE report/manifest precede final custody. Only bounded apply_patch documentary writes and existing publication; no scientific subprocess, code/import/AST/test/dummy/CAS, coefficients, network/AWS/SSH/Git/protected/shared access, live report or agent. All writers idle before handoff.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11290`.
- Body SHA-256:
  `1c51485f6881294627c5269d62335ed8b471f6278ca52955550a36457f4eed7e`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
