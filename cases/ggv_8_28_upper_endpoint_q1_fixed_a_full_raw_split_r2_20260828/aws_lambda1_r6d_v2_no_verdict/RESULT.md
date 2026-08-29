# Lambda-one V2 compiler result

The preregistered lambda-one V2 job ran in the isolated r6d namespace with its
frozen 30-file source packet, passed source/preregistration/desk checks, and
entered only `COMPILE_LAMBDA1_ONLY`.  The compiler used one core for the full
2,700-second inner cap and exited 124:

```text
wall time       45:00.06
user time       2690.98 s
system time     8.65 s
maximum RSS     1,446,624 KiB
swaps           0
stdout/stderr   empty
partial files   none
terminal        NO_VERDICT_LAMBDA1_COMPILE
```

No lambda-one system JSON, reduction, modular screen, unit, survivor, or
certificate was emitted.  This is a target-faithful bounded compiler timeout,
not a mathematical conclusion and not authority to restart V2 unchanged.

Principal custody hashes:

```text
a129e215847396490b8d88daa68dc7eb1bb713832c83c57622915a1fd7e6b216  custody/JOB_ARCHIVE.tar.gz
a2bee657fc1d2014dc37e15e3e0e0062901487c03bf829adbd1264959b03a427  frozen SPLIT_SOURCE_V2.tar.gz
b0b6fc3a436818cfe2664a69c428d8bc77365126c93756832ee4b332c40947c6  output/TERMINAL
b8f26351aab87b44bfc619b19bf90c60299f6feba646341ae63c3ef50a4106e2  output/compile.time
e0b1dbe2beb5e546f8947da66c8bacb95eb3da904396873603dcc990927a6c52  records/FINAL_CENSUS.json
a57af1fb7a96bb065d1b6b6eec27cc90c0a7caf3213297c59062e103b35583a0  records/FROZEN_SOURCE.sha256
54d53e155b5836a42f02f8f934b5fc01d0f3b6aac7ac2e0bc90596bece42da81  EVIDENCE.sha256
```

All 66 archived files replay locally.  Worker rc is 124, monitor rc is zero,
and the final census at 2026-08-28T11:23:55Z has no group member and zero
swap.  Any successor based on a reviewed smaller order-four condition is a new
lane with a new preregistration; this archive itself proves no pole or `Q=0`
consequence.

