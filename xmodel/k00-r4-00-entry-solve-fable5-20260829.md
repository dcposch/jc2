# K00 V20R2 valuation four, packet `R4-00`: exact entry solve, T-fan split, and grade-13..19 continuation

Author: Fable 5 (exact primary research lane)
Date: 2026-08-29 UTC
Basis commit: `31777ce90994a106aade85064c0d868e32863f94`
Lifecycle: `PROVISIONAL_EXACT_DESK_THEOREM_PLUS_TYPED_OPEN_RESIDUALS / DIFFERENT-MODEL REVIEW REQUIRED`

Consumed reviewed pair (hashes verified at run time on the basis):

```text
be37360e22524c0f5e7a739753c237c3c94f71f0b5d44bfd9dcd89dddade134a
  xmodel/k00-r4-jetfan-provisional-sol56-20260829.md   (producer; body 3bb710d3...)
2ce2e4bfd9c23564a8e2be66437772d1cb9855ece4ebaf8ee37b005436c4ff43
  xmodel/k00-r4-jetfan-hostile-review-fable5-20260829-r1.md
  (this lane's hostile review; body 220569e13dd5fbd14baffb53951992dbacbf5975e3c5a91795dced556ccf09d0)
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
```

## 0. Result

Work over an arbitrary characteristic-zero field on the exact normalized
V20R2 source (`C0=(1+d0)/256, C1=d1, C2=(1+d2)/16, C3=d3, C4=(3+d4)/8,
C5=d5, C6=1`; loads `Lambda^2 k10`, `Lambda^6 k6`, `Lambda^10 k2`; targets
`-Lambda^14 mu2` row 2, `-Lambda^16 mu4` row 4, `-Lambda^18 mu6` row 6,
`-(Lambda^19/4) Jdet` row 7; truncation `Lambda^20`), on the `R4-00` packet

```text
d = Lambda^4 x + Lambda^5 y + Lambda^6 z + ...,  x = ell(s,t) != 0,
y = ell(s1,t1),   ell(s,t) = (2s, t/8, s, t, s, 2t),
C6=1, kappa := k10[0] != 0, k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0, Jdet[0] != 0,
```

with every literal coefficient equation `G_i,n = 0` (`1<=i<=7`, `8<=n<=19`)
imposed.  All seven rows were rebuilt from the frozen 569 tails and the
frozen compiler conventions in a clean-room stdlib pipeline (Section 2); no
producer replay code or output was used as an oracle.

1. **Grade-12 entry solved exactly (Section 3).**  Over the full
   `(s,t,s1,t1,kappa)` base, without radical replacement, normalization, or
   chart choice, the literal six-live-row affine-quadratic system
   `Q(z)+kappa*polar_M2(x,z)=0` has solution set exactly the reduced cone
   `A(z)=B(z)=0`: two explicit Q-linear combinations of the literal rows
   equal `(3/16384)*A(z)B(z)` and `(3/524288)*(B(z)^2-64A(z)^2)`, and
   `A(z)^3, B(z)^3` lie in the row ideal by displayed multipliers.  The
   solution is one irreducible component, a rank-4 affine bundle; `s1, t1`
   and the cone coordinates `az, bz` of `z` are inert in the entry system.
2. **The next linearization is a constant-matrix ladder (Section 4).**  With
   `z = cone(az,bz,uz,vz)` on the cone, for every grade `n = 13..19` the
   newest jet `(A_{n-6}, B_{n-6})` enters all seven rows through one fixed
   matrix `T = (1/2048)*[[p, q], [-4q, p/16]]`, `p = 6uz+5*kappa*s`,
   `q = -6vz+5*kappa*t` (rows 3,5,7 are `-1/8, -1/128, -1/1024` times row 1;
   rows 4,6 zero).  The complete reduced rank fan of `T` is the
   kappa-shifted copy of the leading fan: rank 2 on `D := p^2+64q^2 != 0`,
   rank 1 on `D = 0, (p,q) != (0,0)` (nonempty only over fields containing
   `i`), rank 0 exactly at `p = q = 0`.
3. **Universal ladder collapse (Section 5).**  On every cell: grade 13 is
   exactly `T*(A7,B7)=0`; the grade-14 cokernel combos are the pure pair
   `(3/16384)A7B7`, `(3/524288)(B7^2-64A7^2)` forcing `A7=B7=0` over any
   field; the grade-15 combos then vanish identically; through grade 17 the
   three c-combos stay exactly proportional (`c51=-c31/8, c71=-c31/128`);
   the second-level defects first live at grade 18; grade 19 defines
   `mu6[1], mu4[3], Jdet[0]` and converts the source open `Jdet[0]!=0` into
   the survival open of the residual.
