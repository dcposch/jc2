# Fable 5 cross-pollination and adversarial synthesis — round `20260827T0635Z`

Date: 2026-08-27.  Author: Fable 5, equal-standing co-researcher, cross-poll
phase.  Written independently of the coordinator's synthesis.

Input custody: all seven SHA-256 values in the lane prompt were verified on
disk before reading (packet `8e140384…`, sol `05400316…`, fable5 `d1f60700…`,
grok `2c0fa61e…`, opus5 `0fbb4524…`, K00 honest-source design `9c5bf122…`,
symbol/Spencer design `a049794b…`).  The two post-snapshot reports are treated
as delta evidence only; no blind submission is retroactively altered — where
they supersede a blind claim I say so explicitly.

**Verdict tier of this report.**  Everything below is review/navigation tier.
New verification results are labelled `REPLAY-F5` (exact desk arithmetic from
hash-pinned bytes, script `/tmp/xreplay.py`, SHA-256
`05ff05db8d7171a853ef57d0cb7960659d12372f513fe3aaeb056ecdecf2ff36`, exact
`Fraction` arithmetic, seconds, no CAS).  Nothing here proves or disproves
Gate T, order two, maximum twelve, or JC2, and nothing is promoted by this
report alone.

---

## 0. Executive summary

1. **Opus5's two flagship exact claims both survive hostile replay.**  I
   independently reconstructed the 70 ordered-`a1` `rho=0` rows from the
   pinned V23 parser and the V28/V30/V33/V35 exports (all hashes re-verified)
   and confirmed: Theorem L exactly (minimum hitting set 22, maximum
   coordinate zero-section dimension exactly 43, `L43` kills all 51 rows and
   survives with `rho` free on grades 10–15), and the Theorem A cascade line
   by line including the Case B contradiction.  One attribution slip: the A2
   Pell-like relation `k*rs1^2=(96/5)*a1^2` comes from `Tg13_2`, not
   `Tg15_4`.  No hidden divisions beyond the declared `a1`, `ell1`, and
   constants in `2^a*3^b` (char 5 enters only through A2's `96/5`).
2. **Grok's Card B contains a genuine mathematical error.**  The displayed
   rewrite `a1^3*k = (5/72)a1*aa0*ac3 − … + (element of I_19)` is equivalent
   to asserting `φ19 ∈ I_19`, which is self-refuting: the dual kills
   `(I_19)_19` while `λ(φ19)=‖φ19‖² = 7855/6912 ≠ 0` (`REPLAY-F5`).  The rest
   of Grok's dual-transport machinery is sound after two repairs (§3).  A
   second Grok defect: the proposed negative control "`φ19 ≠ 0` at the V34
   point" is broken — `φ19` vanishes there identically.
3. **The V37 nonmemberships are now independently second-model verified in
   full** (`REPLAY-F5`): both selector lanes' duals are byte-identical, each
   dual annihilates *every* fixed-weight product of every row (complete check
   via divisor enumeration; all untouched products vanish on the dual's
   support automatically), and each takes its target to 1.  With the verified
   weight-homogeneity (weight = grade, `rho` weight 0 per the pinned parser),
   my §2 confirms Fable5's shape-floor lemma at raw row-ideal scope.
4. **The K00 correction restructures the receiver lane.**  `Phi7` answers the
   blind round's "first honest equation at K00" question — nonzero on the
   literal section, with the explicit unit certificates (5.6) — and the live
   question is now the closure-first incidence `H_K00` of (7.3), whose
   ordering (saturate, then boundary, then core, then localize) I audited and
   endorse, including the `(x−Λm)` noncommutation control.  Nobody in the
   blind round made the false `J1=J2=0 ⟹ empty fibre` claim; Grok's
   Proj-versus-`V(I)` point anticipated the correction.
5. **Decisions:** launch the `H_K00` incidence job and the A2-first cascade
   continuation; harvest (do not relaunch) the already-present post-snapshot
   V38/V39 waves; keep TD6 in background; stop all raw receiver work and the
   refuted rewrite ansatz; hold grade-20 export and the mixed ladder until
   the cascade/W19 verdicts.  Opus5 does supply significant unique capability
   this round (§9).

---

## 1. Replay record (`REPLAY-F5`)

Loaded exactly as V37 does: pinned parser
`census_j2_typed_v23.py` (`14f2de22…`), V23R1 `RESULT.json` (`ce4d0adb…`),
V28/V30/V33/V35 result manifests (`7e00fc2c…`, `6a644c20…`, `22f64fbb…`,
`074c7b81…`), per-row hash checks, `rho→0`.  Census: 70 named, 51 nonzero,
65 variables, per-grade term counts `0,1,9,28,75,187,424,867,1647,2929` —
identical to Opus5's §0 and the V37 freeze constants.  V37 duals read from
the packet-pinned `aws_q65521/RESULT.json` (`065c96a9…`) and
`aws_q65519/RESULT.json` (`fe2f6ef3…`), each chaining by internal
`result_sha256` to its `compiled/result.json`.

| Check | Result |
|---|---|
| All 51 rows sigma-homogeneous, weight = grade; also all general-`rho` g10–15 rows with `rho` present (weight 0) | confirmed |
| Weight-1 variables among the 65 | exactly `{ell1}` |
| Distinct monomial supports 4,997; minimal 88 = 11 singletons + 54 pairs + 23 triples; singleton list as printed by Opus5 | confirmed |
| Minimum hitting set exactly 22 (independent exhaustive branch-and-bound); max coordinate zero-section dim exactly 43 | confirmed |
| Opus5's `F` (22 vars) is an optimum; `L43` leaves 0 surviving terms in all 51 rows; `k` free, `a1 ∈ F`; maximality witnesses for all 22 excluded vars (`a1→a1^2*cs3` in `Tg15_1`, `e0→e0^2` in `Tg12_4`, `cs1→cs1^3*ell1*k` in `Tg14_1`, `rs1→k*rs1^3` in `Tg13_2` all verbatim) | confirmed |
| `L43 × A^1_rho` on general-`rho` grades 10–15: 0 surviving terms | confirmed |
| Newcomer census g11–g19 (first literal occurrence) | identical to the symbol report's table |
| g14–19: every monomial has ≤ 1 newcomer; rows 4–7 newcomer-free | confirmed |
| Stationary symbol matrix, rows 1–3, all columns, all grades 14–19 (incl. `p,q1,s1,q2,s2,h1,h2`) | every entry matches the symbol report |
| Bezout `Q(X²−XY+Y²)−125k³S² = −32768·a1^6` and `q−(5/8)k·h = −(3/32)a1²` | exact |
| Compatibility term counts rows 3–7 after `e0=0`, grades 14–19 | match the symbol report exactly (incl. 587 at g19 row 5) |
| Cascade residuals (all displayed identities of Opus5 §3.2) | all exact; see §5 |
| `Tg19_7`: 552 terms; 28 supported in `S`; 0 monomials with exactly one outside coordinate | confirmed |
| V34 sigma representative `(a1,ell2,cs1,rs2,aa0,ee1,ec3)=(192,21/4,11,−35,−96,576,2400)`: the only nonzero row among all 70 is `Tg19_7 = −7077888` | confirmed |
| Rescale consistency: `rs2*aa0 = 3360 = 16·210` (λ^10, λ^5=4); `7077888 = 64·110592` (λ^15) against V36's normal form | consistent |
| V37 duals: lanes byte-identical; complete product annihilation (W17/W18: 0 products touch the support — pure divisibility; W19: 11 products checked; W20: 52); `λ(target)=1` all four | confirmed — all four nonmemberships independently verified |
| Grok rewrite: `λ(RHS combo) = −943/6912 ≠ 1`; `λ(φ19)=7855/6912` | rewrite refuted |
| Preflight divisor table: `a1k^3`: 0; `a1^2k^2`: 0; `a1^3k`: 2 (`a1^3` in `Tg15_3`, `a1^3k` in `Tg19_5`); `a1^4`: 1 (`a1^3` in `Tg15_3`) | matches Opus5 §4.3 exactly |

Not verified by this replay (inherited): provenance of the row bytes from the
emitter (Opus5's own §7.5 caveat — a reviewer re-emission of
`Tg14_3, Tg14_4, Tg15_3, Tg15_4, Tg16_5` is still the outstanding hygiene
item); the K00 569-tail replay itself (accepted at its audited SHA); the V35
byte pipeline upstream of the pinned result manifests.

A note on the dual verification's completeness: any weight-`w` element of the
homogeneous row ideal is a Q-combination of weight-`w` monomial multiples of
rows; a product contributes to `λ` only if some term lands in `supp(λ)`, so
checking exactly the divisor-generated multiples is a *complete* proof that
`λ` kills `(I_19)_w`.  This upgrades V37's four verdicts from
dual-selector-agreement to independently checked certificates, modulo row
provenance only.

---

## 2. Adjudication 1 — the typed-certificate shape floor (Fable5 §3.1)

**Verdict: sound, with the scope firewall made explicit.**  The three
ingredients separate as follows.

**(a) Specialization `rho=0`.**  Two elementary steps, both verified: setting
`rho=0` maps any staged identity `a1^i k^j (1+rho·W) = Σ h_r R_r` (over rows
through any grade) to the pure membership `a1^i k^j = Σ h_r|_0 R_r|_0` over
the frozen `rho=0` rows — the grade-16–19 exports *are* the `rho→0` images of
the true rows by construction; then extract the weight-`(5i+4j)` graded piece.
The load-bearing premise — general-`rho` rows are weight-homogeneous with
`rho` of sigma-weight 0 — is now verified from the pinned parser's
`sigma_weight` table and by direct homogeneity check on the general-`rho`
grade 10–15 bytes (`REPLAY-F5`).  No homogeneity of `W` is needed.

**(b) Fixed-weight completeness.**  All 65 chart variables have sigma-weight
≥ 1 (minimum: `ell1`, weight 1); rows are homogeneous with weight = grade.  A
weight-20 (or deeper) generator times any monomial has weight ≥ 20, so the
weight-`w` graded piece of the ideal for `w ≤ 19` is fixed forever once rows
through grade 19 are frozen.  This is the exact content of "W17–W19 complete
forever" and of Opus5's two-line reduction of that packet claim.

**(c) Ideal multiplication.**  If `d | m` then `d ∈ I ⟹ m = (m/d)·d ∈ I`;
contrapositively, nonmembership of a tested target excludes *all its
divisors* at the same ideal.  This radiates V37's four verdicts downward.
It never radiates upward: nothing excludes `a1^5`, `a1^4*k`, or any shape of
weight ≥ 21.

**Exact exclusion list** (raw row-ideal typed certificates
`a1^i k^j (1+rho·W)`, any depth, any cofactor `W`):

- excluded **forever**: `(i,j) ∈ {(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),
  (3,0),(3,1)}` — every shape with `i ≥ 1` and `5i+4j ≤ 19`.  Each divides
  one of the tested targets `(1,3),(2,2),(3,1)` (or `(4,0)` for the pure
  powers), giving nonmembership in `I_19`; ingredient (b) then makes the
  verdict depth-independent because their weights are ≤ 19.
- excluded **through grade 19 only**: `(4,0)` = `a1^4`, weight 20.  Weight 20
  is the first graded piece that future grade-20 rows (weight-20 generators
  entering with scalar cofactors) can enlarge, so finality requires the
  grade-20 export; nothing cheaper can close it.
- **open**: `a1^4` (pending grade 20), every mixed shape with `5i+4j ≥ 21`
  (the smallest is `a1*k^4`, weight 21 — there is no mixed weight-20 shape
  since `5i+4j=20, i,j≥1` has no solution), and every pure power `a1^m`,
  `m ≥ 5`.

Fable5's §3.2 hand check is also verified end-to-end: at the V34 sigma
representative all 70 named rows vanish except `Tg19_7 = −7077888`; a
weight-20 identity over rows through 19 forces a weight-1 cofactor on
`Tg19_7`, and the only weight-1 variable, `ell1`, is outside the support —
so `a1^4 ∈ I_19` would give `0 = a1^4(P) ≠ 0`.  Two independent artifact
chains (V34/V35 evaluation; V37 dual) now agree on W20, and my complete dual
check confirms both.  One cosmetic defect: Fable5 wrote "`a1=48`" for the
representative; the frozen sigma representative has `a1=192` (the `λ^5=4`
rescale of V32's `a1=48` normalization).  Only `a1 ≠ 0` is used, so nothing
breaks, but the ledger entry should carry the correct value.

**Firewall to record next to the lemma:** the exclusions concern membership
in the ideal generated by the *literal source rows*.  If the honest staged
chart ideal acquires generators beyond the rows (saturation, bilinear,
routing equations), every verdict must be re-derived — that is exactly
Grok's dual-transport question, and it is the right follow-up, not a defect.

---

## 3. Adjudication 2 — Grok's use of the V37 five-term dual

**The displayed rewrite is wrong, and provably so on the frozen bytes.**
Card B(iii) displays

```text
a1^3 k = (5/72) a1 aa0 ac3 − (5/144) a1 aa0 cs2^2
       + (1/3) a1 aa0 k rs2 + (5/36) a1 aa1 cs2 rs2 + (element of I_19).
```

Moving everything to one side, this is precisely the assertion
`φ19 ∈ I_19` (the difference *is* the dual polynomial).  But `λ = φ19` (read
as a functional in the monomial dual basis — the identification V37's
`functional` field uses, confirmed byte-for-byte against both selector
lanes) annihilates the entire weight-19 graded piece of `I_19`, while
`λ(φ19) = ‖φ19‖² = 7855/6912 ≠ 0`.  Numerically, applying `λ` to the
rewrite's right side gives `−943/6912`, not the required `1` (`REPLAY-F5`).
A dual functional's support is an orthogonal-complement object; it can never
be a normal form or quotient equality.  The general lesson, which the
adjudication asked me to state: *a linear functional separating a target
from an ideal slice certifies nonmembership and nothing else; it licenses no
rewrite of the target modulo that ideal.*  The rewrite could only hold
modulo a strictly larger ideal on which `λ` no longer vanishes — legitimate
as a labelled speculation, never as a displayed identity.

**Second defect:** Grok's §4 negative control — "the dead V34 point must
keep `φ19 ≠ 0` on raw rows" — is broken.  Every monomial of `φ19` contains
one of `k, ac3, cs2, aa1`, all zero at the V34 representative, so
`φ19(P) = 0` identically.  An implementer following the control as written
would fail a correct build.  Replace it with the self-test
`λ(φ19) = 7855/6912` plus a spot re-check that `λ` kills the
divisor-generated product set (the complete check of §1 runs in
milliseconds).

**Salvaged: the strongest correct dual-transport statement.**  Let `λ` be a
verified weight-`w` dual for target `t` over generator set `G`, and let `G'`
be new generators (chart bilinears, saturation generators, `rho`-linear
pieces).  Then:

1. If `λ(μ·g) = 0` for **every** monomial `μ` and `g ∈ G'` with
   `wt(μg) = w` — and it suffices to enumerate the divisor-generated
   multiples `μ = M/m`, `M ∈ supp(λ)`, `m` a monomial of `g` — then the same
   `λ` certifies `t ∉ (G ∪ G')_w`.  Nonmembership transports with zero new
   linear algebra.
2. If some `λ(μ·g) ≠ 0`, the old certificate is void.  This proves *only*
   that the enlarged ideal's weight-`w` slice grew in a direction `λ` sees.
   It does **not** prove membership of `t`, does not produce a "predicted
   identity", and reopens the question for a full new fixed-weight solve.
3. Evaluating on the bare generators (Grok's literal wording "on every new
   generator at the dual's weight") is fail-open when generators have weight
   < `w`; the enumeration of point 1 is mandatory.

Grok's Card B parts (i)/(ii), the survival/kill outcome logic, and the §4
software design are sound under these repairs; the delayed-`a0`
"predicted-type" reading survives only as labelled navigation.  Grok's
overall PROVISIONAL labelling was honest; the specific rewrite display was
not flagged and is the round's one outright mathematical error.

---

## 4. Adjudication 3 — Opus5's `L43` and the support-incidence preflight

**Theorem L: confirmed exactly, at its stated scope** (`REPLAY-F5`).  Scope
inventory, as demanded:

- **Object:** *coordinate* zero sections (subspaces spanned by coordinate
  directions on which every row vanishes identically as a polynomial).  Not
  arbitrary linear subspaces, not nonlinear components, and — critically —
  not valued *points*.  A point with `a1 ≠ 0` on a small support can kill
  all rows through some grade (V34's point does, through 18) even though no
  coordinate *section* with `a1 ≠ 0` exists.  Theorem L and Fable5's
  TRIVIAL-LOCUS are therefore complementary, not overlapping: L43 answers
  the subspace version of Fable5's Q1 negatively through grade 19; the
  valued-point, Kummer-aware, all-depth version remains the live card.
- **Maximum versus maximal:** both parts hold.  Maximum: my independent
  exhaustive branch-and-bound reproduces minimum hitting set 22, so 43 is
  the maximum dimension (two independent implementations agree; the upper
  bound `≤ 43` is exact, the witness gives `≥ 43`).  Maximal: all 22
  switch-on monomials verified.
- **Depth:** through grade 19 for `rho=0`; through grade 15 with `rho` fully
  free (the only grades with general-`rho` bytes).  The all-depth "front
  property" (every emitter monomial contains a coordinate of `F`) is a
  conjecture — Opus5's Card B(i) — and Opus5 labels it so.  `K00` remains
  the only all-depth statement, at its single point.
- **Raw versus honest:** `L43` lies inside the receiver locus (`a1 ∈ F`,
  `a0=0`, `J1=0`, `k` free) and certifies raw-system nonemptiness only —
  Opus5 says this himself (§7.9), matching Sol's recorded tropical caveat.
- **Row-32/secant interface:** *speculative only.*  The self-label
  "candidate bridge, NOT YET TESTED" is correct; the section headline "the
  receiver is a row-32 object, not a row-31 object" overstates it.  The
  post-snapshot K00 report shows the honest receiver frame actually being
  built is the promoted one-parameter Rees client — a row-31-style object —
  with `Phi7` as its first equation.  No map from the secant presentation
  `I:Delta = I + (det A)` to that frame has been written, and the `[6,2]`
  profile stratification makes type compatibility genuinely unclear.  Hold
  the bridge behind the `H_K00` outcome.

**Preflight: confirmed and adopted.**  The vacuous-nonmember logic is
elementary and correct (no row monomial divides the target ⟹ no ideal
element contains the target monomial at all), the divisor table replays
exactly (0, 0, 2, 1 with the named monomials), and it retro-explains V37's
W17/W18 one-term rank-0 duals *structurally*.  Fair criticism embedded in
it: half of a dual-host AWS campaign answered a divisibility question.  The
"can only refuse work" framing is right, with the precision that a
vacuous-nonmember refusal is itself a (trivially sound) nonmembership
verdict.

**One design consequence Opus5 drew that I endorse with a correction:** the
warning that "any discriminator tested only at `K00` risks a false positive"
is correct in principle, but his generic-`L43` honest-equation test (§4.2)
is not currently executable: the promoted honest equations live in the
one-parameter `[6,2]` client's variables, and the collision-to-`[6,2]`
pullback with correction jets through grade 38 is explicitly missing (K00
report §8).  A generic `L43` point need not even have the `[6,2]` terminal
profile.  Register the generic-`L43` evaluation as the *acceptance test* for
the future pullback, and run `H_K00` (which does admit transverse
corrections in its own frame) now.

---

## 5. Adjudication 4 — the ordered-`T-a1` radical cascade, line by line

All displayed residuals were recomputed exactly from the frozen bytes
(`REPLAY-F5`).  Chain, with each step's epistemic type:

| Step | Statement | Type | Replay |
|---|---|---|---|
| 1 | `Tg11_1 = (3/8)a1·e0` ⟹ `e0=0` | **exact ideal identity** in `(P/I)[a1^{-1}]` (localization, no radical needed) | exact |
| 2 | `Tg12_2|_{e0=0} = (3/32)e1(e1−4a1·ell1)` | exact identity; the **branching** on the factors is field-point/radical scope | exact |
| 3 | branch `e1=4a1·ell1`: `Tg12_1 → (3/8)a1(ee0+4aa0·ell1)` ⟹ `ee0=−4aa0·ell1` | division by `a1`; pointwise | exact |
| 4 | then `Tg13_4 → −(3/2)a1²ell1³` ⟹ `ell1=0` ⟹ `e1=0`; branch collapses | pointwise (`a1≠0`, char ≠ 2,3) | exact |
| 5 | `Tg12_1|_{e0=e1=0} = (3/8)a1·ee0` ⟹ `ee0=0` | division by `a1` | exact |
| 6 | `Tg14_4 → (3/32)a1²·ell1·rs1` ⟹ `ell1·rs1=0` | pointwise, `a1≠0` | exact |
| 7 | `Tg14_3+(1/2)ell1·Tg13_1 → (3/8)a1²cs1·ell1 − (3/16)a1·aa0·rs1` ⟹ `aa0·rs1 = 2a1·cs1·ell1` | exact combination; division by `(3/16)a1` | exact |
| B1 | Case B (`ell1≠0`): `rs1=0`; then step 7 ⟹ `cs1=0` (divide `a1²ell1`) | pointwise | exact |
| B2 | `Tg13_2 → −(3/8)a1·ee1·ell1` ⟹ `ee1=0` | divide `a1·ell1` (holds even before `cs1=0` — the chain is slightly more robust than narrated) | exact |
| B3 | `Tg13_1 → (3/8)a1·ec3` ⟹ `ec3=0`; `Tg15_4 → (3/32)a1²ell1·rs2` ⟹ `rs2=0`; `Tg14_2 → −(3/8)a1·ell1·ez3` ⟹ `ez3=0`; `Tg14_1 → (3/8)a1(ec4−a1·cs2)` ⟹ `ec4=a1·cs2` | pointwise, divisions by `a1`, `ell1` | all exact |
| B4 | `Tg15_3 → a1²((3/8)cs2·ell1 − (1/16)a1)` ⟹ `a1=6cs2·ell1` | divide `a1²` | exact |
| B5 | `Tg16_5 →` (case-B residual) `(3/32)a1³ell1 − (3/16)a1²cs2·ell1²`; substituting `a1=6cs2·ell1` gives `(27/2)cs2³ell1⁴` ⟹ `cs2=0` ⟹ `a1=0`, contradiction | pointwise; needs the two substitution passes composed (the `ec4→a1·cs2` replacement reintroduces `a1`) | exact after two-pass composition |
| A | Case A (`ell1=0`): step 7 ⟹ `aa0·rs1=0`; A1: `rs1=0`; A2 (`rs1≠0`): `aa0=0`, and `Tg13_2 → rs1((5/1024)k·rs1²−(3/32)a1²)` ⟹ `k·rs1²=(96/5)a1²`, `Tg15_4 → (3/32)a1·rs1(a1·ell2−ee1)` ⟹ `ee1=a1·ell2` | pointwise; divisions by `rs1`, `a1`, and 5 | exact |

**Errors found: one attribution slip, zero algebraic errors.**  Theorem A
credits both A2 relations to `Tg15_4`; the Pell-like relation
`k·rs1² = (96/5)a1²` in fact comes from `Tg13_2` (`Tg15_4` supplies only
`ee1 = a1·ell2`).  The mathematics is unaffected; the ledger entry should
carry the correct row name.  Complete division census: `a1`, `ell1`,
constants in `2^a·3^b`; char 5 is needed only for A2's normal form (the Case
B kill itself works in char ∉ {2,3}).  All grade usage is 11–16, `rho=0`
throughout (grades 11–15 restricted from general-`rho` bytes, grade 16 from
the `rho=0` V28 export).

**Exact-versus-radical bookkeeping**, as demanded: steps 1 and 5 are ideal
identities after localization at `a1` (the symbol report's point); step 2's
factorization is an identity but the case split, and everything downstream,
is field-point/radical scope; nothing in the cascade is a membership
certificate, and Opus5's own §7.1–7.2 (the `rho=0` conversion gap under
correction `593f953b…`, and radical-versus-ideal) state the two conversion
debts exactly.  The derived reframing — V32's six-coordinate ansatz is
branch A1 plus *unjustified* extra zeros, so V34/V36 killed a sub-ansatz of
A1, not A1 — is verified (V32's support sets `e0=e1=ee0=ell1=rs1=0`, which
is exactly A1).

---

## 6. Adjudication 5 — integrating the exact symbol result

The symbol report's content replays exactly (§1): newcomer census;
stationarity from grade 14; the full rows-1–3 coefficient matrix; row 3's
newcomer coefficients all proportional to `e0` (hence zero in
`R_g = (P_g/I_{<g})[a1^{-1}]` by the `Tg11_1` *ideal* identity); the two
fraction-free Bezout identities; therefore **symbol rank exactly two on
`D(a1)`**, with the ambient rank three an artifact of ignoring `Tg11_1`.
Rows 3–7 freely represent the compatibility quotient at every grade 14–19,
and no grade-19 newcomer occurs in any of them.

**Consistency checks performed, no conflicts found:**

- **Against the cascade.**  Perfect mechanical agreement: every cascade step
  that forces an *old* coordinate uses a compatibility row (`Tg13_4`,
  `Tg14_3/4`, `Tg15_3/4`, `Tg16_5` — rows 3–7), and every step that solves a
  *newcomer* uses rows 1–2 (`Tg14_1` solving `ec4`; `Tg14_2` solving `ez3`
  via the `EZ` coefficient `−(3/8)a1·ell1+(3/16)e1`).  The symbol structure
  is the reason the cascade instrument works.
- **Against V36.**  The amendment's grade-19 newcomer names are confirmed and
  strengthened: `Tg19_7`'s jet-freeness is structural (shared by rows 3–7 at
  every grade), so the V36 kill mechanism is not an accident of one row.
  The narrow kill scope (one component, not the chart) is unchanged.
- **Against Grok's Card C.**  Material sharpening: on `D(a1)`, rows 1–2 are
  split for all grades 14–19 (`EC` coefficient `(3/8)a1`; row 2 split by the
  Bezout unit), so adjoined newcomers are always *solvable fibre directions*
  and can never empty a slice; and newcomers are absent from rows 3–7
  entirely.  Card C's branch "`Tg19_1..3` then empty it after adjoining
  newcomers" is therefore vacuous.  What survives of Card C: test the
  *old-coordinate compatibility rows 3–7, at all grades 14–19*, on the
  enlarged slice.  Card C's negative control (V34 point + free newcomers
  leaves `Tg19_7` unchanged) is trivially true given the census — legitimate
  as a census control, worthless as a mathematics control.
- **Against the no-single-coordinate-repair statement.**  Verified: of
  `Tg19_7`'s 552 monomials, 28 lie in the seven-coordinate support `S` and
  none has exactly one outside coordinate, so
  `Tg19_7|_{S∪{x}} = Tg19_7|_S` for every single outside `x`.  The report's
  own quantifier discipline (earlier grades may move base coordinates as
  functions of `x`; no enlarged-support unit-ideal claim follows) is
  correct and must travel with any citation.
- **Against Sol's blind Card B.**  The symbol report *is* Card B executed,
  and it lands in the case Sol's dichotomy did not name: the symbol is
  neither obstruction-dead nor involutive — stable rank 2 with a persistent
  five-dimensional compatibility block, so prolongation neither terminates
  structurally nor becomes futile; the decisive question becomes whether new
  compatibility rows are old syzygies.  That is exactly the proposed W19
  case (`Tg19_7 ∈ (J_other)_19?`), whose design (complete homogeneous
  enumeration, dual or multiplier certificate, deterministic reduced
  representative `R19`, negative control) is sound and whose unsaturated
  scope firewall (§7.3: a raw-slice nonmember can still enter after
  localization at `a1` with an `a1^N` factor — precisely the V37/typed
  distinction) is correctly stated.

---

## 7. Adjudication 6 — the K00 correction and the closure-first incidence

**What changed.**  The literal K00 section is not an honest strict source:
on the K00 core the seven `r_l` vanish (`F = q^4` with `q = z²−rho²`, so
`F^{3/2} = q^6` and `F^{5/4} = q^5` are polynomial — verified by hand), so
the terminal target row gives `Phi7|_{K00} = −Λ^{19}·Jdet/4`, a unit on
`D(Λ·Jdet) = D(sigma·Jdet)` with the explicit certificates
`(Λ·Jdet)^{19} = −4·Jdet^{18}·Phi7` and `(sigma·Jdet)^{38} = −4·Jdet^{37}·Phi7`.
This *answers* the blind round's uniform question ("evaluate the first
honest equation at K00") in the exclusion direction — for the
restriction-first literal section.  All three blind receiver cards (Sol A,
Fable5 2, Grok A) are superseded in that respect and none of them
anticipated that the honest equation was already in the promoted stack.

**What did not change.**  Restriction-before-saturation decides nothing
about the transverse closure: saturation and base change do not commute, and
the report's own `(x−Λm)` control exhibits the gap exactly (closure-first
boundary `(Λ,x)` proper; restriction-first unit).  The false claim
"`J1=J2=0` makes the geometric blowup fibre empty" is *not* repeated here
and was not made by any blind submission; the report's §3 corrects it
explicitly (the `(x,y)`-blowup `P¹` fibre; the DVR routing (3.5) is the
exact replacement statement).  Credit where due: Grok's blind §7.2
(Proj-versus-`V(I)`, base-point versus exceptional-fibre) is precisely this
distinction, stated before the delta report existed.

