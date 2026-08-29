# Fable 5 hostile review — U2 first-P2-boundary finiteness R1 (Sol 5.6)

Date: 2026-08-29 UTC. Reviewer: Fable 5, independent adversarial lane.
Target: `xmodel/m2-u2-first-p2-boundary-finiteness-r1-sol56-20260829.md`,
lifecycle `PRODUCER_CHECKED`; this report is the required different-model
review.

## 0. Verdict

**`PASS`**

The conditional theorem `U2-FIRST-P2-BOUNDARY-FINITE` is correct as stated,
at exactly its stated scope. I re-derived by hand every load-bearing step:
the `s`-free boundary identity `kbar = l*W/(l-m)`, the finite boundary-weight
set `T_EQ` with its `L`- and string-length uniformity, the sharp prefix bound
`Mhat = M0*2^B` on the whole P0 prefix, the finite-target generalization of
the reviewed opposite-side product argument (including the genuinely
reachable empty-set branch), and the parent-side typing of `(W,M)`. A
directed hostile search for an infinite `L` family satisfying the hypotheses
produced nothing: every construction dies on the opposite-side sign structure
of the reviewed Lemma 3.1 or on strict monotonicity of `W_L` in `L`. The
no-overclaim perimeter is complete and honest. Five non-blocking nits are
recorded in §4; none affects the statement, the proof, or the scope.

The theorem is conditional and says so: (EQ) is a literal hypothesis, and
the coverage question — whether every relevant `nu>=2` first P2 transition
supplies (EQ) — is explicitly left open and charged onward, not claimed.

## 1. Custody and provenance

Body-hash convention (target and this report): all bytes strictly before the
final blank-line-plus-separator, i.e. `b[:b.rfind(b"\n" + b"-"*3 + b"\n")]`,
which keeps the newline terminating the last body line. The target's match
point is byte 7829 of 7968.

| item | expected | recomputed | match |
|---|---|---|---|
| target, full | `8c46e6bf...` | `8c46e6bf6e31faa191c67ba1bac6d489e0fe27741b35223ff30992f7d27a4db8` | YES |
| target, body | `220aa975...` | `220aa9752200fa3d4188290200e6ad0d15965670de972d35fb5f42e5e5d08951` | YES |
| Fable5 review of Grok U2 primary, full | `e156f94c...` (target §1.1) | `e156f94ca83026fe04b287100ca79f72325c80a82f8ed3f3f8a94044db440740` | YES |
| Sol P0-to-P1 repair, full | `3989703a...` (target §1.2) | `3989703ae243705166843dfe5183bbc83cba44d9284071e49deca19cd935933e` | YES |
| Opus5 review of that repair, full | `9a1775f6...` (target §1.3) | `9a1775f6c9de92e8204098be3a422222f159d0a4f74baf13a75b1d43598c4a58` | YES |
| `ladder/BOOK-OFFAXIS.md`, full | `7679db8a...` (pins inside both prior reviews) | `7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77` | YES |

The source grammar on disk is byte-identical to what both prior reviews in
the chain consumed, so the P0/P1/P2 text I read (§10 of the book: strict NE
laws with "equality is the root-mult law", the transport line
`kbar_F = l*w_G*dq/E in Z (nu>=2)`, `M_F = gcd(dp,dq)`, St 8.4 `l | M`, the
P2 merge pricing and arrival law) is the same grammar the target's inputs
were certified against. Dependencies read: the three xmodel files above in
full; the book's §10 P0/P1/P2/P5 as the literal source.

Execution note: this session had a shell; it was used only for SHA-256
recomputation, a byte-offset scan to confirm the body-hash convention, and
one short exact-rational desk script (fractions arithmetic, output recorded
in §5). All mathematical verification is hand desk work. No web, AWS,
`jc2-lean` access, canonical edit, source-packet edit, commit, or push. The
only repository file written is this report.

## 2. Clause-level findings

### Charge 1 — finite boundary-weight set: CONFIRMED

