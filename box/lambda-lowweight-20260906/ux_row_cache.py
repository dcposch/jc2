#!/usr/bin/env python3
"""Stream exact UX-coordinate quotients into temporary /dev/shm row caches.
The audited filter/audit function bodies are snapshotted from run_truncated.py.
Input and output rows are never retained in memory; arithmetic is exact over Q.
"""
import argparse,ast,hashlib,json,os,pathlib,re,resource,time
O=pathlib.Path(__file__).resolve().parent;ROOT=O.parents[1]
resource.setrlimit(resource.RLIMIT_AS,(200*1024**2,200*1024**2))
runner=(O/'run_truncated.py').read_text();tree=ast.parse(runner)
funcs='\n\n'.join(ast.get_source_segment(runner,x) for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in ('audit','ux_filter'))
ns={'re':re};exec(compile(funcs,str(O/'run_truncated.py')+'#audited-functions','exec'),ns);audit=ns['audit'];ux_filter=ns['ux_filter']
def atomic_json(path,data):
 tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(data,indent=2)+'\n');tmp.replace(path)
def do_case(c,ux):
 t=time.monotonic();sid=c['id'];source=ROOT/c['rows_path'];want=c.get('rows_sha256')
 if not want:
  p=ROOT/'box/gi-only-20260905/classes'/c['class_id']/'solve/solve-result.json';want=json.loads(p.read_text())['rows']['sha256']
 weights={v:(c['n']+c['m']-1 if v=='c' else (1 if v.startswith('h_') else int(v.split('_')[0][1:]))*c['K']-int(v.split('_')[2])) for v in c['variables']}
 xweights={v:c['ell']+1 if v=='c' else int(v.split('_')[1]) for v in c['variables']}
 z=ux['zero_variables'];assert all([xweights[v],weights[v]]==ux['zero_variable_bidegrees'][v] for v in z)
 source_sha=hashlib.sha256();cache_sha=hashlib.sha256();cofactor=hashlib.sha256();partition={}
 dest=pathlib.Path('/dev/shm')/f'lambda-lowweight-{sid}-UX-rows.tsv';tmp=dest.with_suffix('.tsv.tmp')
 meta=dict(schema='jc2.lambda.UX-row-cache/v1',case=sid,source_path=str(source),source_expected_sha256=want,cache_path=str(dest),UX_source_sha256=hashlib.sha256((O/'UX.json').read_bytes()).hexdigest(),UX_generators=z,valid_only_with_UX_generators_retained=True,coefficient_field='Q',coordinate_map='Listed UX coordinates -> 0; all other original coefficients including c -> themselves. Original structural h_power,x_power,y_power and source_index retained.',exact_identity='Every source row f minus cached row is sum(z*C_z); omitted zero rows therefore belong to UX. Cofactors obtained by the audited monomial partition.',runner_snapshot_sha256=hashlib.sha256(runner.encode()).hexdigest(),audited_functions_sha256=hashlib.sha256(funcs.encode()).hexdigest(),original_rows=0,cached_rows=0,zero_rows=0,original_terms=0,retained_terms=0,removed_terms=0,source_bytes=0,cache_bytes=0,maximum_input_buffer_bytes=0)
 with source.open('rb') as inp,tmp.open('wb') as out:
  def write(b):out.write(b);cache_sha.update(b);meta['cache_bytes']+=len(b)
  header=inp.readline(1024);assert header==b'source_index|h_power|x_power|y_power|expr\n';source_sha.update(header);meta['source_bytes']+=len(header);write(header)
  buffer=b'';state=None
  def process(chunk):
   if not chunk:return
   expr=chunk.decode().strip();assert expr
   meta['original_terms']+=audit(expr,weights,xweights,state['w'],state['x']+1)
   reduced=ux_filter(expr,z,cofactor,partition,state['key'])
   if reduced!='0':
    meta['retained_terms']+=audit(reduced,weights,xweights,state['w'],state['x']+1)
    if not state['wrote']:write(state['prefix']);state['wrote']=True
    elif not reduced.startswith('-'):write(b'+')
    write(reduced.encode())
  while True:
   part=inp.read(1<<20)
   if not part:break
   source_sha.update(part);meta['source_bytes']+=len(part);buffer+=part;meta['maximum_input_buffer_bytes']=max(meta['maximum_input_buffer_bytes'],len(buffer))
   while buffer:
    if state is None:
     pieces=buffer.split(b'|',4)
     if len(pieces)<5:break
     idx,h,x,y=pieces[:4];hh,xx,yy=int(h),int(x),int(y);w=c['n']+c['m']-1-hh*c['K']-yy;assert w>0
     state=dict(prefix=b'|'.join(pieces[:4])+b'|',key=idx.decode()+':'+str(hh)+':'+str(xx)+':'+str(yy),w=w,x=xx,wrote=False)
     buffer=pieces[4];meta['original_rows']+=1
    nl=buffer.find(b'\n')
    if nl>=0:
     process(buffer[:nl]);buffer=buffer[nl+1:]
     if state['wrote']:write(b'\n');meta['cached_rows']+=1
     else:meta['zero_rows']+=1
     state=None
    else:
     split=max(buffer.rfind(b'+'),buffer.rfind(b'-'))
     if split<=0:break
     process(buffer[:split]);buffer=buffer[split:];break
  assert not buffer and state is None
  out.flush();os.fsync(out.fileno())
 assert source_sha.hexdigest()==want,(sid,source_sha.hexdigest(),want)
 assert meta['cached_rows']+meta['zero_rows']==meta['original_rows']
 meta['removed_terms']=sum(partition.values());assert meta['original_terms']==meta['retained_terms']+meta['removed_terms']
 tmp.replace(dest)
 meta.update(status='PASS',source_actual_sha256=source_sha.hexdigest(),cache_sha256=cache_sha.hexdigest(),cofactor_partition_sha256=cofactor.hexdigest(),cofactor_partition_counts=partition,wall_seconds=round(time.monotonic()-t,3),peak_python_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 atomic_json(O/f'UX-cache-{sid}.json',meta)
 print(json.dumps({k:meta[k] for k in ('case','status','original_rows','cached_rows','original_terms','retained_terms','removed_terms','cache_path','cache_bytes','wall_seconds','peak_python_rss_kib')}),flush=True)
 return meta
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--ids',nargs='+',default=['C455','C341','C171','C109','R001','R002','R004']);a=ap.parse_args();cs={c['id']:c for c in json.loads((O/'run_cases.json').read_text())};xs={c['id']:c for c in json.loads((O/'UX.json').read_text())['cases']}
 for sid in a.ids:do_case(cs[sid],xs[sid])
