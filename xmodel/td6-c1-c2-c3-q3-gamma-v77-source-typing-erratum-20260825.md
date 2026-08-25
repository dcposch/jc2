# TD6 V77 q3 gamma source-typing erratum

V77's derivative calculation is not source-valid for the claimed pure q3
line.  The load-bearing producer line `qd.B = EDual(0,1)` varies `B`, which
the imported compiler defines as the coefficient of `t^2` in
`q=t+B*t^2+t^25`.  V77 simultaneously varies the q3 transport RHS and adds
`Q_PRIME[2]=3*gamma`, but it does not add the corresponding q2 transport RHS.
The resulting downstream derivative is a hybrid, not the tangent of
`q=t+gamma*t^3+t^25`.

All gamma/q3-specific claims in
`xmodel/td6-c1-c2-c3-q3-gamma-dual-adjoint-v77-aws-20260825.md` are therefore
quarantined.  This includes its nonzero first-minor derivative, the four-term
raw gamma column, three-term remainder gamma column, varying-multiplier
identity, dual-unit conclusion, and gamma denominator/support audit.  No q3
scheduling inference may consume them.

Moreover, the printed first-minor derivative SHA `c0730fa1...` is exactly the
serializer digest of the zero element (18 coordinates, each `0/1`).  The V77
report's claim that this derivative is nonzero is a direct misinterpretation
of its own output, independent of the source-typing defect.

The base projection is unaffected because both the erroneous and correct
assignments specialize to `B=0` at gamma zero.  V77 remains valid only as
corroboration of the already known fixed-A3 base ranks, genuine base P12,
base remainder `-k/50`, and base original-row identity.  It supplies no
transverse q3 theorem.

The exact repair must set `qd.B=0` and retain only the q3 original transport
key and direct q-prime term, then rerun every source and omission control on
AWS.  The original frozen V77 case/report bytes remain unchanged.  Custody
and source hashes are pinned in
`cases/td6_c1_c2_c3_q3_gamma_dual_v77_source_typing_erratum_20260825/README.md`.
