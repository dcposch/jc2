# Hostile review — small-`a` unique-`AC` `d=2,3` support/local-pole census

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_unique_ac_d23_small_a_support_miner_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest bad atom count / coefficient / baseline / local-pole class | none |
| First omitted strict-cell baseline | none among `1<=a<=9`, `d in {2,3}` |
| First extra dangerous family | none; nearest misses are `(2,3,1)` unloaded `R A^2/L^2` (local upper `1`) and `(1,3,1)` `k10 R^2 A/L^2` (local upper `1`) |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer `PASS` markers, validator strings, RESULT summaries, and the finite-field lane are not authority |
| Method | SHA-256 of every charged pin and every freeze/evidence/nested-manifest row; independent reconstruction of the unique-`AC` inequalities; independent binomial expansion of `f=L^4(1+X)` by remaining-budget DFS, not by importing `mine_support.py`; independent derivation of the `A0`-root correction bound. No Singular, Sage, msolve, Lean, or AWS re-execution |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the six required primary pins match the charged bytes. Every path named in `FREEZE.sha256` (5/5) and `EVIDENCE.sha256` (30/30) rehashes to the printed digest, as does `PRODUCER_FREEZE.sha256` (4/4). Both nested `results.sha256` manifests rehash after resolving the AWS absolute paths by basename to the local `output/` copies (2/2 each). Exact `Q` on Box03 is the support endpoint; `F_65521` on r6d is the same rational enumerator with a different characteristic token, not a separately implemented modular census. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

The strict unit-load unique-`AC` inequalities `a>=1`, `r>=2`, `c>=3`, `d=c-a in {2,3}`, `s=r-a>=0`, `a+3*s>d`, restricted to `a<=9`, have exactly eighteen `(a,d)` blocks. Their minimum admissible `s` is the stated table. Independently expanding the four binomial summands of `f^{3/2}+sigma^4 k10 f^{5/4}+sigma^{12} k6 f^{3/4}+sigma^{20} k2 f^{1/4}` through `T=10+2*a+2*d` produces, after like-term aggregation over `Q`, a polar inventory whose signatures match the frozen JSON on every block. The combinatorial local-pole upper bound at the allocated `A0` root is

```text
q - max(e_A - (T-g), 0).
```

Every block contains the target `(3/8) C^2/L^2` as a local double pole at `T`. Exactly one block, `(a,d,s)=(1,3,1)` i.e. `(a,c,r)=(1,4,2)`, has a second family with upper bound at least two: `-(3/8) R A^2/L^2`, first grade `16`, correction depth `2`. No other primitive, including cancelled monomials, `pad=2` extra counts, or remaining-budget tuples outside the code's Cartesian product, crosses that wall.

This is support navigation and an upper bound on source local pole order. It does not replay the seven Faber rows, does not compute actual `u^{-2}` coefficients, does not prove root allocation or truncated divisibility, does not close seventeen cells, and does not decide `(1,4,2)`.

**CONFIRMED**

---

## Verdict table

| Charge | Finding |
|---|---|
| 0. Custody | six primary pins match; freeze 5/5, evidence 30/30, producer freeze 4/4; both nested `results.sha256` match by basename |
| 1. Unique-`AC` inequalities, `r>=2`, eighteen `a<=9` baselines | **holds**; first omitted strict-cell baseline: none. First excluded integer point: `(a,d,s)=(1,2,0)` (`r=1<2` and `a+3s=1<=d`) |
| 2. Four atoms, four summands, costs, multinomials, aggregation, `pad=1` | **holds**; DFS = Cartesian `pad=0` = `pad=1` = `pad=2` = frozen inventory. Zero aggregations are identities of `(1+y)^3`, not hidden poles |
| 3. Bound `q-max(e_A-(T-g),0)` | **holds as an upper bound** at the allocated `A0` root. Losing an `A0` factor cannot cost zero sigma. Load families are separately enumerated. Moving `p` does not raise the local order in the Hensel coordinate. The bound is not an equality and is not a Faber-row statement |
| 4. Eighteen inventory blocks | **holds**; `C^2/L^2` coefficient `3/8` on all eighteen; seventeen `SAFE_C2_ONLY`; sole extra family `-(3/8)R A^2/L^2` at `(1,3,1)`. First extra dangerous family: none |
| 5. Dual AWS custody | **holds**; distinct hosts/PIDs/tags/result JSON; identical inventories and stdout; rc `0`; wall `0.08 s`; RSS `18528`/`18340` KiB; swaps `0`; `F_65521` is a coefficient/software control |
| 6. Firewall | **holds**; a confirmed result is support navigation only |

