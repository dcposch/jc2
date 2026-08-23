# D43 rung-28 C-diag adjudication

**Date:** 2026-08-22  
**Scope:** the banked `a00pp` D43 family data over
\(\mathbf F_{105337}\) and \(\mathbf F_{105673}\), in the residue-A,
B-frozen, no-log, `PIN42`, \(W_1W_2\ne0\) chart of
`SHEET6-DIRECTIONB.md` section 10. This is an exact adjudication of the
reported modular failure. It is not a characteristic-zero or locus-wide
D43 verdict.

## 1. Verdict

The outcome is **(A), with a correction to its diagnosis**:

\[
 \boxed{\text{the emitted dormant-55 block is correct; the C-diag checker
 rejected a valid zero scalar multiple.}}
\]

This is an implementation defect in `proportional`, shared by
`d43_family.py` and `d43_family2.py`; it is not evidence that the
dormant-level emission was zero-filled or mis-reconstructed. It is also not
the structural alternative (B). The rank-two ordinary carrier does **not**
terminate at rung 28.

At rung 28 the four level-55 columns have an exact zero in the boundary row
\(h=28\). If \(d_j\) is the nonzero factor chosen from the first row, that
entry is

\[
                         0=0\,d_j.
\]

The current helper returns `None` for this case and the caller reports
`C-diag factorization FAILS`. The required correction is exactly:

```python
def proportional(pa, pb, p):
    # Decide pb = lambda * pa.  The zero polynomial is 0 * pa.
    if not pb:
        return 0
    if not pa:
        return None
    if set(pa) != set(pb):
        return None
    m0 = next(iter(pa))
    lam = pb[m0] * pow(pa[m0], p - 2, p) % p
    for m, c in pa.items():
        if pb[m] != c * lam % p:
            return None
    return lam
```

Equivalently, in the present caller, `col[i0]` is known nonzero and the
minimal repair is `if not pb: return 0` before the old one-sided-zero test.
One must **not** fill the boundary coefficient with a dormant-55 value or
delete the boundary row. The coefficient is exactly zero and the normalized
constant matrix must retain a zero there.

## 2. Why the reported assertion fired

For rung 28 the selected rows and columns are

```text
rows:    h = 1,4,7,10,13,16,19,22,25,28
columns: tf1_55 tf2_55 tg1_55 tg2_55
         tf1_60 tf2_60 tg1_60 tg2_60 tg01_60 tg02_60
```

For each of the first four columns, in both raw symbolic banks and both
normal-form banks, the per-row term-count vector is

```text
[1,1,1,1,1,1,1,1,1,0].
```

Thus the assertion at `(28, "tf1_55", 9)` does not detect an extra
non-proportional polynomial. It compares a nonzero one-monomial reference
`pa` with the empty polynomial `pb={}`. The old code says:

```python
if not pa and not pb:
    return 0
if not pa or not pb:
    return None
```

The second branch is mathematically wrong when `pa != 0` and `pb == 0`.
The exact difference support reported in section 10.5 is therefore not an
extra boundary term: `common = 0`, `reference-only = 1`,
`boundary-only = 0`.

This also resolves the dormant-level question. `tf1_55` is present as a
symbol in the 189-variable bank and is extracted as a rung variable. Its
*value* was not inherited as zero when this affine coefficient was
computed. The zero in \(\partial E_{28,28}/\partial\mathrm{tf1}_{55}\)
is an emitted support zero, not an assignment to `tf1_55`.

## 3. Exact level-55/rung-28 block

Normalize each nonzero column by its first nonzero polynomial factor. Write

\[
 A_{28}=C_{28}\operatorname{diag}(d_1,\ldots,d_{10}).
\]

In both primes the normalized matrix has the exact repeated-column shape

\[
 C_{28}=
 [\,v_1\ v_2\ v_1\ v_2\ w_1\ w_2\ w_1\ w_2\ w_1\ w_2\,].       \tag{3.1}
\]

The four displayed vectors, in row order
\(h=1,4,\ldots,28\), are as follows.

