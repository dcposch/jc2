# TD6 V77 erratum correction: `qd.B` is inert

The earlier V77 source-typing erratum overreached.  Although V77 writes
`qd.B=EDual(0,1)`, no live downstream compiler function reads `B` after V77
replaces `qd.Q_PRIME`.  V77 independently builds the transport with no q2
boundary coefficient, differentiates exactly the original q3 transport key,
and sets exactly the q3 direct derivative in `Q_PRIME[2]`.  Therefore its q3
derivative computation is source-typed; the stale `B` assignment has no
mathematical effect.

The broad q3 quarantine in
`xmodel/td6-c1-c2-c3-q3-gamma-v77-source-typing-erratum-20260825.md` is
withdrawn.  V77's raw/remainder gamma columns, differentiated source
identity, dual-unit result, and denominator audit return to their original
producer tier.  The separate zero-digest correction is unchanged:
`c0730fa1...` is exact zero, so V77 did not prove a nonzero first-minor
derivative and its prose/scheduling statement must not say that it did.

The dual V77R attempts failed only because a negative control incorrectly
expected changing dead state `qd.B` to change first rows.  The successor uses
an actual `Q_PRIME[1]` q2 injection for that negative control and will rerun
on two AWS hosts.  Frozen V77 and both prior erratum surfaces remain
unmodified; exact custody is recorded in the companion case README.
