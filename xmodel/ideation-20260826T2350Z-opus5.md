# Blind whole-portfolio submission — Opus 5 lane

Round ID: `20260826T2350Z`
Lane: Opus 5, standing blind whole-portfolio researcher
Date: 2026-08-26

## 0. Basis, tool boundary, and evidence language

Charged basis verified locally by rehash before writing; all seven packet
hashes match the freeze exactly:

```text
README.md       f09aefd11cb776c4af9e56b3f5d24501c6d6d7a692f9a26874dd40b0f5e1c44a
COORDINATION.md d5ca2421fdaaf7fac2f142e3fb0f96bf58c181047f092c3434a970d50dcde812
PROGRESS.md     efa2b93161a2fc8ab3b811f670f33f307f7a62c660672d67c3faf5317373e863
APPROACHES.md   26b2e7c18c632e8d217240c34a1b53a46b98f81fb287170b90a965146a8ae0cf
AUDIT.md        faf2c2e3c43d676a79c4a6bc8ae6728706138cb3465ff24e51fe6a3ec638606c
notes.md        ca04b02f534eb41215cfb3f523f8bf5b97aba09075890f2d3e03c4d83abf551c
ladder/REDUCTION.md f0fca49811349483c437d674ab819065eb09500330516d161978868c71bf6371
```

Also read, as charged artifacts named by the freeze or required to
deduplicate: the three new promotions and the `3p` review
(`2c7f624c...`, `4120d6b6...`, `2f5859cb...`, `7f3fd203...`), the `3p`
producer note, the `T-rs` promotion, the Gate-T obligation table
`xmodel/max12-812-order2-p0-total-rees-gate-t-obligation-table-20260826.md`,
the prior round's synthesis
`xmodel/ideation-significant-news-20260826T1740Z-root-synthesis.md`, and
`ladder/SHEET6-CLASSICAL.md` §4.  I did not open the V19 freeze (it is a
case artifact, not present as a charged `.md`); nothing below depends on it.

No other `xmodel/ideation-20260826T2350Z-*.md` file was opened.  No web
access, no heavy computation, no AWS mutation, no `jc2-lean` access.  Local
work was limited to `cat`/`sed`/`grep`/`shasum` and two hand arithmetic
checks reproduced in full below.  This report is my only repository edit.

Evidence labels used throughout:

- **EXACT** — proved here, by hand, in this document, from stated hypotheses.
- **CHARGED** — restatement of an already promoted or reviewed repository
  result; I add no evidence.
- **CONDITIONAL** — an implication whose hypothesis is not discharged here.
- **NAVIGATION** — orientation, not a claim.
- **SPECULATION** — explicitly unproved proposal.

---

## 1. Disposition vector over all 46 master-table avenues

Compact vector, in row order.  Reasons follow for every non-`unchanged`
entry; unchanged rows are unchanged because no charged event in this round's
window touches their stuck-point.

```text
 1 lower      2 unchanged   3 unchanged   4 unchanged   5 raise
 6 unchanged  7 raise       8 unchanged   9 unchanged  10 unchanged
11 unchanged 12 unchanged  13 unchanged  14 unchanged  15 unchanged
16 unchanged 17 unchanged  18 unchanged  19 unchanged  20 unchanged
21 raise     22 unchanged  23 unchanged  24 unchanged  25 unchanged
26 unchanged 27 unchanged  28 unchanged  29 unchanged  30 unchanged
31 raise     32 unchanged  33 unchanged  34 unchanged  35 unchanged
36 unchanged 37 unchanged  38 unchanged  39 unchanged  40 unchanged
41 unchanged 42 unchanged  43 unchanged  44 unchanged  45 unchanged
46 unchanged
```

**Row 1 — GGV corner families + degree farm: `lower`.**
Two independent reasons.  (a) CHARGED: the promoted prime-ray theorem
retires exactly this row's stated essence ("enumerate corner families below
a degree cutoff"): the one-edge final-chain count `(3p-13)/4` and the
`MN`-viable count `(p-3)/2` grow linearly in `p`, and
`Omega((3p-1)/4)` is unbounded, so no `p`-independent literal menu and no
`Delta0 | C(3)*p^e` shortcut exists.  (b) EXACT/scope, §4 below: every
GGV5-interface result is scoped to a *globally minimal* standard pair, so
its deliverable type is `B_GGV != G`, not "no counterexample has
gcd `G`".  That type cannot discharge the partial-`y` frontier obligations
which the rest of the portfolio actually consumes.  The row's *parametric*
successor (`3P-E31`) keeps value; the row as written should be ranked as a
`B_GGV`-value lane and priced against a cofinal programme, not against
`(9,12)`.

**Row 5 — Jung–van der Kulk degree descent: `raise`.**
CHARGED: the promoted prime-ray note names, as one of exactly two sufficient
routes to `3P-E31`, "every one of its solutions supplies a licensed
polynomial degree reduction contradicting global minimality".  That is a
Moh/JvdK-type descent used as a *component* of the campaign's top GGV lane,
not as a standalone JC2 programme.  Row 5's recorded stuck-point ("cusp
leading forms block triangular shears"; "amalgam rigidity never bites on
non-automorphisms") is about the standalone programme and does not apply to
this consumer.  A row with a live named client outranks a row with none.

