#!/usr/bin/env python3
"""Stream exact homogeneous Q/wp Jacobian rows into bounded Singular std.

No large generated input or basis is persisted. A homogeneous row is omitted
iff its positive y-deficit exceeds the requested cutoff. The affine localizer
Z*lambda-1 is homogenized as Z*lambda-ss^(W+1), wt(Z)=wt(ss)=1.
Test ss^B, not 1, for a dehomogenized unit certificate of degree at most B.
"""
import argparse, glob, gzip, hashlib, json, os, re, resource, signal, subprocess, threading, time
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
DRIVER_SHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
CAP=int(7.5*1024**3) # two simultaneous runs remain below the lane's 16 GiB
AS_CAP=int(7.75*1024**3)

def memory_limit():
    resource.setrlimit(resource.RLIMIT_AS,(AS_CAP,AS_CAP))

def persist_small(path,content):
    """Atomic small receipt; preserve a tmpfs copy if unrelated lanes fill disk."""
    temporary=path.with_name(path.name+'.tmp')
    try:
        temporary.write_text(content)
        temporary.replace(path)
        return str(path)
    except OSError as exc:
        temporary.unlink(missing_ok=True)
        if exc.errno!=28: raise
        fallback=Path('/dev/shm')/('lambda-lowweight-'+path.name)
        fallback.write_text(content)
        return str(fallback)

def vw(v,K,n,m):
    if v=='c': return n+m-1
    b,x,y=v.split('_')
    return (1 if b=='h' else int(b[1:]))*K-int(y)

def xw(v,ell):
    return ell+1 if v=='c' else int(v.split('_')[1])

