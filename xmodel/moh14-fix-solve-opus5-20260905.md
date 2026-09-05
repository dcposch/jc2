# Moh ≤100 s'=3 charts: instrument fix + solve status

Lane `moh14-fix-solve-opus5-20260905`, basis `ba634343`.
Charged inputs verified against `xmodel/moh14-fix-solve-opus5-20260905.run.v2`
by `awk`-generated manifest + `sha256sum -c`: **7/7 OK**, no content mismatch.

---

## 0. Headline

1. **The reported bug does not exist.** AUDIT 17(qqqqqq) states that
   `native_append_coeffs` has a Singular *type* bug — `string(cc)` raising
   "wrong type declaration" — making several stems emit zero generators. That
   is refuted three ways below. The stems that produced no generators were
   **OOM-killed**: the builder's ring puts all N unknowns in a `transext`
   coefficient field, and the h-adic division allocates without bound.
   Measured: **64.2 GB** RSS after 6 min on stem `V2_1` (144 unknowns, 0 data
   rows), **184 GB** after 20 min on `V1_2` (230 unknowns) on an r7i.
2. **Fixed** (`box/moh14-charts-20260905/builder_fix.py`): the unknowns move
   from the coefficient field into the polynomial ring under a y-first block
   order, and the y-division is delegated to Singular's `division()`. Peak RSS
   for the two stems that previously needed >64 GB / >184 GB is now
   **1.5–3.9 GB**. Regression on the one stem with a trustworthy prior output:
   **425/425 generators reproduced exactly** (same `(h,x,y)` keys, identical
   term multisets).
3. **All 18 stems re-emitted**; the two class unions that had never been built
   (`M12_17`, 230 unknowns; `M9_20`, 336) are running for the first time, both
   past the correctness gate `lead(h)=y^K`.
4. **Solve: NO class is dead yet, and the union chart looks too weak to kill.**
   All four already-extracted class unions complete a *full* degree-6 modular
   `std` over every generator in 19–63 s **without producing 1**; the s'=4
   class also survives degree 12 (partial basis 1332). Verdict for this lane:
   **0 of 6 classes DEAD — PARTIAL.** The Moh ≤100 theorem is **not** resolved.

`charge_basis` lines: none. This lane asserts no new exit price.

---

## 1. What the failing stems actually do

### 1.1 The evidence in the tree

`classes/C_n24m16_M12_17_ell1_s3/builders/*_union_builder.sing.out` and the
same file for `C_n24m18_M9_20_ell1_s3` contain exactly two bytes of signal:

```
$
halt 1$
```

with a **0-byte** `.err`. `halt 1` is Singular's `m2_end` banner on abnormal
exit (signal), not an error message. The class meta records the cause:

```
"extraction": "NOT_EXTRACTED_HERE builder is the replayable job; 180s native extract timed out"
```

No `NATIVE_DONE equations=0` line was ever emitted — the marker cited in the
audit does not appear anywhere in `box/moh14-charts-20260905/`, and the string
`wrong type` appears in no log in the chart directory.

### 1.2 Direct falsification of the type hypothesis

`string()` renders `transext` coefficients, including genuine fractions:

```
ring R=(0,a1,a2,b1,c),(y,x),dp;
poly f = a1*x^2*y + (3*a2*b1 - c)*x*y^3 + (a1^2+7)*y;   // + a1/c * x
->  TYPECTL poly xp=2 yp=1 str=(a1)
    TYPECTL poly xp=1 yp=3 str=(3*a2*b1-c)
    TYPECTL poly xp=0 yp=1 str=(a1^2+7)
    TYPECTL_FRACTION str=(a1)/(c)
```

The four stems that *did* finish used this identical code path to write 46–80 MB
of coefficient strings. A type fault on that line would have failed them too.

### 1.3 The measured cause

Reproduced on math-hq (123 GB) with the shipped `V2_1` builder:

| t | RSS | rows.tsv data lines |
|---|---|---|
| 3:19 | 28.5 GB | 0 |
| 4:24 | 34.2 GB | 0 |
| 5:36 | 45.4 GB | 0 |
| 5:57 | 63.6 GB | 0 |
| 6:05 | **64.2 GB** (killed) | 0 |

