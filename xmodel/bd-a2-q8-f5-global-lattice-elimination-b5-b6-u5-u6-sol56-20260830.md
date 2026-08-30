# The q=8 singular-F5 global lattice obstruction

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra sublane `/root/u_rows_global_lattice`  
Frozen basis: `eb6c6aeea48ab76f61e606e5addc4107a840f9fb`  
Lifecycle: **EXACT PROVISIONAL GLOBAL THEOREM / UNBALANCED LOCAL INPUT AWAITS BINDING REVIEW**

## 0. Endpoint

In the charged normal, reduced, finite-near-infinity F5 quadratic-incidence
first-leg scope, the two surviving balanced q=8 rows have no global lattice
survivor:

```text
B_5/A_4,       B_6/A_5.                                (0.1)
```

This conclusion charges the already binding balanced local polar theorem.
It includes every allocation left by the Euler cap: the baseline cell, one
affine `A_1` tree, or one affine contracted `A`-null carrier.  It does not
assume chronological proximity or effectivity; the contradiction occurs in
a larger relaxed integral lattice.

Under the following exact unbalanced local input,

```text
U_5/D_5:  three reduced coefficient-one strict germs,
           A-degrees 2+3+3,
           n=e_2+e_4+e_5,  m=(2,4,5,3,3),
           three distinct physical exceptional sites;

U_6/D_6:  two reduced coefficient-one strict germs,
           A-degrees 3+5,
           n=e_2+e_4,      m=(2,4,5,6,3,3),
           two distinct physical exceptional sites,                 (0.2)
```

the two unbalanced q=8 rows also have no global lattice survivor.  The
global calculation below independently reconstructs their marked fibre
classes.  At this packet's frozen basis, however, (0.2) is an exact stated
hypothesis rather than a charged binding local artifact.  Thus the balanced
elimination in (0.1) is the unconditional endpoint of this packet; the
unbalanced elimination becomes binding only when (0.2) is independently
reviewed and integrated.

The decisive observation is non-enumerative.  If the strict ramification
primes have classes

```text
C_j=a_j S_0+2a_jF-sum_i x_(ji)P_i,
```

then the rational-forest boundary forces `C_i.C_j=0` for every pair, whereas
the exact total-transform vectors below force the sum of these intersections
to be strictly positive.  Adjunction and proximity are not needed for the
contradiction.  A complete relaxed enumeration is retained as a replay.

## 1. Charged inputs and scope

The binding inputs on the frozen basis are

```text
fdf8f476acc86e2c07fbc472771ee49358d02c87d2667f15e6b762800eed7bc6
  xmodel/bd-a2-singular-f5-local-polar-and-a6-a7-elimination-coordinator-integration-sol56-20260830.md;

a5bf78c8ab8704884e9bb3c084c88059e01ec7690c1d6f645a9e87a0aa70a884
  xmodel/bd-a2-normal-f5-decorated-carrier-effectivity-reduction-coordinator-integration-sol56-20260830.md;

f092a7152dea8bdee387825fa8181dffeb8145fc99cf65973d74f528491f57a0
  xmodel/bd-a2-a1-ruling-euler-boundary-cap-coordinator-integration-sol56-20260830.md;

6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08
  xmodel/bd-a2-rational-forest-coordinator-integration-sol56-20260830.md.
```

Use the orthogonal total-transform basis of the `S`-adapted ninefold blowup
of `F_2`:

```text
S_0^2=-2,  S_0.F=1,  F^2=0,  P_i.P_j=-delta_(ij),
A=2S_0+5F-sum_(i=1)^9P_i,
B=F,
K=-2S_0-4F+sum_iP_i,
r^*R_X=2A+B=4S_0+11F-2sum_iP_i.         (1.1)
```

For a singular q=8 marking,

```text
L=P_l,
T=S_0+2F-sum_(i in I)P_i,       |I|=4.                (1.2)
```

The remaining four indices form `O={1,...,9} minus ({l} union I)`.
All subset labels below are total-transform labels.  They do not erase
chronological proximity and do not assert that a numerical class is
effective.

## 2. Euler allocation and the forest intersection gate

The binding balanced local theorem gives three distinct global strict primes
in `B_5/A_4`, of `A`-degrees `2,3,3`, and two in `B_6/A_5`, of degrees
`2,6`.  Distinct physical sites in the connected exceptional tree force
distinct global primes: putting two germs on one irreducible global prime
would create a boundary graph cycle.

The Euler cap is

```text
rho+k<=8.                                                (2.1)
```

The local ranks and prime counts leave exactly these cells:

| row | baseline | sole possible extra carrier | sole possible extra ADE tree |
|---|---|---|---|
| `B_5/A_4` | `r_aff=0,k=3` | one `Z`, so `r_aff=0,k=4` | one affine `A_1`, so `r_aff=1,k=3` |
| `B_6/A_5` | `r_aff=0,k=2` | one `Z`, so `r_aff=0,k=3` | one affine `A_1`, so `r_aff=1,k=2` |
| `U_5/D_5` | `r_aff=0,k=3` | impossible | impossible |
| `U_6/D_6` | `r_aff=0,k=2` | impossible | impossible |

The U rows saturate (2.1), so they have no contracted carrier or affine ADE
tree; the second `A^1` ruling has base `A^1`, not `P^1`.  In each balanced
row the three displayed cells exhaust the one unit of residual Euler budget.
The local `A`-degrees already sum to eight, so an extra nonexceptional prime
must be `A`-null and hence is one of the charged contracted classes `Z`.

Every strict prime occurring here attaches at the q=8 exceptional tree.  If
two distinct strict primes met anywhere else, their intersection path and
the path already present through that connected exceptional tree would form
a cycle after a common embedded SNC resolution.  Tangency, a multiple point,
or further blowups merely subdivide the paths.  The rational-forest theorem
therefore imposes the exact necessary condition

```text
C_i.C_j=0                    for all i!=j.             (2.2)
```

This condition is on physical strict primes.  It is not inferred merely from
formal vectors or from distinct analytic factors.

## 3. Exact total classes

### 3.1 Balanced rows

For both `B_5/A_4` and `B_6/A_5`, the exceptional ramification vector equals
the exceptional infinity vector:

```text
B_5: m_R=h_H=(2,3,2,1),
B_6: m_R=h_H=(2,3,3,2,1).
```

Indeed the Cartan products are respectively `e_1+2e_2` and
`e_1+e_2+e_3`, the charged physical infinity vectors.  Hence

```text
M_0=Z_H=3F-2P_l-sum_(o in O)P_o.                       (3.1)
```

After relabelling `l=1`, `O={2,3,4,5}`, and `I={6,7,8,9}`, the baseline
strict total is

```text
C^(0)=r^*R_X-M_0
     =4S_0+8F-sum_i c_iP_i,
c=(0,1,1,1,1,2,2,2,2),
sum c_i=12,                  sum c_i^2=20.             (3.2)
```

It has zero intersection with `S_0,L,T`.  Since every strict prime is a
distinct effective curve from each of those three components, nonnegativity
of local intersections forces every individual strict prime to be disjoint
from all three.

An effective q=8 contracted carrier has

```text
Z_J=S_0+2F-sum_(j in J)P_j,
l notin J,       |J cap I|=2,       |J cap O|=3.       (3.3)
```

There are `binom(4,2)binom(4,3)=24` labelled candidates.  Subtracting one
such carrier leaves

```text
C^(Z)=3S_0+6F-sum_i c_i^(Z)P_i,
multiset(c^(Z))=(0,0,0,0,1,1,1,2,2),
sum c_i^(Z)=7,              sum (c_i^(Z))^2=11.        (3.4)
```

For `B_5`, positivity of the three strict `B`-degrees already forces the
Cartier coefficient of `Z` to be one.  For `B_6`, coefficient two is allowed
by the coarse `B` budget but impossible in (3.2): every `J` contains three
`O` coordinates with baseline value one, so subtracting `2Z_J` makes those
strict multiplicities negative.  Thus (3.4) is the only carrier cell in
either row.

Now let an affine `A_1` exceptional curve have class `Q=P_i-P_j`.  This is
the general square-`-2` integral root in the orthogonal `P` lattice with
`A.Q=B.Q=K.Q=0`.
It cannot use `l`, and disjointness from `T` requires `i,j` both in `I` or
both in `O`.  If its ramification coefficient is `mu`, subtracting `mu Q`
changes

```text
c_i -> c_i+mu,        c_j -> c_j-mu.                   (3.5)
```

For `mu=1`, either orbit has `sum c=12` and `sum c^2=22`.  Nonnegativity
allows `mu=2` only when both indices lie in `I`; then `sum c=12` and
`sum c^2=28`.  No `mu>=3` is possible.  Thus the replay covers not only the
simple affine-root cell but also the only possible higher exceptional
coefficient left by the total class.

### 3.2 Unbalanced rows

Number a `D_s` tree as the chain `R_1--...--R_(s-2)` with spins
`R_(s-1),R_s`, and retain the spin met by `S`.  Reversing the contractions of
the charged `U_s` fibre gives the exact chronological classes

