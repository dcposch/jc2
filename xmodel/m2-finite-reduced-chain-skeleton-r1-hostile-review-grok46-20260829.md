# Hostile review: finite reduced P0 chain skeleton (R1)

Date: 2026-08-29.  Reviewer: Grok 4.6, independent of the Sol56 producer
lane.  Charge: falsify or verify the cap-free finiteness theorem for
**reduced P0 chain states** `(w,M)` at a fixed numerical lambda budget,
together with the charged `(w,M)=(3/2,2), B=5` census and the first td-7
case-III special-`nu` discriminator.  This is not the general `(w,M)`
budget quotient already treated in
`xmodel/m2-budget-quotient-falsifier-grok46-20260829.md`.  That earlier
verdict is not transferred by analogy.

No `jc2-lean` access.  No git inventory.  No web, AWS, Singular, msolve,
Sage, PARI, or heavy CAS.  No canonical edit, commit, or push.  Bounded
exact-rational Python only, including copy-mutations under `/tmp`.  The
packet and producer report were not modified.

## Verdict

**`PASS_AT_STATED_CHAIN_SCOPE`**

Conditional on the imported P0 sheet laws in `ladder/BOOK-OFFAXIS.md` §10
(with R1.0–R1.2 and R2.1–R2.2 as cited), the reachable reduced chain
states `(w,M)` from a fixed entry `(w0,M0)` at a fixed numerical budget
`B` form a finite, effectively computable set.  No global cap on `k`,
`lex`, `num(w)`, `M`, or `nu` is required.  Zero-cost/neutral moves,
unpriced `lex`, and case-III arrivals do not produce an infinite reduced
chain at fixed `B`.  No concrete counterchain was found.

The charged census is independently reproduced: 69 states, 295 edges,
max reduced numerator 3, max `M=25`, state-table SHA-256
`c2835aaf8450ab938170ae3808b5852d53f2c7b1ae29b14ca77b7965bf37f1ad`,
exact `(w,M,lambda_min)` equality with current `book_offaxis.close_p`,
and P5's "70 states" is stale.  The 69 is not a collapsed duplicate of
70 legal reduced states, and the missing 70th slot is not a legal P0
state omitted by both engines.

The td-7 case-III ZCH equation `g*((3h-4)l-2)=3h` follows from the
R2.1 handshakes and the R2.2/P3 shape.  On the declared domain (odd
`h>=3`, `l>=1`, `g>=2`) the unique solution is `(h,l,g)=(3,1,3)`, and
every odd `h>=5` is empty.  The packet does not silently generalize this
to other partners or merge types.

This theorem may replace only P5's claim that the reduced P0 chain
numerator/`M` is unbounded at one fixed entry and budget.  It does not
replace a finite full book quotient, merge finiteness, landing
completeness, a cofinal topological-degree bound, or JC2.

---

## 0. Custody

Producer report, hashes verified on this host before the mathematical
work:

```text
full   239393d7747b6166544342100cfe56b9353860fc7f36cd31620f8fdd04299bad
body   8587625b2f12e486f9a3a3773ee5f4dcac7f853edcaddf69221dbab9ea7b1bcb
```

Body bytes are those strictly before the final `---` separator line,
including the blank line after the scope-firewall paragraph (cut at
byte 7815).  Packet principal hashes, verified:

```text
6e413ff68a0b75f6a7fe28e091f1989b5cb74ed5f2d0f123630cb7520add8218  finite_chain_skeleton_r1.py
cd80757dd068c2af6bc1d0c2e15575e7a696224664dffa9645fc877c144ac38e  test_finite_chain_skeleton_r1.py
f064e0930dc11d05c7276fa0420418ecf1efc62eed9a9b10a69bc626b88fa558  td7_caseiii_special_nu_r1.py
f4cfa83df42cd38975482160848bc35146f8c26a5c66a7f5b5190638201ab7a8  test_td7_caseiii_special_nu_r1.py
```

Cited sources actually read, hashes as on disk this session:

