# DO1-MU2-REPLAY: hostile replay of Domrina--Orevkov I

**Lane.**  The unique-dicritical transverse-degree-two branch of Domrina--
Orevkov, *On four-sheeted polynomial mappings of \(\mathbb C^2\). I*.  The
authority is the Russian publication, *Matematicheskie Zametki* 64:6 (1998),
847--862; printed pages correspond to repository PDF pages 1--16.

**Outcome.**  The conditional \(\mu=2\) exclusion survives a complete replay.
Its local and global censuses, determinants, and root placements close after
the named fills.  No step uses the adjacent \(\mu=1\) conclusion.  Thus

\[
\boxed{\texttt{DO-I-MU2 = REPLAYED-SOUND (after named local repairs).}}
\]

The order-three assembly instead binds to campaign Corollary 3.8;
Proposition 4.1 concerns only all-\(\mu=1\).

## 0. Custody, authority, and verdicts

The custody gate was run before any input was read.  The recomputed digests
were exactly

```text
6883978d6c24165de932c548acb1dfabde0492c0d8614ea4eb8734f14023bf1b  refs/domrina_orevkov1999_mzm_four_sheeted_I_russian.pdf
6ca30d797810400ddfcddb5b92b046796b3fdda5c1fb8f0ba378511506bbfed3  refs/domrina_orevkov1999_mzm_four_sheeted_I_orevkov_preprint.pdf
b838a2860c88d64d2a2162fd1a157e345db027bf4c7e95d2abae899dba9dc5de  [frozen]/domrina-ii-replay1-sol56-20260901.md
99fc1e5870fb74d48e3d14a156115ef625fa9ecbc5843f0d8dd4a138a920e9bf  [frozen]/domrina-gap-repair-opus5-20260901.md
```

The Russian first page verifies volume 64, issue 6, December 1998, p. 847.
Rendered pages control; OCR was only a locator and the English file only an
aid.  The assembly check also used Orevkov's three-sheet paper,
`refs/jc86.pdf`, SHA-256
`f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db`.

**REPLAYED-SOUND** means the displayed inputs imply the conclusion;
**REPAIRED** supplies a bounded missing implication; **GAP** means none was
found.  The \(\mu=2\) track has no GAP verdict.

No exit price is asserted, so `charge_basis` is inapplicable.  Branches,
points, components, and degrees remain separately typed.

## 1. What the source means by \(\mu=2\)

The source does not write \(\mu\).  Its Definition 3 (p. 851) assigns to a
nonconstant source component \(\widetilde l\)

\[
n(\widetilde l)=\text{generic transverse local degree},\qquad
m(\widetilde l)=\deg(F|_{\widetilde l}),\qquad
\operatorname{Deg}\widetilde l=m(\widetilde l)n(\widetilde l).
\]

Campaign \(\mu\) is the first quantity, \(n\), not \(m\).  The branch under
audit therefore starts with

\[
n(\widetilde g)=2,\qquad m(\widetilde g)=1,qquad
\operatorname{Deg}\widetilde g=2.                         \tag{1.1}
\]

The \(m_{\widetilde p}(\widetilde g)=1\) of Lemma 6 is instead the curve
map's local index at the physical point \(\widetilde p\).  The objects are

\[
\begin{array}{ll}
\widetilde L=\widetilde X\setminus\mathbb C^2,&
L=X\setminus\mathbb C^2,\\
\widetilde L_\infty=F^{-1}(L),&
\widetilde g\not\subset\widetilde L_\infty,\\
\widetilde p=\widetilde g\cap\widetilde L_\infty,&
p=F(\widetilde p)=g\cap L.
\end{array}
\]

Later, \(A=\widetilde L-\widetilde L_\infty-\widetilde g\) is a contracted
forest; \(\alpha=\det A\) is not its image point.

### 1.1 Exact location and numbering map

The order-two track begins in §2 on p. 852, after the order \(1,2,3\)
trichotomy, and ends with Theorem 1 on p. 862.  It occupies §§2--5.  The
published-to-preprint map is:

| Russian publication | English aid |
|---|---|
| Lemmas 1--5, formulas (2)--(8), pp. 849--852 | Lemmas 1.2, 1.4, 1.6, 1.7; (1.3), (1.8)--(1.10); Propositions 1.15, 1.17; Lemma 1.19 |
| Proposition 3; Lemma 6, pp. 853--854 | Proposition 2.1; Lemma 2.2 |
| Proposition 4; Lemmas 7--9; Corollaries 4--5, pp. 854--858 | Proposition 3.2; Lemmas 3.4, 3.6, 3.8; Corollaries 3.9--3.10 |
| Lemmas 10--11, pp. 858--860 | Lemmas 4.1, 4.6 |
| Lemmas 12--15, pp. 860--862 | Lemmas 5.1, 5.2, 5.5, 5.6 |

