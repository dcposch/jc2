# Hostile review: D43 §10.7 SPLIT + WTC-1 round-2 naming/multiplicity split

Reviewer: Grok 4.6 (hostile referee, verdict tier). Date: 2026-08-23.
Repo: `/Users/dc/code/math/jc72108`. No git. No file changes except this
review.

Targets:

- (A) `SHEET6-DIRECTIONB.md` §10.7 + `cases/d43_*` residual artifacts.
  Claim: SPLIT — the literal emitted 86-row ideal is NONEMPTY (smooth
  point, dim ≥ 106, both primes), but the graph-preserving D43 family is
  UNRESOLVED (compressed witnesses fail the rung-28 reconstruction gate;
  one reconstructed D25 point is empty already at rung 26).
- (B) `xmodel/sol-wtc1-round2.md`. Claim: the proximity / infinitely-near
  naming half of WTC-1 is PROVED at theorem level; the ordinary
  multiplicities are NOT.

Method: read the stage-2 emitter (`cases/d43_family2.py`) and the residual
drivers as source, not as testimony; independently replay the second-layer
linear Groebner points against the banked witnesses; independently compute
the reconstructed-point rung-26 affine ranks from
`cases/d43_reconstructed_point_p{105337,105673}.pkl`; independently
recompute the Proposition 5.1 Laurent bracket; audit Theorem 2.1 / 3.2 /
4.1 for a hidden appeal to KPC / WTC-ORD. No Singular, no msolve, no
re-ssh to box01, no 1 GB verdict replay, no other repo file modified.

---

## Verdict table

| Target | Claim | Verdict | What would have flipped it |
|---|---|---|---|
| (A) literal 86-row ideal NONEMPTY, smooth dim ≥ 106, both primes | the emitted parked+compat object has a smooth point of local dimension 106 | **CONFIRMED** (artifact-tier, both primes) | a nonzero of the 52-eq slice at the unique F_p point, or a rank defect in the 52 kept Jacobian directions |
| (A) literal-vs-family distinction is real and correctly drawn | stage-2 compression omitted the rung graph equations, so NONEMPTY answers the wrong object | **CONFIRMED** | the 86-row generators implying the 89 raw affine blocks, or the compressed witnesses already satisfying the raw rung-26 rows |
| (A) witnesses fail rung-28 reconstruction | those specific 172-points are not D43 survivors | **CONFIRMED** for the named points. Residual **GAPS** if read as “the compressed component has no graph lift” | the compressed assignment already solving A_26 y = b_26, or a search of the rank-4 fiber producing a later consistent y |
| (A) reconstructed D25 point empty at rung 26 | sound obstruction, not a chart artifact of the 86-row compression | **CONFIRMED** as a completed-point theorem (the 10×16 linear block is already inconsistent). Residual **GAPS** as an A^14-family hint | rank(A)=rank([A\|b]) on that 10×16 block, or emptiness only after an illicit extra freeze that 10.3 would have re-opened and that this block still needs |
| (A) graph-preserving D43 family EMPTY/NONEMPTY | unresolved | **CONFIRMED** as status: still UNRESOLVED. Not a hidden EMPTY | a GB of the 34+89 graph object, or a liftable witness through rung 42 |
| (B) flag / infinitely-near naming + proximity PROVED, not circular, not using the order lemma | Theorem 2.1 / Cor. 2.2 / Prop. 7.2 | **CONFIRMED** as a theorem about a certified exact prefix. Residual **GAPS** only in writeup completeness (Kummer value-group, weak-transform square, generator-change sentence) | a step in the proof that invokes I ⊆ m^A, WTC-ORD, or base-cluster membership |
| (B) ordinary multiplicities NOT proved; that gap is the remaining WTC-1 wall | KPC is necessary and sufficient for WTC-1 | **CONFIRMED** |
| (B) that multiplicity gap is *the* remaining wall for PCC | KPC is necessary for the classical h_p dictionary; PFE remains | **GAPS** (overstatement if unique-wall). KPC is a real remaining PCC wall; it is not the only one | a proof of PFE from KPC, or a proof of PCC from contact-chain transport without concentration |

