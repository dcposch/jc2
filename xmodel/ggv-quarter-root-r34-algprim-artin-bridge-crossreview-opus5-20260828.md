# `R34-ALGPRIM-ARTIN` — hostile cross-review (Opus 5)

Date: 2026-08-28
Reviewer lane: Opus 5, independent hostile mathematical review, exact local desk algebra
Charged producer file: **hash verified, fail-closed gate passed**

```text
525c408e92b7f2cb11f5152e002e60a20a331d268283f1be30fb13b5a104b990
  xmodel/ggv-quarter-root-r34-algprim-artin-bridge-r0-sol-ultra-20260827.md
```

Named dependencies, all four re-hashed and matching the producer's Section 1:

```text
e5a2c968e516a40509d136cfd57613c8be84e50041444ce8146916b976bdf24c
  xmodel/ggv-quarter-root-r30-slice-descendant-r0-sol-ultra-20260827.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1
  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
e9f2a333ef94161e3e9c54288e4e06ed1047ee7a9c93254811787e6a2d517090
  xmodel/ideation-20260827T2259Z-fable5-crossreview-opus5.md
9c8c61a1ca6f71c3a04c396b176da4798817eff75f67e7508ed5be047d988c26
  xmodel/ideation-20260827T2259Z-carrier-hostile-review-sol-ultra.md
```

Pinned reviewer identity and environment:

```text
model            claude-opus-5  (Opus 5)
CLI              Claude Code 2.1.228
platform         Darwin 23.6.0 arm64
python           3.9.6 (Clang 15.0.0); no sympy, no CAS, stdlib fractions only
repo HEAD        418e413593120d19e15e6546eb50c985f4b1f038
review clock     2026-08-28T00:29:22Z
```

**Parent conditionality.** The row-34 descendant `e5a2c968…` is separately under
Fable5 review. Every verdict below that depends on the descendant's displayed
quotient `(uv,u^4,v^2)`, its ideals `(8.1)`, or its coordinate ring `(8.2)` is
stated **conditionally on those displayed atoms**. I did independently rederive
the five parent residue scalars and all five infinity residues (Section 8.4);
those are the only parent atoms I promote to unconditional. The parent is not
otherwise promoted here.

---

## 0. Verdict table

| # | Atom | Verdict |
|---|------|---------|
| 1 | Zero-tail is a section of the provisional row-34 class scheme over `R`; frozen windows respected | **CONFIRMED** (conditional on parent `(8.1)`/`(8.2)`), with one disclosed scope note |
| 2 | Implicit `Q=P^2` equation `(3.1)`; whole-series Hensel uniqueness of `(0.3)`, both branch signs | **CONFIRMED**, and strengthened by a Hensel-free second proof |
| 3 | `alpha_F`, the displayed primitive, every power, coefficient and sign | **CONFIRMED** |
| 4 | Whole coefficientwise class tower vanishes, not only through row 34 | **CONFIRMED**, plus a strictly stronger scheme statement the producer understates |
| 5 | Field/Artin, rational/algebraic, whole-series/truncation, class/raw, primitive/polynomial-`G` firewalls | **CONFIRMED** (five of five), with one **REPAIRED** wording item in §7 |
| 6 | Operational consequence: stop class/ALG-PRIM work here; raw/`G`-window is the next honest interface | **REPAIRED** — `STOP` is right; the `CONTINUE` list is over-funded, because the section is already **raw-dead at `D_22`** by a one-line argument I derive below |

No atom is `GAP` or `REFUTED`. The producer's own claim ledger is accurate; the
repair is to its forward-work recommendation, not to any of its mathematics.

---

## 1. Atom 1 — the zero-tail section — **CONFIRMED**

### 1.1 It is a section

The descendant's newest-slot coordinates and its free/dependent split were
re-read directly from `e5a2c968…` `(2.1)`, `(4.3)`, `(6.3)`, `(8.1)`, `(8.2)`.
Free coordinate census:

```text
a_0..a_8            9      (F_8)
b_1,b_2,b_3,b_7     4      (F_9,  after I_31)
c_1..c_6            6      (F_10)
d_3,d_5             2      (F_11, after I_33)
e_2,e_3,e_4         3      (F_12)
                   24      = the producer's "24 free newest-slot coordinates"
```

Setting all 24 to zero and propagating the two unit-pivot ideals:

```text
I_31: 6b_1+b_5=0            -> b_5=0
      13b_2+3b_6=0          -> b_6=0
      b_4=0                 -> b_4=0
I_33: 8d_1+d_5+32u b_2+16u b_6=0     -> d_1=0   (uses d_5=0, b_2=0, b_6=0)
      2d_2+u(13b_3+7b_7)=0           -> d_2=0
      2d_4+5u(11b_1+5b_5)=0          -> d_4=0
```

The chain closes (`b_6` is itself dependent and lands at `0` before it is used
in the `d_1` row), so `F_8=F_9=F_10=F_11=F_12=0`. The producer's sentence
"the row-31 and row-33 unit-pivot equations then set all dependent odd-slot
coordinates to zero as well" is exactly right, including the observation that
every dependent coordinate lives in an odd slot. **CONFIRMED.**

`F_0=A^4` is not a free choice: R7R1 fixes `F_0=H^2`, and the descendant fixes
`H=A^2` (its §3), so `F_0=(A^2)^2=A^4`. The producer's `(0.2)` is therefore the
descendant's own slice with all newest slots zeroed. **CONFIRMED.**

Producer `(2.1)` — "the row-30, row-32 and row-34 class ideals vanish in `R`" —
is *true but tautological*: `R` is by construction `Q[u,v]` modulo
`I_30+J_32+J_34`, which the parent's `(7.8)` computes to be exactly
`(uv,u^4,v^2)`. It is a restatement of the base, not an independent check. Not
an error; flagged so no later reader mistakes it for corroboration.

### 1.2 Frozen source windows

The producer checks only the three upper bounds. I reconstructed the window law
from the descendant's five declared rows and it fits all five exactly:

```text
slot   declared     lo = max(0, ceil((m-8)/3))   hi = 16-m
F_8    [0,8]        0                             8     OK
F_9    [1,7]        1                             7     OK
F_10   [1,6]        1                             6     OK
F_11   [1,5]        1                             5     OK
F_12   [2,4]        2                             4     OK
```

Against that law the producer's three claims check, with the lower bounds
(which the producer does not state) also satisfied:

```text
F_2 = 4uA^2B = 16u(X^11 - 2X^7 + X^3)   degrees {3,7,11}  in [0,14]   OK
F_4 = 2u^2B^2 = 32u^2 X^6               degree  {6}       in [0,12]   OK
F_6 = v                                 degree  {0}       in [0,10]   OK
```

Independent corroboration: the same law predicts `F_13: [2,3]` (dim 2),
`F_14: [2,2]` (dim 1), `F_15` and `F_16` **empty**. That reproduces R7R1's
independent statement "`F` stops at weight 14" from a completely different
source. Two-source agreement. **CONFIRMED.**

### 1.3 One disclosed scope note (not a defect)

`F_13` and `F_14` are *not* coordinates of the row-34 scheme — they enter at
rows 35 and 36. The producer's `(0.2)` sets them to zero, and discloses this at
line 113 ("all later allowed slots are simply specialized to zero"). So `(0.2)`
is: a point of the row-34 scheme (all 24 free coordinates zero) **together with**
a zero lift of the two not-yet-adjoined slots.

This matters only for Atom 4 and only in one direction: the whole-tower claim
`(0.6)` is a claim about *this full section including `F_13=F_14=0`*, not about
the row-34 scheme's fibre. I recommend `(0.6)` be quoted with that hypothesis
attached. Nothing in the four dependencies forces `F_13` or `F_14` nonzero, so
the lift is admissible; I found no normalization that would forbid it.

---

## 2. Atom 2 — implicit equation and whole-series Hensel — **CONFIRMED**

### 2.1 Reduction to a `Q`-equation is legitimate

On the section `F` has only *even* nonzero coefficients (`F_0,F_2,F_4,F_6`), so

```text
F(X,sP) = A^4 + 4uA^2B s^2 P^2 + 2u^2B^2 s^4 P^4 + v s^6 P^6
```

is a polynomial in `P^2=Q` alone, and `P^8=(P^2)^4=Q^4`. Hence `(3.1)` is exact:

```text
Q^4 = A^4 + 4uA^2B s^2 Q + 2u^2B^2 s^4 Q^2 + v s^6 Q^3.
```

Had any odd `F_i` survived, this reduction would be illegal. It does not, and
the producer's `(0.2)` is what makes it legal. **CONFIRMED.**

