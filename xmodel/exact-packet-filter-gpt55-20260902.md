# CONDITIONAL on EXACT-N -- exact-packet filter, GPT-5.5, 2026-09-02

CONDITIONAL on EXACT-N / D1-SELF-DIFFERENT. This report is only a computation lane under the proposal; it does not re-prove the theorem and does not certify any degree empty. It uses the campaign frontier `N >= 6`, and separately records the restricted window `N in [6,16]`. No canonical ledger was edited and `jc2-lean` was not inspected.

## CONDITIONAL on EXACT-N -- input custody

The frozen input hashes in `/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.I2h68x/inputs` were checked first with `shasum -a 256 -c`; all eight entries returned `OK`:

```text
ideation-20260902T1608Z-sol56.md                         OK
ideation-20260902T1608Z-synthesis.md                     OK
exact-n-rigidity-opus5-20260902.prompt.md                OK
n-on-the-tree-opus5-20260902.md                          OK
n-on-the-tree-review-grok46-20260902.md                  OK
moh_skeleton_N.py                                        OK
uint2.py                                                 OK
uint2.log                                                OK
```

CONDITIONAL on EXACT-N: all computations below import the frozen `moh_skeleton_N.py` copy by absolute path. The per-group sidecar for item (1) is:

```text
xmodel/exact-packet-filter-gpt55-20260902-groups.tsv
bytes=7230279
sha256=e5406d191ce38870ae57626cb98674885d958536ca35c574f8a34d921e913bef
```

Every sidecar row is prefixed `CONDITIONAL on EXACT-N` and contains `D,m,M_tuple,V_s,u,e,branch_type_count,distinct_weight_count,distinct_weights`.

## CONDITIONAL on EXACT-N -- shared and branch-local data

CONDITIONAL on EXACT-N: a packet group is the fixed tuple `(n,m,M_2,...,M_s,V_s)`, where `n=D`, `m=K*d`, `n=K*e`, `K=gcd(n,m)`, the whole divisor chain `d_i`, `s`, `u=V_s*K/d_s`, `v=K-u`, and `V_{s+1}=d_{s+1}` are shared. The top split `V_s` is common to all bottom-major branches because it is the top-form multiplicity split.

CONDITIONAL on EXACT-N: a branch type is one full lower `V` assignment in Moh Def. 5.1(2), i.e. `(V_2,...,V_{s-1})` at the fixed group. The lower `V` entries may vary from branch to branch. Once that full vector is chosen, `delta_1(B)`, root count `r(B)=e*V_2(B)`, and weight

```text
w(B) = e*V_2(B)*d*(1-delta_1(B))/(d+e)
```

are branch-local exact Fractions. The packet constraint is `sum r(B) <= u*e`, equivalently `sum V_2(B) <= u` because `e` is shared inside a group.

## CONDITIONAL on EXACT-N -- item (1), five-degree branch enumeration

CONDITIONAL on EXACT-N: every branch type at the five named degrees was enumerated. The complete per-group weight sets are in the sidecar named above. Aggregate checks:

```text
D    groups  branch_types  distinct_weights  branch_count_range  weight_count_range  u_range
105     264          5037              5037  9..30               9..30               12..30
108     824         85205             85200  8..272              8..272              10..34
112    1163         47655             47655  8..156              8..156              10..26
117      60          1686              1686  18..36              18..36              21..36
120    4104        516309            514956  8..888              8..888              12..38
```

CONDITIONAL on EXACT-N: sample sidecar rows begin as follows; the sidecar is the authoritative full list.

```text
D=105 group (m=42,M=-35,103,V_s=4): 12 branch types, weights start 85/237,740/1027,171/158,3080/2133,2425/1343 and end 19700/5451,11935/3002,360/83.
D=108 group (m=90,M=-84,106,V_s=4): 12 branch types, weights start 174/127,2440/889,4185/1016,30000/5461,7850/1143 and end 190200/13843,3839/254,2160/131.
D=120 group (m=100,M=-96,118,V_s=3): 15 branch types, weights start 42/23,4120/1127,7065/1288,50640/6923,13250/1449 and end 271830/11431,30040/1173,1125/41.
```

