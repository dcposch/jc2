# Hostile review: K00 exact filtered compatibility through D8 (V10)

Reviewer model: Opus 5.  Date: 2026-08-27.
Charged case: `cases/max12_812_order2_u2_62_k00_filtered_macaulay_d8_v10_20260827/`.

## Verdict

**PASS.**

The charged claim is independently established.  No producer `PASS`,
`ENDPOINT`, `status`, or validator string was used as evidence: every load-
bearing fact below was recomputed here from `tails.json` with a
reviewer-written emitter, or hand-checked.

Everything charged was reproduced: the matrix byte-for-byte, the exact `Q`
ranks `2547 = 2547`, the 492-entry lift replaying all 2,996 equations, and the
D2–D7 prefix.  Two observations are recorded that do **not** touch the claim:
one `EVIDENCE.sha256` line fails (on the review-request document, not on any
mathematical artifact), and the producer's validator reads the rank integers
from metadata instead of recomputing them.  Neither is a defect in the
mathematics; both are detailed in §8.

## 0.  What was adjudicated, and what the claim is equivalent to

At the frozen normalized K00 germ `C6=1`, with `m=(d0,...,d5)` and `r1,...,r7`
the unloaded ordinary tails, the complete cumulative multiplier system through
transverse normal degree 8 is consistent, with rank equal to augmented rank,
and a saved exact rational multiplier jet replays every equation.
Equivalently

```text
r7  in  (r1,...,r6) + m^9      in Q[d0,...,d5],   at C6 = 1.
```

I verified that the stated equivalence is tight in both directions, which the
producer asserts but does not prove:

* (⇐) consistency of the emitted system exhibits polynomial multipliers of
  degree ≤ 6 with `sum q_l r_l - r7 ∈ m^9`, hence membership;
* (⇒) conversely, if any polynomial multipliers work, truncating each `q_l` at
  degree 6 changes `sum q_l r_l` only by elements of `m^9`, because every
  `r_l` lies in `m^2` (verified: §1) and every discarded multiplier term has
  degree ≥ 7.  So the degree-≤6 multiplier space is *complete*, not a
  heuristic truncation, and consistency is equivalent to membership.

Nothing stronger is adjudicated.  See §6 and §7 for what is refused.

## 1.  Custody and typing (attack 1)

All charged hashes recomputed locally and matched:

| artifact | sha256 | status |
|---|---|---|
| exact `RESULT.json` | `cc2bed36104932b731c1408b3ab7af635cdc86a2162cf8026db0dc1c4a4b852a` | match |
| mod-p `RESULT.json` | `3f70961e92c6fbba2fe236cf6f06ae70ec762f3adb5c7675e7c98b5c0a238389` | match |
| matrix (both lanes) | `15837b4e24431a61e4cc8f2498bc4cd27959b03b6150f76609b319c1dcbabc30` | match, byte-identical across lanes |
| exact lift | `0b29e3cc3485b39370ed59a8833328b51d469e104eed6edcfabc3d6f5fadb360` | match |
| V9 exact report | `bd1c636827061f1506573487618e533f34cfe413eab042be65411bfaa2eef178` | match |

Every one of the 11 lines of `FREEZE.sha256` verifies today, including
`tails.json` = `d72f774c…3848`, the V9 emitter = `fb82763d…3f7f`, the V9 exact
`RESULT.json` = `8749885b…b81e`, and `ops/aws_exact_lane.sh`.  The self-hash of
`FREEZE.sha256` is `1b26e81c60f2df4126d1819324a0c5050d426bd49673a08a12c1221f3a411b9b`,
equal to `freeze_sha256` in `AWS_REGISTRATION.md`.  The canonical
sorted-compact JSON digest of `tails.json` is
`6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`, equal to
the emitter's `EXPECTED_ALL_TAILS`; so the tail source is pinned twice, by raw
bytes and by canonical serialization.  The four files pinned inside the V9
emitter (`oneparameter` note, quadratic V6 `RESULT.md`, V8 preregistration, V9
preregistration) still carry their pinned digests.  `ENDPOINT_EVIDENCE.sha256`
in both lanes matches the harvested local copies once the AWS-absolute job
paths are remapped.

