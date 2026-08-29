# Hostile review: additive `8_28` R3 rational-mode normal form and squarefree replacement-edge exclusion

**Reviewer:** Grok 4.6 (independent hostile referee). **Date:** 2026-08-27.  
**Target:** the charged freeze of Sol's additive R3 rational-mode exclusion

`cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/`  
together with `xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-sol-20260827.md`.

**Additive follow-up, not a retrial of R0/R1 and not an import of R2.** The
completed R1 hostile review

```text
d40cd78f4f0afc12d09f8d1e99724de9fd5125fddc064089d6ca0870c7d777e0
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-r1-hostile-review-grok-20260827.md
```

confirmed only the raw/local type repair and the two named polynomial
ansatzes `E_{22}=M(A((3/2)P+C))` and `E_{22}=M(3A^2/4)`, together with
failure of `M(Y)=1` inside those ansatzes. That verdict is preserved and
is **not** evidence for R3. R2 is a separate pending review and is **not**
imported: no R2 carrier classification, sidecar statement, or local
scalar conclusion is used below. R3 is reviewed only as a self-contained
derivation in `K(X)[[t]]`.

**Claim under review (narrow):** there is no polynomial-`X` formal jet
`F,G\in K[X][[t]]` over a characteristic-zero field `K` with
`F_0=(X^8-1)^2`, `G_0=(X^8-1)^3`, and
`E=12 F_X G-8 F G_X-t(F_X G_t-F_t G_X)=t^{22}+O(t^{23})`. The argument
is a complete homogeneous classification of `E(F,\cdot)` on
`K(X)[[t]]` through weight 21, including the two negative-power modes,
followed by an endpoint pole-order reduction to `M(Y)=1`. **Not** under
review: the original non-Keller control with `F_0=X^{16}-1`, the whole
GGV `8_28` family, arbitrary multiple-root or square-cube edges, a
Keller pair, the GGV-to-Eggers-Wall functor, `G2-PSC`, `G2-BD`, or JC2.

**Method.** Rehashed the five charged artifacts, the four freeze-internal
lines, and every dependency pinned by R3. Independently constructed the
formal square-root branch in `K(X)[[t]]`; independently differentiated
`E(F,F^{3/2})` and `E(F,t^n F^\alpha)`; independently expanded the first
residual at weight `n` from `F_0=H^2` only; independently solved the
logarithmic ODE in `K(X)` by valuations at every finite place and at
infinity; independently traced denominators of every displayed mode;
independently expanded the weight-22 operator, the simple-root Laurent
leading term, the substitution `d=-Y/(2H)`, and the degree law for
`M`. Desk-scale exact arithmetic in `\mathbb Q[X]` and truncated series
in `\mathbb Q(X)[[t]]/(t^8)` were used as mutation guards, not as the
proof. Producer `PASS`, the Python tables, the completed R0/R1 reviews,
and the prior rootwise fixture `Y=X/48` were not used as evidence for
the exclusion. No AWS, no CAS, no producer-file edits, no
canonical-ledger edits, no `jc2-lean` access.

**Firewall.** The maximum permitted R3 verdict is: no polynomial-`X`
formal jet with this exact squarefree `H^2/H^3` leading edge and
`E=t^{22}+O(t^{23})` exists. A complete rational-mode normal form is not
a polynomial source/target cleanup. A square/cube leading face is not a
Keller jet.

---

## Verdict table

| Item | Verdict |
|---|---|
| Custody | **CONFIRMED** |
| Formal branch | **CONFIRMED** |
| Linearization | **CONFIRMED** |
| Mode `n=0`: `F^{3/2}` | **CONFIRMED** |
| Mode `n=4`: `t^4 F` | **CONFIRMED** |
| Mode `n=8`: `t^8 F^{1/2}` | **CONFIRMED** |
| Mode `n=12`: `t^{12}` | **CONFIRMED** |
| Mode `n=16`: `t^{16} F^{-1/2}` | **CONFIRMED** |
| Mode `n=20`: `t^{20} F^{-1}` | **CONFIRMED** |
| Rational-mode completeness | **CONFIRMED** |
| Negative-mode legitimacy | **CONFIRMED** |
| Endpoint coefficient | **CONFIRMED** |
| Denominator provenance | **CONFIRMED** |
| Pole lemma and mutation | **CONFIRMED** |
| `d=-Y/(2H)` | **CONFIRMED** |
| `M` identity | **CONFIRMED** |
| Degree obstruction | **CONFIRMED** |
| Exact theorem | **CONFIRMED** |
| Scope | **CONFIRMED** |

