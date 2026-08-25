# AS `B9` fixed-D12 branch survives through `Z/243`

Status: **producer-exact / dual-AWS replay / hostile review pending**.

The explicit `B9` branch from
`cases/as_b9_max12_w3_survivor_aws_20260825/` continues without increasing
either total or partial `y`-degree beyond twelve.  With `u=x+y^3`, the exact
pair is

```text
P=u-u^3+18uy+81(2uy+xy^2),
Q=y+u^4+3u^2y+72y^2+81(y^2+x^4y^2+xy^11).
```

Its determinant is one modulo `243`, and its actual degree pair is `(9,12)`
for both total degree and partial `y`-degree.  The proof is a literal integer
determinant expansion plus exact replay of the two mod-three source
primitives that cancel the divided `Z/81` residual.

Box02 and Box03 stdout agree at SHA-256
`86afa339d260ac31d09a1ec59cd189c5adaa02212acd3d7c40bcd4c07678a853`;
the canonical payload SHA is
`04ccf4367c5e321625e41f39faa37c69afdebdcbdc65af4ca66f14094b668850`.

This is a materially deeper finite survivor on the exact maximum-twelve
frontier, but it is still one branch at one finite modulus.  It supplies no
inverse limit, characteristic-zero map, TD6 normalization, or JC2 result.
The immediate producer successor is the complete next-digit linear solve in
the same fixed D12 support.
