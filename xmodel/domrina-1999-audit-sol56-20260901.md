# DOMRINA-1999 urgent audit: the published \(N=4\) claim versus the campaign

## 0. Audit controls and executive disposition

The three frozen inputs passed the required byte gate before inspection:

| frozen input | required and observed SHA-256 |
|---|---|
| `domrina1999_mathnotes65_four_sheeted_general_case.pdf` | `fd73196e85aefd93764fb3994c78bd8d763da03820e3beff623e698e90cfd43a` |
| `block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md` | `46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc` |
| `block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md` | `763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9` |

**Disposition.** The 1999 paper unmistakably announces the unconditional
four-sheet exclusion, but its four pages are an outline, not a stand-alone
proof: Propositions 1--2 are stated, Proposition 3 is called easy, Propositions
4--5 are transferred by analogy, and the root-location and terminal
canonical-class calculations are omitted. The announcement therefore has
status `CLAIMED/FULL-THEOREM; PROOF-ON-PAGE=INCOMPLETE-OUTLINE`.

The acquisition premise changed during this audit. A byte-valid official English
copy of the 33-page sequel became available as
`refs/domrina2000_izv64_four_sheeted_general_case.pdf`; I independently
verified 408,814 bytes, 33 pages, a clean `qpdf --check`, and SHA-256
`0be24c5c6a9cc9423c3049c3402f2c98e44bac5f1c6018b3999989e0f32e5018`.
It substantially expands every announced stage. It also expressly imports
Domrina--Orevkov I's exclusion of the one-dicritical case, so it does not repair
the campaign-audited author inference in that input. Several finite
classification/calculation passages in II remain compressed by analogy or
omission; this audit spot-checked their role but did not replay all 33 pages.
Thus `DOMRINA-II-HOSTILE-SOUNDNESS=AUDIT-OPEN`, not `GAPPED`.

The work was desk-scale: hashing, PDF structural/text inspection, exact
arithmetic already printed in the sources, and literature retrieval. No CAS was
used and `jc2-lean` was not inspected.

The literature posture is nevertheless strong. A refereed 2008 paper by
Żołądek both treats Domrina--Orevkov as proved and gives a different proof of
the stronger topological-degree-at-most-five theorem. Sigray's 2008 thesis
states a distinct degree-at-most-five route, but the campaign's existing audit
finds that proof incomplete as printed. Later papers use six as the known
lower bound for a counterexample. Accordingly, `N=4-LITERATURE=CLOSED`
is the correct present research posture; that sociological/provenance status is
not a substitute for a line audit of Domrina II.

The charged campaign is not yet a complete independent proof of \(N=4\).
It has a rigorous repair of the known μ=1 inference, a sharper analysis once
inside the mixed two-component residual, and ROW-KILL on the explicit
EXHAUST families. The frozen all-degree integration still records a missing
campaign pin, shape tails, and six AM-numerical candidates. Its correct status
is `INDEPENDENT-PARTIAL/OPEN`, not “first rigorous full treatment.”

## 1. Bibliographic identity and claim scope

