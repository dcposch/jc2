# Preregistration: V9 exact coefficient export

Date: 2026-08-26

Status: **MECHANICAL SUCCESSOR TO V8; NO REES OR CAMPAIGN VERDICT.**

Import the frozen V8 explicit-normal-form compiler unchanged.  For every
row, write the total and frozen coefficients at sigma grades 10, 11, and 12
to hash-bound `.poly` files.  All V8 source, normal-form, specialization,
deck, extraction, dependency, and negative-control sentinels remain active.
The only program mutation is adding the 42 writes and their unique
sentinels.  Run exact Q and an independently compiled good-prime control on
AWS.  Missing files, unsafe serialization, a V8 control failure, a Singular
diagnostic, or a hash mismatch is no verdict.

