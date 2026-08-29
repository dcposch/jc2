# `BI-FACE-PROV-R0` cross-review — Opus 5, hostile, equal standing

**Date:** 2026-08-27
**Reviewer:** Opus 5, independent hostile cross-review
**Targets:**

```text
18e3e299b95cdb62ad795bafc5ac717313769564e0a314948d62158efd11107b
  xmodel/ggv-8_28-bi-face-provenance-r0-sol-ultra-20260827.md          (producer, Sol Ultra)
8bad7ca04ae9a6f45efde305b208309f528173820250d20dab67d00bc32d73a4
  xmodel/ideation-20260827T2137Z-postseal-exact-hostile-review.md      (review, Sol Ultra)
```

Both pins were recomputed on the live bytes before any other step and both
matched.  Nothing else in the tree was written.  No AWS process was launched,
inspected, or disturbed.  No canonical file or prior report was edited.  The
separate `jc2-lean` tree was not entered, listed, searched, read, status-
inspected, or modified.  Only exact desk-scale rational arithmetic in Python
was run; no Groebner basis, no determinant ideal, no solver.

**This report is review evidence only.  It claims no JC2, no Keller-pair, no
degree-bound, and no GGV 8_28 face/family conclusion.**

## 0. Itemized verdict

```text
Q1  442-slot ordered raw lattice + upper/lower regrading typed correctly   CONFIRMED
Q2  f_15_52 -> 0 (upper) and -14*a*rho (lower); g_23_80 collision too      CONFIRMED
Q3  localization makes a,rho units; graph fibre product over R_raw = 0     CONFIRMED WITH REPAIR
Q4  current source hashes; upper SOURCE.sha256 growth is custody-only      CONFIRMED WITH ERRATUM + one GAP
Q5  maximum licensed conclusion                                            REFUTED as stated by neither
                                                                           report, but SHARPENED:
                                                                           see section 5 - the separation
                                                                           is exactly the sublocus v_7=0
                                                                           and provably does NOT separate
                                                                           the branch-P stratum
```

The headline mathematical claim of both reports — that these two frozen
normalized fixtures cannot be two faces of one point of their shared ordered
raw slot scheme — is **CONFIRMED** by fully independent recomputation.  The
scope disclaimers in both reports were correct and appropriately cautious; I
upgrade the negative half of the scope statement from a disclaimer to a
theorem (section 5) and correct one typing sentence (section 4.3).

## 1. Custody actually recomputed

All eight mathematical-byte hashes cited by either report were recomputed on
the live tree:

```text
67c4038230829b7b9abea540d78ec15af8f87aa66259c0c8b79873de6106251e
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/SOURCE.sha256           (45 lines)
7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/compile_endpoint.py
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
70af56340845961625ce43945852da8f2350aa3d0a050532ca6138927d9c3298
  cases/ggv_8_28_lower_facepin_lf40_v1_20260827/SOURCE_FREEZE_TARGETFIX_R1.sha256
828f819e78ba36cf019e7014263148a4ee53ffd5b77ef77fee310637b82fc719
  cases/ggv_8_28_lower_facepin_lf40_v1_20260827/compile_lf40.py
bc61e6c33dc450664e1e83a98b9262210242c0713be005c78427161c3d6acc40
  cases/ggv_8_28_lower_facepin_lf40_v1_20260827/compiled/facepin_substitution.json
27de0604b07634c8c619585317ec0a183c1268494ed582ebf5a472be3ed3e841
  cases/ggv_8_28_lower_facepin_lf40_v1_20260827/compiled/slot_census.json
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
```

Every one of the seven non-manifest hashes matches **both** reports exactly.
The upper manifest is treated separately in section 4.

Additional custody recomputed by me and not reported by either target:

```text
all 45 entries of the upper SOURCE.sha256          verify OK against live bytes
all 48 entries of SOURCE_FREEZE_TARGETFIX_R1       verify OK against live bytes
all 15 SOURCE_PINS inside lf40_common.py           verify OK
the 4 PINS inside compile_endpoint.py              verify OK
```

`compile_endpoint.py` pins `raw_input = 28b9b05c...` and `lf40_common.py`
pins the identical `28b9b05c...` for the same path.  **Both compilers are
independently pinned to the same raw blob bytes**, which is stronger evidence
for the shared-lattice claim than either report supplies.  (`lf40_common.py`
also carries two `PRIMARY_SOURCE_PINS` for arXiv e-print URLs; those are not
local files and their absence is not a defect.)

## 2. Q1 — the shared lattice and the two regradings

**CONFIRMED, with every count independently reproduced.**

### 2.1 The lattice

