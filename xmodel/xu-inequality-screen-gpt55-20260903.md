# Xu Final-Root Inequality Screen

Lane: `xu-inequality-screen-gpt55-20260903`.  No ledger edits.  No
`jc2-lean`.  Driver and artifacts are under `box/xuscreen-20260903/`.
`FALLACY-v2` is in force: this is a necessary screen only; survival is not
existence.

## Custody

MEASURED: the eight frozen inputs in `/tmp/jc2-lane.yIqjYn/inputs` were verified
mechanically from `xmodel/xu-inequality-screen-gpt55-20260903.run.v2` by
generating a manifest with `awk` and running `sha256sum -c`.  All returned `OK`.

SOURCE-READ page images created:

```text
box/xuscreen-20260903/source-pages/xu-page-04.png  # Theorem 3.4
box/xuscreen-20260903/source-pages/xu-page-05.png  # Theorem 4.7
box/xuscreen-20260903/source-pages/xu-page-07.png  # Theorem 5.1, Cor. 5.3
box/xuscreen-20260903/source-pages/xu-page-08.png  # (75,50) example
box/xuscreen-20260903/source-pages/xu-page-09.png  # (84,56) examples
box/xuscreen-20260903/source-pages/xu-page-10.png  # Section 7.3 start
box/xuscreen-20260903/source-pages/xu-page-11.png  # Proposition 7.3, Cor. 7.5
box/xuscreen-20260903/source-pages/xu-page-12.png  # Cor. 7.5 and Section 8
box/xuscreen-20260903/source-pages/xu-page-13.png  # (99,66) continuation
```

Layout text used for line citations: `box/xuscreen-20260903/xu-layout.txt`.

## Source Read

SOURCE-READ: Xu defines `pi`-roots on PDF page 1.  With `x=t^-1`, a
`pi`-root is
`sigma=sum_{j<delta_sigma} a_j t^j + pi t^delta_sigma` with
`f(sigma)=f_sigma(pi)t^lambda_sigma+...` and `deg_pi f_sigma>0`.
Its multiplicity is `deg_pi f_sigma`; it is split when `f_sigma(pi)` has
more than one root; it is final when `f_sigma(pi)` has no multiple roots and
degree greater than 1 (`xu-layout.txt:41-51`).

SOURCE-READ: Theorem 3.4 assumes only that `f(x,y)` is monic in `y`; Xu
explicitly says Section 3 does not use the Jacobian condition
(`xu-layout.txt:75-77`).  If `f_xi(sigma)=f_sigma(pi)t^lambda_sigma+...`,
then

```text
I(f_xi, f_y) = - sum_sigma (e(f_sigma(pi))-1) lambda_sigma,
```

where `sigma` runs over all split `pi`-roots of `f_xi`; `e(p)` is the number
of distinct roots of `p` (`xu-layout.txt:176-187`).

SOURCE-READ: From Section 4 onward `(f,g)` is a Jacobian pair
(`xu-layout.txt:203`).  Definition 4.3 calls a root `alpha` of `f_xi` major
if `ord g(alpha)<0` and minor if `ord g(alpha)=0`; in the two-points-at-infinity
case, the roots on the smaller leading-form factor are the principal minor
roots (`xu-layout.txt:217-220`).  Definition 4.6 defines
`D_sigma^h={alpha | h(alpha)=0 and ord(sigma-alpha)=delta_sigma}` and sets
`Pm` to the final minor `pi`-roots and `PM` to the final major `pi`-roots
(`xu-layout.txt:252-259`).

SOURCE-READ: Theorem 4.7 assumes `(f,g)` is a Jacobian pair.  It states:

```text
I(f_xi, f_y) <= deg_y f - 1
                + sum_{sigma in Pm} (|D_sigma^{f_xi}|-1)(delta_sigma-1)

I(f_xi, g) >= 1 + sum_{sigma in Pm} (delta_sigma-1).
```

If there are no final minor roots, Xu states `I(f,f_y)=deg_y f-1` and
`I(f,g)=1` (`xu-layout.txt:260-322`).

