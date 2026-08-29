# `BI-FACE-PROV-R0`: upper branch-P / lower LF40 coefficient provenance

**Date:** 2026-08-27  
**Lane:** Sol Ultra, bounded desk-scale gate  
**Scope:** fixed and linear coefficient layers only; no determinant-ideal
elimination and no solver verdict

## 0. Verdict

**Typed provenance passes, but fixed/linear compatibility fails
decisively.**  The two exact cases consume the same ordered 442-slot raw
lattice, and their unnormalized chart coefficient maps are deterministic
monomial regradings with no transpose.  The normalized case artifacts,
however, are parameter schemes mapping **to** that raw-slot scheme; the
canonical ring maps have variance

```text
R_raw -> U_lin,     R_raw -> L_lin,
```

not the proposal's unprovided maps `U_lin -> R_raw` and `L_lin -> R_raw`.
Consequently the typed simultaneous fixed/linear object is

```text
Spec(U_lin tensor_(R_raw) L_lin).
```

It is empty after the exact LF40 localization.  The first coefficient
collision is

```text
raw coefficient       f_15_52  of the ordered first component f,
raw monomial           x^15 y^52,
upper chart            u=8+3*15-52=1, coefficient [X^15]F_1=0,
lower chart            nu=8-4*15+52=0,
lower FACEPIN          [xi^15] a*xi^2*(xi-rho)^14=-14*a*rho,
lower guard            a*rho != 0.
```

Thus the union contains `f_15_52=0` and
`f_15_52+14*a*rho=0`; their difference is the unit `14*a*rho` in the
localized ring.  The independent second-component collision is
`g_23_80=0=-21*b*rho`, with `b*rho` inverted.  This is a **G1 FAIL / exact
separation**.  No nonlinear upper or LF40 determinant row is needed or
licensed, and G2 must not be launched.

## 1. Custody and boundary

The coefficient audit used only the named upper case, the named lower R1
case, their manifests, and their common raw-slot blob.  Relevant live-byte
hashes recomputed for this audit are:

```text
Upper
324f4293a8fae7baab2632f89d1274dc1b880a8708f34c2348e46a7f4fe915b7
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/SOURCE.sha256
7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/compile_endpoint.py
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json

Lower R1
70af56340845961625ce43945852da8f2350aa3d0a050532ca6138927d9c3298
  cases/ggv_8_28_lower_facepin_lf40_v1_20260827/SOURCE_FREEZE_TARGETFIX_R1.sha256
828f819e78ba36cf019e7014263148a4ee53ffd5b77ef77fee310637b82fc719
  cases/ggv_8_28_lower_facepin_lf40_v1_20260827/compile_lf40.py
bc61e6c33dc450664e1e83a98b9262210242c0713be005c78427161c3d6acc40
  cases/ggv_8_28_lower_facepin_lf40_v1_20260827/compiled/facepin_substitution.json
27de0604b07634c8c619585317ec0a183c1268494ed582ebf5a472be3ed3e841
  cases/ggv_8_28_lower_facepin_lf40_v1_20260827/compiled/slot_census.json

Common raw lattice
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
```

There is one custody qualification.  The 21:37Z packet records
`c66b1396...` as the complete upper source-manifest hash, but the current
`SOURCE.sha256` bytes hash to `324f4293...`; `c66b1396...` is not a prefix
hash of the current 43-line manifest.  I did not reconstruct or silently
substitute an older manifest.  The coefficient verdict above is therefore
stated for the individually named current artifacts at the hashes shown;
their entries and the common raw-input pin agree with the current manifests.
The lower R1 freeze itself matches its recorded `70af5634...` pin.

No AWS process was launched or inspected.  No nonlinear determinant ideal,
Groebner basis, or heavy algebra was run.  No canonical case file or prior
report was edited.  The separate `jc2-lean` tree was not entered, listed,
searched, read, status-inspected, or modified.

## 2. Global typed header

### 2.1 Ordered raw ring and component sort

Let

```text
R_raw = Q[f_i_j, g_i_j : the 442 slots listed in RAW_INPUT.json].
```

The order is literal and is retained on both sides:

```text
first component  f / F  lies on 2S,
second component g / G  lies on 3S.
```

