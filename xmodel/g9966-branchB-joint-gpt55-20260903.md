# (99,66) branch-B high-z joint computation

## Verdict

`COUNTING-BOUND[BRANCH-B-HIGH-Z-DEPTH6-NONUNIT]`.

The rigid branch-B Prop. 6.2 high-z joint systems were completed through depth 6 over `GF(32003)`, `GF(32009)`, `GF(32027)`, and `Q`. They are nonunit; no `[1]` certificate was produced.  Depth 7 is the next nonlinear system and was not solved in this bounded run.

The charged `delta=5/2` system was replayed through depth 6 for custody against the frozen input.  The exact charged depth-7/8 build did not finish inside the bounded window, so those bands are recorded as next systems rather than promoted to solved verdicts.

Artifacts are under `box/g9966B-20260903/`; the report is sealed below.

## Custody

The lane receipt `xmodel/g9966-branchB-joint-gpt55-20260903.run.v2` was parsed mechanically.  The initial manifest was generated from the receipt's indexed basename/SHA-256 fields with `awk` and checked by `sha256sum -c`; all nine frozen inputs returned `OK`.  The driver also wrote `box/g9966B-20260903/charged-inputs.sha256` and recomputed the same digests.

## System Boundary

For branch B the gauge is fixed at `a=1`, so `H=pi^2(pi+3)` and `R=pi^25(pi+3)^14(pi-2)`.  Direct differentiation gives `2 H R_z - 25 H_z R = 5 H^14`, with multiplicity vector `(25,14)`.  No branch-face parameter is present in the branch-B Singular rings.

For `delta=5/2`, the replay uses the charged face `H=pi(pi^2-1)` with the existing `mu2` parity rule and the charged `split_c-1`, `T*gamma*split_c-1` wrapper convention.  As in the charged input, the `e0` parameter in Xu's reduced `q1` is not part of this Prop. 6.2 high-z Fbar/Gbar system.

At depth `d`, the driver uses `Gbar` bands `z^27,...,z^(28-d)` and induced `Fbar` bands `z^18,...,z^(19-d)`.  It keeps only coefficients visible through local order `d`; it then imposes approximate-root divisibility for `Gbar^2-Fbar^3` and the positive z-bands of `J_yz(Fbar,Gbar)=constant`.

Branch B uses an explicit point-set pruning step to keep the nonradical high-z ideal computable: only rows of the form `c*x^k` with `c` a unit over `Q` and all three selected primes are replaced by `x=0`.  Product rows such as `x*y=0` are not collapsed.  The `delta=5/2` replay uses the charged sparse replay builder without this pruning.

## Branch B Results

Depth 4:

| field | equations | Gbar unknowns | basis | verdict | dim | time |
|---|---:|---:|---:|---|---:|---:|
| `GF(32003)` | 8 | 16 | 11 | `NONUNIT` | 9 | 0.021s |
| `GF(32009)` | 8 | 16 | 11 | `NONUNIT` | 9 | 0.013s |
| `GF(32027)` | 8 | 16 | 11 | `NONUNIT` | 9 | 0.018s |
| `Q` | 8 | 16 | 11 | `NONUNIT` | 9 | 0.026s |

Depth 5:

| field | equations | Gbar unknowns | basis | verdict | dim | time |
|---|---:|---:|---:|---|---:|---:|
| `GF(32003)` | 13 | 25 | 38 | `NONUNIT` | 14 | 0.019s |
| `GF(32009)` | 13 | 25 | 38 | `NONUNIT` | 14 | 0.022s |
| `GF(32027)` | 13 | 25 | 38 | `NONUNIT` | 14 | 0.018s |
| `Q` | 13 | 25 | 38 | `NONUNIT` | 14 | 0.013s |

Depth 6:

| field | equations | Gbar unknowns | basis | verdict | dim | time |
|---|---:|---:|---:|---|---:|---:|
| `GF(32003)` | 18 | 36 | 337 | `NONUNIT` | 20 | 5.104s |
| `GF(32009)` | 18 | 36 | 337 | `NONUNIT` | 20 | 6.234s |
| `GF(32027)` | 18 | 36 | 337 | `NONUNIT` | 20 | 6.769s |
| `Q` | 18 | 36 | 337 | `NONUNIT` | 20 | 32.378s |

Branch-B build audit:

| depth | Gbar bands | Fbar bands | raw rows | Jacobian rows | forced rows | pruned rows | Gbar by z | build |
|---:|---|---|---:|---:|---:|---:|---|---:|
| 4 | `[27, 26, 25, 24]` | `[18, 17, 16, 15]` | 11 | 5 | 4 | 2 | `{'24': 4, '25': 4, '26': 4, '27': 4}` | 0.466s |
| 5 | `[27, 26, 25, 24, 23]` | `[18, 17, 16, 15, 14]` | 21 | 12 | 7 | 2 | `{'23': 5, '24': 5, '25': 5, '26': 5, '27': 5}` | 2.978s |
| 6 | `[27, 26, 25, 24, 23, 22]` | `[18, 17, 16, 15, 14, 13]` | 33 | 21 | 10 | 2 | `{'22': 6, '23': 6, '24': 6, '25': 6, '26': 6, '27': 6}` | 7.155s |