```text
R_s       =F-P_1-P_2,          retained spin,
R_(s-1)   =P_1-P_2,            other spin,
R_(s-2)   =P_2-P_3,
...
R_1       =P_(s-1)-P_s,
L         =P_s.                                          (3.6)
```

For `U_5/D_5`, both H sections meet the retained spin at distinct points, so
`I={6,7,8,9}`.  The conditional vector in (0.2) gives

```text
M_5=2R_1+4R_2+5R_3+3R_4+3R_5
   =3F-P_2-P_3-2P_4-2P_5,

C_5=r^*R_X-M_5
   =4S_0+8F-sum_i c_iP_i,
c=(2,1,1,0,0,2,2,2,2),
sum c_i=12,                  sum c_i^2=22.             (3.7)
```

For `U_6/D_6`, `T` meets the other spin.  The first inverse blowup is at
`T cap F`, the second is at the two-spin fibre node and misses `T`, and the
three remaining non-q=8 centres lie on `T`.  Hence
`I={1,7,8,9}`.  The conditional vector gives

```text
M_6=2R_1+4R_2+5R_3+6R_4+3R_5+3R_6
   =3F-P_3-P_4-2P_5-2P_6,

C_6=r^*R_X-M_6
   =4S_0+8F-sum_i c_iP_i,
c=(2,2,1,1,0,0,2,2,2),
sum c_i=12,                  sum c_i^2=22.             (3.8)
```

Both totals have zero intersection with `S_0,L,T`, so every strict prime is
individually disjoint from the strict H components.  The earlier speculative
`D_5` vector `e_1+2e_5` is not used: it arose from confusing ordinary chart
order with surface order at the first generic exceptional.  The exact
conditional row in this packet is only `e_2+e_4+e_5`.

The balanced totals after subtracting either `Z_J` or an affine root likewise
remain disjoint from `S_0,L,T`, because those subtracted curves are themselves
disjoint from H.  Thus the form (4.2) applies in every cell, not just the
baseline rows.

## 4. The uniform positive-intersection identity

Write any strict prime as

```text
C_j=a_jS_0+b_jF-sum_i x_(ji)P_i.                       (4.1)
```

It is horizontal: `a_j=B.C_j>0`.  Otherwise it would be a component of the
same marked q-fibre as its local germ, but that complete `B_s/U_s` fibre has
only `L` and its displayed exceptional root tree; the strict polar is neither.
Because `C_j.S_0=0`,

```text
b_j=2a_j.                                               (4.2)
```

The total-transform multiplicities `x_(ji)` are nonnegative integers.  They
obey further proximity inequalities, but omitting those inequalities only
enlarges the candidate set.  If `d_j=A.C_j`, then

```text
sum_i x_(ji)=5a_j-d_j,
delta(C_j)=1+(2a_j^2-sum_i x_(ji)^2+a_j-d_j)/2>=0,     (4.3)

C_j.C_k=2a_ja_k-sum_i x_(ji)x_(ki).                    (4.4)
```

The delta statement follows from the rational normalization supplied by the
forest theorem.  It is replayed but not needed below.

Put `c_i=sum_j x_(ji)` and `Q=sum_(j,i)x_(ji)^2`.  Summing (4.4) gives the
exact identity

```text
sum_(j<k) C_j.C_k
 =2sum_(j<k)a_ja_k-(sum_i c_i^2-Q)/2.                  (4.5)
```

Since every `x_(ji)` is a nonnegative integer,

```text
Q>=sum_(j,i)x_(ji)=sum_i c_i.                          (4.6)
```

Equations (4.5)--(4.6) yield the following strict lower bounds in every
cell.  The displayed bound is deliberately the uniform closed-form bound;
the enumeration is often sharper.

| row/cell | strict `B`-degrees | `sum c`, `sum c^2` | lower bound for `sum_(j<k)C_j.C_k` |
|---|---|---|---:|
| `B_5` baseline | permutation of `(2,1,1)` | `12,20` | `6` |
| `B_6` baseline | positive pair summing `4` | `12,20` | `2` |
| `B_5` one `Z` | `(1,1,1)` | `7,11` | `4` |
| `B_6` one `Z` | permutation of `(1,2)` | `7,11` | `2` |
| `B_5` simple affine `A_1` | permutation of `(2,1,1)` | `12,22` | `5` |
| `B_6` simple affine `A_1` | positive pair summing `4` | `12,22` | `1` |
| `B_5`, affine coefficient `mu=2` | permutation of `(2,1,1)` | `12,28` | `2` |
| `U_5/D_5` | permutation of `(2,1,1)` | `12,22` | `5` |
| `U_6/D_6` | positive pair summing `4` | `12,22` | `1` |

