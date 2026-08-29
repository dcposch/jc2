# TD6 V89H15 all-q literal-P13 full-normal-form result

Date: 2026-08-26

Verdict: **PASS as an exact producer-tier normal-form theorem.**

## Exact scope

On the frozen V89H12 `F=0` specialization, work over the registered open
`D(U*H*B3)`.  Retain all 22 independent, untruncated q coordinates

```text
q2,...,q14,q16,...,q24
```

with q15 absent only as the reviewed target shear.  The R1 replay rebuilds
literal CURRENT degree 13 from the same generic `compile_x_current` formula
used at degree 12, producing 2,757 literal parameter terms, and rebuilds all
38 literal packed FIRST rows.  No Singular qring is used.

## Complete FIRST quotient

The replay reconstructs the frozen 38-pivot/94-nonpivot common FIRST flag.
It solves the constant equation and every one of all 94 quotient directions,
then directly replays every solution in the original 38-row FIRST matrix.
The complete affine pivot map has 1,223 records and SHA256
`cc31df859f8142c00ed7da8858f9c1d4f8a19bc4a0cfe1ee27511a245987bb27`,
exactly the reviewed V89H12 map.

## Complete P13 normal form

Exact substitution into all literal P13 terms, without parameter or q
truncation, gives a complete normal form with SHA256
`9af3240d4016ad99766122303465d2cea7a10dc5e71b489f62564b9c3540c2d8`.
It has 95 nonzero parameter-support records and 238 nonzero scalar-coordinate
terms.  Its parameter support is exactly the empty monomial plus every one
of the 94 quotient-variable singletons.  Its q support is exactly

```text
(),q2,...,q14,q16,...,q24.
```

The normal form is separately affine in quotient variables and in q, has no
mixed-q monomial, and can contain bilinear `q_e*y_j` terms.  Every
quotient-variable coefficient is supported only in E3 coordinates 0 and 1.
The empty-parameter coefficient is supported in all coordinates 0 through
17.  Consequently coordinates 2 through 17 give 16 exact, y-independent,
affine-linear compatibility equations in the 22 q variables; only the first
two coordinates retain quotient-variable freedom.

Deleting one nonzero literal P13 contribution changes the output, as required
by the omission fixture.  The result artifact has SHA256
`6ad11dd35dbc8df9689e4da5dc076c1d33a566867864b8f85127415554b223a5`;
the exact support artifact has SHA256
`edf5a6702d0f2c5d1c8b026bb428af020c4257f581863d349906ffacfd73f7e4`.

## Denominators and dual custody

Up to units, the common denominators are

```text
affine pivot map: U^7 V^4 (V^2-4U^3)^2
P13 normal form: U^5 V^4 (V^2-4U^3)^2.
```

Every factor belongs to the registered `D(U*H*B3)` radical; no additional
factor is inverted.  The denominator ledger has SHA256
`6ad157b3e9212bbe8c2dd139cf84e71b78930ceea988b34cbed4b67cd507e0c7`.

Independent R1 jobs on Box02 and r6d both returned rc 0.  Their stdout and
every mathematical artifact are byte-identical.  Their timing-only stderr
differs in wall-time, RSS, and scheduler counters.  Wall times were 6:59.82
and 6:59.74, maximum RSS was 296,972 and 297,232 KiB, and both reported zero
swap.  The evidence manifest has SHA256
`7c77bf767eea783d8d25a4c99c9201d039ed24d3a9037a1d2034accba569aa67`.

The first dual launch used the same frozen source archive but selected system
Python, which lacked `flint`; both processes stopped during import before any
transport, FIRST, P13, specialization, or normal-form algebra.  R1 changed no
source byte and only prepended the frozen AWS virtual environment to `PATH`.
The pre-import failure is preserved in
`P13_FULL_NORMAL_FORM_V1_ENVIRONMENT_ERRATUM.md`.

## Scope firewall

This theorem computes only the complete canonical P13 normal form modulo the
original FIRST module in the stated `F=0`, all-22-q slice.  It does not yet
combine P12 and P13, determine whether their 22 y-independent compatibility
equations have a common q, produce a literal source point or total-Rees map,
impose later CURRENT grades, close TD6, or resolve JC2.  All substantive
computation ran on AWS.  `jc2-lean` was not touched.
