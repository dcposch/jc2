# The joint two-infinity system for `(99,66)`

Date: 2026-09-03 UTC  
Producer: Codex `g9966-global-design-sol56-20260903`  
Frozen basis: `afb7e21be9164e6fed9748614361f51db26e1410`  
Lifecycle: **FINAL — sealed below**

## 0. Endpoint and typed scope

**No Keller pair and no `(99,66)` kill was obtained.** The finite global chart,
the two-point incidence rows, and the following common-jet prefixes are exact
and reproducible; every computed prefix is nonempty:

* the simultaneous fixed `h3` `D2` face, `h2` `D2` face, and first `h2`
  `D1` vanishing band below `e^296` have dimension 120;
  its independent projected `h2` audit has `169 -> 162` dimensions;
* that major block meets the `delta=2 [2,1]` common-`h3` minor leader in
  dimension 104 (or 6,704 after restoring the untouched outer `F,G` blocks);
* it meets Xu's curved `delta=5/2` common-`h3` leader, and its reduced
  `T3` ODE remains consistent through `s^28`. At `c=1` its dimension is
  `3=(u,v,b0)`, or `2` after the optional `b0=0` normalization;
* the first common outer/minor/Jacobian prefix has 15 independent pivots:
  dimensions **6,689** for `delta=2` and **6,687** for `delta=5/2` after
  `b0=0`.

The separate straight-centre `delta=2` lift reaches local band 5 with dimension
59 (branch parameter included and Jacobian scalar fixed); band 6 is open. Its
local coordinates have no complete map to the 7,161 global coordinates, so 59
is **not** added to the joint counts.

Accordingly the verdict is

```text
COUNTING-BOUND[MAJOR-h3/h2 + MINOR-h3 JOINT]
SURVIVES[delta=2 COMMON-h3 LEADER]
COUNTING-BOUND[delta=5/2 CONSISTENT-THROUGH-s^28]
COUNTING-BOUND[FIRST-GLOBAL-FG/J-BAND]
OPEN[COMPLETE-GLOBAL-FG/J + OUTER-MAJOR + EFFECTIVE-ROOT-BRIDGE]
```

These are necessary finite subsystems, not a global specialization; no direct
identity `J(F,G)=1` has been checked for a degree `(99,66)` pair.

## 1. Custody, conventions, and source facts

The lane receipt
[`g9966-global-design-sol56-20260903.run.v2`](/home/ubuntu/jc2/xmodel/g9966-global-design-sol56-20260903.run.v2)
was parsed mechanically: `awk` paired every indexed
`charged_input_<i>_basename` with `charged_input_<i>_sha256` under the receipt's
`lane_inputs_dir`, and `sha256sum -c` returned `OK` for all **14/14** frozen
inputs. The manifest was generated from those fields; no supplied digest was
retyped. Drivers that consume frozen inputs repeat this receipt check; the
self-contained first-global-band probe consumes only displayed chart formulas.
No ledger, `jc2-lean`, or named in-progress report was read or edited. A
delegated seal-format `rg` accidentally returned only lifecycle/marker lines
from several `ideation-*` files. No mathematical content was used; this narrow
read-scope breach is disclosed.

Work is over characteristic zero. Exact computations use `Q` or a displayed
localization of it; the coefficient constructions base-change to the intended
field `k`.

### 1.1 The essential label reversal

Write throughout this report

```text
F = prompt f, deg F=99;       G = prompt g, deg G=66;       J(F,G)=1.
```

Moh and Xu instead call the degree-66 polynomial `f` and the degree-99
polynomial `g`. Thus `(F,G)=(g_Moh,f_Moh)`, and their oriented Jacobian is
`J(G,F)=-1`. This reversal matters for the principal-minor multiplicity:

| object in this report | source object | degree | principal-minor multiplicity |
|---|---|---:|---:|
| `F` | Xu/Moh `g` | 99 | `99*3/11 = 27` |
| `G` | Xu/Moh `f=T1` | 66 | `66*3/11 = 18` |
| `T2` | `T2` | 55 | `55*3/11 = 15` |
| `T3` | `T3` | 145 | `(145-2)*3/11+1 = 40` |

The formula is Xu section 7.3's
`((-mu_s-2)u_s/d_s)+1` for the last effective root; see the frozen source audit
at
[`xu9966-read...md:57`](/tmp/jc2-lane.eijAga/inputs/xu9966-read-gpt55-20260903.md:57).
Moh's numerical row gives `d=(99,33,11,1)`, `u3=11-8=3`, the two homogeneous
multiplicity packets, and the major radii; see
[`moh9966-branchB...md:63`](/tmp/jc2-lane.eijAga/inputs/moh9966-branchB-sol56-20260903.md:63)
and
[`moh9966-branchB...md:82`](/tmp/jc2-lane.eijAga/inputs/moh9966-branchB-sol56-20260903.md:82).

