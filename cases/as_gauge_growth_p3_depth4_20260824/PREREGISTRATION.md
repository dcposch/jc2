# Freeze registration — AS-GAUGE-GROWTH-P3-DEPTH4-20260824

Frozen: 2026-08-24T14:47:14Z
Charged bank: 1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a

## Chronology disclosure

Exploratory derivation and private producer/audit replays preceded this
registration. This file freezes the coherent result, exact case split,
certificate, output markers, and refusal perimeter before registered repo
replay. It is not represented as a blinded preregistration.

## Frozen inputs

~~~text
2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b  xmodel/as109-bounded-polar-conductor-gate-20260824.md
bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa  xmodel/as109-bounded-polar-conductor-review-grok-20260824.md
aa07a878b41adfbe9e07beaa48aa793562fb49228ffae8982aa8773f600df4e2  cases/as109_bounded_polar_conductor_20260824/FREEZE.sha256
~~~

These inputs license the exact systems B_(p,n)(D_F,D_phi), the orientation
C_p o Phi_F=F, total-degree simplices, and the cotangent positive control.
They license neither a quantitative growth law nor a polynomial-lift
existence/nonexistence conclusion.

## Registered questions

1. Does coordinate comparison uniquely eliminate the gauge as
   A-A^p=P and B=Q(1-pA^(p-1)), while retaining its degree cap?
2. At p=3, what is the exact minimum equal cap D for depths two and three?
3. At depth four, are B_(3,4)(D,D) empty for D=5 and D=6, and does the
   cotangent point survive at D=7?
4. Do all nonlinear mod-81 carries, the divided determinant carry, and
   every smaller cap have an explicit dispatch?

## Frozen claim and failure perimeter

Allowed positive conclusions are the exact minima 3,5,7 at depths 2,3,4
and the explicit F_3 unit certificate

~~~text
(x^6y second-composition row)
 -(x^4 determinant row)-b_[x^2y] = 1.
~~~

The same-model independent checker may be used as a replay control and its
81-assignment exhaustions may be reported. It is not a substitute for the
required canonical different-model hostile review.

No result may claim the formula for n>=5, a positive asymptotic rate, an
all-depth lift, no polynomial lift, a p=109 computation, an A_infinity
identification, or a JC2 inference.

## Registered replay

~~~text
uv run --offline --no-project --with sympy==1.14.0 python \
  cases/as_gauge_growth_p3_depth4_20260824/replay.py

uv run --offline --no-project --with sympy==1.14.0 python \
  cases/as_gauge_growth_p3_depth4_20260824/independent_check.py
~~~

The first command must terminate with PASS-AS-GAUGE-GROWTH-P3-DEPTH4,
the three exact minima, and all refusal markers. The second must terminate
with PASS-INDEPENDENT-AS-GROWTH-HOSTILE-CHECK and report q_values=[1]
after 81 enumerated four-slot tuples at each of D=5 and D=6, together with
the distinct effective counts 9 and 81. Any assertion failure,
hash mismatch, rectangular support, or omitted scope marker fails closed.
