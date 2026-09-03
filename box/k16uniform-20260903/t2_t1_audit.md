# Frozen-input audit: normalized `t=2` system and `t=1` control

Date: 2026-09-03. Scope: only the frozen inputs in
`/tmp/jc2-lane.fjoTgL/inputs`. This note does not edit the requested main
report and does not use any prohibited in-progress lane report.

## Verdict

The proposed literal fixed residual pattern is false already at `t=2`.
The grading and weighted normalization do persist, and `H_2` has degree two,
but

```text
H_2(y)=25*y^2-15*y+2=(5*y-1)(5*y-2),  disc(H_2)=25.
```

Thus `Q[y]/(H_2)` is not a quadratic field. It is a squarefree étale algebra,
and field-only divisions would be unsound. Performing only divisions by
elements whose inverses were checked modulo `H_2`, or equivalently treating
the two rational fibers separately, gives twelve affine eliminations and four
residual generators in two chart unknowns, from bands `h=0,1,2,3`, of degrees
`9,8,7,6`. Both fibers have exact reduced basis `[1]`.

There is also a syntactic obstruction to the proposed literal residual tuple:
the safe gauge at `t=2` is `alpha_t=alpha_2=0`, so the chart contains no
variable `a2_0` at all.

The `t=1` row retains the positive grading and an irreducible quadratic
`H_1`, but after four coefficient-field affine eliminations it contains an
explicit nonzero coefficient-field constant. Hence its normalized ideal is
already the unit ideal. It does not have the `t=3` six-generator/three-variable
shape either.

## 1. Mechanical input gate

The manifest
`box/k16uniform-20260903/t2_t1_charged.sha256` was generated mechanically from
the receipt's paired `charged_input_<i>_basename=` and
`charged_input_<i>_sha256=` fields with `awk`, then checked by

```text
sha256sum -c box/k16uniform-20260903/t2_t1_charged.sha256
```

All fifteen frozen inputs reported `OK`. No digest was retyped to construct
the manifest.

The main audit driver is
`box/k16uniform-20260903/t2_t1_normalized_audit.py`; its complete exact record,
including all source row tags, weights, pivot coefficients, checked inverses,
substitution images, dropped rows, and final generators, is
`box/k16uniform-20260903/t2_t1_normalized_audit.json`.

## 2. Exact `t=2` normalization

### 2.1 Frozen chart agreement and constant pivots

The frozen generalized driver and frozen dedicated `t=2` driver agree on
parameter order, `h,A,B,z,P,Q`, and every ordered tagged equation. There are
37 tagged equations, with common expression-vector SHA-256

```text
b260a69d40c772f198c618c758d57d38ccb8a3b2c11eba11b94066edd39a5803.
```

The frozen constant-pivot algorithm makes ten quotient-ring isomorphisms,
all with coefficients in `Q*`. It maps the original 37-row, 27-chart-unknown
system (counting `c`) to 26 rows in 17 chart unknowns (again counting `c`).
The pivot bands are `9,8,7,7,6,6,5,5,4,4`; the complete map is checked on
every original generator, not only on the pivot rows. The surviving variables
and the mechanically recovered primitive positive weights are

```text
b1:1, b2:2, b3:3, b4:4,
a1_0:4, a3_0:12, a4_0:16, a5_0:20, a6_0:24,
q2_0:8,
q3_0:12, q3_1:9,
q4_0:16, q4_1:13,
q5_0:17, q5_1:18,
c:45.
```

The monomial-difference matrix has 614 rows, rank 16, and nullity one. Every
one of the 26 residual equations is homogeneous for this grading.

### 2.2 The two exact distinguished rows

Put

```text
x=q3_1,  y=q5_1.
```

Source row 2 (zero-based; band `h=0`, remainder monomial `gamma`) gives

```text
c = 7*x*y*(x^2-10*y)/125.
```

Source row 14 (band `h=2`, remainder monomial `gamma*pi`) is a nonzero rational
associate of

```text
Hhom_2(x,y)=2*x^4-15*x^2*y+25*y^2.
```

Since `c != 0`, the first identity forces `x != 0`. Over the algebraic closure,
choose `lambda` with `lambda^9*x=1` and apply the verified action
`v -> lambda^wt(v)*v`. Homogeneity makes this an existence equivalence, and
the normalized slice is

```text
x=1,
H_2(y)=25*y^2-15*y+2,
c=-7*y*(10*y-1)/125.
```

The two roots and corresponding Jacobian constants are

```text
y=1/5,  c=-7/625;
y=2/5,  c=-42/625.
```

