# Hostile gate: small receiver B reconstruction, all residuals retained (Fable 5.1, 2026-09-06)

Status: **GATE COMPLETE**, 2026-09-06 23:36 UTC. Charged report SHA `cd2792c8ec4fdbd286fe7925f36739337ea621eb69d5ea8df90a7cd5804c82bf` (MATCH). Frozen inputs only; no live file, ledger, tool, adapter, protected project, CAS, AWS, solver or A-dependent expansion was touched. Every own control is standard-library exact arithmetic, under 5 s wall, 5 s CPU, 40 MB.

## Verdict table

| claim | verdict | where |
|---|---|---|
| H quintic has a simple rational root −1 in both exact fields, `h'(−1)=3` / `ρ²` | **CONFIRMED** | §2 |
| homogeneous `[H³,C]=0` ⇒ `5|d` and `C ∈ k·H^(d/5)`; kernel zero otherwise | **CONFIRMED**, own proof plus unrestricted nullspaces d=1..25 | §2 |
| literal free B_d columns are `0..q_d` with the three formulas after full outer/inner-face removal (zero slots included); counts 71/196, 77/214, 98/269 | **CONFIRMED** by half-plane lattices | §3 |
| known K_d face terms are the only inner slots below degree 25 and enter as forcing | **CONFIRMED** (slots by code, coefficients by hand against the preflight); forcing vector itself exercised by no checker, by design | §3 |
| H^r, r=1..4, lie in the free columns strictly below the B faces | **CONFIRMED** | §3 |
| entry `(pd−15i)h_p`, `p=r+1−i`; at most 38×15 | **CONFIRMED** against a direct bracket | §4 |
| triangular pivots −15i; extra Schur pivot is a field unit; minor `(−15)^q q! S_d`; ranks 192/210/265 in both fields and both embeddings | **CONFIRMED** by Gaussian minors and regular-representation ranks | §4 |
| the frozen file retains 144 **exact** witnesses over Q/Q(ρ) | **REFUTED in part**: 57 of 144 `nonzero_minor` entries are IEEE floats, none recovers the exact integer; all 144 Schur values, rows, ranks are exact | §4 |
| mod 101, ρ=24 is rank crosscheck only | **CONFIRMED** | §4 |
| descent d=24..1 uses J degrees 37..14; degrees 0..13, unselected rows, degree-2 target, c guard, 105 lift rows all retained; degree 38 is the identity `[H³,H⁵]=0` | **CONFIRMED** (row bookkeeping below; identity by direct bracket) | §5 |
| exact graph quotient, four kernel scalars, no parameter denominator | **CONFIRMED** as algebra; expanded size unmeasured, as the report says | §5 |
| `B→B−[π^15]B·A` is a whole target shear: kills the degree-15 kernel coordinate, changes lower coefficients, preserves faces/origin/monicity/c and the 105-row ideal via `Q_rows −= s·P_rows` | **CONFIRMED** | §6 |
| same-field affine-line splitting, nonemptiness equivalence, counts 76/84/105 with both λ | **CONFIRMED** | §6 |
| no Hermite savings, fill-shrink, necessity, properness or exclusion claimed | **CONFIRMED** (none present) | §7 |
| normal and `-O` checker pass; nonprimitive-H and false-kernel mutations reject in both modes | **CONFIRMED** (six runs) | §7 |
| root transaction, 3 source + 5 owned pins, manifest `341f71e4…` | **GAP**: manifest and owned-box pins are not among the frozen inputs, so they are unverified here | §1 |

## 1. Inputs and method

The eight frozen files hash as in the charge; the three source pins quoted in the report (`7dec79af…`, `cd69c238…`, `e0debc7d…`) match the frozen composition, gate and preflight. `check.py` (`5a3cc285…`) and `exact-witnesses.json` (`9551e720…`) are the owned artifacts. The manifest and the owned-box registration are not in the frozen set; that pin is a GAP, not a defect.

My checker `gate_own.py` (SHA `e0c01f7b…`, in `box/d125-b-reconstruction-gate-fable5-20260906/`) uses derivations different from the producer's: lattice membership by half-plane inequalities instead of edge cross products; rank over Q(ρ) by the 2×2 regular representation over Q (rank halved), plus the conjugate embedding ρ→3−ρ; selected minors by Gaussian determinant, not by the recurrence; Schur complements by forward substitution on the triangular block; kernels by an exact nullspace of the **unrestricted** homogeneous matrix (all d+1 columns, d=1..25) rather than the free-column matrix; the top identity and the matrix entries by an explicit bracket routine. It never reads a live file and never builds any A-dependent row.

## 2. Kernel theorem

