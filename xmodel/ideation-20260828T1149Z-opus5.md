# Whole-portfolio JC2 ideation — lane `opus5`, round `20260828T1149Z`

**Model:** Opus 5 (`claude-opus-5`).
**Packet:** `xmodel/ideation-20260828T1149Z-packet.md`, SHA-256 verified
`31094db14e41506e121b037bd001e077d6bd80d6b4f38ae49a071116e52fef94` **[MATCH]**.
**Custody gate:** all 8 canonical hashes and all 15 report/checker hashes in
packet §0 recomputed and **[MATCH]**.  `git rev-parse HEAD` =
`418e413593120d19e15e6546eb50c985f4b1f038` **[MATCH]**.
**Blindness:** **no peer `1149Z` response was read.**  At the start of this
session a filename-only listing showed only the packet and the four
`*-prompt.md` files under that tag.  A second filename-only listing, taken
after this report was drafted, showed that `-fable5.md`, `-grok46.md` and
`-sol-ultra.md` had since been written.  I did not open, read, grep, hash or
otherwise inspect the contents of any of them, and nothing in this report
derives from them.  Correcting my own earlier draft wording, which said no peer
submission existed: that was true when written and is no longer true.  See §10
for the one real independence caveat, which is a different issue.
**Execution:** local CPython standard library only.  No AWS, no Singular,
msolve, Sage or Lean, no running job touched.  `jc2-lean` was never entered,
listed, searched, read, built or modified.  Precise disclosure: I ran
`git status --porcelain` **in the parent repository**, and its output includes a
single pre-existing `M jc2-lean` submodule-dirty line that was already present
in this session's opening snapshot.  I did not run any command inside that
tree and did not read or change anything in it.

This lane produces **one new theorem** (§2), **one new source-level defect**
(§3), and a portfolio scan built on them.  I disagree with the packet's framing
in two named places (§1.1, §4.3).

---

## 0. Executive summary

1. **The packet's §2.2 erratum is stronger than it needs to be, and weaker than
   it should be.**  It instructs "delete the circular p. 20 Remark, retain
   condition (7)".  I prove below that the Remark's *conclusion* is a theorem:
   **there is no constant corner at index `j=0` anywhere on `T_a^+`.**  This is
   exactly the residual gap my own earlier review (`47f2b608...` §7.4 item 1,
   §9 item (f)) left open with the words "not established".  It is now
   established, from Facts A/B plus a `delta_0` edge identity I verified
   exactly.  Erratum item (f) should change from *delete-and-hypothesise* to
   *delete-the-proof, restore-the-statement*.
2. **Statement 3.9's `kappa` hypothesis is `h`-dependent and load-bearing, and
   no consumer in the campaign carries it.**  Prop. 3.1's property ("`kappa` is
   a multiple of any order of `x`-pole") is a condition on the *auxiliary*
   polynomial `h`, not on the fibre.  I have an explicit exact failure at
   `kappa=1`.  Every use of St. 3.9 with a *derived* `h` — in particular **Fact
   A applied to Prop. 4.2 tower members `h_j`**, and Prop. 4.4's proof for
   general `h` — needs an `h`-dependent `kappa`-enlargement clause that is
   currently nowhere written.  This is a NEW audit item (`St 3.9` is currently
   `VERIFIED_WITH_NIT`).
3. **The first exact unproved implication on the shortest pure-Sigray route is
   not in §§2–6 at all.**  With Prop. 4.2 + §2's corner theorem + L3/L4/L5, and
   with the audit's supplied repairs for St. 3.14 / Prop. 5.4 / St. 6.2 and the
   `SOL-PROP58` replacement of Prop. 5.8, §§2–6 has no open blocker on the
   entry-menu route.  The first genuinely unproved implication is **landing**
   (`REDUCTION` CRITICAL 4) — but with a *closer* and cheaper obligation in
   front of it that nobody has priced: **thesis §§7–9 has zero audit
   coverage** while T7 consumes Notation 8.1, T9(a) consumes Prop. 8.4, and
   `Q(F)` consumes Notation 9.1.  The 72-item census stops at Prop. 6.2, p. 30,
   of a 67-page source.
4. **Prop. 5.1's finite-nonzero-puncture repair is bypassable, and §2 supplies
   the reason** rather than a vote: every `F in T_a^+` with a nonempty Prop. 4.2
   tower has `d_{g,F} = (l_0/k_0) d_F > 0`, so no `T_a^+` place has
   `g(P) in C*`.  All campaign uses are at `g`-poles, which are in
   `T_{a,pole} subset T_a^searrow subset T_a^+`.  The gap bites only on
   `T_a^0`/`T_a^-`.
5. **New connection (disproof side).**  `T_a^0` — the cv-vertex stratum where
   `g(P) in C` — is simultaneously (i) Prop. 5.1's gap, (ii) the object
   Prop. 4.2's corner would have been, and (iii) the Jelonek asymptotic set
   `A(F)` (Avenue 7) and the one-place objects of Avenue 6.  §2 *types* all
   three into the same stratum and removes it from `T_a^+`.  Avenue 6's
   recorded stuck-point is literally "place data are unpinned"; `L5-exact`
   pins them.  Avenue 6 is a **reopen**.
6. **GGV finite lane.**  The 106-by-105 rank-drop variety does **not** need a
   maximal-minor Groebner computation.  A 106-by-105 matrix has exactly
   `C(106,105) = 106` maximal minors, and they are the entries of the *unique
   left-kernel vector*.  One exact nullspace solve plus one 105-by-105
   determinant replaces 106 determinants; see §6 for the target and gate.

---

## 1. Answers to the packet's seven questions

### 1.1 Q1 — first exact unproved implication on the shortest pure-Sigray route

**Answer: `landing`, but with a nearer and cheaper obligation — an unaudited
source block — that must be discharged first.  It is not decoration, not
`RPMC(C)`, not type control, not cofinality, and it is no longer Prop. 4.2.**

Walking the chain of `ladder/REDUCTION.md` in order, with §2 and §3 of this
report applied:

| step | status after this round |
|---|---|
| T1 predicate | not a gap, a wording fix (`REDUCTION` CRITICAL 1) |
| T2/T3 GGV selection | **bypassed** by a pure architecture (that is the definition of pure) |
| T4 normalization (Lem 2.1) | `VERIFIED_WITH_NIT`; residual is a *reference* debt (`[A,18.13]`, `[A,19.2]` not in `refs/`), not a proof debt |
| T5 `td>=6` | external ledger |
| T6 tree/sheet data | H5a forced by St. 3.8; H5b still a convention |
| Prop. 4.2 + Remark | **CLOSED** (promoted erratum + §2 below) |
| L3/L4/L5-exact | **CLOSED** for a normalized rectangle/NE-corner fibre |
| St. 3.14(ii), Prop. 5.4 q-half, St. 6.2 | GAPs *with verified repairs supplied in the audit*; they are filing debt |
| Prop. 5.8 any-`a` | replaced (`SOL-PROP58` + Chau Thm 4.4 + the `g|_Gamma` nonconstancy line supplied in T7) |
| Prop. 5.1 finite nonzero puncture | **bypassable**, with the reason in §1.4 |
| **Notation 8.1 / Prop. 8.4 / Notation 9.1** | **NEVER AUDITED** — first unproved-in-fact implication |
| T9/T10 landing | **NOT ESTABLISHED** — first unproved-in-architecture implication |

So the correct disposition is a **two-item answer**:

