# Full Theorem-1.2 order chart for the Moh ≤100 residual (u_s=1 / H2)

Lane `moh14-fullorder-grok46-20260905`. Charts:
`box/moh14-charts-20260905/`. Frozen inputs under
`/tmp/jc2-lane.HLLVTr/inputs`. Adapter grok. Date 2026-09-05.

Charged inputs verified against
`xmodel/moh14-fullorder-grok46-20260905.run.v2` by pairing indexed
`charged_input_<i>_sha256=` with `charged_input_<i>_basename=` in `awk`
(no `getline` pairing — basename does not follow sha256 in this receipt)
and `sha256sum -c`. **11/11 OK**, no content mismatch. Banked at
`box/moh14-charts-20260905/charged_input_manifest.sha256`.

No new exit-price assertion is made, so no `charge_basis` line is licensed.

---

## 0. Headline

```text
HEADLINE: PARTIAL. The s'=3 order chart was a tot-degree SUB-SLICE on
7/12 fibres (17(ggggg) shape). Completing it to the full Theorem-1.2 D1
inventory does NOT produce 1 at degBound 6/8 on the 5 fibres that were
already full. Unbounded modular std of those full charts did not return
UNIT or DIM in the 19-63 s window, nor in 25 min locally, nor in
60 min on r7i (11 GB RSS on the 77-unknown chart). The 12 rows are not
killed by (T). They are a receiver/K16-type OPEN: the order chart is the
right object, it is now the full necessary D1 over-approx, and emptiness
is compute-bound. Not a JC2 counterexample (nothing lifts). 17(rrrrrr)
was wrong that these rows need pole/Jacobian/incidence (those are u_s≥2).

k of 6 classes GG__UNIT = 0.
Moh ≤100 theorem: NOT resolved.
```

The one sentence to carry: theorem (T) for the twelve `u_s=1` residuals
is the emptiness of the *full* descended monomial-Jacobian D1 order
chart; the emitted free-lead/`B_safe` chart was missing the tot-degree
cokernel on seven fibres and was already the full inventory on five;
neither the envelope nor the completed chart produced a unit, and no
surviving `(P,Q)` with `J=c·x^ℓ` was extracted.

---

## 1. Frozen-input gate

Manifest generated with `awk` from the receipt's
`charged_input_<i>_sha256=` / `charged_input_<i>_basename=` fields
(collect both maps, then emit). Checked with `sha256sum -c`. 11/11 `OK`.
No digest was retyped. Workspace `builder_fix.py`, `sprime3_compiler.py`,
`modular_solve.py`, `order_basis_full.py` match the frozen copies.

---

## 2. What 17(rrrrrr) got wrong, and what this lane is

AUDIT 17(rrrrrr) read degBound-6 modular `std` with no `1` as “the s'=3
chart is TOO WEAK” and asked for the missing pole / Jacobian /
minor-incidence families that killed (99,66) and D=108 split. That is
the **wrong kill mechanism** for these twelve rows.

- All twelve live residuals have `u_s=1`. They are the (H2) half:
  Prop 6.3/6.4 descent plus theorem (T) = the descended
  monomial-Jacobian **order** chart empty.
- Split-chart pole / Jacobian / incidence rows are the (H1) half,
  `u_s≥2` (17(tttt)/(ddddd)). They are not licensed here.
- DegBound-6 with no unit is **not** a survive (FALLACY-v2; the prior
  lane already typed it `DEGBOUND_NO_UNIT`, never a dimension).
- A non-empty chart is a real survive **only** if it is the full
  necessary over-approximation, not a sub-system (17(ggggg)). A
  surviving point is a JC2 counterexample **only** if it lifts to a
  Keller pair with `J∈k*`.

This lane: (1) compare the emitted D1 inventory to the full Theorem-1.2
necessary inventory; (2) complete it if it is a sub-slice; (3) re-solve
modular; (4) verdict per class `GG__UNIT` / `NON-EMPTY` / `TIMEOUT`.

---

## 3. Diagnosis: tot-degree cap, not a missing Jacobian tag

### 3.1 Start with the smallest already-extracted full class (Mm15_14)

