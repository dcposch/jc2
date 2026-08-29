# Hostile review — repaired normalized order-two square `r=1` receiver (V15)

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_r1_v15_validator_telemetry_repair_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest obstruction | none in the licensed `r=1` grade-thirteen claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. Stored PASS markers are evidence, never authority |
| Method | source reading, SHA-256 of every named pin and freeze-chain file, byte-level Q/`F_65521` and V8--V15 comparison, and hand identities only; no Singular, Sage, msolve, Lean, Groebner-basis computation, package compiler, CAS, or substantive exact Python |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of `RESULT.md` is
`fba49ea691edf8f272308d745fc5918f076d1b1670e875deea439777ed26ed69`.
Independently recomputed SHA-256 of `RESULTS.sha256` is
`10dc7bcfa1acb05d97df1f36ed4291bb8c66b416c928eaf32177fb92527a88a8`.
Independently recomputed SHA-256 of `EVIDENCE.sha256` is
`dc26e462ff415e9d6e8fc4c228e1f3012f0490e7ecf00b695e2348b9b709441b`.
Independently recomputed SHA-256 of `FREEZE.sha256` is
`5eec15866895da7692121cf9e1300f34e9914c45608d631751a24a0fb21bdc97`.
Every path named in `RESULTS.sha256` and `EVIDENCE.sha256` rehashes to its
printed digest. The V15--V1 freeze walker, including the shared-Faber
`tails.json` pin
`d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`
and canonical all-tails digest
`6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`,
rehashes. No file other than this review was written.

The producer statement and the registration agree: V15 is a validator-only
replay of the frozen V14 Singular input. Exact Q is the characteristic-zero
producer; `F_65521` is a software control. The licensed claim is
arcwise/set-theoretic emptiness of the normalized `r=1` leading section on
`D(p*k10)` after the frozen first-normal, half-weight, and `M=0` gates.

---

## Verdict

**CONFIRMED.**

On the generic-square first-normal chart `D(p*k10)`, after the reviewed
half-weight support and `M=0` gates, the substitutions

```text
A = sigma A0,   C = sigma^3 C0,   R = sigma R0,   k10 = k0,
```

with `A0,C0,R0` linear in `z` and `L = z^2+p/2` frozen, produce seven exact
loaded source rows at absolute grade thirteen. Those rows are the
lower-unitriangular Faber image of the proper part

```text
(5/16) k10 R0^3 / L.
```

Every competing unloaded, `k6`, `k2`, Taylor-target, and terminal-target
contribution is either polynomial in `z` or of strictly larger absolute
grade. Polynomiality therefore forces the remainder of `R0^3` modulo `L`
to vanish on `D(p*k10)`. The elementary remainder

```text
(b1 z + b0)^3  mod (z^2 + p/2)
  = b1 (3 b0^2 - (p/2) b1^2) z
  + b0 (b0^2 - (3p/2) b1^2)
```

has common zeros only at `b0=b1=0` over exact Q (and in characteristic
`65521`). That is contact-raising of the normalized order-one leading
section of `R`, not an empty square-branch conclusion and not a statement
about the zero section.

V15 freshly invokes the frozen V14 compiler. It does not silently consume
the quarantined V12 unbounded-D1 claim: the engine is fed only
`square_r1_v14_*.sing`, the r=1 source bytes are the V8--V12 freeze
through a radical/`std` patch and a hand-anchor move, and D1 scripts
remain an unused freeze-chain byproduct. V13 is a genuine negative
control at the premature hand-check. V14 has identical mathematical
stdout and fails only because `/usr/bin/time -v` telemetry made stderr
nonempty. V15 changes only that validator treatment, while still
rejecting `?`, `// **`, `error occurred`, `=FAIL`, timeout, nonzero
engine return, and missing or duplicate markers in either relevant
stream. Both fresh runs are free of the old
`// ** R1_rad is no standard basis` warning.