The identity: with at least one root-multiplicity equality orbit, `m*dq = dp`
exactly, so `E = l*dq - dp = (l-m)*dq` and the printed transport
`kbar = l*W*dq/E` collapses to `kbar = l*W/(l-m)`, independent of `s`, of the
boundary vertex's `nu` and `dq`, and of any other (strict-NE, hence smaller)
orbits present. Rechecked exactly at `(l,m,nu) = (4,1,2)`, `W = 3/2`:
`kbar = 2` for all `s`, matching the Opus §8 fixture, whose backward-factor
sequence `9/4, 15/8, 7/4, 27/16, 33/20, 13/8, 45/28, 51/32 -> 3/2` I also
reproduced.

Given `kbar in N*` (hypothesis), `1 <= m < l` (hypothesis), `l | M`
(hypothesis, St 8.4-shaped) and the prefix bounds of Charge 2:
`l <= M <= Mhat`, `W <= What`, so `kbar = W*l/(l-m) <= What*l <= Mhat*What`
(using `l/(l-m) <= l` from `l-m >= 1`), and
`W = kbar*(l-m)/l >= 1/l >= 1/Mhat`. Hence `W` lies in the target's explicit
set `T_EQ`, every element of which is `>= 1/Mhat > 0`. `T_EQ` is determined
by `(r,mu,w,B)` alone: `Mhat = r*mu*2^B` and `What = r*w*Mhat^B` contain no
`L`, no `s`, no boundary `nu`, no later merge data. The uniformity claims
are exactly right. The target correctly does not bound `s` or the child
`M' = nu*s+1` (I rechecked: `M' = dq = 2s+1` with `W' = 2s/(2s+1)`, `j = 1`,
all P1-legal — one parent, infinitely many legal children, as Opus proved).

### Charge 2 — `Mhat = M0*2^B` on the whole prefix, `L`-freeness: CONFIRMED

Opus F4's argument is terminal-free and applies verbatim to any P0 path of
modeled cost `<= B`, which is exactly what the target's prefix is: `M` grows
only at a dirty step with `k >= 1` NE orbits, by a factor `<= 1+k`
(`M' <= T <= l + Sm <= l + k(l-1) < l(k+1) <= M_parent*(k+1)`); each NE
orbit prices `>= 1`, so `sum k_i <= B`; and `prod(1+k_i) <= 2^(sum k_i)`
since `1+k <= 2^k` for `k >= 1`. I verified the maximum of `prod(1+k_i)`
under `sum k_i <= B` equals `2^B` for `B <= 5`. Nothing in this uses P1 or
anything after the boundary.

`L`-independence of both bounds: `M_L = gcd(r*mu, r+L) | r*mu = M0` and
`W_L = w(L+r-1)/L <= r*w` for every `L >= 1`. The upper weight bound (U)
with the *sharp* `Mhat` substituted is immediate though not literally
printed in Opus: every positive-cost forward multiplier is
`<= l <= M_parent <= Mhat_sharp` (by F4 itself plus `l | M_parent`), at most
`B` such steps, so `W <= r*w*Mhat_sharp^B`. Recorded as nit N2; true in one
line.

### Charge 3 — finite-target extension of the product argument: CONFIRMED

I traced every place P1 enters the reviewed Sol proof. It enters exactly
twice: as the source of a finite target set, and as the source of the
uniform lower bound `tau_min = 1/Mhat`. Both are replaced by the lemma's
hypothesis (`T` finite, `tau_min = min(T) > 0`). Everything else is
target-agnostic, and I re-derived each bound group for arbitrary finite
`T subset Q_{>0}`:

- `M <= Mhat`: forward from the entry, no terminal used (Charge 2).
- Upper weights: (U) forward, no terminal used.
- Lower weights: forward from any intermediate vertex to the target,
  multipliers `<= Mhat` (positive-cost, at most `B`) and `<= 1`
  (neutral/resonant), so `W_i >= tau/Mhat^B >= tau_min/Mhat^B`.
- Charged depth `<= B` (every non-clean step prices `>= 1`); resonant depth
  from `tau_min <= r*w*Mhat^B*(2/3)^R`; weight-changing
  `nu <= 2*Mhat*What/Wmin`; neutral runs collapse to finitely many
  divisor/residue records since `M <= Mhat`.
