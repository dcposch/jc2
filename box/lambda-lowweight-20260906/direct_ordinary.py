#!/usr/bin/env python3
"""Exact ordinary xy coefficient receiver, with original G variables and a wp solve map.
Large polynomials stay in the CAS; no TSV or expanded input file is written.
"""
import argparse,gzip,hashlib,json,pathlib,re,resource,signal,subprocess,time
O=pathlib.Path(__file__).resolve().parent;ROOT=O.parents[1]
AS=8321499136; RSS=8053063680

def wt(v,d):
 if v=='c':return d['n']+d['m']-1
 p,b,a=v.split('_');return (1 if p=='h' else int(p[1:]))*d['K']-int(a)
def xc(v,d):return d['ell']+1 if v=='c' else int(v.split('_')[1])
def specification(d,B,keller=False,solve=False):
 base=ROOT/'box/gi-only-20260905/classes'/d['class_id'];cl=json.loads((base/'class.json').read_text());bp=ROOT/cl['builder'];raw=bp.read_bytes();source=raw.decode()
 pin=json.loads((base/'solve/solve-result.json').read_text())['inputs']['builder']['sha256'];assert hashlib.sha256(raw).hexdigest()==pin
 names=re.search(r'ring R=0,\((.*?)\),\(',source).group(1).split(',');assert names==['y','x']+d['variables']
 setup=re.findall(r'^poly (?:h|AA\d+|BB\d+) = .*;$',source,re.M);assert len(setup)==1+d['e']+d['q']-1
 weights=[wt(v,d) for v in d['variables']];xweights=[xc(v,d) for v in d['variables']];D=d['n']+d['m']-1
 def vec(xs):return ','.join(map(str,xs))
 pair_terms=[('1',d['e'])]+[(f'AA{i}',d['e']-i) for i in range(1,d['e']+1)]
 q_terms=[('1',d['q'])]+[(f'BB{i}',d['q']-i) for i in range(2,d['q']+1)]
 chain=[f'matrix HC[1][{d["e"]+d["q"]+1}];']
 for av,ae in pair_terms:
  for bv,be in q_terms:
   chain += [f'HC[1,{ae+be+1}]=HC[1,{ae+be+1}]+diff({av},x)*diff({bv},y)-diff({av},y)*diff({bv},x);']
   if ae+be:
    chain += [f'HC[1,{ae+be}]=HC[1,{ae+be}]+{be}*({bv})*(diff({av},x)*diff(h,y)-diff({av},y)*diff(h,x))+{ae}*({av})*(diff(h,x)*diff({bv},y)-diff(h,y)*diff({bv},x));']
 chain += ['poly JP=0;int kk;',f'for(kk={d["e"]+d["q"]};kk>=0;kk--)'+ '{JP=JP*h+HC[1,kk+1];}',f'JP=JP-c*x^{d["ell"]};']
 checks=[]
 for seed in (1201,1207):
  values=[int.from_bytes(hashlib.sha256(f'{seed}:{v}'.encode()).digest()[:4],'big')%7-3 for v in d['variables']]
  ci=d['variables'].index('c');values[ci]=seed%5+1
  checks += [f'ring Num{seed}=0,(y,x),dp;',f'map ev=S,y,x,{vec(values)};', 'poly np=ev(pairP);poly nq=ev(pairQ);poly nj=ev(JP);',f'poly expect=diff(np,x)*diff(nq,y)-diff(np,y)*diff(nq,x)-({values[ci]})*x^{d["ell"]};','if(nj!=expect){print("NUMERIC_POLYNOMIAL_CHECK_FAIL");quit;}',f'if(nj==-diff(np,x)*diff(nq,y)+diff(np,y)*diff(nq,x)-({values[ci]})*x^{d["ell"]} || nj+1==expect)'+'{print("NEGATIVE_RECOMPOSITION_FAIL");quit;}',f'print("NUMERIC_POLYNOMIAL_CHECK_{seed}_PASS");','setring S;']
 lines=[f'ring S=0,({",".join(names)}),(lp(2),dp({len(names)-2}));','option(redSB);',*setup,
  f'intvec WY=1,0,{vec([0]*len(weights))};',f'intvec WX=0,1,{vec([0]*len(weights))};',f'intvec CWY=0,0,{vec(weights)};',f'intvec CWX=0,0,{vec(xweights)};','intvec NCWY=-CWY;intvec NCWX=-CWX;',
  'if(deg(h_0_0^2,NCWY)!=-2*deg(h_0_0,CWY)){print("NEGATIVE_WEIGHT_CONTROL_FAIL");quit;}',
  'poly pairP=h^'+str(d['e'])+'+'+'+'.join(f'AA{i}*h^{d["e"]-i}' for i in range(1,d['e']+1))+';',
  'poly pairQ=h^'+str(d['q'])+'+'+'+'.join(f'BB{i}*h^{d["q"]-i}' for i in range(2,d['q']+1))+';',
  'print("PAIR_READY");',*chain,
  'print("DIRECT_J_READY");',*checks,'kill pairP;kill pairQ;','matrix CM=coef(JP,x*y);','print("COEFFICIENTS_READY");','ideal Selected;poly recomposed=0;int jj;int yp;int xp;int ww;int fullterms=0;int selectedterms=0;int selectedcount=0;',
  'for(jj=1;jj<=ncols(CM);jj++){',
  'yp=deg(CM[1,jj],WY);xp=deg(CM[1,jj],WX);',f'ww={D}-yp;',
  'if(deg(CM[2,jj],WY)!=0 || deg(CM[2,jj],WX)!=0){print("COEFFICIENT_MAP_FAIL");quit;}',
  'if(deg(CM[2,jj],CWY)!=ww || deg(CM[2,jj],NCWY)!=-ww || deg(CM[2,jj],CWX)!=xp+1 || deg(CM[2,jj],NCWX)!=-xp-1){print("ROW_GRADE_FAIL");quit;}',
  'fullterms=fullterms+size(CM[2,jj]);recomposed=recomposed+CM[1,jj]*CM[2,jj];',
  f'if(ww<={B})'+'{Selected[size(Selected)+1]=CM[2,jj];selectedcount=selectedcount+1;selectedterms=selectedterms+size(CM[2,jj]);}',
  '}',
  'if(recomposed!=JP){print("RECOMPOSITION_FAIL");quit;}',
  'print("DIRECT_RECOMPOSITION_PASS");print("ROW_GRADES_PASS");print("TOTAL_ROWS="+string(ncols(CM)));print("TOTAL_TERMS="+string(fullterms));print("SELECTED_ROWS="+string(selectedcount));print("SELECTED_TERMS="+string(selectedterms));']
 extras=['T','Z','ss'] if keller else ['Z','ss'];cn=d['variables']+extras
 lines += [f'ring R=0,({",".join(cn)}),wp({vec(weights+[1]*len(extras))});',f'map fromSource=S,0,0,{",".join(d["variables"])};', 'ideal J=fromSource(Selected);','print("COEFFICIENT_RING_MAP_READY");']
 if solve:
  lp=ROOT/d['lambda_path'];lb=gzip.decompress(lp.read_bytes()) if lp.suffix=='.gz' else lp.read_bytes();assert hashlib.sha256(lb).hexdigest()==d['lambda_sha256'];lam=lb.decode().strip()
  lines += ['poly LL='+lam+';',f'J[size(J)+1]=Z*LL-ss^{d["W"]+1};']
  if keller and B>=d['n']+d['m']:lines += [f'J[size(J)+1]=T*c-ss^{d["n"]+d["m"]};']
  lines += ['option(redSB);',f'degBound={B};','print("INPUT_READY");','ideal G=std(J);print("STD_DONE");',f'poly nf=reduce(ss^{B},G);','print("NF_IS_ZERO="+string(nf==0));print("NF_IS_QUERY="+string(nf==ss^'+str(B)+'));print("BASIS_SIZE="+string(size(G)));print("RUN_COMPLETE");']
 else:lines += ['print("INPUT_READY");print("BENCHMARK_COMPLETE");']
 lines += ['quit;'];script='\n'.join(lines)+'\n'
 meta=dict(id=d['id'],class_id=d['class_id'],cutoff=B,solve=solve,keller=keller,original_builder_sha256=pin,coefficient_field='Q',source_variables=names,coefficient_variables=cn,coefficient_weights=weights+[1]*len(extras),coefficient_ring_map='source y,x -> 0; every original coefficient maps identically in declared order',jacobian_arithmetic='exact block product rule followed by Horner in h; independent numerical-polynomial derivative checks at two full assignments',row_presentation='literal ordinary xy coefficients of J(P,Q)-c*x^ell',script_sha256=hashlib.sha256(script.encode()).hexdigest(),script_bytes=len(script.encode()),source_setup_sha256=hashlib.sha256('\n'.join(setup).encode()).hexdigest())
 return script,meta

