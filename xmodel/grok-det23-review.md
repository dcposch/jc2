# Hostile review: SHEET6-DIRECTIONB.md §8.S5 det23

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-19.
Scope: the campaign-riding claim that V(row22red) is nonempty over
the algebraic closure of F_p on the specialized radical_point chart
fiber, at p = 105337, 105673, 200257. Read: §8.S5, xmodel/nf-quickshot.md,
cases/directionb_det23_p105337.ms + .rows.txt, the three banked
det23 GBs, cases/nf_reduced_rows_p*.txt, notes.md 07:14Z/07:15Z/08:25Z
tail, xmodel/sol-avenues3.md §2–3. Method: independent python3
reparse of the NF payload, exact F_p linear algebra, polynomial
identities for g_s and the 200 3x3 minors, GB-file census. No
Singular, no msolve rerun, no other repo file modified, no git.

**VERDICT: CONFIRMED — claims (1)–(4) recompute; the bidirectional
emptiness equivalence holds on this chart; a 509-element reduced GB
that is not `[1]` is a proper ideal, hence V(det23) (and therefore
V(row22red)) is nonempty over F_p-bar at all three primes. Claim (5):
8.S5 states the fiber / mod-p / chart-local scope honestly and does
not claim the other 35 radical fibers, char 0, or F_p-rational
points. Residual items below do not flip the fiber-local NONEMPTY.**

The load-bearing sentence is the addendum at
`SHEET6-DIRECTIONB.md:1466-1472`: the det23 ideal is proper, so
V(det23) is nonempty over the closure, and by the rank pin
V(row22red) is nonempty on this radical_point chart fiber, mod p.
That sentence survives.

---

## Claim chain

### (1) The 6 NF rows are affine in 4 tg vars, A = C diag(uW1², uW2², uW1², uW2²), rank C = 2

**CONFIRMED, all three primes, by reparse of `cases/nf_reduced_rows_p*.txt`.**

- Each payload has exactly 6 × 150 terms. Occurring extras are only
  `{x17, x25, x32, x37}`. `{x16, x24, x69, x47, x52}` are absent.
  Degree in the four tails is 1 (no `tg_i * tg_j`, no `tg_i²`).
- Each tail column is a **single shared carrier**:
  `x17, x32` ride `uW1^2`; `x25, x37` ride `uW2^2`. So
  `A = C · diag(uW1², uW2², uW1², uW2²)` as an identity of
  matrices of polynomials, not a pointwise observation.
- Recomputed C matches the matrices recorded in
  `cases/directionb_det23_p*.rows.txt` entrywise.
- `col0 + col2 = 0` and `col1 + col3 = 0` in F_p, i.e.
  `C = [c1 | c2 | −c1 | −c2]`. All 15 of the 4×4 minors vanish; all
  80 of the 3×3 minors of C vanish. Rank(C) = 2. Nonzero 2×2 witness
  on rows `{24,25}` (payload rows 0,1) and cols `{x17,x25}`:
  `76716` at 105337 (equals the sol-avenues3 minor `76716*uW1²*uW2²`
  after stripping units), `44429` at 105673, `4327` at 200257.
- Emission last three rows of `directionb_det23_p105337.ms` (and the
  other two primes) are coefficient-exact for the claimed `g1,g2,g3`.
  Input shape 400 rows = 397 + 3, 282,316 terms = 282,304 + 12.

No denominators appear in A or b. This is not a localization.

### (2) rank(A) = 2 everywhere on the chart

**CONFIRMED. The saturation actually pins it.**

On V(fiber GB) one has `uW_i · W_i − 1 = 0`. This is not a
reduce-and-hope claim: those two binomials are **elements of the
reduced fiber GB and of the det23 GB** (printed as
`1*W_i^1*uW_i^1+(p-1)`). So every point of V(GB), and every point of
V(det23), has `uW_i` and `W_i` units. Then `D = diag(uW1²,uW2²,uW1²,uW2²)`
is invertible and `rank A(x) = rank C = 2` at every such point.