**Typing, re-derived, not consumed.**  I re-expanded all seven rows from the
frozen tails with my own code, asserting rather than assuming the type
invariants: each monomial is a length-10 exponent vector over
`(a0..a6, k10, k6, k2)` with non-negative entries; each is weighted homogeneous
of weight exactly `12+ell` for weights `(8,7,6,5,4,3,2 | 2,6,10)`; the load
part `(k10,k6,k2)` is at most linear.  All assertions pass.  Restricting to
`load = (0,0,0)` and substituting the K00 chart

```text
a0 = (1+d0)/256,  a1 = d1,  a2 = (1+d2)/16,  a3 = d3,
a4 = (3+d4)/8,    a5 = d5,  a6 = C6 = 1
```

gives

| row | weight | unloaded terms | loaded dropped | expanded terms | normal degrees |
|---|---:|---:|---:|---:|---|
| `r1` | 13 | 19 | 17 | 16 | 2..4 |
| `r2` | 14 | 27 | 27 | 23 | 2..4 |
| `r3` | 15 | 30 | 28 | 27 | 2..5 |
| `r4` | 16 | 40 | 41 | 36 | 2..5 |
| `r5` | 17 | 44 | 45 | 40 | 2..5 |
| `r6` | 18 | 57 | 63 | 42 | 3..6 |
| `r7` | 19 | 63 | 68 | 57 | 2..6 |

Every row vanishes to order ≥ 2 at K00 (`r6` to order 3), so the order-2
sentinel is real and the degree-0 and degree-1 rows are legitimately absent
from the system.  I checked `r1` by hand, off the machine expansion.  Its
constant term vanishes structurally: every one of its 19 unloaded monomials
contains at least one of `a1,a3,a5`, all of which vanish at K00.  Its linear
part vanishes by cancellation, e.g. for `d5`

```text
21/512 + (-15/64)(3/8) + (9/32)(1/16) + (-3/8)(1/256) + (9/32)(3/8)^2 + (-3/8)(1/16)(3/8)
 = (84 - 180 + 36 - 3 + 81 - 18)/2048 = 0,
```

and likewise `d3: (-60+108-27-24+3)/1024 = 0` and `d1: (6-9+3)/64 = 0`.

**Provenance note.**  `emit_D8.py` loads the V9 emitter as a library and calls
`substitutions`, `tail_sector`, `degree_piece`, `write_matrix` directly; it
never runs V9's `main()`, so V9's own `EXPECTED` pin block is not executed at
D8 time.  I confirmed the V9 module body has no import-time side effects, and
that the four files in that block do not enter the D8 arithmetic at all
(they are provenance only).  The tail source, which *does* enter, is pinned
independently by `emit_D8.py` and by `freeze_check`.  No gap.

## 2.  Independent emission of the complete cumulative D8 map (attack 2)

I wrote an emitter from the mathematical specification (`indep_emit.py`,
sha256 `d61cf0e520df9d38a41ff6b069d2208f8010e0201d0c56f1fac1a8e991514525`) —
own polynomial arithmetic, own monomial enumeration, own serialization — and
emitted the system directly from `tails.json`.  Result:

```text
2996 x 5544,  92821 nonzero entries including the RHS column
sha256 = 15837b4e24431a61e4cc8f2498bc4cd27959b03b6150f76609b319c1dcbabc30
```

**byte-identical** (`cmp`) to the matrix in *both* frozen lanes.

Shape derived, not accepted:
`rows = sum_{D=2}^{8} C(D+5,5) = 21+56+126+252+462+792+1287 = 2996`;
`columns = 6 * sum_{g=0}^{6} C(g+5,5) = 6 * (1+6+21+56+126+252+462) = 6*924 = 5544`.
The upper multiplier degree 6 is forced, not chosen: `deg q + 2 ≤ 8`.

Ordering confirmed against the descriptor: rows are normal degree 2→8 then the
producer's recursive monomial enumeration; columns are multiplier degree 0→6,
then row 1→6, then the same monomial enumeration; the RHS is column index
5544 and carries exactly the 57 coefficients of `r7`.

Structure worth recording: a column of multiplier degree `g` has entries only
in rows of normal degree ≥ `g+2`, so the system is block lower triangular in
`(normal degree, multiplier degree)` with the diagonal at `g = D-2`.

