# Blind whole-portfolio submission — Opus 5 lane

Round ID: `20260827T0145Z`
Lane: Opus 5, standing blind whole-portfolio researcher
Date: 2026-08-27

## 0. Basis, tool boundary, disclosure

All seven charged hashes rehashed locally and match the freeze exactly:

```text
README.md       f09aefd11cb776c4af9e56b3f5d24501c6d6d7a692f9a26874dd40b0f5e1c44a
COORDINATION.md d5ca2421fdaaf7fac2f142e3fb0f96bf58c181047f092c3434a970d50dcde812
PROGRESS.md     337a7b4a1f6edf537000cf2548f89e096e2adf2c9d870ebf015d0f9690ac922a
APPROACHES.md   34c0330c22620f0afa72d759aef00627d77517c71d29da59f699646a18ebf9af
AUDIT.md        99c699c3815ed2985d9dcf4bced830c19e1d700efb25ecf158ed22ee7a96f5c1
notes.md        5bf91d75636f3929cc9e1b7ed97f126503ff43568f825f2d45e4f92513745070
ladder/REDUCTION.md f0fca49811349483c437d674ab819065eb09500330516d161978868c71bf6371
```

All six charged artifacts located by content hash and read in full:

```text
16ec6f54…  xmodel/total-rees-localized-rho-unit-staged-calculus-promotion-sol-20260827.md
cd6f34da…  xmodel/max12-812-order2-p0-total-rees-t-c0-rho-unit-promotion-sol-20260827.md
133ad884…  xmodel/max12-812-order2-p0-total-rees-t-c1-cubic-certificate-promotion-sol-20260827.md
5fd19f35…  xmodel/max12-812-order2-p0-total-rees-t-cs-grade14-decisive-fibre-promotion-sol-20260827.md
696152da…  xmodel/as109-one-sided-target-degree-tri-promotion-sol-20260827.md
8b462a91…  xmodel/td6-h19-original-first-total-f-certificate-grok-20260827.md
```

Additionally read, as named custody of those artifacts or as required for
deduplication: the `T-c1` hostile review `40ea0ff3…`, the `T-cs` grade-14
hostile review `7fbd9423…`, the `T-rs` V16 hostile review, the `T-c0/T-c1`
producer, `xmodel/as109-wild-symplectic-conductor-gate-20260824.md`, the
`AS109 SUPPORT GRAMMAR STOP` ledger entry, the prior round's synthesis
`ceea3b67…` and my own prior submission `43adf317…`.

**Disclosure.** A repository-wide `grep` for the string `Tg10_2` returned two
matching lines from `xmodel/ideation-20260827T0145Z-grok.md`, a co-lane blind
submission. I did not open that file, and the two lines I saw contained only
the already-charged identity `(C1)` and one certificate-type table row, both of
which are verbatim in the sealed freeze and in the promoted artifacts. All
subsequent searches excluded `ideation-20260827T0145Z-*`. Nothing below derives
from that exposure; every item in §3–§5 was derived from the frozen `.poly`
displays in the `T-rs` and `T-c1` reviews and is hand-reproduced here.

No web access, no heavy computation, no AWS mutation, no `jc2-lean` access.
Local work was `cat`/`sed`/`grep`/`shasum` plus hand algebra reproduced in
full. This report is my only repository edit.

Evidence language used below: **EXACT** = proved here by displayed algebra from
frozen charged bytes; **CONDITIONAL** = exact given one named unchecked
hypothesis, with the check specified; **NAVIGATION** = ranking or allocation
claim; **SPECULATION** = a research proposal with no proof.

---

## 1. Disposition vector over all 46 master-table avenues

```text
 1 unchanged   2 unchanged   3 unchanged   4 unchanged   5 raise
 6 unchanged   7 unchanged   8 unchanged   9 unchanged  10 unchanged
11 unchanged  12 unchanged  13 unchanged  14 unchanged  15 unchanged
16 unchanged  17 unchanged  18 reopen     19 raise     20 unchanged
21 unchanged  22 unchanged  23 unchanged  24 unchanged  25 unchanged
26 unchanged  27 unchanged  28 unchanged  29 unchanged  30 unchanged
31 raise      32 unchanged  33 unchanged  34 unchanged  35 unchanged
36 unchanged  37 unchanged  38 unchanged  39 unchanged  40 unchanged
41 unchanged  42 unchanged  43 unchanged  44 unchanged  45 unchanged
46 unchanged
```

**Row 5 — Jung–van der Kulk / degree descent: `raise`.**
The promoted `AS-TRI` proof is, mechanically, a Jung/Abhyankar–Moh degree
descent: `p_m = c q_1^m` from the top Jacobian row, then the target shear
`P -> P - cQ^m` strictly lowering `deg_y P`, iterated to a terminal
contradiction. Row 5's recorded stuck-point is *"amalgam rigidity never bites
on non-automorphisms"*. `AS-TRI` bites on a hypothetical **non**-automorphism,
because the thing that closes the ladder is not automorphy but **integrality**
(`v(c) = v(p_m) - m v(q_1) >= 1`, so the shear is residue-preserving over
`Z_109`). That is a genuinely different engine for the same row and it has now
produced a promoted theorem. My prior-round raise was for a different reason
(the prime-ray note names descent as a `3P-E31` client); this reason is
independent and stronger.

**Row 18 — Graded / equivariant / GIT symmetry: `reopen`.**
Row 18 is recorded *closed as a counterexample hunt* (Shaska 2026: graded plane
Keller maps are automorphisms; "a hypothetical CE has no `G_m` symmetry"). That
closure is about the *counterexample*. It says nothing about the **normalized
chart systems the campaign actually computes with**, and §3 below shows by
direct hand check on the frozen bytes that the actual-total landing system
carries an explicit **rank-two torus**: every one of the five displayed source
rows is homogeneous for two independent integer gradings, and every one of the
three promoted certificates is bihomogeneous with exactly the bidegrees the
gradings force. Row 18's machinery — equivariant/weighted reduction, graded
Nullstellensatz, torus-fixed loci, bidegree-restricted cofactor spaces — is
therefore directly applicable as a **proof tool** on the campaign's own charts.
I reopen the row in that role only; its counterexample-side closure stands.

