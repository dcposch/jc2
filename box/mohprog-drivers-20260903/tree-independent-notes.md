# Independent FULL-TREE-PARTITION audit

Scope: source-first derivation and a clean implementation independent of
`full_tree_partition.py` / `candidate_eval.py`.  The implementation is
`tree-independent.py`.  It imports only the frozen `(1)`--`(13)` enumerator.

## Typed result

`FULL-TREE-PARTITION = SOURCE-DERIVED-NECESSARY, BUT NOT THE MISSING MOH
PROGRAM FILTER.`

With the polynomial-prefix interpretation of Proposition 5.4, it maps the 658
printed-list rows at `n <= 100` to **23 rows in 15 groups**.  It keeps all six
printed rows but leaves **17 excess rows**, so it does not meet the required
`658 -> 6` discriminator.  Adding the local Proposition A.3 nondegeneracy and
the cyclic-quotient passport maps the same input to **20 rows in 12 groups**:
all six printed rows and **14 excess rows**.  Consequently neither candidate
can be typed `PROVED-IN-SOURCE` as *the* omitted program elimination.

The weaker interpretation in which any nonzero factor immediately makes a
branch safe from Proposition 5.6 leaves 60 rows.  Proposition 5.4 shows why
that reading is too weak: a nonzero coefficient at an integral exponent is a
term of the removable polynomial prefix `h(x)`.

## Source derivation

I read the page images, not just the broken text layer.  The required pieces
are as follows.

- Proposition 4.6, pp.170--171, says that at a splitting node the relevant
  leading coefficients are powers of a common polynomial `p`, that `q` is
  square-free, every root of `p` is a root of `q`, and `p` is not a power of
  `q`.
- Definition 5.1, p.179, gives the major threshold and the radius formula.
  Proposition 5.3, p.180 (statement) and pp.181--183 (proof), applies to *any*
  factor `pi-c_r` of `p` whose multiplicity is above the displayed average;
  such a factor extends the tower one level.
- Proposition 5.4, pp.183--185, explicitly turns an integer-exponent prefix
  into a polynomial `h(x)` and removes it by a polynomial automorphism.  Thus
  a nonzero coefficient at `delta_j=0` does not by itself defeat Proposition
  5.6.
- Proposition 5.6 is stated at p.188 and proved at p.189: a tower ending in a
  pure `pi t^{delta_1}` root contradicts degree minimality.
- The summary theorem, p.200, clauses (4)--(5), says every above-average
  subdisc extends and every at-or-below-average one is minor; clause (7)
  requires at least one above-average subdisc.
- The root-of-unity automorphism immediately before printed (10)--(11),
  p.201, supplies the `A_j`-orbits of nonzero factors and the distinguished
  zero factor.
- Proposition A.3, p.205, supplies the differential equation and the
  above-average root.  Its displayed proof also supplies the local
  nondegeneracy used below.

Fix a node at level `j` and the already selected values
`V_{j+1},...,V_s`.  Put

```
P = V_{j+1} d_j / d_{j+1},
Q = V_{j+1} (n-M_j) / d_{j+1},
h = d_j/(n-M_j),
A = A_j.
```

Here `P=deg p`, `Q=deg q`, and `h=P/Q`.  If `b` is the multiplicity of the
fixed factor `pi`, and the nonzero `A`-orbits have per-root multiplicities
`v_1,...,v_k`, source necessity gives

```
P = b + A(v_1+...+v_k),
A k + 1_{b>0} <= Q,
v_l >= 1, b >= 0.
```

Every `v_l>h` and, when applicable, `b>h` is a major child.  Proposition 5.3
requires **every** such child to admit a valid subtree with the same remaining
characteristic levels.  Values at or below `h` are minor and stop.  At least
one child must be major.  At `j=2`, every major child must pass printed
(12)/(13).  A chain which remains polynomial-removable through `j=2` is
rejected by Proposition 5.6.  The selected census path must occur as one of
the zero/nonzero children at every level; merely finding some other valid path
is insufficient.