### 2.2 `Q_*` solves it — and does so more generally than claimed

Hand expansion, with `a=eps A`, `b=uBs^2`, `c=(v/4)s^6`, and `bc=c^2=b^4=0` in `R`:

```text
LHS  Q_*^4 = a^4 + 4a^3(b+c) + 6a^2 b^2 + 4a b^3
           = A^4 + 4 eps u A^3B s^2 + eps v A^3 s^6
             + 6 u^2A^2B^2 s^4 + 4 eps u^3 A B^3 s^6
RHS        = A^4 + (4 eps u A^3B s^2 + 4u^2A^2B^2 s^4)
             + (2u^2A^2B^2 s^4 + 4 eps u^3 A B^3 s^6)
             + eps v A^3 s^6
           = A^4 + 4 eps u A^3B s^2 + 6u^2A^2B^2 s^4 + 4 eps u^3 A B^3 s^6 + eps v A^3 s^6
```

Identical term by term. **This expansion never uses `A=X^4-1` or `B=A'`.** My
independent engine confirms `Q_*^4 - RHS = 0` with `A` and `B` as *free
symbols*, and three mutation controls (`uB -> 2uB`, `v/4 -> v/2`, drop the
`s^6` term) all produce nonzero residual, so the check is not vacuous. See
Section 8.2. **CONFIRMED, stronger than displayed.**

### 2.3 Hensel uniqueness, both branch signs

```text
Hdef(s,Q) = Q^4 - A^4 - 4uA^2Bs^2Q - 2u^2B^2s^4Q^2 - v s^6 Q^3
d Hdef/dQ |_(s=0, Q=eps A) = 4(eps A)^3 = 4 eps A^3        (eps^3 = eps)
```

`R(X) = Q(X)[u,v]/(uv,u^4,v^2)` is local with residue field `Q(X)`; an element
is a unit iff its residue is nonzero; `4 eps A^3` has residue `4 eps A^3 != 0`.
So it is a unit and the formal implicit-function theorem over the `s`-adically
complete ring `R(X)[[s]]` gives a unique solution with `Q(0)=eps A`. The
selected `P` (which exists: `d/dP(P^8-F(X,sP))|_(s=0,P=p) = 8p^7 = 8 eps A^3 p`,
and `p` is a unit with `p^(-1)=eps p/A`) yields `Q=P^2` solving `(3.1)` with
`Q(0)=p^2=eps A`, hence `Q=Q_*`. Correct for `eps=+1` and `eps=-1`. The
producer's slightly garbled phrase "the derivative of the left side of (3.1),
moved to one side" reads correctly either way: the three right-hand terms all
carry `s^2`, `s^4` or `s^6` and vanish at `s=0`. **CONFIRMED.**

### 2.4 Independent constructive solve

I rebuilt the whole calculation on a different representation — exact `Q(X)`
rational functions with Euclidean-gcd reduction, an explicit `{1,u,u^2,u^3,v}`
multiplication table, and undetermined-coefficient `s`-adic recursion
`q_n = ([s^n]RHS - [s^n]Q^4|_(q_n:=0)) / (4 eps A^3)` — with **concrete**
`eps = +1` and `eps = -1` (no formal `eps` variable, unlike the producer's
`e&1` trick). Result to order `s^60`, both signs:

```text
nonzero q_n indices: [0, 2, 6]
q_0 = eps*(X^4-1)      q_2 = 4u X^3 = uB      q_6 = v/4
implicit-equation residual nonzero at s-orders: []   (i.e. exact at every order)
```

Note `q_2` and `q_6` come out **independent of `eps`**, matching `(0.3)`.
**CONFIRMED.**

### 2.5 A Hensel-free second proof (new; strictly more robust)

The producer's `§5.3` says formal uniqueness "is what licenses the infinite
conclusion". True for the producer's route, but not necessary. Using the
promoted all-row formula (Fable5 `§3.1`, `q_n = (2/(n+2))[t^n] F^((n+2)/8)`),
write `F = A^4(1+Y)` with

```text
Y = y2 t^2 + y4 t^4 + y6 t^6,   y2 = 4uB/A^2, y4 = 2u^2B^2/A^4, y6 = v/A^4.
```

All three coefficients lie in `m=(u,v)`, and `m^4=0` in `R`, so
`(1+Y)^e = 1 + eY + C(e,2)Y^2 + C(e,3)Y^3` **exactly**, for every exponent `e`.
Enumerating surviving monomials (Section 8.5):

