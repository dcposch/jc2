# Hostile review — TD6 V89H15+H18 P13/FIRST coordinate-12 unit

| Field | Value |
|---|---|
| Target | Frozen H15 full P13 normal form, frozen H18 coordinate-12 producer, and the H15 vector-record-count erratum |
| Overall verdict | **CONFIRMED**, with the frozen erratum controlling the old H15 count terminology |
| Smallest mathematical failure | none |
| Corrected wording | H15 has 238 nonzero `(parameter,q)` E3-vector records and 535 nonzero scalar entries, not 238 scalar-coordinate terms |
| Reviewer | Sol, independent hostile source/custody/ideal audit |
| Method | Transitive SHA-256 verification; in-memory source-archive closure audit; static audit of the generic P13 compiler, FIRST solve, specialization, and substitution; independent parsing of both H15 TSVs and both H18 outputs; direct localized-ring argument. No heavy local replay and no Singular qring |
| Repo / HEAD | `/Users/dc/code/math/jc2` / `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

## Verdict

**CONFIRMED.**

On the frozen normalized three-center source slice

```text
p=t^15,
q=t + sum_{e=2..14,16..24} q_e t^e + t^25,
q15 absent only under the reviewed target shear,
F=C*U-V^2+U^3=0,
D(U*H*B3),
```

with all 22 displayed q coordinates algebraically independent and
untruncated, the exact normal form of literal CURRENT degree 13 modulo all 38
original FIRST rows has E3 coordinate 12

```text
(3500000000/9)*(U/V).
```

This coordinate is independent of all q variables and all 94 quotient
variables.  On `F=0`,

```text
B3 = V^4,
U*H = V^2-4*U^3.
```

Thus `U` and `V` are units on the registered open, and the displayed
coordinate is a unit in characteristic zero.  Consequently the literal
P13/FIRST system has no common zero on this exact normalized `F=0` slice.
P12 is not needed for this conclusion.

The conclusion is a quotient/no-common-zero theorem.  The package does not
emit original-FIRST membership multipliers, a denominator-cleared total-F
identity, or a total-Rees/source-cover theorem.  Those are certificate debts,
not defects in the scoped no-common-zero result.

## 1. Controlling custody

The combined H18 producer pins rehash exactly:

| Artifact | SHA-256 |
|---|---|
| `P13_COORDINATE12_UNIT_RESULT.md` | `0f152a88ba6422b04a3b4274ad5a0e71996c1c65395c7518b6e725321ab32d7f` |
| `P13_COORDINATE12_UNIT_EVIDENCE.sha256` | `bc9590017fb0f6942c9b7d396ba2b95e56fd1cbad2fc8c2b84e2b753bf79932d` |
| `P13_COORDINATE12_UNIT_FREEZE.sha256` | `0d3a9a6aad58635e9f02f160a3012b28dc351ecdbbafd97e59b7c1c2cda44974` |
| `P13_FULL_NORMAL_FORM_VECTOR_RECORD_ERRATUM.md` | `27d8289d7215d16806d1f1197b137acc7d49b0d75a05c766833eaaa38db44418` |
| H18 source archive | `a5b6f7306e4f1df434c53149d10d504332ca7266487cf0f854a83171ffc3d317` |
| H18 client | `00756bb30096442bfd76b2ecdfefb582e4121a2efb9a9c583e64e23df8e912b5` |

All 10 rows of the H18 freeze and all 22 rows of its combined evidence
manifest verify.  Each nine-row per-host harvest manifest verifies.  The H18
archive contains hash-correct copies of all six source-manifest inputs.

The upstream H15 pins also rehash:

| Artifact | SHA-256 |
|---|---|
| `P13_FULL_NORMAL_FORM_RESULT.md` | `29d5723b0d920840dbdfe72398624cfc0672843dbbf1d713b2fdd29dea52712c` |
| `P13_FULL_NORMAL_FORM_EVIDENCE.sha256` | `7c77bf767eea783d8d25a4c99c9201d039ed24d3a9037a1d2034accba569aa67` |
| `P13_FULL_NORMAL_FORM_FREEZE.sha256` | `4048419e15f366baeb03d242f546f096ee22d4529e6c6fededf58b2aea951c18` |
| H15 source archive | `2c13bd51601a64f3c2410bf4d36460f9f8741312aeef649299a22eb4fae3ff81` |
| H15 client | `6c06bed1dde0062d4eeed09b26f9cee11b10259f824fecd319fb3ae0c7a4fc7f` |
| complete P13 normal form | `9af3240d4016ad99766122303465d2cea7a10dc5e71b489f62564b9c3540c2d8` |
| affine FIRST solution map | `cc31df859f8142c00ed7da8858f9c1d4f8a19bc4a0cfe1ee27511a245987bb27` |

The following transitive manifests were checked row by row against the
working tree: H15 freeze 11/11, H15 evidence 46/46, H15 source 7/7, H12
freeze 16/16, H12 evidence 82/82, H12 source 12/12, H11 freeze 11/11, H11
evidence 48/48, H11 source 25/25, flag freeze 11/11, flag evidence 26/26,
flag source 18/18, graph freeze 9/9, graph evidence 34/34, graph source 16/16,
and payload closure 56/56.

The H15 archive was audited without extracting it.  Its 225 regular members
contain hash-correct `source/` copies of every row in `SOURCE_P13`,
`SOURCE_P12_FULL_NORMAL_FORM`, `SOURCE_P12_FLAG`, `SOURCE_FLAG`, and
`PAYLOAD_CLOSURE`; each such member also matches the corresponding working-
tree file.

H15's first two AWS launches stopped before algebra because system Python
lacked `flint`.  The successful R1 runs changed only `PATH`, returned rc 0 on
Box02 and r6d, and produced byte-identical stdout and mathematical artifacts.
The V1 deployment failures are not mathematical evidence.

## 2. H18 runs are custody, not a second P13 computation

Box02 and r6d both consumed the same frozen H15 TSV and the same H18 source
archive.  They returned rc 0 and byte-identical mathematical outputs:

| Output | SHA-256 |
|---|---|
| coordinate-12 TSV | `c5d136d942177882424a75a47c631fbd386d7fff6dbb09187effd32f1be4687f` |
| result text | `9df97904ea47f484494abf544bdf1dafbfeb9fe9352e88f4c3447c2599e185d4` |
| stdout | `bc5defb2ca6fa239fd24d35cb7f104006764363a9685125b2eca0032b7bf2519` |
| rc | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` (`0`) |

