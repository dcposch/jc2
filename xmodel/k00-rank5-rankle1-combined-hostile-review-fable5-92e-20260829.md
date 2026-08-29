# K00 rank-five / grade-three rank-at-most-one combined hostile review

Reviewer: Fable 5, equal-standing independent adversarial reviewer
Date: 2026-08-29
Frozen basis: `92ebe92ad5986a47f01af9ed901260595dfed869` (verified by
`git rev-parse HEAD` at start of work)
Output: this file only.  No canonical, case, ladder, or operations file was
edited.  No web, network, commit, push, AWS, or `jc2-lean` access.  All exact
algebra ran in fresh scratch `/tmp/k00_r5le1_rev_fable5/` under a per-process
CPU cap of 60 s (`ulimit -t`, 55 s for the primdec attempts) with peak RSS
measured by `/usr/bin/time -l` on every heavy process; the maximum observed
was 757 MB < 1 GiB, zero swaps, no warnings or signals.  No full-P6 job was
launched.  Engines: Singular 4.4.1 (44105, arm64-Darwin, exact `Q` only,
`char=0` asserted in every ring) and pure Python 3.9.6 over `Fraction`.

## 0. Binary dispositions

```text
REVIEW A (Sol MAX5CLASS rank-five):        PASS_WITH_REPAIR
REVIEW B (Grok grade-three rank<=1):       PASS_WITH_REPAIR
```

Every load-bearing mathematical claim in both reports was independently
reconstructed from the frozen source artifacts and replayed true.  The
repairs are report-text defects listed in sections 3.7 and 4.8; none changes
a theorem statement.  Both dispositions fail closed on the repairs being
adopted.

## 1. Charged reports and seals

1. `xmodel/k00-rank5-maxclass-next-sol56-20260829.md`, full-file SHA-256
   `0a3af03ed8d07db852f833d0dc9ebe3ec151934308f4a139cf7ac72124f9b3cb`
   (matches the charge).  Body = bytes before its seal heading: 13,199 bytes,
   SHA-256 `5c0397492ad5a739944343686407a909a17d0e7cc37555cb18221ba40548e200`
   — matches its own seal.
2. `xmodel/k00-grade3-rankle1-primary-grok46-92e-20260829.md`, actual bytes
   (18,017) hash to
   `e0947368509714aa96376789914a4dbfd7141b1f77832016bf4dbe7c3caa45e4`
   (recorded here as charged).  Body = bytes before its seal heading: 17,523 bytes,
   SHA-256 `33c9ff079d97933b3c2f59984e2593f4ee70111de8174b0fda063eeb3f08f2dc`
   — matches.  The stated zero-field convention verifies exactly: replacing
   the 64-hex full-file field by zeros and hashing gives
   the recomputed digest, which equals the report's stated
   `3e2b13b2f064e28200972a57da87d6daca300144fd2dc36b0f53c6bbc1455cfc`.

Neither report was used as a premise for the other's audit.

## 2. Frozen source reconstruction (shared)

From `ATLAS_EXACT_POLYNOMIALS.json` (`d7ec6d18...`, hash verified), every
object below was parsed twice — once from `exact_terms` into exact
`Fraction` sparse polynomials, once through an independent parser applied to
the `singular` strings — and the two parses agreed on every entry used
(matrix `A`, `Q1_to_Q6`, `F10`, `b`, all 49 literal `(Lambda_grade,row)`
rows).  The per-polynomial `sha256` fields follow the v26 compiler
convention `sha256(compact-sorted-JSON(payload)+"\n")` (recovered from the
frozen `compile_fitting_atlas_v26.py`, `p_digest`); all digests used were
recomputed from my own parse and matched.  All 49 v27
`singular_text_sha256` labels match `sha256(text.strip()+"\n")` as Grok
states.

Verified shared facts:

- `A` is 7x7 in exactly `Q[d0_1,d1_1,d2_1,d3_1,d4_1,d5_1]`; columns 1-6
  homogeneous linear, column 7 homogeneous quadratic; the entry-term census
  equals Sol's table exactly, including row 6 = `(0,0,0,0,0,0,12)`.
- `q1..q6` are the literal grade-two rows `(1,2,3,4,5,7)` (grade-two row 6
  is exactly zero), matching `NOTATION_CLARIFICATION_R1_GRADE2_ROWS.md`;
  all six polynomial hashes and term counts match Sol's table; homogeneous
  degree 2.  `F10`: 30 terms, homogeneous degree 4.  All seven generators
  of `B=(q1..q6,F10)` occur verbatim among the 35 literal `P6` generators,
  so `B subset P6` and the full-P6 inheritance argument is licensed.