The charged item is A. V. Domrina, *On Four-Sheeted Polynomial Mappings of
\(\mathbb C^2\). The General Case*, *Mathematical Notes* **65**:3 (1999),
386--389, translated from *Matematicheskie Zametki* **65**:3, 464--467,
received 7 May 1998; DOI
[10.1007/BF02675082](https://doi.org/10.1007/BF02675082). Its theorem is exact
and unconditional:

> A polynomial map \(f:\widetilde{\mathbb C}^{\,2}\to\mathbb C^2\) of
> topological degree four cannot have non-zero constant Jacobian.

Here topological degree is generic fibre cardinality, not total polynomial
degree. The introduction says Domrina--Orevkov I handled maps having one
dicritical component and that this note handles “the remaining cases.” Hence
the advertised full theorem is the union of an imported one-dicritical result
and the note's residual analysis; a defect in the imported result is a defect in
that particular proof chain even if the two-dicritical part is sound.

The full publication is A. V. Domrina, *On four-sheeted polynomial mappings of
\(\mathbb C^2\). II. The general case*, *Izvestiya: Mathematics* **64**:1
(2000), 1--33, DOI
[10.1070/IM2000v064n01ABEH000273](https://doi.org/10.1070/IM2000v064n01ABEH000273).
Its [official record](https://www.mathnet.ru/eng/im273) says explicitly that the
paper proves nonexistence of a four-sheeted constant-Jacobian map.

## 2. Complete four-page announcement outline

### 2.1 Set-up and Proposition 1

Assume a degree-four Keller map exists. Blow up at infinity until it extends to
a regular map \(F:\widetilde X\to X\) between smooth compact surfaces whose
boundaries \(\widetilde L\) and \(L\) are SNC unions of rational curves. Put
\(\widetilde L_\infty=F^{-1}(L)\), call a component of
\(\widetilde L-\widetilde L_\infty\) dicritical when \(F\) is nonconstant on
it, and impose the minimality convention from [4], Domrina--Orevkov I.

**Proposition 1.** There are exactly two dicritical components
\(\widetilde g_1,\widetilde g_2\). The restriction of \(F\) is locally
biholomorphic on their affine parts; their transverse ramification orders are
respectively 1 and 2; and

\[
 \widetilde L=\widetilde L_\infty+\widetilde g_1+\widetilde g_2.
\]

Each \(\widetilde g_i\) meets \(\widetilde L_\infty\) once. In [4]'s notation,
made explicit in II, this separates restriction degree
\(m(\widetilde g_1)=m(\widetilde g_2)=1\) from transverse orders
\(n(\widetilde g_1)=1,n(\widetilde g_2)=2\); it must not be read as identifying
a source dicritical, its physical point at infinity, and a cover series.
There is no proof in the announcement.

### 2.2 Proposition 2: target splice diagram

**Proposition 2.** Each image \(g_i=F(\widetilde g_i)\) meets \(L\)
transversally once. The splice diagram of \(g_1\cup g_2\) near \(L\) is one of
Figs. 1--3, with the right arrow \(g_2\) and upper arrow \(g_1\). If \(p\) is a
nodal vertex, \(R_p,L_p,D_p,A_p\) denote its right, left, lower, and upper
branches, respectively; each branch may be empty. All of the following are
asserted:

1. \(\det L=-1\).
2. If \(p\in A_h\), then \(\det A_p=1\) and \(\det R_p>1\).
3. If \(p\in L-A_h\) and \(p\ne h\), then
   \(\det R_p=1,\ \det D_p>1,\ \det L_p>1\).
4. In Fig. 1,
   \(\det A_h=\det R_h=1\) and \(\det D_h,\det L_h>1\).
5. In Fig. 3, \(\det A_h\ne1\) implies
   \(\det R_h=1,\ \det L_h>1\).

The following unnumbered consequence is then taken from [4, Lemma 6]: the
linear chain incident to \(\widetilde g_1\) has degree 1 and the one incident to
\(\widetilde g_2\) has degree 2. Neither Proposition 2 nor its three-diagram
exhaustiveness is proved on-page.

### 2.3 Definition 1 and Proposition 3: the enlarged blocks

For \(a\in L\), define

\[
 a'=\{\widetilde a\in F^{-1}(a):F|_{\widetilde a}\text{ is nonconstant}\},
 \qquad A'=F^{-1}(A_h).
\]

A maximal constant-degree subgraph is one not properly contained in another
constant-degree subgraph. A vertex is a fork when
\(m(\widetilde l)>1\). **Definition 1** takes
\(\widetilde h\in h'\), assuming either \(m(\widetilde h)=1\), or both
\(\det A_h=1\) and \(L\) has Fig. 2 or 3. If \(m(\widetilde h)\ne1\), the block
\(\widetilde\Delta_{\widetilde h}\) consists of all maximal constant-degree
subgraphs incident to \(\widetilde h\), together with incident components of
\(A'\). If \(m(\widetilde h)=1\), use instead the maximal constant-degree
subgraph containing \(\widetilde h\), again with the incident components of
\(A'\). The boundary is claimed to decompose into forks connected by:
maximal constant-degree blocks disjoint from \(h'\), components of \(A'\), and
these \(\widetilde\Delta\)-blocks.

**Proposition 3.** Every such connecting block \(\widetilde Q\) is incident to
at most two vertices of \(\widetilde L_\infty+\widetilde g_2\), and \(F\) is
nonconstant on each incident vertex. If the incident set is
\(\{\widetilde a\}\), then

\[
 \det\widetilde Q={n(\widetilde a)\over\operatorname{Deg}\widetilde Q}
                   \det F(\widetilde Q);
\]

if it is \(\{\widetilde a,\widetilde b\}\), then

\[
 \det\widetilde Q=
 {n(\widetilde a)n(\widetilde b)\over\operatorname{Deg}\widetilde Q}
 \det F(\widetilde Q).
\]

Every linear chain \(\widetilde T\subset\widetilde Q\) incident to one of
those vertices satisfies
\(\operatorname{Deg}\widetilde T=\operatorname{Deg}\widetilde Q\). The text
only says this is “easy to show.” It then deduces from Proposition 3 and [4,
Proposition 1] that, when \(\det A_h=1\), every component of \(A'\) has
determinant 1 and does not contribute to the right-hand side of [4, formula
(5)]; these components are suppressed in later figures. It also observes that
in the one-dicritical case, maximal constant-degree subgraphs satisfy
Proposition 3.

### 2.4 Proposition 4: local fork census

For a fork \(\widetilde a\) not already in one of the three block classes, let
\(U_{\widetilde a}\) be it plus all incident blocks. Its central label is
\((m(\widetilde a),n(\widetilde a))\); each incident edge is labelled by block
degree and placed left/right/down according to its target image. The note
observes that [4] had pairwise coprimality of all lower and relevant left
determinants, whereas here those determinants are pairwise coprime with at
most one determinant excepted, because one branch can meet
\(\widetilde g_1\).

**Proposition 4.** The local diagram is one of [4, Figs. 10, 11, 13--16] or
new Figs. 4--9. The new central/edge data printed are:

| figure | central label | incident degrees |
|---|---|---|
| 4 | \((2,1)\) | horizontal \(2,2\); lower \(1,1\) |
| 5 | \((2,1)\) | right \(2\); left \(1,1\); lower \(2\) |
| 6 | \((4,1)\) | right \(4\); left \(2,1,1\); lower \(3,1\) |
| 7 | \((4,1)\) | right \(4\); left \(3,1\); lower \(2,1,1\) |
| 8 | \((2,2)\) | horizontal \(4,4\); lower \(2,2\) |
| 9 | \((2,2)\) | right \(4\); left \(2,2\); lower \(4\) |

In Figs. 4, 7, 8, \(\widetilde g_1\) is incident to a lower branch; in Figs.
5, 6, to a left branch. In Figs. 6, 7,
\(\operatorname{Deg}(\widetilde a\,\widetilde g_1)=1\), using [4]'s
branch-intersection notation rather than an ordinary path. In Fig. 9, \(a\)
lies right of \(h\). For distinct vertices \(a,b\) of a tree \(\Gamma\), that
notation is
\((ab)=\operatorname{br}_a(b;\Gamma)\cap\operatorname{br}_b(a;\Gamma)\).
The sole proof indication is to repeat [4, Lemmas 8--9] *mutatis mutandis*
despite the weakened coprimality condition.

### 2.5 Proposition 5 and the omitted contradiction

**Proposition 5.** Collapse Fig. 4/5 blocks to degree-2 edges and Fig. 8 blocks
to degree-4 edges, retaining the other local diagrams. Then
\(\widetilde L_\infty+\widetilde g_2\) has one of [4, Figs. 20--25] or new
Figs. 10--12. Their complete printed degree data are:

- Fig. 10 has two \((4,1)\) vertices joined by degree 4. At the left vertex,
  the left branches have degrees \(3,1\), and the lower branches \(1,1,2\).
  At the right vertex, the right branches have degrees \(1,1,2\), with the
  degree-2 branch ending at the open circle, and the lower branches \(3,1\).
- Fig. 11 again has two \((4,1)\) vertices joined by degree 4. At the left
  vertex, the left branches have degrees \(2,1,1\), and the lower branches
  \(3,1\). The right vertex has the same incident data as in Fig. 10.
- Fig. 12 joins a \((2,2)\) vertex to a \((4,1)\) vertex by degree 4. The
  \((2,2)\) vertex has two left branches of degree 2 and one lower branch of
  degree 4. The \((4,1)\) vertex has right branches \(1,1,2\), with the
  degree-2 branch ending at the open circle, and lower branches \(3,1\).

The only justification is “as in [4, Corollary 5].” For new Figs. 10--12,
\(\widetilde g_1\) corresponds to a uniquely determined edge under the note's
edge-identification convention; for inherited [4, Figs. 20--25], several
positions can occur.

The allowed placement of \(\widetilde g_1\) is then split exhaustively as
follows. If its incident block \(\widetilde Q\) is represented by an edge and
is horizontal, then \(\widetilde Q=\widetilde\Delta_{\widetilde h}\), or
\(\operatorname{Deg}\widetilde Q=2\), or its degree is 4 and its local diagram
is Fig. 4, 6, or 8. If it is lower, then \(\widetilde Q\subset A'\), the target
is Fig. 3, \(\det A_h>1\), and the incident \(\widetilde h\in h'\) is a fork.
If its block is not represented, the target is Fig. 1 and the incident
\(\widetilde h\) is a fork. (The printed “if ... lower than” is evidently a
translation/typesetting slip for “then”; the text also once calls
\(\widetilde g_1\) an edge.) These placement claims are not proved.

Finally, for every global diagram and allowed placement, the note says one
first proves that the root of \(\widetilde L\) lies in the source-defined
branch-intersection subgraph \((\widetilde g_1\widetilde g_2)\), inserts [4,
canonical-coefficient
formulas (3)] at the two dicriticals, obtains an equation, and checks that the
diagram data cannot satisfy it. No root proof, equation, complete placement
table, or numerical check appears. This is the actual terminal exclusion, so
the four-page item is properly an announcement of a splice-diagram proof.

## 3. Step-by-step comparison with the promoted campaign machinery

The overlap is real but sharply localized. The following table uses “match”
only for a proved numerical/component conclusion, not for an identification of
a dicritical flag, a physical place, and a covering series.

| Domrina outline step | closest promoted campaign content | relation |
|---|---|---|
| imported one-dicritical exclusion | B0 Proposition 4.1; B0 Corollary 3.8 | repairs two suspect low-degree inferences, described below |
| Proposition 1: two dicriticals, restriction degrees 1, transverse orders 1 and 2, one point at infinity | repaired B0 Theorem 4.3 residual: two source dicriticals with \((\mu,\mathrm{corr})=(2,0)+(1,0)\), \(s_1=s_0=1\), both target normalizations \(\mathbb A^1\) | conditional structural match after entering the campaign's mixed \(\mu=1\) residual; not a derivation from an arbitrary \(N=4\) candidate and not Domrina's compactification identity |
| Proposition 2: three target splice diagrams, transversal boundary intersections and determinant inequalities | one-place/normalization conclusions; branch-curve local monodromies are disjoint transpositions | partial geometric agreement only; no campaign proof of her target diagrams or determinants |
| Proposition 3: edge-block incidence and determinant/degree formulas | no promoted equivalent | unproved by the campaign |
| Proposition 4: exhaustive local fork diagrams under one exceptional coprimality pair | no promoted equivalent | unproved by the campaign |
| Proposition 5: exhaustive global diagrams and \(\widetilde g_1\) placements | no promoted equivalent | unproved by the campaign |
| root location plus canonical-divisor contradictions | no promoted equivalent | the campaign uses a different obstruction |

Once the campaign analysis has entered its mixed \(\mu=1\) residual, B0 is
slightly sharper in the affine direction: write
\(A_F=D_1\cup D_0\), with \(D_1\) the ramified image and \(D_0\) the
unramified-\(\mu=1\) image. Their normalizations are \(\mathbb A^1\); \(D_1\)'s
singularities are double points with smooth branches, \(D_0\) misses those
incidences, and the local monodromies are disjoint transpositions. This agrees
with the component/order core of Proposition 1. It does **not** by itself prove
\(\widetilde L=\widetilde L_\infty+\widetilde g_1+\widetilde g_2\), the exact
target compactification, or transversal meeting with its \(L\). Also, the
campaign's rank-four irreducibility theorem concerns the reduced charged
branch \(B\), not irreducibility of \(A_F\); the unramified component \(D_0\)
is not part of that branch locus.

### 3.1 The known Domrina--Orevkov I defect and its repair

The reviewed registry records the exact problem at
`xmodel/trivial-dicritical-literature-registry-grok46-20260831.md:100-130`.
In the unique-dicritical degree-four case, D--O I says transverse order 3 is
impossible, says order 1 would make \(F\) an unbranched covering of
\(\mathbb C^2\), and retains order 2. The \(\mu=1\) sentence is an author inference,
not the cited Orevkov theorem: Orevkov's version has vanishing corrections,
whereas the unique μ=1 degree-four budget forces correction total 2.

The campaign supplies safe replacements:

- B0 Proposition 4.1 proves that an all-μ=1 profile is impossible. Its proof
  keeps the finite correction set visible and uses purity, equivalently simple
  connectivity after removing finitely many points, rather than pretending the
  map is already unbranched over all of \(\mathbb C^2\).
- B0 Corollary 3.8 proves the separate closing assertion that
  \(\mu=N-1\) is impossible, rather than importing Orevkov's unproved remark.
- Within the mixed \(\mu=1\) lane, repaired B0 Theorem 4.3 derives the
  \((2,0)+(1,0)\) residual. It is not an entry theorem from an arbitrary
  \(N=4\) candidate. Under H2 (\(A_F\) irreducible), Theorem 4.2 excludes
  \(\mu=1\) at \(N=4\).
- The all-degree Theorem 7.B, at frozen
  `block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md:22-35`,
  proves under H2 and
  \(N\ge3\) that no affine-image dicritical has \(\mu=1\). It does not apply to
  reducible \(A_F\).

This repairs the flagged D--O I μ=1 inference and conditionally corroborates
Domrina's residual starting profile inside the mixed lane. It does not
eliminate D--O I's surviving
unique-μ=2 case by B0 alone, and it does not prove Domrina's Propositions
2--5.

### 3.2 ROW-KILL/EXHAUST is a different proof engine

Nothing in the announcement contains the content of ROW-KILL/EXHAUST. Its
explicit keywords and every displayed construction point instead to
resolution trees, Eisenbud--Neumann splice diagrams, determinants,
coprimality, finite graph enumeration, and canonical-class coefficients.

The campaign route is affine and algebraic/topological. EXHAUST says that a
one-place curve **already certified in the reviewed gauge** lies, after a target
automorphism, in one of the explicit normal-form families (charged all-degree
snapshot, lines 36--41). ROW-KILL then proves for the explicit sextics

\[
x=(t^3+bt+c)^2,\qquad
y=t^4+\tfrac{2b}{3}t^2+\tfrac{4c}{3}t,\qquad c\ne0,
\]

and their specified \((8,4)\) automorphic images that no meridional
\(S_4\)-quotient exists. Its chain is exact singularity stratification,
NO-TORUS, the \(S_3\) resolvent, infinity-word triviality, projective-cover
descent (generalized Riemann existence, normality, miracle flatness), and
Shirane's torus-type obstruction; see charged
`block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md:32-53`.
This is neither a transcription nor a hidden instance of Domrina's
canonical-divisor case check. Where applicable it bypasses her Propositions
2--5.

The bypass is not yet exhaustive campaign-wide. The frozen all-degree ledger
retains `OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]`, three higher shape tails,
`OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]`, and six AM-numerical candidates
(`block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md:42-51,65-86`).
Its SHAPE-KILL narrowing is itself explicitly `PROVISIONAL` in the charged
snapshot pending review. Therefore the licensed phrase is “six candidates
plus the typed shape residuals,” never “exactly six.”

## 4. Soundness requirements for the full Izvestiya II proof

The official sequel is not merely a reprint of the announcement. Its actual
architecture is:

| announcement item | expansion in II |
|---|---|
| set-up and minimality | Proposition 1.1 |
| Proposition 1 | Proposition 1.2 and Proposition 1.3(1) |
| Proposition 2 | Proposition 1.3(2) and Corollary 1.4; Lemma 1.5 gives the incident-chain degree statement |
| root/canonical preparation | Lemmas 2.1--2.12, including explicit canonical-coefficient and determinant equations |
| Definition 1 / Proposition 3 | Definition 3.2, Proposition 3.4, Assertions 3.5--3.6, Lemma 3.7, Corollary 3.8, and Assertion 3.9 |
| Proposition 4 | Assertion 3.11 and Lemmas 3.12--3.13 |
| Proposition 5 | Lemma 3.14 gives the global Fig. 11 list; Lemmas 3.15--3.16 add auxiliary constraints for the terminal eliminations |
| final prohibition | §§4--7 eliminate respectively Fig. 11 classes 2a--b, 1a--d, 3a--b, and 4a--b; Lemma 7.11 concludes none is realizable |

For example, II's Proposition 1.2 explicitly gives
\(m(\widetilde g_1)=n(\widetilde g_1)=1\) and
\(m(\widetilde g_2)=1,n(\widetilde g_2)=2\). It proves the “remaining case”
profile using Orevkov's Lemmas 4.2 and 5.2 and simple connectivity of
\(\mathbb C^2\) minus finitely many points. Proposition 1.3 derives the target
diagram by resolving \(g_2\), then \(g_1\), and cites [4] for the determinant
properties. Section 3 formally defines “edge type,” proves substantial block
lemmas, derives a local Fig. 8 census and a global Fig. 11 census. Printed
pp. 16--32 contain the diagram-by-diagram determinant and canonical-class
contradictions. Thus the principal omission in the announcement is genuinely
filled in the journal sequel.

For the *full theorem* to stand through Domrina's own chain, however, all of
the following load-bearing obligations must survive review:

1. **Imported base case.** [4]'s assertion that one dicritical is impossible
   must be valid. II says this was proved and uses “the number ... is greater
   than 1”; it does not reprove it. The campaign's Proposition 4.1 is a valid
   replacement for the flagged μ=1 subcase, but that replacement is external
   to the printed proof.
2. **Residual profile.** Proposition 1.2 must exclude every alternative
   number/order profile and every contracted affine component; Proposition
   1.3 must give exactly the target diagrams and determinant inequalities.
3. **Block identities.** Definition 3.2's determinant formulas and equal-degree
   chain condition must apply to every claimed block, including the enlarged
   \(U^0\) and \(\widetilde\Delta_h\) blocks.
4. **Local exhaustiveness.** The change from full pairwise coprimality to
   allowing at most one exceptional determinant must yield exactly the local
   Fig. 8 types, with no lost fork or \(\widetilde g_1\) placement.
5. **Global exhaustiveness.** Lemmas 3.13--3.14 must glue those blocks into
   exactly Fig. 11, without identifying distinct source vertices merely
   because their image or degree labels coincide.
6. **Root and terminal arithmetic.** The root-location lemmas, signs and
   positivity hypotheses for each determinant formula, canonical coefficients
   at both dicriticals, and every finite numerical elimination in §§4--7 must
   cover every case once and actually contradict integral graph data.

The full paper still has audit-sensitive compression. Lemmas 2.5--2.6 and
2.10--2.11 are said to be analogous to earlier lemmas; Lemma 3.12 begins “we
omit the details” because they are analogous to [4, Lemma 8]; Assertion 6.3 is
transferred from Assertions 5.1--5.2; Lemma 6.10 is transferred from two prior
eliminations; §7 omits intermediate calculations as similar to [4, Lemma 10];
and the last essential branch of Lemma 7.10 says only that successive
consideration of all cases makes equation (7.12) impossible. These are
specific replay targets, not findings of falsity. Until the figures,
determinant maps, and those analogies are independently reconstructed, the
soundness type is `OPEN-AUDIT`, while the publication's claim type remains
`PUBLISHED-AS-PROVED-IN-REFEREED-SOURCE`.

## 5. Literature reception and acceptance status

The answer to “is Domrina cited as proved?” is **yes**, with unusually explicit
evidence.

- The official [MathNet record for Domrina
  II](https://www.mathnet.ru/eng/im273) labels it a 33-page *Izvestiya:
  Mathematics* article and states in the abstract that it proves nonexistence
  of four-sheeted constant-Jacobian maps. As checked on 1 September 2026,
  MathNet listed five citing papers. Citation count is reception evidence, not
  mathematical validation.
- The locally pinned Żołądek article,
  `refs/zoladek2008_official.pdf`, has SHA-256
  `88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad`.
  On printed p. 432 it says Orevkov and Domrina proved the conjecture for
  geometrical degree at most four and cites Domrina II as reference [7]. On
  p. 433 it describes its own method as a direct proof of that theorem and an
  extension to five sheets. Theorem 6.12 on p. 461 states that every Jacobian
  map of topological degree at most five is invertible and is followed by a
  proof; [7] on p. 469 is precisely Domrina II. This is independent of
  Domrina II's splice-diagram elimination, though it still uses Orevkov
  material. See
  [Żołądek 2008](https://doi.org/10.1016/j.top.2008.04.001).
- Sigray's 2008 ELTE thesis, locally
  `refs/sigray_full.pdf` with SHA-256
  `9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae`,
  says the Domrina--Orevkov degree-four case was known, then advertises a new
  proof of the known cases and degree five. Its Theorem 9.1 states that a
  counterexample has topological degree at least six. However, the campaign's
  prior audit at `ladder/SHEET6.md:31-36,85-95` and
  `ladder/REDUCTION.md:986` finds missing row coverage and a missing terminal
  elimination in the printed proof. It is reception evidence and a source of
  a distinct decorated-Eggers--Wall-tree route, not a second complete
  independent proof.
- Borisov's 2020 research/framework article says the current best lower bound
  for the topological degree of a Keller counterexample is six, citing Żołądek; see
  [Question 6](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v27i3p54/pdf/).
  It thereby consumes the low-sheet result as established, although it does
  not directly cite Domrina II for that sentence.
- Makar-Limanov's refereed 2021 article states that the function-field degree
  is known to be at least six and cites Domrina's announcement, Domrina II,
  D--O I, Orevkov, Sigray, and Żołądek. This is direct later treatment of the
  Domrina publications as part of the proved low-sheet record; see its
  [official publication record](https://doi.org/10.1070/IM9067).

There is a documented gap in a different part of Żołądek's paper. Guccione,
Guccione and Valqui identify an unsupported inclusion in Żołądek Lemma 4.10,
used by Theorem 4.12 and the neighboring gcd-of-total-degrees claims; see their
[introduction](https://arxiv.org/html/1401.1784v3). They do not identify
Theorem 6.12 or its low-topological-degree proof as depending on that lemma.
No dependency on that lemma was identified for Theorem 6.12 in this audit;
absence of such an identified path is not itself proof of nondependency. It
would be a fallacy to transfer the adjacent gap to Theorem 6.12 without a
dependency path.

The calibrated verdict is therefore:

- `RECEPTION`: Domrina's \(N=4\) theorem is treated as proved, not conjectural
  or merely announced.
- `REDUNDANCY`: Żołądek supplies the refereed independent \(N\le5\) proof.
  Sigray's distinct treatment is incomplete as printed and supplies no second
  independent redundancy.
- `DOMRINA-II-SOUNDNESS`: still `OPEN` under this campaign's hostile-review
  standard because the compressed splice calculations have not been replayed.
- `LITERATURE-N4`: `CLOSED`, absent a future specific defect in all applicable
  independent proofs.

## 6. Campaign impact by soundness scenario

### Scenario (a): Domrina's full chain is sound

`IMPACT=LITERATURE-CLOSURE/PRIORITY-PIVOT.` The Keller exclusion at \(N=4\)
is closed in the literature. The campaign's B0/profile results become an
independent derivation and sharpening of the entry structure; EXHAUST plus
ROW-KILL becomes independent verification on the rows it actually covers.
Because the charged campaign still has the pin, shape, and six-type residuals,
it is not yet accurate to call its *whole* \(N=4\) chain an independent full
proof.

The six-type suite is no longer needed to decide whether an \(N=4\) Keller map
exists. Its continuing research value is counterexample-side geometry: which
one-place curves exist, which complement groups/meridional representations
they admit, and how sharp the necessary conditions are. It has no remaining
role in deciding the Keller exclusion once the published result is accepted.

Campaign effort should pivot to reducible \(N\ge5\), the one-cusp horn, and
reducible/all-degree work outside the already closed H2/B0 lane. A novelty
caveat belongs on that pivot: Żołądek already closes topological degree 5, so
\(N=5\) is methodological cross-verification; degree 6 is the first degree not
excluded by the checked 2020--2021 lower-bound sources.

### Scenario (b): Domrina's chain contains a gap

`IMPACT=LOCATION-DEPENDENT; NO-FIRST-PROOF-PRIORITY-YET.` There are three
different cases:

1. **Only the imported D--O I μ=1 inference fails.** Campaign B0 Proposition
   4.1 repairs it; Corollary 3.8 repairs the separate \(\mu=N-1\) remark; and
   Theorem 4.3 recovers the two-component profile once its mixed-lane
   hypotheses hold. With
   those substitutions, this particular defect does not threaten the
   mathematical conclusion. Żołądek 6.12 independently preserves the
   published-literature closure posture for \(N=4\).
2. **A Domrina II splice step fails.** If the defect is in target-diagram
   exhaustiveness, edge-block determinants, weakened-coprimality enumeration,
   global gluing, root location, or a terminal canonical equation, no promoted
   campaign theorem repairs that proposition as stated. The campaign only
   bypasses it on the EXHAUST/ROW-KILL strata. The campaign pin, shape tails,
   and six AM candidates remain to be closed before a full alternative proof
   exists. Again Żołądek 6.12 preserves the published-literature closure
   posture unless a concrete dependency defect is also found there.
3. **All independent low-sheet proofs also fail.** Only after a specific audit
   invalidates the applicable parts of Żołądek, *and* the campaign closes its
   own named residuals, could “first rigorous full treatment” be considered.
   None of those conditions is
   established here.

Thus the campaign may claim `EXPLICIT-CAMPAIGN-REPAIR` for the precise D--O I
μ=1 author inference and `INDEPENDENT-RIGOROUS-TREATMENT` for its promoted
rows. It may not currently claim `FIRST-RIGOROUS-N4-THEOREM`.

## 7. Process reconstruction: why three sweeps missed the theorem statement

The premise needs correction: the repository did **not** first discover
Domrina II as a cross-check in three literature sweeps. The theorem statement
was already explicit on 24 August in `AUDIT.md:11576-11586`,
`xmodel/ideation-20260824T0719Z-adversary.md:33-47`, and the corresponding
synthesis at lines 38--46. Those files also named Żołądek Theorem 6.12 and
correctly set the first open sheet degree to six.

What happened later was semantic loss through three downstream hand-offs:

1. `xmodel/ideation-20260831T1033Z-grok46.md:129-135,245-249` used Domrina
   only for the count of dicritical compactification components. Its prompt
   charged roughly the first 250 lines of `AUDIT.md`; the low-sheet checksum at
   line 11576 was outside the charged slice.
2. The narrowly scoped μ=1 literature registry was charged from that synthesis.
   It analyzed the D--O I inference but put Domrina II only in acquisition item
   8 (`xmodel/trivial-dicritical-literature-registry-grok46-20260831.md:154-167`).
   The locally available Żołądek paper was mined for nearby dicritical
   propositions, not its introduction, Theorem 6.12, and bibliography.
3. The B0 proof inherited that registry and deliberately labelled Domrina II a
   future “cross-check ... not a consumption”
   (`xmodel/b0-trivial-dicritical-proof-opus5-20260831.md:575-578`). The
   label then propagated into coordinator integrations.

These are not literally three literature sweeps. `LIT-TARGETED` had unrelated
questions (binary cubics, fold complements, SIROCCO), and `WEB-SWEEP` was a
current-frontier scan, not an old low-sheet census. Counting them as failures
would obscure the actual process fault: a known theorem-level checksum did not
survive scope narrowing, and an acquisition entry did not require first-page
claim extraction.

The search pattern that catches both the announcement and full proof is:

```text
repository: rg -ni 'Domrina|im273|four[- ]sheet|topological degree.*(4|5)'
web:        "four-sheeted polynomial mappings" Domrina
            "topological degree 4" Jacobian Domrina
            site:mathnet.ru Domrina four-sheeted
PDF:        pdftotext FILE - | rg -ni 'Domrina|geometrical degree|Theorem 6.12'
```

Then expand the exact-title family with and without “II,” inspect the author's
MathNet bibliography, follow backward and forward citations, and read at least
the abstract, theorem page, and bibliography of every acquired item before
typing it as a cross-check. Every live packet should carry a short global
checksum such as `td<=5 known-closed; first open td=6`, together with separate
fields for `RESULT-DISCOVERED`, `PROOF-BYTES-HELD`, and
`PROOF-HOSTILELY-AUDITED`. That prevents a narrow lemma registry from
silently reopening a theorem the campaign already knew.

## 8. Typed conclusions and open acquisition obligations

| item | final type |
|---|---|
| 1999 announcement theorem statement | `EXACT/UNCONDITIONAL` |
| proof supplied in the four pages | `OUTLINE/NOT-STANDALONE` |
| Proposition 1 versus campaign residual | `CONDITIONAL-CORE-MATCH` after entry to the mixed \(\mu=1\) residual, with source/target/place distinctions retained |
| announcement Propositions 2--5 and final check versus ROW-KILL/EXHAUST | `DIFFERENT-METHOD/NO-STEPWISE-EQUIVALENCE` |
| D--O I unique-dicritical μ=1 inference | `SOURCE-GAP; CAMPAIGN-REPAIRED` |
| official Domrina II acquisition | `CLOSED`: clean 33-page copy, SHA-256 `0be24c5c6a9cc9423c3049c3402f2c98e44bac5f1c6018b3999989e0f32e5018` |
| Domrina II mathematical replay | `OPEN`: compressed analogies and terminal finite checks remain |
| literature's treatment of \(N=4\) | `PROVED/ACCEPTED`, with independent Żołądek redundancy |
| checked 2020--2021 lower-bound posture | degree 6 is the first not excluded by those sources |
| campaign's complete independent \(N=4\) proof | `OPEN`: pin + shape tails + six AM candidates |
| “campaign is first rigorous \(N=4\) treatment” | `NOT-LICENSED` |

No further acquisition is required to begin the Domrina II replay; the two
corrupt shadows are superseded by the verified official file. The next
desk-scale audit should freeze that hash and replay, in order: Lemma 3.12's
local census, Lemma 3.14's global census, every implicit root-location branch,
the omitted §7 calculations, and Lemma 7.10's undisplayed case check. It
should bind D--O I either to a separately repaired proof or explicitly to the
campaign's Proposition 4.1, rather than inherit the author inference.

For campaign planning, accept \(N=4\) as prior art, retain the six-type work as
curve-existence/complement geometry, and redirect theorem-closing resources to
the reducible higher-sheet, horn, and reducible/all-degree fronts outside the
closed H2/B0 lane.
