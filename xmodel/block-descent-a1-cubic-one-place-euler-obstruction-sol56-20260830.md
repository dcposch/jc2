# Cubic block Euler obstruction from one-place branch components

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, independent audit lane  
Frozen basis: `adb7d06a166bd15f82203fcc1342cbb882a61764`  
Lifecycle: **EXACT PROVISIONAL THEOREM / `C=P1` CLOSED FOR EVERY PROPER CUBIC BLOCK**

## 0. Verdict

Assume the promoted proper-block sandwich for a hypothetical noninvertible
plane Keller map and specialize the finite-flat second leg to degree three:

```text
A2 --g1, etale quasi-finite dominant--> Y
   --g2, finite flat of degree 3--> A2.
```

Let `R=NonEt_Y(g2)_red`, `B=g2(R)_red`, `U=Y minus R`, and let
`rho:U->C` be the promoted `A1`-fibration.  Then the target branch has the
exact topological Euler number

```text
e_c(B)=b0(B)>=1.                                      (0.1)
```

The equality is not a generic source-to-target transfer.  Its load-bearing
cubic input is that a length-three fibre cannot contain two non-etale
points.  Thus

```text
R -> B
```

is finite and bijective, hence a homeomorphism on complex analytic spaces.
This eliminates the target conductor-gluing escape that is real in degrees
at least four.

Combining (0.1) with the frozen cubic Euler ledger

```text
e(U)=3-2e(B)-|S0|,
e(U)=e(C)+Q,                 Q=sum_t(q_t-1)>=0,
S0=A2 minus g2(U),
```

gives the complete alternatives

```text
C=P1:  2b0(B)+|S0|+Q=1,              impossible;

C=A1:  2b0(B)+|S0|+Q=2,
        hence b0(B)=1, S0=empty, Q=0.                (0.2)
```

Consequently every surviving proper cubic block has an affine ruling base,
connected affine target branch, an unramified block sheet over every target
point, and every reduced ruling fibre irreducible.  This is a conditional
proper-cubic-block theorem, not an exclusion of the remaining affine-base
row, an occurrence theorem for a block, or a conclusion about JC2.

## 1. Charged promoted inputs

The proof uses the following binding campaign inputs, with source and target
objects kept distinct:

```text
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md

f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md

94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d
  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md

7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md

b72e39220f9e8d75e94214d2e5669bda072fcbbd644cfed97f97d9a2b820ad57
  xmodel/block-descent-a1-euler-ledger-sol56-20260830.md
```

They supply: `Y` normal affine; `g2` finite flat; `R` nonempty and purely
divisorial; `g1:A2->U` an everywhere-defined dominant morphism; every SNC
completion boundary of `U` a rational forest; the fixed unramified sheet over
every target divisor; the finite set `S0`; and the two displayed Euler
identities.  The proof below adds the missing target-branch sign.

## 2. Exact external theorem and what it says

Nguyen Van Chau, *Note on the Jacobian condition and the non-proper value
set*, Annales Polonici Mathematici 84 (2004), 203--210,
DOI `10.4064/ap84-3-2`, proves the following for a polynomial Keller map
`F=(P,Q):C2->C2` with nonempty nonproper-value set `A_F`:

1. Theorem 1 gives a nonconstant polynomial parametrization of every
   irreducible component of `A_F`, with a common leading direction determined
   by the leading forms of `P,Q`.
2. Corollary 2 says that the **whole curve** `A_F` has one set-theoretic point
   at infinity.

The monic-coordinate display in Theorem 1 loses no generality: a generic
linear change of source coordinates makes both components monic in the same
source variable, and it does not change `A_F` in the target.

The two statements must not be conflated.  “One point at infinity” for the
whole reducible curve does not say that the whole curve has one analytic
place there; several component branches can meet that point.  The proof here
uses the polynomial parametrization component by component.  Corollary 2 is
recorded to settle the projective-language question, but it is not used to
transfer a forest from source to target.

Primary sources:

- published article DOI: `https://doi.org/10.4064/ap84-3-2`
- arXiv source with Theorem 1 and Corollary 2:
  `https://arxiv.org/abs/math/0305088`

## 3. Every component of `B` is exactly a component of `A_F`

The promoted block theorem gives

```text
B=g2(R)_red subset A_F.                                (3.1)
```

This is enough for equality componentwise, not merely containment.  Since
`R` is a nonempty pure curve and `g2` is finite, every irreducible component
of `B` is a one-dimensional irreducible closed subset.  The nonproper-value
set `A_F`, if nonempty, is a plane curve.  An irreducible component `B_i` is
contained in some irreducible component `A_j` of `A_F`.  Both are closed
irreducible curves, so equality of dimensions forces

