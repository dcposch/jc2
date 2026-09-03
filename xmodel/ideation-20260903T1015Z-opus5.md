# Ideation round 20260903T1015Z — blind submission, Opus 5

Charged input: `xmodel/ideation-20260903T1015Z-packet.md`
(sha256 `99c940d1167acfc7796436457a1d87bdd0a1a1a4c673c7bb2e0d3436e3d086b7`, verified).
Basis f5aa1caf. Blind: no 20260903T1015Z submission and no in-progress lane
report was read. **`refs/moh1983_jram340_configurations_of_roots.pdf` is NOT
present on this machine** (refs/ holds only arzhantsev_zaidenberg and chau2004);
every Moh page claim below is taken from the verbatim transcription in
`xmodel/census-rebase-opus5-20260902.md` §1 and is typed SOURCE-UNVERIFIED
where it goes beyond that transcription.

## Contents

0. Headline and the one-sentence answer
1. Q3 first: is skeleton realisability the right all-degree frame
2. Q1 — Moh's missing elimination, in uniform form
3. Q2 — the D = 105 trio
4. Q4 — software
5. NEW avenue
6. NEW cross-connection
7. Strongest proof attack / strongest counterexample attack
8. Reranked bottlenecks
9. Disposition vector — APPROACHES.md 46 rows (changes only)
10. Disposition vector — Q3 (a)–(f) and the queued fronts
11. Idea cards
12. Lane dispositions and the single first lane
13. Campaign-systems check
14. OPEN ledger raised by this submission

---

## 0. Headline — and the one-sentence answer

**I found a candidate for OPEN[MOH-PROGRAM] that meets the packet's own
discriminator exactly, keeps all six printed rows, and empties D = 105.**

It is a conjunction of three clauses, two of which are derivable from text the
campaign already holds verbatim, and one of which is not (and is the honest
OPEN):

```text
MOH-INCREMENT   A_j >= 2 for every j = 1..s-1      (the "increment" of (8) must increment)
NOT-ALL-(11)    some j in {2..s-1} satisfies (10)  (Moh's Prop 5.6 numerical shadow)
MAJOR-MULT      V_j >= 2 for every j = 2..s        (a major disc's selected factor is not simple)
```

MEASURED this session, one core, wall < 6 min, on `box/moh_skeleton_full.py`
(sha256 `d20bf0841a1ba2b2…`, unmodified; drivers under `/tmp`, reproduced below):

```text
FAIL-CLOSED CONTROL  all six of Moh's p.202 rows pass MOH-INCREMENT,
                     NOT-ALL-(11) and MAJOR-MULT.            6/6 KEPT.
DISCRIMINATOR (75,50)  (1)-(13) leaves 9 rows, M_2 in {5,10,40,55,60}.
                     After the three clauses: EXACTLY the two printed rows
                     M = (55,73), V_2 in {2,3}.   M_2 in {5,10,40,60} ALL DEAD.
                     This is the packet's named test, met to the row.
n <= 100, Moh's own space (K unrestricted):
    (1)-(13)                    658 rows / 63 classes      [Moh: 6 / 4]
  + MOH-INCREMENT               391
  + NOT-ALL-(11)                247 rows / 42 classes
  + V_2 >= 2       (MOH-3)       86 rows / 15 classes
  + V_j >= 2 all j (MOH-4)       51 rows / 13 classes
    MOH-4's 13 classes CONTAIN all four of Moh's printed classes.
Campaign space 48 <= D <= 200 (K >= 16), GROUPS:
    (1)-(13)  14,016   ->   MOH-3  2,652   ->   MOH-4  1,908
DEGREES EMPTIED that carried a (1)-(13) skeleton:
    MOH-3: 60, 63, 81, 88, 104, 105, 110, 152, 154
    MOH-4: 48, 60, 63, 81, 88, 104, 105, 110, 152, 154
```

**D = 105 EMPTIES.** All three groups of the packet's trio have `V_2 = 1`
(`m=70, M=[28,103], V_s=5`; `V_s=6`; `m=70, M=[40,103], V_s=4` — verified
individually), so MAJOR-MULT kills the trio outright and MOH-INCREMENT +
NOT-ALL-(11) kill the other 11 groups at that degree. D = 117 drops from 4
pinned-N groups to 1 (`m=78, M=[91,115], V_s=11, V_2=2, N=8`).

**The one-sentence answer to the round.** The all-degree program is *not*
realisability of an infinite census, and it is not the D = 105 trio: it is
**(i) recover the rest of Moh's sieve — 62–92 % of it is here and it is
arithmetic, not case-by-case — and (ii) attack the pair with the one exact
identity family indexed by a free integer `k` rather than by the degree, namely
`d/dx Σ_i f(x,τ_i)^k = J·k·[y^{n-1}](f^{k-1} mod (g-c_2))`, whose left side is
bounded by `k·N = O(k)` because the boundary pinned N to O(1), while its right
side is a Bezout object of size O(k·m).** That is the cofinal invariant Q3(a)
asks for; it exists, and it does not live on the census.

**Where the coordinator's framing is wrong.** Two places, both consequential:

1. *"The remaining program is arithmetic + realisability of an infinite
   census."* The census is a **superset of unknown slack** — the packet itself
   says so (658 vs 6). Treating it as the index set of the remaining program
   commits the campaign to realising objects that Moh already knew do not
   exist, and it prices lanes (a flagship seat on the D = 105 trio) against a
   target list that this submission shows is 5–7× too big and that does not
   contain D = 105 at all. **Recover the sieve before you realise anything.**
2. *"Nothing on the boundary bounds D"* is true and promoted, but it is being
   read as "no O(1) quantity can bound a D-growing quantity". PIN-NOT-CEILING
   says the *boundary* cannot; it says nothing about the *interpolation*
   identity, where N appears as a growth-rate bound on an object (the power-sum
   trace) whose natural size is O(m). PIN-NOT-CEILING is being over-applied.

Everything below is MEASURED or typed. No ledger was edited.

---

## 1. Q1 — Moh's missing elimination, in uniform form

### 1.1 The mechanism, derived

**(A) MOH-INCREMENT: `A_j >= 2`.** Moh's (8), as transcribed in
`census-rebase-opus5-20260902.md` §1.2, defines `A_{r-1}` as *"the **increment**
of the denominator ... the reduced denominator of `L δ_{r-1}`"*, and (10)/(11)
are justified by *"the existence of the following automorphism of `k⟪t̄⟫` over
`k⟪t̄^{A_{r-1}}⟫`, `t̄ → ω t̄`, where `ω` is an `A_{r-1}`-th root of unity"*.
When `A_{r-1} = 1` that automorphism is the **identity**, the Galois argument is
vacuous, and (10)/(11) are both automatically satisfied (`△ = Q`, `□ = 0`). A
tower level whose "increment" is 1 adds no new ramification over the levels
above it, i.e. `δ_{r-1}` is not a characteristic exponent relative to
`δ_s,…,δ_r` — which contradicts its being a genuine new level of the
characteristic tower.

