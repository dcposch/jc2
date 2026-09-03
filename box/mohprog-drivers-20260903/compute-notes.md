# Moh-program computational reproduction notes

Date: 2026-09-03 UTC.  Scope: frozen-input computational lane only.  I did not inspect `jc2-lean`, any `ideation-20260903T*` file, or another lane's in-progress report, and I did not edit a canonical ledger or the main report.

## Bottom line

- The frozen `(1)--(13)` code reproduces **1,692 V-assignments / 1,189 groups** for `48 <= D <= 120` and **658 rows / 63 (n,m) classes** for `n <= 100`.  The latter has 652 rows beyond Moh's six printed rows.
- A separately written enumerator agrees on the complete 658-row set, not merely its cardinality.
- Independent enumeration at `(75,50)` gives 682 `(1)--(7)` assignments and no occurrence of `delta_1=1/3`.  The printed row with `M_2=55,V_2=2,V_3=4` has `delta_1=2/3`.
- All ten deterministic worksheet rows pass every tuple-arithmetic part of `(1)--(13)`.  Conditions (3) and the actual-realizability content of (4) are deliberately marked unverified because an integer tuple cannot certify them.
- The exact Prop. 3.1 bounded-digit semigroup predicate is automatic on all 658 rows and all 23,720 rows at `48 <= D <= 200`; it eliminates nothing.
- The universal zero-path model of Prop. 5.6 leaves 153 rows / 100 groups / 15 classes and exactly performs the requested `(75,50)` cut.
- The complete orbit-factor-tree model leaves 60 rows / 40 groups / 12 classes.  Adding the source-valid local ODE condition `P-Q u != 0` at every root leaves 58 / 38 / 12.  Adding the rigorous but not Moh-stated cyclic-quotient passport bound leaves 55 / 37 / 11.  All keep the six printed rows and exactly the two requested `(75,50)` rows.
- Thus the strongest no-recentering, source-safe finite model still has a precisely bounded residual of **49 excess rows** at `n <= 100`.  It is not the missing 652-row elimination.
- An iterative polynomial-recentering danger model cuts further to 23 rows, or 20 with ODE/passport constraints, but that recursion is **INFERRED/OPEN**, not an exact consequence proved by Moh's Prop. 5.4.  It must not be promoted as Moh's program.

## Frozen input verification

Command: `sha256sum /tmp/jc2-lane.YI70hY/inputs/*`.

All nine values matched the charge before computation:

| frozen input | SHA-256 |
|---|---|
| `census-rebase-opus5-20260902.md` | `fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948` |
| `tf-calibration-review-gpt55-20260902.md` | `5f56d980ed8deea3a7996dd8954d3a9ff4fdd7b2c75802ddb93e51a0afb02ded` |
| `time-function-calibration-d48-opus5-20260902.md` | `db8a10c986a8a8a7b83c285585e299d887c72e52417b76ea7fca8c4fd0dbff2a` |
| `delta-denom-gpt55-20260902.md` | `7355259f17d13edd8e309231b8573ed4c1429093b84a72628c33730827fe59ea` |
| `integration17-coordinator-fable51-20260902.md` | `126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5` |
| `moh_skeleton_full.py` | `d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2` |
| `run_all.py` | `792eb15e74932a084f3d3ecac6ea914d3cff965634b2c19b02e6264c0947e3c7` |
| `survivors-D48-120.txt` | `47f59906927ff9d2b38b25b11c2e46cef3c472b3d8db300f12c12f22906848e1` |
| `moh1983_jram340_configurations_of_roots.pdf` | `6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51` |

The exact script copies `moh_skeleton_full_frozen.py` and `run_all_frozen.py` retain hashes `d20bf...` and `792eb...`.  The isolated copies under `repro/` do too.

## Frozen-driver rerun

Isolated layout:

- `repro/moh_skeleton_full.py`: byte-identical frozen module.
- `repro/censusrebase-drivers-20260902/run_all.py`: byte-identical frozen driver.
- `repro/moh_skeleton_N.py`: compatibility shim re-exporting the frozen full module.  The frozen set did not contain the legacy module used only by control 0.  Consequently control 0 in this isolated run is tautological; the independent enumerator below supplies the substantive second implementation.

Command shape:

```text
cd box/mohprog-drivers-20260903/repro/censusrebase-drivers-20260902
/usr/bin/time -v python3 run_all.py
```

The full logged rerun took 328.1 seconds and all driver assertions passed.  Principal measurements:

| scope / stage | V-assignments | groups | UNI integer N>=6 |
|---|---:|---:|---:|
| `(1)--(7)`, `48<=D<=120` | 902,893 | 10,637 | -- |
| reconstructed `(10)` only | 3,760 | 1,012 | -- |
| `(10)+(12)/(13)` calibration | 329 | 287 | -- |
| full `(1)--(13)`, `48<=D<=120` | **1,692** | **1,189** | **670** |
| full `(1)--(13)`, `121<=D<=200` | 22,028 | 12,827 | 8,161 |
| full `(1)--(13)`, `48<=D<=200` | **23,720** | **14,016** | **8,831** |

The group ratio `1189/287 = 4.143...` is the reported 4.1x correction.  Assignment counts have the larger ratio `1692/329 = 5.143...`; the 4.1x statement is therefore specifically a group-count statement.

At `n<=100,Kmin=2`, the driver reports 658 rows in 63 `(n,m)` classes; Moh prints six rows in four classes.  The exact excess is 652.

The generated survivor file has SHA-256 `22c80f9893966cb1ae17322dfd8f6ac806e74c907ce61724dfcac236bfa14124`.  It differs from the frozen survivor artifact only in the first three header lines (`V_2` and line wrapping); `tail -n +4` is byte-identical.

Baseline requested degree checks, shown as `V/groups/UNI(N>=6)`, are:

| D | baseline count |
|---:|---:|
| 105 | 15 / 14 / 7 |
| 108 | 206 / 125 / 87 |
| 112 | 76 / 71 / 33 |
| 117 | 7 / 7 / 4 |
| 120 | 782 / 515 / 271 |

The separate value “D=105 -> 3 groups” is the narrower mixed/UNI `[6,16]` stage printed by the charged driver, not the unbounded `N>=6` count above.

## Independent enumeration and the `(75,50)` erratum

`independent_enumerator.py` reimplements the gcd chain, all integer windows, Def. 5.1(3) radii, denominator increments, `(9)--(11)`, and `(12)/(13)` without importing the frozen module.  Command: `/usr/bin/time -v python3 independent_enumerator.py` (9.03 seconds in the recorded run).

At `4<=n<=100,Kmin=2` it finds:

- 258,319 arithmetic `(1)--(7)` assignments;
- 658 `(1)--(13)` rows;
- 63 `(n,m)` classes;
- zero set differences against the frozen 658-row result.

At `(n,m)=(75,50)` it finds 682 `(1)--(7)` assignments.  The exact `M_2` support is

```text
-45,-40,-35,-30,-20,-15,-10,-5,5,10,15,20,30,35,40,45,55,60,65,70
```

with `V_2=1,...,20` and `V_3 in {3,4}`.  None has `delta_1=1/3`.

After `(8)--(13)`, exactly nine rows remain, all with `M_3=73,V_3=4`:

| M2 | V2 | delta1 |
|---:|---:|---:|
| 5 | 20 | 8/33 |
| 10 | 1 | 7/17 |
| 40 | 1 | 13/18 |
| 40 | 2 | 4/9 |
| 40 | 11 | 7/27 |
| **55** | **2** | **2/3** |
| **55** | **3** | **1/2** |
| 60 | 9 | 7/22 |
| 60 | 20 | 8/33 |

This independently confirms that the p.202 bracketed `1/3` is unattained and that Def. 5.1(3)'s `2/3` is correct.

## Deterministic ten-row worksheet

`make_ten_row_worksheet.py` chooses the six printed rows, the lexicographically first excess row at each observed `s=3,4,5`, and the lexicographically last excess row.  The ten are:

1. printed `(64,48; M2=52; V2=3,V3=3)`;
2. printed `(84,56; M2=64; V2=2,V3=3)`;
3. printed `(84,56; M2=72; V2=5,V3=3)`;
4. printed `(75,50; M2=55; V2=3,V3=4)`;
5. printed `(75,50; M2=55; V2=2,V3=4)`;
6. printed `(99,66; M2=77; V2=8,V3=8)`;
7. first `s=3` excess `(36,24; M2=16; V2=1,V3=3)`;
8. first `s=4` excess `(48,32; M2=-8,M3=36; V2=2,V3=1,V4=3)`;
9. first `s=5` excess `(96,64; M2=-48,M3=-8,M4=4; V2=24,V3=12,V4=6,V5=3)`;
10. last excess `(100,80; M2=85; V2=5,V3=4)`.

The worksheet records every gcd, window endpoint, raw numerator/denominator product in each radius, `L_j`, `A_j`, the quotient/remainder in (9), branch truth values for (10)/(11), both bottom alternatives, and the p.188 divisibility check.  All ten arithmetic verdicts are PASS.  For every row it separately says that conditions (3) and actual characteristic-data realization in (4) are not tuple-arithmetic claims.

