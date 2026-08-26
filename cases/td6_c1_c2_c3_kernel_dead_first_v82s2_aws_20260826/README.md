# TD6 V82S2 kernel-dead first-stage certificate

Status: **producer-exact; hostile review pending**.

This case freezes four independent AWS executions of the corrected V82S2
source: axes `d10` and `d15`, each on r6d and Box03, over the generic
symbolic-center field `E(C,V,U)`.  Every execution returned `rc=0`, replayed
the exact 3,470-row transport echelon, retained a nonzero raw first-band
source column with an omission-zero control, and found its first-stage
dependent conormal table exactly empty.

## Exact result

For both transport-kernel dead axes:

- first rank is `38/132`, with no dependent compatibility row;
- the first conormal rank is `0/1` and its denominator is the unit `1`;
- the actual and synthetic empty-table paths are the exact header-only byte
  string with SHA256
  `68b4a3a151d2eb15e04b6bb1b0bb6e5656423289e4dca1260844476105ea6692`;
- the raw source columns are nonzero: d10 has 1,108 entries, SHA256
  `e9c830bf3bc0abbc6a91b1e38a227ac0ae61b40bbeabf4e233dce62450f730f7`;
  d15 has 739 entries, SHA256
  `4ea40ca645ec2dd523db2b85ab67cdf1b3c82fe28eb610a5220a44deedbb66ab`;
- removing that source column gives the empty SHA256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

After replacing only hostname, run tag, and absolute run root, the two host
stdouts are byte-identical for each axis.  Their normalized hashes are
`a586c3b473f5cff53939dc5a682ab1da45aff6c3e541f148c2aa39e0fdb24c15`
for d10 and
`359df41d98d795657a08cf02b4175602d0d1e711f851da3c9c87524119397245`
for d15.

Together with the frozen V81C transport statement (rank nine with kernel
the 22 q axes plus d10,d15) and the separately hostile-reviewed V78 q-first
zero statement, this gives the conditional exact composition that the same
24-dimensional transport kernel survives the first gate.  V81C itself is
still producer-tier, so that composed statement remains producer-tier until
review; the present case independently proves only the two dead-axis
first-stage columns.

The scope is strict generic fraction-field, fixed source-typed A3,
square-zero transport-plus-first source incidence.  It is not previous,
pole, current, second-order, nonlinear, a family, full TD6, SP-2, or JC2.

## Custody

- Source archive SHA256:
  `1def8eb0d2e84451a3112c3d3679dde879706bb361267b32f2fbe4b9c6467545`.
- Source manifest SHA256 before archiving:
  `3ee58bcd1437611e2698bf9c1d4c628a47c1a4c6c5177748f111908fbe8f4d4b`.
- r6d run root:
  `/home/ubuntu/runs/td6_v82s2_dead_first_r6d_20260826T0320Z`.
- Box03 run root:
  `/home/ubuntu/runs/td6_v82s2_dead_first_box03_20260826T0320Z`.

Run the lightweight hash/text verifier with:

```bash
python3 cases/td6_c1_c2_c3_kernel_dead_first_v82s2_aws_20260826/verify.py
```
