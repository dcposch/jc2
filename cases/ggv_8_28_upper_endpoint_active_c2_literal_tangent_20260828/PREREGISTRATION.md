# Preregistration: exact-Q endpoint tangent dual

Date: 2026-08-28  
Status: **FROZEN BEFORE AWS EXACT RUN**

## Question

At the frozen deep active-`c2` rational point with homogeneous
`D0=...=D22=0`, allow every legal first-order direction in

```text
S[0..3], Z[0..6], T[0..9], c2,
F4..F14 in their authoritative windows,
G4..G21 in their authoritative windows.
```

Does a tangent vector preserve `D0=...=D21=0` and change the endpoint to
the affine target `D22=1`?

The compiled matrix has 308 columns and 510 coefficient rows.  Three frozen
modular probes (`65521,65519,65497`) all give prefix rank 291 and reject the
target at row label `D22[X^0]`.  Modular agreement is navigation only.

## Acceptance

`TANGENT-OBSTRUCTED-AT-THIS-POINT` requires all of:

1. exact sparse elimination over `Q` returns inconsistent;
2. it emits a left-dual certificate `y` with exact replay
   `y*A=0`, `y*b=1` inside the producer;
3. the contradiction source label is `D22[X^0]`;
4. all source hashes, stdout/stderr, resource telemetry, and certificate
   hashes are preserved;
5. the three modular ranks remain 291.

If exact elimination is consistent, times out, exhausts memory, loses
custody, or fails internal replay, the result is respectively a tangent
survivor or `NO VERDICT`; modular output must not be promoted.

The zero-target mutation is the positive control: the homogeneous system is
consistent (the zero tangent vector) with the same coefficient matrix.

## Frozen source

```text
ddcd7b5d9cc5dd37e56412f606eb4b0fb37bc976280b224ac9dcf91a04be20a1  probe_tangent.py
f3371687df3584bd1dbeac9e9ad05aca8212a6dd35b63c17209916ab9d11fb45  ../ggv_8_28_upper_endpoint_active_c2_literal_d16_d22_probe_20260828/probe_literal_tail.py
112650dc27b0e13d76979d5adca9315919ee65cb8d9eaf717c1685f99d96de26  ../ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/verify_active_c2_extension.py
```

## Scope firewall

Even a certified obstruction proves only that this one homogeneous point
has no first-order deformation to the affine endpoint inside the complete
reduced-prefix/raw-window parameter space.  It does not prove the point is
scheme-isolated, exclude nonlinear arcs based elsewhere, exclude the deep
locus, establish the general-`V0` raw landing bridge, prove a Keller theorem,
or resolve JC2.

