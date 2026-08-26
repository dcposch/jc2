# V82P2 preventive reporter erratum

The immutable V82P source inherited V82S's invalid empty-table denominator
constructor `CTX(1)`.  At preregistration time V82P had not yet reached the
serializer, so this is a preventive, fail-closed software correction rather
than a mathematical endpoint.

V82P2 replaces only that constructor by the already exported `ONE`, asserts
`ONE == CTX.constant(1)`, and adds a separately executed header-only
empty-table positive control.  It then reruns the complete transport, first,
previous, pole, source-replay, denominator, and omission pipeline on two
independent AWS hosts.  No V82P conclusion is consumed merely because the
reporter was patched.
