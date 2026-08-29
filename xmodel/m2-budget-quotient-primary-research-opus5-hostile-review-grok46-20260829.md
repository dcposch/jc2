# Hostile review — Opus 5 cap-free `M>=2` budget quotient

Lane: Grok 4.6, different-model adversarial referee.
Target report: `xmodel/m2-budget-quotient-primary-research-opus5-20260829.md`.
Comparison sources only: `ladder/BOOK-OFFAXIS.md` §§10 P0–P5 and 11–11a;
`ladder/SHEET6-DEPTH.md` R1/DS laws; `ladder/SHEET6-MULTIPOLE.md` MP1–MP8
and the §4 mixed-merge open; `ladder/REDUCTION.md` CRITICAL 4–7 and §5.2;
the Opus report; and
`xmodel/m2-budget-quotient-falsifier-grok46-20260829.md` used solely as an
agreement/disagreement crosswalk, never as authority.

No access of any kind to `jc2-lean`. No web, AWS, heavy/local CAS,
canonical edit, git status, commit, or push. Arithmetic below is desk
`int`/`Fraction` only.

Nothing here claims landing, a type ceiling, realizability, or JC2.

---

## 0. Custody

Full-file SHA-256 of the target, taken over the complete 43,396-byte
file:

```
ffb83ec1fcbfbbb18573a030e80e22c20a7d78bb92a5e7a6a5ce4d7b9b96e7af
```

matches the brief.

Body hash of the first 43,203 bytes (through and including the newline
after `*Report body ends. Self-hash below covers everything above this
line.*`):

```
b161421ccb04a62307b87be4a60f130ded64fe53228bd600c960f2c502632283
```

matches the brief and the report's own `report_body_sha256` line.

Licensed comparison sources were read in the sections named above. The
prior Grok falsifier was read only for the §5 crosswalk.

---

## 1. Verdict

**`REPAIR_REQUIRED`**

The T-law, the chain-layer qualitative quotient, the three-family
regeneration of the promoted 17-row `td=7` book, and the rejection of
ranking-or-lasso as the primary formulation are real. Several numbered
theorems, as stated, are false.

The report writes one grammar and then proves some clauses only on
chains, some only on case-I/II edges, and some only on the `td=7`
class-C book, while advertising them as uniform. The worst instances
are not extra-scope: Theorem 2 clause 4 and the case-I/II form of
(4a) fail on **all 17** promoted §11a cells, and Theorem 3.3's
identification of zero-cost merges with `eps=0` is refuted by that
same book.

Repair is local and cheap. The strongest promotion-safe residue is
stated in §6. The object the campaign actually needs — a cap-free
chain-layer `(w,M)` quotient with semilinear `nu`-fibres — survives.

---

## 2. Reconstructed laws used as the referee's baseline

Notation as in the target §2, which matches P0/R1.0/R2.2:

```
P  := sum_e mu_e + sum_j m_j
s  := r0 + k + lex
dp  = eps + nu*P
dq  = 1 + nu*s
M   = gcd(dp, dq)
E_e = mu_e*dq - dp
C_e := mu_e*s - P
T   := P - s*eps
```

The identity `E_e = (mu_e - eps) + nu*C_e` is elementary and holds at
every vertex. The identity `P*dq - s*dp = T` is the same combination.

Recorded transport is **not** uniform in the arriving edge type.

- Case I/II (R2.1, P0, R1.2/R1.4): `X = mu_e*(kbar - w_e)`, hence
  `kbar = mu_e*w_e*dq/E_e` and `w = mu_e*w_e*s/E_e`. This is the
  displayed (T) of the target §2.
- Case III (R2.1, DEPTH §5c): `X = mu_0*(kbar - nu_e*w_e)`, hence
  `kbar = mu_0*(nu_e*w_e)*dq/E_0`. The arriving `w_e` is replaced by
  the product `nu_e w_e`. Under the promoted E5 pin of §11a the
  product uses `nu_G`, not arrival `nu_U`.

Price (L) is P0/P2: extras of `p` and a **free** 0-root cost at least
1 each; arriving edges and `lex` q-extras price 0. A 0-arrival is not
a free 0-root: P3 prices every class-A/B/C merge at `lambda_merge=0`
with `eps=mu_0` arriving.

Integrality (I): `kbar in Z` at `nu>=2` (DS1(c), Not 3.5); at `nu=1`
the vertex is a case-I lattice meet and `kbar in Q` is legal.

T1 zero-chain law (§11): on the `td=7` class-B/C book, the cell is
T1-dead iff `dp | dq` iff `kbar in {3,4}`. Merge arity never enters.
The law is a closed form for Prop 8.1(iv) on **that book**, dual
certified there, not a vertex-local law of the charged grammar.

R2.2(D): `M_G | sum mu_e` holds iff `eps=0` and `k=0` (then
`dp=nu*sum mu_e` and `gcd(M,nu)=1`). Grounded when `dq>dp`; a rider
when `dq<dp`.

MP1: `sum (r-1) = m-1`. MP2: interior trunk `M != 1`. MP6(d)
subadditivity and the all-`mu=1` menu are the `eps=k=0` plus some
`mu_e=1` specialisation. MULTIPOLE §4 leaves mixed all-`mu>=2` merges
open beyond MP6(b) and (d)-subadditivity.

---

## 3. Attack 1 — Theorem 1 (`T`-law)

> At every vertex, `M | T := P - s*eps` and `T != 0`. Consequently
> `M <= |T|` and `M` is a function of `nu` modulo `|T|`.

