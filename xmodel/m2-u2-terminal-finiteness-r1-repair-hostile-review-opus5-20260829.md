# Opus 5 hostile review — Sol 5.6 U2 fixed-terminal finiteness repair (R1)

Date: 2026-08-29 UTC. Reviewer: Opus 5, independent lane, clean room.
Target: `xmodel/m2-u2-terminal-finiteness-r1-repair-sol56-20260829.md`.

## Verdict

**`PASS_AT_CONDITIONAL_P0P1_SCOPE`**

The theorem is correct as stated, and its two conditional inputs are the two
it names. I re-derived (R), (E) and (D) from the printed P0 transport, closed
the four-family partition, re-proved Lemma 2.1, Lemma 2.2, Lemma 2.3 and
Lemma 3.1 independently, and failed to produce any infinite Diophantine
family contradicting Lemma 3.1 after a directed hostile search. Every
inequality the note asserts held on all 3098 legal P0 steps in an exhaustive
clean-room box, with zero violations.

Nine findings follow. **None is `REPAIR_REQUIRED`.** Two are presentational
(Lemma 3.1's endgame branch and an `h=0` degeneracy), three are strengthenings
I proved and machine-checked (an effective corner bound on `L`, a sharper
`Mhat`, a smaller free-variable inventory), one is hypothesis hygiene (`nu>=2`),
one is a usage note (`B` must be instantiated at `td-2`), one is custody
(body-hash convention divergence in this lane), and one is the sharp scope
boundary described next.

**The sharp boundary.** The note's four-family partition is complete for P0
*as printed*, because P0's NE laws `eps*dq < dp` and `m_j*dq < dp` are strict.
The one family it therefore omits is the root-mult **equality** orbit
`m*dq = dp` — an arriving edge, i.e. the P2 merge regime. That family reverses
*both* load-bearing structures at once: its backward factor
`((l-m)/l)*(nu + 1/s)` tends to its limit **from above**, not from below, and
`M' = gcd(dp,dq) = dq` is **unbounded in `s`**, so Lemma 2.1 fails there. So
the theorem's restriction to P0 paths is not cosmetic; it is exactly where the
proof lives. I show separately (§8) that `kbar in Z` pins the parent weight of
that family to the `s`-free value `kbar*(l-m)/l`, so a one-step widening still
gives finitely many `L` — but by an argument the note does not contain and
must not be assumed to contain.

---

## 1. Custody

Convention used by the target and by this report: **all bytes strictly before
the final `\n---\n` separator, excluding the newline that terminates the last
body line** (`b[:i]` where `i = b.rfind(b"\n---\n")`).

| item | claimed | recomputed | match |
|---|---|---|---|
| target, full | `3989703a…` | `3989703ae243705166843dfe5183bbc83cba44d9284071e49deca19cd935933e` | YES |
| target, body | `aa6f8685…` | `aa6f8685d56c8c7582082717bf802649fa5966282ae76c4666c2c0b6fc9f1bf0` | YES |
| Grok U2 primary, full | — | `9c20947be6d2ac6aad19176fae66f0b4acfb6ec6bce257a2169d8d266c667613` | recorded |
| Fable5 finite-chain review, full | `3dab7f08…` (BOOK §10 P5) | `3dab7f080ebc9ae5568d76cb4a60085646f2365ee7a277c6a0dd8028d4135b1f` | YES |
| Grok46 finite-chain review, full | `bf4c56ae…` (BOOK §10 P5) | `bf4c56ae3afdd34197ff4296c8f90112c6661ca09477bf498e7d9d2b038a0912` | YES |
| `ladder/BOOK-OFFAXIS.md`, full | — | `7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77` | recorded |
| this review's prompt, full | — | `415c7f8a5c3c160ead629d64865627bfad9be4f292156fa9dbfa1ec752c37114` | recorded |

**F7 (custody, low).** The two finite-chain reviews publish their body hashes
under the *other* convention — bytes before the separator **including** the
last body line's newline (`28fc400c…`, `c95fbe40…` reproduce only that way;
their excl-newline hashes are `539357cc…`, `b6d8e689…`). The target uses the
excl-newline convention and its own line says so explicitly, so nothing is
wrong; but the two conventions now coexist across sibling lanes and any
automated cross-lane comparator will mis-report. Recommend the successor state
the convention verbatim, as this report does.

Not read, per prompt: Fable's active review of Grok U2, and every other
post-target result. I read Grok's U2 primary only for the entry display
(§2 lines 160–192, §4), both finite-chain hostile reviews, and BOOK-OFFAXIS
§10 P0/P1/P2/P5.

---

## 2. Clause-level scorecard

