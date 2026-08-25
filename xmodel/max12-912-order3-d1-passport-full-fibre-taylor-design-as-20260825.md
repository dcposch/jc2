# Live unbounded-total successor: cyclic-D1 passport versus the full `k != 0` lower fibre

Date: 2026-08-25  
Status: **EXACT DESIGN / PREREGISTRATION; NO COMPUTATIONAL VERDICT**

## Disposition

The smallest genuinely new `(9,12)` order-three computation is not another
high Laurent row and not another selected-Q8 jet.  It is the cyclic `D=1`
terminal passport tested against the complete previously unhandled `k != 0`
lower Faber fibre, retaining every constant load `(mu,nu)`, followed by both
global Taylor polynomiality families on every geometric degree-one section.

The exact executable contract is frozen at

```text
cases/max12_912_order3_d1_passport_full_fibre_taylor_20260825/
```

Its AWS-only adapter is `compile_gate.py`; its theorem semantics, boundaries,
controls, and stop rules are in `PREREGISTRATION.md`.

## Why this is the first nonduplicate gate

The universal Faber theorem and its different-model review

```text
d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036
e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c
```

already integrate all eleven high rows and leave exactly

```text
r1=r2=r4=r5=r7=0, r3=mu, r6=nu, 9*r8'=j/u.
```

The branch-wide terminal Belyi classification and its hostile review

```text
28f33b993726b4bd7441a79a8f4208983dbbd0c5e4113d839a78af1b8cc7b6c6
5da99825e099232832b0cf91fc02b29cb9460a2f675e2a69ab1769f204cf9fc9
```

already prove that every actual nontrivial order-three trajectory has a
balanced three-value passport.  The cyclic rows `D=1,2` remain terminal
positive controls, so the passport theorem alone excludes nothing.

The selected-Q8 work is not reopened.  In particular:

- formal/local Taylor families are an invertible coefficient change; only
  global pole conditions can cut a trajectory (`ac8d8d4a...`);
- the strict selected `k=mu=0,nu!=0` components meeting corrected-Q8
  contacts are already excluded by the reviewed positive-genus theorem
  (`d7e73783...`, review `f8d5208d...`);
- Q8 contact parity, eight-contact partitions, local jets, and bounded plane
  support do not globalize to the full lower fibre.

The exact hashes abbreviated above are

```text
Taylor-freeness report:
ac8d8d4a53423255d564c6fdbecaf14b0dac3c23025a5156f4f6863a77bd4978
selected-Q8 exclusion V2:
d7e73783191d70a86e5c8786b735d0a596034c1d492559049d13433b8e889209
selected-Q8 exclusion V2 review:
f8d5208d9e915f694a9df1c9ae9014612e87c172b794c94bbfcf30f98bdb7996
```

The exact lower-tail source

```text
cases/max12_912_order3_fibre_20260824/order3_fibre.py
SHA-256 a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf
```

is reusable code but is not itself a reviewed theorem.  The new gate pins it,
calls its transitive pin checker explicitly, and requires a second source
construction of all eight tails before consuming any CAS result.

## Exact D1 incidence

After affine normalization of the two finite cyclic branch points, set

```text
s=t^3=x/(x-1),      r8=t,
u=t^2/(t^3-1)^2,    h=x^2*(x-1)^4,    j=-3.
```

Then `9*t'=-3/u` exactly.  With the frozen generator
`sigma(u)=zeta*u`, one has `sigma(t)=zeta^2*t`.  Therefore

```text
a_i=t^(i mod 3)*A_i(s),
r_l/t^(2*l mod 3) in C(s).
```

This distinction is load-bearing: the tail quotient exponents are
`(0,2,1)`, not `(0,1,2)`.  Equivalently, for `tau=sigma^2` one has
`tau(t)=zeta*t`, `tau(a_i)=zeta^i*a_i`, and
`tau(r_l)=zeta^(2l)*r_l`.

The adapter emits all eight exact rows over
`Q[s,k,mu,nu,A0,...,A7]` with targets

```text
(0,0,mu,0,0,nu,0,1).
```

The primary algebraic endpoint is the absolute/geometric decomposition of
this incidence over the full `k != 0` load space.  Only components of
geometric degree one over `P1_s` are eligible: a higher-degree algebraic
cover enlarges the prescribed Kummer field and is not a trajectory.

## Exact global Taylor endpoint

For a degree-one section, write the true center `r=u*R0`.  The `y^8`
coefficient `9*h^3*R0` bounds finite poles of `R0` by six at `x=0` and
twelve at `x=1`.  Quotienting the polynomial source shear
`y -> y+q(x)` gives the finite, exhaustive center ansatz

```text
R0(s)=sum_{d=-6}^{-1} c_d s^d + sum_{d=1}^{12} c_d s^d.
```

The gate then imposes all `10+13=23` Taylor coefficients exactly.  Since
`x=s/(s-1)`, membership in `C[x]` is encoded by an exact finite expansion in
powers of `s/(s-1)`, not by a local jet or value sampling.  A SAT section is
accepted only after literal reconstruction of `P,Q`, the eight tails, the
original terminal row, generic coprimality, and the constant Jacobian.

## Boundaries and controls

The preregistration retains `s=0,1,infinity`, coefficient infinity, all
`mu/nu` rank strata, every discovered Fitting stratum, resultants, and the
entire `k=0` divisor as an uncovered successor.  It includes independent
D1/D2 terminal controls, the common-cubic zero-tail source control, a Taylor
round trip, a swapped-character negative control, and a wrong-center
negative control.

The first run is bounded at two hours and 128 GiB.  Missing absolute
factorization, an unprocessed exceptional load stratum, or any source/hash/
containment disagreement terminates without inference.

## Exact scope

A complete negative result would exclude only the cyclic `D=1` passport on
the fully processed `k != 0` order-three lower-fibre chart.  A positive result
would be an explicit rational coefficient/Taylor realization candidate, not
yet a counterexample.  `k=0`, higher passports, the order-one Kummer branch,
`(8,12)`, maximum twelve, and JC2 remain open.
