# Different-model promotion cross-audit: D5G, R6, K00 V24R6R1

Date: 2026-08-27
Auditor lane: Opus5, independent different-model promotion gate
Repository `HEAD` at audit time: `418e413593120d19e15e6546eb50c985f4b1f038`

This is a single combined review of three independently charged Sol-produced
results.  Prior Sol/Sol2/Sol-Ultra audits were read only after I had
reproduced the mathematics myself; they are treated as claims, not evidence.
Every number reported below was recomputed in this session.

## Verdict summary

| Item | Verdict |
|---|---|
| **A. D5G raw-global determinant / `H`-multiple custody** | **CONFIRMED** (scope narrowed; see A.9) |
| **B. R6 endpoint-survivor parametrization and codimension** | **CONFIRMED**, strengthened to *exactly* `floor(h/2)`; harness is `GAP` (non-blocking) |
| **C. K00 V24R6R1 selected `D(W)` certificate** | **CONFIRMED** |

No item is REFUTED.  The only `GAP/REPAIR` finding is B's regression
harness, which does not carry the theorem and does not block promotion.

## Execution basis

All work was desk-scale and exact.  Independent scratch code lives outside
the repository in `/tmp/o5audit/` (own sparse polynomial arithmetic over `Q`,
own Singular-syntax parser, own exact linear algebra; `sympy` is not
installed).  Local Singular 4.x was used only for the three *read-only*
`.sing` replays in item C, executed from `/tmp` on copies.  No AWS, no
browsing, no `jc2-lean` access, no producer artifact or canonical ledger was
modified.  I touched exactly one repository file: this one.

**Custody of the charged bytes.** All fourteen charged hashes reproduce from
live bytes, with one path-label correction: the charge lists
`cases/ggv_endpoint_survivor_codimension_r6_20260827/FREEZE.md`, but
`9c23f3f5e99672208e49bebca17b38b81b9190537a08aa4ffd1127132f148bd4` is the
hash of `FREEZE.sha256` in that directory.  There is no `FREEZE.md`.  The
content is correct; only the charge's filename is wrong.

---

# A. D5G direct raw-global determinant custody — CONFIRMED

## A.1 Chart Jacobian and coefficient recurrence — CONFIRMED

I re-derived this from scratch rather than checking the producer's algebra.
D3's frozen maps are `x^i y^j -> t^(8+3i-j) X^i` for `F` and
`x^i y^j -> t^(12+3i-j) X^i` for `G`, i.e. the chart

```text
x = t^3 X,   y = t^-1,   F = t^8 f,   G = t^12 g,   t = 1/y,  X = x y^3.
```

With `f = y^8 F` and `g = y^12 G`, differentiating through `(t,X)` gives

```text
f_x = y^11 F_X,
f_y = 8y^7 F - y^8 t^2 F_t + 3x y^10 F_X,
g_x = y^15 G_X,
g_y = 12y^11 G - y^12 t^2 G_t + 3x y^14 G_X,
```

and in `f_x g_y - f_y g_x` the two `3x y^25 F_X G_X` terms cancel, leaving

```text
Jac_(x,y)(f,g) = y^22 [ 12 F_X G - 8 F G_X - t (F_X G_t - F_t G_X) ] = t^-22 E.
```

Extracting `t^n` from `E` with `F = sum_i t^i F_i`, `G = sum_j t^j G_j`:
`12F_XG` contributes `12 F_i' G_j`; `-8FG_X` contributes `-8 F_i G_j'`;
`-t F_X G_t` contributes `-j F_i' G_j`; `+t F_t G_X` contributes
`+i F_i G_j'`.  Hence

```text
D_n = sum_(i+j=n) ( (12-j) F_i' G_j + (i-8) F_i G_j' ),
```

exactly as charged.  Both shifted integers and both signs are correct; the
`+i` genuinely comes from `+t F_t G_X`.  I also confirm the audit's
coordinate Jacobian `det d(x,y)/d(X,t) = t^3 * (-t^-2) = -t`, consistent with
its `det d(f,g)/d(X,t) = -t^-21 E`.

This also explains the target that D5G declines to assume: `Jac = const`
would read `E = c t^22`, i.e. `D_0 = ... = D_21 = 0` with `D_22` constant.

## A.2 D3 polygon support and the 400 positive slots — CONFIRMED

I enumerated both polygons independently and compared tuple-by-tuple against
`RAW_INPUT.json`, also re-deriving every `weight`, `slot` name,
`raw_monomial`, and `chart_image` field:

```text
F/2S:  0<=i<=16,  max(0,4i-8)  <= j <= 3i+8,   n = 8+3i-j,   0<=n<=22
G/3S:  0<=i<=24,  max(0,4i-12) <= j <= 3i+12,  n = 12+3i-j,  0<=n<=22
```

Both enumerations match exactly, with no extra and no missing lattice point.

| source | rows through 22 | weight-0 rows | positive rows |
|---|---:|---:|---:|
| `F` | 141 | 17 | 124 |
| `G` | 301 | 25 | 276 |
| total | 442 | 42 | **400** |

Per-weight counts reproduce exactly: `F` = 17,16,15,14,13,12,11,10,9,7,6,5,3,2,1
and `G` = 25,24,...,17,16,15,14,13,11,10,9,7,6,5,3,2,1.

**Weight 0 is a real check, not a convention.** `H^2 = (X^8-1)^2` has
`X`-degrees 0..16 (17 monomials) and `H^3` has 0..24 (25 monomials), matching
the 17 and 25 weight-zero row counts exactly.  D5G correctly *replaces* those
rows with the fixed polynomials and treats precisely the remaining 400 as
independent indeterminates.  No `F15`, `G22`, or out-of-support row appears.

