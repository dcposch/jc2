# Hostile different-model review — GCD3 `(6,9)` target-translation erratum

| Field | Value |
|---|---|
| Claim under review | Frozen erratum: constant translation of the first target coordinate is a legal residual gauge on the aligned nontrivial-Kummer `(6,9)` chart; it acts by `a0 |-> a0+q`, `kappa |-> kappa-3q/2`; `kappa` is therefore not an essential modulus modulo that gauge; `I4,I3,I1` and `C=kappa^2+mu` are invariant; both reduced lower sheets and the aligned exclusion are unchanged |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none (in the erratum). The predecessor failure is not an identity: it is the untested phrase “the only essential constant is `kappa=c_3`” / “five moving coefficients plus essential `kappa`”, which is pin-dependent |
| Cleanest canonical repair | keep this immutable erratum; do not rewrite frozen producer or first-review bytes; subsequent promotion language must say that `kappa` is a coordinate of a first-target-constant pin, and that modulo the residual degree-preserving constant target affine group the aligned high rows have five moving coefficients and no essential constant |
| Evidence tier | independent integration of the eight high source rows (no imported `g0`); hand cancellation of the `a0`/`kappa` linear parts of `I4,I3,I1`; simultaneous substitution and Taylor expansion of `I2` and `C`; reconstruction of both reduced sheets, including the `lambda`-bracket `567 lambda^6`; unmodified registered replay as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the erratum producer (OpenAI Codex, GPT-5 family). Same reviewer as the first common-cubic review whose Claim 2 language this note supersedes; the purpose is correction, not inertia |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T14:33:17Z – 2026-08-24T14:40:00Z |
| Python | uv-pinned CPython 3.11.11 + SymPy `1.14.0` (registered replay and independent reconstruction) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Erratum, freeze, first common-cubic producer, first Grok review, and lower-Pfaffian successor reread in full before any verdict. Do not defer to producer assertions or to the first review.

- `xmodel/gcd3-69-target-translation-erratum-20260824.md` (SHA-256 `43fa36968bb90414748330c1b4a5d5169a0eaa21b1925623764e96204e049c78`)
- `cases/gcd3_69_target_translation_erratum_20260824/MANIFEST.sha256` (SHA-256 `a00ff5c38a76a033d0b5688bb98052db75ea4a44aa307a657c4d2bba9a1d9529`)
- `cases/gcd3_69_target_translation_erratum_20260824/FREEZE.sha256` (SHA-256 `4c3f7cb0d0c9bdc45423308a18d50aea5aaef54839c55fd1397b7a31ced21934`)
- `xmodel/gcd3-69-common-cubic-first-gate-20260824.md` (SHA-256 `f63bf74fd1013c74645f9f7fe9292db69199572b390b5b19d160c5ed13b373e8`)
- `xmodel/gcd3-69-common-cubic-first-gate-review-grok-20260824.md` (SHA-256 `5416440bc12bb50ecebfdfa520082aa9e88a26069b43deb13bdaabfcd1690503`)
- `xmodel/gcd3-69-lower-pfaffian-successor-20260824.md` (SHA-256 `7671785519bf4e55b602f117740bd8d8571c6982a8916235407a2bb0a2263043`)

The committed basis is exactly `1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a`. Named erratum, successor, and case artifacts remain uncommitted on top of that basis. No producer, case, canonical, ladder, notes, prompt, log, or run file was edited. Independent reconstruction lived only in `/tmp`.

The first review did not test constant translation of the **first** target coordinate. That omission is the entire reason this note exists. The first review’s Jacobian identities, Kummer descent, shear, second-coordinate translation, and form `g=g0+kappa K` are not re-voted by inertia; they are reused only after the eight high rows were integrated again here.

---

## Promotion

**Accept the `SCOPED-CORRECTION`.** Under the exact frozen aligned `(6,9)` hypotheses, `(f,g)|->(f+q,g)` with `q in k` is a legal Jacobian-1 target automorphism. It is not forbidden by any target-origin, boundary-value, integral, Kummer, monicity, or degree pin. In the normalized coefficient chart it acts by

```text
a0 |-> a0+q,             kappa |-> kappa-3q/2,
```

and `q=2kappa/3` gauges `kappa` to zero. After a chosen pin of the first target constant, `kappa` remains a bookkeeping coordinate. Modulo the residual degree-preserving constant target affine group, the aligned high rows have no essential constant.