No claim under review is REFUTED. Target (A)’s NONEMPTY must not be promoted
to a D43 survivor, an eplus43 floor, or a locus theorem. Target (B)’s
naming theorem must not be promoted to WTC-1 or to PCC.

---

## Target (A) — the SPLIT

Load-bearing sentences: `SHEET6-DIRECTIONB.md` §10.7, especially the two
bullets at 2926–2933 and the ledger at 3003–3008; machine record
`cases/d43_residual_final_report.json`.

### A.1 Stage-2 compression genuinely omits the rung graph

`cases/d43_family2.py` does, per rung k = 26, 28, …, 42:

1. split the NF-reduced band affine in the ten first-occurrence tails
   `y_k` (levels k+27 and k+32; plus `(α,β)` at k = 42);
2. factor `A_k = C_k diag(d_j)` with `C_k` constant;
3. emit only a basis of `ker_L(C_k)` as compatibility rows, after
   asserting that those combinations retain no current `y_k`.

The verdict file is `{34 parked D25 rows} + {52 compat rows}`. Header
comment still says “53 compat”; §10.5 already corrected this to 52
(`6+6+5+6+6+6+6+6+5`). The 89 raw affine blocks `A_k y_k = b_k` are not
emitted. That is exactly the D25 pivot/Schur compression, now applied to
rungs whose eliminated coordinates reappear in later “constant” parts.

This is not a documentation slip. The emitter’s fail-closed assertion
`compat row retains rung tail` forbids keeping `y_k` in the *current*
compat row; it does not adjoin the reconstruction `y_k = A_k^+ b_k` for
use by later rungs. Later compat rows therefore treat earlier
first-occurrence tails as free external variables. The solution set of
the 86-row ideal strictly contains the graph-preserving locus whenever
those reconstructions are nontrivial.

### A.2 Literal 86-row NONEMPTY is real

Independent checks, both primes 105337 and 105673:

- `cases/d43_second_layer_p*.out` are 52-element completely linear reduced
  bases, hence a unique F_p-point on the 52×52 slice.
- Parsing those linear forms and reducing against
  `cases/d43_witness_p*_report.json` gives **0 mismatches / 52 equations /
  2 primes**. Sample identities at p = 105337: `tf1_49 ≡ 100804`,
  `x0 ≡ 5477`, `x1 ≡ 100592`, `x13 ≡ 0`, `tf1_53 ≡ 99429`, matching the
  witness byte-for-byte.
- Same match at p = 105673 (`tf1_49 ≡ 84528`, `x0 ≡ 12610`, `x1 ≡ 24888`,
  `x13 ≡ 0`, `tf1_53 ≡ 92566`).
- Each witness has `full_172_point` of **172** keys = 28 parked + 144
  external, as §10.5’s dedup count.

The slice sets the other 92 external coordinates to 0 and keeps 8 Schur
lower variables plus 44 high pivots. A point of a slice is a point of
the ambient. The 52 linear forms in 52 kept variables are a maximal rank
block, so the 52 compatibility equations are independent at the point in
those directions; with only 52 compat equations the Jacobian rank in the
144 external coordinates is exactly 52. Parked rank 14 is the banked D25
A^14 certificate (already CONFIRMED in `xmodel/grok-d25cert-review.md`),
not re-litigated here. Local dimension `172 - 14 - 52 = 106` on this
component follows. Global dimension is at least 106; no upper bound on
other components is claimed, and none is proved.

This pass did not re-stream the ~1 GB `cases43/d43fam_p*_a00pp_verdict.ms`
files (not present locally). The JSON gates
`d43_raw_witness_gate_p*.json` claim 86/86 zeros and
30,993,910 / 30,993,618 terms, hashes `00c9a4…881b6` / `df0af1…48105`.
That replay is supporting, not independently repeated. It is not needed
for NONEMPTY of the compressed object: the 52-eq slice plus the D25
parked vanishing at the named cell already place a point on
V(34 parked + 52 compat).

