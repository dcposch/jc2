#!/usr/bin/env python3
"""open_triage.py -- which typed OPEN[...] tokens have no consumer lane?

Campaign-systems instrument (ideation-20260902T0022Z-opus5.md sec.8).
The measured bottleneck is workload generation, not compute; every typed
OPEN naming a decidable computation is idle inventory until some lane
prompt charges it.  Prints the orphan list, newest first.
"""
import glob, os, re, sys

TOK = re.compile(r"OPEN\[[A-Z0-9_-]+\]")
SKIP = "ideation-20260902T0022Z"


def main(root="xmodel"):
    raised = {}
    for f in glob.glob(os.path.join(root, "*.md")):
        if SKIP in f or f.endswith(".prompt.md"):
            continue
        with open(f, errors="ignore") as fh:
            for t in set(TOK.findall(fh.read())):
                raised.setdefault(t, []).append(os.path.basename(f))
    charged = set()
    for f in glob.glob(os.path.join(root, "*.prompt.md")):
        if SKIP in f:
            continue
        with open(f, errors="ignore") as fh:
            charged |= set(TOK.findall(fh.read()))
    orphans = sorted((max(v), k) for k, v in raised.items() if k not in charged)
    print("raised=%d charged=%d orphan=%d" % (len(raised), len(charged & set(raised)), len(orphans)))
    for src, tok in reversed(orphans):
        print("  %-46s %s" % (tok, src))


if __name__ == "__main__":
    main(*sys.argv[1:])
