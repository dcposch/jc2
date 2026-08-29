# Hostile review: `8_28` Keller-face R2 rootwise cusp unit-carrier classification

**Reviewer:** Grok 4.6 (independent hostile referee). **Date:** 2026-08-27.  
**Target:** the charged freeze of Sol's additive R2 case

`cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/`  
together with `xmodel/ggv-8_28-keller-face-cusp-unit-carrier-classification-r2-sol-20260827.md`.

**Claim under review (narrow):** after a formal, root-local Morse chart
`F=u^2+U(t)` with `u\equiv H\pmod t` at a simple root of squarefree `H=X^8-1`,
an unrestricted local sidecar

```text
G = W + V u + Q u^2 + Gamma u^3 + sum_{m>=4} G_m u^m,    Gamma(0)=1
```

does not create a third constant-in-`u` Jacobian carrier through weight 22.
Over each geometric simple-root residue field the first constant term is
exactly one of `6 V_8 U_{14}` or `(9/2) U_{11}^2`, hence

```text
6 H'(c) V_8(c) U_{14}(c) = 1     if V_8(c) != 0,
(9/2) H'(c) U_{11}(c)^2 = 1     if V_8(c) = 0,
```

and the two cases may coexist on different étale factors of the same `H`.
**Not** under review, and not granted if claimed: a raw `2S/3S`
cleanup/provenance compiler, a global `H`-multiple at `E_{22}`, the statement
that every sidecar lies in R1's `M(Y)` image, exclusion of the `8_28`
face/family, a Keller pair, GGV-to-tree transport, `G2-PSC`, `G2-BD`, or JC2.

**Method.** Rehashed the five charged artifacts and the two prompt-pinned
inputs. Rehashed the live R1 freeze bytes that R2 itself pins, and the live
R0 cusp-jet freeze, to test additivity. Independently rederived the parametric
Morse chart, the chain-rule identity `E=u_X L`, the three low-`u` channels,
the lower-weight induction, both carrier branches, and the mixed-factor
fixture, using only desk-scale exact arithmetic in `Q` and sparse
`(t,u)`-series. Producer `PASS`, the producer sparse ring, the R0 hostile
review, and the R1 report were not used as evidence for any new R2 identity.
R1 is under a separate additive review; R2 was required to rederive the
formulas it consumes, and those rederivations are what this review checks.
No AWS, no CAS, no producer-file edits, no canonical-ledger edits, no
`jc2-lean` access.

**Firewall.** Maximum licensed result is formal/rootwise carrier completeness
through weight 22, robust to arbitrary local higher-`u` sidecars. A Morse
chart is not a global polynomial source automorphism. A rootwise scalar
`C_{22}=1/H'(c)` is not a global `E_{22}=1` polynomial.

---

## Verdict table

| Item | Verdict |
|---|---|
| Custody / dedup / additivity | **CONFIRMED** |
| Formal Morse existence / orientation | **CONFIRMED** |
| Exact chain rule and determinant unit | **CONFIRMED** |
| `[u^0]` channel | **CONFIRMED** |
| `[u^1]` channel | **CONFIRMED** |
| `[u^2]` channel | **CONFIRMED** |
| Independence from unrestricted sidecar | **CONFIRMED** |
| Lower induction (`U_1..U_7=V_1..V_7=0`) | **CONFIRMED** |
| Carrier branch `V_8 != 0` | **CONFIRMED** |
| Carrier branch `V_8 = 0` | **CONFIRMED** |
| Mixed-factor / deck typing | **CONFIRMED** |
| Compiler / global image gap | **CONFIRMED** |
| Final scope | **CONFIRMED** |

No item is **REFUTED**. No item is **GAP/REPAIR**. No smallest failing
coefficient, sidecar term, root/factor, determinant, or hypothesis was found.
The producer verifier does not itself construct the Morse chart, run the
induction, or exclude same-weight pair cancellation; those were rederived
here and survive. Freeze-consistency of `verify_r2.py` against
`RESULT_R2.json` is custody only and is not a mathematical witness.

