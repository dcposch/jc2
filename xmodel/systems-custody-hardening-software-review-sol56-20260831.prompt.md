# Systems lane: custody-hardening software review (LANE-CUSTODY-HARDENING/v1)

You are a hostile software review lane. The coordinator (a different
model) authored the custody-hardening changes below; your job is to
find real defects before the campaign leans on them further. This is a
systems review — no mathematics. Do not edit any file outside your
report, and never inspect `jc2-lean`.

charged_input=ops/lane.sh
charged_input=ops/seal.py
charged_input=ops/lane_detach.py
charged_input=ops/test_lane_fallacy.py
charged_input=ops/test_seal.py

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
2a48df3188b931832511bccf0c192a18f2dedffacdbfd85e5d80304c5e24b0d7  {{LANE_INPUTS}}/lane.sh
3096dc47ca24eee147207f6d0e8a8a98095e97ada161c014cc6a27577cd69df3  {{LANE_INPUTS}}/seal.py
310b33b4ef8d9ba3f01c702405338a387b6654aa8fba62579eb0070e84ad9e3c  {{LANE_INPUTS}}/lane_detach.py
fb8c8ef9fa062110b95296f42878b2c9200c4f9166813f9b911029420c26859c  {{LANE_INPUTS}}/test_lane_fallacy.py
5b7ec2b6a76410429d982441fedca2de3cd99cd67055ab96a9f1346d37298106  {{LANE_INPUTS}}/test_seal.py
```

The hardening contract these files claim to implement: (a) prompt
lines `charged_input=<path>` freeze inputs into a per-run snapshot
directory substituted for `{{LANE_INPUTS}}` (charset-validated, no
`..`, no `jc2-lean`, unique basenames, mode 400); (b) launch refuses
prompts lacking an `xmodel/<tag>.md` report path; (c) post-run
`seal.py divert` splits output at the first `<!-- BODY-END -->`
(raw tail to `<tag>.raw.md`, overflow to `<tag>.overflow`, statuses
CLEAN/CLEAN_SEALED/DIVERTED/NO_MARKER/MULTI_MARKER) so overflow and
transient provider errors truncate rather than lose reports; (d)
receipts carry `report_state`; (e) contract violations exit rc=7.

Review for: correctness of the divert boundary logic (byte-exact
marker detection, newline handling, multi-marker, marker inside code
fences, CRLF, marker at EOF without newline); TOCTOU or symlink games
between snapshot, hash-check, and lane start; path-validation bypasses
(unicode, case-insensitive APFS collisions between unique basenames,
absolute paths); failure atomicity (partial snapshot on launch abort,
partial divert on kill mid-write); receipt truthfulness (can
report_state say BODY_SEALED while bytes on disk disagree?); test-suite
gaps (name the specific untested edge, and whether an existing test
would catch a regression you postulate); and the launchd detach path
(orphaned lanes, double-launch of one tag, status lying about a dead
pid). You may run the test files read-only from the snapshot against a
scratch checkout under /tmp, but never against the live repo. For each
finding: severity (BLOCKER/MAJOR/MINOR), the exact lines, a concrete
failing scenario, and the minimal fix. End with a verdict:
SOUND / SOUND-WITH-FIXES / UNSOUND for the campaign's reliance on
receipts as custody evidence. Three hours hard budget.

Write one report and no other file:

```text
xmodel/systems-custody-hardening-software-review-sol56-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 5,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration.
