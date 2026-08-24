# Hostile different-model review — TD6 centered global compatibility control

| Field | Value |
|---|---|
| Claim under review | Frozen TD6-GLOBAL-COMPATIBILITY-GATE: bare-chart monomial divisibility obstruction versus LR2-legal centering `T=xy^4-y^3`; explicit SP-2-rectangle polynomial jets with the D73 equality mechanism; one-sided `Q[T][[x]]` recursion; STOP of the bare-divisibility attack with no class kill or realization |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Hidden local-to-global step | none: finite one-sided jets are not promoted to a Keller pair, a class realization, or a two-chart exact-`J` theorem |
| Evidence tier | independent exact algebra over `Q` (producer replay plus a second sparse engine that does not import it); hand chart 2-forms, Jacobian factorisation, Lagrange inversion, Bezout identity, and special-fiber Puiseux; primary-source read of Sigray printed pp. 6, 10–18, 35–38 and committed LR2/SP-2 ledger text |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T09:20:00Z – 2026-08-24T09:50:00Z |
| Python | 3.14.6; stdlib `fractions.Fraction` / `math` only |
| Host | Darwin arm64 |

Producer inputs reread in full before any verdict:

- `xmodel/td6-global-compatibility-gate-20260824.md` (SHA-256 `b53064c877a4f0b741f23f036b2323195bef825ccc72b6722b98f1fc2d2eec17`)
- `cases/td6_global_compatibility_20260824/replay.py` (SHA-256 `d5d0d4d4209ef115b952571082c37252eb0f1e032e02f182cdccf516b29519d9`)

Both frozen hashes match the launch prompt. The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. No producer, canonical, ladder, or PDF file was edited. No D43 or new-book search was launched.

Cited sources reread against that basis:

- `xmodel/d73-strict-or-equality-20260824.md` SHA-256 `90546ffb50b5cf8325195dc04a4e39b550e4075c057049529e29d8d188b698de`
- `xmodel/d73-strict-or-equality-review-grok-20260824.md` SHA-256 `3c0df2009432646bc6b93fa36f4c688b24af9e8df22629755303e89fde0fac3a`
- `ladder/SHEET6.md` SHA-256 `50b4dc45bf091af35a481fead04b7f8f5b120008e97065bf0a5f80ff4ef7b4e3`
- `ladder/SHEET6-CAMPAIGN.md` SHA-256 `fca34f4cad606c9097cdb87c4e9e51609ab5c73d16a03efd764a7c06cdc4ccbb`
- `ladder/SHEET6-LROOT.md` SHA-256 `17b3875e98e31c09f8c8810a942d2d8424af07033c6d5af89d56f665377334d9` (lines 136–158, 172–200, 234–271)
- `ladder/SHEET6-LT-REVIEW.md` SHA-256 `82d94e1a43ae9ec315189b4892faafa840027f4f1696dba6a394866331aa22c6` (lines 66–73, 90–110)
- `refs/sigray_full.pdf` SHA-256 `9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae`: Statement 3.1 forms (3)–(4); Definitions 3.1–3.4; Notations 3.5, 3.8–3.10; Proposition 3.1; Notation 1.5; Notation 7.1 / Statement 7.1; Proposition 7.3 printed pp. 36–38

All seven charged input hashes in the producer header match the files on disk.

**Formatting erratum (non-blocking).** Displayed equation (8) is missing the backslash before `left` on both lines: the raw text is `-left(` and is intended to be `-\left(`. The matching `\right)` is present. Recovered polynomials from the replay (and from the intended LaTeX after the missing backslash is restored) are

```text
f6 = T^{15} + (1/3) x^3 - (T + (25/27) T^9) x^6
g6 = T + T^{25} + (5/9) T^{10} x^3 - ((5/3) T^{11} + (125/81) T^{19}) x^6
```

No mathematical mismatch with the code, with the canonical recursion coefficients `A_6`, `B_6`, or with any numbered identity. A second purely typographical omission is the missing closing `\]` after tag (10). Neither erratum is load-bearing.

