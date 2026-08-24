# Hostile different-model review — AS109 carry erratum

| Field | Value |
|---|---|
| Claim under review | Carry erratum to the frozen AS109 specification gate: base-109 digit carry in the truncated two-layer determinant; five-slot countercontrol; survival of `NO-FROZEN-GRAMMAR` on the integrally zero-carry triangular family; Hensel and `CLOSED-SUPPORT + UNIT-L` independent of digit bookkeeping |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Evidence tier | independent exact arithmetic over `Z` (hand expansion of `det J` modulo `109^3`; closed-form five-slot Jacobian; a second sparse engine that does not import the registered replay) plus unmodified rerun of `verify_carry_erratum.py` |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the erratum producer (OpenAI Codex, GPT-5 family). Same reviewer as the original claim 2 that this note supersedes; the purpose is correction, not inertia |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `c17bd2542b40f3178ec619ae4a73501550555336` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T08:55:54Z – 2026-08-24T09:18:00Z |
| Python | 3.14.6; stdlib only (`math.comb`, integer dicts) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and prior-review inputs reread in full before any verdict:

- `xmodel/as109-support-gate-20260824.md` (SHA-256 `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5`)
- `xmodel/as109-support-review-grok-20260824.md` (SHA-256 `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8`)
- `xmodel/as109-support-gate-20260824-erratum.md` (SHA-256 `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb`)
- `cases/as109_support_20260824/verify_carry_erratum.py` (SHA-256 `cde7f3d467b492c0d914511b7fa609c916e40a33e6ca6c741af9be79a99d53f0`)

The committed basis is exactly `c17bd2542b40f3178ec619ae4a73501550555336`. All named producer artifacts remain uncommitted on top of that basis. No producer, review, replay, canonical, ledger, or case file was edited. No grammar was invented, no cap was widened, and no exponent rectangle was enumerated.

This follow-up attacks the seven numbered erratum claims. It does not re-vote the original eight-claim table by inertia. Original claim 2 is the only original numbered claim that is superseded, and only in the part identified in §7 below.

---

## Promotion

**Accept the `SCOPED-CORRECTION`.** Original review claim 2 remains correct as an expansion of `det J-1`, as a monomial-bracket formula, and as a definition of `N`. It is not correct as the assertion that the two displayed equations `E1` and `E2` over `F_109` are by themselves the exact condition modulo `109^3`. That assertion is replaced by the carry-aware pair `(2.1)--(2.2)` of the erratum, or by the already-packed exact `Z_109` identity of gate §5.1.

**Keep `NO-FROZEN-GRAMMAR` as the registered stop, at this scope only.** The obstruction family has vanishing first-layer carry over `Z`. Successor transport, unbounded literal exponents, and the absence of a finite exhaustive gauge normal form are unchanged.

**Keep the Hensel nonautomorphy lemma and `CLOSED-SUPPORT + UNIT-L` as conditional resurrection targets. Promote neither to existence.**

Do **not** promote this record to any of: nonexistence of a cap-eight lift; `HEIGHT-CERT`; `NO-CYCLE-AT-8`; `SUPPORT-ONLY`; `FEASIBLE-CYCLE`; a found lift; a characteristic-zero counterexample; a statement that the original review as a whole is withdrawn. Do not answer it by widening eight, by sampling exponents, or by writing a motif compiler.

## Quarantine

Generic uncarried `E2` and layerwise marked-section tests over `F_109` in the producer, preregistration, manifest, and original review are quarantined unless either the carry-aware equations are used or the relevant first-layer polynomial is already `0` over `Z`, not merely modulo 109. No result here proves or disproves JC2. The five-slot map is a countercontrol to a digit test, not a Keller candidate and not an enumeration result.

---

## Scope (not enlarged)

One prime `p=109`, one seed `(x-x^{109},y)` over `F_{109}`, two marked source sections `(0,0)` and `(1,0)`, at most eight distinct correction slots counted across layers once, and the first nonlinear successor only. Literal exponents range over all of `N^2`. No rectangle, total-degree bound, second seed, AWS, cap widening, or modular-to-characteristic-zero inference is in scope. Characteristic-zero language below remains purely conditional on an exact integral polynomial lift that this run did not produce.

