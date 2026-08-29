# Hostile review charge — TD6 V84R2 q2--q5 K2 block

Review the exact producer claim in
`xmodel/td6-v84r2-k2-q2q5-zero-producer-20260826.md` and every byte of
`cases/td6_c1_c2_c3_qdead_previous_pole_k2_pilot_v84r2_aws_20260826/`.

Write exactly one report:
`xmodel/td6-v84r2-k2-q2q5-zero-hostile-review-20260826.md`; edit no other
file.  Give verdict `CONFIRMED`, `REFUTED`, or `GAP`.

Charge all of the following rather than accepting marker strings:

1. Verify `MANIFEST.sha256` and `FREEZE.sha256`, the source archive/hash
   closure, both rc files, raw streams, and byte equality of both emitted
   exact tables and denominator files.
2. Reconstruct the licensed q2--q5 source singletons and their omissions from
   the pinned source.  Explain why typed `qd.source_rhs(key).value`, not the
   failed V84R legacy-scalar equality, is authoritative; verify the retained
   X-boundary equality.
3. Inspect the quadratic algebra: diagonal entries are Taylor coefficients,
   mixed entries use the polarized product, the inverse second term and direct
   q-prime variation are included, and q15 target shear is excluded.
4. Verify original-row/source-combination ancestry at transport, FIRST, and
   previous/pole, including varying matrices and every denominator.
5. Verify that `dependent=1` with an empty coefficient table means the one
   dependent previous/pole row pairs to zero with all ten axes.  Attack the
   header-only serializer using the registered nonzero-slot control and a
   deliberately omitted/wrong source control.
6. Reconcile the inherited terminal label `...V84 PASS` with the V84R2 source
   banner and tags.  Decide whether it is a custody repair only or blocks the
   theorem.
7. Enforce scope: only ten pairs in `Sym^2 span(q2,q3,q4,q5)`, only through
   previous/pole, only the common generic principal open.  Deny any inference
   to the other 290 pairs, current, rank-drop fibres, formal integrability,
   nonlinear family, TD6, SP-2, landing, or JC2.

Run no heavy computation on the local Mac.  If independent exact replay is
needed, use a registered AWS host; otherwise give a source-level hostile
audit and state exactly what was not recomputed.
