# K16 t=4 normalizer gate, hostile replay

Date: 2026-09-03.

## Verdict matrix

1. **CONFIRMED, fixed `t=4`.**  The receipt-verified `t4_order_system.py`
   regenerates the gauged `(52,36;49;3)` chart with 45 unknowns including
   `c` and 65 equations.  The charged normalization was replayed to the
   eight-generator system over `Q(sqrt15)`, and Singular 4.3.2 `nfmodStd`
   returned `[1]`.
2. **CONFIRMED, fixed `t=4`.**  The covering chain uses only `Q*` pivots before
   the torus slice, has positive grading, forces `x != 0` from `(C)` and
   `c != 0`, uses the full quadratic algebra/number field and not one chosen
   root, verifies every later unit pivot by inverse and resultant, and ends in
   `[1]`.  I found no pivot-zero branch and no missing conjugate branch.
3. **CONFIRMED, uniform in `t` for the normalizer lemma.**  Sympy over `Q(t)`
   verifies the displayed formulas for `g1,g2,g3`, `(H)`, `(C)`, the normalized
   `H_t,c_t`, `disc_y H_t=48(2t+1)^2(t+1)`, and `c_t` unitness in the
   separable rank-two algebra `A_t=Q[y]/(H_t)` for every integer `t >= 1`.
   The t=1..6 extractor confirms `3t+4` Q-constant pivots.  Dependency note:
   the extractor's generic `t_order_system.py` was not in this lane receipt,
   so I used the workspace copy with the extractor-expected SHA-256
   `e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28`.
4. **CONFIRMED with scope.**  The t=4 kill is fixed-t.  The all-t result here
   is the normalizer lemma, not a generic all-t `[1]` theorem.

No exit-price assertion is made here; no `charge_basis` line is emitted.

## Provenance and artifacts

The lane receipt `xmodel/k16-t4-normalizer-gate-gpt55-20260903.run.v2` was
parsed mechanically with `awk` into
`box/k16t4-gate-20260903/charged_inputs.sha256`; `sha256sum -c` returned `OK`
for all 14 frozen inputs under `/tmp/jc2-lane.F6oLuI/inputs`.  I did not
retype any digest for that check.

All new drivers and outputs are confined to `box/k16t4-gate-20260903/`.
`SHA256SUMS.final` has SHA-256
`b7d26dcdccf6954a9f3398744f873cd3f284a64aa9df66297c1ebba64948c730`, and
`sha256sum -c box/k16t4-gate-20260903/SHA256SUMS.final` checked 58 entries.
No ledger files, `jc2-lean`, or ideation files were edited.

Primary charged/replay program hashes:

| artifact | SHA-256 |
|---|---|
| `/tmp/jc2-lane.F6oLuI/inputs/t4_order_system.py` | `db5e54450444f27c56f00bbec287aea284c8dc190e0e549c2fea51e0dbdd6cee` |
| `/tmp/jc2-lane.F6oLuI/inputs/triangular_preprocess.py` | `f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93` |
| `/tmp/jc2-lane.F6oLuI/inputs/t4_normalization_probe.py` | `085aac73eafda284514bb2f10478f242d3535cca16ef7249043ed85b30a27faf` |
| `/tmp/jc2-lane.F6oLuI/inputs/t4_affine_reduce.py` | `66463156f99204648456ddf0105273517b64252ce6e792f92c051d13b2a3591f` |
| `/tmp/jc2-lane.F6oLuI/inputs/t4_emit_exact_certificate.py` | `42bfd85b39665717c6a885ba5c4b538f59020021b3ef9ad900bd06cb67db7312` |
| `box/k16t4-gate-20260903/deps/t3_normalized_slice.py` | `9e394dae1920e90413ff1aa6d0f5f8eb4dd9aa343a5826e0f4f8c586bd980ac7` |
| `box/k16t4-gate-20260903/run_t4_replay.py` | `9aab882c5a73c8e1485b9f3960a6a12627f0808b2106c44065e4886505fed46c` |

## t=4 mechanical replay

`run_t4_replay.py` rebuilt the gauged chart from the charged generator.  The
chart audit is `t4_chart_audit.json`, SHA-256
`bd0a12f36aff47476dbe5b254e4fca4eb4462d99837fe4ca2d292e69118b9dd7`.
The build took 7.691 s inside the driver.  Whole replay driver timing from
`run_t4_replay.err`: 16:33.32 wall, 770.70 user s, max RSS 210912 KiB,
exit 0.

Chart dimensions:

```text
t = 4, (e,q) = (13,9)
unknowns including c = 45
equations = 65
h-powers = 0..17
degree histogram = {1:1, 2:6, 3:30, 4:28}
equation vector SHA-256 = 0e672bb86c0115883a02932ce5c1894fd0e24940dd3d5034073e840062d3c3a2
```

The first-stage constant reduction is exactly 16 `Q*` pivots.  Pivot
variables:

```text
a5_1,a6_1,a7_1,a8_1,a9_2,a9_1,a10_2,a10_1,
a11_2,a11_1,a12_2,a12_1,a13_2,a13_1,a13_0,a13_3
```

Pivot coefficients:

```text
9,9,9,9,18,9,18,9,18,9,18,9,18,9,-36,-27/4
```

Thus no first-stage pivot-zero branch exists in characteristic zero.  The
reducer verified the composed ring map on every original generator and kept
`c` fixed.  It produced 48 residual rows in 29 variables including `c`.
`t4_normalization_audit.json` has SHA-256
`df33323df108ec4268de6196353d49989b0de34da4340d0ffa17f0ce62957c97`;
`t4_normalized_rows.tsv` has SHA-256
`eca6c7e0026703c7f17e22b750e7eb51cbd867a7d19b4b900c104db161202020`.

The residual monomial-difference grading matrix has 3650 distinct constraints,
rank 28 on 29 variables, nullity 1.  The primitive positive weights include

```text
wt(q5_1)=17, wt(q9_1)=34, wt(c)=85
```

With `x=q5_1`, `y=q9_1`, the decisive rows are

```text
35*x^4 - 270*x^2*y + 486*y^2 = 0
-2187*c + 130*x^3*y - 1404*x*y^2 = 0
```

The second row is `(C)` at `t=4`; with `c != 0` it forces `x != 0`.  The
positive grading justifies the `x=1` slice over an algebraic closure.  The
displayed all-t specialization is

```text
972*y^2 - 540*y + 70
```

with integer content 2 and discriminant `19440 = 1296*15`.  The primitive
polynomial used for the coefficient field is

```text
H_4 = 486*y^2 - 270*y + 35
disc(H_4) = 4860 = 324*15
```

so the field is `Q(sqrt15)`.  The map used in the exact certificate is
`y -> (15+sqrt15)/54`; since the Singular ring has minpoly
`sqrt15^2-15`, this is the full abstract field `Q[y]/(H_4)`, not a discarded
conjugate.  The inverse map is `sqrt15 -> 54y-15`, so both conjugates are
covered by the field embedding.

After the slice and passage to `Q[y]/(H_4)`, the audit has 38 rows in 26
auxiliary variables.  The affine pass over the quadratic algebra has SHA-256
`630fee24008674e903c31b6097fbaabccd3acd1133249577e56d830c4e2f47a5` and took
802.530 s inside the replay.  It performed 22 checked unit pivots, each with
inverse identity and substitution identity verified modulo `H_4`, leaving
eight rows in four variables:

```text
variables = b3,b4,a2_0,q3_0
bands = 0,1,2,3,4,5,6,7
tags = all (gamma_power,pi_power)=(0,1)
degrees = 17,16,15,14,13,12,11,10
```

`t4_unit_norms.json`, SHA-256
`33cde6746d7832f1ead8826b6be761298db9787cbed162ef9d1e485c7213cbab`,
records nonzero resultants and determinant norms for all 22 affine pivot
coefficients.  It also rechecks
`q9_1`, `130-1404*q9_1`, and `cbar` as units.  Example unit data:

```text
Res(H_4,q9_1)=35
Res(H_4,130-1404*q9_1)=27925560
Res(H_4,cbar)=4022200/19683
```

The exact number-field Singular program
`t4_exact_Qsqrt15_nfmodstd.sing` has SHA-256
`d4f75dec682e8990bd10b73045018d734f6790651d86baa37ea211a0c0fbdc17`.
Singular 4.3.2 returned, in 0:01.03 wall and 15424 KiB max RSS:

```text
CONTROL_ACTUAL_PAIR_PASS J=gamma
CONTROL_C_UNIT_PASS
CONTROL_RK_RING_PASS
MAIN_START t=4 field=Qsqrt15 rows=8 vars=4 method=nfmodStd
MAIN_DONE basis_size=
1
MAIN_EXACT_UNIT
G[1]=1
```

Singular stderr was empty.  This is the characteristic-zero fixed-t
certificate.

## Modular full-chart checks

The receipt-verified charged generator emitted the full 65-row, 45-parameter
gauged chart at each prime.  I then made a mechanical method-only variant
replacing the main `std(I)` line by `slimgb(I)` and adding a method marker;
controls and generators were unchanged.  These are typed
**MEASURED-MODULAR** cross-checks, not the characteristic-zero proof.

| field | full-chart `slimgb` input SHA-256 | wall / max RSS | result |
|---|---|---:|---|
| `GF(32003)` | `31f6b01589ef4721b84b82128a647943bd4e1d09826a9749f36c8ba3bc756ff2` | 3:43.25 / 1186772 KiB | `[1]` |
| `GF(65521)` | `96c35bf62794bbb7700ad25f57a4c84d90408040e473c0c20286c7e86b8f1328` | 7:07.48 / 511960 KiB | `[1]` |
| `GF(1000003)` | `44a6d141401d2ae3af36254f633a105f7514abbb5c862262f322ae61b00acb00` | 7:50.30 / 507188 KiB | `[1]` |

