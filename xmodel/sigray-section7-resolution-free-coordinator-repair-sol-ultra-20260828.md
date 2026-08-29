# Sigray Section 7: resolution-free quotient repair

**Date:** 2026-08-28  
**Producer:** coordinator (Sol Ultra)  
**Status:** **FAILED at final delta gate** (`758c0226...`); do not promote

> **Failure notice.**  Sections 2--4.2 and the unweighted cluster bijection
> survive review, but the paragraph claiming transport of jump/max
> `kappa_F` is false as an inference.  The roots of `P(z)-a_0` and
> `P(z)-a` need not match; zero versus nonzero coefficient roots can change,
> changing the post-height gcd and `kappa_F`.  Therefore (4.3), the fixed
> baseline (6.1), and `(22-cl)` are not licensed by this report.  See the
> exact countermodel and clause ledger in the delta gate above.

## 0. Result

The cluster Euler identity `(22-cl)` can be proved without realizing every
critical-value flag on one common surface resolution.  The required
direction line is the abstract finite cyclic quotient of the Puiseux
coefficient line.  Corrected Statement 3.14 induces a choice-independent
isomorphism from each transported quotient line to the reference quotient;
in that transported coordinate both residual value functions agree.
Corrected EW1--EW2 then identify its points with direction clusters directly.

This route addresses the geometric objection in
`xmodel/sigray-section7-resolved-direction-lemma-hostile-review-terra-20260828.md`
by deleting the unproved common-resolution/divisor identification rather
than strengthening it.

The final theorem imports explicitly the reviewed every-fibre Proposition
5.8 replacement

```text
47eef0925470fc769eec08e6d3bf972446feaaff6f6ef709c154edaa31054caf
  xmodel/sigray-prop58-every-fiber-independent-audit-sol-ultra-20260828.md
```

and does not infer it from EW1--EW4.

## 1. Corrected local inputs

Let `Phi=(f,g):A2_C -> A2_C` be a polynomial Keller map.  On the fibre
`f=a`, use centred data for `A=f-a`.

We use only these previously isolated local facts:

1. **Unique zero-order flag (EW1).**  Every normalized puncture with finite
   `g`-value has a unique `Fhat_P in T_(a,cv)` on its ray, with
   `d_(f-a,Fhat_P)=d_(g,Fhat_P)=0`.
2. **Root-orbit realization and clustering (EW2).**  At such a flag, each
   realized root orbit of the centred first residual polynomial is one
   geometric outgoing direction.  Every root orbit is realized.  The
   punctures sharing the flag and direction are exactly the cluster
   `R^*_(F,c)` of repaired Proposition 7.3.
3. **Local weight (EW4).**  For a cluster `C` at `F`,
   `L_C=sum_(P in C) Lambda(P) >= b_F`, where
   `b_F=kappa_F(pi(F)-1)>0`; equality holds for a simple covered root.

The cross-fibre transport and cyclic descent needed below are proved rather
than assumed.

## 2. Arbitrary-truncation cyclic quotient

The construction must work for a rational cv flag, not only at a
characteristic vertex.

Treat the `y`-side; the `x`-side is symmetric.  Choose one common suitable
denominator `K` and write a branch realizing a flag `F=I_P(u)` as

\[
x=t^{-K},\qquad y=\sum_{r\ge0}c_rt^r,\qquad n=Ku\in\mathbb Z.
\]

Put

\[
\phi_{<n}(t)=\sum_{r<n}c_rt^r,
\qquad
e=\gcd\bigl(K,\{r<n:c_r\ne0\}\bigr),
\]

with `e=K` when the displayed support is empty.  The deck subgroup `mu_e`
preserves both `x=t^(-K)` and the truncated prefix.  In the residual chart

\[
y=\phi_{<n}(t)+t^n\eta,
\]

it acts by

\[
(t,\eta)\longmapsto(\zeta t,\zeta^{-n}\eta).
\]

Its effective image on the coefficient is the scalar group

