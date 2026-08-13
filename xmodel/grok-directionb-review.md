# Adversarial review: SHEET6-DIRECTIONB.md §6.T + §6.V

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-13.
Scope: the 83-var forced-nonzero-tail window-build verdict
(NOT EMPTY-BY-KILL). Method: read §6.T/§6.V, SHEET6-TEMPLATE E5
erratum, directionb_window.py / directionb_strike.py end-to-end;
replay `gate` / `bands` / `verdict`; independent census of the
banked D=21 object; fresh D=9 jet rebuild of rows 6 and 8;
spot-check of C6.1, C8.1, C12.1 against the jet rows; extra
`(w, h-sign, dead-stretch)` samples the harness never ran.
No other repo file modified. No git.

**VERDICT: SOUND-WITH-ERRATA — the 7/7 numbers, the over-approximation,
the −42 wiring, and the 47 band conditions survive a hostile replay;
“uniformly in the 7” in (2) is sampled rank-stability, not a closed
identity, and is the only load-bearing wording that overclaims.**

---

## Findings (worst first)

### 1. Severity: erratum — (2) is sampled, not uniform

- File: `cases/directionb_window.py:715-721` (the only proof of
  `SHEET6-DIRECTIONB.md:487-488`)
- Claim: the differential is “INCONSISTENT — uniformly in the
  dead-stretch values (7 free, incl. all-zero)”.
- How checked:
  - `tail_linearize` treats the 7 as *parameters* via `ds` and
    keeps every tail-degree-1 monomial, including
    `(monomial in the 7) * (one tail)`.
  - Independent census of `/tmp/directionb_tails_D21.pkl`:
    **20 488** such terms, hitting 67 of the 77 eta-rows
    (every even row except band 6). So \(L(\mathrm{ds})\)
    *moves* with the 7. There is no structural vanishing that
    would make two samples a proof.
  - The harness tests **exactly two** points: `ds = {}` and one
    `genval` sample (`directionb_window.py:715-717`).
  - Hostile extras (not in the 7/7): a second rational sample,
    a mixed-E sample, the axis vector `uf18=1`, and `ds=0` at
    \(w=(2,3)\). All four: `77 x 76`, rank **29**,
    `incons=True`, `undec=0`. Rank is stuck.
  - `uf30` never appears in any window monomial, so “7 free”
    is 6 genuine parameters plus a dummy.
- Why this is not a break: the target \(b\) (w4-block \(+42\)
  on eta^0) is independent of the 7 (the only empty-varkey
  terms in the whole window are the nine Row_20 w4-blocks).
  Rank-stable inconsistency on 6 points, including the origin
  and a mixed-E sample, is strong evidence the moving 29-plane
  never contains \(b\). It is not a resultant / left-kernel
  identity in the 7. The word “uniformly” should be downgraded
  to “at 0, at a generic sample, rank-stable on further samples”.
- Does not flip NOT EMPTY-BY-KILL. It is a
  FALSE-KILL-SHARPNESS wording hazard on (2) only.

### 2. Severity: nit (wording) — “no functional” is a linear-algebra statement at depth 21

- File: `SHEET6-DIRECTIONB.md:479-530`
- Claim: “There is NO linear-algebra kill … No functional
  annihilates all tail columns while detecting the −42 — the
  exact mechanism that killed the zero-tail stratum … has no
  analogue once tails are on.” Then the headline: “the 83-var
  forced-nonzero-tail window does NOT kill residue-A.”
- How checked: `relax` (`directionb_window.py:638-658`) is
  ordinary unit-pivot GE of the 77 raw eta-rows with every
  var-monomial an independent column. Consistency means: no
  *linear* combination of *these* 77 rows, at chart depth 21,
  kills every monomial column while pairing with −42.
  It does **not** rule out
  - a nonlinear combination (resultant / Groebner of the 47
    band conditions + slot-20),
  - extra J-rows \(k \ge 21\),
  - unfreezing the B-side.
- Honesty audit: the mechanism-sentence is accurate if
  “functional” is read as “linear functional of this row set”.
  The headline is stronger; the next paragraphs walk it back
  (“NONEMPTINESS IS NOT CERTIFIED”, “What IS certified: no
  kill”, “exhausted as a killing instrument at depth 21”).
  Pre-registered semantics “NOT EMPTY-BY-KILL” matches what
  was actually proved. Not a false-survival of the object —
  the caveat is in the same subsection. Still the one place a
  skimming reader can confuse “no linear kill by these rows”
  with “residue-A is nonempty”.

### 3. Severity: nit — gate does not certify the 42 that verdict consumes

- File: `cases/directionb_window.py:236-238` (gate) vs
  `:348` (`RHS42 = K3(42)`) used at `:428-429`, `:476`,
  `:608`, `:655`, `:688`
