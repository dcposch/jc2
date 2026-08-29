# Preregistration: V20 common mixed `Lambda<=19` Kuranishi map

Date: 2026-08-27

Status: **DESIGN FROZEN BEFORE COMPILER OR ALGEBRA.  V17-Q IS A MANDATORY
INPUT GATE.  ALL MATHEMATICAL OUTCOMES ARE OPEN.**

## 1. Charged question

V19 proved only that the three separate V18 covectors are not composable
with any serialized honest-source map.  V20 supplies that missing common
domain.  It must compile, in one calculation, the normalized K00 coefficient
jets, all three simultaneous loads with their honest Rees weights, all four
targets, and the representation freedom of the six unloaded rows through
`Lambda^19`.

The exact one-parameter rows are

```text
Phi_l = r_l(C,Lambda^2*k10,Lambda^6*k6,Lambda^10*k2)
        - Lambda^(12+l)*delta_l,

delta=(0,mu2,0,mu4,0,mu6,Jdet/4).
```

The source is the reviewed seven-row one-parameter client.  `Jdet` is its
Jacobian parameter; it is not either collision ideal `J1` or `J2`.

V20 asks whether the coefficient equations through grade 19 have a common
K00 jet with `k10(0)*Jdet(0) != 0`.  It does not ask three independent
one-load questions and must never add or identify their quotient spaces.

## 2. Normalized K00 chart and honest jet domain

Work after the already licensed finite-flat/Kummer normalization `C6=1` in

```text
R = Q[d0,d1,d2,d3,d4,d5],       m=(d0,...,d5),
```

with the exact inverse coordinate map

```text
C5=d5,          C4=(d4+3)/8,     C3=d3,
C2=(d2+1)/16,   C1=d1,           C0=(d0+1)/256,
C6=1.
```

For a field `F`, put `T19=F[Lambda]/(Lambda^20)`.  The common source object
is the following single typed jet domain:

```text
d_j       = sum_(n=1)^19 d[j,n] Lambda^n,
k10       = sum_(n=0)^17 k10[n] Lambda^n,       k10[0] != 0,
k6        = sum_(n=0)^13 k6[n] Lambda^n,        k6[0] = 0,
k2        = sum_(n=0)^9  k2[n] Lambda^n,        k2[0] = 0,
mu2       = sum_(n=0)^5  mu2[n] Lambda^n,       mu2[0] = 0,
mu4       = sum_(n=0)^3  mu4[n] Lambda^n,       mu4[0] = 0,
mu6       = sum_(n=0)^1  mu6[n] Lambda^n,       mu6[0] = 0,
Jdet      = Jdet[0],                             Jdet[0] != 0.
```

Coefficients that cannot occur through grade 19 are omitted, not projected
from an algebraic closure.  The five displayed zero constants are the K00
boundary equations.  `k10[0]` and `Jdet[0]` are retained as named unit
parameters; setting either to one requires a separately replayed group
action and is not licensed by this specification.

There are 169 labelled jet columns before the five boundary-zero columns are
removed, hence 164 free source columns.  A compiler must emit the complete
column table `(kind,name,series_index,first_Lambda_grade,boundary_status)` and
derive this census rather than hard-code it as a verdict.

The ground-truth finite functor is

```text
Z19(F) = {source jets above : [Lambda^0,...,Lambda^19] Phi_l = 0
                            for l=1,...,7}.
```

Every optimized/Kuranishi presentation must be replayed bidirectionally
against these literal 140 coefficient equations.  No syzygy quotient may
replace the first six equations.

## 3. Exact local relation and common residual

Consume the reviewed V14R1 witness

```text
h = 63*d4+20,                  h(0)=20,
h*r7 = sum_(i=1)^6 u_i*r_i.
```

Let `a_i^X` be the exact affine coefficient of load
`X in {k10,k6,k2}` in row `i`, and define

```text
D_X = h*a_7^X - sum_(i=1)^6 u_i*a_i^X.
```

Affine load linearity gives the exact denominator-free identity

```text
Rmix = h*Phi7-sum_(i=1)^6 u_i*Phi_i

     = Lambda^2  * k10  * D_k10
       + Lambda^6  * k6   * D_k6
       + Lambda^10 * k2   * D_k2
       + Lambda^14 * u2   * mu2
       + Lambda^16 * u4   * mu4
       + Lambda^18 * u6   * mu6
       - Lambda^19 * h    * Jdet/4.                 (3.1)
```