The lower source's historical letters `P,Q` change meaning across its source;
the compiler's fail-closed rule is the polygon sort above.  The name
“branch-P” in the upper case denotes the factorization stratum `H=A^2`; it
does not authorize swapping polynomial components.  No signed transpose is
used anywhere in this audit.

The raw blob calls itself `R0_ARTIFICIAL_CUSP_CONTROL`.  Here only its exact
symbolic 2S/3S lattice is consumed, just as both compilers do.  It is not
promoted to a universal polynomial-pair scheme beyond that frozen support.

### 2.2 Exact chart pullbacks

For a raw monomial `x^i y^j`, the upper case uses

```text
F^U(t,X) = t^8  f(t^3 X,t^-1),
G^U(t,X) = t^12 g(t^3 X,t^-1),

f_i_j x^i y^j -> f_i_j t^(8+3i-j) X^i,
g_i_j x^i y^j -> g_i_j t^(12+3i-j) X^i.
```

Write the upper weights as

```text
u_F=8+3i-j,       u_G=12+3i-j.
```

The lower case uses the unflipped raw-coordinate chart

```text
x=tau^-4 xi,      y=tau,
F^L(tau,xi) = tau^8  f(tau^-4 xi,tau),
G^L(tau,xi) = tau^12 g(tau^-4 xi,tau),

f_i_j x^i y^j -> f_i_j tau^(8-4i+j) xi^i,
g_i_j x^i y^j -> g_i_j tau^(12-4i+j) xi^i.
```

Write the lower weights as

```text
nu_F=8-4i+j,      nu_G=12-4i+j.
```

Therefore every listed slot satisfies the exact cross-chart identities

```text
u_F+nu_F=16-i,    u_G+nu_G=24-i.
```

The 442 stored upper weights and all 442 independently recomputed lower
weights were checked directly against the raw blob.  This is a coefficient
regrading, not a translation and not a component swap.

### 2.3 Gauges, roots, orientation, and guards

Upper fixed gauge:

```text
A=X^4-1,  H=A^2,  F_0=H^2=A^4,  G_0=H^3=A^6,
F_1=H,    V=1,    c2=0.
```

There is no upper translation, auxiliary root, saturation, or nonconstant
denominator in the fixed/linear layer.  The rational denominators are units
over `Q`.  The later `Z,T` variables are private reduced-support lift
coordinates, not extra raw monomial coefficients.

Lower FACEPIN retains all gauges and the characteristic root:

```text
K_rho=xi*(xi-rho)^7,
F^L_0=a*K_rho^2=a*xi^2*(xi-rho)^14,
G^L_0=b*K_rho^3=b*xi^3*(xi-rho)^21.
```

There is no `xi -> xi+rho` coordinate translation: the displayed binomial is
expanded in the unchanged `xi` coordinate.  The source flip/unflip ledger is

```text
y*(x^4*y-rho)^7 -> x*(x*y^4-rho)^7
```

and the flip has Jacobian sign `-1`.  That sign explains the lower determinant
orientation `Dtil_17=-1` when `J(f,g)=1`; it does not change the coefficient
map above.  The exact lower localizer is

```text
s_L=a*b*rho*f_0_8*g_0_12,
```

implemented by `w*s_L-1`.  No other normalization or saturation factor is
licensed.

## 3. Sparse coefficient-provenance table

Each indexed family below is literal: every integer `i` in the stated range
denotes one compiler/raw slot.  Thus the table covers every slot touched by a
fixed or linear equation without printing 185 repetitive rows.  All other
listed raw coefficients are declared live at the end of this section;
coefficients outside the 442-slot support are **absent**, never zero.

Put

```text
Z=sum_(d=0)^6 z_d X^d,       T=sum_(d=0)^9 tt_d X^d.
```

For upper weight `u`, set

```text
I_F(u): max(0,ceil((u-8)/3)) <= i <= 16-u,   0<=u<=14,
I_G(u): max(0,ceil((u-12)/3))<= i <= 24-u,   0<=u<=21.
```

### 3.1 Upper fixed/linear and live families

