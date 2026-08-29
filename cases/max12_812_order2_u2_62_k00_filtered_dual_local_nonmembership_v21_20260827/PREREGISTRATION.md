# Preregistration: V21 filtered-dual implication for V17 local nonmembership

Date: 2026-08-27

Status: **DEPENDENCY-ORDER REPAIR FROZEN AFTER V18R2 EVIDENCE, BEFORE THE
INDEPENDENT REPLAY CHARGED HERE.**

## Exact corollary charged

Put

```text
R=Q[d0,...,d5],  m=(d0,...,d5),
J_X=(r1,...,r6)+E_X,
D_X=h*a7^X-sum_i u_i*a_i^X,
```

for `X in {K10,K6,K2}` and the frozen V17 exact source.  The provisional
V18R2 exact packet contains rational left functionals at cutoffs

```text
K10:D=4,   K6:D=3,   K2:D=2
```

which claim to annihilate the complete image of `J_X` in
`R/m^(D+1)` and to pair nontrivially with `D_X`.

The charged corollary is

```text
D_X notin (J_X)_m
```

for all three directions.  These are exactly the three `LOCAL_NONZERO`
mathematical conclusions requested by V17.

## Lemma

If `D in J_m`, then there is `s in R` with `s(0)!=0` and `sD in J`.
The class of `s` in `R/m^(Dcut+1)` is a unit, so

```text
D in J+m^(Dcut+1).
```

Consequently any exact functional on `R/m^(Dcut+1)` which annihilates the
complete truncated multiplication image of `J` and is nonzero on `D`
proves `D notin J_m`.  This implication does not require a colon standard
basis.

## Mandatory fresh replay

The V21 producer must run on registered AWS and independently:

1. hash-gate the frozen exact V17 source, V14R1 rows/relation, V18R2 result,
   all three exact matrices, row/column maps, rational duals, `IMAGE_X`,
   `TARGET_X`, and the serialized 66-generator six-row module;
2. replay every serialized syzygy against `r1,...,r6` over `Q` and verify
   equality with a freshly computed full `Syz(r1,...,r6)` in both module
   directions;
3. rebuild every `E_X` from all 66 syzygies and all six exact load rows,
   and compare it generator-by-generator with `IMAGE_X`;
4. rebuild every `D_X` from `h,u_i` and all seven exact load rows and compare
   with `TARGET_X`;
5. independently parse the exact polynomials, enumerate every monomial
   multiplier allowed at the charged cutoff, and re-emit each sparse
   augmented Macaulay matrix byte-for-byte, including row and column maps;
6. replay `y^T M=0` and the nonzero exact pairings
   `25/45056`, `45/11264`, and `-25/352`; and
7. emit the lemma application separately for each direction.

A hash mismatch, incomplete multiplier census, syzygy/image/target mismatch,
failed module equality, failed dual replay, engine diagnostic, timeout, or
resource-cap event is `NO_VERDICT`.

## Dependency repair and firewall

V18R2 preregistered an administrative `no-promotion-before-V17-Q` gate
because it originally consumed the modular V17 branch as navigation.  V21
supersedes only that dependency order: its fresh exact source and dual replay,
together with the displayed lemma, supplies the exact local-nonmembership
conclusions directly.  It does not change the V17 or V18 definitions.

The live monolithic V17-Q colon job remains an independent cross-check until
this corollary is frozen and hostile-reviewed.  Agreement is desirable but
is not logically needed by the lemma; disagreement is a mandatory stop and
audit.

The corollary concerns three separate first-order load classes in the
normalized unloaded K00 coefficient-local ring.  It does not couple them,
restore their honest Lambda weights, include targets/Jdet through order 19,
prove an arc obstruction, decide closure incidence, or imply order two,
maximum twelve, or JC2.

