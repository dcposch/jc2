# Preregistration

Read exactly the 64 frozen canonical sampler outputs.  Fail unless their
indices, Q9/Q8/Q7 status, fibre dimensions, and zero RREF-coordinate witnesses
match the producer contract.  For each, emit the source JSON SHA-256, the
32-vector affine particular `y0`, its byte SHA-256, and its nonzero support.
Report the number of zero and nonzero `y0` vectors.  No inference beyond this
coordinate correction is licensed.

