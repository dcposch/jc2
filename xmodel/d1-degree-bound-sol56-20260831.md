# D1-DEGREE: degree constraints for the repaired \(N=4\) residual

## 0. Scope, integrity, and conventions

The three frozen inputs were hashed before reading.  All three matched the charged
values exactly:

```text
b9a83b0783f4b9b844bc881739e0b3c7c63efeb8683f862e007e6584af238696  pi1s4-close-residual-r2-opus5-20260831.md
b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55  b0-trivial-dicritical-proof-opus5-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
```

Write `IN` for the frozen-input directory named in the charge.  I use the repaired
residual displayed in the question as the standing object.  `PROMOTED` means
integration section 1.  Claims imported from CLOSE-RESIDUAL r2 are marked
`PROVISIONAL`; in particular, its closure for `deg D_1 <= 4` is used only when
stating the payoff, never to prove a degree assertion.

**Outcome.**  There is no finite upper bound on the ordinary plane degree that can
follow from the promoted, target-isomorphism-invariant Keller-cover data.  If one
residual map exists, triangular target automorphisms preserve every datum in the
charge and make `deg D_1` arbitrarily large (section 2).  Thus the raw degree problem
needs a target-coordinate gauge; the correct successor is an
`Aut(A^2)`-minimal-degree or endpoint-polar-order problem.  In a fixed target gauge,
Chau does give a new necessary constraint on the reduced pair:

```text
(d/g,n/g) = (u,1), or (u,2) with u odd >= 3, or (4,3),
where g = gcd(d,n).
```

No CAS or uncertain-duration computation was run.  No charged/canonical file or
`jc2-lean` was inspected or changed; this report is the only file created.

## 1. Promoted input ledger

The following typing is load-bearing.

1. `N=4` is the function-field/geometric degree
   `[C(x,y):C(P,Q)]`, not `max(deg P,deg Q)`
   (`IN/b0-trivial-dicritical-proof-opus5-20260831.md:38-40`).  On a resolved
   compactification, `mu_l` is the generic **transverse** local degree along a
   dicritical, `s_l` is the degree of its map to its image, and `corr_l` sums
   multiplicity jumps at finite points of its affine part
   (`ibid.:41-50`).
2. Orevkov's promoted exact budget is
   ```text
   sum_l (mu_l + corr_l) = N-1.
   ```
   (`ibid.:63-65`).  At `N=4` the relevant decomposition of `3` is exactly
   `(mu,corr)=(2,0)+(1,0)` (`ibid.:329-345,369-375`).  This does not say that
   either summand is a pole order or an image degree.
3. In the repaired residual, `A_F=D_1 union D_0`; both normalisations are
   `A^1`; `s_1=s_0=1`; `a_{D_1}=2`, `a_{D_0}=3`; `Br=D_1`; and the connected
   degree-four cover has transposition meridians.  Every singularity of `D_1`
   is a double point of two smooth branches with `a_p=0` and disjoint local
   transpositions (`IN/pi1s4-close-residual-r2-opus5-20260831.md:39-56`), with
   the charged repair `Sing D_1 intersect D_0 = empty`.
4. In target affine coordinates adapted to the polynomial parametrisation,
   `gamma(t)=(p(t),q(t))`, put `d=deg p>n=deg q>=1`; then
   `deg D_1=d` and, at its unique place at infinity,
   `(ord v,ord u)=(d-n,d)` (`ibid.:50-56`).  These are tangential pole orders,
   not the transverse integer `mu_1=2`.
5. The corrected PI1-S4 theorem closes the coprime stratum
   `gcd(d,n)=1` at its promoted scope
   (`IN/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md:28-47`).
   CLOSE-RESIDUAL's stronger low-degree/M-INF conclusions remain
   `PROVISIONAL` (`ibid.:63-77`).