---

## 0. Custody

Recomputed SHA-256 of the six required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `613a8fe989b8c1c34c5c6d3846054df52414bfebd172a56567bacb74e503455f` | named producer report; opened because it is charged; its `PASS` language is not evidence |
| `.../AWS_LAUNCH_METADATA.md` | `681214f474911c892cb39473d1ee75b4ad61258a065678060f09e10a7faf5602` | launch table; host/PID/RSS/swap were re-read from the run files, not from this page |
| `.../FREEZE.sha256` | `aeb01ce491aeb6596d031ba9a5cd7dccfa2b3cc97d85a012b6ae151f3eb66d7f` | source freeze (5 rows, all match) |
| `.../EVIDENCE.sha256` | `e3925672a81fea7e9403b85a46aa5651e8f196acf657d1a9dfcf85f2d824a85b` | evidence freeze (30 rows, all match) |
| `.../PRODUCER_FREEZE.sha256` | `97f66090720b6c26728af1b9d3a3ba6516f934507aa0f3209cda830e10dd4d4f` | four-row producer freeze, all match |
| `.../mine_support.py` | `0e94e5408b8a3b5db06c8eff5c759df1c75a2e8bb4563aa4964f42c39952fe9a` | named enumerator; inspected, not executed (AWS-only gate) |

Nested manifests, AWS absolute paths resolved to the local evidence copies:

| Manifest row | Local path | SHA-256 |
|---|---|---|
| Q `.../output/result.json` | `aws_q_box03/output/result.json` | `60b85c0393b3113984f2db1f1e15b87cc2296960a657e4d12d01662e59f8514f` |
| Q `.../output/support_inventory.json` | `aws_q_box03/output/support_inventory.json` | `373552623cf15658efbef868be26f54dadea7712d417f884ab9c39d5475f45ce` |
| P `.../output/result.json` | `aws_p65521_r6d/output/result.json` | `e956000027910c672528ec53470172d4f14829031e86efedf8abd6e760375df7` |
| P `.../output/support_inventory.json` | `aws_p65521_r6d/output/support_inventory.json` | `373552623cf15658efbef868be26f54dadea7712d417f884ab9c39d5475f45ce` |

The two inventory files are byte-identical. The two stdout streams are byte-identical (`822dd60039724eda238306a522624140e18b51fa1679713a1b2f773e7b41e9d1`). The two `result.json` files differ only in `registered_aws_lane` and `characteristic`. Nested manifest files themselves rehash to the evidence-list values `e1f3d687ee3b036e6d1ef452e8b79eb3ec9b51b3bf611c34a19384e57c89e8dc` (Q) and `4eb217e4216f396cd59ab1d7c11fc138f4911a1b8d81453b791f7c2f8fe244b9` (P).

The source archive pin `f8f1538c8ae29911c9df76cb1304c0ab5aee50b3f4720c8256021fbd6f11d218` is the same on both remote-archive rows and in launch registration. Freeze-check transcripts on both hosts rehash to `5a5d40b7f870233255e6ac7dfc6da766c3e4d2204f152b3d2b3e0795bd4c604e`.

---

## 1. Strict unique-`AC` inequalities

Work on the normalized integral unit-load unique-`AC` cell

```text
a = ord_sigma(A) >= 1,
r = ord_sigma(R) >= 2,
c = ord_sigma(C) >= 3,
d = c - a,          s = r - a >= 0,
d in {2,3},         a + 3 s > d.
```

The conditions `d in {1,2,3}` and `a+3s>d` are the unique-first-`AC` lower-hull requirements (competitors `A2`, `RC`, `R3` start strictly later). This census excludes `d=1` by a separately reviewed ladder and excludes `a>=10` by a separately reviewed high-contact source ceiling; neither exclusion is re-proved here. Equality faces `a+3s=d` are not strict unique-`AC` points.