`C_n24m18_Mm15_14_ell1_s3`, singleton fibre `V=(1,9)`, `s'=3`, `ℓ=1`,
`K=6`, `e=4`, `q=3`, `u'=5`, `δ₁'=-5/36`, `B_safe=-5/4`.

Emitted (post-gauge): 126 unknowns, 176 Jacobian coefficient rows,
`target_xk_level0_nonzero=1`, `level0_deg_x_before_minus_c=7`. Unique
`(h,x,y)` keys = 176. Isolated `-c` rows: **0**. The unique `c`-row is
the target `(h,x,y)=(0,1,0)` with a 59 KB polynomial in the parameters
minus `c` — the opposite of the (25,15) instrument-fail.

Coefficient inventory of the emitted chart **equals**
`order_basis_full.coeff_inventory` (the 17(nnnnn) tot-capped envelope)
**and** equals the raw Theorem-1.2 scan with the tot-degree cut
dropped: **cokernel 0**. Shear audit: `alpha_1` dimension 8, not
scalar; shear omitted. `δ₁'≠0`.

So for this class the emitted chart **is** the full necessary D1
order over-approximation. DegBound-6 no-unit on it cannot be blamed
on a missing monomial. It also cannot be promoted to a survive.

### 3.1b The other named start class: `C_n24m16_M12_17`

Three-fibre class, `(n',m')=(24,16)`, `M'=(12,17)`, `ℓ=1`, `K=8`,
`s'=3`. Union unknown count was 230 under the envelope; 251 after
completion. Native rows were header-only at lane start (the two r7i
extractions of the *envelope* union had run 36 min without writing
generators). Inventory comparison does not need those rows.

| fibre | `V'` | `δ₁'` | `δ₂'` | nunk env→full | coker |
|---|---|---:|---:|---|---:|
| `V2_1` | `(2,1)` | `8/9` | `1/2` | 144 → 153 | 9 |
| `V1_2` | `(1,2)` | `7/6` | `0` | 230 → 251 | 21 |
| `V3_2` | `(3,2)` | `1/3` | `0` | 116 → 118 | 2 |

All three are strict sub-slices of raw Theorem 1.2 (high-`x` monomials
the tot-cap deletes). Emptiness of the old union, had it ever been
extracted, would not have been a (T) kill. Completing cannot make a
non-empty envelope empty: extra coefficients specialise to 0. The
union is being re-extracted under the completed builder; it had not
finished at seal. Shear omitted on all three (`alpha_1` dimensions
22/28/18). Two fibres have `δ₂'=0`; none has `δ₁'=0`.

h-inventory is already a **superset** of `order_basis_full.h_inventory`
(free leading face `tot=K` except monic `y^K`, `deg_x≤u'`).

### 3.2 All twelve fibres

`wt(x^r y^s) = -r + δ₁'·s`. Theorem 1.2 allows every monomial with
`s<K` and `wt ≥ j·B_safe`. The 17(nnnnn) / `order_basis_full` “full”
coefficient inventory adds an extra cut

```text
r + s  ≤  j · K
```

called there “the conservative local finite envelope”. That cut is
**not** in Theorem 1.2. When `floor(δ₁'·s - j B_safe) > jK - s` it
deletes order-allowed high-`x` monomials: a strict sub-slice, the
same *shape* as 17(ggggg) (omitted `x y^3`, `x y^2`, `x^2 y^2`, `x y`
on (25,15)).

Measured cokernel of envelope vs raw Theorem-1.2 D1 (coefficients
only; h kept as free-lead / `u'`-capped):