Own derivation. With `H=γ⁵h(z)`, `C=γ^d c(z)`, `z=π/γ`: `H_γ=γ⁴(5h−zh')`, `H_π=γ⁴h'`, `C_γ=γ^(d−1)(dc−zc')`, `C_π=γ^(d−1)c'`, so `[H,C]=γ^(d+3)(5hc'−dh'c)`; the `zh'c'` terms cancel. At a simple root z₀ of h with `m=ord_{z₀}c`: if m=0 the right side has order 0 with nonzero coefficient `d·h'(z₀)·c(z₀)`, contradiction; if m≥1 both sides have order m with leading coefficients `5h'(z₀)m c_m` and `d h'(z₀) c_m`, so `5m=d`. Then `(c/h^r)'=h^(r−1)(hc'−rh'c)/h^(2r)=0`, and in characteristic zero `c=λh^r` with λ in the ground field of c. `[H³,C]=3H²[H,C]` in a domain gives the same kernel. The argument works verbatim over any extension of k containing −1, so it covers algebraically closed points.

Code: `h(−1)=0`, `h'(−1)=3` (rational) and `ρ²=3ρ−1` (golden) by own Horner on `z²S(1,z)`, both units. The golden factored form expands to `π⁵+(3−2ρ)γπ⁴+(2−ρ)γ²π³+ργ³π²`, so κ=ρ. Unrestricted nullspaces in both branches: dimension 0 at every d≤25 with 5∤d, dimension 1 at d=5,10,15,20,25 with the basis vector a scalar multiple of H^(d/5). The mutation H=π⁵ produces a kernel already at d=1 and is rejected. **CONFIRMED.**

## 3. Faces, free columns, K_d, H^r

Half-plane lattices `{i,j≥0, i+j≤D, w(i,j)≤W}` with `w=5i−7j`, `i−j`, `i` and `(W_A,W_B)=(3,5),(3,5),(9,15)` reproduce: outer faces 10 A and 16 B points; inner faces 2/3, 7/11, 7/11 points; free counts 71/196, 77/214, 98/269; the preflight's 267/293/369 ring variables after adding c,z in the common cases. Removing origin, every outer point (degree 15/25, zero-prescribed slots included) and every inner point leaves, at each 1≤d≤24, exactly the columns `i=0..q_d` with `q_d=⌊(7d+4)/12⌋`, `min(d,⌊(d+4)/2⌋)`, `min(d,14)`. Derivation: the B constraint at degree d reads `12i≤7d+5`, `2i≤d+5`, `i≤15`; the on-face top point is dropped exactly when the bound is attained, which the three formulas encode. Perturbing the unequal formula to `⌊(7d+5)/12⌋` is rejected at d=1. **CONFIRMED.**

The inner B slots below degree 25 are exactly `(1,0),(8,5)`; `(5+j,j)`, j≤9; `(15,j)`, j≤9 (code). The preflight gives `B_in=(5/(9κ))γ+(5κ²/3)γ⁸π⁵+κ⁵γ¹⁵π¹⁰` and `B_in=κ⁵G⁵` with `G=γ(γπ−1)²`, `γ³(π−1)²`; expanding `γ⁵(γπ−1)^10` and `γ¹⁵(π−1)^10` by the binomial theorem gives `κ⁵·C(10,j)(−1)^(10−j)` at those slots, matching the report's K_d, with j=10 the fixed corner κ⁵. So the report's K_d are the correct forcing constants. No checker (theirs or mine) evaluates `[H³,K_d]`; that is consistent with the no-expansion boundary but means the forcing vector is a transcription, not a tested object. **CONFIRMED with that note.**

H^r has γ-degree ≤3r at degree 5r; its B-weights are ≤`12·3r−35r=r`, `2·3r−5r=r`, `3r` — at most 4, 4, 12, strictly below 5, 5, 15 — and `3r≤q_(5r)` in all nine cases (3,6,9,12 against 3/4/5, 6/7/10, 9/9/14, 12/12/14). Code confirms every H^r support lies in the free set. **CONFIRMED.**

## 4. Matrices, pivots, witnesses

For monomials `γ^pπ^(15−p)` and `γ^iπ^(d−i)` the bracket coefficient is `p(d−i)−(15−p)i=pd−15i`, landing at output γ-exponent `p+i−1`; code compares the formula matrix with the direct bracket at d=1,7,24. Rows `0..d+13`, so 38 rows at d=24, and ≤15 columns. Row `i−1`, column `i` has `p=0`, entry `−15i`; columns above the diagonal need `p<0`, so the block is lower triangular. Schur complement of the extra row against that block equals the recurrence residual, so the `(q+1)×(q+1)` minor in column order `1..q,0` is `(−15)^q q!·S_d`. **CONFIRMED.**

Independent results, both branches and the conjugate embedding: rank `n_d−1` exactly at d∈{5,10,15,20}, `n_d` otherwise; sums 192/210/265; for each of the 120 non-kernel witnesses my Gaussian minor equals `(−15)^q q!` times the recorded Schur value, the recorded extra row is the first row ≥q with nonzero Schur complement, and every minor is a unit (norm `a²+3ab+b²≠0`). For the 24 kernel witnesses no extra row exists. ρ=24 satisfies `ρ²−3ρ+1≡0 (mod 101)`, and neither checker uses it for anything but rank. A false kernel vector `(1,1,1,1)` at d=5 is rejected.

