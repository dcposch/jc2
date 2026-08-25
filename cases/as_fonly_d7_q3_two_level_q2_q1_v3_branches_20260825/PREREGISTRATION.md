# Branch-normalized Q2/Q1 carry classifier V3

Consume V1 at SHA-256
`cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd`
and the V2 observation that canonical RREF coordinates make the `/81` carry
nonlinear.

For each of the three structural controls, derive the `/27` source matrix,
identify its exact nonzero-column cone, enumerate only that cone, and retain
every accepted active assignment.  For each accepted branch, keep all other
raw source digits (no arbitrary RREF representative), prove/check the `/81`
function affine by the complete quadratic design, and compute its exact RREF.
Then test the `/243` high-row function on the complete `/81` kernel.  If it is
affine, solve and literal-replay; if not, emit the first exact failed identity
and stop that branch without an inference.

This is an exact branch classifier, not a promise that `/243` is affine and
not a complete-map/all-depth/JC2 claim.  All execution is AWS-only.