**Row 19 — char-p counterexamples + Witt lifting: `raise`.**
Two charged facts plus one new exact one. (a) `AS-TRI` (`696152da…`) is the
first *structural* (degree-shape) constraint on an AS109 lift rather than
another fixed-`deg_y` no-go, and it composes with the reviewed two-sided floor.
(b) §4 below gives the exact source-gauge group of the AS109 lift set and an
explicit gauge section — which is precisely the object the `AS109 SUPPORT
GRAMMAR STOP` ledger entry names as missing ("no finite exhaustive graph exists
without a proved gauge section or groupoid transition rule"). (c) §4.3 opens the
arithmetic `(deg_y, v_109)` Newton polygon, of which `AS-TRI` is exactly the
first corner. The row's recorded stuck-point (uniform support/degree and a
characteristic-zero polynomial limit) is unchanged, but the row now has a live
exclusion engine rather than a serial no-go ladder.

**Row 31 — Integrality / ZMT / Rees valuations: `raise`.**
This row's recorded status was "No direct attempt". In the last 24 charged
hours it produced two more promoted actual-total Rees chart theorems (`T-c0`
full chart, ordered `T-c1`) on top of `T-rs`, plus a promoted localized
special-fibre theorem for `T-cs`. Three of four `J1` charts are closed. It is
the campaign's highest-throughput row and §3 makes its remaining certificates
strictly cheaper. Raised for the second consecutive round on independent
evidence.

**Rows I explicitly did not move, against temptation.**
Row 21 (`p-adic injectivity / Hensel`): I raised it last round; nothing new
this round belongs to it. `AS-TRI` is about lift *shape*, not about transfer to
characteristic zero, so it scores in row 19. Row 7 (`A(F)`): my prior raise
stands and the synthesis put it on `HOLD` pending a precise source-to-`A(F)`
interface; no new charged evidence, so no re-raise. Row 1 (GGV corner farm): I
lowered it last round on a deliverable-type argument that still stands; §5.2
transplants its *engine* to an arithmetic polygon, which is a relabelling of
where the engine is useful, not a rank change for the row as written. Row 36
(guided CE search): §4.2 removes exactly one continuous parameter from any
fixed-box AS109 search; one dimension does not move a row whose stuck-point is
exponential.

---

## 2. Reranked principal bottlenecks

### 2.1 Proof side

1. **Absolute or cofinal complexity/type ceiling.** Unchanged at #1.
   `REDUCTION.md` §7.2 remains decisive: `KJN(C)` is type-relative and becomes a
   ceiling only after an independent bounded `(alpha,beta)` menu with
   provenance. No charged artifact supplies that menu. Every chart closed this
   round is orthogonal to it.
2. **The genuine-localizer complements, promoted from a to-do to a structural
   obligation.**  *This is my main reranking claim.*  §3.4 proves that on the
   `rs` and `cs` charts **no certificate of the promoted staged type can ever
   have localizer `1`**: the bigrading forces a strictly positive power of `k`.
   So `V(k)` is not "one more chart to do later at a higher grade"; it is
   provably outside the reach of the instrument the landing lane is built on.
   Its fanout is every `J1` chart plus the `k=0` siblings the ledger already
   lists. §3.5 then supplies the different mechanism it needs, so this
   bottleneck is simultaneously the newly-highest-ranked one and the one with
   the cheapest available attack.
3. **Universal full-configuration landing / coverage** (`T9`/`T10`): composite
   single-pole, general off-axis, post-jump mixed contexts, all `NOT
   ESTABLISHED`. Unchanged in content, demoted one place by (2).
4. **The arbitrary-standard-pair bridge.** Unchanged from my prior submission
   and still unaddressed: without it the whole GGV5/prime-ray machinery emits
   `B_GGV`-value statements only. §5.1 adds a new argument for why this is the
   *same* obligation as (2) and (5), which raises its priority-by-exposure.
5. **The second stage (`J2` charts over `A/J1`) and the terminal receiver, now
   known to be row-disjoint from stage one.**  §3.6: every row consumed by the
   four promoted `J1` certificates lies in `J1` and therefore vanishes
   **identically** on `V(J1)`. The optimistic budget "six certificates of the
   same shape" is wrong; stage two is a fresh computation on a different row
   support (the surviving grade-12 row gives `e1^2` there).
6. TD6 whole closure (original-FIRST/total-`F` certificate, omitted moduli,
   q15 as a genuine source modulus). High local momentum, low global fanout.
7. Order-two fan exhaustiveness (mixed `H>15`, factor-degenerate receivers).
8. `G2-PSC` and `G2-BD`: dormant. No live lane imports a GGV packet as Sigray
   input; a pure-Sigray architecture bypasses `G2-PSC` outright.

### 2.2 Disproof side

1. **Existence-or-nonexistence of an exact AS109 polynomial lift, attacked by
   the arithmetic Newton polygon.**  Promoted to #1, above effectivity. Reason:
   `AS-TRI` shows the first corner of that polygon is already decisive, and the
   whole floor ladder (`>=9`, then `>=12`, then the `(12,0)`/`(12,1)` shapes)
   is the campaign paying one corner at a time by hand. An engine that walks
   all corners either raises the floor without bound (retiring the campaign's
   single most-developed seed) or exhibits an admissible slope sequence, which
   is a *very* small search target. Either outcome is decisive; the current
   ladder produces one bit per lane.
2. **Effectivity of the finite death depth for a bounded degree box**
   (Greenberg / quantitative Artin approximation on the explicit finite-type
   `Z_p` scheme of a box). Unchanged in content from my prior submission,
   demoted one place because (1) now has a concrete engine and (2) does not.
3. **The unbounded-total partial-`y` frontier `(8,12)`/`(9,12)`**, which
   remains the only live bounded-partial-`y` target and the free floor-raising
   engine for AS109.
4. The polynomial-limit criterion (uniform support/degree). Recorded again so
   the next lane does not rebuild a partial-`y` monovariant: the charged
   all-Witt control has `deg_y = 1` at every level and is uninformative.

---

## 3. New mechanism: the actual-total landing system is bigraded, and the
## bigrading types every certificate

This is the report's main contribution. Everything in §3.1–§3.6 is hand
algebra on frozen bytes and is reproduced in full so a reviewer never has to
take my word.

### 3.1 The frozen rows

Verbatim exact-`Q` V9 bytes, as displayed in the `T-rs` hostile review
(`xmodel/max12-812-order2-p0-total-rees-t-rs-rho-unit-v16-hostile-review-grok-20260826.md`
§2) and, for `Tg10_4`, in the charged `T-c1` hostile review `40ea0ff3…`:

```text
Tg10_1 = 5/16 rho^2 cs^3 k + 15/256 cs rs^2 k + 3/8 a0 c1 + 3/8 a1 c0
Tg10_2 = 15/64 rho^2 cs^2 rs k + 3/8 rho^2 a1 c1 + 5/1024 rs^3 k
         + 3/32 c1^2 + 3/8 a0 c0
Tg10_3 = 5/32 rho^4 cs^3 k + 15/512 rho^2 cs rs^2 k + 3/16 rho^2 a0 c1
         + 3/16 rho^2 a1 c0 + 3/16 c1 c0
Tg10_4 = 3/32 rho^2 c1^2 + 3/32 c0^2
Tg12_6 = 15/128 rho^4 cs^4 k + 45/1024 rho^2 cs^2 rs^2 k
         - 3/64 rho^2 rs a1 c1 - 3/16 rho^2 cs a0 c1 - 3/16 rho^2 cs a1 c0
         + 15/32768 rs^4 k - 3/256 rs c1^2 - 3/64 rs a0 c0 - 3/64 cs c1 c0
```

and, from the charged `T-cs` grade-14 review `7fbd9423…` §3, on the slice
`qrs=rho=qc0=qc1=e0=a0=ell1=0`:

```text
Tg12_2 = 3/32 e1^2 - 5/128 cs^4 k
Tg12_1 = (linear in ell2, coefficient -5/16 cs^3 k)
Tg14_5 = -3/64 cs e1^2 - 1/128 cs^5 k
```

*Consistency check performed first, as a review instrument.* The promoted
`(C1)` plus the promoted `Tg10_4` **determine** `Tg10_2` by polynomial division:
substituting `Tg10_4 = (3/32)(c0^2 + rho^2 c1^2)` into
`c1^3 = (32/3) c1 Tg10_2 - (128/3) a1 Tg10_4 - rs(...) - c0(4a0c1-4a1c0)`
cancels the `+-4 a1 c0^2` pair, and dividing the remainder by the variable `c1`
gives exactly the frozen `Tg10_2` above, coefficient for coefficient
(`(32/3)(3/32)=1`, `(32/3)(3/8)=4`, `(32/3)(15/64)=5/2`,
`(32/3)(5/1024)=5/96`). I did this before reading the review's display; the
agreement is a free, zero-compute cross-check of two independent promotions
and of the frozen `Tg10_2.poly` bytes. Any future lane can use the same trick:
*a promoted certificate over-determines the rows it consumes.*

### 3.2 Two independent gradings  [EXACT on the displayed rows]

Assign

```text
deg_s :  rs, cs, ell2 |-> 2 ;  c0, c1, a0, a1 |-> 5 ;  k |-> 4 ;
         e1 |-> 6 ;  rho |-> 0
deg_2 :  rs, cs, ell2, rho |-> 0 ;  c0, c1, a0, a1, e1 |-> 1 ;  k |-> 2
```

Then **every displayed monomial of every displayed row satisfies**

```text
deg_s(Tg{g}_j) = g          and          deg_2(Tg{g}_j) = 2.
```

Verification, monomial by monomial (30 monomials, no exceptions):

```text
Tg10_1  cs^3 k      6+4=10, 0+2=2      cs rs^2 k   2+4+4=10, 2
        a0 c1       5+5=10, 1+1=2      a1 c0       10, 2
Tg10_2  cs^2 rs k   4+2+4=10, 2        a1 c1       10, 2
        rs^3 k      6+4=10, 2          c1^2        10, 2
        a0 c0       10, 2
Tg10_3  cs^3 k / cs rs^2 k / a0 c1 / a1 c0 / c1 c0        all 10, all 2
Tg10_4  c1^2 / c0^2                                       both 10, both 2
Tg12_6  cs^4 k 8+4=12,2   cs^2 rs^2 k 4+4+4=12,2   rs a1 c1 2+5+5=12,2
        cs a0 c1 12,2     cs a1 c0 12,2            rs^4 k 8+4=12,2
        rs c1^2 2+10=12,2 rs a0 c0 12,2            cs c1 c0 12,2
Tg12_2  e1^2 12,2         cs^4 k 12,2
Tg12_1  ell2 cs^3 k 2+6+4=12, 0+0+2=2
Tg14_5  cs e1^2 2+12=14,2 cs^5 k 10+4=14,2
```

Solving the resulting linear system shows the grading lattice has **rank two**
and that these two are a basis (up to scale): from `Tg10_1` the two `k`-terms
force `deg(cs)=deg(rs)`; from `Tg10_2` they force `deg(rho)=0`; from `Tg10_4`
they force `deg(c0)=deg(c1)`; the `a`-`c` products then force
`deg(a_i)=deg(c_i)`; one free parameter remains, whose two integral
nonnegative normalizations are exactly `deg_s` and `deg_2`.
`deg_s` is the campaign's own sigma-grade (the row label **is** the degree);
**`deg_2` is the new one.** Its meaning is transparent once seen: the rows are
coefficients of a Jacobian bracket, hence quadratic in the level-two jet block
`{c0,c1,a0,a1,e0,e1}`, with the load `k` entering as a *square*
(`deg_2(k)=2`). Every row is a quadric plus a `k`-linear term:

```text
Tg{g}_j  =  v^T M_{g,j}(rs,cs,rho) v  +  lambda_{g,j}(rs,cs,rho,ell) * k ,
            v = (c0,c1,a0,a1,e0,e1,...).
```

`CONDITIONAL` hypothesis, and the only one: that all 21 charted rows plus every
other registered literal source relation are `deg_2`-homogeneous of degree 2
(equivalently, are quadrics-plus-`k`-linear), and that `deg_2 >= 0` on every
one of the 42 ring variables. I verified 7 rows and 30 monomials; the remaining
check is one text parse (Card A, stage 1).

### 3.3 Every promoted certificate is bihomogeneous with the forced bidegree
### [EXACT]

The three promoted certificates were found by search. The bigrading predicts
their exact shape. Write the staged form of the promoted calculus as

```text
f^N * s * (1 + rho W) = sum_j H_j (f y_j - f_j) + sum_m G_m q_m + sum_e L_e z_e.  (*)
```

Because `deg_s(rho) = deg_2(rho) = 0`, bihomogeneity forces `W` to be
bidegree `(0,0)`; because the `q_m` are `(g, 2)`, the cofactor `G_m` is
`(deg_s(LHS) - g, deg_2(LHS) - 2)`.