**Promotion.** Accept as `CENTERING-ESCAPE / FINITE-JET-CONTROL / STOP` of the *bare-divisibility* attack on SP-2 only. Bank the centered coordinate `T=xy^4-y^3` and the two explicit rectangle-respecting jets. Promote nothing else.

**Quarantine.** Neither displayed pair is Keller. No terminal class is killed or realized. The two-chart, fixed-rectangle, exact-`J=1` gate named in producer §5 remains open.

---

## Headline and subclaim table

Write `s=y^{-1}`, `u=xy-1`, `T=xy^4-y^3=y^3 u`, and in the centered chart `x=s+t s^4`, `y=s^{-1}` (so `T=t` and `u=t s^3` identically).

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Bare-chart monomial divisibility: if `h∈Q[x,y]` is holomorphic at `s=0` in `x=t s^R`, `y=s^{-1}` (`R≥2`), the coefficient of `s^k` (`k>0`) is divisible by `t^{⌈k/R⌉}`, hence `h_s(s,0)=0`. If both members of a polynomial Keller pair were holomorphic in that same chart, `(f_s g_t-f_t g_s)(s,0)=0`, contradicting `dx∧dy=s^{R-2} ds∧dt` | **CONFIRMED** | a holomorphic monomial with `Ri-j=k>0` and `i<⌈k/R⌉`; chart 2-form `s^{R-2}` failing; Jacobian contradiction requiring only one of `f,g` holomorphic |
| 2 | LR2/Sigray typing of SP-2 permits a shared unramified `y^{-1}` truncation with no split or characteristic exponent below height four; `T=xy^4-y^3` is exactly Sigray's Eggers coordinate at `π=4` after that truncation, and equals the chart variable `t` identically | **CONFIRMED** | a printed LR2 clause forcing the shared integer coefficients below height 4 to vanish; `y^{-1}` creating a characteristic exponent or a `V_2` split; `η_G` not equal to `y^4(x-y^{-1})` |
| 3 | The pair `(f_3,g_3)` lies in the SP-2 rectangles with height-four patterns `T^{15}` and `T+T^{25}`; exact `J=(1+u)^2(1+4u)(1+(50/9)T^9 x^3)`; centered valuation of `J-1` equals 3; special fiber has three branches, contact `21/5`, `∑Λ=3=π(G)-1`; not a Keller realization | **CONFIRMED** | `J` identity failing; `gcd(3,15)≠3`; `ord_T(g_3|_{f_3=0})≠1`; pairwise contact collapsing under `μ_5`; `J` identically 1 |
| 4 | Recovered `(f_6,g_6)` stay in the same rectangles with the same corners and patterns; centered valuation of `J-1` is exactly six; no stronger fixed-rectangle order is asserted | **CONFIRMED** | a monomial of `f_6` with `i>15` or `j>60`; of `g_6` with `i>25` or `j>100`; `s^3,s^4,s^5` terms in `J_6-1`; a producer claim that `n=9` remains inside the rectangles |
| 5 | Formal theorem in `Q[T][[x]]`: Keller equation is `F_x G_T-F_T G_x=x^2 u'(T x^3)`; coefficientwise linear equation with Bezout identity `q'-(5/3)T^{10} p'=1`; char-0 divisions by `n`; arbitrary finite solvability; truncation `J=1+O(x^{N-2})`; composition back to `Q[x,y]`; `Q[T,x]` is a strict subring of the polynomial-origin completion; degrees grow | **CONFIRMED** | `φ'(0)≠1`; `p',q'` not coprime; a characteristic-`p` obstruction presented as char-0; `xy=1+u(Tx^3)` lying in `Q[T,x]`; `A_9` of `T`-degree `≤9` after composition staying in `i≤15` |
| 6 | Scope: one-sided, cap-dropped, finite-order, no convergence/algebraization/opposite-side chart. Validly stops the bare-divisibility attack; kills or realizes no td6 class; leaves the two-chart fixed-rectangle exact-`J` gate open | **CONFIRMED** | the producer promoting a class kill, a polynomial Keller pair, exact `J=1`, or a two-chart theorem |

All remarks below are non-blocking unless marked otherwise. None changes a Jacobian, a valuation, a Bezout identity, a rectangle, or a verdict.

---

## Replay

