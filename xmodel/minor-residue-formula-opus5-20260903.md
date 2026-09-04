# MINOR-EMPTY as a residue formula: the symbolic fit on four kill certificates

Lane: `minor-residue-formula-opus5-20260903` (Card B "SHARED-LEADER", coordinator-adopted).
Date: 2026-09-04 UTC. Desk CAS only (Singular 4.3.2, sympy), all jobs foreground under
`timeout`. No ledger edit, no `jc2-lean`, no in-progress lane report touched.

## 0. Verdict

`REFUTED[RESIDUE-VALUE-FORMULA]` + `PARTIAL[LADDER-LAW]` + `TYPED[DISC-COLLAPSE]`.

1. **The stated Card-B conjecture is refuted as posed.** "The residue is a rational
   function of the split datum, and the chart dies iff the residue is a unit" asks for a
   formula for a quantity that is not an invariant. Over `Q` every nonzero residue is a
   unit; the *value* depends on the basis and the pivot order. The `delta=2` stage-4 run
   emits **118** nonzero constant residues, any one of which certifies `1`; `6264` is
   simply the first (and, as it happens, their gcd). The `delta=5/2` value `64` is a
   normal form *after* 66 cumulative pivots. Neither number is chart-independent.
2. **A bounded symbolic search finds no formula even on the two numeric points.**
   2-atom and 3-atom multiplicative grammars over 22 datum atoms with a free
   `{2,3,5,7}`-smooth constant return **0** hits on `(6264, 64)`. Four atoms suffice but
   are underdetermined (5 free parameters, 2 equations), so a 4-atom fit is vacuous.
3. **What *is* uniform, and is new, is a derived row law.** The Jacobian band rows that
   do the killing at `(99,66)` obey
   `c(p,k) = +- [ e*A*(K-p) - n*(k-k0) ]`, `k0 = A*(e+f-1)-1`,
   with `K = d_2 = deg K2`, `A` the `y`-multiplicity of the top form of `K2`,
   `e = n/K`, `f = m/K`, `p` the band index. The `k=k0` member is **derived** from the
   top forms alone (the coordinate index cancels identically); the law reproduces
   **66/66** banked ladder entries with signs and all **8** ladder terminations.
   `783 = e*A*(K-p) = 27*29` and `675 = 27*25` fall out; `6264 = 8 * 783` exactly.
4. **The one genuinely uniform residue on the `u_s >= 2` stratum is the discriminant of
   the shared leader.** `R = disc(p_red)`, where `p_red` is the squarefree part of Xu
   Cor. 7.5's common `p(pi)` and the split partition is its multiplicity vector, equals
   the declared localisation in **3/3** charged branches. At `D=108` the kill *is*
   `R in I` (kill order 1): the incidence rows force `p = (pi - jet1^2)^2`, i.e. the
   `[1,1]` partition collapses to `[2]`.
5. **The fourth point is not a test of the stratum.** Moh's `(16,12)` (p. 208-209) is
   the Prop. 6.3 descent of `(64,48)` and has `u_s = 1`: `p` is linear, `disc` is empty,
   and its open condition is `J != 0`, not a partition condition. I computed its kill
   anyway (new result, below): the chart is **empty**, kill order **2**, residue the
   Jacobian constant. It cannot confirm or refute a `u_s >= 2` residue formula.

Score against the lane's own rubric: numeric `R`: **0/4** (and a type error).
Structural `R = disc(p_red)`: **3/3 on the stratum**, but it is the declared
localisation, so as a criterion it restates "dies after localising" rather than
predicting. **MINOR-EMPTY does not acquire a theorem route from a residue formula.** It
does acquire one transferable derived law (item 3) and one sourced mechanism (item 4).

## 1. Custody

