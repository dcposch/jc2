# Hostile Review: N5-S1 Typed-OPEN Report

## Skeleton

## Hash Verification

## Verdict Summary

## Configuration Extraction

## Per-Component Analysis

## Numeric Bookkeeping

## OPEN Scoping

## Recommendation

## Hash Verification

The four frozen input hashes matched before any filesystem write other than this report skeleton. The verified SHA-256 values were:

```text
42c1e998b1a76f881b88f5146ee7e2d5216a02ab11f2d3de3e688c94c2e40573  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.jEbC8L/inputs/n5-s1-kill-chain-sol56-20260901.md
48d417d6980e52d61550a733f0dcded7d26a0c4e127677ac73bd544a8a00713b  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.jEbC8L/inputs/b0-reducible-n5-opus5-20260831.md
bd6443b34e95213b0b2950e45c896417c492487c38a0a721eae4977d1e73f5d6  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.jEbC8L/inputs/b0-reducible-n5-hostile-review-sol56-20260831.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.jEbC8L/inputs/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
```

Line references below use `S1`, `B0`, `REV`, and `INT` for those files in that order. No CAS or uncertain-duration computation was run. I did not inspect `jc2-lean`, edit a charged file, or edit any canonical ledger. I fetched no new literature; the review below is desk-scale checking against the frozen custody chain.

## Verdict Summary

**Overall verdict: PASS-AS-CORRECTED / promote the S1 OPEN, with two scoping edits.** I find no missed kill of S1 in the frozen promoted machinery. The charged report correctly keeps S1 open: the configuration is the reviewed P1 cage, the aggregate Euler computation cancels to the Orevkov budget, the cusp delta lives in the genus budget rather than the covering Euler budget, and the promoted S4 row/INF machinery does not have S5 singular-branch scope.

| item | verdict | basis |
|---|---|---|
| Hash/source discipline inside the charged report | PASS for its own three-input charge | S1:5-24 verifies and scopes the prior three inputs; this review verified all four current frozen inputs. |
| Configuration extraction | PASS | S1:34-100 matches the reviewed P1 cage at B0:474-486 and REV:82-107, including the corrected S1b `3+2` local orbit split. |
| Component-carrier discipline | PASS | S1:68-72,117-127 keeps `D_B` immersivity and the irreducible Euler identity from being transported to `D_A`. |
| Promoted-gate non-application | PASS | S1:268-313 correctly stops INF-TRIVIAL and the S4 row-kill at their explicit S4/nodal-family scope; INT:32-50 and INT:77-82 do not supply an S5 cusp theorem. |
| Numeric bookkeeping | PASS | S1:129-164 and S1:168-220 correctly separate `chi_c`/branch-count bookkeeping from curve-delta/genus bookkeeping. |
| `OPEN[PI1-S5-CUSP-CORRECTION]` | PASS with label/detail edit | The data are necessary and not analogical, but the S1b `S3 x C2` phrase should be framed as the branch-cluster local image/projection forced after declaring the local branch inertia, not as an independent promoted theorem. |
| `OPEN[N5-S1-INF-WORD]` | PASS, high-leverage subroute | S1:342-350 identifies the first missing datum for the INF-TRIVIAL route and does not claim that solving it alone kills S1. |

Recommended ledger action: promote the S1 status as **OPEN**, not KILLED; route the main residual as `OPEN[PI1-S5-CUSP-CORRECTION]` and the narrower infinity-word subproblem as `OPEN[N5-S1-INF-WORD]`. Do not promote any claim that INF-WORD by itself closes S1, and do not reuse the S4 projective-cover obstruction without a separate S5 cusp-scope theorem.

## Configuration Extraction

**Verdict: PASS.** The charged extraction is the reviewed P1 survivor, not a new or analogical cage. The data

```text
D_A: (mu,corr,s)=(2,1,1), W_A=2, a_A=3
D_B: (mu,corr,s)=(1,0,1), W_B=1, a_B=4
```

agree with B0:474-486 and with the prior review's corrected S1 pinning at REV:82-91. Reducibility and two dicriticals force the owners to be distinct; the cover-floor step forces both `s=1`, so both component normalizations are `A^1` and both `h` maps are isomorphisms, as S1:34-57 states.

