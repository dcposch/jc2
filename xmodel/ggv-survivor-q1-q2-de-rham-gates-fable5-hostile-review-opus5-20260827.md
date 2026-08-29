# Hostile review: Fable5 survivor-curve `q1`/`q2` de Rham gates

Reviewer: Opus5 (different-model hostile referee)
Date: 2026-08-27
Scope of charge: **only** §§3.1-3.3 and Card 1 of
`xmodel/ideation-20260827T1606Z-fable5.md`. Reproved from corrected R7R1
(R7R1 sol + the `D35 == 0` repair) and the frozen D3 raw windows.

## Overall verdict

**The `q1` theorem atom is CONFIRMED and is stronger and sharper than the
producer states. The surrounding strategic framing in §3.1 is REFUTED as
written. Card 1's target-gap premise is REFUTED by the post-seal weight-2
correction — but the `q1` gate survives that refutation as genuinely
independent information, which I prove by exhibiting transversality and an
explicit separating fill.**

| # | Charged item | Verdict |
|--:|---|---|
| 1 | `q1=F1/(4p^5)`, `q2=F2/(4H)-F1^2/(16H^3)`, licensing rows | **CONFIRMED** (one inherited off-by-one in the row census: `GAP/REPAIR`) |
| 2 | Branch-P `q1` reduction, image of `Q -> 2AQ'-3A'Q`, codim exactly 3 | **CONFIRMED** (every sub-claim: injectivity, primitive completeness, infinity/branch, base field, twist) |
| 3 | Rank-13 fixture for `A=X^4-1` + load-bearing mutation | **CONFIRMED** for rank 13; `GAP/REPAIR` on the unreconstructable "27 candidate generators"; mutation supplied |
| 4 | `q2` descent to `K(X)`, residue `-3/64` | **CONFIRMED** (descent argument simplified: trace, no `mu4` needed); `GAP/REPAIR` on "row two cuts more" — it cuts `F2`, not `F1` |
| 5 | Special strata (`A` non-squarefree, `4|delta`), branch Q | **GAP/REPAIR**: codim 3 is *exactly* the squarefree locus; every degeneration drops it to 2 or 1. Branch Q genus 3 **CONFIRMED**, codim proved **exactly 4** |
| 6 | "The exact face decouples into F-gates + unique G-completion + endpoint" | **REFUTED as written** (omits `D1..D14`; `q`-gates cannot substitute for rows; G-completion is *not* unique for even `n<=12` on branch P). Repaired architecture supplied |

No item of the `q1` atom was falsified. Everything falsified is in §3.1's
strategy paragraph and Card 1's target-gap sentence.

---

## Custody and execution disclosure

Recomputed SHA-256 of every artifact I consumed:

```text
bb9c54afd086db383dcab3519f556f65ae5abb134ba3555f57c7a6cdbf045257  xmodel/ideation-20260827T1606Z-fable5.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
7ab758fa002c75cd28d81540e8f63fd8cd0de97fad791afedfeb5fb610c6cb29  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-hostile-review-fable5-20260827.md
5735ee90e5b7c51444892c011a072bcaaf497f6e446c46934f392fdb08a85ede  xmodel/ggv-degree8-r5-survivor-raw-support-analysis-hostile-audit-sol-ultra-20260827.md
ed0e3460cc16d0d8b9fb25823dc09f56bb4b1ad41561744bc8713848128fad19  xmodel/ggv-endpoint-survivor-codimension-r6-sol-20260827.md
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
```

The R7R1 sol hash matches the one pinned in the R7R1 hostile review, so the
"corrected R7R1" I reprove from is the reviewed object plus that review's
single repair (`D35 == 0`, sharp maximum `D34`).

This session had a shell. I wrote and ran only my own pure-Python exact
(`fractions.Fraction`) desk scripts in `/tmp/o5q`; no producer code was
executed, no `sympy`/`flint`/Groebner engine is installed or was used, no
AWS was launched, no canonical ledger was edited, and `jc2-lean` was not
read, touched, or status-inspected. I did not open the Opus5 peer ideation
submission. Script manifest (desk-scale, seconds each):

```text
352180688c7e33606f96961dd7ebc8d9130638d50a68e15f6062d315c8c18d1e  lp.py          truncated Laurent-series engine
f5124aa8600d0d30c02e2c6ed8e705325702a5ba2579b02feeca226f05748001  poly.py        exact Q[X] + rref/nullspace
bcce4d7a3825e9120feacdf1971295cf9f00957cee281b742a0a285d75ad59e2  q1q2.py        item 1 symbolic q1,q2
10e1a3ce5db1e5bf76502ae9ab8fa929bf596e41d66b51c56a3ffb9f104b2dda  lattice.py     D3 windows, slot census, D34/D35
d8e5e2ffcc36bb69172d31897de7b22b3d624b566d55f0ccfd4b4e176399b34e  branchP.py     item 2/5 branch-P q1 dimensions
d1292f3e933b5994052fab288a15f4bc6536a2e04998ab29c45137bc4f93c715  coker.py       item 3 rank 13 + cokernel + residue functional
d4bc0044be64b89d5139affa41841a8fda241f51e59b9741e036f34586d298c2  mut.py         item 3 mutations + transversality
5a6f7987eb34735782536e5f9501591727f02c5a59c3b8c599865a7c0556ea3d  twentyseven.py item 3 "27 generators" reconstruction attempts
1c39d11722891fc0db1eee036c95df23ce7775828ad08d5f61945bb300abe3a0  q2P.py         item 4 branch-P q2 codim
d3187857ae14e682e0a8f28873f981748d6e0879efc62b78a321701f31bd8871  res2.py        item 4/5 residues + q2 codim, both branches
c47b2d6523fb3feba650bfca1571e83984fc6a8a0c6c79f70b3f6d957629175f  branchQ.py     item 5 branch-Q q1 codim
a722bf8600a419c3e43931e10f3ff1606f454e31e3fd4c2f015ab902bb3d29a0  wt2.py         item 6 weight-2 identities + branch-Q transversality
03aa7aa8dbe48b6536e90e5043b41bef047e2bced708a76ec1a90691d1e485ca  arch.py        item 6 R_n absorption + ker L_n
eec288d6f4a736c78404662112b5380c3d061f13377567e99db5e0c3619f19c6  wt3.py         item 6 weight-3 probe
0c30d9893e23728c2ed54a2ab4ff611ef24194c128a7d467743467445b5a0ba8  final.py       intersection dimensions
d35a512c2d5e5f71913b32c04d7fe9ae5c43f400de9070bf87ab14b3eeb3e318  res.py         SUPERSEDED, see self-correction below
```

**Self-correction, recorded because it changed a printed number.** My first
`H`-parametrised `q2` script (`res.py`) derived `F2 * H^(K-1) = 4(H R' - K H' R)`
from `g = R/H^K`; the correct clearing is `F2 * H^K = 4(H R' - K H' R)`. The
buggy version printed branch-P `q2` codim 3 and branch-Q codim 4, which
disagreed with my independently written `A`-parametrised script (`q2P.py`,
correct). `res2.py` is the corrected version; it agrees with `q2P.py` and
with the hand derivation. **All `q2` codimensions quoted below (4 on branch P,
5 on branch Q) come from the corrected script and are hand-confirmed.**

