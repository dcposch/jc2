# Box02 amendment: immediate exact 466-generator top rung

Date: 2026-08-27

This amendment changes only the timing and audited execution host of the
reviewed-prefix exact quotient in `PREFIX_QUOTIENT_PREREGISTRATION.md`.
Coordinator direction based on the user's speed priority licenses preparing
the top rung before the current Box03 lanes terminate, while the 512-vCPU
campaign ceiling prohibits creating another instance.  No computation is
authorized by this file alone: `launch_box02_prefix.sh` remains held until an
explicit coordinator approval and a terminal recheck.

The mathematical object and evidence threshold are unchanged.  The
authoritative literal object is the 303-variable, 513-generator system with
SHA-256
`ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0`.
The ideal-equal acceleration retains 466 original generators; its system has
SHA-256
`8e25502c5f8e7b7397d1799f0502fc3088fd0cb8d3425b832b31aa3cd902b611`
and its exact-`Q` Singular input has SHA-256
`afd9565d128417924cb74c46a306bf8d72136a51e2e4f13f695d859eea9837fa`.
All 47 omitted-generator cofactor identities must replay before Singular is
called.  The endpoint-transfer identity is not used.

## Audited host and immutable lane

The only additional host licensed by this amendment is existing Box02:

```text
AWS profile/region: personal / us-east-1
instance:           i-010201a5da47795c4
DMI hostname:       ip-172-30-0-186
instance type:      x2idn.32xlarge (128 vCPU, 2 TiB)
AMI:                ami-052355af2a014bd2c
subnet:             subnet-948915c9
security group:     sg-09ffa8932558f0a79
key fingerprint:    8mg4kK7KYNflkiETs3z8e5H2/w8O0lxHbnuX23ojlfU
Singular binary:    90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4
```

The fixed lane is `exact_prefix_quotient`, one core, `134217728` KiB virtual
memory, and one global `7200`-second wall cap including the compiler and both
exact replay checks.  It runs in a new immutable source namespace and a new
output namespace.  The dedicated launcher passes the `box02_prefix` custody
profile; the remote runner refuses any other mode or resource tuple under
that profile and independently checks the exact DMI instance ID, hostname,
product, CPU count, and Singular binary.

At 2026-08-27T22:20:41Z Box02 had `2131032686592` bytes available, zero swap,
128 processors, and load averages `1.32,1.12,1.03`.  Its sole campaign CAS
process was the existing LF40 sequential `std/dp` Singular lane, at about
2.4 GiB RSS and one CPU.  That lane and all of its files are outside this
case and must remain untouched.  Its registered 900-GiB VM ceiling plus this
128-GiB ceiling still leaves approximately 1 TiB of physical capacity.

## Fail-closed gates

Immediately before copying source, the launcher must obtain the current
public IP from the exact instance ID and verify the pinned AWS state, type,
AMI, subnet, security group, AWS/local key fingerprints, and the remote DMI
identity.  It refuses unless all of the following also hold:

```text
swap used                    = 0 bytes
memory available             >= 298500227072 bytes
online processors            = 128
one-minute load average      <= 16.0
Singular /usr/bin binary SHA = pinned value above
source file set              = exactly SOURCE.sha256
remote tag namespace         = absent
```

The available-memory threshold is exactly the 128-GiB requested cap plus
150 GiB of protected host headroom.  The runner repeats the identity, CPU,
swap, headroom, tool, cap, source-coverage, and source-hash checks and records
the full prelaunch process table before executing the compiler.

The internal hard stops are the 128-GiB `ulimit`, one thread, a two-hour
global deadline, and a 120-second termination grace.  While live, the lane
must be observed at intervals no longer than 60 seconds.  Terminate this lane
only (never Box02 or LF40) if swap becomes nonzero, available memory falls
below 150 GiB, load exceeds 96 for three consecutive checks, LF40 shows a
resource or correctness hazard, a source/identity mutation is detected, or
an authoritative current lane returns a conclusive result that makes this
decision duplicate unnecessary.  Preserve stdout, stderr, metadata, return
codes, `/usr/bin/time -v` telemetry, and `EVIDENCE.sha256` in place; copy and
hash the complete terminal namespace before any later Box02 stop decision.

## Result status

A `PROPER` decision is not promotable without a complete rational
303-coordinate assignment and independent replay in all 513 literal raw
generators.  A `UNIT` decision only licenses a fresh tracked exact-`Q`
certificate; its cofactors must be composed into the 513 raw slots and
replayed exactly.  A timeout, memory stop, guard stop, incomplete stdout, or
modular result is telemetry only.