Artifacts:

- `ten-row-worksheet.md`, SHA-256 `c1468d9766704a0a8ca3aefa41e34ade1a5c7eee9c475a59be39735b847e7a04`;
- `ten-row-worksheet.json`, SHA-256 `8ec633ffa30b1099efa28beff6edf4cc531d454416a383c52ea80ab35e42ca67`.

## Candidate definitions

Every candidate is applied only after the frozen `(1)--(13)` filter.  “Fail-closed” means that all six printed rows survive.  It does not establish that a predicate is Moh's omitted program condition.

### Source scalars and semigroup

- **TOP-SPLIT:** `V_s<d_s`.  It is already automatic in the frozen enumeration: 658 -> 658.
- **TOP-RADIUS:** `(d_s-V_s)(n-M_{s-1})>=d_s`.  Also automatic: 658 -> 658.
- The q-degree residues `Q_j mod A_j in {0,1}` and the stronger `A_j | Q_j-1` are automatic on all 658 and all 23,720 rows.
- The exact bounded-digit Prop. 3.1 equation is checked at every effective level: for `R_i=-mu_i`, `n_i=d_i/d_{i+1}`, find `j>=0` and `0<=alpha_i<n_i` with `j*n + sum_{i<r} R_i alpha_i = n_r R_r`.  It is automatic on the full two census scopes.  Hence it also preserves every residual of every stronger tree filter.
- Alternative semigroup indexing is refuted fail-closed: shifted multiplier through the terminal level leaves 19 rows but kills five printed rows; the preterminal version leaves 111 and kills four.  Reversing the approximate-root inequality kills all six.

### ZERO-PATH

Starting with the top `V_s`, at each `j=s-1,...,2` recompute the radius and `A_j` on the synthetic zero path, let `P=V_{j+1}d_j/d_{j+1}`, and let `b=P mod A_j` be the canonical nonnegative zero multiplicity.  If `b=0` or `b<=d_j/(n-M_j)`, the forced all-zero major path stops.  Otherwise set `V_j=b` and continue; reject if it remains major to the bottom.

This leaves 153 V-rows / 100 groups / 15 classes at `n<=100`, keeps all six, and at `(75,50)` leaves exactly `(M2,V2)=(55,2),(55,3)`.  The forced canonical `b` values for `M2={5,10,40,55,60}` are respectively `{20,3,2,0,9}`.

### Complete orbit-factor tree

At level `j`, set

```text
P = V_{j+1} d_j / d_{j+1},
Q = V_{j+1} (n-M_j) / d_{j+1},
h = d_j/(n-M_j).
```

For orbit size `A_j`, enumerate every partition

```text
P = b + A_j * sum(v_l),   b == P (mod A_j),
```

where `b` is the fixed-zero multiplicity and the `v_l` are per-root multiplicities of nonzero `A_j`-orbits.  The number of distinct nonzero orbits is bounded by `floor(Q/A_j)`, since q is squarefree and contains every p-root.  Every factor with multiplicity `>h` is major and must recursively admit the lower characteristic tower; minor factors stop.  At least one factor is major.  At `j=2`, every major child must pass `(12)/(13)`.  A typed all-zero major chain is rejected by Prop. 5.6.  Finally, the V-path of the census row itself must embed in one global partition.

This is an exact finite dynamic program over bounded integer partitions.  It is a source-motivated model of the simultaneous multiplicity structure; the counts do not by themselves prove it is extensionally identical to Moh's unpublished code.

The bare model leaves 60 rows / 40 groups / 12 classes, including exactly the six printed rows at `s=3`; all 54 excess rows have `s>=4`.  Every accepted row has a complete witness, and every rejected row has a no-partition certificate.

### ODE nondegeneracy and passport

At a q-root carrying p-multiplicity `u`, Moh's A.3 differential equation gives a nonzero denominator `P-Q u`; requiring `P-Q u != 0` for every root in every partition is source-valid.  On the one selected printed path alone it is automatic on all 658 rows.  Inside the complete factor tree it changes 60 -> 58 rows.

The stronger cyclic-quotient passport candidate uses `S=(Q-1)/A`, pads the nonzero p-orbit multiplicities with `u_l=0` to exactly S q-orbit slots, and forms

```text
W_0 = (P-Qb)/A,       W_l = P-Q u_l  (1<=l<=S).
```

