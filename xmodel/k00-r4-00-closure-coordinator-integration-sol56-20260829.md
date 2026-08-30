# K00 V20R2 valuation four: coordinator integration closing `R4-00`

Coordinator: Sol 5.6  
Date: 2026-08-29 UTC  
Frozen campaign basis: `0f7ee003be45ee40d51d4048897cdacf63821172`  
Lifecycle: `PROMOTED EXACT R4-00 GRADE-19 EXCLUSION / COMPOSED NORMALIZED VALUATION-FOUR FINITE-JET EXCLUSION`

## Binding verdict

Promote the reviewed exact exclusion of CELL-R1+, CELL-R1- and CELL-R2,
with every correction below binding.  In fact the reviewer derived one
route-independent identity on the common forced `R4-00` stratum, so the
cell split is unnecessary for the terminal obstruction.

On the frozen normalized V20R2 source, over every characteristic-zero field,
write

```text
d = Lambda^4 ell(s,t) + Lambda^5 ell(s1,t1) + Lambda^6 z + ...,
ell(s,t) = (2s,t/8,s,t,s,2t),
```

and impose every literal coefficient equation `G_i,n=0` for
`1<=i<=7`, `8<=n<=19`, together with the source survival open
`Jdet_0!=0`.  There is no field-valued finite jet on `R4-00` through grade
19.  Equivalently its effective-rank-zero cell, both conjugate rank-one
branches, and its rank-two cell are all empty.

The standard exact-valuation-four packet also has `(s,t)!=(0,0)`,
`kappa=k10[0]!=0`, and the relevant rank-cell opens.  None of those opens is
used by the terminal identity; they remain part of the packet classification,
not hypotheses needed for the contradiction.

Composed with the already promoted reviewed rank fan and exact grade-15
`R4-02` exclusion, this yields the maximum finite-window statement:

> On the normalized frozen V20R2 support, there is no field-valued
> characteristic-zero exact-valuation-four jet satisfying all seven literal
> rows through grade 19 with `Jdet_0!=0` and the registered load/target
> constants.  This is a finite-jet exclusion on that support, not an arc,
> map, attainment, or JC2 theorem.

## Custody and promotion chain

The exact AWS producer is
`xmodel/k00-r4-00-r1-r2-exact-deciders-sol56-20260829.md`:

```text
full  4bd52f063289aa6dbd22b393ebec35cd90024b4ea2031a2fd21f227a5de65042
body  6e420952b432f6d22d676c98431cd7bc8842fe4c9ce8c28dca54828813862083
basis 792eecb189e754046fd3db054cefeae773f1a56d
```

Its lifecycle remains historical `PRODUCER-UNREVIEWED`; this integration,
not a rewrite of the producer, carries promotion.

Opus 5 independently performed the required hostile review in
`xmodel/k00-r4-00-r1-r2-exact-deciders-hostile-review-opus5-20260829-r1.md`:

```text
full  7082bf678825bd0b148b2a9b88ddfb7cdd7f8a9e166712188770ffad0a9ed270
body  8ff0abb2be95f93276c682b617a3be67be53105914d5b3093c30f874fd6c55ca
basis 9b64db896b65e100839f6d75fbeea661cd818b9c
verdict R2/R1+/R1- = CONFIRM_WITH_CORRECTIONS
```

The review rebuilt all 569 tails from the compiler conventions without using
the producer builder or packet polynomials as an oracle, inspected all 140
row/grade slots, matched every retained generator, independently derived the
identity by exact linear algebra, and ran fresh reviewer-owned AWS Singular
replays.  All three unit identities, seven cofactor-drop controls, a used-row
mutation, the `Jdet` localizer sign mutation, and cofactor-free standard-basis
checks passed.  No `msolve` result was consumed; characteristic-zero `[1]`
screens carry no theorem weight here.  No source, compiler, packet, cofactor,
or conclusion error was found.

Frozen packet/evidence custody is the 66-entry manifest
`cases/max12_812_order2_u2_62_k00_r400_exact_deciders_20260829/FULL_DECIDER_FREEZE.sha256`,
SHA-256
`a6e2b54fa0ca8ef3f96144d11c776a09d42175761be302745d02b8b14367ce79`.

## Exact eleven-equation proof

Put `Az=A(z)`, `Bz=B(z)`.  Three grade-12 equations give

```text
G3,12 + G1,12/8 = (3/16384) Az Bz,
G4,12             = (3/524288)(Bz^2-64Az^2).
```

Thus a field-valued solution has `Az=Bz=0`.  The corresponding grade-14
identities then give

```text
G3,14 + G1,14/8 = (3/16384) A7 B7,
G4,14             = (3/524288)(B7^2-64A7^2),
```

so `A7=B7=0` field-valuedly.  On this common forced stratum, with no rank
specialization or localization, the independently derived literal identity is

```text
Jdet_0 = -(s1/64) G1,14 -(s/64) G1,15
          -(5/256) G1,19 -(3/32) G3,19 -(1/2) G5,19 - 4 G7,19.
```