| clause | claim | verdict |
|---|---|---|
| §0 input 1 | Grok's absorbed shape `W_L = w(L+r-1)/L`, `M_L = gcd(r mu, r+L)`, `r>=2`, `mu>=1`, `w` fixed | **CONFIRMED as the claimed input** (Grok §2 `w_tr = w(r+L-1)/L`, `M=gcd(r mu,r+L)`; `r>=2` at Grok line 8) |
| §0 input 2 | P0/P1 grammar, `l\|M_parent`, zero-cost = neutral or clean resonant, P1 = `0<W_t<1`, `M_t>=2`, `j=M_t(1-W_t) in N*` | **CONFIRMED** against BOOK §10 P0/P1 and both finite-chain reviews |
| §1.1 (R) | `Delta=(n-1)nu+1`, `W'=Wn/Delta`, `W = W'(nu-(nu-1)/n)`, factor `<nu`, forward `<=2/3` | **PROVED**; `n=lex+1`, `E=l*Delta`; 40/40 resonant steps in the box satisfy all four |
| §1.1 neutral | fixes `W`, sends `M` to a divisor, contractible to a finite record | **PROVED**; 440/440 in the box |
| §1.2 (E) | `W'=lW/(l-eps)`, `W=W'(l-eps)/l`, free `nu` only moves a finite `M` record | **PROVED**; `M'=gcd(l-eps,nu+1)`; 1020/1020 |
| §1.2 (D) | `E=(l-eps)+nu*C`, `W'=lWs/E`, `W=W'(nu-K/(ls))`, `K=nu(l+Sm)-l+eps>0` | **PROVED**; identity exact on 1598/1598 dirty steps |
| §1 partition | four families, no omitted zero-cost weight-changing family | **PROVED for P0 as printed** (`C=0 <=> k=lex=Sm=0`, 0 counterexamples in a 12×6×8 combinatorial box); see F1 for the equality-orbit boundary |
| §2 L2.1 `M'\|T` | `M'\|T`, `gcd(M',nu)=1`, `T>=1` | **PROVED**; 0 violations / 3098 |
| §2 L2.1 `Mhat` | `M <= M0(B+1)^B` | **CORRECT but loose**; sharp value is `M0*2^B` (F4) |
| §2 L2.2 `2C>=s` | `C>=k+l*lex`, `2C>=s`, `E>=2C>=s` | **PROVED**; 0 violations |
| §2 L2.2 (U) | `W <= What = r w Mhat^B` | **PROVED** (per-step multiplier `ls/E <= l <= Mhat`) |
| §2 L2.2 P1 set | `W_t in {1-j/M}`, finite, `>= tau_min = 1/Mhat` | **PROVED** |
| §2 L2.2 (L) | `W >= Wmin = tau_min/Mhat^B` | **PROVED** |
| §2 L2.3 depth | `tau_min <= r w Mhat^B (2/3)^R`, `R` bounded | **PROVED** |
| §2 L2.3 `nu` | every weight-changing `nu <= 2 Mhat What/Wmin` | **PROVED** for (R) and (D) |
| §3 L3.1 | statement | **PROVED** (independent proof, §6) |
| §3 L3.1 | proof as written | **CORRECT but terse**; two presentational gaps (F2) |
| §4 assembly | fixed path multiplies into `q*prod(v_i - a_i/x_i)`, finitely many types | **PROVED**; free variables are exactly `{n_i} u {s_i}` and the inventory is even smaller than claimed (F8) |
| §5 scope | no ODE, gluing, landing, realization, ceiling, JC2 | **CORRECT and honestly stated** |
| §5 constructivity | "cap-free enumerator" in principle | **TRUE but tower-sized**; effective corner bound supplied (F3) |

---

## 3. Audit 1 — the backward laws and the four-family partition

I rebuilt the P0 step from BOOK §10 P0 without reading any packet code:

```text
dp = eps + nu*(l+Sm),   dq = nu*s + 1,   s = 1+k+lex,   Sm = sum m_j
E  = l*dq - dp = (l-eps) + nu*C,        C = l*(k+lex) - Sm
T  = l + Sm - eps*s,    dp - eps*dq = nu*T
kbar = l*w*dq/E,  w' = l*w*(dq-1)/(nu*E) = l*w*s/E,  M' = gcd(dp,dq)
```

`w' = l w s/E` reproduces the book's `w_F = l w_G(dq-1)/(nu E)` because
`dq-1 = nu*s`. Cross-validation against the reviewed grammar: Fable5's
resolvent identity `E*(l*a*s - kbar*d*C) = l*a*T` (`w = a/d` lowest terms)
held **exactly on all 3098 legal steps**, 0 failures. That is my evidence that
my clean-room model is the same object the two finite-chain reviews certified.