4. **Cell `p=q=0` (rank 0) is EMPTY — exact desk theorem (Section 6).**
   Grade-14 rows force the base onto three explicit rays; on each ray the
   grade-16 combos are again the pure certificate pair, forcing `A8=B8=0`;
   then row 6 at grade 18 is the exact unit `(5kappa/3)^9/2^19` (rational
   ray) or `(5kappa/3)^9/2^20` (conjugate rays), nonzero under `kappa!=0`.
   An end-to-end control confirms the unit on the pristine rows with all
   other window unknowns random.
5. **Cell rank 1 (Section 7)** reduces over `Q(i)` to one closed grade-14
   base cubic `F2' - 8*eps*i*t*F1' = 0` plus a four-line concurrency and a
   two-conic membership in the `(A8,B8)`-plane: five conditions on four base
   unknowns.  Typed `OPEN`; 553 nondegenerate numeric probes of two square
   subsystems produced zero full-system points (numeric indication of
   emptiness, not a claim).
6. **Cell rank 2 (Section 8)** reduces to five closed base conditions
   `X1,X2,X3,X4,X5` on `(s,t,uz,vz,kappa)` (all further window conditions
   carry fresh jet/load/target absorbers).  Exact Gaussian-rational Newton
   reaches residual `3*10^-14` at points with `D != 0` where the Jacobian of
   `{X1,X2,X3,X4}` has rank 2 — strong numeric indication of a
   positive-dimensional surviving base component, with the observed on-locus
   dependence `X5 = X4/8`.  Typed `OPEN`; serialized with canonical digest;
   the exact base-locus decision is the cheapest successor.

No nonemptiness of `R4-00` or of any cell is asserted.  Formal jets are not
arcs or maps; no periodicity, attainment, maximum-12, or JC2 claim is made.

## 1. Inputs, custody, firewall

All four pinned hashes above verified byte-exact at run time.  Work used
only Python 3 standard library with exact `Fraction` (and exact
Gaussian-rational) arithmetic; scratch confined to `/tmp/k00r400/`; no
Singular, no AWS job, no web request, no external model, no `jc2-lean`
access, no git operation.  This report is the only repository file written.
Frozen sources were reconstructed directly; the producer replay was neither
imported nor executed by this lane.

## 2. Clean-room reconstruction and controls

A sparse multivariate polynomial engine over Q expands the seven rows as
`Lambda`-series truncated at `Lambda^20` directly from `tails.json`
(10-slot exponent vectors `C0..C6,k10,k6,k2`, weights `8..2,2,6,10`, row
weight `12+ell`, per-tail load linearity, 569-term census re-verified) under
the frozen coordinate map, load shifts, and target rows re-read from the
frozen compiler.  Stratum substitution: `d4 = ell(s,t)`, `d5 = ell(s1,t1)`,
`d6..d15` free 6-vectors in the adapted coordinates

```text
q = cone(a,b,u,v) + (B,0,0,0,0,A),  cone(a,b,u,v) = (2b+2u, a, b, 8a+v, b-u, 16a+4v),
A(q) = 16q1-4q3+q5,  B(q) = q0-4q2+2q4,   ell(s,t) = cone(t/8, s, 0, 0),
```

loads `k10 = kappa + k10_1 L + .. + k10_11 L^11`, `k6 = k6_1 L + .. + k6_9 L^9`,
`k2 = k2_1 L + .. + k2_5 L^5`, targets `mu2_1..5, mu4_1..3, mu6_1, Jdet_0`.

Verified structural facts (each an exact polynomial identity of the rebuilt
rows): grades 0–7 of all rows vanish identically; the `k10`-shift
consistency (the `k10_1`-marked pieces at grades 11/15/19 equal the
`kappa`-marked pieces at 10/14/18); the adapted decomposition
`Q_i = alpha_i(u,v)A + beta_i(u,v)B + q_i(A,B)` with

```text
alpha_1 = (3/1024)u,    beta_1 = -(3/1024)v,    q_1 = -(3/2048)AB,
alpha_2 = (3/256)v,     beta_2 = (3/16384)u,    q_2 = (15/2048)A^2,
q_3 = (3/8192)AB,  q_4 = (3/524288)B^2-(3/8192)A^2,  q_5 = -(3/262144)AB,
q_6 = 0,  q_7 = 0,   rows 3,5,7 alpha/beta = (-1/8,-1/128,-1/1024)*row 1,
rows 4,6 alpha=beta=0,   det[row1;row2] = (9/16777216)*(u^2+64v^2);
```

the `M2` image identity `M2cone_i = alpha_i*(-10v/3)+beta_i*(10u/3)`; the
old-plane cross forms of `M2` (`polar_M2_i(ell(s,t), q) = lc_i*A(q)+mc_i*B(q)`)