Registered command, rerun unmodified from the charged tree:

```sh
python3 cases/td6_global_compatibility_20260824/replay.py
```

Exit code 0. Printed verdict:

```text
TD6 global-compatibility replay: PASS
bare divisibility monomials checked: 1326
f6 support terms / rectangle: 29 / (15,60)
g6 support terms / rectangle: 63 / (25,100)
J3-1 centered s-valuation: 3
J6-1 centered s-valuation: 6
formal recursion through X^18 nonzero coefficient levels: [(3, 0, 10), (6, 9, 19), (9, 10, 20), (12, 11, 21), (15, 12, 22), (18, 13, 23)]
```

Arithmetic is `fractions.Fraction` on sparse monomials. No CAS, no floating point, no import of D73 code.

A second engine, written for this review and not imported from the registered script, recomputed every polynomial identity the registered script actually computes, plus: the chart 2-form exponent; `T=y^3 u`; the hand factorisation of `J(f_3,g_3)` through the `(x,T)` Jacobian; the exact leading `s^3` coefficient `6t+(50/9)t^9` of `J_3-1`; vanishing of `s^0` through `s^5` in `J_6-1` with nonzero `s^6` coefficient `-45 t^2-50 t^{10}-(1250/27) t^{18}`; Lagrange inversion of `u(1+u)^3=w` through order 12; the unreduced Bezout particular solution `A_n=\mathrm{rhs}`, `B_n=(5/3)T^{10}\mathrm{rhs}` through `n=12`; and the composed supports of `T^9 x^6`, `T^{10} x^9`, `T^{20} x^9`. It recorded 52 exact identities and zero failures.

---

## 1. Bare-chart monomial divisibility and Jacobian contradiction

Chart and inverse, as written:

```text
x = t s^R,     y = s^{-1},     R ≥ 2.
```

A monomial of a polynomial is `x^i y^j = t^i s^{R i-j}` with `i,j ≥ 0`. Holomorphy at `s=0` forces every exponent `k=R i-j` to be nonnegative. For `k>0` one has `i ≥ k/R`, and `i` is an integer, so `i ≥ ⌈k/R⌉`. The coefficient of `s^k` is therefore a polynomial in `t` divisible by `t^{⌈k/R⌉}`. That is (2).

Consequences at `t=0`. For `k>0`, `⌈k/R⌉ ≥ 1`, so every positive `s`-power vanishes. The `k=0` summand is `∑_i a_{i,R i} t^i`, which at `t=0` retains only the constant term. Hence `h(s,0)` is constant and `h_s(s,0)=0`.

Chart 2-form, by hand:

```text
dx = s^R dt + R t s^{R-1} ds,
dy = -s^{-2} ds,
dx ∧ dy = s^R (-s^{-2}) dt ∧ ds = s^{R-2} ds ∧ dt.
```

The `ds` summand of `dx` wedges to 0 against `dy`. For a Keller pair, `df∧dg=dx∧dy`, so `J_{s,t}(f,g)=s^{R-2}`. If both `f` and `g` were holomorphic in this same chart, then `f_s(s,0)=g_s(s,0)=0`, hence `(f_s g_t-f_t g_s)(s,0)=0`, contradicting `s^{R-2}≠0` for `s≠0`. Both members are required: a single vanishing `f_s` leaves `-f_t g_s` possibly nonzero.

The lemma is therefore exact under its stated hypothesis. Independently, every holomorphic monomial in the SP-2 window `0≤i≤25`, `0≤j≤100` at `R=4` satisfies the divisibility (1,326 such monomials, of which those with `k>0` all have `i≥⌈k/4⌉`); the same check holds for `R=2..8` on a larger window.

The D73 germ `f=t^{15}+s^3/(3q'(t))` is diagnosed by (2): its `s^3` coefficient is `1/(3q'(t))`, equal to `1/3` at `t=0`, not divisible by `t^{⌈3/4⌉}=t`. It cannot be the chart expansion of a polynomial in the *bare* coordinates. That diagnosis is local to the zero-truncation chart `t=xy^4` and is not inherited by a centered chart (Claim 2).

---

## 2. Sigray / LR2 typing and the centered variable `T`