**Divisibility: CONFIRMED**, uniformly, including mixed all-`mu>=2`
merges. `M | dp` and `M | dq` imply `M | (P*dq - s*dp) = T`. This is
the unique linear combination that eliminates `nu`. It specialises to
every recorded `M`-law in the target's table: neutral `T=l`, clean
resonant `T=l`, pure-`(b)` `T=l-eps`, all-`mu=1` IIa `T=r`, and
`eps=k=0` merges `T=sum mu_e`.

**`T != 0`: CONFIRMED after a typing repair, not as written.**

The written proof says: `T=0` implies `dp = eps*dq`, forbidden by
root-mult (R) at multiplicity `mu_star = eps`.

- If `eps >= 1` (free 0-root or 0-arrival), 0 is a root of `p` of
  multiplicity `eps` and (R) applies. CONFIRMED.
- If `eps = 0` there is **no** 0-root. Applying (R) to
  `mu_star = eps = 0` is illicit. The conclusion is still true:
  `T=P`, and `P=0` gives `dp=0`, banned independently by St 3.16
  (`deg p >= 2`). Repair: when `eps=0`, `T=P>=1`.

At a case-III 0-arrival, (S) gives `C_0 >= 1`, hence `T = -C_0 < 0`,
so `T != 0` is stronger than (R). The 17-row book has `T = 1-2 mu_0
< 0` in every row.

**Congruence: CONFIRMED.** Any common divisor of `dp` and `dq`
divides `T`. For each `d | |T|`, the conditions `d | dq` and
`d | dp` are congruences on `nu` modulo `d`, hence modulo `|T|`.
`M` is the largest such `d`, so `M` is a function of `nu mod |T|`.
(The naive `gcd(dp + t|T|P, dq + t|T|s)` can appear to jump; it
cannot jump off the divisor lattice of `T`.)

**R2.2(D) rider: DISCHARGED as a uniform `M`-divisibility;
NOT discharged as the original predicate `M | sum mu_e`.**

R2.2(D) is an iff for `M | sum mu_e`. Theorem 1 does not make that
predicate true when `k>0` or `eps>0`. It replaces the right-hand
side by `P - s*eps`. That is the correct reading of "the law never
fails, it merely changes its right-hand side". It is overstated if
read as "the §3 census law `M_G | sum mu_e` is now grounded at
`dq<dp` even with extras".

One sharpening the report misses: family 6a has `eps=k=0` and
`dp > dq`, and subadditivity `M | 2 mu` still holds. So `dq<dp`
does not by itself break R2.2(D); `k>0` or `eps>0` does. The rider
is about those extra-degree contributions, which is exactly what
BOOK-OFFAXIS.md §3 already flags on the 700 mixed skeletons.

On the 17 promoted cells the law holds, independently recomputed:
`M | |1-2 mu_0|` in 17/17 rows, with equality in 16 rows and
`M=5 | 15` on the unique `kbar=7` row. That is a check, not a
proof, and it is the check the report's D1 already ran.

Theorem 1 is the one clause that can be promoted as written, with
the `eps=0` typing sentence repaired.

---

## 4. Attack 2 — Theorem 2 (`C`-dichotomy)

### 4.1 Clauses 1–2

Clause 1 (`C_e=0` implies `E_e` constant, `kbar` affine unbounded,
`w` constant, `M` a function of `nu mod |T|`): CONFIRMED as
**local arithmetic on that edge**, provided `mu_e != eps` (else
`E_e=0`, illegal). The formula `|T|=s*(mu_e-eps)` needs `C_e=0`.

Clause 2 as written is **REFUTED for `C_e >= 1`** and CONFIRMED
for `C_e <= -1`.

The displayed bound `nu <= (E_e + eps - mu_e)/C_e` is the identity
`E_e = (mu_e-eps)+nu C_e` rearranged. It is not a bound: when
`C_e >= 1`, `E_e` grows in `nu` and `(S)` is automatic. Boundedness
of `nu` in this regime is Theorem 4(4a), which the clause does not
invoke. When `C_e <= -1`, `(S)` really does give
`nu < (mu_e-eps)/|C_e|`. That half stands.

Repair: split on the sign of `C_e`; feed `C_e >= 1` through (4a)
on a **case-I/II** edge.

### 4.2 Clause 3 (`C_e=0` for some `e` iff …)

**REFUTED as an iff for a single edge. CONFIRMED after the
quantifier is changed to all arriving edges.**

The written proof takes `e` with `mu_e = mu_min` and uses
`m_j <= mu_min-1` as if it upper-bounded `C_min`. That inequality
upper-bounds `m_j`, hence **lower-bounds** `C`. The displayed
`C_min <= mu_min*lex + k - (sum mu - r0 mu_min)` has the wrong
direction. Block D of the script tests only chain vertices (one
`mu`) and equal-`(mu,w)` joins, then the theorem statement
generalises to "some `e`".

Desk enumeration at `r0=2`, `mu_e <= 6`, `k,lex <= 3`, legal
`m_j in {1,...,mu_min-1}`:

- `C_e=0` for **every** `e` occurs only at equal `mu`, `k=lex=0`
  (6 cells in that range).
- `C_e=0` for **some but not all** `e` occurs 21 times. Samples:
  - `mu=(2,3)`, `k=1`, `m=(1)`, `lex=0`: `C_2=0`, `C_3=3`.
  - `mu=(2,4)`, `k=0`, `lex=1`: `C_2=0`, `C_4=6`.
  - `mu=(1,2)`, `k=0`, `lex=1`: `C_1=0`, `C_2=3`.

All three are legal under (S)+(NE)+(R) as degree inequalities
(`m_j <= mu_min-1`, searrow on arrivals, northeast on extras). They
are not free-`nu` families: unequal `mu` pins `kbar` by R2.1(ii),
and the two (T)-formulae agree at most on a thin condition in
`(w_a,w_b,nu)`.

