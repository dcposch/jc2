# K00 V20R2 valuation four: `R4-02` branch closure

Author: Opus 5 (exact primary research lane)
Date: 2026-08-29 UTC
Repository basis: `31777ce90994a106aade85064c0d868e32863f94`
Lifecycle: `EXACT_DESK_THEOREM / UNREVIEWED / DIFFERENT-MODEL REVIEW REQUIRED`

## 0. Result

Both branches of the preferred residual `R4-02` are **empty**, and both close at
grade 15.  The closure is not a nonzero normal form: it is an explicit unit in
the localized ideal, exhibited as a `Q`-linear identity among the original seven
literal rows.

```text
R4-02a :  u_y = 0,              v_y != 0                       ->  EMPTY at grade 15
R4-02b :  u_y^2 = 192 v_y^2,    v_y != 0   over Q[r]/(r^2-192) ->  EMPTY at grade 15
```

The same computation proves a strictly stronger uniform statement (Section 8):
the **entire** old-plane-leading, next-rank-two cell is empty at grade 15, with
no dependence on the producer's grade-15 row-6 restriction and no case split at
all.  Consequently, subject to the promoted producer/review results consumed in
Section 1, the exact valuation-four grade-19 residual is `R4-00` alone.

Nothing here is an arc, a germ, a map, a periodicity, an attainment, a
maximum-12 statement, or a JC2 statement.  See Section 12.

## 1. Custody and consumed pair

Verified byte-exactly at the repository basis, at the start of this run:

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
be37360e22524c0f5e7a739753c237c3c94f71f0b5d44bfd9dcd89dddade134a
  xmodel/k00-r4-jetfan-provisional-sol56-20260829.md            (producer, full)
2ce2e4bfd9c23564a8e2be66437772d1cb9855ece4ebaf8ee37b005436c4ff43
  xmodel/k00-r4-jetfan-hostile-review-fable5-20260829-r1.md     (review, full)
```

Body seals recomputed here, both matching the pinned values: producer body
`10719` bytes, `3bb710d39c8fea9663bb1e6c1ed4d7c5b323a8741921b75aef2e8b844377bb40`;
review body `21336` bytes,
`220569e13dd5fbd14baffb53951992dbacbf5975e3c5a91795dced556ccf09d0`.

**Consumed as hypothesis** (from the reviewed pair, not re-derived here): the
grade-12 exclusion of leading ranks one and two, and the old-plane next-rank-one
grade-15 exclusion.  These select the stratum; they are not used inside any
identity below.

**Not consumed as an oracle.** The producer replay
`xmodel/k00-r4-jetfan-replay-sol56-20260829.py` was never executed, imported, or
read for values.  Everything below is a clean-room reconstruction from
`tails.json` and the frozen compiler, in scratch outside the repository. Where a
reviewed statement is re-derived independently it is marked `[re-derived]`.

## 2. Source map, ring, and variable order

Read from the frozen compiler and re-implemented from scratch.  Tail census
`569` terms, `ell = 1..7`, ten exponents with weights
`[8,7,6,5,4,3,2 | 2,6,10]` for `[C0..C6 | k10,k6,k2]` and weight law
`sum = 12 + ell`; load exponents in `{0,1}` with at most one active load.
Coordinate images

```text
C0=(1+d0)/256,  C1=d1,  C2=(1+d2)/16,  C3=d3,  C4=(3+d4)/8,  C5=d5,  C6=1,
```

load shifts `Lambda^2 k10`, `Lambda^6 k6`, `Lambda^10 k2`, targets `-Lambda^14
mu2` (row 2), `-Lambda^16 mu4` (row 4), `-Lambda^18 mu6` (row 6),
`-(Lambda^19/4) Jdet` (row 7), truncation `Lambda^20`.  Written out,

```text
G_i,n = [Lambda^n]( R_i(d) + Lambda^2 k10 M_i(d) + Lambda^6 k6 N_i(d)
                            + Lambda^10 k2 P_i(d) ) - target_i,n .