---

## Independent hashes

Recomputed SHA-256, all matching the charged prompt and the internal
`FREEZE.sha256` lines:

```text
74c6c78e4faf527172703d5a115767562d89d9fa20868fc431dcc1f7cd258f15
  cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/verify_r2.py
0dffbb36c20d0b80498d765168a47cdb9ed2889ffc7bd105dce7ec835f600b1d
  cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/RESULT_R2.json
c95f194df15bce9db128e10329602a19ad3cf62bec88f829bc76182ae9fbdc83
  cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/README.md
0f8f3833c8fa16349d52c6d68829e5c86200ab064f84e4172b0ba4039314b733
  xmodel/ggv-8_28-keller-face-cusp-unit-carrier-classification-r2-sol-20260827.md
453f7821f88add5d97b65cee41fe3a4df225db5768526746cf4ff1431aa73aa6
  cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/FREEZE.sha256
```

The four lines inside `FREEZE.sha256` match the four hashed producer files.
The freeze list does not hash itself; that is the usual freeze shape, not a
custody defect.

Prompt-pinned reviewed/input context, live bytes:

```text
171ff47c844331da8971a731c1ffaf20c31ed5b2ba86fdee2d0d81219eb002b0
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-hostile-review-grok-20260827.md
05cbb5c046f9aa4b89e1104448e77fd38ec3a146d2422bf84773f81d668bfe3c
  cases/ggv_8_28_keller_face_cusp_jet_pinning_r1_20260827/FREEZE.sha256
```

R2's own live pins of the R1 freeze contents, all matching both
`RESULT_R2.json` and the R1 freeze list:

```text
f21f6435796f197376f76fc9c57c50743e9a356614591ce88e41dcfad4c3e5f0  R1 verify_r1.py
392f6c0c3ca70a35b9b466944c243a927430838abe022eb960d7f2315e1684f3  R1 RESULT_R1.json
238f51d031b81be14cbbd6756778efbf742a7471b9247e964d78d9f4b1050781  R1 README.md
66121bddbe0b004ad1b8960f896d3691c4dd3963068fbfddb6ad3ba15dda7027  R1 sol report
```

Prior R0 cusp-jet freeze, still identical to the bytes recorded in the pinned
R0 review:

```text
ef9acfa90935b32e244367dada67ab35d6454f431f6d43dc35d144b3d08fe46c  R0 verify.py
46e1b3434badcea007a914ec71bf60d9758ee76d312dc00d252342d52beed76d  R0 RESULT.json
79a16f282f0a3a3e5409b3e0b6d4a8dc61e2fedaa6babdf673b5645d64c38530  R0 README.md
3e4e608d32c44b1b0208bd5472257ba1dbe4cadf4ef5efb2ace49d3d47d756be  R0 sol report
6928428f9cc46641a80275e2bbfa62e784c4290ff041f5089ae789507fa8804f  R0 FREEZE.sha256
```

---

## 1. Custody / dedup / additivity — CONFIRMED

All five charged digests match the prompt. R2 lives in a new case directory
and a new sol path. It does not rewrite the R0 freeze, the R1 freeze, or
either sol report.

The history statement is accurate, and it is the only use made here of the
pinned R0 review and the R1 README, as custody/history rather than as lemmas:

- R0 established a rootwise fixture `6 H'(c) V_8(c) U_{14}(c)=1` in the
  restricted `A_2` packet `G=u^3+V u+W`, together with an explicit global
  remainder `(13/12)H` for one interpolating ansatz.
- R1 repaired the raw/local typing of that fixture (`U_{14}=X` is not a
  direct raw `F_{14}` source coefficient) and tested two named polynomial
  ansatzes, including the `U_{11}^2` alternative, landing both in an operator
  `M(Y)` whose image does not contain `1`. Completeness of those two ansatzes
  for every raw jet was left open.
- R2 claims only the missing rootwise exhaustion, now with an unrestricted
  local sidecar. It does not claim that R1's pending verdict is settled.

