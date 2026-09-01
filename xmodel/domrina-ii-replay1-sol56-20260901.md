# DOMRINA-II-REPLAY-1: hostile replay of Domrina II, §§1–4

**Lane:** first-half soundness audit (local census, global census, implicit
root locations, and the Domrina–Orevkov I dependency).  **Scope stop:** the
end of §4; §§5–7 are forward dependencies only.

## 0. Custody, controls, and verdict vocabulary

The custody gate was run before either charged input was read.  The recomputed
digests are

```text
0be24c5c6a9cc9423c3049c3402f2c98e44bac5f1c6018b3999989e0f32e5018  refs/domrina2000_izv64_four_sheeted_general_case.pdf
5739b317366d0a3c8905fcdc642f823c7bb71d44b79c7101b2cac256512f4d01  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.ALmxog/inputs/domrina-1999-audit-sol56-20260901.md
```

Both equal the charged values.  The first page identifies the first file as
A. V. Domrina, “On four-sheeted polynomial mappings of \(\mathbb C^2\). II.
The general case,” *Izvestiya: Mathematics* **64**:1 (2000), 1–33, DOI
10.1070/IM2000v064n01ABEH000273, and states the advertised theorem (printed
p. 1).  The PDF has 33 pages and its PDF-page numbers agree with the printed
English page numbers.  All page citations below are to those printed numbers.

Lemma 3.12 expressly sends the omitted details to part I, “[4], Lemma 8”
(p. 11).  For the limited purpose of reconstructing that analogy I also used
the repository copy `refs/do.pdf`; its recomputed SHA-256 is
`6ca30d797810400ddfcddb5b92b046796b3fdda5c1fb8f0ba378511506bbfed3`.
That auxiliary copy is not used to cure the charged one-dicritical inference.
The latter is governed only by the binding rule in §5 below.

This is a hostile replay, not a reception survey.  The three verdicts have the
following fixed meanings.

- **REPLAYED-SOUND**: the stated hypotheses imply the printed conclusion by
  a calculation reproduced here; no acceptance presumption is used.
- **REPAIRED**: the printed line is insufficient, but a standalone argument
  supplied here (or the expressly licensed campaign Proposition 4.1 binding)
  supplies exactly the missing implication.  The replacement and its scope
  are named.
- **GAP**: after separating the source vertices, their images, and the
  covering degrees, a necessary implication is neither displayed nor
  derivable from the stated hypotheses and cited results available to this
  replay.  A `GAP-CANDIDATE[...]` name below identifies the exact obligation.

An implication is not promoted merely because the same picture appeared in
part I: part II weakens full branch-determinant coprimality to the one-exception
rule of Assertion 3.11(b).  Likewise, an image branch, a source branch, and a
covering sheet are kept distinct throughout.  No exit price is asserted in
this report, so the FALLACY-v2 `charge_basis` declaration is inapplicable.

The scope boundary is strict.  Section 4 is checked because it consumes the
censuses and makes an implicit root placement.  Sections 5–7, including
Lemma 7.10 and the omitted §7 arithmetic, are recorded only as downstream
consumers for the sibling lane.  The frozen seal basis for this run is
`7a35f2d99c72179080a504484cfc1cf790abb642`.  The completion marker and
canonical seal were withheld throughout drafting and are installed only after
all bounded section writes and checks described below.

## 1. Reconstructed data model and replay invariants

Write (D=\operatorname {Deg}(\widetilde a)=m(\widetilde
a)n(\widetilde a)) for a fork.  Equation (3.1) says that the degrees of
all nonconstant source vertices above a fixed target vertex sum to four
(p. 7).  Hence (D\leq4), while the definition of a fork gives (m>1).
The only possibilities are

\[
(D;m,n)=(2;2,1),(3;3,1),(4;4,1),(4;2,2).                 \tag{R1}
\]

For each of the target directions (X=L,R,D), let
(d_{X,1},\ldots,d_{X,r_X}) be the degrees of the edge-type source
branches at (\widetilde a).  Definition 3.2(c), the local degree sum
([4], formula (4), invoked on p. 11), and the definition of (n) give

\[
d_{X,j}=n e_{X,j},\qquad e_{X,j}\geq1,\qquad
\sum_j e_{X,j}=m.                                        \tag{R2}
\]

There are only these three effective directions.  At (h^0), the omitted
components of (U^0) have local index one by Assertion 3.9(a), so they add
zero to Riemann–Hurwitz.  Formula (5) of [4], also invoked on p. 11, then
becomes

\[
\sum_{X,j}(e_{X,j}-1)=2(m-1),\qquad
r_L+r_R+r_D=m+2.                                         \tag{R3}
\]

This calculation is a **REPLAYED-SOUND** first-stage census.  It is also a
useful guard against reading an edge label as a vertex degree: the label is
(d_{X,j}), whereas (D) is the degree of the central source vertex.

The raw signatures forced by (R1)–(R3) are as follows.  A string such as
`31|211|4` records the unordered degree partitions in the order
(L|R|D).

| central type | branch-count types | number before determinant/routing tests |
|---|---:|---:|
| ((2,1)) | permutations of `2|2|11` | 3 |
| ((3,1)) | permutations of `3|3|111`, and of `3|21|21` | 6 |
| ((4,1)) | counts (4,1,1); (3,2,1); or (2,2,2) | (3+12+8=23) |
| ((2,2)) | twice the ((2,1)) partitions | 3 |

Thus Riemann–Hurwitz gives **35**, not 20, raw signatures.  Reading Fig. 8
at its printed edge labels gives this exact 20-row intermediate list
(pp. 11–12):

