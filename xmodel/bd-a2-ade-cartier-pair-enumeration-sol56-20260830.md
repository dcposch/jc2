# Capped `A_r`/`D_r` Cartier pairs and physical-germ partitions

Date: 2026-08-30 UTC  
Producer: Sol 5.6 delegated lane `/root/quadratic-degeneracy-frontier`  
Frozen basis: `986427df23c30375b6edfd659ba8a6c6139434ab`  
Lifecycle: **EXACT PROVISIONAL FINITE SUCCESSOR / GLOBAL EFFECTIVITY OPEN**

## 0. Endpoint and charged input

This is the smallest finite successor to

```text
ab10ea83f443c93bdb87194ad0e42fe2c442984ba821c3ddf8ddf5cc3f796133
  xmodel/bd-a2-ade-decorated-boundary-different-threat-map-sol56-20260830.md
```

and imports its notation and only its proved caps.  At one Du Val point let
`E_1,...,E_r` be a connected exceptional tree, let `C` be its positive
Cartan matrix, and write

```text
R = R_str + sum_i m_i E_i,       m_i in Z_(>0),
n_i = R_str.E_i,                 n=Cm in Z_(>=0)^r.          (0.1)
```

The charged predecessor proves that the only connected types eligible in
the explicit `D9(-1)` marking are

```text
A_1,...,A_8,             D_4,...,D_9.                       (0.2)
```

It also proves `sum n_i<=8` after choosing a proper target-line slice
through the singular image, avoiding ramification components.  The sharper
`sum n_i<=4` is used here only on the separately conditional stratum where
the corresponding `B`-fibre meets the different properly.

Every count below concerns **one connected local exceptional component of
one fixed type at a time**; the totals are the disjoint sum over the fourteen
types in (0.2).  They do not enumerate disconnected ADE multisets,
simultaneous embedding orbits in `D9(-1)`, allocation of one global slice
budget among several singular points, the paired infinity vectors `(h,a)`,
or labels grouping germs into global carriers.  In this precise sense the
artifact is a complete local table, not the full global successor.

> **CAPPED-CARTIER-PAIR THEOREM.**  For the types (0.2):
>
> 1. There are exactly `16,360` labelled pairs `(m,n)` satisfying (0.1) and
>    `1<=sum n_i<=8`.  Up to the unlabelled Dynkin-diagram symmetry there
>    are `12,238` canonical pairs.  Under the conditional cap four the
>    respective counts are `772` and `646`.
> 2. The nonnegative vector `n` is the unique dominant member of the Weyl
>    orbit of the root-lattice element `sum m_i alpha_i`; consequently no
>    two distinct listed dominant vectors are Weyl-related.  No geometric
>    Weyl quotient is performed.  For unlabelled local-graph bookkeeping,
>    the list is canonicalized only by diagram automorphisms:
>    chain reversal for `A_r`, the spin-node transposition for `D_r`, `r>=5`,
>    and the full `S_3` triality on the three arms of `D_4`.  Every record
>    retains its diagram-orbit and stabilizer sizes, so the labelled list is
>    recoverable.
> 3. A strict-transform branch germ contributes either `k e_i` at a smooth
>    point of `E_i`, or `u e_i+v e_j` at the physical node `E_i intersect E_j`,
>    where `i--j` is one Dynkin edge and all displayed coefficients are
>    positive.  The data gives the exact generating-function count of
>    unordered numerical germ-signature partitions of every canonical
>    `n`, including the minimum and maximum possible numbers of germs and
>    the exact one-germ descriptor when it exists.  It does not identify an
>    entry of `n` with a germ, nor a germ with a distinct physical point.
> 4. Local Cartan arithmetic, diagram bookkeeping, and an unlabelled local
>    forest test by themselves eliminate no enumerated pair: every `n` has
>    a unit-atom decomposition whose abstract dual graph can be drawn with
>    separate outside leaves.  This is not an analytic realizability claim.
>    If one separately proves, on one common SNC resolution, that the actual
>    distinct branch germs give distinct attachment paths and their outside
>    reduced transforms form one connected subgraph, then at most one germ
>    is possible.  In that conditional stratum the absence of a one-atom
>    partition is an exact contradiction, and the cap-eight list falls
>    exactly to `718` labelled pairs or `563` diagram orbits, excluding
>    `15,642` and `11,675`;
>    cap four falls to `198` labelled pairs or `163` orbits, excluding `574`
>    and `483`.