| side / source row | ordered raw key and monomial | exact pullback into `U_lin` | state | chart / guard | cross-verdict |
|---|---|---|---|---|---|
| U / `F_0=A^4`, `i=0..16` | first component `f_i_(8+3i)`, `x^i y^(8+3i)` | `[X^i]A^4` | fixed at `i=0,4,8,12,16` with values `1,-4,6,-4,1`; all other `i` forced zero | upper chart, no guard | lower is live except boundary `i=16`; boundary gives `a=1` |
| U / `G_0=A^6`, `i=0..24` | second component `g_i_(12+3i)`, `x^i y^(12+3i)` | `[X^i]A^6` | fixed at `i=0,4,8,12,16,20,24` with values `1,-6,15,-20,15,-6,1`; all other `i` forced zero | upper chart, no guard | lower live except `i=24`; boundary gives `b=1` |
| U / `F_1=A^2`, `i=0..15` | `f_i_(7+3i)`, `x^i y^(7+3i)` | `[X^i]A^2` | fixed at `i=0,4,8` with `1,-2,1`; all other `i` forced zero | upper chart, no guard | lower live except `i=15`; boundary **collision** |
| U / `G_1=(3/2)A^4`, `i=0..23` | `g_i_(11+3i)`, `x^i y^(11+3i)` | `(3/2)[X^i]A^4` | fixed at `i=0,4,8,12,16` with `3/2,-6,9,-6,3/2`; all other `i` forced zero | upper chart, no guard | lower live except `i=23`; boundary **collision** |
| U / `F_2`, `i=0..14` | `f_i_(6+3i)`, `x^i y^(6+3i)` | `(1/4)[X^i](1+A^2 Z)` | affine-derived | upper chart; `z_0..z_6` private | lower live except `i=14`; boundary equation `z_6/4=91a rho^2` |
| U / `G_2`, `i=0..22` | `g_i_(10+3i)`, `x^i y^(10+3i)` | `[X^i](3A^2/4+3A^4 Z/8)` | affine-derived | upper chart; `z_0..z_6` private | lower live except `i=22`; boundary equation `3z_6/8=210b rho^2` |
| U / `F_3`, `i=0..13` | `f_i_(5+3i)`, `x^i y^(5+3i)` | `(1/8)[X^i](Z+A T)` | linear-derived | upper chart; `z_d,tt_d` private | lower live except `i=13`; boundary equation `tt_9/8=-364a rho^3` |
| U / `G_3`, `i=0..21` | `g_i_(9+3i)`, `x^i y^(9+3i)` | `[X^i](1/8+3A^2 Z/8+3A^3 T/16)` | affine-derived | upper chart; `z_d,tt_d` private | lower live except `i=21`; boundary equation `3tt_9/16=-1330b rho^3` |
| U / `F_u`, `4<=u<=14`, `i in I_F(u)` | `f_i_(8+3i-u)` | the same named raw variable | live | upper chart, no guard | lower live unless `i=16-u`; at that boundary LF40 gives the specialization in §3.3 |
| U / `G_u`, `4<=u<=21`, `i in I_G(u)` | `g_i_(12+3i-u)` | the same named raw variable | live | upper chart, no guard | lower live unless `i=24-u`; at that boundary LF40 gives the specialization in §3.3 |

This accounts for the whole raw lattice on the upper side:

```text
20 fixed nonzero + 62 forced zero + 74 affine/linear-derived + 286 live
= 442 raw slots.
```

The 17 private variables `z_0..z_6,tt_0..tt_9` have no independent raw
monomial key.  Their typed role is to parameterize the graph of the 74
derived assignments above.  Treating them as additional coefficients of the
raw pair would be a type error.

### 3.2 Lower fixed and live families

For lower row `nu`, define

```text
J_F(nu): max(0,ceil((8-nu)/4))  <= i <= 16-nu,  0<=nu<=16,
J_G(nu): max(0,ceil((12-nu)/4)) <= i <= 24-nu,  0<=nu<=24.
```

