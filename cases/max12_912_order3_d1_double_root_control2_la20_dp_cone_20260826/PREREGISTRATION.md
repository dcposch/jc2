# Preregistration: independent-order `la^20` witness cone

This AWS-only successor replays the explicit Rees preimage extraction in
global `dp`, independently of the live LPDP extraction order.  Its compiler
consumes the byte-frozen LPDP compiler and B source only as pinned source
data, changes the ring order and unique markers, and appends an exact
term-by-term audit of the dehomogenized witness.

Required output:

1. the exact saturation exponent and composed Rees identity
   `s^N la^20=sum FINAL_i I_i+s^(N+1)TAIL`;
2. `P=la^20-TAIL|_(s=1)` with a checked identity in the unscaled ideal;
3. the exponent vector and fixed-weight value of every term of `P`;
4. exactly one weight-80 term, equal up to nonzero scalar to `la^20`, and all
   other terms of weight strictly greater than 80.

If successful, the displayed strict linear inequalities

```text
20*w_la < alpha dot (w_la,w_tau,w_rho,w_q1,w_q0,w_r2,w_r1,w_r0)
```

for each other exponent vector `alpha` give a certified open **witness
cone** on which this one polynomial continues to put `la^20` in the initial
ideal.  This is not yet a complete Gröbner fan/cone, parameter stratum, or
support census.

The same fixed-axis/load/support firewall applies.  Compiler/source identity,
AWS custody, literal lift residuals, rc zero, empty stderr, and all PASS
markers are mandatory.  No local compiler/CAS execution is permitted.