The major flag, a principal-minor flag, their physical points at infinity, and
the cover series used to calculate them remain different typed objects. A
common coefficient array does not identify those flags.

## 2. The economical finite global chart

Use the two-direction gauge

```text
Lmin=y,                 Lmaj=y-x,
P=Lmin^3 Lmaj^8 = y^3(y-x)^8.
```

This fixes the torus parameter in `P_a=y^3(y-a*x)^8` to `a=1`. Retaining that
nonzero slope would add one variable everywhere below.

For `D>=r-1`, put

```text
S(D,r)={A in k[x,y] : deg A<=D and deg_y A<r},
dim S(D,r)=r(D+1)-r(r-1)/2.
```

The lossless triangular approximate-root chart with the fixed leading forms is

```text
h3 = P+H,                                      H  in S(10,11),
h2 = h3^3+C2*h3+C3,                            C2 in S(21,11), C3 in S(32,11),
F  = h2^3+A2*h2+A3,                            A2 in S(65,33), A3 in S(98,33),
G  = h2^2+B1*h2+B2,                            B1 in S(32,33), B2 in S(65,33).
                                                        (2.1)
```

The missing `h3^2` and `h2^2` terms are the characteristic-zero
Tschirnhausen/approximate-root normalizations, not discarded solutions. The
counts are

| block | `H` | `C2` | `C3` | `A2` | `A3` | `B1` | `B2` | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| fixed top | 66 | 187 | 308 | 1650 | 2739 | 561 | 1650 | **7161** |

As an audit, before fixing the homogeneous forms the corresponding counts are
`77,198,319,1683,2772,594,1683`, totaling **7326**. That equals the ordinary
monic coefficient count `5049+2277` for degrees 99 and 66. Fixing the two top
forms removes exactly `99+66=165` coefficients. Thus (2.1) is a coordinate
chart, not a dimension heuristic.

Its leading forms are exactly

```text
in h3=P,          in h2=P^3,
in F=P^9=y^27(y-x)^72,       in G=P^6=y^18(y-x)^48.       (2.2)
```

This simultaneously records the 27/18 principal-minor multiplicities at
`y=0` and 72/48 major multiplicities at `y=x`.

### 2.1 Major tower as finite coefficient rows

Set

```text
K3(t,w)=t^11 h3(t^-1,w/t),       K2(t,w)=t^33 h2(t^-1,w/t).
```

At the radius `1/3` major node use
`w=1+pi*t^(4/3)`. At its radius `4/9` child use the integralized recentering

```text
t=e^9,              w=1+e^12+Pi*e^13.                    (2.3)
```

The exact major order data are

| object | degree | multiplicity at `D2` | order at `D2` | multiplicity at `D1` | order at `D1` |
|---|---:|---:|---:|---:|---:|
| `h3` | 11 | 8 | `-1/3` | — | not defined there |
| `h2` | 33 | 24 | `-1` | 8 | `-1/9` |
| `F` | 99 | 72 | `-3` | 24 | `-1/3` |
| `G` | 66 | 48 | `-2` | 16 | `-2/9` |

There is deliberately no invented `h3` row at `D1`: the relevant count 24 is
not divisible by 9. Moh's Theorem 1.2 says that if
`Q=h^d+sum_j Q_j h^(d-j)`, then
`ord Q_j(sigma)>=j ord h(sigma)` (printed p.149/PDF 10 of the frozen
[`Moh PDF`](/tmp/jc2-lane.eijAga/inputs/moh1983_jram340_configurations_of_roots.pdf)).
Applied to (2.1), its economical coefficient blocks are

| node/base | exact order rows |
|---|---|
| `D1`, base `h2` | `ord A2>=-2/9`, `ord A3>=-1/3`; `ord B1>=-1/9`, `ord B2>=-2/9` |
| `D2`, base `h3` | after exact `h3`-adic reduction, `ord F_j>=-j/3`, `ord G_j>=-j/3`; the canonical `F_1=0` |
| `D2`, base `h2` | redundant checks `ord A2>=-2`, `ord A3>=-3`, `ord B1>=-1`, `ord B2>=-2` |

Each order statement means finitely many coefficient vanishings after (2.3)
or the denominator-3 substitution; all source polynomials have finite support.
The radius `-1` information is already in (2.2) and the support filters. It is
not extrapolated into a nonexistent child chart.

Two initial major blocks can be counted without expanding all of (2.1):

