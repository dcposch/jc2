# Hostile review: Gate-T Kummer row bridge (Opus5, different model)

Date: 2026-08-27

Reviewer: Opus5, adversarial, independent derivation.

Producer under review:

```text
1b583d5a58ae3c26edd2f394e85e2540871ccfd996ec0bc798b84235c564361a
  xmodel/max12-812-order2-gate-t-kummer-row-bridge-discriminator-sol-20260827.md

f11b24a3447a0602ef5b55891e156b6f179e62179eb8394fd30f4455adf29af5
  xmodel/max12-812-order2-gate-t-kummer-row-bridge-replay-20260827.py
```

Both producer hashes recomputed locally and **match**.

## 0. Verdict summary

| Claim | Verdict |
|---|---|
| Global finite-flat Kummer descent (§3–§4) | **CONFIRMED** |
| Root-map comparison on `D(2rho)` (§5) | **CONFIRMED as stated; its §6 corollary is REFUTED** |
| Concrete grade-15 actual-total / charged-`D1AC` row equality (§6) | **CONFIRMED, with a material scope and custody repair** |
| Formal grade-16 statement (§6) | **CONFIRMED, and independently strengthened** |
| Claimed strategic narrowing (§0, §6, §8) | **GAP (overreach)** |
| Parity countermodel (§7) | **CONFIRMED but misaimed; a sharper countermodel is supplied** |

The mathematics the producer asserts is, as far as I can check it, **true**.
Every equation I tested held.  What fails is the *characterisation* of that
mathematics: the report describes a rich seven-row comparison and a composed
Kummer/Rees/root-chart/source-map object, and what actually exists is a
two-generator ideal reached by a map that annihilates every coordinate the
root chart is built from.

## 1. What I did, and what the producer's replay does not do

I re-ran the producer replay: it reproduces
`PASS-GATE-T-KUMMER-ROW-BRIDGE-DESK-REPLAY` in 0.06 s, and all six of its
pinned source digests match on disk:

```text
3aa6bbbb…  cases/…_p0_total_rees_t_rs0_discovery_20260826/compile_t_rs0_discovery.py
77f25216…  cases/…_square_load_ladder_20260826/compile_square_load_ladder.py
e024a13d…  cases/…_square_owner_r1_d1_ac_symbolic_20260826/compile_r1_d1_ac.py
c965726d…  cases/…_allrows_g15_export_v22_20260827/export_allrows_g15_v22.py
5c233e0f…  cases/…_allrows_g13_g14_export_v20_20260827/export_allrows_g13_g14_v20.py
d72f774c…  cases/…_compiled_v2/tails.json
```

All five §1 history-search digests also match on disk.

