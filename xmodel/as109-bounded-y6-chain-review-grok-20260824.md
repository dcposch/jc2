# Hostile different-model review — bounded partial-`y` degree six synthesis

| Field | Value |
|---|---|
| Claim under review | Characteristic-zero field theorem: every Keller pair whose two *actual* `y`-degrees are at most six is a polynomial automorphism. The synthesis froze as a conditional coverage audit with unreviewed leaves `(4,6)` and `(5,6)`. Those leaves now have landed different-model `CONFIRMED` reviews. In scope: actual partial `y`-degrees, target reductions, the 28/49 pair table, hash/dependency discharge, descent from an algebraic closure, and a quarantined AS109 correction-degree corollary. Out of scope: arbitrary-support AS109 no-go, a JC2 decision, a found lift, and any novelty or priority claim |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking: the frozen synthesis still labels the two sextic leaves `PROVISIONAL`, which was correct at freeze time and is discharged by the two landed reviews; the coverage replay over-approximates shear children; `(1,6)` in the producer table is worded as a max-five shear even though the affine argument already closes it) |
| Evidence tier | independent hand re-derivation of the top Jacobian identity and of every target reduction over an arbitrary characteristic-zero field, including constant leading coefficients; an independently written 28/49 enumeration that does not import the producer replay; unmodified rerun of `verify_degree_pair_coverage.py` as regression control; hash recomputation of every frozen synthesis file, every trust-matrix producer and hostile review, and both new leaf reviews; consumption of those reviews only at their exact stated hypotheses, not via producer PASS strings |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the synthesis producer (OpenAI Codex, GPT-5 family). The two leaf reviews being consumed were also written by this model family; they are used only as landed hostile reviews of *other* producers |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T11:50:00Z – 2026-08-24T12:02:07Z |
| Python | 3.14.6; stdlib only |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/as109-bounded-y6-chain-audit-20260824.md` (SHA-256 `1078bbdd47ccf085900b93b165ee268d314d2cc4e387b30ad81c4a40817e12f3`)
- `cases/as109_bounded_y6_chain_audit_20260824/verify_degree_pair_coverage.py` (SHA-256 `5c57325e602e2ef13f87f87fd50bc33e368117abf060576936bc7f7e8460df57`)
- `cases/as109_bounded_y6_chain_audit_20260824/FREEZE.sha256` (SHA-256 `2a94df9f42fb2d5e6c4609971cdbf5d23999d7bacd1f0aca3c2dff76bf4110dd`)
- every producer and landed hostile review named in the synthesis trust-state matrix (hashes in the dependency table below)
- landed leaf reviews `xmodel/as109-sextic-46-closure-review-grok-20260824.md` (SHA-256 `183ad7d6eab8b9f74041c2eb7d29180b2c75a4bc84d82bfeb681f29a55b9c32c`) and `xmodel/as109-sextic-56-exclusion-review-grok-20260824.md` (SHA-256 `d7b4f0e033f63f5e8f1f62b44f98ae23b566071cd34c810c18199cd099f88b70`)

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer, freeze, and review artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No enumerator was written into the tree. No AWS call was made.

Write `K` for an arbitrary characteristic-zero field, `Kbar` for an algebraic closure, and `J(f,g)=f_x g_y-f_y g_x`. Actual `y`-degrees are used throughout: a vanishing leading coefficient is a lower pair, not a total-degree convention.

---

## Promotion

**Accept `BOUNDED-Y-DEGREE-SIX FIELD THEOREM` at the stated scope, now that both frozen leaves have landed `CONFIRMED` reviews.**

- Over any characteristic-zero field, every Keller pair with both actual `y`-degrees at most six is a polynomial automorphism of `A^2_K`.
- There is therefore no exact `Z_{109}` polynomial lift of the seed `(x-x^{109},y)` with `det J=1` whose two correction polynomials both have `y`-degree at most six. Equivalently: every such exact lift has at least one correction of `y`-degree at least seven. The reviewed AS109 correction-degree floor rises from six to seven.

**Do not promote this to:** an arbitrary-support AS109 no-go; nonexistence of a lift with some correction of `y`-degree `>=7`; a found lift; a characteristic-zero point; a JC2 counterexample or disproof; `HEIGHT-CERT`; cap widening; an exponent rectangle; a finite Witt-level inference; a total-degree theorem; or a novelty / priority claim.

**Do not start a search for leftover sextic formal branches.** The resurrection condition is an error in a landed leaf review, in the reviewed quintic theorem, or in one of the target reductions below. None of those was found.

**Smallest valid successor.** A `y`-degree-seven (or mixed six/seven) genuine leaf, or an independent support-bounded AS109 argument that is allowed to use correction `y`-degree at least seven. This file licenses neither a heptics grammar nor a support search.

---

## Quarantine

No result here proves or disproves JC2. Producer strings `PASS-BOUNDED-Y6-DEGREE-PAIR-COVERAGE` and `ALL_49_ORDERED_PAIRS_COVERED` were not used as evidence; the pair table and the Jacobian identity were re-derived. The two leaf reviews are consumed only as emptiness of genuine `(4,6)` and genuine `(5,6)`. Their internal Newton/Pfaffian identities are not re-litigated here and are not a substitute for those reviews. Hensel is consumed only as the already reviewed one-way noninjectivity of an exact seed lift. Priority is quarantined from the mathematical verdict.

The classical affine/triangular theory, equal-degree `GL_2`, and divisible-degree shears subsume the reducible rows of the pair table. That observation is recorded separately in Claim 7. It does not replace the dependency audit of the genuine leaves.

---

## Scope (not enlarged)

One characteristic-zero field theorem about *actual partial* `y`-degrees, together with one prime `p=109` and one seed `(x-x^{109},y)` for the quarantined corollary. Arbitrary finite `x`-degree is in scope inside both `y`-degrees `<=6`. Target `GL_2` and polynomial target shears are automorphy tests over `K`; they need not preserve the integral AS109 seed chart, and the AS109 corollary does not apply them to the lift. Source changes used inside the leaf analyses are identities in `K(x)[y]`, not polynomial source automorphisms. Heptic and higher `y`-degree, series lifts, an arbitrary-support AS109 no-go, and JC2 are out of scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | The field statement uses actual partial `y`-degrees, not total degrees or a generic-coordinate convention. Target `GL_2` and polynomial target shears preserve Keller and automorphy. Source operations are not used as reductions in the pair table | **CONFIRMED** | a silent total-degree bound; a reduction that replaces `deg_y` by `deg`; a target operation that can turn a non-auto into an auto; a polynomial source change used as if it were a reduction |
| 2 | The top Jacobian identity is `n a_m' b_n-m a_m b_n'=0`. Equal-degree `GL_2`, divisible-degree shear, degree-zero obstruction, and affine-in-`y` triangular reduction all hold over an arbitrary characteristic-zero field, including constant leading coefficients, without extracting polynomial roots | **CONFIRMED** | a leftover `y^{m+n-1}` term from lower coefficients; `char | n`; kernel of `d/dx` on `K(x)` larger than `K`; `n/m` not an integer yet a polynomial power of `f` cancelling `y^n`; a constant `a_m` breaking the shear or the affine argument |
| 3 | There are exactly 28 unordered and 49 ordered pairs with both actual degrees in `{0,...,6}`. Recursive reductions terminate. The only genuine maximum-six leaves are `(4,6)` and `(5,6)`. One constant target `GL_2` on `(6,6)` lowers exactly one actual degree and produces no hidden third sextic case | **CONFIRMED** | a missing pair; a cycle in `(max,m+n)`; `6/4` integral; both leadings of a `(6,6)` pair cancellable by a single `GL_2` matrix of nonzero determinant; a leftover `(3,6)` or `(2,4)` genuine leaf |
| 4 | Every named producer/review hash matches. Each lower-degree leaf and the sextic skeleton has an applicable landed `CONFIRMED` review. The two new leaf reviews discharge exactly emptiness of genuine `(4,6)` and genuine `(5,6)`. Producer PASS strings are not substitutes | **CONFIRMED** | a hash mismatch; a leaf review still `GAP`/`REFUTED`; a leaf review that only closes a proper sub-stratum; treating `PASS-BOUNDED-Y6-DEGREE-PAIR-COVERAGE` as the theorem |
| 5 | Nonexistence strata descend from `Kbar` to `K`. After reductions, polynomial automorphy over `Kbar` descends to `K` by uniqueness of the inverse (Galois invariance) or faithful flatness | **CONFIRMED** | a `(5,6)` pair over `K` whose base change dropped an actual degree; a non-unique polynomial inverse; an inverse whose coefficients are not Galois-fixed |
| 6 | For the fixed seed, correction `y`-degree bounds are coordinate `y`-degree bounds. Automorphy of a `<=6` lift contradicts reviewed residue-ball Hensel noninjectivity. The only licensed AS109 conclusion is that every exact lift has at least one correction of `y`-degree `>=7` | **CONFIRMED** | the seed introducing a `y`-degree above the correction bound; Hensel uniqueness failing for unit Jacobian; the corollary asserting nonexistence of every finite-support lift; applying a chart-destroying shear to the lift before Hensel |
| 7 | The theorem is bounded partial degree only. It is not an arbitrary-support AS109 no-go, not a JC2 decision, and not a novelty claim. Classical reductions subsume the reducible rows and do not replace the genuine-leaf audit | **CONFIRMED** | a JC2 sentence; a total-degree rebranding; a priority claim; replacing `(2,3)`/`(3,4)`/`(2,5)`/`(3,5)`/`(4,5)`/`(4,6)`/`(5,6)` by Magnus/Moh/Żołądek without reading those reviews |

All remarks below are non-blocking unless marked otherwise. None changes a coefficient or a numbered verdict.

---

## Replay and hashes

Frozen synthesis hashes, recomputed on the charged tree:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-bounded-y6-chain-audit-20260824.md` | `1078bbdd47ccf085900b93b165ee268d314d2cc4e387b30ad81c4a40817e12f3` | prompt and `FREEZE.sha256` |
| `cases/as109_bounded_y6_chain_audit_20260824/verify_degree_pair_coverage.py` | `5c57325e602e2ef13f87f87fd50bc33e368117abf060576936bc7f7e8460df57` | prompt and `FREEZE.sha256` |
| `cases/as109_bounded_y6_chain_audit_20260824/FREEZE.sha256` | `2a94df9f42fb2d5e6c4609971cdbf5d23999d7bacd1f0aca3c2dff76bf4110dd` | prompt (self-hash) |
| `xmodel/as109-sextic-46-closure-review-grok-20260824.md` | `183ad7d6eab8b9f74041c2eb7d29180b2c75a4bc84d82bfeb681f29a55b9c32c` | prompt |
| `xmodel/as109-sextic-56-exclusion-review-grok-20260824.md` | `d7b4f0e033f63f5e8f1f62b44f98ae23b566071cd34c810c18199cd099f88b70` | prompt |