* For `K3`, the fixed face is `w^3(w-1)^8`. Of the 66 lower coefficients,
  43 lie strictly below `3r+4q=32` and two lie on its unwanted equality sites
  `(r,q)=(4,5),(8,2)`. The 45 linear rows leave the 21-term strict space
  `3r+4q>=33`.
* For `K2`, the fixed top is `w^9(w-1)^24`. Its radius-`1/3` face must be
  `(pi^3-1)^8`. In the 561-dimensional fixed-top `h2` coefficient space,
  eight equality coefficients are
  `(-1)^k binom(8,k)` at `(r,q)=(4k,24-3k)`, `1<=k<=8`, and the strict space
  has 169 coefficients (`3r+4q>=97`). Thus this projected `D2` block has 392
  scalar rows. Recentring by (2.3) adds seven independent rows below `e^296`,
  distributed `1,1,1,2,2` at powers `291,292,293,294,295`, leaving 162.

The projected counts cannot simply be added because in (2.1)
`h2=h3^3+C2*h3+C3`. The simultaneous sparse calculation instead starts after
the 45 `h3` rows with

```text
21 h3 variables + 187 C2 variables + 308 C3 variables = 516.
```

Among the 392 projected `D2` output slots, three are exact approximate-root
identities at `(r,q)=(1,23),(1,22),(2,22)`. The remaining 389 rows have a
unit-triangular `Q*` block: 275 pivots in `C3` and 114 in `C2`. Modulo those
rows, the seven `D1` rows have rank seven; explicit binomial minors have
determinants `59049` and `-3`. All 396 pivots use `C2,C3` columns, so all 21
`h3` coordinates remain free. The simultaneous family is consistent and has

```text
516-389-7 = 120 dimensions.                              (2.3a)
```

### 2.2 What Lemma 2.1 does—and does not—supply

Moh's Lemma 2.1 is a Laurent-coordinate restriction, not an `(x,y)` Newton
polygon. In the orientation of this report, take

```text
F=eta^-99,
G=eta^-66+sum_i gamma_i(x) eta^i.
```

Then `J(F,G)=1` forces `gamma_i(x)=gamma_i(0)` for `i<98` and
`gamma_98(x)=gamma_98(0)-x/99`; higher coefficients are not fixed by the
lemma. This is the exact support information on printed p.151/PDF 12. It does
not license deleting arbitrary monomials from (2.1), and it does not replace
the direct Jacobian rows below.

### 2.3 The two minor incidence blocks

Translations remove the constant centre and the chosen linear normalization
puts the principal-minor line at `y=0`. With `x=t^-1`, the direct, finite
`delta=2 [2,1]` leader incidence is

```text
sigma_2(t,z)=u*t+z*t^2,                  p2=z^2(z+3*rho), rho!=0,
t^18 F(t^-1,sigma_2)=p2^9+O(t),
t^12 G(t^-1,sigma_2)=p2^6+O(t).                          (2.4)
```

Thus `F` has packets `18+9`, `G` has packets `12+6`, and `T2` has packets
`10+5`. The necessary degree-40 `T3` leader is

```text
R=z^25(z+3*rho)^14(z-2*rho),
2*p2*R'-25*p2'*R=k*p2^14.                               (2.5)
```

Here and only here a prime denotes `d/dz`. The exact saturated leader solve is
recorded at
[`moh9966-B-lift...md:226`](/tmp/jc2-lane.eijAga/inputs/moh9966-B-lift-sol56-20260903.md:226).

For Xu's exception put `t=s^2` and

```text
sigma_52(s,pi)=u*s^2+v*s^4+pi*s^5,
p=pi(pi^2-c), c!=0,
s^9 F(s^-2,sigma_52)=p^9+O(s),
s^6 G(s^-2,sigma_52)=p^6+O(s).                           (2.6)
```

The three packets are `9+9+9` for `F`, `6+6+6` for `G`, and `5+5+5` for
`T2`. Xu's degree-40 leader is `q=p^10 q1`; in monic gauge

```text
q1=pi^10-(15/4)c*pi^8+5c^2*pi^6-(5/2)c^3*pi^4+b0.       (2.7)
```

Multiplying (2.7) by `-1/5` and harmlessly renaming/rescaling `b0` gives the
normalization used by the drivers and solves `q1'+2p^3=0`. Xu explicitly leaves
this case open; see
[`xu-delta52-lift...md:83`](/tmp/jc2-lane.eijAga/inputs/xu-delta52-lift-gpt55-20260903.md:83)
and the original frozen
[`Xu PDF`](/tmp/jc2-lane.eijAga/inputs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf).

