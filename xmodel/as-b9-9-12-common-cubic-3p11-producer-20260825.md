# Producer report: normalized B9 common-cubic family at `3^11`

Date: 2026-08-25  
Status: **PROVISIONAL PRODUCER WITH SOURCE-INDEPENDENT AWS REPLAY; HOSTILE REVIEW PENDING**

## Corrected integral gate

Over the complete displayed normalized coefficient box, impose without
division by three

```text
H = y^3 + h1*x*y^2 + h2*x^2*y + h3*x^3,
P9 = P_(0,9) H^3,
Q12 = Q_(0,12) H^4,
h1,h2,h3 = 0 (mod 3),
P_(0,9), Q_(0,12) units.
```

There are 276 determinant rows and 23 top-form rows.  The V3 formula uses
64-bit gates, reduces arithmetic operands modulo `177147`, but encodes the
positive modulus/divisor itself as a raw 64-bit constant.  Its complete
constructor audit records 14 residue calls and exactly two raw-modulus calls.

Dual Box03/r6d emitters give byte-identical:

```text
canonical SMT  5af9efbe4b138f1cb0408099c90283842b4ef0b0fef9d7d33447d51a29d53563
Boolector SMT  2eb69355a0b85b6928899a619840ecb7856ee6e6cc2ef050ab76067e44c835f7
patched source 7dfe73ea02f68434b1a548c51b69353a50e4d593f2d3e404e64c13790f49a98c
emitter result 45a79eedbfcec2cd24b60f0fc5a5b3a91b25c2c6fdcd6f4f17afa433c2bcd4fe
```

The canonical formula is byte-identical to the independently repaired audit
formula.

## Independent complete-family construction

An independent AWS compiler at source SHA-256
`460199584e128bc2c5f3196871a34437ebdfd7d674ccf0bcc2f52b9db8ace6b8`
does not consume the producer SMT.  It constructs the 299-row common-core
system directly from the pinned parent and obtains:

```text
modulus       rank    complete family dimension
3^6 = 729       94    55
3^7 = 2187     123    81
3^8 = 6561     131    99
3^9 = 19683    132   116
3^10= 59049    132   133
```

At `3^10 -> 3^11`, the 149 fresh coordinates have rank 94, kernel 55,
and cokernel 205.  The 133 predecessor directions split into 17 active and
116 spectators.  The spectator image has rank 38, and every coefficient of
the active quadratic carry lies in that image: the post-elimination system
has zero equations.

Thus the liftable predecessor projection has exponent
`17+(116-38)=95`; adjoining the 55-dimensional fresh kernel gives a complete
displayed mod-`3^11` family of cardinality `3^150`.  This count is provisional
pending hostile audit of the independent parameterization and containment.

## Literal witness

The independent witness payload has SHA-256
`a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a`
and

```text
H coefficients mod 177147 = [1,119880,40581,0].
```

A separate replay implementation at source SHA-256
`eba7d223b88fd61da246fd766a3c5f4f73163e9b0261263d64406779671d6689`
checks all 276 determinant rows and all 23 common-cubic rows modulo 177147,
the fixed displayed B9 parent modulo 243, leading units `(2,1)` modulo 3,
and exact degree pair `(9,12)`.  Replay-result SHA-256 is
`2008726f5791b86b3c4f6e5b296cbbf4cdfa91766290c1d32aeec81e4a52c67a`.

The raw V3 Boolector/Z3 searches were stopped after this independent exact
SAT witness landed; they are retained only as resource/deployment custody,
not as solver evidence.

## V2 quarantine and refusal scope

V2 reduced its modulus constant to zero and is fully retracted in
`xmodel/as-b9-9-12-common-cubic-v2-zero-divisor-erratum-20260825.md`.
No V2 solver or proof byte supports this report.

This result covers one fixed B9 mod-243 parent and its complete displayed
common-core congruence family only.  It proves no lift past `3^11`, no
inverse-limit or characteristic-zero point, no source-honest landing in all
maximum-twelve charts, no complete earlier-parent coverage, no
maximum-twelve theorem, no counterexample, and no JC2 claim.
