# Xu principal-minor distance floor — derivation and `D <= 200` census

Lane: `xu-principal-floor-sol56-20260903`.  Verdict: **CONFIRMED, with a
type correction**.  For every actual principal split tree satisfying Xu's
hypotheses, the principal contribution to the quantity Xu calls `Im` obeys

```text
C_pr^Im := sum_{sigma in P_m,principal} (delta_sigma - 1)
         >= V_s/u_s - 1.
```

Thus the promoted `u_s>1` floor `0` can safely be replaced by
`V_s/u_s-1`.  The expression with the extra factor
`(|D_sigma^{f_xi}|-1)` in the task is not `Im`: it is the correction term in
Theorem 4.7(i).  For that weighted expression, `V_s/u_s-1` is valid but not
the best cardinality-only floor; Section 3 below gives the stronger bound.

The sharpened replay kills 48 rows / 33 groups, versus 43 / 29 under the
charged policy: **+5 rows / +4 fully killed groups**.  Neither `(99,66)` nor
the named `D=108` row dies.  The direct two-point list and the three `K=16`
ray entries are unchanged.  This remains the scoped necessary screen
`C_FULL_TREE_POLYNOMIAL_ODE AND XU`; survival is not attainment.

## 1. Custody, page images, and variable map

MECHANICAL-CHECK: the manifest was generated from the
`charged_input_<i>_sha256` and `charged_input_<i>_basename` fields of
`xmodel/xu-principal-floor-sol56-20260903.run.v2` with `awk`, streamed through
`tee`, and checked with `sha256sum -c`.  All 10 frozen inputs in
`/tmp/jc2-lane.EOjB13/inputs` returned `OK`; no digest was retyped.
The generated manifest is `box/xufloor-20260903/charged-inputs.sha256`.

SOURCE-READ page images are under `box/xufloor-20260903/source-pages/`:

| source content | printed page | PDF page (1-based) | image name |
|---|---:|---:|---|
| Xu Lemma 4.1, Definition 4.3, Lemma 4.4 start | 4 | 4 | `xu-printed-p4-pdf-p4.png` |
| Xu Lemma 4.4(ii), Definition 4.6, Theorem 4.7 | 5 | 5 | `xu-printed-p5-pdf-p5.png` |
| Xu proof of Theorem 4.7, (4.3)--(4.4) | 6 | 6 | `xu-printed-p6-pdf-p6.png` |
| Xu Section 7.3 and Proposition 7.3 start | 10 | 10 | `xu-printed-p10-pdf-p10.png` |
| Xu Proposition 7.3 proof, Corollary 7.5 | 11 | 11 | `xu-printed-p11-pdf-p11.png` |
| Moh Proposition 6.1 and proof | 190--193 | 51--54 | `moh-printed-p190-pdf-p51.png` through `moh-printed-p193-pdf-p54.png` |
| Moh discussion after 6.1 | 194 | 55 | `moh-printed-p194-pdf-p55.png` |
| Moh Proposition 6.2 | 195--196 | 56--57 | `moh-printed-p195-pdf-p56.png`, `moh-printed-p196-pdf-p57.png` |
| Moh Proposition 6.3 | 197--198 | 58--59 | `moh-printed-p197-pdf-p58.png`, `moh-printed-p198-pdf-p59.png` |
| Moh Proposition 6.4 | 198--199 | 59--60 | `moh-printed-p198-pdf-p59.png`, `moh-printed-p199-pdf-p60.png` |

This corrects a pagination ambiguity: printed pp.196--199 are PDF pages
57--60, but Proposition 6.1 starts on p.190 and Proposition 6.2 on p.195.
PDF pages 51--60 were read as images.

The source-to-driver map is load-bearing:

| source symbol | driver/skeleton field | meaning |
|---|---|---|
| `m=deg_y f` | `S.m` | number of roots of `f_xi` |
| `n=deg_y g` | `S.n` | degree of `g` |
| Xu/Moh lowercase `v_s` | `S.V[S.s]`, reported as `V_s` | larger terminal multiplicity parameter |
| `u_s=d_s-v_s` | `u_s_of(S)` | smaller, principal parameter |
| `d_s=u_s+v_s` | `S.d[S.s]` | terminal gcd |

