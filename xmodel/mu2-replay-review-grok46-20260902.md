# MU2-REPLAY-REVIEW — hostile gate of the part-I μ=2 soundness verdict

**Lane.** `MU2-REPLAY-REVIEW`. Charged producer:
`xmodel/do1-mu2-replay-sol56-20260901.md` (frozen SHA-256 below).
Authority: Domrina–Orevkov, *Математические заметки* 64:6 (1998),
847–862, repository PDF pages 1–16. English preprint is aid only.

**Headline.** All five charged items are **CONFIRMED**. The producer’s
`DO-I-MU2 = REPLAYED-SOUND (+ named local repairs)` survives. This
review licenses the part-I one-dicritical inheritance. It does not
license Domrina II’s unaudited later half, nor campaign-wide N=4
closure. No exit price is asserted; `charge_basis` is inapplicable.

## Verdict table

| # | Item | Verdict |
|---|---|---|
| (1) | `μ+corr=3` unique-dicritical exhaustiveness at degree four | **CONFIRMED** |
| (2) | Named repairs, independently replayed: Prop. 4, Cor. 5 gluing, Lem. 10 `δ(ab)>0`, Lem. 13 citation | **CONFIRMED** |
| (3) | μ=1-contamination of the (2,1) track | **CONFIRMED** (NONE) |
| (4) | (3,0) closure by campaign Cor. 3.8 vs Orevkov’s Remark | **CONFIRMED** |
| (5) | Part-I Theorem 1 as assembled = payload of part-II Prop. 1.2 | **CONFIRMED** |
| — | Producer’s `DO-I-MU2 = REPLAYED-SOUND (+ named local repairs)` | **CONFIRMED** |

---

## 0. Custody

Frozen charged input, hashed on this host before any reading:

```text
8607da5c6a963e459fb463125c1db83c4ee13743964f383919c95a5a300a3696  [frozen]/do1-mu2-replay-sol56-20260901.md
```

Match. Sources hashed on this host before reading:

```text
6883978d6c24165de932c548acb1dfabde0492c0d8614ea4eb8734f14023bf1b  refs/domrina_orevkov1999_mzm_four_sheeted_I_russian.pdf
6ca30d797810400ddfcddb5b92b046796b3fdda5c1fb8f0ba378511506bbfed3  refs/domrina_orevkov1999_mzm_four_sheeted_I_orevkov_preprint.pdf
```

Both match the charge. Secondary files, SHA-256 on this host after the charged input:

```text
f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db  refs/jc86.pdf
b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55  xmodel/b0-trivial-dicritical-proof-opus5-20260831.md
8ffc0a06edcf2be3908b1486da57e7d4a024973e679f9d25577cc281ef005320  xmodel/b0-proof-hostile-review-sol56-20260831.md
b838a2860c88d64d2a2162fd1a157e345db027bf4c7e95d2abae899dba9dc5de  xmodel/domrina-ii-replay1-sol56-20260901.md
0be24c5c6a9cc9423c3049c3402f2c98e44bac5f1c6018b3999989e0f32e5018  refs/domrina2000_izv64_four_sheeted_general_case.pdf
```

Russian pages were rasterized (`pdftoppm -png -r 200`) and read as
images. `pdftotext` on the Russian file emits Type-3 glyph salad; it
was not used as a source. English layout text was used only as a
locator. Numbering below is the published Russian numbering; English
preprint numbers appear in parentheses at first mention.

Rendered first page is volume 64, issue 6, December 1998, p. 847.
Theorem 1, p. 848: there is no four-sheeted locally invertible
polynomial map with one dicritical component.

Divergences re-checked against the producer, not taken from it:

1. Russian p. 852: order one is unbranched over \(\mathbb C^2\)
   **outside a finite set**. English p. 6 drops the qualifier.
2. Russian p. 849: \(C\) is linear iff \(\nu_\Gamma(a)\le 2\) for
   **every** \(a\in C\). English constrains only non-end vertices and
   can admit a nodal endpoint. Lemmas 6 and 13–15 use the published
   meaning. The readings agree on an open interval \((ab)\) (endpoints
   excluded by Definition 1); they diverge for
   \(\Delta\cap(\widetilde v\widetilde g)\), whose nearest node can be
   an endpoint of that intersection.