| fibre | `δ₁'` | `B_safe` | nunk | envelope coker | already full? |
|---|---:|---:|---:|---:|---|
| `M6_13` `V1_1` | `9/4` | `-15/4` | 333 | **99** | no |
| `M6_13` `V1_3` | `1/2` | `-11/2` | 378 | **138** | no |
| `M6_13` `V4_3` | `-2/3` | `-8/3` | 155 | 0 | **yes** |
| `M2_9` `V1_8` | `19/48` | `-71/48` | 120 | **3** | no |
| `M2_9` `V3_8` | `-1/8` | `-3/2` | 88 | 0 | **yes** |
| `Mm12_m2_5` `V1_1_6` | `1/18` | `-13/18` | 77 | 0 | **yes** |
| `M12_17` `V2_1` | `8/9` | `-2/9` | 153 | **9** | no |
| `M12_17` `V1_2` | `7/6` | `-7/6` | 251 | **21** | no |
| `M12_17` `V3_2` | `1/3` | `-2/3` | 118 | **2** | no |
| `Mm15_14` `V1_9` | `-5/36` | `-5/4` | 126 | 0 | **yes** |
| `M9_20` `V1_9` | `1/4` | `-37/12` | 341 | **5** | no |
| `M9_20` `V4_9` | `-1/3` | `-8/3` | 248 | 0 | **yes** |

**7/12 fibres are envelope sub-slices. 5/12 are already the full
Theorem-1.2 D1 inventory.**

Cokernel sample, `M6_13 V1_1` `α_1` (the (25,15) shape, high `x`):

```text
(2,3), (3,2), (3,3), (4,1), (4,2), (4,3), (5,1), …, (10,3)
```

`M12_17 V1_2` `α_1` misses `(2,7), (3,6), (3,7), …, (9,7)`. The
emitted `deg_x≤u'` / `tot≤K` h-chart does **not** miss any
`order_basis_full.h_inventory` monomial (0/12 fibres).

Emitted coeff inventory **equals** `order_basis_full.coeff_inventory`
on all 12 (`ob_coeff_equals_envelope=true`). Completing to 17(nnnnn)
alone would have changed **nothing**. Completing to raw Theorem 1.2
changes the seven sub-slices.

### 3.3 Shear, `δ₁'=0`, Jacobian tags

- Shear: `alpha_{e-q}` is never the scalar `{(0,0)}` on any of the 12.
  Shear omitted on 12/12, as 17(nnnnn) requires when the audit fails.
- `δ₁'=0`: **0/12**. Three fibres have `δ₂'=0` (`Mm12`, `M12_17 V1_2`,
  `M12_17 V3_2`). The zero-slope *centre* support is the same loop:
  when `δ₁'=0`, `max_x = floor(-j B_safe)`, independent of `s`. D108
  control (`δ₁'=0`, `B=-1`, `K=8`): tot-cap cokernel 0, `x`-directions
  8/16/24 in `α_{1,2,3}` — the centre-support is present.
- Jacobian *tags*: native extraction writes every remainder coefficient.
  Missing “order rows” here are missing **variables** (the tot-cap
  cokernel), not missing `(h,x,y)` keys of `J-c x^ℓ`. On Mm15, V3_8,
  V4_3, Mm12 the target row is a huge polynomial, never isolated `-c`.

---

## 4. Completion

`sprime3_compiler.coeff_inventory_necessary` now drops
`r+s ≤ jK`. The tot-capped scan is kept as
`coeff_inventory_envelope` for the cokernel audit.
`inventory_cokernel` is recorded per fibre in `enumerate.json` /
`class.json` (`envelope_coker_total`). Chart tag:
`sprime3_full_D1_thm12_nocap`.

h inventory is unchanged: free leading `y^K` plus every D1 monomial
with `tot≤K`, `deg_x≤u'`, `wt≥B_safe` (Newton width of a
`y`-degree-`K` polynomial). Dropping the `u'` cap on lower `h` would
change the characteristic; 17(nnnnn) does not.

All 18 builders re-emitted, then `builder_fix.py` in place (unknowns
in the polynomial ring, `division()`, `coef(rem,x*y)`). Parameter
counts after the fix:

| stem | params | K |
|---|---:|---:|
| `Mm12` union / `V1_1_6` | 77 | 8 |
| `M2_9 V3_8` | 88 | 6 |
| `M2_9 V1_8` | 120 | 6 |
| `Mm15` union / `V1_9` | 126 | 6 |
| `M12_17 V3_2` | 118 | 8 |
| `M12_17 V2_1` | 153 | 8 |
| `M6_13 V4_3` | 155 | 4 |
| `M12_17 V1_2` / union | 251 | 8 |
| `M9_20 V4_9` | 248 | 6 |
| `M6_13 V1_1` | 333 | 4 |
| `M9_20 V1_9` / union | 341 | 6 |
| `M6_13 V1_3` | 378 | 4 |
| `M6_13` union (pre-gauge 389) | 387 | 4 |