Committed `SHEET6-LROOT.md:143-158` (Lemma LR2): every survivor-class carrier has exactly one x-side cv vertex `G` with `κ_G=1` and `π_G ∈ [R, R+\mathrm{slack}]`; equivalently, all `l_f` x-side Puiseux series form a single cluster (pairwise contact `≥ π_G ≥ R`) with no characteristic exponent below `π_G`. Slack-0 forces `π_G=R` and both patterns unsplit below `G`. SP-2 is slack-0 with `R=4`, `(k_f,l_f)=(60,15)`, `(k_g,l_g)=(100,25)` (`LROOT:175, 187-200`). LT-REVIEW:66-73 re-derives the same pin.

Sigray, printed p. 10, form (4): x-side punctures have `y(P)=∞`, `x(P)∈C`, and

```text
x = ∑_{j≥0} c_j y^{-j/κ},
```

`κ` the multiplicity of `y` at `P`. Definition 3.1: `e_0=κ` and `β_1` is the least `j` with `c_j≠0` *and* `j` not divisible by `e_0`. A term `y^{-1}` has index `j=κ`, which is divisible by `e_0`. It is therefore never a characteristic exponent, for any pole order `κ`. The same holds for every integer power `y^{-m}`. A coefficient shared by every series in the cluster does not produce a `V_2` vertex (Definition 3.2: `O(P,P*)` is the first *differing* exponent; Definition 3.4). LR2's "no characteristic exponent / no split below height four" therefore permits a common truncation

```text
x = c_1 y^{-1} + c_2 y^{-2} + c_3 y^{-3} + c_4 y^{-4} + (terms of order > 4),
```

and does *not* pin `c_1=c_2=c_3=c_4=0`. A constant `c_0` is removable by the polynomial translation `x↦x-c_0`. A `y^{-1}` term is not: the shear `x↦x-y^{-1}` is not polynomial, and a polynomial shear `x↦x+p(y)` with `p≠0` sends `x→∞` as `y→∞`, destroying form (4).

Notation 3.9, y-side, printed p. 13:

```text
η_F = x^{π(F)} ( y - ∑_{j<π(F)} c_j x^{-j} ).
```

The x-side analogue, which the same notation says "can be defined the same way" for `F∈T_{x,a}`, is

```text
η_F = y^{π(F)} ( x - ∑_{j<π(F)} c_j y^{-j} ).
```

At `π(G)=4` with the legal shared truncation `c_1=1` and all other `c_j=0` for exponents `<4`,

```text
η_G = y^4 (x - y^{-1}) = x y^4 - y^3 = T.
```

In the chart `x=s+t s^4`, `y=s^{-1}` one has `T=t` identically (independent engine: the substituted Laurent polynomial equals `t`). So `T` is both Sigray's Eggers coordinate after this truncation and a global polynomial. D73 chose the zero truncation, for which `η_G=y^4 x`. That choice is a gauge not supplied by LR2.

Two source-alignment notes, neither load-bearing.

- The producer's phrase "for the D73 pole order five it is the index 5, divisible by `e_0=5`" is special-fiber language. On a generic x-side puncture of a polynomial pair one typically has `κ=1`, in which case `y^{-1}` has index 1, still divisible by `e_0`. Either way the term is unramified. `κ_G=κ/e_0=1` at `j=0` (Notation 3.5, printed p. 12) is automatic once there is no characteristic exponent below height 4.
- Opposite-side r9/M2 templates are not used and are not claimed to be used. They remain free to pin `φ` in a successor. That is the two-chart gate of producer §5, not a hole in the present typing.

The Newton-slope `k_f/l_f=4` is the height at which `d_F` vanishes along the x-ray, not a requirement that the first Puiseux exponent of `x` be 4. A polynomial in the SP-2 rectangle *may* have leading Puiseux exponent 1 with first difference at exponent 4: that is exactly a slope-1 cancellation along `xy=1`, which `T=y^3(xy-1)` organises. No printed LR2 or Sigray clause forbids it.

Claim 2 is therefore established at the point the launch prompt flags as the GAP trigger. No GAP is returned.

---