The top node is handled by Lemma 5.3 (pp.185--186): `p` has two roots, the
selected multiplicity satisfies `d_s>V_s>d_s/2`, and the complement is minor.
The selected top root is normalized to zero, so the initial prefix is marked
removable/dangerous.

This is an exact finite dynamic program.  Its state records the level, the
higher `V` values, and whether the selected prefix is still removable.  For
each congruent `b` it solves a bounded unbounded-knapsack problem in the
nonzero orbit multiplicities, recursively validating every major value.  No
cap, random search, or floating-point comparison is used.

## The `(75,50)` discriminator

All full-list rows at `(75,50)` have `V_3=4`, hence at `j=2`, `P=20`.

- For `M_2=55`, `A_2=5`, `Q=16`, and `h=5/4`.  The printed `V_2=2` path
  embeds in the zero-free partition `[2,1,1]`; the printed `V_2=3` path embeds
  in `[3,1]`.  The `1` factors are minor, and both selected major factors pass
  (12)/(13).  These are precisely the two rows retained.
- For `M_2=5`, `A_2=55>P`, so the entire degree is forced into the zero factor
  `b=20`; it is major and gives a forbidden pure chain.
- For `M_2=10`, `A_2=17`, every partition has a positive zero multiplicity
  (for example `b=3` plus one nonzero orbit of multiplicity one).  Since
  `h<1`, that zero factor is major and forbidden.
- For `M_2=40`, `A_2=9` and `P` is not divisible by `A_2`; again every
  partition has a positive major zero factor.
- For `M_2=60`, `A_2=11` and the same obstruction holds.

Thus this candidate independently achieves the requested local cut
`M_2 in {5,10,40,60}` while retaining `(M_2,V_2)=(55,2),(55,3)`.

## `n <= 100` census and independent identity control

The polynomial-prefix whole-tree survivor rows are the six printed rows plus:

- `(84,56; M=[70,77,82]; V={2:5,3:10,4:5})`;
- `(90,60; M=[10,45,88]; V={2:1,3:8,4:4})` and its `V_2=3` alternate;
- `(90,60; M=[45,80,88]; V={2:2,3:5,4:4})` and its `V_2=3` alternate;
- `(96,72; M=[-60,56,94]; V={2:1,3:9,4:3})`;
- `(96,72; M=[36,80,94]; V_2=1 or 4,V_3=9,V_4=3)`;
- `(96,72; M=[84,88,94]; V={2:3,3:9,4:3})`;
- `(96,72; M=[36,78,94]; V_2=1 with V_3=1, or V_2=1/4 with V_3=3,
  V_4=5)` (three rows total);
- `(96,64; M=[48,68,94]; (V_2,V_3,V_4)=(2,1,3),(1,2,3),(3,2,3))`;
- `(96,64; M=[-48,-8,20,94]; V={2:1,3:1,4:6,5:3})`;
- `(96,64; M=[80,88,92,94]; V={2:5,3:10,4:5,5:3})`.

This implementation and the independently written primary implementation
agree row-for-row.  Sorted survivor-key files have the common SHA-256

```
f7e9fb5c698da06e949296afca9d77cf5534d400e7ad328d573f315674b0a7fe
```

and contain 23 lines.  With the A.3 local nondegeneracy, both implementations
again agree row-for-row on 20 lines, common SHA-256

```
36b82cd7a74d163143c538fd8fcbeb9e7d2f5f1dc2e561de57e758550169d1bf
```

The three rows removed at this stage are the extra `n=84` row and the
`n=96` rows with `M=[84,88,94]` and `M=[80,88,92,94]`.

## A.3 local and cyclic-quotient passport

Write Proposition A.3's equation in the form

```
P p q' - Q p' q = c p,  c != 0.
```

At a shared root `alpha`, write
`p=(pi-alpha)^v p_0`, `q=(pi-alpha)q_0`.  The p.205 square-freeness gives
`q_0(alpha)!=0`, and the lowest coefficient in the displayed equation is

