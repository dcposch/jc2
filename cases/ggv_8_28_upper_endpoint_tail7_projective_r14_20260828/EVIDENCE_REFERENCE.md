# Evidence custody

The 8-variable block is not recomputed under a new name.  Its exact ordered
terms are frozen at:

`../ggv_8_28_upper_endpoint_tail7_branches_20260828/BRANCHES/shared_block.json`

- full JSON SHA256: `3e586cc283526efa9c12f51f5be5535d31eaa1b03ee0296783438acabf9feaab`
- ordered canonical term-list SHA256:
  `30607ce7a81e6cbd6d5a8eca54087281399c2835ff68f0945a88c092963d4257`
- exact-Q Singular source SHA256:
  `458dce839bce84004be992e146603f05dbce4a1716c5717a4c7ac130e2e1707c`

Audited AWS output is frozen at:

`../ggv_8_28_upper_endpoint_tail7_branches_20260828/AWS_R6D_SHARED_BLOCK_20260828T010806Z/`

- `engine.stdout` SHA256:
  `85d3aad67e459f6f7d8e84556ccfc462cf15eff6ed37ab51a21cda2559eb64c0`
- `engine.stderr` SHA256:
  `f939e5f9a18e9dac4fbe2743dc7f4542bdeb310460f825fb61ce5a468ad63ee9`
- `METADATA.txt` SHA256:
  `1279e540e7817b794d52c6cd8ee16219467827ec2afee4fa1488596349f4716b`
- evidence manifest SHA256:
  `559c028e258c344179b65f7e45f517e1265be9ff3e433a6791ee88ac5b998ccc`

The stdout literally contains `BASIS_SIZE=1`, `UNIT=1`, and `J[1]=1`.
The AWS run used `/usr/bin/Singular` SHA256
`90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`,
one core, an 8 GiB memory cap, a 1,800 s time cap, zero swap, and terminated in
0.07 s with 10,328 KiB maximum RSS.

The separate local `liftstd` certificate and direct identity replay are under
`LOCAL_REPLAY/`.  They are an independent exact-Q certificate, not a replacement
for the audited AWS custody chain.