Producer `[desk-checked]` tags were treated as claims, not evidence. I did
not use agreement with any ideation of my own as evidence; every number
below has either a hand proof or two independently written scripts.

---

## Item 1 — the `q1`/`q2` formulas and their licensing rows

**Verdict: CONFIRMED.** One inherited census error: **GAP/REPAIR.**

### 1.1 The two coefficients

Setup as in R7R1: `F0 = H^2`, `p^4 = H`, `P = F^(1/8)`, `s = t/P`,
`Q = P^2 = F^(1/4) = sum q_n s^n`.

Hand derivation (independent of the producer's route, which went through
`H^(1/2)(1+F1 t/H^2+...)^(1/4)`):

```text
Q = F^(1/4) = p^2 [ 1 + (1/4)F1 H^-2 t + ((1/4)F2 H^-2 - (3/32)F1^2 H^-4) t^2 + O(t^3) ]
P = F^(1/8) = p   [ 1 + (1/8)F1 H^-2 t + O(t^2) ]
t = s P       ==>  t = s p + (1/8) F1 H^-2 p^2 s^2 + O(s^3)
```

Order `s`:   `(1/4) p^2 F1 H^-2 * p = F1 p^3 / (4 p^8) = F1/(4 p^5)`.

Order `s^2`: `(1/32) F1^2 H^-3` (from the reversion term) plus
`(1/4)F2 H^-1 - (3/32)F1^2 H^-3` (from the `t^2` coefficient), total
`F2/(4H) - F1^2/(16 H^3)`.

Both match R7R1 (0.4) exactly. Independently re-verified symbolically in
`Z[F1,F2][p,p^-1]` (`q1q2.py`), which returns

```text
q0 = p^2 ,  q1 = (1/4) F1 p^-5 ,  q2 = (1/4) F2 p^-4 - (1/16) F1^2 p^-12
q1 - F1/(4p^5) == 0 : True
q2 - [F2/(4H) - F1^2/(16H^3)] == 0 : True
```

The producer's §3.1 remark that `q_n` depends on `F` alone is trivially
correct (`Q = F^(1/4)`) and correctly restricted to the 124 free `F` slots
plus `H`. **CONFIRMED.**

### 1.2 Licensing rows

R7R1's truncation schedule: for `E = t^22 + O(t^N)` the licensed rows are
exactly `q_n` with `n+22 < N`. Hence

* `q0` licensed at `N >= 23` (endpoint only);
* `q1` licensed iff `N >= 24`, i.e. **row `D23` must be imposed**;
* `q2` licensed iff `N >= 25`, i.e. **rows `D23` and `D24`**.

§3.4's statement ("`q1` needs row 23 and `q2` row 24") is exactly this.
**CONFIRMED.** D5G currently freezes only `D0..D22`, so *neither* `q1` nor
`q2` is licensed at the truncated tier today; the whole Card-1 instrument
is exact-tier-only until `D23`/`D24` are frozen. The producer states this
correctly and I confirm the tier firewall is drawn in the right place.

### 1.3 The row census — GAP/REPAIR (inherited)

§3.1 item 2 writes the exact system as
`D1..D21=0, D22=1, D23..D35=0` — "thirteen rows beyond the endpoint".

Rederived from the D3 lattice (`lattice.py`, all figures independently
recomputed from the polygon inequalities, not read from any table):

```text
F windows:  max(0, ceil((n-8)/3)) <= i <= 16-n   -> empty for n>=15   [verified n=0..15]
G windows:  max(0, ceil((n-12)/3)) <= i <= 24-n  -> empty for n>=22   [G15..G22 sizes 9,7,6,5,3,2,1,0]
F slots 141 total / 17 at weight 0 / 124 free ;  G slots 301 / 25 / 276 free ;  400 positive
deg_t E <= 14 + 21 = 35
```

So the window facts in §3.1 items 2-3 (including "the `G22` window is
empty", hence no `G22` handle at the endpoint) are **CONFIRMED**.

But by corrected R7R1, `D35 == 0` identically: the unique top slots are
`f_2_0` (`X^2` at weight 14) and `g_3_0` (`X^3` at weight 21), and

```text
D35 = (12-21) F14' G21 + (14-8) F14 G21' = -9(2cX)(dX^3) + 6(cX^2)(3dX^2) = 0 .
```

I recomputed this from the row formula with generic top coefficients and
got the zero polynomial, and recomputed the sharp maximum `D34` witness
`f_2_1 * g_3_0` with coefficient `-3` (script returns `-33 X^4` for `g`
coefficient 11). So the correct exact system is

```text
D0 = ... = D21 = 0   (D0 forced by F0=H^2, G0=H^3),   D22 = 1,   D23 = ... = D34 = 0,
```

**twelve** rows beyond the endpoint, not thirteen; `D35` is automatic. The
producer's "thirteen" repeats the unsharp bound that the corrected R7R1
retired. **GAP/REPAIR, non-load-bearing** — the licensing of `q1`/`q2`
needs only `D23`/`D24`, and nothing in §§3.1-3.3 or Card 1 depends on the
top row. The ideation's blindness disclosure (it explicitly did not read
the R7R1 review, which postdates the packet seal) means this is an
inherited figure, not a process fault.

### 1.4 §3.2's `gamma_n` identity (in charged range)

Claim: `L_n(G) = -8 H^(2-gamma_n) (H^(gamma_n) G)'` with `gamma_n=(n-12)/4`.
Hand check:

```text
-8 H^(2-g) (H^g G)' = -8 H^(2-g) [ g H^(g-1) H' G + H^g G' ] = -8 g H H' G - 8 H^2 G'
Grok's  L_n(G) = 2H[(12-n)H'G - 4HG'] = 2(12-n) H H' G - 8 H^2 G'
equal  <=>  -8g = 2(12-n)  <=>  g = (n-12)/4 .
```

**CONFIRMED**, and it is an identity for every `n`, not only `15..21`.
`gamma_16 = 1`, `gamma_20 = 2` are the rational ones in the block, as
stated.

Caveat on the framing, not the identity: calling the collection "**one**
`mu4`-graded de Rham complex on `y^4=H`" is a metaphor, not a proved
structure. (i) On branch P, `y^4 - H = y^4 - A^2 = (y^2-A)(y^2+A)` is
reducible, so there is no `mu4` cover there and `[L:K(X)] = 2`, not 4.
(ii) The F-side exponents (`i/4` from the `p^i` components) and the G-side
exponents (`gamma_n = (n-12)/4`) are different gradings. (iii) There is no
differential squaring to zero; these are decoupled first-order operator
equations `D_lambda(Y) = H^-lambda (H^lambda Y)'`. The **common operator
species** is real and is a good observation; the "one complex" wording is
unproved framing.

---