```text
lc_1 = (5/2048)s,  mc_1 = (5/2048)t,   lc_2 = -(5/512)t,  mc_2 = (5/32768)s,
rows 3,5,7 = (-1/8,-1/128,-1/1024)*row 1,   rows 4,6 = 0;
```

`N1 = (3/64, 3/1024*B-dir, -3/512, 0, -3/8192, 0, -3/65536)`-vector in
`(A,B)` only, killed by all five universal combos; `C3_i`, `M3_i`, `N2_i`,
`P1_i` vanish or are combo-killed on the old plane; `C4_i|plane` is NOT
combo-killed (its arrivals drive grade 16).  Producer §4.1/§4.2 cross-checks
reproduce exactly (e.g. `c31[C3|cone]` at `u=0` equals `(1/4)v^2(v+3a)`).

Controls performed in this lane: (i) hash gates on all four inputs; (ii)
569/weight/linearity census; (iii) constant-term and shift consistency as
above; (iv) negative control — mutating the row-4 tail `[0,0,0,0,0,2,5,0,0,0]`
(coefficient `-63/1024`) by `+1` breaks the `q_4` certificate form by the
displayed nonzero defect; (v) end-to-end positive control of the Section-6
kill (below).  Earlier grades replayed independently: on the full `R4-00`
stratum with all jets `d6..d15` free, all loads and targets symbolic, grades
0–11 of all seven rows vanish identically, grade 12 equals
`Q_i(z)+kappa*polar_M2_i(x,z)` exactly with row 6 identically zero, and the
columns `d[14], d[15], k10[10], k10[11]` are absent from the entire window.

## 3. The grade-12 entry system, solved exactly

The literal six live rows over the full base (variables of `z` in adapted
coordinates `az,bz,uz,vz,Az,Bz`; `az,bz,s1,t1` do not occur):

```text
G1 = (5/2048)kappa(s*Az+t*Bz) + (3/1024)(uz*Az-vz*Bz) - (3/2048)Az*Bz
G2 = (5/32768)kappa*s*Bz - (5/512)kappa*t*Az + (3/16384)uz*Bz + (3/256)vz*Az + (15/2048)Az^2
G3 = -(1/8)[(5/2048)kappa(s*Az+t*Bz) + (3/1024)(uz*Az-vz*Bz)] + (3/8192)Az*Bz
G4 = -(3/8192)Az^2 + (3/524288)Bz^2
G5 = -(1/128)[same bracket] - (3/262144)Az*Bz
G7 = -(1/1024)[same bracket]
```

**Certificates (exact, over the full base, any coefficient field):**

```text
G3 + (1/8)G1   = (3/16384)Az*Bz
G5 + (1/128)G1 = -(3/131072)Az*Bz
G7 + (1/1024)G1 = -(3/2097152)Az*Bz
G4             = (3/524288)(Bz^2 - 64Az^2)
Az^3 = (1/64)[ Bz*(16384/3)(G3+G1/8) - Az*(524288/3)G4 ]
Bz^3 = Bz*(524288/3)G4 + Az*(1048576/3)(G3+G1/8)
```

Hence field-valued solutions satisfy `Az*Bz = 0` and `Bz^2 = 64Az^2`, which
force `Az = Bz = 0` over any field; conversely every row lies in the ideal
`(Az,Bz)`.  **The exact solution set is the reduced-cone bundle
`{z = cone(az,bz,uz,vz)}`**, one irreducible component, valid at every base
point including all zero branches (`s=0`, `t=0`, `z=0`, `s1,t1` arbitrary);
no radical replacement or normalization was used, and the certificate is a
literal Q-linear-combination identity, not a Groebner normal form.  The
literal row ideal is a proper subideal of `(Az,Bz)` (radical equal by the
cube certificates); field-valued jets see only the common zero set, so the
continuation below is exact for the packet's field-valued equations, and no
scheme-theoretic (nilpotent) claim is made.

## 4. The next linearization and its complete reduced rank fan

On the solved locus (`z` on the cone), for every `n = 13..19` the top jet
`(A_{n-6}, B_{n-6})` occurs in all seven rows exactly through

```text
row1: (1/2048)( p*A + q*B ),        row2: (1/2048)( -4q*A + (p/16)B ),
row3 = -(1/8)row1,  row5 = -(1/128)row1,  row7 = -(1/1024)row1,  rows 4,6 = 0,
p = 6uz + 5*kappa*s,   q = -6vz + 5*kappa*t,   det T = (p^2+64q^2)/2^26,
```

verified as an exact identity of the rebuilt rows at every grade 13–19, and
grade 13 is exactly `T*(A7,B7) = 0` with zero remainder.  The fan of `T`:

```text
CELL-R2:  D = p^2+64q^2 != 0            (rank 2)
CELL-R1:  D = 0, (p,q) != (0,0)         (rank 1; requires i: p = ±8i*q)
CELL-R0:  p = q = 0, i.e. uz = -(5/6)kappa*s, vz = (5/6)kappa*t   (rank 0)
```