Finally, the B0 source expressly withholds any component-wise copy of `(M')`
(`IN/b0-trivial-dicritical-proof-opus5-20260831.md:52-60`).  Accordingly,
section 4 below re-derives the only aggregate equality it uses from the promoted
Euler identity and flat fibre counts; it does not import B0 Theorem 4.3(5).

## 2. Compactification and the Orevkov tree

### 2.1 What the tree actually records

Orevkov, Lemma 2.1, says that each connected component of `L_FC` is a
linear chain meeting `L_infty` once; its endpoint is the sole dicritical and
all preceding vertices are contracted to finite points.  Thus the residual has
two linear hairs, ending in the vertices labelled `(mu,s,corr)=(2,1,0)` and
`(1,1,0)`.  The `2+1` budget fixes neither the lengths nor the
self-intersection weights of these hairs.

Let `l_1 ~= P^1` be the first endpoint and let
`z_infty=l_1 intersect L_infty`.  Since `s_1=1` and
`l_1-{z_infty} ~= A^1`, restriction of the two affine target coordinates gives
the birational parametrisation `(p(t),q(t))`.  Hence

```text
deg p = -ord_{z_infty}(u o Phi|l_1),
deg q = -ord_{z_infty}(v o Phi|l_1).
```

Equivalently, for a generic target line `H` and a projective resolution on
which `Phi` is a morphism,

```text
deg D_1 = l_1 . Phi^*H.
```

This separates the dicritical divisor `l_1`, its physical place `z_infty`,
and the source alteration series.  In particular the chart equality
`mu_l=n_phi-2m_phi=l-k` (`IN/b0-trivial-dicritical-proof-opus5-20260831.md:102-141`)
only gives `l-k=2`; it does not identify either chart integer with `(d,n)`.

Put `L=Phi^*H`.  Geometric degree gives `L^2=4`, but this does not bound
`l_1.L`.  In a blow-up presentation

```text
L = M H_source - sum_i b_i E_i,
M^2 - sum_i b_i^2 = 4,
```

whereas `l_1.L` also needs the class of `l_1` and all base-point
multiplicities.  None is promoted.  Nor can an unspecified endpoint
self-intersection replace them: blowing up `z_infty` preserves the affine map,
curve, and cover data while decreasing the chosen strict transform's square.
The missing object is the two-coordinate polar vector at `z_infty`, not the
unweighted chain shape.

### 2.2 A coordinate-symmetry no-go theorem

> **Proposition 2.1 (proved here).**  The class described by the charged
> residual is either empty or contains curves `D_1` of unbounded ordinary
> plane degree.  More precisely, the target-polynomial-automorphism orbit of
> any one residual object has unbounded `deg D_1` while all promoted
> Keller-cover data stay fixed.

*Proof.*  Suppose `F` is one residual object and write its parametrisation as
`(p(t),q(t))`, with `r=deg p>0`.  For any integer `k` with
`kr>deg q`, let

```text
T_k(u,v)=(u,v+u^k),       F_k=T_k o F.
```

`T_k` is a polynomial automorphism with Jacobian one.  Consequently `F_k`
has the same function-field degree and Keller Jacobian, and
`A_{F_k}=T_k(A_F)`.  Base change by this target isomorphism preserves the
finite cover, its connectedness, `mu_l`, `s_l`, finite multiplicity jumps
`corr_l`, all `a_D` and `a_p`, and all local/global monodromy.  It also
preserves normalisations, analytic branch types, and all incidences in the
charge.

The transformed parametrisation is `(p,q+p^k)`.  Its two degrees are
`(r,kr)`; after swapping target coordinates the normalised pair is

```text
(d_k,n_k)=(kr,r).
```

The parametrisation remains birational, and a generic affine line pulls back
to a polynomial of degree `kr`, so `deg T_k(D_1)=kr`.  This tends to infinity.
`[]`

Thus a universal raw-degree bound would already prove that the residual class
is empty; it cannot be a nontrivial numerical consequence of the invariant
`2+1` profile.  The statement useful for B0 must instead bound

