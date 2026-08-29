# Cap-free `M>=2` budget quotient — primary research (Opus 5, 2026-08-29)

Lane: exact Opus 5, whole-campaign researcher, maximum reasoning.
Target: `REDUCTION.md` §5.2 / CRITICAL 5–6 — the first genuinely unbounded
landing wall, attacked as a **symbolic quotient** of the post-jump/off-axis
`M>=2` grammar rather than as another capped enumeration.

## 0. Custody and scope

Read, in full, exactly the licensed set:
`ladder/REDUCTION.md` (Critical 4–7, §§5.1–5.3, plus the frontier overlay,
Executive verdict and §0 conventions needed to type the objects),
`ladder/BOOK-OFFAXIS.md` (§§0–11a, including P0–P5 and the 2026-08-28
root-classification correction), `ladder/SHEET6-DEPTH.md`,
`ladder/SHEET6-MULTIPOLE.md`, and Card 1 / Card B / Card 2 of the three
named ideation files. No other ideation material was opened.

Not done, as instructed: no access of any kind to `jc2-lean`; no web, AWS,
heavy CAS, canonical edit, commit or push. One desk-scale stdlib-Python
verification script was staged in `/tmp/m2q_check.py` (not in the
repository) and run; its full transcript is reproduced in §9.

Nothing below claims JC2, full landing, `G2-BD`, `G2-PSC`, or a finite book
beyond what is proved here. Every statement carries its own tier.

**Standing trust perimeter** (all pre-existing, nothing new assumed): the
`BOOK-OFFAXIS.md` §10 trust perimeter verbatim — corrected St 9.3 (24) with
the E6 sign fix, St 9.4 (25)/(26) with H3-psi, St 8.4 (`mu_e | M_parent`),
MP2, MP5/MP8 on `b=1` chains, R1.0 (q-multiplicity rigidity), R1.2/R1.4
transport, R2.1/R2.2 merge handshakes and shape laws, Prop 9.3 (a)–(m).
Everything I prove is a consequence of that recorded system; I add no
hypothesis. Where a conclusion needs something the record does *not* supply,
it is labelled OPEN and named.

## 1. Verdict in one paragraph

The proposed theorem is **TRUE for the chain layer and FALSE AS STATED for
the merge layer, and its "finite union of families" conclusion is correct
while its "finite branching" premise is wrong in a way that matters.** The
correct object is not a finite set of cells: I exhibit two *exact infinite*
families of budget-fitting, `lambda=0`, T1-alive cells inside the charged
grammar (§6), and I show that the entire promoted `td=7` off-axis book
(`BOOK-OFFAXIS.md` §11a, 17 rows) is *literally three linear families in
`mu_0`*, truncated only by the arrival `w`-alphabet, not by any cell-level
finiteness. What *is* finite is the **reduced state** `(w, M)` together with
a semilinear fibration in the free parameter `nu`. I prove the exact
invariant that makes this work — a single divisibility law
`M | P - s*eps` (Theorem 1) that generalizes MP6(d) subadditivity, R2.2(D),
and the `M_F = gcd(l, nu+1)` neutral law simultaneously — and an exact
dichotomy `C_e = mu_e*s - P` (Theorem 2) that decides, vertex-locally,
whether `nu` is a free semilinear parameter or a bounded one. The quotient
by congruence classes is **not** sufficient as the proposal states: at a
Proposition 9.3 case-III zero-edge the *full* value of the arriving `nu`
enters linearly, and it is then pinned, not free. Finally, the
ranking-or-lasso formulation of Card 1 is **mathematically the wrong
formulation**: the system provably has infinite runs, so no ranking function
exists, and the lasso it would return is the already-known neutral family —
a vacuous answer. The budget-quotient formulation is the correct one.

The single named first obstruction to generalizing the `td=7` cap-free
inversion is stated in §8: **an upper bound on `kbar` at a merge with no
frozen (`b=1`, singleton-`W`) partner.** At `td=7` that bound is supplied by
the `td=7`-specific pin `kbar = 2*dq/(dq-dp)` plus the T1 zero-chain law;
with two off-axis arrivals the pin degenerates and no printed statement
replaces it.

## 2. One-vertex normal form for the charged `M>=2` grammar

Every statement below is in the `i`-normalized shape space of the engines
(`SHEET6-DEPTH.md` §1): `rho := D/deg(p)`, `kbar := kappa*(1-pi)`,
`w := (kbar - rho)/nu`. By R1.0 (q-multiplicity rigidity, proved in
`BOOK-OFFAXIS.md` §6 and review-confirmed) every vertex `F` in
`T_a^searrow ∩ V_a` has reduced pattern

    p = (-)eta^eps * prod_{e=1..r0} (eta^nu - c_e^nu)^{mu_e}
                   * prod_{j=1..k} (eta^nu - d_j^nu)^{m_j}
    q = (-)eta * (s distinct nu-orbits, every root simple)

with `r0` = number of distinct **nonzero** arriving orbits, `k` = number of
non-chain ("extra") root orbits, `lex` = number of q-orbits off `p`, and
`s = r0 + k + lex`. Write

    P  := sum_e mu_e + sum_j m_j          (all nonzero p-multiplicities)
    dp = eps + nu*P,      dq = 1 + nu*s,      M = gcd(dp, dq).

`eps` has two distinct regimes, and the record conflates them nowhere but
prices them differently (P0 vs P2):

* **free 0-root** (`eps>=1`, no chain arrives at the 0-direction): it is a
  northeast direction, `eps*dq < dp` strictly, and it is priced `lambda>=1`;
* **0-arrival** (`eps = mu_0`, a chain arrives at the 0-direction, Prop 9.3
  case III): it is southeast, `mu_0*dq > dp`, and it prices `0`.

A chain vertex is `r0 + [0-arrival] = 1`; a merge has `r(G) >= 2` arriving
edges in total. Both are covered uniformly below.

**Recorded laws used (no new hypotheses).**
(S) searrow, for every arriving edge: `mu_e*dq > dp` (St 8.2 via R2.2(S)).
(NE) for every non-arriving orbit: `m_j*dq < dp`, and `eps*dq < dp` for a
free 0-root, both strict.
(R) root-mult law: `dp != mu_star * dq` for every multiplicity `mu_star`
occurring in `p` (R1.0).
(T) transport, `i`-normalized Prop 9.3(c),(d) with `deg(p_parent) = i*mu_e`
(St 8.3(ii) + Prop 8.1(i)); this is P0/R1.2/R1.4/R2.1 in one line:

    E_e := mu_e*dq - dp  ( > 0 by (S) ),
    kbar = mu_e * w_e * dq / E_e,   rho = kbar/dq,   X = kbar*dp/dq,
    w    = mu_e * w_e * s  / E_e.                                    (T)