The four lower integrals transform exactly as claimed. `C=kappa^2+mu` is a genuine invariant, as are the elliptic curve `Y^2=3X^3+4096C` and its terminal one-form. Both reduced sheets are covariant. On `C=0`, the shifted Davenport–Stothers path is the ordinary DS path in a translated target chart; the terminal ODE and the nontrivial-Kummer valuation contradiction are unchanged.

**Do not rewrite** the frozen first-gate or first-review bytes. **Do not retract** the aligned two-sheet exclusion. **Do not promote** this to a cube-mismatch obstruction, a full `(6,9)` theorem, or JC2.

**Smallest valid successor language.** Replace “five moving coefficients plus essential `kappa`” by one of the two equivalent pinned statements, and never mix them: either five moving `a_i` after gauging `kappa=0`, or five moving `a_i` plus bookkeeping `kappa` after an explicit first-target-constant pin. Express any later cube-mismatch constants in target-translation-invariant combinations before promotion.

---

## Quarantine

The predecessor phrases “the only essential constant is `kappa=c_3`” and “high source rows reduce to five moving coefficients plus essential `kappa`” are quarantined as gauge-invariant statements. They remain valid only as descriptions of a slice on which the first target constant has been pinned. Successor §3’s sentence “the `kappa K` term is the essential high-row integration constant” is the same language error and is likewise quarantined as language, not as an identity. No result here proves or disproves JC2, closes cube mismatch, or excludes arbitrary degree-`(6,9)` pairs. PASS strings are regression markers.

---

## Scope (not enlarged)

Gauge covariance of the aligned nontrivial-Kummer normal form, the four lower first integrals, the invariant `C`, and the two reduced sheets of the lower-Pfaffian successor. Cube-core mismatch `delta != 0`, arbitrary `(6,9)`, polynomiality of `z=sy+r`, and JC2 remain out of scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | `(f,g)|->(f+q,g)`, `q in k`, is a legal target automorphism under the exact frozen aligned `(6,9)` hypotheses. No target-origin, boundary-value, integral, Kummer, monicity, or degree pin forbids it. Preferring a normalized target value is not a prohibition | **CONFIRMED** | an explicit pin `a0` constant, `P(x,0)` numerical, or `f` monic-and-traceless; a hypothesis that the pair vanish at a source origin in a way that consumes this one-parameter group; a Kummer weight that forbids weight-zero translation of `f` |
| 2 | High-row chart action `a0_new=a0+q`, `kappa_new=kappa-3q/2`; identity `g0(a0+q)+(kappa-3q/2)K=g0(a0)+kappa K`; `q=2kappa/3` proves `kappa` is not an essential modulus modulo the residual (in particular, the full legal) target affine group | **CONFIRMED** | `g0(a0+q)-g0(a0)` not equal to `(3q/2)K`; opposite sign on `kappa_new`; `q=2kappa/3` reintroducing a `z^5` or `z^8` term, or failing to keep `g` |
| 3 | Independently reconstructed `I4,I3,I1` invariant; `I2_new-I2=3 kappa q-9q^2/4`; `C=kappa^2+mu` invariant. Signs checked by simultaneous substitution | **CONFIRMED** | opposite sign on the `I2` shift; `C_new-C` a nonzero remainder; sequential-only substitution that dropped the `a0 kappa` cross term |
| 4 | `d_new=d+q` and `kappa+3d/2` invariant on the zero-bracket sheet. On `C=0`, `q=2kappa/3` sends `f_lambda-2kappa/3` to `f_lambda`, leaves `g_lambda` and all `z`/`lambda` derivatives unchanged, and leaves the terminal ODE and nontrivial-Kummer valuation contradiction unchanged | **CONFIRMED** | `w=4a0-a3^2` not shifting by `4q`; a `kappa`-dependence in `g_lambda`; the `lambda`-bracket changing by a derivative of the constant `-2kappa/3` |
| 5 | “Essential `kappa`” and the modulo-gauge variable count were wrong or pin-dependent. No identity, invariant-fiber decomposition, or aligned-branch exclusion is invalidated: the successor treats every `kappa` and is controlled by invariant `C`. Cube mismatch, arbitrary `(6,9)`, and JC2 remain open | **CONFIRMED** | a reduced prime or terminal identity that used a non-invariant combination in an essential way; an exclusion that failed after `kappa |-> 0`; a hidden cube-mismatch or JC2 inference |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Replay and hashes