**Audit of the proposed incidence (7.1)–(7.3).**  I verified the `M_K00`
arithmetic by hand: `C6=2p` makes the four even relations
`8C4−3C6², 16C2−C6³, 256C0−C6⁴` exactly the `rho`-eliminated
(deck-invariant) form of `C4=3p²/2, C2=p³/2, C0=p⁴/16`, which is (2.2); the
deck-explicit variant (7.4) contracts back to (7.1).  The order —
`K = (Phi):Λ^∞:Jdet^∞` (colon order immaterial), then `+ (Λ) + M_K00`, then
localize at `(C6·k10·Jdet)^∞` — is the load-bearing part and is right; the
final localization selects the generic `rho ≠ 0` (that is, `C6` unit),
unit-`k10`, nonzero-Jacobian slice, which is exactly Grok's `K00 ∩ D(rho)`
piece.  Grok's `K00 ∩ V(rho)` piece is the `C6=0` tip, explicitly left
untouched (item 5) — the split is honoured, and the tip must be registered
as the named companion computation, not forgotten.  Controls are correctly
specified (restriction-first must reproduce (5.6); exact Q decides, good
prime is software control).  Interpretation items 3–5 have the right scope:
`H_K00=(1)` excludes only the generic K00 incidence of the fixed `[6,2]`
ordinary-tail client; `H_K00≠(1)` records accessible boundary support and is
not a Taylor realization or Keller pair.

