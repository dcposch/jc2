# DOMRINA-II-REPLAY-2: hostile replay of Domrina II, §§5–7

**Lane:** second-half determinant and canonical-class replay.  **Charged
boundary:** the first-half census repairs and the two unresolved root lemmas
from `DOMRINA-II-REPLAY-1`.  **Scope:** printed pp. 16–32 of the official
English PDF, including every claim in §§5–6, the suppressed arithmetic in §7,
and the terminal case check in Lemma 7.10.

## 0. Custody, scope, and verdict discipline

The custody gate was run before the sources were read.  The recomputed hashes
are

```text
0be24c5c6a9cc9423c3049c3402f2c98e44bac5f1c6018b3999989e0f32e5018  refs/domrina2000_izv64_four_sheeted_general_case.pdf
b838a2860c88d64d2a2162fd1a157e345db027bf4c7e95d2abae899dba9dc5de  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.pt5fZC/inputs/domrina-ii-replay1-sol56-20260901.md
5739b317366d0a3c8905fcdc642f823c7bb71d44b79c7101b2cac256512f4d01  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.pt5fZC/inputs/domrina-1999-audit-sol56-20260901.md
```

All three equal the charged values.  The PDF has 33 pages, and PDF page
number (i) is printed page (i).  The bibliography identifies [4] as
Domrina–Orevkov I.  For checking only its technical determinant identities I
also used the repository copy `refs/do.pdf`, SHA-256
`6ca30d797810400ddfcddb5b92b046796b3fdda5c1fb8f0ba378511506bbfed3`;
this is the same auxiliary copy already admitted by REPLAY-1.  It is not used
to enlarge the campaign repair of the defective one-dicritical inference.

The verdict column below is deliberately local.

- **REPLAYED-SOUND** means that the printed hypotheses and displayed cited
  identities give the asserted local implication, and the replay records the
  decisive substitution.
- **REPAIRED** means that the paper suppresses a finite calculation, uses an
  unmapped analogy, or has a correctable label/citation error, and this report
  supplies the missing calculation or exact relabelling.
- **GAP** means that no safe local replacement was found.

A local verdict does not erase an upstream dependency.  Thus a row typed
`REPAIRED | DEPENDS[...]` has its own omission filled but remains unusable in
the theorem until the named dependency is repaired.  This convention avoids
calling a correct Diophantine substitution “unsound” merely because its root
placement was imported, while also preventing that substitution from
promoting the theorem.

The two charged dependency tags retain exactly their REPLAY-1 meanings:

```text
DEPENDS[ROOT-U-LAST-CHAIN]
  = Corollary 3.8(b), p. 10: the last linear segment toward h^0 is not
    excluded from containing the root.

DEPENDS[ROOT-DELTA-G2-APPLICATION]
  = Lemma 3.15, pp. 14–15: the hypotheses needed to apply Lemmas 2.5–2.6
    to every selected vertex of delta(a~,g~2) were not established.
```

All tilded vertices and branches below are source objects.  Their untilded
images are target objects, and edge labels are determinants or covering
degrees only as explicitly declared.  A cv flag, a physical place, and a
covering series are never identified.  Positivity away from the root is used
only as a lower/sign statement, never as attainment.  No exit-price assertion
is made, so the FALLACY-v2 `charge_basis` line is inapplicable.

## 1. Shared replay interface and D–O I bindings

### 1.1 Determinant interface

For vertices (x,y) in a weighted tree (Gamma), the technical identity
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
| [4], (3) | canonical coefficient formula | invoked only at (widetilde g_1) or (widetilde g_2) after the vertex class and all branch data are fixed |
| [4], (4), (5) | local degree sum and Riemann–Hurwitz | already charged in the repaired Fig. 8 census |

The formulas used for the final canonical contradictions are REPLAY-1's
checked Lemmas 2.9–2.11.  To prevent the source's index reuse from doing
mathematical work, this report writes (D_i) for an essential-vertex degree
in (2.5), (2.6), (2.11), or (2.12), and reserves (d_i) for a figure label.
In particular, the (d_2=2) obtained in (7.11) is not the later canonical
(D_2=4).

### 1.2 The entry theorem versus technical imports

