# Q6 affine-ADE threat map v2: nonnegative global `B`-degree

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra sublane `/root/u_rows_global_lattice`  
Frozen basis: `54df5b64b5ea8355cd8c13aa790dcf0f703c5bb7`  
Lifecycle: **EXACT CORRECTED PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Corrected verdict

The sealed v1 report made one unjustified restriction: it required

```text
a_j=B.C_j>0
```

for every global reduced strict prime.  That is numerically forced in `U3`,
but it was not proved uniformly in `B3`.  This v2 replay instead enumerates

```text
a_j>=0                                                    (0.1)
```

in every one of the 14 affine cells and 14 rank-zero/carrier controls.

The larger enumeration still has

```text
pair-condition matches before carrier filtering: 0;
necessary lattice survivors:                       0.
```

The conclusion of v1 therefore survives, but its positive-`a` proof does
not.  V2 supersedes v1 for every q=6 theorem or integration.  The sealed v1
bytes were not changed.

Relative to the exact positive-only v1 control, v2 adds

```text
142 branch-feasible metadata rows,
142 exact-join metadata rows,
3317 individual adjunction-valid candidate records.       (0.2)
```

Every added row is passed to the exact weighted coordinate join; none even
satisfies the local pair conditions.  Hence no carrier-incidence or
unlabelled-cycle rule is load-bearing.

The maximum theorem remains conditional on the root-verified but
different-model-review-gated q=6 local contact audit and on the binding
quadratic-F5 global inputs.  Under those inputs, neither `U3/A3` nor any
`B3/A2` modulus has a necessary global boundary configuration.  This does
not prove the quadratic frame occurs, treat nonquadratic incidences, or prove
JC2.

## 1. Exact issue and the two meanings of “vertical”

Keep the physical-prime class and degree formulas

```text
C_j=a_jS0+(2a_j+epsilon_j)F-sum_i x_(ji)P_i,

d_j=A.C_j=5a_j+2epsilon_j-sum_i x_(ji),
t_j=T.C_j=3a_j+epsilon_j-sum_(i in I)x_(ji),          (1.1)

a_j,epsilon_j,t_j,x_(ji)>=0.
```

For Cartier weights `w_j`, the total class gives

```text
sum_j w_j a_j=A0,          A0=4 or 3 after one Z,
sum_j w_j epsilon_j=1,
sum_j w_j t_j=1.                                      (1.2)
```

If `a_j=0` and `d_j>0`, then (1.1)--(1.2) force

```text
w_j=1,       epsilon_j=1,       d_j<=2.               (1.3)
```

Indeed a weight-two prime cannot own the unit `epsilon` contact, and with
`epsilon=0` its degree would be `-sum x_i<=0`.  The complete global
`B.C=0` numerical possibilities are therefore

```text
d=2: C=F,                 t=1;
d=1: C=F-P_o,             t=1;
     or C=F-P_i,           t=0,                       (1.4)
```

up to the allowed `O` or `I` label.  Their adjunction delta is zero.

This global usage must not be confused with the local phrase “vertical
prime.”  The local family `f=h+uv` realizes the analytic doubled prime
`{v=z=0}` in a local coordinate chart.  It proves that a coefficient-two
local prime cannot be omitted from the local census.  It does **not** by
itself realize a full global marked class with `B.C=0`.  In fact (1.3)
shows that the coefficient-two prime cannot be the global unit-contact owner.
The tau-zero doubled rows gain candidates only through their separate
coefficient-one degree-two prime, not by declaring the local doubled prime a
global `B`-vertical curve.

For `U3`, both physical degrees are four, so (1.3) proves `a_j>0` after all.
The same is true for the two degree-four primes in an odd-discriminant
`B3` block.  The nonzero-modulus doubled block also gains nothing: its
weight-one prime has degree four and its degree-two prime has weight two.

## 2. Frozen evidence and preserved v1

The corrected replay charges the same verified inputs as v1:

```text
48717ce3d8b3c5ef6926e3b5ebcf2a0d94ad7bee42ea4ea1c253fb4fd9463649
  xmodel/bd-a2-q6-local-contact-audit-sol56-20260830.md
  body 941d4e27b95bee2483b98fa62c4e1b9c9b94e7dff7aa200848ab03977461522d
  manifest 222d1bffbd05d08103712f922e8baf5710fcf58dc23d144503c4ec94a4cbda83

f092a7152dea8bdee387825fa8181dffeb8145fc99cf65973d74f528491f57a0
  binding Euler/A1-ruling integration

6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08
  binding rational-forest integration

a5bf78c8ab8704884e9bb3c084c88059e01ec7690c1d6f645a9e87a0aa70a884
  binding normal-F5 carrier/effectivity integration.
```