```text
34f5ea9db62caf1da8b436733752e86402ff3f3ee08bc5096f13f8bf0c80eb17  ladder/BOOK-OFFAXIS.md
ad9ced6c0420902f8cf63edf3636bed8633be511e925f208d24a24c35d71036d  ladder/SHEET6-DEPTH.md
93adb7acedf4cf0fd56ffc68e4571649a04eab12e1271431449a79465a964bcb  ladder/SHEET6-MULTIPOLE.md
df776b25565fb43c2f45fd8bc64db822d5775822b834fa58fe7f45db2f1a4e54  xmodel/m2-budget-quotient-falsifier-grok46-20260829.md
11567cee68df5cd11965ea5eb9515f9a5bcb8b54fa7174f8abe105ccf2992dc5  cases/book_offaxis.py
```

Ordinary and `python -O` packet tests both printed
`FINITE_CHAIN_SKELETON_R1_TEST_PASS checks=35` and
`TD7_CASEIII_SPECIAL_NU_R1_TEST_PASS checks=17`.  Charged JSON with
`indent=2, sort_keys=True` plus trailing newline hashes
`74f82b75fade7464dde5e9b57adb418110c0c8fc576a62a4898ef678c487cb18`,
matching the producer.  td-7 emitted JSON hashes
`1e70f2e384eace6b325753a752e1db9247f7e07ba29dbdc2548440bdbba4f3b5`.

---

## 1. Charge 1 — cap-free finiteness from the literal P0 laws

### 1.1 The chain grammar actually used

P0 (`BOOK-OFFAXIS.md` §10, lines 480–509) at a chain vertex with arrival
multiplicity `l | M_parent` (St 8.4):

```text
p = ⊖ eta^eps (eta^nu - c^nu)^l Π_j (eta^nu - d_j^nu)^{m_j},
q = ⊖ eta · (simple orbits),
E := l·dq - dp > 0,
kbar = l·w·dq / E ∈ Z   (nu >= 2),
w'   = l·w·(dq-1) / (nu E),
M'   = gcd(dp, dq),
lambda >= Σ_j max(1, ceil(X/m_j - kbar))
         + [eps >= 1]·max(1, ceil((X/eps - kbar)/nu)).
```

NE laws are strict: `eps·dq < dp` and `m_j·dq < dp`.  Equality is the
root-mult law (R) from R1.0.  Clean/neutral steps (`eps=0`, `k=0`) cost
0.  Every non-clean step costs at least 1, so `B` bounds the number of
non-clean steps.

The extra-present identity claimed by P0(i) is necessary, not merely a
search heuristic.  The shape identities

```text
C = l(k+lex) - Sm,     T = Sm + l - eps(1+k+lex),
E = (l-eps) + nu·C,    C·dq - (1+k+lex)·E = -T
```

give, whenever `kbar ∈ Z`,

```text
l·a·T = E · [l·a·(1+k+lex) - C·d·kbar],
```

hence `E | l·num(w)·T`.  Combined with `nu >= 2` one has
`l + 2C <= E` when `eps=0`, so `E` ranges over a finite divisor list
once `T` is bounded.  The packet's divisor loop is therefore complete
for dirty steps, then filtered by the actual integrality, NE, and price
tests.

`C = 0` occurs if and only if `k = Sm = lex = 0`.  For `k >= 1` the
bounds `k <= Sm <= k(l-1)` make `C = 0` impossible at `l >= 2`.  The
P0 partition into clean/neutral, pure-`(b)`, and extras-present is
therefore exhaustive on the chain layer.  Arrival `l = 1` has no dirty
or pure-`(b)` menu (R1.3: `μ=1` arrivals have no northeast non-chain
root); only clean steps remain.

### 1.2 Zero-cost layer, `eps = 0` and `eps > 0` separately

**Neutral (`n=1`, `eps=0`, `k=0`).**  R1.1/R1.2 give
`(dp,dq) = (l nu, nu+1)`, `Δ = 1`, `w' = w`, `M' = gcd(l, nu+1)`.
Every such `M'` divides `l` hence divides `M`.  Reduced `w` is fixed.
The free `nu` ray is real (Statement 9.6(v); this reviewer's earlier
`S(t)` family) but is invisible to the reduced pair.  Every divisor of
`M` occurs for some `nu >= 2`: the packet's emission of all `M2 | M` is
exact, not a relaxation.

