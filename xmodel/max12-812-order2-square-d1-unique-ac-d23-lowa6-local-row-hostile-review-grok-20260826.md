# Hostile review — eleven low-`a` D1 unique-`AC` local-row obstructions

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_unique_ac_d23_lowa6_local_row_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest omitted or misclassified baseline | none |
| Smallest hidden source monomial | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers, the support-miner census PASS, and prior V5 wording are not authority |
| Method | SHA-256 of every named pin, nested compiled manifest, and evidence file; independent unique-`AC` inequalities; independent four-summand binomial expansion through each `T`; compiled-script inspection of every `H`, Faber bridge, moving recurrence, Hensel root, orientation, `E` correction, and AWS record. No Singular, Sage, msolve, or Lean replay |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the seven required primary pins match. Every path named in `FREEZE.sha256` (23 rows), `EVIDENCE.sha256` (54 rows), and `PRODUCER_FREEZE.sha256` (5 rows) rehashes to the printed digest. All four nested `compiled.sha256` files rehash to the retrieved `.sing` and `source_inventory.json`. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

On the registered square/D1 chart `D(p*k0)`, after the cited upstream gates, each of the eleven strict unique-`AC` contacts

```text
a=ord(A) in {1,...,6},  d=ord(C)-a in {2,3},
s_min=1 if a<=d else 0,  ord(R)>=a+s_min,
```

other than `E=(1,3,1)`, has complete seven-row source of global pole order at most two through

```text
G=10+2*a+d,  T=10+2*a+2*d.
```

`AC/L` is the unique first polar primitive. Its numerator forces the two opposite-root allocations of nonzero linear `A0,C0` on squarefree `L=z^2+p/2`. The moving `L^2` numerator evaluated at either Hensel root is

```text
N(lambda)=Phi4+lambda*(Phi3+(p/4)*Phi1),
```

identically zero in grades `G,...,T-1`, and equal to `(3/2)*lambda^2*gamma^2` at grade `T`. That coefficient is a unit on `D(p*gamma)`. Rows 1, 3, and 4 are target-free through every listed ceiling, so the three full rows in the identity cannot vanish. Finite etale descent from the root cover empties the unsplit exact-contact chart, including the closed-`R` tail. The mandatory control `E` has global pole ceiling three; its isolated `RA^2/L^2` grade-18 second correction is the displayed formula, and it is routed with no emptiness or nonemptiness verdict.

The six cells `a=7,8,9` with `d=2,3`, their grade-32/34 row-4 targets, and JC2 are outside this producer.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Seven primary pins | hashes | all seven match the required bytes |
| 0. Named manifests | every named file | `FREEZE` 23/23, `EVIDENCE` 54/54, `PRODUCER_FREEZE` 5/5, four nested `compiled.sha256` 2/2 each |
| 1. Unique-`AC` list | `d=2,3` inequalities, `s_min`, eleven positives plus `E` | **holds**; first omitted/misclassified baseline: none |
| 2. Four binomials | atoms, cost bounds, pad+1, aggregation, jets, delayed loads, seven tails, targets | **holds**; cancelled `R^2 C` / `R^4` keys are genuine zeros, not hidden monomials |
| 3. First `AC/L` and pole two | unique first, global pole `<=2` through `T`, Laurent/literal bridge, sigma quotients | **holds** on every positive block; `E` is pole three |
| 4. Recurrence and roots | `N=.../L^2`, identity `(1)`, moving `p`, Hensel, both orientations, exhaustiveness | **holds** |
| 5. Grade-`T` coefficient | `(3/2)lambda^2 gamma^2`, earlier vanishing, rows 1/3/4, scheme-theoretic empty chart, closed `R` | **holds** |
| 6. Control `E` | pole three, actual `RA^2` grade-18 correction, routing only | **holds**; no empty/nonempty verdict |
| 7. AWS / V3 | distinct hosts, archive/freeze, rc, diagnostics, caps, zero swap, V3 parser/no-verdict | **holds** |
| 8. Firewall | no `a=7` tie, no `a=8,9` load-first, no grade-32/34 row-4, no JC2 | **holds** |

---

## 0. Custody