## 3. The first jet `(f_3,g_3)`

```text
f3 = T^{15} + (1/3) x^3,
g3 = T + T^{25} + (5/9) T^{10} x^3.
```

**Supports.** `T^{15}=(xy^4-y^3)^{15}` has terms `(15-k,60-k)` for `k=0..15`, plus the extra monomial `x^3`. Seventeen terms, all inside `i≤15`, `j≤60`, corner coefficient `f3[(15,60)]=1`. For `g3`: `T` contributes `(1,4)` and `(0,3)`; `T^{25}` contributes `(25-k,100-k)` for `k=0..25`; `T^{10} x^3` contributes `(13-k,40-k)` for `k=0..10`. These three blocks are disjoint (independent exponent comparison). Thirty-nine terms, all inside `i≤25`, `j≤100`, corner coefficient `g3[(25,100)]=1`.

**Exact Jacobian, two paths.** Path A: sparse `∂/∂x,∂/∂y` on the composed polynomials, matching the expanded right-hand side of (6). Path B, by hand in `(x,T)`:

```text
∂f/∂x|_T = x^2,          ∂f/∂T|_x = 15 T^{14},
∂g/∂x|_T = (5/3) T^{10} x^2,
∂g/∂T|_x = q' + (50/9) T^9 x^3,
q' = 1 + 25 T^{24}.
```

```text
J_{x,T} = x^2 q' + (50/9) T^9 x^5 - 25 T^{24} x^2 = x^2 (1 + (50/9) T^9 x^3).
```

Times `det ∂(x,T)/∂(x,y)=y^2(1+4u)` (itself `T_y`, since `∂x/∂y=0`) and using `x y=1+u` gives (6) exactly:

```text
J(f3,g3) = (1+u)^2 (1+4u) (1 + (50/9) T^9 x^3).
```

This is visibly nonconstant, so the pair is not Keller.

**Centered valuation.** In the chart, `u=t s^3` and `T=t` hold identically, and `x=s(1+t s^3)`. Then

```text
J = (1+t s^3)^2 (1+4 t s^3) (1 + (50/9) t^9 s^3 (1+t s^3)^3)
  = 1 + (6t + (50/9) t^9) s^3 + O(s^6).
```

Independent substitution of the expanded polynomial `J-1` gives s-valuation exactly 3, with leading coefficient exactly `{t^1: 6, t^9: 50/9}`. So `J=1+O(s^3)` as claimed, and the order is sharp.

**Special fiber.** On `f3=0` one has `x^3=-3 T^{15}` as an identity of functions on the fiber, hence

```text
g3 = T + T^{25} + (5/9) T^{10} (-3 T^{15}) = T - (2/3) T^{25}.
```

`gcd(3,15)=3` branches `x=ρ T^5`, `ρ^3=-3`. The identity `T x^3=u(1+u)^3` becomes `u(1+u)^3=-3 T^{16}`. Formal IFT at `u=0` (`φ'(0)=1`) gives a unique series `u=-3 T^{16}+O(T^{32})`. Then `y=(1+u)/x=ρ^{-1} T^{-5}(1+u)`, so each branch has `y`-pole order 5. Inverting,

```text
x = y^{-1} (1+u) = y^{-1} + O(T^{21}) = y^{-1} + C_ρ y^{-21/5} + ⋯.
```

The leading `y^{-1}` is independent of `ρ`. The coefficient of `y^{-21/5}` scales as `ρ^{-16/5}`. The ratio of two cube-root branches is a nontrivial 15th root of unity, not in `μ_5`, so a reparametrization of `y^{-1/5}` cannot identify them. Pairwise contact is exactly `21/5>4`. On each branch `g3=T(1-(2/3)T^{24})` has `T`-order 1, hence `Λ(P)=1` (Sigray Notation 1.5, printed p. 6). With suitable denominator 5, Proposition 7.3's set `R*_0` is `{P: I_P(4+1/5)=G*0}`; the missing `y^{-4}` coefficient is the direction `c=0`, and Definition 3.3's clause `u≤O(P,P')` at `u=21/5` puts all three normalized points in `R*_0`. Thus `∑Λ=3=π(G)-1`. This is the D73 equality mechanism, now with polynomial origin, and it is not a polynomial Keller realization.