```

`[re-derived]` Constants: `R_i(0)=M_i(0)=N_i(0)=P_i(0)=0` for all seven rows.
Degree censuses: `R` `{2,3,4}`, `{2,3,4}`, `{2,3,4,5}`, `{2,3,4,5}`,
`{2,3,4,5}`, `{3,4,5,6}`, `{2,3,4,5,6}`; `M` `{2,3}`, `{2,3,4}`, `{2,3,4}`,
`{2,3,4}`, `{2,3,4,5}`, `{2,3,4,5}`, `{2,3,4,5}`; `N` `{1,2}`, `{1,2}`,
`{1,2,3}`, `{2,3}`, `{1,2,3}`, `{2,3,4}`, `{1,2,3,4}`; `P` `{1}`, `{1}`, `{1}`,
`{1,2}`, `{1,2}`, `{1,2}`, `{1,2,3}`.  (The review's `P` census omits the row-7
cubic and its `M` census omits the row-5/6/7 quintics; both first arrive at
grade 22+, so the window table is unaffected.)

Ring and order.  Coefficient field `Q` on branch `a`, and `Q[r]/(r^2-192)` —
a field, `Q(8*sqrt3)`, with both roots `r -> +-8*sqrt3` admissible — on
branch `b`.  Everything is done in the localization at the rank-two localizer
`v_y`; a formal inverse `iv` with `iv*v_y = 1` is carried and cancelled
canonically.  Declared variable order (also the elimination order):

```text
s, t                                   (leading old-plane point x)
a_y, b_y, u_y, v_y                     (next coefficient y, on the reduced cone)
a_m, b_m, u_m, v_m, A_m, B_m           m = 6..15, jet coefficients d[m]
k10[0..9], k6[1..9], k2[1..5]          load columns live in the window
mu2[1..5], mu4[1..3], mu6[1], Jdet[0]  target columns live in the window
```

`kappa = k10[0] != 0` and `Jdet[0] != 0` are the open conditions;
`k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0` are the boundary zeros.  All of these
freedoms are retained symbolically throughout; nothing is sampled or specialised
except where a solve is stated.

## 3. Adapted coordinates and the universal cokernel

With `A(q)=16q1-4q3+q5`, `B(q)=q0-4q2+2q4`,
`cone(a,b,u,v)=(2b+2u, a, b, 8a+v, b-u, 16a+4v)` and `e(A,B)=(B,0,0,0,0,A)`,
the map `(a,b,u,v,A,B) -> cone(a,b,u,v)+e(A,B)` is a linear isomorphism with
`A(p)=A`, `B(p)=B` (checked).  `[re-derived]` In these coordinates

```text
Q_i = alpha_i(u,v) A + beta_i(u,v) B + q_i(A,B),
```

| i | `alpha_i` | `beta_i` | `q_i(A,B)` |
|---|---|---|---|
| 1 | `3u/1024` | `-3v/1024` | `-(3/2048)AB` |
| 2 | `3v/256` | `3u/16384` | `(15/2048)A^2` |
| 3 | `-3u/8192` | `3v/8192` | `(3/8192)AB` |
| 4 | `0` | `0` | `-(3/8192)A^2 + (3/524288)B^2` |
| 5 | `-3u/131072` | `3v/131072` | `-(3/262144)AB` |
| 6 | `0` | `0` | `0` |
| 7 | `-3u/1048576` | `3v/1048576` | `0` |

so `Q_1+8Q_3 = (3/2048)AB`, `Q_4` is pure, `Q_6 = 0`; a common zero satisfies
`AB=0` and `B^2=64A^2`, hence `A=B=0` over any field — the reduced leading locus
is exactly the 4-plane, with `rank DQ = 2 <=> Delta = u^2+64v^2 != 0`.

A structural fact used below and not stated in the reviewed pair: **the image
of `DQ(y)` sits inside a fixed 2-plane of `Q^7`, independent of `(u_y,v_y)`**,

```text
W = span{ w , e_2 },   w = (1, 0, -1/8, 0, -1/128, 0, -1/1024),
alpha = (3u/1024) w + (3v/256) e_2 ,   beta = (-3v/1024) w + (3u/16384) e_2 ,
```

and `im DQ(y) = W` exactly when `Delta != 0`.  Hence the annihilator of `W` is a
*universal* five-dimensional cokernel basis, valid at every grade with no
`(u,v)`-dependence:

```text
K1 = G_4,  K2 = G_6,  K3 = G_3 + (1/8)G_1,
K4 = G_5 + (1/128)G_1,  K5 = G_7 + (1/1024)G_1.
```

Rows 1 and 2 are the complementary solving pair,
`det = alpha_1 beta_2 - alpha_2 beta_1 = (9/16777216) Delta`.

## 4. The stratum, the calendar, and what is imposed

`R4-02` is: `x = d[4] = ell(s,t) = cone(t/8, s, 0, 0) = (2s, t/8, s, t, s, 2t)`
with `(s,t) != (0,0)`; `y = d[5] = cone(a_y,b_y,u_y,v_y)` with `Delta_y != 0`;
and `u_y(192 v_y^2 - u_y^2) = 0`.  All `d[6..15]` are fully free
six-component jets, all live load and target columns are free symbols.

`[re-derived]` Window calendar, reproduced exactly:
`Q:8, C3:12, C4:16 | M2:10, M3:14, M4:18 | N1:11, N2:15, N3:19 | P1:15, P2:19`,
`mu2[j]:14+j`, `mu4[j]:16+j`, `mu6[1]:19`, `Jdet[0]/4:19`; grades 0-7 vanish
identically on the stratum, so "through grade 19" is the whole `Lambda^20`
truncation.  Degrees `>=5` in `d` are zero in the truncated ring because
`d` starts at `Lambda^4`.

Two consequences of the recursion, both verified symbolically at every grade:

* the *newest* coefficient `d[n-4]` enters grade `n` only through `DQ(x)`,
  which vanishes identically at old-plane rank zero — it is invisible at its
  own first grade;
* the newest *visible* coefficient is `d[n-5]`, entering exactly as
  `alpha_i(u_y,v_y) A_{n-5} + beta_i(u_y,v_y) B_{n-5}` (asserted and checked
  coefficientwise at each grade `n = 11..19`).

So at every grade `rows 1,2` determine `(A_{n-5}, B_{n-5})` and `K1..K5` are the
complete constraint set.  The cone parts `(a_m,b_m,u_m,v_m)` are never fixed at
grade `m+5`; they persist.  `d[15]` never becomes visible in the window.  No
contraction, no scalar shortcut, and no generic solve is used anywhere.

## 5. Grade-by-grade ledger

`K1..K5` at grades 11, 12, 13 are **identically zero** on the whole stratum;
the only content of those grades is the forward solve.

| grade | rows 1,2 determine | constraints `K1..K5` |
|---|---|---|
| 11 | `A_6, B_6` | all five identically `0` |
| 12 | `A_7, B_7` | all five identically `0` |
| 13 | `A_8, B_8` | all five identically `0` |
| 14 | `A_9, B_9` | `K2=0`; `K1` and `K3,K4,K5` live |
| 15 | `A_10, B_10` | `K1,K3,K4,K5` live; `K2` is the row-6 cubic |
| 16-19 | `A_11..A_14, B_11..B_14` | all five live (Section 9 control lane) |

**Grade 11 (exact, no inhomogeneity).**  For all seven rows

```text
G_i,11 = alpha_i(u_y,v_y) A_6 + beta_i(u_y,v_y) B_6 ,
```

with nothing else; explicitly on branch `a`,
`G_2,11 = (3/256) v_y A_6` and `G_1,11 = -(3/1024) v_y B_6`, and on branch `b`,
`G_1,11 = (3 v_y/1024)(r A_6 - B_6)`, `G_2,11 = (3 v_y/16384)(64 A_6 + r B_6)`.
Since `det = (9/16777216) Delta_y != 0` at rank two,

```text
A_6 = B_6 = 0                                                        (G11)
```

on both branches.  This is the only fact the closure needs from grades 8-14.

**Grade 12.**  Rows 1,2 give the unique
`(A_7, B_7) = ((10/3) kappa v_y, -(10/3) kappa u_y)`; the kernel is zero, so
this is complete, and all five cokernel rows vanish identically.

**Grade 14** (after `(G11)` and the grade-12/13 solves).  `K2 = 0` and

* branch `a`:  `K1 = (3/512) v_y^2 ( s + (25/12) kappa^2 )`, and
  `K3,K4,K5 = (3/32), -(3/256), -(3/4096)` times `t v_y^2`.  With `v_y != 0`
  these are exactly `t = 0` and `s = -(25/12) kappa^2`.
* branch `b`:  after dividing by the units `-(3/256)v_y^2` and `(3/1024) r v_y^2`
  (legitimate: `r^{-1} = r/192`),

  ```text
  E1 :  s + r t     + (25/12) kappa^2 = 0
  E2 :  s - (r/3) t + (25/12) kappa^2 = 0
  ```

  `E1 - E2 = (4r/3) t`, so `t = 0` and `s = -(25/12) kappa^2`.  The `2x2`
  system has determinant `-4r/3 != 0`; no case split arises.

`K1` at grade 14 is the producer/review five-term row 4 equation,
`(25/2048)kappa^2 v_y^2 - (25/131072)kappa^2 u_y^2 - (3/32768) s u_y^2
+ (3/512) s v_y^2 - (3/256) t u_y v_y`, consumed here in full; on branch `a` it
is precisely what pins `s`.  Note `s != 0` because `kappa != 0`, so `x != 0`
survives grade 14 on both branches: the cell is *not* killed there.

## 6. The grade-15 closure — exact identities

The following three are **polynomial identities on the stratum**, with `s,t`,
`a_y,b_y,u_y,v_y`, every `d[6..15]`, every live load column and every live
target column free.  No substitution of any kind has been applied.

```text
D1 := 16 G_7,15 - G_5,15 + (1/128) G_1,15
    = (3/4096) v_y (64 v_y^2 - 3 u_y^2)
      + A_6 [ (15/65536)(s u_y - B_6 k10[1] - B_7 kappa) + (9/512) t v_y ]
      + B_6 [ -(15/65536)(A_7 kappa + s v_y) + (9/32768) t u_y ]