```text
Y^1 survives at t-weights {2,4,6}     Y^2 at {4,6}     Y^3 at {6}     Y^k = 0, k>=4
```

Hence `[t^n](1+Y)^e = 0` for every `n` outside `{0,2,4,6}` and **every** `e`.
Therefore `q_n = 0` for all odd `n` and all `n >= 7`, with no Hensel argument,
no unit pivot, and no completeness hypothesis. The remaining even values:

```text
n=0: e=1/4   q_0 = eps A
n=2: e=1/2   q_2 = A^2 * (1/2)*(1/2)*4uB/A^2 = uB
n=4: e=3/4   q_4 = (3/4)*2 + C(3/4,2)*16 = 3/2 - 3/2 = 0     (e-specific cancellation)
n=6: e=1     q_6 = A^4 * (1/4) * v/A^4 = v/4 ;  C(1,2)=C(1,3)=0 kills the u^3B^3 part
```

Worth recording the distinction: `q_n = 0` for `n >= 7` is **structural**
(nilpotency plus the even `t`-support of `Y`), whereas `q_4 = 0` is an
**exponent-specific cancellation** at `e = 3/4`. **CONFIRMED, with a second
independent proof.**

### 2.6 Low-order cross-check against R7R1 `(0.4)`

```text
q_0 = p^2                       = eps A                OK
q_1 = F_1/(4p^5)                = 0    (F_1=0)         OK
q_2 = F_2/(4H) - F_1^2/(16H^3)  = 4uA^2B/(4A^2) = uB   OK
```

Three routes (recursion, binomial, R7R1 closed forms) agree. `(0.3)` holds.

Minor, non-defect: `(0.3)` places `Q` "in `R(X)[s]`"; it is in fact in
`R[X][s]` (polynomial, no `A` in any denominator), which is strictly stronger.

---

## 3. Atom 3 — `alpha_F`, primitive, powers, coefficients, signs — **CONFIRMED**

### 3.1 The filter as displayed is the reviewed one

`(4.1)` is verbatim the form confirmed in Fable5 crossreview `e9f2a333…` `§3.1`
and `§3.7` (`alpha_F = -(s^21/16)(d_s(s^2 P^2) - 2 p^2 s) dX`, ambient
`E' = K(F)(X,s,P,p)`), and matches the carrier hostile review `9c8c61a1…` `§5`
including its index shift `alpha_F = sum_(n>=1) -(n+2) q_n s^(n+22) dX / 16`.
No substitution, no drift. **CONFIRMED.**

I re-derived the identification from R7R1 `(0.2)` independently:

```text
d_s(s^2 Q) = sum_n (n+2) q_n s^(n+1)
-(s^21/16) d_s(s^2 Q) = -(s^22/16) sum_n (n+2) q_n s^n = W_X|s
the +(s^21/16)(2 p^2 s) term cancels exactly the n=0 piece, since q_0 = p^2
```

### 3.2 Every power, coefficient and sign

```text
s^2 Q_*            = eps A s^2 + uB s^4 + (v/4) s^8
d_s(s^2 Q_*)       = 2 eps A s + 4uB s^3 + 2v s^7
minus 2p^2 s       = 4uB s^3 + 2v s^7                               = (4.2)  OK
times -(s^21/16)   = -(u/4) B s^24 - (v/8) s^28                     = (0.4)  OK
beta               = -(u/4) A s^24 - (v/8) X s^28                   = (0.5)
d_X beta           = -(u/4) A' s^24 - (v/8) s^28 = -(u/4)B s^24 - (v/8)s^28   OK
```

Cross-check against the coefficient law: `-(2+2)/16 * uB = -(uB)/4` and
`-(6+2)/16 * (v/4) = -v/8`. Both match. Verified three ways (operator form,
coefficient law, displayed closed form) — all three agree exactly; see 8.2.

`B = A'` is used **exactly once**, in `d_X beta`. The implicit-equation half of
the report is `A`,`B`-generic; the primitive half is not. Worth pinning.

Displayed supports reproduce exactly, on my engine and on the producer's:

```text
support(Q)     [(0,0,0,0,1), (0,6,0,1,0), (3,2,1,0,0), (4,0,0,0,1)]
support(alpha) [(0,28,0,1,0), (3,24,1,0,0)]
support(beta)  [(0,24,1,0,0), (1,28,0,1,0), (4,24,1,0,0)]
```

