# Outer Theorem-1.2 bands for the `(108,72)` joint chart

Lane `g108-outer-bridge-grok46-20260903`.  Basis `efd9174e`.  Add-on to the
charged `D=108` classification; drivers in `box/g108bridge-20260903/`.  No
ledger, `jc2-lean`, `ideation-*`, or named in-progress lane report was read
or edited.

## Verdict first

`MECHANICAL-CHECK`: PASS.  Manifest generated with `awk` from the
`charged_input_<i>_sha256=` / `charged_input_<i>_basename=` lines of
`xmodel/g108-outer-bridge-grok46-20260903.run.v2`, checked with
`sha256sum -c`.  All **11/11** frozen inputs `OK`.  No digest was retyped.
Manifest: `box/g108bridge-20260903/inputs.sha256`.

**`OPEN[108-OUTER-WEIGHTS]` is `DERIVED`.**  The missing `D2` weight cut and
the `D1` boundary bands under `A2=4`, `A1=2`, `weight=4r+6q` are exact linear
rows on the fixed-top outer `A,B` chart, plus the `h3` vmin cut and the empty
`h2`-`D1` window.  Exact `Q*` counts:

| band | A2 | A3 | B1 | B2 | total |
|---|---:|---:|---:|---:|---:|
| ambient `S(D,36)` (fixed tops) | 1962 | 3258 | 666 | 1962 | **7848** |
| D2 unit vanishings `4r+6q < 4(D-j)` | 1548 | 2808 | 408 | 1548 | **6312** |
| D2 remaining | 414 | 450 | 258 | 414 | **1536** |
| D1 raw `(e,Π)` slots | 32 | 66 | 10 | 32 | **140** |
| D1 `Q*` rank | 32 | 63 | 10 | 32 | **137** |
| D1 dependent (homogeneous) | 0 | 3 | 0 | 0 | 3 |

New independent outer pivots: **6449** (`6312+137`).  Occupied `D1` offsets
are even (`W` is even): raw `56,40,25,13,5,1`, rank `53,40,25,13,5,1`
(sum 137).  The `(99,66)` specialisation of the same formulae reproduces the
charged `5598+176=5774` and the charged offset lists
`64,52,40,29,20,11,6,3` / `41,38,33,25,19,11,6,3` exactly.

Tower unknowns: **8694** monic coefficients (`5995+2701-2`), a coordinate
chart; 8514 after fixing the two top forms.  The `9 ⊂ 36` step is
`h2=h3^4+C2 h3^2+C3 h3+C4`; `F_1=G_1=0` identities; 0 new outer pivots.

Residual, exact:

```text
DERIVED[108-OUTER-WEIGHTS]
OPEN[H2-D2-FACE-TRUNCATION]   (pi^4-1)^7  k=5,6,7 have r+q>36
OPEN[EFFECTIVE-T2-T3-BRIDGE]  pre-existing; 0 linear rows (as at (99,66))
```

Nothing here is a Keller witness.  No new exit-price assertion.

## 1. Pages and the general formula

`SOURCE-READ`, Moh p.149 Theorem 1.2: if `Q=h^d+∑_j Q_j h^{d-j}` with
`deg_y Q_j<deg_y h`, then `ord Q_j(σ_i) ≥ j·(λ/d)=j·ord h`.  Equality face
is allowed, not a row.  `SOURCE-READ`, Moh (8) p.201 (skeleton):
`L_j=lcm{den δ_s,…,den δ_{j+1}}`, `A_j=den(L_j δ_j)`.  `SOURCE-READ`,
Prop. 6.2 p.195: `(deg_y,deg_z)=(v_s,u_s)(degree)/d_s`.

Chart names: `F` = Moh `g` (deg `n`), `G` = Moh `f` (deg `m`).  Outer bands
are at the *first* (major) point; `u_s` is the complementary factor at the
second point.  They are not identified.

**General formula**, for the `n/d_2=3`, `m/d_2=2` Tschirnhausen tower
`F=h2^3+A2 h2+A3`, `G=h2^2+B1 h2+B2` (the shape of both `(99,66)` and
`(108,72)`).  Write `α_2=A_2`, `N=den δ_1`, `W_w=α_2 L_1 δ_1`.  On the three
charged rows `N=A_1 α_2`.  Homogenize `Q∈S(D,d_2)` by
`K_Q=t^D Q(t^{-1},w/t)` in the basis `t^r(w-1)^q`, support `r≥0`,
`0≤q<d_2`, `r+q≤D` (dimension `d_2(D+1)-d_2(d_2-1)/2`).

