# B0-ALL-N: eta-criticality at every degree

## 0. Scope, custody, and verdict

The three frozen inputs were hashed before they were read. In the order in the charge, SHA-256 returned:

~~~text
67a9482eecd3fcb5f06bcf2967d4b73f5761429b5be597f2809b8e0767b1b02c
b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55
bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963
~~~

All three match. Below, **N5**, **B0**, and **Coord** denote, respectively:

- corr-budget-n5-sol56-20260831.md;
- b0-trivial-dicritical-proof-opus5-20260831.md;
- block-descent-a1-b0-coordinator-integration-fable5-20260831.md.

**Verdict.** The proposed theorem B0-H2-ALL-N does not follow at all degrees from the promoted eta-criticality mechanism. The exact escape is ramification of a nonprimitive intermediate cover, not a multiple-point ambiguity.

The sharp result proved here is:

> If \(A_F=D\) is irreducible and a dicritical has \(\mu=1\), then
> \(\widetilde D\simeq\mathbb A^1\), that dicritical maps isomorphically to
> \(\widetilde D\), and the normalization map
> \(\eta:\widetilde D\to D\) is immersive everywhere. Every correction,
> after passage to the parametrization point supplied by [Z-6.5(b)], is
> therefore ramification of a cover
> \(h_l:\mathbb A^1\to\mathbb A^1\) with \(\mu_l\ge2\) and \(s_l\ge2\).
> Moreover the generic affine-fibre count \(a\) satisfies \(2a>N\), and the
> local correction excess forces \(N\ge20\).

Thus this packet proves B0 under H2 for every \(N\le19\), and at every degree
if all correction-bearing normalization covers have degree one. The
all-degree remainder is
**OPEN[B0-H2-N>=20/RAMIFIED-NONPRIMITIVE-COVER]**.

This is a typed obstruction, not an attainment claim or a new exit-price assertion.

## 1. Promoted licenses and primary-source scope