- Backward composition per fixed target and type has exactly the reviewed
  Lemma 3.1 shape: `u = w`, `c = r-1 >= 1` (this is where `r >= 2` is
  load-bearing), `q = tau *` (positive constants) `> 0`, `v_i = nu_i`,
  `a_i in {nu_i - 1, K_i/l_i}` both `> 0` at `nu >= 2`, unbounded `x_i in
  {n_i, s_i}` each in a factor approaching `v_i` strictly from below. The
  crucial point for this target: the reversed-approach factor
  `((l-m)/l)(nu + 1/s)` belongs to the boundary step itself, which is *not*
  composed — the cut is strictly before it. The prefix product contains
  only from-below factors, so Lemma 3.1 (independently proved by Opus §6,
  with knife-edge and sign-flip controls) applies.

Empty-set branch: genuinely reachable, not decorative. At
`(r,mu,B,w) = (2,1,0,1/5)`: `Mhat = 2`, `What = 2/5`,
`floor(Mhat*What) = 0`, so `T_EQ` is empty — and correctly so, since any
(EQ) boundary would need `1 <= kbar <= Mhat*What = 4/5`, impossible. The
lemma's trivial branch returns zero qualifying `L`, which is the right
answer. Neutral/residue parameters: free neutral and pure-eps `nu` move only
the finite `M` record; the union over all divisor records is finite and
superset-safe.

One direction had to be checked against the Opus §9 quotient warning
(consumers of the reduced `(w,M)` record must not consume last-vertex `nu`,
`kbar`, or merge legality). The target does not cross it: it uses the full
boundary data only in the *forward* direction (legal (EQ) boundary implies
`W in T_EQ`), then deliberately discards all boundary legality and bounds
the strictly larger set `{L : some cost-<=B reduced P0 path reaches a weight
in T_EQ}`. Dropping constraints enlarges the `L`-set, so finiteness of the
superset is exactly what is needed. The reduced shadow of any full legal
prefix is a legal reduced P0 path of no greater modeled cost, so no family
escapes the superset.

### Charge 4 — typing of `(W,M)` and source licensing of (EQ): CONFIRMED