At the bottom level this is not an interpretation but a **theorem about the
printed text**. Moh p.188 (§1.3 of the transcription) derives (12)/(13) from

> *`A | n*V_2` and `A ∤ m*V_2`  or  `A ∤ n*V_2` and `A | m*V_2`*

— an **exclusive** disjunction. The implementation `cond1213` encodes the two
printed conjunctions (12)/(13), which are both *vacuously true* when `A_1 = 1`,
whereas Moh's own derived disjunction is *false* when `A_1 = 1` (`A_1` then
divides both). For `A_1 ≥ 2` the two readings coincide (if `A_1 | n*V_2` and
`A_1 | m*V_2` then `A_1 | (n*+m*)V_2` and Moh's p.188 identity
`A_1 | (n*+m*)V_2 - 1` forces `A_1 | 1`). **So `A_1 ≥ 2` is exactly the
strengthening of `cond1213` from the printed conjunctions to Moh's own derived
disjunction, and it is recoverable from material the campaign already holds.**
This is PROVED-HERE from the transcription; only the extension to `j ≥ 2` is
by analogy with the same automorphism sentence, and is typed CONJECTURE.

Measured incidence: `A_1 = 1` on **200 of the 658** rows (30.4 %); `A_2 = 1` on
11; `A_3 = 1` on 56; `A_4 = 1` on 25. The clause is doing real work at the
bottom, which is where Moh's own derivation lives.

**(B) NOT-ALL-(11).** Already `OPEN[PROP-5.6-SHADOW]` in the ledger (bounded 220
groups at `D ≤ 120`). I am *raising* it from "measured shadow, not folded in" to
"component of the missing sieve": on Moh's own `n ≤ 100` space it alone cuts
658 → 469, and in conjunction with (A) 658 → 247. Its status as a *necessary*
condition is exactly Moh's Prop 5.6 (both alternatives contradict search
condition (3)); the residual gap is only the `r = 2` branch datum, which
(12)/(13) does not expose — and that gap **narrows** under (A), because `A_1 ≥ 2`
is precisely the condition under which the `r = 2` branch is determined
(exactly one of (12), (13) can hold).

**(C) MAJOR-MULT: `V_j >= 2`.** This is the clause I cannot derive, and it is
the one that kills the D = 105 trio, so I flag it loudly. The reading: by the
census-rebase mechanism paragraph, `V_{r-1}` is the **multiplicity** of the
factor of `p(π)` that selects the next disc down. `V_{r-1} = 1` means that
factor is *simple*, i.e. the disc `D_{r-1}` is selected by a single root of the
bottom polynomial. In the Abhyankar–Moh "configurations of roots" vocabulary a
**major** disc is one at which roots genuinely split; a disc carrying a simple
factor is a *minor* disc. If Moh's Definition 5.1 or the minor-disc clauses of
the Theorem on p.200 (4)–(7) contain that requirement — which is exactly what
his `d_s ≥ 4` (Corollary 6.1) and the Props 6.1–6.4 minor-branch machinery are
about — then MAJOR-MULT is his, not mine. **SOURCE-UNVERIFIED: I cannot see
pp. 179 or 200; the census-rebase lane read p.200 (4)–(7) as reducing to the
lower half of (7) and therefore adding nothing, which is evidence against my
reading and must be re-checked by the second reader with this specific question
in hand.**

`OPEN[MAJOR-MULT]` — bounded quantity: **161 rows at `n ≤ 100`** (247 → 86
under `V_2 ≥ 2`; a further 35 under `V_j ≥ 2` for all `j`), and **744 groups at
`48 ≤ D ≤ 200`** (2,652 → 1,908), including the entire D = 105 trio.

### 1.2 Variants tested and rejected (fail-closed, on the census)

| variant added on top of MOH-INCREMENT ∧ NOT-ALL-(11) | keeps 6/6 | meets (75,50) discriminator | rows n≤100 |
|---|---|---|---|
| `V_2 ≥ 2`                       | **yes** | **yes** | 86 |
| `V_j ≥ 2` all `j`               | **yes** | **yes** | 51 |
| `A_1 ≤ e`                       | yes | no (keeps `M_2 = 40`) | 247 (automatic) |
| `A_1 ≥ 3`                       | **no** | no | 143 |
| `e V_2 ≥ A_1 V_2 + 1`           | **no** | no | 178 |
| `u_s = 1`                       | **no** | no | 196 |
| `q ≥ 1/2`                       | **no** | no | 184 |
| `d_{s+1} = 1`                   | **no** | no | 84 |
| `V_2 ≥ 2` **or** `s ≥ 4`        | yes | yes | 176 |
| shifted (7): `V_2 > d_1/(n-M_2)`| **no** (kills (64,48)) | — | — |

Two survive both gates, and one implies the other. Note `A_1 ≤ e` is
**automatic** on the MOH-INCREMENT ∧ NOT-ALL-(11) space (247 → 247) — a free
structural fact worth banking: *the bottom increment never exceeds `e = n/K`.*

### 1.3 What its all-degree form is — the direct answer

**It is an arithmetic sieve that leaves an infinite family, not a theorem that
empties every D.** MEASURED: under MOH-4, `D = 108` keeps 28 groups, `D = 120`
keeps 127, `D = 144` keeps 273, `D = 180` keeps 538, `D = 192` keeps 540; the
survivor count grows with the divisor structure of `D` exactly as the raw census
does. The emptied degrees (48, 60, 63, 81, 88, 104, 105, 110, 152, 154) are all
*divisor-poor*. **So: recovering Moh's sieve in full will NOT prove JC2.** It
will do three other things, each worth a lane:

1. it makes the counterexample-side **target list** 5–7× smaller and, crucially,
   *different* (D = 105 leaves it; D = 108 and D = 120 remain);
2. it removes the campaign's dependence on an unrecovered filter, which is
   currently a soundness hole in every emptiness statement;
3. it tells us *what kind* of datum Moh's endgame (Appendix II) uses, which is
   the only evidence we have about the shape of a uniform theorem.

Corollary for the mission: **the uniform mechanism must use a datum that is not
in the skeleton at all.** That is Q3(f), and I answer it YES below.

### 1.4 The cheapest test on the census (already run)

`python3 -c "import sys;sys.path.insert(0,'box');import moh_skeleton_full as M; …"`
with the three predicates as one-liners over `M.census(n, Kmin=1, full=True)`.
Whole `n ≤ 100` sweep: 90 s. Whole `48 ≤ D ≤ 200` sweep: 5 min, one core,
< 200 MB. Drivers: `/tmp/id-opus5/{incr,casc,alldeg,battery,moh4}.py` — these
should be banked as `box/mohsieve-drivers-20260903/` by the coordinator; I did
not write into `box/` (no ledger edits from an ideation lane).

