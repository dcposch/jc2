# Xu same-tree screen, exact `I(f_xi,f_y)` check

Lane: `xu-sametree-gpt55-20260903`.  Verdict: **CONFIRMED, no new kills**.
The same-tree optimisation of `IM-Im` was implemented over the frozen
`C_FULL_TREE_POLYNOMIAL_ODE` finite tree model with the sharpened principal
floor `V_s/u_s-1`.  It is row-identical to the sharpened independent-extrema
policy on `48 <= D <= 200`: **48 rows / 33 groups killed**.  Adding Xu
Theorem 3.4's exact `I(f_xi,f_y)` formula plus Theorem 4.7(i) gives no
additional independent constraint on a fixed tree: Xu's equation (4.3)
makes the Theorem 4.7(i) slack equal to the same `IM-Im` slack.

No ledger, `jc2-lean`, ideation file, or named in-progress lane report was
edited.  No exit-price assertion is introduced, so no `charge_basis` line is
applicable.

## 1. Custody and artifacts

MECHANICAL-CHECK: the manifest was generated from
`xmodel/xu-sametree-gpt55-20260903.run.v2` using its
`charged_input_<i>_sha256` and `charged_input_<i>_basename` fields and then
checked with `sha256sum -c`.  All 12 frozen inputs in
`/tmp/jc2-lane.XDZrUG/inputs` returned `OK`; no digest was retyped.  The
materialized manifest and check log are:

```text
box/xusametree-20260903/charged-inputs.sha256
box/xusametree-20260903/sha256check.log
```

SOURCE-READ page images from the frozen Xu PDF:

| image | printed page | contents read |
|---|---:|---|
| `box/xusametree-20260903/source-pages/xu-page-04.png` | 4 | Theorem 3.4; Lemma 4.1; start of Lemma 4.2/Def. 4.3/Lemma 4.4 |
| `box/xusametree-20260903/source-pages/xu-page-05.png` | 5 | Lemma 4.4(ii); Cor. 4.5; Def. 4.6; Theorem 4.7 |
| `box/xusametree-20260903/source-pages/xu-page-06.png` | 6 | proof of Theorem 4.7; equations (4.3), (4.4); Cor. 4.8 |
| `box/xusametree-20260903/source-pages/xu-page-07.png` | 7 | Cor. 4.9; `IM`; Theorem 5.1 |
| `box/xusametree-20260903/source-pages/xu-page-08.png` | 8 | Cor. 5.2; `Im`; Cor. 5.3; start of the `(75,50)` case |

Layout text used for citations: `box/xusametree-20260903/xu-layout.txt`.
Drivers and logs:

```text
box/xusametree-20260903/xu_sametree.py
box/xusametree-20260903/same_tree_results.json
box/xusametree-20260903/audit_sametree.py
box/xusametree-20260903/audit_summary.json
box/xusametree-20260903/run.log
box/xusametree-20260903/audit.log
box/xusametree-20260903/candidate_compare.log
```

`candidate_compare.log` confirms row-level equality between this driver's
independent extrema and the frozen `xu_screen_candidate.py` bounder: `0`
mismatches.

## 2. Source read: exact quantities and Xu constraints

SOURCE-READ, Xu p.4, Theorem 3.4 (`xu-layout.txt:176-187`): for `f` monic
in `y`,

```text
I(f_xi, f_y) = - sum_sigma (e(f_sigma(pi))-1) lambda_sigma,
```

where `sigma` ranges over all splitting `pi`-roots of `f_xi`.  Section 3 is
not using the Jacobian hypothesis (`xu-layout.txt:75-77`).  Thus
`I(f_xi,f_y)` is an exact function of the full split tree `T` of `f_xi`
including each splitting exponent and the number of distinct children.
Equivalently, for a full ultrametric root tree,
`I_T = sum_alpha S_T(alpha)` with
`S_T(alpha)=-ord f_y(alpha)=-sum_{beta != alpha} ord(alpha-beta)`.

SOURCE-READ, Xu p.4, Lemma 4.1 and Def. 4.3 (`xu-layout.txt:193-220`):
from this point Xu assumes a Jacobian pair.  A root `alpha` of `f_xi` is
major if `ord g(alpha)<0`, minor if `ord g(alpha)=0`; in the two-point
leading-form case, the roots on the smaller factor are the principal minor
roots.