**Partition.** With `m_j <= l-1` one gets `C >= k + l*lex >= 0`, and `C = 0`
iff `k = lex = Sm = 0`; checked over `l<=12, k<=5, lex<=7`, 0 counterexamples.
So every P0 step is exactly one of
neutral (`C=0, eps=0`), pure-eps (`C=0, eps>=1`),
clean resonant (`C>=1, eps=k=0`, q-extras only),
dirty (`C>=1`, and `k>=1` or `eps>=1`). Disjoint and exhaustive.

**No omitted zero-cost weight-changing family.** Modeled
`lambda_F >= sum_j max(1, ...) + [eps>=1]*max(1, ...)` is `>= k + [eps>=1]`,
so modeled `lambda = 0` forces `k = eps = 0`, i.e. neutral or clean resonant.
Enumerated directly: over 2985 legal steps the set of families with
`lambda = 0` is exactly `{neutral, resonant}`. Because modeled `lambda` is a
*lower* bound of true `lambda`, any truly free step also has modeled `lambda`
0, so the modeled menu is a superset — finiteness of the superset transfers.

**The derived inequalities the note asserts.** `m_j < l` and `eps < l` are used
without proof in §2. Both are derivable, and I re-derived them rather than
importing them: for the maximal `m_j`, `m_j*s >= m_j + Sm`, so strict NE
`m_j*dq < dp` gives `nu(m_j - l) <= nu(m_j s - Sm - l) < eps - m_j`, and
`m_j >= l` would force `eps > m_j >= l`, contradicting `eps < l`; and `eps < l`
itself follows from `T>=1` and `C>=1` via `eps <= (l+Sm-1)/s <= (ls-2)/s < l`.
No circularity. Severity: citation hygiene only.

**Free local parameters.** Per family, after fixing the discrete type:
neutral — `nu` free, moves only `M' = gcd(l,nu+1)` and the residue `d | nu+1`;
pure-eps — `nu` free, moves only `M' = gcd(l-eps,nu+1)` and a residue class;
resonant — `n = lex+1` unbounded, `nu` weight-changing hence bounded;
dirty — `s = 1+k+lex` unbounded, `nu` weight-changing hence bounded.
So the note's "either `n`, `s`, or a finite reduced residue record" is exact.

---

## 4. Audit 2 — attack on `Mhat`

`M' | T` is right: `M' | dp` and `M' | dq`, so `M' | dp - eps*dq = nu*T`, and
`gcd(M',nu) | gcd(nu*s+1,nu) = 1`, hence `M' | T`. `T >= 1` is the strict
`eps`-NE law. Checked on all 3098 steps: 0 failures of `M'|T`, 0 failures of
`gcd(M',nu)=1`.

Growth. Neutral and resonant give `M' | l | M_parent`. Pure-eps gives
`M' | l-eps < l <= M_parent`. Dirty with `k=0` (so `eps>=1`, `lex>=1`) gives
`T = l - eps(1+lex) < l <= M_parent`. **`M` can only grow at a dirty step with
`k >= 1`,** and there `M' <= T <= l+Sm <= l+k(l-1) < l(k+1) <= M_parent(k+1)`.

**F4 (strengthening).** Since each NE orbit costs `>= 1`, `sum_i k_i <= B`, so
the total growth factor is `prod_i (1+k_i) <= 2^(sum k_i) <= 2^B`, and `2^B` is
attained (all `k_i = 1`). Exhaustive maximisation of `prod(1+k_i)` under
`sum k_i <= B` for `B <= 7` gives exactly `2^B` (1,2,4,8,16,32,64,128) against
the note's `(B+1)^B` (1,2,9,64,625,7776,117649,2097152). So

```text
Mhat_sharp = M0 * 2^B          (vs the note's  M0*(B+1)^B)
```

is valid and enormously smaller. The note's constant is an over-bound, so
nothing downstream breaks; but every later exponent (`What`, `Wmin`, the
`nu`-bound, the depth bound) inherits the looseness multiplicatively, and the
successor enumerator should use `2^B`.

**Hostile search for faster growth.** I looked for a dirty or pure-eps family
beating `(1+k)` per unit of budget. There is none inside P0: `M' <= T` and
`T <= l+Sm` with `Sm <= k(l-1)` are both tight only through `k`, and `l` is
capped by `M_parent` through `l | M_parent` (St 8.4). The only way to break
this is to let `Sm` grow without paying for it — which requires non-NE
(equality) orbits, i.e. leaving P0. That is F1, §8.

---

## 5. Audit 3 — attack on the compact weight bounds