Write `L(A,B)=A_x+B_y` and `s=x^{108}`.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Over `Z[x,y]`, `det J(P,Q)-1 = p C_1 + p^2(L(A_1,B_1)+N_0)` modulo `p^3`, with `C_1=L(A_0,B_0)-s` and `N_0=(A_{0x}-s)B_{0y}-A_{0y}B_{0x}`; after `C_1=0 mod p` one has `K=C_1/p` and corrected `E2` is `K+L(A_1,B_1)+N_0=0 mod p` | **CONFIRMED** | a leftover `p^2` term not in `K+L_1+N_0`; opposite sign on `K` or on the `-A_{0y}B_{0x}` summand; `C_1` not `L-s` |
| 2 | Marked collision modulo `p^3` is `Delta A_0=0 mod p` and `Delta A_0/p + Delta A_1=0 mod p` (and the same for `B`); separate layerwise vanishings over `F_p` do not generically control the carry; integral vanishing at each layer is sufficient | **CONFIRMED** | `Delta(x-x^p)≠0`; `Delta P` not equal to `p Delta A_0 + p^2 Delta A_1`; a counterexample with `Delta A_0=p` and `Delta A_1=0` still giving `Delta P=0 mod p^3` |
| 3 | The five-slot map `A_0=x^{109}-x`, `B_0=(1+x^{108})y`, `A_1=0`, `B_1=(1+2x^{108}+x^{216})y` passes frozen uncarried `E1` and `E2` over `F_{109}`, has exact marked differences zero, and satisfies `det J-1 = 109^2 x^{108} mod 109^3` | **CONFIRMED** | `C_1` not `p s`; uncarried `L_1+N_0` not `0 mod p`; closed-form Jacobian not `1+p^2 s` modulo `p^3`; slot count not five |
| 4 | For every integer `m>=1`, the family `A_0=y^m`, `B_0=x^{108}y` and the transported successor have `C_1=0`, `L(A_1,B_1)+N_0=0`, and marked differences `0` over `Z`; the unbounded-gauge / no-finite-literal-grammar stop survives | **CONFIRMED** | `C_1≠0` over `Z` for some `m>=1`; binomial composition disagreeing with `(4.2)` modulo `p^3`; a same-slot overlap; the erratum promoting the stop to nonexistence of cap-eight lifts |
| 5 | The Hensel nonautomorphy lemma assumes an already exact `Z_{109}` polynomial map with `det J=1` and is independent of truncated digit carries | **CONFIRMED** | the lemma using `E1`/`E2` residue digits in place of `det J_F=1`; a hidden dependence on marked-section carries |
| 6 | `CLOSED-SUPPORT + UNIT-L` uses the packed exact identity `det J(x-x^p+pA, y+pB)-1 = p(L(A,B)-s+p N(A,B))` over `Z_{109}` and is unaffected; it remains wholly conditional | **CONFIRMED** | a `p^3` remainder in the packed `2×2` determinant; the criterion asserting a closed module was found |
| 7 | No enumeration ran, no lift was found, and no JC2 inference is available. Original review claim 2 is superseded only in the inference from the truncated expansion to uncarried `E1`/`E2` over `F_{109}` as the exact condition modulo `109^3`. Original claims 1 and 3–8 are not superseded | **CONFIRMED** | a transition enumerator in the case tree; an inferred existence or nonexistence statement; the erratum withdrawing the bracket formula, the packed identity, or the grammar stop |

All remarks below are non-blocking unless marked otherwise. None changes a coefficient, a slot count, or a verdict.

---

## Replay and hashes

Registered command, rerun unmodified from the charged tree:

```sh
python3 cases/as109_support_20260824/verify_carry_erratum.py
```

Exit code 0. Top-level fields:

```text
verdict = PASS-CARRY-ERRATUM
generic_E2_without_carry = QUARANTINED
no_enumeration_run = true
existence_inference = false
```

Five-slot control fields: `frozen_E1_mod_109 = PASS`, `frozen_uncarried_E2_mod_109 = PASS`, `marked_collision_over_Z = PASS`, `carry_K = x^108`, `corrected_E2_residual_mod_109 = x^108`, `determinant_minus_one_mod_109_cubed = 109^2*x^108`, `slot_count = 5`. Parametric sample `m=1,2,108,109,110,1000`: each reports `C1_over_Z = 0`, `carry_K = 0`, `L1_plus_N_over_Z = 0`, `marked_collision_over_Z = PASS`.

Recomputed SHA-256 (all match the erratum table and the launch prompt):