For each `1<=a<=9` and `d in {2,3}` the independent minimum admissible `s` is

```text
s_min(a,2) = 1 if a <= 2 else 0,
s_min(a,3) = 1 if a <= 3 else 0,
```

i.e. `s_min = 1` if `a<=d` else `0`. Direct check of every integer `s>=0`:

| `a` | `d` | `s_min` | `r` | `c` | `a+3 s_min > d` | `r>=2` | `T=10+2a+2d` |
|---:|---:|---:|---:|---:|---|---|---:|
| 1 | 2 | 1 | 2 | 3 | 4>2 | yes | 16 |
| 1 | 3 | 1 | 2 | 4 | 4>3 | yes | 18 |
| 2 | 2 | 1 | 3 | 4 | 5>2 | yes | 18 |
| 2 | 3 | 1 | 3 | 5 | 5>3 | yes | 20 |
| 3 | 2 | 0 | 3 | 5 | 3>2 | yes | 20 |
| 3 | 3 | 1 | 4 | 6 | 6>3 | yes | 22 |
| 4 | 2 | 0 | 4 | 6 | 4>2 | yes | 22 |
| 4 | 3 | 0 | 4 | 7 | 4>3 | yes | 24 |
| 5 | 2 | 0 | 5 | 7 | 5>2 | yes | 24 |
| 5 | 3 | 0 | 5 | 8 | 5>3 | yes | 26 |
| 6 | 2 | 0 | 6 | 8 | 6>2 | yes | 26 |
| 6 | 3 | 0 | 6 | 9 | 6>3 | yes | 28 |
| 7 | 2 | 0 | 7 | 9 | 7>2 | yes | 28 |
| 7 | 3 | 0 | 7 | 10 | 7>3 | yes | 30 |
| 8 | 2 | 0 | 8 | 10 | 8>2 | yes | 30 |
| 8 | 3 | 0 | 8 | 11 | 8>3 | yes | 32 |
| 9 | 2 | 0 | 9 | 11 | 9>2 | yes | 32 |
| 9 | 3 | 0 | 9 | 12 | 9>3 | yes | 34 |

Eighteen pairs, eighteen minima, largest target `34`. No `(a,d)` in the rectangle is missing. The first integer points *excluded* from the strict cell, in lexicographic `(a,d,s)` order, are

```text
(1,2,0)  r=1<2 and a+3s=1<=2,
(1,3,0)  r=1<2 and a+3s=1<=3,
(2,2,0)  a+3s=2=d     (equality face),
(2,3,0)  a+3s=2<=3,
(3,3,0)  a+3s=3=d     (equality face).
```

None of those is a missing baseline of the census. Homogeneous `eta=sigma^u`, `u>=0`, raises `r` and therefore delays every `R`-bearing primitive; the `s=s_min` slice is the worst local-pole case of each block. `C^2` does not involve `R` and is invariant along the tail.

---

## 2. Atoms, summands, enumerator

The square octic is `f=K^2+sigma^5 D` with `K=L^2+sigma^2 R` and `D=L A+C`. Expanding,

```text
f = L^4 + 2 L^2 sigma^2 R + sigma^4 R^2 + sigma^5 L A + sigma^5 C
  = L^4 (1 + X),
X = 2 sigma^2 R/L^2 + sigma^4 R^2/L^4 + sigma^5 A/L^3 + sigma^5 C/L^4.
```

The four atoms of `X` are therefore

| atom | scalar | `sigma`-fixed | denom | `R` | `A` | `C` | effective grade cost |
|---|---:|---:|---:|---:|---:|---:|---|
| `R/L^2` | 2 | 2 | 2 | 1 | 0 | 0 | `2+r` |
| `R^2/L^4` | 1 | 4 | 4 | 2 | 0 | 0 | `4+2r` |
| `A/L^3` | 1 | 5 | 3 | 0 | 1 | 0 | `5+a` |
| `C/L^4` | 1 | 5 | 4 | 0 | 0 | 1 | `5+c` |

