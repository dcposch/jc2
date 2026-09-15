# An elliptic branch curve excludes the specified Pinchuk donor

Producer: swarmHQ ROOT (gpt-6-astra).
Date: September15,2026. Basis2953627637c67e7d78d8af13f2f578f478de6af5.
Evidence: MANUAL exact algebra and BOOK-relative source attachment.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED; different-model review required.
No novelty claim. This is a donor exclusion, not a proof of JC2.

## Exact object and claim

Let \(f,h\) be algebraically independent over \(\mathbb C\), put \(p=f+h\),
and work in \(K=\mathbb C(f,h)=\mathbb C(p,h)\). Set
\[
\begin{aligned}
q={}&-\frac{h^4(h+1)^2}{f^2}
 +\frac{h^3(h+1)(6h+8)}{f}
 -h^2(6h+7)\\
&-170fh-91h^2-195fh^2-69h^3-75fh^3-\frac{75}{4}h^4.
\end{aligned}
\]
These rational coordinates are the specific complexified Pinchuk
presentation in [Campbell1202.2949v4, Sections2.1--2.2](https://arxiv.org/html/1202.2949v4).
The real map's positive, nonconstant Jacobian is not a complex Keller
condition. We use the displayed algebraic formula, not real fiber counts
or a transfer of the real function-field argument to \(\mathbb C\).

**Claim.** The normalization of \(\mathbb C[p,q]\) in \(K\) has an
irreducible ramification divisor whose image has smooth projective
normalization of genus one. Consequently there is no \(\mathbb C\)-field
embedding \(K\hookrightarrow\mathbb C(x,y)\) sending \(p,q\) to polynomials
with nonzero constant Jacobian on the whole plane.

The embedding is allowed to have arbitrary finite degree; it need not
be birational. The claim fixes these two target elements \(p,q\). It does
not exclude changing the target algebra before substitution, other rational
donors, or arbitrary real nonsingular maps.

## 1. A genuine chart of the finite normalization

At fixed \(p\), substitute \(f=p-h\). As a rational function of \(h\),
\(q=N(p,h)/(p-h)^2\), with numerator of degree six and leading coefficient
\(197/4\). The value of the numerator at \(h=p\) is
\(-p^4(p+1)^2\), nonzero over \(\mathbb C(p)\). Hence the rational map
has degree six:
\[
[K:\mathbb C(p,q)]=6.
\]
Clearing denominators gives a polynomial equation for \(h\) over
\(A=\mathbb C[p,q]\) with constant nonzero leading coefficient. Thus \(h\),
and also \(f=p-h\), are integral over \(A\).

Let \(B\) be the normalization of \(A\) in \(K\).
After inverting the SOURCE element \(f\),
\[
A[h]_f=\mathbb C[f,f^{-1},h].
\]
This ring is normal, so \(B_f=A[h]_f\). In particular, a ramification
curve found in this chart is a divisor of the actual finite normalization,
not a ramification artifact of an arbitrary rational model.

## 2. The critical curve has genus one

Set
\[
r=\frac{h(f-h(h+1))}{f^2},\qquad \alpha=13+15h.
\]
Differentiating \(q(p,h)\) at fixed \(p\) gives the rational identity
\[
\left.\frac{\partial q}{\partial h}\right|_p
 =-f\bigl(r^2+(r+\alpha)^2+1\bigr).
\tag{1}
\]
It can be checked directly from the displayed formula using
\(\partial_h f|_p=-1\). Equivalently, in the original source coordinates
one has \(df\wedge dh=-f\,dx\wedge dy\), and the Pinchuk Jacobian is
\(f^2(r^2+(r+\alpha)^2+1)\). Identity(1), rather than positivity over
the reals, is the relevant algebra.

The critical curve on \(f\ne0\) therefore maps to the smooth projective
conic
\[
C_0:\quad r^2+(r+\alpha)^2+1=0.
\]
On its function field \(h=(\alpha-13)/15\), and \(u=f/h\) satisfies
\[
r u^2-u+(h+1)=0,\qquad
\Delta=1-4r(h+1)=1-\frac4{15}r(\alpha+2).
\tag{2}
\]
The omitted \(h=0\) points are not whole components: at \(h=0,f\ne0\),
the right side of(1) is \(-170f\ne0\).

The conic has two points at infinity. At each, both \(r,\alpha\) have
simple poles and nonzero leading coefficients, so \(\Delta\) has a pole
of order two. Its finite zeros have \(\alpha\ne-2\); substitute
\(r=15/(4(\alpha+2))\) into the conic. Their \(\alpha\)-coordinates satisfy
\[
8\alpha^4+32\alpha^3+100\alpha^2+152\alpha+257=0.
\]
With \(w=\alpha+1\), this is
\[
8w^4+52w^2+16w+181=0.
\tag{3}
\]
This quartic is squarefree over \(\mathbb C\). Here is a small exact
certificate, requiring no computer algebra. Modulo7 it becomes
\(H=w^4+3w^2+2w+6\). Euclidean division with
\(H'=4w^3+6w+2\) gives a nonzero scalar multiple of
\(w^2+w+4\); reducing \(H'\) by this quadratic gives \(w+4\).
At \(w=-4=3\), the quadratic is \(2\ne0\) in \(\mathbb F_7\).
Thus the resultant is nonzero modulo7 and hence in characteristic zero.
No leading degree is lost. The parametrization by \(\alpha\) on
\(\Delta=0\) shows that the four intersections are simple.

Consequently \(\Delta\) has four simple zeros and two double poles on
\(C_0\simeq\mathbb P^1\). It is not a square in its function field.
Equation(2) defines an irreducible double cover ramified at exactly the
four zeros. Riemann--Hurwitz gives
\[
2g-2=2(-2)+4=0,\qquad g=1.
\]
This is the smooth projective normalization of the critical curve.
It remains to show that its branch IMAGE has the same genus: that step
cannot be inferred merely from the genus of a source divisor.

## 3. The critical curve maps birationally to its image

We prove that for generic \(p\) the six finite critical points of
\(h\mapsto q(p,h)\) are simple and have pairwise distinct critical values.
This proves generic injectivity of the critical curve's map to \((p,q)\).

### Two critical points away from the degeneration

At \(p=0\),
\[
q(0,h)=h^2(ah^2+bh+c),\qquad
a=197/4,\quad b=104,\quad c=63.
\]
The two nonzero critical points are the roots of
\[
197h^2+312h+126=0.
\]
They are distinct since \(312^2-4\cdot197\cdot126=-1944\ne0\).
Their values are nonzero: a nonzero multiple root of
\(h^2(ah^2+bh+c)\) would require \(b^2-4ac=-1595=0\).
Their critical values are also different. Reducing \(ah^4+bh^3+ch^2\)
modulo \(4ah^2+3bh+2c\), the coefficient of \(h\) is
\[
\frac{b(9b^2-32ac)}{64a^2},
\qquad 9b^2-32ac=-1944\ne0.
\]
The two simple critical points therefore persist for small \(p\), with
different nonzero limiting values.

### Four critical points near \(h=0\)

Write \(h=pw\). Away from \(w=1\), the exact rational formula has expansion
\[
q(p,pw)=p^2\bigl(S(w)+O(p)\bigr),
\quad
S(w)=\frac{63w^4-306w^3+412w^2-170w}{(1-w)^2}.
\]
This is a formal or analytic expansion of rational functions with regular
coefficients near the points used below, not an assumed algebraization.
With \(v=w-1\),
\[
S=63v^2-54v-128-\frac{12}{v}-\frac1{v^2},\qquad
\frac{v^3}{2}S'=63v^4-27v^3+6v+1.
\tag{4}
\]
The four finite critical points of \(S\) are simple, nonzero in \(v\),
and have distinct values. An exact modulo5 certificate suffices:
\[
63v^4-27v^3+6v+1
\equiv(v+1)(3v^3+1).
\]
The cubic condition is \(v^3=3\); it has root \(v=2\) and the two
roots of \(v^2+2v+4\). That quadratic has nonsquare discriminant3 in
\(\mathbb F_5\), so these four critical points are distinct and nonzero.
The reduced rational function is
\[
\bar S=3v^2+v+2+3/v+4/v^2.
\]
At \(v=-1\) its value is0. On \(v^3=3\) it reduces to
\(4v^2+4v+2\), whose value at2 is1. On the remaining quadratic it is
\(v+1\): two distinct values outside \(\mathbb F_5\), hence different
from0 and1. Thus the four critical values are distinct.

All denominators at these reduced critical points are units, and the
critical polynomial keeps degree four. This verifies a nonzero
discriminant/resultant condition over \(\mathbb Z\), so proves the
corresponding characteristic-zero statement. It is not a modular
counterexample search or an inference of polynomial lifting.

The simple roots in(4) give four branches \(h=pw_i(p)\) of the original
critical equation. Their values have distinct leading coefficients
\(p^2 S(w_i(0))\), so are pairwise different, and tend to0. They are
therefore also different from the two nonzero limiting values above.
After multiplication by \((p-h)^3\), the original \(q_h\) has a
degree-six numerator, with nonzero leading coefficient-197. We have
accounted for six simple roots for small generic \(p\); they are all
the finite critical points.

The critical curve is irreducible by Section2. Pairwise distinct values
for generic \(p\) now show that it is birational to its irreducible image
\(D\subset\mathbb A^2_{p,q}\). Thus the smooth projective normalization
of \(D\) has genus one. In particular, its affine normalization is not
\(\mathbb A^1\). The critical divisor lies in the chart of Section1
generically and is a genuine ramification divisor over this image.
The generic critical points are simple, so the ramification index is two.

## 4. Exclusion of arbitrary dominant source substitutions

Suppose \(K\hookrightarrow L=\mathbb C(x,y)\) sends \(p,q\) to a
polynomial Keller pair. Let \(N\) be the normalization of \(A\) in \(L\).
The extension \(L/K\) is finite, of unrestricted degree.
Extend the ramified valuation above \(D\) from \(K\) to \(L\).
Ramification indices multiply, so it is still ramified over \(D\).

The whole-plane étale source embeds as an open in its finite
normalization. It misses that ramified divisor; consequently \(D\)
is an irreducible component of the polynomial map's nonproperness set.
The accepted polynomial-parametrization theorem for nonproperness
components forces its normalization to be \(\mathbb A^1\), contradicting
Section3.

This is the same reviewed transfer used in Section4 of the
[Laurent-polynomial donor filter](laurent-polynomial-donor-swarmHQ-root-20260915.md),
with the same normalization/ramification hypotheses and its
Jelonek--Lason polynomial-coverage import. Here the obstruction is
genus one, not a critical-value pole or a torsion divisor class.
No arbitrary rational surface or merely birational model replaces the
literal finite-normalization chart checked in Section1.

## Checks, exclusions and dependencies

- Identity(1) specializes at \(p=0,f=-h\) to
  \(q_h=h(197h^2+312h+126)\), agreeing with the direct derivative.
- Both elementary prime certificates retain leading degree, check
  denominators, and certify only nonvanishing conditions used in the
  characteristic-zero argument. No machine arithmetic was executed.
- Genus of the critical source alone would not exclude a donor: its image
  might be rational. Section3's six distinct values is indispensable.
- The birational-substitution case also meets the classical rational-
  component obstruction; the statement here allows arbitrary finite
  substitution degree, so that observation alone is insufficient.
- This does not change the real Pinchuk theorem or the earlier real Nash
  rectification control. It does not exclude all multipole rational donors,
  all Pinchuk-like formulas, or changes of target algebra.
- Existing degree bounds are neither used as search caps nor reverified.
  This single donor calculation earns no parameter farm, relaxed control
  family or automatic successor.

Primary read: Campbell1202.2949v4, version dated January18,2013; the
introduction, Section2.1 and Section2.2 through Corollary6 were read,
including the displayed rational formulas. No whole37-page audit is claimed.
The explicit degree-six rational map calculation above makes a separate
complex-field justification; no real fiber-count argument is transplanted.
The branch, Riemann--Hurwitz and nonproperness imports retain MANUAL/
BOOK-relative scope. Prior canonical searches were targeted, not exhaustive.

Native Astra co-check completed2026-09-15 14:35:48 UTC and was terminally
collected before14:38:09. It independently checked the literal algebra,
degree, conic cover, both prime certificates, six distinct critical values,
normalization chart and source-substitution obstruction, finding no gap.
It wholly read the accepted Laurent donor report (SHA256
0dbb34f986d8747c7dde8ea74e930de8b9b8e1417653e73ad0749d5075ccca0a),
but did not independently retrieve Campbell. This is same-model co-research,
NOT different-model FIRST. Different-model hostile review remains required.
Author mathematical completion:2026-09-15 14:38:24 UTC, before the original
14:40 cap. No scientific execution, parameter search or successor occurred.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

The canonical scanner completed exit0 before14:38:09. This empty identifier
result is not a novelty or mathematical correctness certificate. Targeted
Pinchuk/elliptic-branch history searches found no exact prior test; they do
not establish exhaustive coverage. The retained Laurent donor exclusion
does not cover this rational-in-h multipole presentation, and real Nash
rectification does not produce a whole-plane complex polynomial Keller pair.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12468`.
- Body SHA-256:
  `7e9d9cdccc824997a0456ee5abd72830e9ef8e1ed0559f2d8b6f1b5a5a6a98c4`.
- Frozen basis: `2953627637c67e7d78d8af13f2f578f478de6af5`.