Xu Definition 4.3 calls the roots on the smaller factor
`(y-a_1x)^u`, `u<v`, principal minor roots.  Calling that geometric factor
the first or second point is only an external label; the proof uses the
smaller factor and not the label.

## 2. What the cited sources actually say

SOURCE-READ, Xu p.4, Lemma 4.1: for
`f_x g_y-f_y g_x=J(x,y)` and a Puiseux series `alpha`,

```text
g_y(alpha) d f(alpha)/dt - f_y(alpha) d g(alpha)/dt
    = -J(t^-1,alpha)t^-2.                                      (4.1)
```

From Section 4 onward Xu assumes a Jacobian pair.  Definition 4.3 says an
`f_xi` root is major when `ord g(alpha)<0` and minor when
`ord g(alpha)=0`; every principal root in the two-point leading form is
minor.  Lemma 4.4 says the related final order is `<1` for a major root and
`>1` for a minor root.  In the minor half of its proof Xu explicitly uses
`lambda_sigma^f=lambda_sigma^g=0`.

SOURCE-READ, Xu p.5, Definition 4.6:

```text
D_sigma^h = {alpha : h(alpha)=0 and ord(sigma-alpha)=delta_sigma},
P_m = final minor pi-roots of f_xi,
P_M = final major pi-roots of f_xi.
```

Theorem 4.7 distinguishes two sums:

```text
(i)  I(f_xi,f_y) <= deg_y f - 1
       + sum_{sigma in P_m} (|D_sigma^{f_xi}|-1)(delta_sigma-1),

(ii) I(f_xi,g) >= 1 + sum_{sigma in P_m}(delta_sigma-1).
```

Its p.6 proof applies Lemma 4.1 at a root `alpha` of `f_xi`.  For a minor
root it defines the related final order by the maximum contact with a root
of `g` and states

```text
ord f_y(alpha) = -delta_sigma.
```

This is also the specialization of Proposition 3.3(i):
`f_y(sigma)=f'_sigma(pi)t^(lambda_sigma^f-delta_sigma)+...`;
finality makes the relevant value of `f'_sigma` nonzero, and the minor case
has `lambda_sigma^f=0`.  Equation (4.3) partitions the roots of `f_xi` among
the `D_sigma^{f_xi}` for `P_m` and `P_M`.  Subtracting (4.4) from (4.3)
proves the unweighted inequality (ii).  Corollary 5.3, through Theorem 5.1,
is the charged `IM >= Im` screen with

```text
Im = 1 + sum_{sigma in P_m}(delta_sigma-1).
```

SOURCE-READ, Xu pp.10--11, Section 7.3: under a Jacobian pair monic in `y`,
two points at infinity, and the effective quasi-approximate-root data, the
number of principal roots of `f_xi` is

```text
N = m u_s/d_s,
```

and `u_s<v_s=d_s-u_s`.  The stated principal multiplicities for
`T_0,...,T_s` are `(-mu_i)u_s/d_s` for `i<s` and
`(-mu_s-2)u_s/d_s+1` for `T_s`.  Proposition 7.3 says their order-1 leading
polynomials are powers of a common linear polynomial; its proof obtains
`p(pi)=(pi-a)^u_s`.  This supplies order-1 non-splitting, not a final-root
count or final order.  Corollary 7.5 constrains a split into `u_s` roots
below `(v_s+1)/(u_s+1)` but likewise does not state the desired floor.

SOURCE-READ, Moh pp.190--199: Proposition 6.1 defines a combined minor disc
from selected roots of `g product T_i^psi` and proves only its radius
`delta^*>=1`; p.193 expressly says the proposition does not determine that
radius beyond this estimate.  P.194 writes roots in the top minor disc with
a common jet through exponents `<1`.  Proposition 6.2 supplies the transformed
degree counts, including the `u_s/d_s` packet.  Proposition 6.3 **assumes**
`delta^*>=v_s/u_s`; it does not prove that premise.  Proposition 6.4 proves
the premise only after adding `u_s=1`.

Therefore the new result must not be typed as a Moh assertion
`delta^*>=V_s/u_s` for `u_s>1`.  Moh's `delta^*` is the minimum contact in a
combined `g,T_i` disc.  The quantity bounded below here is each related
final `f_xi` order `delta_sigma`.  Moh's general `>=1` result and Xu
Proposition 7.3 are consistent with the result because `V_s/u_s>1`, but
they are not the numerical step that upgrades `1` to `V_s/u_s`.