---

## 2. Q3 — is skeleton realisability the right all-degree frame? NO. Here is the frame.

### 2.1 The reframe, stated plainly

The boundary computes `N` exactly and `N = O(1)`. The campaign has read that as
"the boundary is exhausted; everything left is the census". The correct reading
is the opposite: **an O(1) invariant that is exactly computable is a *bound*
looking for a quantity that grows.** The census is not that quantity — it is an
index set. The quantity is the **order of growth in `x` of the traces of powers
of `f` along the fibre of `g`**, and `N` bounds it *linearly in `k`, uniformly
in `D`*.

Precisely (PROVED-HERE, §5.1, with a three-pair CAS control):

```text
P_k(x) := Σ_{i=1..n} f(x, τ_i(x))^k        (τ_i the roots of g - c_2)
P_k ∈ k[x, c_2]                            (it is a Newton power sum of a char. poly)
(PS-1)   d/dx P_k = J · k · [y^{n-1}]( f^{k-1} mod (g - c_2) )
(PS-2)   deg_x P_k ≤ k · max_i (1 - δ⁰_i)⁺ ≤ k · N          [by DICT-N / FRONTIER-EXACT]
(PS-3)   hence  deg_x [y^{n-1}]( f^{k-1} mod (g - c_2) ) ≤ k·N - 1  for every k ≥ 1.
```

`N ≤ 16` on the frontier. The right-hand object in (PS-3) is a Bezout/Grothendieck
residue whose *generic* `x`-degree is `Θ(k·m)`. **So the Jacobian condition plus
the boundary forces a family of residues, indexed by a free integer `k` and
independent of the skeleton, to be `O(k)` when they ought to be `O(km)`.** This
is a cofinal invariant that grows with `D` and is bounded by `N` — exactly what
Q3(a) asks for, obtained without D-modules, without Picard–Fuchs, and without
leaving polynomial algebra.

### 2.2 Why this is the right frame and realisability is not

It is **degree-free** (one identity family, not one job per skeleton, where
realisability is `Θ(#groups)` and `#groups → ∞`); **two-sided** (a violation is
a proof step, a witness is a counterexample seed); it **consumes** the promoted
result rather than being blocked by it (D1-PIN and FRONTIER-EXACT enter only
through `N ≤ 16`, read off the frontier line, never re-derived); it has cheap
negative controls (run on automorphisms — done, 10 instances, 0 failures — and
on non-Keller pairs, where (PS-1) must fail); and it **sidesteps
`OPEN[MOH-PROGRAM]` entirely**, which is the point.

### 2.3 Disposition of the coordinator's candidates (a)–(f)

| | candidate | disposition | reason |
|---|---|---|---|
| (a) | one differential operator / D-module / Picard–Fuchs; cofinal invariant bounded by N | **RAISE — but in the elementary form** | The instinct is right and it is the round's best idea. The *implementation* should not be `D`-modules: row 20 (p-curvature) is already run and identically zero, and irregularity/exponents at infinity of the pencil are exactly the tree data we already have, so they cannot be *new*. Replace by PS-GROWTH (§2.1): same content, polynomial algebra, desk-scale controls. |
| (b) | dessin tower / Galois orbit rigidity forcing k = 1 or bounding V_2 | **RAISE to second place** | STAR-ABC + TF-DESSIN make this well-posed and the passport is explicit: `[e^{dV}]`, `[d^{eV}]`, `[(d+e)V-1, 1^γ]`, `γ = V(de-d-e)+1`. And it now has a *specific* client: MAJOR-MULT says `V ≥ 2`, so the `V = 1` Davenport–Stothers pairs (the ones that always exist) are the ones we need to exclude — this is the cheapest possible test of my own conjecture. |
| (c) | characteristic p / Cartier | **LOWER, retype as diagnostic** | The 1608Z synthesis already banked that row 20 was run and the canonical connection has identically zero p-curvature. Cartier on the *interpolant* is not obviously the same object, but it needs a 10-line class before a seat. Keep as a receiver. |
| (d) | Abhyankar–Moh semigroup / conductor / approximate roots as the missing filter | **RAISE — and it is now testable** | This was the census-rebase lane's own probe (ii) and it is my clause (C)'s most likely provenance: MAJOR-MULT is exactly the kind of statement a semigroup/major-disc definition supplies. Cheapest test: ask the second reader ONE question (below) instead of re-deriving the literature. |
| (e) | counterexample-side numerical solve at a D = 105 / D = 108 survivor | **LOWER as posed; REAIM** | D = 105 is now (conjecturally) empty and its trio is `V_2 = 1` throughout. Re-aim at a MOH-4 survivor at `D = 108` or `D = 120` with `V_2 ≥ 2`, and only after the Sol framework lands. Also: the Sol review already refuted the resonance set and the order-2 recurrence of the previous attempt — a numerical solve without the corrected exponent semigroup will produce another artefact. |
| (f) | a theorem that the census never empties | **RAISE — and I assert it, measured** | MEASURED here: under the strongest sieve I can justify, survivors grow with the divisor structure of D through `D = 200` and no tail of degrees empties. **The census will not empty.** Therefore a uniform theorem must use a datum outside the skeleton — which is precisely what PS-GROWTH is. This is the most important disposition in this table: it converts (f) from a question into a design constraint. |

### 2.4 The single question for the second reader of Moh

If the coordinator gets the page images and one Sol/Grok seat, do **not** ask
for a general re-reading. Ask exactly this, in this order:

1. **p.179, Theorem/Definition 5.1:** in the definition of a *major* disc, and
   in the assignment `{V_i : i = r+1,…,s+1}`, is there any requirement that
   `V_i ≥ 2`, or that the selected factor of `p(π)` be non-simple, or that a
   disc containing a single root be *minor*? (This decides `OPEN[MAJOR-MULT]`.)
2. **p.188 l.1–13 and p.201 (12)/(13):** confirm that Moh's derived condition is
   the *exclusive* disjunction, so that `A_1 = 1` is inadmissible.
   (This decides MOH-INCREMENT at `j = 1`, PROVED-HERE from the transcription
   but worth one line of confirmation.)
3. **Appendix II:** for each of the six rows, what datum does the case analysis
   use that is not in `{n, m, M_*, V_*}`? One word per row is enough. This is
   the only direct evidence about the shape of a uniform theorem.

Everything else about pp.200–202 the census-rebase lane already recovered.

---

## 3. Q2 — the D = 105 trio: neither realise nor kill. Do not spend a seat.

### 3.1 The finding

All three groups have `V_2 = 1`:

```text
m=70 M=[28,103] V_s=5  V={2:1, 3:5}  A=[A_1,A_2]=[2,18]  any10=True  q=1/2
m=70 M=[28,103] V_s=6  V={2:1, 3:6}  A=[2,13]            any10=True  q=9/13
m=70 M=[40,103] V_s=4  V={2:1, 3:4}  A=[2,17]            any10=True  q=9/17
```

