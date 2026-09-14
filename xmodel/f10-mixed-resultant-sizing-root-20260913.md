# Mixed scalar: fifth-power clearance and a 151-exception bound

ROOT, September13,2026. MANUAL / PRODUCER-CHECKED / UNPROMOTED.
No scientific execution, changed source, interpolation implementation,
effective integer cutoff, all-r scalar theorem, full-source comparison or
JC2 resolution. This is a size/cardinality bound, not an exception list.

## Charged inputs and literal object

WHOLE read after fresh matching pins in this continuation:

- xmodel/f10-mixed-univariate-reduction-root-20260912.md,
  7b8545a623a771ebd423b441c4c1567389d0ca837d4e5b80c8990bc52b1075f8;
- xmodel/f10-mixed-cube-asymptotic-root-20260913.md,
  1c33e474a4378c88603a5591f1b227e08b17ab5ab25c1c9841d93b3f5397ec6b.

Their stale UNPROMOTED headers are historical: the whole-leading interface
and cube asymptotic have the accepted different-model review chains recorded
in AUDIT17zzd and F10-MIXED-CUBE-1. They are dependencies, not newly reviewed
here. No live Astra report was read. ROOT sent its universal monomial bound
as an advisory message after independently deriving it; Astra reports its
separate seven-adic proof does not need that message as a premise.

Use exactly phi=1+u+Xu^2+Yu^3 and

    B=[u^14](phi'/phi) T_(2t-1) T_(4-t),
    T_s=trunc_7 phi^s.

Let U,V,K,P be the literal polynomials in the charged reduction, and
P0=(t-2)P. Its X-degree is7, leading coefficient9(t-2), total (t,X)
degree at most8. For actual t=(5r+2)/(3r+1), r>=2, U is a unit on
the whole algebra Q[X]/P and Y=V/U. Nothing is specialized at U=0.

## 1. Two simultaneous monomial bounds

Every monomial t^i X^j Y^k occurring in B satisfies

    i+j+2k <= 14,             2j+3k <= 15.             (1)

For [u^n]phi^(at+b), a multinomial term uses ell factors, j of Xu^2,
k of Yu^3, and ell-j-k of u. Thus n=ell+j+2k; its coefficient has
t-degree at mostell, proving the first bound with n on the right.
Also 2j+3k<=n. Truncating at7 only removes terms.

Write phi'/phi=(d/du)log(phi). A term of log(phi) of degree m+1 uses
ell>=1 factors with m+1=ell+j+2k. Hence [u^m]phi'/phi has
j+2k<=m and 2j+3k<=m+1. It has no t dependence. Multiply with the
two truncated powers and sum m+n1+n2=14 to obtain both bounds (1).
Cancellation can only remove monomials, so it cannot invalidate the bounds.

In particular k<=5 and j+k<=7. Thus the smaller clearance

    G=U^5 B(t,X,V/U) in Q[t,X]                         (2)

is polynomial. Since total degrees of U,V are at most2,4, a term in G
has total degree at most i+j+4k+2(5-k)<=24. Their X-degrees are2,3,
so its X-degree m is at most j+3k+2(5-k)<=17. G is nonzero by the
accepted cube asymptotic. The installed producer/checker still uses U^7;
no source change or measured runtime saving follows from this note.

## 2. Resultant degree and forced cube factor

Set R(t)=Res_X(P0,G), using the actual generic X-degree m<=17 of G.
Generic coprimality is already a consequence of F10-MIXED-CUBE-1,
so R is a nonzero polynomial in Q[t]. Its degree is at most

    7*24 + m*8 - 7*m = 168+m <=185.                  (3)

For completeness, every nonzero Sylvester determinant monomial uses m
coefficients of P0 and7 coefficients of G. The sum of their X-indices
is7m (equivalently, apply X->lambda X to the resultant). A coefficient
of X^j has t-degree at most8-j or24-j respectively; adding gives (3).
This remains an upper bound if the generic degree is smaller than17.

At delta=t-5/3=h^7, the accepted seven branches satisfy

    U_j=3 A_j(0)^2 h^4+O(h^5),   A_j(0)^7=1/99225,
    B_j=(-2/279006525)h^14+O(h^15).

Consequently G_j has exact h-order34, each with nonzero leading
coefficient. The norm product over all seven branches has h-order238,
that is delta-order34. The prefactor lc_X(P0)^m has order0 at t=5/3.
Thus R has EXACT order34 there. In particular

    Q(t)=R(t)/(3t-5)^34 in Q[t],   Q!=0,
    deg Q<=151,                  Q(5/3)!=0.          (4)

For every actual r, both lc_X(P0) and U remain nonzero/invertible;
the product formula for the resultant therefore gives

    B is not a unit in the whole actual algebra iff Q(t)=0.

The rational map r->t is injective and never takes the value5/3.
Hence there are at most151 distinct actual integer-r exceptions. This
does NOT say r<=151, supply a height bound, identify a single exception,
or prove that there are any exceptions. Nor does scalar unitness alone
give source exclusion. Generic degree loss in G at a specific t does
not introduce a false zero because P0 retains degree7 there and the
root-product formula with fixed generic m remains valid.

## 3. Exact denominator norm as a separate cross-check

The charged reduction gives

    A=(3t-5)(3t-4)(2t-3)/15,
    x0=-3(t-3)/14, U0=(t-3)(6t-11)/196,
    V=qU/3+A(X-x0), U(x0)=U0.

Here q is the polynomial named in that reduction, not Q from (4).
Since lc_X U=3 and deg_X V=3, evaluation at the two U-roots yields

    Res_X(U,V)=9 A^2 U0,
    Res_X(P0,U)=27 Res_X(U,V)^2=2187 A^4 U0^2,
    Norm_(Q(t)[X]/P)(U)=27 A^4 U0^2/(t-2)^2.         (5)

The middle equality uses P0=3V^2 modulo U and the actual degrees7,2;
the sign is positive. Equation (5) independently checks the cube order4
of Norm(U). Therefore the original clearance U^7 has resultant order42,
whereas the smaller clearance U^5 has order34, consistent with section2.
The original general degree bound217 minus42 gives175; (4) improves
that unreviewed bound to151. Neither number is a maximum possible r.

## Checks, disposition and cheapest use

The special cube is a deliberate boundary control: U loses its inverse
there, so a raw resultant zero at5/3 is forced and must not be advertised
as a finite actual-r exception. We used the faithful two-equation branches,
not a false specialization identifying the boundary with Q[X]/(X-1/3)^7.
The direct norm identity (5), generic-degree loss argument and explicit
cardinality-versus-cutoff distinction check three independent failure modes.
These are manual controls, not executed computational controls.

The possible use is a smaller exact resultant or rational-norm computation
if the already-selected unchanged Bezout computation is too expensive.
No interpolation or source rewrite is selected now, and no speedup is
measured. Review these exact bounds before consuming them. Current cheaper
priority remains the source-attached scalar family discriminator plus the
existing one-shot certificate. No new canonical OPEN, AWS allocation,
cap increase, foundation rereview, protected-tree action or publication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6471`.
- Body SHA-256:
  `9ec9e8e52881516ec3073ec7975c7bb2f35f45f116eb1a26aeeda25996f96c99`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
