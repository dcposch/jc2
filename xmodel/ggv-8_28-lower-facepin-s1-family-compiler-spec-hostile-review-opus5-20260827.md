# Hostile review — GGV `8_28` lower-face `S1` FACEPIN / `LF40` compiler spec

Reviewer lane: Opus 5, independent different-model hostile referee
Date: 2026-08-27
Charged report:
`xmodel/ggv-8_28-lower-facepin-s1-family-compiler-spec-sol-ultra-20260827.md`
Working dir: `/Users/dc/code/math/jc2`. `jc2-lean` was not entered, read,
built, or status-inspected. No repository file was modified except this one.
All scratch work under `/tmp/ggvrev`.

Every producer verdict and prior `PASS` string was ignored as evidence.
Every formula below was re-derived from scratch, not compared against the
NU17 review until after it was independently obtained.

**Revision note (self-correction, same date).** Two defects in the first
issue of *this review* are corrected below; the charged report is not at
fault for either.

1. **Determinant generator census.** The first issue counted rows by window
   arithmetic and reported **780** generic coefficient generators. Window
   arithmetic overcounts: it does not know that a slot pair with proportional
   exponent vectors contributes nothing to the Jacobian. Re-enumerated
   directly from raw exponent pairs, the exact figures are **774** raw
   generators and **740** after `FACEPIN` substitution, and six `xi`-degree
   window endpoints move. Full derivation, table and reconciliation in §8;
   all downstream counts (§6, §10-R5, §10-R7, §12) are amended. The corrected
   census was obtained twice by disjoint code paths — direct enumeration of
   all 42441 raw slot pairs, and polynomial evaluation of the `tau`-recurrence
   on symbolic row polynomials — which agree on the total, on all 41 row
   counts, and on all 41 `xi`-windows. The charged report states no generator
   count at all; that omission is §10-R7 and is unchanged.
2. **R2 wording.** The first issue asserted that §4 of the report carries no
   field/characteristic pin. That is factually wrong and is withdrawn in
   §10-R2 (and in the §5 flag, likewise amended): the report pins
   characteristic zero in §3 and again in §4.7, which asks in terms for a
   "characteristic-zero unit-ideal certificate". The surviving defect is
   narrower — §4 freezes no base coefficient ring or serialization — and the
   warning that a modular unit ideal is not a characteristic-zero certificate
   stands unchanged.

---

## 0. Headline

**Overall: CORRECT / REPAIR.**

The report's central claim — that the raw `8_28` lower face is pinned to
`F_0 = a K_rho^2`, `G_0 = b K_rho^3`, `K_rho = xi(xi-rho)^7`, `a*b*rho != 0`
— is **TRUE and licensed**. Every arithmetic claim in the report that I
could check independently (census, windows, identity, recurrence, target row
and sign, row ceiling, `Dtil_40` structural zero, both control first-rows,
the 37 relations) is **exactly right**. Custody is clean: 16 of 16 hashes
match.

But the report's *derivation* of the pin is incomplete in a way that matters,
and one of the two routes it gestures at **is not available for this edge**:

> The base edge `(A_0, A_0') = ((8,28),(1,0))` of the `8_28` family is
> **not simple** in the sense of GGV5 Definition 2.5. I confirmed this
> against the frozen library (`lib/families.py:is_simple` returns `False`).
> Therefore GGV5 Proposition `multiplicidad`(3)'s equality clause — the
> "simple ⇒ single root" route that `jc72108/SECTION4-AUTOMATION.md:208-225`
> records as rule B1 — **cannot be invoked here**. The report never notices
> this, because it never runs the derivation; it cites GGV22's line-1132
> sentence and stops.

I supply the replacement bridge in §3.4. It is short, self-contained inside
the two fetched e-prints, and it is *strictly stronger* than the report's
route: it does not need GGV6 Proposition 2.5 (not on arXiv), and it does not
need GGV22's three-case split a)/b)/c). That is the main deliverable of this
review.

Six additional repairs (§10, §12), of which two are soundness-relevant:
the saturation instruction "**at minimum** saturate by" is a live
over-saturation hazard, and mutation control 5 as written is degenerate.

---

## 1. Custody — PASS (one hygiene repair)

### 1.1 Charged report

```text
94c10fd8c95424d7161ef4b13b7321529109426282dd0da0da2c94f6594f61c7
  xmodel/ggv-8_28-lower-facepin-s1-family-compiler-spec-sol-ultra-20260827.md
```
Recomputed locally: **MATCH**.

### 1.2 Primary sources — fetched independently into `/tmp/ggvrev`

```text
2afcbe3e6f97eb0d584b097be6ac467b225cbbfd79a4c65c404c40a46d24065e
  https://export.arxiv.org/e-print/1708.07936v1        (GGV5)   MATCH
cac83f92efca63de3da6ca811b9837061e1a343a44b8039c8748d1b72423cba7
  https://export.arxiv.org/e-print/2204.14178v1        (GGV22)  MATCH
```
Both decompress to single TeX files: GGV5 2045 lines, GGV22 2262 lines. All
TeX line numbers below refer to those files. I read the surrounding TeX
directly; the report's excerpts were not trusted.

**REPAIR (custody hygiene).** The report's §1.1 block prints the URLs
*without* the `v1` suffix while quoting v1 digests. I checked: today the
versionless endpoints return byte-identical gzip (both papers are still at
v1), so the report is currently accurate. It is not *version-pinned*: a v2
upload would silently break the custody line without changing the printed
text. Print `…/1708.07936v1` and `…/2204.14178v1`.

### 1.3 Local pins — all recomputed, all MATCH

```text
729a5ee7dd235ccca2138fd80035e08e3fed87fabf98a8fc4a0c7f9da089bd3e  lib/families.py
845d42a2d410234f889d5d846f22f7152354896c67ab3d49152469260e892c0d  tests/test_families.py
1394871719df5a9ae7726268c1ad760af3bc89e7f8e707af550e6155e9114d88  lib/FAMILIES.md
836e3c4a8ef491799cd258a26cd0b7ae04a1309b0eefcedcc3964f5288c71427  jc72108/SECTION4-AUTOMATION.md
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876  …d3_20260827/RAW_INPUT.json
012acfe5ca560757269fd6e332ed3c4bab2f1005bce43113109f31b705ffe022  …d3_20260827/FREEZE.sha256
c7ea900bdf0552c50d2a61c5a8f0f41a7b06e24eccedf5e5ab9cef3946c53556  xmodel/…-M-cokernel-interface-d3-sol-20260827.md
72f10ad7b42fd15d24bfc578ba1f8f9722ba695341307ae61642f614fe34a1ab  xmodel/ggv-second-newton-face-nu17-…-grok-20260827.md
7647f2f118d4fe9fdd060b9e3e9450b58a62e287a80e942cad6de752a3f34ae8  xmodel/…fibre-tagged-…-prototype-sol-20260827.md
971147c5c8a6d3f26c103b0a2da1095ca7c302a2cfd1e812556eaddf6d21a316  xmodel/…fibre-tagged-…-hostile-review-grok-20260827.md
676bdd3ce960221072f037e7160d457a9d1d64c8e7353891f69e9931ae71149b  cases/…fibre_tagged_…_20260827/FREEZE.sha256
3e4e608d32c44b1b0208bd5472257ba1dbe4cadf4ef5efb2ace49d3d47d756be  xmodel/…keller-face-cusp-jet-pinning-sol-20260827.md
171ff47c844331da8971a731c1ffaf20c31ed5b2ba86fdee2d0d81219eb002b0  xmodel/…keller-face-cusp-jet-pinning-hostile-review-grok-20260827.md
6928428f9cc46641a80275e2bbfa62e784c4290ff041f5089ae789507fa8804f  cases/…keller_face_cusp_jet_pinning_20260827/FREEZE.sha256
```

The D3 `FREEZE.sha256` is internally consistent: its `RAW_INPUT.json` line
equals the report's pin, and its cross-reference line for
`xmodel/…-d3-sol-20260827.md` equals the report's pin for that file.

### 1.4 What each source actually licenses