**Truncation soundness (checked, not assumed).** Weights are non-negative on
these polygons (that is exactly the upper edge `j <= 3i+8` / `3i+12`) and
additive under `i+j=n`, so no row of weight `>22` can contribute to any
`D_n` with `n<=22`.  The truncation at weight 22 is therefore sound for the
charged range — but note that non-negativity is *inherited from D3's polygon*
and is not re-derived inside D5G.

## A.3 Literal `D_0,...,D_22` and contribution provenance — CONFIRMED

I wrote an independent compiler that reads only `RAW_INPUT.json`'s slot
support, builds `F_i`, `G_j`, applies the recurrence of A.1, and emits both
the sparse terms and the pre-combination provenance records.  Results:

```text
32,135 final sparse terms          (artifact: 32,135)
58,572 pre-combination records     (artifact: 58,572)
per-weight term counts 0,131,503,839,1132,1375,1594,1795,1915,2036,2078,
                       2116,2109,2057,1950,1847,1703,1556,1408,1265,1006,942,778
```

Every one of the 23 weights matches **term for term** and **contribution for
contribution**, including the two source row identifiers, derivative side,
output `X` degree, and rational coefficient.  Recomputing the producer's
digest scheme over *my* records gives per-weight digests that all match and a
digest-of-digests

```text
cbe21f966bc15d70336ce18176c5954600b32b7d5320dc9e67f8a79f6a5ace45
```

identical to the artifact and to the Sol-Ultra audit's independent value.
The top-level and endpoint-certificate copies of the 1,374 weight-22 records
are byte-equal to each other and to mine.  I also hand-recomputed six sampled
contributions at `n = 0, 11, 22` from the row identifiers alone; all six
agree.

**`D_0 = 0` is a checked cancellation.** `F0` has 3 terms, 2 with nonzero
derivative; `G0` has 4 terms, 3 with nonzero derivative; so
`2*4 + 3*3 = 17` contributions, matching the artifact.  Their coefficients
cancel at every `X`-degree (7, 15, 23, 31, 39 all sum to zero), which is the
identity `12(H^2)'H^3 - 8H^2(H^3)' = 24H^4H' - 24H^4H' = 0`.

**Weight 22 is structurally pure.** Since `deg_wt F <= 14` and
`deg_wt G <= 21`, `i+j=22` admits neither `i=0` nor `j=0`.  I verified that
all 778 terms of `D_22` are of slot-degree exactly 2 — no fixed leading-row
and no linear term reaches weight 22.  (For contrast `D_1` is purely linear
with 131 terms, and `D_2,...,D_21` are mixed.)

## A.4 Monic division `D22 = H*Q22 + R22` — CONFIRMED

I divided by the closed form `X^d = H * sum_(a<q) X^(r+8a) + X^r` for
`d = 8q+r`, applied coefficientwise in the raw ring, entirely independently
of the producer's loop:

| object | terms | max `X` degree |
|---|---:|---:|
| `D22` | 778 | 17 |
| `Q22` | 523 | 9 |
| `R22` | 778 | 7 |

`H*Q22 + R22 = D22` holds exactly, and my `Q22`, `R22` are term-for-term
equal to the certificate's.  `H` is monic, so this is ordinary Euclidean
division in `C[X]` with no localization and no evaluation at roots.

## A.5 The `M` reduction and the seven-vector — CONFIRMED

`M(Y) = 4HY' + 6H'Y`, and D3's map line `Y -> 4*(X^8-1)*Y' + 48*X^7*Y` is the
same operator since `6H' = 48X^7`.  On monomials

```text
M(X^k) = 4(k+12) X^(k+7) - 4k X^(k-1).
```

`M` raises degree by exactly 7 with leading coefficient `4(deg Y + 12) != 0`,
so `M` is injective and `{M(X^k)}` has leading degrees `7,8,9,...`.  Hence
every polynomial has a **unique** decomposition `M(Y) + r` with `deg r <= 6`,
and the cokernel is exactly 7-dimensional.  This is the whole justification
for the seven-vector, and it checks out.

| object | terms | max `X` degree |
|---|---:|---:|
| `Y22` | 621 | 10 |
| `rM22` | 680 | 6 |

Both match the certificate exactly, `M(Y22) + rM22 = D22` holds exactly, and
the seven coordinates carry `93, 90, 90, 97, 104, 103, 103` terms (sum 680),
as claimed.  Two further independent confirmations:

- the closed-form remainder of `X^(8q+r)` — zero for `r=7`, else
  `prod_(s=1..q) (r+8s-7)/(r+8s+5) * X^r` — reproduces `rM22` exactly;
- I replayed all **621** trace steps: every recorded `(monomial, degree,
  coefficient, k, lambda)` has `k = d-7` and `lambda = c/(4(k+12))`, every
  recorded leading coefficient equals the running one, degrees are
  non-increasing, and the replay lands on exactly my `Y22` and `rM22`.
  Zero arithmetic errors.

## A.6 The four exact deltas — ALL FOUR CONFIRMED

I derived these by hand *before* computing, then confirmed by rebuilding the
mutated objects from scratch.

- `Delta Q = 1` and `Delta R = 0`: immediate from uniqueness of Euclidean
  division, `(D22+H) = H(Q22+1) + R22`.
- `Delta Y = X/52`: `M(cX) = 4cH + 6H'cX = 4cX^8 - 4c + 48cX^8 = 52cX^8 - 4c`;
  matching the `X^8` coefficient of `H` forces `52c = 1`, so `c = 1/52`.
- `Delta rM = -12/13`: then `-4c = -1/13`, so `ΔrM = -1 - (-1/13) = -12/13`.

