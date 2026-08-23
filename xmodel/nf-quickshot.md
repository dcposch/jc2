# NF quick-shot: the D23 compat rows modulo the banked D21 fiber GB

[2026-08-19 ~06:50Z; INTERNAL / UNREVIEWED — no promotion claims.
Question tested: is the depth-23 kill decidable by NORMAL-FORM REDUCTION
of the 6 row22red compatibility rows against the banked 397-element D21
fiber Groebner bases, with NO new GB computation?  ANSWER: NO — all six
NFs are nonconstant at all three primes — but the reduced forms collapse
1218 terms/deg 9 -> 150 terms/deg 5, are affine in 4 window vars, have
rank 5, and are banked as the warm-start payload
(cases/nf_reduced_rows_p{105337,105673,200257}.txt).]

## 1. Step-0 structural verdict (wrong-object gate — resolved BEFORE any reduction)

**(a) The banked GB object** (7.S3/7.S4): msolve reduced GBs of
directionb_core2_fiber_p*.ms (24 max-pivot echelon rows + 2 uW rows).
Sources: box01 ~/jc72108/directionb_core2_fiber_p105337.out (byte-equal
md5 to the promoted cases/directionb_fiber_gb_p105337.out.txt),
fiber_p105673.out, fiber_p200257.out (10.5–10.7 MB; scp'd, md5 equal to
the copies already in the session scratchpad fibergb/).  Ring = F_p in
**22 variables** = the 18 CORE2 template coords
{x68,x70–x73,x47,x52–x55,x57–x60,x62,x63,x65,x66} **+ W1,W2,uW1,uW2**,
term order **grevlex (DRL) in exactly that printed variable order**;
397 elements, monic, interreduced; 282,304 total terms at every prime
(cross-prime support identity echo).  The uW rows are IN the ideal, so
V(GB) is the chart-saturated (W invertible) fiber locus.

**(b) Per-fiber vs family**: this is a **PER-FIBER object at the
specialized radical_point base, per prime** — the unsplit CORE2 ring has
base/radical coordinates A1,A2,HW1,HW2,uA, and the fiber emission
specializes ALL of them at the radical point mod p, keeping only
W1,W2,uW1,uW2 symbolic ("W-symbolic").  It is NOT a family object: the
"13-dim" of 7.S4 is the dimension of this one fiber locus, not a base
window.  Any NF conclusion is therefore per-fiber (radical_point chart
fiber), per-prime, all-W on that fiber.

**(c) The compat rows** (8.S2/8.S4): rows 24..29 of
cases/directionb_row22red_p*.ms (order preserved from the Schur rows
c = L·b, pre-multiplied by the per-prime nonzero constant U =
23190/10684/116004 after the 22-pivot elimination).  Ring = **29
variables** = the fiber ring's 22 **+ 7 extras**
{x16=tg1_43, x17=tg1_44, x24=tg2_43, x25=tg2_44, x32=tg01_44,
x37=tg02_44, x69=uf24}; all 7 occur in every one of the six rows
(sizes 1218 x5 + 1216, deg 9, no uW content — matches the banked 8.S4
census).  These extras are **D21-fiber-FREE window variables** (absent
from the 26-row fiber system; existentially quantified in the extension
problem alongside the deep tails).

**Verdict: the compat rows do NOT lie in the fiber GB's polynomial
ring.**  No silent specialization was performed.  The reduction was
computed treating the 7 extras as parameters, which is sound here
because the required order exists: extend grevlex(fiber22) to the
**block order (dp(fiber22) >> dp(extras7))**.  A reduced grevlex GB
G ⊂ F_p[X] remains a Groebner basis of the extension ideal I^e ⊂
F_p[X,Y] for the X-dominant block order (collect any f ∈ I^e by
Y-monomials: f = Σ n(Y)·f_n(X) with f_n ∈ I; the block-LT of f has
X-part = LM of some f_n, divisible by some LT(g)); hence the division
NFs below are CANONICAL, and always row − NF ∈ I^e, i.e. **NF ≡ row
identically on V(GB) × A^7_extras**.

## 2. Method + gates (all PASS)

