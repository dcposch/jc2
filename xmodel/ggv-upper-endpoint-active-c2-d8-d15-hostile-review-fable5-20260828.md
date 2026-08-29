# Hostile review: deep active-`c2` D8--D15 repair/extension

Date: 2026-08-28
Reviewer lane: Fable 5 (different-model hostile review; fully independent
reconstruction)
Verdict: **REPAIR** — charged D8--D11 identities CONFIRMED; the charged
valuation claim at D11 is REFUTED exactly as the extension states, and I
sharpen it to a closed form; the exact `D=0` extension through D15, the
literal raw survivor, and the separate `c2=0` companion all PASS.

## 1. Scope and frozen inputs

Audited from the authoritative fractional-power recurrence, not from any
producer checker.  My checker

```text
xmodel/ggv-upper-endpoint-active-c2-d8-d15-hostile-review-fable5-20260828-check.py
```

is standard-library only, imports nothing from producer code, and
reimplements: sparse Laurent-in-`A` arithmetic, the characteristic
recurrence, exact univariate polynomial/rational replay, and the
determinant rows.  Frozen inputs (hash-verified at start and end of every
run):

| file | sha256 |
|---|---|
| `cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828/verify_q1_prefix_target.py` | `fceb189b…190fde119` |
| `xmodel/ggv-upper-endpoint-active-c2-d8-d11-prefix-sol-ultra-20260828.md` | `e3b777f8…21602b4d1f6` |
| `xmodel/ggv-upper-endpoint-active-c2-d8-d11-prefix-sol-ultra-20260828-check.py` | `00111fee…3b5ef7d97b44fcfa62f5b0372` |
| `xmodel/ggv-upper-endpoint-active-c2-d8-d13-independent-audit-extension-20260828.md` | `da189b7f…a1322d0c98d5577` |
| `cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/verify_active_c2_extension.py` | `112650dc…5f99d96de26` |
| its `README.md` | `c4c2263e…300318ea60d2e` |
| its `RESULT.json` | `568934ce…d90a2712c02e` |

(Full 64-hex digests are pinned inside the checker and in `SOURCE.sha256`;
all seven verified unchanged before and after this review.)

## 2. Independent reconstruction of the recurrence

I re-derived rather than copied the recurrence.  With
`F = sum_n F_n t^n`, `F_0 = A^4`, and `y = F^e`, t-differentiation of
`y = F^e` gives `F*ydot = e*Fdot*y`, whose `t^(n-1)` coefficient is

```text
n*A^4*Y_n = sum_{i=1..n} ((e+1)i - n) * F_i * Y_{n-i},   Y_0 = A^{4e}.
```

The characteristic solution is `G = F^(3/2) + sum_m c_m t^m F^((12-m)/8)`
over the ten even births `m = 2,...,20`; the derived exponent table equals
the frozen table (`5/4, 1, 3/4, 1/2, 1/4, 0, -1/4, -1/2, -3/4, -1`).  Two
structural facts I verified independently:

- **Determinant identity.**  For the row operator
  `D_n = sum_{i+j=n} (12-j)F_i'G_j + (i-8)F_iG_j'` one has, for
  `y = t^m F^e`, the closed form `D(F,y) = t^m F_X F^e ((12-m) - 8e)`.
  Hence rows vanish identically exactly at the registered exponents
  `(12-m)/8`.  My checker confirms this concretely: on a generic rational
  point (`A = X^4-2`, generic `v0,z,t,f4..f15`, **all ten modes nonzero**)
  every determinant row `D_0..D_15` vanishes as a rational function.  A
  mutated exponent (`c14 ↦ -1/2`) leaves rows 0--13 zero and makes row 14
  nonzero, as `(12-14)-8e = 2 ≠ 0` predicts.  So the reconstructed
  recurrence is the authoritative one, certified against the determinant
  rows themselves and not against any producer file.
