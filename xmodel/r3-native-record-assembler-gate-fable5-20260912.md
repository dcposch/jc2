# r3-native-record-assembler-gate-fable5-20260912 — FIRST of the native-record assembler and collector attachment

Fable 5.1, different-model hostile FIRST. STATIC/UNEXECUTED. First action
2026-09-12 17:52:24 UTC; reserve 18:06 UTC, hard 18:09 UTC, never reset.
Charged inputs: the seven snapshots in /tmp/jc2-lane.WPYW84/inputs, hashed
before any read; all seven matched the expected SHA256 (custody table below).
No source was executed, imported, compiled, AST- or syntax-checked; no
interpreter, CAS, network, git, process inspection, or uncharged file.

## 1. Grammar and metadata transformation

**CONFIRMED (conditional).** Every record form the charged template emits
on stdout is admitted by `parse`, and the parser's fixed skeleton matches
the template's emission order: NATIVE_START (date `%N` = 9 digits, literal
`UTC`), hostname / `readlink /proc/self/ns/pid` / boot_id (lines 1-3, must
equal the three facts strings), five package rows in any order (lines 4-8,
exact name set, `dpkg-query` never emits spaces inside a version), the three
PYTHON_PATH lines in the template's literal order (lines 9-11), body, one
COUNTS, one NATIVE_END. Body forms: `sha256sum` two-space line immediately
followed by `stat FILE %s %u %g %a %n` (adjacency enforced by `pending`,
path equality at field 5); `DIRECTORY %u %g %a %n` printed before its ENTRY
lines (parser requires the DIRECTORY first); ENTRY names are `LC_ALL=C`
sorted, which equals Python code-point order on the ASCII names both sides
enforce; ALIAS source is the unresolved path and target is `readlink -e`
output, so target is always subsequently a canonical FILE/DIRECTORY record
(or an earlier one); ABSENT only for the zip. Roles are disjoint because
FILE/DIRECTORY paths are always `readlink -e` canonical and ALIAS sources are
never canonical; the parser re-checks this. Both child-coverage directions
are checked: every ENTRY child in files|directories|aliases (line 159), and
every present path whose parent is a recorded directory appears in that
directory's ENTRY list (lines 160-162). The collector guarantees both for a
successful run: `find -mindepth 1 -maxdepth 1` lists every direct child, and
each child is either recorded or aborts the script under `set -e`
(dangling link, non-regular non-directory, bad name). COUNTS semantics
match: unique canonical files, unique canonical directories, unique alias
sources. Line ceilings are consistent with the count ceilings: an ALIAS line
is at most 6+4096+1+4096 = 8199 <= 8300 bytes, and 2·3000+1000+4000+
(entries <= 8000)+14 <= 20000. Python precedence makes
`permission & 0o111 == 0o111` mean `(permission & 0o111) == 0o111`, as
intended. The six-field full schema and the two-field subset are exactly the
bootstrap's expected keys (finding 3). `encode` is canonical (sorted keys,
ASCII, compact, trailing LF) at every nesting level, so the bootstrap's
re-encode equality holds byte-for-byte.

Qualifications (legitimate refusals, not mismatches, all host-dependent and
not inferred here): (a) a multi-arch co-install would make `dpkg-query` emit
six package rows and the assembler STOPs; (b) an `ldd` dependency reported
through a relative RUNPATH (`/usr/bin/../lib/x.so`) passes the collector's
lexical regex but `record_path` rejects `..`, so the assembler STOPs rather
than normalising, exactly as the contract states; (c) the 4000-alias bound
has no collector-side twin; (d) any `+` in a dependency name (libstdc++)
aborts the collector itself, so no raw exists. None of these is a defect.
The parser admits files that are root-owned and not group/world writable
but not world-readable (0600); the bootstrap's `regular()` later refuses
them (needs 0o004). That is downstream strictness, not a schema mismatch.
The template hash in COLLECTOR-DELTA equals the charged template; the claim
that only the root-vector line differs from collector b386a6cd is an
external assertion (old collector uncharged), and `collector_sha256` in the
facts is carried through as an assertion, never verified.

## 2. File output / consumption boundary

**CONFIRMED.** Order in `run`: argv shape (11, flags at odd positions) →
`local_path` on all three paths (lexical grammar, parent resolved
symlink-free, strict) → distinct triple and `not lexists(out)` (line 192,
before any read) → bounded reads with before/after fstat stability → pins
(line 194, before `json.loads` and `parse`) → facts canonical schema →
`parse` → four outputs formed and ceilinged → receipt formed, its own ceiling
and the 4 MiB whole ceiling → input re-read and byte-compared → `mkdir 0700`
→ five `write_new` in insertion order with the receipt last (O_WRONLY|
O_CREAT|O_EXCL|O_NOFOLLOW 0444, fchmod 0444, full write, flush, fsync, whole
readback with limit = exact length) → fsync OUT and OUT's parent → exact
inventory → input re-read again → status line. So all bytes exist before
OUT exists (contract line 57 holds), exactly five names, and the receipt
carries only input pins, the external collector assertion, four output pins
and byte counts; no self-hash and no authority string. A late failure at
line 235 or 236 (extra entry in OUT, or input drift) exits 2 with
ASSEMBLY_STOP after a complete, internally consistent receipt is on disk:
the contract's warning is exact, and a consumer must have terminal exit 0,
the exact positive status, and independently recomputed output pins.