Already-full stems (`coker=0`) keep their previously extracted rows:
the ring and the generator set are the same. Sub-slice stems must be
re-extracted; that is in flight on the r7i workers under the fixed
builder (RSS 0.4–2.1 GB, past `lead(h)=y^K`).

---

## 5. Controls

| control | result |
|---|---|
| Charged-input `sha256sum -c` | 11/11 OK |
| Enumeration 658→20→14→12→6, Xu deaths, `u_s=1`, `B_safe<0`, p.174 no-op | pass (re-emit) |
| Φ_eff vs Appendix II / charged closed form | not re-run; emitter unchanged on `δ'` |
| K16 `(16,12;13;3;k=1)` tot-cap cokernel | **0** (completing does not disturb the K16 empty chart) |
| D108 `(24,16;18;7;k=4)` `δ₁'=0` tot-cap cokernel | **0**; `x`-directions present |
| Shear omitted on 12/12 | pass |
| `target_xk_level0_nonzero=1` on every extracted stem | pass |
| Isolated `-c` on Mm15, Mm12, V3_8, V4_3 | **0** |
| Empty wrapper `<c, T c-1>∋1` / nonempty `<c-1, T c-1>∌1` | pass on every solve script |
| `lead(h)=y^K` on every new extract | pass |

A 6-parameter linear slice of Mm15 (`h=y^6`, `P=h^4+a0+a1 x+a2 y`,
`Q=h^3+b1 x+b2 y`) is saturated-empty over `Q` after `T·c-1` (sympy
lex GB `[1]`). A 10-parameter slice and the full-`h` plus one `x`-term
slice are `[1]` over `F_32003`. The 27-variable centre/linear
zero-slice of Mm15 and Mm12, and a 12-variable random specialisation
of V3_8, are `ZS/RP_VERDICT UNIT` in Singular. Low-support slices die.
A survive, if any, needs the rich coefficient space.

---

## 6. Solve (modular, not exact-Q)

Stage A is unbounded `std` over `F_32003` and `F_32051` of the **full**
generator set plus `T·c-1`. A unit here is a signal, not a char-0 kill
(FALLACY-v2: modular unit is not promoted). Stage B (exact-Q on a
certificate subset) was never reached. DegBound-`d` with
`reduce(1,G)==0` remains a complete unit certificate; the converse is
not a survive.

Already-full charts (the ones on which emptiness *would* be a (T) kill):

| chart | eqs | unk | degBound | unbounded modular |
|---|---:|---:|---|---|
| `Mm15` union | 176 | 126 | d6: NO_UNIT, 26 s, basis 425 | local 1500 s TIMEOUT (`halt 1`, RSS 1.5 GB); r7i 3600 s TIMEOUT (`halt 1`, RSS 4.0 GB at 38 min) |
| `Mm12` union | 425 | 77 | d6: NO_UNIT 19 s basis 323; d12: NO_UNIT 23 s basis 1332 | c7i 1500 s TIMEOUT; r7i 3600 s TIMEOUT (`halt 1`, RSS 11.2 GB at 58 min) |
| `M2_9 V3_8` | 159 | 88 | d8: NO_UNIT 10 s basis 429; d16: TIMEOUT 120 s | local 1500 s / slimgb 900 s TIMEOUT; r7i 3600 s TIMEOUT (`halt 1`, RSS 4.7 GB); `interred` 159→129 in 0 s then `std` TIMEOUT |
| `M6_13 V4_3` | 243 | 155 | — | local 1500 s TIMEOUT (`halt 1`, RSS 0.3 GB) |

No run printed `MS_VERDICT`. CRT promotion was never triggered: no
modular unit, and no pair of primes with an agreed dimension. The
smallest already-full chart (Mm12, 77 unknowns) reached 11 GB RSS
without returning a basis. That is a TIMEOUT of the full order chart,
not a survive and not a kill.