**Denominator custody.**  Every coefficient in `tails.json` has a power-of-two
denominator (max `2^23`), and the chart images introduce only `2^-8, 2^-4,
2^-3`.  Consequently every entry of the emitted matrix is `n/2^k` with
`|n| ≤ 1179` and `k ≤ 21`: 19 distinct denominators, all powers of two.  The
only prime occurring in any denominator is 2.  Every odd prime is therefore a
legitimate reduction, and `65521` in particular carries no denominator hazard
(verified directly: no denominator ≡ 0 mod 65521, and no numerator either).

As a byproduct my emitter reproduces all six V9 matrices bit-for-bit
(`f872bb5a…`, `860930d5…`, `06b23490…`, `13cee569…`, `3b29f5de…`,
`1a094f16…`), and I verified that each `D_k` system for `2 ≤ k ≤ 7` is
*exactly* the leading block of the D8 system (rows `< n_k`, columns `< m_k`,
RHS remapped), with no D8 column outside the range ever touching a `D_k` row.

## 3.  Rank over exact Q (attack 3)

The load-bearing half — `rank(A) = rank([A|r7])` — is certified **exactly and
independently**, and not from the finite-field lane: an explicit exact
rational solution replays (§4), and consistency of `Ax=b` is equivalent to
equality of the two ranks.  That certificate is self-contained and does not
rely on FLINT, on the producer's engine, or on any modular computation.

Independent exact-`Q` ranks, recomputed here by sparse rational elimination
with Markowitz-style pivoting (`exactrank.py`,
`4504cf8482d6d3cdb19fcb3e5444acb53a2ff7338e658a80791a75bf08b253b6`):

| cutoff | shape | `rank(A)` | `rank([A|r7])` | consistent | V9/V10 claim |
|---:|---|---:|---:|---|---|
| D2 | 21 × 6 | 4 | 4 | yes | 4 |
| D3 | 77 × 42 | 28 | 28 | yes | 28 |
| D4 | 203 × 168 | 106 | 106 | yes | 106 |
| D5 | 455 × 504 | 294 | 294 | yes | 294 |
| D6 | 917 × 1260 | 676 | 676 | yes | 676 |
| D7 | 1709 × 2772 | 1372 | 1372 | yes | 1372 |
| D8 | 2996 × 5544 | **2547** | **2547** | **yes** | 2547 |

D2–D7 are exact `Q` and reproduce the entire V9 ladder, including the
promotion sentinel `1372` that `emit_D8.py` gates on.  Independently of the
producer, the D2 rank 4 is confirmed by hand-scale elimination on the six
quadratic leading forms.

The D8 row is exact `Q` as well: the full 2996 × 5544 augmented system was
row-reduced here over the rationals in 7 m 51 s at 230 MB peak RSS, giving

```text
rank_Q(A) = 2547,   rank_Q([A|r7]) = 2547,   consistent.
```

So the charged value `2547` is **independently reproduced in characteristic
zero**, by a different algorithm (sparse rational elimination with sparsity
pivoting) than the producer's dense FLINT `fmpq_mat_rref`, on a matrix I
emitted myself from `tails.json`.  No finite field enters this computation.

**Second, unrelated confirmation, by a route that never touches the
producer's lane.**  I compiled a small mod-`p` elimination
of my own (`rank.c`, `81aa665f97939d90b244f835c3b6183d1a044e96615b1934975015a95b2a81f2`;
no CAS, ~1 s per run) and ran it on my independently emitted matrix at six
primes, five of them unrelated to the producer's:

```text
p = 65521      rank_A = 2547   rank_aug = 2547   consistent
p = 999983     rank_A = 2547   rank_aug = 2547   consistent
p = 1000003    rank_A = 2547   rank_aug = 2547   consistent
p = 15485863   rank_A = 2547   rank_aug = 2547   consistent
p = 32452843   rank_A = 2547   rank_aug = 2547   consistent
p = 67867967   rank_A = 2547   rank_aug = 2547   consistent
```