- **First exact unproved implication, source-audit category:**
  `Notation 8.1`'s `M_F`/`M_F^*` definition and `Proposition 8.4`'s
  single-pole exclusion mechanism.  `REDUCTION` T7 states that `M_F = b_F`
  "specifically uses ... Notation 8.1"; T9(a) states that the prime-`d`
  single-pole kill "assumes ... Proposition 8.4".  Both are inside the
  `SHEET6-TEMPLATE` trust perimeter and outside the 72-item census.  The
  census covers pp. 7–30; Notation 8.1 is p. 39, Prop. 8.4 is p. 44,
  Notation 9.1 is p. 48.  **The promoted prime-`td` theorem therefore rests on
  a completely unaudited page range.**  My §3 finding is direct evidence that
  audits of this source find real defects at a nontrivial rate (18 of 72 items
  are ERRATUM/KNOWN_ERRATUM/GAP; that is a 25% defect rate, and the two
  KNOWN_ERRATUM entries were found by the campaign, not by the author).
  Extrapolating 25% onto ~40 unaudited items in §§7–9 predicts about ten
  defects sitting under promoted results.
- **First exact unproved implication, architectural category:** `landing`
  (`REDUCTION` CRITICAL 4): there is no defined `B(d,E)`, no total map, no
  coverage certificate.  This dominates `RPMC(C)`, type control and
  cofinality, all of which are consumers of a landing record that does not
  exist.

**Prop. 5.1 finite-nonzero puncture: BYPASSABLE.**  Proof of bypassability, not
opinion — see §1.4.

### 1.2 Q2 — can the terminal certificate + orbit law + corrected tower compose into a new global bound?

**Mostly `NO HIT`, with one interface that is worth exactly one lane and one
explicit warning that a tempting composition is already known to be vacuous.**

*Warning first, because it saves a lane.*  The obvious composition is
Riemann–Hurwitz for `g|` on the normalized fibre plus the puncture count now
pinned by `L5-exact`:

```text
deg( g|_{Cbar_a^nu} ) = d            (Prop 5.8 / SOL-PROP58 + Chau 4.4)
2 g_a - 2 = -2d + R_a                (Riemann-Hurwitz, char 0, per fibre,
                                      summing components: sum_i d_{a,i} = d)
chi(C_a)  = 2 - 2 g_a - n_a
=>          chi(C_a) = 2d - R_a - n_a          (*)
```

`(*)` is correct (I checked it on `f=x, g=y`: `d=1, R=0, n=1, chi(A^1)=1`).  It
is also **useless as a bound**, and the repository already knows why in a
different dress: `ladder/SHEET6-CLASSICAL.md` §1c runs the genus balance
(tree side vs fibration side) and reports that "the two sides agree
IDENTICALLY: every unpinned symbol cancels"; `APPROACHES.md` Avenue 28 records
the Euler/genus ledger as "the predicted non-result".  Feeding `(*)` into
Suzuki's `sum_a lambda_a = 1 - chi(C_gen)` reproduces `2d = 1 + w_gen - sum_a
lambda_a` with `w = n + R`, which is the identity again.  **Do not spend a lane
re-deriving this.**  Sigray's own Prop. 7.5 identity (22) is the same Euler
computation done correctly, and it is already the campaign's budget.

*The one interface that is not vacuous.*  What `L5-exact` newly supplies is not
`n_a` (a count) but the **exact rescaling** `ord_t = (kappa/e_S) ord_S` and the
node-evaluable terminal `(h, chart, kappa, F)` with `deg p_{h,F} = 1`.  That is
a *semigroup* datum, not an Euler datum.  Literal interface:

```text
INTERFACE  PLACE-SEMIGROUP-MASS  (proposed, not proved)

Input   1.  L5-exact: for a normalized fibre f = a, terminal deck orbits
            biject normalized boundary places; orbit size e_S,
            stabilizer kappa/e_S, ord_t = (kappa/e_S) . ord_S.
        2.  T7 mass law: d = sum_{F in T_{a,pole}} Lambda(F),
            Lambda(F) = a_F b_F alpha beta / nu_F,  Lambda(F) >= beta >= 3.
        3.  Section 2 (this report): d_{g,F} > 0 for every F in T_a^+
            carrying a nonempty Prop. 4.2 tower.

Claim   For each boundary place S over a pole vertex F, the value semigroup
        Gamma_S of O_S under (ord_S f, ord_S g) is generated by the
        characteristic data (kappa_F, beta_1..beta_m) of F, and the
        conductor c(Gamma_S) is a Z-linear function of the entry datum
        e_F = (Lambda_F, a_F, b_F, nu_F).

Output  sum_{S} c(Gamma_S) is an entry-menu-computable integer, so
        Abhyankar-Moh/semigroup one-place obstructions become finite
        arithmetic tests on the *entry menu* rather than on configurations.

Missing input (the whole content):  the conductor-to-entry dictionary.  This
is exactly Avenue 6's "place data are unpinned", which L5-exact removes.
```

This is a `HIT` only in the weak sense that it is now *well-typed*; it is not a
bound yet.  I rank it below §6 and §5.

### 1.3 Q3 — which source item next, for maximum fanout

**None of the five offered.  The packet's Q3 menu is mis-specified.**  It lists
Prop. 5.1, the Prop. 5.4 repair, St. 6.2, Props. 6.3–6.8, Sections 7–9 — and
omits both of the audit's own Tier-1 highest-fanout items (Prop. 5.8's
`a`-uniformity and the Not. 3.5/H5a + St. 3.8 `kappa_F` convention).  It also
treats "Sections 7–9" as one menu entry co-equal with a single proposition,
when §§7–9 is the *only unaudited block* and is consumed by two promoted
theorems.

Cheapest decisive triad, ranked by (fanout x fragility) / cost:

| rank | target | proof route | refutation route | bypass route |
|---|---|---|---|---|
| **1** | **Notation 8.1 + Prop. 8.4 + Notation 9.1 (pp. 39, 44, 48)** | re-derive `M_F = gcd(M_F^*, ...)` and the 8.4 exclusion inside the corrected §§3–6 apparatus | randomized exact chart fuzzer (§5) with hypothesis ablation, as in §3 | none — T7's `M_F=b_F` and T9(a)'s prime theorem both die without it |
| 2 | St. 6.2 "in particular" | add `H in V_a cap T_a^+` (audit already has the repair) | already has an explicit counterconfiguration | weaken to the inequality everywhere it is used |
| 3 | Prop. 5.4 q-half | audit's supplied repair, banked with `alpha>=2` | `alpha=1` counterexamples already exist | none: St. 5.2(ii)'s `nu`-menu is consumed verbatim by the promoted prime theorem |
| 4 | Props. 6.3–6.8 | cheap, short section | fuzzer | — |
| 5 | Prop. 5.1 finite punctures | audit's forced `b = g(P)` | — | **bypassed**, see §1.4 |

The reason rank 1 beats everything is not proximity, it is **exposure**:
Prop. 8.4 is the *only* mechanism that kills anything in the single-pole
sector, and it has never been read adversarially.

### 1.4 Q4 — direct intrinsic route to landing/`RPMC(C)`; GGV facts discharging pure-tree hypotheses

**Direction A (intrinsic -> landing): partial YES, and it is the best available
use of `L5-exact`.**  `CRITICAL 4` asks for five things.  `L5-exact` supplies
items (2) and (5) at the *leaf* level, and nothing else:

```text
(1) a precise object B(d,E)                       NOT supplied
(2) a deterministic configuration -> record map    SUPPLIED at leaf level:
        the terminal record (h, chart, kappa, F) with deg p_{h,F} = 1 is
        node-evaluable, so "am I a leaf?" is decidable at the node
(3) termination / totality                        NOT supplied
(4) branch/entry/context preservation             NOT supplied
(5) fail-closed coverage certificate              SUPPLIED at leaf level:
        a node without the deg p = 1 certificate is *typed* as an ancestor
        cluster and cannot silently enter a place sum