**CONFIRMED:** the literal emitted ideal is NONEMPTY, both primes, with a
smooth component of dimension 106. Scope: a00pp, residue-A, B-frozen,
no-log, PIN42, W1W2 ≠ 0, mod p ∈ {105337, 105673}.

### A.3 Those witnesses are not D43 survivors

`cases/d43_lift_witness_p*.json`, both primes, same pattern:

- Before any reconstruction, all 10 raw rung-26 rows are nonzero on the
  compressed assignment (`compressed_assignment_raw_nonzero_rows: 10`).
  The point lies on the left-kernel conditions and not on `A_26 y_26 = b_26`.
- The particular RREF section (nonpivots set to 0) solves rung 26 at
  rank 4/4 and changes six coordinates (the four level-53/58 pivots, and
  `tg01_58`, `tg02_58` → 0).
- After that substitution, rung 28 is rank 4/5, i.e. inconsistent.

The first bullet alone already proves the distinction. A graph-preserving
point cannot have 10 nonzero raw rows at the first rung. The 86-row
NONEMPTY therefore answers an overapproximating ideal. It must not enter
an eplus43 floor measurement. §10.7 states this and is right.

**GAPS on a stronger reading.** `d43_lift_witness.py` reconstructs one
section of the rank-4 fiber, not the general 6-dimensional solution of
rung 26. That is enough to reject *these* 172-points. It is not a proof
that no other `y_26` in `ker A_26` makes later rungs consistent while
keeping the remaining compressed coordinates. The document does not
claim that stronger emptiness, and must not be quoted as if it did.

### A.4 Rung-26 emptiness of the reconstructed D25 point is sound

This is a different object from the 86-row witnesses. Driver
`cases/d43_raw_point_system.py --reconstructed` freezes D25
represented/deep/frontier coordinates via
`d25_eplus.reconstruct_point + eplus43.completed_point_v2`, then retains
all 89 pristine rung graph rows. Artifacts:
`d43_reconstructed_point_p*.pkl`, `d43_reconstructed_full_p*.{ms,out,json}`.

Independent computation on both local pickles, no msolve:

```
rung 26: 10 rows, 16 variables, all degree 1
variables: tf1_53, tf1_58, tf2_53, tf2_58,
           tg01_56, tg01_58, tg02_56, tg02_58,
           tg1_51, tg1_53, tg1_56, tg1_58,
           tg2_51, tg2_53, tg2_56, tg2_58
rank(A) = 8, rank([A|b]) = 9
empty row of the 89-row bank: index 58 (the dropped zero row)
```

Identical 8/9 at both primes. So V(the first 10 graph rows) is already
empty in this completed-point chart. The msolve reduced basis `[1]` on
the 88×98 system (0.01 s, both primes) is a corollary, not the evidence.
The 178/178 numeric fidelity gates against eplus43 plus a coefficient
negative control are consistent with “these 89 rows are the jet engine,”
and were not re-run here.

**Is it a chart artifact of the 86-row compression?** No. The 10×16 block
is the raw NF band-26 affine system after D25 reconstruction, not a
left-kernel shadow.

**Is it a completion-chart artifact?** Only in the scoped sense already
admitted. The reconstruction freezes 58 specialized coordinates,
including tf-deep/frontier 49/51/54/56 (frontier values at p = 105337:
`tf1_51 = 4638`, `tf1_56 = 91894`, not implicit zeros). It does *not*
freeze `tg1_51`, `tg2_51`, `tg*_56`; those six directions remain among
the 16 and the 10×16 system is still inconsistent. So emptiness is not
an artifact of zeroing every kernel column. It *is* emptiness of one
completed D25 point (free values 1,…,14 on one W-component), not of the
A^14 cell. §10.7 says this. The 0/42 pointwise search
(`d43_graph_point_search_report.json`) is the same completed-point
object at 21 samples per prime, all STAGE-A inconsistent at bands
26..40; sampling, not a family certificate, and labelled as such.