## 3. Typed lemma and proof

**Lemma `PFR-DIST` (principal final-root distance floor).**  Let `K` be
algebraically closed of characteristic zero.  Let `(f,g)` be a Jacobian pair
monic in `y`, let `xi` be generic, and assume Xu's two-point-at-infinity
hypotheses.  At the terminal skeleton level put

```text
d=d_s,  u=u_s,  V=V_s=v_s=d-u,  0<u<V,
N=m u/d,  Q=m V/d.
```

Thus `N` is the number of principal `f_xi` roots and `Q=m-N` is the number
at the other infinity point.  For every final minor `pi`-root `sigma`
related to a principal root,

```text
delta_sigma >= Q/N = V/u.                                    (3.1)
```

Consequently, if `P_pr` is the set of final roots covering the principal
packet,

```text
sum_{sigma in P_pr}(delta_sigma-1) >= V/u-1.                  (3.2)
```

The bound holds for every possible actual Puiseux split tree; it makes no
assumption on the number or sizes of its later principal blocks.

**Proof.**  Fix a principal root `alpha` and let `sigma` be its related final
root.  Lemma 4.2 and the decomposition used in Theorem 4.7's proof supply
such final roots.  Definition 4.3 makes `alpha` minor, so Lemma 4.4 puts
`sigma` in `P_m`, gives `delta_sigma>1`, and supplies
`lambda_sigma^f=0`.  The p.6 step of Theorem 4.7's proof gives

```text
delta_sigma = -ord f_y(alpha).                               (3.3)
```

Because `f_xi` is monic, factor it over the Puiseux field.  At a simple root,

```text
ord f_y(alpha)
  = sum_{beta != alpha, f_xi(beta)=0} ord(alpha-beta).        (3.4)
```

Every one of the `Q` roots at the other point has a different coefficient
of `t^-1`, hence contact exactly `-1` with `alpha`.  If `C` is the set of
`N` principal roots, (3.3)--(3.4) become

```text
delta_sigma
  = Q - sum_{beta in C\{alpha}} ord(alpha-beta).              (3.5)
```

For every `beta` in `C\{alpha}` the contact is at most `delta_sigma`.  A root
outside `D_sigma^{f_xi}` separated earlier, so its contact is smaller.  A
root inside that final disc has contact exactly `delta_sigma`: contact
strictly greater would give two branches with the same root of
`f_sigma(pi)`, contrary to finality, which requires `f_sigma` squarefree.
This is the per-tree step; it covers every split pattern rather than a
chosen or representative split.  Therefore

```text
delta_sigma >= Q-(N-1)delta_sigma,
N delta_sigma >= Q,
delta_sigma >= V/u.
```

The `D_sigma` sets used on p.6 partition the `f_xi` roots.  A principal set
cannot mix with the other point because its final order is `>1` while the
cross-point contact is `-1`.  Hence at least one final minor root covers the
nonempty principal packet.  Since `V/u-1>0`, summing (3.1) over the one or
more principal final roots proves (3.2).  QED.

The floor in (3.2) is sharp relative to the distance data, not asserted to
be attained by a Jacobian pair.  The abstract one-stage tree in which all
`N` principal roots separate at `delta=Q/N` makes every inequality above an
equality and respects non-splitting through order 1.  This only shows that a
larger universal number cannot be extracted from these skeleton/contact
facts; under `FALLACY-v2` it is not an existence witness.

### The weighted expression in the task

Define the different, Theorem 4.7(i) quantity

```text
W_pr = sum_{sigma in P_pr}
         (|D_sigma^{f_xi}|-1)(delta_sigma-1).
```

Write `k_sigma=|D_sigma^{f_xi}|` and `r=|P_pr|`.  Finality gives
`k_sigma>=2`, and the p.6 partition gives `sum k_sigma=N`.  Hence
`r<=floor(N/2)` and the termwise bound (3.1) gives

```text
W_pr >= (N-r)(V/u-1)
     >= ceil(N/2)(V/u-1).                                    (3.6)
```