3. Published E (p. 853) is target-minimality with a possible root
   exception. The (2,1) track uses D+E as published.
4. `det L = det\widetilde L = -1` is Prop. 3(c) and
   `det Γ_L = det(-A_L)` (p. 849). English extraction drops leading
   minus signs (Lemma 10 after (14); Lemma 11). Rendered Russian
   controls.

Lemma 1 = edge formula (2); Lemma 2 = coprime branches; Lemma 3 =
root-unit; Lemma 4 = positivity off the root; Lemma 5 = transfer
(7)–(8). Empty graph: `det = 1` (p. 849).

---

## 1. Item (1) — `μ + corr = 3` exhaustiveness

**Verdict: CONFIRMED.**

Orevkov, *Math. USSR-Izv.* 29 (1987), Lemma 4.2 (`jc86.pdf` pp. 7–8,
displayed (4)):

\[
\sum_{l\subset L_F}
\Bigl(\mu_l f^*
+\sum_{x\in\pi(l)\setminus\{\infty\}}
(\mu_x f^*-\mu_l f^*)\Bigr)
= N-1.
\]

The inner summands are nonnegative by upper semicontinuity of
multiplicity (Orevkov’s own sentence after (4); Corollary 4.3). Write
`corr_l` for the inner sum. Then `corr_l ≥ 0` is a theorem of the
cited lemma, not a cap. Multiplicities are integers, and a dicritical
is nonconstant, so `μ_l ≥ 1`.

At topological degree four, \(N-1=3\). Under the unique-dicritical
hypothesis of part I there is a single summand, hence

\[
\mu+\mathrm{corr}=3,\qquad \mu\ge 1,\qquad \mathrm{corr}\ge 0.
\]

The integer solutions are exactly `(μ,corr) ∈ {(1,2),(2,1),(3,0)}`.
No fourth profile exists:

- `(0,3)` is not a dicritical (`μ=0`).
- `(4,-1)` and every `corr<0` row are forbidden by semicontinuity.
- A second dicritical would split the budget and leave the
  unique-dicritical theorem. Those rows are part II’s problem.

Campaign `n(\widetilde l)` is Orevkov’s `μ_l f^*` (generic transverse
local degree / collapsed multiplicity). Part I’s opening trichotomy
p. 852 — orders 1, 2, or 3, from `[3, лемма 4.2]` — is this same
bound `μ ≤ N-1`. The producer’s displayed (3.1) is the unique-`l`
specialisation, correctly quoted.

Żołądek 6.5(b) would force `corr=0` at `μ=1` and kill `(1,2)` a
second way. The producer instead uses campaign Prop. 4.1. That is
not a missed profile.

The `m(\widetilde g)=1` reconstruction is not item (1). Orevkov 4.2
does not mention `m`; the paper’s citation of `[3, лемма 4.2]` for
`(m,n)=(1,2)` is slightly abusive. Independently, `a+sμ=N` at unique
dicritical `μ=2` with `a≥1` gives `a+2m=4`, hence `(m,a)=(1,2)`
only. That does not enlarge the profile list.

---

## 2. Item (2) — named repairs, independently replayed

**Verdict: CONFIRMED.** Four named fills were replayed from the
published text, including the mandatory Corollary 5 gluing.

### 2.1 Proposition 4 (English 3.2), p. 854 — printed with no proof

Let \(\widetilde s\in\widetilde L_\infty\) be nodal, `r = ν(s)` in
`Γ_{L,g}` so `r≥3`, and let `k_i` be the number of points of
\(\widetilde s\) over the `i`-th incident direction of `s`. Keller
ramification of \(F|_{\widetilde s}:\mathbb P^1\to\mathbb P^1\) is
supported at those `r` points, so Riemann–Hurwitz is an equality:

\[
2(m-1)=\sum(e_p-1)=rm-\sum_i k_i,
\qquad
\sum_i k_i=(r-2)m+2.
\]