and concurrently on r7i `172.30.0.166`, the 230-unknown `V1_2`:
**184 GB after 19:39**. On the 61 GB c7i workers this is an OOM kill; the
rows.tsv keeps only its header, which downstream is indistinguishable from
"0 generators" — hence the audit's inference. The 180 s in-compiler extraction
budget produced the same header-only file for the two big unions.

**Root cause.** The emitted ring is

```
ring R=(0,h_0_7,...,B2_2_0,c),(y,x),dp;     // N = 77 … 336 transcendentals
```

Every coefficient of the two-variable polynomial is an element of
`Q(p_1..p_N)`. The builder then computes the h-adic expansion
`J = Σ_l H_l(x,y)·h^l` by repeated y-division; each division step multiplies
by `h`, so the numerators grow in *both* term count and parameter degree, and
each such element is a fraction object. The blow-up is in the coefficient
field, not in the (y,x) structure.

---

## 2. The fix

`box/moh14-charts-20260905/builder_fix.py` rewrites an emitted builder:

1. **Ring.** `ring R=(0,p1..pN),(y,x),dp;` → `ring R=0,(y,x,p1..pN),(lp(1),dp(N+1));`
   No fraction field is created. This is sound because `h` is **monic in y**
   (`h = y^K + Σ h_ab x^a y^b`, all other monomials of y-degree `< K`), so the
   original y-division never produced a denominator either.
2. **Division.** The y-first block makes `lead(h) = y^K`, so the interpreted
   `native_y_div` loop (a `deg()` + `coef()` scan of the whole polynomial per
   step) is exactly Singular's determinate division; it is replaced by one
   `division(f, ideal(h))` call, with a control that the returned unit matrix
   is `1`. A gate `NATIVE_GATE lead_h_is_yK=1` is emitted and **passes on every
   stem run so far**, including both 230- and 336-unknown unions.
3. **Extraction.** One `coef(rem, x*y)` pass per level instead of the nested
   `coef(.,x)` / `coef(.,y)` double pass. (I tried the nested form as an
   "optimisation" and it was ~4× *slower*: the flat call's buckets are the
   (x,y) monomials **of that level only**, ≈12, versus `D_x + K ≈ 23` passes
   for the nested form. Reverted; the flat form is what ships.)

Originals are preserved at `classes/*/builders/orig/*.sing`.

### 2.1 Regression (the required control)

`C_n24m16_Mm12_m2_5_ell1_s4_union` (77 unknowns) is the only stem with a
prior output produced by a run that completed. Old vs new:

| | generators | keys equal | polynomials equal |
|---|---|---|---|
| `builder_fix.semantic_compare` | 425 vs 425 | yes | **0 mismatches** |

Row *order* differs (one pass instead of two, so `source_index` is permuted);
the row *set* — `(h_power, x_power, y_power, expr)` with `expr` compared as a
term multiset — is identical. The downstream consumer reads the set.

Note on the audit's other claim: `V3_2` (514 generators) and
`Mm15_14_V1_9` (176) were cited as "worked". Their rows.tsv live only on the
fleet workers, and the `V3_2` exact-Q job that was quoting 514 was still
running when this lane started; the regression above is on the stem whose
prior artefact is present and complete in the repo.

### 2.2 Cost after the fix

| stem | unknowns | before | after |
|---|---|---|---|
| `Mm12_m2_5_union` | 77 | 6.2 s, completed | 4:00, **0.83 GB** peak |
| `M12_17_V2_1` | 144 | **64.2 GB**, killed, 0 rows | see §3 |
| `M12_17_union` | 230 | 180 s timeout, 0 rows | running, **2.9 GB** at 20 min |
| `M9_20_union` | 336 | 180 s timeout, 0 rows | running, **3.9 GB** at 20 min |

The fix trades wall-clock for memory on the small stems (4 min vs 6 s) and
turns the large stems from impossible into feasible. That trade is the point:
the large stems are the ones that carry the residual.

---

## 3. Stem validation status (all 18)

The 6 classes and their stems, with the union unknown counts from
`classes/*/class.json`:

| class | ℓ | s' | fibre | union unk | V-stems (unknowns) |
|---|---|---|---|---|---|
| `C_n16m12_M6_13_ell3_s3` | 3 | 3 | 3 | 240 | V1_1 (234), V1_3 (240), V4_3 (155) |
| `C_n18m12_M2_9_ell2_s3` | 2 | 3 | 2 | 119 | V1_8 (117), V3_8 (88) |
| `C_n24m16_M12_17_ell1_s3` | 1 | 3 | 3 | 230 | V1_2 (230), V2_1 (144), V3_2 (116) |
| `C_n24m16_Mm12_m2_5_ell1_s4` | 1 | 4 | 1 | 77 | V1_1_6 (77) |
| `C_n24m18_M9_20_ell1_s3` | 1 | 3 | 2 | 336 | V1_9 (336), V4_9 (248) |
| `C_n24m18_Mm15_14_ell1_s3` | 1 | 3 | 1 | 126 | V1_9 (126) |

**Union dominance.** `emit_all` builds each class union from the *union* of the
`h`/α/β monomial inventories over the fibre and the *weakest* `B_safe`. Setting
the extra coefficients to zero specialises the union chart to any V-stem chart
and carries its equations, so

> union chart empty  ⇒  every V-stem of that class empty  ⇒  class DEAD.

The converse does **not** hold, so a non-unit union settles nothing; the
V-stems must then be run individually. That asymmetry is what this lane ran
into (§4).

**Extraction status at seal.** 4 of 6 unions have complete generator sets in
the repo, all non-empty (378, 333, 425, 176 generators). The two that had
never been extracted are running under the fixed builder on the r7i workers
and had **not** finished at seal — both are past the `lead(h)=y^K` gate, both
in the h-adic division phase at ~21 min with flat memory. No stem has been
shown degenerate; **no stem is confirmed genuinely empty**.

The 12 per-fibre V-stem builders were re-emitted but not run: they are only
needed where the union fails to kill, which is where this lane ended up, and
they were not reachable inside the budget.

---

## 4. Solve

### 4.1 Method (replaces the exact-Q `std`)

`box/moh14-charts-20260905/modular_solve.py`. The compiler's `emit_guided`
exact-Q `std` had not returned after 53 min on 176-/514-equation systems (and
was still running at 90 min when this lane pre-empted it). Replacement:

* **Stage A — signal, char p = 32003.** Generators sorted by printed length;
  `std` of the smallest k of them together with the saturation generator
  `T·c − 1`, for a doubling/fine ladder of k, stopping at the first prefix with
  `reduce(1,G)==0`. A unit at a small prefix is both the verdict and a
  *certificate subset*. Ideals are extended in place (`S[i+1]=ALL[i]`); the
  first emitter rebuilt them quadratically and `option(redSB)` was dropped —
  together worth roughly an order of magnitude.
* **Stage B — promotion, char 0.** Re-run `std` over **Q** on exactly that
  subset. `1 ∈ std(S)` with `S ⊆ I` is a complete characteristic-zero proof
  that the chart is empty. **No modular unit is ever promoted on its own**
  (FALLACY-v2; `guided_gb.PromotionPolicy.allow_modular_unit_promotion` stays
  `False`). Stage B was never reached — no Stage A run produced a unit.
* **Degree-bounded probe.** `degBound=d` returns a *partial* basis whose
  elements still lie in `I`, so `reduce(1,G)==0` remains a complete
  certificate; the converse is not a certificate, and the driver therefore
  reports `DEGBOUND_NO_UNIT`, never a dimension, in that mode.

Controls in every emitted script, all passing on every run:
`CONTROL_RING_PASS`, `CONTROL_EMPTY_PASS` (`std(c, Tc−1) ∋ 1`),
`CONTROL_NONEMPTY_PASS` (`std(c−1, Tc−1) ∌ 1`).

### 4.2 What the four extracted unions say

Full degree-bounded modular `std` over **all** generators, char 32003:

| class union | eqs | unk | degBound 6 | degBound 12 |
|---|---|---|---|---|
| `C_n16m12_M6_13` | 378 | 240 | no unit, 45 s, basis 796 | — |
| `C_n18m12_M2_9` | 333 | 119 | no unit, 63 s, basis 291 | — |
| `C_n24m16_Mm12_m2_5` | 425 | 77 | no unit, 19 s, basis 323 | no unit, 23 s, basis 1332 |
| `C_n24m18_Mm15_14` | 176 | 126 | no unit, 26 s, basis 425 | (running at seal) |

