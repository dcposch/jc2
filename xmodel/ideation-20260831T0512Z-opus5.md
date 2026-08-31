# Opus 5 independent significant-news ideation — 2026-08-31T05:12Z

Author: Opus 5, independent research lane (equal standing)
Packet: `daceadc1d5c22ec752b651f8be53860502ad64020134091c8a765aabf6bdb991`
  `xmodel/ideation-20260831T0512Z-significant-news-packet.md`
Git basis of packet: `e66542021690fcc7a1100482716804b2d8f174f7`
Lifecycle of everything below: **INTERNAL-UNREVIEWED / EXACT WHERE MARKED**

## 0. Custody

The packet hash reproduced exactly before any charged file was opened. All
nineteen charged SHA-256 values reproduced byte-exactly:

```text
PROGRESS.md 05b171b8   AUDIT.md 3998e744   APPROACHES.md 4a4fbc3e
COORDINATION.md 37ddc8f2
canonical-normalization-degree3 95c99e2d
all-degree-acyclic-companion   9579d3a1
quartic-branch-topology        5d7df7ce
total-delta-two-iterated-knot  03865aae
genus-three-cable-b1           03b16c2d
genus-three-m0-complete        bcfc47b0
genus-three-t34-m0-projection  2b3cc0b7
genus-three-spectator-fox      a25d4b2f
quartic-cycle1-function-pair   2531a89d
quartic-cycle1-invariant-ring  0e2e09c8
quartic-discriminant-double-plane f5dbad98
quartic-double-plane-fox-localization 60ba8f43
cases/quartic_invariant_mu2_d6_20260830/RESULT.md 3401f33c
websweep-20260831T0454Z        3b7e5db8
post-ledger-dependency-hash-corrigendum be4c287f
```

I read no sibling model report, no `.log`, no `.run`/`.run.v2`, no uncharged
`xmodel/` artifact, and nothing in the excluded nested workspace. I used only
desk-scale exact `python3`/`sympy` in `/tmp`; no AWS, no web, no CAS beyond
polynomial expansion in at most twenty parameters, no repository write except
this file. The corrigendum's two corrected bindings are consumed as directed:
the cable artifact's interfaces are treated as reviewed, and the spectator
artifact's predecessor hash is read as `60ba8f433f...824a0`.

Evidence tiers used below: **EXACT** (a finite symbolic/arithmetic identity I
recomputed here), **PROVISIONAL** (an argument I reconstructed completely but
which is single-model), **CHARGED** (consumed from a sealed campaign artifact
at its stated tier), **CONJECTURAL** (a proposal, not an argument), and
**COMPUTATIONAL** (a finite enumeration whose interface assumptions are named).

## 1. Executive summary of what is new here

Five results below are new relative to the charged corpus. Three of them
change a live frontier.

1. **The surviving `m=1,Delta_aff=3,T(3,4)` row is empty.** PROVISIONAL, with
   an EXACT core. The proof does *not* use the coordinator's conjectural
   length-two ramification extension; it replaces it. Two new lemmas do the
   work: (a) in the charged `b1=1` packet the cubic normalization coordinate
   is `X=t^3+a t` with `a!=0`, so its ramification divisor is always **two
   distinct simple points** — the coordinator's "double critical point"
   sub-case is *vacuous*; (b) a `(3,1)` branch value must be a **singular**
   point of `B`, because at a smooth point the local complement group is `Z`
   and its transposition image is `C2`. Running these through the charged
   four-stratum classification, strata I, II and IV always have a critical
   point at a *smooth* point of `B` (dead for every `m`), and stratum III has
   both critical points at its two ordinary cusps, so the charged `m<=1`
   Euler ledger forces one of them to be `(2,1,1)/C2`. Section 3.
2. **A new genus ladder for the `S4` boundary gate.** COMPUTATIONAL/EXACT.
   Normalising the delta-sequence census and running the charged braid
   coloring machine reproduces the charged conductor-six answer exactly
   (`0/24/72`), and then gives: conductor eight leaves exactly **one** row,
   `(9,6,2)` with `K_infinity=C_(3,2)(trefoil)`, 144 labelled colorings; and
   **conductor ten and conductor sixteen are completely empty**. Hence
   `Delta_aff(B) notin {0,1,2,5,8}` for the whole irreducible one-place
   `A1`-normalised class, independently of `b1`, `m`, `n4`. Section 4.
3. **The degree-eight invariant-ring cell should not get an AWS job.**
   EXACT. I computed the full 20-parameter degree-eight Jacobian: 58 distinct
   monomials, exactly one parameter-independent coefficient (the constant,
   equal to `2`), so the degree-six certificate provably does not extend. But
   the whole bounded programme is subsumed: `H_1,H_2` are honest polynomials
   in the retained chart with constant Jacobian, so **Moh's theorem (`deg<=100`
   implies JC2) already empties every such cell up to pullback degree 100**,
   because an invertible pair has `deg_geo=1!=4mu`. Section 6.
4. **The one-cusp Keller equation is a Poisson-bracket problem on an explicit
   hypersurface.** EXACT for `(mu,r)=(2,2)`: `O(U)=C[A,U,Z]/(U^2-A-A^2 Z)` with
   `{A,U}=2A^2`, `{A,Z}=4U`, `{U,Z}=2+4AZ`; the two charged parameter-free
   coefficients `[x^2y]J=8`, `[x^4y^2]J=4` are literally the two monomials of
   `4AZ`. This yields a sharp dichotomy: if the Hamiltonian derivation
   `{H_1,-}` is locally nilpotent the horn dies at once from `Pic(U)=Z/mu!=0`,
   so the horn *requires* a non-locally-nilpotent Hamiltonian field with a
   slice. Section 5.
5. **An all-degree corollary of the smooth-point lemma.** PROVISIONAL: every
   fibre whose partition is not the generic `(2,1^(d-2))` lies over a singular
   point of `B`, giving `n_nonsimple <= #Sing(B) <= Delta_aff(B)` and, with
   the ruling identity, `n_nonsimple <= d-3+2 b1(B)`. Section 9, idea I4.

Two corrections/clarifications to charged material are recorded in Section 12.
Neither retracts a charged conclusion; one of them (`(6,4,3)`) is
*independently reconfirmed* here by a different route.

## 2. Reassessment of the avenue inventory

I re-read the 46-row master union table and the top ten overlays. The
important observation is that the ranking is now **stale in one direction
only**: the block-descent/rank-four front has absorbed almost all attention
because it produces theorems quickly, but three of its recent gates are in
fact classical-degree-theory questions in disguise, and one whole dormant
avenue cluster has become directly usable.

### 2.1 Stale rankings

- **Row 6, Abhyankar--Moh one-place / coordinate recognition — badly
  underrated.** It is currently filed as an old, partly tried avenue. In fact
  every genus-`g` row of the current proof front *is* a one-place semigroup
  problem: the charged conductor-six census is an Abhyankar--Moh--Assi
  computation, my genus ladder is the same computation at higher conductor,
  and the `b1=1` strata are its coincidence scheme. Promote this row to a
  first-class supporting avenue with a named owner. It is also the avenue that
  supplies **Moh's `deg<=100` theorem**, which retires an entire AWS
  programme (Section 6).
- **Row 27, links at infinity / splice diagrams — correctly rated but
  mis-scoped.** It is now the *decision procedure* for the whole rank-four
  irreducible front, not a side technique. The genus ladder in Section 4 is
  the natural way to run it, and it must be run at the level of the
  **plane embedding** (delta-sequence) rather than the abstract curve — see
  Section 12.2, where two distinct embeddings of the same abstract curve give
  different infinity knots and hence different verdicts.
- **Row 29/30, LND and Makar-Limanov / exotic affine surfaces — newly
  viable, currently dormant.** The one-cusp horn is a question about a
  pseudo-plane `U` with `Pic(U)=Z/mu` and `K_U=0`. The Keller condition is
  exactly `{H_1,H_2}=c` for the induced Poisson bracket, and the derivation
  `{H_1,-}` has a slice. This is precisely the LND/slice-theorem circle of
  ideas (Rentschler, Wright, Daigle, Makar-Limanov). Section 5 turns this into
  a sharp dichotomy. This is the single most valuable dormant reconnection I
  found.
- **Row 25, fibre monodromy / dessins / Hurwitz passports — underrated.**
  The `m=0`/`m=1` arguments are Hurwitz-passport arguments. The passport
  language would have made the "smooth point forces `C2`" lemma obvious from
  the start (a passport entry is constrained by the local branch count). A
  small passport library would have prevented the `m=1` row from looking hard.
