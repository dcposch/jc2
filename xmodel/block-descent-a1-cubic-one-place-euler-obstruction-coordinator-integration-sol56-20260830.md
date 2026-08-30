# Binding integration: cubic one-place Euler obstruction

Date: 2026-08-30 UTC  
Integrator: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `4607fefa25b31d039404ced367ee77d1d482cc90`  
Disposition: **PROMOTE WITH EXPLICIT FIXED-SHEET DEPENDENCY**

## 0. Binding verdict

Promote the rank-three one-place Euler theorem after repairing the hostile
review packet's sole dependency omission.  For an actual proper cubic block

```text
A2 --g1--> Y --g2--> A2,       deg(g2)=3,
R=NonEt_Y(g2),                 U=Y minus R,
B=g2(R)_red,
```

the reduced ramification map is finite point-bijective and hence a complex
analytic homeomorphism

```text
R_red -> B.                                             (0.1)
```

Every irreducible component on either side has normalization `A1`.  The
affine incidence multigraph of `R` is a forest, and therefore

```text
e_c(B)=e_c(R)=b0(B)>=1.                                (0.2)
```

Combining (0.2) with the promoted `A1`-ruling and cubic sheet census gives

```text
C=P1:  2*b0(B)+|S0|+Q=1,                    impossible;

C=A1:  2*b0(B)+|S0|+Q=2,
       hence b0(B)=1, S0=empty, Q=0.                   (0.3)
```

Thus the complete-base ruling is empty for every actual proper cubic block.
The affine-base branch survives, but with connected reduced branch and
ramification support, an unramified block sheet over every target point, and
one reduced `A1` component in every ruling fibre.

The hostile review returns `CONFIRM_WITH_CORRECTIONS`.  Its only mathematical
gate was deliberately procedural: the review prompt did not charge the
already-promoted fixed-sheet integration, so the reviewer correctly stated
its theorem conditionally.  The coordinator rechecked and explicitly binds
that different-model-confirmed input below.  No unreviewed replacement is
being smuggled into the proof.

## 1. Evidence and repaired dependency closure

```text
8b457a752434ac0c7cb6a2a83dd680b4a66dbe3631ab761c43dc789965ff2d2d
  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-sol56-20260830.md
f98149567b865f15a97b1e53c8f1ccd15fde116292e2d0c64a2935d3c45d95ae
  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-sol56-20260830.md.artifact.json

e544a654d3cead096658502f34b0e6e5560b4a0ea8bf97a53b2a76081aceda4d
  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-hostile-review-gpt55-20260830.md
  raw body b16c4bc1ed5756ad39db1f44bc1bdf0fb462de9a0afdc5a5285ae27e712b4fe1

f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d
  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
b72e39220f9e8d75e94214d2e5669bda072fcbbd644cfed97f97d9a2b820ad57
  xmodel/block-descent-a1-euler-ledger-sol56-20260830.md
```

The fixed-sheet theorem in `f9720718...` was already independently reviewed
and promoted.  For every irreducible target divisor, at least one component
of its inverse image is generically unramified.  The proof applies the missed-
principal-divisor lemma to a defining prime `p`: if every component above
`V(p)` were ramified, then the principal divisor of the same element `p` in
the literal intermediate ring would be wholly missed by `g1`, which is
impossible because its pullback to `A2` would be a nowhere-zero nonunit
polynomial.  Residue degrees are retained; geometric inertia fixes
`sum_(e_i=1) f_i>=1` block sheets.  Consequently the no-unramified-sheet set
`S0` has no divisorial component and is finite.  This closes exactly the
reviewer's stated gap and nothing more.

Root reproduced the external lane's receipt, composed prompt, Seatbelt
profile, adapter, launcher, validator, appendix, report, log, and every
charged hash before reading it.  Receipt status `charge_basis_status=ABSENT`
is correct because the review asserted no exit price.  The report was sealed
against basis `f86884a5ab78e5248977942f93547fbf25b5be8e` before custody
commit `4607fefa`.

## 2. Rank-three topology bridge

At a closed source point over a smooth complex target, finite flatness gives

