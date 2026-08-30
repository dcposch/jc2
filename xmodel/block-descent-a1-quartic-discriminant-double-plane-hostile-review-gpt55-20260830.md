# Hostile review: quartic discriminant double-plane gate

## 0. Custody manifest

Custody check passed.  The charged bytes reproduce as follows.

```text
1939c55467f5795c5bb3a264f5516c666c82e34849bc4d74f190c95d18a016bb
  xmodel/block-descent-a1-quartic-discriminant-double-plane-etale3-gate-sol56-20260830.md
5544c05bee8ffeab1791084d7d58b70ca6a45d44079efcc2f8d4535834da0216
  xmodel/block-descent-a1-quartic-discriminant-double-plane-etale3-gate-sol56-20260830.md.artifact.json
2ce87f135a1e91da8e43bc5e4cf3e37ce29f27cff6c6aacabdd08c4b75a1cde8
  ops/block_descent_a1_quartic_discriminant_double_plane_replay.py
5d7df7ce0ad3548e88fd23734917212d6b3fbd3ada4cab81514b12bb76ea64de
  xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md
cf157e17db8179b590f15808aab84447717df343735416578e005a2085d73d4e
  xmodel/block-descent-a1-quartic-minimal-cycle-nodal-control-threat-map-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
9579d3a1737041f73a973a2ac852471a21cdad879a6d7cf3b1f76251cd5cd595
  xmodel/block-descent-all-degree-acyclic-companion-obstruction-coordinator-integration-sol56-20260830.md
```

The artifact manifest for the producer report says:

```text
artifact.name=block-descent-a1-quartic-discriminant-double-plane-etale3-gate-sol56-20260830.md
artifact.full_sha256=1939c55467f5795c5bb3a264f5516c666c82e34849bc4d74f190c95d18a016bb
artifact.body_sha256=4b1a7bf4b829fb2bf653a5421375d8caac159491c3a0986df0428e0b5f77c285
artifact.body_bytes=13844
artifact.file_bytes=14177
artifact.published_mode=0444
artifact.frozen_basis=4393243bccdbe1a32d80fe8c770c2c8b909f4c01
custody.source_sha256=4b1a7bf4b829fb2bf653a5421375d8caac159491c3a0986df0428e0b5f77c285
custody.source_bytes=13844
custody.opened_utc=2026-08-30T22:08:29Z
custody.closed_utc=2026-08-30T22:11:15Z
custody.finalized_utc=2026-08-30T22:11:15Z
custody.owner=rank4_double_plane
```

Target report manifest:

```text
target=xmodel/block-descent-a1-quartic-discriminant-double-plane-hostile-review-gpt55-20260830.md
body_terminator=<!-- BODY-END -->
referee_seal=none asserted here; coordinator seals returned bytes after exit
```

No external source was used.  The producer report internally cites one file not charged in this assignment, namely the ruling-transfer integration, and it omits the charged all-degree acyclic-companion integration from its own charged-input list.  I did not inspect that uncharged ruling-transfer file.  Every conclusion below is therefore conditional on the exact charged texts and on standard algebraic geometry reconstructed here.

Overall verdict: `CONFIRM_WITH_CORRECTIONS / SUCCESSOR OPEN`.  The `m=0` double-plane etale gate is mathematically sound under the charged minimal-row hypotheses.  The named nodal control is excluded.  The positive `S3` control is real but does not satisfy the one-place branch condition.  The proposed one-place successor is not decided by the charged packet.  The replay PASS claimed in the producer report is not reproducible in this local environment because `sympy` is missing.

## 1. Field tower and double plane

Status: `CONFIRMED`, with the explicit scope that the relevant branch components are generically `(2,1,1)`.

Let `K=C(x,y)` and let `Omega/K` be the charged `S4` Galois closure.  The Klein four subgroup `V4` is normal in `S4`.  The action of `S4` on the three perfect matchings of four letters has kernel `V4`, hence

```text
S4/V4 = S3.
```