**Row 7 — Jelonek asymptotic variety `A(F)`: `raise`.**
Three charged facts compose.  (a) `ladder/SHEET6-CLASSICAL.md` §4 records
`A(F)` as PASS-consistent at the td=6 template with exact `mu(F)=6`, and
explicitly registers the Abhyankar–Moh-semigroup test *on the `A(F)`
components* as "a fresh kill test not run here".  (b) Chau's Theorem 4.4
— the polynomially-parametrized structure of the fiber-deficit set — is
already a **load-bearing refereed external input** to `T7`, i.e. the
campaign already depends on `A(F)`-type structure without treating it as an
object.  (c) The whole of the D1 / order-two / landing programme is an
arc-emptiness calculus: each promoted chart certificate is, on its
registered stratum, an `A(F)`-emptiness certificate.  `A(F)` is the only
candidate *global* receiver in the portfolio whose finiteness and
one-place-rational-component structure are published theorems rather than
campaign obligations.  That makes it the cheapest candidate answer to
`REDUCTION.md` §5.1 ("define the endpoint").  I raise the row without
claiming it resolves coverage: covering all arcs is still the wall.

**Row 21 — p-adic injectivity / Hensel: `raise`.**
CHARGED: the AS109 109-ball Hensel noninjectivity theorem is now the
load-bearing hypothesis of the only promoted theorem that converts
proof-side partial-`y` progress into counterexample-side exclusion (the
floor-12 composition, `c76f26a6...` / `430ffa3c...`).  Every future
max-`N` partial-`y` theorem raises that floor for free.  Row 21 is
therefore no longer a standalone low-yield lane; it is a *multiplier* on the
main proof lane, and it is the correct home for the new joint system in §5.

**Row 31 — Integrality / ZMT / Rees valuations: `raise`.**
CHARGED: this round produced the campaign's first promoted **actual-total
Rees chart theorem** (`T-rs` rho-unit lemma, `52b59e8d...`): a saturation
of an explicit Rees chart, with a valuative (DVR-arc) conclusion.  Row 31's
recorded status was "No direct attempt".  It is now executing.  Lemma 3.1
below makes the remaining charts strictly cheaper than the frozen
obligation table assumes, which further raises the row.

Rows 2, 3, 4, 6, 8–20, 22–30, 32–46 are `unchanged`.  In particular row 19
(char-p/Witt) is unchanged despite the floor-12 composition: the floor is a
*consequence* of proof-side progress and changes nothing about row 19's own
recorded stuck-point (bounded-support-or-polynomial-limit criterion).  Row 6
is unchanged only because its raise is entirely contingent on row 7; if the
row-7 experiment in §7 Card A' is run, row 6 raises with it.

---

## 2. Reranked principal bottlenecks

### 2.1 Proof side

1. **Absolute or cofinal complexity/type ceiling.**  Unchanged at #1.
   `REDUCTION.md` §7.2 is decisive: `KJN(C)` is *type-relative*
   (`deg(Psi) <= C (alpha beta)^2 => td <= C alpha beta`) and becomes a
   ceiling only after an independent bounded `(alpha,beta)` type menu with
   provenance.  No charged artifact supplies that menu.  Every finite
   sector kill is orthogonal to this.
2. **Universal full-configuration landing/coverage** (`T9`/`T10`).
   Composite single-pole, general off-axis (`0 DEAD/0 ALIVE/2691 OPEN`),
   and post-jump mixed contexts are all `NOT ESTABLISHED`.  Unchanged at #2.
3. **The arbitrary-standard-pair bridge — promoted from a listed gap to a
   top-three bottleneck.**  This is my main reranking claim, argued in §4.
   Without it, the entire GGV5/prime-ray machinery emits only `B_GGV`-value
   statements, and the partial-`y` frontier — the object that the
   counterexample side actually consumes through the floor theorem — is
   unreachable from that machinery.  It sits *between* the two live halves
   of the portfolio and is therefore higher-fanout than `G2-PSC`.
4. **Gate T: the literal total-source base change** for the five remaining
   Rees charts and the terminal receiver.  Demoted from "six missing maps
   plus a scheme-theoretic equality plus overlaps" to "five membership
   certificates plus one receiver" by Lemma 3.1.
5. **`G2-PSC` — demoted out of the active list.**  Scope-hostile reading of
   `REDUCTION.md` §7.1: a *pure Sigray* architecture bypasses `G2-PSC`
   entirely, and no live lane (landing/Rees, D1, order two, TD6, affine
   Faber) consumes a GGV packet as Sigray input.  `G2-PSC` is therefore an
   obligation of an architecture the campaign is not currently executing.
   It should remain documented and receive zero allocation until a lane
   actually proposes to import GGV corner data downstream.  `G2-BD` stays
   dormant for the same reason: it begins only after a residue-A datum is
   reached, and no live lane reaches one.
6. TD6 whole-closure (source/total-`F` certificate, omitted moduli, q15 as a
   genuine source modulus).  High local momentum, low global fanout.
7. Order-two fan exhaustiveness (mixed `H>15`, factor-degenerate receivers,
   earlier centres).

### 2.2 Disproof side

