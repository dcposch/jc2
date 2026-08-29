# Independent J2 direct-certificate design after V22R1 promotion

Date: 2026-08-27

Reviewer/researcher: Grok 4.6, independent hostile algebra lane. Producer
prose, V23 `RESULT.json` summaries, and the simultaneous Fable5 design are
not evidence. Every polynomial claim below is from the literal V23R1
`.poly` bytes or from an exact `Q`-identity replayed against those bytes.

Repo: `/Users/dc/code/math/jc2`

Git HEAD at writing: `418e413593120d19e15e6546eb50c985f4b1f038`

Sole write: this file.

---

## Verdict

**T-a0: EXACT DIRECT CERTIFICATE, residual zero.**

On the specialized source chart `J1=0`, `a1=a0*qa1`, the identity

```text
(-1/16) a0^3 (1 + 3 qa1^2 rho^2)
  = Tg15_6
    - (3/8) cs1 ell1 Tg11_1
    + (1/2) cs2 rho^2 Tg11_1
    + (1/8) rs2 Tg11_2
    + (3/8) cs1 rho^2 Tg12_1
    + (1/8) rs1 Tg12_2
    + (1/4) cs1 Tg12_3
```

holds identically over `Q`. Equivalently

```text
a0^3 (1 + 3 qa1^2 rho^2)
  = -16 Tg15_6
    + 6 cs1 ell1 Tg11_1
    - 8 cs2 rho^2 Tg11_1
    - 2 rs2 Tg11_2
    - 6 cs1 rho^2 Tg12_1
    - 2 rs1 Tg12_2
    - 4 cs1 Tg12_3.
```

The left-hand side is an exceptional power `a0^3` times the rho-unit
`1 + rho W` with `W = 3 qa1^2 rho`. No cofactor inverts `rho`, `qa1`, a
jet, or `a0`. The coordinate `k` does not appear. Two independent sparse
`Fraction` expansions, one of them not importing the V23 parser, both
return remainder `0`.

This is ideal membership, not radical membership. It is a chart identity
on the full `(a0, qa1, rho, jets)` T-a0 source, not a named-point
evaluation.

**Ordered T-a1: same sparse combination kills row 6 and does not produce
a cubic. No desk certificate. Hash-ready AWS linear algebra specified.**

The identical cofactor shape on the ordered restriction `J1=0`, `a0=0`
gives residual `0` against `Tg15_6`, which has no pure `a1^3` term. The
ordered cubics live in rows 3, 5, 7 (87 / 115 / 124 terms, each carrying
`k`). Analogous grade-11 torsion gives `a1 e0` and `a1 rho^2 e1` but not
`a1 e1`. That is a typed obstruction to copying the T-a0 row-6 argument,
not an obstruction to membership of `a1^3` in the full ordered source
ideal.

---

## 1. Custody, promotion, and the V23 V1 control erratum

Observed locally this session.

V22R1 is **PROMOTED WITH EVIDENCE REPAIRS**. Used as source of the
grade-15 rows only, with the five repairs of the post-review erratum in
force: the Q and F65521 hosts are two custody executions of one exact-Q
reconstruction; failed V1 trees are unharvested; sensitivity is not a
full re-emission; modular term counts are Q-dictionary counts (untriggered
here); CS0/Z00 zeros at grade 15 are homogeneity, not discriminating
controls.

```text
V22R1 producer     199254792a117f4ab6ae02d02fd652a0227ada6576b5c1d1ed3310cd89c6d287
V22R1 Grok review  f49329ceeffe20cea673a927afae5b4b7bfeac56b8d2a17abaefc09603eda80b
V22R1 promotion    0add46ccdfe387efdf3c445327355741fe3b77cc1d85e4a087be900e5bad5357
V22R1 erratum      32fb057c3f82b305cb69a8430398fd593293fe3c05f2b8ef17eace4581dfe4ac
V22R1 Q RESULT     829239c93c9a8bcb34a0428391c378ddd662dbc70cfdd27a6b2cc3b6cdcf00b8
```

