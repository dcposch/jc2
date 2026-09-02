# DELTA-DENOM -- denominator increments in Moh's major-disc radii

Lane: `DELTA-DENOM`.  Agent: GPT-5.5/Codex.  Date: 2026-09-02.

## 0. Custody and Scope

The six frozen inputs were hashed before use.  All matched the charge:

```text
9f47a25f...  time-function-endgame-opus5-20260902.md
126d9c84...  integration17-coordinator-fable51-20260902.md
26479b06...  d1-subtree-opus5-20260902.md
527cd7fc...  deltadenom.py
cf0780cc...  d1floor.py
30220204...  moh_skeleton_N.py
```

Read directly from Moh, J. reine angew. Math. 340 (1983), using the local PDF
`refs/moh1983_jram340_configurations_of_roots.pdf` and rendered page images:

```text
p.147  Def. 1.3 and Prop. 1.2        OCR moh.txt:L351-L385
p.154  deg_y T_r^psi = -mu_r         page image; OCR moh.txt:L778-L782
p.179  Def. 5.1                      page image; OCR moh.txt:L2115-L2136
p.180  Prop. 5.3                     page image; OCR moh.txt:L2155-L2170
p.201  search conditions (8)-(13)    page image; OCR moh.txt:L3270-L3307
p.202  exception table               page image; OCR moh.txt:L3326-L3344
p.207  Appendix II transformed table page image; OCR moh.txt:L3596-L3608
```

No canonical ledger was edited.  `jc2-lean` was not inspected.  I added one
non-canonical driver:

```text
d766a2fb0554147ca54918db14141206041f12252cc65f7e4b0f1baf78959ab0
box/delta-denom-drivers-20260902/delta_increment_filter.py
```

## 1. Verdict

**THEOREM DELTA-DENOM-ACTUAL (PROVED-HERE/UNREVIEWED).**  In Moh Prop. 5.3 the
new radius `delta_{r-1}` is the minimum of `ord_t(alpha-beta)` over roots
`alpha,beta` of

```text
g(y) * T_1^psi(y) * ... * T_r^psi(y)
```

that lie in the selected `D_r` subdisc, namely `ord_t(alpha-tau)>delta_r` and
`ord_t(beta-tau)>delta_r`.  Therefore the reduced denominator of `delta_{r-1}`
must divide the ramification index of at least one branch in an attaining pair.
Equivalently it divides the lcm of all actual branch ramification indices present
in that selected root set.  This is a branch-data theorem, not by itself a
numerical-skeleton theorem.

