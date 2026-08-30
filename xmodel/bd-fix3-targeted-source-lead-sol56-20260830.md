# `BD-FIX3` targeted external-source lead: affine-linear Miranda data

Coordinator: Sol 5.6 Ultra  
Date: 2026-08-30 UTC  
Frozen campaign basis: `0d7544ebd5cb12def6bac892646010301098be3c`  
Lifecycle: **TARGETED SOURCE LEAD / INTERNAL DEDUCTION / REVIEW REQUIRED / NO PROMOTION**

## 0. Verdict

A targeted lookup prompted by the new review-gated `BD-GAL` producer found a
public 2026-07-24 MathOverflow question that studies finite-flat normal
degree-three covers of `A2_C` with affine-linear Miranda data:

```text
https://mathoverflow.net/questions/513574
```

The post is not a JC2 result and currently has no answer.  It supplies a
detailed proof sketch, not a peer-reviewed source.  Its claimed trichotomy
would nevertheless close most of the **affine-linear Miranda subfamily** for
the Keller block sandwich after one short additional observation: any
nonconstant unit on the full etale complement restricts to a unit on the
dense `A2` source chart, hence becomes constant, contradicting injectivity.

One affine-linear case remains untouched by that observation.  In the
post's notation it is

```text
W != 0,   S_X=empty,   Ram(g2) irreducible,
```

where the post derives only `H_c^1(Ram(g2),Z) != 0`.  That topological fact
does not contradict an open `A2` chart contained in the etale locus.  Thus
this source is a useful scoped discriminator and a possible sign of external
activity around the same low-degree-cover perimeter, not a proof of
`BD-FIX3`, primitivity, or JC2.

## 1. Primary and public sources

The load-bearing primary reference is Rick Miranda, *Triple Covers in
Algebraic Geometry*, Amer. J. Math. 107 (1985), 1123--1158:

```text
https://www.math.colostate.edu/~miranda/preprints/TripleCoversInAG.pdf
```

Miranda proves that a finite flat degree-three cover has a rank-two
Tschirnhausen module and gives the coordinate-free and local multiplication
data.  Over `A=C[u,v]`, trace splitting and Quillen--Suslin make that module
free.  With trace-zero basis `(z,w)`, the MathOverflow post uses the standard
four-coefficient table

```text
z^2 = 2(a^2-bd) + a z + b w,
zw  = -(ad-bc) - d z - a w,
w^2 = 2(d^2-ac) + c z + d w,
```

equivalently the binary cubic

```text
Phi = b X^3 - 3a X^2Y + 3d XY^2 - c Y^3.
```

The public post assumes `a,b,c,d` affine-linear in `(u,v)`, writes
`Phi=P0+uP1+vP2`, and analyzes the incidence surface and ramification
divisor.  It claims

```text
( O(U)^*/C^*, Cl(U), H_c^1(D,Z) ) != (0,0,0),
U=Y minus D,   D=Supp Ram(g2).
```

No public note or repository was linked as of this lookup.  The argument
must be reconstructed before use; the present packet charges no theorem to
the MathOverflow post.

## 2. Exact Keller-sandwich consumer of a unit output

Assume provisionally the promoted block structure and let

```text
A2 --g1--> Y --g2 finite-flat degree 3--> A2
```

be a proper intermediate sandwich.  Put `R=NonEtale(g2)` and
`U=Y minus R`.  The promoted theorem gives

```text
g1(A2) subset U,
g1(A2) open and dense in Y,
O(A2)^*=C^*.
```

If `q in O(U)^*` is nonconstant, then `q o g1` is a unit of `C[x,y]`, hence
a scalar `c`.  Since `g1` is dominant, the induced ring map

```text
O(U) -> C[x,y]
```

is injective.  (No open-immersion or degree-one claim about `g1` is made.)
Therefore `q=c` already in `O(U)`, contradiction.  This is
the same constant-unit mechanism as the exact `BD-GAL` missed-principal-
divisor lemma, now applied to the etale complement rather than to `Y`.

Consequently every affine-linear subcase in which the public argument truly
produces a nonconstant unit on `U` is incompatible with a proper Keller
block sandwich.  This deduction is exact conditional on that unit output;
it does not need `g1(A2)=U`.

## 3. Claimed affine-linear partition and the residual

The public proof sketch routes its cases as follows.

| Miranda-data case | claimed output | Keller-sandwich use |
|---|---|---|
| `a,b,c,d` have a common zero | finite class group forces a boundary-divisor relation | nonconstant unit on `U`; killed by section 2 |
| `W!=0`, `S_X` nonempty | affine-line torsor analysis | nonconstant unit on `U`; killed if reconstruction confirms it |
| `W!=0`, `S_X=empty`, `D` reducible | `Cl(Y)` has rank one but boundary group rank at least two | nonconstant unit on `U`; killed if reconstruction confirms it |
| `W!=0`, `S_X=empty`, `D` irreducible | only `H_c^1(D,Z)!=0` | **OPEN**; no contradiction with an `A2` subchart |
| `W=0` | product reduction and boundary relation | nonconstant unit on `U`; killed if reconstruction confirms it |

The residual case is load-bearing.  A nonzero `H_c^1(D,Z)` is a property of
the deleted ramification curve, not a nonconstant unit or divisor class on
the source chart.  It must not be converted into an obstruction to
`g1(A2)` without a new exact sequence or embedding theorem.

The post's global trichotomy is correspondingly weaker than the unit theorem
needed here: if only the third entry is nonzero, the Keller sandwich has not
been contradicted.

## 4. Interaction with the new block theorem

The review-gated `BD-GAL` producer adds constraints absent from the public
question:

1. every branch component has an unramified generic sheet;
2. cubic divisorial inertia is therefore a transposition, never a 3-cycle;
3. the cubic extension is non-Galois;
4. `Y` is nonfactorial and the finite-flat algebra is nonmonogenic; and
5. the actual source chart is an etale open `A2` whose image misses all of
   `R`, but need not equal `U`.

The next desk gate should insert these constraints into Miranda's binary
cubic table and revisit the single residual affine-linear case.  In
particular, it should determine whether irreducible ramification together
with fixed-sheet transposition inertia forces a principal ramification
equation or a nonconstant unit.  If not, the residual is a faithful scoped
control and the affine-linear family remains only partially closed.

Beyond affine-linear `a,b,c,d`, the source supplies a representation, not a
degree bound.  No inference to arbitrary cubic covers is licensed.

## 5. Scope and next action

This was a targeted source lookup, not the scheduled broad web sweep.  It
found no external proof or disproof of JC2.  The public calculation is
unanswered, its proof is not independently verified here, and its author is
not identified with any JC2 team.

The cheapest successor is a hostile reconstruction of the five-row table in
section 3 using Miranda's primary multiplication formulas, followed by the
residual test with fixed-sheet inertia and the constant-unit source chart.
Until that passes, label the claimed affine-linear closure `REVIEW_GATED` and
the full `BD-FIX3` problem `OPEN`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6700`.
- Body SHA-256:
  `b9a7003049aebb23ffbfa084ab67a827d9ee5d618d0891ae50d1d52cf01dd3f7`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