No item is **REFUTED**. No item is **GAP/REPAIR**. No smallest failing
mode, weight, pole, coefficient, field hypothesis, or omitted
denominator was found inside the charged R3 scope. The producer verifier
does not itself derive the square-root lift, the linearization, the mode
identity, the first-residual ODE, the valuation argument, or the pole
leading term; those were rederived here and survive.

---

## Independent hashes

Recomputed SHA-256, all matching the charged prompt and the internal
`FREEZE.sha256` lines:

```text
e1ed280ee1f5d7c997fe1ab6fdeaf40b689de71e1682ba8e13b1c4ba5047ae01
  cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/verify_r3.py
3d69dfbd6c0e28afafdfc7bbb0cf4ebe57d8522938ddd46b418f71123c1da006
  cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/RESULT_R3.json
06053fc175d1a7e212aecb23523bd91287fd33afe4ba181254e236995dc45216
  cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/README.md
b1851156c83657fa85eb875df7e191a99fd339bfcb79ca1a752742ddff9f70b7
  xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-sol-20260827.md
e752b86b5a8953649a3ce8c55379d18eca2dc1bdc8ab4fcd030c63dd64071823
  cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/FREEZE.sha256
```

Completed R1 hostile review, live digest (the charged prompt omitted the
final hex nibble `0`; the file is the R1 review named in that prompt):

```text
d40cd78f4f0afc12d09f8d1e99724de9fd5125fddc064089d6ca0870c7d777e0
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-r1-hostile-review-grok-20260827.md
```

R3 freeze pins, all matching the live bytes. These pins are custody only.
None of their mathematical conclusions is imported:

```text
MATCH  cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/FREEZE.sha256
       453f7821f88add5d97b65cee41fe3a4df225db5768526746cf4ff1431aa73aa6
MATCH  xmodel/ggv-8_28-keller-face-cusp-unit-carrier-classification-r2-sol-20260827.md
       0f8f3833c8fa16349d52c6d68829e5c86200ab064f84e4172b0ba4039314b733
MATCH  cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/verify_r2.py
       74c6c78e4faf527172703d5a115767562d89d9fa20868fc431dcc1f7cd258f15
MATCH  cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/RESULT_R2.json
       0dffbb36c20d0b80498d765168a47cdb9ed2889ffc7bd105dce7ec835f600b1d
MATCH  cases/ggv_8_28_keller_face_cusp_jet_pinning_r1_20260827/FREEZE.sha256
       05cbb5c046f9aa4b89e1104448e77fd38ec3a146d2422bf84773f81d668bfe3c
MATCH  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-hostile-review-grok-20260827.md
       171ff47c844331da8971a731c1ffaf20c31ed5b2ba86fdee2d0d81219eb002b0
```

Repository `HEAD` is still `418e413593120d19e15e6546eb50c985f4b1f038`.

A freeze-internal replay of `verify_r3.py` reproduces the frozen
`RESULT_R3.json` byte-for-byte. That is custody consistency only. It is
not evidence for any identity below.

---

## 1. Custody — CONFIRMED

All five charged digests match the prompt. The four lines inside
`FREEZE.sha256` match the four hashed producer files. All six R3 pins
match the live bytes.

R3 lives in a new directory and a new sol report. It does not rewrite
the R0 freeze, the R1 freeze, the R2 freeze, or the completed R0/R1
reviews. Additivity is intact.

R3 is genuinely distinct from R1 and from the unreviewed R2 claim. R1
proved `M(Y)=1` impossible inside two displayed polynomial ansatzes and
left typed-normal-form completeness open. R3 claims a complete
homogeneous classification of `E(F,\cdot)` on the differential ring
`K(X)[[t]]` through weight 21, including the negative-power modes
`t^{16}F^{-1/2}` and `t^{20}F^{-1}`, and then an endpoint pole reduction
for this exact squarefree edge. That is not a restatement of R1's two
ansatzes, and it does not consume any R2 local-carrier theorem.

