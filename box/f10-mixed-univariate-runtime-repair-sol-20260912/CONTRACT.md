# Mixed-univariate runtime repair — disabled source

This v2 derivative preserves the old six phases, unchanged CAPRUN and all old
caps. It is source-only, unexecuted, unreviewed, unregistered and creates no
worker or authority.

ROOT must mount one fresh 256MiB tmpfs at a canonical root-owned mode0755
mountpoint. Its only initial children are sibling `admin` (root:root0755,
initially empty) and `output` (exact registered nonzero UID, mode0700,
initially empty). The scientific UID cannot rename either sibling. Authorities,
negative inputs, and the frozen candidate are exclusively written root-owned
0444 beneath traversable `admin`; every stdout, stderr, telemetry, receipt,
producer output, cache and temporary path is beneath `output`. Deployment binds
HOME, TMPDIR, TMP, TEMP, XDG_CACHE_HOME and PYTHONPYCACHEPREFIX to `output`.
The qualification must prove the mount type/size and an exact final census;
the dispatcher does not infer those facts from pathname containment.

Registration v2 pins the dispatcher in addition to CAPRUN, probe, setpriv,
interpreter and the three scientific files. UID/GID are positive exact integers
(booleans refused); authority/producer/checker share one canonical scientific
directory; interpreter spelling is canonical. ROOT must select exactly
`PYTHON -E -s -S -B SCRIPT ...`, with no additional flags. The authority source
vector remains exactly authority/producer/checker/interpreter, as required by
the unchanged scientific authority code.

Parser control uses a duplicate top-level JSON key and requires CAPRUN
NORMAL_EXIT/child_exit1, exact empty stdout, exact stderr
`STOP: duplicate JSON key\n`, and absent output/receipt. Identity control
requires changed bytes/SHA, exact integer-rational A1+1 construction, exact
inverse restoration to original WHOLE bytes, CAPRUN normal child exit1, exact
stderr `STOP: CHECK FAILED: full polynomial Bezout identity\n`, and absent
output/receipt. Exception control multiplies all A1/A2/N by exactly 7t-12,
requires changed bytes/SHA and exact rational recurrence division restoring the
original WHOLE bytes, then requires normal child exit2 and a complete checker
result whose sole `exceptional_r` is `"2"`. A prior refusal, resource cap,
partial file, wrong text, missing inverse equality, or abnormal CAPRUN status
never covers a semantic control. Positive-check must first report no exception.

ROOT still must establish installed immutable ancestry, complete native/import
closure, one-cgroup containment/no delegation/no migration, fair-class-only
cpu.max semantics with burst zero, the separately armed original wall deadline,
memory.max's documented temporary-overshoot qualification, pre/post pins,
terminal cgroup emptiness, exact tmpfs census, durable readback and cleanup.
Hashed qualification is not worker authorization. Summary existence cannot
convert a failed control into success. No retry, second gcd, farm, cap increase
or automatic follow-on exists; any missing runtime fact is STOP/NONDECISION.
