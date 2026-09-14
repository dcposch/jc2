#!/usr/bin/env python3
"""Independent exact symbolic differential and emitted-variable-map checks."""
import pathlib,json,re,subprocess,hashlib,time
ROOT=pathlib.Path('/home/ubuntu/jc2'); OUT=ROOT/'box/graded-moh-20260905/validation'; OUT.mkdir(exist_ok=True)
base=ROOT/'box/graded-moh-20260905/instrument'
results=[]
for aud in sorted(base.glob('*_audit.json')):
 d=json.loads(aud.read_text()); mp=ROOT/d['metadata_path']; meta=json.loads(mp.read_text()); stem=mp.stem
 native=ROOT/meta['builder']; source=native.read_text(); rows=pathlib.Path(d['rows_path'])
 ring=next(line for line in source.splitlines() if line.startswith('ring '))
 definitions='\n'.join(re.findall(r'^poly (?:h|AA\d+|BB\d+) = .*?;$',source,re.M))
 cf=meta['meta']['closed_form']; e,q,ell=cf['e'],cf['q'],cf['ell']
 aa=sorted(map(int,re.findall(r'^poly AA(\d+) =',definitions,re.M))); bb=sorted(map(int,re.findall(r'^poly BB(\d+) =',definitions,re.M)))
 P=f'h^{e}'+''.join(f'+AA{i}*h^{e-i}' for i in aa);Q=f'h^{q}'+''.join(f'+BB{i}*h^{q-i}' for i in bb)
 entries=[x.rstrip().split('|',4) for x in rows.read_text().splitlines()[1:]]
 assert len(entries)==d['row_count'] and all(int(x[1])==0 for x in entries)
 emitted='+\n'.join('('+r[4]+f')*x^{r[2]}*y^{r[3]}' for r in entries)
 script=ring+'\n'+definitions+f'\npoly P={P};\npoly Q={Q};\npoly J=diff(Q,x)*diff(P,y)-diff(Q,y)*diff(P,x)-c*x^{ell};\npoly EMITTED={emitted};\nprint("EXACT_FULL_DIFFERENTIAL="+string(J==EMITTED));\nprint("NEGATIVE_CONTROL="+string(J!=EMITTED+1));\nquit;\n'
 path=OUT/(stem+'.sing');path.write_text(script);start=time.time()
 r=subprocess.run(['Singular','--cpus=1','--threads=1','--flint-threads=1','-q','--no-rc',str(path)],capture_output=True,text=True,timeout=120)
 (OUT/(stem+'.log')).write_text(r.stdout+r.stderr)
 assert r.returncode==0 and 'EXACT_FULL_DIFFERENTIAL=1' in r.stdout and 'NEGATIVE_CONTROL=1' in r.stdout and '?' not in r.stdout,(stem,r.stdout,r.stderr)
 custody=json.loads((base/stem/'custody.json').read_text()); vmap=custody['msolve_variable_map']; inv={v:k for k,v in vmap.items() if k!='c'}
 for char in (0,1073741827):
  lines=(base/stem/f'slice_p{char}.ms').read_text().splitlines(); assert lines[0].split(',')==[vmap[v] for v in meta['variables'] if v!='c']; assert lines[1]==str(char)
  assert len(lines[2:])==len(entries)
  for original,renamed in zip(entries,lines[2:]):
   got=re.sub(r'\bv\d+\b',lambda m:inv[m.group()],renamed.rstrip(','))
   want=re.sub(r'\bc\b','1',original[4]); assert got==want
 results.append(dict(stem=stem,parameters=meta['parameter_count'],rows=len(entries),returncode=r.returncode,exact_full_symbolic_identity=True,negative_control=True,msolve_roundtrip_both_fields=True,elapsed_seconds=time.time()-start,source_builder_sha256=hashlib.sha256(native.read_bytes()).hexdigest(),rows_sha256=hashlib.sha256(rows.read_bytes()).hexdigest(),script_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
 print(json.dumps(results[-1]),flush=True)
 (OUT/'summary.json').write_text(json.dumps(results,indent=2)+'\n')