- **Row 5, Jung--van der Kulk degree descent — underrated as a *firewall*.**
  Its value now is negative-result hygiene: it, together with Moh, bounds what
  any bounded coefficient search can possibly learn.
- **Rows 1, 2, 3, 4 (GGV/Sigray/strip/formal-germ) and the whole `K00`
  cluster — correctly parked, and genuinely orthogonal.** Nothing in the
  rank-four progress is evidence for or against them. They remain the only
  counterexample-facing programme. See Section 7.
- **Row 39 (cohomological cluster) — the double-plane `Pic(D)[3]` route is
  the live instance.** It should be filed under row 39 as well as under the
  block-descent front, because its remaining content is an etale-cohomology
  vanishing statement, not a curve-topology statement.

### 2.2 Routes independent of the rank-four proof front

Three genuinely independent live routes, in decreasing order of my confidence:

1. **Classical degree theory as a completeness ceiling** (rows 5/6). Moh plus
   Nakai--Baba/Appelgate--Onishi give unconditional emptiness for entire
   bounded families. This is not a proof route to JC2, but it is a *cheap
   universal firewall* against wasted compute, and I used it in Section 6.
2. **Counterexample-facing coefficient realization** (`K00`/`F2`, rows 1/36).
   Untouched by the branch theorems. Section 7.
3. **All-degree branch topology** (the promoted acyclic-companion theorem).
   This is a genuine all-degree statement and its successor — the non-simple
   fibre count of idea I4 — does not go through rank four at all.

### 2.3 What the recent progress does *not* buy

It must be said plainly: excluding rank four excludes rank four. The canonical
normalization has first-leg degree one and generic degree `[C(x,y):C(F,G)]=d`;
degree three is excluded, degree four is being narrowed. Nothing in the
current front bounds `d`. A cofinal argument — some invariant that is
monotone in `d` and eventually contradictory — is still missing, and no
current lane owns it. I flag this as the campaign's largest structural gap
and propose idea I4 as the first honest attempt at a `d`-monotone inequality.

## 3. The surviving `m=1,T(3,4)` row is empty

This is the section the packet asks for special attention on. I give the
complete implication, then say exactly where each step sees `S3` rather than
recycling the invalid `C2` duplicate argument.

### 3.1 Setting

Charged (from `5d7df7ce...`, `bcfc47b0...`, `2b3cc0b7...`, `03865aae...`,
`03b16c2d...`): an actual rank-four charged minimal-cycle packet with

```text
h=k=1,   beta=b1(B)=n22=1,   n4=0,   Delta_aff(B)=3,
normalization(B)=A1,   one place at infinity,
global meridional monodromy = transitive S4, generic inertia a transposition,
m=|T31| in {0,1}.
```

Charged consequences I consume without re-proving: `K_infinity=T(3,4)` and the
plane delta-sequence is `(4,3)`; the normal form

```text
X=t^3+a t,        Y=t^4+b t^2+c t,                      (3.1)
G(s)=s^3+(2a-b)s-c,   s=t+u,   t u=s^2+a,
D(s)=(t-u)^2=-3s^2-4a,                                  (3.2)
```

with roots of `G` at which `D!=0` giving genuine two-point normalization
fibres and roots at which `D=0` giving diagonal (non-immersive) parameters;
and the four `b1=1` strata

```text
I.   G=s^3,            b=2a,  c=0,     a!=0;
II.  G=(s-r)^2(s+2r),  a=b=-3r^2, c=-2r^3, r!=0;
III. G=s(s-q)(s+q),    a=-3q^2/4, b=-q^2/2, c=0, q!=0;
IV.  G=(s-q)^2(s+2q),  a=-3q^2/4, b=3q^2/2, c=-2q^3, q!=0. (3.3)
```

I verified every line of (3.3) symbolically in `sympy` over the indicated
nonzero parameters: the factorizations of `G`, the value of `D` at each root,
and the resulting conductor pairs. EXACT.

### 3.2 Lemma A (no totally ramified cubic projection)

**Claim.** In the charged `b1=1` packet, `a!=0`. Hence `X'=3t^2+a` has two
distinct simple roots, and `X|_B` is simply ramified at exactly two points.

**Proof.** Suppose `a=0`. Then `D(s)=-3s^2`, so `s=0` is the only possible
diagonal root, and every nonzero root of `G` is admissible.
*If `c!=0`*: `G(0)=-c!=0`, so all three roots (with multiplicity) are
admissible and `b1` is the number of distinct roots; `b1=1` forces a triple
root of `s^3-bs-c`, which has no `s^2` term, so the triple root is `0`, so
`c=0` — contradiction.
*If `c=0`*: `G=s(s^2-b)`, and `s=0` is diagonal. If `b!=0` the two roots
`+/-sqrt(b)` are distinct and admissible, so `b1=2`. If `b=0` then `G=s^3` with
its only root diagonal, so `b1=0`. Either way `b1!=1`. `//`

This is independent of the four-stratum list, and it is confirmed by it:
`a` equals `a`, `-3r^2`, `-3q^2/4`, `-3q^2/4` in the four strata, all nonzero.

**Consequence for the coordinator's conjectural extension.** Overlay item 5
proposed splitting on "a double critical point at the unique `T31` value"
versus "two simple critical points". Lemma A shows the first branch is
**vacuous** inside the charged `b1=1` packet. That is a strict simplification:
the weakest link of the proposed extension (the claim that a triple coalescence
lands all three vertical meridians in a sheet-fixing `S3`) never has to be
argued. It also removes any need for the local `T22` intransitivity sub-case.

### 3.3 Lemma B (a `(3,1)` value is a singular point of `B`)

**Claim.** Let `z` be a smooth point of the reduced branch `B`. Then the local
decomposition group at `z` is `C2` and the quartic fibre over `z` is
`(2,1,1)`. Equivalently, `T31 subset Sing(B)`, and likewise for `(4)` and
`(2,2)` fibres.

**Proof.** Charged (integration `5d7df7ce...`, Section 5): at any closed branch
point the plane-curve local complement group is *generated* by its branch
meridians, not merely normally generated. At a smooth point of `B` a small
bidisk complement is homotopy equivalent to a circle, so there is one branch
and one meridian up to conjugacy; its image is a transposition `tau`, and the
local decomposition group is `<tau>=C2`, whose orbits on four sheets are
`2+1+1`. `//`

This is the exact converse direction of the charged local point-stabilizer
table, and it is the lemma that makes the `m=1` row tractable. It also
explains the spectator control: its two cusps have local `S3` image precisely
because they *are* singular points.

### 3.4 The stratum-by-stratum ramification location

Exact `sympy` output (all four rows verified over the generic parameter):

```text
stratum  X'=0 at        conductor pair {alpha,beta}   diagonal (cusp) params
I        +-sqrt(-a/3)   {+-sqrt(-a)}                  none
II       {+r,-r}        {2r,-r}                       {-r}
III      {+q/2,-q/2}    {+-sqrt(3)q/2}                {+q/2,-q/2}
IV       {+q/2,-q/2}    {-q+-(3i/2)q}                 {q/2} (double, (2,5))
```

Reading off the type of `nu(gamma)` for each critical parameter `gamma`:

* **Stratum I.** `G` has no diagonal root, so the parametrization is immersive
  everywhere; both critical points lie outside the conductor pair (`sqrt(-a/3)
  != sqrt(-a)` because `a!=0`) and have singleton normalization fibres. Both
  are therefore **smooth points** of `B`. `Sing(B)` is the single
  order-three-contact two-branch point, which is the `(2,2)` value, so in fact
  `T31=empty` and `m=0` here.
* **Stratum II.** `t=-r` is simultaneously a conductor endpoint and the
  diagonal cusp; `t=+r` is neither, and is immersive, hence a **smooth
  point**. `Sing(B)` is the single cusp-plus-smooth-branch point, again the
  `(2,2)` value, so `T31=empty` and `m=0`.
* **Stratum III.** Both critical points are exactly the two ordinary cusps.
  `Sing(B)` = {node = the `(2,2)` value} `cup` {two cusps}. Hence
  `T31 subset` {two cusps} and `m<=2`.
* **Stratum IV.** `t=q/2` is the delta-two unibranch `(2,5)` point;
  `t=-q/2` is immersive, outside the conductor pair (checked:
  `(-q/2)^2+2q(-q/2)+13q^2/4=10q^2/4!=0`), hence a **smooth point**.
  `Sing(B)` = {node = `(2,2)`} `cup` {`(2,5)` point}, so `m<=1`.

### 3.5 The closure