```text
min_{T in Aut(A^2)} deg T(D_1),
```

or first impose a canonical Jung/Orevkov target gauge and then bound the
endpoint polar vector.  No such gauge or vector is promoted.

## 3. Jelonek--Chau degree bounds

Write `M=deg P >= E=deg Q` in the same target coordinates used for
`(d,n)`, and keep `N=4` separate from `M`.

### 3.1 Jelonek: a coordinate-degree bound, not an `N`-bound

Jelonek's 1993 Theorem 15 says for a dominant
`f=(f_1,...,f_m):C^m -> C^m`

```text
deg S_f <= (product_i deg f_i - mu(f))/min_i deg f_i.
```

Here `mu(f)` is geometric degree.  In this lane it gives

```text
deg A_F <= (M E-4)/E = M-4/E < M.
```

Since `A_F=D_1 union D_0` is reduced with distinct components,
`deg A_F=d+deg D_0`; integrality therefore yields the useful but
coordinate-dependent estimate

```text
d+deg D_0 <= M-1,             hence d <= M-2.                 (3.1)
```

The later quantitative theorem of Jelonek--Lason says that the
nonproperness set of a polynomial map of algebraic degree `M` is covered by
parametric curves of degree at most `M-1` (Theorem 3.2); this again uses
**algebraic** degree, not geometric degree.  The 1999 *Testing sets for
properness* paper supplies testing-set and uniruledness theorems, but no
replacement of `M` by `mu(f)` in (3.1).  In particular Bezout gives only
`4<=ME`, the wrong direction.  Proposition 2.1 also explicitly makes `M`
unbounded under target postcomposition while `N=4` stays fixed.  Thus none
of these results produces a numerical `B(N)`.

### 3.2 Chau: a genuine constraint on the reduced pair

Chau 1999, Theorem 4.4(E1), applies after a generic source linear change
(making the coordinates monic in `y`) and says that every dicritical-image
parametrisation `(P_phi,Q_phi)` satisfies

```text
deg P_phi / deg Q_phi = deg P / deg Q.                         (3.2)
```

Because `s_1=s_0=1`, these are birational parametrisations of `D_1,D_0`.
Put

```text
g=gcd(d,n),       (u,v)=(d/g,n/g),
k=gcd(M,E),       (M,E)=k(u,v).
```

Chau's Theorem B says that, if `v>1`, there are nonnegative integers
`r,s`, not both zero, such that

```text
N = r u+s v >= min(2v,u);                                     (3.3)
```

the alternative in the theorem is `v=1`.  At `N=4`, (3.3) is elementary
to solve.  If `v>=3`, the lower bound forces `u<=4`, hence coprimality and
`u>v` give only `(u,v)=(4,3)`.  If `v=2`, coprimality makes `u` any odd
integer at least three, and `4=0*u+2*2` is not excluded.  Therefore

```text
(d/g,n/g) in {(u,1):u>=2}
              union {(u,2):u>=3 odd}
              union {(4,3)}.                                  (3.4)
```

This is necessary, not an existence assertion.  On the promoted residual
the coprime case is already closed, so an actual escape has `g>=2` and lies
in the three corresponding scaled families.  In a Jung-reduced target gauge
the divisible family `(u,1)` is removed by triangular degree reduction, but
the infinite `(odd,2)` family remains.

Applied exactly as requested to the promoted `d<=9` intermediate survivor
list, (3.4) retains `(4,3)` and excludes

```text
(5,4), (7,4), (8,3), (9,4), (9,8).
```

There is also a scale constraint.  If the degree pair of `D_0` is
`g_0(u,v)`, then (3.1) becomes

```text
(g+g_0)u <= ku-1,       so g+g_0 <= k-1 and g <= k-2.          (3.5)
```

But `k=gcd(M,E)` is not bounded by `N`; (3.5) is not a finite checklist.

## 4. Fibre and aggregate identities

