# Producer report: repaired fixed-A3 q2-beta `B3=0` atlas union (V74/V75)

Status: **dual-AWS producer-exact; hostile review pending.**

## V74: the repaired `C=-5U^2,V=0` line

V73K supplies an original-source unit obstruction on
`V=0,C=-5U^2,D(U)` for all beta.  The hostile-reviewed V70 origin theorem
supplies the `U=0` endpoint.  Since the raw line is `Spec Q[U]` and
`Spec Q[U]=D(U) union V(U)`, V74 closes the whole raw line.  Both branch-
omission controls fire.

V74 dual outputs:

- Box02: `69b06c29a84648fc233c15707b571dcf0946cc024a61b6f188336f5cfa725339`.
- Box03: `df2810f77e206b1d4ce1715ffd5e3db7f836cb19a0bb2676a60aa0631ed8d4e2`.
- Replay: `fe25b93adf8b79fd08d3b41c33b682758fd191c310017c188305ddc766c095b6`.

## V75: complete raw `B3=0` case tree

The exact polynomial

`B3=4C^2U^2-4CV^2U+24CU^4+V^4-20V^2U^3+20U^6`

is replayed together with
`B3=U^6 b(C/U^2,V^2/U^3)` and the normalized line pencil
`y=t(x+5)`.  The dependency-complete leaves are reviewed V70 on `U=0`,
reviewed V46 on `V=0,C=-U^2,D(U)`, V74 on the whole
`V=0,C=-5U^2` line, reviewed V67 on the two finite factors, and reviewed
V66 on the complementary generic open.  The direct identities
`b(-5,y)=y^2`, the `t=0` specialization, and the `t=2` specialization close
the apparent route boundaries.  The exact decision tree and one omission
control for every dependency pass.

V75 dual outputs:

- Box02: `66b0d9257e9446fd9363eafb23eb40ef71aa7ed6ecef3f393436b55398a0aa96`.
- Box03: `b3ab7324cf911ca5c4ba94a88dbf3b02cb31e037bb5b946029e352b03d8ebcd1`.
- Replay: `0c9cb1fe40d4cb95f0fc347f216dd10fe71324f0d48527b85a04ec35609b4c16`.

The two outputs at each stage differ only by registered run tag and
hostname; every mathematical and dependency line agrees exactly.  Each
host's recursive source manifest verifies.

## Exact conclusion and firewall

The whole raw divisor `B3=0` is producer-exact empty for every beta in the
fixed source-typed A3 q2-beta section.  This does not remove any transverse
center, boundary, dead-stretch, F1-orbit, or pole modulus.  It is not a
whole-A3 or TD6 kill, not SP-2, not a landing theorem, and not JC2.