A positive verdict licenses only the firewalled claim below. It does not
license V12's unbounded D1 claim, any all-load fan, `p=0`, `k10=0`,
positive-order loads, terminal or Taylor closure, scheme structure, the
whole square branch, order two, `(8,12)`, maximum twelve, or JC2.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 1. Transitive ancestry of seven source rows; V15 does not consume D1 | first-normal substitutions, loads, gauges, signs, row order, grades; fresh V14 compile | **holds** |
| 2. First nonpolynomial grade-13 contribution `(5/16) k10 R0^3/L` | independent expansion; unloaded/`k6`/`k2`/targets strictly larger or polynomial | **holds** |
| 3. Seven rows as invertible lower-unitriangular Faber image | recurrence, proper numerator, not only the final marker | **holds** |
| 4. Cubic remainder and common zeros on `D(p*k10)` | both coefficients; divisions/characteristic; reduced support vs scheme | **holds**; set-theoretic only |
| 5. Actual Singular ideal | `inv*p*k0-1`; `std(radical)` before every `reduce`; support test; no `// **` | **holds** |
| 6. V13/V14 negative controls; V15 validator-only telemetry delta | premature hand-check; nonempty time-stderr; remaining rejections | **holds** |
| 7. `R0=0` is contact-raising of the normalized leading section | not empty square branch; not the zero section | **holds** |
| 8. Firewall | licensed vs unlicensed claims | **holds**; producer firewall matches the required scope |

---

## 1. Custody

Recomputed SHA-256 of the named pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| V15 `RESULT.md` | `fba49ea691edf8f272308d745fc5918f076d1b1670e875deea439777ed26ed69` | producer report |
| V15 `RESULTS.sha256` | `10dc7bcfa1acb05d97df1f36ed4291bb8c66b416c928eaf32177fb92527a88a8` | result manifest |
| V15 `EVIDENCE.sha256` | `dc26e462ff415e9d6e8fc4c228e1f3012f0490e7ecf00b695e2348b9b709441b` | evidence manifest |
| V15 `FREEZE.sha256` | `5eec15866895da7692121cf9e1300f34e9914c45608d631751a24a0fb21bdc97` | source freeze |
| V15 `REGISTRATION.md` | `86d7d0048f7a43f6419a5e8e878da0f689b2af642758815b797d9ccbcfedd753` | registration |
| V15 `run_aws.sh` | `43f0da6d0b45f25686cf3a1df8bfbe1e5fd70c2c6b4ac6d0b949b1821fc1bd3b` | validator |
| V14 `compile_r1_v14.py` | `acdfd2a4bb4a02e4ce65c26159f2f8f85a6c5979fe8535d66715aac0c19d7521` | frozen compiler |
| V14 `FREEZE.sha256` | `02cccba7f4e587244fe2d51bbf6968544ced051c497f4e0abd1104a6c988cbaa` | V14 freeze |
| exact-Q `square_r1_v14_q.sing` | `0b1efd2f1db5938ea18d488787d2346a9c253688719db5d673425fc76be13296` | compiled r=1 |
| `F_65521` `square_r1_v14_p65521.sing` | `d9aafc5304ccff369815814a2cbb8b6752b9754718c435ea2e29644d2708ca7c` | compiled r=1 |
| marker-only stdout (both fields) | `fc6ba5c3ec390a8aebf2991920cf8e05c63f64b275e253d79d3222eeac135dff` | engine stdout |
| both `validation` files | `c3a4c8e66bdf91563cd73c2f06524ec7b70334a90f57b5442d9c86d8a1a121e2` | validator payload |
| V12 source-support erratum | `997dda081223d99283bff92851e7da8bc260b7b3e52ff89b97fb0a50c817a114` | D1 quarantine |
| prior V12 hostile review | `509c9edf1c613fa4ff997d3da4acbfeccd7e0895fd76e2f471fad37d90ec15aa` | prior review |
| V13 `RESULT.md` | `0946651a9dbdfd37a2ae22559bde0524a5e7a6d81088e6357c794e1f5c737865` | negative control |
| V14 `RESULT.md` | `db047d7f665b1a130d4fa62b696ac10f5258341974097cec0a108e17ca604c2d` | negative control |

Exact Q (Box03, `ip-172-30-0-249`) and `F_65521` (r6d, `ip-172-30-0-45`) are
separate frozen runs: distinct hosts, tags, PIDs, compiled-script hashes,
stderr hashes, and `.meta` files. Both engine records have `rc=0`. Peak RSS
is about 14--15 MiB with zero swap; wall-clock is 0.03 s. Both validators
print

```text
engine_rc=0
validator=PASS_R1_V15_VALIDATOR_TELEMETRY_REPAIR
```