```text
W(r,q) = α_2 r + W_w q
D2:  t=s^{α_2},  w=1+π s^{W_w}
D1:  t=e^N,      w=1+e^{N W_w/α_2}+Π e^{N W_w/α_2+1}
     E = (N/α_2) W + k
ord h2(D2) = -1,   ord h2(D1) = -1/N
Thm 1.2:  ord A2 ≥ 2 ord h2,  ord A3 ≥ 3 ord h2,
          ord B1 ≥ 1 ord h2,  ord B2 ≥ 2 ord h2
```

Fixed-top slot degrees (`j` = the Theorem-1.2 index):

```text
A2: D=n-d2-1, j=2     A3: D=n-1,     j=3
B1: D=m-d2-1, j=1     B2: D=m-1,     j=2
```

Thresholds and ranks:

```text
W0 = α_2 (D - j)          vanish W < W0  (unit rows; rank = count)
E0 = N D - j              D1 gap: E < E0 on the D2-remaining support
expected outer rank  =  (# D2 unit rows) + (Q* rank of the D1 binomial matrix)
```

`h3` vmin cut, face weight `W_w v_s` (leading `(w-1)^{v_s}` at `r=0`):

```text
vmin(r) = max(0, ceil((W_w v_s + 1 - α_2 r)/W_w)),   r=1..d3,  cap=d3-r.
```

`d3` enters only the inner `h3⊂h2` step (`k2=d2/d3`); the outer `A,B`
formulae use `(n,m,d2)` together with Moh `(8)` radii, not `d3`.

## 2. `(99,66)` specialisation — charged numbers, exact

`α_2=3`, `A_1=3`, `W_w=4`, `N=9`, `W=3r+4q`.  `t=s^3`, `w=1+π s^4`;
`t=e^9`, `w=1+e^{12}+Π e^{13}`.  Slot degrees `65/98/32/65`.  Thresholds
`W0=189/285/93/189`, `E0=583/879/287/583`.

```text
ambient 6600;  D2 unit 5598 remain 1002;  D1 raw 225 rank 176 dep 49
new outer pivots 5774
D1 offsets s=0..7 raw 64,52,40,29,20,11,6,3  rank 41,38,33,25,19,11,6,3
h3 vmin: ceil((33-3r)/4), r=1..11, cap=11-r:  21 variables
h2 D1: W=97 k=0..4 and W=98 k=0..1:  7 rows
(π^3-1)^8 sites (4k, 24-3k), 1≤k≤8: all eight in S(33,33)
```

Every charged outer-bridge / global-band number named above is an assertion
of `outer_weights.py`.  `FALLACY-v2 / floor-attainment`: Theorem 1.2 is `≥`;
the 5774 are unit/Q* ranks of a relaxation, never a pair.

## 3. `(108,72)` specialisation

`α_2=4`, `A_1=2`, `L_1=4`, `δ_1=3/8`, `W_w=4·4·(3/8)=6`, `N=8`.
`W=4r+6q` (always even).  `t=s^4`, `w=1+π s^6`; `t=e^8`,
`w=1+e^{12}+Π e^{13}`; `E=2W+k`.  Slot degrees `71/107/35/71`.

```text
ord A2(D2)≥-2,  ord A3≥-3,  ord B1≥-1,  ord B2≥-2
ord A2(D1)≥-1/4, ord A3≥-3/8, ord B1≥-1/8, ord B2≥-1/4
W0 = 276, 416, 136, 276
E0 = 566, 853, 279, 566
```

Per-block table in the verdict.  `r_min` on D2-remaining: A2/B2 `17`, A3 `52`,
B1 `0` (the `r=0,q≥23` face of B1 survives, as B1 did at `(99,66)`).  D1
`e`-windows: A2/B2 `[552,565]`, A3 `[832,852]`, B1 `[272,278]`.  Odd offsets
are empty because `W` is even — they are not missing bands.

`h3` template, top `z^7 w^2={(0,7):1,(0,8):2,(0,9):1}`, face weight `42`,
strict `4r+6q≥43`:

```text
vmin(r)=max(0, ceil((43-4r)/6)),  r=1..9, cap=9-r
variables (7): (1,7),(1,8),(2,6),(2,7),(3,6),(4,5),(5,4)
unwanted face sites (3,5),(6,3) already excluded by vmin
```

`h2` D2 face weight `W_w·(v_s d2/d_s)=6·28=168`, strict `≥169`,
`r=1..36`, `q<37-r`: **100** remaining coordinates.  D1 ebound `8·36-1=287`.
Min `E` on remaining is `2·169=338>287`, so the `h2` D1 window is **empty**:
the D2 support already implies the D1 bound.  Not an attainment claim.

Prop. 6.2 boxes (charged classification, rechecked): `F` `(84,24)` box 2125;
`G` `(56,16)` box 969; total 3094.  `h2` corner `y^{28}z^8`; `h3` `y^7 z^2`.

