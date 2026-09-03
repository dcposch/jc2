# BRANCH-ORBITS v2 hostile review (GPT-5.5), 2026-09-03

Charged input hashes were verified first against `/tmp/jc2-lane.VgMpMH/inputs`;
all eight matched. I read only the frozen charged inputs and the rendered Moh
pages required below. I did not read any `ideation-20260903T1015Z-*` file, did
not inspect other lane reports, did not run `jc2-lean`, and did not edit any
ledger. The only write in this lane is this report.

Moh page images were rendered from
`refs/moh1983_jram340_configurations_of_roots.pdf`
(`6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51`)
at 300 dpi using journal page `N` = PDF page `N-139`. Page/line references
below use the layout extraction after image reread; formulas were checked
against the PNGs because OCR drops or corrupts display math.

## Hash Custody

```text
55db4a9ef9021ef28d3a86dbd3e44d5e3a5aa1b72d61ba23043497f78ba94411  branch-orbits-v2-grok46-20260903.md
aaea3c345b1d53f561798f6a3e4352722f56c50a762f141dfe5e59cf35b1f276  knapsack.py
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  census-rebase-opus5-20260902.md
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  d1-subtree-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  integration17-coordinator-fable51-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  d1floor.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  moh1983_jram340_configurations_of_roots.pdf
```

## Executive Verdict

The report is mostly correct, but it needs two scope repairs before promotion.

1. CONFIRMED, with wording repair. The `u` normalized slots of the top major
   factor lie under one major disc `D_{s-1}`. They are not `u` conjugate
   discs. However Lemma 6.1 alone does not prove this; the proof uses p.194
   top-form separation plus the p.200 theorem and Def. 5.1 counts. Lemma 6.1
   supplies the nonnegative next radius and the coordinate normalization.
2. CONFIRMED. For one bottom-major disc in one tower, the orbit size is
   `prod_{j=2}^{s-1} omega_j`, with `omega_j=A_j` on a nonzero `(10)` factor
   and `omega_j=1` on the zero `(11)` factor. The action on a nonzero
   `pi`-coordinate is genuinely free of order exactly `A_j`; smaller
   root-of-unity order of `a` and previous ramification do not shrink it.
3. CONFIRMED, with exactness scope. Conditions (8)-(13) are per tower, hence
   per orbit type. The shared constraint is packing in the relevant parent
   polynomial. At `s=3`, this is exact because the unique parent is `D_2` and
   `deg p=Q=V_3 d_2/d_3=u`. At `s>3`, the flat knapsack is only a relaxation.
4. CONFIRMED as measurement. The charged totals rerun in desk scale:
   all-`s` UNB orbit totals are 681 alive at `N>=6` and 575 alive in `[6,16]`;
   the exact `s=3` Z01 totals are 173 and 138 of 274; controls 336/0. Report
   repair: the script's own "STRICT s=3" printed total is global Z01, not the
   274-group subtotal. The 173/138 subtotal is correct but must be computed
   separately.
5. CONFIRMED. `D=88` is numerically emptied in `[6,16]` by the exact `s=3`
   orbit packing. It is not emptied at `N>=6`, because `N=18` survives.
6. CONFIRMED. The `D=105` trio survives as exactly three single nonzero orbit
   packets, all with `N=9`; the old UNI interval `[6..12]` on
   `m=70, M=[28,103], V_s=5` is refuted by orbit closure.
7. GAP if the all-`s` survivor count 575 is read as exact nested packing. It is
   an upper bound on survivors. Kills by the relaxation are valid kills, but
   survivors at `s>3` need `OPEN[NESTED-PACK]`.

Promotion recommendation: promote claims 1, 2, 3 at theorem strength after the
wording repairs above; promote the `s=3` exact knapsack and `D=88` kill; promote
the all-`s` UNB numbers only as a conservative relaxation; keep `BRANCH-ORBITS`
and `NESTED-PACK` open.