Consistency across edges is exactly R2.1: `X = mu_e*(kbar - w_e)`.
(I) integrality: `kbar in Z` whenever `nu >= 2` (DS1(c), Not 3.5); at
`nu = 1` the vertex is a case-I lattice meet and `kbar in Q` is legal.
(L) price: `lambda >= sum_j max(1, ceil(X/m_j - kbar))
             + [free 0-root] * max(1, ceil((X/eps - kbar)/nu))`
(P0/P2, AF2 rule); arriving edges and the `lex` q-extras price 0 (MP8 rows).

Immediate consequence of (NE) + (S): every non-arriving multiplicity obeys
`m_j < dp/dq < min_e mu_e`, hence **`m_j <= mu_min - 1`**, and a free 0-root
obeys `eps <= mu_min - 1`. This one inequality is load-bearing below.

Two sanity anchors, both reproduced exactly by the script of §9: the
`P0` four-escape menu out of the `td=7` chain-2 state `(w,M) = (3/2,2)` —
`(A) (21,15) -> (2/3, M3)`, `(C) (20,16) -> (3/4, M4)`,
`eps (7,5) -> (2, M1)`, `pure-b -> (3, M1)` — and all 17 rows of the
promoted §11a book.

## 3. Theorem 1 (the `T`-law): one divisibility governs every `M`

> **Theorem 1.** At every vertex of the grammar of §2,
>
>     M = gcd(dp, dq)  divides  T := P - s*eps,     and  T != 0.
>
> Consequently `M <= |T|`, and `M` is a function of `nu` **modulo `|T|`**,
> where `|T|` depends only on the discrete pattern data `(mu_e, m_j, eps,
> r0, k, lex)` and not on `nu`.

*Proof.* `M | dp` and `M | dq`, hence `M` divides the integer combination
`P*dq - s*dp = P*(1 + nu*s) - s*(eps + nu*P) = P - s*eps = T`. If `T = 0`
then `dp = eps*dq`, which is exactly the case forbidden by the root-mult law
(R) applied to the multiplicity `mu_star = eps` of the 0-root; so `T != 0`.
For the congruence claim: for each divisor `d | T`, `d | dq` iff
`nu*s == -1 (mod d)` and `d | dp` iff `eps + nu*P == 0 (mod d)`; both are
congruence conditions on `nu` modulo a divisor of `|T|`, so `M`, being the
largest such `d`, is determined by `nu mod |T|`. ∎

**Why this is the right invariant.** Theorem 1 specialises to, and unifies,
every `M`-law in the promoted record:

| specialisation | data | `T` | recorded form |
|---|---|---|---|
| neutral chain step | `r0=1, mu=l, k=lex=eps=0, s=1` | `l` | `M_F = gcd(l, nu+1) \| l` (P2 arrival law) |
| clean resonant step | `k=eps=0, lex=n-1, s=n` | `l` | `M_F = gcd(l, n*nu+1) \| l` (R1.2) |
| pure-(b) step | `k=lex=0, eps>=1, s=1` | `l-eps` | `M_F = gcd(l-eps, nu+1)` (P0(ii)) |
| all-`mu=1` IIa merge | `eps=0,k=0, r0=r` | `r` | `M_G = gcd(r, l*nu+1) \| r` (MP6(d)) |
| general merge, `eps=k=0` | — | `sum mu_e` | `M_G \| sum mu_e` (R2.2(D)) |
| **general merge, `eps>=1` or `k>=1`** | — | `P - s*eps` | **not in the record** |

R2.2(D) states subadditivity `M_G | sum mu_e` "iff `eps = 0` and `k = 0`",
and flags the `dq < dp` case as an open rider. Theorem 1 **discharges that
rider**: the law never fails, it merely changes its right-hand side from
`sum mu_e` to `P - s*eps`. On the 17 promoted §11a cells the law holds with
equality `M = |T|` in 16 rows and with `M = 5 | 15` in the one `kbar = 7`
row (script §9, block A). This is the first uniform `M`-law valid at mixed
all-`mu>=2` merges, which is precisely the object `SHEET6-MULTIPOLE.md` §4
lists as "Open, stated, NOT claimed".

## 4. Theorem 2 (the `C`-dichotomy): exactly which `nu` are free

Define, per arriving edge `e`,

    C_e := mu_e * s - P,     so that     E_e = mu_e*dq - dp = (mu_e - eps) + nu*C_e.

> **Theorem 2 (free-parameter dichotomy).** Fix all discrete pattern data
> `(eps-regime, r0, {mu_e}, k, {m_j}, lex)`. Then:
>
> 1. If `C_e = 0` for the binding edge, `E_e = mu_e - eps` is **independent
>    of `nu`**; `kbar = mu_e*w_e*(1+nu*s)/(mu_e-eps)` is **affine and
>    unbounded in `nu`**, while the successor data
>    `w = mu_e*w_e*s/(mu_e-eps)` is **constant in `nu`** and `M` depends on
>    `nu` only mod `|T| = s*(mu_e - eps)`. The admissible `nu` form a finite
>    union of arithmetic progressions (from `kbar in Z` and the
>    `M`-congruences). This is a genuinely infinite, semilinear family.
> 2. If `C_e != 0` then `nu` is **bounded**:
>    `nu <= (E_e + eps - mu_e)/C_e` when `C_e >= 1`, and
>    `nu < (mu_e - eps)/|C_e|` when `C_e <= -1` (forced by `E_e > 0`).
> 3. `C_e = 0` for some `e` **iff** `k = 0`, `lex = 0`, no chain arrives at
>    the 0-direction, and all nonzero arrival multiplicities are equal
>    (`mu_e = mu` for all `e`), with `0 <= eps < mu` a free 0-root.
> 4. If a chain **does** arrive at the 0-direction (case III) then
>    `C_0 = mu_0*s - P >= 1` by (S) and `E_0 = nu*C_0 = nu*|T|`; combined
>    with Theorem 4 this bounds `nu <= mu_0 * num(w_0)` **unconditionally**.

