# `D = 108`: principal-minor split classification, faces, and joint-chart design

Lane `g108-minor-classification-opus5-20260903`.  Basis `9a813822`.
Row `(108,72)`; `M = (-72,81,106)`; `d = (108,36,9,1)`; `V = (7,7)`;
`u_3 = 2`, `v_3 = 7`; major radii `(delta_1,delta_2,delta_3) = (3/8, 1/4, -1)`.

## Verdict first

`MECHANICAL-CHECK`: PASS.  The manifest was generated with `awk` from the
`charged_input_<i>_sha256=` / `charged_input_<i>_basename=` lines of this
lane's `.run.v2` receipt and checked with `sha256sum -c`; all fourteen frozen
inputs returned `OK`, no digest retyped.  Manifest:
`box/g108minor-20260903/inputs.sha256`.

**The `D = 108` principal-minor split classification is a single branch.**

```text
COMPLETE[108-SPLIT-ORDERS]  delta = 3 is the ONLY admissible split order in
                            the detector window (1, v_s/u_s) = (1, 7/2) under
                            N5 (den(delta) <= u_s = 2)
EXCLUDED[108-DELTA-3/2 | -2 | -5/2]   each by two independent routes
SURVIVES[108-DELTA-3]       partition [1,1]; face p = pi^2 - c (c != 0),
                            q = p^23 u with u' = 5 p^2, deg u = 5;
                            1-parameter mod gauge (the constant e_0 of u)
OPEN[108-DELTA-3-LIFT]      global lift unproved; not a Keller witness
OPEN[MINOR-RADIUS-108]      delta* <= 3 on the split branch, delta* >= 7/2 on
                            the no-split alternative
```

This is strictly tighter than `(99,66)`, where the same recipe left two
branches.  Three things make `D = 108` the better second engine client:

* **one face, not two.**  `u_s = 2` means a genuine split has `deg p = 2` with
  two simple roots, i.e. it *is* a split "to `u_s` different roots", so Xu
  Cor. 7.5 applies below `(v_s+1)/(u_s+1) = 8/3` and kills `3/2, 2, 5/2`
  outright.  The face-ODE budget kills the same three independently.
* **the tree is fully rigid.**  `24` principal `g`-roots split `12 + 12`, both
  final at `delta' = 4`; each root of `p` being *simple*, each child packet has
  `deg p_child = 1` and cannot split again — Xu's §8(iii) `gcd` argument is not
  needed.  `Im = 7`, `IM = 21`, Cor. 5.3 passes.
* **the chart is the same shape.**  `n/d_2 = 3`, `m/d_2 = 2` exactly as at
  `(99,66)`, so the outer `A2/A3/B1/B2` tower and `build_FG` carry over; only
  the `h3 -> h2` step changes (`d_2/d_3 = 4`, not `3`).

Two `DERIVED-SOURCE` items and one printed erratum came out of the source read:

* `DERIVED-SOURCE[FACE-ODE-CLOSED-FORM]`.  Xu's (7.1) at any principal-minor
  split order reduces, for *every* row, to one ODE

  ```text
  K_g * a * q * p' - b * q' * p = K_g (v_s - u_s) * p^{W+1},
      K_g = n/d_s,  W = (-mu_s-2)/d_s,  deg p = u_s,  deg q = W u_s + 1,
      a = ord T_s(sigma) = W(u_s d - v_s) - 1 + d,  b = ord g(sigma) = K_g(u_s d - v_s).
  ```

  The right-hand constant is `delta`-independent — `45` at `(99,66)`, `60` at
  `(108,72)` — and `J(f,T_s)` gives the *same* equation, so this is the
  complete leading-order Jacobian content.
* `DERIVED-SOURCE[RESONANCE-SCREEN]`.  At a root of `p` of multiplicity `mm`
  with `ord_q = r`, either `r = W mm + 1` or `K_g a mm = b r` (then also
  `r <= W mm`).  With `sum r_i <= deg q` this reproduces Xu's printed
  `(99,66)` `q`-vectors exactly and settles `D = 108` in four rows.