## 4. The `h3→h2` step with `d2/d3=4`

Tschirnhausen (`char 0`, drop `h3^3`):

```text
h3 = P,                              y-deg 9
h2 = P^4 + C2 P^2 + C3 P + C4,       y-deg 36
F  = h2^3 + A2 h2 + A3,              y-deg 108
G  = h2^2 + B1 h2 + B2,              y-deg 72
```

Unfixed block counts `H/C2/C3/C4/A2/A3/B1/B2 = 54/135/216/297/1998/3294/702/1998`,
total **8694** = monic array `(108+1)(108+2)/2-1 + (72+1)(72+2)/2-1`.  The
tower is a coordinate chart.  Fixing the two top forms removes `108+72=180`,
leaving 8514 (outer 7848 + inner 666).  `(99,66)` control: `7326=7161+165`.

Expanding in `h3`, leading `F∼h3^{12}`, `G∼h3^8`:

```text
F_1=0,  F_2=3 C2,  F_3=3 C3,  F_4=3 C2^2+3 C4,  F_5=6 C2 C3,
F_6=C2^3+6 C2 C4+3 C3^2,  F_7=3 C2^2 C3+6 C3 C4,
F_8=A2+3 C2^2 C4+3 C2 C3^2+3 C4^2,  F_9=6 C2 C3 C4+C3^3,
F_10=A2 C2+3 C2 C4^2+3 C3^2 C4,  F_11=A2 C3+3 C3 C4^2,
F_12=A2 C4+A3+C4^3
G_1=0,  G_2=2 C2,  G_3=2 C3,  G_4=B1+C2^2+2 C4,  G_5=2 C2 C3,
G_6=B1 C2+2 C2 C4+C3^2,  G_7=B1 C3+2 C3 C4,  G_8=B1 C4+B2+C4^2
```

`F_1=G_1=0` are identities (no `h3^3` in `h2`).  Tower scaling
`ord h3(D2)=-1/4`; Thm 1.2 gives `ord C2≥-1/2`, `ord C3≥-3/4`, `ord C4≥-1`,
and the outer D2 bounds on `A,B` close the rest by addition of lower bounds.
`DERIVED`, **0** new outer pivots.  Inner D2 unit counts on the fixed-top
`C`-blocks (not extra ambient): C2 `97/126`, C3 `178/207`, C4 `254/288`.

The calibrated D2-face rule `(π^{k2}-1)^{v_s}` reproduces the charged
`(99,66)` sites `(4k,24-3k)`, `1≤k≤8`.  At `(108,72)` it is `(π^4-1)^7`,
sites `(6k,28-4k)`: `k=1..4` lie in `S(36,36)` with coefficients
`-7,21,-35,35`; `k=5,6,7` have `r+q=38,40,42>36` and are not ambient.
Truncating the polynomial is not a replacement.
`OPEN[H2-D2-FACE-TRUNCATION]`.

`T2≡G^3-F^2+lower` (`5` unknown; target deg `63`);
`T3≡G^{12}-F^8+lower` (`59` unknown; target deg `227`).  Leading-pair span
after the monic cancellation still misses `p^7` and a degree-`51` `q`.
Linear bridge rows: **0**.  `OPEN[EFFECTIVE-T2-T3-BRIDGE]`.

## 5. Engine constants (design-table format)

Mechanical JSON: `box/g108bridge-20260903/constants.json`.

| site (`(99,66)`) | `(108,72)` replacement | status |
|---|---|---|
| `h3_template` top `z^8 w^3` | `{(0,7):1,(0,8):2,(0,9):1}=z^7 w^2` | DERIVED |
| `h3_template` `cap=11-r` | `cap=9-r` | DERIVED |
| vmin `(33-3r+3)//4`, 21 vars | `(43-4r+5)//6`, **7** vars | DERIVED |
| `build_major_h2` `range(1,34)`, `range(34-r)` | `range(1,37)`, `range(37-r)`; `4r+6q≥169`; 100 strict | DERIVED |
| major weight `3r+4q` | `4r+6q`; `A2=4`, `ord_s(w-1)=6` | DERIVED |
| `h2` D1 `W=97 k≤4`, `W=98 k≤1` (7 rows) | **empty** (`338>287`) | DERIVED |
| outer D1 `A1=3`, offsets `0..7` | `A1=2`; occupied offsets `0,2,4,6,8,10`; ranks `53,40,25,13,5,1` | DERIVED |
| `k2` top `z^{24}w^9=(z^8 w^3)^3` | `z^{28}w^8=(z^7 w^2)^4`; C4 block | shape DERIVED |
| equality `(π^3-1)^8` | in-disk `k=1..4`; `k=5,6,7` | table OPEN |
| `build_FG` `k2^3+a2 k2+a3` / `k2^2+b1 k2+b2` | unchanged (`n/d2=3`, `m/d2=2`) | DERIVED |
| `OUTER_SPECS` `65/98/32/65`, W0 `189/285/93/189`, E0 `583/879/287/583` | `71/107/35/71`, W0 `276/416/136/276`, E0 `566/853/279/566`; sizes `1962/3258/666/1962` | DERIVED |
| `jacobian_band` `99,-66` | `108,-72` | DERIVED |
| `stage_spec` first `-80/-53`, next `-77/-50` | first **`-95/-63`**, next **`-92/-60`** (`t^{12}F∼p^{12}`, `t^8 G∼p^8` at `δ=3`) | DERIVED |
| `h3_branch_map` `delta2`/`delta52` | one branch `delta3`; free `(jet_1,jet_2,c)`, `c≠0` | DERIVED |