Both are nonzero. Consequently the normalized saturated locus is exactly the
union of these two rational fibers; no conjugate or specialization is lost.

### 2.3 Affine reduction and exact residual generators

After solving the `c` row, there are 25 raw rows. Primitive `Q*` normalization
and literal duplicate removal leave 21 rows. The base relation vanishes in
the quotient, leaving 20 rows in 14 auxiliary chart unknowns.

Over the full squarefree algebra `Q[y]/(H_2)`, twelve successive pivots have
explicit inverses modulo `H_2`; every substitution is checked modulo `H_2`.
Four further rows become zero. The result is four generators in `(b3,b4)` from
bands `0,1,2,3`, with total degrees `9,8,7,6`. Their exact common-algebra
coefficients are recorded under
`.audits["2"].split_slices.etale_slice.final_generators` in the JSON audit.

For an independently transparent exact check, the two rational fibers were
reduced separately. On `y=1/5` a deterministic affine choice leaves variables
`(b4,a3_0)` and the following primitive integer generators, in band order
`0,1,2,3`:

```text
283924375*b4^9 + 93940000*b4^6*a3_0
  + 7680000*b4^3*a3_0^2 + 50176,
335013*b4^8 + 77056*b4^5*a3_0 + 3072*b4^2*a3_0^2,
329*b4^7 + 64*b4^4*a3_0,
1953*b4^6 + 352*b4^3*a3_0.
```

On `y=2/5`, the surviving variables are `(b3,b4)` and the primitive integer
generators are

```text
2682059061670*b3^2*b4^3 - 834139815825*b3*b4^6
  + 2446170279750*b4^9 + 2535731817423,
30500078563*b3^2*b4^2 + 17702528580*b3*b4^5
  - 59091781800*b4^8,
287156086*b3^2*b4 - 27046560*b3*b4^4 + 106639425*b4^7,
1189646642*b3^2 + 304374720*b3*b4^3 - 1207034325*b4^6.
```

Exact Singular `std` in characteristic zero returns `[1]` on both systems:

```text
MAIN_START t=2 y=1/5 rows=4 unknowns=2
MAIN_DONE basis_size=
1
MAIN_BRANCH_EMPTY
G[1]=1

MAIN_START t=2 y=2/5 rows=4 unknowns=2
MAIN_DONE basis_size=
1
MAIN_BRANCH_EMPTY
G[1]=1
```

The corresponding inputs are `t2_normalized_y_1_5.sing` and
`t2_normalized_y_2_5.sing`. Each run passes the declared-ring check, empty and
nonempty wrapper controls, extracted-ideal type/ring checks, and the exact
actual-pair Jacobian convention control.

### 2.4 Full-chart replay

The frozen generalized emitter was also run without preprocessing. In
`Q[26 chart parameters,c]`, it extracts the `c`-saturation component from the
returned `sat()` list, asserts its type and ring, and obtains

```text
MAIN_START equations=37 chart_unknowns=27 characteristic=0
MAIN_EXTRACT_RING_PASS
MAIN_DONE basis_size=
1
MAIN_SATURATED_EMPTY
G[1]=1
```

All wrapper and actual-pair controls pass. This is an independent fresh replay
of the already promoted fixed-`t=2` result; the structural branch calculation
above is not needed to re-prove that fixed result.

## 3. Exact `t=1` control

### 3.1 Grading and slice

The generalized gauged `t=1` chart has 23 equations and 18 chart unknowns
including `c`. Seven constant-`Q*` pivots leave 15 rows in 11 chart unknowns.
The 127 monomial-difference constraints have rank 10 and nullity one. The
positive weights are

```text
b1:1, b2:2, b3:3, b4:4,
a2_0:8, a3_0:12,
q2_0:8, q2_1:5,
q3_0:9, q3_1:10,
c:25.
```

Writing `x=q2_1` and `y=q3_1`, the exact distinguished rows are

```text
c = 4*x*y*(x^2-9*y)/81,
Hhom_1(x,y)=5*x^4-36*x^2*y+54*y^2.
```

The `c != 0` condition forces `x != 0`; weighted normalization with
`lambda^5*x=1` gives

```text
H_1(y)=54*y^2-36*y+5,  disc(H_1)=216,
c=-4*y*(9*y-1)/81.
```

The discriminant is nonsquare, so
`K_1=Q[y]/(54*y^2-36*y+5)` is a field. Exact inversion gives

```text
c^(-1) = 2187*y/5 - 2187/10  (mod H_1).
```

