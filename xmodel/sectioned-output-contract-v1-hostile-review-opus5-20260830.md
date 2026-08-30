# Hostile review — `SECTIONED-INDEPENDENT-CALLS/v1` (`ops/sectioned_output.py`)

Reviewer: Opus 5, adversarial. Date: 2026-08-30.

## Custody

Frozen basis `0f7ee003be45ee40d51d4048897cdacf63821172` (`git rev-parse HEAD`
confirmed). Both charged files recomputed before use and again after all work;
byte-identical at both ends, and `git status --porcelain ops/` shows exactly the
two untracked charged files and nothing else:

```text
593bc16465eac0b1146b08b724226cea3b449178090d974dbdfb0357d40f5473  ops/sectioned_output.py
b8e311fe915b2589ab13307840bed4b3e2864d6d13fe1976b65db8f9c9bb30a1  ops/test_sectioned_output.py
```

Neither charged file was edited. All reviewer artifacts live under
`/tmp/soreview/`. No commit, push, network, or AWS use.

## Verdict

**`REPAIR_REQUIRED`**

Two defects each contradict a property the tool states about itself, and both
are cheap to fix. **R1** is a genuine *fail-open*: on one class of error the
`assemble` path leaves an unverified artifact on disk with no receipt. **R2**
defeats the assembled artifact's defining invariant — a single terminator — by
allowing a section body to smuggle a second one. The tool is not yet wired into
any caller, so there is no cost to repairing before first use.

Everything else is strong. Path confinement, output exclusivity, truncation
semantics, and determinism all survived hostile probing without a single
finding, and 5 of 6 in-window mutations fail closed with precise diagnoses.

## Corrections (complete enumeration)

### R1 — fail-open on non-`FileNotFoundError` `OSError` (must fix)

`regular_file` (`ops/sectioned_output.py:69`) guards `path.lstat()` with
`except FileNotFoundError` only. `EACCES`, `ENOTDIR`, `ELOOP`, `EIO` propagate
as bare `OSError`. On the `assemble` path this escapes the
`except ContractError` handler at `:314` — the handler that unlinks the output —
so the output survives.

Demonstrated in-process by patching only my own copy of `write_exclusive` to run
a sabotage callback inside the real post-write verification window:

```text
body swapped (valid->valid)   rc=2  OUTPUT_LEFT_ON_DISK=False
section deleted               rc=2  OUTPUT_LEFT_ON_DISK=False
section made malformed        rc=2  OUTPUT_LEFT_ON_DISK=False
manifest swapped              rc=2  OUTPUT_LEFT_ON_DISK=False
section -> symlink            rc=2  OUTPUT_LEFT_ON_DISK=False
parts/ made unreadable        rc=None  uncaught=PermissionError  OUTPUT_LEFT_ON_DISK=True
```

The last row is the defect: exit 1, raw traceback, no receipt on stdout, and
`assembled.md` left on disk **whose inputs were never re-verified**. A consumer
that keys off file existence rather than exit code consumes an unvalidated
artifact.

Fix: in `regular_file`, `except OSError as exc: raise ContractError(...)`; and
broaden `:314` to `except (ContractError, OSError)` as defence in depth.

### R2 — terminator and marker smuggling into the assembled artifact (must fix)

The guard at `:188` is `any(line == "<!-- BODY-END -->" for line in text.splitlines())`.
That rejects a body line only when the terminator is byte-exact *and* preceded
by something Python's `str.splitlines()` treats as a line boundary. Separator
matrix, prefix character before the terminator:

```text
space U+0020   SMUGGLED (2 occurrences in output)    VT U+000B    refused
tab   U+0009   SMUGGLED (2 occurrences in output)    FF U+000C    refused
NBSP  U+00A0   SMUGGLED (2 occurrences in output)    FS U+001C    refused
any non-separator prefix (e.g. "x")  SMUGGLED        NEL U+0085   refused
                                                     LS/PS U+2028/9, LF  refused
```

Concretely, a section body line ` <!-- BODY-END -->` (one leading space) yields
this assembled artifact:

```text
line  8: ' <!-- BODY-END -->'      <- smuggled; standalone after .strip()
line 12: '<!-- BODY-END -->'       <- the real terminator
```

Any consumer that does `line.strip() == terminator` — the natural
implementation — truncates the report at line 8 and silently drops everything
after it. The guard tests "is some Unicode-split line byte-equal to the
terminator", which is strictly weaker than the property the artifact needs.

Two siblings of the same root cause, both confirmed:

- The section-marker filter at `:183` uses `line.startswith(...)`, so a
  leading-space or mid-line `SECTION-END` marker in a body is invisible to the
  count check and lands verbatim in the output.
- A body may forge an extra `<!-- SECTION <id> sha256=<64 hex> -->` line — the
  exact provenance form the assembler itself emits at `:252`. Confirmed: output
  contained two provenance-looking lines, one entirely attacker-authored with a
  bogus digest.