There are no new direct appeals in §§5–7 to “one dicritical is impossible.”
Every object in the second half nevertheless inherits the load-bearing entry
DO-I-2 from Proposition 1.2: two dicriticals with
((m,n)(\widetilde g_1)=(1,1)) and
((m,n)(\widetilde g_2)=(1,2)).  The charged binding is unchanged:

- the unique-dicritical all-(\mu=1) defect in D–O I is replaced only by the
  charged campaign Proposition 4.1;
- the separate unique-(\mu=2) exclusion and the remaining part-I inputs stay
  source-bound; Proposition 4.1 does not prove them;
- technical calls to [4], Lemmas 2–5 and formulas (2)–(8) receive no halo from
  Proposition 4.1.  They are checked at their own hypotheses in the ledgers
  below.

Thus every second-half row has a background dependency on DO-I-2, but the two
required `DEPENDS[...]` tags are reserved for the two actual first-half gaps.
This makes the final graph show separately (i) the entry trust boundary,
(ii) the root infections, and (iii) the locally repaired arithmetic.

## 2. Section 5: Fig. 11 classes 1a–1d

### 2.1 Fig. 12 set-up and the two assertions

The first suppressed enumeration is the sentence on p. 16 that
\(\widetilde L_\infty\) “corresponds to one of the diagrams in Fig. 12.”
Reading ports rather than visual edge coincidences gives twelve states: four
left-of-\(\widetilde a\) states, one state in which that package is absent at
\(\widetilde a\), two lower-port states, three subdivisions of the degree-two
right route, and two degree-one right-port states.  These are respectively the
twelve drawn rows; none identifies a source fork merely from a repeated edge
label.  This fills the finite port check.  **Verdict: REPAIRED.**

Equations (5.1)–(5.3) are direct determinant-transfer statements.  Put

\[
 x=\det(\widetilde a\widetilde g_2)_\infty.
\]

At \(\widetilde a\), (5.1), (5.2), and [4], (6) reduce all of Assertion
5.1 to the single identity