The component-wise `(M')` shortcut is unavailable, but the correct
two-component identity is short enough to derive.

Let `Sigma=Sing(D_1 union D_0)`, `m=#Sigma`,
`D_i^o=D_i-Sigma`, and `chi_i=chi_c(D_i^o)`.  Stratifying the promoted
Euler identity

```text
1=4(1-chi_c(A_F))+chi_c(F^{-1}(A_F))
```

and using generic affine-fibre counts two and three gives

```text
2 chi_1+chi_0 = 3-4m+sum_{p in Sigma} a_p.                    (4.1)
```

Let `b_{i,p}` be the number of branches of `D_i` at `p` (zero if `p`
is not on that component), and `B_i=sum_p b_{i,p}`.  Both normalisations
are `A^1`, so `chi_i=1-B_i`; hence (4.1) is

```text
2B_1+B_0 = 4m-sum_p a_p.                                     (4.2)
```

Flatness at each point gives independently

```text
2b_{1,p}+b_{0,p}+a_p+epsilon_p=4,                            (4.3)
```

where `epsilon_p>=0` allows any extra contracted boundary contribution.
Summing (4.3) and comparing with (4.2) forces every `epsilon_p=0`.
After that, (4.2) is exactly the sum of (4.3): it supplies no inequality.
Locally one recovers only the charged facts and small branch-count caps:

* at `Sing D_1`, disjointness from `D_0` gives `2*2+a_p=4`, hence
  `a_p=0`;
* at `Sing D_0-D_1`, a `k`-branch point has `k+a_p=4`, hence `k<=4`;
* if a singular point of `D_0` lies on the smooth locus of `D_1`, then
  `2+k+a_p=4`, hence `k<=2`.

No tangency multiplicity occurs.  Indeed, at a singular point of `D_1`,
the two smooth branches have

```text
delta_p=I_p(branch_1,branch_2),
delta_aff(D_1)=sum_p delta_p,
delta_aff+delta_infty=(d-1)(d-2)/2.                           (4.4)
```

The local monodromies `(12)` and `(34)` see the two branch germs but not
their mutual intersection order.  Thus (4.4) and nonempty singular locus
give only `d>=3` and `#Sing D_1<=delta_aff`, not an upper bound.

For a concrete diagnostic (not asserted to be a Keller or global `S_4`
example),

```text
gamma_m(t)=(t(t^2-1)^m,t^2-1),       m>=1,
x^2=y^(2m)(y+1).
```

This is birational with normalisation `A^1`, one place at infinity, pair
`(d,n)=(2m+1,2)`, and one affine double point of two smooth branches with
intersection multiplicity `m`.  It demonstrates exactly why branch counts,
`a_p=0`, and the aggregate cannot control either `delta_aff` or `d`.

## 5. The \(S_4\)-cover and Euler characteristics

Let `r=#Sing D_1`.  Normalisation by `A^1` and identification of two
points at each double point give

```text
chi_c(D_1)=1-r,       chi_c(D_1-Sing D_1)=1-2r,
chi_c(A^2-D_1)=r.
```

The fibre cardinalities of `q:Y->A^2` are respectively four, three, and
two on the complement, smooth branch locus, and singular locus (the last
from two disjoint transpositions).  Therefore

```text
chi_c(Y)=4r+3(1-2r)+2r=3.                                    (5.1)
```

This is an identity independent of `r,d,n`; the unbranched component
`D_0` cannot change it.

There is, however, an exact way to expose the missing degree invariant.
Choose a generic affine target line `L`, avoiding all special points and
with a different point at infinity from the unique one of `D_1`.  It meets
`D_1` transversely in `d` points.  The generic-line theorem for curve
complements makes
`pi_1(L-D_1)->pi_1(A^2-D_1)` surjective, so the restricted degree-four
cover `C_L=q^{-1}(L)` is connected.  Let `Pi in S_4` be the ordered product
of its `d` transposition monodromies, and let `c(Pi)` be its number of
cycles.  On compactifying the cover, finite ramification contributes `d`
and ramification over infinity contributes `4-c(Pi)`.  Riemann--Hurwitz
gives

