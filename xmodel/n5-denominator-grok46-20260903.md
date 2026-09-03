# N5: `den(δ) ≤ u_s` for a principal-minor split

Lane `n5-denominator-grok46-20260903`.  FALLACY-v2.  No ledger, `jc2-lean`,
`ideation-*`, or named in-progress reports were edited.

## Verdict first

**N5 is PROVED.**  Xu p.13 asserts “the denominator of order `δ ≤ u_s = 3`”
with no exhibited proof.  The missing step is the Puiseux Galois action on
the degree-`u_s` leading polynomial of Prop. 7.3: a genuine split of order
`δ = p/e` in lowest terms produces a `μ_e`-orbit of nonzero `π`-roots of
size `e`, which cannot embed in `deg p = u_s` if `e > u_s`.  Hence

```text
den(δ) = e ≤ u_s.
```

The bound is `≤`, not “divides”: `δ = 5/2` has `e = 2`, `u_s = 3`, and
`2 ∤ 3`, with Galois-stable `p = π(π² − c)`.  Promoting N5 to `e | u_s`
would be a false strengthening and would kill a surviving branch.

The split-order classification `δ ∈ {2, 5/2}` is therefore **complete**
inside the detector window `(1, 8/3)`, and the `(99,66)` decider is
exhaustive over the two surviving split branches `{2 [2,1], 5/2 [1,1,1]}`.
Partition `[3]` is unsplit (Moh’s linear-power alternative) and is outside
this classification.  Nothing here is a Keller witness; both surviving
faces remain `OPEN` as global lifts.

`MECHANICAL-CHECK`: PASS.  Manifest generated with `awk` from the
`charged_input_<i>_sha256=` / `charged_input_<i>_basename=` lines of
`xmodel/n5-denominator-grok46-20260903.run.v2`, checked with
`sha256sum -c`.  All eight frozen inputs `OK`.  No digest was retyped.
Manifest: `box/n5-20260903/inputs.sha256`.

No new exit-price assertion, so no `charge_basis` line.

## 0. Pages opened

Printed Moh page `p` is PDF page `p−139`.  Xu printed page `p` is PDF page
`p`.  Images at 200 dpi in `box/n5-20260903/pages/`:

| content | printed | image |
|---|---|---|
| Moh minor-disc dichotomy, Prop. 6.1 statement | 190 | `moh_p190_pdf51.png` |
| Prop. 6.1 proof, order identity | 191–193 | `moh_p191_pdf52.png`–`moh_p193_pdf54.png` |
| two-point leading form; minor jet through order `<1` | 194 | `moh_p194_pdf55.png` |
| p.202 table | 202 | `moh_p202_pdf63.png` |
| `(64,48)` / `u_s=1`; Appendix II start | 207 | `moh_p207_pdf68.png` |
| `(99,66)` p.209 probe | 209 | `moh_p209_pdf70.png` |
| `(15,10)` descent; `2,2,6` of `f` in `D_2` | 210 | `moh_p210_pdf71.png` |
| Xu `(75,50)` / `(84,56)` | 8–9 | `xu_p8_pdf8.png`, `xu_p9_pdf9.png` |
| Xu §7.3, Prop. 7.3, Cor. 7.5 | 10–12 | `xu_p10_pdf10.png`–`xu_p12_pdf12.png` |
| Xu §8, the denominator sentence | 13 | `xu_p13_pdf13.png` |

Moh p.201 (Galois automorphism of major discs) is quoted from the charged
`moh_skeleton_full.py` header, which transcribes it from the same frozen PDF.

## 1. SOURCE-READ

`SOURCE-READ`, Moh p.194.  Highest form
`[(y−ax)^{v_s}(y−bx)^{u_s}]^{n/d_s}`, `a ≠ b`, `u_s = d_s − v_s`.  The
principal minor packet is the `u_s`-fold factor.  In the top minor disc
`D^*_{s−1}` every such root has the **common integral jet** (9)

```text
y = b t^{-1} + e + c† t + higher,     e common to the packet.
```

Prop. 6.1 gives only `δ^* ≥ 1` (p.193: “does not specify” the radius).
At `(99,66)` the p.190 minor test reads `V_r = u_s = 3`, not table `V_3 = 8`.

`SOURCE-READ`, Xu §7.3 p.10.  Principal-minor multiplicity of `f` is
`m u_s/d_s`; of `T_0,…,T_{s−1}` is `(−μ_i) u_s/d_s`; of `T_s` is
`(−μ_s−2)u_s/d_s + 1`.  Prop. 7.3: the order-1 `π`-root `σ_1` of this
packet has all leading polynomials powers of one linear factor, and the
proof (p.10) writes `deg p(π) = u_s`, then claims `p = (π−a)^{u_s}`.

