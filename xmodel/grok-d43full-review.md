# Hostile review: fully reconstructed D43 residue-A family (`sol-d43full`)

Reviewer: Grok 4.6 (adversarial verifier). Date: 2026-08-23.
Repo: `/Users/dc/code/math/jc72108`. No git. No file changes except this
review.

Targets: `xmodel/sol-d43full.md`, `cases/d43_full_final_report.json`,
`cases/d43_full_family.py`, plus the banked audit / certificate / floor /
slice / point-bank artifacts. Prior overapproximation:
`SHEET6-DIRECTIONB.md` §10.7–10.8 (86-row compat-only, then 175-row
late-graph-only).

Claim: the fully graph-preserving residue-A D43 family

\[
I_{43}^{\mathrm{full}}=\langle 34\text{ parked},\ 95\text{ graph }6..24,\
89\text{ graph }26..42\rangle\subset\mathbf F_p[184]
\]

is NONEMPTY at \(p\in\{105337,105673\}\), fiber a00pp, \(B=84\) frozen,
with an explicit 184-point passing all 218 generators and the 18-check
`D43_SURVIVOR` gate.

Method: source-read the assembler and the 10.7/10.8 failure mode; recompute
the window census from `S30`; parse both linear GBs; evaluate all 184
point-bank rows and all 34 parked rows at the named points; classify
D25-eliminated coordinates against the 156-graph ring; independently
re-invoke `d43_graph_witness.floor_gate` at both primes. No msolve rerun,
no box01, no re-stream of the ~2.3 GB 175-row files.

---

## Verdict table

| Question | Verdict | What would have flipped it |
|---|---|---|
| Completeness of \(I_{43}^{\mathrm{full}}\) vs the true graph-preserving D43 family | **COMPLETE** | a missing generator class (kernel-only old rows; D21/Row-22/frontier omitted; eliminated D25 names reintroduced without their graph; odd-band or det23 rows that still cut) |
| 95 “old graph” rows = full D21/D23/D25 reconstruction graph, not a subset | **CONFIRMED** as the full even-window graph bands 6–24 | `rung_rows_idx` dropping an eta, or emitting `left_kernel` instead of `rows` |
| 184-variable union ring (28 parked + 156 graph), no nameless reintroduction | **CONFIRMED** | an eliminated D25 name in the 156 with no old-graph occurrence, or parked∩graph nonempty |
| Witness satisfies all 218 generators | **CONFIRMED** (independent replay, both primes) | any of 184 graph or 34 parked rows nonzero at the decoded point |
| Exact-slice → unsliced 184-row vanishing is valid, not a slice artifact | **CONFIRMED** | nonzero frozen nonpivots, or band-42 rows nonzero, or GB nonlinear / `[1]` |
| Survivor/floor gate is the full `D43_SURVIVOR` battery; `s9_nu_ge_43` tests \(\nu\ge 43\); \(\ell^+\ge 37\) is a real window lower bound | **CONFIRMED** (independent `floor_gate` rerun, byte-equal hashes) | `nu_window is None` stubbed, selected residuals a proper subset of `ROWS_CANON`, or ell a hardcoded 37 |
| Scope disclaimers (not A-SCALE, not char-0, not algebraization) | **HONEST** | a hidden unbounded-\(B\) or char-0 claim |

**Completeness: COMPLETE.**
**Witness: SOUND.**

The 10.8 omitted class is present. No second omitted reconstruction layer
was found.

---

## 1. Completeness

### 1.1 What 10.7/10.8 actually dropped

§10.7 NONEMPTY was \(V(34\text{ parked}+52\text{ compat})\) in 172
coordinates: left kernels of rungs 26–42, no graph. Compressed witnesses
failed raw rung 26.

§10.8 restored the 89 late graph rows (175-row presentation, 184-var
header) and still omitted the older reconstruction graph hidden by the
parked D25 quotient. Algebraic points vanished on 175 generators and then
failed `s9_d43_residual_184_zero` with **94** selected old residuals
nonzero, band census

```
6:9, 8:10, 10:9, 12:9, 14:10, 16:9, 18:9, 20:10, 22:10, 24:9.
```

94 was a witness-failure count, not a generator census. Band 16 has 10
window rows; one vanished on that bad point. The generator census is 95.

### 1.2 The 95 rows are the full even-window graph, not a kernel

`load_rung` keeps `rung_kernel(...)[rows]`, i.e. one grouped polynomial
per eta in `rung_rows_idx(k)`, not the left kernel `L`. Independent
recompute from `d43_family2.S30`:

| bands | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 | Σ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| rows | 9 | 10 | 9 | 9 | 10 | 10 | 9 | 10 | 10 | 9 | **95** |

= 76 D21 window (bands 6–20) + 10 Row-22 + 9 band-24 frontier. Late
bands 26–42 independently recompute to 10+10+9+10+10+10+10+10+10 = **89**.
This is the same eta predicate as the jet window (`S30[a] % 6 == k % 6`
and `S30[a] <= k`), not a Schur/compat subset.

Unspecialized checkpoint `expanded_terms` are strictly positive on every
old row (band 6: nine 4-term rows; band 16 last row 6 terms, not 0). The
95 generators exist before specialization.

Late graph / late compat hashes byte-match the §10.8 emission
(`43dc1d54…` / `536e2c3f…` at 105337; `1f72d049…` / `60b20bee…` at
105673). Parked source hashes match the emission’s `parked_sha256`.
uf30 is the documented PIN42 scope pin (`=0`), not a dropped row class.

### 1.3 The 184-ring does not reintroduce D25 names without their graph

Parked cell = 28 names (`FREE` 14 + `DEP` 10 + `FIXED` 4). Graph = 156.
Disjoint, union 184, both certificates.

Every D25-eliminated x-name (44 names, including all 22 shallow pivots,
`tg1_44=x17`, `tg2_44=x25`, `uf24=x69`) occurs in the 156. All 10 deep
tails (`tf1_49/54`, `tf2_49/54`, `tg1_49/54`, `tg2_49/54`, `tg01_54`,
`tg02_54`) and all 10 band-24 frontier directions (levels 51/56) occur
as graph coordinates. No eliminated D25 name is missing from the ring.

Names that appear only in late specialized rows are first-occurrence
tails at rungs ≥ 26 (`tf*_53`, `tf*_55`, … plus `Xf_alpha,Xg_beta` and
rung-42 extras). That is the 10.7 graph, not a second hidden old layer.

The 52 late compat rows are left-kernel combinations of the 89; retaining
them is redundant (270-row presentation). They are not a missing class.

### 1.4 Provenance caveat (not a missing class)

`old_graph_rows_sha256` is computed and stored, then **not** compared to
an independent `raw_rows21` / Row-22 / frontier emission. Late graph is
dual-sourced; old graph is same-checkpoint census + the `S30` formula.
The 95 rows are NF-det23 images of D43 operator bands 6–24, which on the
parked locus are the window graph. That is the right object. It is a
weaker audit than the late-graph byte regression, not a second
overapproximation of the 10.8 kind.

### 1.5 Origin degeneracy of band 10 (not a missing class)

After specializing the certified parked \(\mathbb A^{14}\) origin, **all
9 band-10 rows become the zero polynomial** in the 156 graph variables
(point-bank empty-row count 9, labels `(10, eta)` for the nine etas with
`S30=10`). Unspecialized they have 14–16 terms; `rank_C=0` at band 10.
This is why the exact slice reports 174 stored prefix rows and 165
nonzero solver rows: \(174-9=165\).

At this parked origin those 9 window slots are identities in the graph
coordinates. They remain generators of the unspecialized family. They
are not a dropped class. They must not be advertised as 95 independent
constraints *at this point*.

---

## 2. Witness soundness

### 2.1 Decoder / slice

The banked `.ms` is the band-40 continuation slice: 174 prefix rows, 101
origin-Jacobian pivots at the band-38 center, 43 nonpivots frozen to that
center. Center solves through band 38; 9 prefix rows are nonzero at the
center (the band-40 obstruction of the band-34 point). msolve 0.10.1
returns a 101-element completely linear basis, not `[1]`.

Independent parse, both primes:

- GB variable order = `variables_retained` = 101.
- 22 nonzero GB coordinates, all among the 101; **no frozen nonzero
  nonpivot**. Zero-init of the other 55 graph coordinates in
  `final_certificate` is therefore the correct continuation point, not a
  dropped-center bug.
- GB values equal `graph_156` exactly.
- Slice/bank sha256 match the certificate.

Specialization of the 14 free cell coordinates to 0 is a fiber of the
family. A point of a specialization is a point of the family. Slice
emptiness is correctly *not* claimed as family emptiness; NONEMPTY is
claimed from unsliced replay.

### 2.2 Algebraic replay (independent)

At each named 184-point:

- 184/184 point-bank graph rows evaluate to 0, band-by-band census
  matching 95+89 (including all 10 band-42 rows, which were **not** in
  the 174-row slice).
