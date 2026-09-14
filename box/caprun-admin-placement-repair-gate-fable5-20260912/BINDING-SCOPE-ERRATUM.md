# Binding-scope erratum — authoritative before any concrete binding

2026-09-12. Supersedes only the “exact text” enforcement wording in the frozen
Sol report ae02a5b31cdf33c9681ebb50396a5d0dc841bece74b8da08957119398ded9d63
and binding contract08bf4806bfb4829f8e86bdbcf2da7404079e2199a8022b7100124f039ce62aeb.
Their artifacts remain unchanged. Fable FIRST6b9b54c4674ed6c7b3d6cc1514708eab5af2d7db29c7f094128d18a7a327e48f
accepts the following conditional contract without a SOURCE edit.

The setup's two sed1–6 comparisons check only the first six lines modulo
trailing newlines. They do NOT certify EOF, a terminating LF, or the absence
of bytes beyond line6. Do not advertise or rely on that stronger predicate.

ROOT constructs each admin manifest as EXACTLY five rows in the documented
role order. Each row is the bound program's64-hex SHA, two spaces, the exact
stage name or absolute installed path, then one LF; nothing precedes or
follows those rows. ROOT independently compares the entire resulting file
with those five expected byte strings, including LF and EOF, and freezes its
SHA into the setup's expected-manifest field. Exactness is then carried by
that frozen file hash. Byte count is supplementary, not a contents check.
Every role hash must agree with the corresponding bound program, security,
configuration and remote8-role manifest. No template hash substitutes for
bound bytes; no circular self-hash is introduced.

No assumptions about sha256sum's treatment of blank rows are necessary.
No source, helper, negative control or runtime has been executed by this
erratum; all original physical/clock/authority/review gates remain in force.