```

That is a real deliverable: the landing compiler can be given a **decidable
leaf predicate and a fail-closed non-leaf type** today, which is precisely what
`REDUCTION` §5.1 asks for ("mark any unknown transition `OPEN`").  It does not
give `RPMC(C)`, which is downstream of the full-configuration record.

**Direction B (GGV -> pure tree): NO.**  I checked the three candidates and all
three fail on typing, not on strength:

- the reviewed `A|V0` / unit-root endpoint theorems are statements about a
  *fixed frozen raw window* on branch P; they have no fibre, no place, and no
  `kappa`.  `REDUCTION` CRITICAL 3 records that live `CornerData` has no
  coefficient field, polynomial pair, fibre, face root, deck action or ring
  map.  Nothing can be discharged from an object with no fibre into a theorem
  quantified over fibres.
- the `v_7 = 0` separation is explicitly refuted as a full branch-P statement
  (`AUDIT`/memory: compatible point `a=b=1, v_7=-14rho`).
- the transpose discriminator proves the *opposite* of what a discharge would
  need: the two source theories' pair-sign conditions are mutually exclusive
  for the same fixed pair.

**Do not let a GGV endpoint theorem be cited as a pure-route hypothesis
discharge.**  That is the `G2-PSC` error with a new coat of paint.

### 1.5 Q5 — fastest exact discriminators in the GGV finite lane

**(a) quadratic-Q rank-drop variety.**  Stop computing "the maximal-minor
ideal" as if it were large.  A `106 x 105` matrix `M` of rank 105 has exactly
`C(106,105) = 106` maximal minors, and by Cramer they are, up to one global
sign pattern, the entries of the **unique left-kernel vector** `lambda` with
`lambda^T M = 0`:

```text
COST NOW      106 determinants of size 105 over Q(q0,q1,q2,c4,c6,c8)
COST INSTEAD  1 nullspace solve of a 105 x 105 system  +  1 determinant
              (to fix the global scale), then clear content.
              rank-drop variety = V( content-cleared entries of lambda ),
              up to saturation by the pivot denominators.
```

Gate: verify `lambda^T M == 0` identically over the function field, verify
`lambda != 0`, and independently recompute **two** entries as honest
105-by-105 determinants and compare against `lambda_i / lambda_j`.  Stop
condition: if the content-cleared entries generate the unit ideal after
saturating by the pivot denominators, the whole quadratic-Q even face is closed
**universally**, not generically, and `e/F8`/even tails may be released.  If
not, decompose and run the endpoint on each component's kernel.
The report's own listed specialization ranks (`c8=0: 104`, `q1=0: 101`,
`q1=q2=0: 99`) are then recovered as *checks* on the decomposition, not as
separate jobs.

Note the packet's own trap: `q1=0` elimination introduced the denominator
`(6144 c6 - 5(q0+q2)^2)(6144 c6 - 5(q0-q2)^2)`.  In the `lambda` route those
factors appear as *content*, where they are visible and auditable, instead of
as invisible pivot inversions.

**(b) lambda-nonzero raw windows.**  The packet says orders four and five
cancel and warns that the face expansion may be "repackaging the determinant
cascade".  **Stop incrementing the order.**  Prove or refute the repackaging in
one bounded test:

```text
REDUNDANCY TEST.  With the normalized expansion Fbar = L^4 + eps L^3 J
+ eps^2 L H + ... at a simple root, the relative-order-n polar coefficient is
a fixed universal polynomial P_n in (J, H, C3, J1, c2, tau).  Build the
transition matrix T of the recursion P_{n+1} = T . P_n on the finite mode
basis, and test whether the D-row numerator ideal I_D (D12/D14 rows) is
T-invariant.
  T-invariant  ==> every higher face residue lies in I_D: the whole face
                   expansion is redundant, PROVED, at every order at once.
  not invariant ==> the first n with P_n not in I_D is the first genuine new
                   cut, and it is named before it is computed.
```

This is a rank/ideal-membership test on a *fixed finite* basis, not another
order-`n` grind, and it terminates either way.  It is the single highest-value
GGV item in this round.

**AWS targets and stop conditions:** one core each, zero swap, 1800 s inner
cap.  (a) exact `lambda` over `Q(q0,q1,q2,c4,c6,c8)`; stop at unit ideal or at
a decomposed component list.  (b) `T`-invariance of `I_D`; stop at
`INVARIANT` or at the first named `n`.  Neither is a duplicate of the four
live arbitrary-Q variants; both must be preflighted against the frozen
`b2e67b16...` archive.

### 1.6 Q6 — under-resourced counterexample avenue

**Avenue 7 / Avenue 6, jointly, as a *constructor*.**  The recorded stuck-points
are "computing `A(F)` is the compactification problem again" (7) and "place
data are unpinned" (6).  `L5-exact` removes the second, and §2 of this report
removes the search space by half: **`A(F)`-relevant places cannot live in
`T_a^+`.**  They are `T_a^0` (cv) objects.  That converts an unbounded hunt into
a bounded one.

The packet asks for two specific things.  Both now have a named mechanism:

- **A source-complete, all-depth, bounded-support family.**  Take the cv-vertex
  stratum `T_a^0`, prescribe the characteristic data `(kappa_F, beta_1..beta_m)`
  at each cv vertex subject to Sigray's own budget
  `td - 1 = sum kappa_F(pi(F)-1) + sum delta` (Prop. 7.5 (22)), and *build
  outward*.  This is source-complete by construction because the budget is an
  identity, and all-depth because the terminal certificate decides
  leaf-vs-ancestor at every node.
- **A characteristic-zero algebraization/collision mechanism.**  This is the
  new one.  `L5-exact` says a terminal record continues **uniquely by Hensel**
  on the shifted `t`-cleared equation.  Therefore a *bounded-support terminal
  prefix determines its whole branch*.  Avenue 4's recorded stuck-point is the
  chain "modular nonempty != germ != char-0 != polynomial".  A `deg p = 1`
  certificate **kills the first two arrows**: a certified terminal over `Q` is a
  genuine char-0 place with a finite determining datum.  It does not kill the
  third (germ -> polynomial still needs toric closure).  A *collision* is then a
  pair of terminals with equal `(f,g)`-value data and distinct places, and
  because both are Hensel-determined, checking a collision is a **finite**
  coefficient match rather than a limit argument.

I explicitly do **not** claim this yields a counterexample.  It converts an
infinite-depth search into a finite-datum search, which is the missing
ingredient the packet names.  Formal or modular survival still proves nothing;
the gate is the `deg p = 1` certificate over `Q`, not over `F_p`.

### 1.7 Q7 — theorem-interface composition pass and a new mechanism

Composition pass across the portfolio, keeping only arrows that type-check:

```text
L5-exact (place/orbit law, terminal certificate)
   --> Avenue 6  (one-place objects: place data now pinned)          REOPEN
   --> Avenue 7  (A(F) components typed into T_a^0)                  RAISE
   --> Avenue 4  (formal germ -> char-0 germ arrow supplied)         RAISE
   --> Avenue 31 (Rees valuations get an exact ord_S input)          RAISE
   --> landing   (decidable leaf predicate + fail-closed non-leaf)   PARTIAL

Prop 4.2 repaired + Sec.2 corner theorem
   --> (7) free on T_a^+ where d_{g,F} >= 0                          NEW
   --> Prop 5.1 finite-puncture gap provably dormant on T_a^+        NEW
   --> Prop 5.3(ii)/(viii), 5.2, 4.4 clause, 6.2/6.3 typed           (Facts A/B)

Sec.3 (St 3.9 kappa is h-dependent)
   --> Fact A on tower members h_j needs kappa-enlargement           NEW DEBT
   --> Prop 4.4's proof for general h needs the same                 NEW DEBT

GGV upper endpoint theorems  --X-->  pure Sigray hypotheses          BLOCKED
   (no fibre, no place, no kappa in CornerData: CRITICAL 3)
