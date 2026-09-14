#!/usr/bin/env python3
"""RSS watchdog: poll the whole descendant tree of ROOT_PID, kill above CAP_KIB."""
import json, os, signal, sys, time

root, cap_kib, interval, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]

def kids():
    seen, stack = set(), [root]
    while stack:
        p = stack.pop()
        if p in seen: continue
        seen.add(p)
        try:
            stack += [int(x) for x in open(f"/proc/{p}/task/{p}/children").read().split()]
        except Exception:
            pass
    return seen

def rss(pids):
    tot = 0
    for p in pids:
        try:
            for ln in open(f"/proc/{p}/status"):
                if ln.startswith("VmRSS:"):
                    tot += int(ln.split()[1]); break
        except Exception:
            pass
    return tot

peak, killed, t0 = 0, False, time.time()
while os.path.exists(f"/proc/{root}"):
    pids = kids()
    r = rss(pids)
    peak = max(peak, r)
    if r > cap_kib:
        killed = True
        for p in sorted(pids, reverse=True):
            try: os.kill(p, signal.SIGKILL)
            except Exception: pass
        break
    json.dump({"root_pid": root, "cap_kib": cap_kib, "peak_rss_kib": peak,
               "cur_rss_kib": r, "rss_killed": killed, "poll_interval_s": interval,
               "elapsed_s": round(time.time()-t0, 1), "running": True}, open(out, "w"))
    time.sleep(interval)
json.dump({"root_pid": root, "cap_kib": cap_kib, "peak_rss_kib": peak,
           "rss_killed": killed, "poll_interval_s": interval,
           "elapsed_s": round(time.time()-t0, 1), "running": False}, open(out, "w"))
