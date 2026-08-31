# Hostile review: NORI-BC report (Opus)

## 0. Integrity, scope, and sources

All three frozen inputs were hashed before they were read beyond their headings.  The
results match the charge exactly:

```text
64bcabd1e14d69026cc86e101ff266a92009c7f15e9dfc00dce88fb607e7560f  nori-bc-extension-opus5-20260831.md
aa41551f14f34bdae34d9f172be253882f67c8cc3c6cc699ed98b5b85bbc60f0  pi1s4-close-residual-hostile-review-sol56-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
```

Nori was independently streamed again from the official NUMDAM PDF,
`https://www.numdam.org/article/ASENS_1983_4_16_2_305_0.pdf`: 4,546,575
bytes, 41 PDF pages, SHA-256
`1b848c19dcaaa016ff8070a7843cfd89db70cbbec3ce13cd9de080074739cc45`.
This is the charged hash.  Journal page `p` is PDF page `p-303`.  I checked the
formula-bearing passages against page images, not just the defective OCR.  As an
independent check on the conic example I also streamed Amram--Garber--Teicher,
*On the fundamental group of the complement of two tangent conics and an
arbitrary number of tangent lines*, arXiv:math/0612346v2, SHA-256
`7287c49c82b1c592245d866aa6e8adaebedfe180af1df092280fa1ccfd5a44cc`;
its Proposition 3.6 is directly on point.

Verdicts below distinguish a false conclusion (`REFUTED`), a correct result with a
literal or scope repair (`CONFIRMED-AS-CORRECTED`), and a genuinely missing
argument (`OPEN`).  Overall: **Theorem N-A and N-A-RES are sound and promotable
after small statement/proof repairs; the charged report is not promotable
wholesale.**  In particular, only one of its alleged two “Nori errata” is an
erratum in Nori.

## 1. Nori §1: verbatim consumption and claimed errata

**Quoted-text verdict: CONFIRMED, apart from the report's characterization of
(E1).**  The following page-by-page comparison exhausts the quotations in charged
§1.

- Journal pp. 305--306 print WLT with `H` connected compact analytic (possibly
  nonreduced), locally principal, `O_U(H)|_H` ample, `q` holomorphic and locally
  invertible, and `R` arbitrary closed.  Parts A, B, and C have exactly the
  finite-index, disjointness `q(H) cap R = empty`, and
  `(Div h)^2/H^2` content quoted.  Page 306 also defines `r(C)` as the number of
  singular points of the curve `C` itself and states the finitely-generated form
  of II.
- Journal p. 310 prints Fact 1.4 B exactly with `S` smooth and `N` a
  normal-crossings divisor near `S`; its conclusion is that the meridian class
  `gamma(S)` is central in `pi_1(U-N)` and hence a singleton.
- Journal p. 330 prints Definition 3.25, Proposition 3.26, and the nodal remark
  with the charged meanings.  Page 331 prints the branch-separation construction,
  `(F.H)=C^2-B(C)`, `H^2=B(C)`, Proposition 3.27, and the quoted first and second
  halves of its proof.  Journal pp. 332--333 print Lemmas 5.1--5.2 and the
  transverse-intersection calculation used in charged §2.  Journal p. 315 prints
  Corollary 2.5 with the additional printed condition that `D` and `E`
  intersect transversely.
- Journal p. 336 prints the resolution definition
  `s=G.(G+2F)`, Proposition 6.5, the node sentence in Remark 6.6, the cusp value
  `6`, and the Zariski sextic statement exactly as quoted.

There are two qualifications.  First, “`O_U(H)|_H` ample iff `H^2>0`” is safe in
the actual 3.27 use, where `H` is one smooth irreducible normalization.  It is not
a blanket equivalence for an arbitrary reducible/nonreduced `H` in WLT: ampleness
must be checked componentwise.  Second, the normal-bundle language outside the
immersed case needs the correction in §2 below.

**(E1), factor 2: REFUTED-AS-AN-ERRATUM.**  The p. 330 image unambiguously reads