- Kernel identities `l0*A=0`, `A*v1=0`, `A*v2=0` recomputed
  coefficientwise with the stated vectors; each registered `+1` mutation
  breaks its identity.  `l0*b` has exactly 690 terms and equals,
  monomial-for-monomial, the frozen serialization
  `.../aws_r6a_aux_constant_kernel/output/L0_B_PRIMARY.txt`
  (`88516f87...`, hash verified), confirming Sol's byte-bound claim.

## 3. Review A: maximal-minor class theorem (Sol)

### 3.1 Independent 441-minor census

All 441 literal 5x5 minors were recomputed by an integer-scaled exact
dynamic-programming determinant expansion (pure Python, 4.16 s, 757 MB),
then compared entrywise against the frozen ledger
`A_COMPOUND_MINORS.json` (`17d13f45...`): **0 mismatches of 441**.
Census, independently derived:

```text
total 441; zero 351; nonzero 90
distinct exact polynomials among nonzero: 54
distinct up to sign: 41
scalar-proportionality classes: exactly 2
W class = RW x C, 4*9 = 36 literal minors, 23 distinct polynomials
M class = RM x C, 6*9 = 54 literal minors, 31 distinct polynomials
RW = {01234,01236,01346,12346}
RM = {01235,01345,01356,12345,12356,13456}
C  = {01236,01256,01346,01456,02356,03456,12346,12456,23456}
```

`RW`, `RM`, `C` equal Sol's sets exactly and both classes are exact
Cartesian products.  Every nonzero minor was verified to equal an exact
rational scalar multiple of its class representative (0 failures in either
class).  Representatives, with frozen polynomial digests matched:

```text
W = det A[01234|01236], 226 terms,
    a78701cd74655f3c1514a954b081a1a602ff657bc39b2477de6fb99a2b0f722e
M = det A[01235|01236], 236 terms,
    de45e3764cd19dc78397c4302b47439140cd2166665a2b5dc982075f82589f5e
```

`W` and `M` have distinct normalized keys; a sign mutation of `A[1,1]`
changes `W` and expels it from both classes (registered mutation fires).
All 49 6x6 determinants were recomputed independently: identically zero
(`I6(A)=0`), and the two constant right kernel vectors explain the generic
rank-5 ceiling as claimed.

### 3.2 The two memberships

Independently, in Singular 4.4.1 exact `Q`, `dp`:

```text
NF(M, std(B))              = 0     (M in B)
NF(M, std((q1,q2,q4,q6)))  = 0     (M in (q1,q2,q4,q6); no q3,q5,F10)
NF(W, std(B))              = 0
NF(W, std((q1,q3,q4)))     = 0     (fresh independent replay of the
                                    reviewed W fact, not a consumption)
```

The `W` fact's cited provenance files exist with exactly the cited hashes
(`f9d2afcb...` = the V24R6R1 hostile review, `d9e65315...` = the Opus
cross-audit); this review nevertheless re-proved the membership from
scratch, including a lift verified coefficientwise in Python
(`W_LIFT_RESIDUAL_ZERO=True`).

Sol's `M` certificate replays **byte-exactly**: `lift(B,ideal(M),U,"std")`
on this engine yields seven coefficients whose `string(poly)` serializations
hash to Sol's seven values exactly
(`9a708aed...`, `8b05adee...`, `5feceb66...`(=sha256("0")), `fc30f54d...`,
`5feceb66...`, `4303323c...`, `5feceb66...`), with term counts
`(56,49,0,38,0,56,0)`, and the concatenation-with-newlines hashes to Sol's
`a9a983ac...`.  A pure-Python verifier multiplied the parsed coefficients
against the frozen generators: residual exactly zero; the registered
mutation `C1 -> C1+1` produces residual exactly `q1`.  My independent
`"slimgb"` lift gives a different, also-valid certificate
(`(37,22,0,38,0,55,0)`, residual zero), with the same zero support on
`q3,q5,F10`.  The 76-byte marker transcript was reconstructed byte-exactly
from its semantics: `sha256 = 1716caed...` matches Sol.

### 3.3 Consequence

Every literal 5x5 minor is zero or an exact rational multiple of `W` or
`M`; both lie in `B2=(q1,...,q6)`.  Hence `I5(A) subset B2 subset B` as
ideals (scheme-theoretic, no radical), `B+I5(A)=B`, `V(B)` has
`rank(A) <= 4` everywhere, every rank-five localizer `B+(z*m-1)` is unit
(verified for the representative: `NF(1)=0`, `dim=-1`, 1 generator; the
rest follow from `m in B`), and the rank-exact-five chart count on `V(B)`
and over `V(P6) supseteq V(B)` is **zero**.  No rank-five AWS job should
run; Sol's hold is correct.

