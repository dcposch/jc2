# s'=3 monomial-Jacobian compiler — Moh Appendix II extended by Φ_eff

Lane `moh-sprime3-compiler-grok46-20260905`; adapter grok. Charts:
`box/moh14-charts-20260905/`. Frozen inputs under `/tmp/jc2-lane.gW3iD7/inputs`.

## 0. Verdict first

```text
HEADLINE: the s'=3 compiler is DERIVED and validated; 6 class charts EMITTED.

DONE:
  (1) 12 live rows / 6 classes re-enumerated fail-closed from
      moh_skeleton_full.py.  The 2 Xu-screen deaths of the earlier 14 are
      (90,60; M=(45,80,88); V=(2,5,4)) and V=(3,5,4), IM=43/7 < Im=7.
  (2) Φ_eff closed form for a general descended datum: δ'_i=(ℓ+1)·Def 5.1(3)
      after the p.174 drop.  At s'=2 this is Moh Appendix II p.207 (5/5,
      every column) and the charged order_basis_full.closed_form (5/5).
  (3) Necessary receiver: free leading form + B_safe = V'_2 δ'_1 + u' δ'_{s'}.
      Not a partition / two-point sub-slice (17(ggggg) / FALLACY-v2).
  (4) 6 class-union charts + 12 V'-fallback builders emitted under
      box/moh14-charts-20260905/classes/.  4/6 unions have extracted
      generators and guided_gb exact-Q jobs; 2/6 leave extraction to the
      fleet (180 s native extract timed out; builders stand).

NOT DONE: k of 12 killed inline = 0.  Smallest extracted chart is 77
unknowns / 425 generators / 97 MB.  That is not a <20 min std.  No
UNIT_IDEAL, no POSDIM, no new exit price.
```

The one sentence to carry: Moh's Appendix II table is the s'=2 specialisation
of Φ_eff; the residual of ≤100 after (99,66) and the Xu screen is twelve
`u_s=1` rows whose descended receivers have height 3 (eleven) or 4 (one),
and those receivers are now compiled as necessary over-approximations for
the fleet.

No new exit-price assertion is made, so no `charge_basis` line is licensed.

---

## 1. Frozen-input gate

Manifest generated with `awk` from the
`charged_input_<i>_sha256=` / `charged_input_<i>_basename=` lines of
`xmodel/moh-sprime3-compiler-grok46-20260905.run.v2` (basename precedes
sha256 in the receipt, so the script collects both then emits).  Checked
with `sha256sum -c`.  7/7 `OK`.  No digest was retyped.  Banked at
`box/moh14-charts-20260905/inputs.sha256`.

Workspace `box/moh_skeleton_full.py` is byte-identical to the frozen copy
(`d20bf084…c506c2`).

---

## 2. The 12 rows and the 2 Xu deaths

Independent re-enumeration, 0.68 s, fail-closed:

| source | count |
|---|---:|
| `(1)–(13)` census, `Kmin=2`, `n≤100` | 658 |
| POLY_ODE (`full_tree_polynomial_ode_ok`) | 20 |
| Moh p.202 printed, kept | 6 |
| excess | 14 |
| Xu Cor 5.3 `IM_max < Im_min` | **2 dead** |
| live residual | **12** |
| descended classes `(n',m',M'_{2..s'},ℓ,s')` | **6** |

Xu deaths, replayed here with the promoted `XuBounder` (not a new inequality;
`IM_max < Im_min` is a contradiction with Cor 5.3, not an attainment claim):

| ancestor | `M_2..M_s` | `V` | `IM_max` | `Im_min` |
|---|---|---|---|---|
| (90,60) | 45,80,88 | (2,5,4) | 43/7 | 7 |
| (90,60) | 45,80,88 | (3,5,4) | 43/7 | 7 |

Both are the same characteristic tower.  They are the two rows the 14-row
lane had as `(18,12; M'=9,16)`.  They receive no chart compute.

All 12 live rows have `u_s=1` and `δ_s=−1`, so Prop 6.4 makes the Prop 6.3
radius automatic.  Descent:

```text
n' = n/d_s,  m' = m/d_s,  M'_i = M_i/d_s (i < s),  V'_i = V_i (i < s),
s' = s−1,  ℓ = v_s − u_s − 1,
then drop M_h = n'−1 if present (p.174 Definition–Remark).
```

The p.174 drop is a no-op on all 12 (`M'_{s'} ≠ n'−1` on 12/12).

| # | ancestor | `M,V` | `(n',m')` | `M'_2..M'_{s'}` | `V'` | `s'` | `ℓ` | `K'` | `V'_2` | `u'` | `δ'_{s'}..δ'_1` | `B_safe` |
|---:|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| 1 | (90,60) | 10,45,88; 1,8,4 | (18,12) | 2,9 | 1,8 | 3 | 2 | 6 | 1 | 5 | −3/8, −1/3, 19/48 | −71/48 |
| 2 | (90,60) | 10,45,88; 3,8,4 | (18,12) | 2,9 | 3,8 | 3 | 2 | 6 | 3 | 3 | −3/8, −1/3, −1/8 | −3/2 |
| 3 | (96,72) | −60,56,94; 1,9,3 | (24,18) | −15,14 | 1,9 | 3 | 1 | 6 | 1 | 5 | −2/9, −1/6, −5/36 | −5/4 |
| 4 | (96,72) | 36,80,94; 1,9,3 | (24,18) | 9,20 | 1,9 | 3 | 1 | 6 | 1 | 5 | −2/3, −1/2, 1/4 | −37/12 |
| 5 | (96,72) | 36,80,94; 4,9,3 | (24,18) | 9,20 | 4,9 | 3 | 1 | 6 | 4 | 2 | −2/3, −1/2, −1/3 | −8/3 |
| 6 | (96,72) | 36,78,94; 1,1,5 | (16,12) | 6,13 | 1,1 | 3 | 3 | 4 | 1 | 3 | −2, 3/2, 9/4 | −15/4 |
| 7 | (96,72) | 36,78,94; 1,3,5 | (16,12) | 6,13 | 1,3 | 3 | 3 | 4 | 1 | 3 | −2, −1, 1/2 | −11/2 |
| 8 | (96,72) | 36,78,94; 4,3,5 | (16,12) | 6,13 | 4,3 | 3 | 3 | 4 | 4 | **0** | −2, −1, −2/3 | −8/3 |
| 9 | (96,64) | 48,68,94; 2,1,3 | (24,16) | 12,17 | 2,1 | 3 | 1 | 8 | 2 | 6 | −1/3, 1/2, 8/9 | −2/9 |
| 10 | (96,64) | 48,68,94; 1,2,3 | (24,16) | 12,17 | 1,2 | 3 | 1 | 8 | 1 | 7 | −1/3, 0, 7/6 | −7/6 |
| 11 | (96,64) | 48,68,94; 3,2,3 | (24,16) | 12,17 | 3,2 | 3 | 1 | 8 | 3 | 5 | −1/3, 0, 1/3 | −2/3 |
| 12 | (96,64) | −48,−8,20,94; 1,1,6,3 | (24,16) | −12,−2,5 | 1,1,6 | **4** | 1 | 8 | 1 | 7 | −1/9, −10/99, 0, 1/18 | −13/18 |

`B_safe < 0` on 12/12, so every row is inside the D1 chart's scope.
`B_tight ≥ 0` on rows 6, 9, 10, 11, 12: cutting by `B_tight` would have
declared five rows out of scope.  That is the floor/attainment error the
safe threshold exists to block.

**On the coordinator's "all 12 have s'=3".** Mechanically 11 have `s'=3`
and **one has `s'=4`** (row 12 of the table, the `(24,16; M'=−12,−2,5)`
class).  The p.174 drop does not reduce it (`M'_4=5 ≠ 23=n'−1`).  The
compiler is written for general `s'` and emits that class as a coverage
control, not as an s'=2 Appendix II client.  None of the 12 is an s'=2
receiver.

---