Recomputation gives exactly `{X^0: 1}`, `{}`, `{X^1: 1/52}`, `{X^0: -12/13}`,
and the certificate's four mutated objects are term-for-term equal to mine.
The mutated seven-vector differs from the original in exactly one place: the
`X^0` coordinate, by `-12/13`.

**Why this is the right custody statement.** I verified D3's firewall claim
directly: the map `Y -> rM(H*Y)` on `Q[X]_(<=6)` is diagonal with entries

```text
-12/13, -6/7, -4/5, -3/4, -12/17, -2/3, -12/19,   det = -20736/146965 != 0,
```

so it is an isomorphism.  The mod-`H` remainder `R22` therefore carries *no*
information about the seven-vector; the global `H`-multiple `Q22` is exactly
the missing datum.  The `-12/13` of the mutation is precisely the `(0,0)`
entry of this matrix.  (I also checked D3's quarantined positive control
`E22 = 1 + (13/12)(X^8-1) = M(X/48)` — remainder zero, as claimed.)

## A.7 Source/compiler mutations — CONFIRMED

Rebuilding the entire determinant under each mutation and counting changed
coefficients across all 23 weights:

| mutation | independently changed coefficients |
|---|---:|
| delete raw slot `f_0_1` | **243** |
| replace `(i-8)` by `(i-7)` | **31,428** |

Both reproduce the Sol-Ultra audit's numbers exactly.

## A.8 Dependency lock, hashes, replay — CONFIRMED

All seven `FREEZE.sha256` entries verify, and every dependency pin in
`RESULT.json` (D3 freeze and raw input, D4R1 hold freeze, D5 design freeze,
`M`-cokernel audit, preregistration) matches live bytes.  The producer replay

```text
python3 -B compile_d5g.py --check ... -> PASS D5G exact raw-global replay
```

runs in 3.5 s, is read-only, and wrote nothing.

**D4R1 non-consumption, in the strongest available form.** Static inspection
shows `compile_d5g.py` reads exactly one key from the source JSON,
`raw_slots_through_weight_22`, and the only D4R1 path it names is
`FREEZE.sha256`, hashed inside `build_result` and never passed to
`determinant`, `build_certificate`, either reduction, or the dense control.
Stronger than static inspection: **I reconstructed every numeric object in
D5G's artifacts — all 32,135 terms, all 58,572 provenance records, all 23
digests, `Q22`, `R22`, `Y22`, `rM22`, the seven-vector, and all four mutated
objects — from D3's slot support alone.** There is no room for a D4R1 datum,
a Morse row, a carrier value, a source equation, or a branch bit to be
embedded in them.

## A.9 Findings that must accompany promotion

These are scope refinements, not defects.  None of them changes the verdict.

1. **The D3 source is self-declared artificial.** `RAW_INPUT.json` carries
   `"scope": "artificial frozen control only; symbolic raw 2S/3S slots
   through weight 22"` and `"control_id": "R0_ARTIFICIAL_CUSP_CONTROL"`.  The
   `2S/3S` support D5G compiles over is a **frozen control fixture**, not an
   established `8_28` Newton face.  The producer note and audit both disclaim
   "`8_28` face/family exclusion", which covers this, but the note's framing
   ("D3's 400 positive-weight `2S/3S` rows") reads as though the support were
   derived.  The promotion sentence must name the fixture.  D5G itself reads
   only the slot *support*: it never touches
   `literal_artificial_raw_face`, `quarantined_global_polynomial_control`,
   `local_carrier_fixture`, or `formal_root_sign_packets`, so no artificial
   *coefficient value* enters the compilation.

2. **The producer's internal "independent dense specialization" is a weak
   control.** Its assignment is `(index mod 13 + 1) * (-1)^index` over 400
   slots, i.e. values drawn from `{+-1,...,+-13}` with massive collisions.
   Agreement of two computations at one such structured point is poor
   evidence for a polynomial identity in 400 variables.  It is a good
   catch-most-bugs check and it is not wrong, but it should not be cited as
   independent verification of the identity.  My full symbolic replay (A.3)
   supplies what it cannot.

3. **The `D22 -> D22+H` mutation cannot fail.** `ΔQ=1` and `ΔR=0` follow from
   uniqueness of Euclidean division, and `ΔrM=-12/13` is a fixed diagonal
   entry of the firewall map — none of the four values depends on the 400
   slots at all.  It is a valid and instructive *demonstration* that `R22` is
   blind to global `H`-multiples while `Q22` and the seven-vector are not,
   which is the point of the case.  It is not a falsification test of the
   compilation.  The discriminating controls are the drop-slot and
   `(i-8)->(i-7)` mutations plus full replay.

4. **`D_0 = 0` is established unconditionally**, and it is one of the 22
   target equations — forced by the fixed leading rows, not assumed.
   `D_1,...,D_21` are all genuinely nonzero as generic expressions (131 to
   939 terms each), so the note's "not assumed zero" is honest in both
   directions.

5. **Cross-case consistency observation (not a D5G claim).** The fixture's
   `H = X^8-1` is squarefree, so in item B's language `h=8`, `b=8`, giving
   `r = (8-24+2)/2 = -7 < 0`: degree-excluded at the rational endpoint.  This
   `H` could never be an endpoint survivor.  That is consistent with D5G
   asserting no target verdict, and it reinforces that the fixture is a
   control rather than a live candidate.

## A.10 Maximum promotion — item A