**Risks to preregister:** feasibility (the two-parameter ancestor timed out
at four hours with no verdict, and the one-parameter Q/32003 launches died
at `ONEPARAM_STAGE_LAMBDA_START`; stage the eliminations and cap, and on
timeout deliver the partial elimination state and the blocking
subcomputation, not a blind rerun); and the standing gap that the
general-`rho` collision emitter is incomplete through grades 28–38, so
nothing in this incidence yet speaks for the full collision receiver.
Fable5's C3 residence map gets its first concrete instance here: §6 of the
K00 report — a genuine arc near the core must realize
`r7 = Λ^{19}·Jdet/4` through nonzero transverse corrections — is exactly
the constraint to hand the counterexample lanes.

---

## 8. Claim matrix

`S` = sound, `SC` = sound with scope correction, `U` = unsupported, `W` =
wrong.  Only material new claims; packet restatements omitted.

| # | Claim (report, §) | Verdict | Reason |
|---|---|---|---|
| 1 | Sol: Spencer–Macaulay dual-complex mechanism (§new) | S | Sound design; instantiated within hours by the symbol report; multiplication-map dual ladder still unexecuted |
| 2 | Sol: Card A K00 fiber/routing discriminator | SC | Sound; superseded in part — `Phi7` answers the "first honest equation" question; live object is now `H_K00` |
| 3 | Sol: Card B symbol dichotomy (localizer-power vs involutive) | SC | Executed; the real outcome is the unnamed middle case (stable rank 2, persistent 5-dim compatibility block) |
| 4 | Sol: Card C inverse-system ladder W21–25 | S | Sound design; note rungs > 20 can never be "forever" without deeper rows |
| 5 | Fable5 §3.1: shape floor (nine shapes forever; `a1^4` minimal open; mixed ≥ 21) | S | Verified end-to-end (§2); firewall: raw row-ideal scope; cosmetic `a1=48`→`192` fix |
| 6 | Fable5 §3.2: W20 already implied by V34/V35 | S | Verified numerically: only `Tg19_7 = −7077888` nonzero at P; unique weight-1 variable `ell1 ∉ S`; stops at weight 21 via `ell2 = 21/4` |
| 7 | Fable5 §3.3: TRIVIAL-LOCUS classifier + section-first rule | SC | Sound design; record the subspace/point split — Theorem L already answers the subspace form of Q1 negatively through g19; the card's live content is valued points (Kummer-aware) and all-depth, now best seeded on branches A1/A2 |
| 8 | Fable5 §3.4: C1 lightcone ledger, C2 templates, C3 residence map | S | Navigation; C1 is now a two-line theorem given verified homogeneity; C3 has its first instance (`Phi7`) |
| 9 | Fable5 Card 2: RECEIVER-HONEST-EQ | SC | Superseded in part by the K00 report (outcome 1 fired for the literal section); the arc-genuineness lemma remains open |
| 10 | Fable5 Card 3: W20 finalization + ladder 21–26 | SC | Sound but resequenced: cascade + W19 case are cheaper and should gate the grade-20 export; rungs > 20 are navigation-only labels |
| 11 | Grok: section-first honest-equation calculus + dictionary | S | Sound navigation; consistent with, and partly anticipating, the K00 report |
| 12 | Grok: K00 is two loci (`D(rho)`/`V(rho)`) with theorem dictionary | S | Adopted; `H_K00` handles the `D(rho)` piece, the `C6=0` tip is the registered companion |
| 13 | Grok: `φ19` delayed-`a0` certificate-type prediction | SC | Admissible only as labelled speculation; the concrete displayed form is claim 14 |
| 14 | Grok Card B(iii): the five-term rewrite modulo `I_19` | **W** | Equivalent to `φ19 ∈ I_19`; refuted: `λ(φ19)=7855/6912 ≠ 0`, `λ(RHS)=−943/6912 ≠ 1` (`REPLAY-F5`) |
| 15 | Grok Card B(i)/(ii) + §4: dual transport engine | SC | Sound after two repairs: enumerate all weight-`w` multiples (bare-generator evaluation is fail-open); nonzero evaluation ⟹ certificate void, never membership |
| 16 | Grok §4 control: "`φ19 ≠ 0` at the V34 point" | **W** | `φ19(P)=0` identically (every monomial contains `k`, `ac3`, `cs2`, or `aa1`); replace with the `‖φ19‖²` self-test |
| 17 | Grok Card A: split + hypothesis-gated named identities | SC | Sound; `D(rho)` half superseded by `Phi7`; met/unmet hypothesis emission adopted into Card II |
| 18 | Grok Card C: first-occurrence support increment | SC | Newcomer-emptying branch vacuous (rows 1–2 split; newcomers absent from rows 3–7); surviving content: compatibility rows 3–7 on the enlarged slice; V34-control tests only the census |
| 19 | Grok: W17/W18 "isolated monomials invisible to `I_19`" | S | Verified; structural reason is the zero-divisor count |
| 20 | Opus5 Theorem L (`L43`, min hitting set 22, dim exactly 43) | S | **Confirmed by independent replay**, including exhaustiveness of the optimum and the general-`rho` g10–15 statement |
| 21 | Opus5: front/tail reading; `K00`/`Z00`/`CS0` one phenomenon | S | Through g19; all-depth front property correctly labelled open (his Card B(i)) |
| 22 | Opus5: `{a1}` minimal support ⟹ K00-obstruction does not transplant to `T-a1` | S | Verified; with the complementary point that valued-point sections with `a1 ≠ 0` are not excluded (claim 7) |
| 23 | Opus5 Theorem A cascade + Case B kill | S | **Confirmed line by line**; one row-attribution slip (`Tg13_2`, not `Tg15_4`, for `k·rs1²=(96/5)a1²`); divisions exactly as declared |
| 24 | Opus5 §3.3: "the receiver is a row-32 object" / secant bridge | U | Self-labelled untested; headline overstates; the honest receiver frame under construction is the one-parameter Rees client; hold |
| 25 | Opus5 §4.2: generic-`L43` honest-equation test | SC | Right design principle; not executable without the missing collision→`[6,2]` pullback (profile mismatch risk); register as the pullback's acceptance test |
| 26 | Opus5 §4.3: support-incidence preflight | S | Confirmed exactly (divisor table 0/0/2/1); adopt as a launch gate |
| 27 | Opus5 2.1(6): `rho`-specialization status as a ranked obligation | S | Correct and important; add as a fail-closed tool field |
| 28 | Opus5: V32 ansatz is a derived sub-ansatz of branch A1 | S | Verified; sharpens the honest scope of the V34/V36 kill |

