# Hostile different-model review — maximum-12 partial-`y` Kummer preflight

| Field | Value |
|---|---|
| Claim under review | Frozen producer preflight: starting only from the reviewed shear/UFD history, the primitive maximum-12 cells are `(8,12)` and `(9,12)` with history residues `4\|H` and `3\|H` (including `H=0`); the exact next Jacobian row is `d u^(d(r+s)-1)(sA-rB)'`; the depression `z=uy+A/m` has second mismatch `-delta/r`; the Kummer split of the leading core has orders `4,2,1` and `3,1`, with `delta` forced to zero on every nontrivial order including the proper order-two class inside `d=4`; all original `y=0` Taylor boundaries stay charged; the conditional binary gate `W=r f g_z - s f_z g` has the exact common-power locus `(K^r,K^s)`, `deg K=d`, and route identity `f D'-s f' D=-W g^(r-1)`; the depressed constant-W tangent data at `K=z^d+z+1` are `18/17/11/7` and `19/18/11/8`; two cost metrics point in opposite directions and no overall cheaper cell is asserted. Out of scope by registration: high-row Faber landing, constant-W component classification, emptiness of either cell, maximum-12 coverage, JC2 |
| Overall verdict | **CONFIRMED** at the registered scope, on the audited bytes |
| Smallest missing hypothesis | none that breaks a registered claim. Non-blocking: (i) the class order in the Kummer split must be the monic-core (divisor) order — the producer's own target scalings supply a monic `h`, and the replay computes exactly the divisor order; with a non-monic core there is an explicit nonzero weight-one `delta` shape (Claim 3); (ii) "residual exactly when `3\|H`" is exact at the level of `H`-classes; at pair level the frozen inputs additionally close the `H=0` sub-stratum with all coefficient `x`-degrees `<=1`, via the `L=2` shear onto total gcd `6=2*3` and the frozen GGV `2p` theorem — no analogous corner exists for `(8,12)` (Claim 1); (iii) byte-level digest recomputation and the replay rerun were not executable in this review environment (see Execution environment) — this is a process limitation, not a discovered defect |
| Evidence tier | independent full hand re-derivation of every registered identity: the `y^(m+n-2)` row with all four terms and the exact logarithmic cancellation, `delta=sA-rB`, the depression and `-delta/r` mismatch, the Kummer degree-equals-class-order lemma with proof, the constant-field lemma for monic cores, the order-two `d=4` leaf, all five divisor examples, both boundary jet families, Euler/Wronskian `(4.1)`, the common-power equivalence `(4.2)`, the route identity `(4.3)`, and a closed-form structural proof of both tangent ranks and kernels (kernel `= m-1`, rank `= n-1`); byte-level read of every frozen payload and both frozen history inputs in full; line-by-line audit of `replay.py` with every internal check independently re-proved; textual hash-chain verification across four documents; no producer script or PASS string used as evidence |
| Reviewer / model | Claude Fable 5 (Anthropic). Different model family from the producer (OpenAI Codex, GPT-5 family) and from the prior history reviewer (Grok 4.6, xAI) |
| Repo | `/Users/dc/code/math/jc2` |
| Launch basis | `1e60fcedc8626650c7c7544ad296c3624173415f` (snapshot HEAD at review start; matches the launch prompt) |
| Tree state observed | via direct `.git` reads: `master` advanced during the live session to `7832fb73ac887041968f9cec2dc6cba7aa0d0bcf` through `5690389…` ("promote partial-y degree eleven theorem and AS controls"), `4cc665e…` ("record post-composition live state"), `7832fb7…` ("Harden p-adic residual provenance gate"). None of the three names this case. All audited bytes were read from the working tree and match the frozen textual chain. The mid-session maximum-eleven promotion is **not** consumed by this review |
| Review window | 2026-08-24, single session; wall-clock timestamps and host/Python identifiers unavailable without a shell |

Producer and provenance inputs read in full before any verdict:

- `xmodel/max12-partial-y-kummer-preflight-20260824.md`
- `cases/max12_partial_y_preflight_20260824/REGISTRATION.md`
- `cases/max12_partial_y_preflight_20260824/replay.py`
- `cases/max12_partial_y_preflight_20260824/MANIFEST.sha256`
- `cases/max12_partial_y_preflight_20260824/FREEZE.sha256`
- `xmodel/as109-partial-y-history-stop-20260824.md` (frozen theorem input, reread in full)
- `xmodel/as109-partial-y-history-review-grok-20260824.md` (frozen confirmation, reread in full)

The case directory contains exactly the four listed files (verified by directory listing). No enumerator, exponent rectangle, or AWS helper is present. No producer, case, canonical, ladder, coordination, prompt, log, run, or erratum file was edited. The only file written by this review is this report, plus an unexecuted checker script outside tracked paths (`/tmp/max12_review_claude/independent_checks.py`).

---

## Execution environment — read this before consuming the verdict

This review session had **no command execution capability of any kind**: no shell tool, the Monitor fallback was permission-denied in "don't ask" mode, subagents inherited the same restriction, and no peer session was reachable. Consequences, stated exactly:

1. `shasum -a 256 -c cases/max12_partial_y_preflight_20260824/FREEZE.sha256` was **not run**. No SHA-256 digest in this review was recomputed from bytes.
2. `python3 cases/max12_partial_y_preflight_20260824/replay.py` was **not rerun**, so the payload digest `eb1e72d6…` and the PASS strings were not reproduced.
3. Everything mathematical was instead verified by complete independent hand derivation, at a strictly stronger evidence level than a rerun: every check the replay performs is re-proved below, and both tangent ranks are proved in closed form rather than re-eliminated.