```
(P-Qv) q_0(alpha) = c.
```

Hence **no p-root can have exactly the average multiplicity** `v=P/Q`.
This is source-proved, not a heuristic.

There is a further safe passport test after taking the cyclic quotient.  For
`Q=AS+1`, pad the `k` nonzero p-orbits with `v_l=0` to the `S` nonzero q-orbit
slots and define

```
W_0 = (P-Qb)/A,
W_l = P-Qv_l  (1 <= l <= S),
g = gcd(|W_0|,...,|W_S|),
d_+ = sum max(W_i,0).
```

The root-of-unity forms are
`p=pi^b product(z-a_l)^{v_l}` and
`q=pi product(z-c_l)`, with `z=pi^A`.  Therefore
`q^P/p^Q` is a rational function of `z` whose divisor weights are the `W_i`.
After division by their gcd, its degree is `d_+/g`.  Dividing A.3 by `pq` and
changing from `pi` to `z` shows that the logarithmic derivative has denominator
`z product(z-c_l)`, so infinity has exact ramification `S`.  Necessarily

```
d_+/g >= S.
```

This cyclic passport is integrated into the partition DP (rather than tested
only on the first witness).  At `n<=100` it removes no row beyond the local
nondegeneracy: **20/12**, six printed plus 14 excess.  Thus exact A.3
*polynomial realizability* remains open; the two divisor/passport consequences
above do not recover Moh's output.

## Degree-range metrics

All counts below use `Kmin=16` and then the pinned-N knapsack from the frozen
driver.  `mixed` means an integer `N` in `[6,16]`; no cap was reached.

| candidate/range | V rows | groups | UNI, N>=6 | mixed alive |
|---|---:|---:|---:|---:|
| whole tree, 48--120 | 91 | 54 | 39 | 41 |
| whole tree, 121--200 | 1,600 | 794 | 551 | 531 |
| whole tree, 48--200 | 1,691 | 848 | 590 | 572 |
| + A.3 quotient passport, 48--120 | 68 | 38 | 27 | 29 |
| + A.3 quotient passport, 121--200 | 1,247 | 593 | 402 | 387 |
| + A.3 quotient passport, 48--200 | 1,315 | 631 | 429 | 416 |

Requested per-degree raw group counts for the whole tree at
`D=105,108,112,117,120` are respectively **0, 7, 1, 0, 31**; mixed-alive
counts are **0, 3, 1, 0, 25**.  With the quotient passport they are
**0, 5, 1, 0, 20** raw and **0, 3, 1, 0, 15** mixed alive.

Among degrees which had at least one printed-list skeleton, whole-tree
partition empties the following before knapsack:

```
48--120: 48,54,60,63,72,80,81,88,100,102,104,105,110,114,117
121--200: 130,152,153,154,170,176,182,186,190,195
```

The quotient passport additionally empties `174` and `184`; at `156` it
leaves raw groups but the mixed knapsack empties the degree.  Degrees with no
printed-list skeleton are recorded separately in the JSON outputs and are not
misreported as eliminations by this candidate.

## Artifacts and bounds

- `tree-independent.py`: independent exact DP and driver.
- `tree-independent-n100.json`: 23-row whole-tree audit.
- `tree-independent-passport-n100.json`: 20-row local/passport audit.
- `tree-independent-D48-120.json`, `tree-independent-D121-200.json`: whole-tree
  extended census.
- corresponding `tree-independent-passport-D*.json`: quotient-passport
  extended census.

The largest measured run (`121--200`) used one core, tens of seconds, and far
below 4 GB.  All writes are confined to the requested driver directory.

Bounded residual: **17 rows after the source-derived whole-tree condition; 14
rows after its A.3 local/passport strengthening**.  A further exact ODE/Belyi
realizability test could cut some of these, but no such cut is printed or
proved in the cited pages, and it is not safe to assume that every abstract
passport is or is not realizable.  This remains a bounded sub-open of
`OPEN[MOH-PROGRAM]`, not a source-proved recovery of Moh's hidden program.