| chart | certificate | `(deg_s, deg_2)` of LHS | forced `G_m` bidegree for a grade-10 row | what the promoted certificate actually uses |
|---|---|---|---|---|
| `T-rs` | `35 rs^2 k U` | `(4+4, 0+2) = (8,2)` after chart division `(8,2)` | `(0,0)` | cofactors `32768, 4096, 8192 qcs, 12288 rho^2 qcs` — all bidegree `(0,0)`, since `qcs=cs/rs` is `(0,0)` |
| `T-c0` | `3 c0^2 (1+rho^2 qc1^2)` | `(10,2)` | `(0,0)` | cofactor `32` on `Tg10_4`; bilinear cofactor `3 rho^2 (c1+c0 qc1)` of bidegree `(5,1)` against a `(5,1)` bilinear |
| `T-c1` | `c1^3` | `(15,3)` | `(5,1)` | cofactors `(32/3) c1` and `-(128/3) a1`, both exactly bidegree `(5,1)` |

Every entry matches. In particular the `T-c1` certificate's cofactor space at
its type is the four-dimensional span `{c0,c1,a0,a1}` per row — a `4x2 = 8`
dimensional linear problem, not a Groebner search. **The bigrading would have
found `(C1)` by solving one tiny linear system.** That is the operational
payoff.

### 3.4 Theorem: on the `rs` and `cs` charts the `k`-localizer is forced
### [EXACT, given the §3.2 hypothesis]

**Claim.** In the presentation `(*)`, on the standard `J1` chart with
exceptional coordinate `f in {rs, cs}` and registered localizer `s = k^M`,
necessarily `M >= 1`.

**Proof.** On those two charts every ratio variable has `deg_2 >= 0`:
on the `cs` chart `qrs = rs/cs` is `deg_2 = 0` and `qc0, qc1` are `deg_2 = 1`;
on the `rs` chart `qcs` is `0` and `qc0, qc1` are `1`. Since
`deg_2(f) = 0`, the left side of `(*)` has `deg_2 = 2M`. Suppose `M = 0` and
take the `deg_2`-degree-`0` component of `(*)`. All chart variables have
`deg_2 >= 0`, so cofactors have `deg_2 >= 0`, so only generators of
`deg_2 = 0` can contribute: the single bilinear `f * q_other - other` with
`other in {rs, cs}` (bidegree `(2,0)`) and the ordered stratum equation
`rs` (bidegree `(2,0)`). Hence

```text
1 + rho W_0  in  ( cs*qrs - rs , rs )        [cs chart]
1 + rho W_0  in  ( rs*qcs - cs )             [rs chart]
```

Evaluate at `rho = 0` together with `rs = qrs = 0` (respectively
`cs = rs*qcs`): the left side is `1`, the right side is `0`. Contradiction.
Therefore `M >= 1`. `QED`

**Consequences.**

- The `D(k)` hypothesis in the promoted `T-rs` theorem is **structural, not an
  artifact of the particular V16 computation**. No amount of extra grades,
  extra rows, or a cleverer search removes it.
- The `k = 0` locus of the `rs` and `cs` charts is **provably outside the reach
  of the promoted certificate calculus**. The charged ledgers list `k=0` as an
  open item alongside "later charts"; it is not the same kind of item. This is
  the reranking in §2.1(2).
- The as-yet-unfound direct `T-cs` certificate **will** carry a genuine `k`
  localizer. Any V19 output typed with `M = 0` is wrong, independently of what
  its engine printed. That is a free negative control for a live AWS lane.

### 3.5 The complement is smaller than it looks: `k = 0` collapses `c0, c1`
### [EXACT, unconditional]

The mechanism §3.4 forbids is not the only mechanism. Set `k = 0` in the four
grade-10 rows and clear constants (`char != 2,3`):

```text
R1 := (8/3)  Tg10_1|_{k=0} = a0 c1 + a1 c0
R2 := (32/3) Tg10_2|_{k=0} = 4 rho^2 a1 c1 + c1^2 + 4 a0 c0
R3 := (16/3) Tg10_3|_{k=0} = rho^2 (a0 c1 + a1 c0) + c1 c0
R4 := (32/3) Tg10_4|_{k=0} = rho^2 c1^2 + c0^2
```

Then `R3 - rho^2 R1 = c1 c0`, so `c0 c1 = 0` on the locus. Split:

- `c1 = 0`: `R4` gives `c0^2 = 0`, so `c0 = 0`.
- `c0 = 0`: `R4` gives `rho^2 c1^2 = 0`. If `c1 != 0` then `rho = 0`, and then
  `R2` reads `c1^2 = 0`, contradiction. So `c1 = 0`.

**Theorem.** `V(k) cap V(Tg10_1, Tg10_2, Tg10_3, Tg10_4) subset V(c0, c1)`,
set-theoretically over any field of characteristic `!= 2,3`.  Adding the other
17 rows only shrinks the locus, so the containment holds on the full source
scheme.

**Consequences.**

- On the `c0` and `c1` charts, `V(k)` forces the exceptional coordinate itself
  to vanish, hence forces `rs = cs = c0 = c1 = 0`: the `k = 0` complements of
  those two charts lie **entirely inside `V(J1)`**, i.e. inside the second
  stage. They are not separate obligations at all.
- On the `rs` and `cs` charts, `V(k)` forces `qc0 = qc1 = 0` (since
  `c0 = f q_{c0}` with `f` a nonzerodivisor on the blowup). The residual is a
  codimension-two, explicitly cut out sublocus of the chart, not a chart.

So the bottleneck newly ranked #2 in §2.1 comes with an immediate, exact,
zero-compute reduction. That pairing — *the grading says the standard tool
cannot reach `k=0`; the `k=0` collapse says a two-line hand argument does* —
is the report's strongest single package.

### 3.6 Stage two is row-disjoint from stage one  [EXACT, scope-hostile]

Every monomial of `Tg10_1, Tg10_2, Tg10_3, Tg10_4, Tg12_6` contains at least
one of `rs, cs, c0, c1`. Hence all five lie in `J1 = (rs,cs,c0,c1)` and
**vanish identically on `V(J1)`**. These are exactly the rows consumed by the
four promoted certificates (`T-rs` uses rows 1,2,3 and `Tg12_6`; `T-c0` uses
row 4; `T-c1` uses rows 2 and 4).

By contrast `Tg12_2` contains the term `(3/32) e1^2`, which survives
`rs=cs=c0=c1=0`; on `V(J1)` (with the other five slice variables zero) it reads
`(3/32) e1^2`, giving `e1 = 0` radically.

**Therefore the `J2 = (a0,a1)` charts over `A/J1` and the terminal receiver
`V(J1+J2)` receive *zero* information from the entire row set that closed
stage one.** The "four `J1` charts, two `J2` charts, one receiver" arithmetic
of the staged calculus is correct as a *cover*, but it is not a cost estimate:
stage two is a fresh computation on a disjoint row support. Any plan that
budgets it as "two more certificates of the same shape" should be corrected
now, before capacity is committed.