## 3. Φ_eff, and the s'=2 Appendix II boundary

**Def 5.1(3), p.179, `SOURCE-READ` via the charged skeleton (CONTROL 1 of
census-rebase, and the p.207 table):**

```text
          (n − M_i)  Π_{j=i+1}^{s} [ V_j (n − M_j) − d_j ]
δ_i = 1 − ─────────────────────────────────────────────────────
          (n − M_s − 1) Π_{j=i+1}^{s} [ V_j (n − M_{j−1}) − d_j ]
```

**Φ_eff (banked, 17(dd)/(y)):** after Prop 6.3 and the p.174 drop of a
terminal `M_h=n−1`,

```text
δ'_i = (ℓ+1) · Def 5.1(3)(n', M', d', V', s', i).
```

At `s'=2` this is an identity with the charged two-point closed form

```text
R = n' − M'_2 − 1,   Π = e' + q',   u' = K' − V'_2,
δ'_2 = −(ℓ+1)/R,
δ'_1 = (ℓ+1)(Π u' − R) / (R (Π V'_2 − 1)),
B    = V'_2 δ'_1 + u' δ'_2.
```

Checked three ways, all pass:

| control | what | result |
|---|---|---|
| A | Φ_eff vs Moh p.207, 5/5 rows, columns `(n',m',M'_2,V'_2,δ'_2,δ'_1,ℓ)` | **5/5** |
| A | p.174 drop is a no-op on those five | 5/5 |
| A | at `s'=2`, `B_safe = B_tight` | 5/5 |
| A2 | Φ_eff vs `order_basis_full.closed_form` on all five banked s'=2 rows | **5/5** |
| A3 | algebraic specialisation of Def 5.1(3) at `(16,12;13;3;ℓ=1)` | identity |

This is the ℓ-boundary case: Moh's Appendix II table *is* Φ_eff at `s'=2`.
The s'=3 compiler does not replace that table; it evaluates the same formula
on a longer characteristic tower.

At `s'=3`, `(10)/(11)` on the child would be active (they are vacuous at
`s'=2`).  Measured on the 12: all pass, as does child `(12)/(13)`.  That is
**not** a kill: applying the parent's search conditions to the child's
tower is a license question (`OPEN[CHILD-SEARCH-CONDITIONS]`), not a
sourced theorem, and is not used below.

---

## 4. The necessary receiver (not a sub-slice)

Moh Theorem 1.2 is a **lower bound** on `ord a_j(σ)`.  The chart includes
every D1 monomial whose weight meets that bound.  Equality with a sparse
emitted basis is not a theorem (FALLACY-v2 floor/attainment).

**Threshold.** For `s'=2` the charged instrument uses
`B = V'_2 δ'_1 + u' δ'_2`.  At `s'≥3` the `u'` outer roots of `h` sit in
`D'_2,…,D'_{s'}`, so the true order can be as small as
`V'_2 δ'_1 + u' δ'_{s'}`.  Write

```text
B_safe  = V'_2 δ'_1 + u' δ'_{s'}   ≤   B_tight = V'_2 δ'_1 + u' δ'_2.
```

Cutting by `B_tight` omits monomials that the floor permits: a strict
sub-slice.  A `SATURATED-EMPTY` on a sub-slice is not a kill (17(ggggg)).
Every chart here uses `B_safe`.

**Leading form.** Appendix II fixes `y^{V'_2}(y−x)^{u'}` (or the `u'=2`
minor-disc split) only when `δ'_2=−1` (two-point, Lemma 5.3).  On the 12,
`δ'_{s'} ≠ −1`.  The two-point fix is not licensed.  The necessary top
face is monic `y^{K'}` plus every D1 monomial of total degree `≤ K'` other
than `(0,K')`, with `deg_x ≤ max(u',0)`.  That `deg_x` cap *is* the
`y^{V'_2}` condition on the degree-`K'` face.  There is no slope
partition: one chart per row covers every outer-root split.