1. **Effectivity of the finite death depth for a bounded degree box.**
   CHARGED: the compactness composition (Heitmann `gcd>=16` + fixed-total-D12
   closure) already gives that any complete nested fixed-box AS collision
   scheme surviving at all `p`-adic depths yields a forbidden
   characteristic-zero counterexample, hence dies at *some finite,
   non-effective* depth.  The whole disproof lane's cost is that
   non-effectivity: without a depth bound, every negative result is a
   bounded observation.  This is now #1 on the disproof side, above the
   support-growth criterion, because it is the only item that would convert
   the lane from open-ended digit chasing into decidable boxes.
2. **The polynomial-limit criterion** (uniform support/degree).  The
   all-Witt control is the counterexample to naive optimism: its `Q_n` has
   exactly `n` monomials and `x`-degree `1+(n-1)(p-1)` while
   `deg_y Q_n = 1`, so any monovariant built only from partial-`y` degree is
   uninformative on that tower.  (I checked this before proposing a
   partial-`y` monovariant and discarded the proposal; recorded here so the
   next lane does not repeat it.)
3. **The `(8,12)`/`(9,12)` unbounded-total partial-`y` frontier**, which is
   the *only* live bounded-partial-`y` target and is simultaneously the
   floor-raising engine for AS109.  This is the shared item and the reason
   for §5.

---

## 3. New mechanism: the rho-unit certificate calculus

This is my primary new contribution.  It is elementary; its value is that it
removes three named obligations from the campaign root's critical path and
gives one machine-checkable type for the certificates every live lane is
already producing.

### 3.1 The lemma

**Lemma 3.1 (rho-unit chart certificate).  [EXACT]**
Let `A` be a commutative ring, `rho in A`, `I=(f_0,...,f_n) subset A`, and
let `X = Proj(Rees_A(I)) -> Spec A` be the blowup.  Fix ratio variables
`y_j`, and for each `i` put `P_i = (f_i*y_j - f_j : j != i) subset A[y]`, so
that the `i`-th standard chart is `Spec C_i` with
`C_i = A[y]/(P_i : f_i^infinity)`.  Suppose that for every `i` there exist
`N_i >= 0`, `H_{ij} in A[y]`, and `W_i in A[y]` with

```text
f_i^{N_i} * (1 + rho * W_i)  =  sum_j H_{ij} * (f_i*y_j - f_j)   in A[y].   (*)
```

Then the fibre of `X` over `V(rho)` is empty.  Consequently no morphism
`Spec R -> Spec A` with `R` a DVR, `I*R != 0`, and `ord_R(rho) > 0` exists.

*Proof.*  (*) says `f_i^{N_i}(1+rho W_i) in P_i`, hence
`1 + rho W_i in (P_i : f_i^infinity)`, hence
`1 in (P_i : f_i^infinity) + (rho)`, hence `C_i/rho C_i = 0`.  The
`Spec C_i` cover `X`, so `X ×_{Spec A} Spec(A/rho) = emptyset`.  For the
consequence: for a DVR `R` with `I*R != 0`, `I*R` is a nonzero ideal of a
DVR, hence invertible, so the universal property of the blowup lifts the
arc uniquely to `X`; its closed point would then lie in the empty fibre. ∎

### 3.2 What this discharges, and what it does not

**(a) The base-change/torsion obligation is not needed.  [EXACT]**
The frozen Gate-T obligation table §2 requires, per chart, *scheme-theoretic
equality* of `K_i^tot + (rho)` and `K_i^0` (the chart ideal recomputed after
literal `rho=0` specialization), and explicitly rejects equality of radicals.
That is a strictly stronger requirement than Gate T needs.  In general one
always has the containment

```text
(K_i^tot + (rho))/(rho)  subset  K_i^0     in (A/rho)[y],
```

because every generator of `K_i^tot` maps into `K_i^0`; the quotient is the
Valabrega–Valla / `rho`-torsion obstruction, which can be nonzero exactly
when `I^n cap (rho) != rho I^n` for some `n`.  Lemma 3.1 uses only
`1 in K_i^tot + (rho)`.  Therefore:

- a **specialized** endpoint (`K_i^0 = (1)`) is a *necessary screen only*;
  it does not imply the Gate-T statement.  This is exactly why the
  obligation table's "Gate-T map" column reads MISSING for all six rows,
  and it is the correct reading.
- the **total** certificate (*) implies the specialized one and needs no
  comparison at all.  The already promoted `T-rs` lemma is literally of this
  shape: `35*rs^2*k*U = 32768 P126 + 4096 P2 + 8192 qcs P3 + 12288 rho^2 qcs P1`
  with `U = 1 + 32 rho^2 qcs^2 (8 rho^2 qcs^2 + 3) ≡ 1 mod rho`.

So `T-rs` already *bypassed* obligation (2.5); the obligation table should
be repaired to require (*) uniformly rather than the equality.  This removes
one open item from the freeze's landing gap list.

**(b) Nilpotents cannot obstruct.  [EXACT]**  `1 in J` is insensitive to
nilpotent or embedded structure; `C_i/rho = 0` kills every scheme structure
at once.  Any "nilpotent" worry attached to the base-change comparison is
therefore moot for the emptiness form of Gate T.  I make **no** claim about
the separate deck-equivariant square bridge, which is a different
obligation (a comparison map, not an emptiness statement) and stays open.