\[
\Gamma_F\simeq\mu_m,
\qquad m=e/\gcd(e,n).
\]

Thus the **geometric coefficient-orbit line** is the algebraic quotient

\[
U_F:=\mathbb A^1_\eta/\Gamma_F
     =\operatorname{Spec}\mathbb C[\eta]^{\Gamma_F}
     =\operatorname{Spec}\mathbb C[\eta^m]
     \simeq\mathbb A^1_z. \tag{2.1}
\]

This is an abstract direction parameter.  No claim that it is an open
stratum of a chosen final boundary divisor is made or needed.

Under a synchronized refinement `K'=L K`, take `t=(t')^L`.  Then
`n'=Ln`, `e'=Le`, and every Laurent exponent `N` becomes `N'=LN`; hence
`e'/gcd(e',n')=e/gcd(e,n)` and the effective quotient is unchanged.
For the finite reference list below we fix one denominator throughout, so
even this explicit independence is not used as an identification step.  On
the `x`-side one writes `y=t^(-K)` and
`x=phi(t)+t^n eta`; the same deck calculation is verbatim.

## 3. Zero-order cyclic descent

For any polynomial `h(x,y)`, substitute the chart above:

\[
H(t,\eta)=h(t^{-K},\phi_{<n}(t)+t^n\eta)
         =\sum_N t^N H_N(\eta).
\]

Deck invariance gives the exact identity

\[
H(\zeta t,\zeta^{-n}\eta)=H(t,\eta),
\]

and hence, coefficient by coefficient,

\[
H_N(\zeta^{-n}\eta)=\zeta^{-N}H_N(\eta). \tag{3.1}
\]

In Sigray's notation `t^N=x^{-N/K}`, so the residual polynomial selected at
order `d_(h,F)=0` is exactly `H_0`.  Equation (3.1) then says

\[
H_0(\gamma\eta)=H_0(\eta)\quad(\gamma\in\Gamma_F).
\]

Therefore every zero-order residual polynomial descends uniquely to a
polynomial on `U_F=A1_z`.  This proves, for arbitrary rational flags, the
zero-order descent that the earlier producer had only asserted.

## 4. Cross-fibre transport on the quotient

Fix values `a_0,a`.  The construction in the proof of corrected Statement
3.14 takes a branch for `f=a_0` realizing `F=I_P(u)` and a branch for `f=a`
whose Puiseux coefficients strictly below `u` agree.  Choose a suitable
denominator common to this pair of presentations.  (Only pairwise common
denominators are needed.)  The two substitutions then have the same strict
prefix and the same prefix-preserving deck group.

Write `U_F` for the reference quotient and `U_{F(a)}` for the quotient in
the transported fibre.  In aligned covers corrected Statement 3.14 has the
form

\[
\eta_{\rm ref}=\omega\eta_a
\]

for one nonzero root of unity `omega`, common to the residuals of **every**
fixed polynomial.  Scalar multiplication commutes with the cyclic deck
actions and therefore induces an isomorphism

\[
\tau_{F,a}:U_{F(a)}\longrightarrow U_F,
\qquad [\eta_a]\longmapsto[\omega\eta_a]. \tag{4.1}
\]

This map is independent of the aligned representatives.  Indeed, two
aligned choices differ by a deck reparametrization preserving the common
strict prefix; their ratio lies in the prefix stabilizer and hence has the
same class on the quotient.  In a coordinate `z=eta^m`, `tau_(F,a)` can be
the nontrivial scaling `z_ref=omega^m z_a`.  Thus the twist is tracked by
`tau`; it is not incorrectly declared trivial on the quotient.

Let the descended centred residuals at the reference flag be

\[
A_F(z)=p_{f-a_0,F}(\eta),\qquad Q_F(z)=p_{g,F}(\eta),
\quad z=\eta^m,
\]

and put `P_F=a_0+A_F`.  If a target quotient point is denoted by
`z:=tau_(F,a)([eta_a])`, then residual transport gives