These three constructible cells are disjoint and exhaust the solved locus.
The weighted scaling (`s,t:4; s1,t1:5; kappa:2; az..vz:6; d_m:m;
k10_j:2+j; k6_j:6+j; k2_j:10+j; mu2_j:14+j; mu4_j:16+j; mu6_1,Jdet_0:19`)
makes every displayed object homogeneous; `G_i,n` has weight `n`.

## 5. Universal ladder facts (grades 13–19, all cells)

With the five universal cokernel combos `c31 = G3+G1/8`, `c51 = G5+G1/128`,
`c71 = G7+G1/1024`, `row4`, `row6` (they kill the `T`-image identically):

1. Grade 13: all five combos identically zero; content is `T*(A7,B7)=0`.
2. Grade 14 combos are exactly `(3/16384)A7B7`, `-(3/131072)A7B7`,
   `-(3/2097152)A7B7`, `(3/524288)(B7^2-64A7^2)`, `0` — no inhomogeneity at
   all (every candidate inhomogeneity is combo-killed on this stratum).
   Hence **`A7 = B7 = 0` on every cell**, by the same two-line certificate.
3. Grade-15 combos vanish identically after `A7=B7=0`.
4. Grades 16–17: `c51 = -(1/8)c31` and `c71 = -(1/128)c31` exactly; row 6
   identically zero; so the closed content is `c31@16, row4@16, c31@17`
   (`row4@17` defines `mu4_1`).
5. Grade 18: second-level defects go live: `D51 := c51+(1/8)c31` (19 terms)
   and `D71 := c71+(1/128)c31` (18 terms) are nonzero and involve only
   `(s,t,kappa,uz,vz,A8,B8)`; `row6@18` (21 terms) likewise; `row4@18`
   defines `mu4_2`; `c31@18` carries fresh absorbers (`A10,B10, az,bz,
   a7,b7,u8,v8, k10_2,k6_2,k2_2, mu2-feedback`).
6. Grade 19: `row4@19 -> mu4_3`, `row6@19 -> mu6_1`, and
   `c71@19 + (1/128)c31@19` contains `-Jdet_0/4` linearly, so grade 19
   **defines** `Jdet_0 = 4*[D71@19 nontarget part]` and converts the source
   open `Jdet_0 != 0` into the residual's survival open; `c31@19, D51@19`
   remain imposed with fresh absorbers (`k2_1*A8, k6_1*uz*vz, u7,v7, A9,B9,
   s1,t1, mu2-feedback`).
7. Rows 1,2 at grades 14–19 are the `T`-solves of the top jets; row 2 at
   grades 15–19 contains `-mu2_{n-14}` so the free targets `mu2_1..5`
   parametrize the solve line on rank-deficient cells and ride inside the
   rank-2 solve.  The grade-14 row remainders are pure base polynomials:

```text
I1@14 = -(3/512)st*uz - (15/4096)s^2 t*kappa + (3/1024)s^2 vz - (3/16)t^2 vz
        + (5/64)t^3 kappa - (5/256)kappa*uz*vz
I2@14 = -(3/128)st*vz + (15/1024)s t^2 kappa - (3/16384)s^2 uz - (5/65536)s^3 kappa
        + (3/256)t^2 uz + (5/8192)kappa*uz^2 - (5/128)kappa*vz^2
```

8. The three grade-18 conditions pair with the grade-16 conics into affine
   **lines** in the `(A8,B8)`-plane:

```text
L18 := row6@18 - (5kappa/12)*row4@16 = LA*A8 + LB*B8 + LC,
LA = -(5/16384)st*kappa - (3/8192)s*vz + (3/8192)t*uz - (25/12288)kappa^2 vz
LB = -(3/524288)s*uz + (5/2097152)s^2 kappa - (3/8192)t*vz - (5/32768)t^2 kappa
     - (25/786432)kappa^2 uz
LC = (25/4096)st*kappa^2 vz - (9/8192)s t^2 uz + (9/8192)s^2 t vz + (15/65536)s^2 t^2 kappa
     + (25/524288)s^2 kappa^2 uz + (3/524288)s^3 uz - (5/8388608)s^4 kappa
     - (25/8192)t^2 kappa^2 uz - (3/128)t^3 vz - (5/2048)t^4 kappa
     + uz(192vz^2-uz^2)/65536
L51 := D51@18 - (5kappa/12)*c31@16   (affine-linear in (A8,B8))
L71 := D71@18 + (5kappa/96)*c31@16   (affine-linear in (A8,B8))
```

(the row-6 cone cubic reappears inside `LC`).  Inert affine factors of the
whole window on the solved stratum (absent from every equation after the
forced `A7=B7=0`): `a10..a13, b10..b13, u12,v12,u13,v13, k10_6..k10_9,
k6_6..k6_9`, plus the parametrized-away `Az,Bz,A7,B7` and the dropped
columns `d[14], d[15], k10[10], k10[11]`.