| \(h\) | \(v_1\) | \(v_2\) | \(w_1\) | \(w_2\) |
|---:|---:|---:|---:|---:|
| **\(p=105337\)** ||||
| 1  | 1 | 1 | 1 | 1 |
| 4  | 104665 | 653 | 104995 | 52989 |
| 7  | 91384 | 84229 | 54755 | 103316 |
| 10 | 45723 | 41991 | 74317 | 83592 |
| 13 | 97268 | 13970 | 75532 | 38664 |
| 16 | 43475 | 70619 | 18568 | 95506 |
| 19 | 95047 | 55161 | 9539 | 46556 |
| 22 | 35469 | 2081 | 48746 | 61953 |
| 25 | 30243 | 968 | 30997 | 101406 |
| 28 | **0** | **0** | 14263 | 65837 |
| **\(p=105673\)** ||||
| 1  | 1 | 1 | 1 | 1 |
| 4  | 75813 | 29841 | 90737 | 67751 |
| 7  | 101337 | 74836 | 82002 | 76573 |
| 10 | 51337 | 36657 | 81599 | 76814 |
| 13 | 47392 | 99425 | 75320 | 39240 |
| 16 | 14288 | 100170 | 89143 | 25295 |
| 19 | 44465 | 24032 | 105388 | 33076 |
| 22 | 5169 | 91208 | 41195 | 93340 |
| 25 | 136 | 42916 | 41604 | 55997 |
| 28 | **0** | **0** | 4561 | 22958 |

The first four, dormant-55 columns form

\[
 A_{28}^{(55)}=[v_1\ v_2\ v_1\ v_2]
                  \operatorname{diag}(d_1,d_2,d_3,d_4),
 \qquad \operatorname{rank}A_{28}^{(55)}=2.                \tag{3.2}
\]

The six level-60 columns form

\[
 A_{28}^{(60)}=[w_1\ w_2\ w_1\ w_2\ w_1\ w_2]
                  \operatorname{diag}(d_5,\ldots,d_{10}),
 \qquad \operatorname{rank}A_{28}^{(60)}=2.               \tag{3.3}
\]

The two column spaces are independent enough to give

\[
 \boxed{A_{28}\text{ has shape }10\times10\text{ and exact rank }4}
                                                               \tag{3.4}
\]

at both primes. A nonzero rank-four minor uses rows
\(h=(1,4,7,10)\) and columns
`(tf1_55,tf2_55,tf1_60,tf2_60)`; its values are

```text
p = 105337: 37062
p = 105673: 84146
```

For completeness, the chosen diagonal factors are all units in the scoped
\(W_1W_2\ne0\) chart:

| column | \(d_j\bmod105337\) | \(d_j\bmod105673\) |
|---|---:|---:|
| `tf1_55` | \(76028W_1\) | \(76645W_1\) |
| `tf2_55` | \(59451W_2\) | \(3W_2\) |
| `tg1_55` | \(56593W_1\) | \(30669W_1\) |
| `tg2_55` | \(61740W_2\) | \(35567W_2\) |
| `tf1_60` | 45896 | 30444 |
| `tf2_60` | 27173 | 59009 |
| `tg1_60` | 4515 | 85377 |
| `tg2_60` | 16997 | 101558 |
| `tg01_60` | 54926 | 95525 |
| `tg02_60` | 61167 | 50779 |

The canonical row-major hashes of the normalized \(10\times10\) matrices
(compact JSON integer arrays) are

```text
p = 105337: a9c13cbacf0e79f90cc5aab2aedd51b943bd8298a8d308aff14c07898247e438
p = 105673: 29db80727bee33eb74606e4f691bb60b2f5cce9437505af16bbb4fba86992e06
```

The hashes are identical whether \(C_{28}\) is extracted from the raw
900-MB symbolic bank or from the corresponding det23-normal-form checkpoint.
Hence NF reduction neither creates nor removes the boundary zero. A direct
evaluation with the separate numeric `eplus43` engine at the named witness
also gives

```text
d/d(tf1_55,tf2_55,tg1_55,tg2_55) E[h=28,k=28] = (0,0,0,0)
```

at each prime.

## 4. Corrected all-rung census

Running the zero-safe proportionality test in memory, without changing the
banked files, gives the following exact result at **each** prime:

| rung \(k\) | selected rows | y-frontier columns | \(\operatorname{rank}C_k\) | y compatibility rows |
|---:|---:|---:|---:|---:|
| 26 | 10 | 10 | 4 | 6 |
| 28 | 10 | 10 | 4 | 6 |
| 30 | 9 | 10 | 4 | 5 |
| 32 | 10 | 10 | 4 | 6 |
| 34 | 10 | 10 | 4 | 6 |
| 36 | 10 | 10 | 4 | 6 |
| 38 | 10 | 10 | 4 | 6 |
| 40 | 10 | 10 | 4 | 6 |
| 42 | 10 | 10 | 4 | 6 |
| **total** | **89** | **90** | **36 pivot ranks** | **53** |

Every C-diag factorization passes. At every rung, including 28, the four
ordinary columns have rank 2, the six even-frontier columns have rank 2,
and the full y-frontier has rank 4. Thus the exact data affirm the
rank-2-plus-rank-2 structure; they do not show its termination.

There is a separate, previously hidden count correction at rung 42. If
`Xf_alpha,Xg_beta` are included as independent x-side coordinates, as in
`SHEET6-DIRECTIONB.md` 10.1 and `sol-xside-spec.md` 2.2 case 3, then

\[
 A_{42}^{\rm full}\text{ has shape }10\times12,qquad
 \operatorname{rank}A_{42}^{\rm full}=5.                  \tag{4.1}
\]

The y-only subblock still has rank 4. The two x columns are mutually
proportional (their actual ratio is \(3:-2\)), so together they add exactly
one direction. Consequently rung 42 has five, not six, compatibility rows
in the independent-x model.

This is not a new C-diag failure: both x columns factor correctly. It is a
correction to the hard-coded prose “53 compat rows” when that prose is
combined with independent x tangents.

## 5. Correct certificate shapes

Three shapes must be kept separate.

### 5.1 Conditional 30-stream / 180-column model

Under the question's \(184\times180\) convention—equivalently, after a
proved fixed/derived x classification satisfying **CONJECTURE X-SIDE-30**—the
operator shape remains

\[
                         M_{43}^{y}:184\times180.
\]

The D25-to-D43 residual family has the conditional raw presentation

\[
 123\text{ equations in }118\text{ variables}
   =(34+89)\text{ in }(28+90).
\]

The corrected rung ranks eliminate 36 pivot equations and 36 pivot
coordinates. The Schur/compatibility certificate therefore has

\[
 \boxed{34+53=87\text{ equations over }118-36=82
        \text{ remaining coordinates}}.                   \tag{5.1}
\]

Pure free frontier parameters may be omitted from a serialized polynomial
ring, but must remain named in the reconstruction/free-parameter manifest.

### 5.2 Independent x-side model actually recorded in section 10.1

With independent \(\alpha,\beta\), the legal derivative window is

\[
                         M_{43}^{\rm full}:184\times182,
\]

not \(184\times180\). The residual family has 123 equations in 120
variables. The total rung rank is \(8\cdot4+5=37\), and the number of
compatibility rows is \(89-37=52\). Its equivalent Schur count is

\[
 \boxed{34+52=86\text{ equations over }120-37=83
        \text{ remaining coordinates}}.                   \tag{5.2}
\]

The x-kernel direction \((D\alpha,D\beta)=(2,3)\) remains free. The
distinction between (5.1) and (5.2) is load-bearing: one may not report the
87-row conditional certificate after adjoining the independent x columns.

Neither (5.1) nor (5.2) is yet an `EMPTY` or `NONEMPTY` certificate. The
corrected family chain must still form the compatibility polynomials, replay
them against the numeric engine, and decide the resulting ideal on all named
rank charts.

## 6. Consequences for \(\ell^+\) and the \(H_{29}\) dichotomy

The rung-28 repair changes no operator coefficient, residual value, or
derivative image. It only allows the family compression to continue.
Therefore:

1. The banked \(H_{29}u^0=t^{36}e_{29}\) obstruction and the pointwise
   lower bound
   \[
                              \ell(L_s^+)\ge37
   \]
   are unchanged.
2. No D43 survivor has yet been produced by this family chain. Hence the
   corrected factorization by itself certifies neither \(\ell^+\ge43\) nor
   flatness at 37.
3. In the conditional 180-column y diagnostic, the banked smoke computation
   leaves \(H_{29}u^1=t^{42}e_{29}\) uncovered. At the named mode-2
   completion this would imply \(\ell^+\ge43\) **only** after the required
   fixed/derived x-side theorem and, for a genuine D43 measurement, a same-
   point D43 residual certificate.