Since `A4` contains `V4`, its image is

```text
A4/V4 = A3 = C3.
```

Thus

```text
M=Omega^V4,      Gal(M/K)=S3,
K2=Omega^A4=M^A3,      Gal(K2/K)=C2.
```

Let `A=C[x,y]`.  The normalization of `A2=Spec A` in `M` is `W`; the normalization in `K2` is `D`.  Along a generic branch component of type `(2,1,1)`, the quartic inertia is a transposition in `S4`.  Its image in `S3=S4/V4` is again odd, so the sign quadratic `K2/K` ramifies to odd order along that component.  Off the reduced transposition branch support the `S3` cover is unramified in codimension one.

The square-class audit is clean.  Write the reduced branch equation as

```text
q_B = product_i q_i
```

with distinct irreducible `q_i in C[x,y]`.  Since `C[x,y]` is a UFD, a quadratic extension of `K` is represented by a square class whose valuations modulo two are prescribed at height-one primes.  The class ramified exactly along the `q_i` is

```text
q_B modulo K^{*2}.
```

If two such classes had the same height-one parity everywhere, their quotient would have all valuations even; factoriality writes it as `c r^2`, and `c in C*` is a square.  Thus there is no hidden unramified quadratic factor.  This is also the purity statement in this affine plane setting: a finite quadratic cover of `A2_C` unramified in codimension one is trivial.

Therefore

```text
K2 = K(sqrt(q_B)).
```

The affine algebra

```text
R_D = C[x,y,s]/(s^2-q_B)
```

is finite over `A`, has fraction field `K2`, and is normal.  Indeed it is a hypersurface, hence `S2`; at a generic smooth point of `B`, the completed local equation is `s^2-u`, which is regular; away from `B` it is etale over the regular plane.  The possible singular locus is contained in

```text
s=0,      q_B=0,      dq_B=0,
```

which is finite because `q_B` is a reduced plane curve.  Hence the singular locus has codimension two in the surface and Serre `R1+S2` gives normality.  Since `q_B` is reduced and nonconstant, it is not a square; `R_D` is a domain.  Thus

```text
D = Spec C[x,y,s]/(s^2-q_B).
```

Similarly, the integral closure of `A` in the field `M` is finite because `A` is excellent and `M/K` is finite.  It is integral and connected because `M` is a field.  The subgroup `A3` acts on `W`, and the quotient normalization is `D`; hence `W -> D` is the finite cyclic degree-three quotient associated to `M/K2`.

The only correction is semantic: if a branch component were generically `(3,1)`, the sign quadratic would not ramify along that component because a three-cycle is even.  The charged minimal rows under review have all branch components generically `(2,1,1)`, with `(3,1)` only as a finite special value when `m=1`, so this correction does not damage the intended gate.

## 2. Stabilizer criterion and local image table

Status: `CONFIRMED`.

Let `z` be a closed point of the affine target and let `w in W` lie over it.  Over `C` all residue fields at closed points are `C`, so there is no separate residue-field Galois factor.  The complete local decomposition group `H_z <= S3` is the stabilizer of `w` for the `S3` action on `W`.  For the quotient by `A3`, the geometric stabilizer of `w` is exactly

```text
H_z cap A3.
```

A finite constant group action of order prime to the characteristic gives a finite etale torsor over the quotient precisely when all geometric stabilizers are trivial.  Therefore `W -> D` is etale at the corresponding quotient point if and only if `H_z cap A3=1`.

The local table is as follows.

```text
quartic fibre     local quartic group               image in S3       cap A3
(2,1,1)           <(12)>                            C2                1
(2,2)             <(12),(34)>                       C2                1
(3,1), finite     subgroup on three sheets with
                   generic transposition             S3                A3
(4)               A4 or S4, after D4 exclusion       A3 or S3          nontrivial
```