| Artifact | SHA-256 |
|---|---|
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` |
| `xmodel/as109-support-review-grok-20260824.md` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` |
| `cases/as109_support_20260824/PREREGISTRATION.md` | `be9138a90b661f069197a4c22235ee1caa4e03fcecd2dab8c980e8934f2d6301` |
| `cases/as109_support_20260824/manifest.json` | `c69d70805bdba5793f385fca9c289f9a12a8c58c45e1625e1c2f69a9632f0364` |
| `cases/as109_support_20260824/FREEZE.sha256` | `0a535ca2877ec3672044faa5c5f20878c4b95adddf4087b89f772d030d6e140e` |
| `cases/as109_support_20260824/verify_spec_obstruction.py` | `1bb8f86596b75bd43e467dc84b569e8fb2bb2744c198c40f5244f0b054634165` |
| `cases/as109_support_20260824/spec_obstruction.json` | `b95ad244da3ea75100c61143dc9c0026ac567c8acfc2398a86ce1623a101131e` |
| `cases/as109_support_20260824/verify_carry_erratum.py` | `cde7f3d467b492c0d914511b7fa609c916e40a33e6ca6c741af9be79a99d53f0` |

The registered program imports no producer replay. It recomputes the frozen original hashes, then checks the five-slot determinant over integer sparse polynomials, the corrected second residual, the parametric zero-carry identities at six exponents, and the two closed-support `N`-probes. It is not a transition enumerator and does not search for a lift.

A second engine, written for this review and not imported from that script, used integer sparse polynomials and binomial expansion. It recorded zero failures on: the generic identity `(2.1)` on forty random supports and four structured supports; the monomial bracket and `N=[A,B]-s B_y` on a spread of exponents including `(109,0; 0,1)`; corrected `E2` whenever `C_1` is `p`-divisible; the five-slot closed form and Jacobian; the evaluation identity `(2.3)` on twenty-five random polynomials plus an explicit collision-carry control `A_0=109 x`; the parametric family at fifteen exponents `m=1,2,3,4,5,17,107,108,109,110,216,217,218,324,1000`; binomial composition `F_{\mathrm{can}}∘G_m` modulo `109^3` at seven of those; the packed exact identity on twenty-five random `(A,B)` with no modulus; `G_m` determinant one; and the two closure probes.

Process remark, non-blocking: the registered replay is a control suite, not a generic symbolic checker of `(2.1)` or `(2.3)`. Those identities are polynomial and were expanded by hand and on random supports in the second engine.

---

## Independent recomputation

### 1. Carry-aware determinant; corrected `E2` — CONFIRMED

Let `p=109` and take fixed integral coefficient lifts

```text
P = x - x^p + p A_0 + p^2 A_1,
Q = y      + p B_0 + p^2 B_1.
```

Exactly over `Z[x,y]`,

```text
P_x = 1 - p s + p A_{0x} + p^2 A_{1x},
P_y = p A_{0y} + p^2 A_{1y},
Q_x = p B_{0x} + p^2 B_{1x},
Q_y = 1 + p B_{0y} + p^2 B_{1y}.
```

The product `P_x Q_y` contributes, modulo `p^3`,

```text
1 + p(B_{0y} - s + A_{0x})
  + p^2(B_{1y} - s B_{0y} + A_{0x} B_{0y} + A_{1x}),
```

and `P_y Q_x` contributes `p^2 A_{0y} B_{0x}`, with every remaining summand in `p^3`. Hence

```text
det J(P,Q) - 1
  = p (A_{0x}+B_{0y}-s)
  + p^2(A_{1x}+B_{1y}+(A_{0x}-s)B_{0y}-A_{0y} B_{0x})
  + O(p^3).
```

The definitions

```text
C_1 = L(A_0,B_0) - s,
N_0 = (A_{0x}-s) B_{0y} - A_{0y} B_{0x}
```

are therefore the displayed `p` and `p^2` coefficients without `A_1,B_1`, including the minus sign on `A_{0y} B_{0x}`. This is erratum `(2.1)`. The same `N_0` is `[A_0,B_0]-s B_{0y}`. For monomials the bracket coefficient is `ad-bc`, with vanishing-power cases supplied by the product rule; that formula is not under correction.

`E1` over `F_p` is `C_1=0` as a polynomial over `F_p`. For integral lifts this means every coefficient of `C_1` is divisible by `p`, so `K=C_1/p` lies in `Z[x,y]` and is well-defined modulo `p`. Substituting `C_1=p K` into `(2.1)` gives