**Resonant clean (`n >= 2`, `eps=0`, `k=0`).**  `Δ = (n-1)nu+1 >= 3`
divides `num(w)`, and `den(w) | dq`.  For `n >= 2` and `nu >= 2` one has
`n < Δ` strictly (`n < (n-1)nu + 1` reduces to `ν > 1`).  Writing
`w = a/d` in lowest terms and `a = Δ a'`, the unreduced numerator of
`w'` is `a' n = a n / Δ < a`.  Reduction by `gcd(a'n, d)` cannot
increase it.  So `num(w') < num(w)` in positive integers, a well-founded
descent.  Also `M' = gcd(l, dq)` divides `l` divides `M`.  Zero-cost
resonance cannot raise `M` and cannot cycle on reduced `w`.

The packet skips `eps=0, k=0` inside the dirty loop
(`finite_chain_skeleton_r1.py:237-238`).  That skip is correct: those
parameters are the clean family, already enumerated under R1.2's
stronger `Δ | num(w)` rather than the weaker dirty divisor bound
`E | l a T`.  Including them as dirty would risk emitting illegal
clean-looking steps.

**Pure-`(b)` (`k = lex = Sm = 0`, `1 <= eps < l`).**  Cost
`ceil(l w / eps) >= 1`.  Collapse: `w' = l w / (l-eps)`,
`M' = gcd(l-eps, nu+1) | (l-eps)`.  The only free parameter is `nu`.
Integrality `kbar = l w (nu+1) / (l-eps) ∈ Z` is
`d(l-eps) | l a N` with `N = nu+1`.  Both this congruence and `M'`
depend on `N` only modulo `lcm(l-eps, (d(l-eps))/gcd(d(l-eps), l a))`.
Each residue class with `N >= 3` is a legal representative.  Residue 0
is the class `N ≡ 0 (mod modulus)`; since the modulus is a multiple of
`E = l-eps`, `gcd(E, N) = E` on that class, consistent with
`gcd(E, 0) = E`.  Finite reduced outputs, finite exact residue classes.
`M'` cannot increase.

**Dirty, `eps > 0`.**  Each of the `k` northeast p-orbits costs at
least 1 and the epsilon root costs another, so
`k + 1 <= remaining budget`.  Then `k <= Sm <= k(l-1)`.  The constraint
`T >= 1` rearranges to

```text
lex <= floor( (Sm + l - eps(1+k) - 1) / eps )
```

and the next integer makes `T <= 0`, i.e. `eps·dq >= dp`, forbidden by
NE or (R).  This bound is necessary and, as a loop envelope, sufficient
for finiteness.  Independent check at the packet's unit-test point
`(l,eps,k,Sm) = (6,2,1,4)`: bound 2, `T(lex=2)=2 >= 1`, `T(lex=3)=0`.

**Dirty, `eps = 0`.**  `T = Sm + l` is independent of `lex` and at least
`l >= 2`.  Then `l + 2C <= E <= l a T` forces

```text
C <= floor( (l a T - l) / 2 ),
lex <= floor( (Cmax + Sm) / l ) - k.
```

The next `lex` violates `l + 2C <= l a T` before any divisor is
considered.  Unpriced `lex` is therefore bounded at a fixed state by
P0 inequalities, not by a search cap.  Python-loop termination for
`eps=0` in the packet *does* rely on this derived bound: there is no
inner `break` analogous to legacy `if 2*C > l*a*T`.  If the bound were
too small, legal successors would be omitted; if absent, the `eps=0`
loop would not be a finite `range`.  Completeness of the bound was
checked by inflating it by 50 at `(w,M,B)=(4/3,3,3)`: same 51 states,
same 177 edges, same state hash.  Forcing `lex <= 0` there dropped one
edge (177 → 176) and **no state**.  Unpriced `lex` can enter the chain
layer as a dirty parameter; it cannot grow a reduced coordinate at
fixed `B`.

### 1.3 Why reduced `num(w)` and `M` cannot run away at fixed `B`