SOURCE-READ: Theorem 5.1 assumes `(f,g)` is a Jacobian pair and defines

```text
IM(f,g) = - sum_{sigma in PM} |D_sigma^f| lambda_sigma^g
        = (deg_y g)/(deg_y f + deg_y g)
          sum_{sigma in PM} |D_sigma^f|(1-delta_sigma).
```

Then `I(f_xi,g)=IM(f,g)` (`xu-layout.txt:342-379`).  Xu then defines
`Im(f,g)=1+sum_{sigma in Pm}(delta_sigma-1)` and Corollary 5.3 gives
`IM(f,g) >= Im(f,g)` for a Jacobian pair (`xu-layout.txt:392-397`).

SOURCE-READ: Section 7.3 assumes a monic Jacobian pair, `f` having two points
at infinity, effective index `s>2`, effective quasi-approximate roots
`T_i(f,g) in K[f,g]`, `T_0=g`, `T_1=f`, and `deg T_i=-mu_i`.  With
`d_i=gcd(-mu_0,...,-mu_{i-1})`, the normalized list
`(-mu_0/d_{s+1},...,-mu_s/d_{s+1})` is a characteristic delta-sequence.
If the multiplicity of the principal minor roots of `f` is `m u_s/d_s` with
`u_s<v_s=d_s-u_s`, then the principal-minor multiplicities of
`T_0,...,T_{s-1},T_s` are
`(-mu_0)u_s/d_s, ..., (-mu_{s-1})u_s/d_s, ((-mu_s-2)u_s/d_s)+1`
(`xu-layout.txt:491-501`).

SOURCE-READ: Proposition 7.3 says the order-1 `pi`-root for the principal
minor roots has all `T_{i,sigma_1}(pi)` powers of a common linear polynomial
(`xu-layout.txt:502-574`).  Corollary 7.5 says that if `u_s>1` and a principal
minor `pi`-root has order `delta_sigma < (v_s+1)/(u_s+1)`, then it cannot
split to `u_s` different roots (`xu-layout.txt:577-616`).

## Skeleton Inputs

DERIVED: exact `IM` needs the final major data: every final major root
`sigma`, its order `delta_sigma` or `lambda_sigma^g`, and `|D_sigma^f|`.
Exact `Im` needs the final minor data: every final minor root and its
`delta_sigma`.  A Moh skeleton row does not determine these sets exactly.

DERIVED: a skeleton row does determine `n,m,M_i,d_i,V_i,delta_i`, and the
full-tree level quantities used by the driver:

```text
A_j = increment denominator of delta_j
P_j = V_{j+1} d_j / d_{j+1}
Q_j = V_{j+1} (n-M_j) / d_{j+1}
major threshold = d_j/(n-M_j)
```

At level `j`, a split has one fixed zero multiplicity `b` and nonzero
`A_j`-orbits with multiplicities `v`, satisfying `P_j=A_j sum(v)+b`.
A child is major iff `v>d_j/(n-M_j)`.  The operative row fixes only one
major path `V_j`; sibling split multiplicities are not row data.

DERIVED: for a bottom major child at `j=2` of multiplicity `v`, one final
major root has

```text
|D_sigma^f| = v m/d_2
-lambda_sigma^g = n/(m+n) (1-delta_1),
```

and a nonzero orbit has `A_2` conjugate copies.  This reproduces Xu's
`IM` factors in Section 6.

DERIVED: for a nonprincipal minor child at level `j`, the first order at
which its `g`-order can reach zero is

```text
delta_minor = delta_j + (d_j/(n-M_j)) (1-delta_j)/v.
```

The driver uses one contribution `delta_minor-1` per distinct fixed zero
factor and `A_j(delta_minor-1)` per nonzero orbit.  Exact later splitting of
that minor disc would require extra split data and can only make the exact
`Im` more specific; the screen uses this as a floor.