For `(2,1,1)`, the henselian fibre has one ramified quadratic factor and two rank-one factors.  The decomposition group fixes the two rank-one factors and acts on the ramified pair by at most `C2`; because the point is on the branch it is the transposition group.  Its image under `S4 -> S3` is a transposition, so its intersection with `A3` is trivial.  This remains true at a singular point of the plane branch if the fibre type is still `(2,1,1)`: the henselian rank decomposition prevents a hidden three-cycle from appearing.

For `(2,2)`, the two rank-two factors have disjoint transposition inertia, say `(12)` and `(34)`.  In the pairing quotient these two transpositions have the same image.  Thus the image of the local group is `C2`, not `V4`, and again the cyclic stabilizer is trivial.  The fact that the branch point is a conductor point or an ordinary node of the branch does not change the quotient-point calculation: the stabilizer for `W -> D` is still the literal intersection with `A3`.

For a finite `(3,1)` value in the charged generic-transposition row, three sheets coalesce and the local group contains a generic transposition on those sheets.  Transitivity on the three-sheet packet plus a transposition gives the full `S3` on that packet.  The restriction of the pairing action to this point stabilizer is faithful, hence the image in the resolvent `S3` is `S3`.  Its intersection with `A3` is the order-three subgroup.

For `(4)`, the fibre is one local packet of total rank four, so the local decomposition group is transitive on the four sheets.  The charged branch-topology integration repairs the earlier overlarge row: a local group at such a point is generated by its own branch meridians, whose divisorial cycle types are transpositions or three-cycles.  A `D4` subgroup contains no three-cycle, and the transpositions inside it generate only an intransitive subgroup, so `D4` cannot supply a `(4)` local packet.  The remaining charged possibilities are `A4` and `S4`, whose images in `S3` are `A3` and `S3`.  Both meet `A3` nontrivially.

Thus the table used by the producer is correct after the charged `D4` deletion.

## 3. The `m=0` horn and codimension-two ramification

Status: `CONFIRMED`.

In the charged minimal no-cusp row,

```text
m=0,      n4=0,
```

every affine branch value has quartic fibre type `(2,1,1)` except the unique `(2,2)` value.  Section 2 gives `H_z cap A3=1` for both fibre types.  Therefore the `A3` action on `W` is free over every affine target point, including the singular point of the double plane over the `(2,2)` conductor value and any branch singularity whose fibre type remains `(2,1,1)`.

This is stronger than codimension-one unramifiedness.  For a finite quotient by a tame constant group, ramification is detected by geometric stabilizers at points.  There is no additional conductor or normalization point at which a hidden `C3` stabilizer can appear once the complete local decomposition group has trivial intersection with `A3`.  Hence

```text
W -> D is finite etale at every affine point in the m=0 row.
```

The argument does not assert anything about a compactification point at infinity.  The object under review is the affine normalization `D`.

## 4. The `C3` torsor, anti-invariance, and Kummer

Status: `CONFIRMED` for the forced class in the `m=0` row; `GAP` for any attempted vanishing theorem not separately proved.

Because `M` is a field, `W` is connected.  In the `m=0` row Section 3 makes `W -> D` a finite etale degree-three quotient with group `A3=C3`.  A trivial constant `C3` torsor over connected `D` is the disjoint union of three copies of `D`; `W` is not disconnected.  The torsor class is therefore nonzero:

```text
0 != alpha=[W/D] in H^1_et(D,Z/3).
```

The involution `iota` of `D/A2` is represented in `S3` by an odd element.  Conjugation by an odd element sends a three-cycle to its inverse.  Therefore pullback by `iota` sends the `C3` torsor to the same cover with inverse group action:

```text
iota^* alpha = -alpha.
```

Since `C` contains the third roots of unity, `Z/3` may be identified with `mu_3`.  The Kummer sequence on the etale site gives

```text
0 -> O(D)^*/O(D)^{*3}
  -> H^1_et(D,Z/3)
  -> Pic(D)[3]
  -> 0.
```

The exact sequence is valid for this normal affine surface; smoothness is not required.  It separates the two possible sources of the class:

```text
unit source:     a cyclic cover T^3=u for u in O(D)^*
Pic source:      a three-torsion line bundle on D
```