Recomputed SHA-256 of the seven required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `04324859fac936e4bca2e114e259d7bcf444491c21d905219a9490deb3dab012` | producer report |
| `.../AWS_LAUNCH_METADATA.md` | `0e46aa910f4755f5534aa9a71a16ac1a9455e20154d09348b6464546ed8663f4` | AWS metadata |
| `.../FAILED_ATTEMPTS.md` | `f6f841e3dbb134a41019071b7cc79b054488387bab11a58310bfb36fd5842f88` | quarantined attempts |
| `.../EVIDENCE.sha256` | `ba45fe4151eccf4644e23dc21fb8dda0d0957780a77a5c615a8cc70c19efb3f4` | evidence freeze |
| `.../FREEZE.sha256` | `5faefef61a58f3121a605a83fe2e35af6fff37857ee8649dba33be3e18acbe07` | source freeze |
| `.../PRODUCER_FREEZE.sha256` | `4d69b97d8c6e24baadc76aba69d3d37158a3aa466cf7e44bc3111008c5a07fd3` | producer freeze |
| `.../compile_local_row.py` | `b2fe07fdd2f855598dde5c6ef9828909c94496eb5e196756eff504056cde2769` | compiler |

`FREEZE.sha256` names 23 files, all matching, including the imported r1/d1 compiler and freeze, the support miner, `compile_cge3_universal.py`, `tails.json` `d72f774c…`, `compile_square_load_ladder.py`, and the five named xmodel pins. `PRODUCER_FREEZE.sha256` repeats the five producer documents and matches. `EVIDENCE.sha256` names 54 files (V5 dual, V7 dual, and the quarantined V3 preflight); all 54 rehash.

Nested `compiled.sha256` on all four AWS lanes rehash. V7 exact-Q and `F_65521` stdout are byte-identical (`ad447f4d…`). V7 compiled scripts are characteristic-normalized equal: the only difference is the twelve ring-characteristic tokens `0` versus `65521` (48-byte size gap 1885463 versus 1885511). Compiler stderr is the empty digest `e3b0c442…` on every compiled lane, including V3.

A passing sentinel is not mathematics. The algebra below is independent of those sentinels.

The `/tmp` source archive `7f0cab79…` recorded in `AWS_LAUNCH_METADATA.md` was not retrieved. Both V7 hosts record that same archive hash and a passing on-host `FREEZE` check. The repository freeze and the 54 evidence files are the custody used here.

---

## 1. Unique-`AC` inequalities and the eleven-plus-`E` list

The frozen lower-hull comparison, after subtracting the common absolute grade ten, has unique-`AC` interior

```text
1 <= d := c-a <= 3,   s := r-a >= 0,   a + 3s > d.
```

Relative gaps from the first `AC` weight `a+c` are `C2: d`, `A2: 4-d`, `RC: 1+s`, `R3: a+3s-d`. The domain constraint `r>=2` forces `s_min=1` whenever `a=1`. Minimality of `s` is the first integer `s>=0` with `a+3s>d` and `a+s>=2` when that is required by `r>=2`.

For `d in {2,3}` this is exactly

```text
s_min = 1 if a <= d else 0,   r_floor = a + s_min.
```

The eighteen integer points with `1<=a<=9` are the miner box. Restricting to `a<=6` gives twelve baselines. Unique first polar among them fails only at `(a,d)=(1,3)` for a later local double pole, not for first-grade uniqueness; that is `E`, retained as a control. The eleven positives are

| `a` | `d` | `s_min` | `r>=` | `G` | `T` |
|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 1 | 2 | 14 | 16 |
| 2 | 2 | 1 | 3 | 16 | 18 |
| 2 | 3 | 1 | 3 | 17 | 20 |
| 3 | 2 | 0 | 3 | 18 | 20 |
| 3 | 3 | 1 | 4 | 19 | 22 |
| 4 | 2 | 0 | 4 | 20 | 22 |
| 4 | 3 | 0 | 4 | 21 | 24 |
| 5 | 2 | 0 | 5 | 22 | 24 |
| 5 | 3 | 0 | 5 | 23 | 26 |
| 6 | 2 | 0 | 6 | 24 | 26 |
| 6 | 3 | 0 | 6 | 25 | 28 |

No `a<=6` unique-`AC` `d=2,3` cell is omitted. The first excluded equality face is `(a,d,s)=(3,3,0)`, where `a+3s=d` and `R3` ties `AC`; it is not unique-`AC`. The first excluded load exception is `a=7`, where `k6*C/L` ties `AC/L` at grade `10+2*7+d`. Neither belongs in this list. `E=(1,3,1)` is present and classified negative. First omitted or misclassified baseline: none.

