# AWS registration: corrected-V2 multiprime exact plane reconstruction

Date: 2026-08-26

Status: preregistered; no endpoint consumed.

- tag:
  `max12_812_order4_mu4_nonzero_plane_multiprime_v2_20260826T011500Z_box03`;
- host: Box03, instance `i-0ece0b9a3b4a7512f`, public IP
  `98.80.65.144`, expected hostname `ip-172-30-0-249`;
- remote directory:
  `/home/ubuntu/jobs/max12_812_order4_mu4_nonzero_plane_multiprime_v2_20260826T011500Z_box03`;
- outer timeout `7200 s`; virtual-memory cap `134217728 KiB`;
- engine: corrected-V2 source, 32 frozen primes, CRT/rational reconstruction,
  then exact characteristic-zero `modSat`/`modStd` membership,
  factorization, torus-node Hessian, and boundary-face checks;
- corrected source SHA-256:
  `5b401beac071a22ec9ad3fc022bf9f87a255e40fdb141359f4bdc40d8547fa47`;
- generic prime compiler SHA-256:
  `09071c833a572bac81ccc32c48db8d65b89a36691a7eff1413ce49f19aed7a23`;
- reconstruction SHA-256:
  `2c8202bfb9da57dd0d15b37f5e0556ffd27680128a336db1f17e307d45ee1a1d`;
- exact verifier compiler SHA-256:
  `6341dfd38a83b5681dcba7dcf9c06a5e2f7ff4fa6ea549734dd553474e2f2178`;
- runner SHA-256:
  `54bfd104fc262b922e0cc372e3e48e86c599bb07b18583610c909bdf0f00fbdf`.

The source archive was transferred before launch and verified on
`ip-172-30-0-249` at `2026-08-26T01:16:12Z`; its SHA-256 is
`685253af86977d1cff6e0ddee029de08c2b77b930dcb15c2bf56fa974ccf259a`.

The frozen primes are

```text
32003 32009 32027 32029 32051 32057 32059 32063
32069 32077 32083 32089 32099 32117 32119 32141
32143 32159 32173 32183 32189 32191 32203 32213
32233 32237 32251 32257 32261 32297 32303 32309
```

Every prime must reproduce the same 18-term support, saturated dimension
one, a principal irreducible plane relation, and the normalized coefficient
of `a5^2*a6^21` equal to one.  Rational reconstruction must stabilize at
16, 24, and 32 primes and replay every residue.  The reconstructed relation
is only a candidate until exact membership in the corrected-V2 saturated
ideal passes.  Exact membership alone is not an elimination-equality or
source-obstruction theorem.  Any missing sentinel, unlucky prime, unstable
reconstruction, failed exact factorization, or failed Hessian/face check is
**NO VERDICT**.
