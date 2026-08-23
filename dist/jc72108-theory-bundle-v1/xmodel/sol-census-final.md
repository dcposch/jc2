VERDICT: EARNED — conditional emptiness over the 411-row quotient, conditional on FC1–FC7, survives the closing pass; the advertised per-row `subadd_authority` provenance and “159 authority + 252 cell-derived” wording are BROKEN but are not load-bearing for any death stamp.

# Findings, ranked

## 1. HIGH ERRATUM — filtering is coverage-effective, but the emitted authority bit is not an authority bit

The deletions that can affect the repaired BB/root menus are correctly scoped: `menu_BB()` applies `M_G | sum(mu_e)` only when `auth = (eps == 0 and k == 0)` (`cases/td11_census.py:254-256`), and `root_menuM()` uses the same antecedent (`:435-437`). The zero-slot outer menus do not apply MP6. This is why the target `M=5` cell now survives enumeration.

The record bookkeeping does **not** implement the stronger claim in the banner. At `:548` and `:552`, `authM/authR` are reconstructed from the numerical fact that `M` divides the relevant sum. That conclusion does not imply `epsilon=0=k`. Consequently `r[7]` is a legacy-divisor-axis marker, not the exact-cell `subadd_authority` bit required by `xmodel/sol-normalform.md:118-120`.

Five spots on each advertised side reproduce: rows 280–282 and 287–288 are flagged `auth` at inner `M=4` and do have the authoritative `(20,16), (eps,k,nu)=(0,0,5)` witness; rows 305–309 are flagged `cell-derived` at inner `M=5`. But the negative control fails: rows 266–268 and 273–274 are flagged `auth` at `M=2`, although their only cells are `(26,16), (eps,k)=(1,1)` and `(14,10), (2,2)`, both non-authoritative. In all, 21 realized nested rows have `r[7]=True` with no authoritative realizing inner cell (12 AB, three BB2-`M=1`, six BB2-`M=2`). Deduplication at `:260-265` also forgets exact provenance: raw `(20,16)` has both authoritative and non-authoritative schemas, and `(11,7)` has two distinct non-authoritative schemas.

There is one residual literal scope violation: `menu_AB()` still tests `3 % M_G == 0` unconditionally at `:209` although its fixed `eps=2` has no R2.2(D) authority. Removing that conjunct independently leaves exactly the same sole pinned candidate `(d_p,d_q,M)=(5,7,1)`, so it is vacuous in this census and omits no row. `cases/nfm_check.py` likewise retains the old blanket filters; it is not evidence for this repair. The standalone v2 census re-enumeration is.

Therefore C1's **count** is right, but its terminology is not: 159 is the old divisor-skeleton slice and 252 is its complement. This provenance defect should be corrected before calling the output a fat normal-form certificate, but it neither deletes a current candidate nor changes a terminal instrument, so it does not create FC8 or break conditional emptiness.

## 2. CLEAR — Sol's chart enters, and the outer replay kills it and its five pure-OUTER siblings

`BB2_MENU` now contains

```text
(kbar,dp,dq,M,eps,k,nu,auth) = (8,65,40,5,0,1,13,False).
```

The local equalities and guards replay exactly:

```text
8*65/40 = 13;  2*40 > 65;  40 < 65;
65 != 40,80;  gcd(5,13)=1;  gap = 8/(2*65)=4/65.
```

Since `auth=False`, `5 | 4` is not demanded. The outgoing choices are `mu_in in divs(5)={1,5}`. At the deduplicated BB2 geometric-cell tier the five other non-authoritative, non-cylinder cells whose rows are purely OUTER-DEAD are `(15,10)M5`, `(45,36)M9`, `(26,16)M2`, `(8,16)M8`, and `(14,10)M2`; their gaps are respectively `1/5, 2/45, 2/13, 1/8, 5/28`, all below `1/2`. The remaining non-authoritative `(11,7)M1` shares its axis with the in-window cylinder and is correctly stamped `SPLIT`, not pure OUTER-DEAD.

Independent outer replay:

| `mu_in` | schemas | at/below `1/2` | in `(1/2,5/2)` and refused | unrefused or `>=5/2` |
|---:|---:|---:|---:|---:|
| 1 | 288 | 7 | 281 | 0 |
| 5 | 100 | 14 | 86 | 0 |

The corresponding root-M menus have 7 and 19 decorated rows, so inner `M=5` contributes 26 rows (`cases/td11_census.py` rows 305–330), all `OUTER-DEAD`. This replay is stronger than gate C1b, whose boolean checks only the projected `M=5` rows rather than the exact `(65,40)` member.

## 3. CLEAR — the R1.0 root-multiplicity guard is legitimate and exact

R1.0 says `d_p != m*d_q` for every multiplicity `m` of a root of `p`; `menu_BB()` checks arrivals, NE roots, and the zero root at `:246-250`. This is the order-`m` consequence of Prop. 8.1(iv), independently re-derived in `BOOK-OFFAXIS-REVIEW.md:69-83` and recorded as R2.2(R) in `BOOK-OFFAXIS.md:317-331`.

Without the guard, `menu_BB(2)` has 129 raw / 127 deduplicated candidates. It removes exactly the 119-member coded truncation of the spurious family

```text
eps=1, k=0, x=2, A=Q=4, nu=2..120,
kbar=3, dp=dq=M=4*nu+1.
```

At the zero root `m=1`, R1.0 forbids `dp=dq`; equivalently the reduced ODE forces `C_ODE=0`, contrary to its required nonzero value. Ten raw / eight deduplicated legitimate BB2 records remain, including `(65,40)` and the genuine cylinder. No collateral deletion was found.

## 4. CLEAR — the 252 added rows retain sound extension-class covering

The run reproduces 411 rows and all 8/8 gates. The 252 additions split as follows:

| source | rows | stamps |
|---|---:|---|
| new inner `M`: BB1 `M=4`; BB2 `M=5,8,9` | 132 | 132 OUTER-DEAD |
| cell-derived outer `M` on old inner decorations | 120 | 52 SPINE, 32 UNREALIZABLE, 4 SPLIT, 32 OUTER-DEAD |

The 132 substantive additions are exactly `25+26+42+39`; their new inner gaps are `1/4, 1/5, 4/65, 2/45, 1/8`, all below-window. The outer analysis is parametric in the unknown inner transport weight, so it covers the exact `epsilon/k/nu` records lost by degree-key deduplication. The other 120 either die before the root decoration matters or use the same all-completions outer/SPLIT argument. A widened hostile scan (`x<=64`, `nu<=500`, `kbar<=200`, enlarged zero-orientation ranges) found no outer escape for outgoing `mu_in in {1,2,3,4,5,8,9}`.

Thus the quotient is sound as an **instrument-uniform death quotient**, not as literal enumeration of every extension record. FC1–FC6 continue to own the named chain/current-arrival/post-merge/`nu=1` perimeter, and FC7 remains load-bearing for finite schema bounds and handshake-form completeness. No eighth subadditivity class is needed: the non-authoritative cells are present and dead.

Final accounting: 411 rows; stamp multiset `185 OUTER / 133 SPINE / 63 UNREAL / 12 SELF / 11 CLASH / 7 SPLIT`; zero live and zero deferred. Conditional on the seven printed KEEP-AS-POSSIBLY-LIVE classes, **CONDITIONAL EMPTINESS IS EARNED**.