> **D5G may be promoted exactly as:** a review-independent, exactly
> replayable *compiler and custody* result.  Over the D3
> `R0_ARTIFICIAL_CUSP_CONTROL` frozen support — 400 algebraically independent
> positive-weight `2S/3S` slots together with the fixed rows `F0 = H^2`,
> `G0 = H^3`, `H = X^8-1` — the literal generic raw-coordinate determinant
> coefficients `D_0,...,D_22` of
> `E = 12F_XG - 8FG_X - t(F_XG_t - F_tG_X)` are exactly as frozen, with full
> pre-combination provenance; `D_0 = 0` by checked cancellation; and the two
> unique exact decompositions `D22 = H*Q22 + R22` (`deg_X R22 < 8`) and
> `D22 = M(Y22) + rM22` (`deg_X rM22 < 7`, `M(Y) = 4HY' + 6H'Y`) hold with the
> frozen `Q22`, `R22`, `Y22`, `rM22` and seven-vector.  The global
> `H`-multiple `Q22` is genuinely independent custody, because reduction
> modulo `H` provably loses it.
>
> **Nothing beyond that.** No Keller specialization, no `R22=1`, no `Q22=0`,
> no `D_1 = ... = D_21 = 0`, no local or global naturality square, no D4R1
> consumption or endorsement, no Keller-row, target, specialization, or
> family result, no `8_28` face/family exclusion, no `G2-PSC`, no `G2-BD`, no
> counterexample, no JC2.  In particular the underlying support is a frozen
> artificial control, so **no statement about the real `8_28` face is
> licensed at all**.

---

# B. R6 endpoint-survivor parametrization — CONFIRMED (strengthened)

I consumed my own confirmed R5 review at exactly its promoted ceiling:
*a necessary rational-endpoint filter for formal polynomial-`X`
`F_0 = H^2, G_0 = H^3` edges, conditional on the inherited weight-22
normalization `[t^22]E = 1`* — items 5, 6, 7, 8 of that review, all
CONFIRMED.  R6 uses R5's theorem, not R5's verifier, so R5's item-9
`GAP/REPAIR` does not propagate.  The R5 freeze hash pinned in R6's
`FREEZE.sha256` (`3d8ba267...`) matches live bytes.

Everything below was recomputed with my own exact rational polynomial
library (Yun squarefree decomposition, exact Gaussian elimination).

## B.1 Uniqueness of `H = A^2 B` with shared factors — CONFIRMED

For a root of multiplicity `e`, `B` squarefree forces
`mult_B = e mod 2` and `mult_A = floor(e/2)`; both are determined, so the
monic decomposition is unique.  When `e` is odd and `>= 3` the root divides
*both* `A` and `B`, which is correct rather than ambiguous.  Verified on 400
random `H` with prescribed multiplicities 1..7 (deliberately including odd
`>= 3`): `A^2B = H` exactly, `B` squarefree, and the shared factors land where
predicted, in every case.  Explicit fixture:

```text
H = X^5 (X-1)^3  ->  A = X^2 (X-1),  B = X(X-1),  gcd(A,B) = B = X(X-1).
```

## B.2 Degree law, leading coefficients, necessity — CONFIRMED

For monic `B` of degree `b >= 1` and `v` of degree `r`:

```text
deg N_B(v) = r + b - 1,      lc N_B(v) = (r + (3/2)b) lc(v),
```

both terms `Bv'` and `(3/2)B'v` having degree `r+b-1` with leading
coefficients `r*lc(v)` and `(3/2)b*lc(v)`.  The factor `r + (3/2)b >= 3/2 > 0`
in characteristic zero, so `N_B` is injective, `A = N_B(v)` forces
`r = a - b + 1 = (h-3b+2)/2` and `lc(v) = 1/(r + (3/2)b)`, and `r >= 0` is
equivalent to `3b <= h+2`.  R6 drops R5's `lc(B)` factor from (1.1) because
`B` is normalized monic — consistent, not an error.

## B.3 Sufficiency and injectivity — CONFIRMED

For every `h` in 1..14 and every live `b >= 1`, 60 random `(B,v)` each: the
canonical decomposition of `H = N_B(v)^2 B` returns **exactly** the chosen
`(A,B)`, including when `A` and `B` share factors; `deg H = h`; `N_B(v)` is
monic of degree `a`; and no two distinct `(B,v)` produce the same `H`.
Structurally: `H` determines `(A,B)` uniquely by B.1, and `N_B` injective
determines `v` — so the normalized map is injective, hence dimension-
preserving in characteristic zero.

## B.4 Fixed-`b` dimensions — CONFIRMED, with a cleaner proof

I computed the **exact rank of the differential** of
`phi_b : (B,v) -> N_B(v)^2 B` at random parameter points (Fraction
arithmetic, `dH = 2A(dA)B + A^2 dB`), which is the true dimension of the
image in characteristic zero.  For every `h` in 1..14 and every live
stratum the rank equals the predicted `a+1` (and `h/2` for `b=0`) — no
exceptions.

I also found a cleaner derivation than R6's parameter count.  The stratum of
*all* `H` whose squarefree part has degree `b` has dimension `a+b`.  Since
`N_B : K[X]_(<=r) -> K[X]_(<=r+b-1)` is injective with source dimension
`r+1` and target dimension `r+b`, the survivor condition `A in im N_B` is
exactly `b-1` independent linear conditions on `A` for fixed `B`.  Hence

```text
dim   = (a+b) - (b-1) = a+1,
codim = a + b - 1 = (h+b-2)/2,
```

reproducing (0.4).  This makes two special cases transparent:

- **`b = 1`:** `N_B` is a *bijection* on the relevant degree spaces, so
  **every** `H` whose squarefree part has degree 1 is a survivor.  Verified:
  300/300 random samples at `h=9`, and all samples at `h=3,5,7,9,11,13`.
- **`b = 0`:** `N_B = beta d/dX` is surjective in characteristic zero, so all
  perfect squares survive; dimension `h/2`, codimension `h/2`.