### 3.7 Typed prediction for the live direct-`T-cs` search  [CONDITIONAL]

Combine §3.2, §3.4 and the promoted grade-14 fibre theorem.

- The promoted fibre theorem says the grade-10–12 prefix fibre on `D(cs*k)` is
  a nonempty (irreducible, rational, 31-dimensional) variety. Hence grades
  10–12 alone **cannot** certify emptiness: reducing `(*)` modulo `rho` and
  localizing at `cs*k` would otherwise give `1` in an ideal with a zero.
  A row of grade `>= 13` is mandatory; in the frozen set that is `Tg14_5`,
  which must appear with a nonzero cofactor.
- Bidegree bookkeeping on `(*)` with `f = cs`, `s = k^M`, `q_m = Tg14_5`:
  `deg_s(G_m) = 2N + 4M - 14 >= 0` and `deg_2(G_m) = 2M - 2 >= 0`.

**Prediction.** The direct total `T-cs` certificate has type

```text
M >= 1        and        N + 2M >= 7 ,       minimal type (N,M) = (5,1),
```

i.e. `cs^5 * k * (1 + rho W)` with `deg_s(W) = deg_2(W) = 0`. At that minimal
type the cofactor spaces are completely determined: the `Tg14_5` cofactor is a
constant in `Q[rho, qrs]`; the grade-10 cofactors have bidegree `(4,0)`, i.e.
`Q[rho,qrs]`-combinations of `{rs^2, rs cs, cs^2, rs ell2, cs ell2, ell2^2}`;
the `c`-bilinear cofactors have bidegree `(9,1)`; the `rs`-bilinear and
stratum cofactors have bidegree `(12,2)`.

This is a **finite explicit linear system**, not a 26-generator ideal
membership lift. It is also consistent with the promoted numerics: on the
prefix fibre `Tg14_5 = -(7/256) cs^5 k`, whose bidegree is exactly `(14,2)`,
matching `cs^5 k` at `(N,M) = (5,1)`.

---

## 4. Second new mechanism (disproof side): the exact source-gauge group of
## the AS109 lift set

### 4.1 The group  [EXACT]

Let `R = Z_109`, and let

```text
L = { (A,B) in R[x,y]^2 : P = x - x^109 + 109A, Q = y + 109B, det J(P,Q) = 1 }.
```

**Claim.** For every `tau in R` (not merely a Teichmüller lift of `F_109`, and
not merely `tau in 109R`), the source translation `sigma_tau(x,y) = (x+tau, y)`
maps `L` to `L`, and the action of `R` on `L` so defined is **free**.

*Proof.* `det J` is preserved by any source automorphism of determinant one.
For the congruence: `(x+tau) - (x+tau)^109 = (x - x^109) + (tau - tau^109) -
sum_{i=1}^{108} C(109,i) tau^{109-i} x^i`, every binomial coefficient
`C(109,i)`, `1 <= i <= 108`, is divisible by `109`, and `109 | tau - tau^109`
by Fermat's little theorem in `R`. Hence `P(x+tau,y) equiv x - x^109 (mod 109)`
and `Q(x+tau,y) equiv y (mod 109)`. Freeness: `P(x+tau,y) = P(x,y)` for
`tau != 0` would force `P` independent of `x`. `QED`

Explicitly, `A |-> A^tau` with

```text
A^tau(x,y) = A(x+tau, y) + (tau - tau^109)/109
             - sum_{i=1}^{108} [ C(109,i)/109 ] tau^{109-i} x^i ,
B^tau(x,y) = B(x+tau, y).
```

Note `(tau - tau^109)/109` is the Fermat quotient: `R`-valued but **not** a
polynomial with `R`-coefficients. So the action is integral yet not
`R`-polynomial in `tau`, and it does not descend to a well-defined action of
`F_109` on the special fibre — it depends on `tau` modulo `109^2`. That is the
Witt-level-two signature and is exactly what one should expect here.

**Relation to charged prior art, stated carefully.** The charged wild-symplectic
gate (`xmodel/as109-wild-symplectic-conductor-gate-20260824.md`) records that
the *deck* translations of the reduction lift to a free determinant-one
**restricted-analytic** `C_p` action on the completed bidisc, and that this
action does **not** descend to a rational or polynomial deck action. That is a
different object: the deck action would require `F o sigma_tau = F`, which is
false. What is claimed here is an exact **polynomial action on the moduli of
lifts** — `F o sigma_tau` is a *different* lift of the same reduction. The two
statements are compatible and neither implies the other.

### 4.2 An explicit gauge section  [EXACT, with its scope]

Let `phi(A) = [x^108 y^0] A`. From the `i = 108` term above,
`C(109,108)/109 = 1`, so

```text
phi(A^tau) = sum_{j >= 108} C(j,108) tau^{j-108} [x^j y^0]A  -  tau .
```

If `deg_x A <= 108` this is `phi(A) - tau` exactly: `phi` is an
`R`-equivariant coordinate on the orbit, and the unique `tau` with
`phi(A^tau) = 0` is `tau = phi(A)`.

**Corollary.** Every AS109 lift with `deg_x A <= 108` may be normalized, within
its translation orbit and without leaving `L`, so that `[x^108 y^0]A = 0`.
For `deg_x A > 108` the gauge equation is a polynomial of degree
`deg_x A - 108` in `tau` with `R`-coefficients and a `-tau` term; solvability
is a Newton-polygon/Hensel question, not automatic.

The `AS109 SUPPORT GRAMMAR STOP` ledger entry records, as the reason for the
stop, that *"no finite exhaustive graph exists without a proved gauge section
or groupoid transition rule"*. The corollary is a proved gauge section for the
translation subgroup — one of the two named missing ingredients, supplied for
one subgroup. It does not supply the section for the `(x + 109 y^m, y)`
triangular family that generated the stop, and I claim nothing about that.

### 4.3 The avenue this opens: the arithmetic `(deg_y, v_109)` Newton polygon
### [SPECULATION with an exact first corner]

For `f = sum_j f_j(x) y^j in R[x,y]` let `S(f) = { (j, v(f_j)) }` with `v` the
Gauss valuation on `R[x]`, and `NP(f)` its lower convex hull. For an AS109 lift

```text
S(P) contains (0,0) and lies in { j >= 1 => v >= 1 } ;
S(Q) contains (1,0) and lies in { j != 1 => v >= 1 } .
```