`2C >= s`: `C >= l(k+lex) - k(l-1) = k + l*lex`, so
`2C - s >= 2k + 2l*lex - 1 - k - lex = k + (2l-1)lex - 1 >= 0` whenever
`k+lex >= 1`, which `C>=1` forces. Then `E = (l-eps) + nu*C >= 1 + 2C >= s`
(using `eps < l`, `nu >= 2`), so the dirty forward multiplier
`l*s/E <= l <= Mhat`. Pure-eps multiplier `l/(l-eps) <= l`. Resonance and
neutral do not expand. 0 violations over 3098 steps.

Upper bound (U): `W_L = w(L+r-1)/L <= r*w` for `L>=1`, at most `B`
positive-cost steps, each `<= Mhat`, so `W <= What = r w Mhat^B`. Correct.

Lower bound (L): forward from any intermediate vertex the remaining
multipliers are `<= Mhat` (positive-cost, at most `B` of them) and `<= 1`
(neutral, resonant), so `W_t <= W*Mhat^B`, i.e. `W >= tau_min/Mhat^B`. Correct.

P1 target set: `0<W_t<1` and `j = M_t(1-W_t) in N*` give
`W_t = 1 - j/M_t` with `1 <= j <= M_t - 1` and `2 <= M_t <= Mhat`, so
`W_t >= 1/M_t >= 1/Mhat = tau_min`. Correct and finite.

Resonance depth: `tau_min <= W_t <= r w Mhat^B (2/3)^R` gives
`R <= log(r w Mhat^(B+1)) / log(3/2)`. Correct; `nu>=2` is what makes the
contraction `n/Delta <= n/(2n-1) <= 2/3`.

Weight-changing `nu`: `(R)` gives `W/W' = nu - (nu-1)/n >= (nu+1)/2 > nu/2`;
`(D)` gives `W/W' = E/(ls) >= nu*C/(ls) >= nu/(2l) >= nu/(2 Mhat)`. Both
combine with `W <= What`, `W' >= Wmin` to the note's
`nu <= 2*Mhat*What/Wmin`. Correct.

**Prompt's two special cases.**

- `k=0`, q-extras-only resonance (`eps=k=Sm=0`, `lex>=1`): `s = n = lex+1`,
  `E = l*Delta`, `w' = w n/Delta` — exactly (R). Forward `<= 2/3`, `M' | l`,
  `lambda = 0`. Nothing escapes: it is the note's clean layer verbatim.
- `eps>0` with q-extras (`C>=1`, `eps>=1`): this is **dirty**, and there
  `T >= 1` caps `lex <= floor((Sm + l - eps(1+k) - 1)/eps)`. Scanned
  `l<=9, k<=3`: with `eps>=1` the largest legal `lex` is 28; with `eps=0`
  the scan ran to its 399 cap without terminating. **F8:** so `s` is a free
  unbounded variable only in the `eps=0, k>=1` dirty family. The §4 product
  therefore has *fewer* free `x_i` than the note claims, which strengthens
  rather than weakens the theorem.

---

## 6. Audit 4 — Lemma 3.1: PROVED

The note's Lemma 3.1 is true. Its own proof is correct but terse; I give a
self-contained replacement that removes both gaps.

> **Lemma 3.1.** Fix positive rationals `q,u,c`, a nonnegative integer `h`,
> positive rationals `v_i,a_i` and integer lower bounds `x_i >= b_i >= 1`.
> Then `u(1+c/L) = q * prod_i (v_i - a_i/x_i)` with every factor positive has
> only finitely many integer solutions `(L, x_1, ..., x_h)`.

*Proof.* Suppose the solution set is infinite. Every coordinate is a positive
integer, so by a diagonal extraction there is an infinite subsequence of
solutions on which each coordinate is either constant or tends to infinity.
Let `S` be the set of coordinates tending to infinity; `S` is nonempty. Absorb
every constant coordinate: each fixed `x_i` contributes the fixed positive
rational `v_i - a_i/x_i` to a new constant `q' > 0`.

*Case A: `L in S`.* Write `R' = q' * prod_{i in S} v_i`. The right side is
`< R'` and tends to `R'`; the left side is `> u` and tends to `u`. (If
`S = {L}` the right side is the constant `R'` and the strictly decreasing left
side meets it at most once, contradicting infinitude.) Otherwise equality
along the subsequence forces `u = lim LHS = lim RHS = R'`, while every term
satisfies `RHS < R' = u < LHS = RHS`. Contradiction.

*Case B: `L` constant.* The left side is a constant `U`, so `S` contains some
`x_i` and the right side tends to `R'` strictly from below while being
identically `U`. Then `U = R'` and `U = RHS < R' = U`. Contradiction. **QED**