The case directory contains only `FREEZE.sha256` and `verify_degree_pair_coverage.py`. No enumerator, exponent rectangle, or AWS helper is present. The freeze lists the synthesis report, the coverage replay, the two then-unreviewed leaf *producers*, the quintic producer, and the sextic-preflight *review*. It does not list the two leaf reviews, which landed after the freeze; those hashes are in the prompt and match the files on disk.

Registered command, rerun unmodified:

```sh
python3 cases/as109_bounded_y6_chain_audit_20260824/verify_degree_pair_coverage.py
```

Exit code 0. Exact output:

```text
PASS-BOUNDED-Y6-DEGREE-PAIR-COVERAGE
unordered_pairs=28
ordered_pairs=49
confirmed_genuine_leaves=(2, 3),(3, 4),(2, 5),(3, 5),(4, 5)
provisional_genuine_leaves=(4, 6),(5, 6)
confirmed_only_unresolved_pairs=(4, 6),(5, 6),(6, 6)
fundamental_unreviewed_blockers=(4, 6),(5, 6)
conditional_on_both_closures=ALL_49_ORDERED_PAIRS_COVERED
```

Those `PROVISIONAL` / `unreviewed` labels are the synthesis freeze's trust state. They are not the present trust state. An independently written enumeration, which does not import that script, recovered the same 28/49 counts, the same genuine max-six leaves, termination on the lex order `(max(m,n),m+n)`, and the same `(6,6)` child list. That enumeration is Claim 3.