```text
B_i=A_j.                                               (3.2)
```

This does not say that `B=A_F`; components caused only by the first-leg
nonproperness may remain outside `B`.

By Theorem 1, each `B_i` is the image of a nonconstant polynomial map from
`A1`.  Its normalization is therefore `A1`.  One quick proof is to lift the
map to the normalization and extend it to a nonconstant morphism from `P1`
to the smooth projective completion.  The latter has genus zero.  Every
puncture of the normalization must have all its preimages at the single
source point `infinity`; surjectivity of the completed curve map permits at
most one puncture, and affineness permits at least one.  Thus exactly one
point is deleted from `P1`.

## 4. The cubic source-to-target bridge

Fix `z in B(C)`.  The finite-flat fibre `Y_z` has scheme length three.  At a
closed point `y` of this fibre, flatness implies:

```text
g2 is etale at y  iff  the local geometric fibre factor at y is reduced,
                        equivalently it has length one over C.
```

Thus every point of `R` in the fibre has local fibre length at least two.
There cannot be two such points, because their lengths would sum to at least
four.  There is at least one because `z` lies in `g2(R)`.  Hence every closed
fibre of

```text
g2|R : R -> B
```

contains exactly one point.  After reduction the restriction is finite and
bijective on complex points.  A finite complex-algebraic morphism is proper
on analytifications, and a proper continuous bijection between locally
compact Hausdorff spaces is a homeomorphism.  Therefore

```text
R(C) homeomorphic to B(C),
e_c(R)=e_c(B),                  b0(R)=b0(B).            (4.1)
```

It also follows in characteristic zero that corresponding irreducible
components are birational.  Their normalizations agree, so every component
of `R` has normalization `A1` by Section 3.

This is exactly where degree three enters.  At degree four the fibre
partition `(2,2)` can have two source ramification points over one target
point.  Then a finite residue map can identify branches or components and
create target nodes/cycles.  No statement in this report transfers to that
case.

## 5. Forest Euler lemma on the source

Choose a projective compactification of `Y` and resolve the pair consisting
of the closure of `R` and the divisor at infinity.  This is a smooth
projective SNC completion of `U=Y minus R`.  The corrected morphic theorem
applies because the actual `g1:A2->U` is everywhere defined and dominant;
its full boundary dual **multigraph** is a forest.

Let `R_1,...,R_c` be the irreducible components of `R`.  Let `Sigma` be the
finite set of intrinsic affine singular points at which the normalization
has at least two preimages, and put

```text
r_p=#nu^(-1)(p),                   p in Sigma.
```

Form the affine incidence multigraph `Gamma_R`: its vertices are the `c`
normalization components and the points of `Sigma`, with one edge for every
branch over every `p`.  This graph is a minor, up to harmless edge
subdivision, of the resolved SNC boundary graph:

- over a singular point of the normal surface `Y`, the resolution fibre is
  connected and lies wholly in the boundary;
- embedded resolution separates all local branches;
- contract each connected exceptional cluster over `p` to the corresponding
  incidence vertex;
- delete infinity vertices and unibranch exceptional twigs.

A minor or subdivision of a forest is a forest.  Parallel branch edges are
retained; in particular, a self-node would already make a two-edge cycle.

Normalization additivity for compactly supported Euler characteristic gives

```text
e_c(R)=sum_i e_c(A1)-sum_(p in Sigma)(r_p-1)
      =c-sum_p(r_p-1).                                 (5.1)
```

Write `s=|Sigma|`, `E=sum_p r_p`, and let `h` be the number of connected
components of `Gamma_R`.  Since `Gamma_R` is a forest,

```text
E=(c+s)-h.
```

Substitution into (5.1) yields

```text
e_c(R)=c-E+s=h=b0(R).                                  (5.2)
```

Together with (4.1), this proves (0.1).  Notice that connectedness of a
projective target discriminant was never assumed.  The exact answer is the
number of connected components of the **affine reduced branch**.

## 6. Euler closure of the projective-base branch

The frozen degree-three fibre census is

```text
partition (1,1,1): z outside B, u(z)=3;
partition (2,1):   z in B minus S0, u(z)=1;
partition (3):     z in S0, u(z)=0.
```

The fixed-sheet theorem makes `S0` finite.  Euler integration gives

```text
e(U)=3-2e(B)-|S0|.                                     (6.1)
```

The ruling gives

```text
e(U)=e(C)+Q,       Q=sum_t(q_t-1)>=0.                  (6.2)
```

