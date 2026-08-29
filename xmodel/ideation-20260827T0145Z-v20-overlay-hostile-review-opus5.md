# Focused hostile review — V20 overlay claims of the Fable 5 adjudication

Reviewer: Opus 5, different-model hostile mathematical reviewer.
Date: 2026-08-27.  Repo `/Users/dc/code/math/jc2`, charged HEAD
`418e413593120d19e15e6546eb50c985f4b1f038`, dirty concurrent worktree left
untouched.  The only repository file written is this one.

Target, rehashed before reading:

```text
1481d3cadc30ee024c7d4e07e746a6e15ce000a52358e589a1fdf5add3e755c1
  xmodel/ideation-20260827T0145Z-crosspollination-hostile-review-fable5.md   MATCH
```

My own prior V20 export review, rehashed:

```text
8665e43cd9df2b6c55aeccde72daa10ddff4768813df045feeb97cb593264bf5
  xmodel/max12-812-order2-p0-total-rees-allrows-g13-g14-v20-hostile-review-opus5-20260827.md
                                                                            MATCH
```

Everything below is recomputed from frozen bytes in this session with a fresh
parser and a fresh degree-8 algebra implementation.  Nothing is taken from
Fable's numbers, from my prior review's numbers, or from model agreement.

---

## 0. Verdict table

| # | Claim audited | Verdict |
|---|---|---|
| 1 | Exact char-0 delayed-load point, Fable §4.2: `A = Q[w,s]/(w^4+1,s^2-5/12)` nonzero; all 22 rows vanish; extends to honest ordered `T-cs` with `cs*k1*rho` a unit and `k=0` | **CONFIRMED** (algebra nonzero and in fact a degree-8 field; 22/22 zero; extension exact) — one notation defect inherited from the memo (`u`), §2.4 |
| 2 | 14 V20 rows at that point: 13 nonzero, only `Tg14_5` zero, `Tg13_6 = 35/128` | **CONFIRMED** exactly, full table §3 |
| 3a | Kill identity `Tg13_6 + (1/2)cs*rho^2*Tg11_1 - (35/128)cs^4*k1*rho^4 ∈ (k,rs,c0,c1)` | **CONFIRMED**, exact, 27-term residual, coefficientwise §4.1 |
| 3b | Set-theoretic conclusion "delayed-load sub-fan dies at grade 13", char `∉ {2,3,5,7}` | **CONFIRMED** as stated, with every hypothesis exhibited as load-bearing (§4.2–§4.4); `qrs=0` **is** available and **is** load-bearing |
| 4 | `RS0` kills all 22 + all 14 rows; compatible with the `T-rs` bilinears | **CONFIRMED**, and vanishing is *termwise* (0 surviving monomials).  Exact scope in §5; **GAP** on transfer to the *promoted* `T-rs` relation list |
| 5 | Factor-two repair of the `e0e1` shifted-core cofactor, both columns | **CONFIRMED** (all eight shapes exact with `(8/3)ell1`); Fable's *printed residual* is itself wrong by `-2` — exact residual in §6 |
| 6 | `Tg14_5\|_{J1}` scope repair: corrections in `(cs1,cs2,rs1,rs2,e0,e1)` not `(cs1)`; row does not die on `qa1=0` | **CONFIRMED** exactly; all 12 printed `k`-terms reproduce byte-for-byte §7 |
| 7 | `M >= 1` gate sound via promoted `CS0`, independent of `deg_2` | **CONFIRMED**; exact certificate shape and generator list in §8; survives enlargement to 36 rows |
| 8 | Parity-refined torsion composition ⟹ existence-only `cs^(3m+6) k^(3m+2)` honest membership | **CONFIRMED** as an existence statement.  Even-part step is *justified* (§9.2).  Saturation is used, at step 2 only, and is correctly flagged non-effective.  No false converse §9.4 |

Net: **no load-bearing claim of Fable's V20 overlay falls.**  Three
presentational defects found (§10), all inside Fable's own repairs rather
than in the results; two scope statements need tightening before the ledger
consumes them.

---

## 1. Custody and method

Row bytes reparsed from frozen files (exact `Q` lane), hashes observed here:

```text
Tg10_1..Tg12_7   cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826/
                   aws_q_v9/compiled/Tg{10,11,12}_{1..7}.poly      21 files
  e.g. Tg11_1.poly  11f6bd635957677cb8a0b29cedc847369d68d6b695e844efdf32f683078db469
Tg14_5           .../t_cs_row5_g14_export_v17_20260826/aws_q/compiled/Tg14_5_q.poly
                   91d96924696ab19a59cd8661fdd778559ce8dc9c1bc0fbc886dbdf4956e838f7
Tg13_1..Tg14_7   .../allrows_g13_g14_export_v20_20260827/aws_q_v20/compiled/*_q.poly
  e.g. Tg13_6_q.poly 1544f802c29de6235764a349bda23b080b4d290b1a9f0ae503f2e3f3ad499345
```

Reparsed term counts, independent of Fable and of my prior review:

```text
g10  4, 5, 5, 2, 5, 0, 5        g13  50, 72, 103, 30, 141, 32, 156
g11 12,14,17, 3,18, 0,18        g14  85,134, 201, 71, 304, 90, 364
g12 27,36,47,12,58, 9,60        Tg14_5 = 304 (V17 = V20 g14 row 5)
```

40 distinct names across all 36 rows; `Tg10_6 = Tg11_6 = 0` literally; every
`rho` exponent even (0 odd exponents across 36 rows); denominators are powers
of `2` only, numerators divisible only by `3` and `5`.  These match the
manifest and my prior clean-room replay.

Method: exact `fractions.Fraction` sparse arithmetic; a fresh
recursive-descent parser handling both the bare V9 format and the
parenthesised V17/V20 format; a fresh rank-8 `Q`-algebra
`A = Q[w,s]/(w^4+1,s^2-5/12)` in the monomial basis `{w^i s^j}`.  Four short
scripts under `/tmp/o5v20/` (not committed):

```text
bc963462 lib.py    26c90a41 alg.py    28e15dd4 load.py    a4a410bf point.py
```

