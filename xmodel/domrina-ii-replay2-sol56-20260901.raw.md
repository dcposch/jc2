# DOMRINA-II-REPLAY-2: hostile replay of Domrina II, §§5–7

**Lane:** second-half determinant/canonical replay.  **Charged boundary:**
REPLAY-1's census repairs and two unresolved root lemmas.  **Scope:** printed
pp. 16–32, including all §§5–6 claims, §7 arithmetic, and Lemma 7.10's cases.

## 0. Custody, scope, and verdict discipline

The custody gate was run before the sources were read.  The recomputed hashes
are

```text
0be24c5c6a9cc9423c3049c3402f2c98e44bac5f1c6018b3999989e0f32e5018  refs/domrina2000_izv64_four_sheeted_general_case.pdf
b838a2860c88d64d2a2162fd1a157e345db027bf4c7e95d2abae899dba9dc5de  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.pt5fZC/inputs/domrina-ii-replay1-sol56-20260901.md
5739b317366d0a3c8905fcdc642f823c7bb71d44b79c7101b2cac256512f4d01  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.pt5fZC/inputs/domrina-1999-audit-sol56-20260901.md
```

All match.  PDF and printed page numbers agree, and [4] is Domrina–Orevkov I.
For its technical identities only I also checked `refs/do.pdf`, SHA-256
`6ca30d797810400ddfcddb5b92b046796b3fdda5c1fb8f0ba378511506bbfed3`;
the same copy admitted by REPLAY-1.  It does not enlarge the campaign repair
of the defective one-dicritical inference.

The verdict column below is deliberately local.

- **REPLAYED-SOUND**: printed hypotheses and cited identities give the local
  implication; the decisive substitution is recorded.
- **REPAIRED** means that the paper suppresses a finite calculation, uses an
  unmapped analogy, or has a label error supplied here.
- **GAP**: no safe local replacement was found.

A local verdict does not erase upstream dependencies.  Thus
`REPAIRED | DEPENDS[...]` fills its own omission but cannot promote the theorem
until that dependency is repaired.

The two charged dependency tags retain exactly their REPLAY-1 meanings:

```text
DEPENDS[ROOT-U-LAST-CHAIN]
  = Corollary 3.8(b), p. 10: the last linear segment toward h^0 is not
    excluded from containing the root.

DEPENDS[ROOT-DELTA-G2-APPLICATION]
  = Lemma 3.15, pp. 14–15: the hypotheses needed to apply Lemmas 2.5–2.6
    to every selected vertex of delta(a~,g~2) were not established.
```

Tilded objects are source objects; untilded ones are targets.  Edge labels are
determinants or degrees only when declared.  No cv flag/place/series is
identified, and positivity supplies only sign/lower bounds, not attainment.
No exit price is asserted, so FALLACY-v2 `charge_basis` is inapplicable.

## 1. Shared replay interface and D–O I bindings

### 1.1 Determinant interface

For vertices \(x,y\) in a weighted tree \(\Gamma\), the technical identity
called “[4], (2)” is the edge-determinant identity

\[
 \det(xy)\det\Gamma
 =\det\operatorname{br}_{x}(y)\det\operatorname{br}_{y}(x)
  -\det(\Gamma-[xy])\det(\delta(xy))^2.                 \tag{E}
\]

Every use below specifies the ambient tree or branch.  The other technical
imports bind as follows.

| II citation | D–O I content used here | replay rule |
|---|---|---|
| [4], Lemma 2 | pairwise coprimality of branch determinants in a unimodular tree | used only after the branches and common vertex are identified |
| [4], Lemma 3 | at the root all branch determinants are one; away from it all off-root branches but at most one are one | the root-facing branch is fixed before charging a unit determinant |
| [4], Lemma 4 | a subgraph excluding the root has positive determinant | supplies positivity, not an exact value |
| [4], Lemma 5; [4], (6), (8) | determinant transfer through a constant-degree component | the source component, its image, endpoint indices, and exceptional factor are displayed |
| [4], (3) | canonical coefficient formula | invoked only at \(\widetilde g_1\) or \(\widetilde g_2\) after the vertex class and all branch data are fixed |
| [4], (4), (5) | local degree sum and Riemann–Hurwitz | already charged in the repaired Fig. 8 census |

The formulas used for the final canonical contradictions are REPLAY-1's
checked Lemmas 2.9–2.11.  To prevent the source's index reuse from doing
mathematical work, this report writes \(D_i\) for an essential-vertex degree
in (2.5), (2.6), (2.11), or (2.12), and reserves \(d_i\) for a figure label.
In particular, the \(d_2=2\) obtained in (7.11) is not the later canonical
\(D_2=4\).

### 1.2 The entry theorem versus technical imports

Sections 5–7 make no new direct “one dicritical is impossible” appeal, but
inherit Proposition 1.2's DO-I-2 entry: two dicriticals with
\((m,n)(\widetilde g_1)=(1,1)\) and
\((m,n)(\widetilde g_2)=(1,2)\).  Its charged binding is:

- the unique-dicritical all-\(\mu=1\) defect in D–O I is replaced only by the
  charged campaign Proposition 4.1;
- the unique-\(\mu=2\) exclusion and other part-I inputs remain source-bound;
- [4], Lemmas 2–5 and (2)–(8) are checked at their own hypotheses, receiving
  no halo from Proposition 4.1.

Every row therefore has background dependency DO-I-2; the two `DEPENDS[...]`
tags mark only the actual first-half gaps.

## 2. Section 5: Fig. 11 classes 1a–1d

### 2.1 Fig. 12 set-up and the two assertions

The first suppressed enumeration is the sentence on p. 16 that
\(\widetilde L_\infty\) “corresponds to one of the diagrams in Fig. 12.”
The port census gives twelve states: four left-of-\(\widetilde a\), one with
that package absent, two lower-port, three degree-two-route subdivisions, and
two degree-one right-port states.  They are the twelve rows without identifying
forks from repeated labels.  **Verdict: REPAIRED.**

Equations (5.1)–(5.3) are direct determinant-transfer statements.  Put

\[
 x=\det(\widetilde a\widetilde g_2)_\infty.
\]

At \(\widetilde a\), (5.1), (5.2), and [4], (6) reduce all of Assertion
5.1 to the single identity