Insert `e(B)=b0(B)>=1`.  If `C=P1`, (6.1)--(6.2) demand

```text
2b0(B)+|S0|+Q=1,
```

whose left side is at least two.  Thus `C=P1` is impossible.  If `C=A1`,
the same equations demand

```text
2b0(B)+|S0|+Q=2.
```

All terms are nonnegative integers and `b0(B)>=1`, so the unique solution is

```text
b0(B)=1,        |S0|=0,        Q=0,        e(U)=1.     (6.3)
```

Since each `q_t>=1`, `Q=0` means every reduced fibre of the ruling consists
of one affine line.  Equation `S0=empty` means every target point has at
least one unramified block sheet; it does not make `g2|U` finite flat of
degree three over the branch.

## 7. Projective infinity and discriminant firewall

The object in (0.1) is the reduced affine curve `B=g2(R)_red`.  Its ordinary
projective closure `Bbar` cannot contain the line at infinity as an
irreducible component: every component of `Bbar` is the closure of an affine
component of `B`.  Chau's Corollary 2 says set-theoretically

```text
|Bbar intersect L_infinity|=1,
```

because `B` is a nonempty union of components of the whole `A_F`.

A different object can occur in a chosen class-`(3,3)` homogenized
binary-cubic presentation: its homogeneous discriminant divisor may acquire
`L_infinity` as a component when the leading binary cubic is everywhere
singular along infinity.  In that case the homogeneous divisor is

```text
L_infinity union Bbar
```

set-theoretically, possibly with multiplicities.  The extra line is not part
of affine `B`, is not charged in `e(B)`, and need not be the closure of any
affine source-ramification component.  If no such line component occurs, the
homogeneous reduced discriminant agrees with `Bbar` on support.  The proof of
Sections 3--6 is deliberately independent of both cases, of discriminant
multiplicities, and of projective basepoints.

## 8. Controls and exact scope

Three controls mark the load-bearing hypotheses.

1. A smooth `C*` boundary component has a one-vertex forest but Euler number
   zero.  Thus rationality plus forest is insufficient without the
   polynomial-parametrization/one-place input that makes each affine
   normalization `A1`.
2. The polynomial curve
   `t -> (t^2-1,t(t^2-1))`, with equation
   `y^2=x^2(x+1)`, has normalization `A1` and a self-node, hence Euler number
   zero.  Its embedded boundary resolution contains a cycle.  Thus the
   morphic forest input is genuinely load-bearing.
3. The degree-four partition `(2,2)` shows why a generic finite image of a
   forest divisor need not have forest topology.  Rank three, not the mere
   existence of a finite block, closes the conductor-identification escape.

Promoted by this report, conditionally on the charged proper cubic block:

```text
e(B)=b0(B)>=1;
C=P1 is impossible;
C=A1 forces b0(B)=1, S0=empty, Q=0.
```

Not proved: irreducibility or smoothness of `B`; absence of unibranch
singularities; a bound on the number of irreducible branch components;
projective basepoint-freeness of a class-`(3,3)` closure; exclusion of the
surviving affine-base topology; exclusion of a block of degree at least four;
existence of a proper block; a polynomial counterexample; or JC2.

## 9. Desk replay

The finite arithmetic is replayed by

```text
931afe2d89c890d841575780bf66c3625ae54e7aa51a275ef6f27da7fb0955f2
  ops/block_descent_a1_cubic_euler_replay.py
```

Ordinary, `python3 -O`, and `python3 -OO` runs were byte-identical.  Each
enumerated the cubic branch partitions `(3)` and `(2,1)`, checked 1,014
forest Euler rows, found the unique affine-base arithmetic solution
`(b0,|S0|,Q)=(1,0,0)`, found no projective-base solution, and printed

```text
payload_sha256=294c5674644c2b9de8a4a21be8391d1c2ee45f10d33b9aa846eb06107ecc7532
"result": "BD-A1-CUBIC-EULER PASS"
```

The two mutations fail with the intended diagnostics:

```text
--mutate-rank-four
  FAIL:cubic fibre length is not three

--mutate-drop-one-place
  FAIL:one-place normalization is required for forest Euler positivity
```

The replay checks only finite partition, graph-Euler, and terminal arithmetic.
It does not certify the external nonproper-value theorem, the promoted
morphic rational-forest theorem, or the geometric source-to-target proof.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13932`.
- Body SHA-256:
  `02cd6f89ee1e8505d2179636246552e76e0b4c3b9a9fa0196c5cef86dae1e62c`.
- Frozen basis: `adb7d06a166bd15f82203fcc1342cbb882a61764`.