**Class chart.** Equal `(n',m',M',ℓ)` does not entail equal charts
(`V'_2` changes `δ'` and `u'`).  The class receiver is the **union** of
the V'-fibre inventories.  If that over-approximation is the unit ideal,
every fibre row dies.  A representative row is not `FULL_ACTUAL`.

**Jacobian.** `P = h^{e'} + ∑ α_i h^{e'−i}`, `Q = h^{q'} + ∑_{i≥2} β_i h^{q'−i}`,
`J(P,Q) = c·x^ℓ`, saturate `c≠0` by Rabinowitsch `T·c−1`.  Coefficient
spaces are the full D1 inventories at threshold `j·B_safe`.  Shear is
omitted unless the charged full-basis audit passes (it does not, on these
rows).  Constant translations are kept where the constant monomial is
present.

**`u'=0`.** Row 8 has `V'_2=K'=4`.  The charged s'=2 builder raises on
the empty partition.  Free leading with `deg_x≤0` is a well-defined
y-only chart (4 `h`-monomials, 157 unknowns after gauges).  Whether
`u'=0` is *inadmissible* remains `OPEN[DESCENDED-U-PRIME-ZERO]`; it is
no longer an emitter refusal.

---

## 5. Emitted charts

Driver `box/moh14-charts-20260905/sprime3_compiler.py`.  Each class
directory has: `class.json`; a class-union native builder; per-row V'
builders; `jobs/*_fleet.sh` (stage 1 = extract rows, stage 2 = guided_gb
exact-Q `std`).  Native builders use a cwd-relative rows path and are
replayable.  Parameter counts below are **after** the charged translation
gauges.

| class | `(n',m'; M'; ℓ)` | `s'` | fibre | unk | eqs | builder | rows | guided_gb job |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `C_n16m12_M6_13_ell3_s3` | (16,12; 6,13; 3) | 3 | 3 | 240 | 378 | 17,116 | 46,351,438 | 92,791,723 |
| `C_n18m12_M2_9_ell2_s3` | (18,12; 2,9; 2) | 3 | 2 | 119 | 333 | 12,787 | 80,258,778 | 160,595,416 |
| `C_n24m16_M12_17_ell1_s3` | (24,16; 12,17; 1) | 3 | 3 | 230 | — | 16,132 | fleet | fleet extracts |
| `C_n24m16_Mm12_m2_5_ell1_s4` | (24,16; −12,−2,5; 1) | 4 | 1 | 77 | 425 | 12,555 | 48,494,347 | 97,087,144 |
| `C_n24m18_Mm15_14_ell1_s3` | (24,18; −15,14; 1) | 3 | 1 | 126 | 176 | 15,235 | 7,076,295 | 14,195,064 |
| `C_n24m18_M9_20_ell1_s3` | (24,18; 9,20; 1) | 3 | 2 | 336 | — | 20,122 | fleet | fleet extracts |

Native gate on every extracted union: `target_xk_level0_nonzero=1` (the
target monomial `x^ℓ` is present at level 0; the chart is not vacuously
killing itself).  Two unions (`(24,16;12,17)` and `(24,18;9,20)`) timed
out at 180 s of native extraction; incomplete header-only row files were
**deleted** so they cannot be run as empty systems.  Their builders remain
the replayable jobs.

Twelve V'-fallback builders sit next to the unions (one per live row).
Ring: `Q(h_{a,b}, A{i}_{a,b}, B{i}_{a,b}, c)[y,x]` for extraction, then
`Q[parameters, T]` for the guided job, `dp`, characteristic 0.
Saturation `T·c−1`.  Promotion scope `EXACT_Q` only; modular unit ideals
are not promoted (`guided_gb` default).

---

## 6. Sanity, and why nothing was killed inline

**Python controls.** Appendix II 5/5, charged closed form 5/5, s'=2
algebraic identity, enumeration 658→20→14→12→6, Xu deaths identified,
`u_s=1` / `B_safe<0` / p.174 no-op on 12/12.  All pass.

**guided_gb wrapper (not a Moh chart).** `<c, T·c−1>` is the unit ideal;
`<c−1, T·c−1>` is nonempty.  Both fire in 0.0 s.
`box/moh14-charts-20260905/controls/`.