Code-enforced: freshness of OUT, distinctness, non-symlink ancestry and
final-component O_NOFOLLOW, modes, readbacks, ceilings, inventory, input
stability. Caller contract only: exclusive ownership/no replacement during
the run (a FIFO or device at an input path would block or misbehave at
`os.open` before `S_ISREG` is tested; liveness is explicitly not claimed),
running as root (nothing here sets ownership), and placement. Placement is
however enforced downstream by the bootstrap: manifests are in
`r['pins']`, so a tmpfs location fails `all current static/native pins
outside tmpfs`; an OUT inside the science/wrapper directories or inside any
recorded native directory breaks the exact-inventory checks. One placement
fact the contract does not state: OUT is created 0700, and the bootstrap's
`directory()` demands `st_mode & 0o005 == 0o005` on every ancestor of a
consumed manifest, so the manifests cannot be consumed in place from OUT as
created. ROOT package binding must copy them (content pins are unchanged by
copying) or re-mode OUT; the receipt records neither. Not a defect of the
assembler; an unresolved qualification for the binding step. Optional
one-token repair, not selected and not implemented: `os.mkdir(out, 0o755)`
at line 222. Static byte ceilings bound the serialized outputs only; RSS and
duration are unmeasured.

## 3. Bootstrap native schema / pin / mode consumer

**CONFIRMED.** Scope is the consumer only. `audit_static` line 282 requires
exactly {schema, files, directories, aliases, absent, python_path} with
`f10-native-closure/v1`, `python_path == sys.path`, 0 < files <= 3000,
0 < directories <= 1000: identical to the assembler's `full` object and
ceilings (1 MiB read ceiling = assembler limit). Line 286 requires the subset
to be exactly {job_tag, files}, `job_tag` equal to the same literal
`f10-source-cone-r3-necessary-rows-v1` in both files, the registration's
python path present in it, and every subset digest equal to the full map
(64 KiB both sides). Directories are re-listed live and compared for exact
equality plus forward child closure; aliases are re-resolved with
`realpath`; absences re-tested with `lexists`. Two places the bootstrap is
stricter than the assembler, both fail-closed: `sys.path` closure excludes
aliases (a symlinked zip is assembler-present but bootstrap-refused), and
every native file must be world-readable, ACL-free, root-owned with a
traversable root-owned ancestry.

P-TOOLS trace. The bootstrap never names env or systemctl. They enter only
through `r['pins']` (INTAKE line 42), and line 307 evaluates
`regular(p, p in n['files'] or p in (python, setpriv))`: an ordinary 0755
tool passes only when its literal pinned path is a key of the full file map.
The charged template's root vector (line 68) appends `/usr/bin/env` and
`/usr/bin/systemctl`, so a successful run records them (and their `ldd`
closure) as FILE records; the assembler's `required` vector (line 165) is
the original seven and does not independently assert either path, exactly
as COLLECTOR-DELTA states. If either tool is itself a symlink it becomes an
ALIAS, the literal pin key is then absent from `files`, and the mode rule
refuses: whether they are canonical files is an external installed fact.
Hence P-TOOLS is supplied only jointly by an authenticated successful new
collection, ROOT binding that places the produced manifests where
`directory()` accepts them (finding 2), and the bootstrap's pin/mode checks.
Metadata syntax alone supplies nothing. Admin/transport/dlopen/mapped
closure/clock facts remain external; INTAKE and source comments are not
observed facts.

## 4. Manual source traces

Traces are read-only walks of the source; nothing was executed.

**Synthetic structural positive (syntax-only, UNQUALIFIED).** Facts:
hostname `synthetic-host`, `pid:[4026531836]`, boot_id
`00000000-0000-4000-8000-000000000000`, five versions `0.0-synthetic`,
any 64-hex collector assertion. Raw, 28 lines: START; the three header
strings; five package rows; three PYTHON_PATH rows; `ALIAS /usr/bin/python3
/usr/bin/python3.12`; `a`×64 SHA + `FILE 1 0 0 755 /usr/bin/python3.12`;
`b`×64 + `FILE 1 0 0 755 /usr/bin/setpriv`; `ALIAS /bin/ps /usr/bin/ps`;
`c`×64 + `FILE 1 0 0 755 /usr/bin/ps`; `DIRECTORY 0 0 755
/usr/lib/python3.12`; `ENTRY /usr/lib/python3.12 lib-dynload`; `DIRECTORY 0
0 755 /usr/lib/python3.12/lib-dynload`; `d`×64 + `FILE 1 0 0 644
/etc/ld.so.cache`; `ABSENT /usr/lib/python312.zip`; `COUNTS 4 2 2`; END one
second later. Every `need` has a literal witness: 4 files, 2 directories, 2
aliases, roles disjoint, the one ENTRY sorted, forward and reverse child
checks satisfied, both alias targets canonical files, all three Python
paths present or absent, all seven required paths present, both subset
paths canonical. This proves metadata syntax only, never a native closure.

