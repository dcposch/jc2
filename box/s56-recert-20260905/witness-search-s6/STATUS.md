# S6 `[1]` exact-rational witness search

## Outcome

**No exact rational sample point was found.**  This search therefore supplies
neither a `SURVIVES` witness nor evidence for `UNIT`/death.  The full
source-complete S6 `[1]` chart (212 parameters, 315 coefficient rows, with
Rabinowitsch equation `c*T-1`) remains outside the scope of every negative
specialized screen below.

The acceptance gate for a prospective survivor was deliberately strict: a
candidate had to lift to rational source variables, satisfy every one of the
315 emitted rows and `c*T=1`, reconstruct `P,Q`, and pass the direct identity

```text
J(Q,P) = c*x^8,       c != 0
```

over `Q`.  No modular hit reached that gate, so no sample point, dimension, or
basis is claimed.

## Legal specializations and parameterization

The emitted builder writes

```text
h = y^3 - x*y^2 + sum h_a_b*x^a*y^b.
```

Thus the assignment `h_1_2=1` and all other `h_* = 0` is a literal source
specialization, not the deletion of an unknown by a weight floor: it cancels
the displayed `-x*y^2` and gives `h=y^3`.  On this slice,

```text
Q = y^6 + b2(x)y^2 + b1(x)y + b0(x),
P = y^9 + sum_{s=0}^8 p_s(x)y^s,
deg_x(b2,b1,b0) <= (12,15,18),
deg_x p_s <= 27-3s.
```

The broader fixed-`Q` search used the centered direct form

```text
Q = y^6 + q4(x)y^4 + q3(x)y^3 + q2(x)y^2 + q1(x)y + q0(x),
deg_x q_r <= 3(6-r),
P = y^9 + sum_{s=0}^8 p_s(x)y^s,
deg_x p_s <= 27-3s.
```

This is also a legal source specialization.  In characteristic different
from two, set

```text
h  = y^3 + (q4/2)y + q3/2,
B2 = (q2-q4^2/4)y^2 + (q1-q4*q3/2)y + (q0-q3^2/4).
```

The support bounds are preserved.  Euclidean division then uniquely writes
any bounded monic `P` as `h^3+A1*h^2+A2*h+A3`, with each `A_i` in its completed
source support.  A constant can be subtracted from `Q` and from `P` to impose
the emitted `B2_0_0` and `A3_0_0` gauges; those translations do not alter the
Jacobian.

For the finite-field coefficient-orbit checks, the group element is explicit.
For `lambda,mu != 0`,

```text
Q'(x,y) = mu^-6 Q(lambda*x,mu*y),
P'(x,y) = mu^-9 P(lambda*x,mu*y),
c'      = lambda^9 mu^-14 c.
```

It preserves monicity and nonvanishing of `c`; a coefficient of `x^e y^r`
in `Q` transforms by `lambda^e mu^(r-6)`.  The orbit programs enumerate this
action rather than silently setting coefficients to one.  By contrast, the
older `[1,1,C]` runs in the table are reported only as slices: dependent
weights and nonsurjectivity modulo `p-1` prevent treating that normalization
as exhaustive.

## Fixed-`Q` solver and checks

For fixed centered `Q`, all Jacobian equations are linear in the 144 bounded
coefficients of `P`.  `reduced_centered.py` eliminates the coefficients of
`y^13,...,y^5` in descending order.  The leading contribution is
`-6*p_s'(x)`; integrating determines `p_8,...,p_0` and leaves nine
`x`-constant integration parameters.  It then enforces every degree overflow
and every remaining `y^4,...,y^0` coefficient, while reserving only
`[x^8 y^0]J` as the target functional.

`validate_fixed_q_reduction.py` compared this recurrence with the independent
all-144-variable row constructor in `search_linear_q.py` for 250 deterministic
random centered `Q` over `GF(32003)`.  Consistency and the possibility of a
nonzero target agreed in every trial; the recorded result is
`fixed-q-reduction-validation.json`.  A separate read-only audit also checked
the Jacobian sign, recurrence sign, source bounds, and 200 reconstructed random
instances by direct Jacobian expansion.