## CONDITIONAL on EXACT-N -- packet DP method

CONDITIONAL on EXACT-N: the closing DP for D=105 and D=117 used exact Python `Fraction` totals, root budget in `V_2` units, and unbounded multiset transitions. For feasibility only, if two branch types had the same exact weight, the one with smaller `V_2` dominates the larger-root copy; this cannot create a false hit because the only side constraint is an upper root budget.

CONDITIONAL on EXACT-N: for dense rows I also tested an exact modular representation. For each group I formed a modulus `Q` coprime to every weight denominator and larger than the common-denominator error bound. Therefore a DP residue equal to a target integer is an exact rational equality; completed no-hit closures are exact no-hits. Rows exceeding the stated state cap are reported as OPEN, not killed.

## CONDITIONAL on EXACT-N -- item (2), five named degrees

CONDITIONAL on EXACT-N: D=105 and D=117 closed fully. D=108,112,120 did not close at desk scale because dense groups exceed the exact residue frontier cap; their rows below are lower-bound hits/no-hits plus bounded OPENs.

```text
Variant N integer >= 6
D    groups  exact_hits  exact_no  OPEN_groups  union_N_found                         cap/wall
105     264         125       139           0    6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30    full Fraction, 8.47s
108     824         195       155         474    6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38    cap 100000, 17.76s
112    1163         185       272         706    6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40    cap 100000, 28.94s
117      60          43        17           0    6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38    full Fraction, 14.21s
120    4104         412       433        3259    6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43    cap 20000, 33.40s

Variant N integer in [6,16]
D    groups  exact_hits  exact_no  OPEN_groups  union_N_found                         cap/wall
105     264         105       159           0    6,7,8,9,10,11,12,13,14,15,16         full Fraction, from D=105 run
108     824         402       194         228    6,7,8,9,10,11,12,13,14,15,16         cap 200000, 16.33s
112    1163         157       300         706    6,7,8,9,10,11,12,13,14,15,16         cap 100000, 28.24s
117      60          34        26           0    6,7,8,9,10,11,12,13,14,15,16         full Fraction, 1.74s
120    4104         319       526        3259    6,7,8,9,10,11,12,13,14,15,16         cap 20000, 31.88s
```

CONDITIONAL on EXACT-N: none of the five named degrees is emptied under either variant, because each degree has at least one exact packet hit. For D=108,112,120 this is not a complete survivor count; the OPEN groups may add survivors and may also contain further no-hits.

## CONDITIONAL on EXACT-N -- item (3), extension status

CONDITIONAL on EXACT-N: the requested exact extension to all `D <= 200` did not complete. The obstruction is not enumeration but the packet DP: a single dense D=108 group `(108,72,(54,81,106),8)` reached 41,087,281 exact modular states by root level 6 of 32 before termination in the unrestricted closure. D=120 has 4,104 groups and 516,309 branch types, with groups as large as 888 branch types.

CONDITIONAL on EXACT-N: from the frozen `uint2.log`, there are 59 skeleton-bearing degrees and 120,482 branch-robust groups at `D <= 200`. After the exact full closures at D=105 and D=117, and the bounded exact classifications shown above, the unclassified group count is bounded by

```text
OPEN[EXACT-PACKET-DENSE-DP-GE6]:    0 <= U_200_ge6    <= 118506 groups.
OPEN[EXACT-PACKET-DENSE-DP-6-16]:   0 <= U_200_6_16   <= 118260 groups.
```

CONDITIONAL on EXACT-N: no list of every emptied degree at `D <= 200` or `D <= 400` is promoted from this lane. The five named degrees are not emptied. The D<=400 run was not attempted after the D<=200 exact pass failed to close.

## CONDITIONAL on EXACT-N -- item (4), smallest D=105 surviving packet

