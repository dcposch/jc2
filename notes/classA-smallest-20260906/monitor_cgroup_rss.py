#!/usr/bin/env python3
"""Sample summed resident pages of every process in this systemd cgroup."""
import json
import os
import sys
import time
from pathlib import Path

output = Path(sys.argv[1])
stop = Path(sys.argv[2])
stop.unlink(missing_ok=True)
page_kib = os.sysconf("SC_PAGE_SIZE") // 1024
cgroup_rel = next(line.split(":", 2)[2] for line in Path("/proc/self/cgroup").read_text().splitlines())
cgroup = Path("/sys/fs/cgroup") / cgroup_rel.lstrip("/")
peak = samples = peak_pids = 0
started = time.monotonic()
while True:
    total = count = 0
    try:
        pids = (cgroup / "cgroup.procs").read_text().split()
    except OSError:
        pids = []
    for pid in pids:
        try:
            resident = int((Path("/proc") / pid / "statm").read_text().split()[1])
        except (OSError, ValueError, IndexError):
            continue
        total += resident * page_kib
        count += 1
    samples += 1
    if total > peak:
        peak, peak_pids = total, count
    if stop.exists():
        break
    time.sleep(0.2)
payload = {"source": "sum_proc_statm_rss_in_systemd_cgroup_200ms", "peak_rss_kib": peak,
           "peak_process_count": peak_pids, "samples": samples,
           "elapsed_seconds": round(time.monotonic() - started, 3), "cgroup": str(cgroup)}
temporary = output.with_suffix(output.suffix + ".tmp")
temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
temporary.replace(output)