Total local cost: every computation in this report is sub-second (full
36-row evaluation in `A`: 0.14 s user, single process).  No Groebner, no CAS,
no web, no AWS read or mutation, no launch, no `jc2-lean`.

---

## 2. Item 1 — the exact characteristic-zero delayed-load point

### 2.1 The algebra is nonzero  [CONFIRMED]

`A = Q[w,s]/(w^4+1, s^2-5/12)`.  Both relations are monic in separate
variables (degree 4 in `w`, degree 2 in `s`), so `A` is **free of rank 8**
over `Q` on `{w^i s^j : 0<=i<=3, j∈{0,1}}` and in particular `A != 0`.
Recomputed in that basis: `w^4 = -1`, `w^8 = 1`, `s^2 = 5/12`, `1 != 0`.

Fable's stronger claim that `A` is the *field* `Q(zeta_8, sqrt(15))` also
holds.  `w^4+1 = Phi_8` is irreducible over `Q`, so `Q[w]/(w^4+1) = Q(zeta_8)`
has degree 4 and `Gal ≅ (Z/8)^* ≅ Z/2 × Z/2`, hence exactly three quadratic
subfields.  Their generators are visible in my basis:

```text
(w^2)^2   = -1        (w - w^3)^2 = 2        (w + w^3)^2 = -2
```

so they are `Q(i), Q(sqrt2), Q(sqrt-2)`.  Now `sqrt(5/12) = sqrt(15)/6`, so
`Q(sqrt(5/12)) = Q(sqrt15)`, and `Q(sqrt15)` equals one of those three only if
one of `-15, 30, -30` is a rational square — none is.  Hence `x^2-5/12` is
irreducible over `Q(zeta_8)` and `A` is a field of degree 8.  **CONFIRMED.**
Only `A != 0` is actually used downstream, so the field claim is a bonus, not
a dependency; Fable states this correctly.

### 2.2 All 22 frozen rows vanish  [CONFIRMED]

Substituting Fable's printed coordinates — `cs = rho = k1 = 1`,
`k = rs = c0 = c1 = 0`, all 33 remaining names `0` except

```text
a0 = (1/2)s w + (1/2)s w^2          a1 = -(1/2)s w + (1/2)s w^2
e0 = s w^2 - s w^3                  e1 = s w^2 + s w^3
k2c   = -1/8 + (1/8)w^2 - (1/4)w^3
rs1   = -1/6 + (1/3)w - (1/6)w^2
k10_4 = -275/256 + (827/384)w - (275/256)w^2
        + (1/6)s + (1/3)s w - (1/3)s w^2 - (1/6)s w^3
```

into each of the 22 rows gives `0` in `A`, **22 of 22**.

**Positive controls** (the test is not vacuous).  Perturbing a single
coordinate by `+1` breaks a large fraction of the 36 rows:

```text
a0+1 -> 25/36    e1+1 -> 25/36    k2c+1 -> 19/36    rs1+1 -> 16/36
k10_4+1 -> 15/36   k1+1 -> 20/36   cs+1 -> 25/36   k:=1 -> 26/36
```

So the 22 zeros are not a parser or evaluator artefact.

**Solve chain cross-check.**  Fable's stated pivots are exact.  Extracting
the linear coefficients from the bytes:

```text
coeff(k2c)   in Tg12_1 = (15/256)cs*rs^2 + (5/16)cs^3*rho^2      -> 5/16   at rs=0
coeff(rs1)   in Tg12_2 = ... + (15/64)cs^2*k1*rho^2              -> 15/64  at c0=rs=ell1=cs1=0
coeff(k10_4) in Tg14_5 = -(15/2048)cs*rho^4*rs^2 - (5/128)cs^3*rho^6
                                                                 -> -5/128 at rs=0
```

and the warned cross-term is present and live: `Tg14_5` contains
`-(15/2048)*cs*k2c*rho^4*rs1^2`, with `rs1 != 0` at this point, so it must be
substituted before the `k10_4` solve.  **Confirmed.**

**Residue-shadow claim.**  I independently found `w, s ∈ F_65521` with
`w^4 = -1` and `s^2 = 5/12`, and evaluated the four displayed coordinates for
all four sign choices:

```text
w=57852 s=21883 -> (60630, 16555, 26715, 62134)
w=57852 s=43638 -> ( 4891, 48966, 38806,  3387)
w= 7669 s=21883 -> (16555, 60630, 62134, 26715)
w= 7669 s=43638 -> (48966,  4891,  3387, 38806)   == memo's F65521 point   MATCH
```

The memo's `(a0,a1,e0,e1) = (48966, 4891, 3387, 38806)` is reproduced
**digit-for-digit** by the embedding `w ↦ 7669, s ↦ 43638`.  Fable's
"the three modular points are residue shadows of this one exact point" is
**CONFIRMED** for `p = 65521`.  (I did not replay `1000033` / `1000081`; the
`65521` reproduction plus the exact `A`-vanishing already carries the load.)

### 2.3 Extension to the honest ordered `T-cs` presentation  [CONFIRMED]

The honest presentation is (direct certificate `7af66e58…` §1)

```text
S# = Q[cs, rs, c0, c1, qrs, qc0, qc1, rho, k, + 34 more]   (43 variables)
K  = ( T ,  rs-cs*qrs ,  c0-cs*qc0 ,  c1-cs*qc1 ,  qrs )   T = the 22 raw rows
```

Evaluated at the point with `qrs = qc0 = qc1 = 0`:

```text
rs-cs*qrs = 0    c0-cs*qc0 = 0    c1-cs*qc1 = 0    qrs = 0    22 rows = 0
cs*k1*rho = 1  (a unit in A)                                   k = 0
```

So the point is a genuine `A`-point of `V(K)` with `k = 0` and `cs*k1*rho`
invertible.  **CONFIRMED.**  Consequence 3c — no `cs^a k1^b rho^c ∈ I + (k)`
over `Q` from the frozen 22 — follows: evaluation is a `Q`-algebra map to
`A != 0` sending the right side to `0` and the left side to a unit.

### 2.4 Defect inherited from the memo: the symbol `u`

Fable writes "extends to the ordered `T-cs` chart presentation with
`qrs = qc0 = qc1 = 0` and `u = 1`", copying the memo.  There are **two
different `u`'s** in play and the report does not disambiguate them:

* the memo's §4.2 grade-10 core sets `u := c0` — and `c0 = 0` at this point;
* the zero-sections review `959603e3…` line 45 uses `u` for the affine
  `cs`-Rabinowitsch variable in `1-u*cs`, which at `cs=1` gives `u=1`.

Only the second reading makes `u = 1` true.  It is also **not needed**: `u`
is not a variable of `S#` and `1-u*cs` is not a generator of `K`.  I verified
separately that `1-u*cs` does vanish at `u=1`, so the sentence is *true under
the second reading and harmless*, but it must be disambiguated before any
ledger copy, because under the memo's own §4.2 definition it is false.
This is a **notation defect, not a mathematical one**; Fable's audit did not
catch it.

---

## 3. Item 2 — the fourteen V20 rows at the point  [CONFIRMED]

Exact values in `A`:

```text
Tg13_1  NONZERO  -(5/768)w + (5/512)w^2 - (5/768)w^3 + (5/16)s w^2 - (5/16)s w^3
Tg13_2  NONZERO  -5/256 - (5/384)w + (5/384)w^3 + (5/16)s w^2 + (5/16)s w^3
Tg13_3  NONZERO  (125/1536)w - (5/3072)w^2 + (125/1536)w^3 + (5/32)s w^2 - (5/32)s w^3
Tg13_4  NONZERO  175/768 + (5/768)w - (5/768)w^3
Tg13_5  NONZERO  (265/6144)w - (55/12288)w^2 + (265/6144)w^3 - (5/128)s w^2 + (5/128)s w^3
Tg13_6  NONZERO  35/128                                   <-- rational unit
Tg13_7  NONZERO  -(45/4096)w + (35/24576)w^2 - (45/4096)w^3 + (5/256)s w^2 - (5/256)s w^3
Tg14_1  NONZERO  -65/192 + (65/96)w - (65/192)w^2 + (5/16)s w - (5/16)s w^2
Tg14_2  NONZERO  575/110592 - (575/110592)w^2 + (565/55296)w^3 - (5/96)s w - (5/96)s w^2
Tg14_3  NONZERO  -125/768 + (125/384)w - (125/768)w^2 + (15/64)s w - (15/64)s w^2
Tg14_4  NONZERO  -55/1536 + (55/1536)w^2 - (25/384)w^3 - (5/64)s w - (5/64)s w^2
Tg14_5  ZERO     0
Tg14_6  NONZERO  -35/1024 + (35/1024)w^2 - (35/512)w^3
Tg14_7  NONZERO  -275/6144 + (275/3072)w - (275/6144)w^2 + (5/512)s w - (5/512)s w^2
```

**13 of 14 nonzero; the only zero is `Tg14_5`, which is the already-frozen
row the point was solved against; `Tg13_6 = 35/128`, a unit of `Q ⊂ A`.**
Fable's §4.4 evaluation is **CONFIRMED** in full.

Combined with §2.2 this settles the qualitative point cleanly: the frozen 22
do **not** kill the delayed-load reading (the point is a witness), and the
grade-13 export does.

---

## 4. Item 3 — the kill identity and every hypothesis of its conclusion

### 4.1 The identity is exact ideal membership  [CONFIRMED]

Recomputed coefficientwise from `Tg13_6_q.poly` (32 terms) and
`Tg11_1.poly` (12 terms):

```text
X := Tg13_6 + (1/2)*cs*rho^2*Tg11_1 - (35/128)*cs^4*k1*rho^4
```

`X` has **exactly 27 terms**, and **0 of them** lie outside `(k,rs,c0,c1)`:

```text
in (c0) only : -3/64 a0c0rs1   3/16 a1c0cs*ell1  -3/16 a1c0cs1rho^2  -3/64 c0cs*e1
in (c1) only :  3/16 a0c1cs*ell1  -3/16 a0c1cs1rho^2  -3/64 a1c1rho^2rs1
                -3/64 c1cs*e0  -3/256 c1^2rs1
in (c0,c1)   : -3/64 c0c1cs1
in (rs) only : -3/64 a0e0rs   -3/64 a1e1rho^2rs   15/32768 k1rs^4
                75/1024 cs^2k1rho^2rs^2
in (c*,rs)   : -3/64 aa0c0rs   -3/128 c1e1rs   3/64 a1c1ell1rs   -3/64 aa1c1rho^2rs
in (k,...)   :  5/1024 c0k rs^2   15/8192 k rs^3 rs1   15/64 c0cs^2k rho^2
                5/64 c1cs*k rho^2 rs   -45/1024 cs^2 ell1 k rs^2
                15/128 cs*cs1 k rho^2 rs^2   75/512 cs^2 k rho^2 rs rs1
                -25/64 cs^4 ell1 k rho^2   15/16 cs^3 cs1 k rho^4
```

**CONFIRMED**, exactly as Fable states, term count included.  This is genuine
**ideal membership** over `Z[1/2]`, not a radical statement.

The arithmetic Fable offers for the constant also checks: `Tg13_6` carries
`+(15/128)cs^4k1rho^4`, `Tg11_1` carries `+(5/16)cs^3k1rho^2`, and
`15/128 + (1/2)(5/16) = 35/128`.

### 4.2 The grade-10 collapse, audited independently  [CONFIRMED, and stronger than cited]

With `u := c0`, `w := c1`, `p := rho^2`, restricting only `k = 0`:

```text
Tg10_1|_{k=0} = (3/8)(a0 w + a1 u)
Tg10_2|_{k=0} = (3/8)a0 u + (3/32)w^2 + (3/8)a1 w p
Tg10_3|_{k=0} = (3/16)(u w + p a0 w + p a1 u)
Tg10_4|_{k=0} = (3/32)(u^2 + p w^2)
```

**Every `rs`-bearing monomial of the four grade-10 rows also carries `k`**
(verified: 0 surviving `rs`-terms at `k=0`), so the collapse needs `k=0`
only — it does **not** need `rs=0` and it does **not** need `rho != 0`:

> Over any field of char `∉ {2,3}`: `Tg10_1 = Tg10_4 = 0` and `k=0` give
> `u w + p(a0w+a1u) = 0` with `a0w+a1u = 0`, hence `u w = 0`, and
> `u^2 + p w^2 = 0`.  If `u != 0` then `w = 0` then `u^2 = 0`, absurd; so
> `u = 0`, hence `p w^2 = 0`.  If `p != 0`, `w = 0`.  If `p = 0`, `Tg10_2`
> reduces to `(3/32)w^2 = 0`, so `w = 0`.  Either way `c0 = c1 = 0`.

So `V(k) ∩ V(Tg10_1..Tg10_4) ⊆ V(c0,c1)` set-theoretically, char `∉ {2,3}`.
**CONFIRMED** exactly as Fable cites it, with all four rows required (`Tg10_2`
is what covers `rho = 0`, `Tg10_3` is only needed via its combination with
`Tg10_1`).

**This step is radical, not membership.**  Modulo `k`, all four generators are
homogeneous of degree 2 in the grading `deg(a0)=deg(a1)=deg(c0)=deg(c1)=1`
(everything else 0), so every element of `(k, Tg10_1..Tg10_4)` has all
homogeneous components of degree `>= 2` outside `(k)`.  `c0` is homogeneous of
degree 1 and `c0 ∉ (k)`, so `c0 ∉ (k, Tg10_1..Tg10_4)`.  The containment is
genuinely only set-theoretic; the case split `u w = 0 ⟹ u=0 or w=0` needs a
field (or a domain), and the conclusion is therefore about field-valued
points, not about ideals.

### 4.3 Is `qrs = 0` really available?  **Yes, and it is load-bearing**

Available: `qrs` is a **literal generator of `K`** in the honest ordered
`T-cs` presentation (`K = (T, Bil, qrs)`), so `qrs = 0` and hence
`rs = cs*qrs = 0` at every point of `V(K)`.  It is a chart-defining equation,
not an added assumption.  (In the substituted presentation `I = (E_1..E_22)`
the variable `rs` does not exist at all, so `rs = 0` holds a fortiori.)

Load-bearing: restricting the 27-term residual to `k = c0 = c1 = 0` leaves

```text
-(3/64)a0*e0*rs - (3/64)a1*e1*rho^2*rs + (15/32768)k1*rs^4
   + (75/1024)cs^2*k1*rho^2*rs^2                        !=  0
```

and only after also setting `rs = 0` does it vanish identically.  So
**dropping `qrs=0` breaks the conclusion**; Fable is right to name the
stratum equation explicitly, and any ledger copy must keep it.

### 4.4 The conclusion, with hypotheses separated  [CONFIRMED]

> **Theorem (recomputed here).**  Let `F` be a field with
> `char F ∉ {2,3,5,7}`.  At every `F`-point of the ordered `T-cs` chart
> stratum (`rs = cs*qrs`, `c0 = cs*qc0`, `c1 = cs*qc1`, `qrs = 0`) with
> `k = 0` at which `Tg10_1, Tg10_2, Tg10_3, Tg10_4, Tg11_1, Tg13_6` all
> vanish, one has `cs^4 * k1 * rho^4 = 0`.
> Consequently the stratum meets `D(cs*k1*rho) ∩ V(k)` in the empty set.

Hypothesis-by-hypothesis audit:

| Ingredient | Type | Needed? | Source |
|---|---|---|---|
| `k = 0` | hypothesis | yes | the sub-fan being tested |
| `qrs = 0 ⟹ rs = 0` | chart equation, ideal-level | **yes**, §4.3 | generator of `K` |
| `c0 = c1 = 0` | **set-theoretic / radical** | **yes**, §4.3 | collapse, §4.2, char `∉{2,3}` |
| `Tg10_1..Tg10_4 = 0` | hypothesis | yes (all four) | frozen 22 |
| `Tg11_1 = 0`, `Tg13_6 = 0` | hypothesis | yes | frozen 22 + V20 |
| `35/128` invertible | characteristic | yes | char `∉{2,5,7}` |
| `1/2`, `3/8`, `3/32` invertible | characteristic | yes | char `∉{2,3}` |

Characteristic exclusions `{2,3,5,7}` are therefore **exactly right**: `2` from
the row denominators and the `1/2`; `3` from the grade-10 rescalings (in char 3
`Tg10_4` vanishes identically and the collapse dies); `5` and `7` from
`35 = 5·7`.  Row denominators are powers of 2 only and row numerators involve
only `3, 5`, so nothing further is excluded.

**Three scope facts that must travel with this theorem.**

1. It is a **set-theoretic emptiness statement, not a certificate.**  It
   yields no `cs^N k^M (1+rho W) ∈ K` and no explicit cofactors.  The
   collapse in §4.2 is radical-only, so ideal membership is not available by
   this route.  Fable does not overclaim here; the ledger must not either.
2. It is a statement about the **enlarged 36-row system**, not about `K`.
   `Tg13_6 ∉ T`.  Membership of `Tg13_6` in the honest total ideal is a
   *source-provenance* claim inheriting the same single-emitter debt as the
   frozen 22 — it is neither better nor worse founded than they are.
3. It genuinely requires new source: §2.2 exhibits an `A`-point of `V(K)`
   with `k=0` and `cs*k1*rho` a unit, so the frozen 22 alone cannot prove it.
   The 13-of-14 evaluation and the identity are two different confirmations
   of the same fact, one pointwise and one uniform.

**Bonus check of Fable's next-stratum claim (§4.4 tail, feeding their queue
item 2).**  `Tg14_6` restricted to `k=k1=rs=c0=c1=0` has **14 terms**:

```text
(15/128)cs^4*k2c*rho^4 + (3/32)a0^2cs^2 + (9/32)a1^2cs^2rho^2 - (3/64)cs*e0e1
 + (3/16)a0cs*e1*ell1 + (3/16)a1cs*e0*ell1 - (3/16)a0cs*ee1rho^2
 - (3/16)a0cs1e1rho^2 - (3/16)a1cs*ee0rho^2 - (3/16)a1cs1e0rho^2
 - (3/16)aa0cs*e1rho^2 - (3/16)aa1cs*e0rho^2 - (3/64)a0e0rs1
 - (3/64)a1e1rho^2rs1
```