Non-clean steps number at most `B`.  Expansions are pure-`(b)` (cost
grows with `w`) and dirty `w' = l w (1+k+lex)/E`.  For large `lex` at
`eps=0`, `E ~ nu C ~ nu l lex` and `w' ~ w/nu < w`.  For budget-bounded
`k` the dirty expansion factor is a function of the current finite
`(w,l, remaining)`.  `M' = gcd(dp,dq)` on a dirty step satisfies
`M' | E <= l a T` with `T` bounded by current `M` and remaining
`k,lex`.  Pure-`(b)` and clean cannot raise `M`.  Bootstrap from finite
`(w0,M0)`: after at most `B` non-clean steps the reduced set is finite.

Case-III arrivals are merge handshakes (R2.1), not chain transitions.
They consume last-vertex `nu`, which the reduced record deliberately
forgets.  They do not add a chain successor.  Last-vertex `nu`,
`kbar = w(nu+1)` on the neutral ray, and full pattern degree remain
unbounded at cost 0; they are not reduced-state coordinates.

### 1.4 No counterchain

A putative infinite reduced chain at fixed `B` would need either
infinitely many non-clean steps (forbidden by price) or an infinite
zero-cost path in the reduced graph.  Zero-cost edges strictly decrease
`(num(w), M)` in the lexicographic well-order of `N* × N*` (resonance
drops numerator; neutral drops or preserves `M` at fixed `w`).  No
infinite reduced path exists.  Explicit small-budget closures:

```text
(3/2,2) B=0:  exactly {(3/2,1), (3/2,2)} at cost 0
(3/2,2) B=1:  same two states (cheapest non-clean costs 2)
(1,1)   B=0,1,2: singleton (no dirty at l=1, no resonance Δ|1)
```

Copy-mutations designed to create an omitted or infinite successor
behaved as the proof predicts: `dirty_lex_bound ≡ -1` collapsed the
charged closure to 4 states (the zero-cost pair plus the two pure-`(b)`
landings); skipping the dirty family did the same; skipping pure-`(b)`
dropped 69 → 48.  Inflating the lex envelope did not nonterminate and
did not add states.

---

## 2. Charge 2 — implementation versus the mathematical state space

The instrument in
`cases/m2_finite_reduced_chain_skeleton_r1_20260829/finite_chain_skeleton_r1.py`
implements the grammar of §1 with no historical global cap.  Broader
token scan than the packet's test: `PCAP`, `10**4`, `M > 200`,
`range(0, 41)`, `NCAP`, `max_nu`, `nu_cap`, `STATE_CAP`, `4000`,
`for k in range(0, 7)` are all absent.  Loop bounds that remain are
derived (`divisors(num(w))`, `kmax = remaining - [eps>=1]`,
`dirty_lex_bound`, `divisors(l a T)`).

Independent enumerator, written for this review, differs from the
packet in the dirty-lex terminator: it advances `lex` until `T <= 0`
(`eps>0`) or `l+2C > l a T` (`eps=0`), with a tripwire at 5000 solely
to detect a true infinite family.  Pure-`(b)` `M'` is collected by
brute `N` over eight modulus periods, not by the packet's residue
loop.  On every compared instance the two closures agreed on the state
set, the min-cost map, and the expanded-edge count:

```text
(3/2, 2, B=5)  69 states, 295 edges, hash c2835aaf...
(4/3, 3, B=3)  51 states, 177 edges, max_lex observed 1
(5/4, 4, B=3)  58 states, 203 edges, max_lex observed 1
(3/2, 2, B=0,1,2), (1,1,B<=2), (2,1,B<=2),
(4/3, 3, B<=2), (3/4, 4, B<=2), (5/2, 2, B<=2): all exact matches
```

The tripwire never fired.  `Fraction(6,4)` as input collides with
`Fraction(3,2)` after normalization, as it must; the closures hash
equal.

Hidden-cap / omitted-branch / cache / assertion audit:

- **No cached-versus-derived invariant.**  Menus are recomputed from
  `(w,M, remaining)` at the first Dijkstra visit.  Remaining is
  maximal at min cost, and `one_step(·, R)` is monotone in `R`, so
  first-visit expansion is complete for reachability.  Legacy
  `_PSTEPS` caching is not used.