For a normal singular surface, `Cl(D)[3]` is not a substitute for `Pic(D)[3]`.  There is a natural injection `Pic(D) -> Cl(D)`, so torsion-freeness of `Cl(D)` kills `Pic(D)[3]`; the converse need not hold.  Also, a class seen on `D_reg` or on a punctured local link is not automatically a class on all of `D`.  It must have trivial local residue around every strict-henselian singular neighborhood.  The forced `m=0` class passes this test because it is already represented by the finite etale cover `W -> D`.  A candidate class found by Alexander modules or complement monodromy still has to pass the local extension test.

Thus the producer's nonzero anti-invariant class is confirmed, but the branch ledger alone does not prove that such classes vanish for all one-place branches.

## 5. The `m=1` cusp row

Status: `CONFIRMED`, with no generalization of analytic type.

In the charged `m=1,n4=0` row, all codimension-one branch inertia is still transposition-type, but there is a unique finite `(3,1)` value.  At that point Section 2 gives local resolvent image `S3`, hence

```text
H_z cap A3 = A3.
```

The cyclic quotient `W -> D` is therefore not etale at the quotient point over that value.  Away from that point, the same point-stabilizer calculation as in the `m=0` row gives trivial `A3` stabilizers.  Thus the canonical cyclic cover in the `m=1` row is finite and etale in codimension one, but not etale on the whole affine surface:

```text
W -> D is quasi-etale but not etale.
```

The ordinary-cusp control realizes the local mechanism.  A plane cusp can be written, after analytic coordinates, as the branch equation behind

```text
s^2 = y^2-x^3.
```

Putting `U=y+s`, `V=y-s`, and `X=x` gives

```text
UV = X^3.
```

This is the quotient

```text
Spec C[a,b] -> Spec C[a*b,a^3,b^3]
(a,b) |-> (zeta a, zeta^(-1) b)
```

by `mu_3`.  The action is free away from `(a,b)=(0,0)` and has the whole `mu_3` as stabilizer at the origin.  Hence the quotient map is etale on the punctured surface and not etale at the singular point.  The nontrivial class on the punctured link is a local residue, not a finite etale cover of the whole singularity.

This control proves the distinction between quasi-etale and etale.  It does not prove that every `(3,1)` germ in the campaign is analytically the ordinary cusp, and the producer report correctly avoids that stronger assertion.

## 6. Named nodal double plane

Status: `CONFIRMED`.

The named nodal branch is

```text
B0: y^2=x^2(x+1).
```

For the double plane, set

```text
u=y+w,      v=y-w.
```

Then

```text
D0 = Spec R0,
R0 = C[x,u,v]/(uv-x^2(x+1)).
```

Normality holds.  This is a hypersurface, hence `S2`.  The partial derivatives of `uv-x^2(x+1)` are

```text
v,      u,      -x(3x+2).
```

Together with the equation they vanish only at

```text
x=u=v=0.
```

The singular locus has codimension two in the surface, so `R0` is normal.

The units are constant.  After inverting `u`,

```text
R0[1/u] = C[x,u,u^(-1)],
```

whose units are `c u^n`.  If a unit of `R0` equals `c u^n` in this localization, its Weil divisor is `n div(u)`.  But

```text
div(u)=2P0+P1,
P0=(u,x),      P1=(u,x+1),
```

so a unit has zero divisor only when `n=0`.  Thus `O(D0)^*=C*`.

Nagata's class-group computation is also correct.  The localization `R0[1/u]` is a UFD.  The only height-one primes removed by inverting `u` are `P0` and `P1`, with multiplicities `2` and `1` in `div(u)`.  Hence

```text
Cl(R0) = Z P0 + Z P1 / <2P0+P1> = Z.
```

There is no hidden torsion because `gcd(2,1)=1`.  For a normal integral scheme, Cartier divisor classes inject into Weil divisor classes, so

```text
Pic(D0) -> Cl(D0)
```