- The gate check named `0 = -42/(c_f c_g)` tests only
  `c1, c2 != 0` on the eta^0 w4-block. It never reads a
  scalar −42 out of the pickle and never compares it to
  `RHS42`.
- How checked:
  - Banked `byk[20][0][()]` in *both* `directionb_dsys.pkl`
    and `directionb_tails_D21.pkl` is **exactly** the two
    keys \((\alpha_1 w_1^4,\ \alpha_2 w_2^4)\). No rational
    constant. dsys vs tails const agree on all 9 overlapping
    eta-comps; tails has the extra pure-tail eta^27.
  - That is the *correct* split: `jrows` is the LHS of (J);
    −42 is the RHS (`directionb_strike.py:7-10`,
    `SHEET6-DIRECTIONB.md:58-66`). Adding `+42` and testing
    `LHS + 42 = 0` is the right equation. Independent
    re-derivation of the chart Jacobian
    \(J_{t,\eta}(x,y) = -42 t^{-11}\) and the
    \(t^{-31}\) prefactor recovers `LHS = -42 t^{20}`
    at \(c_f c_g = 1\). Sign and placement are right.
  - The E5 erratum (`SHEET6-TEMPLATE.md:239-244`) is a
    **different** factor (243 vs 729 in the \(w_i^4\) pin,
    a factor of 3). It does not move 42. The window never
    loads the E5 formula; \(w_1, w_2\) stay free and are
    sampled. Front 5 of SHEET6-DIRECTIONB-REVIEW already
    recorded that the zero-tail kill is E5-independent;
    the same holds here.
  - `directionb_strike.py:295-297` (`danal`: `const == rC(-42)`)
    would **fail** on the actual dsys pickle (const is the
    w4-block). That check is not on the window path.
- False-survival angle: a wrong 42 (or a missed `+42`) would
  change the target of a rank-57 map in 77-space and could
  fake consistency. The wiring is the same constant in every
  analysis phase; the identity matches; extra samples at
  \(w=(2,3)\) (where the weight-4 w4-block and the weight-0
  42 mix differently) still give rank 57, consistent,
  `undec=0`. No break. The gap is that gate will still
  print PASS if someone edits `RHS42`.

### 4. Severity: nit — “ranks identical on all 4” is not in the 7/7

- File: `SHEET6-DIRECTIONB.md:472` vs
  `cases/directionb_window.py:699` (`verdict(s1=1,s2=1,w1=K1,w2=K1)`
  only)
- The 47 band conditions *are* computed on all 4 h-sign
  branches (`bands()`, lines 309-320); ranks match the §6.T
  table on every branch, no leftover.
- The decisive tests (1)(2)(3) run on a single
  \((s,w)\). Hostile extras: full-window relax at
  \(w=(2,3), h=(+,+)\) and at \(w=(1,1), h=(+,-)\) — both
  `77 x 5106`, rank **57**, consistent, `undec=0`. So the
  advertised identity of ranks is true on the samples that
  were missing from the harness; it is not what `verdict`
  certifies.

### 5. Severity: nit — claim (4) is not one of the 7/7, but it reproduces

- File: `SHEET6-DIRECTIONB.md:500-507`. No corresponding
  `chk` in `verdict()`.
- Independent reconstruction: cascade bands 6/8/10 (generic
  frees), then `build_affine` on bands 12..20 in the 50
  level-\(\ge 43\) tails.
  - Two seeds: `48 eqs, 50 unk, rank 16`, **32** leftover
    rows, all `0 = unit`, leftover rhs **different** at
    every one of the 32 labels.
  - `low = 0`: same 48/50/16, but only **6** leftover rows
    are `0 = unit`, exactly
    `Row_20[eta^12,15,18,21,24,27]`. The other 26 collapse
    to `0 = 0`.
- Matches the paragraph, including the “not a constant
  absurdity” reading: generic lows make all 32 into units;
  the zero-low specialisation recovers the six-component
  first-order obstruction. “Unreduced” here means the
  48−16 non-pivot rows, not `esolve`’s `undec` (which is 0).

---

## What was attacked and did **not** break

### (a) False-survival of the relaxation

| Attack | Result |
|---|---|
| Is `relax` a genuine over-approx? | Yes. Columns are the raw `vk` keys (`directionb_window.py:651`). An actual tail assignment maps to a linearized point. Inconsistent ⇒ empty; consistent ⇒ inconclusive. That is what they use it for. |
| Monomial list complete, incl. deg-3 low feeding eta^0? | Banked `Row_20[eta^0]`: 2034 monomials, degrees `{1:14, 2:184, 3:532, 4:582, 5:386, 6:222, 7:78, 8:36}` — matches §6.T:461-462 on the nose. 390 of the 532 deg-3 have every factor at level \(\le 42\). `VDEG_CAP = D = 21`, max degree 8, **0 HIVAR/sentinel hits**. |
| Rows dropped before ranking? | `byk` keys `{6,8,10,12,14,16,18,20}`; eta-counts `9+10+10+9+10+10+9+10 = 77`. Independent recount of `relax` columns: **10 x 2718** and **77 x 5106**. Odd rows identically 0 in the D=21 object and in a **fresh D=9 jet rebuild** (rows 0-5 and 7 empty). Nothing dropped. |
| −42 / E5 consistency? | See finding 3. Same `RHS42` everywhere on the analysis path; E5 is not this 42. Extra \(w=(2,3)\) still consistent. |

