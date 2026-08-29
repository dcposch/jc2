# Hostile review: D5G35 complete raw determinant range and conditional R7R1 cutoffs

Reviewer: Grok 4.6 (xAI), CLI `grok 1.0.5 (5115b46bc909)`, Python 3.14.6  
Date: 2026-08-27  
Producer: OpenAI Sol/Sol2  
Charge: independently reconstruct the complete D3-supported raw determinant
`D0,...,D35`, the frozen unsolved target gate, the D5G byte-identity
through `D22`, and the typed R7R1 cutoff interface.

Producer PASS strings, stored counters, and the same-file `--check` replay
were treated as claims, not evidence.  The D5G Sol Ultra audit was read
only for custody/scope.  Corrected R7R1 was used only to type-check the
cutoff table, not as evidence for the compiler.  No file in `jc2-lean`
was read or touched.  No canonical ledger, case, or source artifact was
edited.  This is the only file written.

## Overall verdict

**CONFIRMED.**

The frozen D3 alphabet is the complete `2S/3S` lattice, not a weight-22
truncation: positive rows stop at weights 14 for `F` and 21 for `G`, so
the source-supported pair-sum ceiling is 35 and no determinant row above
35 exists.  The displayed recurrence, including both signs, is the
coefficient of `t^n` in `E=12 F_X G-8 F G_X-t(F_X G_t-F_t G_X)`.  An
independent four-product sparse engine, which does not call the producer
recurrence, reproduces every stored final term and every serialized
contribution through `D35`.  Rows `D0,...,D22` are compact-JSON-byte
identical to frozen D5G as complete row objects.  `D34` is genuinely
nonzero with four exact terms; `D35` is identically zero by the displayed
`-18+18` cancellation.  The true highest potentially nonzero row is
`D34`.  The exact target gate is the 734 coefficient equations of
`D0=...=D21=0, D22=1, D23=...=D34=0` together with a redundant checked
`D35=0`.  It is frozen `UNSOLVED`.  No existence, emptiness, source
equation, specialization, landing, face/family, `G2-PSC`, `G2-BD`,
counterexample, or JC2 theorem follows.

---

## Execution disclosure

Independent exact engines were run in this session (Fractions and
dictionaries only; no CAS, no AWS, no producer import):

1. Full SHA-256 recomputation of the D5G35 freeze, D3 source, D5G
   predecessor freeze, D22 certificate, producer report, and every
   RESULT pin.
2. Lattice enumeration of the `2S/3S` polygons, compared slot-by-slot
   against D3 `RAW_INPUT.json` chart images and weights.
3. Hand derivation of `E` from the chart Jacobian, then of `D_n`.
4. Independent sparse four-product compiler
   `12 F_X G - 8 F G_X - t F_X G_t + t F_t G_X` over
   `C[X]`, `C=Q[400 named slots]`, through `t^35`.
5. Independent pair-expansion of the recurrence, including contribution
   serialization and recombination of every contribution list into final
   terms.
6. Compact-JSON byte comparison of `direct["D"][0:23]` with frozen D5G,
   and of `D22` terms with `D22_CERTIFICATE.json`.
7. Hand reconstruction of `D34` and `D35`, plus representative exact
   `D23`/`D24` terms from source exponents.
8. Independent rebuild of `TARGET_GATE.json` (734 generators).
9. Independent dense four-product engine in `Q[X,t]/(t^36)` on the
   producer assignment and on a SHA-derived alternate assignment.
10. Producer `--check` replay, recorded only as self-consistency of the
    frozen writer; it is not a proof.

---

## Item 1 — SHA-256 pins and freeze (custody, not mathematics)

**Verdict: CONFIRMED.**  Every charged hash matches independently
recomputed SHA-256.  A matching hash is custody of bytes, not a proof of
the polynomials those bytes claim to represent.

### D5G35 freeze (`cases/ggv_8_28_raw_global_determinant_d5g35_20260827/`)

The case directory contains exactly the eight freeze-listed files plus
`FREEZE.sha256` itself.  Independently recomputed:

```text
3eb156e7400abbf0fe0e21f705d5246d681b911fc1eff8ebec4db1b38e303b95  PREREGISTRATION.md
1131ebafe5fdd60dc062e2796c283352bbd1c13ac505c71b7db5174d32804258  STRUCTURAL_D35_ADDENDUM.md
bbeddd37e5adebcfcd7e666e444e5d91bf5e18d51e048fe739512695b6efbeea  README.md
b066920acaed74c792b2afccec2ba372b8e516c268d262e741b333d1092b90ec  compile_d5g35.py
c2b50ac6515477fb227aaaecfad44305d44a1286c49d37fc94783afd28612a70  DIRECT_DETERMINANT_D0_D35.json
31c9a0ba1cfa600d8eeabe85b206cc18a47e621d58ddd7f52beb464c8bf6ae65  TARGET_GATE.json
b29b9efc26faaadf2b9d6ba5f46a25d42ac3326d3c3e1e836630f843e1978b67  RESULT.json
f0fe0f5dd01d9d47f6b7ee58d3e3426e482a4f8c9d31a81bfa2094782d010e00  xmodel/ggv-8_28-raw-global-determinant-d5g35-sol2-20260827.md
```

`DIRECT_DETERMINANT_D0_D35.json` and `TARGET_GATE.json` are compact
`sort_keys` JSON; `RESULT.json` is pretty-printed `sort_keys` JSON.  Each
equals the canonical encoding of the parsed object, so the freeze pins
the mathematical payload and not an accidental pretty-print variant.

### Literal D3 source and predecessor D5G

```text
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
838b1160f3ddf38fcbf360bd200ee2057e72da2b1b0ba8788d43b83720cdd043  cases/ggv_8_28_raw_global_determinant_d5g_20260827/FREEZE.sha256
069ab7a5fdb133aa2ffb0063e5f36c5664a070798de6ea00520698207e24838d  cases/ggv_8_28_raw_global_determinant_d5g_20260827/DIRECT_DETERMINANT.json
6346ab6afb307fea83516f742ca53b90e5eb8d42c2e1d5bef083920de23e434a  cases/ggv_8_28_raw_global_determinant_d5g_20260827/D22_CERTIFICATE.json
59e9bf2c6713b84ef848bae693a7e88f62c679ff56bad34fce4d3a28548663f3  xmodel/ggv-8_28-raw-global-determinant-d5g-sol-20260827.md
14913814fce76629836da359f630727b92167d3a23912c9fa265ac8d71f800d2  xmodel/ggv-8_28-raw-global-determinant-d5g-hostile-audit-sol-ultra-20260827.md
```

Every line of the frozen D5G `FREEZE.sha256` was rechecked against the
predecessor files and matches.  The D22 certificate hash is the same
object D5G35 asserts is reused unchanged.

### Transitively pinned R7R1 cutoff sources (interface typing only)

```text
2dd9d8f11e0fadff303c8afade0c1f4e52f1a1df4b5afffcea17d5e3d7890a18  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7-hostile-audit-sol2-20260827.md
489647cf5726c46401f4c48c394de64d01ff73fff3a5d3168231428add1c0ea5  cases/ggv_quarter_root_characteristic_r7r1_20260827/FREEZE.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
1cdf577a2775e7cb1b9c44d0f92edeb6f612a1b52aa659a280390b37d49babaa  cases/ggv_quarter_root_characteristic_r7r1_20260827/verify_r7r1.py
dd2ae15c4d33837aa65972070980bb0500ceeb41f6daa5c5d5775a623bfe8419  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-hostile-review-fable5-prompt-20260827.md
7ab758fa002c75cd28d81540e8f63fd8cd0de97fad791afedfeb5fb610c6cb29  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-hostile-review-fable5-20260827.md
```

The last hash is not a D5G35 pin.  Frozen `RESULT.json` still records
`PROVISIONAL CORRECTED R7R1; DIFFERENT-MODEL REVIEW PENDING` and pins the
Fable5 *prompt*, which was accurate at freeze time.  That is custody
timestamping, not a mathematical defect of the compiler.  Item 9 type-
checks the cutoff against the now-existing Fable5 PASS.

---

## Item 2 — Complete polygon census from the D3 source

**Verdict: CONFIRMED.**

Chart maps in the frozen D3 source, verified slot-by-slot against every
`chart_image` and `weight`:

```text
x^i y^j |-> t^(8+3i-j) X^i    for F,
x^i y^j |-> t^(12+3i-j) X^i   for G.
```

The `2S/3S` lattice used by D3, enumerated here with no `n<=22` cutoff,
is

```text
F:  0 <= i <= 16,  max(0, 4i-8)  <= j <= 3i+8,   weight = 8+3i-j,
G:  0 <= i <= 24,  max(0, 4i-12) <= j <= 3i+12,  weight = 12+3i-j.
```

This lattice equals the 442 named D3 alphabet rows, with no extra and no
missing tuple.  Compact SHA-256 of the sorted enumerations:

```text
0bcef3b5f9ae63d9145cc8ced06a7df680a1347db91d37d8ee01c0018d9bae1f  F
5a4114c9d1b6422b5a02b5c800af770a9c30958d3465da272715c1e63f44b1ff  G
```

Census, recovered from D3 exponents rather than from stored counts:

| source | lattice rows | weight 0 | positive slots | weights present | max positive weight |
|---|---:|---:|---:|---|---:|
| `F` | 141 | 17 | 124 | `0..14` | 14 |
| `G` | 301 | 25 | 276 | `0..21` | 21 |
| total | 442 | 42 | 400 | — | — |

No lattice point has negative weight or weight `>22`.  In particular
there is no `F` row of weight 15 and no `G` row of weight 22.  The field
name `raw_slots_through_weight_22` is therefore a complete polygon dump,
not a truncated window: the bound 22 does not omit any `2S/3S` slot.
Maximum pair-sum is `14+21=35`.  No source-supported determinant row
above 35 exists, because it would require an `F` weight `>14` or a `G`
weight `>21`.

Weight-zero raw rows are not variables in `C`.  They are replaced by the
fixed leading polynomials `F0=H^2=(X^8-1)^2` and `G0=H^3=(X^8-1)^3`,
independently expanded as

```text
F0 = 1 - 2 X^8 + X^16,
G0 = -1 + 3 X^8 - 3 X^16 + X^24.
```

The 400 positive slots are uniquely named, with empty `F∩G`, and enter
`C` as free generators of coefficient 1.  D3 also stores a specialized
`literal_artificial_raw_face` (42 nonzero face slots, 34 of them with
coefficient other than `1`).  The compiler never reads that face, nor
any alias map (D3 has none), nor any source equation.  A sample
face-specialized slot `f_6_16` with coefficient `1001` remains a free
name in the determinant.

---

## Item 3 — Recurrence, including signs

**Verdict: CONFIRMED.**

Chart: `x=t^3 X`, `y=t^{-1}`, `F=t^8 f`, `G=t^{12} g`.  The coordinate
Jacobian is

```text
det d(x,y)/d(X,t) = | t^3    3 t^2 X |  = -t.
                    | 0     -t^{-2}  |
```

Direct differentiation gives

```text
f_X = t^{-8} F_X,
f_t = -8 t^{-9} F + t^{-8} F_t,
g_X = t^{-12} G_X,
g_t = -12 t^{-13} G + t^{-12} G_t,
```

hence

```text
det d(f,g)/d(X,t)
  = t^{-21}(-12 F_X G + 8 F G_X + t F_X G_t - t F_t G_X).
```

Dividing by the coordinate Jacobian `-t` produces

```text
J_(x,y)(f,g) = t^{-22} E,
E = 12 F_X G - 8 F G_X - t(F_X G_t - F_t G_X).
```

Write `F=sum_i F_i t^i` and `G=sum_j G_j t^j`.  The coefficient of
`t^n` in each summand is

```text
12 F_X G     ->  12 sum_{i+j=n} F_i' G_j,
-8 F G_X     ->  -8 sum_{i+j=n} F_i G_j',
-t F_X G_t   ->  -sum_{i+j=n} j F_i' G_j,
+t F_t G_X   ->  +sum_{i+j=n} i F_i G_j'.
```

The last line is the source of the `+i` term: it comes from `+t F_t G_X`,
not from a minus.  Collecting,

```text
D_n = sum_{i+j=n} ((12-j) F_i' G_j + (i-8) F_i G_j').
```

