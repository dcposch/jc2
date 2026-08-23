# Hostile review: sol-h29-dichotomy.md (H_29 depth dichotomy)

Reviewer: Grok 4.6 (hostile referee, theorem / verdict tier). Date: 2026-08-21.
Target: `xmodel/sol-h29-dichotomy.md`.
Cross-checks: `cases/eplus_certify.py`, `cases/d25_eplus.py`,
`cases/valuation_e2.py` (`RMAX`, `GIDX`, `DBUILD`), `cases/d23_eplus.json`,
`cases/d25_eplus.json`, `SHEET6-DIRECTIONB.md` §§8.S9 and 9.S3,
`xmodel/sol-round6.md` §1, `xmodel/sol-newton-lemma.md` (1.0)–(1.11),
(2.1), Lemma 2.1, (4.5), Theorem 6.1, (8.7), `xmodel/sol-round5.md` (O),
`xmodel/sol-algkill.md` §3 and Proposition 3.3.
Method: replay the projection argument as a filtered-linear-algebra lemma;
independently recompute the 30-stream window cardinalities; read both
driver sources and both banked JSON headers; check D43/D45/D75 level
arithmetic against (1.11); check the growth/kill quantifiers against
Newton’s sufficient-not-necessary status. No Singular, no msolve, no
replay of the 36+360 point sweeps, no other repo file modified, no git.

The load-bearing sentences are the boxed floor at
`sol-h29-dichotomy.md:16-18`, the persistence claim at lines 20–24,
the RMAX-40 identification at lines 26–30, the D43 discriminator at
lines 33–37, and the growth-kill scope at lines 47 and 721–733.

---

## Verdict

**Four claims under attack. None REFUTED. Claim (1) CONFIRMED as a
theorem about a fixed causal \(L\). Claim (2) CONFIRMED as a
repository fact; 9.S3 (and the joint 8.S9/9.S3 reading) needs a
scope-correction addendum. Claim (3) CONFIRMED on the \(H_{29}\)
level bookkeeping; residual GAPS sit only in the Row-42
first-occurrence extrapolation, already labelled. Claim (4)
CONFIRMED: a growing floor kills finite-loss germs only;
`FORMAL-REGULARITY-30` and `LOCUS-UNIVERSAL-H29` are the correct
named gaps.**

The document does not prove \(\ell=37\), does not prove a locus-wide
floor, and does not prove a kill of \(\mathcal Z_\infty\). It does
not claim those. The campaign consequence stands: the next honest
computation is a real post-41 operator at D43, not another band-40
scan and not D45 as the first \(H_{29}\) test.

**Tier deserved: BANKED analysis note, theorem-tier on persistence
and on the kill quantifiers; artifact-tier on RMAX-40. Not a
promotion. Not a DEPTH \(e\). Not a germ. Not a locus theorem.**

---

## Per-claim table

| # | Claim | Verdict | What would have flipped it |
|---|---|---|---|
| (1) | Persistence: for a fixed completed corrected operator carrying the pair, \(t^{36}e_{29}\) is never repaired by deeper rows / higher causal columns; \(\ell\ge37\) is permanent for that \(L\) | **CONFIRMED** (lemma). Residual **GAPS** only on identifying the banked window with the true \(L_{40}\) | a counterexample to the projection, or a causal high column that hits band 36 |
| (2) | D23 and D25 \(e^+\) sweeps both used the same band-\(\le40\), \(174\times170\) window; 8.S9/9.S3 need scope-correction addenda | **CONFIRMED** (fact + addendum warranted) | a D25 code path that rebuilt `GIDX`/`RMAX` or appended \(H_{29}u^1\) |
| (3) | Cheapest genuine discriminator is D43 (includes level 42); D45 adds Row 44 and no further \(H_{29}\) coefficient | **CONFIRMED** on the bookkeeping. **GAPS** on the \(k+27/k+32\) cap at Row 42 | residual convention `level ≤ D`, or \(H_{29}u^2\) appearing before level 48 |
| (4) | Growing floor kills finite-loss germs only; `FORMAL-REGULARITY-30` + `LOCUS-UNIVERSAL-H29` are the gaps | **CONFIRMED** | a converse to Newton that the file claimed to have, or a locus-wide floor proved from the 36+360 samples |