is injective.  Since `Cl(D0)` is torsion-free, `Pic(D0)[3]=0`.  Since `C*` is divisible, `C*/C*^3=0`.  Kummer therefore gives

```text
H^1_et(D0,Z/3)=0.
```

The named nodal control cannot be the `m=0` discriminant double plane of the charged `S3` resolvent.

## 7. Connected positive `S3` control

Status: `CONFIRMED`, with a boundary correction: it saturates the coarse double-plane odd-etale gate, not the one-place rank-four successor.

The charged control starts with

```text
p(T)=T^3+xT+xy+1,
Delta=-4x^3-27(xy+1)^2.
```

The branch curve `B1=(Delta=0)` is smooth.  On `B1`, `x` cannot vanish because then `Delta=-27`.  If both partial derivatives vanished, then

```text
partial Delta / partial y = -54x(xy+1)=0
```

would force `xy+1=0`, and then `Delta=-4x^3` would force `x=0`, contradiction.  Thus `B1` is nonsingular.

The parametrization is correct:

```text
x=-3r^2,
y=(1-2r^3)/(3r^2),
r in Gm.
```

Substitution gives

```text
xy+1 = 2r^3,
Delta = -4(-27r^6)-27(4r^6)=0.
```

The inverse formula

```text
r=-3(xy+1)/(2x)
```

is regular on the branch because `x` is nowhere zero there.  Hence

```text
B1 is isomorphic to Gm,
e(B1)=0.
```

The cubic is irreducible over `C(x,y)`.  Over `C(x)`, the equation rewrites

```text
y=-(T^3+xT+1)/x.
```

This is a degree-three rational function of `T`, so the induced function-field extension `C(x,T)/C(x,y)` has degree three.  Therefore the monic cubic is the minimal polynomial of `T`.  The discriminant is not a square: `B1` is a nonempty smooth divisor appearing with multiplicity one in `Delta`, equivalently the quadratic polynomial in `y` cannot be the square of a linear polynomial over `C(x)`.  Thus the Galois group is `S3`.

The Galois closure model is

```text
W1: a^3+b^3-3aby+1=0,
mu_3: (a,b) |-> (zeta a, zeta^(-1)b).
```

The hypersurface is integral: a factorization linear in `y` would require a nonconstant common divisor of `ab` and `a^3+b^3+1`, and there is none.  The `mu_3` action has no fixed point on `W1`; a nontrivial fixed point would have `a=b=0`, contradicting the equation.

The invariant ring calculation is explicit.  In `C[a,b,y]`,

```text
A=a^3,      B=b^3,      X=ab
```

generate the `mu_3` invariants with relation `AB=X^3`.  On `W1`,

```text
A+B-3Xy+1=0.
```

Put `x=-3X` and `S=A-B`.  Then

```text
S^2=(A+B)^2-4AB
   =(-xy-1)^2-4(-x/3)^3,
```

so after multiplying `S` by a nonzero scalar in `C`, the relation is

```text
s^2=-4x^3-27(xy+1)^2 = Delta.
```

Thus `W1/mu_3` is the normal double plane `D1=(s^2=Delta)`.  Since the finite group action is free, the quotient

```text
W1 -> D1
```

is finite etale of degree three.  Since `W1` is integral, the cover is connected.

This control is important but limited.  It proves that connected Euler-zero branch and an affine discriminant double plane can carry a nonzero odd etale `C3` class.  It does not satisfy the polynomial one-place condition: its branch normalization is `Gm`, not `A1`.  It is also not a quartic proper block.  Therefore it defeats a universal vanishing slogan for affine double planes but does not defeat the proposed one-place successor.

## 8. Proposed one-place successor

Status: `OPEN` / `GAP`.

The charged files do not prove that the following condition forces vanishing:

```text
every branch component normalizes to A1,
the source forest is connected,
the target branch is obtained by exactly one two-point identification.
```

They also do not provide an exact counter-control satisfying that condition and carrying a nonzero locally extendable anti-invariant mod-three class.