The two compiled inputs differ by exactly one token: `ring Rr1=0,...`
versus `ring Rr1=65521,...`. The twelve required markers occur once each
in the common stdout and in the order produced by the V14 hand-anchor
move. Neither stdout nor stderr contains `=FAIL`, `// **`, a leading
`? `, `error occurred`, or `no standard basis`. Stderr on both hosts is
exactly `/usr/bin/time -v` telemetry from `ops/aws_exact_lane.sh`, with
`Exit status: 0`.

`R1_SOURCE_HASHES=PASS` and `R1_RADICAL_STANDARDIZED=1` are unconditional
prints. The former is acceptable because the digest check is compile-time
in V1 against the frozen tails. The latter is acceptable because the
actual `std(radical(R1_I))` replacement is present in the frozen input
that ran, and because the old `// **` warning is absent. Neither print is
treated as authority for the algebra.

---

## 2. Question 1 — transitive ancestry and non-consumption of D1

**Verdict: holds.**

V1 `compile_r1_d1_ac.py` loads the frozen cge3 module, checks that
module's `EXPECTED` pins including `tails.json` and the load-ladder
compiler, and rechecks the canonical all-tails digest
`6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`.
Each of the seven ordinary coordinates is

```text
base.tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")
```

with target subtractions `mu2`, `mu4`, `mu6`, `J/4` on rows 2, 4, 6, 7
at absolute grades `28,32,36,38`. `tail_text` enforces monomial length,
load linearity, and weight `12+row` against the frozen Faber names. The
compiled `Phi1..Phi7` are those expanded tails under the first-normal
coefficient substitution, not a hardcoded Laurent polynomial.

First-normal substitutions in the V1 r=1 emitter, visible in the compiled
V14 scripts:

| Object | r=1 encoding |
|---|---|
| `p` | frozen `p` |
| `A` | `sigma*(a1 z + a0)` |
| `C` | `sigma^3*(c1 z + c0)` |
| `R` | `sigma*(b1 z + b0)` |
| `k10` | ring variable `k0` |
| lower loads | `k6`, `k2load` present, then forbidden at grade 13 |
| `L` | `z^2+p/2` |

The coefficient encoding matches the load-ladder / cge3 convention after
the documented insertion of the factors 2 and 4: `kc=sigma^2*(rz)`,
`kr=(pp)^2/4+sigma^2*(rc)`, and `n1=sigma^3*((pp*az)/2+cz)`. Direct
polynomial `C,R` therefore land on the same Faber slots as the older
chart. Gauges, signs, and row order: rows 1--7 in increasing ordinary
index; Faber diagonal 1; odd-delta entries zero; even-delta binomial
coefficients `(1/4)p`, `(1/2)p`, `(3/32)p^2`, `(3/4)p`, `(1/4)p^2`, `p`,
`(5/128)p^3`, `(15/32)p^2`, `(5/4)p` as in the compiled `Check`
identities. Absolute grade 13. Denominator convention: simple pole,
proper numerator degree `<2`.

V2--V5 are identifier-only. V6--V7 rewrite only the D1 evaluator. V8
splits r=1 from D1 and keeps `primdec.lib` only in r=1. V9--V12 copy r=1
byte-for-byte. Exact-Q r=1 SHA is frozen at V8 through V12 at
`e253681e155c0cbbc2c2984ecd6eeb7b5edfcb3e75b7b0c5649ec1051be7e5b3`.
V13 applies two textual repairs to that r=1 file only: `std` of the
radical, and insertion of the hand-remainder block. V14 moves that block
to after `poly R1_e1=...; poly R1_e0=...`. V15 invokes V14 unchanged.

V15 therefore freshly compiles the frozen V14 source. D1 scripts are still
emitted as a V12 freeze-chain byproduct and sit in the evidence tree;
they are not engine inputs, not hypotheses of the grade-thirteen
argument, and not consumed by the validator. The engine argv on both
hosts is `Singular -q .../square_r1_v14_{q|p65521}.sing`. Compiler
`result.json` records scope
`R1_GRADE13_ONLY_NO_D1_SQUARE_OR_ORDER2_VERDICT`. The quarantined
unbounded-D1 extrapolation is not used.

---

## 3. Question 2 — first nonpolynomial grade-thirteen contribution

**Verdict: holds.** Independently derived; the quarantined D1
extrapolation is not used.

Write

```text
f = K^2 + sigma^5 D,     K = L^2 + sigma^2 R,     D = L A + C,
L = z^2 + p/2.
```

