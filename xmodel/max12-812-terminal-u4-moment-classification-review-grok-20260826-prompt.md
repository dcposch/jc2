You are the hostile independent reviewer of one exact terminal-classification
experiment in the plane Jacobian-conjecture campaign.  Work from the frozen
bytes, not from the producer's summary or expected counts.

Frozen case:
`cases/max12_812_terminal_u4_moment_classification_20260826/`

Required hashes:

```text
cfbd82dd8e03aa5f7c753e442e9994b011a2fa1fe1e0bdeea197a9663570e354  REGISTRATION.md
31f9b51beca1702ba23443ced509350d7769c2ef52dad5a62051e33883c347ae  enumerate_u4.py
d98fdd62620c5419a07208aedae71b17e074653f79abc5c0edae11a169760c1d  run_aws.sh
9dbdb7ae1d8668924c25eef553840e8c4325d7ab5557ae36becdf1bc7218a1e5  launch_remote.sh
8719cb71fa2e70d2aa11e20243e252fafd7e0aad2ef782449faff754fac143ee  aws_r6d/output/classes.json
e3bca8cfb7ad028dcfc61e28be142db47591f4651b13e61264759d51d2836f78  aws_r6d/output/stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d/output/stderr
```

Charged theorem and its hostile review:

```text
8e1535aa6ed38a7046be26f64ffc493200685d20473313ae74fda423c21fe549
  xmodel/max12-812-terminal-logderivative-pte-u3-classification-20260826.md
91772fd754923cab3a382e3356b661238244b8e2cb2e183c84b6c36ea07a701c
  xmodel/max12-812-terminal-logderivative-pte-u3-review-grok-20260826.md
```

The AWS result reports `m=2`: 5 tested/5 viable/5 affine classes
(1 rational, 4 quadratic), and `m=4`: 36 tested/35 viable/44 affine classes
(5 rational, 39 quadratic).  These counts were not preregistered.

Independently attack every load-bearing point:

1. Re-derive the normalized `U=4` moment equations with support
   `(0,1,x,y)`, including the quadratic, discriminant
   `4*n1*n2*n3*n4`, the `n1+n2=0` linear branch, and the next nonzero moment.
2. Audit profile exhaustiveness: sign types, unordered partitions, bounds
   `3<=D<=3m`, positive parts at most `m`, unrestricted positive pole parts,
   and exact Kummer gcd.  Look for duplicate or missing label assignments.
3. Audit affine canonicalization over every ordered normalization pair and
   permutations of weighted same-sign points.  Check whether the two
   quadratic conjugates are correctly merged or separated over the
   algebraic closure, and whether the representation key can falsely merge
   inequivalent classes.
4. Audit exact quadratic arithmetic and every certificate: moments 0--2,
   nonzero moment 3, coprime monic `A,B`, exact degree of `A-B`, squarefree
   `A-B`, Wronskian sign/constant, and minimal-radicand exponents.
5. Independently check that the existence checksum
   `3*gcd(parts)<=D` is the correct Boccara--Zannier criterion at `U=4`, and
   that using it as a fail-closed equality does not assume the desired class
   count.
6. Inspect the complete JSON, not just the summaries.  Recompute enough
   small profiles by hand to test both rational and quadratic branches, the
   sole empty profile, deduplication, and the 5/44 totals.  Identify the
   strongest theorem licensed and the exact remaining terminal/lower-tail
   firewall.
7. Check AWS provenance, hashes, rc, diagnostics, resource cap, and zero
   swap.  A clean implementation replay is engine evidence; distinguish it
   from an independent proof of census completeness.

The Mac is coordination-only.  Do not execute the enumerator, Singular,
Lean, Sage, or any nontrivial exact-algebra computation locally.  This is a
text/manual audit; if a substantial rerun is required, say so rather than
running it.

Write the review only to
`xmodel/max12-812-terminal-u4-moment-classification-review-grok-20260826.md`.
Include recomputed hashes, any smallest counterexample/repair, independently
checked sample profiles, corrected counts if needed, and end with exactly one
of `CONFIRMED`, `REPAIR`, or `REJECTED`.  Do not edit the frozen case or any
top-level campaign file.