\[
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
“Both” in the last column abbreviates both required `DEPENDS[...]` tags.

| check | decisive replay | verdict | unresolved dependency |
|---|---|---|---|
| Lemma 5.3(1), p. 18 | (5.4) and the type-3 edge identity give \(\det L_h>0\); Lemma 2.12 then puts the root in exactly \((\widetilde h\widetilde g_1)\cup(\widetilde h\widetilde a)\cup(\widetilde a\widetilde g_2)\) | REPLAYED-SOUND | none |
| 5.3(2), root on \((\widetilde h\widetilde g_1)\) | after the two root lemmas make the opposite route linear/unit, (E) gives \(3\det L_a=1\) | REPLAYED-SOUND | Both |
| 5.3(3), root on \((\widetilde h\widetilde a)\) | if \(\det U=1\), Lemma 2.3 makes \(\widetilde h\) inessential; otherwise (2.12) has \(D_n=3\), all preceding \(\mu_i=4\), and \(\det\widetilde L_\infty=-1\), whereas it requires \(-17\) | REPLAYED-SOUND | Both |
| 5.3(4), root on \((\widetilde a\widetilde g_2)\) | in (2.6), \(D_p=3,\mu_p=1\), the earlier \(\mu_i=4\), later \(\mu_i=2\); hence it requires \(\det\widetilde L_\infty=-7\), not \(-1\) | REPLAYED-SOUND | Both |
| Lemma 5.4(1), p. 18 | positivity and Lemma 2.12 leave only the two branches at \(\widetilde a\) | REPLAYED-SOUND | none |
| 5.4(2), root on the \(\widetilde g_1\)-side | row 5 is the 5.3(2) port map; rows 6–7 give either a strictly negative right side in (E), or all \(\mu_i=1\) with determinant \(-1\), contradicting (2.11)'s \(-5\) | REPAIRED | Both |
| 5.4(3), root on the \(\widetilde g_2\)-side | the inessential case has all \(\mu_i=2\) and contradicts (2.5); in the essential case (2.6) gives \(D_1=\frac13\det U-4\), incompatible with \(D_1\in\{\det U,\frac13\det U,\det\widetilde L_a\}\) | REPLAYED-SOUND | Both |
| Lemma 5.5, p. 19 | the two root locations respectively invoke Lemmas 2.5–2.6 and Lemmas 2.3 plus Corollary 3.8; both contradict \(\det\widetilde D_h>1\) | REPLAYED-SOUND | Both |
| Lemma 5.6(1), pp. 19–20 | the last-nodal-vertex descent proves \((\widetilde v\widetilde h)\) linear; (5.5), (E), and Lemma 2.12 exclude \(\widetilde h\cup\operatorname{br}_{\widetilde h}(\widetilde a)\) | REPAIRED | Both |
| 5.6(2) | all canonical \(\mu_i=1\) and \(\det\widetilde L_\infty=-1\), contradicting (2.11) | REPLAYED-SOUND | Both |
| 5.6(3) | all canonical \(\mu_i=2\) and determinant \(-1\), contradicting (2.5)'s \(-5\) | REPLAYED-SOUND | Both |
| Lemma 5.7(1), pp. 20–21 | subtracting the two equations (5.7) and the two canonical equations gives \(d-1=-1\), hence the impossible \(d=0\) | REPLAYED-SOUND | Both |
| 5.7(2) | (2.6) with \(D_1=d,\mu_1=1\), later \(\mu_i=2\), and determinant \(-d\) has residual (4) | REPLAYED-SOUND | Both |
| 5.7(3) | (2.11) with \(D_1=\mu_1=d\), later \(\mu_i=1\), gives \(d(d-1)=4\), with no integer solution | REPLAYED-SOUND | Both |
| Lemma 5.8(1), p. 21 | all \(\mu_i=1\) and determinant \(-1\) contradict (2.11) | REPLAYED-SOUND | Both |
| 5.8(2) | the paper cites Lemma 2.7, but the stated contradiction is Lemma 2.8: \(\widetilde a\) is the unique nodal vertex of the root–\(\widetilde g_2\) path, so \(\det\operatorname{br}_{\widetilde a}(\widetilde v)<-1\), contradicting the linear branch determinant (3) | REPAIRED[5.8-2.7→2.8] | DEPENDS[ROOT-U-LAST-CHAIN] |

The port analogies in 5.4 and 5.6 preserve the target branch, endpoint index,
and root-facing route; they do not infer equality from a repeated numeral.
Consequently Lemmas 5.3–5.8 exhaust Fig. 12 locally and Lemma 5.9 follows.
**Local verdict for Lemma 5.9: REPAIRED.  The theorem status of class 1a is
GAP through Both.**

### 2.3 Claims 5.10–5.11 (classes 1b–1d)

For 1b–1c, determinant transfer gives (5.8), and every nodal vertex on
\((\widetilde b\widetilde a)\) has determinant four toward
\(\widetilde g_2\).  Lemma 2.12 and (E) repair the unstated branch check in
5.10(1).  In 5.10(2), the 1b route is Corollary 3.8 directly; on the 1c route,
Lemma 3.16 makes \((bh)\) and the lifted chain linear, Assertion 3.6 gives the
terminal unit, and Lemma 2.3 propagates it.  This explicitly maps the printed
analogy but still consumes Corollary 3.8(b).

Let (d=\det(\widetilde b\widetilde g_1)>0), keeping it distinct from the
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
excludes incidence of \(\widetilde g_1\) with a right arm and gives (5.9).
If \(\widetilde g_1\) is on a left arm, (5.B) sends the two possible root
routes exactly to rows 6–7 of Lemma 5.4; their (2.11)/(2.6) contradictions
are unchanged.  If \(\widetilde g_1\) is on the lower arm, (2.6) with
\(D_1=3,\mu_1=1\), later \(\mu_i=2\), and determinant \(-1\) has residual
(6); the other root route is the already displayed determinant contradiction
of 5.3(2).  This supplies both suppressed transfers.  **Lemma 5.11:
REPAIRED | Both.**

Accordingly §5 contains no new intrinsic GAP.  It does contain one corrected
lemma citation and several filled finite analogies.  Its four Fig. 11
conclusions 1a–1d all remain globally infected by each charged root gap.