(a)⇒(b). Source valence equal to target valence means the dual graph
of \(\widetilde s\) has `r` edges, hence `r` distinct contacts, so
`∑ k_i = r`. Then `(r-2)(m-1)=0`. Nodal ⇒ `r≥3` ⇒ `m=1`.

(b)⇒(c). `m=1` makes \(F|_{\widetilde s}\) an isomorphism: one
unramified contact in every direction, incident-chain degree equal to
`n(\widetilde s)=Deg\widetilde s`, and valences equal.

(c)⇒(b). Every incident chain of degree `mn` forces every local index
equal to `m`, hence one point per fibre, hence `∑ k_i=r`, hence
`m=1`.

Printed equivalence (a)⇔(b)⇔(c). RH is an equality because the three
target fibres already represent every contact. **Prop. 4 fill:
CONFIRMED.**

### 2.2 Corollary 5 (English 3.10), p. 858 — quotient-tree gluing

Published “proof”: Lemmas 6, 8, 9 and Cor. 4 “give the proof.” That
is not a proof. The assembly is the repair. Orientation is the defect
class. Convention, p. 854 and Fig. 2: **Right** is the direction of
`g`; **Left** is toward the root; **Down** (crosses) maps beneath `l`
and is linear by published C/E. A degree-two arm from a fork to
\(\widetilde g\) is therefore a **Right** arm, never a down-cross.

Local survivors, from Lemmas 8–9 and Figs. 3–19 (pp. 855–857):

| Deg | printed type `L\|R\|D` | Russian figure | has a Right 2-arm? |
|---|---|---|---|
| 2 | `2\|11\|2` | Fig. 4 | no (Right is `1+1`) |
| 3 | `21\|21\|3` | Fig. 10 | yes |
| 3 | `3\|21\|21` | Fig. 11 | yes |
| 4 | `4\|211\|31` | Fig. 13 | yes |
| 4 | `31\|211\|4` | Fig. 14 | yes |
| 4 | `31\|31\|22` | Fig. 15 | no (Right is `3+1`) |
| 4 | `22\|31\|31` | Fig. 16 | no (Right is `3+1`) |

Corollary 4 kills every Deg-2 fork, so Fig. 4 cannot be the first
fork from \(\widetilde g\). Figs. 15–16 cannot host the first
\(\widetilde g\)-arm: their 2-packets are Down.

**Start.** Let `Δ` be the maximal constant-degree block incident at
\(\widetilde g\). Lemma 6 gives `Deg Δ = 2`. Nonfork vertices do not
merge maximal blocks. If the far end of `Δ` were an end of
\(\widetilde L_\infty\), the remaining two sheets would be a second
component of the branch \(\widetilde L_\infty\) at \(\widetilde g\)
(condition A, p. 852). Connectedness forces a first merge; maximality
makes it a fork `A`. Corollary 4 ⇒ `Deg A ∈ {3,4}`.

**`Deg A = 4`.** The Right 2-arm exists only in Figs. 13 and 14.
These are global Figs. 20 and 21. Lemma 9(a) ends every left arm.
Four-sheet identity (9) puts every sheet at this unique Deg-4 vertex,
so a further Right join repeats an already completed join and cycles.

**`Deg A = 3`.** Then `U_A` is Fig. 10 or Fig. 11. Identity (9) at
the same target leaves exactly one Deg-1 nonfork lift `A_0`, separate
until its first join with the `A`-component. That join is strictly
Left:

- a fork on the 2-packet closer to \(\widetilde g\) contradicts
  first-fork;
- a merge of only unit packets is a Deg-2 fork, Corollary 4;
- Down twigs are terminal (crosses, published C).

The join is a fork: a Deg-1 vertex preserves valence by Prop. 4, so
it cannot merge distinct maximal blocks.

*Fig. 11 first.* Left packet 3, companion `A_0` of degree 1. First
meeting is a Deg-4 fork with Right partition `3+1`, i.e. Fig. 15 or
16, giving global Figs. 22 and 23. Lemma 9(a) ends the new left arms.
A further Right join repeats the completed `A`–`A_0` identification
and cycles.

*Fig. 10 first.* Left packets `X=2`, `Y=1`, companion `Z=A_0=1`.

- A Deg-4 join of `X,Y,Z` reconnects `X,Y` already joined at `A`
  (cycle).