V23R1 is a **design census**, not a promotion. Its V1 failed closed because
the A00 control compared the whole `(a0,qa1,rho)` polynomial to a point
that also sets `qa1=0`. R1 pins the V1 parser/rewriter byte-for-byte and
repairs only that comparison. Directory `output/` is quarantined. Only
`output_r1/` is read.

```text
V23 V1 erratum     9c00c9df4dbb1526ad8fcae4460fc409304d5d5497192f0e3b5da8eb26bcf8a0
V23 V1 parser      14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501
V23 R1 wrapper     2273305ed0745add26a961eec50c927cca9865e21f1bf96df69a0b21a3208ea1
V23 FREEZE_R1      cf10b39bd96cfc30b6e61c0fe217e9f0414eda4fa32d43feaef3d6eff7476963
V23 R1 RESULT.json ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641
```

`FREEZE_R1.sha256` rehashes 5/5. The three input manifests pinned by
`RESULT.json` rehash:

```text
V9  COEFFICIENTS.json  86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e
V20 RESULT.json        b23ffacd1e4e26abccaeb94a5e83f301cd98a9918a3a84e207fc462a880fe68d
V22R1 Q RESULT.json    829239c93c9a8bcb34a0428391c378ddd662dbc70cfdd27a6b2cc3b6cdcf00b8
```

All 84 specialized `.poly` files rehash to the `output_sha256` fields of
`RESULT.json` (0 mismatches). The identity below does not use those JSON
fields as coefficients; it parses the bytes.

Load-bearing specialized files for the T-a0 identity:

```text
a0_chart/Tg11_1.poly  ddfff3153c882b43b560515883dd259cf1ee1bae5a3435e99ab7f78fd533ddf0
a0_chart/Tg11_2.poly  70cf6c47af9cf24c47dcd769e75aadf29be15016ce0ea47efd2ec943b42a9537
a0_chart/Tg12_1.poly  8c827abfc3db757158f2be2a8887ca696a33ae9f6696022c7bd965d710c7527e
a0_chart/Tg12_2.poly  b28d2deab2a2f469cdf3e0fa27b67f4729746b65089e003d367480e364f0345c
a0_chart/Tg12_3.poly  9106a96241bbd36253522f0703328cce63497874b077ca5aa9561b5686a2057d
a0_chart/Tg15_6.poly  c3bb2b113e1ce062eb6bc53036aac0d0775951a71bfb16195f0cfccdee06da36
```

This lane did not re-emit V9/V20/V22R1 rows from the 569-tail source. It
treats the specialized V23R1 bytes as the chart presentation of those
promoted exports after the named substitutions, with the three input
manifest pins above as the only provenance check performed here.

---

## 2. Byte-level chart facts, grades 10--15

Charts, as written by the frozen specializer:

- `T-a0`: kill `J1={rs,cs,c0,c1}`, replace `a1` by `a0*qa1`. Exceptional
  coordinate `a0` only.
- ordered `T-a1`: kill `J1 ∪ {a0}`. Exceptional coordinate `a1` only.

From the `.poly` bytes, not from census prose:

- Every grade-10 row on both charts is the two-byte file `0\n`
  (SHA-256 `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`).
  This is the reviewed J1-vanishing prefix, used as a negative control.
- Rows identically zero on both charts at grades 11--14: `Tg11_4`,
  `Tg11_6`, `Tg12_6`, `Tg13_6`.
- The only pure exceptional monomials (support inside `{a0,qa1,rho}`
  respectively `{a1,rho}`) occur at grade 15.

T-a0 pure exceptional vector, parsed from bytes:

```text
Tg15_3: (-1/16) a0^3 qa1^3
Tg15_4: (-3/16) a0^3 qa1^2
Tg15_5: (-3/16) a0^3 qa1  +  (-3/32) a0^3 qa1^3 rho^2
Tg15_6: (-1/16) a0^3      +  (-3/16) a0^3 qa1^2 rho^2
Tg15_7: (-3/32) a0^3 qa1 rho^2  +  (-3/128) a0^3 qa1^3 rho^4
```

