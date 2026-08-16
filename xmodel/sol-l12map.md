# Q2-l12 / J-window intersection map (G* lane 3)

## Executive summary (five lines)

1. The two constructions use the same coefficient tower: the 183-name D21 J registry is exactly `build_generators(53)`, and all 225 depth-53 orbit entries agree name-for-name and coefficient-for-coefficient with the depth-84 Q2 tower.
2. All 74 registry coefficients that occur in J have exact Q2-l12 back-maps (1 zero, 41 identity, 32 polynomial); as formal polynomial pullbacks, every leaf receives **47/47 band conditions and 10/10 slot-20 components**.
3. The literal banked locus called $V$ is only the hidden $B=0$ slice: this makes leaf12 (`bg42_24 != 0`) and leaf13 (`bg21_24 != 0`) domain-disjoint, leaving only leaf11 (`uf24 != 0`).
4. After Q2 pullback to leaf11 and the D21 $B=0$ specialization, all 47 band conditions vanish and slot 20 reduces to eta $0,3,6$; eta3/eta6 are Q2 relation $E$, while eta0 is an affine candidate not proportional to $E$.
5. Payoff: two charts are excluded by the banked slice and one nonzero candidate pullback survives on the third, but no transported-row kill, full-ideal cut, or set-theoretic strictness is certified; the seven Q2 quotient rows and nonemptiness of $V$ remain open.

## 1. Scope and conventions

This report intersects the objects that actually exist on disk.  It does not
silently replace either one by a larger intended object.

- **Q2 side:** the l12 parent and its already-banked first-nonzero leaves
  11/12/13 at $p=105337,105673$.  The exact l13-to-l12 delta and the chart
  identities are recorded in `SHEET6-R1.md:2729-2742`; leaf substitution and
  support collection are implemented in `cases/r1_q2_l8_leaves.py:118-146`.
- **J side:** `directionb_tails_D21.pkl`, the 47 branch-echelon conditions in
  `directionb_window_conditions.pkl`, and the ten raw Row20 eta components.
  The raw VExpr/radical schema is `cases/directionb_window.py:5-11`; the
  branch convention is $HW_i=s_i\mu W_i$ at `:25-31`; condition construction
  and banking are `:287-370`; the unique `+42` is `:374-377,441-459`.
- **Exactness tier:** every equality below was checked in exact sparse
  Laurent-polynomial arithmetic over both banked prime fields and, for the
  echelon conditions, on all four $h$-sign branches.  No `msolve` or numeric
  approximation was used.  This is a modular map/restriction result, not a
  characteristic-zero emptiness certificate.

There is a load-bearing scope correction.  The J builder says “B-side
frozen” and retains only the seven plus P-side `tf*`/`tg*` names
(`cases/directionb_strike.py:227-247`).  The hostile audit makes the
consequence explicit: all 100 `bf/bg*` registry variables occur in no banked
J row, and the displayed $V$ is the **$B=0$ slice**, not the unfrozen
J-window (`SHEET6-DIRECTIONB-REVIEW.md:556-575`).  Thus I use

\[
  V_{\rm bank}=V_{J,D21}\cap\{B_{D21}=0\},
\]

where $B_{D21}$ denotes exactly the 100 B-side registry coefficients at
levels below 53, not every fresh B coefficient in the deeper Q2 tower.

For support bookkeeping I first pull the stored J polynomials back to each
formal Q2 leaf before imposing their B-domain tag.  This is **not** the true
unfrozen J-window: rebuilding with B free would add terms and columns that do
not occur in this bank.  The semantically valid payoff is then assessed on
the literal $V_{bank}$.

## 2. The common coefficient object

### 2.1 Registry semantics

The template uses levels in $1/42$-units; a suffix `_m` is the coefficient
at absolute $t$-level $m$.  The series/level convention is explicit in
`cases/r1_experiment.py:263-265`.  The template scales, vertex polynomials,
free grids and orbit bookkeeping are in `SHEET6-TEMPLATE.md:84-110,113-138`.