The 17 frozen inputs in `/tmp/jc2-lane.boT2Oz/inputs` were checked before any use. The
manifest was generated mechanically with `awk` from the indexed
`charged_input_<i>_sha256=` / `charged_input_<i>_basename=` fields of
`xmodel/minor-residue-formula-opus5-20260903.run.v2`; no digit was retyped.
`sha256sum -c` returned `OK` for all 17. Manifest: `/tmp/lane-manifest.sha256`, 17
records. Work products are under `box/minor-residue-20260903/`.

Moh pp. 206-209 were re-extracted from the frozen PDF (`pdftotext`/`pdftoppm`, journal
page = PDF page + 139, offset established against the existing `moh_p200.txt`); the
display math on p. 208-209 is dropped by OCR and was read from the 200 dpi renders
`box/minor-residue-20260903/moh/moh_p20{7,8,9}.png`.

## 2. The three engine residues, as explicit rows

### 2.1 Dictionary (declared, then validated)

From the pinned engine's own basis (`box/g9966band-20260903/band_engine.py:484` for
`build_FG`, `:496` for `z_band_to_w`, `:506` for `jacobian_band`):

```text
KF = K2^3 + A2*K2 + A3     (deg 99 = n)      KG = K2^2 + B1*K2 + B2   (deg 66 = m)
K2 = t^33 h(1/t, w/t)      (deg 33 = K = d_2), top band w^9 (w-1)^24
J  = 99*KF*(KG)_w - t(KF)_t (KG)_w - 66*(KF)_w*KG + (KF)_w*t(KG)_t
   = [(n - t d_t)KF]*[d_w KG] - [d_w KF]*[(m - t d_t)KG]
```

Setting `t = 1/x`, `w = y/x` this is the plain `J_{x,y}(F,G) = F_x G_y - F_y G_x`
transported to the band basis (up to the substitution's monomial factor in `t`, which is
`1` on the bands used here — checked numerically below), and:

```text
B1c_{r,q}  =  coefficient of  x^{K-1-r-q} (y-x)^q  in B1        (deg B1 = K-1 = 32)
row (D,k)  =  coefficient of  x^{D-k} y^k          in J,   D = n+m-2-p = 163-p
```

so the driver's "Jacobian total degree `D`" is the homogeneous degree and `p = 163-D` is
the `t`-band index. Validation of the dictionary: it reproduces the frozen pivot
coefficients `-783` (`stage4_J_d159_k35` on `B1c_3_22`) and `+675`
(`stage8_J_d155_k35` on `B1c_7_19`) *by two independent routes* — a closed form and a
direct polynomial expansion — in `box/minor-residue-20260903/fits/k0_transfer.py`.
Matching names alone would prove nothing; these are numerical agreements against the
charged ledger.

### 2.2 `(99,66)`, `delta = 2`: `stage4_J_d159_k35 = 6264`

Write `u = y`, `v = y-x` (the change has unit Jacobian, so `J_{x,y} = J_{u,v}`). Take
`F` at its top form `u^{eA} v^{eB}` and the single `B1c_{r,Q}` term of `B1*h^{f-1}`,
namely `(u-v)^{c} u^{d} v^{g}` with `c = K-1-r-Q`, `d = A(f-1)`, `g = Q + B(f-1)`. Then

```text
J = (u-v)^{c-1} u^{a+d-1} v^{b+g-1} [ -c(a+b) u - beta*x ],   a = eA, b = eB,
beta = -(ac + ag - bd),      ac + ag - bd = e*A*(K-1-r)        <-- Q cancels identically
```

The lowest `y`-power in that product is `k0 = a+d-1 = A(e+f-1)-1 = 35`, and there only the
`beta` term survives. Hence, for **every** coordinate `Q`,

```text
[x^{D-k0} y^{k0}] J  =  (-1)^{eB+Q+B(f-1)-1} * e*A*(K-p)  ,   r = p-1.
```

For `(99,66)`: `e*A*(K-p) = 27*(33-p)`, giving `864, 837, 810, 783, 756, 729, 702, 675`
for `p = 1..8` — exactly the `k=35` entries of the frozen ledgers. So, **on the `B1`
block**, the row is

