# A mixed resonant family: algebraic formal kernels are polynomial

Owner /root/contact_collision_geometry. MANUAL / UNREVIEWED. Actual first action 2026-09-11 21:04:12 UTC. Original publication reserve 21:25 UTC / HARD 21:28 UTC, unchanged. Basis 0d39df3c9fd69c939a8420c54d03228b9077777d.

Scientific inputs are ROOT TASK, Bass's pinned 1989 article, and the subsequently authorized ROOT ADDENDUM, fresh-pinned and read WHOLE at 21:09:47 UTC. The amendment adds one coordinate-resonant endpoint without changing either clock. Printed pages 39--49 (PDF pages 2--12), the entire assigned mathematical article, were read after matching the PDF hash; no references or other reports were opened. Bass's formal-versus-Keller distinction is retained. The results below are manual candidates, not campaign promotions or a general U-torsion theorem.

## 1. Statement and homogeneous kernel

THEOREM (manual candidate). Let a,b>0 be coprime integers, c any integer and g in C[T] nonconstant. With e_p=p partial_p, e_q=q partial_q, e=e_p+e_q and delta=p partial_q, put

    Phi=a e_p-b e_q-c+delta g(e).

If f in C[[p,q]] is algebraic over C(p,q) and Phi f=0, then f belongs to C[p,q]. No degree bound, arithmetic coefficient hypothesis, actual Keller extension or convergence hypothesis beyond algebraicity is imposed.

Put m=a+b. The operators e and delta commute and preserve total degree. On degree d, g(e) is multiplication by g(d). Set h_d=g(d)/m and u_d=q-h_d p. Directly,

    (a e_p-b e_q+g(d)delta)(p)=a p,
    (a e_p-b e_q+g(d)delta)(u_d)=-b u_d.

Thus p^i u_d^j, i+j=d, is an eigenbasis with eigenvalues ai-bj-c. In particular the shear has the MINUS sign q-g(d)p/m. Distinct i give eigenvalues differing by m, so the homogeneous kernel is one-dimensional exactly when ai-bj=c has a nonnegative integer solution of degree d.

Let (r,s) be the unique first nonnegative solution of ar-bs=c: all nonnegative solutions are

    (i_n,j_n)=(r+bn,s+an), n>=0.

Existence follows from coprimality and adding sufficiently many copies of (b,a); subtract until both coordinates cannot remain nonnegative. Put d_n=r+s+mn and h_n=g(d_n)/m. Every formal kernel element has the UNIQUE expansion

    f=sum_(n>=0) c_n p^(r+bn)(q-h_n p)^(s+an).           (1)

All d_n are distinct. The zero solution is immediate, so assume some c_n is nonzero.

## 2. Algebraic lowest-weight series and coefficient bound

Give p weight a and q weight -b. In the nth summand of (1), replacing k copies of q by -h_n p raises weight from c to c+mk. Therefore every weight of f is at least c, and its nonzero lowest-weight part is

    f_0=p^r q^s B(p^b q^a),  B(t)=sum_(n>=0)c_n t^n.    (2)

Here the subscript 0 denotes lowest WEIGHT, not total degree.

We prove, rather than assume, that f_0 is algebraic. Choose a nonzero polynomial relation H(p,q,f)=0. Give its indeterminate T weight c. Let mu be the least weight among the finitely many monomials of H, and H_mu the sum of its monomials of that weight. H_mu is a NONZERO polynomial: distinct monomials remain distinct. Under

    (p,q,T) -> (tau^a p,tau^(-b)q,tau^c T),

write f_tau=f(tau^a p,tau^(-b)q)=tau^c(f_0+higher powers of tau). This is a well-defined element of C[[p,q]]((tau)) because f's weights are bounded below. Multiplication and the relation H(tau^a p,tau^(-b)q,f_tau)=0 remain valid there: for each tau coefficient only finitely many weight products occur, and their coefficients are ordinary formal p,q series. Its coefficient of tau^mu is

    H_mu(p,q,f_0)=0.

Thus f_0 is algebraic over C(p,q), despite the negative q weight.

It follows that B(t) is algebraic over C(t). Here is a precise specialization argument avoiding substitution in an arbitrary two-variable formal series. Formula (2) lies in C[p][[q]], since a>0 and each q coefficient has only finitely many terms. Its polynomial relation also lies in that ring. Choose lambda in C* for which H_mu(lambda,q,T) is not the zero polynomial; only finitely many lambda are excluded. Substituting p=lambda shows B(lambda^b q^a) is algebraic over C(q), after dividing the prefactor lambda^r q^s in the fraction field. Since t=lambda^b q^a makes C(q) finite algebraic over C(t), transitivity proves the claim for the original series B(t).

Now specialize (1) at q=0:

    f(p,0)=sum_(n>=0)c_n(-h_n)^(s+an) p^d_n.            (3)

