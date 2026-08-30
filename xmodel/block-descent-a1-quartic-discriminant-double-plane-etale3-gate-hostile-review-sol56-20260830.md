# Hostile review: rank-four discriminant double-plane étale-cubic gate

Date: 2026-08-30 UTC  
Reviewer: Sol 5.6 Ultra (`double_plane_hostile_review` lane)  
Frozen basis: `7afc73b69182b7fc7b33b1153bb945469668f00e`

Frozen producer:

```text
xmodel/block-descent-a1-quartic-discriminant-double-plane-etale3-gate-sol56-20260830.md
full SHA-256     1939c55467f5795c5bb3a264f5516c666c82e34849bc4d74f190c95d18a016bb
body SHA-256     4b1a7bf4b829fb2bf653a5421375d8caac159491c3a0986df0428e0b5f77c285
manifest SHA-256 5544c05bee8ffeab1791084d7d58b70ca6a45d44079efcc2f8d4535834da0216
```

Review status: **INDEPENDENT SAME-MODEL HOSTILE REVIEW; NOT A
DIFFERENT-MODEL PROMOTION REVIEW**.

## 0. Verdict

**CONFIRM AS STATED.**  I independently reconstructed the field tower, the
normal models, every local stabilizer, the codimension-two extension issue,
the nodal units/class-group calculation, and the two positive controls.  I
found no mathematical error in the producer's maximum-safe conclusions.

In particular, in the charged minimal rank-four row:

```text
m=0  =>  W -> D is a connected finite étale C3-torsor,
          0 != alpha in H^1_et(D,Z/3), iota^*alpha=-alpha;

m=1  =>  W -> D has an A3 stabilizer over the unique (3,1) value
          and is only quasi-étale there.
```

There is no hidden ramification at a singular point in the `m=0` row: the
argument checks geometric stabilizers at every closed point, not merely
divisorial inertia.  There is also no `Pic=Cl` substitution in the nodal
control: the proof uses only the valid injection `Pic(D0)->Cl(D0)`.

Two phrases merit conservative interpretation, but no producer edit is
needed.  The "local residue" in the `m=1` discussion means the nontrivial
class on a punctured strict-henselian neighborhood, not a divisor-valued
residue map.  And the displayed class-group presentation is a Nagata
calculation whose absence of extra relations uses the preceding unit
calculation; it is not being inferred from `div(u)` alone.

The result remains an exact gate, not a rank-four exclusion: nothing in the
review proves vanishing for every allowed one-place double plane or constructs
an actual surviving block.

## 1. The `S4/V4` tower and the normal quadratic model

Let `A=C[x,y]`, `K=Frac(A)`, and let `Omega/K` be the charged `S4` Galois
closure.  The action of `S4` on the three perfect matchings has kernel the
normal Klein four group.  The even permutations map to the alternating
subgroup on those three matchings.  Therefore

```text
S4/V4=S3,             A4/V4=A3=C3,
M=Omega^V4,           K2=Omega^A4=M^A3.
```

The minimal row has transposition inertia at the generic point of every
component of the reduced branch `B`.  Its image in `S3` is again a
transposition, and the sign quotient is ramified to odd order on precisely
those components.  If `q_B` is the product of their pairwise nonassociate
reduced equations, then the square class defining `K2/K` differs from `q_B`
by a rational function with even valuation at every height-one prime.  Since
`A` is a UFD, that function is a constant times a square.  Every nonzero
complex constant is a square, so

```text
K2=K(sqrt(q_B)).
```

Put `R=A[s]/(s^2-q_B)`.  It is a domain because `q_B` has an odd valuation
and hence is not a square in `K`.  Being a hypersurface, `R` is Cohen--Macaulay
and satisfies `S2`.  At the generic point of a component of `B`, the base is
a DVR and `q_B` has valuation one, so adjoining `s` gives a DVR.  Away from
`B` the quadratic algebra is étale over a regular ring.  Thus `R` is regular
in codimension one and Serre's criterion makes it normal.  Consequently

```text
D=Spec R
```

is exactly the normalization of `A2` in `K2`; singular intersections or
cusps of `B` occur only in codimension two and do not spoil normality.

If `S` is the normalization of `A` in `M`, then `S` is finite and normal and
`S^A3` is finite normal with fraction field `K2`.  Hence `S^A3=R`.  This
proves, without assuming a classical resolvent equation is normal, that

```text
W=Spec S,             W/A3=D,
```

and `W->D` is a connected finite degree-three quotient because `M` is a
field.

## 2. Complete local stabilizer audit

Fix a closed target point `z` and a geometric point `w` of `W` above it.
All residue fields are `C`, so the stabilizer of `w` in `S3` is its
decomposition group `H_z`.  Its stabilizer for the subgroup acting in
`W->D` is exactly

```text
H_z intersect A3.
```

For a finite constant group in characteristic zero, the quotient is a torsor
at a point exactly when the geometric stabilizer is trivial.  Checking all
closed points therefore detects codimension-two ramification as well as
divisorial ramification.