Since `rank_p ≤ rank_Q` at every `p` where no denominator vanishes, and all
denominators are powers of two (§2), this independently forces
`rank_Q(A) ≥ 2547` even without the rational elimination above — and it agrees
with it exactly.  Note the direction of inference: the finite fields are used
only to *bound* the characteristic-zero rank from below and to probe for
bad-prime behaviour.  The characteristic-zero value, the rank equality, and
the membership statement all rest on the exact `Q` computations of this
section and §4.

*Self-caught artifact, recorded for honesty.*  My first attempt used
`p = 2^31 - 1` and returned `2547 → 2924 / 2925, inconsistent`.  That was an
overflow of *my own* delayed-reduction accumulator — the scheme is valid only
while `(rows+1)·p² < 2^64`, which fails at 31-bit primes — not a producer
defect.  I added an explicit refusal guard and re-ran in the safe range.  The
episode is reported because a reviewer who had stopped there would have filed
a spurious `FAIL`.

**Internal coherence of the ladder.**  From the seven ranks, the cokernel
dimension in each normal degree is

```text
D        2    3    4    5    6    7    8
dim V_D  21   56  126  252  462  792 1287
new rank  4   24   78  188  382  696 1175
coker    17   32   48   64   80   96  112      (sum = 449 = 2996 - 2547)
```

so `dim_Q Q[d]/((r1..r6)+m^9) = 1 + 6 + 449 = 456`, and the cokernel sequence
is `16(D-1)` for `D ≥ 3` with a single extra dimension at `D = 2`.  A linear
Hilbert function of this shape is not something an incorrect rank ladder
would produce by accident; it is strong structural corroboration that the
seven independently checked ranks belong to one consistent computation.

## 4.  Parsing and replaying the exact multiplier jet (attack 4)

`solution_D8.tsv` (`0b29e3cc…b360`) parsed with a strict reader that rejects
malformed lines, duplicate columns, out-of-range columns, and zero values
serialized as nonzero entries.  It carries 7 metadata lines and **492** `x`
lines, and **zero** `y` lines — correct, since a consistent endpoint must not
also ship a left incompatibility certificate.  Metadata is internally
consistent: `field Q`, `cutoff 8`, `rows 2996`, `columns 5544`,
`rank = augmented_rank = 2547`, `consistent 1`.  Entry heights are ≤ 182-bit
numerators over ≤ 162-bit denominators, consistent with a rational RREF.

Two independent replays, both against *my* emission:

**(A) Polynomial replay (ordering-free).**  I decoded the 492 coefficients
through my own column dictionary into six multipliers `q_1,...,q_6 ∈ Q[d]`,
then formed `S = sum_{l=1}^{6} q_l r_l - r7` directly from the *re-expanded*
tails — never touching the serialized matrix.  Result:

```text
S has 62 terms; the degrees present are exactly {9, 10};
S has 0 terms of total degree <= 8.
```

That is a direct exact proof of `r7 ∈ (r1,...,r6) + m^9`, independent of row
order, column order, and of the matrix serialization entirely.

**(B) Coefficientwise replay.**  All **2996** equations of the independently
emitted 2996 × 5544 system replay to exact zero residual.  All 2996 rows carry
at least one coefficient entry (no vacuous row); 57 rows carry a nonzero RHS.

Multiplier profile of the lift:

```text
row      1    2    3    4    5    6      total
terms  123  100   82   68   65   54        492
degs  0-5  1-5  0-5  1-4  0-4  1-4
```

**D2–D7 regression against reviewed V9.**  Truncating the V10 lift to the
2772 columns of multiplier degree ≤ 5 satisfies all 1709 D7 equations exactly,
as it must given the block structure of §2.  The lift has **zero** entries in
the multiplier-degree-6 block.  That is the RREF free-variable convention, not
a truncated multiplier: all 2772 degree-6 columns were present in the system
that was solved and ranked, as the byte-identical emission shows.

## 5.  The modular lane treated strictly as a software control (attack 5)

Enumerated attacks and their disposition:

* **Bad-prime leakage.**  All denominators are powers of two, so no odd prime
  can be bad in the denominator sense; verified explicitly for 65521.  The
  rank and consistency verdict is reproduced at five further primes spanning
  `10^6`–`6.8·10^7`.  Nothing in the exact conclusion routes through any prime:
  §4(A) is characteristic-zero throughout.