Pipeline (scratchpad nfq/{nfq_build,nfq_gates,nfq_affine,nfq_emit}.py;
GB parser reused from cases/valuation_e.py parse_msolve_out; .ms parser
parse_ms_rows; Singular 4.4.1 batch `Singular -q < script`, never
interactive; **no msolve, no new GB computation**; wall ≈ 0.7 s/prime).

- **G-A order pin, x3 primes**: under an independent DRL comparator in
  msolve's printed variable order, every first-printed term of the 397
  basis elements is the unique DRL-max AND monic (LC=1 — a ~1/p
  coincidence per poly if the order were misread), and the basis is
  interreduced: exactly 397 (term, LT) divisibility hits among all
  282,304 terms.  Pins msolve grevlex == Singular dp on this variable
  sequence.
- **G-B Singular sanity, x3**: reduce(G[1],G) = reduce(G[200],G) =
  reduce(G[397],G) = 0; reduce(1,G) = 1.
- **G-C end-to-end identity**: row_j == NF_j evaluated at verified
  V(GB) F_p-points (all 397 GB elements vanish — asserted) × 3 random
  draws of the 7 extras × 6 rows: **72/72 at 105337** (the banked 12
  points, first 4) and **72/72 at 105673** (fresh seed-2026 sample).
  At 200257 there are no F_p-rational chart points (W^4 pins
  non-4th-powers; the banked 8.S3 fail-closed reason), so G-C is not
  applicable there; the identity holds by construction and the NF
  support is cross-prime identical (below).
- **G-D emission round-trip, x3**: cases/nf_reduced_rows_p*.txt
  re-parsed by an independent parser == the parsed Singular output,
  dict-exact; coefficients normalized to [0,p); kernel identity
  Σ a_j·NF_j == 0 re-verified exactly on the emitted forms.

## 3. Results (identical shape at p = 105337, 105673, 200257)

Per-row NFs (row numbering = row22red rows 24..29, Schur order):

| row | input terms/deg | NF terms | NF deg | deg in extras | const term | NF == 0? | NF == const? |
|-----|-----------------|----------|--------|---------------|------------|----------|--------------|
| 24  | 1218 / 9        | 150      | 5      | 1             | 0          | no       | no           |
| 25  | 1218 / 9        | 150      | 5      | 1             | 0          | no       | no           |
| 26  | 1218 / 9        | 150      | 5      | 1             | 0          | no       | no           |
| 27  | 1218 / 9        | 150      | 5      | 1             | 0          | no       | no           |
| 28  | 1218 / 9        | 150      | 5      | 1             | 0          | no       | no           |
| 29  | 1216 / 9        | 150      | 5      | 1             | 0          | no       | no           |

Structure of the payload (all three primes):

- **No row reduced to zero and none to a (nonzero) constant** — the
  quick-shot decision test is NEGATIVE at every prime.
- All six NFs share **ONE common 150-monomial support**, and that
  support is **identical row-for-row across the three primes** (the
  familiar cross-prime pattern gate, passed by the NFs too).