No claim is REFUTED.

---

## Claim (1) — Persistence theorem

Attacked lines: `sol-h29-dichotomy.md:120-184`, Proposition 2.1,
application (2.2)–(2.3).

### 1.1 The lemma, as linear algebra

Let \(L:X\to Y^+\) be \(k\)-linear and causal in the filtration sense
\(L(F^nX)\subseteq F^nY^+\). Write \(q_B:Y^+\to Y^+/F^{B+1}Y^+\) and
let \(L_B\) be the induced finite map. Hypothesis (2.1) is
\(q_B(y)\notin\operatorname{im}L_B\) for a target of level \(\le B\).

Causality gives \(L(F^{B+1}X)\subseteq F^{B+1}Y^+\), so \(L_B\) is
well-defined on \(X/F^{B+1}X\). If \(y=Lx\), then
\(q_B(y)=L_B(q_B^X(x))\), contradiction. That is item 1:
\(y\notin L(X)\). Continuity is not an extra hypothesis: any \(x\) in
the filtration completion still has \(q_B(Lx)=L_B(q_B^X(x))\).

For \(B'>B\), the projections commute. Causality again kills the extra
columns of level \(>B\) after \(q_B\), and extra output coordinates
are discarded by \(q_B\). Hence
\[
q_{B'}(y)\in\operatorname{im}L_{B'}
\;\Longrightarrow\;
q_B(y)\in\operatorname{im}L_B.
\]
Item 2 follows. Item 3 is the literal \(n=0\) clause of (1.1): if
\(y\in F^eY^+\) and \(y\notin L(X)\), then
\(F^eY^+\not\subseteq L(F^0X)\).

The proof at lines 140–146 is terse and complete. There is no hidden
completeness gap, no characteristic-\(p\) division, and no use of Ore
structure. Hostile replay: **CONFIRMED**.

### 1.2 The arithmetic \(\ell\ge37\)

\(y_0=t^{36}e_{29}\) has \(\nu_Y(y_0)=36\), so \(y_0\in F^eY^+\) for
every \(e\le36\) and not for \(e=37\). Combined with item 1 at
\(B=40\), every such \(e\) fails at \(n=0\), hence \(\ell(L)\ge37\).
This is exactly the strengthening (8.7) of
`sol-newton-lemma.md:916-927` over the weaker Round-6 \(n=6\) bound
\(\ell\ge31\). (Because \(r_{\min}=6\), one has \(F^0X=F^6X=X\), so
the two conventions share the same image \(L(X)\); they differ only in
which filtration piece of \(Y^+\) is demanded. The \(n=0\) reading is
the definition (2.1) and is strictly sharper.)

The banked window certificate is of the right shape. Round 6
(`sol-round6.md:97`) adjoins the unit target on \((H_{29},u^0)\) and
raises rank by one. The 8.S9 scan at a named D23 point ends at
```
[n_eval, v, n_uncovered, max_uncovered_level, ell_ge] = [0, 6, 115, 36, 37]
```
in `cases/d23_eplus.json` (literal \(n=0\), max uncovered level 36).
`Colspace.covered_rows` tests unit-target membership, not merely
pivot-row count, so 115 uncovered unit targets at rank 117 is
possible and is the correct obstruction predicate.

### 1.3 What “deeper rows / higher columns cannot repair” does and does not say

On a **fixed** causal \(L\) carrying (2.1) at \(B=40\):

- new output rows cannot put an old missing target into the image
  (item 2);
- new source columns of level \(>40\) are killed by \(q_{40}\)
  (causality);
- surplus output streams, with the same source, only add obligations.

The trichotomy requested in the generating prompt therefore collapses
to the stated dichotomy: drop is impossible for that \(L\); exact
flatness versus reinforcement remain. **CONFIRMED.**

The two named escape hatches at lines 172–177 are the right ones, and
they are not covered by Proposition 2.1:

1. a *different* completed point, whose low operator does not carry
   the pair;
2. an omitted source direction of level \(\le40\).

Escape (1) is excluded only by **CONJECTURE LOCUS-UNIVERSAL-H29**.
Escape (2) is excluded only by corrected source generation plus
`CYCLIC-30` / surplus-`BRIDGE-30`, and, at level 42, by
**CONJECTURE X-SIDE-30**. The document does not smuggle those into
the proposition.

### 1.4 Residual GAPS (do not flip the lemma)

These are identification hypotheses for applying Proposition 2.1 to
the *banked* window, not holes in the projection.

- **Causality of the true \(L\).** FILTER-30 executable check `f1`
  (`eplus_certify.py:234-237`) measures no entry with \(n<r\) in the
  pure-\(y\) window. All-depth causality, including the \(t^{42+}\)
  x-side, is the pending FILTER-30 lemma. If a negative \(t\)-shift
  existed, a high column could hit band 36 and the finite \(L_{40}\)
  would not be the true projection.
- **X-side below \(t^{42}\).** The claim that “the \(t^{42+}\) x-side
  cannot alter the already certified band-\(\le40\) projection” is
  *not* a consequence of Proposition 2.1. It is the construction
  claim `DBUILD = 42`, “pure-\(y\) exact below \(t^{42}\)”
  (`valuation_e2.py:38-41,99-102`; `sol-round5.md:41`). Differentiating
  an x-side factor that started at \(t^{42}\) could produce lower
  terms only if that factor had a negative power of \(t\). That is
  again FILTER-30. The dichotomy file itself refuses to cite
  `SHEET6-R1.md` §16.5 as an implementation (lines 360–362). Honest.
- **Completion dependence of the low matrix.** 8.S9 already records
  that levels 51/53 enter window entries. So even band \(\le40\) of
  \(DH_s\) depends on the named completion. Persistence is for fixed
  \(s\), not for “every prolongation of this D25 cell.” The executive
  sentence “Thus the floor cannot drop” (line 22) is correct only
  under the quantifier on the previous sentence (“every fixed
  completed corrected operator carrying the certified binding pair”).
  Corollary 2.2 states the locus version with the conjecture
  attached. No overclaim once the quantifier is kept.

**Verdict on (1): CONFIRMED.** \(\ell(L_s^+)\ge37\) is permanent for
each such \(L\). It is not an exact loss, and it is not automatically
locus-wide.

---

## Claim (2) — RMAX-40 artifact; 8.S9 / 9.S3 addenda

Attacked lines: `sol-h29-dichotomy.md:26-30, 46, 202-222`.
Required check: `cases/eplus_certify.py` and both driver runs.

### 2.1 The window is a compile-time constant

`cases/valuation_e2.py:102` sets `RMAX = 40`. `GIDX` is built at
import from `allowed_r` with that cap (`valuation_e2.py:104-112`),
length `GD = 170`. `eplus_certify.py:118` binds `RMAX = V2.RMAX`.
`window_object` (`eplus_certify.py:268-283`) enumerates output
coordinates \((a,j)\) with \(s_a+6j\le40\) against those 170 columns.
The gate `p1_square_object_174x170` asserts shape `(174, 170)`.
Independent recount of the 30-stream shifts (below, Claim 3) gives
exactly 174 outputs at band 40.

`gate_param30(E, p, D)` (`eplus_certify.py:312-357`) uses `D` only
for
\[
\texttt{thresh} = \lfloor(D-1)/2\rfloor.
\]
It does not rebuild `GIDX`, does not raise `RMAX`, and does not
append \(H_{29}u^1\) (that row is \(s_{29}+6=42>40\)).

`--depth` exists (`eplus_certify.py:667`) and is a trap: it is
threaded only into `certify_point(..., D=args.depth)` and thence into
that threshold. The dichotomy’s warning at lines 305–306 is factually
right.

### 2.2 The D25 driver calls the same routine

`cases/d25_eplus.py:104` imports `eplus_certify as EC`.
`certify_point_f` (`d25_eplus.py:917-958`) still builds jets with
`Z` of length 42, still calls `V2.euler_rows`, and calls
`EC.gate_param30(E, p, D)` with module-level `D = 25`. It does not
rebind `RMAX`. The band-24 frontier stage changes the *point*
(levels 51/56) and rebuilds the same 42-slot operator; it does not
extend the window. Threshold in the D25 JSON is 12
(`threshold_floor_Dm1_2: 12`); D23 JSON is 11. Window key in both
artifacts is `window_rank_174x170`.

Banked headers:

- `cases/d23_eplus.json`: `depth_D = 23`,
  `ell_lb_certified_distribution = {"37": 36}`,
  `e_plus_certified_all_points = null`, 36 points.
- `cases/d25_eplus.json`: `depth_D = 25`,
  `ell_lb_certified_distribution = {"37": 360}`,
  `e_plus_certified_all_points = null`, 360 points.

The last field is load-bearing exactly as the dichotomy says
(lines 67–70): 37 is a certified floor, not a certified
right-section loss.

### 2.3 Same window, not the same matrix

Lines 26–29 say “the same band-≤40, \(174\times170\) matrix.” The
next sentence correctly weakens this to the same operator-window
*routine*, with the D25 driver changing the point and the Newton
threshold. The first sentence is slightly too strong: D25 interior
points use a nonzero frontier completion, 8.S9 already knows that
levels 51/53 enter window entries, and 9.S3 records the rank split
collapsing from 117/115 to 115/174 uniformly. Those are different
matrices of the same shape. Intended claim (same `RMAX`, same 174×170
scanner, no \(H_{29}u^1\)) is true. Precision only; not a refutation.

### 2.4 Do 8.S9 / 9.S3 need addenda?

Yes, for the two-depth reading. Not because they claimed a locus
theorem they did not.

8.S9 (`SHEET6-DIRECTIONB.md:2214-2324`) already says the window is
bands \(\le40\), already says the floor is completion-dependent, and
already says sampling is not other completions / other fibers /
all-depth loss. In isolation it is an honest D23-stage certificate.

9.S3 (`SHEET6-DIRECTIONB.md:2410-2555`) is the problem child. It
writes “THE LANDSCAPE IS FLAT,” “the identical binding pair as D23,”
and “the window floor DOES NOT MOVE.” Those sentences are true as
*re-measurements of the same band-40 window at new points*. They are
false as a statement that \(\ell(23)=\ell(25)=37\) or that a depth
derivative was estimated. 9.S3 also already says, correctly, that
sampling cannot prove the locus-wide claim. The missing addendum is
the RMAX identification, not the locus-quantifier.

The dichotomy’s own correction (lines 50–62) matches the banked
caveats: 8.S9 is 36 named D23 completions on the radical fiber; 9.S3
is 360 named D25 completions; `LOCUS-UNIVERSAL-H29` is the extra
quantifier. **CONFIRMED**, including the demand for scope-correction
addenda. This review does not write them (no other file changes).

**Verdict on (2): CONFIRMED.** D23 versus D25 did not measure
flatness in depth. One measurement, twice, against two Newton
thresholds (11 and 12), both far below 37. Both refutations of
depth-only germ certification remain valid; the depth-derivative
reading does not.

---

## Claim (3) — D43 versus D45 discriminator

Attacked lines: `sol-h29-dichotomy.md:33-37, 255-296, 276-297, 524-529`.

### 3.1 Residual convention and the first new \(H_{29}\) coefficient

Newton (1.10)–(1.11): a depth-\(D\) point means
\(\mathcal H(s)\in F^DY^+\), i.e. \([u^j]H_a(s)=0\) whenever
\(s_a+6j<D\). Selected output levels therefore satisfy `level < D`.
Band cap of the derivative window is \(D-1\).

\(H_{29}u^0\) lives at 36. \(H_{29}u^1\) lives at \(36+6=42\).
\(H_{29}u^2\) lives at 48.

- D42 has band cap 41 and does **not** contain level 42.
- D43 has band cap 42 and **does** contain level 42. Minimal such
  depth.
- D45 has band cap 44. Next \(H_{29}\) coefficient is 48, first
  present at D49.

Level 42 is also the first x-side band (`DBUILD = 42`). D43 is
therefore not a pure Ore-shift experiment: it confounds
\(H_{29}u^1\) with the omitted x-side. The file says so (lines 30–31,
243–244, 349–362) and banks **CONJECTURE X-SIDE-30**. That does not
make D45 a better *first* \(H_{29}\) test. D45 is the right immediate
regression after D43 works (Row 44, source cap 75→77, \(194\times190\)),
and it still does not expose \(H_{29}u^2\). **CONFIRMED.**

### 3.2 Window cardinalities, independently recomputed

Shifts: nine streams at \(s=6\), ten at \(s=8\), nine at \(s=10\),
one at \(s_{28}=16\), one at \(s_{29}=36\). Inputs: six streams at
each of \(r=6,8,16\), four at each of \(r=7,9,11\). Formula (4.1)
with band \(B=D-1\):

| \(D\) | \(B\) | \(N_Y\) | \(N_X\) | \(H_{29}\) coeffs |
|---:|---:|---:|---:|---|
| 41 (banked window) | 40 | 174 | 170 | \(u^0\) at 36 |
| 43 | 42 | 184 | 180 | \(u^0,u^1\) at 36, 42 |
| 45 | 44 | 194 | 190 | \(u^0,u^1\) at 36, 42 |
| 75 | 74 | 344 | 340 | \(u^0,\ldots,u^6\) at 36 through 72 |

The +10 outputs from 40→42 are the nine \(s=6\) streams plus
\(H_{29}\) (both \(\equiv0\pmod6\)). The +10 inputs are six \(r=6\)
coordinates at 42 plus four \(r=11\) coordinates at 41. 344 and 340
likewise match. \(344\cdot340=116960\) dense slots, as written.
**CONFIRMED.**

### 3.3 Row-30 nine-component count

Even rungs 26, 28, 30, 32, 34, 36, 38, 40, 42. Outputs of level \(k\)
are the streams with \(s_a\equiv k\pmod6\) and \(s_a\le k\). For
\(k=30\equiv0\pmod6\) only the nine \(s=6\) streams are live
(\(s_{29}=36>30\)). Every other listed rung has ten selected
components (the \(\equiv2\) rows are the ten \(s=8\) streams; the
\(\equiv4\) rows are nine \(s=10\) plus \(H_{28}\); the later
\(\equiv0\) rows pick up \(H_{29}\)). So 89 selected equations and,
under ten first-occurrence tails per even row, 90 new coordinates;
28+90=118 variables, 34+89=123 rows. D45 adds ten+ten:
128/133. D25-to-D75: 25 even rungs, 250 tails, 249 equations, 278/283.
The arithmetic is consistent with the 30-stream grading.

### 3.4 GAPS: first-occurrence caps at and after Row 42

The last table column and the exclusive generator caps 75, 77, 107
cite `sol-algkill.md` §3: ordinary tails at Row \(k+27\), six even
tails at Row \(k+32\). That paragraph is stated for even
\(12\le k<42\) (`sol-algkill.md:329-332`). Row 42 is exactly the
boundary at which the law is not claimed, and is the first x-side
row. The same section already says that extrapolating the
\((9,10,10)\) component cycle forever is a conjecture
(`sol-algkill.md:337-340`).

The dichotomy attaches **CONJECTURE X-SIDE-30** and calls the parked
counts “acceptance checks conditional on X-SIDE-30, not permission to
discard a discrepancy” (lines 400–402). That is the right label. It
is a GAP in the *compiler contract’s source cap*, not in the
statement “D43 includes level 42 and D45 adds no new \(H_{29}\)
coefficient.” The \(H_{29}\) bookkeeping does not use the
first-occurrence law.

Ore non-shift (3.1)–(3.2) matches `sol-round5.md:105-107` (O) and the
commutation \(\Theta u=u(\Theta+1)\). A left-cokernel at coefficient
index \(j=0\) is not a relation at \(j=1\). **FLAT-H29** and
**SHIFTED-H29-BINDING** are correctly conjectural. The conditional
window function (3.4) is correctly *not* a current certificate; if
every \(y_j\) were missed on a fixed all-depth operator one would
have \(\ell=\infty\), not a finite growing \(f(D)\).

**Verdict on (3): CONFIRMED** on the discriminator choice and the
level arithmetic. D45 is not a substitute first test of \(H_{29}u^1\).

---

## Claim (4) — Branch scoping; the two named gaps

Attacked lines: `sol-h29-dichotomy.md:47, 50-62, 676-804`, Theorems
6.1–6.2, Lemma 6.3.

### 4.1 Unconditional growth theorem

Dichotomy Theorem 6.1: a certified locus/all-completion floor
\(\ell(L_s^+)\ge f(D)\) on \(\mathcal C_D(k)\), with
\(2f(D)+1>D\) along an unbounded cofinal ladder, and with every
allowed formal zero belonging to \(\mathcal C_D(k)\) through its
D-jet, implies every such zero has \(\ell(L_z^+)=\infty\).

Proof replay: if \(e=\ell(L_z^+)<\infty\), choose ladder depth
\(D\ge2e+1\). Assumption 3 puts the exact completion \(z\) in
\(\mathcal C_D(k)\), so \(e\ge f(D)\). Then
\(2f(D)+1>D\ge2e+1\), hence \(f(D)>e\), contradiction. No division,
no characteristic restriction, no use of Newton. Assumption 3 is
correctly identified as the root-to-selected-system half of
`CYCLIC-30`/`BRIDGE-30`, not a sampling consequence.

This kills finite-loss linearly regular germs in the scoped tower. It
does not prove \(\mathcal Z_\infty(k)=\varnothing\). The file says so
(lines 721–733), including the \(\nu\gg D\) caveat that the sharp
gate is \(\nu>2e\) at the actual residual depth. **CONFIRMED.**

### 4.2 Conditional kill, and the regularity gap

Theorem 6.2 adds **CONJECTURE FORMAL-REGULARITY-30** (every allowed
formal zero has finite delayed loss) and concludes emptiness. The
weaker **EXISTENCE-REGULARITY-30** (a nonempty root set contains at
least one finite-loss root) also suffices; no uniform bound on the
losses is needed, because the ladder may be chosen past \(2e+1\) per
hypothetical root. Proof is the one-line intersection of “all roots
infinite-loss” with “all (or some) roots finite-loss.”

The regularity hypothesis is false for general filtered Euler
equations. The file’s two examples are the right ones:
`sol-newton-lemma.md` (4.5), \((\Theta+1)u^j=(j+1)u^j\) in
characteristic \(p\), exact root \(0\), infinite loss; and
\(\mathcal H(x)=x^2\), exact root \(0\), zero derivative. Neither
existence, Noetherianity, smoothness of the D25 cells, nor
`PARAM-30` at one advertised point proves the conjecture. Hostile
demand that this be isolated rather than blamed on Newton:
**CONFIRMED.** The generating prompt’s “true formal solution has
finite loss \(e\) and its depth-\((2e+1)\) truncation WOULD certify”
is exactly this gap, not a theorem.

### 4.3 Newton is sufficient, not necessary; the circular certificate

Section 6.3: a true finite-loss root \(z\), with the abstract section
of Newton Lemma 2.1, at \(D=2e+1\), completed by \(z\) itself, meets
the *abstract* Newton hypotheses once the universal application gates
hold. Calling that a finite machine certificate is too strong, because
Lemma 2.1 constructs the section by infinitely many degreewise
choices. **CONJECTURE EFFECTIVE-PARAM-30** is the extra gap for an
Ore/recurrence artifact; **EFFECTIVE-SEARCH-30** is the extra gap for
discovery from a finite jet. Neither is needed for the logical
conditional kill. Correct ranking.

Lemma 6.3 (stability of a delayed section under a deep derivative
change): \(KS\) raises target filtration by \(q-e>0\) on \(F^eY^+\),
so \(B=(I+KS)^{-1}\) converges in the filtration topology and
preserves every \(F^{n+e}Y^+\); \(S_D=SB\) is a right section of
\(L_{s_D}\) of loss \(\le e\). Replay: **CONFIRMED**, under the
stated estimate (6.6). **TRUNCATION-STABILITY-30** is correctly
conjectural; FILTER-30 is the intended source of (6.6) and is not
promoted for the x-side.

### 4.4 Locus quantifier

**CONJECTURE LOCUS-UNIVERSAL-H29** is the right name for the gap
between 36+360 named completions and a residue-A survivor-locus
statement. Pointwise persistence does not consume it (lines 61–62).
A growing *universal* floor additionally needs
**CONJECTURE LOCUS-SHIFTED-H29** (every \(t^{36+6j}e_{29}\) missed
whenever it is in the depth window). The user-facing pair of gaps
named in the generating prompt is therefore slightly incomplete: the
kill theorem’s locus input is the *shifted* universal floor, not
merely the level-36 pair. The file itself banks both conjectures and
does not collapse them. No overclaim.

The elementary nesting \(\mathcal C_{D'}\subseteq\mathcal C_D
\Rightarrow\lambda(D)\) nondecreasing (lines 114–118) is correct and
does not upgrade samples to \(\mathcal C_D\).

Unconditional emptiness remains a finite exhaustive inconsistency
\(V_D=\varnothing\). Citation of `sol-algkill.md` Proposition 3.3
(if \(1\in I_\infty\) then some finite subsystem already contains 1;
asymptotic codimension is not emptiness) is accurate.

Flat-branch D75 arithmetic: \(2\cdot37+1=75\); Newton Theorem 6.1
would produce a root in \(s+F^{38}X\), agreeing with the supplied
point only below depth 38; \(\nu-2e=75-74=1\) at the boundary. All
correct, and correctly withheld from present certification. The
engineering estimate is labelled as such.

**Verdict on (4): CONFIRMED.** Growing floor \(\Rightarrow\) no
finite-loss germ in scope (Theorem 6.1). Emptiness \(\Rightarrow\)
add `FORMAL-REGULARITY-30` or `EXISTENCE-REGULARITY-30` (Theorem 6.2).
Locus-wide statements \(\Rightarrow\) add `LOCUS-UNIVERSAL-H29`, and
for growth, `LOCUS-SHIFTED-H29`. Those are gaps, not theorems.

---

## Residual nits (do not flip any claim)

1. Executive “the same \(174\times170\) matrix” (line 27) versus
   “the same operator-window routine” (line 29): prefer the second
   wording in any addendum.
2. Proposition 2.1’s “causal” must mean \(L(F^nX)\subseteq F^nY^+\),
   i.e. the FILTER-30 sign of the *forward* operator, not a bound on
   the inverse loss \(\ell(L)\). The surrounding campaign language
   uses “causal” for both. The proof only needs the forward
   inclusion.
3. Parked 118/123 and source caps 75/77/107 at Row 42+ are
   X-SIDE-30-conditional; the D43 *window shape* 184×180 is not.
4. 8.S9 in isolation does not mis-report a second depth; the addendum
   load is on 9.S3’s “flat landscape” and on any joint reading of the
   two stages as \(\ell(23)=\ell(25)\).

---

## What the file correctly withholds

- exact all-depth loss 37;
- a theorem that the level-36 pair shifts to 42, 48, …;
- D23/D25 as two depth measurements;
- a pivot-compiler proof of D75, `CYCLIC-30`, `BRIDGE-30`,
  `FILTER-30`, or `PARAM-30`;
- a characteristic-zero lift, convergence, algebraicity, or a
  Jacobian-conjecture counterexample;
- \(\mathcal Z_\infty(k)=\varnothing\) from growth alone.

Those withholds match the hostile Newton review’s application-gate
list. The dichotomy note does not attempt to spend the boxed
\(\ell\ge37\) as a germ or as a kill.

**End of review.** No other file changed. No git.