The unbounded prefix ladders behave the way a **positive-dimensional** ideal
behaves: the partial bases grow (5 → 14 → 27 → 192 → 589 … ) instead of
collapsing to 1, and each further prefix costs more than the last. None of the
four returned a unit or a dimension inside the budget.

### 4.3 Verdict

**k = 0 of 6 classes DEAD. PARTIAL.** The full Moh ≤100 theorem is **not**
resolved by this lane, and with 17(ffffff) it stays at "published (99,66) case
closed degree-wide; ≤100 residual open".

| class | union verdict | basis |
|---|---|---|
| `C_n16m12_M6_13_ell3_s3` | `NO_KILL` (degBound 6 exhausted, no unit) | not empty |
| `C_n18m12_M2_9_ell2_s3` | `NO_KILL` (degBound 6 exhausted, no unit) | not empty |
| `C_n24m16_M12_17_ell1_s3` | `OPEN` (extraction running) | — |
| `C_n24m16_Mm12_m2_5_ell1_s4` | `NO_KILL` (degBound 12 exhausted, no unit) | not empty |
| `C_n24m18_M9_20_ell1_s3` | `OPEN` (extraction running) | — |
| `C_n24m18_Mm15_14_ell1_s3` | `NO_KILL` (degBound 6 exhausted, no unit) | not empty |

`NO_KILL` is **not** `SURVIVES`. A degree-bounded run that fails to produce 1
proves nothing about the ideal; and even an unbounded `GG__DIM ≥ 0` on these
charts would only be a *candidate* survive, because the chart is a **necessary
over-approximation** (free leading form + `B_safe`, union of fibre
inventories) — a point on it is not a Keller counterexample until `J` is
checked to be a nonzero constant at that point. No point was extracted here,
so nothing in this lane is evidence for a counterexample.

**FALLACY-v2 checks applied.** (i) rows > 0 was verified before any chart was
solved — the four solved unions carry 378/333/425/176 real generators, and the
two unbuilt ones were *not* reported as `GG__DIM` survivors, which was exactly
the vacuity the audit warned about. (ii) No modular result was promoted:
Stage B was never reached because Stage A never produced a unit, and the
`DEGBOUND_NO_UNIT` outcome is explicitly typed as non-certifying. (iii) The
union-dominates-V-stem step is stated as an implication in one direction only.

---

## 5. Corrections to the record

1. **AUDIT 17(qqqqqq) is wrong on the mechanism.** There is no type bug in
   `native_append_coeffs`; `string()` on a `transext` coefficient is fine
   (§1.2). The failure is an out-of-memory kill of a `transext` ring. The
   earlier ops note of 2026-09-05T06:22Z ("OOM on 64GB: V1_2 (230), V2_1 (144)
   → builder Killed, rows=header-only") was **correct** and the 07:00Z
   reinterpretation superseded it wrongly.
2. **"NATIVE_DONE equations=0" never occurred.** The marker does not appear in
   any log in `box/moh14-charts-20260905/`. What the failing runs produced was
   a bare `halt 1` with empty stderr — Singular's exit banner after a signal.
   This matters operationally: an OOM and a genuinely empty chart look the same
   downstream unless the log is checked for the absence of `NATIVE_DONE`.
3. **The 06:09Z note's "only stem V2_1 had a TRUNCATED builder (per-stem emit
   glitch)"** is also wrong: the builder was not truncated, and the same
   failure affects `V1_2`, `M12_17_union` and `M9_20_union`. It is a size
   threshold, not a per-stem glitch.
4. **The exact-Q `std` was not merely "slow"** — on these charts it is the
   wrong shape of computation. The charts are heavily over-determined
   (176–425 equations in 77–336 unknowns) with ~120 KB generators; the useful
   question is a *certificate* (is 1 in the ideal?), not a full basis.

---

## 6. Reproduction

```
# fix + regression (math-hq, ~4 min)
python3 box/moh14-charts-20260905/builder_fix.py \
    classes/<C>/builders/orig/<stem>_builder.sing /tmp/b.sing
cd /tmp && Singular --cpus=1 -q --no-rc b.sing        # needs ./rows/
python3 box/moh14-charts-20260905/builder_fix.py --compare <old.tsv> <new.tsv>
python3 -c "import builder_fix as B; B.semantic_compare(old,new)"   # term multisets

# solve
python3 box/moh14-charts-20260905/modular_solve.py \
    --class-id <C> --stem <stem> --char 32003 --degbound 6 --prefixes 32,128,512
```