`RAW_INPUT.json` carries `raw_slots_through_weight_22` with `F` of length 141
and `G` of length 301, total **442**, all 442 slot names distinct.  For every
record I checked the four internal consistency conditions

```text
slot name == f_i_j / g_i_j from raw_exponents,
raw_monomial == x^i*y^j,
weight       == 8+3i-j  (F) / 12+3i-j  (G),
chart_image  == t^weight * X^i.
```

Violations: **0 of 442**.  The stored `weight` field therefore *is* the upper
grading, on the nose, for the whole lattice.

Windows recomputed from the blob:

```text
F: u=0..14, degrees  (0,16),(0,15),(0,14),(0,13),(0,12),(0,11),(0,10),(0,9),
                     (0,8),(1,7),(1,6),(1,5),(2,4),(2,3),(2,2)
G: u=0..21, degrees  (0,24),(0,23),(0,22),(0,21),(0,20),(0,19),(0,18),(0,17),
                     (0,16),(0,15),(0,14),(0,13),(0,12),(1,11),(1,10),(1,9),
                     (2,8),(2,7),(2,6),(3,5),(3,4),(3,3)
```

These agree slot-for-slot with the producer's closed forms
`I_F(u): max(0,ceil((u-8)/3)) <= i <= 16-u` and
`I_G(u): max(0,ceil((u-12)/3)) <= i <= 24-u`.

### 2.2 Upper regrading

`compile_endpoint.py` `build_system` fixes literally

```text
A=(-1,0,0,0,1)=X^4-1,  H=A^2,  F[0]=H^2,  F[1]=H,  G[0]=H^3,  G[1]=(3/2)H^2,
F[2]=(1+H*Z)/4,  F[3]=(Z+A*T)/8,
G[2]=(3/2)H*F[2]+(3/8)H,  G[3]=(3/2)H*F[3]+(3/4)F[2]-1/16,
Z=sum z_d X^d (d<=6),   T=sum tt_d X^d (d<=9).
```

Expanding `G[2]` and `G[3]` gives `(3/4)A^2+(3/8)A^4 Z` and
`1/8+(3/8)A^2 Z+(3/16)A^3 T`, matching the producer's §3.1 table exactly.

`raw_windows` skips `weight <= 0` and raw variables are introduced only for
`weight in range(4,15)` (F) and `range(4,22)` (G).  `RAW_DIRECT_SYSTEM.json`
confirms this: **303 variables = 17 private (`z_0..z_6`, `tt_0..tt_9`) + 286
raw slots, every one of upper weight >= 4** (checked: zero raw variables of
weight < 4).  So the producer's `U_lin` is exactly the compiler's variable
ring.

Upper census recomputed from the polynomials, not copied:

```text
F_0=A^4  nonzero at i=0,4,8,12,16  values 1,-4,6,-4,1        5 nonzero, 12 zero
F_1=A^2  nonzero at i=0,4,8        values 1,-2,1             3 nonzero, 13 zero
G_0=A^6  nonzero at i=0,4,...,24   values 1,-6,15,-20,15,-6,1  7 nonzero, 18 zero
G_1=(3/2)A^4 nonzero at i=0,4,8,12,16  values 3/2,-6,9,-6,3/2  5 nonzero, 19 zero
                                                             ---------------------
                                              20 fixed nonzero + 62 forced zero
derived F_2,F_3,G_2,G_3 window sizes 15+14+23+22 =            74
live (weight >= 4)                                           286
                                                             ---
                                                             442
```

Identical to the producer's §3.1 total, including every fixed value.

### 2.3 Lower regrading

`compile_lf40.py` `load_slots` builds `Slot(..., shift - 4*i + j)` with
`shift` 8 for F and 12 for G, reading the **same** `RAW_INPUT.json` under
`RAW_REL`.  So `nu_F = 8-4i+j`, `nu_G = 12-4i+j`.  Recomputed independently:

```text
lower weight 0:   F 15, G 22, total 37
positive weight:  F 126, G 279, total 405
min lower weight over all 442 slots: 0   (no negative weights)
F profile 0..16 = 15,14,13,12,12,11,10,9,9,8,7,6,5,4,3,2,1
G profile 0..24 = 22,21,20,19,19,18,17,16,16,15,14,13,13,12,11,10,9,8,7,6,5,4,3,2,1
```

These are byte-equal to the frozen `compiled/slot_census.json`.

The cross-chart identities `u_F+nu_F=16-i` and `u_G+nu_G=24-i` are immediate
from the two formulas and hold on all 442 slots.

### 2.4 No transpose, and a real swap detector

Both compilers map `side "F" -> shift 8` and `side "G" -> shift 12` on the
same slot names from the same blob.  There is no component swap and no signed
transpose anywhere in the path I audited.  Beyond the producer's assertion,
`compile_lf40.py` carries two fail-closed cross-checks I re-ran by hand:

```text
stored_upper_matches != 442  -> fail   (the lower compiler certifies the
                                        UPPER grading on all 442 slots)
coincident_weights   != 22   -> fail   (u == nu on exactly 22 slots)
min(swapped_f_weights) >= 0  -> fail   (a P/Q swap is detectable because it
                                        drives some weight negative)
```

I recomputed `stored_upper_matches = 442` and `coincident_weights = 22`
directly from the blob.  Both hold.

**Q1 verdict: CONFIRMED.**  The lattice is shared, ordered, and consumed
identically by both compilers; the two regradings are deterministic monomial
regradings of the same slot set with no translation and no component swap.

## 3. Q2 — the two coefficient collisions

**CONFIRMED, by two independent frozen serializations plus my own expansion.**

### 3.1 `f_15_52`

The slot exists with `raw_exponents {x:15,y:52}`, stored `weight 1`,
`chart_image t^1*X^15`.  Upper weight `8+3*15-52 = 1`; lower weight
`8-4*15+52 = 0`.

Upper graph: the `u=1` F-row is `F_1 = H = A^2 = X^8-2X^4+1`, so

```text
alpha_U(f_15_52) = [X^15](X^4-1)^2 = 0     (deg 8 < 15; forced zero)
```

Lower graph: `face_substitutions` assigns, for every lower-weight-0 F slot,
`coefficient = comb(14, i-2) * (-1)^(16-i)` on monomial `a*rho^(16-i)`.  This
is literally `[xi^i] a*xi^2*(xi-rho)^14`.  At `i=15`:

```text
alpha_L(f_15_52) = C(14,13)*(-1)^1 * a*rho = -14*a*rho.
```

I recomputed **all 37** face relations from the closed forms and compared
against the frozen `compiled/facepin_substitution.json`: **0 mismatches, all
37 coefficients nonzero**.  The independent frozen
`desk_gate/facepin_derivation.json` records the same relation as
`{integer_coefficient: -14, rho_power: 1, scalar: "a", slot: "f_15_52",
xi_degree: 15}`.  Two frozen serializations and one hand expansion agree.

### 3.2 `g_23_80`

Stored `weight 1`, `chart_image t^1*X^23`; upper `12+3*23-80 = 1`, lower
`12-4*23+80 = 0`.

```text
alpha_U(g_23_80) = [X^23](3/2)(X^4-1)^4 = 0     (deg 16 < 23; forced zero)
alpha_L(g_23_80) = C(21,20)*(-1)^1 * b*rho = -21*b*rho
                 = [xi^23] b*xi^3*(xi-rho)^21.
```

Confirmed against the same two frozen files.

### 3.3 The complete cross-state census

Recomputed slot by slot over all 442:

```text
upper fixed/derived x lower fixed :   8
upper fixed/derived x lower live  : 148
upper live          x lower fixed :  29   (11 F rows u=4..14, 18 G rows u=4..21)
upper live          x lower live  : 257
                                    ---
                                    442
```

Exactly the producer's §3.3 numbers.  The 8 doubly-constrained slots are
exactly `f_16_56, f_15_52, f_14_48, f_13_44, g_24_84, g_23_80, g_22_76,
g_21_72`, i.e. `u = 0,1,2,3` on each component.  I verified the structural
reason: lower weight 0 means `j = 4i - shift`, hence `u = 2*shift - i`, i.e.
`i = 16-u` (F) and `i = 24-u` (G), which is precisely the **top** of each
upper window.  So the 37 lower-fixed slots are the upper window boundary, and
only `u <= 3` is doubly constrained.

The four derived boundary values were recomputed symbolically:

```text
[X^14]F_2 = z_6/4        [X^13]F_3 = tt_9/8
[X^22]G_2 = (3/8)z_6     [X^21]G_3 = (3/16)tt_9
```

matching §3.3, and the frozen face values are `91a rho^2`, `-364a rho^3`,
`210b rho^2`, `-1330b rho^3`.  With `a=b=1` from `u=0`, `f_14_48` gives
`z_6 = 364 rho^2` and `g_22_76` gives `z_6 = 560 rho^2`; the secondary
contradiction the producer records is real.  (`f_13_44`/`g_21_72` similarly
give `tt_9 = -2912 rho^3` vs `-21280/3 rho^3`; not stated by either report,
consistent with both.)

**Q2 verdict: CONFIRMED.**

## 4. Q3 — localization, units, and fibre-product variance

### 4.1 The localizer is literal

`singular_program` in `compile_lf40.py` emits verbatim