| Source | What it licenses here | What it does **not** |
|---|---|---|
| GGV5 505–528 (Prop. `multiplicidad`) | `l_{rho,sigma}(P) = x^{m a'/l} y^{m b'} p(z)`, `z = x^{-sigma/rho}y`, `p(0)!=0`; root `lambda in K^x` with multiplicity `m_lambda`; `m_lambda/m <= v_01(A-A')/gap(rho,l)`, **equality iff the edge is simple** | Does not by itself give equality here — the `8_28` edge is not simple (§3.4) |
| GGV5 545–565 (proof of (3)) | `p(z) = pbar(z^k)`, `k = gap(rho,l)`; `t = deg pbar = m*v_01(A-A')/gap`; `m_lambda <= deg pbar` (quoting GGV2 Rmk 3.8/3.9) | Its final `pbar = (z^k-c)^t` step is inside the *simple* branch |
| GGV5 589–598 (Rmk `comentarios`) | **`gamma := m_lambda/m`**; `deg(p) = m b`; `gamma <= (b-b')/gap <= b`; `gamma = b` ⇒ type III ⇒ excluded from complete chains; `gmax = min((b-b')/gap, b-1)` | Nothing about which `gamma` occurs |
| GGV5 623–646 (Def. of `Gamma`, `A_(gamma)`) | `gamma_max = min(gcd(a-a',b-b'), b-1)`; **`A_(gamma) = (a_1/l_1, b_1)` with `l_1 = lcm(l,rho)`, `b_1 = gamma`, `a_1 = a l_1/l + (gamma-b)(-sigma l_1/rho)`** | — |
| GGV5 743–765 (Rmk `bala`) | For a type-II.b regular corner: `b' < gamma <= gamma_max` and **`A_(gamma) = A_1`**, the generated corner, with `gamma = m_lambda/m` for the `lambda` of Prop. `multiplicidad`(4) | — |
| GGV22 1009–1018 | Raw corners `{(0,0),(1,0),(8,28),(0,4)}` times `(m,n)=(3,2)`; flip `phi_1: x<->y`; `(rho_0,sigma_0)=(-1,4)`, `l=1`, `(a/l,b)=(28,8)`; `en_{-1,4}(F)=(21,6)=(3/4)(28,8)` ⇒ `q=4` | Does not itself state the `(-1,4)` edge polynomial |
| GGV22 1073–1090 | The three post-transformation cases a)/b)/c); uses **GGV6 Prop. 2.5** (not on arXiv) | — |
| GGV22 **1132** | "In all the three cases the edge `{(28,8),(1,0)}` **must be of the form `y(x^4y-alpha)^7`**, corresponding to its form before the transformations." Then `phi_3: y -> y + alpha x^{-4}` reduces `{(28,8),(0,1)}` to `{(28,8),(24,7)}` | It is an assertion with a back-reference; the supporting computation is not printed |
| GGV22 1001, 287–288, 251–268, 314–317 | Prop. 4.3 conclusion `[P,Q] = x^2`; §2 dichotomy `maxdeg >= 125` or degree pair `(72,108)`; exactly two `maxdeg = 108` cases, `(8,28)*(3,2)` and `(9,27)(2,3)` | — |

The report's citation targets are accurate. Two nits: (i) it writes
"lines 1132--1140" for the edge sentence, but the sentence is line **1132**
alone; 1137–1141 is the `N(P)/N(Q)` display. (ii) It says the GGV5 citations
"carry … its seventh power". They carry `gamma`; the **`7`** comes from
`gamma_max = min(gcd(7,28), 27) = 7` together with `b_1 = gamma`, arithmetic
the report never performs. Supplied in §3.4.

---

## 2. The three-object firewall — PASS

I re-expanded both explicit pairs as literal sparse polynomials over `Q`
(exact `Fraction` arithmetic, pure Python; no CAS available in this session,
see §13).

Put `B = x(xy^4-1)^7`.

| Object | Literal | Support check | Lower face `nu=0` |
|---|---|---|---|
| Native fibre-tagged control | `f = B^2 - x - y^8`; `g = B^3 - 2x^2y^2 + y^12 + lambda*x*y^15` | `Supp(f) ⊂ 2S`, `Supp(g) ⊂ 3S`: **verified** | `F_0 = xi^2(xi-1)^14`, `G_0 = xi^3(xi-1)^21` |
| D3/R0 artificial completion | `f = B^2 - 2x^8y^32 + y^8`; `g = B^3 - 3x^16y^60 + 3x^8y^36 - y^12` | `Supp ⊂ 2S/3S`: **verified** | identical `F_0`, `G_0` |

Both therefore realize `a = b = rho = 1`. Neither is Keller: `J(f,g)` has 93
non-constant terms (native, `lambda=1`) and 56 (artificial). The report's
claim that the two agree on the lower face **because every added term has
strictly smaller `(4,-1)` weight** is exactly right — the added exponents sit
at `nu_F ∈ {8,16}` and `nu_G ∈ {8,16,24}`, i.e. `v_{4,-1} < 8` versus `= 8`
on the edge. Their upper faces genuinely differ (native `f` has upper face
`X^16 - 1`, not a square; artificial has `(X^8-1)^2`, `(X^8-1)^3`), so the
report's refusal to transport `H = X^8-1` into the family is correct.

**Raw constant bracket vs. final `psi_4` bracket `x^2` — triple-confirmed:**

1. `jc72108/SECTION4-AUTOMATION.md` step 6: `psi_j: x -> x^{-1}, y -> x^j y`,
   an `L^(1)`-morphism **not in `Aut K[x,y]`**, with
   `[psi P, psi Q] = -x^{j-2}[P,Q]`, and `j = ceil(b_0/a_0) = ceil(28/8) = 4`
   ⇒ `x^2`.
2. `lib/families.py:corner_data` computes `rhs_exp = jpsi - 2 = 2`
   independently from the lattice; I ran it read-only and got `rhs_exp=2`.
3. GGV22 line 1001 states `[P,Q] = x^2` for the emitted systems.

Everything used up to and including GGV22 line 1132 is `phi_1` (flip,
Jacobian `-1`), `varphi: y -> y + lambda x^{-k}` (Jacobian `1`) and
`phi_3: y -> y + alpha x^{-4}` (Jacobian `1`). So the raw pair's bracket is a
nonzero **constant**, and `x^2` is manufactured only by `psi_4`. The report's
firewall is sound, and `cases/emit.py:40-48`'s `open_8_28_c1/c2` are indeed
post-`psi_4` objects and not valid `LF40` inputs.

---

## 3. Source theorem and family pin — CORRECT / REPAIR

### 3.1 `S`, `(m,n)`, and which polygon is which — with a source defect

GGV22 line 1010: corners of `N(P)`, `N(Q)` are
`{(0,0),(1,0),(8,28),(0,4)}` multiplied by `(m,n) = (3,2)`.
`lib/families.py` (run read-only) returns for key `8_28`:

```text
A0=(8,1,28)  A0p=(1,1,0)  final=(11,4,7)  steps=((4,-1,3,4),)
mn=(3,2)  degP,degQ=(108,72)  S=((0,0),(1,0),(8,28),(0,4))  c=4
upper_dir=(-3,1)  rhs_exp=2
SuppP = 3S = [(0,0),(3,0),(24,84),(0,12)]
SuppQ = 2S = [(0,0),(2,0),(16,56),(0,8)]
```

This matches GGV22 lines 1010–1083, where `P` is consistently the `m`-side:
line 1075 "`the lower side of varphi(P)` has corners `m(-2,0)`, `(0,0)`,
`m(28,8)`", line 1081 `l_{1,-3}(P) = lambda x^{4m}(x^3y-a_1)^{4m}(x^3y-a_2)^{4m}`
(end `= m(28,8)`), line 1016 `l_{rho,sigma}(P) = lambda R^{4m}` with
`en(R) = (7,2)`.

**Silent P/Q swap in the source (finding).** GGV22 then reverses the
labelling without comment:

- line 1110 (figure caption): `1/2 N(P) = 1/3 N(Q)` — i.e. `N(P) = 2·shape`;
- line 1136: "we can set `(en(Q), en(P)) = ((2,1),(-1,0))`";
- lines 1139–1140: `N(P) = {(-1,0),(0,0),2(28,8),2(24,7)}`,
  `N(Q) = {(2,1),(0,0),3(28,8),3(24,7)}`;
- the Proposition statement, lines 1003–1004: `N(P)` tops out at `(8,16)`,
  `N(Q)` at `(12,24)` — ratio `2:3`.

So GGV22 has `P = 3S` before line 1090 and `P = 2S` from line 1110 onward.
The repository follows the *early* convention.

**Impact: none on the mathematics, but the report overstates.** The FACEPIN
shape is labelling-invariant: the `2`-side gets the square, the `3`-side the
cube, whatever the letters. The report's sentence

> "If the GGV pair is presented as `(P,Q)` with `P in 3S`, `Q in 2S` and
> `[P,Q]=1`, take `(f,g)=(Q,-P)` … **No unrecorded orientation swap is
> needed.**"

is *mathematically* fine (`[Q,-P] = [P,Q] = 1`) but *factually wrong as a
description of the source*: GGV22 does contain an unrecorded P/Q swap, and a
future transcriber reading Prop. 4.3's statement rather than its proof will
attach the square to the wrong letter. **REPAIR:** record the swap and pin
the orientation by *polygon*, never by letter.

Also note the report's own §3 sign bookkeeping omits that `phi_1` itself
contributes a `-1` (a flip has Jacobian `-1`). Harmless — everything is
absorbed into the `J(f,g) = 1` normalization, which is legitimate because
scaling `f -> c f` preserves `Supp(f) = 2S` and only rescales the saturated
parameter `a`. **REPAIR:** state that normalization explicitly.

### 3.2 The flip / unflip — CONFIRMED

`phi_1(x) = y`, `phi_1(y) = x`. Flipped shape `= {(0,0),(0,1),(28,8),(4,0)}`,
which is exactly the second tikzpicture of GGV22 (lines 1051–1068: origin at
`(12,0)`, step `0.25`, so `(19,2) -> (28,8)`, `(12,0.25) -> (0,1)`,
`(13,0) -> (4,0)`, `(15,0) -> (12,0)`).

Edge direction: `(0,1)` and `(28,8)` are level for `v_{rho,sigma}` iff
`sigma = -4 rho`; with `rho = -1`, `sigma = 4`. That is GGV22's
`(rho_0,sigma_0) = (-1,4)` — **verified, not assumed**. Unflipped the same
edge is `{(1,0),(8,28)}` with direction `(4,-1)`, matching
`lib/families.py` `steps=((4,-1,3,4),)`.

`z := x^{-sigma/rho} y = x^4 y` in the flipped frame. Applying `x<->y`:

```text
y(x^4 y - alpha)^7   -->   x(x y^4 - alpha)^7 .
```

Newton segment of `x(xy^4-alpha)^7`: bottom `x*(-alpha)^7` at `(1,0)`, top
`x*(xy^4)^7 = x^8 y^28` at `(8,28)` — exactly the unflipped `S` edge.
**The report's unflip is correct.**