## Item 2 — the branch-P `q1` theorem

**Verdict: CONFIRMED, every sub-claim, with two sharpenings the producer
did not state.**

### 2.1 Reduction to `w^2 = A`

`H = A^2` with `deg A = 4` gives `p^4 = A^2`, so `p^2 = eps A`,
`eps in {+1,-1}`, and `L = K(X)(w)` with `w = p`, `w^2 = eps A`. Take
`eps = +1` first. Then `p^5 = p^4 p = A^2 w` and

```text
q1 dX = F1 dX / (4 A^2 w)   =   F1 w dX / (4 A^3) ,
```

matching §3.3's displayed form `[F1 dX/(4A^2 w)] = 0` exactly. **CONFIRMED.**

Because `L/K(X)` is separable of degree 2, every `f in L` is uniquely
`f = f0 + f1 w` with `f_i in K(X)`, and

```text
d(f0 + f1 w) = [ f0' + w ( f1' + f1 A'/(2A) ) ] dX .
```

`q1 dX` is purely odd, so `f0' = 0` and the whole gate is the **rational**
first-order equation

```text
(*)   v' + v A'/(2A) = F1/(4A^3),      v = f1 in K(X).
```

Note this decoupling uses only `K(X)`-linear independence of `1, w`; it
needs **no roots of unity and no base change** — a simplification of the
producer's `mu4` language, and the reason the base-field audit below is
clean.

### 2.2 Primitive completeness — CONFIRMED (producer's compressed reason is right)

The producer writes: "odd primitives with poles only over `A` and infinity
are exactly `Qw/A^2` ... (higher `A`-orders force `A|Q`; lower orders absorb
via `Q -> AQ`)". This is correct but stated as an ansatz. The honest proof:

*Uniqueness.* Two solutions of (\*) differ by a solution of `v' = -vA'/(2A)`,
i.e. `v^2 ~ 1/A`; since `A` is squarefree of degree 4 it is not a square in
`K(X)`, so the only rational homogeneous solution is `v = 0`. **The
primitive, if it exists, is unique** (up to the additive constant `f0`).

*No poles off `A`.* At `beta` with `A(beta) != 0`, if `ord_beta(v) = m < 0`
then `ord(v') = m-1` with leading coefficient `cm != 0` while
`ord(v A'/(2A)) >= m > m-1`, so `ord(LHS) = m-1 < 0`, contradicting
`ord(RHS) >= 0`. (This argument is valid for *any* `A`.)

*Pole order exactly `<= 2` at roots of `A`.* At a **simple** root `alpha`,
`A'/(2A) = 1/(2(X-alpha)) + O(1)`, so with `ord_alpha(v) = m` the coefficient
of `(X-alpha)^(m-1)` in the LHS is `c(m + 1/2) = c(2m+1)/2`, which is
**never zero for integer `m`**. Hence `ord(LHS) = m-1` exactly, and
`ord(RHS) = ord_alpha(F1) - 3 >= -3` forces `m >= -2`.

Therefore `A^2 v in K[X]`; set `Q := A^2 v`. Conversely

```text
d(Q w / A^2) = (2AQ' - 3A'Q) dX / (2 w A^2)
```

(hand-verified: put everything over `2wA^3` using `w^2 = A`, `w' = A'/(2w)`),
which matches the producer's formula. Setting this equal to
`F1 dX/(4A^2 w)` gives

```text
F1 = 2 (2AQ' - 3A'Q).
```

**Sharpening the producer's phrasing:** the literal solution set is
`2 * im(T_A)` where `T_A(Q) = 2AQ' - 3A'Q`. As *subspaces of* `K[X]_(<=15)`
these coincide, so "`F1` is exactly the image of `Q -> 2AQ'-3A'Q`" is
correct as a subspace statement — the factor 2 is not an error, but a
successor freezing an explicit certificate must carry it.

**The resonance is exactly where squarefreeness is load-bearing.** This is
the point the producer's one-line parenthetical hides:

*Injectivity.* `T_A(Q) = 0` gives `2Q'/Q = 3A'/A`; comparing residues of the
logarithmic derivatives, every root of `A` occurs in `Q` and `2k_i = 3m_i`,
so every `m_i` is even. Hence

```text
ker T_A != 0   <=>   A = c * (perfect square) ,
```

and then `Q = e * (sqrt(A/c))^3`, of degree `3 * (deg A)/2 = 6`. So
squarefreeness is *sufficient* (producer's "`Q^2 ~ A^3`" reason is right)
but the exact criterion is "`A` not a constant times a square", and the
kernel, when it exists, sits **precisely at `deg Q = 6`** — the same degree
as the producer's Card-1 "`deg Q = 6` resonance". Verified: for
`A = X^4-1`, `deg T_A(X^d)` for `d = 0..14` is
`3,4,5,6,7,8,**5**,10,11,12,13,14,15,16,17` — the drop at `d = 6` is the
leading-coefficient cancellation `2(d-6) lc(A) lc(Q)`, and `A` squarefree
keeps the kernel empty there.

*Degree bound.* `deg T_A(Q) = deg Q + 3` for `deg Q != 6` (and `<= 8` at
`deg Q = 6`). So `T_A(K[X]_(<=12)) subset K[X]_(<=15)`, and no `Q` of degree
`>= 13` can land in the window. **`deg Q <= 12` is forced, not assumed.**

*Conclusion.* `dim im = 13`, `dim K[X]_(<=15) = 16`, **codimension exactly 3**.
**CONFIRMED.**

### 2.3 Infinity and branch behavior — CONFIRMED

*Branch points.* Near a root `alpha` of `A`, `w` is a uniformiser,
`X - alpha = w^2/A'(alpha) + O(w^4)` is **even** in `w`, and
`dX = (2w/A'(alpha) + O(w^3)) dw`. Hence

```text
omega = F1 w dX/(4A^3) = [ even Laurent series in w ] * w^-4 dw ,
```

whose `w^-1` coefficient vanishes. **Branch-point residues vanish
identically** — the producer's parity reason ("`dX ~ w dw`") is exactly
right, and this is the fact that makes the count come out to 3 rather than 7.

*Infinity.* `deg A = 4` even and `A` squarefree, so the cover is unramified
over `infinity` and there are two points `inf_+`, `inf_-`, swapped by
`w -> -w`; since `omega` is odd, `res_(inf_-) = -res_(inf_+)`, so infinity
contributes **one** functional. With `u = 1/X`, `B = A/X^4`,

```text
omega = -(1/4) sum_k c_k u^(8-k) B^(-5/2) du ,   res_(inf_+) = -(1/4) sum_(k>=9) c_k b_(k-9)
```

where `B^(-5/2) = sum b_j u^j`. For `A = X^4-1` this is
`-(1/4)c_9 - (5/8)c_13`; it is **nonzero** (take `F1 = X^9`), it annihilates
the whole image, and it lies in the computed 3-dimensional cokernel
(`coker.py`, all three checks `True`).

*Identification of the three functionals.* All residues of `omega` vanish
`<=>` the one infinity functional vanishes; `omega` is then of the second
kind, and classically a differential of the second kind on a compact curve
is exact iff its class in `H^1_dR` vanishes — here `dim H^1_dR = 2g = 2`
for the genus-one curve `w^2 = A`. Total `1 + 2 = 3`, matching the
algebraic codimension exactly, so the map from the 16-dimensional window to
`(residue) (+) H^1_dR` is surjective. **The producer's identification "one
residue pair at infinity plus the two compact `H^1_dR` classes" is
CONFIRMED**, and it is now a second, independent proof of codimension 3.

### 2.4 Base field — CONFIRMED

`T_A` is defined over the field of definition `K` of `A`; injectivity and
the rank of an explicit `16 x 13` matrix are preserved under every field
extension, so **codim 3 is stable under arbitrary base change**. Two honest
caveats the producer does not state: (i) on branch P `[L:K(X)] = 2`, so the
`mu4` grading of R7R1's repair 2 is *unavailable* here (`p -> i p` maps
`p^2 = A` to `-A`, not an automorphism) — but nothing in the proof needs it;
(ii) if one writes `A = c C^2` with `c` a non-square (item 5 stratum), `w`
requires a constant-field extension. Neither affects the squarefree
statement.