This matches the 10.3 numeric story (generic interiors fail already at
band 26) without promoting it to scheme-theoretic EMPTY over the cell.

### A.5 What must be re-emitted

The true a00pp graph-preserving D43 family, at the same modular chart
scope, is the zero set of

```
{34 parked D25 rows}  ∪  {all 89 pristine rung graph rows, k = 26..42}
```

in the 172-coordinate ring, with first-occurrence tails `y_k` **retained
as variables** and with the 14 D25-free parameters **not** specialized
to 1,…,14. Drop the one identically-zero graph row if it remains zero
unspecialized; do not drop it by hand after specialization and then
quote 88 as a family count.

Equivalently: 34 parked + 52 compat **plus** the 37 independent
reconstruction equations (`rank C_k` per rung: 4+4+4+4+4+4+4+4+5). The
52 compat rows are linear combinations of the 89 and become redundant
once the 89 are kept. Do not emit compat-only. Do not left-kernel-
eliminate per rung. Do not pass compressed witnesses to eplus43.

A sequential cascade is legal only if each particular solution *and* its
kernel coordinates remain variables consumed by later rungs. The current
lift gate (one RREF section, nonpivots = 0, stop at first 4/5) is a
witness filter, not that cascade.

Until that 34+89 object returns 1 or a liftable point through rung 42,
the family verdict stays UNRESOLVED and `ell+ ≥ 37` is unchanged. The
0/42 samples and the 10×16 inconsistency make EMPTY the expected
outcome; expected is not a Groebner basis.

### A.6 What (A) needs next

1. Re-emit the 34+89 graph object over unspecialized A^14, fiber a00pp,
   both primes. Same PIN42 / no-log / B-frozen chart.
2. Decide EMPTY vs NONEMPTY of *that* ideal, fail-closed on emission
   fidelity (the 178/178 jet replay is the model; it must be rerun on the
   unspecialized rows, not only on one completed point).
3. If NONEMPTY: a graph-lifted witness through rung 42, then and only
   then an eplus43 floor. If EMPTY: a unit in the 34+89 ideal, per
   rank chart, not a sampling census.
4. Do not promote §10.7’s 86-row dimension table (152, 146, …, 106).
   Those dimensions belong to the overapproximation and die at the
   graph-lift gate, as the file already says.

---

## Target (B) — WTC-1 naming vs multiplicities

Load-bearing sentences: `xmodel/sol-wtc1-round2.md` §0 items 1–2, Theorem
2.1, Corollary 2.2, Lemma 3.1, Theorem 3.2, Theorem 4.1, Conjecture KPC,
Conjecture PFE, §10 ledger.

### B.1 The naming theorem does not assume the order lemma

Round 1 isolated four conjectures: WTC-CHART, WTC-ID, WTC-ORD, WTC-DEN.
Round 2 claims the first two are theorems about a certified exact prefix,
and that WTC-ORD + WTC-DEN collapse to one ideal-containment lemma KPC.

Theorem 2.1 constructs, from the packet’s primitive weight and marked
residue root, the composite flag valuation

```
ν̂_λ(H) = (ν(H), ord_{z=λ} res_ν(H)) ∈ Z²_lex
```

pulls it back through the inverse of the exact Laurent prefix (Kummer
restriction in the fractional case), and takes the unique center on
models of the original P² by the valuative criterion. The infinitely-near
point is that center; the blowup word is Zariski’s factorization of a
divisorial valuation of a smooth surface plus the residual closed point
on E; proximity parents are the creators of the exceptional components
through that point. None of this mentions `I ⊆ m^A`, transverse jets,
or membership in either pencil cluster. The integer t (root
multiplicity) names a contact number, not the point. A multiple root is
the same closed point.

KPC / WTC-ORD is the opposite inequality to the easy boundary bound
Lemma 3.1 (`ord I ≤ A`, because A_f(0,r) contains r^A). Theorem 2.1 never
uses Lemma 3.1. Theorem 3.2 uses Theorem 2.1 to *name* the point and
invokes KPC only afterwards, to put that point in both base clusters and
to read `R_p = A`. That is the correct dependency order. Not circular.

