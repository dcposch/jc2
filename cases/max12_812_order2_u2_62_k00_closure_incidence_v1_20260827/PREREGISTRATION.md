# Preregistration: K00 closure-first incidence V1

Date: 2026-08-27

Status: **SOURCE FROZEN BEFORE AWS LAUNCH.  NO ENDPOINT AT REGISTRATION.**

## Exact charge

In the reviewed one-parameter ring

```text
A=Q[Lambda,C0,...,C6,k10,k6,k2,mu2,mu4,mu6,Jdet],
```

compile the seven frozen ordinary-tail generators with targets
`(0,mu2,0,mu4,0,mu6,Jdet/4)` and compute, in this exact order,

```text
KL = (Phi1,...,Phi7):Lambda^infinity,
K  = KL:Jdet^infinity,
B  = K+(Lambda)+M_K00,
H  = B:(C6*k10*Jdet)^infinity,
```

where

```text
M_K00=(C5,C3,C1,
       8*C4-3*C6^2,16*C2-C6^3,256*C0-C6^4,
       k6,k2,mu2,mu4,mu6).
```

`Jdet` is the retained nonzero Jacobian constant formerly named `J`.  It is
not either collision correction ideal `J1` or `J2`; neither `J1` nor `J2`
is a variable in this computation.

## Mandatory noncommutation control

The compiler must separately impose `M_K00` *before* saturation and verify
both the literal identity

```text
(Lambda*Jdet)^19 = -4*Jdet^18*Phi7 mod M_K00
```

and that the restriction-first localization is the unit ideal.  This is a
negative control only.  A run is invalid if it substitutes that ideal for
the closure-first `K` above or omits either test.

## Lanes, caps, and fail-closed policy

- Exact `Q` is the mathematical lane; characteristic `65521` is a separately
  serialized software/control lane.
- Both run on registered AWS EC2 hosts only, with a 6-hour first cap and a
  192-GiB virtual-memory cap.  Timeout, kill, missing/nonunique marker,
  Singular diagnostic, source mismatch, failed negative control, or failed
  certificate replay is **no verdict**.
- `H=(1)` must save a replayed localizer-power lift against `B`.
- `H!=(1)` must save the complete final standard basis.

## Both-outcome scope

If `H=(1)`, the result excludes only the generic `C6*k10*Jdet != 0` K00
incidence for this fixed source-typed `U=2,[6,2]` ordinary-tail client.

If `H!=(1)`, the result records accessible algebraic boundary support only;
it is not a Taylor realization, rational trajectory, or Keller pair.

Either outcome leaves the `C6=0` tip, `k10=0`, other load rays, other square
normal cones, the full collision receiver, Gate T, order two, maximum twelve,
and JC2 unresolved.