Setting `qa1=0` retains only `Tg15_6 = (-1/16) a0^3`, which is the V21/V22R1
A00 control. The other four rows' extra `qa1` powers are exactly what V1
mislabeled as an A00 failure. They are chart content, not a defect.

Ordered T-a1 pure exceptional vector, parsed from bytes:

```text
Tg15_3: (-1/16) a1^3
Tg15_5: (-3/32) a1^3 rho^2
Tg15_7: (-3/128) a1^3 rho^4
```

These are the V21/V22R1 A10 controls. Row 6 on this restriction has 12
terms and **no** pure `a1` monomial.

`k` first appears at grade 13. It is absent from every grade-11 and
grade-12 row, from `Tg13_4`, `Tg14_6`, and from T-a0 `Tg15_6`. It is
present in ordered `Tg15_3,5,7`.

Term counts that matter for the next computation, from bytes:

```text
              T-a0                 ordered T-a1
         terms  a0-deg  k?      terms  a1-deg  k?
Tg11_1      2      1            1      1
Tg11_2      2      1            1      1
Tg12_1      4      1            3      1
Tg12_2      6      1            5      1
Tg12_3      7      1            5      1
Tg12_4      2      0            2      0     (identical files)
Tg14_6      4      1            2      1
Tg15_3    103      3   k       87      3   k
Tg15_4     44      3   k       29      2   k
Tg15_5    146      3   k      115      3   k
Tg15_6     19      3           12      1      (k-free)
Tg15_7    161      3   k      124      3   k
```

`Tg12_4` is byte-identical on the two charts
(`58ab21164b626795549a138a6778b67b2d4d8e6fd4de1d52db851e80c63901a7`).

---

## 3. Grade-11/12 core, the unit `1 - qa1^2 rho^2`, and torsion

Literal T-a0 grade 11:

```text
Tg11_1 = (3/8) a0 (e1 + qa1 e0)
Tg11_2 = (3/8) a0 (e0 + qa1 rho^2 e1)
Tg11_3 = (1/2) rho^2 Tg11_1
Tg11_5 = -(1/8) rho^4 Tg11_1
Tg11_7 =  (1/16) rho^6 Tg11_1
Tg11_4 = Tg11_6 = 0
```

The last three identities are exact (remainder 0). Rows 3, 5, 7 are not
independent generators.

Write `L1 = e1 + qa1 e0`, `L2 = e0 + qa1 rho^2 e1`, and
`U = 1 - qa1^2 rho^2`. Then `U = 1 + rho W_U` with `W_U = -qa1^2 rho`, so
`U` is a permitted rho-unit polynomial. Cramer's rule over the polynomial
ring, with no inversion, is

```text
(8/3) Tg11_1 - qa1 (8/3) Tg11_2           = a0 U e1
(8/3) Tg11_2 - qa1 rho^2 (8/3) Tg11_1     = a0 U e0
```

Both remainders are 0. Thus `a0 U e0` and `a0 U e1` lie in the T-a0
source ideal. The same calculation gives the consistency relation
`a0 U (e0^2 + rho^2 e1^2) ∈ (Tg11_1, Tg11_2)`, hence
`a0 U Tg12_4` lies in that pair. `Tg12_4 = (3/32)(e0^2 + rho^2 e1^2)` is
already a source row, with no `a0` factor.

**The linear unit `U` is not required for the T-a0 cubic certificate
below.** It is recorded because the prompt asked, and because it is the
correct determinant of the `(e0,e1)` pair. On the locus `U=0` one has
`qa1^2 rho^2 = 1` (when `qa1 ≠ 0`), and the cubic unit becomes
`1 + 3 qa1^2 rho^2 = 4 ≠ 0`. Degeneracy of `(L1,L2)` therefore does not
kill the cubic factor. No `D(U)` / `V(U)` stratification is needed for
T-a0.

A second exact identity, remainder 0:

```text
Tg12_3 + (1/2) ell1 Tg11_1 - (1/2) rho^2 Tg12_1  = (3/16) e0 e1.
```

So the bilinear `e0 e1` is in the T-a0 source ideal, with no exceptional
factor. This is the step that finishes the row-6 cancellation.

`Tg14_6` is redundant given grade 11:

```text
Tg14_6 + (1/2) cs1 rho^2 Tg11_1 + (1/8) rs1 Tg11_2  = 0.
```

Ordered T-a1 grade 11, literal bytes:

```text
Tg11_1 = (3/8) a1 e0
Tg11_2 = (3/8) a1 e1 rho^2
Tg11_3 = (1/2) rho^2 Tg11_1
Tg11_5 = -(1/8) rho^4 Tg11_1
Tg11_7 =  (1/16) rho^6 Tg11_1
```

Torsion: `a1 e0 ∈ I` and `a1 rho^2 e1 ∈ I`. There is **no** polynomial
identity in these rows producing `a1 e1` without a positive even power of
`rho`. The factor `rho^2` is not of the form `1 + rho W`. Inverting it is
forbidden. The same `e0 e1` identity holds after the ordered substitution
(remainder 0), and `e0*(8/3)Tg11_1 + e1*(8/3)Tg11_2 = a1 (e0^2 + rho^2 e1^2)`
is exact. On the fibre `rho=0`, grade 11 therefore kills `e0` after
`a1`-saturation and does **not** kill `e1`.

That is the precise sense in which ordered-a1 torsion is analogous but
weaker. It is enough to cancel the k-free row 6. It is not, by itself,
enough to cancel a grade-15 cubic whose support includes `e1` without
`rho`.

---

## 4. T-a0 identity: cofactors, replay, typed reading

### 4.1 Cofactors

Work in the ordinary polynomial ring over `Q` on the V23R1 T-a0 names.
Let `I` be the ideal generated by the 42 specialized source rows at
grades 10--15. Grade 10 contributes `0`. The following is an identity in
that ring, hence a membership in `I`:

```text
(-1/16) a0^3 (1 + 3 qa1^2 rho^2)
  = 1  · Tg15_6
    + (-3/8 cs1 ell1 + 1/2 cs2 rho^2) · Tg11_1
    + (1/8 rs2) · Tg11_2
    + (3/8 cs1 rho^2) · Tg12_1
    + (1/8 rs1) · Tg12_2
    + (1/4 cs1) · Tg12_3.
```

Net cofactors, all polynomial, all sigma-homogeneous of complementary
weight:

```text
Tg11_1 :  (-3/8) cs1 ell1 + (1/2) cs2 rho^2     (weight 4)
Tg11_2 :  (1/8) rs2                              (weight 4)
Tg12_1 :  (3/8) cs1 rho^2                        (weight 3)
Tg12_2 :  (1/8) rs1                              (weight 3)
Tg12_3 :  (1/4) cs1                              (weight 3)
Tg15_6 :  1                                      (weight 0)
```

Derivation, for replay rather than as a second proof: the 17 nuisance
terms of `Tg15_6` cancel in five homogeneous steps against the grade-11/12
core, leaving

```text
(-1/16) a0^3 (1 + 3 qa1^2 rho^2)  +  (-3/64) cs1 e0 e1.
```

The displayed `e0 e1` identity then absorbs the last nuisance. No grade
13--14 row, and no `k`, enters.

### 4.2 Residual-zero replay

Two independent implementations, both exact `Fraction` arithmetic, both
restricted to integer constants, names, `+,-,*,/,^` with nonnegative
integral exponents:

1. the frozen V23 parser's `parse` / `multiply` / `add` on the six
   `.poly` files;
2. a second AST evaluator written for this session, not importing that
   module.

Both return remainder `0` against
`(-1/16) a0^3 + (-3/16) a0^3 qa1^2 rho^2`. Wall time `< 0.05 s`, RSS far
under 1 GiB. The integer form obtained by multiplying through by `-16`
has the same remainder `0` against `a0^3 + 3 a0^3 qa1^2 rho^2`.