Frozen hashes, recomputed on the charged tree, match the launch prompt, `MANIFEST.sha256`, and `FREEZE.sha256`:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/gcd3-69-target-translation-erratum-20260824.md` | `43fa36968bb90414748330c1b4a5d5169a0eaa21b1925623764e96204e049c78` | prompt, `MANIFEST`, `FREEZE` |
| `cases/gcd3_69_target_translation_erratum_20260824/MANIFEST.sha256` | `a00ff5c38a76a033d0b5688bb98052db75ea4a44aa307a657c4d2bba9a1d9529` | prompt (self-hash), `FREEZE` |
| `cases/gcd3_69_target_translation_erratum_20260824/FREEZE.sha256` | `4c3f7cb0d0c9bdc45423308a18d50aea5aaef54839c55fd1397b7a31ced21934` | prompt (self-hash) |
| `cases/gcd3_69_target_translation_erratum_20260824/REGISTRATION.md` | `5687238a1d6d2ff40d55134ca9885e2b1a063c646b66079669a23d90dc6bce79` | `MANIFEST`, `FREEZE` |
| `cases/gcd3_69_target_translation_erratum_20260824/check.py` | `e4b3dffea984436ae0affd61b978053455e7d992b41a6c7816644c7d89d0ed67` | `MANIFEST`, `FREEZE` |
| `xmodel/gcd3-69-common-cubic-first-gate-20260824.md` | `f63bf74fd1013c74645f9f7fe9292db69199572b390b5b19d160c5ed13b373e8` | registration |
| `xmodel/gcd3-69-common-cubic-first-gate-review-grok-20260824.md` | `5416440bc12bb50ecebfdfa520082aa9e88a26069b43deb13bdaabfcd1690503` | registration |
| `xmodel/gcd3-69-lower-pfaffian-successor-20260824.md` | `7671785519bf4e55b602f117740bd8d8571c6982a8916235407a2bb0a2263043` | registration |

The case directory contains exactly those four files. No enumerator, exponent rectangle, or AWS helper is present.

Registered command, rerun unmodified from the repository root:

```sh
uv run --offline --no-project --with sympy==1.14.0 python \
  cases/gcd3_69_target_translation_erratum_20260824/check.py
```

Exit 0. Exact output:

```text
PASS-GCD3-69-TARGET-TRANSLATION-ERRATUM
kappa=PINNED-NORMALIZATION-COORDINATE-NOT-GLOBAL-MODULUS
C=kappa^2+mu=TARGET-TRANSLATION-INVARIANT
aligned_lower_exclusion=UNCHANGED
cube_mismatch=OPEN
jc2_inference=false
```

Those PASS strings are regression only. The independent reconstruction of Claims 1–5 is the evidence. In particular the registered script hardcodes the eight `b`-rows rather than re-solving them; the high-row integration below does not import that table.

---

## Claim 1 — legality of `(f,g)|->(f+q,g)`

**CONFIRMED.**

Post-composition with the target automorphism `(u,v)|->(u+q,v)`, `q in k`, has Jacobian `1`. If `J(f,g)=j in k^*`, then `J(f+q,g)=j`. Actual `z`-degrees remain `(6,9)`: the leading terms are `z^6` and `z^9`, and adding a constant cannot cancel them. Monicity in `z` is likewise untouched. The Kummer datum `a_6=h^2`, `b_9=h^3` lives in the leading coefficients, so the extension `L=k(x)(s)`, `s^3=h`, is unchanged. Weight of a constant `q` is `0`, matching `wt(a0)=wt(kappa)=0`. Boundary values shift as `P(x,0) |-> P(x,0)+q` and `Q(x,0) |-> Q(x,0)`, remaining polynomial. Depression `z=sy+r` is a source-coefficient identity and is not moved.

Search of the frozen first gate for a pin that would consume this one-parameter group:

- **Target origin.** Section 5 records that the two constant-`W` primes meet at the coefficient origin `a0=...=a4=0`. That is a point of coefficient space, not a normalization `f |-> f-f(0)` of the first target coordinate.
- **Boundary value.** Provenance `(1.6)` states that `P(x,0)=f(r)` and `Q(x,0)=g(r)` are polynomial and need not vanish. Adding `q` preserves that statement. A hypothetical JC2 convention that the pair vanish at a single source point would pin one number, not the function `a0(x)`, and is not among the frozen hypotheses.
- **Integral.** The eight high rows produce eight constants. Kummer kills `c7,c5,c4,c2,c1`. The replay of the first gate then uses the shear `g |-> g-c6 f` and the *second*-coordinate translation `g |-> g-c0`. Those are two of the three residual constant target gauges compatible with degrees `(6,9)` (see Claim 2). The first-coordinate translation is never used and never forbidden.
- **Kummer.** Weight-zero constants are exactly `{c0,c3,c6}`. Translation of `f` is weight-zero and is not killed by descent.
- **Monicity / degree.** Leading coefficients and actual degrees are already pinned; neither constraint involves the constant term of `f`. Residual source translations of `z` would reintroduce a `z^5` term and are not available to kill `a0`.

Preferring to keep `kappa` visible as a bookkeeping constant is a slice choice, not a prohibition. No frozen hypothesis pins the numerical value of the first target coordinate. The map is legal.

No identity failed.

---

## Claim 2 — high-row chart action and inessential `kappa`

**CONFIRMED.**

The eight high source rows of `D=f_x g_z-f_z g_x` were integrated independently, with a free constant `c_j` in each `b_j`. After Kummer descent `c7=c5=c4=c2=c1=0` one has the identity, rechecked here,

```text
g = g0(a) + c6 f + c3 K + c0,
K = z^3+(a4/2)z+a3/2,
```

with `g0` the zero-constant solution. The shear removes `c6`; second-coordinate translation removes `c0`. The remaining slice is `g=g0(a)+kappa K` with `kappa=c3`.

The only `a0`-dependence in `g0` is linear:

```text
[z^3] g0 = 3 a0/2 + (...),
[z^1] g0 = 3 a0 a4/4 + (...),
[z^0] g0 = 3 a0 a3/4 + (...).
```

Hence

```text
g0(a0+q)-g0(a0)
  = (3q/2) z^3 + (3q/4) a4 z + (3q/4) a3
  = (3q/2) K.
