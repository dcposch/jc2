# t=4 normalization, residual structure, and exact unit certificate

## Typed result

**PROVED-HERE for the fixed `t = 4` order-chart necessary superset.**  After
the corrected three target gauges, 16 exact Q-star-pivot
eliminations, weighted normalization, and 22 exact affine eliminations over a
quadratic number field, the 65-row/45-unknown chart becomes eight equations in
four unknowns.  Singular's exact characteristic-zero number-field routine
returns the reduced unit basis `[1]` for this residual.  Consequently the
`c != 0` component of the corrected `t = 4` necessary chart is empty.

This result is stronger than the charged several-prime computation.  The
finite-field calculations below are labelled `MEASURED-MODULAR`; the promotion
uses the characteristic-zero basis only.  It is a fixed-t statement and is
not, by itself, a generic-t theorem.

## Frozen-input provenance

The lane receipt
`xmodel/k16-uniform-structure-sol56-20260903.run.v2` was parsed mechanically:
an `awk` command paired each `charged_input_<i>_sha256` with the corresponding
`charged_input_<i>_basename`, wrote
`box/k16uniform-20260903/t4_charged_inputs.sha256`, and
`sha256sum -c` returned `OK` for all 15 files.  No digest was retyped into the
check manifest.  All mathematical reconstruction in this note reads the
read-only files under `/tmp/jc2-lane.fjoTgL/inputs`.

The two primary reconstruction sources are:

- `t4_order_system.py`, SHA-256
  `db5e54450444f27c56f00bbec287aea284c8dc190e0e549c2fea51e0dbdd6cee`;
- `triangular_preprocess.py`, SHA-256
  `f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93`.

The quadratic-field affine routine is imported verbatim from the charged
`t3_normalized_slice.py`, SHA-256
`9e394dae1920e90413ff1aa6d0f5f8eb4dd9aa343a5826e0f4f8c586bd980ac7`.

## Correct chart and first triangular reduction

For `t = 4`,

\[
(n,m;M_2,V_2)=(52,36;49,3),\qquad (e,q)=(13,9),
\qquad \Phi=(-1,4/13).
\]

The two-disc coefficient-space dimensions for indices `1,...,13` are

```text
1,1,1,1, 2,2,2,2, 3,3,3,3, 5.
```

The gauges are exactly

```text
alpha_4 = 0,
const(beta_9) = 0,
const(alpha_13) = 0.
```

In particular, the middle gauge is `alpha_4`, not `alpha_2`: its term is
aligned with the leading `h^9` term of `Q`.  The gauged chart has 45
unknowns including `c`, 65 Jacobian-coordinate rows in bands `h^0` through
`h^17`, and degree histogram

```text
degree 1: 1; degree 2: 6; degree 3: 30; degree 4: 28.
```

The charged constant-pivot rule visits rows in descending band order and
eliminates only a row `aX+b` with `a in Q-star`.  Its direct frozen
rerun gives 16 pivots:

```text
band 17: a5_1
band 16: a6_1
band 15: a7_1
band 14: a8_1
band 13: a9_2,  a9_1
band 12: a10_2, a10_1
band 11: a11_2, a11_1
band 10: a12_2, a12_1
band  9: a13_2, a13_1
band  8: a13_0, a13_3
```

Their coefficients, in the same order, are

```text
9,9,9,9,18,9,18,9,18,9,18,9,18,9,-36,-27/4.
```

Every coefficient is a nonzero rational constant.  The charged reducer checks
the composed ring map on every one of the 65 original generators and keeps
`c` fixed.  The result is 48 rows in 29 variables including `c`.  The
recomputed audit is `t4_normalization_audit.json`; the deterministic normalized
row vector is `t4_normalized_rows.tsv`.

## Positive grading and the two decisive rows

For the 48 residual rows, the mechanical monomial-difference matrix has 3,650
distinct rows, rank 28 on 29 variables, and therefore a one-dimensional
grading space.  Normalizing `wt(b1)=1` makes every weight positive.  The full
remaining-variable table is