Necessity is equally visible: at `h=8, b=2` and `h=9, b=3` and `h=12, b=4`,
random `(A,B)` give 0/300, 0/300, 0/300 survivors; squarefree `H` (`b=h`)
gives 0/200 survivors at `h = 4,6,8,10`.  The occasional 1/300 hit at
`h=6,10` with `b=2` is the codimension-one condition being met by chance at
small integer coefficients, exactly as expected.

## B.5 Codimension is exactly `floor(h/2)` — CONFIRMED (strengthening)

Codimensions are `h/2` for `b=0` and `(h+b-2)/2`, increasing in `b`, for
`b >= 1`.  Minimizing over live strata:

- `h` even: `b=0` gives `h/2`; the smallest live positive `b` is 2 (live for
  `h >= 4`), also giving `h/2`.  Minimum `= h/2`.
- `h` odd: the smallest live `b` is 1, giving `(h-1)/2`.

So the minimum is `floor(h/2)` in both parities, and it is *attained*, not
merely bounded.  Verified by exact Jacobian rank for `h = 1..14` and by
parity/degree census for `h = 1..100`: zero discrepancies.

R6's prose (0.5) says "at least `floor(h/2)`", which is correct but
understated; its own `RESULT.json` (`"minimum_codimension": "floor(h/2)"`)
and the Sol2 audit both state the exact form.  **The exact form is right and
should be the promoted one.**

## B.6 Constructibility and closure — CONFIRMED, with a precision

- **Constructible:** yes.  `phi_b` is a morphism from an irreducible
  variety (an open subset of `A^(b+r)`, only the discriminant condition being
  added), so the image is constructible by Chevalley.
- **Not closed, for `b >= 2`:** degenerating `B` to a non-squarefree limit
  drops the squarefree-part degree, so the limit leaves the stratum.
  Concretely at `h=8`, `B_s = X^2-s^2`, `v = X^2/5` gives
  `A_s = X^3 - (2/5)s^2 X` with `b(H_s)=2` for `s != 0`, while `s=0` gives
  `H_0 = X^8` with `b=0`.  Verified.  `S_0` and `S_1` are closed.
- **Closure codimension = stratum codimension**, since a constructible set
  and its Zariski closure have the same dimension.  So (0.4) and (0.5) are
  unaffected by which reading is used, and the Sol2 audit's insistence on the
  closure reading is the correct one.
- **Whether the *union* is closed I did not settle.**  I probed it hard:
  across `h = 4..16`, every live `b >= 2`, 40 random discriminant
  degenerations each, **every** boundary point was still a survivor (0
  non-survivors out of ~760).  So I found no evidence of non-closedness of
  the full locus.  Neither R6 nor I prove it either way; nothing in (0.4) or
  (0.5) depends on it.

## B.7 Degree eight and edge cases — CONFIRMED

`h=8`: parity gives `b in {0,2,4,6,8}` and `r = (10-3b)/2` gives
`r = 5,2,-1,-4,-7`, so exactly `b=0` (dim 4) and `b=2` (`r=2`, dim `2+2=4`)
survive, both codimension 4 in the 8-dimensional monic space; `b=4,6,8` are
degree-excluded.  Confirmed.

The `b=2` branch equals R5's cokernel equation: on 400 random
`(A of degree 3, B = z^2-D)`, the predicate `4a_0 + D a_2 = 0` agreed with
true solvability in **every** case, 0 mismatches.  My R5 review's field
caveat carries over unchanged — `D` lies in `K`, no base extension is needed
— and R6 inherits the sol-document phrasing "after base extension", which
remains harmless but imprecise.

Edge cases:

- **`h=1`:** `b=1`, `a=0`, `r=0`, `lc(v) = 1/(3/2) = 2/3`, `N_B(2/3) = 1 = A`.
  Every monic `X-c` is a survivor; dimension 1, codimension `0 = floor(1/2)`.
  Verified.  (Note `verify_r6.py` starts at `h=2` and never tests this.)
- **`h=2`:** only `b=0` is live (`b=2` needs `r=-1`).  The survivor locus is
  exactly the perfect squares: 9/9 of `(X-c)^2` survive, 0/9 of distinct-root
  quadratics do.  Dimension 1, codimension `1 = floor(2/2)`.  Verified.
- **shared-factor fixture:** `B=X`, `v=(2/5)X` gives `N_B(v) = X = A` and
  `H = X^3`, where `A = B`.  The canonical decomposition returns exactly this
  pair.  Any "repair" demanding `gcd(A,B)=1` would wrongly delete a genuine
  survivor.  Verified, as are the audit's other two fixtures
  (`B=X^2-3, v=X^2/5+2X-7 -> A = X^3+8X^2-(111/5)X-6` with `4a_0+3a_2=0`).

## B.8 `GAP/REPAIR`: the regression harness does not carry the theorem

`verify_r6.py` passes and writes nothing, but it is purely integer
bookkeeping.  Its `strata()` function *computes* `dimension = a+1` and
`codimension = h-a-1` and then asserts `dimension == a+1` — tautological.
The `codimension == (h+b-2)/2` and `min codim == h//2` assertions are real
but are one-line algebraic identities.  The harness tests **none** of the
mathematical content: not the uniqueness of `H=A^2B`, not injectivity, not
that the image has the claimed dimension, not sufficiency, not
constructibility, not the `4a_0+Da_2` equivalence, not a single polynomial.
It also covers only `h = 2..64`, omitting `h=1`.

This is non-blocking — the theorem is correct, and B.1–B.7 above supply the
checks the harness lacks — but the harness must not be cited as evidence for
the theorem.  **Recommended repair:** add the parametrization round-trip
(`(B,v) -> H -> (A,B) -> v`), an exact Jacobian-rank dimension check, and a
random-`(A,B)` solvability comparison, and extend the range down to `h=1`.