*Proof.* 1 and 2 are the displayed identity `E_e = (mu_e-eps) + nu*C_e`
together with `E_e > 0` from (S); the `w`-formula in (T) has `nu` only
through `E_e`, so `C_e = 0` makes it constant; `M | T` is Theorem 1 and
`T = P - s*eps = mu_e*s - s*eps = s*(mu_e - eps)` when `C_e = 0`.
For 3: `C_e = mu_e*(r0+k+lex) - sum_{e'} mu_{e'} - sum_j m_j`. By the
`m_j <= mu_min - 1` inequality of §2, taking `e` with `mu_e = mu_min`,
`C_min <= mu_min*(r0+k+lex) - r0*mu_min - k*(mu_min-1) - (sum mu - r0 mu_min)
       = mu_min*lex + k - (sum mu - r0*mu_min)`,
and the last bracket is `>= 0` with equality iff all `mu_e` are equal.
Conversely with equal `mu`, `k = lex = 0` gives `C = 0` exactly. If a
0-chain arrives, `eps = mu_0` is itself an arrival and (S) gives
`mu_0*dq > dp`, i.e. `mu_0*(1+nu*s) > mu_0 + nu*P`, i.e. `mu_0*s > P`, i.e.
`C_0 >= 1`; then `E_0 = mu_0*dq - dp = nu*(mu_0*s - P) = nu*|T|` since
`T = P - s*mu_0 < 0`. That is 4's identity; the bound is completed in
Theorem 4. ∎

Block D of the script verifies clause 3 exhaustively over
`l <= 6, k,lex <= 3` with all legal `m_j`: `C = 0` iff `k = lex = 0`.

**Reading.** Theorem 2 is the exact answer to "isolate all products of
unbounded variables that leave Presburger or semilinear arithmetic". The
transport law (T) is a **ratio of two affine functions of `nu`**,
`kbar = mu*w*(1+nu*s)/((mu-eps)+nu*C)`. That is not Presburger-definable.
But the ratio degenerates exactly along `C = 0`, where it becomes affine
(hence Presburger), and where it does *not* degenerate it is strictly
monotone and bounded in `nu`, so integrality of `kbar` admits only finitely
many `nu`. **The grammar is semilinear not because it is Presburger, but
because the single non-Presburger operation it performs has a clean
degeneracy locus.** That is the mechanism the proposed theorem was reaching
for, and it is sharper than a congruence quotient.

## 5. Theorem 3 (cost) and Theorem 4 (integrality bounds)

> **Theorem 3 (zero-cost characterisation and monovariants).**
> Under the recorded price (L):
>
> 1. `lambda_F = 0` is available **iff** `k = 0` and there is no free
>    0-root; in that case `lambda >= k + [free 0-root] = 0`. In particular
>    `lambda_F >= k + [free 0-root]` always, so at a step of cost `lambda`
>    at most `lambda` extra searrow orbits and at most one free 0-root
>    occur.
> 2. **On a chain vertex** (`r0 = 1`, nonzero arrival of mult `l | M_parent`)
>    with `lambda = 0`: `T = l`, hence `M_F | l | M_parent`. So **`M` is
>    non-increasing under divisibility along every zero-cost chain run**, and
>    every increase of `M` on a chain costs `lambda >= 1`.
> 3. **On a merge vertex** with `lambda = 0` (`eps = 0`, `k = 0`):
>    `T = sum_e mu_e`, so `M_G | sum_e mu_e <= r0 * max mu_e`. Zero-cost
>    `M`-growth therefore happens only at merges and only by a factor
>    `<= r0 <= r`. By MP1 (`sum (r-1) = m-1`) the total zero-cost growth
>    factor over a whole configuration is at most `max(m, 2^(m-1))`.
> 4. `num(w)` is non-increasing along zero-cost chain runs and strictly
>    contracts by a factor `<= 2/3` at every resonant (`lex >= 1`) one, with
>    `den(w)` **invariant**; hence fewer than `log_{3/2} num(w_0) + 1`
>    resonant zero-cost steps per run (DS3 verbatim, now with `l` cancelled).
> 5. At a positive-cost step `M_F | T` with `|T| <= P + s*eps`, and in the
>    free-0-root regime (`eps*dq < dp`) one has `T > 0` and therefore
>    `M_F <= P = l + sum_j m_j <= l*(1+k) <= M_parent*(1 + lambda_F)`.
>    Iterating over the at most `B := td - 1 - psi` charged steps,
>    `M <= M_entry * max(m, 2^(m-1)) * prod (1+lambda_i)
>       <= M_entry * max(m,2^(m-1)) * 2^B`.

*Proof.* 1 is (L) read literally. 2, 3, 5 are Theorem 1 with the indicated
data (`eps = 0, k = 0` gives `T = P = sum mu_e + sum m_j = sum mu_e`), plus
`sum_j m_j <= k*(l-1)` from `m_j <= l-1`, plus the fact that under (NE) a
free 0-root forces `eps*s < P`, i.e. `T > 0`. 4 is DS3: in (T) with
`eps=k=0`, `E = l*Delta`, `Delta := (n-1)nu+1`, so `kbar = w*dq/Delta` and
`gcd(Delta, dq) = gcd(Delta, nu) = 1` force `Delta | num(w)`, while
`w_F = w*n/Delta` keeps the denominator. The `l`-factor cancels identically,
which is exactly R1.2's "`l`-fold thickening CANCELS". ∎

Clause 5 is the direct repair of `BOOK-OFFAXIS.md` §10 P5's "at a fixed
budget, reachable states can have unbounded numerator and `M`". **`M` is
bounded at fixed budget, effectively.** At `td = 7`, `b = 2`, `B <= 5`,
`m = 2` the bound reads `M <= 2 * 2 * 32 = 128`; the engine's observed
closure at budget 5 tops out at `M = 25`, and the promoted §11a book at
`M = 49`. Both are inside the bound. The bound is not sharp; it is
*effective and cap-free*, which is the property P5 says does not exist.

> **Theorem 4 (integrality bounds).** Let `nu >= 2` (so `kbar in Z` by (I)),
> and let `w_e = a_e/b_e` in lowest terms on an arriving edge `e`. Then
>
>     E_e  <=  M * mu_e * a_e ,                                     (4a)
>     kbar >  w_e  and  dq/dp = kbar / (mu_e*(kbar - w_e)) ,         (4b)
>     dq/dp <= kbar_min * b_e / mu_e,  kbar_min := floor(w_e)+1 .    (4c)

