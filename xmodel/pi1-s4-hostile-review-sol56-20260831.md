# Hostile review: PI1-S4 decision report

## 0. Integrity, sources, and verdict key

**Integrity — CONFIRMED.** Before either input was read, `shasum -a 256` returned

```text
010330d208c5899ce41832f1187b73d9a63268725d809b0370f2b4d9cd66eadd  pi1-s4-decision-opus5-20260831.md
bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963  block-descent-a1-b0-coordinator-integration-fable5-20260831.md
```

These are the charged values. I then streamed, without retaining a workspace copy, the
official Numdam PDF [M. V. Nori, *Zariski's conjecture and related problems*, Ann. Sci.
ENS 16 (1983), 305–344](https://www.numdam.org/item/ASENS_1983_4_16_2_305_0.pdf).
It is 4,546,575 bytes and hashes to
`1b848c19dcaaa016ff8070a7843cfd89db70cbbec3ce13cd9de080074739cc45`, exactly as
charged. “CONFIRMED” below means the printed claim and scope follow; “GAP” means the
claim may be true but the printed proof omits a needed argument or hypothesis;
“REFUTED” means the printed claim or inference is false. A corrected, explicitly
conditional replacement is not a promotion of the original statement.

## 1. Normalization and affine topology

1. **Shear/swap WLOG (charged lines 49–54) — CONFIRMED.** The coordinate functions on
   the normalization are polynomials. If their degrees agree, subtracting the ratio of
   leading coefficients drops one degree; swapping then gives `d=deg p>n=deg q`. If the
   lower coordinate becomes constant, birationality gives
   `C(t)=C(p(t))`, hence `deg p=1`; this is the line case and cannot have an `S_4`
   quotient.
2. **Degree and proper vertical projection (55–60) — CONFIRMED.** A generic affine line
   pulls back to a degree-`d` polynomial and the parametrization is birational, so
   `deg D=d`. The unique point at infinity is `[1:0:0]`; equivalently the degree-`d`
   leading form is a nonzero multiple of `Y^d`, so the centre `[0:1:0]` of the
   `x`-projection is not on the closure. Thus `x|_D` is finite (hence proper), of degree
   `d`.
3. **Place data (61–68) — CONFIRMED.** In the stated chart,
   `ord_s(v)=d-n=:a<d=ord_s(u)=:b`. Therefore the branch multiplicity is `a` and its
   intersection multiplicity with `L_infinity={u=0}` is `b=d`; it is smooth exactly when
   `a=1`.
4. **Genus identity (70–76) — CONFIRMED.** The compact normalization is `P^1`, the
   arithmetic genus of a degree-`d` plane curve is `(d-1)(d-2)/2`, and an
   `A_{2k-1}` made of two smooth branches has `delta=k`. This gives (G), including
   `s<=delta_aff`.
5. **Immersion and (V) (78–87) — CONFIRMED, with a later-use qualification.** A point at
   which both derivatives vanish would give multiplicity at least two on that
   normalization branch. At a smooth image point the normalization is locally an
   isomorphism, and at each allowed singularity both branches are smooth. Hence `gamma`
   is indeed immersive everywhere. Extending `p` to `P^1 -> P^1`, infinity contributes
   ramification `d-1` to the total `2d-2`; equivalently `deg p'=d-1`. Thus finite vertical
   ramification counted with multiplicity is `V=d-1`. It is not automatically `d-1`
   *distinct simple* tangencies. The simple-factor arguments in §§2 and 5, and the
   factor-count wording in §3's exponent check, silently need a generic affine choice of
   `x=p+lambda q` (which preserves the degrees and place data) to make finite ramification
   simple, its values distinct, and the projection transverse to every singular branch.
   Such a choice exists, so this is a repairable omitted setup hypothesis, not a failure
   of (V). Theorem B does not need this choice.
6. **(A) (89–98) — CONFIRMED.** For an irreducible affine plane curve the meridians give
   `H_1(C^2-D;Z)=Z`. If the fundamental group is abelian it equals this abelianization,
   hence is `Z` and has no quotient `S_4`.

## 2. Local braids and the van Kampen presentation

1. **Vertical tangency (charged 122–129) — CONFIRMED** once the generic projection
   specified in §1 above is made. The half-twist Artin action gives two equivalent fixed
   relations, `xi_i=xi_{i+1}`.
2. **`A_{2k-1}` braid and relation (131–144) — GAP as written; corrected claim
   CONFIRMED** under the likewise necessary transversality of the vertical `x`-fibre to
   both branches (so `x` is a local parameter on each). The difference of the two graph
   functions has a zero of order `k`; its full winding is `sigma_i^(2k)`. With
   `w=xi_i xi_{i+1}`, `sigma_i^(2k)` conjugates both generators by `w^k`. The two fixed
   relations are equivalent to the single relation
   `[(xi_i xi_{i+1})^k,xi_i]=1`, since commutation with `xi_i` and `w` also gives
   commutation with `xi_{i+1}=xi_i^(-1)w`.
3. **Disjointness verdict (146–152) — CONFIRMED.** Disjoint transpositions commute, so
   they satisfy the stronger nodal relation. Consequently they satisfy every `(N_k)`;
   parity of `k` is immaterial. This is a valid representation-level strengthening, not
   an assertion that the source local groups coincide.
4. **Affine ZvK presentation and infinity (104–117) — CONFIRMED, but the explanation is
   compressed.** For a generic finite linear projection, affine Zariski–van Kampen gives
   the displayed quotient of the free group by all finite critical-fibre monodromies.
   There is no additional relation on the boundary word in `pi_1(C^2-D)`. The relation
   filling that boundary word belongs to the projective complement. Properness of
   `x|_D` is the relevant “no finite escape to fibre-infinity” hypothesis; properness
   alone is not a derivation of the theorem, and genericity/transversality must also be
   stated. With those standard repairs, the affine/projective distinction in lines
   114–117 is right.
5. **“All singular-point data are invisible” (154–160) — CONFIRMED only at the target
   tuple.** A conjugated local factor fixes the `S_4` tuple because its corresponding
   local meridians have disjoint images. This does not erase the relation in the source
   group, but it is exactly what the later representation obstruction needs.

## 3. Theorem A

1. **Hurwitz framework (charged 166–176) — CONFIRMED.** Applying `phi` to the Artin
   action turns every ZvK fixed-word relation into fixedness of the transposition tuple.
   Hurwitz moves preserve both the ordered product `Pi` and the subgroup generated by the
   entries. Hence a monodromy product, in particular the large-circle braid, also fixes
   the tuple.
2. **Infinity braid (178–197) — GAP as written; corrected claim CONFIRMED on
   `gcd(d,n)=1`.** A torus-knot closure by itself does not prove conjugacy of braids.
   The missing direct argument is short: write the solutions of
   `p(t)=R exp(i theta)` as
   `t_j=A R^(1/d) exp(i(theta+2 pi j)/d)(1+o(1))`, uniformly in `theta`. Then
   `q(t_j)=B R^(n/d) exp(i n(theta+2 pi j)/d)(1+o(1))`. Coprimality makes the leading
   points uniformly distinct, so for sufficiently large `R` the error can be homotoped
   away inside the configuration space. This proves, more strongly than merely comparing
   closed links, that the braid is conjugate (initial labelling accounts for the
   conjugacy) to `delta^n`. For a conjugate `h delta^n h^(-1)`, replace the tuple by
   `h^(-1).T`; its product and generated subgroup are unchanged. Thus braid conjugacy is
   sufficient for the proof. The exponent-sum check is also correct:
   `(d-1)+2 delta_aff=n(d-1)`, using the one-pair infinity delta invariant available under
   coprimality.
3. **Action formula (204–212) — CONFIRMED.** With the report's left Hurwitz convention
   and right-to-left word action, at `d=3`
   `(a,b,c) -> (abc b^(-1)a^(-1),a,b)=(Pi c Pi^(-1),a,b)`; at `d=4` it is
   `(a,b,c,e) -> (abce c^(-1)b^(-1)a^(-1),a,b,c)=(Pi e Pi^(-1),a,b,c)`.
   The same cancellation proves the formula for all `d`, and its `d`th power conjugates
   every entry by `Pi`.
4. **Theorem A(1) (214–227) — CONFIRMED.** Fixedness under `delta^n` implies fixedness
   under `delta^(nd)`, hence conjugation by `Pi^n` fixes every entry. The entries generate
   `S_4`, whose centre is trivial, so `Pi^n=1`.
5. **Theorem A(2) (229–230) — CONFIRMED.** `Pi` has sign `(-1)^d`; taking signs in
   `Pi^n=1` gives `dn` even.
6. **Theorem A(3) (232–247) — CONFIRMED.** The extension
   `t_(j-d)=Pi t_j Pi^(-1)` makes `delta` the unit backward shift. Fixedness supplies
   `n`-periodicity; because `gcd(d,n)=1`, conjugation by `Pi` runs through one full orbit
   of the `n` entries. That orbit generates `S_4`. Identity, transposition, and double
   transposition conjugators have orbits of size at most two. A 3-cycle works only on the
   three edges joining its fixed letter to its cycle, and a 4-cycle works on an adjacent
   edge orbit (not on its diagonal orbit). Thus the actual `Pi` has order 3 or 4. The
   order, sign, and minimal three-transposition generating set give exactly the two cases
   printed and `n>=3`, `d>=4`.

**Theorem A recommendation: PROMOTE at its stated coprime scope**, after making both the
generic-projection setup and the uniform asymptotic infinity-braid isotopy explicit. It is
not a theorem off the coprime stratum.

## 4. Theorem B and Nori's Proposition 3.27

1. **Primary-source statements (charged 257–279) — CONFIRMED.** Journal p. 331
   (PDF p. 28) states Proposition 3.27 with the hypotheses: `D` and `E` are curves on the
   smooth projective surface `X` and meet transversally; `D` is nodal; and
   `C^2>2r(C)` for every irreducible curve `C` contained in `D`. Its conclusion is exactly
   that the displayed kernel is abelian and its centralizer has finite index. Definition
   3.25 and the nodal remark on journal p. 330/PDF p. 27 are also transcribed faithfully.
   Nori defines `r(C)` as the number of singular points, hence the node count here. The
   journal-p. 307/PDF-p. 4 acknowledgement does say that blowing up cusps and applying
   3.27 gives the `C^2>6b+2a` criterion. This is corroboration, not an additional
   hypothesis.
2. **Surface identities (281–293) — CONFIRMED.** Taking `B_infinity` to mean the reduced
   support of the total inverse image, deleting it undoes all blow-ups over the line and
   gives `X'-B_infinity = C^2`; deleting `C'` as well gives `C^2-D`. The terminal
   log-resolution condition makes `C'` meet `B_infinity` once, transversely, at a smooth
   point. The self-intersection and genus-drop formulas, including multiplicity-one
   separation blow-ups, are correct.
3. **Lemma 4.3 (295–301) — CONFIRMED.** Since
   `N_infinity=2 delta_infinity+M_infinity`, genus adjunction gives
   `C'^2-2 delta_aff=3d-2-M_infinity`. Positivity is therefore equivalent, integrally, to
   `M_infinity<=3d-3`. The parenthetical `K_X'.C'<=-3` is the same inequality.
4. **Lemma 4.4 recursion (303–327) — CONFIRMED, with one base-case clarification.** For
   `a=d-n`, `b=d`, coprimality means the Euclidean multiplicity recursion reaches the
   terminal boundary corner. For `b>a`,
   `M(a,b)=a+M(a,b-a)` and `N(a,b)=a^2+N(a,b-a)`, with swapping when needed. At the
   *terminal corner reached during this resolution*, the final multiplicity-one blow-up
   has `M(1,1)=N(1,1)=1`; this yields `M=a+b-1` and `N=ab`. An initially transverse
   `(1,1)` pair would need no blow-up, but cannot be the initial pair here because
   `d>n>=1`. All seven listed sequences have the claimed sums and square-sums. For
   `a=1`, there are `d` multiplicity-one centres, so `M=N=d`. Thus
   `C'^2=nd` and `C'^2-2 delta_aff=n+d-1` are correct.
5. **Full hypotheses of 3.27 (329–339) — CONFIRMED.** `X'` is smooth projective.
   `D_Nori=C'` is the sole component subject to the numerical test: it is irreducible,
   nodal in the affine chart, and smooth at infinity. The exceptional curves and strict
   transform of `L_infinity` lie in `E=B_infinity`, so Proposition 3.27 does **not** ask
   for their self-intersections to exceed node counts. Nori permits a reducible `E`; here
   it is SNC, and `C'` avoids its crossings and meets one component transversely. Finally
   `nd>(n-1)(d-1)=2r(C')`, with slack `n+d-1`.
6. **Endgame — CONFIRMED.** The target of Nori's map is
   `pi_1(X'-B_infinity)=pi_1(C^2)=1`; its kernel is therefore the whole affine-complement
   group and is abelian. Section 1 then identifies it with `Z`.

**Theorem B recommendation: PROMOTE exactly for the coprime, ordinary-node subclass.**
It does not cover tangential double points without the separate §5 argument.

## 5. Theorem C and specialization

1. **Tangency-blow-up fallback (charged 354–369) — CONFIRMED.** For an
   `A_{2k-1}`, `k>=2`, each of the `k` centres has strict-curve multiplicity two; the last
   blow-up separates the triple boundary meeting. Putting these exceptionals in Nori's
   `E` costs `4k` in self-intersection and removes that singularity from `r(C')`.
   `C^2` minus finitely many blown-up centres remains simply connected. The strict
   inequality is exactly the integral condition `2K_tac<=n+d-2`. This proves only the
   printed sufficient subclass `(B')`.
2. **Parameter space and Lemma 5.3 (371–380) — CONFIRMED.** If the map had generic degree
   `e>1`, its one-pole function-field factor gives a polynomial right factor of degree
   `e`, forcing `e` to divide both `d` and `n`; coprimality makes every member birational.
   Exact leading degrees give infinity orders `(d-n,d)`. Since these are coprime, the
   first characteristic exponent already ends denominator shedding, so
   `delta_infinity=(d-n-1)(d-1)/2`; genus then gives the stated constant `delta_aff`.
3. **Lemma 5.4 (382–393) — CONFIRMED, although the printed count is terse.** For a fixed
   parameter, the two derivative equations use independent coefficient blocks. For fixed
   distinct `t_1,t_2`, degree at least three makes the two-point Hermite evaluation map
   (values and first derivatives) surjective; after the two value-equality equations, the
   tangent determinant is therefore not identically zero. This gives three independent
   equations over a two-dimensional pair space. At three distinct parameters, evaluation
   differences have rank two in each coordinate block, hence four equations over a
   three-dimensional parameter space. The three incidence images have codimension at
   least one. Birationality plus immersion, transverse double fibres, and absence of
   triple fibres leaves precisely ordinary nodes. Thus the nodal locus is dense, and a
   nodal member can be chosen arbitrarily close to the given map (also in the open locus
   where the fixed `x`-projection has separated critical values).
4. **Lemma 5.5 (395–400) — GAP as written; corrected local conservation is valid.**
   Constancy of the *global* delta sum alone does not allocate `k_p` nodes to each old
   singularity. Choose disjoint normalization discs about the two preimages `a_p,b_p`.
   In their ordered product, the two equations
   `gamma_t(z)=gamma_t(w)` have an isolated zero at `(a_p,b_p)` of intersection
   multiplicity `I(B_1,B_2;p)=k_p`. After choosing a boundary free of zeros, local
   conservation of intersection number gives exactly `k_p` reduced zeros for a generic
   nodal fibre. Reversing the ordering gives the symmetric copy; “the single pair” in the
   report must mean one chosen ordering. Summing these local counts and using Lemma 5.3
   excludes extra nodes or loss to infinity. This supplies the missing proof.
5. **Lemma 5.6, tube and `B_2` (402–415) — GAP in setup; corrected argument
   CONFIRMED.** First make the generic shear described in §1 and choose the nearby nodal
   member generically enough that all relevant critical values are distinct. Around an
   old tangency the two normalization discs are then graphs over one `x`-disc and form an
   isolated two-sheet tube. A common trivialization embeds one fixed `B_2` in `B_d`.
   Every transverse holomorphic crossing contributes the positive full twist
   `w sigma^2 w^(-1)`; conjugations caused by paths inside the tube vanish because
   `B_2=Z`. Its `k` factors impose the single commutator, whereas the special boundary
   braid imposes only the `(N_k)` relation. Boundary isotopy identifies all factors
   outside these clusters.
6. **Presentation `(*)` and direction (416–420) — CONFIRMED after those repairs.** The
   nodal commutator implies the old `sigma^(2k)` fixedness relation, so the nearby group is
   the quotient of the special group by the added commutators:

   ```text
   pi_1(C^2-D_0)  --surjective-->  pi_1(C^2-D_t).
   ```

   This is the usual specialization direction. It is also the direction needed for
   factorization: a homomorphism from the special group that kills the new relators
   descends to the nearby group.
7. **Final contradiction (422–442) — CONFIRMED.** The original disjoint-transposition
   condition kills every added commutator. The descended map remains surjective, while
   Theorem B makes its nodal source group abelian, impossible for a surjection to `S_4`.

**Theorem C recommendation: PROMOTE only with the explicit generic-projection and local
intersection-conservation repairs above.** Its statement and quotient direction are
sound; the two gaps are in the charged proof, not counterexamples to the theorem.

## 6. Scope discipline

1. **Coprime Main-Theorem scope and the campaign's `D_1` (charged 448–484) —
   CONFIRMED.** The actual theorem and decision repeatedly say “on `(C1)`.” Lines 479–484
   expressly state that the coordinator has not supplied `(C1)` for `D_1` and that this is
   not a promotion of the campaign closure. Thus the report does **not** discharge the
   unrestricted residual for that curve.
2. **The Puiseux-pair equivalence (457–458 and 554–556) — REFUTED.** `(C1)` is equivalent
   to `gcd(d-n,d)=gcd(d,n)=1`, and it implies that the displayed first order pair is
   already primitive. It is **not** equivalent to “the place has exactly one Puiseux
   pair,” nor does failure imply two or more pairs. The report's own example
   `gamma(t)=(t^4,t^2+t)` has initial orders `(v,u)=(s^2+s^3,s^4)` and gcd two, but after
   the analytic coordinate change `u'=u-v^2` one has `ord(u')=5`; the branch is of type
   `(2,5)` and has one Puiseux pair. Correct statement: `(C1)` says no later series term or
   coordinate cancellation is needed to finish denominator shedding.
3. **Claimed three `(C1)`-independent gains (484–490) — REFUTED for one entry.** The §2
   local relation is independent of infinity, and Lemma 4.3 is a general numerical
   equivalence. Theorem A is not `(C1)`-independent: its statement assumes coprimality and
   its proof uses `rho_infinity~delta^n`; §9 itself says the proof does not transcribe off
   `(C1)`. Off-stratum unconditional facts include only such weaker items as the
   `d`-cycle permutation at infinity and `V=d-1`, not Theorem A's conclusions.

Accordingly the campaign caveat itself is respected. Separately, the later “regardless
of `(C1)`” gain list contains a false scope claim. That sentence and the Puiseux-pair
gloss must be corrected before promotion.

## 7. Residual typing

1. **`(M-INF)` equivalence (charged 558–568) — CONFIRMED with nodal scope retained.**
   Lemma 4.3 gives
   `C'^2-2 delta_aff=3d-2-M_infinity`; integrality makes strict positivity equivalent to
   `M_infinity<=3d-3`. This supplies Nori 3.27 directly only for the ordinary-node version
   of Theorem B. Tangential curves still need the extra affine blow-ups or a valid
   nodalization/extension.
2. **Worked `(d,n)=(4,2)` example (569–576) — CONFIRMED.** At infinity
   `(v,u)=(s^2+s^3,s^4)`. The analytic change `u'=u-v^2` exposes type `(2,5)`, while the
   literal boundary is still `u=0`; resolving the branch-boundary pair has multiplicities
   `2,2,1,1`. Thus `M=6`, `N=10`, and `C'^2=16-10=6`. The arithmetic genus and infinity
   delta give one affine node, so `6>2`. This example simultaneously refutes the report's
   “noncoprime iff multiple Puiseux pairs” gloss.
3. **Fork `(ii-a)/(ii-b)` (578–589) — GAP in `(ii-a)` wording, correctly OPEN in
   status.** A merely named locally closed subset containing `D`, constant
   `delta_infinity`, and generically nodal is insufficient if `D` lies on the wrong
   component or the generic points are not locally reachable. The needed input is an
   actual one-parameter deformation through `D` (or an irreducible component through it)
   with nearby nodal, birational fibres and controlled/equisingular branch-boundary data
   at infinity. Arm `(ii-b)` is accurately described as a proposed strengthening of
   Nori, not something proved by 3.26.
4. **“The criterion decides that curve” (591–594) — REFUTED as a biconditional gloss.**
   `C'^2>2s_1+4K_tac` is a sufficient NO criterion. Its failure supplies no YES and leaves
   the curve open.
5. **Successor cable/block paragraph (596–606) — CONFIRMED AS A HYPOTHESIS ONLY.** Its
   premises—compatibility of block products with the cabled Hurwitz action and
   centerlessness of the block-product subgroup—are expressly unproved. No current
   result may consume the proposed conclusion `Pi^q_1=1`.

The safe residual is therefore `OPEN[PI1S4-NONCOPRIME]`. For the proposed
Nori/nodalization route, `(M-INF)` plus a correctly formulated nodalization or an
applicable Nori extension are still required; a different future route is not excluded.

## 8. Promotion recommendation and corrected statements

**Overall verdict:** the Main Theorem is mathematically sound on the strict coprime
condition `(C1)`, but the charged report is **not promotable verbatim**. Its conclusion can
be promoted with the proof repairs in §§1, 3, and 5 of this review and with the false scope
glosses deleted. It does not settle the coordinator's unrestricted `D_1`.

| Result | Gate | Exact safe scope |
|---|---|---|
| Theorem A | **PROMOTE AS CORRECTED** | A curve as in §1 (irreducible polynomial curve, normalization `A^1`, one place at infinity), `d>n>=1`, `gcd(d,n)=1`, and a surjective meridian-transposition representation. The conclusions `Pi^n=1`, the parity obstruction, `n>=3`, and the order-3/order-4 fork are valid. Add the uniform asymptotic braid isotopy and choose a generic projection. |
| Theorem B | **PROMOTE** | Irreducible polynomial curve, normalization `A^1`, one place at infinity, `(C1)`, and only ordinary affine nodes. Then `pi_1(C^2-D)=Z`. Nori 3.27 is fully applicable. |
| `(B')` | **PROMOTE as sufficient only** | Same coprime class with tangencies and `2K_tac<=n+d-2`; then the group is abelian. No converse is asserted. |
| Theorem C | **PROMOTE AS CORRECTED** | Same coprime class, all affine singularities double points of two smooth branches, tangency allowed. The specified `S_4` representation does not exist. Insert generic-projection control and replace Lemma 5.5 by local intersection-number conservation. |
| Main Theorem | **PROMOTE AS CORRECTED, coprime-stratum representation-level only** | Exactly Theorem C's scope. It is not an unconditional rank-four campaign closure unless `(C1)` is separately proved for the campaign curve `D_1`. |
| Noncoprime residual | **OPEN** | Neither Theorem A nor Theorem C currently extends. `(M-INF)` and a valid arm `(ii-a)` or `(ii-b)` remain missing. |

The corrected Main-Theorem hypothesis should read:

> After an affine coordinate normalization write `gamma(t)=(p(t),q(t))` with
> `d=deg p>n=deg q>=1`. Assume `gcd(d,n)=1`; equivalently,
> `gcd(mult_Q(Dbar), I(Dbar,L_infinity;Q))=1`. Then no stated `S_4`
> representation exists.

Delete “equivalently, exactly one Puiseux pair.” Replace Lemma 5.5 by the ordered
normalization-disc intersection argument in §5.4 of this review. Before all braid
factorizations, insert a generic shear making singular branches transverse to the
projection, finite ramification simple, and critical values distinct. Replace the
“three `(C1)`-independent gains” sentence by: the §2 local verdict and Lemma 4.3 are
`(C1)`-independent; Theorem A is a coprime-stratum theorem. Finally, describe the §9
inequality only as a sufficient NO test and strengthen `(ii-a)` to an actual deformation
through the given curve.

<!-- BODY-END -->