**Banking precondition.** Before this review is banked, a shell-bearing session must run the two frozen commands above unmodified and observe (a) all four `OK` lines from the freeze check, and (b) replay exit 0 with terminal line `payload_sha256=eb1e72d69193cded40438981907f62972725945c39a18e34891dd8f5b3645bf1`. If either fails, the byte custody is breached and this review's CONFIRMED transfers only to the exact contents quoted and derived herein, not to the on-disk files. A prepared independent checker (list-based polynomial arithmetic, independent elimination plus a mod-`1000003` rank cross-check, and all instance checks below) is at `/tmp/max12_review_claude/independent_checks.py`, unexecuted.

Given the audit below, a rerun of `replay.py` on the audited bytes has exactly two possible outcomes: failure at the input-hash pinning step (custody breach), or the advertised PASS output — every other `PreflightFailure` branch is proved unreachable in Claims 1–6.

---

## Hashes and custody

No digest was recomputed. The textual chain was verified character-for-character across independent documents:

| Artifact | Frozen SHA-256 | Textual cross-checks that agree |
|---|---|---|
| `xmodel/max12-partial-y-kummer-preflight-20260824.md` | `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07` | launch prompt; `FREEZE.sha256` line 3; `MANIFEST.sha256` line 3 |
| `cases/…/REGISTRATION.md` | `c6562834437aed42b61207c215a9d8196cf33d297f0a94503f42e4204caaf18a` | launch prompt; `FREEZE.sha256` line 1; `MANIFEST.sha256` line 1 |
| `cases/…/replay.py` | `9239addecd3db4c2b5c656d8c1625d2761ab61bd83930ac17f926432a4da2cb4` | launch prompt; `FREEZE.sha256` line 2; `MANIFEST.sha256` line 2 |
| `cases/…/MANIFEST.sha256` | `ac686b584b93e1b5bf69f36402c4f99deeec0ec8d7557704053531e7619aa13d` | launch prompt; `FREEZE.sha256` line 4 |
| `cases/…/FREEZE.sha256` | `59ef0712aea2424ea57b6f1727031018e769701b0f2e2384eb4638f4286ea558` | launch prompt only (self-hash; no in-tree cross-source exists by construction) |
| replay payload (stdout) | `eb1e72d69193cded40438981907f62972725945c39a18e34891dd8f5b3645bf1` | launch prompt; `REGISTRATION.md` §Replay |
| `xmodel/as109-partial-y-history-stop-20260824.md` | `6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe` | report §1; `REGISTRATION.md`; `replay.py` `EXPECTED_HASHES`; header of the landed Grok history review, which states it recomputed this digest |
| `xmodel/as109-partial-y-history-review-grok-20260824.md` | `f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd` | report §1; `REGISTRATION.md`; `replay.py` `EXPECTED_HASHES` |

`MANIFEST.sha256` is verbatim the first three lines of `FREEZE.sha256`, as required. The audited bytes of all seven artifacts were read in full through the file API; the mathematical audit below applies to those exact bytes.

---

## Promotion

**Accept the preflight at its registered scope**, subject to the banking precondition above:

- The primitive maximum-12 cells under the frozen history are exactly `(8,12)` and `(9,12)`; the still-unclosed `H`-classes are exactly `4|H` and `3|H`, including `H=0`, with the pair-level corner precision of Claim 1.
- The exact next row, `delta=sA-rB`, the depression `z=uy+A/m`, the mismatch `-delta/r`, the Kummer orders `4,2,1` / `3,1`, forced `delta=0` on every nontrivial order (monic core), retained parity-only weights on the order-two leaf, and all charged Taylor boundaries.
- The conditional binary-W algebra `(4.1)`–`(4.3)` and the exact tangent data `18/17/11/7` and `19/18/11/8`, now proved in closed form.
- The two-metric comparison exactly as stated: raw first gate smaller for `(8,12)`, Kummer branch tree simpler for `(9,12)`, and **no** ordering of whole-cell cost.

**Do not promote this to:** a high-row Faber reduction or landing for either cell; a constant-W component classification; emptiness of either cell; maximum-12 coverage or automorphy; an arbitrary-support statement; a constructed pair or counterexample; or any JC2 inference. None of these is claimed by the producer, and none is licensed by this review.

---

## Quarantine

No result here proves or disproves JC2. No PASS string was consumed as evidence; the replay was not even run. The maximum-eleven composition artifacts (promoted to `master` mid-session) and every `(6,9)` exclusion remain strictly outside the input set: the routing of Claim 1 was reconstructed from the two frozen history artifacts alone, and Section 5 of the report imports only method *shapes*, never conclusions. The Kummer forcing is quarantined to the monic-core (divisor) class order per Claim 3. The tangent ranks are local linear algebra at one squarefree point and support no global component statement. The `H=0` corner of Claim 1 closes only the `x`-degree `<=1` sub-stratum and says nothing about the generic `H=0` leaf.

---

## Headline and subclaim table