All four costs are at least `4` on the eighteen baselines, so the per-atom bound `floor(budget/cost)` is finite and the Cartesian product with `pad=0` already contains every tuple of grade `<=T`.

Weighted homogeneity of `wt(f)=8` with loads of weights `2,6,10` forces the four inverse-Faber summands

```text
f^{3/2} + sigma^4 k10 f^{5/4} + sigma^{12} k6 f^{3/4} + sigma^{20} k2 f^{1/4}.
```

Writing `f^alpha = L^{4 alpha} (1+X)^alpha`, a multi-index of total `X`-degree `n>=1` has pole order `denom - 4 alpha` (and `4 alpha in {6,5,3,1}` is an integer on every summand) and first grade

```text
summand.fixed + 2 n_R + 4 n_{R^2} + 5 n_A + 5 n_C + r e_R + a e_A + c e_C.
```

The coefficient is `C(alpha,n)` times the multinomial `n! / (n_R! n_{R^2}! n_A! n_C!)` times `2^{n_R}`. Combinations with the same `(e_R,e_A,e_C)` have the same `fixed` `2 e_R+5(e_A+e_C)` and the same denominator `2 e_R+3 e_A+4 e_C`, so they correctly share an aggregation key. Polar terms (`pole>0`) of grade `<=T` are retained; holomorphic companions (`pole<=0`) cannot acquire a `u`-pole at a simple root of squarefree `L`.

Independent remaining-budget DFS, the code's Cartesian product at `pad=0`, the same product at `pad=1` and `pad=2`, and the frozen inventory signatures agree on all eighteen blocks. The `pad=1` cutoff sentinel is therefore redundant completeness, not a hidden degree cap.

Zero-aggregation keys occur (23 across the eighteen blocks). They are identities, not truncated primitives. The model case is unloaded `R^2 C`:

```text
(n_R,n_{R^2},n_C)=(2,0,1):  C(3/2,3)*3*4 = -3/4,
(n_R,n_{R^2},n_C)=(0,1,1):  C(3/2,2)*2     = +3/4.
```

The sum is zero. Equivalently, with `y=sigma^2 R/L^2`, one has `(1+2y+y^2)^{3/2}=(1+y)^3`, which is cubic in `y` and has no `y^2 c` term at linear order in the `C` atom. The same square identity kills unloaded `R^4` (pole 2) and the other cancelled keys. Dropping them does not hide a local double pole.

Hand coefficients used as classification keys:

```text
C^2, unloaded, two C atoms:
  C(3/2,2) = 3/8.

R A^2, unloaded, one R-atom and two A-atoms:
  C(3/2,3)*3!*2 / (1! 2!) = (-1/16)*3*2 = -3/8.

k10 R C: C(5/4,2)*2*2 = 5/8.
k10 A^2: C(5/4,2) = 5/32.
k10 R^2 A, aggregated: -15/32 + 5/16 = -5/32.
k6 C: 3/4.
k6 R^2, aggregated: C(3/4,1) + C(3/4,2)*4 = 3/4 - 3/8 = 3/8.
k2 R: C(1/4,1)*2 = 1/2.
k2 A: C(1/4,1) = 1/4.
A^3: C(3/2,3) = -1/16.
```

All match the frozen inventory.

---

## 3. Correction-depth bound

Fix a polar primitive `P/L^q` of first grade `g` containing `e_A` copies of `A`. Set `h=T-g`. After the first `AC/L` allocation on squarefree `L0=(z-lambda)(z+lambda)`,

```text
A0 = alpha (z-lambda),   C0 = gamma (z+lambda),   alpha gamma lambda != 0.
```

In the local parameter `u=z-lambda` one has `A = alpha u + sigma A1(lambda+u)+cdots` with `A1` holomorphic, and `L0 = u(u+2 lambda)`. The `sigma^0` jet of `A^{e_A}` is `(alpha u)^{e_A}`. Replacing one factor `alpha u` by `sigma A1(lambda)` costs at least one sigma and loses at most one `u`-zero. After `h` corrections at most `h` of the `e_A` allocated zeros can be spent, so the remaining `u`-valuation of the numerator is at least `max(e_A-h,0)`, and the local pole order is at most