Write the three matchings as `12|34`, `13|24`, and `14|23`.  The quotient map
`q:S4->S3` has

```text
q((12))=q((34))=a transposition.
```

The four local cases reconstruct as follows.

1. A `(2,1,1)` point has one two-sheet orbit and two fixed sheets.  Its local
   group lies in the corresponding `S2`, and in the branch case its image is
   `C2`.  Its intersection with `A3` is trivial.
2. A `(2,2)` point has two two-sheet orbits, so its local group lies in
   `<(12),(34)>`.  The two charged local meridians give the two disjoint
   transpositions, while their images under `q` coincide.  Thus the image is
   `C2` (and, for freeness, the weaker containment in `C2` already suffices),
   again with trivial intersection with `A3`.
3. At a finite `(3,1)` point the local group is transitive on three sheets
   and fixes the fourth.  It contains a divisorial transposition, so it is
   `S3`, not `C3`.  Its image under `q` is all `S3`, whose intersection with
   `A3` is `A3`.
4. At a `(4)` point the corrected charged theorem leaves local group `A4` or
   `S4`; their images are respectively `A3` and `S3`, both with nontrivial
   `A3` intersection.

Off `B` the decomposition group is trivial.  In the `m=0,n4=0` row these
cases exhaust every closed point, including unibranch singular points whose
quartic fibre still has type `(2,1,1)`.  The `A3` action on `W` is therefore
free everywhere, and the finite quotient

```text
W -> D
```

is an étale `C3`-torsor.  This is the decisive reason no singular-point
ramification has been overlooked.

In the `m=1,n4=0` row, the unique `(3,1)` point instead has full `A3`
stabilizer.  Deleting its unique image point on `D` and its preimage in `W`
leaves an étale `C3`-torsor.  The source remains connected because it is a
nonempty open subset of the integral normal surface `W`.  At the deleted
point the action is fixed, so normalization cannot extend that punctured
torsor étale across the singularity.  This independently confirms the
producer's quasi-étale, not étale, conclusion.

## 3. Cohomology class and the codimension-two gate

In the `m=0` row, integrality of `W` makes the étale torsor connected.  The
zero class in `H^1_et(D,C3)` is the split union of three copies of `D`, so its
class `alpha` is nonzero.  Choose a transposition in `S3` lifting the deck
involution `iota` of `D/A2`.  Conjugation by that transposition sends a
generator of `A3` to its inverse.  Pullback of the monodromy character hence
gives

```text
iota^*alpha=-alpha.
```

After choosing a cube root of unity, `C3` is identified with `mu3`.  The
Kummer sequence (three is invertible) gives exactly

```text
0 -> O(D)^*/O(D)^{*3}
  -> H^1_et(D,Z/3)
  -> Pic(D)[3]
  -> 0.
```

Thus constant units would force a nonzero anti-invariant `3`-torsion line
bundle, while nonconstant units remain a genuine alternative.

For a normal surface, a finite étale cover is determined by its restriction
to the regular locus, but not every cover of the regular locus extends
étale.  Normalizing in its function field extends it finitely; étaleness is
equivalent to triviality on each punctured strict-henselian neighborhood of
a singular point.  The producer correctly retains this local condition.
The ordinary-cusp model `UV=X^3` displays the failure: `A2->A2/mu3` is free
off the origin and fixed at the origin.  The weighted affine cone is
contractible, so comparison over `C` gives no nontrivial finite constant
étale torsor on the whole cone even though its punctured locus has the
expected connected cubic cover.

## 4. Nodal control: units, `Cl`, and `Pic`

For the named nodal branch, the substitutions `u=y+w`, `v=y-w` give

```text
R0=C[x,u,v]/(uv-x^2(x+1)).
```

The only singular point is `(x,u,v)=(0,0,0)`, so this hypersurface is `S2`
and regular in codimension one, hence normal.  Localizing at `u` gives the
UFD

```text
R0[1/u]=C[x,u,u^(-1)]
```

with unit group `C^* u^Z`.  The height-one primes containing `u` are

```text
P0=(u,x),             P1=(u,x+1),
```

and DVR valuations give

```text
div(u)=2P0+P1.
```

If an element of `R0` is a unit, its image in the localization is `c u^n`;
its Weil divisor is zero, so the displayed nonzero divisor forces `n=0`.
Therefore `R0^*=C^*`.

Nagata's localization sequence says that `Cl(R0)` is generated by `P0,P1`.
The kernel is the image of `R0[1/u]^*/R0^*`; the unit computation shows this
image is generated by `(2,1)` and supplies no second hidden relation.  Hence

```text
Cl(R0)=Z^2/<(2,1)> ~= Z.
```

For a normal integral scheme, Cartier divisors inject into Weil divisor
classes, so `Pic(D0)->Cl(D0)` is injective.  The producer does not identify
the two groups.  Since the latter is torsion-free, `Pic(D0)[3]=0`; since
`C^*=(C^*)^3`, Kummer now gives

