# Opus 5 cross-pollination and adversarial synthesis — round `20260827T0635Z`

Author: Opus 5, equal-standing JC2 co-researcher
Date: 2026-08-27
Status: **CROSS-REVIEW AND MERGE. NO JC2 PROOF OR COUNTEREXAMPLE. NO
PROMOTION. NO AWS JOB LAUNCHED. NO CAMPAIGN ARTIFACT EDITED EXCEPT THIS
FILE.**

## 0. Custody and what I actually executed

All seven required SHA-256 values were recomputed locally and match the
prompt exactly:

```text
8e140384a0603a588c03dfd65a764b8be5ab26f3301838de09b5b2d1c39131be  ideation-20260827T0635Z-packet.md
05400316ac7ba488faf93822a6a8dac8b5fde0ab8be4e0fcce0132565e179764  ideation-20260827T0635Z-sol.md
d1f607000ba9992e2778066ce95364205df48db15e3d27fbe71f3933953615a5  ideation-20260827T0635Z-fable5.md
2c0fa61ede365a4c9ef6f4252704c1dc18825818a6c35e12b4c9de763a1f1761  ideation-20260827T0635Z-grok.md
0fbb452456a34b24b28b35a9fd0f99fc6ac86f81edab7a704369aeba0b7881da  ideation-20260827T0635Z-opus5.md
9c5bf1229cf45dd7ea4d5d3907fd6033c88c0d9768934d01ea79e658f3d65a17  ...k00-honest-source-discriminator-design-sol-20260827.md
a049794b885b0bd49d79228d47790aa5466a33c29e8ba4057509b939e4af922e  ...j2-a1-first-occurrence-symbol-spencer-design-sol-20260827.md
```

This round I did have a shell, and I used it for desk-scale exact
`Fraction` arithmetic only (seconds, far under 1 GiB): no CAS, no Groebner
engine, no network, no AWS, no `jc2-lean` contact of any kind.

**Primary positive control.** I re-parsed all 70 ordered-`a1` row files
from their producing cases, recomputed their SHA-256, and matched **70/70**
against V37's pinned `row_sha256` map. Setting `rho=0` in the general-`rho`
V23R1 grades 10--15 bytes reproduces V37's frozen census exactly: **51**
nonzero rows of 70, **65** variables, per-grade term counts
`0,1,9,28,75,187,424,867,1647,2929` for grades 10--19. Every numeric
assertion below was recomputed from those bytes, not quoted.

**One structural fact I verified first, because four of the six
adjudications depend on it.** With the pinned V23 weight table
(`rho=0`, `a1=5`, `k=4`, `ell{n}=n`, `cs{n}=rs{n}=2+n`,
`ac/az/ec/ez{n}=5+n`, `k10_{n}=4+n`, `k6_{n}=12+n`), **all 70 rows are
sigma-weight-homogeneous of weight exactly equal to their grade — zero
inhomogeneous monomials — and every one of the 65 row variables has weight
>= 1.** `ell1` is the *unique* weight-1 variable and `ell2` the unique
weight-2 variable.

---

## 1. Adjudication 1 — Fable5's typed-certificate shape floor

**Verdict: sound, with three scope corrections, and I extend it.**

I separate the three ingredients as instructed.

### (a) The `rho=0` specialization

`rho` has sigma-weight **0** (verified in the pinned parser), and all rows
are weight-homogeneous with `rho` present as a weight-0 coefficient
variable. Hence `rho -> 0` is a weight-preserving graded ring map. If a
registered typed certificate `a1^i k^j (1 + rho*W) = sum h_m F_m` exists
over general-`rho` rows through grade `g`, applying it gives
`a1^i k^j = sum (h_m|_{rho=0}) (F_m|_{rho=0})`, i.e. membership in the
`rho=0` row ideal *at the same weight* `5i+4j`.

This is the **safe** direction of the promoted correction `593f953b…`.
That correction forbids lifting `rho=0` *emptiness* to a certificate;
Fable5 instead uses `rho=0` *nonmembership* to exclude a certificate.
Contrapositive, not converse. I checked specifically for this error and it
is not present. This is the single best piece of reasoning hygiene in the
four blind reports.

Two conditions the argument silently needs, which should be written into
the ledger entry:

- **C1.** The certificate must literally have the registered
  `unit = 1 + rho*W` type. A general unit `u` would only give
  `a1^i k^j u|_{rho=0}` in the specialized ideal, and the argument breaks.