The preserved v1 artifacts are

```text
report full ffa81bfce15077b02d9a44974890b7fd49d09553be4a1f788136c722ddc4cdf2
report body ef8e80f4744e382d98bbfbfe4c335d1c7feac217e7ffc689ae3d8e4fe1ce9a7e
manifest    cafbb864460b4850db9807b170982d66dfa21fe7e37b3f971e7650882729b01a
v1 replay  b892cd1520f13f10093fc51f547672cb8145ad4949c92a86a6ecb9055f3bdd46.
```

V2 hash-checks the v1 replay before importing its finite root and class
engine.  It runs that engine twice: once with all nonnegative weighted
compositions and once with the old positive-only compositions.  The latter
must reproduce the exact v1 output SHA
`293f2aee078dbcb0448c57ce4720646503719e2596a9454e709736baa041d602`.
This makes (0.2) an executable exact comparison, not a comparison of two
hand-copied tables.

No active external log/report, web source, heavy CAS, `jc2-lean`, or
`pilot-local.log` was accessed.

## 3. Exhaustive global vertical classification in the cells

The root allocation, Euler caps, strict totals, carrier list, weighted local
partitions, contact-depth corrections, and chronological `O` filter are
unchanged from v1.  Only the domain of the `a` composition changes.

The cells which gain affine metadata are exactly:

| affine cell | v1 metas | v2 metas | added metas | added candidate records |
|---|---:|---:|---:|---:|
| `B3 tau!=0,Delta!=0` | 16 | 32 | 16 | 260 |
| same `+Z` | 18 | 46 | 28 | 204 |
| `B3 Delta=0`, split | 16 | 32 | 16 | 260 |
| same `+Z` | 18 | 46 | 28 | 204 |
| `tau=0`, distinct residual | 0 | 7 | 7 | 142 |
| `tau=0`, split residual | 0 | 7 | 7 | 142 |
| `tau=0`, odd residual | 7 | 9 | 2 | 6 |
| `tau=0`, doubled residual | 2 | 9 | 7 | 47 |

The following affine cells gain exactly zero metadata:

```text
U3, U3+Z;
B3 Delta=0 odd, with or without Z;
B3 Delta=0 doubled, with or without Z.                (3.1)
```

This matches (1.3): only coefficient-one local primes of degree one or two
can produce a new global `a=0` branch.

The rank-zero/control cells which gain metadata are:

| rank-zero control | v1 metas | v2 metas | added metas | added candidate records |
|---|---:|---:|---:|---:|
| generic `B3` | 11 | 15 | 4 | 268 |
| generic `B3+Z` | 1 | 3 | 2 | 74 |
| split `Delta=0` | 11 | 15 | 4 | 268 |
| same `+Z` | 1 | 3 | 2 | 74 |
| `tau=0`, distinct residual | 1 | 8 | 7 | 584 |
| `tau=0`, split residual | 1 | 8 | 7 | 584 |
| `tau=0`, odd residual | 9 | 13 | 4 | 148 |
| `tau=0`, doubled residual | 1 | 2 | 1 | 52 |

All other rank-zero controls gain zero.  The affine additions total 111
metadata rows and the rank-zero additions total 31, giving (0.2).

## 4. Corrected lower bounds and the exact-join backstop

The coefficient-one energy inequality remains valid for nonnegative `a`:

```text
sum_(j<k) C_j.C_k
 >=2sum_(j<k)a_ja_k+A0-a_e
   -(sum_i(c_i^2-c_i))/2.                             (4.1)
```

Its derivation uses `x^2>=x`, not `a_j>0`.  For split and doubled blocks,
the block-versus-complement Cartier inequality also remains

```text
D_G.D_H
 >=2a_Ga_H+a_G epsilon_H+a_H epsilon_G
   -(sum_i(c_i^2-c_i))/2.                             (4.2)
```

The corrected chronology-filtered diagnostic minima are:

| affine cell | no `Z` | one `Z` | diagnostic used |
|---|---:|---:|---|
| `U3` | 1 | 2 | (4.1) |
| generic `B3` | 3 | 3 | (4.1) |
| split `Delta=0` | 2 | 2 | (4.2) |
| odd `Delta=0` | 1 | 2 | (4.1) |
| doubled `Delta=0` | 1 | 1 | (4.2) |
| `tau=0`, distinct residual | 6 | impossible | (4.1) |
| `tau=0`, split residual | 1 | impossible | (4.2) |
| `tau=0`, odd residual | 4 | impossible | (4.1) |
| `tau=0`, doubled residual | 0 | impossible | direct `F` intersection plus exact join |

The zero in the last row is honest.  V2 does not turn it into a positive
bound by reinstating horizontality.  There is nevertheless a one-line
geometric numerical kill for every newly added meta in that row: its only
possible global vertical branch is the coefficient-one degree-two class
`F`, and

```text
F.C_k=a_k>0
```

for the distinct-site degree-four companion, which is necessarily
horizontal.  Its nine feasible metadata rows and 79 candidate records are
also passed to the exact weighted join; none satisfies the required
cross-pair intersections.  More generally this direct `F` intersection
kills every newly added degree-two vertical branch whenever it has a
distinct-site degree-four companion.  Degree-one vertical candidates in the
tau-zero four-prime rows remain covered by (4.1)--(4.2) and the exact join.

For the rank-zero controls the corresponding minima are

```text
U3: 3 / 3 with Z;
generic B3: 4 / 4 with Z;
split block: 3 / 3 with Z;
odd block: 3 / 3 with Z;
doubled block: 4 / 3 with Z;
tau0 distinct/split/odd/doubled: 7,2,3,3.              (4.3)
```

No energy or aggregate diagnostic prunes an executable metadata row.  Every
feasible row is joined exactly.  In all 28 rows of the cell/control table,
the count of exact weighted decompositions satisfying the local pair rules
is zero before the carrier-forest filter.  Thus the result is independent of
the conceptual lower bounds and of unresolved same-owner carrier triples.

## 5. Full corrected replay table

`Candidates` is the sum of individual adjunction-valid branch-list records
across exact-join metadata, not a count of effective configurations.

| affine cell | allocation orbits | feasible allocations | join metas | candidates | pair matches | survivors |
|---|---:|---:|---:|---:|---:|---:|
| `U3` | 31 | 7 | 40 | 656 | 0 | 0 |
| `U3+Z` | 26 | 8 | 28 | 176 | 0 | 0 |
| generic `B3` | 31 | 4 | 32 | 714 | 0 | 0 |
| generic `B3+Z` | 26 | 8 | 46 | 390 | 0 | 0 |
| split block | 31 | 4 | 32 | 714 | 0 | 0 |
| split block `+Z` | 26 | 8 | 46 | 390 | 0 | 0 |
| odd block | 62 | 8 | 42 | 660 | 0 | 0 |
| odd block `+Z` | 70 | 16 | 58 | 262 | 0 | 0 |
| doubled block | 62 | 10 | 16 | 163 | 0 | 0 |
| doubled block `+Z` | 70 | 6 | 6 | 19 | 0 | 0 |
| `tau=0`, distinct residual | 8 | 1 | 7 | 142 | 0 | 0 |
| `tau=0`, split residual | 8 | 1 | 7 | 142 | 0 | 0 |
| `tau=0`, odd residual | 22 | 1 | 9 | 129 | 0 | 0 |
| `tau=0`, doubled residual | 22 | 4 | 9 | 79 | 0 | 0 |

The corrected rank-zero/control table is:

| control | join metas | candidates | pair matches | survivors |
|---|---:|---:|---:|---:|
| `U3` / `U3+Z` | 6 / 2 | 972 / 72 | 0 / 0 | 0 / 0 |
| generic `B3` / `+Z` | 15 / 3 | 1623 / 134 | 0 / 0 | 0 / 0 |
| split block / `+Z` | 15 / 3 | 1623 / 134 | 0 / 0 | 0 / 0 |
| odd block / `+Z` | 6 / 2 | 972 / 72 | 0 / 0 | 0 / 0 |
| doubled block / `+Z` | 1 / 1 | 141 / 21 | 0 / 0 | 0 / 0 |
| `tau=0`, distinct residual | 8 | 664 | 0 | 0 |
| `tau=0`, split residual | 8 | 664 | 0 | 0 |
| `tau=0`, odd residual | 13 | 827 | 0 | 0 |
| `tau=0`, doubled residual | 2 | 112 | 0 | 0 |

The affine-root inventory is unchanged, as it must be: only the strict-prime
`a` domain changed.  The inventory digests remain