CONDITIONAL on EXACT-N: using lexicographic order on `(m,M_tuple,V_s)` among D=105 groups, the smallest group with an exact integer packet `N >= 6` is:

```text
D=105, m=42, K=21, d=2, e=5
M=(-14,103), s=3, V_s=5, u=15, v=6, root budget u*e=75
achievable integer N values: 10
```

CONDITIONAL on EXACT-N: the full witness packet is one branch type with multiplicity 12:

```text
multiplicity 12
full V-vector: V_2=1, V_3=5, V_4=1
branch roots r=e*V_2=5
delta_1=5/12
weight w=5/6
packet root use = 12*5 = 60 <= 75
packet N = 12*(5/6) = 10
```

CONDITIONAL on EXACT-N: this is a packet hit only. It is not a Puiseux-orbit, residue, coefficient, or Keller realization claim.

## CONDITIONAL on EXACT-N -- item (5), Moh six survivor controls

CONDITIONAL on EXACT-N: `(y,x+y^5)`-type automorphism rows have `nu=1` and were not run through Moh's census. Instead, the six Moh survivor rows from `MOH_SURVIVORS` were checked at their shared group `(n,m,M_*,V_s)`, allowing all lower `V` branch types in the group. All six admit an exact packet with integer `N >= 6`; none dies at this packet filter.

```text
Moh row                       group (D,m,M,V_s)              branch_types  U_tower  achievable integer N >= 6
(64,48)                       (64,48,(52,62),3)                        11  9        9
(84,56) M2=64,V2=2            (84,56,(64,82),3)                        20  6        7,15
(84,56) M2=72,V2=5            (84,56,(72,82),3)                        19  21/2     10,14
(75,50) V2=3                  (75,50,(55,73),4)                        19  12       6,7,8,9,15
(75,50) V2=2                  (75,50,(55,73),4)                        19  8        6,7,8,9,15
(99,66)                       (99,66,(77,97),8)                        23  16       8,9,12,16
```

CONDITIONAL on EXACT-N: the two `(75,50)` Moh rows share the same packet group because `V_s=4` is common and the different printed `V_2` values are branch-local row choices.

## CONDITIONAL on EXACT-N -- controls and fallacy audit

CONDITIONAL on EXACT-N: positive controls were the closed D=105 Fraction DP and the Moh six rows. Negative controls are bounded rather than promoted: dense D=108/D=112/D=120 groups exceeded the state cap and are left OPEN. No exit-price assertion is made, so no `charge_basis` line is applicable.

CONDITIONAL on EXACT-N: flag/place/series are not identified. A bottom-major disc is only a packet carrier in this computation; it is not a physical place, dicritical flag, or cover series. `N` is the geometric degree under the proposal; `D` is Moh's `n`. The report uses exact Fractions or exact modular residues with an explicit OPEN on cap overflow. No `sat()`, quotient remainder, derivative-prime, or `M`-descent inference occurs.


## CONDITIONAL on EXACT-N -- dense OPEN appendix

CONDITIONAL on EXACT-N: representative capped groups from the exact-modulus DP are listed here to make the OPEN finite and reproducible. A capped row may already have found one or more exact target residues before overflow; those hits are counted in `exact_hits`, but the group remains OPEN for complete value enumeration and for no-hit classification.

```text
Variant N integer >= 6, cap 100000 unless stated
D=108 OPEN sample: (108,72,(-60,-56,106),3), branch_types=135, kept_weights=135, u=27, maxfloor=21, states=100001, hits_before_cap={}
D=108 OPEN sample: (108,72,(-60,-20,106),3), branch_types=135, kept_weights=135, u=27, maxfloor=21, states=100001, hits_before_cap={12}
D=112 OPEN sample: (112,32,(-24,-20,110),3), branch_types=42, kept_weights=42, u=12, maxfloor=12, states=100001, hits_before_cap={}
D=112 OPEN sample: (112,32,(-24,36,110),3), branch_types=42, kept_weights=42, u=12, maxfloor=12, states=100001, hits_before_cap={6,8}
D=120 OPEN sample, cap 20000: (120,100,(-90,-85,118),3), branch_types=42, kept_weights=42, u=12, maxfloor=10, states=20001, hits_before_cap={}
D=120 OPEN sample, cap 20000: (120,100,(-90,-85,118),4), branch_types=72, kept_weights=72, u=16, maxfloor=32, states=20001, hits_before_cap={}
```