R2 pins R1 bytes for additivity. That is a custody coupling, not a logical
dependence: every identity used below is rederived from the charged `E`
formula and the Morse chart, without taking R1's two-slot image statement as
a hypothesis. If the separate R1 review later revises R1 prose, the R2 pin
will break as custody, but the R2 theorem as rederived here would not.

No earlier charged artifact proves that `Q`, `Gamma-1`, and `u^4+` cannot
create a third constant carrier. R1's remaining-work line that a later
compiler should land in `V_8 U_{14}` or `U_{11}^2` is a task statement, not
that proof.

---

## 2. Formal Morse existence / orientation — CONFIRMED

Work throughout at one simple root `c` of `H=X^8-1`, over the residue field
`κ=κ(c)` (so `κ=Q` at `c=\pm 1`, and a cyclotomic extension `Q(ζ_8)` at the
other geometric points). Coefficient hypotheses, all used later as well:

- `char κ=0`, in particular `2,3∈κ^×`;
- `H'(c)∈κ^×` (equivalently `H` squarefree at `c`; independently,
  `gcd(X^8-1, 8X^7)=1` in `Q[X]`);
- the complete local ring `κ[[X-c,t]]`, or equivalently `κ[[u,t]]` after
  the chart is built;
- `F∈κ[[X-c,t]]` with `F(X,0)=H(X)^2`.

No analytic disk, no `C^∞` Morse lemma, and no global polynomial
`(X,t)`-automorphism is assumed or obtained.

At `t=0`:

```text
F(c,0)=0,
F_X(c,0)=2 H(c) H'(c)=0,
F_XX(c,0)=2 H'(c)^2 ∈ κ^×.
```

The Hessian in the `X`-direction is therefore a unit. The implicit-function
theorem in `κ[[t]]` produces a unique critical section
`X_{\mathrm{crit}}(t)∈c+t κ[[t]]` with `F_X(X_{\mathrm{crit}}(t),t)=0`. Set

```text
U(t) := F(X_{\mathrm{crit}}(t), t) ∈ t κ[[t]].
```

Then `F-U(t)` vanishes to order two along `X=X_{\mathrm{crit}}`, so

```text
F - U(t) = (X - X_{\mathrm{crit}}(t))^2 Q(X,t),
Q(c,0) = F_XX(c,0)/2 = H'(c)^2,
```

and `Q` is a unit in `κ[[X-c,t]]`. The formal binomial/Hensel square root of
that unit exists because `2∈κ^×` and `Q(c,0)` is already a square in `κ`.
The two roots are `±H'(c)` at the closed point. Choosing

```text
q(c,0)=+H'(c)
```

and setting `u=(X-X_{\mathrm{crit}}) q` gives `F=u^2+U(t)` with
`u_X(c,0)=H'(c)`. At `t=0` one has `X_{\mathrm{crit}}(0)=c` and
`q(X,0)=H(X)/(X-c)` as formal series, hence

```text
u(X,0)=H(X).
```

That is the orientation convention `u\equiv H\pmod t`. The opposite square
root would give `u\equiv -H\pmod t` and would flip the sign of every odd
coefficient of `G` (in particular `V` and `Γ(0)`). The charged formulas
fix the `+H` chart and `Γ(0)=1`, which is exactly `G(X,0)=H(X)^3` in this
orientation. Either the sign or the leading cube would have to move if the
chart were flipped; both are fixed, so the later scalars `6` and `9/2` are
not free signs.

Attacks that fail:

- **Sign/orientation.** Fixed by `u=H\bmod t` and `q(c,0)=+H'(c)`, not by
  an implicit positivity on `U`. The endpoint identity in §3 inherits this
  sign through `u_X(c,0)=H'(c)`.
- **Square root.** One takes the square root of the *unit* `Q`, not of `F`.
  No ramified extension of `κ` is required.
- **Critical section.** Unique in `κ[[t]]` by `F_XX(c,0)∈κ^×`. `U(t)` is
  the critical value, not an extra coordinate.
