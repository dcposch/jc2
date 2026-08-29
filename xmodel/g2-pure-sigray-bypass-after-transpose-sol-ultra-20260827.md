# Pure-Sigray bypass after the transpose audit

**Lane:** Sol Ultra, independent desk-scale assessment  
**Date:** 2026-08-27  
**Question:** starting with the whole exact Sigray-normalized hypothetical
Keller pair, rather than a GGV family or frozen polygon record, what is already
available; where does the pure route first need new mathematics; and is that
mathematics cheaper or more informative than a new anti-standard GGV source
theorem?  
**External source checked:** Valqui--Guccione--Guccione (VGG), *On the shape
of possible counterexamples to the Jacobian Conjecture*,
[arXiv:1401.1784v3](https://arxiv.org/abs/1401.1784), especially Remark 6.8,
Proposition 6.9, Proposition 7.3, and Corollary 7.4.  
**Computation:** none. No local or AWS algebra job was run.

## 0. Verdict

The pure-Sigray bypass is real, but it bypasses only the **GGV source and
transport problem**, not the endpoint problem.

1. If the input is the whole exact normalized pair `(f,g)` and a fibre value
   `a`, standard Newton--Puiseux theory constructs every boundary place of
   `f=a` in both infinity charts, its full contact ancestry, and whether `g`
   is a pole or has a finite limit there. Thus the pure route needs neither
   `G2-PSC` nor a second GGV run merely to *name all pole paths*. This is the
   strongest conclusion of the exact-pair constructor after its hostile
   review.
2. The intrinsic two-chart tree is stronger than the current GGV packet but
   weaker than a fully certified Sigray book source. The Sigray-specific
   approximate-root and `Q/jump/max` decorations still inherit the filed
   Proposition 4.2 finite-leading-part gap, the `T_a^-` typing repair, and the
   requirement to retain tower degrees at every pole ancestor.
3. Pole mass and the resolved-pencil mismatch identity are exact at their
   stated perimeters. Landing is not: composite one-pole, general `b>=2`, and
   post-first-jump `M>=2` continuations remain open. Bounded delay is not:
   only the conditional implication `UCD => G2-BD` is proved. Degree control
   is not: `RPMC(C)` gives a type-relative bound, and a selected-pair type cap
   is separately missing.
4. VGG's Laurent reflection
   `psi_2(x)=-x^-1, psi_2(y)=x^2 y` is **not** a chart-preserving bypass. It
   sends an `x=infinity` valuation to the divisor `x'=0`, not to the other
   infinity chart of the same fixed polynomial pair. Proposition 6.9 uses it
   as a special support normalization, not as an all-branch source theorem.
5. VGG Proposition 7.3 and Corollary 7.4 are more useful than the reflection:
   on the same fixed pair they propagate bracket-zero/valuation-ratio data
   through the opposite interval and make the eligible `P`-faces perfect
   powers. They provide **common-power face data**, not intrinsic branch
   labels, successor/ancestor paths, pole tags, deck stabilizers, or
   proximity-center coverage.
6. The highest-value next theorem is therefore not a fresh anti-standard
   analogue of all fourteen GGV complete-chain clauses. It is the narrower
   **all-root Corollary-7.4 face-to-place/proximity theorem**, followed by a
   root-weighted capacity estimate at the first centers where VGG
   proportionality fails. The numerical clause is precisely an
   exit-supported route to `RPMC(C)`.

Two new exact connections sharpen that recommendation.

- A Riemann--Hurwitz balance shows that the finite-valued boundary ends,
  which the pole-only book discards, carry total local degree

  \[
  \sum_{S\text{ finite}} e_S
    = td+ b_1(f^{-1}(a))-1.
  \]

  Hence every hypothetical counterexample necessarily has finite-valued
  ends of total weight at least `td`. A route claiming full boundary
  coverage cannot silently discard the finite-end Sigray gaps, although a
  genuinely pole-only contradiction could bypass that sector.
- Proposition 7.3 describes a **zero-mismatch corridor**: after a faithful
  face-to-proximity transport, its normalized valuation ratios make the
  corresponding point-basis discrepancy zero. Total degree is carried by
  the exits from common-power propagation, not by the length of the
  common-power corridor. This explains why an anti-standard chain can add a
  great deal of source metadata while adding little direct degree control.

No total-degree upper bound, contradiction, counterexample, or JC2 result is
proved here.

---

## 1. Strongest exact-pair chain presently in the repository

The following table deliberately starts **after** the requested premise: an
arbitrary exact normalized hypothetical Keller pair is already in hand. It
does not import a GGV family, a live corner, or a polygon-degree cutoff.

| layer | strongest existing statement | exact stopping point |
|---|---|---|
| source | The whole coefficient pair `(f,g)`, with `J(f,g) in C*`, the normalized rectangle/NE-corner property, type `2<=alpha<beta`, and a fibre `a`, is a lossless source object. If one starts earlier with an arbitrary counterexample, `REDUCTION.md` T4 supplies such a representative, relative to its disclosed Sigray/Abhyankar source perimeter. | No GGV restriction survives this choice unless a separate transport theorem is proved. For this report that is intentional. |
| two-chart tree | Normalization of `f=a` plus Newton--Puiseux gives every boundary DVR, both chart expansions, deck orbits, all characteristic/contact vertices, and the intrinsic Eggers--Wall forest. The normalized rectangle proves the two-chart dichotomy. | The reviewed contact is the maximum over presentations. Full later-book labels require the repaired `Q/jump/max` value of `kappa_F`, `T_a^-` tower data, and tower degrees at all ancestors. The Proposition 4.2 constant-leading-part existence gap remains. |
| pole/path | Direct substitution of the exact `g` in every branch field gives `ord_S(g)`, hence pole/finite status and every full ancestor path to a pole. Exact-pair coverage is tautological: there is no selected-root or chart-surjectivity debt. | This does not validate every Sigray transition identity or the unaudited later thesis statements used by the book. A pole-spanned subtree also omits finite-valued ends. |
| pole mass / entry | At the corrected perimeter, every fibre has `d=sum_F Lambda(F)`, with `Lambda=D_g deg(p)/nu`; promoted pole formulas give `Lambda=ab alpha beta/nu`, `M=b`, `Lambda>=beta`, and a finite entry menu for each fixed `d`. | The mass identity is repaired using the disclosed local Sigray inputs, surface geometry, and Chau. The complete entry parameterization and `M=b` remain conditional on the stated Sigray/TDU/MP package. A finite entry menu at fixed `d` is not a full book. |
| landing | Prime-`d` one-pole configurations are conditionally excluded. For multi-pole all-`b=1`, every configuration conditionally lands at a marked first jump/root event in a finite local menu for fixed `(s,d)`. | Composite one-pole, general off-axis `b>=2`, all-`mu>=2` later merges, post-jump `M>=2` suffixes, and full downstream provenance are not covered. There is no universal complete landing map. |
| delay | Along a characteristic segment, `prod_j nu_j <= kappa` and `nu_j>=2`, so `d_sh<=floor(log_2 kappa)`. A uniform carrier-denominator bound `kappa<=K` would imply `G2-BD`. | No such `K` is proved. At residue A, abstract `l=0` carriers preserve `w=2` indefinitely. Fixed-passport rigidity and the D-window cadence do not bound their source fibre. |
| degree | `d>=6`; exact pole mass; and the exact common-resolution identity `d/(alpha beta)=1/2 sum_p(R_p/alpha-S_p/beta)^2`. Common leading powers and the rootwise orthogonal split are exact. `RPMC(C)` implies `d<=C alpha beta`. | `RPMC(C)`, `KME-finite`, and a selected-counterexample type cap are open. A fixed absolute bound for **all** counterexamples is equivalent to JC2 because iterates have degrees `d^k`. |

The important distinction is between two meanings of “full tree.” The exact
pair determines the full **intrinsic** tree. The campaign does not yet have a
single reviewed theorem saying that all Sigray approximate-root, `M`,
`lambda`, and `Q(F)` labels used by Sections 8--9 exist with the corrected
semantics at every vertex of that tree. The pure route closes coverage, not
that trust perimeter.

### 1.1 Exact source and two-chart constructor

For a normalized pair, the rectangle/NE-corner property excludes a place of
`f=a` at which both affine coordinates tend to infinity. At every boundary
place exactly one coordinate is therefore the Laurent coordinate and the
other has a Puiseux expansion with finite constant term. Normalizing the
projective fibre gives the exact evaluation maps

\[
 \mathbf C[x,y]/(f-a)\longrightarrow \mathbf C((t_S))
\]

for every boundary place `S`. Taking every conjugate and quotienting by the
deck action gives both components of the Eggers--Wall forest. This consumes
the actual pair and therefore has no `CornerData -> branch` information loss.

The hostile review of
[`g2-psc-typed-source-to-pole-tree-interface-sol-ultra-20260827.md`](g2-psc-typed-source-to-pole-tree-interface-sol-ultra-20260827.md)
confirmed this constructor with four repairs recorded in
[`g2-psc-typed-source-to-pole-tree-interface-hostile-review-opus5-20260827.md`](g2-psc-typed-source-to-pole-tree-interface-hostile-review-opus5-20260827.md):

1. include the normalized rectangle hypothesis;
2. use contact maximum over presentations;
3. retain the Proposition 4.3 `T_a^-` tower and disclose the Proposition 4.2
   gap; and
4. retain `lambda_F`, `M_F`, `Q(F)`, and all approximate-root degrees at
   every ancestor vertex, not only at poles.

These repairs do not revive `G2-PSC`. They say exactly what extra Sigray
labels must be computed from the already complete intrinsic forest.

### 1.2 Pole paths are present; book landing is not

For each exact branch evaluation, `ord_S(g)<0` is the pole predicate. Thus
the set of pole places and the smallest subtree spanning their roots and
ancestor paths are computed without a GGV occurrence. The every-fibre mass
identity in [`REDUCTION.md`](../ladder/REDUCTION.md) T7 then reads

\[
 d=\sum_{F\in T_{a,\mathrm{pole}}}\Lambda(F),\qquad
 \Lambda(F)=\frac{a_Fb_F\alpha\beta}{\nu_F}.
\tag{1.1}
\]

This gives a finite necessary entry menu at fixed `d`. It does not bound
`d`, and it does not supply a finite full configuration beyond the sectors
listed in the table. In particular, replacing GGV transport with the exact
pair does not repair `T9(c)` or `T10`.

### 1.3 Delay and degree remain independent obligations

The exact depth implication is

\[
 \prod_j\nu_j\le\kappa_i,\quad \nu_j\ge2
 \quad\Longrightarrow\quad
 d_{\rm sh}\le\lfloor\log_2\kappa_i\rfloor.
\tag{1.2}
\]

It becomes a uniform delay theorem only after `UCD` bounds `kappa_i`. No
tree-coverage theorem supplies that bound.

The degree identity lives on a different common resolution. If
`deg f=B alpha`, `deg g=B beta`, and `R_p,S_p` are the point-basis
multiplicities of the two pencils, then

\[
 \boxed{
 \frac d{\alpha\beta}
 =\frac12\sum_p
 \left(\frac{R_p}{\alpha}-\frac{S_p}{\beta}\right)^2.}
\tag{1.3}
\]

This is exact and bypasses book landing. Its missing input is a quantitative
Keller constraint on the normalized divergence centers, not another finite
entry enumeration.

---

## 2. The Laurent reflection is not the other chart

VGG Remark 6.8 defines

\[
 \psi_2(x)=-x^{-1},\qquad \psi_2(y)=x^2y
\tag{2.1}
\]

on `L^(1)=C[x,x^-1,y]`. It is involutive and Jacobian preserving. On a
monomial and on a direction it acts as

\[
 (a,b)\longmapsto(-a+2b,b),
 \qquad
 (\rho,\sigma)\longmapsto(-\rho,2\rho+\sigma),
\tag{2.2}
\]

and its determinant `-1` explains the endpoint swap.

For a physical valuation `v_S`, however,

\[
 v_S(\psi_2(x))=-v_S(x),\qquad
 v_S(\psi_2(y))=2v_S(x)+v_S(y).
\tag{2.3}
\]

Consequently an original `x=infinity` place becomes `x'=0`. Conversely,
the new `x'=infinity` chart probes the original divisor `x=0`. The map is
not a polynomial automorphism of `A^2`; it changes the compactification and
has a pole on `x=0`. It therefore transports a Laurent branch identity but
does not produce the missing physical infinity chart of the same fixed
polynomial pair.

VGG Proposition 6.9 is consistent with this reading. It applies
`psi_2 o psi_1` in the special direction `(2,-1)` to turn one endpoint into
an `(1,0)` endpoint and derive a support restriction. It contains no claim
that all branches of the other fixed-pair chart are emitted.

Thus `psi_2` is useful for checking formulas and normalizing a selected
corner. It is not the pure-Sigray bypass and not an anti-standard source
theorem.

---

## 3. What VGG Proposition 7.3 and Corollary 7.4 really add

Let `m,n>1` be coprime and let `P,Q in L^(l)` satisfy the constant-Jacobian
and matching `(1,1)`/`(0,1)` valuation-ratio hypotheses of VGG Proposition
7.3. At a direction `(rho_0,sigma_0)`, the proposition additionally assumes
an eligible positive face, common normalized starting endpoint, the reversed
inequality `b<a/l`, and the stated bracket-tower endpoint condition. Its
conclusion, throughout the maximal opposite interval, is

\[
 [\ell_{\rho,\sigma}(T_j),\ell_{\rho,\sigma}(P)]=0,
 \qquad
 \frac{v_{\rho,\sigma}(T_j)}{v_{\rho,\sigma}(P)}
 =
 \frac{v_{\rho_0,\sigma_0}(T_j)}
      {v_{\rho_0,\sigma_0}(P)}.
\tag{3.1}
\]

Corollary 7.4 adds its Theorem-2.6 rationality hypothesis and concludes that
for every direction in that interval

\[
 \ell_{\rho,\sigma}(P)=R^{qm}
\tag{3.2}
\]

for a homogeneous Laurent polynomial `R`.

This is genuine same-fixed-pair anti-side information. It is stronger than
conjugating the already known branch and materially lowers the cost of an
anti-side proof. But its output is a face factorization, not a branch forest.
Neither statement supplies:

- a fibre value or a map into a boundary branch field;
- every residual root rather than the existence of a useful factorization;
- a proof that cumulative translations equal the strict Puiseux truncation
  of an actual branch (`H-TRUNC`);
- deck stabilizers and reduced branch denominators;
- successor/ancestor, characteristic, contact, or merge IDs;
- pole versus finite-limit status of `Q` along a leaf;
- the repaired `Q/jump/max` label, approximate-root tower, or `M_F`; or
- gluing and no-double-counting on a common projective resolution.

### 3.1 Narrow missing structural theorem: `C74-PLACE`

The smallest useful source theorem is therefore the following, not a new
anti-standard copy of all GGV complete-chain clauses.

> **CONJECTURE `C74-PLACE` (all-root Corollary-7.4 face-to-place forest).**  
> For an exact normalized pair and a generic fibre, retain every deck orbit
> of every residual root of the common-power faces in the Proposition-7.3
> interval. Successive exact translations are the strict Newton--Puiseux
> truncations of actual boundary places. As the direction changes, their
> continuations form the intrinsic successor/ancestor forest in the relevant
> infinity chart. Leaves modulo deck action biject the tagged boundary
> places, and the construction records their corresponding infinitely-near
> base centers without duplication.

The first two sentences can be attacked with the exact pair and ordinary
Newton--Puiseux continuation; no GGV family theorem is needed. The last
sentence is the load-bearing bridge to (1.3): face directions must be
identified with the point-basis/proximity centers on the common resolution.

`C74-PLACE` by itself gives neither pole-path *exhaustion of a pole-only
packet* nor a total-degree bound. In the pure architecture, exhaustion comes
from the exact-pair tree; what remains is the compatibility of the VGG face
labels with that tree and with the resolution lattice.

### 3.2 New connection: VGG corridors are zero-mismatch corridors

For the `T_0=Q` specialization under Proposition 7.3's stated tower
hypotheses, its starting endpoint condition and (3.1) give

\[
 \frac{v_{\rho,\sigma}(P)}m
 =\frac{v_{\rho,\sigma}(Q)}n
\tag{3.3}
\]

throughout the eligible interval. Suppose `C74-PLACE` identifies a string of
these divisorial valuations with consecutive exceptional divisors on the
common pencil resolution. If (3.3) holds on the string and its parent, the
invertible proximity transform gives, at the corresponding point-basis
centers,

\[
 \frac{R_p}{m}=\frac{S_p}{n}.
\tag{3.4}
\]

When `(m,n)=(alpha,beta)` are the normalized pair exponents, every such
center contributes zero to the mismatch square in (1.3). This implication
is elementary once the missing transport is supplied; it does not claim
that the transport is already proved.

The strategic conclusion is important:

> **The length of a common-power chain is not what total degree sees. Total
> degree is supported at the first exits from VGG valuation-ratio
> propagation and at their later nonproportional descendants.**

This explains both the value and the limitation of an anti-standard source
extension. It can locate a longer proportional corridor, but it does not
bound the number, amplitude, or persistence of the exit discrepancies.

---

## 4. New exact finite-end balance

This section connects the pure two-chart tree, the pole-mass identity, and
the global topology of a generic fibre. The identity is elementary, but it
is not presently used in the repository's pure-Sigray roadmap. No literature
novelty is claimed.

Choose a generic `a` so that

\[
 C=f^{-1}(a)
\]

is smooth and connected. Connectedness follows from primitivity: if
`f=h(u)` with `deg h>1`, a root of `h'` has a nonempty `u`-fibre on which
`df=0`, contradicting `J(f,g) in C*`. Let `bar C` be the smooth projective
completion, of genus `g_C`, and let

\[
 \mathcal B=\bar C\setminus C
 =\mathcal P\sqcup\mathcal N
\]

where `P` is the set of `g`-poles and `N` is the set of boundary places at
which `g` has a finite value. Put

\[
 r_\infty=|\mathcal P|,\qquad r_0=|\mathcal N|,
 \qquad r=r_\infty+r_0.
\]

For `S in P`, let `lambda_S=-ord_S(g)`. For `S in N`, let

\[
 e_S=\operatorname{ord}_S(g-g(S))\ge1.
\]

The rational map `g:bar C -> P^1` has degree `d=td(f,g)`, and

\[
 \sum_{S\in\mathcal P}\lambda_S=d.
\tag{4.1}
\]

The Jacobian condition says that `g|_C` has no ramification: the tangent to
`f=a` is annihilated by `df`, while `dg` cannot annihilate it as well.
Therefore every ramification point of the compactified map lies in
`mathcal B`. Riemann--Hurwitz gives

\[
 2g_C-2
 =-2d
  +\sum_{S\in\mathcal P}(\lambda_S-1)
  +\sum_{S\in\mathcal N}(e_S-1).
\tag{4.2}
\]

Using (4.1) and adding `r_0` yields the exact balance

\[
 \boxed{
 \sum_{S\in\mathcal N}e_S
   =d+2g_C+r-2
   =d+b_1(C)-1.}
\tag{4.3}
\]

Here `b_1(C)=2g_C+r-1`; this notation is deliberately distinct from
Sigray's later `delta_a`.

### 4.1 Consequences

1. **Pole saturation is the automorphism endpoint.** If `N` is empty, then
   (4.3) forces `d=1` and `b_1(C)=0`. Equivalently, `g:C->A^1` is a connected
   finite etale cover and hence an isomorphism. The resulting birational
   Keller map is an automorphism.
2. **A counterexample must have substantial finite ends.** The existing
   dual-pencil endpoint says a nonautomorphic Keller pair has `b_1(C)>=1` in
   every pencil direction. Hence (4.3) gives

   \[
   \sum_{S\in\mathcal N}e_S\ge d.
   \tag{4.4}
   \]

   Pole ends carry total pole degree exactly `d`; finite ends carry total
   local degree at least `d`.
3. **Three exact global coordinates coincide.** Combining (1.1), (1.3), and
   (4.3) gives

   \[
   \boxed{
   \sum_{F\in T_{a,\mathrm{pole}}}\frac{a_Fb_F}{\nu_F}
   =\frac12\sum_p
      \left(\frac{R_p}{\alpha}-\frac{S_p}{\beta}\right)^2
   =\frac{1+\sum_{S\in\mathcal N}e_S-b_1(C)}
          {\alpha\beta}.}
   \tag{4.5}
   \]

   The first term is Sigray pole mass, the second is resolved mismatch
   energy, and the third is finite-end ramification minus topology.

Equation (4.5) is the most useful new connection in this report. It shows
that a pole-only landing object is not a complete model of the boundary: a
hypothetical counterexample necessarily contains a comparably large
finite-valued sector. This does not rule out a proof that independently
kills every possible pole configuration without modeling the finite ends,
and it does not prove that every counterexample hits the precise
constant-leading stuck subcase in Sigray Proposition 4.2. It does prove that
any route claiming full boundary coverage must repair or bypass the filed
Proposition 4.2/5.1 finite-asymptotic gaps.

The cheapest direct contradiction statement is therefore

> **`GENERIC-POLE-SATURATION`:** some generic fibre of a degree-minimal
> normalized hypothetical pair has no finite-valued boundary place of `g`.

It proves JC2 immediately by (4.3). But it is the already known
zero-infinity-defect endpoint in branch language, so its proof cost is
essentially that of the conjecture. It is a clean target, not a cheap one.

---

## 5. First missing theorem with high information value

There are three notions of “universal bound,” and they must not be conflated.

1. A fixed bound for **every** Keller counterexample is equivalent to JC2:
   if one counterexample has degree `d>1`, its iterates have degrees `d^k`.
2. A type-relative bound `d<=C alpha beta` is a genuine intermediate result.
3. An absolute bound for a **selected source/target-minimal** representative
   is also meaningful, but it additionally needs a uniform selected-type
   theorem.

For item 2, the smallest existing numerical target is

\[
 \boxed{
 \mathcal E_P
 :=\frac12\sum_{p\succ P}
 \left(\frac{R_p}{\alpha}-\frac{S_p}{\beta}\right)^2
 \le C\frac{\mu_P}{B}.}
\tag{5.1}
\]

This is `RPMC(C)`, where `P` is a proper root of the common leading form
`H`, of multiplicity `mu_P`, and `sum_P mu_P=B`. Summing (5.1) gives
`d<=C alpha beta`.

The VGG audit suggests a sharper proof organization for (5.1):

> **`EXIT-RPMC(C)`.** Under `C74-PLACE`, every nonzero normalized
> point-basis discrepancy lies in a unique subtree rooted at the first exit
> from a Proposition-7.3 proportionality corridor. For each proper leading
> root `P`, the complete energy of all its exit subtrees is at most
> `C mu_P/B`.

The first clause is a source/proximity theorem; the second is the new
Keller-specific capacity inequality. Together they imply `RPMC(C)`. This
form is preferable to “extend the anti-standard chain” because it asks the
source theory to emit exactly the centers that carry degree.

For item 3, even `EXIT-RPMC(C)` is insufficient. One still needs the
selected-counterexample type cap `alpha beta<=B_0` (or a direct selected-pair
degree ceiling). Neither VGG common powers nor Sigray landing supplies that
cap.

### 5.1 Cost and information comparison

The numerical ratings are strategic estimates, not theorem statuses.

| target | estimated proof cost | information if proved | residual obligations |
|---|---:|---|---|
| use `psi_2` as the second chart | 1/10 to test; it fails | none for the other physical chart | all source, coverage, and endpoint obligations remain |
| fresh anti-standard analogue of the full GGV complete-chain theorem | 7--8/10 | selected-root chains and anti-side necessary conditions | still needs all roots, actual branch truncations, deck orbits, pole/finite tags, path coverage, proximity transport, `Q/jump/max`, landing, delay, and degree/type control |
| `C74-PLACE` using VGG Corollary 7.4 plus exact Newton--Puiseux | 4--6/10 | same-fixed-pair all-root anti-side forest and resolution provenance | still needs an exit capacity inequality; Sigray labels needed only for a book endpoint |
| `EXIT-RPMC(C)` / `RPMC(C)` | 8.5--9/10 | a genuine type-relative total-degree theorem, independent of book landing | selected absolute bound still needs a type cap |
| `GENERIC-POLE-SATURATION` | 10/10 | direct contradiction / JC2 | essentially the whole global problem in endpoint form |

An honest anti-standard theorem is therefore worth running only if it emits
new **exit restrictions** unavailable from VGG Section 7 and exact
Newton--Puiseux. Re-certifying a longer common-power corridor has low degree
information because that corridor is normalized-mismatch zero after faithful
transport.

---

## 6. Recommended next proof probe

The following is narrower than either rebuilding GGV or completing the full
Sigray book.

1. Prove `C74-PLACE` first for one exact generic fibre and one chart, with
   every residual root retained. The output must include cumulative
   translations, deck stabilizers, intrinsic branch IDs, and the associated
   proximity centers. This is a desk-scale theorem-development task, not an
   enumeration.
2. Verify the zero-mismatch-corridor implication (3.3)--(3.4) on that exact
   dictionary. Mark the first successor at which the normalized ratio
   fails. Do not spend effort extending already proportional ancestors.
3. Attack the `mu_P=1` one-root instance of `EXIT-RPMC(C)`: classify the
   integrable two-gradient matrix factorizations at a first exit and seek a
   root-length budget. This is the smallest sector in which a proof changes
   the degree theorem rather than only its source metadata.
4. In parallel, add the finite-valued ends from (4.3) to the intrinsic
   target. Any future “pure full tree” theorem must type their local degrees
   `e_S`; pole-only coverage is known in advance to omit necessary mass.
5. Keep the anti-standard GGV lane in the background as a constraint
   generator. Promote it over the pure route only if it proves an exit
   condition, no-double-counting law, or root-weighted capacity unavailable
   from Corollary 7.4.

This route does not wait for a universal landing theorem or bounded-delay
review. Once the exact pair and common resolution are fixed, `EXIT-RPMC(C)`
can be attacked while Sigray book reviews continue independently.

---

## 7. Scope firewall and workspace disclosure

- No GGV family, live polygon, degree cutoff, or farm output is consumed in
  the mathematical conclusions above.
- No statement here promotes the filed Sigray Proposition 4.2 gap, later
  unaudited sheet package, `G2-BD`, full landing, `RPMC`, a type cap, or JC2.
- Only this xmodel report was created; no canonical file was edited.
- No heavy computation or AWS resource was used.
- A broad read-only `rg` command from the repository root unintentionally
  traversed the nested `jc2-lean` directory and surfaced a few grep snippets
  before the scope error was noticed. None of that material is used or cited
  here. No `jc2-lean` status, build, or modification was performed; all later
  reads were restricted to named non-Lean files.

## 8. Final answer

Starting from the whole exact normalized pair, **source, both infinity
charts, all boundary places, and intrinsic pole paths are already
available**. The pure bypass therefore dominates a new GGV anti-standard
source theory for coverage. Its first serious missing mathematics is not
another chart: it is control of the nonproportional exits on a common
resolution.

VGG Section 7 supplies the proportional anti-side corridors. The clean next
interface is `C74-PLACE`; the clean next numerical theorem is
`EXIT-RPMC(C)`. The new finite-end balance shows simultaneously that a direct
pole-saturation contradiction is possible in principle and that a pole-only
book is not a complete all-boundary model. A full anti-standard
complete-chain theorem should not block either attack.
