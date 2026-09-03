# Exact band-5 compatibility variety

Let (K=\mathbf Q(a)), (L=z+3a), and (M=z^6L^2).  For

\[
N=243UV^2-3888z^3LVf_3+640b_2z^4LU^3,
\]

with degrees (7,10,14), respectively, the reduced locus (M\mid N) in
\(\mathbb A_K^{35}\) has dimension **30**.  Its unique top component is

\[
b_2=0,\qquad z^3(z+3a)\mid V.
\]

Thus (V=z^3(z+3a)W), \(\deg W\le6\), while (U,f_3) are arbitrary, and
the dimension is (7+8+15=30).  The fixed high summand in the script's
`f3` is a multiple of (M), so this is equally a statement about `f3new`.

The normalization (z=ax), \(\widehat f_3(x)=a^4f_3(ax)\),
\(\widehat b_2=a^5b_2\) is invertible over (K) and reduces to (a=1).
CRT gives

\[
K[x]/(x^6(x+3)^2)\simeq K[x]/(x^6)\times K[t]/(t^2),\quad t=x+3.
\]

The coefficient-to-jet map has determinant (3^{12}=531441).  The degree
bounds leave free kernel dimensions (0,3,7) for (U,V,f_3), so ten affine
directions are added to the 25-variable residue calculation.

Exact `minAssGTZ` over the declared degree-reverse-lexicographic rational
ring finds 15 residue components with dimensions

\[
20^1,\quad19^8,\quad18^3,\quad17^3.
\]

Consequently the original component histogram is

\[
30^1,\quad29^8,\quad28^3,\quad27^3.
\]

The local valuation classification has six (x^6)-components: dense orders
\((\operatorname{ord}U,\operatorname{ord}V)=(3,0),(2,1),(0,2),(1,2)\),
plus (b_2=0,\operatorname{ord}V\ge3) and
\(\operatorname{ord}U\ge1,\operatorname{ord}V\ge3\).  The (t^2)-factor
has primes

\[
(b_2,V(-3)),\quad(U(-3),V(-3)),\quad
(U(-3),U'(-3)V(-3)-16(-3)^3f_3(-3)).
\]

Accounting for the shared (b_2) and removing contained pairings gives the
15 components above.  In particular, the band-5 equations impose only
codimension five on the 35 old parameters.  Adding the unaffected 15
`f4new,b4` directions and the 13-dimensional band-5 linear kernel gives
cumulative fiber dimension (30+15+13=58) over (K), or 59 including (a).

Replay from this directory:

```sh
python3 band5_component_audit.py
sha256sum -c SHA256SUMS
```

This is an exact local-band statement, not a full Keller-pair existence
claim.