Corollary 2.2’s interface rider is honest: Section-4 currently stores
support-only packets, so the theorem does not emit a machine `center_id`.
That is an implementation omission, not a missing existence proof.

### B.2 Residual writeup GAPS (do not flip PROVED)

These are the attacks that stick as completeness complaints, not as
hidden KPC:

1. **Fractional descent is a sketch.** §1.2 argues that a deck element
   stabilizing a nonzero root λ has character 1, hence acts trivially on
   z−λ, hence does not rescale the second flag coordinate. For a Kummer
   action z ↦ χz this is correct at λ ≠ 0 (the map z ↦ z^l is étale
   there, residue ramification index 1). It is not written as a
   value-group / inertia calculation for a general prefix-conjugated
   action, and the file itself flags a future nontrivial-tangential-inertia
   certificate as outside the convention. The nonzero-root restriction is
   load-bearing and must stay.

2. **(0.4) is associated-graded, not Theorem 2.1.** Round-1 WTC-CHART
   item (3.11) was the boundary restriction of the *weak pencil
   numerators*. Round 2 obtains (0.4) from “the leading form is an
   associated-graded residue” plus gcd-stripped pullbacks of the four
   sections. That is the standard “restriction of the weak transform =
   initial form” identification, and it is *not* WTC-ORD (transverse
   jets can only *lower* ordinary order). It is asserted rather than
   drawn as a commutative square of pullbacks through the cut-graph.
   Labelling “WTC-CHART is a consequence of Theorem 2.1” slightly
   oversells: naming/proximity is Theorem 2.1; the boundary orders are
   §1 + §3. Neither step is the order lemma.

3. **The generator-change sentence is a non sequitur.** “Pencil-generator
   changes do not change either two-generated base ideal and hence do not
   change the valuation center.” The flag valuation is built from the
   packet-designated leading forms, not from the ideals. T-const
   preserves the ideals and can change which root a *different* packet
   would have marked. The sentence is harmless only if “allowed change”
   means a change that does not alter the certified face/root. It must
   not be read as identifying the flag center with a base point — that
   identification is KPC, and Theorem 3.2 already says so.

4. **Cut-graph vs toric fan** is existence/uniqueness by valuation
   theory, not an explicit Enriques word. Fine for the theorem; not a
   replacement for the missing Section-4 maps.

None of these is an assumption of KPC. The naming/proximity content of
WTC-CHART / WTC-ID, for a certified exact prefix with the nonzero-root
convention, is a theorem.

### B.3 Contact transport is proved; one-center multiplicities are not

Theorem 4.1 is Noether’s formula along the unique contact of a general
member with E, given A(0,r) = u(r) r^N. Independent check of the
diagnostic example, Proposition 5.1:

```
[P, Q] = -3/2          (exact Q-arithmetic, reproduced)
ord(r^2+x, x^2) = 1
ord(r^3+(3/2)xr, x^3) = 2
predicted packet orders 2, 3
blowup chart x = r x_1:  (r^2+x, x^2) = r(r+x_1, r x_1^2)     → (1,1)
                         (r^3+(3/2)xr, x^3) = r^2(r+(3/2)x_1, r x_1^3) → (2,1)
```

So paired leading powers + both denominator capacities + a constant
Laurent Jacobian do **not** force KPC. The file’s scope restriction
(Laurent, not a polynomial Keller pair, not a full Corollary-7.4 prefix)
is correctly drawn: this kills a local proof template, not JC / PCC /
KPC.

Corollary 4.2 is the right unconditional theorem: two contact-chain
vectors summing to (αT, βT) when denominators survive, with named points
and proximity, without claiming the chains coincide, without claiming
the ratio α:β pointwise, and without claiming a single nonzero entry.
KPC is exactly the extremal, no-splitting case of that identity
(Corollary 4.3). Label CONJECTURE is mandatory.