`SOURCE-READ`, Xu p.13: “Our tools are two constrains: one is that the
denominator of order `δ ≤ u_s = 3`; another is equation 7.1.”  No proof
of the first tool appears in §7.3, Prop. 7.3, Cor. 7.5, or §8.
“If `δ` splits, it must split to 2 or 3 roots” is stated as a corollary
of that bound plus `deg p = 3`.

`SOURCE-READ`, Moh p.201 (charged skeleton transcription):
`t̄^{L A_{r−1}} = t` and the automorphism `t̄ ↦ ω t̄` of
`k⟨⟨t̄⟩⟩` over `k⟨⟨t̄^{A_{r−1}}⟩⟩`, `ω` an `A_{r−1}`-st root of unity.
That is the major-disc instance of the same `μ_e` action.

## 2. Lemma

**Lemma N5.**  Let `K` be algebraically closed of characteristic 0.  Let
`(f,g)` be a Jacobian pair, monic in `y`, with two points at infinity, in
the setting of Xu §7.3.  Let `σ` be a **split** principal-minor `π`-root
of order `δ`, with leading polynomial `p` of degree `u_s` (Prop. 7.3).
Then `den(δ) ≤ u_s`.  The same bound holds for any later split of a
sub-packet of multiplicity `mm`, with `u_s` replaced by `mm`.

**Proof.**  Write `t = x^{-1}`.  Prop. 7.3 plus Moh (9) give a common
jet with **integer** exponents through order 1.  While the cluster is
unsplit, a common coefficient of a fractional power `t^{r/e}` would have
to be `μ_e`-invariant, hence zero or the exponent integral.  So the first
possibly fractional exponent is the first split order `δ > 1`.

Write `δ = p/e` in lowest terms.  The expansions live in `K((τ))` with
`t = τ^e`.  The Galois automorphism `τ ↦ ζ_e τ` sends
`σ = (jet_{<δ}) + π t^δ + ⋯` to a conjugate with `π ↦ ζ_e^{p} π`.
Since `gcd(p,e) = 1`, nonzero `π`-roots form orbits of size `e`; the
origin is the unique fixed point.  These orbits embed in the root
multiset of `p`, of degree `u_s`.  A genuine split is not all-at-`0`.
Hence `e ≤` (number of distinct nonzero roots) `≤ u_s`, i.e.
`den(δ) ≤ u_s`.

If the packet later splits, the child leading polynomial has degree
`mm ≤ u_s` (Xu §8(iii): `deg p = 2` on the double packet).  The same
orbit count gives `den(δ') ≤ mm ≤ u_s`.

**What Xu does not print.**  The `μ_e` action itself.  Characteristic 0
and the Puiseux field are Xu p.1; `deg p = u_s` is Prop. 7.3.  The
automorphism is the minor-place analogue of Moh p.201.  No extra
geometric hypothesis is required.  The `(99,66)` skeleton satisfies
§7.3: two points, monic, `s = 3 > 2`, `u_s = 3 < v_s = 8`.

**Not proved:** `e | u_s`.  Witness `δ = 5/2`, `p = π(π²−c)`, `c ≠ 0`.

## 3. Sanity

Driver, against charged `MOH_TABLE` arithmetic.

| row | `u_s` | principal `#f` | N5 at the principal place | known tree |
|---|---:|---:|---|---|
| `(64,48)` | 1 | 12 | `deg p = 1` ⇒ `den = 1`, unramified, no split of `p` | single series; Prop. 6.4 pins `δ^* = v_s/u_s = 3` |
| `(75,50)` `V_2=3` | 1 | 10 | same: principal N5 vacuous | see below |
| `(99,66)` | 3 | 18 | `den ≤ 3` | `{2 [2,1], 5/2 [1,1,1]}` |

`(75,50)` `V_2=3`, `m/d_2 = 2`.  Moh p.210, after Prop. 6.3 descent to
`(n,m,M_2,V_2) = (15,10,11,3)`: “in the major disc `D_2` there are
precisely three subdiscs which contains 2, 2, 6 of roots `f` respectively.
The datum `δ_1 = 1/2`…”.  Cluster sizes `2,2,6` are even, hence
`μ_2`-stable for `den(δ_1) = A_1 = 2`.  That is the **major-disc**
analogue of N5 at the descended place, not the original principal-minor
bound (`u_s` remains 1).  `FALLACY-v2 / flag-place-series`: major `A_1`
is not identified with principal-minor `den(δ)`.