For a weight `w >= 0`, `v_w(sum f_j y^j) = min_j ( v(f_j) + j w )` is a
valuation. At each `w` where the `v_w`-leading forms of `P` and `Q` have a
nonzero Jacobian bracket, the constancy `J = 1` forces a numerical equality;
where the bracket vanishes, the leading forms are algebraically dependent and
one obtains a corner equation of exactly the shape

```text
p_m^n = c q_n^m ,   p_m = alpha h^a , q_n = beta h^b ,  m = da, n = db,
```

with the associated shear `P |-> P - c Q^{m/n}` (or `Q |-> Q - c' P^{n/m}`)
integral precisely when `v(alpha) >= (m/n) v(beta)` (respectively the mirror).
**`AS-TRI` is exactly the `n = 1` corner**: there `v(beta) = v(q_1) = 0` and
`v(alpha) = v(p_m) >= 1`, so the shear is integral and residue-preserving, and
the ladder terminates in a contradiction. For `n >= 2` the seed forces
`v(beta) >= 1` and the sign of `v(alpha) - (m/n) v(beta)` is no longer
automatic — that is precisely the obstruction, and it is a **slope condition on
`NP(P)` and `NP(Q)`**, i.e. finite combinatorics for each `(m,n)`.

The `x`-side is not symmetric and that asymmetry is itself information: if
`deg_x(109A) < 109` then `P_M = -1` is a constant, which forces the top-`x`
coefficient `Q_N` of `Q` to be constant in `y`; and the `x`-side shear
`P |-> P - c Q^{M/N}` is *nonintegral* (`v(c) <= -109`) while the mirror shear
`Q |-> Q - c' P^{N/M}` is integral. So descent on the `x` axis runs in exactly
one direction. Building the two-axis polygon and its admissible slope sequences
is the concrete proposal (Card C).

---

## 5. New connections between existing avenues

### 5.1 Every promoted result of this campaign is *selection-scoped*, and the
### staged calculus contains the only proved covering lemma  [NAVIGATION]

Three superficially unrelated lanes share one logical shape.

| lane | selection made | covering lemma |
|---|---|---|
| landing / Rees (`T-c1`) | "the **ordered** registered stratum", explicitly not the unordered standard chart | **PROVED**: standard charts cover `Proj` and least-index ordered strata cover set-theoretically (staged calculus `16ec6f54…`) |
| GGV5 / prime ray | "**globally minimal** standard pair"; explicitly inapplicable to nonminimal prime shears | **MISSING**: the arbitrary-standard-pair bridge |
| order two / D1 / affine Faber | "the **normalized** chart on `D(p k0)`, `D(J)`, `D(E M)`, …" | **MISSING**: the literal source/landing composition |

The staged calculus's covering argument is the campaign's *only* discharged
selection debt, and it is discharged by a well-ordering (least index), not by
new geometry. That is a usable template: **every selection-scoped promotion
should be required to name its covering lemma at promotion time, and the
covering-lemma ledger — not the theorem ledger — is the campaign's real
critical path.** Concretely I propose the coordinator add one column
("covering lemma: proved / named-open / absent") to the promotion ledger. On
today's state that column has one `proved` and roughly a dozen `absent`, and
it collapses bottlenecks 2.1(3), 2.1(4) and 2.1(5) into one measurable
quantity.

### 5.2 Row 1's engine, in the arithmetic direction (rows 1 × 19/21)

Row 1 is a Newton-polygon corner-emptying engine, mature and heavily tooled,
whose *deliverable type* I argued last round is `B_GGV`-valued and cannot reach
the partial-`y` frontier. §4.3 says the AS109 lift problem carries a completely
untried Newton polygon in the `(deg_y, v_109)` plane whose corners are the same
kind of object (leading forms that are powers of a common `h`, with a
degree-lowering shear at each corner). The corner engine is therefore
transplantable to a lane whose deliverable *is* frontier-relevant. This is a
tooling connection, not a mathematical implication: the arithmetic polygon has
an extra integrality datum at each corner that the geometric one lacks, and
that datum is what makes `AS-TRI` work.

### 5.3 Row 18 × row 31 (already stated, recorded here as the second half of
### the required connection)

The bigrading of §3 is a rank-two torus acting on the landing system. Row 18's
closure was about counterexamples, not about the campaign's charts. Equivariant
Groebner/linear algebra over the torus is the correct instrument for §3.7, and
would have produced `(C1)` mechanically. Two lanes previously believed disjoint
share an object.

---

## 6. Strongest proof attack and strongest falsification attack

### 6.1 Strongest proof attack — type-directed closure of the `J1` stage,
### including its localizer complements

Target: close the whole first stage of the staged tree, *including* `V(k)`,
which the current instrument provably cannot reach.

Three steps, in order, none blocking the others:

1. **Confirm the bigrading** (Card A stage 1, minutes). This upgrades §3.4 and
   §3.7 from `CONDITIONAL` to `EXACT`.
2. **Synthesize the direct `T-cs` certificate at type `(5,1)`** by exact linear
   algebra over the forced cofactor spaces (Card A stage 2). If `(5,1)` is
   infeasible, walk `(N,M)` with `N + 2M >= 7`, `M >= 1`. This replaces V19's
   untyped 26-generator lift.
3. **Close `V(k)` by the collapse theorem** (Card B): on the `c0`/`c1` charts
   `V(k)` lies inside `V(J1)` and is discharged by the stage-two argument; on
   the `rs`/`cs` charts `V(k)` lies in `V(qc0,qc1)`, where the presentation has
   two fewer ratio variables and the rows lose every `k`-term, becoming pure
   quadratic forms in `(c0,c1,a0,a1,e0,e1)` over `Q[rho, rs, cs, ell]`.

Why this beats the alternatives (TD6 H19R2, D1 residual cells, affine-Faber
`H16`): it is the only attack in the portfolio whose *remaining* obligations
have a computed shape rather than an estimated one, and step 3 addresses a
bottleneck that step 2's instrument is proved unable to touch, so the two are
not redundant.

Honest ceiling: this closes one collision family's first stage inside order
two. It is not a landing theorem, it does not cover other load rays, and it
leaves the deck/square bridge, the receiver, and the cofinal ceiling untouched.

### 6.2 Strongest falsification attack — walk the arithmetic Newton polygon
### to decide AS109 lift existence

Target: convert the AS109 floor ladder from one hand-proved corner per lane
into an engine.

Deliverable A (exclusion): a proof that no admissible slope sequence exists
for any `(deg_y P, deg_y Q)`. That is a **nonexistence theorem for exact AS109
polynomial lifts** — it would retire the campaign's most-developed
counterexample seed outright and free essentially all disproof capacity. It
would *not* prove JC2 and must not be advertised as progress toward one.