Theorem 3.2 (WTC-1 ⇔ KPC) is correct as an equivalence of statements
about certified packets, given Theorem 2.1 and (0.4). The “ancestors are
base points else pullback remains invertible” step is standard and sits
after KPC, not before.

### B.4 Multiplicities are a PCC wall, not the PCC wall

`xmodel/sol-pcc-orbits.md` §0 already split the Corollary-7.4 lane into
WTC-1 *and* a second coverage/no-double-counting theorem. Round 2
discharges the identity/no-double-counting *relation* (Definition 7.1 /
Proposition 7.2) once points exist as flags. What PCC still needs from
WTC-1 is the numbers `R_p, S_p` that feed `h_p`. That is KPC.

After KPC one still needs Conjecture PFE,

```
∑_p c_p² ≥ B² − 1
```

on the all-root, occurrence-complete forest, with `c_p` the conservative
point-max of packet weights. Section 8.1: contact splitting has the wrong
quadratic sign (`∑ u_i² = T² − 2∑_{i<j} u_i u_j ≤ T²`). Section 8.2: a
linear all-root law `∑ T_i = B` with no T_i = B cannot reach B²−1.
Proposition 5.1 is worse than synchronized splitting: floors vanish
entirely. So PFE is not a renaming of KPC, and KPC does not imply PFE.

**CONFIRMED:** ordinary multiplicities are the remaining WTC-1 wall, and
they are a necessary remaining wall for the classical PCC dictionary.
**Not confirmed as unique PCC wall.** The honest remainder is KPC + PFE.
A vector-valued substitute that skips KPC would still have to beat the
quadratic defect (8.2)/(8.5); no banked identity does that.

### B.5 What (B) needs next

1. Prove or refute **KPC** for polynomial-origin packets with the full
   eligible Corollary-7.4 prefix. Local face + denominators + cleared
   Jacobian is the wrong template (Prop. 5.1). The file’s two plausible
   sources — eligible-prefix saturation, or canonical-divisor /
   polynomial-origin constraints — are the right attack surface.
2. Independently, prove **PFE** (or a packing-function substitute with
   an explicit local rule). Do not quote linear root-enumeration as
   coverage.
3. Tighten Theorem 2.1’s writeup: drop or repair the generator-change
   sentence; write the weak-transform/residue square for (0.4); record
   the Kummer value-group statement for nonzero roots as a named lemma.
4. Store the exact field maps and conjugate root orbit in Section-4
   certificates, so the naming theorem is executable. That is not a
   remaining existence gap.

Until KPC, WTC-1 stays CONJECTURE. Until KPC + PFE, PCC stays
CONJECTURE, and `td ≤ αβ` with it. The geometric name/proximity problem
is not the obstruction.

---

## Independent checks (this pass)

| Check | Result |
|---|---|
| `d43_family2.py` emits parked + left kernels only | yes; 89 graph rows not in the `.ms` |
| second-layer GB vs witness, 52 eqs × 2 primes | 0 mismatches |
| `full_172_point` key counts | 172 = 28 + 144, both primes |
| reconstructed pkl rung-26 affine ranks | 10×16, deg 1, rank 8/9, both primes |
| leftover kernel-like columns in that 16 | `tg1_51, tg2_51, tg{1,2,01,02}_56` still free; still 8/9 |
| Prop. 5.1 `[P,Q]` over Q | `{(0,0): -3/2}` |
| Prop. 5.1 ordinary orders / blowup vectors | 1,2 and (1,1), (2,1) |
| Theorem 2.1 uses KPC / WTC-ORD / base-cluster membership | no |
| 1 GB streaming replay / msolve / box01 | not repeated |

---

## Scope box (do not quote this review without it)

Everything in (A) is modular, fiber a00pp, residue-A, B-frozen, no-log,
PIN42, W1W2 ≠ 0. Emission-fidelity of future optimized D27+ presentations
remains CONJECTURE FUTURE-EMISSION FIDELITY from `sol-pcc-orbits.md`.
Nothing here is characteristic 0, locus-wide, a germ, a DEPTH e, or an
eplus43 floor. `ell+ ≥ 37` stands.
