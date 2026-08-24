# Hostile different-model review — round-2 `NORM-MOMENT-SEP` (`DIFFERENT-INSUFFICIENT`)

| Field | Value |
|---|---|
| Claim | Producer-checked bounded R-root verdict `DIFFERENT-INSUFFICIENT` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Evidence tier | exact `QQ[q]` Laurent / companion-matrix arithmetic; four preregistered records; `m <= 2`; formal-local Darboux controls, not polynomial Keller maps |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, Bacon/R receiver lane). COORDINATION.md promotion rule 1 is satisfied. |
| CLI | `grok 1.0.5 (5115b46bc909) [stable]` |
| Python | documented `python3` = CPython 3.14.6 (`/opt/homebrew/opt/python@3.14/bin/python3.14`); producer pin CPython 3.9.6 (`/usr/bin/python3`); stdout **byte-identical** across both |
| Host | `dc-mbp-m2.local`, Darwin 23.6.0 arm64 |
| Review window (UTC) | 2026-08-24T03:01:53Z – 2026-08-24T03:07:14Z |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `8bf25a52f5f6c20886b77c6d9aeeb879eb18f8e4` |
| Scratch | `/tmp/jc2-norm-moment-sep-grok-Ou6h8i` (fresh `mktemp -d`, outside the repository) |

**Promotion.** The scoped `DIFFERENT-INSUFFICIENT` stop may be promoted off producer-checked provisional: the displayed local finite algebra, different/derivation conductor, selected contact/gcd decoration, coordinate valuations, local Jacobian two-form, and complete first principal part of `Tr(x)` do not determine the quadratic coordinate moment on the two exact denominator-42 formal Darboux completions. Nothing else may.

**Quarantine if this review is treated as a failure.** Do not read this as a polynomial Keller countermodel, a refutation of a global signed or polynomial-origin identity, a `NO-TYPED-FUNCTOR` / `FINGERPRINT-COLLISION` finding, a statement about TRACE-REG, integrality, properness, or any conclusion about JC2. Do not run or backfill the preregistered-but-unreached native GGV type gate from this review. Do not launch theorem descendants.

**Dirty-state perimeter.** HEAD matches the preregistered basis. Tracked dirt is `APPROACHES.md`, `AUDIT.md`, `COORDINATION.md`, `PROGRESS.md`, and `pilot-local.log`; none is an input of this gate. The case directory `cases/round2_norm_moment_sep/` and the producer report are untracked post-basis artifacts, as are the hashed round-1 / ideation inputs. Those frozen inputs were rehashed here and match the preregistration table byte-for-byte. The farm manifest was content-addressed only; its cases were not parsed.

Reviewer discipline: producer implementation read in full before execution; exact integers/fractions only; all scratch output outside the repository; no network; no author contact; no shared-ledger edits; no repository writes except this file; native type-gate function not invoked; no descendants launched. Verdicts rest on independent matrix/trace/wedge calculations, not on stored `verdict` strings or record hashes.

---

## Claim under review (not enlarged)

Five clauses, attacked separately.

---

## Verdict table

| Clause | Verdict | What would have flipped it |
|---|---|---|
| 1. Independent rederivation of `QQ(q)((u))/QQ(q)((t))`, `t=u^e`, trace filter, different, and trace-pairing discriminant; the two different calculations agree exactly | **CONFIRMED** | round-1 import; filter/companion disagreement; pairing-matrix determinant sign or `e^e t^{e-1}` mismatch; different-norm conversion sign error |
| 2. Triangular automorphism and `(x^2,xy)` nonproper/non-Keller controls give the stated zero/pole principal parts; receiver neither pole-blind nor frozen-accepting | **CONFIRMED** | nonempty C1 affine PP; C2 missing `2q^2 t^{-1}` or extra poles; stored traces not independently recomputable |
| 3. D1/D2 share algebra, different/conductor, selected decoration, valuations, local two-form, and complete `Tr(x)` first PP; coordinates kept as a separate differing field | **CONFIRMED** | any listed fixed field actually depends on `b`; `x`/`y` multiplication hashes equal; `b` leaking into decoration/Jacobian/algebra |
| 4. `Tr(x_b)=42(t^{-2}+t^{-1}+b t)` and `Tr(x_b^2)=42(t^{-4}+2t^{-3}+t^{-2}+2b t^{-1}+2b+b^2 t^2)`; residues 84 and 168; `y_b` first two moments have no negative PP; wedge identity holds | **CONFIRMED** | extra `e\|n` pair in `x^2`; residue not `84b`; `ord_u(y_b)≠126`; wedge sign/coefficient not `+42 u^{41}` |
| 5. Scoped conclusion only; not a Keller countermodel; no global-identity refutation; native type gate not run; nothing about TRACE-REG or JC2 | **CONFIRMED** | overbroad TRACE-REG/JC2/Keller language; native gate executed; `GLOBAL-SEPARATOR-CANDIDATE` fired |