```text
ideal J=w*a*b*rho*f_0_8*g_0_12-1;
```

with `EXACT_SATURATION_FACTORS = ("a","b","rho","f_0_8","g_0_12")` and base
ring `QQ[a,b,rho,405 positive-weight raw slots]`.  In a commutative ring a
factor of an invertible product is invertible, so `a`, `b`, `rho`, `f_0_8`,
`g_0_12` are each units in `L_lin`, and `a*rho`, `b*rho` are units.
**CONFIRMED as stated by both reports.**

The escape route is genuinely closed: `f_0_8` has upper weight
`8+0-8 = 0`, `i=0`, so `alpha_U(f_0_8) = [X^0]A^4 = 1`; likewise
`alpha_L`-inverted `g_0_12` maps to `[X^0]A^6 = 1`.  Both localizer raw
factors are sent to `1` on the upper side, so they impose no contradiction of
their own and cannot rescue the ring.  Also note `f_0_8`, `g_0_12` have
*lower* weights 16 and 24, so they are live variables of `L_lin`, as required
for the Rabinowitsch relation to be well formed.

### 4.2 The fibre product really is the zero ring

The correct typed object is `Spec(U_lin tensor_(R_raw) L_lin)` with the two
canonical **source** maps `alpha_U: R_raw -> U_lin` and
`alpha_L: R_raw -> L_lin`.  In the tensor product,
`alpha_U(r) tensor 1 = 1 tensor alpha_L(r)` for every `r in R_raw`.  Taking
`r = f_15_52`:

```text
0 = alpha_U(f_15_52) tensor 1 = 1 tensor (-14*a*rho) = -14*(1 tensor a*rho).
```

Characteristic zero makes `14` a unit, so `1 tensor a*rho = 0`; multiplying by
`1 tensor (a*rho)^-1` gives `1 tensor 1 = 0`.  Hence
`U_lin tensor_(R_raw) L_lin = 0`.  The parallel `g_23_80` computation gives
the same conclusion independently.  **CONFIRMED.**

This is conservative in the right direction: for any later ideals `I_U`,
`I_L`, the map `U_lin tensor L_lin -> (U_lin/I_U) tensor (L_lin/I_L)` is
surjective, so a zero source forces a zero target.  Adding the nonlinear rows
cannot resurrect a point.  G2 must indeed not be launched on this pair.

### 4.3 REPAIR — the upper graph map is surjective

The producer's §5 asserts of `rho`, `a`, `b`, `z_d`, `tt_d` that "**None** is
a coordinate of the unrestricted raw-slot ring", and frames both sides as
irreversible.  For `rho` this is right; for `z_d`, `tt_d` it is **wrong**.

I formed the 74 derived-slot images as affine-linear forms in
`(z_0..z_6, tt_0..tt_9)` and computed the exact rank over `Q`:

```text
rank = 17 of 17.
```

So all 17 private variables lie in the image of `alpha_U`.  Explicit
preimages, using only F-side slots:

```text
z_0  = 4*f_0_6 - 1                     tt_0 = 4*f_0_6 - 8*f_0_5 - 1
z_1  = 4*f_1_9                         tt_1 = 4*f_1_9 - 8*f_1_8
z_2  = 4*f_2_12                        tt_2 = 4*f_2_12 - 8*f_2_11
z_3  = 4*f_3_15                        tt_3 = 4*f_3_15 - 8*f_3_14
z_4  = 8*f_0_6 + 4*f_4_18 - 2          tt_4 = 12*f_0_6+4*f_4_18-8*f_0_5-8*f_4_17-3
z_5  = 8*f_1_9 + 4*f_5_21              tt_5 = 12*f_1_9+4*f_5_21-8*f_1_8-8*f_5_20
z_6  = 8*f_2_12 + 4*f_6_24             tt_6 = 12*f_2_12+4*f_6_24-8*f_2_11-8*f_6_23
                                       tt_7 = 4*f_3_15-8*f_3_14-8*f_7_26
                                       tt_8 = tt_4 - 8*f_8_29
                                       tt_9 = tt_5 - 8*f_9_32
```

Since the 286 live slots map to themselves, `alpha_U` is **surjective**.
Therefore `Spec(U_lin) -> Spec(R_raw)` is a **closed immersion** and
`U_lin ~= R_raw/ker(alpha_U)`; `ker(alpha_U)` is an honest ideal of `R_raw`
containing `f_15_52` and `g_23_80`.

This does not weaken the verdict — it strengthens the proof.  The fibre
product collapses to a one-line base change:

```text
U_lin tensor_(R_raw) L_lin = L_lin / (alpha_L(ker alpha_U))
                           = L_lin / (..., -14*a*rho, -21*b*rho, ...) = 0,
```

