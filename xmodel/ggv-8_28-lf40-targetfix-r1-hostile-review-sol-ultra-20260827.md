# Hostile review: GGV `8_28` LF40 target-fix R1

Date: 2026-08-27  
Reviewer: Sol Ultra, independent compiler-to-Singular audit  
Scope: mathematical target sign, target serialization, fresh AWS replay,
R0/R1 byte diff, row sequencing/counts, and validator semantics

## Verdict

**PASS TO RESTART on the R1 freeze; no blocker.**  The corrected program
encodes the required ideal, applies the inhomogeneous target exactly once,
and is byte-for-byte unchanged from R0 except for that correction and the
corresponding evidence-manifest digest.  R0 produced no mathematical verdict
and no R0 basis or result may be imported.

This verdict licenses restarting the preregistered producer lane.  It does
not promote any eventual Singular result, the GGV reduction, or a JC2 claim.

There is one nonblocking regression weakness: the compiler's new row-17
guard derives its expected string with the same `with_target()` function
that performs serialization.  It catches omission at the call site, but a
future sign mutation inside `with_target()` could satisfy the guard.  The
cheapest independent regression is specified below.

## 1. Independent target-sign derivation

The lower chart is

```text
x=tau^-4 xi,  y=tau,  f=tau^-8 F,  g=tau^-12 G.
```

Direct differentiation gives

```text
J_(x,y)(f,g)
 = tau^-17[-12 F_xi G + 8 F G_xi
            + tau(F_xi G_tau-F_tau G_xi)].
```

Consequently, for

```text
Dtil = 12 F_xi G - 8 F G_xi
       - tau(F_xi G_tau-F_tau G_xi),
```

one has `Dtil=-tau^17 J_(x,y)(f,g)`.  With the frozen orientation
`J(f,g)=1`, this is

```text
Dtil_17=-1,  Dtil_n=0 for n != 17.
```

Since Singular generators are set equal to zero, the constant coefficient
at row 17 must therefore be `Dtil_17+1`, not `Dtil_17-1` and not
`Dtil_17`.

The degree-zero determinant coefficient can also be recovered without the
chart formula.  The only nonproportional pairs at row 17 and `xi`-degree zero
are

```text
f_0_1*g_1_0  -> +1,
f_1_0*g_0_1  -> -1,
```

under the compiler's independently checked direct-coordinate sign
`-(i*l-j*k)`.  Thus the exact required solver generator is

```text
1+f_0_1*g_1_0-f_1_0*g_0_1.
```

The R1 output has precisely this sign.

## 2. Repair trace and exact-once check

`compile_lf40.py` keeps each `face_rows[row][degree]` as an untargeted
determinant polynomial.  Its R1 serializer now calls

```text
with_target(face_rows[row][degree], row, degree)
```

before `singular_poly(...)`.  `with_target()` first copies the sparse
polynomial and adds the numeric constant `+1` only when
`(row,degree)=(17,0)`.  It does not mutate `face_rows`, so later calls cannot
accumulate a second constant.

I independently parsed all three compressed row ledgers and the complete
generated Singular program.  The checks returned:

```text
41 rows
740 post-FACEPIN determinant generators
numeric constants in untargeted Dtil coefficients: none
numeric constants in target generators: exactly [(17,0,+1)]
Singular ROW_1,...,ROW_40: exact ordered match to all JSON `singular` fields
ROW_17 degree zero: 1+f_0_1*g_1_0-f_1_0*g_0_1
occurrences of that complete generator in the program: exactly 1
cumulative determinant count after row 40: 740
listed equations including Rabinowitsch: 741
```

The raw recurrence ledger and the disjoint direct-coordinate ledger also
each contain exactly the single target constant `(17,0,+1)`.  The frozen
row-17 digests are

```text
recurrence row 17  bf7b3522a63ea3008f886a8f99d0b4b182b3a66498e387944d9d3974c97e7ac9
direct row 17      03f985c5fc0d63f467315c285ffc61eefe636904f996b86d8fb2ff403a435d70
FACEPIN row 17     a6d7d9621b54292ba223d6534781eaeacad7db150e5ec6dffe6e61589c82bef7
```

This excludes an omitted target, a doubled target, a target on the wrong
degree, and a sign reversal in the present R1 artifact.

## 3. R0/R1 diff and AWS replay

The source-code diff from the immutable R0 archive to R1 has only two
logical changes:

1. apply `with_target()` at the Singular serialization boundary; and
2. abort unless the targeted and homogeneous row-17 strings differ and the
   targeted string begins `ideal ROW_17`.

The compiler SHA-256 is

```text
828f819e78ba36cf019e7014263148a4ee53ffd5b77ef77fee310637b82fc719
```

I rechecked the fresh output directly on AWS `r6b`, rather than relying only
on the harvested copy.  The staged compiler and output hashes there are
identical to the local frozen artifacts.  The replay printed
`PASS-LF40-COMPILER-CUSTODY`, exited `0`, took `5.31` seconds, used maximum
RSS `361512` KiB, and recorded zero swaps.  Every entry in the remote
`COMPILER_EVIDENCE.sha256` replayed `OK`.

An exhaustive old/new directory comparison found exactly two changed files:

```text
lf40_sequential_QQ.sing
COMPILER_EVIDENCE.sha256
```

The Singular content diff is exactly

```diff
-ideal ROW_17=f_0_1*g_1_0-f_1_0*g_0_1,
+ideal ROW_17=1+f_0_1*g_1_0-f_1_0*g_0_1,
```