D2 := G_3,15 + 8 G_5,15 + (3/16) G_1,15
    = -(1/512) v_y (64 v_y^2 - 3 u_y^2)
      + A_6 [ (5/8192)(B_6 k10[1] + B_7 kappa) - (9/8192) s u_y - (3/64) t v_y ]
      + B_6 [ (5/8192) A_7 kappa + (9/8192) s v_y - (3/4096) t u_y ]

D3 := G_6,15
    = (1/65536) u_y (192 v_y^2 - u_y^2)
      + A_6 [ -(5/32768)(A_6 k10[1] + 2 A_7 kappa) - (3/8192) s v_y + (3/8192) t u_y ]
      + B_6 [ (5/2097152)(B_6 k10[1] + 2 B_7 kappa) - (3/524288) s u_y - (3/8192) t v_y ]
```

`D1` and `D2` are `Q`-combinations of the universal cokernel rows,
`D1 = 16K5 - K4`, `D2 = K3 + 8K4`; `D3 = K2` is the producer's row-6 cubic,
independently re-derived here as `C3_6|cone = u(192v^2-u^2)/65536`.

Write `Phi := v_y (64 v_y^2 - 3 u_y^2)` and `Psi := u_y (192 v_y^2 - u_y^2)`.
Imposing `(G11)` kills every bracket, so on the `R4-02` cell

```text
D1 = (3/4096) Phi = 0,   D2 = -(1/512) Phi = 0,   D3 = (1/65536) Psi = 0 .
```

`D1` and `D2` are proportional; they are one equation, `Phi = 0`.  `Phi` is new
here — the reviewed pair only extracted `Psi`.

### 6.1 Branch `a`: `u_y = 0`, `v_y != 0`

`Phi = 64 v_y^3`, so `D1 = (3/4096)*64*v_y^3 = (3/64) v_y^3` and
`D2 = -(1/512)*64*v_y^3 = -(1/8) v_y^3`.  Both must vanish while `v_y != 0`.
**Empty.**  (`D3 = 0` identically on this branch, which is why the reviewed
pair could not close it.)

### 6.2 Branch `b`: `u_y^2 = 192 v_y^2`, `v_y != 0`, over `Q[r]/(r^2-192)`

`Phi = v_y(64 - 3*192) v_y^2 = -512 v_y^3`, so
`D1 = -(3/8) v_y^3` and `D2 = v_y^3`.  Both must vanish while `v_y != 0`.
**Empty.**  The right-hand sides contain no `r`, so the conclusion is identical
for the two conjugate roots `r -> +-8*sqrt3` and descends to any field in which
`192` is a square; over a field in which it is not, the branch is empty for
trivial reasons.  Again `D3 = 0` identically on this branch.

### 6.3 Certificate in the original seven-row presentation

Minimal generator set for the closure of `R4-02` — five of the eighty-four
literal equations:

```text
branch a:   G_2,11 ;  G_1,11 ;  G_1,15 , G_5,15 , G_7,15
branch b:   G_1,11 ;  G_2,11 ;  G_1,15 , G_5,15 , G_7,15
```

In the ring `L = F[s,t,a_y,b_y,u_y,v_y, jets, loads, targets][1/v_y]`
(`F = Q` or `Q[r]/(r^2-192)`), with

```text
branch a:  A_6 = (256/(3 v_y)) G_2,11 ,     B_6 = -(1024/(3 v_y)) G_1,11
branch b:  A_6 = (4/(3 v_y)) ( r G_1,11 + 16 G_2,11 ) ,
           B_6 = (1/(3 v_y)) ( 64 r G_2,11 - 256 G_1,11 )
           (the 2x2 solve of rows 1,2, determinant (9/65536) v_y^2; verified by
            back-substitution into the displayed grade-11 rows)
