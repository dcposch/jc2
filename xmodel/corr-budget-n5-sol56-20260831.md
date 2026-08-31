# CORR-BUDGET-N5: the single correction point at \(N=5\)

## 0. Scope, method, and frozen-input verification

This lane addresses only the promoted \(N=5\) residual described in the
request.  It treats an assertion from either integration as available only
when that integration marks it promoted, and otherwise re-derives it from the
three frozen inputs or labels it `OPEN`.  No canonical ledger or charged file
was edited, and no part of `jc2-lean` was inspected.  The requested
`FALLACY-v2` distinctions (flag/place/series, floor/attainment, and typed
charging) are kept in force throughout.

Before any input was opened, `shasum -a 256` returned, in the order supplied,

```text
bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963
b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55
8ffc0a06edcf2be3908b1486da57e7d4a024973e679f9d25577cc281ef005320
```

These agree exactly with the three required hashes.  All subsequent line
references of the form `integration`, `proof`, or `review` refer respectively
to the frozen files named in the request.

## 1. Promoted premises and notation

Put \(D=A_F\).  H2 says that \(D\) is irreducible.  Thus the two
dicriticals in the promoted profile

\[
 (\mu,\operatorname{corr})=(2,1)+(1,0),\qquad
 (s_2,s_1,a)=(1,1,2)                                      \tag{1.1}
\]

dominate the **same** target curve \(D\); they are not two components of
\(A_F\).  This profile and these degrees are promoted at integration
69--74 (the competing correction on the \(\mu=1\) dicritical is excluded
there by [Z-6.5(b)]).

Three integers must not be conflated:

* \(\mu_2=2\) is the generic transverse ramification index of the surface
  map along the nontrivial dicritical;
* at the unique correction quotient point \(x\), \(\mu_x=3\) is the local
  multiplicity of the collapsed/finite **surface** map; and
* \(s_2=s_1=1\) is the degree with which either dicritical parametrizes
  the normalization of its image.

Orevkov's exact equality
\(\sum_l(\mu_l+\operatorname{corr}_l)=N-1\) makes the total correction one,
so there is exactly one such \(x\) and \(\mu_x-\mu_2=1\).  Corrections are
attached to points of \(\pi(l)\), not silently to a chosen flag or series
(proof 38--50, 63--65; review 66--71).

The promoted pointwise conclusions are these.  [O-5.2] says that
\(\mu_y=\mu_l\) makes the restricted parametrization a nonsingular local
embedding.  [Z-6.5(b)] says that a jump is equivalent to a critical point
of that parametrization, and also that \(\mu_l=1\) gives an immersive
parametrization everywhere (proof 66--77; review 73--93).  Contrary to a
premise in the question, [Z-6.5(b)] does **not** by itself say that the
whole reduced image germ is locally irreducible.  The hostile review
expressly refutes that gloss: a critical nonprimitive parametrization may
have smooth reduced image (review 235--244), and the integration makes
the corrected reading binding (integration 108--116).

For the Euler count, write

\[
 \widetilde D=\mathbf P^1\setminus\{c\text{ points}\},\quad
 \Sigma=\operatorname{Sing}D,\quad \sigma=|\Sigma|,\quad
 \nu=\sum_{p\in\Sigma}(r_p-1),\quad A=\sum_{p\in\Sigma}a_p,       \tag{1.2}
\]

where \(r_p=|\eta^{-1}(p)|\) for the normalization
\(\eta:\widetilde D\to D\), and \(a_p\) counts affine points in the
finite-model fibre.  The letter \(\sigma\), rather than \(s\), keeps the
number of singular points distinct from the covering degrees \(s_i\).

## 2. Local model at the correction point