Let `gamma` be a critical parameter of `X` with `nu(gamma)` of quartic type
`(2,1,1)`, hence local group `C2=<tau>`. Because `X` is simply ramified at
`gamma` and `nu(gamma)` has a singleton normalization fibre, exactly two of
the three points of the nearby vertical fibre coalesce along **one** analytic
branch of `B` at `nu(gamma)`. Transport the generic three-puncture fibre into
a local frame over a small disk about `X(gamma)`. The two coalescing meridians
lie in the local complement group at `nu(gamma)`, whose image `C2` is abelian,
so both equal `tau`. The third puncture is a separate sheet and contributes
some transposition `rho`. The local triple is `(tau,tau,rho)`.

Charged: `X` is the degree-three coordinate of the plane quartic (`B` closes to
a quartic smooth at `[0:1:0]`, the projection `x` is finite of degree three,
`q_B` is monic of degree three in `y`), so affine Zariski--van Kampen makes the
three fibre meridians generate `pi_1(A^2-B)`; and elementary Hurwitz moves
`(A,B) -> (ABA^{-1},A)` are Nielsen transformations, so the local triple and
the original based triple generate the same subgroup of `S4`. Three
transpositions generate a transitive subgroup of `S4` iff their supports form a
spanning tree on four vertices; a duplicate leaves at most two distinct edges,
hence order at most six, hence intransitive. Contradiction with the charged
transitive `S4`.

It remains to produce such a `gamma`.

* Strata **I**, **II**, **IV**: a critical point at a **smooth** point of `B`
  exists (table above); by Lemma B its type is `(2,1,1)` with group `C2`.
  These strata are dead **for every `m`**, with no Euler input at all.
* Stratum **III**: both critical points are cusps. Their normalization fibres
  are singletons, so neither is the `(2,2)` value (charged: `(2,2)` fibres are
  exactly the two-point normalization fibres, and `n22=1` with `b1=1` pins the
  unique one at the node); `n4=0` excludes `(4)`; and independently a cusp's
  local group is generated by two conjugate transpositions satisfying
  `aba=bab`, which is `C2` or `S3`, never `A4`/`S4`. So each cusp is `(2,1,1)`
  or `(3,1)`. With `m<=1` at least one cusp is `(2,1,1)`, giving `gamma`.

Therefore the charged irreducible row with `Delta_aff=3` is **empty for
`m in {0,1}`**, i.e. empty outright. Combined with the charged
`Delta_aff>=3`, the irreducible minimal row now needs `Delta_aff>=4`.

### 3.6 Independent reconstruction of `m<=1`

I did not want the closure to rest on an uncharged threat map, so I rebuilt
the arithmetic. With `U=Y-R`, `R` the reduced non-etale locus,
`e_c(A^2)=1`, `e_c(B)=1-b1=0`, and fibre contributions
`(2,1,1)->2`, `(2,2)->0`, `(3,1)->1`, `(4)->0` counted as unramified points:

```text
e_c(U)=4(1-e_c(B))+2(e_c(B)-1-m-n4)+m = 4-2n22-m-2n4 = 2-m-2n4.  (3.6.1)
```

The promoted ruling identity `e_c(U)=e(C)+Q`, `C in {A1,P1}`, `Q>=0`, with
`n4=0` gives exactly

```text
(m,C,Q) in {(0,A1,1), (1,A1,0), (0,P1,0)},               (3.6.2)
```

which is verbatim the charged three-subrow statement of integration
`5d7df7ce...` Section 7. EXACT, and it independently confirms `m<=1`.

### 3.7 Why each step sees `S3` and not `C2`

The packet asks this explicitly. Every step above is written so that the `S3`
escape is *named* and then either avoided or excluded:

- Lemma B is the only place a local group is computed from geometry, and it
  computes it at a **smooth** point, where `S3` is impossible because there is
  only one branch and hence one meridian. It never asserts `C2` at a cusp.
- Strata I, II and IV never touch a cusp or a `(2,5)` point. Their `gamma` is a
  smooth point, so the `S3` escape is not available to the adversary there,
  and no `m` hypothesis is used.
- Stratum III is the *only* place where an `S3` cusp can occur, and the
  argument does not claim either cusp is `C2`. It uses the counting fact that
  there are two cusps and at most one `(3,1)` value.
- The spectator control `(t^3-3t,t^4-2t^2)` is exactly stratum III with `q=2`
  (`a=-3`, `b=-2`, `c=0`; cusps at `t=+-1=+-q/2`, node at `t=+-sqrt(3)`), and
  its charged quartic has **both** cusps with local `S3` image, i.e. `m=2`.
  So the spectator sits precisely one unit outside the charged row and
  demonstrates that the `m<=1` input in stratum III is load-bearing, not
  decorative. My argument correctly does not exclude it.
- No step identifies a cv flag with a physical place, charges a separation set
  twice, uses a pole identity, or upgrades a floor to attainment.

### 3.8 Residual risk

Single-model. The three interfaces I would attack first in a hostile review:
(i) whether "the local complement group at a closed branch point is generated
by its branch meridians" is being used with the right basepoint/frame
convention in Lemma B (it is charged, but the *converse* direction is new
usage); (ii) whether the charged four-stratum classification is really complete
(I re-derived the four strata from `G` having exactly one distinct admissible
root and confirmed each line symbolically, so I believe it is); (iii) whether
the charged `(4,3)` delta-sequence is forced, i.e. whether `B`'s plane
embedding could be the `(6,4,3)` one — it cannot, because that embedding has
`b1>=2`, and Section 12.2 gives an independent proof of that.

## 4. The genus-four successor, and a new genus ladder

### 4.1 Method

The charged genus-three census combines two independent filters: the
Assi--Garcia-Sanchez conductor arithmetic on delta-sequences (an *algebraic*
filter on the plane embedding) and the `S4` meridian-transposition coloring
count of the resulting iterated torus knot (a *topological* filter). I
reimplemented both from scratch.

*Delta-sequence enumerator.* Conditions imposed: `delta_0>delta_1`;
`d_1=delta_0`, `d_{i+1}=gcd(d_i,delta_i)`, `d_{h+1}=1`; `e_i=d_i/d_{i+1}>=2`;
the non-degenerate stage normalization `delta_k/d_{k+1}>=2` (this is the
campaign's `a>b>=2`, and it is exactly what deletes trivial first stages such
as `(6,3,4)`); the ordering `delta_k d_k > delta_{k+1} d_{k+1}`; freeness
`e_k delta_k in <delta_0,...,delta_{k-1}>`; and the conductor formula
`mu=sum(e_k-1)delta_k-delta_0+1`. Enumeration bound `delta_i<=4g+5` is safe:
telescoping the stage genera gives `delta_0<=2g+1`, and
`(e_1-1)delta_1<=2g+delta_0-1` with `e_1>=2` gives `delta_k<=4g`.

*Validation.* At conductor six this returns exactly `{(4,3),(6,4,3),(7,2)}`,
byte-for-byte the charged list (3.6) of `03b16c2d...`. COMPUTATIONAL, validated.

*Braid/coloring machine.* Torus braid `(s_1...s_{p-1})^q`; block-transposition
words `X_2=s2 s3 s1 s2`, `X_3=s3 s4 s5 s2 s3 s4 s1 s2 s3` (charged (6.1)) and
their general form; blackboard `p`-parallel with framing correction
`(s_1...s_{p-1})^(q-p*w)`, `w` the companion writhe; Artin action
`sigma_i:(A,B)->(ABA^{-1},A)`; retain tuples fixed by the closed braid whose
entries generate all 24 elements of `S4`. Simultaneous-conjugacy reduction:
full-`S4` tuples have trivial centralizer, so fixing the first entry and
multiplying by six is exact.

*Validation.* Reproduces the charged census (6.5) exactly:
`T(2,7)->0`, `T(3,4)->24`, all four `C_(2,+-3)(trefoil+-)->72`, all four
`C_(3,+-1)(trefoil+-)->0`. COMPUTATIONAL, validated.

### 4.2 Result

```text
conductor  delta-seq   infinity knot            labelled full-S4 colorings
  6        (4,3)       T(3,4)                     24
  6        (6,4,3)     C_(2,3)(trefoil)           72     [killed by b1>=2]
  6        (7,2)       T(2,7)                      0
  8        (5,3)       T(3,5)                      0
  8        (6,4,5)     C_(2,5)(trefoil)            0
  8        (9,2)       T(2,9)                      0
  8        (9,6,2)     C_(3,2)(trefoil)          144
 10        (6,4,7)     C_(2,7)(trefoil)            0
 10        (11,2)      T(2,11)                     0
 16        (10,4,9)    C_(2,9)(T(2,5))             0
 16        (17,2)      T(2,17)                     0
```