- A Deg-3 fork `B` taking `X` and `Y` makes two `A`–`B` routes
  (cycle).
- So `B` takes `X` and `Z`; unused `Y` is the new companion `B_0`.
  The arm from `B` toward `A` (hence toward `g`) is the 2-packet
  `X`, so `B` has a Right 2-arm, hence is Fig. 10 or 11.

If `B` is Fig. 11, the exposed 3-packet plus `B_0` can enter only a
Deg-4 fork of Right type `3+1`. That reconnects vertices already
joined through `A` (cycle). The completed graph with no further join
is Fig. 24.

If `B` is Fig. 10, exposed packets `X'=2`, `Y'=1`, companion
`Z'=B_0=1`. A Deg-4 of all three, or a Deg-3 of `X',Y'`, repeats two
strands from `B`. A Deg-3 of `X',Z'` reconnects `B` to `B_0` through
the preceding spine. Every continuation cycles. The completed graph
is Fig. 25.

No other first-fork type exists, and a Down-2 orientation toward
\(\widetilde g\) contradicts Fig. 2. The list is exactly Figs. 20–25,
the input of §§4–5. **Corollary 5 fill: CONFIRMED.** Right/Left/Down
are target directions of `Γ_{L,g}`; each source packet is counted
once as a first-separation from `A`.

### 2.3 Lemma 10, `δ(ab)>0`, pp. 858–859

The paper cancels `δ²` in (12) and in the identity after (14) without
stating `δ≠0`. If `δ=0`, that last identity becomes `-2d_2=-2d_2` and
there is no contradiction. The omitted premise is load-bearing.

`δ = det δ(ab)` is the off-path forest of the **target** path from
`a` to `b` (Definition 1, p. 849). Fig. 2 places the root strictly
Left of every nodal vertex on the spine of `g` near `L`. In Fig. 26
the path `a→b` runs Right, toward `g`. Then
`[ab]=\mathrm{br}_a(b)\cap\mathrm{br}_b(a)` does not contain the Left
(root) branch at `a`, so the root lies outside `δ(ab)`. Lemma 4 gives
`δ>0`; the empty-forest convention is 1. Either way `δ≠0`.

With that premise the rendered algebra is:

\[
\det\mathrm{br}_{\widetilde b_2}(\widetilde a_2)
=18\delta^2-2d_2,\qquad
y:=\det\mathrm{br}_{\widetilde b_2}(\widetilde a_1)
=\det\Delta+4d_3\delta^2>4,
\]

then `d_3=1` by Lemma 3 at \(\widetilde b_2\), then

\[
-2d_2=18\delta^2-2d_2-6y\delta^2.
\]

The leading minus is on the rendered p. 859; English drops it. Since
`δ>0` one gets `y=3`, contradicting `y>4`.

Fig. 25 is the Left/Down swap of packets `(3d_1,2)` at the left
target node. The product `6d_1` is invariant; the coefficient 18 is
`2·3·3` with one 3 still at `b`, hence invariant; two nonunit
branches at \(\widetilde a_2\) still force `d_1=1` by Lemma 3. Same
contradiction. **Lemma 10 `δ`-fill and Fig. 25 companion: CONFIRMED.**

### 2.4 Lemma 13 citation, p. 861

Case `d>1`. The paper: «из леммы 4 следует, что
`det br_{\widetilde v_1}(\widetilde g)=1`». Lemma 4 is positivity,
not unity. The correct lemma is Lemma 3 (root-unit). Independently:
`d>1` forbids \(\widetilde v_1\) from being the root (Lemma 3: every
root-branch has determinant 1). At a non-root vertex, at most one
branch is nonunit. The `d`-branch occupies that slot, so the
\(\widetilde g\)-branch is unit. The implication stands; the number
is wrong. **Citation repair: CONFIRMED.**

Lemma 7 is inequality (10), a conservation **lower** bound. A generic
disk at `c` misses image-points of `F`-constant components, so those
cannot swallow sheets. The producer uses (10) only as a floor.
Lemma 11’s Fig. 23 companion preserves the target product 6 and the
lifted product 3. Lemma 15’s Fig. 21 companion swaps the unsplit-4
and `3+1` roles; (19) is invariant, and the last edge identity uses
only the floors `B≥1`, `C≥3`.

