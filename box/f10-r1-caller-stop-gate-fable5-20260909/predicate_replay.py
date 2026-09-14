"""Metadata-only replay of the old vs proposed dummy identity predicate on frozen
event dictionaries. Reads only the pinned telemetry JSON. No imports of
dispatch_batch.py/probe.py, no fork, no signals, no /proc scan."""
import json, copy, sys, resource
resource.setrlimit(resource.RLIMIT_AS, (64*1024*1024, 64*1024*1024))
tele = json.loads(open(sys.argv[1]).read())
actual = tele["identity_checks"]
EXPECTED = [("before-term","MATCH",None),("before-term-send","SENT",15),
            ("before-kill","MATCH",None),("before-kill-send","SENT",9)]
def old(checks):   # dispatch_batch.py:99 frozen predicate
    return all(x.get("result")=="MATCH" for x in checks)
def proposed(checks):  # CALLER-FIX-PROPOSAL.md / .diff
    return [(x.get("stage"),x.get("result"),x.get("signal")) for x in checks]==EXPECTED
def strengthened(checks):  # proposed + MATCH cross-check + int-typed signal
    if not proposed(checks): return False
    for x in checks:
        if x["result"]=="MATCH":
            if not (x.get("observed_pid")==tele["pid"]==tele["pgid"]==x.get("observed_pgid")
                    and x.get("observed_start_identity")==tele["start_identity"]): return False
        else:
            if type(x.get("signal")) is not int or isinstance(x.get("signal"),bool): return False
    return True
def variant(name, fn):
    c = copy.deepcopy(actual); fn(c); return name, c
def swap(c,i,j): c[i],c[j]=c[j],c[i]
cases = [("ACTUAL", actual), ("EMPTY", []),
 variant("DELETE-before-term-send", lambda c: c.pop(1)),
 variant("DELETE-before-kill+send", lambda c: (c.pop(3), c.pop(2))),
 variant("REORDER-send-before-match", lambda c: swap(c,0,1)),
 variant("REORDER-kill-before-term", lambda c: (swap(c,0,2), swap(c,1,3))),
 variant("MISMATCH-before-kill", lambda c: c[2].update(result="MISMATCH")),
 variant("NOT_FOUND-before-term", lambda c: (c.__setitem__(0,{"stage":"before-term","result":"NOT_FOUND","utc":c[0]["utc"]}))),
 variant("GROUP_GONE-kill-send", lambda c: c.__setitem__(3,{"stage":"before-kill-send","result":"GROUP_GONE","utc":c[3]["utc"]})),
 variant("WRONG-SIGNAL-term=9", lambda c: c[1].update(signal=9)),
 variant("WRONG-SIGNAL-kill=2", lambda c: c[3].update(signal=2)),
 variant("SENT-without-MATCH", lambda c: c.pop(0)),
 variant("EXTRA-fifth-SENT", lambda c: c.append(dict(c[3]))),
 variant("STAGE-RENAMED", lambda c: c[0].update(stage="before-TERM")),
 variant("SIGNAL-AS-STRING", lambda c: c[1].update(signal="15")),
 variant("SIGNAL-AS-FLOAT-15.0", lambda c: c[1].update(signal=15.0)),
 variant("MATCH-FOREIGN-PID", lambda c: c[0].update(observed_pid=9999, observed_pgid=9999)),
 variant("MATCH-FOREIGN-START-IDENTITY", lambda c: c[2].update(observed_start_identity="boot=x;start_ticks=1")),
]
print("%-32s %-5s %-8s %-12s" % ("case","old","proposed","strengthened"))
for name, c in cases:
    print("%-32s %-5s %-8s %-12s" % (name, old(c), proposed(c), strengthened(c)))
