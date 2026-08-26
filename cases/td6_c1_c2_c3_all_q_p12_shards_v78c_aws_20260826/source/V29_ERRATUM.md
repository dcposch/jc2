# V29 source-pin correction

V28 failed before import or algebra because the new wrapper asserted an
incorrectly transcribed SHA-256 for the byte-identical V27 trivariate source.
The V28 `SOURCE.sha256` itself correctly recorded the source as
`1fb512643f31b4eda6c0e96ca1adbfe3e79599986c7c095b825605a4145fdaea`;
the wrapper literal instead contained a different suffix.  V29 changes only
that literal and refreshes the source closure.  No mathematical code or
evidence was produced by the failed V28 startup.