| Fig. 8 | ((m,n)) | (L|R|D) | Fig. 8 | ((m,n)) | (L|R|D) |
|---|---:|---|---|---:|---|
| a | (2,1) | `2|2|11` | b | (2,1) | `2|11|2` |
| c | (2,1) | `11|2|2` | d | (3,1) | `111|3|3` |
| e | (3,1) | `3|3|111` | f | (3,1) | `21|21|3` |
| g | (3,1) | `3|21|21` | h | (4,1) | `4|4|1111` |
| i | (4,1) | `1111|4|4` | j | (4,1) | `4|211|31` |
| k | (4,1) | `211|4|31` | l | (4,1) | `31|4|211` |
| m | (4,1) | `31|211|4` | n | (4,1) | `31|31|22` |
| o | (4,1) | `22|31|31` | p | (4,1) | `31|22|22` |
| q | (4,1) | `22|22|31` | r | (2,2) | `4|4|22` |
| s | (2,2) | `4|22|4` | t | (2,2) | `22|4|4` |

The determinant conversion used in the second-stage filter is not equality
of labels.  If an edge-type branch (Q) is incident only to
(\widetilde a), Definition 3.2(b) gives

\[
 \det Q={n(\widetilde a)\over\operatorname {Deg}Q}
          \det F(Q),                                    \tag{R4}
\]

and an additional endpoint ramification factor occurs when (Q) is incident
to a second nonconstant vertex.  This is why a fractional value such as
(1/2) is a contradiction only after the endpoint class and the target
determinant have been fixed.  It is also why the analogy with part I cannot
simply identify edges having the same numeral.

Assertion 3.11 supplies the other filter (p. 11): (\det R_a=1), while
(\det L_a,\det D_a>1); the image of a left branch is coprime to
(\det D_a); and all lower branches together with those left branches that
are actual branches of (\widetilde L_\infty) are pairwise coprime, with at
most one exceptional pair and with one member of that pair incident to
(\widetilde g_1).  In particular:

- a controlled `11` pair has two equal determinants (>1), so it must be
  the unique exceptional pair and one member must reach (\widetilde g_1);
- controlled `111` or `1111` creates more than one bad pair and cannot be
  rescued by the exception;
- a `211` direction has exactly one repeated degree-one pair; and
- none of these observations controls a left endpoint that is another fork,
  or a right endpoint, until (3.1), (3.2), and the tree routing are applied.

These implications will be used only in those endpoint classes for which the
paper or the replay has actually established them.  They do not by themselves
prove the 35-to-20 reduction.

## 2. Lemma 3.12: local fork census

### 2.1 The missing 35-to-20 filter

The proof begins, “We omit the details since they are analogous to [4],
Lemma 8” (p. 11).  That analogy is not itself a replay because part I had a
stronger coprimality situation.  The needed standalone replacement is the
following denominator-cancellation argument.

Let a left edge-type block of degree (e) have image determinant (P), and
let (n_b=1) if it has no second nonconstant endpoint.  Definition 3.2(b)
gives

\[
 e\mid n(\widetilde a)n_bP.                              \tag{L1}
\]

All 15 signatures absent from Fig. 8 have (n(\widetilde a)=1).  If
(e=3), cancellation of the factor 3 would require (3\mid n_b); a second
endpoint is a fork, so its degree would be at least (2\cdot3=6), contrary
to (3.1).  Thus a degree-3 left block forces (3\mid P).  An unsplit
degree-4 block forces (2\mid P), because an endpoint fork of degree at most
four has (n_b\le2), cancelling at most one factor 2.  Finally, a degree-2
block in a split direction forces (2\mid P): otherwise (n_b=2), so that
fork already has degree four, while the parallel positive-degree branch
supplies another sheet at the same downstream target vertex by (3.2),
contradicting (3.1).

For a lower block (P=\det D_a).  Assertion 3.11(a) says that a left-image
determinant (P_L) is coprime to (\det D_a).  Consequently the partition
types impose these tests:

| partition in a controlled (L) or (D) direction | forced condition |
|---|---|
| `4` | the relevant target determinant is even |
| `31` | it is divisible by 3 |
| `22` | it is even |
| `211` | it is even; its two degree-one blocks also use the sole possible exceptional pair |
| `1111` | impossible if all are controlled branches: four equal determinants (>1) give more than one bad pair |

The two absent ((3,1)) rows are now forced out.  In `3|111|3`, both the
left and lower unsplit degree-3 blocks force a factor 3.  In `21|3|21`, the
degree-2 blocks in both controlled directions force a factor 2.  Each
contradicts Assertion 3.11(a); the cancellation alternatives were excluded
above.

Here is the complete check of the 13 absent ((4,1)) rows.  The last column
shows the common prime forced into the left-image determinant and
(\det D_a).

| absent (L|R|D) | prime | absent (L|R|D) | prime |
|---|---:|---|---:|
| `4|31|211` | 2 | `4|22|211` | 2 |
| `4|211|22` | 2 | `4|1111|4` | 2 |
| `31|31|31` | 3 | `31|22|31` | 3 |
| `22|4|211` | 2 | `22|31|22` | 2 |
| `22|22|22` | 2 | `22|211|4` | 2 |
| `211|4|22` | 2 | `211|31|4` | 2 |
| `211|22|4` | 2 |  |  |