def audit(expr, weights, xweights, expect_y, expect_x):
    count=0
    for term in re.split(r'[+-]',expr):
        if not term.strip(): continue
        wy=wx=0
        for name,expo in re.findall(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?',term):
            k=int(expo or 1); wy+=weights[name]*k; wx+=xweights[name]*k
        assert (wy,wx)==(expect_y,expect_x),(wy,wx,expect_y,expect_x,term[:160])
        count+=1
    return count

def ux_filter(expr,zero_order,digest,partition,key):
    """Exact monomial partition f-filter(f)=sum(z*C_z), no quotient guessing."""
    kept=[];zero_set=set(zero_order);rank={v:i for i,v in enumerate(zero_order)}
    for match in re.finditer(r'[+-]?[^+-]+',expr):
        term=match.group(0)
        hits=zero_set.intersection(re.findall(r'[A-Za-z][A-Za-z0-9_]*',term))
        if not hits:kept.append(term);continue
        z=min(hits,key=rank.get)
        pattern=r'(?<![A-Za-z0-9_])'+re.escape(z)+r'(?:\^(\d+))?(?![A-Za-z0-9_])'
        def divide(m):
            power=int(m.group(1) or 1)
            return '1' if power==1 else z if power==2 else z+'^'+str(power-1)
        cofactor,n=re.subn(pattern,divide,term,count=1);assert n==1
        digest.update((key+'|'+z+'|'+cofactor+'\n').encode())
        partition[z]=partition.get(z,0)+1
    return ''.join(kept).lstrip('+') or '0'

def process_rss(pid):
    total=0; todo=[pid]
    while todo:
        current=todo.pop()
        try:
            total+=int(Path(f'/proc/{current}/statm').read_text().split()[1])*4096
            for f in glob.glob(f'/proc/{current}/task/*/children'):
                todo.extend(map(int,Path(f).read_text().split()))
        except (FileNotFoundError,ProcessLookupError): pass
    return total

def run(case,N,seconds,keller=False,charge_zero=False,frontier=0,std_seconds=0,packed=False,ux=False,packed_max_exp=511):
    assert not (keller and charge_zero)
    assert not (frontier and charge_zero)
    assert not ux or (keller and not frontier and not charge_zero)
    assert not case.get('ux_cache_receipt') or ux, 'UX-filtered rows require all necessary coordinate generators'
    B=N*case['W']+3; cid=case['id']+('.keller' if keller else '.charge0' if charge_zero else '')+('.UX' if ux else '')+(f'.frontier{frontier}' if frontier else '')+(f'.packed{packed_max_exp}' if packed else ''); vars=case['variables']
    if frontier: assert 0<frontier<=B
    weights={v:vw(v,case['K'],case['n'],case['m']) for v in vars}
    xweights={v:xw(v,case['ell']) for v in vars}
    assert min(weights.values())>0
    result={'case':cid,'N':N,'W':case['W'],'cutoff':B,'margin':3,
            'driver_sha256':DRIVER_SHA256,'runner_pid':os.getpid(),
            'started_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
            'field':'Q','order':'wp(y-deficit,Z=1,ss=1)',
            'homogenized_localizer':'Z*lambda-ss^(W+1)',
            'query':f'ss^{B}','wall_cap_seconds':seconds,'rss_cap_bytes':CAP,
            'std_wall_cap_seconds':std_seconds or None,
            'virtual_memory_cap_bytes':AS_CAP,
            'input_rows':0,'selected_rows':0,'selected_terms':0,'selected_max_weight':None}
    result['keller_localizer']=keller
    result['charge_zero_target_component']=charge_zero
    result['frontier_weight']=frontier or None
    result['exponent_packing_maxExp']=packed_max_exp if packed else None
    result['temporary_exponent_bound']=2*B if packed else None
    result['necessary_attainment_UX']=ux
    ux_case=None;ux_digest=hashlib.sha256();ux_partition={}
    if ux:
        ux_bytes=(HERE/'UX.json').read_bytes()
        ux_case=next(c for c in json.loads(ux_bytes)['cases'] if c['id']==case['id'])
        for v in ux_case['zero_variables']:assert [xweights[v],weights[v]]==ux_case['zero_variable_bidegrees'][v]
        result['UX_source_sha256']=hashlib.sha256(ux_bytes).hexdigest()
        result['UX_generators']=[v for v in ux_case['zero_variables'] if weights[v]<=B]
        if case.get('ux_cache_receipt'):
            assert set(case['ux_cache_requires_coordinate_generators']) <= set(result['UX_generators'])
            cache_path=ROOT/case['ux_cache_receipt']
            cache_bytes=cache_path.read_bytes()
            assert hashlib.sha256(cache_bytes).hexdigest()==case['ux_cache_receipt_sha256']
            result['UX_row_cache_receipt']=str(cache_path)
            result['UX_row_cache_receipt_sha256']=hashlib.sha256(cache_bytes).hexdigest()
            result['original_rows_sha256']=case['original_rows_sha256']
            result['original_rows_path']=case['original_rows_path']
        result['UX_filtered_rows_zero']=0;result['UX_retained_row_terms']=0
    result['keller_row_weight']=case['n']+case['m']
    result['keller_row_selected']=keller and B>=case['n']+case['m']
    t0=time.monotonic(); log_path=HERE/f'{cid}.N{N}.log'
    live_log=Path('/dev/shm')/f'lambda-lowweight-live-{cid}.N{N}.log'
    errors=[]
    with live_log.open('wb') as output:
        proc=subprocess.Popen(['/usr/bin/time','-f','RESOURCE_PEAK_RSS_KIB=%M','Singular','-q'],stdin=subprocess.PIPE,stdout=output,
            stderr=subprocess.STDOUT,start_new_session=True,cwd=ROOT,preexec_fn=memory_limit)
        result['process_pid']=proc.pid;result['process_group']=os.getpgid(proc.pid)
        def emit():
            try:
                def send(s): proc.stdin.write(s.encode())
                extra=['T','Z','ss'] if keller else ['Z','ss']
                send('ring R=0,('+','.join(vars+extra)+'),wp('+','.join(map(str,[weights[v] for v in vars]+[1]*len(extra)))+');\n')
                if packed:
                    assert packed_max_exp in (255,511) and 2*B<=packed_max_exp//2
                    send(f'list PackList=ringlist(R);attrib(PackList,"maxExp",{packed_max_exp});def Packed=ring(PackList);setring Packed;\n')
                    send(f'if(char(basering)!=0 || nvars(basering)!={len(vars+extra)})'+'{print("PACKED_RING_FAIL");quit;}\n')
                    probe='+'.join(f'{i+1}*{v}' for i,v in enumerate(vars+extra))
                    send('setring R;poly ringProbe='+probe+';setring Packed;map packMap=R,'+','.join(vars+extra)+';\n')
                    send('if(packMap(ringProbe)!=('+probe+')){print("PACKED_MAP_FAIL");quit;}\n')
                    send('intvec DeclW='+','.join(map(str,[weights[v] for v in vars]+[1]*len(extra)))+';int checkWeight;\n')
                    send('for(checkWeight=1;checkWeight<=nvars(basering);checkWeight++){if(deg(var(checkWeight))!=DeclW[checkWeight]){print("PACKED_WEIGHT_FAIL");quit;}}\n')
                    send('print("PACKED_MAP_AND_WEIGHTS_PASS");\n')
                    send(f'poly exponentControl=ss^{B}*ss^{B};\n')
                    send(f'if(deg(exponentControl)!={2*B} || exponentControl!=ss^{2*B})'+'{print("PACKED_EXPONENT_FAIL");quit;}\n')
                    send('kill exponentControl;print("PACKED_EXPONENT_CONTROL_PASS");\n')
                send('option(redSB);\nideal J=0;\n')
                if ux:
                    for v in result['UX_generators']:send('J[size(J)+1]='+v+';\n')
                digest=hashlib.sha256()
                with open(ROOT/case['rows_path'],'rb') as handle:
                    digest.update(next(handle))
                    for raw in handle:
                        digest.update(raw)
                        idx,h,x,y,expr=raw.decode().strip().split('|',4)
                        h,x,y=map(int,(h,x,y)); w=case['n']+case['m']-1-case['K']*h-y
                        result['input_rows']+=1
                        if w>B or (frontier and w>frontier): continue
                        assert w>0
                        if charge_zero:
                            assert x+1>0
                            continue
                        result['selected_terms']+=audit(expr,weights,xweights,w,x+1)
                        result['selected_rows']+=1
                        result['selected_max_weight']=max(w,result['selected_max_weight'] or 0)
                        if ux:
                            expr=ux_filter(expr,result['UX_generators'],ux_digest,ux_partition,idx+':'+str(h)+':'+str(x)+':'+str(y))
                            result['UX_filtered_rows_zero']+=int(expr=='0')
                            if expr!='0':result['UX_retained_row_terms']+=audit(expr,weights,xweights,w,x+1)
                        if expr!='0':send('J[size(J)+1]='+expr+';\n')
                result['rows_sha256']=digest.hexdigest()
                if case.get('rows_sha256'): assert result['rows_sha256']==case['rows_sha256']
                if frontier:
                    result['frontier_rows']=result['selected_rows']
                    send(f'degBound={frontier}; ideal GF=std(J);\n')
                    send('if(size(reduce(J,GF))!=0){print("PREFIX_REDUCTION_FAIL");quit;}\n')
                    send('print("PREFIX_REDUCTION_PASS");J=GF;\n')
                    send('print("FRONTIER_READY");print("FRONTIER_BASIS_SIZE="+string(size(GF)));\n')
                    send('degBound=0;\n')
                    send('poly currentRow; poly reducedRow; int nReduced=0; int nZero=0; int nRemTerms=0;\n')
                    second=hashlib.sha256()
                    with open(ROOT/case['rows_path'],'rb') as handle:
                        second.update(next(handle))
                        for raw in handle:
                            second.update(raw)
                            idx,h,x,y,expr=raw.decode().strip().split('|',4)
                            h,x,y=map(int,(h,x,y)); w=case['n']+case['m']-1-case['K']*h-y
                            if not frontier<w<=B: continue
                            result['selected_terms']+=audit(expr,weights,xweights,w,x+1)
                            result['selected_rows']+=1
                            result['selected_max_weight']=max(w,result['selected_max_weight'] or 0)
                            send('currentRow='+expr+';\nreducedRow=reduce(currentRow,GF);\n')
                            send('nReduced++;if(reducedRow==0){nZero++;}else{J[size(J)+1]=reducedRow;nRemTerms=nRemTerms+size(reducedRow);}\n')
                    assert second.hexdigest()==result['rows_sha256']
                    send('print("PRE_REDUCED_ROWS="+string(nReduced));print("ZERO_REMAINDERS="+string(nZero));print("REMAINDER_TERMS="+string(nRemTerms));\n')
                    send('kill currentRow;kill reducedRow;\n')
                if case.get('lambda_path'):
                    lp=ROOT/case['lambda_path']
                    if not lp.exists() and lp.with_suffix(lp.suffix+'.gz').exists(): lp=lp.with_suffix(lp.suffix+'.gz')
                    lam=(gzip.open(lp,'rt').read() if lp.suffix=='.gz' else lp.read_text()).strip()
                else: lam=case['lambda']
                result['lambda_terms']=audit(lam,weights,xweights,case['W'],0)
                result['lambda_sha256']=hashlib.sha256(lam.encode()).hexdigest()
                if ux:
                    lp=ROOT/case['lambda_path'];raw=gzip.decompress(lp.read_bytes()) if lp.suffix=='.gz' else lp.read_bytes()
                    assert hashlib.sha256(raw).hexdigest()==ux_case['original_lambda_sha256']
                    lam=ux_filter(lam,result['UX_generators'],ux_digest,ux_partition,'lambda')
                    assert hashlib.sha256((lam+'\n').encode()).hexdigest()==ux_case['reduced_lambda_sha256']
                    result['UX_lambda_terms']=audit(lam,weights,xweights,case['W'],0)
                    result['UX_lambda_sha256']=hashlib.sha256((lam+'\n').encode()).hexdigest()
                    result['UX_cofactor_partition_sha256']=ux_digest.hexdigest()
                    result['UX_cofactor_partition_counts']=ux_partition
                send('poly LL='+lam+';\n')
                send('J[size(J)+1]=Z*LL-ss^'+str(case['W']+1)+';\n')
                if result['keller_row_selected']:
                    send('J[size(J)+1]=T*c-ss^'+str(case['n']+case['m'])+';\n')
                send('int dCut='+str(B)+'; degBound=dCut;\n')
                send('print("INPUT_READY");\nideal G=std(J);\n')
                send('print("STD_DONE");\nprint("BASIS_SIZE="+string(size(G)));\n')
                send('poly nf=reduce(ss^dCut,G);\nprint("NF_TERMS="+string(size(nf)));\n')
                send('print("NF_IS_ZERO="+string(nf==0));\nprint("NF_IS_QUERY="+string(nf==ss^dCut));\n')
                send('print("BASIS_WEIGHT_MAX="+string(deg(G)));\nprint("RUN_COMPLETE");\nquit;\n')
                proc.stdin.close()
            except BaseException as exc:
                errors.append(repr(exc))
                try: os.killpg(proc.pid,signal.SIGKILL)
                except ProcessLookupError: pass
        thread=threading.Thread(target=emit,daemon=True);thread.start()
        peak=0;stop=None;ready_at=None
        while proc.poll() is None:
            rss=process_rss(proc.pid); peak=max(peak,rss)
            if std_seconds and ready_at is None and 'INPUT_READY' in live_log.read_text(errors='replace'):
                ready_at=time.monotonic()
            if rss>CAP: stop='RSS_CAP'
            elif time.monotonic()-t0>seconds: stop='WALL_CAP'
            elif ready_at is not None and time.monotonic()-ready_at>std_seconds: stop='STD_WALL_CAP'
            elif live_log.stat().st_size>65536: stop='LOG_CAP'
            if stop:
                os.killpg(proc.pid,signal.SIGKILL);break
            time.sleep(.2)
        proc.wait();thread.join(timeout=2)
    result.update(wall_seconds=round(time.monotonic()-t0,3),peak_rss_bytes=peak,
                  returncode=proc.returncode,stop_reason=stop,emitter_errors=errors,
                  finished_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
    text=live_log.read_text(errors='replace')
    result['log_path']=persist_small(log_path,text)
    live_log.unlink(missing_ok=True)
    result['input_ready']='INPUT_READY' in text
    result['std_done']='STD_DONE' in text
    result['run_complete']='RUN_COMPLETE' in text
    result['singular_errors']=bool(re.search(r'^\s*\?',text,re.M)) or '_FAIL' in text
    result['prefix_reduction_pass']='PREFIX_REDUCTION_PASS' in text
    result['packed_exponent_control_pass']='PACKED_EXPONENT_CONTROL_PASS' in text
    for k,v in re.findall(r'^(BASIS_SIZE|NF_TERMS|NF_IS_ZERO|NF_IS_QUERY|BASIS_WEIGHT_MAX|FRONTIER_BASIS_SIZE|PRE_REDUCED_ROWS|ZERO_REMAINDERS|REMAINDER_TERMS)=(\d+)$',text,re.M): result[k.lower()]=int(v)
    result['frontier_ready']='FRONTIER_READY' in text
    actual_peak=re.search(r'^RESOURCE_PEAK_RSS_KIB=(\d+)$',text,re.M)
    if actual_peak: result['peak_rss_bytes']=max(peak,1024*int(actual_peak.group(1)))
    result['status']='COMPLETE_TRUNCATED_NONUNIT' if result['run_complete'] and not result['singular_errors'] and result.get('nf_is_zero')==0 else ('UNIT_CANDIDATE_NEEDS_COFACTORS' if result.get('nf_is_zero')==1 else 'OPEN_'+str(stop or 'ERROR'))
    result['completed_homogeneous_weight']=B if result['status'].startswith('COMPLETE_') else None
    receipt=persist_small(HERE/f'{cid}.N{N}.json',json.dumps(result,indent=2)+'\n')
    if receipt.startswith('/dev/shm'): print('FALLBACK_RECEIPT='+receipt,flush=True)
    print(json.dumps(result),flush=True)
    return result

def main():
    global CAP,AS_CAP
    ap=argparse.ArgumentParser();ap.add_argument('--cases',type=Path,required=True)
    ap.add_argument('--ids',nargs='*');ap.add_argument('--N',type=int,nargs='*',default=[1,2,3])
    ap.add_argument('--keller',action='store_true')
    ap.add_argument('--charge-zero',action='store_true')
    ap.add_argument('--frontier',type=int,default=0)
    ap.add_argument('--std-seconds',type=float,default=0)
    ap.add_argument('--packed',action='store_true')
    ap.add_argument('--packed-max-exp',type=int,choices=[255,511],default=511)
    ap.add_argument('--ux',action='store_true')
    ap.add_argument('--rss-gib',type=float)
    ap.add_argument('--as-gib',type=float)
    ap.add_argument('--seconds',type=float,default=240);args=ap.parse_args()
    if args.rss_gib is not None:
        assert 0<args.rss_gib<=16;CAP=int(args.rss_gib*1024**3)
    if args.as_gib is not None:
        assert 0<args.as_gib<=16;AS_CAP=int(args.as_gib*1024**3)
    cases=json.loads(args.cases.read_text())
    for case in cases:
        if args.ids and case['id'] not in args.ids: continue
        for N in args.N: run(case,N,args.seconds,args.keller,args.charge_zero,args.frontier,args.std_seconds,args.packed,args.ux,args.packed_max_exp)

if __name__=='__main__': main()
