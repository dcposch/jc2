# D43 `a00pp` sparse-tail elimination: independent reconstruction R1

**UTC:** 2026-08-28T20:16:46Z  
**Role:** independent mathematical audit; read-only with respect to both row
producer packets  
**Scope:** residue A, `B=84`, `a00pp`, `PIN42`,
`Xf_alpha=Xg_beta=0`, common 22-tail support  
**Verdict:** **PROMISING LOCAL ELIMINATION SHAPE / EXACT SEVEN-POLYNOMIAL
ARTIFACT NOT YET EMITTED / NO LAUNCH**

This report reconstructs exactly what follows from the presently frozen
sources and what does not.  It does not assert a characteristic-zero point,
full-template existence, equivalence with the banked normal-form
presentation, all-depth compatibility, a Keller map, or anything about JC2.
No CAS or AWS job was run.  The only new computation was a 0.5-second
standard-library modular row-basis check on the two already committed
pointbanks.

## 1. Typing: four displayed W symbols collapse to two coordinates

Before the fiber specialization, an `R_ext` monomial is keyed by

```text
(z,A1,A2,W1,HW1,W2,HW2,EB).
```

The literal `a00pp` map in
`cases/d43_common_integral_emitter.py:234-274` imposes

```text
HW1 = h*W1,       HW2 = h*W2,       EB exponent = 0,
2*h^2 = 3.
```

Therefore the canonical collapsed coefficient ring is

```text
K0[W1,W2],
K0 = Q[zeta42,r3,A1,A2,h]/
     (Phi42, r3^2-3, A1^3-(3+r3), A2^3-(3-r3), 2*h^2-3).
```

Its displayed basis has rank at most 432 over `Q`.  Initially this is a
finite quotient algebra, not automatically a field; a solver must prove a
field component or decompose the finite etale algebra componentwise.

If a four-symbol presentation
`W=(W1,W2,HW1,HW2)` is desired for provenance, it must be the quotient

```text
K0[W1,W2,HW1,HW2]/(HW1-h*W1, HW2-h*W2),
```

not a polynomial ring in four independent W variables.  The seven tail
compatibilities below live canonically in two independent W coordinates.
The two displayed collapse relations are not two additional J residuals.

The current packet `cases/d43_exact_sparse_rows_20260828/` does not perform
this collapse.  It retains independent `HW1,HW2` and the `EB` generator in
the rank-6048 selector algebra.  Thus that packet cannot yet certify the
claimed rank-432 `a00pp` row census or the elimination described here.

## 2. Reconstruction of the 29-row / 22-tail claim

The common support, in the deterministic lexical column order used below,
is

```text
tf1_57 tf1_62 tf1_67 tf1_72
tf2_57 tf2_62 tf2_67 tf2_72
tg01_62 tg02_62 tg1_57 tg2_57
x12 x15 x20 x23 x28 x31 x36 x4 x41 x7.
```

The shallow x/source translation is

```text
x4=tf1_47,  x7=tf1_52,   x12=tf2_47, x15=tf2_52,
x20=tg1_47, x23=tg1_52,  x28=tg2_47, x31=tg2_52,
x36=tg01_52,              x41=tg02_52.
```

The sealed Opus audit reports a source-first scratch replay with the
following shape at both registered residues:

| item | reported value |
|---|---:|
| canonical raw-J rows | 184 |
| identically dead after the proposed support specialization | 155 |
| live rows | 29 |
| live `(slot:count)` bands | `20:10, 30:9, 40:10` |
| maximum total tail degree | 2 |
| tail-Jacobian rank at the witness | 22 |

The committed modular pointbanks independently have exactly the same
29-row band census and degree bound.  Their block shapes are:

| slot | rows | variables first appearing at this slot | rank in those new variables after earlier witness values are inserted |
|---:|---:|---:|---:|
| 20 | 10 | 10 | 4 |
| 30 | 9 | 8 | 4 |
| 40 | 10 | 4 | 4 |

The `4/4/4` statement is not the full tail rank: later rows also constrain
the unresolved earlier tails.  The full 29-by-22 Jacobian can therefore have
rank 22 even though each diagonal new-variable block has rank four.  Nor
does `29-22=7` by itself say that a global elimination ideal has seven
minimal polynomial generators.  It says that on a 22-tail etale chart one
may use 22 equations to define the local tail branch and retain the other
seven source equations as compatibility conditions.

Exact evidence presently committed is smaller:

* `directionb_tails_D21.pkl`, after the literal collapse, gives the ten
  exact slot-20 affine source rows in the ten shallow tails.  Both registered
  specializations have coefficient and augmented rank four.  This proves an
  exact source-side lower block and an exact rank lower bound, not the global
  rank-22 upper/lower certificate.
* `cases/d43_char0_lift.py:240-266` is an independent numeric source
  evaluator for all 184 canonical rows.
* `cases/d43_exact_sparse_rows_20260828/selected_rows.py:251-272` implements
  the correct selected-component source formula, but currently emits it in
  the uncollapsed selector algebra.

What is still absent is a hash-sealed all-184 row object over the collapsed
`K0[W1,W2]`, including exact identities for the 155 zero rows.  Consequently
the sealed Opus counts are high-quality independent diagnostics, not a
replayable exact characteristic-zero row certificate.

## 3. A common candidate 22-row chart and its seven residual labels

Write `R[s,eta]` for the restricted raw source row; this follows the modular
pointbank label order `(slot,eta)`.  A deterministic standard-library check
formed the Jacobian in the 22 lexical tail columns at each committed modular
witness, scanned columns lexically, and selected the first surviving row
pivot after exact finite-field elimination.  It chose the same ordered row
basis at both primes:

```text
P = [
 (30,2), (30,5), (40,1), (40,4), (30,8), (30,11),
 (40,7), (40,10), (40,13), (40,16), (40,19), (40,22),
 (20,12), (20,15), (30,14), (30,17), (30,20), (30,23),
 (20,6), (20,9), (40,25), (40,28)
].
```

For the pointbank Jacobians, the corresponding ordered 22-by-22 determinant
is

```text
42703 mod 105337,
82971 mod 105673.
```

Both are nonzero.  The seven complementary labels are

```text
Q = [
 (20,0), (20,3), (20,18), (20,21),
 (20,24), (20,27), (30,26)
].
```

In the producer's `(eta,slot)` convention these are

```text
(0,20), (3,20), (18,20), (21,20),
(24,20), (27,20), (26,30).
```

This identifies a clean candidate set of seven residual *source rows*.  It
does not yet provide seven explicit W-polynomials.  The determinants above
belong to the frozen modular banked presentation; they are a reproducible
chart-selection diagnostic, not a substitute for the missing exact
collapsed raw-source minor.  The source producer must emit the exact rows
and either confirm this chart or record the exact chart it actually uses.

The correct local definition is as follows.  Let `T` be the 22-tail vector,
let

```text
I_P = (R[p] : p in P) in K0[W1,W2,T],
Delta = det(d(R[p]:p in P)/dT),
A_Delta = (K0[W1,W2,T]/I_P)[1/Delta].
```

If the exact `Delta` is nonzero on the desired component, the seven local
compatibilities are precisely

```text
C[q] := class of R[q] in A_Delta,       q in Q.
```

They are rigorous residual equations in the etale tail algebra.  To publish
literal W-only polynomials, the producer must additionally compute and
certify

```text
J_W = ((R[s,eta] for all 29 live labels) : Delta^infinity)
      intersect K0[W1,W2],
```

or an equivalent rational-univariate/finite-algebra representation.  An
invertible Jacobian gives an implicit local tail branch; it does not by
itself prove that all 22 tails are rational polynomial functions of W.
Likewise, the number seven is the number of leftover source rows on this
chart, not a proof that `J_W` has exactly seven minimal generators globally.

Thus the strongest presently defensible identification is

```text
C[20,0], C[20,3], C[20,18], C[20,21],
C[20,24], C[20,27], C[30,26],
```

with each `C` defined by exact reduction in `A_Delta`.  Their expanded
coefficients still require emitted source rows.

## 4. Cleanest exact solve and certificate

### 4.1 Emit before solving

The repaired producer should first emit all 184 rows in canonical
`K0[W1,W2,T]` form, with all of the following literal:

* the 326-name tail complement, the named `uf/vf` coordinates, all six
  level-74 `PIN42` tails, and `Xf_alpha,Xg_beta` are zero;
* fixed B-orbit constants are retained;
* `HW1=h*W1`, `HW2=h*W2` are applied source-first;
* `+42` occurs once, in `R[20,0]`;
* every one of the 184 target labels is retained, including the 155 exact
  zero rows.

The output gate is exact `155 zero + 29 live`, the stated band census,
degree at most two, an exact 22-tail minor, and re-specialization to both
registered residues.  Any mismatch is an adapter failure, not mathematics.