All weights must be nonzero.  With `g=gcd(|W_0|,...,|W_S|)` and `dplus=sum max(W_i,0)`, require `dplus/g >= S`.  This is a rigorous necessary consequence of the A.3 ODE plus the elementary degree bound for the quotient rational map, but it is not a condition Moh states.  Therefore it is typed **SOURCE-DERIVED, NOT PROVED-IN-SOURCE**, and not identified with Moh's program.  It changes 58 -> 55 rows.

The exact moment/distinct-root realization equations remain stronger and are not solved by this integer passport test.

### Polynomial-recentering danger (OPEN)

The exploratory propagation starts “dangerous” at the top, preserves danger on a zero edge, and treats a nonzero edge as still removable only when its radius is integral (in this search range, radius zero).  Reaching the bottom dangerous is rejected.  This is motivated by polynomial absorption in Prop. 5.4, but Prop. 5.4 assumes a specially chosen smallest disc containing all roots of `g*T_1`.  The source does not prove that a generic recursive child retains that hypothesis.  Accordingly these counts are useful experiments only:

- factor tree + recenter: 23 rows / 15 groups / 7 classes;
- plus ODE nondegeneracy: 20 / 12 / 7;
- plus passport: 20 / 12 / 7.

The last two contain 14 excess rows, all at `s>=4`.  This 14-row residual must not replace the source-safe 49-row residual.

## Fail-closed candidate summary

| candidate | `n<=100` V/groups/classes | printed killed | `D48..200` V/groups/UNI |
|---|---:|---:|---:|
| baseline `(1)--(13)` | 658 / 508 / 63 | 0 | 23,720 / 14,016 / 8,831 |
| TOP-SPLIT | 658 / 508 / 63 | 0 | 23,720 / 14,016 / 8,831 |
| TOP-RADIUS | 658 / 508 / 63 | 0 | 23,720 / 14,016 / 8,831 |
| Prop. 3.1 bounded semigroup | 658 / 508 / 63 | 0 | 23,720 / 14,016 / 8,831 |
| NOT-ALL-(11) numerical shadow | 469 / 387 / 43 | 0 | 18,971 / 12,384 / 7,843 |
| ZERO-PATH | 153 / 100 / 15 | 0 | 7,431 / 3,212 / 2,221 |
| FULL-TREE | 60 / 40 / 12 | 0 | 3,090 / 1,516 / 978 |
| FULL-TREE + ODE nonzero | 58 / 38 / 12 | 0 | 2,824 / 1,384 / 865 |
| FULL-TREE + PASSPORT | **55 / 37 / 11** | **0** | **2,581 / 1,261 / 803** |
| FULL-TREE + RECENTER (OPEN) | 23 / 15 / 7 | 0 | 1,691 / 848 / 590 |
| RECENTER + ODE (OPEN) | 20 / 12 / 7 | 0 | 1,420 / 686 / 459 |
| RECENTER + PASSPORT (OPEN) | 20 / 12 / 7 | 0 | 1,315 / 631 / 429 |
| force positive p-complement | 231 / 201 / 46 | **2** | 4,294 / 3,006 / 2,510 |
| canonical p/q zero coprime | 5 / 4 / 4 | **1** | 71 / 67 / 66 |

The last two candidates are WRONG as general restrictions because they kill printed rows.

## Requested downstream metrics

Counts are `V-assignments / groups / groups alive for an integer UNI N>=6`.

| candidate | 48..120 | 121..200 | 48..200 |
|---|---:|---:|---:|
| ZERO-PATH | 497 / 279 / 174 | 6,934 / 2,933 / 2,047 | 7,431 / 3,212 / 2,221 |
| FULL-TREE | 183 / 113 / 57 | 2,907 / 1,403 / 921 | 3,090 / 1,516 / 978 |
| FULL-TREE + ODE | 168 / 103 / 50 | 2,656 / 1,281 / 815 | 2,824 / 1,384 / 865 |
| FULL-TREE + PASSPORT | **152 / 96 / 45** | **2,429 / 1,165 / 758** | **2,581 / 1,261 / 803** |
| RECENTER (OPEN) | 91 / 54 / 39 | 1,600 / 794 / 551 | 1,691 / 848 / 590 |
| RECENTER + ODE (OPEN) | 74 / 42 / 30 | 1,346 / 644 / 429 | 1,420 / 686 / 459 |
| RECENTER + PASSPORT (OPEN) | 68 / 38 / 27 | 1,247 / 593 / 402 | 1,315 / 631 / 429 |

Requested degrees for the strongest no-recenter source-safe candidate FULL-TREE+PASSPORT:

| D | V | groups | UNI N>=6 |
|---:|---:|---:|---:|
| 105 | 0 | 0 | 0 |
| 108 | 18 | 11 | 8 |
| 112 | 8 | 7 | 2 |
| 117 | 0 | 0 | 0 |
| 120 | 71 | 41 | 17 |

It has no `(1)--(13)` group at degrees

```text
48,54,60,63,81,88,102,104,105,110,114,117,
130,152,153,154,170,174,182,184,186,190,195.
```

The pinned-N test additionally empties candidate-active degrees `72,80`.  Thus the complete all-empty list is the preceding list plus `72,80`.

For comparison, FULL-TREE+ODE has `D105=0`, `D108=20/12/8`, `D112=8/7/2`, `D117=0`, and `D120=82/46/22`; it has the same degree-empty lists.

## Artifacts and final hashes

Core code/results:

| artifact | SHA-256 |
|---|---|
| `independent_enumerator.py` | `5c4df6f7888a9f5c9fc2ec2f0e7339315bfca4df2309ed26f38474a50f432fb8` |
| `make_ten_row_worksheet.py` | `9b4cbbe78093c58a80b0ac0e3d05f176c1c5cb1e4dba8ebf50c5bd57e66afd73` |
| `candidate_eval.py` | `5d1b21222eecc448975c83d3628c22ada5cd26737155ecf2a7a27304ec40e553` |
| `full_tree_partition.py` | `875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8` |
| `candidate-results.json` | `01a5341fec7e5f26a31671c5227b3851bf6635f6ef0f3f1f9f00d0172431ffd2` |
| `independent-n100-summary.json` | `8d8c794951bec7c5e2efe04e5c89790b1d98c01bcbaf46e3345e1aeaaa105ac6` |
| `independent-n100-rows.json` | `724d121b84acdf8c48dba869bf523bad5ccecd4a8b4f9d1836e1517b810d974e` |
| `independent-75-50.json` | `1148a52f66a91f4bb744c1bde6a1802e93b346be6a1fa9c1860c26cb71c55e5f` |

Exact n<=100 audit/witness files:

| filter artifact | SHA-256 |
|---|---|
| `full-tree-n100-audit.json` | `ca82a1281a293afa3d31a15b19865309b2e833359b5dd57e97e3ec8da7f1a589` |
| `full-tree-excess-witnesses.json` | `9058d07d5d8b8e4caa55ef15001f42bee68173d9bf2822a46dcce3786b1cbda6` |
| `full-tree-ode-n100-audit.json` | `26bceb75f4a5d526f75e03461b2c8607fa895b40d9709dc8e61a513d43aa402c` |
| `full-tree-ode-excess-witnesses.json` | `334e6fd87521741d2c7c35e647fad28a8d9cd245c0daf33b9f6151ef85b154d5` |
| `full-tree-passport-n100-audit.json` | `e7727a6d235b1e1d5d0251fcdfb7410b659d5147cad5e6e73265f488057940cc` |
| `full-tree-passport-excess-witnesses.json` | `ca9712814b62810e50075f0c105e439eadaa25f7d8d27ff320cefc84b7f828da` |
| `full-tree-passport-printed-witnesses.json` | `04c7114ca9edaad14fa35527bfd57bfd99816767301d5db2bb376499029f44d3` |
| `full-tree-polynomial-passport-n100-audit.json` | `41845441e89007fd4943ad9acfcd6723397bea2a2bdf083307973b1781d6c234` |

The JSON audits carry one record per input row, an exact selected-path embedding flag, a witness for acceptance, and a bounded failure certificate for rejection.  In particular, `full-tree-passport-excess-witnesses.json` is the exact 49-row source-safe residual; `full-tree-polynomial-passport-excess-witnesses.json` is the 14-row exploratory residual.

Final candidate run: 80.70 seconds wall, maximum RSS 672,620 KiB, one core.  Six-variant n<=100 audit run: 4.3 seconds.  Both remain well below the desk-scale limits.

## Reproduction commands

```text
python3 independent_enumerator.py
python3 make_ten_row_worksheet.py
python3 full_tree_partition.py
/usr/bin/time -v python3 candidate_eval.py
sha256sum candidate-results.json ten-row-worksheet.* independent-*.json full-tree*-audit.json full-tree*-witnesses.json
```

No numerical candidate found in this lane both reduces the 658 rows to exactly Moh's six and has a proved source equivalence.  The bounded computational residual is 49 excess rows under the strongest no-recentering factor-tree/passport model; the unresolved content is full distinct-root ODE realization and/or a non-numerical or case-by-case program step.