All sign and chirality variants were run for every nonzero-strand row
(`q -> -q`, companion mirror): the counts are unchanged, so no orientation
convention weakens any conclusion.

**Consequences.**

- **Genus four (`Delta_aff=4`) leaves exactly one row: `(9,6,2)`,
  `K_infinity=C_(3,2)(trefoil)`, 144 labelled colorings.** This is the exact
  analogue of `T(3,4)` at genus three, and it is the *only* target the
  genus-four successor must attack.
- **`Delta_aff(B)=5` and `Delta_aff(B)=8` are impossible.** Both conductor
  censuses are complete (two rows each) and both are entirely zero. This
  needs no `b1`, `m`, `n4`, `n22` or Euler input; it is a pure boundary gate.
  Combined with the charged `Delta_aff>=3` and Section 3, the irreducible
  one-place `A1` class satisfies

```text
Delta_aff(B) notin {0,1,2,5,8},   and in the charged minimal row
Delta_aff(B) >= 4.                                       (4.2.1)
```

- The gate is genuinely sporadic, not monotone: conductors 12, 14, 18, 20, 24
  all have survivors. So this is a sieve to be run row by row, not a bound.
- Partial data at higher conductor (rows with more than seven braid strands
  were skipped as too expensive for a desk lane, and are listed in Section 11
  as an AWS item): conductor 12 leaves `(6,4,9)` and `(9,6,4)`; conductor 14
  leaves `(8,3)` and `(8,6,3)`; conductor 22 has all four computed rows zero
  with two rows uncomputed — that last one is a plausible third empty genus.

### 4.3 What can be proved symbolically before any enumeration, for `(9,6,2)`

This answers the packet's "say what can be proved symbolically" directly.

The value semigroup of `(9,6,2)` is `<9,6,2>=<2,9>`, genus four, conductor
eight. Since the degree semigroup of `C[B]` contains `2`, and any subring of
`C[t]` with the same degree semigroup as a larger one is equal to it, we get
without any enumeration:

```text
C[B] = C[w,V],   deg w=2,  deg V=9.                       (4.3.1)
```

Normalising: after an affine change of the parameter and of `w` we may take
`w=t^2`; subtracting a polynomial in `w` from `V` we may take `V` odd:

```text
w=t^2,   V=t*P(t^2),   P monic of degree 4.               (4.3.2)
```

Four consequences, all symbolic:

1. **The abstract curve carries a hyperelliptic-type involution.** `sigma:t
   -> -t` fixes `w` and negates `V`. Since the plane coordinate of degree six
   lies in `C[w]` (degree `6<9=deg V`) it is a cubic `U=W(w)`, so `sigma`
   extends to the **linear** involution `(U,V) -> (U,-V)` of `A^2`, and `B` is
   invariant under it. The whole pair `(A^2,B)` is `Z/2`-symmetric, hence the
   braid monodromy factorization is symmetric and the `S4` representation is
   constrained by an induced action on the coloring set. Nothing analogous
   exists at genus three. This is the sharpest new handle.
2. **`b1` is computed in closed form.** `w(t)=w(u)` with `t!=u` forces
   `u=-t`; since `V` is odd, `V(t)=V(-t)` iff `V(t)=0`. So the two-point
   fibres are `{+-sqrt(z_i)}` for the nonzero roots `z_i` of `P`, and

   ```text
   b1(B) = #{distinct nonzero roots of P}.                (4.3.3)
   ```

   Hence `b1=1` gives exactly four strata by the multiplicity pattern of `P`
   at `0` and at its unique nonzero root `rho`:
   `P=(z-rho)^4`, `z(z-rho)^3`, `z^2(z-rho)^2`, `z^3(z-rho)`. The first has
   `t=0` immersive; the others give a unibranch singularity at `t=0` of
   semigroup type `<2,9-2k>`. This is the exact genus-four analogue of the
   charged four-stratum table, obtained with no enumeration.
3. **The projection lever is weaker and must be replaced.** `Gamma=<2,9>` does
   not contain `3`, so there is **no** degree-three linear projection; the two
   linear projections have degrees six and nine. A duplicate among six
   meridians still leaves five distinct transpositions and can be transitive,
   so the genus-three mechanism does not transfer. The replacement should be
   the factorization `U|_B = W o w` with `deg w=2`, `deg W=3`: the six
   punctures of a generic `U`-fibre are three `sigma`-orbits, and the induced
   `S4`-coloring is a coloring of a *three*-strand object twisted by `sigma`.
   Making that precise is the concrete symbolic task.
4. **Realizability is a bounded approximate-root condition.** `C[U,V]=C[w,V]`
   holds iff `w in C[U,V]`; splitting into `sigma`-parity,
   `C[U,V]=S (+) S*V` with `S=C[U(w),wP(w)^2] subset C[w]`, so the condition
   is exactly `C[U(w),wP(w)^2]=C[w]` for a cubic `U` and a degree-nine
   `wP^2`. That is a one-variable Abhyankar--Moh reduction with a small
   parameter count: entirely desk-scale, and it is the *first* thing to
   compute, because if it is empty the whole genus-four row dies with no
   topology at all.

### 4.4 The genus-four screening order I recommend

Replacing the charged five-step order with a cheaper one that front-loads the
symbolic kills:

```text
G4-1  (desk, symbolic)  solve C[U(w),wP(w)^2]=C[w] for the (9,6,2) embedding;
G4-2  (desk, symbolic)  intersect with b1=1 via (4.3.3): four strata;
G4-3  (desk, arithmetic) rerun (3.6.1) at Delta_aff=4 to bound m and n4;
G4-4  (desk, topology)  locate Sing(B) and the ramification of the degree-six
                        projection; apply Lemma B to force T31 onto Sing(B);
G4-5  (desk, topology)  exploit the (U,V)->(U,-V) involution on the braid
                        factorization and on the 144-element coloring set;
G4-6  (desk, cohomology) affine sign-Fox space and every singular-link
                        restriction, then the quartic-lift gate.
```

Note that `G4-1` through `G4-3` are pure algebra and can be finished before any
knot enumeration; the charged order put enumeration first.

## 5. Reattacking the one-cusp index-four / log-Jacobian gate

The packet asks for at least two of field theory, valuations, logarithmic
symplectic geometry, compactified intersection theory, pseudo-plane
automorphisms, companion resultants. I use **logarithmic symplectic geometry**
(as a Poisson algebra), **valuations/LND theory**, and **field theory**, and I
supply the controls the charged artifact demands.

### 5.1 The invariant ring is an explicit Poisson hypersurface

For the primitive single-pole model with `(mu,r)=(2,2)`, `d=r-1=1`,
`w=1+x^2 y`, `z=y(1+w)`, the charged generators pull back to

```text
A=x^2,   U=x w=x+x^3 y,   Z=z=2y+x^2 y^2,
```

and I verified exactly, by direct expansion:

```text
U^2 - A - A^2 Z = 0,                                     (5.1.1)
{A,U}=2A^2,   {A,Z}=4U,   {U,Z}=2+4AZ,                   (5.1.2)
```

where `{f,g}=J_(x,y)(f,g)`. So `O(U)=C[A,U,Z]/(U^2-A-A^2 Z)` is a Poisson
hypersurface, and (5.1.1) is Poisson-compatible (`{A,R}={U,R}=0` for
`R=U^2-A-A^2Z`, checked). EXACT.

This is the coordinate-free content of the charged logarithmic Jacobian
equation: the Keller condition on the horn is precisely

```text
find F_1,F_2 in O(U)  with  {F_1,F_2}=c in C*,
plus the field condition [C(U):C(F_1,F_2)]=4.            (5.1.3)
```

**Control (and an explanation of the charged AWS certificate).** The charged
degree-six certificate `[x^2y]J=8`, `[x^4y^2]J=4` is not a coincidence: it is
literally `4AZ = 8x^2y+4x^4y^2`, the non-constant part of `{U,Z}` in (5.1.2).
The certificate says that in that cell no correction term reaches those two
monomials. Section 6 shows the certificate does **not** survive to degree
eight, which is exactly why the charged "tiny exploratory expansion" found
nothing.

### 5.2 The Hamiltonian LND dichotomy

Suppose (5.1.3) has a solution. Set `D=(1/c){F_1,-}`, a derivation of `O(U)`
with `D(F_2)=1`: **`D` has a slice**.