### 4.2 Keep the finite coefficient algebra honest

Do not divide in the rank-432 quotient merely because a coefficient is
nonzero.  Either:

1. factor/decompose the finite etale `K0` algebra and solve every component;
   or
2. prove a primitive-element field presentation for each retained component
   and transport all rows with exact inverse maps.

The two finite-field embeddings are regression points; they do not select a
unique characteristic-zero component.

### 4.3 Use E early, but retain every ratio branch

Put

```text
a1=3+r3,  a2=3-r3,
E=(9+5*r3)*A1*W1^4 + (9-5*r3)*A2*W2^4.
```

On `W1*W2 != 0`, introduce `q=W1/W2` and `s=W2`.  Then

```text
q^4 = (15*r3-26)*A2/A1,       W1=q*s,       W2=s.
```

This removes one W dimension without pinning the common scale.  Work in the
whole squarefree quotient for `q`, or factor it and retain every factor;
selecting only the modularly banked fourth root would be circular.  The
reported degree-six scale polynomial modulo 105337 is useful reconnaissance,
not an exact lift.

### 4.4 Preferred algebraic engine

The smallest robust solve is a block-elimination/RUR computation for

```text
I = (29 exact J rows, E, tW*W1*W2-1, K0 defining relations),
```

with tail variables eliminated before `(q,s)` and with the candidate
`Delta` chart explicitly saturated.  A fraction-free Groebner basis or
Macaulay/F4 computation is acceptable only if it emits exact generator
traces.  Modular computations may choose orders and primes, but promotion
requires exact-Q/component replay.

On `D(Delta)`, reduce the seven `Q` rows in the exact algebra defined by the
22 `P` rows.  A rational univariate representation is preferable to
printing enormous expanded W resultants: it preserves branches, supplies a
squarefree isolating polynomial, and allows exact zero/unit tests.  Then
recurse on `Delta=0`; the witness chart alone cannot prove a whole-scheme
existence or emptiness statement.

Required terminal certificates are:

* **empty:** an exact ideal-membership identity for `1` after all claimed
  saturations and coefficient components, plus a separately checked
  `Delta=0` complement if the claim is global;
* **nonempty:** an exact number-field/RUR candidate with every defining
  polynomial and unit denominator checked, followed by direct replay of all
  184 raw source rows;
* **chart-only:** an exact result explicitly labelled `D(Delta)` if the
  complement was not closed.

### 4.5 Literal E5/E6 reconstruction is a mandatory promotion gate

Let

```text
S_M = 7^12/2^6,
C   = 243*S_M^3*(a1-a2)^4,
U   = A1*W1^4,
V   = A2*W2^4.
```

From an exact candidate satisfying `E=0` and the W units, reconstruct

```text
HM = -C*a1^2*U / (4*(a1-4))
   = -C*a2^2*V / (4*(a2-4)),
s1F = (2^8/7^16)*HM,
tSAT = s1F^(-1).
```

Then replay literally, without simplifying them away,

```text
4*(a1-4)*HM + C*a1^2*U = 0,
4*(a2-4)*HM + C*a2^2*V = 0,
2^24*HM^3 - 7^48*s1F^3 = 0,
s1F*tSAT - 1 = 0,
```

as well as the exact W-unit rows used by the template.  This proves only the
displayed E5/E6/unit extension.  Every other residue-A/template equation
remains a separate replay obligation.

## 5. Evidence boundary

| statement | present status |
|---|---|
| selected raw-J formula and canonical 184-target registry | exact committed source |
| literal `a00pp` collapse map | exact committed source |
| ten slot-20 affine rows after collapse | exact D21 artifact |
| E plus W units is the existential projection of displayed E5/E6/unit subsystem | exact reviewed algebraic bridge |
| 29 live rows, bands 20/30/40, degree at most two | two-prime banked replay plus sealed source-first Opus diagnostic |
| tail rank 22 at both witnesses | sealed source-first Opus diagnostic; exact minor not emitted |
| common candidate pivot/residual labels and nonzero modular determinants above | reproducible banked modular diagnostic only |
| exact 155 zero-row identities | missing |
| exact collapsed 29-row payload | missing |
| expanded seven W residuals or certified RUR equivalent | missing |
| exact solution or exact emptiness certificate | missing |
| all-184 exact candidate replay | missing |

The present correct mathematical verdict is therefore **NO_VERDICT on exact
finite-J existence**.  The small chart is well motivated, and the seven row
labels above are a concrete target for the repaired emitter, but no exact
telescoping/elimination certificate has yet been produced.

