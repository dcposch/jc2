#!/usr/bin/env python3
"""Exact monomial certificate and Singular localizer controls on full constant-block Delta."""
import pathlib,json,re,gzip,hashlib,subprocess,time
OUT=pathlib.Path('box/lambda-lowweight-20260906')
rows=[]
for d in json.loads((OUT/'leaders.json').read_text()):
 raw=gzip.decompress(pathlib.Path(d['lambda_path']).read_bytes());assert hashlib.sha256(raw).hexdigest()==d['lambda_sha256']
 expr=raw.decode().strip();terms=re.findall(r'[+-]?[^+-]+',expr);positive=set();cofactor_counts={}
 for term in terms:
  vv=[v for v in re.findall(r'\b(?:A|B)\d+_0_\d+\b',term) if int(v.rsplit('_',1)[1])>0]
  assert vv,(d['id'],term)
  v=vv[0];positive.update(vv);cofactor_counts[v]=cofactor_counts.get(v,0)+1
 assert len(terms)==d['lambda_terms']
 def delta_var(m):
  v=m.group(0)
  return '0' if v.startswith(('A','B')) and int(v.rsplit('_',1)[1])>0 else v
 projected=re.sub(r'\b(?:h|A\d+|B\d+)_0_\d+\b',delta_var,expr)
 all_names=set(re.findall(r'\b(?:h|A\d+|B\d+)_0_\d+\b',expr))
 retained=sorted(v for v in all_names if v.startswith('h') or v.endswith('_0_0'))
 # Declare every h/scalar block coordinate, even if it is absent from lambda.
 K=d['K'];retained=set(retained)|{f'h_0_{a}' for a in range(K)}|{f'A{i}_0_0' for i in range(1,d['e'])}|{f'B{i}_0_0' for i in range(2,d['q'])}
 script='ring R=0,('+','.join(sorted(retained)+['Z','V'])+'),dp;\npoly lam='+projected+';\nprint("DELTA_LAMBDA="+string(lam));\nideal B=std(ideal(Z*lam-1));print("DELTA_UNIT="+string(B[1]==1));\nideal C=std(ideal(Z*V-1));print("NEGATIVE_PROPER="+string(reduce(1,C)!=0));\nquit;\n'
 t=time.monotonic();p=subprocess.run(['prlimit','--as=17179869184','--','Singular','-q'],input=script,text=True,capture_output=True,timeout=30)
 assert p.returncode==0 and '?' not in p.stdout and p.stdout.strip().splitlines()==['DELTA_LAMBDA=0','DELTA_UNIT=1','NEGATIVE_PROPER=1'],p.stdout
 # Independent ACTUAL unrestricted lambda localizer in the complete x-charge-zero ring.
 declaration=(OUT/(d['id']+'.derive.sing')).read_text().splitlines()[0]
 actual_vars=re.search(r'ring R=0,\((.*?)\),\(',declaration).group(1).split(',')
 actual_vars=[v for v in actual_vars if v not in ('y','hh')]
 assert all(v in actual_vars for v in all_names)
 actual_script='ring R=0,('+','.join(actual_vars+['Z'])+'),dp;\npoly lam='+expr+';\nideal I=Z*lam-1;ideal G=std(I);poly nf=reduce(1,G);\nprint("ACTUAL_BASIS_SIZE="+string(size(G)));print("ACTUAL_NF_ONE="+string(nf==1));print("ACTUAL_LOCALIZER_PROPER="+string(nf!=0));\nquit;\n'
 actual_start=time.monotonic()
 ap=subprocess.run(['prlimit','--as=536870912','--','/usr/bin/time','-f','PEAK_RSS_KIB=%M','Singular','-q'],input=actual_script,text=True,capture_output=True,timeout=60)
 assert ap.returncode==0 and '?' not in ap.stdout and ap.stdout.strip().splitlines()==['ACTUAL_BASIS_SIZE=1','ACTUAL_NF_ONE=1','ACTUAL_LOCALIZER_PROPER=1'],(d['id'],ap.stdout,ap.stderr)
 actual_control=dict(ideal='(Z*lambda-1)',coefficient_field='Q',variable_order=actual_vars+['Z'],order='dp',truncation='NONE: untruncated std on principal ideal',lambda_sha256=d['lambda_sha256'],returncode=ap.returncode,basis_size=1,normal_form_of_one=1,proper=True,stdout=ap.stdout,wall_seconds=round(time.monotonic()-actual_start,4),peak_rss_kib=int(re.search(r'PEAK_RSS_KIB=(\d+)',ap.stderr).group(1)),virtual_memory_cap_bytes=536870912)
 rows.append(dict(id=d['id'],lambda_sha256=d['lambda_sha256'],monomials=len(terms),all_monomials_divisible_by_positive_y_block_coordinate=True,retained_h_and_scalar_coordinates=sorted(retained),cofactor_partition_counts=cofactor_counts,identity='1=Z*sum(v*C_v)-(Z*lambda-1); each C_v consists of lambda terms assigned to their first positive-y block factor, divided by v',delta_lambda=0,delta_unit=True,negative_localizer_proper=True,actual_lambda_negative_control=actual_control,singular_stdout=p.stdout,wall_seconds=round(time.monotonic()-t,4)))
result=dict(schema='jc2.lambda.delta-controls/v1',coefficient_field='Q',coordinate_map='All positive-y A/B coordinates map to zero; all h coordinates and surviving scalar block coordinates map identically; terminal constant gauges remain zero.',status='PASS',total_monomials=sum(r['monomials'] for r in rows),cases=rows)
(OUT/'delta-controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','cases':len(rows),'total_monomials':result['total_monomials']}))