*If `D` is locally nilpotent*, the slice theorem gives
`O(U)=ker(D)[F_2]`, so `U ~ Spec(ker D) x A^1`. `ker D` is factorially closed,
hence integrally closed, one-dimensional and finitely generated; `U` smooth
forces `C=Spec(ker D)` smooth affine. Then
`Pic(U)=Pic(C[F_2])=Pic(C)`. But the Picard group of a smooth affine curve
over `C` is a quotient of the divisible group `Pic^0` of its projective model,
hence divisible, and a nonzero finite group is not divisible; so `Pic(U)=0`.
This contradicts the charged `Pic(U)=Z/mu` with `mu>=2`.

*Therefore the horn requires `{F_1,-}` to be a derivation with a slice that is
**not** locally nilpotent.* PROVISIONAL (the only non-elementary input is
`Pic(U)=Z/mu`, which the charged artifact states with a "generally"
qualifier and which must be pinned for the exact `(U,rho,mu)` in the horn).

**Why this is worth something.** On `A^2` the same dichotomy is circular:
`{F_1,-}` locally nilpotent is equivalent, by Rentschler, to `F_1` being a
variable, which is what one is trying to prove. On the pseudo-plane the
locally-nilpotent branch is an outright **contradiction**, because `Pic(U)!=0`
obstructs any product decomposition. So the horn has been reduced from "prove
a global Jacobian statement" to "exclude a non-locally-nilpotent Hamiltonian
derivation with a slice on a `Q`-homology plane with `K_U=0`" — a question
squarely inside the Makar-Limanov/Daigle/Dubouloz--Palka circle, where the
`ML` invariant and the `A^1`-fibration `rho` are exactly the available tools.

**Control against overclaiming.** I do *not* claim `D` is locally nilpotent,
and there is no cheap reason it should be. Three named traps:
(i) a derivation with a slice need not be locally nilpotent — `D=d/du+v d/dv`
on `C[u,v]` has `D(u)=1` and `ker D=C`;
(ii) `Pic(U)=Z/mu` is charged with a hedge and is the load-bearing input;
(iii) the argument says nothing about the *existence* of `F_1,F_2`, so it is
a gate, not an exclusion.

### 5.3 Field-theoretic sharpening: the degree semigroup is `2N`

In the `(mu,r)=(2,2)` model the pullback degree of `x^a w^b z^c` is `a+3b+4c`
subject to `a+b` even, so every element of `O(U)` has **even** total degree in
`(x,y)`. Hence for any solution of (5.1.3),

```text
deg H_1, deg H_2 are both even.                          (5.3.1)
```

Combined with the classical leading-form theory on `A^2` (the leading forms of
a Keller pair are proportional to powers of a common form, so `e | deg H_1`
and `e | deg H_2` for `e` the degree of that form) and with Nakai--Baba /
Appelgate--Onishi divisibility, (5.3.1) is a real restriction on which degree
pairs can occur. This is the cheap field/valuation-side content that the
charged artifact's "the two weights `nu(X),nu(S)` alone do not decide
membership" warning leaves open. It should be pushed to general `(mu,r)`: the
parity is a shadow of the `C_mu`-grading, and the general statement is a
congruence on `deg H_i` modulo something built from `mu` and `r`.

### 5.4 What I deliberately did not do

I did not attempt the companion-resultant route or the compactified
intersection ledger, because the charged function-pair integration already
states four precise ways to close and I judged the Poisson/LND route strictly
stronger per unit of effort. I also did not re-derive `deg_geo(H)=4mu`, `mu=d_1`
or the Orevkov--Chau saturation; those are charged.

## 6. Decision on the degree-eight invariant-ring cell: **no**

### 6.1 The cheap certificate provably does not extend

I built the full degree-eight cell exactly. Basis of pullback degree at most
eight: candidate invariant monomials `x^a w^b z^c` with `a+b` even and
`a+3b+4c<=8` span a **13-dimensional** space (15 monomials, two redundant
modulo `U^2=A+A^2Z`), matching the charged count. Excluding `1,U,Z` leaves ten
elements `{A,A^2,A^3,A^4,AU,A^2U,AZ,A^2Z,UZ,Z^2}`, so
`H_1=U+sum a_i P_i`, `H_2=Z+sum b_i P_i` has **20 parameters**, matching.

Expanding `J(H_1,H_2)` symbolically gives **58 distinct monomials**, i.e. 57
non-constant coefficient equations plus the constant term, which is exactly
`2` — matching the charged normalization. Scanning all 58 coefficients:

```text
the ONLY parameter-independent coefficient is the constant term, = 2.
```

So there is no degree-six-style parameter-free certificate at degree eight.
EXACT. This settles the charged "a tiny exploratory expansion found no
parameter-independent coefficient" as an exhaustive statement.

### 6.2 The whole bounded programme is subsumed by Moh

`H_1,H_2` are ordinary polynomials in the retained chart coordinates `(x,y)`,
with `J_(x,y)(H_1,H_2)=c` a nonzero constant. If the cell has any solution,
`(H_1,H_2):A^2->A^2` is a plane Keller map of total degree at most eight.
T. T. Moh, *On the Jacobian conjecture and the configurations of roots*,
J. reine angew. Math. 340 (1983), 140--212, proves the plane Jacobian
conjecture for `deg<=100`. Hence any such pair is a **polynomial automorphism**,
so `deg_geo(H_1,H_2)=1`. But the charged horn requires
`deg_geo(H)=[C(x,y):C(H_1,H_2)]=4mu>=8`. Contradiction.

Therefore:

```text
Every normalized invariant-ring cell of pullback degree at most 100,
for any (mu,r), is empty of horn-relevant solutions, by one citation.  (6.2.1)
```

The charged degree-six AWS run is thereby retrospectively redundant *for the
horn* (it does prove the strictly stronger statement that no constant Jacobian
occurs at all, which Moh does not give; that is a genuine but horn-irrelevant
increment). PROVISIONAL only in that someone should confirm the exact form of
Moh's hypothesis (`max(deg H_1,deg H_2)<=100`, characteristic zero, two
variables) against the primary source before this is promoted; I did not have
the paper in hand and did not run a web search.

### 6.3 Higher-value exact computation instead

Reallocate the AWS slot to one of these, in order:

1. **`G4-1`/`G4-2` scaled up** — the exact `(9,6,2)` realizability and `b1=1`
   strata (Section 4.3). Desk-scale first; if the elimination grows, it is a
   small, well-posed Groebner problem over `Q` in at most six parameters, with
   a clean promotable output (an exact normal form or an emptiness
   certificate). This is the single highest-value exact computation available.
2. **The higher-strand rows of the genus ladder** (Section 4.2): conductor 22
   rows `(12,8,6,11)` (8 strands) and `(15,10,4)` (10 strands), and the
   conductor-14 rows `(12,8,3)`, `(12,8,6,3)`, `(15,10,2)`. Each is a fixed
   finite `S4`-coloring count: `6^(n-1)` tuples with the conjugacy reduction,
   trivially shardable, byte-reproducible, no CAS. If conductor 22 is empty it
   is a third impossible genus and a strong hint of a structural theorem.
3. **A structural leading-form study of `gr O(U)`** (idea I7) — cheap, and it
   is the only thing in this area that could produce a degree-independent
   theorem rather than another bounded emptiness.

### 6.4 If the coordinator still wants the degree-eight job

For completeness, the packet asks for a full specification if the answer is
yes. My answer is no, but the minimal honest specification would be:
coefficient ring `Q[a_0..a_9,b_0..b_9]`; the 57 equations above; degrevlex
with the parameters last, plus one elimination order for the `deg_geo` test;
primes `32003`, `65521`, `2147483647` with a rational-reconstruction lift;
saturation by the nonvanishing of the constant Jacobian is unnecessary since
the constant term is identically `2`; shard on the rank-`<=1` stratification
of the `5x2` matrix `[a_3,a_5,a_7,a_8,a_9; b_3,b_5,b_7,b_8,b_9]` (the seven
top-degree equations are exactly its `2x2` minors, which I verified — this is
the leading-form proportionality appearing automatically); mutation: replace
the constant target `2` by `3` and require the unit ideal; stopping rule: any
positive-dimensional component must be pushed through the `[M:K]=4` test before
promotion. Even so, (6.2.1) makes the outcome known in advance.

## 7. Higher-degree routes and counterexample-facing programmes

**Do not assume excluding rank four proves JC2.** Recording the honest state:
degree three is promoted excluded; degree four is being narrowed row by row;
every degree `>=5` is untouched, and the canonical normalization gives no bound
on `d`. The all-degree acyclic-companion theorem is the only `d`-uniform
statement, and it is a necessary condition, not a ceiling.