\[
p_{f-a,F(a)}(\eta_a)=P_F(z)-a,
\qquad p_{g,F(a)}(\eta_a)=Q_F(z). \tag{4.2}
\]

The effective deck orbits used here are exactly EW2's coefficient-root
orbits.  A prefix-preserving deck reparametrization gives the same truncated
Puiseux direction, while coefficients in distinct effective orbits first
differ at height `u` and give distinct outgoing directions.  Consequently
EW2 applies to the points of `U_F`, including the fixed orbit `eta=0`.

The baseline weight is also transported, rather than assumed constant.
In the notation of Section 2, the common strict prefix preserves `K`, `n`,
and `e`.  For each realization at height `u`, multiplication by the nonzero
scalar `omega` preserves whether its coefficient is zero.  A nonzero
coefficient changes the post-height gcd from `e` to `gcd(e,n)`, while a zero
coefficient makes no jump there.  Hence the complete multiset of rooted
contact jumps at `u` is preserved.  The audited Q/jump/max convention takes
the maximum post-jump lattice index over these realizations, so it gives the
same `kappa_F` on both fibres; this is the explicit lattice form of the
reviewed H5a repair (`dd09069b...`, review `3b8bd5c9...`).  Since `pi(F)=u`
is unchanged,

\[
b_F=\kappa_F(\pi(F)-1) \tag{4.3}
\]

is unchanged as well.

Finally, aligned expansion preserves every Laurent exponent of `g`, hence
preserves `d_(g,F)=0`.  Corrected Statement 3.14 and its inverse therefore
give a bijection

\[
T_{a_0,cv}\longleftrightarrow T_{a,cv}. \tag{4.4}
\]

This quotient isomorphism, rooted-jump transport, and flag bijection are the
only cross-fibre statements used below.

## 5. Quotient points are exactly direction clusters

Enumerate the finite reference set

\[
T_{a_0,cv}=\{F_1,\ldots,F_s\}.
\]

For each `i`, fix the quotient line `U_i=A1_z` and polynomial map

\[
\varphi_i:U_i\longrightarrow\mathbb A^2,
\qquad z\longmapsto(P_i(z),Q_i(z)). \tag{5.1}
\]

Take `z in U_i`, put `a=P_i(z)`, and use `tau_(i,a)^(-1)` to choose any
covered lift `c` of the corresponding target quotient point.  Equation
(4.2) makes the orbit of `c` a root orbit of the centred first residual at
the transported flag `F_i(a)`.  EW2 realizes that orbit as exactly one
geometric outgoing direction; all punctures over it form one nonempty
cluster `C(i,z)`.  Residual transport together with EW2/repaired Proposition
7.3 gives their common value `g=Q_i(z)`.  The result is independent of the
lift by construction of the quotient.

Conversely, take any finite-value cluster on any fibre.  A puncture in it
has one unique flag by EW1.  Transport (4.2) returns one unique reference
`F_i`; EW2 returns one coefficient orbit, hence one unique quotient point
`z`.  Thus

\[
\coprod_{i=1}^s U_i(\mathbb C)
\ \xrightarrow{\sim}\
\{\text{finite-value direction clusters in all fibres}\}. \tag{5.2}
\]

There is no cross-vertex duplication: a cluster has one flag by EW1, and
injectivity of the flag transport (4.4) gives one reference index `i`.
There is no cyclic duplication because one orbit is one quotient point.
Collision points are ordinary finite coefficient orbits and remain in
`U_i`; nothing is deleted except the coefficient value infinity, which was
never in `A1_eta`.

The first coordinate `P_i` is nonconstant.  At the reference cv flag the
centred residual `A_i=P_i-a_0` is a nonzero leading polynomial and has a
realized root orbit.  A nonzero constant has no root, so `A_i`, and hence
`P_i`, has positive degree.  Thus `P_i` is surjective over `C`, and every
`varphi_i` has finite fibres.

## 6. Constructible baseline

Put

