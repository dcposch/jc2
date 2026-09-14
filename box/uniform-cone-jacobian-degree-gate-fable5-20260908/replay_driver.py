import json,subprocess,hashlib,time,sys,os
box='/home/ubuntu/jc2/box/uniform-cone-jacobian-degree-gate-fable5-20260908'
chk=box+'/scratch/uniform-check.py'
modes=['positive','--omit-b4','--omit-b2','--wrong-euler-sign','--false-h0','--false-gcd-one']
runs=[];t0=time.time()
for opt in ([],['-O']):
    for m in modes:
        argv=['/usr/bin/prlimit','--cpu=25:25','--as=536870912:536870912','--','/usr/bin/python3','-I','-B']+opt+[chk,m]
        t=time.time()
        try:
            r=subprocess.run(argv,capture_output=True,text=True,timeout=30,cwd=box+'/scratch')
            rc,out,err=r.returncode,r.stdout,r.stderr
        except subprocess.TimeoutExpired as e:
            rc,out,err=-999,(e.stdout or ''),(e.stderr or '')
        errmsg=[l for l in err.strip().splitlines() if l.startswith('ValueError')]
        runs.append({'argv':argv,'seconds':time.time()-t,'rc':rc,'stdout':out,'stdout_sha256':hashlib.sha256(out.encode()).hexdigest(),'stderr_last':err.strip().splitlines()[-1] if err.strip() else '','stderr_error_lines':errmsg})
rep={'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'checker_sha256':hashlib.sha256(open(chk,'rb').read()).hexdigest(),'elapsed_seconds':time.time()-t0,'runs':runs}
json.dump(rep,open(box+'/replay-fable5.json','w'),indent=1)
print(json.dumps({k:v for k,v in rep.items() if k!='runs'}))
for r in runs: print(r['rc'],r['argv'][-2:],r['stdout_sha256'][:16],r['stderr_error_lines'])