Repository search for the six-mode display
`F^{3/2}, t^4 F, t^8 F^{1/2}, t^{12}, t^{16} F^{-1/2}, t^{20} F^{-1}`
hits only the charged R3 artifacts and the R3 review prompt. No prior
campaign object contains this normal form.

---

## 2. Formal branch — CONFIRMED

**Hypotheses, used as such below.** `K` is a field of characteristic
zero. `H=X^8-1\in K[X]`. `F,G\in K[X][[t]]` with `F_0=H^2` and
`G_0=H^3`. The ambient working ring for the proof is `K(X)[[t]]`, with
commuting derivations `\partial_X` and `\partial_t`. (The sol report's
phrase "differential field `K(X)[[t]]`" is nomenclature: `K(X)` is the
field, `K(X)[[t]]` is a differential integral domain. Every inversion
below is of a series whose constant term is nonzero in `K(X)`, so the
distinction is harmless.)

`H` is squarefree on this field: `H'=8X^7` and
`\gcd(X^8-1,X^7)=1` because any common divisor divides `1`. Characteristic
zero is load-bearing: in characteristic `2`, `H=(X^4-1)^2` is a square.

**Existence and uniqueness of `S=F^{1/2}` with `S_0=H`.** Write

```text
F = H^2 (1 + t W),    W = F_1/H^2 + t F_2/H^2 + \cdots \in K(X)[[t]].
```

`H^2` is nonzero in the field `K(X)`, so this is a unit times a
binomial series. In characteristic not `2`,

```text
(1 + t W)^{1/2} = \sum_{k\ge 0} \binom{1/2}{k} (t W)^k
```

is a well-defined formal series in `K(X)[[t]]`, uniquely determined by
having constant term `1`. Therefore

```text
S := H (1 + t W)^{1/2} = H + O(t)
```

exists uniquely in `K(X)[[t]]` through every finite order, in particular
through the charged order `22`. Equivalently, the recurrence

```text
S_0 = H,     2 H S_n = F_n - \sum_{i=1}^{n-1} S_i S_{n-i}  (n\ge 1)
```

divides by `2H` in `K(X)` at each step. Hensel lifting of `S^2-F=0` at
`S_0=H` is unique because `2S_0=2H` is a unit of `K(X)`.

The second formal square root is `-S`, with leading term `-H`. It is
excluded by the normalisation `S_0=H`, and independently by `G_0=H^3`:
`(-H)^3=-H^3\neq H^3` in characteristic not `2`. So the branch is forced
by the charged leading edge, not chosen for convenience.

**Nothing extra is smuggled.** The construction is purely formal: no
analytic radius, no convergence of `t`, no algebraic closure of `K`, and
no global polynomial square root. The coefficients `S_n` generally have
denominator a power of `H` (`S_1=F_1/(2H)` already), so `S` does not
lie in `K[X][[t]]` in general. Only the formal rational-function branch
is used.

An independent truncation with `F=H^2+t(3X+1)+t^2(X^2-5)` recovered
`S^2=F` through `t^8` in `K(X)[[t]]`, with `S_1=F_1/(2H)`. That check
is diagnostic only.

---

## 3. Linearization — CONFIRMED

`E` is linear in the second slot. Explicitly

```text
E(F,G) = 12 F_X G - 8 F G_X - t(F_X G_t - F_t G_X).
```

Put `R=G-F^{3/2}` in `K(X)[[t]]`. It is enough to check
`E(F,F^{3/2})=0`. Let `Q=F^{3/2}=F\,S`. The chain rule in this
differential ring gives

```text
Q_X = (3/2) F^{1/2} F_X,     Q_t = (3/2) F^{1/2} F_t.
```

Substitute:

```text
E(F,Q)
  = 12 F_X F^{3/2} - 8 F · (3/2) F^{1/2} F_X
    - t( F_X · (3/2) F^{1/2} F_t - F_t · (3/2) F^{1/2} F_X )
  = 12 F_X F^{3/2} - 12 F^{3/2} F_X
    - t · (3/2) F^{1/2} (F_X F_t - F_t F_X)
  = 0.
```

The first two summands cancel because `8·(3/2)=12`. The Jacobian block
cancels because `Q` is a composite of `F` alone. Component order and
the sign of the `t`-term match the charged generating function. As a
coefficient check, the same generating function expands to the recurrence

```text
E_n = \sum_{i+j=n} ((12-j) F_i' G_j + (i-8) F_i G_j'),
```