```text
rank 3 ordinary: 4e584d96f2e8312388d1576d549473ac628ad74aced2fef09e50379fdf4e6ff0
rank 2 plus Z:   f46c9543e7ec0935347a71bfdd57ac54f02cabb06633de8401b085833bc7104c
rank 4 ordinary: 4932df18ae6e297686b495698ebda75e481c82de758cf4e5aa35c82ad173bf13
rank 3 plus Z:   428206d838650d097d7816e090189971057013115cdad17219ca421a4f68518d
tau0 rank 2:     5b5969b7bc521f5ddd3717cefd142c071c14bebb635c6c075b3588bf02b80f80
tau0 rank 3:     31e66e9e8be4f7083bf848c4727bf3fc30c842fb3f63d45fd7b7065aabd0d5db.
```

The empty survivor payload also remains exactly 830 bytes with SHA
`ab2fc3c6c5d47160fa947542dd5d33e375c9221a43df05c10cd99cfb6926b46d`.

## 6. Executable vertical-domain control

The v2 wrapper checks a literal global numerical vertical class before the
full enumeration:

```text
C=F,  a=0, epsilon=1, t=1, d=2, x=(0,...,0), delta=0,
B3 B-degree partition (1,0,3).                        (6.1)
```

It then verifies the exact cell deltas in Section 3.  In particular, generic
`B3` must gain exactly 16 affine metadata rows and the `tau=0` distinct row
must gain exactly seven, while `U3` and the nonzero-modulus doubled block
must gain zero.  This proves that the corrected full engine—not merely a
standalone helper—actually traverses the `a=0` domain.

The old-pass/new-fail mutation

```text
--mutate-drop-vertical
```

restores the v1 positive-only generator.  It must exit nonzero with

```text
FAIL:vertical a=0 domain was not exercised
```

The independent contact-vector mutation remains and must fail with

```text
FAIL:q6 baseline multiplicity sum must be fourteen
```

## 7. Replay

The v2 replay is

```text
ops/q6_f5_affine_ade_threat_replay_v2.py
SHA-256 c2ca2874b9bf80a9612010d034118d0f854a9c0cb6167b0865d22470374a0c56
```

It hash-pins the preserved v1 engine.  Run:

```bash
q6_tmp=$(mktemp -d)
python3 ops/q6_f5_affine_ade_threat_replay_v2.py > "$q6_tmp/ordinary.json"
python3 -O ops/q6_f5_affine_ade_threat_replay_v2.py > "$q6_tmp/O.json"
python3 -OO ops/q6_f5_affine_ade_threat_replay_v2.py > "$q6_tmp/OO.json"
cmp "$q6_tmp/ordinary.json" "$q6_tmp/O.json"
cmp "$q6_tmp/ordinary.json" "$q6_tmp/OO.json"
shasum -a 256 "$q6_tmp/ordinary.json" "$q6_tmp/O.json" "$q6_tmp/OO.json"
```

All outputs are byte-identical, 37,859 bytes, with SHA

```text
27ca7c500f411843c34c1aad60d51261b6e66e9ba712eddf48aa67893add8f3e.
```

Before v2 metadata is attached, the corrected nonnegative-domain engine has
raw SHA
`33d8841e0609857220f80fc3d46e8a33ccfc655ef19bfb42b465ee802ae13216`.
The exact positive-only control has the v1 SHA quoted in Section 2.

Both the v1 engine and v2 wrapper have zero Python AST `assert` nodes.  Both
mutations fail in ordinary, `-O`, and `-OO` modes with the displayed exact
diagnostics.  The
ordinary two-domain comparison used about 3.7 seconds and 30 MB resident
memory.  It is a standard-library desk replay; neither AWS nor a heavy CAS
is needed.

## 8. Disposition

1. Mark the sealed v1 theorem as superseded by this corrected enumeration;
   preserve its bytes as provenance.
2. Submit v2 and the underlying local analytic audit to independent hostile
   review before integration.
3. If both pass, the conditional q=6 closure may be integrated.  The
   integration must say `a_j>=0`, retain the distinction between local and
   global verticality, and must not claim `f=h+uv` realizes a global marked
   configuration.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14628`.
- Body SHA-256:
  `03590225ea52239df4d485b4b7aaac015af4d4e8975aba299b637663f6ce2f34`.
- Frozen basis: `54df5b64b5ea8355cd8c13aa790dcf0f703c5bb7`.
