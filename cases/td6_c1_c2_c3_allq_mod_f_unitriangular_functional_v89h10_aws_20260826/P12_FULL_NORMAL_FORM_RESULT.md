# TD6 V89H12 all-q literal-P12 full-normal-form result

Date: 2026-08-26

Verdict: **PASS as an exact producer-tier normal-form theorem.**

## Exact scope

On the frozen V89H10T `F=0` specialization, work over the registered open
`D(U*H*B3)`.  Retain all 22 independent, untruncated q coordinates

```text
q2,...,q14,q16,...,q24
```

with q15 absent only as the reviewed target shear.  The R3 replay rebuilds
literal P12, consisting of 2,893 parameter terms, and all 38 literal packed
FIRST rows from the pinned source compiler.  No Singular qring is used.

## Complete FIRST quotient

The transported kernel has exactly 132 coordinates.  The frozen FIRST pivot
list has 38 distinct coordinates, leaving exactly 94 nonpivot coordinates:

```text
6,8,9,11,12,13,15,16,17,18,20,21,22,24,25,27,36,37,38,40,41,43,
44,45,47,48,49,50,51,53,54,55,56,58,59,60,61,62,64,65,66,67,68,
69,70,72,73,74,75,76,77,79,80,81,82,83,84,85,87,88,89,90,91,
92,93,94,96,97,98,99,100,101,102,104,105,106,107,108,109,111,
112,113,114,115,117,118,119,120,122,123,124,126,127,129.
```

The exact triangular recursion solves the constant FIRST equation and each
of all 94 nonpivot directions.  Every direction directly replays the
original 38-by-38 FIRST system.  The complete affine pivot-map artifact has
1,223 records and SHA256
`cc31df859f8142c00ed7da8858f9c1d4f8a19bc4a0cfe1ee27511a245987bb27`.
Its constant solution is q-linear, while every free-direction response is
q-independent.  Deleting an active pivot-direction contribution breaks the
original-FIRST replay, as required by the omission fixture.

## Complete P12 normal form

Exact substitution of the complete affine pivot map into every literal P12
term produces its unique normal form modulo the original FIRST module.  The
normal form has 166 nonzero `(parameter monomial, q monomial)` records,
parameter degree one, q degree one, and no mixed-q monomial.  The parameter
support is exactly

```text
(), (6,), (8,), (9,), (11,), (12,), (13,), (15,), (16,),
(17,), (18,), (20,), (21,), (22,), (24,), (25,), (27,).
```

Thus only 16 of the 94 quotient variables survive in P12; the other 78
directions cancel exactly.  The q support is exactly

```text
(), q2, q3, ..., q14.
```

In particular every coefficient of q16,...,q24 vanishes after the complete
literal reduction; those coordinates were retained throughout and are not
omissions.  The normal-form artifact has SHA256
`c8a738b6024ac02e56455674efa8c89c37684a87e0312141a5ca4259ca02e4c4`.
It is separately affine in the 16 surviving quotient variables and in q;
terms `q_e*y_j` are allowed, so this is not a claim of joint total degree
one.

The empty-parameter coefficient equals frozen V89H11 exactly, with SHA256
`530d3c78df4d1dd43a892976aede83bcc6aefd697a40be71a195e83cbc15a7f8`.
The complete pure-q14 class equals frozen V89H6 exactly, with SHA256
`56ebf08a3f9814f714920a4fcb3ae7fb0957db0c0f6d231382f9b5efbf3321a2`.
Deleting a nonzero literal-P12 contribution changes the result, as required
by the P12 omission fixture.

Equivalently, the P12/FIRST quotient problem in this exact scope now reduces
to 18 scalar equations involving only 16 effective quotient variables and
q2,...,q14.  This is a reduction theorem, not a common-zero verdict.

## Denominators and dual custody

Up to units, the common denominators are

```text
affine pivot map: U^7 V^4 (V^2-4U^3)^2
P12 normal form: U^5 V^4 (V^2-4U^3)^2.
```

Every factor belongs to the registered `D(U*H*B3)` radical; no additional
factor is inverted.  The denominator ledger has SHA256
`1ace2f9d73e63546b9ab5d15e12c61901b04e8819a46c9aa907a5df593090bd0`.

Independent R3 jobs on Box02 and r6d both returned rc 0, with byte-identical
stdout and every mathematical artifact.  Their stdout SHA256 is
`6ab1403c06dc6985bde2a0860f2a0092a6abe0140cea9fa0005aea9b01a2553e`.
Wall times were 7:31.63 and 7:26.40, maximum RSS was 297,032 and 297,336
KiB, and both runs reported zero swap.  The result artifact has SHA256
`1f843be94ebe5a5675bc0a1292a209b3773bbfe490ccd0ee249524ec2395a3c4`.

V1 lacked the required `TD6_Q_EXPONENT` wrapper variable and computed no
algebra.  R1 stopped after source compilation when its inherited 17-count
assertion met the corrected 94-coordinate inventory, before solving any
direction or reducing P12.  R2 did not start the client because its source
archive used the wrong filename case.  These three pre-result failures are
preserved by their immutable errata and evidence; only R3 supports the
mathematical theorem.

## Scope firewall

This producer theorem computes the complete canonical P12 normal form modulo
the original FIRST module only in the stated `F=0`, all-22-q scope.  It does
not prove that the 18 scalar equations have no common zero, prove a unit
ideal or source-point exclusion, cover a projective unit-q chart, license
q15 as a source coordinate, provide a total-Rees/source map, close TD6, or
resolve JC2.  All substantive computation ran on AWS.  `jc2-lean` was not
touched.