- **Convergence.** Not claimed. The chart is formal.
- **Global polynomial coordinate.** A series `u∈κ[[X-c,t]]` is not a
  polynomial automorphism of `Q[X,t]` and does not preserve supports. Any
  reading of `F=u^2+U(t)` as a global polynomial identity in `X` is a scope
  failure; the charged writeup does not make that reading.

The result is allowed to be, and is, formal and root-local. Leading-face
normalisation `Γ(0)=1`, `W(0)=V(0)=Q(0)=0`, and `G_m(0)=0` for `m≥4` is
forced by `G(X,0)=H^3=u^3`, not by an extra ansatz.

---

## 3. Exact chain rule and determinant unit — CONFIRMED

Take the charged operator as given,

```text
E = 12 F_X G - 8 F G_X - t (F_X G_t - F_t G_X),
```

and write `F(X,t)=\widetilde F(u(X,t),t)`, `G(X,t)=\widetilde G(u(X,t),t)`,
with `t`-derivatives of the tilded functions holding `u` fixed. Chain rule:

```text
F_X = \widetilde F_u u_X,
F_t = \widetilde F_u u_t + \widetilde F_t,
G_X = \widetilde G_u u_X,
G_t = \widetilde G_u u_t + \widetilde G_t.
```

The wedge expands as

```text
F_X G_t - F_t G_X
  = (F_u u_X)(G_u u_t + G_t) - (F_u u_t + F_t)(G_u u_X)
  = u_X (F_u G_t - F_t G_u),
```

in which the two `u_t` summands cancel identically (`F_u G_u u_X u_t` is
commutative). Substituting into `E` factors `u_X`:

```text
E = u_X L,
L = 12 F_u G - 8 F G_u - t (F_u G_t - F_t G_u).
```

This is an identity of formal series, not a truncation. A numeric
substitution `(F_u,F_t,G_u,G_t,u_X,u_t,t,F,G)=(3,5,7,11,13,17,19,23,29)`
reproduces `E=u_X L` on both sides; that is a check of the bilinear algebra,
not a replacement for the identity.

`u_X(c,0)=H'(c)∈κ^×`, so `u_X` is a unit of `κ[[X-c,t]]` and of `κ[[u,t]]`.
In the `t`-adic filtration the product `E=u_X L` is triangular:

```text
E_0 = a_0 L_0,          a_0 = u_X(·,0) a unit of κ[[u]],
E_n = a_0 L_n + sum_{i=1}^n a_i L_{n-i}.
```

Thus `E_0=\cdots=E_{21}=0` if and only if `L_0=\cdots=L_{21}=0` as series in
`u`. No determinant unit is missing, and the triangular inference does not
pass through evaluation at `u=0` yet.

At weight 22, `E_{22}=a_0 L_{22}`. The constant term in `u` is
`H'(c)\,[t^{22}u^0]L`, because `a_0=H'(c)+O(u)` and
`L_{22}=C_{22}+O(u)`. If `E_{22}` is the constant `1` (as a polynomial in
`X`, or as the constant series `1` in `κ[[X-c]]`), evaluation at the closed
point gives

```text
1 = H'(c)\, [t^{22} u^0] L.
```

Higher `u`-coefficients of `L_{22}` are *not* used as constant-channel
carriers. They cannot supply the value `1` at `u=0`: any positive power of
`u` vanishes at `c`. Conversely, they are constrained by the function
identity `H'(X) L_{22}(H(X))=1` in `κ[[X-c]]`, which is precisely the
global-image question left open in §12. For the rootwise scalar it is
enough, and it is necessary, that `C_{22}=1/H'(c)∈κ^×`.

A sign error in `u_X(c,0)`, a swap of `(F,G)`, or a failure to cancel `u_t`
would change this endpoint. None of those errors is present.

---

## 4. Low-`u` channels — CONFIRMED (each)

Insert `F=u^2+U(t)` so that `F_u=2u` and `F_t=U'`, and expand

```text
G = W + V u + Q u^2 + Γ u^3 + sum_{m≥4} G_m u^m
```

with `t`-derivatives at fixed `u`. Then