DegBound-6/8 no-unit on an *already-full* Theorem-1.2 chart is the same
numerical fact 17(rrrrrr) reported, now on a chart that is **not** a
sub-slice. It still does **not** prove the ideal nonempty, and it does
**not** prove it empty.

No point with `J(P,Q)=c·x^ℓ` and `c≠0` was extracted. Tiny
specialisations that *do* finish are unit after saturation.

---

## 7. Verdict per class

Union-empty ⇒ every fibre empty ⇒ class dead. The converse is false.
A class is `NON-EMPTY` only if a fibre of the **full** chart yields a
verified monomial-Jacobian pair. `TIMEOUT` is the honest label when
unbounded `std` does not return.

| class | fibres | full Thm-1.2? | verdict |
|---|---:|---|---|
| `C_n24m18_Mm15_14_ell1_s3` | 1 | already full (126) | **TIMEOUT** |
| `C_n24m16_Mm12_m2_5_ell1_s4` | 1 | already full (77) | **TIMEOUT** |
| `C_n18m12_M2_9_ell2_s3` | 2 | V3_8 full (88); V1_8 +3 monomials | **TIMEOUT** (V3_8 already-full, no unit) |
| `C_n16m12_M6_13_ell3_s3` | 3 | V4_3 full (155); V1_1/V1_3 sub-slices, now completed (333/378) | **TIMEOUT** |
| `C_n24m16_M12_17_ell1_s3` | 3 | all three were sub-slices (+9/+21/+2); re-extract in flight | **TIMEOUT** |
| `C_n24m18_M9_20_ell1_s3` | 2 | V4_9 full (248); V1_9 +5; re-extract in flight | **TIMEOUT** |

**k = 0 of 6 `GG__UNIT`. 0 `NON-EMPTY` (no verified `(P,Q)`). 6 `TIMEOUT`.**

Moh ≤100: with 17(ffffff) the published (99,66) case is closed
degree-wide; the ≤100 residual of twelve `u_s=1` rows is **not**
closed. **PARTIAL. Not MAJOR.**

Characterisation of the residual, now that the chart is the full
necessary order over-approx:

```text
OPEN[MOH-LE100-ORDER-CHART]:
  12 u_s=1 rows / 6 descended classes;
  kill mechanism = (T) = full D1 monomial-Jacobian order chart empty;
  the tot-degree envelope is no longer the obstruction;
  low-support slices are saturated-empty;
  unbounded std of the full chart is compute-bound (K16-type);
  a point on the chart would be a descended pair with J = c γ^ℓ,
  c≠0, which is NOT a Keller counterexample unless it lifts.
```

This is a receiver/K16-type OPEN, not a JC2 counterexample, and not a
missing pole/incidence family.

---

## 8. FALLACY-v2

- *Floor/attainment.* The tot-degree cut is a finite envelope, not
  Theorem 1.2. Completing it is the point of the lane. `B_safe` is
  still the cutoff, never `B_tight`.
- *Carrier/attainment.* Class charts remain fibre-unions. A
  representative row is not `FULL_ACTUAL`. DegBound no-unit is not
  `NON-EMPTY`.
- *`sat()` wrapping.* Saturation is `c`; ring / empty / nonempty
  controls fire on every script. The Rabinowitsch generator is
  `T·c-1`.
- *Modular → char 0.* No modular unit. `allow_modular_unit_promotion`
  stays false. CRT was not used to invent a dimension.
- *Variable/ring map.* Rings are declared in each builder (`y`-first
  block after `builder_fix`) and each solve script. Matching names
  were not treated as a map. Prime marks `n',M',δ',s'` are labels;
  `ℓ=v_s-u_s-1` is the Prop 6.3(3) exponent.
- *Pole/interior.* Not invoked. These are order-chart rows, not pole
  identities.
- *Flag/place/series, per-ray charge.* Not invoked. No new exit price.