```text
A(C;P) = 2 sum_{i<j} length(A/(f_i,f_j)),
B(C)   = C^2 - sum_P A(C;P).
```

Thus Nori's print is right: a node has `A(C;P)=2`.  If an earlier lane gloss put
the `2` outside the second displayed formula, that gloss needed correction; Nori
did not.  The charged report thereafter uses the correct net value
`B=C^2-2 sum I(f_i,f_j)`, so this labeling error does **not** move N-A's
numerics.

**(E2), `s(node)`: CONFIRMED genuine misprint.**  Remark 6.6 visibly prints
`s(C;P)=2` and, in the same sentence, the condition `C^2>4r(C)`.  Resolve a node
once.  With exceptional curve `E`, total exceptional part `G=2E`, strict
transform `F`, `E^2=-1`, and `F.E=2`, Nori's own definition gives

```text
s = (2E).(2E+2F) = -4+8 = 4.
```

Equivalently the blow-up drops the strict transform's square by `2^2=4`.
Nori's printed inequality and Example 3.19(C) are therefore consistent with
`s(node)=4`, not `2`; Example 6.7's cusp value `6=2^2+1^2+1^2` is a further
check.  Promote only this second item as a Nori erratum.

## 2. Transversality consumption and the normal-bundle bound

**Location verdict: CONFIRMED-AS-CLARIFIED.**  There are exactly two
top-level gateways in the proof of 3.27.

1. On p. 331 Nori invokes Fact 1.4 B for the normalization `H` and says that
   `H` meets the closure of `q^{-1}(R)-H` transversely.  This uses smoothness of
   every local branch of `D`, transverse self/cross intersections in nodal `D`,
   and transverse `D cap E`; charged §2 mentions only the self-node picture.
2. The abelianness half invokes Lemma 5.2.  Its p. 333 proof applies Lemma 5.1,
   where nodality and etaleness make `A` meet the residual pullback divisor
   transversely and give `(A.R)=2r(B)-2r(A)`.  Nested inside the same gateway,
   Lemma 5.2 also uses the local tame normal-crossing facts that inertia is
   abelian and that the inverse image of each analytic branch stays analytic.

Thus “two places” is right if it means two invocation sites in 3.27, but N2 is
not just one numerical identity.  Producing a genuinely nodal `D~` transverse to
`E~`, as N-A does, discharges all these subuses.  Repairing only the first
central-meridian argument would not.

**Normal-degree verdict: correct at N-A's smooth-branch scope, overclaimed in
general.**  If `h:Cbar -> X` is the normalization map of a nodal curve, it is an
immersion and its normal line bundle has

```text
deg N_h = C^2 - 2 delta(C) = C^2 - 2r(C).
```

The same holds for any curve all of whose analytic branches are smooth, including
the `A_{2k-1}` points used in N-A.  Here
`delta_P=sum_{i<j} I_P(f_i,f_j)`, so Nori's branch separation is smooth and

```text
H^2 = B(C) = deg N_h.
```

For arbitrary branches the charged formulas still give the useful formal
comparison

```text
B(C) - (C^2-2 delta(C)) = 2 sum_{P,i} delta(f_i) >= 0,
```

with equality exactly when every branch is smooth.  But charged (2.1) should not
call the second term the degree of a *normal bundle* without qualification.  At
a cusp the normalization is not immersive; its normal cokernel has torsion and
there is no honest normal line bundle.  Moreover the `H` in Nori 3.26 is the
possibly singular branch-separation curve with local rings `A/(f_i)`, not the
normalization.  What Nori actually proves there is `H^2=B(C)`.  One may define a
coherent normal sheaf (including torsion) whose Euler degree is
`C^2-2delta`, but that is not the WLT divisor `H` and does not justify the claimed
general “run the 3.26 computation with `H=Cbar`.”

This correction strengthens, rather than weakens, the hostile conclusion about a
naive general-singularity extension.  It does not alter N-A, whose branches are
smooth and whose normalization maps are immersions.

## 3. Local blow-ups and kernel invariance