### 3.4 Composition with V27, upgraded

The cited review `xmodel/k00-v27-base4-base3-base2-hostile-review-fable5-
20260827.md` hashes to `738f4603...` as claimed and proved
`I4(A), I3(A) subset B+I5(A)`.  This review **replayed the composition
directly**: `NF` of all stored `I4(A)` (594) and `I3(A)` (813) generators
against `std(B)` is zero, while 291 of 441 `I2(A)` slots are nonzero mod
`B`.  So `I5,I4,I3 subset B` exactly, `rank(A) <= 2` on all of `V(B)`,
and the corollary no longer needs the V27 review as a premise (it now
confirms it).  The 291 count matches the reviewed V27 ncols-repair census.

### 3.5 Controls (Review A)

Ordinary vs optimized: `std(B)` and `slimgb(B)` mutually reduce to zero.
Localization pair: forced unit `(B,z*M-1)` unit vs named proper control
`(B,z*d0_1-1)` proper of dim 3; `B` itself proper of dim 3; `B+(1)` unit.
Entry mutation: sign flip of `A[1,1]` changes `W` and its class; kernel
vector mutations break their identities.  `ncols` vs `size`:
`minor(A,2)` has `ncols=441` but `size=351` on this engine (zero slots
retained for k=2), while `minor(A,k)` for k=3,4,5 stores only nonzero
minors (`813/594/90`) — positional loops must use `ncols`, and all of mine
did.  Exact `Q` only: `char=0` asserted in every ring.

### 3.6 Facts consumed vs replayed

Replayed from source: everything in 3.1-3.5.  Consumed at reviewed status
only: none required for the endpoint; the V27 containments and the
V24R6R1/Opus `W` provenance were re-proved here.

### 3.7 Review A repairs (fail-closed)

- **R-A1 (report text, required).** Sol's displayed command
  `lift(B,ideal(M),U,"slimgb")` does not produce the hashed certificate on
  this engine: the literal `"slimgb"` invocation yields the different lift
  `(37,22,0,38,0,55,0)`.  The recorded hashes come from the `"std"` lift
  path.  A replayer following the report text verbatim cannot reproduce the
  seven coefficient hashes.  Repair: correct the invocation string to
  `"std"` (the recipe pinned by this review).
- **R-A2 (replayability note).** The 6,985-byte labelled lift transcript
  (`ad2455e0...`) exists only in Sol's scratch; its byte format is not
  recoverable from the report, so its hash is unverifiable.  Mitigated:
  the transcript's entire mathematical content (the seven coefficients) is
  pinned by the per-coefficient hashes, which this review regenerated and
  verified independently.  Repair: archive certificate serializations, or
  state the generating script bytes, for future certificates.

Neither repair touches the theorem.  Disposition A:
**PASS_WITH_REPAIR** for
`PASS_K00_MAX5CLASS_ZERO_RANK5_CHARTS`.

## 4. Review B: grade-three rank-at-most-one theorem (Grok)

### 4.1 Reconstruction of `P3 = C u + c3`

The seven literal `(3,1..7)` rows were re-extracted; all seven
`sha256(text.strip()+"\n")` values match Grok's list and the v27 labels
file, and the atlas payload digests verify.  Independent facts, all
replayed exactly:

```text
P3_NCOLS=7  P3_ZERO_SLOTS=0
support(P3) = {d0_1..d5_1, d0_2..d5_2} exactly; k10_* absent (grade<=3)
every monomial has u-degree <= 1  (all second u-derivatives zero)
P3 == C*u + c3 exactly (affine reconstruction, 0 defects)
C == A[:,1..6] coefficientwise (0 of 42 mismatches)
C zero entries: exactly row 6 (6 slots); C homogeneous degree 1
c3: no zero slots; term counts (7,9,13,15,19,21,23); homogeneous degree 3
```

Ring-map attacks: an off-by-one `u`-map and a reversed `u`-map each
produce 36 mismatches against `A[:,1..6]` (caught); `A[1,1]+1` and a sign
flip each trip the comparison; `c3[1]+1` changes exactly **30** of 441
`I2(E3)` slots, matching Grok's control row.

### 4.2 Ideal tower, engine census

All of Grok's engine counts replay exactly on the same engine family
(Singular 4.4.1 arm64-Darwin):