which is the standard `t^n` slice of the charged `E` and is not taken
from R0/R1. Thus `E(F,G)=E(F,R)`.

An independent truncation on the jet of §2 recovered
`E(F,F^{3/2})=0` through `t^7`. Diagnostic only.

---

## 4. Exact modes — CONFIRMED (all six)

Let `n\in\mathbb Z` and `α\in\mathbb Q`, and set `Z=t^n F^α` in
`K(X)[[t]]` whenever the formal power exists (binomial series of
`(1+tW)^α`, times `H^{2α}`). Then

```text
Z_X = t^n α F^{α-1} F_X,
Z_t = n t^{n-1} F^α + t^n α F^{α-1} F_t.
```

Substitute into `E`:

```text
E(F,Z)
  = 12 F_X t^n F^α - 8 F · t^n α F^{α-1} F_X
    - t[ F_X (n t^{n-1} F^α + t^n α F^{α-1} F_t)
         - F_t · t^n α F^{α-1} F_X ].
```

The two `α F^{α-1} F_X F_t` terms cancel, leaving

```text
E(F, t^n F^α) = t^n F^α F_X (12 - 8α - n).
```

This is an identity of formal series, not a sample. The kernel condition
is `12-8α-n=0`, i.e. `α=(12-n)/8`. The leading `X`-coefficient of
`Z` at `t=0` is `H^{2α}=H^{(12-n)/4}`. For this leading term to lie in
`K(X)` it is necessary that `(12-n)/4\in\mathbb Z`, because `H` is
squarefree (hence not a proper power in `K(X)`). For `0\le n<22` those
weights are exactly

```text
n=0,4,8,12,16,20.
```

Each charged mode:

| `n` | `α=(12-n)/8` | `Z` | leading `H`-power | `12-8α-n` |
|---|---|---|---|---|
| `0` | `3/2` | `F^{3/2}` | `3` | `0` |
| `4` | `1` | `t^4 F` | `2` | `0` |
| `8` | `1/2` | `t^8 F^{1/2}` | `1` | `0` |
| `12` | `0` | `t^{12}` | `0` | `0` |
| `16` | `-1/2` | `t^{16} F^{-1/2}` | `-1` | `0` |
| `20` | `-1` | `t^{20} F^{-1}` | `-2` | `0` |

**`n=0`.** Already the linearization. Forced by `G_0=H^3=S_0^3`.

**`n=4`.** Polynomial in `X` whenever `F` is. Independent truncation:
`E(F,t^4 F)=0` through `t^7`.

**`n=8`.** Uses the unique branch `S=H+O(t)`. Independent truncation:
`E(F,t^8 F^{1/2})=0` through `t^7`.

**`n=12`.** `Z=t^{12}` is independent of `F`. Directly
`12-8·0-12=0`.

**`n=16` and `n=20`.** These exist in `K(X)[[t]]` because `F_0=H^2` is
a *unit* of `K(X)`: it is not the zero rational function. Thus `F` is a
unit of `K(X)[[t]]`, with inverse `H^{-2}(1+tW)^{-1}`, and
`F^{-1/2}=S^{-1}=H^{-1}(1+tW)^{-1/2}`. They are exact zeros of `E` by
the same identity. Independent truncation through `t^7` recovered the
off-kernel identities `E(F,F^{-1})=20 F^{-1} F_X` and
`E(F,F^{-1/2})=16 F^{-1/2} F_X`, which are the `n=0` cases of the same
formula and confirm the signs of the negative exponents.

A non-mode check `E(F,t^3 F)=t^3 F F_X` (`12-8-3=1`) through `t^7`
guards the general coefficient `12-8α-n` against a dropped `n` or a
swapped `8α`.

---

## 5. Rational-mode completeness — CONFIRMED

Suppose a residual `D\in K(X)[[t]]` vanishes below weight `n`, so
`D=t^n r_n+O(t^{n+1})` with `r_n\in K(X)`. Write `F=H^2+t F_1+\cdots`.
Then, collecting `t^n` in `E(F,D)`:

- `12 F_X D` contributes `12·(2HH') r_n = 24 H H' r_n`;
- `-8 F D_X` contributes `-8 H^2 r_n'`;
- `-t F_X D_t` contributes `-t·(2HH')·n t^{n-1} r_n = -2n H H' r_n`;
- `+t F_t D_X` starts at order `n+1`, because `F_t=F_1+O(t)` has
  `t`-valuation `0` and the extra `t` pushes it to `n+1`.