- **A `d`-monotone inequality is the missing object.** Idea I4 gives the first
  candidate: `n_nonsimple <= #Sing(B) <= Delta_aff(B)` together with
  `n_nonsimple <= d-3+2 b1(B)` from the ruling identity. These pull in
  opposite directions as `d` grows and are worth pushing.
- **Reduction mod `p` / `p`-curvature (rows 19--21).** Untouched by any of
  this. The charged char-`p` state (Mondello `F_2` stratum `W_2`-obstructed;
  an `F_3` degree-three collision lifting at every Witt level with growing
  support, limit restricted-analytic) is unchanged. The one new question I can
  contribute: the Poisson formulation (5.1.3) makes sense over `Z`, and the
  pseudo-plane `x^r z=w^mu-1` is defined over `Z`; asking whether the mod-`p`
  reduction of the horn admits solutions for small `p` is a bounded, honest
  test that has not been run.
- **Valuation / formal-map programmes.** The one-cusp horn now has a *single*
  divisorial valuation `nu=ord_Phi` controlling polynomiality (charged (3.3)).
  A formal-germ study at `nu` is the natural bridge to the `D`-series
  machinery of row 4, and nobody owns that connection.
- **Bounded search hygiene.** Any coefficient search over honest plane
  polynomials with `deg<=100` is now known-empty. This applies to some of the
  small-support/sparse-support programmes of row 36, and should be written into
  the search harness as a preflight rejection.
- **`K00`/`F2` coefficient realization.** Degrees there are far above 100, so
  Moh does not touch it. It remains the campaign's only live
  counterexample-facing lane and should keep its independent budget.

## 8. Safe research questions from the Strinz note

The charged sweep is explicit: the note is prose-tier, publishes no exact
artifacts, and makes no exclusion, map, or occupancy claim. I extract only
questions, and promote nothing.

Q1. Does the campaign's own literal band object already supply the note's
missing **source-to-reduced adapter**? This is answerable entirely inside our
frozen `.poly` rows; a negative answer is as useful as a positive one.
Q2. Is the note's five-periodic band staircase through `K5` the same
periodicity as our `K00`/`F2` recurrence, or an artifact of its normalization?
Compare *our* exact recurrences to *our* own data; do not import its formulas.
Q3. The note's `q19` component "has an exact quadratic normal form and positive
complex truncations". The safe question is only: **does our machinery produce a
quadratic normal form at the analogous index?** A positive complex truncation
is not an occupancy statement and must never be recorded as one.
Q4. Its `q18` leading-pole kill of a tuned family is a finite witness. The safe
question: does our band ledger have an *independent* obstruction at the same
index? If yes, that is a cross-check; if no, that is a gap in ours, not
evidence for theirs.
Q5. The corrected Row-40 tower homogenizing to `(15,25)` and being classically
excluded is the note's own admission that only the reduced model closes. Our
version of that question is whether *our* reduced models have the same adapter
gap. This is a hygiene audit of our own ledger.

Explicit firewall: none of Q1--Q5 may be closed by citing the note. Every
answer must be reconstructed from campaign-frozen exact artifacts, and no
finite truncation witness may be promoted to a theorem in either direction.

## 9. Twelve ideas

Score is expected value per unit cost on 0--10.

### I1. Smooth-point local-group lemma closes the `m=1` genus-three row
*(new; the centrepiece)*
- **Implication.** `Delta_aff(B)=3` is impossible in the charged irreducible
  minimal row for `m in {0,1}`, so that row needs `Delta_aff>=4`.
- **Hypotheses.** Charged: `b1=n22=1`, `n4=0`, `h=k=1`, transitive `S4` with
  transposition inertia, `A1` normalization, one place at infinity, the `(4,3)`
  normal form and its four strata, Zariski--van Kampen generation, Hurwitz
  invariance. New: Lemma A (`a!=0`) and Lemma B (smooth `=>` `C2`).
- **Weakest failure mode.** Lemma B's converse use of "the local complement
  group is generated by branch meridians" — if that charged statement is only
  valid up to normal generation in some frame, stratum III's counting step
  survives but strata I/II/IV would need repair.
- **First falsification test.** Exhibit a plane branch germ, smooth at `z`, and
  a degree-four cover étale off `B` whose fibre over `z` is not `(2,1,1)`. If
  none exists (it should not), Lemma B is safe.
- **Interface.** Integration `5d7df7ce...` Sections 5 and 7; classification
  `2b3cc0b7...` Sections 3--4; Zariski--van Kampen; Nielsen/Hurwitz.
- **Score 9.** **Deliverable.** A sealed producer with the two lemmas, the
  four-stratum ramification table, and the `sympy` replay; then a hostile
  review by a model other than Opus.

### I2. The genus ladder as a standing sieve *(new, cross-avenue: rows 6 and 27)*
- **Implication.** `Delta_aff(B) notin {5,8}` unconditionally; genus four has a
  unique surviving row; a reusable oracle for every future genus.
- **Hypotheses.** The delta-sequence normalization conditions; the
  delta-sequence-to-iterated-torus-knot dictionary; the charged infinity-to-
  affine meridian-preserving surjection.
- **Weakest failure mode.** The stage normalization `delta_k/d_{k+1}>=2`. If a
  degenerate stage is legitimate, extra rows reappear. Mitigation: it exactly
  reproduces the charged conductor-six list, which is strong evidence.
- **First falsification test.** Feed the enumerator conductor six and demand
  `{(4,3),(6,4,3),(7,2)}`; feed the coloring machine `T(3,4)` and demand 24.
  Both pass here.
- **Interface.** Assi--Garcia-Sanchez arXiv:1407.0490; Schubert; charged
  `03b16c2d...` Sections 2--3 and 6.
- **Score 9.** **Deliverable.** A single deterministic script producing the
  table of Section 4.2 with byte-stable stdout, plus the higher-strand rows.

### I3. The genus-four `(9,6,2)` row via its hyperelliptic involution *(new)*
- **Implication.** Close, or exactly classify, `Delta_aff=4`.
- **Hypotheses.** `Gamma=<2,9>`, hence `C[B]=C[w,V]`, `w=t^2`, `V` odd, and the
  linear involution `(U,V)->(U,-V)` of `A^2` preserving `B`.
- **Weakest failure mode.** Realizability: if `C[U(w),wP(w)^2]=C[w]` has no
  solutions the row is empty for free, but if it has a large family the
  involution alone may not suffice against six-strand monodromy.
- **First falsification test.** Solve the one-variable subalgebra condition of
  Section 4.3(4) for `P=(z-rho)^4` first; that single case decides whether the
  simplest stratum exists.
- **Interface.** Abhyankar--Moh subalgebra theory in one variable; charged
  local point-stabilizer table; Lemma B.
- **Score 8.** **Deliverable.** The exact `(9,6,2)` normal form or an emptiness
  certificate for it.

### I4. Non-simple fibres live over singularities — an all-degree count
*(new, cross-avenue: extends the promoted all-degree branch theorem)*
- **Implication.** For any finite `pi:Y->A^2` of degree `d`, étale off reduced
  `B`, with transposition generic inertia: every fibre of partition other than
  `(2,1^(d-2))` lies over `Sing(B)`. Hence
  `n_nonsimple<=#Sing(B)<=Delta_aff(B)`, and with
  `e_c(U)=d b_1+(d-2)(1-b_1-N)+sum f_z` and the ruling identity,
  `N<=d-3+2b_1(B)`.
- **Hypotheses.** `B` reduced; local complement group generated by branch
  meridians; `A1` normalization for the `b_1` form of the Euler ledger.
- **Weakest failure mode.** The Euler ledger's fixed-point count `f_z` at
  exotic partitions; and `#Sing<=Delta_aff` needs each singular point to have
  `delta>=1`, which is automatic.
- **First falsification test.** Recompute `d=4` and demand exactly (3.6.2);
  this passes here.
- **Interface.** Integration `5d7df7ce...` Sections 3--6; promoted all-degree
  theorem `9579d3a1...`.
- **Score 8.** **Deliverable.** A short all-degree note with the two
  inequalities and their `d=4` specialization; it is the campaign's first
  `d`-monotone candidate.

### I5. Hamiltonian LND dichotomy on the pseudo-plane *(new, cross-avenue:
rows 29/30 x rank four)*
- **Implication.** The one-cusp horn requires a derivation with a slice that is
  not locally nilpotent; local nilpotence contradicts `Pic(U)=Z/mu`.
- **Hypotheses.** `O(U)` normal finitely generated of dimension two;
  `Pic(U)=Z/mu` with `mu>=2`; `U` smooth.