The four charged source summands are `f^{3/2}`, `sigma^4 k10 f^{5/4}`,
`sigma^{12} k6 f^{3/4}`, and `sigma^{20} k2 f^{1/4}`, plus the four
target rows already named. Put `f = L^4 (1+ε)` with

```text
ε = 2 sigma^2 R/L^2 + sigma^4 R^2/L^4 + sigma^5 D/L^4.
```

The `R^3/L` piece of `sigma^4 k10 f^{5/4}` comes from the `ε^2` and `ε^3`
binomial terms of `(1+ε)^{5/4}`:

```text
α(α-1)/2 |_{α=5/4} · 4 = 5/8,          from (2 sigma^2 R/L^2)(sigma^4 R^2/L^4),
α(α-1)(α-2)/6 |_{α=5/4} · 8 = -5/16,   from (2 sigma^2 R/L^2)^3.
```

Sum `5/8 - 5/16 = 5/16`. Multiplying by `sigma^4 k10 L^5` yields

```text
(5/16) sigma^{10} k10 R^3 / L.
```

On the normalized chart `R = sigma R0` this is

```text
(5/16) sigma^{13} k10 R0^3 / L,
```

absolute grade thirteen. The compiled analytic generating function
contains this term as
`(5/16)*sigma^10*(k0)*(sigma*(b1+b0*t))^3*Inv1` with
`Inv1 = 1 - (p/2) t^2 + ...`, which is a unit at the simple pole
`t^2 = 2/p` and does not change the proper numerator modulo `L`.

Competing terms, with `A=sigma A0`, `C=sigma^3 C0`, `R=sigma R0`, and
unit leading `k10,k6,k2`:

| Contribution | sigma order | absolute grade |
|---|---|---|
| `(3/8) A^2` from `f^{3/2}` | `sigma^{12}` | 12, polynomial in `z`, dropped by `[_-]` |
| `(3/4) A C / L` | `sigma^{14}` | 14 |
| `(3/8) C^2 / L^2` | `sigma^{16}` | 16 |
| `R A^2` correction | `sigma^{15}` | 15 |
| `A^3 / L^3` | `sigma^{18}` | 18 |
| `(5/16) k10 R^3 / L` | `sigma^{13}` | **13** |
| `(5/8) k10 R C / L` | `sigma^{15}` | 15 |
| `(5/32) k10 R^2 A / L^2` | `sigma^{16}` | 16 |
| `(5/32) k10 A^2 / L` | `sigma^{16}` | 16 |
| first nonpolynomial `k6` (`R^2/L` in `f^{3/4}`) | `>= sigma^{16}` before `R=sigma R0`; `>= sigma^{18}` after | `>= 16` |
| first nonpolynomial `k2` (`R/L` in `f^{1/4}`) | `>= sigma^{22}` | `>= 22` |
| `mu2`, `mu4`, `mu6`, `J/4` targets | `28,32,36,38` | strictly larger |

No other first-normal term enters at grade 13. The truncated inverses
`Inv2=Inv3=1` in the r=1 analytic generating function are harmless at
this grade: those denominators multiply terms already above grade 13.
The compiled source rows independently forbid `k6`, `k2load`, `mu2`,
`mu4`, `mu6`, and `J` after `/sigma^{13}` and `subst(sigma,0)`. The
surviving proper part is exactly `(5/16) k10 R0^3 / L`.

---

## 4. Question 3 — Faber transform, recurrence, proper numerator

**Verdict: holds.** The seven source rows at grade 13 are the claimed
invertible lower-unitriangular Faber image of the first seven Laurent
coefficients. The recurrence and proper-numerator construction are
present in the compiled input and hold by hand.

Faber transform at frozen `p`, offset 0:

```text
g1 = h1
g2 = h2
g3 = (1/4) p h1 + h3
g4 = (1/2) p h2 + h4
g5 = (3/32) p^2 h1 + (3/4) p h3 + h5
g6 = (1/4) p^2 h2 + p h4 + h6
g7 = (5/128) p^3 h1 + (15/32) p^2 h3 + (5/4) p h5 + h7
```

This is lower unitriangular with unit diagonal, hence invertible over
`Z[1/2]`. Characteristic zero and `65521` both invert 2. The compiled
`R1_Check13_i` polynomials are exactly these identities, emitted from
`v1.transform_series` at offset 0, and compared against the extracted
source coefficients `R1_g13_i`. Seven vanished source rows therefore
vanish all seven Laurent coefficients.