### 3.2 Early unit and failure of the fixed residual shape

Solving the `c` row gives 14 raw rows; exact duplicate removal leaves 12, and
removing the minimal-polynomial row leaves 11 rows in eight auxiliary
unknowns. Four checked affine eliminations over `K_1` pivot

```text
q3_0, b4, b2, a3_0.
```

One more row reduces to zero. Among the six displayed survivors is the
coefficient-field constant

```text
20*y-10/3,
(20*y-10/3)^(-1)=27/10-27*y/5  (mod H_1).
```

It is therefore a unit. The surviving row tags, before replacing the unit by
`1`, have bands `0,0,0,0,1,2`, remaining variables
`(b1,b3,a2_0,q2_0)`, and degrees `1,2,0,2,2,1`; the degree-zero band-0 row is
the displayed unit. The intrinsic final ideal is simply `[1]`, not a six-row
system in three unknowns from bands `0,...,5`.

The normalized Singular control checks `c`, the terminal constant and their
displayed inverses, runs empty/nonempty wrapper checks in both declared system
rings, and returns

```text
CONTROL_C_UNIT_PASS
CONTROL_TERMINAL_UNIT_PASS
MAIN_DONE basis_size=
1
MAIN_T1_EMPTY
G[1]=1
```

The full unpreprocessed gauged chart independently returns
`MAIN_SATURATED_EMPTY`, `G[1]=1`, with all `sat()` extraction, ring, wrapper,
and actual-pair controls passing. This is consistent with the charged Moh
`(16,12)` control, though it is the uniform generalized gauged chart (18
unknowns), not a claim that Moh printed this exact basis or this preprocessing.

## 4. Semantic and FALLACY-v2 controls

The exact semantic control is

```text
(F,G)=(pi,pi-gamma^2/2),  J(F,G)=gamma.
```

The frozen `k16_symbolic.py` additionally checks that both reciprocal Lemma
anchor degrees are two while the `pi`-degrees are `(1,1)`. Thus it passes the
monomial-Jacobian/Lemma-shape check but fails the K16 four-tuple classifier; it
is not inserted into either K16 chart.

The audit observes the relevant FALLACY-v2 guards:

- `sat()` list components are extracted and asserted in the full-chart runs;
  normalized runs have `c` already proved a unit and still run positive and
  negative wrapper controls in their declared rings.
- Monic `h`-division is inherited unchanged from the frozen generator; no
  coefficient leader is divided out and no zero-leader branch is discarded.
- Every constant-pivot quotient map is checked on every original tagged row.
  Every normalized affine coefficient has a displayed, verified inverse in
  the declared field or étale algebra, and every substitution is checked.
- The reducible `H_2` quotient is never called a field and no zero divisor is
  inverted. The two rational fibers provide an independent branch check.
- This note asserts no exit set or exit price, so no `charge_basis` line is
  due.

## 5. Reproduction commands and limitations

Principal commands, from `/home/ubuntu/jc2`, were

```text
sha256sum -c box/k16uniform-20260903/t2_t1_charged.sha256
python3 box/k16uniform-20260903/t2_t1_normalized_audit.py \
  > box/k16uniform-20260903/t2_t1_normalized_audit.out \
  2> box/k16uniform-20260903/t2_t1_normalized_audit.err
Singular -q box/k16uniform-20260903/t2_normalized_y_1_5.sing
Singular -q box/k16uniform-20260903/t2_normalized_y_2_5.sing
Singular -q box/k16uniform-20260903/t1_normalized_unit.sing
python3 /tmp/jc2-lane.fjoTgL/inputs/t_order_system.py \
  --t 1 --gauged --emit-singular
python3 /tmp/jc2-lane.fjoTgL/inputs/t_order_system.py \
  --t 2 --gauged --emit-singular
python3 /tmp/jc2-lane.fjoTgL/inputs/k16_symbolic.py
```

This audit proves only the fixed `t=1,2` structural statements above. It does
not infer an all-`t` Gröbner certificate from these samples. Residual generator
sets also depend on the chosen sequence of valid affine coordinates; the
reported full-étale `t=2` count is for a deterministic, audited unit-pivot
algorithm, while the two branch presentations give separately checked
coordinate choices. The invariant negative conclusions are stronger: `H_2`
is reducible, `a2_0` is absent at `t=2`, and a valid reduction exists with only
four rows in two chart unknowns. Therefore the literal claimed fixed
six-row/three-unknown/bands-`0..5` pattern cannot be the uniform theorem.

<!-- BODY-END -->