\[
 {\det L_a\over4}\det D_a{\det D_a\over3}x
 ={\det L_a(\det D_a)^2x\over12},\qquad
 \det\widetilde L_\infty=-{\det D_a\over3}\,x.          \tag{5.A}
\]

The twelve port rows give only the following three factor pairs:

| Fig. 12 rows | \((\det D_a,x)\) | value from (5.A) |
|---|---:|---:|
| 1–5, 8, 9, 11, 12 | \((3,1)\) | \(-1\) |
| 6, 7 | \((\det U,1)\) | \(-\frac13\det U\) |
| 10 | \((3,\det U)\) | \(-\det U\) |

This is exactly Assertion 5.1(1)–(3), including its unstated divisibility
\(3\mid\det U\) in rows 6–7.  **Verdict: REPAIRED.**  Formula (5.3) does not
assert that the exceptional block and its image are the same object: it is a
determinant transfer with the endpoint index retained.

Assertion 5.2 checks separately.  In part (1), the selected nodal
\(\widetilde q\) is not a fork,
\(n(\widetilde q)=n(\widetilde g_2)=2\), and the displayed route is an
edge-type block; [4], Lemma 5 gives
\(\det(\widetilde q\widetilde g_2)=2\).  In part (2), the constant-degree
path has \(n(\widetilde q)=4\), [4], (8) transfers
\(\det(\widetilde q\widetilde a)=\det(qa)\), and (5.A) gives determinant
four on the \(\widetilde g_2\)-route.  Part (3) is
\(\det\widetilde D_q=\det D_q>1\), using Proposition 1.3 only after the
lower branch is fixed.  **Verdict: REPLAYED-SOUND.**

Finally, applying the same endpoint indices to \(L_h,(ah),R_h\) gives

\[
 \det\widetilde L_h={n(\widetilde h)\over4}\det L_h,
 \quad\det(\widetilde a\widetilde h)
 ={n(\widetilde h)\over4}\det(ah),
 \quad\det(\widetilde h\widetilde g_2)
 =n(\widetilde h)\det R_h,                              \tag{5.4}
\]

so (5.4) is **REPLAYED-SOUND**.

### 2.2 Claims 5.3–5.9 (class 1a)

The following ledger separates each local check from the charged root facts.
Throughout this report, “Both” is only a rendering shorthand for the literal
pair `DEPENDS[ROOT-U-LAST-CHAIN]` and
`DEPENDS[ROOT-DELTA-G2-APPLICATION]`; it is not a third tag.

| check | decisive replay | verdict | unresolved dependency |
|---|---|---|---|
| Lemma 5.3(1), p. 18 | (5.4) and the type-3 edge identity give \(\det L_h>0\); Lemma 2.12 then puts the root in exactly \((\widetilde h\widetilde g_1)\cup(\widetilde h\widetilde a)\cup(\widetilde a\widetilde g_2)\) | REPLAYED-SOUND | none |
| 5.3(2), root on \((\widetilde h\widetilde g_1)\) | after the two root lemmas make the opposite route linear/unit, (E) gives \(3\det L_a=1\) | REPLAYED-SOUND | Both |
| 5.3(3), root on \((\widetilde h\widetilde a)\) | if \(\det U=1\), Lemma 2.3 makes \(\widetilde h\) inessential and the same endpoint canonical string applies; in either branch (2.12) has \(D_n=3\), all preceding \(\mu_i=4\), and \(\det\widetilde L_\infty=-1\), whereas it requires \(-17\) | REPLAYED-SOUND | Both |
| 5.3(4), root on \((\widetilde a\widetilde g_2)\) | in (2.6), \(D_p=3,\mu_p=1\), the earlier \(\mu_i=4\), later \(\mu_i=2\); hence it requires \(\det\widetilde L_\infty=-7\), not \(-1\) | REPLAYED-SOUND | Both |
| Lemma 5.4(1), p. 18 | positivity and Lemma 2.12 leave only the two branches at \(\widetilde a\) | REPLAYED-SOUND | none |
| 5.4(2), root on the \(\widetilde g_1\)-side | row 5 is the 5.3(2) port map; in rows 6–7, \(3\mid\det U\) makes the negative right side in (E) at most \(-4\), not \(-2\); the other subcase has all \(\mu_i=1\) and determinant \(-1\), contradicting (2.11)'s \(-5\) | REPAIRED | Both |
| 5.4(3), root on the \(\widetilde g_2\)-side | the inessential case has all \(\mu_i=2\) and contradicts (2.5); in the essential case (2.6) gives \(D_1=\frac13\det U-4\), incompatible with \(D_1\in\{\det U,\frac13\det U,\det\widetilde L_a\}\); the last alternative occurs only in row 7, where \(\det U=3\) | REPLAYED-SOUND | Both |
| Lemma 5.5, p. 19 | the two root locations respectively invoke Lemmas 2.5–2.6 and Lemmas 2.3 plus Corollary 3.8; both contradict \(\det\widetilde D_h>1\).  The first use needs REPLAY-1's `REPAIRED[LEMMA-2.6-g1-TO-g2]`; the literal printed hypothesis would not suffice | REPAIRED | Both |
| Lemma 5.6(1), pp. 19–20 | the last-nodal-vertex descent proves \((\widetilde v\widetilde h)\) linear; (5.5), (E), and Lemma 2.12 exclude \(\widetilde h\cup\operatorname{br}_{\widetilde h}(\widetilde a)\) | REPAIRED | Both |
| 5.6(2) | all canonical \(\mu_i=1\) and \(\det\widetilde L_\infty=-1\), contradicting (2.11) | REPLAYED-SOUND | Both |
| 5.6(3) | all canonical \(\mu_i=2\) and determinant \(-1\), contradicting (2.5)'s \(-5\) | REPLAYED-SOUND | Both |
| Lemma 5.7(1), pp. 20–21 | subtracting the two equations (5.7) and the two canonical equations gives \(d-1=-1\), hence the impossible \(d=0\) | REPLAYED-SOUND | Both |
| 5.7(2) | (2.6) with \(D_1=d,\mu_1=1\), later \(\mu_i=2\), and determinant \(-d\) has residual \(4\) | REPLAYED-SOUND | Both |
| 5.7(3) | (2.11) with \(D_1=\mu_1=d\), later \(\mu_i=1\), gives \(d(d-1)=4\), with no integer solution | REPLAYED-SOUND | Both |
| Lemma 5.8(1), p. 21 | all \(\mu_i=1\) and determinant \(-1\) contradict (2.11) | REPLAYED-SOUND | Both |
| 5.8(2) | the paper cites Lemma 2.7, but the stated contradiction is Lemma 2.8: \(\widetilde a\) is the unique nodal vertex of the root–\(\widetilde g_2\) path, so \(\det\operatorname{br}_{\widetilde a}(\widetilde v)<-1\), contradicting the linear branch determinant \(3\) | REPAIRED[5.8-2.7→2.8] | DEPENDS[ROOT-U-LAST-CHAIN]; 5.8(1) also depends on ROOT-DELTA-G2-APPLICATION |

