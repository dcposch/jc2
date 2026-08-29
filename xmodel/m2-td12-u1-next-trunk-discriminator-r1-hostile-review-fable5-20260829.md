# Fable 5 hostile review — td=12 U1 first-trunk discriminator (exact charge 8, depth-24 pure-power gate)

Lane: Fable 5, independent adversarial review, not primary. Date: 2026-08-29.
Basis commit at session start: `cd770c92e8307cffe82e985e54ba99abf6713459`.

Target:

```text
xmodel/m2-td12-u1-next-trunk-discriminator-r1-sol56-20260829.md
full  2a151eef1e661464ada47b0e387051733f9c2cb39cc7893366f5b1e09e15e829   (verified)
body  b25217e9b733efcc28d263c9df057d6ebcac61976002dd1c815e8063591caaae   (verified;
      all 12312 bytes before the target's own final Seal heading)
```

Worked only in `/Users/dc/code/math/jc2`. No access of any kind to
`jc2-lean`; no web, no AWS, no commit/push, no canonical edit, no heavy
computation (desk `python3` `int`/`Fraction` one-liners only). One file
written: this path.

All seven dependency hashes recomputed and matching the target's list:

```text
599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271  m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
91b36515950f038d08a444df16f9c09ee9763adb7950d46e9c50e43451f25c0f  m2-td12-u1-trunk-consumer-hostile-review-opus5-20260829.md
991e1b350ad2f8b2b82808fdc84dec71154f9ae17250c18953a36ac8f6588508  m2-td8-first-extra-jet-exact-lambda-primary-opus5-20260829.md
ec3557953c6387ce35dcf4efe1df267fb828771119c479eb00c8f1793e0ee370  m2-td8-first-extra-jet-exact-lambda-primary-hostile-review-fable5-20260829.md
8fd4d1d01bcb082b6f7dfd0ccb91cee072a1e7e2fdb6a319c099075b0b39a9de  m2-td12-pole-entry-price-r1-sol56-20260829.md
0159cdf18f9ad1c986677d4631916dbbef0b5310829958f6dac192eab2795a31  sigray-section7-full-independent-audit-sol-ultra-20260828.md
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933  sigray-section9-source-audit-sol-ultra-20260828.md
```

All dependencies were read in full this session. The mathematics below was
rebuilt from those pinned documents, not from the target's prose.

## 0. Verdict

**`PASS_WITH_REPAIR`.**

The headline is confirmed: for the reviewed td=12 U1 first trunk
`(nu_F, kbar_F, X_F, M_F, w_F) = (25, 17, 25, 3, 2/3)`, the B-direction
first-exit charge is exactly

```text
lambda_{F,B} = 8,
```

charge 9 cannot occur, and the next source gate is the finite depth-24
recursive pure-power test with a split first allowed at normalized level
25. I attempted charge-9 and early-split counterexamples inside the
reviewed grammar and every construction dies; the exclusion is in fact
overdetermined (two independent kill routes per parting mode, §8).

One repair is required (R1, §4): the target's §2 no-split proof, as
written, covers only partings into **distinct direction-orbits**. In the
orbit-level accounting that repaired Corollary 7.1 actually sums over —
the Section 9 audit states in terms that "cyclically conjugate roots in
one `eta^nu - c^nu` orbit count as one direction" and that only
*different* directions "give distinct cv vertices" — a parting of
deck-conjugate sheets within one orbit produces a **single** later
critical-value flag with `kappa_H/kappa_F >= 2`, not two flags, so §2's
"Those flags are distinct" does not close that mode. The mode is instead
killed by the target's own §3 machinery applied in the right order:
`tau_0 >= D_F/i = 25` holds with or without partings (Theorem A(2)+(5)),
so a conjugate parting forces weight `>= 2(25-17) = 16` and Corollary 7.1
gives `12 >= 17`, the same contradiction. With both modes closed,
`N == i`, `tau_0 = 25`, `r = 1`, `Delta = 8` follow exactly as printed.
The repair is a case split using only the target's own pinned
dependencies; no number changes and no new source datum is needed.

One provenance finding (F2, §5, non-blocking): the target's sentence
"Pole entry has independently been proved to have price zero" cites a
primary whose different-model hostile review is *recorded as completed
with verdict PASS* in
`xmodel/m2-td12-pole-entry-price-r1-hostile-review-fable5-20260829.run.v2`
(`final_status=DONE`, report SHA-256
`48525c6fbc9416cbeef7a12764173e0abf484c411b773767c6a6e593adcd53e6`), but
the named review report file is **absent from the workspace**. The
pole-zero claim is not load-bearing for the exact charge (it prices route
survival, not the 8-versus-9 discrimination), so this does not gate the
verdict; it should be regularized before canonical promotion.