SOURCE-READ, Xu pp.5-6, Lemma 4.4 and Theorem 4.7 proof
(`xu-layout.txt:226-241`, `275-322`): for a related final minor root,
`ord f_y(alpha)=-delta_sigma`, hence `delta_sigma=S_T(alpha)`.  The exact
tree therefore determines every final minor order once the final minor
partition is part of `T`.  It also determines

```text
Im_T = 1 + sum_{sigma in P_m}(delta_sigma - 1).
```

For major roots, Lemma 4.1 gives `ord g(alpha)=S_T(alpha)-1`, so

```text
IM_T = sum_{major alpha}(1-S_T(alpha)),
```

which is the same quantity Xu later denotes through final major roots.

SOURCE-READ, Xu p.5, Theorem 4.7 (`xu-layout.txt:261-273`): for a Jacobian
pair,

```text
I(f_xi,f_y) <= deg_y f - 1
              + sum_{sigma in P_m} (|D_sigma^{f_xi}|-1)(delta_sigma-1),

I(f_xi,g) >= 1 + sum_{sigma in P_m}(delta_sigma-1).
```

If there are no final minor roots, Xu also states
`I(f,f_y)=deg_y f-1` and `I(f,g)=1`.

SOURCE-READ, Xu p.6, Corollary 4.8 (`xu-layout.txt:323-335`): for a
Jacobian pair the following are equivalent:
`K(f,g)=K(x,y)`, `K[f,g]=K[x,y]`, `I(f,g)=1`, `f` has no minor roots, and
`I(f,f_y)=deg_y f-1`.  This is not an extra counterexample screen here:
the operative two-point rows have principal minor roots, and using
`K[f,g]=K[x,y]` would be proving invertibility, not a necessary condition on
counterexample rows.

SOURCE-READ, Xu p.7, Theorem 5.1 (`xu-layout.txt:342-379`):
for a Jacobian pair, `I(f_xi,g)=IM(f,g)`, where

```text
IM(f,g) = - sum_{sigma in P_M} |D_sigma^f| lambda_sigma^g
        = deg_y g/(deg_y f+deg_y g)
          sum_{sigma in P_M}|D_sigma^f|(1-delta_sigma).
```

SOURCE-READ, Xu p.8, Corollary 5.3 (`xu-layout.txt:392-397`): defining
`Im(f,g)=1+sum_{sigma in P_m}(delta_sigma-1)`, Xu combines Theorem 4.7 and
Theorem 5.1 to obtain `IM(f,g) >= Im(f,g)` for a Jacobian pair.

SOURCE-READ conclusion on skeleton exactness: Xu pp.4-8 give exact
`I(f_xi,f_y)` from the full split tree, exact `IM` and exact `Im` from the
full final major/minor tree, and necessary Jacobian inequalities among
them.  They do **not** give an exact formula for `deg_x Res_y(f_xi,f_y)` from
only `(n,m,M,V,d)`, nor a Milnor-number/genus formula determining it from
the skeleton.  The only `deg_y f-1` equalities on these pages are the
no-final-minor case of Theorem 4.7(iii), Cor. 4.8, and the embedded-line
Cor. 4.9 (`xu-layout.txt:336-339`), not a general skeleton equality.

## 3. Same-tree identity for the `I` constraint

Let

```text
W_T = sum_{sigma in P_m} (|D_sigma^{f_xi}|-1)(delta_sigma-1).
```

Xu's equation (4.3) on p.6 gives, on the same tree,

```text
I(f_xi, f_y g) = deg_y f + sum_{sigma in P_m}|D_sigma^{f_xi}|(delta_sigma-1)
               = deg_y f + W_T + (Im_T - 1).
```

Using `I(f_xi,f_y g)=I_T+I(f_xi,g)` and Theorem 5.1,

```text
I_T + IM_T = deg_y f + W_T + Im_T - 1.
```

Therefore

```text
deg_y f - 1 + W_T - I_T = IM_T - Im_T.              (*)
```

So once the test is same-tree, Theorem 3.4's exact `I_T` plus Theorem 4.7(i)
is not a second inequality.  Its slack is exactly the Corollary 5.3 slack.
The driver records the two slacks equal; `audit_sametree.py` asserts equality
on all 1420 rows.  This is the cheapest safe use of Theorem 3.4 under
`FALLACY-v2`: do not invent an unproved skeleton target for `I_T`.

## 4. Implementation

`xu_sametree.py` imports the frozen lane inputs, not mutable workspace copies
(`xu_sametree.py:35-40`).  The operative row set is exactly the charged
`C_FULL_TREE_POLYNOMIAL_ODE` set: `M.census(... full=True)` filtered by
`FT.full_tree_polynomial_ode_ok` (`xu_sametree.py:799-812`).