Root cause: the assembler's marker vocabulary is not reserved against section
bodies; only two byte-exact line forms are rejected. Fix: reject any body
containing the substrings `BODY-END`, `SECTION-END`, or `<!-- SECTION ` — the
cheapest repair and the one that matches the stated fail-closed posture.

### R3 — `write_exclusive` catches only `FileExistsError`

`:263` lets `PermissionError`, `EROFS`, `ENOSPC` escape `os.open`. Confirmed
with a `0555` output directory: exit 1 plus traceback. Not fail-open — nothing
is created — but off the documented 0/2/4 contract.

### R4 — `path` is the only unvalidated manifest string

`id`, `tag`, `basis`, and `prompt_sha256` all carry regexes; `path` carries
none. A `path` containing NUL passes `safe_relative`, then `Path.exists()` and
`Path.is_symlink()` swallow the resulting `ValueError` and return `False`.
Confirmed: `rc=4`, `completed: []`, `next_section: one`. The section is reported
as *not yet produced* rather than as malformed, so the runner is instructed to
regenerate, forever, a section it can never satisfy. A liveness defect, not a
safety one. Fix: reject control characters in `path` at load time.

### R5 — "canonical" is claimed but not checked

`:122` reports "manifest is not canonical UTF-8 JSON", but no canonicality test
exists. `json.loads` accepts duplicate keys, last-wins. Confirmed: a manifest
carrying two `"sections"` keys is **accepted**, and the first — the one a human
reviewer reads at the top of the file — is silently discarded in favour of the
second. The manifest digest pins the bytes, so this cannot change behaviour
undetected across runs; it can mislead a reader auditing the manifest. Fix: an
`object_pairs_hook` that rejects duplicate keys, or drop the word "canonical".

### R6 — `prompt_sha256` is decorative

Registered, regex-checked, echoed into the receipt at `:222`, and never compared
to anything. Confirmed: setting it to 64 `f`s changes nothing and the value is
reproduced verbatim in the receipt. The docstring's "The manifest pre-registers
their order, prompt hashes, and byte budgets" reads as though all three are
enforced; order and budgets are, prompt hashes are not. A receipt consumer could
reasonably mistake the echoed digest for a verified binding. Fix: verify against
an on-disk prompt file, or rename to `prompt_sha256_declared` and state in the
docstring that it is an unverified operator annotation.

### R7 — `lstat`→`read` TOCTOU (demonstrated, low severity)

`regular_file` lstats the path, then re-opens it by path via `read_bytes()` with
no `O_NOFOLLOW`. I did not merely assert this window; I won it. Against a
maximally adversarial thread renaming a regular file and a symlink alternately
onto the target:

```text
attempts=1861153  lstat-said-regular-but-read-through-symlink=1
refused-as-symlink=1774556  benign=86596  errors=0
```

One hit in 1.86M attempts (0.0001%). Real, exploitable in principle, negligible
in the intended single-operator local-disk model, and material on shared or
networked storage. Fix: `os.open(path, os.O_RDONLY | os.O_NOFOLLOW)` + `os.fstat`
+ read from the fd, which closes the window outright.

### R8 — immutability overclaim

`:5` describes "one immutable output file per section". Nothing enforces
immutability; the tool detects change only between its own two reads inside a
single `assemble`. The accurate claim is: *changes are detected across the
assembly window*. Separately, the docstring describes a split into
`ops/lane.sh` calls, but `ops/lane.sh` contains no sectioning support and no
file in the repo references `sectioned_output` — the described integration does
not exist yet.

### R9 — documentation minors

Exit codes 0/2/4 are pinned only by the tests, absent from `--help` and the
docstring; exit 1 is undocumented and reachable via R1/R3. `max_bytes` budgets
the marker line as well, so usable body is `max_bytes - len(marker) - 1` (e.g.
14 bytes at `max_bytes=40`); undocumented. The test file's contract label
`SECTIONED-OUTPUT-CONTRACT/v1` differs from the round label
`SECTIONED-INDEPENDENT-CALLS/v1`.

## What holds (verified, no findings)

**Test execution.** Charged tests 5/5 under Python 3.12.14 ordinary, `-O`, and
`-OO`, and under system Python 3.9.6. Full `ops` suite 43/43. The tool contains
no `assert` statements, so `-O` is behaviourally inert by construction as well
as by observation.

**Path confinement — 13 controls, all correct.** Refused: `..` escape, absolute
path, mid-path `..`, `..` in `output`, absolute `output`, `output` equal to a
section path, symlinked intermediate directory, symlinked parent resolving to
`/etc`, symlinked manifest, symlinked `--root`. Accepted and correctly
normalised to one identity: `./p/x`, `p//x`, `p/x/`. Alias-based duplicate
section paths (`parts/one.md` vs `./parts/one.md`) are caught.

**File-type discrimination.** Directory, FIFO, and symlink-to-`/dev/null` as a
section are all refused as "regular non-symlink file".

