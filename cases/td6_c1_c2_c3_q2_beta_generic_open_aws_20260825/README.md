# TD6 q2-beta generic-open P12/N13 unit certificate

Frozen status: **producer-exact and independently mirrored on AWS.**

This package stays inside the fixed source-typed normalized A3 section

```text
y=s^-1,
x=C*s+V*s^2+U*s^3+t*s^4,
p=t^15,
q_beta=t+beta*t^2+t^25,
H=C-3U^2,
B3=4C^2U^2-4CV^2U+24CU^4+V^4-20V^2U^3+20U^6.
```

The F1 orbit, dead stretch, pole scale, and pole data remain frozen.  The
open set is exactly `D(U*H*B3)`; no source scaling or gauge normalization is
used.

## Exact canonical identity

V43 was run from one byte-identical archive independently on r6d and Box03.
Both jobs exited zero and produced byte-identical mathematical stdout,
SHA256

```text
a53cc30d8d6d24988b94a3c3812da42c1ac8247205322df26c504e86797a0527.
```

The replay retains direct
`q_beta'=1+2*beta*t+25*t^24`, full transport, the genuine 2,893-term P12,
all first original rows, and the separately staged N13 source certificate.
It proves:

- transport rank `3470/3602` and first rank `38/132`;
- exact P12 lift through 28 nonzero original first rows, 1,648 multiplier
  terms, and 39,583 termwise source slots;
- P12 remainder `-k/50 + beta*T`, with a nonzero two-term beta tail `T`;
- staged `N13=(k/25)beta` and exact multiplier `(25/k)T`;
- exact cancellation without beta division, leaving the constant residual
  `-k/50`;
- direct-q-prime omission and P12-without-N13 negative controls;
- complete denominator radical contained in `U*H*B3`, with the N13
  multiplier denominator equal to one.

The frozen Bezout certificate for `k` makes `-k/50` a unit over the campaign
coefficient field and every extension.  Therefore the fixed A3 q2-beta
system has no point on `D(U*H*B3)` for any beta.

## Staged N13 dependency

The included V41 exact replay retains transport, first, previous/pole, and
current original-row ancestry through `t^13`.  It has ranks `3470/3602`,
`38/132`, `38/94`, and `25/56`, emits all 11 current compatibilities, and
asserts the unique target value `N13=(k/25)beta`.  Its terminal exact PASS is
the source-lift dependency consumed by V43.

V41's standalone reporter predates canonical E3-coordinate serialization;
some digest strings can contain process-address provenance.  That reporter
defect does not alter its exact assertions, rows, ranks, denominators, or
source replay and none of its legacy digests is used as V43 custody.  A
canonical two-host replay is being produced as a nonblocking supplement.

## Custody negative control

V37 proved the same algebraic expressions and source identity but used
legacy `repr(E3)` in four reporter fields: first-pivot, beta-tail, N13 value,
and N13 multiplier.  Its independent r6d and Box03 outputs are retained as
negative custody controls.  V43 serializes every E3 value through all 18
exact rational coordinates; its two outputs agree byte-for-byte.

## AWS custody

V43 archive SHA256:
`42953e8ae8a22df4082618fe6fb833a960ab9c4304b9664faafbf8f1ed62f8b3`;
V43 source-manifest SHA256:
`92d60540490af5cfbf3a5c8410fe01bbe4baf7a527d21f238d13d67871ec6c8f`;
producer SHA256:
`3cc0fc3bc4a55810c4d4320b53ff77a48341045c06f556cd6243119b8fe4c332`.
Both hosts used Python 3.12.3, python-flint 0.9.0,
`PYTHONHASHSEED=0`, and exited zero.

## Scope quarantine

This theorem closes only `D(U*H*B3)` for the fixed q2-beta A3 source.  The
separate frozen packages for `U=0`, `H=0`, and `B3=0` are required for the
complete fixed-A3 atlas.  No fourth center/boundary/dead-stretch/F1/pole
modulus, whole-TD6, SP-2, landing, or JC2 claim is made here.