```text
H^1_et(D0,Z/3)=0.
```

The nodal control is therefore genuinely excluded by the double-plane gate.

## 5. Independent reconstruction of the positive controls

For `w^2=x^2-1`, put `t=x+w`.  Then `t^{-1}=x-w`, so the double plane is
`Gm_t x A1_y`, and adjoining a cube root of `t` is a connected étale cubic
cover.  Its two-line branch is disconnected and lies outside the horn, but
it correctly refutes universal odd-cohomology vanishing for affine double
planes.

For the connected control, let

```text
p(T)=T^3+xT+xy+1,
Delta=-4x^3-27(xy+1)^2.
```

The parametrization

```text
x=-3r^2,             y=(1-2r^3)/(3r^2)
```

has inverse `r=-3(xy+1)/(2x)` on `Delta=0`; that curve has no point with
`x=0`.  Thus the branch is smooth and isomorphic to `Gm`, so `Delta` is
reduced, irreducible, and nonsquare.  A triple root would require both
`x=0` and `xy+1=0`, which is impossible.  Over `C(x)`, solving `p(T)=0` for
`y` gives the degree-three rational map

```text
T |-> -(T^3+xT+1)/x.
```

Hence `[C(x,T):C(x,y)]=3`, proving that the cubic is irreducible.  Its
nonsquare discriminant therefore gives Galois group `S3`.

The proposed closure

```text
W1: a^3+b^3-3aby+1=0,
x=-3ab,
```

is smooth: its three first derivatives can vanish only with `ab=0`, which
then forces `a=b=0`, contrary to the constant term.  The `mu3` action
`(a,b)->(zeta a,zeta^(-1)b)` has the same impossible fixed locus.  Its
invariant ring is generated by `C=ab`, `y`, and `d=a^3-b^3`; using
`a^3+b^3=3Cy-1` gives

```text
d^2=(3Cy-1)^2-4C^3.
```

After `x=-3C` and a nonzero complex rescaling of `d`, this is exactly
`s^2=Delta`.  Thus `W1->D1` is a connected finite free `C3` quotient, hence
étale.  Swapping `a,b` supplies the complementary transposition and recovers
the full `S3` closure.  This verifies the producer's sharp negative control;
its branch normalization is `Gm`, not the charged `A1`.

## 6. Replay and custody audit

The producer and manifest verify transactionally:

```text
producer full SHA-256  1939c55467f5795c5bb3a264f5516c666c82e34849bc4d74f190c95d18a016bb
producer body SHA-256  4b1a7bf4b829fb2bf653a5421375d8caac159491c3a0986df0428e0b5f77c285
producer manifest SHA  5544c05bee8ffeab1791084d7d58b70ca6a45d44079efcc2f8d4535834da0216
producer replay SHA    2ce87f135a1e91da8e43bc5e4cf3e37ce29f27cff6c6aacabdd08c4b75a1cde8
```

I reran the replay under ordinary Python, `python3 -O`, and `python3 -OO`.
All three outputs are 896 bytes and byte-identical:

```text
stdout SHA-256 66ecf7bae2685fb6c379fef27cbcad006cc513d2b1b32af700a3821411119745
status=PASS-QUARTIC-DISCRIMINANT-DOUBLE-PLANE
payload_sha256=e5bd7a7fc837d40a7aa604c1b213964c2b7e91e9f09d95cf1a996f674960fafb
```

An AST walk finds zero Python `Assert` nodes.  The mutation
`--mutate-cusp-as-etale` exits nonzero at the explicit requirement that the
cusp packet have nontrivial `A3` stabilizer.  Independent symbolic reduction
also reproduces the cubic discriminant and the invariant relation
`d^2=(3Cy-1)^2-4C^3`.

As the producer says, the replay checks finite permutation and polynomial
identities only.  It does not prove normality, the torsor criterion, Kummer,
Nagata localization, or irreducibility; those steps were reconstructed in
Sections 1--5 above.

## 7. Disposition

Safe to bind, subject to the campaign's separate different-model review
policy, are exactly:

1. the connected étale cubic and nonzero anti-invariant class forced by the
   `m=0` minimal cyclic-`S4` row;
2. failure of étaleness at the unique `(3,1)` point in the `m=1` row;
3. vanishing of mod-3 étale cohomology for the named nodal double plane; and
4. existence of affine double planes, including a connected Euler-zero full
   `S3` control, carrying connected étale cubic covers.

Do not promote universal vanishing for the charged one-place branch class,
an exclusion of either abstract quartic horn, existence of an actual proper
block, or any conclusion about the primitive/no-proper-block case.  The
producer's successor `R4-DP3` remains the correct open problem.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13488`.
- Body SHA-256:
  `d85b91d912fc70a84ad47f37a9e915cfa053ad55a83a468a1fd6f4b7cbfab4b7`.
- Frozen basis: `7afc73b69182b7fc7b33b1153bb945469668f00e`.
