# Independent audit of the six u_s=2 U-NEG radius licences

Primary source p.194, following Lemma6.1, says that the minor logarithmic
radius is **greater than or equal to1**. It does not say strictly greater.
Proposition6.3 p.197 requires delta* >=v/u; in the complementary detector
regime the source-supported interval therefore includes its lower boundary:

    1 <= delta* < v/u.

The frozen face screen's detector_orders() starts num=den+1 and thus checks
only 1<delta*<v/u. The four-row proof's interior delta*=3/2 obstruction is
correct as arithmetic, but it does not eliminate delta*=1. The other two
u=2 rows' empty strict interval likewise does not eliminate that boundary.

The face identity consumed by the frozen script is

    X=u*delta-v, a=W*X-1+delta,
    a*q*p' - X*p*q' = (v-u)*p^(W+1).

At delta=1, X=u-v and a=W*X. Dividing by v-u gives

    p*q' - W*q*p' = p^(W+1).

For any monic degree-u polynomial p and any constant C, the polynomial
q=(pi+C)*p^W satisfies this identity exactly; its degree is u*W+1. In the
u=2 case choose p=pi*(pi-1), C=2. It has two distinct split coefficients;
q=(pi+2)*[pi*(pi-1)]^W is an explicit boundary-face solution for every
nonnegative integer W. The reduced radius denominator is1, so the Galois
orbit condition imposes no restriction. At each p root, q has multiplicity
W (the allowed low branch), and the remaining linear root supplies the
one extra degree. The local multiplicity screen therefore also passes.

This is a face solution, not a source-pair realization. It proves that the
(G)/(L) necessary screen has not excluded the boundary. Proposition5.6's
major-D1 degree-reduction conclusion does not by itself exclude an integer
minor split at radius1. No separate such lemma has been located in the
charged primary source.

Consequently the honest U-NEG status is **84 automatically licensed u=1
rows, plus6 u=2 rows conditional on the unresolved Prop6.3 radius licence**.
A separate necessary source-tree obstruction may exclude those six rows,
but must not be presented as proof of the missing radius licence or used
to convert conditional descent data into an actual child.
