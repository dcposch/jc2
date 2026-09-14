"""Tiny no-CAS integration probe: mocked host/context, REAL timer and exec."""
from datetime import datetime,timezone
import importlib.util,json,os,signal,sys,time
from pathlib import Path
from unittest.mock import patch
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import exact as E
import hybrid as H
old=sys.argv[1]=='old';mode=sys.argv[2]
path=HERE.parent/'d125-hybrid81-solver-prep-20260907/driver.py' if old else HERE/'driver.py'
spec=importlib.util.spec_from_file_location('probe_driver',path);D=importlib.util.module_from_spec(spec);spec.loader.exec_module(D)
fixture=HERE.parent/'d125-hybrid81-solver-gate-sol56-20260907/tiny-engine-fixture.jsonl'
E.need(E.digest(fixture.read_bytes())=='d00df83bafddcd3436dad44034bdb1680d306f6d67f8bfa83d4b32de19961bbf','fixture pin')
started=time.time();end=started+.75
a={'deadline_utc':datetime.fromtimestamp(end,timezone.utc).isoformat()}
actual_read=Path.read_bytes;actual_hybrid=H.read_hybrid;actual_exec=os.execve
def context(unused,phase):
    # Models delayed context/binary-pin handoff while the outer cap is stale.
    time.sleep(.20)
    return a,'a'*64,10
def read(path):
    if str(path)==f'/proc/{os.getppid()}/cmdline':return (D.CWD+'/run_capped.py').encode()+b'\0'
    return actual_read(path)
def tiny(data,production):
    E.need(production is True,'actual payload read mode')
    print(json.dumps({'marker':'PARSE_ENTER','utc':time.time(),'timer':signal.getitimer(signal.ITIMER_REAL)}),flush=True)
    time.sleep(.90 if mode=='parse' else .10)
    print(json.dumps({'marker':'PARSE_DONE','utc':time.time()}),flush=True)
    return actual_hybrid(data,production=False)
def exec_survivor(path,args,env):
    E.need(path=='/usr/bin/Singular','unexpected exec target')
    # Execute only Python, same PID: prints inherited timer before sleeping.
    code='import json,os,signal,time; print(json.dumps({"marker":"EXEC_ALIVE","pid":os.getpid(),"utc":time.time(),"timer":signal.getitimer(signal.ITIMER_REAL),"default":signal.getsignal(signal.SIGALRM)==signal.SIG_DFL}),flush=True); time.sleep(1.0); print("SURVIVED",flush=True)'
    actual_exec(sys.executable,[sys.executable,'-I','-B','-c',code],env)
print(json.dumps({'marker':'START','pid':os.getpid(),'pgid':os.getpgrp(),'utc':started,'deadline':end,'variant':'old' if old else 'repaired','case':mode}),flush=True)
# Repaired arm must correct both an ignored and blocked inherited disposition.
signal.signal(signal.SIGALRM,signal.SIG_IGN)
signal.pthread_sigmask(signal.SIG_BLOCK,{signal.SIGALRM})
with patch.object(D,'context',context),patch.object(D,'SOURCE',fixture),patch.object(D,'limits',lambda phase:None),patch.object(D,'observed_host',lambda:{'boot':'MOCK_ONLY'}),patch.object(Path,'read_bytes',read),patch.object(H,'read_hybrid',tiny),patch.object(D.os,'execve',exec_survivor):
    D.payload('NO_AUTHORITY_MOCK','decision')