```

one has, from the identity `D1` above and with `c_a = 3/64`, `c_b = -3/8`,

```text
c * v_y^3 = 16 G_7,15 - G_5,15 + (1/128) G_1,15
            - A_6 * [ (15/65536)(s u_y - B_6 k10[1] - B_7 kappa) + (9/512) t v_y ]
            - B_6 * [ -(15/65536)(A_7 kappa + s v_y) + (9/32768) t u_y ] ,
```

with `A_6, B_6` replaced by the displayed multiples of `G_1,11, G_2,11`.  Since
`v_y` is invertible in `L`, the left side is a unit, so the ideal generated by
the seven rows through grade 19 is the unit ideal of `L`: the cell is empty as a
set over every characteristic-zero field and over any algebraic closure.  This
is an explicit membership of `1`, not a nonzero normal form.

`D2` is a second, independent certificate with the same shape and constants
`-1/8` and `1`; the two are not proportional as *combinations* of rows (they use
row 3 versus row 7), only their reduced values are.

Canonical digest of the certificate data (the 57 records printed as
`name|branch|monomial:coefficient;...` in the declared order — grade-11 rows,
grade-14 cokernel rows reduced by `(G11)`, grade-15 cokernel rows reduced by
`(G11)`, and the raw `D1`, `D2`, for each of the three strata `u_y=0`,
`u_y=r v_y`, `u_y` free):

```text
CERTIFICATE_DIGEST = 630b18798658b50f7a7dbc10decb7acc8258eb543bbeb2211e95f6b874986b51
CERTIFICATE_RECORDS = 57
```

## 7. Grades 16-19

Because the ideal is the unit ideal from grade 15, grades 16-19 are imposed but
vacuous over `R4-02`.  They are not skipped: they were computed and are reported
in the control lane of Section 9, which shows exactly what they would consume.

## 8. Uniform strengthening

The identities of Section 6 hold on the whole old-plane-leading, next-rank-two
stratum with `u_y` free.  There, `(G11)` still gives `A_6=B_6=0`, so grade 15
imposes `Phi = Psi = 0` with `Delta_y = u_y^2 + 64 v_y^2 != 0`:

```text
v_y = 0  =>  Delta_y = u_y^2 != 0  =>  u_y != 0  =>  Psi = -u_y^3 != 0 .   contradiction
v_y != 0 =>  Phi = 0 gives 3 u_y^2 = 64 v_y^2, so u_y != 0;
             Psi = 0 then gives u_y^2 = 192 v_y^2;  hence 64 v_y^2 = 576 v_y^2,
             i.e. 512 v_y^2 = 0.                                          contradiction