**Source transcription defect (finding).** GGV22 line 1132 as printed reads
"the edge `{(28,8), (1,0)}`". In the flipped frame the low vertex is
`(0,1)`, not `(1,0)`; the very next clause of the same sentence writes
"reducing the edge `{(28,8),(0,1)}`". So `(1,0)` is a slip — most likely a
leftover unflipped vertex paired with a flipped one. It is self-repairing
(from the next clause and from the geometry of `y(x^4y-alpha)^7`), but the
report calls the sentence "exactly" clean and does not flag it.
**REPAIR:** record the erratum in the transcription ledger.

### 3.3 The square/cube powers — CONFIRMED

In the flipped frame with `A' = (0,1)` (so `a' = 0`, `b' = 1`, `l = 1`),
GGV5 line 508 gives `l_{-1,4}(P) = y^{m b'} p(z) = y^m p(x^4 y)`. With
`m = 3` and `en = 3(28,8) = (84,24)`, a term `z^k` sits at `x^{4k}y^{k+3}`,
so `4k = 84`, `k = 21`: `deg p = 21`. If `p = c(z-alpha)^{21}` then

```text
l_{-1,4}(P) = c * y^3 (x^4y-alpha)^21 = c * [ y(x^4y-alpha)^7 ]^3 ,
```

and identically `l_{-1,4}(Q) = c' [ y(x^4y-alpha)^7 ]^2` with `deg q = 14`.
So GGV22's `y(x^4y-alpha)^7` is necessarily the **reduced/shape-level** edge
polynomial, not `l(P)` or `l(Q)` (whose ends are `(84,24)` and `(56,16)`,
not `(28,8)`). The report's reading is *forced*, and its assignment
"square on the 2-side, cube on the 3-side" is correct.

Unflipped and pushed through the chart `x = tau^{-4} xi`, `y = tau`
(so `xy^4 = xi`):

```text
x(xy^4-rho)^7  =  tau^{-4} * xi(xi-rho)^7  =  tau^{-4} K_rho(xi).
```

Hence `F_0 = tau^8 * a * (tau^{-4}K)^2 = a K^2` and
`G_0 = tau^12 * b * (tau^{-4}K)^3 = b K^3`. **CONFIRMED** for the compiler
orientation `f in 2S`, `g in 3S`.

`alpha != 0` is forced: `p(0) != 0` (GGV5 line 508) and `lambda in K^x`
(GGV5 line 518); equivalently the vertex `(1,0)` of `S` is attained, i.e.
`f_{2,0} = a rho^14 != 0`.

### 3.4 The exponent seven — REPAIR (the report's route is incomplete, and the "simple" route is unavailable)

This is the load-bearing atom, and it is where the report is thinnest. It
writes:

> "Since `alpha` is the nonzero characteristic root whose normalized
> multiplicity is the final-chain entry `gamma=7` …"

Two unproved steps hide there: (a) that the third entry of
`final=(11,4,7)` *is* `gamma`, and (b) that `gamma = 7` for this family. Both
are true. Here is the derivation, which the report does not give.

**Step 1 — `b_1 = gamma` (GGV5 line 644).** For `b' <= gamma <= gamma_max`,

```text
A_(gamma) = (a_1/l_1, b_1),   l_1 = lcm(l,rho),   b_1 = gamma,
a_1 = a*l_1/l + (gamma-b) * (-sigma*l_1/rho).
```

Unflipped: `A = (8,28)`, `A' = (1,0)`, `(rho,sigma) = (4,-1)`, `l = 1`, so
`l_1 = lcm(1,4) = 4` and `a_1 = 8*4 + (gamma-28)*(1*4/4) = gamma + 4`.
At `gamma = 7`: `A_(7) = (11/4, 7)`. **That is exactly
`lib/families.py`'s `final=(11,4,7)`.** So the third entry *is* `gamma`, and
`gamma = 7`. Cross-check in the flipped frame (`A=(28,8)`, `A'=(0,1)`,
`(rho,sigma)=(-1,4)`, `l_1 = 1`): `a_1 = 28 + 4(gamma-8) = 24` at
`gamma=7`, i.e. `A_(7) = (24,7)` — **exactly GGV22 line 1132's
"reducing the edge `{(28,8),(0,1)}` to `{(28,8),(24,7)}`"**. Two independent
frames, same `gamma = 7`.

**Step 2 — `gamma_max = 7` (GGV5 lines 624, 633).**
`gap(rho,l) = rho/gcd(rho,l) = 4`;
`gamma_max = min((b-b')/gap, b-1) = min(28/4, 27) = 7`;
cross-check `min(gcd(a-a', b-b'), b-1) = min(gcd(7,28), 27) = 7`.
So `gamma = gamma_max = 7`. I recomputed both forms with
`lib/families.py`'s own helpers: `gap = 4`, `gamma_max = 7`,
`gcd(7,28) = 7`.

**Step 3 — the edge is NOT simple. (This is the finding.)**
`lib/families.py:is_simple` implements GGV5 Definition 2.5
(`v_01(enF) - 1 == gap` and (`gap > 1` or `v_01(A') > 0`)) and returns
**`False`** for this edge. GGV5's Remark `simple` (line 635) gives no relief:
it only excludes simplicity when `gamma_max < (b-b')/gap`, and here they are
equal (`7 = 7`). Consequently:

- GGV5 Prop. `multiplicidad`(3)'s **equality** clause is unavailable;
- `SECTION4-AUTOMATION.md:208-225`'s rule B1 — "the major root's
  multiplicity is fixed by `A_{h+1}`: `mult/m = v_01(A-A')/gap` **when the
  edge is simple**" — is unavailable;
- `Gamma = {b'+1, …, gamma_max} = {1,…,7}` a priori (the library takes
  `range(Ap.b+1, gmax+1)`), so `gamma = 7` is **not** forced by simplicity.

Anyone who "derives" the exponent 7 from the simple case has made an error.

**Step 4 — the replacement bridge (single root without simplicity).**
The generated corner of a complete chain pins `gamma` directly:

- GGV5 Rmk `bala` (743–765), items (4)–(5): for a type-II.b regular corner,
  `b' < gamma <= gamma_max` and `A_(gamma) = A_1`, where
  `gamma = m_lambda/m` for the `lambda in K^x` of Prop. `multiplicidad`(4).
  Type II.b holds here: `l = 1` gives type II (Prop. `multiplicidad`(1)),
  and `v_{1,-1}(A') = 1 - 0 = 1 > 0` gives II.b (GGV5 line 754).
- The chain record fixes `A_1 = (11/4,7)`, so by Step 1 `gamma = 7`, hence
  `m_lambda = m*gamma = 3*7 = 21`.
- GGV5 line 553: `t := deg pbar = m * v_01(A-A')/gap = 3*28/4 = **21**`,
  where `p(z) = pbar(z^gap)` (GGV2 Rmk 3.9, quoted at GGV5 line 551).
- In characteristic zero with `p(0) != 0`, writing
  `pbar(w) = prod_i (w-c_i)^{mu_i}` with all `c_i != 0` gives
  `p(z) = prod_i prod_{zeta^gap = c_i} (z-zeta)^{mu_i}`; so the multiplicity
  of a root `lambda` of `p` equals `mu_{lambda^gap}`, and
  `m_lambda <= deg pbar` (GGV2 Rmk 3.8, quoted at GGV5 line 557).
- Here `m_lambda = 21 = deg pbar`, i.e. **`pbar` has a single root of full
  multiplicity**: `pbar(w) = c (w - alpha)^{21}` with `alpha = lambda^{gap} != 0`.

With `gap = 4` and `z^4 = (x^{1/4}y)^4 = x y^4` in the unflipped frame,

```text
l_{4,-1}(P) = lambda_P * x^3 * (x y^4 - alpha)^21
            = lambda_P * [ x (x y^4 - alpha)^7 ]^3 ,
```

and correspondingly `l_{4,-1}(Q) = lambda_Q [x(xy^4-alpha)^7]^2`. This is the
report's `F_0 = a K_rho^2`, `G_0 = b K_rho^3` with `rho = alpha`.
**The family pin is licensed.**

Three properties of this bridge that make it better than the report's:

1. It **does not need GGV6 Proposition 2.5** (used at GGV22 lines 1019–1020,
   and *not on arXiv* per `SECTION4-AUTOMATION.md`), nor the a)/b)/c) case
   split. The report's route runs through GGV22 line 1132's "in all the three
   cases", which inherits both.
2. It **does not need the "simple" hypothesis**, which is false here.
3. Only *one* side needs the argument: `Dtil_0 = 0` (§5) then forces the
   *same* `K` on the other side.

**REPAIR:** replace the report's one-sentence justification of `gamma = 7`
with Steps 1–4, and serialize them as the `FACEPIN` derivation object that
§4.1 input 4 already demands.

### 3.5 Imported hypotheses, and whether `G2-PSC` is needed

Load-bearing for the pin as stated:

- **H1** A counterexample lands in `(A_0,m,n) = ((8,28),(3,2))` with raw
  polygons `3S`/`2S` — GGV22 lines 1009–1010 + §2 dichotomy, itself resting
  on GGV5's enumeration under the bound `maxdeg <= 150`.
- **H2** The complete chain of that family is `(8,28) -> (11/4,7)` and is
  unique. Verified in the frozen library: from `A_0=(8,28)` with
  `maxdeg <= 150` there are exactly two complete chains,
  `(8,28)->(7/4,3)` with `(m,n)=(3,4)`, `maxdeg 144`, and
  `(8,28)->(11/4,7)` with `(m,n)=(3,2)`, `maxdeg 108`. For `(3,2)` the chain
  is unique. Conditional on GGV5 Thm 2.20 / Algorithm 8 under that bound.