---

## Claim 1 — actual partial `y`-degrees; operations preserve automorphy

**CONFIRMED.**

Let `f,g in K[x,y]` with `J(f,g) in K^*`. Write

```text
f = a_m(x) y^m + ... ,     g = b_n(x) y^n + ... ,
```

with `a_m,b_n` nonzero in `K[x]`. Then `m=deg_y f` and `n=deg_y g` are the *actual* partial degrees. A zero leading coefficient is a different pair. No generic linear coordinate change is applied to manufacture these degrees, and no total-degree bound `deg(f),deg(g)<=6` is used. The synthesis, the coverage replay, the quintic theorem it consumes, and both leaf reviews all speak this language. A pair with `y`-degrees `(5,6)` may have arbitrarily large total degree through `x`; Moh-style total-degree theorems are therefore not a hidden input.

Target operations used as reductions are polynomial automorphisms `Phi` of the target `A^2`:

- constant `GL_2(K)`, including coordinate swap;
- elementary shears `(u,v) |-> (u, v-k u^d)` for `k in K` and `d>=1`.

If `F=(f,g)`, then `J(Phi o F)=J(Phi)(F)*J(F)` with `J(Phi) in K^*`, so Keller is preserved. `F` is an automorphism if and only if `Phi o F` is, because `Phi` is invertible in the polynomial automorphism group. In particular these operations cannot manufacture automorphy.