Every displayed coefficient — `15/128`, `3/32`, `9/32`, `-3/64` — matches.
**CONFIRMED**: the next stratum is a genuine core solve, not a one-line
identity, so Fable's routing of it as desk work rather than a corollary is
correct.

---

## 5. Item 4 — `RS0`, verified and scoped

`RS0`: `rs = 1`, every other non-`rho` source name `0` (so `cs = k = c0 = c1 = 0`),
`rho` a free indeterminate.

**Vanishing [CONFIRMED, and termwise].**  All 22 frozen rows and all 14 V20
rows evaluate to the zero polynomial in `Q[rho]`.  Stronger: counting
monomials *before* summing, **not one monomial of any of the 36 rows is
supported inside `{rs, rho}`**.  The same holds for `CS0`, `A00`, `A10`,
`Z00` (0 surviving monomials each), reproducing and extending the
`959603e3…` promotion and my prior review's grade-13/14 finding.  So `RS0`'s
vanishing is combinatorial in the exponent vectors, not an arithmetic
coincidence, and no `+1`-style coefficient perturbation could break it.

**Chart compatibility [CONFIRMED].**  With `qcs = qc0 = qc1 = 0`:

```text
cs - rs*qcs = 0      c0 - rs*qc0 = 0      c1 - rs*qc1 = 0
```

**Exact scope, stated as a negative too.**  `RS0` is **not** a point of the
`T-cs` chart: `rs - cs*qrs` evaluates to `1`, not `0`.  So `RS0` gives nothing
on the `T-cs` side; `CS0` and `RS0` are statements about different charts and
must not be pooled.

**GAP on the transfer to the *promoted* `T-rs` object.**  Fable's inference
"`RS0` … gives `M >= 1` on the `rs` chart" is sound for the presentation whose
relations are the raw rows plus the `T-rs` bilinears.  But the promoted `T-rs`
identity (`total-rees-localized-rho-unit-staged-calculus-promotion-sol-20260827.md`,
"Repaired `T-rs` instantiation") states that its relation list is **"four
divided raw source rows"** with exceptional power `rs^4` and genuine localizer
`35*k` — not the 22 raw rows.  If those four are `T_i / rs^{a_i}` for frozen
`T_i`, then `RS0` kills them too (at `rs=1` a division by a power of `rs` is
invisible) and the inference transfers verbatim; if they are different rows,
it does not.  I could not identify the four divided rows from local frozen
bytes.  **Record `RS0` as: a `Q[rho]`-section of the raw-row `T-rs`
presentation, with the transfer to the promoted `T-rs` relation list left as
an open one-line check.**  The `CS0` half of Fable's §2.3 is unaffected — it
is stated against `K`, which I verified generator-by-generator (§8).

---

## 6. Item 5 — the factor-two repair, and a defect inside it

Restrictions recomputed from the bytes.

**`V(J1)` column (`rs=cs=c0=c1=0`)** — all four shapes exact:

```text
(8/3)Tg11_1|  = a0e1 + a1e0
(8/3)Tg11_2|  = a0e0 + p a1e1
(32/3)Tg12_4| = e0^2 + p e1^2
(16/3)(Tg12_3 - (p/2)Tg12_1)| + (8/3)*ell1*Tg11_1|  =  e0e1
```

**`V(k)` column (`rs=c0=c1=k=0`)** — all four shapes exact:

```text
(8/3)Tg11_1|  = a0e1 + a1e0 + (5/6)cs^3*k1*p
(8/3)Tg11_2|  = a0e0 + p a1e1
(16/3)(Tg12_3 - (p/2)Tg12_1)| + (8/3)*ell1*Tg11_1| = e0e1 - 2cs(a0^2 + p a1^2)
(32/3)Tg12_4| = e0^2 + p e1^2 - 8 p cs a0a1
```

Fable's diagnosis is **CONFIRMED**: the memo printed `(1/2)*ell1*(8/3)Tg11_1`,
i.e. `(4/3)ell1`, where the correct cofactor is `(8/3)ell1` (equivalently
`(1/2)ell1` against `(16/3)Tg11_1`), and the **same** correction applies to
the `V(k)` column.

**Defect in Fable's own repair.**  Fable reports the residual of the memo's
printed identity as `a0e1ell1 + a1e0ell1`.  The exact residual is

```text
V(J1):  LHS_memo - e0e1                      = -(1/2)a0e1*ell1 - (1/2)a1e0*ell1
V(k) :  LHS_memo - (e0e1 - 2cs(a0^2+p a1^2)) = -(1/2)a0e1*ell1 - (1/2)a1e0*ell1
                                               - (5/12)cs^3*ell1*k1*rho^2
```

i.e. in **both** columns the residual is exactly

```text
-(1/2) * ell1 * [ (8/3)*Tg11_1| ]     (verified identically zero difference)
```

Fable's printed value is `-2 ×` the true `V(J1)` residual and omits the `V(k)`
load term.  This is a **normalisation slip in the erratum, not in the
correction** — the factor-2 verdict and both corrected columns stand.  But if
the ledger copies Fable's residual verbatim it will record a wrong number
while fixing a wrong number.

---

## 7. Item 6 — `Tg14_5|_{J1}` census  [CONFIRMED exactly]

`Tg14_5` restricted to `rs=cs=c0=c1=0` has **62 terms**, of which **exactly
12 contain `k`**.  Recomputed from `91d96924…`, all twelve reproduce Fable's
printed list, coefficient and monomial:

```text
-(5/128) a0*a1*k*rho^4
+(5/64)  cs1*e0*ell1*k*rho^2      -(5/128)  cs1*ee0*k*rho^4
+(15/1024) cs1*ell1*k*rs1^2       -(15/1024) cs1*k*rho^4*rs1*rs2
-(15/128) cs1^2*cs2*k*rho^6       +(15/128)  cs1^3*ell1*k*rho^4
-(5/128) cs2*e0*k*rho^4           -(15/2048) cs2*k*rho^4*rs1^2
+(5/256) e1*ell1*k*rho^2*rs1      -(5/512)   e1*k*rho^4*rs2
-(5/512) ee1*k*rho^4*rs1
```