**F2 (presentational, low).** Two things in the note's own proof:
(i) "The right side is strictly below its limit `R = q*prod v_i`" is false at
`h = 0`, where the right side *equals* `R`. The conclusion is unaffected
(`h=0` gives `L = uc/(R-u)`, at most one value, or none if `R<=u`), but the
sentence as printed is not universally true.
(ii) The branch "If it is `L`, fix it and use the identical argument for the
remaining product variables" silently invokes a *pure-product* sub-case,
`U = q*prod(v_i - a_i/x_i)` with `U` fixed, which is not literally the lemma's
statement. It is true and the "identical argument" does work — with `L` fixed
one has `U < R`, so `R - U = R - q*prod(...) > 0` is a fixed positive constant
while the right side tends to 0, forcing a bounded `x_i` and an induction on
`h` with base "at most one solution". The note should say this in one line.

**The strict signs are load-bearing — machine-checked controls.**

| fixture | structure | solutions found |
|---|---|---|
| `R = u` knife edge, `h=1`, four cells | LHS from above, RHS from below | **0** for `x <= 30000` each |
| `u(1-c/L) = q(v-a/x)` at `R=u` | LHS from **below**, RHS from below | 2998 for `x<3000` — **unbounded family** |
| `u(1+c/L) = q(v+a/x)` at `R=u` | LHS above, RHS from **above** | 2998 for `x<3000` — **unbounded family** |

So the theorem's conclusion is false the moment either side's approach
direction flips. That is exactly the structure §3 of the note calls
"opposite-side", and it is the whole content of the lemma.

**Directed search for a counterexample.** Random hostile `h=1` sweep: 1200
instances, 895 solutions, at most 24 per instance, none unbounded. Tiny-gap
sweep `R-u in {1/10, 1/100, 1/1000, 1/10000}`: 4/6/31/14 solutions with
`maxL` 120 / 10200 / 1002000 / 100020000 — finite, but showing that `L` can be
enormous. Structured `h=2` sweep over 2×144×3×2 parameter cells with
`x_i < 45`: 8884 solutions total, at most 160 per instance, `maxL = 13104`.
Adversarial commensurable `h=2,3` corners: no infinite family. **No
counterexample to Lemma 3.1 was found.**

**F9 (informational).** There is no uniform bound on the *number* of surviving
`L` per path type — the count is a divisor count and can be made as large as
one likes (`y | u*c*h` gives `d(uch)` solutions: 6, 12, 24, 48, 120 for
`h = 12, 60, 360, 2520, 55440`). Finiteness only; the note claims only
finiteness, so this is a consumer warning, not a defect.

**F3 (strengthening — an effective corner bound).** The note's induction is
effective but tower-sized: each level's threshold depends on the constants
absorbed at the previous level. There is a clean closed form. Every backward
factor `v_i - a_i/x_i` is *strictly increasing* in `x_i`, so the right side is
increasing in the product order, so `L = u c/(RHS - u)` is *decreasing*; hence
`L` is maximal at the coordinatewise-least qualifying corner:

```text
if  P0 := q * prod_i (v_i - a_i / x_i^0)  >  u    then   L <= u*c/(P0 - u),
where x^0 is the least tuple (>= the lower bounds) with q*prod(...) > u.
```

For `h = 1` this is a single scan and always applies. Verified: on the witness
`w=7/4, r=4, nu=3, tau=3/5` the first qualifying `n` is 25, the bound is
`L <= 2625`, and the observed maximum over `n <= 4000` is **exactly 2625**
(48 surviving `L`) — the bound is attained. Swept over 1620
`(w,r,nu,tau)` cells: **0 violations**. I recommend the successor adopt this
as the enumerator's cap-free stopping rule.

---

## 7. Audit 5 — the product assembly and the finiteness of path types

Composing backwards along a fixed reduced path,

```text
W_L = W_t * [prod_{pure-eps} (l-eps)/l] * prod_{res}(nu - (nu-1)/n)
                                        * prod_{dirty}(nu - K/(l s)),
```

neutral steps contributing 1. This is exactly Lemma 3.1's shape with
`u = w`, `c = r-1 >= 1` (this is where `r >= 2` is load-bearing — at `r=1`
every `L` gives the same `W_L` and the conclusion would be false),
`q = W_t * prod (l-eps)/l > 0`, `v_i = nu_i`, `a_i in {nu_i - 1, K_i/l_i}`,
`x_i in {n_i, s_i}`. Both `a_i` are strictly positive: `nu>=2` gives
`nu-1 >= 1`, and `K = nu(l+Sm) - l + eps >= 2l - l + eps = l + eps > 0`.