They pass MOH-INCREMENT and NOT-ALL-(11) and die on MAJOR-MULT alone. The other
11 D = 105 groups die on MOH-INCREMENT (`A_1 = 1`: 4 groups) or NOT-ALL-(11)
(6 groups) or both. So `D = 105` is empty under MOH-3/MOH-4 and the trio's
status is **entirely hostage to `OPEN[MAJOR-MULT]`** — a question answerable by
one page-image lookup at essentially zero cost.

### 3.2 The cheapest exact discriminator (if the trio survives the lookup)

Not the global interpolation system. Use the bottom dessin, because `V_2 = 1`
makes it maximally rigid:

- `(d,e) = (2,3)`, `V_2 = 1` ⟹ `deg p_f = 2`, `deg p_g = 3`, and BOTTOM-ODE
  `2 p_f p_g' − 3 p_g p_f' = κ`. By STAR-ABC the pair is the **unique**
  Davenport–Stothers pair of type (2,3) up to the affine/scalar normalisation —
  Sol's review pins it: `p_g = π³ − π`, `p_f = π² − 2/3`. There is **one orbit**.
- Therefore *all* bottom discs of a `D = 105` trio realisation carry the *same*
  normalised star, and the only freedom is the `k` gluing constants and the
  outer-root data. `Σ_B V_2(B) = Σ_B 1 = k ≤ u`, and `N = k·q`. For the three
  groups: `q = 1/2, 9/13, 9/17` and `u = 25, 30, 28`, so `k ∈ {12,…,24}`,
  `k = 13`, `k = 17` respectively — the second and third are **rigid in `k`**.
- **The discriminator: `k` bottom discs all carrying the identical (2,3) star
  must be a single Galois orbit** (they are the conjugate bottom branches of one
  pair defined over `Q̄`). A Galois orbit of size 13 or 17 of a rigid dessin,
  glued through a Puiseux tower with `A_1 = 2`, is an extremely thin object: the
  field of moduli of the (2,3) DS pair is `Q`, so the orbit is *not* generated by
  the dessin — it must come from the gluing constants, whose number is exactly
  `k` (one `a_i` per branch) minus the `n − m = 35` degree-killing relations.
  Counting: `13 < 35` and `17 < 35`. **First order at which a kill by counting
  is possible: order 0.** The `k` gluing constants cannot absorb 35 relations
  unless the outer-root data supplies at least `35 − k` further unknowns, and
  those are prescribed by the tree, not free.

This count is *cheaper* than the global interpolation system — no exponent
semigroup needed, just a dimension count on the star orbit against the
polynomiality relations — but it is exactly the object Sol's review says the
previous flagship mishandled (inner unknowns counted without separating
prescribed outer data), so the outer/inner split must be **declared first**.

### 3.3 What a kill of the trio buys, plainly

**`D_min ≥ 108`. That is all.** It does not narrow the frontier (108 has 76
pinned-N groups under (1)–(13), 28 groups under MOH-4), it does not generalise
(the trio is `V_2 = 1`, `(d,e) = (2,3)`, `s = 3` — the thinnest case in the
census), and its method (a rigid single-orbit star) does not transfer to `V_2 ≥ 2`
where the DS moduli are positive-dimensional.

**Verdict: the trio is NOT worth a flagship seat.** It is worth exactly one page
lookup. If MAJOR-MULT is Moh's, the trio is dead for free and the seat is saved;
if it is not, the trio is still a `D_min` increment of 3, which is worth a
background lane at most. I would spend the seat on §5 instead.

---

## 4. Q4 — software: the smallest instrument worth building this week

**Do not build the order-by-order Puiseux engine first.** The Sol review
established that the exponent semigroup is unknown, the outer-root degrees were
omitted, and the resonance set was wrong — an engine built now would be
calibrated against an object that does not exist yet, and its "pass" would be
vacuous in exactly the way Q4 asks us to guard against. Build these two instead.

### 4.1 `mohsieve.py` — the sieve harness (half a day)

A thin layer over `box/moh_skeleton_full.py` that takes a **predicate registry**
(each entry: name, source type `PRINTED | DERIVED | CONJECTURE | SOURCE-UNVERIFIED`,
lambda) and reports, for any conjunction:

```text
gates:  (G1) all six p.202 rows survive           [HARD, fail-closed]
        (G2) the (75,50) residue is exactly {M_2 = 55, V_2 ∈ {2,3}}
        (G3) row/class counts at n ≤ 100 vs Moh's 6/4
        (G4) group counts and emptied degrees over 48 ≤ D ≤ 200
        (G5) the pinned-N knapsack downstream of the sieve
negative control: the EMPTY conjunction must reproduce 658/63 exactly, and
        each single predicate must be reported with its solo kill count, so a
        predicate that kills nothing is visible as such (this is what catches a
        vacuous pass: a "filter" whose solo count equals the base count).
```

Cost: the whole `D ≤ 200` sweep is 5 min on one core, so the harness is
interactive. It turns `OPEN[MOH-PROGRAM]` from an essay into a leaderboard, and
it is the instrument that made this submission's finding possible in 20 minutes.

### 4.2 `psgrowth.py` — the PS-GROWTH checker (one day)

Given a candidate pair (or a genuine Keller pair for control), compute
`P_k(x, c_2)` from `Res_y(g − c_2, T − f)` by Newton's identities and check
(PS-1) and (PS-3) for `k = 1..K`. Gates:

```text
positive control: automorphisms in Moh's gauge at n = 2,3,4 — (PS-1) exact.
                  [DONE this session: 3 pairs, 10 instances, 0 failures]
negative control: a NON-Keller pair with J non-constant must FAIL (PS-1);
                  and a Keller pair must fail (PS-3) if N is understated.
vacuity guard:    report deg_x P_k as a function of k and fit the slope; a
                  slope of 0 for all k means the pair is degenerate in the
                  gauge, not that the bound bites — refuse to report a pass.
```

Why this and not the Puiseux engine: it needs **no** Puiseux data, no exponent
semigroup, no resonance analysis, and its arithmetic is exact over `Q`. It is the
only instrument in the campaign that can be pointed at an actual candidate pair
rather than at a skeleton.

### 4.3 The decisive experiment (if only one runs)

Run `psgrowth.py` in *reverse*: for the `(d,e) = (2,3)` bottom star and the
tree of a MOH-4 survivor at `D = 108`, compute the **predicted** `deg_x P_k`
from the tree via (PS-2) and compare with the **Bezout-generic** degree of
`[y^{n-1}](f^{k-1} mod (g − c_2))`. If the gap is already positive at small `k`
for every survivor, the sieve is unnecessary and JC2 follows from PS-GROWTH plus
one degree lemma. If the gap only opens at `k ≈ m`, the mechanism is real but
needs the resultant lower bound (§5.2). Either outcome is decisive about where
the next month goes. Cost: hours, exact, desk scale.