```text
g2 etale at y  <=>  the local fibre factor at y has length one. (2.1)
```

A non-etale point therefore consumes length at least two.  Since the total
fibre length is three, a branch value has exactly one reduced source point in
`R`.  This remains true at a singular point of normal `Y`: length one would
make the finite-flat local algebra etale and hence its source regular.

The restriction `R_red->B` is finite and bijective on closed points.  After
analytification it is a proper continuous bijection between locally compact
Hausdorff spaces, hence a homeomorphism.  This proves (0.1), but not a scheme
isomorphism: cusp normalization and conductor data remain legitimate.  In
characteristic zero the corresponding components are birational and have
the same normalizations.

The inequality `2+2>3` is load-bearing.  At rank four, a `(2,2)` fibre can
contain two reduced ramification points, and target conductor identifications
can change the topology.  No degree-at-least-four statement is promoted.

## 3. One-place components and the forest Euler identity

Every component of `B` is an entire irreducible component of the Keller
nonproper-value curve.  Nguyen Van Chau's published theorem gives a
nonconstant polynomial parametrization of each such component.  Passing to
the normalization and projective completion shows that its affine
normalization is `A1`.  This is componentwise: the whole possibly reducible
nonproper-value curve merely has one set-theoretic point at infinity and may
have several analytic branches there.

Resolve the closure of `R` together with infinity and the singularities of
normal `Y`.  The affine incidence multigraph of `R`, retaining self-nodes and
parallel edges, is obtained from the actual morphic strict-SNC boundary
forest by minors, subdivisions, and vertex deletions.  It is therefore a
forest.  If `c` is the number of normalized `A1` components, `Sigma` the
affine multibranch points, `r_p` the number of normalization branches at
`p`, and `h=b0(R)`, normalization additivity and the forest identity give

```text
e_c(R)=c-sum_(p in Sigma)(r_p-1)=h.                   (3.1)
```

Together with (0.1), this proves (0.2).  Unibranch cusps cause no Euler
defect; a self-node creates parallel incidence edges and is forbidden by the
forest.  The rational-forest input is licensed only by the actual everywhere-
defined morphism `g1:A2->U`, never by abstract rational domination.

## 4. Euler closure and exact meaning of the survivor

With the promoted fixed sheet, the rank-three fibre census is

```text
(1,1,1) off B:       u(z)=3;
(2,1) on B-S0:       u(z)=1;
(3) on finite S0:    u(z)=0.
```

Hence

```text
e(U)=3-2*e(B)-|S0|.                                  (4.1)
```

The ruling identity is

```text
e(U)=e(C)+Q,       Q=sum_t(q_t-1)>=0.                 (4.2)
```

Equations (0.2), (4.1), and (4.2) give (0.3).  In the affine-base survivor,
`S0=empty` means there is at least one unramified **block** sheet at every
target point; it does not identify an original source sheet or make
`g2|U` finite flat of degree three over the branch.  `Q=0` says every reduced
ruling fibre has one `A1` component; it does not prove scheme-reducedness,
multiplicity one, or absence of special fibre values.  Connectedness is for
the reduced affine branch/ramification topology.

## 5. Maximum-safe conclusion and successor

For an actual proper cubic block satisfying the promoted sandwich, fixed-
sheet, morphic-forest, and `A1`-ruling theorems, the ruling base cannot be
`P1`.  If it is `A1`, then necessarily

```text
b0(B)=1,       S0=empty,       Q=0.
```

This is a proper-block discriminator, not an exclusion of the affine-base
survivor, not a degree-four theorem, not a block-existence theorem, and not a
proof of JC2.  The cheapest successor is to combine the unique affine ruling
with the rank-three local splitting over the connected branch, the class
group of `U`, and multiple-fibre/Kummer constraints.  That successor must
keep ruling fibres, branch components, unramified companion sheets, and
original source sheets distinct.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8528`.
- Body SHA-256:
  `0d77db42a859fb280ba02c3b2351a668ed52d6e53bd580e2faef1d185480c1fd`.
- Frozen basis: `4607fefa25b31d039404ced367ee77d1d482cc90`.