---

## 9. Strongest unique contribution per model (after deduplication)

- **Sol (blind):** the Spencer/compatibility *framing* — turning "export
  another grade" into "compute the symbol, its left kernel, and whether new
  compatibility classes are old syzygies" — which its own post-snapshot
  symbol lane then executed and which now organizes the whole `T-a1`
  program.  (The two post-snapshot reports are Sol's, but the cross-review
  scores the blind phase.)
- **Fable5:** the shape-floor restriction lemma with the W20 hand
  cross-check — the only new forever-tier mathematics produced in the blind
  phase from zero compute, now adversarially verified here — plus the
  trivial-locus point-section classifier as the complement to `L43`.
- **Grok:** the `D(rho)`/`V(rho)` split of K00 with the promoted-theorem
  hypothesis dictionary and the Proj-versus-base-point warning — the two
  disciplines the closure-first receiver computation actually needed; both
  were consumed by the delta report.  This stands despite the Card B(iii)
  error.
- **Opus5:** the pair Theorem L + Theorem A — one converts the receiver
  wall from a point into a 43-dimensional structured component and yields
  the preflight instrument; the other is the first chart-wide structural
  result on ordered `T-a1`, derives V32 instead of guessing it, and kills a
  branch — both now second-model confirmed.

---

## 10. Merged idea cards (three)