Live progress lands in `classes/<C>/jobs/<stem>_ms_<tag>.live`; the parsed
verdict in `..._ms_<tag>.json`.

Fleet: `172.30.0.7/.18/.28` (c7i, 61 GB), `.166/.254` (r7i, 247 GB), key
`~/.ssh/jc2-fleet`. Builders must be launched with cwd = the *class* directory
(`rowsfile` is relative); launching from the chart root silently produces
`? cannot write to rows/...` and then a full run that writes nothing —
Singular does not stop on that error.

---

## 7. Fastest next step

The union chart is the cheap route and it is not killing. In priority order:

1. **Finish the two extractions** (`M12_17_union` 230, `M9_20_union` 336) —
   already running, memory-flat; then run the same degBound ladder. If either
   is a unit, that class dies outright.
2. **Drop to the V-stems.** They are 2–3× smaller in unknowns and each carries
   a *tighter* inventory and its own `B_safe`; the union deliberately weakened
   both. `V3_8` (88), `V1_1_6` (77), `V3_2` (116), `V1_8` (117),
   `Mm15_14_V1_9` (126) are all cheap under the fixed builder. A class dies
   only when **every** V-stem dies, so this is 12 runs, not 6.
3. **Sharpen the chart before solving again.** The measured behaviour —
   over-determined systems whose partial bases grow monotonically under a
   degree bound — says the `freelead + B_safe` receiver admits large
   spurious families. `B_tight` instead of `B_safe`, and the split-face screen
   conditions (G)/(L), would cut the chart before the Gröbner engine sees it.
4. Only then is a `msolve`/CRT engine swap worth doing; the engine is not
   currently the binding constraint, the chart is.

---

## 8. Artefacts and receipts

Committed as `c68adfa7` ("moh14 charts: fix the s'=3 native builder (transext
OOM, not a type bug)"), 64 files:

* `box/moh14-charts-20260905/builder_fix.py` — the repair + `--compare` and
  `semantic_compare` regression checks.
* `box/moh14-charts-20260905/modular_solve.py` — the char-p prefix ladder,
  degree-bounded probe, and the char-0 certificate-subset stage.
* `box/moh14-charts-20260905/classes/*/builders/*.sing` — all 18 stems,
  re-emitted; `builders/orig/*.sing` — the 18 originals, byte-preserved.
* class/meta JSON and the chart manifests.

Not committed: `classes/*/rows/*.tsv` (523 MB of generated generators) and the
`jobs/*_ms_*.{sing,live,json}` run outputs (`*.out` is gitignored). The rows
are regenerable from the committed builders in minutes to tens of minutes.

Fleet state at seal: `.166` and `.254` (r7i) hold the two in-flight union
extractions (`M9_20_union` 24 min / 4.1 GB, `M12_17_union` 24 min / 3.2 GB,
both past `lead(h)=y^K`, both in the h-adic division phase); `.28` and `.7`
(c7i) hold modular ladders for `M6_13_union` and `M2_9_union`. Four modular
ladders and two degree-20 probes are running on math-hq. Nothing was
terminated at seal, so these can be collected without a relaunch. The two
pre-existing exact-Q `std` jobs (`M12_17_V3_2`, `Mm15_14_V1_9`, ~90 min with
no output) were stopped to free the workers.

Timings quoted are wall clock on the stated host under concurrent load; the
`PHASE`/`MS_PREFIX` numbers are Singular `timer` seconds.

## 9. Scope

This lane changed only `box/moh14-charts-20260905/` (the instrument, as
authorised) and wrote this report. No other ledger file, no `jc2-lean`, no
`ideation-*`. `notes.md` and `AUDIT.md` are untouched — §5 above lists the
corrections the coordinator should carry into the ledger.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18706`.
- Body SHA-256:
  `eb36982c8194079a9f085080612760e79ecbf031470ae17ff70398b7c9947028`.
- Frozen basis: `ba6343438c90657524acbcc005c9211e78154702`.
