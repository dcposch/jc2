# Registration: affine-Faber `A` graph-relative multigraded support

Date: 2026-08-26

Status: preregistered navigation client; no theorem or fan-coverage claim.

## Purpose

Reconstruct all seven frozen ordinary-Faber rows directly after the exact
two-sided load-coordinate change

```text
d6 = K6-(15*E^2/32)*K10,
d2 = K2-(15*E^4/256)*K10,
dm = mu2+(5*E^6/4096)*K10,
d4 = mu4.
```

Emit the complete exact support of `K=E*H3+H5` in these graph-relative
coordinates.  This is the required input for a relative Newton analysis of
the routed `0<v(a)<5` cells; it is not itself a predecessor reduction or a
source-cover theorem.

## Preregistered controls

- reconstruct from the pinned literal tails, not by rewriting the old 371
  output;
- retain all seven rows and the targets `dm,d4,mu6,J/4`;
- verify the exact transverse identities

  ```text
  [lambda]K = M*E*(-3*E^2*d6/64+d2/8),
  [a]K      = -9*E^5*d6/128+E^3*d2/8-E*dm+4*d4;
  ```

- verify the central intrinsic cubic `-E*lambda^3*M^3/16`;
- require that the one-coefficient mutation
  `d6 -> d6+E^2*K10` destroys the lambda cancellation;
- reject any surviving raw `q,n,k` coordinate after source substitution;
- emit every nonzero term with its full exponent vector.

The first downstream weight test is the fixed delayed timing with normal
order 15 and `v(a)=3`, where the raw central load wall at weight 45 cancels
on the affine graph.  Arbitrary kernel/complement coordinates and all four
transverse deviations must remain live.

## AWS lanes

```text
Box03: exact Q
r6d:   F65521 software/support control
```

No heavy local computation is permitted.  Stop on a frozen-input mismatch,
failed positive or negative control, engine diagnostic, timeout, memory cap,
or support-custody disagreement.
