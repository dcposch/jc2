# TD6 fixed-A3 q2 generic source-DAG certificate (V57)

Status: **exact, independently duplicated localized source identity on
`D(U H B3)`; the three divisor strata remain open.**

Here

```text
H  = C - 3 U^2,
B3 = 4 C^2 U^2 - 4 C V^2 U + 24 C U^4
     + V^4 - 20 V^2 U^3 + 20 U^6.
```

The fixed source-typed center is `(c1,c2,c3)=(C,V,U)` and the transverse
boundary source is

```text
q_beta(t) = t + beta t^2 + t^25.
```

V57 preserves arbitrary-degree original rows.  It replays the staged N13
functional through its current, previous/pole, and first-row ancestry, pins
the genuine V43 P12 source relation, and verifies the exact scalar
composition with residual `-k/50`.  The proof DAG uses exact edge
substitution in the free equation module; it does not replace quadratic
source rows by a linear-only packing.

The denominator ledger has radical support only on `U H B3`.  Thus this
package repairs the generic-open localization and certifies the obstruction
only where `U*H*B3 != 0`.  It does not say anything on `U=0`, `H=0`, or
`B3=0`; those require direct original-row rebuilds.  In particular, it is
not an all-center, all-TD6, SP-2, landing, or JC2 theorem.

## Exact dependency and controls

- transport rank: `3470/3602`;
- first rank: `38/132`;
- previous/pole rank: `38/94`;
- current rank: `25/56`;
- N13 left-null support: one current row, index 13;
- exact N13 proof-DAG SHA256:
  `a906b803a3c0835630884a56e4e9546c7dffa277ba21c36bc3d75027b539da32`;
- exact denominator-ledger SHA256:
  `69c1086b6e302910fe331e7f1c8cfa246a760f429507af2b9d0dd970d1c29ecf`;
- omission of the required N13 edge is an exact negative control;
- P12 without the N13 correction is an exact negative control;
- the genuine 2,893-term P12 control and V43 dependency markers pass.

The producer notes that a full audit of every unused previous/current row is
independent work.  It is not needed by the dependency-closed DAG claim and is
not silently claimed here.

## Independent AWS custody

The same source archive was run on two hosts under 12 GiB caps:

- r6d `100.26.198.153`,
  `/home/ubuntu/runs/td6_v57_dag_r6d_20260825T1048Z`, rc `0`,
  `2026-08-25T10:54:38Z`--`2026-08-25T12:47:15Z`, maximum RSS
  `1050484` KiB;
- Box03 `98.80.65.144`,
  `/home/ubuntu/runs/td6_v57_dag_box03_20260825T1108Z`, rc `0`,
  `2026-08-25T11:04:07Z`--`2026-08-25T12:50:17Z`, maximum RSS
  `1051132` KiB.

The stdout bytes differ only through absolute artifact paths.  The proof DAG
and denominator ledger are byte-identical across hosts.  Source archive
SHA256:
`cc34d029fc30f469239ebb0d4c07eb33992c7de75fbd71242eed24bbbc2df310`.