* **The p-lane is not independent evidence.**  All 492 modular entries are
  *exactly* the reductions mod 65521 of the exact rational entries, on the
  same column support, computed from the byte-identical matrix.  It is the
  same algorithm on the same input, so it corroborates only that FLINT's
  `nmod` and `fmpq` paths agree.  The producer's `RESULT.md` says precisely
  this ("corroboration only, not characteristic-zero evidence").  Honest.
* **Swapped or perturbed RHS.**  My emitter places `tails["7"]` in the RHS by
  construction.  Falsification controls at `p = 1000003` on my emission:

  ```text
  RHS = r7                                 rank 2547 / aug 2547   CONSISTENT
  RHS = r7 + d0^2                          rank 2547 / aug 2548   inconsistent
  RHS = r7 + d2^4                          rank 2547 / aug 2548   inconsistent
  RHS = r7 + d1 d3^2 d5^3                  rank 2547 / aug 2548   inconsistent
  RHS = r7 + d0 d1 d2 d3 d4^2 d5^2         rank 2547 / aug 2548   inconsistent
  RHS = pseudo-random element of m^2/m^9   rank 2547 / aug 2548   inconsistent
  RHS = r6  (a generator; sanity)          rank 2547 / aug 2547   CONSISTENT
  ```

  So the D8 `PASS` is not vacuous: the cokernel is 449-dimensional and a
  single monomial perturbation at any degree from 2 to 8 destroys
  consistency.  The degree-8 perturbation is the sharpest: it leaves the
  entire D7 prefix untouched yet breaks D8, which proves that **D8
  compatibility is strictly stronger than D7 compatibility** and that V10 is
  genuinely new content over V9 rather than a re-statement of it.
* **Truncated multipliers.**  Refuted structurally in §0 and §2: degree ≤ 6 is
  the complete multiplier space for this congruence.
* **Row/column-order mistakes.**  Refuted by §4(A), which is order-free, and
  by an additional chart control: repeating the whole emission with the plain
  translated coordinates `e_i = a_i - a_i(K00)` and again with a rescaled
  chart (`a1 = 7e1`, `a4 = (3/8)(1+e4)`, `a5 = -2e5`) leaves the shape,
  nonzero count, ranks, and the consistency verdict unchanged, as an
  invertible linear change of normal coordinates must.
* **False sparse-solution parsing.**  Refuted by the strict parser above.
* **Rank versus augmented-rank confusion.**  The engine does not compute
  `rank(A)` directly: `fmpq_mat_rref` returns `rank([A|b])`, and `rank(A)` is
  derived as `augmented_rank - [inconsistent]`.  That derivation is correct,
  and the zero-coefficient-row-with-nonzero-RHS test does detect
  inconsistency correctly.  But the *validator* re-reads both integers from
  the solution metadata and only checks that `augmented_rank - rank ∈ {0,1}`
  and that the flag agrees; it never recomputes either.  So `2547` is
  engine-asserted.  This is why §3 and §4 were done independently.  It does
  not endanger the claim, because the claim needs the *equality*, which the
  replay certifies outright.

Runner hygiene: `run_D8_aws.sh` is `set -euo pipefail`, refuses non-EC2 hosts,
runs `sha256sum -c` on the freeze before anything else, exports the registered
lane tag, applies `ulimit -v`, and appends `validator=PASS_FILTERED_D8` only
after a successful validator exit.  The banner is producer-authored but
genuinely guarded.  The Q lane's `time -v` shows 955 s CPU, 8,174,576 KiB peak
RSS, 0 swaps, exit 0, under a 256 GiB cap — consistent with a rational RREF of
this size (my own mod-`p` rank of the same matrix takes 1 s and 133 MB, and
the gap is exactly the rational coefficient growth one expects).  The p lane
took 11 s and 285 MB.

Cosmetic: the mod-p `RESULT.json` carries `"characteristic_source": 0`
alongside `"field": "65521"`.  It is inherited from the emitter audit and is
literally true (the *source* tails are characteristic zero), but a careless
reader could misread it as a char-0 result.  Worth a wording pass; not a
defect.

## 6.  Reconciliation with reviewed V8, and refusals (attack 6)

