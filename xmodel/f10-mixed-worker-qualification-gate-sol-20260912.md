# DELTA FIRST: mixed worker qualification sources

Status: **CONDITIONAL SOURCE CONFIRMED / UNEXECUTED**. First action
`2026-09-12T20:38:55.513480233Z`. No worker, registration, authority,
collector result, native/import qualification, science run or mathematical
result exists from this review.

## Exact diff findings

The new dispatcher differs from the accepted native-envelope dispatcher in
exactly two command-vector lines. Each inserts `-E -s -S -B` between the
registered interpreter and CAPRUN script: once for every ordinary phase and
once for the dummy. CAPRUN's own `sys.argv` is unchanged: its script remains
argv0 and `--wall-seconds` remains argv1. The scientific `command` list is
byte-identical. Consequently authority `argv=command[5:]` still places
`ROOT_AUTHORITY_SHA256` at science argv slot6, and the caller still replaces
absolute `command[11]`; neither typed slot moved. The outer dispatcher itself
must separately be launched with exact flags, as CONTRACT states.

The collector diff has three operational changes plus one accurate comment:
file count `3000 -> 8192`; nominated roots add exactly
`/opt/jc2-mixed-20260912/{science,runtime,lib}`; and the comment now describes
its three `PYTHON_PATH` records as declared base paths rather than observed
complete sys.path. Recursion, canonical-name grammar, root ownership/mode
records, direct-child census, alias handling, per-file SHA, ELF identification/
ldd dependency recursion, physical-instance placeholder, timestamps, package
rows, directory/alias counts and other bounds are unchanged.

The assembler diff changes exactly: r3 job label to the mixed job; both file
count checks `3000 -> 8192`; required roots add env, systemctl and the three
deployment directories; the former two-binary job-tag subset becomes
`{"schema":"f10-mixed-native-files/v1","files":dict(files)}`; and that
projection's byte cap becomes 2MiB. Parsing, SHA/FILE adjacency, duplicate and
role-conflict refusal, ownership/mode checks, sorted complete direct-child
inventories, aliases/absences, input drift checks, O_EXCL publication/fsync,
raw/facts protocol, and all other limits are byte-identical.

## Interface and bounds

The complete projection is made from the same already validated `files`
dictionary as the six-field full map. It therefore matches the enlarged
authority's exact `f10-mixed-native-files/v1` schema and 2MiB/8,192-file
admission envelope; no separate asserted subset can substitute for it.
Collector and assembler share the 8,192 count. The three nominated deployment
roots exactly match CONTRACT's science/runtime/lib layout.

Bounds remain joint: raw4MiB/20,000 lines; full map1MiB; projection2MiB;
stats2MiB; hash list1MiB; total outputs4MiB; directories1,000; aliases4,000.
Thus not every 8,192-file inventory is promised to serialize or fit. Any
actual excess is STOP. Adding startup flags and metadata roots changes no
CAPRUN/science arguments, phase, scientific schema, authority logic, CPU,
wall, memory, tmpfs, FSIZE or per-file cap.

## Trust boundary and verdict

The retained `r3-*` fact/stats/receipt schema names are private administrative
labels only. They do not match or create a mixed registration/authority and do
not revive an r3 runtime. The collector remains disabled until ROOT binds its
fresh instance. Its syntax cannot prove its nominated roots are complete,
that lib contains exactly compatible full Sympy/mpmath packages, that pyc and
startup resolution are controlled, or that ldd output closes all dynamic
loading. The assembler's root-presence and all-files projection likewise do
not prove those physical facts.

**CONDITIONAL SOURCE CONFIRMED.** I find no blocking mismatch in this narrow
adaptation. Before any use, ROOT still needs separate bounded registration for
collection/assembly, actual-host raw/facts authentication, collector-source
binding, complete directories/aliases/absences/native backend and exact
sys.path/import/pyc qualification, immutable ancestry/no writers, installed
source pins, serialization fit, and all accepted cgroup/timer/cap/cleanup/
retirement predicates. Source review is not worker or science permission.

## Custody

Fresh WHOLE reads covered all fourteen pinned inputs listed in
`box/f10-mixed-worker-qualification-gate-sol-20260912/PINS.json`. Final WHOLE
readback covers PINS, report and manifest; strict postpins precede terminal
custody. No interpreter, import, AST, syntax, compile, test, dummy, CAS,
network, AWS, protected tree, repair or source edit occurred.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4537`.
- Body SHA-256:
  `37adade81bf131b6f382d0e5715cae1ba90081d60aeebf19fcffabc71bc04656`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