Height-four patterns after centered substitution: the `s^0` parts are exactly `t^{15}` and `t+t^{25}` for both this pair and the second jet.

---

## 4. The second jet `(f_6,g_6)`

Recovered from the replay and from intended (8) after restoring the missing backslash; they agree, and they agree with the canonical recursion coefficients `A_6=-T-(25/27)T^9`, `B_6=-(5/3)T^{11}-(125/81)T^{19}`:

```text
f6 = f3 - (T + (25/27) T^9) x^6,
g6 = g3 - ((5/3) T^{11} + (125/81) T^{19}) x^6.
```

**Rectangles.** `T x^6` has terms `(7,4),(6,3)`. `T^9 x^6` has terms `(15-k,36-k)` for `k=0..9`, max `i=15`. Disjoint from `T^{15}` (whose `y`-exponents are `60-k≥45`). Twenty-nine terms, corner `f6[(15,60)]=1`, all inside `(15,60)`. On the `g` side, `T^{11} x^6` and `T^{19} x^6` have max `i=17` and `i=25` respectively, max `j=44` and `76`; after overlaps with `g3` one has 63 terms, corner `g6[(25,100)]=1`, all inside `(25,100)`. Both corners remain 1.

**Valuation exactly six.** Sparse `J(f6,g6)` substituted into the centered chart yields `J-1` of `s`-valuation 6. Independently, the coefficients of `s^0` through `s^5` all vanish, and the `s^6` coefficient is the nonzero univariate

```text
-45 t^2 - 50 t^{10} - (1250/27) t^{18}.
```

So the order is exact, not a lower bound. `J_6` is not identically 1.

**No stronger fixed-rectangle order is asserted.** Producer §4 states that only the truncation through `x^6` is claimed to stay inside the SP-2 rectangles, and that the `x^9` coefficient of the canonical `F` already has `T`-degree 10. Independently: `A_9` has `T`-degree 10, and `T^{10} x^9` contains `x^{19} y^{40}` (`i=19>15`); `B_9` has `T`-degree 20, and `T^{20} x^9` contains `x^{29} y^{80}` (`i=29>25`). Adding a homogeneous solution `(λ p', λ q')` *increases* `T`-degree by at least 14, so it cannot restore the rectangle. The producer does not claim a `Q[T,x]` obstruction at `n=9` either: that would confuse the convenient subring with the full `Q[x,y]` rectangle (Claim 5).

---

## 5. The formal recursion in `Q[T][[x]]`

**Coordinate Jacobian factor.** `T x^3=u(1+u)^3` and `det ∂(x,T)/∂(x,y)=y^2(1+4u)` are polynomial identities (independent engine). For series `F,G∈Q[T][[x]]`,

```text
J_{x,y}(F,G) = (F_x G_T - F_T G_x) · y^2 (1+4u).
```

From `y=(1+u)/x` one has `y^2(1+4u)=x^{-2}(1+u)^2(1+4u)`. Differentiating `w=u(1+u)^3` gives `dw/du=(1+u)^2(1+4u)`, so `u'(w)=1/((1+u)^2(1+4u))`. The exact one-sided Keller equation is therefore (10):

```text
F_x G_T - F_T G_x = x^2 u'(T x^3).
```

**Formal IFT.** `φ(u)=u(1+u)^3` has `φ'(0)=1`, so there is a unique formal `u(w)` with `u(0)=0` and no localization in `T`.

**Lagrange inversion.** Writing `w=u/ψ(u)` with `ψ(u)=(1+u)^{-3}`,

```text
[w^n] u = (1/n) [u^{n-1}] (1+u)^{-3n} = (1/n) (-1)^{n-1} binom(4n-2, n-1).
```

Differentiating and setting `k=n-1` yields the displayed series `u'(w)=∑_{k≥0}(-1)^k binom(4k+2,k) w^k`. Independent check: the integrated series, composed as `u+3u^2+3u^3+u^4`, recovers `w` through order 12.