```text
I3A ncols=813 nonzero=813        I2A ncols=441 nonzero=351
I2C ncols=315 nonzero=225        I2E ncols=441 nonzero=351
I3E ncols=813 nonzero=813
J2:  std 9 gens,  proper, dim 3
J1:  std/slimgb 10/10, proper, dim 2, mutual reduction
fresh J1 == V27 BASE2 (both containments; BASE2_R3_STANDARD_BASIS.txt
  a840c9b6..., hash verified)
I2C_OUTSIDE_J1=0    I3E_OUTSIDE_J1=0
I2E_OUTSIDE_J1=120  I2E_INSIDE_J1=321
R1:  std/slimgb 13/13, proper, dim 2, mutual; J1 strictly inside R1
J0:  std/slimgb 4/4,  proper, dim 2, mutual; basis EXACTLY
     2*d3_1-d5_1, d2_1-d4_1, 16*d1_1-d5_1, d0_1-2*d4_1
R0 = J0 (all seven c3 slots have NF 0 mod J0); std 4 gens, dim 2
R1 subset J0;  J0 not subset R1;  J1 strictly inside J0
```

The `813/1225` discrepancy is engine-real and correctly handled: this
4.4.1 build stores only the 813 nonzero 3x3 minors while the reviewed
V27 Linux 4.3.2 producer retains 1,225 labelled slots (documented in
`DESIGN_ERRATUM_R3_SIZE_NCOLS.md` and re-flagged in the chart-free
packet review); dropped zero slots cannot change the ideals, and all
positional loops here used `ncols`.

### 4.3 Radical certificate

For each of the four displayed linear generators `g`, the minimal power
with `NF(g^k, std(R1))=0` is **exactly 4** (k=1,2,3 all nonzero — a
strict upgrade on the report, which asserted only k=4 membership), and
`NF(g^k, std(J1)) != 0` through k=12.  With `R1 subset J0` (verified) and
`J0` a prime linear complete intersection (four forms with unit leading
entries in the four distinct variables `d3_1,d2_1,d1_1,d0_1`: rank 4,
codimension 4, dimension 2), this gives `sqrt(R1) = J0` exactly as
claimed, and `R1 != J0` as ideals (power-1 normal forms nonzero), so
replacing radical equality by ideal equality is correctly not done.

### 4.4 Rabinowitsch pairs and pins

```text
R1 + (z*(2*d3_1-d5_1)-1):  unit (NF(1)=0, dim -1)   [positive control]
J1 + (z*(2*d3_1-d5_1)-1):  proper, dim 2, std=slimgb [negative control]
J1 + (z*(d2_1-d4_1)-1):    proper, dim 2
J1-chart + (d4_1, d5_1-1): proper, dim 0, vdim 4
J1-chart + (d4_1-1, d5_1): proper, dim 0, vdim 4
  (J1-chart := J1 + (z*(2*d3_1-d5_1)-1))
```

So `2*d3_1-d5_1 in sqrt(R1) \ sqrt(J1)`, `V(J1)` is not contained in the
plane, and `V(J1)` contains nonempty finite `Q-bar` schemes with
`2*d3_1-d5_1 != 0`; since `A[1,1] = (3/2048)*(2*d3_1-d5_1)` exactly
(verified), such points have `rank(C)=1` on the rank-<=1 base.  Grok's
parenthetical discriminant remarks also verify on the chart-free pin
ideals `J1 + (pin)` (the chart then removes the plane branches): the
`(d4_1=1,d5_1=0)` eliminant is `d3_1^3*(3086024704*d3_1^4+13867072*d3_1^2+281961)` — a
quadratic in `d3_1^2` with negative discriminant
(`13867072^2 < 4*3086024704*281961`), no real nonplane point; the
`(d4_1=0,d5_1=1)` eliminant factors as
`(2*d3_1-1)*(1736*d3_1^2-3275*d3_1+1469)` with discriminant
`524889 = 9*58321`, positive nonsquare, and the rational root
`d3_1=1/2` lies on the plane (`2*d3_1-d5_1=0`), excluded from the chart.

### 4.5 The plane, as polynomial identities

Beyond Grok's evaluation sampling, this review proved at ideal level:
**all 49 entries of `A` — including the quadratic column 7 — have
`NF(.,std(J0))=0`** (`I1A_OUTSIDE_J0=0`), and all seven `c3` slots
likewise (`R0=J0`).  Hence on `V(J0)`: `A=0`, `C=0`, `c3=0`, and
`P3 = 0` identically in `u` — a polynomial identity, not a sampling
claim, with no residual column-7 rank piece.  The displayed
parametrization `(2s, t/8, s, t, s, 2t)` annihilates all four generators
(desk check: `2t-2t`, `s-s`, `16(t/8)-2t`, `2s-2s`) and has two free
parameters, so it is the full reduced 2-plane.

### 4.6 The theorem's logic, audited