The port analogies in 5.4 and 5.6 preserve the target branch, endpoint index,
and root-facing route; they do not infer equality from a repeated numeral.
Consequently Lemmas 5.3–5.8 exhaust Fig. 12 locally and Lemma 5.9 follows.
**Local verdict for Lemma 5.9: REPLAYED-SOUND.  The theorem status of class 1a is
GAP through Both.**

### 2.3 Claims 5.10–5.11 (classes 1b–1d)

For 1b–1c, the suppressed determinant transfer in (5.8) is

\[
\begin{gathered}
 \det\widetilde D_a^3=1,\quad
 \det\widetilde D_a^1=\det D_a=3,\quad
 \det(\widetilde a\widetilde g_2)=1,\quad
 \det(\widetilde b\widetilde g_2)=2,\\
 \det(\widetilde a\widetilde b)=\tfrac12\det(ab)>0,\quad
 \det\operatorname{br}_{\widetilde a}(\widetilde b)_\infty>0,\quad
 \det\widetilde L_\infty<0.                            \tag{5.8}
\end{gathered}
\]

Thus (5.8) is **REPAIRED**.  Every nodal vertex on
\((\widetilde b\widetilde a)\) has determinant four toward
\(\widetilde g_2\).  Lemma 2.12 and (E) repair the unstated branch check in
5.10(1).  In 5.10(2), the 1b route is Corollary 3.8 directly; on the 1c route,
Lemma 3.16 makes \((bh)\) and the lifted chain linear, Assertion 3.6 gives the
terminal unit, and Lemma 2.3 propagates it.  This explicitly maps the printed
analogy but still consumes Corollary 3.8(b).

Let \(d=\det(\widetilde b\widetilde g_1)>0\), keeping it distinct from the
canonical degrees.  The two final substitutions are

\[
\begin{array}{c|c}
 \widetilde v\in(\widetilde b\widetilde a)&
 0=1-d+4(d+3)-2(d-1)=15+d \quad\text{from (2.12)},\\
 \widetilde v\in(\widetilde a\widetilde g_2)&
 0=3-d+4d-2(d-1)=5+d \quad\text{from (2.6)}.
\end{array}
\]

Both are impossible.  **Lemma 5.10: REPAIRED | Both.**

For Lemma 5.11, the source twice says “as in” without listing the port map.
The required map exchanges the non-right packages

\[
 j:(L=4,D=3+1)\quad\longleftrightarrow\quad
 m:(L=3+1,D=4),                                      \tag{5.B}
\]

while retaining the same right carrier and its endpoint indices.  This first
excludes incidence of \(\widetilde g_1\) with a right arm.  More explicitly,
Fig. 12 rows 5, 8, 9, 10, and the symmetric pair 11–12 are the five
transported classes: the missing \(U^0\)-port, the unsubdivided degree-two
port, its \((1,2)\) and \((2,1)\) subdivisions, and the degree-one-port
class.  They reproduce Lemmas 5.4–5.8 respectively.  This is not target
\(L/D\) symmetry: Proposition 1.3 supplies positivity/coprimality, Lemma 3.16
controls the left route, and \(D_h=U\) at \(a=h\) leaves only target types
2–3.  Direct transfer also supplies the compressed formula

\[
 \det(\widetilde a\widetilde g_2)=1,\quad
 \det D_a=4\det\widetilde D_a,\quad
 \det L_a=\det\widetilde L_a^1=3\det\widetilde L_a^3,
\]

\[
 \det\widetilde L_\infty=
 \begin{cases}
 -1,&\widetilde g_1\text{ on }\widetilde D_a,\\
 -\frac13\det L_a,&\widetilde g_1\text{ on }
       \widetilde L_a^1\text{ or }\widetilde L_a^3.
 \end{cases}                                           \tag{5.9}
\]

Hence (5.9) is **REPLAYED-SOUND**.
If \(\widetilde g_1\) is on a left arm, (5.B) sends the two root routes to
rows 6–7 of Lemma 5.4.  On the \(\widetilde g_1\)-side the essential edge
equation is
\(-2=-\lambda/3-(\lambda^2/3)\det\widetilde D_{\widetilde a}\);
integrality gives \(3\mid\lambda\), so its right side is at most \(-4\).
On the \(\widetilde g_2\)-side, an inessential \(\widetilde a\) has
\(\lambda=3\), determinant \(-1\), and all \(\mu_i=2\), contradicting
(2.5)'s \(-5\).  If it is essential, (2.6) gives
\(D_1=\lambda/3-4\) with
\(D_1\in\{\lambda,\lambda/3,\det\widetilde D_a\}\); the third alternative
occurs only for \(\lambda=3\), so none is possible.
If \(\widetilde g_1\) is on the lower arm, (2.6) with
\(D_1=3,\mu_1=1\), later \(\mu_i=2\), and determinant \(-1\) has residual
\(6\); the other root route is the already displayed determinant contradiction
of 5.3(2).  This supplies both suppressed transfers.  **Lemma 5.11:
REPAIRED | Both.**

Accordingly §5 contains no new intrinsic GAP.  It does contain one corrected
lemma citation and several filled finite analogies.  Its four Fig. 11
conclusions 1a–1d all remain globally infected by each charged root gap.

## 3. Section 6: Fig. 11 classes 3a–3b

### 3.1 Lemma 6.1 and the Fig. 13 transfer

Equation (6.1) is the degree/determinant transfer at the two forks and is
**REPLAYED-SOUND**.  In the printed 3a notation it is