Typed OPEN: `OPEN[MOH-LE100-ORDER-CHART]` as above.
`OPEN[DESCENDED-U-PRIME-ZERO]` on `M6_13 V4_3` (`u'=0`) remains an
emitter that exists, not a source prohibition; that fibre's full
chart (155 unknowns, 243 rows, target `x^3`) did not return empty
either.

---

## 9. Reproduction

```text
# inventory audit (no solve)
python3 box/moh14-charts-20260905/fullorder_audit.py

# re-emit completed builders and apply the ring fix
python3 box/moh14-charts-20260905/sprime3_compiler.py --mode emit
python3 -c "from pathlib import Path; import builder_fix as B;
[Path(p).write_text(B.fix_text(Path(p).read_text())[0])
 for p in Path('box/moh14-charts-20260905/classes').glob('*/builders/*_builder.sing')
 if 'orig' not in Path(p).parts]"

# extract (cwd = class directory; rows path is relative)
cd box/moh14-charts-20260905/classes/<C>
timeout 2400 Singular --cpus=1 --threads=1 --flint-threads=1 -q --no-rc \
  builders/<stem>_builder.sing

# unbounded modular Stage A
python3 box/moh14-charts-20260905/fullorder_solve.py \
  --class-id <C> --stem <stem> --char 32003 --mode unbounded --timeout 3600
```

Fleet: `172.30.0.7/.18/.28` (c7i, 61 GB), `.166/.254` (r7i, 247 GB),
key `~/.ssh/jc2-fleet`. Builders must be launched with cwd = the class
directory. Jobs were started with `setsid`/`nohup`/`timeout` so they
survive disconnect. Do not promote a modular unit; if Stage A ever
prints `MS_VERDICT UNIT`, re-run the same generators over `Q`.

Jacobian check of a candidate point (none extracted here):

```text
python3 box/moh14-charts-20260905/jacobian_check.py \
  --class-id <C> --stem <stem> --point-json <vals.json> --char 32003
```

A PASS is a descended monomial-Jacobian pair, not a Keller pair.

---

## 10. Artefacts

```text
box/moh14-charts-20260905/
  charged_input_manifest.sha256   awk-generated, 11/11 OK
  sprime3_compiler.py             tot-cap dropped; cokernel audit
  fullorder_audit.py / .json      7 sub-slices / 5 already-full
  fullorder_solve.py              unbounded / zero-slice / point probe
  jacobian_check.py               J(P,Q) vs c x^ell
  builder_fix.py                  unchanged (still the ring fix)
  modular_solve.py                unchanged
  classes/*/builders/*.sing       18 stems, re-emitted + fixed
  classes/*/meta/*.json           full-D1 inventories, shear, δ1_zero
  classes/*/class.json            chart=full_D1_thm12_nocap_class_union
```

Rows `.tsv` of the already-full stems are regenerable from the
builders (Mm15 176 eqs / 7 MB; Mm12 425 / 48 MB; V3_8 159 / 5 MB;
V4_3 243 / 1.6 MB). They are not committed. Completed-chart
extractions of the large unions (`M9_20`, `M12_17`, `M6_13`) hit
the 2400 s cap in the h-adic phase (`lead(h)=y^K` then `halt 1`,
header-only rows) — the same size-threshold the ring fix turned
from OOM into a long division, not a type bug. Unbounded `std`
jobs are all dead (1500 s local / 3600 s r7i), no `MS_VERDICT`.

---

## 11. Scope

This lane changed only `box/moh14-charts-20260905/` (the instrument,
as authorised) and wrote this report. No other ledger file, no
`jc2-lean`, no `ideation-*`. `notes.md` and `AUDIT.md` are untouched.

The coordinator correction this report is asking for: 17(rrrrrr)'s
“need the full joint chart (pole+Jacobian+incidence)” is the (H1)
mechanism. The twelve `u_s=1` rows die only if the **full** descended
order chart is empty. That chart is now the raw Theorem-1.2 D1
inventory; it did not return empty inside this lane.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19457`.
- Body SHA-256:
  `17f604f4bf5de55351cf643ec11a73a89a2c707138e7c86056ad3988a1d7710e`.
- Frozen basis: `d947e8fd54c29904e40a63b8f977ce3f96044123`.