Source operations `F |-> F o Psi` would likewise preserve both properties, but the pair table does not use them. The rational substitutions `z=h y+r` inside the `(4,6)` and `(5,6)` analyses are identities in `K(x)[y]` (or a quadratic algebraic differential extension) and are not claimed to be polynomial source automorphisms. The chain never treats a non-polynomial source change as a reduction.

---

## Claim 2 — Jacobian identity and the four reductions

**CONFIRMED.**

A pair of terms `(a_i y^i, b_j y^j)` contributes `j a_i' b_j - i a_i b_j'` to the coefficient of `y^{i+j-1}`. Lower `y`-coefficients cannot produce a higher top degree. The unique top contribution is therefore

```text
n a_m' b_n - m a_m b_n' = 0                                   (2.1)
```

whenever `m+n-1>0`, because `J` is a nonzero constant. Characteristic zero supplies `n!=0` and `deg pi'=deg pi-1` for nonconstant `pi in K[x]`. Equivalently `(a_m^n / b_n^m)'=0` in `K(x)`, so `a_m^n = c b_n^m` with `c in K^*`: the kernel of `d/dx` on `K(x)` is `K` (write a ratio in lowest terms in the Euclidean domain `K[x]`; a nonconstant denominator would have to divide a strictly lower-degree derivative).

*Equal actual degrees `m=n>0`.* Then `(a_n/b_n)'=0`, so `a_n = k b_n` with `k in K^*`. The constant target operation `(f,g) |-> (f-k g, g)` cancels the `y^n` term of the first coordinate and leaves the second at actual degree `n`. A general matrix in `GL_2(K)` cannot cancel *both* leadings: that would require both rows to be proportional to `(-k,1)`, hence determinant zero. Constant leading coefficients are included: if both leadings are in `K^*` the Wronskian vanishes automatically and the same row operation applies. If exactly one leading is constant, (2.1) forces the other to be constant as well.

*Divisible degrees `0<m<n` with `m` dividing `n`.* Let `d=n/m in Z`. Unique factorization in `K[x]`: at every prime, `n v(a_m)=m v(b_n)`, hence `v(b_n)=d v(a_m)`. Therefore `b_n = k a_m^d` with `k in K^*`. No `m`-th root of a polynomial is extracted; the exponents already match. Units of `K[x]` are `K^*`, so `k` lies in `K` without extending the constant field. The polynomial target shear `g |-> g-k f^d` cancels the `y^n` term and strictly lowers the maximum actual degree. Constant `a_m` is included: (2.1) then forces `b_n` constant, and `f^d` is still a polynomial of `y`-degree `n`.

This is why `gcd(4,6)=2` does not help: `6/4` is not an integer, so no polynomial `f^d` has `y`-degree 6. Conversely `(2,4)`, `(2,6)`, `(3,6)`, and every `(1,n)` *are* honest shears.

*Degree zero, `m=0`.* Then `f=a_0(x)` and `J=a_0' g_y`. If `a_0` is constant then `a_0'=0` and `J=0`, so `(0,0)` is impossible and so is any `(0,n)` with constant `a_0`. If `n>=2` then `g_y` has positive `y`-degree or else `n=1`; a product of a nonconstant element of `K[x]` with a polynomial of positive `y`-degree, or with a nonconstant element of `K[x]`, cannot be a nonzero constant. The remaining case is `(0,1)`: `a_0' b_1 = j in K^*` forces both factors to be units of `K[x]`, so `a_0` is degree one and `b_1 in K^*`. That pair is triangular. In particular `(0,n>=2)` is not Keller, including `(0,6)`.