*Proof.* (4a): `kbar = mu_e*a_e*dq/(b_e*E_e) in Z` gives
`b_e*E_e | mu_e*a_e*dq`, so `E_e | mu_e*a_e*dq`. Put `g := gcd(E_e, dq)`;
then `E_e/g` and `dq/g` are coprime, so `E_e/g | mu_e*a_e` and
`E_e <= g*mu_e*a_e`. Finally `g | E_e` and `g | dq` give
`g | mu_e*dq - E_e = dp`, so `g | gcd(dp,dq) = M`. (4b): `E_e < mu_e*dq`
gives `kbar > w_e`; solving `kbar*(mu_e*dq - dp) = mu_e*w_e*dq` for
`dq/dp` gives the identity. (4c): `kbar - w_e >= 1/b_e` since `kbar` is an
integer exceeding `a_e/b_e`, and `x/(x-w_e)` is decreasing in `x`. ∎

(4a) is the engine of Theorem 2 clause 4: with `E_0 = nu*|T|` and
`M | |T|` we get `nu*|T| <= M*mu_0*a_0 <= |T|*mu_0*a_0`, hence
**`nu <= mu_0 * num(w_0)` at every case-III 0-arrival vertex**, with no cap
and no reference to the merge cell. Block E of the script confirms (4b) on
the promoted cells.

## 6. Two exact infinite families inside the charged grammar

Theorem 2 clause 1 is not vacuous. Both families below satisfy **every**
recorded law: R1.0 shape, (S), (NE), (R), `dq == 1 (mod nu)`,
`gcd(M,nu) = 1`, `kbar in Z`, MP2, the §11 T1 zero-chain law, and
`lambda = 0` at the vertex itself.

### 6a. The equal-`(mu,w)` join family (the `s=2` survivors of §9, in closed form)

Take a merge with `r0 = 2` nonzero arrivals of equal multiplicity `mu` and
equal invariant `w = a/b` (the join law R2.1(i) forces equal `w` at equal
`mu`), `eps = 0`, `k = 0`, `lex = 0`. Then for every `nu` with `b | 2nu+1`:

    dp = 2*mu*nu,  dq = 2*nu+1,  E = mu,  T = 2*mu,
    kbar = w*(2*nu+1)   (unbounded, affine in nu),
    M_G  = gcd(mu, 2*nu+1)   (a function of nu mod mu),
    w_child = 2*w            (independent of nu),   lambda_G = 0.

T1 test: the §11 law kills a cell iff `dp | dq`; here `dp = 2*mu*nu > dq`
for `mu >= 1, nu >= 1`, so **no member is T1-dead**. The searrow law (S) is
`mu*(2nu+1) > 2*mu*nu`, i.e. vacuous — which is exactly why R2.3(ii)'s
pruning ("`r = 2, mu = (2,3)` needs `nu = 1`") does not touch the equal-`mu`
case. MP2 (`M >= 2`) selects the congruence `gcd(mu, 2nu+1) >= 2`.
Verified for `(mu,w,nu) = (3,3,1), (3,3,4), (3,3,7), (3,3,100), (5,2,12)`
in block D of the script.

This is precisely `BOOK-OFFAXIS.md` §9's survivor anatomy type (i) —
"equal-`mu` equal-`w` joins (`kbar` underdetermined at stage R)" — now given
in closed form and shown to be **infinite, not merely undetermined**. It is
also the `td=7` class-A "`(2,2t)` M2 tail" at `mu = 1`, `w = 2`, generalized
to all `mu`. At `td = 7` the tail died on budget (P4). At `td >= 8` the
budget is `>= 6` and P5 already concedes budget pricing cannot close those
panels; the first entry with **no** frozen `b=1` partner is the `td = 8`,
`m = 2`, `M`-vector `[2,2]` row of §1, and the `td = 13` `(2,3)`,
`Lambda = (4,9)`, `M = [2,3]` row that §1a flags as the only prime-`td`
survivor with no `b = 1` pole.

### 6b. The promoted `td=7` book is three linear families in `mu_0`

Every one of the 17 promoted §11a cells has `P = 1` and `s = 2` (script
block A). Writing `c := dq - dp` and using the `td=7` chain-1 freeze
`(mu,w) = (1,2)`, which gives `X = kbar - 2` and hence `kbar = 2*dq/c`, the
shape equations `dp = mu_0 + nu`, `dq = 2*nu + 1` collapse to the single
Diophantine identity

    c*(kbar - 4) = 4*mu_0 - 2,     nu = c + mu_0 - 1,
    M = gcd(2*mu_0 - 1, c),        mu_0 * w_U = kbar - 4.

Therefore the whole book is

| `kbar` | `(dp, dq, nu, M)` | arrival `w_U` | rows in §11a |
|---|---|---|---|
| 5 | `(6m-3, 10m-5, 5m-3, 2m-1)` | `1/m` | `m = 2,3,4,5` |
| 6 | `(4m-2, 6m-3, 3m-2, 2m-1)` | `2/m` | `m = 3,5,7,...,25` odd |
| 7 | `((10m-5)/3, (14m-7)/3, (7m-5)/3, ...)` | `3/m` | `m = 8` |

with `m = mu_0`. Block B of the script regenerates **all 17 rows, including
`nu` and `M`, from these three formulas** and continues them past the book:
`kbar=6, mu_0 = 27` gives `(106,159,79,53)`, `mu_0 = 41` gives
`(162,243,121,81)`. The record's own explanation of where the table stops is
consistent with this and identifies the true finiteness source:
"it TERMINATES at `mu_0 = 25` because the closure contains no state with
`w <= 2/27` at budget 5 — closure-forced, not a cap."

**Consequence for the endpoint question of CRITICAL 4.** The `td=7`
off-axis "book" is not a finite list that happened to come out at 17. It is
three infinite linear families intersected with the finite arrival
`w`-alphabet. Any endpoint object `B(td, entry)` defined as a *set of cells*
is therefore the wrong object; the right endpoint is
`(finite reduced-state set) x (semilinear nu-fibre)`. This is a concrete,
checkable answer to REDUCTION §5.1's "define the endpoint".

## 7. Quantifier audit — the six required questions

**(a) Can neutral moves change `M`, `w`, arrival eligibility, provenance, or
later merge equations outside a finite congruence quotient?**

| quantity | changed by a neutral move? | captured by a congruence in `nu`? |
|---|---|---|
| `w` | no (Theorem 3.4, `C = 0` case of (T)) | trivially |
| `den(w)` | no | trivially |
| `M` | yes, `M_F = gcd(l, nu+1)` | **yes**, `nu mod l` (Theorem 1) |
| arrival eligibility `mu \| M_H` | yes | **yes**: `mu \| l` and `nu == -1 (mod mu)` |
| `kbar` | yes, `kbar = w*(nu+1)`, unbounded | **no** — affine, not periodic |
| deck/root provenance | no: DS1(a)–(d) generalize verbatim to `l >= 2` (§2(b)), so segment vertices stay consecutive characteristic vertices of their own pole | n/a |
| case-I/II merge equations | **no**: `kbar_e` and `nu_e` are eliminated; only `w_e` survives (R2.1) | n/a |
| case-III merge equation | **yes and non-congruentially**: `kbar_G - X_G/mu_0 = kbar_e - rho_e = nu_e * w_e` | **no** |