\[
\begin{gathered}
 \det\widetilde D_a^1=\det D_a=2,\quad
 \det\widetilde D_a^2=1,\quad
 \det\widetilde R_a^1=\det(\widetilde a\widetilde g_2)=\det R_a=1,\\
 \det(\widetilde a\widetilde b)=\tfrac13\det(ab)>0,\quad
 \det(\widetilde b\widetilde g_2)=\det\widetilde R_b^1=\det R_b=1,\\
 \det\widetilde D_b^1=3\det\widetilde D_b^3,\quad
 \det L_1=\det L_2=\tfrac12\det L_b,\quad
 \det\widetilde L_\infty=-2\det L_1\det\widetilde D_b^3. \tag{6.1}
\end{gathered}
\]

Under the contrary assumption that
\(\widetilde g_1\) is not incident to
\((\widetilde b\widetilde g_2)\), its possible ports are exhaustive: the
type-1 \(h=b\) port, the right degree-one port, either left port, or either
lower port.  The first three are excluded by Corollary 3.8, Lemma 2.3, and
the unit-branch rule.  On a lower port, (6.2) gives determinant three along
\((\widetilde a\widetilde b)\) and determinant two along
\((\widetilde a\widetilde g_2)\).  The two root positions then have the
following canonical outcomes:

- on \((\widetilde a\widetilde b)\), (2.12) either contradicts
  \(\det\widetilde L_\infty=-2\), or gives
  \(D_1=\det\widetilde D_b^3-4\), incompatible with
  \(D_1\in\{\det\widetilde D_b^3,3\det\widetilde D_b^3\}\);
- on \((\widetilde a\widetilde g_2)\), (2.6) similarly gives
  \(D_1=\det\widetilde D_b^3-2\).

The p. 23 reference to “(6.5)” is impossible—no such formula exists—and the
data used are exactly (6.2).  **Repair: (6.5)→(6.2).**  The printed proof
does 3a only.  For 3b, exchange the left and lower packages at
\(\widetilde b\):

\[
 \det\widetilde L_b^1=3\det\widetilde L_b^3,
 \qquad \det\widetilde D_b^2=\det\widetilde D_b^{2\prime},
 \qquad
 \det\widetilde L_\infty
   =-2\det\widetilde L_b^3\det\widetilde D_b^2.
\]

The same two canonical substitutions, now with
\(t=\det\widetilde L_b^3\), apply when \(\widetilde g_1\) is on a left
branch: both degree-two lower determinants are then one and
\(D_1\in\{t,3t\}\), whereas the equations give \(D_1=t-4\) and
\(D_1=t-2\).  A lower placement is the exchanged Lemma 2.3/unit-branch
case.  This is the missing companion check.  **Lemma 6.1: REPAIRED | Both.**

Corollary 6.2 follows from the unit branches at \(\widetilde b\) and [4],
(6):

\[
 \det\widetilde L_\infty
   =-2\det(\widetilde b\widetilde g_2)_\infty.          \tag{6.A}
\]

Its wording “the lower branch of degree 1 ... equals three” is true for 3a.
For 3b it is the **left** degree-one branch.  The product in (6.A) is
unchanged.  **Corollary 6.2: REPAIRED[LOWER→LEFT-IN-3b] | Both.**

The omitted proof of Assertion 6.3 reduces to two master identities,

\[
 \det\widetilde D_a^1=2\det\widetilde D_a^2,
 \qquad
 \det\widetilde L_\infty
 =-\det\widetilde D_a^1
    \det(\widetilde a\widetilde g_2)_\infty.           \tag{6.B}
\]

Reading all eleven Fig. 13 rows gives the complete table:

| Fig. 13 rows | determinant data | conclusion |
|---|---|---|
| 1–4, 7–10 | \(\det\widetilde D_a^1=2,\det\widetilde D_a^2=1\), both displayed \(\widetilde g_2\)-routes unit | \(\det\widetilde L_\infty=-2\) |
| 5–6 | \(\det\widetilde D_a^1=\det U=2\det\widetilde D_a^2\), \(\det(\widetilde a\widetilde g_2)=1\) | \(\det\widetilde L_\infty=-\det U\) |
| 11 | \(\det\widetilde D_a^1=2,\det\widetilde D_a^2=1\), \(\det(\widetilde a\widetilde g_2)_\infty=\det U\) | \(\det\widetilde L_\infty=-2\det U\), and each upper \(\widetilde h\)-edge has determinant \(\det U\) |

The three carrier classes are exhaustive: no exceptional \(U\)-factor gives
rows 1–4 and 7–10, the lower carrier gives 5–6, and the
\((\widetilde a\widetilde g_2)\)-carrier gives 11.  Assertion 3.9 excludes
two simultaneous exceptional carriers.  **Fig. 13 enumeration: REPAIRED.**

Part (d) is the degree-three counterpart of Assertion 5.2: a nonfork nodal
\(\widetilde s\in\langle\widetilde h,\widetilde a\rangle\cup\{\widetilde h\}\)
has the same endpoint index as the degree-three route; [4], (8) transfers
the constant-degree path and [4], (6) supplies
\(\det(\widetilde s\widetilde g_2)=3\).  This proves every part, rather than
importing the word “analogously.”  **Assertion 6.3: REPAIRED | Both** (the
dependency is transitive through Lemma 6.1 and Corollary 6.2).

### 3.2 Lemmas 6.4–6.12