Off the chart the rank does drop, and only there: at random
`(uW1,uW2) = (0,1), (1,0), (0,0)` one has rank A = 1, 1, 0
respectively. 8.S5's warning that a consumer who drops the pin must
fall back to the one-way minor reading is correct and necessary.
It is not a hole in the emitted object, because the uW rows are in
the input and still in the output GB.

### (3) Solvability ⇔ g1 = g2 = g3 = 0 ⇔ V(det23) empty iff V(row22red) empty

**CONFIRMED on the chart, both directions. The hunted gaps are not there.**

Linear algebra over the residue field at a chart point x:

- `exists tg : A(x) tg + b(x) = 0` iff `u · b(x) = 0` for every
  `u ∈ leftker(A(x))`.
- `leftker(A(x)) = leftker(C)` because D(x) is invertible. C is
  **constant**, so the left kernel is a constant 4-dimensional
  F_p-subspace of F_p^6. There is no chart locus at which a cokernel
  basis degenerates, and no pivot/denominator in the kernel
  calculation.
- Recomputed: `dim leftker(C) = 4`. The nf-quickshot kernel vector
  `a` lies in it, and `a · NF = 0`, `a · b = 0` as polynomial
  identities (so one of the four conditions is the zero polynomial).
  The coefficient matrix of `{u · b : u ∈ leftker}` has rank **3**.
- The recorded `w1,w2,w3` all lie in leftker(C). `w_s · NF = g_s`
  exactly (5, 5, 2 terms); tail monomials cancel. `{g1,g2,g3}` are
  linearly independent and **span the 3-dimensional condition
  space** (each of the four `u·b` polynomials, including the
  10-term ones, lies in `span_F_p{g1,g2,g3}`).