**(c) Overlaps/gluing are not needed for emptiness.  [EXACT]**  Two
independent reasons.  (i) The `n+1` standard charts cover `Proj` by
construction, so chartwise emptiness is global emptiness; no transition data
enter.  (ii) If the cheaper *ordered* stratification
`D_+(f_0), V(f_0) cap D_+(f_1), ...` is used instead, those strata cover
`X` **set-theoretically** (a point has a least index with `f_i != 0`), and
emptiness of a scheme is a property of its underlying space, so
set-theoretic covering suffices.  The obligation table §6's demand that
"set-theoretic partition language is not enough" is over-strict *for the
emptiness goal*; what genuinely remains is a **provenance** obligation —
each stratum ideal must be the honest image of the total chart ideal, which
is a one-line surjectivity check on generators, not a scheme comparison.

**(d) What is *not* discharged.**  Localization debt is unchanged and must
be tracked explicitly: `T-rs` is certified on `D(k)`, so `V(k)` is a new
closed stratum needing its own certificate; similarly `k10 = 0`, `p = 0`,
`E*M = 0`, `D(p*k0*J)` complements.  The certificate calculus *converts*
localization into a visible list of residual closed strata; it does not
remove them.  Likewise the closed receiver `V(J1)` / `V(J1,J2)` still needs
its own emptiness argument; Lemma 3.1 covers only arcs with `I*R != 0`.

**(e) Two free stability properties.  [EXACT]**
(i) *Finite-prefix / further-relations stability*: (*) is an identity in
`A[y]`, so it survives every ring map `A -> A'`; in particular adjoining
later source-grade equations cannot break it.  This is the obligation
table's §3 acceleration, obtained for free rather than argued per chart.
(ii) *Parametric reuse*: prove (*) once over the universal parameter ring
and specialize.  This is exactly the freeze's "parametric symbolic support
rather than serial instances".

### 3.3 Certificate type

Uniform deliverable for landing, D1, TD6, and affine-Faber lanes:

```text
rho-unit certificate := ( source_presentation_hash,
                          multiplicative_set S,       # registered units
                          degeneration parameter rho, # may be 1
                          N, U, {H_j},
                          field/characteristic list )
valid iff   s^N * U == sum_j H_j * Phi_j   identically,
            U ≡ 1 (mod rho),   s in S,
            every denominator occurring lies in S.
```

`rho = 1` degenerates it to the ordinary unit certificates the D1 and TD6
lanes already emit (`-J/4`, `(3/8)(c0 ± lambda c1)^2`,
`(3500000000/9)*(U/V)`, `-E*lambda^3*M^3/16`), so one type covers the whole
portfolio.

---

## 4. New connection I: prime-ray/GGV5 is a `B_GGV`-value lane, not a frontier lane

This connects rows 1, 5, 19, 21 and the max-12 clients, and it is a ranking
claim, so I give it in full.

### 4.1 The charged reduction, restated