Let \(\phi_i:l_i'\to D\) be the two restrictions.  They factor uniquely
through the normalization,

\[
 \phi_i=\eta\circ h_i,\qquad h_i:l_i'\longrightarrow\widetilde D.       \tag{2.1}
\]

Orevkov Lemma 2.1 makes each \(l_i'\) an affine line.  The maps \(h_i\)
are finite (equivalently, one can take the finite normalization
factorization used at proof 240--243), and \(\deg h_i=s_i=1\).  Hence
both \(h_i\) are isomorphisms.  In particular, the corrected
parametrization is primitive.  If \(z=h_2(x)\), [Z-6.5(b)] gives

\[
 d\phi_2(x)=0\quad\Longleftrightarrow\quad d\eta(z)=0.                 \tag{2.2}
\]

Thus the normalization branch marked by \(z\) is genuinely singular;
this removes the review's nonprimitive loophole.  It still does not say
that no other normalization branch passes through \(p=\eta(z)\), nor
does it identify a Puiseux pair.

### 2.1 What \(\mu_x=3\) does not determine

The correction \(\mu_x-\mu_2=1\) is not the multiplicity of the plane
branch and not the order of \(d\eta\).  The following hand-checked local
models show why a transverse degree-three slice is insufficient.  For
odd \(k\ge1\), set

\[
 G_k(u,v)=(X,Y)=\bigl(u,\ v^3-3u^k v\bigr).                           \tag{2.3}
\]

At the origin its local algebra is
\(\mathbf C\{u,v\}/(u,v^3)\), of length three.  Its critical curve is
\(v^2=u^k\); generically \(\partial^2Y/\partial v^2=6v\ne0\), so the
generic transverse index is two.  Normalizing the critical curve by
\((u,v)=(t^2,t^k)\) maps it to

\[
 (X,Y)=(t^2,-2t^{3k}),                                                \tag{2.4}
\]

of Puiseux type \((2,3k)\).  The smooth target disc \(X=0\), transverse
to its tangent, sees \(v\mapsto v^3\).  Consequently the ordinary cusp
\((2,3)\), \((2,9)\), \((2,15)\), and so on all have the same displayed
\((\mu_l,\mu_x)=(2,3)\) data.

Even multiplicity two is not forced when the finite source is merely
normal, which is the promoted scope.  Consider the finite flat triple
cover

\[
 W=\{z^3+xz+y^2=0\}\longrightarrow\mathbf C^2_{x,y}.                 \tag{2.5}
\]

It has local algebra \(\mathbf C\{z\}/(z^3)\) at the origin.  Its total
space is normal: the hypersurface is Cohen--Macaulay and its gradient
vanishes only at the origin.  Generic ramification is simple, while the
discriminant is

\[
 4x^3+27y^4=0,                                                        \tag{2.6}
\]

a \((3,4)\) branch.  More explicitly, its ramification curve is
\(x=-3z^2,\ y^2=2z^3\); the normalization
\((z,y)=(t^2,\sqrt2\,t^3)\) maps with degree one to
\((x,y)=(-3t^4,\sqrt2\,t^3)\).  These are diagnostic analytic germs,
not witnesses for a global Keller map; using them as attainment would
violate the floor/attainment guardrail.

If one adds the **unpromoted** hypotheses that the finite source and the
reduced ramification divisor are smooth at \(x\), a corank-one cubic can
be written after Weierstrass changes as
\((u,v)\mapsto(u,v^3+a(u)v)\).  Smoothness of
\(3v^2+a(u)=0\) forces \(\operatorname{ord}_0a=1\), and then the image is
the ordinary \((2,3)\) cusp.  Those extra hypotheses are precisely what
is missing here.  Therefore the safe isolated-germ status is
`OPEN[LOCAL-PUISEUX-N5]`: the promoted data force a critical primitive
normalization branch, but no specific Puiseux characteristic.  Against
the *complete* profile, §5 will show that the consistent list is empty.

## 3. Euler and aggregate accounting for the two components

The heading's “two components” can only mean the two source dicriticals.
Under H2 there is one target component, so the repaired \(N=4\)
two-target aggregate must not be copied componentwise.  The exact analogue
of its \(s_0=1,c_0=1\) repair is

\[
 s_2=s_1=1,\qquad l_2'\simeq l_1'\simeq\widetilde D\simeq\mathbf A^1,
 \qquad c=1.                                                          \tag{3.1}
\]

Indeed, Orevkov Lemma 2.1 gives \(l_i'\simeq\mathbf A^1\), and either
degree-one finite map \(h_i\) in (2.1) identifies it with the one common
normalization.  This is the same primary-source affine-line repair used
in review 321--337, now applied to the promoted degrees (1.1).

The promoted irreducible Euler calculation (proof 236--265, with the
equality repair at review 181--212) is

\[
 \chi_c(D-\Sigma)=2-c-\nu-\sigma,
 \qquad
 (N-a)\chi_c(D-\Sigma)=N-1-N\sigma+A.                                \tag{3.2}
\]

Putting \((N,a)=(5,2)\) gives

\[
 3c+3\nu-2\sigma+A=2.                                                 \tag{3.3}
\]

With (3.1), this becomes the exact \(N=5\) aggregate

\[
 3\nu+A=2\sigma-1.                                                    \tag{3.4}
\]

### 3.1 Pointwise fibre equation and the correction contribution

Let \(p_*=\phi_2(x)\), and put \(\iota_p=1\) for \(p=p_*\), zero
otherwise.  Let \(B_i\) denote the finite-model boundary prime
corresponding to \(l_i\).  Local degree is additive over branches
specializing to one physical fibre point.  Hence two distinct
normalization places of \(B_1\) could coalesce only with local
multiplicity at least two, contradicting
\(\operatorname{corr}_1=0\); two places of \(B_2\) would give at least
four, contradicting its total correction one.  A cross-dicritical
collision would give at least \(1+2=3\), and in particular a positive
correction on \(B_1\).  Thus all these physical points are distinct.
For every normalization place over \(p\), \(l_1'\) therefore supplies one
boundary point of local multiplicity one and \(l_2'\) one of local
multiplicity two, except that the marked \(l_2'\)-point has multiplicity
three.  There are no separate \(L_C\) “epsilon” points in the repaired
finite model; the contrary term in the printed \(N=4\) identity was
refuted (integration 56--66, 108--111; review 308--337).

Flatness and the empty `(U,e>1)` box therefore give the exact fibre
equation

\[
 a_p+\underbrace{r_p}_{l_1'}+
       \underbrace{\bigl(2r_p+\iota_p\bigr)}_{l_2'}=5,
 \qquad\text{i.e.}\qquad a_p+3r_p+\iota_p=5.                          \tag{3.5}
\]

At \(p_*\), (3.5) and \(r_{p_*}\ge1\) force

\[
 r_{p_*}=1,\qquad a_{p_*}=1,\qquad
 \text{local fibre partition }(3,1,1).                               \tag{3.6}
\]

Thus local irreducibility at the correction image is a consequence of
the degree-five fibre, not of [Z-6.5(b)].  If \(p\ne p_*\), (3.5) forces
\(r_p=1\) and \(a_p=2\).  At such a point both dicritical parametrizations are
nonsingular embeddings by pointwise [O-5.2]; a one-branch germ with that
property is smooth.  Hence \(p_*\) is the only singular point.  The full
pin is

\[
 \sigma=1,\qquad \nu=0,\qquad A=a_{p_*}=1.                            \tag{3.7}
\]

Equation (3.4) is then \(1=1\).  Unlike row (d) at \(N=4\) under H2,
strictness does not itself kill the arithmetic: here
\(\sum\mu_l=3=N-2\), exactly the promoted bound.

## 4. Componentwise normalization and singularity budgets

There are no separate image-curve budgets.  Both source components give
the same normalization map after the isomorphisms \(h_i\).  Their exact
requirements at \(z\in\widetilde D\) over \(p_*\) are:

| source dicritical | normalization degree | local datum | consequence for the same \(d\eta_z\) |
|---|---:|---|---|
| \(l_2'\), \(\mu=2\) | \(s_2=1\) | \(\mu_x=3>2\) | \(d\eta_z=0\) by [Z-6.5(b)] |
| \(l_1'\), \(\mu=1\) | \(s_1=1\) | \(\operatorname{corr}_1=0\) | \(d\eta_z\ne0\) by [O-5.2]/[Z-6.5(b)] |

The curve budget before imposing the second row is nevertheless precise:

* \(D\) is a polynomial curve, \(\widetilde D\simeq\mathbf A^1\), with
  one place at infinity;
* its only affine singularity is \(p_*\), and \((D,p_*)\) is a single
  primitive plane branch;
* the correction point contributes zero to
  \(\nu=\sum(r_p-1)\), but contributes \(a_{p_*}=1\) to the affine-fibre
  term in (3.4); and
* the critical normalization forces \(\delta_{p_*}\ge1\).  Since
  \(r_{p_*}=1\), its Milnor number is
  \(\mu_{\mathrm{Mil}}(p_*)=2\delta_{p_*}\ge2\).  This Milnor number is
  unrelated to Orevkov's \(\mu_x=3\).

The promoted Euler machinery contains \(r_p-1\), not \(\delta_p\), so it
does not determine the last integer or a Puiseux characteristic.  The
local models (2.3)--(2.6) exhibit, for example, budgets
\(\delta=1\) for \((2,3)\), \(\delta=4\) for \((2,9)\), and
\(\delta=3\) for \((3,4)\), all before the trivial dicritical is imposed.
The second table row instead makes \(\eta\) immersive at \(z\); because
the germ has only one branch, that forces it smooth and
\(\delta_{p_*}=\mu_{\mathrm{Mil}}(p_*)=0\).  The two componentwise
budgets are therefore incompatible.

## 5. Verdict on the \(N=5\) profile

**Verdict: the promoted profile self-destructs.**  This is not the
\(N=4\) row-(d) strictness argument.  The Euler and fibre machinery first
pins the arithmetically consistent shape (3.1), (3.6), (3.7); the two
degree-one parametrizations then contradict one another.

Indeed, let \(x_1=h_1^{-1}(z)\).  Since \(h_2\) is an isomorphism, the
unique correction gives

\[
 0=d\phi_2(x)=d\eta(z)\,dh_2(x),
 \quad\text{hence}\quad d\eta(z)=0.                                  \tag{5.1}
\]

Since \(h_1\) is also an isomorphism,

\[
 d\phi_1(x_1)=d\eta(z)\,dh_1(x_1)=0,                                 \tag{5.2}
\]

contrary to the everywhere-immersive \(\mu=1\) parametrization.  The
argument does not identify a cv flag with a physical place: it compares
the two distinct source points only after each has been mapped
isomorphically to the same normalization place \(z\).  Nor does it use a
lower bound as attainment.

Consequently no Puiseux type is consistent with **all** of (1.1).  The
ordinary cusp is not singled out and then excluded; rather, every
possible critical normalization germ is excluded by the second
degree-one copy of the normalization.  Thus the trivial-dicritical
profile at \(N=5\) is impossible under H2.

## 6. The exact PI1-S4-style residual question

There is no genuine fundamental-group residual after §5.  For clarity,
the question that would remain if one deliberately forgot the fatal
\(\mu=1\) normalization copy is the following.

> **Counterfactual `PI1-S5-CORR`.**  Let \(D\subset\mathbf C^2\) be an
> irreducible polynomial curve normalized by \(\mathbf A^1\), with one
> place at infinity and exactly one affine singular point \(p\), which is
> unibranch.  Suppose the germ is the discriminant of a normal local
> three-sheeted cover having generic simple ramification and one
> local-degree-three point.  Can
> \(\pi_1(\mathbf C^2-D)\) surject onto \(S_5\) so that every meridian of
> \(D\) maps to a transposition and the local group at \(p\) has orbit
> partition \((3,1,1)\), acting as \(S_3\) on the three-letter orbit and
> fixing the other two letters?

The \(S_5\) target is forced counterfactually: the branch locus is \(D\),
the generic meridian has cycle type \((2,1,1,1)\), and connected global
monodromy is a transitive group generated by transpositions, hence
\(S_5\).  Likewise, the three-letter local orbit is transitive and its
branch generators are transpositions, so its image is \(S_3\).  In the
additional smooth-source/smooth-ramification subcase,
\((D,p)\) is \(A_2\); the two standard local transpositions share one
letter and generate the displayed \(S_3\), rather than being disjoint as
in `PI1-S4`.

This question is only the \(\pi_1\)-shadow of the numerical packet.  A
YES would not realize the Keller configuration, because it omits the
second degree-one parametrization.  The exact source-aware residual is

> Can one normalization map \(\eta:\mathbf A^1\to D\) be critical at
> \(z\) through one degree-one dicritical parametrization and immersive
> at the same \(z\) through another?

Equations (5.1)--(5.2) answer this **NO**.  Accordingly no
`OPEN[PI1-S5-CORR]` should be entered and no PI1 acquisition is needed
for this profile.

## 7. Primary-source record and audit notes

The only literature results consumed are promoted statements or the
affine-line part of Orevkov Lemma 2.1 used in the reviewed source repair.
The frozen proof and hostile review independently record the following
primary-PDF hashes; no substitute edition is used here.

1. S. Yu. Orevkov, “On three-sheeted polynomial mappings of
   \(\mathbf C^2\),” *Math. USSR-Izv.* **29** (1987), 587--596,
   DOI `10.1070/IM1987v029n03ABEH000984`; Lemma 2.1 and Lemma 5.2,
   PDF pp. 2 and 8--9.  Hashed file `refs/jc86.pdf`:
   `f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db`.
   The source and statement audit is at proof 20--29, 63--72 and review
   56--83, 321--337.  Official record/PDF:
   <https://www.mathnet.ru/eng/im1571>.
2. H. Żołądek, “An application of Newton--Puiseux charts to the
   Jacobian problem,” *Topology* **47** (2008), 431--469,
   DOI `10.1016/j.top.2008.04.001`; Proposition 6.5(b), printed
   pp. 457--458/PDF pp. 27--28.  Hashed file
   `refs/zoladek2008_official.pdf`:
   `88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad`.
   The exact scope audit is at proof 73--77 and review 85--93.

The local germs (2.3) and (2.5), their Jacobians, normality check, and
discriminants were derived directly in this report; they are not cited
as global examples.  No CAS was run.  No canonical ledger or charged
input was edited, and `jc2-lean` was not inspected.  No new exit price is
asserted, so no charging declaration is appropriate.

<!-- BODY-END -->
