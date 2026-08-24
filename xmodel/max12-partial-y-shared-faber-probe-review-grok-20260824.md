# Hostile different-model review — shared maximum-12 Faber compiler

| Field | Value |
|---|---|
| Claim under review | Frozen producer shared high-row Faber compiler: over a characteristic-zero differential field, every monic depressed pair of degrees `(m,n)` with `deg_z D<=m-2` has a unique Faber form `g=sum h_j F_j` with all `h_j` differential constants; the remaining Laurent system is `r_1'=...=r_(m-2)'=0`, `m r_(m-1)'=j/u`; both maximum-twelve cells have all eleven high rows reconstructed; after character filters and the three legal target translations the quotient widths are `7,10,16` and `9,17`; the two-row ranks are local controls only; aggregate route-cost may allocate `(9,12)` next, with no overall cheaper-cell theorem |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking: `t_m=0` identically in both inverse series, so `len(z(w))=13` rather than `14`; the `n+1` truncation is still necessary for `r_2`. The preflight's own hostile review had not landed at producer freeze; the Kummer orders used here were re-derived from the reviewed history rather than imported as a reviewed preflight theorem) |
| Evidence tier | independent formal-Laurent derivation of uniqueness, the fixed-`w` identity including sign, `A_ell`, `det=m^(m-1)`, and `P->P+q`; independent exact reconstruction of both cells (Newton/`w`-product Faber, not the producer `binom(j/m,k)` loop) verifying all eleven high rows, both first two integrated rows, binomial cutoff, support totals, every per-branch `r_1,r_2` digest at two test points, and `n+1` necessity for `r_2`; unmodified producer replay as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `7832fb73ac887041968f9cec2dc6cba7aa0d0bcf` (descendant of the charged basis `1e60fcedc8626650c7c7544ad296c3624173415f`; named producer artifacts remain uncommitted) |
| Review window (UTC) | 2026-08-24T18:05:39Z – 2026-08-24T18:26:00Z |
| Python | CPython 3.14.6, stdlib only (registered replay and independent reconstruction) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, freeze, pinned preflight, and reviewed history pair reread in full before any verdict:

- `xmodel/max12-partial-y-shared-faber-probe-20260824.md` (SHA-256 `d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036`)
- `cases/max12_high_row_probe_20260824/REGISTRATION.md` (SHA-256 `1ba83d340efa28ca6d24237e97065253571ee94774a273a80ed83c4593de2d91`)
- `cases/max12_high_row_probe_20260824/shared_faber_probe.py` (SHA-256 `69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f`)
- `cases/max12_high_row_probe_20260824/MANIFEST.sha256` (SHA-256 `0b086f312627b81fcc09a884681ca31b0c88ed95151556b5d751b68dd20f3882`)
- `cases/max12_high_row_probe_20260824/FREEZE.sha256` (SHA-256 `3a25edb31a53ecee9c96e039ab4a947908ebc0542123fb131447e1a661f45a28`)
- `xmodel/max12-partial-y-kummer-preflight-20260824.md` (SHA-256 `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07`)
- `cases/max12_partial_y_preflight_20260824/FREEZE.sha256` (SHA-256 `59ef0712aea2424ea57b6f1727031018e769701b0f2e2384eb4638f4286ea558`)
- `xmodel/as109-partial-y-history-stop-20260824.md` (SHA-256 `6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe`)
- `xmodel/as109-partial-y-history-review-grok-20260824.md` (SHA-256 `f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd`)