Every positive-grade `F_k` likewise lands at order `\ge n+1`. Therefore

```text
E_n = (24-2n) H H' r_n - 8 H^2 r_n'
    = 2H \bigl( (12-n) H' r_n - 4 H r_n' \bigr).
```

`K(X)` is a field and `2H\neq 0`, so `E_n=0` if and only if

```text
(12-n) H' r_n - 4 H r_n' = 0.
```

The zero solution `r_n=0` is allowed. For `r_n\neq 0`,

```text
r_n'/r_n = \frac{12-n}{4} \frac{H'}{H}.
```

**Every nonzero rational solution is `r_n=c H^{(12-n)/4}` with `c\in K`.**
Write `H=\prod p_i` as a product of distinct monic irreducibles of
`K[X]` (squarefree), and write a nonzero `r\in K(X)` as
`r=c\prod q_j^{e_j}` in lowest terms. Logarithmic derivatives of distinct
monic irreducibles are linearly independent as rational functions (distinct
simple-pole supports). Matching

```text
\sum e_j q_j'/q_j = λ \sum_{p\mid H} p'/p,    λ=(12-n)/4,
```

forces: the only primes of `r` are the primes of `H`, and each exponent
equals `λ`. Valuations of rational functions are integers, so `λ\in\mathbb Z`
is necessary, and then `r=c H^λ`. Equivalently, at every root `α` of `H`
in an algebraic closure (each simple, because `H` is separable in
characteristic zero), the residue of `r'/r` is `v_α(r)` and the residue
of `H'/H` is `1`, hence `v_α(r)=λ` at every such root and `v_β(r)=0` at
every other finite place. No extra finite prime, and no different
constant on a proper factor of `H`, can occur. At infinity,
`v_\infty(H)=-8` automatically gives `v_\infty(r)=-8λ`, so there is no
further constraint and no extra polynomial factor. In characteristic
zero, `{f\in K(X): f'=0\}=K`, so `c` is a constant of `K`, not a
nonconstant with vanishing derivative.

**Squarefree `H` permits a nonzero rational solution exactly for
`n\equiv 0\pmod{4}`.** That is the condition that `λ=(12-n)/4` is an
integer. For `0\le n\le 21` this is `n=0,4,8,12,16,20`. Non-integral
`λ` (in particular `λ=5/2` at `n=2`, `λ=-5/2` at `n=22`, `λ=k/4` with
`k` odd) would require `r` in a ramified extension of `K(X)`, which is
outside the coefficient field of a polynomial-`X` jet. Zero-divisors do
not arise: the ambient rings `K(X)` and `K(X)[[t]]` are integral
domains.

**Induction through weight 21.** Start from `R=G-F^{3/2}`, whose
constant term vanishes by `G_0=H^3`. Assume the residual has been
cleaned below weight `n<22`. If `n` is not in `{4,8,12,16,20}`, then
`E_n=0` forces `r_n=0`. If `n` is in that list, then `r_n=c_n H^λ`, and
subtracting the *full* exact mode `c_n t^n F^{(12-n)/8}` kills the
leading term, introduces no lower `t`-terms, and does not change `E` at
any weight (the mode is an exact zero, including all higher coefficients
of `F` that the mode carries). The next residual again starts at a
single weight. There is no leftover interaction among modes: they are
supported at distinct lowest weights, so the constants `c_n` are unique.
Higher `F_k` never contribute to the *first* residual equation, and
after a mode is subtracted they are absorbed into later coefficients of
`D` rather than into a second kernel at the same weight.

Thus, after the five positive subtractions,

```text
G = F^{3/2} + c_4 t^4 F + c_8 t^8 F^{1/2} + c_{12} t^{12}
    + c_{16} t^{16} F^{-1/2} + c_{20} t^{20} F^{-1}
    + t^{22} d + O(t^{23})
```

in `K(X)[[t]]`, with `d\in K(X)` and `c_n\in K`. This is a
differential-ring identity, not a polynomial source transformation.

---

## 6. Negative-mode legitimacy — CONFIRMED

