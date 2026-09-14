# Installed FLINT documentary preflight — no arithmetic

Root registered metadata-only access in REGISTRATION.md (SHA
f10e2c28b046eebe991ec084171bdb69d9badc7ffa535d3e430aeffb649b63fa).
Its22:08 header is rounded; exact start request22:07:53 was made only after
independent22:23:00 STOP timer was confirmed active. Fresh EC2/DMI identity
matched i-08d2a40f272ee9fa2, Ownerf10-r1-exact-artifact-validation-20260909,
c7i.4xlarge, ip-172-30-0-72, diskvol-0574e0fa5aed1f5e3.
Standard quota1920; latest delayed usage212vCPU at22:05, not instantaneous
usage or billing. No other instance or volume touched.

All remote calls were short, foreground shell metadata operations. Installed
/usr/local/lib/python3.12/dist-packages/flint/__init__.py was read WHOLE:
its literal __version__ is0.9.0, matching distribution METADATA. Module SHA
2e5f8f1768d14eccd7961353c635195bd557f297edff8b8de09e2d211f03ec2d.
/usr/bin/python3 resolves to/usr/bin/python3.12, SHA
a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223.
No Python/version invocation, import, compiler, parser test, CAS or arithmetic.

rg is absent on the worker, so the failed rg metadata commands were replaced
by grep/find. /usr/lib/python3/dist-packages/flint is absent; the confirmed
installation is the/usr/local path above. These misses caused no install,
retry of mathematics, modification or engine fallback.

environment.json records100 exact absolute file pins:93 package/vendored
files (including existing pyc/stub files, excluding tests), six resolved
system native libraries/loader and one distribution METADATA. All100 hashes
matched a second complete pass22:11; interpreter matched again separately.
Only hashes were taken for native/binary files. No binary body was loaded.

readelf -d over every installed flint/*.so and python_flint.libs/*.so* found
the NEEDED union: libflint-6839011d.so.24.0.0,
libgmp-e0c82b6b.so.10.5.0, libmpfr-be332c05.so.6.2.2, libc.so.6,
libm.so.6, libpthread.so.0, ld-linux-x86-64.so.2. RPATH union was
$ORIGIN/../../python_flint.libs, $ORIGIN,
$ORIGIN/../../../.local/lib and$ORIGIN/../../../../.local/lib.
The latter two resolve from the installed module levels to the absent
/usr/local/lib/.local/lib. Python's ELF adds libz.so.1 andlibexpat.so.1.
readlink resolves all six system paths to the exact/usr/lib paths pinned;
ldconfig -p confirmed their default cache mappings. readelf on those six
adds only the already included libc andloader. No ldd/executable probing.

This is the declared installed-package/ELF dependency pin set, NOT an observed
import map, hermetic whole-OS/stdlib closure or installed-API success. Future
runtime must recheck every pin and resolved path, exact module/version and
its separately reviewed finite API/generic tests. No source acceptance or
mathematical dispatch is conferred here; no installation/fallback needed.

Root requested exact-worker STOP22:11:44 after post-hashes. Fresh EC2
STOPPED was confirmed22:12–13; only then was the22:23 backup canceled and
confirmed inactive22:13:57. Disk and all old artifacts retained; no files
were written on the worker by this task, no detached process or stop duty
remains. Capture is the root tool transcript plus these documentary records,
not a claimed independently signed remote receipt or measured computation.