`s`-order of `beta` is 24, so `>= 23` holds; Fable5 `§3.3` has already shown the
order clause is redundant, and the producer's "compatible with (and stronger
than)" is accurate.

### 3.3 The four bullets in `§4`

* "no finite poles to reduce" — `alpha_F` is a polynomial differential. OK.
* "exact polynomial differentials have zero residue, including at infinity" —
  `Res_inf(X^n dX) = -[tau^(-1)](-tau^(-n-2)) = 0` for `n >= 0`. OK.
* "de Rham remainder is zero by the explicit primitive" — OK.
* "`beta` lies in the rational base ring before adjoining either `p` or `P`" —
  OK; neither `alpha_F` nor `beta` contains `p` or `P`, because on this section
  `q_0 = p^2 = eps A` is already in `R[X]`.

`(4.3)`'s `E'_R = R(X,s,p,P)/(p^2 - eps A, P^2 - Q)` is well-typed here
*because* `Q` is polynomial on this section, so it is an honest finite
extension of `R(X,s)` and `beta in R[X,s] subset E'_R`. On a general section
`Q` is only a formal series and `(4.3)` would need restating; the producer does
not claim otherwise. **CONFIRMED.**

---

## 4. Atom 4 — the whole class tower — **CONFIRMED**, and understated

### 4.1 The tower does vanish, at every row

By 2.4/2.5, `q_n = 0` for all `n >= 1` except `n in {2,6}`, to all orders. For
the two survivors:

```text
even-row gauge:  A^((n+2)/2) p^(-(n+22)) q_n = q_n   (since p^2 = eps A, eps^2 = 1)
q_2 dX = uB dX  = d_X(uA)             q_6 dX = (v/4) dX = d_X(vX/4)
```

Both primitives are **polynomial**, hence regular on `V_H`. That matters: the
tower condition confirmed in Fable5 `§3.5` is not bare exactness in the
fraction field but exactness with a primitive in `O(V_H)`. The section passes
the stronger form. Odd rows gauge into the twisted receivers `V_1`, `V_3` with
`nabla_j = d + (j/2)(B/A)dX`; all odd `q_n` vanish and `0` is `nabla_j`-exact.
So `(3.3)` and "all remaining positive-index class rows vanish identically" are
correct as stated. **CONFIRMED.**

### 4.2 Independent agreement with the parent's own rows 32 and 34

The descendant's `(5.3)`/`(7.3)`, evaluated at the zero tail, give

```text
q_10 = -(u^2 v/4) B^2/A^2 - (u^5/2) B^5/A^4       -> 0 in R  (u^2v = u(uv), u^5 = u(u^4))
q_12 =  (3/32) v^2/A + (1/4) u^3 v B^3/A^3 + (1/2) u^6 B^6/A^5  -> 0 in R
q_9  = (1/4)p^3 P_9 = 0        q_11 = (1/4)p^5 P_11 + (5/32)p^(-3)F_2 P_9 = 0
```

exactly matching my recursion's `q_9 = q_10 = q_11 = q_12 = 0`. Two structurally
unrelated derivations agree on the four charged rows.

### 4.3 The producer understates its own result — strengthening

`§0` says only that later rows "cannot shrink the projected Artin base `(0.1)`
**along this section**". The correct statement is stronger and is a genuine
scheme-theoretic conclusion. Let `I` be the ideal of the full class tower for
this slice in `Q[u,v][slots]`. The section is a `Q[u,v]`-algebra map
`Q[u,v][slots]/I -> R`, so

```text
I cap Q[u,v]  subset  ker(Q[u,v] -> R) = (uv, u^4, v^2).
```

The parent's `(7.8)` gives the reverse containment. Hence

```text
I cap Q[u,v] = (uv, u^4, v^2)   exactly, for the ENTIRE class tower.
```

Row 34 is therefore the **last** row that can ever cut this slice's projected
base — not merely "later rows do not cut along this section". I recommend the
promoted statement be upgraded to this form (still conditional on the parent's
`(7.8)`).

### 4.4 Precision on the hypothesis

Per 1.3, `(0.6)` requires `F_13 = F_14 = 0` in addition to the 24 zeroed
coordinates. State it with the hypothesis.

---

## 5. Atom 5 — the five firewalls — **CONFIRMED** (5/5), one wording **REPAIRED**