```text
det J - 1 = p^2 (K + L(A_1,B_1) + N_0)   modulo p^3.
```

Vanishing modulo `p^3` is therefore

```text
K + L(A_1,B_1) + N_0 = 0  mod p.          (2.2)
```

The sign of `K` is plus, not minus: the carry is the integer quotient of the first digit, not its negation. Uncarried `E2`, namely `L(A_1,B_1)+N_0=0` over `F_p`, is the special case `K=0 mod p`. That holds when `C_1=0` as a polynomial over `Z` (so `K=0`), and more generally when `C_1` is divisible by `p^2`. It is not a consequence of `E1` over `F_p` alone: derivative multipliers, in particular the exponent `p` on `x^p`, can make `C_1` equal to `p` times a nonzero polynomial even after `E1` holds over `F_p`.

This is exactly the inference that original review claim 2 stated as “setting the determinant equal to 1 forces the displayed `E1` and `E2` over `F_p`”. The displayed expansion in that claim is the same as `(2.1)` and is correct; the inference omits `K`. The original claim’s own flip criterion — “a `p^2` term in `det J-1` not equal to `L(A_1,B_1)+N(A_0,B_0)`” — is met by the extra summand `K`.

### 2. Marked-collision carries — CONFIRMED

The seed satisfies `1-1^p=0` and `0-0^p=0`, so

```text
P(1,0)-P(0,0) = p Delta A_0 + p^2 Delta A_1,
Q(1,0)-Q(0,0) = p Delta B_0 + p^2 Delta B_1,
```

as integers, for `Delta H = H(1,0)-H(0,0)`. Vanishing of `Delta P` modulo `p^3` is `p Delta A_0 + p^2 Delta A_1 = 0 mod p^3`, equivalently

```text
Delta A_0 = 0 mod p,
Delta A_0/p + Delta A_1 = 0 mod p,
```

and the same for `B`. Separate equations `Delta A_i = Delta B_i = 0 mod p` are the uncarried layerwise tests. They miss the integer carry of `Delta A_0` into the second layer whenever `Delta A_0` is divisible by `p` but not by `p^2`.

Exact integral vanishing `Delta A_i=Delta B_i=0` over `Z` implies both carry equations and is sufficient, as the erratum states. It is not necessary: `Delta A_0=p`, `Delta A_1=-1` also kills `Delta P` modulo `p^3`.

Independent collision-carry control, not required by the erratum but confirming `(2.3)`: `A_0=109 x`, `B_0=x^{108} y`, `A_1=B_1=0`. Then `C_1=p` so uncarried `E1` passes over `F_{109}`, `Delta A_0=109≡0 mod p`, `Delta A_1=0`, yet `Delta A_0/p + Delta A_1=1` and `Delta P=p^2 ≠ 0 mod p^3`. The five-slot map of claim 3 happens to have integral marked vanishing, so it is not itself a collision-carry witness; the evaluation identity does not need one.

### 3. Five-slot countercontrol — CONFIRMED

```text
A_0 = x^{109} - x,
B_0 = (1 + x^{108}) y,
A_1 = 0,
B_1 = (1 + 2 x^{108} + x^{216}) y.
```

Slots: `(P,(109,0))`, `(P,(1,0))`, `(Q,(0,1))`, `(Q,(108,1))`, `(Q,(216,1))`. Five labeled pairs, all coefficients nonzero.

Directly over `Z`, with `s=x^{108}`:

```text
A_{0x} = p s - 1,     B_{0y} = 1 + s,     A_{0y} = 0,
C_1 = (p s - 1) + (1 + s) - s = p s,     K = s,
N_0 = ((p-1)s - 1)(1+s) = -1 + 107 s + 108 s^2,
L(A_1,B_1) = 1 + 2s + s^2,
L(A_1,B_1)+N_0 = p(s + s^2).
```

Thus `C_1 ≡ 0 mod p` and `L_1+N_0 ≡ 0 mod p`: frozen uncarried `E1` and `E2` both pass over `F_{109}`. The corrected second residual is `K + L_1 + N_0 ≡ s ≠ 0 mod p`. Every displayed correction has `Delta=0` over `Z` (`A_0(1,0)=1-1=0`, and `B_0,B_1` vanish on `y=0`).