All remarks below are non-blocking (hardcoded decoration attachment, C1 PASS locking only empty PPs, closed-form rather than 42×42 producer dets, split-uniformizer packaging, valuation certificates for `y`, compact-JSON key aliases). None changes a number, a scope, or a verdict.

---

## What was rerun, independently, and not

```sh
SCRATCH=$(mktemp -d /tmp/jc2-norm-moment-sep-grok-XXXXXX)
# SCRATCH=/tmp/jc2-norm-moment-sep-grok-Ou6h8i

# Documented replay (this machine's python3 = 3.14.6)
python3 cases/round2_norm_moment_sep/norm_moment_sep.py \
  | LC_ALL=C shasum -a 256
# c81c75b0cc3721f1198d3dc049f66cd3c87fdb24c81e6542d7cecfd15bffae96  -

python3 cases/round2_norm_moment_sep/norm_moment_sep.py \
  > "$SCRATCH/stdout-py314.json"
# 41522 bytes; same digest

# Producer-tested interpreter
/usr/bin/python3 cases/round2_norm_moment_sep/norm_moment_sep.py \
  > "$SCRATCH/stdout-py39.json"
# cmp silent; BYTE-IDENTICAL with 3.14.6

# README jq gate against scratch stdout (not against compact results.json)
python3 cases/round2_norm_moment_sep/norm_moment_sep.py | jq -e '
  .status == "STOPPED" and
  .verdict == "DIFFERENT-INSUFFICIENT" and
  .stages.receiver_controls == "PASS" and
  .stages.fixed_different_separator == "PASS_STOP" and
  .stages.native_source_type_gate ==
    "NOT_REACHED_BY_PREREGISTERED_HARD_STOP" and
  .derivation_checks.all_agree and
  .fixed_different_varying_moment.same_local_algebra and
  .fixed_different_varying_moment.same_different_and_conductor and
  .fixed_different_varying_moment.same_retained_decoration and
  .fixed_different_varying_moment.same_local_jacobian_data and
  .fixed_different_varying_moment.same_coordinate_valuations and
  .fixed_different_varying_moment.same_x_first_principal_part and
  (.fixed_different_varying_moment.same_x_second_principal_part | not)
'
# JQ_GATE_PASS
```

Python stderr is empty (the 29-byte files next to the timed copies are `/usr/bin/time -p` stats). The native type-gate function was not called: replay JSON stores the string `NOT_REACHED_BY_PREREGISTERED_HARD_STOP`, not a gate object, and contains neither `4_12mn34d64_c2` nor `NO-TYPED-FUNCTOR`.

Independent work, **not** `norm_moment_sep.py` and **not** stored `verdict` / `record_sha256` strings as authority:

- Scratch script `indep_norm_moment.py` (SHA-256 `7c2ad0e2f9c616fd53bcd9f2aa89cc97420be31d70c58b9ab21506a41d5af86a`), standard library only, no producer import. Result: `ALL_INDEPENDENT_CHECKS_PASSED`, 0 failures.
- Rehashed every frozen preregistration input against disk: **0 mismatches**.
- Built actual trace-pairing matrices and took Gaussian determinants over `QQ` at `t=2` for `e ∈ {1,2,3,4,5,6,7,8,9,10,12,41,42,43}` and at `t=3` for `e ≤ 12` and `e=42`.
- Compared the conjugation/divisibility filter to a from-scratch companion-basis diagonal trace on every monomial `u^n` for `e ∈ {1,2,3,6,42}` and `-3e ≤ n ≤ 3e`, plus numeric multiplication-matrix traces for representative positive powers.
- Expanded `x_b^2` by explicit exponent pairs (not producer `laurent_pow`) and filtered.
- Differentiated `x_b` and checked the two-form identity by cancellation, not series inversion.
- Confirmed `b` lives in the coordinate fields and in the regular part of `Tr(x)` / the `t^{-1}` slot of `Tr(x^2)`, not in algebra, different, decoration coefficients, two-form, or valuations.

Not done, and forbidden by the review contract:

- No parse of `jc72108/systems/farm/4_12mn34d64/manifest.json` beyond SHA-256.
- No call of `native_type_gate()`.
- No moment above two, no network, no shared-ledger write, no descendant lane.

---

## Pins and hashes (SHA-256)

| File | Hash | Matches |
|---|---|---|
| `cases/round2_norm_moment_sep/PREREGISTRATION.md` | `15caf35ca825f7a56bb6766cf585b4845c41a491904a748301264a7eb708330b` | pin, producer, replay `inputs` ✓ |
| `cases/round2_norm_moment_sep/norm_moment_sep.py` | `150cdc2fb211d20685694e698eeb14f295c7d660be419eb8642d339815255601` | producer report + runtime self-hash ✓ |
| `cases/round2_norm_moment_sep/README.md` | `37dcd941a33e146af18bdb9497a8bc3bbd21bbe72e0e36b298918d1373588608` | (recorded here) |
| `cases/round2_norm_moment_sep/results.json` | `0cd40789cbac93fe6d517c6b86e5bf83f094f454b6cb4ba5e4b20f56a470b2b6` | compact certificate; overlapping record hashes match full stdout ✓ |
| `xmodel/round2-norm-moment-sep-20260824.md` | `6bbdad39f53f17e39f59ebcc60d157722100b92cb858cfa9a127883d66515fa9` | (recorded here) |
| full deterministic stdout, 41522 bytes | `c81c75b0cc3721f1198d3dc049f66cd3c87fdb24c81e6542d7cecfd15bffae96` | README + compact `full_stdout_sha256` + both Pythons ✓ |
| `xmodel/ideation-20260824T0156Z-synthesis.md` | `9c0455ddae2388d7f5256ec46094c0d97dd5bc6748f2b61177f736cc23581f50` | prereg table ✓ |
| `xmodel/ideation-20260824T0156Z-adversary.md` | `b9ad25c0cd16ec6698b7922128f00da6ca4dede812dc38d9e9444f42dcf1aec8` | prereg table ✓ |
| `xmodel/review-round1-proof-gates-claude.md` | `ef0bf14d10abfedb5c4b8921344ff9de1dc0078f287ed5c6fe3fc7a24a522e11` | prereg table ✓ |
| `xmodel/round1-trace-regularity-20260824.md` | `908dc24bfb7f493d108e05135d863bc1a32a4c4ef8e3889f7dee89574978920c` | prereg table ✓ |
| `cases/round1_trace_probe/trace_probe.py` | `faadfaf26c7184c24fc3e55a3de90c881e38b0bf12293cb245bcaa9ab5ad0372` | hash-only; not imported ✓ |
| `cases/round1_trace_probe/results.json` | `51f5a6e200327dd343c1c06ed2e9529ef807428531d21535caef63c655f00706` | hash-only ✓ |
| `jc72108/systems/farm/4_12mn34d64/manifest.json` | `26bf6d4e7845e6278a24d09161bef36e320af2e87bff1c32a1f2a5eeae72e577` | hash-only; type gate not run ✓ |