## 6. Controls

**(99,66).**  The general formulae specialise to the charged outer-bridge
totals, per-block ranks, D1 `e`-windows, offset raw/rank lists, 21-variable
`h3` cut, 7-row `h2` D1, and eight in-disk `(π^3-1)^8` sites.  Zero point
kills every homogeneous row.  D1 leftover rows reduce to `0` (3 dependent
slots at `(108,72)` are not a cokernel).

**(64,48).**  `d=(64,16,4,2)`, `u_s=1`, `v_s=3`, `δ=(9/16,1/4,-1)`,
`A2=A1=4`, `W_w=9`, `N=16`, `W=4r+9q`, `t=s^4`, `w=1+π s^9`, `t=e^{16}`.
Tower shape is `n/d2=4`, `m/d2=3` — **not** the `A2/A3/B1/B2` 3+2 chart; the
named outer blocks of this lane do not apply.  The same `W0=α_2(D-j)`,
`E0=ND-j` rules apply to whatever Tschirnhausen blocks are named.  `u_s=1`:
the `T2,T3` bridge is trivial (Xu Prop. 7.3 / Moh Prop. 4.4).
`NOT-APPLICABLE[3+2 outer A,B; (108,72) engine]`.

Automorphism `(ax+y,(a-1)x+y)` remains `NOT-APPLICABLE[degrees (1,1)]`.

## 7. FALLACY-v2

*Flag/place/series*: D1/D2 radii `(3/8,1/4)` are the major tower of Moh's `g`;
they are not the principal-minor split order `δ=3` and not `δ*`.  First-point
`v_s=7` is not identified with second-point `u_s=2`.  Even D1 offsets are a
parity of `W`, not a missing odd place.
*Carrier/attainment*: 6449 / remaining 1536 are a relaxation floor, never a
pair and never `FULL_ACTUAL_EXIT`.  The empty `h2` D1 window is a support
implication, not attainment of `ord h2=-1/8`.
*Floor/attainment*: Theorem 1.2 is `≥`; outer `A,B` equality faces are not
rows.  `h3` leading form is fixed, so its face is an exact coefficient
assignment, not a promoted bound.  Products of `≥` on `F_j,G_j` remain `≥`.
*`sat()`*: no ideal was saturated; D1 is exact `Q` Gaussian with leftover-zero.
*Variable/ring map*: `F=` Moh `g`, `G=` Moh `f`, `K_Q=t^D Q(t^{-1},w/t)`,
`t=s^4` at D2 and `t=e^8` at D1, `w=z+1`, `z=y-bx-e` (Prop. 6.2); stated.
*Prime marks*: none used as derivatives.
*Raw remainder*: D1 leftover = 0 in the declared `Q`-matrix.
No new exit-price assertion, so no `charge_basis` line.

## 8. Reproduction

```text
python3 box/g108bridge-20260903/outer_weights.py   # ~3 s, Q Gaussian
```

Python 3, SymPy 1.12.  No Singular.  Artifacts:
`box/g108bridge-20260903/{outer_weights.py,outer_weights.json,constants.json,inputs.sha256}`.

The exact next engine job is to instantiate `band_engine.py` on the single
`δ=3` chart with these constants (7 `h3` variables, 100 strict `h2`
coordinates, 1536 remaining outer `A,B` after D2, 137 D1 rows).  Closing
`OPEN[H2-D2-FACE-TRUNCATION]` is a separate face-identification, not a
weight cut.  Closing `OPEN[EFFECTIVE-T2-T3-BRIDGE]` remains nonlinear.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12501`.
- Body SHA-256:
  `ac40a2784c6227000486bbd768bcb0d8b53b3d43f24f9eea9e643c333f0256fe`.
- Frozen basis: `efd9174ea792eea15ec38a1a7ab47003928c7c87`.