The (\widetilde g_1) exception does not save a `211` row: its repeated
degree-one pair consumes that exception, while its parallel degree-2 block
still forces evenness.  Thus `211` can face only `31` across the two
controlled directions (the printed k and l); `4` can face `31` (j and m);
and `31` can face `22` (n, o, p, q).  Together with the rows a–c, d–g,
h–i, and r–t already listed in §1, this proves that the 20 printed
intermediate rows are exhaustive.  **Verdict: REPAIRED**—the omitted
enumeration is supplied, and no raw signature remains.

### 2.2 Four printed candidates eliminated

The eliminations on p. 12 check as follows.

- **e = `3|3|111`: REPLAYED-SOUND.**  Its three lower degree-one blocks
  each have determinant (\det D_a>1) by Definition 3.2(b), producing
  three bad pairs where Assertion 3.11(b) permits one.
- **h = `4|4|1111`: REPLAYED-SOUND.**  The four equal lower determinants
  produce six bad pairs.
- **i = `1111|4|4`: REPLAYED-SOUND.**  Since
  (\operatorname {Deg}\widetilde a=4), (3.2) makes all four degree-one
  left blocks full branches of (\widetilde L_\infty).  Their determinants
  all equal (\det L_a>1), again producing six bad pairs.
- **d = `111|3|3`: REPAIRED.**  If all three left degree-one blocks were
  full, their equal determinants would leave at least one forbidden pair
  even after the (\widetilde g_1) exception.  Hence one meets a source
  fork (\widetilde c).  At its target image the other two branches each
  contribute one sheet, so (3.1)–(3.2) give
  (\operatorname {Deg}\widetilde c\le4-1-1=2).  It is a fork, hence has
  degree two.  The edge back to (\widetilde a) has degree one, forcing
  local type b at (\widetilde c).  The next left fork has degree four by
  part (2) below, while the two original parallel branches still contribute
  two sheets.  This violates (3.1).  This is the explicit degree/tree chase
  compressed on p. 12.

Removing d, e, h, i from the 20-row intermediate list leaves exactly
`a,b,c,f,g,j,k,l,m,n,o,p,q,r,s,t`, the list in Lemma 3.12(1).

### 2.3 The six numbered assertions

**(1) Local list — REPAIRED.**  Sections 2.1–2.2 supply the missing complete
enumeration and give exactly the printed list (pp. 11–12).

**(2) The endpoint of b and s — REPAIRED.**  For b, its lower degree-2
block makes (\det D_a) even.  If its left degree-2 block had no second
fork endpoint, its image determinant would also be even, contradicting
Assertion 3.11(a).  Thus it reaches a fork (\widetilde b), and (L1)
forces (n(\widetilde b)) even.  Since (m(\widetilde b)\ge2) and
(m(\widetilde b)n(\widetilde b)\le4), one has
(m(\widetilde b)=n(\widetilde b)=2).  For s the ratios are

\[
 \det\widetilde Q_D={2\over4}\det D_a,qquad
 \det\widetilde Q_L={2n(\widetilde b)\over4}P_L;
\]

the same coprimality argument makes (n(\widetilde b)) even and gives the
same conclusion.  This reconstructs the claim on pp. 11 and 13.

**(3) The (\widetilde g_1) branches in a, l, r — REPLAYED-SOUND.**  In a
and r the two lower blocks have the same determinant (\det D_a>1); in l
the two lower degree-one blocks do.  They must be the sole exceptional pair,
so one member reaches (\widetilde g_1).  Its image runs down to the unique
target attachment (h).  Since (\widetilde a\notin U^0), this forces
(a=h), not an identification of the source flag with the target place.  In
l the selected edge itself has degree one, hence
(\operatorname {Deg}(\widetilde a\widetilde g_1)=1) (p. 11).

**(4) Type c — REPLAYED-SOUND.**  Its two left degree-one blocks have equal
determinant (\det L_a>1) if both are full.  If (a) is not right of (h),
neither can reach (\widetilde g_1) through a left route.  Assertion 3.11(b)
therefore forces one to meet another source fork.  This is exactly the
printed disjunction.

**(5) Type k — REPLAYED-SOUND.**  Degree four and (3.2) make its two
degree-one left blocks full branches.  Their equal determinant uses the
single exception, so one reaches (\widetilde g_1) (pp. 11–12).

**(6) Types b, s, t lie right of (h) — REPAIRED.**  The p. 13 phrase “As
in 4)” suppresses a finite descent.  If a t-vertex (a\le h), one of its
two left degree-2 blocks reaches a fork (\widetilde b); the parallel block
already contributes two sheets, so (3.1)–(3.2) force
(\operatorname {Deg}\widetilde b=2).  Its return edge has degree two, so
its type is a or c.  Type a would put (b=h<a), impossible.  Type c and
part (4) force a still farther-left fork; at that next image the unused
c-branch contributes one sheet and the unused t-branch contributes two,
leaving degree at most one for a fork.  Thus t is right of (h).

For s, part (2) makes its left endpoint a ((2,2))-fork.  Its return edge is
a right degree-4 edge, so that endpoint is r or t.  Type r is at (h) by
part (3), and type t is right of (h); either contradicts an endpoint
strictly left of (a\le h).  For b, part (2) again gives a left
((2,2))-fork, but the return edge is one of two right degree-2 edges, so
its type is s, just proved right of (h).  This completes the descent.

**Local-census disposition:**
`LEMMA-3.12=REPAIRED; RAW-35=EXHAUSTED; OMITTED-15=EXCLUDED;
UNRESOLVED-LOCAL-SIGNATURES=NONE`.

## 3. Lemmas 3.13–3.14: global census

### 3.1 Lemma 3.13: the four additional local exclusions