The modes at `n=16,20` are not polynomial in `X`, and the sol report
does not claim they are. They are exact elements of `\ker E(F,\cdot)`
inside `K(X)[[t]]`. Subtracting them is legitimate for a contradiction
that starts from polynomial `F,G`, for three independent reasons.

1. `K[X][[t]]\subset K(X)[[t]]`. Any polynomial-`X` jet is a
   rational-coefficient jet. A proof that no jet of the latter class
   with the charged leading edge and the charged `E` exists is a proof
   that no polynomial sub-jet exists.
2. `F_0=H^2` is a unit of `K(X)`, so `F^{\pm 1}` and `F^{\pm 1/2}` exist
   as formal series. One is not inverting a series with vanishing
   constant term, and one is not passing to a meromorphic Laurent series
   in `t`.
3. `E` is linear in the second slot and vanishes on each mode, so
   `E(F,G)=E(F, t^{22}d+O(t^{23}))` as an identity in `K(X)[[t]]`. The
   original `F,G` remain polynomial; only the comparison object is
   rational.

High-order `H`-poles in the *tails* of `F^{-1/2}` and `F^{-1}`
(already `[t^1]F^{-1/2}=-F_1/(2H^3)` may be a triple pole) are absorbed
into later coefficients of `D`, including `d`. They do not invalidate
the subtraction. If those tails failed to cancel in `d` down to simple
poles, the pole lemma of §8 would already contradict regularity of
`E_{22}=1`. Either cancellation occurs, or the jet is impossible even
before the degree obstruction. Both branches exclude the charged edge.

---

## 7. Endpoint coefficient — CONFIRMED

After the five positive modes are subtracted, `D=t^{22}d+O(t^{23})`.
The general first-residual formula of §5 at `n=22` is

```text
E_{22} = 2H\bigl((12-22)H'd - 4 H d'\bigr)
       = -20 H H' d - 8 H^2 d'.
```

Lower `D` is absent by the induction. Positive-grade `F_k` contribute
only to `t`-weight `\ge 23`: the dangerous-looking block `t F_t D_X`
starts at `t^{23}`, and `t F_{k,X} D_t` with `k\ge 1` likewise starts at
`t^{23}`. The integer `22` is load-bearing: it is the first weight past
the last rational mode `n=20`, and it is the charged vanishing order of
`E`. The target `E=t^{22}+O(t^{23})` means the coefficient of `t^{22}`
is the constant polynomial `1`, so

```text
-20 H H' d - 8 H^2 d' = 1
```

in `K(X)`. Signs match the expansion `(24-2n)=24-44=-20` and `-8`.

---

## 8. Denominator provenance — CONFIRMED

`d=[t^{22}](G-\sum\text{modes})`. `G_{22}` is polynomial. Each mode
coefficient is built from polynomial `F_i` by the operations of §2 and
§4:

- `F` itself, `t^4 F`, and `t^{12}` are polynomial in `X`;
- `S=F^{1/2}` divides by `2H` at each recurrence step, and products of
  previous `S_i` preserve `H`-denominators;
- `F^{3/2}=F S` multiplies by a polynomial;
- `F^{-1}` is `H^{-2}(1+tW)^{-1}`, geometric series in `W` whose
  coefficients have denominators powers of `H`;
- `F^{-1/2}=S^{-1}` divides by `H` at each recurrence step.

Binomial coefficients of `(1+tW)^α` for `α\in\{3/2,1,1/2,0,-1/2,-1\}`
contribute only integers and powers of `2`, invertible in characteristic
zero, not new finite primes in `X`. Cancellation of numerator and
denominator can only *remove* poles. Therefore every finite denominator
of `d` divides a power of `H`.

Independently of this trace, regularity of `E_{22}=1` already forbids
poles off `H=0`. At a place `q` with `v_q(H)=0` and `v_q(d)=-m`, `m\ge 1`,
one has `v_q(-20 H H' d)=-m` while `v_q(-8 H^2 d')=-m-1` in characteristic
zero (`d'` drops the order by exactly one). The `d'` term is strictly more
polar and cannot cancel, so `E_{22}` would pole at `q`. Thus even a
failure of the mode-trace would still force finite poles of `d` to lie
along `H`. No omitted denominator was found.

---

## 9. Pole lemma and mutation — CONFIRMED

Let `c` be a simple root of `H` (or, equivalently, work at an irreducible
`p\mid H`, which is separable). Locally `H` is a uniformizer times a
unit. Write