Historical wrong-object retraction (SHEET6-DIRECTIONB-REVIEW Front 4)
does not recur: the object here is the thing §6 said it would
build (7 + 76 P-side tails = 83; B-side frozen by `build_frozen`).
74 of the 83 actually appear in some monomial; the missing ones
are `uf30` and a handful of unused odd-level names, not dropped
rows.

### (b) False-kill-sharpness of the differential

Origin and one generic sample do what the doc says (rank 29,
inconsistent). Four further samples, including a mixed-E point
and a different \(w\), stay at rank 29 inconsistent. The
uniformity *argument* is still only sampling (finding 1). No
counter-sample found.

### (c) Reproduction

```
cd cases && python3 directionb_window.py gate      # 16/16, 3.0s
                 python3 directionb_window.py bands     # ledger, 15.6s
                 python3 directionb_window.py verdict   # 7/7, 100.3s
```

| Phase | Claimed | Replay | Mismatch? |
|---|---|---|---|
| gate | 16/16, ~3s | 16/16, 3.0s | no |
| bands | 47 conditions, ranks as table, ~11s | ranks **exact** (S and V, all 4 branches), C6.1 / C10.6 / C16.10 print matches, 15.6s | time only |
| verdict | 7/7, ranks 10 / 57 / 29 / 4 / 8 / 16, ~89s | 7/7, those ranks exactly, 100.3s | time only |

Band-16 V-tier is `10 E-rows x 634 (varmono, w-mono) cols`;
the table’s `321 x 628` is the S-tier, as labelled. No
leftover on any V-tier. State used: `/tmp/directionb_tails_D21.pkl`
(identical `byk[20][0]` to the repo copy
`directionb_tails_D21.pkl`).

### (d) Semantics

Covered in finding 2. Pre-registered call NOT EMPTY-BY-KILL
is the right name for what (1) certifies. Residue-A is not
certified nonempty.

### (e) Band-condition spot-check vs a direct jet

Fresh rebuild: `directionb_strike.dsys_tails(9)` (58.7s,
P-side tails free, B-side frozen, `VDEG_CAP=9`, sentinel
assert on). Compared to the banked D=21 object **by variable
name**, not by registry index.

- Row_6: 9 eta-comps, 6 monomials each, **coefficient-for-coefficient
  identical**.
- Row_8: 10 eta-comps, 18 (resp. 12 at eta^27) monomials,
  **identical**.
- Odd rows 1,3,5,7 and rows 0-5 identically 0 on the fresh jet.

Then three of the 47 echelon conditions, evaluated in E at
on-locus and off-locus points (cascade the lower bands, solve
the new levels, substitute back into the *raw* jet row):

| Condition | On locus | Off locus (perturb one new tail) |
|---|---|---|
| **C6.1** (`SHEET6-DIRECTIONB.md:423`, `directionb_window.py:335`) | all 9 raw Row_6 etas = 0 and C6.1 = 0 | all 9 etas nonzero and C6.1 ≠ 0 |
| **C8.1** (band 8, after C6) | all 10 raw Row_8 etas = 0; C8.1–C8.4 = 0 | all 10 etas fire; C8.1–C8.4 all fire |
| **C12.1** (after cascade 6/8/10/12) | all 9 raw Row_12 etas = 0; C12.1–C12.7 = 0 | all 9 etas fire; C12.1–C12.4 fire (C12.5–7 do not see the perturbed level-44 tail) |

C8.1 and C12.1 were the requested bands. Because Row_8 of the
banked object **is** the fresh D=9 jet row, the C8 on/off test
is a jet test, not a code-vs-same-code echo. C6.1 has the same
status. C12.1 is only as good as the banked Row_12 (no D=13
rebuild; D=9 cannot see slot 12).

---

## Bottom line

Do not retract NOT EMPTY-BY-KILL. The relaxation is a real
over-approximation of the banked window, no rows were dropped,
the deg-3 low monomials that feed eta^0 are present, and −42
is the chart-Jacobian RHS (not the E5 factor-of-3) used with
the same sign in every analysis phase. The differential at
the origin is a genuine first-order kill; “uniformly in the 7”
should be rewritten as a sampled + rank-stability statement
unless someone produces a left-kernel identity in the 7.
Nonemptiness of \(V\) remains open, exactly as §6.V says.