The authoritative registry builder is
`cases/r1_experiment.py:344-404`.  It gives these literal name
identifications—there is no rescaling between the Q2 and J names:

| prefix | residue-A coefficient tower / orbit |
|---|---|
| `uf_m` | common dead-stretch coefficient shared by all six P-side A orbits |
| `vf1_m`, `vf2_m` | pole-1/pole-2 merge coefficient shared by the corresponding f/g orbits |
| `tf1_m`, `tf2_m` | f-tail on `P1`, `P2` |
| `bf_m` | f-tail on the B 42-orbit |
| `tg1_m`, `tg2_m` | g-tail on `Gp1`, `Gp2` |
| `tg01_m`, `tg02_m` | g-tail on the even 21-orbits `G0p1`, `G0p2` |
| `bg42_m`, `bg21_m` | g-tail on the B-side 42- and 21-orbits |

The defining assignments are exactly
`cases/r1_experiment.py:373-403`.  The machine guard rebuilt depths 53 and 84,
replaced volatile ids by registry names, and compared the 225 common orbit
series entries as exact dictionaries.  It also checked that the 183 names in
the J pickle equal the fresh depth-53 registry in order.

### 2.2 Every J-occurring name and its Q2 core alias

Only 74 of the 183 D21 registry names occur in a J monomial.  They are exactly
the following.  The ordered level lists make every individual identification
explicit; the corresponding banked aliases appear verbatim in
`systems/r1/r1_full_core.rows.txt:107-138,157-198`.

| J registry names (ordered levels) | Q2 full-core aliases, same order | l12 back-map class |
|---|---|---|
| `uf18, uf24` | `x0, x1` | `uf18 -> 0`; `uf24` identity |
| `vf1_34, vf1_36, vf2_34, vf2_36` | `x2, x3, x4, x5` | identity |
| `tf1_{38,39,40,41,42,43,44,45,46,47,48,50,52}` | `x6`–`x18` | polynomial |
| `tf2_{38,39,40,41,42,43,44,45,46,47,48,50,52}` | `x19`–`x31` | polynomial |
| `tg1_{38,39,40,41,42,43,44,45,46,47,48,50,52}` | `x50`–`x62` | levels 38/40/42 polynomial; the other ten identity |
| `tg2_{38,39,40,41,42,43,44,45,46,47,48,50,52}` | `x63`–`x75` | levels 38/40/42 polynomial; the other ten identity |
| `tg01_{38,40,42,44,46,48,50,52}` | `x76`–`x83` | identity |
| `tg02_{38,40,42,44,46,48,50,52}` | `x84`–`x91` | identity |

This is 1 zero + 41 identities + 32 nontrivial composed maps.  The
complete polynomial maps are produced by the reverse UU/reduction
substitutions in `cases/r1_q2_screen.py:167-228`; that function independently
regresses all 119 core values against the banked witness at `:229-250`.
Core `xN` is carried to depth 84 by **exact registry-name equality** at
`:255-271`.

For an audit-sized fingerprint of all 32 polynomial maps, their exact numbers
of surviving Laurent monomials are:

| family | ordered levels | term counts at both primes |
|---|---|---|
| `tf1` | 38,39,40,41,42,43,44,45,46,47,48,50,52 | 1,1,1,1,3,1,2,1,9,4,16,56,121 |
| `tf2` | 38,39,40,41,42,43,44,45,46,47,48,50,52 | 1,1,1,1,3,1,2,1,2,4,2,2,104 |
| `tg1` | 38,40,42 | 1,1,3 |
| `tg2` | 38,40,42 | 1,1,3 |

The support and term-count vectors agree at the two primes; coefficients are
the appropriate exact reductions of the common radical/back-map expressions.
`cases/q2j_map.py` checks every sparse expression, not merely these counts.

The J occurrence census agrees with the emitted residual registry description:
42 high tails, 26 low tails, and six of the seven dead-stretch/merge names;
`uf30` never occurs (`SHEET6-DIRECTIONB.md:610-628`).  No B name occurs.

