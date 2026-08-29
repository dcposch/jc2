# Opus 5 hostile review — generalized tail-7 field obstruction

You are Opus 5 acting as an independent hostile mathematical reviewer in
`/Users/dc/code/math/jc2`.  This is a promotion gate in the plane Jacobian
conjecture campaign, so fail closed: a prose paraphrase or trust in the
producer's verifier is insufficient.

First verify and record these two SHA-256 pins, and stop with a `GAP` report if
either differs:

```text
8eed5736afba781ce6bf522db7a8348c0f7ce0b1f4dbe885c9ba6eed95bdd882
  xmodel/ggv-upper-endpoint-tail7-field-obstruction-r0-sol-ultra-20260828.md
29ffa224682d8f424b1ff5f33fc8c1227e8805f1b67cec0610b74fcc14599955
  cases/ggv_8_28_upper_endpoint_tail7_projective_r14_20260828/SOURCE.sha256
```

Read the charged producer report completely.  Inspect only its exact named
dependencies and frozen source/evidence needed for this review.  Never enter,
list, search, read, build, or modify `jc2-lean`; do not touch AWS or running
lanes; do not run heavy local computation; and do not edit any canonical
ledger (`AUDIT.md`, `APPROACHES.md`, `PROGRESS.md`, `notes.md`, or
`COORDINATION.md`).  Desk-scale exact rational Python and the already tiny
8-variable Singular replays are allowed.  Ephemeral helpers may be created in
`/tmp` but must be removed before completion.

Perform the following hostile review, with literal command outputs, hashes,
and exact arithmetic in the report:

1. From the projective case directory run `sha256sum -c SOURCE.sha256` and
   fail closed on any mismatch.  Check the upstream frozen tail-7 source and
   the shared-block/AWS custody pins, rather than merely copying the report.
2. Independently rederive from the frozen
   `TAIL_DEFORMATION_SYSTEM.json`, using fresh exact-`Q` polynomial and RREF
   code that neither imports nor invokes `compile_projective_r14.py` or
   `verify_projective_r14.py`:
   - triangular rows 14 through 21 while withholding `p32,p87` as pivots;
   - the literal endpoint equation `-1-p32*p87=0`;
   - an exact row-21 compatibility
     `-(3/4)*p86*p87^2=0`, including its actual index/order and enough row
     rank/free/compatibility counts to expose pivot drift;
   - the row-14 elimination rank 10 on `p33,...,p43`, free mode `p43`, and
     exactly 16 nonzero homogeneous degree-2 compatibilities supported exactly
     on `p78,...,p87`.
   Include at least one non-vacuity/mutation control for this clean-room
   derivation and report the independent helper's SHA-256 (or, if executed
   entirely through a heredoc, a SHA-256 of the exact code bytes quoted in the
   report).
3. Independently substitute `p87=1,p86=0`, canonically encode the ordered 16
   polynomials, and test byte-for-byte equality with the frozen shared block.
   Recompute and report both the ordered-term byte SHA-256 and the shared JSON
   SHA-256.  Explain why this normalization is licensed for the *homogeneous
   necessary row-14 subsystem* without claiming a torus symmetry of the full
   residual system.
4. Only after the clean-room derivation, rerun the frozen independent verifier
   and the direct cofactor identity:

   ```sh
   cd cases/ggv_8_28_upper_endpoint_tail7_projective_r14_20260828
   python3 -B verify_projective_r14.py
   /opt/homebrew/bin/Singular -q R14/r14_nullstellensatz_replay_q.sing
   ```

   Require literal `status: PASS`, `DIRECT_REPLAY_LHS=1`, and
   `DIRECT_REPLAY_OK=1`.  Inspect the 16 rational cofactors and directly decide
   whether `1=sum_i h_i f_i`; do not substitute the earlier AWS `J[1]=1` line
   for this identity.  Record the replay source and stdout hashes and check
   the frozen AWS stdout separately for its literal three markers.
5. Audit the logic and scope adversarially:
   - endpoint implies `p87 != 0` over a field;
   - in characteristic zero the row-21 relation then implies `p86=0`;
   - homogeneous dehomogenization plus the unit identity yields the claimed
     contradiction;
   - identify exactly which characteristics, if any, the displayed rational
     proof does or does not cover;
   - distinguish field-valued points, scheme assertions, the fixed
     square-tail/tail-7 specialization, unrestricted branch P, other branches,
     and JC2;
   - check that the conclusion does not rely on the producer's explicitly
     forbidden global diagonal-scaling argument.

Classify each charged atom `CONFIRMED`, `REPAIRED`, `GAP`, or `REFUTED`, and
give one overall verdict from `CONFIRMED / GAP / REFUTED`.  State the narrowest
licensed promotion and stop rule.  Include pinned model/CLI identity and a
compact exact replay transcript.  A finding that changes wording but not the
mathematical obstruction must be labeled `REPAIRED`, not silently normalized.

Write exactly one persistent output and change nothing else:

`xmodel/ggv-upper-endpoint-tail7-field-obstruction-crossreview-opus5-20260828.md`

Print that report's SHA-256 at completion.