The two charged controls bracket the problem but do not decide it.

```text
nodal cubic B0:
  normalization A1, one two-point identification, one place at infinity;
  H^1_et(D0,Z/3)=0.

positive S3 control B1:
  connected, smooth, e(B1)=0, nonzero etale C3 cover of the double plane;
  normalization Gm, so it violates the one-place input.
```

Thus the exact successor remains:

```text
Compute H^1_et(D,Z/3)^- for D=(s^2=q_B), under the one-place
polynomial-curve plus one-identification hypotheses, including the local
extension condition at every singular point.
```

A punctured or link class is insufficient.  The ordinary cusp quotient `A2 -> A2/mu_3` gives a nontrivial `C3` cover of the punctured smooth locus, but it is not etale over the whole singular surface.  In Kummer terms, the calculation must separately account for:

```text
O(D)^*/O(D)^{*3},
Pic(D)[3],
the injection Pic(D)->Cl(D),
and the residues of classes first seen on D_reg.
```

If the successor aims for vanishing, it must prove constant units and no anti-invariant `Pic[3]`, or otherwise show that all anti-invariant punctured classes have nonzero local residue and fail to extend.  If it aims for a counter-control, it must exhibit a branch satisfying the one-place and one-identification hypotheses, verify the local `(2,1,1)/(2,2)` stabilizer conditions, and produce a nonzero class extending over every singularity.

No rank-four exclusion may be inferred from the present charged packet.

## 9. Replay audit

Status: `REFUTED` for local replay reproducibility; `CONFIRMED` for the script's limited intended scope by source inspection.

The charged script imports `sympy` at top level.  In the active local `python3`, `sympy` is not installed, so none of the replay modes reaches the mathematical checks.  I ran the requested invocations.  The exact results were:

```text
ordinary:
  returncode=1
  stdout_sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  stdout_bytes=0
  stderr_sha256=0ae6a012a8025caaf5d54dbb24cad38877f1777509193f4f55cc22fa2f7f6937
  stderr_bytes=223
  stderr_last=ModuleNotFoundError: No module named 'sympy'

python3 -O:
  returncode=1
  stdout_sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  stdout_bytes=0
  stderr_sha256=0ae6a012a8025caaf5d54dbb24cad38877f1777509193f4f55cc22fa2f7f6937
  stderr_bytes=223
  stderr_last=ModuleNotFoundError: No module named 'sympy'

python3 -OO:
  returncode=1
  stdout_sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  stdout_bytes=0
  stderr_sha256=0ae6a012a8025caaf5d54dbb24cad38877f1777509193f4f55cc22fa2f7f6937
  stderr_bytes=223
  stderr_last=ModuleNotFoundError: No module named 'sympy'

--mutate-cusp-as-etale:
  returncode=1
  stdout_sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  stdout_bytes=0
  stderr_sha256=0ae6a012a8025caaf5d54dbb24cad38877f1777509193f4f55cc22fa2f7f6937
  stderr_bytes=223
  stderr_last=ModuleNotFoundError: No module named 'sympy'
```

Because stdout is empty, the combined `2>&1` byte hash is the same as the stderr hash in these runs.  The producer's reported stdout hash

```text
66ecf7bae2685fb6c379fef27cbcad006cc513d2b1b32af700a3821411119745
```

was not reproduced here.  The mutation did not certify rejection of the cusp-as-etale branch in this environment; it failed before argument-dependent logic ran.

By source inspection only, the script has zero Python `assert` statements and nineteen calls to its `require` function.  If the missing dependency is supplied, those calls check:

```text
S4/V4 has order six and kernel V4;
A4/V4 has order three;
the node packet image has C3 stabilizer order one;
the cusp packet image has C3 stabilizer order three;
the nodal Danielewski identity;
the cubic discriminant and Gm parametrization;
the Cardano closure identities;
the mu_3 invariance and fixed-point exclusion;
the ordinary-cusp quotient relation.
```