- **Mode retention.**  Each `c_m` first appears exactly at row `m` and is
  never deleted; `c12` (exponent 0) appears exactly once, as the constant
  `c12` in row 12, since `F^0 = 1` truncates in the recurrence.  The
  subleading (regular and `A^-1`) classes at D13 retain `c2, c6, c8`
  alongside `e1, ell, f7, f8, p1, q, s`.

The reduced prefix `F0=A^4, F1=A^2V0, F2=(V0^2+A^2Z)/4, F3=(V0Z+AT)/8` is
taken as the reviewed dependency (q1-free D9 theorem `A|T` assumed, as in
the extension); every substitution used below was checked to be an exact
inverse of its defining relation (`64f4-z^2 = AR`, `s^2-2z_q = AQ`,
`256f5_P-rs+2s^2u = AP1`, `2048f6_E-2sp1-4qsu_L-8u_L^2 = Ae1`,
`qs+4u_L = A*ell`).

## 3. Charged D8--D11 identities: CONFIRMED

On `V0=AS`, `T=AU` (rows 0--7 verified pole-free), with `K=64F4-Z^2`:

- complete deepest D8 class `3K^2/(32768A^2)` (and nothing deeper);
- after `K=AR`, complete remaining D8 polar part
  `-5c2(S^2-2Z)^3/(65536A)`;
- after `S^2-2Z=AQ` on `c2!=0`, with `D=R-4SU`, `P=256F5-RS+2S^2U`:
  complete D9 `3DP/(65536A)` and complete deepest D10
  `3P(P-2SD)/(524288A^2)`;
- rootwise `A|P`: scalar anchors confirm the branch logic — a point with
  `D=0, P!=0` passes D9 and fails deepest D10; `P=0` passes both.  At
  every root of squarefree `A`, `DP=0` and `P(P-2SD)=0` force `P=0`; over
  characteristic zero with distinct roots this gives `A|P`;
- after `P=AP1`, all D9 poles vanish; complete residual D10
  `D(20c2D+3Egen)/(524288A)` with
  `Egen=2048F6-2SP1+Q(R-8SU)-8U^2`;
- complete deepest D11 `D*B11/(1048576A^2)` with the displayed
  `B11=-10c2SD-3072F6S+3P1S^2-3QS(R-6SU)-6U(R-6SU)`.

Every identity was rebuilt coefficientwise from my recurrence and matched
as the **complete** stated class (full negative part where claimed, full
`A^-2` class where claimed, with the minimal pole order asserted).

## 4. The valuation defect, sharpened: REFUTED as charged, repaired

The charged report's sentence that the branch `D=0 mod A` "survives both
(A10r) and the deepest D11 equation" is false, exactly as the extension
found.  I sharpen the refutation to a closed form.  Writing `D=A*d1`
(i.e. `R=4SU+A*d1`) and substituting consistently everywhere (including
inside the `F4`/`F5` lifts), the **entire** weight-11 negative part is

```text
g11^- = (N11 + 4*d1*B11r0) / (4194304*A),
B11r0 = B11|_{R=4SU} = -3072F6S + 3P1S^2 + 6QS^2U + 12SU^2,
```

with `N11` as in Section 5.  The `d1`-dependent residue is nonzero, so
`A|D` alone generally leaves a simple pole; surviving deepest D11 with
`d1 != 0` costs the additional codimension condition
`N11 + 4*d1*B11r0 ≡ 0 (mod A)`, which is not automatic.  Setting `d1=0`
recovers the exact-`D=0` class below, confirming consistency.

**Impact:** the charged "smallest exact successor" is mis-specified as
stated; the correct successor is the exact equation `D=0` (or the extra
valuation condition above).  I audited every other sentence of the charged
report against my reconstruction: **this is the only mathematical defect
in it.**  The extension's repair is correct.

## 5. Exact `D=0` paired forcing: CONFIRMED

Imposing exact `D=0` (`R=4SU`), with

