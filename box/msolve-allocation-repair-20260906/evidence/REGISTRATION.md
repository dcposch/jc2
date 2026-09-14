# msolve allocation repair registration

Owner: `/root/model_productivity`; coordinator `/root` retains instance custody.
Worker: `i-0da0cebfc97c9fd54`, `ip-172-30-0-56`, `172.30.0.56`.
Fresh root: `/home/ubuntu/msolve-allocation-repair-20260906` only.
Tag: `msolve-allocation-repair-astra-20260906`.
This is an instrument task; no frontier/mathematical result is asserted.

Payloads, sequential: dummy 3 s / 256 MiB; build + upstream tests 600 s /
16 GiB; tiny boundary + unit/proper controls 600 s / 16 GiB. At most 1200 s
build/test arithmetic. Reviewed CAPRUN/v1 exact-PGID runner, 1 s TERM grace.
Guard checks Linux, exact EC2 hostname/DMI, exact cwd, and task tag before
payload. No new dependencies/packages, installation, shared-build edits,
instance control, giant parser, or complete F4 invocation permitted.

Parent approval received at task start 2026-09-06 11:53Z; separate
different-model review is required before any giant-input replay.