```text
q - max(e_A - (T-g), 0).
```

Three charges:

1. *Can losing an allocated root factor cost zero sigma?* No. The leading jet `A0` is allocated to vanish at this root, and it is linear. There is no `sigma^0` holomorphic-in-`u` summand of `A` at `u=0`. Vanishing of `A1(lambda)` can only make a replacement *more* expensive, which lowers the actual local pole.

2. *Do load or moving-`p` corrections invalidate the bound?* Load primitives are the other three binomial summands; they are enumerated as their own families, not as silent corrections of the unloaded expansion. In the Hensel local ring `L(sigma)=u(sigma) v(sigma)` with `v` a unit, `1/L^q` has exact local order `q`; moving `p` redefines the coordinate and does not add extra `u`-poles. Apparent `sigma/u` terms in the *original* coordinate are the moved simple root written in a stale parameter, not a larger local order at the allocated root. Inverse-Faber mixing and connection polynomials are not part of this miner; they are firewall-excluded.

3. *Is the formula only an upper bound?* Yes. Extra vanishing, coefficient cancellation after jet expansion, or displacement of `A0` along the moving root can only decrease the actual order. For `C^2` the bound is sharp: `e_A=0`, `C0(lambda)=2 lambda gamma != 0`, coefficient `3/8 != 0`, so the local order is exactly two at `T`. For every other family the census records a ceiling, not an attained Laurent coefficient.

The code clamps a negative value of `q-max(e_A-h,0)` to zero. Classification uses the predicate `>=2`, so the clamp does not change any dangerous/safe bit.

---

## 4. Eighteen canonical blocks

Independent DFS vs the frozen `support_inventory.json` (SHA-256 `373552623cf15658efbef868be26f54dadea7712d417f884ab9c39d5475f45ce`): every primitive signature — summand, load, `fixed_sigma`, `(R,A,C)`, pole, reduced coefficient, first grade, allocated-`A0` floor, local-pole upper bound — matches. Target `C^2` sits at grade `T` with coefficient `3/8` and local upper bound `2` on all eighteen blocks.

Dangerous families (`local pole upper >= 2`):

| `(a,d,s)` | class | dangerous families |
|---|---|---|
| `(1,2,1)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 16 |
| `(1,3,1)` | `NEGATIVE_RA2` | `-(3/8) R A^2/L^2` at 16, depth 2, alloc 0, local 2; and `(3/8) C^2/L^2` at 18 |
| `(2,2,1)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 18 |
| `(2,3,1)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 20 |
| `(3,2,0)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 20 |
| `(3,3,1)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 22 |
| `(4,2,0)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 22 |
| `(4,3,0)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 24 |
| `(5,2,0)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 24 |
| `(5,3,0)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 26 |
| `(6,2,0)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 26 |
| `(6,3,0)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 28 |
| `(7,2,0)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 28 |
| `(7,3,0)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 30 |
| `(8,2,0)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 30 |
| `(8,3,0)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 32 |
| `(9,2,0)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 32 |
| `(9,3,0)` | `SAFE_C2_ONLY` | `(3/8) C^2/L^2` at 34 |

Seventeen safe, one negative control. No first extra dangerous family.

RA2 timing `g=12+r+2a`, depth `2d-2-a-s`, local `2-max(2-depth,0)` when `g<=T`:

```text
(1,2,1): depth 0, alloc 2, local 0
(1,3,1): depth 2, alloc 0, local 2     <-- sole extra
(2,3,1): depth 1, alloc 1, local 1     <-- nearest RA2 miss
(3,3,1): depth 0, alloc 2, local 0
(4,3,0): depth 0, alloc 2, local 0
otherwise RA2 starts after T.
```

Other `q>=2` families that reach `T` keep at least one allocated `A0` or have local upper bound `0`:

- `(1,3,1)` `k10 R^2 A/L^2`, `q=2`, `e_A=1`, depth `0`, alloc `1`, local `1`.
- `(1,3,1)` `A^3/L^3`, `q=3`, `e_A=3`, depth `0`, alloc `3`, local `0`.
- `(9,3,0)` `k2 A/L^2`, `q=2`, `e_A=1`, depth `0`, alloc `1`, local `1`.

