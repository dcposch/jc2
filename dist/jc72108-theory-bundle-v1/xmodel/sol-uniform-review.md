VERDICT: CONFIRMED — no third perimeter escape survives: after correcting WIN to budget-admissible competing vertices, AM/WIN/N1–N4 close nonminimum charged strata, arbitrary insertion/padding stacks, E5 reroutes, and boundary M-drops; the 17-cell tower obstruction is sound, although several prose and executable-completeness claims need the errata ranked below.

# Sol hostile review of `TOWER-UNIFORM.md`

Date: 2026-08-14

Scope reviewed: `TOWER-UNIFORM.md`, the five promoted/probe tower
certificates and reviews, `TOWER-ROLLOUT.md`, `BOOK-OFFAXIS.md` §11a,
`xmodel/sol-gluing-design.md` §2.4/§4.1, `xmodel/sol-h5a.md`,
`cases/tower_check.py`, and the `px2`/`px5`/E5-census machinery.  I
independently replayed the WIN menus, expanded the dirty-menu search caps,
enumerated the terminal-side closures, derived E5F from the H5a formulas,
recomputed three deliberately awkward witness rows, and constructed mixed
perimeter stress realizations.  No theorem escape was found.

## Ranked findings

### 1. HIGH, statement/certification erratum — the literal WIN lemma is false, but the corrected budget-admissible lemma is sound

`TOWER-UNIFORM.md:95-111` needs two scope words that are mathematically
load-bearing for the statement, though not for the intended proof.

First, "every realization vertex gap is `<= 2/5`" is literally false:
the same document gives `gap(X)>1/2` and pole gap `5/2`.  The proved
statement is:

> Every budget-admissible competing vertex other than the poles and the
> pole-adjacent chain-1 vertex `X` has gap at most `2/5`.

Second, "every non-resonant step has menu ratio `<=2`" is true only after
the route budget is imposed.  If a parent has full `f`-degree `D`, then

```text
D_child = D*d_p/l,
gap(child) = d_q/D_child = (l*d_q/d_p)/D.
```

My independent scan of all 69 closure states found 49 budget-admissible
dirty/`st96` transitions.  Their ratio supremum is exactly `2`, uniquely at

```text
parent (w,M)=(1/2,4), spent=4,
st96 l4e0k1S1x0nu2(10,5), l=4, added cost=1.
```

At ENTRY the complete dirty menu is

| cell | `l` | cost | `l*d_q/d_p` | child gap from `D=4` |
|---|---:|---:|---:|---:|
| `(21,15)` (A) | 2 | 2 | `10/7` | `5/14` |
| `(20,16)` (C) | 2 | 2 | `8/5` | `2/5` |
| `(7,5)` epsilon | 2 | 3 | `10/7` | `5/14` |

Thus the corrected entry bound is exactly `8/5`, and `(C)` really attains
the enumeration-wide competing-vertex maximum `2/5`.  Every later parent
has `D>=8` because `d_p/l>=nu>=2`, so a non-resonant child has gap at most
`2/8=1/4`.  Pure-b and neutral `n=1` families give, respectively,

```text
l(nu+1)/(l*nu+epsilon) <= (nu+1)/nu <= 3/2,
(nu+1)/nu <= 3/2.
```

Without the budget qualifier there is a concrete ratio counterexample:
from `(w,M)=(3/5,5)` at spent cost `5`, the outgoing cell `(14,7), l=5`
has ratio `5/2`.  Its added cost is `2`, so total cost `7` is outside the
td-7 perimeter.  It cannot be used against the theorem, but it refutes the
literal menu sentence and the present check label.

The resonance conclusion is also correct, but one executable check passes
partly vacuously.  The only resonant-step state keys are

```text
(3,1), (3/5,1), (3/5,5),
```

all with `clean D3n2nu2`, hence ratio `5/2`.  They are non-entry states, so
the structural `D>=8` bound already gives gap at most `5/16<1/2`.
`tower_check.py:1595-1603` never reaches `(3/5,1)` in its sampled frames and
accepts it through `.get(state,10**9)`.  An exact omitted realization is

```text
ENTRY --(20,16),l2--> D=40
      --(25,10),l4--> D=250, state (3/5,5)
      --neutral (4,5),l1,nu4--> D=1000, state (3/5,1)
      --clean (2,5),n2,nu2--> D=2000, gap=1/400.
```

So this is a checker hole, not a window escape.  The robust check is state
membership plus the structural `D>=8` proof, with no large default.