**Lemma 3.1: CONFIRMED-AS-CORRECTED.**  Straighten the two branches to
`b_1:{y=0}` and `b_2:{y=x^k}`.  After `j` blow-ups, `1<=j<k`, the continuing
chart is

```text
y=x^j y_j,       b_1:{y_j=0},       b_2:{y_j=x^(k-j)},       E_j:{x=0}.
```

The next common point lies on `E_j` but not on `E_{j-1}'`; thus every center
*after the first* is a free point on exactly one exceptional.  For `k>=2`, after
`k-1` steps the three lines `y_{k-1}=0`, `y_{k-1}=x`, and `x=0` form an ordinary
triple point.  The last blow-up records their three distinct tangent directions
as three distinct points of `E_k`.  The final reduced exceptional configuration
is

```text
E_1(-2) -- ... -- E_{k-1}(-2) -- E_k(-1),
```

and the two branch arrows meet `E_k` transversely at two further distinct
points.  In particular the strict branches avoid every exceptional-chain node.

The requested endpoint checks are:

- `k=1`: blow up once.  In a direction chart the two strict branches meet
  `E_1` at the distinct directions of `y=0` and `y=x`, transversely.  There is
  no `E_0` and no pre-blow-up triple-point clause.
- `k=2`: the first chart `y=xv` has `v=0`, `v=x`, and `E_1:{x=0}` at an
  ordinary triple point.  Blowing it up gives branch points `w=0,1` on `E_2`;
  `E_1'` meets `E_2` at the third (infinite-direction) point.  Hence
  `E_1'^2=-2`, `E_2^2=-1`.

The germ has multiplicity `2` at each of its `k` centers.  A self-point of one
irreducible component therefore costs `4k` in its self-intersection; at a
cross-point each participating component is smooth at every center and costs
`k`.  The same multiplicity sequence gives
`s(A_{2k-1})=sum_{1}^{k}2^2=4k` (`4` for a node, `8` for a tacnode).
Thus the mathematics of the lemma is right, but “every centre” must become
“every centre after the first,” and the triple-point clause must be restricted
to `k>=2` with `k=1` stated separately.

**Lemma 3.2: CONFIRMED.**  For a blow-up at `p in D`, with the exceptional
assigned to `E_tot`, blow-down is a space isomorphism

```text
X~-(D~ union E~ union Exc)  ~=  X-(D union E).
```

On the target side it identifies `X~-(E~ union Exc)` with `(X-E)-{p}` if
`p notin E`, and with `X-E` if `p in E`.  Inclusion
`(X-E)-{p} -> X-E` induces a `pi_1` isomorphism: use a small real four-ball,
whose puncture retracts to the simply connected `S^3`, or general position.
The natural square therefore has vertical `pi_1` isomorphisms and identifies
the kernels (up to the harmless basepoint inner automorphism).  Iteration covers
both cases: the first center of a tangency is outside the old `E`, while later
centers lie on exceptionals already put into `E`.  The report correctly claims a
`pi_1` isomorphism, not a target-space isomorphism, in the first case.

## 4. Theorem N-A: proof assembly and numerical hypotheses

**Verdict: CONFIRMED-AS-CORRECTED; promote the theorem.**  Blow up `k_p` times
at every point with `k_p>=2`, put every exceptional into `E~`, and leave the
ordinary nodes untouched.  The checks needed for Nori 3.27 are all available:

- A finite sequence of point blow-ups of the complex smooth projective surface is
  again smooth and projective.
- Over every resolved point the strict branches are disjoint.  Hence `D~` has
  exactly the untouched ordinary double points and is nodal.
- Each resolved branch meets only the last exceptional `E_k`, transversely and
  away from its two other marked points; it misses the exceptional-chain nodes.
  At untouched nodes `E` is absent by (A2), and at original smooth points (A2)
  supplies normal crossings.  Thus `D~` and `E~` intersect transversely.  Notice
  that stopping after `k-1` blow-ups would leave the new node *on* the
  exceptional, so the final blow-up is essential.