A naive “`den ≤` multiplicity” bound is false for major discs: Xu’s
`(75,50)` `V_2=2` display has `δ_2 = 1/5` and factors `π^5 − c_i`, so
`den = 5 > V_2`.  N5 uses `deg p = u_s` at the **principal-minor** place.

## 4. Classification at `(99,66)`

Window: `1 < δ < v_s/u_s = 8/3` (Xu Prop. 7.3; detector ceiling from
Prop. 6.1’s order identity `ord g = 9(3δ−8)`).  Reduced fractions with
`den ≤ 3`: `4/3, 3/2, 5/3, 2, 7/3, 5/2`.

Face ODE, Xu (7.1), `p' = d/dπ`, `deg p = 3`, `deg q = 40`:

```text
9 a q p' − b q' p = 45 p^{14},   a = 40δ−105,  b = 27δ−72.
```

Xu’s printed iterate `q = p^{13}(π−c)` has nonzero residual at every
window `δ` (driver, test cubic `(π−1)(π+1)(π−2)`).  The resonance
budget (`r = 13 mm + 1` or `r = ρ mm`, `ρ = 5(8δ−21)/(3δ−8)`,
`Σ r ≤ 40`) plus Galois:

| `δ` | ODE split survivors | Galois |
|---|---|---|
| `4/3, 3/2, 5/3, 7/3` | none | — |
| `2` | only `[2,1]` vector `(25,14)` | `e=1`, allowed |
| `5/2` | `[1,1,1]` and `[2,1]` | `μ_2` kills `[2,1]`; keeps `p=π(π²−c)` |

Charged faces have residual `0`: `δ=2`,
`p=π²(π+3a)`, `q=π^{25}(π+3a)^{14}(π−2a)`; `δ=5/2`, `q = p^{10} q_1`
with `q_1' = 10 p^3`.  Alive means a face solution, never a Keller pair.

Without N5, ODE alone admits further rows in `(1,8/3)` with `den>3`
(`9/4, 13/5, 17/7, …`; driver, `den≤30`).  All have `e>3` and are
Galois-killed.  So N5 is load-bearing for Xu’s printed tool, and
redundant with Galois for the classification.

## 5. Typed scope

```text
PROVED[N5]                 den(δ) ≤ u_s for a genuine principal-minor split
NOT[N5-DIVIDES]            e | u_s is false (witness 5/2)
PROVED[SUBCLUSTER]         den ≤ mm ≤ u_s on any child packet
COMPLETE[9966-SPLIT-ORDERS] δ ∈ {2, 5/2} inside (1, 8/3)
EXHAUSTIVE[9966-SPLIT-DECIDER] branches {2 [2,1], 5/2 [1,1,1]}
OPEN[9966-DELTA-2-BRANCH-B]  face a point mod gauge; lift unproved
OPEN[9966-DELTA-52-BRANCH]   face 1-parameter; lift unproved
```

N6 of the charged source review stands, now with N5 typed `PROVED`
rather than `SOURCE-ASSERTED`.

## 6. FALLACY-v2

Flag/place/series: major radii `(4/9,1/3,−1)`, split order `δ`, combined
`δ^*`, and major increment denominators `A_j` are not identified; §3
separates the `(75,50)` major `2,2,6` from principal-minor N5.
Floor/attainment: `den ≤ u_s` is an upper bound on the denominator, not
attainment of a split; `e=3` is allowed by Galois and killed by the ODE,
not by N5.  Carrier/attainment: face residuals `0` are
`REPRESENTATIVE[FACE-ODE]`, not `FULL_ACTUAL_EXIT`.  Prime mark:
`p',q'` are `d/dπ`.  Raw remainder degree: the `deg q=40` budget keeps
resonant and non-resonant branches.  No `sat()`.  No exit-price
assertion.

## 7. Reproduction

```text
python3 box/n5-20260903/n5_driver.py > box/n5-20260903/results.json
```

Python 3, SymPy 1.12; under 5 s; no Singular.  Artifacts:
`box/n5-20260903/{n5_driver.py,results.json,inputs.sha256,artifacts.sha256,pages/}`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10050`.
- Body SHA-256:
  `bd002fa473d366fc3592caf193003d58eadb6a823ce8f7dd9a12b5e13177438f`.
- Frozen basis: `816102f31ab5f894600338fccd02de0f7e59f766`.