The word “pair” throughout is local numerical Cartier data.  A survivor is
not an assertion that the ADE curves occur effectively in the global
`D9(-1)` marking, that several local configurations embed simultaneously,
or that a bidegree-`(2,3)` incidence equation realizes the divisor.

## 1. Exact finite enumeration

Put `w(n)=sum_i n_i`.  Since the inverse of a connected finite ADE Cartan
matrix is entrywise strictly positive, every nonzero `n>=0` has
`C^(-1)n>0` over the rationals.  Thus

```text
{m in Z_(>0)^r : Cm>=0 and w(Cm)<=c}
  <--> {n in Z_(>=0)^r - {0} : n in C Z^r and w(n)<=c},       (1.1)
```

with `m=C^(-1)n`.  There is no hidden positivity test after integrality.

For `A_r`, numbered `1--...--r`, integrality is exactly

```text
sum_(i=1)^r i n_i = 0 mod (r+1),                            (1.2)
```

and the inverse used in the enumeration is

```text
m_j = ((r+1-j) sum_(i<=j) i n_i
       + j sum_(i>j) (r+1-i)n_i)/(r+1).                     (1.3)
```

For `D_r`, use the chain `1--...--(r-2)` with fork vertices `r-1,r`
attached to `r-2`.  Set

```text
a=n_(r-1),       b=n_r,       T=sum_(i=1)^(r-2) i n_i.
```

Integrality is exactly

```text
a=b mod 2,       2T+(r-2)a+r b=0 mod 4,                     (1.4)
```

and the inverse is

```text
m_j       = sum_(i=1)^(r-2) min(i,j)n_i + j(a+b)/2,
                                                   1<=j<=r-2,
m_(r-1)   = (2T+r a+(r-2)b)/4,
m_r       = (2T+(r-2)a+r b)/4.                              (1.5)
```

Equations (1.2)--(1.5) make the enumeration literal: list every weak
composition `n` of each weight `1,...,8`, retain precisely the vectors
satisfying (1.2) or (1.4), compute `m`, and verify `Cm=n`.  This considers
all `72,695` nonzero capped vectors before the congruence filters.  An
independent `fractions.Fraction` Gaussian solve of all `72,695` candidates
agreed with the closed formulas and their integrality decisions.

Accordingly, local Cartier integrality itself rules out exactly `56,335` of
the `72,695` cap-eight candidate vectors and `2,446` of the `3,218` cap-four
candidates, leaving `16,360` and `772`.  Diagram canonicalization then
identifies `4,122` and `126` duplicate labelled images, respectively; that
identification is bookkeeping, not a geometric contradiction.  Section 4
states the only forest cut justified by the information retained here.

The exact counts are below.  `raw/can` means labelled pairs divided by
unlabelled diagram orbits.  The histogram `g:k` means that `k` canonical
orbits have minimum numerical germ count `g`.