For algebraically closed `K` and `x in V(J1)(K)`: solvability of
`P3(x,u)=0` forces `rank[C|c3](x) = rank C(x) <= 1` (using
`I2(C) subset J1`), hence `x in V(R1) = V(sqrt(R1)) = V(J0)` = the
plane; on the plane `C(x)=0` and `A(x)=0`, so no compatible point has
`rank C(x)=1` (or `rank A(x)=1`) — the rank-exactly-one compatible
locus is empty under either reading of the stratum.  Conversely
rank-zero compatibility is `C(x)=0, c3(x)=0`, i.e. `V(R0)=V(J0)`, on
which every `u` works identically.  The rank-zero direction is
`Q`-rational, so it needs no geometric-field qualification; the
rank-one emptiness and the nonemptiness of the incompatible rank-one
stratum are correctly typed "over an algebraic closure" (the exhibited
pins have no rational points; see 4.4).  The weak automatic condition
`I3(E3) subset J1` (verified, 0 slots outside) indeed decides nothing
about rank-one solvability — the compatibility content sits in the 120
`I2(E3)` slots, and the `rank(C)`-vs-`rank(E3)` distinction is
load-bearing exactly as the report says (`I2C` inside `J1`, `I2E` not).
No projection is treated as a lift anywhere in the report; free `u` on
the plane is an identity of the seven labelled rows only.

### 4.7 `k10_0` typing and the successor rule

Verified from source: `SOURCE_COLUMNS.json` (`2e8ceeb4...`) records
`k10_0` as `kind=load, first_Lambda_grade=2, boundary_status=FREE`;
the 49 literal contracted rows first contain `k10_0` at Lambda grade
**4** (`k10_1` at 5, `k10_2` at 6); grade <= 3 rows are `k10`-free and
grade 3 uses exactly `{d*_1, d*_2}`.  The six-variable ring does not
contain `k10_0`, so neither imposing `z*k10_0-1` nor saturating by it is
possible or licensed at grade 3; it first becomes a polynomial-ring
condition at grade 4 on the plane.  Grok's three-way typing is exact.

### 4.8 Review B repairs and notes (fail-closed)

- **R-B1 (report text, required).** §5's `I1C_NCOLS=20` described as
  "the engine storage after adjoining the 42 slots" is not the plain
  engine behavior: `ideal(C)` stores 42 slots (36 nonzero) on this same
  engine build.  20 is the count after proportionality deduplication
  (e.g. `simplify(ideal(C),2+8)`; equivalently the 36 nonzero entries
  fall into exactly 20 scalar classes, verified).  No downstream effect:
  `J0` is identical either way.  Repair: state the simplification step.
- **R-B2 (justification wording, required).** §6 attributes the identity
  `I1(A) subset J0` to "C is linear and J0 is radical" plus four-point
  evaluation.  That argument covers the linear columns, and for the
  homogeneous quadratic column 7 the three nontrivial sample points do
  suffice — but the report does not make that argument, and for the
  cubic `c3` four points (one trivial) are insufficient; `c3 subset J0`
  rests on `R0=J0`, which the report has.  This review closed the gap
  outright: `I1A_OUTSIDE_J0=0` and `C3_OUTSIDE_J0=0` by normal form.
  Repair: cite the NF facts, not the sampling.
- **Note (resolved blocker).** Grok's typed `OPEN` on `minAssGTZ(J1)`
  (their 58 s cap hit) resolves at desk on this machine in 0.12 s:
  `J1` has exactly **two** minimal primes, both of dimension 2 — the
  plane `J0` (component equality verified against the displayed forms)
  and a 7-generator rank-one component `Cmp1` (serialized in evidence,
  primality per the primdec certificate).  Honesty checks: `J1` is
  contained in both components, and every generator of
  `intersect(Cmp1,J0)` is in `sqrt(J1)` by per-generator Rabinowitsch
  units.  So `V(J1) = V(Cmp1) union plane`, and the incompatible
  rank-one locus is `V(Cmp1) \ plane`.
- **Note (unverifiable, non-load-bearing).** Grok's scratch artifacts
  (`rankle1.sing` `06cee70f...`, stdout `a0b937aa...`, `SJ1o/SR1o/SJ0o`
  hashes) are not archived and cannot be byte-checked; every underlying
  fact was rebuilt from frozen sources instead, and all replayed true.

Disposition B: **PASS_WITH_REPAIR** for
`PASS_K00_G3_RANKLE1_CHARTFREE` with
`RANK1_COMPATIBLE_GEOMETRIC_LOCUS = EMPTY` and
`RANK0_COMPATIBLE_LOCUS = SURVIVES (reduced 2-plane)`.

## 5. Composition table