Thus `V/u-1` answers the actual `Im` question, but is not the sharp
cardinality-based answer to the displayed weighted sum.  Bound (3.6) is
sharp for just these contact and partition constraints as an infimum: take
`floor(N/2)` terminal blocks of size two (and one size three when `N` is
odd), give distinct blocks common contact `c=V/u-epsilon`, and choose each
terminal order
`delta_i=V/u+(N-k_i)epsilon/k_i`.  Equation (3.5) holds and the weighted sum
tends down to (3.6) as positive rational `epsilon` tends to zero.  This is
again an abstract sharpness check, not attainment.

### Principal contribution to `IM`

It is exactly zero, so its best upper bound is `0`.  Xu Definition 4.3 makes
every principal root minor.  Lemma 4.4 puts its related final root at order
`>1`, whereas final major roots have order `<1`.  Xu's

```text
IM = n/(m+n) sum_{sigma in P_M}|D_sigma^f|(1-delta_sigma)
```

sums only `P_M`.  No principal final root can enter that index set.  There
is no conditional principal-major capacity to add to `IM_max`.

## 4. Driver change and controls

`box/xufloor-20260903/xu_screen_candidate.py` is the charged driver copied
against the current frozen input directory.  The tree enumerator, operative
`POLY_ODE` filter, nonprincipal first-zero floors, and independent
optimizations are unchanged.  The only mathematical policy change is to
retain two parallel columns:

```text
principal_minor_floor_promoted = V_s/u_s-1 if u_s=1, else 0
principal_minor_floor_candidate = max(V_s/u_s-1,0) for every u_s>0

Im_min_promoted  = 1 + promoted floor  + tree_minor_min
Im_min_candidate = 1 + candidate floor + tree_minor_min.
```

Both verdict columns use the same `IM_max`.  The candidate kills a row only
when `IM_max < Im_min_candidate`.  The charged fail-closed logic is therefore
preserved: an actual tree has `IM<=IM_max` and `Im>=Im_min_candidate`, even
though the two extrema may come from different completions.

MEASURED: a clean replay completed with exit status zero.  The independent
`audit_results.py` assertions also passed.  Xu's three printed calibrations
remain exact:

| Xu case | `IM` | `Im` | reproduced result |
|---|---:|---:|---|
| `(75,50)` split (ii) | 4 | 6 | excluded |
| `(84,56; M_2=64,V_2=2)` | 4 | 5 | excluded |
| `(84,56; M_2=72,V_2=5)` | 10 | 4 | not excluded |

## 5. Sharpened `D <= 200` census

MEASURED:

| policy | killed rows / 1420 | killed groups / 686 | touched groups / 686 |
|---|---:|---:|---:|
| charged/promoted | 43 | 29 | 37 |
| sharpened | 48 | 33 | 42 |
| delta | **+5** | **+4** | **+5** |

The `u_s>1` portion has 310 rows / 177 groups.  The promoted screen killed
9 rows / 7 groups and touched 8 groups, leaving the 170 promoted-surviving
groups named in the task.  The sharpened screen kills 14 rows / 11 groups
and touches 13 groups: four of those 170 groups now die, leaving 166 not
fully killed.  All 1,110 `u_s=1` rows have identical promoted/candidate
floor, `Im`, and verdict.

The four newly killed groups are:

| group `(n,m; M; V_s,u_s)` and killing row `V_2,...,V_s` | floor added | `IM_max` | old `Im_min` | new `Im_min` |
|---|---:|---:|---:|---:|
| `(168,112; [154,161,166]; 5,2)`, `V=(5,10,5)` | `3/2` | 5 | `11/3` | `31/6` |
| `(180,144; [162,168,178]; 4,2)`, `V=(4,5,4)` | 1 | `32/7` | 4 | 5 |
| `(192,128; [160,184,190]; 5,3)`, `V=(11,10,5)` | `2/3` | `22/3` | 7 | `23/3` |
| `(198,132; [154,187,196]; 7,4)`, `V=(8,7,7)` | `3/4` | `80/13` | 6 | `27/4` |

The fifth newly killed row is
`(192,128; [160,176,184,190]; V=(11,10,5,5); V_s=5,u_s=3)`, with
`22/3 < 23/3` after adding `2/3` to the old `Im_min=7`.  Its group is only
touched: the sibling `V=(5,10,5,5)` survives with `10 >= 5/3`.