The branch-B solved dimension path is `4: [9], 5: [14], 6: [20]`.  Thus no drop or inconsistency appears in the solved high-z bands; the necessary family enlarges as additional lower coefficients are admitted.

At depth 6 the four fields agree on the same basis size and the same dimension.  The displayed basis is intentionally omitted in the logs once it exceeds 80 elements; the recorded size is still read from Singular's `size(G)` after the Groebner run.

Deepest branch-B family dimension seen by Singular is `[20]` at depth 6, counting the Jacobian scalar.  Fixing `gamma` would subtract one on nonunit components.

## Delta 5/2 Replay

Depth 4:

| field | equations | Gbar unknowns | basis | verdict | dim | time |
|---|---:|---:|---:|---|---:|---:|
| `GF(32003)` | 2 | 8 | 4 | `NONUNIT` | 7 | 0.021s |
| `GF(32009)` | 2 | 8 | 4 | `NONUNIT` | 7 | 0.019s |
| `GF(32027)` | 2 | 8 | 4 | `NONUNIT` | 7 | 0.019s |
| `Q` | 2 | 8 | 4 | `NONUNIT` | 7 | 0.017s |

Depth 5:

| field | equations | Gbar unknowns | basis | verdict | dim | time |
|---|---:|---:|---:|---|---:|---:|
| `GF(32003)` | 2 | 12 | 4 | `NONUNIT` | 11 | 0.018s |
| `GF(32009)` | 2 | 12 | 4 | `NONUNIT` | 11 | 0.019s |
| `GF(32027)` | 2 | 12 | 4 | `NONUNIT` | 11 | 0.020s |
| `Q` | 2 | 12 | 4 | `NONUNIT` | 11 | 0.018s |

Depth 6:

| field | equations | Gbar unknowns | basis | verdict | dim | time |
|---|---:|---:|---:|---|---:|---:|
| `GF(32003)` | 89 | 18 | 5 | `NONUNIT` | 16 | 0.030s |
| `GF(32009)` | 89 | 18 | 5 | `NONUNIT` | 16 | 0.026s |
| `GF(32027)` | 89 | 18 | 5 | `NONUNIT` | 16 | 0.029s |
| `Q` | 89 | 18 | 5 | `NONUNIT` | 16 | 0.029s |

Charged replay build audit:

| depth | Gbar bands | Fbar bands | raw rows | Jacobian rows | forced rows | pruned rows | Gbar by z | build |
|---:|---|---|---:|---:|---:|---:|---|---:|
| 4 | `[27, 26, 25, 24]` | `[18, 17, 16, 15]` | 5 | 3 | 2 | 0 | `{'24': 2, '25': 2, '26': 2, '27': 2}` | 0.059s |
| 5 | `[27, 26, 25, 24, 23]` | `[18, 17, 16, 15, 14]` | 15 | 13 | 2 | 0 | `{'23': 2, '24': 3, '25': 2, '26': 3, '27': 2}` | 0.396s |
| 6 | `[27, 26, 25, 24, 23, 22]` | `[18, 17, 16, 15, 14, 13]` | 95 | 93 | 2 | 0 | `{'22': 3, '23': 3, '24': 3, '25': 3, '26': 3, '27': 3}` | 19.671s |

The charged replay dimension path is `4: [7], 5: [11], 6: [16]`.  It reproduces the frozen depth-6 custody result: 89 equations, basis size 5, nonunit, dimension 16 over all three finite fields and over `Q`.

Deepest `delta=5/2` family dimension seen by Singular is `[16]` at depth 6, again counting the Jacobian scalar.

## Depth 7 and 8

The only new unknowns introduced in this licensed extension are Gbar coefficients in newly visible high-z slots.  Fbar coefficients are not independent; they are induced from `Gbar^2-Fbar^3`.  The driver does not introduce independent `T2` coefficients, `T3` coefficients, or Omega-centre parameters `a1,a2`.

Reason: the frozen charged sources license the Prop. 6.2 boxes and constant-Jacobian rows here, but leave the effective `T2 in K[f,g]` recurrence, the `T3` recurrence, and the major-side `4/9` centre as missing full-lift data.  Adding those variables without the printed map would be an invented system.

Branch B delta=2:

- depth 7: new Gbar unknowns 13 with z-band split {'21': 7, '22': 1, '23': 1, '24': 1, '25': 1, '26': 1, '27': 1}; status `NEXT-SYSTEM-NOT-SOLVED-IN-THIS-LANE`, verdict `NOT-RUN`, dimensions [].
  New coefficient slots: `g_27_65`(z=27, y=65, order=7), `g_26_63`(z=26, y=63, order=7), `g_25_61`(z=25, y=61, order=7), `g_24_59`(z=24, y=59, order=7), `g_23_57`(z=23, y=57, order=7), `g_22_55`(z=22, y=55, order=7), `g_21_53`(z=21, y=53, order=7), `g_21_54`(z=21, y=54, order=6), `g_21_55`(z=21, y=55, order=5), `g_21_56`(z=21, y=56, order=4), `g_21_57`(z=21, y=57, order=3), `g_21_58`(z=21, y=58, order=2), `g_21_59`(z=21, y=59, order=1).
