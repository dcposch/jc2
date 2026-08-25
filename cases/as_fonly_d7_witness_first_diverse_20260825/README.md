# Diverse witness-first AS search

`compile_sample.py` consumes the frozen source prefix used by the reviewed
Q8-state sampler, but replaces its coordinate-axis selection with deterministic
combined-direction Q9/Q8 states.  It exhausts only the nine-dimensional Q7
fibre beneath each selected state.

All execution is AWS-only.  SAT hits require direct integer replay (already
performed in-lane) and a separately typed lifting-Jacobian gate.