Deliverable B (lead): an admissible slope sequence. Then the search target is
a specific corner shape with prescribed `h`, `a`, `b`, and valuations — a far
smaller object than any support rectangle the campaign has enumerated, and one
that composes with the `(8,12)`/`(9,12)` frontier machinery through the
already-charged floor argument.

Ingredients already in hand: `AS-TRI` as the `n = 1` corner and as a positive
control; the one-directional `x`-side descent of §4.3; the gauge section of
§4.2 to remove the translation redundancy before any enumeration; the promoted
Hensel noninjectivity as the terminal contradiction.

I again record the negative control from my prior round so it is not rebuilt:
a partial-`y`-degree monovariant is useless here, because the charged all-Witt
control has `deg_y = 1` at every level.

---

## 7. Software acceleration / decisive experiment

**A bigrading validator and type-directed certificate synthesizer.**

*Stage 1 — the decisive experiment (minutes, local-legal at this size).*
Parse the 22 frozen `.poly` files plus every registered source relation; build
the integer matrix of monomial exponents; solve for the full lattice of
gradings under which every row is homogeneous. Emit:

```text
grading_lattice_rank = ...
all_rows_homogeneous = true/false
per_variable_degrees  = ... (both basis gradings)
nonneg_on_chart[rs|cs|c0|c1] = true/false
forced_localizer_power_M_min[chart] = ...
forced_type_bound[chart]  =  N + 2M >= ...
```

This is decisive in the campaign's sense: it either promotes §3.4 and §3.7 to
theorems and hands the live V19 lane two free negative controls, or it falsifies
my hypothesis at zero cost by exhibiting one inhomogeneous row.

*Stage 2 — the accelerator (AWS, exact `Q` plus one good prime).*
Given the bidegrees, enumerate the finite monomial bases of every cofactor slot
at a requested type `(N,M)` and solve one exact linear system for `(*)`. Emit a
certificate in the promoted type fields (exceptional power / genuine localizer /
stratum equations / `rho` cofactor) plus a replay expansion. Fail closed if any
cofactor slot is empty at the requested type, and print the next feasible type.

Why this and not more raw compute: the campaign's binding constraint is review
latency, and a typed certificate is reviewable by expansion plus a scope audit
rather than by bespoke rederivation. The bidegree data additionally *bounds the
search a priori*, which is what turns "run V19 for twelve hours and hope"
into "solve a linear system of known size". It also generalizes: the same
validator run on the D1, affine-Faber and TD6 row sets would type their
localizers (`D(p k0)`, `D(J)`, `D(E M)`, `D(U H B3)`) the same way, and I
predict — SPECULATION, cheaply testable — that several of those localizers are
likewise forced rather than incidental.

---

## 8. Idea cards

### Card A — Confirm the bigrading, then synthesize `T-cs` at its forced type

- **Type:** `NEW`. The single grading by sigma-grade is used elsewhere in the
  campaign (D1/affine-Faber "tails homogeneous of weight `12+i`"); the second
  grading `deg_2`, the rank-two lattice, and the certificate typing are not
  recorded anywhere I could find in the charged corpus.
- **Dependencies:** frozen V9/V17 `.poly` bytes and their manifest; the
  promoted staged calculus `(*)`; the promoted `T-cs` grade-14 fibre theorem
  (used only to argue `Tg14_5` must appear). Independent of V19's outcome.
- **Cheapest discriminator:** stage 1 above — one text parse and one integer
  linear solve over 22 files. Cost: minutes.
- **Interpretation of every outcome.**
  *All rows bihomogeneous, `deg_2 >= 0` on the `rs`/`cs` charts:* §3.4 and
  §3.7 become theorems. Immediately (i) impose `M >= 1` and a nonzero
  `Tg14_5` cofactor as V19 acceptance gates, (ii) launch stage 2 at `(5,1)`.
  *All rows bihomogeneous but some chart variable has `deg_2 < 0`:* the
  `M >= 1` argument fails on that chart; record which one and why, and keep
  the type bounds that survive (`deg_s` alone still bounds `N + 2M >= 7`).
  *Some row is inhomogeneous:* my hypothesis is false, the typing collapses,
  and the campaign has learned in minutes that the landing system is *not*
  torus-equivariant — which is itself worth knowing, because it explains why
  certificate search has needed Groebner machinery.
- **Stop condition:** stop stage 2 after two consecutive infeasible types with
  no new structure; that triggers the two-non-informative-attempts rule and
  forces a different `J1` generating set.
- **Expected information gain:** high, at near-zero first-stage cost. It types
  a live AWS lane, supplies two negative controls, and either bounds or refutes
  the shape of every future landing certificate.

### Card B — Close the `k = 0` complements using the collapse theorem

- **Type:** `NEW`. `k = 0` is listed as an open item in every recent overlay
  and `LIVE STATE`; I found no charged attempt and no statement that it forces
  `c0 = c1 = 0`.
- **Dependencies:** the four frozen grade-10 rows only. §3.5 is complete as
  written; no compute is required to establish it. The follow-on needs the
  chart presentations already built for `T-rs`/`T-cs`.
- **Cheapest discriminator:** hostile review of §3.5 by hand from the frozen
  bytes (a different model, twenty minutes, no CAS). Then, on the `cs` chart,
  restrict the presentation to `V(k) cap V(qc0,qc1)`, where every row loses its
  `k`-terms and becomes a quadratic form in `(c0,c1,a0,a1,e0,e1)` over
  `Q[rho, rs, cs, ell]`, and test emptiness of the `rho = 0` fibre there.
- **Interpretation of every outcome.**
  *§3.5 confirmed and the restricted fibre is empty:* the `k = 0` complements
  of all four `J1` charts are discharged, and bottleneck 2.1(2) closes without
  ever needing a certificate of the forbidden type.
  *§3.5 confirmed, restricted fibre nonempty:* the campaign has an explicit,
  small, fully written-out residual locus for the first time, instead of an
  unexamined "`k=0`" line item. That locus is then the correct target.
  *§3.5 refuted (a sign or coefficient misread):* one of the two displayed row
  sets is wrong, which is itself a high-priority custody finding, since both
  displays are charged review artifacts.
- **Stop condition:** stop if the restricted quadratic system needs a row of
  grade `> 14`; that would mean `k = 0` is not cheaper than the main chart and
  should be rescheduled behind stage two.
- **Expected information gain:** high and almost free. It is the only item in
  this report whose main theorem is already proved in the report itself.

### Card C — The arithmetic `(deg_y, v_109)` Newton polygon for AS109