### 2.5 Twist invariance — CONFIRMED

On `p^2 = -A`: `p^5 = p^4 p = A^2 p` still, so `q1 = F1/(4A^2 p)` unchanged;
using `1/p = -p/A`,

```text
d(Q p/A^2) = p (2AQ' - 3A'Q)/(2A^3) ,     q1 dX = -F1 p dX/(4A^3) ,
==>  2AQ' - 3A'Q = -F1/2 .
```

The condition is `F1 in -2 * im(T_A) = im(T_A)`: **literally the same
subspace**. Producer's claim CONFIRMED, with the sharper statement that the
two twists give the *same linear system up to an overall sign*, not merely
the same dimension.

---

## Item 3 — the rank-13 fixture and a load-bearing mutation

**Verdict: rank 13 CONFIRMED (three independent routes). The "27 candidate
generators" bookkeeping is GAP/REPAIR — unreconstructable.**

### 3.1 Rank 13, reproduced

Three independent computations for `A = X^4-1`:

1. Direct: `rank{ T_A(X^d) : d = 0..12 } = 13` (`coker.py`).
2. Uniform, ansatz-free: solve the linear system
   `F1 * A^(K-2) = 4AQ' + (2-4K)A'Q` for `v = Q/A^K`, `deg Q <= 40`, and
   project onto `F1`. Dimensions for `K = 2,3,4,5` are `13,13,13,13` —
   **stabilised at `K = 2`**, which is an independent confirmation of the
   pole-order-2 primitive-completeness claim of §2.2 (`branchP.py`).
3. Geometric: `16 - (1 residue + 2 periods) = 13` (§2.3).

The cokernel is 3-dimensional with basis (rows of the rref, `coker.py`)

```text
phi_1 = c_0/3           - c_4/15        + c_8/3      + c_12
phi_2 =                                   (2/5)c_9   + c_13
phi_3 = -(5/77)c_2      + (5/77)c_6     + (5/11)c_10 + c_14
```

Note the supports are the residue classes `0, 1, 2 mod 4`: for `A = X^4-1`
the cokernel is `mu4`-isotypic under `X -> i X`. That is a property of the
`4|delta` fixture, not of a generic `A` (see item 5), and it is a good
discriminator for anyone replaying the fixture.

### 3.2 The "27 candidate generators" — GAP/REPAIR

§3.3 says "rank 13 of the 27 candidate generators confirmed exactly for
`A=X^4-1`". The text never defines the 27 generators and I could not
reconstruct the figure under any natural reading (`twentyseven.py`):

```text
Q of deg <= 26 (27 gens), truncated to coeffs 0..15   -> rank 16  (not 13)
Q of deg <= 26, untruncated                           -> rank 27
Q of deg <= 12 (13 gens)                              -> rank 13
families d(X^k w/A^j), j=1,2,3, deg <= 15             -> 22 gens, rank 13
```

The **conclusion** (rank 13) is confirmed by all three of my independent
routes; the **generator count** is a bookkeeping figure that no reader can
check as written. Immaterial to the theorem; a successor must define its
generating set explicitly.

### 3.3 Load-bearing mutation

The strongest available mutation is one that passes *both* cheap surrogate
tests and still fails the gate:

```text
MUTATION:   A = X^4 - 1,   F1 = A = X^4 - 1
  * satisfies the post-seal weight-2 compatibility gate  A | F1        YES
  * has zero residue at infinity (phi_2 support is c_9,c_13; both 0)   YES
  * lies in im(T_A) ?                                                   NO
      phi_1(F1) = (1/3)(-1) + (-1/15)(1) = -2/5 != 0
```

So `F1 = X^4-1` is killed **only** by the genus-one period part of the
obstruction. This is load-bearing in three separate ways: it shows the
`q1` gate is not implied by the weight-2 divisibility gate; it shows the
gate is not implied by residue calculus alone (the two compact `H^1_dR`
classes do real work); and it is a fill a reviewer checking only residues
would wrongly pass. Contrast pair inside the same divisibility class:
`F1 = A * X^11` (degree 15, `A | F1`, zero residue) **is** in the image.
Further mutations verified (`mut.py`): `F1 = 1` (not in image, zero
residue), `F1 = X^9` (not in image, residue `-1/4`), `F1 = T_A(X^6)` (in
image, the resonance element).

---

## Item 4 — the `q2` row

**Verdict: descent CONFIRMED (with a simpler proof), residue `-3/64`
CONFIRMED, "row two cuts more" GAP/REPAIR.**

### 4.1 Descent to `K(X)` — CONFIRMED, and `mu4` is not needed

`q2 = F2/(4H) - F1^2/(16H^3)` lies in `K(X)`. §3.3 justifies descent by
"Galois averaging after the `mu4` base change". That is unnecessarily
strong. Correct argument: `L/K(X)` is separable (char 0), so for
`f in L` with `df = q2 dX`, the trace over the embeddings into a normal
closure gives `Tr(f) in K(X)` and

```text
d(Tr f) = sum_i tau_i(df) = sum_i tau_i(q2 dX) = [L:K(X)] q2 dX ,
```

since every `tau_i` fixes `X` and hence commutes with `d`. So
`g = Tr(f)/[L:K(X)] in K(X)` is a rational primitive. No roots of unity, no
base change, no Galois hypothesis. **CONFIRMED with the justification
repaired to something weaker and always available** — which matters,
because on branch P the `mu4` base change is *not* available (§2.4).

Consequence, also CONFIRMED: `K(X)` is the function field of `P^1`, so
`H^1_dR = 0` and a rational differential is exact iff **all** its residues
vanish. "The `q2` row is genus-zero residue calculus on both branches" is
correct.

### 4.2 The residue `-3/64` — CONFIRMED