- **`require` is not `assert`.**  Optimized Python does not strip it.
  `-O` replay of the charged closure reproduced the state hash.
- **`k=0, eps>0, lex>=1` is kept** (q-extras plus epsilon, no NE
  p-orbit).  `C = l lex >= l >= 2`.  Not silently dropped with clean.
- **Permissive k-loop.**  Replacing `kmax = remaining - [eps]` by
  `kmax = remaining` did not change the charged 69/295: the price
  filter still rejects `k` that cannot be paid.  The subtraction is a
  tightener, not a completeness patch, at this instance.
- **Pure-`(b)` over-approximation is the legacy engine's, not the
  packet's.**  Forcing the packet to emit every divisor of `E` as `M'`
  left the charged **state hash unchanged** and raised edges 295 → 347.
  Those extra edges are illegal or redundant at this instance (see
  Charge 3).  The packet's congruence census is the correct reduced
  quotient of the free-`nu` family.
- **Test gap, not a theorem gap.**  The 35-check file locks the charged
  golden values and a few formula identities.  It does not call
  `close_p`, does not lock a `lex > 0` closure (charged
  `max_lex_observed = 0`), and the cap-token list is syntactic.  A
  mutation that omitted only `lex > 0` dirty steps would still pass
  the charged golden lock.  Independently, `(4/3,3)` at `B=3` does
  exercise `lex=1` and still matches.

Dijkstra `first_predecessor` uses `setdefault` on first *push*, not on
the min-cost pop.  Two charged states therefore record a strictly
suboptimal witness path, while `lambda_min` in the state table is
correct (Charge 3).  This is a witness defect, not a finiteness defect.
Minimal reproducers from the charged payload:

```text
state (2/9, 9): lambda_min = 4, recorded path
  (2/7, 7) at 3  --dirty, cost 2-->  claimed 5
state (1/2, 1): lambda_min = 4, recorded path
  (3/10, 10) at 4  --pure-epsilon, cost 1-->  claimed 5
```

Location: `finite_chain_skeleton_r1.py:319-325`.  The state-table hash
does not include predecessors, which is why the golden lock is silent.

Residue 0 in a stored pure-`(b)` witness means `N ≡ 0 (mod modulus)`,
i.e. `N = modulus, 2 modulus, ...`, not `nu = -1`.  A later consumer
that treated the integer 0 as a literal `N` would be wrong.  The
reduced skeleton itself never materializes `N=0` as a vertex.

---

## 3. Charge 3 — charged `(w,M)=(3/2, 2), B=5`

Independently reproduced, three ways, all exact:

| quantity | independent P0 enumerator | packet | current `close_p` |
|---|---|---|---|
| `state_count` | 69 | 69 | 69 |
| `expanded_edge_count` | 295 | 295 | (not reported; state map agrees) |
| `max_reduced_w_numerator` | 3 | 3 | 3 |
| `max_M` | 25 | 25 | 25 |
| `max_k_observed` | 2 | 2 | (legacy `k` cap is 6, not hit) |
| `max_lex_observed` | 0 | 0 | (legacy `lex` cap is 40, not hit) |
| `state_table_sha256` | `c2835aaf8450ab938170ae3808b5852d53f2c7b1ae29b14ca77b7965bf37f1ad` | same | n/a (same `(w,M,lambda_min)` map) |
| `capped` | n/a | `hard_loop_caps = []` | `False` |

Cost mismatches between packet and `close_p`: none.  Symmetric
difference of `(w, M, lambda_min)` triples: empty.

P5 (`BOOK-OFFAXIS.md:639-643`) still says the `(3/2,2)` closure at
budget 5 "has 70 states up to `M=25`".  Current `close_p` returns 69
and `capped=False`.  The producer is right that 70 is stale relative to
its own current engine.

Is 69 a duplicate-collapsed 70, or is a legal state missing?

- Unique reduced `w` in the 69: 25 values, not 70 and not 69.
- `M=1` count: 25.  Cost histogram: 2 + 0 + 5 + 6 + 20 + 36 = 69.
- Independent enumerator using a different dirty-lex terminator and a
  brute `N`-window for pure-`(b)` still yields 69, same hash.  A shared
  off-by-one in both engines would have to sit in the P0 identities
  themselves, which were re-derived in §1.
- Legacy `chain_steps_p` (`book_offaxis.py:539-609`) assigns every
  divisor of `E` as a pure-`(b)` `M'`, ignoring the `kbar` congruence.
  At charged reachable parents this disagrees with the packet at 207
  `(w,l,eps)` triples (typically `M'=1` is forbidden by the congruence
  but `| E`).  Comparing one-step destinations at remaining
  `5 - lambda_min` finds extra *legacy edges* at 8 parents, e.g. from
  `(2/7, 7)` at spent 3, and **no packet-only destination**.  Every
  extra legacy target is already present in the 69 via another legal
  path (or would land on an already-reached `(w,M)`).  Over-approximating
  the packet the same way produced 69 states and 347 edges.  So the
  congruence is a quotient of edges, not a deletion of reduced states,
  at this instance.