## Source Audit

### Top branch and the unique `D_{s-1}`

Moh p.150 is not a proof of UNI. The automorphism there is the eta-adic
automorphism of `k[x]((eta))`: OCR/image lines p.150:14-36 introduce `Omega_i`,
the analytic factorization at `g=infinity`, and symmetry of characteristic
tree data `{M_i,d_i}`. That concerns the curve expansion over `eta=g^{1/n}`,
not the later `t`-adic fibre tree of `g-c_2`, and it says nothing about the
lower `V` data of all bottom-major discs.

Proposition 4.4, p.168:3-23 and p.169:51-70, is the nonsplitting case:
under its hypotheses the leading coefficients are powers of one common linear
polynomial. This proves only that a disc must be shrunk further. Moh says so
explicitly on p.173:5-14: under Prop. 4.4 the disc is not a tree-data disc.

Proposition 4.5, p.169:87-96, says that in the `M_r=n-2` situation the highest
homogeneous forms have at most two linear factors and that the two multiplicities
are different. The exact top use appears on p.194:13-20: Moh restricts to
`M_s=n-2`, writes the highest homogeneous form with two distinct constants
`a != b`, and says the major disc `D_s` of radius `-1` contains a major
`D_{s-1}` and a minor `D^*_{s-1}`.

The p.200 theorem, p.200:12-37, says that for any `r>=2` the roots in `D_r`
are covered by disjoint subdiscs `E_i`, major ones extend the tower, minor ones
do not, the number of `E_i` is bounded by
`(n-M_r) V_{r+1}/d_{r+1}`, and at least one major `E_i` exists. At `r=s`,
`M_s=n-2` and `V_{s+1}=d_{s+1}` by Def. 5.1, so the bound is 2. Coupled with
p.194's two-factor top form and unequal multiplicities, this gives exactly one
major and one minor top child. Thus all normalized top-major slots lie under
one `D_{s-1}`.

Definition 5.1, p.179:19-50, fixes the counts in a tower. Criterion (1) says
`D_i` contains `(n/d_{i+1}) V_{i+1}` roots of `g`; criterion (4) says the
Prop. 4.6 polynomial at level `i` has degree
`v=V_{i+1} d_i/d_{i+1}`. For `i=s-1`, the number of `g`-roots in the top major
child is `(n/d_s)V_s=e u`, since `e=n/K`, `K=d_2`, and `u=V_s K/d_s`.
So "the `u` copies" must be read as normalized slots, not literal root count.

Lemma 6.1, p.194:33-40, proves that if `delta_s=-1` then `delta_{s-1}>=0`,
and then all roots in the major `D_{s-1}` have the displayed form. Lines
p.194:44-46 allow the coordinate choice making the major leading constant
zero. This supports the fixed top disc, but it is not by itself the source of
uniqueness; uniqueness comes from the two top factors and the unequal major/minor
split above.

Verdict on claim (1): CONFIRMED, with repair. Cite p.194 and p.200 for the
one major child; cite Lemma 6.1 only for `delta_{s-1}>=0` and normalization.

### Prop. 4.6 and later splits

Proposition 4.6, p.170:108-141 and p.171:190-195, gives the splitting
polynomial. For `r>=2`, the leading coefficients are powers of a common
`p(pi)` of degree `v`; `T_r,sigma(pi)` has an extra `q(pi)` factor; `q` has
distinct roots; every root of `p` is a root of `q`; `p` is not a power of `q`.
On p.173:20-25 Moh says the roots in such a disc are covered by subdiscs,
the number of subdiscs is the degree of `q(pi)`, the numbers of roots in the
subdiscs are unequal, and one chooses a sufficiently large subdisc to continue.

This is important against UNI: Galois conjugates of a chosen nonzero factor
have the same multiplicity, while Moh's actual `q`-children can have unequal
root counts. Unequal child counts force more than one orbit/type unless only
one child is major and every other child is discarded as minor. Moh supplies no
theorem that every bottom-major child in the fibre has the same lower
`V_2,...,V_{s-1}` data.