because the ideal contains a unit.

By contrast `alpha_L` is **not** surjective, so the producer's variance
warning is exactly right on the lower side.  Proof: grade
`Q[a,b,rho,405 slots]_{s_L}` by `(deg_a, deg_b, deg_rho)`.  The image of
`alpha_L` is the subring generated by the 405 live slots (degree `(0,0,0)`),
`a`, `b`, and `a*rho^u` (`u<=14`), `b*rho^u` (`u<=21`); `w` has no raw
preimage.  Every generator with `deg_rho >= 1` has `deg_a+deg_b = 1`, and
this property is closed under products, so no element of the image has
`deg_rho = 1` with `deg_a = deg_b = 0`.  Hence `rho` is not in the image.

**Erratum recorded.**  The correct statement is: the *lower* fixture is a
genuinely non-closed parametrization requiring the fibre product; the *upper*
fixed/linear fixture is a closed subscheme, and on the upper side an ideal
description is available.  Naively summing two ideals living in two different
rings is still a type error, and the producer is right to refuse it.

### 4.4 Presentational erratum in §4 of the producer

Producer §4 presents the argument as two "augmented rows" `f_15_52 = 0` and
`f_15_52 = -14*a*rho` and subtracts them.  Read literally that is the naive
ideal sum its own §5 forbids.  It is nevertheless *sound*, because both
expressions are images of the same raw element under the two structure maps,
which is precisely the identification the tensor product makes.  This is a
presentation defect, not a mathematical one; the 21:37Z review states the
tensor form correctly.

**Q3 verdict: CONFIRMED WITH REPAIR.**

## 5. Q5 — maximum licensed conclusion

Taken first because it is where I depart most from both reports.

### 5.1 What the collision actually tests

Consolidating section 3.3: at each `u` the single doubly-fixed slot is
`i = 16-u` (F) / `24-u` (G), the top of the upper window.  The lower value is
always a unit times `rho^u`.  The upper value is `[X^(16-u)]F_u`.  Comparing
the polynomial degree with the window top:

```text
u=0  deg F_0 = 16 = top 16   leading 1        -> compatible, forces a=1
u=1  deg F_1 =  8 < top 15   leading 0        -> COLLISION
u=2  deg F_2 = 14 = top 14   leading z_6/4    -> free, compatible
u=3  deg F_3 = 13 = top 13   leading tt_9/8   -> free, compatible
u=0  deg G_0 = 24 = top 24 ; u=1  deg G_1 = 16 < top 23 -> COLLISION ; u=2,3 free
```

So the entire separation is the single statement that the frozen upper `F_1`
and `G_1` fall **7 degrees short** of their windows while the lower face,
having a nonzero root, does not vanish there.

Two immediate robustness facts, both verified:

* If `rho = 0` were allowed, the lower face degenerates to `a*xi^16`,
  `b*xi^24`, all eight doubly-fixed rows read `a=1, b=1, z_6=0, tt_9=0`, and
  the fixed/linear layer is **consistent**.  The separation is carried
  entirely by `rho != 0`, which is exactly what the Rabinowitsch localizer
  supplies.  The argument is therefore not vacuous, and it is not degenerate.
* The collision needs nothing about `A` beyond `deg A = 4`: any monic quartic
  gives `deg H^2 = 16`, `deg H = 8`, and the same shortfall.

### 5.2 The branch-P family is provably NOT separated

The upper compiler pins `cascade_producer = 6e3d9104...`, which is line 43 of
the upper `SOURCE.sha256` and verifies OK.  That pinned artifact states the
branch-P stratum literally:

```text
P: H=A^2, deg A=4, A monic squarefree
   F1 = H V,          deg V <= 7
   F2 = (V^2 + H Z)/4, deg Z <= 6
   F3 = (V Z + A T)/8, deg T <= 9
   c2 = 0  or  A | V
```

The frozen fixture is the single point `V = 1`, i.e. `v_7 = 0` — and the
upper `PREREGISTRATION.md` says so explicitly: "the reviewed branch-P
coordinate `F1=H V` is fixed at `V=1`".

I carried out the general-`V` computation.  The `c2=0` normalization
`G = F^(3/2)` gives

```text
G_1 = (3/2) H^2 V,
G_2 = (3/2) H F_2 + (3/8) H V^2,
G_3 = (3/2) H F_3 + (3/4) V F_2 - (1/16) V^3,
```

which reduce at `V=1` to exactly the three hardcoded expressions in
`compile_endpoint.py`.  As an independent validation I evaluated the literal
D5G recurrence `D_n = sum_(i+j=n) ((12-j) F_i' G_j + (i-8) F_i G_j')` from the
compiler on these general forms:

```text
D_0, D_1, D_2, D_3 vanish identically in v_0..v_7, z_0..z_6, tt_0..tt_9.
```

(The compiler only asserts this at `V=1`.)  The general boundary
coefficients are then

```text
[X^16]F_0 = 1                     [X^24]G_0 = 1
[X^15]F_1 = v_7                   [X^23]G_1 = (3/2) v_7
[X^14]F_2 = (v_7^2 + z_6)/4       [X^22]G_2 = (3/4)v_7^2 + (3/8)z_6
[X^13]F_3 = (tt_9 + v_7 z_6)/8    [X^21]G_3 = (3/16)tt_9 + (1/8)v_7^3 + (3/8)v_7 z_6
```

**Both collisions hold if and only if `v_7 = 0`.**  And for `v_7 != 0` the
fixed/linear layer is not merely non-colliding — it is fully solvable.  Set

```text
a = b = 1,   v_7 = -14 rho,   z_6 = 168 rho^2,   tt_9 = -560 rho^3.
```

All eight doubly-fixed rows are then simultaneously satisfied (verified
exactly):

```text
F u=0..3 :  1, -14 rho,  91 rho^2, -364 rho^3      = face values
G u=0..3 :  1, -21 rho, 210 rho^2, -1330 rho^3     = face values
```

Every value is inside its declared window (`deg V <= 7`, `deg Z <= 6`,
`deg T <= 9`), `A = X^4-1` is unchanged, `c2 = 0` is unchanged.  The 29
`upper live x lower fixed` rows merely assign 29 distinct free live slots, so
they add no obstruction.  Hence

```text
U_lin(general branch-P, v_7 != 0)  tensor_(R_raw)  L_lin  !=  0.
```

The structural reason is visible in the pinned cascade artifact itself: for
`U = H + (V/2)t` one has `F = U^2`, `G = U^3` fitting every frozen window,
while the lower face is `a*K_rho^2`, `b*K_rho^3` with `K_rho = xi(xi-rho)^7`.
Both sides are a square/cube pair, and the eight boundary rows are exactly the
statement that the two leading data agree; they do agree, at `v_7 = -14 rho`.

### 5.3 Maximum licensed conclusion

**Licensed.**  For the shared frozen ordered 442-slot `R0` raw lattice, the
two frozen charts, and the two frozen graph parametrizations, the
scheme-theoretic fibre product

```text
Spec(U_lin) x_(Spec R_raw) Spec(L_lin)
```

is **empty**, and remains empty after adjoining any further ideals on either
side.  This holds not only at the two literal fixtures but on the family

```text
upper: any monic quartic A, H=A^2, c2=0, any V with v_7=0 (deg V <= 6),
       any Z (deg<=6), any T (deg<=9), arbitrary values on the 286 live slots;
lower: the full 3-parameter torus a, b, rho all invertible.
```

That is positive-dimensional on both sides, so the answer to the question as
posed is: **more than the two literal normalized fixtures, but strictly less
than the branch-P stratum.**

**Not licensed, and now provably false if asserted.**  The proof does *not*
separate the branch-P family from the lower FACEPIN family.  Section 5.2
exhibits an explicit compatible point for every `rho` with `v_7 = -14 rho`.
Any promotion text asserting an upper-branch-P / lower-FACEPIN family
separation would be refuted by that point.

**Also not licensed.**  Nothing after coordinate change, normalizer action,
or any gauge freedom on `(x,y)` or on the pair `(f,g)`: such actions change
the raw support and the weight windows, so the whole cross-table is
re-derived, not transported.  Neither report claims otherwise and neither
should.

**Inherited firewall.**  `RAW_INPUT.json` self-declares
`control_id = R0_ARTIFICIAL_CUSP_CONTROL`, `scope = "artificial frozen
control only; symbolic raw 2S/3S slots through weight 22"`, and lists
`"8_28 face/family exclusion"` explicitly among `firewalls.claims_not_made`.
The producer handles this correctly (§2.1: only the symbolic lattice is
consumed).  Any downstream text must carry the same firewall.

**Q5 verdict.**  Both reports' scope sentences ("separates these two
normalized frozen fixtures", "does not separate the whole upper branch-P
stratum") are **CONFIRMED and correct**.  I refute only the stronger reading
that a reader might take from the producer's §0 phrase "exact separation",
and I replace the disclaimer with the exact criterion `v_7 = 0` plus an
explicit counterexample for `v_7 != 0`.

## 6. Q4 — source hashes and the manifest growth

### 6.1 The three competing manifest states