All three printed `MAIN_START equations=65 parameters=45 plus_T=1`,
`MAIN_SATURATED_EMPTY`, and `G[1]=1`; all three Singular stderr files were
empty.

## All-t normalizer lemma

The charged `uniform_binomial_identities.py` ran with source SHA-256
`39469e4e4b4cfab455aea9a919d595a3e05e9d666913c5285862198b927e4707`,
exit 0, 0:01.81 wall, max RSS 48224 KiB, and printed
`ALL_BINOMIAL_IDENTITIES_PASS`.

The independent added audit `all_t_formula_audit.py`, SHA-256
`fff9e5f79e678aef4ffb137c674b5196541e936f4982e45482060325a65c896e`,
ran in 0:01.21 wall, max RSS 52764 KiB, exit 0.  Its JSON SHA-256 is
`d464b7ee1d5682ce8135e3f5b73e04399dcfebc0b8645d8b79cd3ec2b2b517d2`.

Over `Q(t)`, with `q=2t+1`, `e=3t+1`, `r=e/q`, the checked solution is

```text
g1 = r*x
g2 = r*y + binom(r,2)*x^2
g3 = 2*binom(r,2)*x*y + binom(r,3)*x^3
```

The audit verifies `E1=E2=E3=0`,

```text
E4 = t*(3t+1)*Hhat_t/(6*(2t+1)^3)
E0 with c=cimage is 0
```

where

```text
Hhat_t = 12*(2t+1)^2*y^2 - 12*(2t+1)*(t+1)*x^2*y
         + (t+1)*(3t+2)*x^4
c = t*(3t+1)*x*y*((t+1)*x^2 - 6*(2t+1)*y)/(6*(2t+1)^3)
```

Since `(C)` is divisible by `x`, `c != 0` forces `x != 0`.  The grading formula
has `wt(x)=4t+1`, `wt(y)=8t+2=2(4t+1)`, and
`wt(c)=20t+5=5(4t+1)`, all positive for `t >= 1`.  The `x=1` normalized
relations are

```text
H_t(y)=12*(2t+1)^2*y^2 - 12*(2t+1)*(t+1)*y + (t+1)*(3t+2)
c_t(y)=t*(3t+1)*y*((t+1)-6*(2t+1)*y)/(6*(2t+1)^3)
disc_y(H_t)=48*(2t+1)^2*(t+1)
```

For the full numerator of `c_t`, the symbolic resultant is

```text
Res_y(H_t, t*(3t+1)*y*((t+1)-6*(2t+1)*y))
= 12*t^2*(t+1)^2*(2t+1)^2*(3t+1)^2*(3t+2)*(4t+1)
```

Every factor is nonzero for every positive integer `t`, hence there is no
positive integer root.  The content issue is handled separately: specializing
`H_t` can introduce nontrivial integer content, but nonzero content does not
change the roots or gcd/unit question over `Q[y]`.  The two direct factor
checks also pass:

```text
H_t(0) = (t+1)*(3t+2)
H_t((t+1)/(6*(2t+1))) = (t+1)*(4t+1)/3
```

Thus `c_t` is a unit in `A_t=Q[y]/(H_t)` for every integer `t >= 1`, including
split fibers.  The correct uniform object is the separable rank-two algebra;
it is a field only off the split set.

## Q-pivot count t=1..6

The charged extractor ran with patched lane-local paths in
`run_uniform_extractor_t1_6.py`.  Output SHA-256:
`0cbd5231f6489d2fd02d592291e7da88a1f54b12261cce9c78b8a140f221e765`.
Timing: 23:50.72 wall, 1269.42 user s, max RSS 354048 KiB, exit 0.
stderr was empty.

The mechanical `DIMS` lines confirm `3t+4`:

| `t` | equations / unknowns | Q pivots | `3t+4` | residual rows / unknowns |
|---:|---:|---:|---:|---:|
| 1 | 23 / 18 | 7 | 7 | 15 / 11 |
| 2 | 37 / 27 | 10 | 10 | 26 / 17 |
| 3 | 51 / 36 | 13 | 13 | 37 / 23 |
| 4 | 65 / 45 | 16 | 16 | 48 / 29 |
| 5 | 79 / 54 | 19 | 19 | 59 / 35 |
| 6 | 93 / 63 | 22 | 22 | 70 / 41 |

The same output prints positive grading and homogeneous residual rows for each
`t=1..6`, together with the sparse `(C)` and `H` rows.

## Fallacy-v2 check

Typed scope is explicit throughout: fixed-t kill versus uniform normalizer
lemma.  The chart is treated as a necessary superset, so unit ideal proves
emptiness, while modular `[1]` is only a measured cross-check.  The ring maps,
generator order, coefficient fields, quotient/algebra distinction, `sat` or
Rabinowitsch wrappers, positive/negative controls, and raw-remainder
normal-form requirements were checked by the generated drivers.  I do not
promote a generic all-t `[1]` result.

<!-- BODY-END -->