- For every original irreducible component `C`, self-tangencies contribute
  `-4k` and tangencies to other components contribute `-k`.  Therefore

  ```text
  C~^2 = C^2 - 4T(C) - T_x(C),       r(C~)=r_1(C).
  ```

  Cross-points are not singularities of the individual component, tangential
  self-points have been resolved, and no new singularity of `C~` is created.
  The hypothesis of N-A is consequently exactly
  `C~^2>2r(C~)`.  The exceptional curves are in `E~`, not `D~`, so Nori imposes
  no impossible positivity condition on their negative squares.

Nori 3.27 now gives a finitely generated abelian kernel with finite-index
centralizer on the blown-up surface (finite generation is explicit in its proof
and in the p. 306 formulation).  Iterated Lemma 3.2 identifies that kernel with
the original one.  This also discharges both transversality gateways in §2, not
merely Fact 1.4 B.

The alternative numerical wording is correct.  At a self-`A_{2k-1}` point,
Nori's actual definition gives `A(C;p)=2k`; cross-component contacts do not enter
`B(C)` for the individual smooth component.  Hence

```text
B(C)=C^2-2r_1(C)-2T(C),
B(C)>2T(C)+T_x(C)  iff  C^2>2r_1(C)+4T(C)+T_x(C).
```

Three formal repairs should accompany promotion.  Work with reduced complex
curves; define `D_{!=C}` as the union of the other components rather than the
ambiguous set notation `D-C`; and either assume `D,E` have no common component
or begin by deleting from `D` every component already contained in `E`.  This
last deletion changes neither complement nor kernel.  Under (A2), a shared
component is smooth and disjoint from the remaining `D`, so all hypotheses on
the remainder persist.  The charged proof silently assumes this reduction, but
it is a repair, not a counterexample to the theorem.

## 5. Countermodels in §4

**Zariski sextic: CONFIRMED.**  Nori's own Example 6.7 (journal p. 336)
states that a general sextic `f^2-g^3=0`, with `deg f=3`, `deg g=2`, has six
ordinary cusps and

```text
pi_1(P^2-C) ~= (Z/2) * (Z/3).
```

Each cusp is unibranch, so the pairwise sum in Definition 3.25 is empty and
`B(C)=C^2=36>0`.  Since `P^2` is simply connected, the relevant kernel is the
whole displayed nonabelian group.  Its abelianization is `Z/6`, as independently
required for an irreducible degree-six projective curve.  This decisively refutes
the unrestricted replacement “nodal” by `B(C)>0`; even positivity of the
coherent normal-sheaf degree `36-2(6)=24` would not save it.

**Two bitangent conics: CONFIRMED by rederivation and source.**  For
`C_1:{zy=x^2}` and `C_2:{zy=lambda x^2}`, `lambda notin {0,1}`, Bezout is
concentrated at `[0:1:0]` and `[0:0:1]`, with contact two at each.  Thus the union
has two `A_3` points.  In the chart `x=1`, put `f(Y,Z)=YZ`.  For

```text
W = C^2 - {YZ=1} - {YZ=lambda},
```

the inverse image of `C-{0,1,lambda}` is explicitly
`C^* x (C-{0,1,lambda})`.  A small inverse image around `0` contracts by
`(Y,Z)->(Y,sZ)`.  Van Kampen therefore kills both the fibre loop `mu` and the
base loop `t_0`, leaving `pi_1(W)=F(t_1,t_lambda)`.

Restoring the line `x=0` kills its meridian.  On a generic transverse line
`Z=cY`, a loop around infinity sends under `f` to a large base loop traversed
twice; after `t_0=mu=1` this imposes

```text
(t_1 t_lambda)^2=1.
```

Consequently

```text
pi_1(P^2-(C_1 union C_2))
 = <a,b | (ab)^2=1> ~= Z * (Z/2),
```

which is nonabelian.  Its abelianization `Z direct-sum (Z/2)`
agrees with the degree relation `2a+2b=0`.  Amram--Garber--Teicher,
arXiv:math/0612346v2, Proposition 3.6 independently gives the same projective
group.  Here each `C_i` is smooth, hence `B(C_i)=C_i^2=4>0`, and again the
kernel is the whole group.