## 6. CELL-R0 (`p = q = 0`) is empty: exact grade-18 unit kill

On `uz = -(5/6)kappa*s, vz = (5/6)kappa*t` the matrix `T` vanishes, so the
grade-14 rows 1,2 are closed conditions.  Exactly:

```text
I1@14|R0 = (5/36864)*kappa*t*F1,   F1 = 27s^2 + 100s*kappa^2 - 576t^2,
I2@14|R0 = (5/589824)*kappa*F2,    F2 = 9s^3 + 50s^2 kappa^2 - 1728s t^2 - 3200 t^2 kappa^2,
576*F2 - (1728s+3200kappa^2)*F1 = -512*s*(9s+25kappa^2)^2   (polynomial identity).
```

With `kappa != 0` and `(s,t) != (0,0)` this forces exactly three rays:

```text
P0:  (s,t) = (-50kappa^2/9, 0),                    uz = (125/27)kappa^3, vz = 0;
P±:  (s,t) = (-25kappa^2/9, ±(25i/72)kappa^2),     uz = (125/54)kappa^3,
     vz = ±(125i/432)kappa^3      (only over fields containing i;
     over fields without i the t != 0 branch is empty at grade 14).
```

On each of the three rays the grade-16 combos are again exactly the pure
pair `c31@16 = (3/16384)A8B8`, `row4@16 = (3/524288)(B8^2-64A8^2)` (all
affine parts cancel on the rays), forcing `A8 = B8 = 0`.  Then row 6 at
grade 18 evaluates to the exact units

```text
row6@18|P0 = (1953125/10319560704)*kappa^9 = (5kappa/3)^9 / 2^19  != 0,
row6@18|P± = (1953125/20639121408)*kappa^9 = (5kappa/3)^9 / 2^20  != 0,
```

with no target on row 6 before grade 19 and no remaining freedom in the
equation.  **CELL-R0 is empty over every characteristic-zero field.**  Every
forcing used is itself an imposed packet equation (grade 12 certificates,
grade 14 combos, grade 14 rows, grade 16 combos), so the kill is
order-independent.  End-to-end control: on the pristine seven-row expansion
(nothing pre-reduced), at `kappa=3`, `s=-50, t=0, uz=125, vz=0`,
`Az=Bz=A7=B7=A8=B8=0` and **all ~90 remaining window unknowns independently
random rationals**, `G_6,18 = 1953125/524288` exactly (`= (5*3/3)^9/2^19`),
while `G_6,8..17`, rows 1–5,7 at grade 14, and the grade-16 combos all
vanish — confirming the unit is blind to every jet, load, and target
freedom.

```text
CERTIFICATE R4-00-R0 EMPTY v1
CELL p=q=0 : uz=-(5/6)*kappa*s ; vz=(5/6)*kappa*t
STEP1 grade14 rows: kappa*t*F1=0 ; kappa*F2=0 ; F1=27*s^2+100*s*kappa^2-576*t^2 ; F2=9*s^3+50*s^2*kappa^2-1728*s*t^2-3200*t^2*kappa^2
STEP2 identity 576*F2-(1728*s+3200*kappa^2)*F1=-512*s*(9*s+25*kappa^2)^2 ; opens kappa!=0,(s,t)!=(0,0) => rays P0=(-50*kappa^2/9,0) ; Ppm=(-25*kappa^2/9,+-(25*i/72)*kappa^2)
STEP3 on P0,Ppm grade16 combos: G3+G1/8=(3/16384)*A8*B8 ; G4=(3/524288)*(B8^2-64*A8^2) => A8=B8=0
STEP4 row6 grade18 = (5*kappa/3)^9/2^19 on P0 ; = (5*kappa/3)^9/2^20 on Ppm ; nonzero
CONCLUSION CELL-R0 EMPTY over every characteristic-zero field at grade 18
```

Canonical digest (SHA-256 of the fenced block content above, first line
`CERTIFICATE...` through last line `CONCLUSION...`, one trailing newline):
`56b3ca0a32773d69eebe798a6a9d1de4e9f50b091ba0549b40794ffa7620d2b9`.

## 7. CELL-R1 (`D = 0`, `(p,q) != (0,0)`): typed OPEN residual over Q(i)

Branches `p = 8*eps*i*q`, `eps = ±1`, `q != 0`; parametrize
`uz = (8*eps*i*q - 5*kappa*s)/6`, `vz = (5*kappa*t - q)/6`.  On the branch
`T_2 = (eps*i/2)T_1`, so row 1 solves `B_m = -2048*I1@n/q - 8*eps*i*A_m`
(each `A_m` a kernel freedom) and the sixth combo `c21' := G2 - (eps*i/2)G1`
is closed at grade 14 and absorbs `mu2_{n-14}` at grades 15–19.  Exactly:

```text
c21'@14 = (5*kappa/589824) * [ F2 - 8*eps*i*t*F1 ]        (q cancels),
```

with `F1, F2` from Section 6.  The remaining closed content through grade 18
is carried entirely by the `(A8,B8)`-plane geometry: the point `(A8,B8)`
must lie on the four lines `row1@14`, `L18`, `L51`, `L71` and on the two
conics `c31@16`, `row4@16` (all listed literally in Section 5 / below).
Equivalently: `c21'@14 = 0`, two concurrency minors
`M1 = det3(row1,L18,L51)`, `M2 = det3(row1,L18,L71)` vanish, and the two
conic values at the pinned point vanish — five closed conditions on the four
base unknowns `(s,t,kappa,q)`.  Grades 17–19 impose `c31@17, c31@18,
c31@19, D51@19` with fresh absorbers (`A9..A11`, cone parts, `k10_2..`,
`k6_*`, `k2_*`, `mu2`-feedback), `row4@17..19 -> mu4_1..3`,
`row6@19 -> mu6_1`, `D71@19 -> Jdet_0` with open `!= 0`.

Numeric status (guide only, not evidence for promotion): 488 distinct
nondegenerate solutions of the square subsystem `{c21', M1, M2}` and 65 of
the swap `{c21', M1, conic2}` were computed at `kappa = 1` (float Newton,
600/400 random complex starts); at every one the complementary conditions
were nonzero, with the observed on-locus dependence `conic1 = 2*conic2`.
**Typed `OPEN` (numerically indicated empty; UNREVIEWED, not a claim).**

```text
PACKET R4-00-R1 SERIAL v1
BASIS 31777ce90994a106aade85064c0d868e32863f94
TAILS d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
COMPILER 2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
FIELD char-0 containing i ; branch eps in {+1,-1}
VARS s t s1 t1 kappa q ; az bz ; a7 b7 u7 v7 A7 B7 ; d8..d13 adapted (a_m b_m u_m v_m A_m B_m) ; k10_1..9 k6_1..9 k2_1..5 ; mu2_1..5 mu4_1..3 mu6_1 Jdet_0
SOURCE d=L^4*ell(s,t)+L^5*ell(s1,t1)+L^6*cone(az,bz,uz,vz)+sum_{m=7..13}L^m*(cone(a_m,b_m,u_m,v_m)+(B_m,0,0,0,0,A_m)) ; uz=(8*eps*i*q-5*kappa*s)/6 ; vz=(5*kappa*t-q)/6 ; ell(s,t)=(2s,t/8,s,t,s,2t) ; cone(a,b,u,v)=(2b+2u,a,b,8a+v,b-u,16a+4v) ; loads k10=kappa+sum_{j=1..9}k10_j*L^j k6=sum_{j=1..9}k6_j*L^j k2=sum_{j=1..5}k2_j*L^j ; targets and truncation per frozen compiler
EQUALITIES G_i,n=0 for i=1..7 n=8..19 ; grades<=11 identically satisfied ; grade12,13,14-combos force A7=B7=0 (imposable as equality)
OPENS kappa!=0 ; (s,t)!=(0,0) ; q!=0 ; Jdet_0!=0
INERT a10..a13 b10..b13 u12 v12 u13 v13 k10_6..k10_9 k6_6..k6_9
STATUS OPEN ; numeric-empty indication UNREVIEWED
```

Canonical digest (same convention): `739c3c558a3d3ae7c8e0fe1bca71ea21c1c60a1ac32fb82d2e66027884a21a69`.

## 8. CELL-R2 (`D != 0`): typed OPEN residual, serialized

Rows 1,2 uniquely solve every top jet:
`(A_m,B_m) = -(2048/D)*( p*I1@n - 16q*I2@n , 64q*I1@n + 16p*I2@n )` at grade
`n = m+6`, with `mu2_{n-14}` riding in `I2@n` as the free line parameter at
grades 15–19 (solve-check verified exactly).  In the shifted coordinates
`(p,q)` the grade-14 solve is

```text
D*A8 = -(250/9)st*kappa^3 p + 2st*p^2 + 128st*q^2 - 480s t^2 kappa*q - (15/2)s^2 t*kappa*p
       + (125/9)s^2 kappa^3 q + (5/2)s^3 kappa*q + (50/9)t*kappa^2 p^2 + (3200/9)t*kappa^2 q^2
       - (8000/9)t^2 kappa^3 q + 160t^3 kappa*p - (5/9)kappa*p^2 q - (320/9)kappa*q^3
D*B8 = -(16000/9)st*kappa^3 q + 480s t^2 kappa*p + (50/9)s*kappa^2 p^2 + (3200/9)s*kappa^2 q^2
       - 480s^2 t*kappa*q - (125/9)s^2 kappa^3 p + s^2 p^2 + 64s^2 q^2 - (5/2)s^3 kappa*p
       + (8000/9)t^2 kappa^3 p - 64t^2 p^2 - 4096t^2 q^2 + 10240t^3 kappa*q
       - (320/9)kappa*p*q^2 - (5/9)kappa*p^3
```

