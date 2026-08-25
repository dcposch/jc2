# AWS-only canonical zero-section next-carry discriminator

This successor consumes the frozen 64-state canonical Q8-to-Q7 sampler.  At
each sampled canonical Q9 state it fixes the reported Q8 fibre coordinates to
the zero vector, solves the full Q7 affine system, and exhausts every point of
the resulting Q7 solution fibre against the exact degree-12 through degree-9
divided high carry.

The calculation is deliberately narrow.  A zero-section failure does not
exclude the other 17 Q8 fibre directions surviving the Q7 equations, and 64
sampled Q9 states do not exhaust the canonical Q9 chart.