DERIVED / OPEN: the principal minor contribution is exact at skeleton level
for `u_s=1`: one final principal minor root of order `V_s/u_s=V_s`, matching
Xu's Section 6 examples.  For `u_s>1`, Section 7.3 gives multiplicities and
non-splitting information at order 1, but it does not determine the number of
final principal minor roots or their final orders.  Therefore the promoted
driver uses the most permissive fail-closed value `0` for the principal
minor contribution when `u_s>1`.

DERIVED: the census screen tests only

```text
max_possible(IM) >= min_forced(Im).
```

The maximum and minimum are allowed to come from different split completions.
This is deliberately weaker than exact realizability and is fail-closed.

## Calibration

MEASURED: `box/xuscreen-20260903/xu_screen.py` replays Xu's three worked
Section 6 cases exactly before any census count is trusted.

```text
case                         split data        IM    Im    result
(75,50) split (ii)           A=5; [2,1,1]       4     6    excluded
(84,56) M2=64,V2=2           A=7; [2,1]         4     5    excluded
(84,56) M2=72,V2=5           A=4; b=1; [5]     10     4    not excluded
```

SOURCE-READ: these are exactly Xu's printed numbers:
`(75,50)` split (ii) has `Im=1+(4-1)+10(6/5-1)=6` and `IM=5*4*1/5=4`
(`xu-layout.txt:417-428`); `(84,56;M2=64,V2=2)` has
`Im=1+7(9/7-1)+(3-1)=5` and `IM=4*7*3/21=4`
(`xu-layout.txt:430-442`); `(84,56;M2=72,V2=5)` has
`Im=1+(2-1)+(3-1)=4` and `IM=4*10*3/12=10`
(`xu-layout.txt:443-452`).

DERIVED: the `(75,50;V2=2)` row itself is not killed fail-closed, because the
more permissive split `[2,2]` gives `IM=8`, `Im=4`.  Xu prints that this
alternative is not excluded by the intersection inequality
(`xu-layout.txt:407-416`).

## Measured Census

MEASURED: controls passed:

```text
Moh six pass the operative C_FULL_TREE_POLYNOMIAL_ODE screen: 6/6
Xu calibration cases: 3/3 exact
D<=200 operative rows/groups: 1420 / 686
```

MEASURED: promoted conservative policy:

```text
principal minor floor = V_s/u_s - 1 for u_s=1
principal minor floor = 0 for u_s>1
```

MEASURED: total Xu screen result on the operative `48<=D<=200` census:

```text
rows killed     43 / 1420
groups killed   29 / 686
groups touched  37 / 686
```

MEASURED: by the requested `u_s` phases:

```text
phase    rows  killed rows  groups  killed groups  touched groups
u_s>1     310            9     177              7               8
u_s=1    1110           34     509             22              29
```

MEASURED: strata by `moh_skeleton_full.Skel.s` and post-descent two-point
status for `u_s=1`:

```text
u_s class  s  two-point       rows  killed rows  groups  killed groups
u_s=1      3  not-two-point      9            1       8              1
u_s=1      3  two-point         15            0      14              0
u_s=1      4  not-two-point    302           18     187             12
u_s=1      4  two-point         16            0      13              0
u_s=1      5  not-two-point    584            8     245              6
u_s=1      5  two-point         18            3      12              2
u_s=1      6  not-two-point    162            3      47              1
u_s=1      6  two-point          4            1       3              0
u_s>1      3  NA                19            0      18              0
u_s>1      4  NA                96            4      69              4
u_s>1      5  NA               195            5      90              3
```

MEASURED: killed groups by degree:

```text
84:1, 90:1, 108:1, 120:1, 135:1, 144:6, 150:1,
168:1, 180:8, 192:7, 200:1
```

MEASURED: killed groups at `D<=120`:

```text
n   m   M                         V_s  u_s  rows  bound
84  56  [64,82]                    3    1     1    IMmax=4 < Immin=5
90  60  [45,80,88]                 4    1     2    IMmax=43/7 < Immin=7
108 72  [60,100,106]               3    1     1    IMmax=12/5 < Immin=5
120 90  [75,110,118]               4    1     1    IMmax=30/7 < Immin=7
```