```text
d = a H^{-m} + O(H^{1-m}),    a(c)\neq 0,
```

as a local expansion at `c`; different roots may have different `m`. Then

```text
d' = a' H^{-m} - m a H' H^{-m-1} + \cdots.
```

The `a'` contribution to `E_{22}` is `-8 H^2 a' H^{-m}`, of order
`H^{2-m}`, which is strictly milder than `H^{1-m}` for the leading polar
part. The two leading terms are

```text
-20 H H' · a H^{-m} = -20 a H' H^{1-m},
-8 H^2 · (-m a H' H^{-m-1}) = 8 m a H' H^{1-m}.
```

Sum: `(8m-20) a H' H^{1-m}`. At a simple root `H'(c)\neq 0`, and `a(c)\neq 0`,
so the leading polar term vanishes if and only if `8m-20=0`, i.e.
`m=5/2`. Two distinct Laurent terms at the same place cannot cancel this
leading coefficient: it is the unique lowest-order coefficient. Poles at
distinct roots cannot cancel each other.

`m=5/2` is not the order of a rational function at a simple zero of
`H`. For integer `m\ge 2`, `8m-20\neq 0` (`m=2` gives `-4`). Regular
`E_{22}=1` therefore forbids `m\ge 2` at every root, i.e. `m\le 1`.

**Target-weight mutation.** The same leading scalar at a general weight
`n` is `2(12-n+4m)`, the coefficient of `a H' H^{1-m}` in
`2H((12-n)H'r-4H r')`. At `n=20`, `m=2`: `2(12-20+8)=0`, recovering the
exact mode `t^{20} F^{-1}\sim t^{20} H^{-2}`. At the charged `n=22`,
`m=2`: `2(12-22+8)=-4\neq 0`. Target `20` would admit a double-pole
homogeneous solution in `K(X)`; target `22` does not. The scalar `-4` at
`(n,m)=(22,2)` matches `8·2-20=-4`.

---

## 10. `d=-Y/(2H)` — CONFIRMED

`d` has no finite poles off `H` (§8) and at most simple poles along
`H` (§9). `H` is squarefree, so the denominator of `d` in lowest terms
divides `H`. Clearing the missing factors of `H` into the numerator
gives `d=P/H` for some `P\in K[X]`. Characteristic not `2` lets us set
`Y=-2P\in K[X]`, i.e.

```text
d = -Y/(2H).
```

The polynomial part of `d` (numerator degree `\ge 8`) is included: `Y`
is allowed to have any degree. Behaviour at infinity is that of a
rational function, hence a finite pole order, already encoded by
`\deg Y`. No extra generator at infinity is needed.

---

## 11. `M` identity — CONFIRMED

From `d=-Y/(2H)`,

```text
d' = -Y'/(2H) + Y H'/(2 H^2).
```

Substitute:

```text
E_{22}
  = -20 H H' · (-Y/(2H)) - 8 H^2 · (-Y'/(2H) + Y H'/(2 H^2))
  = 10 H' Y + 4 H Y' - 4 H' Y
  = 4 H Y' + 6 H' Y.
```

Define `M(Y):=4 H Y'+6 H' Y`. Then `E_{22}=M(Y)`, and the charged
endpoint is `M(Y)=1`. The factor `2` in `d=-Y/(2H)` is a normalisation
that matches this operator; any other constant multiple would only
rescale `Y`.

The identity was recomputed on dense polynomials in `\mathbb Q[X]`
(including `(3,-2,5,7)` and `(1/3,0,-5/7,11,0,2)`) as a mutation guard.
The proof is the substitution above.

**Fixture, as a mutation/consistency check, not as evidence.**
`Y=X/48` has `Y'=1/48`, so

```text
M(X/48) = 4 H · (1/48) + 6 H' · (X/48)
        = H/12 + (1/8) X · 8 X^7
        = H/12 + X^8
        = H/12 + (H+1)
        = 1 + (13/12) H.
```

The two polynomials are identical in `\mathbb Q[X]`, coefficients
`(-1/12,0,0,0,0,0,0,0,13/12)`. This is the same remainder that R0/R1
attached to a rootwise interpolant; R3 does not use that interpolant as
a hypothesis. It is recorded only because the charged artifacts display
it and because it is an exact evaluation of the operator just derived.

---

## 12. Degree obstruction — CONFIRMED

