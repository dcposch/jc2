#!/usr/bin/env python3
"""No-CAS descendant cleanup discriminator.  Never scientific output."""
import json, os, resource, signal, stat, sys, time
from pathlib import Path, PurePosixPath
if sys.argv != [sys.argv[0], "--descendant-rss-term-kill"]:
    raise SystemExit(64)
pid = os.fork()
if pid:
    os._exit(0)
signal.signal(signal.SIGTERM, signal.SIG_IGN)
payload = bytearray(64 * 1024 * 1024)
for i in range(0, len(payload), 4096):
    payload[i] = 1
def need(ok, why):
    if not ok:
        raise ValueError(why)
def bounded(path):
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC)
    try:
        before = os.fstat(fd); need(stat.S_ISREG(before.st_mode), "nonregular metadata")
        raw = os.read(fd, 4097); need(len(raw) <= 4096, "metadata cap")
        after = os.fstat(fd); need((before.st_dev, before.st_ino, before.st_mode) ==
                                  (after.st_dev, after.st_ino, after.st_mode), "metadata identity drift")
        return raw.decode("ascii")
    finally:
        os.close(fd)
raw_stat = bounded("/proc/self/stat")
fields = raw_stat[raw_stat.rfind(")") + 2:].split(); need(len(fields) >= 20, "short stat")
raw_status = bounded("/proc/self/status")
def status_value(label):
    rows = [x.split(":", 1)[1].strip() for x in raw_status.splitlines() if x.startswith(label + ":")]
    need(len(rows) == 1, "status field"); return rows[0]
no_new_privs, cap_eff = status_value("NoNewPrivs"), status_value("CapEff")
need(no_new_privs == "1" and cap_eff == "0000000000000000", "privilege state")
uid, euid, gid, egid = os.getuid(), os.geteuid(), os.getgid(), os.getegid()
need(uid == euid and gid == egid and uid > 0 and gid > 0, "unprivileged identity")
raw_cgroup = bounded("/proc/self/cgroup")
rows = raw_cgroup.splitlines(); need(len(rows) == 1 and rows[0].startswith("0::/"), "single cgroup2 entry")
relative = rows[0][3:]; pure = PurePosixPath(relative)
need(str(pure) == relative and pure.is_absolute() and ".." not in pure.parts, "canonical cgroup path")
root = Path("/sys/fs/cgroup").resolve(strict=True)
cgroup_path = (root / relative.lstrip("/")).resolve(strict=True)
need(cgroup_path == root or root in cgroup_path.parents, "confined cgroup path")
cgstat = os.lstat(cgroup_path); need(stat.S_ISDIR(cgstat.st_mode), "cgroup directory")
names = ("cpu.max", "cpu.max.burst", "memory.max", "memory.swap.max",
         "cgroup.type", "cgroup.controllers", "cgroup.subtree_control")
controls = {name: bounded(str(cgroup_path / name)) for name in names}
need(controls["cpu.max"] == "80000 100000\n" and controls["cpu.max.burst"] == "0\n" and
     controls["memory.max"] == "34359738368\n" and controls["memory.swap.max"] == "0\n" and
     controls["cgroup.type"] == "domain\n" and controls["cgroup.subtree_control"] == "\n", "cgroup limits")
controller_tokens = controls["cgroup.controllers"].strip().split()
need(len(controller_tokens) == len(set(controller_tokens)) and
     all(x.isascii() and x.replace("_", "").isalnum() for x in controller_tokens), "controller list")
rlimits = {"cpu": [str(x) for x in resource.getrlimit(resource.RLIMIT_CPU)],
           "as": [str(x) for x in resource.getrlimit(resource.RLIMIT_AS)],
           "fsize": [str(x) for x in resource.getrlimit(resource.RLIMIT_FSIZE)]}
need(rlimits == {"cpu": ["3", "4"], "as": ["34359738368", "34359738368"],
                 "fsize": ["268435456", "268435456"]}, "rlimits")
identity = {"schema": "f10-mixed-dummy-identity/v2", "status": "DESCENDANT_READY",
            "pid": str(os.getpid()), "pgid": str(os.getpgrp()), "start_ticks": fields[19],
            "boot_id": bounded("/proc/sys/kernel/random/boot_id").strip(),
            "pid_namespace": os.readlink("/proc/self/ns/pid"),
            "cgroup_namespace": os.readlink("/proc/self/ns/cgroup"), "cgroup": raw_cgroup,
            "cgroup_path": str(cgroup_path),
            "cgroup_stat": {"device": str(cgstat.st_dev), "inode": str(cgstat.st_ino),
                            "mode": str(stat.S_IMODE(cgstat.st_mode)), "uid": str(cgstat.st_uid),
                            "gid": str(cgstat.st_gid)},
            "cgroup_controls": controls, "rlimits": rlimits, "uid": str(uid), "gid": str(gid),
            "no_new_privs": no_new_privs, "cap_eff": cap_eff, "payload_bytes": str(len(payload))}
os.write(1, b"DESCENDANT_READY\n" +
         (json.dumps(identity, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii"))
while True:
    time.sleep(1)