### 2.3 The exact l12 delta and charts

The two surviving l12 emit pickles and both `.ms` emissions give

\[
\operatorname{hdr}(l12)\setminus\operatorname{hdr}(l13)=
\{uf24,bg42\_24,bg21\_24,tg1\_60,tg2\_60,tg01\_60,tg02\_60,
bg42\_60,bg21\_60\}.
\]

This is the documented low triple plus six level-60 highs
(`SHEET6-R1.md:2729-2738`).  The deterministic depth-84 identifications are:

| l12-new name | core alias | depth-84 registry id |
|---|---:|---:|
| `uf24` | `x1` | 1 |
| `bg42_24` | `x103` | 319 |
| `bg21_24` | `x115` | 384 |
| `tg1_60` | fresh | 192 |
| `tg2_60` | fresh | 238 |
| `tg01_60` | fresh | 273 |
| `tg02_60` | fresh | 296 |
| `bg42_60` | fresh | 355 |
| `bg21_60` | fresh | 402 |

The low core aliases are banked at
`systems/r1/r1_full_core.rows.txt:108,210,222`; the high names are fresh
depth-84 coordinates.  Q2 leaf construction applies the zero prefix
monomial-by-monomial and then adds the pivot saturation
(`cases/r1_q2_l8_leaves.py:118-143,187-190`):

| leaf | coefficient chart | literal banked-$V$ domain |
|---:|---|---|
| 11 | `uf24 != 0` | compatible after setting the 100 D21-registry B coefficients to zero |
| 12 | `uf24 = 0`, `bg42_24 != 0` | empty: $B=0\Rightarrow bg42_{24}=0$ |
| 13 | `uf24 = bg42_24 = 0`, `bg21_24 != 0` | empty: $B=0\Rightarrow bg21_{24}=0$ |
| origin | all three lows zero | l13, already proof-tier empty |

### 2.4 The B-coordinate map

The D21 registry has exactly 100 B coefficient names:

- `bf_13,...,bf_52` (40),
- `bg42_13,...,bg42_52` (40),
- `bg21_14,bg21_16,...,bg21_52` (20).

On the l12 Q2 coefficient map, 26 are already zero by the cutoff, 19 are
same-name core coordinates, and 55 are same-name fresh coordinates.  None has
a nontrivial polynomial back-map.  Therefore the hidden B freeze transports
unambiguously to “set these 74 live chart coordinates to zero”; in particular
it really does set the two B-low pivots to zero.  This is machine-checked
against all 100 names, not inferred from their prefixes.

## 3. Which J conditions restrict?

### 3.1 Correct transport test

A coefficient-by-coefficient support test is too conservative here.  After
the Q2 back-map and leaf zeros, only 50/74 individual J coefficients have
support entirely inside a leaf header.  The other 24 are

- `tf1,tf2,tg1,tg2` at levels 43,45,47,50,52 (20 names), and
- `tg01,tg02` at levels 50,52 (4 names).

That does **not** make an equation untransportable.  Those names are dummy
coordinates for the particular Q2 quotient projection, and their
contributions cancel across complete J equations.  The correct exact test is:

1. replace every registry coefficient in the J equation by its composed Q2
   back-map (`cases/r1_q2_screen.py:167-228`);
2. drop every monomial hit by the leaf's zero prefix, exactly as
   `cases/r1_q2_l8_leaves.py:118-143` does;
3. for an echelon branch set $HW_i=s_i\mu W_i$, matching the bank convention
   in `cases/directionb_window.py:25-31`;
4. multiply and add the **whole** sparse polynomial;
5. inspect the final, cancelled support against the emitted leaf header.

The checker also repeats the computation from the 77 raw eta rows, so the
result is not an artifact of the echelon presentation.

### 3.2 Counts per chart

As a polynomial-support statement, the answer is full formal transport on
every leaf:

| Q2 chart | banked band conditions | raw slot-20 components | total scalar pullbacks |
|---|---:|---:|---:|
| leaf11 | 47/47 | 10/10 | 57/57 |
| leaf12 | 47/47 | 10/10 | 57/57 |
| leaf13 | 47/47 | 10/10 | 57/57 |

