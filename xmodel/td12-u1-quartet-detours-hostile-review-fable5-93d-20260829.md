# Hostile review — TD12 U1 first-nonneutral quartet and detour analysis

Reviewer: Fable 5 (different-model hostile review)  
Date: 2026-08-29 UTC  
Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125` (verified = HEAD)  
Target: `xmodel/td12-u1-first-nonneutral-quartet-detour-analysis-sol56-93d-20260829.md`

Target seal recomputed and confirmed byte-exactly: body = first byte through
the `END-SEALED-BODY` marker line inclusive, `17030` bytes, SHA-256
`7204148ee85590dfc3d02d57340f6372e16997d11481c55652bfc630e3d652d4`.

## 0. Verdict

**REPAIRABLE.**

The headline theorem `TD12-U1-FIRST-NONNEUTRAL-QUARTET` is **REJECTED as
stated**: its codomain is wrong.  The deletion of the two remaining
epsilon-zero dirty rows `(k,nu)=(4,13)` and `(8,11)` by "their own terminal
budgets" is unsound, and I exhibit explicit budget-fitting formal
continuations from both rows, at exactly the tier at which the report's own
A7/C5 tails are constructed, robust under **both** promoted floor regimes
(AF2 `REPRESENTATIVE` and the promoted full-exit piecewise floor).  The
provable statement is a **first-nonneutral SEXTET**

```text
A7, C5, B25, S17, D13:=(k=4,nu=13)->(5/6,6), E11:=(k=8,nu=11)->(9/10,10),
```

all six budget-surviving.  Consequently the report's reduction "B/S landing
reduces to excluding the A7 and C5 detours" and its §7 claim that
`TD12-U1-DETOUR-EXCLUSION` (drafted over A7/C5 starts only) "proves the
conditional `TD12-U1-ACTUAL-LANDING`" are **false as stated**: two further
detour lanes must be excluded.

Everything else material survives attack and is **CONFIRMED**: the 13-edge
menu and its budget-10 exhaustiveness; the MP2/M=1 deletions; both A7/C5
tails row-for-row (P0, divisor, resolvent, N1, R1.0, strict NE, prices,
terminal psi/budget); every §4 vertex-local T1 solution with its guards; the
B/S-avoidance and non-realization firewalls; the cross-vertex-consumer
diagnosis; and the §5 global td-selector no-go.  The refutation
*strengthens* the report's own negative conclusion: B/S landing is even
further from provable than claimed.

No new exit price is asserted anywhere in this review; every lambda below
consumes the promoted AF2 rule or the promoted full-exit correction at a
declared cell.

## 1. Menu reconstruction and the deletions (charge 1): PASS except one hole

### 1.1 Independent reproduction

I re-enumerated the complete one-step P0 menu from `(w,M)=(9/2,2)` from the
printed laws only (`ladder/BOOK-OFFAXIS.md` §10 P0/P1/P2 + §6 R1.0–R1.4 +
the 2026-08-29 full-exit floor correction), with an exact-`Fraction`
scratch enumerator (`/tmp/quartet_review/qscan.py`), independently of the
producer's packet and of the trunk-consumer enumerator.  Filters enforced:
(S) strict, NE strict per orbit, (R) `dp != mu*dq` for every p-mult
(including `eps`), `kbar in Z>0`, `X in Z`, N1 `gcd(kbar,nu)=1`, R1.0
`gcd(M_F,nu)=1`, `E | l*num(w)*T`, `l | M_parent`, `m_j <= l-1`,
`eps <= l-1`.  Result, at AF2 price cap 12 (not merely 9 or 10):

```text
clean-resonant 0;  clean-neutral 2 (M'=1 via l=1; M'=2 via l=2, nu odd);
pure-epsilon   1 (l=2,eps=1: w->9, M'=1, lambda>=9);
dirty         10 = 6 eps=0 + 4 eps=1;  total 13.
eps=0: (k,nu) = (1,7),(1,25),(2,5),(2,17),(4,13),(8,11)   [prices 6,8,6,8,8,8]
eps=1: (1,2),(1,8),(2,4),(4,2)                            [all price 9, all M'=1]
```

Field-for-field agreement with the Opus-reviewed record (`86ccd2f1`) and
with the Grok primary (`ea43c281`).  No edge of AF2 price 10 exists even at
cap 12, and dropping my conservative extra `X in Z` filter changes nothing
(10 dirty rows either way).  So the target's §2 exhaustiveness claim at the
maximal budget 10 — which is Opus REPAIR 6a, correctly consumed — is
**CONFIRMED**, and is in fact cap-stable.

### 1.2 Sound deletions

- Clean-resonant emptiness: re-derived (all four `Delta | 9` candidates
  fail `kbar in Z` by the parity of `dq`).  **CONFIRMED.**
- Clean-neutral `M'=1`, pure-epsilon, and all four `eps=1` dirty rows have
  `M'=1`: for `l=2, eps=1, lex=0, Sm=k` one has `dp-dq=nu` and
  `dq ≡ 1 (mod nu)`, so `M=gcd(dp,dq) | gcd(nu,dq)=1` — a clean general
  proof, verified.  MP2 (trunk `M != 1`) kills them as interior rows, and
  P1's `M >= 2` kills them as terminals (their `w>1` does too).
  **CONFIRMED**, fully dead.
- The neutral-prefix logic (price 0, `(9/2,2)` preserved, menu a function
  of `(w, M, remaining budget)`, first nonneutral edge exists by finiteness
  plus `w=9/2>1` non-terminal): **CONFIRMED**.

### 1.3 The hole: the `(4,13)` and `(8,11)` deletions are unsound

The target deletes these rows because they "fail their own terminal
budgets" (`lambda=8` against own-terminal budgets 6 and 2).  That only
excludes terminating **at** them.  Printed P1 types the *last* trunk vertex;
no printed law forces a P1-shaped interior vertex to terminate — and the
target's own tails pass **through** the fully P1-shaped state `(6/7,7)`
(`w<1`, `M=7>=2`, `j=1 in N*`, own-terminal budget `5 <` spent `8`),
continuing to a cheaper terminal where `psi` drops from 6 to 1.  The same
move is available from `(5/6,6)` and `(9/10,10)`, and it fits:

**D13 witness** (from `(5/6,6)`, spent 8):

```text
(5/6,6) --D(l=6, m=(5), nu=49); cell (539,99); E=55; kbar=9; X=49;
          delta=4/5; lambda_AF2=1, lambda_FULL=2--> (2/11,11)
terminal: j=9, psi=1, budget 10;  total 8+1=9 (AF2, slack 1),
                                        8+2=10 (full-exit, slack 0).
```

Checks: `l=6 | M=6`; `m=5<=l-1`; NE `5*99=495<539` strict; (S) `594>539`;
(R) `539 not in {99,495,594}`; `kbar=9 in Z`; N1 `gcd(9,49)=1`;
`M_F=gcd(539,99)=11`, R1.0 `gcd(11,49)=1`; divisor `55 | 6*5*11=330`;
resolvent `55*(90-84)=330` exact.  Reduced T1 on `(539,99)` (two-root
pattern, `theta=49/9=nu(l+m)/(2nu+1)`): top coefficient cancels
identically, forced ratio `B/A=5/4`, constant `(245/36)A^2 != 0`, roots
distinct and nonzero, `rho=49/9` strictly between the multiplicities 5 and
6.  Exactly the same nondegeneracy pattern as the target's own five rows.

**E11 witnesses** (from `(9/10,10)`, spent 8) — six distinct one-step
fitting terminals exist under the **full-exit** floor alone, 36 under AF2.
Two representatives:

```text
(9/10,10) --D(l=10, m=(9), nu=47); cell (893,95); E=57; kbar=15; X=141;
            delta=2/3; lambda_AF2=1, lambda_FULL=2--> (6/19,19)
terminal: j=13, psi=1, budget 10; total 9 (AF2) / 10 (full-exit).

(9/10,10) --D(l=10, m=(6,6), nu=7); cell (154,22); E=66; kbar=3; X=21;
            deltas=(1/2,1/2); lambda=1+1=2 under BOTH floors--> (9/22,22)
terminal: j=13, psi=1, budget 10; total 10, both regimes.
```

The `(154,22)` witness uses `delta=1/2` cells — the identical robustness
class the target itself invokes for its H row.  T1 solves nondegenerately
at all of these: `(893,95)` forces `B/A=3/2`, constant `(141/10)A^2`;
`(154,22)` (three-root, `theta=7`) forces `B+D=3A`, `BD=3A^2`, constant
`-21A^3`, discriminant `-3A^2 != 0` — the same relations as the target's
own C5/A-middle rows.  All guards pass.

The `(893,95,47)` cell and the onward pure-epsilon `(1/2,12)` family were
moreover already verified by the producer's *own* later audit
(`xmodel/u1-star-pcb-independent-audit-sol56-93d-20260829.md` §6.3,
re-checking my `td12-occurrence-coverage-attack-fable5-93d-20260829.md`
aggravation 2): the state `(9/10,10)` at spent 8 reached via C5 admits
`(893,95) -> (6/19,19) -> (1/2,12)` at floors `1+1`.  The menu is a
function of `(w, M, remaining budget)` only — the target says so itself —
so the identical continuation attaches to the first-step `(8,11)` row.
The producer's own banked arithmetic refutes the producer's deletion.

Exhaustive scan (BFS over states, clean drops and resonant/pure-epsilon
families included, extra cost `<= 3`): from `(5/6,6)@8` there are 13
AF2-fitting completions (2 surviving the full-exit floor); from
`(9/10,10)@8` there are 36 (6 surviving).  Scratch-tier superset counts;
the load-bearing objects are the individually verified witnesses above.

I attempted to rescue the deletion and failed: no printed statement makes
a P1-shaped vertex absorbing (my earlier attack's B25-continuation point,
independently re-verified by the producer's audit §6.3, already
establishes non-absorption); MP2 does not fire (`M=6,10,11,19,22 >= 2`);
N1/R1.0/(S)/(NE)/(R)/divisor/resolvent all pass; the full-exit floor does
not close either row; a positive pole price would be needed to overrun the
budget, and the PASS-reviewed `POLE-EXIT-ZERO` (`8c872c12`) proves exact
`lambda=0` there.  **The deletion is unrescuable at this tier; the quartet
is a sextet.**

## 2. A7 and C5 tail calculations (charge 2): CONFIRMED

All five rows replayed exactly by hand and by the independent enumerator;
every displayed number is correct:

| row | cell | E | kbar | X | deltas | lam | child | checks |
|---|---|---:|---:|---:|---|---:|---|---|
| A7 | `(21,15)@7` | 9 | 15 | 21 | (6) | 6 | `(2,3)` | all pass |
| C5 | `(20,16)@5` | 12 | 12 | 15 | (3,3) | 6 | `(9/4,4)` | all pass |
| A-mid | `(63,28)@9` | 21 | 8 | 18 | (1,1) | 2 | `(6/7,7)` | all pass |
| C-mid | `(119,35)@17` | 21 | 15 | 51 | (2) | 2 | `(6/7,7)` | all pass |
| H | `(247,39)@19` | 26 | 9 | 57 | (1/2) | 1 | `(6/13,13)` | all pass |

Divisor checks `9|54, 12|72, 21|42, 21|252, 26|546` all verified; the
resolvent identity evaluates to `54,72,42,252,546` on both sides at all
five rows (noting, per the Opus trunk review §3, that the resolvent is an
algebraic identity whose entire content is `kbar in Z` — it is a re-check,
not an independent constraint); N1 gcds `(15,7),(12,5),(8,9),(15,17),
(9,19)` all 1; R1.0 gcds `(3,7),(4,5),(7,9),(7,17),(13,19)` all 1; strict
NE `15<21, 16<20, 56<63, 105<119, 234<247` (the target prints these as
`m_j*dq < dp`; correct).  Arrival divisibility `2|2, 2|2, 3|3, 4|4, 7|7`
along both chains.  Terminal: `j=13(1-6/13)=7 in N*`, `psi=1`, shared
budget `12-1-1=10`; tail floors `6+2+1=9 <= 10`, slack 1 — and the floors
are unchanged under the promoted full-exit correction (all deltas integral
except H's `1/2`, priced 1 under both regimes), exactly as §3.2 argues.
The §3.2 framing of the `L_safe` line as a numerical robustness check
rather than an invocation of the (absent) typed `s>=3` carrier is honest
and correct: the promoted attachment theorem is a **two-pole** theorem and
the carrier integration's own text confirms the td12 thirteen-edge menu is
untouched by the reprice.

Minor (cosmetic): §3.1 writes `C_P0 = l*k - Sm`; the printed law is
`C_P0 = l*(k+lex) - Sm`.  All displayed rows have `lex=0`, so no number is
affected.

## 3. Vertex-local T1 identities and guards (charge 3): CONFIRMED; no local kill exists

I re-derived the reduced Prop 8.1(iv) expression from `q = eta*Q(t)`,
`t = eta^nu` (it agrees with family C of `cases/l1_ode_check.py` and with
the Opus-confirmed form), then verified all §4 calculations by exact
multivariate polynomial arithmetic over `Q[A,B,D]` (three-root constants
checked in `Q(sqrt(-3))`):

- Two-root law: top coefficient vanishes identically given
  `theta = nu(l+m)/(2nu+1)` (true at all displayed rows); constancy is
  exactly `nu(lB+mA) = theta(nu+1)(A+B)`; constant `theta*A*B`.  Forced
  ratios and constants: A7 `3/2, (21/10)A^2`; C-middle `3/2, (51/10)A^2`;
  H `2, (38/3)A^2` — **all exact as printed**.  Nonzero-scale and
  distinctness guards pass (`ratio != 0,1`; `A != 0`; `rho` strictly
  between the two multiplicities at every row, so the R1.0 order-mu
  coefficients are nonzero).
- Three-root law: for C5 and A-middle the `t^2`/`t^1` conditions reduce
  exactly to `B+D=3A`, `BD=3A^2`; constants `-(15/4)A^3` and `-(27/4)A^3`;
  discriminant `-3A^2`, so `B,D` distinct, nonzero, and `!= A` (value at
  `z=A` is `A^2 != 0`).  **All exact as printed.**
- The C-middle `(119,35)` row agrees with the producer's banked six-cell
  record (`u1-star-pcb-independent-audit` §6.2 prints the same
  `B/A=3/2`, `(51/10)A^2`), as claimed.

Kill attempt: I tried to kill either detour locally and **it is
impossible at this tier**, confirming §4's obstruction claim — reduced T1
is nondegenerately solvable at every dirty row of both tails (and at every
witness row of the two extra detours), the budget fits with slack under
both floor regimes, `psi` at H is already minimal (`j=7`, `psi=1`), the
pole prices are reviewed exact zeros, and no reviewed filter fires.  §4.3's
scope statement (independent local scales; no transport, no Statement 3.9
instantiation, no actual child) is accurate and FALLACY-v2-compliant.

## 4. B/S avoidance and path legality (charge 4): CONFIRMED

Neither tail contains a B25 or S17 occurrence datum: the only `nu=17` row
(C-middle) is the cell `(119,35)` with `(kbar,X,M,w)=(15,51,7,6/7)`,
disjoint from S17's `(68,52)` with `(13,17,4,3/4)`; no row matches B25's
`(75,51)@25`.  Both tails are legal formal necessary-data paths for the
current P0/N1/R1.0/MP2/P1 system (every filter verified above), and the
target consistently refrains from calling them occurrences, realizations,
or glued source paths.  The `RETAIN ... AS ADVERSARIAL FORMAL FIXTURES`
disposition is correct — but the fixture set must now include the D13/E11
witnesses of §1.3.

## 5. Cross-vertex packet (charge 5): direction CONFIRMED, scope must widen

Confirmed: no promoted theorem supplies the missing cross-vertex
source/gluing consumer.

- Printed Statement 3.9 pins the sheet count law and the leading
  coefficient only; the Opus trunk review (charge 4, `PASS_WITH_REPAIR`)
  confirmed it is not applicable count-exactly to reduced patterns and
  that its sheet-level instance yields the index pin `i_F = 3n*i_G` —
  a linear pin on unbounded indices, not a gluing or a kill.
- The B bridge (`td12-global-source-bridge-b-fable5-92e`) is an exact
  interface functor "conditional on the occurrence witness ... none
  manufactures it" (its §8), and the S bridge states the same (§B5:
  "Nothing here proves the sibling cell occurs").  Quartet §1 items 6–7
  are accurate.
- The depth-24/depth-16 discriminator gates
  (`m2-td12-u1-next-trunk-discriminator-r1`, sibling exact charge
  `9b53f3ce`) are B/S-branch-conditional finite gates, not detour
  exclusions.
- The pole side is **stronger** than the target admits: §3.2's "the three
  U1 pole-entry prices are likewise not source-pinned" is stale.  The
  PASS-reviewed `POLE-EXIT-ZERO` (`m2-td12-pole-entry-price-r1`,
  `8c872c12`) proves exact `lambda=0` at all three actual pole vertices
  under its named Sigray-repair-tier conditions, for the displayed direct
  entries; the only residual is a hypothetical longer entry route with an
  interior chain vertex.  The hedge is safe-direction but §8 item 6 should
  cite and consume the reviewed zero rather than re-open it.

The §8 packet field list is the right minimal shape (pair+fibre, named
actual merge with place/component/edge, AP parameter and full indices,
serialized neutral prefix, finite Puiseux/source prefix, branch tags,
fixtures, T1 witnesses) with two mandatory amendments: (i) the branch tags
and fixtures must cover **four** detour starts `A7, C5, D13, E11` (and
step 7 must exhaust every in-budget first-nonneutral continuation, not
only A7/C5); (ii) step 6 should consume the promoted pole zeros.

## 6. Global caveat (charge 6): CONFIRMED

- REDUCTION T2 defines exactly `B_GGV = min gcd(deg P, deg Q)` over all
  counterexamples and its verdict states the selected pair's topological
  degree need not match a given counterexample's.  Quartet §1 item 1 and
  §6 item 1 are verbatim-faithful.
- The quantifier analysis is correct: fixed-`td` finiteness of the entry
  menu (`forall d, |E_d| < infinity`) neither bounds nor selects `td`,
  and Sigray normalization preserves the unknown `td`.
- The td=9 obstruction exhibit is real: `ladder/SHEET6-TDUNIFORM.md` §5
  records the hand-verified entry `(3,4), a=1, b=3, nu=4, Lambda=9,
  Q=(3,9,4,3,7), M=3`, zero-price IIa0 step, case-IV terminal `psi=2`,
  `Sum lambda = 0 <= 6`, slack 6 — a formal entry passing the entire
  promoted kill set at `td=9`.  So the local necessary-data axioms alone
  cannot imply `td=12`.  **CONFIRMED** (formal, not an actual pair — the
  target says so).
- U1-row uniqueness is sector-conditional (unique only after `td=12`,
  `m=3`, off-axis, `[2,2,2]`), per the confirmed residue inherited by the
  Opus trunk review.  §5's closing paragraph is accurate.
- §6 item 4 (Statement 9.6): verified against
  `xmodel/sigray-section9-source-audit-sol-ultra-20260828.md` §6.1 — the
  audited legal rows of (6.1) are `(k,n,nu)=(1,10,7),(2,7,5)` (producing
  exactly the A7/C5 cells `(21,15)` and `(20,16)`), the printed
  `(1,13,25)` fails (6.1) itself (left side 0, right side 27), and the
  raw-ratio solutions `(1,12,25)` and `(2,8,17)` violate `n ≡ 1 (mod 3)`
  (`(2,8,17)`: `nu(17-16)=17` with `8 ≡ 2`).  All three sub-claims exact.
  Independent two-way corroboration: the printed source's own legal 9.6
  rows are precisely the A7/C5 shapes, and its would-be `(75,51)` case B
  is phantom — B25/S17 come from the reviewed menu, not from St 9.6.

Both selector gaps G1, G2 stand, and G2 is now strictly harder than the
target states (four detour lanes, not two).

## 7. Strongest safe theorem

> **TD12-U1-FIRST-NONNEUTRAL-SEXTET (repaired).**  Under the target's
> hypotheses (exact normalized `td=12` Keller pair; named actual
> source-pinned `m=3` U1 equality merge with retained provenance;
> serialized clean-neutral `M=2` prefix), the first nonneutral trunk child
> `F` either already violates MP2 (all `M'=1` rows: the clean-neutral
> `l=1` row, the pure-epsilon row, and the four `eps=1` dirty rows;
> clean-resonant rows do not exist), or its reduced data are exactly one
> of the six epsilon-zero dirty rows
>
> ```text
> A7  (7,21,15,9,15,21)   -> (2,3)      floor 6   nonterminal detour
> C5  (5,20,16,12,12,15)  -> (9/4,4)    floor 6   nonterminal detour
> B25 (25,75,51,27,17,25) -> (2/3,3)    floor 8   P1-fitting terminal
> S17 (17,68,52,36,13,17) -> (3/4,4)    floor 8   P1-fitting terminal
> D13 (13,78,66,54,11,13) -> (5/6,6)    floor 8   nonterminal detour
> E11 (11,110,100,90,10,11)-> (9/10,10) floor 8   nonterminal detour
> ```
>
> and **all six are budget-surviving** at the current reviewed tier: B25
> and S17 fit as immediate P1 terminals (psi 2, 3; budgets 9, 8); A7, C5,
> D13, E11 each admit explicit budget-fitting formal continuations to
> B/S-free P1 terminals (the target's two three-step tails at total floor
> 9 against ceiling 10; the D13 witness `(539,99)@49 -> (2/11,11)` at
> total 9; the E11 witnesses `(893,95)@47 -> (6/19,19)` at total 9 and
> `(154,22)@7 -> (9/22,22)` at total 10), the D13/E11 witnesses fitting
> under the promoted full-exit floor as well.  Every dirty row on every
> named path has a nondegenerate reduced Prop 8.1(iv) solution, so no
> local budget/P0/N1/R1.0/T1 argument can prove B25/S17 landing.  Formal
> paths are necessary-data records, never occurrences or realizations; all
> floors are lower bounds, never attainment.

This is strictly stronger than the target's obstruction conclusion and
strictly weaker than its quartet claim; it is what the evidence supports.

## 8. Exact next lane

`TD12-U1-DETOUR-EXCLUSION/v2` at actual source-typed scope, with the
target's §8 packet amended as follows, in execution order:

1. widen the branch tags and adversarial fixtures to the four detour
   starts `A7, C5, D13, E11`, adding the Section-1.3 witness cells
   (`(539,99)@49`, `(893,95)@47`, `(154,22)@7`, and the pure-epsilon
   `(1/2,12)` family) with their T1 data as fixtures;
2. keep required steps 1–5 as drafted but instantiate Statements
   3.7/3.9/3.18 on all four lanes' rows, not only A7/C5's;
3. replace step 6 by consuming the PASS-reviewed exact pole zeros
   (`8c872c12`), retaining only the longer-entry-route rider;
4. step 7 becomes: exhaust every in-budget actual first-nonneutral
   continuation (sextet closure), retaining neutral prefixes and
   full-index exceptional classes.

Verdict grammar as drafted (`PROVED_DETOUR_EXCLUSION` /
`REFUTED_BY_ACTUAL_TAIL` / `SOURCE_TRANSPORT_OPEN`) is sound once "both
A7 and C5" reads "all four detour lanes".  Independent of that lane, the
two global selector gaps G1/G2 remain open exactly as the target states.

## 9. Findings ledger (non-blocking)

- **F1.** §3.2's "three U1 pole-entry prices ... not source-pinned"
  contradicts the PASS-reviewed exact `lambda=0` (`8c872c12`); safe
  direction, but v2 should consume the reviewed zero (§5 above).
- **F2.** §3.1's `C_P0 = l*k - Sm` omits `lex` (printed law
  `l*(k+lex)-Sm`); harmless here (`lex=0` throughout).
- **F3.** §2's proof never cites where budget-10 exhaustiveness was
  proved (it is Opus REPAIR 6a); it is true and now independently
  re-verified cap-stable, but the pin should be explicit.
- **F4.** The target's §9 input list omits the three parallel
  occurrence-coverage attacks banked at the same basis; the producer's own
  later audit (`u1-star-pcb-independent-audit` §6.3) verified the exact
  cells that refute the §2 deletion, so the collision was knowable.

## 10. Execution and custody disclosure

Read-only review at frozen basis; no web, AWS, commit, push, canonical
edit, heavy CAS, or external message; `jc2-lean` untouched in every sense.
Scratch: `/tmp/quartet_review/qscan.py` (exact `Fraction` arithmetic;
multivariate T1 checks over `Q[A,B,D]` and `Q(sqrt(-3))`; BFS completion
scans).  Artifacts consumed and verified this session: the target and its
seal; `m2-td12-u1-trunk-consumer-primary-grok46` (`ea43c281`) and its Opus
review (`86ccd2f1`); `m2-td12-u1-sibling-exact-charge-r1` (`306d69f6`);
`m2-td12-u1-next-trunk-discriminator-r1`; `m2-td12-pole-entry-price-r1`
review (`8c872c12`); `td12-occurrence-coverage-attack-fable5-93d`
(mine, prior session; its load-bearing cells re-verified here from the
printed laws); `u1-star-pcb-independent-audit-sol56-93d` §6;
`td12-source-interface-gap-coordinator-audit`; both B/S bridges;
`ladder/BOOK-OFFAXIS.md` §§6, 10 and the 2026-08-29 full-exit floor
correction; `ladder/SHEET6-TDUNIFORM.md` §5; `ladder/REDUCTION.md` T2;
`xmodel/sigray-section9-source-audit-sol-ultra-20260828.md` §6.1.  This
review asserts no occurrence, gluing, attainment, landing, degree bound,
panel closure, or JC2 consequence; all witness paths are formal
necessary-data records at reduced-superset scope, and every price cited is
a floor.  File written: this path only (plus `/tmp` scratch).

<!-- END-SEALED-BODY::td12-u1-quartet-detours-hostile-review-fable5-93d-20260829 -->

## Seal

- Body definition: every byte from the first byte through the unique
  body-end marker line above, including its terminating newline.
- Body byte count: `22585`.
- Body SHA-256:
  `3a35c6b764354cb8309b54cdd7f97745f66b435f284a9cb99aa19fbc1739b22d`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