```text
L = 24 u G - 8(u^2+U) G_u - 2 t u G_t + t U' G_u.
```

**`[u^0]`.** Only `-8 U V + t U' V` survives, hence

```text
[u^0] L = V (t U' - 8 U).
```

Coefficientwise, writing `U=sum_{j≥1} U_j t^j` and `V=sum_{i≥1} V_i t^i`
(the `t^0` coefficients vanish by the leading face),

```text
C_n := [t^n u^0] L = sum_{i+j=n} V_i (j-8) U_j.
```

**`[u^1]`.** The contributing pieces are `24 W`, `-16 U Q`, `-2 t W'`, and
`2 t U' Q`, hence

```text
[u^1] L = 24 W - 2 t W' + 2 Q (t U' - 8 U),
```

and

```text
[t^n u^1] L = (24-2n) W_n + 2 sum_{i+j=n} Q_i (j-8) U_j.
```

Weight twelve is the `W` resonance (`24-2n=0`). That resonance constrains
`Q,U` at `n=12`; it does not feed the constant channel.

**`[u^2]`.** The contributing pieces are `24 V`, `-8 V`, `-24 U Γ`,
`-2 t V'`, and `3 t U' Γ`, hence

```text
[u^2] L = 16 V - 2 t V' + 3 Γ (t U' - 8 U),
```

and

```text
D_n := [t^n u^2] L
     = 2(8-n) V_n + 3 sum_{i+j=n} Γ_i (j-8) U_j.
```

Every displayed `t`-derivative is accounted for: `t\partial_t` acts on a
monomial `t^n` by the scalar `n`, which is what produces `24-2n`, `16-2n`,
and `j` in `t U'-8U`. There is no dropped `W'`, `V'`, or `U'` term in these
three channels.

An independent sparse `(t,u)` expansion through `t^{22}`, with generic
prime coefficients for all of `U,V,W,Q,Γ,R=G_4,G_5,G_6`, matched the three
convolutions on every weight `n=0..22`. That expansion was not the producer
ring (different truncation, and `G_5,G_6` present). The producer engine
itself is audited in §5; it is not the proof.

---

## 5. Independence from unrestricted sidecar — CONFIRMED

Let `m≥4` and consider a pure term `G_m(t) u^m`.

- `24 u G` contributes `u^{m+1}` with `m+1≥5`.
- `-8 u^2 G_u` contributes `u^{m+1}` with `m+1≥5`.
- `-8 U G_u` contributes `U · m G_m u^{m-1}`, which has `u`-order `≥3`.
- `-2 t u G_t` contributes `u^{m+1}` with `m+1≥5`.
- `t U' G_u` again has `u`-order `≥3`.

The nearest contaminant is `m=4`, which first appears in the `u^3` channel
as `4 G_4 (t U'-8 U)`. It does not enter `u≤2`. Independently, the
difference of `L` for `G=u^3+R u^4+S_5 u^5+S_6 u^6` versus `G=u^3`, with
the same generic `U(t)`, has vanishing `u^0,u^1,u^2` coefficients through
weight 22.

Thus:

- `Q` enters only `[u^1]`;
- `Γ-1` enters only `[u^2]`;
- every `u^4+` coefficient of `G` misses `[u^0]`, `[u^1]`, and `[u^2]`;
- the constant channel `C(t)=V(t U'-8 U)` is independent of `Q`, `Γ`, `W`,
  and all higher-`u` terms.

Producer-engine audit, not used as evidence above:

- `TMAX=22` does not alias `[t^n]` for `n≤22`: dropped products have
  `t`-weight `>22`.
- `UMAX=6` with `G` only through `u^4` is a weaker computational probe than
  the hand expansion; it is sufficient to see that `u^4` misses `u≤2`, and
  the `m≥5` case is the same estimate.
- Coefficient polynomials are bilinear in `(U_j, V_i/Q_i/Γ_i)`, so the
  “degree `≤2`” monomial encoding is adequate for the channels. The
  coordinate-change identity uses higher-degree monomials; the encoder does
  not truncate degree, so that comment in the source is sloppy but not
  false in code.