* `ERRATUM[XU-COR-7.5-DISPLAY]` (`SOURCE-READ`, Xu p.12, cropped image in the
  drivers directory).  The `T_s(sigma)` line and the following `deg q(pi)` in
  Cor. 7.5's proof are printed with `(-mu_s + n - 2)/d_s`, the same fraction as
  the `(T_s)_f` line.  (7.1) forbids it: it forces
  `ord (T_s)_f = ord T_s + ord g + 1 - delta`, which holds only with
  `(-mu_s-2)/d_s` in the `T_s` line.  §7.3's multiplicity list and §8's
  `(99,66)` display both use `(-mu_s-2)/d_s` and are self-consistent
  (`deg q = 40`, not `3*22+1 = 67`).  Cor. 7.5's **conclusion** is unaffected:
  the inequality chain runs with `W >= 1` and the threshold is unchanged.
  Nothing charged downstream used the erroneous display.

Nothing here is a Keller witness.  No new exit-price assertion is made, so no
`charge_basis` line is licensed.

## 1. Pages opened, and the principal-minor data

`SOURCE-READ`.  Moh printed `p` is PDF page `p-139`; Xu printed `p` is PDF `p`.
Images at 150 dpi in `box/g108minor-20260903/pages/`:

| content | printed | image |
|---|---|---|
| Moh minor-disc dichotomy `V_r <= d_r/(n-M_r)`; Prop. 6.1 and its proof; the order identity; `delta*_{r-1} >= 1` and "does not specify the logarithmic radius"; the `(y-ax)^{v_s}(y-bx)^{u_s}` top form and `z = y-bx-e` | 190--194 | `moh_p190_pdf51-51.png` -- `moh_p194_pdf55-55.png` |
| Xu §7.3, Prop. 7.3 and its semigroup proof | 10--11 | `xu_p10_pdf10-10.png`, `xu_p11_pdf11-11.png` |
| Xu Cor. 7.5 proof, equation (7.1), the erratum display | 12 | `xu_p12_pdf12-12.png`, crop `xu_p12_cor75_display.png` |
| Xu §8, the `(99,66)` five-order display and split table | 13 | `xu_p13_pdf13-13.png` |

`SOURCE-READ`, Moh p.190: `D*_{r-1}` is **minor** exactly when
`V_r <= d_r/(n - M_r)`.  At `(108,72)` the threshold is `9/(108-106) = 9/2`, so
the `u_3 = 2` factor is minor and `v_3 = 7` is major: every Prop. 6.1 formula on
the principal packet is read with `V_r = u_s = 2` (threshold `11/2` at
`(99,66)`).  `SOURCE-READ`, Moh p.193 after the Q.E.D.: "*The above proposition
does not specify the logarithmic radius `d*_{r-1}` of `D*_{r-1}`.  We only get
an estimate `d*_{r-1} >= 1`.*"  That is `OPEN[MINOR-RADIUS-108]` verbatim.

### 1.1 Semigroup data (Moh p.150 recipe, calibrated on Xu's printed `(99,66)`)

`DERIVED-SOURCE`.  With `q_1 = M_1`, `q_i = M_i-M_{i-1}`, `lambda_1 = q_1 d_1`,
`lambda_i = lambda_{i-1} + q_i d_i`, `mu_i = lambda_i/d_i`:

```text
(99,66) : q = (-66,143,20)   lambda = (-6534,-1815,-1595)   -mu = (66, 55,145)
(108,72): q = (-72,153,25)   lambda = (-7776,-2268,-2043)   -mu = (72, 63,227)
```

The `(99,66)` line reproduces **Xu p.13's printed** `-mu_2 = 55`, `-mu_3 = 145`
— the calibration.  At `(108,72)`, `(108,72,63,227)` is a delta-sequence
(`gcd`s `36, 9, 1`), and `-mu_3 = 227 = 2 (mod 9)`, so `W = (-mu_3-2)/d_s = 25`
is integral as required.

### 1.2 The five Xu-type orders at `(108,72)`

`DERIVED-SOURCE`, from Xu §7.3's list `(-mu_i)u_s/d_s`, `((-mu_s-2)u_s/d_s)+1`.
Write `X = u_s delta - v_s = 2 delta - 7`:

```text
f(sigma)        = p(pi)^8  t^{ 8X} + ...        principal multiplicity 16
g(sigma)        = p(pi)^12 t^{12X} + ...                              24
T_2(sigma)      = p(pi)^7  t^{ 7X} + ...                              14
(T_3)_f(sigma)  = p(pi)^37 t^{37X} + ...                              74
T_3(sigma)      = q(pi)    t^{25X - 1 + delta} + ...   deg q = 25*2+1 = 51
here deg p(pi) = u_3 = 2.
```

The `(T_3)_f` exponent is Xu's own printed `(-mu_s+n-2)/d_s = 37` (Cor. 7.5),
equal to `W + K_g = 25 + 12`, which is what (7.1)'s order bookkeeping forces.
All five orders are checked in the driver against the **independent** count
`ord X(sigma) = -(#major roots of X) + (#principal roots)*delta` for every
`delta` in `{7/6, ..., 29/6}`, at both rows.  Prop. 6.1's order identity is the
`g` row, `ord g(sigma) = (n/d_s)(u_s delta - v_s) = 12(2 delta - 7)`, so

```text
ord g(sigma) < 0   <=>   delta < v_s/u_s = 7/2  =  the detector window ceiling.
```

## 2. Classification of the split orders

`DERIVED-SOURCE`.  `N5` (`PROVED`, charged `n5-denominator`) gives
`den(delta) <= u_s = 2`; Xu Prop. 7.3 gives `delta > 1`; the ceiling gives
`delta < 7/2`.  Candidates: exactly `{3/2, 2, 5/2, 3}`.  Since `deg p = 2`, the
only partitions are `[2]` (a linear power — Moh's unsplit branch-A analogue,
outside this classification) and `[1,1]` (two simple roots).

**Route A, printed: Xu Cor. 7.5.**  `u_s = 2 > 1`, and a `[1,1]` split *is* a
split to `u_s` different roots, so every `delta < (v_s+1)/(u_s+1) = 8/3` is
excluded: `3/2, 2, 5/2` die, `3` is untouched.  At `(99,66)` the same corollary
reached only `[1,1,1]` (threshold `9/4`); at `u_s = 2` it is far stronger.

**Route B, derived: the face-ODE budget.**  `p'`, `q'` are `d/dpi`, not labels.
From `J(g,T_3) = -(T_3)_f J(f,g)` in the `(t,pi)` chart
(`dx ^ dy = -t^{delta-2} dt ^ dpi`), Xu's (7.1) becomes the ODE of §Verdict with
`c = K_g(v_s-u_s) = 60`, `W+1 = 26`.  Screening with
`rho = K_g a/b = (51 delta - 176)/(2 delta - 7)`:

| `delta` | `a = ord T_3` | `b = ord g` | `rho` | `[1,1]` vectors with `sum r_i <= 51` | verdict |
|---|---:|---:|---:|---|---|
| `3/2` | `-199/2` | `-48` | `199/8` | non-resonant only: `(26,26)`, `52 > 51` | **EXCLUDED** |
| `2`   | `-74`    | `-36` | `74/3`  | non-resonant only: `(26,26)`, `52 > 51` | **EXCLUDED** |
| `5/2` | `-97/2`  | `-24` | `97/4`  | non-resonant only: `(26,26)`, `52 > 51` | **EXCLUDED** |
| `3`   | `-23`    | `-12` | `23`    | `(26,23)` and `(23,23)` | **ALIVE** |

A `[1,1]` split needs `rho` integral, since `mm = 1` forces `r = rho`; only
`delta = 3` has it.  `FALLACY-v2 / floor-attainment`: "alive" is a screen
survivor, never `FULL_ACTUAL_EXIT`.

**Galois.**  `den(3) = 1`, so `mu_e` is trivial and imposes nothing; conversely
the translation `pi -> pi + tau` *is* a gauge at integral `delta` (it adds
`tau t^3`, an integral-exponent term, to the common jet).  At half-integral
`delta` neither holds — that asymmetry is what forced `p = pi(pi^2-c)` at
`(99,66)`'s `5/2` and `p = pi^2(pi+3a)` at its `2`.

### 2.1 The surviving face in closed form, and its rigidity