```text
2g_L-2 = -8+d+4-c(Pi),
d = 2g_L+c(Pi)+2 <= 2g_L+6.                                  (5.2)
```

Equivalently, `chi_c(C_L)=4-d`.  Parity merely says that for odd `d`,
`Pi` is a transposition (`c=3`) or a four-cycle (`c=1`), while for even
`d` it is the identity (`c=4`), a three-cycle, or a double transposition
(both `c=2`).  Nothing promoted bounds `g_L`, so (5.2) is a conversion
law, not a degree cap.

If `e=deg D_0`, then passing from `C_L` to the original affine source
removes one boundary point above each of the `d+e` intersections with
`A_F`; hence the generic Keller-pencil fibre satisfies

```text
chi_c(F^{-1}(L))=4-2d-e.                                     (5.3)
```

Again its genus may grow with `d`.  Geometrically, the missing invariant
can be named as `g_L`, the horizontal-different intersection
`B_1.q^*L=d`, or the pole order at infinity of the quartic discriminant.

## 6. Consequences for the normalized pair \((d,n)\)

The unconditional fixed-coordinate information obtained in this lane is:

```text
d>=3;
gcd(d,n)=g>=2 for any escape from the promoted coprime theorem;
(d/g,n/g) is (u,1), (odd u,2), or (4,3);
d=2g_L+c(Pi)+2;
g <= gcd(deg P,deg Q)-2.
```

In particular an escaping residual has `d>=4`.  Through `d<=9`, the Chau
filter leaves the noncoprime pairs

```text
(4,2);
(6,2),(6,3),(6,4);
(8,2),(8,4),(8,6);
(9,3),(9,6).
```

This is not yet a finite global list.  If one additionally imposed a
Jung-reduced target gauge (so the reduced denominator-one family has been
removed), the displayed list would shrink to `(6,4),(8,6),(9,6)`; no such
gauge is presently part of the promoted residual.  Separately, section 3.2
reduces the charged coprime intermediate kill-list to the single pair
`(4,3)`.

The `PROVISIONAL` CLOSE-RESIDUAL result kills `(4,2)` and, more generally,
closes any representative with `deg D_1<=4`.  Because target automorphisms
preserve the cover problem, its invariant payoff is properly phrased as:

```text
if min_{T in Aut(A^2)} deg T(D_1) <= 4, then the residual is closed
(conditional on the provisional residual-closure review).
```

The provisional `(M-INF)` reduction asks for
`beta_h<=2d+n-2`; sections 4--5 provide no bound on `beta_h`, the conductor,
or `g_L`.  Thus neither aggregate Euler data nor the `S_4` Euler identity
turns (3.4) into a finite checklist.

## 7. Verdict and typed OPEN

**No finite bound `B` on ordinary `deg D_1` is proved; more strongly, such a
bound is incompatible with target-automorphism closure unless the residual
class is empty.**  The four requested routes fail closed as follows.

1. Orevkov's `2+1` identity controls transverse local degrees and finite
   jumps.  Degree is the unrecorded tangential pole order at the endpoint.
2. Jelonek bounds by algebraic coordinate degree, which geometric degree four
   neither bounds nor is confused with.  Chau supplies (3.4), not a scale cap.
3. The correct two-component aggregate collapses to the sum of pointwise flat
   fibre equations and is insensitive to branch intersection multiplicity.
4. `chi_c(Y)=3` is an identity.  The generic slice replaces the desired degree
   by the equally unbounded genus/different in (5.2).

