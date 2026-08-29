# Adversarial falsifier — cap-free `M>=2` symbolic quotient

Round tag: `20260829`  
Lane: Grok 4.6, independent of peer `20260829T0002Z` answers  
Charged scope: fixed `td`, fixed entry, fixed numerical `lambda` budget `B`  
Grammar: off-axis / post-jump `M>=2` as priced by `BOOK-OFFAXIS.md` §10 P0–P5, with R1.0–R1.2, R2, P1 `psi`, and the `M=1` comparison object from `SHEET6-DEPTH.md`  
Proposed object under test: a finite exact quotient of that grammar by `(w,M)` together with finitely many congruence/divisor fields, as the cap-free state theorem named in `ladder/REDUCTION.md` §5.2 / Critical 5–6 and as the common shape of Sol56 Card 1 (`M2-RANK-OR-LASSO`) and Grok46 Card 2 (`OFFAXIS-COLON`)

Read-only inputs (exactly these): `ladder/REDUCTION.md` Critical 4–7 and §5.2; `ladder/BOOK-OFFAXIS.md` current P0–P5 and later superseding §11/§11a; `ladder/SHEET6-DEPTH.md`; `ladder/SHEET6-MULTIPOLE.md`; `xmodel/ideation-20260829T0002Z-sol56.md` Card 1; `xmodel/ideation-20260829T0002Z-grok46.md` Card 2. No other ideation body, no `jc2-lean`, no web, no AWS, no CAS, no canonical edit.

No landing, `RPMC(C)`, type ceiling, or JC2 inference is drawn.

---

## Verdict

**`REPAIRABLE`**

The as-stated finite exact quotient by `(w,M)` plus a partner-independent handful of residue/divisor flags is false at charged scope. The Avenue-1 colon transplant is ill-typed and vacuous in this grammar. There is no genuine failure of finite symbolic representation: the only infinities at fixed `(td, entry, B)` are one-parameter families (chiefly last-vertex `nu`, plus a scale that the filed engines never use to kill). Those families are not a product of two free unbounded parameters in the i-normalized P0–P5 arithmetic.

A proof-producing quotient exists after a finite, named enlargement of the record and three lemmas. It is a finite set of symbolic classes, some of which are infinite arithmetic progressions with uniform live/dead verdicts, together with a finite table of special `nu`. It is not a colon dichotomy, and it is not `(w,M)` alone.

---

## 0. What was proposed, and the charged grammar

`REDUCTION.md` Critical 5 records that for any `b>=2` entry the generic grid has no completeness certificate: at a fixed budget the solver sees unbounded numerator and `M`, and its proved loop bounds scale with those quantities. Critical 6 records that even the all-`b=1` local book omits a resonant jump emitting `M>=2`, a subsequent `M>=2` chain, and a later all-`mu>=2` merge. Section 5.2 asks for an invariant, monovariant, or proof-producing finite automaton for exactly those segments. Budget alone is declared insufficient because zero/low-cost escapes exist.

Two ideation cards name the candidate repairs.

- Sol56 Card 1: a Presburger/semilinear abstraction of one omitted two-pole post-jump `M>=2` SCC, with ranking or exact lasso replay. A spurious lasso is to be repaired by adding one missing residue/root/deck or divisibility field, at most twice.
- Grok46 Card 2: saturate with respect to the state denominator or `M`-content, split `D(denom)` versus `V(denom)`, bound the proper open by the Proposition 4.2 terminal-degree formula, and recurse on a strictly simpler closed successor.

The common proposed quotient, as a finite exact state theorem, is therefore:

> after fixing `td`, entry, and a numerical budget `B >= Sigma lambda`, every reachable chain frame is equivalent, for exact legality and for terminal/cell verdicts, to a record `(w, M)` plus finitely many congruence and divisor flags.

The P0 grammar actually used is as follows. At a chain vertex with arrival multiplicity `l | M_parent` (Statement 8.4),