---

## 3. Item (3) — μ=1-contamination of the (2,1) track

**Verdict: CONFIRMED (NONE).**

The defective inference is the order-one sentence on p. 852. Its
conclusion is “order one is impossible.” Campaign Prop. 4.1 replaces
that slice only. The (2,1) track begins at the next sentence
(`m,n)=(1,2)`) and runs through p. 862. Citation graph:

| Step | Cites | Uses the order-one covering, or “order one is impossible”? |
|---|---|---|
| Conditions A–E, pp. 852–853 | `[3]` only for unique \(\widetilde g\cap\widetilde L_\infty\) (A) | no |
| Prop. 3 | Abhyankar–Moh `[13,14]`, Neumann `[8]` | no |
| Lemma 6 | `n=2`, `m=1`, A, B, Prop. 1 | no; `m_{\widetilde p}(\widetilde g)=1` is the curve-map index at a point, not dicritical `μ=1` |
| Prop. 4 | RH at a nodal vertex of \(\widetilde L_\infty\) | no; `m(\widetilde s)=1` is a non-dicritical curve-map degree |
| Lemma 7 | sheet conservation | no |
| Lemmas 8–9, Cor. 4 | Lemmas 2, 5, 7, Prop. 3, (4)(5)(7)(8)(9) | no |
| Cor. 5 | Lemmas 6, 8, 9, Cor. 4 | no |
| Lemma 10 | Lemmas 3, 4, 5, (2)(6)(7) | no |
| Lemma 11 | Lemmas 2, 5, Prop. 2–3, (6) | no |
| Lemma 12 | `n(\widetilde g)-1=1` from the (2,1) entry | no; uses `n=2`, not the order-one *impossibility* |
| Lemmas 13–15 | Prop. 3–4, Lemmas 2, 3 (as repaired), 4, 12, (2)(3)(6)(7)(8) | no |

No later line invokes the order-one covering or its conclusion.
Deleting that paragraph and entering at `(m,n)=(1,2)` leaves
pp. 853–862 unchanged. Census forks with `n=1` are transverse
degrees of \(\widetilde L_\infty\) components, not dicriticals.
The entry citation `[3, лемма 4.2]` is Orevkov’s budget, not the
covering sentence. Prop. 4.1 is neither used nor needed in the
(2,1) track.

---

## 4. Item (4) — (3,0) closure versus campaign Corollary 3.8

**Verdict: CONFIRMED.** Scope match, not a near-miss.

Orevkov’s closing Remark (`jc86.pdf` p. 10), after the N=3 case-3
argument:

> Repeating the above arguments, one can prove the following
> assertion. If \(f\colon\mathbb C^2\to\mathbb C^2\) is a polynomial
> mapping satisfying condition (1), then the curve \(L_F\) cannot
> contain an irreducible component \(l\) such that
> \(\mu_l f^*=N-1\).

Campaign Corollary 3.8
(`xmodel/b0-trivial-dicritical-proof-opus5-20260831.md:312–316`):

> No component of \(L_F\) has \(\mu_l f^*=N-1\).
> *Proof.* If \(\mu_{l_1}=N-1\) then [O-4.2] forces every other term
> of the budget to vanish, so \(l_1\) is the only dicritical and
> \(\mathrm{corr}_{l_1}=0\); hence \(A_F\) is irreducible and
> \(\sum\mu_l=N-1\), contradicting Cor. 3.7.

The two **statements** are the same sentence. Part I cites the Remark
as `[3, замечание к лемме 5.3]` to kill ramification order 3
(p. 852). Unique dicritical of order 3 is `μ=3=N-1`, and the budget
forces `corr=0`. That is `(3,0)`.