**Type finiteness.** Depth is `<= B + R_max`; per step the labels are
`l <= Mhat` (`l | M`), `eps < l`, `k <= B`, `m_j < l`, `Sm <= k(l-1)`, and the
weight-changing `nu <= 2 Mhat What/Wmin`. Every one of these bounds is
independent of `L`: `M_L | r mu = M0`, `W_L <= r w`, `tau_min = 1/Mhat`. That
`L`-uniformity is the actual repair over Grok §4, and it holds.

**Can changing `M`, residue classes, `l`, partitions or local legality create
infinitely many types at bounded depth?** No. `M <= Mhat`, so `l`, `eps`, `k`,
the partition `(m_j)` and the divisor/residue records all range over finite
sets; each such constraint (`l|M`, `kbar in Z`, `M' | T`) only *restricts* the
solution set, so dropping it keeps the argument superset-safe. Neutral runs of
unbounded length contract to one divisor record because they multiply weight
by 1 and send `M` to a divisor — a superset of what is achievable.

**Corroboration (bounded search, not proof).** A direct P0 closure at depth
`<= 3`, `B = 2`, caps `nu<=7, lex<=4, k<=2`, over `L = 1..400`:
`(r,mu,w)=(2,6,3/2)` gives 1 surviving `L` (`L=1`);
`(2,1,2)` gives 0; `(3,4,4/3)` gives 0; `(2,12,1/2)` gives 2 (`L=1,2`).
This is capped search and I do not treat it as evidence of the theorem — only
as a failure to find the predicted failure.

**Focusing fixtures.** Directed hostile attempt to send infinitely many `L` to
one target through a single backward step, with legality *dropped* (superset):
one resonance focuses at most **42** distinct `L` in the sweep
(`w=7/4, r=4, nu=3, tau=3/5`, `L` up to 2625); one dirty step at most **34**
(`w=3/2, r=3, nu=2, l=1, Sm=3, eps=0, tau=4/5`, `L` up to 1710). In both the
surviving `L` decrease monotonically toward the finite limit
`L_inf = w(r-1)/(tau*nu - w)` and stop. Focusing is real, bounded, and
governed exactly by the mechanism §3 of the note describes.

---

## 8. F1 — the sharp scope boundary: root-mult equality orbits

P0's NE laws are **strict** (`eps*dq < dp`, `m_j*dq < dp`); the equality case
is the printed root-mult law (R). So within P0 the note's partition is
complete. Outside it — at a vertex carrying an arriving edge, i.e. a P2 merge
— a `p`-orbit can sit at `m*dq = dp`. That family is invisible to the note and
is worth stating exactly, because it breaks both of its mechanisms.

Adding `j` equality orbits of multiplicity `m` raises `Sm` by `jm` and `s` by
`j`, and `m*dq = dp` is preserved for every `j` (the `j`-terms cancel). Then

```text
E  = l*dq - m*dq = (l-m)*dq,          kbar = l*W/(l-m)      (s-free!),
W' = kbar*s/dq,   M' = gcd(m*dq,dq) = dq = nu*s+1,
backward factor  W/W' = ((l-m)/l) * (nu + 1/s).
```

Two failures, both machine-checked on `l=4, m=1, nu=2, W=3/2`,
`s = 1..8`:

- the backward factor is `9/4, 15/8, 7/4, 27/16, 33/20, 13/8, 45/28, 51/32`,
  strictly **decreasing to `((l-m)/l)*nu = 3/2` from above** — the exact
  reversal that my §6 control shows admits infinite families;
- `M' = 3,5,7,9,11,13,15,17,...` is **unbounded in `s`**, so Lemma 2.1's
  `M <= Mhat` and hence the finiteness of the P1 target set both fail. The
  children `W' = 2s/(2s+1)` with `M' = 2s+1` are all P1-legal
  (`0<W'<1`, `M'>=2`, `j = M'(1-W') = 1 in N*`): one parent reaches
  **infinitely many** P1-legal terminals.

**But the conclusion still survives one step of widening,** by a different
argument: `kbar = l*W/(l-m)` is `s`-free, so `kbar in Z` pins

```text
W = kbar*(l-m)/l,      and    j = M'(1-W') = (nu - kbar)*s + 1 >= 1
                              forces kbar <= nu.
```

The parent weight is therefore one of finitely many `s`-independent rationals
(58 distinct values over `l<=8, nu<=5`), so at most finitely many `L` satisfy
`W_L = kbar(l-m)/l`. Verified: 0 deviations from `kbar`-rigidity, `M'=dq`, and
the `j`-law over `l<=8, m<l, nu<=5, kbar<=nu, s<=39`.