The correction is also extracted at the correct carrier. On `D_A`, `K_A=1` and `s=1`, so the unique correction parameter has `e=1`, `k=1`, and `M=3`; the criticality is therefore on `eta_A`, not on a ramified cover `h_A` (S1:59-66). On `D_B`, `mu=1,corr=0,s=1` gives immersivity only for `eta_B` (S1:68-72). The report explicitly refuses the invalid transfer of this smoothness to `D_A`.

The local split is the one demanded by REV:93-97. In S1a, the `D_A` germ at `p_0` is the single singular branch; `D_B` incidence is still allowed, with `a_{p_0}=2-r_{B,p_0}`. In S1b, a second smooth `D_A` branch is present, and LOC forces `D_B` away and `a_{p_0}=0`, with local orbits exactly `3+2`. This fixes the B0 error that allowed an optional five-letter orbit, and S1:74-93 keeps that correction.

The only degree statement is held at the right custody level. S1:95-100 records `d=3+2g_L+Sigma_infinity>=4` only as the reviewed-held Gate TG floor, while retaining the safe unconditional statement that there is no upper bound on `deg D_A` and only `deg D_B>=1` is automatic. This matches REV:105 and REV:154.

## Per-Component Analysis

**Verdict: PASS, with one wording guard on S1b.** The charged report keeps component carriers separated. The false kill `K_A=a_A-1` is rejected at S1:117-127: the irreducible Euler identity is not componentwise in the reducible cage, and the missing unit is exactly `W_B=1`. Likewise, `D_B` immersivity is consumed only to say that `D_B` branches are smooth; it is not used to smooth the correction branch on `D_A` (S1:68-72).

The non-application of N-A/N-A-RES is genuine. B0 states Corollary N-A-RES for an irreducible polynomial curve whose singularities are double points of two smooth branches (B0:430-434), and REV explicitly says S1 remains outside that class because it has a singular branch (REV:91,136,154). S1:310-323 therefore correctly refuses to apply N-A/N-A-RES to S1. This is not a missed kill.

The non-application of the promoted row-kill/INF package is also genuine. INT promotes an S4 theorem for explicit ROW-NF sextics and transported octics, with proof links including an S3 resolvent, INF-TRIVIAL at those strata, and Shirane's projective obstruction (INT:32-50). Its N=5 consequence routes S1 separately as "singular branch; own treatment needed" and applies S5 machinery only to S2/nodal residuals (INT:77-82). S1:268-313 is therefore correct that the promoted theorem does not imply an S5 cusp-scope obstruction.

The local S1a longitude paragraph at S1:240-248 is safe at its stated scope. It is a local peripheral observation after killing any trivial `D_B` meridians, not an assertion about the generic-line infinity loop. The report immediately separates it from `OPEN[N5-S1-INF-WORD]` at S1:342-350, so it does not smuggle local triviality into global INF-TRIVIAL.

The S1b paragraph at S1:249-256 is acceptable as a necessary branch-cluster typing, but it should be worded carefully. REV:97 required the local orbits to be `3+2` and warned that a stronger product assertion needs local inertia. S1 supplies the intended inertia assignment: singular-branch meridians act on the three-letter cluster and the smooth-branch meridian on the disjoint two-letter cluster. With that declaration, the local image is `S3 x C2`. Without that declaration, the promoted fact is only the pair of projections on the two reviewed orbits. The ledger should carry the product as part of the typed OPEN's local data, not as a separately promoted kill theorem.

## Numeric Bookkeeping

**Verdict: PASS.** The aggregate identity is checked in the right quotient of data. For P1,

```text
W_A+W_B+K_tot = 2+1+1 = 4 = N-1.
```

S1:104-127 correctly treats this as the Orevkov budget plus the cover-floor decomposition, not as an extra inequality. The tempting irreducible substitution `K_A=a_A-1` would give a false contradiction; S1 rejects that component split.

The compact-support computation at S1:129-152 is algebraically sound. If `Sigma` contains all singular, component-incidence, and correction points, then each component normalization is `A^1`, so `chi_c(D_i\Sigma)=1-R_i`, where `R_i` is the number of removed normalization preimages. The covering stratification gives

```text
2(1-R_A)+(1-R_B)=4-5 sigma + A_Sigma,
```

while summing LOC over `Sigma` gives

```text
A_Sigma + 2R_A + R_B + 1 = 5 sigma.
```

Substitution makes both sides `3-2R_A-R_B`. Thus the identity is satisfied at S1a points, S1b points, ordinary/tangential `D_A` double points, and `D_A`/`D_B` incidences. There is no leftover Euler charge to spend on a kill.