```text
p = ⊖ eta^eps (eta^nu - c^nu)^l Π_j (eta^nu - d_j^nu)^{m_j},
q = ⊖ eta · (simple orbits),
E := l·dq - dp > 0,
kbar_F = l·w_G·dq / E    (integer at nu >= 2),
w_F = l·w_G·(dq-1) / (nu E),
M_F = gcd(dp, dq),
lambda_F >= Σ_j max(1, ceil(X_F/m_j - kbar_F))
          + [eps >= 1]·max(1, ceil((X_F/eps - kbar_F)/nu)).
```

Clean/neutral steps (`eps = 0`, `k = 0`) cost `0` and include Statement 9.6(v). Extra-present steps have `E | l·num(w_G)·T` with `T >= 1`, hence a finite Diophantine menu per `(w, l)`. Pure-`(b)` steps (`k = lex = Sm = 0`, `1 <= eps <= l-1`) have free `nu`, collapse to `w_F = l·w_G/(l-eps)` and `M_F = gcd(l-eps, nu+1) | l-eps`, and cost `lambda >= ceil(l·w_G/eps) >= 1`. Every non-clean step costs at least `1`, so `B` bounds the number of non-clean steps. Shared budget is Statement 9.4(25) with `psi = ceil(1/(1-w_G)) - 1` at the trunk (P1); both chains, merges, and the trunk share one budget.

R1.1–R1.2 give the clean `n=1` law used below. For `n_F = 1`,

```text
(dp, dq) = (l nu, nu+1),     Delta = 1,
w_F = w_G,                   M_F = gcd(l, nu+1),
kbar_F = w_G · (nu_F + 1),   rho_F = w_G.
```

Parent `nu` cancels in `kbar_F`. Staying at the same `M` requires `l = M` and `M | (nu+1)`, i.e. `nu ≡ -1 (mod M)`. For the live `td=7` chain-2 start this is all odd `nu`.

---

## 1. Attack A — zero-cost lasso versus later merge admissibility

### 1.1 The infinite zero-cost ray, exactly

Take the unique L6-surviving `td=7` off-axis entry (`BOOK-OFFAXIS.md` §1a, §10 P3):

```text
type (2,3),  Lambda = (3,4),
poles (a,b,nu) = (1,1,2) ⊕ (1,2,3),
M = (1,2),   w0 = (2, 3/2).
```

Chain 2 starts at `(w, M, nu) = (3/2, 2, 3)`. Zero-cost `n=1` steps with `l=2` (the only `l | 2` that preserves `M`) produce the family

```text
S(t):   nu = 2t+1  (t >= 1),   (dp, dq) = (2 nu, nu+1),
        M = gcd(2, nu+1) = 2,   w = 3/2,
        kbar = (3/2)(nu+1) = 3(t+1).
```

Check: `w = (kbar - rho)/nu = (3t+3 - 3/2)/(2t+1) = 3(2t+1)/(2(2t+1)) = 3/2`. Cost `0`. Statement 9.6(v) is this family at `j`-scale (section 3).

Write `S3 := S(1)` (`nu=3`, the entry) and `S5 := S(2)` (`nu=5`). Both have the same proposed record `(w, M) = (3/2, 2)` and the same parity `nu ≡ 1 (mod 2)`, which is the unique congruence forced by staying at `M=2`.

From `S(t)` one may step to `S(t')` at cost `0` for any `t' >= 1`. In the projected `(w, M, nu)` graph this is a zero-cost clique, hence a lasso. It is not a configuration cycle: each step is a new characteristic vertex, and full pattern degree strictly multiplies by `nu_F >= 2` (section 4.2). Card 1 therefore classifies a `(w,M,nu)`-cycle as a spurious lasso whose missing field is `deg p` (or depth). The configuration object is an unbounded zero-cost ray, the same shape as the `M=1` `n=1` ray that `SHEET6-DEPTH.md` already knows.

### 1.2 The same class, two exact merge legalities

Keep chain 1 frozen at `(mu, w, M) = (1, 2, 1)` (P3). Arrange chain 2 at `0` with `mu0 = 2` (case III; R2.1 / DEPTH §5c). Handshakes:

```text
X = mu1 (kbar - w1) = kbar - 2,
X = mu0 (kbar - nu2 w2) = 2(kbar - nu2 · 3/2).
```

Eliminating `X` gives the exact pin