Verdict on global UNI: REFUTED as a theorem. A true weaker statement survives:
inside one local Galois orbit, the lower data are uniform. Across several
orbits they need not be.

## Orbit Size Proof

Moh's conditions (8)-(11) are on p.201:13-39. For a hypothetically existing
tower `D_s superset ... superset D_1`, line p.201:19 computes the radii from
Def. 5.1. Lines p.201:20-23 define `A_{r-1}` as the reduced denominator of
`L delta_{r-1}`, where `L` is the l.c.m. of the reduced denominators of
`delta_s,...,delta_r`. Lines p.201:25-30 give the division

```text
Q := V_r (d_{r-1}/d_r) = Delta_{r-1} A_{r-1} + Square_{r-1}
```

and the automorphism `tbar -> omega tbar` with `omega` an `A_{r-1}`-th root of
unity. Lines p.201:32-39 split the alternatives: (10) for a factor
`pi-a, a != 0`; (11) for a factor `pi`.

The freeness issue checks out. Work over the previous field
`k((t^{1/L}))`, so all earlier centre terms are fixed. Write
`L delta_{r-1}=B/A` with `A=A_{r-1}` and `(A,B)=1`; then
`t=(tbar)^{LA}` and `t^{delta_{r-1}}=(tbar)^B`. The automorphism sends the
new coefficient by `pi -> omega^B pi`. Since `(A,B)=1`, `omega^B` is primitive
of order `A`. If `a != 0`, then `(omega^B)^i a=a` implies `(omega^B)^i=1`,
hence `A | i`. The orbit has exactly `A` elements.

This also answers both hostile edge cases:

* If `a` is itself a root of unity of smaller order, it does not matter. The
  stabilizer condition is multiplicative cancellation by nonzero `a`, not a
  comparison of orders of `a`.
* If `A` shares factors with previous ramification, those factors are already
  in `L`; the new action is over `k((t^{1/L}))`, and the reduced denominator
  condition `(A,B)=1` makes the new multiplier primitive.

For the zero factor `pi`, the centre is fixed. The rest of `p(pi)` is a union
of free nonzero orbits, so `Q-V_{r-1}` is divisible by `A`; this is exactly
condition (11). For a nonzero factor, one entire orbit consumes
`A V_{r-1}` degree in `p`, giving condition (10).

Therefore one bottom-major disc in one tower has

```text
|O|(D_1) = product_{j=2}^{s-1} omega_j,
omega_j = A_j on (10), omega_j = 1 on (11).
```

When both (10) and (11) hold at a level, both centres are numerically possible;
the safe enumerator must keep both `omega_j=1` and `omega_j=A_j`.

Can a `(10)` level carry several orbits of the same multiplicity? Yes. Moh's
condition for one selected nonzero factor is only `A_j V_j <= Q_j`. If
`ell A_j V_j <= Q_j`, `p(pi)` may contain `ell` distinct nonzero Galois orbits
with the same multiplicity and different residue representatives. That does
not change the orbit size of any one disc; it only changes the packet count and
degree consumed. At `s=3`, the knapsack budget captures this exactly for
nonzero packets. At `s>3`, the parent-by-parent nesting remains open.

Verdict on claim (2): CONFIRMED. Promote the product formula per orbit; do not
promote any statement that product formula forces a single orbit or full
geometric realizability of the packet.

## (12)/(13) Are Internal to `D_1`

The p.188 image is decisive. Lines p.188:3-10 discuss conjugations of
`k((t^{1/A}))` over `k((t))`, where `A` is the reduced denominator of
`delta_1`. The polynomial under discussion is `g_sigma(pi)` of degree
`n* V_2`; this is the polynomial of the roots inside the selected bottom disc
`D_1`, not the parent polynomial whose roots are bottom discs. The same lines
also give the identity `A | (n*+m*)V_2 - 1`. Lines p.188:11-28 derive the
two alternatives leading to Moh's printed (12)/(13). P.201:39-47 explicitly
introduces (12)/(13) only after "when `r=2`".