The finite tree model is the charged model: the selected Moh `V` path must
embed, major children recurse, terminal minor packets contribute their
first final order, polynomial-recentering danger and ODE nondegeneracy are
on (`xu_sametree.py:2-19`, `227-252`, `319-322`).

Per-terminal metrics:

* Principal packet: roots `u_s m/d_s`, order `V_s/u_s`, contribution
  `V_s/u_s-1`, weighted contribution `(u_s m/d_s - 1)(V_s/u_s-1)`, and
  `I` contribution `(u_s m/d_s)(V_s/u_s)` (`xu_sametree.py:244-252`).
* Nonprincipal terminal minor packet: `delta=S_out/N`, checked against the
  charged formula
  `delta_j + (d_j/(n-M_j))(1-delta_j)/v`; its `Im`, weighted, and `I`
  contributions are computed exactly inside the finite terminal-packet model
  (`xu_sametree.py:260-286`).
* Bottom major packet: `(12)/(13)` is checked before contributing; the
  distance identity for `S(alpha)` is asserted before adding `IM`
  (`xu_sametree.py:288-317`).

The same-tree optimisation is a scalar DP over `IM-Im`: `DIFF_MAX` adds
major `IM` contributions and subtracts minor `Im` contributions on the same
completion.  The selected-zero and selected-nonzero embedding cases follow
the charged driver, with cached multiset optimisation rather than
materialising all partitions (`xu_sametree.py:383-504`, `552-588`).  The
independent extrema are computed by the same scalar engine in `IM_MAX` and
`IM_MIN` modes; `candidate_compare.log` verifies row-level equality with the
frozen `xu_screen_candidate.py` bounder.

## 5. Census results

MEASURED (`run.log`, `audit.log`): operative census is 1420 rows / 686
groups.  All three policies are row-identical:

| policy | killed rows / 1420 | killed groups / 686 | touched groups / 686 |
|---|---:|---:|---:|
| sharpened independent extrema | 48 | 33 | 42 |
| same-tree Cor. 5.3 only | 48 | 33 | 42 |
| same-tree + all Xu constraints | 48 | 33 | 42 |

By `u_s` class:

| class | rows | groups | killed rows | killed groups | touched groups |
|---|---:|---:|---:|---:|---:|
| `u_s=1` | 1110 | 509 | 34 | 22 | 29 |
| `u_s>1` | 310 | 177 | 14 | 11 | 13 |

The same-tree slack is smaller than the independent slack on 8 survivor rows
in 5 groups, but none crosses zero.  There are **0 new row kills and 0 new
group kills** from same-tree correlation relative to the sharpened
independent policy, including at `D <= 120`.

All fully killed groups at `D <= 120` remain the four prior groups:

```text
(84,56;  M=[64,82];        V_s=3,u_s=1)  slack -1
(90,60;  M=[45,80,88];     V_s=4,u_s=1)  slack -6/7  [2 rows]
(108,72; M=[60,100,106];   V_s=3,u_s=1)  slack -13/5
(120,90; M=[75,110,118];   V_s=4,u_s=1)  slack -19/7
```

There are 7 killed rows at `D <= 120`; the extra two are in the touched
group `(120,80; M=[60,104,118]; V_s=3,u_s=1)`, whose sibling row survives,
so it is not a fully killed group.

Killer attribution under the all-Xu policy:

```text
rows:   Corollary 5.3 / Theorem 4.7(ii) = 48; survives = 1372
groups: Corollary 5.3 / Theorem 4.7(ii) = 33
        Theorem 3.4 + Theorem 4.7(i)    = 0
        mixed                           = 0
```

Targets and non-regressions:

```text
(99,66; M=[77,97], V=(8,8)):
  survives; independent IM/Im = 16 >= 8/3; same-tree slack = 40/3.

(108,72; M=[81,106], V=(7,7)):
  survives; independent IM/Im = 21 >= 7/2; same-tree slack = 35/2.

direct post-descent two-point list:
  18 rows / 17 groups; 0 row kills and 0 group kills under all policies.

K=16 entries:
  (64,48;  M=[52,62],   V=(3,3))  survives, slack 6.
  (112,80; M=[100,110], V=(3,3))  survives, slack 12.
  (160,112;M=[148,158], V=(3,3))  survives, slack 18.
```

The `K=16` entries did **not** die; no refutation stop was triggered.

## 6. Xu calibration

