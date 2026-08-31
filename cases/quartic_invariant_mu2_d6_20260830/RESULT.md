# Exact result: the pullback-degree-six cell is empty

## Statement

There is no pair in the normalized pullback-degree-at-most-six cell of
`README.md` whose Jacobian is constant.  Equivalently, after an invertible
affine target change, no pair

```text
H1 = U + a1 A + a2 A^2 + a3 A^3 + a4 A Z + a5 A U,
H2 = Z + b1 A + b2 A^2 + b3 A^3 + b4 A Z + b5 A U
```

has `J(H1,H2)=2`.

## Direct certificate

Exact expansion gives, independently of all ten parameters,

```text
[x^2 y] J(H1,H2) = 8,
[x^4 y^2] J(H1,H2) = 4.
```

Either coefficient already contradicts constancy.  `verify_result.py`
replays these identities and the invariant-ring relation.  The argument is
over characteristic zero; the modular runs below are cross-checks, not the
reason for the characteristic-zero conclusion.

The target normalization is lossless: the linear coefficient matrix of
`(U,Z)` must be invertible for a nonzero constant Jacobian, since at the
origin the Jacobian is twice its determinant.  Applying its inverse makes
the linear terms exactly `(U,Z)` and the constant Jacobian exactly `2`.

## AWS cross-check and custody

All lanes used source hashes
`04b80b51c461efa79783f1b953a93fdfaf8e50c53c8b3112e0d623d756557bac`
(runner) and
`edcbc3796ffae65265a89b10bbd19836d6b5a60cd0c35c561c555c0b6afc5dd1`
(generator), with Git basis
`aa0f341f8553e78a28084eaf51c1e4ffbc2ad21a`.  Every remote
`EVIDENCE.sha256` verified before retrieval.

| lane | instance | field/engine | result SHA-256 | evidence-manifest SHA-256 |
|---|---|---|---|---|
| mutation target `3` | `i-02cb2b4a379ffcc64` | `Q/std` | `dc11c50378791a148587957026f1ff98cbc1b4e3cdb07a97fcb3c1ea4dbf687c` | `7e16cfdb4db723b4596281877805204d13cdc91d441ddedd64c294c0d33e5b63` |
| actual target `2` | `i-02cb2b4a379ffcc64` | `Q/std` | `76aacf8431f46705eb5c7347e08d500d841c6c0419f6d3240a61926a085ef079` | `eb2b97af1e33a7f609fec4632051d5a60f6f3c6665f9f50234a8fceff1301604` |
| actual target `2` | `i-07eeaf8ba6f0bc419` | `Q/slimgb` | `76aacf8431f46705eb5c7347e08d500d841c6c0419f6d3240a61926a085ef079` | `a7e36da6ceb5332454e69147f6231e83485787d535159ab6a82d8976de5d12ee` |
| actual target `2` | `i-0f089e64c378f5da3` | `F_32003/slimgb` | `76aacf8431f46705eb5c7347e08d500d841c6c0419f6d3240a61926a085ef079` | `962903e41a1f2e0e26b749597da22b02555bedbb7dcfe6ad97fd3b7c117dd9e3` |
| actual target `2` | `i-040b7a1c2ed72d4cc` | `F_65521/std` | `76aacf8431f46705eb5c7347e08d500d841c6c0419f6d3240a61926a085ef079` | `b35373c4567becb09851a71ab892fe7354d4a4d337e440b8f1752448ad7467cf` |

The target-`3` mutation and all four actual lanes returned the unit ideal;
the actual lanes' printed results are byte-identical.  The direct coefficient
certificate makes this engine-independent.

## Scope

This closes only the complete invariant-ring cell whose pullbacks have total
degree at most six.  Terms first appearing at pullback degree eight, other
`(mu,r)` values, and the full quartic horn remain open.  In particular this
is neither a rank-four exclusion nor a proof or disproof of JC2.