### 2. HIGH, perimeter-accounting erratum — nonminimum charged strata are omitted from the prose and the 238-route interpretation

The realization axes that the endpoint-record quantifier must cover are
listed explicitly by `xmodel/sol-gluing-design.md:1651-1655`: every
predecessor, arrival, root-of-unity branch, neutral-depth family,
free-characteristic pure-b family, nonminimum budget-feasible charged
stratum, and tower branch.  Its COVERAGE construction also requires all
positive-cost strata at `:1064-1086`.

`TOWER-UNIFORM.md:22-26` names arrivals/`M_U`, free characteristics,
padding, insertions, terminals, and E5 reroutes, but not nonminimum charged
strata or charged state self-returns.  The §11a counts use the minimum
`dist[(w,M)]`; they are state/endpoint summaries, not a count of all charged
provenances.

There is a concrete omitted charged stratum inside the `(10,15,7,5)@3`
record:

```text
P2 -- A=(21,15),l2,cost2 --> (w,M)=(2/3,3), D=42
   -- (21,9),l3,cost2 ----> (w,M)=(2/3,3), D=294.
```

The second tag is
`st96 l3e1k1S2x0nu4(21,9)`.  It is a positive-cost state self-return,
so the arrival state is reached at cost `4` rather than its filed minimum
`2`.  The last vertex is a legal direct arrival with

```text
nu_U=4, kbar_U=3,
n=4*6-7*3=3,
i_G=294/3=98, P=49,
gaps=(5/14,3/98).
```

There are three budget-fitting one-cost terminals from the cell state:
`(2/9,M9)`, `(2/7,M7)`, and `(4/9,M9)`.  This charged provenance is not a
new member of the §11a minimum-cost count, but it is present in the uniform
frame traversal and is killed: AM still fixes its first charged vertex to
(A), WIN keeps both gaps below `X`, and the universal A/B/C block is
unchanged.

I also composed all of the suspected interaction axes in one realization:

```text
pre-A neutral Y=(6,4), l2,nu3
  -> A=(21,15)
  -> charged self-return (21,9),l3
  -> E5 repair pad (15,6),l3,nu5
  -> one-cost terminal.
```

Its full degrees and gaps are

| vertex | full degree | gap |
|---|---:|---:|
| `Y` | 12 | `1/3` |
| (A) | 126 | `5/42` |
| charged return | 882 | `1/98` |
| E5 pad | 4410 | `1/735` |

The pad has `(nu_U,kbar_U)=(5,4)`, hence E5 offset
`n=5*6-7*4=2`; `i_G=1470` and `P=735`.  This combines a pre-first-charged
insertion, nonminimum charge, rerouting pad, and terminal choice without
opening the window or weakening the joint cap.

Arbitrary finite repetitions remain closed.  Before the first charged
vertex, preserving `M=2` makes every inserted characteristic odd, so N3
continues to give `gcd(4,2P_pre)=2`.  Elsewhere every neutral insertion has
gap `(nu+1)/(D_prev*nu)` and increases downstream degree.  An `M`-drop to
`1` is absorbed by AM; an `M`-drop retaining a divisor at least `2` is an
ordinary zero-cost closure edge and obeys the same N4 bound.  Root choices,
later NE-multiplicity partitions, and tower branches do not change the
degree/gap/frame inputs used by the level-1 contradiction.

The theorem should therefore add "all budget-feasible charged predecessor
strata, including charged state self-returns and multiplicity partitions"
to its perimeter sentence.  This corrects the accounting without changing
the verdict.

### 3. MEDIUM, executable-completeness erratum — `242 path-states` is a finite symbolic sample, not exact realization enumeration

The parser at `cases/tower_check.py:1489-1522` takes only one
characteristic for each pure-b or neutral-drop family, omits identity
self-loops, and the traversal has depth `8` and degree `10^8` cutoffs at
`:1539-1548`.  It prints 242 but never asserts that count.  Larger symbolic
characteristics and arbitrary neutral stacks are therefore not enumerated.

There are even legal small members missed by the "first characteristic then
break" rule.  At ENTRY, an `M:2->1` neutral with `l=1,nu=3`, cell `(3,4)`,
has exact frame `(rho,kbar)=(3/2,6)` and degree `12`.  The parser first tries
`nu=2`, obtains a nonintegral frame, rejects it, and never tries `nu=3`.
This particular omitted path is harmless because it lands `M=1` and AM
absorbs it; the missing `(3/5,1)` resonance above is harmless by growth.