`DERIVED-SOURCE`, residual identically zero in SymPy.  At `delta = 3` the ODE
is `p q' - 23 q p' = 5 p^26`; substituting `q = p^23 u` collapses it to

```text
p^24 * u' = 5 p^26      i.e.      u' = 5 p^2,   deg u = 51 - 46 = 5.
```

With the translation gauge (`p` monic quadratic, linear term removed) and the
scaling gauge `pi -> lam*pi` (which sends `c -> c/lam^2`, normalising `c = 1`):

```text
p(pi) = pi^2 - c,  c != 0        (c = 1 after gauge)
u(pi) = pi^5 - (10c/3) pi^3 + 5c^2 pi + e_0,      q = p^23 * u.
```

**The `delta = 3` face is a 1-parameter family mod gauge**, the parameter being
the integration constant `e_0` — the rigidity class of `(99,66)`'s `5/2` face,
looser than branch B's point.  The ODE does not see `p`'s linear term at all
(checked with `p = pi^2 + b_1 pi + c`), which is why the translation gauge is
the right quotient.

Internal consistency: `u(±sqrt c) = ±(8/3)c^{5/2} + e_0`, so `u` vanishes at
one root of `p` (giving `r = 23+3 = 26`) for one special `e_0` each, and at both
only if `c = 0` — precisely the budget statement that `(26,26)` is forbidden
while `(26,23)` and `(23,23)` are allowed.

### 2.2 The split tree is completely determined

`DERIVED-SOURCE`.  Continuing one packet,
`ord g(sigma') = -84 + (24-g_k)3 + g_k delta'`, final at `0`.  With `g_k = 12`:

```text
24 principal g-roots  ->  12 + 12,     each 12 g / 8 f,  final at delta' = 4.
Im = 1 + 2*(4-1) = 7.          IM = (n/(n+m)) * 56 * (1 - 3/8) = 21.
sharpened principal floor V_s/u_s = 7/2:   4 >= 7/2 for both packets.
principal places: 24, all e = 1 (delta = 3 is integral, unramified).
```