```

**The genuinely new mechanism is §5: adversarial exact fuzzing of a source
statement with hypothesis ablation.**  It is not "run more checks"; it is a
specific and, on this round's evidence, unusually productive protocol.  See §5.

---

## 2. NEW THEOREM — no constant corner at index 0 on `T_a^+`

This closes the residual gap that the promoted Prop. 4.2 erratum leaves open.
My earlier review (`47f2b608...`) states at §7.4: *"Item 1 (the Remark) is
**not** repaired by anything here.  It must be deleted and (7) carried as a
hypothesis where used ... or proved separately."*  This section proves it
separately.

**Setting.**  Normalized Keller pair `(f,g)`, `J(f,g)=1`, `a in C`, Sigray tree
`T_a` with roots `(0,y)` (component `T_{a,y}`) and `(0,x)` (component
`T_{a,x}`).  `T_a^+ = {F : d_F > 0}`, `d_F := d_{f,F}`.  Prop. 4.2 tower at
`F in T_a^+` uses `h_0 = g`, data `(k_j,l_j,s_j)`, length `m_F`,
`delta_j := kappa(d_F + d_{h_j,F} - alpha_j d_F - 1 + u)`, `alpha_0 = 0`,
`u := pi(F)`.  Under the erratum, `l_j = 0` occurs only in the unique terminal
form `(k,l,s) = (1,0,c)`.

> **Theorem C.**  For every `F in T_a^+`, `g^+_F` is not a nonzero constant.
> Equivalently, `l_0 >= 1`: no Prop. 4.2 corner occurs at index `j = 0`.

**Proof.**  Suppose `g^+_F = s in C*` at some `F in T_a^+`; then
`d_{g,F} = 0`, `deg p_{g,F} = 0`, and the corner is terminal at index 0, so
`m_F = 1` and `delta_0(F) > 0`.

By Fact B (promoted erratum item (g)), `h^+_{(0,y)} = xi^{deg_x h} .
(leading x-coefficient of h)` is a nonzero constant iff `h` is a nonzero
constant; `g` is nonconstant, so `F` is not a root vertex.  Let `F^0` be its
parent, `F = F^0 * c`, `pi(F) = pi(F^0) + 1/kappa`.

1. *The parent inherits `d_g = 0`.*  St. 3.9(i) gives
   `mult(p_{g,F^0}, c) = deg p_{g,F} = 0`; St. 3.9(iii) then gives
   `d_{g,F^0} = d_{g,F} - 0 = 0`.
2. *The parent is in `T_a^+`.*  St. 3.9(iii) for `h = f` gives
   `d_F = d_{F^0} - mu_f/kappa` with `mu_f := mult(p_{f,F^0},c) >= 0`, so
   `d_{F^0} >= d_F > 0`.
3. *`mu_f >= 1`.*  St. 3.18: if `F^0 * c` exists then `c` is a root of
   `p_{F^0} = p_{f,F^0}`.  (This half of St. 3.18 is true as printed; the
   filed erratum concerns only the dropped `epsilon`.)
4. *The parent's tower is nonempty.*  With `mu_g := mult(p_{g,F^0},c) = 0`
   from step 1 and `alpha_0 = 0`,

   ```text
   delta_0(F) - delta_0(F^0)
       = kappa[ (d_F - d_{F^0}) + (d_{g,F} - d_{g,F^0}) + 1/kappa ]
       = 1 - mu_f - mu_g  =  1 - mu_f  <= 0.
   ```

   Hence `delta_0(F^0) = delta_0(F) + mu_f - 1 >= delta_0(F) > 0`, so
   `m_{F^0} >= 1`.  In particular Fact A's escape branch ("the `F^0`-tower has
   already stopped") **cannot occur here**.
5. *The parent has the same corner.*  `m_{F^0} >= 1` and `m_F >= 1`, so by
   Prop. 4.4's "In particular" clause — repaired by Fact A, and applicable
   because both towers are nonempty — the two towers share their first step.
   `F`'s first step is `(1,0,s)`, so `F^0`'s is too, i.e. `g^+_{F^0} = s`.
6. *Induct.*  Steps 1–5 apply verbatim at `F^0`.  The ancestor chain is finite
   and terminates at `(0,y)` or `(0,x)`, contradicting Fact B.  QED

**What Theorem C buys.**  For `F in T_a^+`:

```text
d_{g,F} > 0            (7) holds for every b in C          [m_F >= 1 case]
d_{g,F} = 0, p nonconst (g-b)^+_F = p_{g,F}(eta) - b nonconst: (7) holds
d_{g,F} = 0, p const    EXCLUDED BY THEOREM C
d_{g,F} < 0            (g-b)^+_F = -b: (7) FAILS for b != 0, holds for b = 0
```

and the last row forces `m_F = 0` (if `m_F >= 1` then
`k_0 d_{g,F} = l_0 d_F` with `d_F > 0` and, by Theorem C, `l_0 >= 1`, so
`d_{g,F} > 0`).  Therefore:

> **Corollary C1.**  Condition (7) holds at every `F in T_a^+` for `b = 0`
> unconditionally, and for every `b in C` whenever `d_{g,F} >= 0`.  The p. 20
> Remark's conclusion is therefore **true**, not circular, on the whole of
> `T_a^+` except the residual sliver `{ m_F = 0 and d_{g,F} < 0 }`.

> **Corollary C2 (the sliver is deep).**  Along a ray of `N` edges from the
> root, `d_{f,F} = k_f - (1/kappa) sum mu_f`, `d_{g,F} = k_g - (1/kappa) sum
> mu_g`, `u = N/kappa`, and `delta_0 = kappa(k_f + k_g - 1) - sum(mu_f + mu_g
> - 1)`.  Combining `d_{f,F} > 0`, `delta_0 = 0` and `d_{g,F} < 0` gives
> `N > kappa`, i.e. **`pi(F) > 1`**.  So the sliver, if nonempty, is confined
> to the same depth regime `pi(F) > 1` in which `LROOT` places the cv vertices.

**Erratum consequence.**  Item (f) of the promoted repair
(`47f2b608...` §9) should be restated:

```text
(f) [REVISED]  Delete the p. 20 Remark's PROOF, which is circular, and
    restore its statement as a corollary of Prop. 4.4 + Prop. 4.5 + Fact A
    + Fact B by the delta_0 edge identity above.  Condition (7) then need
    NOT be carried as a hypothesis in Props. 4.1, 4.6, 6.2 on T_a^+ except
    on the residual sliver { m_F = 0, d_{g,F} < 0, pi(F) > 1 }, which must be
    named explicitly.  Prop. 4.3 (T_a^-) is untouched: there (7) remains a
    genuine hypothesis on b.
```

**Verification.**  Checker `opus5_1149Z_check.py`, SHA-256
`5893a14a54844ce97069276958c12aca9e87b96c020176400e91b80d129ac143`, CPython,
standard library, exact `Fraction`s, ~7 s.  It implements Notation 3.9/3.10
literally and checks, on 11,349 exact random parent/child pairs with `kappa`
satisfying Prop. 3.1's hypothesis:

```text
St 3.9(i)   mult(p_{h,F},c) = deg p_{h,F*c}                     PASS
St 3.9(iii) d_{h,F*c} = d_{h,F} - mult/kappa                    PASS
MON         d_{h,F*c} <= d_{h,F}   (ancestors of T_a^+ in T_a^+) PASS
DELTA       delta_0(F*c) - delta_0(F) = 1 - mu_f - mu_g          PASS
CORNER      434 non-vacuous corner children; each has mu_g = 0,
            d_{g,parent} = 0, delta_0(parent) = delta_0(child) + mu_f - 1 PASS
FACT B      5,857 trials                                         PASS
KAPPA       negative control breaks as predicted (see Sec. 3)    PASS
```

**Firewall.**  Theorem C is a statement about Prop. 4.2 towers on `T_a^+` for a
normalized pair.  It is not a landing theorem, not `RPMC(C)`, not a degree
bound, not a Keller contradiction, and not JC2.  It rests on the promoted
Facts A/B, which were authored by this same model — see §10.

---

## 3. NEW SOURCE DEFECT — Statement 3.9's `kappa` hypothesis is `h`-dependent

`ladder/SIGRAY-AUDIT.md` currently rates St. 3.9 `VERIFIED_WITH_NIT` with
"the one-line printed argument is sound".  The printed argument controls only
terms of the *same* `eta`-degree.  The statement is rescued by its hypothesis
"`kappa in N*` is suitable **and has the property of Proposition 3.1**", and
Prop. 3.1's property is *"`kappa` is a multiple of any order of `x`-pole"* — of
the curve `h = 0`, i.e. a condition on the **auxiliary polynomial `h`**, not on
the fibre `f - a`.

**Exact failure at `kappa = 1`** (reproduced by the checker's `KAPPA` block):

```text
f = xy,  a = 1  (root y = x^{-1}; the truncation (0,y)*0 is a genuine edge)
F = (0,y),  c = 0,  kappa = 1
h = -2 y^3 + 4 x y + 2 x y^3 - x^2 y^3
  = -y ( x^2 y^2 - 2 x y^2 + 2 y^2 - 4 x )