## B.9 Maximum promotion — item B

> **R6 may be promoted exactly as:** a complete normalized parameter
> compression of the **rational endpoint survivor locus**, conditional on R5
> at its promoted scope.  Over an algebraically closed characteristic-zero
> field, writing the unique monic `H = A^2 B` with `B` squarefree (valid even
> when `A` and `B` share factors), the survivors with `deg B = b >= 1` are
> exactly `H = N_B(v)^2 B`, `N_B(v) = Bv' + (3/2)B'v`, with `B` monic
> squarefree of degree `b`, `deg v = r = (h-3b+2)/2 >= 0`, and
> `lc(v) = 1/(r+(3/2)b)`; the map is injective, the image is constructible
> (and not closed for `b >= 2`), and the stratum has dimension `a+1` and
> closure codimension `(h+b-2)/2`.  Together with the `b=0` perfect-square
> stratum of codimension `h/2`, the full rational-endpoint survivor locus has
> codimension **exactly** `floor(h/2)`.  At `h=8` only `b=0` and `b=2`
> survive, each of dimension 4 and codimension 4, and the `b=2` branch is
> equivalent to R5's `4a_0 + D a_2 = 0`.
>
> **Nothing beyond that.** This is endpoint-survivor parameter compression
> only.  It is not a jet theorem and not a landing theorem: it does not show
> a survivor extends to a formal jet, does not construct a polynomial or
> source object, does not establish raw `2S/3S` provenance or GGV landing,
> does not exclude an `8_28` face or family, and yields no global
> automorphism, `G2-PSC`, `G2-BD`, cofinal degree bound, counterexample, or
> JC2.  It inherits R5's rollback and R5's conditionality on the weight-22
> normalization.  Its regression harness carries none of this and must not be
> cited as evidence.

---

# C. K00 V24R6R1 selected `D(W)` certificate — CONFIRMED

## C.1 Custody — CONFIRMED

All six charged hashes reproduce.  In addition:
`REVIEWED_BUNDLE_R6R1.sha256` replays **14/14** (from the repository root —
its paths are root-relative); `SOURCE_FREEZE_R6R1_LEADING_BASE_DW.sha256`
replays **14/14**; `SOURCE_FREEZE_R6R1_W_SYZYGY_REPLAY.sha256` replays
**13/13**; and `aws_box02_r6r1_unit/EVIDENCE.sha256` replays **26/26** after
rebasing only its frozen `/home/ubuntu/jobs/...box02` prefix.

I confirm the Sol-Ultra custody observation and can sharpen it: the harvest
directory holds 33 files, of which 26 are manifest entries; the seven
unlisted are `EVIDENCE.sha256` itself, `outer.stdout`, `outer.stderr`, and
the four later-added `independent_replay/*` files.  Both `outer.*` are empty
(`e3b0c442...b855`).  The manifest is declared non-exhaustive, so this is
hygiene, not a false claim, and `REVIEWED_BUNDLE_R6R1.sha256` now pins them.

## C.2 Fresh-process exact recomputation — CONFIRMED

I parsed the frozen sources with my own parser and recomputed in exact
rational arithmetic, using neither the producer's Python nor Singular:

```text
Q1..Q5  : 8, 11, 9, 12, 8 terms, all homogeneous of degree 2
Q6      : identically zero
F10     : 30 terms, homogeneous of degree 4
W       : 226 terms, homogeneous of degree 6
```

The eight serialized certificate slots have support exactly `{1,3,4,8}`:

```text
(c1, 0, c3, c4, 0, 0, 0, -1),
c1, c3, c4 : 15, 15, 60 terms, each exactly z^1 times a z-free degree-4 form.
```

and in `Q[x0,...,x5,z]`

```text
sum_i cert_i * gen_i = 1   exactly.
```

Slot 8 is `-1` and slot 6 is zero, as charged.  The `(Q1,...,Q5,F10,zW-1)`
ideal is therefore the unit ideal.

## C.3 Seven actual generators versus eight logical slots — CONFIRMED, with a precision

The `.sing` scripts declare

```text
ideal B = Q1,Q2,Q3,Q4,Q5,F10,z*W-1;      size(B) = 7,
```

so `Q6` is **not a member of the ideal at all** — it is not that Singular
silently drops it from a written list, it is simply never included, and the
script separately asserts `Q6 == 0`.  The serialization is
`(C[1..5], 0, C[6], C[7]) -> CERT_01..08`, so logical slots 1–5 map to actual
rows 1–5, slot 7 to actual row 6 (`F10`), slot 8 to actual row 7
(`z*W-1`).  I verified this mapping by direct multiplication against the
7-generator list: it gives exactly 1.

**Precision that must accompany promotion.** `CERT_06.txt` is *hard-coded*:
the producer script contains literally `write(".../LEADING_BASE_CERT_06.txt",0)`.
It is not a computed coefficient.  And because `Q6 = 0`, *any* value in that
slot would satisfy the identity equally.  So "the logical `Q6` coefficient is
zero" is a serialization convention with no mathematical content.  The
producer labels it honestly (`"Q6=0_LOGICAL_ONLY"`,
`"logical_q6_coefficient": "0"`) and the Sol-Ultra review calls it "literal
zero", but it must not be promoted as a *verified* fact.  Relatedly, since
slots 5, 6, 7 are all zero, the identity alone cannot pin *where* among them
the logical `Q6` slot sits — harmless, but worth knowing.

## C.4 Independent replay of `W = A1*Q1 + A3*Q3 + A4*Q4` — CONFIRMED

Each of `c1, c3, c4` is divisible by `z` with `z`-free quotient; dividing and
cancelling `z` is legitimate because `Q[x0..x5,z]` is an integral domain.
Setting `A_i = c_i/z` (equivalently `c_i|_(z=1)`, same thing here):