(Fable's third line prints `cs1*ell1*k*rs1^2` without a `rho` power; the bytes
agree — that term is genuinely `rho`-free.)

Census results:

* terms outside `(cs1, cs2, rs1, rs2, e0, e1)`: **exactly 1**, namely
  `-(5/128)a0a1k rho^4`.  So the memo's "modulo the shifted `J1` block"
  reading is right and Fable's exact statement
  `Tg14_5|_{J1} ≡ -(5/128)a0a1krho^4  mod (cs1,cs2,rs1,rs2,e0,e1)` is
  **CONFIRMED**.
* terms **not** divisible by `cs1`: **6 of 12** — `a0a1krho^4`,
  `cs2e0krho^4`, `cs2krho^4rs1^2`, `e1ell1krho^2rs1`, `e1krho^4rs2`,
  `ee1krho^4rs1`.  So "plus `cs1`-weighted corrections" is **REFUTED**;
  Fable's "not `(cs1)`" is **CONFIRMED**.
* **Does the row die on `qa1 = 0` alone?  No.**  Setting `a1 = 0`,
  `Tg14_5|_{J1}` still has **47 terms**, of which **11 contain `k`** — every
  one of the twelve above except `a0a1krho^4`.  Fable's **GAP as stated** is
  **CONFIRMED**, and the memo's sentence "it is `a0a1`-weighted, hence dies on
  the ordered stratum `qa1=0`" must not be quoted.

The downstream consequence Fable draws is also right: the `A00`/`A10` sections
kill the entire block (`cs1, cs2, rs1, rs2, e0, e1, ee0, ee1, ell1` are all
zero there), so those sections and the `H3` negative control survive on the
promoted `959603e3…` evidence — but they are no longer *derived* from the
memo's one-line mechanism.

---

## 8. Item 7 — the `M >= 1` gate, via `CS0` only

**Certificate shape, exactly.**  From the promoted staged calculus, a
registered certificate on the `T-cs` chart is

```text
f_i^N * s * (1 + rho*W)   with   f_i = cs (exceptional chart power),
                                 s   = k^M (genuine localizer),
```

and the direct-certificate instance is `cs^447 * k^164 * (1 + rho*W)` with
`W = 0`, an **ordinary polynomial identity in `S#`** — "no factor of `cs` and
no factor of `rho` is inverted anywhere; the only localization used is at `k`,
and it is paid for by `k^164`".  This is decisive for the gate: because the
final statement is polynomial, evaluation at a point with `k = 0` is defined.
(Had the certificate been an identity in `S#[1/k]`, the argument below would
be inapplicable — this is the one hypothesis worth checking each time.)

**Honest ideal generators needed for the evaluation.**  `K = (T, rs-cs*qrs,
c0-cs*qc0, c1-cs*qc1, qrs)`.  I evaluated **every** generator at `CS0`
(`cs=1, k=0`, all other source names `0`, `rho` free, extended by
`qrs=qc0=qc1=0`):

```text
rs-cs*qrs -> 0     c0-cs*qc0 -> 0     c1-cs*qc1 -> 0     qrs -> 0
22 frozen rows -> 0   (and, as a bonus, all 14 V20 rows -> 0)
1-u*cs -> 0 at u=1    (optional; not a generator of K)
```

So `CS0` induces a `Q`-algebra map `S# -> Q[rho]` killing `K`.

**The gate.**  Suppose `cs^N * k^M * (1 + rho*W) ∈ K` with `M = 0` and
`W ∈ S#`.  Applying the map: the left side goes to `1^N * (1 + rho*W|_{CS0})`,
a polynomial in `Q[rho]` with **constant term 1**, hence nonzero; the right
side must be `0`.  Contradiction.  Therefore **`M >= 1`**.  **CONFIRMED**,
using only the promoted zero-sections result plus a four-line bilinear check
— no `deg_2`, no grading lattice, no refuted material.

Three scope notes.

* The gate says nothing about `N`: `cs = 1` at `CS0`, so `cs^N ↦ 1` for all
  `N`.  Only the genuine localizer is constrained.
* The argument is **fail-safe** in the required direction: it shows no
  genuine certificate can have `M = 0`, so rejecting `M = 0` harvests can
  never reject a true certificate.  Keeping the gate is strictly safe.
* It **survives enlargement**: `CS0` also kills the 14 V20 rows, so the gate
  remains valid against the 36-row system.  This is a real strengthening over
  Fable's statement, which only checked the 22.

Fable's §1f verdict — the memo was wrong to declare the gate unsound — is
therefore **CONFIRMED**, and the memo's decision "drop the `M >= 1` gate"
should be reversed.

---

## 9. Item 8 — the parity-refined torsion composition

### 9.1 The links, recomputed

**Step 5 first, since it is the arithmetic input.**  I re-expanded the
grade-10 torsion certificate from the frozen bytes in **both** presentations,
using the printed `A_1..A_4` and `B_rs, B_c0, B_c1, B_qrs`:

```text
substituted:  cs^6*k^2*rho^6 - sum A_i * E_{Tg10_i}                  residual 0 terms
honest S#  :  cs^6*k^2*rho^6 - [ sum A_i*Tg10_i - B_rs*(rs-cs*qrs)
                - B_c0*(c0-cs*qc0) - B_c1*(c1-cs*qc1) - B_qrs*qrs ]  residual 0 terms
```

Both **EXACT**.  So `cs^6*k^2*rho^6 ∈ I` and `∈ K`, verified here from bytes,
not taken from the promotion.

**Step 1** (promoted, read not re-proved): the localized special-fibre ideal
— substituted rows + `qrs` + `rho`, localized at `cs*k` via `1-u*cs, 1-v*k` —
is the unit ideal over `Q`; explicitly "a Nullstellensatz/faithful-flatness
conclusion [that] supplies no explicit cofactors".  Fable's description is
faithful to the promotion text.

**Step 2** (Rabinowitsch clearing): `1 ∈ J·S#[u,v]` with `1-u*cs, 1-v*k ∈ J`
gives `(cs*k)^m ∈ (Ehat) + (qrs) + (rho)` for some `m`.  Valid; `m` not
effective.