- **C2.** The general-`rho` grade-16..19 rows must specialize to the frozen
  V28/V30/V33/V35 bytes. I verified this myself for grades 10--15 (V23R1
  with `rho -> 0` reproduces V37's census); for grades 16--19 there is no
  general-`rho` export to check against, so this is inherited producer
  provenance, exactly the caveat Fable5 records for the receiver lane.

### (b) Fixed-weight completeness

Sound, and it is a two-line argument, not a solver output. For weight `w`,
the graded piece of the row ideal is spanned by `m*F` with `F` a row of
weight `d <= w` and `m` a monomial of weight `w-d`. Rows of weight `> w`
need a negative-weight multiplier, and there are no weight-0 non-constant
monomials because every one of the 65 row variables has weight `>= 1`.
Rows have weight = grade `>= 10`. So for `w <= 19` only the frozen rows
matter and the verdict is final at any depth. For `w = 20` a grade-20 row
can enter, so `a1^4` is *only through grade 19*. Fable5's statement of this
boundary is exactly right.

**Correction C3, and it matters:** completeness at fixed weight is a
property of the `rho=0` ring. With `rho` present, `rho` has weight 0, so
weight-`w` multipliers form an infinite-dimensional `Q`-space (finite only
as a `Q[rho]`-module). Any successor that tries to run the same
completeness argument in the general-`rho` ring is invalid. (This kills a
step of Grok's Card B — see §2.)

### (c) The ideal-multiplication implication

Sound, and Fable5 under-uses it. `J` is an ideal, so `a1^i k^j in J`
implies `a1^{i'} k^{j'} in J` for `i' >= i, j' >= j`. Contrapositive:
nonmembership of a monomial excludes every divisor of it. V37's four
targets `(1,3),(2,2),(3,1),(4,0)` are precisely the maximal elements of the
divisibility order among shapes with `i >= 1` and weight `<= 19`, plus
`(4,0)`. Combining with (a)+(b) I get the **complete** exclusion lattice,
which I computed rather than asserted:

```text
FOREVER (nonmember, weight <= 19, any depth, any rho-cofactor W):
  (1,0) w5   (1,1) w9   (1,2) w13  (1,3) w17
  (2,0) w10  (2,1) w14  (2,2) w18
  (3,0) w15  (3,1) w19
THROUGH GRADE 19 ONLY:
  (4,0) w20      [a1^4 — needs the grade-20 export to become final]
MINIMAL OPEN SHAPES:
  (4,0) w20,  (1,4) w21,  (2,3) w22,  (3,2) w23
```

So Fable5's headline — "the minimal conceivable typed certificate is `a1^4`
at weight 20, or a mixed shape of weight `>= 21`" — is correct, and the
exact minimal open frontier is the four shapes above. `(4,1)` and `(5,0)`
are *not* minimal: they are multiples of the still-open `(4,0)`, which is
why W20 must be finalized first.

Fable5 derives `(m,0)`, `m <= 3` from V34 point evaluation. That is valid
(I verified it, §1.1), but it is also redundant: those shapes are divisors
of `(1,3)` and `(3,1)`, so they already fall out of V37 + multiplication +
completeness. Two independent routes agreeing is genuine confirmation, not
waste.

### Three exclusions Fable5's floor does **not** cover, and one I can add

1. **The localizer is assumed to be a power of `k`.** Registered
   certificates in this campaign have used composite localizers
   (`T-cs`: `cs^447*k^164`; `T-rs`: `s in S` costing `V(s)`). A shape
   `a1^i * s` with `s` not a `k`-power is untouched by the floor. State
   the floor as "monomial-in-`k` localizer" or it will be over-quoted.
2. **Raw row ideal only.** Honest chart generators — Rees-kernel
   bilinears, saturation generators, the Rabinowitsch element `1-v*k` —
   are not in `J`. The floor excludes *raw-row* certificates, not honest
   chart certificates. Grok and Sol both flag this correctly.
3. **Pure `k^j` shapes (`i = 0`) were never tested by V37**, and they are
   a legitimate (stronger) certificate shape: `k^j in J` would close
   `D(k)` outright. **My `L43` closes this gap for free.** `L43` is a
   coordinate zero section of all 51 rows on which `k` is free, so
   `k^j != 0` while every row vanishes; hence `k^j` is not in the row
   ideal through grade 19, and for `4j <= 19` (i.e. `j <= 4`) that is
   final forever by (b). `k^5` and up are "through grade 19" only.

So the merged, complete shape floor is: **nine `a1`-shapes excluded
forever, four `k`-shapes excluded forever, `a1^4` open at weight 20 and
decidable by one grade-20 export, and three minimal mixed shapes open at
weights 21--23.**

### 1.1 Fable5's V34 hand cross-check — verified exactly

I evaluated all 70 rows at the frozen V35 representative
`a1=192, ell2=21/4, cs1=11, rs2=-35, aa0=-96, ee1=576, ec3=2400`, all
other coordinates zero:

- **exactly one nonzero row: `Tg19_7 = -7077888`** — Fable5's number, to
  the digit;
- `ell1` is the unique weight-1 variable and `ell1(P) = 0`, so a weight-20
  identity over rows through grade 19 evaluates at `P` to
  `(scalar)*ell1(P)*Tg19_7(P) = 0 != 192^4`. Sound;
- `ell2` is the unique weight-2 variable and `ell2(P) = 21/4 != 0`, so the
  argument genuinely dies at weight 21. Fable5's stated stopping point is
  exact;
- `k(P) = 0`, so the point says nothing about any `j >= 1` shape. Fable5
  says this explicitly. Correct and honest.

Non-material numeral note: Fable5 writes `48^m` and Grok writes
`rs2*aa0 = 210`, both quoting the **unscaled** `a1=48` curve, while the
frozen V35 `POINT` is the `lambda^5=4`-scaled representative. I verified
the two are consistent: at the frozen point `rs2*aa0 = (-35)(-96) = 3360 =
210 * lambda^10 = 210*16`, with `weight(rs2)+weight(aa0) = 4+6 = 10`. No
error in either report, but two live normalizations of "the V34 point" now
circulate and a successor will eventually mis-substitute one. Pin the
scaled tuple by hash in any card that uses it.

### 1.2 New, free, and decisive: a W20 preflight that may make the span unnecessary

The same evaluation yields an exact necessary condition nobody stated.
A weight-20 element of the ideal generated by rows through **grade 20**,
evaluated at `P`, equals `sum_i c_i * Tg20_i(P)` with `c_i` scalars,
because (i) all rows of grade `<= 18` vanish at `P`, (ii) the only
grade-19 survivor `Tg19_7` carries a weight-1 cofactor and `ell1(P)=0`,
and (iii) grade-20 rows carry weight-0 cofactors, which are constants.
Therefore

> **`a1^4 in I_20` implies some grade-20 row is nonzero at `P`.**

If the seven grade-20 rows all vanish at `P`, `a1^4` is a nonmember
**forever at weight 20** with a two-line certificate and *zero linear
algebra* — no W20 span, no AWS solve. This is the cheapest forever-labelled
fact still available in the lane, and it costs one substitution after the
export lands. Mandatory control: verify the grade-20 export introduces no
new weight-1 variable (grade-19 newcomers have weights 8--14, so this is
expected but must be checked, not assumed).

---

## 2. Adjudication 2 — Grok's use of the V37 five-term dual

**Verdict: the transcription is exact; one displayed rewrite is wrong and
is self-refuting; one outcome branch is an over-read; one dependency is
invalid. The salvage is clean.**

### 2.1 What is right

Grok's `phi19` matches the frozen V37 functional **coefficient for
coefficient** in both selector lanes (`q65521` and `q65519`):

```text
lambda(a1^3*k) = 1,  lambda(a1*aa0*ac3) = -5/72,  lambda(a1*aa0*cs2^2) = 5/144,
lambda(a1*aa0*k*rs2) = -1/3,  lambda(a1*aa1*cs2*rs2) = -5/36.
```

All five monomials have sigma-weight 19. Grok's reading of W17/W18 —
"one-coordinate duals of rank 0 (`component_nnz=0`): those isolated
monomials are invisible to `I_19`, not merely missing a low-degree
cofactor" — is exactly right, and my divisibility preflight gives the
mechanism: **no row monomial divides `a1*k^3` or `a1^2*k^2`** (0 divisors
each), while `a1^3*k` has 2 divisors (`a1^3` in `Tg15_3`, `a1^3*k` in
`Tg19_5`) and `a1^4` has 1 (`a1^3` in `Tg15_3`). Verified.

### 2.2 The error

Grok's Card B, discriminator (iii), displays:

```text
a1^3 k  =  (5/72) a1 aa0 ac3 - (5/144) a1 aa0 cs2^2
         + (1/3) a1 aa0 k rs2 + (5/36) a1 aa1 cs2 rs2
         + (element of I_19).
```

This asserts that `phi19`, read as a *polynomial*, lies in `I_19`. It does
not, and the certificate refutes it in one line: `lambda` annihilates
`I_19`, so if `phi19 in I_19` then `lambda(phi19) = 0`. But

```text
lambda(phi19) = 1^2 + (5/72)^2 + (5/144)^2 + (1/3)^2 + (5/36)^2
              = 7855/6912 != 0.
```

So `phi19 is not in I_19`, and the rewrite is false. The underlying mistake
is the category error the prompt names: a **dual** vector separating a
target from an ideal has been read as a **primal** normal form. The
functional's support is the set of monomials on which `lambda` is nonzero;
it carries no information about a representation of the target modulo the
ideal. `mark: wrong`.

### 2.3 The over-read

Grok's Card B outcome "Some chart/saturation generator has `phi19 != 0`: a
mixed delayed-`a0` identity becomes the predicted staged type; run the §4
linear ansatz with that right-hand side, exceptional power read from the
leading `a1`/`aa0` factor" inherits the same error. A nonzero evaluation
yields no identity, no right-hand side, and no exceptional power.

### 2.4 The invalid dependency

Card B (ii) proposes evaluating `phi19` on "general-`rho` V23R1 rows
linearized in `rho` at the same weight". Because `rho` has weight 0, the
weight-19 graded piece over general-`rho` rows is not a finite-dimensional
`Q`-space, so the fixed-weight completeness that makes the whole dual
argument final is unavailable there (correction C3 of §1). "Linearizing in
`rho`" is a truncation with no completeness statement. `mark: unsupported`
as designed; it needs restating as a `Q[rho]`-module computation with its
own completeness argument, or dropping.

### 2.5 The strongest correct dual-transport statement (salvage)

Let `V_w` be the `Q`-space of weight-`w` polynomials in the 65 row
variables, `U_w` the span of all products `m*F` (`F` a frozen row of weight
`d <= w`, `m` a monomial of weight `w-d`), and `lambda in V_w^*` V37's
certificate with `lambda|_{U_w} = 0`, `lambda(t) = 1`.

> **Dual transport (correct form).** Let `G_1..G_r` be new *weight-
> homogeneous* generators of an enlarged ideal `J'`, of weights
> `d_1..d_r <= w`. Set `U'_w = U_w + span{ m*G_s : wt(m) = w - d_s }`.
> - If `lambda(m*G_s) = 0` for **every** monomial `m` of the complementary
>   weight and **every** `s`, then `lambda|_{U'_w} = 0`, so `t` remains a
>   nonmember of `J'` at weight `w`, and (for `w <= 19`) forever.
> - If `lambda(m*G_s) != 0` for some `m, s`, then **all that follows is
>   that this particular functional is no longer a separator.** It does not
>   follow that `t in J'_w`, that a certificate of any shape exists, or
>   that the monomials in `lambda`'s support appear in one. The only legal
>   continuation is a fresh rank/membership solve on `U'_w`.

Two implementation conditions Grok's card omits: the new generators must be
weight-homogeneous (inhomogeneous generators must be split into graded
pieces first), and one must enumerate **all** complementary-weight monomial
multipliers, not merely evaluate `lambda` on the generators themselves.

With those repairs the transport is cheap, exact, sparse, and genuinely
useful — it is the correct way to ask "does the honest chart see what the
raw rows do not?" without rebuilding a span. That salvaged mechanism is
Grok's best contribution and I carry it into merged card M3.

---

## 3. Adjudication 3 — Re-audit of my own `L43` and support-incidence preflight

I recomputed everything from the bytes. The mathematics survives exactly;
**the strategic use I made of it does not, and I withdraw a disposition
change.**

### 3.1 What is exactly true (verified this session)

- The 51 nonzero rows contain **4,997** distinct monomial supports, of
  which exactly **88** are minimal under inclusion: **11 singletons, 54
  pairs, 23 triples**. Singletons:
  `{a1} {aa0} {aa1} {e0} {e1} {ec3} {ec4} {ee0} {ee1} {ez3} {ez4}`.
- Coordinate zero sections are exactly the independent sets. Exact branch
  and bound gives **minimum hitting set 22** over 65 vertices, so the
  **maximum** coordinate zero section has dimension **43**.
- My published `F` (22 variables, `k` *not* among them) is a valid hitting
  set: all 51 rows vanish identically on `V(F)`, **no** variable of `F` is
  redundant, and the 43 free coordinates are exactly the published list.
  So `L43` is both **maximum** (43 is the global maximum) and **maximal**
  (irredundant). My blind report's wording — "maximum ... exactly 43" plus
  "maximal, not merely large" — is correct on both counts.
- `L43` survives with `rho` completely free on grades 10--15: zero
  surviving terms on `L43 x A^1_rho`.
- `{a1}` is a minimal support (`a1^3` occurs in `Tg15_3` with coefficient
  `-1/16`), so **no coordinate zero section has `a1 != 0`**, and every
  coordinate support containing `a1` dies by grade 15. This independently
  **rederives the recorded grade-15 death of `A10`** — precisely the
  control Fable5's Card 1 demands — from the support hypergraph alone.
- Divisibility preflight verified: `a1*k^3` and `a1^2*k^2` have **0** row
  monomials dividing them; `a1^3*k` has 2; `a1^4` has 1. V37's own
  manifests report `component_products: 0`, `rank: 0`, one-term functional
  for W17/W18 in both lanes. Half of a dual-host exact-`Q` AWS campaign
  answered a question that costs milliseconds.

### 3.2 What is bounded-through-grade-19, not all-depth

`L43` is proved for the frozen rows of grades 10--19 only. Nothing here
proves an all-depth statement; a grade-20 row could hit a currently free
coordinate. My blind Card B part (i) correctly identified the all-depth
version as an unproved emitter-structure claim, and it stays unproved.

### 3.3 Maximal versus maximum versus non-coordinate

The optimum is not unique — my branch and bound returned a *different*
size-22 optimum containing `k` (hence with `k = 0`). So the sentence in my
blind §3.1 describing `F` as "a front ... the low-index head of each source
family" describes **one** optimum, not a canonical object. More
importantly: `L43` ranges over **coordinate subspaces only**. Non-coordinate
linear sections, and nonlinear/parametrized sections of the V34
Kummer-quintet type, are entirely outside its reach. My blind self-audit
item 9 said this; I restate it here because it is the boundary that
determines what Fable5's Card 1 still has to do (§5).

### 3.4 Raw coordinate section versus honest receiver — **my scope error**

My blind report used `L43` as evidence about the **terminal receiver**
(bottleneck 2.1(2), Card B, §4.2). That transfer is not established:

- `L43` lives in the 65-variable **ordered-`a1` chart** coordinates, i.e.
  in the rows already specialized to `J1 = 0`, `a0 = 0`, `rho = 0`.
- `L43` is contained in `{a1 = 0}` (because `a1 in F`), so it lies *outside*
  the chart's own unit locus `D(a1)`. Evaluating chart rows there is
  formally legal but carries no chart-geometric meaning. This is exactly
  Grok's §7.2 "`Proj` versus `V(I)`" hazard, and I walked into it.
- The terminal receiver is `V(J1+J2)`, and the honest equations that
  decide it — Sol's `Phi_1..Phi_7` — live in a *different ring*,
  `A = Q[Lambda, C0..C6, k10, k6, k2, mu2, mu4, mu6, Jdet]`. My §4.2
  "evaluate the honest saturated Rees kernel at a generic `L43` point" is
  therefore **not well-typed** without the compiled jet -> `(C, Lambda,
  k10, ...)` map, which my card never names.

**Correction.** My bottleneck 2.1(2) headline — "the terminal receiver has
no algebraic closure route on this source" — is **wrong as phrased**. The
correct statement, now available from the post-snapshot evidence, is: *the
raw tail rows are silent on the receiver, but an honest source-typed
equation is not* (§6). My §4.2 falsification card is `unsupported` as
designed and is superseded by Sol's `H_K00` construction.

Likewise my blind sentence "`K00`, `Z00`, and `CS0` are three points of one
phenomenon" is `unsupported`: `CS0` and `Z00` are recorded as off-family
`k = 0` sections on other charts, and `L43` is an ordered-`a1` chart object.
I retract the unification claim. §6 supplies a *better* explanation of the
same observations that I did not have when writing blind.

### 3.5 The row-32 / secant interface — **withdrawn**

I raised avenue 32 on the argument that row 32's promoted saturation-free
collision presentation `I:Delta = I:Delta^infinity = I + (det A)` supplies
"the receiver's missing input type". Now that the missing object is
explicitly written down, that claim fails on type:

- the receiver needs a saturation of the **one-parameter `Phi` ideal at
  `Lambda` and `Jdet`** in `A`, not a saturation of a **collision ideal at
  the diagonal** in a Keller pair's polynomial ring;
- the saturating elements, the ambient rings, and the ideals are all
  different, and row 32's own recorded stuck point ("proving the
  three-generator ideal is `(1)` is still injectivity") means invoking it
  here would beg the question.

I labelled the bridge "candidate, `NOT YET TESTED`", but even the weaker
claim I made — that its *output type* matches the receiver's *input type* —
is not supported. **I withdraw the avenue-32 raise.** The avenue-38 raise
survives, with the caveat that the "tropical" filing is cosmetic: the
instrument is monomial-support/Newton-face combinatorics, and what matters
is that it becomes a launch gate, not which row it is filed under.

---

## 4. Adjudication 4 — Line-by-line re-audit of the ordered-`T-a1` cascade

I replayed every displayed residual against the frozen bytes. **Every
displayed identity is exactly correct, and the Case B kill is sound.** I
found no algebraic error and no hidden division. I found one sharpening and
one place where the report's presentation obscures a shorter argument.

### 4.1 The chain, with the exact/radical boundary marked

| # | Step | Verified residual | Divides by | Scope |
|--:|---|---|---|---|
| 1 | `Tg11_1 = (3/8)*a1*e0` | exact | `a1` | **exact ideal identity** in `A[1/a1]/I`: `e0 = 0` |
| 2 | `Tg12_2\|_{e0=0} = (3/32)*e1*(e1 - 4*a1*ell1)` | exact | — | zero-divisor split; **field-point** |
| 3 | `Tg13_4\|_{e0=0} = -(3/32)*e1^2*ell1`; on `e1=4a1*ell1` this is `-(3/2)*a1^2*ell1^3` | exact | `a1^2` | field-point; forces `ell1=0`, hence `e1=0` |
| 4 | `Tg12_1\|_{e0=e1=0} = (3/8)*a1*ee0` | exact | `a1` | exact once `e0,e1` are known zero |
| 5 | `Tg14_4\|_{e0=e1=ee0=0} = (3/32)*a1^2*ell1*rs1` | exact | `a1^2` | `ell1*rs1 = 0` |
| 6 | `Tg14_3 + (1/2)*ell1*Tg13_1 = (3/8)*a1^2*cs1*ell1 - (3/16)*a1*aa0*rs1` | exact | — | **exact combination**, machine-checked |

Step 2/3 is a valid disjunction elimination: at a field point either
`e1 = 0`, or `e1 != 0` forcing `e1 = 4*a1*ell1` and hence `ell1 != 0`,
which step 3 contradicts. So `e1 = 0` on `D(a1)` unconditionally. My blind
report's phrasing ("the branch collapses") is correct but terse; the clean
version is above.

**Case B (`ell1 != 0`) — every step verified:**

```text
Tg14_4        -> rs1 = 0                    (divide a1^2*ell1)
step 6        -> cs1 = 0                    (divide a1^2*ell1)
Tg13_2        -> ee1 = 0                    (divide a1*ell1)
Tg13_1        -> ec3 = 0                    (divide a1)
Tg15_4        -> rs2 = 0                    (divide a1^2*ell1)
Tg14_2        -> ez3 = 0                    (divide a1*ell1)
Tg14_1        -> ec4 = a1*cs2               (divide a1)
Tg15_3        -> a1^2*((3/8)*cs2*ell1 - (1/16)*a1) = 0, so a1 = 6*cs2*ell1
Tg16_5        -> (27/2)*cs2^3*ell1^4 = 0, so cs2 = 0, so a1 = 0.  CONTRADICTION
```

I confirmed `Tg15_3` vanishes identically at `(a1 = 6*cs2*ell1,
ec4 = a1*cs2)` and that `Tg16_5` there equals exactly `(27/2)*cs2^3*ell1^4`
(checked at `cs2 = 7/3`, `ell1 = 5/2`: both sides `214375/32`). **Every
division in Case B is by `a1` or `ell1`, both nonzero by hypothesis. There
is no hidden division.** Characteristic requirement for Case B is
`char != 2, 3` (denominators `8,16,32,64` and the factor 3); the `96/5`
relation in branch A2 additionally needs `char != 5`. My blind report's
blanket `char != 2,3,5` is a safe superset.

**A shorter kill exists and should replace the published one.** Before
using `Tg15_3`, substituting only `ec4 = a1*cs2` gives

```text
Tg16_5 = (3/32)*a1^2*ell1*(a1 - 2*cs2*ell1)   =>   a1 = 2*cs2*ell1,
```

which contradicts `Tg15_3`'s `a1 = 6*cs2*ell1` immediately (both need only
`a1, ell1 != 0`). Same conclusion, one fewer substitution, and it exhibits
the contradiction as a clash of two linear relations rather than a cubic
residual. Not an error in the published chain — a strictly better
presentation of it.

**Branch A2 verified.** With `ell1 = 0`: `Tg14_3 = -(3/16)*a1*aa0*rs1`
gives `aa0*rs1 = 0`; with `rs1` a unit, `aa0 = 0`;
`Tg13_2 = rs1*(-(3/32)*a1^2 + (5/1024)*k*rs1^2)` gives
`k*rs1^2 = (96/5)*a1^2`; and `Tg15_4 = (3/32)*a1*rs1*(a1*ell2 - ee1)`
gives `ee1 = a1*ell2`. All three of Theorem A's A2 relations replay
exactly.

### 4.2 Exact identity versus radical/field-point — the honest ledger

My blind report labelled Theorem A "radical/field-point scope". That label
is correct and necessary, but it under-sells step 1 and over-sells nothing:

- `e0 = 0` is an **exact ideal identity** after localizing at `a1`
  (agreeing with Sol's post-snapshot report, which states this
  independently). It is not a field-point deduction.
- `e1 = 0` is a genuine field-point deduction — **but I can now upgrade it
  to an exact nilpotency statement.** From `e1^2 ≡ 4*a1*e1*ell1` and
  `e1^2*ell1 ≡ 0` modulo the rows, `e1^3 ≡ 0`. I verified the explicit
  multiplier identity against the frozen bytes:

  ```text
  a1^2*e1^3 = (64/3)*a1^2*ee0*Tg11_1 - (128/3)*a1^3*Tg13_4
            + (32/3)*a1^2*e1*Tg12_2  - (32/3)*a1*aa0*e1*Tg11_1 ,
  residual exactly 0.
  ```

  So `e1^3 in I*A[1/a1]` **exactly**, with an explicit certificate. That
  converts the first radical rung of the cascade into an ideal-level fact
  with a named exponent, which is the form the staged calculus consumes.
- Everything downstream of `e1` (`ee0`, and the whole Case B chain) remains
  radical/field-point. **Theorem A must never be quoted as a certificate.**
  V37's `W19` nonmembership is fully *consistent* with Theorem A: `a1^3*k`
  need not lie in the raw ideal even if the variety has no point with
  `a1 != 0`. My blind self-audit item 2 said this; it stands.
- `rho = 0` is not the chart. Every grade-16+ export has `rho` killed at
  compile time, so the `Tg16_5` step that kills Case B is a special-fibre
  statement, and promoted correction `593f953b…` blocks lifting it to a
  certificate. My blind self-audit item 1 said this first and it remains
  the single largest limitation of the whole cascade.

### 4.3 One presentation defect worth recording

My blind report writes "On the second branch `Tg12_1` forces
`ee0 = -4*aa0*ell1`, and then `Tg13_4 = -(3/2)*a1^2*ell1^3`". The `Tg12_1`
step is **not used** by the `Tg13_4` step — with `e0 = 0`, `Tg13_4` does
not involve `ee0` at all. The sentence is true but reads as if the `ee0`
substitution is load-bearing. It is not. Harmless, but a reviewer
re-deriving the chain will waste time on it.

---

## 5. Adjudication 5 — Integrating the exact symbol result

**Verdict: sound. I verified essentially every checkable assertion in Sol's
symbol report, entry by entry. It is the highest-quality mathematics of the
round, and it interacts with three of the four blind reports.**

### 5.1 Independent verification

- **First-occurrence census:** reproduced grade by grade, all ten rows of
  the table, exactly.
- **Stationary incidence:** grades 14--17 have 8 newcomers used by rows
  `(7,5,2,0,0,0,0)`; grades 18--19 have 9 used by `(8,6,2,0,0,0,0)`.
  Exact match. **Zero** monomials contain two newcomers and **zero**
  newcomers appear nonlinearly, at every grade 14--19.
- **The stationary symbol matrix:** I extracted every entry at grades 14
  and 19 and it matches Sol's displayed matrix and all seven auxiliary
  polynomials `p, q1, s1, q2, s2, h1, h2` **exactly**, and is identical at
  the two grades.
- **Rank two on `D(a1)`:** row 3's only newcomer coefficients are
  `-(3/16)*a1*e0` and `(3/16)*e0`, both killed by the exact identity
  `e0 = 0`; row 1 pivots on `EC` with unit coefficient `(3/8)*a1`; row 2
  splits by the Bezout identity. Confirmed.
- **The Bezout identity** `Q*(X^2-X*Y+Y^2) - 125*k^3*S^2 = X^3 =
  -32768*A^6` is the sum-of-cubes factorization with `Q = X+Y`,
  `Y^3 = 125*k^3*S^2`. Correct by inspection. The short grade-18/19
  certificate `q - (5/8)*k*h = -(3/32)*A^2` also checks exactly.
- **Compatibility term counts** after `e0 = 0`, rows 3--7, grades 14--19:
  `[13,5,3,0,0] [37,15,17,2,3] [84,40,56,12,18] [168,85,141,42,67]
  [300,165,303,109,189] [498,287,587,235,445]`. Exact match, all thirty
  entries.
- **`Tg19_7` support facts:** 552 monomials, **28** supported in
  `S = {a1,ell2,cs1,rs2,aa0,ee1,ec3}`, and **zero** monomials whose
  outside-`S` name support has cardinality one. At the V34 point the only
  nonzero partial derivatives are the seven `S` directions, with
  `Tg19_7(P) = -7077888`. All confirmed.

### 5.2 Conflicts and confirmations

**Confirms my cascade, and the two are the same experiment.** My cascade
uses `Tg13_4, Tg14_4, Tg14_3, Tg15_3, Tg15_4, Tg16_5` — all rows 3--5, i.e.
exactly Sol's compatibility block — while its uses of rows 1 and 2 at
grades 14+ (`Tg14_1 -> ec4 = a1*cs2`, the `EC` pivot; `Tg14_2 -> ez3 = 0`,
the `EZ` pivot) are precisely the split-surjective newcomer solves Sol's
theorem guarantees. My blind Card A and Sol's blind Card B are **the same
experiment approached from two sides**, and the symbol theorem is the
systematic version. Merge them (card M1).

**Refutes a Grok outcome branch.** Grok's Card C live slice sets `a1 = 48`,
frees V32's six coordinates and the nine grade-19 newcomers, and zeroes
everything else — so `e0 = 0` and `a1 != 0`. Its outcome branch "`Tg19_7`
cuts a proper nonempty scheme, and `Tg19_1..3` then empty it after
adjoining newcomers" is **structurally impossible**: on `D(a1)` with
`e0 = 0`, rows 1 and 2 are split-surjective onto their newcomer columns, so
they can always be solved for the newcomers and can never obstruct; and
row 3's newcomer coefficients are both multiples of `e0 = 0`, so `Tg19_3`
does not see the newcomers at all. `mark: wrong` on that branch. Grok's
*negative control* for the same card (freeing the newcomers must leave
`Tg19_7` unchanged) is `sound` and is now not merely a control but a
theorem: `Tg19_7` contains no grade-19 newcomer.

**Sharpens V36 without contradicting it.** `Tg19_7` is not an accidental
jet-free row; it is the fifth component of a rank-five compatibility block
that no grade-19 newcomer can touch. V36's kill of the six-coordinate
component stands unchanged; what changes is that its mechanism is
structural and shared by rows 3--7.

**Correctly bounds itself.** Sol's §5 quantifier is narrow and right: the
one-outside-name observation holds *with the coordinate restriction fixed*,
and does not license adding a coordinate, re-solving grades 11--18, and
retaining the V34 basis relations. Any enlarged-support claim needs a new
exact solve. Sol's §7.3 also flags that the proposed W19 question is
**unsaturated** — a negative dual at `N = 0` does not rule out
`a1^N*Tg19_7` entering. Both firewalls are correct and must be carried.

**No conflict with the shape floor.** The symbol result is about
prolongation of the row system; the shape floor is about monomial
membership. They are independent and consistent.

---

## 6. Adjudication 6 — Integrating the K00 correction

**Verdict: sound. I verified the algebraic core by hand, including the
counterexample that makes the correction necessary.**

### 6.1 Verified by hand

- With `p = -2*rho^2`, the K00 octic coefficient tuple
  `(C6,C4,C2,C0) = (-4rho^2, 6rho^4, -4rho^6, rho^8)`, odd coefficients
  zero, gives `F = z^8 - 4rho^2 z^6 + 6rho^4 z^4 - 4rho^6 z^2 + rho^8 =
  (z^2-rho^2)^4 = q^4`. Hence `F^{3/2} = q^6` and `F^{5/4} = q^5` are
  polynomials. That is the structural reason all 569 tail monomials cancel
  — it is not a coincidence of the compilation.
- `M_K00` is exactly this condition with the root eliminated:
  `8C4 = 3C6^2`, `16C2 = C6^3`, `256C0 = C6^4` with `C6 = 2p` reproduce
  `C4 = 3p^2/2`, `C2 = p^3/2`, `C0 = p^4/16`. Checked.
- The restriction-first unit certificates are exact:
  `-4*Jdet^18*Phi7 = -4*Jdet^18*(-Lambda^19*Jdet/4) = (Lambda*Jdet)^19`,
  and with `Lambda = sigma^2`, `-4*Jdet^37*Phi7 = (sigma*Jdet)^38`.
- The negative control `I = (x - Lambda*m)` is exactly right:
  closure-first gives boundary `(x, Lambda)` with `m` still a unit
  (nonempty); restriction-first gives `(x, Lambda*m):(Lambda*m)^infinity =
  (1)` (empty). Saturation and restriction genuinely do not commute.

### 6.2 The false claim, and why it is false

`J1 = J2 = 0` at K00 does **not** make the geometric blowup fibre empty. The
standard blowup of `(x,y)` in `A^2` has chart `Q[x,y_2]` and fibre `A^1`
over the origin — nonempty — while imposing `x = y = 0` first inside the
bilinear ideal and then saturating gives the unit ideal. That is precisely
the pattern here, and it is why (6.1) and (6.2) in Sol's report are not
equal. I will not repeat the claim, and Grok's independent §7.2 warning
("Card A may be evaluating a base-point of `V(J1+J2)` rather than a point of
`Proj(Rees(J1+J2))`") is the same correction reached from the other side.
`mark: sound` for both.

### 6.3 Audit of the proposed closure-first incidence

```text
K      = (Phi1..Phi7) : Lambda^infinity : Jdet^infinity
B_K00  = K + (Lambda) + M_K00
H_K00  = B_K00 : (C6*k10*Jdet)^infinity
```

- **Order is correct and load-bearing.** Saturate to the closure of the
  strict interior `D(Lambda*Jdet)`, then take the boundary `Lambda = 0`,
  then impose the K00 core, then localize onto the generic moving ray.
  Reversing any of the first three reproduces the (5.6) unit and answers
  the wrong question.
- `K = I:(Lambda*Jdet)^infinity` — the two saturations commute, so the
  split form is cosmetic.
- The final localization at `C6*k10*Jdet` correctly excludes the
  coefficient-irrelevant origin (`C6` a unit), so no large irrelevant-ideal
  saturation is needed for this slice. Sol's §7.5 firewall — that the
  `C6 = 0` tip, `k10 = 0`, other load rays, other square-normal cones and
  the full collision receiver are untouched — is accurate and must be
  carried verbatim.
- The mandatory negative control (restriction-before-saturation must
  reproduce (5.6)) is exactly the right control, because it is the one
  computation an implementation is most likely to perform by accident.
- The optional deck control (adjoin `rho`, replace the even relations by
  `C6+4rho^2, C4-6rho^4, C2+4rho^6, C0-rho^8`, verify `rho -> -rho`
  invariance and contraction back to `M_K00`) is a genuine safeguard
  against smuggling a root orientation in as source data. Keep it.

### 6.4 The structural fact that reframes the whole raw-row debate

Sol's (5.3) gives `Phi_l = r_l(...) - Lambda^{12+l}*delta_l` with
`(delta_1..delta_7) = (0, mu2, 0, mu4, 0, mu6, Jdet/4)` and
`Lambda = sigma^2`. So the four inhomogeneous targets first enter at
sigma-grades **28, 32, 36, 38**, and the terminal one at **38**. Every raw
row export in this campaign stops at **grade 19**.

That single observation explains, without any appeal to a mysterious
"all-depth degeneracy", why `K00`, `Z00`, `CS0` and my `L43` all exist:
through grade 19 the exported system is *target-free*, and — as I verified
in §0 — every row is weight-homogeneous in variables of positive weight, so
the origin and large coordinate subspaces are automatic solutions at every
exported grade. Raw rows are silent on the receiver not because the
receiver is beyond algebra, but because **the discriminating data enters
nine to nineteen grades below where the exports stop**.

This supersedes and corrects three things at once: the packet's "all-depth"
framing (correct for the *tails*, but the tails are not the whole equation);
my own bottleneck 2.1(2) and my `CS0/Z00/K00` unification claim (§3.4); and
Grok's §4 falsification reading ("if honest equations vanish on
`K00 ∩ D(rho)`, this is the leading char-0 algebraization candidate") —
`Phi7` does **not** vanish there, so that branch is not currently live.
Grok's `rho`-split itself survives and is material: `K00_rho` (moving-`p`
exact square, zero normal, unit load) and `K00_0` (`p = 0`, all-zero higher
contact) are different geometric objects and the `C6 != 0` localization in
`H_K00` selects the former. **The `H_K00` computation as designed decides
`K00_rho` (generic `rho != 0`) only; `K00_0` needs its own registration.**
That is a real gap in the design, and it is Grok's contribution to spot it.

---

## 7. Claim matrix

Marks: `S` sound · `SC` sound with scope correction · `U` unsupported ·
`W` wrong.

### Sol (blind)

| # | Claim | Mark | Reason |
|--:|---|:--:|---|
| S1 | Raises 4, 16, 19, 21, 31, 38; no avenue reopened/stopped | S | Navigation; each raise has a named new client |
| S2 | Graded Spencer--Macaulay dual complex as the new mechanism | S | Delivered exactly by the post-snapshot symbol report; I verified it entry by entry (§5.1) |
| S3 | "V37 functionals, if they extend compatibly, witness a nonnilpotent localized quotient or an associated component" | SC | Macaulay-dual extension is a statement about the inverse system; a compatible chain can be a nonreduced distribution, not a field-valued point. Sol's own self-audit says this — carry it as a hard firewall, not a caveat |
| S4 | Card A: evaluate genuine Rees/routing equations at K00; block honestly if the presentation is missing | S | Realized as the post-snapshot design; the "deliverable is the exact missing map, not a surrogate standard basis" discipline is correct and rare |
| S5 | Card B: generic first-occurrence symbol/compatibility test | S | Realized and verified; identical in content to my blind Card A |
| S6 | Card C: compatible graded inverse-system ladder | SC | Sound design; must not run fixed-weight completeness in the general-`rho` ring (§1 C3) |
| S7 | Self-audit ("a Spencer obstruction on a component is not chart-wide") | S | Accurate and load-bearing |

### Sol (post-snapshot, symbol/Spencer)

| # | Claim | Mark | Reason |
|--:|---|:--:|---|
| P1 | First-occurrence census, grades 10--19 | S | Reproduced exactly |
| P2 | From grade 14, newcomers affine-linear, no two newcomers in one monomial; incidence `(7,5,2,0,0,0,0)` / `(8,6,2,0,0,0,0)` stationary | S | Reproduced exactly, all grades |
| P3 | The stationary symbol matrix and all seven auxiliary polynomials | S | Every entry verified at grades 14 and 19 |
| P4 | `e0 = 0` is an **ideal** identity in `R_g`, not merely radical | S | `Tg11_1 = (3/8)*a1*e0`; localizing at `a1` |
| P5 | Symbol rank exactly two on `D(a1)`; `coker = R_g*[e_3] ⊕ … ⊕ R_g*[e_7]` | S | Row 3 killed by `e0=0`; row 1 unit `EC` pivot; row 2 split by the verified Bezout/`k*h` identities |
| P6 | Rows 3--7 are the five-component compatibility block; no grade-19 newcomer can change any component | S | Verified: rows 4--7 use zero newcomers at every grade; row 3's newcomer coefficients are multiples of `e0` |
| P7 | Compatibility term-count table (30 entries) | S | Exact match |
| P8 | `Tg19_7`: 552 monomials, 28 in `S`, zero with a single outside name; all nonzero partials at `P` lie in `S` | S | Exact match |
| P9 | "This does not close ordered `T-a1`; it says where every repair must enter" | S | Correct narrow quantifier |
| P10 | Proposed W19 case (`Tg19_7` modulo the other 69 rows) is final for unsaturated weight-19 membership | S | Follows from homogeneity + completeness (§1b); Sol correctly flags it is **unsaturated** |

### Sol (post-snapshot, K00 discriminator)

| # | Claim | Mark | Reason |
|--:|---|:--:|---|
| K1 | K00 core gives `F = q^4`, so `F^{3/2}`, `F^{5/4}` polynomial and all tails cancel | S | Verified by hand |
| K2 | `Phi7\|K00 = -Lambda^19*Jdet/4`; unit certificates (5.6) | S | Arithmetic verified |
| K3 | Restriction-first K00 section is killed on `D(Lambda*Jdet)` | S | Direct from K2 |
| K4 | `J1=J2=0` does **not** make the geometric blowup fibre empty | S | Verified with the blowup-of-`(x,y)` model and the `(x-Lambda*m)` control |
| K5 | Closure-first incidence `K/B_K00/H_K00`, order load-bearing | S | Order is exactly right for the intended question |
| K6 | `M_K00` is the correct core ideal | S | Verified against `C6=2p` |
| K7 | Firewalls: one generic incidence for a fixed `[6,2]` client; `C6=0` tip, `k10=0`, other rays untouched | S | Accurate |
| K8 | Missing-object list (targets at grades 28/32/36/38; Taylor families uncompiled; general-`rho` emitter incomplete) | S | This is the round's most useful negative inventory (§6.4) |
| K9 | `H_K00` decides both K00 pieces | — | Not claimed by Sol, but a reader will assume it. The `C6 != 0` localization selects `K00_rho`; **`K00_0` needs separate registration** (Grok's split) |

### Fable 5

| # | Claim | Mark | Reason |
|--:|---|:--:|---|
| F1 | `rho=0` is a graded ring map carrying `a1^i k^j (1+rho W)` to a pure membership at the same weight | S | `rho` has weight 0; all rows weight-homogeneous. Safe direction of `593f953b…`. Conditions C1/C2 of §1 should be recorded |
| F2 | Fixed-weight completeness makes `w <= 19` verdicts final forever | S | Two-line argument; verified. Add correction C3: this is a `rho=0` fact |
| F3 | Shapes `(1,3),(2,2),(3,1)` impossible forever, any depth, any `W` | S | Direct V37 + F1 + F2 |
| F4 | Shapes `(m,0)`, `m <= 3` impossible forever via the V34 point | S | Verified; also independently derivable from V37 + ideal multiplication |
| F5 | Minimal conceivable typed certificate is `a1^4` at w20, or mixed w >= 21 | SC | Correct; exact minimal open frontier is `{(4,0) w20, (1,4) w21, (2,3) w22, (3,2) w23}`. Scope: monomial-in-`k` localizer, raw row ideal only, `i >= 1` only (pure `k^j` untested — closed by my `L43`, §1) |
| F6 | §3.2 V34 hand cross-check of W20; stops at w20 because `ell2 != 0`; `k=0` so says nothing about `j >= 1` | S | All three verified exactly, including `Tg19_7(P) = -7077888` |
| F7 | TRIVIAL-LOCUS: define and classify all-depth finite-support sections; all-depth vanishing is a finite exact condition | SC | Sound design. Decidability is conditional on the canonical-tail instantiation property, which Fable5 correctly makes mandatory and fail-closed. **Headline Q1/Q2 already answered NO at coordinate-support scope through grade 19** (§3.1): `{a1}` is a minimal support, so no coordinate section has `a1 != 0`, and this rederives the recorded grade-15 death of `A10`. Residual value is exactly the non-coordinate (Kummer-type) sections and the all-depth emitter statement |
| F8 | Section-first rule (evaluate targets against `T` before funding a sweep) | S | Correct and cheap; it is the same instrument as my §4.3 preflight |
| F9 | C1 graded lightcone ledger field ("question X is complete below weight w") | S | Cheap process fix that would have pre-flagged the W20 boundary |
| F10 | C2 power-absorption templates from the receiver cascade identities | U | Ordering heuristic only; Fable5 says so. No evidence the `ee1^3`/`ec3^3`/`aa0^4` shapes transfer to `T-a1` |
| F11 | C3 residence map (the first honest exclusion equation is a CE constraint) | SC | Directionally right, but the first honest equation is now known (`Phi7`) and it excludes a *restriction-first section*, not an arc. Recompute the hand-off from `H_K00`, not from `Phi7` |
| F12 | Avenue 31 raise; receiver moves to critical path | S | Correct, and reinforced by §6.4 |
| F13 | "K00 kills all deeper raw receiver exports forever" | SC | True for raw rows. §6.4 gives the real reason (targets enter at grades 28--38) and shows an honest equation *does* kill the literal section |
| F14 | HARDENED-LADDER (fail-closed every metadata field, relocatable paths, static pin of `shared_faber_probe` on import, dual selectors + exact-`Q` replay, mistyped-certificate and corrupted-metadata negative controls) | S | Best software specification in the round; adopt verbatim |
| F15 | Self-audit items 1--6 (sparse-only blindness; chart compatibility; instantiation risk; scheme-theoretic solving not optional; value claim capped; even total success is local) | S | Item 4 (V34's Kummer quintet proves rational-point search misses sections) is exactly the right lesson and is what my coordinate-only `L43` cannot see |

### Grok

| # | Claim | Mark | Reason |
|--:|---|:--:|---|
| G1 | `phi19` five-term transcription | S | Matches both frozen selector lanes coefficient for coefficient |
| G2 | W17/W18 rank-0 duals mean the monomials are "invisible to `I_19`", not missing a cofactor | S | Verified: zero row monomials divide either target |
| G3 | Card B (iii) rewrite `a1^3 k = (…) + (element of I_19)` | **W** | Self-refuting: `lambda(phi19) = 7855/6912 != 0` while `lambda` annihilates `I_19`. Dual read as primal |
| G4 | Card B outcome "generator with `phi19 != 0` ⇒ predicted staged type, exceptional power from the leading factor" | **W** | Same category error; a nonzero evaluation only invalidates the separator |
| G5 | Card B (ii): general-`rho` rows "linearized in `rho` at the same weight" | U | Fixed-weight completeness fails when a weight-0 variable is present (§1 C3) |
| G6 | Dual transport as a cheap sparse alternative to a new echelon | S | Correct and valuable **after** the semantic repair of §2.5 |
| G7 | Split K00 into `K00_rho` and `K00_0` before any solver | S | Materially right; the two are different geometric objects and `H_K00`'s `C6` localization only reaches the first |
| G8 | §7.2 `Proj` versus `V(I)` / base-point warning | S | Same correction as K4, reached independently; it is the error class the prompt warns about |
| G9 | §7.4 emit a met/unmet hypothesis bit per identity | S | Correct fail-closed design; promoted square theorems are scoped |
| G10 | §7.5 R1--R3 are radical/field-point and must not be imported as scheme generators of the honest Rees ideal | S | Correct, and it is the same discipline my Theorem A needs |
| G11 | §7.6 `k` vs `k10`; keep `1-v*k`; Z00 must fail it | S | Correct typing hygiene |
| G12 | §7.7 killing both named pieces does not close `V(J1+J2)` | S | Correct |
| G13 | Card C outcome "`Tg19_1..3` empty the slice after adjoining newcomers" | **W** | Refuted by P5/P6: on `D(a1)` with `e0=0`, rows 1--2 are split-surjective and row 3 does not see newcomers |
| G14 | Card C negative control (`Tg19_7` unchanged when newcomers are freed) | S | Now a theorem, not just a control |
| G15 | §4 falsification: simultaneous vanishing on `K00 ∩ D(rho)` would make it the leading char-0 algebraization candidate | SC | Superseded: `Phi7` does not vanish on the restriction-first section. The reading may revive for `H_K00 != (1)`, but only as "accessible algebraic boundary support", never as a germ |
| G16 | Avenue 2 raise (deck/square as the remaining discriminator) | S | Navigation; consistent with F12 |
| G17 | "K00 is on-family (`1-v*k = 0`); Z00 is the off-family origin" | — | Inherited from the receiver audit; I did not re-derive it. Not disputed |

### Opus 5 (my own blind report — audited at least as hostilely)

| # | Claim | Mark | Reason |
|--:|---|:--:|---|
| O1 | Theorem L: maximum coordinate zero section has dimension exactly 43 (min hitting set 22); `L43` with `k` free is maximum **and** maximal; survives with `rho` free on grades 10--15 | S | Recomputed from bytes: 4,997 supports, 88 minimal (11/54/23), 65 vertices, hitting set 22, zero surviving terms, no redundant variable |
| O2 | No coordinate zero section has `a1 != 0`; every `a1`-support dies by grade 15 | S | `a1^3` in `Tg15_3` with coefficient `-1/16`; rederives the recorded `A10` grade-15 death |
| O3 | Divisibility preflight table (0 / 0 / 2 / 1 divisors) | S | Verified; matches V37's `component_products` and rank signatures in both lanes |
| O4 | "W17--W19 complete forever" is a two-line argument, not a solver output | S | Verified: all rows weight-homogeneous, all 65 variables weight `>= 1` |
| O5 | Theorem A: `e0=e1=ee0=ell1=0` on `D(a1)`, `rho=0`; Case B empty; A2 relations | S | Every displayed residual replays exactly; no hidden division; `char != 2,3` for Case B, `!= 5` for A2 |
| O6 | Theorem A is radical/field-point scope, not a certificate | S | Correct and necessary; **now sharpened**: `e0=0` is an exact ideal identity and `a1^2*e1^3 in I` exactly (§4.2), with a verified multiplier certificate |
| O7 | "`K00` is the most degenerate point of a 43-dimensional family"; receiver conclusions from `L43` | **W (scope)** | `L43` lies in `{a1=0}`, outside the chart's unit locus, and the honest receiver equations live in a different ring. The transfer is not established. Grok's §7.2 names this error class |
| O8 | Bottleneck 2.1(2): "the terminal receiver has no algebraic closure route on this source" | **W** | `Phi7` is a unit on the restriction-first K00 section. Correct statement: raw rows are silent, and §6.4 explains why |
| O9 | §4.2 generic-`L43` honest-equation falsification test | U | Not well-typed as designed (no named jet -> `(C, Lambda, k10, …)` map). Superseded by `H_K00` |
| O10 | "`K00`, `Z00`, `CS0` are three points of one phenomenon" | U | Retracted; different charts, different families. §6.4 supplies the real common cause |
| O11 | Avenue 32 raise; row-32 secant presentation as the receiver's missing input type | **U — withdrawn** | Wrong ideal, wrong localizer, wrong ambient ring; and row 32's own stuck point would beg the question (§3.5) |
| O12 | Avenue 38 raise as a proof-side preflight instrument | SC | The instrument is real and paid three times this round; the "tropical" filing is cosmetic. Raise the *instrument*, not the label |
| O13 | Bottleneck 2.1(6): every grade-16+ export lives on the wrong side of `593f953b…` | S | Correct and under-weighted by the other three reports |
| O14 | Card C support-incidence preflight as a launch gate | S | Fixtures verified (V37 W17/W18 signature, `A10`, `L43`) |
| O15 | Disclosure of the read-only `git status` on `jc2-lean` as a boundary slip | S | Correct to disclose. No `jc2-lean` contact of any kind this session |
| O16 | **New here:** `a1^4 in I_20` implies some grade-20 row is nonzero at the V34 point | S | Derived and verified in §1.2; makes the W20 span possibly unnecessary |

---

## 8. Strongest genuinely unique contribution of each model, after deduplication

- **Sol — the exact first-occurrence symbol and its rank.** Not "a symbol
  exists", but: the symbol is *stationary* from grade 14, its rank on the
  ordered chart is *exactly two* (not the tempting ambient three), the drop
  is caused by an *ideal* identity `e0 = 0` rather than a genericity
  argument, and the compatibility quotient is a free rank-five module
  spanned by rows 3--7. Every entry replayed exactly. This is the only
  result in the round that explains *why* prolongation has been failing
  rather than recording *that* it failed, and it converts "export another
  grade" from a plan into a provably ineffective move. Its companion K00
  report contributes the round's most valuable single sentence: saturation
  and restriction do not commute, with a two-line counterexample.

- **Fable 5 — the restriction lemma turning V37 into a shape floor.** Four
  isolated nonmembership data points become a complete exclusion lattice
  over an infinite family of certificate shapes, valid at *any* depth, by
  pure hand algebra with no compute. The reasoning hygiene is the best in
  the round: it uses `rho = 0` in the one direction the promoted correction
  permits, and it states its own weight-20 boundary precisely rather than
  rounding it up to "forever". The independent V34 cross-check of W20 is a
  genuine second chain to the same conclusion.

- **Grok — the `rho`-split of K00, and the base-point/`Proj` warning.**
  Both are corrections nobody else made, and both are load-bearing:
  `K00_rho` and `K00_0` are different geometric objects with different
  applicable theorems, and the `C6 != 0` localization in the post-snapshot
  design silently decides only the first. The `Proj` versus `V(I)` warning
  is independently the same correction as the K00 report's non-commutation
  lemma, reached from the arc side. Grok also produced the only correct
  *cheap* mechanism for testing whether honest generators disturb a frozen
  negative result — once its semantics are repaired.

- **Opus 5 — exact desk-scale replay as a first-class instrument.** The
  support hypergraph (4,997 supports, 88 minimal, hitting set 22, `L43`),
  the divisibility preflight that shows half of a dual-host exact-`Q` AWS
  campaign was answerable in milliseconds, the chart-wide `T-a1` cascade
  that is derived rather than guessed, and the free grade-20 point
  preflight of §1.2. The common thread is that questions the campaign has
  been routing to AWS are decidable on a laptop in seconds, and that
  ansatz-free hand identities have now closed three charts (`T-c1`,
  `T-a0`, and Case B of `T-a1`).

---

## 9. Merged executable idea cards

### M1 — Ordered `T-a1`: symbol-reduced compatibility cascade, with the free W20 gate

Merges Opus5 Card A, Sol blind Card B, Sol's post-snapshot symbol theorem,
and Fable5 Card 3. Replaces all four.

- **Dependency.** The 70 frozen rows (70/70 hashes verified); the pinned
  V23 AST parser; Sol's symbol matrix and its two Bezout certificates;
  promoted `16ec6f54…` and its converse correction `593f953b…`. For the
  gate only: a grade-20 ordered-`a1`, `rho=0` export in the V28--V35
  pattern (AWS, bounded, one grade).
- **Cheapest exact discriminator.** Desk scale, no solver. At each grade
  `g = 15..19`, in branches A1 (`ell1 = rs1 = 0`) and A2 (`aa0 = 0`,
  `k*rs1^2 = (96/5)a1^2`, `ee1 = a1*ell2`): (i) solve rows 1 and 2 for two
  newcomers using the unit `EC` pivot and the `q/s` or `q/h` Bezout
  certificate — Sol's theorem guarantees this always succeeds on `D(a1)`;
  (ii) reduce the five compatibility rows 3--7 in the old variables; (iii)
  look for a forced vanishing or a two-row identity of `T-c1`/`T-a0` type.
  A2 is the small branch and should resolve first.
  **Separately and independently**, once the grade-20 export lands:
  evaluate the seven grade-20 rows at the frozen scaled V34 point. If all
  seven vanish, `a1^4` is a nonmember **forever at weight 20** with no
  linear algebra at all; only if one is nonzero does the W20 span get
  funded, and then under Fable5's HARDENED-LADDER.
- **Both outcomes.** *Contradiction in both branches* ⇒ ordered `T-a1` has
  empty `rho=0` fibre on `D(a1)` at radical scope. That is **not** a
  certificate; the conversion to an honest `a1^N s (1+rho W)` identity is a
  separate, unproved step, and §1's floor says the cheapest surviving
  target shapes are `(4,0)` then `(1,4),(2,3),(3,2)`. *A surviving branch*
  ⇒ an explicitly parametrized candidate family — incomparably better
  input than a guessed support — and the correct input to one bounded AWS
  `std` on that branch only. *W20 gate vanishes at `P`* ⇒ the shape floor
  becomes nine `a1`-shapes plus `(4,0)` excluded forever, frontier moves to
  weights 21--23.
- **Stop rule.** Stop the cascade if two consecutive grades add no forced
  vanishing and no two-row identity in *either* branch — that is the signal
  that the residual content is genuinely nonlinear and needs a solver. Stop
  immediately if the `rho=0` restriction is shown lossy for the registered
  chart type. Never prolong the dead V32/V34 orbit. Any nonmembership at
  weight `> 20` must be labelled "through grade `g`", never "forever".
- **Exact scope firewall.** Raw `rho=0` ordered-`a1` row ideal, on `D(a1)`,
  `char != 2,3,5`, radical/field-point scope except where an explicit
  multiplier certificate is exhibited (`e0 = 0`; `a1^2 e1^3 in I`). Says
  nothing about the honest saturated chart, the terminal receiver, source
  coverage, deck/square, `G2-PSC`, order two, maximum twelve, or JC2.

### M2 — `H_K00`: closure-first terminal incidence, `rho`-split, with the target-grade preflight

Merges Sol's post-snapshot design, Sol blind Card A, Fable5 Card 2, Grok
Card A.

- **Dependency.** The promoted one-parameter Rees reduction and its AWS
  compiler; `M_K00` as written; the receiver audit `b6c1c4ce…`; the
  restriction-first unit (5.6) as negative control; the deck control (7.4).
- **Cheapest exact discriminator.** *Free desk preflight first:* confirm
  from the frozen emitter that the four inhomogeneous targets `mu2, mu4,
  mu6, Jdet/4` enter only at sigma-grades 28, 32, 36, 38, hence that every
  exported raw row through grade 19 is target-free. This costs one grep and
  it is what licenses stopping all raw receiver work permanently.
  *Then* compute `K = (Phi):(Lambda*Jdet)^infinity`,
  `B = K + (Lambda) + M_K00`, `H_K00 = B:(C6*k10*Jdet)^infinity`, exact `Q`
  as the mathematical lane with a separately serialized good prime as a
  software control. Mandatory controls: restriction-before-saturation
  reproduces (5.6); `rho -> -rho` invariance and contraction of the deck
  form back to `M_K00`; a met/unmet hypothesis bit per invoked theorem.
  **Register `K00_0` (`rho = 0`, `C6 = 0`) as a separate case** — the
  `C6 != 0` localization does not reach it.
- **Both outcomes.** `H_K00 = (1)` with a saved certificate ⇒ the first
  honest exclusion of the generic K00 incidence for this fixed `[6,2]`
  ordinary-tail client. `H_K00 != (1)` ⇒ accessible algebraic boundary
  support — **not** a Taylor realization, **not** a rational coefficient
  trajectory, **not** a Keller pair, **not** a germ. In that case the next
  object is the uncompiled Taylor families, not another tail export.
- **Stop rule.** One run plus its controls. Do not extend to the `C6 = 0`
  tip, `k10 = 0`, other load rays or other square-normal cones without a
  separate registration. If the compiler cannot produce `(Phi)` in one lane
  cycle, the deliverable is the precise missing base-change object, not a
  surrogate standard basis.
- **Exact scope firewall.** One generic terminal incidence for one fixed
  source profile. Does not empty `V(J1+J2)`, does not decide Gate T, does
  not decide `K00_0`, and `J1 = J2 = 0` never implies an empty blowup fibre.

### M3 — Preflight and dual-transport gate (fail-closed), hardened

Merges Opus5 §4.3/Card C, Grok's dual transport (semantics repaired),
Fable5's HARDENED-LADDER and section-first rule.

- **Dependency.** The pinned V23 AST parser and the frozen `.poly` bytes
  only. No AWS, no new mathematics.
- **Cheapest exact discriminator.** One script, one lane-session, three
  functions: (i) **support incidence** — minimal monomial supports, target
  divisibility, and maximum coordinate zero sections by exact branch and
  bound; (ii) **section-first** — evaluate a proposed target's units
  against the registered section list before funding any sweep; (iii)
  **dual transport with the corrected semantics of §2.5** — for each frozen
  functional and each new *weight-homogeneous* generator, enumerate **all**
  complementary-weight monomial multipliers and report survive/invalidate,
  and **nothing else**. Fixtures that must reproduce: V37's `rank 0` /
  one-term functional for W17 and W18; the grade-15 death of `A10` from
  `{a1}`; `L43` with `k` free; `lambda(phi19) = 7855/6912` as the standing
  negative control against re-reading a dual as a primal. Hardening per
  Fable5 §4: fail-closed over **every** metadata field, relocatable
  evidence paths (remap AWS-absolute paths at harvest), static pinning of
  `shared_faber_probe` at library import rather than only in `main()`, dual
  modular selectors with exact-`Q` full-product replay, plus one
  deliberately mistyped certificate and one deliberately corrupted metadata
  field as mandatory negative controls.
- **Both outcomes.** Reproduces all fixtures ⇒ adopt as a mandatory launch
  gate for every landing membership/emptiness job. Disagrees on any fixture
  ⇒ a real defect in either the preflight or the frozen census, found for
  free.
- **Stop rule.** One lane-session. It is a script, not research. If it
  grows a solver, it has become a different lane and needs its own
  registration.
- **Exact scope firewall.** The tool may only ever **refuse** work. It must
  be structurally incapable of emitting a membership verdict, an emptiness
  verdict, or a "predicted certificate type". Coordinate sections only —
  it cannot see Kummer-type parametrized sections, and a clean report from
  it is never evidence that a chart is closable.

---

## 10. Decisions

### Launch now

1. **M1 cascade continuation** (desk, zero compute, one lane). Highest
   information per dollar in the portfolio; already killed one of two
   branches and four coordinates.
2. **Grade-20 ordered-`a1` `rho=0` export** (AWS, bounded, one grade) —
   *resolving the Fable5/Opus5 disagreement in Fable5's favour, with my
   gate attached*: export, but fund the W20 span **only** if some grade-20
   row is nonzero at the frozen scaled V34 point. My blind "stop for now"
   was wrong; the export is the only route to a forever-labelled `(4,0)`.
3. **M2 free preflight** (target grades 28/32/36/38), then **`H_K00`** on
   AWS with its controls and the separate `K00_0` registration.
4. **M3 preflight/transport gate** (one lane-session, desk).
5. **AS109 arithmetic `(deg_y, v_109)` Newton corner `n=2`** with the exact
   source-gauge section applied first — **or an explicit demotion.** All
   four reports rank it and none has run it; this is now the third
   consecutive round with a ranked, unblocked, cheap experiment idle, which
   is a `COORDINATION.md` fresh-eyes-reset trigger. Ranked-and-idle is the
   worst of the three options.

### Continue in background

- **TD6 H19R2 exact-`Q`** (r6d, Box01) to cap; harvest original-FIRST
  multipliers and the denominator-cleared total-`F` certificate. Unanimous.
- **V29 capped grade-16 Groebner controls** to their existing caps, then
  harvest and stop — *I concede my blind `stop`*; the jobs are already
  running and cancelling buys nothing. No extension.
- **D1 residual source/timing faces**, narrowly.
- **Direct total `T-cs`** at low priority; **V19 `T-cs` 26-generator lift**
  then type-gate.
- **Web sweep** on its unchanged `2026-08-28T00:00Z` clock.
- **`jc2-lean`** asynchronous and untouched.

### Hold

- **Grok Card C support increment** — its decisive outcome branch is
  structurally impossible (§5.2). Hold pending a redesign that targets the
  compatibility rows 3--7 in *old* variables, which is M1.
- **Any further terminal-receiver work beyond `H_K00`**, including the
  `C6 = 0` tip and `k10 = 0` rays, until `H_K00` returns.
- **Prime-ray full `3P-E31`** — firewall stands.
- **Fable5 Card 1 TRIVIAL-LOCUS at coordinate-support scope** — already
  answered NO through grade 19 (§3.1). Hold, and relaunch **only** in the
  form that has residual value: non-coordinate/parametrized sections
  solved scheme-theoretically over `Q`, plus the all-depth emitter
  statement. Fable5's own self-audit item 4 is the reason.

### Stop

- **Deeper raw-row receiver exports, raw-leaf standard bases, and any
  further raw grade aimed at emptying `V(J1+J2) ∩ D(k)`.** Unanimous across
  all four reports, and §6.4 now gives the mechanism: the exports stop at
  grade 19 and the discriminating targets enter at grades 28--38.
- **V32/V34/V36 six-coordinate orbit prolongation**, including the
  symbolic `Tg18_6` reduction on the grade-17 curve. Unanimous.
- **V37-style hunts at any of the nine `a1`-shapes now excluded forever**,
  and at pure `k^j` for `j <= 4`. Provably wasted compute.
- **Grok's Card B (iii) rewrite** as an object; the transport survives only
  in the repaired form of §2.5.
- **My avenue-32 raise and the row-32/receiver bridge.** Withdrawn.
- **My §4.2 generic-`L43` honest-equation test** as designed. Superseded by
  `H_K00`.
- **Serial affine-Faber `H` increments; paid AS109 rigid-leaf search.**
  Unchanged.

---

## 11. Verdict — does Opus 5 supply significant unique campaign capability beyond Fable 5 this round?

**Yes, but narrowly, and with a real self-inflicted deduction. Not
dominance.**

*For.* Four things in this round exist only because of exact desk-scale
replay, and none of them appears in Fable5's report: the support hypergraph
and `L43` (which is *maximum*, not merely maximal, and which I proved
rather than estimated); the divisibility preflight, which demonstrates that
two of V37's four dual-host exact-`Q` AWS targets were answerable in
milliseconds; the chart-wide `T-a1` cascade, which is derived rather than
guessed and which independently arrives at the same structure Sol's symbol
theorem explains; and the grade-20 point preflight of §1.2, which may make
the W20 span unnecessary altogether. Two of these directly consume Fable5's
own work: `L43` closes the pure-`k^j` gap in Fable5's shape floor, and the
`{a1}` singleton answers Fable5's flagship Card 1 question NO at coordinate
scope for free, including the exact `A10` grade-15 control that card asked
for. Fable5 could not have produced either without the instrument.

*Against.* Fable5's restriction lemma is the strongest single
*theorem-shaped* result of the round, and it was obtained by hand with no
compute at all — which is a capability I did not display. My report also
contains the weakest strategic reasoning of the four submissions: I took an
exactly-correct computation about the ordered-`a1` chart and used it to
rerank the *terminal receiver* and to raise an avenue on a type-match that
does not hold. Both the bottleneck claim and the avenue-32 raise are
withdrawn above. That is not a presentational slip; it is the specific
failure mode of a compute-first researcher — letting a verified number
license an unverified geometric identification — and it cost the round a
disposition change that has to be reversed.

*Net.* The marginal capability is real and it is **instrumental rather than
theoretical**: exact byte-level replay, combinatorial preflight, and
line-by-line verification of other models' hand algebra. That capability
independently confirmed Fable5's V34 cross-check to the digit, verified
every entry of Sol's symbol matrix and all thirty of its term counts,
verified the K00 report's core by hand, and refuted two of Grok's displayed
conclusions with one-line certificates. On correctness-adjusted information
gain the ranking this round is **Sol (post-snapshot) > Fable 5 ≈ Opus 5 >
Grok**, and the case for keeping Opus 5 in the loop rests on the
verification and preflight role, not on out-reasoning Fable 5 at the
whiteboard. The corrective for the failure mode is mechanical and should be
registered: **every disposition change must name the ring its evidence
lives in**, and any claim that crosses from one ring to another must
exhibit the map.

Nothing in this report proves or disproves JC2, closes Gate T, empties the
terminal receiver, closes ordered `T-a1`, promotes V37, globalizes TD6,
supplies `G2-PSC` or `G2-BD`, bounds `td`, or produces an AS109 lift.

---

## 12. File-read / tool / edit disclosure

**Read in full, SHA-256 verified against the prompt (7/7 match):** the
sealed packet; the four blind submissions (`sol`, `fable5`, `grok`,
`opus5`); the two post-snapshot sol design reports (K00 discriminator;
first-occurrence symbol/Spencer).

**Read for verification (not promoted):** all **70** ordered-`a1` `.poly`
row files from `..._typed_census_v23_20260827/output_r1/a1_ordered/`
(grades 10--15), `..._boundary_prolong_g16_v28_.../aws_q/compiled/`,
`...g17_v30_...`, `...g18_v33_...`, and
`...grade19_rational_orbit_v35_.../aws_q/compiled/` (grades 16--19); V37's
`aws_q65521/RESULT.json`, `aws_q65519/RESULT.json` and both
`compiled/result.json`; `census_j2_typed_v23.py` (the `sigma_weight` table
and parser head); `solve_graded_ladder_v37.py` (grep only, for the weight
and completeness logic); `..._v35_.../PREREGISTRATION.md` and
`evaluate_grade19_orbit_v35.py` (grep only, for the frozen `POINT`);
directory listings under `cases/` and `xmodel/`.

**Tools used:** `Bash` only (`shasum`, `cat`, `head`, `sed`, `grep`, `ls`,
`find`, `wc`, and `python3` running exact `Fraction` arithmetic from
scripts staged in `/tmp/xr/`). Total runtime seconds; peak memory far under
1 GiB. **No CAS, no Groebner engine, no network, no AWS, no heavy or
sustained computation.**

**Edits:** exactly one file written — this report,
`xmodel/ideation-20260827T0635Z-opus5-crossreview.md`. No campaign artifact
was created, modified, staged, or deleted. Two scratch scripts were written
outside the repository under `/tmp/xr/`.

**`jc2-lean`:** not read, entered, built, inspected, edited, staged,
cleaned, or contacted in any way during this session — including no
`git status`. (My blind report disclosed a read-only `git status` slip in
the prior session; there is no such contact here.)

**Blind-submission integrity:** no blind submission was altered. Where
post-snapshot evidence supersedes or sharpens a blind claim, it is marked
as such in §§1, 3, 5, 6 and in the claim matrix.