- Full 3×3 census of the 6×5 `[A|b]`, as **polynomials**, all three
  primes: 120 identically zero, **80 nonzero, 80/80 in
  `span{g1,g2,g3}` after stripping the unit monomial
  `uW1² uW2²` (or a sign)**. Matches 8.S5's 80/200. So
  V(GB + g's) = V(GB + all 3×3 minors) as chart sets. The unit
  monomial is a unit on V(GB); it does not add or lose zeros there.
- `g1,g2` have the perfect-square leading piece `(x57−x65)² uW_i²`
  with coefficients `(1, −2, 1)` at all three primes. `g3` is
  `x70 + e x72`. Independently: `g3` is not in the fiber ideal,
  because a reduced grevlex fiber GB in this variable order would
  then contain a degree-1 element with LM `x70`, and the fiber
  prefix does not.

Set-theoretic translation, chart-fiber:

- If `(x, extras, tg) ∈ V(row22red)`, then `x ∈ V(GB)` and
  `NF(x,tg) = 0` (nf-quickshot: `NF ≡ row` on `V(GB)×A^7`), hence
  `g(x) = 0`, hence `x ∈ V(det23)`.
- If `x ∈ V(det23)`, then `x ∈ V(GB)`, `g(x) = 0`, the affine
  system in the four tails is solvable (rank pinned at 2), and
  `{x16,x24,x69}` are free. A lift exists in `V(row22red)`.

This is a **set** equivalence of affine varieties over F_p-bar, not
an ideal equality and not a scheme isomorphism. Emptiness /
nonemptiness only needs the sets. No remaining denominator. The
only way the converse dies is if a consumer evaluates off the
`uW·W=1` chart; 8.S5 says so.

Inherited, not re-derived here (stated perimeter, not a hole in
the linear algebra): `NF_j ≡ row22red-row_j` on `V(GB)×A^7`
(nf-quickshot Singular block-order division) and the 8.S4
row22red ↔ row22compat chart isomorphism (unit pivots, constant U).

### (4) 63 s msolve GB = 509 ≠ [1] at 3 primes ⇒ nonempty over the closure

**CONFIRMED. No trivial-unit / saturation subtlety.**

Banked files `cases/directionb_det23_gb_p{105337,105673,200257}.out.txt`:

| prime  | header | parsed els | terms   | linear | constants | maxdeg |
|--------|--------|------------|---------|--------|-----------|--------|
| 105337 | 509    | 509        | 405,524 | 3      | 0         | 16     |
| 105673 | 509    | 509        | 405,524 | 3      | 0         | 16     |
| 200257 | 509    | 509        | 405,524 | 3      | 0         | 16     |

- Leading monomials are identical across the three primes, in
  order. Term-count sequence is identical. Variable-monomial
  supports are identical element-for-element. The only
  printed-support mismatch is the constant `p−1` in the two
  saturation binomials `W_i uW_i − 1` — that is the field, not the
  shape. 8.S5's "support identical element-for-element" is true for
  the actual monomials.
- No constant polynomial. In particular the reduced GB is not
  `{1}`. In a polynomial ring over a field the only units are
  nonzero constants, so a reduced GB other than `{1}` means `1 ∉ I`.
- Affine Nullstellensatz over an algebraically closed field: `V(I)`
  empty iff `1 ∈ I`. Hence V(det23) is nonempty in `A^{22}` over
  F_p-bar. This is the correct theorem for msolve's affine `-g 2`
  output.
- Saturation-variable trap, hunted: the chart inverses are already
  **polynomial generators** `uW_i W_i − 1 ∈ I`. If some power of
  `W_i` or `uW_i` were a unit after saturation, it would already be
  a unit in `R/I` (its inverse is the other variable), forcing
  `1 ∈ I`. A proper GB cannot hide a chart-saturation unit. The
  output GB still contains those two binomials, so the computed
  variety is still on the chart.
- `g3` is itself a GB element (`1*x70^1+e*x72^1`), so the linear
  residual survived into the basis. Saturation rows survived.

I did not rerun msolve. Trust that the 509-el files are the reduced
GBs of the emitted 400-row inputs sits on: (i) the emission
recomputes to the independent g's, (ii) the 397-prefix of
`directionb_det23_p105337.ms` is byte-identical to
`cases/directionb_fiber_gb_p105337.out.txt` once the msolve
wrapper `]:` is stripped from the last fiber element (396/397 raw
string match was that wrapper; polynomials equal, 547,446 bytes),
(iii) three-prime LM / term-count / support identity. A
catastrophic msolve bug that produced a 509-element proper-looking
basis of a unit ideal at three primes with identical supports is
outside the attack surface that python3 can close; it is the
stated msolve perimeter.

### (5) Scope: one radical fiber of 36, mod p, chart-local — does 8.S5 say so honestly?

**Mostly yes. Not a false global claim. Incomplete if read in isolation.**

What 8.S5 actually asserts:

- INTERNAL / UNREVIEWED, no promotion claims.
- "per-fiber at the specialized radical_point base, per-prime, mod p".
- "no variety-level claim is made here — emptiness is what the
  launched runs decide" (construction paragraph), then the addendum
  reports a variety-level decision **on that same fiber**.
- "the depth-23 exclusion FAILS at the variety level on the
  radical_point chart fiber, at all three primes (mod p)".
- Dimension / degree / F_p-rational points / char-0 lift are
  explicitly open.

What 8.S5 does **not** say, and must not be read as saying:

- The other 35 radical fibers (`3×3×2×2` specializations of
  `A1,A2,HW1/W1,HW2/W2`, sol-avenues3 §2). The integer 36 does not
  appear in 8.S5. It does appear earlier in SHEET6-DIRECTIONB.md
  (G0.7 / §8 vicinity, lines 1124–1126) and in notes.md 08:25Z.
  A reader of the whole sheet can recover that `radical_point` is
  one named branch. A reader of 8.S5 plus the addendum punch line
  alone could over-promote.
- The unspecialized 87-variable D23 hybrid, B-unfrozen residue A,
  or JC2.
- Existence of an F_p-rational point (the 24 sampled chart points
  all miss; that is consistent with a thin sublocus over a field
  of size ~10^5, and is not a contradiction).

The wording tension between "no variety-level claim" and "FAILS at
the variety level" is sequential, not contradictory: the
construction is emptiness-agnostic; the 63-second run decides
emptiness of **this** fiber. The phrase "variety level" is doing
work against the 24-point sample, not against the 36-fiber cover.
notes.md 08:25Z is the sharper scope sentence and should ride with
any external use.

---

## Findings (worst first)

### 1. Severity: none on the fiber-local NONEMPTY — chain holds

Recomputed (1)–(4) as above. No break. The rank-drop escape that
made the commissioned 5×5 minors vacuous is real, was correctly
abandoned, and does not apply to the emitted rank-2 object.

### 2. Severity: consumer-hazard (not a math error) — 8.S5 does not name the 36-fiber cover

- File: `SHEET6-DIRECTIONB.md:1466-1472` (and the SEMANTICS
  paragraph at 1417–1424)
- The addendum is easy to quote as "D23 is nonempty". The
  surrounding qualifiers (radical_point, chart fiber, mod p, char-0
  open) are present in 8.S5; the count "1 of 36" is not. Any
  campaign use must keep notes.md 08:25Z / sol-avenues3 §2 in the
  same breath: this kills the hope of a cheap `[1]` on **this**
  representative fiber; it does not decide the other 35, and it
  does not produce a formal germ.

### 3. Severity: nit — "GB block byte-VERBATIM" is polynomial-verbatim

- File: `cases/directionb_det23_p105337.ms` vs
  `cases/directionb_fiber_gb_p105337.out.txt`
- Raw last-element strings differ by the msolve closer `]:` (2
  bytes). After stripping the wrapper, 397/397 polynomials are
  equal. Not a wrong prefix.

### 4. Severity: nit — "support identical" includes the constants `p−1`

The only cross-prime support mismatch under a naive monomial strip
is `105336` vs `105672` vs `200256` in the two sat rows. Those are
`−1 mod p`. Variable supports match.

### 5. Inherited perimeter (labeled, not attacked as a hole)

8.S5 already lists it: banked D21 GB, 8.S4 unit-pivot isomorphism,
nf-quickshot `NF ≡ row`, msolve/Singular/flint. This review
recomputed everything that is a matrix or a polynomial identity
over the payload and the banked GB **files**. It did not re-reduce
the 1218-term Schur rows and did not re-solve the 400-row ideal.

---

## What this does and does not decide

Decided, on the radical_point W-symbolic chart fiber, mod p, at
three primes: the depth-23 compatibility block does **not** cut
the D21 fiber down to empty over the algebraic closure. The 24
F_p-rational kills are samples of a proper sublocus, not a proof
of emptiness. That is exactly the 8.S5 addendum.

Still open, and 8.S5 says so: dimension and degree of the solvable
sublocus; F_p-rational points; the other 35 radical fibers;
characteristic 0; a formal germ (NONEMPTY is not a germ).

`g3 = x70 + e x72` being linear, and `g1,g2` living on the
banked free coordinates `{x53,x58,x70,x72}` plus chart units, is
consistent with a positive-dimensional leftover (sol-avenues3's
`≥ 13−3 = 10` heuristic). It is not a dimension certificate; `-g 2`
does not report one.

---

## Recomputation ledger (python3, this review)

- Parsed `nf_reduced_rows_p{105337,105673,200257}.txt`.
- Extracted A, b; rebuilt C; ranks, minors, column relations,
  leftker, `a` and `w_s` membership, `w_s·NF = g_s`, span of
  `{u·b}`, 80/80 3×3 membership, 40 random chart-unit points per
  prime (rank A = 2; `g=0` iff all 3×3 vanish iff rank`[A|b]=2`).
- Checked emission row counts, last-three-row identities, term
  count 282,316, fiber-prefix polynomial identity at 105337.
- Census of the three 509-el GB files (counts, linears, constants,
  LMs, supports, sat rows, `g3` present).

Not run: Singular, msolve, flint Laplace/cofactor, the 24-point
kill set (accepted as recorded; it is not load-bearing for
NONEMPTY).
