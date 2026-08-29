# Lambda-zero exact origin endpoint plus q5..q15 preregistration

Date: 2026-08-28

This packet freezes a reduced discriminator for the proper branch

```text
A=X^4-1, lambda=0, c2!=0, exact D=0,
reviewed D11/D12 lifts, q3 plus A|U gives U=0.
```

It does not identify this proper branch with the full lambda-zero slice.

## Exact reduced F and q gates

The retained forms are

```text
F1=F3=0,
F2=-A^3 Q/8,
F4=A^2 Q^2/256,
F5=A^2 r/256,
F6=A e/2048,
F7=A f,
F8,...,F14 in their complete authoritative raw windows,
F15=0 (there is no raw weight-15 F slot).
```

Arbitrary `Q` is retained in the general system.  Exact de Rham gates are
compiled for every `q5,...,q15` from

```text
q_n = 2/(n+2) [t^n] F^((n+2)/8).
```

Both quadratic twists have the same coefficient ideal up to nonzero
character scalars.  The complete bounded rational primitive operator is used;
no primitive coefficient or even gate is silently dropped.

## Full characteristic and raw endpoint

All ten even characteristic modes are retained in

```text
G = F^(3/2)
    + sum_{birth=2,4,...,20} c_birth t^birth F^((6-birth)/4).
```

`G8,...,G15` are reconstructed from this expression, never introduced as
independent raw variables.  Exact divisibility of every Laurent numerator by
its power of `A` and every authoritative raw X-window is imposed.  These are
the complete remaining four-root/polynomiality constraints through G15:

```text
G8 [0,16], G9 [0,15], G10 [0,14], G11 [0,13],
G12 [0,12], G13 [1,11], G14 [1,10], G15 [1,9].
```

An independent census over all 442 frozen raw slots proves that the constant
coefficient of the endpoint has exactly two possible contributions:

```text
D22[X0] = F11[X1] G11[X0] - F7[X0] G15[X1].
```

The charged equation sets this value to one.  The same census verifies for
every raw F and G slot that weight parity is exactly raw total-degree parity:
if `w=8+3x-y` on F or `w=12+3x-y` on G, then
`w == x+y (mod 2)`.  Consequently the all-odd-weight-zero section makes
G11, G15, and the endpoint value zero and is immediately incompatible with
the target one.

## Controls and repaired firewall

The slice `Q=e=F8=r=0` is compiled separately as an exact control.  The
candidate checksum after q-parameterization is

```text
D22[X0] = -8*a1*(3*c6*b2+2*c8*a2),
G15 remainder X1 = 40*(3*c6*b2+2*c8*a2).
```

The AWS reduction must independently derive and map these parameters before
the checksum is accepted.  This identity is control-only.  It is explicitly
forbidden to infer that G15 polynomiality forces the origin value to vanish
for arbitrary Q: an exact Q=X mutation exists with legal G11/G15 and nonzero
origin pairing.  Therefore G15-only membership is recorded as diagnostic;
the general verdict uses arbitrary Q and the full q plus G8..G15 constraint
ideal.

## Frozen local desk audit

The standard-library desk check (1.6 seconds) independently matched the
ten-mode characteristic through weight 15 against the frozen literal-tail
implementation, replayed the 442-slot endpoint census and parity identity,
and checked that an even-F sample has zero odd G11/G15 and odd q5..q15.

```text
9c90e6d6cca8e99d08eba3c68c2ff948e93822062a40dde1af5448c2908d84bf  compile_origin_q15.py
01f57aa0026c02cb30fd6043a353029def77aaae4af9dc3dc5486101df270481  reduce_origin_q15.py
50afdaa0bdc1f18c3883f32c56b31b02800cce411d236808b9d633601248b873  DESK_CHECK.stdout
```

Pinned mathematical dependencies are listed in `SOURCE.sha256` and rechecked
inside the compiler.

## AWS execution and verdicts

Run the control and general systems in separate fresh namespaces on separately
audited idle Amazon EC2 r6i hosts.  Each job uses one core, exactly zero swap,
a 64-GiB address-space cap, an 8-GiB file cap, a two-hour master cap, explicit
inner caps, immutable source, PID/PGID/SID/starttime registration, continuous
group monitoring, and a final no-orphan census.  Abort on source/prereg drift,
host mismatch, an active-job conflict, nonzero swap, formula mismatch, exact
versus three-prime rank disagreement, or reducer failure.

For each system:

1. compile exact q gates, reconstructed G8..G15 constraints, and endpoint;
2. perform sequential constant-Q exact RREF, comparing ranks at
   `65521,65519,65497` at every gate;
3. test endpoint-value membership in the G15-only ideal as diagnostic;
4. test endpoint-value membership in the complete base ideal at three primes;
5. only after three-prime agreement, run tracked exact-Q membership and require
   basis and cofactor replay;
6. if membership does not decide, test the full endpoint ideal at all three
   primes and run tracked exact Q only after a modular unit signal.

An exact replayed membership certificate proves the endpoint value is zero on
the full recorded base ideal, hence contradicts `D22[X0]=1`.  A tracked exact
unit certificate also proves emptiness.  A modular result, factor, dimension,
or nonunit basis is navigation only.  An exact survivor must explicitly replay
every q gate, every G8..G15 polynomial/window equation, `c2!=0`, and the origin
target; otherwise the verdict is `NO-VERDICT`.

No conclusion about the full lambda-zero slice, unrestricted branch P,
primitive values, family landing, Keller theorem, JC2, HENS-CT, `jc2-lean`, or
any canonical file is in scope.