**Manifest schema — ~40 controls.** Correctly refused: wrong/`str` schema, extra
and missing keys, non-object root, truncated JSON, BOM, 0 or 17 sections,
duplicate ids, duplicate paths, `max_bytes` as `NaN`/float/bool/0/1000001,
uppercase or short `basis`, uppercase or short `prompt_sha256`, ids with
newlines or over 64 chars, tags with slashes or shell metacharacters, section as
a list, empty or null `output`. Boundary correct: `max_bytes` exactly at the
limit passes, `+1` fails.

**Truncation semantics and partial usefulness.** Clean monotone progression;
the mid-run receipt is genuinely actionable:

```text
0 sections: rc=4  MISSING_BEFORE_FIRST_SECTION      next=one    done=[]
1 section : rc=4  TRUNCATED_AFTER_SECTION_one       next=two    done=[one]
2 sections: rc=4  TRUNCATED_AFTER_SECTION_two       next=three  done=[one,two]
3 sections: rc=0  COMPLETE                          next=None   done=[one,two,three]
```

`status` is read-only (tree hash unchanged across ordinary and `-O` runs).
`assemble` on an incomplete set emits the receipt, returns 4, and writes
nothing.

**Noncontiguity fails closed**, including the awkward case where the
out-of-order section is *also* malformed — the structural error wins and no
partial assembly occurs.

**Exclusive output.** Second `assemble` refused, first artifact byte-unchanged.
Dangling-symlink output refused **without creating the link target** (`O_EXCL`
semantics correct). Directory-as-output refused. Simulated `ENOSPC` at `fsync`
leaves no partial file — the `except BaseException` cleanup at `:271` works.

**Determinism.** Across 5 runs varying temp root, interpreter (3.9 vs 3.12),
`-O`, and `PYTHONHASHSEED` (0/99/777/12345/31337): **1** distinct
`output_sha256` and **1** distinct receipt. No timestamps, no set-iteration
leakage. Assembly order derives from the manifest, not the filesystem —
confirmed by writing sections in reverse order and observing `[one, two, three]`.

**Encoding and marker rigour.** Refused: invalid UTF-8 body, CRLF section file,
marker without trailing newline, empty file, marker-only file, whitespace-only
body, duplicate marker line, marker naming a different section id. Prefix-
colliding ids (`one`/`onetwo`) handled correctly.

**No live-provider overclaim.** The docstring's "deliberately not a model
runner" is accurate: there is zero provider, network, or credential code. This
is the one self-description that is exactly right.

## Mutation and negative-control ledger

Ten independent families, well past the required five: path confinement (13),
manifest schema (≈40), marker/terminator smuggling (10 + 6), post-write
verification window (6), separator classes (10), TOCTOU race (1.86M attempts),
determinism (5 runs), file types (3), size and newline boundaries (5), empty-run
and read-only checks (3).

## Maximum safe lifecycle

- **As it stands, unrepaired:** `status` only, as an advisory progress reporter,
  single trusted operator, local disk, one writer. Any `assembled.md` produced
  by `assemble` must be treated as **unverified** until R1 is fixed, because the
  artifact's presence on disk does not imply it passed verification.
- **After R1 + R2 + R3 + R4:** usable as an assembly gate for review artifacts
  under a single operator on local disk. R5, R6, R8, R9 are documentation-
  accuracy repairs and should land with it so the receipt is not over-read.
- **After R7 additionally:** tolerable on shared or networked filesystems.
- **Never:** this is an opt-in assembly and validation tool. It is not a model
  runner, not an authentication layer, not a semantic checker, and not a proof.
  It validates byte-level shape, size, order, and stability across one window —
  nothing about the truth, provenance, or mathematical content of any section.
  **No mathematical claim may depend on it**, and a green `ASSEMBLED` receipt is
  not evidence for any statement inside the assembled text.
- Re-review required before wiring into `ops/lane.sh` or any promotion path;
  the described integration does not exist today (R8).

No exit price is asserted, so no `charge_basis` line is declared.

## Execution notes and disclosed gaps

- **`jc2-lean` traversal.** One wiring check used a repository-wide
  `grep -rn --include=...` rooted at `.`, which would have traversed a
  `jc2-lean` working tree if one is present. This was inadvertent and contrary
  to the brief's exclusion. Mitigation and impact: the command returned exactly
  two matches, both in `xmodel/`, and no `jc2-lean` path appeared in the output
  or informed any finding in this report. No other command in this session
  referenced, listed, stated, built, or modified `jc2-lean`.
- The R1 and the `fsync`-failure demonstrations required running `main()` in
  process with a reviewer-owned patch applied to my own imported module object.
  The charged file on disk was never modified; hashes above are re-verified
  post-hoc. The patch wraps the real `write_exclusive` and calls it unchanged,
  so the tool's own write and verification logic executed as written.
- The R7 race was won once and is reported with its exact denominator rather
  than characterised as "theoretical" or as "readily exploitable". It is neither.
- Not attempted: behaviour on filesystems other than APFS; concurrent
  multi-process `assemble` contention beyond the `O_EXCL` single-shot check;
  fuzzing beyond the structured mutation families listed above.

<!-- BODY-END -->