A mutation control, not a third implementation: dropping the
`(1/4) cs1 Tg12_3` term leaves the nonzero residual `(-3/64) cs1 e0 e1`.
Dropping any other listed cofactor leaves a nonzero residual supported on
the corresponding cancelled nuisance.

Coefficientwise reduction modulo `65521` is licensed: every denominator
in the identity is a power of 2 times at most a factor `3` already
present as a numerator in the source rows, and `16` is a unit in
`F_65521`. This lane did not run Singular. Independent F65521 replay is
variant A of the AWS queue, as a custody control, not as a derivation.

### 4.3 Typed reading

In the staged form `(*_s)` used for the reviewed `T-c1` cubic and the
`T-cs` / `T-rs` rho-unit certificates:

```text
f_i = a0,   N = 3,   s = 1 + 3 qa1^2 rho^2,   W = 3 qa1^2 rho,
q_m = {Tg11_1, Tg11_2, Tg12_1, Tg12_2, Tg12_3, Tg15_6},
z_e = {rs, cs, c0, c1}   (already imposed by the chart substitution),
chart substitution a1 = a0 * qa1,
k is not a localizer and is not present.
```

- `a0^3` is an exceptional power. Kernel-as-saturation of the standard
  Rees chart `D_+(a0)` absorbs it. The coordinate `a0` is never inverted
  and is never a unit of the chart ring.
- `s = 1 + rho W` is a polynomial rho-unit. It is a genuine localizer of
  the permitted form. It is not a chart unit in `qa1`. The identity does
  not invert `s`.
- Because `W ≠ 0`, this is **not** a `T-c1`-style whole-stratum emptying
  with localizer `1`. After saturating by `a0`, one has
  `s ∈ (I : a0^∞)`. Localizing at `s`, or completing in `rho`, makes the
  chart the zero ring. The residual closed set `V(s)` inside the
  `a0`-saturated source is `1 + 3 qa1^2 rho^2 = 0`, which does not meet
  the fibre `rho = 0`. At `qa1 = 0` one has `s = 1` and recovers the A00
  value `a0^3/16 ∈ I`.
- Unwritten Rees bilinears are not used. Membership in the source ideal
  is membership in a smaller ideal, so it survives adding Rees equations.
- Point killing (A00) is the face `qa1 = jets = 0` of this identity, not
  a substitute for it.

**Not claimed:** `a0^3 ∈ I` with `W = 0`; emptiness of `T-a0` as an affine
scheme over `Q` without the rho-unit localizer; anything about ordered
`T-a1`; Gate T; order two; maximum twelve; JC2.

### 4.4 A W=0 attempt that fails at desk scale

The combination `Tg15_6 - rho^2 Tg15_4` has pure part `(-1/16) a0^3` and
51 nuisance terms, including five `k`-terms. Isolating `a0^3` with `W=0`
is a bounded cofactor search through the k-bearing grade-13/14/15 rows,
not a six-row identity. It is AWS variant C, not a counterexample to
§4.1.

No pure `a0^2` (or `a0^1`) exceptional term exists at grades 10--14. The
grade-13 row `Tg13_4` contains `a0^2 rs1` and `a0^2 cs1 qa1 rho^2`, both
tied to non-unit nuisances. There is no desk `a0^2` certificate.

---

## 5. Ordered T-a1: what the same argument does and does not give

The same six-row combination, after the ordered substitution, has
remainder `0` against ordered `Tg15_6`. That row has no cubic. The
identity is a consistency check that the T-a0 cancellation is compatible
with `a0=0`, not a certificate.

Ordered `Tg15_3` has 87 terms, a unique `a1^3` monomial `(-1/16) a1^3`,
three `a1^2` monomials

```text
(9/16) a1^2 cs1 ell2 + (9/16) a1^2 cs2 ell1 + (-9/16) a1^2 cs3 rho^2,
```

16 terms of `a1`-degree 1, and 67 terms of `a1`-degree 0, of which 43
carry `k`. Rows 5 and 7 are the same cubic multiplied by `(3/2) rho^2`
and `(3/8) rho^4` on the pure part, with still larger nuisance support
(115 and 124 terms).