---

## 5. The genuinely NEW avenue — PS-GROWTH

### 5.1 Statement and proof of the identity (PROVED-HERE, CAS-controlled)

Let `(f,g)` be a Keller pair in Moh's gauge, `deg_y g = n`, `deg_y f = m < n`,
`g − c_2` monic in `y` with `n` distinct roots `τ_1,…,τ_n` over `k(x)` (generic
`c_2`). Let `J = f_x g_y − f_y g_x ∈ k*`.

**(PS-0) `P_k(x,c_2) := Σ_i f(x,τ_i)^k` is a polynomial in `x` and `c_2`.**
Immediate: `P_k` is the `k`-th Newton power sum of the roots of the
characteristic polynomial `Res_y(g − c_2, T − f) ∈ k[x,c_2][T]`, which is monic
in `T` of degree `n` with polynomial coefficients.

**(PS-1) `dP_k/dx = J·k·[y^{n-1}]( f^{k-1} mod (g − c_2) )`.**
Proof. JAC-FIBRE gives `d/dx f(x,τ_i) = J/g_y(x,τ_i)`, so
`dP_k/dx = k·J·Σ_i f(x,τ_i)^{k-1}/g_y(x,τ_i)`. For any `h ∈ k(x)[y]` with
`deg_y h ≤ n−1`, the classical Lagrange/Euler identity gives
`Σ_i h(τ_i)/g_y(τ_i) = [y^{n-1}] h` (both sides are linear in `h` and agree on
the basis of Lagrange interpolants). Apply it to `h = f^{k-1} mod (g − c_2)`,
which has `deg_y ≤ n−1` and the same values at the `τ_i`. ∎

**Control (run this session, `/tmp/id-opus5/resdeg2.py`, sympy, exact):**
three Keller pairs (`f=y, g=x+y²`; `f=y+x³, g=x+f²`; `f=y, g=x+y³+y²`),
`k = 2,3,4`, **10 instances, 0 failures**, sign carried by `J` exactly as
stated. `P_1 = Tr(f)` came out constant in `x` in all three (0, 0, −1), which is
the `k = 1` case (`[y^{n-1}] 1 = 0` for `n ≥ 2`) — a free corollary worth its own
name: **TRACE-CONSTANT: `Σ_i f(x,τ_i)` is independent of `x`.**

**(PS-2) `deg_x P_k ≤ k·N`.** By DICT-N (promoted), the order of `f` along the
branch `τ_i` is exactly `1 − δ⁰_i`, and `N = Σ_i (1 − δ⁰_i)⁺`. Each term of
`P_k` has `x`-order `k(1 − δ⁰_i)`, so
`deg_x P_k ≤ k·max_i (1 − δ⁰_i)⁺ ≤ k·Σ_i (1 − δ⁰_i)⁺ = k·N`. ∎
(The inequality `max ≤ Σ` uses only that every term of the sum defining `N` is
`≥ 0`, which is how `N` is defined. No attainment is claimed — this is a floor
on nothing and a ceiling on `deg_x P_k`, which is the direction we need.)

**(PS-3) Consequence.** `deg_x [y^{n-1}]( f^{k-1} mod (g − c_2) ) ≤ k·N − 1`
for every `k ≥ 1`, with `N ≤ 16` on the frontier.

### 5.2 Why this can bound `D`, when the boundary cannot

PIN-NOT-CEILING says no *boundary* functional bounds `D`. (PS-3) is not one:
it constrains the **reduction of `f^{k-1}` mod `(g − c_2)`**, whose size is
governed by `m, n`, not by the tree. Its generic `x`-degree is `Θ(k·m)`; (PS-3)
caps it at `O(k)`. Two ways to close:

- **(P-a) Resultant route.** `Π_i f(x,τ_i) = ± Res_y(g − c_2, f)/lc`, hence
  `deg_x Res_y(g − c_2, f) = Σ_i (1 − δ⁰_i) = N − Σ_i (1 − δ⁰_i)⁻`. The left
  side is a Newton-polygon quantity of the *supports* of `f` and `g`; the right
  side is tree data. If a lower bound `deg_x Res_y(g − c_2, f) ≥ φ(D)` with
  `φ → ∞` can be extracted from the Keller normalisation (it is a Bezout number
  minus intersection multiplicity at infinity), then `N ≥ φ(D)`, and `N ≤ 16`
  gives `D ≤ C`. **This is a ceiling route that PIN-NOT-CEILING does not
  forbid**, because it prices the *shed* term `Σ (1 − δ⁰_i)⁻`, which is not a
  boundary functional either.
- **(P-b) Growth route.** Fix `k` and let `D → ∞` along MOH-4 survivors; if the
  residue `[y^{n-1}](f^{k-1} mod (g − c_2))` can be shown to have `x`-degree
  `≥ c·k·m/n` for some `c > 0` on any Keller pair, (PS-3) closes at
  `k = 1` already (`c·m/n ≤ N − 1`), i.e. it bounds `m/n`, not `D`. So (P-b)
  alone gives a *shape* constraint, not a ceiling — still useful, and much
  cheaper to test.

### 5.3 Stop condition and honest risk

The risk is that (PS-3) is **automatically satisfied** — the residue vanishing
identically for all `k` on a Keller pair. That would be a clean theorem (the
plane case of "image conjecture" style vanishing) and would kill the route.
Measured against it: in the three controls the residue was *non-zero* at `k = 2`
and `k = 4` (values `2`, `4c − 4x`, `3`, `−4`). `OPEN[PS-VACUITY]` — bounded
quantity: the finite set `k ≤ 20`, `n ≤ 6`; one CAS run.

---

## 6. New cross-connection — RES-DEGREE joins Moh's tree to the GGV Newton polygon

`deg_x Res_y(g − c_2, f) = Σ_i (1 − δ⁰_i)` (§5.2) is an **equation between the
two halves of the campaign that have never been connected**:

- the left side is computable from the **supports/Newton polygons** of `f` and
  `g` — APPROACHES row 1 (GGV corner families), row 2 (boundary trees), and the
  whole degree-farm apparatus;
- the right side is `N` minus the *shed* part `Σ_i (1 − δ⁰_i)⁻`, i.e. Moh's
  tree data — rows 6, and integrations #14–#17.

Verified on control: `f = y, g = x + y²`, `Res_y = x − c_2`, `deg_x = 1`; the two
branches `τ_± = ±√(c_2 − x)` give `f(x,τ_i)` of `x`-order `1/2` each, sum `1`. ✓

Three immediate consequences worth a lane:

1. **It gives the first exact meaning to "denominator shedding" in the FALLACY
   list.** The shed term is `Σ_i (1 − δ⁰_i)⁻` and it is exactly
   `N − deg_x Res_y(g − c_2, f)` — a computable number, not a bookkeeping
   convention. Any future charge that separates strict-below from at-level
   parting can now be audited against it.