The source writes `R=sigma^{r_floor}*(b1+t*b0+jets)` and does not invert `b0,b1`. That is the closed tail `ord(R)>=r_floor`, not only the exact-order slice.

---

## 2. Four binomial summands, cost bounds, aggregation, jets, tails, targets

The square source is `f=K^2+sigma^5 D` with `K=L^2+sigma^2 R` and `D=L A+C`. Factoring `f=L^4(1+x)` with

```text
x = 2 sigma^2 R/L^2 + sigma^4 R^2/L^4 + sigma^5 A/L^3 + sigma^5 C/L^4
```

gives four atoms of costs `(2,4,5,5)` in `sigma` and denominators `(2,4,3,4)`. The four load summands are the binomial series of

```text
f^{3/2},   sigma^4 k10 f^{5/4},   sigma^{12} k6 f^{3/4},   sigma^{20} k2 f^{1/4},
```

i.e. alphas `3/2, 5/4, 3/4, 1/4` with load weights `Lambda^{2,6,10}` after `Lambda=sigma^2`. Pole order is `denominator - 4 alpha`. These alphas and weights are the frozen load-ladder generating function, not a miner-only convention.

Independent expansion through each `T`, with atom bounds `budget // cost` and with one extra count in every atom direction, produces identical retained signatures. Every positive atom cost is at least 2, so a degree-(bound+2) tuple already exceeds `T`. There is no cutoff hole.

Aggregation by `(summand, load, fixed, eR, eA, eC, pole)` produces genuine zeros, typically

```text
(unloaded, fixed=9, R=2, C=1, pole=2)     # two type-1 R plus C versus one type-2 R plus C
(unloaded, fixed=8, R=4, pole=2)          # four type-1 R versus two type-2 R
```

with binomial coefficients `-3/4+3/4=0`. Those monomials are absent from the source, not hidden by cancellation. No cancelled key reappears with a nonzero coefficient after padding.

Jet ceilings are `T - first_grade` over primitives carrying that stem. Compiled rings match: `pmax=d` on positives (`3` on `E`); `A,C` jets equal `d`; `mu2max=max(T-28,0)`, `mu4max=max(T-32,0)`; `k2` first appears in-window only for `(6,3)` at grade 28, as the leading `k20` with no extra jet. Delayed loads in the literal tails are the frozen weights `(sigma^2)^2 k10`, `(sigma^2)^6 k6`, `(sigma^2)^10 k2`.

Every compiled `H` contains exactly the independently enumerated primitives, with the same coefficients and `sigma` prefixes. Samples:

- `(1,2)`: six terms, `AC 3/4`, `k R^3 5/16`, `k RC 5/8`, `k A^2 5/32`, `C^2 3/8`, `RA^2 -3/8`;
- `E`: those plus `k R^2 A -5/32` and `A^3 -1/16` (`Inv3`);
- `(6,3)`: eight terms including `k6 C 3/4`, `k6 R^2 3/8`, and `k2 R 1/2`.

`t`-power is `1+2q-eR-eA-eC`, the overall extra `t` plus `t^{2q}` from `L^{-q}` minus one `t` per linear `z`. Inverse series are `(1+(P/2)t^2)^{-q}` through `t^8`, which is exactly `[t^8]=h7`. Extra `t^{10}` cannot enter the seven rows.

Literal rows are `tail_text` of frozen `tails.json` (seven rows, 36/54/58/81/89/120/131 monomials, canonical digest `6eed03d4…`), with `Lambda -> sigma^2` and target subtractions

```text
row 1,3,5: 0
row 2: sigma^{28} mu20
row 4: sigma^{32} mu4
row 6: sigma^{36} mu6
row 7: sigma^{38} (J/4)
```

on every block. `SourcePhi` begins with the delayed-load tail monomials, not with a handwritten polar list. Through `T<=28` the only in-window target is `mu2` at grade 28 in row 2, and only for `(a,d)=(6,3)`.

---

## 3. Unique first `AC/L`, pole ceiling two, bridge, quotients