Both displayed integers and both signs are therefore correct.  Vanishing
prefactors `j=12` or `i=8`, and vanishing `X`-derivatives of `X`-degree
0, omit contributions because the coefficient is identically zero (3937
such structural zeros through `D35`), not because a nonzero term was
dropped.

---

## Item 4 — `D0..D22` byte identity and unchanged D22 certificate

**Verdict: CONFIRMED.**

Frozen D5G has 23 row objects `D0,...,D22`.  For each `n=0,...,22` the
complete JSON row object in D5G35 — `weight`, `term_count`, `terms`,
`contribution_count`, `contribution_sha256`, `contributions` — is
object-equal to D5G, and the compact encodings are byte-identical.  In
particular the contribution lists and per-row digests match, not merely
the final polynomials.  The wrapper files are *not* byte-identical
(different schema, extra rows `D23..D35`); the charged claim is the row
records, and that claim is exact.

`direct["D"][22]["terms"]` equals `D22_CERTIFICATE.json["D22"]` (778
terms).  The certificate file hash is unchanged from the D5G freeze:
`6346ab6afb307fea83516f742ca53b90e5eb8d42c2e1d5bef083920de23e434a`.
D5G35 does not rewrite the certificate; it asserts term equality against
the frozen predecessor.

`D0` is empty after cancellation, not omitted.  It serializes 17
nonzero leading-row contributions from `F0=H^2` and `G0=H^3`, which
recombine to the identity `24 H^4 H' - 24 H^4 H' = 0`.

---

## Item 5 — All rows through the true ceiling

**Verdict: CONFIRMED.**  Counts below are lengths of the stored lists,
independently recomputed, not trusted `term_count` fields.  Every row's
contribution list recombines to its stored final polynomial.

| row | final terms | contributions | independent four-product match |
|---|---:|---:|---|
| `D23` | 626 | 1,106 | exact, including term/contribution bytes |
| `D24` | 494 | 896 | exact |
| `D0..D35` total | 34,528 | 63,012 | exact |
| `D0` | 0 | 17 | cancel to 0 |
| `D34` | 4 | 8 | exact |
| `D35` | 0 | 2 | cancel to 0 |

All 36 weights `0..35` are present.  There is no `D36` row.  Stored
`term_count`/`contribution_count` equal the list lengths at every
weight.  Terms are sorted by `(raw monomial, X degree)` with sorted
names; contributions are Python-list sorted.  No zero-coefficient final
term is stored.

Independent four-product terms equal stored `terms` for every `n`.
Independent recurrence contributions equal stored `contributions` for
every `n`, and their compact digests match `contribution_sha256`.  The
digest of the 36 contribution digests is

```text
39a1676da232e717becf51f128c7e7d29ef56007a551a65101ae6bbfef824bfc.
```

`D23` support in `X` is degrees `1..16` (no constant term).  `D24`
support is degrees `1..15` (no constant term).  Pair weights for `D23`
are exactly `(i,j)=(2,21),...,(14,9)` and for `D24` exactly
`(3,21),...,(14,10)`: `G` cannot supply `j=22` or `j=23`, so the
off-by-one at the top of `G` is correct.

Representative new-row identities, reconstructed from source exponents
and the recurrence, not from stored counters:

```text
f_0_1 = y  (weight 7, X^0),   g_2_2 = x^2 y^2  (weight 16, X^2),
D23 first term: (7-8)*2 f_0_1 g_2_2 X = -2 f_0_1 g_2_2 X.

f_9_33 (weight 2, X^9),  g_3_0 = x^3 (weight 21, X^3),
D23 last term: (12-21)*9 + (2-8)*3 = -99, at X^11.

f_0_1 and g_2_1 (weight 17, X^2) give D24 first term -2 f_0_1 g_2_1 X.
f_9_32 (weight 3, X^9) and g_3_0 give D24 last term
  (12-21)*9 + (3-8)*3 = -96 at X^11.
```

All four match the stored first/last terms of `D23` and `D24`.  The
first `D23` contribution `[23,2,21,"FX_G","f_10_36","g_3_0",12,"-90"]`
is the single factor `(12-21)*10=-90` at `X^{12}`; it is a genuine
pre-cancellation summand, not a final term.