- Expected convolutions are independently coded and asserted against
  computed `L`. That is a real check of those three formulas, not a
  hard-coded `L`.
- `classification_replay` only enumerates orders and scalars. It does not
  prove uniqueness of pairs or run the induction. Those are in the sol
  prose and were rederived here.

No omitted term, truncation artifact, aliasing, or hard-coded equality
affects the three charged channels.

---

## 6. Lower induction — CONFIRMED

All statements in this section and the next two are over one geometric
simple-root residue field `κ`, so a nonzero value is a unit and
`z^2=0` forces `z=0`. Nilpotents and zero-divisors are excluded by working
on geometric points of the étale algebra `Q[X]/(H)`, which is reduced
because `H` is squarefree.

`L_n=0` for `n<22` as series in `u`, so in particular `C_n=D_n=0` for
`n<22`.

`U_0=0` and `V_0=0` (`D_0=16 V_0=0`). Let `k` be minimal with `U_k\neq 0`,
and suppose `k<8`. For `n<k`, every `U_j` in `D_n` vanishes, so
`D_n=2(8-n)V_n=0`. Here `8-n\neq 0`, hence `V_n=0` for `n<k`.

At `n=k`, the only surviving convolution in `D_k` is `i=0`, `j=k`:
`Γ_0=1` and `U_j=0` for `0<j<k`. The partner `U_8` is unavailable because
`k<8`. Thus

```text
2(8-k) V_k + 3(k-8) U_k = 0.
```

Since `8-k=-(k-8)\neq 0`, one gets `V_k=(3/2) U_k`. Then `C_n=0` for
`n<2k` because both `V_i` and `U_j` vanish below `k`, and the first
constant coefficient is at weight `2k`,

```text
C_{2k} = V_k (k-8) U_k = (3/2)(k-8) U_k^2.
```

For `k=1,\ldots,7` one has `2k∈{2,4,6,8,10,12,14}`, all strictly less than
22, and the scalar `(3/2)(k-8)` is
`-21/2,-9,-15/2,-6,-9/2,-3,-3/2`, none zero in `κ`. This contradicts
`C_{2k}=0`. Therefore no such `k<8` exists:

```text
U_1=\cdots=U_7=0,
```

and then `D_n=2(8-n)V_n=0` gives `V_1=\cdots=V_7=0`.

`Q`, `W`, `Γ-1`, determinant coefficients, and `u^4+` terms never enter
`C` or the first-`k` instance of `D`. The first forbidden constant
coefficient is exactly `3(k-8)U_k^2/2` at weight `2k`.

At weight eight both `U_8` and `V_8` are resonant:
`D_8=2(0)V_8+3\sum Γ_i(j-8)U_j` has every `U_j` either below eight
(vanishing) or at eight (killed by `j-8=0`). So `U_8` is annihilated by
`t\partial_t-8` in every charged convolution. In particular every occurrence
of `U_8` in `C_n` and in `D_n` is killed by an `(8-8)` factor.

---

## 7. Carrier branch `V_8\neq 0` — CONFIRMED

Let `k>8` be minimal with `U_k\neq 0`. Such a `k` exists: `C_{22}=1/H'(c)\neq 0`,
while `U_8` cannot contribute to `C`.

For `8<n<k`, `D_n=2(8-n)V_n` because the only possible `U`-partner below
`k` is `U_8`, which is killed. Thus `V_n=0` for `8<n<k`. At `n=k` the full
`Γ` convolution is

```text
D_k = 2(8-k) V_k + 3 sum_{i+j=k} Γ_i (j-8) U_j.
```

The sum has `j=k`, `i=0` giving `(k-8)U_k`, and `j=8`, `i=k-8` giving
`Γ_{k-8}(8-8)U_8=0`. No earlier `Γ_r`, `Q_r`, `W_r`, determinant
coefficient, or higher-`u` term enters. Hence again `V_k=(3/2)U_k`, even
with generic `Γ=1+O(t)` and generic `U_8`. An independent numeric check
with prime `Γ_i` and `U_8=99` still returned `V_k=(3/2)U_k` at
`k=9,11,14`.