No second split is possible: each root of `p` is simple, so each child packet
has `deg p_child = 1`.  (At `(99,66)` branch B the double packet needed Xu
§8(iii)'s `gcd(12,18,10,25) = 1`; here it is automatic.)  Cor. 5.3 passes,
`21 >= 7`: a non-kill, as at `(99,66)`.  The Theorem 3.4 / (4.3) bookkeeping is
again tree-blind — the difference is the constant `m(v_s-u_s)/d_s = 40` for
every `k` and `delta` (`30` at `(99,66)`) — so
`SATURATED-EMPTY[THM-34-EQUALITY-SEPARATION]` carries over, and is moot with
one branch.

### 2.3 The dichotomy that remains

`FALLACY-v2 / flag-place-series`: the split order `delta`, the combined minor
radius `delta*`, and the major radii are three different objects.  §2 gives:

```text
(A)  the principal packet splits below 7/2  ->  delta = 3, the face of §2.1,
     the tree of §2.2, and delta* <= 3 < 7/2, so Prop. 6.3 is NOT licensed;
(B)  it does not split below 7/2           ->  delta* >= 7/2 = v_s/u_s, which
     is exactly Prop. 6.3's unproved premise, and Moh's descent runs, with
     descended profile (g,f,T_2) = (24,16,14) and monomial Jacobian exponent
     v_s - u_s - 1 = 4.
```

`(B)` is `DESCEND-WITH-MODIFIED-HYPOTHESIS`, not a proof of the premise;
`OPEN[MINOR-RADIUS-108]` stands.  The lane's contribution is that `(A)` is now a
*single, rigid* branch rather than an unclassified window.

## 3. Joint-chart design for the surviving face

`DERIVED`.  The chart is `g9966-global-design-sol56`'s two-point object,
re-instantiated.  Approximate-root tower, Tschirnhausen-normalised (the
`(k-1)`-th power dropped):

```text
h3 = P,                              y-degree d_3 = 9,   top form z^7 w^2
h2 = P^4 + C2 P^2 + C3 P + C4,       y-degree d_2 = 36,  top form z^28 w^8
F  = h2^3 + A2 h2 + A3,              y-degree n = 108
G  = h2^2 + B1 h2 + B2,              y-degree m = 72
```

(`F` is the degree-`n` object, `G` the degree-`m` one — the charged design
report's naming, opposite to the campaign's `f = m`, `g = n`.)  `w = z+1`;
`P`'s leading form is `y^{u_s}(y-x)^{v_s} = y^2(y-x)^7`.

**Ambient count, exact.**  Each block carries `y`-degree below the object under
it and total degree at its slot:

| block | `H` | `C2` | `C3` | `C4` | `A2` | `A3` | `B1` | `B2` | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `(108,72)` | 54 | 135 | 216 | 297 | 1998 | 3294 | 702 | 1998 | **8694** |
| `(99,66)` control | 77 | 198 | 319 | — | 1683 | 2772 | 594 | 1683 | **7326** |

`8694` equals the monic coefficient count `5995 + 2701 - 2` for degrees `108`
and `72`, so the tower is a coordinate chart, not a heuristic; the `(99,66)` row
reproduces the charged design report's counts exactly.  Fixing the two top forms
removes `180`, leaving **`8514`** named coordinates (`7161` at `(99,66)`).

**Prop. 6.2 bidegree box.**  In Moh p.194's `z = y-bx-e` coordinates the
bidegrees are forced, `(deg_y, deg_z) = (v_s,u_s)(degree)/d_s`:

```text
deg 108: (84,24), corner y^84 z^24, box 85*25 = 2125
deg  72: (56,16), corner y^56 z^16, box 57*17 =  969   (T_2: (49,14))
total 3094
```

`84+24 = 108` and `56+16 = 72` are the total degrees, so the boxes are full
rectangles with single-monomial corners.  `8696/3094 = 2.81` is the cut before
any branch data (`2.46` at `(99,66)`).

**Minor incidence block.**  The pole-cleared local leaders (the analogue of the
engine's `h3_minor_control` targets `t^9 zeta^2(zeta+3rho)`, `s^21 pi(pi^2-c)`)
are, with `ord_t(t^{deg}X) = deg + (deg/d_s)(u_s delta - v_s)` at `delta = 3`,
`e = 1`:

```text
t^9 h3 : t^8 (pi^2-c)     t^36 h2 : t^32 (pi^2-c)^4
t^108 F: t^96 (pi^2-c)^12 t^72 G  : t^64 (pi^2-c)^8
```

with the centre localised at `c != 0` (Rabinowitsch `Zc*c - 1`, never `sat()`)
and the child packets carried to `delta' = 4` with `deg p_child = 1`.  Because
`e = 1` there is **no `mu_2` equivariance to impose** — unlike `(99,66)`'s
`5/2` branch — so the block is a plain jet condition.  Centre parameters: the
jet coefficients at orders `1, 2`, plus `c` (gauged to `1`) and `e_0`; the `H`
block is `54` raw coefficients before the `D_2` weight cut.

**Jacobian rows.**  `J(F,G) = const != 0`, imposed band by band; the engine's
`jacobian_band` scalars `99` and `-66` become `108` and `-72`.

**What must be adapted in `box/g9966band-20260903/band_engine.py`.**

| site (`(99,66)` constant) | `(108,72)` replacement | status |
|---|---|---|
| `h3_template` top `{(0,8):1,(0,9):3,(0,10):3,(0,11):1}` = `z^8w^3` | `{(0,7):1,(0,8):2,(0,9):1}` = `z^7w^2` | `DERIVED` |
| `h3_template` `cap = 11 - r` (`d_3 = 11`) | `d_3 = 9` | `DERIVED` |
| `h3_template` `vmin` cut `(33-3r+3)//4`, `assert 21 vars` | rederive from the new weight | `OPEN[108-OUTER-WEIGHTS]` |
| `build_major_h2` `range(1,34)`, `range(34-r)` (`d_2 = 33`) | `range(1,37)`, `range(37-r)` | `DERIVED` |
| major weight `3*r + 4*q` (`A_2 = 3`, `ord_s(w-1) = 4`) | `4*r + 6*q` (`~ 2r+3q`); `A_2 = 4`, `ord_s(w-1) = 6` | `DERIVED`, rule below |
| `D1` thresholds `W >= 97`; rows `W=97 k<=4`, `W=98 k<=1`; `106`/`99`/`7` (`A_1 = 3`) | `A_1 = 2` — a **different** `D_1` boundary shape | `OPEN[108-OUTER-WEIGHTS]` |
| `k2` fixed top `z^24 w^9 = (z^8w^3)^3` (`d_2/d_3 = 3`) | `z^28 w^8 = (z^7w^2)^4`; `h2` gains a `C4` block, `equality` table recomputed | shape `DERIVED`, table `OPEN` |
| `build_FG` `k2^3 + a2 k2 + a3` / `k2^2 + b1 k2 + b2` | **unchanged** (`n/d_2 = 3`, `m/d_2 = 2`) | `DERIVED` |
| `OUTER_SPECS` slot degrees `65/98/32/65` | `72/108/36/72`, block sizes `1998/3294/702/1998` | sizes `DERIVED`, offsets `OPEN` |
| `jacobian_band` scalars `99`, `-66` | `108`, `-72` | `DERIVED` |
| `stage_spec` poles `-81/-54`, `-189/-126`, next `-77/-50` | one branch; recompute from `ord_t(t^{deg}X)` above | `OPEN[108-OUTER-WEIGHTS]` |
| `h3_branch_map` branches `delta2`, `delta52` | one branch `delta3`, free `(jet_1, jet_2, c)`, `c != 0` | `DERIVED` |

The major-weight rule, `DERIVED` and calibrated: with Moh (8)'s
`L_j = lcm{den delta_s..den delta_{j+1}}`, `A_j = den(L_j delta_j)`, the `D_2`
parameter is `t = s^{A_2}` and `ord_s(w-1) = A_2 L_1 delta_1`.  At `(99,66)`:
`A_2 = 3`, `3*3*(4/9) = 4`, giving the charged `3r + 4q` — the calibration.  At
`(108,72)`: `A_2 = 4`, `4*4*(3/8) = 6`, giving `4r + 6q`.  Because `A_1 = 2`
here and `3` there, the `D_1` boundary band count is **not** transferable; that
is what the engine lane must rederive first.

`COUNTING-BOUND` only: the first prefix dimension is `8514` named coordinates
minus the ranks of the six direct pole rows and the leading Jacobian band.  At
`(99,66)` that prefix moved `6704 -> 6689` over sixteen rows with fifteen unit
pivots; the `(108,72)` prefix has the same *shape* (`n/d_2 = 3`, `m/d_2 = 2`,
six pole rows, one Jacobian face) but its ranks need the weight cut.  This
report does **not** run the bands.

## 4. Controls

All in `box/g108minor-20260903/`: `python3 g108_minor_driver.py` and
`python3 g108_chart_design.py`, SymPy 1.12, under 60 s, no Singular, `<= 2`
cores.  Every assertion below is an `[ok]` line of the drivers' output.

* **C0/C1** skeleton and semigroup: both rows' `d`, `u_s`, `v_s`, Def. 5.1(3)
  radii; the Moh p.150 recipe reproduces **Xu's printed** `-mu_2 = 55`,
  `-mu_3 = 145`, the multiplicities `(27,18,15,40)`, the `p`-exponents
  `(9,6,5,22)`, Moh p.209's `t^-18`, and both charged five-order rows
  `(-12,-18,-10,-44,-25)`, `(-3,-9/2,-5/2,-11,-5)`; all ten orders agree with
  the independent root-contact count at both rows.
* **C2** replay: the screen returns exactly `{2 [2,1], 5/2 [1,1,1]}` at
  `(99,66)` after Galois, with `(25,14)` forced at `delta = 2` and
  `{(10,10,10),(14,10,10),(14,14,10)}` at `5/2` — Xu's printed vectors — and
  `[2,1]` alive at `5/2` at the ODE level, killed only by `mu_2`.  This is the
  replay the task required.
* **C3** faces: residual identically zero for `(99,66)`'s
  `p = pi^2(pi+3a), q = pi^25(pi+3a)^14(pi-2a)`, for `q = p^10 q_1` with
  `q_1' = 10p^3`, and for `(108,72)`'s `q = p^23 u`, `u' = 5p^2`; `J(f,T_3)`
  gives the same ODE as `J(g,T_3)` at every candidate.
* **C4** chart: the tower blocks reproduce the charged
  `77/198/319/1683/2772/594/1683 = 7326 = 7161 + 165`, `(108,72)` totals `8694`
  = its monic array, and the weight rule reproduces `3r+4q`.  Trees:
  `(3,4)`/`Im=6`, `(3,3,3)`/`Im=7`, `IM=16`; Thm 3.4 gap `30` for all `k`,
  `delta`.

## 5. FALLACY-v2 audit

*Flag/place/series*: major radii `(3/8,1/4,-1)`, split order `delta`, combined
radius `delta*`, and the denominators `A_j` are kept distinct; §2.3 states the
`delta`/`delta*` dichotomy without identifying them, and the ceiling `7/2` (on
`delta`, from `ord g < 0`) is never identified with the floor `V_s/u_s = 7/2`
(on the *final* `delta_sigma`, N11) though the values coincide.
*Carrier/attainment*: "alive"/"survives" is a screen result and a face
representative, never `FULL_ACTUAL_EXIT`.  *Floor/attainment*: `IM = 21` is the
all-major evaluation, used only to check Cor. 5.3 passes, so no kill rests on
it; the budget `sum r_i <= deg q` is necessary, and both survivors `(26,23)`,
`(23,23)` are exhibited by an explicit `q`.  *`sat()`*: no ideal was saturated
here; §3 declares the Rabinowitsch form `Zc*c - 1` for the engine lane.
*Prime label/derivative*: `p'`, `q'`, `u'` are `d/dpi`, stated at first use.
*Variable/ring map*: the `(y,z)` map is Moh p.194's `z = y - bx - e`, `b != 0`;
`w = z+1` is the engine's coordinate; the `pi`-gauge is given with its action
`c -> c/lam^2`, and the translation gauge is licensed by integrality of
`delta = 3` — exactly why it is *not* available at `(99,66)`'s `5/2`.
*Raw remainder degree*: the budget enumerates resonant and non-resonant
branches at every root rather than dropping leaders, and `r >= 1` is proved.
*Merge-free/M-descent*, *target/arrival index*: not touched.  No exit-price
assertion is made, so no `charge_basis` line.

## 6. Verdict and the exact next lane

```text
TYPED[D=108 SPLIT CLASSIFICATION]
  window     1 < delta < 7/2 (Xu Prop 7.3; Prop 6.1 ceiling); den <= 2 [N5]
  candidates 3/2, 2, 5/2, 3;  EXCLUDED 3/2, 2, 5/2 (Cor 7.5 AND ODE budget)
  SURVIVES   delta = 3, partition [1,1]
  face       p = pi^2 - c (c != 0);  q = p^23 u,  u' = 5 p^2,  deg u = 5
  rigidity   1-parameter mod gauge (e_0);  no mu_e constraint (e = 1)
  tree       24 -> 12+12, both final at delta' = 4; no second split
  invariants Im = 7, IM = 21 (Cor 5.3 passes); principal floor 7/2 cleared
  chart      8694 monic coefficients, 8514 after fixing the two top forms;
             Prop 6.2 box 3094; tower y-degrees (9, 36, 108/72), d_2/d_3 = 4
  OPEN       [108-DELTA-3-LIFT], [MINOR-RADIUS-108], [108-OUTER-WEIGHTS]
```

**Next lane, exactly one:** `g108-outer-bridge` — rerun the charged
`g9966-outer-bridge` derivation for `(108,72)` to produce the `D_2` weight cut
and the `D_1` boundary bands under `A_2 = 4`, `A_1 = 2`, `weight = 4r + 6q`.
That is the only `OPEN` blocking a full band run; every other engine constant
in §3's table is `DERIVED`.  Only after it should `g108-band-engine`
instantiate the single `delta = 3` chart — which, unlike `(99,66)`, needs no
branch fork, no `mu_2` equivariance, and no second-split argument.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `22158`.
- Body SHA-256:
  `ebc950a863bf3584ee5afce08f900844c09ff50bab3b9a0a1a522e659898e79f`.
- Frozen basis: `9a813822d081ac72494af8fe39666765fb2aaaa2`.