Let \(l\) be an affine-image dicritical,
\(\phi_l:l'\to D_l\), \(s_l=\deg\phi_l\), and

\[
 \operatorname{corr}_l=
 \sum_x(\mu_x-\mu_l)\ge0.
\]

These are the definitions at **B0:38--50**. The exact Orevkov budget is

\[
 \sum_l(\mu_l+\operatorname{corr}_l)=N-1.                         \tag{1.1}
\]

See **B0:63--65**. The coordinator promotes the branch-locus and normalization package and, under H2, strictness

\[
 A_F\text{ irreducible}\quad\Longrightarrow\quad
 \sum_l\mu_l\le N-2,\qquad
 \sum_l\operatorname{corr}_l\ge1.                                \tag{1.2}
\]

See **Coord:24--48**. Under H2 every \(D_l\) is the same curve \(D=A_F\), as used explicitly at **B0:302--310**. At a generic point of \(D\), promoted flatness gives

\[
 a+\sum_l s_l\mu_l=N,\qquad a\ge1.                               \tag{1.3}
\]

This is **B0:182--188,200--211**, promoted at **Coord:34--38**.

The pointwise implications must retain their exact directions. [O-5.2] says that no jump implies a nonsingular local embedding (**B0:66--70**). Its contrapositive is “non-embedding implies a jump,” not the direction needed in Step 3. The required equivalence is [Z-6.5(b)]:

\[
 \mu_x>\mu_l\quad\Longleftrightarrow\quad d\phi_l(x)=0,
 \qquad
 \mu_l=1\quad\Longrightarrow\quad d\phi_l\ne0
 \text{ everywhere}.                                            \tag{1.4}
\]

Here “singular point of the immersed curve” means criticality of that parametrization; intersections of smooth local components are expressly not counted. This is the binding correction at **Coord:43--45,108--116**, also explained at **N5:55--64**. In particular, (1.4) does not say that the reduced image germ is unibranch or singular.

Two primary PDFs were checked directly and rehashed:

- S. Yu. Orevkov, “On three-sheeted polynomial mappings of \(\mathbb C^2\),”
  DOI 10.1070/IM1987v029n03ABEH000984, refs/jc86.pdf, SHA-256
  f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db.
  Lemma 2.1 is on PDF pp. 2--4; the local normal form, multiplicity
  definition, and constant-multiplicity equation used in §4 are on pp. 4--7;
  Lemma 5.2 is on pp. 8--9.
- H. Żołądek, “An application of Newton--Puiseux charts to the Jacobian problem,”
  DOI 10.1016/j.top.2008.04.001, refs/zoladek2008_official.pdf, SHA-256
  88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad.
  Proposition 6.5(b) and its definition of immersed-curve singularity are on
  printed pp. 457--458 / PDF pp. 27--28.

Orevkov Lemma 2.1 is independent of \(N\): every connected finite-image boundary chain has one \(L_F\)-component \(l\simeq\mathbb P^1\), meeting \(L_\infty\) at exactly one point. Hence

\[
 l'=l\cap\Phi^{-1}(\mathbb A^2)
 \simeq\mathbb P^1-\{\infty\}
 \simeq\mathbb A^1.                                              \tag{1.5}
\]

This is the primary-source affine-line repair consumed at **Coord:56--66**; **N5:81--91,164--179** uses the same lemma and the finite normalization factorization. I use (1.5) at its primary-source, all-degree scope, not by extrapolating the \(N=5\) values \(s_l=1\).

## 2. Global normalization factorization and the trivial dicritical

Write \(A=\mathbb C[D]\), let \(\overline A\) be its normalization in \(K(D)\), and use \(\mathbb C[l']=\mathbb C[t]\) from (1.5). Dominance of \(\phi_l\) embeds \(K(D)\) in \(\mathbb C(t)\). If \(u\in\overline A\), its image is integral over \(A\subset\mathbb C[t]\), hence integral over \(\mathbb C[t]\); since \(\mathbb C[t]\) is integrally closed in \(\mathbb C(t)\), that image belongs to \(\mathbb C[t]\). The normalization universal property therefore gives a unique global factorization

\[
 \phi_l=\eta\circ h_l,\qquad
 h_l:l'\longrightarrow\widetilde D.                              \tag{2.1}
\]

This factorization is defined at every source point, including those mapping to \(\operatorname{Sing}D\): \(h_l(x)\) is the particular normalization place selected by the source germ, not the physical target point.

Choose a target coordinate whose pullback to \(\mathbb A^1\) is a nonconstant polynomial \(f(t)\). Then \(\mathbb C[t]\) is finite over \(\mathbb C[f(t)]\). Since
\(\mathbb C[f(t)]\subset\overline A\subset\mathbb C[t]\), the same finite module generators work over \(\overline A\). Thus \(h_l\) is finite. It is dominant, so its closed image is all of \(\widetilde D\), and

\[
 \deg h_l=[\mathbb C(t):K(D)]=s_l.                               \tag{2.2}
\]

This proves the precise finite, surjective, degree-\(s_l\) license used without proof at **B0:236--243** and in the degree-one instance **N5:81--91**.

Now suppose \(\mu_0=1\). By (1.4),
\(\operatorname{corr}_0=0\) and \(d\phi_0(x)\ne0\) for every \(x\in l'_0\). The chain rule

\[
 d\phi_0(x)=d\eta_{h_0(x)}\circ dh_0(x)                          \tag{2.3}
\]

forces both \(dh_0(x)\ne0\) and \(d\eta_{h_0(x)}\ne0\). Since \(h_0\) is surjective, \(\eta\) is immersive at every normalization point, including every point over \(\operatorname{Sing}D\). Also \(h_0\) is a connected finite étale cover of degree \(s_0\).

In fact H3 is not needed. By (1.5), the source of \(h_0\) is \(\mathbb A^1\). Extend \(h_0\) to smooth projective completions

\[
 \overline h_0:\mathbb P^1\longrightarrow\overline D.
\]

The point at infinity must map to the boundary of \(\widetilde D\); otherwise the nonconstant projective map would land in an affine curve. Every boundary point has a preimage under the surjective projective extension, and no finite source point maps to the boundary. Since the source has only one omitted point, \(\overline D-\widetilde D\) is one point and its full preimage is \(\{\infty\}\).

Riemann--Hurwitz first forces \(\overline D\simeq\mathbb P^1\). All ramification of \(\overline h_0\) would then be at infinity, with contribution \(s_0-1\), whereas Riemann--Hurwitz requires total ramification \(2s_0-2\). Therefore \(s_0=1\), \(h_0\) is an isomorphism, and

\[
 \widetilde D\simeq\mathbb A^1.                                 \tag{2.4}
\]

If Orevkov Lemma 2.1 were deliberately withheld, the safe conclusion without H3 would stop at a connected finite étale cover \(h_0\); H3 would then trivialize it. At the actual licensed scope, (1.5) proves (2.4), so existence of a trivial dicritical itself forces H3.

## 3. What a correction point really forces

By (1.2), some correction summand is positive. A correction is recorded at a point of Orevkov's collapsed physical model, whereas \(h_l\) is a map from the normal parametrizing curve. These are not identified. Pass instead to the parametrization point \(\widehat x\in l'\) associated to that summand by pointwise [Z-6.5(b)], and set \(z=h_l(\widehat x)\). Then

\[
 0=d\phi_l(\widehat x)
   =d\eta_z\circ dh_l(\widehat x).                               \tag{3.1}
\]

Section 2 proves \(d\eta_z\ne0\) at every \(z\). Hence

\[
 dh_l(\widehat x)=0.                                             \tag{3.2}
\]

This is the opposite of the proposed eta-criticality conclusion: criticality is forced into the intermediate cover. Conversely, at any lifted parametrization point where \(dh_l=0\), (2.3) makes \(d\phi_l=0\), and [Z-6.5(b)] gives a jump. Thus, at the parametrization-point level licensed by [Z], correction support is exactly ramification support of \(h_l\). Every correction-bearing \(h_l\) therefore has \(s_l\ge2\). It also has \(\mu_l\ge2\), because \(\mu_l=1\) makes its parametrization immersive everywhere.

The image-germ alternatives are exact. A reduced branch of \(D\) at \(p\) is singular precisely when \(d\eta_z=0\) at its normalization place. That alternative has been excluded. Every branch of \(D\) is consequently smooth, and every singular point of \(D\) is multibranch; tangent smooth branches are allowed. This reconciles promoted Lemma 3.3 (**B0:219--225**): zero correction implies a smooth branch, but the converse “correction implies a singular reduced branch” was never promoted.

Nor does a multiple point itself explain (3.1). If \(h_l\) is unramified at a place over a multiple point, the selected branch parametrization is immersive and there is no jump. If \(h_l\) ramifies there, the jump comes from \(h_l\). A correction image need not even be a reduced singular point: locally, \(\eta(u)\) may parametrize a smooth branch while \(h_l(t)=u_0+t^e\), \(e\ge2\). Then \(\eta\circ h_l\) is critical although its reduced image is smooth. This is precisely the nonprimitive loophole warned of at **N5:60--64**; it is a diagnostic germ, not a Keller-map witness.

## 4. The sharp theorem supported by the mechanism

> **Theorem 4.1 (eta/cover obstruction under H2).** Let \(F\) be a
> noninvertible plane Keller map of geometric degree \(N\), and assume
> \(D=A_F\) is irreducible. If an affine-image dicritical has \(\mu_0=1\),
> then:
>
> 1. \(s_0=1\), \(h_0:l'_0\overset{\sim}{\longrightarrow}\widetilde D\),
>    and \(\widetilde D\simeq\mathbb A^1\); H3 follows rather than being an
>    extra hypothesis.
> 2. The normalization map \(\eta\) is immersive everywhere. All reduced
>    branches of \(D\) are smooth and all singularities of \(D\) are
>    multibranch.
> 3. Some other dicritical has \(\mu_l\ge2\), \(s_l\ge2\), and a correction.
>    Every correction is supported, after the [Z] point lift, on ramification
>    of its polynomial cover \(h_l:\mathbb A^1\to\mathbb A^1\).
> 4. The generic affine-fibre count satisfies \(2a>N\), and \(N\ge20\).
>
> Consequently no \(\mu=1\) dicritical exists for \(N\le19\), or at any
> degree if every correction-bearing \(h_l\) has degree one.

Parts 1--3 were proved in §§2--3. For part 4, put

\[
 \Sigma=\operatorname{Sing}D,\qquad
 \sigma=|\Sigma|,\qquad
 \nu=\sum_{p\in\Sigma}(|\eta^{-1}(p)|-1),\qquad
 A_\Sigma=\sum_{p\in\Sigma}a_p.
\]

The irreducible curve \(D\) is singular by promoted Corollary 3.6 (**Coord:39--43**), so \(\sigma\ge1\). Since all branches are smooth, every singularity is multibranch and \(\nu\ge\sigma\). From \(\widetilde D\simeq\mathbb A^1\),

\[
 \chi_c(D-\Sigma)=1-\sigma-\nu.
\]

The promoted irreducible Euler identity, re-derived at **B0:236--265** and stated at **N5:181--188**, is

\[
 (N-a)\chi_c(D-\Sigma)=N-1-N\sigma+A_\Sigma.
\]

Substitution and regrouping give

\[
 0=(a-1)+(N-2a)\sigma+(N-a)(\nu-\sigma)+A_\Sigma.                \tag{4.1}
\]

If \(2a\le N\), all four terms are nonnegative. Since \(N\ge3\) in the noninvertible scope and \(\sigma\ge1\), either the second term is positive or, when \(N=2a\), \(a-1>0\). This contradicts (4.1), so \(2a>N\).

It remains to use the local multiplicities hidden by the coarse correction
sum. Put

\[
 W=N-a=\sum_l s_l\mu_l,\qquad d=a-W=2a-N>0.                     \tag{4.2}
\]

The trivial dicritical contributes one to \(W\), and a correction carrier has
\(\mu_l,s_l\ge2\), so \(W\ge5\).

For \(t\in l'\), let \(e_t\) be the local degree of \(h_l\), let
\(M_t=\mu_{\pi(t)}f^*\) be Orevkov's local surface multiplicity, and set

\[
 k_t=M_t-e_t\mu_l.
\]

Here the notation does not merge a place with a physical point. Orevkov
Lemma 2.1 says that each component of \(L_{FC}\) is a linear chain with one
\(L_F\)-endpoint; contraction of its \(L_C\)-part lands at the unique
attachment point on \(\pi(l)\). Thus \(\pi|_{l'}\) does not identify distinct
finite points, different chains meet only in \(L_\infty\), and there are no
extra finite \(L_C\)-fibre points.

We claim

\[
 M_t\ge e_t\mu_l,\qquad k_t\ge0.                                \tag{4.3}
\]

Indeed, deform \(h_l(t)\) to a nearby regular normalization place. Its
\(e_t\) nearby inverse points on \(l'\) are distinct and can be chosen away
from the finite correction set. At each, Orevkov Lemma 3.1 gives the generic
local normal form with \(\mu_l\) transverse sheets. A nearby off-branch target
therefore has \(e_t\mu_l\) inverse points, in disjoint neighborhoods all
contained in any fixed neighborhood of \(\pi(t)\). Orevkov's definition of
local multiplicity in §4 gives (4.3). This uses the hashed PDF pp. 4--7, not a
new promoted assertion.

Because \(\eta\) is immersive, §3 says that the correction points are exactly
the critical points of \(h_l\). Since
\(h_l:\mathbb A^1\to\mathbb A^1\) is a degree-\(s_l\) polynomial,
\(\sum_t(e_t-1)=s_l-1\). Consequently

\[
 \operatorname{corr}_l
 =\mu_l(s_l-1)+\sum_t k_t.                                      \tag{4.4}
\]

The sums here are over the finite critical points (equivalently over all
finite \(t\), with zero summands off that set).

For \(p\in D\), put \(r_p=|\eta^{-1}(p)|\) and let \(K_p\) be the sum of the
\(k_t\)'s over all \(t\) whose selected normalization place lies over \(p\).
For each such place, \(\sum_{h_l(t)=z}e_t=s_l\). The point separation just
proved and Orevkov's constant-multiplicity equation therefore give the exact
physical-fibre identity

\[
 a_p+r_pW+K_p=N.                                                \tag{4.5}
\]

At a singular point \(r_p\ge2\), hence \(K_p\le N-2W=d\). Also (4.5) gives

\[
 A_\Sigma=a\sigma-W\nu-\sum_{p\in\Sigma}K_p.
\]

Substitution in (4.1), using \(N-a=W\), yields

\[
 \sum_{p\in\Sigma}K_p=a-1.                                     \tag{4.6}
\]

Let \(R=\sum_l(s_l-1)\), the total finite ramification multiplicity of the
polynomial covers. A singular image with \(K_p>0\) contains a critical
point of some \(h_l\); the number of such images is at most \(R\). Equations
(4.5)--(4.6) imply

\[
 a-1\le dR.                                                     \tag{4.7}
\]

If \(b\ge1\) is the number of \(\mu=1\) dicriticals and \(q\ge1\) the number
with \(\mu\ge2\), every former has \(s_l=1\), while

\[
 W\ge b+2\sum_{\mu_l\ge2}s_l,\qquad
 2R\le W-b-2q\le W-3.
\]

Thus \(R\le\lfloor(W-3)/2\rfloor\). Writing \(a=W+d\), (4.7) becomes

\[
 W+d-1\le d\left\lfloor\frac{W-3}{2}\right\rfloor,\qquad
 N=2W+d.                                                       \tag{4.8}
\]

For \(W=5,6\), (4.8) is impossible. For \(W=7\) it forces \(d\ge6\), giving
\(N\ge20\); \(W=8\) gives \(N\ge23\), \(W=9\) gives \(N\ge22\), and
\(W\ge10\) already gives \(N\ge21\). Hence \(N\ge20\). The conditional
degree-one assertion follows directly from §3 and strictness. This proves
Theorem 4.1.

\[
 \boxed{N\ge20}.
\]

The first possible aggregate stratum is now forced. Equality \(N=20\) in
(4.8) gives \(W=7\), \(d=6\), \(a=13\), and \(R=2\). Equality in the bounds
for \(R\) leaves exactly

\[
 (\mu,s,\operatorname{corr})=(1,1,0)+(2,3,16).                  \tag{4.9}
\]

Moreover equality in (4.6)--(4.7) forces the cubic \(h_l\) to have two
distinct simple critical points. Each maps to a two-branch singular point,
has \(k_t=6\), \(M_t=2\cdot2+6=10\), and contributes correction \(8\);
(4.5) gives \(a_p=0\) at both images. Additional singularities with \(K_p=0\)
are not excluded. Packet (4.9) is necessary only: it is not an attainment
claim or a Keller example. Excluding this ramified-cubic, multibranch packet
is the first OPEN left by the mechanism.

## 5. Consequences and remaining gaps

### 5.1 Irreducible \(A_F\)

At \(N=5\), **Coord:69--74** promotes the sole H2 profile containing a trivial dicritical:

\[
 (\mu,\operatorname{corr})=(2,1)+(1,0),\qquad
 (s_2,s_1,a)=(1,1,2).
\]

Both \(h\)'s have degree one, so the correction cannot be absorbed in a cover. This is exactly the common-normalization contradiction at **N5:252--318**. Theorem 4.1 recovers it and excludes every H2 trivial profile through \(N=19\). Together with the promoted \(N=4\) theorem (**Coord:49--55**),

\[
 \boxed{\text{H2 implies no trivial dicritical for every }N\le19.}
\]

In campaign notation this gives \(b=0\) in that range, with no H3 hypothesis. H3 is needed only for the separate printed rank-four (M) bookkeeping (**Coord:52--54,117--118**); in the present hypothetical case H3 already follows from Theorem 4.1.

The promoted general estimate is

\[
 2m_{\mathrm{nt}}+m_{\mathrm{triv}}
 \le\sum_l\mu_l\le N-2                                         \tag{5.1}
\]

under H2 (**Coord:67--68; B0:487--491**). Hence for \(N\le19\), or conditionally at all \(N\) if B0-H2-ALL-N is later closed,

\[
 2m\le\sum_l\mu_l\le N-2,                                      \tag{5.2}
\]

one unit stronger than \(2m\le N-1\). Without H2, the exact budget (1.1) shows that the separate hypothesis \(b=0\) implies \(2m\le N-1\). An H2-only B0 theorem cannot make that bound unconditional; the reducible cases must also be closed.

### 5.2 Reducible \(A_F\)

At \(N=4\), the exact remaining configuration is the coordinator's repair, not printed Theorem 4.3(5), which **Coord:56--66,108--111** refutes. There are two dicriticals over distinct components,

\[
 (\mu,\operatorname{corr},s)=(2,0,1),(1,0,1).
\]

Here \(a_{D_1}=2\), \(a_{D_0}=3\), both target normalizations are
\(\mathbb A^1\), and the branch locus is \(D_1\). The component \(D_1\) is a
singular polynomial curve whose affine singularities are double points of two
smooth branches; \(\operatorname{Sing}D_1\cap D_0=\varnothing\), and
\(a_p=0\) at each such singularity. Its complement must surject onto \(S_4\),
with all meridians transpositions and the two local meridians at every double
point disjoint. This is exactly OPEN[PI1-S4] at **Coord:84--106**; a negative
answer closes B0 at \(N=4\) without H2.

There is no promoted single PI1-\(S_N\) analogue for \(N\ge5\). The honest remainder is:

> **OPEN[B0-REDUCIBLE-N>=5/COMPONENT-INCIDENCE+RAMIFIED-COVERS].**
> Exclude all reducible-\(A_F\) configurations containing at least one
> \((\mu,\operatorname{corr})=(1,0)\), at least one \(\mu\ge2\) dicritical,
> and satisfying
> \[
> \sum_l(\mu_l+\operatorname{corr}_l)=N-1,\qquad
> a_D+\sum_{l\to D}s_l\mu_l=N
> \]
> for every target component \(D\), together with the promoted meridian
> cycle-type and transitivity constraints.

The \(\mu\ge2\) component is required by branch-locus nonemptiness (**B0:190--211**), and \(\mu=N-1\) is excluded by promoted Corollary 3.8 (**Coord:46--48**). Different target components have different normalization maps. Moreover H2 strictness does not supply a correction on the component seen by a trivial dicritical. Thus the common-eta argument is only componentwise and need not meet any correction.

At \(N=5\), the reducible cost multisets are exactly

\[
 (2,1)+(1,0),\qquad
 (3,0)+(1,0),\qquad
 (2,0)+(1,0)+(1,0),                                             \tag{5.3}
\]

with target-component incidence and cover degrees still undetermined. The unique profile at **Coord:69--74** and its destruction in **N5** are H2-only; they do not classify or eliminate (5.3) in the reducible case. The PI1-S5-CORR paragraph at **N5:320--356** is explicitly counterfactual and is not the \(N\ge5\) reducible residual.

## 6. Fail-closed dependency audit

The five requested steps close as follows.

1. **Normalization/covering — CLOSED.** Equations (2.1)--(2.2) give the finite, surjective, degree-\(s_l\) factorization on all source points, including lifts over \(\operatorname{Sing}D\). No cv flag, physical quotient point, and normalization place is identified.
2. **Trivial dicritical — CLOSED, stronger than requested.** It makes \(h_0\) finite étale and \(\eta\) immersive everywhere. The all-degree primary-source statement \(l'_0\simeq\mathbb A^1\) then forces \(s_0=1\) and H3; H3 is not an additional assumption.
3. **Correction-to-eta transfer — REFUTED as stated.** [O-5.2]'s contrapositive cannot supply jump-to-criticality; [Z-6.5(b)] does. But [Z] makes the composite \(\eta\circ h_l\) critical. Since \(\eta\) is immersive, it forces \(dh_l=0\), not \(d\eta=0\). A multiple reduced point may remain, but is incidental; ramification of the nonprimitive cover is the exact escape.
4. **Assembly — PARTIAL, Theorem 4.1.** The mechanism closes H2 through
   \(N=19\) and whenever correction-bearing covers have degree one. It leaves
   OPEN[B0-H2-N>=20/RAMIFIED-NONPRIMITIVE-COVER], necessarily in the
   \(2a>N\) region and beginning with packet (4.9).
5. **Consequences — TYPED in §5.** The all-degree conclusions \(b=0\) under
   H2 and \(2m\le N-2\) remain conditional beyond degree nineteen. The
   unconditional \(2m\le N-1\) additionally requires the reducible gap.

A safe all-degree replacement would follow from any one of: every correction carrier has \(s_l=1\); a correction cannot arise solely from ramification of \(h_l\); or \(2a\le N\) under H2. None is promoted in the charged inputs.

No CAS or uncertain-duration computation was run. No canonical ledger or charged input was edited, and no part of jc2-lean was inspected.

<!-- BODY-END -->