Row-census SHA-256 values in `RESULT.json` equal independent hashes of
the stored `terms` and `contributions` at every weight, including

```text
D23 terms        7b5ad4a59cdfb700135ceee56c2b7a0d1009f2fc5c1c1132371923781e916b61
D24 terms        e0c13f3d358c6ebb12dc8c4be69b073aa0291d7c8c9c67d7ceda07704816c1c8
empty-terms      37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
```

(the last is `D0` and `D35`).

---

## Item 6 — `D34` four terms, `D35` cancellation, true ceiling

**Verdict: CONFIRMED.**  `D34`, not `D35`, is the true highest
potentially nonzero row.

The only weight splits at 34 are `(13,21)` and `(14,20)`.  The only
slots are

```text
F14 = f_2_0 X^2,
F13 = f_2_1 X^2 + f_3_4 X^3,
G21 = g_3_0 X^3,
G20 = g_3_1 X^3 + g_4_4 X^4.
```

Pair `(13,21)`:

```text
(12-21) F' G + (13-8) F G'
  = -3 f_2_1 g_3_0 X^4 - 12 f_3_4 g_3_0 X^5,
```

from the eight-to-four recombination `(-18+15)` and `(-27+15)`.  Pair
`(14,20)`:

```text
(12-20) F' G + (14-8) F G'
  = 2 f_2_0 g_3_1 X^4 + 8 f_2_0 g_4_4 X^5,
```

from `(-16+18)` and `(-16+24)`.  Total:

```text
D34 = (2 f_2_0 g_3_1 - 3 f_2_1 g_3_0) X^4
    + (8 f_2_0 g_4_4 - 12 f_3_4 g_3_0) X^5.
```

These are four distinct monomials in `C[X]`.  They do not cancel.  Two
independent nonzero specializations of the 400 slots both give nonzero
numeric `D34` (producer assignment: `16 X^4 - 620 X^5`; SHA-alternate:
`236 X^4 + 4176 X^5`).  `D34` is genuinely nonzero as a generic
polynomial.

The only split at 35 is `(14,21)`:

```text
(12-21) (2 f_2_0 X) (g_3_0 X^3) + (14-8) (f_2_0 X^2) (3 g_3_0 X^2)
  = -18 f_2_0 g_3_0 X^4 + 18 f_2_0 g_3_0 X^4
  = 0.
```

The `D35` record retains both opposite contributions and stores no final
term.  All rows above 35 vanish by support.  After the displayed
cancellation, all rows above 34 vanish.

---

## Item 7 — Exact target gate, unsolved

**Verdict: CONFIRMED.**  The gate was not solved, and no existence or
emptiness is inferred.

Independent rebuild of the coefficient equations, one generator per
`(weight, X-degree)` whose remaining polynomial in `C` is nonzero after
imposing the numeric target, is byte-identical to `TARGET_GATE.json`:

```text
target string:   D0=...=D21=0, D22=1, D23=...=D35=0
generators:      734
status:          UNSOLVED-EXACT-GATE; NO SPECIALIZATION CLAIM
D0 generators:   0   (already 0)
D1..D34:         all strictly positive generator counts
D35 generators:  0   (already 0; redundant checked row)
D22 X^0 target:  1
D34 generators:  X^4: 2 f_2_0 g_3_1 - 3 f_2_1 g_3_0 = 0
                 X^5: 8 f_2_0 g_4_4 - 12 f_3_4 g_3_0 = 0
```

Mathematically the live equations are
`D0=...=D21=0, D22=1, D23=...=D34=0`.  `D35=0` is a checked redundant
structural row and does not change the generator count.  The 734 figure
counts coefficient-of-`X^k` equations, not raw monomials: `D23` alone
contributes 16 generators packing all 626 terms.

`D22=1` subtracts `1` from the constant coefficient in `C`, producing a
three-term generator whose `()` monomial is `-1`.  The two stored `D22`
`X^0` terms have no empty monomial, so this subtraction is a genuine
normalization to target `1`, not a no-op.

The compiler contains no Groebner basis, no SAT call, and no
satisfiability verdict other than the frozen `UNSOLVED` tag.

---

## Item 8 — Independent dense `Q[X,t]/(t^36)` control and mutations