| type | cap 8 raw/can | cap 8 canonical minimum-germ histogram | cap 4 raw/can | cap 4 canonical minimum-germ histogram |
|---|---:|---|---:|---|
| `A1` | 4 / 4 | `1:4` | 2 / 2 | `1:2` |
| `A2` | 14 / 9 | `1:9` | 4 / 3 | `1:3` |
| `A3` | 42 / 28 | `1:12, 2:16` | 9 / 7 | `1:4, 2:3` |
| `A4` | 98 / 56 | `1:13, 2:43` | 13 / 9 | `1:4, 2:5` |
| `A5` | 216 / 125 | `1:14, 2:85, 3:26` | 21 / 15 | `1:4, 2:10, 3:1` |
| `A6` | 428 / 231 | `1:15, 2:124, 3:92` | 29 / 19 | `1:4, 2:13, 3:2` |
| `A7` | 809 / 439 | `1:16, 2:174, 3:220, 4:29` | 42 / 28 | `1:4, 2:19, 3:4, 4:1` |
| `A8` | 1,429 / 749 | `1:16, 2:218, 3:407, 4:108` | 54 / 34 | `1:4, 2:22, 3:7, 4:1` |
| `D4` | 134 / 52 | `1:24, 2:10, 3:18` | 21 / 11 | `1:8, 2:1, 3:2` |
| `D5` | 336 / 245 | `1:48, 2:116, 3:81` | 35 / 30 | `1:14, 2:12, 3:4` |
| `D6` | 811 / 605 | `1:76, 2:298, 3:183, 4:48` | 64 / 54 | `1:22, 2:25, 3:7` |
| `D7` | 1,733 / 1,349 | `1:84, 2:600, 3:473, 4:192` | 98 / 88 | `1:24, 2:50, 3:12, 4:2` |
| `D8` | 3,549 / 2,821 | `1:112, 2:992, 3:1,223, 4:443, 5:51` | 156 / 139 | `1:32, 2:78, 3:27, 4:2` |
| `D9` | 6,757 / 5,525 | `1:120, 2:1,504, 3:2,589, 4:1,095, 5:217` | 224 / 207 | `1:34, 2:118, 3:48, 4:7` |
| **all** | **16,360 / 12,238** | **`1:563, 2:4,180, 3:5,312, 4:1,915, 5:268`** | **772 / 646** | **`1:163, 2:356, 3:114, 4:13`** |

The cap-four set is exactly the `w(n)<=4` subset of the cap-eight data; it
is not a second enumeration and it is not asserted when the `B`-fibre is a
component of the different.

## 2. Weyl separation and diagram bookkeeping

Let

```text
lambda=sum_i m_i alpha_i.
```

In the simply-laced normalization,

```text
(lambda,alpha_i)=n_i.                                 (2.1)
```

Thus `n>=0` says exactly that `lambda` lies in the closed dominant chamber.
Every finite Weyl orbit meets that chamber in exactly one point, so no two
distinct enumerated dominant vectors belong to the same Weyl orbit.  This
is only a separation observation: the program does not apply Weyl
reflections, and neither positivity of the displayed simple-root
coefficients `m` nor carrier data is transported through a Weyl action.
In particular, no reflection is asserted to come from an automorphism or
an allowed change of marking of the resolved incidence surface.

The remaining unlabelled graph groups are

```text
A1:             trivial,
A_r, r>=2:      C2, reversing the chain,
D4:             S3, permuting arms 1,3,4 and fixing vertex 2,
D_r, r>=5:      C2, swapping fork vertices r-1,r.       (2.2)
```

The program applies (2.2) simultaneously to `m` and `n`, selects the
lexicographically least `n`, and records the orbit size and stabilizer
order.  Because `C` commutes with every diagram automorphism,
`C^(-1)(g n)=g m`; hence canonicalizing `n` canonicalizes the pair.

Diagram quotienting is deliberately only an unlabelled-local convention.
An ambient `D9(-1)` marking, another divisor, or the global fibration may
distinguish diagram-related vertices.  In that situation the stored orbit
size and the explicit group permutations recover all labelled images; no
global orbit-transitivity claim is being made.

## 3. Physical-germ signatures, not coordinate support

On the smooth minimal resolution, the exceptional divisor is SNC.  One
analytic branch germ of the strict transform, not contained in it, has one
centre on the exceptional locus.  Its numerical contact vector is therefore
precisely one of

```text
k e_i,                         k>=1,                 (3.1)
u e_i+v e_j,                   u,v>=1, i--j an edge. (3.2)
```

Formula (3.1) is contact at a smooth point of `E_i`; (3.2) is one branch at
the node `E_i intersect E_j`.  In local SNC coordinates these are the two
possible locations.  Conversely, every numerical signature in (3.1) is represented
by a smooth tangent germ, and every positive pair in (3.2) by an
irreducible plane branch after adding a sufficiently high primitive term if
the two leading orders have a common divisor.  This local observation does
not say that an arbitrarily chosen collection descends to the charged
Cartier divisor or occurs in an incidence equation.  A globally irreducible
carrier may have several analytic branches over the singular point and may
therefore contribute a sum of several atoms.

Let `A_G` be the set of atoms (3.1)--(3.2) of weight at most eight.  The
finite program computes

```text
P_G(x_1,...,x_r;t)
  = product_(a in A_G) (1-t*x^a)^(-1),               (3.3)
```