This example also proves the advertised sharpness with the exact scope claimed.
For each component, `r_1=T=0` and `T_x=2+2=4`; N-A's inequality is `4>4`, short
by one integral unit.  Replacing the coefficient of `T_x` by any number less
than `1` would make the hypothesis true while the conclusion is false.  It says
nothing about improving the coefficient `4` on *self*-tangencies; the report is
right to leave that as `OPEN[NORI-BC-SELF-TANGENT-COEFF]`.

## 6. Corollary N-A-RES and the \((6,3)\) residual table

**N-A-RES: CONFIRMED, with dependency and wording made explicit.**  With one
fixed convention including the terminal multiplicity-one centers of the infinity
resolution,

```text
C'^2=d^2-sum m_j^2,       2delta_infty=sum m_j(m_j-1),
M_infty=sum m_j.
```

Together with
`delta_aff+delta_infty=(d-1)(d-2)/2`, these identities independently rederive
the charged Lemma 4.3 consequence

```text
C'^2-2delta_aff = 3d-2-M_infty.
```

Here `C'` is smooth and transverse **at infinity**; it still has the stated
affine double points.  For those points `delta_aff=r_1+T`.  Since the divisor
`D=C'` is irreducible, there are no other components and `T_x=0`.  N-A's strict
condition becomes

```text
C'^2-2r_1-4T = 3d-2-M_infty-2T > 0,
```

or, integrally, exactly

```text
M_infty+2T <= 3d-3.
```

After the affine tangencies are blown up and their exceptionals are included in
`E~`, the target complement is `C^2` minus finitely many points, hence simply
connected.  Thus Nori's kernel is the whole `pi_1(C^2-D_1)` and is abelian.
For an irreducible affine plane curve its first homology is `Z`, generated by a
meridian, so the group itself is `Z`.  Every step of the asserted endgame is
therefore valid.

**The `(d,n)=(6,3)` table: CONFIRMED row by row.**  Here `a=d-n=3`.  On the
one-characteristic-pair branch at infinity, the first characteristic exponent
must satisfy `beta_1>6` and `3` does not divide `beta_1`; there is no additional
parity condition.  Since

```text
delta_infty=(3-1)(beta_1-1)/2=beta_1-1,
delta_aff=10-delta_infty=11-beta_1 >= 1,
M_infty=3+beta_1-1=beta_1+2,
```

the only exponents are `7,8,10`:

| `beta_1` | divisibility | `delta_infty` | `M_infty` | `delta_aff` | possible `T` | N-A-RES result |
|---:|:---:|---:|---:|---:|:---|:---|
| 7 | `3 does not divide` | 6 | 9 | 4 | `0,2,3,4` | gate `T<=3`; only `T=4` open |
| 8 | `3 does not divide` | 7 | 10 | 3 | `0,2,3` | gate `T<=2`; only `T=3` open |
| 10 | `3 does not divide` | 9 | 12 | 1 | `0` | closed |

`T=1` cannot occur because every tangential contribution has contact at least
two.  Accordingly, among these numerical configurations the only survivors are
exactly `(beta_1,T)=(7,4),(8,3)`.  This is a conditional row classification; it
does not assert that either surviving curve actually exists.

## 7. §6: refutation (ii-a) and remaining halves

Two preliminary route verdicts are secure, but should be stated narrowly.

**Local-transversality replacement: REFUTED in the form needed by 3.27.**  At
`y(y-x^k)=0` the local complement group has the meridian presentation

```text
G_k=<a,b | (ab)^k=(ba)^k> = <a,c | [a,c^k]=1>,  c=ab.
```

The element `c^k` is central, but quotienting by it gives
`Z*(Z/k)`.  For `k>=2` this quotient has trivial center and the image of `a` is
an infinite-order free generator, so no nonzero power of the branch meridian
`a` is central.  Thus Fact 1.4 B's meridian conclusion is locally false at a
tangency.  This kills the proposed direct local replacement, not every
conceivable different global proof.

