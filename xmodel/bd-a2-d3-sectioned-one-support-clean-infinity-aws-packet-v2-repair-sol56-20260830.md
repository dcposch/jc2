# D3 one-support clean-infinity AWS packet: hardened v2 repair

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, coordinator repair lane  
Frozen basis: `2aa49d87c6a5d1823849fdc712582e064874bc8b`  
Lifecycle: **EXACT OPERATIONAL REPAIR / UNLAUNCHED AWS SCREEN**

## 0. Verdict

Replace the launch interface of the committed v1 one-support clean-infinity
packet with the hardened v2 scripts frozen below.  The mathematical jet ideal,
the modular-versus-exact interpretation, and the evidence files and verdict
states are unchanged.  The repair closes all five static-audit findings:

1. every non-self-test generator path now refuses execution unless it sees
   Linux, Amazon EC2 DMI, and a canonical nonempty coordinator route token;
2. lane tags and job roots have canonical slash-free and dot-free grammars,
   the root is derived from the tag, and one plain `mkdir` atomically acquires
   the exact root before either subdirectory is made;
3. the requested virtual-memory cap may not exceed exactly `85%` of live
   `/proc/meminfo:MemTotal`, in addition to the existing absolute bounds;
4. the runner accepts and checks both frozen script hashes and accepts the
   self-test only when stdout has the exact frozen SHA-256 and stderr is empty;
5. all hashes in this v2 artifact are printed as exact 64-hex strings, without
   the trailing punctuation that appeared inside three v1 code fences.

The sealed v1 report and manifest at commit
`6ea2a4fe92b379bcc7912bf8d0be9630d9e82ef9` remain byte-untouched.  No AWS
lane, full jet expansion, or Singular process was launched while producing
this repair.

## 1. Frozen v2 payload

```text
3e7ab2773c99667331f1e2767bf0b4f090c4c8ab0885a4da3ef28548c17a1d61
  ops/d3_one_support_clean_hb_generate.py
  bytes: 16473

24d5a118009bff9158873b59783961657f302697eb63bb83e3dfbcd2b87d9bbc
  ops/aws_d3_one_support_clean_hb_run.sh
  bytes: 12102
```

The generator has zero AST `Assert` nodes and thirty explicit `require()`
call sites.  The runner uses `set -euo pipefail`, retains the 120-second
self-test cap, two-hour generator cap, at-most-twelve-hour Singular cap,
`ulimit -v`, single-thread environment, internal control ideals, exact-one-
verdict validation, and the v1 evidence set:

```text
payload/aws_d3_one_support_clean_hb_run.sh
payload/d3_one_support_clean_hb_generate.py
run/run.meta
run/input.sing
run/generator.stderr
run/selftest.stdout
run/selftest.stderr
run/result.stdout
run/singular.stderr
run/lanes.log
EVIDENCE.sha256
```

The metadata schema is now `D3_ONE_SUPPORT_CLEAN_HB_AWS_RUN_V2`.  It adds
expected and observed runner/generator hashes, the exact expected self-test
hash, route-token hash, `MemTotal`, the `85` percent bound, and the resulting
maximum permitted memory cap.  The final states and their mathematical prices
are unchanged:

```text
FAILED_CLOSED_SELFTEST
FAILED_CLOSED_GENERATOR
FAILED_CLOSED_OR_INCONCLUSIVE
MODULAR_SCREEN_UNIT
MODULAR_SCREEN_NONUNIT
EXACT_SCREEN_UNIT_CERTIFICATE_REQUIRED
EXACT_SCREEN_NONUNIT
```

In particular no runner marker is promoted to a characteristic-zero emptiness
theorem without a separately serialized and independently replayed exact
certificate.

## 2. Generator route firewall

`--self-test` branches before the route check.  It remains the only licensed
local execution mode and never performs the interior jet expansion.

Every other path calls `require_aws_route()` before the primality loop or any
jet construction.  It requires all of

```text
sys.platform starts with "linux";
/sys/class/dmi/id/sys_vendor is exactly "Amazon EC2";
environment D3_ONE_SUPPORT_CLEAN_HB_ROUTE_TOKEN matches
  ^d3_clean_hb_[A-Za-z0-9][A-Za-z0-9_-]{0,95}$
```

The route token is an accidental-execution capability, not a secret or an
authentication boundary.  The v2 runner sets it to the already canonical
coordinator lane tag only for the full generator subprocess and unsets it
immediately afterward.  A direct full generator call on the local Mac fails
even if a syntactically valid token is supplied, because the Linux check is
first.  A direct full generator call on an arbitrary Linux host still fails
unless Amazon EC2 DMI is present.

## 3. Canonical and atomic job custody

The accepted lane grammar is

```text
^d3_clean_hb_[A-Za-z0-9][A-Za-z0-9_-]{0,95}$
```

Dots, slashes, whitespace, empty suffixes, and traversal spellings are
impossible.  If the suffix after `d3_clean_hb_` is `TAG`, the only accepted
root is the literal string

```text
/home/ubuntu/jobs/d3_one_support_clean_hb_TAG
```

After Linux, exact EC2 instance, memory, both payload hashes, required tools,
and SymPy import have passed, the runner sets `umask 077` and executes

```text
mkdir -- "$D3_JOB_ROOT"
```

without an earlier existence test and without `-p`.  Kernel directory-entry
creation is therefore the lease: an existing path, a symlink, or a simultaneous
second launch loses atomically and exits `125`.  Only the winner then creates
the `payload` and `run` subdirectories.

## 4. Memory and hash gates

The existing absolute interval remains

```text
4194304 <= MEMORY_KIB <= 1000000000
```