- **H3** `(A_0,(4,-1))` is a regular corner of type II.b of the `(3,2)`-pair
  (GGV5 Prop. `multiplicidad`(1),(4); GGV1 Defs 5.5, Props 5.16/5.18/5.19).
- **H4** GGV5 Rmk `bala`, line 644, line 553; GGV2 Rmks 3.8/3.9 (quoted
  verbatim inside GGV5, so visible in custody, but *originating* in a paper
  I did not fetch).
- **H5** Characteristic zero, `K` algebraically closed.
- **H6** `[P,Q] in K^x`, normalized to `1` by scaling `f`.
- **H7** Newton polygons **exactly** `3S`, `2S` (all four vertices attained,
  with `(0,0)` a hull anchor).

**`G2-PSC` is NOT needed.** `ladder/REDUCTION.md:1179-1196` defines
`G2-PSC` as the GGV-packet/corner → decorated-Sigray-pole-tree transport and
fidelity obligation, owed only by a *hybrid GGV-to-Sigray* architecture
before it may use GGV polygon restrictions as sheet/book input. `LF40` never
leaves the GGV lane: it takes the raw `2S/3S` support plus `J = const` and
emits a determinant ideal in the same coordinates. `G2-BD` (bounded
delay/carrier after residue-A) is likewise unrelated. The report lists both
correctly on the *output* side ("neither outcome proves … `G2-PSC`,
`G2-BD`") but never states the *input*-side conclusion. **REPAIR:** state
"`LF40` owes neither `G2-PSC` nor `G2-BD`" explicitly, so that a later reader
does not import the hybrid-packet obligation by association.

---

## 4. Raw exponents, weights, windows, census — PASS (independent recount)

I enumerated the lattice points of `2S = conv{(0,0),(2,0),(16,56),(0,8)}`
and `3S = conv{(0,0),(3,0),(24,84),(0,12)}` by brute force and regraded with
`nu_F = 8-4i+j`, `nu_G = 12-4i+j`.

Derivation of the weights (not taken from the report): the chart
`x = tau^{-4} xi`, `y = tau` sends `x^i y^j -> xi^i tau^{j-4i}`, and the
prefactors `tau^8`, `tau^12` give `nu_F = 8-4i+j`, `nu_G = 12-4i+j`.

```text
# 2S = 141      # 3S = 301      total 442                      MATCH
nu_F range 0..16,  nu_F = 0 : 15 slots (i = 2..16)              MATCH
nu_G range 0..24,  nu_G = 0 : 22 slots (i = 3..24)              MATCH
no negative weights on either side                              (new)
positive-weight slots: 126 + 279 = 405                          MATCH
```

Window formulae, re-derived from the four supporting lines of each polygon
(`j >= 0`, `j >= 4i-8` resp. `4i-12`, `j <= 8+3i` resp. `12+3i`, `i >= 0`):

```text
F_nu : max(0, ceil((8-nu)/4))  <= i <= 16-nu,   j = nu-8+4i
G_nu : max(0, ceil((12-nu)/4)) <= i <= 24-nu,   j = nu-12+4i
```

Machine check of **set equality** (not just cardinality) against the actual
lattice, for every `nu`: **exact for F rows 0..16 and G rows 0..24**.
`F_17` empty by formula and by enumeration. `G_17..G_24 = 8,7,6,5,4,3,2,1`.
All **MATCH**.

**Complete per-row census (the report gives only rows 17+; supplied here so
the compiler can assert it):**

```text
F_nu, nu=0..16 : 15 14 13 12 12 11 10 9 9 8 7 6 5 4 3 2 1      (sum 141)
G_nu, nu=0..24 : 22 21 20 19 19 18 17 16 16 15 14 13 13 12 11
                 10 9 8 7 6 5 4 3 2 1                          (sum 301)
```

Note the non-monotone steps (`12,12` and `9,9` in F; `19,19`, `16,16`,
`13,13` in G) — a compiler that assumes a strictly decreasing row profile
will silently mis-slot. Worth an assertion.

**D3 cross-check.** `RAW_INPUT.json`'s `raw_slots_through_weight_22.F` and
`.G` are **exactly** the 141 and 301 lattice points (set equality verified),
with slot names `f_i_j` / `g_i_j` consistent with `raw_exponents`. Its
`weight` field equals the **upper** value `8+3i-j` (resp. `12+3i-j`) for
every slot — the report's warning is correct and necessary. Sharpened trap:
`8+3i-j = 8-4i+j` iff `7i = 2j`, which holds for **9 F-slots**
(`i = 0,2,…,16`, e.g. `f_16_56`, `f_8_28`) and **13 G-slots**
(`i = 0,2,…,24`). A spot-check that happens to land on those slots passes
while the grading is wrong. **REPAIR:** the compiler's regrade assertion must
be over *all* slots, and should additionally assert `nu >= 0` everywhere
(this also fail-closes mutation control 8, see §10).

---

## 5. `Dtil_0` UFD classification and endpoints — PASS

`Dtil_0 = 12 F_0' G_0 - 8 F_0 G_0' = 0`. Divide by `4`:
`3 F_0' G_0 = 2 F_0 G_0'`, i.e. `(F_0^3/G_0^2)' = 0` as rational functions.
**In characteristic zero** this forces `F_0^3 = c G_0^2`, `c in K^x`. In
`K[xi]`, a UFD, comparing `ord_pi` for each irreducible `pi` gives
`3 ord_pi(F_0) = 2 ord_pi(G_0)`, so `ord_pi(F_0) = 2 e_pi`,
`ord_pi(G_0) = 3 e_pi`, hence

```text
F_0 = a K^2,   G_0 = b K^3,   K = prod pi^{e_pi},   a^3 = c b^2.
```

Endpoint consequences (verified symbolically):

- `deg F_0 = 16` **iff** `f_{16,56} != 0` (i.e. `a != 0`) ⇒ `deg K = 8`;
  independently `deg G_0 = 24` **iff** `g_{24,84} != 0` ⇒ `deg K = 8`.
- `ord_xi F_0 = 2` **iff** `f_{2,0} != 0` ⇒ `ord_xi K = 1`;
  independently `ord_xi G_0 = 3` ⇒ `ord_xi K = 1`.

So `K = xi h(xi)`, `deg h = 7`, `h(0) != 0` — **exactly the report's
statement**, and exactly what the saturation `a*b*rho` buys. The residual
freedom after `Dtil_0` alone is the root structure of `h`; the GGV theorem
of §3.4 collapses it to a single root. Machine confirmations:

```text
deg_xi K = 8, ord_xi K = 1 ; deg F_0 = 16, ord 2 ; deg G_0 = 24, ord 3
Dtil_0 after FACEPIN : IDENTICALLY ZERO
b^2 F_0^3 - a^3 G_0^2 == 0 : True
```

**Flag:** characteristic zero is load-bearing twice over (the log-derivative
step, and `3F_0'G_0 = 2F_0G_0'` degenerating in char 2 or 3). The report does
state it — §3 opens "Work over an algebraically closed characteristic-zero
field", and §4.7 asks specifically for a "characteristic-zero unit-ideal
certificate" — so the hypothesis is pinned where the verdict is drawn. What
§4 does **not** do is name a base coefficient ring for the objects it emits,
which is what would let §4.7 tell what it was handed. See §10-R2.

---

## 6. `FACEPIN` relations — PASS

`F_0 = a K^2 = a xi^2 (xi-rho)^14` has `xi`-support exactly `i = 2..16`
(**15** relations); `G_0 = b K^3 = b xi^3 (xi-rho)^21` has support exactly
`i = 3..24` (**22** relations). Total **37**. Both supports coincide with the
raw `nu = 0` windows — no orphan and no missing slot. Verified symbolically.

Closed forms (verified for every index):

```text
f_{i, 4i-8}  = a * C(14, i-2) * (-rho)^(16-i),   i = 2..16
g_{i, 4i-12} = b * C(21, i-3) * (-rho)^(24-i),   i = 3..24
```

so in particular `f_{2,0} = a rho^14`, `f_{16,56} = a`,
`g_{3,0} = -b rho^21`, `g_{24,84} = b`. The report's indexing is correct.

**Remaining variables (substituted compute form):**
`442 - 37 + 3 = 405 + {a,b,rho} = 408`. Matches. This is *one* of two
representations: the **relational custody form** keeps all 442 raw slots,
adds `a,b,rho` for **445** variables, and carries the 37 relations as
equations rather than as a substitution. The two must never be quoted with
each other's counts; see the representation table in §8.

**Is any relation among `a,b,rho` missing?** No. `Dtil_0` vanishes
identically after substitution (verified), and it is the only row that
involves `F_0,G_0` alone; every row `n >= 1` also involves free slots, so no
further constraint on `(a,b,rho)` is forced by the raw system. The
`(m,n)`-pair relation `b^2 F_0^3 = a^3 G_0^2` is automatic.

**Normalization.** The report forbids `rho = a = b = 1` without a typed
ledger. I checked whether the normalization is even *available*: under
`x -> lam x`, `y -> mu y`, `f -> c f`, `g -> c' g` with `c c' lam mu = 1`
(to preserve `J = 1`), one gets `u := lam mu^4`, `rho -> rho/u`,
`a -> c a lam^2 u^14`, `b -> c' b lam^3 u^21`. Solving for `(1,1,1)` reduces
to `lam^17 = u^{-139} a^{-4} b^{-4}` with `u = rho` — solvable over an
algebraically closed field. So the normalization **is** legitimate and would
remove 3 variables, but it acts on all 405 remaining slots and needs the
transport ledger the report demands. The report's conservatism is correct,
not merely cautious; I record the normalization as an available optimization,
not a defect.

---

## 7. Saturation — PASS on soundness, REPAIR on wording

Claimed saturator: `a * b * rho * f_0_8 * g_0_12`.

**Soundness (each factor must be nonzero on every family member):**

| Factor | Equivalent to | Attained because |
|---|---|---|
| `a` | `f_{16,56} != 0` | `(16,56) = 2*(8,28)` is a vertex of `2S` |
| `b` | `g_{24,84} != 0` | `(24,84) = 3*(8,28)` is a vertex of `3S` |
| `rho` | `f_{2,0} = a rho^14 != 0` and `g_{3,0} = -b rho^21 != 0` | `(2,0)`, `(3,0)` are the images of the vertex `(1,0)` of `S` |
| `f_0_8` | `(0,8) = 2*(0,4)` attained | `(0,4)` is a vertex of `S` (GGV22 line 1010; `lib/families.py` `c = 4`) |
| `g_0_12` | `(0,12) = 3*(0,4)` attained | same |

These are **exactly** the four vertices of each polygon other than the
origin. Both `f_0_8` (`nu_F = 16`) and `g_0_12` (`nu_G = 24`) survive
`FACEPIN` as free slots, so the saturator is well defined after substitution.
**No over-saturation, no under-saturation of the vertex conditions.**

**Origin coefficients — correctly excluded.** `(0,0)` is a vertex of `2S`
and `3S`, but in GGV's convention `N(P) = conv(Supp(P) ∪ {(0,0)})`, and
`P -> P - P(0,0)` preserves `[P,Q]` and `N(P)`. So `f_{0,0}` and `g_{0,0}`
may legitimately be zero. Saturating them would be **unsound**. The report
gets this right ("`(0,0)` is a hull anchor and need not be saturated") and
correctly quarantines a strict-origin variant as a separate control.

**Exact hull attainment vs. harmless overapproximation.** The compiler treats
all 442 lattice points as free slots, so `Supp(f) ⊆ 2S` is an
overapproximation of any particular member — harmless, since the slots may be
zero. Exactness of `N(f) = 2S` is then recovered by the three vertex
saturations plus the origin anchor. The two together are **equivalent** to
`N(f) = 2S`, `N(g) = 3S`. Correct.

**Semantics.** The exclusion direction is sound: a family member yields a
point of `V(I)` off `V(a b rho f_0_8 g_0_12)`; so
`I : (a b rho f_0_8 g_0_12)^inf = (1)` ⇒ no family member. The converse is
*not* claimed, and the report is explicit that a survivor is not a chain
point. Correct.

**REPAIR (soundness-relevant wording).** The report says

> "**At minimum** saturate by `a*b*rho*f_0_8*g_0_12`."

That invites adding factors. Saturating by anything *not* proved nonzero on
every family member **enlarges** the ideal and can manufacture a false unit
ideal, i.e. a false exclusion. Rewrite as: "Saturate by **exactly**
`a*b*rho*f_0_8*g_0_12`. Any additional factor requires a written proof that
it is nonzero on every member of the raw family; adding one without such a
proof is unsound."

---

## 8. Lower chart, identity, recurrence, target, map, ceiling — PASS

Everything in this section was derived before reading the NU17 review's
formulas.

**Chart.** `xi = x y^4`, `tau = y`, inverse `x = tau^{-4} xi`, `y = tau`.
With `f = tau^{-8} F`, `g = tau^{-12} G`:

```text
f_x = tau^{-4} F_xi
f_y = tau^{-9} (4 xi F_xi + tau F_tau - 8 F)
g_x = tau^{-8} G_xi
g_y = tau^{-13}(4 xi G_xi + tau G_tau - 12 G)
```

so the `4 xi F_xi G_xi` cross-terms cancel and

```text
J_{x,y}(f,g) = tau^{-17} [ -12 F_xi G + 8 F G_xi + tau(F_xi G_tau - F_tau G_xi) ]
```

i.e. **`12 F_xi G - 8 F G_xi - tau(F_xi G_tau - F_tau G_xi) = -tau^17 J_{x,y}(f,g)`**.
Verified symbolically on a nontrivial test pair with exact rational
arithmetic: **True**. (Consistency with the NU17 review's
`J_{xi,tau} = tau^{-21}[…]`: `det ∂(x,y)/∂(xi,tau) = tau^{-4}`, so
`J_{xi,tau} = tau^{-4} J_{x,y}` — the two agree.)

**Recurrence.** Expanding `F = sum_r F_r tau^r`, `G = sum_s G_s tau^s`, the
`tau^n` coefficient of the left side is

```text
Dtil_n = sum_{r+s=n} [ (12-s) F_r'(xi) G_s(xi) + (r-8) F_r(xi) G_s'(xi) ]
```

— **exactly the report's formula.** Verified term-by-term against the direct
`tau`-expansion for rows `0..40`: **True**.

**Target row and sign.** `J = 1` gives right side `-tau^17`, so
`Dtil_17 = -1`, `Dtil_n = 0` otherwise. The sign is tied to the
`J(f,g) = 1` orientation, as the report says. The exponent `17` is not
arbitrary: for a Jacobian monomial from `(i_1,j_1) in 2S` and
`(i_2,j_2) in 3S`, `17 - 4p + q = nu_F(i_1,j_1) + nu_G(i_2,j_2) = r+s`, so
the grading is consistent and never negative.

**Direct-coordinate map.** `c x^p y^q -> -c xi^p tau^(17-4p+q)`: verified to
reproduce the left side exactly on the test pair and on both controls.
**PASS.** The report is right that this is a *same-source* consistency check
(same slot data, same `J`), not independent evidence.

**Row ceiling and exact generator census — REVISED (this corrects the first
issue of this review).** `max nu_F = 16`, `max nu_G = 24`, so `n <= 40`.

The first issue computed the per-row `xi`-window and generator count
*combinatorially from the windows* and reported **780** generic generators.
**That count is wrong.** Window arithmetic asks only which `xi`-degrees are
*reachable*; it does not ask whether any reachable pair actually contributes.
Re-derived from raw exponent pairs, six reachable positions turn out to be
structurally zero.

**Generation rule (re-derived directly, not from the windows).** For an
`f`-slot `(i,j)` and a `g`-slot `(k,l)`, the Jacobian `J(f,g) = f_x g_y -
f_y g_x` receives from that single pair exactly

```text
(i*l - j*k) * f_i_j * g_k_l * x^(i+k-1) y^(j+l-1) ,
```

which the direct-coordinate map `c x^p y^q -> -c xi^p tau^(17-4p+q)` places in
row `n = nu_F(i,j) + nu_G(k,l)` at `xi`-degree `p = i+k-1` with coefficient
`-(i*l - j*k)`. I checked this against the `tau`-recurrence for **all
`141 * 301 = 42441` pairs**:

```text
(12-s)*i + (r-8)*k  ==  -(i*l - j*k)   for every pair,  r = nu_F, s = nu_G
```

(identically: `(12-s)i+(r-8)k = (4k-l)i + (j-4i)k = jk - il`). So the two
engines agree **pairwise**, not merely row-wise. Two consequences:

- a pair with `i*l = j*k` — i.e. with **proportional exponent vectors**,
  `(i,j)` and `(k,l)` on a common ray through the origin — contributes
  **nothing**;
- distinct pairs carry distinct monomials `f_i_j g_k_l`, so no cancellation
  between pairs is possible.

Hence, exactly: **position `(n,p)` carries a generator iff at least one
contributing pair is non-proportional.** This is a structural statement, not a
genericity statement.

**Exact raw census, all 41 rows, re-enumerated over the 42441 pairs:**

```text
row  0 : xi-deg  5..38  34     row 21 : xi-deg  0..18  19
row  1 : xi-deg  4..38  35     row 22 : xi-deg  0..17  18
row  2 : xi-deg  4..37  34     row 23 : xi-deg  0..16  17
row  3 : xi-deg  4..36  33     row 24 : xi-deg  0..15  16
row  4 : xi-deg  4..35  32     row 25 : xi-deg  0..14  15
row  5 : xi-deg  3..34  32     row 26 : xi-deg  0..13  14
row  6 : xi-deg  3..33  31     row 27 : xi-deg  0..12  13
row  7 : xi-deg  3..32  30     row 28 : xi-deg  0..11  12
row  8 : xi-deg  3..31  29     row 29 : xi-deg  0..10  11
row  9 : xi-deg  2..30  29     row 30 : xi-deg  0..9   10
row 10 : xi-deg  2..29  28     row 31 : xi-deg  0..8    9
row 11 : xi-deg  2..28  27     row 32 : xi-deg  0..7    8
row 12 : xi-deg  2..27  26     row 33 : xi-deg  0..6    7
row 13 : xi-deg  1..26  26     row 34 : xi-deg  0..5    6
row 14 : xi-deg  1..25  25     row 35 : xi-deg  0..4    5
row 15 : xi-deg  1..24  24     row 36 : xi-deg  0..3    4
row 16 : xi-deg  1..23  23     row 37 : xi-deg  0..2    3
row 17 : xi-deg  0..22  23     row 38 : xi-deg  0..1    2
row 18 : xi-deg  0..21  22     row 39 : xi-deg  0..0    1
row 19 : xi-deg  0..20  21     row 40 : (empty)         0
row 20 : xi-deg  0..19  20
TOTAL raw nonzero coefficient generators, rows 0..40 = 774
deg_xi(Dtil_n) <= 39 - n for every n : True
  — attained for every n >= 1; STRICT at n = 0 (raw row 0 tops out at xi^38)
```

**The six overcounted positions**, each with every contributing pair
proportional (so a structural zero, not a generic one):

```text
(row  0, xi^4 ) : f_2_0   * g_3_0                              il-jk = 0
(row  0, xi^39) : f_16_56 * g_24_84   [= 2*(8,28) and 3*(8,28)] il-jk = 0
(row  4, xi^3 ) : f_1_0 * g_3_0 , f_2_0 * g_2_0                all 0
(row  8, xi^2 ) : f_0_0 * g_3_0 , f_1_0 * g_2_0 , f_2_0 * g_1_0 all 0
(row 12, xi^1 ) : f_0_0 * g_2_0 , f_1_0 * g_1_0 , f_2_0 * g_0_0 all 0
(row 16, xi^0 ) : f_0_0 * g_1_0 , f_1_0 * g_0_0                all 0
```

They are the two endpoints of row 0 — the two bottom vertices, and the two top
vertices `2*(8,28)`, `3*(8,28)`, proportional by construction — plus the low
endpoint of each of rows 4, 8, 12, 16, where every contributing pair lies on
the bottom edge `j = l = 0`. **Reconciliation: `780 - 6 = 774`.** (For
completeness: 801 positions are reachable if one also admits the 21 phantom
`p = -1` slots of rows 20..40, which arise only from `i = k = 0` and which the
window form correctly never emitted; `801 - 21 = 780` is exactly the first
issue's figure.)

**After `FACEPIN` substitution — checked symbolically over `Z[a,b,rho,…]`,
not by random evaluation.** Substituting `F_0 = a xi^2 (xi-rho)^14`,
`G_0 = b xi^3 (xi-rho)^21` (i.e. `f_{i,4i-8} -> a C(14,i-2)(-rho)^(16-i)`,
`g_{k,4k-12} -> b C(21,k-3)(-rho)^(24-k)`) and accumulating each position as a
`Z[rho]`-combination of the monomials `a*g_k_l`, `b*f_i_j`, `f_i_j g_k_l`:

- **all 34 raw row-0 coefficient polynomials cancel identically.** Row 0 is
  the only row in which both sides are substituted, so all pairs with
  `i + k = p + 1` collapse onto the single monomial `a*b`, and the row-0
  coefficient of `xi^p` is
  `-a b (-rho)^(39-p) * sum_{i+k=p+1} (8k - 12i) C(14,i-2) C(21,k-3)`,
  whose inner sum I verified to be `0` for every `p` — the coefficient-level
  form of `Dtil_0 = 0` of §5;
- **no position in rows 1..39 vanishes.** In those rows at most one side is
  substituted, each surviving monomial occurs exactly once, and the exact
  computation returns `raw_row(n) == substituted_row(n)` for every
  `1 <= n <= 40`.

```text
raw nonzero generators                 774
post-FACEPIN nonzero generators        740   (= 774 - 34, row 0 emptied)
positions that vanish under FACEPIN    exactly the 34 of raw row 0
```

**Representation table — quote these together, never mixed:**

| Representation | Variables | Listed equations |
|---|---|---|
| Raw pre-`FACEPIN` determinant list | (442 raw slots) | **774** determinant generators |
| **Relational custody form** | 442 raw slots + `a,b,rho` = **445** | 37 `FACEPIN` relations + 774 determinant generators = **811** |
| **Substituted compute form** | 405 positive slots + `a,b,rho` = **408** | **740** determinant generators |

Saturation is *not* included above. If it is represented by **Rabinowitsch**
(one auxiliary `w` with `w*a*b*rho*f_0_8*g_0_12 - 1 = 0`), add one variable and
one equation: **446 vars / 812 equations** relational, **409 vars / 741
equations** substituted. If the saturation is represented **directly as an
ideal colon**, add **no** auxiliary variable and **no** equation — the counts
stay 445/811 and 408/740. (`f_0_8` has `nu_F = 16` and `g_0_12` has
`nu_G = 24`, so both are free positive-weight slots in either form and the
saturator is well defined in both.)

**`Dtil_40` / `Dtil_39`.** `Dtil_40` has **zero** generators: its only pair is
`(r,s) = (16,24)`, i.e. `F_16 = f_{0,8}` and `G_24 = g_{0,12}`, both constant
in `xi`, so both derivative terms vanish — equivalently `i = k = 0` gives
`i*l - j*k = 0`. It is a structural zero, exactly as the report says, and
**must still be serialized as the row-ceiling control while contributing 0 to
every generator count above.** `Dtil_39` has exactly one generator; its closed
form is

```text
Dtil_39 = -12 F_15' G_24 + 8 F_16 G_23'   (pairs (15,24) and (16,23))
```

and it is realized nonzero by the native control (§9). **The report's
"`Dtil_39` is the last potentially nonzero row" is CONFIRMED.**

The target row is unaffected: row 17 keeps its full window `0..22` (23
generators), and its `xi^0` generator — the one carrying the `+1` of
`Dtil_17 + 1` — is genuinely nonzero, receiving `f_0_1 * g_1_0` with
`il - jk = -1` and `f_1_0 * g_0_1` with `il - jk = +1` (its other two
reachable pairs, `f_0_0 * g_1_1` and `f_1_1 * g_0_0`, are proportional and
drop). So no row-17 position collapses to the constant generator `1`, which
would hand the compiler a free — and spurious — unit ideal.

**Off-by-one / orientation attacks — all survived:**

- Upper window limits `16-nu`, `24-nu`: re-derived from the upper edges
  `j = 8+3i`, `j = 12+3i`; set-equality verified for every row.
- `F_17` empty because `16-17 < 0`; verified against the lattice.
- Lower window `max(0, ceil((8-nu)/4))`: `ceil`, not `floor`; verified.
- **Orientation swap of the `(8,12)` shift pair.** If `f in 3S` is fed as
  `F` (shift 12) and `g in 2S` as `G` (shift 8) while the coefficients
  `(12-s)`, `(r-8)` are kept, rows differ from correct starting at row 0.
  The correctly re-derived formula is `(8-s) F_r' G_s + (r-12) F_r G_s'`,
  which I verified reproduces the direct map of `J(g,f)`. So the `(8,12)`
  pair is **typed by polygon and not interchangeable**. The report's
  §4.6 control 8 ("swap `(f,g)` without changing the target sign") only tests
  the sign. In practice the swap is caught by §4.2's set-equality assertion
  (regrading `3S` by `nu_F` produces negative weights, e.g. `(3,0) -> -4`),
  but only if that assertion is applied per side and an explicit `nu >= 0`
  guard exists. See §10.

---

## 9. The two negative controls — PASS

Recomputed from the literal sparse polynomials, exact rationals, both
engines (recurrence and direct-coordinate), all `41` rows:

**Native fibre-tagged control, `lambda = 1`:**
```text
F rows present : 0, 4, 16          G rows present : 0, 6, 23, 24
nonzero Dtil rows : 4, 6, 10, 16, 22, 23, 24, 27, 28, 39
FIRST nonzero row : 4                          <-- MATCHES the report
Dtil_17 = 0  (target -1 : absent)              <-- MATCHES
Dtil_40 = 0 (structural) ; Dtil_39 = -8 (NONZERO)
recurrence == direct-coordinate engine : True
```
Row 4 is nonzero because `-x` sits at `nu_F(1,0) = 4`; by hand
`Dtil_4 = -12 G_0 + 4 xi G_0' = 84 xi^4 (xi-1)^20 != 0`, matching the
machine.

**D3/R0 artificial completion:**
```text
F rows present : 0, 8, 16          G rows present : 0, 8, 16, 24
nonzero Dtil rows : 8, 16, 24
FIRST nonzero row : 8                          <-- MATCHES the report
Dtil_17 = 0  (target -1 : absent)              <-- MATCHES
Dtil_39 = Dtil_40 = 0
recurrence == direct-coordinate engine : True
```

Both **CONFIRMED**. Neither has the row-17 Keller target, so neither can be
mistaken for a family point; both agree on `F_0, G_0`, so both remain valid
face-pin checksums. The report's characterization is accurate.

**Additional finding the report should record:** only the **native** control
exercises rows above 24 (nonzero at 27, 28, 39). The artificial completion's
nonzero rows stop at 24, so it alone would *not* detect a compiler that
truncates at row 24. Control 3 in §4.6 is therefore carried by the native
control only — worth saying, since the artificial one is the "custody"
fixture and the tempting one to keep.

**`lambda = 1` is the fibre parameter, not the chart variable — CONFIRMED
constructively.** `lambda` is the coefficient of `x y^15` in `g`
(`nu_G(1,15) = 23`; `(1,15)` lies on the upper edge `j = 12+3i` of `3S`).
Re-running with `lambda = 0` changes exactly rows **23, 27, 39**. Closed
form: `G_23 = lambda*xi`, `F_16 = f_{0,8} = -1`, `F_15 = 0`, so

```text
Dtil_39 = 8 * F_16 * G_23' = -8*lambda ,
```

which is `-8` at `lambda = 1` and `0` at `lambda = 0` — exactly the machine
output. The chart variables are `xi` and `tau`; `lambda` is neither.
(Notation hazard worth flagging: GGV5 uses `lambda` for the *characteristic
root* — the report's `rho` / GGV22's `alpha` — and GGV5 uses `(rho,sigma)`
for the *direction*, colliding with the report's `rho` for the root. Three
different `lambda`s and two different `rho`s are in play across the sources;
the contract should rename or at least tabulate them.)

---

## 10. The `GGV-8_28-LF40-v1` contract — CORRECT / REPAIR

I rebuilt the contract's checkable content (windows, census, 37 relations,
row recurrence, both engines, both controls) end to end. The specification is
implementable as written and its arithmetic is right. Gaps, in descending
severity:

**R1 (soundness).** `§4.3` "**At minimum** saturate by …" — see §7. Must
become "exactly", with the nonvanishing-proof obligation for any addition.

**R2 (soundness) — REVISED.** The first issue of this review said "no
field / characteristic pin anywhere in §4". **That is factually wrong and is
withdrawn.** The report *does* pin characteristic zero, twice and in the right
places: §3 opens "Work over an algebraically closed characteristic-zero field
after the usual base extension", and §4.7's own verdict bullet reads
"A **characteristic-zero** unit-ideal certificate for `I_LF40` excludes the raw
pre-final `8_28` GGV family…". The mathematical hypothesis that §5 shows to be
load-bearing is present and correctly attached to the verdict.

The surviving defect is narrower, and it is a *compiler-contract* defect rather
than a mathematical one: **§4 never freezes a concrete base coefficient ring
and serialization for the emitted ideal.** §4.4 asks for "the combined sparse
polynomial over the coefficient ring" without ever naming that ring, and §4.1's
input pins do not fix one. A conforming implementation may therefore build
every object of §4.2–§4.6 over `GF(p)` and satisfy each clause literally, then
hand its output to §4.7 — which asks for characteristic zero but has no
contract-level way to tell what it received.

The warning from the first issue survives intact and is the reason this
matters: **a modular unit ideal is not a characteristic-zero certificate.**
`I = (p x - 1)` reduces to the unit ideal mod `p` while `I_Q != (1)`, so a
mod-`p` run cannot discharge §4.7 no matter how clean it is.

**Repair:** name the ring in §4.2/§4.4, per representation and matching §8 —
`QQ[a, b, rho, 405 slots]` in the substituted compute form,
`QQ[a, b, rho, 442 slots]` in the relational custody form (plus the
Rabinowitsch variable if that route is taken) — and add: "mod-`p` runs are
heuristics only; the promotable certificate is over `QQ`."
(Conversely, a certificate over `Q` *does* exclude points over every
characteristic-zero field, since all generators have integer coefficients —
worth stating, it is the reason `K = Kbar` is not needed for the exclusion.)

**R3 (control strength).** `§4.6` control 5 — "change the exponent `7` in
`K_rho` to `6`" — is **degenerate**. `K = xi(xi-rho)^6` has degree 7, so
`deg F_0 = 14 != 16` and the mutation is killed by a pure degree/saturation
check that carries **no GGV content**. The mutation that actually tests the
family theorem is

```text
K' = xi (xi-rho)^6 (xi-rho2),   rho != rho2, both nonzero.
```

I verified: `deg K' = 8`, `ord_xi K' = 1`, `deg F_0 = 16`, `ord F_0 = 2`,
`deg G_0 = 24`, `ord G_0 = 3`, `f_{2,0} = a rho^12 rho2^2 != 0`,
`f_{16,56} = a != 0`, and **`Dtil_0 = 0` identically**. So `K'` passes every
lattice check, every endpoint saturation, and the whole `Dtil_0` UFD
classification. It is excluded *only* by the single-root theorem of §3.4.
**Replace control 5 by the two-distinct-root mutation** (and keep the
exponent-6 one as a cheap smoke test).

**R4 (fail-closed inputs).** §4.1 requires `RAW_INPUT.json`, `lib/families.py`,
the two arXiv digests, and a serialized `FACEPIN` derivation. Missing:
`tests/test_families.py` and `lib/FAMILIES.md` (cited in §1.2 but not pinned
as inputs — the `8_28` `GATE_B` row is what actually certifies
`final=(11,4,7)`, `steps=((4,-1,3,4),)`, `S`, `mn`, `degs`), and
`jc72108/SECTION4-AUTOMATION.md` (pinned in §1.2, not required in §4.1).

**R5 (missing checks).** Add, all cheap:
- assert `nu >= 0` for every regraded slot (fail-closes the polygon/shift
  swap of §8);
- assert the **full per-row census** of §4, not just rows 17+ (the profile is
  non-monotone: `12,12` and `9,9` in F; `19,19`, `16,16`, `13,13` in G);
- assert `deg_xi(Dtil_n) <= 39-n` — attained for every `n >= 1`, **strict at
  `n = 0`**, where the raw row tops out at `xi^38` — together with the exact
  §8 counts: **774** raw generators, **740** after `FACEPIN`, raw row 0
  exactly **34** and post-`FACEPIN` row 0 exactly **0**, row 39 exactly **1**,
  row 40 exactly **0**;
- assert the exact per-row `xi`-windows of §8 and **not** the naive reachable
  windows: six positions (both endpoints of row 0, and the low endpoint of
  each of rows 4, 8, 12, 16) are structural zeros because every contributing
  slot pair has proportional exponent vectors, `i*l = j*k`. A compiler that
  emits them will emit six `0 = 0` rows and inflate its own census to 780;
- assert the regrade over *all* 442 slots, not a sample — 9 F-slots and
  13 G-slots have upper weight `=` lower weight coincidentally (§4).

**R6 (target convention).** §4.4 pins `Dtil_17 = -1` but never records how
`J(f,g) = 1` is reached from `[P,Q] in K^x`: by scaling `f`, which preserves
`Supp(f) = 2S` and rescales only the saturated `a`. Also unrecorded: the flip
`phi_1` contributes `-1` on its own. Both are harmless; both must be in the
ledger or the sign becomes folklore.

**R7 (coefficient generators).** §4.4 asks for "every coefficient generator of
`Dtil_n + delta_{n,17}`" without pinning how many there should be. Use the §8
per-row table as the fail-closed expected count, and pin *which
representation* the count belongs to: **774** generators in the raw
pre-`FACEPIN` list, **740** in the substituted compute form. `Dtil_40` is
still emitted, as the row-ceiling control, and still contributes **0**. A
count of 780 is the window-arithmetic overcount and must fail the gate.

**R8 (dual-engine honesty).** §4.5 already says the direct-coordinate engine
is "a same-source consistency check, not an independent-model review."
**Correct and worth preserving verbatim.** Both engines read the same 442
slot symbols and the same `J`; they differ only in expansion order. Genuine
independence would require a different *model* re-deriving the chart identity
— which is what this review supplies (§8), not what §4.5 supplies.

---

## 11. Verdict semantics — CORRECT / REPAIR (sharpen, do not weaken)

**Maximum theorem promotable now (before any solve):**

> *Let `K` have characteristic zero. Let `f, g in K[x,y]` with
> `N(f) = 2S`, `N(g) = 3S` for `S = conv{(0,0),(1,0),(8,28),(0,4)}` and
> `J(f,g) = 1`. Then, in the chart `x = tau^{-4}xi`, `y = tau`,
> `F = tau^8 f`, `G = tau^12 g`, one has `F = sum_{r=0}^{16} F_r tau^r`,
> `G = sum_{s=0}^{24} G_s tau^s`, and*
> ```
> sum_{r+s=n} [ (12-s)F_r'G_s + (r-8)F_rG_s' ] = -delta_{n,17},  0 <= n <= 40.
> ```
> *Moreover `F_0 = aK^2`, `G_0 = bK^3` with `deg K = 8`, `ord_xi K = 1`,
> `a b != 0`. If in addition `(f,g)` arises as the raw pair of the GGV
> `8_28` complete-chain family, then `K = xi(xi-rho)^7` with `rho != 0`.*

The first two sentences are **unconditional**. The last sentence is
conditional on H1–H7 of §3.5.

**What a characteristic-zero unit-ideal certificate for `I_LF40` would and
would not exclude. Being strict:**

- **YES:** the bounded GGV raw pre-final `8_28` family — a pair with
  polygons exactly `3S`/`2S`, constant Jacobian, and the pinned lower face.
  This is the honest object.
- **NO, not directly:** GGV22 Proposition 4.3's *final* systems
  (`open_8_28_c1/c2`, `[P,Q] = x^2`, post-`psi_4` coordinates) as standalone
  objects. Raw exclusion removes their *source*, hence removes any
  counterexample that would produce them; it does not prove those printed
  systems have no solutions in their own right.
- **The `(72,108)` degree pair:** GGV22 lines 258–260 and its table
  (314–317) list exactly two `maxdeg = 108` cases: `(9,27)(2,3)` and
  `(8,28)*(3,2)`, and both give the pair `(72,108)`. `9_27` is already
  discarded (GGV22 line 267; `cases/emit.py` carries it as `reg_9_27` in the
  solved regression suite). So — **and this is the sharpest correct
  statement, which the report does not make** — a unit ideal for `I_LF40`
  would discard the *last* `(72,108)` case and, by GGV22's own line 252,
  **raise the lower bound from 108 to 125**, exactly the improvement GGV22
  names as the open goal. That is a real, nameable result. It is not
  "all degree `(72,108)` possibilities" in any looser sense, and it is
  achieved only through GGV22's dichotomy, not by `LF40` alone.
- **NO:** arbitrary hypothetical counterexamples. GGV22 §2's theorem
  (lines 287–288) is a **lower**-bound dichotomy; nothing here bounds degree
  from above. `ladder/REDUCTION.md` records "An exhaustive finite GGV polygon
  catalog for all counterexamples: **NOT ESTABLISHED**."
- **NO:** JC2. **NO:** `G2-PSC`, `G2-BD`, GGV landing for arbitrary
  counterexamples, or a cofinal degree bound.

**Conditionality ledger.** The `8_28` exclusion would rest on: GGV1 (Thm 2.6,
Prop 2.11(3), Cor 7.4, Def 5.5, Props 5.16/5.18/5.19, Prop 8.2); GGV2
(Prop 3.12, Rmks 3.8/3.9); GGV5 (Prop `multiplicidad`, Rmks `comentarios`
and `bala`, Defs of `Gamma`/`A_(gamma)`, Thm 2.20 + §6/§7 tables **under the
`maxdeg <= 150` bound**); **GGV6 Prop 2.5 — not on arXiv, not in custody**;
GGV22 §2 + Prop 4.3; Horruitiner. Plus: characteristic zero, the
normalization/transcription ledger (§3.1–3.2 errata), and the exactness of
`N(f) = 2S`, `N(g) = 3S`. `ladder/REDUCTION.md`'s standing verdict applies
verbatim: "The GGV2/GGV5/GGV6/GGV22 bounded residual lane: **CONDITIONAL** on
the exact imported statements/version perimeter."

Note that the §3.4 bridge **removes GGV6 Prop 2.5 and the a)/b)/c) split from
the pin's dependency set** (they remain in H1's dependency set via GGV22 §2,
but not in the FACEPIN's). That is a genuine reduction of the conditionality
surface and should be recorded.