This is algebraic over C(p). Indeed divide a polynomial relation for f by its maximal common q factor; its specialization at q=0 is a nonzero relation. A one-variable algebraic formal series converges near zero, the standard fact also used in Bass's printed page 49 argument. Hence, for some rho>0 and M>0, its degree-d coefficient has modulus at most M rho^(-d). Distinct d_n in (3) rule out cancellation.

Let k=deg g>=1. The polynomial h_n in n has degree k and nonzero leading coefficient; after finitely many n, |h_n|>=K n^k for some K>0. Its finitely many zeros cause no difficulty. Consequently

    |c_n|^(1/n)
      <= M^(1/n) rho^(-d_n/n) |h_n|^(-a-s/n) -> 0.

The series in (2) is therefore ENTIRE. An entire algebraic function is a polynomial: outside a large disk, the polynomial relation and the elementary root bound give polynomial growth; Cauchy's estimates kill all sufficiently high Taylor coefficients. This is also the terminal algebraic-entire argument on Bass's printed page 49. Thus only finitely many c_n are nonzero, and (1) makes f polynomial. No lower exponential bound on coefficients was used.

## 3. Authorized coordinate-resonant endpoint

For each integer r>=0, the same exclusion holds for

    Phi_r=e_p-r+delta g(e),  deg g>=1.

This includes r=0 under ADDENDUM; it is not silently inferred from Bass's printed special-linear endpoint condition. On total degree d, put u=q-g(d)p. Direct evaluation gives (e_p+g(d)delta)p=p and (e_p+g(d)delta)u=0. The eigenbasis p^i u^j has eigenvalue i-r, so the only kernel vector when d=r+n is p^r(q-g(r+n)p)^n; degrees d<r have zero kernel. Thus

    f=p^r sum_(n>=0)c_n(q-g(r+n)p)^n.                    (4)

Its lowest p-order is r, with coefficient B(q)=sum c_n q^n. Apply the polynomial-initial-relation argument above with wt(p)=1, wt(q)=0 and wt(T)=r; it proves p^r B(q) algebraic, hence B(q) algebraic by the same legitimate p=lambda specialization. At q=0, distinct powers p^(r+n) have coefficients c_n[-g(r+n)]^n. The convergent algebraic restriction therefore gives

    |c_n|^(1/n)<=M^(1/n)rho^(-1-r/n)/|g(r+n)| -> 0.

Only finitely many g(r+n) vanish. Hence B is entire algebraic and polynomial, proving that f is polynomial. The n=0 term is simply c_0 p^r; no division by g(r) or by a possibly zero c_n occurs. The argument covers r=0 literally and uses no actual-source degree projection.

## 4. Controls, scope and closeout

The nonconstant hypothesis is essential. For g=gamma constant, put u=q-gamma p/(a+b). Then

    f=p^r u^s/(1-p^b u^a)

is a nonpolynomial rational formal solution of the positive-a,b operator: p^b u^a is invariant under a e_p-b e_q+gamma delta and p^r u^s has eigenvalue c. At the coordinate endpoint the corresponding control is p^r/(1-q+gamma p). Both denominators have constant term one; neither control is an actual globally regular Keller element merely because it is an algebraic germ. They show exactly where the growing shear matters.

No trace section, global shear automorphism of a Keller extension, local nilpotence of its lifted delta, or closure under homogeneous projections was assumed. All shears and projections act only on the ambient formal series degree pieces. The proof does not classify general elements of U or show that an arbitrary actual-source annihilator has either displayed form. ROOT's ADDENDUM records a later-literature motivation, not a theorem imported into this proof; no new actual-Keller frontier, JC2 conclusion or novelty claim is asserted.

QUANTITY / CHEAPEST TEST: all-degree algebraic-formal kernel exclusion for the two exact displayed families, by a nonzero weighted initial polynomial relation and the one-variable coefficient bound. The endpoint is PROVED at this manual-candidate tier, not left GAP. Scientific runtime is UNMEASURED; no coefficient scan, computation, new OPEN, review launch or successor is authorized here.

OWN CHECKS: three inputs are pinned before reads and postpinned before seal; ROOT TASK and ADDENDUM are preserved. No clipping or reuse. Own WHOLE partial/PINS readback, scope/OPEN/collision checks precede the unique final BODY-END marker. Close/finalize/expected-manifest verification and sealed WHOLE report/manifest readback precede final custody. Only owned documentary bytes were written by apply_patch and the existing transaction. No scientific subprocess, code/import/AST/syntax/test/CAS/dummy, coefficient artifact, network/AWS/SSH/Git/protected/shared access or other agent. All writers are idle before handoff.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8853`.
- Body SHA-256:
  `382e24769ffbafd09e7f9b76a49c2d77ef0f494b96dc1d8e671e49366f11ab3d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
