# AWS registration: exact residual boundary/normalization certificate V1

Date: 2026-08-26

Status: preregistered; no endpoint consumed.

- tag:
  `max12_812_order4_mu4_nonzero_boundaryQ_v1_20260826T012200Z_box03`;
- host: Box03, instance `i-0ece0b9a3b4a7512f`, public IP
  `98.80.65.144`, expected hostname `ip-172-30-0-249`;
- remote directory:
  `/home/ubuntu/jobs/max12_812_order4_mu4_nonzero_boundaryQ_v1_20260826T012200Z_box03`;
- timeout `1800 s`; virtual-memory cap `16777216 KiB`;
- exact input SHA-256:
  `6cf48f3de77f0f6399f36e39184b3c3ff0c1355c30b96069a623a5da49efdb7c`;
- parent reconstructed candidate SHA-256:
  `706505e02f57e6991170e230738d6a8b96b5ac82ed2ec3fa83b1ba8ff498508d`;
- parent exact-membership stdout SHA-256:
  `9b0e08c2d826286364f07f6a6fba9560e23ca8ea4fcba15cbbcf373152badbe3`.

The client factors both degenerate boundary faces, verifies all torus
singularities are ordinary nodes, and checks smoothness of the curve at the
repeated left/top face roots using the first transverse coefficient.  A
genus-three sentinel is valid only if the exact residual polynomial is
irreducible, the torus singular scheme has length four with invertible
Hessian, and every repeated boundary root is smooth on the toric closure.
The other two edge faces are binomials with nonzero endpoint coefficients;
the curve misses all toric fixed points because every polygon-vertex
coefficient is nonzero.  This is geometry of the reconstructed relation,
not yet proof that the characteristic-zero elimination image equals that
curve or that a source map is nonconstant.