Definition 5.1 also matches this reading: for `i=1`, `D_1` contains
`(n/d_2)V_2=eV_2` roots of `g`; there is no assigned `V_1`. Thus `A_1` is the
increment from `delta_2,...` down to the bottom radius `delta_1`, and it
controls the internal polynomial of the `D_1` roots. It is not an additional
Galois orbit multiplier for discs.

Verdict on claim (b): CONFIRMED. Repair only the language: say `(12)/(13)` is
the internal bottom-disc Galois condition on `g_sigma(pi)`, not a disc-orbit
condition and not a second packet weight.

## Packing and Exactness

For a selected orbit type, the packet is

```text
weight w = |O| V_2
value  c = |O| V_2 q,     q = (1-delta_1) d e/(d+e).
```

The shared parent can only supply the degree available in its `p(pi)`. For
`s=3`, the only split below the top major child is `D_2 -> D_1`, so
`j=2`, `r=3`, and the parent polynomial has

```text
Q = V_3 d_2/d_3.
```

The campaign's normalized top-major pool is

```text
u = V_s K/d_s.
```

At `s=3`, `V_s=V_3`, `K=d_2`, and `d_s=d_3`, hence algebraically

```text
Q = V_3 d_2/d_3 = V_s K/d_s = u.
```

The script's control confirms this on all 305 `s=3` V-assignments, but the
algebra is enough. Because there is only one parent `D_2`, there is at most
one zero-centred `pi` factor. Nonzero `(10)` packets may repeat subject to
degree budget; zero `(11)` packets are 0-1. This is exactly the script's Z01
model at `s=3`.

For `s>3`, the flat condition `sum |O_k| V_2^{(k)} <= u` is necessary but does
not reconstruct the nested choices of parent factors at every level
`j=s-1,...,2`. It is therefore a relaxation: if the relaxed knapsack has no
integral packet, the real nested packing has none; if it has one, that may be
a false survivor.

Verdict on claim (3)/(d): CONFIRMED with scope. Promote `s=3` exactness. Type
all all-`s` UNB survivor counts as upper bounds and all all-`s` UNB kills as
valid conservative kills.

## Script Review and Rerun

The charged `knapsack.py` hash matches. It has one engineering wart:
lines 31-35 hard-code `/tmp/jc2-lane.GqI4QH/inputs` ahead of the import. In
this run that path did not exist, so Python imported
`/home/ubuntu/jc2/box/moh_skeleton_full.py`, whose SHA-256 is the same
`d20bf084...` as the frozen input. The rerun is therefore valid here. Repair:
make the script import the enumerator relative to the frozen input directory
or require an explicit `--inputs` path; do not leave an old temp-lane path in
a promoted artifact.

The orbit model is implemented in `knapsack.py` lines 53-94:
`level_omegas`, `orbit_sizes`, and `packets` map each `(10)/(11)` level to
`{A_j}` or `{1}` and then form packet weights. The all-`s` UNB run is in
lines 405-475. The Z01 run is in lines 534-689; lines 534-536 state the
intended one-zero-factor restriction.

Rerun results:

```text
Controls: 336 checks, 0 failures.
Rebase reproduction: 1189 groups, UNI N>=6 670, UNI [6,16] 589,
mixed [6,16] 648, cap 0.
All-s UNB orbit: N>=6 681, [6,16] 575, cap 0.
Empty all-s UNB orbit [6,16]: D=48, D=88.
Empty all-s UNB orbit N>=6: D=48.
s=3 exact Z01 subtotal: 274 groups, N>=6 173, [6,16] 138.
```