```text
Variant N integer in [6,16]
D=108 OPEN sample, cap 200000: (108,72,(-60,-56,106),3), branch_types=135, kept_weights=120, u=27, maxfloor=21, states=200001, hits_before_cap={}
D=108 OPEN sample, cap 200000: (108,72,(-60,104,106),3), branch_types=117, kept_weights=106, u=27, maxfloor=21, states=200001, hits_before_cap={}
D=112 OPEN sample, cap 100000: (112,32,(-24,-20,110),3), branch_types=42, kept_weights=42, u=12, maxfloor=12, states=100001, hits_before_cap={}
D=117 no OPEN at full Fraction closure.
D=120 OPEN sample, cap 20000: (120,100,(-90,-85,118),3), branch_types=42, kept_weights=42, u=12, maxfloor=10, states=20001, hits_before_cap={}
D=120 OPEN sample, cap 20000: (120,100,(-90,-85,118),4), branch_types=72, kept_weights=47, u=16, maxfloor=32, states=20001, hits_before_cap={}
```

CONDITIONAL on EXACT-N: the `kept_weights` number is after the only dominance pruning used for feasibility: identical exact weights are represented by their minimum `V_2` root cost. The sidecar still records the unpruned branch-type count and all distinct weights for item (1).

## CONDITIONAL on EXACT-N -- D<=200 bounded universe

CONDITIONAL on EXACT-N: the frozen `uint2.log` gives the following skeleton-bearing degrees up to 200. These are proxy census rows, not exact-packet conclusions, but the group counts bound the remaining packet workload.

```text
D<=200 skeleton-bearing degrees:
48,54,60,63,66,72,75,80,81,84,88,90,96,99,100,102,104,105,108,110,112,117,120,125,126,128,130,132,135,136,138,140,144,147,150,152,153,154,156,160,162,165,168,170,171,174,175,176,180,182,184,186,189,190,192,195,196,198,200
branch-robust group count at D<=200: 120482
frozen proxy V1>=6 groups at D<=200: 30
frozen proxy V1[6,16] groups at D<=200: 0
frozen proxy V2>=6 groups at D<=200: 21545
frozen proxy V2[6,16] groups at D<=200: 13429
```

CONDITIONAL on EXACT-N: those proxy counts are not used to declare exact packet emptiness. They are included only to show that the packet computation failed at the exact mixed-branch stage, not at the Moh group enumeration stage.

CONDITIONAL on EXACT-N: all OPEN counts are group counts, not degree counts; an OPEN group is bounded by the displayed state cap and remains unclassified.

## CONDITIONAL on EXACT-N -- typed verdict

CONDITIONAL on EXACT-N: the five-degree branch enumeration is complete and sealed in the sidecar. The exact packet filter is fully closed for D=105 and D=117 and for the six Moh controls. D=108, D=112, and D=120 are not emptied and are not fully counted: they contain exact hits, exact no-hits, and bounded OPEN dense groups. The all-`D<=200` and all-`D<=400` exact-packet extensions remain OPEN in this lane.

CONDITIONAL on EXACT-N: no theorem-level emptiness statement is promoted. The actionable realization target from the requested D=105 search is the lexicographically smallest packet `(D,m,M,V_s)=(105,42,(-14,103),5)` with 12 copies of `(V_2,V_3,V_4)=(1,5,1)` and `N=10`.

<!-- CONDITIONAL on EXACT-N SEALED body_sha256=02416c9ac8d2ebfeacb38a785eee3876a2816db6215dad778e08be715d5803b7 -->