**Artifact defect.** The frozen `exact-witnesses.json` is a pretty-printed re-serialisation of the checker's output, not the checker's output: the checker prints compact JSON with exact integers (my runs give `07b4ce88…`, 29 KB), the frozen file is 95 KB, and 57 of its 144 `nonzero_minor` entries hold floats such as `-1.4044064585576255e+21` (6/7/14 rational, 8/8/14 golden, by case). Zero of the 57 round back to the exact integer. All 144 `schur`, `rank`, `extra_row`, `triangular_rows` fields are exact, and the checker recomputes everything at run time without reading the file, so the PASS is unaffected. The statement that the file records every minor "as canonical pairs of rational numbers" is **REFUTED** for those 57 entries; the mathematical claim behind them is CONFIRMED by my own exact minors, and the fix is to re-emit the file from `check.py` directly.

## 5. Descent bookkeeping and retained residuals

Layer `d+13` of `[A,B]` is `Σ_{i+j=d+15}[A_i,B_j]` with `i≤15`; `i=15` gives `[H³,B_d]`, `i<15` gives `j>d`, so no lower B enters. Rows per degree e are `e+1`; degrees 14..37 hold 636 rows, degrees 0..13 hold 105, degree 38 holds 39, total 780 as in the lift gate.

| case | pivots consumed (14..37) | compatibility rows retained (14..37) | rows 0..13 retained | degree 38 |
|---|---:|---:|---:|---:|
| unequal | 192 | 444 | 105 | 39, identically 0 |
| common3 | 210 | 426 | 105 | 39, identically 0 |
| common4 | 265 | 371 | 105 | 39, identically 0 |

`[H³,H⁵]=0` and `[H,H⁴]=0` hold by direct bracket in both branches. The degree-2 target `cγ²` and the guard `zc−1` live in degrees ≤13 and are untouched. Because every pivot minor is a nonzero field constant, each solved coordinate is `x−g` with g polynomial in A, the kernel scalars and higher B blocks, so `k[x,y]/I ≅ k[y]/(I|_{x=g})` with every unsolved row carried through; no localisation appears. That is existence of a circuit only; nothing about its expanded size or CAS cost is claimed or checked. **CONFIRMED.**

## 6. Gauge and lift preservation

Fixture (golden face, random full-support A with `A_15=H³`, B with `B_25=H⁵`): `B'=B−sA`, `s=[π^15]B`, gives `[π^15]B'=0`, `[A,B']=[A,B]`, every degree-25 and weight-5 B slot unchanged, origin absent, `[π^25]B'=1`, and `[π⁵]B'≠[π⁵]B`; deleting `s·H³` alone changes the bracket. Lattice: A ⊂ B polygon, max B-weight of A is 3/3/9 <5/5/15, and `(0,15)` is free in all cases, so `(A,B',s)↦(A,B'+sA)` is a unipotent coordinate automorphism preserving the whole ideal. The lift gate's φ is one ring homomorphism, linear in its argument, so `Q'=Q−sP` and each negative row of Q' is the Q row minus s times the P row (zero outside the 30-slot envelope; my numeric-λ expansion of all 136 A-polygon monomials has negative support inside the 30 P slots, and `LP⊂LQ`, 30⊂75). Hence the 105-row ideal is fixed by an invertible row operation, c and the leader are untouched, and a solution over any field maps to a solution with s=0 over the same field. Counts: 71+3=74, 77+3+2=82, 98+3+2=103; with λ2, λ3 kept, 76/84/105. **CONFIRMED.** The report correctly avoids Hermite savings, fill predictions, necessity, properness and exclusion.

## 7. Controls, custody

Producer `check.py` from the frozen copy: normal and `-O` exit 0 in 0.3–0.4 s, ≤17 MB; `--mutate` and `--mutate-kernel` exit 1 in both modes with the injected messages (0.4–0.8 s, ≤40 MB). Own `gate_own.py`: normal and `-O` exit 0 in 4.8–4.9 s, ≤18 MB; `--mutate-H`, `--mutate-kernel`, `--mutate-q`, `--mutate-minor` exit 1 in both modes at the intended explicit raise. All under `ulimit -v 524288 -t 25`, `timeout 30`. Owned outputs: `gate_own.py`, `own*.out/.err`, `out_*.json`, `err_*.txt`, `input_pins.txt`, all in the owned box only. No process is retained.

**Net:** every mathematical claim of the reconstruction and gauge is CONFIRMED by independent derivations; one artifact claim is REFUTED (57 float-degraded minors in the frozen witness file, exact values re-derived here); the manifest/owned-pin verification is a GAP outside the frozen inputs. Nothing here is a point, a proper ideal, an exclusion or a solver estimate.

<!-- BODY-END -->