- 34/34 parked rows evaluate to 0.
- Parked Jacobian rank 14, graph Jacobian rank 111, as reported.
  Subranks only; no global dimension is claimed, and none is confirmed
  here.
- Negative control `tf1_57 += 1` is reported to break 18 graph rows;
  not re-executed (the independent floor gate’s residual-break control
  did fire).

This is not “slice rows vanish, ambient rows untested.” The 10 band-42
rows are an out-of-slice vanishing that the decoder does not impose by
construction; they vanish anyway.

### 2.3 Gate (independent rerun)

`floor_gate` = `eplus43.gate_suite(..., "D43_SURVIVOR")` plus

- `s9_d43_residual_184_zero`: all `ROWS_CANON` (184 selected slots =
  174 through band 40 + 10 band-42) vanish in the rebuilt jet;
- `s9_nu_ge_43`: `nu_window is None`, where `nu_window` is the least
  \(n\in\{0,\ldots,42\}\) with \(V[:30,n]\ne 0\), else `None`. That is
  \(\nu\ge 43\), not a stub;
- `s9_chart_unit_audit`.

Those 3 + 15 `gate_suite` checks = the 18 executable checks. This is
the campaign’s official `D43_SURVIVOR` battery, not a stripped subset.

Independent `floor_gate` at both certificate points: 18/18 PASS,
`selected_residual_nonzero_count = 0`, `nu_window = None`,
`ell_lb_certified = 37`, window rank 125, \(M_2\)-rank 17,
\((\delta_{N_1}^+,\delta_{N_2}^+)=(26,43)\), \(\alpha=\beta=0\).
Matrix / value-array / manifest sha256 **byte-equal** to the banked
floor JSONs.

\(\ell^+\ge 37\) is the brute/fast loss-scan lower bound on the 184×182
window. `e_plus.certified` remains `null`, tag `E_PLUS_CANDIDATE`.
Threshold at D43 is 21; 37 is above it. First possible named Newton
certification remains D75. Not an equality claim.

The 184 selected jet slots are the same \((\eta,\mathrm{band})\)
indexing as the 184 family graph rows (95 old + 89 late). Family
vanishing and jet vanishing are two paths on the same window. That is
exactly the check §10.8 failed.

---

## 3. Scope honesty

The writeup’s negatives are correct and are not hiding a stronger
theorem:

- **Does not disprove A-SCALE.** A-SCALE is the unbounded-\(B\) carrier
  tower \(\kappa=42\cdot 2^r\). This is one modular fiber at frozen
  \(B=84\).
- **Does not lift to char 0.** Two primes, exact \(\mathbf F_p\).
- **Does not algebraize** to a polynomial Keller map, inverse-limit
  germ, or globalization.

Right reading: the fixed-\(B=84\) residue-A a00pp carrier **survives
through D43 mod \(p\)**, on the fully graph-preserving family, with an
explicit full-gate witness at the parked \(\mathbb A^{14}\) origin (one
W-component). D43 is not a first depth kill at this scale.

Residual, scoped, not a completeness hole:

- Witness is the cell origin (`FREE = 0`), not a generic interior of
  the \(\mathbb A^{14}\) cell. §10.7’s reconstructed sequence-point
  emptiness at rung 26 (`rank(A)=8`, `rank([A|b])=9` at free
  values \(1,\ldots,14\)) is a **different point** and is not refuted.
  Family NONEMPTY ≠ every completed D25 point prolongs.
- Equivariance reduces 36 fibers to a00pp; that is campaign doctrine,
  not re-litigated here.
- Local Jacobian subranks 14+111 are not a dimension theorem.

---

## Independent checks performed

- `S30` window census = 95+89.
- Both linear GBs parsed; 101 linear, 22 nonzero, equal to `graph_156`.
- 184/184 point-bank rows and 34/34 parked rows vanish at both points.
- All 44 D25-eliminated x-names, 10 deep tails, 10 frontier directions
  present in the 156.
- Late-graph / compat / parked hashes match the §10.8 emission.
- `floor_gate` rerun both primes; three sha256s match the banked floors.

Not done: msolve rerun; re-NF of raw D21 `VExpr` against
`old_graph_rows_sha256`; box01 checkpoint re-hash.

---

## One-line honest reading

**At frozen \(B=84\), residue-A a00pp, the fully graph-preserving D43
family is NONEMPTY mod \(p\) with a full-gate survivor; this is a live
fixed-scale anti-A-SCALE signal and not a first depth kill, and it does
not disprove A-SCALE, lift to char 0, or algebraize.**