The printed "STRICT s=3" total in the script is misleading: it prints global
Z01 totals (`611/493`) while only the per-row `s3alive16` column is an
`s=3` subtotal. I recomputed the `s=3` subtotals from the same objects:

```text
s=3 totals:
groups 274
UNI N>=6 187, UNI [6,16] 165
mixed [6,16] 166
UNB orbit N>=6 182, UNB orbit [6,16] 148
Z01 orbit N>=6 173, Z01 orbit [6,16] 138
```

Verdict on claim (c): CONFIRMED, with report/code repair for the stale import
path and the misleading "STRICT s=3" total label.

## Special Degrees

### `D=88`

The hostile check finds no escape hatch. The frozen enumerator has one group
and one assignment:

```text
n=88, m=66, M=[-33,86], s=3, K=22
d={1:88, 2:22, 3:11, 4:1}
V={2:1, 3:9, 4:1}, u=18
delta_2=3/14, delta_1=1/4, q=9/7
A_2=14, Q=18 = 1*14 + 4
(10)=true, (11)=false
A_1=2, (12)=true, (13)=false
```

Since `(11)` is false, the zero-centred child is not allowed. Since there is
only one V-assignment in the group, there is no second orbit type to mix. A
nonzero orbit has size 14, weight 14, and value

```text
14 * V_2 * q = 14 * 1 * 9/7 = 18.
```

A second such orbit would require weight 28, over the budget `u=18`. Thus the
orbit-admissible N-set up to 100 is exactly `{18}`. The old UNI survivor
`N=9` uses seven singleton copies and is not Galois closed.

Verdict on claim (e): CONFIRMED. `D=88` is emptied in `[6,16]` and survives
at `N>=6` via `N=18`.

### `D=105`

All 14 groups at `D=105` are `s=3`. The exact Z01 orbit survivors in `[6,16]`
are exactly the following three:

```text
m=70, M=[28,103], V_s=5, u=25, V_2=1, q=1/2,  A_2=18, |O|=18, N=9
m=70, M=[28,103], V_s=6, u=30, V_2=1, q=9/13, A_2=13, |O|=13, N=9
m=70, M=[40,103], V_s=4, u=28, V_2=1, q=9/17, A_2=17, |O|=17, N=9
```

The first row is the charged refutation of UNI: UNI allows
`N=k/2` for `12<=k<=24`, giving `[6..12]`; orbit closure forces
`k` to be 18 and leaves only `{9}`. All three survivors are nonzero `(10)`
packets, so the Z01 zero-factor issue is irrelevant.

Verdict: CONFIRMED. Promote as exact numerical `s=3` packing; not as geometric
realizability of a Keller pair.

### `D=117`

The all-`s` UNB table keeps four groups in `[6,16]`, but the exact `s=3` Z01
packing keeps only three. The killed row is

```text
m=78, M=[13,115], V_s=8, u=24, V_2=3, q=3/7,
A_2=21, |O|=1, (11)-only.
```

It is a single zero-centred packet with value `V_2 q=9/7`, not an integer.
UNI's `N=9` repeats the unique zero-centred packet seven times, which is not
allowed at the single parent `D_2`. The other three `D=117` rows are nonzero
packets and survive.

Verdict: CONFIRMED only when phrased as "Z01 exact drops `D=117` 4 -> 3";
REFUTE any reading that the all-`s` UNB column drops it, because UNB still
prints 4.

### `D=112` and `D>100`

The all-`s` UNB orbit count in `[6,16]` drops `D=112` from 29 mixed survivors
to 22. This is a valid conservative kill count because UNB is a relaxation.
Z01 drops further to 19, but that is not exact globally because `s>3` occurs.

No listed degree above 100 is emptied by the exact numerical filter. Even where
`s>3` exists, every `D in {105,108,112,117,120}` has exact `s=3` Z01 survivors
in `[6,16]`:

```text
D=105: 3
D=108: 10
D=112: 9
D=117: 3
D=120: 31
```