After this substitution the entire closed window content on the base
`(s,t,uz,vz,kappa)` is the five conditions (`D^2`-cleared, valid on `D!=0`)

```text
X1 := D^2 * c31@16|sub ,  X2 := D^2 * row4@16|sub ,  X3 := D^2 * row6@18|sub ,
X4 := D^2 * D51@18|sub ,  X5 := D^2 * D71@18|sub ,
```

where the unsubstituted generators are exactly (literal, complete):

```text
c31@16 = (3/16384)A8B8 + (5/4096)kappa(uz*A8 - vz*B8) - (3/8192)st*B8 - (3/16384)s^2 A8
  + (3/256)t^2 A8 - (3/128)s t^3 + (3/8192)s^3 t + (3/1024)s*uz*vz - (3/2048)t*uz^2
  + (3/32)t*vz^2 - (15/4096)st*kappa*uz + (15/8192)s^2 kappa*vz - (15/128)t^2 kappa*vz
row4@16 = -(3/8192)A8^2 + (3/524288)B8^2 + (5/1024)kappa*vz*A8 + (5/65536)kappa*uz*B8
  + (3/2048)st*A8 - (3/262144)s^2 B8 + (3/4096)t^2 B8 - (9/4096)s^2 t^2 + (3/524288)s^4
  + (3/128)t^4 - (3/32768)s*uz^2 + (3/512)s*vz^2 - (3/256)t*uz*vz - (15/1024)st*kappa*vz
  - (15/131072)s^2 kappa*uz + (15/2048)t^2 kappa*uz
row6@18, D51@18, D71@18: via L18, L51, L71 of Section 5 (equivalently the
  19/18/21-term literal forms verified in this lane's pipeline)
```

with `c51@16 = -(1/8)c31@16`, `c71@16 = -(1/128)c31@16` identities disposing
of the remaining grade-16 combos.  All other window conditions
(`c31@17` — 39 literal terms including `-(1/4)vz*k2_1`,
`(3/128)(s*vz-t*uz)*k6_1`, `k10_1`-, `u7,v7`-, `s1,t1`-, `(A9,B9)`- and
hence `mu2_1`-terms — `c31@18`, `c31@19`, `D51@19`) contain fresh
jet/load/target freedoms; `row4@17..19` define `mu4_1..3`; `row6@19`
defines `mu6_1`; `c71@19+(1/128)c31@19` defines `Jdet_0` with the survival
open `Jdet_0 != 0`.

Exact numeric status (guide only): scaled-random float Newton on
`{X1,X2,X3,X4}` at `kappa=1` finds points such as

```text
(s,t,uz,vz) ~ (-2.2190001+0.0067670592i, 0.00084588185-0.27236049i,
               2.3173055+0.0000114i, -0.0000014-0.289673i),  |D| = 1.235,
```

at which exact Gaussian-rational Newton descends to residual
`max|X_i| = 2.96*10^-14` (and `5.97*10^-15` at a second point) with slow
linear convergence, and the exact-evaluation Jacobian of `{X1,X2,X3,X4}`
has numerical rank 2 (max `|3x3 minor| ~ 3*10^-11` against `|2x2| ~ 10^-4`);
`X5 = X4/8` is observed on the locus.  This indicates a positive-dimensional
surviving base component with `D != 0` — but it is a numeric indication
only.  **Typed `OPEN`.  No nonemptiness or emptiness of CELL-R2 is
claimed.**