Consequence for the record: the note's theorem is **correct and its P0
restriction is exactly right**, but a consumer who reads "the trunk below the
U2 merge is finite" as covering a trunk that meets a *further* merge is
reading beyond the proof. In that regime the note's Lemma 2.1 and Lemma 3.1
hypotheses both fail and are replaced by `kbar`-rigidity. Severity: scope
clarification, not a defect — the note says "P0 path" and means it.

---

## 9. Audit 6 — is the neutral / pure-eps free-`nu` quotient legal?

**Yes, for the stated P0/P1 terminal theorem.** The theorem's predicate is
"exists a P0 path from `(W_L,M_L)` to a P1-legal terminal within budget `B`".
Every ingredient of that predicate factors through the reduced pair `(w,M)`:

- P1 is `0<W_t<1`, `M_t>=2`, `j = M_t(1-W_t) in N*` — a function of `(W_t,M_t)`
  alone, and `psi = ceil(M_t/j) - 1` likewise;
- modeled `lambda` is 0 for neutral and resonant *for every* `nu`, and the
  pure-eps price `ceil(l*w/eps)` is `nu`-free (it equals the AF2 `eps`-term
  because `T=E` there);
- the `nu` of dirty and resonant steps is *not* quotiented — it is bounded
  type data;
- neutral/pure-eps `nu` reaches only `M' = gcd(l,nu+1)` resp.
  `gcd(l-eps,nu+1)`, and taking all divisors is a superset, so no path is lost.

**Consumers that would invalidate the quotient if the conclusion were widened**
(this is the list the successor must not cross):

1. **P2 arrival law / merge legality.** "An edge of mult `mu` can leave a chain
   vertex of state `(w,M)` only at a vertex `(nu_H, M_H)` with `mu | M_H`,
   `M_H = gcd(l,nu_H+1)` — so `nu_H = -1 (mod mu)`." This consumes the
   *actual* last-vertex `nu`, which the quotient forgets. Grok46's finite-chain
   review says the same in its §1.3: "Last-vertex `nu`, `kbar = w(nu+1)` on the
   neutral ray, and full pattern degree remain unbounded at cost 0; they are
   not reduced-state coordinates."
2. **Case-III / class-B / class-C merge handshakes (R2.1, BOOK §10 P3).**
   `kbar = (mu_0 nu_H2 w_2 - 2)/(mu_0 - 1)` and the cell equations need
   `nu_H`, `kbar`, `dp`, `dq` — none reduced-state coordinates.
2b. **The equality-orbit regime of §8**, whose whole content is `kbar`-pinning.
3. **T1-rigidity / exact Prop 8.1(iv) solves** on surviving cells, which need
   the fully pinned `(kbar, X, dp, dq, nu, M)` tuple.
4. **Full pattern degree / `num(w)` bookkeeping** (`Delta | num(w)`,
   `E | l*num(w)*T`): the reduced pair records neither `deg p` nor `deg q`.
5. **BOOK §10 P5's own rider**, which already says the `(w,M)` theorem
   "quotients [nothing] for all consumers" and keeps every entry
   `OPEN_UNBOUNDED_MIXED_OR_POSTJUMP`.
6. Landing, Statement 3.9 gluing, realization, panel exclusion, `td` ceiling —
   excluded by the note itself.

**F5 (hypothesis hygiene, low).** `nu >= 2` is load-bearing in §1.2 and §2
(`a = nu-1 > 0` in (R), `K > 0` in (D), `E >= 1+2C` in Lemma 2.2, and the
`2/3` contraction) but is stated only in §1.1. For robustness I checked the
`nu = 1` degeneration: the backward factor becomes `1 - (eps+Sm)/(l s)`, still
approaching its limit **from below**, and `E = (l-eps)+C >= 1+s/2` still gives
`l s/E < 2l`. So the sign structure and (U) survive `nu=1` with `Mhat -> 2Mhat`
— hygiene, not a hole. Recommend restating `nu>=2` as a standing hypothesis.

**F6 (usage, low).** The note fixes `B` abstractly, but P1's budget
`sum lambda <= td - 1 - psi` *couples* the budget to the terminal. Since
`0 < W_t < 1` forces `psi = ceil(1/(1-W_t)) - 1 >= 1`, the safe uniform
instantiation is `B = td - 2`; any consumer who instantiates `B` per-terminal
must take the maximum over the terminal set for the theorem's `Mhat`, `What`,
`Wmin` and depth bound to be uniform. One sentence, not a defect.

---

## 10. Maximum safe consequence

Exactly this implication, and nothing more:

> **If** Grok's absorbed-U2 transport display is correct at a named entry
> (`W_L = w(L+r-1)/L`, `M_L = gcd(r mu, r+L)`, `w` a fixed positive rational,
> `r >= 2`, `mu >= 1` fixed) **and** BOOK-OFFAXIS §10's P0/P1 grammar and
> modeled lambda prices are as reviewed, **then** for each fixed numerical
> modeled budget `B` only finitely many integers `L >= 1` admit a P0 path from
> `(W_L, M_L)` to a P1-legal terminal, and the bound is uniform in `L`.