Cor. 3.8’s **proof** applies: its first sentence produces
unique-dicritical, `corr=0`, irreducible `A_F` — part I’s (3,0) row,
not an extra hypothesis. Cor. 3.7 then wants Theorem 3.5(ii): every
`corr=0` and `2a≤N`. The fibre identity is `a+3s=4` with `s≥1`,
`a≥0`, hence `(s,a)=(1,1)` and `2a=2≤4`. Theorem 3.5 is for
noninvertible Keller maps of degree `N≥3` with `A_F` irreducible.
Part I is a degree-four Keller map; (3,0) supplies irreducibility.
The residual `OPEN[B0-N4-REDUCIBLE-PI1]` is the reducible-`A_F`
direction, which (3,0) never enters.

H2 is the title-decoration of Cor. 3.7. Cor. 3.8 does not assume H2;
it derives it. Promoted `a≥1` is unused on this row: `a=1` is forced
by `a+3s=4`. Lemma 3.1’s `Br≠∅` is immediate from `μ=3≥2`, without
the all-trivial half (Prop. 4.1, unused here).

The proof path differs from Orevkov’s “repeating” (AMS, then the
cyclic cover of \(\mathbb C^2\) minus a line, ramification `N`).
Cor. 3.8 uses Euler plus meridian cycle type. Different proofs of
the same statement; the Remark is covered, not under- or over-cut.
Independently confirmed at
`xmodel/b0-proof-hostile-review-sol56-20260831.md:246–249`. The
REFUTED gloss there (Cor. 3.7’s “locally irreducible singularity”)
is not consumed by Cor. 3.8.

---

## 5. Item (5) — Theorem 1 as assembled versus part-II Proposition 1.2

**Verdict: CONFIRMED.**

Part I Theorem 1 (p. 848) is the exclusion of **exactly one**
dicritical. Part II, Izv. Math. 64:1 (2000), Proposition 1.2(1)
(`refs/domrina2000_izv64_four_sheeted_general_case.pdf` p. 2):

> The number of dicritical components of \(F\) is greater than 1
> (see [4]).

That is the unique textual load-bearing use of part I’s exclusion
(charged replay-1 ledger DO-I-2). DO-I-1 in the Introduction is the
same statement as a scope gate. Later “[4], Lemma 2/3/5” citations
are determinant/canonical imports, not a second use of the
one-dicritical theorem.

Theorem 1 as assembled in the producer’s §8 is: `(1,2)` closed by
campaign Prop. 4.1; `(2,1)` closed by part I §§2–5 after the named
fills; `(3,0)` closed by campaign Cor. 3.8; zero dicriticals closed
by the classical proper/finite-étale argument. That is exactly the
payload `[4]` must supply for the sentence “greater than 1”.

Two precisions, neither a mismatch:

1. Theorem 1 as printed does not mention the zero-dicritical case.
   Part II’s `[4]` for `>1` silently includes “not zero”. The zero
   case is not in part I §2. It is classical: no dicritical ⇒
   `F(\widetilde L)\subset L` ⇒ proper on \(\mathbb C^2\) ⇒ finite
   étale of degree 4 over simply-connected \(\mathbb C^2\) ⇒ degree
   1. The producer names this extra lemma rather than folding it
   into Theorem 1. The statements then match.
2. Proposition 1.2’s **full** conclusion — two dicriticals with
   `(m,n)=(1,1)` and `(1,2)` — uses `[3], Lemma 4.2` plus a covering
   argument for the remaining all-`μ=1` multi-dicritical profiles.
   That is not a part-I consumption. The producer does not claim
   otherwise.

Items (1)–(4) close the three unique-dicritical profiles, so the
assembled Theorem 1 is the statement Proposition 1.2 cites `[4]` for.

---

## 6. Gate

The producer’s `DO-I-MU2 = REPLAYED-SOUND (+ named local repairs)`
is **CONFIRMED**. No `GAP-CANDIDATE[DO1-MU2-*]` is opened. The named
repairs are bounded fills of printed omissions and one wrong lemma
number; none imports the defective all-`μ=1` covering inference.
This review promotes only the part-I one-dicritical inheritance. It
does not promote Domrina II past the named first-half gaps, and it
does not promote campaign-wide closure.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20222`.
- Body SHA-256:
  `1ffa338d98647d2217681df9ae6a897d0bb1afbb28bd0c8686285527375b5810`.
- Frozen basis: `dbf941d3f3d85234d43302009434acbf55d9a326`.