The prompt's possible escape by `lcm(e,e')` is too weak and not sharp: if
`alpha in C((t^(1/e)))` and `beta in C((t^(1/e')))`, then the first non-cancelled
term of `alpha-beta` comes from the union of the two supports, so its denominator
divides `e` or `e'` itself.  A denominator not present in either branch index is
not created by subtracting the two series.

**REFUTED:** the test `denom(delta_i) | n` or `| m` is not the theorem.  Moh p.207
has the transformed `(n,m)=(21,14)` row with `delta_2=-1/2`, `delta_1=7/6`.
The raw denominator `6` divides neither `21` nor `14`.  The row is not a mistake:
the correct object is the denominator increment after higher radii are already
adjoined.

**THEOREM MOH-INCREMENT-FILTER (SOURCE-MOH / IMPLEMENTED-HERE-UNREVIEWED).**
Moh p.201 gives the skeleton-level denominator condition.  Let

```text
L_i = lcm(denom(delta_s), ..., denom(delta_{i+1})),
A_i = denom(L_i * delta_i).
```

For `i=1`, Moh's printed conditions (12)/(13) are exactly:

```text
A_1 | (n/d_2)V_2  and  A_1 | (m/d_2)V_2 - 1,
or
A_1 | (m/d_2)V_2  and  A_1 | (n/d_2)V_2 - 1.
```

For `i>=2`, write

```text
B_i = V_{i+1} d_i/d_{i+1} = Delta_i A_i + R_i,  0 <= R_i < A_i.
```

Moh's p.201 conditions (10)/(11) give the necessary union

```text
V_i <= Delta_i       or       V_i == R_i mod A_i.
```

This is the filter implemented below.  It is stricter and more faithful than
raw `denom(delta_i)|n,m`; it also explains why the p.202 rows have a strong
denominator bias.  They were printed after Moh's denominator-increment search
conditions, not sampled from the raw Def. 5.1(2) window.

## 2. Source Reading

Moh's tree data are order data.  The p.147 remark says the paper works in
`K=k((t))` or its Puiseux field and replaces distance by order
(`moh.txt:L351-L356`).  Prop. 1.2 identifies a `pi`-root
`sigma=sum a_j t^j + pi t^delta` with roots satisfying
`ord(sigma-tau_i)=delta`, and the leading polynomial is a product of the
corresponding linear factors (`moh.txt:L373-L385`).  Thus a disc radius is
an actual first-separation order, not only a formal rational number.

Moh p.154 gives `deg_y T_r^psi(f(x,y),g(x,y)) = -mu_r` and says the sequences
`{n,mu_1,...,mu_r}` and `{n,M_1,...,M_r}` determine each other
(`moh.txt:L778-L782`).  This identifies the parent degrees entering Prop. 5.3:
`g` has degree `n`; `T_j^psi` has degree `-mu_j`; `T_1^psi=f` in the search
normalization has degree `m=-mu_1`.

Def. 5.1(1), p.179, counts roots inside `D_i`: `g` contributes
`(n/d_{i+1})V_{i+1}` roots and `T_j^psi` contributes
`(-mu_j/d_{i+1})V_{i+1}` roots for `j=1,...,i`.  Def. 5.1(3) then gives the
closed formula for `delta_i` (`moh.txt:L2115-L2136`, page image checked).

Prop. 5.3, p.180, is the crucial geometric definition.  For `r>=2`, choose a
factor `pi-C_r` of the Prop. 4.6 polynomial with multiplicity `V_r`.  Moh then
defines `delta_{r-1}` as the minimum of `ord(tau_i-tau_j)` over roots of
`g * prod_{i=1}^r T_i^psi` satisfying the strict condition
`ord(tau_i-tau)>delta_r` and `ord(tau_j-tau)>delta_r`; the same display says
this is the logarithmic radius of the minimal next disc (`moh.txt:L2155-L2170`,
page image checked).  The formula following that definition is Def. 5.1(3) with
`i=r-1`.

Finally, p.201 is the skeleton-level denominator paragraph.  Moh says the radii
are computed from Def. 5.1 and then considers the denominator increment `A_{r-1}`
using the "l.c.m. of the reduced denominators" of the already constructed higher
radii (`moh.txt:L3286-L3289`).  The page image gives the division algorithm
`V_r(d_{r-1}/d_r)=Delta_{r-1}A_{r-1}+R_{r-1}`, conditions (10)/(11), and the
special bottom alternatives (12)/(13).

## 3. Proof of the Branch Denominator Theorem

Let `rho` be a Puiseux branch with minimal ramification index `e(rho)`, so
`rho in C((t^(1/e(rho))))` and not in a smaller such field.  If `rho` is a root
of a monic polynomial `H(y) in C((t))[y]`, then `e(rho)` is the degree of the
irreducible Puiseux factor containing `rho`; it is a part of a partition of
`deg_y H`.  It need not divide the total degree unless `H` is irreducible or an
extra one-place hypothesis is supplied.

For two branches `rho,rho'`, the exponents appearing in `rho-rho'` are among
the exponents already appearing in `rho` or in `rho'`.  Common exponents can
cancel, but cancellation does not introduce new exponents.  Therefore

```text
ord_t(rho-rho') in (1/e(rho))Z union (1/e(rho'))Z union {infinity}.
```

For a finite nonzero order, its reduced denominator divides `e(rho)` or
`e(rho')`.  Applying this to an attaining pair in Moh's Prop. 5.3 gives
DELTA-DENOM-ACTUAL.

Degree-only corollary: if all relevant parent polynomials are irreducible over
`C((t))`, then the denominator of `delta_{r-1}` divides one of
`n,-mu_1,...,-mu_r`.  Without irreducibility, a branch of ramification `A` is
possible inside a degree `D` parent whenever an irreducible factor of degree
multiple `A` is present; the numerical skeleton does not record this
factorization.

## 4. D=105 Selected Skeleton

The selected skeleton from the charged TIME-FUNCTION report is

```text
n=105, m=70, M=(-70,-63,103), d=(105,35,7,1), V_2=1, V_3=4,
delta_1=3/4, delta_2=71/95, delta_3=-1.
```

The odd gcd chain alone does **not** prove that every relevant Puiseux
ramification index is odd.  That would require an additional theorem identifying
actual irreducible branch degrees of the roots of `g,T_1^psi,T_2^psi,T_3^psi`
with divisors of the gcd chain.  Def. 5.1 and Prop. 5.3 do not state that.  This
is a bounded GAP:

```text
OPEN[CHAIN-TO-RAMIFICATION]
bounded quantity: for the single D=105 skeleton, the actual branch ramification
multisets of roots of g,T_1^psi,T_2^psi,T_3^psi in the Prop. 5.3 selected discs.
```

However the skeleton dies by Moh's p.201 denominator-increment condition, without
using the odd-chain claim.  For `delta_1`, the higher lcm is `L_1=denom(delta_2)=95`,
so

```text
A_1 = denom(95 * 3/4) = 4,
d_2 = 35,  n/d_2 = 3,  m/d_2 = 2,  V_2 = 1.
```

Moh (12) would need `4|3` and `4|1`; Moh (13) would need `4|2` and `4|2`.
Both alternatives fail.  For `delta_2`, `A_2=95` and
`V_3 d_2/d_3 = 20 = 0*95 + 20`; the p.201 higher-level union would need
`V_2<=0` or `V_2==20 mod 95`, also false.  Thus:

```text
THEOREM/UNREVIEWED: the selected D=105 skeleton is impossible by Moh p.201.
GAP: the stronger statement "the odd d-chain forces odd branch ramification"
     is not proved here and is not used.
```

## 5. Cross-Checks on Moh's Tables

Moh p.202 lists the exceptional data after the search conditions; the page image
has the four rows with bracket alternatives (`moh.txt:L3326-L3344`).  Splitting
brackets gives the six rows below.  `A_1` is the denominator increment
`denom(L_1 delta_1)`, not the raw denominator of `delta_1`.

```text
row                    n   m   delta_2  delta_1  A_1  p201 bottom
(64,48)               64  48   1/4      9/16     4    pass
(84,56) M2=64,V2=2    84  56   2/7      16/21    3    pass
(84,56) M2=72,V2=5    84  56   1/4      7/12     3    pass
(75,50) V2=3          75  50   1/5      1/2      2    pass
(75,50) V2=2          75  50   1/5      2/3      3    pass
(99,66)               99  66   1/3      4/9      3    pass
```

All six also pass the higher p.201 union condition in the driver:

```text
(64,48)                  A=[4,4]  D1=True  ALL=True
(84,56) M2=64,V2=2       A=[3,7]  D1=True  ALL=True
(84,56) M2=72,V2=5       A=[3,4]  D1=True  ALL=True
(75,50) V2=3             A=[2,5]  D1=True  ALL=True
(75,50) V2=2             A=[3,5]  D1=True  ALL=True
(99,66)                  A=[3,3]  D1=True  ALL=True
```

Moh p.207 transforms the first three Appendix II cases (`moh.txt:L3596-L3608`,
page image checked).  The transformed `(21,14)` row is the warning against raw
`denom(delta_1)|n or |m`:

```text
row                      n   m   delta_2  delta_1  raw denom  A_1  p201 bottom
p207 (16,12)            16  12   -1       1/4      4          4    pass
p207 (21,14) M2=16      21  14   -1/2     7/6      6          3    pass
p207 (21,14) M2=18      21  14   -1       1/3      3          3    pass
p207 (15,10) V2=3       15  10   -1       1/2      2          2    pass
p207 (15,10) V2=2       15  10   -1       4/3      3          3    pass
```

The p.207 row `delta_1=7/6` has raw denominator `6`, with `6` dividing neither
`21` nor `14`; after adjoining `delta_2=-1/2`, the increment is only `A_1=3`,
which satisfies Moh (12).

## 6. Implemented Filter, D <= 120

Driver:

```text
python3 box/delta-denom-drivers-20260902/delta_increment_filter.py
```

Definitions:

```text
D1pass  = pass Moh p.201 (12)/(13) at the bottom step.
ALLpass = D1pass plus the p.201 (10)/(11) necessary union for all i>=2.
UNI     = the charged one-orbit integrality survivor test with N>=6.
```

Complete per-degree results:

```text
    D         V    D1pass   ALLpass    D1kill   ALLkill       UNI   UNI_D1p  UNI_ALLp
   48      1301       207         2      1094      1299        26        17         0
   54       514        42         2       472       512        10         8         2
   60      3623       608        18      3015      3605        72        48        14
   63       438        25         2       413       436         7         2         1
   64      2417       408        10      2009      2407        57        39         7
   66       390        21         0       369       390         3         1         0
   72     15694      2165        55     13529     15639       302       217        31
   75       682        68         9       614       673        12         8         5
   78       558        24         0       534       558         9         2         0
   80     16074      2429        45     13645     16029       241       168        25
   81       764        49         2       715       762        14         7         1
   84     10748      1366        51      9382     10697       152       113        28
   88       550        39         1       511       549         9         4         1
   90     30107      3699        91     26408     30016       368       238        50
   96    130186     23278       229    106908    129957      1610      1189       103
   99      1180        62         8      1118      1172        25        13         7
  100     26873      3585        67     23288     26806       247       184        34
  102       984        36         3       948       981        14         5         3
  104       786        51         4       735       782        15        11         4
  105      5037       310        15      4727      5022        63        34         7
  108     85205     11229       206     73976     84999      1184       798       120
  110      1890       105         3      1785      1887        14         8         1
  112     47655      6106        76     41549     47579       593       396        36
  114      1242        45         4      1197      1238        18         6         4
  117      1686        78         7      1608      1679        22        10         4
  120    516309     81284       782    435025    515527      4466      3186       352
```

Totals over `D in [48,120]`:

```text
V-skeletons:       902893
D1 kills:          765574  (84.7912%)
ALL-increment kills:901201 (99.8126%)
ALL survivors:       1692  (0.1874%)

UNI N>=6 survivors: 9553
D1 kills among UNI: 2841   (29.7393%)
ALL kills among UNI:8713   (91.2070%)
UNI ALL survivors:   840   (8.7930%)
```

Degrees emptied:

```text
D1-only: none among V-skeleton degrees; none among UNI N>=6 survivor degrees.
ALL increments: V-skeleton degrees 66 and 78 are emptied.
ALL increments: UNI N>=6 survivor degrees 48, 66 and 78 are emptied.
```

MOH-SHARP-2 degrees:

```text
D=105  V 5037 -> 15    UNI>=6 63   -> 7
D=108  V 85205 -> 206  UNI>=6 1184 -> 120
D=112  V 47655 -> 76   UNI>=6 593  -> 36
D=117  V 1686 -> 7     UNI>=6 22   -> 4
D=120  V 516309 -> 782 UNI>=6 4466 -> 352
```

No MOH-SHARP-2 degree is emptied by the all-increment filter.  The selected
`D=105` skeleton dies, but `D=105` itself still has 7 `(UNI) N>=6` survivors after
the all-increment condition.

## 7. Same Question for Higher Radii and Numerators

For every `i<s`, `delta_i` is produced by Prop. 5.3 at the step `r=i+1`.  The
actual branch theorem is identical: the reduced denominator of `delta_i` divides
one actual ramification index in an attaining pair among roots of
`g*T_1^psi*...*T_{i+1}^psi` in the selected higher disc.  This is not recorded
by Def. 5.1(3)'s closed rational formula.

The skeleton-level condition is not raw `denom(delta_i)`.  It is the increment
`A_i=denom(L_i delta_i)` after adjoining the higher radii.  For `i>=2`, Moh p.201
does not give a single congruence because the selected factor of `p(pi)` may be
of the form `pi-a` with `a!=0`, or of the form `pi`.  The implemented `ALLpass`
uses the necessary union of those two printed cases.  It is a certified kill
condition; surviving it is not an existence theorem.

I found no independent numerator divisibility condition.  Prop. 5.3 constrains
the value as a valuation order and p.201 constrains its denominator increment and
the compatible multiplicity `V_i`.  Once the denominator lattice is fixed, the
numerator of a first-separation order can vary with the exponent level.  Thus
there is no additional skeleton filter on numerators from Def. 1.1-1.3, Prop.
1.2, Prop. 5.3, or Def. 5.1.

## 8. Typed Outcomes

```text
PROVED-HERE/UNREVIEWED
  DELTA-DENOM-ACTUAL: Prop. 5.3's delta_{r-1} is a minimum over the selected
  roots of g*prod_{j<=r}T_j^psi, and denom(delta_{r-1}) divides a ramification
  index of an attaining branch.

SOURCE-MOH / IMPLEMENTED-HERE-UNREVIEWED
  MOH-INCREMENT-FILTER: p.201 conditions (10)-(13), with A_i the denominator
  increment after adjoining higher radii.

REFUTED
  Raw filter denom(delta_i)|n or |m.  It is neither the branch theorem nor Moh's
  p.201 condition; p.207's (21,14) transformed row has raw denom(delta_1)=6.

KILLED/UNREVIEWED
  The selected D=105 skeleton with delta_1=3/4 and delta_2=71/95 fails Moh p.201
  at both A_1=4 and A_2=95.

GAP
  CHAIN-TO-RAMIFICATION: the odd d-chain (105,35,7,1) alone has not been shown
  to force all actual branch ramification indices odd.
```

The six-of-six p.202 coincidence is therefore not evidence for `denom(delta_1)|n`
or `|m`; it is a shadow of Moh's denominator-increment search conditions.  The
correct arithmetic object is `A_i`, not the raw denominator of `delta_i`.

<!-- BODY-END -->
