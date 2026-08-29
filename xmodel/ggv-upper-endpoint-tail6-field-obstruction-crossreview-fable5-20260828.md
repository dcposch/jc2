# Fable 5 hostile crossreview: cutoff-six square-tail field obstruction

Reviewer: Fable 5, hostile different-model lane (exact certificate review)
Review date: 2026-08-28 (campaign dating; local clock 2026-08-27 evening)
Reviewed report: `xmodel/ggv-upper-endpoint-tail6-field-obstruction-r0-sol-ultra-20260828.md`
Reviewed report sha256: `c62acd1be938b14e10e76c28c6bc45cabf874ed8ef4385d617746fdf104c3101` (matches charge pin)
Frozen case: `cases/ggv_8_28_upper_endpoint_tail6_desk_20260828/`

## Overall verdict

**CONFIRMED.**  Every charged atom passes under a fully independent
standard-library exact-`fractions.Fraction` reconstruction that starts one
level *below* the producer's own compiler: my checker re-derives the entire
p-coordinate constraint system from the pinned upstream
`RAW_DIRECT_SYSTEM.json` plus the frozen nullspace basis (something
`analyze_tail6.py` never does — it trusts `TAIL6/TAIL_DEFORMATION_SYSTEM.json`),
then re-runs every elimination with its own tracked RREF.  All frozen
numbers, spans, signs, witnesses, provenance lists, and the final unit
identity reproduce exactly; both live mutations fail loudly with the
predicted exact nonzero residual polynomials; the producer's documented
`--check` replay passes byte-for-byte with the documented marker.

One point where hostile scrutiny produced a *positive* finding: my first
row-13 run deliberately omitted the row-12 pivot substitutions and got
compatibility span rank 12, not the claimed 9.  This is not a producer
defect — the raw rows occupy a four-wide weight window `[r-3, r]`, so
row-13 equations really do contain stage-12 parameters, and the certified
progressive-substitution semantics are load-bearing.  Re-running with the
producer's exact progressive semantics gives 9 and matches the model
identification.  The same is true at rows 14/15 (verified: plain
`{A=HV, branch}` substitution does **not** reproduce the certified
compatibility lists, and the row-14 pivot substitutions are specifically
load-bearing for the row-15 lists).  The progressive semantics were
therefore audited exactly as charged, and they are implemented correctly.

## Atom-by-atom verdicts

| # | Atom | Verdict |
|---|------|---------|
| 1 | Pins and source geometry (220/260/98/122/253) | CONFIRMED |
| 2 | Endpoint sign `D22[X^0]-1=-1-p32*p110`; `p32=G15[X^1]`, `p110=F7[X^0]` | CONFIRMED |
| 3 | Rows 12/13 field-radical cover (`A=CB`, `B=CV`, `V0∈{0,4p110}`) | CONFIRMED |
| 4 | Rows 14/15 elimination (ranks, pivots, cumulative 19, no divisions) | CONFIRMED |
| 5 | Both sparse `p110^2` witnesses + literal-row provenance | CONFIRMED |
| 6 | Final unit identity + producer replay marker | CONFIRMED |
| 7 | Live mutation with exact nonzero residual | CONFIRMED |
| 8 | Firewall audit (char 0, field vs scheme, fixed baseline, no D23/G22) | CONFIRMED (with custody notes) |

## 1. Hashes and manifest (exact command output)

```text
$ sha256sum xmodel/ggv-upper-endpoint-tail6-field-obstruction-r0-sol-ultra-20260828.md
c62acd1be938b14e10e76c28c6bc45cabf874ed8ef4385d617746fdf104c3101  xmodel/ggv-upper-endpoint-tail6-field-obstruction-r0-sol-ultra-20260828.md

$ cd cases/ggv_8_28_upper_endpoint_tail6_desk_20260828
$ sha256sum UNIT_CERTIFICATE.json analyze_tail6.py TAIL6/TAIL_DEFORMATION_SYSTEM.json
812dc5b7d337dc8a6bb68b5419c4ce0556c2e0ed29e1eb4213d5a79ece3a8269  UNIT_CERTIFICATE.json
86a0c851cea30bb397d4e80bb9cda8a6f50559d5cbc7de649a431960ecd10113  analyze_tail6.py
c038fd929d8c11cf8465dd72edb5fc4cca430140d11199f3c6fbd2f968e1b389  TAIL6/TAIL_DEFORMATION_SYSTEM.json

$ sha256sum -c SOURCE.sha256
TAIL6/TAIL_DEFORMATION_SYSTEM.json: OK
../ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json: OK
../ggv_8_28_upper_endpoint_branch_p_20260827/tail_deformation.py: OK
```

All four charge pins match; every `SOURCE.sha256` line is `OK`.  I also
verified every additional custody hash declared in the producer report
(`RESULT.md` `7481713f…`, `TAIL6_DESK_ANALYSIS.json` `7ed24725…`,
`tail_deformation.py` `a411d661…`, `RAW_DIRECT_SYSTEM.json` `ead2fa40…`,
and both exact-Q target hashes `f2c59134…` / `e458f63f…`), and all six
`TARGETS/*.sing` hashes on disk against
`UNIT_CERTIFICATE.json.emitted_target_sha256` — all match, including the
two `p65521` and two diagnostic files.

## 2. Independence: what was reconstructed vs. custody-checked

My checker (`/tmp/fable5_tail6_check.py`, full source in Appendix C, run
end-to-end in ≈2.4 s) does **not** import or execute `analyze_tail6.py`.
It implements from scratch: sparse multivariate polynomials over `Fraction`
(monomial = sorted int tuple), addition/scaling/multiplication/one-pass
substitution, a single dense RREF routine with first-nonzero pivoting and
optional provenance tracking, span-rank, and in-span witness solving.  The
triangular stages are mechanized differently from the producer (one dense
matrix whose columns are the candidate parameters followed by all residual
monomials, with elimination restricted to the candidate columns), while
deliberately sharing three *conventions* needed for index/hash
comparability, which I disclose: (i) the same first-nonzero-row pivot/swap
convention so displayed-compatibility indices align; (ii) the same
synthetic variable ids (b0..b6 → 1000..1006, v0..v2 → 1100..1102); (iii)
the same compact-JSON serialization for sha256 comparison only.

**Independently reconstructed** (evidence): the retained-variable census
and the 260-equation prefix from `RAW_DIRECT_SYSTEM.json`; prefix rank 98
by my own RREF; validation of the frozen 122-vector nullspace basis
(annihilates all 260 rows; rank 122; hence a complete basis defining the
p-coordinates); the full `raw_value_linear_map` (all 303 variables); all
253 D12..D22 constraints in p-coordinates rebuilt from the raw records and
compared term-by-term and hash-by-hash against the frozen JSON; the
endpoint identity; all four triangular stages on both branches with my own
tracked elimination; the two span-model identifications; the branch cover
algebra; both sparse witnesses (my solver independently *finds the same
sparse witnesses*); all provenance combinations; the unit identity; both
mutations.

**Custody/replay-checked only** (not independent evidence): byte-identity
of `TAIL6_DESK_ANALYSIS.json`, `RESULT.md` prose, and the six unrun
`.sing` coefficient-custody artifacts (via hashes and the producer's
`--check` byte-regeneration); and the upstream provenance of
`RAW_DIRECT_SYSTEM.json` itself (the branch-P square-baseline recurrence
data), which is pinned and was reviewed upstream — this review treats it
as the frozen authority per the charge, but did verify its internal
structure (row census 4..22, single affine constant, `charged_rows`
target `D22=1`, recurrence-consistent weight windows, no weight-22 G slot,
no row 23).

## 3. Atom 1 — pins and source geometry: CONFIRMED

From `RAW_DIRECT_SYSTEM.json` (303 variables, 513 generator records, rows
4..22, record counts per row `{4:36, 5:35, …, 22:18}`), with the weight
convention `weight(f_a_b)=8+3a−b`, `weight(g_a_b)=12+3a−b`, `z_*→2`,
`tt_*→3` (formula verified against all 442 slot records of the upstream
weight source, 0 mismatches):

* retained (weight ≥ 6): **220**, equal as an ordered list to the frozen
  `retained_variables`;
* prefix rows ≤ 11: **260** records; every surviving monomial after
  zeroing weight<6 variables is a bare retained variable (asserted);
* my own RREF over Q: prefix rank **98**, nullity **122**;
* frozen 122-vector nullspace basis: annihilates all 260 prefix rows,
  has rank 122 — a complete basis (this *defines* the p-coordinates);
* remaining rows 12..22: **253** records, and all 253 p-coordinate
  constraints rebuilt from raw match the frozen `constraints` exactly
  (terms, row, x_degree, and per-record sha256): 0 mismatches.

Structural findings worth recording: the raw rows are *not*
weight-homogeneous; pure f/g monomials in row r span the weight window
`[r−3, r]` (consistent with the recorded recurrence
`D_n=Σ_{i+j=n}((12−j)F_i'·G_j+(i−8)F_i·G_j')`).  Consequently 43 of the
122 nullspace vectors have mixed-weight support and the producer's
`stage = min weight of support` convention is the operative one.  The
frozen stage partition reproduces exactly
(`stage12=[57..72]` (16), `stage13=[44..56]` (13), `stage14=[33..43]` (11),
`stage15=[24..32]` (9)), and — importantly for the "16 weight-12
parameters" language — the stage-12/13/14/15 parameters have *pure*
weight supports `[12]/[13]/[14]/[15]` respectively, so calling them
weight-r parameters is exact even though other stages mix.

## 4. Atom 2 — endpoint sign and carriers: CONFIRMED

The literal raw record (row 22, x_degree 0; the only record in the whole
system with a constant term) is

```text
[[[], "-1"], [["f_0_1","g_1_0"], "-1"], [["f_1_0","g_0_1"], "1"]]
```

i.e. `D22[X^0]−1 = −1 − f_0_1·g_1_0 + f_1_0·g_0_1` in raw slots.  My
reconstruction from the verified basis gives, at constraint index 235:

```text
row22/x0  =  (-1)*1 + (-1)*p32*p110
```

The `+f_1_0·g_0_1` term dies because the general prefix solution forces
`g_0_1 ≡ 0` (its parameter form is empty — a pivot variable solved to
zero; `f_1_0 = p77` survives but is multiplied by 0).  The sign was
checked against the raw record, not the serialized certificate.  Label
tracing to source: `forms[f_0_1] = p110` exactly, with
`weight(f_0_1)=8+0−1=7` and x-index 0; the weight-7 F slots are
`f_0_1, f_1_4, …, f_9_28` (x = 0..9), so `F7[X^0] = f_0_1 = p110`.
`forms[g_1_0] = p32` exactly, with `weight(g_1_0)=12+3−0=15` and x-index
1; the weight-15 G slots are `g_1_0, g_2_3, …, g_9_24` (x = 1..9, the
x=0 slot does not exist at weight 15), so `G15[X^1] = g_1_0 = p32`.

Field consequence, with no normalization: the endpoint equation is
`−1−p32·p110 = 0`, i.e. `p32·p110 = −1`.  In any field a product equal to
−1 forces both factors invertible, hence `p32 ≠ 0`, `p110 ≠ 0`, and
`p32 = −p110^{-1}` *as a derived relation at points*.  The certificate
never sets `p110=1` or `p32=−1`; it keeps the polynomial generator
`1+p32·p110` (the `p110=1` files are explicitly non-covering
diagnostics).  No localization enters the certificate.

## 5. Atom 3 — rows 12 and 13 field-radical cover: CONFIRMED

**Row 12** (no substitutions; candidates = the 16 stage-12 parameters):

```text
log12: equations=28 candidates=16 rank=12 pivots=[57..68] free=[69,70,71,72]
       displayed compatibilities=16, compatibility span rank=8
```