The charged basis named by the prompt is `1e60fcedc8626650c7c7544ad296c3624173415f`. Named producer artifacts remain uncommitted on top of that basis. No producer, case, canonical, ladder, coordination, prompt, log, or run file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp`.

The universal differential-field identities were re-derived and were not imported from a `(6,9)` coefficient expansion. The preflight is consumed only for the residual Kummer-order list of the two primitive maximum-twelve cells; those orders were re-derived from the reviewed shear/UFD history. The preflight's own hostile review is not treated as landed.

---

## Promotion

**Accept `COMPLETE UNIVERSAL HIGH-ROW FABER INTEGRATION; BOTH MAXIMUM-TWELVE CELLS HAVE ALL ELEVEN HIGH ROWS IN FABER FORM; QUOTIENT WIDTHS `7,10,16` AND `9,17`; TWO-ROW LOCAL WIDTHS `5,8,14` AND `7,15`; AGGREGATE ROUTE-COST MAY ALLOCATE `(9,12)` NEXT` at the stated scopes.**

- For a characteristic-zero differential field `K` and monic depressed `f` of degree `m`, the monic formal root `w=f^{1/m}=z+O(z^{-1})` exists uniquely in `K((z^{-1}))`. The polynomials `F_j=[w^j]_+` are monic of degree `j` and strictly triangular, so a monic `g` of degree `n` has a unique expansion `g=sum_{j=0}^n h_j F_j` with `h_n=1`.
- Differentiation at fixed `w` gives the exact identity `D=-f_z(partial_x g)|_w=-f_z sum h_j' w^j+f_z sum r_ell' w^{-ell}`. The terminal Laurent term occurs with a plus sign relative to the series `H(w)-g(z(w))=sum r_ell w^{-ell}`. The opposite sign is false. If `deg_z D<=m-2`, descending triangularity in degrees `m-1+j` forces every `h_j'=0`. After the licensed harmless constant extension, these constants are scalars of the Kummer root field.
- `A_ell=[f_z w^{-ell}]_+` has leading term `m z^{m-1-ell}` for `1<=ell<=m-1` and vanishes for `ell>=m`, with `A_{m-1}=m`. The matrix on `(r_1',...,r_{m-1}')` is triangular of determinant `m^{m-1}`. The chain rule `J_{(x,y)}=u D=j` yields the positive terminal system `r_1'=...=r_(m-2)'=0`, `m r_(m-1)'=j/u`.
- Both cells reconstruct exactly. The first two integrated rows are `b_{10}=(3/2)a_6+c_{10}`, `b_9=(3/2)a_5+(11/8)delta0 a_6+c_9` on `(8,12)` and `b_{10}=(4/3)a_7+c_{10}`, `b_9=(4/3)a_6+(11/9)delta0 a_7+c_9` on `(9,12)`. All eleven high Jacobian rows vanish. Support totals are `242` in either cell, with largest single support `64` and `66`.
- Reversion `f(z(w))=w^m` through `w^{-(n+1)}` is necessary and sufficient for `r_2`. Every per-branch digest matches. Rank two at two rational test points is a local independence control, not a component dimension.
- For `n<2m`, `P->P+q` acts by `h_{k,new}=h_k-((k+m)/m)h_{k+m}q` on `0<=k<=n-m` and slices `h_{n-m}`. Together with `Q->Q-h_m P` and `Q->Q-h_0` the three indices `(m,0,n-m)` are distinct and character-compatible: `(8,12)` uses `8,0,4`; `(9,12)` uses `9,0,3`.
- High-row quotient widths are `7,10,16` and `9,17`. Two-row local widths are `5,8,14` and `7,15`. Aggregates `33` versus `26` and `27` versus `22` license a speed allocation of `(9,12)` next. They do not license an overall simpler-cell theorem. The widest single branch remains `16` versus `17`, favouring `(8,12)` under a different cost rule.
- Both complete Taylor-boundary families remain charged.

**Do not promote this to:** a lower-fibre component classification; a rational or polynomial trajectory; emptiness of either maximum-twelve frontier; maximum-twelve automorphy; a counterexample; or JC2.

**Smallest valid successor.** A lower-fibre / remaining-Laurent probe on `(9,12)`, retaining the order-four `(8,12)` leaf as the cheapest control, without converting the aggregate width comparison into a complexity theorem. Reconstruct both original Taylor jets at every step. Do not open a generic coefficient rectangle or AWS.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a characteristic-zero Keller pair of type `(8,12)` or `(9,12)`, classifies a lower invariant fibre, produces a rational trajectory, or empties either frontier. Producer string `PASS-MAX12-SHARED-HIGH-ROW-PROBE` was not used as evidence; the Faber basis, the fixed-`w` identity, the terminal triangle, the eleven high rows, the two Laurent rows, the target quotient, and the widths were re-derived. Two-row test ranks are local. Summing widths across Kummer leaves is an engineering cost, not an algebraic dimension. The reviewed partial-`y` history stop is consumed only for the residual criterion that isolates `(8,12)` with `4|H` and `(9,12)` with `3|H`; it does not license maximum-twelve automorphy.

---

## Scope (not enlarged)

