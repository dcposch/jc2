# Preregistration: cutoff-three square-tail desk reduction

Date: 2026-08-28

## Charged specialization

Use the authoritative fixed branch-P raw determinant source and set exactly
the raw deformation parameters of weight below three to zero. Thus all
weight-two `z_*` coordinates vanish, while every weight-three `tt_*`
coordinate and every later raw `F`/`G` slot remains literal. Impose

```text
D0=...=D21=0,  D22=1,
```

with no `G22` slot and no `D23` equation.

## Exact desk charge

Independently compile the cutoff-three prefix nullspace directly from
`RAW_DIRECT_SYSTEM.json`, using only Python standard-library exact rational
arithmetic. Do not import a cutoff-four, cutoff-five, cutoff-six, or
cutoff-seven compiler. Determine:

1. the retained count, prefix rank/nullity, literal endpoint, and exact raw
   lifts of all endpoint carriers;
2. the first nonlinear compatibility rows and every licensed field-radical
   reduction, rederived from cutoff three rather than inherited from a later
   cutoff;
3. the earliest exact invariant-core relation or branch obstruction in the
   later rows;
4. literal source-row provenance, exact reconstruction maps, and live
   mutations for every promoted identity.

Preserve all endpoint carriers symbolically. No carrier may be normalized
without a proved homogeneous or localization argument.

## Resource boundary

Use standard-library exact arithmetic locally. Any heavy Gröbner or
elimination target must be frozen for AWS and must not run locally.

## Stop and evidence rules

* Report a literal unit or low-generator obstruction immediately.
* A field-radical implication must be labelled fieldwise and may not be
  promoted to a nonreduced-scheme equivalence.
* A proper projection, modular point, partial basis, or timeout is
  non-evidence.
* Preserve an honest successor target rather than projecting away an
  unavoidable partner variable.

## Scope firewall

Every conclusion is confined to the fixed branch-P square baseline and the
cutoff-three specialization. No conclusion is asserted for cutoff four, the
full branch-P family, a Keller pair, a counterexample, or JC2.