The compiler must derive and replay (3.1) from all seven frozen rows over
both `Q` and the control prime before it emits a Kuranishi block.  Since `h`
is a unit at K00, the systems

```text
(Phi1,...,Phi7)=0
```

and

```text
(Phi1,...,Phi6,Rmix)=0
```

are equivalent in the normalized K00 local ring.  This equivalence is the
ground truth for every later optimization.

## 4. Representation-invariant universal first-order object

Fix the sign convention

```text
w=(-u1,-u2,-u3,-u4,-u5,-u6,h) in Syz(r1,...,r7).
```

For a seven-row unloaded syzygy `v=(v1,...,v7)`, define its universal mixed
deformation vector in `R^7`, with coordinate order

```text
(k10,k6,k2,mu2,mu4,mu6,Jdet),
```

by

```text
K(v) = (
  sum_(i=1)^7 v_i*a_i^k10,
  sum_(i=1)^7 v_i*a_i^k6,
  sum_(i=1)^7 v_i*a_i^k2,
  -v2, -v4, -v6, -v7/4
).
```

Thus

```text
K(w)=(D_k10,D_k6,D_k2,u2,u4,u6,-h/4),
```

and (3.1) is the weighted contraction of `K(w)` with

```text
P(Lambda)=(Lambda^2*k10,Lambda^6*k6,Lambda^10*k2,
           Lambda^14*mu2,Lambda^16*mu4,Lambda^18*mu6,
           Lambda^19*Jdet).
```

Let `S6=Syz_R(r1,...,r6)`.  Its common deformation-action map is

```text
Gamma:S6 -> R^7,
Gamma(s)=(
  sum_i s_i*a_i^k10,
  sum_i s_i*a_i^k6,
  sum_i s_i*a_i^k2,
  -s2,-s4,-s6,0
).
```

The common first-order Kuranishi target is

```text
Qcommon = (R_h)^7 / ( I*(R_h)^7 + image(Gamma)_h ),
I=(r1,...,r6).                                      (4.1)
```

It uses the complete six-row module, expected to have 66 frozen polynomial
generators.  The seven-row module, expected to have 87 generators, is only a
representation-invariance control.  For every seven-row generator `v`, the
compiler must construct

```text
s(v)=(h*v1+v7*u1,...,h*v6+v7*u6) in S6
```

and replay the exact cross relation

```text
h*K(v)-v7*K(w)=Gamma(s(v)).                          (4.2)
```

Local completeness is mandatory: any local syzygy clears by a denominator
which is a unit at `m`, and its inverse has a finite Taylor expansion to the
charged cutoff.  The Macaulay blocks must therefore include every required
monomial multiple of all 66 polynomial generators, not only generator
constants or one RREF representative.

Restricting (4.1) to a single load axis recovers the V17 quotient
`R/(I+E_X)`.  The converse is false: three axis covectors need not extend to
a covector on `Qcommon`.  V18 duals are extension controls, never columns or
summands inserted by hand.

## 5. Bifiltered finite compiler

The compiler has two mutually checking presentations.

### 5.1 Literal source-jet presentation

Substitute the 164 free source series into all seven `Phi_l`, expand modulo
`Lambda^20`, and serialize every coefficient polynomial with a row label
`(Phi_l,Lambda_grade)`.  Boundary equations and the two unit opens are
serialized separately.  No load or target is solved away.

### 5.2 Kuranishi/adjoint presentation

Use the first six literal rows and the exact residual (3.1).  Proceed by
increasing Lambda grade.  On each constructible compatible prefix stratum,
write the next coefficient equations as

```text
L_n(prefix) * z_n = b_n(prefix),                    (5.1)
```

where `z_n` contains every newly active coefficient, simultaneous-load,
target, `Jdet`, and allowed local-multiplier jet.  Columns are labelled by
source and grade.  The allowed multiplier columns are the complete bounded
Macaulay image of `I*(R^7)+image(Gamma)` in the relevant
`(Lambda-grade,normal-degree)` window.

Equation (5.1) is affine-linear only after the lower jet is fixed.  V20 must
not flatten the full nonlinear problem into one constant matrix.  Rank
changes over a prefix family require a Fitting/minor split into constructible
strata.  A random point may choose work order but cannot close a stratum.

At every grade, serialize:

- the complete row and column maps;
- the sparse matrix and affine target;
- equations and inequations defining the prefix stratum;
- a compatible lift, or a left functional with nonzero target pairing;
- the replay of that lift or dual; and
- a hash link to its parent prefix.

The modular lane may use the V18 first filtered breaks as navigation:

```text
k10: normal degree 4,
k6:  normal degree 3,
k2:  normal degree 2.
```

They are not common-source obstructions.  A V18 covector may be reported as
`EXTENDS`, `DOES_NOT_EXTEND`, or `NOT_TYPED` only after solving the common
adjoint extension equations against every cross-direction and target
column.

## 6. Valuation prefilter, not a verdict

Let `m0=min_j v_Lambda(d_j)>=1`.  V16R1 implies, for every local unloaded
representation, that the even multipliers have zero constant term.  Put
`e_i=v_Lambda(q_i(d(Lambda)))`; then `e_2,e_4,e_6>=m0`.  Hence the
target-only ways to meet the unit `Lambda^19*Jdet` term obey

```text
e_2+v(mu2)=5,       or       e_4+v(mu4)=3;
```

the `mu6` option would require `e_6+v(mu6)=1` and is impossible under the
K00 boundary conditions.  The shorter splits `m0+v(mu2)=5` and
`m0+v(mu4)=3` are licensed only on a stratum where the relevant multiplier
has a replayed nonzero first-normal term.  The compiler must compute the
affine space of relation jets, not inherit the order of one chosen lift.
These statements may order the branch search, but they do not discard
branches receiving order-19 contributions from the three load terms.

The V18 leading normal degrees similarly suggest the provisional load
orders

```text
2  + 4*m0,
6  + v(k6) + 3*m0,
10 + v(k2) + 2*m0.
```

They are lower-bound/branch heuristics only.  Cancellations can raise order,
and the common quotient can differ from every axis quotient.  Every branch
discard must have a replayed ideal, rank, or valuation certificate in the
literal seven-row jet presentation.

## 7. Dependency gates and execution order

Before any algebraic conclusion, V20 must:

1. hash and independently re-emit the reviewed 569-tail one-parameter
   source and distinguish `Jdet` from `J1/J2`;
2. replay the exact V14R1 `h,u_i` identity and `h(0)=20`;
3. replay all 66 six-row and 87 seven-row syzygies;
4. replay (3.1), every instance of (4.2), and a sign-mutation control;
5. consume a completed V17-Q endpoint with all three branches
   `LOCAL_NONZERO` and require its exact `IMAGE_X` and `TARGET_X` bytes to
   match the provisional V18R2 extraction; and
6. treat V18R2 exact ranks/duals as provisional until gate 5 passes.

The compiler may be written and syntax-tested before gate 5.  A modular
preflight may run under an explicit provisional dependency, but no exact or
geometric theorem may be emitted until gate 5 passes.

All nontrivial algebra runs on registered AWS hosts.  Each launch freezes
the full source tree, host/tag, field, wall and memory caps, row/column maps,
and expected fail-closed sentinels.  Timeout, OOM, engine diagnostic,
incomplete stratum cover, missing dual/lift, hash mismatch, or failed replay
is `NO_VERDICT`.

## 8. Allowed endpoints and firewall

The only producer endpoints are:

```text
EXACT_OBSTRUCTION_ON_COMPLETE_STRATUM_COVER_THROUGH_LAMBDA19
EXACT_COMPATIBLE_JET_THROUGH_LAMBDA19
MODULAR_NAVIGATION_ONLY
INCOMPLETE_STRATUM_COVER
NOT_TYPED_OR_SOURCE_DRIFT
RESOURCE_CAP_NO_VERDICT
```

An exact obstruction must cover every constructible prefix stratum and
replay a rational dual in the literal source-jet presentation.  It proves
only absence of a normalized `Lambda<=19` K00 jet for this frozen source
client.  Any upgrade to closure-first incidence requires a separately
audited normalization/valuative comparison and the prescribed
`Lambda,Jdet` saturation order.

A compatible exact jet is finite compatibility only.  It is not a formal
arc, algebraic arc, Taylor realization, Keller pair, or counterexample.
Formal lifting and finite-support realization are separate successors.

Neither a modular dual, an individual V18 class, a raw nonzero residual, nor
a single compatible prefix decides K00 closure incidence, order two,
maximum twelve, or JC2.