Universal high-row Faber integration over a characteristic-zero differential field; exact specializations of all eleven high rows in both primitive maximum-twelve cells; character/target quotient widths; a bounded `r_1,r_2` control. Lower Laurent fibres `r_ell` for `ell>=3`, algebraic components of those fibres, either original Taylor-boundary family, emptiness, maximum-twelve coverage, and JC2 remain out of scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | For monic depressed `f` of degree `m` over a characteristic-zero field, `w=f^{1/m}` exists uniquely as a monic formal Laurent series at infinity, `F_j=[w^j]_+` are monic of degree `j` and unitriangular, and a monic `g` of degree `n` has a unique expansion `g=sum_{j=0}^n h_j F_j` with `h_n=1` | **CONFIRMED** | a `z^{j-1}` term in `F_j`; non-existence or non-uniqueness of the monic root in `K((z^{-1}))`; binomial coefficients leaving `Q`; an expansion that required `h_n≠1` |
| 2 | At fixed `w`, `D=-f_z(partial_x g)|_w=-f_z sum h_j' w^j+f_z sum r_ell' w^{-ell}`. The plus sign on the tail is forced by `H(w)-g=sum r_ell w^{-ell}`. If `deg_z D<=m-2`, descending triangularity of `f_z w^j` (leading term `m z^{m-1+j}`) kills every `h_j'`. After the licensed scalar extension, constants of the Kummer root field are the scalars | **CONFIRMED** | opposite sign matching the identity; leftover mixing of a higher `j` into degree `m-1+j`; `deg D<=m-2` failing to constrain `h_0'`; constants of `k(x)(u)` larger than the licensed scalars |
| 3 | `A_ell` has leading term `m z^{m-1-ell}` for `1<=ell<=m-1`, vanishes for `ell>=m`, and `A_{m-1}=m`. Determinant `m^{m-1}`. Chain rule `J_{(x,y)}=uD=j` gives the positive system `r_1'=...=r_(m-2)'=0`, `m r_(m-1)'=j/u` | **CONFIRMED** | a nonnegative part of `A_ell` for some `ell>=m`; `A_{m-1}≠m`; `det≠m^{m-1}`; Jacobian factor `u` of the wrong sign; constant row `-m r_{m-1}'=j/u` |
| 4 | First two rows reconstruct exactly as displayed. All eleven high rows `z^{17}..z^7` and `z^{18}..z^8` vanish along every `a_i`. Finite binomial cutoff `k<=j/2` is sharp. Support totals `242`/`242`, maxima `64`/`66` | **CONFIRMED** | a different `b_{10}` or `b_9`; a nonzero high Jacobian coefficient; a polynomial contribution from `k>j/2`; support totals other than `242` |
| 5 | Inverse `z(w)` through `w^{-(n+1)}` is necessary for `r_2` and unnecessary for `r_1`. All ten per-branch digests match. Rank `2` at two rational points is a local control only | **CONFIRMED** | a digest mismatch or a printed failing polynomial; `t_{n+1}` dropping out of `r_2`; a global component dimension inferred from the test rank |
| 6 | For `n<2m`, `P->P+q` acts by `h_k |-> h_k-((k+m)/m)h_{k+m}q` and slices `h_{n-m}`. The three gauges `(h_m,h_0,h_{n-m})` are legal, independent, and `0 mod e` for every live Kummer order. Remaining constant indices are exactly the displayed lists | **CONFIRMED** | `g` not invariant under the displayed action; opposite sign on `q`; a gauge collision; a surviving constant of weight not `0 mod e`; `n>=2m` used as if the action stayed finite |
| 7 | Widths `7,10,16` and `9,17`; local widths `5,8,14` and `7,15`; aggregates `33` vs `26` and `27` vs `22`. Speed allocation of `(9,12)` is licensed only as that heuristic. No overall simpler-cell theorem | **CONFIRMED** | a width change; treating the aggregate as a dimension; promoting `(9,12)` as mathematically simpler; ignoring that the widest branch favours `(8,12)` |
| 8 | Both complete Taylor-boundary families remain charged. No lower-fibre classification, rational trajectory, emptiness, maximum-twelve automorphy, counterexample, or JC2 is licensed | **CONFIRMED** | a hidden discharge of (1.1); a component of `r_ell` classified; a frontier declared empty; a JC2 sentence |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Replay and hashes