\[
b_i=\kappa_{F_i}(\pi(F_i)-1)>0,
\qquad
B(a,b)=\sum_i b_i\,#\varphi_i^{-1}(a,b). \tag{6.1}
\]

The count is of quotient points/directions, not normalized punctures.  Since
`P_i` is nonconstant, `varphi_i` is quasi-finite; its geometric fibre count
is constructible.  Compactly supported Euler-Fubini gives

\[
\int_{\mathbb A^2}#\varphi_i^{-1}(a,b)\,d\chi_c
=\chi_c(U_i)=\chi_c(\mathbb A^1)=1,
\]

so

\[
\int_{\mathbb A^2}B\,d\chi_c=\sum_i b_i. \tag{6.2}
\]

Ramification, self-intersections of `varphi_i(U_i)`, and common image curves
for different `i` cause no problem: geometric fibre cardinality counts the
source points with exactly the required multiplicity convention.

## 7. Pointwise deficit and the Euler identity

Let `d=td(f,g)` and `N(a,b)=#Phi^{-1}(a,b)`.  The reviewed every-fibre
Proposition 5.8 says that `g` has meromorphic degree `d` on the normalization
of every fibre `f=a`.  The divisor of `g-b`, together with the fact that
affine Keller preimages are simple, gives

\[
d-N(a,b)
=\sum_{P\text{ at infinity},\ g(P)=b}\Lambda(P). \tag{7.1}
\]

Group the right side by (5.2).  EW4 yields

\[
d-N(a,b)=B(a,b)+E(a,b),\qquad E(a,b)\ge0, \tag{7.2}
\]

where `E` is the sum of `L_C-b_C` over the clusters with value `(a,b)`.
For fixed `a`,

\[
\sum_bE(a,b)=\delta_a^{cl}. \tag{7.3}
\]

The function `E=d-N-B` is constructible.  Outside the finite union of the
critical-value sets of the `P_i` and the values `P_i(0)` for nontrivial
covers, every root is simple in the covered coefficient coordinate.
Repaired Proposition 7.3 then gives `E=0`.  Thus `delta_a^cl` has finite
support and

\[
\int_{\mathbb A^2}E\,d\chi_c=\sum_a\delta_a^{cl}. \tag{7.4}
\]

Finally, a Keller map is quasi-finite, and Euler-Fubini for its finite
geometric fibres gives

\[
\int_{\mathbb A^2}N\,d\chi_c=\chi_c(\mathbb A^2)=1.
\]

Integrating (7.2), using (6.2) and (7.4), proves

\[
\boxed{
td(f,g)=1+\sum_{i=1}^s\kappa_{F_i}(\pi(F_i)-1)
          +\sum_{a\in\mathbb C}\delta_a^{cl}.}
\tag{22-cl}
\]

In particular the repaired Corollary 7.1 follows for any pairwise distinct
cv vertices on one fibre.

## 8. Dependency and failure ledger

- The literal per-puncture `delta_a` and printed equation (22) remain
  invalid/unproved.  Only the direction-cluster replacement is claimed.
- The exact local germ from the earlier hostile review is not a global
  polynomial counterexample; it is used only to refute the proposed local
  inference from a whole-cluster degree to one baseline per puncture.
- No common compactification, divisorial realization, or assertion that
  later blowups preserve a particular open boundary stratum is used.
- The new mathematical input is the elementary arbitrary-truncation deck
  calculation (Sections 2--3), plus the explicit quotient isomorphism and
  rooted jump/max transport in Section 4.
- Proposition 5.8 is an explicit reviewed dependency, not hidden inside the
  Euler algebra.
- GPT-5.5 independently passed the quotient route and Euler proof but asked
  for centred notation and safe twist wording (`521080ae...`).  Terra found
  that the earlier wording still failed to track the induced quotient
  scaling and did not prove jump/max weight transport (`d207180a...`).
  Section 4 now installs exactly those two
  repairs.  Promotion awaits a different-model delta check of the amended
  clauses only.