Model: with `A = F6 = Σ_{d=0..10} p_{121−d} X^d` (traced from the basis:
`F6[X^d] = p_{121−d}`), `C = X^4−1`, `H = C^2 = X^8−2X^4+1`, my own dense
multiplication and mod-H reduction (`X^8 ≡ 2X^4−1`) give 8 coefficient
polynomials of `A^2 mod H` with `rank(model)=8` and
`rank(compats ∪ model)=8`: **the two Q-spans are equal** (my sample,
X^0 coefficient: `p121² −4p111² −6p111p115 −4p111p119 −6p112p114
−4p112p118 −3p113² −4p113p117 −2p113p121 −4p114p116 −2p114p120 −2p115²
−2p115p119 −2p116p118 −p117²`).  Radical justification (char 0): at a
field point the 16 compatibilities vanish iff all 8 coefficients vanish
iff `H | A^2` in `k[X]`.  `C` is squarefree over char-0 `k`
(`gcd(C, 4X^3)=1`), so for each irreducible factor `π | C`,
`v_π(A^2)=2v_π(A) ≥ 2` forces `v_π(A) ≥ 1`; hence `C | A`, `A = C·B`
with `deg B ≤ 10−4 = 6`.  This is set-theoretic only — `H | A^2` does
*not* imply the scheme-level factorization — and the producer's firewall
says exactly that.

**Row 13** (after `A=C·B`; progressive semantics): substituting `A=C·B`
kills all 16 row-12 compatibilities identically (checked both by direct
substitution into my computed compatibilities and by re-running the
stage: 0 displayed).  Because row-13 equations occupy weight window
`[10,13]` they contain stage-12 parameters, so the row-12 pivot solutions
must be substituted first; with them in force:

```text
log13: equations=27 candidates=13 rank=11 pivots=[44..54] free=[55,56]
       displayed compatibilities=16, compatibility span rank=9
```

(My deliberate non-progressive control run gave span rank 12 — the
progressive substitution is load-bearing and correctly implemented.)
Model: `rank(8 coeffs of B(4·C·F7−B) mod H) = 8`; adding the scalar

```text
E = p110·b0 − (b0b4 + b1b3 + b2b6 + b3b5)/2 − (b2² + b4² + b6²)/4
```

gives rank 9; union with the 16 compatibilities is still rank 9: **the
compatibility span equals the model span + Q·E** (`F7 = Σ p_{110−d}X^d`
traced from the basis).  Reduction mod C (my own `X^4 ≡ 1` reduction):
`(4BCF7 − B²) mod C == −(B²) mod C` — an exact identity — so at a field
point `C | B²`, hence `C | B` by squarefreeness, `B = C·V`, `deg V ≤ 2`.
Substituting `b_d = v_{d−4} − v_d` (my own `B=C·V` map):

```text
E|_{B=CV} = (1/4)·v0² − p110·v0 = V0·(V0 − 4·p110)/4    (exact)
```

At a field point `E = 0`, and a field has no zero divisors, so `V0 = 0`
or `V0 = 4·p110`: **the two branches cover all characteristic-zero
field points** (char ≠ 2 is used by the `/4` and by squarefreeness of C;
char 0 certainly).  These are radical/set-theoretic implications, and
both `RESULT.md` and the producer report firewall them as such; no
scheme identity is claimed across rows 12/13.

## 6. Atom 4 — rows 14/15 elimination: CONFIRMED

Branch pipeline (mirrored progressively, then re-verified): substitutions
`A = H·V` (`p_{121−d} → v_d − 2v_{d−4} + v_{d−8}`), then the recorded
row-12 stage pivots (0 compatibilities, as forced by the exact identity
`(H·V)² mod H = 0`, which I verified symbolically), then the row-13 stage
pivots (4 displayed compatibilities of span rank 1, all becoming
identically zero after the branch substitution `v0 → 0` resp.
`v0 → 4·p110` — verified on both branches), then rows 14 and 15.  Both
branches give identical elimination shape:

```text
log14: equations=26 candidates=11 rank=10 pivots=[33..42] free=[43]
       displayed compatibilities=16, span rank 8
log15: equations=25 candidates=8 (p32 withheld: candidates=[24..31])
       rank=8 pivots=[24..31] free=[]
       displayed compatibilities=17, span rank 17
cumulative span rank(r14+r15) = 19   (8+17−19 = 6 duplicate directions)
```

`p32` is confirmed absent from the row-15 pivot set (all eight other
stage-15 parameters are pivoted; no free candidates remain).  Progressive
substitution is again load-bearing and correct: plain `{A=HV, branch}`
substitution reproduces *neither* the row-14 nor the row-15 compatibility
lists, and specifically re-running row 15 with the row-12/13 pivots but
*without* the row-14 pivots does not reproduce the certified row-15 list
(both branches) — consistent with the certificate's interpretation
sentence and with stage-13/14 parameters appearing in raw rows 14/15
(my leak census: rows 14/15 contain stage-14 params 33–43, stage-13
params 44–56, and stage-12 params 57–68/70–72 resp. 70–72).

No hidden division: in my representation a parameter inverse is not even
expressible; the structural assertion that every candidate occurrence is
a *bare linear monomial with rational coefficient* held at every stage,
so every RREF division is by an explicit nonzero rational scalar; every
substitution image (A=HV, `v0`-branch, pivot solutions) is a polynomial
with rational coefficients; the branch map `v0 → 4·p110` and the unit
multipliers are polynomial.  No division by `p110`, `p32`, or any
parameter occurs anywhere in the pipeline.

Branch targets (19 cumulative-span generators + endpoint):

```text
v0_zero:      generators=20, operative variables=22, max degree=2
v0_four_p110: generators=20, operative variables=23, max degree=2
```

matching `RESULT.md`'s table, and the producer's serialized
`triangular_log` in `TAIL6_DESK_ANALYSIS.json` matches my logs field by
field on every stage of both branches.

## 7. Atom 5 — sparse `p110^2` witnesses and provenance: CONFIRMED

Direct term-by-term expansion with my own arithmetic, on my own
compatibility lists (zero-based indices):

```text
V0=0:        (1/12)r14[1] + (1/9)r14[13] − (2/9)(r15[3]+r15[7]+r15[11]+r15[15])  ==  p110²   True
V0=4·p110:   −r14[9] − (37/9)r14[13] + (16/9)r15[3] + (32/9)r15[7]
             + (256/45)r15[11] + (512/63)r15[15]                                  ==  p110²   True
```

Stronger: my own in-span solver (tracked RREF over the 33 pre-span
compatibilities, no knowledge of the frozen witness) independently
produces *exactly the same sparse witnesses* on both branches:
`{1:1/12, 13:1/9, 19:−2/9, 23:−2/9, 27:−2/9, 31:−2/9}` and
`{9:−1, 13:−37/9, 19:16/9, 23:32/9, 27:256/45, 31:512/63}` in combined
indexing.  All twelve selected compatibility polynomials (full text in
Appendix B; term counts 18/16/43/43/41/35 and 21/17/43/43/40/34) have
sha256 values equal to the certificate's `compatibility_sha256` entries,
with matching coefficients and stage indices.

Provenance: my tracked elimination reconstructs every one of the twelve
selected compatibilities as an exact Q-combination of the substituted
literal source rows of its stage (asserted internally for *all*
compatibilities, not just the selected ones).  Collapsing my provenance
through the witness reproduces the certificate's frozen
`source_row_provenance` exactly:

```text
v0_zero  row14: {58: 7/24, 62: 5/24, 66: 1/12, 78: 1/9}
v0_zero  row15: {84,88,92,96,100,104: all −2/9}
v0_four  row14: {58: 16/3, 62: 2/3, 74: −1, 78: −37/9}
v0_four  row15: {84: −2/9, 88: 4/9, 92: 16/9, 96: 32/9, 100: 256/45, 104: 512/63}
```

(constraint indices in the frozen 253-list; row-14 sources have
x_degrees 3/7/11/19/23, row-15 sources x_degrees 3/7/11/15/19/23 — the
mod-4 structure of `C = X^4−1`).  Applying each collapsed combination to
the *substituted* literal source rows at the correct progressive stage
(row 15 including the row-14 pivot substitutions) reproduces the
corresponding witness part exactly; applying the row-15 combination to
the **unsubstituted** raw p-rows does **not** (checked `False` on both
branches), and row 15 without the row-14 pivots does not reproduce the
certified list either — so the provenance is genuinely
progressive-stage provenance, not raw-row provenance, exactly as the
certificate's interpretation sentence states.  This rules out a
cumulative-span emission artifact: `p110²` is rebuilt from pre-span
lists that are themselves rebuilt from literal source equations.

## 8. Atom 6 — final unit identity and producer replay: CONFIRMED

My own expansion:

```text
(1 − p32·p110)·(1 + p32·p110) + p32²·(p110²)  =  1     (exact, all cross terms cancel)
```

Inputs are genuine members of each branch target: `1+p32·p110` is
literally generator #20 (appended, sign-flipped from the constraint
`−1−p32·p110`, same ideal), and `p110²` is *literally one of the 19
cumulative-basis generators* on both branches (checked; and
independently it reduces to 0 against my span basis, and is a
Q-combination of pre-span compatibilities by Atom 5).  The multipliers
`1−p32·p110` and `p32²` are polynomials; no localization division is
used.  Hence both branch target ideals contain 1 over Q.

Producer replay (documented command, run after all independent checks):

```text
$ python3 cases/ggv_8_28_upper_endpoint_tail6_desk_20260828/analyze_tail6.py \
    --check --output cases/ggv_8_28_upper_endpoint_tail6_desk_20260828
{"check": true, "direct_unit_certificate": "PASS_BOTH_ROW13_BRANCHES_NO_GB", ...}   (exit 0)
```