So:

| reading | verdict |
|---|---|
| `C_e=0` for some `e` iff equal `mu`, `k=lex=0`, no 0-arrival | **REFUTED** |
| all `C_e=0` iff equal `mu`, `k=lex=0`, no 0-arrival, `0 <= eps < mu` | **CONFIRMED** |
| some edge `C=0` implies an unbounded legal family | **REFUTED** |
| all edges `C=0` implies `kbar` affine in `nu` and `w` constant, unless a later global constraint pins `kbar` | **CONFIRMED** (this is family 6a and the pure-`(b)` chain) |

The 0-arrival half of clause 3 is CONFIRMED: `(S)` at `eps=mu_0`
is exactly `C_0 >= 1`. A 0-edge is never a free-`nu` edge.

`nu=1`: `C_e=0` still makes `E_e` independent of `nu`, but `nu` is
a point, not a family. Integrality of `kbar` is not required.
Clause 1's "unbounded affine in `nu`" is vacuous.

Non-minimal edges: if `C_min=0` and some `mu_e > mu_min` then
`C_e > 0`. The "some `e`" zeros in the table above all sit on the
**minimal** arrival. Checking only the binding/`mu_min` edge is
not a substitute for checking every edge.

All-edge searrow consistency is the real obstruction the clause
skipped. For the `(2,3)` sample, `kbar` from the `C=0` edge is
`w_2(1+3 nu)` and from the other edge is `w_3(1+3 nu)/(1+nu)`.
Equality forces `w_2 = w_3/(1+nu)`, which is not the equal-`w`
join and is not an AP in `nu` at fixed `(w_2,w_3)`.

### 4.3 Clause 4 — postponed to Attack 4

The identity `E_0 = nu*|T|` is vertex-local at the merge and is
CONFIRMED (`eps=mu_0` cancels). The bound `nu <= mu_0*num(w_0)` is
Attack 4.

---

## 5. Attack 3 — Theorem 3 (zero-cost and the `M` bound)

### 5.1 Clause 1

`lambda_F = 0` is available iff `k=0` and there is no **free**
0-root. CONFIRMED, if "free 0-root" is kept distinct from a
0-arrival. P2/MP8 price arriving edges and `lex` q-extras at 0.
P3 prices every class-A/B/C merge at 0 with `eps=mu_0`.

### 5.2 Clauses 2 and 4 (chains)

Clause 2: zero-cost chain has `eps=0`, `k=0`, hence `T=l` and
`M_F | l | M_parent`. CONFIRMED. `M` is non-increasing under
divisibility along every zero-cost chain run.

Clause 4: DS3 with the `l`-cancellation of R1.2. CONFIRMED.
`num(w)` contracts by `<= 2/3` at resonant zero-cost steps;
`den(w)` is invariant; fewer than `log_{3/2} num(w_0)+1`
resonant zero-cost steps.

### 5.3 Clause 3 (zero-cost merges have `eps=0,k=0`)

**REFUTED.** The parenthetical "with `lambda=0` (`eps=0`, `k=0`)"
identifies zero-cost with vanishing `eps`. A case-III 0-arrival
has `eps=mu_0 >= 1`, prices 0, and with `k=0` is zero-cost.
That is the entire promoted §11a book: 17 rows, all `lambda_merge=0`,
all `eps=mu_0`, all `P=1`, `s=2`, `T=1-2 mu_0 < 0`. P3 already
says this in so many words.

Consequence for `T`: the written `T = sum_e mu_e` is the
`eps=k=0` case only. At case III, `T = P - s mu_0 < 0` and
`M | |T| = s mu_0 - P`, which depends on the unpriced `lex`.

**Unpriced `lex` q-extras.** P2: q-extras price 0. On an
`eps=0` merge they do not enter `T` (`T=P=sum mu_e + sum m_j`).
On a case-III merge they do: `|T| = mu_0*(r0+lex) - P_nonzero`
grows in `lex`. This does **not** by itself give an unbounded
`M` at fixed arrival `w`. Theorem 4(4c) on any nonzero
integer-`kbar` arrival supplies `dq/dp <= kbar_min * den(w_e)/mu_e`,
an upper bound on `dq/dp`, hence a bound on `s/P` and on `lex`.
Large `kbar` makes `dq/dp -> 1/mu` and **shrinks** `lex`. The
unpriced-`lex` threat is at small `kbar`, which is the side the
`td=7` T1 floor already kills. Finiteness of `M` at a case-III
vertex with a nonzero integer-`kbar` partner can be repaired by
(4c). The written factor `<= r0` cannot.

**Mixed all-`mu>=2` merges.** Theorem 1 applies arithmetically
(Attack 1). Zero-cost mixed merges with `eps=k=0` are exactly
the `all C_e=0` locus if `mu` are equal, i.e. family 6a, or a
bounded-`nu` locus if `C != 0`. MULTIPOLE §4 remains open as a
completeness statement; the T-law does not close it.

### 5.4 Clause 5 — the explicit bound
`M <= M_entry * max(m, 2^{m-1}) * 2^B`

**Chain layer: CONFIRMED after dropping the merge factor.**
Every charged chain step has `T>0` (free 0-root is `eps*s < P`;
`eps=0` is `T=P>=1`), `l | M_parent`, `m_j <= l-1`,
`lambda >= k + [free 0-root]`, hence
`M_F <= |T| <= P <= l(1+k) <= M_parent (1+lambda_F)`.
At most `B` charged steps, product maximised by `B` units of
`lambda=1`, so

```
M <= M_entry * 2^B.
```