Perimeter: nothing here (or in the target) is a landing theorem, a
full-book td=12 exclusion, a Keller-pair construction or counterexample,
or any JC2 consequence.

## 1. Charge 1 — the pinned row: PASS

Recomputed from the P0/R1.3 laws at
`(l,eps,k,lex,Sm,nu_F) = (2,0,1,0,1,25)` with parent `(w,M) = (9/2,2)`:

```text
dp=75  dq=51  E=27  kbar_F=17  X_F=25  M_F=3  w_F=2/3
j = M(1-w) = 1,  psi = ceil(3/1)-1 = 2,  budget td-1-psi = 9
AF2 gap = X_F - kbar_F = 25 - 17 = 8   (exact integer)
```

All match the trunk-consumer primary as corrected by its Opus review
(both hash-pinned above). `D_F = X_F * i = 25 i` is the DEPTH
i-normalization (`D_F/deg p_F = 25/75 = 1/3`, `deg p_F = 75 i`), and the
B-root has reduced multiplicity 1, hence full multiplicity
`mult(p_F, c) = i` for each `c` with `c^25 = B`.

Sheet indices: the trunk-edge count law (St 3.9(i), orientation confirmed
by the Opus review's charge 4) gives `i * 2 = i_G * 6n`, i.e.
`i = 3n * i_G`, which is verbatim Opus REPAIR 4a. For the displayed
*direct* pole entries the merge-arrival edge gives `2 i_G = 4` (arrival
reduced multiplicity 2 at G against the pinned full pole-top degree
`b_e * alpha = 4`), so `i_G = 2` and `i = 6n`. The target correctly
separates scope: the exact-charge argument is homogeneous in `i` and
needs only `i > 0` (`D_F/mult = 25i/i = 25` is `i`-free); the values
`i_G = 2`, `i = 6n` enter only the explicit gate degree
`deg gcd(C_1, C_1') = 6n - 1`, and they inherit the direct-entry
(zero-length pole chain) hypothesis, which P2's arrival law licenses but
does not force. That separation is exactly right and is preserved below.

## 2. Charge 2 — finiteness, cv flags, and the two-flag step: PASS with R1

**Finiteness and existence, per ray: PASS.** The gap `8 > 0` puts `F+B`
in `T_a^nearrow` (northeast test `D_F/mult = 25 > 17 = kbar_F`). The
Section 7 audit §3 proves repaired Statement 7.3 in the universal form —
"a ray containing any nearrow flag is finite," using Proposition 6.6
(nearrow persistence) exactly as the target cites, and repaired 7.2
supplies the **unique** critical-value flag on each such ray. So every
ray through the B-direction is finite and owns exactly one cv flag, and
`pi(H) > 1` (St 7.1), with weight `kappa_H(pi(H)-1) in N*` by the (INT)
upgrade confirmed in my td8 review. The target's review-risk 1 is
discharged at audit tier: the quantifier in the pinned source really is
"every ray," not "one selected continuation."

**Distinctness after a split: the loophole is real but closable (R1).**
Two rays that separate at a flag with `d_f > 0` cannot share any later
flag — the no-remerge tree order is sound, and a split at a level where
`d_f = 0` is precisely the level-25 endpoint case, so the case division
in the target is exact. However, "each acquires its own critical-value
flag ... distinct" holds only when the two sub-clusters leave through
**different direction-orbits** at the separation vertex. If the departing
sheet is a deck conjugate of the surviving ray (equivalently, the
separation sits at a characteristic exponent, a denominator jump), the
two post-split rays are conjugate, and the accounting that repaired
Corollary 7.1 sums over counts their cv data as **one** vertex — the
Section 9 audit says so expressly for direction counting, and the td8
Theorem F ledger (four cv vertices, weights 2,2,2,1, exhausting
`td-1 = 7`) is only consistent with that orbit-level reading. So a
conjugate parting yields one flag, not two, and §2's contradiction does
not fire for it.

Exhaustion of the leak (this is the R1 repair, all from pinned inputs):
let the selected ray be `P*` and let a sheet `S` depart at
`theta < tau_0`.

- If `S` is conjugate to `P*` (or agrees through the cv level with some
  conjugate of `P*` — the "rejoin via a conjugate" trick reduces to
  this), then `E` drops, so `r = kappa_H/kappa_F = E_+/E_0 >= 2`
  (Theorem A(4)); and `tau_0 >= D_F/i = 25` unconditionally (Theorem
  A(2),(5): `integral N = D_F` with `N <= i`). Hence
  `Delta_H = r(tau_0 - 17) >= 2*8 = 16` and Corollary 7.1 gives
  `12 >= 1 + 16`. Dead.
- Otherwise the cv flags of `S` and `P*` are distinct orbit-level
  vertices, both below the same B-direction, and corrected Statement 9.3
  prices **each** at `>= 8` (see charge 3). Corollary 7.1 gives
  `12 >= 1 + 8 + 8 = 17`. Dead.

Both modes contradict `td = 12`, so no sheet leaves the cluster before
the cv level and `N(tau) = i` on `(0, tau_0)` — the target's conclusion,
now for every parting type. The target's §3 sentence "neither a
characteristic-denominator jump nor a contact split" shows the producer
intends both exclusions; the printed §2 derivation delivers only the
second, and §3's `r`-exclusion is stated after `tau_0 = 25` has already
been asserted, which is circular for the jump mode as ordered. R1
reorders it; nothing else changes. There is no same-fibre identification
loophole beyond this: the terminal x-side witness lives in the other tree
component (St 3.3) and pole flags cannot be cv flags at all
(Prop 5.5 against repaired Prop 7.2).

## 3. Charge 3 — Statement 9.3 per flag, Corollary 7.1 against two flags: PASS

Corrected Statement 9.3 as repaired in the Section 9 audit (4.1) reads,
for `c* != 0`:

```text
kappa_H(pi(H)-1) >= D_F/mult(p_F,c*) - K_F,      K_F = kappa_F(1-u),
```

and it is quantified per ray: `F = I_P(u)`, exit child `G = F+c* = I_P(v)`,
`H = I_P(w)` the cv vertex *on that exit ray*, for any Puiseux ray `P`
through the exit child. With `mult(p_F, c*) = i` and `D_F = 25i` the
bound is `25 - 17 = 8` for **every** cv flag below the B-direction,
whatever the split profile — the bound's denominator is the multiplicity
at `F`, not the sub-cluster size, so a departed minority cluster is
priced at the same `>= 8`. The E6 sign repair this rests on has been
re-verified independently in at least two reviewed documents (my td8
review re-derived it from the proof's own chain and all three p. 53
usages).

Repaired Corollary 7.1 (Section 7 audit §8.4) is exactly the subset form
the target states: for a chosen subset `{F_1..F_n}` of `T_{a,cv}`,

```text
td >= 1 + sum_i kappa_{F_i}(pi(F_i)-1),
```

valid because omitted baselines are positive ((INT)) and `delta_a^cl >= 0`
(repaired 7.4). Two distinct flags of weight `>= 8` give
`12 >= 17`, impossible. This uses the actual-weight ledger only — no
first-separation ownership convention, no exit-set disjointness (4.2/4.3)
— so the target's review-risk 3 claim of ownership independence is
correct. Subject to R1's caveat that "distinct" must mean distinct
orbit-level cv vertices, this charge is clean.

## 4. Charge 4 — one flag forces `N == i`, `tau_0 = 25`, `r = 1`, charge 8: PASS (with R1 ordering)

Given no parting of either mode (§2 repaired):

- `N(tau) = i` on `(0, tau_0)`, so the exact descent integral (Theorem
  A(2), confirmed in my td8 hostile review) gives
  `25i = D_F = i * tau_0`, hence `tau_0 = 25` exactly.
- `r = kappa_H/kappa_F = E_+/E_0` is a **positive integer** (Theorem
  A(4): `E` is a divisor chain; confirmed at printed scope in my td8
  review), and no parting gives `E_0 = E_+`, i.e. `r = 1` directly.
- Independently, the td12 budget forces `r = 1` even without that:
  `12 >= 1 + Delta_H = 1 + 8r` (Corollary 7.1 with the single flag) kills
  `r >= 2` since `1 + 16 = 17 > 12`. The target's parenthetical that the
  psi-sharpening to `12 >= 1 + 2 + 8r` is available but unneeded is
  correct (the x-side witness carries integral weight `>= psi = 2` when
  `psi*l_f < k_f`, and sits in the other component, hence distinct).

Hence `Delta_H = r(tau_0 - kbar_F) = 1 * (25 - 17) = 8` exactly, and
`lambda_{F,B} = 8` under both the literal and the first-separation
ownership conventions (with a single flag there is no ownership
ambiguity). Charge 9 would need `tau_0 = 26` at `r = 1`, i.e. shed
branch-area `i`, i.e. a parting — both parting modes are dead (§2). The
`{8,9}` window of the trunk-consumer review is genuinely closed to `{8}`.

## 5. Charge 4a — pole-price footnote (F2, non-blocking)

The exact-charge argument nowhere needs the pole prices: the two-flag and
`r >= 2` contradictions use only the flags themselves. Pole prices enter
only route survival (`8 <= 9` fitting). The cited pole note derives
`Y(P_i) = empty`, `lambda = 0` from Prop 5.5 (a ray through a pole flag
has `g(P) = infinity`) against repaired Prop 7.2 (a ray carrying a cv
flag has `g(P) in C`) — a mechanism I checked and find sound at its
stated tier, and which moots the Opus review's REPAIR 5a `+3` scenario.
But its different-model hostile review exists only as a run record
(verdict PASS, `final_status=DONE`) whose report file is missing from the
workspace. The target's "independently been proved" should therefore be
read "proved at producer tier with a recorded but non-archived PASS
review." Regularize before promotion; no effect on this verdict.

## 6. Charge 5 — endpoint and indexing of the gate: PASS

- With no parting before `tau_0` there is no characteristic exponent
  below `tau_0`, so the ray's denominator stays `kappa_F` and the
  admissible levels are exactly the integer normalized levels
  `tau = 1, 2, ..., 24` strictly between 0 and `tau_0 = 25`: no skipped
  and no fractional levels. A fractional-level split *is* a denominator
  jump and is already dead by the `r >= 2` route, matching the target's
  "immediate rejection on any earlier characteristic-denominator jump."
- The target's graded pieces `P_k` are the `kappa_F`-graded objects —
  i.e. it builds on the R1-repaired indexing from my td8 review
  (`P_{k'} = p_{n - (kappa/kappa_F)k'}`), not the vacuous ambient-kappa
  layers. Correct.
- `C_1(z) = sum_k [(eta-c)^{i-k}]P_k z^{i-k}` is verbatim the derived
  child-pattern law (C) with the vanishing ladder (V) making the diagonal
  extraction exact; `c_0 != 0` is St 3.9(ii). A level with vanishing
  subdiagonal data gives `alpha_k = 0`, a legal pure power — so the gate
  never stalls.
- Pure power `<=>` `deg gcd(C_1, C_1') = i - 1` (given `a_0 != 0`,
  degree exactly `i`), `<=>` the binomial list
  `a_k = a_0 * C(i,k) * (a_1/(i a_0))^k`, `2 <= k <= i` — identity
  desk-verified. For direct entries `i = 6n`, test degree `6n - 1`.
- Endpoint: a split at exactly level 25 sits at the unique cv flag
  (`d = 0` there defines `u_0`), creates no earlier flag, and leaves
  `integral_0^{25} N = 25i` intact; charge stays 8. Not excluded, exactly
  as the target says. (A *conjugate* split at 25 would jump `kappa_H`
  and is separately dead by budget, but the gate does not need that.)
- The gate is **necessary only**: passing all 24 levels does not lower
  the price below 8, failing any level contradicts td=12 — with R1's
  phrasing fix that a failure forces "two `>= 8` flags **or** one
  `>= 16` flag," either of which kills. The target's claim of provisional
  usability without further review rounds is fair for a necessary test.

## 7. Charge 6 — A/B interpolation and residue/degree audit: PASS at formal scope only

All arithmetic verified:

- `N_1 = (-kbar_F) mod nu_F = -17 mod 25 = 8`; `8^{-1} = 22 (mod 25)`
  (`8*22 = 176 = 7*25 + 1`); Theorem D(ii) with `D_F = 25i ≡ 0 (mod 25)`
  gives `e_k ≡ 22k`, and `e_k ≡ k e_1` for all `k` — the pure-power
  residue progression, so semi-invariance does not obstruct the gate.
  (Same formula reproduces the td8 pins `(2,0,4,1)` and `(10,0,12,7)`;
  cross-checked.)
- `P_k = eta^{e_k}(T-A)^{2i-k}(T-B)^{i-k}R_k(T)`, `deg R_k <= 1`, meets
  the vanishing ladder exactly (`2i-k` at the chain orbit, `i-k` at the
  extra orbit), carries residue `e_k`, and has
  `deg P_k <= e_k + 25(3i - 2k + 1) <= 75i`, closest case
  `k=1: 75i - 3 < 75i`. Verified.
- The arrival diagonal at `a` (`a^25 = A`) is a nonzero unit times
  `R_k(A)` and the B-diagonal at `c` is a nonzero unit times `R_k(B)`;
  `A != B` (ratio `9/8`), so degree-one interpolation chooses the two
  independently. So the known arrival transport can be retained while the
  first B-child is set to any on-residue pure power. Verified.

This proves exactly what the target claims and no more: **formal**
top/weight/arrival/degree compatibility. It does not couple the g-side
recurrences, does not solve constant-Jacobian lower terms, does not
construct `(f,g)`, and does not land the source; the target's §5 closing
disclaimer and risk 5 state this correctly, and I do not upgrade it.

## 8. Counterexample attempts (all fail)

1. **Charge 9, no split** (`r = 1`, `tau_0 = 26`): the integral forces
   shed area `i`, i.e. a parting; both parting modes contradict td=12
   (`17 > 12`). Unconstructible.
2. **Charge 9 via ramification** (`r >= 2` with small `tau_0`):
   `tau_0 >= 25` always, so `Delta >= 16`. Unconstructible; also `8r = 9`
   has no integer solution.
3. **Cheap departed flag**: corrected 9.3's denominator is
   `mult(p_F, c*) = i` at `F`, independent of the departing sub-cluster's
   size, so every flag below B costs `>= 8`. No cheap second flag exists.
4. **Flag identification**: departed-vs-surviving flags can only merge in
   the ledger via deck conjugacy, which is the `r >= 2` mode (dead);
   x-side and pole flags are in the wrong component / cannot be cv.
   No identification escape.
5. **Split exactly at 25 with charge drift**: `N` on `(0,25)` is still
   `i`, `tau_0` still 25, charge still 8. No drift.
6. **Fractional/skipped gate levels**: fractional means denominator jump
   (dead); "skipped" cannot occur since `c_0 != 0` at every level and
   `alpha_k = 0` is a legal pure power. No gate evasion.

## 9. Maximum safe consequence and perimeter

For the two reviewed P1-fitting td12 terminals of the U1 row:

> On the charged `(2/3,3)` terminal at `nu_F = 25`, conditional on the
> reviewed row and on the pinned repaired source package: every
> configuration surviving td=12 has exactly one critical-value flag below
> the nearrow B-direction, `N == i`, `tau_0 = 25`, `kappa_H = kappa_F`,
> and exact first-exit charge `lambda_{F,B} = 8`; the value 9 is
> excluded. Consequently the route's slack against the shared ceiling 9
> is exactly 1 given the derived merge zero and the producer-tier pole
> zeros (F2). The next source gate is the necessary depth-24 recursive
> pure-power/denominator test, with a split first allowed at level 25;
> its first failure kills the whole U1 row at td=12. For the sibling
> `(3/4,4)` terminal at `nu_F = 17` nothing here computes its charges;
> its own-budget-8 status is untouched.

Explicitly not established, by the target or by this review: landing or
realizability of any cell by a polynomial pair; the lower Keller
recurrences; a full-book td=12 exclusion or panel change; any
counterexample; any td ceiling; any JC2 consequence. The target's own §7
risk ledger is accurate except that risk 2 understates the conjugate mode
(subsumed by R1).

## 10. Findings summary

| # | item | verdict |
|---|---|---|
| 1 | pinned row, `i_G=2`, `i=6n`, `D_F=25i`, `kbar=17`, mult `i`, gap 8, `psi=2`; scope separation exact-charge vs direct-entry | **PASS** |
| 2 | per-ray finiteness + unique cv flag (Prop 6.6 / repaired 7.3) | **PASS** |
| 2' | "two distinct flags" after a split | **REPAIR R1** — distinct-orbit partings only; conjugate partings give one flag with `r >= 2`, killed by `tau_0 >= 25` + Cor 7.1; conclusion unchanged |
| 3 | corrected St 9.3 gives each flag `>= 8`; Cor 7.1 kills two flags, ownership-free | **PASS** |
| 4 | `N == i`, `tau_0 = 25`, `r in N*`, budget forces `r = 1`, exact charge 8, 9 excluded | **PASS** (order via R1) |
| 5 | endpoint/indexing: 24 integer levels, split allowed at 25, gcd/binomial test, no skipped/fractional levels | **PASS** |
| 6 | interpolation and residue/degree audit | **PASS at formal-compatibility scope** |
| 7 | perimeter / no overclaim | **PASS** (with F2 provenance note on the pole-price review artifact) |

Smallest remaining source datum: unchanged from the target's §6 — the
first B-child coefficient vector `([(eta-c)^{i-k}]P_k)_{k=1..i}`
(equivalently the cluster's first contact level), extracted from the
source polynomial identities or a Keller/transport recurrence.

## Seal

Body SHA-256 (all bytes before this `## Seal` heading): `8ef16e10a62e7723f1294bf345b2ea23164add2b490df08ec061fcff17409895`