**On the report's own verdict text.** Its §4.7 bullets are close to right,
but "A characteristic-zero unit-ideal certificate for `I_LF40` excludes the
raw pre-final `8_28` GGV family, conditional on the cited GGV reduction and
the orientation bridge" understates the *positive* consequence (the
108 → 125 improvement) and does not name the `9_27` sibling. Sharpen, do not
weaken.

---

## 12. Smallest additive repairs, and the single best next job

**Repairs, each additive, none requiring a rewrite:**

| # | Defect | Smallest repair |
|---|---|---|
| 1 | "At minimum saturate by" (§7) | "Exactly"; require a nonvanishing proof for any added factor |
| 2 | §4 names no base coefficient ring/serialization — though §3 *and* §4.7 do pin char 0 (§5, §10-R2) | Name the ring: `QQ[a,b,rho,405 slots]` substituted / `QQ[a,b,rho,442 slots]` relational; mod-`p` heuristic only |
| 3 | Control 5 degenerate (§10-R3) | Replace with `K' = xi(xi-rho)^6(xi-rho2)`, `rho != rho2 != 0` |
| 4 | `gamma = 7` asserted, not derived (§3.4) | Insert Steps 1–4; note the edge is **not simple** |
| 5 | Source P/Q swap unrecorded (§3.1) | Erratum line; pin orientation by polygon, never by letter |
| 6 | GGV22 line 1132 prints `{(28,8),(1,0)}` (§3.2) | Erratum line: read `(0,1)` |
| 7 | Missing input pins / checks (§10-R4, R5, R7) | Add `tests/test_families.py`, `lib/FAMILIES.md`, `SECTION4-AUTOMATION.md`; add `nu >= 0`, full slot census, `deg_xi <= 39-n`, the exact §8 row windows, and the 774 raw / 740 substituted / 34 raw-row-0 / 1 row-39 / 0 row-40 generator counts |
| 8 | `J = 1` normalization + flip sign unrecorded (§10-R6) | Two lines in the ledger |
| 9 | Versionless arXiv URLs (§1.2) | Print the `v1` suffix |
| 10 | `G2-PSC` input-side silence (§3.5) | One line: `LF40` owes neither `G2-PSC` nor `G2-BD` |