```text
c66b139604c5f45357a4f078b1ba9360ea8cee5cd87e878722466f12846e6338
   recorded as "complete source manifest" in ideation-20260827T2137Z-packet.md:176
324f4293a8fae7baab2632f89d1274dc1b880a8708f34c2348e46a7f4fe915b7
   recorded by the BI-FACE producer, described there as a 43-line manifest
67c4038230829b7b9abea540d78ec15af8f87aa66259c0c8b79873de6106251e
   the LIVE bytes now, 45 lines  (also what the 21:37Z postseal review records)
```

The 21:37Z postseal review's account is the accurate one.

I tested whether the growth was append-only:

```text
sha256(head -40) = 5893633f...   sha256(head -43) = ddc8ad0a...
sha256(head -41) = 04ae8bbe...   sha256(head -44) = 4fd77e91...
sha256(head -42) = 2fff2dac...   sha256(head -45) = 67c40382...
```

**Neither `324f4293...` nor `c66b1396...` is a prefix hash of the current
bytes.**  So the manifest was not merely appended to: existing entries were
also rewritten.  This is a small correction to any "grown by appending"
reading of the 21:37Z sentence.

### 6.2 Custody repair vs math-byte change — separated

Mtimes of every file named in the current manifest, against the coefficient
argument's dependency set:

```text
math bytes consumed by the BI-FACE argument
  RAW_INPUT.json                 07:42   hash unchanged, matches both reports
  compile_endpoint.py            12:12   hash unchanged, matches both reports
  RAW_DIRECT_SYSTEM.json         12:12   hash unchanged, matches both reports
  raw_direct*.sing / *.ms        12:12   all verify against the manifest
  compile_lf40.py / facepin_substitution.json / slot_census.json
                                         all verify, inside the 70af5634 freeze

bytes that changed after the BI-FACE audit
  launch_box03.sh                14:47   AWS launcher
  BOX02_PREFIX_QUOTIENT_AMENDMENT.md 15:24  preregistration amendment
  TERMINAL_CUSTODY.md            15:29   telemetry for two terminated pilots
  launch_box02_prefix.sh         15:29   AWS launcher
  run_aws.sh                     15:29   AWS runner
  SOURCE.sha256                  15:29   the manifest itself
```

Not one of the changed files is an input to the coefficient argument.
`TERMINAL_CUSTODY.md` is pure `time -v` / exit-status telemetry for two
memory-exhausted pilots and itself re-records `ead2fa40...` for
`RAW_DIRECT_SYSTEM.json`, unchanged.  **The growth is a custody repair, not a
mathematical repair.**  The 21:37Z characterization is CONFIRMED.

### 6.3 One custody GAP

The upper case directory contains **no source archive** (unlike the lower
case, which ships `GGV_8_28_LF40_v1_source_20260827.tar.gz` and
`..._targetfix_r1_...tar.gz`), and the case is untracked in git.  Therefore no
frozen copy of the `c66b1396...` or `324f4293...` manifest states exists
anywhere in the tree, and the manifest's history cannot be replayed.  Only the
*current* state is verifiable.

This is a **GAP**, not a defect: it is fully mitigated for this review by the
fact that all eight math-byte hashes match what *both* reports independently
recorded, so the coefficient argument's inputs are pinned from two directions
even though the manifest history is not.  It should be closed before the
upper case is promoted on its own account.

**Q4 verdict: CONFIRMED WITH ERRATUM (non-append-only growth) AND ONE GAP
(no replayable manifest history).**  The BI-FACE producer's custody
qualification was stale but was honestly flagged rather than silently
patched, which is the correct behaviour.

## 7. Errata against the two reports

```text
E1  producer §5: "None [of rho,a,b,z_d,tt_d] is a coordinate of the
    unrestricted raw-slot ring."  FALSE for z_d and tt_d: alpha_U is
    surjective (rank 17), with explicit raw preimages in §4.3 above.  TRUE
    for rho.  Verdict unaffected; the proof is actually shorter.
E2  producer §4: the "augmented row subtraction" presentation is the naive
    ideal sum its own §5 forbids.  Sound as a shorthand for the tensor
    identification, but should be written as such.
E3  producer §1: the manifest hash 324f4293/43 lines is stale; live is
    67c40382/45 lines.  Honestly flagged by the producer, corrected by the
    21:37Z review.
E4  21:37Z review §1: "has legitimately grown" is right in substance, but the
    manifest is not append-only - no prefix of the current bytes reproduces
    either earlier hash.
E5  both reports: the frozen fixture V=1 is a codimension-1 specialization
    (v_7=0) of the pinned branch-P family, and that is exactly the hypothesis
    the collision consumes.  Neither report identifies the criterion, and
    neither exhibits the compatible point that exists off it.  Their scope
    disclaimers are correct but understate how sharply the result is pinned.
```