So the proposal's phrase "quotient all zero-cost neutral moves by their
exact invariant data and congruence classes" is **correct for case-I/II and
false for case-III**. The repair is not to enlarge the congruence: by
Theorem 2 clause 4 the arriving `nu_e` at a case-III edge is *bounded*
(`nu_e <= mu_0 * num(w_e)`), so the correct quotient there is by a **finite
set of exact values**, not by residues. Equivalently: **a chain vertex spends
its free `nu` the moment it sends its edge into a 0-direction.** That
asymmetry between the two edge types is the sharpest quantifier finding of
this report and is invisible in the P0/P2 presentation, which prices the two
identically at `lambda = 0`.

One further genuine gap, orthogonal to `nu`: the whole calculus is
`i`-normalized, and the stage-R policy records that `n_e in N*` and `i`-sync
"are never used to kill". The quotient therefore drops `i`. That is
superset-safe (no false kills) but means **no statement here is a
realizability statement**: a finite family of reduced states is an upper
bound on what occurs, never a claim that any member occurs. Every clause
below inherits this rider, exactly as R4 does.

**(b) Products of unbounded variables leaving Presburger.** Exactly one,
and it is the transport ratio itself: `kbar = mu*w*(1+nu*s)/((mu-eps)+nu*C)`
(§4). Its degeneracy locus is `C = 0`. Secondary occurrences —
`M = gcd(dp,dq)` (a gcd, not Presburger) and `nu_e*w_e` in case III — are
both tamed: the first by Theorem 1 (`M` is a `nu mod |T|` function), the
second by Theorem 2 clause 4 (`nu_e` bounded), and `w_e` ranges over a
finite alphabet so `nu_e*w_e` is piecewise affine in `nu_e` anyway.

**(c) Finite path length vs finite state count.** These are *different*, and
only the second holds. Path length is provably unbounded: `SHEET6-DEPTH.md`
§2 R1 shows the segment depth is bounded by the Puiseux denominator
`kappa_i`, which "is NOT bounded by `(m, td)`". Neutral moves (`C = 0`,
`lambda = 0`) are always available from any state with `M >= 1`, so the
abstract transition system has infinite runs. What is finite is the reduced
state set (Theorem 3.5 + Theorem 3.4) and the family count (Theorem 2).

**(d) Does one positive-cost step admit an unbounded family whose later exact
cell equations need the full parameter?** Yes, and the answer splits:
the pure-(b) family (`eps >= 1`, `k = lex = 0`, `C = 0`, cost
`lambda >= ceil(l*w/eps) >= 1`) is unbounded in `nu` with successor
`(w, M) = (l*w/(l-eps), gcd(l-eps, nu+1))` depending only on `nu mod (l-eps)`
— residue class suffices. But if that vertex later supplies the 0-arrival of
a case-III merge, the full `nu` enters, and Theorem 2 clause 4 then forces
`nu <= mu_0*num(w)`, deleting all but finitely many members of the family.
**So the residue class does not suffice, and the parameter is finitely
determined when it does not.** The quotient must be taken jointly over the
configuration, not vertex-locally.

**(e) Does the `td=7` cap-free inversion generalize?** See §8.

**(f) Ranking-or-lasso vs budget quotient.** See §10.

## 8. The `td=7` inversion, and the first obstruction to generalizing it

The `td=7` inversion of `BOOK-OFFAXIS.md` §11a is cap-free because of a
four-link chain, and exactly one link is `td=7`-specific.

1. **Frozen partner.** Chain 1 is a `b = 1` pole with singleton `w`-alphabet
   `W(2) = {2}`, `mu = 1`, `lambda = 0` (MP5/MP8/DS3, §8 Step 1). This is a
   *rigid* handshake `X = kbar - 2`.
2. **Pin.** With (4b) this gives the one-parameter identity
   `kbar = 2*dq/(dq - dp)` — `kbar` is now a function of the cell alone.
3. **T1 floor.** `kbar in {3,4}` is T1-dead (§11 zero-chain law, dual
   certified) and `kbar <= 2` is impossible, so `kbar >= 5`.
4. **Inversion.** `c*(kbar-4) = 4*mu_0 - 2` with `c >= 1`, `kbar >= 5` gives
   `c <= 4*mu_0 - 2` and hence a finite integer `c`-window per `(mu_0,w_U)`,
   with `nu_G` determined. That is `(I5a)-(I5d)`, and it is why no cap is
   needed.

The same argument, run generally, bounds the `lex` parameter too: with a
0-arrival `mu_0`, one nonzero arrival `(mu,w) = (1,2)`, `k = 0`, `lex = L`,
the constraint `kbar >= 5` reads `2*(1+nu*(1+L)) >= 5*(nu*L - 1)`, i.e.
`nu*(3L-2) <= 2*nu + 7 - ...`, forcing `L <= 1`. That is exactly why every
one of the 17 promoted cells has `s = 2`.

> **First obstruction.** Link 1 fails as soon as no arriving chain has a
> singleton `w`-alphabet, i.e. at the first entry with **all** `b_i >= 2`.
> Then R2.1(ii) pins `kbar = (mu_a w_a - mu_b w_b)/(mu_a - mu_b)` only at
> **unequal** `mu`; at equal `(mu,w)` the pin degenerates to
> `X = mu*(kbar - w)`, one equation in two unknowns, and `kbar` is free —
> which is family 6a. Links 2–4 then have nothing to invert. The named
> first instances are `td = 8, m = 2, M = [2,2]` and `td = 13, m = 2`,
> `Lambda = (4,9), M = [2,3]` (`BOOK-OFFAXIS.md` §1, §1a).

What is *missing* is therefore precise and small: **an upper bound on `kbar`
at a merge with two off-axis arrivals**, equivalently (by (4b)) a lower bound
on `dq/dp` away from `1/mu`. Theorem 4 gives `kbar > w_e` and
`dq/dp <= kbar_min*b_e/mu_e`, both lower-side; the upper side is what the
`td=7` T1 floor supplied for free. This is a single, well-posed, desk-scale
lemma request, and it is the honest replacement for "the off-axis sector has
no completeness theorem".

## 9. Machine verification (desk, stdlib, seconds)

