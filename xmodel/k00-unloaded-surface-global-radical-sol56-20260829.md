# Exact global radical of the normalized unloaded K00 rows

Author: Sol 5.6 Ultra (coordinator exact lane)
Date: 2026-08-29 UTC
Lifecycle: `PRODUCER_EXACT / DIFFERENT-MODEL HOSTILE REVIEW REQUIRED`

## 0. The result

Let `I=(r1,...,r7)` be the seven frozen unloaded normalized K00 rows in
`Q[d0,...,d5]`, taken byte-for-byte from the V14R1 serialized replay prelude,
and set

```text
f0 = d0-2*d4-d4^2,
f1 = 8*d1-(1+d4)*d3,
f2 = d2-d4-16*d3^2,
f5 = d5-2*d3,
J  = (f0,f1,f2,f5).
```

Then, exactly over `Q`,

```text
sqrt(I) = J.
```

Equivalently, the global reduced zero set of all seven unloaded rows is the
two-parameter graph

```text
D(S,T)=(2S+S^2,(1+S)T/8,S+16T^2,T,S,2T).
```

This is global, not merely local at the origin. It is an unloaded source
theorem. It is not a theorem that a mixed loaded arc lies on this graph.

## 1. Two-containment proof

The first containment is direct exact reduction:

```text
r_i mod J = 0,  i=1,...,7.
```

Thus `I subset J`, hence `sqrt(I) subset J` because `J` is prime. Primality
does not rely on a decomposition routine: the four triangular equations give

```text
Q[d0,...,d5]/J  ~=  Q[d3,d4],
```

by eliminating `d5,d2,d1,d0` in that order. In particular `J` is prime and
has dimension two.

For the reverse containment, the AWS producer constructed 28 explicit
polynomial multipliers `c_(a,j)` and the independent replay expanded the four
identities

```text
f_a^5 = sum_(j=1)^7 c_(a,j)*r_j,    a in {0,1,2,5}.
```

Therefore every generator of `J` lies in `sqrt(I)`, so
`J subset sqrt(I)`. Combining the two containments proves the displayed
equality. The producer's exact standard basis also found that powers one
through four have nonzero normal form for each of the four displayed
generators; this sharp individual-power observation is not needed for the
radical theorem.

## 2. Portable replay and custody

The evidence packet is

```text
cases/max12_812_order2_u2_62_k00_unloaded_surface_local_v1_20260829/
```

with frozen source prelude SHA-256
`5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a`.
The portable producer is `global_power.sing`, SHA-256
`bb95d104e6d5ddfb31a59c88a782a584c3a836134b041ad0d4a5ea6caede53ef`.
Its V4 stdout SHA-256 is
`e7b23ec573d9a72112977e69ec533f5585f575b3931c2ee8e214f2b901ffd87c`.
The complete 36-file custody manifest, including all 28 multiplier
polynomials, has SHA-256
`8f307a03fadc8d610fda151f671d815ae8bc3dd7ceee233593743018e65b81f4`.

The fresh replay uses no standard-basis or lifting computation. It checks all
custody hashes, parses the 28 polynomials, expands the four identities in the
original seven-row presentation, checks `I subset J` and `dim(J)=2`, and
requires both an input mutation and a multiplier mutation to be detected.
Its script SHA-256 is
`a14e3f84ff95adbb6e799aaa663fd16f2152fbcac0e439547c6aba4ef8354f4e`;
its AWS stdout SHA-256 is
`d8c59b0e86d88557b30511648dff1279fc5b5535779f6028a6165d74fe2a9614`.
It ends with

```text
K00_SURFACE_POWER_REPLAY_I_IN_J=1
K00_SURFACE_POWER_REPLAY_J_DIM=2
K00_SURFACE_POWER_REPLAY_IDENTITIES=4
K00_SURFACE_POWER_REPLAY_EXPONENT=5
K00_SURFACE_POWER_REPLAY_MUTATION=1
PASS_K00_SURFACE_EXACT_GLOBAL_RADICAL_J
```

Both producer and replay ran under the fail-closed EC2 wrapper on r6b with
Singular 4.3.2, zero swap, maximum reported replay RSS 15,752 KiB, and exact
characteristic-zero arithmetic.

An independent `minAssGTZ(I)` route on a separate preregistered run found one
minimal prime. Its serialized generators were

```text
2*d3-d5,
-4*d5^2+d2-d4,
-d4*d5+16*d1-d5,
-d2*d4+64*d1*d5+d0-d2-d4,
```

and exact two-way reduction identifies this prime with `J`. This corroborates
the direct-power proof but is not needed by it.

## 3. Harness repair ledger

V1 stopped before any power conclusion because its harness compared a
Singular matrix object directly with scalar zero. Entrywise comparison fixed
that false failure; no mathematical formula changed.

V2 retained an unconditional multiplication through power 64 after a first
hit and was resource-cancelled without a verdict after V4 superseded it.

V3 found the correct exponent-five identities in memory, but Singular's
`write(matrix)` coercion emitted only the first entry of each seven-row
vector. V4 writes and hashes all 28 entries separately. The fresh replay is
the promotion-bearing artifact. These failures are preserved in `LAUNCH.md`;
none is silently reinterpreted as evidence.

## 4. Exact consequence and firewall

For every field extension `K/Q`, a point `d in K^6` satisfying all seven
unloaded rows lies uniquely on `D(S,T)`, with `S=d4` and `T=d3`. More
generally, the same conclusion holds for points over any reduced
`Q`-algebra: each identity gives `f_a(d)^5=0`, and reducedness kills the
nilpotent.

In particular, if a six-tuple of formal series over a characteristic-zero
field satisfies `r_i(d(t))=0` identically for every `i`, then it lies on the
graph identically. This uses that the formal-series ring is a domain. It does
not require extracting fifth roots or extending the coefficient field.

The mixed normalized source equations are instead

```text
R(d) + Lambda^2*k10*M(d) + Lambda^6*k6*N(d)
     + Lambda^10*k2*P(d) - targets = 0.
```

They do not set the unloaded ideal `I` to zero. Hence `sqrt(I)=J` cannot be
applied wholesale to a loaded trajectory. It may be used on a prefix or an
associated-graded step only after that step independently proves that the
unloaded rows vanish there. No formal recentering induction, ramification
reduction, resonance exclusion, load-face coverage, jet lifting, attainment,
polynomial map, counterexample, or JC2 conclusion is asserted here.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5661`.
- Body SHA-256:
  `41d6460a0f1228f192f67c98c75accdfa3d7ccb29d6dda080015ea8393f50959`.
- Frozen basis: `9b64db896b65e100839f6d75fbeea661cd818b9c`.
