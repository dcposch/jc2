#!/usr/bin/env python3
"""No-CAS descendant cleanup discriminator.  Never scientific output."""
import json, os, signal, sys, time
from pathlib import Path
if sys.argv != [sys.argv[0], "--descendant-rss-term-kill"]:
    raise SystemExit(64)
pid = os.fork()
if pid:
    os._exit(0)
signal.signal(signal.SIGTERM, signal.SIG_IGN)
payload = bytearray(64 * 1024 * 1024)
for i in range(0, len(payload), 4096):
    payload[i] = 1
raw_stat = Path("/proc/self/stat").read_text()
fields = raw_stat[raw_stat.rfind(")") + 2:].split()
identity = {"schema": "f10-mixed-dummy-identity/v1", "status": "DESCENDANT_READY",
            "pid": str(os.getpid()), "pgid": str(os.getpgrp()),
            "start_ticks": fields[19],
            "boot_id": Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
            "pid_namespace": os.readlink("/proc/self/ns/pid"),
            "cgroup": Path("/proc/self/cgroup").read_text(),
            "payload_bytes": str(len(payload))}
os.write(1, b"DESCENDANT_READY\n" +
         (json.dumps(identity, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii"))
while True:
    time.sleep(1)