```text
PACKET R4-00-R2 SERIAL v1
BASIS 31777ce90994a106aade85064c0d868e32863f94
TAILS d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
COMPILER 2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
FIELD char-0
VARS s t s1 t1 kappa ; az bz uz vz ; d7..d13 adapted (a_m b_m u_m v_m A_m B_m) ; k10_1..9 k6_1..9 k2_1..5 ; mu2_1..5 mu4_1..3 mu6_1 Jdet_0
SOURCE d=L^4*ell(s,t)+L^5*ell(s1,t1)+L^6*cone(az,bz,uz,vz)+sum_{m=7..13}L^m*(cone(a_m,b_m,u_m,v_m)+(B_m,0,0,0,0,A_m)) ; ell(s,t)=(2s,t/8,s,t,s,2t) ; cone(a,b,u,v)=(2b+2u,a,b,8a+v,b-u,16a+4v) ; loads k10=kappa+sum_{j=1..9}k10_j*L^j k6=sum_{j=1..9}k6_j*L^j k2=sum_{j=1..5}k2_j*L^j ; targets and truncation per frozen compiler
EQUALITIES G_i,n=0 for i=1..7 n=8..19 ; grades<=11 identically satisfied ; A7=B7=0 forced at grade 14 ; (A_m,B_m)=-(2048/D)*(p*I1@n-16q*I2@n,64q*I1@n+16p*I2@n) n=m+6=14..19 ; closed base content {X1,X2,X3,X4,X5} as defined ; mu4_1..3 mu6_1 Jdet_0 defined at grades 17,18,19,19,19
DERIVED p=6*uz+5*kappa*s ; q=-6*vz+5*kappa*t ; D=p^2+64*q^2
OPENS kappa!=0 ; (s,t)!=(0,0) ; D!=0 ; Jdet_0!=0
INERT a10..a13 b10..b13 u12 v12 u13 v13 k10_6..k10_9 k6_6..k6_9
STATUS OPEN ; positive-dimensional numeric candidate base component UNREVIEWED
```

Canonical digest (same convention): `d621a68ea9b90e79a4650310099a3e0dd157bef1f372a6dec0d2af0990d5a9b8`.

## 9. Maximum exact statement and cheapest successor

**Maximum exact statement safe to consume.**  Over any characteristic-zero
field, on `R4-00` with all literal equations `G_i,8..19 = 0` imposed:

1. grade 12 forces `z` onto the reduced cone (Section-3 certificates), with
   `(s1,t1,az,bz)` inert at entry;
2. every new jet moves by the single matrix `T` (Section 4), whose reduced
   rank fan is the kappa-shifted leading fan in `p = 6uz+5kappa*s`,
   `q = -6vz+5kappa*t`;
3. grade 14 forces `A7 = B7 = 0` on every cell;
4. the rank-0 cell is **empty** (grade-18 unit kill on three exact rays —
   Section 6);
5. the rank-1 and rank-2 cells narrow to the serialized residuals of
   Sections 7–8: on rank 2 the complete closed base content through grade 19
   is `{X1..X5}` plus absorbable conditions and the `Jdet_0 != 0` survival
   open; on rank 1 it is `{c21'@14, four-line concurrency, two conics}` over
   `Q(i)` plus the analogous absorbable tail.

Every grade-19 survivor of `R4-00` lies in CELL-R1 or CELL-R2 as serialized.
No point of either residual is asserted to exist.

**Cheapest decisive successor (frozen AWS packet; desk elimination here
became heavy/uncertain at the float noise floor, so per lane discipline
local computation stops).**  Two independent jobs, both consuming only the
pinned tails/compiler and this report's serialized generators:

1. `R4-00-R2-BASE-DECIDE`: ring `Q[s,t,uz,vz,kappa]`, `dp`; ideal
   `(X1,X2,X3,X4,X5)` built deterministically by the Section-8 recipe;
   saturate by `D` and `kappa`; remove components inside `V(s,t)`; primary
   decomposition; for each surviving component, substitute a generic point
   into the Section-5 absorbable conditions and the `Jdet_0` value and
   decide grade-19 completion.  Expected to settle CELL-R2 (and hence, with
   job 2, all of `R4-00`) either way.
2. `R4-00-R1-BASE-DECIDE`: ring `Q(i)[s,t,kappa,q]` (or `Q[..,i]/(i^2+1)`),
   same treatment of `{c21'@14, M1, M2, conic1, conic2}` saturated by
   `q*kappa`, minus `V(s,t)`.

Runtime of this lane's exact pipeline (structure, stratum replay, grade-12
solve, T-ladder, cells R0/R1/R2 reductions, controls): under 20 s total,
stdlib only.  The numeric probes (float and exact-rational Newton, ~6 min
total) are exploration only and carry no evidentiary weight.

## 10. Scope and nonclaims

Field-valued, reduced-rank, finite-jet results on the exact normalized
V20R2 support only.  Nothing here decides `R4-02`, other valuations,
other supports, scheme-theoretic (nilpotent) structure, arcs, germs,
polynomial Keller maps, a counterexample, or JC2.  `REPRESENTATIVE` data is
not attainment; a floor is not attainment; formal jets are not arcs or
maps.  The Section-7/8 numeric indications are `UNREVIEWED` and must not be
consumed as verdicts.  Promotion requires a different-model hostile review
rebuilding the rows and attacking every displayed identity, the three-ray
elimination, the unit kills, and the serialized residual definitions.

Only this report was written; no canonical or existing artifact, ledger, or
`jc2-lean` content was touched.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `28435`.
- Body SHA-256:
  `3b9e1abdeb69ef781ebf4598545d71bc2ab8987c70244fddb630ddf5882eaf65`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
