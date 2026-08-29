# V18 fail-closed record: identifier collision

Date: 2026-08-26

Both registered V18 lanes compiled their exact inputs but Singular stopped
before standard-basis computation because the generated script reused `E12`
for a polynomial and an ideal.  Both engine wrappers returned zero because
Singular reports this language error on stdout without a nonzero process exit;
the fail-closed validators correctly rejected the diagnostic tokens and wrote
`validator_rc=1`.

No mathematical conclusion follows from either V18 lane.  V18R1 repairs only
the duplicate ideal name under `PREREGISTRATION_V18R1.md`; the original V18
outputs remain failed provenance and must never be cited as a chart verdict.