```text
A1*Q1 + A3*Q3 + A4*Q4 = W    exactly.
```

The three frozen `W_SYZYGY_A*.txt` files are term-for-term equal to my
`c_i/z`.  The grading is fully consistent: `deg A_i = 4`, `deg Q_i = 2`,
`deg W = 6`, so this is a graded syzygy in degree 6.  Equivalently

```text
c1*Q1 + c3*Q3 + c4*Q4 - (z*W-1) = 1 + z*(A1*Q1+A3*Q3+A4*Q4 - W) = 1,
```

so the unit identity is not a localization artifact.  Note also that `Q2`,
`Q5`, and `F10` carry zero coefficients: the conclusion needs only
`(Q1,Q3,Q4)`.  That ideal is proper (all generators are homogeneous of
degree 2, so it lies in `(x0,...,x5)` and its zero set contains the origin),
so the syzygy is genuine content, not a vacuous membership.

## C.5 Source maps and the 36-generator embedding — CONFIRMED

Let `phi : Q[x0..x5,z] -> Q[d0_1..d5_5, k10_0, k10_1, k10_2, zinv]` be the
ring homomorphism `x_i -> d_i_1`, `z -> zinv*k10_0`.  I verified
**coefficientwise** that every object declared in the embedding script is
exactly the `phi`-image of the corresponding frozen small object:

```text
Q1F..Q5F = phi(Q1..Q5),   F10F = phi(F10),   WF = phi(W),
CF[1],CF[2],CF[3],CF[4],CF[5],CF[35],CF[36] = phi(cert slots 1,2,3,4,5,7,8),
phi(z*W-1) = zinv*k10_0*phi(W) - 1 = P36.
```

So the 36-entry identity is the `phi`-image of the small identity, hence
`phi(1) = 1` automatically; I also confirmed it directly by multiplying out
over slots `{1..5, 35, 36}`.  Slots 6..34 carry coefficient zero, so
**whatever `P[6..34]` are, they cannot affect the identity** — and since a
sub-ideal is already the unit ideal, the conclusion is robust to any error in
the 29 generators I did not independently reconstruct.  The script's
`size(P)!=36` census and its three source-map guards cover exactly the seven
generators that matter.

**The characteristic change is load-bearing, and it holds.** The frozen V24
source `modular_prior_reduction_v24.sing` is over `F_65521`; the replay is
over `Q`.  I compared bytes: lines 2 and 3 (the 35 prior generators and the
localizer) are **byte-identical** (SHA-256 `986d96f1...` and `65755f35...`
respectively), and line 1 is identical after the single substitution
`ring R=65521,` -> `ring R=0,`.  Crucially I did not merely accept the
argument that the serialization is exact-rational — I *parsed* those bytes as
exact rationals and matched them against `phi` of the exact-`Q` V22/V23
sources.  So the char-0 reading is the genuine exact-`Q` lift.

## C.6 Preflight, mutations, and fail-closed structure — CONFIRMED

The preflight is correctly fail-closed and directly addresses the retained R6
erratum (Singular drops a literal zero generator; direct `lift(B,1)` on a
proper ideal errors rather than returning a typed branch).  It runs
`slimgb`, then `reduce(1,S)`, and only on `NF(1)==0` *and* `dim == -1` does it
declare `UNIT`; only then is direct `lift(B,ideal(1),U,"slimgb")` invoked,
with `U` checked to be `1` and the identity checked directly.  Every success
banner is reached only after all guards; there is no unconditional PASS.

I ran all three read-only `.sing` files in fresh local Singular processes from
`/tmp` (on copies; no repository file touched) and reproduce the frozen
stdout bytes exactly:

```text
e53b8ac0b9a046255b887bd0ae2a385990da93e9c26b55d676786533633f66d2  preflight  (PREFLIGHT=UNIT, DIM=-1)
60ed7462e541aedcdf20c79d3101b4ac9e676bc05fd1cc0aa9adc8384dcd9b12  small replay
8f8790c6f46979d8bf768b0ec7383e5275ba3d9b0be8448b033ad777931a79a0  full 36-generator replay
```

**Mutations: real but not discriminating.** Dropping `c1` and adding 1 to
`c1` both break the identity, in the producer run, in my Singular replays,
and in my Python recomputation.  But they are *forced* to break: the residual
changes by `-c1*Q1` and by `+Q1` respectively, both nonzero in an integral
domain.  They exercise the arithmetic path, not the claim.  This is a
non-blocking observation — the certificate is verified directly and exactly —
but the mutations should not be described as load-bearing evidence.

## C.7 Exactly what is proved, and what is not — CONFIRMED

With `I = (Q1,...,Q5,F10)` in `Q[x0,...,x5]`:

- `W in (Q1,Q3,Q4) subset I`, therefore `(I, zW-1) = (1)` and
  `(Q[x]/I)[1/W] = 0`.  **The selected leading-base/`F10` `D(W)` chart is
  empty.**
- Under `phi`, the exact-`Q` 36-generator V24 prior/localizer ideal is
  likewise the unit ideal, so **the normalized `D(k10_0*W)` prior-prefix
  chart is empty** — as a scheme, not merely on sampled points.
- **Adjoining `W=0` to the base ideal is redundant: CONFIRMED.**  `W in I`
  gives `I + (W) = I` identically.

The reason for the emptiness is worth stating plainly, because it changes how
the result should be used: **`W` vanishes identically on the whole base
scheme.**  `V(I)` is a nonempty cone (all generators are homogeneous with no
constant term, so it contains the origin) lying entirely inside `{W=0}`.  So
V23's selected "generic rank witness minor" is not generic on this stratum at
all — it is identically zero there.  This is a negative result about the
*chart selection*, not about the geometry of the stratum, and the entire
content of the V24 grade-seven question survives untouched on `W=0`.