**Proposition 3.26 substitution: REFUTED as a direct substitution.**  It requires
`C cap R=empty`.  For the desired complement, `R=C' union B_infty` contains
`C'`, so the map from its normalization into `X-R` is not defined.  Taking only
`R=B_infty` still violates disjointness because `C'` meets the boundary; even if
one ignored that defect, its target is the simply connected `C^2` and supplies
no information about meridians of `C'`.  This does not rule out an indirect use
of 3.26 with some auxiliary curve.

**The fixed-genus reduction in §6.1: CONFIRMED only on the birational,
fixed-degree locus.**  For a degree-`d` rational curve with one place at infinity,

```text
delta_aff+delta_infty=(d-1)(d-2)/2,
```

so either delta is constant iff the other is.  Because the infinity germ remains
unibranch, delta constancy also fixes its Milnor number.  If `P_{d,n}` means all
coefficient pairs rather than the birational locus, “every member has degree
`d`” is false: `p=t^6,q=t^3` has image `x=y^2`, of degree two.  Promotion must
state the locus.  The local theorem that the delta-constant stratum of a reduced
plane-curve singularity is irreducible with dense nodal open is standard and
supports the charged local half (Teissier, *Résolution simultanée I--II*, in
LNM 777 (1980), 71--146).  The primary NUMDAM scans fetched were
`https://www.numdam.org/item/SSS_1976-1977____A9_0.pdf` (SHA-256
`142540ba736a24aef507bd32d1c944d187896dd6de9b6929779b07a4586a0521`) and
`https://www.numdam.org/item/SSS_1976-1977____A10_0.pdf` (SHA-256
`00daab805010e3d615baef7dda5ab434ef348ccc34dea8e130f3767155c2aac4`).
What remains `OPEN[PI1S4-ES-SPREAD]` is a global
statement about the image of the parametrized family.  Surjectivity onto the
entire product of versal bases is stronger than necessary; dominance or
transversality along the product delta-stratum, meeting its nodal open, would
suffice.

**The delta-constant `pi_1` transport: REFUTED only as an unqualified
principle.**  Deform one conic in the bitangent pair of §5 generically.  The two
`A_3` points (total delta four) split into four transverse nodes (again total
delta four).  At the special fibre the projective complement group is
`Z*(Z/2)`.  At a nearby fibre Nori 3.27 applies to the two smooth conic
components and makes the group abelian; its first homology is
`Z direct-sum Z/2`.  Thus abelianness of the nearby complement cannot simply be
“transported back.”  A fixed generic line and Nori with that line as `E` gives
the analogous affine counterexample.  But this witness is reducible and is not
an irreducible one-place polynomial curve in the residual `P_{d,n}`.  It refutes
the report's unqualified inference, while a specially proved residual transport
theorem remains OPEN.

**Cover-level half: partly repaired locally, globally OPEN.**  Charged Lemma 6.6
correctly observes that disjoint transpositions satisfy every local
`A_{2k-1}` relation and every resulting node relation.  A compatibility model is
explicit: deform the branches `y=x^k` and `y=-x^k+2epsilon`; their `k`
intersections `x^k=epsilon` are transverse, and both old and new representations
factor through the two branch-linking numbers `Z^2`, sent to the same two
disjoint transpositions.  This proves local compatibility, not deformation or
gluing of the global branched cover over the outside piece.  The latter is
exactly `OPEN[PI1S4-COVER-DEFORMATION]`.  Neither OPEN may be promoted as a
transport theorem.

## 8. Verdicts and promotion recommendation