```text
b1,b2,b3,b4                         1,2,3,4
a1_0,a2_0,a3_0                      4,8,12
a5_0,...,a12_0                      20,24,28,32,36,40,44,48
q2_0,q3_0,q4_0                      8,12,16
q5_0,q5_1                           20,17
q6_0,q6_1                           24,21
q7_0,q7_1                           28,25
q8_0,q8_1                           32,29
q9_0,q9_1                           33,34
c                                     85
```

Thus, with

\[
x=q5_1,\qquad y=q9_1,
\]

one has

\[
\operatorname{wt}(x)=17,
\quad \operatorname{wt}(y)=34,
\quad \operatorname{wt}(c)=85.
\]

The two decisive exact residual rows are:

\[
35x^4-270x^2y+486y^2=0                                      \tag{1}
\]

and

\[
-2187c+130x^3y-1404xy^2=0.                                  \tag{2}
\]

More precisely, (1) is original zero-based source 26, band `h^4`, monomial
tag `(1,1)`, with rational associate multiplier `52/2187`.  Equation (2) is
source 2, band `h^0`, tag `(1,0)`; its coefficient of `c` after primitive
normalization is `-1`.

Equation (2) shows that `c != 0` forces `x != 0`.  The verified weighted
multiplicative-group action can therefore be used over an algebraic closure: choose
`lambda` with `lambda^17 x = 1`.  This makes `x = 1`, and (1) becomes

\[
H_4(y)=486y^2-270y+35.                                      \tag{3}
\]

The discriminant is

\[
(-270)^2-4\cdot486\cdot35=4860=18^2\cdot15,
\]

so `H_4` is irreducible over `Q`.  Equation (2) gives

\[
\bar c=\frac{y(130-1404y)}{2187}.                            \tag{4}
\]

Exact inverses modulo `H_4`, recomputed by the normalizer, include

```text
y^(-1)                  = 54/7 - 486*y/35
(130-1404*y)^(-1)       = 27*y/1105 - 5/442
cbar^(-1)               = 531441*y/1547 - 1062882/7735.
```

Thus `y`, `130-1404y`, and `cbar` are units in
`K4 = Q[y]/(H4)`.  Replacing `c` by (4) loses no point of the
normalized `c != 0` locus.

## Normalized system and exact affine reduction

Deleting the unique `c`-pivot row leaves 47 raw rows.  Canonical primitive
integer normalization exposes eight rational-associate duplicates, with
source indices

```text
3, 9, 15, 21, 27, 32, 37, 42.
```

The remaining copy of (3), source 26, becomes zero when `H_4` is installed
as the coefficient-field minimal polynomial.  Hence the normalized input is
exactly 38 rows in 26 auxiliary unknowns over `K_4`.

The charged affine routine then makes 22 pivots.  At each step its coefficient
is an element of `K_4`, its inverse is explicitly computed and checked
modulo `H_4`, and substitution into the pivot row is checked to give zero
before the operation is accepted.  Each step is therefore a quotient-ring
isomorphism, not a vanished-leader assumption.  The pivot sequence is

| step | source | band | variable |
|---:|---:|---:|---|
| 1 | 41 | 7 | `a1_0` |
| 2 | 20 | 3 | `q6_1` |
| 3 | 14 | 2 | `q2_0` |
| 4 | 36 | 6 | `q7_1` |
| 5 | 31 | 5 | `q8_1` |
| 6 | 8 | 1 | `a3_0` |
| 7 | 1 | 0 | `q9_0` |
| 8 | 25 | 4 | `q4_0` |
| 9 | 50 | 8 | `a5_0` |
| 10 | 19 | 3 | `q5_0` |
| 11 | 13 | 2 | `q6_0` |
| 12 | 45 | 7 | `a6_0` |
| 13 | 6 | 0 | `b1` |
| 14 | 30 | 4 | `a9_0` |
| 15 | 7 | 1 | `q7_0` |
| 16 | 40 | 6 | `a7_0` |
| 17 | 0 | 0 | `q8_0` |
| 18 | 35 | 5 | `a8_0` |
| 19 | 24 | 3 | `a10_0` |
| 20 | 49 | 8 | `b2` |
| 21 | 18 | 2 | `a11_0` |
| 22 | 12 | 1 | `a12_0` |