- **Weakest failure mode.** `Pic(U)=Z/mu` is charged with a hedge; and the
  dichotomy is a gate, not an exclusion.
- **First falsification test.** Compute `Pic(U)` exactly for the explicit
  hypersurface `x^r z=w^mu-1` mod its free `C_mu`-action; that is a finite
  divisor-class computation.
- **Interface.** Rentschler; Wright's slice theorem; Daigle/Makar-Limanov;
  Dubouloz--Palka Adv. Math. 339 (2018) 248--284 for the pseudo-plane class;
  charged `0e2e09c8...` Sections 2--5 and 9.
- **Score 8.** **Deliverable.** A sealed lemma "locally nilpotent Hamiltonian
  `=>` horn empty", with the exact `Pic(U)` computation.

### I6. Moh firewall for bounded invariant cells *(new, cross-avenue: row 5/6 x
the AWS programme)*
- **Implication.** Every normalized invariant-ring cell of pullback degree
  `<=100` is horn-empty by citation; the degree-eight AWS job is unnecessary.
- **Hypotheses.** Moh's `deg<=100` theorem; `deg_geo(H)=4mu>=8`.
- **Weakest failure mode.** Mis-citing Moh's hypothesis (per-coordinate vs
  maximum degree; whether the published bound is exactly 100).
- **First falsification test.** Pull the primary source and confirm the exact
  statement; then re-derive the degree-six cell's emptiness from it and check
  agreement with the charged AWS certificate.
- **Interface.** Moh, J. reine angew. Math. 340 (1983) 140--212; charged
  `RESULT.md`; charged `2531a89d...` Section 2.
- **Score 9.** **Deliverable.** A one-page firewall note plus a preflight
  check in the search harness that refuses any bounded plane-Keller cell below
  degree 101.

### I7. Leading forms in the graded pseudo-plane ring *(new)*
- **Implication.** A degree-independent obstruction, replacing bounded cells:
  the top-degree parts of `F_1,F_2` must Poisson-commute in `gr O(U)`, hence
  be algebraically dependent, hence proportional to powers of a common form
  lying in the leading-form algebra `L`.
- **Hypotheses.** `deg{f,g}=deg f+deg g-2` (verified for (5.1.2)); `L` is the
  graded algebra generated by the leading forms `x^2, x^3y, x^2y^2`.
- **Weakest failure mode.** Cancellation in the leading forms (the classical
  degenerate case), and the fact that `gr O(U)` is not a polynomial ring
  (`U^2=A^2Z` in the graded ring).
- **First falsification test.** The seven top-degree equations of the
  degree-eight cell are exactly the `2x2` minors of the `5x2` degree-eight
  coefficient matrix — I verified this. Check that the same pattern holds at
  degree ten before generalizing.
- **Interface.** Abhyankar--Moh leading-form theory; charged `0e2e09c8...`
  Section 8.3, which asks for exactly this pattern.
- **Score 7.** **Deliverable.** An explicit description of `L` and of which
  homogeneous elements of `L` are perfect powers.

### I8. Degree-congruence obstruction from the `C_mu` grading *(new)*
- **Implication.** `deg H_i` lies in a proper congruence class; combined with
  Nakai--Baba/Appelgate--Onishi divisibility this excludes whole degree pairs
  without any coefficient computation.
- **Hypotheses.** The invariant-monomial congruence `a+d b-r c = 0 mod mu`.
- **Weakest failure mode.** The congruence on degrees may be vacuous for some
  `(mu,r)`; it is nontrivial (`deg` even) at `(2,2)`, which is the case checked.
- **First falsification test.** Compute the degree semigroup of `O(U)` for
  `(mu,r)=(3,2),(3,3),(4,2),(5,2)` and see whether any is all of `N`.
- **Interface.** Charged `0e2e09c8...` (5.5)--(5.6); classical degree theory.
- **Score 6.** **Deliverable.** A table of degree semigroups by `(mu,r)`.

### I9. Embedding versus abstract curve — the gate is an embedding invariant
*(new, cross-avenue: rows 6 x 27)*
- **Implication.** The `S4` boundary gate depends on the *plane embedding*, not
  the abstract curve; so the search must enumerate re-embeddings, and a row
  killed in one embedding can survive in another.
- **Hypotheses.** Two delta-sequences with the same value semigroup can have
  different infinity knots (`(4,3)` and `(6,4,3)` both have `Gamma=<3,4>`;
  `(9,2)` and `(9,6,2)` both have `Gamma=<2,9>`), yet
  `T(3,4)` vs `C_(2,3)(trefoil)` and `T(2,9)` vs `C_(3,2)(trefoil)`.
- **Weakest failure mode.** Confusing the pole semigroup with the branch
  semigroup; the negative characteristic exponents at infinity are what make
  the two differ.
- **First falsification test.** Verify by hand that the `(6,4,3)` family, read
  through its degree-three approximate root, is the `(4,3)` family with
  `(a,b,c)=(3h,2h,c)` — I did this, see Section 12.2, and it independently
  reproves the charged `b1>=2`.
- **Interface.** Neumann, Invent. Math. 98 (1989); Rudolph; Assi--Garcia-Sanchez.
- **Score 7.** **Deliverable.** A short note fixing the dictionary and adding
  the "embedding, not abstract curve" warning to the campaign's fallacy list.

### I10. Fox/Picard localization at the surviving genus-four row
- **Implication.** Either kill `(9,6,2)` cohomologically or produce the first
  genuine nonzero locally extendable class.
- **Hypotheses.** The charged localization theorem
  `Pic({w^2=q_B})[3] = ker[H^1(A^2-B,L_sign) -> (+)_p H^1(M_p,F_3)]`.
- **Weakest failure mode.** `det C_(3,2)(trefoil)=9` passes the boundary
  screen, so this route will need the affine braid relations and every singular
  link, exactly as in the spectator control.
- **First falsification test.** Compute the affine sign-Fox space for one
  explicit `(9,6,2)` curve once `G4-1` produces it.
- **Interface.** Charged `60ba8f43...` (0.1)--(0.3) plus the corrigendum;
  spectator control `a25d4b2f...`.
- **Score 6.** **Deliverable.** A `F_3` Fox matrix for the first explicit
  `(9,6,2)` member.

### I11. The reducible source-forest rows `h>=2`
- **Implication.** Use `n22>=h-k+1` and `m>=2h-1` with idea I4: every `(3,1)`
  value sits at a singular point, so `Delta_aff(B) >= n22+m >= 3h-k >= 2h`.
  Since the branch is then a forest of `A1`s, the genus ledger and the
  `#Sing<=Delta_aff` bound may collide.
- **Hypotheses.** Charged (0.1) of `5d7df7ce...`; `k<=h`.
- **Weakest failure mode.** `Delta_aff` for a reducible branch is not the same
  invariant as for the irreducible one-place case, and the infinity link is not
  a knot, so the whole cable machinery is unavailable.
- **First falsification test.** Write the Euler ledger for `h=2,k=1` and see
  whether `N<=d-3+2b_1` is already violated.
- **Interface.** Charged (3.1), (6.1)--(6.2) of `5d7df7ce...`.
- **Score 5.** **Deliverable.** The `h=2` row table.

### I12. Strinz crosswalk against our own band ledger
- **Implication.** Either our band objects supply the missing adapter (a real
  cross-pollination win) or they do not (a clean negative that stops the lane).
- **Hypotheses.** None imported; only our frozen `.poly` rows are used.
- **Weakest failure mode.** Prose-to-theorem leakage. The controls in Section 8
  exist precisely for this.
- **First falsification test.** Q1 of Section 8, answered from our own data.
- **Interface.** Charged sweep `3b7e5db8...` only.
- **Score 4.** **Deliverable.** A one-page yes/no on Q1 with our own citations.

Cross-avenue or genuinely new: I1, I2, I3, I4, I5, I6, I7, I8, I9 — nine, well
above the required four.

## 10. Campaign and software improvements

**C1. A theorem-interface scope linter.** Every sealed artifact already lists
its charged interfaces in prose. Make that machine-readable: a small
`interfaces:` block naming, for each consumed theorem, its source, the exact
statement used, and the *direction* of use. My Lemma B is a case in point: it
uses a charged statement in the converse direction, which is legitimate but is
exactly the kind of move a reviewer must be pointed at. The linter should flag
any interface whose direction of use differs from the charging artifact's.