h^F  = -eta^3 + ... ,  d_{h,F} = 2,  p_{h,F} = -eta^3,  mult(p_{h,F},0) = 3
h^{F*0} = -2 eta^3 xi^{-3} + 2 eta^3 xi^{-2} - eta^3 xi^{-1} + 4 eta
       => d_{h,F*0} = 0,  p_{h,F*0} = 4 eta,  deg = 1

St 3.9(i)   predicts deg = 3   ACTUAL 1     FAILS
St 3.9(iii) predicts d   = -1  ACTUAL 0     FAILS
```

Cause: the second factor has `y ~ +-2 x^{-1/2}` at infinity, an `x`-pole of
order 2, so `kappa = 1` violates Prop. 3.1's hypothesis for this `h`.  With
`kappa` a multiple of every `x`-pole order of `h`, all 11,349 trials pass.

**Why this is load-bearing and not a nit.**

- **Fact A is applied to tower members `h_j`.**  `h_j` is produced by the
  Prop. 4.2 recursion, so its `x`-pole orders are *not* controlled by any
  `kappa` chosen for `f - a` at the start.  The erratum's Fact A must carry
  "enlarge `kappa` to a common multiple of the `x`-pole orders of `h_j`".
- **Prop. 4.4's printed proof** quantifies over "a polynomial `h(x,y)`" and
  applies St. 3.9 to it.  Same debt.
- **Enlarging `kappa` is not free**: `F * c` is defined in the printed proof by
  `eta_G = x^{1/kappa}(eta_F - c)`, so the *edge* depends on `kappa`.  The
  erratum must therefore either (i) fix one `kappa` up front that is a common
  multiple of the `x`-pole orders of `f-a`, `g`, and every `h_j` in every tower
  (finitely many, since towers are finite and `T_a` is finite), or (ii) prove
  a compatibility lemma.  Option (i) is available and cheap; it just has to be
  *written*.

**Proposed audit change:** `St 3.9` moves `VERIFIED_WITH_NIT ->
VERIFIED_WITH_NIT (hypothesis-critical)`, with a new rider: *"Prop. 3.1's
`kappa`-property is a condition on the auxiliary `h`; explicit failure at
`kappa=1` recorded.  Every consumer with a derived `h` must state its
`kappa`-enlargement."*  Census counts are unchanged.  Theorem C itself is
**unaffected**: it applies St. 3.9 only to `h in {f, g}`, both fixed at the
start, so one initial `kappa` suffices.

---

## 4. Disposition vector, avenues 1–46

Format: `n: label` (+ reason for every change).  `G2-PSC` and `G2-BD` are kept
distinct and are *not* avenues; they are obligations inside Avenue 2.

**Changed (8):**

- **1 GGV corner families / degree farm — `lower`.**  Not because it stopped
  producing: because its marginal information per wall-clock hour fell.  The
  packet itself routes away from face-order increments ("repackaging the
  determinant cascade"); the arbitrary-Q serial order timed out with no
  marker; the lambda-1 compiler timed out; the surviving targets are rank-drop
  varieties, which §1.5(a) shows are far cheaper than the lane has been
  pricing them.  Keep two focused jobs (§1.5), retire breadth.
- **2 Sheet ladder / Sigray–Orevkov — `raise`.**  L3/L4/L5-exact, Prop. 4.2,
  and Theorem C removed three source obligations in one day.  The raise is
  *with relocation*: the bottleneck moved out of §§2–6 into the unaudited
  §§7–9 block and into landing.  This remains the only avenue with a
  credible path to JC2.
- **4 Formal-germ certification + algebraization — `raise`.**  `L5-exact`'s
  `deg p = 1` terminal certificate supplies the missing
  `formal germ -> char-0 germ` arrow (two of the three arrows in its recorded
  stuck-point).  Germ -> polynomial still open.
- **6 Abhyankar–Moh one-place / coordinate recognition — `reopen`.**  Its
  recorded stuck-point is verbatim *"correct one-place objects are `A(F)`
  components, whose place data are unpinned"*.  `L5-exact` pins place data
  exactly (orbit `e_S`, stabilizer `kappa/e_S`, `ord_t = (kappa/e_S) ord_S`).
  Reopen at the "place semigroups of asymptotic-set components" reading only;
  the old fibre-based attempt stays refuted as a category error.
- **7 Nonproperness / Jelonek `A(F)` — `raise`.**  Theorem C proves
  `A(F)`-relevant places cannot sit in `T_a^+`, halving the search space and
  identifying them with the `T_a^0` cv stratum that already carries Sigray's
  own Prop. 7.5 budget.  This is the first time `A(F)` has had a *bounded*
  home in the tree.
- **16 D-module / holonomic index — `lower`.**  Two reasons.  (a) HENS-CT
  passed its upstream gate but timed out in
  `annihilator_of_composition` before creative telescoping, and is stopped
  pending a backend redesign; there is no client.  (b) A naming disclosure:
  the campaign overlays use "Avenues 1/16" for the D-finite gate-transport
  lane, whereas the master table's Avenue 16 is "D-module / holonomic index,
  Fable unique find, no concrete invariant named".  Under either reading the
  disposition is `lower`.
- **31 Integrality / ZMT / Rees valuations — `raise`.**  Its scored proposal is
  "Rees valuations of one complete boundary book"; `L5-exact` is the first
  time the book supplies exact `ord_S` per place rather than raw cover orders.
  Small raise, cheap to test, and it is the natural consumer of §1.2's
  `PLACE-SEMIGROUP-MASS` interface.
- **34 2D tangent-sweep / pole removal — `lower`.**  Nothing this round moved
  it, and the S:7 sweep-ansatz score has now been outranked by three cheaper
  items in the same "novel mechanism" slot (§1.5(b), §5, §6).  Recording the
  demotion so the DISSENT does not silently re-inflate.

**Unchanged (38), grouped:**

- *Active but not repriced:* 3 (vertex-gap/strip ODEs), 5 (Jung–van der Kulk),
  8 (formal-inverse combinatorics), 9 (Lee–Li conjecture E), 13 (Dixmier
  DC(2)), 14 (End(A_1)/Zheglov), 25 (fibre monodromy/passports), 27
  (links at infinity/splice), 28 (log surfaces/BMY — the Euler/genus ledger is
  identity-like, confirmed again in §1.2; the vdDB `KEF-ONE-VERTEX`
  discriminator is already recorded in `APPROACHES` and does not change rank),
  32 (off-diagonal collision ideal), 36 (guided CE search), 46 (Lean/formal).
- *Explicitly do-not-raise, history is negative:* 26 (primitive monodromy —
  `sol-monodromy-td.md` `b8144631...` already ran the exact `td=6..9` census),
  35 (descent of dim>=3 CEs), 37 (finite-field census).
- *Dead / refuted, no change:* 11 (Mathieu/GMC/Zhao), 18 (graded/GIT — Shaska
  2026), 41 (naive scaling deformation), 42 (Markus–Yamabe), 44 (Moskowicz —
  refuted-as-proof), 23 (analytic global inverse), 24 (real JC/Pinchuk).
- *Low, untouched:* 10 (HC4 Hessian bridge), 12 (face isolation/p-adic
  multinomials), 15 (spectral surfaces), 17 (BCW/Druzkowski/Yagzhev — and the
  Matysiak audit `c5655b43...` explicitly must not rerank it), 19 (char-p +
  Witt), 20 (p-curvature formalism), 21 (p-adic injectivity/Hensel), 22
  (Diophantine/heights), 29 (LND/Hamiltonian completeness — scoped gate
  complete), 30 (affine-surface classification/ML), 33 (global symplectic
  exactness — `COSTUME`), 38 (tropical), 39 (cohomological cluster), 40
  (free-associative lift), 43 (Ritt decomposition), 45 (differential Galois).

Count check: 8 changed + 38 unchanged = 46.  `G2-PSC` and `G2-BD` are not
merged with each other and neither is merged into an avenue label.

---

## 5. Bottleneck reranking, new mechanism, and the two attacks

### 5.1 Three principal proof bottlenecks (reranked)

1. **Landing / coverage (`REDUCTION` CRITICAL 4–6).**  Unchanged at rank 1, but
   its *cost* dropped this round: `L5-exact` supplies a decidable leaf
   predicate and a fail-closed non-leaf type, which is two of the five
   `CRITICAL 4` requirements.  Previously rank 1 with no purchase; now rank 1
   with a foothold.
2. **The unaudited §§7–9 source block.**  *New entrant, straight to rank 2.*
   Prop. 8.4 is the only mechanism that kills anything in the single-pole
   sector and has never been read adversarially; Notation 8.1 defines the
   `M_F` that T7's `M_F = b_F` pin consumes; Notation 9.1 defines `Q(F)`.  A
   25% observed defect rate on pp. 7–30 makes this the highest
   expected-defect-per-hour target in the campaign.
3. **Cofinal `td`/complexity ceiling (`CRITICAL 7`).**  Demoted from 2 to 3 —
   not because it got easier, but because 1 and 2 now have concrete instruments
   and this still has none.  No cited result truncates `td`.

(Previously rank 2, "deep GGV upper endpoint `A|V0`", drops out of the proof
bottleneck list entirely: even a complete deep-locus exclusion needs 1–3
anyway, and the packet concedes the face lane is repackaging.)

### 5.2 Two principal disproof bottlenecks (reranked)

1. **A char-0 algebraization of a certified terminal.**  *Newly rank 1.*  With
   `L5-exact`, "modular nonempty" -> "char-0 germ" is now a finite check; the
   remaining arrow is germ -> polynomial (toric closure).  This is the only
   disproof bottleneck that got structurally smaller this round.
2. **A source-open, rank-exact K00/full-`P6` point plus prolongation.**  Demoted
   from 1 to 2: K00 full-`P6` capped `RESOURCE_CAP_NO_VERDICT`, and the
   compressed successor is still unfrozen.  Real, but stalled.

### 5.3 New mechanism (compared explicitly with repository history)

> **`SRC-FUZZ` — adversarial exact fuzzing of source statements with
> hypothesis ablation.**

Build a small exact evaluator for the source's *primitive objects* (here:
`eta_F`, `h^F`, `d_{h,F}`, `p_{h,F}`, `F * c`, `pi`, `mult`) and then, for each
printed statement, (a) sample exact random instances satisfying the printed
hypotheses and check the conclusion; (b) **ablate one hypothesis at a time and
check that the conclusion breaks**.  A hypothesis that can be ablated without
breaking anything is either redundant or, more usefully, *not being tested* —
which is the signature of an unstated dependence.

*Comparison with history.*  The repository already does heavy exact checking:
`SIGRAY-AUDIT.md` records "400-trial exact confirmation" (St 3.2), "20000-trial
exact sweep" (Not 3.4), "2988-tuple exact sweep" (St 5.2), "300k/82k-trial
exact sweeps" (Prop 6.2), "295-trial" (Prop 4.6).  Those are all **conclusion
sweeps under the printed hypotheses**.  I found no instance of *hypothesis
ablation* in the repository.  That difference is exactly what produced §3: the
printed hypothesis "`kappa` has the property of Proposition 3.1" is
`h`-dependent, a conclusion sweep with a correctly chosen `kappa` never sees
it, and a 72-item expert read-through rated the statement `VERIFIED_WITH_NIT`
with "the one-line printed argument is sound".  Ablating `kappa` broke it in
under a minute.

*Why it is not a generic brainstorm item.*  It has a measured hit rate on this
round: one new load-bearing defect (§3) and one closed gap (§2) in a single
lane, both from the same 250-line evaluator.

### 5.4 Strongest proof attack to run next

**Audit §§7–9 with `SRC-FUZZ`-first ordering: Notation 8.1, Prop. 8.4,
Notation 9.1, Props. 6.3–6.8.**  Extend the §2 evaluator with `M_F`, `M_F^*`,
`Q(F)` and the `T_a^searrow` descent, sample under the printed hypotheses,
then ablate each hypothesis.  Expected yield, from the observed pp. 7–30 rate:
~10 defects across ~40 items, of which the ones under Prop. 8.4 are the only
ones that can retract a **promoted** theorem (the prime-`td` single-pole kill).
This is cheaper than any live AWS job and can retract a promoted result, which
no live AWS job can.

### 5.5 Strongest counterexample/falsification attack to run next

**Certified-terminal collision search on `T_a^0`.**  Prescribe cv-vertex
characteristic data subject to Sigray's own Prop. 7.5 identity (22)
`td - 1 = sum kappa_F(pi(F)-1) + sum delta`; for each admissible assignment,
emit a `deg p = 1` terminal record; Hensel-continue it over `Q` (finite
datum, by `L5-exact`); and test whether two terminals share `(f,g)`-value data.
Falsification value is symmetric: an *empty* admissible set at small `td` is a
genuine `td`-exclusion by a route independent of the book machinery, and a
nonempty one is a bounded-support all-depth family of exactly the kind the
packet asks for.  Gate: reject any candidate whose terminal certificate is only
modular; the `deg p = 1` certificate must hold over `Q`.

---

## 6. One software acceleration / decisive experiment

> **`LEFT-KERNEL MINORS` — replace the quadratic-Q maximal-minor computation by
> one exact nullspace solve.**

- **Exact target.**  The frozen `106 x 105` matrix `M` of
  `0775a496.../83ab6c75...`, over `k = Q(q0,q1,q2,c4,c6,c8)`.  Compute the
  left-kernel vector `lambda` (1-dimensional, since `rank M = 105`), clear
  content, and output the ideal `I = (lambda_1,...,lambda_106)` together with
  the product `P` of pivot denominators.  Rank-drop variety `= V(I : P^inf)`.
- **Why it is a real acceleration.**  `C(106,105) = 106`, and Cramer makes the
  106 maximal minors the entries of `lambda` up to one global scale.  The
  current plan ("compute and decompose the 105-by-105 maximal-minor ideal")
  reads as 106 independent size-105 determinants over a 6-variable rational
  function field.  The nullspace route is one solve plus one determinant.
  Denominators that the report already saw appear as *content* rather than as
  invisible pivot inversions — the `q1=0` factor
  `(6144 c6 - 5(q0+q2)^2)(6144 c6 - 5(q0-q2)^2)` becomes auditable output.
- **Verification gate (fail-closed).**  (i) `lambda^T M == 0` identically over
  `k`; (ii) `lambda != 0`; (iii) two entries `lambda_i, lambda_j` recomputed as
  honest `105 x 105` determinants and checked against `lambda_i/lambda_j`;
  (iv) the four published specialization ranks (`c8=0:104`, `q1=0:101`,
  `q0=q2=0:104`, `q0=q1=0:101`, `q1=q2=0:99`) recovered as consequences of the
  decomposition.  Any gate failure ⇒ `NO VERDICT`, not a partial result.
- **Stop condition.**  `I : P^inf = (1)` ⇒ the quadratic-Q even face is closed
  **universally** and `e/F8`/even tails may be released.  Otherwise output the
  component list and stop; endpoint evaluation per component is a separate,
  separately gated job.
- **Cost.**  One core, zero swap, 1800 s inner cap, AWS-only.  Non-duplicate of
  the four live arbitrary-Q variants (different object: kernel of the frozen
  matrix, not a Groebner basis of the generator ideal).

---

## 7. Idea cards (three)

### Card A — `§§7–9 SOURCE FUZZ` (highest expected information per hour)

- **Dependencies:** `refs/sigray_full.pdf` (`9bf9f032...`); the §2 evaluator;
  the corrected §§3–6 apparatus (Facts A/B, Theorem C, the §3 `kappa` rider).
- **Licensed assumptions:** none beyond the corrected §§3–6 readings already
  promoted.  Explicitly *not* assumed: that Notation 8.1 or Prop. 8.4 is
  correct as printed.
- **Cheapest decisive discriminator:** hypothesis ablation on Prop. 8.4's
  `F in T_a^searrow cap V_a` and on Notation 8.1's `gcd` convention (which
  needs `gcd(n,0)=n` and emission of the terminal `h_m` — both introduced by
  the Prop. 4.2 erratum and never re-checked at 8.1).
- **Materially different outcomes:** (i) clean ⇒ the promoted prime-`td`
  theorem's perimeter is finally honest and landing is the sole wall;
  (ii) defect in Prop. 8.4 ⇒ the prime-`td` single-pole theorem is retracted
  and `REDUCTION` T9(a) loses its only kill; (iii) defect in Notation 8.1 ⇒
  `M_F = b_F` and hence T7's entry parameterization are retracted.
- **Stop/rollback:** stop at the first ERRATUM/GAP with a supplied repair;
  roll back only the results that cite the defective item.
- **Cost:** ~1 lane-day of reasoning + a few local CPU-minutes.  No AWS.
- **Expected information gain:** highest in the portfolio — it is the only
  cheap action that can *retract a promoted theorem*.

### Card B — `LEFT-KERNEL MINORS` (see §6)

- **Dependencies:** frozen `0775a496.../83ab6c75.../965024b9...`; exact linear
  algebra over `Q(q0,q1,q2,c4,c6,c8)`.
- **Licensed assumptions:** the fixed even face `A=X^4-1, S=U=0,
  e=F8=F10=F12=F14=0, c2=1`, quadratic `Q`; **no** `G16..G21`, **no** four-root
  system, **no** released even tail.  These are exactly the producer's.
- **Cheapest decisive discriminator:** `I : P^inf = (1)` or not.
- **Materially different outcomes:** universal closure of the quadratic-Q face
  (releases the even tail) vs. an explicit component list (each of which then
  gets one endpoint test on its kernel).
- **Stop/rollback:** any gate failure in §6 ⇒ `NO VERDICT`; do not report a
  partial rank.  Do not rerun the four live arbitrary-Q variants.
- **Cost:** one core, ≤1800 s, AWS.
- **Expected information gain:** high but bounded — it closes a *face*, not the
  branch.

### Card C — `CERTIFIED-TERMINAL COLLISION` (see §5.5)

- **Dependencies:** `L5-exact` (`5d219c53...`, checker `26e24ec...`); Sigray
  Prop. 7.5 identity (22) as transcribed in `SHEET6-LROOT.md`; Theorem C for
  the `T_a^+` exclusion.
- **Licensed assumptions:** normalized Lemma 2.1 rectangle/NE-corner fibre
  (mandatory — coverage is FALSE otherwise, `y - x^2` is the control); the
  `SOL-PROP58` replacement of Prop. 5.8 for the mass budget.
- **Cheapest decisive discriminator:** emptiness of the admissible cv-datum set
  at `td = 6`, which is a finite arithmetic enumeration under (22).
- **Materially different outcomes:** empty ⇒ a `td=6` exclusion by a route
  independent of the books, i.e. an *independent check* on the existing td6
  campaign; nonempty ⇒ the bounded-support all-depth family the packet asks
  for, with a finite Hensel datum per branch.
- **Stop/rollback:** reject any modular-only certificate; reject any terminal
  without `deg p = 1` over `Q`.  If (22)'s transcription is found defective by
  Card A, roll this card back entirely — it consumes §7 of the source.
- **Cost:** ~1 lane-day; local, exact, small.
- **Expected information gain:** medium-high, and it is the only card that can
  produce a counterexample rather than an exclusion.

---

## 8. Lane calls

| lane | call | reason |
|---|---|---|
| **pure Sigray / exact-pair** | **continue** | the only route to JC2; three obligations closed in one day; bottleneck relocated to §§7–9 + landing |
| **hybrid `G2-PSC`** | **stop** | the transpose theorem proves the same fixed pair cannot feed both source theories; `CornerData` has no fibre/place/`kappa`; nothing this round moved it, and §1.4 shows no GGV fact can discharge a pure hypothesis |
| **arbitrary-Q / rank-drop GGV** | **redesign** | redesign to §6's left-kernel route; do not relaunch the serial membership order or a fifth equivalent variant |
| **lambda-nonzero / raw-window GGV** | **redesign** | stop incrementing the face order; run §1.5(b)'s `T`-invariance redundancy test, which terminates either way |
| **LF40** | **continue** under existing custody | independent falsifier; the Box02 `std/dp` row-zero cap licenses no identical relaunch |
| **K00 / order-two / TD6** | **redesign** | full-`P6` capped `RESOURCE_CAP_NO_VERDICT`; a compressed successor must have its exact rank-open target and fail-closed stop frozen *before* launch |
| **D43** | **continue** under existing custody | long tail builder, non-duplicate, already registered |
| **Artin–Schreier** | **stop** as a lift route | the promoted maximum-eleven theorem plus Hensel noninjectivity force correction `y`-degree ≥ 12; the zero-tail section is review-confirmed raw-dead at `D22`.  Keep only as negative control |
| **HENS-CT** | **stop** pending structural backend redesign | timed out in `annihilator_of_composition` before CT; no client survives (see Avenue 16 `lower`).  Do not repeat the generic composition path |
| **external intelligence** | **continue** at current cadence | next broad sweep due 2026-08-29 05:24Z; Matysiak refuted-on-audit; vdDB is a bounded topology filter, not progress |

---

## 9. One likely-missed insight, and its cheapest test

> **The campaign has never checked whether the `SHEET6` promoted files actually
> satisfy the corrected readings they are said to use.**

`SIGRAY-AUDIT.md` §1–§2 records **three filing fixes** where a promoted file
quotes a *silently corrected* statement as "verbatim": `SHEET6-H3.md` §2a
(St. 3.12), `SHEET6-A2P-REVIEW.md` (St. 3.18), and `SHEET6-A3L1-REVIEW.md`:61
(the inverted Prop. 5.3(ii) ratio, quoted **unflagged**).  The audit treats
these as *filing* problems.  They are not: a file that believes it is quoting
the print, while actually using the corrected form, has an **untested
dependency direction**.  If any *other* promoted file used the *printed*
(false) form of the same statement, the two would silently disagree and the
disagreement would be invisible, because both cite the same statement number.

`REDUCTION.md` MEDIUM 1 says the same thing from the other side
("contradictory status prose is unsafe to cite"), and T7 already found one
live instance: `SOL-PROP58.md`'s header claims all review patches are
incorporated while N2 is absent from its body.

**Cheapest test (minutes, local, no CAS).**  For each of the 12 errata/known-
errata statements, grep every promoted `ladder/SHEET6-*.md` for the statement
number, extract the *quoted formula* at each hit, and machine-compare it
against both the printed form and the corrected form.  Output a three-column
table: `file : cites-printed / cites-corrected / cites-neither`.  Any file in
the "cites-printed" column for St. 3.13, St. 3.15, St. 3.18, Prop. 5.3(ii),
St. 3.11(ii) or Prop. 6.2 is consuming a false statement.  Any file in
"cites-neither" is paraphrasing and must be read by hand.

This is a pure text-and-grep task with an exact pass/fail per hit; it needs no
mathematics and it directly tests the integrity of the promotion ledger.  I did
not run it (it touches ~30 `ladder/` files and the round's scope is ideation),
but it is the cheapest high-value action in this report after §5.4.

---

## 10. Epistemic ledger

### 10.1 Proved / promoted facts I relied on

- Custody: all 23 hashes in packet §0 verified `[MATCH]`; `HEAD` `[MATCH]`.
- `L3/L4/L5-exact` for a normalized Lemma 2.1 rectangle/NE-corner fibre, with
  R1 (terminal typed as `(h,chart,kappa,F)`, `deg p_{h,F}=1`) and R2 (coverage
  is conditional on normalization; FALSE in general, `y-x^2` control).
- Prop. 4.2 globally repaired on `T_a^+`; terminal `(1,0,c)`;
  `deg p_terminal = (mu-1) deg p_F + 1`; corner in `T_a^nearrow`; Facts A and B.
- Sigray St. 3.9(i)(ii)(iii), St. 3.18 (the "c is a root of `p_F`" half),
  Prop. 4.4 (statement) and Prop. 4.5, all as printed and audited.
- `REDUCTION` T7 (entry menu, `SOL-PROP58` + Chau Thm 4.4 + the `g|_Gamma`
  nonconstancy line) and the CRITICAL 1–7 gap list.
- `sol-monodromy-td.md` `b8144631...`'s negative `td=6..9` monodromy census.

### 10.2 Provisional inputs (used, not leaned on)

- The generic quadratic-`Q` rank-105 theorem (`0775a496...`) — used only to
  *reprice* the follow-on computation in §6, never as a closure.
- The unit-`S` order-four/order-five cancellations (`874bcd98...`,
  `aa88f190...`) — treated as provisional exactly as the packet instructs; my
  §1.5(b) recommendation does not depend on their truth, only on the *pattern*
  they exhibit.
- 875-point quadratic-Q navigation grid — sampled evidence, used for nothing.

### 10.3 Conjectures I am stating as conjectures

- The `PLACE-SEMIGROUP-MASS` interface (§1.2): the conductor-to-entry-datum
  dictionary is **not proved**.
- The `T`-invariance redundancy test (§1.5(b)) is a *test design*; I do not
  claim to know its outcome.
- The extrapolated "~10 defects in §§7–9" is a rate extrapolation, not a
  theorem.
- Corollary C2's sliver `{m_F = 0, d_{g,F} < 0, pi(F) > 1}` is **not shown to
  be empty**.  I could not close it and say so.

### 10.4 Failed attempts (recorded in full)

1. **First checker run refuted St. 3.9 — incorrectly.**  With `kappa` sampled
   freely, 3 of 3,864 trials violated St. 3.9(i)/(iii).  I traced the failure
   to the omitted Prop. 3.1 `kappa`-hypothesis rather than reporting a
   refutation.  It became §3 (a hypothesis-criticality finding), not an
   erratum.  Recording this because the first reading was wrong.
2. **My `delta_0` edge identity was initially wrong.**  I first wrote
   `delta_0(child) - delta_0(parent) = 1 - mu_f`, which failed 48 of 5,655
   trials.  The correct general identity is `1 - mu_f - mu_g`; the corner case
   has `mu_g = 0` and recovers the original.  Theorem C step 4 uses the
   corrected form.
3. **I tried and failed to close condition (7) unconditionally on `T_a^+`.**
   The `m_F = 0, d_{g,F} < 0` sliver survives; Corollary C2 confines it to
   `pi(F) > 1` but does not empty it.
4. **I tried the Riemann–Hurwitz / Euler composition for a new global bound and
   it is vacuous** (§1.2).  I then found the repository already knew the
   mechanism class is identity-like (`SHEET6-CLASSICAL.md` §1c, Avenue 28's
   "predicted non-result"), so I am reporting it as a saved lane rather than a
   hit.

### 10.5 Hidden assumptions I am surfacing

- Theorem C step 6 assumes every `F in T_a` has a finite ancestor chain to
  `(0,y)` or `(0,x)` within its component (Notations 3.2/3.3/3.6, St. 3.3).
  This is standard in the source and audited, but it is an assumption.
- Theorem C uses `alpha_0 = 0` in `delta_0`, read off the printed
  Prop. 4.1/4.2 pairing.  If `alpha_0 != 0` in some convention, step 4's
  arithmetic changes.
- The corner is assumed terminal (`m_F = 1` when the corner is at `j = 0`),
  which is the erratum's own normalization, not the print.
- §6's claim that clearing content recovers the minor ideal is exact only up to
  saturation by the pivot denominators; gate (iii) exists precisely to catch a
  wrong global factor.

### 10.6 Checks run

`opus5_1149Z_check.py`, SHA-256
`5893a14a54844ce97069276958c12aca9e87b96c020176400e91b80d129ac143`, CPython,
standard library, exact `Fraction`s, ~7 s, exit 0.  Seeds `11491149` and
`31337`.  11,349 edge trials, 434 non-vacuous corner children, 5,857 Fact-B
trials, plus one deterministic `kappa`-ablation negative control that **breaks
as predicted**.  All pass.

**Write-scope disclosure:** the packet permits exactly one write, this report.
The checker therefore lives at `/tmp/op5check/opus5_1149Z_check.py` and is
**ephemeral**; it is not in the repository and is not a campaign artifact.  Its
full construction is described in §2 and §3 in enough detail to rebuild, and
its hash is pinned above.  A follower lane that wants it as a case artifact
must recreate it under a normal write authorization.

### 10.7 Contamination and independence

- **No peer `1149Z` response was read.**  Two filename-only listings were taken.
  The first (session start) showed only the packet and the four
  `*-prompt.md` files.  The second (after drafting, while confirming write
  scope) showed that `-fable5.md`, `-grok46.md` and `-sol-ultra.md` had been
  written in the interim.  **No `ideation-20260828T1149Z-*` file was opened,
  read, grepped or hashed except the packet and `-opus5-prompt.md`**, and no
  content of this report derives from a peer submission.  Because the peer
  files appeared only after this report's mathematics (§2, §3) and all seven
  answers were already drafted, the contamination risk is nil; I am recording
  the sequence rather than merely asserting the conclusion.
- **Real independence caveat, disclosed prominently.**  Two of the packet's
  load-bearing inputs — the exact-pair hostile review `5d219c53...` and the
  Prop. 4.2 hostile review `47f2b608...` — are attributed to **Opus 5, i.e.
  this model**.  Theorem C (§2) is built on Facts A and B, which come from
  `47f2b608...`.  This lane is therefore **not** a different-model check on
  those facts, and Theorem C inherits that dependency.  Under
  `COORDINATION.md`'s different-model promotion rule, **Theorem C must not be
  promoted on this report alone**; it needs hostile review by Fable 5, Grok46
  or Sol Ultra, who should attack step 4 (the `delta_0` identity and
  `alpha_0 = 0`) and step 5 (the applicability of Fact A when both towers are
  nonempty).  §3 is independent of that concern: it is a direct exact
  counterexample against the printed text.
- No AWS job, running process, or `jc2-lean` file was touched, listed or read.

### 10.8 Exact scope of every claim in this report

- **Theorem C** is about Prop. 4.2 towers with `h_0 = g` on `T_a^+` for a
  normalized Keller pair.  It is not landing, not `RPMC(C)`, not `G2-PSC`, not
  `G2-BD`, not a degree bound, not a Keller contradiction, not JC2.
- **§3** is about the printed hypotheses of Statement 3.9 and their consumers.
  It changes no conclusion of any promoted result; it names a missing clause.
- **§1.2's `(*)`** is correct and vacuous; no bound is claimed.
- **§1.5, §6** are computational designs with gates; no GGV result is claimed.
- **§5.5, Card C** propose a search; no counterexample is claimed, and none
  exists.
- The 25% defect-rate extrapolation is an estimate for prioritisation only.
- A model verdict is not mathematical evidence, including every verdict above.

---

**End of `opus5` submission, round `20260828T1149Z`.**
