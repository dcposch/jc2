# V89H10G V1 launch erratum

Date: 2026-08-26

Both V1 deployments passed archive and payload custody checks, then exited at
the first ancestor import because the launcher omitted the inherited sentinel
environment variable `TD6_Q_EXPONENT=2`.  The failure was an assertion in
`replay_v85tf1_total_f.py`; no FIRST row, pivot block, graph, determinant,
P12 object, or mathematical verdict was computed.

V1 is deployment-negative only.  R1 exports the inherited q-exponent and
pivot-policy sentinels without changing the mathematical client.
