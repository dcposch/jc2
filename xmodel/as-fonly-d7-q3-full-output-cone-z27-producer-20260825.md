# AS F-only D7: complete three-fibre output cones survive modulo 729

Status: **PRODUCER-EXACT / PROVISIONAL PENDING DIFFERENT-MODEL REVIEW**

## Result

At each of the three reviewed Q3 fibres `0000`, `0270`, and `0513`, the
complete degree-at-most-seven output-coefficient cone contains maps with
Jacobian determinant one modulo 729.

Write `F=F0+27T`, where `T` contains all 72 coefficients of both D7 output
polynomials modulo 27.  Exact determinant bilinearity gives

`det J(F)-1 = D0 + 27*A*T + 729*det J(T_P,T_Q)`.

Therefore, at this precision and no farther, the full problem is the linear
congruence `D0/27+A*T=0 mod27`.  The exact three-stage Bockstein calculation
gives:

| fibre | stage ranks / kernel dimensions | prior mod243 solutions that lift | mod729 solution count |
|---|---|---:|---:|
| `0000` | `27/45 -> 36/81 -> 47/106` | `3^61` of `3^81` | `3^106` |
| `0270` | `27/45 -> 43/74 -> 49/97` | `3^52` of `3^74` | `3^97` |
| `0513` | `27/45 -> 43/74 -> 49/97` | `3^52` of `3^74` | `3^97` |

The previously displayed mod243 particular at each fibre is terminal, but the
full fibre is not.  Each newly reconstructed particular passes literal
integer replay of all 91 determinant coefficients modulo 729 and reduces to
the Artin--Schreier seed modulo three.

## Controls and custody

- all 1,296 P/Q pair controls prove exact linearity modulo 27 after division
  by 27;
- all 1,008/720/720 Q3-kernel/fresh controls are divisible by 2187, so the
  reviewed Q3 fibre directions remain absorbed by complete D7 output digits;
- Box02 and r6d independently executed identical source SHA
  `f6eaa0a0f1dabb785bdd4358fa84739d907820bc539cc619a1b692ad5755cb19`
  and produced byte-identical result JSONs;
- output SHAs are `007b3f097e...`, `b7d571a23b...`, and `5d109dde44...`.

These are two executions of one implementation.  A different-model source
review is still required.

## Exact scope and next gate

The result is exhaustive over the prior `3^81` / `3^74` modules, but only at
the three displayed Q3 fibres and only modulo 729.  It does not cover the
whole predecessor scheme.

The fourth digit is not another global linear Bockstein.  Modulo 2187 the
term `729*det J(T_P,T_Q)` survives and varies quadratically over the
61- or 52-dimensional liftable prior stratum; a fresh order-729 output digit
enters linearly.  The correct successor is therefore a source-pinned
quadratic-Kuranishi/Fitting or exact trit-SAT gate on that entire nonreduced
stratum.  No all-depth lift, collision, characteristic-zero point,
counterexample, or JC2 conclusion is claimed.