truncated to total `x`-weight eight.  The coefficient of `x^n t^g` is the
number of unordered multisets of numerical germ signatures with total `n`
and `g` germs.  Each canonical record contains this whole coefficient
vector, its sum, and its least and greatest nonzero degrees.

Three distinctions are essential.

* The coordinate `n_i` is an intersection multiplicity, not a number of
  germs.  For example, `u e_i+v e_j` can be one germ at one ADE node.
* A germ is not automatically a distinct physical point.  Several germs
  can share a smooth point, and all edge germs for the same edge begin at
  its unique node.  Separating them can require further blowups.
* The partitions in (3.3) are numerical germ-signature partitions.  They
  do not count analytic moduli or locations, do not group germs into global
  carrier curves, and are not quotiented by the stabilizer of the chosen
  diagram representative.

Every `n` has the unit-vertex partition consisting of `n_i` copies of
`e_i`.  Consequently the maximum possible germ number is `w(n)`, with
coefficient one.  A one-germ partition exists exactly when `n` itself has
support on one vertex, or on both endpoints of one edge and nowhere else.
The congruence (1.2) or (1.4) still applies to the total `n`; an individual
branch need not separately be a Cartier divisor downstairs.

## 4. The exact forest cut, and why it is conditional

Let `T_E` denote the connected exceptional ADE tree in a fully resolved SNC
boundary.  Any actual strict divisor supplies a collection of analytic
branches, and their contact vectors give one of the partitions counted by
(3.3).  Thus the computed minimum is a rigorous lower bound for the number
of actual branches, although the converse realization of every counted
partition is not claimed.  After the additional point blowups needed to
separate tangencies or branches, distinct branches have distinct final
attachment edges; several branches may have shared a physical crossing and
an initial infinitely-near path before that separation.

First suppose nothing is known about how the germs group into outside
carriers.  For any enumerated `n`, its unit-vertex partition can be drawn as
an abstract graph by assigning every atom a separate outside leaf.  The
resulting graph is a tree: it is `T_E` with leaf paths attached.  This
drawing does not construct simultaneous analytic branches or a Cartier
equation; it proves only that the unlabelled numerical forest test contains
no contradiction.  Hence neither a large coefficient, support on several
Dynkin vertices, nor minimum germ
count greater than one is by itself a forest contradiction.  This proves
the exact negative result:

```text
local Cartan pair + cap + forest, without carrier data,
rules out zero of the 16,360 cap-eight pairs.          (4.1)
```

Now add the genuinely stronger hypothesis that on one common embedded SNC
resolution: (i) the inner graph consisting of `T_E` and any shared
infinitely-near attachment trunks is connected; (ii) the reduced strict
transforms of all relevant outside carriers form one connected subgraph
disjoint from that inner graph before final attachments; and (iii) distinct
analytic branches give distinct final joining edges.  Two such edges
between these connected subgraphs make a cycle.  There can therefore be at
most one analytic branch, so `n` must itself be an atom (3.1) or (3.2).

This conditional cut is exact on the finite numerical list:

| cap | raw all | raw one-germ | raw excluded | canonical all | canonical one-germ | canonical excluded |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 16,360 | 718 | 15,642 | 12,238 | 563 | 11,675 |
| 4, conditional | 772 | 198 | 574 | 646 | 163 | 483 |

The table is not licensed merely because `R_str` is effective, because its
support is connected downstairs, or because several numerical atoms begin
at the same physical crossing.  One must establish the stated connected
resolved outside subgraph and the separated final joining edges.  Nor
does “one germ” mean “one Dynkin vertex”: an edge atom is one physical germ
with two positive coordinates.  Conversely, an allowed one-germ signature
remains only a necessary local pattern until global effectivity is proved.

## 5. Reproducible artifact and internal controls

The complete canonical list in the one-connected-local-component scope is
the deterministic compressed artifact

```text
xmodel/bd-a2-ade-cartier-pairs-cap8-sol56-20260830.json.gz
```

with

```text
gzip artifact bytes:          174608
gzip artifact SHA-256:        bfbd89d61d1181bc0bdb9a243c8d3b85074541194621eb57047af9ecf884e279
canonical JSON bytes:         3762426
canonical JSON SHA-256:       11ca074c9a4bc6656960222897d8c674f8486970b7a20cb1975cfcdb818d1d19
compression:                  gzip level 9, mtime 0
schema:                       jc2.ade_cartan_pairs.v1
```