Their stderr differs only in timing/RSS counters; both report about 0.05 s,
zero swap, and exit status zero.  These runs independently validate archive
and parsing custody.  They do **not** independently recompile P13 or redo the
FIRST elimination.  The load-bearing algebra is the H15 construction audited
below.

## 3. Literal P13 and FIRST construction

The H15 `compile_current_degree(bands,13)` loop agrees term for term with the
frozen generic `compile_x_current` formula:

```text
 f1*g2' + 2*f2*g1' + 3*f3*q' - 3*p'*g3
-2*f1'*g2 - f2'*g1.
```

The generic degree-zero constant is irrelevant at degree 13.  The client
rebuilds the transport bands, requires both registered transport events,
requires each of the 22 q variables to be seen exactly once, obtains all 38
literal packed FIRST rows, and compiles all 2,757 literal P13 parameter terms.
No q value is sampled and no q or parameter support is truncated.  The raw
common denominator is exactly `U*H`, coprime to `F`.

After the exact chart `C=(V^2-U^3)/U`, the 132 transported-kernel variables
split into 38 distinct pivots and their complete 94-variable complement.  If
the FIRST equations are written

```text
A(q) x + D(q) y = r(q),
```

H15 reconstructs the frozen constant flag for
`N=A(0)^(-1)A(q)-I`.  In that basis `N` is strictly upper triangular, so the
triangular recursion uses only the registered base denominators and never
inverts a q polynomial.  It solves the constant equation and every one of the
94 direction equations, and then directly checks in the original FIRST
matrix that

```text
A(q) x0 = r(q),
A(q) x_j + D(q)e_j = 0   for all 94 j.
```

The resulting 1,223-record affine map has the same digest as reviewed H12.
This verifies the orientation and shows that the map is a parametrization of
the complete FIRST zero locus, not a projection onto a chosen subset of free
variables.

H15 then substitutes this complete affine map into every literal P13 term.
It scans all 2,757 terms, retains an active nonzero-contribution omission
fixture, and obtains a polynomial only in the 94 free variables.  The final
normal form has parameter degree one and q degree one; bilinear `q_e*y_j`
terms are allowed.  The common denominator factorizations are, up to rational
units,