Left open: `W=0` (which is everything), any other rank-five minor chart,
rank at most four, grades 7–19, a complete finite jet, an arc, K00 closure
incidence, order two, maximum twelve, and JC2.  The producer's firewall,
the Sol-Ultra review, and `ADJUDICATION_V24R6R1.md` all state this
accurately; I found no overreach in any of the three.  One wording note: the
producer's firewall paragraph does not explicitly mention *other minors*,
though the Sol-Ultra review and adjudication both do — the promotion sentence
should carry it.

**Consistency with the prior gate.** My earlier V24 hostile review
established that this same chart is empty *mod p* at 65521, 32003, 1000003,
and 2147483629, and set the next gate as exact-`Q` nonemptiness, to be
decided by "an exact-`Q` std ... or an explicit `1 = sum h_i g_i`
certificate".  R6R1 delivers precisely that certificate, and the answer is
the negative one.  By the terms of that gate, V22/V23/V24 are true and
vacuous on this chart, and the campaign needs a different stratum or a
genuine `W=0` analysis — not a longer ladder.  R6R1 is exactly the right
piece of work and its conclusion is correctly bounded.

## C.8 Maximum promotion — item C

> **V24R6R1 may be promoted exactly as:** an exact-`Q`, fully replayable
> emptiness certificate for two open charts.  In `Q[x0,...,x5]` the frozen
> V23 rank-five witness satisfies the graded syzygy
> `W = A1*Q1 + A3*Q3 + A4*Q4` with explicit degree-4 cofactors, so
> `W` lies in the reviewed V22 leading quadratic ideal; consequently
> `(Q1,...,Q5,F10,zW-1) = (1)` in `Q[x0,...,x5,z]`, the selected
> leading-base/`F10` `D(W)` chart is empty, and adjoining `W=0` to the base
> ideal is redundant.  Under the frozen substitution `x_i -> d_i_1`,
> `z -> zinv*k10_0` the exact-`Q` 36-generator V24 prior/localizer ideal is
> likewise the unit ideal, so the full normalized prior-prefix chart
> `D(k10_0*W)` is empty as a scheme.  Equivalently: the V24 conditional
> grade-seven rank-five theorem remains true but has **no source point on its
> selected Cramer chart**, and every possible survivor lies on `W=0`.
>
> **Nothing beyond that.** In particular this does not analyse the `W=0`
> locus — which is the entire base scheme, since `W` vanishes identically on
> it — and does not decide any other rank-five minor chart, rank at most
> four, grades 7 through 19, a complete finite jet, an arc, K00 closure
> incidence, order two, maximum twelve, or JC2.  The `Q6` slot value is a
> serialization convention, not a verified coefficient, and the drop/add
> mutations are engine checks rather than discriminating evidence; neither
> may be cited in support of the result.

---

# Consolidated findings

**Non-blocking corrections and precisions to carry into promotion**

1. (A) The D3 support is a self-declared `R0_ARTIFICIAL_CUSP_CONTROL`
   fixture; D5G's custody is over that fixture, and no statement about the
   real `8_28` face is licensed.
2. (A) The producer's internal dense specialization control uses a
   heavily-colliding structured assignment and is weak as an identity test;
   the symbolic replays (mine and Sol-Ultra's) are what settle the identity.
3. (A) The `D22 -> D22+H` mutation cannot fail; it demonstrates the
   blindness of `R22` to `H`-multiples but falsifies nothing.
4. (B) R6's prose bound "at least `floor(h/2)`" should be promoted in its
   exact form, "exactly `floor(h/2)`".
5. (B) `verify_r6.py` is tautological integer bookkeeping and tests none of
   the geometry; it must not be cited as evidence.  Repair suggested in B.8.
6. (B) The charge's path label `FREEZE.md` should read `FREEZE.sha256`.
7. (C) `LEADING_BASE_CERT_06.txt` is hard-coded, and any value would satisfy
   the identity since `Q6 = 0`; it is a convention, not a verified fact.
8. (C) The drop/add mutations are forced to break and are engine checks only.
9. (C) The producer firewall should explicitly name *other rank-five minor
   charts* among the things left open, as the review and adjudication do.

**Nothing found that blocks any of the three promotions.**  I attempted, and
failed, to break: the recurrence signs and shifts, the polygon census and the
weight-22 truncation, the provenance records and digests, the `D0`
cancellation, both endpoint decompositions and their uniqueness, all four
deltas, D4R1 leakage into any frozen number, the `A^2B` decomposition under
shared factors, injectivity and sufficiency of the `(B,v)` parametrization,
every stratum dimension by exact Jacobian rank, the exact codimension in both
parities and at `h = 1, 2, 8`, closedness of the survivor union, the
certificate identity, the `z`-cancellation, the seven-versus-eight slot
alignment, the char-65521-to-char-0 lift, and the robustness of the embedded
identity to the 29 generators I did not reconstruct.

## Scope firewall for this review

This review promotes nothing beyond the three boxed sentences in A.10, B.9,
and C.8.  It does not establish a local/global naturality square, a Keller
specialization or Keller pair, an `8_28` face or family exclusion, a formal
jet or arc, K00 closure incidence, a GGV landing theorem, `G2-PSC`, `G2-BD`,
a cofinal degree bound, a counterexample, or JC2.  It does not promote R5,
D3, D4R1, V22, V23, or V24 beyond their own separately reviewed ceilings; it
consumes R5 only at its already-confirmed endpoint scope, and it treats
D4R1's freeze as a lifecycle hold exactly as D5G does.
