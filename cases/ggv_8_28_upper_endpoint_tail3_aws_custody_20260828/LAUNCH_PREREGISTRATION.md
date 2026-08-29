# Cutoff-three AWS launch preregistration

Date: 2026-08-28

Status: **HOLD — no Singular launch without coordinator clearance**

## Frozen source

The authoritative source archive is
`GGV_8_28_TAIL3_SOURCE_R0_20260828T043008Z.tar.gz` (10,195,122 bytes),
SHA-256
`b2dfa8805a7e2f7c45db18104fed19fae015624751e1cf905219ad9b312faea9`.
It contains the exact sixteen-file cutoff-three case plus only the two
external raw inputs named by `SOURCE.sha256`.  Its 21 tar members are those
18 files and three directory entries; no AppleDouble member is present.

The inner immutable hashes are:

* `SOURCE.sha256`: `f3f451a3c6e7b850deed3a481378155c4d4ad444872463fc04ecc7dcb1dee5a8`
* `EVIDENCE.sha256`: `cba8c71dcec44ca4c442b214b884c216f4a1c6cbafd17db415cd82c79ff4c669`
* target JSON: `619cae5ca7db7e3dadb49e76c941b0eb644982afcd004dce3a3d1c897ad64023`
* analyzer: `d824d5e1e2f17d7e36e275710351e55f8503a231c0e7dda8f64a3b476877b32e`
* literal branch-P raw system: `ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0`

The registered remote immutable source root is
`/home/ubuntu/jobs/ggv_8_28_tail3_source_r0_20260828T043008Z`.
Extraction must fail closed if that path already exists.  After replay, its
`cases` tree is made read-only; run output is written only to a separate
fresh run root.

## First launch, held

The first lane is modular reconnaissance of the necessary `core` subsystem
on all six projective nonzero-`V` localization charts.  It is heuristic
only.  No modular unit, nonunit, timeout, or killed process is promotable.

Host: r6d, instance `i-07eeaf8ba6f0bc419`, public `100.26.198.153`.

Frozen run root:
`/home/ubuntu/jobs/ggv_8_28_tail3_core_mod_r6d_r1_20260828T043008Z`.

Runner charge:

```text
mode=mod scope=core charts=all
six workers, 40 GiB virtual-memory cap per worker
6 GiB transcript cap per worker
21,600 s per-job and global wall cap
150 GiB live MemAvailable floor
50 GiB live free-disk floor
zero configured/used swap
30 s resource telemetry
```

The runner is source/host/chart pinned and uses isolated, recorded process
groups.  Its guard and explicit stop path validate the namespace before
TERM and KILL.  Every output is retained and hashed; no old namespace is
modified or deleted.

Immediately before launch, recheck: no authoritative result already exists,
the source archive and both inner manifests replay, instance ID and Singular
binary match, no heavy user process is present, MemAvailable is at least
390 GiB, free disk is at least 86 GiB, and swap remains zero.

The immutable archive was transferred to the registered source root and
replayed there without CAS.  At `2026-08-28T04:34:51Z`, all six remote
modular dry renders were byte-identical to the independent local renders;
the ordered-pair rejection controls returned `2,2,2`; and the source tree
was made read-only.  The full remote preflight subsequently passed with:

```text
INSTANCE_ID=i-07eeaf8ba6f0bc419
SINGULAR_SHA256=90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4
MEM_AVAILABLE_KIB=513793044
DISK_AVAILABLE_BYTES=118946856960
SWAP_TOTAL_KIB=0
SWAP_USED_KIB=0
```

Its custody hashes are:

* `PREFLIGHT_R6D.txt`: `664d13736b9773c901067072257a47d2f10d6e8192b2072ca60d76b9599a2b05`
* `DRY_RENDER_R6D.sha256`: `bbbec42c27baac6fc58aa4bfbb0986cbf88bc9efbbb9769750badc55a78919b3`
* `NEGATIVE_PIN_TEST_R6D.txt`: `c7fc3fd9db15ec1860186dd5721a35ea8c8df226a4e7c4d8474c6b7300ba5866`

After an immediate coordinator terminal-result recheck and explicit launch
clearance, the exact registered remote command is:

```bash
ssh -i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes \
  -o ConnectTimeout=10 ubuntu@100.26.198.153 '
set -euo pipefail
source_root=/home/ubuntu/jobs/ggv_8_28_tail3_source_r0_20260828T043008Z
case_dir=$source_root/cases/ggv_8_28_upper_endpoint_tail3_desk_20260828
launch_root=/home/ubuntu/jobs/ggv_8_28_tail3_core_mod_r6d_r1_20260828T043008Z
archive=$source_root/GGV_8_28_TAIL3_SOURCE_R0_20260828T043008Z.tar.gz
expected_archive=b2dfa8805a7e2f7c45db18104fed19fae015624751e1cf905219ad9b312faea9
[[ ! -e "$launch_root" ]]
[[ "$(sha256sum "$archive" | awk "{print \$1}")" == "$expected_archive" ]]
if find "$source_root/cases" -type f -perm -u=w -print | grep .; then
  echo "STOP: immutable source tree became writable" >&2
  exit 41
fi
install -d -m 700 "$launch_root"
sha256sum "$archive" "$case_dir/SOURCE.sha256" \
  "$case_dir/EVIDENCE.sha256" \
  "$case_dir/TARGETS/tail3_v_nonzero_d22_target.json" \
  | tee "$launch_root/START_HASHES.sha256"
nohup setsid env TAIL3_RUN_ROOT="$launch_root/runs" \
  bash "$case_dir/TARGETS/run_aws.sh" \
    mod core cutoff3_core_mod_r6d_r1 all \
  >"$launch_root/launcher.stdout" \
  2>"$launch_root/launcher.stderr" </dev/null &
launcher_pid=$!
printf "%s\n" "$launcher_pid" | tee "$launch_root/launcher.pid"
kill -0 "$launcher_pid"
echo "LAUNCH_ROOT=$launch_root"
echo "LAUNCHER_PID=$launcher_pid"
'
```

The runner repeats the analyzer, both manifests, host/Singular identity,
memory, disk, swap, and no-heavy-process gates before it invokes Singular.
If any gate changes, the fresh namespace remains fail-closed evidence and
must not be reused.

## Exact successor, not yet launched

If modular reconnaissance identifies unit charts, exact-Q replay remains
mandatory for every chart used in a closure.  The frozen distributed split
is r6a charts `0,1`, r6c charts `2,3`, and r6d charts `4,5`.  Each host uses
two 120-GiB workers for at most 43,200 s, the same 150-GiB memory and
50-GiB disk floors, exact `liftstd` cofactors, in-CAS
`CERTIFICATE_CHECK=PASS`, per-pair validation, and a combined validator
requiring the disjoint union `{0,1,2,3,4,5}` with identical source and target
hashes.