The symbolic proof does carry what the enumeration does not: pure-b ratios
are monotone-bounded, neutral insertions are covered by N1–N4, and changing-
state clean resonances have strict numerator descent.  I expanded the dirty
search in memory from `k<7, ell_ex<41` to `k<13, ell_ex<501`; it produced no
new budget-admissible transition on any of the 69 states.  Accordingly the
242 rows are useful corroboration, but `TOWER-UNIFORM.md:137-140,202-205`
should not call them exact or full realization enumeration.

### 4. MEDIUM, terminal-side proof/check gap — the cited `L-E` is not bound by uniform mode, but an independent conservative scan closes it

Uniform mode enumerates the chain-2 predecessor frames and calls
`px5.feasible` for route-count parity; it does not reconstruct the merge and
trunk frames for all 238 terminal records.  `TOWER-UNIFORM.md:109-110`
instead cites "L-E", which appears as a candidate obligation in the planning
artifact `TOWER-ROLLOUT.md:98,191-195`, not as a named check in uniform mode.

I independently started each of the 16 new/probed merge cells at its minimum
E5-legal arrival degree, allowed its entire remaining budget (a conservative
superset of each actual completion), and replayed every trunk transition with
exact fractions.  For every cell the largest terminal-side gap was the merge
cell's own gap; the three largest were

```text
(10,15): 3/28,
(25,35): 7/250,
(18,27): 3/196.
```

All are below `1/2`, and every rootward child was smaller.  For symbolic
pure-b and neutral members, the ratio is maximized by the smallest admissible
characteristic; extra insertions only enlarge `D_prev`.  Thus terminal choice
cannot steal the `(gap(X),5/2)` window.  The theorem is safe, but this audit
should be promoted into an explicit lemma/check rather than left under the
undefined `L-E` label.

### 5. MEDIUM, checker-binding defects — pad vertices and two advertised E5 claims are not actually checked

For a pad witness, `tower_check.py:1682-1683` multiplies the degree but keeps
the pre-pad `frames` tuple.  Consequently the max-gap and prefix-delta loops
at `:1693` and `:1722-1724` omit the pad itself, despite
`TOWER-UNIFORM.md:137-140,168-170` saying every witness vertex.  The frozen
depth field is also never compared at `:1699-1704`.

Two named E5 checks are similarly weak:

- the global charged-form check at `:1613-1616` has condition `True`;
- "m=23 has NO legal direct arrival" at `:1725-1727` only checks the frozen
  expected label.

These are real gate defects, but independent replay closes them.  The added
pad gaps and deltas for the three rows audited below are all valid, and the
only direct cell at `(w,M)=(2/23,23)` is `nu_U=11`, whose E5 offset is `-1`.

There is also a prose overrestriction at `TOWER-UNIFORM.md:117`: the charged
closed form needs `rho_U=1/mu0`, not `M_U=mu0`.  The promoted `(9,15)`
charged arrival with `(mu0,M_U)=(2,4)` is a counterexample to the parenthetical
equality and still satisfies the formula because `rho_U=1/2`.  Write
`mu0 | M_U` plus the stated `rho_U` condition.

### 6. CONFIRMED — E5F agrees exactly with the independent H5a/E5 derivation

Under the thesis-to-campaign letter map in `xmodel/sol-h5a.md:48-60`, the
promoted E5 equation is

```text
kbar_G = (nu_G*kbar_U+n)/nu_U,
n = nu_U*kbar_G-nu_G*kbar_U.
```

Using `kbar_U=rho_U+nu_U*w_U` and
`X=mu0*(kbar_G-nu_G*w_U)` gives the useful general intermediate identity

```text
n = nu_U*X/mu0 - nu_G*rho_U.
```

Hence:

- if `rho_U=1/mu0`,
  `n=(X*nu_U-nu_G)/mu0`;
- for a clean pad, `rho_U=w_U` and
  `kbar_U=(nu_U+1)w_U`, so
  `n=((nu_U+1)X-mu0*kbar_G)/mu0`;
- at the minimal pad `nu_U=mu0-1`,
  `n=X-kbar_G=-2` because `X=kbar_G-2`;
- on the last-six-cell family
  `(kbar_G,X,nu_G)=(6,4,3m-2)`, the direct
  `nu_U=(m-1)/2, kbar_U=1` has `n=-1` identically.

These are precisely the E5F forms in `TOWER-UNIFORM.md:113-133`.  There is
no orientation, denominator, or congruence mismatch with `sol-h5a`.

### 7. CONFIRMED — three independently recomputed awkward witness rows match, including the pad vertices omitted by the gate