MEASURED: the `D=90` killed group has both operative rows killed:
`V=(2,5,4)` and `V=(3,5,4)`, with the same bound
`IMmax=43/7 < Immin=7`.

MEASURED: seven killed groups are in the previously untouched `u_s>1`
residue:

```text
144  96  [120,132,138,142]      V_s=4  u_s=2  IMmax=27/7 < Immin=5
144  96  [120,132,142]          V_s=8  u_s=4  IMmax=27/7 < Immin=5
144 108  [126,135,142]          V_s=6  u_s=3  IMmax=18/5 < Immin=5
168 112  [84,154,161,166]       V_s=5  u_s=2  IMmax=31/5 < Immin=7
180 120  [150,168,178]          V_s=4  u_s=2  IMmax=36/7 < Immin=8
180 120  [150,170,175,178]      V_s=3  u_s=2  IMmax=11/3 < Immin=4
180 120  [150,174,178]          V_s=4  u_s=2  IMmax=11 < Immin=15
```

MEASURED: the direct Appendix-II target list from the post-POLY report
(`u_s=1`, `s_eff=2`, two-point) is untouched: 18 rows / 17 groups, 0 kills.
The K=16 ray entries at `D=64,112,160` survive with bounds
`9>=3`, `15>=3`, `21>=3`.

MEASURED: Moh's six under the promoted screen:

```text
row                         IMmax  Immin  Xu screen
(64,48)                       9      3    survives
(84,56) M2=64,V2=2            4      5    killed
(84,56) M2=72,V2=5           10      4    survives
(75,50) V2=3                  9      5    survives
(75,50) V2=2                  8      4    survives
(99,66)                      16      1    survives under u_s>1 fail-closed floor
```

## Verdict

DERIVED / MEASURED: `IM>=Im` is a new independent skeleton screen over the
operative post-POLY census.  It sees a global final-root intersection-number
deficit: even after maximizing final-major capacity over all full-tree
embeddings and minimizing forced final-minor charge, some rows have
`IMmax<Immin`.  PATH-ARITH, full tree, ODE, and POLY do not test this global
intersection balance; all 29 killed groups were operative survivors before
this lane.

MEASURED: the screen kills 29 groups at `48<=D<=200`, including 7 groups in
the `u_s>1` residue that POLY left untouched.  It also reproduces Xu's
published `(84,56;M2=64,V2=2)` exclusion and the split-specific
`(75,50)` split (ii) exclusion.

MEASURED: it does not touch 657 operative groups, does not touch the 17
direct two-point `s_eff=2` Appendix-II target groups, does not kill the K=16
ray entries in range, and does not settle `(99,66)`.  In particular,
`(99,66)` survives here because the promoted fail-closed `u_s>1` principal
minor floor is `0`.

OPEN[principal-us-gt-1-exact]: Section 7.3 supplies principal-minor
multiplicities and non-splitting at order 1, but not the final principal
minor root count and final orders for `u_s>1`.  Bounded quantity used here:
principal contribution floor `0`.  Cheapest test: source a theorem or add
explicit principal split data giving the final principal minor roots and
orders, then rerun the same driver with that floor.

OPEN[minor-disc-exact-Im]: nonprincipal minor children are charged only by
the first zero-order floor
`delta_j + (d_j/(n-M_j))(1-delta_j)/v - 1`.  Exact `Im` needs the later final
minor split data.  Cheapest test: record the final minor roots and orders for
each minor child in the full split tree.

OPEN[attainment-correlation]: the promoted census screen compares an
independent `max(IM)` bound with an independent `min(Im)` floor.  This is
fail-closed but not exact.  Cheapest test: replace the two independent extrema
with an actual split tree, or with a same-tree optimization of `IM-Im`, before
claiming any survivor is compatible with equality.

No new exit-price assertion is made, so no `charge_basis` line is present.

<!-- BODY-END -->