Frozen hashes, recomputed on the charged tree, match the launch prompt, `MANIFEST.sha256`, and `FREEZE.sha256`:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/max12-partial-y-shared-faber-probe-20260824.md` | `d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036` | prompt, `MANIFEST`, `FREEZE` |
| `cases/max12_high_row_probe_20260824/REGISTRATION.md` | `1ba83d340efa28ca6d24237e97065253571ee94774a273a80ed83c4593de2d91` | prompt, `MANIFEST`, `FREEZE` |
| `cases/max12_high_row_probe_20260824/shared_faber_probe.py` | `69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f` | prompt, `MANIFEST`, `FREEZE` |
| `cases/max12_high_row_probe_20260824/MANIFEST.sha256` | `0b086f312627b81fcc09a884681ca31b0c88ed95151556b5d751b68dd20f3882` | prompt, `FREEZE` (self-hash) |
| `cases/max12_high_row_probe_20260824/FREEZE.sha256` | `3a25edb31a53ecee9c96e039ab4a947908ebc0542123fb131447e1a661f45a28` | prompt (self-hash) |
| Canonical JSON payload | `abbd72dc33aecd86d648696c138bcf5c919db6781a30447223fd184492d66a2d` | prompt, registration |

Pinned inputs, recomputed independently of the producer printout:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/as109-partial-y-history-stop-20260824.md` | `6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe` | residual criterion |
| `xmodel/as109-partial-y-history-review-grok-20260824.md` | `f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd` | different-model confirmation of that history |
| `xmodel/max12-partial-y-kummer-preflight-20260824.md` | `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07` | Kummer-order list, charged boundaries |
| `cases/max12_partial_y_preflight_20260824/FREEZE.sha256` | `59ef0712aea2424ea57b6f1727031018e769701b0f2e2384eb4638f4286ea558` | preflight freeze |

The case directory contains exactly those four files plus `FREEZE.sha256`. No enumerator, exponent rectangle, or AWS helper is present.

Registered commands, rerun unmodified from the repository root:

```sh
shasum -a 256 -c cases/max12_high_row_probe_20260824/FREEZE.sha256
python3 cases/max12_high_row_probe_20260824/shared_faber_probe.py
```

The freeze check is `OK` on every named path. The replay exits 0. Exact terminal lines:

```text
PASS-MAX12-SHARED-HIGH-ROW-PROBE
frontier_8_12_quotient_widths=7,10,16
frontier_9_12_quotient_widths=9,17
all_high_rows=EXACT_FABER
speed_allocation_by_aggregate_width=(9,12)
overall_cheaper_cell=NOT_CLAIMED
payload_sha256=abbd72dc33aecd86d648696c138bcf5c919db6781a30447223fd184492d66a2d
```

Those PASS strings are regression only. The independent reconstruction of Claims 1–8 is the evidence.

Independent reconstruction, second derivation for every load-bearing finite identity: unitriangular Faber bases and the fixed-`w` identity on `(m,n)=(3,4),(3,5),(4,5),(4,7)`; `A_ell` leading terms, vanishing boundary, `A_{m-1}=m`, and `det=m^{m-1}` (`9` and `64`); `P->P+q` invariance of `g`; Newton/`w`-product reconstruction of every `F_j` on both maximum-twelve cells matching the binomial form; vanishing of all eleven high rows; both first two integrated rows; every per-branch `r_1,r_2` digest; rank `2` at the producer point and at the alternate point `(3i+7)`; `n+1` necessity for `r_2` only.

---

## Claim 1 — Faber basis and uniqueness

**CONFIRMED.**

Let `K` be a field of characteristic zero. Let

```text
f=z^m+a_(m-2)z^(m-2)+...+a_0 ∈ K[z]
```

be monic and depressed. In the formal neighbourhood of infinity write `U=sum_{i=0}^{m-2} a_i z^{i-m} ∈ z^{-2}K[z^{-1}]`, so `f=z^m(1+U)`. The binomial series

```text
(1+U)^{1/m}=sum_{k>=0} binom(1/m,k) U^k
```

lies in `1+z^{-2}K[[z^{-1}]]` because every binomial coefficient is in `Q subset K` and `U` has valuation at least `2`. Thus

```text
w=z(1+U)^{1/m}
```