Closed form, independent of sparse Jacobians:

```text
P = (1-p)(x - x^p),
Q = y ( 1 + p(1+s) + p^2 (1+s)^2 ).
```

Then `P_y=0` and

```text
det J = P_x Q_y
      = (1-p)(1 - p s) (1 + p(1+s) + p^2 (1+s)^2)
      = 1 + p^2 s     modulo p^3.
```

So `det J-1 = p^2 x^{108} = 109^2 x^{108}` modulo `109^3`, not zero. The second engine also multiplied the four partials on the sparse representatives and reduced modulo `p^3`; the residual is exactly `{(108,0): 109^2}`.

This map is a countercontrol to the generic uncarried digit test. It is not a candidate Keller map (`det J ≠ 1`), not a support core, and not an enumeration result.

### 4. Parametric family, zero carry, grammar stop survives — CONFIRMED

For every integer `m>=1`,

```text
A_0 = y^m,     B_0 = x^{108} y.
```

Then `A_{0x}=0` and `B_{0y}=s`, so `C_1=0` as the zero polynomial over `Z`, hence `K=0`. Directly over `Z`,

```text
N_0 = (0-s)s - (m y^{m-1})(108 x^{107} y)
    = -x^{216} - 108 m x^{107} y^m.
```

Reduction modulo 109 uses `-108≡1`, giving `N_0 ≡ -x^{216} + (m \bmod 109) x^{107} y^m` over `F_{109}`. The transported successor

```text
A_1 = -x^{108} y^m,
B_1 = x^{216} y + 108 x^{107} y^{m+1}
```

has

```text
L(A_1,B_1) = -108 x^{107} y^m + x^{216} + 108(m+1) x^{107} y^m
           = x^{216} + 108 m x^{107} y^m
           = -N_0
```

over `Z`. Combined with `K=0`, corrected `E2` holds integrally, not merely over `F_{109}`. Every displayed monomial has `y`-degree at least `1`, so marked differences vanish identically.

Transport is composition, not an `E2` guess. With `F_{\mathrm{can}}=(x-x^p,\, y+p s y + p^2 s^2 y)` and `G_m=(x+p y^m,\, y)`, the binomial theorem modulo `p^3` retains only `k=0,1` in `X^p` (`k=2` contributes `p^3(p-1)/2` times a monomial) and yields exactly `(4.2)` of the original gate. The second engine recomputed this at `m=1,2,108,109,110,216,1000`. Closed forms prove it for every `m>=1`.

Slot sets, for every `m>=1`:

```text
layer 0:   (P,(0,m)), (Q,(108,1))
successor: (P,(108,m)), (Q,(216,1)), (Q,(107,m+1)).
```

These five labels are pairwise distinct (`0≠108`, `108≠216`, `108≠107`, and `P≠Q`). No successor coefficient vanishes modulo 109 (`-1`, `1`, and `108`). The union is not a same-slot cycle. `G_m` remains triangular of determinant one with inverse `(x-p y^m,\, y)`.

The first-layer carry of this family is the zero polynomial, so every identity the original review used in claims 3–5 is an identity over `Z`, not an uncarried `F_{109}` truncation. Unbounded literal exponent `m`, gauge-dependent residual support, three new transported slots, and failure of a finite successor-invariant grammar therefore remain. The registered procedural verdict remains `NO-FROZEN-GRAMMAR`: a cap on the number of slots does not bound literal exponents, and no finite exhaustive gauge normal form with successor transport was proved. This is still only a specification stop. It proves neither existence nor nonexistence of a cap-eight lift.

### 5. Hensel nonautomorphy is independent of digit carries — CONFIRMED

Gate §2.1 and original review claim 6 assume `F ∈ Z_{109}[x,y]^2` reducing to `(x-x^{109},y)` with `det J_F=1` as a polynomial identity, not as a pair of residue-digit equations. Multivariate Hensel on the complete DVR `Z_{109}` uses that the reduction has Jacobian `I` at every residue point and that `det J_F(\hat c)` is a unit. The 109-to-1 mapping of residue balls over `(0,b)`, noninjectivity over `Q_{109}`, and finite-type embedding into `C` then proceed exactly as in the original review.

None of those steps reads a Witt digit, a carry `K`, or a marked-section increment. A truncated expansion that omitted `K` cannot infect a lemma whose hypothesis is already exact determinant one. The lemma still does not assert that such an `F` exists, still does not repair the failed grammar, and still does not use the frozen marked-section equations.