Russian Figs. 3--5, 6--11, 13--19, and 20--25 correspond respectively to
English Figs. 3(a--c), 4(a--f), 6(a--g), and 7(a--f).  Russian Fig. 26 is
English Fig. 8; Russian Figs. 27--28 are the two halves of English Fig. 9.

### 1.2 Publication/preprint divergences actually relevant here

Three differences matter.

1. Russian p. 852 says the order-one covering is unbranched **outside a
   finite set** (“`вне конечного множества точек`”); English p. 6 omits the
   qualifier.  Section 3 treats it.
2. The Russian definition on p. 849 calls a connected subgraph \(C\) linear
   only if every vertex of \(C\) has ambient valence at most two.  The English
   definition controls only non-end vertices of \(C\) and can admit nodal
   endpoints.  Lemmas 6 and 13--15 below use the stricter published meaning.
3. Published E (p. 853) imposes target minimality with a possible root
   exception.  The aid folds a stronger statement into (2d).  I use D+E.
All rendered determinant signs agree once extraction loss is ignored:
\(\det L=\det\widetilde L=-1\), Lemma 11 gives
\(\det\widetilde L_\infty=-2\), and Lemma 15 gives
\(\det\widetilde L_\infty=-1\).

## 2. What Domrina II consumes

The charged replay-1 ledger, frozen lines 810--840, identifies exactly two
textual uses:

| label | part-II text and role | exact payload |
|---|---|---|
| DO-I-1 | Introduction p. 1: part I proved the one-dicritical case impossible | historical scope gate |
| DO-I-2 | Proposition 1.2(1), p. 2: “The number of dicritical components of \(F\) is greater than 1 (see [4])” | load-bearing entry to every later two-dicritical construction |

Part II imports Theorem 1 of part I, not Lemma 8, Lemma 10, or another
internal \(\mu=2\) statement.  The authoritative theorem (p. 848) says:

> «Не существует четырехлистного локально обратимого полиномиального
> отображения … имеющего одну дикритическую компоненту.»

That is the exclusion of **exactly one** dicritical.  To obtain DO-I-2's
“greater than one,” one also needs the zero-case: if there is no dicritical,
the polynomial map is proper; a proper Keller map is finite étale over
\(\mathbb C^2\), hence has degree one.  A four-sheeted map therefore has at
least one dicritical, and Theorem 1 changes \(\ge1\) to \(>1\).
**DO-I-BINDING-MAP: REPLAYED-SOUND.**

Later two-dicritical labels and blocks inherit DO-I-2 once.  Subsequent
part-I citations are technical determinant imports, not new uses of the
exclusion (charged replay-1 lines 829--840, 854--858).

## 3. Entry seam and independence from the \(\mu=1\) sentence

The authoritative p. 852 first partitions the unique dicritical's transverse
order into \(1,2,3\), excludes 3 by “[3], remark to Lemma 5.3,” discusses 1,
and then says:

> «Таким образом, остается лишь случай ветвления порядка 2. … Из [3, лемма
> 4.2] вытекает, что \(m(\widetilde g)=1, n(\widetilde g)=2\).»

From this sentence onward, pp. 852--862 use (1.1), uniqueness of
\(\widetilde g\), resolution conditions A--E, and the general determinant and
canonical tools.  They never invoke “order one is a covering,” the
contradiction closing order one, or the conclusion “order one is impossible.”
Deleting the order-one paragraph and entering with (1.1) leaves every later
line unchanged.  Thus

```text
MU2-DEPENDENCE-ON-MU1 = REPLAYED-SOUND (NONE)
PROP-4.1-USE-INSIDE-MU2 = NONE
```

The terse \(m(\widetilde g)=1\) is not borrowed from the \(\mu=1\) case.  It
can also be checked rather than merely name-matched to [3].  Orevkov's Lemma
4.2 gives, for one dicritical at degree four,

\[
n(\widetilde g)+\sum_{x\ne\infty}
  \bigl(\mu_xF^*-n(\widetilde g)\bigr)=3.                 \tag{3.1}
\]

At \(n=2\), the finite correction total is one.  Condition A gives a single
point of \(\widetilde g\simeq\mathbb P^1\) above infinity.  If the curve map
had degree \(m>1\), Riemann--Hurwitz would leave finite longitudinal
ramification of total at least \(m-1\): the unique infinity point contributes
at most \(m-1\) to the total \(2m-2\).  A finite point of longitudinal index
\(r>1\) has two-dimensional local multiplicity at least \(2r\), and hence
contributes at least \(2(r-1)\) to (3.1).  The correction total would be at
least \(2(m-1)\ge2\), not one.  Therefore \(m=1\).
**MU2-ENTRY-(m,n)=(1,2): REPLAYED-SOUND.**

### 3.1 The adjacent order-one wording

