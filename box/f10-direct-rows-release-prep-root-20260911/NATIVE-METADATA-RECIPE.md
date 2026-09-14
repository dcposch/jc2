# ROOT native and actual-registration composition recipe

Metadata only, no scientific/Python startup probe or source import. This
recipe preserves the accepted six-field closure and separate bounded subset.
The unchanged collector b386a6cd2d732e6618b994fdbdec67d8e2a59fc997206f296b4cf55513684ed0
is instantiated with only the exact returned instance ID, then run on that
worker under ROOT's setup cutoff. Physical collector separately supplies host,
boot, namespace, EBS device/FSTYPE, canonical binaries and absent paths.
Require terminal collector exit0, empty stderr and unchanged script/raw hashes.
No subsequent model or process can write this raw stdout during ingestion.

Read native.stdout in bounded complete metadata chunks with line/byte counts;
retain raw bytes/hash independently. Parse only its explicit record grammar:

- NATIVE_START/NATIVE_END timestamps, one each; exact fresh host/ns/boot and
  nominated package version in the fixed header. The five package rows name
  python3.12/python3.12-minimal/libpython3.12-stdlib/util-linux/procps.
- PYTHON_PATH path, exactly three in order: /usr/lib/python312.zip,
  /usr/lib/python3.12, /usr/lib/python3.12/lib-dynload. This is installation
  metadata only; actual sys.path must still be checked by the dispatcher.
- ALIAS absolute-path absolute-resolved-target: distinct endpoints, unique
  consistent alias. Target must occur in final files or directories.
- DIRECTORY uid gid octal-mode absolute-path: root/root, not group/world
  writable, traversable. Unique directory. Its ENTRY records form its exact
  sorted unique name array; every child resolves within files/dirs/aliases.
- ENTRY directory basename: directory already declared, safe ordinary name.
- SHA256 two-spaces canonical-path followed by FILE size uid gid mode path:
  matching unique path, root/root and not group/world writable; nonnegative
  metadata file size, digest literal64lowercasehex.
- ABSENT absolute-path: unique, not declared present/alias/directory.
- COUNTS filecount dircount aliascount: match all collected unique records,
  bounded1..3000 files/1..1000 dirs; no unparsed/extra body lines.

Retain stat metadata separately in the ROOT readback record; the exact runtime
native-manifest.json has ONLY schema/files/directories/aliases/absent/python_path.
Schema f10-native-closure/v1; files maps canonical paths to hashes; directories
maps directory paths to sorted unique direct-child arrays; aliases maps paths
to resolved targets. Serialize metadata with JSON+LF, <=1048576B.
The source-native-manifest.json has ONLY job_tag and files. Job tag is
f10-source-cone-r3-direct-rows-v1; files contains the matched /usr/bin/python3.12
and /usr/bin/setpriv hashes from the NEW full closure. It is intentionally not
a full closure, <=65536B, and matches the accepted prior two-entry recipe.
native.sha256 lists EVERY full-closure file hash and canonical path once.
No old raw native record or old hash is substituted for current evidence.

The qualified nominated Ubuntu amd64 binary is
a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223,
from package3.12.3-1ubuntu0.16. New physical/package/native data must match it
and the conditional source-derived refusal report cb6a98bc... . Package
correspondence and native closure trust remain explicit. A different package
or source/invocation layout is STOP for this release, not a calibration target.

Use the final disabled ROOT registration from the pinned previous packet.
Populate actual canonical Python/setpriv SHA, host/instance/boot/ns, EBS device
as a JSON integer, full/subset native SHA and preflight SHA. Four deadline
values are exact ISO UTC strings ending+00:00 from the original clock card.
Source hashes, reference vector, place and accepted command/phase policies
are unchanged. Enabled/exclusive become true ONLY with ROOT's final release.

Compute science authority preimages independently from the pinned dispatcher
authorize() metadata recipe/previous AUTHORITIES template, using new binary
and subset hashes. Compact recursively ASCII-key-sorted JSON+LF, then SHA256.
No scientific integers pass through JS numeric values; mathematical fields
are decimal strings. Fill exact literal digests for refuse-status/caps/
inventory/source and startup-produce/startup-check/produce. Refuse-hash stays
sixty-four zeros in argv (its true authority object remains unmutated).
Valid/dummy digests are already fixed; mutator policy points to frozen baseline
and is unused by its CLI. Checker authority digests remain the two explicitly
typed future AUTHORIZATION_SHA256 slots; mutator retains only its typed
ROOT_REGISTRATION_SHA256. Never substitute any other generic placeholder.

ROOT independently compares all13 literal CAPRUN vectors with dispatcher
run(), final source_files/source_pins/contract, source/helper authority fields
and flags/targets. Precompute policy/authority bytes outside outputs as
reference evidence only; the runtime authority/frozen/writer directories must
remain empty before launch. No self-hash in ROOT registration or helper policy.

Stage unchanged5science+3wrapper+CAPRUN, final ROOT registration/execution card,
source contract, preflight policy, full/subset manifests, raw native stdout and
native.sha256. Stage manifest lists all seventeen installed source/metadata
files by relative basename; installed.sha256 uses their final absolute paths.
Setup script pins BOTH manifests as prescribed, then root0444 installs and
mounts the fresh128MiB tmpfs; sources/wrappers are EXACT5/3 files. Stage script/
original clocks/allocation/physical evidence are additional retained inputs,
not inserted into exact source/wrapper sibling sets or the fresh authoritydir.

Before outer launch independently recheck all source/review/registration/
stage/installed/native pins, original deadlines and fresh-ABSENT cgroup; CPU
origin0 may then count from creation. Unchanged outer launcher arms original
TERM/KILL before starting dispatcher, then captures actual MainPID/Invocation/
namespace/PGID/cgroup and kernel limits within60seconds. This is the one
registered13-phase source observation, not a rank or source-zero computation.

No normalization of unexpected output, retries, producer-only smoke, AST/
syntax/import or interpreter calibration, capraise, optional hardening,
new supervisor, protected-infrastructure inspection or idle worker retention.