*Affine in `y`, `m=1`.* Write `f=a y+b` with `a!=0` and put `t=f`. Expanding `g=sum_{k=0}^N c_k(x) t^k` over `K(x)` gives `J_{x,y}(f,g)=-a (partial g / partial x)|_t`, so `sum c_k' t^k` is, up to the unit `-a`, a nonzero constant. Linear independence of `{1,t,...,t^N}` over `K(x)` forces `c_k` constant for every `k>=1`. The remainder `c_0=g-sum_{k>=1} c_k f^k` lies in `K[x,y] cap K(x)=K[x]`, and `-a c_0'=j`. Both factors are units of `K[x]`: `a in K^*` and `c_0` has degree one. The pair is triangular over `K`, with polynomial inverse over `K`. Constant leading coefficient is not an extra case: the argument *proves* `a` is a unit. Characteristic zero is load-bearing (`c_k'=0` implies constant, and `deg c_0'=deg c_0-1`). This closes every `(1,n)` including `(1,6)`, independently of the quintic theorem.

All four reductions take place over `K`, not only over `Kbar`.

---

## Claim 3 — 28/49 pairs, termination, only two genuine sextic leaves, `(6,6)`

**CONFIRMED.**

The unordered pairs with `0<=m<=n<=6` are the 28 pairs `n=0..6`, `m=0..n`. The ordered pairs with `0<=i,j<=6` are the 49 pairs in `{0,...,6}^2`. Coordinate swap is constant `GL_2` and identifies each ordered pair with `i>j` to an unordered pair. There is no 50th pair and no missing 29th.

Independent classification of the 28 unordered pairs, not imported from the producer script:

| Pair | Route | Result |
|---|---|---|
| `(0,0)` | `J=0` | impossible |
| `(0,1)` | degree-zero triangular | automorphism |
| `(1,1)` | affine-in-`y` (also equal-degree `GL_2 -> (0,1)`) | automorphism |
| `(0,n)` for `n=2,3,4,5,6` | degree-zero obstruction | impossible |
| `(1,n)` for `n=2,3,4,5,6` | affine-in-`y` | automorphism |
| `(2,2),(3,3),(4,4),(5,5)` | equal-degree `GL_2` | reduces to prior rows |
| `(2,4)` | shear `g-k f^2` | max drops below four |
| `(2,3)` | genuine coprime | empty, cubic `CONFIRMED` |
| `(3,4)` | genuine coprime | empty, quartic `CONFIRMED` |
| `(2,5),(3,5),(4,5)` | genuine coprime | empty, quintic `CONFIRMED` |
| `(2,6)` | shear `g-k f^3` | max at most five |
| `(3,6)` | shear `g-k f^2` | max at most five |
| `(4,6)` | genuine imprimitive; `6/4` not an integer | empty, landed `(4,6)` closure |
| `(5,6)` | genuine coprime; `6/5` not an integer | empty, landed `(5,6)` exclusion |
| `(6,6)` | equal-degree `GL_2 -> (r,6)`, `0<=r<=5` | no third leaf; see below |

Every equal-degree or divisible step strictly lowers the lex measure `(max(m,n), m+n)`: shears drop the maximum, and equal-degree `GL_2` keeps the maximum but drops the sum. There is no cycle.

*The pair `(6,6)`, scrutinized.* One constant target `GL_2` cancels exactly one leading coefficient and produces an ordered pair `(r,6)` with `0<=r<=5`. It cannot produce a second `(6,6)`: that would require both leadings to survive. It cannot produce a pair whose *maximum* is less than six in a single step: the surviving coordinate still has actual degree six. The six children and their fates are:

```text
(0,6)  impossible as Keller, so a (6,6) Keller pair cannot land here
(1,6)  affine triangular automorphism
(2,6)  shear to maximum <=5, then the quintic theorem
(3,6)  shear to maximum <=5, then the quintic theorem
(4,6)  empty as Keller (landed closure)
(5,6)  empty as Keller (landed exclusion)
```

Thus a `(6,6)` Keller pair cannot land on `(0,6)`, `(4,6)`, or `(5,6)`, and must land on `(1,6)`, `(2,6)`, or `(3,6)`, all of which are automorphisms after the reviewed quintic range. There is no hidden third sextic case such as a residual `(6,6)` after `GL_2`, a mixed `(6,r)` that is not a swap of `(r,6)`, or an imprimitive `(6,6)` needing its own normal form.

The producer coverage replay over-approximates divisible-shear children as every `(m,r)` with `r<n`. That is conservative for dependency tracking (it may list genuine leaves that a particular shear never hits) and does not hide a pair. The independent classification above uses the same child set for shears and still finds no extra genuine max-six leaf.

---

## Claim 4 — dependencies and hashes; leaf reviews discharge exact hypotheses