- depth 8: new Gbar unknowns 15 with z-band split {'20': 8, '21': 1, '22': 1, '23': 1, '24': 1, '25': 1, '26': 1, '27': 1}; status `NEXT-SYSTEM-NOT-SOLVED-IN-THIS-LANE`, verdict `NOT-RUN`, dimensions [].
  New coefficient slots: `g_27_64`(z=27, y=64, order=8), `g_26_62`(z=26, y=62, order=8), `g_25_60`(z=25, y=60, order=8), `g_24_58`(z=24, y=58, order=8), `g_23_56`(z=23, y=56, order=8), `g_22_54`(z=22, y=54, order=8), `g_21_52`(z=21, y=52, order=8), `g_20_50`(z=20, y=50, order=8), `g_20_51`(z=20, y=51, order=7), `g_20_52`(z=20, y=52, order=6), `g_20_53`(z=20, y=53, order=5), `g_20_54`(z=20, y=54, order=4), `g_20_55`(z=20, y=55, order=3), `g_20_56`(z=20, y=56, order=2), `g_20_57`(z=20, y=57, order=1).

Delta 5/2 charged replay:

- depth 7: new Gbar unknowns 6 with z-band split {'21': 3, '22': 1, '24': 1, '26': 1}; status `NEXT-SYSTEM-NOT-SOLVED-IN-THIS-LANE`, verdict `NOT-RUN`, dimensions [].
  New coefficient slots: `g_26_66`(z=26, y=66, order=7), `g_24_61`(z=24, y=61, order=7), `g_22_56`(z=22, y=56, order=7), `g_21_54`(z=21, y=54, order=6), `g_21_55`(z=21, y=55, order=4), `g_21_56`(z=21, y=56, order=2).
- depth 8: new Gbar unknowns 8 with z-band split {'20': 4, '21': 1, '23': 1, '25': 1, '27': 1}; status `NEXT-SYSTEM-NOT-SOLVED-IN-THIS-LANE`, verdict `NOT-RUN`, dimensions [].
  New coefficient slots: `g_27_68`(z=27, y=68, order=8), `g_25_63`(z=25, y=63, order=8), `g_23_58`(z=23, y=58, order=8), `g_21_53`(z=21, y=53, order=8), `g_20_51`(z=20, y=51, order=7), `g_20_52`(z=20, y=52, order=5), `g_20_53`(z=20, y=53, order=3), `g_20_54`(z=20, y=54, order=1).

For both branches, the solved depth-4/5/6 systems therefore give only a counting bound.  The requested lower-band interaction with the major-side `4/9` centre is not encoded as a solved algebraic system in this lane because the available charged sources do not provide the centre map or the effective `T2` recurrence coefficients.

## Controls

Moh `(64,48)` Appendix-II calibration: 77 equations, 19 unknowns excluding `T`; `Q` run verdict `SATURATED-EMPTY`, basis size `1`.  Empty-wrapper, nonempty-wrapper, and unsaturated-nonunit controls passed.

Automorphism control: `F=x+y^6`, `G=y+(x+y^6)^7` has degrees `[6, 42]` and direct Jacobian `1`.  The two-infinity control remains the linear witness `A=2,C=1`, `J=1`.

## FALLACY-v2

No exit-price assertion is made, so no `charge_basis` line is licensed.  The branch-B face point is not promoted to a full pair; the `delta=5/2` nonunit systems are not promoted to a full pair; and all saturation checks use explicit Rabinowitsch wrappers with declared Singular rings.  The major radii, the branch split order, and the unprinted Omega centre remain distinct.

## Reproduction

```text
python3 box/g9966B-20260903/g9966B_joint_driver.py
python3 ops/seal.py stamp xmodel/g9966-branchB-joint-gpt55-20260903.md --basis dd3488e6f00ac5940d1541384ab18bfc6038f4a9
python3 ops/seal.py verify xmodel/g9966-branchB-joint-gpt55-20260903.md
```

Primary artifacts:

```text
box/g9966B-20260903/g9966B_joint_driver.py
box/g9966B-20260903/g9966B_joint_results.json
box/g9966B-20260903/systems/*.sing
box/g9966B-20260903/logs/*.log
box/g9966B-20260903/artifacts.sha256
```

Typed final:

```text
COUNTING-BOUND[BRANCH-B-HIGH-Z-DEPTH6-NONUNIT]
COUNTING-BOUND[DELTA-5/2-HIGH-Z-DEPTH6-NONUNIT]
OPEN[(99,66)-FULL-JOINT-NOT-DECIDED]
NO KELLER PAIR PRODUCED
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11087`.
- Body SHA-256:
  `ec45c7ffbe15d1391f925fda289856e42e3af17ec4bbc71ebcd856511920ebb2`.
- Frozen basis: `dd3488e6f00ac5940d1541384ab18bfc6038f4a9`.