Eight additional rows become identically zero modulo `H_4` during these
substitutions: sources `43,38,33,28,22,16,10,4`.  The final exact residual is:

| source | band | tag | total degree | remaining variables |
|---:|---:|---|---:|---|
| 5  | 0 | `(0,1)` | 17 | `b3,b4,a2_0,q3_0` |
| 11 | 1 | `(0,1)` | 16 | same |
| 17 | 2 | `(0,1)` | 15 | same |
| 23 | 3 | `(0,1)` | 14 | same |
| 29 | 4 | `(0,1)` | 13 | same |
| 34 | 5 | `(0,1)` | 12 | same |
| 39 | 6 | `(0,1)` | 11 | same |
| 44 | 7 | `(0,1)` | 10 | same |

Here `y` is a coefficient-field element, so the displayed total degrees are
in the four auxiliary variables.  The exact coefficients, inverses, right
sides, and all eight generators are recorded in `t4_affine_audit.json`.

This answers the fixed-size question negatively: `t = 4` does **not** end in
six rows in three variables.  Together with the charged `t = 2,3` structures,
the observed shape is instead `2t` rows in `t` variables, in bands
`h^0,...,h^(2t-1)`.  The `t = 4` computation proves that shape only at
`t = 4`; it does not prove the all-t induction.

## Exact number-field certificate and both conjugates

Put

\[
s=54y-15.
\]

Then

\[
s^2-15=(54y-15)^2-15=6H_4(y).
\]

Conversely `y = (15+s)/54`, and direct substitution gives

\[
H_4((15+s)/54)=(s^2-15)/6.
\]

Therefore the maps

\[
\mathbf Q[y]/(H_4)\longleftrightarrow
\mathbf Q[s]/(s^2-15),
\qquad s\mapsto54y-15,
\quad y\mapsto(15+s)/54,
\]

are mutually inverse `Q`-algebra isomorphisms.  This is an abstract
quadratic field, so a unit certificate in it covers both embeddings
`s -> sqrt(15)` and `s -> -sqrt(15)`, equivalently both roots of
`H_4`.  Applying the nontrivial field automorphism to the certificate gives
the conjugate certificate; no root branch is discarded.

The final program installs the exact coefficient field

```text
ring RK=(0,sqrt15),(b3,b4,a2_0,q3_0),dp;
minpoly=sqrt15^2-15;
```

and calls Singular's `nfmodStd`, whose modular computations reconstruct a
standard basis over the characteristic-zero number field.  This is an exact
characteristic-zero algorithm; the conclusion is not inferred from a finite
field.  The captured run reports

```text
MAIN_START t=4 field=Qsqrt15 rows=8 vars=4 method=nfmodStd
MAIN_DONE basis_size=
1
MAIN_EXTRACT_RING_PASS
MAIN_EXACT_UNIT
G[1]=1
TIME_SEC=0.82 MAX_RSS_KB=15532 EXIT=0
```

The stderr file is empty.

## Controls and specialization discipline

The exact certificate program runs positive and negative wrapper controls in
each declared ring:

- `RAC` over `Q`: ring assertion, empty/nonempty wrapper controls,
  and the actual-pair check `J(pi, pi-gamma^2/2) = gamma`;
- `RC` over `Q(s)`: ring assertion, empty/nonempty wrapper controls,
  and the exact unit check for the image of `cbar`;
- `RK` over `Q(s)`: ring assertion and empty/nonempty wrapper
  controls immediately before the main ideal.

Every marker is `PASS`.  The actual pair remains a negative-classifier
control: as the charged driver records, it has `J = gamma` but fails the
`K = 16`, `t = 4` tuple and is not a target witness.