| check | decisive replay | verdict | unresolved dependency |
|---|---|---|---|
| Lemma 6.4, p. 25 | Lemmas 2.3–2.4 put the root on \((\widetilde h\widetilde g_1)\); Lemma 2.7 and Assertion 6.3(d) then force the supposedly \(>1\) linear \(\widetilde D_h\) to have determinant one | REPLAYED-SOUND | Both, transitively |
| Lemma 6.5 | if the root avoided both dicritical routes, (E) first makes the intermediate branch negative; the last-nodal descent of 5.6(b), with (6.3), makes \((\widetilde v\widetilde h)\) linear.  The two displayed edge equations then give a positive off-route branch and Lemma 2.12 returns the root to a dicritical route | REPAIRED | Both |
| Lemma 6.6(1), p. 25 | (2.11) receives \(\det\widetilde L_\infty=-2,D_1=2,\mu_1=0\), later \(\mu_i=1\), leaving residual \(4\) | REPLAYED-SOUND | Both |
| Lemma 6.6(2) | the remaining routes give: \(D_n=2,\mu_i=3\ (i<n)\), so (2.12) requires determinant \(-10\); or \(D_p=2,\mu_p=1\), earlier \(\mu_i=3\), later \(\mu_i=2\), so (2.6) requires \(-6\), not \(-2\) | REPAIRED | Both |
| Lemma 6.7, p. 26 | all \(\mu_i=1\) and determinant \(-2\) contradict (2.11), which requires \(-5\).  The value \(-2\) comes from Assertion 6.3(a), not, as printed, from Corollary 3.8 | REPAIRED[6.7-ATTRIBUTION] | Both |
| Lemma 6.8(1) | positivity plus (6.B) and Lemma 2.12 gives the stated three-branch union | REPLAYED-SOUND | Both, transitively |
| Lemma 6.8(2), first port order | (E) gives \(\det\operatorname{br}_{\widetilde a}(\widetilde b)=-(2d-2)/(2d+1)\), strictly between \(-1\) and \(0\) for integer \(d>1\) | REPLAYED-SOUND | Both |
| Lemma 6.8(2), second port order | integrality of \(-(2d-2)/(d+2)\) forces \(d+2\mid6\), hence \(d=4\) and the branch determinant is \(-1\); the next edge equation is \(2=-6x-1\), impossible for integral \(x\) | REPAIRED | Both |
| Lemma 6.9(1), p. 26 | (2.6) gives \(0=4-\det U+D_1\).  The three candidates for \(D_1\) leave only \((\det U,D_1)=(8,4)\), while (E) then says \(-24=-12\) | REPLAYED-SOUND | Both |
| Lemma 6.9(2) | in the inessential case (2.11) requires determinant \(-5\), incompatible with the even \(-\det U\); in the essential case \(-2=-\det U-\frac12(\det U)^2\det\operatorname{br}_{\widetilde a}(\widetilde b)\), whose right side is at most \(-4\) | REPAIRED | Both |
| Lemma 6.10, p. 27 | Fig. 13(7), (8), (10) map to Fig. 12(8), (11), (12), respectively, with \(\det\widetilde D_a^1:3\mapsto2\) and \(\det\widetilde L_\infty:-1\mapsto-2\).  The corrected \(g_2\)-hypothesis of Lemma 2.6 gives the first sign contradiction; the others give all \(\mu_i=1\) or a unit linear branch contradicting determinant two | REPAIRED | Both |
| Lemma 6.11(1) | the mapped 5.7/5.6 descent gives (6.4).  Its second printed bound must be weakened: \(3\det U/2-2\ge1\), not always \(\ge2\); positivity is all Lemma 2.12 needs | REPAIRED[6.4-BOUND] | Both |
| Lemma 6.11(2a) | (2.6) with \(D_1=\det U,\mu_1=1\), determinant \(-2\det U\), later \(\mu_i=2\), gives \(\det U=4\); then \(2\mid\det(ah)\), but \(\gcd(\det(ah),\det D_a)=1\) and \(\det D_a=2\) | REPLAYED-SOUND | Both |
| Lemma 6.11(2b) | the mapped (2.11) calculation gives \(4-(\det U)^2=0\), hence \(\det U=2\), and the same \(\det D_a=2\) coprimality contradiction | REPAIRED | Both |

The analogies in Lemmas 6.10–6.11 are therefore finite determinant maps, not
new structural assumptions.  Lemmas 6.4, 6.6, 6.7, and 6.9–6.11 exhaust all
eleven Fig. 13 rows, so Lemma 6.12 follows locally.  **Lemma 6.12:
REPAIRED; no new §6 GAP.**  Globally, classes 3a–3b depend on Both through
Lemma 6.1 even where a later row has no fresh direct citation.

## 4. Section 7: the omitted calculations and Lemma 7.10

### 4.1 Fig. 14 parameters and integrality

Keep the graph \(\delta(ab)\) distinct from its determinant
\(\delta:=\det\delta(ab)\).  Put

\[
 X=d_0d_1d_3\delta^2,\qquad H=18X-2d_2,\qquad P=6X-d_2.
\]

Let \(\widetilde V\) be the possible unique non-edge-type block and \(d_4\)
the determinant of its degree-one branch.  The bracketed possibilities in
Fig. 14 are

| position of \(\widetilde V\) | ordinary label | actual label | path factor |
|---|---:|---:|---:|
| left branch at \(\widetilde a_1\) | \(d_0\) | \(d_4d_0\) | \(1\) |
| crossed \((\widetilde a_1\widetilde b_2)\)-block | \(d_2\) | \(d_4d_2\) | \(d_4\) |
| right branch at \(\widetilde b_2\) | \(1\) | \(d_4\) | \(1\) |

Thus \(\lambda=1\) except in the middle row, where \(\lambda=d_4\).
The half-label argument on p. 28 is valid after supplying its Bézout step.
If an exceptional block occurs on the relevant branch, both \(2d_i\) and
\(d_4d_i\) are integral.  At its internal \((2,1)\)-fork, [4], Lemma 2
makes \(d_4\) coprime to the even determinant on the other controlled branch,
so \(d_4\) is odd.  Hence \(d_i\in\mathbb Z\).  For \(d_0\) this is the
printed \(\det U=d_4\), even-\(\det L_h\) argument; for \(d_2\) the same
calculation uses \(n(\widetilde a_1)=1\) and \(\det R_a=1\).  If the
exceptional block is elsewhere, the parameter is itself an edge-type
determinant.  **Integrality of \(d_0,d_2\): REPAIRED.**

### 4.2 Reconstruction of (7.1)–(7.6)

The exact p. 28 omission is: “We omit some intermediate calculations, which
are similar to those in [4], Lemma 10.”  Determinant transfer along the three
constant-degree lifts gives

\[
\det\delta(\widetilde a_2\widetilde b_2)_\infty
=\det\delta(\widetilde a_1\widetilde b_1)_\infty=\delta,
\qquad
\det\delta(\widetilde a_1\widetilde b_2)_\infty=\lambda\delta. \tag{7.1}
\]

For \((ab)\subset L\), (E) reads

\[
 (2d_2)(-1)=\det R_a\det L_b
 -(2d_0)(3d_1)(3d_3)\delta^2,
\]

and therefore