**Coefficient equation.** With `F=T^{15}+∑_{n≥1} A_n(T) x^n` and `G=T+T^{25}+∑_{n≥1} B_n(T) x^n`, the `x^{n-1}` coefficient of (10) after lower terms are fixed is

```text
n (A_n q' - p' B_n) = H_{n-1}(T),
```

`p'=15 T^{14}`, `q'=1+25 T^{24}`. The new unknowns enter only through `n A_n q'` and `-n B_n p'`.

**Bezout.** Directly `q'-(5/3)T^{10} p'=1+25 T^{24}-25 T^{24}=1`. So `gcd(p',q')=1` in `Q[T]`, and an explicit particular solution of `A q'-p' B=\mathrm{rhs}` is `A=\mathrm{rhs}`, `B=(5/3)T^{10}\mathrm{rhs}`. Independently, this unreduced solution satisfies the coefficient identity through `n=12`. The replay's canonical solution reduces `A_n` modulo `T^{14}` (`q'≡1 \pmod{T^{14}}`) and is the displayed pair at `n=3,6`.

**Characteristic zero.** The only scalar divisions are by the positive integer `n` and the constants `3,5,9,15,27,81` already in the displayed formulae. In characteristic `p` the step `n\mid p` would require a compatibility condition on `H_{n-1}`. The producer scopes the statement as characteristic zero; that scope is necessary and is kept.

**Arbitrary finite solvability, truncation, composition.** By induction every `A_n,B_n` exist in `Q[T]`. Truncating at `n=N` produces `F_N,G_N∈Q[T,x]`; composing `T=xy^4-y^3` produces elements of `Q[x,y]` whose height-four patterns remain `p,q` (the `x=0` parts). If (10) holds modulo `x^N`, multiplication by the coordinate factor `x^{-2}(1+u)^2(1+4u)` gives `J=1+O(x^{N-2})`. Any one-sided order `M` is obtained by `N≥M+2`. Because the target `u'(T x^3)` is a series in `x^3`, the actual vanishing is often stronger (orders 3 and 6 at `N=3,6`); the producer does not claim sharpness of the crude `N-2` bound, only its sufficiency. The recursion through `x^{18}` was reconstructed by a second solver; nonzero levels are exactly the multiples of 3, with `(deg A_n, deg B_n)=(0,10),(9,19),(10,20),(11,21),(12,22),(13,23)`.

**`Q[T,x]` versus the polynomial-origin completion.** The global polynomial `xy=1+u` equals `1+u(T x^3)`, and `u(w)` is an infinite series (`[w^8]u≠0`). So `xy` has an infinite expansion in `Q[T][[x]]` while remaining a polynomial in `(x,y)`. Canonical `A_9` of `T`-degree 10 already leaves the naive `Q[T,x]` rectangle, which is therefore a *strict* subring of the true polynomial-origin module (finite `Q[x,y]` rectangles). A valid fixed-degree obstruction cannot be read off this convenient chart.

---

## 6. Scope

The construction is intrinsically one-sided (completion only along `x→0`, `xy→1`), cap-dropped for the arbitrary-jet statement, and finite-order (`J=1+O(x^{N-2})`, never `J=1`). It does not converge, algebraize, constrain the r9/M2 pole-side expansion, pin mapping degree six, or control the finite affine critical locus.

What it does prove, and what was attacked:

- The bare-chart divisibility lemma is exact, and its hypothesis (holomorphy of *both* members in the zero-truncation chart) is not pinned by LR2. Explicit centered polynomials in the SP-2 rectangles satisfy the leading Jacobian equation that the bare argument called impossible. The bare-divisibility / "illegal `t`-independent `s^3`" attack is therefore stopped.
- The displayed pairs realise the SP-2 x-side *local* equality mechanism (patterns, three branches, contact `21/5`, `∑Λ=3`) at polynomial origin, with Jacobian one through two transverse orders inside the fixed rectangles. They do not realise SP-2 as a Keller pair.
- Arbitrary finite one-sided polynomial-origin jets exist when the degree cap is dropped. That kills any proposed obstruction that uses only a finite amount of one-sided x-chart data inside `Q[T,x]`.