## 6. Bounded AWS-ready job specification (not launched)

After a repaired producer packet receives independent PASS, use one isolated
AWS worker, one pinned core, at most 256 GiB RAM, zero swap, and a two-hour
hard cap for the first exact chart.  Bind all source hashes below and the new
collapsed-row archive hash.  Stages are:

1. exact 184-row emission and `155/29` census;
2. exact D21 equality, HW-sign and `+42` mutations;
3. exact 22-minor selection and two-prime regression;
4. component-safe `D(Delta)` elimination with `E` and W units;
5. exact certificate parse and all-184 plus literal E5/E6 replay;
6. atomic archive/manifest promotion only after worker rc 0, zero swap,
   resource compliance, and zero tagged descendants/orphans.

Fail-closed terminal markers should distinguish

```text
ADAPTER_FAILURE_NO_VERDICT
SOURCE_CENSUS_MISMATCH_NO_VERDICT
COEFFICIENT_COMPONENT_UNRESOLVED_NO_VERDICT
RANK_CHART_MISMATCH_NO_VERDICT
TIMEOUT_NO_VERDICT
EXACT_DDELTA_EMPTY_CERTIFICATE
EXACT_DDELTA_CANDIDATE_REPLAY_PASS
EXACT_GLOBAL_EMPTY_CERTIFICATE
```

No modular rank, timeout, or adapter failure is a mathematical verdict.

## 7. Frozen inputs inspected

```text
456edb3ad982da10c13ebe6f41e9ebdf7e7124e1ae4ef76363f253626ad5fea0  xmodel/d43-exact-sparse-source-opus5-hostile-audit-20260828.md
283d47df4f55a0e83fbf1758cc8ac71fbe5ee8549dcdb1c3a6838c8ccc42b21e  xmodel/d43-exact-sparse-rows-hostile-review-gpt56-20260828.md
e1b99600b01f91f7b95df4f7f969481efa1e7b1ee377e83156f3f6b6a8e3c863  xmodel/d43-e5-e6-elimination-bridge-gpt56-20260828.md
480c7dcd52543a438cf9588d4842273c717cc3695bade2ff87c923b9d9ea262c  xmodel/d43-direct-exact-sparse-source-preflight-gpt56-20260828.md
6b873ac1b7bf9cb8513876a13ccf8b5ffe6c845f247b40972c3d023c0a97762a  cases/d43_char0_lift.py
5420b5c0b4164c719e98316cade96c094c2945a6fed8bad3ac0926771855984d  cases/d43_common_integral_emitter.py
504341d6a26dccf18ee83db21bc02d36cd5e58651e251043ec76ecbdb34aa4f5  cases/d43_exact_sparse_source_preflight.py
05c244b6bf19334d61bdd79835b56f6e1f8cf8f4e3556e6eea51330c4d705755  cases/d43_exact_sparse_rows_20260828/selected_rows.py
d18e03f989043fc3c7b1b79442107831602559db79781cc8d89e3109b800f435  cases/d43_exact_sparse_rows_20260828/PILOT_MANIFEST.json
b4ba8dfcd9755fb3201780cd97c1d2ef38bd26d2d1b023521a0e62a3d6db169e  directionb_tails_D21.pkl
bb0f13b61616c486116027e284483a4fb0f529f8df2dca7f728d56584d98fcbb  cases/d43_full_pointbank_p105337.pkl
b933cdb5b72bd4073da0cb82150db768f6b4607d5cd29d3d4aec0fe22ce5bcc3  cases/d43_full_pointbank_p105673.pkl
6e50a00f651b4e6ea0a5666d7507c499ff86e86d7eed9c0c17cd7add247eec7c  cases/d43_full_certificate_p105337.json
3c2bef3987cb4644c49f992cacbe36f688ecf97cfcdbe32f83267f749b1f58d9  cases/d43_full_certificate_p105673.json
```

Diagnostic registry hashes (newline-delimited order exactly as printed in
this report's calculation) are:

```text
3751a2f1855aed74fccf03c2be4944bbd2140e1d1ee98efe528842da6cfb9f3f  lexical 22-tail support
494532c74106fecd93991da39c97c2aa2155add4070851a200db349637bc8721  ordered 22 pivot labels
c19b5390f3ef42fbc28ebd0dbbcf5e737da1d53368c3b85a35b1b8815584ae18  ordered seven residual labels
```
