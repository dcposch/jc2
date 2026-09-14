import pathlib,json,hashlib,re,datetime
root=pathlib.Path('/home/ubuntu/jc2/box/graded-moh-20260905')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
ans=[]
for sf in sorted((root/'runs').glob('*/status.json')):
 d=json.loads(sf.read_text());rec={k:d.get(k) for k in ('chart','host','ip','worker','pid','state','field','kind','order','representation','gauge','memory_gib','timeout_seconds','returncode','start_utc','end_utc','elapsed_seconds','command','input','input_sha256','solver_sha256')};rec['run']=sf.parent.name
 inp=pathlib.Path(d['input']);rec['input_hash_valid']=inp.exists() and sha(inp)==d['input_sha256']
 rec['outputs_valid']=True;rec['output_checks']=[]
 for fn,val in d.get('outputs',{}).items():
  p=sf.parent/fn;ok=p.exists() and p.stat().st_size==val['bytes'] and sha(p)==val['sha256'];rec['outputs_valid'] &=ok;rec['output_checks'].append(dict(file=fn,valid=ok,**val))
 sout=(sf.parent/'stdout.log').read_text(errors='replace') if (sf.parent/'stdout.log').exists() else ''
 rec['completion_markers']=[l for l in sout.splitlines() if len(l)<1200 and any(s in l for s in ('DONE','IDENTITY','PASS','FAIL','RESULT'))]
 rec['singular_error_lines']=[l[:300] for l in sout.splitlines() if l.lstrip().startswith('?')][:20]
 tim=(sf.parent/'time.txt').read_text() if (sf.parent/'time.txt').exists() else ''
 mt=re.search(r'Maximum resident set size \(kbytes\): (\d+)',tim);rec['peak_rss_kib']=int(mt.group(1)) if mt else None
 rec['disposition']='RUNNING' if d['state']=='RUNNING' else 'TIMEOUT_OPEN' if d.get('returncode')==124 else 'NEEDS_EXACT_REVIEW'
 stop=sf.parent/'manual-stop.json'
 if stop.exists():
  rec['manual_stop']=json.loads(stop.read_text());rec['disposition']='STOPPED_AFTER_CERTIFIED_N1_NONMEMBERSHIP'
 elif d.get('returncode')==0 and 'CURVE_N2_DONE NF_ZERO=1' in sout:
  rec['disposition']='PROJECTED_N2_ZERO_UNPROMOTED'
 ans.append(rec)
p=root/'resume-r2/run-summary.json';p.write_text(json.dumps(dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),runs=ans),indent=2)+'\n')
for d in ans: print(d['run'],d['state'],d['returncode'],d['disposition'], 'hashes',d['input_hash_valid'],d['outputs_valid'],'rss',d['peak_rss_kib'])