is the unique element of `K((z^{-1}))` with `w^m=f` and `w=z+O(z^{-1})`. Depression is used only to kill the constant term in `w-z`; uniqueness of the monic root does not need it, but the later leading-term calculus does.

Then `w^j=z^j(1+U)^{j/m}`. The highest term of `U^k` has degree `-2k`, so `z^j U^k` can meet the nonnegative `z`-axis only for `k<=j/2`. The polynomial part `F_j=[w^j]_+` is therefore a finite sum, monic of degree `j`, and (because `U` has no `z^{-1}` term) has vanishing `z^{j-1}` coefficient. In the monomial basis `(z^n,...,z^0)` the matrix of `(F_n,...,F_0)` is unitriangular, hence invertible over `K`. Every polynomial of degree at most `n`, and in particular every monic `g` of degree `n`, has a unique expansion `g=sum_{j=0}^n h_j F_j` with `h_n=1`.

The same unitriangularity was checked on the four small pairs `(3,4),(3,5),(4,5),(4,7)` and, by an independent Newton-then-product construction of `w^j`, on both maximum-twelve cells. Extra binomial index `k=j/2+1` contributes no nonnegative `z`-power.

Hypotheses that are actually used: characteristic zero (for `1/m` and the binomial series); the formal Laurent field `K((z^{-1}))`; monicity of `f` (to have `w∼z`); depression (to have `w=z+O(z^{-1})` rather than `w=z+a_{m-1}/m+O(z^{-1})`). No convergence in the analytic topology is required.

---

## Claim 2 — differential identity and sign

**CONFIRMED.**

Write `H(T)=sum_{j=0}^n h_j T^j` and define the negative tail in `w` by

```text
H(w)-g(z(w))=sum_{ell>=1} r_ell w^{-ell}.
```

The polynomial `g` is a function of `(x,z)`. The inverse `z=z(x,w)` is cut out by `f(z,x)=w^m`. Differentiating `f` at fixed `w` gives `z_x|_w=-f_x/f_z`, hence

```text
(partial_x g)|_w=g_z z_x|_w+g_x=(f_z g_x-f_x g_z)/f_z=-D/f_z,
```

so `D=-f_z(partial_x g)|_w`. This is the chain-rule identity at fixed `w`, not at fixed `z`. At fixed `z` one would obtain only `g_x`, and the identity would be false.

Along the same slice, `g(z(x,w),x)=H(w)-sum r_ell w^{-ell}` with `w` held fixed, so

```text
(partial_x g)|_w=sum h_j' w^j-sum r_ell' w^{-ell}.
```

Substitution produces the displayed formula with a **plus** sign on the tail. The opposite sign `-f_z sum h_j' w^j-f_z sum r_ell' w^{-ell}` fails already on `(m,n)=(3,4)` as a series identity in `z` (nonzero discrepancy in degrees `-4,-3,-2,0,1`). The nonnegative `w`-powers of `H(w)-g(z(w))` vanish identically, which pins the series definition of `r_ell` rather than its negative.

The second sum, rewritten in `z`, has polynomial part of degree at most `m-2` (Claim 3). In the first sum, `[f_z w^j]_+` has leading term `m z^{m-1+j}`. If some `h_j'` is nonzero, the largest such `j` produces a unique highest degree `m-1+j>=m-1`, which cannot cancel against the tail or against a smaller index. Therefore `deg_z D<=m-2` forces `h_0'=...=h_{n-1}'=0`. (The leading `h_n=1` is already constant.) This is descending triangularity, not a simultaneous linear algebra in mixed degrees.

The `h_j` then lie in the constant field of `K`. For the Kummer extensions used here, `K=k(x)(u)` with `u^d=h∈k[x]` after a licensed harmless constant extension containing the needed roots of unity. A finitely generated algebraic extension of `k(x)` in characteristic zero has constant field equal to the algebraic closure of `k` in that extension. After the licensed scalar extension, that constant field is the scalar field. No further constant-field enlargement is introduced by the high-row integration.

The producer replay never differentiates the `h_j` along `x`; it only checks the algebraic converse (constant `H` implies vanishing high rows along every `a_i`). The differential direction is the triangular argument above, independently confirmed as a series identity on four small pairs.

---

## Claim 3 — lower triangular terminal

**CONFIRMED.**

After `h_j'=0`,

```text
D=f_z sum_{ell>=1} r_ell' w^{-ell}.
```