2. **ORTHO-DEFECT gets a second reading.** `2deN = Σ_ν (e m_ν − d m'_ν)²` prices
   `N` on the base-point cluster; RES-DEGREE prices `N − shed` on the resultant.
   Subtracting gives an identity for the shed part purely in terms of the
   cluster — a new constraint on which infinitely-near points may be
   non-proportional. That is a **kill test for skeletons** that needs no
   realisation and no interpolation.
3. **It reopens row 1 as a receiver rather than a route.** GGV's corner-family
   machinery computes exactly `deg_x Res`; it has been treated as a dead
   enumeration route, but as a *computer of the left side of RES-DEGREE* it
   is live and cheap.

`OPEN[RES-SHED]` — bounded quantity: the shed value `Σ_i (1 − δ⁰_i)⁻` is
unknown for each of the **1,908 MOH-4 groups at `48 ≤ D ≤ 200`** (and for each
of the 14,016 under (1)–(13) if MOH-4 is not adopted).

---

## 7. Strongest attacks

### 7.1 Strongest proof attack

**PS-GROWTH + RES-DEGREE, in that order.** Concretely:

1. Prove (PS-1)–(PS-3) as stated (they are proved here; they need a
   different-model review, not new work).
2. Establish the **residue non-vanishing lemma**: on a Keller pair in Moh's
   gauge with `m < n`, `[y^{n-1}](f^{k-1} mod (g − c_2))` is not identically zero
   for infinitely many `k`. (Evidence: three controls, non-zero at `k = 2,4`.)
3. Establish a **lower bound** for the `x`-degree of that residue in terms of
   `m, n` on any Keller pair — the one genuinely new theorem needed. Then (PS-3)
   with `N ≤ 16` bounds `m/n` and, with RES-DEGREE, `D`.

This attack has the property the campaign has been missing for a week: **it does
not consume the census, so it is immune to `OPEN[MOH-PROGRAM]`.**

### 7.2 Strongest counterexample attack

**Target the `V_2 ≥ 2`, `k` small, `s = 3` MOH-4 survivors at `D = 108` — not
`D = 105`, and not `V_2 = 1`.** Reason: `V_2 ≥ 2` is where the Davenport–Stothers
moduli become positive-dimensional (`γ = V(de−d−e)+1` grows with `V`), so the
bottom star has free parameters to absorb the gluing relations; `V_2 = 1` is
rigid and therefore the *worst* place to look for a solution, which is precisely
why the previous flagship's `D = 105` targets were hard. The concrete first
target from the MOH-4 list at `D = 108`, `K = 36`, is a group with `V_2 ≥ 2`,
`s = 3` and the largest `γ`; the coordinator can read it off
`box/censusrebase-drivers-20260902/survivors-D48-120.txt` intersected with the
MOH-4 predicate.