**Is the family pin licensed?** **Yes** — with repair 4. The report's
conclusion stands; its derivation does not. The narrowest source-to-FACEPIN
bridge is precisely §3.4: it lives entirely inside the two fetched e-prints
plus the frozen chain record, needs no GGV6 and no case split, and survives
the fact that the edge is not simple.

**Single best next job.** The report's §6 desk-scale `FACEPIN` custody gate,
**with three amendments**, and it should be run before any Gröbner work:

1. Reconstruct the `8_28` record from `get_pllc`, `get_starting_edges`,
   `get_complete_chains`, `get_mn_families` — **not** from a copied tuple —
   and assert `A_0=(8,28)`, `A_0'=(1,0)`, `(rho,sigma)=(4,-1)`, `q=4`,
   `(m,n)=(3,2)`, `S`, `degs=(108,72)`, `rhs_exp=2`, and **uniqueness of the
   complete chain for `(m,n)=(3,2)`** (I verified: exactly two chains from
   `A_0=(8,28)` under `maxdeg <= 150`, only one with `(3,2)`).
2. **New:** assert `gap = 4`, `gamma_max = min(gcd(7,28),27) = 7`,
   `is_simple(edge) = False`, and recompute `A_(gamma)` from GGV5 line 644 to
   land on `(11/4,7)` *and*, in the flipped frame, on `(24,7)` matching
   GGV22 line 1132. Then serialize the §3.4 chain
   `gamma = b_1 = 7 ⇒ m_lambda = 21 = deg pbar ⇒ pbar = c(w-alpha)^21`.
   This is the step that turns the external sentence into a typed object,
   and it is the step the report skips.