Taking polynomial parts in `z` gives `D=sum_{ell=1}^{m-1} r_ell' A_ell` with `A_ell=[f_z w^{-ell}]_+`. Write `w=z(1+U)^{1/m}` and `w^{-ell}=z^{-ell}(1+U)^{-ell/m}`. Then

```text
f_z w^{-ell}=(m z^{m-1}+O(z^{m-3}))(z^{-ell}+O(z^{-ell-2}))=m z^{m-1-ell}+O(z^{m-3-ell}).
```

For `1<=ell<=m-1` the leading term is `m z^{m-1-ell}`. For `ell>=m` every exponent is negative, so `A_ell=0`. For `ell=m-1` the displayed expansion has constant term `m` and no other nonnegative power, so `A_{m-1}=m` as a polynomial. These leading terms and the vanishing boundary were checked on `(m,n)=(3,4),(3,5),(4,5),(4,7)`.

Ordering rows as coefficients of `z^{m-2},...,z^0` and columns as `(r_1',...,r_{m-1}')` produces an upper-triangular matrix with diagonal `m,...,m` and determinant `m^{m-1}` (`9` for `m=3`, `64` for `m=4`). When `h'=0`, the identity `D=sum r_ell' A_ell` holds as polynomials in `z`.

For the Keller factor: `z=uy+r` with `r=A/m`. The composition `(x,y)→(x,z)→(f,g)` has Jacobian

```text
J_{(x,y)}(P,Q)=D·(∂z/∂y)=u D.
```

(The `z_x` cross terms cancel in `P_x Q_y-P_y Q_x`.) The original Keller equation is `J_{(x,y)}=j`, hence `uD=j` and `D=j/u`, independent of `z`. Vanishing of the coefficients of `z^{m-2},...,z^1` forces `r_1'=...=r_{m-2}'=0` by the triangular matrix; the constant row is then exactly `m r_{m-1}'=j/u`. The sign is positive. The algebraic fibres of the constants `r_ell` are not solved.

---

## Claim 4 — independent specializations

**CONFIRMED.**

The coefficient of `z^{n-1}` in `g` is `delta0=h_{n-1}`, because `F_n` has no `z^{n-1}` term and `F_{n-1}` is monic. The next two rows are the unique triangular evaluations

```text
b_{n-2}=(n/m)a_{m-2}+c_{n-2},
b_{n-3}=(n/m)a_{m-3}+((n-1)/m)delta0 a_{m-2}+c_{n-3}.
```

(The quadratic binomial term in `U^2` first reaches `z^{n-4}`.) Specializing:

```text
(8,12):  b10=3/2 a6+c10,     b9=3/2 a5+(11/8)delta0 a6+c9;
(9,12):  b10=4/3 a7+c10,     b9=4/3 a6+(11/9)delta0 a7+c9.
```

An independent engine that first formed `w` by Newton and then took nonnegative parts of repeated products `w^j` reproduced both rows exactly, matched the binomial `F_j` for every `j`, and found no polynomial contribution from `k>j/2`.

High Jacobian degrees: `f_x` has degree at most `m-2` and, with constant `H`, `g_x` has degree at most `n-2`, so `D` has degree at most `m+n-3`. Vanishing of `z^{m-1}` through `z^{m+n-3}` is `n-1=11` rows, namely `z^{17}..z^7` and `z^{18}..z^8`. Every such coefficient vanished along every `∂/∂a_i`. Combined with Claim 2 this is existence plus uniqueness of the high-row solution, not a scan of `delta0'` along `a_i` (that row is the `j=n-1` step of the triangular argument, already constant by construction of `b_{n-1}`).

Relation supports, independently counted:

| Cell | `b0..b10` supports | Total | Max |
|---|---|---:|---:|
| `(8,12)` | `64,49,37,28,21,15,11,7,5,3,2` | `242` | `64` |
| `(9,12)` | `66,48,38,27,21,14,11,7,5,3,2` | `242` | `66` |

---

## Claim 5 — two-Laurent-row control

**CONFIRMED.**

The inverse `z=w+sum_{q>=1} t_q w^{-q}` is triangular: `t_q` first appears in `z^m` at exponent `m-1-q` with coefficient `m`. Truncation through `q=n+1` is necessary and sufficient for `[w^{-2}]z^n`, because the linear term is `n w^{n-1}·t_{n+1} w^{-(n+1)}=n t_{n+1} w^{-2}`. Independently: dropping `t_{n+1}` changes `r_2` and does not change `r_1`; `t_{n+1}` is nonzero on both cells. A numerical Newton iteration at the specialization `a_i=i+3` matched the residual inverse through `w^{-(n+1)}`.

