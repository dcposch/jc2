# Correction to the V77 source-typing erratum

Date: 2026-08-25  
Status: **NONMUTATING LOAD-BEARING CORRECTION**

This note retracts the source-contamination claim in
`cases/td6_c1_c2_c3_q3_gamma_dual_v77_source_typing_erratum_20260825/`
without changing any frozen bytes there or in V77.

The old erratum correctly noticed that V77 assigns
`qd.B=EDual(0,1)`, but incorrectly inferred that this injects a q2 tangent.
In the imported q2 module, `B` is read only while the module's initial
`Q_PRIME` and `build_first_band_system` definitions are formed.  V77 does
not call that builder: it builds transport directly with boundary
`{1:1,25:1}`, carries the unique q3 source key `('g','X',0,3)`, and then
replaces `qd.Q_PRIME` with `{0:1,2:3*gamma,24:25}`.  The downstream compiler
functions read `Q_PRIME`, not `B`.  Thus the later `qd.B` assignment is stale
and semantically inert.

The failed clean-source V77R control independently exposed the mistake:
changing only `qd.B` left the first rows exactly unchanged on both Box02 and
r6d, so the deliberately expected inequality failed before any q3 result.
That is a software/control failure, not a mathematical q3 failure.

Accordingly, the old erratum's broad q3 source quarantine is withdrawn.
V77's q3 raw column, q3 remainder column, differentiated multiplier identity,
dual-unit calculation, and q3 denominator audit retain their original
producer status.  One distinct correction remains fully valid:
`c0730fa1...` is the canonical digest of the exact zero field element, so the
V77 report's prose claim that the selected first minor has a *nonzero* q3
derivative is false.  The supported statement is that this selected minor
has zero first derivative.

A clean V77R rerun removes the stale `B` assignment, asserts its inertness,
and uses an actual `Q_PRIME[1]` injection as the q2-leak negative control.
Until that succeeds, no new q3 theorem is claimed here.

## Pinned inputs

| object | SHA-256 |
|---|---|
| original V77 replay | `5e088d8c9b9f7f4f74de108c816f51e5f69d477572fa8b7ec0cf475efcb1ec22` |
| imported q2 compiler | `0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357` |
| original V77 report | `53e590c3a22aad8333933d776aab50bed148d1918f50d124891d569437f2512d` |
| superseded erratum report | `4169eb1b72b4a2666c6b5c9a5b1d23106d9d0e61af22e48dff950ecca01e7035` |
| V79 failed-control source archive | `cc7717b46d667726d0b4b51b51027b19dfbbb3823104018fca4a912af6eb6579` |
| Box02 failed-control stderr | `ab24b32df299c2cfc2e421701c5fc581327b88fffeb087452316879b5b2f7f51` |
| r6d failed-control stderr | `750c06d5fdad2f105c88bd9f620bf3cdb4d2374101820c7f8816548544abc39f` |