- Legacy still has `k in range(0,7)` and `lex in range(0,41)`
  (`book_offaxis.py:572-576`) plus `PCAP_BUDGET=5`, `PCAP_STATES=4000`,
  `num(w) > 10**4`, `M > 200` (`:613-637`).  None of those caps fire
  here (`max_k=2`, `max_lex=0`, `max_M=25`, numerator 3).  They cannot
  explain a 70th *missing legal* state in current `close_p`.

Conclusion: 70 is stale prose.  It is not a second representation of
one of the 69, and it is not a legal reduced P0 state that the cap-free
engine dropped.  The honest charged object is 69 reduced pairs, maximum
`M=25`, maximum reduced numerator 3.

Start menu at remaining 5, independently: 2 clean-neutral, 1
pure-epsilon (`w → 3`, `M → 1`, `lambda = 3`), 3 dirty.  No clean
resonance (`Δ | 3` gives `Δ=3`, `dq=5` not divisible by `den(w)=2`),
matching P0's printed four-escape list up to M-drops.

---

## 4. Charge 4 — td-7 case-III special `nu`

### 4.1 The equation, from the actual handshake

Freeze chain 1 at `(μ,w)=(1,2)`.  Place chain 2 at the 0-direction with
`(μ0, w, nu_H)=(2, 3/2, h)`, `h` odd `>= 3` (neutral ray at `M=2`:
`nu ≡ -1 (mod 2)`).  R2.1 (`BOOK-OFFAXIS.md:321-327`; DEPTH §5c is the
`μ=1` shadow):

```text
X = μ1 (kbar - w1)     = kbar - 2          (case I/II)
X = μ0 (kbar - nu_H w2) = 2(kbar - 3h/2)   (case III)
```

Eliminating `X` yields `kbar = 3h-2`, `X = 3h-4`.  For `h >= 3`,
`X >= 5 > 0`.  Also `X < kbar`, so `dp/dq < 1`, hence `dq > dp`.
R2.2(S) then forces `k=0` (northeast p-orbits require `dq < dp`).

ZCH shape with a 0-chain (`ε = μ0 = 2` by R2.2), one non-0 arrival
`μ=1`, no NE extras: `dp = 2 + g = g+2`,
`dq = (1 + l_ex) g + 1`.  Writing `l` for `l_ex`, `dq > dp` forces
`l >= 1` (and MP7 independently kills `l=0` ZCH).  This is P3's printed
shape and BOOK-OFFAXIS §8 Step 3's shape.

Ratio `X/kbar = dp/dq`:

```text
(3h-4)/(3h-2) = (g+2)/((l+1)g+1)
```

clears to `g*((3h-4)l - 2) = 3h`.  The algebra is the same as Step 3's
`nu_G = (A+2)/(l(A-2)-2)` with `A = 3h-2`, rewritten without the
auxiliary `A`.

### 4.2 Domain and uniqueness

Declared domain: odd `h >= 3`, `l >= 1`, `g = nu_G >= 2`.