The p/q calculation on p. 13 is not justified merely by saying that a branch
lies “entirely to the right.”  In either type the right labels exhaust the
four sheets in (3.1).  Equality in (3.2) therefore rules out both a return
across the target vertex and an extra positive-degree fork.  The right block
not containing \(\widetilde g_2\) is either already a full edge-type block or
passes once through a suppressed type-a block.  In the first case Definition
3.2(b) gives

\[
 \det\widetilde R={1\over2}\det R_a={1\over2};
\]

in the second, the identical ratio applies to the terminal right block.
Both contradict integrality.  Thus p and q are excluded.  **Verdict:
REPAIRED.**

For c, suppose a left arm first meets a fork \(\widetilde b\).  The unused
degree-one arm and (3.1)–(3.2) give
\(\operatorname {Deg}\widetilde b\le3\).  Degree two forces b, producing
two routes between the same source vertices.  Degree three forces f or g,
the two diagrams in Fig. 9 (p. 13).  At each visible fork the labelled
degrees, together with the complementary sheet, total four.  Hence the two
indicated right branches stay on their respective sides.  One does not
contain \(\widetilde g_2\), and its terminal determinant is again
\(\det R/2=1/2\).  Therefore neither c-left arm meets another fork: both
are full branches of \(\widetilde L_\infty\), and their equal determinants
\(\det L_a>1\) force one to be the exceptional
\(\widetilde g_1\)-branch.  **Verdict: REPAIRED.**

It remains to check s rather than accept “the other cases are treated in
the same way” (p. 14).  Its degree-four left block ends at a
\((m,n)=(2,2)\) fork.  Lemma 3.12 gives exactly the four continuations in
Fig. 10:

| Fig. 10 | first \((2,2)\) fork | possible next degree-two fork |
|---|---|---|
| a | r | none |
| b | t, with both left arms terminal | none |
| c | t | a |
| d | t | c |

There is no fifth row: at t a nonterminal degree-two left arm has endpoint
degree at most two by (3.1)–(3.2), and the return label then permits only a
or c.  Write \(S=\det\widetilde L_{\widetilde a}\).  Applying [4], formula
(6), i.e. the determinant-ratio formula, gives these four separate checks.

- In 10a (type r), if \(d_3\) is either equal lower determinant at the
  \((2,2)\) fork, then
  \(\det L_a=2S/d_3\), exactly as printed.  Here
  \(\det L_b=2d_1\), and Corollary 1.4 gives
  \(\gcd(\det L_b,d_3)=1\), so \(d_3\) is odd.
- In 10b (type t), put \(\ell=\det L_b\), \(d=\det D_b\).
  The source-minus and target-minus products in formula (6) are
  \(\ell^2(d/2)\) and \(\ell d\), respectively, whence
  \(\det L_a=2S/\ell\).  Integrality of the degree-four lower block makes
  \(d\) even; \(\gcd(\ell,d)=1\) makes \(\ell\) odd.
- In 10c the extra degree-two fork is a.  At that fork the products are
  \((L/2)D^2\) and \(LD\), with ratio factor \(n/m=1/2\).
  Thus its inserted source determinant is \(\ell D\) and
  \(\det L_a=2S/(\ell D)\).  The degree-two left block makes \(L\) even,
  so coprimality makes \(D\) odd.
- In 10d the extra fork is c.  Its products are \(L^2(D/2)\) and \(LD\);
  the inserted determinant is \(\ell L\), and
  \(\det L_a=2S/(\ell L)\).  Here \(D\) is even and \(L\) odd.

In 10c–d the first fork is the same type-t fork as in 10b: its lower
degree-four block makes \(\det D_b\) even, so
\(\ell=\det L_b\) is odd by coprimality.
Each displayed denominator is odd and divides the numerator.  Consequently
\(\det L_a\) is even in all four rows.

The next two sentences of the English text contain two independent slips.
It calls \(d_7\) the determinant of the “left branch” of \(U_{\widetilde
a}\), although the relation \(\det D_a=2d_7\) uses the **lower** degree-four
branch.  It then says “the fact that \(\det L_a\) is odd,” immediately after
proving it even.  With those corrections, both \(\det L_a\) and
\(\det D_a\) are even, contradicting their coprimality in Proposition
1.3(2), equivalently Assertion 3.11(a).  Thus s is impossible.  Type b
has a left \((2,2)\) endpoint whose return edge forces type s, so b is
impossible as well.  **Lemma 3.13 verdict: REPAIRED.**

### 3.2 State space for Lemma 3.14

The paper replaces every a- or c-block by a degree-two edge before stating
Lemma 3.14 (p. 14).  This is a quotient convention: such blocks are not
additional visible forks in Fig. 11.  Subdivision by one of them therefore
does not create a new global case.  It is important not to turn the
\(\widetilde g_1\)-branch in such a suppressed block into an additional
covering sheet.

Nor may uniqueness of the physical \(g_1\)-place alone be used to forbid
reuse.  The needed distinct-block check is as follows.  Every a maps to h
and its marked lower port is degree one; two a's cannot be serial, while
parallel a-ports reconverge on the same C-state carrier and their two
\(g_1\)-routes make a cycle.  After Lemma 3.13, c has two full left ports,
one meeting \(\widetilde g_1\).  A second serial c would require the
eliminated b splitter, and two parallel full c-ports cannot merge at
\(\widetilde g_1\) without a cycle.  Finally an a-lower block and a c-left
block have different target directions and cannot be one edge-type block.
Thus no repeated a/c word survives; this is the standalone repair that
makes the quotient convention exhaustive.