**5.1 Field vs Artin — CONFIRMED.** Standard monomials of `(uv,u^4,v^2)` in
`Q[u,v]` are `u^a v^b` with (`a=0` or `b=0`), `a<=3`, `b<=1`, i.e. exactly
`1,u,u^2,u^3,v`: length five, local, not a field. Every ring map `R -> K` kills
the nilpotents `u,v`, so the only field-valued point is the origin, where
`Q = eps A` and `alpha_F = -(s^21/16)(2 eps A s - 2 eps A s) = 0`. The producer
correctly refuses to present this as an application of the field theorem, and
correctly hedges the Artin extension ("**If** one extends the algebraic-
primitive test functorially to Artin coefficient rings"). I confirm no such
functorial extension is proved anywhere in the four dependencies; the actual
content is precisely the displayed identity `alpha_F = d_X beta` over `R`,
which the producer says in as many words.

**5.2 Rational vs algebraic — CONFIRMED.** `alpha_F in R[X,s]dX` and
`beta in R[X,s]`; no `p`, no `P`, no poles anywhere, so this is indeed not a
"residues vanish but a positive-genus second-kind class survives" example.

**5.3 Whole series vs truncation — CONFIRMED.** Checking `q_1,…,q_12` alone
genuinely does not license `(0.6)`. My 2.5 shows the producer's Hensel route is
*a* structural argument but not the only one; the firewall itself stands.

**5.4 Class vs raw — CONFIRMED, and now realized rather than hypothetical.**
"A class row that is exact can still carry a nontrivial polynomial-window
compatibility condition in the raw determinant system" — Section 6 exhibits an
explicit point of this very section where that happens fatally.

**5.5 Polynomial-`G` window descent — CONFIRMED.** `beta` gives only the
`X`-primitives. R7R1 `(0.3)` leaves the whole constant series `Phi(s) in C_L[[s]]`
free and `w_22` undetermined, and `G = P^12 W` with `s = t/P` requires
`s^m P^12 = t^m P^(12-m)` to descend to the frozen window for `m >= 23` —
untouched here. Correct as written.

**5.6 Scope inside the 24-slot descendant — CONFIRMED.**

**REPAIRED (wording, `§7` last paragraph).** "This slice is a clean negative
control for the claim that the algebraic-primitive gate is automatically
strictly stronger than the class tower." A section on which *both* the gate and
the tower fail to cut is **not** evidence against strictness: strict strength
needs only one point where the gate cuts and the tower does not, and Fable5
`§3.7` already records strictness as unproven either way. The producer's
qualifier "automatically" makes the sentence defensible as literally written,
but it must not be quoted downstream as evidence against strictness. Recommend
rephrasing to: *"a point where `GATE-ALG-PRIM` provably adds nothing beyond the
class tower; it neither establishes nor refutes strictness."*

---

## 6. Atom 6 — operational consequence — **REPAIRED**

`STOP` is correct and correctly reasoned. The `CONTINUE` list is over-funded.

### 6.1 New finding: the section is raw-dead at `D_22`

At the reduced point `u=v=0` of this section, every slot is zero, so
`F = F_0 = A^4` is **`t`-free**. Then `F_t = 0` and R7R1 `(0.1)` factors, for
**every** `G`:

```text
E = 12 F_X G - 8 F G_X - t(F_X G_t - F_t G_X)
  = 12(4A^3B)G - 8A^4 G_X - t(4A^3B)G_t
  = 4 A^3 ( 12 B G - 2 A G_X - B t G_t ).                       (*)
```

I verified `(*)` symbolically against the unfactored expression on random
bivariate `G` (Section 8.3). Consequently every raw coefficient satisfies
`D_m in A^3 Q[X]`, and

```text
D_22 = 4 A^3 * (polynomial in X)   can never equal   1.
```

A second, independent route to the same kill: `F` is `t`-free and R7R1 freezes
`G` at weight 21, so `deg_t E <= 21` and `D_22 = 0` outright. Both routes were
exercised on random `G` and agree.

Now lift it off the reduced point. `R` is local Artin with residue field `Q`,
and `(0.1)` is `R`-linear in `G` with `Q`-coefficients, so it commutes with
`R -> R/m = Q`. Any `G in R[X][t]` solving `E = t^22` over `R` would reduce to a
`Q`-solution at the origin — impossible. Therefore:

> **The charged zero-tail Artin section admits no polynomial `G` at all, over
> `R` or any quotient of `R`. It contains no face point.**

Sanity confirmation in Keller coordinates: at the origin
`f = t^(-8)F = y^8(x^4 y^12 - 1)^4`, and `[f,g]` restricted to `x = 0` is
`-8y^7 g_x`, which vanishes at `y = 0` and so cannot equal `1`.

### 6.2 What this changes

* Do **not** fund `§7` option 1 ("raw determinant rows through the full
  possible range, with `D_22=1`") on this section. `D_22` alone decides it, by
  hand, in one line. Compiling `D_0..D_35` here would only re-derive death.
* Do **not** fund `§7` option 2 (`G`-window descent) on this section either;
  there is no `G` to descend.
* The producer's own firewalls `§5.4`/`§5.5` are thereby **realized**: here is
  an explicit point that passes the *entire* class tower **and**
  `GATE-ALG-PRIM`, yet has no polynomial `G`. In my judgement this is the most
  valuable object in the neighbourhood: a citable witness that
  `GATE-ALG-PRIM` is necessary-and-not-sufficient on this family, which is
  exactly the caveat Fable5 `§3.7` and the carrier review `§5` both record as
  asserted-but-undemonstrated.
* **Scope guard, important.** This does **not** kill the descendant slice. A
  general point of the descendant reduces mod `m=(u,v)` to `F = A^4 + sum_(i>=8)
  F_i t^i` with the *reduced slot values surviving*; then `F` is not `t`-free
  and `F_X` is not divisible by `A^3`, and `(*)` does not apply. Only the
  zero-tail section is killed. The 24-slot family remains open.
* The genuinely open successor is unchanged in spirit but sharper: a
  **nonzero-slot** section of the descendant, or the field-valued whole-tower
  survivor the producer already recommends in `§7`'s last paragraph.

This finding is mine, is new, and has not itself been reviewed. It should carry
the same provisional status the producer's own report carries until a different
model checks `(*)`, the weight-21 bound on `G`, and the mod-`m` reduction step.

---

## 7. Promotion recommendation (narrowest)

**Promote, conditional on the parent descendant `e5a2c968…` clearing Fable5
review with `(8.1)`/`(8.2)` intact:**

1. `(0.2)` is a section of the row-34 class-prefix scheme over `R`, respecting
   the frozen `F_2/F_4/F_6` windows — **with the hypothesis `F_13=F_14=0`
   stated explicitly**.
2. `(3.1)`, and `(0.3)`/`(0.6)` as a whole-series identity for both branch
   signs. Cite the Hensel route *and* the Hensel-free binomial route (2.5).
3. `(0.4)`, `(0.5)`, `(4.2)`: `alpha_F = d_X beta` with `beta in R[X,s]`, and
   the consequence that `GATE-ALG-PRIM` makes no cut on this section.
4. The upgraded `§4.3` statement: the projected base of the **entire** class
   tower on this slice is exactly `Spec R` — not merely unshrunk along the
   section.
5. All six firewalls `§5.1`–`§5.6` as written.

**Promote unconditionally (parent-independent, rederived here):** the five
residue scalars `3, 256, 1/4, 6, 1155/2` and the five infinity residues
(`-1024` for `B^5/A^4`; zero for the other four) used in the parent's `(5.5)`,
`(5.6)`, `(7.5)`, `(7.6)`.

**Do not promote:** `§7`'s `CONTINUE` list as written (superseded by 6.1–6.2);
any reading of `§7`'s "negative control" sentence as bearing on strictness.

**Route to a fresh different-model review, unpromoted:** the endpoint-death
finding of Section 6.1.

---

## 8. Independent replay

All work was local, exact, stdlib-only, and small. Scripts staged in
`/tmp/o5r34/`, hashed for custody:

```text
573db36fcf7b03a453b5b8402d3d24d1df8967d03f7b5677c4ff066ba1a8721b  indep.py
c2418fac6002426de202ae162ef23893d6cd6c20efafe26a5539bbeee9704d40  indep2.py
2f8ca42f1763a61bdd94000d632d4952d4e3b53e864b8172fe1368ea73093d51  raw.py
b17f240ae4eed3932df9875b9a18e2d0485579a6dbcafc1c2f8cc40329d89982  windows.py
c59e46acef84a841ab995e2d926400290303390cbf0e4e37a3ae683e1fbba5a8  binom.py
71e3e3bf2dd29ead66e3239bdfecb24ffe600ec6918c90fcac3d1360e6776e20  producer_replay.py
```

### 8.1 Producer's own `§6` replay, run verbatim

Extracted from lines 263–326 of the charged file and executed unmodified.
Output reproduced **byte-identically** against the file's displayed
"Exact output" block, including all three supports.

### 8.2 `indep2.py` — symbolic-`A`,`B` identity, three `alpha` routes

```text
(a) Q*^4 - RHS  with A,B FREE SYMBOLS : 0
    mutation [u B s^2 -> 2u B s^2] residual nonzero? True
    mutation [v/4 -> v/2] residual nonzero? True
    mutation [drop v/4 s^6] residual nonzero? True
(b) alpha(coefficient law) == alpha(0.4) : True
    alpha(operator 4.1)   == alpha(0.4) : True
    d_s(s^2Q)-2p^2 s      == 4uBs^3+2vs^7: True
(c) d_X beta == alpha (with B=A') : True
```

### 8.3 `raw.py` — the raw-interface probe

```text
Structural identity  E(A^4,G) - 4A^3*(12 B G - 2 A G_X - B t G_t) == 0 ?
    True   True   True   True                (4 random bivariate G)
E divisible by A^3 = (X^4-1)^3 ? True (6/6 random G);  D22 == 1 ? False (6/6)
```

### 8.4 `indep2.py` — parent residue scalars, independently recomputed

```text
Res_{z=1}((A')^k / A^l dz),  A = z^4 - 1,  z = 1+w
k=2 l=2: 3       claimed 3        OK      alpha-exp 3     Res_inf 0
k=5 l=4: 256     claimed 256      OK      alpha-exp 0     Res_inf -1024
k=0 l=1: 1/4     claimed 1/4      OK      alpha-exp 1     Res_inf 0
k=3 l=3: 6       claimed 6        OK      alpha-exp 2     Res_inf 0
k=6 l=5: 1155/2  claimed 1155/2   OK      alpha-exp 3     Res_inf 0
```

The `alpha`-exponent law `alpha^(3k+1)` follows from `A(alpha z) = A(z)` and
`(A')^k(alpha z) = alpha^(3k)(A')^k(z)`; it reproduces the parent's `3alpha^3`,
`256`, `alpha/4`, `6alpha^2`, `(1155/2)alpha^3` and its `-1024` /
"all three infinity residues vanish".

### 8.5 `binom.py` — Hensel-free route

```text
Y^1 surviving t-weights [2, 4, 6]
Y^2 surviving t-weights [4, 6]
Y^3 surviving t-weights [6]
Y^4..Y^7  = 0 in R
=> [t^n](1+Y)^e = 0 for every n not in {0,2,4,6}, for EVERY exponent e
=> q_n = 0 for all odd n and all n >= 7, with NO Hensel argument
n=0 e=1/4 -> eps A ;  n=2 e=1/2 -> uB ;  n=4 e=3/4 -> 0 ;  n=6 e=1 -> v/4
```

### 8.6 `indep.py` — constructive Artin-basis solve to `s^60`

```text
eps=+1  nonzero q_n indices up to n=60: [0, 2, 6]
eps=-1  nonzero q_n indices up to n=60: [0, 2, 6]
q_0 = eps(X^4-1)   q_2 = 4uX^3   q_6 = v/4
implicit-equation residual nonzero at s-orders: []      (both signs)
```

### 8.7 `windows.py` — window law and zero-tail forcing

Reproduced in Sections 1.1 and 1.2 above.

---

## 9. Disclosures

* The charged file and all four named dependencies were hash-verified before
  reading. No other `xmodel` submission, case directory, or canonical ledger
  was read.
* I did have a shell this session. All computation was exact, local,
  stdlib-only, and completed in seconds. No AWS resource was contacted. No
  heavy local computation ran. No canonical ledger was edited.
* No path under `jc2-lean` was listed, searched, read, built, statused, or
  modified.
* This file is the only write into the repository.
* The parent descendant `e5a2c968…` is **not** promoted by this review beyond
  the five residue scalars and five infinity residues of Section 8.4. Every
  other conclusion resting on `(uv,u^4,v^2)`, `(8.1)` or `(8.2)` is explicitly
  conditional on its separate Fable5 review.
* Section 6.1 is a **new, unreviewed** finding by this reviewer and carries
  provisional status.
