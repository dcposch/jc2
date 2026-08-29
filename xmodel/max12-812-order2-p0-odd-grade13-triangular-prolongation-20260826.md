# Order-two p=0 odd sheet: exact grade-13 triangular prolongation

Date: 2026-08-26

Status: **exact local source theorem, terminal grade 13 only**.  This note does
not establish the sheet-to-global algebraization Gate A and makes no finite
Taylor, order-two, or JC2 claim.

## 1. Scope and normalization

Work in the normalized p=0 odd sheet on `D(b*k0)`, with

```text
w=e1/b^2,                 k0=(12/5)w^2,                 b*w != 0.
```

The complete frozen terminal source retains the raw predecessor equation

```text
F = -(3/4)b^3 ell2 w^2 +(9/64)b rs1^2 w^2
    +(3/8)aa0 b^2 w -(3/8)a1^2 b +(3/8)a1 ee0.
```

No radical, saturation, unit lift, or global coefficient identification is
used below.

## 2. Exact collected grade-13 rows

Exact-Q sparse collection of the seven raw grade-13 rows gives

```text
G1 = -(9/4)b^2 cs1 ell2 w^2 -(3/4)b^3 ell3 w^2
     +(3/16)b^2 rs1 w^3 -(5/16)b^3 ell2 k10_1
     -(3/8)a1 b^2 w^2 +(9/64)cs1 rs1^2 w^2
     +(9/32)b rs1 rs2 w^2 +(15/256)b k10_1 rs1^2
     +(3/8)ac2 b^2 w +(3/4)b ee0 w^2
     -(3/4)a1 aa1 b -(3/8)a1^2 cs1 +(3/8)a1 ec3
     +(3/8)aa1 ee0 +(3/8)aa0 ee1,

G2 = -(3/8)b^3 cs1 w^2 -(9/16)b^2 ell2 rs1 w^2
     -(5/128)b^4 k10_1 -(3/8)a1 b^2 ell2 w
     +(3/256)rs1^3 w^2 +(3/16)b^2 ee1 w
     -(3/4)a1 aa0 b -(3/32)a1^2 rs1 +(3/8)aa0 ee0,

G3 = -(3/32)b^2 w (b rs1 w + 4 a1 b - 2 ee0),

G4=G5=G6=G7=0.
```

The four zero rows are exact cancellations in characteristic zero, not
sampled zeros.  The exact expansions agree with independent evaluations of
the unexpanded factor DAG in characteristics 32003 and 65521.

Neither `G2` nor `G3` belongs to the raw principal ideal `(F)` before the
other grade-13 equations are imposed, and `gcd(G2,G3)=1`.  These facts do not
make them obstructions: the full system is triangular.

## 3. Triangular prolongation theorem

Let

```text
R = Q[a1,aa0,aa1,ac2,ac3,az2,b,cs1,cs2,cs3,cs4,
      ec3,ec4,ee0,ee1,ell2,ell3,ell4,ell5,ez3,ez4,
      k10_1,rs1,rs2,rs3,rs4,rs5,w,(b*w)^(-1)].
```

In `R`, the raw ideal

```text
I13=(F,G1,G2,G3,G4,G5,G6,G7)
```

is triangular with pivots, in order,

```text
G3 : ee0   coefficient +(3/16)b^2 w,
F  : ell2  coefficient -(3/4)b^3 w^2,
G2 : ee1   coefficient +(3/16)b^2 w,
G1 : ac2   coefficient +(3/8)b^2 w.
```

Every pivot coefficient is a unit on `D(b*w)`.  Therefore every assignment
of the remaining 24 displayed variables has one and only one extension to
`ee0,ell2,ee1,ac2` satisfying all raw predecessor and grade-13 equations.
Equivalently, the raw quotient `R/I13` is the Laurent polynomial ring in the
remaining variables; in particular this localized raw ideal is prime and
reduced without taking its radical.

The first two pivot formulas can be written compactly as

```text
ee0 = 2 a1 b +(1/2)b rs1 w,

ell2 = [3 rs1^2 w^2 + 8 aa0 b w + 8 a1^2 + 4 a1 rs1 w]
       / [16 b^2 w^2].
```

After these substitutions, `G2=0` uniquely determines `ee1`; after that,
`G1=0` uniquely determines `ac2`.  Keeping `G1` and `G2` in the displayed
raw form is cleaner and safer than silently replacing them by denominator-
cleared solved formulas.

## 4. Computational custody

Frozen exact client manifest:

```text
cases/max12_812_order2_p0_odd_sheet_receivers_20260826/FREEZE_G13_EXACT.sha256
SHA-256 a6642e5e6781c27efa7970b42d8236a3e9c61251472c2a519be371ae4fbd3320
```

Registered AWS lane:

```text
max12_812_order2_p0_odd_g13_exact_q_20260826T101948Z_Box03
```

Validator endpoint:

```text
python_rc=0
singular_rc=0
validator=PASS_G13_EXACT_COLLECTION_REDUCTION
```

Key remote result hashes:

```text
grade13_exact_polynomials.json  b8b69b066fb6ff599489342fa1da21e8c296d64563057ee779fbdd6db5642e35
grade13_reduce_factor.sing      c01594c5c3a25150af713478abcf78cb08ea9ae433677477fb0871720ba097e9
result.json                     cad98c8ab66359d468525c86844475a9d72b164446902a7e97c9c3b433f9e920
Singular stdout                 4308f4ea1473e025efccde5f2d897dccc8f03d5e66987b498f161c48f139b7a1
validation                      24378b320cc2e33973e9deafde7d4d0b0217df0533ac1a65e48a09869455083a
```

## 5. Consequence and next gate

Grade 13 supplies no local terminal obstruction on the normalized odd
sheet.  The correct next local action is to substitute the four triangular
pivots into the complete raw source and inspect grade 14, continuing
horizontally without waiting for Gate A review.

Separately, Gate A remains fail-closed: local principal coefficients such as
`b,e1,w` have not been identified with global rational coefficient
functions or finite-branch jets.  The source deck action, terminal infinity
calculation, and typed Taylor pullbacks therefore cannot yet be combined
into a global contradiction.

## 6. Explicit nonclaims

This note does not claim:

- that the normalized odd sheet algebraizes to a global component;
- that a global rational square root `W^2=5k0/12` exists;
- that the deck action fixes or negates a single global `W`;
- that either finite Taylor pullback is compatible with this local chart;
- that grades 14 through 38 prolong;
- that the p=0 odd sheet is eliminated;
- that order two, the `(8,12)` slice, or JC2 is closed.