Zero-cost chain steps cannot raise `M`. Pure-`(b)` cannot raise
`M`. The factor `max(m, 2^{m-1})` is a merge count and is not
used. Including it is a harmless inflation, not a proof of merge
growth.

**Whole configuration / merge layer: the written proof is
REFUTED; the numerical claim is UNPROVED; no reachable
counterfamily exceeding the `td=7` figure 128 is extracted from
the licensed book.**

The proof of the merge factor is "zero-cost `M`-growth happens
only at merges and only by a factor `<= r0 <= r`", which consumes
clause 3's false `eps=0`. At case III the factor is
`M_G | (s mu_0 - P)`, which is not `<= r0 max mu_e`. On the
promoted book one already has `M_G=5` at `(10,15,7,5)@3` against
nonzero `r0 max mu = 1`. MP1's `max(m, 2^{m-1})` therefore has
no licence at 0-arrivals.

Family 6a, which **does** have `eps=k=0`, grows by `M | 2 mu` with
`mu | M_parent`, a genuine factor `<= r0=2`, and sits inside the
written merge story. The `td=7` kbar=6 family has `M=2 mu_0 - 1
<= 2 M_U`, numerically inside `2 * M_entry * 2^B`. Tight, not a
counterfamily.

P5's "unbounded numerator and `M`" is too strong for **reduced**
`w` and `M` at fixed `(td, entry, B)`, on the chain layer, as both
this report and the prior falsifier claim. The repair of P5 is
chain-safe. It is not a proved whole-configuration bound of the
displayed constant.

Internal contradiction: §12 lists the bound as proved; §10a makes
the merge layer conditional on a `kbar` cap. Those cannot both
stand. The §10a conditionality is the honest one.

---

## 6. Attack 4 — Theorem 4 and the case-III `nu` bound

### 6.1 (4a)–(4c) on case I/II edges

**(4a) `E_e <= M * mu_e * a_e`: CONFIRMED for case I/II,
`nu>=2`.** The proof uses `kbar = mu_e a_e dq / (b_e E_e) in Z`,
which is (T) of §2, i.e. R2.1 case I/II. Then `E_e | mu_e a_e dq`,
`g=gcd(E_e,dq)` gives `E_e/g | mu_e a_e` and `g | dp`, hence
`g | M`. Which `M` is the child's `gcd(dp,dq)`. This is strictly
sharper than P0's `E | l num(w) T`, because `M | |T|` and `M`
may be proper.

**(4b): CONFIRMED**, independently of case. `E_e < mu_e dq` is
`dp>0`, hence `kbar > w_e` only in the case-I/II reading of (T).
The slope identity `dq/dp = kbar / (mu_e (kbar - w_e))` is
R2.1 plus `X/kbar = dp/dq`. On the 17-row book the nonzero
arrival is `mu=1`, `w=2`, `X=kbar-2`, and `dp/dq = X/kbar` holds
in 17/17 (the frozen-partner pin, not a 0-edge identity).

**(4c): CONFIRMED for case I/II, `nu>=2`.** `kbar - w_e >= 1/b_e`
and `x/(x-w_e)` decreasing in `x` give the displayed upper bound
on `dq/dp`. This is an **upper** bound on `dq/dp` and a **lower**
bound on `kbar`. It does not cap `kbar` from above: as `kbar ->
infinity`, `dq/dp -> 1/mu_e`, which sits *below* the (4c) ceiling.
The report's §8 sentence that Theorem 4 is "both lower-side" is
the right qualitative, slightly mislabelled.

### 6.2 The derived bound `nu <= mu_0 * num(w_0)`

**REFUTED**, by illicit transport and by the promoted book.

The proof: `E_0 = nu |T|` and (4a) `E_0 <= M mu_0 a_0` and
`M | |T|` cancel `|T|`. Three substitutions are wrong at once.

1. (4a) requires case-I/II (T). A 0-edge is case III. The correct
   formula is `kbar = mu_0 (nu_e w_e) dq / E_0`.
2. The `M` in (4a) is `M_G`. The cancellation `M_G <= |T|` is
   legal (Theorem 1) but unused if (4a) itself fails.