None of E1–E5 changes the confirmed core claim.

## 8. Exact replay

Desk-scale, pure Python `fractions`, no external CAS, seconds to run.

```text
1  shasum -a 256 xmodel/ggv-8_28-bi-face-provenance-r0-sol-ultra-20260827.md \
       xmodel/ideation-20260827T2137Z-postseal-exact-hostile-review.md
2  shasum -a 256 -c cases/ggv_8_28_upper_endpoint_branch_p_20260827/SOURCE.sha256
       -> 45 lines, all OK
3  shasum -a 256 -c \
       cases/ggv_8_28_lower_facepin_lf40_v1_20260827/SOURCE_FREEZE_TARGETFIX_R1.sha256
       -> 48 lines, all OK
4  for n in 40..45: head -n $n SOURCE.sha256 | shasum -a 256
       -> no prefix equals 324f4293... or c66b1396...
5  lattice:  json.load(RAW_INPUT.json)["raw_slots_through_weight_22"]
       assert len(F)==141 and len(G)==301 and 442 distinct names
       assert weight == shift+3i-j and chart_image == "t^{w}*X^{i}" for all 442
       assert min(shift-4i+j) == 0 over all 442
6  upper census: A=[-1,0,0,0,1]; H=A^2; expand A^4, A^2, A^6, (3/2)A^4
       -> 20 fixed nonzero / 62 forced zero; +74 derived +286 live = 442
7  face relations: for each lower-weight-0 slot compare the frozen
       facepin_substitution.json entry against
       comb(14,i-2)*(-1)^(16-i) * a*rho^(16-i)   /   comb(21,i-3)*(-1)^(24-i) * b*rho^(24-i)
       -> 37 relations, 0 mismatches, all nonzero
8  surjectivity: build the 74 derived-slot images as affine forms in
       (z_0..z_6, tt_0..tt_9); exact Gaussian elimination -> rank 17 of 17
9  general-V: F1=HV, F2=(V^2+HZ)/4, F3=(VZ+AT)/8, G1=(3/2)H^2 V,
       G2=(3/2)H F2+(3/8)H V^2, G3=(3/2)H F3+(3/4)V F2-(1/16)V^3;
       evaluate D_0..D_3 by the compiler's recurrence -> identically zero;
       substitute v_7=-14rho, z_6=168rho^2, tt_9=-560rho^3, a=b=1
       -> all eight boundary rows match the face values
```

Step 9 is the load-bearing new computation; the general-`V` `G_1,G_2,G_3`
forms are **my derivation** from `G = F^(3/2)`, validated two independent
ways (they reduce exactly to the compiler's hardcoded `V=1` expressions, and
they annihilate `D_0..D_3` identically).  Steps 1–8 read only literal frozen
artifacts.

## 9. Promotion

The BI-FACE producer is **Sol Ultra** and the 21:37Z post-seal hostile review
is also **Sol Ultra** ("Reviewer: Sol Ultra, independent narrow review").
That pair does **not** satisfy the campaign's different-model promotion rule.
This Opus 5 cross-review supplies the missing different-model leg.

**Recommendation: yes, this may enter `AUDIT.md`** as
DIFFERENT-MODEL CONFIRMED WITH REPAIR, provided the entry states all of:

```text
1  the collision is exact and doubly frozen (facepin_substitution.json and
   desk_gate/facepin_derivation.json), and the tensor product is the zero ring;
2  alpha_U is surjective, so the upper fixed/linear fixture is a closed
   subscheme - correcting producer §5;
3  the licensed scope is the v_7 = 0 sublocus of branch-P crossed with the
   full lower (a,b,rho) torus - NOT the branch-P stratum;
4  for v_7 != 0 there is an explicit compatible point
   (a=b=1, v_7=-14rho, z_6=168rho^2, tt_9=-560rho^3), so no family separation
   may be asserted;
5  the separation is carried entirely by rho != 0;
6  the R0_ARTIFICIAL_CUSP_CONTROL firewall, including its own
   claims_not_made entry "8_28 face/family exclusion";
7  the upper manifest custody GAP of §6.3;
8  G2 must not be launched on this pair.
```

Suggested attribution line for the entry: producer SHA `18e3e299...`,
same-model review SHA `8bad7ca0...`, different-model Opus5 cross-review SHA
as printed on completion of this file.

## 10. Firewalls

This review decides only the provenance/compatibility question about two
frozen compiler fixtures over one frozen artificial control lattice.  It does
not validate either compiler's nonlinear ideal, does not decide any
determinant row, does not touch any live lane, and establishes **no** GGV
8_28 face or family exclusion, **no** Keller-pair statement, **no**
degree bound, and **no** JC2 consequence.