V8 proves `r7 ∉ (r1,...,r6)` on the generic `D(C6)` coefficient chart.  V10
proves `r7 ∈ (r1,...,r6) + m^9` at `C6=1`.  **There is no tension**: the second
is a statement about a finite jet at one point, the first about the polynomial
ideal.  A polynomial can fail to lie in an ideal while agreeing with it to any
prescribed finite order at a chosen point.

I independently confirmed the identity V8 quotes, on my own expansion of the
degree-2 leading forms:

```text
r7_2 = -(1/512) * r1_2 - (1/128) * r3_2      (exact, verified termwise)
```

and that the six quadratic leading forms span a 4-dimensional space with
`r6_2 = 0`, giving `rank(A_D2) = 4` over `Q`.

Explicitly rejected inferences:

* D8 compatibility does **not** imply polynomial membership `r7 ∈ (r1,...,r6)`
  — V8 refutes that outright.
* D8 compatibility does **not** imply membership in the local ring at K00.
  That would require `r7 ∈ I + m^n` for *every* `n`; by Krull, the intersection
  over all `n` is the localized ideal.  V10 supplies exactly one value,
  `n = 9`.
* D8 compatibility does **not** imply formal membership, nor anything about
  the completion.
* D8 compatibility does **not** establish the existence of a finite
  obstruction, and does **not** establish its non-existence.  It moves a lower
  bound: the first pure-coefficient filtered obstruction, if there is one, is
  at normal degree ≥ 9.  The cokernel is nonzero in every degree 2..8 (17, 32,
  48, 64, 80, 96, 112), so the system is nowhere near saturating and no
  stabilization argument is available from this data.
* The failed V11–V13 local-transform producers are **not** evidence for V10
  and are not used here.  Confirmed on disk: V11 and V12 carry `FAILURE.md`
  and no `RESULT.md`; V13 has only a preregistration, freeze, and compiler
  with no result directory at all.  V10's `RESULT.md` does not cite them.

## 7.  Firewall (attack 7)

* **Loads are zero.**  Only monomials with zero exponent on all of
  `(k10, k6, k2)` enter; 17/27/28/41/45/63/68 loaded terms are dropped from
  rows 1..7 respectively.  Verified in my own emitter, not inherited.
* **`C6 = 1`.**  `a6` maps to the constant 1 with no normal direction; the
  transverse chart is 6-dimensional in `(d0,...,d5)`.  The map
  `(d0..d5) → (a0..a5)` is an affine isomorphism, so `m = (d0,...,d5)` is
  exactly the maximal ideal at the K00 point on that slice.
* **Scope note on the slice.**  Because `a6` has weight 2 while `a1,a3,a5`
  carry odd weights, `C6=1` is a weighted-Kummer normalization rather than a
  plain dehomogenization.  V10 states its claim *on the slice*, so nothing
  needs to be lifted and nothing is wrong; but no off-slice or `D(C6)`-generic
  statement is licensed by V10 on its own.
* No `Lambda`, load, target, `mu`, `Jdet`, closure-first incidence, Taylor
  realization, receiver, order-two, maximum-twelve, or JC2 conclusion is drawn
  here, and none is drawn by the producer: a sweep of `RESULT.md` and
  `PREREGISTRATION.md` finds those terms only inside explicit disclaimers.

## 8.  Findings

**F1 — `EVIDENCE.sha256` drift (bookkeeping; outside the claim).**  27 of 28
manifest lines verify.  The failing line is
`xmodel/max12-812-order2-k00-d8-hostile-review-prompt-20260827.md`: manifest
says `16d92f969e579e275d958e4f47532ecfe658185a6f3485965554492238b5a1e1`, the
file hashes `13da05a7eb3e698f15c8694b6f3b9afbc8f4073a36ff1fe8e631133b11ef96d0`
and is untracked with an mtime 4 minutes after the manifest.  This is the
review-request document, not a mathematical artifact, and no evidentiary
artifact drifted.  I did not modify it.  Recommended repair: re-stamp the line
or drop the prompt from the evidence manifest.

**F2 — the validator does not recompute the rank integers (design note).**
See §5.  The validator reads `rank` and `augmented_rank` from the solution
metadata rather than recomputing them, so within the producer's own pipeline
those integers are unchecked.  Fully mitigated here: all seven ranks D2–D8,
including `2547`, were recomputed over exact `Q` by an independent algorithm
(§3), and the equality the claim actually needs is separately certified by the
exact replay (§4).  The observation stands as a design note on the validator,
not as an unresolved gap.

