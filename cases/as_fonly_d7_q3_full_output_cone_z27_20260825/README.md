# Complete fixed-D7 output cone modulo 729 at three pinned Q3 fibres

Status: **PRODUCER-EXACT / PROVISIONAL PENDING DIFFERENT-MODEL REVIEW**.

The source-first calculation consumes the three reviewed Q3 fibres `0000`,
`0270`, and `0513`.  For each it writes

`F = F0 + 27*T`, `T in (Z/27)^72`,

where all coefficients of both degree-at-most-seven output polynomials are
present.  Exact bilinearity gives

`det J(F)-1 = D0 + 27*A*T + 729*det J(T_P,T_Q)`.

Consequently the complete 91-row determinant condition modulo 729 is the
linear congruence `D0/27+A*T=0 mod 27`.  Three exact F3 Bockstein stages solve
the entire prior modulo-243 modules; no point enumeration or representative
extrapolation is used.

| Q3 fibre | mod-3 rank/kernel | mod-9 rank/kernel | mod-27 rank/kernel | liftable prior dimension | new solutions |
|---|---:|---:|---:|---:|---:|
| `0000` | `27/45` | `36/81` | `47/106` | `61` of `81` | `3^106` |
| `0270` | `27/45` | `43/74` | `49/97` | `52` of `74` | `3^97` |
| `0513` | `27/45` | `43/74` | `49/97` | `52` of `74` | `3^97` |

The particular modulo-243 representative previously printed at each fibre
does not lift, but the complete fibre does.  Each reconstructed survivor has
literal integer determinant congruent to one modulo 729 in every one of the
91 coefficient slots.  All 1,296 P/Q pair controls and 1,008/720/720
Q3-kernel/fresh mixed controls pass.

Two AWS hosts replayed identical source bytes and produced byte-identical
result JSON per fibre:

- Box02 `ip-172-30-0-186`, job
  `/home/ubuntu/jobs/as_d7_full_output_z27_20260825T1545Z_box02`;
- r6d `ip-172-30-0-45`, job
  `/home/ubuntu/jobs/as_d7_full_output_z27_20260825T1545Z_r6d`.

These are independent executions of the same implementation, not independent
implementations.

## Scope firewall

This is complete only for the fixed-D7 output coefficients over the three
displayed Q3 fibres and only modulo 729.  It does not cover the rest of the
predecessor scheme or give an all-depth lift.

The next modulus is qualitatively different.  Modulo 2187 the term
`729*det J(T_P,T_Q)` survives, so the next gate is a quadratic Kuranishi carry
on the full `61`- or `52`-dimensional liftable prior stratum plus a linear
fresh order-729 digit.  No fourth global linear-Bockstein claim is licensed.
There is no collision, characteristic-zero point, counterexample, or JC2
conclusion.

`verify_frozen.py` checks hashes, both-host equality, ranks, counts, controls,
and refusal fields without re-running the algebra.  `replay_all.sh` is the
substantive source replay and must be run on AWS under campaign policy.