**Semantic reverse-child negative.** Delete only the ENTRY line, keep both
DIRECTORY lines and `COUNTS 4 2 2`, recompute the raw SHA and pass it. Line
194 passes; line 152 passes (ENTRY lines are not counted); line 159 is
vacuous; line 162 fails for `/usr/lib/python3.12/lib-dynload`, whose parent
is recorded and whose name is no longer listed: `present direct child
missing ENTRY`, raised inside `parse` before line 222, no OUT. Rejection is
by the semantic check, not by a stale pin.

**Other negatives.** FILE path changed after its SHA line: line 127
`SHA/FILE adjacency or path mismatch`. `ALIAS /opt/zip
/usr/lib/python312.zip` with the zip ABSENT and `COUNTS 4 2 3`: roles are
disjoint (key is `/opt/zip`), rejection comes at line 163 `alias target not
canonical present path`. `COUNTS 5 2 2` only: line 152 `collector counts
mismatch`. Wrong `--raw-sha256` of correct shape: line 194 before parsing;
wrong shape: line 190 `digest shape`. Pre-existing OUT, including a dangling
symlink: line 192 before any read or write. Late failure: after five
successful `write_new` calls an extra entry in OUT (or input drift) fails
line 235/236; OUT then holds a complete receipt whose pins verify, exit is
2 with `ASSEMBLY_STOP_NO_QUALIFICATION`.

**Termination.** Before `main` handling: the flag guard raises SystemExit
at import (exit 1, no JSON line), and import errors escape. Inside `run`,
every `Exception` subclass, including OSError, KeyError, MemoryError and
RecursionError, yields the JSON stop line and exit 2; BaseException
subclasses and a failing `print` inside the handler escape. No universal
termination theorem: a FIFO at an input path blocks in `os.open`, and fsync
or read on a hung filesystem can block indefinitely.

## Verdict

CONDITIONAL ACCEPTANCE at static source-review tier. No blocking defect. The
one unstated interface fact is OUT's 0700 mode versus the bootstrap's
traversable-ancestry rule; ROOT binding must copy or re-mode before the
manifests can be consumed, and no assembler change is selected. Unresolved
qualifications: no collector execution, host freshness, native completeness,
alias-versus-file status of env/systemctl, package-row multiplicity,
RUNPATH-relative dependency paths, count ceilings on the real host,
runtime/RSS bounds, or the old-collector diff claim is established here.
No worker, enabled spec, execution, scientific outcome, retry, cap increase
or foundation re-review follows.

## Custody

Pre-read hashes 17:52:24Z and postpins 18:01:21Z, both from `sha256sum` on
the seven snapshots; every value equals the expected pin in the prompt.

| basename | sha256 (pre = post) |
|---|---|
| COORDINATION.md | 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597 |
| native_records.py | 44bd5d3b18d5552d811dd42071b8d54a6096e42f5ceac939e04cd1bd1ae70e0e |
| CONTRACT.md | b5876b7297d98c90c719c9d4901caa0e7e67503e375c3f7aca7d1e2d11206416 |
| native-metadata.template.sh | 601adf816495d9d4c7f72626b0d5ab170bf736b840a4a6d8f19c6e73ed5ca49c |
| COLLECTOR-DELTA.md | 410f993e50f17d54507d652dbcdb8591adf8300bfe6c6083cdc96999ec2c9bf2 |
| bootstrap.py | f04f1b7b16bed194e5d7b503a78fe9bd36e3bd58da3696adf6a40bfdbdcd17d2 |
| INTAKE.md | e401fd9f017196a8c711b2bf4198b1f0b8b2ff38c8246abe9d34d0c04e83068e |

Reads: COORDINATION.md whole first (three unclipped ranges after one
overflowed cat), then the other six whole. Writes: this file only, four
bounded apply_patch writes plus this custody append; no Write/Edit tool, no
shell redirection. Own whole readback at 18:01:21Z: 200 lines, 1845 words
including headings, sections in order, no marker before this append. Scope
check: no other file in xmodel/ was written by this lane (the .log and
.run.v2 beside this report are launcher-owned). No charge_basis is declared;
no exit price is asserted. No finalizer was run. ROOT owns TERM/KILL,
terminal-before-receipt custody and timer retirement.

<!-- BODY-END -->