This holds at both primes and on all four $h$-sign branches.  The band ranks
are $1+4+6+7+10+10+9=47$, exactly the promoted ledger at
`SHEET6-DIRECTIONB.md:404-426`.  Slot 20 is ten simultaneous eta equations
with `+42` only at eta0 (`SHEET6-DIRECTIONB.md:437-445`).

Before imposing the banked B-domain tag, the same 26 formal echelon pullbacks
vanish identically on all primes, branches, and leaves:

```text
C6.1
C8.1-C8.4
C10.1-C10.6
C12.1-C12.7
C14.7-C14.10
C16.7-C16.9
C18.8
```

The 21 nonzero pullbacks are:

```text
C14.1-C14.6
C16.1-C16.6, C16.10
C18.1-C18.7, C18.9
```

At the raw-row level, every component of Rows 6, 8, 10 and 12 cancels; all
10/10, 10/10 and 9/9 components of Rows 14, 16 and 18 remain nonzero, and all
10 Row20 components remain nonzero.  The two presentations agree because the
banked echelon rows generate the exact band condition modules.

The nonzero mapped band support has a simple explanation:

- `C14.1-C14.6` is B-loaded through `bf_18`;
- the nonzero C16/C18 rows are loaded through at least one of
  `bf_18,bf_24,bg42_24,bg21_24`;
- every monomial of every nonzero mapped band condition contains a B
  coefficient.

Thus the stored frozen-row polynomials, considered outside their proper
domain only for support bookkeeping, acquire B-low Q2 coordinates through
the Q2 back-map.  This must not be called an unfrozen-J connection: the true
B-free J rows were never built.  On the proper domain, the D21 $B=0$
specialization annihilates all of these formal B-loaded terms.

## 4. Restriction to the literal banked locus

After first composing each complete J equation through the Q2 map on a leaf,
and then setting the 100 B coordinates in the D21 registry to zero:

- every raw band component in Rows 6 through 18 is identically zero, hence all
  47 banked band conditions vanish;
- Row20 eta $9,12,15,18,21,24,27$ vanishes;
- only eta $0,3,6$ survives, and these three contain no coefficient
  variable—only $W_1^4,W_2^4$ and the eta0 constant.

At $p=105337$:

```text
eta0: 42 + 35984 W1^4 + 80126 W2^4
eta3:      63830 W1^4 + 41180 W2^4
eta6:      73422 W1^4 + 84747 W2^4
```

At $p=105673$:

```text
eta0: 42 + 94026 W1^4 + 56719 W2^4
eta3:      57599 W1^4 + 89386 W2^4
eta6:      24037 W1^4 + 60980 W2^4
```

The Q2 relation-E rows are respectively

```text
p105337: 94902 W1^4 + 21273 W2^4
p105673: 11986 W1^4 + 12462 W2^4.
```

Both cross-determinants with eta3 and eta6 are zero at both primes; eta3 and
eta6 are also proportional to each other.  Consequently, after Q2 pullback
and the D21 B-zero specialization, the only J candidate beyond the
already-present Q2 relation E is eta0.

## 5. Payoff assessment

### 5.1 What is already strict

As a statement about the **literal banked object**, the intersection strictly
shrinks the l12 chart cover from three possible nonorigin charts to one:
leaf12 and leaf13 are empty against $B=0$ because their saturated pivots are
forced to zero.  This is exact and characteristic-independent.

It is not, however, a transported J-row kill and must not be advertised as the
first cross-family kill of the unfrozen program.  It diagnoses that the banked
§6.V object omitted precisely the B directions needed by two of the three
l12 charts.

### 5.2 The one surviving candidate equation

On leaf11, write $X=W_1^4, Y=W_2^4$.  Relation E and eta0 have nonzero
coefficient determinant, so eta0 is an affine scale equation linearly
independent from E in the displayed pole-scale subsystem:

| prime | determinant | forced $X$ | forced $Y$ | one fourth root pair |
|---:|---:|---:|---:|---:|
| 105337 | 46643 | 57673 | 53212 | `(31931, 9457)` |
| 105673 | 95410 | 44399 | 92038 | `(8021, 20111)` |

All four forced values are nonzero quartic residues.  With the displayed
fourth roots, the checker also solves the two E5 equations for `HM`, the E6
cube tie for nonzero `s1F`, and both saturations:

| prime | `HM` | `s1F` | checked Q2 rows |
|---:|---:|---:|---|
| 105337 | 13616 | 2811 | rows 0-7 and 15-19, all zero |
| 105673 | 40064 | 11339 | rows 0-7 and 15-19, all zero |

So eta0 is not an immediate pole-scale/E5/E6 contradiction.  It is an exact
candidate equation-level reduction: unless implied by the seven quotient
rows, it fixes the common scaling left by the homogeneous relation E.

The check deliberately stops short of a stronger claim.  Q2 quotient rows
8-14 were not solved, and §6.V itself states that no point of $V$ was
extracted (`SHEET6-DIRECTIONB.md:565-572`).  Without a Q2 point outside eta0
and a joint point inside it—or ideal membership/nonmembership—one cannot
certify that eta0 strictly shrinks the full set of geometric points.  The
honest payoff verdict is therefore:

- **literal-slice domain reduction:** yes, two charts excluded;
- **new nonzero candidate pullback on the surviving chart:** yes, one affine
  scale row nonproportional to E;
- **transported J-row chart kill:** not found;
- **full set-theoretic cut or intersection nonemptiness:** open.

### 5.3 No-log addendum

The instrument plan asked for J/no-log, while the task's named $V$ consists
of the 47+slot20 family.  Kept separate from those counts, all six live
level-42 no-log pins also transport.  Their registry identification is
documented at `SHEET6-DIRECTIONB.md:755-771`.

After the two direct pins

```text
tg01_42 = 0,  tg02_42 = 0,
```

the pullbacks of `tf1_42,tg1_42` are Laurent-unit multiples of
`uW1^2 * E`, and those of `tf2_42,tg2_42` are Laurent-unit multiples of
`uW2^2 * E`.  Hence no-log adds two direct coordinate pins modulo Q2 E, but
no immediate kill.  The three B-side no-log pins are not consumed: the source
itself requires the separate B-place normalization guard before using them
(`SHEET6-DIRECTIONB.md:769-776`).

## 6. Artifact and reproduction audit

The exact bank hashes used here are:

```text
directionb_tails_D21.pkl
  b4ba8dfcd9755fb3201780cd97c1d2ef38bd26d2d1b023521a0e62a3d6db169e
directionb_window_conditions.pkl
  43370c13ee42f078320acd029d64ebcedfb62eb205746186d97a0ab76a12869b
```

For each prime, the surviving `/tmp/r1q2/emit_p*_l12.pkl` and
`emit_p*_l13.pkl` were checked against the emitted `.ms` header, equation and
label lists exactly.  Their header delta is the nine-name set in §2.3.  Those
emit pickles are optional archival guards in the checker: if absent, the
banked `.ms`/`.rows.txt` artifacts remain the source, and `--verbose` reports
the missing optional files.

The original deeper Q2 build pickles and the reduction/leaf pickles were not
all preserved.  The latter two were deterministically replayed from the
archived full-core snapshot and the banked reduced `.ms`; `q2_backmap`'s
all-119 witness regression passed at both primes.  This archival gap does not
change the map, but it is why the checker has an explicit state-replay option.

Reproduce without any solver:

```sh
python3 cases/q2j_map.py
```

If the transient UU/reduction ledgers are absent (this option does not attempt
to recreate the optional Q2 emit pickles):

```sh
python3 cases/q2j_map.py --rebuild-state
```

Use `--verbose` for hashes, coefficient-map counts, zero labels and the exact
pole-scale data.  The script's default output is the registered five-line
summary.  It writes only transient replay state under `/tmp`; it does not
modify the repository.
