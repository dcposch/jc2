# V26R1D serialized-standard-basis custody erratum

Status: `PRODUCER_PASS_REPLAY_WARNING_NO_THEOREM`.

R1D fixed the multi-column matrix validator and its producer process returned
a tracked standard basis with exact affine dimension `3`.  Its serialized
second-process identity replay was exact.  However, the replay reconstructed
`string(G)` as an ordinary ideal and then called `reduce` and `dim` on it
without restoring the standard-basis attribute.  Singular printed twice:
`G is no standard basis`.  The worker did not initially classify that warning
as fatal.

Consequently R1D is retained only as producer evidence.  Its claimed complete
replay status and theorem endpoint are not consumed.

R1E keeps the exact serialized identity `J*T=Graw`, which proves
`(Graw) subset (J)`.  It then computes `G=std(Graw)`, checks every generator of
`J` reduces to zero modulo `G`, proving the reverse inclusion, and derives
properness and dimension only from this freshly computed standard basis.  The
transform-deletion mutation is checked against `Graw`, the object to which
the serialized transform is typed.  The runner now also fails closed on any
`is no standard basis` warning.

No polynomial, ideal, matrix, minor, field, resource cap, rollback tag, or
mathematical endpoint changed.  R1D itself implies no grade-seven stratum,
jet, arc, closure, or JC2 result.