If `l >= 2`, then `D = (3h-4)l-2 >= 6h-10`.  For `h >= 3`,
`6h-10 > 3h/2`, while `g D = 3h` and `g >= 2` require `D <= 3h/2`.
Contradiction.  So `l=1` and `g(h-2)=h`, i.e. `(h-2) | 2`.  Positive
divisors of 2 are 1 and 2: `h=3, g=3` or `h=4, g=2`.  Oddness kills
`h=4`.  Negative divisors give `h <= 1`.  Unique odd solution
`(h,l,g)=(3,1,3)`, cell `(dp,dq,M_G)=(5,7,1)`, interior MP2-dead
(Step 3; MP2 trunk `M ≠ 1`).

Independent rectangular scan `2 <= h < 80`, `1 <= l < 40`, `g >= 2`
produces exactly three integer points: `(3,1,3)` odd, and even
`(2,2,3)`, `(4,1,2)`.  The packet's test scan `3 <= h <= 1001` odd,
`1 <= l <= 100` finds only `(3,1,3)`.  Every odd `h >= 5` is empty on
this shape, including this reviewer's earlier `S5` (`h=5`:
`g(11l-2)=15`, no `g >= 2`).

Step 3's older filter `A-4 | 6` is equivalent on integer `h`:
`A-4 = 3(h-2)`, and `3(h-2) | 6` iff `(h-2)|2`.  The packet's form is
cleaner and does not generate the non-integer-`h` ghosts `A-4 ∈ {1,2}`.

### 4.3 No silent generalization

`td7_caseiii_special_nu_r1.py` hard-codes the frozen partner, the odd
ray, and the ZCH shape.  `scope_firewall` sets
`other_partner_states`, `other_case_III_shapes`, `full_td7_book`,
`landing`, and `jc2` all to `False`.  The producer text treats this as
the first consumer and names the rest as future work.  The equation is
not applied to other charged skeleton states or to IIa/I merges.
Cap-token scan of that source is clean (`NCAP`, `range(3,`, `nu_cap`,
`max_nu` absent); the rectangle lives in the test, as a negative
control of the *equation*, not as a substitute for the handshake
derivation.

---

## 5. Charge 5 — relation to the earlier general falsifier

The earlier report
`xmodel/m2-budget-quotient-falsifier-grok46-20260829.md` (verdict
`REPAIRABLE`) attacked a different object: a finite exact quotient of
the whole priced grammar by `(w,M)` plus a partner-independent handful
of residue flags, sufficient for every later merge legality.  That
object remains false.  The present theorem is the L1 fragment of the
repair named there, not the repaired quotient.

| Earlier objection | Status at reduced-chain scope | Status at merges |
|---|---|---|
| Attack A / S3 vs S5: same `(w,M, nu odd)`, different case-III well-formedness | Not a chain-layer objection: `nu` is quotiented | **Survives in general.**  Repaired for *this* frozen partner and *this* ZCH shape: `N_special = {3}`, generic odd ray empty.  Other partners, other shapes, and case I/II still need their own special tables |
| Attack B §2.1: reduced `num(w)` and `M` are finite at fixed `B`; P5's "unbounded numerator and `M`" is false for reduced states | **Repaired, and now cap-free constructive.**  This is the theorem | Unchanged: last-vertex `nu`, `kbar`, pattern degree remain unbounded |
| Attack B §2.2: what is actually unbounded | Confirmed, and correctly excluded from the reduced record | Still the obstruction to a coarse quotient |
| Attack C: product of two free integers | Out of chain-layer scope | Not re-opened here |
| Attack D: two states, one record, different verdicts | Same as A | Survives except for the one discriminator of Charge 4 |
| L3 generic-AP uniformity for every consumer | Not claimed | **Open.**  Producer says so |
| Avenue-1 colon / Card 2 | Not used | Irrelevant to this packet |

Safe replacement, and no further: P5's sentence that the reduced P0
chain closure at a fixed entry and budget has unbounded numerator and
`M`, together with the stale "70 states" example.  Not safe as a
replacement for: a finite full transition/book quotient; merge
q-extra families; partner-dependent merge legality; last-vertex `nu`
uniformity; landing; `G2-BD`; `RPMC(C)`; a cofinal degree bound; JC2.