3. Under promoted E5, the pin uses `nu_G w_U`, and arrival `nu_U`
   is free on an AP (`§11a` arrival vertices: "neutral
   `nu ≡ -1 (mod mu_0)`"). A bound on arrival `nu_U` would
   contradict the book the report regenerates.

Independent replay on all 17 promoted cells, using `w_e = w_U`
as the report's `w_0`:

| cell | `E_0` | `M mu_0 num(w_U)` | `nu` | `mu_0 num(w_U)` |
|---|---:|---:|---:|---:|
| `(9,15,7,3)@2` | 21 | 6 | 7 | 2 |
| `(10,15,7,5)@3` | 35 | 30 | 7 | 6 |
| `(15,25,12,5)@3` | 60 | 15 | 12 | 3 |
| `(25,35,17,5)@8` | 255 | 120 | 17 | 24 |
| `(98,147,73,49)@25` | 3577 | 2450 | 73 | 50 |

`(4a)` with `w_U` fails in **17/17**. The bound `nu <= mu_0 num(w_U)`
fails in **16/17** (only the `kbar=7` row satisfies it, by accident:
`17 <= 24`). The case-I/II kbar formula on the 0-edge returns
`kbar/nu_G` (e.g. `6/7` on `(10,15)`), not the integer `kbar`.

The case-III formula `kbar = mu_0 nu_G w_U dq / E_0` reproduces
`kbar` in 17/17 and agrees with the E5 pin
`(mu_0 nu_G w_U - 2)/(mu_0 - 1)`. The corresponding (4a) analogue
`E_0 <= M mu_0 num(nu_G w_U)` holds in 17/17, and **does not bound
`nu_G`**, because the numerator on the right contains `nu_G`. That
is the cancellation the report wanted, and it does not fire.

Which `M` is used: `M_G`. Which `nu` sits in `E_0 = nu |T|`:
`nu_G`. Which `w` the report plugged into (4a): arrival `w_U`.
Those three objects do not make one inequality.

Repair: drop the bound. On the printed DEPTH §5c fork, case-III
arriving `nu_e` is a finite list of exact values (the prior
falsifier's `N_special`), not a residue, and not
`<= mu_0 num(w_0)`. On the promoted E5 fork, arrival `nu_U` is
an AP and is not pinned at all. Theorem 2.4 as stated is false
on both forks.

---

## 7. Attack 5 — the explicit `M` bound, chain vs merge

Stated in Attack 3.4. Summary for the brief's item 5:

- **Proved, chain-only:** `M <= M_entry * 2^B`.
- **True as a looser rewriting, chain-only:**
  `M <= M_entry * max(m, 2^{m-1}) * 2^B`.
- **Not proved for whole configurations.** The merge factor uses
  a false zero-cost identification. Case-III requires a separate
  `M <= |T|` estimate with `lex` controlled by (4c), not by `r0`.
- **No legal reachable counterfamily** in the 17-row book exceeds
  the `td=7` instance `2*2*32=128` (observed max `M=49`). Family
  6a does not exceed the merge factor `r0` either.
- **P5 repair is chain-safe** and does not licence the merge
  constant.

---

## 8. Attack 6 — the infinite equal-`(mu,w)` family

Local pattern, `r0=2`, equal `mu`, equal `w=a/b`, `eps=k=lex=0`,
and `b | 2 nu+1`:

```
dp = 2 mu nu,   dq = 2 nu + 1,   E = mu,   T = 2 mu,
kbar = w (2 nu + 1),   M_G = gcd(mu, 2 nu + 1),
w_child = 2 w,   lambda_G = 0.
```

**R1/R2 shape: CONFIRMED as a formal local cell.** (S) is
`mu(2 nu+1) > 2 mu nu`, vacuous, which is why R2.3(ii)'s
`(2,3)` prune does not touch equal `mu`. (R) is `2 nu != 2 nu+1`.
`dq ≡ 1 (mod nu)`. `gcd(M,nu)=1` because `M | (2 nu+1)`. All-edge
searrow and R2.1(i) are consistent: same `mu`, same `w`, same `E`.
This is the R2.3(ii) `l=0` arithmetic family that mixed merges
are allowed to have, and the §9 type-(i) survivor anatomy in
closed form. MULTIPOLE §4's mixed all-`mu>=2` open is exactly
this object when `mu>=2`.

**Integrality: CONFIRMED with a denominator constraint the
report states and then under-uses.** `kbar in Z` at `nu>=2`
requires `b | 2 nu+1`. Since `2 nu+1` is odd, **even
`den(w)` is impossible**. The five displayed points
`(3,3,1),(3,3,4),(3,3,7),(3,3,100),(5,2,12)` all have odd
denominator and check. The `td=8` entry `w=3/2` has `b=2`:
`kbar=(3/2)(2 nu+1)` is never integral at `nu>=2`, and at
`nu=1` one has `kbar=9/2` (legal as a lattice meet) with
`M=gcd(2,3)=1`, MP2-dead on an interior trunk.

**`gcd(M,nu)=1`: CONFIRMED**, as above.

**T1: ILLICIT, and unnecessary.** §11 is a closed form for
Prop 8.1(iv) on the `td=7` class-B/C book with the chain-1
freeze. Family 6a is an IIa-style equal-`mu` join, often with
`dp>dq` and `lex=0`, outside that class. The argument "T1
kills iff `dp | dq`, and here `dp>dq` so not dead" applies a
non-theorem and then uses a comparison that would make T1
vacuous on every `dp>dq` cell. For `mu=1` one has `M=1`
anyway (MP2). Do not cite T1 off-class.

**Arrival reachability and budget: NOT CONFIRMED.** The
members are formal local cells. The report's §1 and §6 openers
call them "budget-fitting, `lambda=0`, T1-alive cells inside
the charged grammar". `lambda_G=0` is a vertex price, not a
configuration price. Reaching equal `(mu,w)` with `mu>=2` and
odd `den(w)` from a fixed entry costs chain budget that was
not computed. `w_child=2w`; if `w>=1/2` the child has `w>=1`
and cannot terminate (P1 / R2.1 root window). A trunk is
required, and MP2 forbids `M_G=1`. None of this is checked.
§9 honesty note (ii) correctly withholds budget claims from
the 6b continuations; 6a did not get the same sentence.

**`td=7` class-A tail is not this family.** P3's `(6,10)` cell
is IIa with `l=1`, not `lex=0`. The `(2,2t)` tail is `nu_G=1`.
P4 prices class A out. Family 6a at `mu>=2` cannot start from
the unique `td=7` off-axis entry's frozen `(1,2)` partner.

Distinction the report blurs, and which REDUCTION CRITICAL 4
requires: **formal local cells are not reachable fixed-entry
configurations**. Family 6a is an exact infinite formal
family. Instantiation at any listed entry is D2, unrun.

---

## 9. Attack 7 — three-family regeneration, and D2

### 9.1 The 17-row book as three linear families

**CONFIRMED**, including `nu` and `M`.

Every promoted §11a cell has `P=1`, `s=2` (one nonzero
`mu=1` arrival, `k=0`, `lex=1`, 0-arrival `eps=mu_0`). The
chain-1 freeze `X=kbar-2` plus `kbar=2 dq/c` plus
`dp=mu_0+nu`, `dq=2 nu+1` collapse to

```
c (kbar-4) = 4 mu_0 - 2,     nu = c + mu_0 - 1,
M = gcd(2 mu_0 - 1, c),      mu_0 w_U = kbar - 4.
```

The three closed forms regenerate the book exactly:

| `kbar` | `(dp,dq,nu,M)` | `w_U` | `mu_0` in §11a |
|---|---|---|---|
| 5 | `(6m-3, 10m-5, 5m-3, 2m-1)` | `1/m` | `2,3,4,5` |
| 6 | `(4m-2, 6m-3, 3m-2, 2m-1)` | `2/m` | odd `3..25` |
| 7 | integer only at `m=8`: `(25,35,17,5)` | `3/8` | `8` |

Independent replay: 17/17 match, `book == regen`. The kbar=6
oddness is N1 (`gcd(6, 3m-2)=1`). Truncation at `mu_0=25` is
the priced `W` of the budget-5 closure, as §11a already says.
Continuation rows `(106,159,79,53)` and `(162,243,121,81)` are
family members, not budget-fitting; the report's §9(ii) is
honest here.

This is the right answer to "what kind of object is the `td=7`
off-axis book": three linear families in `mu_0`, cut by a finite
arrival alphabet, not 17 sporadic cells. It is not a finite-cell
theorem and the report does not need it to be one.

T1, N1, MP2, class-B emptiness, and the E5 pin are **inputs**
to the family (they select `kbar in {5,6,7}` and kill even
`nu` at kbar=6). The regeneration does not re-prove them.

### 9.2 Discriminator D2

As a reachability test for family 6a at the first all-`b>=2`
entry, D2 is well-posed and cheap. It needs four riders before
it can decide the merge layer.

1. Do not invoke T1. The `td=8` join is not a `td=7` class-C
   cell.
2. The odd-`b` constraint is load-bearing, not decorative. The
   named `td=8`, `M=[2,2]` entry has both `w_0=3/2`. Neutrals
   preserve `w` and cannot instantiate family 6a at `nu>=2`.
   D2 is a **dirty / pure-`(b)` / post-jump `w`** question, not
   an entry-join question.
3. A YES on an equal-`(mu,w)` pair with `gcd(mu, 2 nu+1)>=2`
   is a formal merge cell, not a complete configuration. One
   still needs `w_child` to feed a trunk with `w<1`, MP2, and
   `Sigma lambda <= td-1-psi`. `psi` is terminal and is not
   the single number `6`.
4. A YES proves the **cell** set infinite at that entry (one
   AP of `kbar`). It does not prove the **reduced-state** set
   infinite: `w_child=2w` is constant and `M | 2 mu` is finite.
   That is the report's own corrected reading of finiteness
   (§10 table, last finite-vs-infinite row). D2's sentence
   "the off-axis cell set is provably infinite at `td=8`" is
   accurate only in the cell reading the report already
   rejected as the campaign object.

A NO whose reason is "no odd-`den(w)` equal-`(mu,w)` pair in
budget" is a priced-alphabet fact, not the missing `kbar`
bound in disguise. The stop-rule's clause 2 over-reads a
negative.

---

## 10. Attack 8 — ranking, lasso, colon, and the prior falsifier

### 10.1 Ranking-or-lasso

On the **reduced** state `(w,M)`, a ranking function cannot
exist: the clean `n=1` step with `l=M` and `nu ≡ -1 (mod M)`
is an exact self-loop at cost 0. That is Statement 9.6(v) /
DS2 `n=1`, now at `M>=2`. CONFIRMED.

On a state that includes `deg p` or chain depth, the same move
is a ray (`deg p` multiplies by `nu>=2`) and a ranking exists.
It is uninformative for the campaign, which needs a finite
menu, not bounded delay along a chain (DEPTH §2 R1, DS4). The
report's "a ranking function cannot exist" is true of the
reduced graph and false of the configuration graph. Card 1
in its present form would return the known neutral loop and
be misread as a negative. Agree: do not run it as stated.

### 10.2 Colon

The split `C=0` (free `nu`, `w` constant) versus `C != 0`
(bounded `nu`) is a useful **Diophantine** dichotomy on case
I/II edges, after clause 3 is repaired to all-edges. It is
**not** an ideal-colon operation. There is no polynomial
ideal `I subset Q[x_i]`, no `Delta`, no `V(I,Delta)`, and
`V(den(w))` is empty (`den in N*`). Calling Grok Card 2
"closer to correct" because `C=0` looks like a proper open
is a metaphor. The prior falsifier's Attack E stands: the
Avenue-1 colon transplant is ill-typed in this grammar. The
slogan that survives is only "do not cap an unbounded
coordinate; quotient it".

### 10.3 Crosswalk with
`xmodel/m2-budget-quotient-falsifier-grok46-20260829.md`

Used only as agreement/disagreement, not as authority.

| prior item | Opus | this referee |
|---|---|---|
| L1: finite reduced `(w,M)` at fixed `B` | Thm 3.5, explicit constant | **L1 survives.** Explicit constant survives on chains as `M_entry 2^B`; merge constant does not. |
| L2: finite one-step menu, affine in parent `nu` | Thm 2.1–2.2 + (4a) | **L2 survives** on case I/II / chains. |
| L3: generic-AP uniformity plus a finite `N_special` | Thm 2.4 tries to replace `N_special` by `nu <= mu_0 num(w_0)` | **L3 survives.** Thm 2.4 is refuted. S3 vs S5 (same `(w,M, nu odd)`, different case-III well-formedness) still forces a special-`nu` table on the printed case-III fork. On the E5 fork, live cells are already uniform on APs (prior §1.3); arrival `nu_U` is not special. |
| Colon rejection | `C=0/C!=0` advertised as the colon split | **Rejection survives.** The C-split is the right Diophantine dichotomy, not a colon. |
| Ranking/lasso | both horns uninformative | **Survives** as a recommendation against Card 1 as stated. Optional depth ranking on the configuration graph remains legal and useless. |
| Attack A (S3/S5) | §7(a) agrees case-III needs full `nu_e` | Agree on the phenomenon. Disagree that a uniform bound replaces `N_special`. |
| Attack B (P5 mixes infinities) | P5 too strong; `M` bounded at fixed `B` | **Agree** for reduced `w` and `M` on chains. What is unbounded is `nu`, `kbar`, and `deg p`. |
| Attack C (no product of two free `nu`) | transport ratio is the one non-Presburger operation, degenerating at `C=0` | **Agree**, and this is the one place Opus is sharper. |
| Finite `kbar` window off-axis | family 6a, `kbar` affine unbounded | **Prior was wrong** to transplant DEPTH §5b's `w < kbar <= (r+1)w` (which needs `l>=1`) onto off-axis `l=0` equal-`mu` joins. Opus is right that `kbar` is unbounded on 6a. Both reports still agree the reduced `(w_child, M)` set of 6a is finite (`M | 2 mu`). |
| Proposed quotient `(w,M)` plus a handful of partner-independent residues | too coarse at case-III; repair by exact values not residues | **Agree.** |

The Diophantine `C=0 / C!=0` split is the repaired form of
Card 2's intended dichotomy and is not a colon. L1–L3 remain
the minimum lemmas for a proof-producing chain-layer quotient.
Opus's Theorem 1 is a new exact ingredient those lemmas should
absorb (it names the modulus `|T|`).

---

## 11. Clause-by-clause ledger

| item | verdict |
|---|---|
| Hash pair | CONFIRMED |
| Thm 1 divisibility `M | P-s eps` | CONFIRMED, including mixed all-`mu>=2` |
| Thm 1 `T!=0` via (R) at `eps=0` | REPAIRED (type: `P>=1` / `deg p>=2`) |
| Thm 1 `M` is `nu mod |T|` | CONFIRMED |
| Thm 1 discharges R2.2(D) as uniform `M`-law | CONFIRMED |
| Thm 1 discharges R2.2(D) as `M | sum mu_e` at `k>0` or `eps>0` | REFUTED (not claimed if the RHS-change sentence is read strictly) |
| Thm 2.1 (`C=0` edge arithmetic) | CONFIRMED locally |
| Thm 2.2 bound for `C<= -1` | CONFIRMED |
| Thm 2.2 bound for `C>= 1` | REFUTED as written (circular); REPAIR via (4a) on case I/II |
| Thm 2.3 iff, some edge | REFUTED |
| Thm 2.3 iff, all edges | CONFIRMED |
| Thm 2.4 identity `E_0 = nu_G |T|` | CONFIRMED |
| Thm 2.4 bound `nu <= mu_0 num(w_0)` | REFUTED (17/17 against (4a); 16/17 against the bound) |
| Thm 3.1 zero-cost iff `k=0` and no free 0-root | CONFIRMED |
| Thm 3.2, 3.4 chain monovariants | CONFIRMED |
| Thm 3.3 zero-cost merge has `eps=0` | REFUTED by case-III / the 17-row book |
| Thm 3.5 chain bound `M <= M_entry 2^B` | CONFIRMED |
| Thm 3.5 merge/config bound as written | REFUTED proof, UNPROVED constant |
| Thm 4 (4a)(4b)(4c) on case I/II, `nu>=2` | CONFIRMED |
| Thm 4 (4a) on case-III 0-edges | REFUTED |
| §6a formal local family | CONFIRMED, with odd-`den(w)` constraint |
| §6a as budget-fitting reachable cells | REFUTED (unrun); T1 citation illicit |
| §6a `mu=1` members | MP2-dead (`M=1`) |
| §6b three-family regeneration of 17 rows | CONFIRMED |
| §8 `td=7` four-link inversion | CONFIRMED as a `td=7`-specific argument |
| §8 first obstruction (no `kbar` cap at equal-`(mu,w)` joins) | CONFIRMED as the merge-layer open |
| §10a chain-layer repaired theorem, items 3–5 on chains | CONFIRMED after Thm 2.3/3.5 narrowing |
| §10a.1 normal form `kbar = w nu dq/(dq-1)` | REFUTED for `s != 1` (equals `w dq/s`, not (T)) |
| §10a merge layer conditional on a `kbar` cap | CONFIRMED as honesty; contradicts §12's "proved" |
| §10b algorithm, `nu <= mu_0 a` on 0-arrivals | REFUTED (consumes Thm 2.4); also ill-typed on a chain-only algorithm |
| Ranking absent on reduced `(w,M)` | CONFIRMED |
| Ranking-or-lasso the wrong primary formulation | CONFIRMED |
| `C=0/C!=0` as a literal colon | REFUTED (metaphor only) |
| P5 "unbounded `M`" too strong for reduced `M` at fixed `B` | CONFIRMED on chains |
| No JC2 / landing / realizability claim | CONFIRMED (riders held) |

---

## 12. Strongest promotion-safe result

> **Theorem (chain-layer budget quotient, repaired).**
> Fix `td`, a normalised entry, and `B = td-1-psi`. Restrict to
> chain vertices (`r=1`) of the P0 grammar. No new hypothesis.
>
> 1. `M | T` with `T = P - s*eps != 0` (`T=P>=1` if `eps=0`;
>    (R) if `eps>=1`). `M` is a function of `nu mod |T|`.
> 2. `C = l s - P`. Then `C=0` iff `k=lex=0`. In that case
>    `w` is constant on neutrals and expands by `l/(l-eps)` on
>    pure-`(b)`, `kbar` is affine in `nu`, and admissible `nu`
>    are a finite union of arithmetic progressions. If `C <= -1`,
>    `(S)` bounds `nu`. If `C >= 1`, (4a) bounds `E` and hence
>    `nu`.
> 3. Zero-cost steps are exactly `k=0` with no free 0-root.
>    Along them `M_child | M_parent` and `num(w)` is a
>    monovariant (DS3 / R1.2, `l` cancelled).
> 4. At most `B` charged steps, `M <= M_entry * 2^B`, and
>    `num(w)`, `den(w)` remain finite. The reduced state
>    `(w,M)` therefore ranges over a finite effective set.
> 5. The one-step successor of a chain state is decidable from
>    P0 plus (1)–(4). Case-III 0-edges, equal-`(mu,w)` joins,
>    and mixed all-`mu>=2` merges are **not** in scope.
>
> **Merge-layer residue, not promoted.** Theorem 1 still holds.
> All `C_e=0` iff equal `mu`, `k=lex=0`, no 0-arrival: this is
> family 6a, an exact infinite **formal** cell family with
> unbounded `kbar` and finite reduced `(w_child,M)`. Zero-cost
> includes case-III (`eps=mu_0`). The bound
> `nu <= mu_0 num(w_0)` is not a theorem. An upper bound on
> `kbar` at equal-`(mu,w)` joins remains the first obstruction
> to a cell-finite merge theorem; it is not needed for a
> reduced-state theorem, because `M | T` already bounds `M_G`
> once the discrete pattern `(mu_e, m_j, eps, k, lex)` is
> bounded. Whether that pattern is bounded at equal-`(mu,w)`
> joins without a `kbar` cap is D2 plus a trunk/MP2 check,
> not a consequence of Theorem 4.

The proposed theorem of the ideation cards, as adjudicated in
the target §10, then stands in this narrower form: **CONFIRMED
for the chain layer after the C-quantifier and the `M`-constant
are repaired; CONDITIONAL at merges** on a discrete-pattern
bound, of which a `kbar` cap is a sufficient but possibly
stronger request.

---

## 13. Cheapest next exact discriminator

D1 is already executed and independently replayed: T-law holds
on the 17-row book and the four P0 escapes. It cannot save
Theorems 2.3, 2.4, or 3.3.

Two desk-scale discriminators are now cheaper than D2, and
one of them is already run:

- **D1′ (executed here).** Replay (4a) with `w_e = w_U` on the
  17 0-edges. Falsifier of Theorem 2.4: 17/17 failures. No
  further work.
- **D1″ (executed here).** Exhibit a legal degree tuple with
  `C_e=0` for some but not all `e` (`mu=(2,3)`, `k=1`,
  `m=(1)`, `lex=0`). Falsifier of Theorem 2.3 as stated.

**D2, repaired, remains the right merge-layer experiment.**
Take `td=8`, `m=2`, `M=[2,2]`. Compute both priced chain
closures under P0 at budget `<= td-1-psi` with `psi` tracked
as a terminal, not a constant. Ask whether there exists an
equal-`(mu,w)` pair with `mu>=2`, `den(w)` odd, joint cost
fitting a legal trunk (`w_child=2w` descending to `w<1`,
`M_G>=2`, `gcd(mu, 2 nu+1)>=2`). Do not apply T1. A YES is
an infinite **cell** family at that entry and a finite
reduced-state family. A NO is a priced-alphabet statement
and does not produce a `kbar` theorem.

Do not substitute a larger enumerator cap. Family 6a, once
instantiated, is infinite as cells; a cap cannot be
completeness evidence in the cell reading.

---

## 14. Scope firewall

This review does not assert: a landing theorem; completeness
at any `td`; restoration of the prime-`td` exclusion;
realizability of any cell or family; an adjudication of
CONJECTURE H5a (the 17-row regeneration is of the promoted
E5 book; Theorem 2.4 fails on it regardless); `G2-BD`;
`G2-PSC`; a cofinal bound on `td`; or any JC2 consequence.
It does not access `jc2-lean`. It does not promote the
target's Theorems 2.3, 2.4, 3.3, or 3.5 at merge scope.

P5's generic `0 DEAD / 0 ALIVE / 2691 OPEN` remains the
honest grid-level statement until the repaired chain-layer
theorem is compiled and D2 is run. The obstruction named in
REDUCTION §5.2 is not "`M` is infinite at fixed budget" on
chains, and is not yet a theorem at equal-`(mu,w)` merges.

---

## 15. Replay

- Files read: the six paths named in the header, in the
  sections named in the brief.
- Files written: this path only.
- Compute: desk `int`/`Fraction` on the 17-row book, the
  `C_e=0` search at `r0=2`, family 6a identities, and the
  four P0 escapes. No engine, no CAS, no `jc2-lean`.
- Blindness: no ideation bodies, no other `20260829`
  research reports except the named prior falsifier used
  as a crosswalk.

**Verdict: `REPAIR_REQUIRED`.**

---

*Report body ends. Self-hash below covers everything above this line.*

report_body_sha256 = 7af0e75fb1b62dd9394fd60f63de1bbbb6e5b76526f025eb4b4e393aa27506ed
(sha256 of this file up to and including the line "*Report body ends...*", i.e. of the first 36337 bytes)
