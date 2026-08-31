# Systems lane: P0 custody patch (post-review fixes)

You are a systems patch lane. A hostile software review (charged
below, your own model family's product) returned UNSOUND with typed
findings. The coordinator has triaged a P0 subset for immediate fix —
the findings that bite under the campaign's ACTUAL threat model
(honest-but-erring providers, transient provider errors, accidental
misuse), not the full hostile-provider redesign. Produce a patch as
your report; you do not apply it. Do not edit any file outside your
report; never inspect `jc2-lean`.

charged_input=ops/lane.sh
charged_input=ops/seal.py
charged_input=ops/lane_detach.py
charged_input=ops/test_lane_fallacy.py
charged_input=ops/test_seal.py
charged_input=xmodel/systems-custody-hardening-software-review-sol56-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
2a48df3188b931832511bccf0c192a18f2dedffacdbfd85e5d80304c5e24b0d7  {{LANE_INPUTS}}/lane.sh
3096dc47ca24eee147207f6d0e8a8a98095e97ada161c014cc6a27577cd69df3  {{LANE_INPUTS}}/seal.py
310b33b4ef8d9ba3f01c702405338a387b6654aa8fba62579eb0070e84ad9e3c  {{LANE_INPUTS}}/lane_detach.py
fb8c8ef9fa062110b95296f42878b2c9200c4f9166813f9b911029420c26859c  {{LANE_INPUTS}}/test_lane_fallacy.py
5b7ec2b6a76410429d982441fedca2de3cd99cd67055ab96a9f1346d37298106  {{LANE_INPUTS}}/test_seal.py
3e4b7ee6d96eff60f74d00c3f0a765b24b44505b471fe6ca40ccad22ac91289f  {{LANE_INPUTS}}/systems-custody-hardening-software-review-sol56-20260831.md
```

P0 scope — fix exactly these, per the review's minimal-fix
prescriptions, at the review's cited lines:

1. D1 (BLOCKER): `seal.py` divert must reject ANY bytes beyond one
   canonical seal serialization after the marker — a valid seal plus
   a trailing provider-error line must take the DIVERTED path (raw +
   overflow banked), never CLEAN_SEALED. Pick one canonical form,
   document it in the module docstring, state the CRLF policy.
2. D2 (MAJOR): EOF marker without terminating newline must NOT be
   CLEAN in divert; return a distinct UNTERMINATED_MARKER status and
   have `lane.sh` map it to report_state=PARTIAL_NO_MARKER semantics
   with rc 7 (or a sibling typed state — your choice, but verify and
   divert must agree on what "sealed" means; that is the invariant).
3. D3 (partial): when overflow path is occupied, fail WITHOUT leaving
   a newly created raw file (clean up); re-validate the report bytes
   immediately before the atomic replace and re-classify if they
   changed. Skip the full fsync/transaction-manifest redesign.
4. S1 (lexical subset): validate charged paths byte-wise under
   LC_ALL=C; reject `.` components as well as `..`; case-fold the
   jc2-lean exclusion and the basename-uniqueness key; reject any
   path with a symlink in ANY component (python helper is fine).
   Skip the dirfd/openat rewrite.
5. S5: route every hardening-contract violation through exit 7
   uniformly (launch-time refusals included); record the provider's
   own rc in a new receipt field `adapter_exit_code` so nothing is
   lost; post-run boundary violations force rc 7 even when the
   adapter rc was nonzero.
6. R4 (partial): reject CR/LF and other control characters in
   prompt-supplied paths before they are emitted into receipts.

For EVERY item add or extend tests in the two test files, following
the review's coverage table: sealed-plus-suffix; unterminated EOF
marker through divert AND the lane-level state; CRLF divert boundary;
occupied-overflow raw-absence assertion; `./jc2-lean`, uppercase
exclusion alias, ancestor-symlink, `.` component, absolute path,
non-ASCII-under-UTF8 rejection; rc-7 uniformity including nonzero
adapter rc + malformed report; control-char path rejection. Preserve
all existing passing behavior; keep the patch minimal and idiomatic
to the existing code; do not rename existing receipt fields; new
receipt fields are additive only.

Report format: one section per finding with a one-paragraph design
note, then ONE fenced unified diff (`diff -u` format, paths relative
to repo root, against the frozen bytes you verified) covering all
files, then a final section listing every new/changed test name and
what it asserts. The coordinator will apply the diff and run the full
ops suite; a diff that does not apply cleanly to the charged hashes
is a failed lane. Three hours hard budget.

Write one report and no other file:

```text
xmodel/systems-custody-p0-patch-sol56-20260831.md
```

Create the report file with a skeleton of section headers as your
very first action and append each completed section as you finish it.
End its body with a single standalone `<!-- BODY-END -->` line and
write absolutely nothing after that line. Do not include a
`charge_basis` declaration.