**However, the replay verifies none of the mathematics it pins.**  Reading
`source_map_check()`, `root_coordinate_check()` and
`parity_countermodel_check()`: not one of them reads a byte of any pinned
file.  Both sides of the "universal versus `D1`" comparison are *literals
typed into the replay by the producer*.  The pinned files are touched only by
`sha256` and by six substring greps
(`'p_total = "-2*rho^2+"' in total_text`, `"ROWS = tuple(range(1, 8))"`, …).
The reported `loads_map` and `targets_fixed` are hardcoded dictionaries never
compared to anything; the reported `loads_map` key is even wrong (`"k"`,
where the `D1AC` compiler's dictionary key is `"k10"`).

So the producer replay is a **self-consistency check of the report's own
transcription** plus hash custody plus a tail census.  It is not evidence that
the transcription matches the frozen compilers.  Supplying that evidence is
the bulk of this review.

I therefore did the following independently, with my own polynomial and
truncated-series arithmetic, importing no campaign module:

1. read `compile_r1_d1_ac.py`, `compile_square_load_ladder.py`,
   `compile_cge3_universal.py`, `export_allrows_g13_g14_v20.py`,
   `export_allrows_g15_v22.py`, and `compile_t_rs0_discovery.py` line by line;
2. reconstructed all seven **frozen actual-total grade-15 rows** from the
   569-tail JSON and the source series, and compared against the frozen
   `.poly` bytes;
3. reconstructed the `D1AC` branch from `d1_section`'s exact arguments;
4. checked `delta_D1([sigma^g]Phi_ell^total) = [sigma^g]Phi_ell^D1` at
   **every** grade `0..16`, not only at 15;
5. ran mutation controls on every clause of the (6.1) table to find which
   clauses the frozen comparison can actually detect.

The consolidated verifier is `e388fdcc881e7f40a812c9e48a41967135f1d1953a82885b3090d048f26c65cb`
(203 s, desk-scale, pure Python `Fraction`); it is reproduced in Appendix A.
No AWS, no CAS, no web, no ledger edit, no `jc2-lean` access.

## 2. Attack 1 — the Kummer map, Rees algebras, charts, saturation

### 2.1 What checks out

`B = k[p0,rho]/(p0+2*rho^2)`.  Division by the monic `rho^2+p0/2` gives the
normal form `b0(p0)+rho*b1(p0)`, so `B` is **free of rank two** over `k[p0]`
with basis `{1,rho}`; equivalently `k[rho] = k[rho^2] ⊕ rho*k[rho^2]` and
`k[rho^2] ≅ k[p0]`.  A nonzero free module is faithfully flat.  **Correct.**

Étale exactly on `D(p0)`: `kappa^{-1}(D(p0)) = D(rho^2) = D(rho)`, and the
different `2*rho` is a unit there.  At `p0=rho=0` the map is ramified but
still finite flat.  The report's warning that étaleness must not be
substituted for flatness at that fibre is **correct and load-bearing**.

Base change of `A_p,G` along `kappa` is flat, so:

- `J^n ⊗ B → A ⊗ B` stays injective with image `(J_B)^n`, hence
  `Rees_A(J) ⊗ B ≅ Rees_{A_B}(J_B)` as graded rings, degree by degree — (4.3)
  is **correct**;
- `Proj` of a Rees algebra base-changes accordingly, and the standard chart at
  `f` is the degree-zero part of `Rees(J)_f`, i.e. `A[J/f]`;
- `(4.4)`'s presentation `A[y_j]/((f*y_j - f_j) : f^infinity)` is the correct
  model of `A[J/f]` (the kernel of `A[y] → A_f` is exactly that saturation),
  so `beta_(m,f)` is an isomorphism.  **Correct.**
- ordered-stratum equations are ordinary quotients, and quotients commute with
  any base change.  **Correct.**

### 2.2 Omitted hypotheses — checked, and none is needed

The report never states a noetherian hypothesis.  I checked whether one is
required: it is not.  `(I : f^n) = ker(A/I --f^n--> A/I)`, flat base change
commutes with kernels, and `(I : f^infinity)` is the filtered colimit of the
`(I : f^n)`, which `⊗ B` also commutes with.  So (4.4)–(4.5) hold without
noetherian hypotheses.  The hypothesis holds anyway: `U_G` is a finitely
generated `k`-algebra since §2 fixes finite jet ranges.  **No gap.**

I found no omitted chart equation.  The named list (4.6) — four `J1` charts,
two `J2` charts after quotient by `J1`, and the separately named terminal
receiver — is complete for the staged tree recorded in `AUDIT.md`.

### 2.3 Two presentational slips (harmless)

- §2 leaves `sigma` a free polynomial variable in `U_G`, yet no generator of
  `I_G` involves `sigma` (they are `sigma`-coefficients).  `A_p,G` therefore
  carries a spurious free variable.  Nothing downstream uses it.
- (2.1) writes `p(sigma) = p0 + 2*sum_(i>=1) sigma^i*ell_i` as an infinite
  sum in a ring §2 declares finite.  Truncation is meant and is what the
  frozen emitters do.

### 2.4 One custody observation the report does not make

`U_G` in §2 is a `k[p0]`-algebra with `p0` free, and §3 base-changes it.  But
**both** frozen total emitters hard-code the Kummer substitution:
`compile_t_rs0_discovery.py:140` has
`p_total = "-2*rho^2+" + …`, and `export_allrows_g15_v22.py` sets
`p[0] = -2*rho*rho`.  There is **no frozen artifact working over `k[p0]` with
`p0` free.**  The "universal unsplit total emitter" exists only as (2.1)–(2.2)
inside the report.  This is repairable and I repair it in §4.3, but §0's
phrase "the universal unsplit total emitter specializes exactly to the frozen
`D1AC` emitter" reads as if a frozen unsplit emitter were being cited.

**Verdict, global finite-flat descent: CONFIRMED.**

## 3. Attack 2 — the three root matrices

Checked by hand and by exact arithmetic:

```text
(rs,cs): [[1/4, rho],[1/4,-rho]]      det = -rho/4 - rho/4 = -rho/2
(c0,c1): [[1/2, rho/2],[1/2,-rho/2]]  det = -rho/4 - rho/4 = -rho/2
(a0,a1): [[1, rho],[1,-rho]]          det = -rho   - rho   = -2rho
```

matching (5.3).  The inverses (5.2) are correct:
`Rplus+Rminus = rs/2`, `Rplus-Rminus = 2*rho*cs`;
`Cplus+Cminus = c0`, `Cplus-Cminus = rho*c1`;
`Aplus+Aminus = 2*a0`, `Aplus-Aminus = 2*rho*a1`.
`tau(rho)=-rho` swaps each `plus/minus` pair.  In characteristic zero
`D(2rho) = D(rho)`, so the "2" is cosmetic; the report does not lean on it.

Nothing is silently extended to `rho=0`: §5 explicitly says (5.2) is
unavailable there, and the report does not use a root chart on the ramified
fibre.  **Correct, and correctly fenced.**

### 3.1 But the §6 corollary is false for the only instantiated client

§6 states, after adjoining `D_16^spl` and identifying `rho=lambda`:

> Equations (5.1)–(5.3) then give both root orientations and their deck swap.
> This is the exact source-level composition available to any already reviewed
> `D1AC` endpoint …

I computed the images of the six coordinates that (5.1) is built from:

```text
delta_D1(rs) = 0    delta_D1(cs) = 0
delta_D1(c0) = 0    delta_D1(c1) = 0
delta_D1(a0) = 0    delta_D1(a1) = 0
```

Every generator of `J1 = (rs,cs,c0,c1)` and of `J2 = (a0,a1)` is annihilated
by the source map.  Therefore

```text
Rplus = Rminus = Cplus = Cminus = Aplus = Aminus = 0
```

identically in `D_16^spl`.  The advertised composition of §3–§5 with §6 is the
**zero map on all six root coordinates**, and the deck swap it "gives" acts on
the zero ideal.

What the `D1AC` compiler actually does is different.  In
`compile_r1_d1_ac.py`, `D1AC_or15`/`D1AC_sw15` substitute

```text
p -> -2*lam^2 ;  a1 -> au , a0 -> -/+ au*lam ;  c1 -> cv , c0 -> +/- cv*lam
```

on **its own** `a0,a1,c0,c1`, which by (6.1) are the images of the total
emitter's *third* jets `aaa0, aaa1, ez3/2, ec3/2` divided by `theta` — not the
leading jets that (5.1) names.  The `plus/minus` shape is genuinely reused,
one contact level deeper.  That deeper root structure is a **separate,
unproved-here** statement: nothing in §3–§5 establishes that the deck
involution acts on `aaa0, aaa1, ez3, ec3` the way it acts on `a0,a1,c0,c1`.

This is the report's central overreach, and it is precisely the object §1
advertises as new ("no located artifact composes the global finite-flat
Kummer map, the two staged Rees ideals, the root-coordinate matrices, and an
exact frozen source map").  The composition exists; it is trivial.

**Verdict, root-map comparison: CONFIRMED as stated in §5.  The §6 corollary
that (5.1)–(5.3) supply the `D1AC` root orientations is REFUTED.**

## 4. Attack 3 — independent reconstruction of `delta_D1` and the rows

### 4.1 The seven frozen actual-total grade-15 rows reproduce exactly

I rebuilt the source series from the mathematics — `p = -2rho^2 + 2*sum
sigma^i ell_i`, `c = sigma^2*Cseries`, `r = (p^2 + sigma^2*Rseries)/4`,
`n3 = sigma^3*Az`, `n2 = sigma^3*Ac`, `n1 = sigma^3*(p*Az+Ez)/2`,
`n0 = sigma^3*(p*Ac+Ec)/2`, then (2.2) — and summed the 569 tail monomials
with load shifts `sigma^4, sigma^12, sigma^20` for `k10, k6, k2`.  Against
the frozen bytes in
`cases/…_allrows_g15_export_v22_20260827/aws_q_r1/compiled/Tg15_*_q.poly`:

```text
row 1  133 terms   MATCH        row 5  585 terms   MATCH
row 2  224 terms   MATCH        row 6  200 terms   MATCH
row 3  355 terms   MATCH        row 7  759 terms   MATCH
row 4  140 terms   MATCH        ----------------------------
                                total 2396 terms   ALL MATCH
```

So the report's (2.1)–(2.2) are a faithful description of the frozen
actual-total emitter, and the frozen rows are what they claim to be.  This is
a genuine positive result and it is stronger than anything the producer replay
establishes.

The tail census also independently reproduces: `36+54+58+81+89+120+131 = 569`,
every monomial of length 10, weight `12+ell` under `[8,7,6,5,4,3,2,2,6,10]`,
loads linear.

### 4.2 Index and load conventions agree across the two branches

`term_text` in `compile_square_load_ladder.py` uses
`NAMES = [a0..a6,k10,k6,k2]`, `WEIGHTS = [8-i]+[2,6,10]`, applies `coeffs[i]`
at monomial position `i`, and appends `Lambda^(sum LOAD_WEIGHTS)`.
`build_row` in V20/V22 uses `coefficients[index]` at the same positions with
the same weights and load shifts `2*w`.  With `Lambda = sigma^2` these are the
same convention.  **No transposition; no load-weight mismatch.**

### 4.3 The `rho`-parity step the report omits, and why it rescues `D_16`

`delta_D1` as defined in (6.1) has source `U_16` with `p0` free.  The frozen
rows live in the `rho`-substituted ring.  To compare them you must invert
`kappa`, and that is possible only on `rho`-even elements.

I checked: **every term of all seven frozen grade-15 rows has even `rho`
exponent** (max exponent 8, zero odd terms).  This is not an accident —
`export_allrows_g15_v22.py` fail-closes on it:

```python
if any(exponent % 2 for monomial in polynomial for name, exponent in monomial
       if name == "rho"):
    fail(("rho parity", row))
```

Because `kappa` is injective and `{1,rho}` is a basis, the `rho`-even part is
exactly the image of `k[p0]`, so `rho^(2j) -> (-p/2)^j` is well defined and
unique.  Hence the comparison lands in `D_16` and **does not** need the
splitting `D_16^spl` of (6.5).

The report asserts "their grade-15 raw row ideals are equal in `D_16`" without
ever mentioning `rho`-parity.  The conclusion is right; the justification is
missing.  Supplying it is a one-line repair.

### 4.4 Functoriality holds — at every grade, not just 15

I built the `D1AC` branch from `d1_section`'s literal arguments

```text
pp = (p+2*sigma*ell1)          rz = (sigma^2*theta*eta*b1)
az = (sigma^2*theta*(a1+sigma*aa1))    rc = (sigma^2*theta*eta*b0)
ac = (sigma^2*theta*(a0+sigma*aa0))
cz = (sigma^3*theta*(c1+sigma*cc1))
cc = (sigma^3*theta*(c0+sigma*cc0))
```

through `source_coefficients`, and checked

```text
delta_D1([sigma^g]Phi_ell^total) = [sigma^g]Phi_ell^D1
```

for all `ell = 1..7` and **all `g = 0..16`**: true in every case.  I also
confirm the factors `4` and `2` are the correct conventions, exactly as
(6.2) states.

I additionally confirm, independently, the `D1AC` compiler's
`SOURCE_DIVISIBLE` claim: every `D1AC` row is divisible by `sigma^15` — no
row has a nonzero coefficient at any grade below 15.

### 4.5 The deflation the report does not report

This is the finding that most changes how the result should be read.
`delta_D1` is a deep contact specialization.  Its images:

```text
                 total row      charged D1AC row
row 1   g15:     133 terms  ->   2 terms
row 2   g15:     224 terms  ->   2 terms
row 3   g15:     355 terms  ->   2 terms
row 4   g15:     140 terms  ->   0 terms   (identically zero)
row 5   g15:     585 terms  ->   2 terms
row 6   g15:     200 terms  ->   0 terms   (identically zero)
row 7   g15:     759 terms  ->   2 terms
        ------------------------------------------------
                2396 terms  ->  10 terms
```

and the ten terms are not independent.  Writing
`g1 = (3/4)*theta^2*(a0^D*c1^D + a1^D*c0^D)` and
`g2 = (3/8)*theta^2*(2*a0^D*c0^D - p*a1^D*c1^D)`:

```text
row1 = g1        row3 = -(p/4)*g1     row5 = -(p^2/32)*g1   row7 = -(p^3/128)*g1
row2 = g2        row4 = 0             row6 = 0
```

**The entire grade-15 raw row ideal in `D_16` is `(g1, g2)` — two binomials.**
Only six symbols occur in it: `a0^D, a1^D, c0^D, c1^D, p, theta`.  Absent
altogether: `b0, b1, eta, k0, ell1, aa0^D, aa1^D, cc0^D, cc1^D`.

The `g1` coefficient is hand-checkable.  Row 1's tail has exactly two
`F`-degree-two loadless monomials, `F1*F2` and `F0*F3`, both with coefficient
`3/4`.  `sigma^2*n2` carries `aaa0` at `sigma^7` and `sigma^2*n1` carries
`ez3/2` at `sigma^8`, so `F1*F2` contributes `theta^2*a0^D*c1^D` at
`sigma^15`; symmetrically `F0*F3` contributes `theta^2*a1^D*c0^D`.  Every one
of the other 34 tail monomials of row 1 contributes zero (machine-checked).

The report's §0 ("all seven coefficient primitives, all three loads, all four
targets, and the canonical 569-tail polynomial are the same … a concrete
equality for all seven frozen actual-total grade-15 rows") is literally true
and materially misleading.  Two of the seven equalities are `0 = 0`; three
more are `p`-multiples of a fourth.  A reader budgeting downstream work from
§0 would badly overestimate what has been transferred.

Related: at grade 15 the four targets `mu2,mu4,mu6,J` enter only at
`sigma^(2*(12+ell)) >= sigma^28`, and the `k2` load only at `sigma^20`.  The
"all four targets … are the same" clause is **vacuous at the only grade with
frozen custody**.  The `k6` load, which could reach grade 15, cancels
identically — consistent with the `D1AC` compiler's own `forbidden` gate.

### 4.6 What the frozen comparison can actually detect

I mutated each clause of (6.1) and asked which rows change.

```text
clause                          detectable at g15   detectable at g16
------------------------------------------------------------------------
rs2 -> 4*theta*eta*b0  (factor 4)      NO           yes (rows 1,2,3,5,7)
ez/ec factor 2                         yes          yes
moving term 2*sigma*ell1               NO           yes (rows 2,3,5,7)
cs1 -> 0, rs1 -> 0                     yes          yes
aa0,aa1,e0,e1,ee0,ee1 -> 0             yes          yes
k1, k2c, k10_3..5, k6_1 -> 0           NO           NO
cs3, rs3, az4, ac4, ez5, ec5 -> 0      NO           NO
ell2, ell3 -> 0                        NO           NO
```

Two of the three negative controls the producer names in §8 item 6 — the
factor `4` and the moving term `2*sigma*ell1` — are **invisible at grade 15**,
the only grade with a frozen actual-total artifact.  The producer's replay
"detects" them, but only by comparing two of its own hand-written expressions
at the level of the `F`-primitives, with no frozen custody at all.  §6's "The
factors `4` and `2` are load-bearing" is half right: the `2` bears load at
grade 15, the `4` does not bear any until grade 16.

There is also a live naming trap here, of exactly the `k`/`k0`/`k10` kind this
campaign has hit before.  The frozen `k10` jet series is
`["k","k1","k2c","k10_3",…]`.  The third jet is named **`k2c`**, which looks
like a `k2` jet but is not.  (6.1) says only "`k10_i (i>=1) -> 0`" and never
names `k1` or `k2c`; §2's jet list (`k10_i; k6_i; k2_i`) does not match the
frozen names either.  A reader implementing (6.1) by name could send
`k2c -> k2load` and corrupt the map — and, as the table shows, **neither
grade 15 nor grade 16 would notice**.

### 4.7 Custody defects in the grade-15 pin

Three, in increasing severity.

1. **"Both source branches call the same frozen `tail_text` function
   `77f25216…`" is false for the total branch.**  `D1AC` does call it
   (`compile_r1_d1_ac.py` → `compile_cge3_universal.load_base()` →
   `compile_square_load_ladder.py`, pinned `77f25216…`).  V20/V22 do **not**:
   they use their own `build_row`, loaded from
   `cases/…_p0_odd_grade14_unit_replay_20260826/replay_row5_grade14.py`.  Two
   different implementations.  Their semantic agreement is true — I verified
   it in §4.2 — but it is an extra obligation the report discharges by a false
   statement of identity rather than by argument.

2. **The pinned V22 exporter produced nothing.**  §6 pins
   `export_allrows_g15_v22.py` (`c965726d…`) and says "It … builds all seven
   actual-total grade-15 rows."  The case's own
   `V22_V1_SERIALIZATION_BRIDGE_ERRATUM.md` records that **both** V1 jobs
   "failed closed before exporting or accepting any grade-15 polynomial,"
   failing at a premature polynomial-*text* comparison.  The rows in
   `aws_q_r1/compiled/` were produced by `export_allrows_g15_v22r1.py`
   (`d9f23a279b39b45ca27717a00493a6e928d1042007bc2c3c183eb2d239882768`), which
   imports V1, pins its hash, and defers only that text gate.  The V1 file is
   the right *mathematical* pin; it is the wrong *custody* pin.

3. **Neither the report nor the replay pins the seven `.poly` files.**  The
   objects the theorem is about — `Tg15_1_q.poly … Tg15_7_q.poly` — have no
   digest anywhere in either artifact, nor does the R1 wrapper, nor
   `aws_q_r1/RESULT.json`.  The chain from a pinned file to a frozen row is
   not closed.  My §4.1 reconstruction closes it by content instead.

**Verdict, concrete grade-15 row equality: CONFIRMED.**  The identity is true;
I reproduced both sides independently.  It is CONFIRMED *with* the repairs in
§4.3 (state `rho`-parity), §4.5 (state the deflation), §4.6 (state what the
controls cannot see), and §4.7 (fix the custody statements).

## 5. Attack 3b — the formal grade-16 statement

The report's discipline here is **correct and should be preserved**: the
polynomial identity does cover grade 16, and there is no frozen actual-total
grade-16 export, so it must not be called an actual-total artifact comparison.
I searched and confirm none exists; V22 stops at `NEW_GRADE = 15`.

I went further and checked grade 16 computationally.  The charged `D1AC`
grade-16 rows have `8, 10, 11, 2, 11, 0, 11` terms, and they equal
`delta_D1` of the grade-16 total rows (`199, 357, 583, 255, 1043, 399, 1459`
terms) exactly.

Two caveats on my own grade-16 evidence, stated so it is not over-read:

- my grade-16 total rows are **derived here**, not frozen.  They require one
  more jet in each family than V22 carries (`ell16`, `cs14`, `rs14`, `az11`,
  `ac11`, `ez11`, `ec11`, `k10_12`, `k6_4`);
- but the *image* is insensitive to that extension, because `delta_D1` sends
  every one of those new jets to zero.  So the charged grade-16 rows are
  canonical, and the identity does not depend on my truncation choice.

Grade 16 is also where the interface first acquires content beyond the `a/c`
pair: `b0, b1, eta, k0` appear there (e.g. row 1 gains
`(5/8)*b0*c1^D*eta*k0*theta^2` and `(15/16)*b0^2*b1*eta^3*k0*theta^3`), and it
is the first grade at which the factor `4` and the moving term are testable.
**If a grade-16 actual-total export is ever frozen, it is worth roughly an
order of magnitude more than the grade-15 one.**  That is the single most
useful forward recommendation in this review.

**Verdict, formal grade-16 statement: CONFIRMED, correctly hedged, and
independently strengthened to a derived-here exact check.**

## 6. Attack 4 — the parity countermodel

§7 takes `E=k[p0,x]`, `I=(x)`, `J=(x+p0)`, pulls back to `(x)` and
`(x-2*rho^2)` in `k[rho,x]`, notes both are `tau`-stable and that the second
generator has residue `-2*rho^2 != 0` mod the first.  Arithmetically
**correct**; the replay's check is correct.

But it is misaimed, and nearly vacuous: `I` and `J` are already ideals of the
*base*, so their pullbacks are `tau`-stable for trivial reasons, and any two
distinct base ideals would serve.  It establishes only "distinct ideals can
both be deck-invariant."

The statement actually at issue for a ramified Kummer cover is the converse:
does `tau`-invariance make an ideal *descend*?  That is what an averaging or
Reynolds argument would need, and it is **false at exactly the fibre the
report cares about**.  Sharper countermodel, which I offer as a replacement:

> Let `I = (rho) ⊂ B = k[rho]`.  Then `tau(I) = (-rho) = I`, so `I` is
> deck-invariant.  But `I` is not extended from `k[p0]`.  Indeed
> `I ∩ k[rho^2] = (rho^2) = (p0)`, so any `I_0 ⊆ k[p0]` with `I_0*B = I`
> satisfies `I_0 ⊆ (p0)`, whence `I_0*B ⊆ (rho^2) ⊊ (rho)`.  Contradiction.

This is one line, it is about the ramified fibre rather than about the generic
locus, and it kills the averaging strategy properly.  The report's conclusion —
"deck invariance alone is insufficient; literal source/presentation equality
such as (6.4) is necessary" — survives, on stronger grounds.

**Verdict, parity countermodel: CONFIRMED as arithmetic; the argument should
be replaced by the `(rho)` example, which proves the stronger and relevant
fact.**

## 7. Attack 5 — downstream scope audit

### 7.1 Where the bridge actually lands

Because `delta_D1` annihilates `J1 + J2` (§3.1), it factors through
`U_16/(J1+J2)` and induces

```text
U_16/(I_16 + J1 + J2)  ->  D_16/I_16^{D1},
```

equivalently a morphism of schemes

```text
Spec(D_16 / I^{D1}_16)  ->  Spec of the total *terminal receiver* raw-row scheme.
```

So the bridge is supported on the **terminal receiver** — and on none of the
six blowup charts.  Each standard chart `C_(m,f)` inverts `f`, and
`delta_D1(f) = 0` for every `f` in (4.6).  The source map does not extend to
any of the four `J1` charts or either `J2` chart.

Cross-checking `AUDIT.md`: the `T-cs` promotion records that "all four ordered
`J1` chart strata are now closed" on `D(k)`, with "arcs on `V(J1)` still route
to the two `J2` stages and the terminal receiver."  So the bridge lands on a
live obligation — good — but it lands on the one place where the §5 root chart
degenerates, which is why the composition collapses.

### 7.2 Which endpoints can consume the grade-15 equality

Reading `extraction`, `analytic_extract`, `row_checks` in
`compile_r1_d1_ac.py`, the `D1AC` endpoint's fatal product is

```text
divisible * identities * forbidden * analyticDiv * row15 * row16
          * scale15 * scale16 * rec15 * rec16 * orient * residue
```

- **Can consume it:** `D1AC_divisible` (`sigma^15` divisibility of the raw
  rows — which I independently verified), `D1AC_forbidden` (no
  `k6, k2load, mu2, mu4, mu6, J` in the extracted rows), and the raw-row half
  of `D1AC_row15` (`g15_i` compared to a transform of the analytic `h15_j`).
- **Cannot consume it:** `analyticDiv`, `scale15/16`, `rec15/16`, `orient`,
  `residue`.  These are statements about `universal_hshift`, a separately
  hand-written analytic expression that the total emitter does not produce at
  all.  The report says as much ("downstream analytic auxiliary relations must
  retain their reviewed provenance") and that fencing is **correct**.
- Note that `row15` for `i = 4` and `i = 6` now reduces to "the predicted
  transform of the analytic `h` vanishes," since those raw rows are zero.  That
  is still a real check, but it is a check on the analytic side, not a transfer
  from the total side.

### 7.3 Remaining source/presentation and auxiliary debt

1. The deeper root/deck structure on `(aaa0, aaa1, ez3, ec3)` — used by
   `D1AC_or15/sw15` — is not established anywhere in this report (§3.1).
2. `V20/V22`'s `build_row` versus `tail_text`: semantic agreement verified here
   by reading, not proved in the report (§4.7.1).
3. Custody chain from a pinned file to the seven `.poly` rows is open
   (§4.7.2–3).
4. The `k10`-jet clauses of (6.1) are untested at both grades and carry a live
   naming trap (§4.6).
5. Every other charged generic-square client still needs its own source map;
   §8's "next finite manifest" correctly says so.
6. No `k[p0]`-free frozen emitter exists (§2.4); the unsplit universal object
   is a report-level reconstruction legitimised by `rho`-parity.

### 7.4 Why everything global remains open

The report's §9 firewall is accurate and I do not weaken it.  Concretely:

- **ramified fibre `rho=0`:** untouched.  §3–§4 preserve its Rees geometry;
  §5 gives no chart there; §6's client sits on the terminal receiver but says
  nothing about `rho=0` — indeed the grade-15 ideal `(g1,g2)` has no `rho`
  at all after un-substitution.
- **`G2-PSC` / `G2-BD`:** as `ladder/REDUCTION.md` §7.1 records, these are
  disjoint obligations with no implication in either direction; nothing here
  is a GGV-to-Sigray transport or a bounded-delay statement.
- **Gate T:** needs the four `J1` charts, two `J2` charts and terminal
  receiver over `rho=0`.  This closes none of them.
- **order two / maximum twelve / JC2:** the family here is post-`M=0`,
  unit-`k10`, and §9's third bullet correctly denies that every order-two
  source, let alone every Keller pair, enters it.

### 7.5 Verdict on strategic narrowing

The report claims (§8) that the discriminator is completed, that the exact
source interface should be banked, and that AWS time should not be spent
re-checking functorial substitution.  Banking the identity is right.  But as a
*narrowing* claim it overreaches:

- the transferable grade-15 content is two binomials in six symbols, not seven
  rows;
- it cannot reach any of the six charts, only the terminal receiver;
- the composition that §1 calls the novel content is identically zero;
- and the advice to stop is aimed at the wrong grade: grade 15 cannot see the
  factor `4`, the moving term, or any `k10` jet, while grade 16 — which has no
  frozen custody — can see the first two.

**Verdict, claimed strategic narrowing: GAP (overreach).**

## 8. Strongest exact bridge preserved, and the smallest repair

### 8.1 What survives verbatim

> **Bridge (verified).**  Let `delta_D1` be the (6.1) table, extended by
> `rho^(2j) -> (-p/2)^j` — well defined because every frozen actual-total
> grade-15 row is `rho`-even, a property `export_allrows_g15_v22.py`
> fail-closes on.  Then for every `ell in {1,…,7}` and every `g <= 16`,
>
> ```text
> delta_D1( [sigma^g] Phi_ell^total )  =  [sigma^g] Phi_ell^{D1AC}   in D_16.
> ```
>
> `delta_D1` annihilates `J1 + J2`, so it induces
> `U_16/(I_16+J1+J2) -> D_16/I^{D1}_16`.  At `g = 15` the left side has frozen
> custody, and the image ideal is exactly `(g1, g2)` with
> `g1 = theta^2*(a0^D*c1^D + a1^D*c0^D)` and
> `g2 = theta^2*(2*a0^D*c0^D - p*a1^D*c1^D)`; rows 4 and 6 map to zero and
> rows 3, 5, 7 to `-(p/4)`, `-(p^2/32)`, `-(p^3/128)` times `g1`.
> Consequently: **if the total terminal-receiver raw-row scheme were empty,
> the charged `D1AC` raw-row scheme would be empty.**  Nothing follows in the
> other direction, and nothing follows for any `J1` or `J2` chart.

### 8.2 The smallest repair to the producer document

Four edits; no computation changes.

1. **§6, delete** "Equations (5.1)–(5.3) then give both root orientations and
   their deck swap.  This is the exact source-level composition available to
   any already reviewed `D1AC` endpoint …".  **Replace with:** "`delta_D1`
   annihilates `J1+J2`, hence all six root coordinates of (5.1).  The `D1AC`
   compiler's own orientations apply the same 2×2 shape one contact level
   deeper, to `(aaa0, aaa1, ez3/2, ec3/2)`; that compatibility is not proved
   here."
2. **§6, insert before the `D_16` ideal claim:** "Every frozen actual-total
   grade-15 row is `rho`-even (the V22 exporter fail-closes otherwise), so
   `rho^2 -> -p/2` is well defined and the comparison lands in `D_16`."
3. **§6, replace** "Both source branches call the same frozen `tail_text`
   function" **with** "The `D1AC` branch calls the frozen `tail_text`
   (`77f25216…`); the total branch uses `build_row` in the V20/V22 exporters.
   The two implementations agree on index and load conventions
   (`coeffs[i]` at position `i`, weight `8-i`; `Lambda^w = sigma^(2w)`)."  And
   re-pin custody to `export_allrows_g15_v22r1.py`
   (`d9f23a27…`) plus the seven `Tg15_*_q.poly` digests, noting that the V1
   file failed closed.
4. **§0 and §8, add the deflation:** "Two of the seven grade-15 equalities are
   `0 = 0`, three more are `p`-multiples of a fourth, and the grade-15 image
   ideal has two generators in six symbols.  The factor `4` and the moving
   term `2*sigma*ell1` are undetectable at grade 15; the `k10`-jet clauses are
   undetectable at grades 15 and 16."

With these four edits the document is accurate and I would not object to it.

## 9. `AUDIT.md` promotion eligibility

**Eligible, as one narrow filing, after repairs 1–4:** the exact `delta_D1`
identity at all grades `<= 16`, the `sigma^15` divisibility of the charged
rows, the `rho`-parity un-substitution, the two-generator structure of the
grade-15 image, and the terminal-receiver scope statement of §8.1.  It is
independently reconstructed on both sides here, it is desk-replayable, and no
existing `AUDIT.md` entry covers it (I searched `Kummer`, `deck/square`,
`deck-equivariant`, `root-value`; the `Kummer` hits at lines 1641, 1769, 1923
are the unrelated Kummer-order/leaf topic).

**Not eligible:** §0's and §6's headline phrasing as written; the §1 novelty
claim about the composed Kummer/Rees/root/source object; anything asserting
root orientations for the `D1AC` endpoint.

**Eligible but of low value:** §3–§4 as a standalone lemma.  It is correct and
correctly fenced, but it is textbook flat base change; it is better filed as a
scope note ("the Kummer extension is a red herring; the obstruction is the
root chart, not the base ring") than as a promotion.

**Not promotable in any form:** any grade-16 statement as an actual-total
comparison, until a grade-16 exporter is frozen.  My §5 check is derived-here
evidence and must be labelled as such.

## 10. Execution record

Desk-scale only.  No AWS launch, no heavy local CAS, no web sweep, no
canonical-ledger edit, no access of any kind to `jc2-lean`.  Only this file was
written; no other campaign artifact was touched.

```text
producer report      1b583d5a…  hash verified
producer replay      f11b24a3…  hash verified, re-run, PASS in 0.06 s
6 replay pins                   all verified on disk
5 history pins                  all verified on disk
reviewer verifier    e388fdcc881e7f40a812c9e48a41967135f1d1953a82885b3090d048f26c65cb
                                203 s, pure-Python exact Fraction arithmetic
```

## Appendix A — reviewer verifier

Run from the repository root; imports no campaign module.

```python
#!/usr/bin/env python3
"""Opus5 hostile independent verifier for the Gate-T Kummer row bridge."""
import json, re
from fractions import Fraction
from pathlib import Path

MAXDEG = 16; N = MAXDEG + 1
ROOT = Path(".")
TAILS = ROOT/"cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
FROZEN = ROOT/"cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/aws_q_r1/compiled"

def pzero(): return {}
def pconst(c):
    c=Fraction(c); return {(): c} if c else {}
def pvar(n): return {((n,1),): Fraction(1)}
def padd(*ps):
    o={}
    for p in ps:
        for m,c in p.items():
            v=o.get(m,Fraction(0))+c
            if v: o[m]=v
            elif m in o: del o[m]
    return o
def pscale(s,p):
    s=Fraction(s); return {} if not s else {m:c*s for m,c in p.items()}
def pmul(a,b):
    o={}
    for ma,ca in a.items():
        for mb,cb in b.items():
            d=dict(ma)
            for n,e in mb: d[n]=d.get(n,0)+e
            m=tuple(sorted(d.items())); v=o.get(m,Fraction(0))+ca*cb
            if v: o[m]=v
            elif m in o: del o[m]
    return o
def ppow(p,e):
    o=pconst(1); b=p
    while e:
        if e&1: o=pmul(o,b)
        e>>=1
        if e: b=pmul(b,b)
    return o
def szero(): return [pzero() for _ in range(N)]
def sadd(*ss): return [padd(*[s[i] for s in ss]) for i in range(N)]
def sscale(c,s): return [pscale(c,x) for x in s]
def smul(a,b):
    o=szero()
    for i in range(N):
        if not a[i]: continue
        for j in range(N-i):
            if b[j]: o[i+j]=padd(o[i+j],pmul(a[i],b[j]))
    return o
def sshift(s,k): return ([pzero()]*k+s[:N-k]) if k else list(s)
def spow(s,e):
    o=szero(); o[0]=pconst(1); b=s
    while e:
        if e&1: o=smul(o,b)
        e>>=1
        if e: b=smul(b,b)
    return o
def named(ns):
    s=szero()
    for i,n in enumerate(ns):
        if i<N: s[i]=pvar(n)
    return s
def sig(k,poly):
    s=szero()
    if k<N: s[k]=poly
    return s
def F_from(p,c,r,n3,n2,n1,n0):
    return {6:sscale(2,p), 5:sscale(2,c), 4:sadd(smul(p,p),sscale(2,r)),
            3:sadd(sscale(2,smul(p,c)),sshift(n3,2)),
            2:sadd(smul(c,c),sscale(2,smul(p,r)),sshift(n2,2)),
            1:sadd(sscale(2,smul(c,r)),sshift(n1,2)),
            0:sadd(smul(r,r),sshift(n0,2))}

# TOTAL branch: report (2.1)-(2.2) with p0 = -2 rho^2
p=szero(); p[0]=pscale(-2,pmul(pvar("rho"),pvar("rho")))
for d in range(1,17):
    if d<N: p[d]=pscale(2,pvar(f"ell{d}"))
c=sshift(named(["cs"]+[f"cs{i}" for i in range(1,15)]),2)
r=sscale(Fraction(1,4),sadd(smul(p,p),sshift(named(["rs"]+[f"rs{i}" for i in range(1,15)]),2)))
az=named(["a1","aa1","aaa1"]+[f"az{i}" for i in range(3,12)])
ac=named(["a0","aa0","aaa0"]+[f"ac{i}" for i in range(3,12)])
ez=named(["c1","e1","ee1"]  +[f"ez{i}" for i in range(3,12)])
ec=named(["c0","e0","ee0"]  +[f"ec{i}" for i in range(3,12)])
FT=F_from(p,c,r,sshift(az,3),sshift(ac,3),
          sshift(sscale(Fraction(1,2),sadd(smul(p,az),ez)),3),
          sshift(sscale(Fraction(1,2),sadd(smul(p,ac),ec)),3))
LT={7:sshift(named(["k","k1","k2c"]+[f"k10_{i}" for i in range(3,13)]),4),
    8:sshift(named(["k6","k6_1","k6_2","k6_3","k6_4"]),12),
    9:sshift(named(["k2"]),20)}

# D1AC branch: literal d1_section arguments
pp=szero(); pp[0]=pvar("p"); pp[1]=pscale(2,pvar("ell1"))
th,et=pvar("theta"),pvar("eta")
azd=sadd(sig(2,pmul(th,pvar("a1_D"))),sig(3,pmul(th,pvar("aa1_D"))))
acd=sadd(sig(2,pmul(th,pvar("a0_D"))),sig(3,pmul(th,pvar("aa0_D"))))
czd=sadd(sig(3,pmul(th,pvar("c1_D"))),sig(4,pmul(th,pvar("cc1_D"))))
ccd=sadd(sig(3,pmul(th,pvar("c0_D"))),sig(4,pmul(th,pvar("cc0_D"))))
kc=sshift(sig(2,pmul(pmul(th,et),pvar("b1"))),2)
kr=sadd(sscale(Fraction(1,4),smul(pp,pp)),sshift(sig(2,pmul(pmul(th,et),pvar("b0"))),2))
FD=F_from(pp,kc,kr,sshift(azd,3),sshift(acd,3),
          sshift(sadd(sscale(Fraction(1,2),smul(pp,azd)),czd),3),
          sshift(sadd(sscale(Fraction(1,2),smul(pp,acd)),ccd),3))
LD={7:sig(4,pvar("k0")), 8:sig(12,pvar("k6")), 9:sig(20,pvar("k2load"))}

W=[8-i for i in range(7)]+[2,6,10]
tails=json.loads(TAILS.read_text())
def build(entries,row,F,L):
    tot=szero()
    for rm,rc in entries:
        m=[int(v) for v in rm]
        assert len(m)==10 and sum(a*b for a,b in zip(m,W))==12+row
        u=szero(); u[0]=pconst(1)
        for i,e in enumerate(m[:7]):
            if e: u=smul(u,spow(F[i],e))
        for i,e in enumerate(m[7:],start=7):
            assert e in (0,1)
            if e: u=smul(u,L[i])
        tot=sadd(tot,sscale(Fraction(str(rc)),u))
    return tot

SUB={"ell1":pvar("ell1"),
     "cs2":pmul(pmul(th,et),pvar("b1")), "rs2":pscale(4,pmul(pmul(th,et),pvar("b0"))),
     "aaa1":pmul(th,pvar("a1_D")), "az3":pmul(th,pvar("aa1_D")),
     "aaa0":pmul(th,pvar("a0_D")), "ac3":pmul(th,pvar("aa0_D")),
     "ez3":pscale(2,pmul(th,pvar("c1_D"))), "ez4":pscale(2,pmul(th,pvar("cc1_D"))),
     "ec3":pscale(2,pmul(th,pvar("c0_D"))), "ec4":pscale(2,pmul(th,pvar("cc0_D"))),
     "k":pvar("k0"), "k6":pvar("k6"), "k2":pvar("k2load")}
HALF=pscale(Fraction(-1,2),pvar("p"))
def delta(poly):
    out=pzero()
    for mono,co in poly.items():
        t=pconst(co); dead=False
        for n,e in mono:
            if n=="rho":
                assert e%2==0, "odd rho: delta_D1 undefined"
                t=pmul(t,ppow(HALF,e//2))
            elif n in SUB: t=pmul(t,ppow(SUB[n],e))
            else: dead=True; break
            if not t: dead=True; break
        if not dead: out=padd(out,t)
    return out

TERM=re.compile(r'^\((-?\d+(?:/\d+)?)\)\*(.*)$')
def parse_frozen(path):
    o={}
    for part in path.read_text().strip().split('+'):
        part=part.strip()
        if not part: continue
        mm=TERM.match(part); assert mm
        co=Fraction(mm.group(1)); d={}
        for f in mm.group(2).split('*'):
            if '^' in f: n,e=f.split('^'); d[n]=d.get(n,0)+int(e)
            else: d[f]=d.get(f,0)+1
        k=tuple(sorted(d.items())); o[k]=o.get(k,Fraction(0))+co
    return {k:v for k,v in o.items() if v}

print("A. FROZEN GRADE-15 ROWS, INDEPENDENT RECONSTRUCTION")
okA=True
for row in range(1,8):
    tot=build(tails[str(row)],row,FT,LT)
    fr=parse_frozen(FROZEN/f"Tg15_{row}_q.poly")
    m=(tot[15]==fr); okA&=m
    odd=sum(1 for mo in fr for n,e in mo if n=="rho" and e%2)
    print(f"   row {row}: terms {len(fr):>4}  match={m}  odd_rho_terms={odd}")
print("   ALL SEVEN REPRODUCED:",okA)

print("\nB. delta_D1 FUNCTORIALITY AND THE CHARGED ROWS")
okB=True; img={}
for row in range(1,8):
    tot=build(tails[str(row)],row,FT,LT); d1=build(tails[str(row)],row,FD,LD)
    for g in range(N): okB &= (delta(tot[g])==d1[g])
    img[row]=d1[15]
    low=[g for g in range(15) if d1[g]]
    print(f"   row {row}: total g15={len(tot[15]):>4} g16={len(tot[16]):>4} | "
          f"D1AC g15={len(d1[15])} g16={len(d1[16])} | nonzero below g15: {low or 'none'}")
print("   FUNCTORIAL AT EVERY GRADE 0..16:",okB)

print("\nC. GRADE-15 IDEAL STRUCTURE")
g1=pmul(ppow(th,2),pscale(Fraction(3,4),padd(pmul(pvar("a0_D"),pvar("c1_D")),
                                             pmul(pvar("a1_D"),pvar("c0_D")))))
g2=pmul(ppow(th,2),pscale(Fraction(3,8),padd(pscale(2,pmul(pvar("a0_D"),pvar("c0_D"))),
                          pscale(-1,pmul(pvar("p"),pmul(pvar("a1_D"),pvar("c1_D")))))))
for row,(s,d,j) in {1:(1,1,0),3:(-1,4,1),5:(-1,32,2),7:(-1,128,3)}.items():
    assert img[row]==pmul(pscale(Fraction(s,d),ppow(pvar("p"),j)),g1), row
assert img[2]==g2 and not img[4] and not img[6]
print("   row1=g1, row3=-(p/4)g1, row5=-(p^2/32)g1, row7=-(p^3/128)g1")
print("   row2=g2, row4=row6=0 ; ideal = (g1,g2)")
print("   variables:",sorted({n for P in img.values() for mo in P for n,_ in mo}))

print("\nD. IMAGES OF THE J1 AND J2 GENERATORS")
for n in ("rs","cs","c0","c1","a0","a1"):
    print(f"   delta_D1({n}) = {delta(pvar(n)) or 0}")
print("   => all six root coordinates of (5.1) vanish under delta_D1")

print("\nE. MUTATION DETECTABILITY")
def variantD1(rs4=4, ez2=2, moving=True):
    q=szero(); q[0]=pvar("p")
    if moving: q[1]=pscale(2,pvar("ell1"))
    cz=sadd(sig(3,pscale(Fraction(ez2,2),pmul(th,pvar("c1_D")))),
            sig(4,pscale(Fraction(ez2,2),pmul(th,pvar("cc1_D")))))
    krv=sadd(sscale(Fraction(1,4),smul(q,q)),
             sshift(sig(2,pscale(Fraction(rs4,4),pmul(pmul(th,et),pvar("b0")))),2))
    return F_from(q,kc,krv,sshift(azd,3),sshift(acd,3),
                  sshift(sadd(sscale(Fraction(1,2),smul(q,azd)),cz),3),
                  sshift(sadd(sscale(Fraction(1,2),smul(q,acd)),ccd),3))
base={r:build(tails[str(r)],r,FD,LD) for r in range(1,8)}
for lab,kw in {"rs factor 4 -> 1":dict(rs4=1),
               "ez/ec factor 2 -> 1":dict(ez2=1),
               "drop moving 2*sigma*ell1":dict(moving=False)}.items():
    Fm=variantD1(**kw); det={15:[],16:[]}
    for row in range(1,8):
        mv=build(tails[str(row)],row,Fm,LD)
        for g in (15,16):
            if mv[g]!=base[row][g]: det[g].append(row)
    print(f"   {lab:<26} g15: {det[15] or 'NONE'} ; g16: {det[16] or 'NONE'}")
print("\nOPUS5-HOSTILE-VERIFY-COMPLETE okA=%s okB=%s"%(okA,okB))
```

Observed output is reproduced verbatim in §4.1, §4.4, §4.5, §4.6 and §3.1
above.