It is generated by the seconds-scale, Python-standard-library-only script

```text
ops/ade_cartan_pair_enumerate.py
SHA-256: d79fd1c484f229a0d564f537e29a31de6b86c97250db7649a6edf2de34ee8a94
```

The ordinary generation command is

```text
python3 ops/ade_cartan_pair_enumerate.py \
  --output xmodel/bd-a2-ade-cartier-pairs-cap8-sol56-20260830.json.gz
```

Each type record stores its Cartan matrix, Dynkin edges, diagram group and
permutations, summary counts, and canonical pairs.  Each pair record stores
`m`, `n`, weight, cap-four membership, diagram orbit/stabilizer sizes, and
the physical-germ polynomial data.  Labelled pairs are recovered by applying
the stored diagram permutations.

The script asserts `Cm=n`, positivity, orbit-size recovery of every raw
count, cap nesting, and elementary germ-polynomial controls.  Its optional
`--deep-check` path uses an independent exact Gaussian elimination over
`fractions.Fraction` on all `72,695` candidate vectors; this audit was run
successfully.  No floating-point arithmetic, random sampling, CAS, or
external package enters either generation or checking.

## 6. Attacks and scope firewall

The following tempting strengthenings are not conclusions of this packet.

1. **No formal-to-effective jump.**  A canonical pair does not prove an
   effective configuration of exceptional curves in the fixed global
   `D9(-1)` marking.  The standard local `A_r` or `D_r` diagram is not a
   proof that the corresponding root sublattice occurs effectively.
2. **No simultaneous-embedding claim.**  Lists for different singular
   points cannot be combined by rank alone.  Their embeddings, orthogonal
   complements, divisor classes, and total slice budget must be checked
   simultaneously.  The displayed all-type totals are a disjoint sum, not
   a count of exceptional multisets or Weyl(`D9`) embedding orbits.
3. **No ambient symmetry claim.**  Weyl dominance and unlabelled diagram
   symmetry are local root-system bookkeeping.  The ambient fibration may
   distinguish every diagram-related record.
4. **No coordinate/germ/point conflation.**  `n_i`, analytic branch germs,
   resolved joining paths, and physical attachment points are four
   different notions.  Section 3 records exactly which level the data sees.
5. **No unconditional cap four.**  The `B`-fibre bound is discarded when
   the fibre is a component of the different or proper intersection is not
   proved.  Likewise the cap-eight enumeration does not cover a target-line
   common-carrier stratum where the charged proper-slice hypothesis fails.
6. **No automatic connected-carrier cut.**  The exclusions in Section 4
   require the stated outside-carrier connectivity.  Without it, separate
   leaf carriers defeat the cycle argument.
7. **No converse incidence realization.**  The numerical germ partitions
   do not construct a local hypersurface equation, a global divisor in
   class `2A+B`, or a bidegree-`(2,3)` incidence surface.
8. **No paired-boundary or carrier labelling.**  The infinity data
   `a=Ch` and its compatibility with `(m,n)` are not enumerated.  Nor does
   the artifact say which numerical germs belong to the same strict
   different or infinity component; that missing labelling is exactly what
   controls the conditional forest cut.

Disconnected ADE configurations, nonnormal incidence closures, nonproper
slice/common-component strata, and the already excluded `A9,E6,E7,E8`
types are outside this enumeration.  The first exact remaining bridge is to
derive the carrier partition and global divisor classes of the actual
strict different, then intersect the surviving one-germ records with
simultaneous effective embeddings in the explicit `D9(-1)` marking.  Until
that bridge is proved, this packet is a finite threat map, not a singular
stratum elimination theorem.

No shared ledger was edited.  No staging, commit, AWS job, heavy local CAS,
Singular operation, or `jc2-lean` access was used.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20023`.
- Body SHA-256:
  `002ce81b56f2d703766db0e5a52696a8537be5cee52c2730d3832eaa6d1f85dc`.
- Frozen basis: `986427df23c30375b6edfd659ba8a6c6139434ab`.
