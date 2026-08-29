# Lambda-zero origin q15 inhomogeneous syzygy adapter r2

Date: 2026-08-28

## Frozen predecessor failure

The two r1 sparse jobs are classified `ADAPTER_FAILURE`, not mathematical
failures.  Exact receiver deduplication and the tiny solver self-check passed,
but the search adapter asserted that the endpoint was homogeneous.  The frozen
endpoint actually has term degrees `{3,4,5,6,7}`, so both jobs stopped before
constructing a Macaulay system and emitted no certificate.

The complete immutable r1 failure archives are:

```text
739db1684e532df160f87aaa430d5690afce5e00b20706c6a83d308bbffd6e91  g15 r1 archive
f1598f420d1e916b38687b93c700c632ac2ebab41fbb0ffe0a342ad74ce4e306  full r1 archive
eabe45db71777edc56f3b3d1717a6fd4f3f3c71c44fdf318d71a9babe3447a57  exact DEDUP.json
```

r2 is a new source tree and namespace.  r1 bytes are not mutated or reused as
results.

## Exact adapter repair

For total degree bound `D=7`, r2 retains every generator multiple `m*g_i`
with

```text
deg(m) <= D - max_term_degree(g_i).
```

This is the ordinary inhomogeneous total-degree Macaulay span.  It includes all
multiplier degrees from zero through the bound; it does not homogenize,
truncate lower endpoint terms, or silently keep only top-degree multiples.
The solver still emits a full coefficient list and directly replays the
resulting polynomial against the entire inhomogeneous target over the selected
prime field.

The desk self-check covers a mixed-degree polynomial, exact enumeration of all
monomials through degree two, a replayed consistent linear solve, and an
inconsistent control.  Plan-only replay against the frozen exact DEDUP input
gave:

```text
g15/target support: 28 variables, 10 generators, 1102 columns
full/active support: 40 variables, 16 generators, 14396 columns
target degrees:      3,4,5,6,7
```

Both counts are below the already registered 5000/20000 column caps.

## Runs and verdict firewall

Rerun only the two repaired jobs in fresh namespaces:

```text
ggv_origin_syzygy_g15_d7_p65521_r2_20260828T112300Z_r6c
  g15 subset, target-support multipliers, p=65521, D=7, <=5000 columns,
  1200-second inner cap

ggv_origin_syzygy_full_d7_p65519_r2_20260828T112300Z_r6b
  full exact-dedup base excluding the open-equation generator, active-support
  multipliers, p=65519, D=7, <=20000 columns, 2400-second inner cap
```

The omitted `c2*invc2-1` generator makes any found base-ideal membership
certificate stronger; a bounded failure remains nonmembership in neither the
base ideal nor its saturation.  A replayed modular syzygy is navigation only
and authorizes a separately frozen exact-Q lifting attempt.  A timeout,
inconsistent bounded ansatz, modular nonmembership, or solver error proves no
mathematical claim.  Any nonzero solver exit other than timeout is now marked
`ADAPTER_FAILURE_BOUNDED_SOLVER_ERROR` rather than being conflated with an
absent signal.

Use the same frozen exact reduction hashes, exact dedup proof, one-core
64-GiB/16-GiB limits, one-hour master cap, zero-swap gate, EC2 r6i identity and
idle-process gates, immutable source, process-group guard, and no-orphan census
as r1.  No exact-Q computation, install, canonical file, `jc2-lean`, HENS
namespace, lambda job, or unrelated AWS process is in scope.

