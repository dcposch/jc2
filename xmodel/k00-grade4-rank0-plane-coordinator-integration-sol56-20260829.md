# Coordinator integration — K00 grade four over the rank-zero plane

Date: 2026-08-29 UTC  
Coordinator: Sol 5.6  
Frozen basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`  
Lifecycle: `PROMOTED_WITH_REPAIRS / NONREDUCED_SURVIVOR / NO_G4_KILL`

## 0. Evidence and disposition

Opus 5 primary:

```text
0d2a9861126c8857e04a9170c8586b6b4eabe67d2e65d3b4d3b7e991774b614f
  xmodel/k00-grade4-rank0-plane-primary-opus5-92e-20260829.md
  body 40012 / f6356d974f2f183d571297384d33f9161c2dd12d6a21c10a3fdc3200591cb6a2
```

Independent Grok 4.6 hostile review:

```text
1ec95a45d97658fbd3b2464831deb768ee19574feefc8bb9dcac656d5f79bb2e
  xmodel/k00-grade4-rank0-plane-opus5-hostile-review-grok46-40c-20260829.md
  body 25176 / 41da5999a230115a8a63bc0b7793534dd9ab39800aa5ed77ce493381cbb479c2
```

The review independently rebuilt all 49 atlas rows from `exact_terms`, used a
name-declared exact-Q ring map, reproduced all seven grade-four identities in
Python and Singular, and returned `PASS_WITH_REPAIR`. Its lane is `DONE`, exit
zero, with stable declared inputs and `charge_basis_status=ABSENT`. The review
did not use the producer scripts as mathematical evidence.

Binding disposition:

```text
PROMOTE THE GRADE-FOUR CLOSED FORM, REDUCED LOCUS, AND NONREDUCED STRUCTURE
NO GRADE-FOUR BRANCH KILL
RUN GRADE FIVE RADICAL-FIRST FOR GEOMETRIC SURVIVAL
USE THE SCHEME INPUT ONLY FOR INFINITESIMAL/NILPOTENT STRUCTURE
```

## 1. Promoted theorem

Work over an algebraic closure of `Q` and consume the reviewed complete
grade-three incidence. On its rank-zero plane

```text
(d0_1,...,d5_1)=(2s,t/8,s,t,s,2t),
u=(d0_2,...,d5_2),
mu=(s^2,st/8,16t^2,0,0,0),
w=u-mu,
```

the seven literal grade-four rows obey the generatorwise polynomial identity

```text
phi(Lambda_(4,r)) = Q_r(w),       r=1,...,7,
```

where `Q_r` is the literal grade-two row, including its zero sixth row. The
whole `d*_3` block and `k10_0` disappear identically at this grade. This is an
equality of the displayed generators, not merely of radicals.

In

```text
T=Q[s,t,u0..u5,v0..v5,k,z]
```

let `I4` be those seven rows together with `z*k-1`, and set

```text
RA=16*u1-4*u3+u5-2*s*t,
RB=u0-4*u2+2*u4-s^2+64*t^2.
```

Then

```text
I4 is proper,
dim(T/I4)=13,
mult(T/I4)=8,
sqrt(I4)=(RA,RB,z*k-1),
```

and the radical is prime. In the open-coordinate presentation the reduced
locus is

```text
{RA=RB=0} in A^14_(s,t,u,v) x G_m,k,
```

which is smooth, irreducible, rational, and isomorphic to
`A^12 x G_m`. The Rabinowitsch variable is merely the graph coordinate
`z=k^(-1)`.

The scheme is strictly nonreduced. Its nilradical has exact nilpotency index
three. Under the triangular shift `u -> u-mu`, its primary structure is
transported from the six-variable grade-two ideal: one reduced
top-dimensional minimal component and embedded components of dimensions
three and two, the latter with prime equal to the already reviewed plane
ideal `J0` in shifted coordinates. Recovering that embedded prime corroborates
the plane; it does not independently re-prove grade-three exhaustiveness.

Neither projection to `(s,t)` nor projection to `u` has a separate
constraint. The entire geometric content is the coupled pair `RA=RB=0`.
Explicit sections prove the claimed projections, rather than an elimination
closure alone. Thus grade four leaves a nonempty stratum and supplies no
conditional branch kill.

## 2. Radical-first scheduling theorem

The producer and reviewer both requested two independent grade-five
geometric verdicts, one from `I4` and one from `sqrt(I4)`. That scheduling
claim is repaired. For any later ideal `J` in the same ring,

```text
sqrt(I4+J) = sqrt(sqrt(I4)+J).
```

Indeed, `I4+J` is contained in `sqrt(I4)+J`, giving one radical inclusion;
conversely `sqrt(I4)` and `J` are both contained in `sqrt(I4+J)`, giving the
other after taking radicals.

Consequently the scheme-input and radical-input grade-five systems must have
the same geometric point set, unit/proper verdict, reduced minimal primes,
and Krull dimension. Any claimed binary divergence in those quantities is an
algebra error. The inputs can still differ in nilpotents, embedded primes,
multiplicity, tangent/cotangent modules, and infinitesimal lifting structure.

Therefore run grade five radical-first to decide geometric survival. A
scheme-input calculation is a secondary filtered/cotangent diagnostic, not a
second existence computation. This repair does not discard the proposed
Fitting-module analysis; it types its purpose correctly.

## 3. Binding repairs and frontier

- Every successor must declare the jet-major source ring and use a name-based
  map. The atlas component-major order is different and cannot be consumed
  positionally.
- Replace the producer's invariant-sounding mutation phrase “rows 2 and 4”
  by the named witness, or by the reviewed generic statement that six of
  seven rows fire.
- At grade five `d*_4` and `k10_1` disappear after the plane substitution and
  are dummy free coordinates. Retaining them is allowed only if dimension is
  interpreted accordingly. The returning blocks are `d*_3` and `k10_0`.
- Producer and reviewer scratch under `/tmp` is not archival custody. Future
  computational certificates must place a deterministic reconstruction or
  serialization in-tree.
- The producer seal's quoted marker is not unique; the verified body hash uses
  the first marker. Successors must use a genuinely unique marker.

No grade-five solution, normalized source point, finite jet, formal or
convergent arc, polynomial map, K00-closure point, counterexample, order-two
or maximum-twelve exclusion, exit price, or JC2 conclusion follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5663`.
- Body SHA-256:
  `917207a71e7aea537e0a079205dfa91fec853a4b00bff01ceaffe597701117c7`.
- Frozen basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`.