The `a1^2` monomials are visibly in the span of `ell2·Tg13_1`,
`ell1·Tg14_1` / `Tg14_3`, and `rho^2·(grade-13/14 cs3-type rows)`, at the
cost of dumping the `k`-content of those rows into the residual. That is
the high-contact triangular pivot, now with live lower-contact jets. It
is the correct *shape* of an ordered-a1 identity and the wrong *size* for
a one-minute desk expansion.

Sparse-ansatz obstruction, strictly scoped: the k-free cofactor shape
that certifies T-a0 row 6, copied onto ordered rows 3/5/7, cannot cancel
the `k`-supported `a1`-free summands, because those summands are absent
from the k-free subideal generated by grades 11--12 together with
`Tg13_4`, `Tg14_4`, `Tg14_6`, and `Tg15_6`. This is not a proof that
`a1^3 ∉ I`. It is a proof that any ordered-a1 cubic identity must use
k-bearing rows or a genuine `k` localizer, and must be found by a
bounded homogeneous linear system rather than by the six-row hand
pattern.

---

## 6. Hash-ready AWS specification (ordered T-a1, plus two T-a0 controls)

Do **not** run an unstructured Groebner basis of the 42-row chart ideal.
The T-a0 identity shows the right computation is homogeneous cofactor
linear algebra at sigma-weight 15, with a finite monomial ansatz.

### 6.1 Common contracts, all variants

- Host: Box02 (`x2idn.32xlarge`, 128 vCPU / 2 TiB), or an r6i.16xlarge if
  Box02 is loaded. Wrap with `ops/aws_exact_lane.sh`. Linux + EC2 DMI
  fail-closed. No local Mac CAS.
- Characteristic-zero statement in an ordinary Singular ring `R = 0` or
  an exact-`Q` python-flint/Sage matrix; F65521 is a reduction control,
  not a derivation. Honour the V22R1 modular term-count erratum: if a
  modular lane reports term counts, they must be counts after
  coefficientwise reduction, not Q-dictionary counts.
- Inputs: the 84 V23R1 `output_r1` polynomials, pinned by the hashes in
  §1, plus the three upstream manifests. Freeze those files. Refuse
  overwrite. Do not read `output/`.
- Forbidden inside any identity: inversion of `rho`, `qa1`, any jet, or
  the exceptional coordinate; saturation encoded as a division; radical
  membership reported as ideal membership.
- Resource cap, every variant: 64 GiB RSS, 1800 s wall, 8 threads.
  Exceeding the cap is `RESOURCE_FAIL`, not a mathematical no.
- Negative control: all seven grade-10 rows remain the zero polynomial
  after loading. Positive control: the T-a0 identity of §4 reduces to 0
  in the same ring (variant A is exactly that control, run first).
- Scope string, compiled and printed:

  ```text
  SOURCE_IDEAL_MEMBERSHIP_ONLY_NO_REES_RADICAL_ARC_GATE_T_ORDER2_OR_JC2
  ```

### 6.2 Variant A — T-a0 identity replay (control, mandatory, tiny)

- Ring: `Q[a0,qa1,rho,e0,e1,ee0,ee1,aa0,aa1,cs1,cs2,ell1,rs1,rs2]`.
- Generators: the six rows of §4.1.
- Target: `a0^3 (1 + 3 qa1^2 rho^2)`.
- Engine: expand the displayed `Q`-combination; print `RESIDUAL_TERMS=0`
  or fail. Independently reduce coefficientwise mod 65521 and print the
  same. Mutation: omit `Tg12_3` cofactor, demand nonzero residual.
- Stop: `PASS_TA0_IDENTITY_REPLAY` iff both characteristics report
  remainder 0 and the mutation is nonzero. This variant does not search.

### 6.3 Variant B1 — ordered T-a1, target `a1^3`, weight 15, no extra localizer