Script `/tmp/m2q_check.py`, exact `Fraction`/`int` arithmetic, no floats, no
repository engine imported, no cap anywhere. It checks my laws **against the
frozen published numbers**, so it is an independent replay of the record, not
a re-run of the record's own engines.

```
== A. T-law  M | |P - s*eps|  on the 17 promoted 11a cells ==
  (  9, 15,nu= 7,M= 3)@ 2  P=1 s=2 T=  -3 M||T|=True kbar=5
  ( 10, 15,nu= 7,M= 5)@ 3  P=1 s=2 T=  -5 M||T|=True kbar=6
  ( 15, 25,nu=12,M= 5)@ 3  P=1 s=2 T=  -5 M||T|=True kbar=5
  ( 18, 27,nu=13,M= 9)@ 5  P=1 s=2 T=  -9 M||T|=True kbar=6
  ( 21, 35,nu=17,M= 7)@ 4  P=1 s=2 T=  -7 M||T|=True kbar=5
  ( 25, 35,nu=17,M= 5)@ 8  P=1 s=2 T= -15 M||T|=True kbar=7
  ( 26, 39,nu=19,M=13)@ 7  P=1 s=2 T= -13 M||T|=True kbar=6
  ( 27, 45,nu=22,M= 9)@ 5  P=1 s=2 T=  -9 M||T|=True kbar=5
  ( 34, 51,nu=25,M=17)@ 9  P=1 s=2 T= -17 M||T|=True kbar=6
  ( 42, 63,nu=31,M=21)@11  P=1 s=2 T= -21 M||T|=True kbar=6
  ( 50, 75,nu=37,M=25)@13  P=1 s=2 T= -25 M||T|=True kbar=6
  ( 58, 87,nu=43,M=29)@15  P=1 s=2 T= -29 M||T|=True kbar=6
  ( 66, 99,nu=49,M=33)@17  P=1 s=2 T= -33 M||T|=True kbar=6
  ( 74,111,nu=55,M=37)@19  P=1 s=2 T= -37 M||T|=True kbar=6
  ( 82,123,nu=61,M=41)@21  P=1 s=2 T= -41 M||T|=True kbar=6
  ( 90,135,nu=67,M=45)@23  P=1 s=2 T= -45 M||T|=True kbar=6
  ( 98,147,nu=73,M=49)@25  P=1 s=2 T= -49 M||T|=True kbar=6
== B. closed-form semilinear families reproduce the whole book ==
  all 17 rows regenerated by kbar in {5,6,7}, c=(4mu0-2)/(kbar-4): True
    kbar=5 mu0= 2 -> (9, 15, 7, 3)
    kbar=6 mu0= 3 -> (10, 15, 7, 5)
    kbar=7 mu0= 8 -> (25, 35, 17, 5)
    kbar=6 mu0=25 -> (98, 147, 73, 49)
    kbar=6 mu0=27 -> (106, 159, 79, 53)
    kbar=6 mu0=41 -> (162, 243, 121, 81)
== C. free-nu dichotomy  C_e = mu_e*s - P ==
  (A) (21,15)  (dp,dq)=(21,15) kbar=5 w->2/3 M->3 T=3 C=1 M||T|=True
  (C) (20,16)  (dp,dq)=(20,16) kbar=4 w->3/4 M->4 T=4 C=2 M||T|=True
  eps (7,5)    (dp,dq)=(7,5) kbar=5 w->2 M->1 T=1 C=1 M||T|=True
  pure-b       (dp,dq)=(7,4) kbar=12 w->3 M->1 T=1 C=0 M||T|=True
  neutral      (dp,dq)=(18,10) kbar=15 w->3/2 M->2 T=2 C=0 M||T|=True
  P0 four-escape menu reproduced exactly (A,C,eps,pure-b): w,M as printed
== D. free-nu family: C=0 <=> k=lex=0 & equal mu & no 0-arrival ==
  chain vertices: C=0 iff k=lex=0  -> True (m_j<=l-1 from NE+searrow)
  equal-(mu,w) join r0=2: E=mu, kbar=w(2nu+1), w_child=2w, M=gcd(mu,2nu+1), lam=0
    mu=3 w=3 nu=  1: (dp,dq)=(6,3) kbar=9 w_child=6 M=3 T=2mu=6 lam=0
    mu=3 w=3 nu=  4: (dp,dq)=(24,9) kbar=27 w_child=6 M=3 T=2mu=6 lam=0
    mu=3 w=3 nu=  7: (dp,dq)=(42,15) kbar=45 w_child=6 M=3 T=2mu=6 lam=0
    mu=3 w=3 nu=100: (dp,dq)=(600,201) kbar=603 w_child=6 M=3 T=2mu=6 lam=0
    mu=5 w=2 nu= 12: (dp,dq)=(120,25) kbar=50 w_child=4 M=5 T=2mu=10 lam=0
== E. dq/dp bound from kbar in Z (kbar > w_e) ==
  dq/dp = kbar/(mu_e(kbar-w_e)) verified on 4 cells; bound <= ceil(w)*den(w)/mu

RESULT: ALL CHECKS PASS
```

Two honest readings of this transcript. (i) The `(C) (20,16)` chain step has
`kbar = 4`; the §11 T1 law is stated for the `td=7` merge-cell pin, so this
is *not* evidence that the `(C)` escape is T1-dead, and I do not use it as
such. (ii) Block B's continuation rows `(106,159,79,53)` and
`(162,243,121,81)` are family members, **not** claimed to be budget-fitting;
they exist to show the book's boundary is the arrival alphabet, nothing else.

## 10. Verdict on the proposed theorem: (b) strongest repaired statement

The proposed theorem said: *"quotient all zero-cost neutral moves by their
exact invariant data and congruence classes; every positive-cost move occurs
only finitely often; the P0 Diophantine bounds give finite branching except
for explicit free-`nu` families, and those families have a finite
divisor/congruence quotient; consequently the complete two-pole `M>=2`
transition set is a finite union of exact semilinear/parametric families
with a decidable total move classifier."*

Adjudication clause by clause:

| clause | verdict |
|---|---|
| quotient neutral moves by congruence classes | **REPAIR** — correct for case-I/II edges, **false at case-III** 0-edges, where the full `nu_e` enters; there the quotient is by a bounded set of exact values (Thm 2.4) |
| positive-cost moves occur finitely often | **CONFIRMED** — immediate from `sum lambda <= td-1-psi`, and sharpened: `lambda >= k + [free 0-root]` (Thm 3.1) |
| P0 bounds give finite branching except free-`nu` families | **REPAIR** — the correct criterion is not "P0's bound" but the exact dichotomy `C_e = mu_e*s - P` (Thm 2); P0's stated divisibility `E \| l*num(w)*T` is superseded by the correct `E_e <= M*mu_e*num(w_e)` (Thm 4a), whose proof is the `gcd(E,dq) \| M` step |
| free-`nu` families have a finite divisor/congruence quotient | **CONFIRMED with an exact characterisation** (Thm 2.1/2.3): free iff no 0-arrival, equal `mu_e`, `k = lex = 0`; then `w` is constant and `M` is `nu mod s*(mu-eps)` |
| the transition set is a finite union of semilinear families | **CONFIRMED for the chain layer; CONDITIONAL at merges** on an upper bound for `kbar` (§8) |
| ... is *finite* | **REFUTED if read as a finite set of cells** (§6a, §6b give exact infinite families); TRUE if read as a finite set of reduced states `(w,M)` with semilinear `nu`-fibres |
| decidable total move classifier | **CONFIRMED for the chain layer**, algorithm below; at merges, decidable relative to the same `kbar` bound |

### 10a. The repaired theorem

> **Theorem (budget quotient, chain layer — unconditional at the recorded
> tier).** Fix `td`, a normalized entry datum `E`, and the shared budget
> `B = td - 1 - psi`. In the charged grammar of §2 restricted to chain
> vertices (`r = 1`), define the reduced state `sigma = (w, M)`.
>
> 1. **(Normal form.)** Every vertex is coded by `(sigma; nu; kbar)` with
>    `kbar = w*nu*dq/(dq-1)` determined by `(w, nu, dq)`.
> 2. **(Finite reduced state set.)** The set of reduced states reachable
>    from `E` within budget `B` is finite and effectively bounded:
>    `M <= M_entry * max(m, 2^(m-1)) * 2^B` (Thm 3.5) and `num(w)` and
>    `den(w)` are bounded by the same induction (`den` is invariant at
>    `lambda = 0`, and multiplies by at most `E_e <= M*mu_e*num(w_e)` at each
>    of the `<= B` charged steps).
> 3. **(Semilinear fibres.)** Over each reduced state the admissible `nu`
>    form a finite union of arithmetic progressions if `C = 0`, and a finite
>    explicitly bounded set if `C != 0` (Thm 2).
> 4. **(Zero-cost quotient.)** Zero-cost moves are exactly `k = 0` with no
>    free 0-root; they fix `w` (neutral) or contract `num(w)` by `<= 2/3`
>    (resonant), and always satisfy `M_child | M_parent`. Hence `M` and
>    `num(w)` are simultaneous monovariants of the zero-cost sub-grammar, and
>    every increase of either costs `lambda >= 1`.
> 5. **(Decidability.)** The one-step successor relation is decidable and the
>    reachable-state set within budget `B` is computable by the algorithm of
>    §10b.
>
> **Merge layer (conditional).** The same conclusions hold at merges, with
> `M_G | sum_e mu_e + sum_j m_j - s*eps` (Thm 1) replacing subadditivity,
> **provided** an upper bound `kbar <= K(w_1,...,w_r; mu_1,...,mu_r)` is
> available. Such a bound exists at `td=7` (frozen partner + T1 floor, §8)
> and at every merge with unequal arrival multiplicities (R2.1(ii) pins
> `kbar` outright). It is **OPEN** at an equal-`(mu,w)` join, and §6a shows
> the conclusion genuinely fails there in the cell reading.

Riders, all inherited and none discharged: superset semantics
(alive != existent, R4); `lambda` values are lower bounds (P0 honesty rider
(i)); `n_e in N*` and `i`-sync are never used to kill; the `i`-normalization
means no realizability is asserted; the case-III handshake reading is subject
to the open CONJECTURE H5a fork, on which see §10c.

### 10b. Decision algorithm (total move classifier, chain layer)

Input: state `(w = a/b, M, nu, kbar)` and remaining budget `B'`.
Output: the complete successor set, as a finite list of
`(reduced state, nu-progression or nu-list, lambda)`.

```
for l | M:                                   # St 8.4
  for k = 0 .. B'                            # Thm 3.1: lambda >= k
    for each multiset {m_j}, j=1..k, 1 <= m_j <= l-1:      # NE+searrow
      for eps in {0} u {1..l-1}:             # free 0-root; eps=0 if lambda 0
        # 0-arrival branch handled separately: eps=mu_0, C_0>=1, nu<=mu_0*a
        for lex = 0 .. floor(M*l*a / l):     # Thm 4a: l*lex <= C <= E
          P = l + sum m_j ; s = 1+k+lex ; C = l*s - P ; T = P - s*eps
          if T == 0: continue                                    # law (R)
          if C == 0:                          # free family, Thm 2.1
             emit AP { nu : b*(l-eps) | l*a*(nu+1) } with
                 w' = l*a*s / (b*(l-eps)),  M' = gcd(l-eps, nu+1) mod |T|
          else:                               # bounded, Thm 2.2
             for nu = 2 .. (M_max*l*a + eps - l)/C:
                 dp,dq,E as in §2 ; require E>0, kbar=l*w*dq/E in Z,
                 dq == 1 mod nu, gcd(M',nu)=1, dp != mu_star*dq
                 emit (w' = l*w*s/E, M' = gcd(dp,dq))
          price lambda by (L); drop if lambda > B'
```

Termination of the enumeration is Theorem 2 plus `M' | T` (Theorem 1), which
bounds `M_max` before the loop is entered. Reachability closure then
iterates this over the `<= B` charged steps, taking the zero-cost closure
(finite by Theorem 3.4) between them. The output is by construction a finite
union of semilinear families — the object the proposal asked for.

### 10c. Ranking-or-lasso versus budget-quotient — which formulation is right

`sol56` Card 1 asks for *either* a bounded-below lexicographic ranking
function on every reachable SCC *or* an exact repeatable lasso. **Both horns
are already decided, and neither is informative.**