**CONFIRMED.**

Trust-state matrix after the two landed leaf reviews. Producer PASS strings were not read as theorems; each hostile review's overall verdict and exact claim is the object consumed.

| Layer | Producer SHA-256 | Hostile review SHA-256 | State | Logical use |
|---|---|---|---|---|
| quadratic `<=2` | `10ee0b91d4be7ced8d6c053ba66e6d677d7c4cc83af89fc481d215f145e38ea1` | `4ee7793d352d130d79b5efb1f555c8a241ed5ed59335426238505da5dcae48f2` | `CONFIRMED` | historical base; subsumed by quintic |
| cubic `<=3` | `198f0b2ff39f91a7815b9be15f7fc3c3afdd00c00b1c4c0ada6b9f6438d62820` | `2fdb8ae2beffb766b38d8e7de4bdff353bc354c4dba84d026225f88376f95cef` | `CONFIRMED` | closes genuine `(2,3)` |
| quartic `<=4` | `8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276` | `3f9e763c07aa019a766b267774f92df857aadd94750cb8c3c9431671318d930e` | `CONFIRMED` | closes genuine `(3,4)`; input to quintic |
| quintic `<=5` | `598cdf3799d4abf40ec761f1fd2b0a5a6457ee2b578371bd864c296259d2a978` | `ab5ce55c1d71628e16800bc9ff9985da9f4ae90fe521849fa2060e97ff552e0e` | `CONFIRMED` | every pair of maximum actual degree `<=5` is an automorphism |
| sextic skeleton | `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4` | `5bf1a677a59975defb33a58da74d7c7c1381535d84f91e7f1584d21624a385ff` | `CONFIRMED` | only `(4,6),(5,6)` are fundamental sextic leaves; re-derived in Claim 3 |
| `(4,6)` discriminator | `b2f6a16eb8399d4de408c41070c666000b324409a5332fa211eff011b5624552` | `4f2c8b6cd1a165ed73dedb0a3fc92256199927961a6c5126afc6689408106c59` | `CONFIRMED` as survivor normal form | exact input to the `(4,6)` closure |
| `(4,6)` local closure | `587a142a09ac70805264f56ed408545fa6dd0b771d4712459fad6eddcf9902ac` | `183ad7d6eab8b9f74041c2eb7d29180b2c75a4bc84d82bfeb681f29a55b9c32c` | **`CONFIRMED`** | genuine `(4,6)` empty |
| `(5,6)` weighted exclusion | `31420c0cd667640f340f4d127f185edd4515aac7df3733560e6d1fda5ec6c7a4` | `d7b4f0e033f63f5e8f1f62b44f98ae23b566071cd34c810c18199cd099f88b70` | **`CONFIRMED`** | genuine `(5,6)` empty |
| Hensel (corollary only) | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` | `CONFIRMED` as one-way implication | noninjectivity of an exact seed lift over `Q_109` |

All sixteen hashes were recomputed from the on-disk bytes and match the synthesis matrix, the freeze, and/or the launch prompt.

*Exact hypotheses discharged by the new leaves, not by PASS strings.*

- The `(4,6)` review's claim under review is emptiness of every solution of the frozen normal-form equations (1.1)–(1.6) after the reviewed parent discriminator and the reviewed grandparent split. Overall verdict `CONFIRMED` on all seven numbered claims. It explicitly refuses a `y`-degree-`<=6` theorem. That is exactly “genuine `(4,6)` is empty”. The parent's former `PROVISIONAL` label is recorded there as historically accurate and mathematically discharged by the landed discriminator and preflight reviews. This chain review does not re-open Newton faces; a resurrection would be an error in that landed review, which was not found in its stated scope.
- The `(5,6)` review's claim under review is that no characteristic-zero Keller pair has actual degrees `(5,6)`, using both `y=0` boundaries, the third integral `dI_1=omega-(2A/5) dI_3` licensed by the preflight review, the weighted common-factor lemma, and polynomial infinity. Overall verdict `CONFIRMED` on all seven numbered claims. It explicitly refuses a `<=6` theorem and does not consume `(4,6)` or the quintic theorem. That is exactly “genuine `(5,6)` is empty”. The preflight headline that no third integral followed is the completeness overstatement already recorded by the synthesis; the successor identity is the reviewed input, not a producer PASS.

The two closures concern disjoint actual leading-degree strata. No compatibility condition between them is required. Together with the confirmed quintic theorem and Claims 2–3, every pair of maximum actual degree at most six is either impossible, an automorphism, or empty.

The coverage replay remaining labels `provisional_genuine_leaves` and `fundamental_unreviewed_blockers` are freeze-time strings. They are not a live blocker.

---

## Claim 5 — descent from an algebraic closure

**CONFIRMED.**

*Nonexistence strata* (`(0,n>=2)`, genuine empty leaves including `(4,6)` and `(5,6)`). A Keller pair over `K` remains a Keller pair of the same actual `y`-degrees after base change to `Kbar`: leading coefficients stay nonzero. Emptiness over `Kbar` therefore implies emptiness over `K`. Scalar extension of the constant field to absorb units into pure powers `H^2`, `h^5`, and so on is the same one-way implication. The `(5,6)` review's use of algebraically closed residue fields and a monic linear factor `z-r t`, and the `(4,6)` review's Puiseux analysis over `Kbar`, are therefore licensed as nonexistence arguments over every characteristic-zero `K`.

*Automorphy after reductions.* The reductions of Claim 2 are defined over `K`: the ratio `k` lies in `K^*` by unique factorization in `K[x]`, and the affine-in-`y` argument never leaves `K`. Once a reduced pair is an automorphism over `K`, so is the original pair, because the target operation is in `Aut(A^2_K)`.

If one prefers to check automorphy after base change: a polynomial endomorphism of `A^2` has at most one polynomial inverse. If `(f,g)` is defined over `K` and becomes an automorphism over `Kbar`, that inverse is unique as a morphism, hence Galois-fixed, hence defined over `K` (`K` is perfect in characteristic zero). Faithful flatness of `Kbar/K` gives the same descent for isomorphy of coordinate rings. Injectivity, which is all the AS109 corollary needs, descends even more cheaply.

No pair was found whose actual degrees drop under base change, and no inverse-uniqueness gap was found.

---

## Claim 6 — conditional AS109 corollary

**CONFIRMED.**

The reviewed Hensel lemma is a one-way implication: *if* an exact polynomial lift over `Z_{109}` of the seed `(x-x^{109},y)` with `det J=1` exists, *then* it is bijective on each residue ball, hence 109-to-1 onto balls over `(0,b)`, hence noninjective over `Q_{109}`. It does not assert that such a lift exists.

The seed's first coordinate has `y`-degree 0 and the second has `y`-degree 1. If both correction polynomials have `y`-degree at most six, both lift coordinates have `y`-degree at most six over `Q_{109}`: the seed contributes no higher `y`-power, and cancellation with the linear seed term can only *lower* the second coordinate's degree. (The launch phrasing “equal the correction bounds” is this inequality for this fixed seed, not an identity in every monomial.) The field theorem of Claims 1–5 then makes the lift a polynomial automorphism of `A^2_{Q_{109}}`, hence injective over `Q_{109}`.

That contradicts Hensel. The field theorem is applied to the lift pair itself, not to a sheared pair, so chart-destroying target operations never enter the corollary. Characteristic `109!=2,3,5` is compatible with every displayed denominator in the consumed leaves.

The only licensed conclusion is: every exact `Z_{109}` lift of this seed with `det J=1` has at least one correction of `y`-degree at least seven. The reviewed floor therefore rises from six (quintic theorem: not both corrections `<=5`) to seven. This is not an arbitrary-support no-go, not a statement that no lift exists, and not a JC2 inference.

---

## Claim 7 — scope; simpler theorems recorded separately

**CONFIRMED.**

The admissible theorem is bounded partial `y`-degree six. The synthesis does not claim, and this review does not confirm:

- nonexistence of an exact AS109 lift with some correction of `y`-degree `>=7`;
- an arbitrary-support or cap-eight no-go;
- a found lift, a characteristic-zero point, or a complex Keller counterexample in hand;
- a JC2 decision;
- a total-degree theorem;
- a novelty or priority claim.

*Simpler known facts that subsume part of the pair table, recorded so they are not mistaken for a replacement of the genuine-leaf audit:*

- `(0,1)` and every `(1,n)` are classical triangular / affine-in-`y` automorphisms (Jung–van der Kulk generators, not JC2).
- Equal-degree constant `GL_2` and divisible-degree elementary shears are standard 2-variable reductions (they appear in the quartic and quintic reviews and in the sextic preflight). They account for `(n,n)`, `(2,4)`, `(1,6)`, `(2,6)`, and `(3,6)`.
- Jung–van der Kulk generates `Aut(K[x,y])` by affine and triangular maps. It does **not** prove that Keller maps are automorphisms.
- Total-degree theorems (Moh; various coprime-total-degree results of Magnus / Appelgate–Onishi / Nowicki–Nakai as flagged in the campaign priority notes; Żołądek 2008 in a Newton–Puiseux chart) do **not** subsume genuine leaves of unbounded `x`-degree. A `(5,6)` pair may have total degree far above any published total-degree bound.

Those observations do not close `(2,3)`, `(3,4)`, `(2,5)`, `(3,5)`, `(4,5)`, `(4,6)`, or `(5,6)`. Those seven leaves remain the objects of the consumed hostile reviews. The present theorem is a campaign synthesis of those reviews plus the elementary reductions, not a citation of a simpler published `deg_y<=6` statement.

---

## Non-blocking precisions

None of the following changes a numbered verdict.

1. *Synthesis still says `PROVISIONAL` / `TWO UNREVIEWED LEAVES`.* Historically correct at freeze time `2026-08-24T11:38:17Z`. After the two landed leaf reviews and this chain review, the degree-at-most-six theorem is actual, not conditional. A later freeze may relabel the leaves; no identity changes.

2. *`(1,6)` table wording.* The producer table lists `(1,6)` as “shear `g-k f^6`, or affine reduction / maximum degree at most five”. The affine argument of Claim 2 already makes `(1,6)` a triangular automorphism over `K`, stronger than reduction into the quintic range. Both routes are valid.

3. *Coverage replay children.* Divisible shears are recorded as every ordered pair `(m,r)` with `r<n`. That over-approximation cannot hide a missing pair. It is why `(2,6)` lists `(2,5)` as a possible child even though a particular shear might land lower.

4. *Freeze contents.* The freeze file hashes the two leaf *producers* and the preflight *review*, not the two leaf reviews. Those reviews did not exist at freeze. Their hashes match the launch prompt.

5. *Constant-field units in leading UFD.* Writing `a_5=h^5` or `a_4=H^2` after constant scaling may require extracting an `m`-th root of a unit of `K`. That is a scalar extension of the constant field, used only in nonexistence strata, and is covered by Claim 5. The divisible shears of Claim 2 never need it: `k` is already in `K^*`.

6. *Linear `K` on the `(4,6)` nonsquare side, Cayley–Hamilton packaging of `(5,6)` poles, and the unused Darboux search* remain the non-blocking precisions of the consumed leaf reviews. None of them is a missing pair or a partial-to-total-degree switch.

---

## Attacks that did not land

The following were checked because they are the stated failure modes.

- *Missing pair.* Independent listing of all 28 unordered and 49 ordered pairs; no 29th unordered pair, no unclassified remainder. `AssertionError` in the producer script is aimed at an unclassified genuine pair and does not fire.
- *Bad UFD / root extraction.* Divisible shears use exponent arithmetic `v(b_n)=(n/m) v(a_m)` in the UFD `K[x]`. Polynomial roots are not extracted. `(4,6)` is correctly *not* treated as a shear.
- *Constant-field descent error.* Reductions run over `K`. Nonexistence over `Kbar` implies nonexistence over `K`. Unique polynomial inverses are Galois-fixed.
- *Illicit partial-to-total-degree switch.* The Jacobian top, the pair table, the quintic input, both leaves, and the AS109 corollary all use `deg_y`. No total-degree bound is an input.
- *Hidden third sextic case from `(6,6)`.* One `GL_2` step lowers exactly one actual degree. Both leadings cannot vanish at once. The six children are accounted for.

---

## Promotion advice (repeated)

Accept the synthesis, together with the two landed leaf reviews, as a completed characteristic-zero theorem: every Keller pair with both actual `y`-degrees at most six is a polynomial automorphism of `A^2_K`. Accept the quarantined AS109 corollary that every exact `Z_{109}` lift of `(x-x^{109},y)` with `det J=1` has at least one correction of `y`-degree at least seven.

- Bank it as the successor of the confirmed quintic theorem, not as a replacement of Hensel or of the support grammar stop.
- Do not treat this as an arbitrary-support AS109 no-go, a found lift, a JC2 decision, or a novelty claim.
- Do not feed a closed sextic pair into a search for polynomial automorphisms.
- Next bounded calculation this review licenses: genuine leaves of maximum actual `y`-degree seven, or an independent support argument that is allowed to use correction `y`-degree at least seven. It licenses no enumerator and no AWS.

No result in this review proves or disproves JC2.