Hence the eleven imposed equations

```text
G1,12 G3,12 G4,12;
G1,14 G3,14 G4,14;
G1,15;
G1,19 G3,19 G5,19 G7,19
```

force `Jdet_0=0`, contradicting `Jdet_0!=0`.  The grade-12 and grade-14
substitutions are radical/field-valued steps, not equalities of the original
row ideal.  Accordingly the promoted statement is about field-valued points;
it makes no nonreduced scheme claim.  After those pointwise forcings, each
sealed substituted packet also has an exact rational unit identity with the
Rabinowitsch equation `1-Jdet_0*jinv`, independently replayed in a second
process.

## Corrections binding on consumption

1. The identity requires the grade-12 and grade-14 field-valued forcings, but
   it requires **no R1 or R2 route substitution**.  It holds before the
   effective-rank split.
2. It uses only the `Jdet_0` survival open.  The `D*kappa`, `q*kappa`, and
   `(s,t)` localizers have zero cofactors.  Do not advertise them as necessary
   hypotheses of the terminal contradiction.
3. The result is uniform on `R4-00` and therefore also kills CELL-R0 at grade
   19.  Retain the already promoted rank-zero result below because its
   grade-18 obstruction is sharper and it exhibits lifts through grade 17.
4. The producer's frozen replay drops a used **cofactor**; it does not mutate a
   generator.  The hostile reviewer separately tested both a cofactor drop
   and a generator mutation.  Consumption must use that corrected wording.
5. Load shifts and the `mu` target signs do not discriminate this certificate:
   their columns are free and the changes are relabellings.  This means the
   identity is independent of them; it is not a license to claim those
   mutations were detected.  Coordinate, stratum, live-tail, `Jdet` target,
   generator, cofactor, and localizer-sign mutations did discriminate.
6. The identity does **not** extend to the wider family with free transverse
   coordinates in `d[5]`.  The condition
   `d[5]=ell(s1,t1)` (`u5=v5=0`) is a real `R4-00` cell condition, not a
   consequence of earlier equations.  Any valuation-four-wide composition
   must consume the separately reviewed `R4-02` closure rather than silently
   widening `R4-00`.

## Composition with prior promoted cells

**R0 refinement.**  The sealed exact report
`xmodel/k00-r4-00-rankzero-closure-sol56-20260829.md` has full SHA-256
`2b299e652b0676f0fcfd6e780d61bab3c08602410c7a389045016284a2d6c66c`
and body SHA-256
`c073054c61ce1037fe01ccdd4dec03acbe6940775cf536246728d5eaa635ac38`.
On the effective-rank-zero cell it gives exactly three grade-14 rays, exact
lifts through grade 17, and a nonzero row-6 obstruction at grade 18.  This
lower-grade statement is retained.  The new grade-19 identity is redundant
there and does not replace the sharper first-obstruction claim.

**R4-02.**  The binding promoted integration
`xmodel/k00-r4-02-branch-closure-coordinator-integration-sol56-20260829.md`
has full SHA-256
`649943461185f1f580f069e76da4252daf207689ff5baa6dab2c05ba7c8f1bea`
and body SHA-256
`0e4dc8077e53fec6d69eb572db6e17ef3f2944fcd0736f2c7ffb9fbd37df888a`.
It excludes the old-plane next-rank-two `R4-02` cell at grade 15 over
characteristic-zero fields and, composed with the reviewed parent fan, leaves
`R4-00` as the sole integer valuation-four residual.

The parent fan integration
`xmodel/k00-r4-jetfan-coordinator-integration-sol56-20260829.md` has full
SHA-256
`bb6ebb1273865f92fec12313216bc36e66a36d7238b7eb988d813e84f7906839`
and body SHA-256
`75dce8299048dff7b36238a5c2dda9485e59b2e4e14826dfe29f963af8c0755d`.
It supplies the exhaustive reduced field-valued rank split.  The logical
composition is therefore exactly

```text
exact valuation four -> R4-02 or R4-00;
R4-02 -> empty by grade 15;
R4-00 -> empty by grade 19.
```

No claim is made outside those pinned packet definitions.

## Firewalls and nonclaims

This is `EXACT` evidence and `PROMOTED` lifecycle for reduced field-valued
finite jets on one normalized V20R2 support.  It does not decide nonreduced
scheme structure of the unsubstituted ideal, compatible infinite jets,
formal arcs, convergence, algebraization, polynomial Keller maps, another
support or valuation, a counterexample, or JC2.  Finite jets are not maps,
and a packet exclusion is not a global theorem.

The three long-running base-locus jobs on Box02/Box03 are diagnostic only and
were not consumed in this promotion.  They remain protected and running.
No canonical ledger, ideation file, or separate formalization instance was
edited, inspected, or controlled.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8708`.
- Body SHA-256:
  `26fbcfb5dc6fe4a8271bb9613aa6a0f3ee88cd7ff1513829fd57ec6f8516cc18`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