I selected two neutral-only `kbar=5` rows and the `m=23` no-legal-direct
row, rather than the already certified/probe rows.

#### `(15,25,12,5)@3`

The minimum predecessor is

```text
(20,16),l2:       D=40,   gap=2/5
(119,35),l4:      D=1190, gap=1/34
pure-b (15,3),l7: D=2550, gap=1/850,
```

at `w=1/3`.  Pad `nu=2` has `kbar_U=1`, degree `5100`, and
`n=2*5-12=-2`, so it is refuted.  Pad `nu=5` has

```text
kbar_U=2, n=5*5-12*2=1,
deg_U=12750, i_G=4250, P=2125,
gap_pad=6/12750=1/2125.
```

With `D_f=rho*deg=(1/3)*12750=4250`, the missing pad deltas at
`g in {3/2,1,2}` are `(6373,4248,8498)`, all positive integers.

#### `(21,35,17,7)@4`

The minimum predecessor degrees are

```text
(20,16),l2 -> 40,
(119,35),l4 -> 1190,
(55,11),l7 -> 9350,
pure-b (36,4),l11 -> 30600,
```

at `w=1/4`.  Pad `nu=3`, `kbar_U=1`, has degree `91800` and `n=-2`.
Pad `nu=7` gives

```text
kbar_U=2, n=7*5-17*2=1,
deg_U=214200, i_G=53550, P=26775,
gap_pad=8/214200=1/26775.
```

The omitted pad deltas are `(80323,53548,107098)`.

#### `(90,135,67,45)@23`

The minimum predecessor is

```text
(20,16),l2 -> D=40,
(119,35),l4 -> D=1190,
(247,39),l7 -> D=41990,
(253,23),l13 -> D=817190,
```

at `(w,M)=(2/23,23)`.  The only direct arrival is
`nu_U=11,kbar_U=1`; it has `n=11*6-67=-1` and is refuted.  The first legal
pad is `nu_U=45`, with

```text
kbar_U=4, n=45*6-67*4=2,
deg_U=817190*45=36773550,
i_G=1598850, P=799425,
gap_pad=46/36773550=1/799425.
```

Here `D_f=(2/23)*36773550=3197700`, and the omitted pad deltas are
`(4796546,3197696,6395396)`.  Every one is positive integral.  In all
three rows the path maximum remains the first `(C)` gap `2/5`.  The frozen
table is arithmetically exact for these picks.

### 8. CONFIRMED, with terminology correction — reading independence consumes no proof of `U_7C`

`xmodel/sol-h5a.md:19-34,136-196` establishes Q+E5 as the promoted global
repair; it does not establish equal indices.  `U_7C` is an additional
conjectural restriction, not a second H5a convention.  The clean logical
case split is:

1. Under the promoted Q+E5 perimeter, the conservative book has all 17
   cells, and this theorem kills them.
2. If `U_7C` is additionally imposed, §11a restricts the book to exactly
   `(9,15)` and `(10,15)`, already killed by the promoted certificates.

On the only case-III edge of each forced-index certificate, the indices are
actually equal and the two formula presentations coincide pointwise:

```text
(9,15):  nu_G=nu_U=7,  7*5 = 7*4 + 7;
(10,15): nu_G=nu_U=7,  7*6 = 7*5 + 7.
```

All their other edges are case II or IV.  Thus no proof or hidden use of
`U_7C` enters the global empty-book conclusion.  The 15 unequal-index cells
do consume exactly the promoted Q+E5 resolution already declared in the
trust perimeter, and nothing stronger.  `TOWER-UNIFORM.md:39-42` should say
"the Q+E5 book and its `U_7C`-restricted sub-book" rather than "both
coherent H5a readings."

## Reproduction and final disposition

The advertised gate ran with exit `0`: 1550 `[PASS]`, zero `[FAIL]`, and all
21 negative perturbations caught.  Independently, `cases/td7_census_e5.py`
reproduced:

```text
closure: 69 states;
promoted: 17 cells, 238 raw (202 equality), 233 dedup (197 equality);
forced-index restriction: 2 cells, 51 raw (33 equality), 49 dedup (31 equality);
ALL GATES PASS.
```

Uniform mode itself checks the 16 displayed raw/equality pairs; the
`233` deduplicated total comes from the census engine, not from a uniform
assertion.  The executable weaknesses above should be hardened, and the WIN
and perimeter sentences should be corrected before calling the 1550 checks
an exhaustive realization certificate.  They do not supply a surviving
ladder: the panel-closure theorem is confirmed on its stated filed P0/§11a
perimeter.
