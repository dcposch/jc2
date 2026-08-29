# Producer result: `p=0`, `D(rs*k0)` cusp grade-12 unit

Date: 2026-08-26

Status: **PROVISIONAL PRODUCER RESULT; DUAL EXACT-Q REPLAY PASSED.  HOSTILE
REVIEW REQUIRED BEFORE PROMOTION.**

## Exact conclusion

On the raw normalized cusp chart after the reviewed `M=0` gate,

```text
p=0,                 rs*k0 != 0,
c0=0,
5*k0*rs^3+96*c1^2=0,
15*k0*cs*rs^2+96*a0*c1=0,
u=c1/rs,
```

the complete seven-row source replay through absolute grade twelve gives the
grade-eleven unit pivots

```text
row(4,11)=-(864/25)*k^4*tau^6*ell1,
row(3,11) mod ell1=(18/5)*k^2*tau^3*e0,
```

and, before using any later triangular solution, the exact raw row

```text
row(6,12)=(18144/125)*k^5*tau^8
          =-(21/1024)*rs^3*u^2.                 (1)
```

Equation (1) is a unit on `D(k*tau)=D(rs*k0)`.  Hence the raw source ideal is
the unit ideal on this cusp open, provisionally excluding this open from the
post-`M=0` order-two square special fibre.

The unit is stronger than the preregistered quotient prediction: both exact
replays find the same expression in row six before reducing by the two
grade-eleven pivots.  Row six has no target; the first possible target grades
are 28, 32, 36, and 38.

## Source completeness and controls

The independent sparse collector imports neither the terminal DAG nor the
grade-10/11 Singular emitter logic.  Starting from the frozen canonical tails
it reconstructs the normalized primitive coefficient series, forms all seven
rows through grade twelve, and verifies:

- every row below grade ten vanishes and all normalized grade-ten rows vanish;
- all seven grade-eleven and grade-twelve rows are formed before reduction;
- the two displayed grade-eleven pivots and the unreduced grade-twelve unit;
- exact absence of a target from row six at grade twelve;
- the focused specialization `rs=u=1`, `s=a1=0`, `k0=-96/5`, in which exactly
  four frozen-tail contributions are
  `-9/1024,-3/256,+3/256,-3/256`, summing to `-21/1024`;
- nonzero controls `19859 mod 32003` and `5911 mod 65521`.

Dual registered AWS lanes on Box03 and r6d returned `engine_rc=0` and
`PASS_P0_CUSP_GRADE12_UNIT_REPLAY`; exact Q was completed before the modular
controls.  See `AWS_LAUNCH_METADATA.md` and `RESULTS.sha256` for custody.

## Exact scope and nonclaims

This result concerns only the raw `p=0`, `D(rs*k0)` cusp chart after `M=0`.
It does not treat the residual `V(rs,cs)` exact-square zero section, the
already separate odd chart `V(rs) intersect D(cs*k0)`, positive-valuation or
ramified moving-`p` overlap, `k0=0`, the nonsquare discriminant, any global
Taylor interface, all order-two arcs, maximum twelve, or JC2.  It is not a
scheme-theoretic statement beyond the displayed localized raw ideal.  The
modular controls do not carry a characteristic-zero claim.