Across a target interval, record the partition of all four sheets:

\[
 A=(4),\qquad B=(3,1),\qquad C=(2,2),\qquad D=(2,1,1).                 \tag{G2}
\]

For a degree-three source fork the missing degree-one source point is
included in this four-sheet state.  After Lemma 3.13, every visible fork
has exactly the following transition:

| type | left state | right state | lower state |
|---|---|---|---|
| f | D | D | B |
| g | B | D | D |
| j | A | D | B |
| k | D | A | B |
| l | B | A | D |
| m | B | D | A |
| n | B | B | C |
| o | C | B | B |
| r | A | A | C |
| t | C | A | A |

This table is a direct rewrite of Fig. 8, not a new assumption.  For
example f has local \(21\) on each horizontal side and a complementary
degree-one sheet, hence state D; g has local degree 3 on the left plus that
sheet, hence B.

There must be a visible fork.  Indeed, delete the leaf
\(\widetilde g_1\) at its unique intersection (Proposition 1.3(1));
\(\widetilde L_\infty+\widetilde g_2\) remains connected.  The degree-two
carrier through \(\widetilde g_2\) leaves a complementary degree-two lift
by (3.1).  A lone suppressed a/c block preserves that split after its
\(g_1\)-port is deleted.  The first vertex joining the two carriers has
total degree three or four and is one of the visible f–t types.  Hence the
zero-visible-fork alternative is impossible.

Lemma 1.5 says that the chain incident to \(\widetilde g_2\) has degree
two (p. 3).  Its last visible fork must consequently have right state D,
and the local degree-two arm must be the one reaching
\(\widetilde g_2\).  The only candidates are

\[
                 \mathrm{j,\ m,\ g,\ f}.                              \tag{G3}
\]

This also reconstructs the branch-location step hidden in the one-line
proof of Lemma 3.14.

### 3.3 Complete predecessor and cycle check

Matching the right state of a left fork to the left state of its successor
gives the following complete first-predecessor table.

| last fork | possible immediate visible predecessor | result |
|---|---|---|
| j | none, r, t, l, k | Fig. 11: 1a, 1b, 1c, 2a, 2b |
| m | none | Fig. 11: 1d |
| g | o or n | Fig. 11: 3a, 3b |
| f | g or f | Fig. 11: 4a, 4b |

Here is the exclusion check behind the table.  A degree-four B-to-B
matching joins both its degree-three and degree-one arms to the same two
fork regions and creates two source paths; hence n or o may precede the
degree-three g, but cannot precede the degree-four m.  The same argument
excludes a degree-four D-state fork j or m immediately before f.  A
degree-three-to-degree-three D matching is possible only in the crossed
form: the degree-two arms join the visible forks, while each local
degree-one arm joins the complementary sheet on the other side.  This gives
exactly g–f and f–f.

The same check prevents a hidden third visible fork.  For n–g and o–g, a
further B-state degree-four predecessor would give two paths; o has no
visible C-state predecessor.  For g–f, a preceding n or o closes the
cycle through the complementary degree-one sheet.  For f–f, a third
degree-three fork gives, with visible forks \(F_1,F_2,F_3\) and the middle
complement \(C_2\), the explicit cycle

\[
                 F_1-F_2-F_3-C_2-F_1.
\]

For a predecessor of j, t has left state C and no visible predecessor; l
has left state B, where n/o would make the degree-four B-to-B cycle; and k
has left state D, where either a degree-four or degree-three predecessor
supplies two routes through its degree-two and degree-one lifts.  Finally,
r lies over h by Lemma 3.12(3).  A further r or l predecessor would also
lie over h and cannot be strictly left of it.  Type t is right of h by
Lemma 3.12(6); type k has its \(g_1\)-port in a left branch and is
therefore right of h.  Neither can precede r.  Thus none of the five j
rows extends.

Conversely every row in the table satisfies the state match and contains
no repeated source path.  Reading off the local types gives, without
identifying flags with target places,

| Fig. 11 | visible type word | joining degree |
|---|---|---:|
| 1a | j | — |
| 1b | r–j | 4 |
| 1c | t–j | 4 |
| 1d | m | — |
| 2a | l–j | 4 |
| 2b | k–j | 4 |
| 3a | o–g | 3 |
| 3b | n–g | 3 |
| 4a | g–f | 2 |
| 4b | f–f | 2 |

These are precisely the ten drawings on p. 15.  The drawings do not encode
a complete placement of \(\widetilde g_1\): Lemma 3.12 fixes it for the
suppressed a/c blocks and for l, k, r, while the Fig. 11 quotient leaves it
undrawn in the other rows.  Lemma 3.14 is exhaustive as a census of the
quotient graph, not as an extra theorem of exact \(g_1\)-attainment.

**Global-census disposition:**
\(\mathrm{LEMMA\ 3.13=REPAIRED}\);
\(\mathrm{LEMMA\ 3.14=REPAIRED}\);
\(\mathrm{FIG.\ 11\ TEN\ ROWS=REPLAYED\!-\!SOUND}\);
\(\mathrm{UNRESOLVED\ GLOBAL\ CASES=NONE}\).

## 4. Root/branch-location ledger for §§1–4

The rooted-tree facts used here are [4], Lemma 3 (away from the root, all
non-root branches but at most one have determinant one; at the root every
branch does) and [4], Lemma 4 (a subgraph not containing the root has positive
determinant).  These are generic determinant facts, not the defective
one-dicritical inference discussed in §5.

### 4.1 Section 1 and the auxiliary root calculations