**Step 3** (retraction `qrs ↦ 0`): fixes `(cs*k)^m` and maps `Ehat_i ↦ E_i`,
giving `(cs*k)^m ∈ (E) + (rho)`.  Elementary.

### 9.2 The even-part operation is justified, not hand-waved  [CONFIRMED]

Requirements, all checked here:

* **`rho`-parity of the generators.**  Across all 36 rows, **0 monomials have
  an odd `rho` exponent** (exponents occurring: `{0,2,4,6,8}`).  Substitution
  `rs↦0, c0↦cs*qc0, c1↦cs*qc1` introduces no `rho`, so the `E_i` are
  `rho`-even too.  The bilinears and `qrs` are `rho`-free.
* **`cs`, `k` are `rho`-free.**  Immediate.

Then with `sigma : rho ↦ -rho`, from `(cs k)^m = Σ a_i E_i + rho*h`:

```text
apply sigma :  (cs k)^m = Σ sigma(a_i) E_i - rho*sigma(h)
average     :  (cs k)^m = Σ ((a_i+sigma(a_i))/2) E_i + rho*(h - sigma(h))/2
```

and `(h - sigma(h))/2` is the odd part of `h`, divisible by `rho`.  Hence
`(cs k)^m ∈ (E) + (rho^2)`.  The operation uses only `1/2` (fine over `Q`) and
`sigma`-stability of the ideal.  **Not** an unjustified even-part move.

### 9.3 The composition and the exponents  [CONFIRMED]

Torsion-multiplier lemma, restated with `rho^2` in the role of `rho`: if
`f ≡ c*rho^2 (mod K)` and `g*(rho^2)^r ∈ K` then
`g*f^r ≡ c^r*g*rho^{2r} ≡ 0 (mod K)`.  Instantiate `f = (cs*k)^m`,
`g = cs^6*k^2`, `r = 3` (since `rho^6 = (rho^2)^3`):

```text
cs^6*k^2 * (cs*k)^{3m}  =  cs^{3m+6} * k^{3m+2}  ∈  K       (W = 0)
```

Arithmetic verified.  The transfer from `I` to `K` needs only the **easy**
direction of Lemma 0 (`E_i ∈ K`, since `E_f = f - B_rs(rs-cs qrs) - … ∈ K`),
which both certificate reviews reconstructed.  Fable's improvement over the
memo's `r = 6` result `cs^{6m+6}k^{6m+2}` is **CONFIRMED**: same conclusion,
half the exponent inflation.

Presentational note: Fable's §0 row 4 writes the exponents as
`(3N+6, 3M+2)`, suggesting two independent exponents; §5 correctly writes
`(3m+6, 3m+2)` with the single clearing exponent `m` from step 2, because
`f = (cs*k)^m` forces `N = M = m`.  The §5 form is the correct one.

### 9.4 Hidden saturation, false converse, and the control

* **Saturation is used — once, at step 2, and only there.**  Passing from
  "unit ideal in the localization at `cs*k`" to "`(cs*k)^m` in the ideal" is
  exactly the saturation-clearing pattern.  `m` is not effective, so the
  conclusion is **existence-only**: no explicit exponents, no exponent-quality
  claim, no minimality.  Fable states this correctly; the explicit
  `(447, 164)` certificate remains the only effective instance, and the two
  results must not be conflated in the ledger.
* **No false converse is used.**  The corrected false converse would be
  "`cs^a k^b ∈ I + (rho)` ⟹ `cs^a k^b (1 + rho W) ∈ I`".  The chain never
  needs the `rho`-cofactor to be divisible by anything; divisibility is
  *bought* by multiplying with the torsion certificate.  **CONFIRMED.**
* **The control works, and by two independent mechanisms.**  For
  `I = (cs - rho)`: Fable notes the chain dies at step 5, since setting
  `cs = rho` sends `cs^a k^b rho^c` to `cs^{a+c}k^b != 0`, so no monomial
  times a `rho`-power lies in `I`.  **Confirmed** — and there is a *second*
  independent failure Fable does not mention: `cs - rho` has **odd** `rho`
  degree, so `I` is not `sigma`-stable and the parity step 9.2 also fails.
  The refined chain is therefore strictly harder to abuse than the memo's.

**Answer to the prompt's question: YES**, an existence-only honest membership
`cs^{3m+6} k^{3m+2} ∈ K` with `W = 0` follows from the promoted fibre theorem,
Lemma A, the `rho`-parity of the rows, and the byte-verified grade-10 torsion
certificate — with no branch-(b) input and no effective exponent.

---

## 10. Defects found in the Fable report

None of these changes a verdict; all three are inside Fable's own repairs and
would propagate wrong numbers or wrong words into the ledger.

* **D1 (§3.2, arithmetic).**  Fable's stated residual of the memo's incorrect
  `e0e1` formula, "`a0e1ell1 + a1e0ell1`", is wrong by a factor `-2` and omits
  the `V(k)` load term.  The exact residual in both columns is
  `-(1/2)*ell1*[(8/3)Tg11_1|]`, i.e. `-(1/2)(a0e1ell1 + a1e0ell1)` on `V(J1)`
  and that plus `-(5/12)cs^3ell1k1rho^2` on `V(k)`.  §6.
* **D2 (§4.2, notation, inherited from the memo and not flagged).**  "`u = 1`"
  collides with the memo's own `u := c0`, which is `0` at this point.  The
  true reading is the `cs`-Rabinowitsch variable of `1-u*cs`; `u` is not a
  variable of `S#` and `1-u*cs` is not a generator of `K`, so the clause is
  optional.  §2.4.
* **D3 (§2.3, scope).**  The `RS0` half of the `M >= 1` repair is verified
  against the raw-row `T-rs` presentation, but the *promoted* `T-rs`
  instantiation's relation list is "four divided raw source rows" with
  localizer `35*k`.  The transfer is plausible (division by a power of `rs` is
  invisible at `rs=1`) but unchecked.  §5.  The `CS0` half is unaffected and
  fully sufficient for the gate.