```text
kbar = 3 nu2 - 2,     X = 3 nu2 - 4.
```

`X > 0` holds for every `t >= 1`. Because `X = kbar - 2 > 0` one has `dq > dp`, so R2.2(S) forces `k = 0`. The P3 ZCH shape is then

```text
dp = nu_G + 2,     dq = (l+1) nu_G + 1,     X / kbar = dp / dq.
```

**At `S3` (`nu2 = 3`):** `kbar = 7`, `X = 5`,

```text
5/7 = (nu_G + 2) / ((l+1) nu_G + 1)
=>  nu_G (5l - 2) = 9.
```

`l = 1` gives `nu_G = 3`, cell `(dp, dq) = (5, 7)`, `M_G = gcd(5, 7) = 1`. Well-formed, then MP2-dead on an interior trunk. (This is §8 Step 3's `A = 7` cell, reproduced without a cap.)

**At `S5` (`nu2 = 5`):** `kbar = 13`, `X = 11`,

```text
11/13 = (nu_G + 2) / ((l+1) nu_G + 1)
=>  nu_G (11l - 2) = 15.
```

No integer `l >= 1` works (`l=1` gives `9 nu_G = 15`; `l=2` gives `20 nu_G = 15`; `l=3` gives `31 nu_G = 15`). No cell.

Same proposed quotient record, different exact legality of a case-III configuration. This is a counterfamily to `(w, M)` and to `(w, M, nu mod 2)`. It is not yet a live/dead split of an ALIVE cell: both outcomes are dead. Critical 4 nonetheless requires a total configuration-to-record map that preserves every cell kill, including MP2. `S3` produces an MP2-killable cell that `S5` does not produce.

The partner-specific divisor that separates them is

```text
for l = 1:   nu_G (5l - 2) = 9    is the S3 line;
generally,   (A+2) / (l(A-2)-2) in N*,   A = 3 nu2 - 2.
```

The `t=1` specialization `A-4 | 6` in §8 is the divisor field `(nu2 - 2) | 2`. That flag is not a field of the single-chain record: the constants `3` and `2` are chain 1's frozen `w=2` and `mu=1`. A finite list of partner-independent congruences, fixed before the other chain is known, cannot pre-split every later case-III condition.

### 1.3 Live cells on a later AP are uniform, and that is the distinction

After the priced `(A)`-step `(21, 15)` (`lambda >= 2`, `w |-> 2/3`, `M |-> 3`, `nu = 7`; P0 / St 9.6(iii)), neutrals that stay at `M=3` are `l=3`, `nu ≡ 2 (mod 3)`. Section 11a records the live cell `(10, 15, 7, 5)@3` with E5 arrival `w_U = 2/3` and arrival vertices “direct `(4,3),(7,3)` and neutral `nu ≡ 2 (mod 3)`”. The E5 pin

```text
w_U^req = (kbar (mu0 - 1) + 2) / (mu0 nu_G) = (6·2 + 2) / (3·7) = 2/3
```

is independent of arrival `nu_U`. The merge-edge `n_e = nu_H kbar_G - kbar_H` on a neutral parent at `w=2/3` is affine in `nu_H` and lies in `N*` on the whole AP `nu ≡ 2 (mod 3)` (same arithmetic as §4.1 below). So the live cell is constant on that AP.

This is an infinite family represented by one parameter, with uniform live verdict. It is not a failure of finite symbolic representation. Attack A therefore kills the unrefined quotient and does not kill a quotient that splits finite special `nu` from generic APs.

---

## 2. Attack B — unbounded data at one fixed budget

P5 asserts that already at budget `td-2 >= 5` the `(3/2, 2)` closure contains post-jump states of unbounded numerator and `M` (70 states up to `M=25` quoted). That sentence mixes three different infinities. At charged scope they separate.

### 2.1 Reduced `w` and `M` are finite at fixed `B`

Non-clean steps number at most `B`. Extra-present P0(i) has `E | l·num(w)·T` and each extra costs at least one lambda unit, so `k + [eps >= 1] <= B`. Arrival `l | M_parent` and extra multiplicities `m_j <= l-1`, hence `T = Sm + l - eps(1+k+lex)` is bounded by a function of the current `M` and remaining budget. Then `M_F | E` (because `gcd(l·dq - E, dq) = gcd(E, dq)`), so `M_F <= E <= l·num(w)·T`.

Pure-`(b)` cannot raise `M`: `M_F | (l-eps) < l <= M_parent`. It expands `w` by `l/(l-eps)` at cost `>= ceil(l w / eps)`, so remaining budget bounds `w` from above. Clean `n >= 2` contracts `num(w)` (`Delta | num(w)`, `Delta >= 3`).

Bootstrap from the entry `(w0, M0=b)`, which is finite at fixed entry: after at most `B` non-clean steps the set of reduced pairs `(w, M)` is finite. For the `(3/2, 2)` start at `B=5` an explicit crude bound is enough to see finiteness; the engine figure `M=25` is an observed maximum under its own caps, not a proof that `M` is infinite.

P5's “unbounded numerator and `M`” is therefore false for reduced `w` and for `M` at fixed `(td, entry, B)`. What P5 correctly saw is that an un-quotiented enumerator whose loop bounds scale with `num(w)·M_G` has no completeness certificate, because those bounds do not cap `nu`.

### 2.2 What is actually unbounded at fixed `B`

- **Last-vertex `nu`.** Zero-cost `n=1` and positive-cost pure-`(b)` both have free `nu` in an arithmetic progression determined by the current `M` (or by `l-eps`). Unbounded.
- **`kbar`, `dp`, `dq` of a neutral frame.** On `S(t)`, `kbar = 3(t+1)` is unbounded. This is the “unbounded numerator” that P5 is actually looking at: the numerator of `kbar`, not of reduced `w`.
- **Full pattern degree.** Each `n=1` step multiplies `deg p` by `nu_F >= 2`. Unbounded. This is the M=1 phenomenon of `SHEET6-DEPTH.md` §2 R1 (`kappa_i` not bounded by `(m, td)`), now at `M>=2`.
- **Statement 9.6(v) scale `j`.** The printed `lambda=0` family is `Q = ((6s+3)j, (4s+2)j, 2s+1, 2, 3s+3)`, `w ≡ 3/2`. Two parameters `(s, j)`. The `s`-axis is the odd-`nu` AP of §1.1. The `j`-axis is the i-normalized scale; `BOOK-OFFAXIS.md` R4 treats i-sync as always solvable and never uses it to kill. Unbounded, but invisible to R2.1 handshakes (`kbar = 3s+3` does not contain `j`; `rho = 3/2` cancels `j`).
- **Arrival data.** P2 permits every neutral `nu ≡ -1 (mod mu)` with `mu | M_H`, plus finitely many stored dirty landings and the entry. The neutral clause is an infinite AP.
- **Root/deck orbit size.** Pattern `p_red = ⊖ (eta^nu - c^nu)^l` has orbit size `nu`, hence unbounded on the ray. No P0–P5 kill uses the orbit as a second independent parameter once `nu` is kept.

None of these is a second free unbounded *reduced* `(w, M)` coordinate at fixed `B`.

### 2.3 Post-jump is the same infinity

A first resonant jump on an `M=1` ancestry has a finite cell menu per `w` (`SHEET6-DEPTH.md` DS4). The emitted `(w_child, M_G)` is one of finitely many starts. The suffix is the P0 grammar of §0. No new unbounded sort appears after the jump. The Critical 6 hole is this same `nu` / degree ray, not a second mechanism.

---

## 3. Attack C — a product of two unbounded parameters

Presburger/semilinear abstractions die when a load-bearing predicate contains a product of two variable integers. The candidates at charged scope all reduce or cancel.

**Case I/II handshake (R2.1).** `X_G = mu_e (kbar_G - w_e)` does not contain arrival `nu`. Equal-`mu` equal-`w` joins share `w` and leave `kbar_G` free in a finite window (`w < kbar <= (r+1)w` on the `M=1` model; the same window shape applies off-axis once `w` is from a finite set). No product.

**Case III.** `X_G = mu0 (kbar_G - nu_e w_e)` is affine in the single arrival `nu_e`. The second chain contributes a fixed `(w, mu)` from a finite set, or, if it also carries a free `nu`, at most one of the two arrivals can occupy the unique 0-direction. P3 already bounds that `nu_e` per `(mu0, w2)` for class C (`kbar >= 5 => c <= (4 mu0 - 2)/(kbar - 4)`). ZCH determines `nu_e = w_other / w_0chain` when that ratio is an integer `>= 2` (`SHEET6-DEPTH.md` §5c). The value is taken from a finite `W` set, hence bounded. No product of two free `nu`.

**Dirty `n_e` from a neutral parent.** For a fixed child cell, parent `rho = w`, `kbar_p = w(nu_p+1)`,

```text
n = (dp kbar_p - l dq w) / E = (w dp / E) nu_p - w.
```

Affine in `nu_p`. For the `(A)`-cell `(21, 15)` from `(3/2, 2)`:

```text
E = 9,   n = (7 nu_p - 3)/2.
```

For `nu_p = 2t+1`, `n = 7t + 2 in N*` for every `t >= 1`. The whole AP admits `(A)`. Uniform, not a product.

**`M_F = gcd(l, n nu + 1)`.** Clean `n=1` gives `gcd(l, nu+1)` with `l | M` bounded. Clean `n >= 2` has `Delta | num(w)` with `num(w)` bounded, so `n` and `nu` are bounded. Finite casework, not a variable product.

**Un-normalized `Q`-datum.** Statement 9.6(v) has `D = 3 nu j` and `deg p = 2 nu j`. If a consumer stored `D`, `nu`, and `j` as independent Presburger sorts, the identity `D = 3 nu j` would leave Presburger arithmetic. The i-normalized grammar does not: `w` and `kbar` eliminate `j`, and R4 never kills on i-sync. Reintroducing `D` as a third sort is a scope error, not a theorem of P0–P5.

**Two-pole equal-`w` at `td=8`.** The entry `td=8`, `m=2`, `M=[2,2]`, type `(2,3)`, both poles `(a,b,nu)=(1,2,3)` has `Lambda = ab alpha beta / nu = 4+4=8` and both `w0 = 3/2`. Both chains may run the odd-`nu` ray independently. Equal-`mu` equal-`w` non-0 joins are independent of both `nu` (R2.1(i)). Case III on one edge determines at most one `nu` as a ratio of the two `w` values, here `nu_0 = 1`, which is illegal. No product.

Attack C fails at charged scope. The Sol56 Card 1 abstraction is not blocked by multiplication. What Card 1 must not do is treat un-normalized `(D, nu, j)` as three free sorts.

---

## 4. Attack D — two states, one record, different verdicts

Section 1.2 is the exact pair: `S3` versus `S5`, record `(3/2, 2, nu odd)`, different case-III well-formedness.

A second, weaker pair is N1-style primitivity at a chain vertex, which is *not* required (the entry itself has `nu=3`, `kbar=6`, `gcd(6,3)=3`, and is L6-legal by `gcd(a(alpha+beta), nu)=gcd(5,3)=1`). If a consumer wrongly copied the §11a merge test `gcd(kbar, nu_G)=1` onto chain vertices, then

```text
gcd(kbar, nu) = gcd(3(t+1), 2t+1)  divides  3,
equals 3  iff  nu ≡ 3 (mod 6).
```

`S3` would fail and `S5` would pass, again same `(w,M, nu mod 2)`. That filter is not in the chain grammar. It is recorded only so it is not “discovered” later as a new invariant.

For ALIVE §11a cells the APs that actually arrive (`nu ≡ 1 (mod 2)` at `w=1/2`, `nu ≡ 2 (mod 3)` at `w=2/3`) are uniform. The unrefined quotient therefore fails exact configuration legality and does not, on the filed `td=7` live book, fail the coarser live/dead projection. A proof-producing map in the sense of Critical 4 cannot use that coarser projection.

---

## 5. Attack E — Avenue-1 colon is ill-typed, and Card 2's own discriminator fires

Grok46 Card 2 transplants the colon dichotomy that closed TRIPLE03 / TRIPLE02 node 1: after two-way equality, searching for `NF_I(Delta^k)=0` cannot succeed on a proper open, so one splits `D(Delta)` from the closed successor `V(I, Delta)`. The proposed off-axis translation is: saturate with respect to the denominator of the unbounded numerator (or the `M`-content), bound `D(denom)` by Proposition 4.2's terminal-degree formula, and have `V(denom)` drop `M` or the numerator valuation.

This is not a well-typed map of tools.

1. **No ideal.** Avenue 1 colon is an operation on a polynomial ideal `I subset Q[x_i]` with an explicit polynomial `Delta`. The P0 state space is a Diophantine subset of integer tuples `(nu, l, n, eps, k, w=p/q, M, kbar, lambda_spent, ...)`. There is no `I` and no `Delta` in that ring.

2. **`V(den(w))` is empty.** Reduced `w = num/den` has `den in N*`. The zero-locus of the denominator, in any reading copied from `Spec` of a polynomial ring, is `{den = 0} = emptyset`. Then `D(den)` is the entire state space and the closed successor is vacuous. The split does no work. The same emptiness holds for `V(M)`: `M = gcd(dp, dq) >= 1` at every legal vertex.

3. **`V(E)` is the illegal wall, not a simpler grammar.** The searrow gap `E = l dq - dp > 0` is the nearest analogue of a vanishing denominator in the transport formulae. `E = 0` is `dp = l·dq`, forbidden by the root-mult law R1.0/R2.2(R). The closed successor is the illegal locus. Recursing on it is not a legal instance of smaller `M`.

4. **Proposition 4.2 does not bound `M` on the open.** Card 2's discriminator asks whether `D(denom)` has a finite `M` bound by the unique terminal `(1,0,c)` shift and terminal degree `(mu_F-1) deg p_F + 1`. On the zero-cost ray, `deg p_F` multiplies by `nu_F` at every step, so the terminal degree is unbounded in `nu`. It supplies no `M` bound. Independently, Statement 9.6(v) already exhibits unbounded `nu` at `lambda=0` with `M` fixed and equal to `2`. The hoped bound is false.

5. **`M` is not a monovariant.** Dirty vertices raise `M` (the `(A)`-cell is `M: 2 -> 3`; P4's trunk example `(35,15)` is `M: 3 -> 5`). A closed successor defined by “`M` drops” is not closed under P0. This is the same reason R1.5's `W_off` finiteness was retracted and replaced by budget-boundedness.

Card 2's own stop conditions now fire on the smallest `s=2`, both-`b_i>=2` example it names. For `td=8`, `M=[2,2]`, both chains sit at `(w, M)=(3/2, 2)` with `den(w)=2` constantly on the odd-`nu` ray of §1.1. `V(den)` is empty; `D(den)` still has unbounded `nu`; `M` does not drop. “Proper open still unbounded” and “closed successor not simpler” are both true. The transplant stops. This is a method failure, not a failure of the `(w, M)` arithmetic.

The completeness *shape* that Card 2 correctly imported from Avenue 1 is only this slogan: do not raise a cap on an unbounded coordinate. The repair is a quotient with a ranking or a uniform-AP lemma, which is Card 1, not a colon.

---

## 6. What survives, and the minimum extra fields

### 6.1 Infinite families versus failed representation

| Family | Parameters | Load-bearing in P0–P5? | Finite symbolic form |
|---|---|---|---|
| Neutral `n=1` at fixed `(w,M)` | one: `nu ≡ -1 (mod M)` | last `nu` in case III; otherwise no | one AP, plus a finite special-`nu` table |
| Pure-`(b)` | `nu` free, `M' | (l-eps)` | lands in finitely many `(w', M')` APs | finite union of APs mod `l-eps` |
| Statement 9.6(v) `(s,j)` | two | `s` is the odd-`nu` AP; `j` cancelled by i-normalization and unused by R4 | one AP after dropping `j` |
| `(2,2t)` class-A tail | one: `t >= 2` | `w_tr = 2 + 1/(t-1) >= 2`, cannot terminate; P4 prices it out | one explicit 1-parameter cell family |
| Reduced `(w,M)` at fixed `B` | none | finite | finite set |
| Product `nu · j` in `D` | two, if `D` is kept | not in the i-normalized grammar | do not reintroduce `D` |

The S3/S5 pair is coarseness of the record, not an unrepresentable family.

### 6.2 Minimum additional fields

A proof-producing record at charged scope, for one chain in a fixed entry, is

```text
R = ( w, M, B_rem, l, shape, src, nu_tag )
```

where:

- `(w, M)` is a reduced pair from the finite P0-closure at budget `B` (lemma L1);
- `B_rem` is remaining numerical slack before a terminal `psi` is chosen; configuration-level sum is P1's shared `Sigma lambda <= td - 1 - psi`, so `B_rem` is a configuration coordinate, not a private chain coordinate;
- `l | M` is the current arrival multiplicity;
- `shape` is the finite P0 type of the last non-neutral step (`clean n=1`, `clean n>=2`, extra-present `(k, eps, m_j)`, or pure-`(b)`), with `k + [eps>=1] <= B`;
- `src in {entry, dirty-landing, neutral}` distinguishes P2's three arrival clauses; the dirty-landing list is finite by P0(i);
- `nu_tag` is either a specific integer from a finite set `N_special(w,M)` or a residue class modulo `L(w,M)`, where `L` is the lcm of `M`, of `l-eps` over legal pure-`(b)`, and of the finitely many `E` of the extra-present menu from `(w,l)`.

The configuration record is a tuple of such chain records, a merge shape `(r, mu_*, eps, k, l_ex, nu_G, dp, dq, M_G, kbar_G)`, a trunk state, and the single shared `(Sigma lambda, psi)`.

Do not include un-normalized `D` or the 9.6(v) scale `j` as Presburger sorts. Do include `deg p` or depth only if a ranking function on the abstract graph is required (to kill the spurious `(w,M,nu)`-clique of §1.1). Merge predicates themselves do not need it: R4 and the i-cancellation in R1.2 already make case I/II independent of history.

### 6.3 Minimum lemmas

**L1 (finite reduced skeleton).** At fixed `(td, entry, B)`, the reachable reduced pairs `(w, M)` are finite. Proof: §2.1 bootstrap from P0(i), pure-`(b)` descent of `M`, budget-bound on expansions, and contraction of clean resonance.

**L2 (finite one-step menu, affine in parent `nu`).** From a fixed `(w, l)`, extra-present landings form a finite set of child cells, independent of parent `nu` except that `n_e = (w dp / E) nu_p - w` lies in `N*`, which is a congruence on `nu_p` modulo a divisor of `E · den(w)`. Pure-`(b)` lands on finitely many APs. Clean `n=1` preserves `(w, M)` on `nu ≡ -1 (mod M)` (or drops `M` onto finitely many divisors).

**L3 (uniformity on generic APs).** There is a bound `nu_* = nu_*(td, entry, B, W)` such that for every partner record in the finite skeleton and every `nu > nu_*` in a fixed residue class mod `L(w,M)`:

- case I/II legality and the merged-child `(w, M, cell-menu)` are constant (R2.1 independent of `nu`; DS4-style window finite per `w`);
- case III is uniformly empty (P3 class-C bound; ZCH/`nu_e = w_other/w` is a specific integer `<= max W / min W`, hence not generic-large);
- every extra-present P0 child that is legal for one such `nu` is legal for all, or illegal for all, by L2.

The finite set `N_special` is the dirty-landing `nu`s together with every case-III/ZCH `nu` that L3 does not call generic. On `td=7` against frozen chain 1 this set contains `nu=3` (the MP2-dead `(5,7)` cell) and does not contain `nu=5`.

Optional ranking lemma, only for Card 1's lasso search: `deg p` (or chain depth) strictly increases on every `n=1` step with `nu>=2`, so the only loops in a record that includes `deg p` have positive cost and are budget-bounded.

These lemmas are local to the priced grammar. They do not restore MP8 equality, do not bound `td`, and do not land a configuration in the Critical 4 sense beyond the `M>=2` suffix/off-axis fragment.

---

## 7. One concrete exact small-sector test

Sector: `td=7`, the unique off-axis entry of §1.1, budget `B=5` (`td-2`; P1 with `psi >= 1`). Chain 1 frozen. This is P3/P4/§11a's sector, already cap-free on merge `nu_G` under E5.

**Test T.** Form the candidate quotient of chain 2 at `B=5` by L1–L3. Check three exact identities, all by hand, no cap.

1. **Skeleton finiteness.** Every reduced `(w, M)` reachable from `(3/2, 2)` at `lambda <= 5` occurs in the P0 one-step menu of P0's displayed four escapes plus their budget-bounded iterates:
   - `(A) (21,15)`: `w: 3/2 -> 2/3`, `M: 2 -> 3`, `lambda >= 2`;
   - `(C) (20,16)`: `w -> 3/4`, `M -> 4`, `lambda >= 2`;
   - `eps (7,5)`: `w -> 2`, `M -> 1`, `lambda >= 3`;
   - pure-`(b)`: `w -> 3`, `M -> 1`, `lambda >= 3`.
   The `(A)`-then-`(35,15)` trunk example (`w: 4/3 -> 4/5`, `M: 3 -> 5`) is the only further M-increasing unit quoted at this budget. If any reduced pair outside this finite list appears, L1 is false.

2. **Generic-AP uniformity for live cells.** On `(w, M)=(2/3, 3)`, residue `nu ≡ 2 (mod 3)`, every such `nu` (not just `nu=7`) must realize the same E5 number `w_U^req = 2/3` for cell `(10,15,7,5)@3` and the same `n_e in N*` verdict. Already checked for the merge pin; the remaining check is that no hidden `nu_G`-independent kill (N1 is on `nu_G=7`, odd, `kbar=6`, `gcd(6,7)=1`, passes uniformly) splits the AP. If some large `nu ≡ 2 (mod 3)` is T1-dead or budget-dead while `nu=7` is live, L3 is false.

3. **Special-`nu` table is finite and necessary.** `S3` produces the well-formed MP2-dead cell `(5,7)` of §1.2; `S5` produces none. Any quotient that identifies `S3` with `S5` fails Critical-4 provenance for that MP2 kill. Any quotient that stores every odd `nu` as its own class is an enumerator cap, not a quotient. The test passes iff `N_special` contains `3` (and any other case-III `nu` with `nu_G (5l-2)`-type solutions at this frozen partner) and L3 calls all larger odd `nu` uniformly case-III-empty, which the denominator `l(A-2)-2 ~ 6l t` versus numerator `A+2 ~ 6t` already gives: `nu_G ~ 1/l < 2` for large `t`.

A pass of T is not a `td=7` closure and not a full-configuration book. It is the smallest exact check that the repaired quotient is neither too coarse (T3) nor an infinite enumeration in disguise (T2).

---

## 8. Scope firewall

This report does not assert: a landing theorem; a completeness certificate for any `td`; restoration of the prime-`td` exclusion; correctness of the 17-cell §11a list beyond the arithmetic cited; coefficient/T1 solvability; `G2-BD`; `RPMC(C)`; a cofinal `td` bound; or any JC2 consequence. It does not promote Sol56 Card 1's ranking search, which remains unexecuted. It does reject Grok46 Card 2 as a method for this grammar.

P5's generic `0 DEAD / 0 ALIVE / 2691 OPEN` remains the honest grid-level statement until L1–L3 are proved and the quotient is compiled. The obstruction named in `REDUCTION.md` §5.2 is not “`M` is infinite at fixed budget”. It is “the un-quotiented `nu`-ray has no proved uniformity lemma”. That is a different, smaller theorem.

---

## 9. Replay

- Files read: exactly the six paths in the header.
- Files written: this path only.
- Compute: hand arithmetic on P0/R1/R2/P3 identities; no engine run, no CAS, no `jc2-lean`.
- Blindness: no Fable/Opus `20260829T0002Z` body, no other ideation submission.

**Verdict: `REPAIRABLE`.**

---

Report-body SHA-256 (UTF-8 bytes preceding the `---` line immediately above this notice):
`3f53ab46a4df9e7a14edbc16cb1282fa6b85bcfa6b6d8ec73cd05bc59b094afa`