Producer imports: `hashlib`, `json`, `sys`, `fractions.Fraction`, `pathlib.Path`, `typing.Any`. No `trace_probe`, no `sympy`/`numpy`, no network. The three `trace_probe` string hits are path keys in `PINNED_INPUTS`.

---

## Clause 1 — local algebra, traces, two discriminants

**CONFIRMED.**

Let `k = QQ(q)`, `K = k((t))`, `L = k((u))`, `t = u^e`. Power basis `1,u,…,u^{e-1}`. Reduction `u^n = t^{⌊n/e⌋} u^{n mod e}` with remainder in `{0,…,e-1}` (Python `divmod` on negative exponents is this remainder, and that is the correct one).

Field trace is the trace of `K`-linear multiplication, which does not require `μ_e ⊂ k`. For a monomial,

```text
Tr(u^n) = e t^{n/e}  if e | n, else 0.
```

Two producer algorithms implement this independently: the divisibility filter, and the companion-basis diagonal (for each basis index `i`, keep the coefficient of `u^i` after reducing `u^{n+i}`). They agree in the replay (`algorithms_agree: true` on every computed moment). This reviewer added a third path: form the actual `e × e` multiplication matrix at a numeric `t` and sum the diagonal. All three agree on the monomial grid above and on the C1/C2/`x_b` series.

Different of the monogenic extension `k[[u]]/k[[t]]` is `(e u^{e-1})`. The trace-pairing matrix `(Tr(u^{i+j}))_{0 ≤ i,j < e}` has a unique nonzero per row: `e` at `(0,0)` and `e t` at `(i, e-i)` for `i > 0`. It is a monomial matrix for the permutation `[0, e-1, e-2, …, 1]`. Inversion count `C(e-1,2) = (e-1)(e-2)/2`, whose parity equals `⌊(e-1)/2⌋`. Product of entries `e · (e t)^{e-1} = e^e t^{e-1}`. Hence

```text
det(pairing) = (-1)^{⌊(e-1)/2⌋} e^e t^{e-1}.
```

Independently, `X^e - t` has `Norm(u) = (-1)^{e-1} t` and

```text
disc(X^e - t) = (-1)^{e(e-1)/2} Norm(e u^{e-1}),
```

which is the same sign, coefficient, and `t`-exponent. Producer stores these as two distinct closed forms and checks equality. Reviewer Gaussian-eliminated the *actual* pairing matrix over `QQ` at `t=2` (and `t=3` on a subset), including the 42×42 case:

| `e` | sign | `e^e` | `t^{e-1}` | matrix det at `t=2` |
|---|---|---|---|---|
| 1 | `+` | 1 | `t^0` | `+1` |
| 2 | `+` | 4 | `t` | `+8` |
| 3 | `−` | 27 | `t^2` | `−108` |
| 4 | `−` | 256 | `t^3` | `−2048` |
| 42 | `+` | `42^{42}` | `t^{41}` | `+42^{42}·2^{41}` |

`42^{42} = 150130937545296572356771972164254457814047970568738777235893533016064`, matching the producer integer. Pairing inversions at `e=42` are `C(41,2)=820` (even), sign `+1`. No discriminant sign error.

Split-uniformizer packaging: records store `{"t": "u^e", "unit_twist": "1"}`. Residue field `QQ(q)` need not contain `μ_e`. That is a presentation choice, not a claim that `L/K` is Galois. The matrix trace is the definition used here; the filter is an equivalent formula for this presentation (same observation as the confirmed P2 remark T1, non-blocking).

---

## Clause 2 — C1 / C2 poles

**CONFIRMED.**

**C1.** `(P,Q)=(x, y+x^2)`, `e=1`, `x=t`, `y=q-t^2`. Extension is trivial, trace is the identity. Independent full traces (stronger than the preregistered empty-PP check):

```text
Tr(x)=t,     Tr(x^2)=t^2,
Tr(y)=q-t^2, Tr(y^2)=(q-t^2)^2 = q^2 - 2q t^2 + t^4.
```