### Card I — `T-A1-STRUCTURE-FIRST` (cascade + W19 compatibility + floor registration)

- **Dependencies.**  The 70 pinned row files (all hashes re-verified this
  session); pinned V23 parser; Theorem A now second-model replayed (this
  report); the symbol report's stationary matrix and controls; hardened
  validator for anything promoted.  No dependency on V34/V36/V37 for the
  cascade itself.
- **Cheapest discriminator.**  (a) Desk: continue branches A1 and A2 grade
  by grade to 19 on frozen bytes, A2 first (it carries `aa0=0`,
  `ee1=a1·ell2`, `k·rs1²=(96/5)a1²` and should resolve fastest);
  (b) one bounded AWS sparse-linear case: `Tg19_7 ∈ (J_other)_19` per the
  symbol report's §6 spec.  A V39 case directory for exactly this question
  already exists post-snapshot: **harvest it, do not double-launch.**
- **Both outcomes.**  W19 membership ⟹ `Tg19_7` redundant at raw scope; the
  compatibility census shrinks and support screening retargets to rows 3–6.
  Nonmembership ⟹ the reduced representative `R19` becomes the canonical
  small obstruction polynomial valid against *every* support.  Cascade:
  both branches contradict ⟹ ordered `T-a1` has empty `rho=0` fibre on
  `D(a1)` at field-point scope — only then fund typed-certificate
  conversion (honest weights `a1^4` = 20 pending grade 20, `a1^4k` = 24,
  `a1^5` = 25) and the grade-20 export; a branch survives ⟹ an explicitly
  parametrized family, handed to Card III's point classifier and to one
  bounded `std` on that branch only.