The cusp delta bookkeeping is also correct. S1:168-184 uses the projective genus formula

```text
delta_infinity + delta_aff = (d-1)(d-2)/2
```

for the rational projective closure of `D_A`. In S1a, the distinguished branch contributes `delta_{p_0}>=1`. In S1b, `delta_{p_0}` must mean the whole two-branch germ, and the reviewed sharper lower bound is `delta(C_cusp)+I(C_cusp,C_smooth)>=1+2=3`, exactly as REV:105 requires. This is separate from the normalization Euler term `r_p-1`; a cusp has `r-1=0` but positive delta. S1:188-197 therefore correctly blocks the N=4 node-style transfer.

The quartic table at S1:199-213 is only an arithmetic control, and it is labeled that way. For `d=4`, the genus budget is three; S1a can allocate `1` to the cusp and `2` elsewhere, while S1b can allocate all `3` at `p_0`. Since there is no promoted upper bound on `d` and Gate TG's lower bound remains custody-conditional, this does not kill S1. The report also keeps curve `delta_infinity` distinct from Gate TG's `Sigma_infinity`, avoiding the denominator/series collision warned against in FALLACY-v2.

## OPEN Scoping

**`OPEN[PI1-S5-CUSP-CORRECTION]`: PASS with a wording edit.** The statement at S1:327-337 is the correct umbrella residual: an irreducible polynomial curve `D_A`, normalization `A^1`, one place at infinity, all meridians mapping to transpositions, transitive image `S5`, exactly one correction/singular branch with `K=1,M=3`, corrected S1a/S1b local typing, disjoint transpositions at other two-smooth-branch singularities, exact delta-genus budget, and the homological sign condition for `gamma_infty`. These are necessary conditions extracted from the reviewed cage; the report explicitly says a YES is not a Keller-map attainment claim.

The wording edit is narrow. In S1b, write "local image with projections `S3` on the three-letter singular-branch orbit and `C2` on the two-letter smooth-branch orbit; equivalently `S3 x C2` once the branch-cluster inertia assignment is declared." This preserves REV:97's warning and prevents the product phrase from being read as a promoted theorem independent of local branch data.

**`OPEN[N5-S1-INF-WORD]`: PASS, but child/subroute rather than replacement.** S1:342-350 asks for an S1-compatible Zariski-van Kampen/peripheral word for the generic-line infinity loop and its image in all representations above. This is exactly the missing datum for importing an INF-TRIVIAL-style descent. S1:268-280 correctly notes that even exponent sum gives only an element of `A5`, not identity; products of transpositions can be nontrivial even permutations. The homological sign pin at S1:282-290 is valid but too weak to kill.

Priority: route `N5-S1-INF-WORD` first if the intended attack is projective descent, because it decides whether that route can even start. Keep `PI1-S5-CUSP-CORRECTION` as the main S1 residual, because INF-WORD alone does not close S1. If INF-WORD forces identity, the next missing theorem is still an S5 cusp-scope projective-cover obstruction; INT's promoted obstruction is S4 explicit-family scoped and uses tools not available for S1 (INT:32-50,77-82). If INF-WORD allows a nontrivial image, it blocks only that promoted route, not the existence of the S1 cage.

No exit-price assertion is made in the charged report or in this review.

## Recommendation

Promote the charged report's central verdict:

```text
S1: OPEN, not KILLED.
```

Promote these supporting items at reviewed scope: the P1 configuration extraction; the corrected S1a/S1b local alternatives; the component-carrier separation; the compact-support cancellation of the aggregate Euler identity; the cusp delta/genus separation; the `S5` transposition quotient as a necessary representation gate; and the non-transfer of N-A/N-A-RES, S4 row-kill, and INF-TRIVIAL to the S1 singular-branch cage.

Do not promote more than this. In particular, do not promote a numerical kill from cusp delta, a degree cap from Gate TG, a global INF-TRIVIAL statement from the S1a local longitude calculation, or an S5 projective-cover obstruction by analogy with the S4 theorem.

Register the residuals as:

```text
OPEN[PI1-S5-CUSP-CORRECTION]
OPEN[N5-S1-INF-WORD]
```

with `N5-S1-INF-WORD` recorded as the high-leverage projective-descent subproblem under the main S1 representation residual. The only requested correction before ledger use is the S1b wording guard above: state the `S3 x C2` local image as branch-cluster typed data, or state only the two projections until the local inertia assignment is included.

<!-- BODY-END -->
