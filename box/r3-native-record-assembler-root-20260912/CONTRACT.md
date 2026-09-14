# Raw native-record assembler — STATIC / UNEXECUTED / FIRST pending

This single pure-metadata program implements the transformation selected in
box/r3-bootstrap-preparation-root-20260912/NATIVE-METHOD.md. It does not
collect native data, inspect any path named in a raw record, import campaign
source, construct registration/approval, run a subprocess, or control a host.
It is not a generic registration generator or replacement launcher.

CLI, literal argument order:

    PYTHON -I -S -B native_records.py --raw RAW --raw-sha256 SHA --facts FACTS --facts-sha256 SHA --out OUT

Uppercase words are explanatory metavariables. No actual facts, approval,
enabled specimen, worker or runtime command is supplied. No invocation,
import, AST, compile, syntax check, fixture or scientific test has occurred.

## Inputs and external trust

ROOT first obtains independently terminal exit0/empty-stderr collector
evidence and freezes the raw bytes. ROOT supplies raw SHA and a separately
frozen canonical ASCII JSON+LF facts file with its SHA. Exact facts keys:
schema, collector_sha256, hostname, pid_namespace, boot_id, packages; schema
r3-native-expected-facts/v1. All leaves are strings; five package names are
the collector's exact list. Host, boot and namespace must match the separately
authenticated physical observation, not merely be copied from untrusted raw.
The supplied collector hash is explicitly an EXTERNAL ASSERTION. This
converter cannot prove that a collector ran or that those facts are fresh.

RAW <=4MiB and <=20000 ASCII/LF records; FACTS <=16KiB. No floats, numeric
facts literals, duplicates, noncanonical JSON, NUL or CR. Local inputs/output
use nominated canonical absolute paths, nonsymlink ancestry and final-file
O_NOFOLLOW. The caller guarantees exclusive stable ownership/no replacement;
this is not an adversarial-writer/security attestation. Raw-record paths use
PURE lexical checks only and are never resolved or opened on the coordinator.

The grammar follows the unchanged collectorb386a6cd and the selected portion
of recipe584f044f, not its old job/release steps. Header timestamps are parsed
and ordered to nanosecond-text precision; they are not monotonic qualification.
Five package rows may occur in any order but match exact expected names/versions.
The three declared Python paths must match the template order. The body has
only ALIAS, DIRECTORY, ENTRY, adjacent SHA256/FILE pairs and the one optional
ABSENT zip. COUNTS and NATIVE_END are unique final records.

Require root/root, no group/world writable bits and traversable directories;
unique/disjoint path roles; sorted unique direct children; every named child
present AND every declared present direct child listed; aliases targeting
canonical present files/directories; all collector roots and Python paths
present or the declared zip absent. At most3000 files/1000 directories and
the additional conservative4000-alias bound. Unexpected text, sizes, counts,
paths or versions cause STOP, not normalization. Full raw bytes remain the
external source of provenance; stat fields are separately retained as strings.
No ELF-dependency omission invisible to these records, ACL, actual sys.path,
mapped library or installed-native claim can be decided by this grammar alone.

## Outputs and consumption contract

All bytes are formed and checked BEFORE OUT is created. Exactly five files:

- native-manifest.json: EXACT six fields of f10-native-closure/v1, <=1MiB;
- source-native-manifest.json: EXACT job_tag/files, <=64KiB, CURRENT tag
  f10-source-cone-r3-necessary-rows-v1 and the same canonical Python/setpriv
  digests from the full map, not the retired direct-rows tag;
- native.sha256: every canonical file once, path-sorted, <=1MiB;
- native-stat-records.json: header/facts and all FILE/DIRECTORY stat strings,
  <=2MiB, separately from the runtime six-field schema;
- assembly-receipt.json: input pins, EXTERNAL collector assertion and four
  output pins/byte counts, <=32KiB, no self-hash or approval.

Total serialized output <=4MiB; these preparation files stay outside the
working tmpfs and exact science/wrapper/native directory inventories. This
does not change the runtime128MiB mount or8MiB metadata budget. All arithmetic
in this program is metadata sizing/counting, not scientific integer conversion.

OUT must be absent; mkdir0700 then each file is O_EXCL/O_NOFOLLOW-created,
fchmod0444, fsynced and whole-byte read back. Receipt is written last. OUT
and its parent are fsynced; exact inventory and unchanged raw/facts bytes are
checked. No overwrite, retry, removal, automatic cleanup or global transaction
claim. Failure after directory creation retains partial files; a late failure
can leave a complete-looking receipt. Therefore a consumer MUST independently
obtain terminal exit0, exact positive status, final receipt/output pins and
unchanged input/source pins before using the maps. A receipt alone is not
success. The only positive status is ASSEMBLED_METADATA_ONLY_UNQUALIFIED;
science_outcome is NONE. No authority string exists in any output.

Caller registration supplies a bounded administrative execution/custody method
and fresh paths. No duration, RSS or filesystem-liveness guarantee is proved
by byte ceilings. The first review is static; a separately capped future
metadata qualification is still required. This note authorizes no execution.

## Manual source controls, NOT executed

A minimal STRUCTURAL fixture can use two declared directories
/usr/lib/python3.12 and its listed child lib-dynload; four canonical file
records for Python3.12/setpriv/ps/ld.so.cache; aliases /usr/bin/python3 and
/bin/ps to their canonical files; the absent zip; and counts4/2/2. Match the
five arbitrary version strings and physical header to explicitly synthetic
facts, use well-formed distinct digest strings, chronological timestamps and
root0755/0644 stat fields. Every source grammar/closure condition then has a
literal witness. This is deliberately NOT a complete installed native closure
and cannot qualify a host; acceptance would demonstrate metadata syntax only.

With recomputed raw pin, delete ONLY the lib-dynload ENTRY while retaining
its DIRECTORY and counts. The reverse direct-child check rejects before OUT
creation; the initial one-way-only draft would not detect that inconsistency.
Changing FILE path after its SHA rejects adjacency; alias-to-absent rejects
target closure; changing only COUNTS rejects census; an existing OUT rejects
before writes. Wrong raw/facts pin rejects before parsing. These are source
traces, not actual tests or old-program executions. During ROOT readback the
draft was also tightened to reject double-leading-slash paths explicitly.

No scientific source, bootstrap, collector, launcher or earlier frozen file
was edited. Different-model actual-code FIRST is required before any use.
