# Quotient-adapter correction

Date: 2026-08-28

This sidecar supersedes every mathematical rank, minor, gcd, factor, and
rank-locus claim in the r2/r3 packets for the six quotient-ring branches
`P`, `C8P02`, `Q1P02`, `Q1P03`, `TRIPLE02`, and `TRIPLE03`.

The old adapter carried unreduced polynomial representatives through matrix
reduction and determinant/factor parsing in a quotient-ring presentation.
The adversarial instance is decisive: on a branch containing `q2=0`, a
displayed factor `q2` was treated as nonzero instead of first reducing to
zero modulo the pinned standard basis of the branch ideal.  Consequently,
those six r2/r3 branch packets are **ADAPTER_FAILURE / NO_VERDICT**.  Their
bytes and hashes remain preserved as failure evidence; they are not erased
or silently repaired.

The following three ordinary polynomial-ring packets do not use a nonzero
quotient ideal and remain exact, within their registered census-only scope:

| Branch | r2 exact result | r3 exact result | Strict scope |
| --- | --- | --- | --- |
| `C8` | 95 rational-unit pivots; residual rank 9; total receiver rank 104 | 550 signed 9-minor slots preserved; 133 nonzero; ambient common-gcd diagnostic `q1^5*(5*q0^2-6144*c6)` up to literal rational unit | Fitting/minor census only; no endpoint or component verdict |
| `Q1` | 95 rational-unit pivots; residual rank 6; total receiver rank 101 | exact 4-by-8 plus 7-by-2 block support; ranks 4 and 2; raw block-minor census | Fitting/minor census only; no endpoint or component verdict |
| `C8_Q1` | 95 rational-unit pivots; residual rank 6; total receiver rank 101 | exact 4-by-8 plus 7-by-2 block support; ranks 4 and 2; raw block-minor census | Fitting/minor census only; no endpoint or component verdict |

Ambient gcd/factor displays remain diagnostics only.  They are not proofs in
a coordinate ring and no cancellation, radical equality, saturation, or
scheme equality is inferred from them.

## Exact terminal packet hashes

| Branch | r2 terminal archive SHA-256 | r3 terminal archive SHA-256 | Status after correction |
| --- | --- | --- | --- |
| `C8` | `ec13fb990a35f0a3c02da2bcbbfb3a99b21a8f3cae180e3a712a5431a3802c02` | `6350b3d5b29fde13a80839ac9342d7684511eaafc553cf4cd2d631136012eaed` | exact ordinary-ring census retained |
| `Q1` | `15b91c08c47bb933ce5d9231bf602d09c8e4fd290d466e2fb8fb5d07599c3a4d` | `db20796d45eaeb03f38ea0a235ff4e9dd406c773acd7574de0642a7237c820c8` | exact ordinary-ring census retained |
| `C8_Q1` | `fc773ba8745876fc1d95dc39e44f298e34b2dbc2bdc2056ab561491828b3211c` | `e0b0a3c47d6210d8f810379044271dd3b371a3a97f2ae46403533e7aa7699a98` | exact ordinary-ring census retained |
| `P` | `b3f9024711176a00c62460179b526d25748ef6a0258b24af7788538cbb0737ec` | `de79b639c5b187ce2b493bec5890468c34ae104254c27effdd2271d6eb09b2e7` | **ADAPTER_FAILURE / NO_VERDICT** |
| `C8P02` | `3f2db20b34a94ee5b63669e1c20c46cb2c2e52cede3ee90d03708f282373bc8f` | `83b4b39f6c04bff64e7f6ed43c15aa5949a143a1ea40595457bcfd2764e34ac5` | **ADAPTER_FAILURE / NO_VERDICT** |
| `Q1P02` | `62731094b8c25128ca8f69682fcc9a23046f0c96a4981ed1f89896ccab4598b5` | `2545f54015864949bebc38dc298f17ad360a5c62d3c068a6be5d6631a8040480` | **ADAPTER_FAILURE / NO_VERDICT** |
| `Q1P03` | `3ff39d779654e8f0726e6084c25f77151416f36dcfb6a927c667efcc56c6a8c0` | `65e79be3ce70d9e1e9f19bea552feb0ce30db9ffda7c4ccfa06309124a8fef7b` | **ADAPTER_FAILURE / NO_VERDICT** |
| `TRIPLE02` | `09ad7d9e39c15b3dd9bf760cee7b7de6a04ae2a36aecd8aa53efa0a864f62e33` | `2a455f90c09bd91bbd3a41a5944db0214e5d0b23d41f46653c3033b72379a83c` | **ADAPTER_FAILURE / NO_VERDICT** |
| `TRIPLE03` | `ed93f709c86430b490096a02179fac1b1320dd8b50917db00c95ccce858c248f` | `a73b2c096cddc262f0d6a7daaaac8c63ed576c5fe79b53dbfccab397bb6a81a5` | **ADAPTER_FAILURE / NO_VERDICT** |

## Replacement contract

The reducer-safe successor must use one ambient polynomial ring with a
pinned `std(I)` for each exact stratum.  Every matrix entry, row-operation
result, determinant, and minor must be normalized against that same standard
basis before zero/nonzero or factor parsing.  Rank `r` requires both an exact
`r`-minor with nonzero normal form and the vanishing normal form of every
`(r+1)`-minor, or an equivalent exact fraction-field/structural-support
certificate.  Its mandatory negative control presents `q2` on a `q2=0`
branch and requires normal form zero before any rank/factor logic.