- Each NF is **AFFINE (degree 1) in the four level-44 window tails**
  x17=tg1_44, x25=tg2_44, x32=tg01_44, x37=tg02_44 (never a product of
  two extras, never degree >1); the other three extras
  **x16=tg1_43, x24=tg2_43, x69=uf24 cancel entirely** — modulo the
  fiber ideal the compatibility condition does not depend on them.
  x47 and x52 (the GB's two linear pivots) are also eliminated.
- **Rank of the six NFs = 5** over F_p at each prime: one exact linear
  dependency (kernel, normalized: [1,58526,64401,35257,74853,58238] @
  105337; [1,93937,29382,35369,63348,105378] @ 105673;
  [1,44507,189160,66897,97147,85205] @ 200257; Σ a_j·NF_j == 0 as
  polynomials).  On the fiber the compat block is really 5 conditions.

Bonus per-point upgrade (evaluation only, no solver): at a fiber point
the reduced system is a 6×4 AFFINE system over F_p in
(x17,x25,x32,x37).  Rank test rank(A) vs rank([A|b]):
**12/12 banked points at 105337 and 12/12 fresh seed-2026 points at
105673 are INCONSISTENT** — each sampled D21 fiber point fails to
extend through depth 23 for **ALL values of the free window tails**
(the 7.S4/8.S2 filter verdict reproduced with the aux quantifier
upgraded from "3 sampled draws" to "for all"; x16/x24/x69 provably
irrelevant).  0/24 solvable.

## 4. What IS and is NOT proved

PROVED (modulo the frozen artifacts + msolve's GB claim + Singular's
division, gated above; all mod p, INTERNAL/UNREVIEWED):

1. NF_j ≡ row22red-row_j on V(fiberGB) × A^7 (canonical block-order
   NFs; exact polynomial identities row − NF ∈ I^e).
2. Hence on the radical_point chart fiber: {compat c = 0} ⇔
   {NF_1..NF_6 = 0}, and **V(row22red) = V(397-GB ∪ 6 NFs)** as
   subsets of the 29-var chart (same ideal: the GB generates the
   24-core+2-uW ideal; the 6 rows are congruent to the NFs mod it).
   The D23-emptiness question is carried VERBATIM to the smaller
   object.
3. The compat block mod the fiber has rank 5, is affine in the 4
   level-44 tg's, and is independent of tg1_43, tg2_43, uf24.
4. 24/24 sampled fiber points (2 primes) are killed at depth 23 for
   all aux values.

NOT PROVED — scrupulously:

- **No variety-level D23 kill.**  A nonconstant NF says the compat row
  is not a unit on the fiber ring's quotient — it does NOT say the row
  has (or lacks) zeros on the 13-dim fiber LOCUS; conversely the 24
  point-kills are sampling, not emptiness.  Emptiness of
  V(fiberGB + NFs) (equivalently row22red) remains with the solver
  lanes / warm-start run.
- **Per-fiber only, not family**: everything is at the specialized
  radical_point base; nothing is claimed for other base points of the
  tower, other charts, or any window family.
- **Per-prime mod p only**: no char-0 statement; at 200257 the
  pointwise gate/test could not run over F_p (no rational chart
  points) — the NF algebra there is construction-certified only.
- Inherits the row22red equivalence gates (8.S4: U a unit constant,
  back-solve round-trip) and msolve's correctness for the banked GBs.
  No independent re-derivation of either was attempted here.

## 5. Warm-start consumption (the payload contract)

Files: **cases/nf_reduced_rows_p{105337,105673,200257}.txt** ('#'
provenance header; stripping '#' lines leaves an .ms-shaped body:
vars line / characteristic / 6 comma-joined rows).

- **Ring**: the 29 listed variables, in the payload's order = the 22
  fiber GB vars **in msolve's fiber order** (x68,x70,x71,x72,x73,x47,
  x52,x53,x54,x55,x57,x58,x59,x60,x62,x63,x65,x66,W1,W2,uW1,uW2)
  followed by the 7 parameters (x16,x17,x24,x25,x32,x37,x69).  Only
  26 variables actually occur (22 fiber + x17,x25,x32,x37).
- **Order**: the NFs are canonical w.r.t. the block order
  **(dp(fiber22) >> dp(extras7))**; any consumer that keeps the fiber
  block dominant (e.g. Singular (dp(22),dp(7)); msolve grevlex on the
  26 occurring vars is a DIFFERENT order — legal as input generators,
  but then the forms are just generators, not NFs).
- **Parameters**: x16,x24,x69 are absent — genuinely free (factor
  A^3); x17,x25,x32,x37 are unknowns of the D23 condition.
- **Warm-start emission** (the ratified accelerant): feed the solver
  the 397 GB elements VERBATIM (already a reduced grevlex GB of their
  ideal — a zero-cost prefix for the engine) + the 6 NF rows (900
  terms) in the fiber-order ring above; V of that input == V(row22red)
  on the chart, with 43 fewer variables than row22compat and the 12h+
  timeout object replaced by a GB-plus-6-rows input.  Do NOT mix in
  the original 1218-term rows (redundant) or reorder the fiber block
  (breaks the GB-prefix property).

Provenance sha256 (first 16 hex): GBs 92e274d7076c9a57 (105337; ==
banked cases/directionb_fiber_gb_p105337.out.txt), fiber_p105673.out /
fiber_p200257.out as scp'd 2026-08-19 and md5-matched to box01;
row22red .ms 5d4a181545711f81 (105337) — full hashes in the payload
headers.  Scripts: scratchpad nfq/ (session e1e34384).  No git.