Verdict: CONFIRMED. Promote "no `D>100` empty" only as a numerical
(1)-(13) statement, still subject to `OPEN[STAR-REALISABILITY]` and
`OPEN[MOH-PROGRAM]`.

## UNI: What Survives

UNI does not survive as a theorem that all bottom-major discs in the fibre
share one lower `V` datum. The true replacement has three levels:

1. Within one Galois orbit, data are uniform. This is the only unconditional
   UNI-like theorem.
2. If an actual geometry has exactly one orbit type, then the allowable
   multiplicity count `k` is not free; it must be assembled from full orbit
   sizes. In the simple `s=3`, `(10)`-only case, `k` is a positive multiple of
   `A_2`. If `A_2 V_2=u`, that single nonzero orbit fills the parent and the
   UNI N-set collapses to one value `u q`.
3. If `|O|=1` because `A_j=1` on a nonzero branch, the old UNI arithmetic may
   coincide with orbit arithmetic. If `|O|=1` because of a zero `(11)` centre
   at `s=3`, UNI still does not allow arbitrary copies; the zero factor is
   unique in the parent.

Consequences for record N-sets:

```text
Moh six rows, orbit-admissible in [6,16]:
(64,48)                    {9}
(84,56) M2=64,V2=2         {}
(84,56) M2=72,V2=5         {10}   # old UNI 5 is removed
(75,50) V2=3               {9}
(75,50) V2=2               {8}
(99,66)                    {16}
```

The integration #17 UNI sets should be retained only as HYP/RELAXED records.
The promoted replacement is "orbit-admissible N-set" with the packet rule
above, exact at `s=3` and relaxed at `s>3` until nested packing is implemented.

Verdict on claim (f): UNI survives only inside one orbit and in special
one-orbit/full-orbit numerical cases. Global UNI N-sets are demoted.

## Open Items and Cheapest Tests

`OPEN[BRANCH-ORBITS]`.
Bounded quantity: number of Galois orbits of bottom-major discs, an integer
from 1 to `u`, plus the partition of `sum_B V_2(B) <= u` among orbit types.
Cheapest test: for each surviving numerical group, enumerate admissible orbit
packets with multiplicities and require parent degree budgets; this prices the
arithmetic. A theorem or explicit local construction is still needed to decide
which packet partitions are geometrically realizable.

`OPEN[NESTED-PACK]`.
Bounded quantity: for `D<=120`, `s<=5`, so the nested budget tuple has length
`s-2<=3`; at each level `j`, parts are bounded by
`Q_j=V_{j+1}d_j/d_{j+1}`. Cheapest test: replace the flat UNB DP by a
parent-indexed DP from `j=s-1` down to `2`, with one zero child per parent and
free nonzero orbit packets per parent. This is desk-scale and should decide
how many of the 575 all-`s` relaxed survivors remain numerically alive.

`OPEN[PROP-5.6-SHADOW]`.
Bounded quantity from census-rebase: 220 groups at `D<=120` and 1412 at
`121<=D<=200`. Cheapest test: do not use "all (11)" as a proxy. Track whether
the actual `sigma_1` has all previous coefficients zero, and add positive and
negative controls against Moh's six rows. The branch data exposed by (12)/(13)
alone is insufficient.

`OPEN[MOH-PROGRAM]`.
Bounded quantity from census-rebase: 652 excess rows and 59 excess `(n,m)`
classes at `n<=100` beyond Moh's p.202 table. Cheapest test: reimplement the
missing restrictions Moh's computer program applied, likely including minor
branch constraints, and require exact reproduction of p.202 before applying it
above 100.

`OPEN[V-FLOOR]`.
Bounded quantity from D1-SUBTREE: the integer choices
`V_j in (d_j/(n-M_j), V_{j+1}d_j/d_{j+1}]` for `j=2..s`, equivalently the
pinned `q` interval. Cheapest test: search the surviving exact orbit packets
for a lower bound on `V_2` or on `q`; absent a Moh/Jacobian theorem, this stays
as a measured floor problem, not an equality claim.