3. Serialize the flip `y(x^4y-rho)^7 -> x(xy^4-rho)^7`, expand square and
   cube, and compare all 37 coefficients against the closed forms of §6;
   then run the mutations of §10-R3 plus `rho = 0` plus both controls
   replayed at rows `0..40` (expected first-nonzero 4 and 8, `Dtil_17 = 0`,
   `Dtil_39 = -8*lambda` for the native pair).

Everything in that gate is desk-scale — the entire verification underlying
this review, including the full 42441-pair census and the symbolic `FACEPIN`
substitution, ran in seconds in pure Python with exact arithmetic. Only the
saturated elimination of `I_LF40` is heavy and belongs on AWS, and it must be
launched against a *named* representation (§8):

```text
relational custody form : 445 variables (442 slots + a,b,rho),
                          811 listed equations (37 FACEPIN + 774 determinant)
substituted compute form: 408 variables (405 slots + a,b,rho),
                          740 determinant generators
Rabinowitsch saturation : +1 variable and +1 equation
                          => 446/812  or  409/741
colon saturation        : no auxiliary variable, no extra equation
                          => 445/811  or  408/740
Dtil_40                 : serialized as the row-ceiling control, counted as 0
```

"408 variables, 780 generators" — the figure the first issue of this review
printed here — mixes the substituted variable count with a window-arithmetic
generator count that belongs to no representation at all.