The `L`-recurrence `h_{j+2} + (p/2) h_j = 0` for `j=1..5` is the
coefficient form of a unique degree-`<2` numerator of a simple pole
along `L`. The compiled checks are

```text
R1_h13_3+(p/2)*R1_h13_1 == 0
...
R1_h13_7+(p/2)*R1_h13_5 == 0.
```

The proper numerator is `R1_N = R1_h13_1*z + R1_h13_2`. The compiled
numerator identity is

```text
reduce(R1_N - (5/16)*k0*R1_R^3, std(ideal(L))) == 0
```

with `R1_R=b1*z+b0`. Thus `N` is the remainder of `(5/16) k0 R0^3`
modulo `L`. On `D(p*k10)` the prefactor `5/16 k0` is a unit (5 and 16
invertible in both registered characteristics), so vanishing of the
seven rows is equivalent to vanishing of that remainder. The printed
`R1_ROW_IDENTITIES_13=1`, `R1_DENOMINATOR_RECURRENCE=1`, and
`R1_NUMERATOR_IDENTITY=1` markers are the engine report of these
checks, not a substitute for them.

---

## 5. Question 4 — cubic remainder and common zeros

**Verdict: holds** over exact Q on `D(p*k10)`. Reduced support, not
scheme structure.

Reduce `R0^3` modulo `L=z^2+p/2` using `z^2 ≡ -p/2` and
`z^3 ≡ -(p/2) z`:

```text
(b1 z + b0)^3
  = b1^3 z^3 + 3 b1^2 b0 z^2 + 3 b1 b0^2 z + b0^3
  ≡ b1^3 (-p/2 z) + 3 b1^2 b0 (-p/2) + 3 b1 b0^2 z + b0^3
  = [3 b1 b0^2 - (p/2) b1^3] z + [b0^3 - (3p/2) b1^2 b0].
```

So the displayed coefficients are

```text
e1 = b1 ( 3 b0^2 - (p/2) b1^2 ),
e0 = b0 ( b0^2 - (3p/2) b1^2 ).
```

The compiled hand check is byte-for-byte this pair, compared after
`R1_e1=diff(R1_rem,z)` and `R1_e0=subst(R1_rem,z,0)`, and both fields
print `R1_REMAINDER_FORMULA=1`.

On `D(p*k10)` one has `p ≠ 0` and `k10 ≠ 0`. The system `e0=e1=0`
forces `b0=b1=0`:

- `b1=0` ⇒ `e0=b0^3=0` ⇒ `b0=0` in a domain;
- `b0=0` ⇒ `e1=-(p/2) b1^3=0`; `p≠0` and `2≠0` ⇒ `b1=0`;
- both nonzero ⇒ `3 b0^2 = (p/2) b1^2` and `b0^2 = (3p/2) b1^2`, hence
  `4 p b1^2 = 0`. On `D(p)` this is `4=0`, a contradiction in
  characteristic not 2.

Characteristic exclusions used: invertibility of 2 (for `p/2` in `L`
and in `e1,e0`) and of 5 and 16 (for the `5/16` prefactor). Both hold
in characteristic 0 and in `65521` (`65521` is an odd prime not
dividing 5). The `p/6` form of the same split additionally inverts 3,
which is likewise invertible here; the `4p=0` form does not need it.
No division by a vanishing chart coordinate occurs: `k10` and `p` are
inverted by the localization, not cancelled.

This is set-theoretic support of the linear `R0`. The raw ideal of
`(e0,e1)` may retain multiplicity; scheme structure is not claimed and
is firewalled. Reduced support of the localized radical is `(b0,b1)` in
those two coordinates.

---

## 6. Question 5 — actual Singular ideal

**Verdict: holds.**

Localization on `D(p*k10)` is represented by the chart equation
`inv*p*k0-1` inside

```text
R1_I = std(ideal(R1_e0, R1_e1, inv*p*k0-1)).
```

The ring variable `k0` is the V1 encoding of leading `k10`, so this is
the intended localization `D(p*k10)`, not a silent change of chart.
Then

```text
ideal R1_rad_raw = radical(R1_I);
ideal R1_rad     = std(R1_rad_raw);
```

so the radical is standardized before every `reduce`. The support test