```text
E = 2048F6 - 2SP1 - 4QSU - 8U^2   ( = Egen|_{D=0}, verified),
L = QS + 4U,   M = P1 + 2QU,
N11 = 5c2*L*(4E+L^2) + 6E*M,
```

the complete negative D11 part is `N11/(4194304A)` and the independently
rebuilt deepest D12 class is `(3E^2-2S*N11)/(33554432A^2)`.

**Field/radical scope, stated exactly.**  At each root of `A` over a
characteristic-zero field (A squarefree, so four distinct roots in a
splitting field): D11 gives `N11=0`; D12 then gives `3E^2=0`, hence `E=0`
(3 invertible, field reduced); substituting back, `N11 = 5c2L^3 = 0`, and
on the open `c2 != 0` (5 invertible) `L=0`.  Distinct roots give `A|E`
and `A|L` over the splitting field, and divisibility descends.  The only
"units" used are 3, 5, and `c2`; no nonvanishing of `S`, `U`, or `Q` is
assumed anywhere in this step.  This is a field-point/radical necessity
only — it proves nothing over a nonreduced parameter scheme and asserts
no ideal membership.

## 6. Post-lift D12/D13: CONFIRMED

With `E=Ae1`, `L=A*ell` (hence `U=(A*ell-QS)/4` and the induced `F6`
substitution), every D11 pole vanishes.  With `J=P1-SQ^2/2` and
`N=8192F7-e1S+QJ`:

- complete remaining D12 polar part `J(20c2J+3N)/(8388608A)`;
- the **entire** `A^-2` class at D13 is
  `-S*J(20c2J+3N)/(33554432A^2)`, i.e. `-S/4` times the D12 numerator
  with one more denominator power — not an independent factor cut, as the
  extension says.

The complete subleading D13 (`A^-1`) class was inspected: 25 terms in
`{c2, c6, c8, e1, ell, f7, f8, p1, q, s}`.  No registered mode is absent
that could invalidate the literal survivor below; the fixture replay
(Section 7) closes weight 13 literally with these modes live.

## 7. Literal raw D0--D15 survivor: CONFIRMED, with one sharpening

The Section-5 fixture was rebuilt from scratch over `Q`: `A=X^4-1`,
`S=Q=c2=c6=1`, `U=-1/4`, `R=-1`, `Z=(1-A)/2`, `P1=1/2`,
`F4=(Z^2-A)/64`, `F5=(A-1)/512`, `F6=1/4096`, `F7..F15=0`, other modes 0.
Branch consistency verified (`D=0`, `S^2-2Z=A`, `K=AR`, `P=A/2`,
`E=L=J=0`).  Then:

- all `G0..G15` evaluate to literal polynomials and all determinant rows
  `D0..D15` vanish identically as polynomials in `X`;
- windows `deg F_n <= 16-n`, `deg G_n <= 24-n` hold for all `n=1..15`
  (with `deg F0 = 16`, `deg G0 = 24` exactly);
- `G12 = 4093/268435456`, `G13=G14=G15=0`;
- **c14 forcing:** the weight-14 class is affine in `c14`; its polar
  residue is nonzero at `c14=0` and the `c14`-coefficient residue is
  nonzero, with the unique root `c14 = -6139/17179869184 = -6139/2^34`.
  Uniqueness is exact (the affine residue vanishes identically at exactly
  one scalar).  D15 then vanishes with no further condition;
- **q1-freeness VERIFIED** (not merely asserted): the linear system
  `A'R0+2AR0' = V0 = A` with `deg R0 <= 4` is inconsistent over `Q`
  (coefficients force `a1=1/2` and `a1=1/6` simultaneously).  Under the
  frozen convention `V0=A'R0+2AR0'`, this fixture is not a q1 point.