Non-blocking observation: `t_m=0` identically (`z`-keys omit `-8` on `(8,12)` and `-9` on `(9,12)`), so `len(z(w))=13=1+(n+1)-1`. The producer loop still runs through `q=n+1` and still needs that last term for `r_2`.

By definition `H` has no negative powers, so `r_ell=-[w^{-ell}]g(z(w))`. After character/target specialization, every digest matched the producer:

| Cell | `e` | `r1` SHA-256 | `r2` SHA-256 | supports | ranks |
|---|---:|---|---|---|---|
| `(8,12)` | `4` | `d9c22f2addb15eeae5aa3f8f42daccdfeeb34478d8fd276897f8442736f56df0` | `1b36d219441be7dd0c978dd113026fb2b1dff655f71dd5e51d7547f92f253f07` | `19/27` | `2/2` |
| `(8,12)` | `2` | `f39c5b6a2f485208e4ce77acf75aeb747a76c3d3fcb9747b7d6a42f8f2095a04` | `a2f674eaa050d1bc910c067db791126365cab09708e568978201821a5bc5eaf0` | `36/54` | `2/2` |
| `(8,12)` | `1` | `d32685ae4d959eb1ecdea99f749a771ac43f117804e1e55fdecbddd8363f2303` | `2ad3011c4a39aae9fb250c2da02bb1706c3ab787d9ae21555f8255702e4345ea` | `79/99` | `2/2` |
| `(9,12)` | `3` | `7840bbc36f27dc819f3a20c9d31984784d18aaeb642808cd5c25d0c4eca83208` | `2a838beb9a2761f102ef66201729b9a35d7acf5a5fc740bd6dc052e83225837b` | `25/36` | `2/2` |
| `(9,12)` | `1` | `f81e2b95d45c5ad9e34fe8487cd405af3248d2a0701a4563e9ee7495015dca6f` | `2794d6786d0e11d0a7ec7d1c5ec5eac8e9549bdbf4fca7d948cfd644166169c9` | `80/106` | `2/2` |

Ranks are at the producer point `x_i=i+2` and at the alternate point `x_i=3i+7`. Rank two at two points proves local independence of `(r_1,r_2)` there. It is not a component dimension of any fibre, and no such inference is licensed.

---

## Claim 6 — target quotient

**CONFIRMED.**

Both cells have `n<2m` (`12<16` and `12<18`). The monic root of `f+q` is

```text
w_new=w(1+q w^{-m})^{1/m}=w+(1/m)q w^{1-m}+O(w^{1-2m}).
```

Substituting into `H(w)` and discarding `O(w^{j+1-2m})`, which is strictly negative for `j<=n<2m`, yields the finite triangular action

```text
h_{k,new}=h_k-((k+m)/m) h_{k+m} q,     0<=k<=n-m,
```

with `h_n=1` unmoved. The identity `g=[H_new(w_new)]_+` was checked on the four small pairs: `g` is invariant, and the opposite sign on `q` is not. Choosing `q=(m/n)h_{n-m}` slices `h_{n-m}`.

The other two gauges are target automorphisms of Jacobian `1`: `Q|->Q-h_m P` kills `h_m` because `F_m=f`, and `Q|->Q-h_0` kills `h_0`. No degree, monicity, source, or target-value pin in this probe consumes them. The three indices are

```text
(8,12): 8,0,4;     (9,12): 9,0,3,
```

pairwise distinct because `n≠2m` and `n≠m`. For a Kummer class of order `e`, a constant `h_j` can survive only for `j≡0 mod e`. Each gauge index is `0 mod e` for every `e|d` in the live lists `{4,2,1}` and `{3,1}`, so the quotient is character-compatible. Remaining constant indices, independently listed:

| Cell | `e` | allowed before quotient | remaining after |
|---|---:|---|---|
| `(8,12)` | `4` | `0,4,8` | none |
| `(8,12)` | `2` | `0,2,4,6,8,10` | `2,6,10` |
| `(8,12)` | `1` | `0..11` | `1,2,3,5,6,7,9,10,11` (nine, including `delta0=h_{11}`) |
| `(9,12)` | `3` | `0,3,6,9` | `6` |
| `(9,12)` | `1` | `0..11` | `1,2,4,5,6,7,8,10,11` (nine, including `delta0`) |