```text
stage_p_J_d(163-p)_k35 |_{B1}  =  +- e*A*(K-p) * SUM_Q (-1)^Q B1c_{p-1,Q},
```

a scalar times **one** alternating linear form. (The derivation covers the `B1` block
only; that the reduced row is exactly this — no `A2`, `A3`, `B2` remainder at this slot —
is what the `6264 = 8 * 783` cancellation below confirms, not something I derived.)
Equivalently the functional is
`phi |-> phi(u,v)|_{u=0,v=-1}`: `k0` is the lowest `y`-power, so it reads off the
`x`-pure coefficient of the block's top form.

The killing partner is the `delta=2` pole row at local power 8, frozen in
`stage4.json`'s ledger as

```text
stage4_G_local8_coord0 :  8*B1c_3_22  =  B1c_3_23 - B1c_3_24 + ... + B1c_3_29 - 8
```

i.e. the *same* alternating form set equal to `-1`. Substituting into
`stage4_J_d159_k35 = -783 * SUM_Q (-1)^Q B1c_{3,Q}` cancels every variable and leaves

```text
residue = (-8) * (-783) = 6264 = 2^3 * 3^3 * 29,      783 = e*A*(K-p) = 27*29.
```

So the arithmetic of `6264` is fully accounted for: `29 = K - p = 33 - 4` is a *band
index complement*, not a datum prime (no `29` divides `n, m, d_i, V_i, u_s, v_s`), and
the residual factor `8` is the pole row's inhomogeneous offset.
Localisation: `rho != 0`, wrapper `Zrho*rho-1`.

### 2.3 `(99,66)`, `delta = 5/2`: `stage8_G_local16_coord0 = 64`

Row: the `G`-side minor/pole row at local power 16 in the branch coordinate
(`t = s^2`, `w = u s^4 + v s^6 + pi s^7`), `pi`-coordinate 0; localisation `c != 0`.
The value `64` is the **exact normal form after all 66 cumulative `Q*` pivots**
(charged report, line 132), not a raw row coefficient. The seven new stage-8 pivots
`675, 576, 477, 378, 279, 180, 81` are the `p=8` ladder `27*25 - 99*(k-35)`, terminating
at `k = 41` because `27*25 - 99*7 = 81 > 0 > 27*25 - 99*8`. That termination rule
`k_max = max{k : e*A*(K-p) > n(k-k0)}` reproduces all eight banked ladders.

`64 = 2^6` has no derivation here. It is a post-reduction constant; I did not reconstruct
it and I do not claim a formula for it.

### 2.4 `D = 108`, `delta = 3`: the residue is `disc p`

The charged gate reports the stage-0 certificate as a combination of five residual rows.
Working directly from the frozen `incidence-variants.json` (both hostile variants):

```text
cutoff_43 (7 h3 coords):  -jet2^2,  2*jet1^2*jet2,  -2*jet2,
                          -c - jet1^4 + 9*jet1*jet2^2,   b + 2*jet1^2
cutoff_42 (9 h3 coords):  -c - jet1^4,                   b + 2*jet1^2
```

Both solve to `b = -2*jet1^2`, `c = -jet1^4` (and `jet2 = 0` in the tighter variant), so

```text
p(pi) = pi^2 + b*pi - c  ==  (pi - jet1^2)^2 ,     reduce(b^2 + 4c, I_inc) = 0.
```

The residue is exactly `disc p = b^2 + 4c`, with kill order 1 (`disc in I`, not merely in
the radical). **Mechanism, stated plainly:** the common-`h3` incidence forces the shared
leader to be a perfect square, so the declared `[1,1]` split partition collapses to `[2]`.
Verified in `box/minor-residue-20260903/fits/formula_search2.py`.

In the translation gauge `p = pi^2 - c` this degenerates to the charged
`1 = -(9/2) jet1 jet2 Zc r71 - (1/2) jet1^2 Zc r81 - Zc r80 - L`, whose row combination
is `-c`; the gauge-free statement is the discriminant.