Consumed reviewed inputs beyond the two charged reports: the V27
containment review (`738f4603...`, and independently re-replayed here) and,
for one optional row, the chart-free rank-two packet
`cases/k00_g3_r2_chartfree_v1_20260829/` at its reviewed
`PASS_WITH_REPAIR` status (`6bb957b4...`), consumed as reviewed, not
replayed here.

| # | statement | status |
|---|---|---|
| 1 | `I5(A) subset B2 subset B`; `B+I5(A)=B`; zero rank-exact-5 charts on `V(B)` and over `V(P6)`; no rank-5 AWS launch | replayed (A) |
| 2 | `I4(A), I3(A) subset B` exactly; `rank(A) <= 2` on all of `V(B)`; rank-exact-4 and rank-exact-3 loci on `V(B)` also empty | replayed (A + direct NF) |
| 3 | `V(J1) = V(B) cap {rank <= 1}`; grade-three compatible geometric locus of `V(J1)` = the reduced 2-plane `V(J0)`, on which `A=0`, `c3=0`, and every `u` works; rank-exactly-one compatible locus empty | replayed (B) |
| 4 | `sqrt(J1) = Cmp1 cap J0`, two minimal primes, both dim 2 | new here (4.8) |
| 5 | with the chart-free packet: rank-exactly-two grade-three-compatible points of `V(B)` are excluded (`I2(A) subset sqrt(B+I3(E3))`), hence the **maximum jointly licensed theorem**: *over an algebraic closure, the full grade-three compatible locus of the leading base `V(B)` is exactly the reduced 2-plane `V(J0)`, with `u` free on it* | composed (A+B+chartfree at reviewed status) |

Nonclaims (jointly and severally): no Keller lift or Keller-pair
statement; no order-two exclusion; no maximum-twelve statement; **no JC2
conclusion**; no statement at grades 4-6 or 7-19; no `k10_0`-open source
point; no formal or convergent arc, jet, or K00-closure statement; no
full-`P6` proper-ideal computation (only inherited unit certificates for
rank-5 localizers); no rank-two review beyond consuming the chart-free
packet at its own reviewed status; free `u` on the plane is an identity
of the seven grade-three rows, not a lift; nonemptiness of the
incompatible rank-one stratum is not a lift.  Neither report declares an
exit price and none is declared here (no FALLACY-v2 exit line owed).

## 6. Blockers and successors (deduplicated)

Deduplication baseline: the chart-free rank-two packet is reviewed
`PASS_WITH_REPAIR` and its coordinator integration records that no AWS
successor follows from the closed rank-two branch; nothing below repeats
its calculation or re-opens rank two at grade 3.

- **Smallest live successor (rank-zero branch, unchanged from Grok §12):**
  the grade-4 gate on the 2-plane `V(J0)`, in the ring that first
  contains the literal `(4,1..7)` rows — verified to adjoin exactly
  `{d*_3}` and `k10_0`.  Retain `k10_0 != 0` there and not earlier
  (grade-4 birth verified from source).  Not a full-P6 job, not a
  rank-five job.
- **Rank-one at grade 3: no successor** — compatible locus empty
  (Review B); do not launch selected `I2(E3)` charts.  The optional
  component list of the incompatible locus is now partially delivered:
  `Cmp1` (4.8).  Remaining typed `OPEN`: a rational point of
  `D(I1(C)) cap V(J1)` — both Grok pins verified to have none; other
  charts unexplored.
- **Rank five / full-P6 rank charts: dead** (Review A); Sol's
  conditional `Kleft = P6 + (l0*b, t*k10_0-1)` screen remains a valid
  registered kill test whose inputs all verify (`c7 = l0*b` replayed
  against `88516f87...`), gated behind the grade-4 review; it must not
  run ahead of it.
- Sol's `H3 = B + I3(E3)` successor naming is exactly the chart-free
  packet's `H` (using `I3(A) subset B`, replayed): already produced and
  reviewed; no competing packet is needed or created.

## 7. Evidence ledger

Scratch `/tmp/k00_r5le1_rev_fable5/`; engine `Singular for arm64-Darwin
version 4.4.1 (44105, 64 bit)`; Python 3.9.6.  Stdout evidence files and
SHA-256:

```text
624df3cd3748b76619effafa26bc2f513756404ed3fda9a4c578f991129c9d2a  custody_A.out
dfcb5d6765a6dccfad04f61ab4920149b2621ed0ebc673c6df5f4a31e0029043  census5.out
0009457574a9c8f7064bd8be668723edbb27dbc445d54984255c5b2b5eef2546  memb.out
67730fb3c40175314e86fb1107b46102d107bc035bb13b3e483d3384e5089bf1  lift_std.out
aca0617a2dc07c3b1483f8e6c5a15e4094d6d469465b0047f4381360747ee3cc  lift_slim.out
95e724942d05b4377c8311976c674ccc74b6edaeb49ac07b1cb475c4238042b8  mutual.out
b720ec65112e51e4c3b177b001333b5bf6835bf92efaf2e79a193b98a0367d56  revB_custody.out
d2024d48697039d51455f74c82fb4bfc0983c865429d39274e2f7d0d4149eeed  revB_ideals.out
95b4996fdffc6bde9fcba9e0319b82936a3253fc2fd3fb163a5b26e67b735d9f  revB_rabin.out
05e9784b9011bce6554e9989d823a66edf459ed6d249d02b35307aa7694c01ec  revB_minass.out
b80ffbbbbf2aab51eacb7e8a07a243e410e491c8e8fd4ab915afa62e939620da  revB_minass2.out
912a03e88c6739ad410c5918007d2b4b02fce7c8d3708cf9f7267b9c7252a7d3  revB_i4.out
```

Heaviest processes: 5x5 census 4.16 s / 757 MB; atlas custody 2.6-2.8 s /
~620 MB; every Singular run < 0.4 s / < 31 MB; primdec run 0.12 s.  All
under the 60 s / 1 GiB caps; zero swaps; no cap hits, warnings, or
signals.  `memb.out` contains four inert parser-rejection lines from one
ternary-syntax marker line; that marker (`STD_SLIM_MUTUAL=1`) was
re-derived in the clean run `mutual.out`.  Generating scripts (scratch,
deterministic from the frozen atlas bytes):

```text
8e299839aefe39e6921461ece68f76a6173dd7b502995d6fc7e4fd9fcaa13b49  polylib.py
dc797ebaecb3c90585e18709e2f188b713afd990a399e0b7458a34bedd120303  custody_A.py
2c70d0f5ec2c8eb0872dc308510d7b597be5571bf5a1891263d6c4e00355d6ab  census5.py
c546b22a3e67f03416fc685ce1ff790d9e2510d84adc516201150d39b06d238e  memb.sing
57a195f45590e23ceefe2b8b257cfcece44d28c7ce2c26aff6c3645c8d640fdf  memb_min.sing
5867b58de978ab1d19956b4e71187708e5951522beee99e16004524b752b85ba  memb_min2.sing
481c9a4b7a1b1daa825caf6407f5ade6d421a1635162653bed1d83eb288ec739  memb_lift_dump.sing
83379905b6b6c390e9289d3708e680097037b45138b616bce1a1a6e876062668  memb_lift_dump2.sing
b52ad4ef04a0527c09c0900488cd4747c812df9ccd514dbb193c7fc1bda9a096  mutual.sing
1d0a5b91b1f3027708aaad874f0e0807f186fc88ca0d45711e3abe72703506fa  revB_custody.py
4fd559017339ad7fe9708553701d41b0918a85f4457a3000fe18cd1b09af7a94  revB_ideals.sing
db750d3334ec4bdeeba25e0d7bfaf9191d763c9795bd2bbe3558cf44255a343b  revB_rabin.sing
b5edcc47b926334d6417e83b347612e2b1765aeb026314a10d7038af4ebd83da  revB_minass.sing
3ae4e2cd6d7f82a176826790f983f9d841c6b9f91dedb07ed1f9eac3054223f9  revB_minass2.sing
a04851c0e42a55e6fef21269c48258d89864ee76a43cbf45808563027f7f69a1  revB_pins.sing
a4e093d2f126be1c4e04ec3d594a974bcf1f9c7914b1668134b0c668d80b5003  revB_i4.sing
```

## charge_basis