Only `B_6` with affine coefficient `mu=2` needs a refinement.  Its shifted
`I`-coordinates are `(4,0,2,2)` and its four `O`-coordinates are all one.
If the degree-two prime has `B`-degree one, (4.3) and `T`-disjointness give
`I`-multiplicity two and `O`-multiplicity one; the `O` coordinates contribute
zero to the mutual dot product, and the `I` contribution is at most four.
Thus the intersection is at least `6-4=2`.  If its `B`-degree is two, the
corresponding sums are four and four; the `I` dot product is at most six, so
the intersection is at least `8-6=2`.  Degree three is incompatible with the
nonnegative `O` sum.  Hence this last cell also has positive intersection.

Every row contradicts the forest requirement (2.2).  This proves the stated
global eliminations before chronological proximity, analytic effectivity, or
adjunction can remove any further candidates.

## 5. Exact replay

The standard-library replay

```text
ef689257528b850ea1c504f429eac78e2d5339f4f45ad783d6b85189fd9acd0c
ops/q8_f5_global_lattice_replay.py
```

checks the four Cartan products, reconstructs (3.7)--(3.8) from the ordinary
blowup sequence, checks the balanced class, generates all 24 labelled q=8
`Z` candidates and all labelled members of both affine-root orbits, and then
exhausts one representative of each exact coordinate-permutation orbit.
Every coordinatewise nonnegative split satisfies the imposed degree,
`S/T/L`-disjointness, and `delta>=0` tests.  Degree-three branches are
labelled, and affine-root counts are per oriented root.  Chronological
proximity is intentionally omitted, so a zero count is a safe elimination.

| replay cell | linear splits | adjunction-valid | pairwise-disjoint |
|---|---:|---:|---:|
| `B_5` baseline | 648 | 270 | 0 |
| `B_6` baseline | 59 | 37 | 0 |
| `U_5/D_5` exact H-disjoint cell | 504 | 90 | 0 |
| `U_6/D_6` | 67 | 21 | 0 |
| `B_5` one simple `Z`, per candidate | 33 | 15 | 0 |
| `B_6` one simple `Z`, per candidate | 8 | 5 | 0 |
| `B_5` simple affine root in `O`, per oriented root | 504 | 90 | 0 |
| `B_5` simple affine root in `I`, per oriented root | 513 | 162 | 0 |
| `B_6` simple affine root in `O`, per oriented root | 49 | 19 | 0 |
| `B_6` simple affine root in `I`, per oriented root | 52 | 30 | 0 |
| `B_5` coefficient-two affine root, per oriented root | 234 | 18 | 0 |
| `B_6` coefficient-two affine root, per oriented root | 33 | 9 | 0 |

As a diagnostic, omitting `T`-disjointness from `U_5/D_5` leaves 2,860
linear and 370 adjunction-valid labelled splits, still with zero
pairwise-disjoint survivors.  The exact 90 count above restores the full H
condition.  The replay uses explicit `require`/`RuntimeError` checks rather
than Python `assert`, and includes a forged-one-survivor negative control
that must be rejected in ordinary, `-O`, and `-OO` modes.

All three modes emit the identical deterministic JSON digest
`dcfbe164178ea93e85c608526edb588ea96aaf6d6488c3865660c708b79f3da7`.

The replay is arithmetic evidence only.  It does not establish the analytic
local factorizations, physical sites, effectivity of a root or `Z`, or the
existence of any incidence surface.

## 6. Maximum theorem and firewall

Promoted provisionally by this packet:

```text
binding balanced local input
  => B_5/A_4 and B_6/A_5 have no global q=8 survivor;

exact unbalanced input (0.2)
  => U_5/D_5 and U_6/D_6 have no global q=8 survivor.  (6.1)
```

Together with the already binding deaths of `B_7/A_6`, `B_8/A_7`, and
`B_9/A_8`, (6.1) conditionally empties the entire singular q=8 F5 table.  The
word “conditionally” remains mandatory until the unbalanced full-family
local packet and this global packet receive the campaign's independent
review/integration gate.

The theorem does not eliminate the q=6 rows `B_3/A_2` or `U_3/A_3`, a smooth
F5 row, nonreduced infinity, projective nonfiniteness, degree drop, a change
of trace-zero presentation, or a higher-degree block.  It proves no
realization, no polynomial map, no counterexample, and no JC2 conclusion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15844`.
- Body SHA-256:
  `cf89570ab34aab91d8e317335fe0fc1768bf74d0d42ec60df6ae875fb861b64e`.
- Frozen basis: `eb6c6aeea48ab76f61e606e5addc4107a840f9fb`.