On the exact EC2 host, v2 parses live `MemTotal` and additionally requires

```text
MEMORY_KIB <= floor(85*MemTotal_KiB/100).               (4.1)
```

Thus at least fifteen percent of reported physical RAM is outside the
per-lane virtual-address cap.  The same value is then installed with
`ulimit -v`.  A cap copied from a larger node is rejected before job-root
creation.  Recommended nominal single-lane caps are `110000000` KiB on each
128-GiB `r6a/r6b/r6c`, `220000000` KiB on 256-GiB `r6d`, and `440000000`
KiB on 512-GiB Box03.  The live check is binding; if a host reports less RAM,
lower the cap rather than weakening (4.1).

The ninth and tenth runner arguments are now, in order,

```text
EXPECTED_RUNNER_SHA256 EXPECTED_GENERATOR_SHA256
```

Both must be 64 lowercase hex digits and equal the staged files before root
creation.  The copied runner is hashed once more inside the acquired root.
The self-test is accepted only if

```text
exit code = 0,
SHA256(selftest.stdout)
  = fc80bb406ce8755af035adf86bd7100e14c74f541db27764aaa924ef01412061
selftest.stderr is empty
```

A schema substring is no longer sufficient.

## 5. Exact v2 runner CLI

```text
bash aws_d3_one_support_clean_hb_run.sh \
  JOB_ROOT \
  LANE_TAG \
  EXPECTED_INSTANCE_ID \
  PRIME \
  JET_ORDER \
  ENGINE \
  MEMORY_KIB \
  TIMEOUT_SECONDS \
  EXPECTED_RUNNER_SHA256 \
  EXPECTED_GENERATOR_SHA256
```

For the first `r6a` lane, after resolving its current IP, auditing live
processes, copying both files into a fresh stage directory, and independently
reproducing both hashes, the exact positional form is

```bash
nohup bash aws_d3_one_support_clean_hb_run.sh \
  /home/ubuntu/jobs/d3_one_support_clean_hb_p32003_n8_20260830_v2 \
  d3_clean_hb_p32003_n8_20260830_v2 \
  i-02cb2b4a379ffcc64 \
  32003 8 slimgb 110000000 21600 \
  24d5a118009bff9158873b59783961657f302697eb63bb83e3dfbcd2b87d9bbc \
  3e7ab2773c99667331f1e2767bf0b4f090c4c8ab0885a4da3ef28548c17a1d61 \
  > launch.stdout 2> launch.stderr &
```

Every lane still requires a distinct stage directory, root, and tag.  The
recommended launch order remains one memory-heavy lane per node:

1. `r6a/r6b/r6c`: `N=8` at `p=32003,32009,32027`, respectively;
2. surviving modular nonunit primes: sequential `N=12`, then `N=16` on the
   same nodes;
3. `r6d`: one `N=20` modular lane, then an exact lane at the lowest still-live
   useful prefix;
4. Box03 only if needed: sequential `N=24`, `N=27`, modular before exact.

Timeout, OOM, failed marker, or nonzero Singular exit remains inconclusive.
No two nominal full-memory caps may be stacked on one node.

## 6. Bounded desk replay

The repair was tested without a full generator path, Singular, or AWS.

```text
python3 -m py_compile generator                    PASS
bash -n runner                                     PASS

self-test ordinary / -O / -OO                     exit 0
self-test stdout bytes                             543 each
self-test stdout SHA-256                           
fc80bb406ce8755af035adf86bd7100e14c74f541db27764aaa924ef01412061
self-test stderr SHA-256
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

mutation ordinary / -O / -OO                      exit 1
mutation stdout bytes                              0 each
mutation stderr SHA-256
415e271805890a904f6f9cf84ec0afd7862a2b417a15ffa8725e02d89d7e76be

full generator locally, token absent               exit 1
full generator locally, canonical token supplied  exit 1
both stdout bytes                                  0
both stderr SHA-256
ca93c841c473a9c623114dbfd1f71d3d3d4cc4824b1f3b811137b4376cb82906

v2 runner locally with otherwise valid arguments  exit 125
runner stdout bytes                                0
runner stderr SHA-256
0022ea2e819d5cce6f8bb655aad7d62bde344e1f0238af4b8c280a55ea38f6c4

job root containing /../                           exit 125 before route check
path-refusal stderr SHA-256
9705cafca8dfe5cadaac7a9bf5e31c54663ccad3572394928ec4773d176f4553

lane tag containing ..                             exit 125 before route check
tag-refusal stderr SHA-256
5775d644dd70e95686eb3aa1e4ae375b9623632c8a5d7ecb0d9ed3f3f58b623a
```

The local full-generator error is exactly

```text
D3_ONE_SUPPORT_CLEAN_HB_ERROR: heavy generation requires Linux on AWS
```

and the runner error is exactly

```text
refusing heavy lane outside Linux
```

These refusal paths occur before any jet construction, Singular invocation,
or job-root allocation.  The EC2-only positive path, atomic root acquisition,
and live-memory rejection were statically audited but not executed locally or
remotely; their first real use remains screening-tier until its evidence bundle
is returned and reviewed.

## 7. Scope

This v2 packet is an operational hardening of the exact same normalized
`U_Z!=0` P18 clean-infinity screen.  It adds no mathematical exclusion and
does not widen the shard.  The complementary `U_Z=0` locus, other CFS charts,
degenerate infinity rows, the primitive horn, polynomial-map existence, and
JC2 remain outside its scope.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10145`.
- Body SHA-256:
  `cfb158cc543c7c63a8c48ae083629aa76f9feb357ad393ef6091320d98863072`.
- Frozen basis: `2aa49d87c6a5d1823849fdc712582e064874bc8b`.
