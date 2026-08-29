# Preregistration: cutoff-five square-tail desk reduction

Date: 2026-08-28

## Charged specialization

Use the authoritative fixed branch-P raw determinant source and set exactly
the raw deformation parameters of weight below five to zero.  Equivalently,
the prefix before the first retained deformation is the exact square family

```text
C=X^4-1,  H=C^2,  U=H+t/2,  F=U^2,  G=U^3.
```

Retain every literal raw `F` and `G` slot of weight at least five.  Impose

```text
D0=...=D21=0,  D22=1,
```

with no `G22` slot and no `D23` equation.

## Exact desk charge

Independently recompile the cutoff-five prefix nullspace from
`RAW_DIRECT_SYSTEM.json` using only standard-library rational arithmetic.
Do not import a tail-six or tail-seven compiler.  Determine:

1. the retained count, prefix rank/nullity, and literal constant endpoint;
2. the earliest nonlinear compatibility rows and every licensed
   field-radical divisibility reduction;
3. the smallest exact later-row subsystem which still retains the four
   endpoint determinant carriers symbolically;
4. exact raw-slot lifts, source-row provenance, reconstruction maps, and a
   regression which detects deletion of the `V0^2` contribution to the
   endpoint carrier `p86`.

No carrier may be normalized.  A field-radical reduction must be labelled as
such and may not be promoted to an equality of nonreduced schemes.

## Resource boundary

The producer may use Python's standard library and exact `Fraction`
arithmetic locally.  It may emit a Singular input as an immutable coefficient
custody artifact, but it must not run a local CAS and must not launch AWS.

## Stop rules

* A literal exact unit or a directly replayed low-generator identity is an
  immediate report.
* Otherwise freeze the first honest subsystem below roughly thirty operative
  variables, with no unsupported projection or normalization.
* A proper projected core is not an endpoint witness.  A modular point,
  timeout, partial basis, or unreviewed numerical solve is non-evidence.

## Scope firewall

Every conclusion is confined to the fixed branch-P square baseline and the
cutoff-five specialization.  No conclusion is asserted for the full branch-P
family, for a Keller pair, for a counterexample, or for JC2.