For completeness, all 11 fully killed `u_s>1` groups under the sharpened
screen are listed below; `NEW` marks the four above:

```text
(144, 96; [120,132,138,142]; V_s=4,u_s=2)   27/7 < 6
(144, 96; [120,132,142];     V_s=8,u_s=4)   27/7 < 6
(144,108; [126,135,142];     V_s=6,u_s=3)   18/5 < 6
(168,112; [84,154,161,166];  V_s=5,u_s=2)   31/5 < 17/2  [2 rows]
(168,112; [154,161,166];     V_s=5,u_s=2)   5 < 31/6      NEW
(180,120; [150,168,178];     V_s=4,u_s=2)   36/7 < 9
(180,120; [150,170,175,178]; V_s=3,u_s=2)   11/3 < 9/2
(180,120; [150,174,178];     V_s=4,u_s=2)   11 < 16
(180,144; [162,168,178];     V_s=4,u_s=2)   32/7 < 5      NEW
(192,128; [160,184,190];     V_s=5,u_s=3)   22/3 < 23/3  NEW
(198,132; [154,187,196];     V_s=7,u_s=4)   80/13 < 27/4 NEW
```

Targets and non-regressions:

- `(99,66; M=(-66,77,97); V=(8,8))` survives.  The new principal floor is
  `8/3-1=5/3`, so total `Im_min=8/3`, while `IM_max=16`.
- `(108,72; M=(-72,81,106); V=(7,7))`, `u_s=2`, survives.  Its new floor is
  `7/2-1=5/2`, total `Im_min=7/2`, and `IM_max=21`.
- The direct post-descent `s_eff=2` two-point list remains 18 rows / 17
  groups with zero killed or touched rows.
- The named `K=16` ray rows remain `(D,IM_max,Im_min)=(64,9,3)`,
  `(112,15,3)`, `(160,21,3)`.  They have `u_s=1`, so their columns are
  literally unchanged.

Artifacts: `results.json` is the full row census; `audit_summary.json` is the
compact checked extraction; `run.log` and `audit.log` record the runs;
`CENSUS-README.md` gives the replay commands.  All are confined to
`box/xufloor-20260903/`.

## 6. Verdict and remaining bounded opens

**PROMOTE (scoped):** replace the `u_s>1` principal `Im` floor `0` by
`V_s/u_s-1` in the Xu necessary screen.  `PFR-DIST` is termwise, so the floor
holds for every actual split tree; it is not inferred from a representative,
an optimized witness, Moh's conditional Proposition 6.3, or an attainment
assumption.  The formerly open principal-floor gate is closed.  The weighted
Theorem 4.7(i) quantity remains separately typed and was not fed into the
Corollary 5.3 driver.

`OPEN[principal-Im-exact]`: bounded quantity is
`C_pr^Im=sum(delta_sigma-1)`, now certified below by `V_s/u_s-1`; neither its
exact value nor an upper bound is skeleton-determined.  Cheapest test: obtain
the actual final principal `D_sigma` partition and each final order, then sum
once.  Do not replace the floor by equality without that data.

`OPEN[minor-disc-exact-Im]`: bounded quantity is the nonprincipal contribution
to `Im`; the driver still uses the charged first-zero-order floor for every
minor child.  Cheapest test: record that child's later final-minor split
blocks and orders and replace only its floor by the resulting exact sum.

`OPEN[attainment-correlation]`: bounded quantities are the separately
optimized `IM_max` and `Im_min`.  Cheapest test: optimize `IM-Im` on one
common full-tree completion.  Until then, kills are necessary contradictions
but survivors do not certify compatible attainment.

`OPEN[99-66-and-108-after-floor]`: the bounded comparisons are respectively
`16 >= 8/3` and `21 >= 7/2`; this gate does not decide either target.
Cheapest Xu-side test is the actual final-root partition/orders plus a
same-tree `IM-Im` evaluation.  On the Moh side, keep the separate combined
minor radius `delta^*` and its general-point jet typed as such; Proposition
6.1 alone supplies only `delta^*>=1` when `u_s>1`.

No exit-price assertion is introduced, so no `charge_basis` declaration is
applicable.  No ledger, `jc2-lean`, ideation file, or named in-progress lane
report was edited.

<!-- BODY-END -->