| # | Registered subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Source-honest routing: primitive maximum-12 cells are exactly `(8,12)`, `(9,12)`; residues exactly `4\|H` and `3\|H` including `H=0`; no maximum-11 or `(6,9)` input | **CONFIRMED** (class-level; pair-level corner recorded) | a third primitive cell; a residual `H` closed by the frozen route for `(8,12)`; a `4∤H` class not closed; silent use of the max-11 composition |
| 2 | Next row `d u^(d(r+s)-1)(sA-rB)'`; all integer coefficients; logarithmic terms cancel; `delta=sA-rB`; depression `z=uy+A/m`; mismatch `-delta/r`; per-cell instantiations | **CONFIRMED** | a surviving `u'` term; a wrong power of `u`; a wrong mismatch constant; a lower coefficient reaching the `y^(m+n-2)` row |
| 3 | Kummer: minimal root extension degree `= e` (class order) after adjoining roots of unity; `A,B,delta` character one; `e>1 ⇒ delta=0` incl. the proper order-two class in `d=4`; five divisor examples; Gauss on trivial class; constants; repeated roots; reducible binomials | **CONFIRMED** with the monic-core normalization made explicit | degree ≠ class order; a character ≠ 1; a nonzero fixed `delta` on a nontrivial monic-core leaf; a mis-typed example; order-two leaf degenerate |
| 4 | Boundary provenance: `u^ℓ/ℓ! ∂_z^ℓ f(A/m) = [y^ℓ]P` and likewise for `g`, all orders; character filter `wt(c_j) = -j`; `z^11` slot excluded; order-two leaf keeps every even weight `0..10` | **CONFIRMED** | a wrong factorial or power; a discarded coordinate boundary; `z^11` counted as a later constant; a missing even slot |
| 5 | Binary umbrella: `J_(t,z)(F,G)\|_{t=1}=dW`; `W=0 ⇔ f=K^r, g=K^s`, `K` monic depressed of degree `d`; `f D'-s f' D=-W g^(r-1)`; monicity/UFD/zero cases; conditionality on the high-row landing enforced | **CONFIRMED** | a failing identity; a common-power locus larger or smaller than `(K^r,K^s)`; an unconditional high-row claim |
| 6 | Tangent gate at `K=z^d+z+1`: ambient `18/19`, positive rows `17/18`, ranks `11/11`, kernels `7/8`, common-K parameters `3/2`; squarefree point; local only | **CONFIRMED**, proved in closed form: kernel `= m-1`, rank `= n-1` | any count off by one; a kernel not containing the common-K tangent; a global component claim |
| 7 | Two-metric ranking with no overall winner; exact reuse/type-fail split of the `(6,9)` machinery | **CONFIRMED** | an asserted cheaper whole cell; an imported `(6,9)` coefficient, potential, Pfaffian sheet, resultant, or exclusion |
| 8 | Strongest licensed conclusion; no promotion beyond scope | **CONFIRMED** | any statement of high-row reduction, emptiness, coverage, support, counterexample, or JC2 |
| R | Freeze digest check and replay rerun (regression only) | **NOT RERUN — BLOCKED** by the shell-less environment; textual chain verified; banking precondition stated | n/a — process, not mathematics |

---

## Claim 1 — source-honest residual route

**CONFIRMED** (exact at the level of `H`-classes; one pair-level corner recorded below).

The frozen history supplies exactly four mechanisms: `Z` (a zero `y`-degree coordinate), `G` (large triangular source shear, then the repaired prime-gcd theorem for sheared total gcd `p` and the GGV theorem for sheared total gcd `2p`), `D` (divisible-degree polynomial target shear from the leading UFD relation), `E` (equal-degree constant target `GL_2`). The shear identity (history (1.3)) gives sheared total degrees `a(H+dL)`, `b(H+dL)` with `L > max(M,1)`, `M` the maximum coefficient `x`-degree.

Independent reconstruction of the unordered maximum-12 row:

| `(m,12)` | Route |
|---|---|
| `(0,12)` | `Z` |
| `(1,12)`, `(5,12)`, `(7,12)`, `(11,12)` | `G`, gcd one, every `H` |
| `(2,12)`, `(10,12)` | `G`, gcd two: `g=gcd(H,2)∈{1,2}` for every `H` |
| `(3,12)`, `(4,12)`, `(6,12)` | `D`, derivative (reduce to strictly smaller pairs; their unresolved content lives in lower rows, not in this row) |
| `(12,12)` | `E`, derivative (lands on some `(r,12)`) |
| `(8,12)` | `gcd 4`; `8∤12`; primitive |
| `(9,12)` | `gcd 3`; `9∤12`; primitive |

So the primitive cells are exactly `(8,12)` and `(9,12)`. Nothing above touches the maximum-eleven composition or any `(6,9)` artifact.

**Residues, `(8,12)`, `d=4`.** If `4∤H` then `g=gcd(H,4)∈{1,2}` and Dirichlet (finitely many `L` excluded by `L>max(M,1)`) lands the sheared gcd on `g·p`: closed. If `4|H` (including `H=0`, since `gcd(0,4)=4`), then for **every** admissible `L` the sheared total gcd is `H+4L = 4N` with `N = H/4+L ≥ 2` (because `L≥2` always, as `L>max(M,1)≥1`). `4N` is never prime (composite for `N≥2`), and `4N=2p` forces `p=2N` even, hence `p=2`, `N=1` — excluded. So no choice of `L` ever reaches a cited theorem. Residual **exactly** `4|H`, at pair level with no exception.

**Residues, `(9,12)`, `d=3`.** If `3∤H` then `g=1` and the prime shear closes the pair. If `3|H`, the sheared gcd is `3N`, `N=H/3+L ≥ 2`; `3N` is never prime; `3N=2p` forces `p=3`, `N=2`, i.e. `(H,L)=(0,2)`, which is admissible precisely when `M≤1`. Therefore:

- At the level of `H`-classes the statement is exact: every class `3|H` still contains history-open pairs (any pair with `M≥2` forces `L≥3`, `N≥3`, and `3N` is then neither prime nor `2p`), and every class `3∤H` is fully closed. This is the form the registration fixes ("residual conditions on `H`") and the form the replay encodes (`open_H` per residue class). **CONFIRMED.**
- At pair level there is one corner the frozen grammar does not mention: a `(9,12)` Keller pair with `H=0` and **all** coefficient `x`-degrees `≤1` shears with `L=2` to total degrees `(18,24)`, total gcd `6=2·3`, and the frozen GGV theorem ("no counterexample has total-degree gcd `2p` for any prime `p`", `p=3` included) makes it an automorphism. The identical corner exists for the frozen history's own `(6,9)` row (sheared `(12,18)`, gcd `6`). This is a *strengthening* of the frozen coverage derived from the frozen inputs alone, not a break: it means "residual exactly when `3|H`" must be read class-level, exactly as the replay and registration state it. No such corner exists for `d=4` (shown above). Any future `(9,12)` or `(6,9)` `H=0` integration should not assume the whole `H=0` leaf is history-open — its `x`-degree `≤1` corner is classical.

