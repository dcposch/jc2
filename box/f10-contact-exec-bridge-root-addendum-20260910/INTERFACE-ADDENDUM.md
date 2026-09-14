# ROOT execution-interface addendum — static only

2026-09-10. This supplements, without modifying, the immutable Astra interface
e62418e44e86696136536ba0ce5ec7013f4f8b103399ee46d149ca8a56229670 and implements
the exact documentation remedies in FIRST Fable gate
9d7cda0b6a181b52608a013fac31585541743b086da7d3e2dab773f1db2f831c.
It is not an enabled authority, registration, runtime receipt or certificate.

1. The bridge emits a CONTACT_AUTHORIZED_EXEC JSON line before payload stdout;
   the positive checker must exit0 and emit the subsequent complete line
   `CHECK_OK sha256=DIGEST identity=exact_Q[z,V,W,X]`, with DIGEST equal to
   the independently collected exact input SHA256, not an arbitrary substring
   or a claim that the entire stdout file is only that line. Producer status
   and PRODUCER_STAGE/CANDIDATE_WRITTEN markers alone never establish success;
   Singular -q can mix errors into stdout, and only the independently checked
   exact certificate establishes the intended identity.
2. Serialization constructs tokens, joined text and encoded bytes before its
   64MiB refusal, and parsing also allocates; that refusal is not a
   preallocation memory bound. Finite external CPU/RSS/wall/aggregate limits
   remain mandatory and are not raised by this addendum.
3. Both corrupted-certificate CLI checks must exit2 with the complete stderr
   line `CHECK_FAIL exact polynomial identity is nonzero`. Only when the
   independently established F+1 polynomial is zero may that corruption
   instead produce `CHECK_FAIL F is zero`. Any other error, truncation,
   missing file, parser/header refusal, resource limit or unmatched reason
   fails the control; status2/CHECK_FAIL alone is insufficient. H4+1 has no
   zero-F exception. Both mutations must preserve the original accepted
   certificate and pass the exact-delta/read-back requirements already given.

ROOT compared these exact success/error strings and streams with the unchanged
checker source2e0dda86514a0cdb2aa0a86acf3f32de72645f6566f80a77596b1394a3c9fca7
at lines149-185 as text. No code, imports, syntax tests or mathematics ran.
Fable did not independently read the optional startup-flag manual; ROOT's
earlier selected primary-source read is separate evidence, not a Fable or
installed-runtime verification. Source pins, cooperative-custody limitations,
all seven preflight/dummy controls and future fresh ROOT registration remain
unchanged. No F, source exclusion or JC2 result is asserted.
