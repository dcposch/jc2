# V21 R0 fail-closed source-replay wrapper

Date: 2026-08-27

R0 verified all frozen hashes, replayed all 66 serialized syzygy identities,
freshly computed 66 syzygy generators, and replayed every load, image,
target, and sign-mutation control.  It then failed closed before the matrix
and dual stage for two wrapper reasons:

1. a reduced module retaining zero columns was compared to the literal zero
   module, so the mutual-generation check reported false without testing its
   component vectors; and
2. this Singular build uses `quit`, not the emitted `exit(integer)` syntax.

The Python wrapper rejected the transcript and emitted no result.  This is
not a mathematical endpoint and does not affect V17 or V18.  The complete
frozen R0 source and run transcript are preserved in `aws_q_box01_r0_failed/`.
R1 may change only those two source-replay control semantics and must use a
new freeze and AWS tag.

