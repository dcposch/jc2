# D1 — Canonical seal boundary

`verify_bytes` now accepts exactly the UTF-8 byte string emitted by `_canonical_seal`; its fixed post-body line ending is LF, while an LF- or CRLF-terminated marker remains part of the body and is hashed byte-for-byte.  The divert classifier consequently treats a valid canonical seal plus even one suffix byte (and every CRLF-encoded or otherwise noncanonical seal tail) as overflow, preserving the untouched input in the raw bank and the complete tail in the overflow bank instead of reporting `CLEAN_SEALED`.

# D2 — Unterminated marker

Divert still detects an exact standalone marker at EOF, but it no longer calls that report clean when the marker has no LF or CRLF terminator: it returns the distinct, non-mutating `UNTERMINATED_MARKER` status.  `lane.sh` maps that status to `report_state=PARTIAL_NO_MARKER` and forces final rc 7, matching `verify`'s existing refusal to regard the same bytes as sealed.

# D3 — Divert race and cleanup

The diversion attempt tracks only the raw and overflow files it successfully created; every pre-replace failure removes those files, so an occupied overflow target cannot strand a new raw artifact or disturb the pre-existing overflow.  The existing last-moment report reread is changed from an error-only comparison into a retry boundary: if bytes or metadata changed, the staged report and this attempt's sidecars are removed, the newly read stable bytes are reclassified, and only an unchanged classification reaches `os.replace`; the requested larger fsync/manifest transaction redesign remains out of scope.

# S1 — Charged-path lexical hardening

The launcher exports `LC_ALL=C` before shell pattern checks, rejects absolute paths plus `.`/`..` components, folds ASCII case for both the `jc2-lean` exclusion and basename-uniqueness key, and calls a small `os.lstat` walker that rejects a symlink at every charged relative-path component without resolving it.  Lexical exclusion runs before that walker, so excluded aliases are refused without traversal; the deliberately scoped fix retains the existing hash/copy flow rather than introducing the deferred dirfd/openat redesign.

# S5 — Uniform hardening exit status and adapter receipt

Launch-time report-path and charged-input contract refusals now return 7, as do all post-run BODY-END boundary failures regardless of a nonzero provider result; a no-marker report remains informational only when no BODY-END contract was declared.  The status returned directly by `wait` is captured before any lane override and added to the receipt as `adapter_exit_code`, while the existing `exit_code` field continues to record the final lane rc, preserving both facts without renaming or changing any existing receipt key.

# R4 — Receipt-safe paths

Before any prompt-derived path can be echoed into a receipt, the launcher rejects control bytes: the CLI-supplied prompt pathname is checked without reflecting the unsafe value, and each charged path is checked before diagnostics, manifest construction, or receipt emission.  These refusals use the same rc 7 hardening-contract path; printable non-ASCII prompt filenames remain outside this partial fix, while charged paths remain intentionally ASCII-only under the S1 bytewise policy.

# Unified diff

# Test inventory

<!-- BODY-END -->