Let `H=X^8-1`, so `\deg H=8`, `H'=8X^7`, `\mathrm{lc}(H')=8`. Treat
`Y=0` separately: `M(0)=0\neq 1`.

Now let `Y` be nonzero of degree `d\ge 0` with leading coefficient
`\ell\neq 0`.

- If `d=0`, then `Y' = 0` and `M(Y)=6 H' Y` has degree `7=d+7` and
  leading coefficient `48\ell=(4·0+48)\ell`.
- If `d\ge 1`, then `4 H Y'` has degree `d+7` and leading coefficient
  `4 d \ell`, while `6 H' Y` has degree `d+7` and leading coefficient
  `48\ell`. There is no cancellation of top terms:
  `4d\ell+48\ell=4(d+12)\ell`.

In characteristic zero, `4(d+12)\neq 0`. Thus for every nonzero
polynomial `Y`,

```text
\deg M(Y) = d+7,     \mathrm{lc}\, M(Y) = (4d+48)\,\mathrm{lc}(Y).
```

In particular `\deg M(Y)\ge 7 > 0=\deg(1)`, so `M(Y)` cannot be the
constant polynomial `1`. This holds over every characteristic-zero field:
such a field contains `\mathbb Q`, and a product of nonzero elements is
nonzero. No splitting of `H`, no algebraic closure, and no analytic
hypothesis is used.

The mechanical monomial loop `Y=X^d` for `d=0..64` in the verifier is
not the proof. The leading-coefficient identity is algebraic and holds
for every `d`. Independent evaluation on `d=0..19` and on a dense degree
`5` polynomial with leading coefficient `-1/4` recovered
`\mathrm{lc}= (4·5+48)·(-1/4)=-17` and degree `12`. Diagnostic only.

---

## 13. Exact theorem — CONFIRMED

Assembling §§2–12: if a polynomial-`X` formal jet with `F_0=H^2`,
`G_0=H^3`, and `E=t^{22}+O(t^{23})` existed over a characteristic-zero
field, the unique branch `S=H+O(t)` would put `G` into the displayed
rational normal form, the endpoint coefficient `d` would satisfy
`M(Y)=1` for a polynomial `Y`, and no such `Y` exists. Contradiction.

The maximum permitted conclusion is exactly the charged theorem: there
is no such jet. The argument never uses later `2S/3S` support, so
adding more raw coefficients cannot repair *this* leading edge. It also
never uses a polynomial-source normal form: the negative modes are proof
terms in `K(X)[[t]]`.

---

## 14. Scope — CONFIRMED

The charged artifacts claim, and only claim, the exclusion of a
polynomial-`X` formal jet with

```text
F0 = (X^8-1)^2,    G0 = (X^8-1)^3,    E = t^{22} + O(t^{23}).
```

That is the exact squarefree Keller-compatible replacement edge used as
a fidelity control, not the original non-Keller witness
`F_0=X^{16}-1`. The sol report, README, `RESULT_R3.json` `scope` field,
and `claims_not_made` list all stay inside this firewall. They do not
claim:

- exclusion of the original non-Keller `8_28` control, or of the whole
  GGV `8_28` family;
- exclusion of multiple-root or non-squarefree square-cube edges (the
  pole lemma and the integrality of `λ` both use squarefreeness);
- construction of a Keller pair;
- the GGV-to-Eggers-Wall functor;
- `G2-PSC`, `G2-BD`, a counterexample, or JC2.

The status string
`PASS-R3-SQUAREFREE-H2-H3-RATIONAL-MODE-EXCLUSION` is bounded by those
disclaimers and does not enlarge the theorem. Completeness is
completeness of `\ker E(F,\cdot)` on `K(X)[[t]]` through weight 21, not
a typed polynomial-source normal form and not a family exclusion.

Maximum permitted verdict, and the verdict reached: **no
polynomial-`X` formal jet with this exact squarefree `H^2/H^3` leading
edge satisfies `E=t^{22}+O(t^{23})`.**

---

## Replay note

The producer command

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/verify_r3.py
```

reproduces frozen `RESULT_R3.json`. That replay was used only as freeze
consistency. Every identity above was rederived independently in
`K(X)[[t]]` and in `\mathbb Q[X]`. Truncated series through `t^8` and
the monomial degree law were used only as sign/coefficient guards.