| side / source row | ordered raw key and monomial | exact pullback into `L_lin` | state | chart / guard | cross-verdict |
|---|---|---|---|---|---|
| L / FACEPIN `F^L_0`, `i=2..16` | first component `f_i_(4i-8)`, `x^i y^(4i-8)` | `a*(-1)^(16-i)*C(14,i-2)*rho^(16-i)` | fixed by face shape | lower chart; `a,rho` inverted | exact boundary comparison in §3.3 |
| L / FACEPIN `G^L_0`, `i=3..24` | second component `g_i_(4i-12)`, `x^i y^(4i-12)` | `b*(-1)^(24-i)*C(21,i-3)*rho^(24-i)` | fixed by face shape | lower chart; `b,rho` inverted | exact boundary comparison in §3.3 |
| L / `F^L_nu`, `1<=nu<=16`, `i in J_F(nu)` | `f_i_(nu-8+4i)` | the same named raw variable | live | lower chart; `f_0_8` additionally inverted | identical raw key; accepts every upper assignment |
| L / `G^L_nu`, `1<=nu<=24`, `i in J_G(nu)` | `g_i_(nu-12+4i)` | the same named raw variable | live | lower chart; `g_0_12` additionally inverted | identical raw key; accepts every upper assignment |

The lower census is exactly

```text
15 fixed F-face + 22 fixed G-face + 126 live F + 279 live G = 442.
```

Every one of the 37 face coefficients is nonzero under the declared guard.
There are no lower forced-zero slots inside the listed support.  The solver's
`w` is only a Rabinowitsch witness for the localizer and is not a raw or
compiler coefficient.

### 3.3 Complete boundary cross-table

The 37 lower fixed slots are exactly the upper-window boundary slots.  Using
`u` as their upper weight gives all 37 rows in two sparse indexed families:

| component / rows | ordered raw key | upper expression / state | lower expression / state | guard | cross-verdict |
|---|---|---|---|---|---|
| F, `u=0` | `f_16_56` | `1`, fixed | `a`, fixed | `a!=0` | compatible equation `a=1` |
| F, `u=1` | `f_15_52` | `0`, forced zero | `-14a rho`, fixed | `a rho!=0` | **collision** |
| F, `u=2` | `f_14_48` | `z_6/4`, derived | `91a rho^2`, fixed | `a rho!=0` | compatible equation by itself; moot after `u=1` |
| F, `u=3` | `f_13_44` | `tt_9/8`, derived | `-364a rho^3`, fixed | `a rho!=0` | compatible equation by itself; moot after `u=1` |
| F, each `4<=u<=14` | `f_(16-u)_(56-4u)`, monomial `x^(16-u)y^(56-4u)` | same named upper live raw coefficient | `a*(-1)^u*C(14,u)*rho^u`, fixed | `a rho!=0` | compatible specialization by itself |
| G, `u=0` | `g_24_84` | `1`, fixed | `b`, fixed | `b!=0` | compatible equation `b=1` |
| G, `u=1` | `g_23_80` | `0`, forced zero | `-21b rho`, fixed | `b rho!=0` | **collision** |
| G, `u=2` | `g_22_76` | `3z_6/8`, derived | `210b rho^2`, fixed | `b rho!=0` | compatible equation by itself; moot after `u=1` |
| G, `u=3` | `g_21_72` | `3tt_9/16`, derived | `-1330b rho^3`, fixed | `b rho!=0` | compatible equation by itself; moot after `u=1` |
| G, each `4<=u<=21` | `g_(24-u)_(84-4u)`, monomial `x^(24-u)y^(84-4u)` | same named upper live raw coefficient | `b*(-1)^u*C(21,u)*rho^u`, fixed | `b rho!=0` | compatible specialization by itself |

The indexed F tail represents 11 separate rows and the indexed G tail 18,
so the table represents `4+11+4+18=37` fixed LF40 coefficients exactly.
All other cross-states are:

```text
148 upper fixed/derived slots  x lower live slots: compatible identity;
257 upper live slots           x lower live slots: same raw variable, unused;
29  upper live slots           x lower fixed slots: the tail specializations above.
```

The omitted upper `G_22` and every coefficient outside the raw support are
absent.  They are not silently forced to zero.

## 4. Exact linear consistency and guard replay

Over the exact coefficient field `Q(a,b,rho)` the first F-slot subsystem has
augmented rows

