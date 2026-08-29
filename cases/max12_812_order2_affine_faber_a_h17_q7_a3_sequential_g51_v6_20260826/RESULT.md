# Result: H17/q7/a3 sequential reduction through grade 51

Date: 2026-08-26

Status: **DUAL-AWS PASS; FINITE NORMALIZED PRODUCER, HOSTILE REVIEW
REQUIRED.**

The exact-Q Box03 lane and independent F65521 Box02 control both passed
the preregistered sequential reduction of the complete frozen V5 rows.
On each of `D(x0*p*m*a3)` and `D(y0*p*m*a3)`, 21 literal Laurent pivots
solve the five registered variables at every grade 48--51.  All twelve
`P5,P7` compatibilities in grades 48--50 vanish exactly.

At grade 51, after the five ordinary pivots, the reducer verifies the
literal identities

```text
K51 = P5_51,
H51 = 16*p*P5_51 + 64*P7_51.
```

The remaining `K51=P5_51=0` equation solves the free leading correction

```text
d60 = 36*(r00*m^2-y0^2)/p^4
      -5*kk0*a3^2*p - 2*m^3/(a3*p^4).
```

Here `y0=0` on the `D(x0)` chart after its cross-kernel pivot; the full
display remains on `D(y0)`.  After this solve, `K51=P5_51=0` and the sole
remaining grade-51 equation on both charts is

```text
64*P7_51 = H51
          = -2*m^3*p^2 + (5/4)*kk0*a3^3*p^7.
```

Thus the fixed boundary does not die through grade 51.  It lands on the
candidate rational/Kummer receiver

```text
5*kk0*a3^3*p^5 - 8*m^3 = 0.
```

It is rational when solving for the campaign load variable `kk0`; over a
fixed `kk0` it is a cubic Kummer sheet.  The complete final Laurent
solutions and residuals are preserved in `chart_reductions.json` for each
lane.

## Evidence

- immutable source/input manifest SHA:
  `ba04614debcc85e590f716ec966deae7d13fbd9ffbfee39f6596dd4748b88904`;
- exact-Q reductions SHA:
  `44fc3d616b241047198612d0020be6217f49fe511ecb6150fa68189e1cae8d6d`;
- F65521 reductions SHA:
  `2c1b0acda6c3244a7a60df192ebb04ebad4c3bdd7f136fde2114b78141227692`;
- both external validators say
  `PASS_A_H17_Q7_A3_SEQUENTIAL_G51_V6`.

## Scope firewall

This is finite prolongation only, in the fixed normalized
`(H,q,ord(a))=(17,7,3)` graph and registered localizations.  It is not an
all-orders arc, a literal-source/total-Rees accessibility theorem, a
terminal `[6,2]` or Taylor calculation, or an order-two,
maximum-twelve, JC2 closure/counterexample.  Hostile review is required
before promotion even at this finite scope.
