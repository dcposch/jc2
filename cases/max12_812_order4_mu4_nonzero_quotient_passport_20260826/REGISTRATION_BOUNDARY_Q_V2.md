# AWS registration: exact residual boundary diagnostic V2

Date: 2026-08-26

Status: preregistered repair of failed-closed V1; no endpoint consumed.

- tag:
  `max12_812_order4_mu4_nonzero_boundaryQ_v2_20260826T012600Z_box03`;
- host: Box03, instance `i-0ece0b9a3b4a7512f`, public IP
  `98.80.65.144`, expected hostname `ip-172-30-0-249`;
- same-named directory under `/home/ubuntu/jobs/`;
- timeout `1800 s`; virtual-memory cap `16777216 KiB`;
- exact input SHA-256:
  `f0381bbfc766f6f1a8b2d3f274dcb714175a4e4d8f209df0983bf8d04b7838a3`;
- reconstructed candidate SHA-256:
  `706505e02f57e6991170e230738d6a8b96b5ac82ed2ec3fa83b1ba8ff498508d`.

V1 is retained as a failed-closed diagnostic: it omitted `elim.lib`, so its
`sat` call was undefined and no normalization/genus sentinel is valid.  V2
adds the missing library, prints factor multiplicities for the left/top and
lower coefficient faces, repeats the exact four-node/Hessian certificate,
and identifies exactly which top repeated roots also kill the first
transverse coefficient.  It is diagnostic only; a complete local delta or
geometric-genus claim is a successor theorem.