```

Rearrangement is identity (2):

```text
g0(a0+q) + (kappa-3q/2) K = g0(a0) + kappa K.
```

The same pair `(f,g)` is therefore represented in the translated chart by `a0_new=a0+q` and `kappa_new=kappa-3q/2`. Direct simultaneous substitution of that rule into `g` leaves `g` invariant; `f` shifts by `q`. High rows remain zero because derivatives do not see `q`. Setting `q=2kappa/3` gives `kappa_new=0` and

```text
g0(a0+2kappa/3) = g0(a0)+kappa K,
```

so the pair is represented with vanishing `kappa`. (Sequential substitution that sends `kappa |-> 0` *inside* `q=2kappa/3` before shifting `a0` is not the geometric action and incorrectly erases the shift. Simultaneous substitution, or a frozen old value of `kappa`, is required. The registered replay uses `simultaneous=True`.)

The residual affine automorphisms of the target that preserve Jacobian `1`, actual degrees `(6,9)`, and the already-used leading-power/monicity pin are exactly: shears `g |-> g+c f` (used), translations of `g` (used), and translations of `f` (omitted). Mixing `g` into `f` raises degree. Residual scalings are already spent on `a6=h^2`, `b9=h^3`. Thus `q=2kappa/3` is a legal element of the residual — and a fortiori of the full — target affine group, and it gauges `kappa` to zero. `kappa` is not an essential modulus. It is a coordinate of the pinned first-target-constant slice.

The erratum’s phrase “modulo the full affine target gauge” is slightly loose if read as including degree-destroying maps, but those maps are already excluded by the frozen degree pin, and the killing map is a translation. The mathematical conclusion does not depend on the extra maps.

No identity failed.

---

## Claim 3 — four lower integrals and `C`

**CONFIRMED.**

From the undifferentiated pair `f`, `g=g0+kappa K`, the coefficient one-forms `alpha_r=[z^r]D` in `(da0,...,da4)` were rebuilt and the four triangular corrections of successor `(3)` were reintegrated. Mixed partials vanish and the potentials differentiate back to the one-forms. The resulting potentials match the successor closed forms

```text
I4=9 e4/128 + 3 kappa A/4,     I3=9 e3/128 + 3 kappa B/2,
I2=N2/512,                     I1=-N1/128,
```

identically, so covariance may be read either from the potentials or from those formulas.

Simultaneous substitution `(a0,kappa)|->(a0+q, kappa-3q/2)`:

- `e4` is linear in `a0` with slope `16 A`. The `I4` shift `9/128 * 16 A q` cancels `3(-3q/2)A/4`. `I4` is invariant.
- `e3` is linear in `a0` with slope `32 B`. The `I3` shift `9/128 * 32 B q` cancels `3(-3q/2)B/2`. `I3` is invariant.
- Writing `T=a1 a4+2 a2 a3-a3 a4^2`, one has `d N1/da0=96 T` and `d N1/dkappa=64 T`, so `96 T q + 64 T(-3q/2)=0`. `I1` is invariant.
- `I2` is quadratic in `(a0,kappa)` with `d^2 I2/da0^2=9/2`, `d^2 I2/da0 dkappa=3`, `d^2 I2/dkappa^2=0`. The Taylor remainder at `(q,-3q/2)` collapses to `3 kappa q-9q^2/4` after the `a`-dependent linear terms cancel in the same way as for `I4,I3,I1`. Thus

```text
I2_new - I2 = 3 kappa q - 9 q^2/4.
```

The sign is the one written, not the opposite. Both sequential polynomial substitution orders agree with the simultaneous rule for this polynomial; a computer-algebra substitution that reduced `kappa` inside `q` would not.

Consequently `mu_new=mu+3 kappa q-9q^2/4` on the invariant fiber `I2=mu`, and

```text
C_new
  = (kappa-3q/2)^2 + mu + 3 kappa q - 9q^2/4
  = kappa^2 + mu
  = C.