## Completed searches

Every row below ended with zero hits.  Counts are executions, not disjoint
geometric points; several families overlap.

| family | field | checked | scope / custody |
|---|---:|---:|---|
| `h=y^3`, each of `b2,b1,b0` absent or one unit monomial | 32003 | 4,759 | `monomial-p32003.json`; 6.48 s, 13,948 KiB |
| `h=y^3`, target-degree exponent triples, `[1,1,C]`, all `C != 0` | 32003 | 22,305,394 | `reduced-allfield-p32003.json`; normalization slice only; 20:08.34, 13,792 KiB |
| alternate dependent-weight monomial slices | 32003 | 704,044 | `monomial-degenerate-allfield-p32003.json`; 31.73 s, 13,344 KiB |
| fully collinear `(4,5,6)` slice, 24 first coefficients and all last coefficients | 32003 | 768,048 | `monomial-collinear-p32003.json`; still a slice |
| even `Q=y^6+x^ea*y^4+x^eb*y^2+C*x^9`, all `C != 0` | 32003 | 2,912,182 | `even-allfield-p32003.json`; narrow even slice; 17:36.51, 13,680 KiB |
| centered three lower terms, `[1,1,C]`, `C in {+/-1,...,+/-12}` | 32003 | 1,048,320 | `centered-k3-smallcoeff-p32003.json`; slice; 34:48.56, 13,748 KiB |
| centered three terms selected by the older restrictive `(14,9)` filter | 101 | 232,600 | `centered-relevant-k3-p101.json`; checked subset only; 4:15.08, 13,456 KiB |
| safe-target supports with one nonzero lower term, all coefficient orbits | 29 | 2 supports / 2 orbits | `centered-k1-all-target-orbits-p29.json` |
| safe-target supports with two nonzero lower terms, all coefficient orbits | 29 | 238 supports / 788 orbits | `centered-k2-all-target-orbits-p29.json`; 1.14 s, 13,732 KiB |
| safe-target supports with three nonzero lower terms, all coefficient orbits | 29 | 10,484 supports / 449,736 orbits | `centered-k3-all-target-orbits-p29.json` |
| safe-target supports with four lower terms, all four coefficients equal to one | 32003 | 260,732 | `centered-k4-unit-p32003.json`; slice; 9:56.14, 13,684 KiB |
| `h=y^3+x^eu*y+x^ev`, `B=C*x^eb*y^rb`, `C in {+/-1,...,+/-12}` | 32003 | 78,960 | `huvb-smallcoeff-p32003.json`; natural completed-support slice; 4:59.75, 13,636 KiB |

The current safe support filter is only a combinatorial necessity for an
`x^8 y^0` target.  It includes the possible contribution of an arbitrary
integration constant in `p_1` or `p_0`; this gives 10,484 three-term supports,
not the older 2,326-support count.  On those supports the `GF(29)` orbit run is
exhaustive for nonzero **base-field** coefficient triples modulo the displayed
`x/y` torus.  It is not an exhaustive search over algebraic extensions, dense
`Q`, or rational points, and a rational point can also have bad reduction at a
chosen prime.

## Interpretation and handoff

- No exact rational survivor was constructed.
- No full-row exact verification was run because there was no candidate to
  verify.
- No negative specialization is promoted to a full-chart `UNIT` result.
- The result of this witness lane is therefore **negative/inconclusive** for
  the 212-parameter S6 `[1]` chart.
- All processes started by this witness search have exited; no worker or fleet
  resource was launched.

The principal reproducible programs are `search_linear_q.py`,
`reduced_centered.py`, `validate_fixed_q_reduction.py`,
`search_centered_orbits.py`, `search_centered_orbits_lowk.py`,
`search_centered_k4_unit.py`, and `search_huvb_slice.py`, all in this directory.