- Ring names, the exact union of variables occurring in the 42 ordered
  files:

  ```text
  a1, rho,
  k, k1, k2c,
  aa0, aa1, aaa0, aaa1,
  e0, e1, ee0, ee1,
  ell1, ell2, ell3, ell4,
  cs1, cs2, cs3,
  rs1, rs2, rs3,
  ac3, ac4, az3, az4,
  ec3, ec4, ec5, ez3, ez4, ez5
  ```

  Sigma weights are those of the frozen V23 parser (`a1:5`, `rho:0`,
  `k:4`, `k1:5`, `k2c:6`, `aa*:6`, `e*:6`, `aaa*:7`, `ee*:7`, `ell n : n`,
  `cs n : 2+n`, `rs n : 2+n`, `ac/az/ec/ez n : 5+n`).
- Generators: all 42 ordered specialized rows. The zeros are loaded and
  must remain zero.
- Exact target: `a1^3`.
- Ansatz: for each generator of sigma-weight `g`, cofactors are
  `Q`-linear combinations of monomials of weight `15-g` in the ring
  names, even in `rho`, with `deg_rho ≤ 8` and total degree at most 8.
  No monomial may contain a negative exponent. This is a Macaulay matrix
  at weight 15, not `std`.
- Engine: exact rational row reduction (Singular `lift` / python-flint
  / Sage). Print cofactors on success, or the rank of the weight-15
  piece and a linear certificate that `a1^3` lies outside the column
  span.
- Stop:
  - `PASS_TA1_A1CUBED` if cofactors are printed and residual 0 over `Q`,
    with F65521 reduction also 0;
  - `GRADED_MISS_A1CUBED` if the matrix is fully reduced under the cap
    and `a1^3` is certified outside the span (this is a graded
    obstruction to `W=0`, `m=0` membership, not to chart emptiness);
  - `RESOURCE_FAIL` otherwise.
- A `GRADED_MISS` here is the trigger to B2, not a chart verdict.

### 6.4 Variant B2 — ordered T-a1, target `a1^3 (1 + rho W)` with `W` even of weight 0

Same ring, generators, cofactor degree bounds, and cap as B1.

- Exact target family: `a1^3 s`, where

  ```text
  s = 1 + w2 rho^2 + w4 rho^4 + w6 rho^6 + w8 rho^8,    w_i ∈ Q unknown.
  ```

  The unknowns `w_i` are additional columns. `s` is forced into the
  permitted shape `1 + rho W` with `W ∈ Q[rho^2] rho` of `deg_rho ≤ 7`.
  Do not invert `s`.
- Stop: `PASS_TA1_RHOUNIT` on residual 0 with printed cofactors and
  printed `w_i`; `GRADED_MISS_RHOUNIT` if the extended span still misses;
  else `RESOURCE_FAIL`.
- Control: the T-a0 unit `1 + 3 qa1^2 rho^2` is *not* in this family
  (`qa1` is absent on the ordered chart). Do not import it.

### 6.5 Variant B3 — genuine `k` localizer, only if B1 and B2 miss

Same ring and generators.

- Targets, separately: `a1^3 k` at weight 19, and `a1^3 k (1 + rho W)`
  with the same `W`-ansatz as B2. Cofactor weights shift by 4. Raise
  `deg_rho` still to 8, total degree to 10.
- `k` may be retained as a genuine localizer. It must not be inverted.
- Cap unchanged. If this also `GRADED_MISS`, the next enlargement is a
  *new* freeze (higher jet degree in cofactors, or `N=4` exceptional
  power), not a silent Groebner.

### 6.6 Variant C — T-a0 `W=0` hunt, concurrent with B

- Ring: T-a0 names appearing in grades 11--15, including `k,k1,k2c` and
  the `aaa, ac, az, ec, ez, ell, cs, rs` jets of those files.
- Generators: all 42 T-a0 rows.
- Target: `a0^3` (i.e. `W=0`).
- Ansatz: same complementary-weight Macaulay matrix as B1, now in the
  T-a0 names, `deg_rho ≤ 8`, total degree ≤ 8. Seed the system with the
  known §4 combination plus `-rho^2 Tg15_4` so the engine is asked only
  to cancel the 51 leftover nuisances of that difference.