**Smallest extracted chart.** The s'=4 singleton, 77 unknowns, 425
equations, builder 6.2 s, guided job 97 MB.  The 14-row lane already
timed out a 76-unknown / 500-generator cone seed at 400 s.  This is not
a `<20 min` std.  The next-smallest extracted s'=3 union is `(18,12;2,9)`,
119 unknowns / 333 equations / 161 MB.  Same conclusion.  **No std was
launched on any class chart.**

`k of 12 killed inline = 0`.  The two Xu deaths are screen deaths of the
old 14, not chart deaths of the 12.

---

## 7. FALLACY-v2 ledger

* *Floor/attainment.* `B_safe` throughout.  `B_tight` is recorded and
  never used as a cutoff.  Theorem 1.2 is a lower bound; the chart is an
  over-approximation of the D1 support.
* *Carrier/attainment.* Class charts are fibre-unions, not a
  representative row.  12 is the live residual after promoted screens,
  not twelve Keller pairs.
* *Variable/ring map.* Ring, generator order, and `Q` are declared in
  each builder and each guided job.  Matching names were not treated as a
  map.
* *`sat()` wrapping.* Saturation is `c`; ring / empty / nonempty controls
  are in every guided prelude.  Cone dehomogenisation `(I,c−1)` is **not**
  used: free leading monomials of total degree `K'` have weight 0, so
  positive-weight properness is unavailable.
* *Prime label / derivative.* `n',M',δ',s'` are descended labels.
  `ℓ=v_s−u_s−1` is the Prop 6.3(3) exponent.
* *Flag/place/series.* Not invoked.  No first-separation charge.
* *Modular → char 0.* No modular run.  `guided_gb` jobs are exact-Q.
* *`POSDIM` is not a witness.* None extracted.

Typed OPENs (nothing below is promoted): the 12 rows remain
`OPEN[MOH-PROGRAM-ARTIFACT]`; `OPEN[DESCENDED-S3-FULL-BASIS]` is now a
fleet job, not an uncompiled residue; `OPEN[DESCENDED-U-PRIME-ZERO]` is
an emitter that exists, not a source prohibition; `OPEN[CHILD-SEARCH-CONDITIONS]`
as above.  Degree-wide `(99,66)` is untouched.

---

## 8. Artifacts

```text
box/moh14-charts-20260905/
  inputs.sha256              awk-generated, 7/7 OK
  sprime3_compiler.py        closed form + enumerator + emitter
  enumerate.json             14 − 2 Xu, 12 live, descended data
  classes_manifest.json      6 class summaries
  controls/sanity_{unit,live}.sing   guided_gb wrapper
  classes/C_n16m12_M6_13_ell3_s3/         (16,12;3)  240 unk, 378 eqs
  classes/C_n18m12_M2_9_ell2_s3/          (18,12;2)  119 unk, 333 eqs
  classes/C_n24m16_M12_17_ell1_s3/        (24,16;1)  230 unk, builder only
  classes/C_n24m16_Mm12_m2_5_ell1_s4/     (24,16;1) s'=4  77 unk, 425 eqs
  classes/C_n24m18_Mm15_14_ell1_s3/       (24,18;1)  126 unk, 176 eqs
  classes/C_n24m18_M9_20_ell1_s3/         (24,18;1)  336 unk, builder only
```

Replay a class on the fleet: `jobs/<stem>_fleet.sh`, then
`timeout 3600 Singular --cpus=1 --threads=1 --flint-threads=1 -q --no-rc
jobs/<stem>_Q_guided.sing`.  Markers: `GG__UNIT main 1` =
`UNIT_IDEAL_CHAR0`; `GG__DIM main k` with `k>0` = `POSDIM` (not a pair).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15022`.
- Body SHA-256:
  `a66aef10e01c08b1273cad2408c980297ff0401f30a55950d9982bc5a79507cb`.
- Frozen basis: `e7079e10ac6d2a5be8c93f4cfbb0bb1b97c5816c`.