Now `C_n=\sum_{i+j=n} V_i(j-8)U_j`. With `V_8\neq 0` the first surviving
pair is `i=8`, `j=k` at weight `8+k`, coefficient `(k-8)V_8 U_k`. Other
pairs at that same first weight:

- `V_k U_8` is killed by `(8-8)`;
- `V_i` for `i<8` or `8<i<k` vanish;
- `U_j` for `j<k`, `j\neq 8` vanish.

No cancellation by another pair. Vanishing of `C_n` for `n<22` forces
`8+k≥22`, i.e. `k≥14`. Nonvanishing of `C_{22}` forces `8+k≤22`, i.e.
`k≤14`. Thus `k=14` and

```text
C_{22} = 6 V_8 U_{14}.
```

The endpoint of §3 gives `6 H'(c) V_8(c) U_{14}(c)=1`. Later coefficients
(`U_{15}`, `V_{16}`, \ldots) cannot hit weight 22: they would require a
partner of complementary weight already forced to vanish. Weights `>22` are
irrelevant to the first carrier.

If `U_{11}` were also nonzero, the first constant term would already have
occurred at weight `19`, which is forbidden. So this branch forces
`U_9=\cdots=U_{13}=0` and in particular excludes a simultaneous `U_{11}^2`
carrier.

---

## 8. Carrier branch `V_8=0` — CONFIRMED

On the complementary geometric points, `V_8=0`. The first surviving pair in
`C` is then `i=k`, `j=k` at weight `2k`, with coefficient

```text
V_k (k-8) U_k = (3/2)(k-8) U_k^2.
```

The same pair-uniqueness argument applies: any other complementary index
either hits a vanishing lower `V` or a vanishing lower `U`, or hits `U_8`
and is killed. No same-weight cancellation.

Vanishing below 22 forces `2k≥22`, i.e. `k≥11`. Nonvanishing at 22 forces
`k≤11`. Thus `k=11` and

```text
C_{22} = (9/2) U_{11}^2,
```

hence `(9/2) H'(c) U_{11}(c)^2=1`. The scalar `9/2=3/2·3` uses `2,3∈κ^×`,
already in force.

There is no third branch. If `V_8=0` and every `U_k` for `k>8` vanished,
then `C\equiv 0`, contradicting the endpoint. Coefficients beyond weight 22
cannot move the first nonzero slot.

---

## 9. Mixed-factor / deck typing — CONFIRMED

The dichotomy is a statement about geometric residue fields, not about a
single global bit `V_8=0` versus `V_8` a unit in `Q[X]/(H)`. The charged
example

```text
H = (X^4+1)(X^4-1) = X^8-1,    V_8 = X^4+1
```

is computed independently in `Q[X]`, low coefficient first:

```text
gcd(H, X^4+1) = X^4+1,
(X^4+1) mod (X^4+1) = 0,
(X^4+1) mod (X^4-1) = 2,
gcd(X^4+1, X^4-1) = 1.
```

So `V_8=0` on the first factor (the `U_{11}^2` case) and `V_8=2∈κ^×` on
the second (the `V_8 U_{14}` case). Both carrier types can coexist on one
and the same `H`. A globally binary reading of a polynomial `V_8` is false
and is not licensed.

For a global polynomial representative of `V_8` modulo `H`, splitting by
`gcd(H,V_8)` or by the idempotents of `Q[X]/(H)` (here
`(X^4+1)/2` and `(1-X^4)/2`, using `2∈Q^×`) is sufficient to separate the
two geometric loci. For a purely local packet one simply evaluates the
scalar `V_8(c)∈κ(c)`. In either language the following tags must survive
on every packet:

- geometric root `c`, or the étale factor through `c`;
- Galois/conjugation orbit (the factors `X^4\pm 1` are rational, but the
  four roots of `X^4+1` are conjugate over `Q` in two quadratic pairs);
