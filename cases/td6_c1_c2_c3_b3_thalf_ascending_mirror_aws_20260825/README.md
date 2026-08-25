# TD6 `B3=0`, `tau=1/2`: clean ascending mirror

Frozen status: **exact independent pivot-order mirror** of the theorem-producing
clean V26 reverse certificate already frozen in
`../td6_c1_c2_c3_b3_raw_divisor_aws_20260825/`.

This AWS run uses the identical immutable V26 archive and source closure, but
selects ascending first-band pivots on the raw `tau=1/2` component of the
birational `B3=0` cover.  It completed with `rc=0` on `r6a` at
`2026-08-25T04:23:26Z`.

Exact output facts:

```text
transport_rank=3470/3602
first_rank=38/132
raw_terms=2893
remainder_is_expected_constant=true
remainder_is_constant_unit=true
source_nonzero_rows=28
source_multiplier_terms=1528
source_relation_original_first_row_replay=true
source_relation_plus_one_negative_control=true
termwise_clear_slot_count=31796
certificate_chart=x^29
rational_constant_subfield_descent=true
auxiliary_curve_subfield_descent=true
```

The constant is the same `-k/50` unit as in the reverse certificate.  The only
chart boundary is `w=0` (printed as `x=0` by this one-variable field), which is
the already frozen origin.  This mirror is corroboration, not a new locus or a
new hypothesis: either original-row identity alone is sufficient on `D(w)`.

AWS/source custody:

```text
archive_sha256=b96ebc627c1be7a07691428aa7d8eca10fe70af0e2599f62929989080517e053
SOURCE.sha256=93cf77eaf4805b562c1fc6a862fde317538781555b1de5cf0c8d8fef0c3853cb
producer_sha256=91745b0ef827306e27a7126503d637539b47fb430262d380faad306ee9a510de
stdout_sha256=bb694e0da81dc482c7d954af87f41fcc1fa03af1c4ea9144b86b8873cebe9baf
stderr_sha256=2de86246392e2c5ee454b463ba3544bdfe062ee26f783f9ec8f34a95ee70f4ed
```

The nonempty stderr is `/usr/bin/time -v` telemetry and records exit status
zero.  `source-check.stderr` is empty.

Scope is unchanged: the fixed source-typed normalized three-center TD6
section only.  This is not a neighborhood theorem, whole-TD6/SP-2 kill,
maximum-degree theorem, or resolution of JC2.