- Stop: `PASS_TA0_W0` on residual 0; `GRADED_MISS_TA0_W0` if `a0^3` is
  outside the span (the §4 identity with `W ≠ 0` remains). Do not
  weaken §4 on a miss.

### 6.7 Ranking for concurrent Box02 launch

Launch order, all independent after variant A:

| rank | variant | why this rank | expected size |
|---|---|---|---|
| 0 | A | custody of the only existing identity; fail-closed gate for B/C | seconds, ≪1 GiB |
| 1 | B1 | strongest ordered-a1 statement (`W=0`, no `k`) | small dense matrix, well under the cap if the ansatz is as sparse as T-a0 |
| 2 | B2 | the typed rho-unit analogue of §4, no `k` | one extra 4-dimensional target family |
| 3 | C | strongest possible upgrade of T-a0; complementary to Fable5's likely grade-15 Groebner | seeded, 51-term residual |
| 4 | B3 | only if B1 and B2 miss; retains `k` explicitly | weight 19 |

A, B1, B2, and C may run concurrently on Box02. B3 waits on B1/B2. None
of these jobs is a Groebner basis of the full chart. None launches
itself; this document is the specification, not a freeze or a
`run_aws.sh`.

---

## 7. Complementary route, and what was refused

Fable5, by its prompt, is searching low-degree certificate shapes from
the grade-15 cubics, with first attention to the grade-11/12 core and
row 6, and with a Groebner-shaped AWS as one allowed outcome. This lane
did not read that design.

The complementary computation actually performed is: hand syzygies of the
grade-11 pair `(L1,L2)`, the bilinear `e0 e1` identity, and a five-step
cancellation of the 19-term row 6, across *all* grades 10--15 (zeros,
redundancies, and k-first-appearance included), followed by a
*structured* linear-algebra AWS rather than `std`. The T-a0 certificate
is the output of that cancellation. The ordered-a1 cubic is deliberately
left as a Macaulay matrix of complementary weight, not as an open
elimination.

Refused as methods this session: Groebner bases; saturation encoded as
division by `a0` or `a1`; inverting `rho` to pass from `a1 rho^2 e1` to
`a1 e1`; treating A00/A10 point values as chart emptiness; treating
`a0 U e0 ∈ I` as `e0 ∈ I`; treating `Tg15_6 - rho^2 Tg15_4` as a `W=0`
certificate; launching AWS; writing case inputs; touching `jc2-lean`.

---

## 8. Scope firewall

This document establishes one polynomial identity in the specialized
T-a0 source rows at grades 11, 12, and 15, and specifies a frozen AWS
search for the ordered T-a1 analogue.

It does **not**:

- promote V23, empty either J2 chart as a scheme without the stated
  localizer, or upgrade the T-a0 identity to `W=0`;
- prove radical membership, construct or exclude a formal arc, or write
  a Rees equation;
- invert `rho`, `qa1`, a jet, `a0`, or `a1` inside any identity;
- treat named-point killing (A00, A10, CS0, Z00) as chart emptiness;
- import the high-contact Cech identities `g15[6]=-a0^3/16` and
  `g15[3]=-a1^3/16` as substitutes for cancellation of live jets (those
  identities remain a face of the chart, recovered at `qa1=jets=0` and
  at A10, not a generalization);
- establish Gate T, order two, maximum twelve, or JC2;
- freeze, compile, or launch any AWS job.

Rollback of V22R1 would retract the grade-15 bytes and therefore the
T-a0 identity as a statement about the actual-total source. The six-row
algebraic combination would remain an identity of whatever polynomials
occupy those filenames.

Immediate successor queue, in order: (1) different-model residual-zero
review of §4 from the six hashes; (2) Box02 variant A then concurrent
B1/B2/C; (3) B3 only on graded miss; (4) only then a larger cofactor
degree freeze.