In (2.4) and (2.6), `O(t)`/`O(s)` is an exact finite instruction: after the
displayed normalization, set every negative-power coefficient to zero and the
constant coefficient to the displayed polynomial. No infinite unknown tail is
introduced. Localize with a Rabinowitsch row `Z*rho-1` or `Z*c-1`, or take the
torus slices `rho=1`, `c=1` after proving the parameter is nonzero.

Mechanical support enumeration gives the raw direct-leader row counts:

| branch | `F99` rows | `G66` rows | total |
|---|---:|---:|---:|
| `delta=2` | 1,134 | 513 | **1,647** |
| `delta=5/2` | 1,316 | 594 | **1,910** |

These count unique `(local exponent,local-coordinate degree)` output slots, or
equation labels, before rank reduction. Many global coefficients can contribute
to one row. The fixed top adds only `z^27,z^18` or `pi^27,pi^18`, whose
monic coefficients cancel the targets. The first original coefficients touched
are `F_(98,0),G_(65,0)`, where the indices mean `[x^i y^j]`: at
`t^-80,t^-53` for branch 2 and at
`s^-187,s^-124` for branch 52. These raw counts do not imply full-block
codimension; section 3.4 ranks the first three pole rows of each polynomial.

### 2.4 Direct Jacobian and the joint schemes

Let `C` be the polynomial ring over `k` in the 7161 named coordinates of
(2.1), and declare

```text
R_2  = C[u,rho,rho^-1],              R_52=C[u,v,c,c^-1].
```

Equivalently, polynomial implementations adjoin wrappers with
`Zrho*rho-1` or `Zc*c-1`. Let `Imaj` be all coefficient rows from section 2.1,
and let `Imin,2^FG` and `Imin,52^FG` be only the direct `F,G` coefficient rows
(2.4) and (2.6). Define the explicitly relaxed incidence schemes

```text
IJ = < [x^i y^j](F_x G_y-F_y G_x-1) : i,j>=0, i+j<=162 >,
X_2^FG  = Spec R_2 /(Imaj+Imin,2^FG +IJ),
X_52^FG = Spec R_52/(Imaj+Imin,52^FG+IJ).                 (2.8)
```

This is the base finite-support global major/direct-`F,G`-leader/Jacobian
relaxation: both local charts are images of the **same** coefficient arrays in
(2.1), and (2.8), not a local ODE, contains the actual Jacobian equation. It is
a necessary superset, not yet the complete requested Moh/Xu joint system,
because the effective-root bridge described below is absent. Before
local-centre variables and a
Rabinowitsch wrapper, its global ambient has exactly 7161 unknowns. Branch 2
adds `(u,rho)` and branch 52 adds `(u,v,c)`; the torus slices remove `rho` or
`c` respectively.

The degree-163 homogeneous part of the Jacobian vanishes identically because
the top forms are powers `P^9,P^6`. Therefore an economical direct expansion
has at most

```text
1+2+...+163 = 13,366
```

coefficient rows in degrees 0 through 162 (the constant row has target 1).
Only the first ten contiguous degree-162 rows are ranked in section 3.4; that
is not the rank of `IJ`.

The effective `T2,T3 in k(x)[F,G]` equations and the condition excluding a
later split inside the double packet are additional necessary derived blocks.
Their explicit source recurrences are not among the frozen inputs: Moh says the
radius-2 case reduces to 11 variables but does not print the variables or the
system
([`moh9966-branchB...md:131`](/tmp/jc2-lane.eijAga/inputs/moh9966-branchB-sol56-20260903.md:131)).
They were therefore not fabricated. Scheme (2.8) is exact for its displayed
global-tower, direct-`F,G`-leader, and Jacobian rows; promotion to Moh's complete
unprinted 11-variable minor system remains `OPEN[EFFECTIVE-T2-T3-BRIDGE]`.

## 3. Where the two points first share coefficients

The first sharing is already the homogeneous polynomial `P`: both points see
the same coefficients of (2.2). The first nonleading common block is even more
explicit. After the 45 major `h3` rows, write

```text
K3=w^3(w-1)^8
   +sum c_(r,d) t^r (w-1)^v_r w^(d-v_r),
v_r=max(0,ceil((33-3r)/4)),
1<=r<=11, v_r<=d<=11-r.                                  (3.1)
```

There are exactly 21 coefficients. Substituting either minor centre into this
same `K3` gives the computations below. In both branches the first active
minor row contains `c_(1,8)` and forces it to zero. Hence the common jet begins
at the first lower global `h3` coefficient, not only at a distant Jacobian
band. Through (2.1), every `c_(r,d)` also occurs in the global `F,G`; what is
missing is the **complete** map from the charged lifts' independent local
`F_n,G_n` names to all 7161 chart coordinates. Section 3.4 emits its first
global prefix directly from (2.1).