All four principal parts empty. Different `(1·u^0)` is a unit. Stored producer traces are exactly these series, computed by both algorithms, not copied from a frozen table. The C1 *PASS predicate* only asserts empty principal parts (as the preregistration wrote); the stored traces nevertheless lock the regular parts, and this review recomputed them.

**C2.** `(P,Q)=(x^2, xy)`, `t=u^2`, `x=u`, `y=q/u`. Non-Keller (`J=2x^2=2t` on the arc) and nonproper (generic `(0,q)` has no affine preimage). Independent traces, including the global-minpoly cross-check `T^2-P` for `x` and `y^2=Q^2/P`:

```text
Tr(x)=0,  Tr(x^2)=2t,  Tr(y)=0,  Tr(y^2)=2q^2 t^{-1}.
```

The unique negative principal part is `2q^2 t^{-1}` (producer `y_second_principal_part_sha256` `b4057cad…f293`, JSON `2*q^2*t^{-1}`). Numeric companion-matrix traces of `x` and `x^2` at `t=7` are `0` and `14`. A pole-blind receiver would have emptied `Tr(y^2)`; a frozen-only receiver would not have two agreeing algorithms plus this independent matrix path. Different `(2u)`, pairing disc `+4t`, matches `e=2`.

---

## Clause 3 — D1/D2 fixed fields vs coordinates

**CONFIRMED.**

Both records: `e=42`, `t=u^{42}`,

```text
x_b = u^{-84} + u^{-42} + u^{-30} + u^{-10} + u^{-5} + b u^{42},
y_b = 42 q u^{41} / (dx_b/du),   b=1,2.
```

Independently derived and then compared:

| Field | D1 | D2 | Agree? |
|---|---|---|---|
| algebra `U^{42}-t`, rank 42, `f=1`, split `t=u^{42}` | `4b478e76…e08c` | same | yes, depends only on `e` |
| different `(42 u^{41})`, conductor exponent 41, disc `+ 42^{42} t^{41}` | `3fc5e68b…e8a8` | same | yes, depends only on `e` |
| gcd chain / char indices / visible exponents `(-30,-10,-5)` with coeff 1 | `c299892d…e952` | same | yes; see remark N1 |
| `dP∧dQ = 42 u^{41} du∧dq`, wedge identity `True` | `ceb33356…2eed` | same | yes; identity holds for every `b` with `x'≠0` |
| `ord_u(x)=-84`, `ord_u(y)=126` | both | both | yes; `b u^{42}` and `42b u^{41}` do not move valuations |
| `PP Tr(x) = 42 t^{-2} + 42 t^{-1}` | `19fd6e4c…7766` | same | yes; `b` sits at `t^{+1}` |
| `PP Tr(x^2)` `t^{-1}` slot | 84 | 168 | **no** |
| `x` multiplication hash | `9c593e70…f9e2` | `bab8d240…8c38` | **no** |
| `y` multiplication hash | `ad8b1385…422f` | `b21695d1…a6dc` | **no** |

Coordinate data are a separate field. After unit-denominator normalization,

```text
y_num = −(q/2) u^{126}          (independent of b)
y_den = 1 + (1/2) u^{42} + (5/14) u^{54} + (5/42) u^{74}
        + (5/84) u^{79} − (b/2) u^{126}.
```

Producer JSON matches this exactly (`D1` last den coeff `-1/2`, `D2` last den coeff `-1`). The `b`-slot of `x` is the last numerator term (`1` vs `2`). No leakage of that coefficient into algebra, different, contact-visible coefficients, two-form, or valuations. Support lists the *exponent* 42 (present for both nonzero `b`) but not the coefficient; `varying_b_slot_retained` is `False`. Full `Tr(x)` differs by the regular term `42 b t`; the *principal part* does not.

Offsets of the non-invariant exponents from the leading `-84` are `54,74,79`. Successive gcds `42 → 6 → 2 → 1`, characteristic indices `(7,3,2)`. Varying slot offset `126 > 79`, strictly after the last retained contact level, and conjugation-invariant (`42 | 42`). Same collision geometry as the confirmed P2 audit, now with different, conductor, Jacobian two-form, valuations, and full `m=1` principal part added to the frozen packet.