### 2.5 The three declared localisations are all `disc p_red`

| branch | `u_s` | partition | `p(pi)` (charged `h3_control` target) | `p_red` | `disc p_red` | declared localisation |
|---|---:|---|---|---|---|---|
| `(99,66)` `d=2` | 3 | `[2,1]` | `zeta^2 (zeta + 3 rho)` | `zeta(zeta+3rho)` | `9 rho^2` | `rho != 0` |
| `(99,66)` `d=5/2` | 3 | `[1,1,1]` | `pi (pi^2 - c)` | same | `4 c^3` | `c != 0` |
| `D=108` `d=3` | 2 | `[1,1]` | `pi^2 + b pi - c` | same | `b^2 + 4c` | `c != 0` / `b^2+4c != 0` |

`deg p = u_s` in all three, as Xu Cor. 7.5 requires. This is 3/3 and is the single
best-supported uniform object in the lane. It is, however, the *localisation*, so
"dies iff `R` is a unit" is by construction true and carries no predictive content on its
own; the content is the **kill order** `N = min{ N : R^N in I }`, which is `0, 0, 1` here.

## 3. Moh's `(16,12)` calibration: new computation

### 3.1 What `(16,12)` is

`(16,12)` is the Prop. 6.3 descent of Moh's `(64,48)` row `M=[52,62]`, `V={2:3,3:3}`,
`d=(64,16,4,2)`, `u_s = d_s - V_s = 1`, `v_s = 3`, `Jacobian X^1`; descended skeleton
`Skel(16,12,[13],{2:3})`, `d = (16,4,1)`, so again `u_s = 1`. **It is a `u_s = 1` point,
outside the MINOR-EMPTY stratum.** The p. 208 chart (verified against the render):

```text
h(x,y) = y^3(y-x) + b1 y^3 + b2 y^2 + b3 y + b4 = y*A + b4 = y^2*B + b3 y + b4
gbar = h^4 + al1 h^3 + al2 h^2 + al3 h + al4 ,      fbar = h^3 + be2 h + be3
al1 constant (gauged to 0 by h -> h + al1/4)
al2 = c1 A + c2                 be2 = c3 A + c4
al3 = c5 A + c6 B + c7          be3 = c8 A + c9 B + c10
al4 = c11 A + c12 B + c13 (y-x)                             -> 17 coefficients
```

