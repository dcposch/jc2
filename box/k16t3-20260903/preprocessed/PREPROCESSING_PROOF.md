# Constant-pivot preprocessing audit

## Scope and current status

This directory contains a proof-preserving preprocessing of the gauged
Theorem-1.2 necessary order-chart superset for the K=16 ray at t=2,3,4.
It does not impose the omitted tuple-level Laurent bridge.  Thus a nonunit
residual basis is only a counting-bound result, and finitely many fixed-t
computations are not a uniform theorem.

The deterministic Sympy driver "triangular_preprocess.py" prepares Singular
inputs and never launches Singular.  Every prepared program retains:

- the three safe target gauges already applied by the source builder;
- the independent convention control F=pi, G=pi-gamma^2/2, J(F,G)=gamma,
  explicitly not a K=16 four-tuple witness;
- empty and nonempty Rabinowitsch wrapper controls in the declared main ring;
- the main equation T*c-1, which presents the c != 0 component.

The emitted residual generators are primitive integer polynomials.  The file
"tN_emission_scalars.tsv" records and verifies the nonzero rational multiplier
relating every emitted row to its rational substituted row.

## Exact quotient-ring argument

At one step let

    R_i = k[V_i]
    I_i = (a_i*x_i + b_i, E_i)

with a_i in k nonzero and x_i absent from b_i.  Let
S_i = k[V_i minus {x_i}] and define theta_i by

    theta_i(x_i) = -b_i/a_i
    theta_i(y) = y for y != x_i.

Inclusion of S_i in R_i and theta_i induce inverse maps

    R_i / I_i  isomorphic to  S_i / theta_i(E_i).

Indeed theta_i kills a_i*x_i+b_i, while
x_i-(-b_i/a_i) = (a_i*x_i+b_i)/a_i vanishes in the other quotient.
Each step is therefore an isomorphism, not merely a projection or a
necessary-condition replacement.

Composing the steps gives the ring map in each "tN_ring_map.tsv".  The driver
checks by exact expansion that the fully composed map sends every original
generator to its recorded residual or to zero.  It also checks each emitted
primitive integer row g against an identity g = lambda*f with lambda in Q
nonzero.

No chart-dependent expression is inverted: every pivot is a nonzero rational
field constant.  The map fixes c, so it extends after inverting c, or
equivalently after adjoining T and T*c-1.  Hence the original and reduced
c != 0 coordinate rings are isomorphic.  The original extended ideal is the
unit ideal if and only if the reduced extended ideal is.

For a modular run, pivot coefficients, substitution denominators, and every
emission multiplier must remain units.  The driver computes and rejects all
bad characteristics.  The present finite lists, including the denominator 2
from the actual-pair control, are:

| t | excluded characteristics | prepared primes |
|---:|---|---|
| 2 | 2,3,5,7 | none |
| 3 | 2,3,5,7 | 32003,32009,32027 |
| 4 | 2,3,13 | 32003,65521,1000003 |

## Mechanical source comparisons

For t=2, the generic builder was compared with the frozen charged
"t2_order_system.py".  Parameter order, h,A,B,z,P,Q, all tags, row order, and
all 37 equations agree exactly.  The frozen certificate SHA-256 is

    8543fd41c391c10d5d5cbc9f3d36aac794a9a294bcb88aff993230f600fa1b2b

It records the exact-Q reduced basis [1] for the original 37-generator
Rabinowitsch system.  The quotient isomorphism transfers this unit-ideal
result to the reduced t=2 input.  A fresh reduced run independently passed
all controls and returned the reduced basis [1] in 0.48 seconds wall time,
with maximum RSS 13,916 KB.

For t=4, the generic builder was compared with the dedicated
"t4_order_system.py".  Parameter order, h,A,B,z,P,Q, all tags, row order, and
all 65 equations agree exactly.

Full input hashes, vector hashes, and comparison flags are in
"reduction_audit.json".

## Finite reduction counts and pivots

| t | input eqs | residual eqs | input vars incl. c | residual vars incl. c | pivots | pivot bands |
|---:|---:|---:|---:|---:|---:|---|
| 2 | 37 | 26 | 27 | 17 | 10 | 9,8,7x2,6x2,5x2,4x2 |
| 3 | 51 | 37 | 36 | 23 | 13 | 13,12,11,10x2,9x2,8x2,7x2,6x2 |
| 4 | 65 | 48 | 45 | 29 | 16 | 17,16,15,14,13x2,12x2,11x2,10x2,9x2,8x2 |

Ordered pivot variables and coefficients:

- t=2:
  a3_1:5, a4_1:5, a5_2:10, a5_1:5, a6_2:10, a6_1:5,
  a7_2:10, a7_1:5, a7_0:-20, a7_3:-15/4.
- t=3:
  a4_1:7, a5_1:7, a6_1:7, a7_2:14, a7_1:7, a8_2:14,
  a8_1:7, a9_2:14, a9_1:7, a10_2:14, a10_1:7, a10_0:-28,
  a10_3:-21/4.
- t=4:
  a5_1:9, a6_1:9, a7_1:9, a8_1:9, a9_2:18, a9_1:9,
  a10_2:18, a10_1:9, a11_2:18, a11_1:9, a12_2:18, a12_1:9,
  a13_2:18, a13_1:9, a13_0:-36, a13_3:-27/4.

Each TSV records the step identity a*x+b=0 iff x=-b/a, both as the
right-hand side at that step and after composition into the final ring.
Source row indices are zero-based indices in the builder's ordered "tagged"
array.

## Generic pivot spine, but not a generic unit certificate

The existence and location of these constant pivots can be proved for every
positive integer t, rather than inferred from the three tables.  Put

    q = 2*t+1
    e = 3*t+1.

From

    B = pi*(pi-gamma) + b1*pi + b2
    A = pi*B + b3
    h = pi*A + b4

one computes exactly

    J(h,A) = pi*h - b4*pi
    J(h,B) = 2*h - b3*pi - 2*b4.

The pair of h^q, the leading term of Q, with alpha_i*h^(e-i) in P
contributes

    q*J(h,alpha_i)*h^(e+q-i-1).

After monic h-division, its quotient contributes in band h^(e+q-i):
coefficient q on the pi row for the A-coordinate of alpha_i, and coefficient
2*q on the constant row for its B-coordinate.  Pairing that alpha_i with a
nonleading Q coefficient lowers the band.  Every other term at this band
uses a strictly smaller coefficient index.  Descending-band elimination
therefore gives:

- pivot q on the A-coordinate for i=t+1 through e;
- pivot 2*q on the B-coordinate for i=2*t+1 through e.

After its constant gauge, alpha_e has coordinates along gamma,A,B,z, with
z=pi-gamma.  Its A,B coordinates are already in the preceding list.  For the
remaining two coordinates, direct calculation gives

    J(h,gamma) =
      -3*b1*pi^2 - 2*b2*pi - b3 + 3*gamma*pi^2 - 4*pi^3

    J(h,z) =
       3*b1*pi^2 + 2*b2*pi + b3 - 3*gamma*pi^2 + 3*pi^3.

In band h^(q-1), the pi^3 row has coefficients (-4*q,3*q) on the
(gamma,z) coordinates.  Solving first for gamma leaves coefficient -3*q/4
on z in the gamma*pi^2 row.  These are constant pivots whenever the
characteristic does not divide 6*q.

Thus the generic count is

    (e-t) + (e-2*t) + 2 = (2*t+1) + (t+1) + 2 = 3*t+4

in bands 4*t+1 down through 2*t.  This proves a uniform triangular
preprocessing recurrence.  It does not show that the residual ideal is the
unit ideal uniformly in t.

The three finite maps also have the same simple final images.  If u is the
A-coordinate of beta_(t+1) and v is the B-coordinate of beta_q, then

    alpha_(e,gamma) maps to 0

    alpha_(e,z) maps to
      -t*(t+1)*e*u^3/(6*q^3) + t*e*u*v/q^2.

The coefficients match binom(e/q,3) and 2*binom(e/q,2), using A^3=h^2*z and
A*B=h*z after specializing lower chart parameters to zero.  Full
cancellation of all other parameters has only been checked exactly for
t=2,3,4 in this lane.  This closed final-image formula is therefore typed
MEASURED-PATTERN/CANDIDATE, not a generic theorem here.

## Reproduction and interpretation

Run

    python3 box/k16t3-20260903/preprocessed/triangular_preprocess.py

to rebuild and revalidate the maps and prepared standard-basis inputs.
Verify "SHA256SUMS.prepared" from within this directory.  The separate
"SHA256SUMS.slimgb" covers the mechanically generated method variants.
"RUN_COMMANDS.txt" lists basis commands; resource coordination is external,
and the driver runs none of them.

An exact-Q unit basis [1] is a proof-producing outcome.  A modular [1] is
typed MEASURED-MODULAR unless a separate characteristic-transfer argument is
supplied.  A nonunit basis is typed NONTRIVIAL_SUPERSET_ONLY because the
tuple-level bridge is absent.