The decisive marker `"direct_unit_certificate": "PASS_BOTH_ROW13_BRANCHES_NO_GB"`
is present, `"check": true` (byte-identical regeneration of all 9 emitted
payloads, whose hashes in the replay output match the on-disk files and
the certificate's `emitted_target_sha256`).  Full replay JSON in
Appendix A.

## 9. Atom 7 — live mutations: CONFIRMED

Both mutations are in-memory only; the frozen case was not touched.

**(a) Witness-coefficient mutation** (`1/12 → 1/11` on `r14[1]`,
`v0_zero`): the expansion misses `p110²` by exactly
`(1/132)·r14[1]` — the printed exact residual (18 terms):

```text
(6/11)p101p107 + (6/11)p102p106 + (12/11)p102p110 + (6/11)p103p105 + (12/11)p103p109
− (6/11)p103v1 + (3/11)p104² + (12/11)p104p108 − (6/11)p104v2 + (12/11)p105p107
+ (6/11)p106² + (18/11)p106p110 + (18/11)p107p109 − (9/11)p107v1 + (9/11)p108²
− (9/11)p108v2 + (9/11)p110² + (9/44)v2²   ≠ 0
```

**(b) Literal-source-row mutation** (constraint 84 = row 15, x_degree 3,
coefficient of `p110²` increased by 1; row-15 elimination re-run from
scratch on the mutated system, `v0_zero`): the frozen witness expansion
then fails with exact residual

```text
−(2/9)·p110²   ≠ 0
```

which equals the prediction (collapsed provenance coefficient of
constraint 84 is −2/9), confirming both that the check fails loudly and
that the provenance bookkeeping is quantitatively correct.

## 10. Atom 8 — firewall audit: CONFIRMED (with custody notes)

**(a) Characteristic.**  Every claim is characteristic-zero, and must be:
the branch-cover step divides by 4 and uses squarefreeness of `X^4−1`
(fails in char 2); the witnesses and span transitions have denominators
with prime support {2,3,5,7} (e.g. 12, 9, 45, 63, 24, 16); nothing is
claimed mod p.  The `p65521` `.sing` files are unrun coefficient-custody
artifacts and are not cited as evidence by the producer.  No bad-prime
issue exists because no positive-characteristic claim is made.

**(b) Field vs. scheme.**  Correctly separated everywhere: the row-12/13
steps are radical/set-theoretic (`H|A²⟹C|A`, `C|B²⟹C|B`, `E=0⟹` branch),
so no lifted unit certificate for the upstream nonreduced row-12/13
scheme is claimed — and none follows from this evidence.  What *is*
scheme-level is each post-parametrization branch target: its ideal
contains 1 over Q, an honest polynomial identity.  The producer's
firewalls state exactly this split.

**(c) Fixed baseline and cutoff.**  The result concerns only the pinned
branch-P square baseline raw system with every weight<6 parameter set to
zero (`specialization` field; `negative_result_scope:
"specialization_only_non_evidence"` is present in the frozen source).
Nothing about the branch-P family, other cutoffs, or the tail-seven lane
is claimed or supported.  The `p110=1, p32=−1` diagnostics are labeled
non-covering and are not used in any exclusion.

**(d) No Keller/JC2 claim; no D23/G22.**  Verified at the raw level: the
generator rows are exactly 4..22 (no row 23); `charged_rows.D23_imposed
= false` with affine target `D22 = 1` only; no weight-22 G slot exists
among the 303 raw variables (`slotless.G22_present = false`,
`G_max_weight = 21`); the frozen TAIL6 flags agree.  The constraint set
used is a *necessary subsystem* (rows 12–15 plus the row-22 X^0
endpoint; ignoring rows 16–21 and the other row-22 coordinates only
weakens the system, so emptiness of the subsystem's locus is sound).
Neither report makes any Keller-pair, counterexample, or JC2 claim.

**Custody notes (no verdict impact).**  (i) The weight source
`cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json`
(observed sha256 `28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876`)
is read by the pinned upstream compiler but is not itself pinned in this
case's `SOURCE.sha256`.  Not load-bearing here: the closed-form weight
formula reproduces all 442 slot records with 0 mismatches, and the
retained list derived from the formula equals the list frozen inside the
pinned TAIL6 JSON; but a successor case could add the pin for hygiene.
(ii) The derivation of `RAW_DIRECT_SYSTEM.json` itself (branch-P square
baseline) is upstream of this charge and only custody-checked here.
(iii) The six `.sing` files remain unrun; they are custody artifacts,
not evidence, exactly as the producer states.

## 11. Narrowest promotable theorem

> **Theorem (cutoff-six square-tail field obstruction).**  Fix the pinned
> branch-P square-baseline raw system
> (`RAW_DIRECT_SYSTEM.json`, sha256 `ead2fa40…`) and set every raw
> deformation parameter of weight below 6 to zero.  Then over every field
> of characteristic zero, the resulting cutoff-six tail system — the 253
> coefficient equations `D12..D22` on the 122-dimensional prefix
> nullspace, with the affine endpoint `D22[X^0]=1` — has no field-valued
> point.  Specifically: rows 12–13 force, set-theoretically,
> `F6=(X^4−1)^2·V` with `deg V ≤ 2` and `V0 ∈ {0, 4·p110}`; and on each
> branch the polynomial ideal generated by the 19-dimensional row-14/15
> compatibility span together with `1+p32·p110` contains 1, via
> `1=(1−p32·p110)(1+p32·p110)+p32²·(p110²)` with `p110²` an explicit
> Q-combination of displayed compatibilities.

Explicitly **not** established: any scheme-level/nonreduced statement
across the row-12/13 parametrizations; anything about the unspecialized
branch-P family or other cutoffs; any positive-characteristic statement;
any Keller-pair, counterexample, or Jacobian-conjecture consequence.

---

# Appendix A — key command outputs

## A.1 Producer replay (full JSON, exit 0)

```text
{"check": true, "direct_unit_certificate": "PASS_BOTH_ROW13_BRANCHES_NO_GB", "payload_sha256": {"SOURCE.sha256": "d98630ac84c14b64e4f6a1de5b74ce7ba0ba8b85c319428580ec5e96c8ae28ab", "TAIL6_DESK_ANALYSIS.json": "7ed247251df0122fa71211a945f7ab092a9f157bbe31842c3cc8c92f9d53b5fb", "TARGETS/v0_four_p110_p110_one_diagnostic_q.sing": "2f19bc0617867231e995b367117ff0fd732e803afcd099047db367b02290118f", "TARGETS/v0_four_p110_row14_15_localized_p65521.sing": "16684fc9aea7b8da6ed167d935a7524a95d886d4a84d7d4c09bedc49ec87c608", "TARGETS/v0_four_p110_row14_15_localized_q.sing": "e458f63fcb8964f4ebce98146ff577860a4e11222e43ad33f74334ca3a76e70c", "TARGETS/v0_zero_p110_one_diagnostic_q.sing": "6b09d44037a0f0f9b5a8b030d5c6657eb70a4d7c571ec1fe86a87e9af1366589", "TARGETS/v0_zero_row14_15_localized_p65521.sing": "51383dbae50f88e9ec3b726e5cef82c593cc9ee27892d853a7c04e285fe2f823", "TARGETS/v0_zero_row14_15_localized_q.sing": "f2c59134e29b68c9a33e45aa418d1ce821755673f44e0793f2d23fc5685699d6", "UNIT_CERTIFICATE.json": "812dc5b7d337dc8a6bb68b5419c4ce0556c2e0ed29e1eb4213d5a79ece3a8269"}, "source_sha256": "c038fd929d8c11cf8465dd72edb5fc4cca430140d11199f3c6fbd2f968e1b389", "status": "PASS"}
```

## A.2 Independent checker log (complete stdout, exit 0, ≈2.4 s)

```text
========================================================================
S1 RAW CENSUS
  RAW_DIRECT_SYSTEM.json sha256 = ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  TAIL_DEFORMATION_SYSTEM.json sha256 = c038fd929d8c11cf8465dd72edb5fc4cca430140d11199f3c6fbd2f968e1b389
  RAW_INPUT.json (weight source, UNPINNED in this case) sha256 = 28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
  weight formula vs RAW_INPUT slots: 442 slots, mismatches = 0
  retained (weight>=6) = 220  (frozen says 220)
  raw records per row: {4: 36, 5: 35, 6: 34, 7: 33, 8: 32, 9: 31, 10: 30, 11: 29, 12: 28, 13: 27, 14: 26, 15: 25, 16: 24, 17: 23, 18: 22, 19: 21, 20: 20, 21: 19, 22: 18}
  prefix records (rows<=11) = 260; rows 12..22 = 253
  pure f/g monomial weight window per row: {4: (4, 4), 5: (4, 5), 6: (4, 6), 7: (4, 7), 8: (5, 8), 9: (6, 9), 10: (7, 10), 11: (8, 11), 12: (9, 12), 13: (10, 13), 14: (11, 14), 15: (12, 15), 16: (13, 16), 17: (14, 17), 18: (16, 18), 19: (17, 19), 20: (18, 20), 21: (19, 21), 22: (20, 22)}
  monomials containing z_/tt_ (all zeroed at cutoff 6): 18586; constant terms: 1
  slotless flags: {'F_max_weight': 14, 'G22_present': False, 'G_max_weight': 21}; charged_rows: {'D23_imposed': False, 'affine_target': {'row': 22, 'value': 1}, 'zero': [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]}
  weight-22 G slots present in raw variables: []
========================================================================
S2 PREFIX RANK (my RREF over Q)
  prefix rank = 98, nullity = 122
========================================================================
S3 FROZEN NULLSPACE BASIS
  basis vectors failing some prefix equation: 0
  rank of 122 frozen basis vectors = 122
  mixed-weight-support basis vectors: 43 of 122 (stage = min weight, producer convention)
  stage -> parameters:
    stage  6: n= 11  [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121]
    stage  7: n= 10  [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
    stage  8: n= 10  [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    stage  9: n=  7  [84, 85, 86, 87, 88, 89, 90]
    stage 10: n=  6  [78, 79, 80, 81, 82, 83]
    stage 11: n=  5  [73, 74, 75, 76, 77]
    stage 12: n= 16  [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]
    stage 13: n= 13  [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]
    stage 14: n= 11  [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
    stage 15: n=  9  [24, 25, 26, 27, 28, 29, 30, 31, 32]
    stage 16: n=  7  [17, 18, 19, 20, 21, 22, 23]
    stage 17: n=  6  [11, 12, 13, 14, 15, 16]
    stage 18: n=  5  [6, 7, 8, 9, 10]
    stage 19: n=  3  [3, 4, 5]
    stage 20: n=  2  [1, 2]
    stage 21: n=  1  [0]
    weight support of stage-12 parameters: [12]
    weight support of stage-13 parameters: [13]
    weight support of stage-14 parameters: [14]
    weight support of stage-15 parameters: [15]
  raw_value_linear_map mismatches over all 303 variables: 0
  forms[f_0_1] = (1)*p110   weight=7 x_index=0
  forms[g_1_0] = (1)*p32   weight=15 x_index=1
  forms[f_1_0] = (1)*p77   weight=11
  forms[g_0_1] = 0   weight=11  (empty => forced 0)
  weight-15 G slots: ['g_1_0', 'g_2_3', 'g_3_6', 'g_4_9', 'g_5_12', 'g_6_15', 'g_7_18', 'g_8_21', 'g_9_24']
  weight-7 F slots: ['f_0_1', 'f_1_4', 'f_2_7', 'f_3_10', 'f_4_13', 'f_5_16', 'f_6_19', 'f_7_22', 'f_8_25', 'f_9_28']
========================================================================
S4 RECONSTRUCT 253 CONSTRAINTS FROM RAW
  constraints differing from frozen TAIL6 (terms/row/x_degree/sha256): 0
  per-row constraint counts: {12: 28, 13: 27, 14: 26, 15: 25, 16: 24, 17: 23, 18: 22, 19: 21, 20: 20, 21: 19, 22: 18}
========================================================================
S5 ENDPOINT
  raw row22/x0 terms: [[[], '-1'], [['f_0_1', 'g_1_0'], '-1'], [['f_1_0', 'g_0_1'], '1']]
  reconstructed row22/x0 (constraint index 235): (-1)*1 + (-1)*p32*p110
  => D22[X^0]-1 = -1 - p32*p110 with p32=value(g_1_0)=G15[X^1], p110=value(f_0_1)=F7[X^0]
     (third raw term +f_1_0*g_0_1 dies because g_0_1 is a forced-zero pivot)
========================================================================
S7 ROW 12 (no substitutions)
  log12: {'row': 12, 'equations': 28, 'candidates': 16, 'rank': 12, 'pivot_params': [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], 'free_params': [69, 70, 71, 72], 'compat_count': 16, 'compat_span_rank': 8}
  rank(A^2 mod H coeffs) = 8; rank(r12 U model) = 8
  => span(r12 compats) == span(coeffs of F6^2 mod H)  [both rank 8, union rank 8]
  model[0] (X^0 coeff of A^2 mod H) = (-4)*p111*p111 + (-6)*p111*p115 + (-4)*p111*p119 + (-6)*p112*p114 + (-4)*p112*p118 + (-3)*p113*p113 + (-4)*p113*p117 + (-2)*p113*p121 + (-4)*p114*p116 + (-2)*p114*p120 + (-2)*p115*p115 + (-2)*p115*p119 + (-2)*p116*p118 + (-1)*p117*p117 + (1)*p121*p121
========================================================================
S8 ROW 13 UNDER A=C*B
  row-12 compats after A=C*B substitution: nonzero = 0
  re-run row-12 stage under A=C*B: compat_count = 0
  log13 (with row-12 pivot substitutions in force): {'row': 13, 'equations': 27, 'candidates': 13, 'rank': 11, 'pivot_params': [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], 'free_params': [55, 56], 'compat_count': 16, 'compat_span_rank': 9}
  rank(B(4CF7-B) mod H coeffs) = 8; +E = 9; union with r13 = 9
  => span(r13 compats) == span(8 coeffs of B*(4*C*F7-B) mod H) + Q*E
  E = (1)*p110*b0 + (-1/2)*b0*b4 + (-1/2)*b1*b3 + (-1/4)*b2*b2 + (-1/2)*b2*b6 + (-1/2)*b3*b5 + (-1/4)*b4*b4 + (-1/4)*b6*b6
  (4BCF7-B^2) mod C == -(B^2) mod C : True
  E under B=C*V: (-1)*p110*v0 + (1/4)*v0*v0
  == V0*(V0-4*p110)/4 exactly  => field branches V0=0 or V0=4*p110
========================================================================
S9 BRANCH PIPELINES
  symbolic check: (H*V)^2 mod H == 0  (so row-12 compats must vanish)
  stage-12/13/14 parameters appearing in raw rows 14/15 (row, param, stage): [(14, 33, 14), (14, 34, 14), (14, 35, 14), (14, 36, 14), (14, 37, 14), (14, 38, 14), (14, 39, 14), (14, 40, 14), (14, 41, 14), (14, 42, 14), (14, 43, 14), (14, 44, 13), (14, 45, 13), (14, 46, 13), (14, 47, 13), (14, 48, 13), (14, 49, 13), (14, 50, 13), (14, 51, 13), (14, 52, 13), (14, 53, 13), (14, 54, 13), (14, 55, 13), (14, 56, 13), (14, 57, 12), (14, 58, 12), (14, 59, 12), (14, 60, 12), (14, 61, 12), (14, 62, 12), (14, 63, 12), (14, 64, 12), (14, 65, 12), (14, 66, 12), (14, 67, 12), (14, 68, 12), (14, 70, 12), (14, 71, 12), (14, 72, 12), (15, 33, 14), (15, 34, 14), (15, 35, 14), (15, 36, 14), (15, 37, 14), (15, 38, 14), (15, 39, 14), (15, 40, 14), (15, 41, 14), (15, 42, 14), (15, 43, 14), (15, 44, 13), (15, 45, 13), (15, 46, 13), (15, 47, 13), (15, 48, 13), (15, 49, 13), (15, 50, 13), (15, 51, 13), (15, 52, 13), (15, 53, 13), (15, 54, 13), (15, 55, 13), (15, 56, 13), (15, 70, 12), (15, 71, 12), (15, 72, 12)]
------------------------------------------------------------------------
  BRANCH v0_zero
    row-12 compats under A=HV: 0; row-13 compats nonzero after branch: 0 (of 4)
    log14: {'row': 14, 'equations': 26, 'candidates': 11, 'rank': 10, 'pivot_params': [33, 34, 35, 36, 37, 38, 39, 40, 41, 42], 'free_params': [43], 'compat_count': 16, 'compat_span_rank': 8}
    log15: {'row': 15, 'equations': 25, 'candidates': 8, 'rank': 8, 'pivot_params': [24, 25, 26, 27, 28, 29, 30, 31], 'free_params': [], 'compat_count': 17, 'compat_span_rank': 17}
    plain {A=HV,branch} equals progressive: row14=False row15=False (if False, the recorded pivot substitutions are load-bearing)
    row-15 compats with row-12/13 pivots but WITHOUT row-14 pivots equal certified row-15 compats: False
    cumulative span rank(r14+r15) = 19
    my own solved witness (index: coeff): {1: '1/12', 13: '1/9', 19: '-2/9', 23: '-2/9', 27: '-2/9', 31: '-2/9'}
    frozen sparse witness expansion == p110^2 : True
    r14[1] coeff 1/12: 18 terms, sha256 3eb85794603f50c3..., certificate match=True
    r14[13] coeff 1/9: 16 terms, sha256 f0412b18ee894ff3..., certificate match=True
    r15[3] coeff -2/9: 43 terms, sha256 a70967cd25045414..., certificate match=True
    r15[7] coeff -2/9: 43 terms, sha256 f8fb628886e09c40..., certificate match=True
    r15[11] coeff -2/9: 41 terms, sha256 74c5f7769ba1d9bd..., certificate match=True
    r15[15] coeff -2/9: 35 terms, sha256 9ebab33d258c75ca..., certificate match=True
    collapsed row-14 source combination {58: '7/24', 62: '5/24', 66: '1/12', 78: '1/9'} matches certificate: True
      Q-combination of substituted literal source rows reproduces the row-14 witness part: True
    collapsed row-15 source combination {84: '-2/9', 88: '-2/9', 92: '-2/9', 96: '-2/9', 100: '-2/9', 104: '-2/9'} matches certificate: True
      Q-combination of substituted literal source rows reproduces the row-15 witness part: True
      same combination on UNSUBSTITUTED raw p-rows equals witness part: False  (must be False: substitution is load-bearing)
    p110^2 in span of 19-dim cumulative basis: True; literally a basis element: True
    target: generators=20, operative variables=22, max degree=2
    unit identity expansion (1-p32*p110)*(1+p32*p110)+p32^2*p110^2 = (1)*1
------------------------------------------------------------------------
  BRANCH v0_four_p110
    row-12 compats under A=HV: 0; row-13 compats nonzero after branch: 0 (of 4)
    log14: {'row': 14, 'equations': 26, 'candidates': 11, 'rank': 10, 'pivot_params': [33, 34, 35, 36, 37, 38, 39, 40, 41, 42], 'free_params': [43], 'compat_count': 16, 'compat_span_rank': 8}
    log15: {'row': 15, 'equations': 25, 'candidates': 8, 'rank': 8, 'pivot_params': [24, 25, 26, 27, 28, 29, 30, 31], 'free_params': [], 'compat_count': 17, 'compat_span_rank': 17}
    plain {A=HV,branch} equals progressive: row14=False row15=False (if False, the recorded pivot substitutions are load-bearing)
    row-15 compats with row-12/13 pivots but WITHOUT row-14 pivots equal certified row-15 compats: False
    cumulative span rank(r14+r15) = 19
    my own solved witness (index: coeff): {9: '-1', 13: '-37/9', 19: '16/9', 23: '32/9', 27: '256/45', 31: '512/63'}
    frozen sparse witness expansion == p110^2 : True
    r14[9] coeff -1: 21 terms, sha256 a489aff2954e19c5..., certificate match=True
    r14[13] coeff -37/9: 17 terms, sha256 9dc623f906f6e301..., certificate match=True
    r15[3] coeff 16/9: 43 terms, sha256 7be494cb20fb6e65..., certificate match=True
    r15[7] coeff 32/9: 43 terms, sha256 6e3c0731ff70f084..., certificate match=True
    r15[11] coeff 256/45: 40 terms, sha256 6607afb685cc7ba0..., certificate match=True
    r15[15] coeff 512/63: 34 terms, sha256 2a0f0f158427423f..., certificate match=True
    collapsed row-14 source combination {58: '16/3', 62: '2/3', 74: '-1', 78: '-37/9'} matches certificate: True
      Q-combination of substituted literal source rows reproduces the row-14 witness part: True
    collapsed row-15 source combination {84: '-2/9', 88: '4/9', 92: '16/9', 96: '32/9', 100: '256/45', 104: '512/63'} matches certificate: True
      Q-combination of substituted literal source rows reproduces the row-15 witness part: True
      same combination on UNSUBSTITUTED raw p-rows equals witness part: False  (must be False: substitution is load-bearing)
    p110^2 in span of 19-dim cumulative basis: True; literally a basis element: True
    target: generators=20, operative variables=23, max degree=2
    unit identity expansion (1-p32*p110)*(1+p32*p110)+p32^2*p110^2 = (1)*1
========================================================================
S10 LIVE MUTATIONS (in-memory only; frozen case untouched)
  (a) mutate witness coefficient of r14[1]: 1/12 -> 1/11
      residual (= (1/132)*r14[1]) has 18 terms; residual == (1/132)*r14[1]: True
      residual = (6/11)*p101*p107 + (6/11)*p102*p106 + (12/11)*p102*p110 + (6/11)*p103*p105 + (12/11)*p103*p109 + (-6/11)*p103*v1 + (3/11)*p104*p104 + (12/11)*p104*p108 + (-6/11)*p104*v2 + (12/11)*p105*p107 + (6/11)*p106*p106 + (18/11)*p106*p110 + (18/11)*p107*p109 + (-9/11)*p107*v1 + (9/11)*p108*p108 + (-9/11)*p108*v2 + (9/11)*p110*p110 + (9/44)*v2*v2
  (b) mutate literal source row: constraint 84 (row 15, x_degree 3) += 1*(p110^2); re-run row-15 elimination
      mutated-stage log15: rank=8 compat_count=17
      residual of frozen witness expansion = (-2/9)*p110*p110
      predicted -2/9*p110^2 (collapsed coefficient of row 84 is -2/9): True
  both mutations fail loudly with exact nonzero residual polynomials
========================================================================
ALL INDEPENDENT CHECKS PASS
```

# Appendix B — the twelve selected witness compatibility polynomials

Exact text as recomputed independently (hashes match `UNIT_CERTIFICATE.json`):

```text
== v0_zero ==
r14[1]  (coeff 1/12, 18 terms, sha256 3eb85794603f50c340315c1fc273f8559238f3f4c95700ca34459ffed4fda015):
  (72)*p101*p107 + (72)*p102*p106 + (144)*p102*p110 + (72)*p103*p105 + (144)*p103*p109 + (-72)*p103*v1 + (36)*p104*p104 + (144)*p104*p108 + (-72)*p104*v2 + (144)*p105*p107 + (72)*p106*p106 + (216)*p106*p110 + (216)*p107*p109 + (-108)*p107*v1 + (108)*p108*p108 + (-108)*p108*v2 + (108)*p110*p110 + (27)*v2*v2
r14[13]  (coeff 1/9, 16 terms, sha256 f0412b18ee894ff3f49648280b5fc384e31159cf655805b11094b643f25cbdc4):
  (72)*p101*p103 + (36)*p102*p102 + (-72)*p102*p110 + (-72)*p103*p109 + (36)*p103*v1 + (-72)*p104*p108 + (36)*p104*v2 + (-72)*p105*p107 + (-36)*p106*p106 + (-144)*p106*p110 + (-144)*p107*p109 + (72)*p107*v1 + (-72)*p108*p108 + (72)*p108*v2 + (-72)*p110*p110 + (-18)*v2*v2
r15[3]  (coeff -2/9, 43 terms, sha256 a70967cd250454145bca2fee17b819ef9e6bceefd6915caf8812558887e79263):
  (96)*p91*p102 + (144)*p91*p106 + (87)*p91*p110 + (72)*p92*p106 + (144)*p92*p110 + (72)*p93*p105 + (144)*p93*p109 + (-72)*p93*v1 + (72)*p94*p104 + (144)*p94*p108 + (-72)*p94*v2 + (72)*p95*p103 + (144)*p95*p107 + (72)*p96*p102 + (144)*p96*p106 + (216)*p96*p110 + (72)*p97*p101 + (144)*p97*p105 + (216)*p97*p109 + (-108)*p97*v1 + (144)*p98*p104 + (216)*p98*p108 + (-108)*p98*v2 + (144)*p99*p103 + (216)*p99*p107 + (27)*p101*p107 + (27)*p102*p106 + (-90)*p102*p110 + (27)*p103*p105 + (-18)*p103*p109 + (9)*p103*v1 + (27/2)*p104*p104 + (-18)*p104*p108 + (9)*p104*v2 + (-18)*p105*p107 + (-9)*p106*p106 + (-279)*p106*p110 + (-171)*p107*p109 + (171/2)*p107*v1 + (-171/2)*p108*p108 + (171/2)*p108*v2 + (-3537/16)*p110*p110 + (-171/8)*v2*v2
r15[7]  (coeff -2/9, 43 terms, sha256 f8fb628886e09c407ba3051bfcbc05ee8a00958567c172e8a94cf64cf6e7d53a):
  (-240)*p91*p102 + (-392)*p91*p106 + (-229)*p91*p110 + (96)*p92*p102 + (-132)*p92*p106 + (-360)*p92*p110 + (96)*p93*p101 + (-132)*p93*p105 + (-360)*p93*p109 + (180)*p93*v1 + (-132)*p94*p104 + (-360)*p94*p108 + (180)*p94*v2 + (-132)*p95*p103 + (-360)*p95*p107 + (-132)*p96*p102 + (-360)*p96*p106 + (-588)*p96*p110 + (-132)*p97*p101 + (-360)*p97*p105 + (-588)*p97*p109 + (294)*p97*v1 + (-360)*p98*p104 + (-588)*p98*p108 + (294)*p98*v2 + (-360)*p99*p103 + (-588)*p99*p107 + (36)*p101*p103 + (18)*p102*p102 + (324)*p102*p110 + (144)*p103*p109 + (-72)*p103*v1 + (144)*p104*p108 + (-72)*p104*v2 + (144)*p105*p107 + (72)*p106*p106 + (876)*p106*p110 + (582)*p107*p109 + (-291)*p107*v1 + (291)*p108*p108 + (-291)*p108*v2 + (10059/16)*p110*p110 + (291/4)*v2*v2
r15[11]  (coeff -2/9, 41 terms, sha256 74c5f7769ba1d9bdccc0fb61de341e90cac8fdfa028ef582fad0ee5f716f69d9):
  (200)*p91*p102 + (360)*p91*p106 + (205)*p91*p110 + (-180)*p92*p102 + (60)*p92*p106 + (300)*p92*p110 + (-180)*p93*p101 + (60)*p93*p105 + (300)*p93*p109 + (-150)*p93*v1 + (60)*p94*p104 + (300)*p94*p108 + (-150)*p94*v2 + (60)*p95*p103 + (300)*p95*p107 + (60)*p96*p102 + (300)*p96*p106 + (540)*p96*p110 + (60)*p97*p101 + (300)*p97*p105 + (540)*p97*p109 + (-270)*p97*v1 + (300)*p98*p104 + (540)*p98*p108 + (-270)*p98*v2 + (300)*p99*p103 + (540)*p99*p107 + (-300)*p102*p110 + (-150)*p103*p109 + (75)*p103*v1 + (-150)*p104*p108 + (75)*p104*v2 + (-150)*p105*p107 + (-75)*p106*p106 + (-840)*p106*p110 + (-570)*p107*p109 + (285)*p107*v1 + (-285)*p108*p108 + (285)*p108*v2 + (-9315/16)*p110*p110 + (-285/4)*v2*v2
r15[15]  (coeff -2/9, 35 terms, sha256 9ebab33d258c75caab51765e9bb1cc9d3c7ead6a330c9e0f35c9b0227f3c909a):
  (-56)*p91*p102 + (-112)*p91*p106 + (-63)*p91*p110 + (84)*p92*p102 + (-84)*p92*p110 + (84)*p93*p101 + (-84)*p93*p109 + (42)*p93*v1 + (-84)*p94*p108 + (42)*p94*v2 + (-84)*p95*p107 + (-84)*p96*p106 + (-168)*p96*p110 + (-84)*p97*p105 + (-168)*p97*p109 + (84)*p97*v1 + (-84)*p98*p104 + (-168)*p98*p108 + (84)*p98*v2 + (-84)*p99*p103 + (-168)*p99*p107 + (84)*p102*p110 + (42)*p103*p109 + (-21)*p103*v1 + (42)*p104*p108 + (-21)*p104*v2 + (42)*p105*p107 + (21)*p106*p106 + (252)*p106*p110 + (168)*p107*p109 + (-84)*p107*v1 + (84)*p108*p108 + (-84)*p108*v2 + (2793/16)*p110*p110 + (21)*v2*v2
== v0_four_p110 ==
r14[9]  (coeff -1, 21 terms, sha256 a489aff2954e19c5c308106861c98c42222219ad3f299510671c185f21f183ef):
  (-576)*p91*p110 + (-168)*p101*p103 + (48)*p101*p107 + (-84)*p102*p102 + (48)*p102*p106 + (-264)*p102*p110 + (48)*p103*p105 + (264)*p103*p109 + (-132)*p103*v1 + (24)*p104*p104 + (264)*p104*p108 + (-132)*p104*v2 + (264)*p105*p107 + (132)*p106*p106 + (-480)*p106*p110 + (480)*p107*p109 + (-240)*p107*v1 + (240)*p108*p108 + (-240)*p108*v2 + (672)*p110*p110 + (60)*v2*v2
r14[13]  (coeff -37/9, 17 terms, sha256 9dc623f906f6e301e3fd2450531c3a9757f844ec3c87d3553e7b9df72718b2be):
  (192)*p91*p110 + (72)*p101*p103 + (36)*p102*p102 + (72)*p102*p110 + (-72)*p103*p109 + (36)*p103*v1 + (-72)*p104*p108 + (36)*p104*v2 + (-72)*p105*p107 + (-36)*p106*p106 + (144)*p106*p110 + (-144)*p107*p109 + (72)*p107*v1 + (-72)*p108*p108 + (72)*p108*v2 + (-216)*p110*p110 + (-18)*v2*v2
r15[3]  (coeff 16/9, 43 terms, sha256 7be494cb20fb6e6502b895a5c16791580d6429d76a7d5f5fda588077810dfacd):
  (96)*p91*p102 + (144)*p91*p106 + (120)*p91*p110 + (72)*p92*p106 + (-144)*p92*p110 + (72)*p93*p105 + (144)*p93*p109 + (-72)*p93*v1 + (72)*p94*p104 + (144)*p94*p108 + (-72)*p94*v2 + (72)*p95*p103 + (144)*p95*p107 + (72)*p96*p102 + (144)*p96*p106 + (-216)*p96*p110 + (72)*p97*p101 + (144)*p97*p105 + (216)*p97*p109 + (-108)*p97*v1 + (144)*p98*p104 + (216)*p98*p108 + (-108)*p98*v2 + (144)*p99*p103 + (216)*p99*p107 + (27)*p101*p107 + (27)*p102*p106 + (-54)*p102*p110 + (27)*p103*p105 + (-18)*p103*p109 + (9)*p103*v1 + (27/2)*p104*p104 + (-18)*p104*p108 + (9)*p104*v2 + (-18)*p105*p107 + (-9)*p106*p106 + (63)*p106*p110 + (-171)*p107*p109 + (171/2)*p107*v1 + (-171/2)*p108*p108 + (171/2)*p108*v2 + (-3933/16)*p110*p110 + (-171/8)*v2*v2
r15[7]  (coeff 32/9, 43 terms, sha256 6e3c0731ff70f084f83829ec315d1d222aa2949cc96d777147233fd782227f08):
  (-240)*p91*p102 + (-392)*p91*p106 + (-512)*p91*p110 + (96)*p92*p102 + (-132)*p92*p106 + (360)*p92*p110 + (96)*p93*p101 + (-132)*p93*p105 + (-360)*p93*p109 + (180)*p93*v1 + (-132)*p94*p104 + (-360)*p94*p108 + (180)*p94*v2 + (-132)*p95*p103 + (-360)*p95*p107 + (-132)*p96*p102 + (-360)*p96*p106 + (588)*p96*p110 + (-132)*p97*p101 + (-360)*p97*p105 + (-588)*p97*p109 + (294)*p97*v1 + (-360)*p98*p104 + (-588)*p98*p108 + (294)*p98*v2 + (-360)*p99*p103 + (-588)*p99*p107 + (36)*p101*p103 + (18)*p102*p102 + (36)*p102*p110 + (144)*p103*p109 + (-72)*p103*v1 + (144)*p104*p108 + (-72)*p104*v2 + (144)*p105*p107 + (72)*p106*p106 + (-288)*p106*p110 + (582)*p107*p109 + (-291)*p107*v1 + (291)*p108*p108 + (-291)*p108*v2 + (13455/16)*p110*p110 + (291/4)*v2*v2
r15[11]  (coeff 256/45, 40 terms, sha256 6607afb685cc7ba0a1458620fbd9912dc2634dd5e16a1aa2fa642a2fdd9c0c7b):
  (200)*p91*p102 + (360)*p91*p106 + (560)*p91*p110 + (-180)*p92*p102 + (60)*p92*p106 + (-300)*p92*p110 + (-180)*p93*p101 + (60)*p93*p105 + (300)*p93*p109 + (-150)*p93*v1 + (60)*p94*p104 + (300)*p94*p108 + (-150)*p94*v2 + (60)*p95*p103 + (300)*p95*p107 + (60)*p96*p102 + (300)*p96*p106 + (-540)*p96*p110 + (60)*p97*p101 + (300)*p97*p105 + (540)*p97*p109 + (-270)*p97*v1 + (300)*p98*p104 + (540)*p98*p108 + (-270)*p98*v2 + (300)*p99*p103 + (540)*p99*p107 + (-150)*p103*p109 + (75)*p103*v1 + (-150)*p104*p108 + (75)*p104*v2 + (-150)*p105*p107 + (-75)*p106*p106 + (300)*p106*p110 + (-570)*p107*p109 + (285)*p107*v1 + (-285)*p108*p108 + (285)*p108*v2 + (-13575/16)*p110*p110 + (-285/4)*v2*v2
r15[15]  (coeff 512/63, 34 terms, sha256 2a0f0f158427423f5df811ee65a0b700193cb695fae843e9d86b669079cd02b6):
  (-56)*p91*p102 + (-112)*p91*p106 + (-168)*p91*p110 + (84)*p92*p102 + (84)*p92*p110 + (84)*p93*p101 + (-84)*p93*p109 + (42)*p93*v1 + (-84)*p94*p108 + (42)*p94*v2 + (-84)*p95*p107 + (-84)*p96*p106 + (168)*p96*p110 + (-84)*p97*p105 + (-168)*p97*p109 + (84)*p97*v1 + (-84)*p98*p104 + (-168)*p98*p108 + (84)*p98*v2 + (-84)*p99*p103 + (-168)*p99*p107 + (42)*p103*p109 + (-21)*p103*v1 + (42)*p104*p108 + (-21)*p104*v2 + (42)*p105*p107 + (21)*p106*p106 + (-84)*p106*p110 + (168)*p107*p109 + (-84)*p107*v1 + (84)*p108*p108 + (-84)*p108*v2 + (4053/16)*p110*p110 + (21)*v2*v2
```

# Appendix C — full source of the independent checker

Run as `python3 /tmp/fable5_tail6_check.py` from any directory; deleted from
`/tmp` after this review per the charge, reproducible verbatim from here.

```python
#!/usr/bin/env python3
"""Fable5 hostile crossreview: independent checker for the cutoff-six
square-tail field obstruction (tail6 desk case, 2026-08-28).

Fully standard-library, exact Fraction arithmetic.  Does NOT import or
execute analyze_tail6.py.  Reconstructs the p-coordinate system directly
from the pinned upstream RAW_DIRECT_SYSTEM.json plus the frozen nullspace
basis, then re-derives every charged atom with its own polynomial algebra
and tracked eliminations.
"""

import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path("/Users/dc/code/math/jc2")
CASE = ROOT / "cases/ggv_8_28_upper_endpoint_tail6_desk_20260828"
TAIL6 = CASE / "TAIL6/TAIL_DEFORMATION_SYSTEM.json"
RAW = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
RAW_INPUT = ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json"
CERT = CASE / "UNIT_CERTIFICATE.json"

B0 = 1000  # b0..b6 -> 1000..1006 (same synthetic ids as producer, for hash comparability)
V0 = 1100  # v0..v2 -> 1100..1102

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def compact_bytes(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()

# ---------- my own exact sparse polynomial algebra (monomial = sorted tuple of int vars)
def padd(a, b):
    out = dict(a)
    for m, c in b.items():
        s = out.get(m, F(0)) + c
        if s:
            out[m] = s
        elif m in out:
            del out[m]
    return out

def pscale(a, c):
    c = F(c)
    if not c:
        return {}
    return {m: c * v for m, v in a.items()}

def pmul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = tuple(sorted(ma + mb))
            s = out.get(m, F(0)) + ca * cb
            if s:
                out[m] = s
            elif m in out:
                del out[m]
    return out

def psubst(poly, sub):
    out = {}
    for m, c in poly.items():
        term = {(): c}
        for var in m:
            term = pmul(term, sub.get(var, {(var,): F(1)}))
        out = padd(out, term)
    return out

def pencode(poly):
    return [[list(m), str(c)] for m, c in sorted(poly.items())]

def phash(poly):
    return hashlib.sha256(compact_bytes(pencode(poly))).hexdigest()

def pstr(poly, names=None):
    if not poly:
        return "0"
    def vn(v):
        if v < 1000:
            return f"p{v}"
        if 1000 <= v < 1100:
            return f"b{v-1000}"
        return f"v{v-1100}"
    bits = []
    for m, c in sorted(poly.items()):
        mono = "*".join(vn(v) for v in m) if m else "1"
        bits.append(f"({c})*{mono}")
    return " + ".join(bits)

# ---------- my own dense RREF over Q with optional provenance tracking
def rref(matrix, eliminate_cols, track=False):
    """matrix: list of rows (lists of F).  Eliminate only columns
    [0, eliminate_cols).  Pivot = first row >= rank with nonzero entry,
    swapped into position rank; full reduction above and below.
    Returns (rows, pivots, prov) with prov[i] = combination of input rows."""
    n = len(matrix)
    rows = [list(r) for r in matrix]
    prov = [[F(1) if j == i else F(0) for j in range(n)] for i in range(n)] if track else None
    rank = 0
    pivots = []
    for col in range(eliminate_cols):
        sel = None
        for r in range(rank, n):
            if rows[r][col]:
                sel = r
                break
        if sel is None:
            continue
        rows[rank], rows[sel] = rows[sel], rows[rank]
        if track:
            prov[rank], prov[sel] = prov[sel], prov[rank]
        piv = rows[rank][col]
        rows[rank] = [v / piv for v in rows[rank]]
        if track:
            prov[rank] = [v / piv for v in prov[rank]]
        for r in range(n):
            if r == rank or not rows[r][col]:
                continue
            f = rows[r][col]
            rows[r] = [a - f * b for a, b in zip(rows[r], rows[rank])]
            if track:
                prov[r] = [a - f * b for a, b in zip(prov[r], prov[rank])]
        pivots.append(col)
        rank += 1
    return rows, pivots, prov

def span_rank(polys):
    mons = sorted({m for p in polys for m in p})
    if not mons:
        return 0, [], mons
    mat = [[p.get(m, F(0)) for m in mons] for p in polys]
    rows, pivots, _ = rref(mat, len(mons))
    basis = [{m: c for m, c in zip(mons, rows[i]) if c} for i in range(len(pivots))]
    return len(pivots), basis, mons

def in_span_witness(polys, target):
    """Solve target = sum c_i polys[i] by my own tracked RREF; None if not."""
    mons = sorted({m for p in polys + [target] for m in p})
    mat = [[p.get(m, F(0)) for m in mons] for p in polys]
    rows, pivots, prov = rref(mat, len(mons), track=True)
    vec = [target.get(m, F(0)) for m in mons]
    wit = [F(0)] * len(polys)
    for i, pc in enumerate(pivots):
        s = vec[pc]
        if not s:
            continue
        vec = [a - s * b for a, b in zip(vec, rows[i])]
        wit = [a + s * b for a, b in zip(wit, prov[i])]
    if any(vec):
        return None
    chk = {}
    for c, p in zip(wit, polys):
        chk = padd(chk, pscale(p, c))
    assert chk == target
    return wit

# ---------- section 1: raw census
print("=" * 72)
print("S1 RAW CENSUS")
print(f"  RAW_DIRECT_SYSTEM.json sha256 = {sha(RAW)}")
print(f"  TAIL_DEFORMATION_SYSTEM.json sha256 = {sha(TAIL6)}")
print(f"  RAW_INPUT.json (weight source, UNPINNED in this case) sha256 = {sha(RAW_INPUT)}")
raw = json.loads(RAW.read_text())
tail6 = json.loads(TAIL6.read_text())
cert = json.loads(CERT.read_text())
src = json.loads(RAW_INPUT.read_text())
slot_w = {s["slot"]: int(s["weight"]) for k in ("F", "G")
          for s in src["raw_slots_through_weight_22"][k]}

def weight(name):
    if name.startswith("z_"):
        return 2
    if name.startswith("tt_"):
        return 3
    kind, a, b = name.split("_")
    return (8 if kind == "f" else 12) + 3 * int(a) - int(b)

bad = [(n, w) for n, w in slot_w.items() if weight(n) != w]
print(f"  weight formula vs RAW_INPUT slots: {len(slot_w)} slots, mismatches = {len(bad)}")
assert not bad
variables = raw["variables"]
assert len(variables) == 303
retained = [v for v in variables if weight(v) >= 6]
print(f"  retained (weight>=6) = {len(retained)}  (frozen says {tail6['retained_variable_count']})")
assert retained == tail6["retained_variables"], "retained list mismatch"
gens = raw["generators"]
from collections import Counter
per_row = Counter(int(g["row"]) for g in gens)
print(f"  raw records per row: {dict(sorted(per_row.items()))}")
prefix_records = [g for g in gens if int(g["row"]) <= 11]
nl_records = [g for g in gens if 11 < int(g["row"]) <= 22]
print(f"  prefix records (rows<=11) = {len(prefix_records)}; rows 12..22 = {len(nl_records)}")
assert len(prefix_records) == 260 and len(nl_records) == 253
assert not [g for g in gens if int(g["row"]) > 22], "row>22 present!"

# weight homogeneity: assert for pure f/g-slot monomials (the load-bearing
# structure); z_/tt_ monomials counted separately (they are all zeroed by the
# cutoff-six specialization, so their grading is immaterial downstream)
inhom_fg = []
n_ztt = 0
n_const = 0
for g in gens:
    r = int(g["row"])
    for m, c in g["terms"]:
        if not m:
            n_const += 1
            if (r, int(g["x_degree"])) != (22, 0):
                inhom_fg.append((r, g["x_degree"], "const"))
            continue
        if any(n.startswith(("z_", "tt_")) for n in m):
            n_ztt += 1
            continue
        if sum(weight(n) for n in m) != r:
            inhom_fg.append((r, g["x_degree"], m))
wt_window = {}
for g in gens:
    r = int(g["row"])
    for m, c in g["terms"]:
        if not m or any(n.startswith(("z_", "tt_")) for n in m):
            continue
        wt_window.setdefault(r, set()).add(sum(weight(n) for n in m))
print(f"  pure f/g monomial weight window per row: "
      f"{ {r: (min(s), max(s)) for r, s in sorted(wt_window.items())} }")
print(f"  monomials containing z_/tt_ (all zeroed at cutoff 6): {n_ztt}; constant terms: {n_const}")
assert n_const == 1
assert all(max(s) <= r and min(s) >= r - 3 for r, s in wt_window.items())
print(f"  slotless flags: {raw['slotless']}; charged_rows: {raw['charged_rows']}")
g22 = [v for v in variables if v.startswith("g_") and weight(v) == 22]
print(f"  weight-22 G slots present in raw variables: {g22}")
assert not g22

# ---------- section 2: prefix rank/nullity, my own RREF
print("=" * 72)
print("S2 PREFIX RANK (my RREF over Q)")
ridx = {n: i for i, n in enumerate(retained)}
pref_rows_named = []
mat = []
for g in prefix_records:
    row = [F(0)] * len(retained)
    named = {}
    for m, c in g["terms"]:
        c = F(c)
        if any(n not in ridx for n in m):
            continue  # a weight<6 variable is set to 0
        assert len(m) == 1, ("prefix nonlinear survivor", g["row"], m)
        row[ridx[m[0]]] += c
        named[m[0]] = named.get(m[0], F(0)) + c
    mat.append(row)
    pref_rows_named.append(named)
rows_, pivots_, _ = rref(mat, len(retained))
rank = len(pivots_)
print(f"  prefix rank = {rank}, nullity = {len(retained) - rank}")
assert rank == 98 and len(retained) - rank == 122

# ---------- section 3: frozen nullspace basis verification + stages
print("=" * 72)
print("S3 FROZEN NULLSPACE BASIS")
basis_named = []
for vec in tail6["nullspace_basis"]:
    basis_named.append({name: F(c) for name, c in vec})
assert len(basis_named) == 122
badv = 0
for k, vec in enumerate(basis_named):
    for named in pref_rows_named:
        s = sum(named[n] * vec.get(n, F(0)) for n in named)
        if s:
            badv += 1
print(f"  basis vectors failing some prefix equation: {badv}")
assert badv == 0
bmat = [[vec.get(n, F(0)) for n in retained] for vec in basis_named]
_, bpiv, _ = rref(bmat, len(retained))
print(f"  rank of 122 frozen basis vectors = {len(bpiv)}")
assert len(bpiv) == 122
stages = {}
stage_of = {}
mixed = 0
for k, vec in enumerate(basis_named):
    ws = {weight(n) for n in vec}
    if len(ws) > 1:
        mixed += 1
    w = min(ws)  # producer convention: stage = minimal weight in the support
    stages.setdefault(w, []).append(k)
    stage_of[k] = w
print(f"  mixed-weight-support basis vectors: {mixed} of 122 (stage = min weight, producer convention)")
print("  stage -> parameters:")
for w in sorted(stages):
    print(f"    stage {w:2d}: n={len(stages[w]):3d}  {stages[w] if len(stages[w])<20 else str(stages[w][:6])+'...'}")
for w in (12, 13, 14, 15):
    supp = sorted({weight(n) for k in stages[w] for n in basis_named[k]})
    print(f"    weight support of stage-{w} parameters: {supp}")
assert stages[12] == list(range(57, 73))
assert stages[13] == list(range(44, 57))
assert stages[14] == list(range(33, 44))
assert stages[15] == list(range(24, 33))
# parameter forms (transpose) + full raw_value_linear_map comparison
forms = {}
for name in retained:
    forms[name] = {(k,): vec[name] for k, vec in enumerate(basis_named) if vec.get(name)}
mism = 0
for name in variables:
    mine = forms.get(name, {})
    theirs = {(int(i),): F(c) for i, c in tail6["raw_value_linear_map"][name]}
    if mine != theirs:
        mism += 1
print(f"  raw_value_linear_map mismatches over all 303 variables: {mism}")
assert mism == 0
print(f"  forms[f_0_1] = {pstr(forms['f_0_1'])}   weight={weight('f_0_1')} x_index=0")
print(f"  forms[g_1_0] = {pstr(forms['g_1_0'])}   weight={weight('g_1_0')} x_index=1")
print(f"  forms[f_1_0] = {pstr(forms['f_1_0'])}   weight={weight('f_1_0')}")
print(f"  forms[g_0_1] = {pstr(forms.get('g_0_1', {}))}   weight={weight('g_0_1')}  (empty => forced 0)")
assert forms["f_0_1"] == {(110,): F(1)} and forms["g_1_0"] == {(32,): F(1)}
assert forms.get("g_0_1", {}) == {}
w15g = sorted((weight(v), v) for v in variables if v.startswith("g_") and weight(v) == 15)
print(f"  weight-15 G slots: {[v for _, v in w15g]}")
w7f = sorted(v for v in variables if v.startswith("f_") and weight(v) == 7)
print(f"  weight-7 F slots: {w7f}")

# ---------- section 4: reconstruct all 253 constraints from raw
print("=" * 72)
print("S4 RECONSTRUCT 253 CONSTRAINTS FROM RAW")
my_constraints = []
for g in nl_records:
    poly = {}
    for m, c in g["terms"]:
        c = F(c)
        if not m:
            poly = padd(poly, {(): c})
            continue
        if any(n not in forms for n in m):
            continue
        term = {(): F(1)}
        for n in m:
            term = pmul(term, forms[n])
        poly = padd(poly, pscale(term, c))
    my_constraints.append({"row": int(g["row"]), "x_degree": int(g["x_degree"]), "poly": poly})
assert len(my_constraints) == 253
mismatch = 0
for mine, theirs in zip(my_constraints, tail6["constraints"]):
    tpoly = {tuple(m): F(c) for m, c in theirs["terms"]}
    ok = (mine["row"] == int(theirs["row"]) and mine["x_degree"] == int(theirs["x_degree"])
          and mine["poly"] == tpoly and phash(mine["poly"]) == theirs["sha256"])
    if not ok:
        mismatch += 1
print(f"  constraints differing from frozen TAIL6 (terms/row/x_degree/sha256): {mismatch}")
assert mismatch == 0
by_row = {}
for i, c in enumerate(my_constraints):
    by_row.setdefault(c["row"], []).append((i, c))
print(f"  per-row constraint counts: { {r: len(v) for r, v in sorted(by_row.items())} }")

# ---------- section 5: endpoint identity
print("=" * 72)
print("S5 ENDPOINT")
raw220 = [g for g in nl_records if int(g["row"]) == 22 and int(g["x_degree"]) == 0]
assert len(raw220) == 1
print(f"  raw row22/x0 terms: {raw220[0]['terms']}")
e_idx, e_rec = next((i, c) for i, c in by_row[22] if c["x_degree"] == 0)
print(f"  reconstructed row22/x0 (constraint index {e_idx}): {pstr(e_rec['poly'])}")
assert e_rec["poly"] == {(): F(-1), (32, 110): F(-1)}
print("  => D22[X^0]-1 = -1 - p32*p110 with p32=value(g_1_0)=G15[X^1], p110=value(f_0_1)=F7[X^0]")
print("     (third raw term +f_1_0*g_0_1 dies because g_0_1 is a forced-zero pivot)")

# ---------- section 6: triangular stage driver (mine)
def stage(row_number, candidates, subs, constraints=None):
    """Returns (compat list, log, details) with tracked provenance.
    details[i] = (prov dict global_constraint_index -> F, substituted source polys)"""
    items = by_row[row_number] if constraints is None else constraints
    subbed = []
    for gi, c in items:
        subbed.append((gi, psubst(dict(c["poly"]), subs)))
    cset = set(candidates)
    mons = sorted({m for _, p in subbed for m in p
                   if not (len(m) == 1 and m[0] in cset)})
    ncand = len(candidates)
    mat = []
    for gi, p in subbed:
        rowv = [F(0)] * (ncand + len(mons))
        for m, c in p.items():
            hits = [v for v in m if v in cset]
            if hits:
                assert len(hits) == 1 and m == (hits[0],), (row_number, m)
                rowv[candidates.index(hits[0])] += c
            else:
                rowv[ncand + mons.index(m)] += c
        mat.append(rowv)
    rows, pivots, prov = rref(mat, ncand, track=True)
    free = [c for c in range(ncand) if c not in set(pivots)]
    newsubs = {}
    for i, pc in enumerate(pivots):
        sol = {}
        for fc in free:
            if rows[i][fc]:
                sol = padd(sol, {(candidates[fc],): -rows[i][fc]})
        for j, m in enumerate(mons):
            if rows[i][ncand + j]:
                sol = padd(sol, {m: -rows[i][ncand + j]})
        newsubs[candidates[pc]] = sol
    compat = []
    details = []
    for i in range(len(pivots), len(rows)):
        assert not any(rows[i][:ncand]), "nonzero candidate part below rank"
        poly = {m: rows[i][ncand + j] for j, m in enumerate(mons) if rows[i][ncand + j]}
        if not poly:
            continue
        pv = {subbed[j][0]: prov[i][j] for j in range(len(subbed)) if prov[i][j]}
        recon = {}
        for j in range(len(subbed)):
            if prov[i][j]:
                recon = padd(recon, pscale(subbed[j][1], prov[i][j]))
        assert recon == poly, "provenance reconstruction failed"
        compat.append(poly)
        details.append((pv, poly))
    log = {"row": row_number, "equations": len(items), "candidates": len(candidates),
           "rank": len(pivots), "pivot_params": [candidates[c] for c in pivots],
           "free_params": [candidates[c] for c in free],
           "compat_count": len(compat), "compat_span_rank": span_rank(compat)[0]}
    return compat, log, newsubs, details

# ---------- section 7: row 12 (no substitutions) and A^2 mod H model
print("=" * 72)
print("S7 ROW 12 (no substitutions)")
r12, log12, subs12, _ = stage(12, stages[12], {})
print(f"  log12: {log12}")
assert log12["equations"] == 28 and log12["candidates"] == 16
assert log12["rank"] == 12 and len(log12["free_params"]) == 4
assert log12["compat_count"] == 16 and log12["compat_span_rank"] == 8

def dense_mul(a, b):
    out = [{} for _ in range(len(a) + len(b) - 1)]
    for i, pa in enumerate(a):
        for j, pb in enumerate(b):
            out[i + j] = padd(out[i + j], pmul(pa, pb))
    return out

def mod_H(dense):
    d = [dict(p) for p in dense]
    while len(d) < 8:
        d.append({})
    for k in range(len(d) - 1, 7, -1):
        lead = d[k]
        if not lead:
            continue
        d[k] = {}
        d[k - 4] = padd(d[k - 4], pscale(lead, 2))
        d[k - 8] = padd(d[k - 8], pscale(lead, -1))
    return d[:8]

def mod_C(dense):
    d = [dict(p) for p in dense]
    while len(d) < 4:
        d.append({})
    for k in range(len(d) - 1, 3, -1):
        lead = d[k]
        if not lead:
            continue
        d[k] = {}
        d[k - 4] = padd(d[k - 4], lead)
    return d[:4]

A = [{(121 - d,): F(1)} for d in range(11)]
modelA2 = mod_H(dense_mul(A, A))
rkA, _, _ = span_rank(modelA2)
rk_union, _, _ = span_rank(r12 + modelA2)
print(f"  rank(A^2 mod H coeffs) = {rkA}; rank(r12 U model) = {rk_union}")
assert rkA == 8 and rk_union == 8
print(f"  => span(r12 compats) == span(coeffs of F6^2 mod H)  [both rank 8, union rank 8]")
print(f"  model[0] (X^0 coeff of A^2 mod H) = {pstr(modelA2[0])}")

# ---------- section 8: A=C*B, row 13
print("=" * 72)
print("S8 ROW 13 UNDER A=C*B")
subs_CB = {}
for d in range(11):
    val = {}
    if 0 <= d - 4 <= 6:
        val = padd(val, {(B0 + d - 4,): F(1)})
    if 0 <= d <= 6:
        val = padd(val, {(B0 + d,): F(-1)})
    subs_CB[121 - d] = val
dead = [p for p in (psubst(p, subs_CB) for p in r12) if p]
print(f"  row-12 compats after A=C*B substitution: nonzero = {len(dead)}")
assert not dead
subsCB2 = dict(subs_CB)
r12b, log12b, ns12b, _ = stage(12, stages[12], subsCB2)
print(f"  re-run row-12 stage under A=C*B: compat_count = {log12b['compat_count']}")
assert log12b["compat_count"] == 0
# progressive semantics: row-13 equations live in weight window [10,13], so
# they contain stage-12 parameters; the row-12 pivot solutions must be
# substituted before eliminating the stage-13 candidates.
subsCB2.update(ns12b)
r13, log13, ns13_, _ = stage(13, stages[13], subsCB2)
print(f"  log13 (with row-12 pivot substitutions in force): {log13}")
assert log13["equations"] == 27 and log13["candidates"] == 13
assert log13["rank"] == 11 and len(log13["free_params"]) == 2
assert log13["compat_count"] == 16 and log13["compat_span_rank"] == 9
Bp = [{(B0 + d,): F(1)} for d in range(7)]
F7p = [{(110 - d,): F(1)} for d in range(10)]
CF7 = [{} for _ in range(14)]
for d in range(10):
    CF7[d] = padd(CF7[d], pscale(F7p[d], -1))
    CF7[d + 4] = padd(CF7[d + 4], F7p[d])
model13 = mod_H([padd(pscale(x, 4), pscale(y, -1))
                 for x, y in zip(dense_mul(Bp, CF7) + [{}] * 9, dense_mul(Bp, Bp) + [{}] * 7)])
E = {(110, B0): F(1),
     tuple(sorted((B0, B0 + 4))): F(-1, 2),
     tuple(sorted((B0 + 1, B0 + 3))): F(-1, 2),
     (B0 + 2, B0 + 2): F(-1, 4),
     tuple(sorted((B0 + 2, B0 + 6))): F(-1, 2),
     tuple(sorted((B0 + 3, B0 + 5))): F(-1, 2),
     (B0 + 4, B0 + 4): F(-1, 4),
     (B0 + 6, B0 + 6): F(-1, 4)}
rk13m, _, _ = span_rank(model13)
rk13mE, _, _ = span_rank(model13 + [E])
rk13u, _, _ = span_rank(r13 + model13 + [E])
print(f"  rank(B(4CF7-B) mod H coeffs) = {rk13m}; +E = {rk13mE}; union with r13 = {rk13u}")
assert rk13m == 8 and rk13mE == 9 and rk13u == 9
print("  => span(r13 compats) == span(8 coeffs of B*(4*C*F7-B) mod H) + Q*E")
print(f"  E = {pstr(E)}")
mc = mod_C([padd(pscale(x, 4), pscale(y, -1))
            for x, y in zip(dense_mul(Bp, CF7) + [{}] * 9, dense_mul(Bp, Bp) + [{}] * 7)])
negB2_mod_C = mod_C(dense_mul(Bp, [pscale(p, -1) for p in Bp]))
print(f"  (4BCF7-B^2) mod C == -(B^2) mod C : {mc == negB2_mod_C}")
assert mc == negB2_mod_C
subs_BCV = {}
for d in range(7):
    val = {}
    if 0 <= d - 4 <= 2:
        val = padd(val, {(V0 + d - 4,): F(1)})
    if 0 <= d <= 2:
        val = padd(val, {(V0 + d,): F(-1)})
    subs_BCV[B0 + d] = val
E_v = psubst(E, subs_BCV)
print(f"  E under B=C*V: {pstr(E_v)}")
assert E_v == {(V0, V0): F(1, 4), (110, V0): F(-1)}
q = pmul({(V0,): F(1)}, padd({(V0,): F(1)}, {(110,): F(-4)}))
assert pscale(q, F(1, 4)) == E_v
print("  == V0*(V0-4*p110)/4 exactly  => field branches V0=0 or V0=4*p110")

# ---------- section 9: branch pipelines
print("=" * 72)
print("S9 BRANCH PIPELINES")
subs_HV = {}
for d in range(11):
    val = {}
    if 0 <= d <= 2:
        val = padd(val, {(V0 + d,): F(1)})
    if 0 <= d - 4 <= 2:
        val = padd(val, {(V0 + d - 4,): F(-2)})
    if 0 <= d - 8 <= 2:
        val = padd(val, {(V0 + d - 8,): F(1)})
    subs_HV[121 - d] = val
HVdense = [dict(subs_HV[121 - d]) for d in range(11)]
assert all(not p for p in mod_H(dense_mul(HVdense, HVdense))), "A=HV should kill A^2 mod H"
print("  symbolic check: (H*V)^2 mod H == 0  (so row-12 compats must vanish)")

# progressive-substitution audit: do stage-12/13/14 parameters appear in raw
# p-rows 14/15?  If yes, the recorded row-12/13/14 pivot substitutions are
# load-bearing for later stages; if no, they are vacuous there.
later_params = set(stages[12]) | set(stages[13]) | set(stages[14])
leak = set()
for r in (14, 15):
    for gi, c in by_row[r]:
        for m in c["poly"]:
            for v in m:
                if v in later_params:
                    leak.add((r, v, stage_of[v]))
print(f"  stage-12/13/14 parameters appearing in raw rows 14/15 (row, param, stage): "
      f"{sorted(leak)}")

results = {}
for branch in ("v0_zero", "v0_four_p110"):
    print("-" * 72)
    print(f"  BRANCH {branch}")
    bsub = {V0: {}} if branch == "v0_zero" else {V0: {(110,): F(4)}}
    subsB = {k: psubst(v, bsub) for k, v in subs_HV.items()}
    subsB.update(bsub)
    # producer-style progressive pipeline: row12 stage then row13 stage record pivots
    S = dict(subs_HV)
    r12h, log12h, ns12, _ = stage(12, stages[12], S)
    assert log12h["compat_count"] == 0
    S.update(ns12)
    r13h, log13h, ns13, _ = stage(13, stages[13], S)
    S.update(ns13)
    # apply branch substitution to everything recorded
    S = {k: psubst(v, bsub) for k, v in S.items()}
    S.update(bsub)
    r13hb = [psubst(p, bsub) for p in r13h]
    nz = [p for p in r13hb if p]
    print(f"    row-12 compats under A=HV: {log12h['compat_count']}; "
          f"row-13 compats nonzero after branch: {len(nz)} (of {len(r13h)})")
    assert not nz
    # rows 14/15 under the full progressive substitution S
    r14, log14, ns14, det14 = stage(14, stages[14], dict(S))
    S14 = dict(S)
    S15 = dict(S)
    S15.update(ns14)
    cand15 = [p for p in stages[15] if p != 32]
    r15, log15, ns15, det15 = stage(15, cand15, dict(S15))
    print(f"    log14: {log14}")
    print(f"    log15: {log15}")
    assert log14["compat_count"] == 16 and log14["compat_span_rank"] == 8
    assert log15["compat_count"] == 17 and log15["compat_span_rank"] == 17
    assert 32 not in log15["pivot_params"]
    # measured diagnostic: rows 14/15 with plain {A=HV,branch} substitution
    # versus the certified progressive pipeline
    r14_plain, log14p, _, _ = stage(14, stages[14], dict(subsB))
    r15_plain, log15p, _, _ = stage(15, cand15, dict(subsB))
    print(f"    plain {{A=HV,branch}} equals progressive: "
          f"row14={r14_plain == r14} row15={r15_plain == r15} "
          f"(if False, the recorded pivot substitutions are load-bearing)")
    r15_no14, _, _, _ = stage(15, cand15, dict(S14))
    print(f"    row-15 compats with row-12/13 pivots but WITHOUT row-14 pivots equal "
          f"certified row-15 compats: {r15_no14 == r15}")
    cum_rank, cum_basis, _ = span_rank(r14 + r15)
    print(f"    cumulative span rank(r14+r15) = {cum_rank}")
    assert cum_rank == 19
    target_sq = {(110, 110): F(1)}
    mywit = in_span_witness(r14 + r15, target_sq)
    assert mywit is not None
    print(f"    my own solved witness (index: coeff): "
          f"{ {i: str(c) for i, c in enumerate(mywit) if c} }")
    # frozen sparse witness, direct expansion
    frozen = {"v0_zero": {("r14", 1): F(1, 12), ("r14", 13): F(1, 9),
                          ("r15", 3): F(-2, 9), ("r15", 7): F(-2, 9),
                          ("r15", 11): F(-2, 9), ("r15", 15): F(-2, 9)},
              "v0_four_p110": {("r14", 9): F(-1), ("r14", 13): F(-37, 9),
                               ("r15", 3): F(16, 9), ("r15", 7): F(32, 9),
                               ("r15", 11): F(256, 45), ("r15", 15): F(512, 63)}}[branch]
    acc = {}
    for (which, i), c in sorted(frozen.items()):
        poly = r14[i] if which == "r14" else r15[i]
        acc = padd(acc, pscale(poly, c))
    print(f"    frozen sparse witness expansion == p110^2 : {acc == target_sq}")
    assert acc == target_sq
    # per-selected-compat print + hash comparison with certificate
    cert_b = cert["certificates"][branch]
    cert_hashes = {(w["stage_row"], w["stage_compatibility_index"]): w["compatibility_sha256"]
                   for w in cert_b["p110_square_pre_span_witness"]}
    cert_coeffs = {(w["stage_row"], w["stage_compatibility_index"]): F(w["coefficient"])
                   for w in cert_b["p110_square_pre_span_witness"]}
    for (which, i), c in sorted(frozen.items()):
        rowno = 14 if which == "r14" else 15
        poly = r14[i] if which == "r14" else r15[i]
        h = phash(poly)
        match = cert_hashes.get((rowno, i)) == h and cert_coeffs.get((rowno, i)) == c
        print(f"    {which}[{i}] coeff {c}: {len(poly)} terms, sha256 {h[:16]}..., "
              f"certificate match={match}")
        assert match
    # provenance: collapse witness through my tracked details, compare to certificate
    for rowno, dets, wpart in ((14, det14, [( i, frozen.get(('r14', i), F(0))) for i in range(len(r14))]),
                               (15, det15, [( i, frozen.get(('r15', i), F(0))) for i in range(len(r15))])):
        combined = {}
        for i, c in wpart:
            if not c:
                continue
            for gi, pc in dets[i][0].items():
                combined[gi] = combined.get(gi, F(0)) + c * pc
        combined = {gi: c for gi, c in combined.items() if c}
        cert_list = cert_b["source_row_provenance"][f"row{rowno}"]
        cert_comb = {int(e["constraint_index"]): F(e["coefficient"]) for e in cert_list}
        ok = combined == cert_comb
        print(f"    collapsed row-{rowno} source combination "
              f"{ {gi: str(c) for gi, c in sorted(combined.items())} } "
              f"matches certificate: {ok}")
        assert ok
        # verify combination against substituted literal source rows
        Sx = S14 if rowno == 14 else S15
        acc2 = {}
        for gi, c in combined.items():
            crec = my_constraints[gi]
            assert crec["row"] == rowno
            acc2 = padd(acc2, pscale(psubst(dict(crec["poly"]), Sx), c))
        expect = {}
        for i, c in wpart:
            if c:
                expect = padd(expect, pscale(r14[i] if rowno == 14 else r15[i], c))
        assert acc2 == expect
        print(f"      Q-combination of substituted literal source rows reproduces the "
              f"row-{rowno} witness part: True")
        if rowno == 15:
            accraw = {}
            for gi, c in combined.items():
                accraw = padd(accraw, pscale(dict(my_constraints[gi]["poly"]), c))
            print(f"      same combination on UNSUBSTITUTED raw p-rows equals witness part: "
                  f"{accraw == expect}  (must be False: substitution is load-bearing)")
            assert accraw != expect
    # membership of p110^2 in my span basis by reduction
    red = target_sq
    for b in cum_basis:
        m0 = sorted(b)[0] if b else None
    def reduce_by(basis, poly):
        mons = sorted({m for x in basis + [poly] for m in x})
        matb = [[x.get(m, F(0)) for m in mons] for x in basis]
        rb, pb, _ = rref(matb, len(mons))
        vec = [poly.get(m, F(0)) for m in mons]
        for i, pc in enumerate(pb):
            if vec[pc]:
                s = vec[pc]
                vec = [a - s * bb for a, bb in zip(vec, rb[i])]
        return {m: c for m, c in zip(mons, vec) if c}
    assert not reduce_by(cum_basis, target_sq)
    literally = target_sq in cum_basis
    print(f"    p110^2 in span of 19-dim cumulative basis: True; literally a basis element: {literally}")
    # target counts
    endpoint = {(): F(1), (32, 110): F(1)}
    constraints_out = cum_basis + [endpoint]
    opvars = sorted({v for p in constraints_out for m in p for v in m})
    maxdeg = max(len(m) for p in constraints_out for m in p)
    print(f"    target: generators={len(constraints_out)}, operative variables={len(opvars)}, "
          f"max degree={maxdeg}")
    expected_vars = 22 if branch == "v0_zero" else 23
    assert len(constraints_out) == 20 and len(opvars) == expected_vars and maxdeg == 2
    # no-division audit: every pivot coefficient inverted is a rational scalar by construction;
    # all substitution images are polynomials (dict rep cannot express division by a parameter)
    # unit identity
    u = padd(pmul({(): F(1), (32, 110): F(-1)}, endpoint),
             pmul({(32, 32): F(1)}, target_sq))
    print(f"    unit identity expansion (1-p32*p110)*(1+p32*p110)+p32^2*p110^2 = {pstr(u)}")
    assert u == {(): F(1)}
    results[branch] = {"r14": r14, "r15": r15, "det14": det14, "det15": det15,
                       "S14": S14, "S15": S15, "cum_basis": cum_basis}
    with open("/tmp/fable5_tail6_witness_polys.txt", "a") as fh:
        fh.write(f"== {branch} ==\n")
        for (which, i), c in sorted(frozen.items()):
            poly = r14[i] if which == "r14" else r15[i]
            fh.write(f"{which}[{i}]  (coeff {c}, {len(poly)} terms, sha256 {phash(poly)}):\n")
            fh.write("  " + pstr(poly) + "\n")

# ---------- section 10: live mutations (in-memory only)
print("=" * 72)
print("S10 LIVE MUTATIONS (in-memory only; frozen case untouched)")
br = results["v0_zero"]
target_sq = {(110, 110): F(1)}
# (a) witness-coefficient mutation: 1/12 -> 1/11 on r14[1]
acc = {}
for (which, i), c in sorted({("r14", 1): F(1, 11), ("r14", 13): F(1, 9),
                             ("r15", 3): F(-2, 9), ("r15", 7): F(-2, 9),
                             ("r15", 11): F(-2, 9), ("r15", 15): F(-2, 9)}.items()):
    poly = br["r14"][i] if which == "r14" else br["r15"][i]
    acc = padd(acc, pscale(poly, c))
resid = padd(acc, pscale(target_sq, F(-1)))
print(f"  (a) mutate witness coefficient of r14[1]: 1/12 -> 1/11")
print(f"      residual (= (1/132)*r14[1]) has {len(resid)} terms; residual == (1/132)*r14[1]: "
      f"{resid == pscale(br['r14'][1], F(1, 132))}")
print(f"      residual = {pstr(resid)}")
assert resid and resid == pscale(br["r14"][1], F(1, 132))
# (b) literal source-row mutation: constraint 84 (row15 x3), add +1 to monomial (110,110)
mut_constraints = [dict(c, poly=dict(c["poly"])) for c in my_constraints]
mut_constraints[84]["poly"] = padd(mut_constraints[84]["poly"], {(110, 110): F(1)})
mut_by_row15 = [(gi, mut_constraints[gi]) for gi, _ in by_row[15]]
cand15 = [p for p in stages[15] if p != 32]
r15m, log15m, _, _ = stage(15, cand15, dict(br["S15"]), constraints=mut_by_row15)
acc = {}
for (which, i), c in sorted({("r14", 1): F(1, 12), ("r14", 13): F(1, 9),
                             ("r15", 3): F(-2, 9), ("r15", 7): F(-2, 9),
                             ("r15", 11): F(-2, 9), ("r15", 15): F(-2, 9)}.items()):
    poly = br["r14"][i] if which == "r14" else r15m[i]
    acc = padd(acc, pscale(poly, c))
resid_b = padd(acc, pscale(target_sq, F(-1)))
print(f"  (b) mutate literal source row: constraint 84 (row 15, x_degree 3) += 1*(p110^2); "
      f"re-run row-15 elimination")
print(f"      mutated-stage log15: rank={log15m['rank']} compat_count={log15m['compat_count']}")
print(f"      residual of frozen witness expansion = {pstr(resid_b)}")
print(f"      predicted -2/9*p110^2 (collapsed coefficient of row 84 is -2/9): "
      f"{resid_b == {(110, 110): F(-2, 9)}}")
assert resid_b == {(110, 110): F(-2, 9)}
print("  both mutations fail loudly with exact nonzero residual polynomials")

print("=" * 72)
print("ALL INDEPENDENT CHECKS PASS")
```

FINAL VERDICT: CONFIRMED