**Verdict: CONFIRMED.**  Lightweight exact arithmetic; no heavy local
algebra was required.

The dense engine used here does not call the sparse recurrence.  It
builds `F,G` as 36-term series in `Q[X]`, forms the four products
`F_X G`, `F G_X`, `F_X G_t`, `F_t G_X`, and compares with the sparse
artifact specialized at the same point.

Producer assignment: slot `k` in the sorted 400-name list gets
`((k mod 17)+1) * (+/-1)`.  Independent dense series equals the
specialized sparse polynomial at every weight `0..35`, with

```text
assignment_sha256           38b1b380ba247636891fccba92859a16cf4549eb29ba4a6f040657604b387d69
E0_through_E35_sha256       6f164fca16821a3441e46713a7b90489145eeb9d39537e1a66c63e2dfa23df82
D23_numeric_sha256          e24ebacdd1e9bd1645cef7eee77eae95dda2df4f2d57d40c42c1e388480c613f
D24_numeric_sha256          ec3c229d89491d202a15a48b3345f1c7e5115918329f33303cb3989cf241a115
nonzero_weight_count        34
```

Numeric `D0=D35=0` and `D1..D34` all nonzero, matching the structural
ceiling.  Numeric `D23` and `D24` have vanishing constant coefficients,
as in the sparse support.

A second assignment, `1+(sha256(name) mod 23)` with independent signs,
again matches dense against sparse, again kills only `D0` and `D35`, and
again leaves `D34` nonzero.  That assignment is not in the producer
file; agreement is therefore not a replay of a stored digest.

Mutations `D23 -> D23+1` and `D24 -> D24+1` add `1` to the constant
`X^0` coefficient of the named row.  In the dense series they change
exactly that one coefficient (`orig 0 -> 1`) and alter the full-series
digests to

```text
D23+1  99f4807163b6073d89e19a20fdaf64e5df2481d918fd47b4589e11802c9a328b
D24+1  f6911e9ef0aa3c126d91288c6ca9d4c007b2b08d9b1d1445086e78584863f992
```

In the sparse gate they produce the constant generator `1=0`, SHA-256
`49e1d506dc64fc56fd8259c7bc14618ece27a4c5a7262b18de5d017645901501`,
which is unsatisfiable.  The producer `gate_verdict: REJECTED` is
hard-coded, but the mutated generator is independently `1=0`, so the
verdict is correct for this mutation.

Clarified strength, not a defect: because generic `D23` and `D24` have
no `X^0` terms, `D23+1=0` and `D24+1=0` fail at the constant term alone.
These mutations therefore certify that the mutated *targets*
`E=t^{22}+t^{23}+O(t^{24})` and `E=t^{22}+t^{24}+O(t^{25})` are
impossible on this alphabet.  They do not, by themselves, audit the 626
and 494 nonzero terms; those were audited by the four-product engine and
by both dense specializations.  The mutations also do not assert that
the resulting `q`-form is non-exact.  That is the correct R7R1 reading:
they revoke the *license*, they do not compute a residue.

The producer `--check` replay prints `PASS`.  That replay regenerates
the artifacts from the same functions that wrote them, so it is
self-consistency of the freeze, not an independent proof.  The
independent engines above are the proof.

---

## Item 9 — Conditional R7R1 cutoff interface

**Verdict: CONFIRMED.**  Typed against the Fable5-passed cutoff rule,
not promoted as a D5G35 theorem.

Corrected R7R1 states: for `N>22`, `E=t^{22}+O(t^N)` licenses exactly
those `q_n dX` that are exact in `L` for `n+22<N`, and conversely.
Hence

| exact target rows | congruence | licensed in `L` |
|---|---|---|
| through `D22` | `E=t^{22}+O(t^{23})` | `q0` only |
| plus `D23=0` | `E=t^{22}+O(t^{24})` | `q0,q1` |
| plus `D24=0` | `E=t^{22}+O(t^{25})` | `q0,q1,q2` |

with

```text
q0 = p^2,
q1 = F1/(4 p^5),
q2 = F2/(4H) - F1^2/(16 H^3).
```