What it does not prove, and what the producer does not claim: a kill or realization of SP-2 or of any of the other seven terminal classes; exact `J=1`; a two-chart compatibility theorem; landing, coverage, `G2-PSC`, `G2-BD`, or JC2.

The smallest honest remaining implication is exactly producer §5: with the full fixed Newton rectangles, the LR2-centered x-side cluster *including the three shared integer coefficients of `φ`*, and the pinned r9/M2 y-side patterns, prove that no single polynomial pair realises both charts at exact `J=1` — or exhibit such a pair. A contradiction confined to the bare chart or to `Q[T,x]` is pre-registered as a wrong-object stop.

---

## Source caveats (none load-bearing)

1. Proposition 7.3 is stated for polynomial Jacobian pairs. The special-fiber `Λ`-count for `(f_3,g_3)` is a geometric computation on a non-Keller polynomial pair, used only as a mechanism match with D73. It is not an application of the printed proposition to a counterexample.
2. Notation 3.5 defines `κ_F` on `V_a` with a known P-presentation ambiguity (campaign H5a). At `j=0` one has `κ_G=κ/e_0=1` unambiguously, which is the only value used.
3. Printed Statement 3.15 has the campaign's standing E10 label swap. Direct multiplicity of `g` on a uniformizer is used for `Λ`, so the swap is not load-bearing.
4. The x-side formula for `η_F` is the "same way" clause of Notation 3.9 rather than a separately displayed equation. The resulting identity `η_G=xy^4-y^3` is confirmed both by that reading and by direct substitution in the chart.
5. Committed LROOT:256-266 already records D73 as retiring direction-multiplicity strictness and names the remaining surface as polynomial realizability versus opposite-side templates. The present report is the first bounded attack on that surface (bare-chart globalization of D73's illegal term) and correctly stops it.
6. Equation (8) typographical omission and the missing `\]` after (10) are formatting only; recovered polynomials match the replay and the recursion.

---

## Promotion advice

**Accept** the report as a bounded `CENTERING-ESCAPE / FINITE-JET-CONTROL / STOP` of the bare-divisibility attack: LR2 does not pin the zero truncation, the bare monomial lemma therefore does not apply to the legal centered chart, and explicit SP-2-rectangle polynomials already match the local equality mechanism through two transverse Jacobian orders. Bank `T=xy^4-y^3` as the centered polynomial coordinate and bank `(f_3,g_3)`, `(f_6,g_6)` as finite-jet controls.

**Do not accept** as any of the following:

- a polynomial Keller pair, or a realization of SP-2 or of any other terminal class;
- a kill of any slack-0 class, or a cut of the book 8;
- an exact all-order `J=1` statement, a convergent or algebraized formal pair, or an opposite-side (r9/M2) theorem;
- a fixed-degree obstruction inside `Q[T,x]`, or a claim that the `x^9` event is an SP-2 obstruction;
- a JC2 decision.

Successor work, if any, has to be a two-chart coefficient transport on the original `C[x,y]` rectangles, with the three shared centering coefficients of `φ` carried as data and with exact Jacobian rows, consuming the pinned y-side patterns at the first band where they enter.

---

## Explicit exclusions

This review does not:

- edit the producer file, the replay, `ladder/SHEET6-LROOT.md`, `ladder/SHEET6-LT-REVIEW.md`, `AUDIT.md`, `APPROACHES.md`, or `refs/sigray_full.pdf`;
- treat D73's internal hostile audit, or any other uncommitted xmodel artifact, as evidence;
- assert that `(f_3,g_3)` or `(f_6,g_6)` is Keller, entire, or a finite map `C^2→C`;
- assert convergence or algebraization of the infinite `Q[T][[x]]` pair;
- assert anything about y-side orbits, pole clusters, mapping degree, or the (22) ledger of a global pair;
- launch a D43, new-book, or sparse-search task.

Frozen producer SHA-256, recomputed on disk at review time:

```text
b53064c877a4f0b741f23f036b2323195bef825ccc72b6722b98f1fc2d2eec17  xmodel/td6-global-compatibility-gate-20260824.md
d5d0d4d4209ef115b952571082c37252eb0f1e032e02f182cdccf516b29519d9  cases/td6_global_compatibility_20260824/replay.py
```
