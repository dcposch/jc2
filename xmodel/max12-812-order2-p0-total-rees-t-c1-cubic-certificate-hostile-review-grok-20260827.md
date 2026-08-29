# Hostile review: ordered `T-c1` cubic exceptional-power certificate

**Identity (C1): CONFIRMED**

**Chart type (`c1^3`, `s=1`, `W=0`, ordered `J1` stratum): CONFIRMED**

**Fable5 residual retired: CONFIRMED**

**Whole ordered registered `T-c1` stratum empty (`W=0`): CONFIRMED**

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-p0-total-rees-t-c1-cubic-certificate-producer-sol-20260827.md` |
| Charged claim | Exact identity (C1) is a staged `(*_s)` certificate with exceptional power `c1^3`, genuine localizer `1`, `W=0`, ordered equations `rs,c0`, source rows `Tg10_2,Tg10_4`; kernel-as-saturation absorbs `c1^3` without inverting `c1`; this empties the ordered registered `T-c1` stratum of the total family, not merely the `rho=0` fibre, and retires the Fable5 residual |
| Producer status | `EXACT HAND CANDIDATE`. SHA-256 `95117024a7f52dc5faaa968699bff7ff27d92c2f4ee7030c95f58d2ed02da69b` |
| Reviewer / model | Grok 4.6 (xAI). Hostile different-model reread. Producer expansion, Fable5 row-display, and AWS stdout were not trusted |
| Method | Independent SHA-256 of the frozen exact-Q and F65521 V9 row-2/row-4 files and the complete compiler/source pin chain; sparse monomial parse of the raw `.poly` bytes; exact `Fraction` expansion of (C1) over `Q`; coefficientwise reduction of every named rational and of the identity modulo `65521`. No Groebner basis, no emitter re-evaluation, no AWS mutation, no `jc2-lean`, no web |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-27 |

The displayed combination is an identity of the frozen polynomials, every coefficient and sign. On the honest fourth `J1` chart stratum it is a genuine `(*_s)` certificate of the reviewed staged form with `W=0`. Exceptional-power saturation kills `c1^3` without a residual `V(c1)`. The Fable5 leftover from consuming `Tg10_2` alone is exactly the `4 rho^2 a1 c1^2` term cancelled by `Tg10_4`. Nothing larger is accepted.

---

## Narrow reusable theorem

Work in the ordinary polynomial ring over `Q` on the frozen V9 names
`{a0,a1,c0,c1,cs,k,rho,rs}`. Let `Tg10_2` and `Tg10_4` be the frozen
exact-Q grade-10 rows (byte contents below). Then:

1. The polynomial identity

   ```text
   c1^3
     = (32/3) c1 * Tg10_2 - (128/3) a1 * Tg10_4
       - rs * ((5/2) rho^2 cs^2 k c1 + (5/96) rs^2 k c1)
       - c0 * (4 a0 c1 - 4 a1 c0)
   ```

   holds identically over `Q`. Equivalently, clearing the universal
   denominator `96`,

   ```text
   96 c1^3
     = 1024 c1 * Tg10_2 - 4096 a1 * Tg10_4
       - rs * (240 rho^2 cs^2 k c1 + 5 rs^2 k c1)
       - 384 c0 * (a0 c1 - a1 c0)
   ```

   holds over `Z` in these names, hence `c1^3` lies in
   `(Tg10_2, Tg10_4, rs, c0)` as a `Q`-ideal membership. The same
   identity reduces coefficientwise modulo `65521`.

2. This is an instance of the reviewed staged form `(*_s)` on the
   standard Rees chart `D_+(c1)` of `J1=(rs,cs,c0,c1)`, with

   ```text
   f_i = c1,   N = 3,   s = 1,   W = 0,
   q_m = {Tg10_2, Tg10_4},
   z_e = {rs, c0}   (base-function reading; H_j = 0),
   E = {rs, c0} ⊂ {rs, cs, c0}.
   ```

   The factor `c1^3` is an exceptional power. It is absorbed by the
   exact presentation `C = A[y] / ((c1 y_j - f_j) : c1^∞)`. The
   coordinate `c1` is never inverted and is never a unit of `C`.
   Genuine localizer `s=1` costs no residual closed stratum. Because
   `W=0`, `c1` is nilpotent on `V(rs,c0)` in the source, so
   `A_{c1}=0` and `C=0` on that locus: the chart stratum is the zero
   ring, not merely rho-empty.

3. The honest ordered fourth `J1` stratum is
   `V(rs,cs,c0) ∩ D_+(c1)` (obligation-table naming; least-index
   complement of `D_+(rs)`, then `D_+(cs)`, then `D_+(c0)`). Both
   the ratio reading `qrs=qcs=qc0=0` and the base-function reading
   `rs=cs=c0=0` are licensed by the covering analysis. Unused `cs`
   is a subset `E`, not a missing equation: emptiness of the larger
   locus `V(rs,c0) ∩ D_+(c1)` implies emptiness of the ordered
   stratum. The Fable5 residual

   ```text
   V(c1) ∩ (ordered T-c1 stratum) ∩ V(rho)
   ```

   is empty, because `c1 T` is nilpotent on the stratum and therefore
   lies in every homogeneous prime.

This closes only the ordered registered stage-one `T-c1` stratum of
the hash-pinned actual-total family. It does not close the unordered
full `D_+(c1)` chart.

---

## Verdicts

| Claim | Verdict | Reason |
|---|---|---|
| Identity (C1), every `Q` coefficient and sign | **CONFIRMED** | Independent sparse expansion from frozen `.poly` bytes; remainder `0` |
| Coefficientwise F65521 reduction of both rows and of (C1) | **CONFIRMED** | Every denominator is a unit mod `65521`; reduced identity remainder `0` |
| `rs=cs=c0=0` is the honest ordered fourth `J1` stratum | **CONFIRMED** | Table order `rs,cs,c0,c1`; both `z`-readings licensed; `E` may be a subset |
| Unused `cs` equation harmless | **CONFIRMED** | `cs` appears in (C1) only inside the `rs` cofactor; extra strength, not a hole |
| `c1^3` is a legitimate exceptional power; `c1` is not a unit | **CONFIRMED** | Same saturation mechanism as the repaired `T-c0` identity `(1')` |
| Fable5 residual eliminated | **CONFIRMED** | `Tg10_4` cancels the exact leftover `4 rho^2 a1 c1^2` of the `Tg10_2`-only factorization |
| Whole ordered registered `T-c1` stratum empty for the total family (`W=0`) | **CONFIRMED** | Nilpotent exceptional coordinate ⇒ `D_+(c1)` of the stratum is empty, including `rho ≠ 0` |
| Source-provenance of the two frozen rows | **CHARGED** to Fable5 SHA `139ecb67…`, whose poly hashes and the full pin chain reconfirm here. Not re-extracted from the V0R1 emitter this session |

Failure modes examined and refused as defects: rational denominators `32/3`, `128/3`, `5/2`, `5/96` (units of `Q` and of `F_65521`); cofactor `a1` (a source coordinate of `A`, not inverted); absence of Rees bilinears from (C1) (`H_j=0` is legal in `(*_s)`); interface-theorem English that mentions only the `rho=0` fibre (the identity `(*_s)` with `W=0` is stronger, and the producer claims the stronger reading, which the nilpotent case of the chart presentation supplies).

---

## 1. Custody and SHA pins

Independently recomputed this session. Producer-quoted hashes of the two
exact-Q rows, the Fable5 review, and the F65521 control triple
`dc775709…` / `491dec9e…` / `75330c39…` all match the on-disk bytes.
Every V9 `FREEZE.sha256` line rehashes. Every literal compiler pin
along V9→V8→V7→V6→stream V2→V0R1→base/tails rehashes. V0R1's six
`EXPECTED` pins (tails, base, owner, raw-v2, audit, gate) rehash.
Canonical `tails.json` is `6eed03d4…` with `569` entries, row 2 of
`54` and row 4 of `81`. `KeepT10_2.poly` is byte-identical to
`Tg10_2.poly`.

| Artifact | SHA-256 |
|---|---|
| cubic producer | `95117024a7f52dc5faaa968699bff7ff27d92c2f4ee7030c95f58d2ed02da69b` |
| Fable5 `T-c0`/`T-c1` review | `139ecb673995eff3c19f72da54b7a79d0a2a4c9c01f3b8600935f855704066fb` |
| staged-calculus promotion | `16ec6f54e80a420755a52b8d2068390b65344311a5f84c4d486192513a928867` |
| obligation table | `50db2706f5a8d435618e615bfc393d2eb7dd22828a9a3fa35ac8a2e685ab15c4` |
| `T-c0` promotion (residual filing only) | `cd6f34da8e1e3048cfe0914c12be4355a83a669be467d92fbe047362dc430a90` |
| original `T-c0`/`T-c1` producer | `6a29aac9506fba6ffd7f12a35efedb7501fb149d8f5d7c949740e8b1c2876da6` |
| Fable5 ideation review | `db160c13351bab3a238582601e9a4f444ff98319524722176afb4ef047c54b00` |
| V9 `compile_coeffexport_v9.py` | `b1fc724dbb1cf4883cb4d2fb163335dbd74313f98a1e9e60218862992d422be1` |
| V9 `validate_coeffexport_v9.py` | `b22743e58b85c66593ccb4e7f8070f46f81afe57f0b6758922a4925a3d236d35` |
| V9 `PREREGISTRATION.md` | `c0bdfe2f631c93c5a132846d81321b507571b419480bf7afd3ff5c9e60d5a5fb` |
| V9 `FREEZE.sha256` | `ee87f8b94eb0d3bd87d58f1c8fd1cf9993caa013b7bfea7a319f0c260a7c24d7` |
| V9 `run_aws.sh` | `8d32c15e3f6a59be993c9fd5a60688861a2948110f96ee6d8a4461ac97cf8e88` |
| V9 `launch_host.sh` | `828769387f6705a898cb8b8cab96e1c7775d910b89bfeef38b022ee6bc263240` |
| V8 compiler | `41484e92ac2c3433562b8f120c922cb8d2bff5bff736c4b5664989c692dc85fa` |
| V7 compiler | `c678d293c2c26462c3ca5cc3776644b181176a2cf657b0beb6b65754c7dcd2d0` |
| V6 compiler | `9937fcfc61dff1d39029e6653b2be73ab3f835c2bc8bc81405876e54ef10b6bf` |
| stream V2 compiler | `5b176dfd0747f3736bc4519077877f4d877b5b726b9701e1b9dcaf56e059a112` |
| V0R1 emitter | `3aa6bbbbe539607461c5f27b400aeedd335a4d18e01e40d730f5537da4f45938` |
| base `compile_square_load_ladder.py` | `77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc` |
| `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` |
| canonical tails | `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8` |
| V9 exact-Q `COEFFICIENTS.json` | `86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e` |
| V9 F65521 `COEFFICIENTS.json` | `dc7757090bac53482ff674794e4e45cf33ff052d10c34f4e29a1de4133befde4` |
| exact-Q `Tg10_2.poly` | `50c88196628dc04407c47c49059849f7f43265ade03afa13c9f27eecc1f928a6` |
| exact-Q `Tg10_4.poly` | `6c33503e153a1adda56810a62db220f74b1dfd8c71158d1f3794f128773c503d` |
| F65521 `Tg10_2.poly` | `491dec9edba67a4eff1f7006a8a0ac294532505dd2f861cb08fa99aa06d2d4f1` |
| F65521 `Tg10_4.poly` | `75330c3958ba8e0b223f0d6bf01c9f0cac29d77345ef4c89446f0b8eb7b9502c` |

Pin chain, each hop a source literal checked against the hashed file:

```text
V9 compile_coeffexport_v9.py
  V8_COMPILER_SHA256 -> V8 compiler
    V7_COMPILER_SHA256 -> V7 compiler
      V6_COMPILER_SHA256 -> V6 compiler
        STREAM_SHA256 -> stream V2 compiler
          OLD_SHA256 -> V0R1 emitter
            EXPECTED[BASE]  -> compile_square_load_ladder.py
            EXPECTED[TAILS] -> tails.json
            EXPECTED_CANONICAL_TAILS
            EXPECTED[OWNER], EXPECTED[RAW_V2], EXPECTED[AUDIT], EXPECTED[GATE]
```

V9 `COEFFICIENTS.json` pins both exact-Q row files at the hashes above.
F65521 `COEFFICIENTS.json` pins both reduced row files at the hashes
above. Manifest characteristics are `0` and `65521`.

Frozen exact-Q bytes, parsed here and not taken from the producer
display:

```text
Tg10_2 = 15/64*rho^2*cs^2*rs*k + 3/8*rho^2*a1*c1 + 5/1024*rs^3*k
       + 3/32*c1^2 + 3/8*a0*c0
Tg10_4 = 3/32*rho^2*c1^2 + 3/32*c0^2
```

Frozen F65521 bytes:

```text
Tg10_2 = 1024*rho^2*cs^2*rs*k - 24570*rho^2*a1*c1 - 21819*rs^3*k
       + 26618*c1^2 - 24570*a0*c0
Tg10_4 = 26618*rho^2*c1^2 + 26618*c0^2
```

Row provenance of these two files is charged to Fable5
`139ecb67…`, which already reimplemented the V0R1 actual-total
emitter and reproduced both rows. This session does not repeat that
extraction. The pin chain and the file hashes that Fable5 quoted are
intact, so the cubic combination may use the frozen polynomials as
source relations.

---

## 2. Independent expansion of (C1) over `Q`

Parser: signed Singular terms, fractions `a/b`, exponents `var^n`,
applied to the raw `.poly` bytes. No campaign module imported.

Multiply the frozen `Tg10_2` by `(32/3) c1`:

| `Tg10_2` term | coefficient product | contribution |
|---|---|---|
| `(3/32) c1^2` | `(32/3)*(3/32)=1` | `c1^3` |
| `(3/8) rho^2 a1 c1` | `(32/3)*(3/8)=4` | `4 rho^2 a1 c1^2` |
| `(15/64) rho^2 cs^2 rs k` | `(32/3)*(15/64)=5/2` | `(5/2) rho^2 cs^2 rs k c1` |
| `(5/1024) rs^3 k` | `(32/3)*(5/1024)=5/96` | `(5/96) rs^3 k c1` |
| `(3/8) a0 c0` | `(32/3)*(3/8)=4` | `4 a0 c0 c1` |

Multiply the frozen `Tg10_4` by `(128/3) a1`:

| `Tg10_4` term | coefficient product | contribution |
|---|---|---|
| `(3/32) rho^2 c1^2` | `(128/3)*(3/32)=4` | `4 rho^2 a1 c1^2` |
| `(3/32) c0^2` | `(128/3)*(3/32)=4` | `4 a1 c0^2` |

Difference:

```text
(32/3) c1 Tg10_2 - (128/3) a1 Tg10_4
  = c1^3
    + (5/2) rho^2 cs^2 rs k c1
    + (5/96) rs^3 k c1
    + 4 a0 c0 c1
    - 4 a1 c0^2.
```

The `4 rho^2 a1 c1^2` terms cancel. The displayed cofactors are
exactly the remaining four terms:

```text
rs * ((5/2) rho^2 cs^2 k c1 + (5/96) rs^2 k c1)
  = (5/2) rho^2 cs^2 rs k c1 + (5/96) rs^3 k c1,

c0 * (4 a0 c1 - 4 a1 c0)
  = 4 a0 c0 c1 - 4 a1 c0^2.
```

Subtracting them leaves `c1^3`. Remainder polynomial: `0` (zero
terms). The integer form with leading `96 c1^3` is likewise the
zero polynomial. Every producer-quoted coefficient and sign is
correct, including the relative minus on the `Tg10_4` summand and
the inner minus `4 a0 c1 - 4 a1 c0`.

On the ordered substitutions `rs=c0=0` (with or without `cs=0`)
this collapses to the two-row identity

```text
c1^3 = (32/3) c1 * ((3/8) rho^2 a1 c1 + (3/32) c1^2)
     - (128/3) a1 * ((3/32) rho^2 c1^2),
```

which is `c1^3 + 4 rho^2 a1 c1^2 - 4 rho^2 a1 c1^2`. That is the
mechanism: `Tg10_4` exists to cancel the rho-linear leftover of
`Tg10_2`, not to invert anything.

---

## 3. Reduction modulo `65521`

`65521` is prime and does not divide `2` or `3`, hence does not
divide any denominator of (C1) or of the two frozen rows
(`64, 8, 1024, 32, 3, 96`). Independently,

```text
15/64  ≡  1024
3/8    ≡  40951 ≡ -24570
5/1024 ≡  43702 ≡ -21819
3/32   ≡  26618
32/3   ≡  21851
128/3  ≡  21883
5/2    ≡  32763
5/96   ≡  29348
```

with `3^{-1} ≡ 43681`. The frozen F65521 `.poly` files are the
coefficientwise reductions of the exact-Q files (five terms and two
terms, monomial-for-monomial, not a sample). Expanding (C1) on those
reduced polynomials with the reduced structure constants yields
`c1^3` with remainder `0`. Encoding control only; the theorem is the
`Q` identity.

---

## 4. Chart typing against `(*_s)` and the ordered fourth stratum

The reviewed staged form (Fable5 ideation §6, promoted interface
theorem) is

```text
f_i^N * s * (1 + rho*W)
  = sum_j H_j (f_i y_j - f_j) + sum_m G_m q_m + sum_{j in E} L_j z_j.
```

Identity (C1) is that equation with `f_i=c1`, `N=3`, `s=1`, `W=0`,
`H_j=0`, `q_m` the two frozen rows, `z_j` the base functions `rs`
and `c0`, and `E={rs,c0}`. The three slots are stored separately
exactly as demanded:

- `c1^3` exceptional-chart power, absorbed freely by saturation;
- `s=1` genuine localizer, producing no residual `V(s)`;
- `z_e = rs, c0` ordered-stratum equations with source provenance
  (the two `q_m` are the hash-pinned total rows).

**`c1` is not a unit.** The original `T-c1` note inverted `c1` and
paid a residual. Fable5 §5/§6 exists to refuse that conflation. The
cubic producer does not repeat it. The mechanism is the same as the
repaired `T-c0` identity `(1')`: an exceptional power in the source
ideal becomes `1` in the saturation `(P : c1^∞)`. If the exceptional
coordinate is nilpotent in the source after the stratum equations,
the localization `A_{c1}` is the zero ring and the chart is empty.
That is the `(2a)` nilpotent case of the chart presentation, not a
new principle.

**`W=0` is stronger than a rho-unit.** The interface theorem's
English concludes emptiness of the `rho=0` fibre. The identity
itself, with `W=0` and `s=1`, puts `c1^3` in
`(Tg10_2, Tg10_4, rs, c0)` with no remaining `rho` factor, so `c1`
is nilpotent on `V(rs,c0)` in the total source. Then
`D_+(c1 T) ∩ V(rs,c0)` is empty in `Proj Rees_A(J1)` for the whole
family, including `rho ≠ 0`. The producer claims this stronger
reading. It is the correct reading of `(*_s)` at `W=0`, and it is
accepted. Finite-prefix stability is immediate: (C1) is a polynomial
identity, so it survives every later source equation.

**Ordered fourth stratum.** Obligation table §4 names
`V(rs,cs,c0) ∩ D_+(c1)` as the fourth `J1` special-fibre stratum,
after `D_+(rs)`, then `V(rs) ∩ D_+(cs)`, then `V(rs,cs) ∩ D_+(c0)`.
Covering analysis: a point of `Proj` has a least index `i` with
`f_i t` outside its prime; for `j<i` the ratio vanishes, and
`f_j = f_i y_j` makes the base-function stratum larger and still a
cover. Both readings are licensed. The producer uses the
base-function reading `rs=cs=c0=0` together with the `T-c1` Rees
bilinears in the chart presentation. The identity itself does not
need the bilinears (`H_j=0`) and does not need `cs`.

**Unused `cs` is harmless.** On `D_+(c1)`, `cs` occurs in (C1) only
as `rs * ((5/2) rho^2 cs^2 k c1 + …)`. After the `rs` cofactor is
spent, no `cs` remainder exists. Lemma `(*_s)` permits `E` to be a
proper subset of the earlier indices. Certifying against a smaller
honest stratum ideal is the direction the covering analysis calls
safe. Geometrically this empties the *larger* locus
`V(rs,c0) ∩ D_+(c1)`, which contains the ordered fourth stratum.
The producer does not claim, and this review does not infer, any
`T-cs` consequence of that extra strength.

**Ratio reading.** Substituting `rs=c1 qrs`, `cs=c1 qcs`,
`c0=c1 qc0` into (C1) preserves the identity. The ordered complement
`qrs=qcs=qc0=0` returns the same cube membership. No
ratio/base-function defect.

**Coverage of the residual point.** Fable5's residual was a point of
`D_+(c1)` over `V(J1)` with all three ratios zero: the origin of
the affine chart, equivalently `[0:0:0:1]` in the exceptional
`P^3`. DVR arcs with `J1 R' ≠ 0` and `ord(c1)` minimal-positive
among the four generators route there. The `Tg10_2`-only
factorization

```text
32 Tg10_2 ≡ 3 c1 (c1 + 4 rho^2 a1)   (mod (rs,cs,c0))
```

leaves `c1 + 4 rho^2 a1 = 0` after one saturation step, hence
`c1=0` on `rho=0`, and that point survives. After (C1), `c1^3=0`
already in the source on `V(rs,c0)`, so `c1 T` is nilpotent and
belongs to every homogeneous prime. The residual point is not a
point of `D_+(c1 T)`. No other chart is required to pick it up.

**What is not closed.** The unordered full chart `D_+(c1)` without
`rs=c0=0` is not emptied: if `rs` or `c0` is nonzero the cofactor
terms remain. The producer claims only the ordered stratum. That
scope is exact.

---

## 5. Smallest theorem and nonclaims

**Theorem.** Let `A` be the registered actual-total source quotient
(V9 exact-Q rows, later equations allowed). On the standard Rees
chart `D_+(c1)` of `J1=(rs,cs,c0,c1)`, after the ordered (or the
weaker `rs=c0=0`) stratum equations, identity (C1) puts `c1^3` in
the source ideal. Kernel-as-saturation therefore makes that chart
stratum the zero ring. In particular its `rho=0` fibre is empty,
and the Fable5 residual
`V(c1) ∩ (ordered T-c1 stratum) ∩ V(rho)` is empty. The same
membership holds after reduction modulo `65521`.

**Nonclaims.** This review does not infer, and the identity does not
supply:

- any `T-cs` certificate, residual, or emptiness;
- either second-stage `a0`/`a1` chart over `V(J1)`;
- the terminal receiver `V(J1+J2)`;
- Gate T as a base-change/special-fibre comparison;
- the unordered full `D_+(c1)` chart;
- source-localizer complements such as `k=0`;
- the generic deck/square bridge;
- order two, maximum twelve, or JC2.

The coefficient `k` occurs in the `rs` cofactor of (C1) and is not
inverted. No `D(k)` hypothesis is used.

This file is the only repository write.