The replay's `open_H` lists (`[0,4,8,12,16]` for `d=4` over `H≤16`; `[0,3,6,9,12]` for `d=3` over `H≤12`) are exactly `gcd(H,d)∉{1,2}`: re-derived and correct. `H=0` is residual in both cells: `gcd(0,d)=d`.

---

## Claim 2 — general next row, depression, mismatch

**CONFIRMED.**

Let `m=dr`, `n=ds`, `gcd(r,s)=1`, and after the target scalings `P↦λP`, `Q↦μQ` with `λ=α^{-1}`, `μ=β^{-1}` (which exist, are harmless for the Keller property and automorphy, and make the common core **monic** — see Claim 3), write `a_m=h^r=u^m`, `b_n=h^s=u^n` with `u^d=h`, and `A=a_{m-1}/u^{m-1}`, `B=b_{n-1}/u^{n-1}`.

The coefficient of `y^{m+n-2}` in `J=P_xQ_y-P_yQ_x` receives contributions only from index pairs `(i,j)` with `i+j=m+n-1`, i.e. `(m,n-1)` and `(m-1,n)`; every lower coefficient reaches at most `y^{m+n-3}`. The four terms are exactly the report's display:

```text
T1 = (n-1) a_m' b_(n-1)  =  m(n-1) u^(m+n-2) u' B
T2 =  n a_(m-1)' b_n     =  n(m-1) u^(m+n-2) u' A + n u^(m+n-1) A'
T3 = -m a_m b_(n-1)'     = -m(n-1) u^(m+n-2) u' B - m u^(m+n-1) B'
T4 = -(m-1) a_(m-1) b_n' = -n(m-1) u^(m+n-2) u' A
```

`T1+T3` kills the `u'B` terms and `T2+T4` kills the `u'A` terms — the logarithmic cancellation is exact, with integer coefficients `m(n-1)` and `n(m-1)`. The remainder is

```text
u^(m+n-1) (nA' - mB') = d u^(d(r+s)-1) (sA - rB)',
```

since `n=ds`, `m=dr`, `m+n-1=d(r+s)-1`. For a Keller pair this coefficient vanishes (`m+n-2 ≥ 18 > 0`), `u≠0`, `d≠0` in characteristic zero, hence `(sA-rB)'=0`: `delta=sA-rB` is a `d/dx`-constant — equation (2.2), with the constant-field caveat resolved in Claim 3.

**Depression.** With `z=uy+A/m`, i.e. `y=(z-A/m)/u`: the first coordinate's `z^{m-1}` coefficient receives `-A` from `u^m y^m=(z-A/m)^m` and `+A` from `u^{m-1}A y^{m-1}=A(z-A/m)^{m-1}`; total zero. The second coordinate's `z^{n-1}` coefficient is `-nA/m + B = B-(s/r)A = -(sA-rB)/r = -delta/r` — equation (2.3). Lower coefficients cannot reach these slots. So `delta` is simultaneously the integrated next row and the first depression mismatch, as claimed.

**Per-cell instantiations.** `(8,12)`: `(d,r,s)=(4,2,3)`, row `u^{19}(12A'-8B') = 4u^{19}(3A-2B)'`, `delta=3A-2B`, depression `z=uy+A/8`, mismatch `-delta/2`. `(9,12)`: `(d,r,s)=(3,3,4)`, row `u^{20}(12A'-9B') = 3u^{20}(4A-3B)'`, `delta=4A-3B`, depression `z=uy+A/9`, mismatch `-delta/3`. All exponents and constants re-derived and exact. The replay's `top_row` bookkeeping (`{A_prime: n, B_prime: -m}`, log terms cancelling) matches the four terms above coefficient-for-coefficient.

**Normalization constants and the constant field, challenged.** The scalings divide by `α, β` only (no root extraction); the Jacobian constant rescales by `λμ ≠ 0`; the depression divides by `m ≠ 0`. The one genuine trap is the constant field of `k(x)(u)`, which is where `delta` lives; it is dealt with in Claim 3 and is the review's first non-blocking precision.

---

## Claim 3 — full Kummer-class audit