`F1 = 0`, `F2 = 1`, `A = X^4-1`, `H = A^2`, so `q2 = 1/(4A^2)`. With
`u = X-1`: `A = 4u(1 + (3/2)u + ...)`, `A^2 = 16u^2(1 + 3u + ...)`,

```text
1/(4A^2) = 1/(64u^2) - 3/(64u) + O(1) ,     res_(X=1) = -3/64 .
```

Reproduced numerically-exactly (`res2.py`/`res.py` residue routine) and by
the closed form `res_alpha = -c A''(alpha)/(4 A'(alpha)^3)` for a simple root
`alpha`: `A''(1) = 12`, `A'(1) = 4`, `-12/(4*64) = -3/64`. **CONFIRMED.**

### 4.3 One excluded fill vs a branch gate — the distinction the charge asks for

The producer proves **nonvacuity**: the single fill `F1=0, F2=const != 0` is
excluded on branch P at the exact tier. That is correct and correctly
tiered. But §3.3 then summarises "row one already cuts three dimensions on
branch P, and **row two cuts more**", which invites the reading that the
tower keeps cutting the *same* (`F1`) locus. It does not. I computed the
actual gate.

**The `q2` row is a codimension-`d` affine condition on `F2` alone, where
`d` = number of distinct roots of `H`; it imposes nothing whatever on `F1`.**

Proof sketch (branch P, `A` squarefree). The `F1`-dependence of `q2` is the
fixed inhomogeneous term `-F1^2/(16H^3)`. For the linear part, local analysis
of `F2/(4H) = g'` forces `ord_alpha(g) >= -1` at each root, so `g = R/A`, and
`F2 = 4(AR' - A'R)`; the kernel is `R = A` and the degree is `deg R + 3`
(resonance at `deg R = 4`), so `deg R <= 11` and

```text
dim{ exact F2 } = 12 - 1 = 11    inside the 15-dimensional F2 window  ->  codim 4 .
```

Since `15 - 11 = 4` equals the dimension of the residue target `K^4`, the
residue map is **surjective**, so the inhomogeneous `F1^2` term is *always*
absorbable: **the `q2` row is solvable for `F2` whatever `F1` is.**

Computed dimensions (`q2P.py` and corrected `res2.py`, two independently
written parametrisations agreeing):

| `H` | distinct roots of `H` | `dim{exact F2}` | codim in 15-dim window | `F2 = const` excluded? |
|---|--:|--:|--:|---|
| `(X^4-1)^2` | 4 | 11 | **4** | yes |
| `(X^4+X^3+X+3)^2` | 4 | 11 | **4** | yes |
| `((X^2-1)^2)^2` | 2 | 13 | 2 | yes |
| `(X^2(X-1)(X-2))^2` | 3 | 12 | 3 | yes |
| `X^8` | 1 | 14 | 1 | **no** |
| `(X^3-2X/5)^2 (X^2-1)` (branch Q) | 5 | 10 | **5** | yes |

So: the producer's "row two cuts more" is **true on the `F2` window**
(codim 4 > 3, and 5 on branch Q) and **false on the `F1` window** (codim 0).
**GAP/REPAIR**, with the correct statement supplied above.

Two further repairs to the excluded-fill claim, both in the producer's
favour and both beyond what was proved:

* The exclusion is **not fixture-specific**. For general branch-P `H = A^2`
  the residue of `c dX/(4A^2)` at a simple root `alpha` is
  `-c A''(alpha)/(4 A'(alpha)^3)`, which vanishes at every root only if
  `A''` vanishes at all distinct roots of `A`. Since `deg A'' = 2 < 4`,
  that is impossible for squarefree `A`. **`F1=0, F2=const != 0` is
  excluded on the whole squarefree branch-P locus, not only for `A=X^4-1`.**
* It **fails** on exactly one stratum: `A = c(X-a)^4`, i.e. `H = c^2(X-a)^8`,
  where `q2 = const/(4(X-a)^8)` has zero residue. Verified in the table
  (`H = X^8`, `F2 = const` is exact). That stratum is a survivor
  (perfect square, `b = 0`), so the exclusion is not uniform on branch P as
  the branch label suggests.

---

## Item 5 — special strata and the branch-Q scope bound

**Verdict: GAP/REPAIR. Codimension 3 holds on *exactly* the squarefree
locus; every degeneration of `A` drops it. Branch-Q genus 3 CONFIRMED and
its codimension proved exactly 4 (the producer's "expected larger than 3"
was right but unproved).**

The producer's `[desk-proved for squarefree quartic A]` tag is honest; the
branch-P bullet header ("`H=A^2`, `deg A=4`") is not, and Card 1 lists the
special strata only as future work. I bounded them.

### 5.1 Branch-P strata (exact, `branchP.py`, `v = Q/A^K` with `K = 2..5`)

| `A` | `A` squarefree? | `dim{exact F1}` | **codim** | geometry of `w^2 = A` |
|---|---|--:|--:|---|
| `X^4-1` (`4|delta`) | yes | 13 | **3** | genus 1, 2 pts at inf |
| `X^4+7` (`4|delta`) | yes | 13 | **3** | genus 1 |
| `X^4+X^3+X+3` (generic) | yes | 13 | **3** | genus 1 |
| `X^4+2X^3-X^2+5X-2` (generic) | yes | 13 | **3** | genus 1 |
| `X^2(X-1)(X-2)` | no (double root, not a square) | 14 | 2 | genus 0, 2 pts over `X=0`, 2 at inf |
| `(X^2-1)^2` | no (square) | 14 | 2 | `w in K(X)`; `P^1`, 2 poles |
| `X^2(X-1)^2` | no (square) | 14 | 2 | `P^1`, 2 poles |
| `(X^2+X+3)^2` | no (square) | 14 | 2 | `P^1`, 2 poles |
| `X^3(X-1)` | no (triple root) | 15 | 1 | genus 0 |
| `X^4` | no (4th power) | 15 | 1 | `L = K(X)`, one pole |
| `(X-1)^4` | no (4th power) | 15 | 1 | `L = K(X)`, one pole |

Every number has an independent geometric derivation, so this is not a
numerical extrapolation:

* squarefree: 4 branch points (residues 0 by parity) + 1 infinity residue
  + `2g = 2` periods = **3**;
* `A = C^2`, `C` squarefree quadratic: `w = C in K(X)`, `q1 = F1/(4C^5)` on
  `P^1`, two residue conditions, no periods = **2**;
* `A = X^2 * (squarefree quadratic)`: `w = X sqrt(...)`, genus 0; branch
  residues 0, one condition over `X=0`, one at infinity = **2**;
* `A = X^3(X-1)`: `w = X sqrt(X(X-1))`, genus 0, branch residues 0, one
  condition at infinity = **1**;
* `A = c(X-a)^4`: `L = K(X)`, `q1 = F1/(4c^(5/2)(X-a)^10)`, one residue = **1**.