Because the 396 major `h2` pivots use only `C2,C3`, projection of the
120-dimensional major family onto its 21 `h3` coordinates is surjective. The
minor ranks therefore add exactly to this triangular block. Before the outer
probe of section 3.4, the four blocks `A2,A3,B1,B2` contain 6600 untouched
variables. The joint counts at that boundary are:

| branch/stage | `h3,h2+centre` dimension | plus 6600 untouched outer variables |
|---|---:|---:|
| computed major `h3/h2` bands, before a minor centre | 120 | 6720 |
| `delta=2`, before minor rows | 122 | 6722 |
| `delta=2`, after 18 leader pivots | **104** | **6704** |
| `delta=5/2`, before minor rows | 123 | 6723 |
| `delta=5/2`, after 20 leader pivots | **103** | **6703** |
| `delta=5/2`, after first ODE compatibility, `b0=0` | **102** | **6702** |

These are exact dimensions of the displayed pre-outer partial schemes, not of
`X_2^FG` or `X_52^FG`; most outer-major, minor-`F,G`, effective-root, and
Jacobian rows remain.
The last row uses the driver's `b0=0` normalization. Restoring the additive
`q1` constant adds one auxiliary effective-root coordinate (dimension 103 in
the displayed incidence, or 6703 with the untouched variables); it is not an
extra `F,G` coefficient.

The preprocessing is graded throughout. Major `h3` uses
`wt(t)=3, wt(w-1)=4` with boundary 32, major `h2` uses the same weights with
boundary 96, and the two minor charts are processed in increasing `t`- or
`s`-exponent. The global Jacobian is to be split by the induced total/face
weight before nonlinear elimination. The unrelated K=16 numerical weights
were not transported into this ring.

### 3.1 Major `h3` inside `h2`: exact `516 -> 120`

[`major_h2_probe.py`](/home/ubuntu/jc2/box/g9966-20260903/major_h2_probe.py)
uses the invertible basis `t^r(w-1)^q` and extracts all rows below `e^296`:

| `e` power | 291 | 292 | 293 | 294 | 295 | total |
|---:|---:|---:|---:|---:|---:|---:|
| new scalar rows/rank | 1 | 1 | 1 | 2 | 2 | **7** |

Thus the projected dimension is 162; back-substitution and positive/perturbed
controls pass.

The simultaneous approximate-root calculation then supplies the correction
(2.3a): three of the nominal `D2` slots are identities, while 389 `D2` and
seven `D1` rows pivot only `C2,C3`. Dimension 120 and the free 21-coordinate
`h3` projection justify the joint counts. This calculation stops before the
outer `F,G` blocks. The exact support/binomial-minor certificate is
[`major_tower_structure.py`](/home/ubuntu/jc2/box/g9966-20260903/major_tower_joint/major_tower_structure.py),
with its JSON result beside it.

### 3.2 `delta=2 [2,1]`: the common `h3` leader

In (3.1) substitute `w=u*t^2+t^3*z` and require
`K3=p2*t^9+O(t^10)`. Exact constant-pivot elimination gives:

| minor `t` band | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| new rows = rank | 1 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 3 |
| cumulative dimension incl. `(rho,u)` | 22 | 21 | 20 | 18 | 16 | 14 | 11 | 8 | **5** |

There is no residual row; on the localized open `rho!=0`, the pivots divide by
neither `rho` nor `u`. The free global
`h3` coefficients are `c_(7,4),c_(10,1),c_(11,0)`. In the straight slice
`u=0`, the same global polynomial gives

```text
W3=-8*z^4-18*rho*z^3,       W6=28*z^5+45*rho*z^4.        (3.2)
```

These are exactly the old-polynomial tails used by the charged branch-B lift.

That separate lift uses source-ordered local polynomials
`F66=G` and `G99=F` and the exact transformed Jacobian recurrence

```text
E_n=sum_(r+s=n)((18-s)f_r' g_s+(r-12)f_r g_s')-cJ*[n=31]. (3.3)
```

Its banked ledger is:

| band | new unknowns | raw / quotient rows | new rank | old compatibility | dimension incl. `rho`, fixed `cJ` |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 | 1 |
| 1 | 43 | `32 / 27` | 26 | 0 | 18 |
| 2 | 41 | `36 then 30 / 25` | 24 | 5 | 30 |
| 3 | 39 | `30 / 25` | 24 | 4 | 41 |
| 4 | 37 | `29 / 24` | 22 | 5 | 51 |
| 5 | 35 | `28 / 23` | 22 | codimension 5 | **59** |
| 6 | 33 | `27 / 22` | 20 | 17 remainder rows | **OPEN** |