\[
 \det L_b=18d_0d_1d_3\delta^2-2d_2=H,
 \qquad
 \det\operatorname{br}_{\widetilde a_1}(\widetilde b_1)_\infty=1. \tag{7.2}
\]

Formula [4], (6), on the two indicated inverse-image components gives

\[
 \det\Delta_{\widetilde a_1}=\lambda d_0d_2H,
 \qquad
 \det\Delta_{\widetilde b_2}=\lambda d_2.              \tag{7.3}
\]

Set \(B=\det\operatorname{br}_{\widetilde b_2}
(\widetilde a_1)_\infty\).  Formula (E) for
\((\widetilde a_1\widetilde b_1)_\infty\) gives

\[
\begin{aligned}
 2d_2B
 &=\lambda\{d_0d_2H-6d_0^2d_1d_2d_3\delta^2\}\\
 &=2\lambda d_0d_2P,
\end{aligned}
\]

so

\[
 B=\lambda d_0P.                                      \tag{7.4}
\]

The companion calculation for
\((\widetilde a_2\widetilde b_2)_\infty\) is

\[
 2d_2\det\operatorname{br}_{\widetilde a_1}
      (\widetilde b_2)_\infty
 =\lambda d_2(H-6X)=2\lambda d_2P,
\]

hence

\[
 \det\operatorname{br}_{\widetilde a_1}
      (\widetilde b_2)_\infty=\lambda P.              \tag{7.5}
\]

After factoring the bracketed \(d_4\) in each of the three positions above,
the final two edge formulas reduce uniformly to

\[
\begin{aligned}
 d_2\det\widetilde L_\infty
  &=\lambda d_0(P^2-2XH)=\lambda d_0d_2(d_2-8X),\\
 d_2\det\operatorname{br}_{\widetilde a_2}
      (\widetilde b_2)_\infty
  &=\lambda d_0d_2(P-4X)=\lambda d_0d_2(2X-d_2).
\end{aligned}
\]

The Fig. 14 edge block \((ab)\) excludes the target root, hence [4], Lemma 4
gives \(2d_2=\det(ab)>0\).  Thus every cancelled factor is positive, and

\[
 \det\widetilde L_\infty
   =\lambda d_0(-8d_0d_1d_3\delta^2+d_2),
 \qquad
 \det\operatorname{br}_{\widetilde a_2}(\widetilde b_2)_\infty
   =\lambda d_0(2d_0d_1d_3\delta^2-d_2).              \tag{7.6}
\]

This checks both the p. 28 omission and the p. 29 sentence “The other cases
are studied analogously.”  **Equations (7.1)–(7.6): REPAIRED.**

### 4.3 Lemmas 7.1–7.8

| check | decisive replay | verdict | unresolved dependency |
|---|---|---|---|
| Lemma 7.1, p. 29 | part (1) is the rooted branch rule at the two branches of determinant \(>1\); part (2) is the common sign in (7.4)–(7.5); part (3) substitutes \(d_2<6X\) in (7.6), then applies Lemma 2.12 | REPLAYED-SOUND | none |
| Lemma 7.2, p. 30 | positivity of the complementary source pieces and Lemma 7.1(3) give \(\det\widetilde L_\infty<0\); Lemma 2.12 fixes the only possible \(\widetilde g_1\)-port | REPLAYED-SOUND | none |
| Lemma 7.3 | positivity in (7.6) gives \(d_2<2X\), hence (7.4) gives \(B>4\); the root rule forces \(d_0=d_1=d_3=1\).  The two \(\widetilde g_1\)-ports give either \(d_2-2d_2^2\det\delta(\widetilde b_2\widetilde g_2)^2<0\), or \(B=3\) | REPLAYED-SOUND | none |
| Corollary 7.4 | Lemmas 7.1 and 7.3 plus the root rule give the incidence, root union, and \(d_0=d_1=1\); uniqueness of the \(\widetilde g_1\)-flag removes the exceptional block | REPLAYED-SOUND | none |
| Lemma 7.5(1) | the unit branch follows directly at \(\widetilde a_2\) | REPLAYED-SOUND | none |
| Lemma 7.5(2) | map Lemma 5.10(2) with \(\widetilde b\mapsto\widetilde a_2\); Corollary 3.8 handles the terminal \(U^0\)-piece, while Lemma 3.16/Assertion 3.6 and Lemma 2.3 handle the type-3 route | REPAIRED | DEPENDS[ROOT-U-LAST-CHAIN] |
| Lemma 7.6 | (E) on \((\widetilde a_2\widetilde g_1)\) gives \(9d_3\delta^2-4d_2\) for the left port and \(6d_3\delta^2-2d_2\) for the lower port | REPAIRED | DEPENDS[ROOT-U-LAST-CHAIN] through 7.5 |
| Lemma 7.7 | if the root avoided the asserted union, (7.4) would give \(d_2\ge6d_3\delta^2\), making both values in Lemma 7.6 negative on a root-free branch | REPLAYED-SOUND | DEPENDS[ROOT-U-LAST-CHAIN] |

Lemma 7.8 suppresses a second determinant calculation.  For the first nodal
\(k\in(ab)\) with \((ka)\) linear, the three distinct, nonfork lifts in
Fig. 15 give

\[
\begin{aligned}
 \det(\widetilde k_3\widetilde g_1)&=\det L_k,&
 \det(\widetilde k_1\widetilde k_2)&=d_5\det L_k,\\
 \det(\widetilde k_3\widetilde k_2)_\infty&=d_7,&
 \det L_k&=6d_6-d_5.                                  \tag{7.8}
\end{aligned}
\]

The three distinct rooted-vertex applications give the omitted display

\[
 \det\operatorname{br}_{\widetilde k_2}(\widetilde a_1)
 =\det\operatorname{br}_{\widetilde a_1}(\widetilde b_1)
 =\det\operatorname{br}_{\widetilde k_1}(\widetilde b_1)=1.       \tag{7.9}
\]

Formula (E) for
\((\widetilde a_1\widetilde k_1)\) then gives

\[
 \det L_k=1+2d_6,\qquad d_5=4d_6-1.                  \tag{7.10}
\]

Lemma 7.5 and (E) make the determinant toward \(\widetilde a_2\) equal to
\(2-5d_6<0\) on the left port and \(1-2d_6<0\) on the lower port, so the
root lies there.  Lemma 3.15 supplies the opposite unit delta.  The next edge
identity is