```text
charge_basis:
  0a3af03ed8d07db852f833d0dc9ebe3ec151934308f4a139cf7ac72124f9b3cb  xmodel/k00-rank5-maxclass-next-sol56-20260829.md
  e0947368509714aa96376789914a4dbfd7141b1f77832016bf4dbe7c3caa45e4  xmodel/k00-grade3-rankle1-primary-grok46-92e-20260829.md  (actual bytes; zero-field self-seal 3e2b13b2... verified)
  e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
  d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501  cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/aws_box02_r2_held_compile/output/ATLAS_EXACT_POLYNOMIALS.json
  17d13f45fd64b8b3cb584e7451891d9f9f2201b18be70b280d2a04014e1a0e58  .../output/A_COMPOUND_MINORS.json
  f1a6f1fc988fc77816daaab13b294b1321de7e476d2891cf7fbfa2e033868d97  .../output/RESULT.json
  5de20da0d3501db668fca38db3c678ba4719745e3df7b32d0d0a8d2867e4da32  .../output/COMPILED_SOURCE.sha256
  ea2f8a4519a5a0bb1dcf35edbb02bc9600971f8b16eb90cb2b64367c6b1bafd8  .../output/CONTROLS.json
  24640d0dacec16b27b4c7eb83419188aa86e3fc80b481b0ba64aa136348fc892  cases/.../compile_fitting_atlas_v26.py  (hash-convention source)
  794b1d8e399e8b331a45acfa5df94d4552b47890c23686ce215948c0ea749995  cases/.../NOTATION_CLARIFICATION_R1_GRADE2_ROWS.md
  ce5063930117bc8fe9869dc80f1535459dd41209a35406ed7edacde1213618dd  cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/aws_r6a_alt_full_p6_rank2_chart_r5r7_c6c7/output/P6_LITERAL_SOURCE_LABELS.json
  c8aa23e46f909e70c2c8d302ca67a415496df9a969f99817d2ef593f60f614c0  .../aws_r6a_r2_exact_base3/output/BASE3_R2_STANDARD_BASIS.txt
  a840c9b69d64646e900531dddfba8ba9309336c61a83ddefb424a33d2fcdc26b  .../aws_r6a_r3_exact_base2/output/BASE2_R3_STANDARD_BASIS.txt
  c42c0482f0b5861f5099e6e121c60a93d018c87a9619749ee1844f5954545c39  .../RESULT_V27_BASE3_R2_EXACT_PREPASS.md
  8e4b545d72e2dc62a1c60090e2d956969320d738c6c35968944039e3bccb80a2  .../RESULT_V27_BASE2_R3_EXACT_PREPASS.md
  ceb69e22c43cb366d52a2e7d9bd3ec9d5ae4befd18368202d711a20e4b5e3f99  .../DESIGN_ERRATUM_R3_SIZE_NCOLS.md
  acede1dc67a4516c67c64368a8fedc5ce516897bfcb381454bb26b108cf9380a  .../RESULT_V27_CONSTANT_KERNEL_REPLAY.md
  b9358a7dac37bfd9e8c5389e4ce9dddc02af4d35182e7957a943df0f9b2d786d  .../aws_r6a_aux_constant_kernel/output/RESULT.json
  88516f87868cb27a78ac9b35d15d6aeef3ea555182710424d9520b2f9bfb565e  .../aws_r6a_aux_constant_kernel/output/L0_B_PRIMARY.txt
  2e8ceeb42dcc41752f82fe1df866c28b33e289097b065bf965db25574230919c  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/aws_r6b_r2_pass/output/SOURCE_COLUMNS.json
  738f46030a73fea2a06a8e3139ed9aa5e2001b72a579e459357af81f6801647a  xmodel/k00-v27-base4-base3-base2-hostile-review-fable5-20260827.md
  f9d2afcb01c1ad1161783d0ff51d9d47d1a6aa5831b508936072f0c9170012b9  xmodel/max12-812-order2-k00-v24r6r1-leading-base-dw-hostile-review-sol-ultra-20260827.md  (provenance identified; W re-proved here)
  d9e653150d14bc2791e366c2e425de5790f0f4390ab5790469bb9fe6ef4b644b  xmodel/promotion-crossaudit-d5g-r6-k00r6r1-opus5-20260827.md  (provenance identified; W re-proved here)
  ac843e4c3da54a60d96f8b15961f1d75ffb45ca7ebef1664d44c755fffb25d76  xmodel/k00-chartfree-next-sol56-20260829.md  (branch pointer only)
  55fb39eaddb5a57a4d90967cfad74e621b6d763c1738de949c33deeba4898e29  cases/k00_g3_r2_chartfree_v1_20260829/PACKET.md  (dedup only)
  6bb957b4983cdfc36ab667cb2ad34aebb5325dd08a64d00dcef593bbb70fd2c8  xmodel/k00-g3-r2-chartfree-hostile-review-grok46-92e-20260829.md  (dedup; consumed at reviewed status in table row 5)
  8c273911283ff3b25d1a4b0158feb5f3311901b68c170abc7ab7a8139b0aae70  xmodel/k00-g3-r2-chartfree-coordinator-integration-sol56-20260829.md  (dedup only)
```

## Seal

- Body definition: all bytes of this file before the literal `## Seal`
  heading.
- Body length: 29665 bytes.
- Body SHA-256: `b3dd864afaf5878fd079fc202da5ee7e89f53bc35bc353ff3eab1a0a4cb86b9f`.
- Frozen basis: `92ebe92ad5986a47f01af9ed901260595dfed869`.
- Full-file SHA-256: recorded by the lane runner out of band.