---

## 13. Execution disclosure

- Shell was available. All computations are exact over `Q`.
- **No CAS was available in this session** (`sympy` is not installed, and no
  local Gröbner engine was used). I therefore implemented sparse Laurent
  polynomial arithmetic over `Q` in pure Python (`/tmp/ggvrev/poly.py`) and
  used it for: the chart identity, the row recurrence, the
  direct-coordinate map, both controls at all 41 rows, the `FACEPIN`
  expansions of `aK^2`/`bK^3`, the two-root mutation, and the `Dtil_0`
  vanishing. No Gröbner basis, saturation, or elimination was attempted, and
  none is claimed.
- **The §8 census was recomputed from scratch for this revision**
  (`/tmp/ggvrev/census.py`, `/tmp/ggvrev/facepin.py`), by direct enumeration
  of all `141 * 301 = 42441` raw slot pairs under the Jacobian coefficient
  rule `(i*l - j*k) f_i_j g_k_l x^(i+k-1) y^(j+l-1)` — **not** by window
  arithmetic, which is what produced the withdrawn 780. The pairwise identity
  `(12-s)i + (r-8)k = -(i*l - j*k)` was verified on every one of those pairs,
  so the census is independent of which engine is trusted. The `FACEPIN`
  substitution was carried out **symbolically over `Z[a,b,rho]`** — each
  position accumulated as an exact integer `rho`-polynomial attached to each
  monomial `a*g_k_l`, `b*f_i_j`, `f_i_j g_k_l` — and **not** by evaluation at
  random `(a,b,rho)`; the row-0 cancellation was additionally confirmed in
  closed form (`sum_{i+k=p+1} (8k-12i) C(14,i-2) C(21,k-3) = 0` for every `p`)
  and by literal expansion of `12 F_0' G_0 - 8 F_0 G_0'` at three generic
  rational `(a,b,rho)`.
- `lib/families.py` was imported **read-only** to obtain `CornerData`,
  `is_simple`, and the chain enumeration. No repository file was written
  except this review. `jc2-lean` was never touched.
- **Not in custody, hence not independently verified:** GGV1
  (arXiv:1401.1784), GGV2 (arXiv:1605.09430), **GGV6** (*Pro Mathematica* 30,
  not on arXiv), and Horruitiner's thesis. Statements I use from GGV2
  (Rmks 3.8/3.9) appear quoted verbatim inside GGV5, which *is* in custody;
  GGV1's and GGV6's statements are taken on the citing papers' word and are
  listed in the conditionality ledger of §11.
- I did not treat agreement with the NU17 review as evidence. Where the two
  agree (chart identity, recurrence, windows, census) the derivations here
  were obtained independently and only afterwards compared.

## 14. Scope firewall for this review

This review verifies the report's arithmetic, repairs its licensing
derivation, and bounds its verdict. It does **not** implement or solve the
`LF40` compiler, promote either control, prove Proposition 4.3's
exhaustiveness, prove GGV landing, discharge `G2-PSC` or `G2-BD`, improve any
degree bound, or resolve JC2.