**F3 — the p-lane is correlated with the exact lane (scope).**  Its 492
entries are the exact entries reduced.  The producer already labels it
corroboration only; no over-claim.

**F4 — cosmetic.**  `"characteristic_source": 0` in the mod-p `RESULT.json`
(§5).

**F5 — reviewer-side, self-caught.**  My 31-bit-prime rank run overflowed and
was discarded (§3).

None of F1–F5 changes the verdict.

## 9.  The strongest statement that survives

> Let `r1,...,r7` be the unloaded ordinary tails of the frozen `u2_62` strict
> Rees compilation, restricted to the K00 transverse chart at `C6=1` with
> `m = (d0,...,d5)`.  Each `r_l` lies in `m^2` (and `r6 ∈ m^3`).  Then there
> exist explicit polynomials `q_1,...,q_6 ∈ Q[d0,...,d5]` of degree ≤ 5, with
> 492 nonzero rational coefficients of height ≤ 182 bits, such that
>
> ```text
> sum_{l=1}^{6} q_l * r_l  -  r7   has no term of total degree <= 8,
> ```
>
> i.e. `r7 ∈ (r1,...,r6) + m^9`.  Equivalently the complete cumulative
> multiplier system through transverse normal degree 8, of shape 2996 × 5544
> and sha256 `15837b4e…cbabc30`, is consistent over `Q`, with
> `rank_Q(A) = rank_Q([A|r7]) = 2547`.

That statement is verified here end to end from `tails.json`, in
characteristic zero, without recourse to any finite field and without using
any producer status string.

What it does **not** say is set out in §6 and §7: no polynomial membership, no
local or formal membership, no claim about a finite obstruction in either
direction, no off-slice statement, and nothing about `Lambda`, loads, targets,
`mu`, `Jdet`, closure-first incidence, Taylor realization, receivers, order
two, maximum twelve, or JC2.  The single downstream effect of V10 is to move
the earliest possible pure-coefficient filtered obstruction from normal degree
8 to normal degree ≥ 9.

## 10.  Reproduction

Reviewer scripts, staged outside the campaign tree in `/tmp/k00rev/`:

```text
indep_emit.py   d61cf0e520df9d38a41ff6b069d2208f8010e0201d0c56f1fac1a8e991514525
replay.py       be7056cc6ad1e8706cf68db64adbc50446a1ab626a036bbd40d1422cce576363
prefix.py       f7ca51e6b5af07738954b2ca564f9250097a022bc1ef7d91681822eb13fba856
rank.c          81aa665f97939d90b244f835c3b6183d1a044e96615b1934975015a95b2a81f2
exactrank.py    4504cf8482d6d3cdb19fcb3e5444acb53a2ff7338e658a80791a75bf08b253b6
nullcontrol.py  aa2e2b69644a1179d029384a3e16c99486f585c9128abd654d51cd0eaea4461a
chartvar.py     a1b2959c944a5348d6db640428ff3ca664dc13020e34fcea964a7912f132fd59
```

```sh
python3 indep_emit.py 8      # -> 2996 x 5544, sha 15837b4e...cbabc30
python3 replay.py            # -> polynomial + coefficientwise replay, 492 entries
python3 prefix.py            # -> D2..D7 leading-block and D7 regression
cc -O2 -o rank rank.c && ./rank indep_D8.tsv 1000003
python3 exactrank.py         # -> exact Q ranks (D8 row: 7m51s, 230 MB)
python3 nullcontrol.py       # -> RHS falsification controls
python3 chartvar.py          # -> chart-normalization controls
```

## 11.  Execution notes

All work was local and desk-scale: pure-Python exact rational arithmetic (the
heaviest single item being the exact `Q` rank of the full D8 system, 7 m 51 s
at 230 MB) plus one ~120-line C mod-`p` elimination (≈1 s, 133 MB per run).  No AWS job was
launched, no web access was used, no computer-algebra system was invoked, and
no canonical ledger was edited.  `jc2-lean` was not entered, read, built,
status-inspected, or modified.  The only file written in the repository is
this report.