---

## Claim 7 — widths and allocation

**CONFIRMED.**

High-row width is `(m-1)` coefficient functions of `f` plus remaining Faber constants. Two-row local width subtracts the exact test rank `2`.

| Cell/`e` | remaining constants | high-row width | local width |
|---|---|---:|---:|
| `(8,12)`, `e=4` | `0` | `7` | `5` |
| `(8,12)`, `e=2` | `3` | `10` | `8` |
| `(8,12)`, `e=1` | `9` | `16` | `14` |
| `(9,12)`, `e=3` | `1` | `9` | `7` |
| `(9,12)`, `e=1` | `9` | `17` | `15` |

Arithmetic: `7+10+16=33`, `9+17=26`; `5+8+14=27`, `7+15=22`. Raw constant-`W` size and widest-branch width (`16` versus `17`) favour `(8,12)`. The order-four leaf is the narrowest single leaf. The mandatory order-two leaf of `(8,12)` is a second nontrivial width-`10` route, while `(9,12)` has a single nontrivial leaf of width `9`. Summing disjoint mandatory-route leaves is an engineering cost, not an algebraic dimension. On that explicitly stated metric the next lower-fibre allocation may be `(9,12)`, with the order-four `(8,12)` leaf retained as the cheapest control. No statement that `(9,12)` is mathematically simpler overall is licensed, and the producer does not make one.

---

## Claim 8 — scope and boundaries

**CONFIRMED.**

The original polynomiality conditions are the complete jets

```text
u^ell f^{(ell)}(A/m)/ell! ∈ k[x],
u^ell g^{(ell)}(A/m)/ell! ∈ k[x].
```

Nothing in the high-row integration, the target quotient, or the two-row control evaluates or cancels these families. Both remain charged on every Kummer class, including the polynomial cores `e=1`.

The complete remaining *differential* system on the tail is (0.1). That is not a classification of the algebraic fibres of the constants `r_ell`, not a rational or polynomial trajectory, and not emptiness of either frontier. Maximum-twelve automorphy is not a consequence of high-row integration: the history theorem still leaves `(8,12)` with `4|H` and `(9,12)` with `3|H` as residues. No counterexample is exhibited. JC2 is not claimed.

Independently, the two primitive maximum-twelve residues of the reviewed shear/UFD theorem are exactly these cells: among ordered pairs of maximum `12`, every pair other than `(8,12)` and `(9,12)` is `gcd<=2`, equal-degree `GL_2`, or a divisible target shear. That routing check uses the history stop, not a maximum-twelve automorphy theorem.

---

## Remarks (non-blocking)

1. The producer high-row scan differentiates only along the `a_i`. That is the correct algebraic converse for constant `H`. The `z^{m+n-2}` row is the `delta0'` step of Claim 2 and is not visible to `∂/∂a_i`; it is already constant by construction of `b_{n-1}`.
2. `t_m=0` in both inverse series is a depression identity, not a truncation defect. It explains `len(z(w))=13` and does not weaken `n+1` necessity for `r_2`.
3. Coefficient digests serialize sorted monomials as JSON and are independent of `PYTHONHASHSEED` (`0` and `1` produced identical sample digests). The producer claim of stability under four hash seeds is therefore unsurprising and was not used as evidence.
4. The preflight hostile review had not landed at producer freeze. The Kummer orders `{4,2,1}` and `{3,1}` were re-derived from `e|d` together with the residual criterion `gcd(H,d)=d`. No preflight conclusion beyond that routing and the charged Taylor jets is imported.
5. Comparison with the already reviewed `(6,9)` cube-core terminal `6 r_5'=j/s` is organizational only. No `(6,9)` coefficient, potential, or exclusion was used.

---

## Terminal boundary (accepted, not enlarged)

```text
complete universal high-row Faber integration=PROVED/REPLAYED
lower Laurent invariants reconstructed=ONLY r_1,r_2 CONTROL
lower-fibre components=NOT CLASSIFIED
either maximum-12 frontier empty=false
overall cheaper cell=NOT CLAIMED
JC2=NOT CLAIMED
```