```text
affine map: U^7 V^4 (V^2-4U^3)^2,
P13 NF:    U^5 V^4 (V^2-4U^3)^2.
```

All factors are registered on the specialized open.  The computation uses
custom exact `Rat3`/E3/`QPoly` arithmetic, not Singular qring assignment,
comparison, substitution, or differentiation.

## 4. Corrected record taxonomy and coordinate 12

I independently parsed both H15 host copies rather than relying on the H18
PASS banner.  Each TSV has 238 unique `(parameter monomial,q monomial)` keys;
each value is an 18-component exact E3 vector.  The two parsed tables agree
entrywise and have SHA `9af3240d...`.

Across the 238 vectors there are exactly 535 nonzero scalar components.
Coordinate 12 is nonzero in exactly one vector record:

```text
parameter monomial = ()
q monomial         = ()
coordinate 12      = ('3500000000/9*U', 'V')
```

Thus it is exactly `(3500000000/9)*(U/V)`, with no q or quotient-variable
dependence.  The old phrase “238 scalar-coordinate terms” in the immutable
H15 result is false terminology; the frozen erratum states the correct
238-vector/535-scalar census.  No TSV byte, algebraic coefficient, support
claim, or coordinate-12 consequence changes.  With that erratum controlling,
no further correction is required.

## 5. Localized ideal implication

Let

```text
S = Q[U,V,q2,...,q14,q16,...,q24]
    localized at U*V*(V^2-4U^3),
T = S[x1,...,x38,y1,...,y94].
```

Here the `x` are the FIRST pivots and the `y` are the complete nonpivot
coordinates.  Since `A(q)` is invertible over `S`, evaluation at

```text
x = A(q)^(-1)*(r(q)-D(q)y)
```

induces an isomorphism

```text
T/(FIRST_1,...,FIRST_38)  ~=  S[y1,...,y94].
```

H15 computes the image of the literal P13 E3 coordinate 12 under precisely
this evaluation, and H18 extracts it as `kappa*U/V`, where
`kappa=3500000000/9` is nonzero in `Q`.

The specialization identities follow directly by putting
`C*U=V^2-U^3` into the registered polynomials:

```text
U*H = C*U-3U^3 = V^2-4U^3,
B3  = V^4.
```

Therefore `D(U*H*B3)` is exactly sufficient to make `U`, `V`, and
`V^2-4U^3` units after `F=0`; no unregistered factor is inverted.  Hence
`kappa*U/V` is a unit of `S`, and

```text
(FIRST_1,...,FIRST_38,P13_coordinate_12) = T.
```

The ideal generated by the full 18-coordinate P13 vector contains this one
coordinate, so the full P13/FIRST common-zero locus is empty on the stated
slice.  The conclusion holds for arbitrary values of all 22 retained q
coordinates and all 94 quotient variables.

Equivalently, in the total localized ring before imposing `F`, the reviewed
quotient theorem implies the abstract membership

```text
1 in (FIRST_1,...,FIRST_38,P13_coordinate_12,F) localized at U*H*B3.
```

This last statement is an existence consequence of reduction modulo `F`.
The frozen package does not display its multipliers or a cleared polynomial
representative.

## 6. Certificate debt and scope firewall

The following are **not** part of the confirmed theorem:

- an emitted identity `s=a*P13_12+sum b_i*FIRST_i+F*h` with exact registered
  denominator exponent and source-row multipliers;
- a proof that raw P13 coordinate 12 is already the unit before FIRST
  elimination;
- a lift retaining independent total `F` as a base variable;
- q15 as an independent source coordinate rather than the reviewed target
  shear;
- omitted orbit, pole, correction, centering, boundary, or other TD6 source
  moduli;
- a two-sided total-Rees/source cover, whole-TD6 closure, or JC2 result.

The cheapest composable successor is the frozen raw-coordinate audit.  If
raw P13 coordinate 12 is already the displayed unit modulo `F`, only its
explicit F-quotient and denominator clearing remain.  Otherwise one should
track coordinate 12 alone through the existing affine FIRST solve and emit
the 38 original-row multipliers.  Neither task requires recomputing or
combining P12.

**CONFIRMED**