**R-1, target-root trichotomy (p. 3) — REPLAYED-SOUND.**  In Proposition
1.3 the component (l_0) containing the unique infinity point of (g_1) is
either nodal, the root, or non-root and non-nodal.  Resolving the (g_1)-germ
at these three locations gives respectively Fig. 1a, Fig. 1b′, and Fig. 1b.
The three cases are mutually exclusive and exhaustive.

**R-2, (\widetilde v\in\widetilde L_\infty) (p. 3) —
REPLAYED-SOUND.**  The root is the strict transform of the original source
line at infinity.  At its generic point the homogenized target coordinate is
zero; resolving indeterminacies does not change that generic image.  It
therefore lies in (F^{-1}(L)=\widetilde L_\infty).

**R-2a, terminal linear chains (Lemma 1.5, p. 3) —
REPLAYED-SOUND.**  On a linear constant-degree chain ending at a dicritical,
[4], Proposition 1 identifies the chain degree with the transverse order at
that terminal flag. Proposition 1.2 gives
\(n(\widetilde g_1)=1\) and \(n(\widetilde g_2)=2\); these, rather than the
physical target places, are the two asserted chain degrees.

**R-3, Lemmas 2.3–2.4 (p. 4, (2.1)–(2.2)) — REPLAYED-SOUND.**  Substitution
in the displayed equations gives

\[
-1=p_1-dp_2,\quad
0=-2-p_1+(d-1)(p_2-1)+d\Sigma
\quad\Longrightarrow\quad p_2=d(\Sigma-1),
\]

contrary to the branch coprimality in [4], Lemma 2.  In Lemma 2.4 the
canonical formula gives (p_1=-2), and the edge formula gives
(p_2=1-2p_3<0).  The parenthetical “automatic if
((\widetilde v\widetilde q)) is linear” is sound because the open path then
has no nodal, hence no essential, vertex.

**R-4, Lemmas 2.5–2.6 (p. 4) — REPAIRED.**  The paper merely calls them
analogous.  For 2.5, under the contrary assumption,

\[
-2=p_1-dp_2,qquad
1=-2-p_1+(d-1)(p_2-1)+d\Sigma
\]

again gives (p_2=d(\Sigma-1)), impossible.  For 2.6, absence of essential
(\widetilde g_2)-contributions toward the root gives (p_1=-3); if
(p_3=\det\operatorname {br}_{\widetilde q}(\widetilde g_2)>0), the edge
formula is

\[
-2=p_1p_3-p_2,qquad p_2=2-3p_3<0.             \tag{R5}
\]

There is a printed subscript error: Lemma 2.6 says “essential for
(\widetilde g_1),” whereas the analogue and (R5) require “essential for
(\widetilde g_2).”  The repair is therefore
`REPAIRED[LEMMA-2.6-g1-TO-g2]`; the printed statement with its literal
(g_1) hypothesis is not what the proof establishes.

**R-5, Lemmas 2.7–2.9 (pp. 5–6, (2.3)–(2.10)) —
REPLAYED-SOUND.**  At each essential path vertex, its branch of determinant
(d_i>1) consumes the one possible non-unit non-root branch.  The branch on
the opposite side from (\widetilde v) therefore has determinant one.  This
justifies the undisplayed orientations in Figs. 3–4 and the assertions
(l_1=\cdots=l_n=1) used in (2.7).  Substitution of (2.3) in (2.4) gives
(p_2=d_1(\Sigma-1)).  Lemma 2.8 similarly gives
(\det\operatorname {br}_{\widetilde q_1}(\widetilde v)=-3B+1<-1) in the
inessential case and (-d(\widetilde q_1)-1<-1) in the essential case.
The algebra from (2.7) through (2.10) checks term by term.

**R-6, omitted Lemma 2.10 calculation (p. 6, (2.11)) — REPAIRED.**  Put
(D_j=\prod_{q\le j}d_q).  With the root between
(\widetilde k_n) and (\widetilde g_1), the opposite-side branch
determinants are one and the terminal canonical value is (-2).  The edge
formula gives

\[
x_i=-\frac12\left(d_i\prod_{q>i}d_q^2-\mu_i\right),\qquad
x_0=\frac12(\det\widetilde L_\infty-D_n^2).
\]

Inserting these in the canonical formula and using

\[
\sum_{j=1}^n(d_j-1)D_{j-1}d_j(D_n/D_j)^2=D_n^2-D_n
\]

gives

\[
0=-4-\det\widetilde L_\infty-D_n+
  \sum_{j=1}^n\mu_j(d_j-1)D_{j-1}.
\]

The tail with (\mu_j=1) telescopes to (D_n-D_p), which is exactly
(2.11) after changing sign.

**R-7, omitted Lemma 2.11 calculation (p. 7, (2.12)) — REPAIRED.**  This is
not a formal copy of 2.9 because the root changes side.  Put (m=n-1),
(D=D_m), (d=d_n), and (C=d^2+d+1).  The root condition and
(\det(\widetilde k_n\widetilde g_2)=1) give

\[
\det\operatorname {br}_{\widetilde k_n}(\widetilde v)=-(d+1),\qquad
\det\operatorname {br}_{\widetilde g_2}(\widetilde v)=-C,
\]

and hence, for (i\le m),

\[
x_i=-{1\over C}\left(d_i\prod_{q=i+1}^{n}d_q^2-\mu_i\right),\qquad
x_0={1\over C}(\det\widetilde L_\infty-(Dd)^2).
\]

The canonical formula at (\widetilde g_1) and the same telescoping identity
through (m) reduce to

