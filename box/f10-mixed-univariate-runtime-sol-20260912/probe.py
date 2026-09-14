#!/usr/bin/env python3
"""No-CAS descendant cleanup discriminator.  Never scientific output."""
import os, signal, sys, time
if sys.argv != [sys.argv[0], "--descendant-rss-term-kill"]:
    raise SystemExit(64)
pid = os.fork()
if pid:
    os._exit(0)
signal.signal(signal.SIGTERM, signal.SIG_IGN)
payload = bytearray(64 * 1024 * 1024)
for i in range(0, len(payload), 4096):
    payload[i] = 1
os.write(1, b"DESCENDANT_READY\n")
while True:
    time.sleep(1)