This table and the fact that `cJ` first appears only at band 31 are sourced at
[`moh9966-B-lift...md:293`](/tmp/jc2-lane.eijAga/inputs/moh9966-B-lift-sol56-20260903.md:293).
Band 5 is consistent on 15 components; band 6 is the exact next local system.
Because (3.3) is a straight-centre local slice, not the pullback of (2.8), its
59 is not a joint-global dimension and supplies no `J=1` witness.

### 3.3 `delta=5/2`: common leader and ODE through `s^28`

Substitute `t=s^2`, `w=u*s^4+v*s^6+pi*s^7` in the same (3.1), kill the
coefficients below `s^21`, and set `[s^21]K3=p`. There are 20 rows and 20
`Q*` pivots. The active bands are:

| `K3` `s` power | 2 | 4 | 6 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| new rank | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 1 | 2 | 1 |
| cumulative dimension incl. `(u,v,c)` | 23 | 22 | 21 | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 11 | 10 | 8 | 7 | 5 | **4** |

The sole free `h3` coefficient is `c_(11,0)`. Selected shared identities are

```text
c_(2,9)=3u,       c_(3,8)=-3v,
c_(7,4)=c-3u^2v, c_(10,1)=-cv.                          (3.4)
```

Now write `h=p/s+sum A_i s^i` from that same finite global `h3`, and
`Q=q1+sum_(n>=1) B_n s^n`. The reduced Xu equation is

```text
D_s(Q,h)+2s^2 h^4=0,       D_s(Q,h)=Q_s h_pi-Q_pi h_s.   (3.5)
```

At `n=1` (`s^-1`), its only nonzero cokernel condition is
`-(2/5)c^4*c_(11,0)=0`; on `c!=0` this sets `c_(11,0)=0`. After the slice
`c=1`, every level `n=1,...,30` was solved and every original coefficient row
was rechecked. Each level has 19 new coefficients of `B_n` (`deg_pi<=18`),
21 coefficient rows, 19 rational pivots, and two formal cokernel rows. The two
rows vanish after the first shared specialization. No later free parameter appears.

| solved `n` | ODE powers | new variables per level | rows / pivots | nonzero old compatibility | dimension at `c=1` |
|---:|---:|---:|---:|---:|---:|
| 1 | `s^-1` | 19 | `21 / 19` | `c_(11,0)=0` | 3 incl. `b0` |
| 2–6 | `s^0...s^4` | 19 | `21 / 19` | 0 | 3 incl. `b0` |
| 7–30 | `s^5...s^28` | 19 | `21 / 19` | 0 | **3 incl. `b0`** |

Thus the exact typed result is
`COUNTING-BOUND[CONSISTENT-THROUGH-s^28]`, with free `(u,v,b0)`, or `(u,v)`
after setting `b0=0`. The first new order beyond the charged `s^4` cap was
`n=7/s^5`; it too has zero residual. The next unsolved system is

```text
p*B31' + 31*p'*B31 + R31 = 0,
p=pi(pi^2-1), deg B31<=18, deg R31=15,                  (3.6)
```

with 21 rows, 19 unknowns, and two formal cokernel rows. Its exact expanded
forcing is
[`next_system_n31.txt`](/home/ubuntu/jc2/box/g9966-20260903/xu_joint_extension/next_system_n31.txt).
Equation (3.5) is still only a necessary reduced ODE: it does not impose
`T3 in k(x)[F,G]`, the rest of the major tower, or `J(F,G)=1`.

### 3.4 First direct outer/minor/Jacobian overlap

The first global outer prefix was pulled through (2.1), not matched by name.
Put `d32=C3_(32,0)` and
`d31=C3_(31,0)+C2_(21,0)H_(10,0)`.  In either minor branch its first three
pole rows for each polynomial are

```text
F: A3_(98,0),
   A3_(97,0)+A2_(65,0)d32,
   A3_(96,0)+A2_(64,0)d32+A2_(65,0)d31+d32^3+u A3_(97,1);
G: B2_(65,0),
   B2_(64,0)+B1_(32,0)d32+d32^2,
   B2_(63,0)+B1_(31,0)d32+B1_(32,0)d31+2d32d31+u B2_(64,1).
```

They occur at exponents `(-80,-79,-78)` and `(-53,-52,-51)` for branch 2,
and `(-187,-185,-183)` and `(-124,-122,-120)` for branch 52.  The six rows
have six unit pivots.  In the degree-162 Jacobian face,
`[x^145 y^17]J=1764 A3_(98,0)` is dependent on the first pole row;
`[x^144 y^18]J` pivots `1698 A3_(97,1)`.  Continuing contiguously through
`[x^136 y^26]J` gives nine new pivots; the last row is the first to meet
`B2_(65,0)` and, after reduction, pivots `1170 A2_(65,0)`.  Hence 16 rows have
exact rank 15, with no residual.