4. In the independent-x model, the two x columns contribute one image
   direction at rung 42 and the banked smoke computation covers
   \(H_{29}u^1\). Thus no growth beyond 37 is currently certified there.
   Another level-42 target could still supply a floor of 43, and every
   target must be rescanned at an actual D43 survivor.
5. If the corrected family ideal is empty on an exhaustively certified
   chart, that is a finite-depth chart kill; no loss argument is needed.
   If it is nonempty, each reconstructed survivor needs its own
   \(184\times180\) or \(184\times182\) derivative, old-\(H_{29}\) replay,
   literal loss scan, and exact dual witnesses.

Accordingly the `FLAT-H29` versus `SHIFTED-H29-BINDING` dichotomy remains
open. The rung-28 event supplies no evidence for a new structural rank and
no evidence that a deviation polynomial merely vanishes at sampled points:
there is no deviation polynomial at all.

## 7. Exact-data provenance and remaining gaps

The remote artifacts used in this adjudication were:

```text
d43modp_p105337_a00pp.pkl
  19a4f73ce8dd271406610fc2e716eea583e259ce6478abf8580b895a9ed4588a
d43modp_p105673_a00pp.pkl
  97ff826c81df596c321ed2d727edb187b762236bd103e30bccfbae1544b2f14d
d43red_p105337_a00pp_band28.pkl
  1fb7e6feab1692d5f5e7ac2caa40521d1aef106751a3f4c4bde78b0e5e4f9c96
d43red_p105673_a00pp_band28.pkl
  9ceefcbacb8b0576eb1f055d1cebda9a00fe869d9dec2704d3cb232524986472
d43_family2.py
  c4e97d9542faea59303dfb4c4584632f152fb1f22f5eb2d34151833305abe332
```

The audit performed four exact checks:

- raw-bank and NF-bank extraction of every rung-28 affine column;
- zero-safe polynomial proportionality and finite-field rank at both primes;
- all-rung y-frontier factor/rank census through rung 42;
- rung-42 recomputation with the exact x correction and both independent x
  columns.

The following remain explicitly **CONJECTURE** or unproved:

- **CONJECTURE (CHAR-0-LIFT):** the two-prime modular family factorization,
  including all later compatibility polynomials, lifts to the intended
  characteristic-zero object. The running `build_tails43.py` gold lane had
  not completed at adjudication time.
- **CONJECTURE (LOCUS/FIBER COVER):** the `a00pp` result transports faithfully
  to every required fiber, cell, and rank chart. No such exhaustion was
  computed here.
- **CONJECTURE X-SIDE-DERIVATION**, **CONJECTURE X-SIDE-30**,
  **CONJECTURE CYCLIC-30**, **CONJECTURE BRIDGE-30**, and the Row-42
  post-41 grading/first-occurrence conjectures remain exactly as in
  `sol-xside-spec.md`.
- **CONJECTURE (D43 VERDICT):** the corrected 87-row or 86-row family ideal
  is empty or nonempty. The aborted run never reached this decision, and
  this adjudication did not run the downstream Gröbner/pivot verdict.
- `FLAT-H29`, `SHIFTED-H29-BINDING`, `LOCUS-UNIVERSAL-H29`, and every
  all-depth finite-loss/formal-existence implication remain conjectural.

## 8. Final ruling for the ledger

Replace the section-10.5 interpretation by:

> **ADJUDICATED: checker defect, not structural failure.** At rung 28 the
> four dormant level-55 columns vanish in the boundary row \(h=28\). The
> family proportionality helper incorrectly rejected this valid
> \(\lambda=0\) entry. With zero-safe proportionality, the raw and reduced
> banks agree at both primes; the level-55 subblock is \(10\times4\) of rank
> 2, the level-60 subblock is \(10\times6\) of rank 2, and the full rung is
> \(10\times10\) of rank 4. All y-frontier rungs 26--42 pass. The conditional
> 180-column model yields 53 compatibility rows (87 including the parked
> 34); the independent-x 182-column model yields 52 (86 including parked),
> because rung 42 has rank 5. The D43 EMPTY/NONEMPTY and \(H_{29}u^1\)
> survivor verdicts remain open.