**CHARGED.**  For a characteristic-zero Keller pair `F=(P,Q)` write
`deg_y P = d a`, `deg_y Q = d b` with `gcd(a,b)=1`; the top Jacobian row
gives `[y^{da}]P = alpha h^a` and `[y^{db}]Q = beta h^b` for a univariate
`h` with `H = deg h`.  Put `e = gcd(H,d)` (the repository's "partial gcd").
The reviewed source-shear theorem says `y -> y + x^L` produces, for large
`L`, a source-equivalent Keller pair of exact total degrees
`a(H+dL), b(H+dL)`, whose total-degree gcd is `H+dL`.  Since
`gcd(H/e, d/e) = 1`, Dirichlet makes `H+dL = e*p` for infinitely many
primes `p`.  Then:

```text
e = 1 -> gcd is prime -> Nagata/Appelgate-Onishi -> automorphism;
e = 2 -> gcd is 2p    -> GGV 2p theorem          -> automorphism;
e >= 3 -> open.
```

The residual primitive partial-`y` pairs at maximum twelve are exactly
`(8,12)` (`d=4`, residual `e=4`) and `(9,12)` (`d=3`, residual `e=3`);
that is why total scale `3p` is the `(6,9)`/`(9,12)` residual scale.

### 4.2 The scope claim  [EXACT, given the charged inputs]

The classical inputs consumed above (`prime gcd`, `2p`) are **arbitrary-pair**
theorems: they exclude *any* Keller pair of that gcd.  The sheared pair is by
construction **nonminimal** (it lies in the source orbit of the seed).
GGV5 Theorem 2.20 and Algorithm 8, as recorded in `ladder/REDUCTION.md`
§2.2 and reaffirmed in the prime-ray note §7, are consumed **only** for a
globally minimal standard pair.  Therefore:

> Even a complete proof of `3P-E31` for **every** edge and every final
> corner at scale `3p` — not merely the one `(3,-1)` edge — would establish
> `B_GGV notin 3*Primes`.  It would **not** exclude a `(9,12)`
> counterexample, because such a counterexample only forces
> `B_GGV <= 3p`, and `B_GGV` may be any admissible value `>= 16`.

Symmetrically for `4p` and `(8,12)`.  The prime-ray promotion note already
states it does not close `(6,9)`; the point here is the stronger and more
consequential one: this lane's *deliverable type* cannot close any
partial-`y` frontier without the arbitrary-standard-pair bridge, so its
priority must be judged as a `B_GGV`-value lane inside a programme that
intends to exclude *all* values of `B_GGV` — i.e. it inherits the cofinal
wall (bottleneck 2.1.1) rather than bypassing it.

### 4.3 There is no `min(e_x,e_y) <= 2` shortcut  [EXACT — hand check]

The tempting escape is to hope that some coordinate direction always gives a
classical `e`.  It does not.  Take `H_1(x,y) = (y, x+y^3)`, Jacobian `-1`,
and iterate:

```text
F_2 = H_1 o H_1 = ( x + y^3 ,  y + (x+y^3)^3 )
F_3 = H_1 o F_2 = ( y + (x+y^3)^3 ,  (x+y^3) + (y+(x+y^3)^3)^3 )
```

For `F_3`: `deg_y = (9,27)`, so `d_y = 9`, `a=1`, `b=3`, and
`[y^9]P_3 = 1`, so `h` is constant and `H_y = 0`, giving `e_y = gcd(0,9)=9`.
`deg_x = (3,9)`, so `d_x = 3`, `[x^3]P_3 = 1`, `H_x = 0`, giving
`e_x = gcd(0,3) = 3`.  Hence `min(e_x,e_y) = 3` for a genuine Keller pair.
So the uniform statement "every Keller pair has `min(e_x,e_y) <= 2`" is
**false**, and no elementary two-direction shear argument can close the
frontier.  (Recording this negative control is the point: it is a cheap
idea that will recur.)

### 4.4 Consequence for allocation

The prime-ray lane should be relabelled and gated: before further
`3P-E31` regrading work, spend one bounded lane on the *bridge*, because the
bridge is what determines whether `3P-E31` is worth its cost (Card C).

---

## 5. New connection II: AS109 x max-12 is admissible at `p=109` even though it was refused at `p=3`

**CHARGED (the refusal).**  The 14:53Z overlay and its audit entry record a
theorem-interface composition check that found **no** direct p-adic
counterexample chart in the Q8 or TD6 normalizations, with the explicit
reason: "Q8 already uses nonunit `1/3,1/9` Kummer/depression normalizations
in residue characteristic three, while TD6 has `3H^3=1` and normalized roots
of valuation `-1/6`."  It was classified a scope conflict, not a negative
theorem.

**EXACT (why the reason is characteristic-specific).**  The obstruction is
that the normalizing denominators are non-units at the residue
characteristic.  The counterexample-side seed with the *promoted* Hensel
noninjectivity theorem is AS109, at residue characteristic `109`.  Every
denominator appearing in the charged max-12 / order-two / D1 / landing
algebra that I have read is supported on primes strictly below 109 and
different from it:

```text
1/16, 3/8, 3/32, 21/320, 41/640, 21/1024, 7/256, 12/5, 1/50, 1/4,
3500000000/9, 32768, 4096, 8192, 12288, 35, 96
```

— i.e. primes `2,3,5,7,41` only.  All are units in `Z_109`.  The exact
reason recorded for refusing the `p=3` pairing therefore **does not apply**
at `p=109`, and the interface deserves a fresh admissibility check rather
than inheriting the earlier `SCOPE-CONFLICT`.

**CONDITIONAL (the joint system).**  Compose three charged results:

1. every characteristic-zero Keller pair with `max deg_y <= 11` is an
   automorphism (promoted);
2. any exact integral polynomial lift of `(x - x^109, y)` is noninjective
   over `Q_109` (reviewed), whence `max(deg_y A, deg_y B) >= 12` for
   `P = x - x^109 + 109A`, `Q = y + 109B` (promoted floor-12);
3. the residual primitive partial-`y` pairs at maximum twelve are exactly
   `(8,12)` and `(9,12)`, with residual `4|H` resp. `3|H` (§4.1).

Then: **if an exact AS109 polynomial lift exists with maximum partial-`y`
degree exactly twelve, then after the charged target reduction/swap its
partial-`y` pair is `(8,12)` with `4|H`, or `(9,12)` with `3|H`.**  Those
are precisely the two families the order-two/order-one machinery is already
built for — now with three extra, very rigid constraints that the pure
proof lane does not have: `109`-integrality of all coefficients, a
prescribed reduction modulo `109` (`P ≡ x - x^109`, `Q ≡ y`), and a marked
collision.  The `109`-integrality alone forces `deg_x P >= 109`, which is
exactly the unbounded-coefficient-`x` regime the frontier gate insists on;
so the joint system is *inside* the live frontier, not a method control.

This is a genuinely smaller object than either lane alone, and it is
falsifiable in both directions: emptiness raises the AS109 floor to
thirteen for free (without proving a max-12 theorem); nonemptiness is the
sharpest counterexample lead the campaign has ever had.

---

## 6. Strongest proof attack and strongest falsification attack

### 6.1 Strongest proof attack — finish Gate T by five rho-unit certificates

Target: close the post-`M=0`, unit-`k10` collision family in the **total**
(moving-`p`) family, i.e. the campaign root.

Why this is the strongest available attack, ranked against TD6, D1, and the
affine fan: it is the only lane in which *every remaining obligation has a
known finite shape*.  After Lemma 3.1 the residual list is exactly

```text
five certificates (*) on  D_+(cs), D_+(c0), D_+(c1)  [J1 charts]
                     and  D_+(a0), D_+(a1)           [J2 charts on A/J1],
one emptiness argument for the terminal receiver V(J1,J2),
the residual closed strata V(k), V(k10), and the seven A source shards
    (c,r) = (2,>=3),(2,2),(3,>=3),(3,2) and r=1 with c=2, c=3, c>=4.
```

with certified finite decisive prefixes (grade 10 for the two `C` opens,
12 for the cusp, 14 for the odd sheet, <=15 per `A` shard, grade 38 only at
the terminal receiver).  No flatness, no torsion comparison, no scheme
overlap, no nilpotent analysis.  Each certificate is verified by expansion.

The attack's honest ceiling: this closes one collision family inside order
two.  It is **not** a landing theorem, does not touch the six-chart cover of
other load rays, and leaves the deck-equivariant square bridge and the
cofinal ceiling untouched.

### 6.2 Strongest counterexample/falsification attack — effective death depth

Target: convert the disproof side from open-ended digit chasing into
decidable boxes.

CHARGED: any complete nested fixed-degree-box AS collision scheme surviving
at all `p`-adic depths would produce a characteristic-zero counterexample
forbidden by Heitmann/GGV in that box, hence must die at some finite depth —
but the argument is a compactness argument and the depth is **not
effective**.  The attack is to replace the compactness step by a
**Greenberg / quantitative Artin approximation** constant computed on the
explicit finite-type `Z_p`-scheme of the box: an explicit `N(box)` such that
a solution modulo `p^{N(box)}` lifts to an honest `Z_p`-point.  Then a
*single* bounded computation per box decides that box outright.

The honest scoping, which is why this is a falsification attack and not a
proof: the live frontier families are unbounded in coefficient-`x` degree,
so they are not finite-type boxes.  Effectivity therefore decides a ladder
of boxes `(deg_y <= 12, deg_x <= D_x)`, not the frontier.  Each rung is
still decisive: a survivor at large `D_x` is a real lead, and a death at
`N(box)` is an exclusion no current method delivers.

A partial-`y`-degree monovariant is **not** an alternative and should not be
tried: the charged all-Witt control has `deg_y = 1` at every level, so the
gauge-minimal partial-`y` degree is bounded by 1 along that tower and
carries no information.  (I derived and then discarded this; recorded to
prevent a repeat.)

---

## 7. Software acceleration / decisive experiment

**The rho-unit certificate verifier.**  A single small, fail-closed tool
consuming the type in §3.3 and emitting `VALID / INVALID / OUT-OF-SCOPE`:

1. rehash the named source presentation against the frozen manifest;
2. expand `s^N * U - sum_j H_j * Phi_j` over exact `Q` and over one fresh
   good prime, and require identical zero;
3. check `U ≡ 1 mod rho` (or `U` a unit in `S` when `rho = 1`);
4. check every denominator appearing anywhere lies in the registered `S`,
   and refuse if an unregistered factor (e.g. the `K = 2R38` incident) is
   inverted;
5. emit the exact scope string (open, characteristic, retained jets,
   localizers) as the certificate's only advertisable claim.

Why this and not more compute: the campaign's binding constraint is review
latency and review debt, not CPU.  Today a hostile review of a chart result
is a bespoke re-derivation (the `T-rs` review "independently expanded the
identities over Q, checked the `rs`-valuations, inspected saturation
encodings"), which is expensive and rate-limits promotion.  With the type,
the *mathematical* review reduces to an expansion check plus a scope audit,
and the reviewer's scarce judgement is spent where it belongs — on whether
the registered scope is the scope claimed.  It also mechanizes the
`FAIL_`-guard/producer-authored-banner hazard, because the verifier is a
different program from the producer and re-derives the identity.

Secondary benefit: because (*) is stable under `A -> A'` (§3.2(e)),
certificates become *reusable assets* across lanes rather than per-case
artifacts, which is exactly the "parametric rather than serial" software gap.

---

## 8. Idea cards

### Card A — Complete Gate T by direct total-family rho-unit certificates

- **Type:** `NEW` as a method (the frozen obligation table demands a
  strictly stronger and unnecessary base-change equality); `DUPLICATE` as a
  target (Gate T is already the root's own priority).
- **Dependencies:** Lemma 3.1 (EXACT, above); the frozen total-source
  emitter and its reviewed manifest; the finite-prefix surjectivity remark;
  the promoted `T-rs` certificate as the template; AWS for exact `Q` plus one
  good prime.  Does **not** depend on V18R1/V19/H19R1 outcomes.
- **Cheapest discriminator:** the `V(rs) cap D_+(cs)` stratum at grade 14 —
  the smallest chart with a *promoted specialized* endpoint (odd-sheet unit
  `E_(5,14) = -(7/256) k0 cs^5`, `f48401b5...`).  Search for
  `N, U ≡ 1 mod rho, {H_j}` making (*) hold in the total family at that
  prefix, by bounded linear algebra over the grade-14 coefficient module.
- **Interpretation of outcomes.**
  *Certificate found:* Gate T holds on that stratum in the total family;
  the specialized endpoint is retroactively re-typed as a screen, and the
  obligation-table row's "Gate-T map MISSING" is discharged without any base
  change.  Immediately try the same shape on `c0`, `c1` (grade 10).
  *No certificate at the decisive prefix:* two sub-cases must be separated
  before any conclusion.  (i) The prefix is genuinely insufficient — extend
  by one grade and retry; the finite-prefix lemma guarantees monotonicity,
  so this terminates or exposes (ii).  (ii) `1 notin K^tot + (rho)` — then
  the total chart has a nonempty `rho = 0` fibre while the specialized chart
  is empty, and the difference is exactly `rho`-torsion in the Rees algebra.
  That is a *positive* structural discovery: it localizes the landing
  obstruction to a Valabrega–Valla failure and names the first `n` with
  `I^n cap (rho) != rho I^n`.  Either way the round yields a theorem or a
  named obstruction; there is no null outcome.
- **Stop condition:** stop after two consecutive grade extensions with no
  certificate and no torsion witness; that is the campaign's
  two-non-informative-attempts rule and forces a redesign of the chart
  presentation (e.g. a different `J1` generating set).
- **Expected information gain:** high.  Discharges up to three named freeze
  gaps (scheme-theoretic overlaps, the base-change comparison, nilpotents in
  that comparison), converts five open maps into five bounded searches of a
  known shape, and produces the first reusable certificate assets.

### Card A' — `A(F)` as the named endpoint (row 7 raise, cheapest form)

- **Type:** `KNOWN-BUT-NOT-RUN`.  `ladder/SHEET6-CLASSICAL.md` §4 registers
  precisely this as "a fresh kill test not run here".
- **Dependencies:** Chau Thm 4.4 (already a charged refereed input to `T7`);
  Jelonek's one-place-rational-component structure; the td=6 template's
  pinned `mu(F)=6`, `e`-budget `<= 6` per asymptotic value, and the
  `Sum(e_p - 1) = 2g + 6 >= 6` excess.  No new compute.
- **Cheapest discriminator:** on the pinned td=6 template, use the recorded
  `e`-assignments to pin each `A(F)` component's degree from the `c_p(a)`
  correspondence, then run the Abhyankar–Moh semigroup chain on the
  components (each is one-place rational, so AM applies *correctly* here,
  unlike the documented row-6 category error on fibers).
- **Outcomes:** a semigroup violation kills the template outright — the one
  classical test it has never faced; a pass adds a fifth zero-slack
  consistency and, more usefully, produces the first *typed* global receiver
  (`REDUCTION.md` §5.1's missing endpoint definition) expressed in
  published-theorem language rather than campaign obligations.
- **Stop condition:** stop if component degrees cannot be pinned from
  R1/R5 within one bounded lane; the test is worthless on unpinned degrees.
- **Expected information gain:** medium-high and very cheap; it is the only
  item in this report that costs almost nothing and can kill a template.

### Card B — The `p=109` joint AS109 x max-12 system

- **Type:** `NEW` connection; `SCOPE-CONFLICT` explicitly re-examined (the
  recorded refusal was characteristic-specific — §5).
- **Dependencies:** the promoted max-11 partial-`y` theorem; the reviewed
  AS109 109-ball Hensel noninjectivity and the promoted floor-12
  composition; the charged `(8,12)`/`(9,12)` primitivity checksum; the
  order-two/order-one source machinery.  Requires the frontier gate to be
  re-run with `--partial-y-degrees 8 12` / `9 12` and `--total-unbounded`;
  it must return `NOT_CLOSED_BY_THIS_GATE`, not `REFUSE_CLASSICALLY_CLOSED`.
- **Cheapest discriminator:** *before* any solver, a pure admissibility
  audit: enumerate every denominator and normalization constant used by the
  frozen `(9,12)` order-three and `(8,12)` order-two compilers and verify
  each is a `109`-adic unit.  This is a grep-and-factor job on frozen
  artifacts, no algebra.  Only if it passes, impose `109`-integrality plus
  the prescribed mod-109 reduction on the smallest already-frozen `(9,12)`
  coefficient system and test consistency at the first two Faber rows.
- **Interpretation of outcomes.**
  *A non-unit denominator is found:* the interface is refused for the same
  reason as at `p=3`, the connection is closed honestly, and the specific
  offending normalization is recorded so a future repair has a target.
  *All units, and the first rows are inconsistent:* the AS109 floor rises to
  thirteen without proving any max-12 theorem — a strictly cheaper route to
  the same effect, and it retires the `(8,12)`/`(9,12)` families as AS109
  hosts.
  *All units, and the rows are consistent:* the campaign has, for the first
  time, a single object constrained simultaneously by the proof-side Faber
  rows and the counterexample-side integrality; it becomes the top lane on
  both sides and every subsequent row is a decisive test.
- **Stop condition:** stop at the admissibility audit if any load-bearing
  constant has `109` in its denominator; stop the second stage after two
  Faber rows with no rank change.
- **Expected information gain:** high, asymmetric, and cheap at the first
  stage.  It is the only proposal here that could move both walls at once.

### Card C — Decide the arbitrary-standard-pair bridge before more `3P-E31`

- **Type:** `NEW` as a gating decision; the bridge itself is a `KNOWN` gap.
- **Dependencies:** the reviewed first-corner facts `a+b=G` and
  `gcd(a,b)>2` already used in the broader arbitrary-standard-pair argument
  for the `2p` theorem (named in the prime-ray note §7); GGV1's
  standardization (refereed); the prime-ray corner data
  `A0 = Corner(3u,1,3v)`, `A_gamma = Corner(gamma+3,3,gamma)`.
- **Cheapest discriminator:** attempt to extend the *existing* `2p`
  first-corner argument from `G = 2p` to `G = 3p` — i.e. determine whether
  the first corner of an **arbitrary** standard pair of gcd `3p` is already
  forced, without invoking global minimality anywhere.  This is a hand/short
  symbolic job over `Q[p, gamma]` on two corners, not a chain enumeration.
- **Interpretation of outcomes.**
  *The first corner is forced without minimality:* the bridge exists at
  first-corner depth; `3P-E31` becomes a frontier lemma and the whole
  prime-ray lane's rank rises sharply (and row 1's `lower` should be
  reverted).
  *Minimality is provably used at the first corner:* the bridge is
  obstructed at the cheapest possible depth, `3P-E31` is confirmed as a
  `B_GGV`-value lemma, and the lane should be capped and re-priced against
  the cofinal wall (§4.2).
  *Undecided after the bounded attempt:* treat as obstructed for allocation
  purposes; the burden of proof is on the lane that wants frontier credit.
- **Stop condition:** one bounded lane, hard stop; no chain enumeration, no
  prime census, no regrading of `p=7,11` systems until this returns.
- **Expected information gain:** high per unit cost, because it is a
  *decision* about an existing allocation rather than new mathematics, and
  because both outcomes change a launch/stop decision immediately.

---

## 9. `continue / redesign / stop` for current major lanes

| Lane | Verdict | Reason (scope-hostile) |
|---|---|---|
| Landing / actual-total Rees (root, Gate T) | **continue, redesign the obligation table** | Correct root and only lane with all obligations of known finite shape.  Redesign: replace obligation (2.5) and the scheme-theoretic overlap demand by uniform rho-unit certificates (§3); keep a visible residual-closed-strata ledger (`V(k)`, `V(k10)`, receiver). |
| V18R1 / V19 (T-cs positive + explicit lift) | **continue** | Frozen, running, nonblocking.  Note the honest asymmetry: V18R1's main result is provisional until the drop-grade-14 negative control lands, and V19 is a lift-extraction, not an independent chart theorem.  Do not let a second host's replay be counted as independent recomputation. |
| TD6 (H19R1, source/total-`F` certificate) | **continue, with a hard gate** | The P13 coordinate-12 unit is a real theorem on its slice, but the lane has now produced a long series of narrow residue-block results (q14, q13, high-q, total-`q2`, P13) that do not compose into a source/landing statement.  Gate: H19R1 must emit the 38 original-FIRST multipliers *and* a denominator-cleared total-`F` identity.  If it does not, redesign rather than start another q-jet successor. |
| D1 (strict `a=8,9` cells, composition) | **continue** | Near closure; three residual cells with a mechanically complete grade-38 producer and known first pole-four grades (41,42,43).  Cheap to finish, and the row-7 order-three functional is reviewed. |
| Affine-Faber order-two fan (H16 and beyond) | **redesign** | The first control beyond the homogeneous range already shows graph deviations absorbing the grade-44 quadratic obstruction at `(H,q)=(16,6)`.  That is the signature of a fan without a well-founded ranking.  Hard-stop serial `H`-increments until either an explicit well-founded ranking or an explicit transition cycle is produced — the 17:40Z synthesis asked for this and it has not been delivered; a third serial successor needs written justification under the campaign's own two-attempt rule. |
| Prime-ray / GGV5 (`3P-E31`) | **redesign** | Re-label as a `B_GGV`-value lane (§4).  Gate all further `3P-E31` work behind Card C.  Do not spend on regrading `p=7,11` terminal systems before the bridge decision. |
| Counterexample side (AS109 / Witt) | **continue, retargeted** | Retarget from serial fixed-`deg_y` no-gos (superseded by floor-12) to Card B's joint `p=109` system, with Greenberg effectivity (§6.2) as the parallel instrument.  Do not build a partial-`y` monovariant (§6.2). |
| `G2-PSC` | **stop (zero allocation, keep documented)** | No live lane consumes a GGV packet as Sigray input, and a pure Sigray architecture bypasses it outright.  Re-activate only when a lane actually proposes the hybrid import. |
| `G2-BD` | **stop (dormant)** | Begins only after a residue-A datum is reached; no live lane reaches one. |
| Software / certificates | **continue, with §7 as the next deliverable** | Review latency, not CPU, is the binding constraint. |
| Formalization (`jc2-lean`) | **continue asynchronously** | Separately owned and read-only this round; must never gate discovery. |

---

## 10. Explicit nonclaims

- No proof or disproof of JC2, of any partial-`y` frontier family, of Gate T,
  of whole TD6, of order two, or of `3P-E31`.
- Lemma 3.1 is elementary blowup algebra; it proves no chart empty.  It
  changes which obligations are on the Gate-T critical path, nothing else.
- §4.2 is a scope claim about deliverable *types*.  It asserts no defect in
  the promoted prime-ray arithmetic, which I take as CONFIRMED.
- §5 shows only that the *recorded reason* for the earlier p-adic x max-12
  refusal is characteristic-specific.  It does not show the interface is
  admissible; that is Card B's first stage.
- The `F_3` triple-Hénon computation in §4.3 refutes a hypothetical uniform
  shortcut; it says nothing about counterexamples.
- I ran no heavy computation, made no AWS change, browsed no web source,
  read no other blind submission, and touched no file in `jc2-lean`.
- This report is my only repository edit.