\[
0=1+\det\widetilde L_\infty+(D+d)(d+1)
 -\sum_{j=1}^{m}\mu_j(d_j-1)D_{j-1}.
\]

The tail (\mu_j=d+1) is ((d+1)(D-D_p)), leaving precisely (2.12).
This repaired formula is first consumed in §7, outside this lane.

**R-8, Lemma 2.12 (p. 7, (2.13)) — REPLAYED-SOUND.**  If the root is in
neither (Q_1) nor (Q_2), all displayed subgraphs in the proof are
positive.  For (i=1), the first edge formula has negative right-hand side
and forces (\Delta_1<0).  The second rearranges as

\[
\det Q_1\Delta_1=-\det(\widetilde a\widetilde g_1)
 +\det Q_2\det Q_3(\det\delta(\widetilde a\widetilde g_1))^2\ge0
\]

by (2.13) and (\det Q_2\ge1), a contradiction.  The (i=2) branch is
symmetric.

### 4.2 Section 3 location claims

The directional claims in Lemma 3.12(2)–(6), including the finite strict-left
descent suppressed in part (6), are reconstructed in §2.3.  The p. 12 case-d
cycle is reconstructed in §2.2.  They are **REPLAYED-SOUND** or **REPAIRED**
as typed there.

The earlier incidence assertions are also closed.  In Lemma 3.7(a) (pp. 9–10)
the induction follows the unique source-tree path over the ordered target
vertices \(c_1,\ldots,h\); its displayed determinant calculation gives the
one incident nonconstant vertex.  Part (b)'s branch containing \(h^0\) is
that unique path, while the other branch is linear and positive by
Proposition 1.3 and [4], Lemma 5.  Assertion 3.9 then uses (3.1) and the
local degree formula [4], (4): the \(m(\widetilde h)\) incident
\(U^0\)-components each have determinant and local multiplicity one.
These incidence conclusions are **REPLAYED-SOUND**.  They still do not imply
Corollary 3.8(b)'s root exclusion, treated separately below.

The two implicit Lemma 3.13 branch routings are replayed in §3.1; both are
**REPAIRED** there by (3.1)–(3.2) saturation and the determinant-\(1/2\)
contradiction.

Two actual root-location gaps remain.

**GAP-CANDIDATE[ROOT-U-LAST-CHAIN] (Corollary 3.8(b), p. 10).**  The exact
quote is: “If \(\widetilde U\) is incident to \(\widetilde g_1\), then
\(\widetilde v\notin\delta(\widetilde g_1\widetilde h)\).”  It is followed
only by a citation to Lemmas 2.3, 2.4, and 3.7(b).  Lemmas 2.3–2.4 require
both

\[
\det(\widetilde q\widetilde g_1)=
\det\delta(\widetilde q\widetilde g_1)=1
\]

at a selected (\widetilde q).  Lemma 3.7(b) gives determinant one for a
whole lifted (U_c)-component, not these two path determinants.  More
decisively, it supplies positivity only for the exceptional branch not
containing (h^0).  If the root is in the final linear segment toward
(h^0), Lemma 2.4 merely declares that same segment negative; no displayed
fact contradicts it.  No last vertex or endpoint equation handles this
case.  **Verdict: GAP.**

**GAP-CANDIDATE[ROOT-DELTA-G2-APPLICATION] (Lemma 3.15, pp. 14–15).**  The
exact first conclusion is: “Then \(\widetilde v\notin
\delta(\widetilde a\widetilde g_2)\).”  The proof establishes positivity of
the whole delta graph, linearity of certain components, and
(\det(\widetilde s\widetilde g_2)=2), then invokes Lemmas 2.5–2.6.  It
never establishes their hypothesis
(\det\delta(\widetilde s\widetilde g_2)=1) for each possible selected
(\widetilde s), never checks the corrected (g_2)-essential-vertex
hypothesis of Lemma 2.6, and never converts (R5)'s negative branch
determinant into a contradiction with positivity of the whole delta graph.
Linearity alone does not make an open-chain determinant one.  **Verdict:
GAP.**  Its uses are forward dependencies in §§5–7.

The two root-sign steps in Lemma 3.16 (p. 15) are
**REPLAYED-SOUND**.  A lifted branch excluding the root is positive by [4],
Lemma 4.  At a nodal (\widetilde b\subset
\widetilde L_{\widetilde a}-U^0), the lifted left and lower branches both
exclude the root, so [4], Lemma 3 gives

\[
\min(\det\widetilde L_{\widetilde b},
     \det\widetilde D_{\widetilde b})=1.
\]

Formula (6) and [4], Lemma 5 transfer those determinants to (L_b,D_b);
Proposition 1.3 then leaves only (b=h) in target type 3, as printed.

### 4.3 Section 4: orientation typo and the omitted companion case

The p. 16 sentence assigning (\widetilde a) to the right vertex and
(\widetilde b) to the left is reversed.  Formula (4.1) assigns to
(\widetilde a) left degrees (1,3) and lower degrees (1,2), which is the
visually **left** l-block of Fig. 11(2a); it assigns to (\widetilde b)
lower degrees (1,3) and right degrees (1,2), the visually **right**
j-block.  The final inclusion
((\widetilde b\widetilde g_2)\subset
\operatorname {br}_{\widetilde a}(\widetilde b)) is well typed only with
that order.  Repair: read “left (respectively right).”  **Verdict:
REPAIRED[SECTION-4-a-b-REVERSAL].**