For every `a<=6` and `d in {2,3}`, the unique primitive of least grade is unloaded `AC` at `G=10+2a+d`, coefficient `3/4`, pole 1. Independently: `k6 C` sits `7-a` grades after `AC`, hence strictly later for `a<=6`; `k2 C` sits `15-a` later; `C^2` sits `d` later; `RA^2` sits `a+s+2-d` later, which is at least 2 on these floors.

Global pole through `T` is 2 on every positive block. The only pole-3 primitive in the twelve compiled baselines is unloaded `A^3` on `E` at grade 18, local pole 0 after allocating three `A` zeros. Compiled `GLOBAL_POLE_CEILING` is 2 on the eleven positives and 3 on `E`.

The first `AC` numerator identity, with `h_j=[t^{j+1}]H` and `Inv1=1-(p/2)t^2+O(t^4)`, is

```text
Nfirst = h1 z + h2
       = (3/4)*((a1 c0+a0 c1)z + a0 c0 - (p/2) a1 c1),
```

which is `A0 C0` reduced modulo `L=z^2+p/2`. Compiled `NfirstExpected` is this polynomial.

The analytic-Laurent/literal bridge is coefficientwise `SourcePhi_j - T_{j*}(P) h` modulo `sigma^{T+1}`, with moving

```text
P = p + 2 sigma ell1 + ... + 2 sigma^{pmax} ell_{pmax}
```

and the frozen `T_{ij}` of `compile_cge3_universal.py`:

```text
Phi1=h1
Phi2=h2
Phi3=h3+(P/4)h1
Phi4=h4+(P/2)h2
Phi5=h5+(3P/4)h3+(3 P^2/32)h1
Phi6=h6+P h4+(P^2/4)h2
Phi7=h7+(5P/4)h5+(15 P^2/32)h3+(5 P^3/128)h1.
```

Every powered numerator is parenthesized; V3's `P^2/32` parsed as `P^(2/32)` is not present. Recursive sigma quotients divide `FullPhi_j` by `sigma^G`, then peel one `sigma` at a time through `T`, requiring each remainder to be in `(sigma)` and the reconstruction identity `sigma^{G} Q_G = FullPhi`. Those are the exactness flags, not boolean decorations.

If a polar monomial were missing from `H` but present in the tails, the bridge would fail. If a jet ceiling were too small, the tails (which substitute the same truncated series) could agree with `H` while both being incomplete; pad+1 plus strictly positive atom costs close that cut. No in-window monomial is missing from compiled `H`.

---

## 4. Moving pole-two recurrence, identity `(1)`, Hensel, exhaustiveness

For global pole at most two, `H=N/L^2` with `deg N <= 3`. The extra-`t` packing gives

```text
n3=h1, n2=h2, n1=h3+P h1, n0=h4+P h2,
```

because `[t^2]Inv2=-2*(P/2)=-P`. Hence

```text
N = h1 z^3 + h2 z^2 + (h3+P h1)z + (h4+P h2).
```

The three recurrences `h_{k+4}+P h_{k+2}+(P^2/4)h_k=0` for `k=1,2,3` are `(z^2+P/2)^2` acting on `H`, compiled as `Rec5,Rec6,Rec7` modulo `sigma^{T+1}`. They are the pole-two certification. `E` does not run them.

At a root `lambda^2=-P/2`,

```text
N(lambda) = h4+(P/2)h2 + lambda (h3+(P/2)h1).
```

The frozen connection is `Phi4=h4+(P/2)h2`, `Phi3=h3+(P/4)h1`, `Phi1=h1`, so

```text
N(lambda)=Phi4+lambda*(Phi3+(P/4)Phi1).            (1)
```

This is an identity of power series in `sigma`, not a grade-by-grade approximation. Compiled `Psi` is `(1)` on `SourcePhi`, with moving `lambda(sigma)=lam+sigma rho1+...` and moving `P`.

Hensel: `(lam+sigma rho1+...)^2 + P/2` is expanded in `sigma`. The constant term is `lam^2+p/2`, checked separately and imposed by `subst(p,-2*lam^2)`. Higher coefficients do not contain `p`; they are `2 lam rho1+ell1`, `rho1^2+2 lam rho2+ell2`, …, and generate `RootIdeal` together with `ilam*lam-1`. Both orientations substitute before reducing by that ideal.

Opposite-root maps, `lam^2=-p/2`:

```text
plus:  A0=au(z-lam), C0=cv(z+lam), evaluate (1) at +root
minus: A0=au(z+lam), C0=cv(z-lam), evaluate (1) at -root.
```

Exhaustiveness on `D(p)` with linear `A0,C0`. Squarefree `L` has two distinct roots. `Nfirst=0` if and only if `L` divides `A0 C0`. A degree-`<=2` polynomial divisible by a squarefree quadratic is a unit times `L`, so both forms have degree exactly one and vanish at complementary roots. They cannot share a root: that would square `L` and force `p=0`. A nonzero constant cannot be a complementary factor of `L`. The remaining possibilities are exactly the two maps. Exact `ord(A)=a` excludes `A0=0`; exact `ord(C)=a+d` excludes `C0=0`.

---

## 5. Grade-`T` local coefficient, targets, scheme, closed `R`

After either map, leading `C0=cv(z\mp lam)`. The unique local double pole at grade `T` on every positive block is unloaded `C^2/L^2`, coefficient `3/8`, from the leading section of `C`. Its `L^2` numerator is `(3/8)C0^2`. At the `A`-allocated root this is

```text
(3/8) cv^2 (2 lambda)^2 = (3/2) lambda^2 cv^2.
```

The same value appears on both decks. It does not depend on `d`: `C^2` always first arrives at `T=10+2c` from leading `C`.

Every other in-window family is globally pole 1, or globally pole 2 with enough allocated `A` zeros that the local pole at the `A`-root is at most 1 through `T`. A global simple pole, rewritten over `L^2`, is `N_s L`, which vanishes at either moving root. A leftover `RA^2` or `k R^2 A` with allocated `A` zeros likewise vanishes there. Consequently all coefficients of `(1)` in grades `G,...,T-1` vanish as polynomials after the maps and `RootIdeal`, and the grade-`T` coefficient is exactly `(3/2)lambda^2 gamma^2` with `gamma=cv`. Characteristic zero supplies `2,3`.

Independent local-pole census of the eleven positives: the unique family with local pole `>=2` at the `A`-root is `C^2` at `T`. That is a support upper bound; the actual coefficient is the expansion above, not the bound.

Rows 1 and 3 have target `0` identically (`FullPhi=SourcePhi-(0)` on all twelve blocks). Row 4 subtracts `sigma^{32} mu4`. Every positive `T` is at most 28, so row 4 is target-free modulo `sigma^{T+1}`. The only grade-28 target is `mu2` in row 2, which is absent from `(1)`. Compiled `Psi` uses `SourcePhi`, not `FullPhi`; the two agree on rows 1, 3, 4 through every positive ceiling.

Scheme-theoretic emptiness of the exact-contact chart. Grade `G` of the seven rows is equivalent to `Nfirst=0`. On `D(p*k0*gamma)` with exact `ord(A)=a` and exact `ord(C)=a+d`, that forces the two opposite-root maps on the etale cover `lambda^2=-p/2`. After those maps, `(1)` equals `sigma^T` times a unit in the truncated ring modulo `sigma^{T+1}`. The three full rows in `(1)` therefore generate the unit ideal in the `T`-jet (and there is no formal arc: the lowest term is a unit). The cover is finite etale of degree two on `D(p)` because the discriminant is a unit times `p`. Emptiness descends to the unsplit chart. This is emptiness of that localized jet/formal chart, not a claim about associated primes of an unlocalized ideal.

Closed-`R` tail. Leading `b0,b1` are not inverted. Raising `ord(R)` delays every `R`-family and cannot create an earlier local double pole. The obstruction `(3/2)lambda^2 gamma^2` is independent of `R`. The compiled floor with uninverted leading `R` is the whole tail.

Inverted: `p` (via `lam`), `gamma=cv`, and the chart unit `k0`. Not inverted: leading `R`, `au` (the obstruction does not use it; exact `a` is `D(au)` inside the maps), `ell`, `rho`, `k6`, `k2`, targets. `k0` is the registered D1 chart even when `k10` is delayed out of the window.

---

## 6. Control `E=(1,3,1)`

`E` has `G=15`, `T=18`, `r>=2`, eight primitives, global pole 3 (`A^3/L^3` at grade 18, local pole 0). Two families have local pole `>=2` at the `A`-root: `C^2` at 18 and `RA^2` at 16 with depth 2, so both allocated `A` zeros can be lost. The pure pole-two endpoint is correctly refused.