def rss(pid):
 todo=[pid];total=0
 while todo:
  p=todo.pop()
  try:
   total+=int(pathlib.Path(f'/proc/{p}/statm').read_text().split()[1])*4096
   for c in pathlib.Path(f'/proc/{p}/task').glob('*/children'):todo.extend(map(int,c.read_text().split()))
  except (FileNotFoundError,ProcessLookupError):pass
 return total

def run(d,B,seconds,keller=False,solve=False):
 script,meta=specification(d,B,keller,solve);tag=d['id']+'.ordinary'+('.keller' if keller else '')+f'.B{B}';log=pathlib.Path('/dev/shm')/('lambda-lowweight-'+tag+'.log');t=time.monotonic();peak=0
 import threading
 with log.open('wb') as out:
  p=subprocess.Popen(['prlimit',f'--as={AS}','--','/usr/bin/time','-f','PEAK_RSS_KIB=%M','Singular','-q'],stdin=subprocess.PIPE,stdout=out,stderr=subprocess.STDOUT,cwd=ROOT,start_new_session=True)
  errors=[]
  def send():
   try:p.stdin.write(script.encode());p.stdin.close()
   except BaseException as e:errors.append(repr(e))
  th=threading.Thread(target=send);th.start();stop=None
  while p.poll() is None:
   peak=max(peak,rss(p.pid))
   if peak>RSS:stop='RSS_CAP'
   elif time.monotonic()-t>seconds:stop='WALL_CAP'
   elif log.stat().st_size>65536:stop='LOG_CAP'
   if stop:oskill=signal.SIGKILL;__import__('os').killpg(p.pid,oskill);break
   time.sleep(.2)
  p.wait();th.join(timeout=2)
 text=log.read_text(errors='replace');m=re.search(r'PEAK_RSS_KIB=(\d+)',text)
 if m:peak=max(peak,int(m.group(1))*1024)
 meta.update(returncode=p.returncode,wall_seconds=round(time.monotonic()-t,3),peak_rss_bytes=peak,stop_reason=stop,emitter_errors=errors,stdout=text,input_ready='INPUT_READY' in text,benchmark_complete='BENCHMARK_COMPLETE' in text,run_complete='RUN_COMPLETE' in text,errors=bool(re.search(r'^\s*\?',text,re.M)) or 'FAIL' in text)
 for key,val in re.findall(r'^(TOTAL_ROWS|TOTAL_TERMS|SELECTED_ROWS|SELECTED_TERMS|NF_IS_ZERO|NF_IS_QUERY|BASIS_SIZE)=(\d+)$',text,re.M):meta[key.lower()]=int(val)
 meta['status']='PASS' if p.returncode==0 and not meta['errors'] and (meta['benchmark_complete'] or meta['run_complete']) else 'OPEN'
 final=O/(tag+'.json');tmp=final.with_suffix('.json.tmp');tmp.write_text(json.dumps(meta,indent=2)+'\n');tmp.replace(final);print(json.dumps({k:meta[k] for k in ['id','status','wall_seconds','peak_rss_bytes','input_ready','stop_reason','stdout']}),flush=True)
 return meta
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--id',required=True);ap.add_argument('--cutoff',type=int);ap.add_argument('--seconds',type=int,default=600);ap.add_argument('--solve',action='store_true');ap.add_argument('--keller',action='store_true');ap.add_argument('--emit',action='store_true');a=ap.parse_args();d=next(d for d in json.loads((O/'run_cases.json').read_text()) if d['id']==a.id);B=a.cutoff or 3*d['W']+3
 if a.emit:print(specification(d,B,a.keller,a.solve)[0],end='')
 else:run(d,B,a.seconds,a.keller,a.solve)