Method: fix the bottom dessin in its `γ`-dimensional family, impose the `n − m`
degree-killing relations of the Lagrange interpolant order by order **after**
declaring the outer/inner split and the exponent semigroup (Sol's repair list),
and Newton-lift over `Q_p` for a prime `p ∤ deK`. A solution to order `≫ 1` at a
`V_2 ≥ 2` skeleton would be the first positive signal above `D = 100`; the
dimension count (free star moduli `γ` + gluing constants `k` versus `n − m`
relations) is the stop condition and it is computable before any lifting.

---

## 8. Reranked bottlenecks

**Proof side** (1 = most binding):

1. **No datum outside the skeleton.** Every promoted result is a function of the
   tree; the tree cannot bound `D` (PIN-NOT-CEILING). *Unblocked by §5.*
2. **`OPEN[MOH-PROGRAM]`.** Not because it proves anything (§1.3 — it doesn't),
   but because every emptiness sentence the campaign writes is unsound until it
   is typed. *62–92 % recovered here; the remainder is one page lookup.*
3. **The residue lower bound (§7.1 step 3).** The single new theorem the proof
   attack needs. Previously not on the list at all.
4. *(was 1)* Realisability of an infinite census. **Demoted**: measured here to
   be non-terminating (§2.3(f)); it is a target-list generator, not a program.
5. The exponent semigroup / outer-root split for the interpolation engine
   (Sol's repair list). Still blocking any order-by-order lane.

**Disproof side:**

1. **No `V_2 ≥ 2` target has ever been attempted.** Every realisation attempt so
   far (D = 105 STAR row, mixed-branch packet, the trio) is `V_2 = 1` or dead.
   This is the largest unforced error in the campaign's target selection.
2. The order-by-order engine's foundations (semigroup, outer data) — Sol's lane.
3. Absence of a Newton/Puiseux lifting harness with a declared dimension count.
4. *(was high)* D = 105 specifically. **Demoted to background**: conjecturally
   empty, and rigid where it isn't.

---

## 9. Disposition vector — APPROACHES.md, 46 rows (changes only)

Unchanged unless listed. Reasons are one line each.

| row | change | reason |
|---|---|---|
| **1** GGV Newton-polygon corner families | **REOPEN as receiver** (not as a route) | RES-DEGREE (§6) makes `deg_x Res_y(g−c_2,f)` a needed quantity, and GGV's corner machinery is the campaign's only tool that computes it from supports. Do not restart the degree farm. |
| **6** Abhyankar–Moh one-place / coordinate recognition | **RAISE** | `OPEN[MAJOR-MULT]` is most likely an AM major/minor-disc definition (Q3(d)). The row was closed as "tried on the wrong object"; the right object is now named: Moh's `p(π)` factor type, not the fibres. |
| **7** Nonproperness / Jelonek `A(F)` | **RAISE slightly** | RES-DEGREE's shed term `Σ(1−δ⁰_i)⁻` is a computable invariant of the asymptotic behaviour; it is the first handle on `A(F)` that does not require constructing it. |
| **16** D-module / holonomic index | **RETYPE, do not raise** | Q3(a) points here, but §2.1 shows the same content is available in polynomial algebra. Keep as the abstract home of PS-GROWTH, not as a lane. |
| **20** Reduction mod p / p-curvature | **unchanged (LOW)** | Already run; identically zero p-curvature. Q3(c) does not revive it. |
| **25** Fiber monodromy / dessins / Hurwitz passports | **RAISE to second flagship candidate** | TF-DESSIN + STAR-ABC give an explicit passport `([e^{dV}],[d^{eV}],[(d+e)V−1,1^γ])`; Q3(b)'s tower-rigidity question is now well-posed, and MAJOR-MULT gives it a specific client (`V = 1` pairs). The row's stated weakness ("single-cover passports ignore the second coordinate") is exactly what BOTTOM-ODE fixes. |
| **29** LND / Hamiltonian-derivation / commuting frames | **RAISE slightly** | (PS-1) is a Hamiltonian/trace identity; the row's `κ(P) = [div V] mod D_P` Gauss–Manin gate is the natural receiver for a residue-non-vanishing lemma (§7.1 step 2). |
| **36** Guided counterexample search | **RETARGET, same score** | Change the target class from "structured supports" to "MOH-4 survivors with `V_2 ≥ 2` at `D = 108,120`". Same machinery, a target list that is now 1,908 not 14,016. |
| **44** Moskowicz "no prime td" | **unchanged (closed)** | — |

All other rows unchanged. Note in particular that **no row is raised on the
strength of the census** — that is deliberate (§2.3(f)).

## 10. Disposition — Q3 (a)–(f) and the queued fronts

Q3 (a)–(f): see the table in **§2.3** (a RAISE-in-elementary-form, b RAISE,
c LOWER/diagnostic, d RAISE, e LOWER-and-reaim, f RAISE-and-asserted).

| queued front | disposition | reason |
|---|---|---|
| census-rebase second-reader review (Moh pp.200–202 + App. II) on the page images | **RAISE to first priority among queued; and RESCOPE** | It is now the cheapest decisive act in the campaign: three specific questions (§2.4) decide `OPEN[MAJOR-MULT]`, `MOH-INCREMENT` and the shape of Appendix II, and one of them empties `D = 105` for free. Rescope from "second reading" to "three questions". |
| branch-orbits v2 on the (1)–(13) space | **LOWER, rescope to MOH-4 space** | Running it on the (1)–(13) superset burns a seat on 5–7× too many groups. Hold until the sieve is typed; then it is cheap. Its (UNI) question is unchanged. |
| DISC-COUPLING relaunch (GLOBAL-COUPLING) on a `D = 105` survivor | **STOP as scoped; RELAUNCH on a `V_2 ≥ 2` `D = 108` survivor** | The `D = 105` targets are `V_2 = 1` (rigid, single-orbit star) and conjecturally empty. Same lane, different target — this is the largest single correction I can offer to the queue. |
| box01 Keller-cluster census harvest | **unchanged (auxiliary)** | A numerical cluster is not a map; the merge is fail-closed and the summary is the result. Do not re-run to close `N = 8`. |

## 11. Idea cards

### CARD 1 — MOHSIEVE: recover Moh's program as a typed predicate stack

- **Dependencies.** `box/moh_skeleton_full.py` (present); optional: Moh page
  images for `OPEN[MAJOR-MULT]`. No AWS, no PDF strictly required to *start*.
- **Cheapest discriminator.** Already run (§1): the (75,50) residue must be
  exactly `{M_2 = 55, V_2 ∈ {2,3}}` and all six printed rows must survive.
  Any candidate predicate is accepted/rejected in seconds.
- **Outcomes.** (i) MAJOR-MULT is Moh's → the sieve is 3 clauses, `D = 105`
  empties, `D_min ≥ 108`, and the target list drops to 1,908 groups.
  (ii) MAJOR-MULT is not Moh's → it is typed CONJECTURE, the two derivable
  clauses still cut 658 → 247, and the trio survives as a `V_2 = 1` background
  target. (iii) A fourth clause is found that reaches 6 rows → Moh's program is
  fully recovered and `OPEN[MOH-PROGRAM]` closes.
- **Stop condition.** If no predicate stack reaches ≤ 20 rows at `n ≤ 100`
  while keeping 6/6 within two lane-days, declare the residue case-by-case
  (Appendix II) and stop; the campaign then knows a uniform sieve does not exist
  and must use §5.
- **Expected information gain.** High and immediate: it converts the campaign's
  largest soundness liability into a measured number, and it has already moved
  `D = 105` from "flagship target" to "conjecturally empty".

### CARD 2 — PSGROWTH: the degree-free identity family

- **Dependencies.** sympy (present); a small library of genuine Keller pairs in
  Moh's gauge for controls. Nothing else. Independent of `OPEN[MOH-PROGRAM]`.
- **Cheapest discriminator.** Is `[y^{n-1}](f^{k-1} mod (g − c_2))` identically
  zero on Keller pairs? Measured NO at `n = 2,3` (values 2, 4c−4x, 3, −4). Next:
  `n = 4,5,6`, `k ≤ 20`. One CAS run.
- **Outcomes.** (i) Non-zero with `x`-degree growing in `k` → (PS-3) bites and
  §7.1 is the proof route. (ii) Identically zero → a clean theorem
  ("plane image-conjecture vanishing") and the route dies cleanly. (iii)
  Non-zero but `x`-degree bounded independently of `m` → the mechanism is real
  but weak; it becomes a shape constraint on `m/n`.
- **Stop condition.** Outcome (ii), or no residue lower bound within a lane-week.
- **Expected information gain.** This is the only card that can produce a
  *ceiling*. PIN-NOT-CEILING closed the boundary route; this reopens the
  question on a different object, and it is cheap enough to settle in a day.

### CARD 3 — STAR-ORBIT: Galois rigidity of a tower of Davenport–Stothers pairs

- **Dependencies.** STAR-ABC and TF-DESSIN (promoted); the passport
  `([e^{dV}],[d^{eV}],[(d+e)V−1,1^γ])`, `γ = V(de−d−e)+1`.
- **Cheapest discriminator.** For `V = 1` and `(d,e) = (2,3)` the DS pair is
  unique up to normalisation (one orbit, field of moduli `Q`). So a realisation
  with `k` bottom discs has exactly `k` gluing constants against `n − m`
  polynomiality relations. **Test: is `k < n − m` for every `V_2 = 1` group in
  the census?** If yes, every `V_2 = 1` skeleton dies by counting — and that
  would *prove* MAJOR-MULT rather than assume it, closing `OPEN[MAJOR-MULT]`
  without the page images. Desk-scale: it is one pass over the census.
- **Outcomes.** (i) `k < n − m` always → MAJOR-MULT proved, `D = 105` dead,
  `OPEN[MAJOR-MULT]` closes positive. (ii) Counterexamples exist → those are the
  precise `V_2 = 1` skeletons that need the page images. (iii) The count is
  wrong because outer data supplies unknowns → Sol's outer/inner split is
  required first, and this card queues behind the framework lane.
- **Stop condition.** Outcome (iii) — do not guess the outer count.
- **Expected information gain.** Potentially decisive for `D = 105` at zero
  external cost, and it is the only card that could turn my conjectured clause
  into a theorem. **This is the highest expected-value hour in the whole
  submission.**

## 12. Lane dispositions

| lane | disposition | reason |
|---|---|---|
| `global-interpolation-sol56-20260902` (running) | **CONTINUE unchanged** | It is writing the exact global conditions and the exponent semigroup, which every order-by-order card queues behind. Do not retarget it mid-flight; the `D = 105` first targets in its charge are now suspect, but the *framework* is target-independent. |
| `reducible-branch-review-grok46-20260903` (running) | **CONTINUE** | Delta (g) is unreviewed and its claim (the census + pinned-N filter is ONE program for both branches) is load-bearing for everything in §1 — my group counts are branch-agnostic and inherit that claim. |
| `websweep-20260903T1010Z-grok46` (running) | **CONTINUE** | 24 h cadence was overdue; also the only channel that could find the Abhyankar–Moh major/minor-disc definition without the page images (Q3(d)). **Add one query**: "major disc" / "minor disc" in Moh's and Abhyankar–Moh's configurations-of-roots papers, and Sathaye–Stenerson δ-sequences. |
| census-rebase second reader (queued, blocked on PDF) | **CONTINUE, RESCOPE, PROMOTE to first** | §2.4's three questions. |
| branch-orbits v2 (queued) | **REDESIGN** | Run on the MOH-4 space, not (1)–(13). |
| DISC-COUPLING / GLOBAL-COUPLING (queued) | **REDESIGN** | Retarget from `D = 105` (`V_2 = 1`) to a `D = 108` survivor with `V_2 ≥ 2`. |
| box01 cluster census | **STOP** | It is billing ~$7/h, its merge is fail-closed, and its output is auxiliary. Nothing in this submission uses it. |

### The single lane I would launch first with a frontier seat

**CARD 3 (STAR-ORBIT), as a short exact lane** — "is `k < n − m` for every
`V_2 = 1` group in the (1)–(13) census, given the unique `(d,e)` Davenport–
Stothers star?" It is desk-scale, needs no page images, no AWS and no framework,
and it can *prove* the one clause on which `D = 105` and 744 groups now hang.
Every other candidate either waits on the Sol framework, waits on the PDF, or
costs a flagship seat for `D_min ≥ 108`.

Second choice, if the coordinator wants breadth rather than depth: CARD 2
(PSGROWTH), because it is the only card that is independent of
`OPEN[MOH-PROGRAM]` and the only one that can produce a ceiling.

## 13. Campaign-systems check — UPGRADE

**Finding.** This submission's central result came from running a banked
instrument with three one-line predicates, in 20 minutes, against a fail-closed
control the campaign already had. It was available to every lane since
2026-09-02 and no lane ran it. The systems gap is not compute, sandboxing or
adapters (all healthy: `LINUX_BWRAP` regression PASS, systemd twin sealed) — it
is that **`OPEN[…]` entries carry a bounded quantity but no cheapest-test
field**, so an OPEN that is 20 minutes from resolution looks the same in the
ledger as one that needs a flagship.

**UPGRADE (smallest useful test).** Add one required field to the
`ops/open_collision.py` OPEN contract:

```text
cheapest_test: <one line: the instrument, the gate, and the wall-clock estimate>
```

and one gate in the round packet template: *any OPEN whose `cheapest_test` is
under one lane-hour must be attempted before the round's questions are set.*

Smallest useful test of the upgrade itself: re-emit the six currently live
OPENs (`MOH-PROGRAM`, `PROP-5.6-SHADOW`, `MAJOR-MULT`, `RES-SHED`,
`PS-VACUITY`, `UPPER-TO-FLOOR` if still open) with the new field, and check that
at least one is under an hour. **Predicted result: `PROP-5.6-SHADOW` and
`MAJOR-MULT` both are** — `PROP-5.6-SHADOW` was measured on 2026-09-02, typed as
an OPEN, and then not folded in, which is exactly the failure this field
prevents.

Second note (no card): box01 is idle and billing; stopping it is a human gate,
so raise it to DC inside the round synthesis message, not separately.

## 14. OPEN ledger raised by this submission

| OPEN | bounded quantity | cheapest test |
|---|---|---|
| `OPEN[MAJOR-MULT]` — is `V_j ≥ 2` (equivalently: is the `p(π)` factor selecting a major disc non-simple) part of Moh's Def 5.1 / p.200 (4)–(7)? | **161 rows at `n ≤ 100`** (247 → 86 under `V_2 ≥ 2`, → 51 under `V_j ≥ 2`); **744 groups at `48 ≤ D ≤ 200`** (2,652 → 1,908); **the entire `D = 105` trio (3 groups)** | one page lookup (p.179 Def 5.1), or CARD 3's counting test — under one lane-hour either way |
| `OPEN[PS-VACUITY]` — is `[y^{n-1}](f^{k-1} mod (g − c_2))` identically zero on Keller pairs? | the finite set `k ≤ 20`, `n ≤ 6`; currently **non-zero in 4 of 10 measured instances** | one sympy run, minutes |
| `OPEN[RES-SHED]` — the value of the shed term `Σ_i (1 − δ⁰_i)⁻ = N − deg_x Res_y(g−c_2,f)` per skeleton | **1,908 MOH-4 groups at `48 ≤ D ≤ 200`** (14,016 if MOH-4 is not adopted) | derive `deg_x Res` from the tree on one group and compare with the `q`/`δ_1` data already in `survivors-D48-120.txt`; one lane-hour |
| `OPEN[MOH-PROGRAM]` (existing, bounded 652 excess rows) | **REPRICE: 80 excess rows / 11 excess classes at `n ≤ 100`** under MOH-4 (51 rows / 13 classes vs Moh's 6 / 4), if MOH-INCREMENT and MAJOR-MULT are accepted; 241 excess rows if only the two derivable clauses are | the predicate stack of CARD 1 |
| `OPEN[PROP-5.6-SHADOW]` (existing, bounded 220 groups at `D ≤ 120`) | **RAISE**: promote from "measured, not folded in" to a component of the sieve; its residual gap is only the `r = 2` branch datum, which `A_1 ≥ 2` determines | §2.4 question 2 |

## 15. Custody, reproduction, and what I did not do

- Charged input hash verified before reading. `refs/moh1983…pdf` **absent**;
  every Moh-page claim is from the census-rebase §1 transcription, and the one
  claim that goes beyond it (MAJOR-MULT's provenance) is typed
  SOURCE-UNVERIFIED.
- Instruments: `box/moh_skeleton_full.py` (`d20bf0841a1ba2b2…`, read-only, not
  modified), sympy. Drivers written to `/tmp/id-opus5/` only:
  `probe.py, incr.py, casc.py, alldeg.py, battery.py, moh4.py, resdeg2.py`.
  Total wall < 12 min, one core, < 1 GB. No ledger edited, no `box/` write,
  `jc2-lean` not inspected, no 20260903T1015Z submission read, no in-progress
  lane report read.
- Not done: I did not run the pinned-N knapsack downstream of MOH-3/MOH-4 (the
  `d1floor.py` composition). That is the obvious next 10 minutes and I ran out
  of window; the group counts above are pre-knapsack, so the emptied-degree list
  is a **floor** on what the sieve plus integrality empties. In particular
  `D = 105` empties before integrality is even applied.
- No exit-price assertion is made in this submission, so no `charge_basis` line
  is required.

<!-- BODY-END -->