- **Type:** `NEW` as an engine; `KNOWN` in its first corner (`AS-TRI`,
  promoted) and in its ingredient facts (Gauss valuation, leading-form powers).
  The `x`-side one-directionality and the gauge section of §4.2 are new.
- **Dependencies:** `AS-TRI` `696152da…`; the reviewed two-sided floor
  `>= 12`; the promoted Hensel noninjectivity; §4.1–§4.2 (proved here). No
  charged artifact is contradicted. No AWS needed for the first stage.
- **Cheapest discriminator:** by hand, for `n = deg_y Q = 2` only, write the
  top two Jacobian coefficient rows, extract the corner equation
  `p_m^2 = c q_2^m`, and decide whether the seed congruence forces
  `v(alpha) >= (m/2) v(beta)` or forbids it. One bounded lane.
- **Interpretation of every outcome.**
  *Integrality forced:* the ladder extends and `deg_y B >= 3` follows, raising
  the one-sided floor for free and giving strong evidence that the engine walks
  all corners.
  *Integrality forbidden for some `m`:* the obstruction is located exactly, and
  the surviving `(m,2)` shapes are a short explicit list — the first genuinely
  small AS109 search target.
  *Neither, because the second row does not close:* the corner needs the next
  polygon vertex; record which, and either continue or stop with a named
  vertex, which is still more than the current one-lane-per-degree ladder gives.
- **Stop condition:** hard stop after `n = 2` and `n = 3` if neither yields a
  determinate integrality verdict. Do not enumerate supports; do not launch a
  rigid-congruence leaf computation (the charged `Z_109`-flat model still does
  not exist).
- **Expected information gain:** medium-high, asymmetric. Cheap, and the only
  proposal that could retire the campaign's principal counterexample seed.

---

## 9. `continue / redesign / stop` for current major lanes

| Lane | Verdict | Reason (scope-hostile) |
|---|---|---|
| Landing / actual-total Rees (root, Gate T) | **continue, retype the obligation ledger** | Correct root; three of four `J1` charts closed in 24h. Retype: add the forced `(N,M)` per chart (§3.7), move `k=0` from "later chart" to "outside the instrument, see Card B" (§3.4/§3.5), and correct the stage-two budget (§3.6). |
| V19 direct `T-cs` lift | **redesign** | Replace the untyped 26-generator membership lift by the type-directed linear system at `(N,M)` with `M >= 1`, `N + 2M >= 7`. Impose two acceptance gates now, before harvest: a nonzero `Tg14_5` cofactor, and `M >= 1` after inverse variables `u,v` are cleared. A returned lift failing either is wrong regardless of engine output. |
| Opus5 independent direct-`T-cs` search | **continue, retargeted** | Point it at the minimal type `cs^5 k (1 + rho W)` with the forced cofactor spaces rather than a free-form search. |
| TD6 H19R2 | **continue as designed** | The design (`8b462a91…`) is fail-closed, reuses H15 rather than forking it, and has a complete negative-control list including the source-addend omission and the `F`-omission. Its Stage 5 denominator clearing is itself a localizer-typing step; the same bigrading validator applied to the TD6 row set may bound it a priori. Do not launch before the root static audit the `LIVE STATE` already requires. |
| D1 residual cells / composition | **continue** | Near closure, mechanically complete producer, cheap to finish. |
| Affine-Faber order-two fan (`H16` and beyond) | **redesign** | Unchanged from my prior round and now overdue: the `(H,q) = (16,6)` control showed graph deviations absorbing the grade-44 obstruction, which is the signature of a fan without a well-founded ranking. A third serial `H` increment needs written justification under the campaign's own two-attempt rule. |
| Prime ray / GGV5 (`3P-E31`) | **redesign, gated** | Keep the bounded source-typing/bandwidth preflight with `p=23` fit-plus-one and `p=31` holdout. Gate all further proof work behind the arbitrary-standard-pair bridge; §5.1 additionally reclassifies that bridge as one instance of a portfolio-wide covering-lemma debt, which raises its priority-by-exposure. |
| Counterexample side (AS109 / Witt) | **redesign** | Retarget from serial fixed-`deg_y` no-gos to the arithmetic polygon (Card C), with the gauge section (§4.2) applied first to any enumeration. The paid rigid-congruence leaf computation stays held: no charged `Z_109`-flat model exists. |
| `G2-PSC` | **stop (zero allocation, keep documented)** | No live lane imports a GGV packet as Sigray input; a pure-Sigray architecture bypasses it. Reactivate only when a lane proposes the hybrid import. |
| `G2-BD` | **stop (dormant)** | Begins only after a residue-A datum is reached; no live lane reaches one. |
| Software / certificates | **continue, §7 stage 1 as the next deliverable** | Minutes of work, decides two open questions, types a live AWS lane. |
| Formalization (`jc2-lean`) | **continue asynchronously** | Separately owned and read-only; must never gate discovery. |

---

## 10. Explicit nonclaims

- No proof or disproof of JC2, of Gate T, of any partial-`y` frontier family,
  of whole TD6, of order two, of `3P-E31`, or of AS109 lift existence or
  nonexistence.
- §3.2's bigrading is verified on 30 monomials of 7 rows. The statements that
  depend on *all* rows being bihomogeneous — §3.4's `M >= 1` and §3.7's type
  bound — are `CONDITIONAL` on the Card A stage-1 check and must not be cited
  as theorems before it returns.
- §3.5 (`V(k) cap V(Tg10_1..4) subset V(c0,c1)`) is unconditional given the
  frozen bytes, but it is a set-theoretic containment on the grade-10 locus. It
  asserts nothing scheme-theoretically, nothing about nilpotents, and nothing
  about whether the residual `V(k) cap V(qc0,qc1)` locus is empty.
- §3.6 concerns the five rows I could read verbatim. It does not claim all 21
  rows lie in `J1`; `Tg12_2` demonstrably does not.
- §4.1 asserts an action on the *set of lifts*. It is not a deck action, does
  not contradict the charged wild-symplectic gate, and does not assert that any
  lift exists.
- §4.3 is a research programme, not a theorem. Its only proved corner is the
  already-promoted `AS-TRI`.
- §5.1 is a navigation/process claim. It asserts no defect in any promoted
  result; every result it lists is taken as correct at its stated scope.
- Nothing here changes the classical frontier gate: fixed or capped
  actual-total-degree-at-most-12 scopes remain closed, and the unbounded-total
  partial-`y` `(8,12)`/`(9,12)` families remain `NOT_CLOSED_BY_THIS_GATE`.