The English claim “an unbranched covering over \(\mathbb C^2\)” drops the two
finite corrections allowed at \(n=1\); the Russian removes a finite set.
After also removing correction and contracted-component images, the resolved
map is a proper unramified degree-four cover with connected source, whereas
\(\mathbb C^2\) minus finitely many points is simply connected.  This is the
bounded completion; campaign inheritance uses Proposition 4.1 regardless.

Accordingly, the most precise ledger is

```text
DO-I-MU1-RUSSIAN-PUBLISHED = REPAIRED by the finite-set covering completion
DO-I-MU1-ENGLISH-AID       = DEFECTIVE STRONGER WORDING
DO-I-MU1-CAMPAIGN-BINDING  = REPAIRED independently by Proposition 4.1
```

Neither version enlarges Proposition 4.1's all-\(\mu=1\) scope or enters the
order-two proof.

## 4. Replay invariants and the two omitted structural proofs

Let \(\widetilde a\) be a fork, meaning
\(m(\widetilde a)>1\), and put
\(D=\operatorname{Deg}\widetilde a=mn\).  For a target vertex \(a\), formula
(9) on p. 854 is the generic-sheet identity

\[
\sum_{\widetilde a\in a'}\operatorname{Deg}\widetilde a=4. \tag{4.1}
\]

Thus a fork has only

\[
(D;m,n)=(2;2,1),(3;3,1),(4;4,1),(4;2,2).                \tag{4.2}
\]

At the three target directions \(X=L,R,D\), write the longitudinal index
partition of \(m\) as \((e_{X,1},\ldots,e_{X,r_X})\).  The source edge labels
are \(d_{X,j}=ne_{X,j}\), and

\[
\sum_j e_{X,j}=m,qquad
\sum_{X,j}(e_{X,j}-1)=2(m-1),qquad
r_L+r_R+r_D=m+2.                                        \tag{4.3}
\]

The middle equality is Riemann--Hurwitz for
\(F|_{\widetilde a}:\mathbb P^1\to\mathbb P^1\).  It is an equality, not a
floor, because Keller ramification is supported at the boundary contacts
already represented by the three fibers.

The one- and two-contact forms of published Lemma 5 say, for a constant-degree
block \(Q\) over target branch \(B\),

\[
\frac{\det Q}{\det B}=\frac{n(\widetilde a)}{\operatorname{Deg}Q}
 =\frac1e                                                     \tag{4.4}
\]

when the far endpoint is an end, and

\[
\frac{\det Q}{\det B}
 =\frac{n(\widetilde a)n(\widetilde b)}{\operatorname{Deg}Q} \tag{4.5}
\]

when it meets a second nonconstant vertex \(\widetilde b\).  A fractional
right side is therefore a contradiction only after the endpoint class has
been fixed.  This is the denominator control used in every census below.

Published Proposition 3 (p. 853) gives

\[
\det R_a=1,qquad \det D_a>1,qquad \det L_a>1,qquad
\det L=-1,                                                   \tag{4.6}
\]

and the indicated target branch determinants are pairwise coprime.  Here
\(\det L=-1\) follows from the sign convention \(\det(-A_L)\) and contraction
to the original \(+1\)-line.  The right unit and lower strict inequality are
the terminal splice and target-minimality E.  The left strict inequality is
the cited Abhyankar--Moh strict characteristic-sequence result under D; this
is a named structure input, not inferred from a drawing.

The edge formula used below is

\[
\det(ab)\det\Gamma=
 \det\operatorname{br}_a(b)\det\operatorname{br}_b(a)
 -\det(\Gamma-[ab])\bigl(\det\delta(ab)\bigr)^2.          \tag{4.7}
\]

For a blowup tree, branch determinants at one vertex are coprime; away from
the root all non-root branches but at most one have determinant one; and a
subgraph excluding the root has positive determinant (published Lemmas 2--4).
These foundational determinant/transfer statements (published Lemmas 1--5
and Propositions 1--2) are the charged structure package.  This lane checks
every application, hypothesis, sign, and integrality use; it does not
independently promote that package.

### 4.1 Proposition 4, printed without proof — REPAIRED

At a target nodal vertex of valence \(r\ge3\), let \(k_i\) be the number of
points of \(\widetilde a\) above its \(i\)-th incident direction.  Riemann--
Hurwitz gives

\[
\sum_i k_i=(r-2)m+2.                                     \tag{4.8}
\]

If source and target valences agree, the left side is \(r\), so
\((r-2)(m-1)=0\), hence \(m=1\).  Conversely \(m=1\) gives one unramified
longitudinal contact in every direction, equality of valences, and incident
chain degree \(n=\operatorname{Deg}\widetilde a\).  Finally, if every
incident chain has degree \(mn\), every local index is \(m\), so every fiber
has one point and (4.8) again gives \(m=1\).  This proves the printed
equivalence of Proposition 4(a)--(c).

### 4.2 Lemma 7, printed without proof — REPAIRED

Let forks \(\widetilde a,\widetilde b\) be joined by a degree-\(q\) constant
tube, and let the target vertex \(c\) lie beyond \(b\) from \(a\).  Take a
generic transverse disk at \(c\) and continue toward it the \(q\) sheets in a
proper neighborhood of the tube.  They stay inside
\(\operatorname{br}_{\widetilde a}(\widetilde b)\); any parting only
distributes sheets among distinct nonconstant vertices above \(c\).  Counting
each such vertex by its full local degree gives

\[
\sum_{\widetilde c\in c'\cap
\operatorname{br}_{\widetilde a}(\widetilde b)}
\operatorname{Deg}\widetilde c\ge q,                    \tag{4.9}
\]

which is published (10).  This is a conservation lower bound; no equality or
attainment is being assumed.

Lemma 6 is then immediate without mixing degree notions: degree one of the
curve map gives \(m_{\widetilde p}(\widetilde g)=1\), and Proposition 1 on the
published-linear transverse terminal chain gives degree
\(1\cdot n(\widetilde g)=2\).  **LEMMA 6: REPLAYED-SOUND.**

## 5. Complete local census (Lemmas 8--9)

For auditability I encode a local picture by

\[
L\mid R\mid D,
\]

where each entry is the partition of the longitudinal degree \(m\) in that
target direction; multiplication by \(n\) gives the edge labels actually
printed.  This records contacts, not vertices: a part can end, continue to a
fork, or ultimately reach \(\widetilde g\).  Those alternatives are resolved
only after (4.4)--(4.5), the coprimality statements, and (4.1) have been
applied.  Thus the enumeration does not silently turn representatives into
full branches.

### 5.1 Raw enumeration

Equation (4.3) gives the whole list before determinant pruning:

| \((m,n)\) | partitions in each direction | raw rows |
|---|---|---:|
| \((2,1)\) | one \(2\), two \(1+1\), with total five parts | 3 |
| \((3,1)\) | \(3,3,1+1+1\), or \(3,2+1,2+1\) | 6 |
| \((4,1)\) | triples of partitions of 4 with six total parts | 23 |
| \((2,2)\) | longitudinally \(1+1,2,2\); printed labels \(2+2,4,4\) | 3 |

The counts are respectively \(3\), \(3+3\), \(23\), and \(3\), hence 35.
For \((4,1)\), a direct check of the partition lengths
\((1,1,4),(1,2,3),(2,2,2)\), followed by choosing a partition of the stated
length, gives

\[
3+6(2)+\binom32^3=3+12+8=23.                         \tag{5.1}
\]

This supplies the enumeration behind the publication's “using (4), (5).”

### 5.2 Degrees two and three: published Lemma 8

For \(m=2,n=1\) the three rows, Russian Figs. 3--5, are

\[
2\mid2\mid11,\qquad 2\mid11\mid2,\qquad 11\mid2\mid2. \tag{5.2}
\]

The first has two endpoint blocks with the same nonunit determinant;
published Lemma 2 says those source branch determinants at
\(\widetilde a\) are coprime, so it dies.  In the second, (4.4)--(4.5) and
\(\gcd(\det L_a,\det D_a)=1\) force the left endpoint to be a fork and force
its transverse degree to be even.  Since its total degree is at most four and
its longitudinal degree is at least two, it has
\((m,n,\operatorname{Deg})=(2,2,4)\).  In the third, if both left contacts
ended, the two source branch determinants would both equal the same target
left determinant \(>1\), again contradicting coprimality.  At least one left
endpoint is therefore a fork; this row is held until the degree-three census.

For \(m=3,n=1\), the six rows, Russian Figs. 6--11, are

\[
111\mid3\mid3,\quad 3\mid3\mid111,\quad
21\mid3\mid21,\quad 3\mid111\mid3,\quad
21\mid21\mid3,\quad 3\mid21\mid21.                    \tag{5.3}
\]

They are exhausted as follows.

- The second row repeats a nonunit lower determinant in distinct branches and
  fails coprimality.
- In the third, the split left endpoint forced by (4.4) is a fork with even
  \(n\), hence total degree at least four.  The parallel lift in the same
  source branch contributes additional degree at the downstream target;
  Lemma 7 then violates the four-sheet identity (4.1).
- In the fourth, the analogous left fork has \(3\mid n\), hence total degree
  at least six, immediately violating (4.1).
- In the first, one of the three left endpoints must be a fork.  The two
  parallel unit lifts and (4.1), with Lemma 7 preventing their disappearance,
  force that fork to have total degree two.  Its degree-two neighborhood is
  the second row of (5.2), whose left endpoint has degree four.  All source
  routes from the original three left contacts would then have to pass
  through that same degree-four vertex.  They cannot do so in the tree
  \(\widetilde L_\infty\).

Return now to the third row of (5.2).  Its forced left fork has degree less
than four by (4.1) and Lemma 7, and it is not degree two by the just-excluded
first row of (5.3).  It is degree three, so its neighborhood is one of the
last two rows of (5.3).  After gluing, the two right branches shown in Russian
Fig. 12 must remain constant-degree tubes.  Indeed, a nearest further fork
toward either tube would have degree two by (4.1).  The middle row of (5.2)
would then force its left endpoint to have degree four, but that endpoint is
the already identified adjacent fork of degree three or two.  Since the
source graph is a tree, at least one of those two right
tubes misses the unique dicritical.  Its target right branch has determinant
one by (4.6), while the one-contact formula (4.4) assigns source determinant
\(1/2\), impossible.  This eliminates the deferred degree-two row.

Exactly the last two rows of (5.3), Russian Figs. 10--11, remain.  This
reproduces every case in published Lemma 8, including the two “analogously”
steps.  **LEMMA 8: REPLAYED-SOUND.**

### 5.3 Degree four: published Lemma 9

There are two factorizations.

For \((m,n)=(2,2)\), the longitudinal partitions are \(1+1,2,2\);
multiplication by \(n=2\) gives printed labels \(2+2,4,4\).  A split on the
left or below would repeat a nonunit determinant.  The only survivor of that
first filter, in printed labels, is

\[
4\mid22\mid4,                                           \tag{5.4}
\]

Russian Fig. 19.  The same transfer/coprimality calculation as in the
degree-two case forces its left endpoint to be a fork with even transverse
degree; the four-sheet cap gives the printed label \((m,n)=(2,2)\).  Applying
the classification there would require an unsplit degree-four right arm,
whereas (5.4) provides two degree-two arms.  The tree and (4.1) leave no
hidden arm.  Thus the \((2,2)\) factorization is impossible.

For \((4,1)\), determinant pruning can be replayed without trusting the
pictures.  On a nonunit left or lower target branch, a partition
\(1+1+1+1\) or \(2+1+1\) repeats a nonunit determinant and dies; the unit
right branch is exempt.  A \(3+1\) block forces its target branch
determinant to be 3, since the two coprime transfer factors are \(P/3,P\).
A \(2+2\) block forces it to be 2.  The target left and lower determinants
are coprime by Proposition 3.  An unsplit 4 over either of them forces that
target determinant even: (4.4) contributes denominator 4 at an end, while
(4.5) contributes \(4/n(\widetilde b)\) at a fork, with
\(n(\widetilde b)\in\{1,2\}\) by the degree cap.  Thus 4 cannot pair with 4
or \(2+2\); it can pair only with \(3+1\).  Consequently:

- with one left arm, that arm is 4, the lower partition must be \(3+1\), and
  the right partition is \(2+1+1\): Russian Fig. 13;
- with at least two left arms, the allowed triples are
  \(31\mid211\mid4\), \(31\mid31\mid22\),
  \(22\mid31\mid31\), \(22\mid22\mid31\), and
  \(31\mid22\mid22\): Russian Figs. 14--18 respectively.

That is six candidates, and the preceding factor analysis accounts for all
23 raw rows.  In the last two candidates the right partition is \(2+2\).
The nearest-fork argument used above shows both right arms are constant:
a degree-two fork would have the middle type in (5.2), whose degree-four
left endpoint is incompatible with the degree-four vertex currently of type
\((4,1)\); Lemma 8 supplies no other degree-two type.  One right arm misses
\(\widetilde g\) because \(\widetilde L\) is a tree, and (4.4) again produces
determinant \(1/2\) over the unit target right branch.  Russian Figs. 17--18
die; Figs. 13--16 survive.

It remains to justify Lemma 9(a), which controls possible unseen continuation
at a left endpoint.  If such an endpoint of degree below four were a fork,
Corollary 3 would require two right constant blocks, impossible at the single
left endpoint of \(U_{\widetilde a}\) in a tree.  For the unsplit left side of
Fig. 13, an endpoint fork of degree four would have to be one of Figs. 13--16,
but none has a right arm of degree four.  Hence it too is an end.  No
attainment was inferred from a lower bound.
**LEMMA 9 AND COROLLARY 4: REPLAYED-SOUND.**

## 6. From local neighborhoods to the six global graphs

Published Corollary 5 (p. 858) says only that Lemmas 6, 8, 9 and Corollary 4
“give the proof.”  Here is the missing assembly.

Start at the maximal degree-two constant block incident to
\(\widetilde g\).  If its other end were terminal, the other two sheets would
form a separate component: nonfork vertices cannot merge maximal blocks.
Connectedness of \(\widetilde L_\infty\) therefore forces a first merge, and
maximality makes it a fork.  Corollary 4 excludes a degree-two fork.  If the
first fork has degree four, its incident right
degree-two arm occurs only in local Figs. 13 or 14.  These give global Russian
Figs. 20 and 21.  Lemma 9(a) ends their left arms; all right packets already
meet at the sole degree-four lift, so another right join would cycle.

If the first fork \(A\) has degree three, it is local Fig. 10 or 11.  At the
same target vertex (4.1) requires exactly one distinct degree-one nonfork lift
\(A_0\), separate until its first join with the \(A\)-component.  That join is
strictly left: a fork on the degree-two packet closer to \(\widetilde g\)
contradicts the choice of \(A\), a merge of only unit packets would be a
degree-two fork excluded by Corollary 4, and the lower twig is terminal.  The
join is a fork because a degree-one vertex preserves valence by Proposition 4.

For local Fig. 11 the left packets have degrees 3 and 1.  Their first meeting
is a degree-four fork with right partition \(3+1\), so local Figs. 15 and 16
give global Figs. 22 and 23.  Lemma 9(a) ends the left arms, and another right
join would repeat the completed \(A\)-to-\(A_0\) join and cycle.  For local
Fig. 10, call its left packets
\(X=2,Y=1\) and the companion packet \(Z=1\).  A degree-four join of all three
would reconnect \(X,Y\), already joined at \(A\), and make a cycle.  A
degree-three fork \(B\) must take \(X\) and one unit; it must take \(Z\), since
taking \(Y\) again makes parallel \(A\)-to-\(B\) routes.  The unused \(Y\) is
the new companion \(B_0\).  Local Fig. 11 at \(B\) gives global Fig. 24 and
local Fig. 10 gives global Fig. 25.  If \(B\) is Fig. 11, its exposed
3-packet plus \(B_0\)'s
unit can only enter a degree-four \(3+1\) fork; that reconnects vertices
already joined through \(A\), hence cycles.  If \(B\) is Fig. 10, its exposed
packets are \(X'=2,Y'=1\), with companion \(Z'=1\).  A degree-four receiver
of all three creates parallel routes.  A degree-three receiver of
\(X',Y'\) repeats two strands from \(B\), while one receiving \(X',Z'\)
reconnects \(B\) to \(B_0\), already connected through the preceding spine.
Every continuation cycles; the list stops.

Thus the alternatives are exactly Russian Figs. 20--25, and the determinant
section has a complete input list.  **COROLLARY 5 (GLOBAL SIX-GRAPH CENSUS):
REPAIRED by the explicit assembly above.**

## 7. Elimination of the six global graphs

### 7.1 Russian Figs. 24--25: Lemma 10 — REPAIRED

Use the labels \(d_1,d_2,d_3\) in Russian Fig. 26 and let
\(\delta=\det\delta(ab)\) for its target \(a\)-to-\(b\) path.  At
\(\widetilde a_2\), two displayed branches already have determinant greater
than one.  The root-unit lemma therefore makes the remaining
\(\widetilde b_2\)-branch unit and places the root outside it.  The path from
\(\widetilde a_1\) to the root then runs through
\(\widetilde b_2,\widetilde a_2\); the displayed determinant-two nonroot
branch uses the sole nonunit allowance, so the root-unit lemma gives
\(d_1=1\).

The source cancels \(\delta^2\) without saying why it is nonzero.  The target
root lies strictly left of \(a\), hence outside the off-path forest
\(\delta(ab)\).  Lemma 4 gives \(\delta>0\); for an empty forest the
determinant convention is one.  This is the omitted premise.

Apply the edge formula first in the target tree and then transfer the labeled
constant blocks.  Let \(\widetilde L'\) be the component of
\(F^{-1}(\operatorname{br}_a(b))\) containing \(\widetilde b_2\).  With
\(d_1=1\) this gives

\[
 \det\operatorname{br}_{\widetilde b_2}(\widetilde a_2)
   =18d_3\delta^2-2d_2,
 \qquad \det\widetilde L'=d_2.                          \tag{7.1}
\]

Let \(\Delta=\operatorname{br}_{\widetilde a_2}(\widetilde b_2)
\cap\widetilde L_\infty\) and
\(y=\det\operatorname{br}_{\widetilde b_2}(\widetilde a_1)\).
The root exclusion just proved puts the root outside \(\Delta\), so Lemma 4
gives \(\det\Delta>0\).  The source edge formula, using (7.1), becomes

\[
y=\det\Delta+4d_3\delta^2>4.                            \tag{7.2}
\]

At \(\widetilde b_2\) the root branch points toward \(\widetilde a_2\), while
\(y>4\) uses the possible nonunit nonroot branch; the root-unit lemma therefore
gives \(d_3=1\).  The final whole-tree edge calculation is

\[
-2d_2=18\delta^2-2d_2-6y\delta^2.                      \tag{7.3}
\]

Since \(\delta>0\), (7.3) says \(y=3\), contradicting (7.2).  All signs were
checked in the rendered p. 859 equation; OCR drops the leading minus signs.

The paper disposes of Fig. 25 by “analogously.”  The required relabeling
swaps, at the left target node, the left/lower packets \((3d_1,2)\) and the
corresponding source packets, while preserving their product \(6d_1\).  The
singleton lift still has two nonunit branches, so the same root exclusion and
\(d_1=1\) hold; the root/nonroot roles just identified are preserved.
Equations (7.1)--(7.3), including coefficients 18, 4, and 6, are invariant
under that swap.  Hence Fig. 25 has the same
contradiction.  The printed proof is sound for Fig. 24 and is completed for
Fig. 25; the \(\delta>0\) premise is also supplied.

### 7.2 Russian Figs. 22--23: Lemma 11 — REPAIRED

For Fig. 22, transfer at the degree-four fork \(\widetilde b\) gives target
branch determinants \(\det L_b=3\), \(\det D_b=2\), and \(\det R_b=1\).
Published Proposition 2, after suppressing unit factors, reads

\[
\frac{\det\widetilde L_\infty}{\det L}
=4\left(\frac{1\cdot3}{3}\right)
  \left(\frac{1\cdot1}{2}\right)
  \left(\frac{\det(\widetilde b\widetilde g)}{\det R_b}\right).
                                                               \tag{7.4}
\]

Since \(\det L=-1\), this is
\(\det\widetilde L_\infty=-2\det(\widetilde b\widetilde g)\).
At the degree-three fork \(\widetilde a\), coprimality and transfer give
\(\det D_a=2\), source terminal determinants \(1,2,1,1\), and
\(3\det(\widetilde b\widetilde a)=\det(ab)\).  Proposition 2 applied inside
the ambient branch \((\widetilde b\widetilde g)\) then gives
\(\det(\widetilde b\widetilde g)=1\).  Consequently

\[
\det\widetilde L_\infty=-2.                             \tag{7.5}
\]

Let \(\alpha=\det A\), with the empty-forest determinant convention one.
The whole-tree edge formula on \((\widetilde a\widetilde g)\) now has the
form

\[
-1=-2\det\operatorname{br}_{\widetilde a}(\widetilde g)
-2\alpha\det\operatorname{br}_{\widetilde a}(\widetilde b)
       (\det\delta(\widetilde a\widetilde g))^2,         \tag{7.6}
\]

whose right side is even.  This contradicts the odd left side without any
positivity or attainment assumption.

For Fig. 23, interchange the local 3- and 2-packets at \(\widetilde b\).
The target product remains six, the lifted product remains three, and the
right degree-three calculation is unchanged.  Thus (7.4)--(7.6) repeat.
This supplies the source's omitted “same arguments.”

### 7.3 Russian Figs. 20--21: Lemmas 12--15 — REPAIRED

Write the boundary-supported canonical divisors as
\(\widetilde K=F^*K+B\).  The target dicritical image \(g\) is not an
interior boundary component, so its coefficient in \(K\) is zero; the
Jacobian divisor has coefficient \(n(\widetilde g)-1=1\) at
\(\widetilde g\).  Hence the coefficient of \(\widetilde g\) in
\(\widetilde K\) is one.  The source root lies in
\(\widetilde L_\infty\): the generic point of the original line at infinity
maps to target infinity under polynomial coordinates, and this containment
persists under the resolving blowups.  These checks license the canonical
and root identities in Lemmas 12--14.

Let \(\Delta\) be the maximal degree-two block from \(\widetilde g\), and
suppose \(\Delta\cap[\widetilde v\widetilde g]\) is nonlinear.  At its first
nodal vertex \(\widetilde v_1\) from \(\widetilde g\), put
\(d_v=\det\operatorname{br}_{\widetilde v_1}(\widetilde v)\), let \(d\) be
the third branch determinant, and put \(\alpha=\det A\ge1\).  Transfer gives
\(\det(\widetilde v_1\widetilde g)=2\); Proposition 3 gives
\(\max(d,d_v)>1\).

If \(d>1\), p. 861 cites published Lemma 4 for the unit
\(\widetilde g\)-branch.  Lemma 4 supplies positivity, not unity; the correct
citation is the root-unit Lemma 3, because \(d\) is the nonroot nonunit
branch.  The edge and canonical decompositions are

\[
-2=\det\widetilde L_\infty-\alpha d d_v,                \tag{7.7}
\]
\[
1=-1-\alpha-\det\widetilde L_\infty
  +\alpha(d-1)(d_v-1)+\alpha d\Sigma.                  \tag{7.8}
\]

Here \(\Sigma\) is exactly the remaining canonical sum; it is not assigned a
sign.  Eliminating the determinant yields \(d_v=d(\Sigma-1)\), contradicting
\(\gcd(d,d_v)=1\).  If \(d=1\), the nonunit lower determinant locates the root
below \(\widetilde v_1\), so \(d_v>1\) and the published-linear lower tail has
zero remaining canonical sum.  The edge formula gives
\(\det\widetilde L_\infty\ge0\), whereas the canonical formula gives
\(\det\widetilde L_\infty=-\alpha-2<0\).  Lemma 13 follows.

If the root lay in \(\Delta\), Lemma 13 would make the whole root-to-dicritical
path linear, and the same canonical decomposition would give
\(\det\widetilde L_\infty=-\alpha-2<-2\).  This contradicts (7.5) for the
middle pair and the value \(-1\) computed below for the remaining pair.
That is Lemma 14, with its hypothesis used in the correct direction.

Finally, in Fig. 20 the left packet is an unsplit 4, so its source determinant
is \(\det L_a/4\); the lower \(3+1\) packet has target determinant 3 and source
determinants 1 and 3.  In Fig. 21 these two packet roles are interchanged.
In both cases Proposition 2 gives

\[
\det\widetilde L_\infty=\det L=-1,\qquad
\det(\widetilde L_\infty-[\widetilde a\widetilde g])\ge3. \tag{7.9}
\]

Lemma 14 places the root outside \(\Delta\), and Lemma 13 makes the relevant
path linear.  Thus, with
\(B=\det\operatorname{br}_{\widetilde a}(\widetilde g)\ge1\) and the omitted
branch product \(C\ge3\), the final edge identity is

\[
-1=(-1)B-\alpha C\le-4,                                \tag{7.10}
\]

a contradiction.  The inequality uses only floors \(B\ge1,C\ge3\); it does
not promote either to an attained value.  This eliminates Figs. 20--21 and
completes the conditional \(\mu=2\) proof.

## 8. Main-theorem assembly and trust-boundary ledger

For one dicritical at degree four, Orevkov's exact budget is

\[
\mu+\operatorname{corr}=3,
\]

with \(\mu\ge1\) and \(\operatorname{corr}\ge0\).  Hence the three and only
three profiles are \((1,2),(2,1),(3,0)\).  They close as follows.

| profile | closing input | verdict |
|---|---|---|
| \((1,2)\) | campaign Proposition 4.1, exactly its all-\(\mu=1\) slice | **REPAIRED** |
| \((2,1)\) | §§2--7 of the authoritative part-I text, with the bounded fills listed below | **REPAIRED** |
| \((3,0)\) | campaign Corollary 3.8, `xmodel/b0-trivial-dicritical-proof-opus5-20260831.md:312--321`, independently confirmed in `xmodel/b0-proof-hostile-review-sol56-20260831.md:246--249` | **REPAIRED**: replaces Orevkov's unproved closing Remark |

This is exhaustive arithmetic, not a cap or analogy.  Proposition 4.1 does
not touch the second or third row.  Conversely, no conclusion from the first
row occurs in the proof of the second.  With the standard zero-dicritical
proper/finite-etale exclusion from §2, part-I Theorem 1 therefore supplies
exactly the statement used by part-II Proposition 1.2.

The repairs are the proofs of Proposition 4 and Lemma 7, the quotient-tree
gluing behind Corollary 5, \(\delta(ab)>0\) in Lemma 10, the three omitted
companion cases, and the Lemma 13 citation correction.  The 35-row census and
endpoint checks are replay expansions, not extra repairs.  None imports the
disputed \(\mu=1\) inference.

The requested typed dispositions are therefore

```text
CHECK-1[LOCATION-AND-DO-II-BINDING] = REPLAYED-SOUND
CHECK-2[COMPLETE-MU2-REPLAY]        = REPAIRED[PROP4; LEM7; COR5;
                                               LEM10-DELTA; COMPANIONS;
                                               LEM13-CITATION]
CHECK-2[MU1-CONTAMINATION]          = REPLAYED-SOUND (NONE)
CHECK-3[PART-I-THEOREM-ASSEMBLY]    = REPAIRED[MU1->PROP-4.1;
                                                 MU3->B0-COR-3.8]
DO-I-MU2                            = REPLAYED-SOUND (+ named local repairs)
DO-I-ONE-DICRITICAL-BOUNDARY        = THEOREM MODULO NAMED REPAIRS
                                        AND CHARGED STRUCTURE PACKAGES
```

No `GAP-CANDIDATE[DO1-MU2-*]` remains.  This promotes only the part-I
inheritance, not Domrina II's unaudited later half or campaign-wide closure.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `34582`.
- Body SHA-256:
  `d4b19f80f6db58b2dd14363e2202ec182ee6106e9dbaf63c8841cbd576dd854a`.
- Frozen basis: `4252acc58f89a5cc6047b7f2215bab3278911407`.