```text
f_15_52             = 0,
f_15_52             = -14*a*rho.
```

One row subtraction gives

```text
0 = -14*a*rho.
```

In `L_lin`, `a*rho` is a unit; characteristic zero makes `14` a unit.  This
is already a one-step exact row-reduction certificate of inconsistency.  The
parallel G rows give `0=-21*b*rho`, independently inconsistent.

The remaining localizer factors do not create an escape:

```text
upper f_0_8=[X^0]A^4=1,
upper g_0_12=[X^0]A^6=1.
```

Hence `f_0_8` and `g_0_12` replay as nonzero, while the coefficient union
forces the separately inverted product `a*rho` (and also `b*rho`) to zero.
Equivalently, the exact localized fixed/linear ring is the zero ring.

There are later redundant contradictions.  For example, `u=0` gives
`a=b=1`, while the `u=2` equations give both

```text
z_6=364*rho^2,       z_6=560*rho^2.
```

Since `rho` is invertible these are incompatible as well.  They are not
needed for the stop verdict; `f_15_52` is the first raw coefficient
collision.

## 5. Variance and the first type obstruction

The two artifacts do supply a common raw **slot lattice** and deterministic
unnormalized chart regradings.  They do not supply a globally deterministic
map from an arbitrary raw pair to each normalized case coordinate ring.

Define the actual fixed/linear parameter algebras by

```text
U_lin = Q[z_0..z_6,tt_0..tt_9, the 286 upper-live raw slots],

L_lin = Q[a,b,rho, the 405 lower-live raw slots]_[s_L^-1],
s_L   = a*b*rho*f_0_8*g_0_12.
```

The tables in §3 are canonical ring maps

```text
alpha_U: R_raw -> U_lin,
alpha_L: R_raw -> L_lin.
```

Geometrically they are the source maps

```text
Spec(U_lin) -> Spec(R_raw) <- Spec(L_lin).
```

This is the usual parameter-to-source variance.  The first type obstruction
to reversing it is already visible before any equation comparison: `rho` is
an auxiliary choice of the full-multiplicity nonzero lower characteristic
root, while `a,b` are face scales and `z_d,tt_d` are private upper lift
coordinates.  None is a coordinate of the unrestricted raw-slot ring.  On
the lower FACEPIN image one can recover, for example,

```text
a=f_16_56,       rho=-f_15_52/(14*f_16_56),
```

but that formula presupposes the face open and its other 35 graph equations;
it is not a compiler morphism on all of `Spec(R_raw)`.  Likewise, extracting
upper `Z,T` from selected raw coefficients does not impose the remaining
reconstruction equations.  The upper parametrization is explicitly only
the reduced geometric branch support, not the natural nonreduced coefficient
scheme.  An arbitrary reverse projection would therefore forget precisely
the image conditions this audit must test.

Accordingly, for later nonlinear ideals `I_U` and `I_L` the typed object
would be

```text
U=(A_U/I_U)_[s_U^-1],       L=(A_L/I_L)_[s_L^-1],
X_bi=Spec(U tensor_(R_raw) L),
```

with every private lift and guard retained.  Contracting two ideals into
`R_raw` or merely adding equations after an arbitrary reverse projection is
not equivalent to that fibre product.  At the present fixed/linear stage,

```text
U_lin tensor_(R_raw) L_lin = 0
```

by §4, so no nonlinear fibre product should be constructed.

## 6. Gate disposition

```text
G0a  common ordered raw support and chart coefficient provenance    PASS
G0b  proposed deterministic normalized raw->compiler variance       FAIL/RETYPE
G1   localized fixed/linear compatibility                            FAIL
G2   full nonlinear localized fibre product                          NOT RUN
```

This separates the exact upper branch-P endpoint fixture from the exact
lower LF40 FACEPIN fixture at coefficient level.  It does not invalidate
either compiler in isolation, does not use or disturb any live solver lane,
does not decide either nonlinear ideal, and has no family-landing, Keller,
degree-bound, or JC2 consequence.  Its only promoted conclusion is the one
the provenance gate was designed to supply: these two frozen normalized
fixtures cannot be the two faces of one point of their shared ordered raw
slot scheme.