### 6. Packed `CLOSED-SUPPORT + UNIT-L` is unaffected and conditional — CONFIRMED

Pack `F=(x-x^p+p A,\, y+p B)` with full `Z_{109}` coefficients `(A,B)`. The `2×2` determinant produces no `p^3` remainder:

```text
det J_F - 1 = p(L(A,B)-s) + p^2 N(A,B)
            = p(L(A,B)-s + p N(A,B)),
```

exactly in `Z[x,y]` for integral `(A,B)`, hence exactly in `Z_{109}[x,y]`. The second engine checked this as an unreduced integer identity on twenty-five random supports, on the canonical slot, on the five-slot pair packed as `A=A_0+p A_1`, and on the `m=1` transported pair. Digit carries of a two-layer truncation never enter, because there is no truncation.

The contraction criterion of gate §5.1 is the Banach map `T(u)=R(s-109 N(u))` on a finite free, already gauge-fixed coefficient module whose residual module is nonlinearly closed and on which `L` admits a `Z_{109}`-unit inverse or right inverse. Those hypotheses refer to the packed equation, not to uncarried `E2`. No module in this run meets them. The same two closure probes remain: canonical `B=x^{108} y` produces `N=-x^{216}` outside `L(U)`; the allowed vector `B=x^{216} y` in the five-slot union produces `N=-x^{324}` outside its derivative residual span. The criterion is still only a resurrection target. Combined with claim 5 it would be a JC2 counterexample; no such support was found or tested by enumeration.

### 7. Scope; what is superseded — CONFIRMED

The case directory contains `PREREGISTRATION.md`, `manifest.json`, `FREEZE.sha256`, `verify_spec_obstruction.py`, `spec_obstruction.json`, and the carry replay `verify_carry_erratum.py`. There is no `enumerate_dfs.py`, `enumerate_ilp.py`, or other transition generator. The preregistration header remains `SPECIFICATION GATE; NO ENUMERATION RUN`. Sampling closed-form identities is not cap-eight graph enumeration. No exact lift was produced. No characteristic-zero counterexample was inferred. No statement in the erratum or in this review proves or disproves JC2.

**Supersession, exactly.** Original review claim 2 is superseded in one assertion: that the displayed `E1` and `E2` over `F_{109}` are by themselves the exact condition modulo `109^3`. Not superseded, and reconfirmed here, are: the truncated expansion `(2.1)` as written; the monomial bracket `[x^a y^b,x^c y^d]=(ad-bc)x^{a+c-1}y^{b+d-1}`; the formula `N=(A_x-s)B_y-A_y B_x`; and the packed exact identity. Original claims 1 and 3–8 are not superseded. In particular claims 3 and 4 of that review use the family of erratum claim 4, whose carry is the zero polynomial over `Z`.

The producer, preregistration, and manifest display the same uncarried `E2` and layerwise marked tests as frozen coefficient equations over `F_{109}`. Those generic assertions are quarantined on the same terms as original claim 2. Their conclusions about the triangular obstruction family, the Hensel lemma, and the packed contraction criterion are not quarantined.

---

## Smallest missing hypothesis or overclaim

None of the seven claims is an existence theorem, a nonexistence theorem for cap-eight lifts, or a characteristic-zero decision. No identity above failed.

The smallest precision a reader could miss, and that this review therefore isolates, is the same one the erratum already draws: `K=C_1/p` is a polynomial quotient of coefficients after `E1` over `F_p`, and it is the only missing `p^2` summand. Uncarried `E2` remains valid on every family whose first-layer equality holds over `Z`. The obstruction family is of that kind. The five-slot map is not a candidate, and constructing it does not enlarge the registered cap or the registered seed.

---

## Stop conditions that remain in force

No cap, degree, or prime may be changed in response to this review. A request to choose a large exponent box is not a resurrection trigger. The only resurrection trigger remains a separately reviewed theorem giving either a finite gauge-normal-form grammar with exact successor transport, or a terminating symbolic-motif classification exhaustive for all exponent supports of size at most eight, or an explicit finite module that meets `CLOSED-SUPPORT+UNIT-L`.

Carry-aware digit equations are the correct truncated form of the first nonlinear successor. They do not make the literal-exponent graph finite.

No result here proves or disproves JC2.