The mechanism of the drop is exactly the resonance identified in §2.2: at a
root of multiplicity `e` the local indicial coefficient is `c(m + e/2)`,
which vanishes for even `e` at `m = -e/2`. **Squarefreeness is not a
convenience hypothesis; it is the whole hypothesis.** Note also that the
`K = 2` ansatz *undercounts* on the square strata (it returns 12 where the
truth is 14), so the producer's `Qw/A^2` normalisation would silently give
a wrong answer there; the pole-order-2 bound must be re-derived per stratum.

**The `4|delta` question.** Reading `4|delta` as "all exponent gaps of `A`
divisible by 4", i.e. `A = X^4 + a` (which is what the fixture `A = X^4-1`
is): the codimension is still **exactly 3** — the special modes change the
*shape* of the cokernel (it becomes `mu4`-isotypic, §3.1) but not its
dimension. So the fixture is drawn from a special stratum, but the number
it reports is generic. Verified on `X^4-1` and `X^4+7`. If the intended
reading of `delta` is the discriminant, I did not test that reading and say
so rather than guess.

### 5.2 Branch Q

`H = A^2 B`, `deg B = 2` squarefree, `deg A = 3` (forced by `deg H = 8`),
`A = N_B(v)` per R6.

*Genus.* `K(X)(p^2) = K(X)(A sqrt B) = K(X)(sqrt B)` is a conic `C_0`
(genus 0, 2 points at infinity since `deg B = 2`). `L = C_0(sqrt(A y))`,
`y^2 = B`. On `C_0`, `div(Ay)` has odd order at the 6 points over the roots
of `A` and at the 2 zeros of `y`, and order `-4` at each infinity, so there
are **8** branch points and Hurwitz gives `2g_L - 2 = 2(-2) + 8 = 4`,
`g_L = 3`. **The producer's "computed here, unverified" genus-three claim is
CONFIRMED.**

*Codimension — proved, not expected.* Here `[L:K(X)] = 4` (`X^4 - A^2B` is
irreducible: `A^2B` is not a square because `B` is squarefree, and
`-4A^2B` is not a fourth power by a degree/radical count). Decomposing
`f = sum f_i p^i` over the `K(X)`-basis and using `p' = H'p/(4H)`,

```text
d(f_i p^i) = p^i [ f_i' + (i/4)(H'/H) f_i ] dX ,
```

and `q1 = F1/(4p^5) = F1 p^3/(4H^2)` sits in the `i = 3` component:

```text
f_3' + (3/4)(H'/H) f_3 = F1/(4H^2) .
```

Local indicial coefficient at a root of `H` of multiplicity `e` is
`m + 3e/4`, never zero for `e in {1,2}`; the bounds give `f_3 = Q/(A^3 B)`
and

```text
F1 = 4AB Q' - (6A'B + AB') Q ,
```

leading coefficient `4(d-5)`, kernel `Q^4 ~ A^6 B` empty, so `deg Q <= 11`
and `dim im = 12`: **codimension exactly 4** in the 16-dimensional `F1`
window. Confirmed by the uniform linear system for `(a,b) = (3,1), (4,2),
(5,2)`, all returning 12, on three different `(A,B)` including the R5
survivor pair `B = X^2-1, v = X^2/5 -> A = X^3 - (2/5)X` and the Sol-ultra
audit fixture `A = 5X^3-4X^2+X+1` (`branchQ.py`).

So the producer's "expected codimension larger than 3" is **CONFIRMED and
upgraded to `= 4`**, but it was an expectation in the source and must not be
promoted from that document.

---

## Item 6 — the strategic "decoupling" claim

**Verdict: REFUTED as written.** The three-line display in §3.1 is a list of
*necessary* conditions, not a decomposition of the face decision, and it
omits 14 of the 22 vanishing rows. Two of its three lines also need
correction. A repaired — and strictly stronger — architecture follows.

### 6.1 What the display omits

```text
(F-gates)  every [q_n dX]=0 in L           — analytic, F-only;
(G-step)   mixed_n in im(L_n), n=15..21    — unique G-completion;
(endpoint) mixed_22 = 1                    — one bilinear evaluation.
```

* Rows `D1,...,D14` do not appear anywhere. They are 14 genuine equations
  coupling `F1..F14` (124 slots) and `G1..G14` (243 of the 276 free `G`
  slots) — i.e. **367 of the 400 positive slots** are governed by rows the
  display does not mention.
* The `q_n` gates cannot substitute for them. By R7R1, `E = t^22` implies
  every `[q_n dX] = 0`; the converse constructs a formal `W` over `L`, and
  R7R1's own firewall says "the converse need not descend to `K(X)` or
  produce polynomials". So `(F-gates) & (G-step) & (endpoint)` is *implied
  by* the face system and does not imply it. Calling this a decomposition
  of "the exact-tier face decision" is a category error.
* Consequently "**No Groebner elimination on 400 bilinear slots is required
  to decide the face**" is not established. This is exactly consequence 6 of
  the post-seal audit: "although every new-weight equation is linear in the
  new slots, the existential problem in the accumulated earlier parameters
  is nonlinear."

Minor, already charged: "the finite system `D_1..D_21=0, D22=1, D23..D35=0`
— thirteen rows beyond the endpoint" should read `D0..D21=0` (with `D0`
automatic), `D22=1`, `D23..D34=0` — **twelve** rows (§1.3).

Correct in the display: `L_n` **is** injective for `n = 15..21`, because
`ker L_n` is spanned by `H^((12-n)/4)`, a negative power of `H` there, hence
no polynomial mode; and the `G22` window **is** empty, so `D22 = mixed_22`
is a single bilinear evaluation. Both **CONFIRMED**.

### 6.2 The repaired architecture (my derivation; desk tier, unreviewed)

The producer restricted the G-step to `n >= 15` because `F_n` also enters
`D_n` for `n <= 14`. That obstruction is illusory. From the chart row
`D_n = sum_(i+j=n) [(12-j)F_i'G_j + (i-8)F_iG_j']`, the `F_n` handle is the
`(n,0)` term `3H^2[4H F_n' + (n-8) H' F_n]`, and one computes

```text
L_n( (3/2) H F ) = -3H^2 [ 4H F' + (n-8) H' F ] .
```

Hence, with `R_n := G_n - (3/2) H F_n` (`R_n = G_n` for `n >= 15`),

```text
D_n = L_n(R_n) + mixed_n(F_(<n), R_(<n))      for every n = 1..21 .
```

Both identities verified symbolically on random data for all `n = 1..21`
(`arch.py`, `True`). This is the weight-2 cancellation of the post-seal
audit, generalised to every weight, and it says the raw `F_n` slot is
**pure gauge** inside its own row: the entire lower system is a cascade in
`F` alone plus the free homogeneous modes.

The homogeneous modes are *not* absent below weight 15, contradicting the
"unique G-completion" framing: `ker L_n = <H^((12-n)/4)>`, which on
**branch P** (`H = A^2`) is the polynomial `A^((12-n)/2)` for every even
`n <= 12`, and each lies inside its `G_n` window (`deg = 24-2n <= 24-n`).
Verified for `n = 2,4,6,8,10,12` (`arch.py`). So the branch-P completion
carries **six free constants** (`n = 2,4,6,8,10,12`); on branch Q only
`4 | (12-n)` survives, i.e. `n = 4,8,12`.

