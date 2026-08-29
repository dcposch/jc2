# V82QSD AWS denominator-diagnostic launch

Source archive SHA-256:
`86bf989c2ac8b4e263b1f2de19004e32098cd0df10e225828f3f448b7b3b6757`.
Source closure manifest SHA-256:
`8cf8174d554e0e728254fe803c964ad96c5fca26c667f2b7728635fab56fcd9a`.
Patched reporter-parent SHA-256:
`336b9228378e990f896ea82729fef6a9384135a75a01af349574cb9a5ef42c0c`.

- Box03 run: `/home/ubuntu/runs/td6_v82qsd_current_box03_20260826T073444Z`
- Box03 supervisor PID: `180985`
- Box03 lanes: q2, q3, q4, q5, q6
- r6d run: `/home/ubuntu/runs/td6_v82qsd_current_r6d_20260826T073444Z`
- r6d supervisor PID: `246642`
- r6d lanes: q7, q8, q9, q10

Every lane is separately registered as
`td6_v82qsd_current_<host>_q<exponent>_20260826T073444Z`, capped at 2 GiB,
and bounded by a two-hour timeout.  The reporter emits exact denominator,
factorization, rank, and kernel data before retaining the inherited fail-closed
assertion.  An rc=1 with the diagnostic file present is therefore expected
evidence of a foreign rank-drop factor, not a theorem failure or a licensed
generic-open coefficient table.