Isolated `H_RA2=-(3/8) sigma^{12} t^2 R A^2 Inv2`. After the plus allocation `a1=au`, `a0=-au lam` and evaluation of the `L^2` numerator at the moving root,

```text
A(root) = sigma^2 (lam a1_1 + a0_1 + au rho1) + O(sigma^3),
R(root) = sigma^2 (b1 lam + b0) + O(sigma^3).
```

The naive grade-16 term is leading `R A0^2` and vanishes at the `A`-root. Grade 17 has odd extra order and vanishes. Grade 18 is

```text
-(3/8)(b1 lambda+b0)(lambda a1_1 + a0_1 + au rho1)^2
```

modulo the Hensel ideal. Compiled `RA2ExpectedRed` is this polynomial, compared after reducing both sides. First two local coefficients are required to vanish. This reconstructs the second correction; it does not solve the seven rows and does not decide emptiness or nonemptiness.

V5 printed `NEGCTRL_GLOBAL_POLE3=1` and routed `E` without this coefficient. V7 supersedes V5. Frozen custody is V7.

---

## 7. AWS custody and preserved V3

| | exact Q | `F_65521` control |
|---|---|---|
| host | Box03, `ip-172-30-0-249` | r6d, `ip-172-30-0-45` |
| tag | `..._v7_q_20260826` | `..._v7_f65521_20260826` |
| launcher PID | 249616 | 313357 |
| characteristic | 0 | 65521 |
| start | 2026-08-26T17:50:46Z | same |
| engine end | 17:50:57Z | 17:50:53Z |
| timeout / VM cap | 1800 s / 33,554,432 KiB | same |
| engine rc | 0 | 0 |
| wall / peak RSS | 11.13 s / 2,486,060 KiB | 7.62 s / 1,961,792 KiB |
| swaps | 0 | 0 |
| compiled SHA-256 | `d05e9da8…` | `5a029019…` |
| stdout SHA-256 | `ad447f4d…` | same |
| compiler stderr | empty | empty |

GNU `time -v` is the only engine-stderr content. No `error occurred`, no `=FAIL`, no nonzero swap. Distinct hosts, distinct PIDs, same archive hash `7f0cab79…`, passing on-host freeze. Exact Q is the characteristic-zero endpoint; `F_65521` is a second host/software control (`2` and `3` are units). `launch_host.sh` refuses a non-matching archive hash, a non-fresh job directory, and a non-AWS host.

V3 is a parser failure, not a mathematical verdict. Powered moving-`p` was inserted unparenthesized; Singular diagnosed `` `polyBucket` ^ `number` failed `` on `P^2/32` parsed as `P^(2/32)`, printed `error occurred`, left `B12_PredPhi5` undefined, and still returned process status 0 (`Exit status: 0` in GNU time). It continued far enough to print empty `MOVING_L2_RECURRENCE=` and a dangling `ENDPOINT` attempt. V3 was preflight-only and was never dual-launched. The frozen validator greps stdout and stderr for `error occurred` and `=FAIL`, requires eleven `PASS_EMPTY_CLOSED_R_TAIL` lines, the `E` second-correction marker, and the high-`a` routing line. V3 would not pass that validator. Preserved hashes match `FAILED_ATTEMPTS.md` and `EVIDENCE.sha256`.

---

## 8. Firewall

This producer closes exactly the eleven named `a<=6` strict unique-`AC` `d=2,3` closed-`R` tails after the registered upstream gates. Independently:

- `a=7`: `k6 C` and `AC` both at grade `10+14+d`, coefficients both `3/4`. Tie. Excluded.
- `a=8,9`: `k6 C` is first (`7-a<0`). Load-first. Excluded.
- Row-4 target `sigma^{32} mu4` first meets a `d=2,3` ceiling at `T=32` (`a=8,d=3`) and `T=34` (`a=9,d=3`). Those shadows are not in this window.
- `E` is routed, not decided.
- Equality faces, positive-order leading load, `p=0`, `k0=0`, another D1 face, a terminal/global chart, the square component, order two, `(8,12)`, maximum twelve, and JC2 are not this claim.

Compiled high-routing marker is `A7_TIE_A8_A9_LOAD_FIRST_EXCLUDED`. Nothing here may be imported through those six cells or to JC2.

---

## Verdict

**CONFIRMED**