With that correction, (4.2) is reproducible.  At the left vertex select a
full degree-one left branch of determinant (\det L_a>1) and the full
degree-one lower branch not reaching (\widetilde g_1), of determinant
(\det D_a>1).  If the root lay toward (\widetilde b), these would be two
non-root non-unit branches, violating [4], Lemma 3.  Thus

\[
\widetilde v\notin\operatorname {br}_{\widetilde a}(\widetilde b),qquad
\det\operatorname {br}_{\widetilde a}(\widetilde b)=1.
\]

At (\widetilde b), (4.1) and the same root rule give
(d_b^3=1,d_b^1=3), and
(\det\operatorname {br}_{\widetilde b}(\widetilde g_2)=1).  Formula (6)
of [4] gives (\det(\widetilde a\widetilde g_2)=1), and the edge formula
inside the root-free branch becomes

\[
1=1-3\det(\widetilde a\widetilde b)
       (\det\delta(\widetilde b\widetilde g_2))^2,
\]

impossible because the two omitted determinants are positive.  **Case 2a:
REPAIRED.**

For the undisplayed 2b calculation, the left block is k rather than l; replace
the first line of (4.1) by

\[
l_a^1=2l_a^2=\det L_a,qquad
d_a^1=3d_a^3=\det D_a.
\]

Lemma 3.12(5) places (\widetilde g_1) on one degree-one left arm.  Select
the other such arm and the degree-one lower arm.  The right
(\widetilde b)-data are unchanged, so the preceding root exclusion,
(4.2), and the final impossible equation repeat verbatim.  **Case 2b:
REPAIRED.**

## 5. Domrina–Orevkov I dependency bindings

There are two direct textual uses of part I's one-dicritical exclusion in the
audited range.

| use | exact Domrina II text | role | binding and verdict |
|---|---|---|---|
| DO-I-1 | “This paper is a continuation of [4], where the case when (f) has one dicritical component was proved to be impossible. Here we consider the remaining cases” (Introduction, p. 1) | historical scope gate | For the unique-μ=1 slice, bind to the charged audit §3.1 statement of campaign Proposition 4.1: an all-μ=1 profile is impossible with the finite correction set retained. **REPAIRED** for that slice. |
| DO-I-2 | “The number of dicritical components of (F) is greater than 1 (see [4])” (proof of Proposition 1.2(1), p. 2) | load-bearing entry to the two-dicritical profile used by every later lemma | The same explicit Proposition 4.1 binding replaces, and only replaces, part I's defective unique-μ=1 inference. **REPAIRED** for that slice. |

This is not a claim that Proposition 4.1 proves the whole sentence “greater
than 1.”  Part I divided the unique-dicritical degree-four case into transverse
orders 1, 2, and 3.  The charged audit identifies the order-one author
inference as `SOURCE-GAP; CAMPAIGN-REPAIRED`; Proposition 4.1 eliminates that
all-μ=1 profile.  It does **not** eliminate the surviving unique-μ=2 case.
Thus the entry to Proposition 1.2 retains part I's separate μ=2 exclusion (and
its other non-μ=1 inputs).  This lane neither re-audits nor silently replaces
that different part-I argument.

After Proposition 1.2, the dependence is transitive rather than a fresh use:
the labels (\widetilde g_1,\widetilde g_2), their
((m,n)=(1,1),(1,2)) data, (3.1), and every local/global block all presuppose
the two-dicritical entry.  They inherit the DO-I-2 binding once; they do not
license a stronger conclusion from Proposition 4.1.

The many other citations “[4], Lemma 2/3/5,” “[4], (2)–(6),” and the analogy
with “[4], Lemma 8” are technical determinant, canonical-class,
Riemann–Hurwitz, and block-enumeration dependencies.  They are not uses of
the unique-dicritical μ=1 *exclusion*.  They are audited on their own terms in
§§2–4 and receive no Proposition 4.1 halo.  In particular, campaign
Proposition 4.1 cannot fill a missing Fig. 8 or Fig. 11 enumeration step.

## 6. First-half disposition and forward boundary

After the recorded repairs, Lemma 3.12 exhausts all 35 raw signatures and
Lemma 3.14 exhausts the ten Fig. 11 quotient graphs.  No census row is open.

The root ledger does not close.  Corollary 3.8(b) leaves
**GAP-CANDIDATE[ROOT-U-LAST-CHAIN]**, and Lemma 3.15 leaves
**GAP-CANDIDATE[ROOT-DELTA-G2-APPLICATION]**.  Neither missing implication is
supplied by a determinant floor, linearity, or analogy.  Thus this lane
cannot promote **DOMRINA-II-SOUNDNESS**, although it does promote the two
census subclaims in their repaired form.

The only charged D–O I inheritance is bound as follows: DO-I-1 and DO-I-2
use campaign Proposition 4.1 solely for the unique-dicritical
all-\(\mu=1\) slice.  The broader “number greater than one” entry still
depends on part I's separate unique-\(\mu=2\) analysis; no campaign halo is
claimed for it.

Sections 5–7 remain for the sibling lane, including the forward uses of
Lemma 3.15, Lemma 7.10, and the omitted §7 calculations.  Thus

\[
\boxed{\text{CENSUSES REPAIRED AND EXHAUSTIVE;\quad
FIRST-HALF SOUNDNESS HAS TWO NAMED GAPS.}}
\]
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `39878`.
- Body SHA-256:
  `6eb2c7afb4647a419b6ada145de96e92ff7dd09cb67910b83c5dcc220c3dc486`.
- Frozen basis: `7a35f2d99c72179080a504484cfc1cf790abb642`.