- **Stop rule.**  Two consecutive grades with no forced vanishing and no
  two-row identity in either branch; one run for the W19 case; never
  prolong the V34 orbit; no ladder rung before the cascade verdict.
- **Scope firewall.**  Everything is `rho=0`, raw row-ideal,
  radical/field-point scope, char ∉ {2,3,5}; conversion to typed
  `a1^N(1+rho·W)` certificates and the `rho ≠ 0` lift (correction
  `593f953b…`) are separately gated steps; nonmembership at weight > 20 is
  labelled "through grade g", never "forever".

### Card II — `RECEIVER-CLOSURE-FIRST` (`H_K00` incidence with gating and the `C6=0` companion)

- **Dependencies.**  Promoted one-parameter seven-row source and compiler
  (pinned in the K00 report); `M_K00` (7.1) (arithmetic verified here);
  Grok's per-identity met/unmet hypothesis emission; restriction-first
  (5.6) as the mandatory negative control; deck-invariance control
  (7.4)→(7.1).
- **Cheapest discriminator.**  Compile and run (7.3) —
  `K=(Phi):Λ^∞:Jdet^∞`, `B=K+(Λ)+M_K00`, `H_K00=B:(C6·k10·Jdet)^∞` — as an
  exact-Q plus good-prime AWS pair with staged elimination and a
  preregistered cap (the two-parameter ancestor timed out at 4 h; the
  one-parameter launches died at `ONEPARAM_STAGE_LAMBDA_START`).  On
  timeout: deliver the partial elimination state and the exact blocking
  subcomputation, not a rerun.