The manual split calibrations compute `IM`, `Im`, exact tree `I`, weighted
minor sum, and both slacks.  The Theorem 4.7(i) slack equals `IM-Im` in each
case, as predicted by (*).

| case | `IM` | `Im` | `I` | weighted minor | slack | result |
|---|---:|---:|---:|---:|---:|---|
| `(75,50)` split (i) | 8 | 4 | 72 | 27 | 4 | survives |
| `(75,50)` split (ii) | 4 | 6 | 80 | 29 | -2 | excluded |
| `(84,56; M_2=64,V_2=2)` | 4 | 5 | 84 | 28 | -1 | excluded |
| `(84,56; M_2=72,V_2=5)` | 10 | 4 | 76 | 27 | 6 | survives |

These reproduce Xu's three printed exclusion/non-exclusion computations:
`(75,50)` split (ii), `(84,56;64,2)`, and `(84,56;72,5)`.

## 7. Same-tree policy lemma

**Lemma `XU-SAME-TREE-SCREEN`.**  Fix an operative row `R` satisfying
`C_FULL_TREE_POLYNOMIAL_ODE`.  Let `E(R)` be the finite set of full split
trees generated by the charged embedding enumerator with polynomial
recenter danger and ODE nondegeneracy enabled.  Suppose a Jacobian pair
realizes `R` and satisfies Xu's hypotheses.  Then its actual full split tree
`T*` lies in `E(R)`.  For every `T in E(R)`, the quantities `IM_T`, `Im_T`,
`I_T=I(f_xi,f_y)(T)`, and `W_T` are determined by the root contacts and the
terminal final-root packets of `T`.  Xu's necessary constraints imply

```text
IM_T >= Im_T
deg_y f - 1 + W_T - I_T = IM_T - Im_T >= 0.
```

Therefore if `max_{T in E(R)}(IM_T-Im_T)<0`, no actual Jacobian-pair tree can
realize `R`; killing the row is fail-closed.  If the maximum is nonnegative,
the row only survives this necessary screen.  Survival is not a witness for
attainment or existence.

Proof sketch: membership `T* in E(R)` is exactly the operative full-tree
hypothesis: Def. 5.1 radii on every path, the `b` plus nonzero-orbit split
equation, recursive major children, bottom `(12)/(13)`, Prop. 5.6 danger,
and ODE nondegeneracy.  Lemma 4.1 and the root factorization make
`S_T(alpha)` a tree function; hence major `IM` and final minor orders are
tree functions.  Theorem 3.4 gives exact `I_T`.  Theorem 5.1 and Cor. 5.3
give `IM_T>=Im_T`.  Xu equation (4.3) gives identity (*) above, so Theorem
4.7(i) is necessary but not independent on the same tree.

## 8. Verdict and opens

**PROMOTE (scoped):** replace the open independent-extrema correlation test
by the same-tree scalar `max_T(IM_T-Im_T)` if desired; on this `D <= 200`
census it changes no verdicts.  The sharpened independent policy already
has the same row signs in this range, but the same-tree version is the
properly typed object.

**CLOSE `OPEN[attainment-correlation]` as a kill-strengthening test:** it was
run.  Bounded quantity: `max_T(IM_T-Im_T)` over the operative finite tree set.
Cheapest test was exactly this DP; measured delta is zero row/group kills.
Survival remains non-attainment.

**OPEN[I-skeleton-target]:** bounded quantity is
`I(f_xi,f_y)=deg_x Res_y(f_xi,f_y)`.  Xu pp.4-8 give exact `I_T` from a full
split tree, but no exact target determined from `(n,m,M,V,d)`, and no
genus/Milnor formula usable as a skeleton equality.  Cheapest next test:
prove or source an exact discriminant-degree/genus formula for the generic
fiber in these skeleton variables, then compare that target to `I_T`.

**OPEN[actual-final-minor-refinement]:** bounded quantity is exact `Im` and
exact `I` below terminal minor packets if the campaign later distinguishes
more final splits than the finite operative model records.  Cheapest test:
include the actual final minor packet partition and contacts in the
enumerated tree object; then recompute `S_T`, `Im_T`, `W_T`, and `I_T`
directly.  Do not replace a floor by equality without that final-root data or
the already promoted theorem that supplies it.

FALLACY-v2 status: no representative tree was treated as the actual tree;
no lower bound was promoted to attainment; the Theorem 3.4 formula was used
only as an exact same-tree identity and not as an unproved skeleton equality.

<!-- BODY-END -->