The code does not prove normality, connectedness of the integral normalizations, purity, finite-group torsor criteria, Kummer theory, the Nagata class-group computation, irreducibility as a theorem over `C(x,y)`, local extension residues, existence of an actual proper block, a rank-four exclusion, or JC2.

## 10. Maximum-safe theorem, corrections, blast radius

Status: `CONFIRMED_WITH_CORRECTIONS`.

The maximum safe theorem is:

```text
Assume an actual charged rank-four proper block in the minimal connected-cycle
row, with S4 Galois closure, all branch components generically (2,1,1), and
n4=0.

Let D be the normal sign-discriminant double plane and W the normalization in
the S3 resolvent field.

If m=0, then W -> D is a connected finite etale C3 torsor.  Its class
alpha in H^1_et(D,Z/3) is nonzero and anti-invariant under the double-plane
involution.

If m=1, then W -> D is finite quasi-etale but not etale at the unique finite
(3,1) point.

The named nodal double plane uv=x^2(x+1) has H^1_et(D,Z/3)=0 and cannot
realize the m=0 discriminant gate.

There exist connected Euler-zero affine double planes with connected finite
etale C3 covers, but the charged positive control has branch normalization
Gm and does not satisfy the one-place minimal horn.
```

Corrections and guardrails:

```text
1. The sign double plane is branched along the reduced transposition branch
   support.  This equals the charged B only because the relevant components
   are generically (2,1,1).
2. The m=1 cyclic cover is not an etale cover of D; it is only quasi-etale.
3. The ordinary cusp quotient is a local control, not a classification of
   all (3,1) germs.
4. Cl[3] is not the Kummer target; Pic[3] is.  Cl is useful only through
   Pic -> Cl or through a separate divisor-class analysis on D_reg plus
   local residue checks.
5. A punctured-link C3 class does not imply a finite etale cover of the
   singular surface.
6. The positive S3 control refutes only universal double-plane vanishing,
   not the one-place successor.
7. The replay PASS hash is not locally reproduced because the active Python
   environment lacks sympy.
8. The producer's internal charged-input list is not identical to this
   assignment's charged list; I did not use the uncharged file it cites.
```

Blast radius:

```text
Safe to promote:
  the m=0 etale C3 double-plane gate;
  the nonzero anti-invariant class forced by a connected m=0 torsor;
  the exclusion of the named nodal control;
  the non-etaleness of the m=1 canonical cyclic cover at the (3,1) point;
  the positive Gm-normalized S3 control as a coarse negative control.

Not safe to promote:
  vanishing for every one-place branch double plane;
  an exclusion of the m=0 minimal horn;
  an exclusion of the m=1 horn;
  inheritance of a proper cubic block by the resolvent;
  a rank-four block exclusion;
  a primitive/no-proper-block result;
  a Keller counterexample or JC2.
```

The cheapest decisive successor is an explicit one-place computation.  For the actual branch equation, or for the full formal class of allowed one-place branches, compute

```text
H^1_et(Spec C[x,y,s]/(s^2-q_B), Z/3)^-
```

by Kummer and local residues.  Concretely:

```text
1. Prove O(D)^*=C* or exhibit a nonconstant unit and its involution parity.
2. Compute Pic(D)[3], not only Cl(D)[3]; use Pic -> Cl only when it is enough.
3. If using D_reg or complement monodromy, impose trivial residue on every
   singular link of D.
4. Check the complete local stabilizer table for the proposed cover, especially
   at the unique two-point conductor value and at any unibranch singularity.
```

The decisive output should be either a vanishing theorem for the anti-invariant locally extendable part under the one-place hypotheses, or a single explicit branch satisfying those hypotheses with a nonzero extending anti-invariant `C3` torsor.  Until then the correct campaign status is `OPEN`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `27041`.
- Body SHA-256:
  `4e386bee67a5c1a67050313251f59c89d879f5f12378986e44a9fbaab34d9128`.
- Frozen basis: `06a4110854d7ad38525daccfa7895943259a3812`.