```text
reduce(b0, R1_rad)==0 && reduce(b1, R1_rad)==0 && size(R1_rad[1])>0
```

is a Groebner-membership certificate that `b0` and `b1` lie in the
radical, together with a nonempty-first-generator guard against the
zero ideal. Combined with the hand remainder, it is a meaningful
reduced-support test in the `(b0,b1)` plane. It does not certify
scheme-theoretic structure.

The old warning `// ** R1_rad is no standard basis` is absent from both
fresh compiled inputs and from both stdout/stderr streams.

---

## 7. Question 6 — V13 and V14 as negative controls; V15 validator delta

**Verdict: holds.**

V13 correctly replaced `ideal R1_rad=radical(R1_I)` by
`std(radical(R1_I))`, and that is enough to remove the V12 warning. It
then inserted the hand-remainder block *before* `R1_e1` and `R1_e0`
were declared. Both V13 engines returned `rc=0` and printed

```text
   ? `R1_e1` is not defined
   ? error occurred in or before ... `int R1_hand_rem=(R1_e1-R1_e1_hand==0 && R1_e0-R1_e0_hand==0);`
```

The marker `R1_REMAINDER_FORMULA=1` is missing (`R1_REMAINDER_FORMULA=`
with empty value). Both V13 validators fail closed with
`FAIL_MISSING_OR_NONUNIQUE:R1_REMAINDER_FORMULA=1`. V13 is therefore a
negative control at the premature hand-check anchor, not a mathematical
refutation of the remainder identity.

V14 moves the hand block to immediately after the declarations. Its
stdout is byte-identical to V15's marker-only stdout
`fc6ba5c3ec390a8aebf2991920cf8e05c63f64b275e253d79d3222eeac135dff`,
with all twelve required markers once and no Singular diagnostic.
Engine `rc=0` on both hosts. Its validator still contains

```text
if [[ -s "$stderr" ]] || grep -Fq '=FAIL' "$stdout" || grep -Fq '// **' "$stdout" || grep -Eq '^[[:space:]]*\? ' "$stdout"
```

and therefore fails with `FAIL_SENTINEL_OR_DIAGNOSTIC` solely because
`ops/aws_exact_lane.sh` records benign `/usr/bin/time -v` telemetry on
stderr. V14 is preserved as a validator negative control; its
mathematical bytes are consumed only through the fresh V15 replay.

V15 pins and invokes the frozen V14 compiler without changing the
Singular input. The only source delta versus V14 `run_aws.sh` is the
validator: nonempty stderr is no longer fatal, while `=FAIL`, `// **`,
a leading Singular `?`, and `error occurred` are rejected in *either*
stream. Missing or duplicate markers, timeout (`rc=124`), and nonzero
engine return remain fatal. That is validator treatment of the
telemetry, plus a documented strengthening of diagnostic rejection;
the algebra is untouched.

---

## 8. Question 7 — meaning of `R0=0`

**Verdict: holds.**

The substitution was `R=sigma R0` with `R0` the declared leading linear
section of the normalized `r=1` receiver and `ord_sigma(R)=1`. Forcing
`R0=0` says this receiver has no arc with a nonzero order-one leading
section. Every such arc contact-raises `R` to order at least two.
Higher contact, or `R=0` identically, is a different face and must be
routed by the pinned closure criterion. The producer statement matches
that: no finite-order arc in this normalized receiver has a nonzero
leading `R0`. It is not an empty square-branch conclusion and says
nothing about the zero section. The closure criterion's demand to
invert declared leading units applies to units that are supposed to
stay nonzero; here the leading of `R` is the unknown being killed, so
it must not be inverted.

---

## 9. Question 8 — firewall

**Verdict: holds.**

A positive verdict licenses only arcwise/set-theoretic elimination of
the normalized `r=1` receiver on `D(p*k10)` after the frozen
first-normal, half-weight, and `M=0` gates. The producer firewall
states the same restriction and explicitly withholds V12's quarantined
unbounded `d=1` claim, `p=0`, `k10=0`, positive-order loads, the exact
zero section, terminal or Taylor conditions, fan exhaustiveness, scheme
structure, the whole square branch, order two, `(8,12)`, maximum
twelve, and JC2. Exact Q is the characteristic-zero producer; `F_65521`
is a software control. This review does not enlarge that license.

---

CONFIRMED

ORDER2_SQUARE_R1_V15_CONFIRMED