```

`C` is a target-translation invariant. So are `X=8a2-2a4^2` and `Y=3 a4 X`, which do not depend on `a0` or `kappa`. The curve `Y^2=3X^3+4096 C` and the terminal one-form pulled back to that curve are therefore genuine invariants, not chart artifacts.

No identity failed.

---

## Claim 4 — both reduced sheets

**CONFIRMED.**

**Zero-bracket sheet.** `w=4a0-a3^2` shifts by `4q`, so `d=w/4` obeys `d_new=d+q`. Then

```text
kappa_new + 3(d+q)/2
  = (kappa-3q/2) + 3d/2 + 3q/2
  = kappa + 3d/2.
```

On the successor parameterization `f=K^2+d`, `g=K^3+(kappa+3d/2)K`, translation of `f` is absorbed into `d` and the coefficient of `K` in `g` is invariant. Direct differentiation with moving `K` and constant `(d,kappa)` still gives `D=0`; the extra constant `q` cannot create a terminal row. The PA equation `9w^2+48 kappa w-64 mu` is itself invariant under the simultaneous rule, as is the embedded generator `12a0-3a3^2+8 kappa` of `PE`. On this sheet `C=(kappa+3d/2)^2`, the square of the physical coefficient of `K`.

The first gate’s common-component slice `d=0`, `g=K^3+kappa K` is gauge-equivalent to `kappa=0`, `d=2kappa/3`, `f=K^2+2kappa/3`. Distinguishing “high-row `kappa`” from “lower-row `d`” is pin-dependent bookkeeping; the successor already showed that the whole reduced sheet has vanishing bracket, so the exclusion does not depend on the pin.

**`C=0` sheet.** The PB relation `a0=a2 a4/4-a4^3/16-2kappa/3` is covariant: the right-hand side shifts by `q` when `kappa |-> kappa-3q/2`. Restricting to the successor coordinates `a4=4lambda`, `a3=a1=0`, `a2=10 lambda^2` and substituting the independently reconstructed `g0+kappa K` yields exactly

```text
f = f_lambda - 2kappa/3,         g = g_lambda,
```

with the displayed `f_lambda`, `g_lambda`. Choosing `q=2kappa/3` cancels the constant in `f` and sets `kappa_new=0`, so the pair becomes `(f_lambda, g_lambda)`. The polynomial `g_lambda` does not depend on `kappa`. The constant `-2kappa/3` has vanishing `z` and `lambda` derivatives, and an independent expansion gives

```text
(f_lambda)_lambda (g_lambda)_z - (f_lambda)_z (g_lambda)_lambda
  = 567 lambda^6
```

whether or not the constant is present. The five-row determinant identity and the terminal equation `567 s lambda^6 lambda'=j` are therefore the same as on the unshifted DS path. Descent `lambda=s^2 q` and the predecessor’s finite-place/infinity classification, already reviewed, are identities in `(h,q,j)` and do not see the target translation. The nontrivial-Kummer valuation contradiction is unchanged. The “shifted DS” path is the ordinary DS path in a translated target chart.

No identity failed.

---

## Claim 5 — impact on the trust record