---

## Clause 4 — moments, residues, `y`-poles, wedge

**CONFIRMED.**

Filter on `x_b` keeps only exponents divisible by 42: `-84, -42, 42`. Weight 42:

```text
Tr(x_b) = 42 (t^{-2} + t^{-1} + b t).
```

For `x_b^2`, the exponent pairs whose sum is divisible by 42 are exactly

```text
(-84,-84), (-84,-42), (-84,42),
(-42,-84), (-42,-42), (-42,42),
( 42,-84), ( 42,-42), ( 42, 42).
```

No pair involving `-30`, `-10`, or `-5` survives (Laurent truncation attack fails: the series is finite and every pair was enumerated). Collecting coefficients and weighting by 42:

```text
Tr(x_b^2) = 42 (t^{-4} + 2 t^{-3} + t^{-2} + 2b t^{-1} + 2b + b^2 t^2).
```

Residue `[t^{-1}] Tr(x_b^2) = 84 b`, hence **84** and **168**. Companion-diagonal traces agree with the filter on both powers. First principal parts coincide (`42 t^{-2}+42 t^{-1}`); quadratic principal parts differ already at `t^{-1}` and also in the displayed higher negative terms being equal while that slot changes.

`dx_b/du` has valuation `-85`, so `ord_u(y_b)=41-(-85)=126`. Then `ord_u(y_b^m) ≥ 126 m`, so every `u`-exponent in `y_b` and `y_b^2` is positive and every surviving `t`-exponent is at least `3m ≥ 3 > 0`. No negative principal part. The producer certifies this by valuation rather than expanding `1/x'`; the bound is valid because the shifted denominator is a unit in `k[[u]]` (constant term 1).

Wedge, by cancellation, not inversion:

```text
dx∧dy = (dx/du) (∂y/∂q) du∧dq,
∂y/∂q = 42 u^{41} / (dx/du),
dx∧dy = 42 u^{41} du∧dq = d(u^{42}) ∧ dq = dP ∧ dQ.
```

Coefficient `+42`, exponent `41`. A minus sign would have failed the producer's `rational_equal` and this review's cross-multiplication. `q` is absent from `x`, so there is no extra quotient-rule term.

---

## Clause 5 — scope

**CONFIRMED.**

Replay stages:

```text
receiver_controls:         PASS
fixed_different_separator: PASS_STOP
native_source_type_gate:   NOT_REACHED_BY_PREREGISTERED_HARD_STOP
global_separator:          preregistered false / unavailable
```

The hard stop fired before the native source type gate, as preregistered. Compact `results.json` independently records `native_type_gate_executed: false`. `GLOBAL-SEPARATOR-CANDIDATE` cannot fire: no candidate identity was preregistered.

Producer report §4 and the compact `scope` field state the narrow negative: the listed local algebra/different/contact/valuation/Jacobian data do not determine the quadratic coordinate moment. They label the Darboux records as formal-local controls, not polynomial Keller maps; `m≤2` as a discriminator, not an integrality test; and they refuse TRACE-REG, finiteness, properness, automorphism, counterexample, and JC2. The full-stdout `scope` string is slightly shorter (it does not name TRACE-REG/JC2) but does not overclaim. Coordinate multiplication data are acknowledged as the actual carriers of the differing moments. A global polynomial-origin identity could still impose further relations; nothing here refutes that possibility.

This is a strengthening of the confirmed P2 `INSUFFICIENT-DATA` collision (same completions, residues 84/168), not a reuse of P2 code and not a claim about TRACE-REG itself.

---

## Attacks that did not fire