**Sharpening.**  Dropping `c6` (with `c14` frozen) first fails at weight
14 — the intended reason: the weight-14 residue moves and the frozen
`c14` no longer cancels it.  However, re-tuning `c14` to `5/2^34` under
`c6=0` rescues the entire D0--D15 replay.  So on this fixture `c6` is
genuinely **present** (as the extension claims) but is **not forced** by
D0--D15: the pair `(c6, c14)` has one free direction at this depth.  The
extension report never claims `c6` is forced, so this is a precision, not
a defect; but any successor should not cite this fixture as evidence that
`c6 != 0` is necessary.

## 8. Separate `c2=0` companion: CONFIRMED

Without the `H`-lift, on `V0=AS`, `T=AU`, `K=AR` only, with `H=S^2-2Z`,
`D=R-4SU`, `P0=256F5-RS+2S^2U+2UH`:

- complete D9 `3D*P0/(65536A)`;
- complete deepest D10 `3[P0(P0-2SD)+HD^2]/(524288A^2)`.

Rootwise: `D=0, P0!=0` dies at deepest D10 (forces `P0=0` at every root,
hence `A|P0`); then `HD^2=0` root by root, a genuine per-root split
(`H=0` or `D=0`) that does **not** globally force `A|H` or `A|D`.  Scalar
anchors confirm all three branch behaviours.  This stratum is kept
disjoint from the `c2 != 0` open and none of its conclusions are merged.

## 9. Sensitivity mutations (all fail for the intended reason)

| mutation | intended failure | observed |
|---|---|---|
| M1 wrong D8 factor (`K` for `K^2`) or coefficient (`3/65536`) | class mismatch | caught |
| M2 treating `A|D` as `D=0` | surviving simple pole | exactly `(N11+4d1*B11r0)/(4194304A)` |
| M3 dropping `c6` | weight-14 residue moves under frozen `c14` | first polar failure at weight 14; `c14=5/2^34` retune rescues (see §7) |
| M4 wrong `c14` (`0` and `c*+1`) | weight-14 pole survives | caught; unique affine root `c*` |
| M5 perturbing `F7` from 0 to 1 | D13 pole | D0..D12 clean, D13 pole exactly `6139/(8192A)` |
| M6 deleting born mode `c14` from the recurrence | identical failure to `c14=0` | residues byte-identical: modes may not be deleted |
| M7 wrong mode exponent (`c14 ↦ -1/2`) | determinant identity breaks at row 14 | rows 0--13 zero, row 14 nonzero |

## 10. Verdict and non-claims

**REPAIR.**  Proven-identity layer: all charged and extension formulas
D8--D13 are coefficientwise exact.  Field/radical layer: `A|K`, `A|H`
(on `c2!=0`), `A|P`, then on exact `D=0`: `A|E`, `A|L`; on `c2=0`:
`A|P0` and per-root `HD^2=0`.  Defect layer: the charged claim that
`A|D` survives deepest D11 is refuted, with the exact surviving pole
exhibited; it is the only defect in the charged report, and the
extension's exact-`D=0` repair is correct.  Literal-existence layer: one
verified non-q1 rational point satisfies D0--D15 in the legal windows
with `c2=c6=1` and forced `c14 = -6139/2^34` (with the §7 caveat that
`c6` is present but not forced at this depth).

Nothing here proves scheme membership, ideal-theoretic divisibility,
endpoint emptiness, q1 exclusion, unrestricted branch-P exclusion, a
Keller theorem, or JC2.  This lane is a different-model hostile review of
a same-model extension; promotion rules are the campaign's to apply.

## 11. Replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  xmodel/ggv-upper-endpoint-active-c2-d8-d15-hostile-review-fable5-20260828-check.py
```

Terminal marker:

```text
FABLE5_HOSTILE_ACTIVE_C2_D8_D15=REPAIR
```

Runtime ≈ 19 s (pure Python, exact rationals).  The checker validates
`cases/ggv_8_28_upper_endpoint_active_c2_d8_d15_hostile_review_fable5_20260828/RESULT.json`
byte-exactly on replay and re-verifies all seven frozen input hashes at
start and end.