Corrections Fable itself owes the ledger — the §3.2 factor-2 cofactor, the
§3.3 "`cs1`-weighted / dies on `qa1=0`" sentence, the reversal of "`M >= 1`
gate unsound", and attaching the §4.4 counter-evaluation to the §4.3 witness
record — are all **independently confirmed here** and are correct as
identified.

---

## 11. Ledger corrections safe to promote now

Safe to promote immediately (each is exact, recomputed from frozen bytes by a
second model, and self-contained):

1. **Reverse the memo's "drop the `M >= 1` gate" decision.**  Keep the gate,
   with provenance "promoted `CS0` section (`959603e3…`) + the four honest
   `T-cs` chart generators", and record that it is fail-safe and that it also
   holds against the 36-row system.  Strike the `deg_2` citation.  (§8)
2. **File the factor-2 correction to the shifted-core `e0e1` cofactor**, in
   *both* the `V(J1)` and `V(k)` columns: the correct combination is
   `(16/3)(Tg12_3-(p/2)Tg12_1)| + (8/3)*ell1*Tg11_1|`.  File the exact
   residual of the superseded form as `-(1/2)*ell1*[(8/3)Tg11_1|]`, **not**
   Fable's `a0e1ell1 + a1e0ell1`.  (§6, D1)
3. **Retire the sentence "`Tg14_5|_{J1}` is `a0a1`-weighted, hence dies on
   `qa1=0`."**  Replace with the exact census: 62 terms, 12 containing `k`,
   `≡ -(5/128)a0a1k rho^4  mod (cs1,cs2,rs1,rs2,e0,e1)`, 6 of the 12 not
   divisible by `cs1`, and 11 of the 12 surviving `a1 = 0`.  Record that
   `A00`/`A10` and the `H3` control now rest on the promoted zero-sections
   result, not on the mechanism sentence.  (§7)
4. **Attach the V20 counter-evaluation to the §4.3 witness record**, so the
   char-0 point is never quoted against the 36-row system: the point kills
   22/22 frozen rows but only 1 of 14 V20 rows.  (§2.2, §3)
5. **Record the exact char-0 point as a theorem about the frozen 22**, with
   the field statement (`A ≅ Q(zeta_8, sqrt15)`, degree 8), the honest-chart
   extension (`qrs=qc0=qc1=0`, `cs*k1*rho = 1`, `k = 0`), and the verified
   `F65521` residue shadow `w ↦ 7669, s ↦ 43638 ⟹ (48966,4891,3387,38806)`.
   Disambiguate `u`: either drop the clause or write "the `cs`-Rabinowitsch
   variable of `1-u*cs`".  (§2, D2)
6. **Record the grade-13 kill identity as exact ideal membership**
   (`27` terms, all in `(k,rs,c0,c1)`, over `Z[1/2]`) and the emptiness
   conclusion as **set-theoretic only**, with the hypothesis table of §4.4
   attached: `qrs = 0` is a chart generator and is load-bearing; `c0 = c1 = 0`
   comes from a **radical** containment (`c0 ∉ (k,Tg10_1..Tg10_4)`, proved by
   the degree-1 argument in §4.2); characteristic exclusions are exactly
   `{2,3,5,7}`.  No certificate and no cofactors follow.  (§4)
7. **Record the parity refinement** `cs^{3m+6} k^{3m+2} ∈ K, W = 0` as
   **existence-only**, with `m` the non-effective clearing exponent of step 2,
   and with the byte-verified grade-10 identity (residual 0 in both
   presentations) as its arithmetic input.  Note both reasons the `(cs-rho)`
   control defeats the chain (no monomial-times-`rho`-power membership; and
   `rho`-odd, so parity fails too).  Use the single-`m` form `(3m+6, 3m+2)`.
   (§9)
8. **Record `RS0` with its charts named**: a `Q[rho]`-section of the raw-row
   `T-rs` presentation killing all 36 rows **termwise** (0 surviving
   monomials), compatible with `cs-rs*qcs, c0-rs*qc0, c1-rs*qc1` at
   `qcs=qc0=qc1=0`, and **explicitly not** a point of the `T-cs` chart
   (`rs-cs*qrs ↦ 1`).  Flag the open one-line check against the promoted
   `T-rs` relation list.  (§5, D3)
9. **Drop the "conditional on unreviewed V20 bytes" qualifier at the byte
   level.**  The V20 export has now had a different-model hostile review
   (`8665e43c…`, CONFIRMED WITH REPAIRS): all fourteen coefficients were
   reproduced byte-for-byte in both characteristics from a clean-room
   re-implementation.  The remaining conditionality is *source provenance*
   (the single upstream Faber emitter), which the frozen 22 share, **not**
   custody of the grade-13/14 bytes.  The five repairs R1–R5 of that review
   still stand and travel with the citation.

Not safe to promote: anything asserting that the grade-13 result yields a
certificate, exponents, or a statement about grades `>= 15`; and the transfer
of `RS0` to the promoted `T-rs` object (item 8's flagged check).

---

## 12. Scope firewall

Everything new here is producer-tier from this lane and needs different-model
review before promotion, **except** where it merely re-verifies an already
promoted object (`CS0` sections, the grade-10 torsion identity, the honest
presentation) — those are re-verifications, not new claims.

All statements about the 22 frozen rows and the 14 V20 rows are statements
about **those frozen bytes**, not about the source ideal, and say nothing
about grades above 14.  They inherit in full the single-emitter literal-source
provenance debt; agreement between Fable's lane and mine bounds transcription
and reasoning error, not source error, since both read the same bytes.

Nothing here establishes or refutes: JC2; Gate T; the `k10=0` sibling fan as a
whole; either `J2` chart; the terminal receiver; chart overlaps; the
deck/square bridge; the generic comparison; literal source universe or
coverage; TD6, SP-2, or the omitted-moduli cover; order two; maximum twelve;
arbitrary-standard-pair landing; `G2-PSC`; any invoked `G2-BD`; any cofinal
degree/type bound; existence or nonexistence of an AS109 lift; or any Lean
statement.

No AWS state was read beyond already-harvested case files, none was mutated,
nothing was launched, `jc2-lean` was not accessed, no web was used, no
Groebner basis or CAS was run.  All scratch under `/tmp/o5v20/`.  The only
repository file written is this one.