- **Laurent truncation.** `x_b` is a six-term Laurent polynomial; `x_b^2` has 21 ordered pairs, of which nine survive the filter, matching the closed form.
- **Split-uniformizer ambiguity.** Unit twist is recorded as `1`. Matrix trace does not need `μ_{42} ⊂ QQ(q)`. No hidden `c_0` factor in these controls.
- **Different/discriminant sign.** Pairing permutation, different-norm, resultant conversion, preregistration `⌊(e-1)/2⌋` formula, and actual matrix determinants agree, including sign `+` at `e=42`.
- **Coordinate leakage into fixed fields.** `b` appears in `x` (slot `u^{42}`), in `y_den` (slot `u^{126}`), in the regular term of `Tr(x)`, and in `[t^{-1}] Tr(x^2)`. It does not appear in algebra, different, visible contact coefficients, two-form, or valuations.
- **Wedge sign.** Positive `42 u^{41}`.
- **Overbroad conclusion.** Stop + scope language match the preregistration precedence; native gate unreached; no JC2/TRACE-REG implication.

---

## Non-blocking remarks

- **N1.** `contact_decoration()` is a nullary hardcoded blob. Software equality `same_retained_decoration` is therefore true by construction. The *mathematical* decoration of the two series was independently recomputed (support, invariant/visible split, gcd chain, characteristic indices, leading coefficient 1) and does match that blob for both `b=1,2`. The clause is about the objects agreeing, which they do.
- **N2.** C1's PASS predicate locks only empty principal parts. Full traces are computed, stored, and here independently verified as `t`, `t^2`, `q-t^2`, `(q-t^2)^2`.
- **N3.** Producer discriminants are closed forms, not a 42×42 determinant. This review computed the matrices.
- **N4.** Darboux `y` moments are valuation certificates (`trace: null`). Sufficient for “no negative principal part”; not a computation of `Tr(y_b)`.
- **N5.** Compact `results.json` uses aliased fdvm keys (`same_different_and_derivation_conductor`, `same_retained_contact_decoration`, `same_local_jacobian_two_form`) versus full stdout (`same_different_and_conductor`, …). README `jq` is against full stdout. Overlapping record/algebra/different/PP hashes and the verdict agree. Packaging only.
- **N6.** Function name `darbouz_control`. Typo, not a math error.

---

## What may enter `AUDIT.md`, and what must remain open

**May enter** (promotion gate satisfied by this different-model review), at tier EXACT, citing this file:

The bounded R-root `NORM-MOMENT-SEP` fired `DIFFERENT-INSUFFICIENT` on two exact denominator-42 formal Darboux completions that share finite local algebra `U^{42}-t`, different `(42 u^{41})` and conductor, selected contact/gcd decoration with chain `42 → 6 → 2 → 1` and indices `(7,3,2)`, valuations `(-84, 126)`, local two-form `42 u^{41} du∧dq`, and complete first principal part `42 t^{-2}+42 t^{-1}` of `Tr(x)`, while the quadratic residues of `Tr(x^2)` are 84 and 168. The listed local data therefore do not determine the quadratic coordinate moment. Native type gate not reached. `GLOBAL-SEPARATOR-CANDIDATE` unavailable.

**Must remain open:**

- TRACE-REG for any actual Keller family; whether an augmented packet (complete branch pairing, native typed functor, polynomial-origin identity) determines the moment.
- Any polynomial Keller map, automorphism, counterexample, integrality, or properness claim.
- Native GGV source-to-receiver typing (`NO-TYPED-FUNCTOR` / `FINGERPRINT-COLLISION`).
- Any statement about JC2.

---

## Evidence scope of this review

Checked: producer script in full; documented replay plus Python 3.9.6 cross-check, both byte-identical to the pinned 41522-byte digest; README `jq` gate; every frozen input hash; independent companion/filter/pairing-matrix/convolution/wedge/valuation calculations (scratch script hash above); C1/C2 full traces; D1/D2 coordinate rationals; leakage into listed fixed fields; stop precedence and scope language against the preregistration; compact certificate overlapping hashes. One packaging mismatch (compact vs full fdvm key names) diagnosed and recorded as N5.

Not re-adjudicated: P1 `COSTUME` and P2 `INSUFFICIENT-DATA` beyond the formulas this gate consumes (those formulas were re-derived here and match the confirmed P2 review); farm packet contents; any native type-gate field.

— Grok 4.6, hostile different-model reviewer, 2026-08-24T03:07Z