| Charged item | Verdict | Exact promotion scope |
|---|---|---|
| Nori quotations | **CONFIRMED** | Promote with the journal/PDF pages in §1. |
| Factor `2` in `A(C;P)` | **REFUTED as a Nori erratum** | Promote as a correction to the earlier gloss only. |
| Remark 6.6 `s(node)=2` | **CONFIRMED misprint** | Correct to `4`; the printed `C^2>4r(C)` is right. |
| `B(C)>=deg N_h` | **CONFIRMED-AS-CORRECTED** | Honest normal bundle for immersed normalizations; coherent normal sheaf including torsion in general. |
| Two transversality locations | **CONFIRMED-AS-CLARIFIED** | Two top-level gateways; Lemma 5.2 contains the extra tame/nodal subuses listed in §2. |
| Lemma 3.1 | **CONFIRMED-AS-CORRECTED** | Separate `k=1`; “after the first center”; triple clause only for `k>=2`. |
| Lemma 3.2 | **CONFIRMED** | Promote the natural `pi_1`-kernel identification. |
| Theorem N-A | **CONFIRMED-AS-CORRECTED** | Promote over complex smooth projective surfaces and reduced curves, with common components removed/forbidden and `D_{!=C}` defined.  Full finitely-generated abelian and finite-index-centralizer conclusion survives. |
| `T_x` coefficient `1` | **CONFIRMED sharp** | Sharp for cross-component tangencies, witnessed by the two conics. |
| N-A-RES | **CONFIRMED** | Promote together with the terminal-center version of Lemma 4.3; gate `M_infty+2T<=3d-3` implies `pi_1(C^2-D_1)=Z`. |
| `(6,3)` table | **CONFIRMED** | Close every numerical row except `(7,4)` and `(8,3)`. |
| Naive `B(C)>0` extensions | **REFUTED** | Both unrestricted singularities and the componentwise smooth-branch version are false. |
| Local Fact-1.4 replacement / 3.26 substitution | **REFUTED at stated direct scopes** | Do not promote broader impossibility claims about unrelated global or auxiliary-curve arguments. |
| Delta-constant `pi_1` transport | **REFUTED unqualified; restricted case OPEN** | The reducible conic witness does not decide the residual irreducible one-place family. |

There is one custody correction.  The supplied coordinator integration still
labels all CLOSE-derived material provisional; it does not itself support the
charged phrase `PROMOTED-CONSUMED` for Lemma 4.3.  The identity is independently
proved in §6 of this review, so it and N-A-RES may be promoted **now as a
package**, rather than described as previously coordinator-promoted.  The
`(6,3)` values can also be checked directly from terminal multiplicity sequences
`(3,3,1,1,1)`, `(3,3,2,1,1)`, and `(3,3,3,1,1,1)`, whose sums are `9,10,12`.

The following OPENs remain correctly typed after narrowing:

- **`OPEN[NORI-BC-SELF-TANGENT-COEFF]`.**  N-A proves the coefficient `4T` for
  self-tangencies; neither counterexample proves it optimal.  The first numerical
  gap is degree six.  An irreducible rational sextic with five tacnodes would
  have `delta=T=10`, `B=36-20=16>0`, while N-A asks `36>40`.  Existence of such a
  sextic and the abelianness of its complement are both unproved here.  It is an
  extremal test, not a witness.
- **`OPEN[M-INF-T]`.**  At `(6,3)` only `(beta_1,T)=(7,4),(8,3)` remain; no claim
  here repairs the charged `(6,4)` semigroup gap or settles all higher rows.
- **`OPEN[PI1S4-ES-SPREAD]`** and
  **`OPEN[PI1S4-COVER-DEFORMATION]`.**  The former needs the parametrized family
  to hit the nodal open of the product delta-stratum; the latter needs global
  deformation/gluing of the cover.  Local relation compatibility proves neither.
- **`OPEN[PI1S4-D1-DEGREE]`** remains unchanged and highest-leverage; nothing in
  N-A bounds the residual degree.

Final recommendation: **PROMOTE-AS-CORRECTED, not wholesale.**  The flagship
extension itself is sound, its residual gate and `(6,3)` gain are sound, and the
two countermodels are sound.  Hold the two overbroad deformation inferences,
the general normal-*bundle* wording, the claim of two printed Nori errata, and
all assertions beyond the exact OPEN scopes above.

<!-- BODY-END -->