**C2. Automatic adversarial controls: a negative-control registry.** The
campaign keeps rediscovering that a control is needed (the nodal control, the
spectator, the `X=t^3,Y=t^(3r+1)(t+1)` family). Maintain
`controls/REGISTRY.md`: one row per exact control, with its invariants
(`Delta_aff`, `b_1`, `K_infinity`, `det`, local groups, `m`, Fox dimension,
`Pic[3]`) and the exact claims it refutes. Then *require* that every new
exclusion claim be run against every registry row whose invariants are
compatible, automatically. The spectator would have instantly shown that any
`m<=2` claim in stratum III is false, and my Section 3 argument would have been
forced into its correct `m<=1` form on the first draft rather than the second.

**C3. AWS packet scheduling with a mandatory classical preflight.** Before any
bounded coefficient job is scheduled, run a preflight that checks (i) whether
Moh/Nakai--Baba/Appelgate--Onishi already decides the cell, (ii) whether the
target is horn-relevant or merely stronger-than-needed, and (iii) whether a
cheap parameter-free coefficient exists (a 30-second symbolic scan, as in
Section 6.1). The degree-six job would have been correctly reclassified as
"redundant for the horn, useful as a strictly stronger certificate", and the
degree-eight job would have been cancelled. Also: with 192 stopped-and-ready
vCPUs and four idle running `r6*` nodes, the cheapest immediate win is to move
the higher-strand coloring rows of Section 4.2 there — they are embarrassingly
parallel, need no CAS, and produce byte-stable stdout.

**C4. Make replays carry their own validation corpus.** Every replay in this
area should re-derive a *charged* number before reporting its new number. My
coloring machine reproduces `0/24/72/0` before it reports `144/0/0`; that is
what makes its new outputs trustworthy without a second implementation. Make
this a hard requirement: a replay that computes only new numbers is not
evidence.

**C5. Improving the next ideation round itself.** Two concrete changes.
(a) *Charge the negative controls, not just the theorems.* This packet charged
the spectator artifact, which was decisive for me; it did not charge the threat
map, so I had to reconstruct `m<=1` from scratch (Section 3.6). That
reconstruction was valuable, but it was luck that it was feasible. Rule: any
numerical constraint the packet's overlay *relies on* must be charged or be
reconstructible from charged material, and the packet should say which.
(b) *Ask for one disconfirmation per idea.* The packet asks for a "weakest
likely failure mode", which invites a defensive answer. Ask instead for the
cheapest experiment that would *destroy* the idea, and require that it be run
if it costs under an hour. I ran that test for I1 (the spectator), I2 (the
conductor-six revalidation) and I6 (the degree-eight parameter scan); two of
the three changed my answer materially.

**C6. A standing "what would excluding this actually buy" field.** Each row of
the rank-four front should carry an explicit statement of what remains open if
the row closes. This is the discipline that keeps Section 2.3 honest.

## 11. Ranked next-wave allocation

Reviews are background; nothing below waits on one. "Provisional-consumable"
means a successor may build on the result before its hostile review returns.

| # | Task | Owner | Consumes | Provisional-consumable |
|---|---|---|---|---|
| 1 | Seal the `m=1` closure (I1): Lemmas A/B, four-stratum ramification table, `sympy` replay, and the independent `m<=1` Euler rederivation | Sol (coordinator or internal lane) | Section 3 | yes, by tasks 2--4 |
| 2 | Hostile review of task 1 — **must not be Opus** | Fable 5 | task 1 | n/a |
| 3 | `G4-1`/`G4-2`: exact `(9,6,2)` realizability and `b1=1` strata | internal agent | Section 4.3 | yes, by task 5 |
| 4 | Genus ladder producer + higher-strand rows on AWS | internal agent + AWS | Section 4.2, C4 | yes, by task 3 |
| 5 | Genus-four involution attack `G4-4`/`G4-5` | Grok 4.6 | tasks 3, 4 | yes |
| 6 | Moh firewall note (I6) and the search-harness preflight (C3) | internal agent | Section 6 | yes, immediately |
| 7 | Hamiltonian LND dichotomy (I5) incl. the exact `Pic(U)` computation | Opus 5 (separate lane) | Section 5 | yes, by task 8 |
| 8 | Leading forms in `gr O(U)` (I7) and degree congruences (I8) | GPT-5.5 | task 7 | yes |
| 9 | All-degree non-simple-fibre count (I4) | Sol | Section 9 I4 | yes |
| 10 | Hostile review of the genus ladder (I2) | GPT-5.5 or Grok | task 4 | n/a |
| 11 | Fox/Picard at `(9,6,2)` (I10) | internal agent | task 3 | yes |
| 12 | Reducible `h>=2` rows (I11) | internal agent | task 9 | yes |
| 13 | Strinz crosswalk Q1 only (I12) | Grok 4.6 | Section 8 | no — negative results only |
| 14 | Controls registry (C2) and interface linter (C1) | software lane | Section 10 | yes |

AWS: cancel the degree-eight cell. Schedule task 4 (coloring rows) on the four
idle `r6*` nodes immediately — it needs no CAS and finishes in minutes — and
hold the 192 stopped vCPUs for task 3's elimination if it outgrows a desk.

Parallelism note: tasks 1, 3, 6, 7, 9 are mutually independent and can start at
once. Task 5 is the only one with a hard dependency.

## 12. Corrections, cautions, and exact scope

### 12.1 The coordinator's conjectural extension is partly vacuous

Overlay item 5 asks for a proof using "the full length-two ramification
divisor", splitting on a double critical point versus two simple ones, with a
local `T22` sub-case at a conductor endpoint. Lemma A shows the double-critical
branch cannot occur in the charged `b1=1` packet, and the stratum table shows
the `T22` sub-case is never needed: in stratum II, where a critical point *is*
a conductor endpoint, the *other* critical point is a smooth point and settles
the row by itself. The extension as stated is therefore sound to attempt but
strictly harder than necessary; Section 3 is the shorter proof.

### 12.2 The `(6,4,3)` row, re-derived

Reading the charged `(6,4,3)` family through its own degree-three approximate
root (charged (4.5): `V^2-U^3-(3/4)c^2 h U=(c^3/64)(8t^3+24h t+9c)`) and
renormalizing puts it into the `(4,3)` normal form with

```text
a=3h,   b=2h,   c=c!=0,   so G(s)=s^3+4h s-c = H(s).     (12.2.1)
```

That is *literally* the charged self-pair cubic (0.5). Moreover `D(s)=-3s^2-12h`
vanishes only at `s^2=-4h`, where `G(s)=s(s^2+4h)-c=-c!=0`, so the family has
**no** diagonal roots: it is immersive (consistent with the charged
`Res(U',V')=-1728c^5`), every root of `G` is admissible, and a triple root is
impossible because `c!=0`. Hence `b1 = #distinct roots of G >= 2`. This
independently reproves the charged (0.7) by a completely different route, and
simultaneously confirms that `(6,4,3)` never meets my four strata (each of
I--IV forces `h=0` or `c=0`). I record this as a *confirmation*, not a
correction.

### 12.3 A caution I want on record

The value semigroup `Gamma={deg f : f in C[B]}` does **not** determine the knot
at infinity. `(4,3)` and `(6,4,3)` both have `Gamma=<3,4>` but infinity knots
`T(3,4)` and `C_(2,3)(trefoil)`; `(9,2)` and `(9,6,2)` both have `Gamma=<2,9>`
but `T(2,9)` and `C_(3,2)(trefoil)`. The reason is that characteristic
exponents at infinity may be negative, so the place at infinity is not a plane
branch germ. I nearly made this error while reconstructing the genus-four
census and think it belongs in the campaign's fallacy list under
"flag/place/series".

### 12.4 Exact scope of everything above

Nothing here proves or disproves JC2. Nothing here constructs a proper block, a
Keller counterexample, or any quartic cover. Section 3 closes one charged row
of one degree of one horn, at single-model tier. Section 4's genus exclusions
are statements about the irreducible one-place `A1`-normalised class with
transitive meridian-transposition `S4` monodromy, and say nothing about
reducible branches, several places at infinity, non-transposition inertia,
degrees other than four, or the primitive/no-proper-block case. Section 5 is a
gate, not an exclusion. Section 6 retires a computation; it does not close the
one-cusp horn. Section 9's ideas are proposals except where explicitly marked.
No result here is an exit claim, so no `charge_basis` line is declared. No
top-level ledger, sibling artifact, replay, or formalization tree was read or
modified; the only file written is this report.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `64290`.
- Body SHA-256:
  `a7cddda963362dc53bbb731748d79de86cf25f467a392a713c9b1b78966b01cd`.
- Frozen basis: `e40079bf3699311a3955486ee300197e1248d374`.
