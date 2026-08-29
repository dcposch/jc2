# TD6 V89H10T all-q simultaneous triangular-flag result

Date: 2026-08-26

Verdict: **PASS as an exact producer-tier transported-FIRST theorem; P12 was not reduced.**

On the frozen V89H10G `F=0` specialization over the registered open
`D(U*H*B3)`, rebuild all 38 literal FIRST rows with the 22 licensed,
independent variables `q2,...,q14,q16,...,q24`.  For the registered relative
pivot matrix

```text
B(q) = A(0)^(-1) A(q),     N(q) = B(q)-I,
```

the exact digest of `N` is
`38fb14e38daa36d597cc7ae1cd2bd5dd402ef2cd1587337321b8c204eeeb7f36`.

The thirteen coefficient matrices of `q2,...,q14` on the unique 14-node
SCC admit a complete common invariant flag.  At every successive quotient
dimension 14 down to 1 the common kernel has dimension exactly one.  The
emitted constant basis `S` and its inverse are exact two-sided inverses;
both have 79 nonzero entries.  In this basis every low-q coefficient matrix
is strictly upper triangular.

Extending `S` by the identity to the other 24 coordinates and applying the
emitted topological order makes the full, all-22-q matrix `N` strictly upper
triangular.  The resulting artifact contains 2,989 nonzero q-coefficient
terms.  Hence, without expanding a monolithic inverse,

```text
(I+N)^(-1) = I-N+N^2-...+(-N)^37
```

is an exact two-sided polynomial inverse.  In particular the full relative
FIRST pivot matrix is unimodular in the q variables on this specialized
registered open.

The basis denominator ledger is fail-closed and contains only licensed
factors:

```text
S:       U^4 V^4 (V^2-4U^3)^2
S^(-1): U^5 V^4 (V^2-4U^3)
```

up to units.  No q variable was specialized in the flag construction or
the final full-matrix check.  Both AWS runs returned rc 0 with byte-identical
stdout and mathematical artifacts.

Custody:

- Source archive SHA `6fb15850c4e6c4b92039c584c30700295602f2a1c65f048724789cda8a19cb9c`.
- `SOURCE_FLAG.sha256` SHA `67a94374f3ca2585713480477f7aa93caf82c1a79192ecd3d33773c9bc2cdcde`.
- Client SHA `9c7a5eeede117568aa76d4c26bae11f6e78640313cad6ad559b414ee2cf5098c`.
- Byte-identical stdout SHA `554a5d43f5c1b484b8f62ee92c067c439cee47bb9e6ab77a6e4bb19667b6e8f9`.
- Common-flag telemetry SHA `89db0510983c95cd5c8b62e6a04ab3675939c62f1f5c2605d9add475cdad12c2`.
- Basis SHA `05f9b3df78dc4abcf6ad39c36e1b48c54529b351459664cccfa3cd59d49d1542`.
- Basis-inverse SHA `30e644c244f65b17cbf9d7a599b60883d1e8c0b1dd6c3fb326c8ae70cda87aac`.
- Strict-upper order SHA `35e88aa807ba6a4a0e275f946c23e86b0b3e8fa8aa155684103a08ae13cacb6a`.
- Strict-upper matrix SHA `946b75e5307941a81696ec68e1ae2fbcb6ce480294cead6076e434d8e819e913`.
- Denominator ledger SHA `5ebfa2b9d693974a21ae0622bf5e5f1aa701e3b2c802952d56d678c6278b8956`.

This producer theorem does **not** reduce P12, extend the reviewed H7/H8
functionals to arbitrary low q, prove a unit ideal or source-point exclusion,
totalize the q15 target shear, supply a total-Rees chart, close all of TD6,
or resolve JC2.  All substantive computation ran on AWS; `jc2-lean` was not
touched.
