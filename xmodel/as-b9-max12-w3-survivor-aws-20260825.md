# AS `B9` gives an exact maximum-twelve `Z/27` survivor

Status: **producer-exact / independently duplicated AWS replay / hostile
review pending**.

The tame integral automorphism

```text
B9=(u,v)=(x+y^3, y+u^4)
```

has determinant one.  Over `F_3`, right-composition of the Artin--Schreier
seed `(s-s^3,t)` gives

```text
G9=(u-u^3,v),
```

an etale noninjective map of actual partial `y`-degrees `(9,12)` with unit
leading coefficients.  It is tame-equivalent to the old residue seed, so it
is not a new residue isomorphism class.  Its new value is that it lies exactly
on one of the two primitive characteristic-zero maximum-twelve checksums.

More strongly, with `u=x+y^3`, the fixed integer pair

```text
P=u-u^3+18uy,
Q=y+u^4+3u^2y+18y^2
```

has actual partial `y`-degrees `(9,12)`, reduces to `G9`, and satisfies

```text
det J(P,Q)
 = 1-81u^4+54y-162u^2y+648y^2
 = 1 mod 27.
```

The exact all-coefficient replay retains the integer mixed terms suppressed
by Frobenius after reduction, checks the explicit collision
`(0,0),(2,2)->(0,0)`, and contains two omission controls.  Identical replay
stdout SHA-256 on Box02 and Box03 is
`f9e55a4f3cfc6c3b85b2d4c9ec724e0d757e083b0e82e0ff0e387d7125ea1aef`;
the canonical payload SHA-256 printed by both is
`d4482e42f617a4693e7142725ae37de45e3285926408d56c6ad1b746cb405f2e`.

This finite-depth point is evidence for a serious counterexample-side client,
not a counterexample.  No compatible `Z/81`/all-depth tower, fixed-scheme
generic fibre, `Z_3` polynomial map, or characteristic-zero map is supplied.
The source automorphism does not make the AS seed a TD6 object: the special
fibre has separable function-field degree three, while TD6 is topological
degree six and its frozen source requires the unrelated pole data
`p=t^15,q=t+t^25` plus SP-2 normalization.

Producer case:
`cases/as_b9_max12_w3_survivor_aws_20260825/`.