If the `A0` allocation were ignored, the first extra dangerous family would be `(1,3,1)` `k10 R^2 A/L^2`. It is not ignored. Higher-`s` tails only delay RA2, so they cannot create a second dangerous family that the baseline missed.

---

## 5. Dual AWS custody

| Field | Exact Q, Box03 | `F_65521` control, r6d |
|---|---|---|
| host | `ip-172-30-0-249` | `ip-172-30-0-45` |
| tag | `..._support_q_20260826_box03` | `..._support_p65521_20260826_r6d` |
| launcher PID | `242590` | `305367` |
| characteristic token | `0` | `65521` |
| start UTC | `2026-08-26T17:09:45Z` | same |
| timeout / VM cap | 600 s / `4194304` KiB | same |
| engine rc | `0` | `0` |
| wall / peak RSS / swaps | `0.08 s` / `18528` KiB / `0` | `0.08 s` / `18340` KiB / `0` |
| `time` exit status | `0` | `0` |
| inventory SHA-256 | `37355262…45ce` | same |
| stdout SHA-256 | `822dd600…e9d1` | same |
| stderr SHA-256 | `464a4abc…67f3` | `55984da0…4704` |
| source archive | `f8f1538c…d218` | same |

PIDs in `host_launcher.pid`, `launch_registration.txt`, and `AWS_LAUNCH_METADATA.md` agree per lane and differ across lanes. Swap lines are the literal `/usr/bin/time -v` field `Swaps: 0`; the wrapper rejects any `Swaps: [1-9]`. The validator string is recorded after those checks; it was not used as a calculation.

Both lanes execute the same `Fraction` enumerator. The `--characteristic` flag is stored in `result.json` and is not a modulus for the census. The only modular step is the software check that every dangerous coefficient is nonzero in `F_65521` (`3/8 ≡ 40951`, `-3/8 ≡ 24570`, and `65521` is prime). Exact `Q` is the support endpoint. The prime lane is not a proof and is not a second enumerator.

The miner prints `D1D23_SUPPORT_SOURCE_HASHES=PASS` as a constant. The actual freeze check is `sha256sum -c FREEZE.sha256` in `run_aws.sh` / `launch_host.sh` before the engine, and those transcripts rehash. That constant is not taken as evidence.

---

## 6. Firewall

A confirmed result of this miner is exact source support and a combinatorial local-pole *upper bound* at the allocated `A0` root, for the eighteen `a<=9`, `d in {2,3}` baselines and their `s>=s_min` tails. It licenses a complete-source/local-row-syzygy batch with seventeen putatively safe blocks and `(1,4,2)` as a required fail-closed negative control.

It does **not**:

- rebuild or identify the seven literal Faber rows,
- compute the actual local `u^{-2}` coefficient of any correction,
- prove truncated divisibility of the simple block,
- prove the first `AC/L` root allocation,
- prove emptiness of any of the seventeen safe cells,
- decide `(a,c,r)=(1,4,2)`,
- handle equality faces, unique `RC`, positive-order `k10`, `p=0`, `k0=0`,
- close D1, the square component, order two, maximum twelve, or JC2.

The high-contact `a>=10` ceiling and the `d=1` ladder are imported as the reason the residue is finite; they are not re-verified here.

---

## Strongest exact statement that survives

Over a field of characteristic zero, on the unit-load unique-`AC` chart with `1<=a<=9`, `d in {2,3}`, and `s>=s_min(a,d)` as in §1, every polar primitive of the four binomial source summands of first grade at most `T=10+2a+2d` is among the independently expanded families recorded in inventory `373552623cf15658efbef868be26f54dadea7712d417f884ab9c39d5475f45ce`. At the allocated `A0` root the combinatorial local-pole ceiling of each such primitive is `q-max(e_A-(T-g),0)`. Under that ceiling the only families with local pole order possibly at least two are the target `(3/8)C^2/L^2` on all eighteen blocks and `-(3/8)R A^2/L^2` on the single block `(a,d,s)=(1,3,1)`.

CONFIRMED
