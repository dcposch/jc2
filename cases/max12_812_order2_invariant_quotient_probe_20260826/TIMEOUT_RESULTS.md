# Fixed-load order-two invariant quotient: original-pair timeout controls

Date: 2026-08-26

Status: **DUAL AWS TIMEOUT; NO MATHEMATICAL VERDICT.**

The two originally preregistered fixed-load probes reached the source and
deck-parity sentinels, entered the first source-ideal saturation, and timed
out at the exact one-hour cap without reaching `SAT_DONE`, elimination, a
quotient image, a fixed locus, or a genus signal.

| tuple | prime / host | tag | engine | peak RSS | last mathematical marker |
|---|---|---|---:|---:|---|
| A `(2,3,5,7,11,13)` | `32003` / Box03 | `max12_812_order2_invariant_quotient_tupleA_p32003_20260826T040200Z_box03` | `rc=124`, `TIMEOUT_NO_VERDICT` | `703132` KiB | `ORDER2_QUOTIENT_SAT_START` |
| B `(17,19,23,29,31,37)` | `65521` / Box02 | `max12_812_order2_invariant_quotient_tupleB_p65521_20260826T040600Z_box02` | `rc=124`, `TIMEOUT_NO_VERDICT` | `630376` KiB | `ORDER2_QUOTIENT_SAT_START` |

Both jobs used one CPU, exactly `1:00:00` wall time, and zero swap.  The
compilers had already passed the frozen source hashes, complete six-load
specialization, and deck-involution parity checks.  Those compile sentinels
validate the inputs but do not supply a fibre endpoint.

The two timeouts are matched controls against interpreting runtime or small
memory use as geometry.  They do not determine fibre dimension, components,
involution stability after saturation, the invariant quotient, a fixed
locus, normalization genus, an exceptional discriminant, any source map,
order-two emptiness, `(8,12)`, maximum twelve, or JC2.

The already-running A/B cross-prime and tuple-C controls are not consumed in
this report.  They remain independently capped jobs and must be harvested on
their own terminal states.  No larger or longer rerun is licensed by this
timeout result; any successor should first replace the monolithic source
saturation by an exact component/first-normal stratification.