- **Both outcomes.**  `H_K00=(1)` with a saved certificate ⟹ first honest
  transverse exclusion of the generic K00 incidence for the `[6,2]` client;
  record exceptional power/localizer/rho factor; queue the `C6=0` tip.
  `H_K00≠(1)` ⟹ accessible algebraic boundary support: the
  germ/algebraization fork opens with an explicit ideal — Grok's
  falsification track — and the C3 residence constraint
  (`r7 = Λ^{19}Jdet/4` via nonzero transverse corrections) is handed to the
  counterexample lanes.  Not a Taylor realization, not a Keller pair, not a
  counterexample.
- **Stop rule.**  One compile, one dual-lane run, at most one retry with a
  strictly smaller staged elimination; if the compiler cannot produce the
  system, file the precise missing map and stop (Fable5 Card 2's honest
  blocking clause).
- **Scope firewall.**  Fixed `[6,2]` ordinary-tail client, generic
  (`C6·k10·Jdet` unit) incidence only; the `C6=0` tip, `k10=0`, other load
  rays, and the full collision receiver are untouched; generic-`L43`
  evaluation is *not* this card — it is the acceptance test of the future
  collision→`[6,2]` pullback; no Gate-T inference either way.

### Card III — `GATE-AND-SECTION` (one tool: preflight + trivial locus + dual transport)

- **Dependencies.**  Pinned V23 parser; the unified typed-certificate tool
  as host (no fork); registered section list (`CS0`, `Z00`, `K00`, `L43`,
  `A00`/`A10` deaths); the frozen V37 duals.
- **Cheapest discriminator.**  Three launch gates plus one classifier:
  (i) divisibility/vacuous-nonmember; (ii) minimal-support/hitting-set
  census (subspace sections); (iii) dual transport with full weight-`w`
  multiple enumeration; (iv) valued-point trivial-locus classifier over
  `Q[rho]`, supports ≤ 3, scheme-theoretic and Kummer-aware, seeded on
  branches A1/A2, with the per-support canonical-tail instantiation check
  fail-closed.  Controls: reproduce the W17/W18 rank-0 signature, `K00`,
  `L43`, the grade-15 `A00`/`A10` deaths, `a0^3` as positive control; the
  `λ(φ19)=7855/6912` self-test **replacing Grok's broken V34-point
  control**; one deliberately mistyped target and one corrupted metadata
  field must fail.
- **Both outcomes.**  Gates refuse or license every future landing launch
  (on recorded evidence they would have removed two of four V37 targets and
  flagged the receiver census before V26).  Classifier Q2 positive (an
  all-depth valued section with `a1·k ≠ 0`) halts the entire `T-a1`
  certificate program in one stroke; negative through size 3 licenses it
  and banks permanent preflight entries.