\[
 d_7=d_7\det\operatorname{br}_{\widetilde b_2}(\widetilde g_2)
       -d_7^2d_3,
\]

so the displayed branch determinant is \(>1\); the root rule gives
\(d_3=B=1\).  Finally,

\[
 d_7\det(\widetilde k_3\widetilde g_2)
 =d_7-d_7^2d_6
   \det\delta(\widetilde k_2\widetilde b_2)^2<0,
\]

although this subgraph excludes the root.  Hence
\(\delta(ab)=\varnothing\).  Hereafter
\(\delta=\det\varnothing=1\), not zero.  **Lemma 7.8: REPAIRED |
DEPENDS[ROOT-U-LAST-CHAIN] |
DEPENDS[ROOT-DELTA-G2-APPLICATION].**

### 4.4 Lemmas 7.9–7.11 and the full Lemma 7.10 split

Corollary 7.4 gives \(d_0=d_1=1\), and all Fig. 14 edges are now edge type,
so \(\lambda=1\).  Under Lemma 7.9's contrary root placement, the rooted
branch rule gives \(d_3=1\) and
\(\det\operatorname{br}_{\widetilde b_2}(\widetilde a_2)=1\).  Lemma 7.6
then has exactly two possibilities:

\[
 9-4d_2=1\Rightarrow d_2=2,
 \qquad
 6-2d_2=1\Rightarrow d_2=5/2\notin\mathbb Z.
\]

Thus \(\widetilde g_1\) is on the left port, and

\[
 d_2=2,\quad B=4,\quad \det\widetilde L_\infty=-6,\quad
 \det\operatorname{br}_{\widetilde a_2}(\widetilde b_2)_\infty=0. \tag{7.11}
\]

Rename the canonical degrees \(D_1=3,D_2=4\).  Formula (2.5), with
\(\mu_1=0,\mu_2=1\) and later \(\mu_i=2\), has residual

\[
 3-6+2(3)(4)-\{0(3-1)+1(4-1)3\}=12.
\]

**Lemma 7.9: REPLAYED-SOUND | DEPENDS[ROOT-U-LAST-CHAIN] |
DEPENDS[ROOT-DELTA-G2-APPLICATION].**  Notice that the printed Fig. 14
parameter \(d_2=2\) and the canonical degree \(D_2=4\) are different
quantities.

For Lemma 7.10 assume
\(\widetilde v\in(\widetilde a_2\widetilde b_2)\) and put

\[
 t=d_3,\qquad s=B=6t-d_2,\qquad
 r=D_1=d(\widetilde a_2)\in\{2,3\}.
\]

The rooted branch rule says that at least two of the three off-route branch
determinants at \(\widetilde b_2\) are one.  The cases are exactly:

1. **\(\widetilde b_2\) inessential:** \(t=s=1\).  Then \(d_2=5\),
   \(\det\widetilde L_\infty=-3\), and the sole canonical
   \(\mu_1=-3\).  Equation (2.5) has residual
   \(5r-3\in\{7,12\}\).
2. **Essential, \(t=1,s>1\):** \(d_2=6-s,D_2=s,\mu_1=s-4\), and
   \(\det\widetilde L_\infty=-s-2\).  Substitution in (7.12) gives
   \[
      s^2+s+5r-5>0.
   \]
   In the printed variable this is
   \(d_2^2-13d_2+37+5r\); its discriminants for \(r=2,3\) are
   \(-19,-39\).
3. **Essential, \(s=1,t>1\):** \(d_2=6t-1,D_2=t,\mu_1=1-4t\), and
   \(\det\widetilde L_\infty=-2t-1\).  Equation (7.12) has residual
   \[
      t^2+5t(r-1)+1>0.
   \]

There is no fourth case: \(t=s=1\) is precisely the inessential row, while
an essential row cannot have both \(t>1\) and \(s>1\), since then only the
\(\widetilde g_2\)-branch determinant would be one.  This replaces the p. 32
sentence “Successive consideration of all cases ...”.  **Lemma 7.10:
REPAIRED | DEPENDS[ROOT-U-LAST-CHAIN] |
DEPENDS[ROOT-DELTA-G2-APPLICATION]**, also consuming REPLAY-1's repaired
Lemma 2.11.

The p. 27 parenthesis “The case 4a) is similar” is repaired by a port map,
not by swapping physical places.  Case 4a exchanges the left fork's
\(D=(2,1,1)\) and \(B=(3,1)\) sheet partitions between \(L_a,D_a\), so
\(2d_0\leftrightarrow3d_1\); the joining edge, right fork, and
\(\widetilde g_2\)-route are unchanged.  Before Corollary 7.4 the formulas
use these parameters only through \(d_0d_1\); afterward both equal one.
Lemma 7.6 already separates the two \(\widetilde g_1\)-ports, the two
Lemma 7.8 determinants remain negative, and Lemma 7.10 includes both
\(r=2,3\).  The exceptional a/c placements are both in the three-row
\(d_4\)-audit.  **Case 4a transfer: REPAIRED | Both.**

Thus Lemma 7.11 is locally **REPAIRED** for 4a and 4b.  It depends on
ROOT-U through Lemmas 7.5–7.10 and on ROOT-DELTA directly through Lemmas
7.8–7.10: `DEPENDS[ROOT-U-LAST-CHAIN]` and
`DEPENDS[ROOT-DELTA-G2-APPLICATION]`.  Section 7 introduces no new intrinsic
GAP.

## 5. Complete soundness graph and minimal promotion set

### 5.1 Claim disposition