`OPEN[STAR-REALISABILITY]`.
Bounded quantity from D1-SUBTREE: for each surviving skeleton, the multiplicity
partition of the level-1 polynomial `p(pi)` of total degree `eV_2`. Cheapest
test: implement the Prop. 4.6 local construction at level 1 and kill any
skeleton forcing repeated roots where D1-STAR predicts simple roots.

No exit-price assertion is made in this report, so no `charge_basis` line is
applicable.

## Typed Verdict Block

```text
LANE          BRANCH-ORBITS v2 hostile review (GPT-5.5), 2026-09-03
INPUT         Frozen copies in /tmp/jc2-lane.VgMpMH/inputs; 8/8 hashes matched.
SOURCE        Moh 1983 JRAM 340 pp.150,168-171,173,179-180,188,194,200-202
              rendered at 300 dpi and checked against layout OCR.

CONFIRMED     Unique top-major D_{s-1}; u means normalized top-major slots,
              i.e. e*u roots of g under that disc.
CONFIRMED     Nonzero local orbit size exactly A_j; zero local orbit size 1;
              |O|(D_1)=prod_{j=2..s-1} omega_j per orbit.
CONFIRMED     Root-of-unity stabilizer objection fails: a!=0 cancels, and
              gcd(B,A)=1 after A is the reduced denominator of L*delta_j.
CONFIRMED     A (10)-level may contain several nonzero orbits of the same
              multiplicity; this repeats packets but does not change |O|.
CONFIRMED     (12)/(13) is internal to D_1; A_1 is not a disc-orbit multiplier.
CONFIRMED     (8)-(13) are per tower/per orbit type.
CONFIRMED     s=3 packing exact: Q=V_3 d_2/d_3=V_s K/d_s=u; Z packets are 0-1.
CONFIRMED     knapsack rerun: controls 336/0; rebase 1189/670/589/648;
              all-s UNB orbit 681/575; s=3 exact Z01 173/138 of 274.
CONFIRMED     D=88 exact kill in [6,16], with only orbit N={18}; not killed at N>=6.
CONFIRMED     D=105 trio survives as single NZ packets, all N=9.
CONFIRMED     D=117 Z01 exact drops 4->3; the killed row is (11)-only with value 9/7.

REFUTED       UNI as a theorem across bottom-major orbits.
REFUTED       Treating the u top-major slots as u conjugate top discs.
REFUTED       Using A_1 as part of |O|(D_1).
REFUTED       The D=105 UNI interval [6..12] after orbit closure.
REFUTED       The (84,56) M2=72 UNI value N=5 after orbit closure.

GAP           all-s UNB survivor count 575 if read as exact; it is an upper
              bound pending OPEN[NESTED-PACK].
GAP           geometric realisability of any surviving packet; left to
              OPEN[STAR-REALISABILITY] and OPEN[MOH-PROGRAM].

REPAIR        In the report, cite p.194+p.200 for unique D_{s-1}; use Lemma 6.1
              only for delta_{s-1}>=0 and coordinate normalization.
REPAIR        In knapsack.py, remove stale hard-coded /tmp/jc2-lane.GqI4QH path.
REPAIR        Label the script's printed STRICT totals as global Z01; print the
              separate 274-group s=3 subtotal explicitly.
REPAIR        Demote old UNI N-sets to HYP/RELAXED and replace promoted records
              with orbit-admissible N-sets.

PROMOTE       Claims (1),(2),(b),(d),(e) after repairs; claim (c) as measured
              plus exact only on s=3; all-s UNB only as relaxation.
NO-CLAIM      No degree ceiling; no D>100 geometric emptiness; no new exit price;
              no ledger/place identification; no nested-packing exactness at s>3.
```

<!-- BODY-END -->