- chart and orientation `u\equiv H\pmod t`;
- the determinant unit `H'(c)=8c^7=8 c^{-1}`.

Dropping `H'(c)` or the orientation would flip or lose the scalars `6` and
`9/2`. Dropping the factor tag would identify the two branches.

A stronger single étale-algebra sentence “`V_8` is zero or a unit in
`Q[X]/(H)`” is not justified and is not claimed. The charged theorem stays
at the correct strength.

---

## 10. Compiler / global image gap — CONFIRMED

R2 classifies the first constant-in-`u` carrier of a Morse packet. It does
not compile a raw `2S/3S` jet through that Morse cleanup with source
provenance; it does not prove that every raw higher-`u` sidecar lies in the
image of R1's operator

```text
M(Y) = 4 H Y' + 6 H' Y;
```

and it does not classify the global polynomial `H`-multiple contributed at
`E_{22}`. Those are exactly the remaining-gap entries in `RESULT_R2.json`,
and they are genuine.

In particular, the local identity `C_{22}=1/H'(c)` at eight roots does not
force `E_{22}=1` in `Q[X]`. Higher-`u` terms, `X`-dependence left in a
naïve interpolant of local `U,V`, and the Jacobian factor `u_X=H'(X)+O(t)`
all produce global `H`-multiples. That is the same species of remainder
already visible for the truncated pair `(U_{14},V_8)=(X,1/48)`, and R2
correctly refuses to close it.

---

## 11. Final scope — CONFIRMED

The charged artifacts claim, and only claim, formal simple-root carrier
completeness through weight 22, including an arbitrary local higher-`u`
sidecar, with mixed-factor typing and with the two displayed unit
identities. They do not claim:

- a global typed-normal-form or `E_{22}` image theorem;
- that R1's `M(Y)` exhausts every raw sidecar;
- exclusion of the `8_28` face or family;
- a Keller pair, a counterexample, GGV-to-tree transport, `G2-PSC`,
  `G2-BD`, or JC2.

Maximum permitted result reached, not exceeded.

---

## Independent arithmetic (desk scale)

All identities above were rerun in `Q` with univariate polynomials (low
coefficient first) and sparse `(t,u)` supports. No producer function was
imported. The producer `PASS` token was not used.

Recorded checks:

- `E=u_X L` on a generic integer 9-tuple, with exact `u_t` cancellation in
  the wedge.
- `[t^n u^m]L` for `m=0,1,2` and `n=0..22` against the three charged
  convolutions, with generic prime coefficients including `G_4,G_5,G_6`.
- Difference of `L` for `G=u^3` versus `G=u^3+R u^4+S_5 u^5+S_6 u^6`
  vanishes in `u≤2` through weight 22; a pure `R u^4` term with the same
  `U(t)` first appears in `u^3` as `4 R(t U'-8 U)`.
- Lower scalars `(3/2)(k-8)` for `k=1..7`; branch scalars `6` and `9/2`;
  `U_8` factor `8-8=0`.
- `V_k=(3/2)U_k` from the full `Γ` convolution at `k=9,11,14`, with
  generic `Γ_i` and with `U_8=99`.
- Unique contributing pair at the first constant weight on each branch;
  `C_{22}` receives no later complementary pair once the lower vanishing
  is imposed.
- `H=(X^4+1)(X^4-1)`, `gcd(H,X^4+1)=X^4+1`, remainder `0` and `2` on the
  two factors, `gcd(H,8X^7)=1`.

No producer `PASS` was required for any of these.

---

## Licensed conclusion

R2 is an additive, correctly scoped, formally local classification: at each
geometric simple root, after Morse normalisation with the charged
orientation, the constant Jacobian through weight 22 is carried by exactly
one of `6 H'(c) V_8(c) U_{14}(c)` or `(9/2) H'(c) U_{11}(c)^2`, and
unrestricted local sidecars do not create a third constant-channel
mechanism. The compiler that would turn this rootwise dichotomy into a
global `E_{22}` image statement, a raw-provenance normal form, or an
`8_28` exclusion is not supplied and is not licensed by this freeze.