There is no `FALLACY-v2` generic-parameter specialization issue here.  The
certificate is at the fixed integer `t = 4`, all 22 divided coefficients have
verified inverses in the declared quadratic field, and `[1]` is computed in
that exact field.  The separate GF(32003) subset scan is corroborative only:
the full eight rows, the first five bands, and one interleaved five-row subset
are modular units, while the last five and last six bands are nonunit.  No
characteristic-zero conclusion is drawn from those modular outcomes.

## Why this proves fixed-t = 4 emptiness

Suppose the original corrected gauged chart had a point with `c != 0` over an
algebraic closure of `Q`.  The 16 rational constant pivots carry it,
via exact quotient isomorphisms, to the 48-row residual.  Equation (2) makes
`x != 0`, and the positive homogeneous action carries that point to the
`x = 1` slice.  Equations (1)--(2) then put `y` in `K_4` (after choosing
either embedding) and set `c = cbar != 0`.  The 22 checked `K_4`-affine
pivots carry it to a common zero of the eight final generators.  But their
ideal is the unit ideal in `K4[b3,b4,a2_0,q3_0]`, and hence remains the
unit ideal after algebraic closure.  This is a contradiction.

Thus the necessary order-chart superset has empty `c != 0` component.  Since
the requested tuple locus maps into that necessary superset, the fixed
`t = 4` instance of theorem (T) follows.  This argument makes no converse
claim about the omitted tuple-level Laurent bridge.

## Reproduction

From `/home/ubuntu/jc2`:

```bash
sha256sum -c box/k16uniform-20260903/t4_charged_inputs.sha256
python3 box/k16uniform-20260903/t4_normalization_probe.py
python3 box/k16uniform-20260903/t4_affine_reduce.py
python3 box/k16uniform-20260903/t4_emit_exact_certificate.py
/usr/bin/time -f 'TIME_SEC=%e MAX_RSS_KB=%M EXIT=%x' \
  Singular -q box/k16uniform-20260903/t4_exact_Qsqrt15_nfmodstd.sing
```

The affine rerun is the long step (about 541 seconds in this run); the final
exact standard-basis computation takes under one second.

The entries in `t4_SHA256SUMS` use workspace-relative paths.  Verify that
manifest from `/home/ubuntu/jc2`, as in the reproduction block above.

## Principal artifact digests

```text
085aac73eafda284514bb2f10478f242d3535cca16ef7249043ed85b30a27faf  t4_normalization_probe.py
e903700fd21e3886816e3053fd7c6d79fcf33d86d9afb9877e3d36240c8aa683  t4_normalization_audit.json
eca6c7e0026703c7f17e22b750e7eb51cbd867a7d19b4b900c104db161202020  t4_normalized_rows.tsv
66463156f99204648456ddf0105273517b64252ce6e792f92c051d13b2a3591f  t4_affine_reduce.py
374674e76d58e27e154380c6823f3ed7c7b2caf90f40a94c21b4d6419014e05d  t4_affine_audit.json
42bfd85b39665717c6a885ba5c4b538f59020021b3ef9ad900bd06cb67db7312  t4_emit_exact_certificate.py
6b2f8f0eafe2792b99ede7d902504a34a9a8ce7096df7d948b441e97936421cf  t4_exact_Qsqrt15_nfmodstd.sing
cbd6bc9fb207011f86c325d7932274dd0104ac7c2b37fda9b69c0cbba6ed29cd  t4_exact_Qsqrt15_nfmodstd.out
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  t4_exact_Qsqrt15_nfmodstd.err
b0f7f23b877f1326baadbde1ed7942fbe1948d6e1155c7ca6312a1b7ce5c7806  t4_exact_Qsqrt15_nfmodstd.resource
983800a9fb64d8da035d705fe73d0f8a627869bd5cb1ec5cac4af4cb5cd1c8e4  t4_mod32003_subset_scan.out
7fc03fe2292ecdb3353367e8e0c7e3174564152d254a3a79431bd8ebedae854c  t4_mod32003_subset_scan.resource
```