```

So the **entire** cell `{x on the old plane, rank DQ(y) = 2}` is empty at grade
15 over any field of characteristic zero, with no case split and without
assuming the producer's `u_y(192v_y^2-u_y^2)=0` restriction (that restriction is
`Psi=0`, one of the three inputs).  The `v_y != 0` clause of the producer's
`R4-02` is thereby a derived, not an assumed, condition.

Combined with the reviewed grade-12 exclusions of leading ranks one and two and
the reviewed old-plane next-rank-one grade-15 exclusion, the exact
valuation-four grade-19 residual is exactly `R4-00`.

## 9. Controls

1. **Negative control (the decisive one).**  Withholding *only* the five
   grade-15 cokernel rows and keeping everything else — all rows at grades
   11-14, rows 1,2 at grades 15-19, and `K1..K5` at grades 16-19 — the
   elimination runs to grade 19 **consistently** on both branches, solving
   four fresh variables per grade and determining `Jdet[0]` at grade 19 from
   `K5`.  Grade 16 gives `v_6 = 0` and `u_6 = (625/432) kappa^3` on both
   branches, and grades 17-19 each consume four further fresh jet parameters.
   So the machinery does not manufacture contradictions, and grade 15 is the
   unique kill.  A triangular auto-reducing substitution store is used; an earlier
   non-reducing store gave a spurious three-fold re-solve of `b_6` and was
   discarded.
2. **Independent numeric path.**  A second evaluator that re-reads `tails.json`
   and builds the seven rows as plain `Fraction` series — no symbolic layer, no
   shared code with the elimination — confirms at 20 exact random rational
   points, with all jets, loads and targets random and only `A_6=B_6=0` imposed,
   that `D1 = (3/4096)Phi`, `D2 = -(1/512)Phi`, `D3 = (1/65536)Psi`; and at 20
   further random points, with `A_6, B_6` also random, that
   `G_i,11 = alpha_i A_6 + beta_i B_6` for all seven rows.  A branch-`a`-specific
   run confirms the `(3/64)v_y^3` form at 12 points.
3. **Cross-checks against the reviewed pair, all independently re-derived and
   all matching:** `Q_1+8Q_3=(3/2048)AB`, `Q_4` pure, `Q_6=0`; the two-line
   reduced-cone proof; `M2_6 = -(5/32768)A^2 + (5/2097152)B^2` pure; `N1_i(ell)=0`
   and `M2_i(ell)=0` for all rows; `C3_6|cone = u(192v^2-u^2)/65536`;
   `C4_i(ell) != 0` for every row except row 6; row 6 at grades 13, 14 vanishing
   on the stratum once `A_6=B_6=0`; the row-4 grade-14 five-term equation;
   `G_i,12 = Q_i(z) + kappa polar_M2_i(x,z)` at old-plane next-rank-zero, for
   which I add that `C3_i(ell) = 0` for **all** seven rows, so no cubic
   inhomogeneity contaminates the `R4-00` entry system.
4. **A structural non-rescue.** `P1_i(ell) = (t/2) w + (s/32) e_2` lies in the
   fixed plane `W = im DQ(y)`, so the grade-15 `k2[1]` inhomogeneity is
   annihilated by all five universal cokernel functionals: the `k2[1]` column
   can move `(A_10,B_10)` but can never relieve `D1`, `D2` or `D3`.  Likewise
   `k6[1]` first reaches a cokernel row at grade 16.  This is why retaining the
   full load freedom does not weaken the closure.
5. **Mutation controls.**  `192 -> 193` in the row-6 cone cubic, and `+1` on a
   row-6 unloaded tail monomial, both change `D3`; `C4=(3+d4)/8 -> (1+d4)/8`
   breaks the constant-term cancellation of Section 2 — each detected.

Inert with respect to the closure certificate (carried and imposed, never
consumed by it): `k10[2..9]`, `k6[1..9]`, `k2[1..5]`, all target columns, the
cone parts of every `d[m]`, and `d[8..15]` entirely.  `d[15]` is invisible in
the window on this stratum.

## 10. Maximum exact result safe to promote

Over any field of characteristic zero, on the exact normalized V20R2 source with
`C6=1`, `k10[0]=kappa != 0`, `k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0`,
`Jdet[0] != 0`, `d = Lambda^4 x + Lambda^5 y + ...`, `x != 0`, `x` on the old
plane and `rank DQ(y) = 2`:

1. grade 11 forces `A(z)=B(z)=0`, and grade 15 forces both
   `v_y(64 v_y^2 - 3 u_y^2) = 0` and `u_y(192 v_y^2 - u_y^2) = 0`;
2. these are incompatible with `Delta_y != 0`, so the cell is empty as a set,
   by the explicit unit `(3/4096) v_y (64v_y^2-3u_y^2)` of Section 6.3;
3. in particular both branches of `R4-02` are empty, at grade 15, with the
   branch-specific units `(3/64) v_y^3` and `-(3/8) v_y^3`;
4. hence, with the promoted producer/review results, the exact valuation-four
   grade-19 residual is `R4-00` alone.

This is a field-valued, reduced, finite-jet emptiness statement.  It is *not* a
scheme-theoretic emptiness claim for a nonreduced rank cell: the certificate
exhibits `1` in the ideal of the localized reduced presentation, which settles
the set of `F`-points for every characteristic-zero `F` and every algebraic
closure, and nothing about nilpotents in a different presentation.

## 11. Cheapest successor

`R4-00` entry solve, desk-scale with exactly this machinery and now better
conditioned than the reviewed pair suggested:

* the grade-12 entry system is `Q_i(z) + kappa * polar_M2_i(x,z) = 0`; row 6 is
  identically zero, so it is six affine quadrics in the six components of `z`;
* `C3_i(ell) = 0` for all seven rows and `M2_i(ell) = 0` for all seven rows, so
  no cubic and no `M2` inhomogeneity enters; the first nonvanishing old-plane
  inhomogeneity is the quartic `C4_i(ell)`, live at grade 16 in every row except
  row 6 (`C4_6(ell) = 0`);
* solve the six quadrics over the `(s,t,kappa)` base, then split `z` by the same
  reduced fan.  On the resulting next-rank-two sub-cell the present Section 8
  argument applies verbatim one grade lower in the recursion, since `DQ(x) = 0`
  identically makes the whole ladder depend only on the second nonzero
  coefficient; that is the first thing to test, and it is a five-minute run.

No AWS packet is needed for this successor.  Should it stall, the frozen packet
is: pinned tails `d72f774c...`, the `R4-00` grade-12 ideal exactly as displayed,
`dp` over `Q`, eliminate the jet variables grade by grade through 19, decide
emptiness; nothing else.

## 12. Scope and nonclaims

This is an exact finite-jet emptiness theorem on the frozen V20R2 support, at
reduced, field-valued scope.  Formal jets are not arcs, germs, or maps; a
grade-19 residual point would not be one either.  Nothing here asserts or
denies: exact valuations three or five, any other support or normalization, any
periodicity or transfer between valuations, any attainment or maximum-12
statement, any polynomial Keller map, any counterexample, or JC2.  No exit
price, charge, or flag count is asserted, so no `charge_basis` declaration
applies.  The producer's and reviewer's grade-12 and next-rank-one results are
consumed as hypotheses selecting the stratum and are not re-verified here; a
different model should rebuild the seven rows and attack Sections 6 and 8
directly, in particular the claim that `G_i,11` carries no inhomogeneity and the
three grade-15 identities.

## 13. Compute and firewall

Clean-room scratch confined to `/tmp/k00r402/` (20 stdlib-only Python files,
exact `Fraction` and `Q[r]/(r^2-192)` arithmetic).  Full symbolic elimination
through grade 19: `2.1 s` per branch.  Numeric validation battery: `13.9 s`.
Structure, census, identity and control scripts: under `1 s` each.  All far
below desk caps.  No Singular, no AWS job, no web request, no external model, no
`jc2-lean` access of any kind, and no use of the producer replay.  Exactly one
repository file was created — this report; no canonical or existing artifact was
read for values, edited, or otherwise touched, and no git operation was run.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23493`.
- Body SHA-256:
  `32f79463afee2083dd5ca010d8783942484961a290766d06c707a2ed99c0a6b0`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
