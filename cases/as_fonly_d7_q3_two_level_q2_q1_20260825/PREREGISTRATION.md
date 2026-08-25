# Two-level accepted-digit Q2/Q1 successor

Consume the source-complete whole-kernel Q3 producer at SHA-256
`14d69e65255482491293373bbbd212742e2077322931e65b8d5af215915d303b`.
Its exact valuation table shows determinant degrees two and one have minimum
3-adic valuation three, not four, so an order-81-only continuation is
ill-typed.

Retain the entire Q3 affine kernel.  Add homogeneous order-27 pieces
`(W3,Z3),(W2,Z2)` and homogeneous order-81 pieces
`(H3,J3),(H2,J2)`.  Compile a triangular accepted-digit affine tower from the
literal integer determinant:

1. all 91 coefficient slots in degrees 0..12, divided by 27 modulo 3;
2. on the complete first zero-locus, the same 91 slots divided by 81 modulo 3;
3. on the complete second zero-locus, the 63 over-cap slots in degrees 7..12,
   divided by 243 modulo 3.

At every layer, retain the entire affine kernel, prove affineness by the full
quadratic design, and preserve rank-zero/drop strata.  A single global affine
system is not assumed: exact carries make the accepted-digit tower the typed
object.  Record whether each layer is genuinely affine after restriction.

On SAT, reconstruct the integer map and verify every determinant coefficient
is divisible by 243 and every degree-7-through-12 coefficient by 729.  Degree
zero is an explicit asserted control; if it becomes nonzero without a pivot,
stop and branch to `(C1,D1)` rather than clearing or discarding it.

Strict scope: pointwise finite depth under cap D=7.  No infinite lift,
algebraization, counterexample, or JC2 claim.  All substantive execution is
AWS-only.

