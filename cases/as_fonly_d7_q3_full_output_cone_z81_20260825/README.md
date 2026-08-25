# Fixed-D7 complete output cone modulo 2187

This is the first nonlinear successor to the frozen modulo-729 third
Bockstein.  It reconstructs the full modulo-729 affine torsor, compiles the
quadratic Kuranishi carry plus every fresh order-729 output digit, tests two
large linear zero strata, and otherwise emits a complete QF_BV formula.

Run only on AWS under the campaign compute policy.  Required environment
variables are documented at the top of `compile_full_output_z81.py` and are
provided by `launch_remote_one.sh`.
