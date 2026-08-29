# Hostile implementation review: row-streaming `T-rs-0` V2

Work in `/Users/dc/code/math/jc2`.  This is a source/software equivalence
review only.  Do not run Singular or any heavy algebra locally, do not edit
campaign source or ledgers, and do not trust PASS markers.

Read completely and rehash:

```text
b505f3c51ec8a5e10936119826445d9d2b92e47dd936f6f0996ce13e52b18397
  cases/max12_812_order2_p0_total_rees_t_rs0_stream_v2_20260826/FREEZE.sha256
5b176dfd0747f3736bc4519077877f4d877b5b726b9701e1b9dcaf56e059a112
  cases/max12_812_order2_p0_total_rees_t_rs0_stream_v2_20260826/compile_t_rs0_stream.py
4ff10d85aeb91f3853a4fd2c89ac2e0fe93bd07fd2c3769241cd8f40afb01949
  cases/max12_812_order2_p0_total_rees_t_rs0_stream_v2_20260826/validate_t_rs0_stream.py
51c294e0ae3d07ced3dac380814d4767bec1e5cc63bd1159cd76ce698f3f69ea
  xmodel/max12-812-order2-p0-total-rees-t-rs0-discovery-implementation-review-grok-20260826.md
```

Also read every file pinned by `FREEZE.sha256`, the reviewed V0R1 compiler
which V2 imports, its preregistration/validator, and the relevant transitive
source compilers/tails needed to assess equivalence.

Adversarially determine whether V2 computes exactly the reviewed V0R1
mathematical transcript while releasing one row at a time.  In particular:

1. Compare every total/frozen source formula, row, target, quotient grade,
   dependency bit, negative control, retained cusp coefficient, `Delta`, and
   pass gate.  Find the earliest mismatch if any.
2. Check that row-major accumulation cannot misstate the common order or
   grade support, and that overwriting/releasing Singular `poly` objects
   cannot corrupt the six retained coefficients.
3. Check the literal 76+7 manifests independently, variable ordering,
   characteristic handling, and every source/hash boundary.
4. Attack the strengthened validator: forged stdout, altered compiler JSON,
   omitted candidate, inconsistent grade bit/count, stale metadata, duplicate
   sentinels, zero/nonzero `Delta`, timeout, and an engine diagnostic.
5. Distinguish a math/source defect, a software/custody defect, and a scope
   wording defect.  Do not infer any engine result from a live job.

Write the report only to
`xmodel/max12-812-order2-p0-total-rees-t-rs0-stream-v2-implementation-hostile-review-grok-20260826.md`.
End with exactly one scoped verdict: `GO_STREAM_EQUIVALENT`, `REPAIR`, or
`NO_GO`, followed by a firewall saying this is no Rees, moving-p, order-two,
maximum-twelve, or JC2 theorem.