| node | local result after the charged replays | theorem-chain status |
|---|---|---|
| D–O I unique-dicritical all-\(\mu=1\) slice | SOURCE-GAP; campaign Proposition 4.1 supplies the charged replacement | REPAIRED for exactly that slice |
| D–O I unique-\(\mu=2\) slice | not re-audited here; retained exactly as the REPLAY-1 native binding | source trust boundary, not covered by Proposition 4.1 |
| Proposition 1.2 two-dicritical entry | DO-I-2 binding made explicit | conditional on the preceding two rows |
| Lemma 3.12 / Fig. 8 | all 35 raw signatures, charged from REPLAY-1 | REPAIRED/exhaustive |
| Lemma 3.14 / Fig. 11 | all ten quotient graphs, charged from REPLAY-1 | REPAIRED/exhaustive |
| Fig. 11(2a–2b), §4 | orientation and omitted companion calculation repaired by REPLAY-1 | closed relative to DO-I-2; neither root gap is used |
| Fig. 11(1a–1d), §5 | all Fig. 12 ports and terminal equations replayed; wrong 5.8 citation corrected | locally REPAIRED; depends on both root gaps |
| Fig. 11(3a–3b), §6 | 3b, Fig. 13, Assertion 6.3, Lemmas 6.10–6.11 supplied; source labels/bound corrected | locally REPAIRED; depends on both root gaps |
| Fig. 11(4a–4b), §7 | (7.1)–(7.6), Fig. 15, 4a transfer, and Lemma 7.10 cases supplied | locally REPAIRED; depends on both root gaps |
| Lemma 7.11 and main theorem | all ten Fig. 11 rows have local eliminations | **GAP, inherited from the two root nodes** |

There is no new intrinsic §§5–7 GAP.  “No new gap” is not an unconditional
soundness verdict: both charged gaps are used downstream, so Domrina's theorem
cannot yet be promoted by this replay.

### 5.2 Dependency graph

```text
D–O I unique-dicritical analysis
  ├─ all-μ=1 author inference
  │    └─ REPAIRED by charged campaign Proposition 4.1 (only this slice)
  └─ unique-μ=2 and other native inputs
       └─ retained D–O I binding
            ↓
      Proposition 1.2 / DO-I-2 two-dicritical profile
            ↓
      §§1–3 block machinery
            ↓
      Lemma 3.12 (35 raw signatures) ── REPAIRED
            ↓
      Lemma 3.14 (ten Fig. 11 graphs) ── REPAIRED
            ├─ 2a,2b → Lemma 4.1 ── REPAIRED → excluded
            ├─ 1a–1d → Lemmas 5.3–5.11 ── locally REPAIRED ─┐
            ├─ 3a,3b → Lemmas 6.1–6.12 ── locally REPAIRED ├─→ Lemma 7.11
            └─ 4a,4b → Lemmas 7.1–7.10 ── locally REPAIRED ┘       ↓
                                                               Theorem

GAP-CANDIDATE[ROOT-U-LAST-CHAIN]
  → Corollary 3.8(b)
  → §5: 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.10, 5.11 → 5.9/§5
  → §6: Lemma 6.1 → Cor. 6.2/Assertion 6.3 → 6.4–6.12
  → §7: Lemma 7.5 → 7.6–7.10 → 7.11
  → Theorem

GAP-CANDIDATE[ROOT-DELTA-G2-APPLICATION]
  → Lemma 3.15
  → §5: 5.3–5.7, 5.8(1), 5.10, 5.11 → 5.9/§5
  → §6: Lemma 6.1 → Cor. 6.2/Assertion 6.3 → 6.4–6.12
  → §7: Lemmas 7.8, 7.9, 7.10 → 7.11
  → Theorem
```

The two root infections are not interchangeable.  ROOT-U supplies the
last-chain root exclusion and unit \(\widetilde g_1\)-delta; ROOT-DELTA
supplies the \(\widetilde g_2\)-side root exclusion/inessentiality used by
Lemma 3.15.  Repairing only one leaves §5, §6, and §7 open.

### 5.3 Minimal repairs

Under the charged D–O I bindings, the **minimal remaining mathematical repair
set** is exactly

\[
 \{\text{ROOT-U-LAST-CHAIN},\qquad
   \text{ROOT-DELTA-G2-APPLICATION}\}.                 \tag{M}
\]

| obligation | present status | repair scale | reason |
|---|---|---|---|
| ROOT-U-LAST-CHAIN | GAP | lane-repairable | needs a genuine endpoint/last-linear-segment determinant argument; it is narrower than the census but not a one-line substitution |
| ROOT-DELTA-G2-APPLICATION | GAP | lane-repairable | must verify the delta-unit and corrected \(g_2\)-essential hypotheses for every selected vertex, then convert the negative branch determinant against the correct positive component |
| second-half analogies and arithmetic | installed in §§2–4 above | desk-repairable/completed | finite port maps and integer substitutions; no new theorem used |
| D–O I all-\(\mu=1\) entry | charged external replacement installed | structural/completed | campaign Proposition 4.1 replaces an invalid source inference, but only on its declared slice |
| D–O I unique-\(\mu=2\) entry | explicit native binding | structural trust boundary, not a newly found gap | a standalone proof would require a separate part-I replay; it is not in minimal set (M) under the user's charged basis |

The local desk repairs that must remain attached to any corrected edition are:

```text
REPAIRED[LEMMA-5.8-2.7-TO-2.8]
REPAIRED[LEMMA-6.1-CASE-3B]
REPAIRED[6.5-TO-6.2]
REPAIRED[COR-6.2-3B-LEFT-NOT-LOWER]
REPAIRED[LEMMA-6.7-ATTRIBUTION]
REPAIRED[LEMMA-6.10-THREE-CASES]
REPAIRED[6.4-LOWER-BOUND]
REPAIRED[SECTION-7-(7.1)-(7.6)/FIG15/4A/7.10]
```

If both elements of (M) are proved, then, **relative to the stated D–O I
unique-\(\mu=2\) trust boundary**, REPLAY-1 plus the repairs in this report
make Domrina's entire displayed chain sound.  If either root obligation
fails rather than merely lacking a proof, every terminal family except the
independent §4 elimination loses its current route, and a structural
replacement for §§5–7 would be required.

## 6. Final typed verdict

\[
\boxed{\begin{gathered}
 \text{§§5–7 LOCAL OMISSIONS REPAIRED; NO NEW INTRINSIC GAP;}\\
 \text{DOMRINA-II-SOUNDNESS = GAP (TWO INHERITED ROOT OBLIGATIONS).}
\end{gathered}}
\]

This is a clean completion boundary for REPLAY-2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->`
  line, including its terminating newline; this seal is outside the body.
- Body bytes: `39642`.
- Body SHA-256: `89d794a7b79d4e43092e2dac1215272fced8a1aa0d3436adffc4ab07b87d3a71`.
- Frozen basis: the official PDF and two charged-input digests listed in §0,
  all reverified at completion.