(The printed `alpha_3 = c5 A + c5 B + c7` has a repeated index in the journal; the second
must be `c6`, since the running count "17" requires 13 distinct `c`'s.)
Here `n=16, m=12, K=4, A=3, B=1, e=4, f=3` and `h_top = y^3(y-x)`, i.e. `A=3, B=1`.

### 3.2 The kill (new)

`box/minor-residue-20260903/charts/moh1612_kill.sing`, `moh1612_order.sing`. Building
`f, g` verbatim, `J = f_x g_y - f_y g_x`, and requiring every non-constant `x,y`-monomial
of `J` to vanish gives 67 distinct generators `I` in 17 unknowns, with Jacobian constant

```text
cst = c13 * ( 3 b3 b4^2 + b3^2 c3 + b2 b4 c3 + b3 c4 + b2 c8 + b1 c9 ).
```

Results (all four Singular controls pass: raw `dim = 10`, empty control `-1`, point
control `0`, `reduce(1, S) = 0`):

```text
dim std(I)                       = 10        (raw chart nonempty)
dim std(I + <Z*cst - 1>)         = -1        (Keller-localised chart EMPTY)
size(GB) = 1,  GB[1] = 1,  reduce(1,GB) = 0
kill order: reduce(cst, I) != 0,  reduce(cst^2, I) = 0     ->  N = 2
```

so `(16,12)` is **dead**, confirming Moh's "first case", and its residue is the
polynomial `cst`, whose normal form modulo `I` is

```text
4/3 c2 c8^2 - 8/9 c4 c8^2 + 1/6 b3 c6 c11 - b4 c8 c11 - 2/9 b3 c9 c11
 + 5/3 b3 c8 c12 + 1/2 b3 c2 c13 - 1/3 b3 c4 c13 + 3 b2 c8 c13 + 3/2 c7 c12 .
```

There is **no rational-constant residue** at `(16,12)`: the ideal is not `[1]` before the
localisation, so no row reduces to a nonzero number. The requested "kill value" does not
exist as a number for this point.

### 3.3 What transfers, and what does not

*Does not transfer.* The `(99,66)` killing row is the `k0` row of a Jacobian band, and
`k0` reads off the **`x`-pure coefficient of the leading Tschirnhaus block's top form**.
At `(99,66)` that block is `B1` with a generic degree-32 top form, so the row is nonzero.
At `(16,12)` Moh's `ord` conditions force `beta_2^{top} = c3 * y^2 (y-x)`, divisible by
`y^2`, so its `x`-pure coefficient is `0`. Singular confirms directly:
`[x^7 y^14] J = 0`, i.e. the predicted `k0` row is identically zero. **The `(99,66)`
mechanism is vacuous at `(16,12)`.**

*Does transfer, and reproduces Moh's own constant.* The degree bookkeeping predicts the
first nonvanishing Jacobian band at `p = 5` (`deg_y beta_2 = 3 => r = 2K-1-3 = 4`), and
Singular returns leading `x,y`-monomial `x^5 y^16`, total degree `21 = 26 - 5`. That whole
band is rank one:

```text
[x,y]-degree-21 part of J  =  (3 c1 - 4 c3) * y^16 (y-x)^5,
```

with coefficients `1,-5,10,-10,5,-1`. The single relation is `f*c1 = e*c3`, i.e.

```text
alpha_2^{top} / beta_2^{top}  =  e/f  =  n/m  =  4/3 ,
```

which is **exactly Moh's p. 209 constant**, recovered independently. His three constants
`4/3, 2/9, -4/81` are the binomial coefficients `C(n/m, j) = C(4/3, j)` of
`g == f^{n/m}` (verified symbolically). The analogue at `(99,66)` is `C(3/2,j) =
3/2, 3/8, -1/16, 3/128`, whose denominators are 2-powers — the origin of the 2-power
character of `64`, though not a derivation of `64` itself.

So the honest answer to "compute the `(16,12)` kill value the same way" is: the chart is
empty, the residue is a polynomial of kill order 2, and the number `81` that the lane
brief highlighted is `3^4 = ` the denominator of `C(4/3,3)` — a binomial denominator of
the ratio `n/m`, not a value of any residue.

## 4. The symbolic fit, stated as a search

`box/minor-residue-20260903/fits/formula_search.py`, `formula_search2.py`.

Datum atoms per branch (22 of them): `n, m, K, A, B, e, f, d_2, d_3, V_2, V_3, u_s, v_s`,
`delta` numerator and denominator, number of partition parts, band index `p`, local power
`ell`, `deg p = u_s`, and the derived `K-p`, `e*A`, `e*A*(K-p)`, `k0`. Only seven differ
between the two `(99,66)` branches, with ratios

```text
dnum 2/5,  dden 1/2,  npart 2/3,  p 1/2,  ell 1/2,  (K-p) 29/25,  c_J 29/25 .
```

The required ratio is `6264/64 = 783/8 = 3^3*29 / 2^3`.

```text
grammar                                              formulas fitting BOTH points
R = 2^i 3^j X^a Y^b, i in -3..6, j in -3..4, a,b in -2..3            0
R = C * X^a Y^b Z^c, a,b,c in -3..3, C {2,3,5,7}-smooth              0
```

Four atoms do admit solutions (e.g.
`R = 2^12*3^3 * (K-p) * dnum^-2 * npart^-3 * p^-2`), but that is 5 free parameters
against 2 equations: **a 4-atom fit on two points is not evidence.** The lane's stop
condition ("two candidate families refuted") is met by the two grammars above; I did not
continue, because the obstruction is not the grammar.

**The obstruction is a type error.** Over a field the residue *value* is not an
invariant: only its vanishing is. Concretely, from the frozen `stage4.json`:

```text
118 residual rows, all 118 nonzero, gcd = 6264
first four:  6264,  -6896032501736664,  711057573512402688,  -36797229429266839104
```

Any of the 118 certifies `1 = (1/r) * r`. `6264` is distinguished only as the gcd of the
family *in the charged integral basis*, and rescaling any row rescales it. Likewise `64`
is a normal form after 66 pivots and moves with the pivot order. A formula predicting
these numbers would be a formula for a basis choice.

## 5. What survives as transferable content

**(T1) The ladder law (derived at `k0`, fitted above it).**
For a chart `F = K2^e + ...`, `G = K2^f + B_1 K2^{f-1} + ...` with `K2` top form
`y^A (y-x)^B`, `K = A+B`, the `B_j`-block row in the band of homogeneous degree
`n+m-2-p` at the lowest `y`-power `k0 = A(e+f-j)-1` is

```text
c_J(p, k0) = +- e*A*(jK - p) ,   independent of the coordinate index Q,
```

and the row is `c_J * SUM_Q (-1)^Q B_{j,r,Q}` with `r = p-1`. The ladder above `k0`
follows `c(p,k) = c_J(p,k0) - n(k-k0)` on 66/66 banked entries with correct signs and all
8 terminations, but that part is a **fit, not a derivation** — it holds for the *reduced*
rows and I did not reconstruct the reduction. Consequences, all checkable per census row
with no engine: the killing band index range, the ladder length
`ceil( e*A*(jK-p) / n )` -- which reproduces the eight observed lengths
`9,9,9,8,8,8,8,7` exactly -- and the exhaustion point `p = jK`, where the ladder is
empty.

**(T2) The availability criterion.** The `k0` row is nonzero iff the top form of the
leading Tschirnhaus block has a nonzero `x`-pure coefficient. `(99,66)` passes;
`(16,12)` fails (its block top form is `y^2`-divisible). This is a one-line screen that
says in advance whether the `(99,66)` instrument can even fire on a given row.

**(T3) The disc-collapse mechanism.** On the `u_s >= 2` stratum, `R = disc(p_red)` is the
declared localisation in 3/3 branches, and at `D = 108` the kill *is* `R in I`. The
theorem candidate this supports is not "R is a unit" (vacuous) but:

> **MINOR-EMPTY (candidate).** Let `(F,G)` be a Keller pair whose Moh skeleton has
> `u_s >= 2` at the second point at infinity, and let `p(pi)` be the common
> principal-minor leader of Xu Cor. 7.5, of degree `u_s`, with multiplicity vector the
> declared split partition. Then the joint incidence + Theorem-1.2 order system forces
> `disc(p_red) in sqrt(I)`; i.e. the shared leader degenerates below the declared
> partition, and the chart is empty.

What remains to prove is *not* a number-theoretic statement about a residue. It is:
for every admissible datum, the incidence block forces the leader's root multiplicities
to strictly coarsen. That is a statement about the incidence compiler (tier 1), and this
lane's result is that it cannot be shortcut by a residue formula.

## 6. FALLACY-v2 audit

- **Raw remainder degree.** Declared throughout: `6264` is the first of 118 constant
  residues (and their gcd) in the charged integral basis; `64` is a normal form after 66
  pivots. Neither is presented as an invariant. `reduce`/`std` were run in the declared
  ring with `option(redSB)`; zero cases were handled explicitly (`[x^7 y^14] J = 0` is
  reported as a vanished row, not as an absent one).
- **Variable/ring map.** The map `B1c_{r,q} <-> x^{K-1-r-q}(y-x)^q`, `row (D,k) <->
  [x^{D-k}y^k] J`, generator order and coefficient field `Q` are declared in §2.1 and
  validated numerically against the frozen ledger by two independent routes. Matching
  names were not used as evidence.
- **Floor / attainment.** The `k0` value `e*A*(K-p)` is **derived**; the `k > k0` ladder
  is a 66/66 **fit** and is labelled as such. It is a description of the reduced rows,
  not a theorem about the unreduced system.
- **Carrier / attainment.** `(16,12)` `dim = -1` is emptiness of the declared localised
  chart, not a statement about any polynomial pair; no `REPRESENTATIVE` or
  `FULL_ACTUAL_EXIT` claim is made anywhere.
- **`sat()` wrapping.** Not used. Localisation is by Rabinowitsch variable only
  (`Z*cst-1`), with positive and negative controls run in the same ring: raw `dim = 10`,
  empty control `-1`, point control `0`, `reduce(1,GB) = 0`.
- **Flag / place / series.** The three kill orders `0, 0, 1` (and `2` at `(16,12)`) are
  reported per (chart, declared open condition). They are **not** identified as one
  invariant, and the four charts are not claimed to be instances of one filtration.
- **Prime label / derivative.** `p'`-type marks are avoided; `p_red` denotes the
  squarefree part, stated explicitly, not a derivative.
- **Fit vs proof.** The headline negative (§4) rests on a search over two bounded
  grammars plus a structural argument (non-invariance over `Q`). The search alone would
  only be evidence; the structural argument is what carries the refutation.
- No exit-price assertion is made, so no `charge_basis` line is emitted.

## 7. Two observations for other lanes (no edits made)

1. **`descent_table.py` `M_2` lacks the `u_s` factor.**
   `box/m2descent-drivers-20260903/descent_table.py:20` returns
   `M2 = Fraction(S.M[2], d_s)`, while `n2, m2` carry `u_s`. Moh's p. 209 table for the
   descended `(99,66)` reads `n=27, m=18, M_2=21, V_2=8, Jacobian X^4`; the driver prints
   `M_2 = 77/11 = 7`, and `21 = u_s * 77/11`. The two agree exactly when `u_s = 1`, which
   is the only case gate G1 checks (all four `P207` rows have `u_s = 1`), so the gate
   cannot see it. Any `u_s >= 2` row descended with this code has a wrong `M_2'`.
   Not touched by this lane.
2. **`p = jK` is the ladder's hard stop.** At `(16,12)` the `j=1` ladder is already
   empty at `p = K = 4`; at `(99,66)` it survives to `p = 32`. No single ladder is longer
   than `ceil(e*A*jK/n) = A*j` rows, so census rows with small `A` or small `K` cannot be
   killed by this instrument at all. Worth folding into the tier-0 screen.

## 8. Artifacts

```text
box/minor-residue-20260903/fits/ladder_law.py         66/66 ladder + 8/8 terminations
box/minor-residue-20260903/fits/derive_ladder.py      independent (x,y) top-form check
box/minor-residue-20260903/fits/k0_transfer.py        closed form vs direct expansion
box/minor-residue-20260903/fits/formula_search.py     2-atom grammar  -> 0 hits
box/minor-residue-20260903/fits/formula_search2.py    3-atom grammar  -> 0 hits; disc check
box/minor-residue-20260903/charts/moh1612.sing/.out   (16,12) chart, 67 rows, J constant
box/minor-residue-20260903/charts/moh1612_kill.sing   dim -1, GB 1, controls
box/minor-residue-20260903/charts/moh1612_order.sing  kill order 2, factorisation
box/minor-residue-20260903/charts/moh1612_band.sing   top band = (3c1-4c3) y^16 (y-x)^5
box/minor-residue-20260903/moh/moh_p20{6,7,8,9}.txt/.png   re-extracted source pages
```

Resources: all jobs foreground under `timeout`. The Singular jobs are cheap
(`moh1612_kill` measured at 0.14 s wall / 13 MiB RSS); the only slow step was a sympy
expansion of the degree-163 `(99,66)` Jacobian, which ran a few minutes and was then
superseded by the closed form of §2.2.

<!-- BODY-END -->