`(W,M)` is the incoming parent — the last P0 state, feeding the boundary
step — throughout: in the theorem statement ("the incoming parent
immediately before a first P2 transition"), in the identity
(`kbar = l*W/(l-m)` uses the parent weight, matching Opus §8's
"pins the parent weight"), and in §2's explicit disclaimer that the child
values `s` and `M' = nu*s+1` are not bounded. The `l` of (EQ) is the mult of
the parent's own arriving edge with `l | M` read against the parent's
reduced record. No parent/child conflation anywhere.

Source licensing: the book's P0 states the NE laws as strict with "equality
is the root-mult law (R)", i.e. an orbit at `m*dq = dp` is exactly the
arriving-branch regime of a P2 merge — outside P0, which is why this is the
*first* non-P0 transition. The transport proportion and
`kbar = l*w*dq/E in Z (nu >= 2)` are the printed P0/R1.2/R1.4 lines; Opus §8
derived (EQ) from precisely these and machine-checked `kbar`-rigidity with
zero deviations. The target's conditional scope matches the license exactly:
integrality is *hypothesized* (`kbar in N*`), which covers all
source-legal `nu >= 2` boundaries (where the printed line forces
`kbar in Z`) and harmlessly includes any accidental-integral `nu = 1` case,
while §5 excludes the rational-`kbar` `nu = 1` regime by name. One subtlety
done right: the target uses the coarse pin `kbar <= Mhat*What` rather than
Opus §8's sharper `kbar <= nu`, because the sharper pin consumes the child's
P1 `j`-law — a downstream legality assumption that would contradict the
theorem's "uniform in everything after the boundary" claim. The coarse
choice is the correct one for the stated uniformity.

### Charge 5 — hostile search for an infinite `L` family: NONE FOUND

Constructions attempted, and how each dies:

1. **Zero-step prefix** (boundary at the entry): needs
   `W_L = kbar*(l-m)/l in T_EQ`; `W_L = w(1 + (r-1)/L)` is strictly
   decreasing in `L` (verified on the `r=2, w=3/2` sequence), so at most one
   `L` per element of the finite `T_EQ`. Dead.
2. **Neutral-only prefix**: weight unchanged; same as 1 with an extra finite
   record union. Dead.
3. **Single resonance / single dirty step** (`h = 1`): backward equation
   `w(1+(r-1)/L) = tau*(nu - a/x)` is opposite-sided; Lemma 3.1 plus Opus's
   focusing fixtures (at most 42 resp. 34 distinct `L` per instance, `L`
   monotone to `w(r-1)/(tau*nu - w)` and stopping) kill it. The knife edge
   `tau*nu = w` has zero solutions (left side `> w`, right side `< w`).
   Dead.
4. **Deep interleavings**: charged depth `<= B`, resonant depth `<= R_max`,
   weight-changing `nu` bounded, neutral runs collapsed — finitely many
   types, each a Lemma 3.1 instance. Dead.
5. **Unbounded equality-string `s` or unbounded child `M'`**: varies only
   data after the cut; produces infinitely many *children* at one `L`
   (explicitly allowed) but revives no excluded `L`. Dead as an `L` family.
6. **Growing budget with `L`**: excluded — `B` is fixed by hypothesis, and
   in the source the shared St 9.4 budget is `td`-coupled, not `L`-coupled.
7. **Nested two-parameter `(L_inner, L_outer)` family**: the inner parameter
   rides inside `(r,mu,w)`; this genuinely escapes the theorem — and is
   excluded by name in §5. It is a coverage gap, not a defect: no
   construction satisfies the theorem's stated hypotheses.

Separation, as charged: I find **no defect in the conditional theorem** —
under its hypotheses the finiteness proof is sound. The **coverage claim**
(every relevant first boundary is P1, integral-(EQ), or excluded-by-name) is
open, is not asserted by the target, and is flagged twice in the target's
own text (§1 last paragraph, §5). The verdict applies to the conditional
statement only.

### Charge 6 — no-overclaim perimeter: CONFIRMED

The target claims no exhaustive downstream merge grammar (§0), no nested-U2
statement, no landing, no Statement 3.9 / gluing, no realization, no
full-cell finiteness, no neutral-index or arrival-vertex data, no exact
lambda, no panel, no degree ceiling, no `G2-PSC`/`G2-BD`, no JC2 conclusion
(§5). The two-case consequence in §0 (P0-to-P1, or first exit through
integral-(EQ)) is a finite union of the reviewed theorem and the new one,
properly conditional ("whenever"). §4's closing claim — that later merges
and unbounded post-merge data cannot restore an excluded outer `L` — is
correct because the excluded `L` already fails to reach the cut. §4 and §5
are consistent: §4's coverage sentence is conditional on the first
transition supplying (EQ); §5 lists precisely the boundaries where it does
not. The citation of Opus §8 ("derives (EQ) ... and explicitly notes that
its old P1-target proof does not itself cover that family") is accurate
against the Opus text.

## 3. Findings summary

| # | clause | verdict |
|---|---|---|
| 1 | boundary weight in explicit finite `T_EQ`, uniform in `L`, `s`, boundary `nu`/`dq` | CONFIRMED |
| 2 | `Mhat = M0*2^B` valid on entire prefix; bounds `L`-free | CONFIRMED (N2: one-line sharp-(U) justification supplied) |
| 3 | product argument extends to any finite positive target set, empty branch included | CONFIRMED (empty branch genuinely reachable and correct) |
| 4 | `(W,M)` typed as pre-merge parent; (EQ) licensed at exactly the stated scope | CONFIRMED |
| 5 | infinite-`L` family under the hypotheses | NOT CONSTRUCTIBLE; leak is coverage, not the theorem |
| 6 | no-overclaim perimeter | CONFIRMED |

## 4. Non-blocking nits

- **N1.** "carries one root-multiplicity equality orbit" should read "at
  least one": the identity needs only `>= 1` such orbit, and all equality
  orbits share the same multiplicity `m = dp/dq`, so nothing else changes.
- **N2.** §2's display (1) attributes both bounds to Opus; Opus proved (U)
  with the loose `Mhat`. The sharp-substituted (U) is true by the one-liner
  in Charge 2 above and should be stated.
- **N3.** "The finite set is effective" is true but tower-effective through
  the Lemma 3.1 induction; a successor enumerator should adopt Opus F3's
  corner bound (`L <= u*c/(P0 - u)` at the least qualifying corner) for a
  usable cap.
- **N4.** `B` is abstract here. Under the shared St 9.4 budget the safe
  uniform consumer instantiation remains `B = td - 2` (Opus F6), counting
  *prefix* cost only; the boundary step's own merge pricing (arriving edges
  and equality orbits price 0 per MP8) is not part of `B`. One sentence for
  the successor.
- **N5.** `T_EQ` can be empty (`floor(Mhat*What) = 0` for small `w`), in
  which case the theorem is vacuous and correctly so (no (EQ) boundary is
  even arithmetically possible). Worth one sentence so a consumer does not
  misread vacuity as a kill of the merge itself.

## 5. Desk-check ledger

Hand or exact-rational checks performed this session (short, no heavy
computation): the equality-orbit factor sequence at `(l,m,nu) = (4,1,2)`
(eight values, matching Opus §8 digit-for-digit, decreasing to `3/2`);
`kbar` `s`-freeness at four `s` values; the child ledger `M' = 2s+1`,
`W' = 2s/(2s+1)`, `j = 1`; `max prod(1+k_i) = 2^B` for `B <= 5`; the
`(2,1,0,1/5)` empty-`T_EQ` instance; strict monotonicity of `W_L` in `L`;
the inequality chain `kbar = W*l/(l-m) <= Mhat*What` and
`W >= 1/Mhat`; and the algebra `E = (l-m)*dq` under `m*dq = dp` from the
printed `E = l*dq - dp`. All agreed with the target.

## 6. Maximum safe theorem

> Under the reviewed absorbed-U2 input (fixed rational `w > 0`, integers
> `r >= 2`, `mu >= 1`; `W_L = w(L+r-1)/L`, `M_L = gcd(r*mu, r+L)`), the
> reviewed P0 grammar with standing `nu >= 2` and a fixed prefix budget `B`,
> and the literal boundary hypothesis (EQ) — at least one root-multiplicity
> equality orbit at the boundary vertex with `l | M`, `1 <= m < l`, and
> `kbar = l*W/(l-m) in N*` — only finitely many integers `L >= 1` admit a
> P0 continuation of modeled cost `<= B` whose last P0 state `(W,M)`
> immediately precedes such a first P2 transition. The bound is effective
> from `(r,mu,w,B)` and is uniform in the equality-orbit count and string
> length, the boundary vertex's `nu` and `dq`, the later merge data, and
> everything after the cut. Combined with the reviewed P0-to-P1 theorem,
> finitely many `L` support any continuation that either terminates at P1
> inside P0 or first leaves P0 through an integral-`kbar` (EQ) boundary.

Nothing more: no statement about first boundaries without integral (EQ), no
nested U2, no full-cell or downstream conclusion of any kind.

## 7. Smallest remaining U2 leak

A continuation whose first non-P0 transition is a `nu = 1` merge (case I),
where `kbar = l*W/(l-m)` is licensed only as a rational and (EQ)'s
integrality anchor is absent — concretely the nested U2 boundary with two
parameters `(L_inner, L_outer)`, where even the fixed-`(r,mu,w)` hypothesis
fails because the inner parameter rides inside the absorbed data. One level
above it sits the open coverage question, asserted by nobody: that every
relevant first departure from P0 is a P1 terminal, an integral-(EQ)
boundary, or one of the excluded-by-name types. The target's §6
two-parameter discriminator (exact equal-weight and integrality equations
for the nested `nu = 1` boundary, no caps) is the right next instrument;
a finite-denominator analogue of (EQ) would close U2 recursively, and an
explicit surviving `(L_inner, L_outer)` family is the honest counterfamily
target.

---

Report-body SHA-256 (all bytes before the separator line above):
`f254339913a87162dc80ab0cc155f75fe09ca1c4875c106273a0a5344eadfe0e`.