| commuting stage | cumulative rank | `delta=2` dimension | `delta=5/2`, `b0=0` dimension |
|---|---:|---:|---:|
| common-`h3` base | 0 | 6704 | 6702 |
| six direct pole rows | 6 | 6698 | 6696 |
| first Jacobian row | 6 | 6698 | 6696 |
| Jacobian rows 2 through 10 | 7 through 15 | 6697 through **6689** | 6695 through **6687** |

All 15 pivots are outer `A/B` coordinates, disjoint from the preceding
`H,C2,C3` pivots, so these dimension subtractions are exact over both bases.
With `b0` restored, branch 52 ends at 6688.  Direct substitution rechecks all
rows; a perturbed duplicate reduces to 1.  This is
`COUNTING-BOUND[FIRST-GLOBAL-FG/J-BAND]`, not the rank of the full ideals.
The next common system adds `[x^135 y^27]J`, pole rows `F_(95,*)/G_(62,*)`
(branch-2 exponents `-77/-50`, branch-52 `-181/-118`), and the matching
unresolved **outer-`F,G`** `D1` major-order rows.

## 4. Calibration controls

### 4.1 Moh's `(64,48)` parent / reduced `(16,12)` kill

For `s=3,u_s=1`, the trivial minor side adds no variables or rows. Dividing the
parent degrees by 4 gives Moh's p.208 `(16,12)` chart. Both readings were tested:

* the printed repeated `c5`; and
* the compiler convention absorbing `alpha1` and using a distinct `c6`.

The source distinction is recorded at
[`jet-edge-1612...md:68`](/tmp/jc2-lane.eijAga/inputs/jet-edge-1612-sol56-20260903.md:68);
`OPEN[PRINTED-C5-EMENDATION]` remains for general reuse even though both tested
control ideals are empty.

Each has 18 unknowns (17 coefficients and nonzero Jacobian scalar `kappa`) and
77 rows. In the declared rational ring, adjoining `T*kappa-1` gives reduced
Groebner basis `[1]`; the raw ideal still has its `kappa=0` origin. Ring,
wrapper, and controls pass. Verdict:

```text
SATURATED-EMPTY[P208-COMMON-POLYNOMIAL-ANSATZ].
```

The independent charged order spine also reproduces the kill: 23 rows in 18
unknowns reduce by seven `Q*` pivots to 15 rows in 11 variables; after four
more affine pivots over `Q[z]/(54z^2-36z+5)`, the terminal element
`20z-10/3` is a unit, with explicit identity
`(20z-10/3)(27/10-27z/5)-1=-2(54z^2-36z+5)`.
This is an exact characteristic-zero calibration certificate, not evidence that
the uncomputed `(99,66)` ideal is empty. The 77-row and order-spine counts are
independently recorded at
[`moh9966-B-lift...md:802`](/tmp/jc2-lane.eijAga/inputs/moh9966-B-lift-sol56-20260903.md:802).

### 4.2 A genuine automorphism that must survive

For `a!=0`, compose the two triangular affine automorphisms

```text
T1(x,y)=(a*x+y,y),
T2(u,v)=(u,((a-1)u+v)/a).
```

Their determinants are `a` and `1/a`, and the composition is

```text
F=a*x+y,             G=(a-1)*x+y,
J(F,G)=1,            x=F-G, y=aG-(a-1)F.                (4.1)
```

Both are monic in `y` with `deg=deg_y=1`. Their projective closures meet the
line at infinity at the two distinct points
`P_F=[1:-a:0]` and `P_G=[1:1-a:0]`. At these points the exact jets are
`(tF,tG)=(pi,pi-1)` and `(pi+1,pi)`. In the shared ansatz
`F=A*x+y,G=C*x+y`, both point charts and the direct Jacobian reduce to the same
row `A-C-1`; the two-variable family has dimension one, and the slice `A=2`
gives the rational witness `(2x+y,x+y)` of dimension zero.

This is `EXACT-AUTOMORPHISM / SURVIVES[UNIVERSAL-GLOBAL-CHECKS]`. The special
`s=3` tower and principal-minor split are
`NOT-APPLICABLE[degrees (1,1)]`; the control tests only that the common-global
coefficient plumbing and direct Jacobian do not falsely kill an automorphism
with one distinct point on each of the two coordinate-fibre closures. It is not
a nontrivial Moh/Xu major/minor configuration.

## 5. Reproducibility and controls