**CONFIRMED**, with the monic-core normalization made explicit (non-blocking; the producer's own scalings supply it and the replay implements exactly the divisor order).

**Degree equals class order.** Work over `k ⊇ μ_d`. All `d`-th roots of `h` differ by elements of `μ_d ⊂ k`, so `k(x)(u)` is independent of the chosen root and "minimal root extension" is well defined. Let `e` be the order of `h` in `k(x)^*/k(x)^{*d}`. Then `h^e=w^d` for some `w∈k(x)^*`, so `(u^e/w)^d=1` and `u^e=ζw∈k(x)`: the minimal polynomial of `u` divides `X^e-u^e`, giving degree `≤e`. Conversely if the degree is `e'`, the conjugates of `u` lie in `{ζu}`, so `N(u)=ζ' u^{e'}∈k(x)`, hence `h^{e'}=(u^{e'})^d∈k(x)^{*d}` and `e\|e'`. Degree `=e` exactly. Irreducibility of `X^d-h` is never needed, so every reducible-binomial case (see the order-two leaf below) is covered; with `i∈k` the classical `-4c^4` quartic pathology dissolves (`-4c^4=(c(1+i))^4`). The Kummer pairing `σ ↦ σ(u)/u` embeds the cyclic Galois group onto `μ_e`, so a generator sends `u ↦ ζu` with `ζ` a primitive `e`-th root of unity.

**Characters.** `σ(A)=ζ^{-(m-1)}A=ζA` and `σ(B)=ζ^{-(n-1)}B=ζB` since `e\|d\|m,n`: characters one, exactly as claimed. Hence `σ(delta)=ζ·delta`.

**The fixed-field step and the constant field.** `delta'=0` places `delta` in the full constant field of `k(x)(u)` — not automatically in `k`. The step "`delta` belongs to the fixed field" is valid exactly when the constant field is `k`, and that is where the monic normalization is load-bearing:

- *Lemma.* If `h` is **monic** nonconstant, then (a) the class order of `h` over `k(x)` equals the divisor order `e = lcm_i(d/gcd(d,v_i))` computed from the finite valuations `v_i` of `h` — because `h^j=c·g^d` with `g` monic forces `c=1`, and the monic `d`-th root `∏p_i^{jv_i/d}` lies in `k[x]` whenever the exponents are integral; and (b) the constant field of `k(x)(u)` is `k`: valuation values persist over any constant extension `k''`, so the class order over `k''(x)` is still `e`, and `e=[k(x)(u):k(x)]=[k(x)(u):k''(x)]·[k'':k]=e·[k'':k]` forces `k''=k`.
- Then `delta ∈ k` is `σ`-fixed and has character one, so `(ζ-1)delta=0` and `e>1 ⇒ delta=0` — equation (2.4), proved.
- *Explicit failure shape without the normalization* (this is why the precision is genuine): over `k=Q(i)`, take `h=2x^4` (class order 4: `2^j∈(Q(i)^*)^4` first at `j=4`), `u=2^{1/4}x`, and `a_7=2x^7`, `b_{11}=2x^{11}`, `a_8=h^2=4x^8`, `b_{12}=h^3=8x^{12}`. Then `A=a_7/u^7=u/(2x)`, `B=b_{11}/u^{11}=u/(4x)`, and `delta=3A-2B=u/x=2^{1/4}`: a **nonzero** `d/dx`-constant of character one, while the `y^{18}` row `(11a_8'b_{11}-8a_8b_{11}')+(12a_7'b_{12}-7a_7b_{12}') = (704-704)x^{18}+(1344-1344)x^{18} = 0` is satisfied identically. The constant field grew to `Q(i,2^{1/4})` and the fixed-field step fails. Renormalizing the same data monic (`λ=1/4`, `μ=1/8`) gives `h_0=x^4`, `e=1`, `u=x`, `Ã=1/2`, `B̃=1/4`, `delta=1`: a legal unforced constant on the trivial leaf — fully consistent. Conclusion: the leaf labels are the monic-core (divisor) orders. The report's prose leaves "monic" implicit; its own target scalings provide it, and `replay.py`'s `class_order` computes only the divisor order, so nothing registered is broken.

**The proper order-two class inside `d=4`, in detail.** `e=2` iff all `v_i` are even and some `v_i≡2 (mod 4)`; then `h=q^2` with `q` monic and not a square. `X^4-q^2=(X^2-q)(X^2+q)` is reducible; the minimal extension is `k(x)(√q)=k(x)(√{-q})` (using `i∈k`), a **genuine quadratic** — degree 2 by the lemma, not a degenerate notation for the quartic or polynomial leaf. The generator sends `u↦-u` (`ζ=-1`), so only parity weights exist: `delta=0` is forced by the same character argument, but every even lower index `j∈{0,2,4,6,8,10}` remains character-admissible. The report explicitly refuses the mod-four filter on this leaf: correct.

**Five divisor examples, recomputed** (order = least `j` with `d\|j·v` for all residues; each divisor sums to zero; including the residue `-H` at infinity can never change the order, since `d\|j v_i` for all finite `i` already forces `d\|jH`):

```text
d=4: [1,1,1,1,-4] -> 4    (h=x(x-1)(x-2)(x-3), H=4)
d=4: [2,2,-4]     -> 2    (h=x^2(x-1)^2,       H=4; q=x(x-1) squarefree, not a square)
d=4: [4,-4]       -> 1    (h=x^4,               H=4)
d=3: [1,1,1,-3]   -> 3    (h=x(x-1)(x-2),       H=3)
d=3: [3,-3]       -> 1    (h=x^3,               H=3)
```

All five match the report and the replay's expected map; all five sit at the smallest positive residual degrees (`H=d`), and repeated roots are handled by the valuation computation itself.

**Gauss on the trivial class; constants.** `e=1` means `h=w^d` in `k(x)`; all valuations of `w` are `v_i/d ≥ 0`, so `w∈k[x]` and (monic core) `u=w` is polynomial: no nontrivial character, `delta` weight-unforced. For `H=0` the scalings give `h=1`, `u=1`, `e=1`: the constant-core case lands in the trivial leaf, so "including `H=0`" is consistent across Claims 1 and 3.

---

## Claim 4 — boundary and constant provenance

**CONFIRMED.**

`y=0` is exactly `z=A/m` since `z=uy+A/m` and `u≠0`. Writing `w=z-A/m`, the depressed first coordinate is *literally* `f = Σ_ℓ a_ℓ (w/u)^ℓ`, so its `ℓ`-th Taylor coefficient at the boundary is `a_ℓ u^{-ℓ}`, i.e.

```text
u^ℓ/ℓ! · ∂_z^ℓ f(A/m) = a_ℓ = [y^ℓ]P ∈ k[x],   0 ≤ ℓ ≤ m,
```

and identically for `g` with `0 ≤ ℓ ≤ n` (cross-check: `∂_z = u^{-1}∂_y` by the chain rule, so `∂_z^ℓ f|_{z=A/m} = u^{-ℓ}·ℓ!·[y^ℓ]P`). Both coordinates, every derivative order, and all powers and factorials in (2.5) are exact. Neither boundary may be discarded after the root extension: the polynomiality of every original coefficient is re-imposed through these jets on every Kummer leaf. Correct.

**Character filter.** From `σ(P)=P`, `σ(z)=ζz` one gets `σ(c_j)=ζ^{-j}c_j`: a term `c_j z^j` carries weight `-j`, so a later *constant* is character-admissible only when `e\|j`. Recomputed admissible sets on `0 ≤ j ≤ n-2 = 10`:

```text
(8,12) e=4: {0,4,8}      e=2: {0,2,4,6,8,10}      e=1: all of 0..10
(9,12) e=3: {0,3,6,9}                              e=1: all of 0..10
```

These match the report's table and the replay's `range(self.n - 1)` filter. The `z^{11}` slot is the depression mismatch `-delta/r` — already forced to zero on every nontrivial leaf — and is correctly **excluded** from the later-constant count in both the report ("`0<=j<=10`") and the replay (explicit comment and range). The order-two leaf retains every even lower weight, exactly as registered; the filter is presented as a character constraint only, with no claim that integration realizes each slot — the hedge is correct and necessary.

---

## Claim 5 — binary umbrella

**CONFIRMED**, including the producer's conditionality.

**(4.1).** For monic `f,g` of degrees `m=dr`, `n=ds` with binary homogenizations `F,G`: Euler gives `F_t = mF - zF_z` at `t=1`, so

```text
J_(t,z)(F,G)|_{t=1} = (mf - z f')g' - f'(ng - z g') = m f g' - n f' g = d(r f g_z - s f_z g) = dW.
```

Both sides are forms of degree `m+n-2` after homogenization, so the bivariate identity holds as displayed. Exact.

**(4.2).** If `W=0` then `(f^s/g^r)' = f^{s-1}g^{-r-1}(s f' g - r f g') · g^{...}` vanishes (`g≠0` monic, characteristic zero), so `f^s = c·g^r`; degrees `drs` agree and monicity forces `c=1`. UFD with `gcd(r,s)=1`: `s·v_p(f)=r·v_p(g)` forces `r\|v_p(f)` at every prime, so `f=K^r` with `K` monic, and `g^r=K^{rs}` with monicity gives `g=K^s`; `deg K = m/r = d`. Depression is inherited: `[z^{m-1}]K^r = r·[z^{d-1}]K = 0` forces `K` depressed. Conversely `W(K^r,K^s) = rsK^{r+s-1}K' - rsK^{r+s-1}K' = 0`. Zero-polynomial cases are excluded by monicity; the only constants that could appear are killed by monicity. Exact in both directions, with `K` monic depressed of degree `d`:

```text
(8,12): W = 2 f g_z - 3 f_z g,  common locus (K^2,K^3), deg K = 4;
(9,12): W = 3 f g_z - 4 f_z g,  common locus (K^3,K^4), deg K = 3.
```

**(4.3).** With `D=f^s-g^r`:

```text
f D' - s f' D = f(s f^{s-1}f' - r g^{r-1}g') - s f'(f^s - g^r)
             = -r f g^{r-1} g' + s f' g^r = -g^{r-1}(r f g' - s f' g) = -W g^{r-1}.
```

A three-line polynomial identity, valid for all `f,g`; the replay's instance checks on `f=z^m+2z^2+1`, `g=z^n+3z^3-1` therefore pass necessarily.

**Conditionality enforced.** The report's §4 opens with "The new cells have not yet been proved to land on a complete Faber system. Conditionally on the usual constant binary-Jacobian landing…", and the scope block pins `full_high_row_integration=NOT_DONE`. No high-row landing for either cell is proved anywhere in the artifact, and none is assumed in this review. Any consumer who reads §4 as an unconditional reduction is out of scope.

---

## Claim 6 — widths and tangent ranks

**CONFIRMED** — and proved in closed form, which is stronger than a numerical rerun.

Setup: depressed monic perturbations `δf` (degree `≤ m-2`, so `m-1` variables) and `δg` (degree `≤ n-2`, so `n-1` variables); ambient `= m+n-2`: **18** for `(8,12)`, **19** for `(9,12)`. Linearizing `W` at `f=K^r`, `g=K^s` and writing `L_a(φ) := Kφ' - aK'φ`:

```text
dW = r K^(r-1) L_s(δg) - s K^(s-1) L_r(δf).
```

On the depressed family `deg W ≤ m+n-3` (the `z^{m+n-1}` coefficients cancel by `rn=sm` and the `z^{m+n-2}` coefficients vanish by the two depressions), and the column `δf=z^{m-2}` attains degree `m+n-3` with leading coefficient `rn-s(m-2)=2s≠0`, so the positive-degree row count is exactly `m+n-3`: **17** and **18**. All counts match the report.

**Kernel, exactly.** `K=z^d+z+1` is irreducible over `Q` for both `d=3` (no rational roots: values `3` and `-1` at `±1`) and `d=4` (no rational roots; a factorization into two rational quadratics forces `a^6-4a^2-1=0` with `a=±1` the only rational candidates, both failing); in particular `K` is squarefree and `gcd(K,K')=1`. Since `r-1≥1`, `K` divides `dW`, so a constant `dW` is forced to be zero: the positive-row kernel equals the full kernel `{dW=0}`. Now (both cells have `s=r+1`):

1. `r L_s(δg) = s K^{s-r} L_r(δf) = sK·L_r(δf)`, so `K \| L_s(δg) = Kδg' - sK'δg`, hence `K \| K'δg`, hence `K \| δg`. Write `δg=Kψ`, `deg ψ ≤ n-2-d = m-2`.
2. `L_s(Kψ) = K(K'ψ+Kψ') - sKK'ψ = K·L_{s-1}(ψ) = K·L_r(ψ)`, so `r L_r(ψ) = s L_r(δf)`, i.e. `L_r(rψ - sδf) = 0`.
3. `L_r(φ)=0` with `deg φ ≤ m-2` forces `φ=0`: a nonzero solution of `Kφ' = rK'φ` has leading-coefficient balance `deg φ = r·deg K = m > m-2` (and a nonzero constant fails outright).

Hence `ψ=(s/r)δf` and the kernel is **exactly**

```text
{ (δf, (s/r)·K·δf) : deg δf ≤ m-2 },   dimension m-1,
```

with the converse inclusion immediate (`L_s((s/r)Kδf) = (s/r)K L_r(δf)` makes `dW=0`). So:

```text
(8,12): kernel = m-1 = 7,  rank = ambient - kernel = 18-7 = 11;   δg = (3/2)K·δf
(9,12): kernel = m-1 = 8,  rank = 19-8 = 11;                      δg = (4/3)K·δf
```

Both registered ranks are `n-1 = 11` — the coincidence of the two ranks is structural (`n=12` for both cells), not accidental. The common-K tangent `(δf,δg)=(rK^{r-1}δK, sK^{s-1}δK)`, `deg δK ≤ d-2`, satisfies `δg=(s/r)Kδf` and stays depressed, so it sits inside the kernel with dimension exactly `d-1`: **3** and **2**, strictly smaller than `7` and `8`. Every number in the report's table and the registration (`18/17/11/7`, `19/18/11/8`, common-K `3/2`) is therefore proved, not merely re-eliminated; a rerun of the replay's Gaussian elimination on these matrices can only return `11/11` or expose a byte-custody breach.

**The point is squarefree** (indeed irreducible). **The local calculation supports no global component claim**, and the report makes none: it labels the computation "a local singularity check, not a global component classification" and the replay pins `constant_W_components=NOT_CLASSIFIED`. One wording caution (non-blocking): "Both gates are highly singular along their common-power loci" is justified here only in the sense the colon supplies — the linearization kernel (`7/8`) strictly exceeds the common-power tangent (`3/2`), i.e. the gate's linearization degenerates along the locus. Scheme-theoretic singularity of the gate at the point would additionally require its local dimension to be `< m-1`, which neither the producer nor this review computes. The registration registers only the numbers; the numbers are exact.

---

## Claim 7 — ranking and reuse

**CONFIRMED.**

**Two metrics, not one.** Raw first gate: `(8,12)` has `18` variables, `17` positive rows, kernel `7` — strictly smaller than `(9,12)`'s `19/18/8` in every count — and carries the familiar `2:3` signature. Kummer branch tree: `(9,12)` has two leaves (`3,1`) against three (`4,2,1`), no intermediate quadratic branch, and `4` nontrivial weight-zero slots against the order-two leaf's `6`. Both directions re-derived above. The producer refuses any whole-cell ordering — report §4 ("These facts do not prove that one complete cell closure will be cheaper"), the verdict block, and the replay's `whole_cell_cost=NOT_ORDERED_BEFORE_HIGH_ROW_INTEGRATION` all agree. No cheaper-cell conclusion is asserted anywhere in the artifact; none is licensed.

**Reuse audit.** The five items listed as reusable are exactly the ones this review re-proved for general `(dr,ds)`: the leading UFD/source-shear route (Claim 1), root-extension normalization, next-row cancellation, depression, mismatch character and charged boundaries (Claims 2–4), Euler/binary-W, the common-power lemma and route identity (Claim 5), abstract target gauges, and valuation/genus/trajectory *methods* explicitly deferred until "after the new exact curves and denominators have been derived". These import shapes, not conclusions. The type-fail list is genuinely type-specific: the exact `(6,9)` Faber coefficients and five Laurent potentials, Kuranishi quadrics, the lower-Pfaffian two-sheet decomposition, exceptional polynomials, DS resultants, the finite-pole exponent table, and trajectory reconstruction are all coefficient-level data of the degree-`(6,9)` core; `(8,12)` changes the core degree (`4` vs `3`) and its order-two leaf has parity-only weights, `(9,12)` keeps core degree `3` but changes the Wronskian signature `2:3 → 3:4`, so every such object must be recomputed. Neither change is cosmetic — confirmed. One editorial slip (non-blocking): report §1 says the `(6,9)` artifacts are "used only in Section 6 to label reusable methods"; the labeling actually happens in §5, while §6 reuses the `2:3` organization as a template. Either way, no `(6,9)` exclusion is load-bearing anywhere in §§2–4: checked line by line.

---

## Claim 8 — strongest licensed conclusion

**CONFIRMED.**

The smallest missing hypotheses found, all non-blocking and all recorded above:

1. **Monic-core normalization** in the Kummer split (Claim 3). Without it, (2.4) has the explicit `h=2x^4`, `delta=2^{1/4}` failure shape; with it — and the producer's own target scalings supply it, while the replay computes only the divisor order — (2.4) is a theorem. Recommended one-line erratum-level clarification in any successor artifact: "the class order is that of the monic core".
2. **Class-level reading of "exactly"** for the `(9,12)` residue (Claim 1). The frozen inputs close the `H=0`, all-`x`-degrees-`≤1` corner via the `L=2` shear onto total gcd `6=2·3` plus GGV. The registered class-level statement is exact; the pair-level reading has this one corner; `(8,12)` has none. The identical observation applies to the frozen history's `(6,9)` grammar and should accompany any `H=0` successor integration.
3. **Regression not executable here** (process): see Execution environment and the banking precondition.

No promotion beyond scope occurs in the artifact: it derives no high-row Faber system, classifies no constant-W component, proves neither residue empty, claims no maximum-12 coverage or automorphy, constructs nothing, touches no arbitrary-support statement, and makes no JC2 inference. The replay's terminal scope block (`full_high_row_integration=NOT_DONE`, `constant_W_components=NOT_CLASSIFIED`, `either_frontier_empty=false`, `JC2=NOT_CLAIMED`) matches the report's §7 and the registration's refusals exactly. The strongest statement this review licenses is precisely the producer's verdict block: the exact first routing of the two primitive cells, the forced-zero mismatch on every nontrivial monic-core Kummer leaf, the charged boundaries, the conditional binary gate with its exact local tangent data, and the two-way cost comparison with no overall winner.

---

## Non-blocking precisions

None of the following changes a numbered verdict.

1. *Monic core.* Claims 3/8 above. The report's §2 phrase "harmless scalar extension containing the needed roots of unity" should not be read as licensing a non-monic core; `μ_d` alone does not prevent constant-field growth, monicity does.
2. *`H=0` corner for `d=3`.* Claims 1/8 above. Class-level "exactly" is the registered and correct form.
3. *"Highly singular" wording.* Claim 6: proved is kernel `>` common-power tangent (linearization degeneracy along the locus); scheme-singularity of the gate would need a local dimension bound nobody computed. The registered numbers are exact.
4. *Section pointer.* Report §1 says "Section 6" for the method-labeling that occurs in §5. Editorial only.
5. *`delta in k`.* Equation (2.2)'s "in k" is exact under the monic normalization (constant field `=k`); in general it reads "in the constant field", which is where the weight argument needs the lemma of Claim 3.
6. *Rank coincidence.* Both ranks equal `n-1=11` structurally (kernel `=m-1` for `s=r+1` cells); the equality of the two cells' ranks is not evidence of any deeper symmetry between the cells.
7. *Prepared checker.* `/tmp/max12_review_claude/independent_checks.py` (untracked, unexecuted) encodes hash recomputation, an independent list-based rebuild of the tangent matrices with exact and mod-`1000003` ranks, the routing sweep, next-row and depression instances on the `e=1` leaf, the five class orders, the non-monic control, and the binary identities — available to any shell-bearing session that wants a second machine check beyond the two frozen commands.

---

## Attacks that did not land

Checked because they are the stated failure modes; none landed.

- *A third primitive maximum-12 cell.* Full row reconstructed: `Z/G/D/E` cover everything except `(8,12)`, `(9,12)`.
- *A shear closing `4|H`.* `H+4L≡0 (mod 4)` is never prime and `4N=2p` forces `N=1<2`: impossible for every admissible `L`.
- *A surviving logarithmic term in (2.1).* The four coefficients `m(n-1)`, `n(m-1)`, `-m(n-1)`, `-n(m-1)` cancel in pairs; only `u^{m+n-1}(nA'-mB')` survives.
- *A wrong mismatch constant.* `B-(n/m)A = -(sA-rB)/r` re-derived; `-delta/2` and `-delta/3` per cell.
- *Kummer degree ≠ class order on a reducible binomial.* The norm argument gives `e\|e'` and `u^e∈k(x)` gives `e'≤e`, with no irreducibility used; the `d=4`, `e=2` leaf `(X^2-q)(X^2+q)` is a genuine quadratic.
- *A nonzero forced `delta` slipping through on a nontrivial leaf.* Only possible via constant-field growth; killed by the monic core (lemma with proof), and the non-monic shape is quarantined as a normalization error, not a producer leaf.
- *Mod-four filter smuggled onto the order-two leaf.* The report and replay both keep all six even slots `{0,2,4,6,8,10}`; only parity weights exist there.
- *`z^11` counted as a later constant.* Excluded in the report table (`0<=j<=10`) and in the replay (`range(n-1)` with the explicit comment).
- *A discarded boundary after the root extension.* (2.5) is definitionally exact in the recentered variable; both coordinates carry all `m+1` resp. `n+1` jets.
- *An unconditional high-row landing.* §4's first sentence and the scope block forbid it; nothing in §§2–6 uses it.
- *A tangent count off by one.* Closed-form kernel `{(δf,(s/r)Kδf)}` of dimension `m-1`; ambient `m+n-2`; rows `m+n-3` with the top row realized by the `2s≠0` coefficient.
- *A global component claim hiding in the rank table.* `constant_W_components=NOT_CLASSIFIED`; the kernels strictly exceed the common-K tangents, which is the opposite of a transversality claim.
- *An overall cheaper-cell assertion.* Refused three times (report §4, verdict block, replay ranking); the two metrics genuinely point in opposite directions.
- *A `(6,9)` exclusion or maximum-11 input.* The two frozen history hashes are the only pinned inputs; the routing, algebra, and gates above never touch either artifact; the mid-session maximum-11 promotion happened after the freeze and is not consumed.

---

## Promotion advice (repeated)

Accept the preflight as a bounded, source-honest first routing of the two primitive maximum-12 cells, at exactly its registered scope and subject to the banking precondition (one shell-bearing rerun of the two frozen commands). Carry forward: the monic-core clarification, the class-level reading of the `(9,12)` residue with its `H=0` `x`-degree-`≤1` corner, and the closed-form tangent-kernel description `{(δf,(s/r)Kδf)}`, which any high-row successor can consume directly. The cheapest licensed successors remain the producer's §6 items: the first integrated `2:3` block on the full-order `(8,12)` leaf, the mandatory `h=x^2(x-1)^2` order-two adversarial control (mod-four vanishing is falsified on that leaf), and the `(9,12)` order-three/polynomial pair of controls — all terminated at the first nonlinear compatibility, with no generic coefficient rectangle and no AWS.

Do not treat this preflight, or this review, as a high-row reduction, a component classification, an emptiness statement for either cell, maximum-twelve coverage or automorphy, an arbitrary-support statement, a counterexample, or a JC2 decision.

No result in this review proves or disproves JC2.