* A ranking function **cannot exist**. Neutral moves (`C = 0`, `k = eps = 0`,
  any `nu` in the progression `b | nu+1`, `l = M`) are available from every
  state and return the *same* reduced state `(w, M)` whenever
  `gcd(M, nu+1) = M`, i.e. `nu == -1 (mod M)`. That is an exact self-loop, so
  the transition system has infinite runs and no bounded-below ranking. This
  is not a discovery; it is `SHEET6-DEPTH.md` §2 R1 ("no bound on segment
  depth is available from `(m,td)`") restated in automaton language.
* The lasso the card would return is therefore **that same neutral loop**,
  already known, already harmless, and *not* a refutation of anything the
  campaign needs: the campaign never needed bounded delay along a chain, it
  needed a finite *menu*, which is DS4/depth-invariance.

Card 1's stated outcome semantics — "an exact replayed lasso or unbounded ray
refutes bounded delay within that grammar" — would therefore fire on a
trivial witness and be **misread as a negative result**. I recommend against
running Card 1 in its present form.

The budget-quotient formulation is the correct one, for a structural reason:
the grammar is not terminating and is not meant to be. Its finiteness is
finiteness *of the state quotient*, and the right technical frame is a
**well-structured / semilinear transition system with a `nu`-fibration**, not
a well-founded one. Grok's `OFFAXIS-COLON` card is closer to correct — its
"saturate with respect to the state denominator, split `D(denom)` vs
`V(denom)`" is, in this language, exactly the split by `C = 0` versus
`C != 0`: the proper open is the free-`nu` family (semilinear, `w` constant)
and the closed successor is the `C != 0` locus (bounded `nu`, strictly
smaller `num(w)` or `M`). §4 supplies the monovariant that card asked for and
the answer to its first outcome branch ("split works on the example"). Fable5
Card B's `LANDING-LEDGER` is complementary and unaffected: Theorem 1 and
Theorem 2 are exactly the two move-completeness facts such a ledger would
have to encode for the `M>=2` sector, and §7's table is the uncovered-class
list for that sector, at length four rather than "a few dozen".

**H5a fork.** Everything above is stable across the recorded readings of the
case-III pin, but the *content* differs: under the promoted E5/Q-value
reading `(I4)` uses `nu_G`, so `nu_U` is genuinely free and the congruence
quotient is complete at 0-edges; under the printed case-III equations as read
in `SHEET6-DEPTH.md` §5c (`kbar_G - X_G = kbar_e - rho_e = nu_e*w_e`) the
arriving `nu_e` enters and is pinned by Theorem 2.4. I do not adjudicate
H5a. Both readings yield a finite reduced-state set; they disagree on which
cells are realizable, which is precisely the conditionality §11a already
records.

## 11. Cheapest independently replayable discriminator, and the stop rule

**Discriminator D1 (already executed, §9).** Recompute `P`, `s`, `T` from the
published `(dp, dq, nu, M, mu_0)` of the 17 promoted §11a cells and the four
P0 escape cells, and test `T != 0`, `M | |T|`, and the `C`-dichotomy.
Cost: seconds, stdlib, no engine import, no cap. *Falsifier:* a single
published cell with `M` not dividing `P - s*eps` refutes Theorem 1 and with
it §§4–10. *Result:* 21/21 pass.

**Discriminator D2 (the next one to run, desk-scale, ~1 hour).** The exact
question that decides the merge layer, stated so that either answer is a
deliverable:

> Take the first entry with no `b = 1` pole — `td = 8, m = 2, M = [2,2]`
> from `BOOK-OFFAXIS.md` §1. Compute its two priced chain closures under P0.
> Ask: does there exist an equal-`(mu, w)` pair `(mu >= 2, w = a/b, b odd)`
> in the two closures, at joint cost `<= td - 1 - psi = 6 - psi`, with
> `gcd(mu, 2nu+1) >= 2` solvable? If yes, family 6a is instantiated at
> `td = 8` and the off-axis cell set is provably infinite at `td = 8`. If
> no, record *why* — that reason is the missing `kbar` bound in disguise.

This is one closure computation and one congruence test. It needs no new
machinery: `px5`'s closure and `feasible` already exist and are read-only.
I did not run it, because it requires the campaign's own priced closure
engine and the brief scoped me to desk mathematics on the frozen record.

**Stop rule.** Stop the budget-quotient line and hand back if any of:

1. D1 fails on any promoted cell (Theorem 1 dead; everything above falls).
2. D2 returns "no" *and* the reason is a printed statement rather than an
   accident of the `td=8` alphabet — then family 6a is not reachable, the
   cell reading may survive, and the correct next object is that printed
   statement, not this quotient.
3. A `kbar` upper bound at equal-`(mu,w)` joins is proved — then §10a's merge
   clause becomes unconditional and the work moves to the realizability
   (`i`-sync, `n_e`) layer, which this report does not touch.
4. Two rounds pass without either (2) or (3). Do **not** substitute a larger
   enumerator cap; by §6 the cell set is infinite and no cap can be
   completeness evidence.

## 12. What is and is not claimed

**Proved here, at the recorded trust tier, with no new hypothesis:**
Theorem 1 (`M | P - s*eps`, `T != 0`), Theorem 2 (the `C`-dichotomy and the
exact free-`nu` characterisation, including `nu <= mu_0*num(w_0)` at every
case-III 0-arrival), Theorem 3 (zero-cost characterisation; `M` and `num(w)`
monovariants; the effective `M <= M_entry*max(m,2^(m-1))*2^B` bound),
Theorem 4 (`E_e <= M*mu_e*num(w_e)`, `kbar > w_e`, the `dq/dp` identity), the
closed-form regeneration of the entire promoted §11a book as three linear
families, and the two infinite families of §6.

**Repaired, not proved:** the proposed theorem, in the form of §10a.

**Explicitly not claimed:** JC2; full landing; `G2-BD`; `G2-PSC`; any finite
book; that any state or cell described here is *realized* by an absolute
`(f,g)` (the `i`-normalization and the untracked `n_e`/`i`-sync forbid it);
any restoration of the `td = 11` or `td = 13` panels; any adjudication of
CONJECTURE H5a, of the `U_7C` sub-book, or of the P-value reading; any claim
about `jc2-lean`, which was not accessed.

**Corrections offered to the record** (each falsifiable by D1):
`BOOK-OFFAXIS.md` §10 P5's "reachable states can have unbounded numerator and
`M`" is too strong — at fixed budget both are effectively bounded (Thm 3.5);
R2.2(D)'s open rider on subadditivity when `dq < dp` is discharged by
Theorem 1; P0's finiteness relation `E | l*num(w)*T` should be
`E_e <= M*mu_e*num(w_e)` with the `gcd(E,dq) | M` proof; and §11a's
17-row table is three linear families whose truncation point is a statement
about the arrival `w`-alphabet, not about cells.

---

*Report body ends. Self-hash below covers everything above this line.*

report_body_sha256 = b161421ccb04a62307b87be4a60f130ded64fe53228bd600c960f2c502632283
(sha256 of this file up to and including the line "*Report body ends...*", i.e. of the first 43203 bytes)