The earlier L1 sketch already believed reduced finiteness.  This review
does not inherit that belief.  The lex bounds, the `eps=0` versus
`eps>0` split, the `E | l a T` identity, the exhaustive `C=0` / `C>=1`
partition, and the charged 69-state census were re-derived and
re-run here.

---

## 6. Findings, severity order

### F1 — no counterchain at stated chain scope (informational)

No infinite reduced `(w,M)` family exists at fixed `B` under the
imported P0 laws.  Zero-cost edges are well-founded; non-clean depth
is at most `B`; unpriced `lex` and free `nu` do not accumulate in the
reduced record.  Locations: P0 at `BOOK-OFFAXIS.md:480-509`; packet
loops at `finite_chain_skeleton_r1.py:178-287` and `:165-176`.

### F2 — witness field is not a shortest-path tree (low, implementation)

`first_predecessor` records the first Dijkstra *push*, which need not
be a min-cost path.  Charged reproducers: `(2/9,9)` and `(1/2,1)` as
in §2.  `lambda_min` in the state table is nevertheless exact.
Location: `finite_chain_skeleton_r1.py:319-325`.  Does not touch the
theorem.  Repair would be to set the predecessor on a strictly cheaper
push, or on pop.

### F3 — packet tests do not lock the claims they sit next to (low, tests)

`test_finite_chain_skeleton_r1.py:87-111` hard-codes the charged 69
and the hash; it never imports `close_p`.  Equality with the legacy
map is a producer-report claim, verified here, not a packet check.
Charged `max_lex_observed = 0`, so the golden lock is silent on
`lex > 0` dirty completeness.  The syntactic cap-token list would miss
a renamed cap.  None of these is a mathematical omission: the
independent enumerator and the copy-mutations close the gaps.

### F4 — P5's 70 is stale; 69 is not a collapsed 70 (informational)

Location of the stale claim: `BOOK-OFFAXIS.md:641-643`.  Current
`close_p` and the cap-free packet agree on 69.  Distinction: extra
legacy pure-`(b)` `M'` values are extra *edges*, not an extra legal
reduced state, at this instance (`book_offaxis.py:567-570` versus
`finite_chain_skeleton_r1.py:139-162,226-228`).

### F5 — even solutions of the ratio equation exist off-domain (informational)

`(h,l,g) = (4,1,2)` and `(2,2,3)` solve `g*((3h-4)l-2)=3h` with
`g >= 2`.  They are excluded by odd `h >= 3`.  The uniqueness claim is
domain-correct and is not stated as uniqueness in `Z`.  Location:
`td7_caseiii_special_nu_r1.py:30-35` and the producer proof list.

No `REPAIR_REQUIRED` item at stated chain scope.  No `REJECT` item.

---

## 7. Scope firewall

Conditional on the imported P0 sheet laws (R1.0–R1.2, R2.1–R2.2, AF2
pricing, St 8.4, St 9.4 as used by P0).  This review does not certify
those sheet theorems.

This PASS does not assert: landing completeness; merge finiteness or
a complete partner-dependent special-`nu` table; generic-AP uniformity
for every later consumer; a full configuration ledger; `G2-BD`;
`RPMC(C)`; a cofinal topological-degree bound; realizability; a Keller
counterexample; or JC2.

---

## Verdict (repeated)

**`PASS_AT_STATED_CHAIN_SCOPE`**

---

Report-body SHA-256 (UTF-8 bytes preceding the separator line above,
including the blank line after the repeated verdict):
`c95fbe402dd4d9791290e914f7fbb9d12632400ae898ec2d9cc873db990f86a1`

Full-report SHA-256 is the digest of the entire on-disk file after this
write, including this footer and its trailing newline.  Recompute both
by

```python
from hashlib import sha256
from pathlib import Path
p = Path("xmodel/m2-finite-reduced-chain-skeleton-r1-hostile-review-grok46-20260829.md")
b = p.read_bytes()
i = b.rfind(b"\n---\n")
print(sha256(b[:i+1]).hexdigest(), "body")
print(sha256(b).hexdigest(), "full")
```

The body digest is stable under this footer.  The full-file digest is
not inlined, because inlining it would change it; run the snippet on
the on-disk file.