It does **not** establish, and must not be cited for:

- Grok's U2 ODE, normal form, `nu=1` absorption, low-`td` controls, or the
  unbounded-lex support lemma (Fable's active review is the authority);
- Statement 3.9 gluing, landing, source realization, a panel exclusion, a `td`
  ceiling, or any JC2 consequence;
- any trunk that passes through a **further merge** — outside P0, where §8
  shows both of the note's mechanisms fail and a separate `kbar`-rigidity
  argument is required;
- any *effective* cap usable by an enumerator without first adopting the
  corner bound of F3; the note's own induction yields a tower;
- any statement about the number of surviving `L` (F9), the survivors'
  existence (all counts here are superset-alive), the mixed/full-cell
  quotient, or the `OPEN_UNBOUNDED_MIXED_OR_POSTJUMP` riders in §10 P5;
- any promotion of `ladder/BOOK-OFFAXIS.md`. No canonical file was edited.

**Valid narrower lemmas preserved,** independent of the top-level verdict:
(a) the exact backward laws (R), (E), (D) and the four-family partition of P0;
(b) `M' | T`, `gcd(M',nu)=1`, `M' <= T <= l+Sm`, and `Mhat_sharp = M0*2^B`;
(c) `2C >= s`, `E >= 2C >= s`, and the per-step multiplier bound `l*s/E <= l`;
(d) Lemma 3.1 in the strengthened form of §6, with the corner bound of F3;
(e) `kbar`-rigidity of the equality-orbit family (§8).

---

## 11. Commands, counts, and boundaries

Clean-room scratch in `/tmp/u2rev` (nothing written outside it and this
report):

| file | sha256 | what it establishes |
|---|---|---|
| `p0model.py` | `1b694f70…` | P0 step model from BOOK §10 P0; asserts the `E` and `nu*T` identities |
| `check1.py` | `0d418af9…` | 3098 legal steps, 4 families, resolvent identity 3098/0, **0 violations** of every §1–§2 claim |
| `check2.py` | `ed2b126c…` | `C=0` partition 0 counterexamples; `lambda=0` families `= {neutral,resonant}` over 2985 steps; backward-factor monotonicity 0 violations |
| `lemma31.py` | `fb6225fa…` | knife edge `R=u` -> 0 solutions ×4; tiny-gap finiteness; 1200-instance `h=1` sweep; two sign controls -> unbounded families |
| `l31_h2b.py` | `81223235…` | `h=2` sweep, 8884 solutions, max 160/instance, `maxL=13104` |
| `l31_h23.py` | `9af0ab86…` | adversarial `h=2,3` corners; divisor blow-up of the solution count |
| `focus.py` | `d45b7086…` | capped genuine-P0 closure over `L=1..400`, four entries |
| `hostile_focus.py` | `5526b482…` | one-step focusing fixtures: max 42 (resonance) / 34 (dirty) distinct `L` |
| `sharp.py` | `bbeaa82a…` | corner bound sharp (2625 attained), 0 violations / 1620 cells; equality-orbit sign reversal and `M'` blow-up |
| `rigid.py` | `1e34f928…` | `kbar`-rigidity 0 deviations; `eps>=1` caps `lex` at 28 vs unbounded at `eps=0`; `max prod(1+k_i) = 2^B` for `B<=7` |
| `bodyhash.py` | `bfdf6f08…` | full/body hash recomputation under both conventions |

Headline counts: 3098 exhaustively enumerated legal P0 steps with **0**
violations of any asserted inequality and 3098/3098 resolvent-identity
agreement; 2985 further steps for the zero-cost census; ~11k Lemma 3.1
instances across `h = 1,2,3` with **no** infinite family; 1620 corner-bound
cells with **0** violations; 4 knife-edge cells with **0** solutions and 2
sign-flipped controls with unbounded families.

Boundaries honoured: no web, no AWS, no commit, no push, no canonical edit, no
heavy CAS, no long or high-memory local process (longest single command 20 s;
peak working set a few tens of MB; two commands were killed at a 2-minute
guard and re-run smaller, which is recorded here rather than hidden).
`jc2-lean` was never accessed, listed, searched, built, statused or
controlled. No global `git status`; no workspace-wide search; `git` was not
run at all. The only file created inside the repository is this report.

---

Report-body SHA-256 (all bytes before the separator line above):
`eba44e04f3628e2fa7214c12a6bcefda5c9c3371c6f4af677660c51827967804`.