The producer table matches this rule, including the formulas.  `D23+1`
removes the `n+22<24` hypothesis, so it revokes the `q1` license;
`D24+1` revokes the `q2` license.  Neither mutation is a computation of
non-exactness of the form.

If the entire frozen gate were later solved, support plus the `D35`
cancellation would give the polynomial identity `E=t^{22}`.  R7R1 then
licenses every `q_n dX` exact in `L`, but does **not** truncate the
transformed series `Q=P^2`, and proves no finite decision procedure and
no finite recurrence certificate for the de Rham tower.  The producer
firewall on that point is correct, and is the same repair Fable5
confirmed in R7R1 Item 7.

Wording note, not a correction: `RESULT.json`'s `q2` blurb says
"rationally exact only after the D24 gate".  The typed license is
exactness *in `L`*.  Rational exactness over `K(X)` is a separate
necessary base-field condition once rows through 24 are licensed
(R7R1 (0.4) plus trace descent), not a theorem of this compiler.  The
producer report table is the load-bearing statement and is correctly
typed.

The frozen `dependency_status` still says the different-model R7R1
review is pending.  That review now exists and PASSes.  The cutoff
interface of D5G35 is correctly typed against it and remains conditional
on R7R1: this case does not re-prove the tower.

---

## Item 10 — Artificial-fixture scope

**Verdict: CONFIRMED.**

Work is exactly `H=X^8-1` with the frozen D3 raw alphabet and the
normalization `F0=H^2`, `G0=H^3`.  Positive slots are free.  The D3
artificial face, factor packets, local carrier fixture, quarantined
reducer, and `M`-cokernel data are not consumed.  No source equation,
specialization, Keller landing, `8_28` face or family exclusion,
`G2-PSC`, `G2-BD`, counterexample, or JC2 theorem is proved, and none is
claimed.

---

## Attacks checked and not found

| Attack | Result |
|---|---|
| Serialization order of terms/contributions | Sorted; independent rebuild matches bytes |
| Omitted zero rows | All 36 weights present; `D0` and `D35` kept with cancelling contributions |
| Off-by-one at pair-sum 35 / missing `D34` | `D34` live, `D35` cancelled, no `D36` |
| Use of face coefficients or aliases | Alphabet only; no alias key in D3; face unread |
| Tautological verifier as sole proof | Rejected as proof; independent four-product and dense engines used |
| Mutation that does not change `E` | Dense series differs in exactly the named constant; sparse gate becomes `1=0` |
| Scope inflation to a solved gate or a finite tower | Absent from the frozen claims |
| Stored hash / PASS banner as mathematics | Hashes used only as custody |

No counterexample was found.  No correction of the charged mathematics
is required.

---

## Files read

- `xmodel/ggv-8_28-raw-global-determinant-d5g35-sol2-20260827.md`
- `xmodel/ggv-8_28-raw-global-determinant-d5g35-hostile-review-grok-prompt-20260827.md`
- `cases/ggv_8_28_raw_global_determinant_d5g35_20260827/` (all eight frozen files)
- `cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json`
- `cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/compile_d3.py` (polygon bounds only)
- `cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/README.md`
- `cases/ggv_8_28_raw_global_determinant_d5g_20260827/{FREEZE.sha256,DIRECT_DETERMINANT.json,D22_CERTIFICATE.json,compile_d5g.py}`
- `xmodel/ggv-8_28-raw-global-determinant-d5g-sol-20260827.md` (custody)
- `xmodel/ggv-8_28-raw-global-determinant-d5g-hostile-audit-sol-ultra-20260827.md` (custody/scope only)
- `xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md` (cutoff typing)
- `xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-hostile-review-fable5-20260827.md` (cutoff typing)

Not read: `jc2-lean`, canonical ledgers, unrelated cases.

---

## Scope of this review

This review confirms a complete literal raw determinant compiler on the
frozen D3 alphabet, a frozen but unsolved coefficient gate, and a
conditional R7R1 cutoff interface.  It does not solve the gate, does not
prove or disprove existence of a raw lift, and does not prove a source
equation, specialization, Keller landing, finite de Rham tower,
`8_28` face or family exclusion, `G2-PSC`, `G2-BD`, counterexample, or
JC2 theorem.

CONFIRMED