**CONFIRMED.**  The candidate verdict stands. No step of Claims 1–4 failed, so there is nothing to refute.

**What was wrong.** First-gate §1.1 and §8, the first-gate replay comment, and first-review Claim 2 all call `kappa=c_3` the only *essential* high-row constant after “constant target gauges.” Those gauges were the shear and the second-coordinate translation. The first-coordinate translation was not tested. The eight-row identities, the list of weight-zero constants `{c0,c3,c6}`, the form `g=g0+kappa K`, and the vanishing bracket on `f=K^2`, `g=K^3+kappa K` remain correct on that pinned slice. The word “essential” and the gauge-invariant reading of the count “five moving coefficients plus `kappa`” do not. After the omitted gauge the aligned high-row count is five moving coefficients and zero essential constants. Equivalently, `kappa` is retained if and only if the first target constant is pinned.

First-review Claims 1 and 3–8 are not superseded. First-review Claim 2 is superseded only in the essential/`5+1` language identified above.

**What is not invalidated.** The successor integrates the four lower rows for arbitrary `kappa`, decomposes the invariant fiber over `Q[a0,...,a4,kappa,mu]`, and reduces the elliptic sheet by the invariant `C`. PA is excluded by `D=0` for every `(d,kappa)`. PB is excluded by a terminal form that depends on `(X,Y,C)`, all invariant. The `C=0` DS calculation uses the constant `-2kappa/3` only through derivatives that vanish, and after `q=2kappa/3` it is the already-reviewed ordinary DS ODE. Quotienting the redundant translation simplifies the proof; it does not change the exclusion. Successor §3’s “essential” is the same language error and does not enter the identities.

**What remains open.** Cube-mismatch `delta != 0` has additional weight-unforced high-row constants; the translation action on that branch is not computed here and must be written in invariant combinations before any promotion. Arbitrary degree-`(6,9)` pairs outside the frozen aligned normal form, polynomiality of `z=sy+r`, and JC2 are untouched. The erratum infers none of these.

No identity failed. No exclusion is retracted.

---

## Non-blocking remarks

1. The registered `check.py` hardcodes the eight `b`-rows of `g0` rather than re-integrating the high source rows, and it checks the `C=0` cancellation `-2kappa/3+q=0` without reconstructing `f_lambda`, `g_lambda`, or the `lambda`-bracket. Those are replay-coverage gaps, not mathematical gaps. Both reconstructions were done independently above and match.
2. “Full affine target gauge” should be read as the residual Jacobian-1 affine group preserving the frozen degree and monicity pins. The killing map is already a translation, so the inessentiality of `kappa` does not rely on degree-destroying affine maps.
3. On PA, `kappa` and `d` are not independently essential even as lower-row constants: only the invariant `kappa+3d/2` (equivalently `C`, which is its square) is. The successor’s decision to keep the three notions distinct is valid pinned-chart bookkeeping and is not an identity error.
4. Characteristic zero is used to invert `2` and `3` in `kappa_new=kappa-3q/2` and `q=2kappa/3`. That is among the frozen field hypotheses.

---

## Promotion (restated)

**Accept the `SCOPED-CORRECTION`.** `kappa` is not an essential modulus modulo legal constant translation of the first target coordinate. After an explicit first-target-constant pin it remains a bookkeeping coordinate. The four lower integrals, the invariant `C`, both reduced sheets, and the aligned two-sheet exclusion stand.

**Do not promote this to** a rewrite of frozen producer or first-review bytes; a retraction of the aligned exclusion; a cube-mismatch obstruction; a full `(6,9)` theorem; or JC2.

**Smallest valid successor language:** five moving `a_i` after `kappa=0`, or five moving `a_i` plus bookkeeping `kappa` after a declared first-target-constant pin. Cube-mismatch constants must be written in target-translation-invariant combinations before promotion.

---

## Quarantine (restated)

No result here proves or disproves JC2. PASS strings are regression markers. “Essential `kappa`” and the gauge-invariant `5+1` high-row count are quarantined. Independent reconstruction, not the producer script, is the evidence for every numbered claim.

---

## Smallest failing identity and cleanest canonical repair (restated)

**Smallest failing identity:** none in the erratum. The predecessor error is the untested gauge-language claim that `kappa` is essential and that the modulo-gauge high-row count is five plus `kappa`.

**Cleanest canonical repair:** this immutable erratum, with subsequent promotion language corrected as above, and with frozen producer and first-review bytes left untouched.