and the evidence-manifest diff changes only that program's digest.  The
other eight compiler payloads are byte-identical, including the already
correct JSON row ledgers and compiler result.

Relevant R1 hashes are

```text
compiler result            84ae569bef4719cfabfafc0b8eb8a9e367a674b954e3edb903e3ef477faeb618
FACEPIN rows gzip          a83a9d6550107cdcc395fb21ea7e8fcfd5e9818042f2fbbd8edcf07220261ee1
Singular program           435c350f8a5be062d9b1e1b7cf57e9483dcf2648400fe250d4edbd13ccf846f7
compiler evidence manifest 787e934d35cf3d458d03f15fe299f475109d198b924851689f8246783411e8a0
R1 source-freeze manifest  70af56340845961625ce43945852da8f2350aa3d0a050532ca6138927d9c3298
R1 source archive          3895fa95022f1a894695f5e30ea7ae4f3ae62e423748956df791d0201aa42648
```

The R1 source freeze has 48 entries; all replayed `OK`.  Its archive has
those 48 files plus the freeze manifest itself, and no `jc2-lean` member.

## 4. R0 impact and containment

R0's program SHA-256 is
`73789f7d19362627b05823e3d8a0f6c24b9f9ea83aa23e496413fb87f6a6b382`
and visibly contains the homogeneous row-17 generator.  Its preserved packet
replays cleanly as custody evidence, but its terminal record is only

```text
status       DEPENDENCY_SOURCE_REPLAY_OR_ENGINE_FAILURE
solver rc    1
validator rc 90
```

with

```text
RESULT.json  b78e6aad20bd7880d278313e2b161d0a1b511d931518b16c89d687b3dbd0744a
EVIDENCE     9eef6aa288e52c9837c91642986d8f8bc2b58a251d313fd8f015de9bc065cca3
```

There is **no wrong mathematical conclusion to retract**.  At termination,
R0 had completed only row 0 and was still computing row 1, so it had not yet
inserted the faulty row-17 equation; those early prefixes happen to coincide
with R1.  However, it had no terminal verdict or reusable serialized basis,
and its full programmed ideal was wrong.  Retiring it and importing nothing
is the clean containment policy.

## 5. Adjacent serialization and validator audit

### Row 0

PASS.  Post-FACEPIN row 0 is asserted empty by the compiler.  The program
therefore starts from only the Rabinowitsch ideal, reports the row-0 stage,
and checks properness without declaring `ROW_0`.  The serialized JSON count,
program count, and validator expectation are all zero.  If row 0 were ever
nonempty, the current `if row > 0` logic would skip it, but the existing
`if face_rows[0]: fail(...)` makes that impossible for this frozen case.

### Row sequencing and cumulative counts

PASS.  The program declares every `ROW_1` through `ROW_40` exactly once and
emits all begin/end markers in order `0,...,40`.  The cumulative sequence is
the prefix sum of

```text
0,35,34,33,32,32,31,30,29,29,28,27,26,26,25,24,23,23,22,21,
20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0.
```

It ends at 740.  `ROW_40=0` changes no ideal; retaining it as a structural
row-ceiling marker while counting zero generators is consistent.

### Sequential ideal semantics

PASS.  At each positive row the program replaces the prior generator list by
its standard basis `G`, then forms `G+ROW_n`.  Since `G` generates the same
prior ideal, no constraint is dropped.  `reduce(1,G)==0` is the correct test
for the unit ideal.  The proper and forced-unit synthetic controls use the
same convention and fail closed.

### Validator

PASS for the frozen runner path.  It distinguishes resource-cap exits from
engine failures, requires exact field/variable/generator/Rabinowitsch
metadata, rejects missing headers, Singular fatal/question markers,
nonsequential completion markers, multiple inconsistency markers, a terminal
inconsistency together with a full-proper marker, and incorrect terminal
equation counts.  Its count convention is correct: 740 determinant
generators and one Rabinowitsch equation.

Two limitations are nonblocking because the AWS runner first regenerates the
compiler output and requires its entire manifest to be byte-identical:

1. the validator trusts `compiler_result.json` for target metadata and does
   not independently parse the Singular program; and
2. it does not compare every printed cumulative marker with the frozen prefix
   counts, although it does validate the completed-row sequence and terminal
   count.

## 6. Cheapest additional regression

Before the next compiler refactor, add one small, engine-free
`audit_lf40_serialization.py` and invoke it both after compilation and in the
AWS runner before Singular.  It should take the declared numeric target map
`{17: -1}` as its independent input, then:

1. parse `facepin_rows.jsonl.gz` and `lf40_sequential_QQ.sing`;
2. form every residual generically as `Dtil_coefficient - target`, rather
   than calling `with_target()`;
3. require the complete ordered equality of all 740 JSON residuals with all
   Singular `ROW_n` generators;
4. require the numeric-constant inventory to be exactly `[(17,0,+1)]`;
5. require row counts, the 41 cumulative markers, and the exact
   Rabinowitsch equation; and
6. run omission and sign-flip mutations, both of which must reject.

This closes the self-referential-guard gap at negligible cost.  It is not a
restart blocker for the already frozen R1 bytes, because this hostile review
performed that independent comparison and found an exact pass.

## Scope disclosure

The audit was confined to the named LF40 case, its frozen source reports, its
R0 packet, and the targeted AWS paths.  I did not read, list, status, build,
or modify `jc2-lean`, and no accidental traversal occurred.  The only file
created by this review is this report.