All new writes are under `box/g9966-20260903/` except this report. The main
artifact manifest is
[`artifacts.sha256`](/home/ubuntu/jc2/box/g9966-20260903/artifacts.sha256);
the calibration and Xu extension have their own validated manifests.

| computation | driver (paired JSON is beside it) | exact outcome | replay cost |
|---|---|---|---:|
| common `h3` leaders; Xu ODE through `s^4` | [`joint_probe.py`](/home/ubuntu/jc2/box/g9966-20260903/joint_probe.py) | 14/14 hashes; row/map checks pass | 52.54 s, 69,324 KiB |
| projected major `h2` | [`major_h2_probe.py`](/home/ubuntu/jc2/box/g9966-20260903/major_h2_probe.py) | 7/7 pivots; dimension 162 | 0.97 s, 53,868 KiB |
| simultaneous major `h3` in `h2` | [`major_tower_structure.py`](/home/ubuntu/jc2/box/g9966-20260903/major_tower_joint/major_tower_structure.py) | rank 396; dimension 120 | 0.45 s, 52,108 KiB |
| raw minor rows | [`minor_row_count.py`](/home/ubuntu/jc2/box/g9966-20260903/minor_row_count.py) | 1,647 / 1,910; no rank claim | 1.19 s, 18,528 KiB |
| first global minor/J prefix | [`first_global_band.py`](/home/ubuntu/jc2/box/g9966-20260903/first_global_band/first_global_band.py) | 16 rows; rank 15; no residual | 12.21 s, 53,760 KiB |
| Xu extension | [`xu_joint_extension.py`](/home/ubuntu/jc2/box/g9966-20260903/xu_joint_extension/xu_joint_extension.py) | consistent through `s^28` | 191.92 s, 185,372 KiB |
| calibrations | [`calibration_controls.py`](/home/ubuntu/jc2/box/g9966-20260903/calibration/calibration_controls.py) | controls pass | 20.26 s |

The probes use declared maps, rational `Q*` pivots, back-substitution, and
positive/perturbed controls. The Xu extension rechecks every scalar row at all
30 ODE levels; calibration asserts its saturation ring and both wrapper
controls. K=16 preprocessing supplied methods, not `(99,66)` evidence: its
tuple and ring differ, as the charged audit warns at
[`xu-delta52-lift...md:305`](/tmp/jc2-lane.eijAga/inputs/xu-delta52-lift-gpt55-20260903.md:305).

## 6. Verdict, bounded quantity, and cheapest decisive test

The principal bounded quantity is now exact:

```text
global fixed-top ambient                         7161 coefficients
major h3-inside-h2 partial family                6720 incl. untouched outer blocks
major h3/h2 + delta=2 common-h3 leader           6704 incl. centre parameters
major h3/h2 + delta=5/2 leader/ODE compatibility 6702, c free/nonzero, b0=0
after first direct-FG/J prefix                    6689 / 6687 respectively
direct Jacobian coefficient slots               <=13,366
```

The 6704/6702 boundary retains 6600 untouched outer variables; the next prefix
pivots 15 of them. None of these counts is evidence that the final variety is
large, and finite-band consistency is not attainment.

For `delta=2`, the deepest complete local `F,G` band is 5 (dimension 59 in its
own slice), and the next system is band 6 with 17 remainder rows. For
`delta=5/2`, the deepest common-`h3` reduced ODE band is `s^28`, dimension 3 at
`c=1` with `b0`, and (3.6) is the exact next system. Neither branch is
inconsistent, so there is no kill certificate to present.

The cheapest genuinely new test is the exact next system in section 3.4:
continue the degree-162 Jacobian at `[x^135 y^27]`, add pole rows
`F_(95,*)/G_(62,*)`, and impose the matching outer-`F,G` `D1` major band, using
`Q*` pivots before Groebner elimination.

An empty localized ideal there would be a valid finite necessary-condition
kill for that branch. A nonempty result remains a counting bound. Only after a
full specialization is recomposed into polynomials
and `F_xG_y-F_yG_x` is checked identically as `1` may it be called a Keller
pair.

FALLACY-v2 audit: no cv flag is identified with a place or cover series; no
lower bound is promoted to attainment; all saturations declare their rings and
controls; raw remainders are checked in their stated quotient; source and
driver variable maps are typed; derivative primes occur only where declared;
and every stopped lift is labeled `COUNTING-BOUND` or `OPEN`. No new exit-price
assertion is made, so no `charge_basis` declaration is emitted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `31595`.
- Body SHA-256:
  `c5693637dd440e33b7c01a4b2dd9bc883d6bdacb0ff323e564f33ebbc9b96c43`.
- Frozen basis: `afb7e21be9164e6fed9748614361f51db26e1410`.