- **Stop rule.**  Fable5 Card 1's caps verbatim (support size 3, per-support
  wall clock, two-strike rule); each gate is one lane-session of tooling,
  not research.
- **Scope firewall.**  Gates certify raw/unsaturated facts only; the
  preflight never emits a membership; subspace-section absence ≠
  valued-point absence ≠ chart closability; nothing lifts to
  saturated/`rho≠0`/Gate-T scope automatically.

---

## 11. Decisions

**Launch now.**
- Card II compile + run (`H_K00`): the receiver's single live discriminator.
- Card I(a): A2-first cascade continuation (desk lane, zero compute).
- Card I(b): the W19 `Tg19_7` case — **as harvest/validation of the
  already-present V39 case**, not a fresh launch; likewise reconcile the
  post-snapshot V38 ladder wave against the shape floor before any new rung.
- AS109 arithmetic-Newton `n=2` corner with the source-gauge section: two
  full rounds ranked #1 and idle is the worst state (Opus5 is right); staff
  it this cycle or record an explicit demotion.
- Card III gates (i)–(iii): under an hour each, immediate compounding value.

**Continue in background.**
- TD6 H19R2 exact-Q to its caps; harvest original-FIRST multipliers and the
  total-`F` certificate debt.
- V29 grade-16 Groebner controls: to their existing caps only, then stop;
  preempt if Card II needs the hosts.
- Broad web sweep on its unchanged clock (next deadline 2026-08-28 00:00Z).
- `jc2-lean`: asynchronous, untouched.

**Hold.**
- Grade-20 row export, W20 finalization, and the mixed ladder 21–26 — until
  the cascade and W19 verdicts retarget or release them.
- The row-32 secant/receiver bridge — until `H_K00` returns; then test the
  interface only if the one-parameter frame fails to progress.
- Opus5's generic-`L43` honest test — until the collision→`[6,2]` pullback
  exists; register it as that pullback's acceptance test.
- `3P-E31` full prime-ray: firewall stands.

**Stop.**
- All deeper raw receiver exports and raw-leaf standard bases (K00 + L43;
  unanimous across all four reports).
- V32/V34 six-coordinate orbit prolongation (dead; unanimous).
- `T-a0` successors (chart is the zero ring).
- Grok Card B(iii)'s rewrite ansatz (refuted here) and the V34-point `φ19`
  control (broken as stated).
- Grok Card A's literal-K00 identity evaluation on the `D(rho)` piece as
  originally designed (answered by `Phi7`); the `V(rho)`/`C6=0` companion
  survives inside Card II.
- Promotion of anything through the frozen V37 validator (hardening first;
  the mathematics itself is verified, the custody is not).
- Serial affine-Faber `H` increments and the paid AS109 rigid-leaf search
  (standing stops; no prerequisite has appeared).

---

## 12. Verdict on Opus5's unique capability this round

**Yes — significant, and this round the largest of the four blind lanes on
correctness-adjusted information gain.**  The basis, after my adversarial
replay rather than style or volume: Theorem L is fully correct and converts
the receiver wall from one degenerate point into a structured
43-dimensional object with an immediate design consequence (test at generic
sections, not at `K00`); Theorem A is fully correct at its declared scope
(one row-name slip), is the first chart-wide structural result on the last
open `J2` chart, and retro-derives the lane's guessed ansatz; the preflight
is correct and would have saved real compute twice already; the
`rho`-specialization obligation is a genuine ledger improvement.  All four
are absent from my own blind report, whose contributions (shape floor, W20
hand check, trivial locus, lightcone ledger) are disjoint — the two lanes
composed rather than duplicated, which is the outcome cross-pollination is
for.  Deductions: the row-32 headline overstates a self-labelled untested
candidate, and both flagship theorems were single-model until this session;
they are now second-model confirmed at stated scope.  Net: Opus5's blind
report is this round's highest-value single artifact; the post-snapshot Sol
delta reports are the round's highest-value artifacts overall.

---

## 13. Nonclaims

Nothing in this report proves or disproves JC2, closes ordered `T-a1`,
empties or populates the terminal receiver, establishes Gate T, coverage,
the deck/square bridge, `G2-PSC`/`G2-BD`, any `td` ceiling, or an AS109
lift.  The shape floor and the V37 verifications concern the raw row ideal
only.  Theorem A remains a `rho=0` radical/field-point screen with both
conversion debts open.  `H_K00` is a design, not a result.  No promotion is
made by this report; every verification here still needs the ordinary
different-model review gate to enter the ledger.

---

## 14. File-read / tool / edit disclosure

**Files read in full:** the seven prompt-listed inputs (hashes verified
first: `8e140384…`, `05400316…`, `d1f60700…`, `2c0fa61e…`, `0fbb4524…`,
`9c5bf122…`, `a049794b…`).

**Files read in part (replay custody chain):**
`cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_20260827/`
(`PREREGISTRATION.md`, `solve_graded_ladder_v37.py` lines 1–145,
`FREEZE.sha256`, both `RESULT.json` lane files, both `compiled/result.json`
files); `cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827/`
(`census_j2_typed_v23.py` — hash-checked, imported as the pinned parser;
`output_r1/RESULT.json` and its 42 `a1_ordered` chart output files via the
loader); the four prolong-export `result.json` manifests and their 28
grade-16–19 coefficient files (V28/V30/V33/V35, all hash-checked);
`cases/…_w19_tg19_7_compatibility_v39_20260827/ROW_BRIDGE.json` (metadata
fields only, to confirm the case exists — its results were **not** read);
directory listings of `cases/` and the V37/V39 case trees.  I noted the
existence of post-snapshot V38/V39 case directories from listings and file
names only and consumed no result content from either.

**Tools used:** `shasum`, `ls`, `find`, one `grep -r` file locate, `wc`,
Read, Grep, and `python3` for the desk replay (exact `Fraction` arithmetic,
< 5 s total, well under 1 GiB; no CAS, no Groebner engine).  Replay script
staged outside the repo at `/tmp/xreplay.py`, SHA-256
`05ff05db8d7171a853ef57d0cb7960659d12372f513fe3aaeb056ecdecf2ff36`.

**Edits:** this file,
`xmodel/ideation-20260827T0635Z-fable5-crossreview.md`, is the only
campaign artifact written or modified.  `/tmp/xreplay.py` was created and
edited outside the repository.

**Boundaries:** no network, no AWS access or job launches, no browsing, no
edits to any other campaign artifact, and no contact of any kind with
`jc2-lean` (not read, entered, built, status-inspected, edited, staged, or
cleaned).