> **`OPEN[PI1S4-D1-POLAR-GAUGE]`.**  Fix a canonical target gauge, or replace
> raw degree by
> `d_min=min_{T in Aut(A^2)} deg T(D_1)`.  Then acquire the endpoint polar
> vector
> ```text
> (-ord_{z_infty}(u|l_1), -ord_{z_infty}(v|l_1)),
> ```
> equivalently the two pullback-of-ruling coefficient vectors/base-point
> multiplicities on a minimal weighted Orevkov tree, and bound `d_min`.

> **`OPEN[PI1S4-D1-DEGREE/GENERIC-SLICE-DIFFERENT]`.**  Bound the compact
> genus `g_L` of a generic Keller-pencil fibre, equivalently the horizontal
> different intersection or quartic-discriminant pole order.  Formula (5.2)
> converts `g_L<=G` into `deg D_1<=2G+6` in that fixed gauge.

> **`OPEN[PI1S4-D1-DELTA/CONDUCTOR]`.**  To make the aggregate/genus and
> provisional `(M-INF)` route bite, supply a Keller-specific upper bound on
> `delta_aff=sum I_p` or directly on the last characteristic exponent
> `beta_h`.  The promoted values `a_p=0` and disjoint transpositions record
> branch count, not conductor length.

Accordingly `OPEN[PI1S4-D1-DEGREE]`, as literally phrased for ordinary plane
degree, should be replaced by the first typed OPEN.  A bound `d_min<=4` would
have exactly the campaign payoff requested, conditional on review of the
provisional residual closure.

## References

Primary bytes used or checked in this lane:

```text
30b497466c1c27923a918db1c7277e90485667647fb3f2d6505f3f2c26ef420e  189637 bytes
Z. Jelonek, "The set of points at which a polynomial map is not proper",
Ann. Polon. Math. 58 (1993), 259-266, Theorem 15 and Corollary 16.
https://matwbn.icm.edu.pl/ksiazki/apm/apm58/apm5834.pdf

febddbecb4c54d354fefca1a7e7730fcc18c0e2807fe3e03b5af8017b1d59d39  268049 bytes
Nguyen Van Chau, "Non-zero constant Jacobian polynomial maps of C^2",
Ann. Polon. Math. 71 (1999), 287-310, Theorem B, Theorem 3.6(ii),
and Theorem 4.4(E1).
https://matwbn.icm.edu.pl/ksiazki/apm/apm71/apm7135.pdf

a8476f967c1dd2f929cc80f494d05b1fc77d973558aa40bafef6e3a935a17fff  562720 bytes
Z. Jelonek and M. Lason, "Quantitative properties of the non-properness
set of a polynomial map", Manuscripta Math. 156 (2018), 383-397,
Theorem 3.2.  DOI 10.1007/s00229-017-0965-0.
https://link.springer.com/content/pdf/10.1007/s00229-017-0965-0.pdf
ArXiv v2 cross-check: da2c918f0aca141043333b05863a088abea6402c43fdd8e589aa074e81e9159a,
229101 bytes, https://arxiv.org/pdf/1411.5011v2

f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db  163174 bytes
S. Yu. Orevkov, "On three-sheeted polynomial mappings of C^2",
Math. USSR-Izv. 29 (1987), 587-596, Lemmas 2.1 and 4.2.
https://www.math.univ-toulouse.fr/~orevkov/jc86.pdf
```

Jelonek, *Testing sets for properness of polynomial mappings*, Math. Ann.
315 (1999), 1-35, DOI `10.1007/s002080050316`, was checked through the
author-uploaded full-text page.  Its publisher PDF endpoint returned an HTML
access page and the author-upload PDF endpoint returned 403, so no PDF hash is
claimed and no statement unique to that paper is load-bearing here.  Its degree
remarks refer back to the hashed 1993 estimate.

Classical facts used without a new source claim: projection formula; Bezout;
Riemann--Hurwitz; Euler additivity; generic-line surjectivity for an affine plane
curve complement; and the fact that a polynomial automorphism is a proper target
isomorphism.  All arithmetic in (3.3)--(3.5) and (5.2) is displayed.

<!-- BODY-END -->