### 6.3 The post-seal weight-2 correction, re-derived

I re-derived the audit's weight-1/weight-2 results from scratch rather than
consuming them (`wt2.py`, all `True` on three random `(A,F1,F2)`):

```text
D1 = 0  and ker L_1 has no polynomial mode  ==>  G_1 = (3/2) H F_1   (unique)
mixed_2 = 11 F_1' G_1 - 7 F_1 G_1' = 6H F_1F_1' - (21/2) H' F_1^2
L_2( (3/8) F_1^2 / H ) = -mixed_2                     [cleared form: 28 N H' - 8 H N', N=(3/8)F_1^2]
ker L_2 (branch P) = <A^5>, a polynomial that cannot cancel a pole
==>  R_2 = (3/8)F_1^2/H + c_2 A^5 polynomial  <=>  H | F_1^2  <=>  A | F_1   (branch P)
                                                              <=>  AB | F_1  (branch Q)
```

All windows accommodate this (`deg R_2 <= 22` = the `G_2` window maximum),
so there is no extra window obstruction. **The audit's (3.1)-(3.4) are
CONFIRMED independently.**

This **REFUTES Card 1's target-gap sentence** ("no tractable necessary
conditions on the raw `F` slots beyond the `q_0`/endpoint row"). The
weight-2 gate is a necessary condition on raw `F1`, it is *linear* after
factorisation, and it is available at a **strictly cheaper tier**: it needs
only `D1 = D2 = 0`, which any landing satisfies at any truncation `N >= 3`,
whereas `q1` needs `D23`. The ideation's blindness disclosure explains why
it was missed; the sentence is nonetheless false.

### 6.4 But the `q1` gate is *not* subsumed — the decisive check

This is the finding that saves the atom, and it is the thing a hostile
referee must check before either promoting or discarding Card 1.

`A | F1` cuts the 16-dimensional window to **12**; `im(T_A)` is **13**; they
are **transverse**, so their intersection is `12 + 13 - 16 = 9`. Computed
for `A = X^4-1` and `A = X^4+X^3+X+3`: intersection dimension **9** in both
(`mut.py`, `final.py`), with the closed-form basis
`A * (2A R' - A' R)`, `deg R <= 8` (dimension 9, verified inside the image).
**The marginal codimension of the `q1` gate given the weight-2 gate is still
exactly 3.** Branch Q likewise: `AB | F1` gives dimension 11, image 12,
intersection **7**, marginal codimension **4** (`wt2.py`).

I then pushed one row further, since item 6 asks me to account for
`D1..D14`. **New (mine, desk tier, unreviewed):**

> **Weight-3 gate, branch P, `A` squarefree.** `D1 = D2 = D3 = 0` with all
> slots polynomial forces `H | F1`, i.e. `A^2 | F1`.

*Proof.* Write `F1 = AR` (weight-2 gate). Then `G_1 = (3/2)A^2 F_1` and
`R_2 = (3/8)R^2 + c_2 A^5`, so
`mixed_3 = 10F_1'G_2 - 7F_1G_2' + 11F_2'G_1 - 6F_2G_1' ≡ (15/4) A' R^3 (mod A)`.
But `L_3(G) = 4A^3(9A'G - 2AG')`, so `im(L_3) ⊆ A^3 K[X]`, whence
`A | A' R^3`; `A` squarefree gives `gcd(A,A') = 1`, so `A | R^3`, so
`A | R`, so `A^2 | F1`. `[]`

Checked exactly for `A = X^4-1` by solving `mixed_3 + L_3(G_3) = 0` for
`(F_2, c_2, G_3)` (`wt3.py`):

| `F1` | `A|F1` | `A^2|F1` | in `im(T_A)` | weight-3 solvable |
|---|---|---|---|---|
| `A` | yes | no | **no** | **no** |
| `A(X+1)` | yes | no | no | no |
| `A X` | yes | no | **yes** | **no** |
| `A^2` | yes | yes | **no** | **yes** |
| `A^2(X+2)` | yes | yes | **no** | **yes** |
| `A^3` | yes | yes | **no** | **yes** |
| `A^2 X^7` | yes | yes | yes | yes |
| `0` | yes | yes | yes | yes |

The two boxed disagreements are the point: `F1 = A X` passes `q1` and fails
weight 3; `F1 = A^2, A^2(X+2), A^3` pass weight 3 and fail `q1`. **Neither
gate implies the other.** Quantitatively, `{H | F1}` has dimension 8, and
its intersection with `im(T_A)` is **5** (`= 8 + 13 - 16`, transverse), with
closed-form basis `A^2 (2A R' + A' R)`, `deg R <= 4` — verified for two
different `A`. So on branch P, weights 1-3 plus `q1` cut the 16-dimensional
`F1` window to **5 dimensions**, with `q1` contributing marginal
codimension 3 on top of a cheaper codimension-8 cascade gate.

I did **not** test weights 4-14; whether they eventually imply the `q1` gate
is open, and is the single most valuable thing a successor can settle.

---

## Separation: the atom versus the strategy

**Atom (survives, and is stronger than stated).** §3.3's branch-P `q1`
theorem, its proof skeleton, its residue/period identification, its
twist-invariance, its scoping tag `[desk-proved for squarefree quartic A]`,
and §3.1's observations that the `q_n` are `F`-only, that finitely many
honest rows license an infinite tower, and that `L_15..L_21` are injective
with an empty `G22` window. Plus §3.2's `gamma_n` operator identity.

**Overstatement (does not survive).** §3.1's claim that the face decision
*decomposes* into the displayed three items, and that no elimination on the
400 bilinear slots is needed to *decide* the face; §3.1's "thirteen rows";
§3.3's "row two cuts more" read as an `F1` statement; §3.3's branch-Q
codimension expectation (true, but unproved there); the unreconstructable
"27 candidate generators"; Card 1's target-gap premise; and the "one `mu4`
de Rham complex" framing where the branch-P cover is reducible.

The ideation's own tier discipline is good — it labels everything
`IDEATION / DESK-DERIVED, UNREVIEWED`, tags R7R1/R6 `PROVISIONAL`, and draws
the truncated/exact firewall in §3.4 in the right place. The failures above
are mathematical scope, not custody.

---

## Maximum promotable scope

Promotable at **desk tier, conditional on R7R1 (PROVISIONAL)**, after
different-model replay of this review:

> **Theorem (branch-P `q1` gate).** Let `char K = 0`, `A in K[X]` monic of
> degree 4 and **squarefree**, `H = A^2`, `L = K(X)(p)` with `p^4 = H` (so
> `p^2 = eps A`, `eps = +/-1`, `[L:K(X)] = 2`). On the frozen D3 raw window
> `F1 in K[X]_(<=15)` (dimension 16), the R7R1 row-one condition
> `[q1 dX] = 0` in `L` holds **iff** `F1 in im(T_A)`,
> `T_A(Q) = 2AQ' - 3A'Q`, `deg Q <= 12`. `T_A` is injective (its kernel is
> nonzero exactly when `A` is a constant times a square, at `deg Q = 6`),
> the image is 13-dimensional, so the gate has **codimension exactly 3**,
> independent of `eps` and stable under every base-field extension. The
> three functionals are the residue at infinity (one, because branch-point
> residues vanish identically by parity and the two infinite places carry
> opposite residues) together with `H^1_dR` of the genus-one curve
> `w^2 = A` (two).
>
> **Branch Q** (`H = A^2 B`, `deg A = 3`, `deg B = 2` squarefree, coprime,
> `[L:K(X)] = 4`, `L` of genus 3): the same row is
> `F1 in im(Q -> 4ABQ' - (6A'B + AB')Q)`, `deg Q <= 11`, injective,
> **codimension exactly 4**.
>
> **Independence.** On branch P the gate is transverse to the weight-2
> compatibility gate `A | F1` (intersection 9) and to the weight-3 gate
> `A^2 | F1` (intersection 5, basis `A^2(2AR' + A'R)`, `deg R <= 4`);
> on branch Q, transverse to `AB | F1` (intersection 7). Neither the
> weight-2 nor the weight-3 cascade gate implies it, and it implies
> neither.

Explicitly **not** promotable: any codimension-3 statement outside the
squarefree locus (it is 2 or 1 on every degenerate stratum); any `q2`
statement about `F1`; any claim that the face decision decouples; any claim
that the `q1` row is the first `F`-side necessary condition past `q0`.

Tier ceiling: the whole statement is licensed only when `D23` is imposed
(exact tier, or a truncated tier through `N >= 24`). D5G freezes `D0..D22`,
so **at today's frozen tier this gate licenses nothing about any landing**.
It is an instrument awaiting a tier, and R7R1 remains PROVISIONAL beneath
it.

## Cleanest exact successor

Two, in priority order.

**S1 (recommended, strictly better value per unit of tier risk): the lower
cascade compiler, weights 3-6, both survivor branches.** By §6.2 every row
`n = 1..21` is `L_n(R_n) + mixed_n = 0` with `R_n = G_n - (3/2)HF_n`, so the
solvability gates are exact, purely linear-algebraic per row, and — unlike
any `q_n` row — **require no `D23`/`D24` and therefore no tier extension at
all**. Weight 2 gives `A | F1` (recorded); weight 3 gives `A^2 | F1` (proved
above); weights 4-6 are the same computation with the six branch-P free
constants `c_2, c_4, c_6` carried symbolically. Deliverable: the exact gate
at each weight on generic `(A)` and `(A,B)`, plus the decisive open question
— whether the cascade eventually implies `im(T_A)`, which would retire
Card 1, or does not, which promotes it. Desk/exact, no Groebner, no AWS.

**S2 (the atom itself): freeze the `q1` gate as an explicit certificate.**
Both branches, generic `(A)` and `(A,B)`, with (i) the three/four cokernel
functionals as explicit linear forms carrying the factor 2 from
`F1 = 2 T_A(Q)`, (ii) the squarefree hypothesis stated as a hypothesis with
the degenerate-stratum table of §5.1 attached, (iii) the transversality
dimensions 9/5/7 as the load-bearing controls, and (iv) `F1 = A` (branch P)
as the frozen negative control — it passes both the weight-2 gate and the
residue test and fails only on the genus-one period. Card 1's proposed
positive control (a support-preserving gauge direction) and negative control
(`F2 = const`) should be **replaced**: `F2 = const` tests the `q2` row,
which by §4.3 constrains `F2` only, so it controls nothing about the `q1`
instrument.

Do **not** fund Card 1 item (iii) ("full `q2` gate with the `F1^2` quadratic
term on both branches") as an `F`-cutting instrument: §4.3 settles that the
`q2` row is always solvable in `F2` and cuts `F1` by codimension 0.

---

## Ledger

*What I proved by hand and re-verified by script:* `q1`, `q2` (§1.1);
`d(Qw/A^2)` (§2.2); primitive completeness with the indicial coefficient
`c(2m+1)/2` (§2.2); the kernel criterion "`A` = constant times a square"
(§2.2); twist invariance (§2.5); the trace descent (§4.1); the residue
closed form `-cA''/(4A'^3)` (§4.2); the branch-Q genus-3 Hurwitz count and
its codimension 4 (§5.2); `L_n((3/2)HF) = -3H^2[4HF' + (n-8)H'F]` (§6.2);
`ker L_n = <H^((12-n)/4)>` (§6.2); the weight-3 gate `A^2 | F1` (§6.4).

*What is script-only (exact rational arithmetic, no floating point):* the
degenerate-stratum dimension table of §5.1 (each entry cross-checked
against an independent geometric derivation), the cokernel functionals of
§3.1, and the weight-3 solvability table of §6.4.

*What I did not do:* weights 4-14 of the cascade; the `deg Q = 6` resonance
as an arithmetic phenomenon over non-closed `K`; the `4|delta` reading in
which `delta` is the discriminant; any statement about whether the face is
alive or dead; and any use of the Opus5 peer ideation submission, which I
did not open. No canonical ledger was edited; no AWS was launched; no file
inside `jc2-lean` was read, touched or status-inspected; this review is the
only repository file written.

*Consequences for the rest of the packet:* none. This review changes no
promotion status, retracts nothing, and adds no evidence tier. R7R1 stays
PROVISIONAL, R6 stays PROVISIONAL, the D3 polygon remains the self-declared
`R0_ARTIFICIAL_CUSP_CONTROL` fixture (`RAW_INPUT.json`,
`"scope": "artificial frozen control only"`) — which is a scope caveat
sitting under *everything* above, including the "16-dimensional raw `F1`
window": that window is a fixture window, not a proven `8_28` Newton face.

---

**Review verdict: `q1` theorem atom CONFIRMED and sharpened; §3.1
"decoupling" strategy REFUTED as written; Card 1 target-gap premise
REFUTED by the post-seal weight-2 gate, with the instrument surviving as
provably transverse to it. Promotable scope as stated above, exact-tier only
and conditional on PROVISIONAL R7R1. Recommended successor: S1, the lower
cascade compiler at weights 3-6.**

---

## Report SHA-256

Self-referential stamps cannot hash themselves, so this is the SHA-256 of
the report **body**, i.e. of every line above this `## Report SHA-256`
heading (the file as written before this stamp block was appended):

```text
432645ebbb6cd801945c82c6b27e82f5c865ea8d3131f3e1e90a9dc25585495e
```

Reproduce with:

```bash
head -n 956 xmodel/ggv-survivor-q1-q2-de-rham-gates-fable5-hostile-review-opus5-20260827.md \
  | shasum -a 256
```

**Review verdict (restated for the ledger): `q1` theorem atom CONFIRMED;
surrounding §3.1 "decoupling" strategy REFUTED as written; Card 1
target-gap premise REFUTED, instrument survives as transverse.**
